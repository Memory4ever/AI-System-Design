# Daily Research — 2026-10-13

**规范：** V3
**窗口：** 2026-10-12 ～ 2026-10-12
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-13T12:26:11+08:00

## 1. 结论

本日报只处理10月12日北京时间完整自然日。有限来源检查及贡献筛选已结束，冻结60个唯一材料家族（54个arXiv、6个官方说明/artifact）；59项完成必要证据审阅和Books判断，1项必要正文受阻。53项实际整合到27个章节，6项由现有具体论证承载；书稿改动均已经非写入者读核，整日报独立验收通过，普通可执行待办0。完成表示处理到合同允许的安全终态，不表示受阻正文、目录缺段或争议主张已获正面证明。

主要增量包括：推理缓存从“保结果”转向“保可重放输入”，把语义历史与物理驻留分开；模型表示/生成接口分别验收信息保留、可见性及消费协议；评价与Agent恢复保留真实分母、准入和失败退路。局部FLOPs、算子计时、统一形状、模型自报或检测分数都不能替代端到端质量、安全和控制验收。论文中的负侧、条件限制与旧方案已融入相应论证，不将较新方案默认升级为全局最优。

原始宽列表跨分类的648身份仅用于查漏，不是648篇已筛论文；本轮具名arXiv完整题摘58项，贡献前关闭4项，54项保留。T2Mem与Hide and Seek在最小core核验后纠正早期准入判断，现为正式候选/具体已有覆盖，不沿用旧排除标签。星期二不生成Weekly；按用户本轮授权，日报验收后再恢复历史来源补查，不把其进度计入本日报。

## 2. 来源覆盖

机构检查依据：[全球来源](../_sources/daily-20261013/global-sources.md)、[中国模型厂商](../_sources/daily-20261013/china-sources.md)。下表说明实际范围，不宣称互联网无遗漏；GitHub组织前缀只用于发现实际触发的变更，不代表全组织扫描。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI |Research index当前9张日期卡；最新10-07，止于窗前前缀；已检查；未确认当窗新事件| 已检查 | 不保证隐藏或删除条目 |
| SRC-ANTHROPIC |Research Publications当前10项；10-12两篇原文，止于10-09；已检查；两项进入必要审阅| 已检查 | 作者评价未完整披露，不当独立复现 |
| SRC-GOOGLE-AI |DeepMind Publications页1的30/265条，最新09-16；Research Blog页1最新10-07；EmbeddingGemma2实际原文10-06；可日期入口已检查；Google Pubs日级切片受阻| 受阻 | Pubs只有年份/venue，日级首次公开段隔离，不扩全年论文 |
| SRC-META-AI |Research提取为空后直取Blog与Publication；publication前12个日期位置最新10-02，之后混入旧年份；已检查可提取段；完整当窗目录受阻| 受阻 | 动态/混排及隐藏分页不支持当窗零研究保证 |
| SRC-QWEN |旧主页迁移至新Research，app壳及一次浏览器恢复失败；官方组织首10、qwen-code releases首5、Image commits首5；替代入口已检查；Research受阻| 受阻 | 发布页并非严格日期倒序，逐项核字段；动态Research日期段隔离 |
| SRC-DEEPSEEK |News当前5项、研究索引10项，最新分别09-10/06-24，止于窗前；已检查；未确认当窗新事件| 已检查 | 不扩组织旧仓库或完整版本史 |
| SRC-MOONSHOT |Blog完整可见26项；组织首10，MoonEP commits首5、kimi-code commits首10及releases首5，夹窗停止；已检查；具体修复核心关闭| 已检查 | 只支持这些有限入口，不授全组织保证 |
| SRC-TENCENT-HUNYUAN |Research官方publicList API，中英文各11/11、9/9；全部日期窗前；组织首10及触发的UniRL窄查询；已检查；一项进入必要审阅| 已检查 | 三个日期字段语义不同；不以repo updated替代论文公开日期 |
| SRC-ZAI |Research及release日期前缀最新08-26；组织首10与触发的zcode-plugins两条commit；已检查；UI插件组合具体关闭| 已检查 | 组织前缀不保证其余仓库无事件 |
| SRC-BYTEDANCE-SEED |论文Newest页1/13、20/242条，最新08-18；Blog前缀及featured原文实际08-05；VeOmni releases首5与5个当窗commit；已检查；不扩旧13页| 已检查 | 只验这些日期入口和相关变更，不授全论文审阅 |
| SRC-BAIDU-ERNIE |Blog页1/2的10项，最新05-09；Publication四项只有年份；唯一ERNIE release为2025-06-30；已检查日期入口| 已检查 | 年份目录无独立日级首公开保证 |
| SRC-XIAOMI-MIMO |Paper8项最新06-29；Blog15项，第一篇实际09-27；MiMo-Code release两项、当窗commit页1十条/页2一条短页停止；可日期入口已检查；其余无日期Blog隔离| 受阻 | 另外14篇无目录日期，不用来证明当窗零命中 |
| SRC-MINIMAX |中英文dated cards各当前段，最新08-13；Agent Tech Blog三项最新10-08；触发CLI及OpenAgentCore三次release；已检查；OpenAgentCore同一家族必要审阅| 已检查 | v0.0.10/11不是两家族；组织首10只是有限发现 |
| SRC-ARXIV |官方Mon12公告为公开日依据；model/multimodal/agents/systems主题查询首段分别100/100/53/10，前两query尾页分别76/276与63/263；相关新命名标题补检和具名题摘归并结束，具体范围见[runtime停止依据](../_sources/daily-20261013/runtime-evidence.md#有界-arxiv-发现的实际停止与归并) | 已检查 | 宽查询中未读部分不称已筛；有限主题检查不保证全分类召回。Dream to Remember必要正文受阻，见§5 |

## 3. 候选与判断

下列60个唯一家族为最终清单。评分只针对各材料的新增命题，不能由“能映射章节”倒推准入。arXiv公开日依据为Mon12官方公告批次，页面的Submitted Oct8/9不是公开日；定点核对既有10月1～12日报未发现这些arXiv身份的已处理重复。工程项目采用本窗merge/接口事件，release载体不重复计家族。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai) | 2026-10-12 | 部署容量与自主组合能力须在同模型/资源条件下相交；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，生命周期威胁的闭环资格 |
| [Strengthening our defenses against distillation attacks](https://www.anthropic.com/research/distillation-defenses) | 2026-10-12 | reasoning跨组织/模型消费与重复提取边界；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，隐藏reasoning消费授权 |
| [feat(managed-agent): admit public foreground Shell with mandatory approval](https://github.com/QwenLM/qwen-code/pull/13674) | 2026-10-12 | 关fresh admission不取消原回执与合资格收尾；1 + 2 + 2 = 5 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，Workspace准入/收尾分责 |
| [perf(minimax-h3): enable expandable allocator segments for trainside training](https://github.com/Tencent-Hunyuan/UniRL/pull/583) | 2026-10-12 | 同all-gather字节下allocator retry造成降速；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，具体瓶颈归因 |
| [fix(fs): treat absolute path.relative results as outside in contains](https://github.com/XiaomiMiMo/MiMo-Code/pull/2650) | 2026-10-12 | absolute relative跨卷结果不能认证containment；1 + 2 + 2 = 5 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，effect-time路径检查 |
| [Recover confirmed lost compute](https://github.com/MiniMax-AI/OpenAgentCore/pull/667) | 2026-10-12 | 确认exact compute loss才可释放writer并保留continuation；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，Resume资格 |
| [When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors](https://arxiv.org/html/2610.13910v1) | 2026-10-12 | 局部predicate信号不保证global consumer保留；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，关系写入/读取 |
| [Task Context Shapes Component Roles in Language Models](https://arxiv.org/html/2610.13895v1) | 2026-10-12 | 固定head身份不固定task-conditioned influence；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md)，组件诊断 |
| [Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection](https://arxiv.org/html/2610.13821v1) | 2026-10-12 | score学习/校准/release分责，ranking变好仍可能负utility；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，阈值评价 |
| [Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction](https://arxiv.org/html/2610.13672v1) | 2026-10-12 | cut位置和新turn边界是独立repair变量；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)，局部repair |
| [Multi-Stream Attention Residuals](https://arxiv.org/html/2610.13630v1) | 2026-10-12 | 单流持久source与多视角depth读出分离；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，depth-routing分支 |
| [ReplaySSM: Cache SSM Inputs, Not State](https://arxiv.org/html/2610.13778v1) | 2026-10-12 | input buffer令rollback成为cursor操作，并隔离低精read和高精recurrence；2 + 2 + 3 = 7 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，recurrent写回/回滚 |
| [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/html/2610.13708v1) | 2026-10-12 | required/optional residency与speculative union搬运分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，addressable history与HBM |
| [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/html/2610.13325v1) | 2026-10-12 | 高prefix hit仍暴露全文tokenization，exact IDs与graph容量分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-REQUEST-LIFECYCLE` [Ch42](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)，Frontend |
| [KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse](https://arxiv.org/html/2610.13060v1) | 2026-10-12 | 位置修正不恢复前文conditioning，segment hit可伴跨文档质量损失；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，非Prefix correction与exact回退 |
| [zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss](https://arxiv.org/html/2610.13605v1) | 2026-10-12 | dynamic codebook输入/输出几何、span位置与切分评分分责；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-TOKENIZER` [对应章节](../../../../books/part-02-model/11-tokenizer.md) |
| [Proactive Agentic Orchestration](https://arxiv.org/html/2610.13485v1) | 2026-10-12 | 同worker暂停/修订harness与可归因反馈；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [对应章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [From Structure to Validity: Mechanism-Guided Generation and Refinement of LLM Rubrics](https://arxiv.org/html/2610.13375v1) | 2026-10-12 | rubric树可组织leaf，不宜默认父节点剪枝；校准不能替语义有效性；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Host-Aware Web Crawling for LLM Pretraining Data](https://arxiv.org/html/2610.13321v1) | 2026-10-12 | 采集前host fetch-budget与发现/后过滤/训练收益分开；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DATA` [对应章节](../../../../books/part-04-training-system/27-data.md) |
| [Training User Simulators with Latent Intrinsic Feedback](https://arxiv.org/html/2610.13617v1) | 2026-10-12 | latent评价与下一utterance联合生成，但模拟reward不等真实用户评价；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-RLHF` [对应章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [Overcoming Data Imbalances with Expert Selection Biases](https://arxiv.org/html/2610.13370v1) | 2026-10-12 | category preferred expert share可独立data share，但撤除bias有失配；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-MOE` [对应章节](../../../../books/part-02-model/21-moe.md) |
| [What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training](https://arxiv.org/html/2610.12995v1) | 2026-10-12 | frozen task信息gain与current-policy KL投影两reference分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-SFT` [对应章节](../../../../books/part-04-training-system/29-sft.md) |
| [CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/html/2610.13257v1) | 2026-10-12 | 跨tokenizer span对应、chunk credit和无对应位置anchoring分开；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [对应章节](../../../../books/part-04-training-system/33-grpo.md) |
| [S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding](https://arxiv.org/html/2610.13202v1) | 2026-10-12 | 单response importance weight不能恢复其他组成员的比较人口；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [对应章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Unsupervised Multimodal Reward Modeling](https://arxiv.org/html/2610.12707v1) | 2026-10-12 | negative sampler/readout层与真实policy pool决定reward，不由benchmark唯一识别；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-RLHF` [对应章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [Prediction Is Not a Sufficient Memory State](https://arxiv.org/html/2610.13881v1) | 2026-10-12 | 当前predictor不一定是未来更新的充分state；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT` [对应章节](../../../../books/part-02-model/22-long-context.md) |
| [Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency](https://arxiv.org/html/2610.13835v1) | 2026-10-12 | 同facts的entity内顺序改变future更新成本与历史保留；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-PRETRAINING` [对应章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans](https://arxiv.org/html/2610.13303v1) | 2026-10-12 | 匹配rubric重写可提高judge一致而不提高human alignment；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Do Prompt Optimizers Break Requirements They Are Not Scored On? A Preregistered Study](https://arxiv.org/html/2610.13287v1) | 2026-10-12 | 上游截断/parser失败会被误计成多个独立内容退化；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling](https://arxiv.org/html/2610.13171v1) | 2026-10-12 | MH共享前缀预取可重排执行而不改接受核；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Scaling Agentic Data for Long-Horizon Terminal Intelligence](https://arxiv.org/html/2610.13166v1) | 2026-10-12 | 任务构造可能先替solver做完核心工作，test pass不足验收；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models](https://arxiv.org/html/2610.13041v1) | 2026-10-12 | 同shared block recurrent steps的精度次序受误差收缩约束；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs](https://arxiv.org/html/2610.13767v1) | 2026-10-12 | weight双尺度可被activation消费，不能把weight MSE称joint最优；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Rethinking the Roles of Diffusion and Decoding: Predictive-State Flows for Parallel Language Generation](https://arxiv.org/html/2610.12898v1) | 2026-10-12 | flow预测块前的predictive state，块内AR仍负责离散选择；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [On the Design Space of Continuous Diffusion Language Models](https://arxiv.org/html/2610.13834v1) | 2026-10-12 | one-hot flow训练vertices与denoiser simplex内部存在支持失配；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/html/2610.13912v1) | 2026-10-12 | policy与predictor修订须组件比较再成对保留；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents](https://arxiv.org/html/2610.13157v1) | 2026-10-12 | 来源声明一致性奖励不等观察到真实推理provenance；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/html/2610.13025v1) | 2026-10-12 | 持久evolver学harness编辑，任务executor并非权重自改；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [CompileMask: Bridging the Gap Between Expressiveness and Efficiency in Attention Masking](https://arxiv.org/html/2610.13474v1) | 2026-10-12 | bounded interval结构先编译，在线只填mask端点metadata；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [A Simplified Layout Algebra for GPU Kernels](https://arxiv.org/html/2610.13679v1) | 2026-10-12 | typed layout合法性、broadcast只读与restriction不可混为一类；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers](https://arxiv.org/html/2610.13735v1) | 2026-10-12 | local历史生产者与global输出查询双流可分摊prefill；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving](https://arxiv.org/html/2610.13328v1) | 2026-10-12 | MoE resident容量与batch-one decode读率必须分账；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [SlackSwap: Bandwidth-Aware Activation Swapping and Recomputation for Memory-Efficient DNN Training](https://arxiv.org/html/2610.13003v1) | 2026-10-12 | 隐藏offload容量受bandwidth×forward时间而非缺口字节支配；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Deploying RDMA for Large-Scale Inference and Training Workloads](https://arxiv.org/html/2610.12815v1) | 2026-10-12 | RDMA receive credit、在途bytes与fabric backpressure分责；1 + 2 + 2 = 5 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Ember: Making Unified Virtual Memory Practical for Discrete-Memory GPUs](https://arxiv.org/html/2610.13408v1) | 2026-10-12 | host-mapped默认与remote counters避免未知hot set临界thrashing；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Contextual Correction of Parallel Draftsfor Speculative Decoding](https://arxiv.org/html/2610.12570v1) | 2026-10-12 | parallel候选K²scoring与真实proposal分布分别验收；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [AutoIndexer: Flexible-Order Decoding by Training Causal Models on Chains of Edits](https://arxiv.org/html/2610.12545v1) | 2026-10-12 | 因果generation clock与可编辑display clock可以分离；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-DECODER-ONLY` [Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Chronos Policy: Learning Robot Policies on Physical Time](https://arxiv.org/html/2610.13929v1) | 2026-10-12 | capture time与action execution time应分别进入policy attention；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices](https://arxiv.org/html/2610.13740v1) | 2026-10-12 | 零padding仍吸收softmax mass，压缩应分depth/layout迁移；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos](https://arxiv.org/html/2610.13732v1) | 2026-10-12 | continuous latent transition与同flow expert换target须分阶段验收；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](https://arxiv.org/html/2610.13516v1) | 2026-10-12 | failure AUROC不等同state恢复的净操作价值；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/html/2610.12818v1) | 2026-10-12 | joint future/action flow需防clean-action泄漏并分direct/planner消费；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure](https://arxiv.org/html/2610.12544v1) | 2026-10-12 | finite ERM估计、结构近似与并行宽度共同决定masked输出误差；2 + 1 + 3 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [CacheScope: Exact-Compute Allocation for Training-Free Diffusion Acceleration](https://arxiv.org/html/2610.12530v1) | 2026-10-12 | input-normalized shallow probe分离轨迹移动与directional gain；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Dream to Remember: Continual Steering of Generalist Robot Policies with World Models](https://arxiv.org/html/2610.13816v1) | 2026-10-12 | 冻结generalist不消除steering遗忘，rehearsal需不同fidelity；2 + 2 + 2 = 6 | 受阻 | 暂缓：必要正文隔离，见§5；无Books采用 |
| [InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators](https://arxiv.org/html/2610.13944v1) | 2026-10-12 | 异构generator中途handoff需shared state与有限位移共同对齐；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/html/2610.13941v1) | 2026-10-12 | 冻结prompt encoder不等joint text residual不被image反馈改写；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LapMerge: Differentiable Exact-Budget Token Merging in Linear Time](https://arxiv.org/html/2610.13858v1) | 2026-10-12 | CDF equal-mass可恰好N聚合，但精确预算不等信息保真；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Test-Time Memory Construction](https://arxiv.org/html/2610.13348v1) | 2026-10-12 | query-time记忆构造可继续获取首次检索池之外的raw证据；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](https://arxiv.org/html/2610.13935v1) | 2026-10-12 | attribution proxy须随受控shortcut依赖变化验证，mask差额非自动faithfulness；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，cue-only falsifier、匹配扰动和OOD分轨 |

## 4. 证据与知识整合

本次阅读方法/关键评价及直接反侧，不默认遍历附件或旧版；当前已打开事件页的撤回/纠错信号纳入判断。论文证据为作者实验或理论，官方接口与artifact只证明相应公开实现；未运行代码、复现实验或验收生产能力。没有采用性能数字的段落不制造统一benchmark表；采用时只保相应配置，未披露条件不补造。

较长定位和对照：[机构证据](../_sources/daily-20261013/institution-evidence.md)、[模型证据](../_sources/daily-20261013/model-evidence.md)、[runtime证据](../_sources/daily-20261013/runtime-evidence.md)。以下逐项给出采用判断，正文与Review notes各有职责，不将论文列表搬到书稿。

### [AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)

官方10-12正文A/B、G及必要Appendix A～C/F：15台4GB Android盒上的Gemma4-26B-A4B部署，与外部服务器驱动GLM5.2、在八节点模拟环境部署Llama3.1-8B，是不同实验。简化访问、五次运行与当前capability floor/size ceiling未相交，不证明controller自身在目标硬件闭环复制；趋势预测不采用。Ch72生命周期威胁新增同模型能力、资源和实际新副本三重资格，保PP故障/KV重建/低并发代价，不扩写Memory章。

### [Strengthening our defenses against distillation attacks](https://www.anthropic.com/research/distillation-defenses)

官方Simple defenses/New methods/How well/Trade-offs给出reasoning消费组织/代际约束、两阶段检测及重复尝试成本。措施含更早实施日期，本窗是新公开说明，非全部措施首次发布。未披露评价分母/混杂控制，提取量、FPR和SWE数字只属厂商观察，不采用永久安全保证或对手归因。Ch72“Hidden Reasoning Trace不是Secrecy Boundary”已有用户/workspace/组织/会话/model-family消费授权，以及artifact admission与output hold分责，正文真实覆盖；实施/计费事实仅本报告保存，不制造Books diff。

### [feat(managed-agent): admit public foreground Shell with mandatory approval](https://github.com/QwenLM/qwen-code/pull/13674)

merge `a8990042e648a7807e251d99b3d37c0ee8c16100`的Store/Compiler/profile与admission tests：先取原key回执再拒fresh Shell，reserved内部profile不可由公有allowlist或跨policy重放取得。关闭准入仍保合资格approval/cancel/settlement，default-off不变；作者H2/特定CI不证明Windows、物理quiescence或完整生命周期。Ch84 Workspace处新增两段，明确部署开关与既受理收尾不同，不重复Ch81的effect对账。

### [perf(minimax-h3): enable expandable allocator segments for trainside training](https://github.com/Tencent-Hunyuan/UniRL/pull/583)

merge `279298dc8aa9d3a727c015fcf10fc0da90613871`的六patch与作者test/risk：1×8H20、torch2.13+cu130、H3 trainside近容量上限，1.3GB临时all-gather会触发allocator回收/retry/sync；相同字节不代表相同等待。开关默认false、进程级，HSDP验证配方关闭、VeOmni拒绝；与max_split512组合作者耗时约为原两倍，另一同代码报告缺allocator状态。局部timer未提交、IPC共享引擎未验，不排名训练框架。Ch36具体瓶颈段新增allocator归因与组合/兼容边界。

### [fix(fs): treat absolute path.relative results as outside in contains](https://github.com/XiaomiMiMo/MiMo-Code/pull/2650)

merge `8e1df4abee56da60c11db14606dd855823b1a29f`两contains/overlaps实现及新增test：跨drive/UNC的relative可能是absolute而非`..`，旧predicate因此fail-open。新拒absolute关闭这条具体路径；POSIX测试旧实现也绿，win32局部模拟非真实Windows acceptance，不能给symlink/TOCTOU或整个sandbox签字。Ch72 effect-time授权处新增跨平台containment反侧，保真实consumer检查与保守拒绝。

### [Recover confirmed lost compute](https://github.com/MiniMax-AI/OpenAgentCore/pull/667)

merge `48292f409a042e2b8bb8588c87e1e1a7004dc867`的Confirmed-compute-loss、idleCompute/releaseLostCompute和并发/negative tests：只有online owning node确认exact incarnation终止、cleanup成功、native continuation仍有效，再在Session lock里复核compute revision，才释放writer。offline/paused/unknown或并发新状态不授replacement；保filesystem/native ID/pending input，不重放旧input或偷偷建新root。v0.0.10/11是本窗载体，作者VM-loss验收不证明host-crash与任意crash-tail完整。Ch84 Resume新增资格与失败退路。

### [When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors](https://arxiv.org/html/2610.13910v1)

exact-v1 §3/4.2–4.4/Limitations：保持image不变、只改caption单概念，原caption训练probe、留出image-group测试，predicate与EOS/mean读出明显不同。局部识别编辑词不是完整空间绑定，text-only/有限模型和非线性边界保留；行为分数不能认证pooled representation。Ch23关系写入/读取处新增consumer、token/layer/pooling的独立验收和局部token/专用readout退路。

### [Task Context Shapes Component Roles in Language Models](https://arxiv.org/html/2610.13895v1)

exact-v1 §2/3/Fig2–5：同graph facts下改任务指令或内部task vector，局部扰动/恢复支持组件响应随条件改变；influence是下游响应，importance是答案margin的替换损失。路径可间接、选定sites/方向有限，少数head恢复只解释小部分task变化，不能推出唯一全局回路。Ch15诊断段新增task-conditioned角色与这两种干预量分责，保真实干预和非目标行为检查。

### [Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection](https://arxiv.org/html/2610.13821v1)

exact-v1 §3.4–3.6/4与E.1：Qwen3-14B无thinking、同greedy candidate、独立calibration set、三seed比较score学习与标量再校准。TriviaQA本域收益不等跨域资格；NQ未重校时selector仍负utility，低于always-abstain零基线；RL预算不同、调整区间跨零不证明无效。局部150-unit审查非全语义验收。Ch66阈值段新增score/calibration/release分账，保预定阈值与全部学习/评分成本。

### [Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction](https://arxiv.org/html/2610.13672v1)

exact-v1 §4–6、B/C必要模板：冻结reasoner，轻量gate与paragraph cut另训；保前缀，以同指令新user turn修后缀。inline/new-turn和位置对照支持conditioning差异，不把合成user role视为真实授权。相同最大generation次数不是同token、最终候选数或compute；数学/可验证任务及共享词表有限，误gate和重prefill付费。Ch80局部repair新增cut与角色边界两个变量，保不修改、整轮retry与独立verifier。

### [Multi-Stream Attention Residuals](https://arxiv.org/html/2610.13630v1)

exact-v1 §3.1–3.4、4.1–4.4/Eq9–17：从单流source按需构造因果多尺度视图，各自depth softmax，再融合单流子层输入。无conv与uniform mixer消融分开source diversity/fusion；persistent source/跨stage payload的O(Nd)不等所有retrieved states/访存免费。18B/28B MoE与10B消融有限，四scale iso-loss FLOPs拟合非wall-clock吞吐。Ch17 depth-routing新增读取视图与持久多流分支的区别，不改已有checkpoint接线。

### [ReplaySSM: Cache SSM Inputs, Not State](https://arxiv.org/html/2610.13778v1)

exact-v1 §3–7/Eq4–6/Alg1–3：缓存recent inputs，flush仅折叠committed prefix；tentative suffix被拒可移动cursor/覆盖，output-only不物化每draft state。高精checkpoint负责递推、低精副本只读，GDN还需保v并重算correction；当前output与高精路径仍有误差。四hybrid模型/单H100或B300/无TP/L16，B1收益近零，FP32性能与低精quality实验不拼成一项保证。Ch45 recurrent协议新增两段，保逐步物化分支。

### [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/html/2610.13708v1)

exact-v1 §2–3.5/4.1/4.3.1：required hot/tail/verification预算不可借，optional history只用余量；copy后ready、backup及旧readers完成后reclaim。多query合并miss搬运，不合并selector或causal mask。8×B300、GLM/DeepSeek特定TP与100K/500K配置：负载跃变填slot需53s而关闭optional为3s；decode-GPU归一化不含prefill，排首wave统计另计。Ch45 addressable-history段增placement生命周期/成本，不改原selector或一般SLO。

### [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/html/2610.13325v1)

exact-v1 §2–4/6.2–6.3/6.10/6.12：prefix hit之后仍需tokenization；family predicate、保序BPE和预分配graph必须保持完整reference IDs，token数/还原文本不够。五配置、单H100研究有限；NFC/config识别/truncation在graph外，Dynamo模拟关闭tokenizer-prefix cache，不证明多GPU端到端TTFT。Ch42 Frontend增tokenizer容量/语义合同，保safe-boundary复用、短输入CPU与fallback。

### [KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse](https://arxiv.org/html/2610.13060v1)

exact-v1 §2.1/3.2/4.1–4.4：unrotated K重施RoPE只改位置，不重算其旧前文attention；跨document质量下降，过滤相关文档只部分恢复且混杂文档数/内容。GPT-OSS-120B/H200/vLLM0.20/NVMe与合成Zipfian负载的hit不外推生产质量。具体已有覆盖：Ch45“非Prefix复用必须绑定Position-aligned Segment与Correction State”和下一KV intervention段已要求conditioning revision、approximate状态、选择性修正与exact重算退路；无需新增论文摘要。

### [zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss](https://arxiv.org/html/2610.13605v1)

exact-v1 §2–5/Eq3–4及F：在线LZW的prefix竞争使input/output hyper-encoder承担不同目标；size-aware位置和digits保护改变行为。四模型LoRA同配置仍有code/IF反退；canonical-prefix下target多view不是全文segmentation marginal，可逆codec不保证质量无损或端到端提速。Ch11联合行为接口新增这一分支，保固定canonical tokenizer。

### [Proactive Agentic Orchestration](https://arxiv.org/html/2610.13485v1)

exact-v1 §3.2–3.3/Eq3–8、4.1–4.5及B.2/E.3/G：worker主动带status/request/evidence暂停，orchestrator revision进入原local trajectory；仅归因足够的hint作self-teacher，外生新要求不归罪旧delegation，outcome另训。tool撤销/轮询对照支持有限连续性，只有一个active worker，API成本不含训练、重复次数不全对称。Ch82 clone/archive后新增mid-lifecycle分支，不授并发或最优成本。

### [From Structure to Validity: Mechanism-Guided Generation and Refinement of LLM Rubrics](https://arxiv.org/html/2610.13375v1)

exact-v1 §3.1–3.3/T1–4、4/5及B/C：Tree父routing漏检会遮蔽leaf，Path保语义context而不剪枝；Shuffled-Path控制并非仅增加字数。先检语义validity，再以独立responses测区分、跨judge一致和冗余。750偏好实例/两个judge、六response校准只是selection，人工gold/同源偏差和离线费用保留。Ch66 criterion段新增组织与执行分责。

### [Host-Aware Web Crawling for LLM Pretraining Data](https://arxiv.org/html/2610.13321v1)

exact-v1 §3–4、6.1/Limitations：已抓CC页面上模拟host先采样再加深；centrality与语言混杂，quality classifier yield不是真实训练效果。三样本和58M未抓估算依赖host未抓页相似，未执行live crawler，低分host仍可能贡献其他链接。Ch27 retention段新增采集预算与探索/多样性取舍，不把模拟yield当模型收益。

### [Training User Simulators with Latent Intrinsic Feedback](https://arxiv.org/html/2610.13617v1)

exact-v1 §3–5/T1–5及D：Gemma3模拟器联合生成thought/rating/reaction与utterance；WildChat提供话语，LES由Gemini合成，非真实心智。realism/critique/LES F1和assistant质量不全同步；下游Qwen2.5-1.5B三turn实验的三次sampling非三次RL训练，估算FLOPs不含模拟器制备/训练。Ch31真实反馈后新增环境/评分执行耦合及独立效标。

### [Overcoming Data Imbalances with Expert Selection Biases](https://arxiv.org/html/2610.13370v1)

exact-v1 §3/Eq6–11、5/T1–2、6/T5–6：bias只影响Top-K selection，gate仍用原score，K/专家数不增且跨类别可共享。345M–10.6B/特定mixture验证支持受限容量分配；强bias拔除严重退步、退火和保bias推理各有代价。token-equivalent估算非完整净节省。Ch21 specialization/load处新增软类别prior及无bias验收，不改global balancing。

### [What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training](https://arxiv.org/html/2610.12995v1)

exact-v1 §3/Eq4–20、4/T1–4：相同gold prefix给/不给task的reference likelihood差提出监督；empty input只是marginal近似。soft-target CE与weighted CE须detach才梯度等价，值不等价，分母不是随意sum weights。所测数学/代码有Pass反退，update norm小不排总尺度解释，预算/seed不完备不补造。Ch29条件监督后新增双reference、分母和退路。

### [CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/html/2610.13257v1)

exact-v1 §3/Eq1–11、4/T1–6：student uncertainty×teacher局部平滑度分signed credit，归一保chunk总advantage；异tokenizer仅anchor未对齐位置，同tokenizer全位置KL。smoothness不是teacher正确性、局部allocation最优不授无偏更新。uniform control匹配主要设置，但best checkpoint/额外SFT与scoring计费，更多rollouts/anchor非单调。Ch33 selective distillation新增alignment后credit与absence。

### [S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding](https://arxiv.org/html/2610.13202v1)

exact-v1 §3–6、C/F：own-response IS不一般恢复dense group-relative更新；sparse仅proposal，冻结snapshot、dense历史KV/full-layer verifier及exact residual sampling才能恢复相应独立组分布。8H100/DAPO/特定长数学rollout的stack收益非单机制因果；main dtype未披露，不借component BF16；小batch/短context可亏，denseKV不消失。Ch33组依赖处新增纠偏边界，基础speculation留Ch48。

### [Unsupervised Multimodal Reward Modeling](https://arxiv.org/html/2610.12707v1)

exact-v1 §2–3/Eq1–5/T1–8、5：冻结VLM中间层linear head、同图caption扰动提供监督；benchmark选layer用了标签，bootstrap亦用verifier labels。改policy自身comparison可改善caption选择却降低rewardbench；CHAIR兼label/metric只核COCO absent mentions，同源、长度shortcut及coupled BT/AdamW限制保留。Ch31相近候选处新增扰动head→policy-error比较分支，不称完全无监督或小全链成本。

### [Prediction Is Not a Sufficient Memory State](https://arxiv.org/html/2610.13881v1)

exact-v1 §2/Eq1–4/Theorem1、7/Prop7/Theorem8：continuous、unrestricted features/labels、exact cumulative ridge条件下，相同当前readout可在同next sample后分离；kernel ratio还需normalization mass。不是训练LLM失败或新RLS算法。Ch22实际S,z numerator/denominator及online ridge Gram/inverse段已保留下一次写入的统计责任；具体已有覆盖，理论验证只报告，不另造架构。

### [Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency](https://arxiv.org/html/2610.13835v1)

exact-v1 §3–6/Eq1–3/T2/Fig5–6：synthetic biographies相同records，entity内chron/shuffle可塑造specialist/generalist，旧history shuffle+近window chron是局部折衷。dated/undated目标不同，LoRA新值阈值不等自由生成全正确；拟合A与初gradient近似不是普适收敛定理，steps少不等生命周期省算力。Ch28目标扩展前新增data order与后续适配取舍。

### [Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans](https://arxiv.org/html/2610.13303v1)

exact-v1 §3–7/T3–4：相同editor/编辑数的随机对照、SummEval paired bootstrap与多重检验，agreement改善但alignment无可检测增益，不等统计等价；英文三数据集、gold噪声和provider混杂保留。Ch66 criterion/gold人口及judge spread非truth已实际承载，不增引用冒充整合。

### [Do Prompt Optimizers Break Requirements They Are Not Scored On? A Preregistered Study](https://arxiv.org/html/2610.13287v1)

exact-v1 §3–7/T1–6：严格JSON消费者与first-object评分抽取不同，200-token cap下共同extraction failure被记成多个内容失败；同prompt提高至1024的事后检查提供受限反解释，不证明优化器普遍安全。原stop reason缺失、少prompt clusters、输出预算费用近正文保留。Ch66五层成功表后已加入归因分责。

### [PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling](https://arxiv.org/html/2610.13171v1)

exact-v1 §3/Condition1/Alg1–2、Prop1必要假设、§5/D2–3：共享prefix条件成立时预取两种决策路径；defer保留随机输入，预测仅分预算，不代accept/reject。固定1024、单GH200、model-call计时不等完整SLO或有限MH已达stationary；废分支/KV另计。Ch20 Power-SMC之后新增该条件分支。

### [Scaling Agentic Data for Long-Horizon Terminal Intelligence](https://arxiv.org/html/2610.13166v1)

exact-v1 §2.2–4.3/F：public-only challenger检查实际工作缺口并重构，扩展任务依赖此前证据，不添加不可发现要求。1535 packages/Qwen3.5-27B/BF16/144H20训练为作者有限对照，未独立归因所有合成组件；长trace与模型过滤非真值。Ch27 executable环境管线后实际增加工作保留与公开视野边界；Science案例不采用。

### [RAMP: Recurrent Adaptive Mixed Precision for Efficient Prefill in Recurrent-Depth Language Models](https://arxiv.org/html/2610.13041v1)

exact-v1 §3–4/Theorems3.1–3.2及§6：局部收缩与统一误差界支持先低后高的bound排序，不证明全局最优。Huginn32步/H100仅first-prefill至logits，128/256输入反慢且不含网络/tokenization/decode。Ch49精度保护处已加入次序与旧统一精度回退。

### [DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs](https://arxiv.org/html/2610.13767v1)

exact-v1 §4/Alg1/Theorem1、§5：row/column weight重建，column逆作用activation；格式投影与坐标stationarity条件不等global optimum。GH200 fake MX/NV与4090 native INT4分开，activation量化和KV成本未省略。Ch49离线重建处已整合尺度消费接口。

### [Rethinking the Roles of Diffusion and Decoding: Predictive-State Flows for Parallel Language Generation](https://arxiv.org/html/2610.12898v1)

exact-v1 §2–3/Eq2–7/T1–3：shifted causal context不能读本块，joint state flow供并行block/内部AR，landing target不认证长程一致。OWT训练预算不等、states-only低PPL仍可损topic/coherence；操作数优势仅在大batch转吞吐。Ch24连续prior与离散读出已增加这条分工。

### [On the Design Space of Continuous Diffusion Language Models](https://arxiv.org/html/2610.13834v1)

exact-v1 §2–5/Eq3.1–3.7：DoubleCat扩展simplex内部训练支持，SemiCat提供可辨认clean条件；不增加network forward次数不等无额外成本。TinyGSM含预算/sampler变化，1.7B likelihood为proxy，OBQA与embedding迁移反侧保留。Ch24实际正文采用训练路径/可见token条件，不写外部commit机制。

### [RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/html/2610.13912v1)

exact-v1 §2.1/2.4–2.5/Eq10–18及代码/GUI必要评价：数据不足为Unknown，组件各自通过不代pair；update、gate和heldout人口分开。CodeContests200×3seeds、每轮4候选及capacity-matched verifier对照仅支持局部更新控制，全部训练/selection费另计。Ch25支持与policy revision处落实pair验收；AI for Science结果不采用。

### [SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents](https://arxiv.org/html/2610.13157v1)

exact-v1 §3.2/Eq2–6、§4/T2–4/AppB/D：query-only内部stream、检索stream与显式声明可被分别打分，exact-match/model judge只检一致，不授因果credit。Qwen2.5-3/7、E5/Wiki2018/top3条件保留；Eq6与AppD重复gamma的配方争议隔离不采用。Ch33 reward来源处已加入该分责。

### [Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](https://arxiv.org/html/2610.13025v1)

exact-v1 §3/恢复接口、§4.5–4.6/T5：同evolver不同role，真实edit应用后的匹配score差监督，last-applied prefix恢复仍需启动/任务验收。训练evolver对照为局部coding/memory证据，不证明递归持续增益；预训练、搜索与恢复成本保留。Ch80参数化诊断器之后已整合。

### [CompileMask: Bridging the Gap Between Expressiveness and Efficiency in Attention Masking](https://arxiv.org/html/2610.13474v1)

exact-v1 §2–4.4：互斥覆盖的结构条件、interval数量与forward/backward行列分责决定编译资格，descriptor不决定逻辑可见性。受限Blackwell对照native causal仍更快，训练收益不等operator峰值；SKU未披露。Ch49 mask执行计划处已增加结构编译和fallback。

### [A Simplified Layout Algebra for GPU Kernels](https://arxiv.org/html/2610.13679v1)

exact-v1 §2–7/Thm1必要范围、§9：logical/thread-value完整域与physical无alias不同，先组合完整view再取slice，合法映射未必affine。Rocq仅定义和decision procedure，CuTe/部分restriction有限测试，不授GPU速度或race freedom。Ch49 lowering处实际增加这些条件。

### [Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers](https://arxiv.org/html/2610.13735v1)

exact-v1 §3–5及必要A：共同训练local base/global output streams，仍保存全部KV；不是旧checkpoint直接mask flip。部分检索反退、128K另需20B继续训练、decode不普遍赢hybrid。Ch22访问图分支已增加重输入/轻输出适用性，不授减KV容量。

### [DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving](https://arxiv.org/html/2610.13328v1)

exact-v1 §3/Props1–2/§4–5：prefix-readable artifact的两相位read depth；同正routing frequency乘distortion/cost时局部取消，pooled/resident约束不继承。Qwen30B单模型质量、布局推算流量、prefix kernel未端到端测量，质量评价也未真分两相。Ch54 weight/KV读取交点后已整合，不能把read bpw当驻留节省。

### [SlackSwap: Bandwidth-Aware Activation Swapping and Recomputation for Memory-Efficient DNN Training](https://arxiv.org/html/2610.13003v1)

exact-v1 §2–4/Alg1及repair：留有限D2H预算给昂贵重建对象，再recompute其余，FIFO/EDF须守buffer与peak合同。仅单GPU无碎片DES/模型化DMA/A100 roofline，不是实机半显存或近理想吞吐。Ch36 host offload处实际加预算与no-swap回退。

### [Deploying RDMA for Large-Scale Inference and Training Workloads](https://arxiv.org/html/2610.12815v1)

exact-v1 §2.1/3–9：dedicated RQ、SRQ例外、RCQP completion与buffer生命期，hardware可靠不等Push重试exactly-once。推荐PS实测hardware-only尾更差、软件window后的观察不证明可禁PFC或LLM collective加速。Ch36 transport归因处已增加该控制边界，未核代码/复现。

### [Ember: Making Unified Virtual Memory Practical for Discrete-Memory GPUs](https://arxiv.org/html/2610.13408v1)

exact-v1 §3–8必要路径：counter看不到resident冷度，需启发式衰减/回迁保护；adaptive需UVM module，static需应用calls。有限LLM generation仍<3tok/s，稳定hot static/单scan mapped可更好。Ch54 UVM层级处已增加默认路径与权限/质量成本，不授serving SLO。

### [Contextual Correction of Parallel Draftsfor Speculative Decoding](https://arxiv.org/html/2610.12570v1)

exact-v1 §3–5、必要A/B/C/G及T10：首slot开始的prefix walk不等global argmax；确定选路为point mass，accept按target probability，reject残余排除该token。B200平均吞吐不是每suite优，Llama3.1-8B no-thinking MBPP仍弱于Domino/DFlash；训练/native draft长度不匹配保留。Ch48 parallel draft处已落机制与采样边界，不误归Q4。

### [AutoIndexer: Flexible-Order Decoding by Training Causal Models on Chains of Edits](https://arxiv.org/html/2610.12545v1)

exact-v1 §2–3/5/A1–3：marker/cursor与inverse edits训练，unrotated KV按display旋转，deleted span仅mask不物理free。精确性限新CoE语义，不等普通decoder重前向；单corruption free-generation repair远低于teacher-forced定位。Ch18多流之后实际整合，显示编辑不能撤销外部effect。

### [Chronos Policy: Learning Robot Policies on Physical Time](https://arxiv.org/html/2610.13929v1)

exact-v1 §3/Eq2–4及§4–5：time-aware RoPE保physical elapsed relation，temporal randomization不改timestamp；controller仍验deadline/丢stale动作。多传感无time增广可退，AddTime nominal也可胜，当前fixed action rate。Ch26 action chunk处已落时间与控制分责，不把时间查询当真实安全。

### [SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices](https://arxiv.org/html/2610.13740v1)

exact-v1 §3.2–3.3/§4/A5：zero text slots截短需恢复归一mass，保action位置，single-block删减不能推联合等价。400 LIBERO/单seed/16-action open-loop，长任务与texture反侧，不采用11×为全链同质量保证。Ch26单向WAM接口后已落压缩机制，移段保完整内容与阅读交接。

### [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos](https://arxiv.org/html/2610.13732v1)

exact-v1 §3.2–3.3/Eq1–8/§4.3–4.7：Gaussian posterior、感知/语义/flow目标→冻结mean target，再同head换human latent与robot action监督、mask padding。VQ消融仅LAM不独立证明robot因果，camera-relative变化非可独立自由度；视频/对齐/动作数据费计入。Ch26 forward/inverse分支后已整合。

### [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](https://arxiv.org/html/2610.13516v1)

exact-v1 §III/Eq1–5及§IV–V：完整simulator/policy checkpoint配对continue/recover，不刷新remaining deadline；false alarm/fresh attempt费用按renewal模型。恢复可反伤，所测primary monitor无人胜never-intervene，不推广监测无用或真实物理rollback。Ch26 monitoring处已加干预净收益边界。

### [LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/html/2610.12818v1)

exact-v1 §3.1–3.3/§4.1–4.4/T1–2/§5：state/noisy action/history masks各持可见性；SIGReg isotropy仅anti-collapse，goal另条件化。有限实机总体33.3%不全面胜DP38.9%，13.3×GFLOPs非墙钟。Ch25 latent dynamics处已落实proposal/rollout/refine与真实反馈分责。

### [Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure](https://arxiv.org/html/2610.12544v1)

exact-v1 §2–4.2/Eq18–24：有限词表/序列、MHMT近似、bounded模型类exact ERM、value-independent fixed-cardinality schedule与保留partition的expected KL界。不证SGD找到ERM或真实语言遵结构，小tree不自动小并行依赖；architecture依赖规模。Ch24 tau-leaping后实际增加finite learner条件，未遍历无关证明。

### [CacheScope: Exact-Compute Allocation for Training-Free Diffusion Acceleration](https://arxiv.org/html/2610.12530v1)

exact-v1 Method/Eq2–12、T1–2及B3/C/D5–6：固定probe/reconstructor、CFG两轨迹统计与exact anchor；低proxy不是global Jacobian或error bound，刷新近似latent不还原原轨迹。开发16校平均budget、test32固定阈值，LPIPS与SSIM可不一致；RTX PRO6000D，precision/batch/concurrency Not Disclosed。Ch24 cache段已加条件，全部校准/求值费保留。

### [Dream to Remember: Continual Steering of Generalist Robot Policies with World Models](https://arxiv.org/html/2610.13816v1)

exact-v1 完整精确v1官方题摘支持潜在准入，但必要正文未取得：exact HTML404、网页PDF超大，45s直取和一次有界后台恢复均只有不完整PDF，未解析/采用。作者摘要的性能数字不作正面证据；Ch25/26尚未作采用或已有覆盖判断，无Books写入。取得完整exact-v1或作者同版本全文后，只重开steering/rehearsal与匹配遗忘/新task对照。

### [InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators](https://arxiv.org/html/2610.13944v1)

exact-v1 §3.3–3.5/Eq3–14、§4/T1/5/7/8/§5：shared frozen VAE与兼容time是前提，LAE联合重建/状态/有限位移；state-only可collapse。Eq13/14自适应阈值口径与order-invariance不采用，重复roundtrip退；LAE/训练/多backbone驻留仍计费，硬件/precision/batch Not Disclosed。Ch24表示bridge后落实条件交接。

### [Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/html/2610.13941v1)

exact-v1 §2–3、必要D/F/G：聚合消息后的I2T/T2I定向缩放，保prompt的负reference与in-place分支不同。matched sign/paired image支持局部控制；A800/BF16/batch1下零额外NFE仍有0.31s局部额外时间，不授普遍自增强或真实内容。Ch24 guidance处实际整合，不取得新事实或用户目标。

### [LapMerge: Differentiable Exact-Budget Token Merging in Linear Time](https://arxiv.org/html/2610.13858v1)

exact-v1 §3/Eq3–6/Prop1声明及§4/5/D：给定mass/顺序的prefix/suffix scans线性，router排序额外MlogM；first moment保存非所有信息无损。GH200计时仅reducer、frozen Qwen2.5VL7B values替换仍有位置失配，overwide和调参ceiling反侧保留；临床不采用。Ch23 rate/distortion后已整合。

### [Test-Time Memory Construction](https://arxiv.org/html/2610.13348v1)

exact-v1 完整题摘后原贡献前排除被最小core纠正，保留改判依据。§3.1–3.2/Eq3–13/§4–5/T1–3/A3–5：offline metadata+backlink，SearchMeta未见池、ReadRaw已见source，构造/证据获取互驱；质量切片与总token可退，LazyMem backbone替换限制匹配。Ch77有预算关联回忆、late constructor、global未覆盖实体及lossless source实际完整覆盖，不重复写书。

### [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](https://arxiv.org/html/2610.13935v1)

exact-v1 §3/Eq1–7、§4–6及必要G/H：VLM检索概念图、定位/填补后比较黑盒output；caption使用gender-word概率，忽略无gender词，不是全输出truth。受控色块shortcut提供检验proxy是否追随真实行为依赖的有限反证，但body clean accuracy/四rates与Table11 gap/十一rates口径冲突，具体相关系数、显著性和整体优越均隔离不采用。Ch66实际attribution contract的estimand/assumptions、cue-only falsifier、匹配mask/output/replacement预算和zero/OOD分轨已完整承载剩余测量边界，具体已有覆盖，不因新工具名重复写书。

## 5. 缺口与下一步

本窗普通可执行待办：无。以下为终态保留项：已隔离的外部材料或争议主张保留精确重开条件，不支持正面证据、Books采用、性能/安全保证或无遗漏断言。

本窗外部保留项：Google Pubs日级首次公开目录、Meta动态/混排隐藏段、Qwen动态Research以及MiMo另14篇无目录日期Blog。当前可用替代入口已有限检查；缺口不支持正面证据、Books采用或“无遗漏”声明。取得官方本窗带日期列表/窗口快照，或具体材料的首次公开原件后，仅重开相应段/材料。

- [Dream to Remember — 2610.13816v1](https://arxiv.org/abs/2610.13816v1)：完整题摘已读、潜在贡献已确认；exact HTML404、网页PDF超大及两次有界直取均未取得完整正文。不完整PDF未解析，摘要性能不作正面证据，Books没有采用。需要完整exact-v1 PDF或作者对应全文，以核steering/noise、旧技能rehearsal、新task真实环境/想象切换、匹配遗忘及失败条件；到达后只重开此项与Ch25/26差额比较，不重新扫描全年。
- SOAR Eq6/AppD系数、InstantFusion Eq13/14自适应阈值及次序不变、Hide and Seek shortcut评价的clean/gap与rate人口冲突，只采用彼此独立且可支持的最小机制/测量边界；争议配方、统计数字和更强保证不进入Books。作者给出对应精确版本澄清时，定点重开这些被隔离主张，不影响已核的其他命题。

## 6. 复核

复核者：`today_institutions`（非报告作者；报告作者为root）。

结论：通过

实际完整核对本日报六部分、14来源与有限停止、全部60候选的准入/日期/评分、必要证据和Books处置；复用三研究作者的有效必要Source与root非writer实际正文/完整局部邻接/末注POST，53实际整合均在Review notes之前，6具体已有覆盖及1受阻隔离成立。没有无差别重读全部附件，也没有执行作者实验。

特殊排除信号直接检查14组/16事件的必要原件/受影响patch；普通排除按来源/理由抽检9样本/8来源，另核原池三篇完整题摘。T2Mem与HnS的早期误判已定点纠正，原宽池截断中段、其余ordinary与无关附件没有被冒称全量审阅。完整范围与修复依据见[独立DAY §14](../_sources/daily-20261013/institution-evidence.md#14-最终非报告作者六部分-day通过待作者同步完成字段)。

V3字段/一致性、60行及全部本地链接、正文绑定、围栏/尾空白、42项日期窗口测试、全局unstaged与cached `git diff --check`通过；脚本不证明研究语义。既有staged Ch69/LEARNING_STATE及并发历史修改保持，本轮未stage、commit或push。
