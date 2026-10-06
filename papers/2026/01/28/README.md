# Daily Research — 2026-01-28

**规范：** V3
**窗口：** 2026-01-27T09:00:00+08:00 ～ 2026-01-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T15:09:08+08:00

## 1. 结论

独立复核纠正了共同日期错因：Submitted不是公开，但官方公告schedule可提供最早公开下界；结合DataCite created的已可访问上界，93个arXiv事件包络完全落窗，原始时间精度及逐项包络见[DATE_BOUNDS](../_sources/daily-20260128/DATE_BOUNDS.json)。Updated/OAI metadata datestamp未用于公开时间。93是日期可支持事件数，不是贡献分母。

arXiv四主题API受限后，registration窄窗恢复377个去重发现线索，仅按相关题目定点完整读106个v1题摘；另2个非arXiv native核心说明，共108个唯一相关材料。当前候选已冻结64家族、贡献/范围关闭30、必要日期保留12；另KimiK2.5/MiniMax-M2-her两个非arXiv native日期保留。64/64家族已完成必要证据、Books处置及root实际逐项独立复核；21项受影响深入（含4项中心争议安全终态）、43项标准审阅。Books为2整合、5已有覆盖、53仅报告、4争议暂缓；整日报告六部分及来源停点/日期包络已获root独立语义验收通过。不将宽列表剩余标题追加为题摘/全文队列，改判只能由新证据或具体共同误理由驱动，不能由审阅成本或Books覆盖驱动。

Kareus频率改变overlap资源/launch最佳点的联合时间—能耗条件已整合Ch36，并保留小work/profiling/static回退与physical/emulation分界。知识编辑locality指标自身的GT/teacher-forcing/contrastive混杂已深入限定审阅，实际整合Ch66两段并获root非作者POST通过；端侧profile不整段上传但改写prefix回传的隐私边界，在Ch72具体filter/observable-channel正文已有覆盖。Acoustic Field Video、disability paired evaluation、多数树模型、JaxARC、PEAfowl、dLLM-ASR与VSA等限定标准结论已分批获独立通过；RobustPrivacy同一classifier的‘扩大preimage’中心主张与定义冲突，争议终态不进Books。逐项必要审阅、Books落实及日级独立验收均已完成；14个日期保留项、历史目录缺口及4个中心争议明确隔离，不授正面Coverage/Evidence/Books Gate、无遗漏或性能/安全保证。[逐项源锚点与反侧](../_sources/daily-20260128/REVIEWS.md)保留实际读到的位置，不用完整AB代替证据审阅。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | news RSS403，Prism原介绍web恢复，产品/科学写作组合无新机制；[停点](../_sources/daily-20260128/SOURCE_STOPS.md) | 受阻 | 历史Research目录不可恢复，终态隔离，不声称无遗漏 |
| SRC-ANTHROPIC | Research403，Jan27原域查询只恢复GOV.UK商业合作 | 受阻 | 无当窗历史研究目录，终态隔离 |
| SRC-GOOGLE-AI | Research Jan2026月页标题段完整读完；ATLAS/agent-scaling核心原说明与旧论文身份核验；DeepMind current blog | 受阻 | 两篇blog无本次新增机制；DeepMind历史列表未恢复，终态隔离 |
| SRC-META-AI | official Research仅57字响应，非有效研究目录 | 受阻 | 历史目录/原发布缺失，终态隔离 |
| SRC-QWEN | 旧github入口最新2025-09-23、redirect线索与定点查询 | 受阻 | 无Jan2026完整历史dated目录，终态隔离 |
| SRC-DEEPSEEK | 首页+news429，web primary精选10篇恢复OCR2及其v1 | 受阻 | OCR2 native Jan28仅日精度；历史完整目录缺失，终态隔离 |
| SRC-MOONSHOT | platform旧blog，K2.5原tech blogweb恢复、官方model/help日精度 | 受阻 | K2.5必要first public区间未明，终态隔离 |
| SRC-TENCENT-HUNYUAN | Research脚本壳；浏览器按首查要求实际两次超时 | 受阻 | “全部”dated研究目录未读到，终态隔离 |
| SRC-ZAI | official Research15条时间顺序读到2025-12-09，Jan19与Feb2之间无条目 | 已检查 | 无；只支持该入口可见排序区间 |
| SRC-BYTEDANCE-SEED | Research10篇精选含Jan27Keel，paper目录当前18条，Keel原publication+v1 | 受阻 | Keel日精度日期；历史完整目录缺失，终态隔离 |
| SRC-BAIDU-ERNIE | 第1页10条，Jan29→Jan15→Jan8覆盖排序区间，下一页更旧2025年 | 已检查 | 无；只支持该入口对应排序区间 |
| SRC-XIAOMI-MIMO | 当前首页与Jan2026原域窄query | 受阻 | 无历史Paper/Blog dated目录，终态隔离 |
| SRC-MINIMAX | blog12条，Jan27M2-her被Feb12/Dec23夹住，核心说明可读 | 受阻 | native仅日期，JSON-LD午夜未证明实际first public，终态隔离 |
| SRC-ARXIV | model/multi/agent/system API429；DataCite窄registration2/1/2/1页；CL/LG/CV/DC/AI相关标题有限补检，106定点v1AB读完；schedule+created为93事件建立完整包络 | 受阻 | 老Submitted10项、nativeKeel/OCR2日期保留；不称零命中/全分类召回，普通候选证据另列 |

所有请求URL、原响应、分页/停止范围、恢复条件集中于[来源停点](../_sources/daily-20260128/SOURCE_STOPS.md)和[发现/筛选记录](../_sources/daily-20260128/SCREENING.md)。未扫描每周来源；辅助搜索只作有限身份恢复。

## 3. 候选与判断

当前通过具体原增量准入64项，清单已经冻结。完整逐项身份及判断以[SCREENING](../_sources/daily-20260128/SCREENING.md)为维护入口；评分/必要证据与Books处置已按[REVIEWS](../_sources/daily-20260128/REVIEWS.md)落实；64项独立必要复核已通过，中心争议仍保留暂缓，不被完成计数掩盖。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Acoustic Field Video for Multimodal Scene Understanding](https://arxiv.org/abs/2601.17123v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:42:32Z | 声压场overlay补充RGB/stereo丢失的声源可见性；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Learning to Collaborate: An Orchestrated-Decentralized Framework for Peer-to-Peer LLM Federation](https://arxiv.org/abs/2601.17133v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:42:46Z | 中央profile匹配与P2P teacher文本的暴露边界；2+2+2=6 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning](https://arxiv.org/abs/2601.17261v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:45:44Z | activation子空间ZO仅conditioned目标与能量条件；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Latent-Space Contrastive Reinforcement Learning for Stable and Efficient LLM Reasoning](https://arxiv.org/abs/2601.17275v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:46:02Z | latent预筛成本与全decode、冻结权重零遗忘保证冲突；2+1+2=5 | 争议 | 暂缓：中心保证争议，见§5 |
| [Phase Transition for Budgeted Multi-Agent Synergy](https://arxiv.org/abs/2601.17311v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:46:53Z | 多数树相关误差与有损通信的small-signal预算相变；2+2+2=6 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Conformal Feedback Alignment: Quantifying Answer-Level Reliability for Robust LLM Alignment](https://arxiv.org/abs/2601.17329v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:47:18Z | CP集合用于偏好权重但marginal覆盖不认证真值；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Power-based Partial Attention: Bridging Linear-Complexity and Full Attention](https://arxiv.org/abs/2601.17334v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:47:25Z | 偏移幂律稀疏mask的固定window/复杂度分支；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Are We Evaluating the Edit Locality of LLM Model Editing Properly?](https://arxiv.org/abs/2601.17343v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:47:36Z | 编辑locality的GT、teacherforcing与contrastive混杂；3+1+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [编辑locality两段](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Shadow Self: Intrinsic Value Misalignment in Large Language Model Agents](https://arxiv.org/abs/2601.17344v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:47:38Z | 显式reasoning压力下的可见rationalization信号；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Auditing Disability Representation in Vision-Language Models](https://arxiv.org/abs/2601.17348v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:47:43Z | paired语境引发视觉外unsupported inference；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Robust Privacy: Inference-Time Privacy through Certified Robustness](https://arxiv.org/abs/2601.17360v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:48:00Z | 同classifier有效证书不能扩大原label preimage；2+1+2=5 | 争议 | 暂缓：中心保证争议，见§5 |
| [Elastic Attention: Test-time Adaptive Sparsity Ratios for Efficient Transformers](https://arxiv.org/abs/2601.17367v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:48:09Z | perhead可变attention结构选择及目标稀疏边界；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Physical Prompt Injection Attacks on Large Vision-Language Models](https://arxiv.org/abs/2601.17383v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:48:31Z | 视觉文字presence与实际prompt-injection effect分离；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [presence不等effect](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ReLE: A Scalable System and Structured Benchmark for Diagnosing Capability Anisotropy in Chinese LLMs](https://arxiv.org/abs/2601.17399v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:48:54Z | 同权重sample子集改变rank、但不能分解原因比例；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning](https://arxiv.org/abs/2601.17421v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:49:23Z | wrong-associated token并非所有模型中的必要错误因子；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [A Syllogistic Probe: Tracing the Evolution of Logic Reasoning in Large Language Models](https://arxiv.org/abs/2601.17426v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:49:30Z | empty/nonempty语义条件影响syllogism有效性标签；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Data-driven Test Generation for Fuzzing AI Compiler](https://arxiv.org/abs/2601.17450v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:50:03Z | 低级IR约束下发现compiler failure的探索接口；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping](https://arxiv.org/abs/2601.17467v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:50:26Z | 边界扰动agreement表征与局部uncertainty sensor；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [To Case or Not to Case: An Empirical Study in Learned Sparse Retrieval](https://arxiv.org/abs/2601.17500v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:51:10Z | 同cased checkpoint lowercasing改变稀疏检索表现；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Less is More for RAG: Information Gain Pruning for Generator-Aligned Reranking and Evidence Selection](https://arxiv.org/abs/2601.17532v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:51:54Z | 单passage entropy proxy漏联合证据及假自信；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents](https://arxiv.org/abs/2601.17549v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:52:17Z | 论文sampling角色与官方MCP capability定义冲突；2+2+2=6 | 争议 | 暂缓：中心保证争议，见§5 |
| [GreenServ: Energy-Efficient Context-Aware Dynamic Routing for Multi-Model LLM Inference](https://arxiv.org/abs/2601.17551v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:52:19Z | query-context能耗选择的测量与routing开销条件；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [JaxARC: A High-Performance JAX-based Environment for Abstraction and Reasoning Research](https://arxiv.org/abs/2601.17564v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:52:37Z | 同batch ARC functional环境的规模可行性条件；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Sponge Tool Attack: Stealthy Denial-of-Efficiency against Tool-Augmented Agentic Reasoning](https://arxiv.org/abs/2601.17566v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:52:39Z | 工具步数膨胀与billing/语义保持的不同分母；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-PLATFORM [stop-controller及成本分母](../../../../books/part-07-agent/84-agent-platform.md) |
| [Improving User Privacy in Personalized Generation: Client-Side Retrieval-Augmented Modification of Server-Side Generated Speculations](https://arxiv.org/abs/2601.17569v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:52:43Z | 端侧profile改draft、服务器仍收到accepted/corrected prefix；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [policy-bound sensor与observable-channel](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/abs/2601.17593v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:53:16Z | goldproof DAG的线性可访问结构不认证causal机制；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Understanding Transformer Encoder-Decoder Representations through Bernoulli Dropout](https://arxiv.org/abs/2601.17602v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:53:28Z | 归一化擦除表示的统一偏差界存在明确反例；2+1+2=5 | 争议 | 暂缓：中心保证争议，见§5 |
| [A Systemic Evaluation of Multimodal RAG Privacy](https://arxiv.org/abs/2601.17644v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:54:25Z | 检索库membership与conditional caption泄漏接口；2+2+2=6 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Kareus: Joint Reduction of Dynamic and Static Energy in Large Model Training](https://arxiv.org/abs/2601.17654v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:54:38Z | 频率、资源与launch共同决定overlap时间—能耗frontier；2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [overlap频率/能耗两段](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction](https://arxiv.org/abs/2601.17668v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:54:57Z | 离线KV重建监督转在线hidden gate的局部可行性；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE [预算及hiddengate局部分支](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [$\infty$-MoE: Generalizing Mixture of Experts to Infinite Experts](https://arxiv.org/abs/2601.17680v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:55:13Z | 连续Gaussian latent生成共享FFN mask而非无限独立专家；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [S$^3$-Attention:Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference](https://arxiv.org/abs/2601.17702v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:55:43Z | 稀疏feature索引与re-prefill的CPU/GPU质量成本分工；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [The Script is All You Need: An Agentic Framework for Long-Horizon Dialogue-to-Cinematic Video Generation](https://arxiv.org/abs/2601.17737v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:56:32Z | time-window CLIP引入局部视频评价信号；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [MV-S2V: Multi-View Subject-Consistent Video Generation](https://arxiv.org/abs/2601.17756v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:56:58Z | subject/view/reference时序identity分隔的有限对照；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [LLM-42: Enabling Determinism in LLM Inference with Verified Speculation](https://arxiv.org/abs/2601.17768v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:57:15Z | 动态验证路径在固定shape与KV commit边界下控制数值差异；2+2+2=6 | 标准完成 | 已有覆盖：INFER-CONTINUOUS-BATCHING [动态状态/验证与commit](../../../../books/part-05-inference-system/46-continuous-batching.md) |
| [MMR-Bench: A Comprehensive Benchmark for Multimodal LLM Routing](https://arxiv.org/abs/2601.17814v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:58:19Z | 固定outcome矩阵内模态fusion收益依router而变；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [ViTCoP: Accelerating Large Vision-Language Models via Visual and Textual Semantic Collaborative Pruning](https://arxiv.org/abs/2601.17818v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:58:24Z | 小K-L2与视觉聚类的局部depth/质量折中；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [VAE-REPA: Variational Autoencoder Representation Alignment for Efficient Diffusion Training](https://arxiv.org/abs/2601.17830v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:58:40Z | 已有VAE features替外部teacher并保留alignment开销；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [A Universal Load Balancing Principle and Its Application to Large Language Model Serving](https://arxiv.org/abs/2601.17855v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:59:15Z | 集中batch admission中的短未来负载接口与条件模型；2+2+2=6 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [VidLaDA: Bidirectional Diffusion Large Language Models for Efficient Video Understanding](https://arxiv.org/abs/2601.17868v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:59:33Z | modality/depth drift支持有限异步refresh与global anchor；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation](https://arxiv.org/abs/2601.17885v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T03:59:56Z | 逐token几何lift及crossview接口的task-finetuned验证；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [dLLM-ASR: A Faster Diffusion LLM-based Framework for Speech Recognition](https://arxiv.org/abs/2601.17902v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:00:22Z | ASR prior/pruning/confidence联合配方的WER边界；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [treaming-dLLM: Accelerating Diffusion LLMs via Suffix Pruning and Dynamic Decoding](https://arxiv.org/abs/2601.17917v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:00:43Z | masked suffix保邻近与terminal位置的局部结构条件；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [RemEdit: Efficient Diffusion Editing with Riemannian Geometry](https://arxiv.org/abs/2601.17927v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:00:57Z | learned ODE edit/control与pruning的质量时延折中；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [TensorLens: End-to-End Transformer Analysis via High-Order Attention Tensors](https://arxiv.org/abs/2601.17958v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:01:39Z | input-conditioned token×channel分解不是Jacobian/因果认证；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Addressing LLM Diversity by Infusing Random Concepts](https://arxiv.org/abs/2601.18053v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:03:49Z | 无关词及随机字符串改变list-mode输出分布；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Grounded Concreteness: Human-Like Concreteness Sensitivity in Vision-Language Models](https://arxiv.org/abs/2601.18065v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:04:06Z | concreteness分层关联不隔离visual训练预算因果；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents](https://arxiv.org/abs/2601.18077v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:04:23Z | engine外供deductions成绩不能认证内生state tracking；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models](https://arxiv.org/abs/2601.18091v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:04:44Z | thinking模型需要独立prune/recovery质量验收；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Spatial-Conditioned Reasoning in Long-Egocentric Videos](https://arxiv.org/abs/2601.18100v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:04:56Z | 同模型depth-fusion对不同consumer可改善或退化；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [AttenMIA: LLM Membership Inference Attack through Attention Signals](https://arxiv.org/abs/2601.18110v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:05:10Z | whitebox attention membership sensor仍需known-member监督；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs](https://arxiv.org/abs/2601.18113v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:05:14Z | URL文本accept评价不等实际有害站点访问；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:06:06Z | 每policy-step FP8/KV校准支持容量受限rollout；2+2+2=6 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [\textsc{NaVIDA}: Vision-Language Navigation with Inverse Dynamics Augmentation](https://arxiv.org/abs/2601.18188v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:06:58Z | action-type entropy方向改变的有限horizon截断；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents](https://arxiv.org/abs/2601.18217v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:07:37Z | goal-irrelevant observation noise的有限训练泛化条件；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [LLM-ForcedAligner: A Non-Autoregressive and Accurate LLM-Based Forced Aligner for Multilingual and Long-Form Speech](https://arxiv.org/abs/2601.18220v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:07:41Z | timestamp slot分辨率更细可更拟合pseudo而不改善human；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [BoRP: Bootstrapped Regression Probing for Scalable and Human-Aligned LLM Evaluation](https://arxiv.org/abs/2601.18253v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:08:27Z | 极端case rubric与几何resampling的冷启动评价接口；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Reflecting Twice before Speaking with Empathy: Self-Reflective Alternating Inference for Empathy-Aware End-to-End Spoken Dialogue](https://arxiv.org/abs/2601.18281v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:09:06Z | spoken audio与unspoken reflection交错的局部条件；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment](https://arxiv.org/abs/2601.18292v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:09:21Z | 三role安全训练的过滤人口与unmatched loop预算；2+1+2=5 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning](https://arxiv.org/abs/2601.18296v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:09:27Z | hard-first curriculum限制temporal search shortcut的局部反侧；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM](https://arxiv.org/abs/2601.18306v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:09:41Z | 固定量化预算下校准语言的非单调收益；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion](https://arxiv.org/abs/2601.18323v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:10:04Z | generatedvideo到metric rigid TCP与gripperstate的分工；2+2+2=6 | 深入完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Code over Words: Overcoming Semantic Inertia via Code-Grounded Reasoning](https://arxiv.org/abs/2601.18352v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:10:44Z | paired contradictory-rule测试code/text prior的局部盲区；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |
| [Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models](https://arxiv.org/abs/2601.18383v1) | 2026-01-27T01:00:00Z ～ 2026-01-27T04:11:26Z | 后验answer attention标签转在线importance proxy的边界；2+1+2=5 | 标准完成 | 仅报告：局部接口/评价条件，未形成普遍设计结论 |

表中时间为保留UTC原精度的保守公开包络，起点Jan27T01Z即北京时间09:00；上界为DataCite created+1秒，不是补造实际发布时间。所有范围完全落窗。原Submitted、created及官方schedule依据见DATE_BOUNDS，不使用Updated。评分只针对表述的新增命题；争议项已隔离，不用于正面证据。

## 4. 证据与知识整合

已实际写入并通过非作者POST的是[Ch36频率×资源×launch联合time-energy frontier两段](../../../../books/part-04-training-system/36-distributed-training.md)以及[Ch66知识编辑locality sensor两段](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：same-query before/after保留性与事实正确性分账，topk相同不保证KL小、lasttoken不认证全continuation。17569隐私机制的[Ch72具体已有覆盖](../../../../books/part-06-ai-infrastructure/72-security.md)为“隐私检测是Policy-bound Sensor”与“全部Observable Channels”，不是只按主题关联判覆盖。其他已完成局部结论及完整必要反侧见REVIEWS；作者实验未复现，代码/生产能力未核验。

### [Acoustic Field Video for Multimodal Scene Understanding](https://arxiv.org/abs/2601.17123v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17123v1)。精确v1采用边界：声压场overlay补充RGB/stereo丢失的声源可见性。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17123）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Learning to Collaborate: An Orchestrated-Decentralized Framework for Peer-to-Peer LLM Federation](https://arxiv.org/abs/2601.17133v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17133v1)。精确v1采用边界：中央profile匹配与P2P teacher文本的暴露边界。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17133）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [AGZO: Activation-Guided Zeroth-Order Optimization for LLM Fine-Tuning](https://arxiv.org/abs/2601.17261v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17261v1)。精确v1采用边界：activation子空间ZO仅conditioned目标与能量条件。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17261）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Latent-Space Contrastive Reinforcement Learning for Stable and Efficient LLM Reasoning](https://arxiv.org/abs/2601.17275v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17275v1)。精确v1采用边界：latent预筛成本与全decode、冻结权重零遗忘保证冲突。中心结论冲突；保留反证与重开条件，不作正面采用。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17275）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Phase Transition for Budgeted Multi-Agent Synergy](https://arxiv.org/abs/2601.17311v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17311v1)。精确v1采用边界：多数树相关误差与有损通信的small-signal预算相变。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17311）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Conformal Feedback Alignment: Quantifying Answer-Level Reliability for Robust LLM Alignment](https://arxiv.org/abs/2601.17329v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17329v1)。精确v1采用边界：CP集合用于偏好权重但marginal覆盖不认证真值。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17329）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Power-based Partial Attention: Bridging Linear-Complexity and Full Attention](https://arxiv.org/abs/2601.17334v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17334v1)。精确v1采用边界：偏移幂律稀疏mask的固定window/复杂度分支。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17334）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Are We Evaluating the Edit Locality of LLM Model Editing Properly?](https://arxiv.org/abs/2601.17343v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17343v1)。精确v1采用边界：编辑locality的GT、teacherforcing与contrastive混杂。处置为整合，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17343）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [The Shadow Self: Intrinsic Value Misalignment in Large Language Model Agents](https://arxiv.org/abs/2601.17344v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17344v1)。精确v1采用边界：显式reasoning压力下的可见rationalization信号。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17344）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Auditing Disability Representation in Vision-Language Models](https://arxiv.org/abs/2601.17348v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17348v1)。精确v1采用边界：paired语境引发视觉外unsupported inference。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17348）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Robust Privacy: Inference-Time Privacy through Certified Robustness](https://arxiv.org/abs/2601.17360v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17360v1)。精确v1采用边界：同classifier有效证书不能扩大原label preimage。中心结论冲突；保留反证与重开条件，不作正面采用。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17360）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Elastic Attention: Test-time Adaptive Sparsity Ratios for Efficient Transformers](https://arxiv.org/abs/2601.17367v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17367v1)。精确v1采用边界：perhead可变attention结构选择及目标稀疏边界。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17367）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Physical Prompt Injection Attacks on Large Vision-Language Models](https://arxiv.org/abs/2601.17383v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17383v1)。精确v1采用边界：视觉文字presence与实际prompt-injection effect分离。处置为已有覆盖，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17383）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [ReLE: A Scalable System and Structured Benchmark for Diagnosing Capability Anisotropy in Chinese LLMs](https://arxiv.org/abs/2601.17399v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17399v1)。精确v1采用边界：同权重sample子集改变rank、但不能分解原因比例。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17399）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning](https://arxiv.org/abs/2601.17421v1)

精确v1采用边界：wrong-associated token并非所有模型中的必要错误因子。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17421）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [A Syllogistic Probe: Tracing the Evolution of Logic Reasoning in Large Language Models](https://arxiv.org/abs/2601.17426v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17426v1)。精确v1采用边界：empty/nonempty语义条件影响syllogism有效性标签。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17426）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Data-driven Test Generation for Fuzzing AI Compiler](https://arxiv.org/abs/2601.17450v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17450v1)。精确v1采用边界：低级IR约束下发现compiler failure的探索接口。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17450）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping](https://arxiv.org/abs/2601.17467v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17467v1)。精确v1采用边界：边界扰动agreement表征与局部uncertainty sensor。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17467）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [To Case or Not to Case: An Empirical Study in Learned Sparse Retrieval](https://arxiv.org/abs/2601.17500v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17500v1)。精确v1采用边界：同cased checkpoint lowercasing改变稀疏检索表现。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17500）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Less is More for RAG: Information Gain Pruning for Generator-Aligned Reranking and Evidence Selection](https://arxiv.org/abs/2601.17532v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17532v1)。精确v1采用边界：单passage entropy proxy漏联合证据及假自信。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17532）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents](https://arxiv.org/abs/2601.17549v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17549v1)。精确v1采用边界：论文sampling角色与官方MCP capability定义冲突。中心结论冲突；保留反证与重开条件，不作正面采用。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17549）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [GreenServ: Energy-Efficient Context-Aware Dynamic Routing for Multi-Model LLM Inference](https://arxiv.org/abs/2601.17551v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17551v1)。精确v1采用边界：query-context能耗选择的测量与routing开销条件。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17551）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [JaxARC: A High-Performance JAX-based Environment for Abstraction and Reasoning Research](https://arxiv.org/abs/2601.17564v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17564v1)。精确v1采用边界：同batch ARC functional环境的规模可行性条件。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17564）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Sponge Tool Attack: Stealthy Denial-of-Efficiency against Tool-Augmented Agentic Reasoning](https://arxiv.org/abs/2601.17566v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17566v1)。精确v1采用边界：工具步数膨胀与billing/语义保持的不同分母。处置为已有覆盖，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17566）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Improving User Privacy in Personalized Generation: Client-Side Retrieval-Augmented Modification of Server-Side Generated Speculations](https://arxiv.org/abs/2601.17569v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17569v1)。精确v1采用边界：端侧profile改draft、服务器仍收到accepted/corrected prefix。处置为已有覆盖，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17569）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/abs/2601.17593v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17593v1)。精确v1采用边界：goldproof DAG的线性可访问结构不认证causal机制。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17593）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Understanding Transformer Encoder-Decoder Representations through Bernoulli Dropout](https://arxiv.org/abs/2601.17602v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17602v1)。精确v1采用边界：归一化擦除表示的统一偏差界存在明确反例。中心结论冲突；保留反证与重开条件，不作正面采用。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17602）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [A Systemic Evaluation of Multimodal RAG Privacy](https://arxiv.org/abs/2601.17644v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17644v1)。精确v1采用边界：检索库membership与conditional caption泄漏接口。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17644）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Kareus: Joint Reduction of Dynamic and Static Energy in Large Model Training](https://arxiv.org/abs/2601.17654v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17654v1)。精确v1采用边界：频率、资源与launch共同决定overlap时间—能耗frontier。处置为整合，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17654）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction](https://arxiv.org/abs/2601.17668v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17668v1)。精确v1采用边界：离线KV重建监督转在线hidden gate的局部可行性。处置为已有覆盖，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17668）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [$\infty$-MoE: Generalizing Mixture of Experts to Infinite Experts](https://arxiv.org/abs/2601.17680v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17680v1)。精确v1采用边界：连续Gaussian latent生成共享FFN mask而非无限独立专家。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17680）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [S$^3$-Attention:Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference](https://arxiv.org/abs/2601.17702v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17702v1)。精确v1采用边界：稀疏feature索引与re-prefill的CPU/GPU质量成本分工。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17702）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [The Script is All You Need: An Agentic Framework for Long-Horizon Dialogue-to-Cinematic Video Generation](https://arxiv.org/abs/2601.17737v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17737v1)。精确v1采用边界：time-window CLIP引入局部视频评价信号。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17737）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [MV-S2V: Multi-View Subject-Consistent Video Generation](https://arxiv.org/abs/2601.17756v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17756v1)。精确v1采用边界：subject/view/reference时序identity分隔的有限对照。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17756）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [LLM-42: Enabling Determinism in LLM Inference with Verified Speculation](https://arxiv.org/abs/2601.17768v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17768v1)。精确v1采用边界：动态验证路径在固定shape与KV commit边界下控制数值差异。处置为已有覆盖，具体正文位置见上表及笔记；不授超出反侧的普遍保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17768）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [MMR-Bench: A Comprehensive Benchmark for Multimodal LLM Routing](https://arxiv.org/abs/2601.17814v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17814v1)。精确v1采用边界：固定outcome矩阵内模态fusion收益依router而变。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17814）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [ViTCoP: Accelerating Large Vision-Language Models via Visual and Textual Semantic Collaborative Pruning](https://arxiv.org/abs/2601.17818v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17818v1)。精确v1采用边界：小K-L2与视觉聚类的局部depth/质量折中。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17818）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [VAE-REPA: Variational Autoencoder Representation Alignment for Efficient Diffusion Training](https://arxiv.org/abs/2601.17830v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17830v1)。精确v1采用边界：已有VAE features替外部teacher并保留alignment开销。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17830）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [A Universal Load Balancing Principle and Its Application to Large Language Model Serving](https://arxiv.org/abs/2601.17855v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17855v1)。精确v1采用边界：集中batch admission中的短未来负载接口与条件模型。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17855）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [VidLaDA: Bidirectional Diffusion Large Language Models for Efficient Video Understanding](https://arxiv.org/abs/2601.17868v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17868v1)。精确v1采用边界：modality/depth drift支持有限异步refresh与global anchor。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17868）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [PEAfowl: Perception-Enhanced Multi-View Vision-Language-Action for Bimanual Manipulation](https://arxiv.org/abs/2601.17885v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17885v1)。精确v1采用边界：逐token几何lift及crossview接口的task-finetuned验证。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17885）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [dLLM-ASR: A Faster Diffusion LLM-based Framework for Speech Recognition](https://arxiv.org/abs/2601.17902v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17902v1)。精确v1采用边界：ASR prior/pruning/confidence联合配方的WER边界。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17902）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [treaming-dLLM: Accelerating Diffusion LLMs via Suffix Pruning and Dynamic Decoding](https://arxiv.org/abs/2601.17917v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17917v1)。精确v1采用边界：masked suffix保邻近与terminal位置的局部结构条件。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17917）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [RemEdit: Efficient Diffusion Editing with Riemannian Geometry](https://arxiv.org/abs/2601.17927v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17927v1)。精确v1采用边界：learned ODE edit/control与pruning的质量时延折中。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17927）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [TensorLens: End-to-End Transformer Analysis via High-Order Attention Tensors](https://arxiv.org/abs/2601.17958v1)

[实际证据正文 v1](https://arxiv.org/html/2601.17958v1)。精确v1采用边界：input-conditioned token×channel分解不是Jacobian/因果认证。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.17958）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Addressing LLM Diversity by Infusing Random Concepts](https://arxiv.org/abs/2601.18053v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18053v1)。精确v1采用边界：无关词及随机字符串改变list-mode输出分布。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18053）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Grounded Concreteness: Human-Like Concreteness Sensitivity in Vision-Language Models](https://arxiv.org/abs/2601.18065v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18065v1)。精确v1采用边界：concreteness分层关联不隔离visual训练预算因果。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18065）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents](https://arxiv.org/abs/2601.18077v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18077v1)。精确v1采用边界：engine外供deductions成绩不能认证内生state tracking。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18077）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models](https://arxiv.org/abs/2601.18091v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18091v1)。精确v1采用边界：thinking模型需要独立prune/recovery质量验收。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18091）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Spatial-Conditioned Reasoning in Long-Egocentric Videos](https://arxiv.org/abs/2601.18100v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18100v1)。精确v1采用边界：同模型depth-fusion对不同consumer可改善或退化。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18100）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [AttenMIA: LLM Membership Inference Attack through Attention Signals](https://arxiv.org/abs/2601.18110v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18110v1)。精确v1采用边界：whitebox attention membership sensor仍需known-member监督。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18110）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs](https://arxiv.org/abs/2601.18113v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18113v1)。精确v1采用边界：URL文本accept评价不等实际有害站点访问。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18113）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v1)

精确v1采用边界：每policy-step FP8/KV校准支持容量受限rollout。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18150）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [\textsc{NaVIDA}: Vision-Language Navigation with Inverse Dynamics Augmentation](https://arxiv.org/abs/2601.18188v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18188v1)。精确v1采用边界：action-type entropy方向改变的有限horizon截断。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18188）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents](https://arxiv.org/abs/2601.18217v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18217v1)。精确v1采用边界：goal-irrelevant observation noise的有限训练泛化条件。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18217）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [LLM-ForcedAligner: A Non-Autoregressive and Accurate LLM-Based Forced Aligner for Multilingual and Long-Form Speech](https://arxiv.org/abs/2601.18220v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18220v1)。精确v1采用边界：timestamp slot分辨率更细可更拟合pseudo而不改善human。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18220）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [BoRP: Bootstrapped Regression Probing for Scalable and Human-Aligned LLM Evaluation](https://arxiv.org/abs/2601.18253v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18253v1)。精确v1采用边界：极端case rubric与几何resampling的冷启动评价接口。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18253）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Reflecting Twice before Speaking with Empathy: Self-Reflective Alternating Inference for Empathy-Aware End-to-End Spoken Dialogue](https://arxiv.org/abs/2601.18281v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18281v1)。精确v1采用边界：spoken audio与unspoken reflection交错的局部条件。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18281）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [TriPlay-RL: Tri-Role Self-Play Reinforcement Learning for LLM Safety Alignment](https://arxiv.org/abs/2601.18292v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18292v1)。精确v1采用边界：三role安全训练的过滤人口与unmatched loop预算。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18292）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning](https://arxiv.org/abs/2601.18296v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18296v1)。精确v1采用边界：hard-first curriculum限制temporal search shortcut的局部反侧。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18296）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM](https://arxiv.org/abs/2601.18306v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18306v1)。精确v1采用边界：固定量化预算下校准语言的非单调收益。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18306）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion](https://arxiv.org/abs/2601.18323v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18323v1)。精确v1采用边界：generatedvideo到metric rigid TCP与gripperstate的分工。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18323）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Code over Words: Overcoming Semantic Inertia via Code-Grounded Reasoning](https://arxiv.org/abs/2601.18352v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18352v1)。精确v1采用边界：paired contradictory-rule测试code/text prior的局部盲区。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18352）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

### [Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models](https://arxiv.org/abs/2601.18383v1)

[实际证据正文 v1](https://arxiv.org/html/2601.18383v1)。精确v1采用边界：后验answer attention标签转在线importance proxy的边界。采用范围只限披露的接口、对照与评价条件；不授完整因果、生产/SLO或通用质量保证。必要方法、配置、收益/代价与直接反侧见[本日逐项证据笔记（2601.18383）](../_sources/daily-20260128/REVIEWS.md)。root已独立核验本项必要命题与处置；未复现实验或核验可选实现。

首批准入校准实际覆盖[Crystal-KV v1](https://arxiv.org/abs/2601.16986v1)、[FlashMoE v1](https://arxiv.org/abs/2601.17063v1)、[Lost in Simulation v1](https://arxiv.org/abs/2601.17087v1)与[视频生成world-model taxonomy v1](https://arxiv.org/abs/2601.17067v1)。前三者有值得核验的缓存/存储替代选择、真人/代理有效性增量，后一篇仅术语归纳/倡议不足；校准未给予日期许可或证据采用许可。

Google [ATLAS](https://research.google/blog/atlas-practical-scaling-laws-for-multilingual-models/)和[agent-scaling blog](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)复述旧研究；后一项定点对照[Dec17 v2原AB](https://arxiv.org/abs/2512.08296v2)的180配置/架构-任务匹配/错误放大，未披露本次新增方法或实验。不是以“别人可能已审”去重，也不采用博客性能/安全保证。原增量不足条目具体关闭原因在SCREENING；没有为凑Books变更把它们重新包装为知识缺口。

## 5. 缺口与下一步

尚可执行工作：无。64项必要证据/Books处置及本报告六部分日级独立验收已通过；机器/引用/变更范围检查通过。Ch66/Ch36窄锁均已释放。以下是本窗已隔离的终态保留项，不是未执行的普通待办，后续只凭指定新材料定点重开。

本窗终态保留项（不用于正面证据、不进入Books、不支撑无遗漏或性能/安全保证）：

- arXiv必要日期：老Submitted的16986/16987/17006/17037/17042/17050/17063/17082/17086/17087，仅上界落窗，最早公告下界不完全落窗；原字段/精确v1/停点见[SCREENING](../_sources/daily-20260128/SCREENING.md)。只请求一次ID→官方公告day映射或不可回溯首次公开正文日志，证明完整落窗才重开该ID，不重扫全月。其余93事件已经schedule+created支持，不再请求不可得dayheading。
- [RobustPrivacy v1](https://arxiv.org/html/2601.17360v1)：同一f有效证书下区间并集等于原label preimage，不能支持中心扩大集合保证；换smoothed classifier的实验不能补此证明。root独立核定义/实验/always-label协议后确认争议，只留报告、Books暂缓。重开需修正同一f定义及非平凡隐私证明，或明确classifier/query协议变化后的受控保证。
- [DeepLatent Reasoning v1](https://arxiv.org/html/2601.17275v1)：latent预筛与全部G decoded的描述冲突，K/G主模型compute估算遗漏assistant/筛选/训练，冻结W不认证新latent输入零遗忘。需可在decode前获得的reward/筛选定义、完整成本及旧任务行为对照才重开；不采效率/零遗忘保证、不进Books。
- [Breaking the Protocol v1](https://arxiv.org/html/2601.17549v1)：sampling被论文作为server capability及无限升级，与2024-11-05官方client sampling声明和negotiated operation约束冲突。需有效dated spec角色更正及同接口/权限/预算对照，才重开具体协议claim；不采ASR/全compliant放大或厂商CA部署保证。
- [Representation Robustness v1](https://arxiv.org/html/2601.17602v1)：iid擦除与确定阈值实现不同，unit q=v1均匀、v2=-q时归一化masked innerproduct偏差趋1−√p，声称界却趋0；本例top1仍保持。需与实现一致的分布、归一化/embedding假设与有效偏差证明才重开；不采定理/corollary、不进Books。
- [Kimi K2.5](https://www.kimi.ai/blog/kimi-k2-5)：原PARL机制可读，officialJan27 release日精度不足；需该tech正文/发布的首公开时刻或完全落窗区间，不用Feb技术报告、后续文档或搜索收录时刻替代。
- [MiniMax-M2-her](https://www.minimax.io/blog/minimax-m2-her)：situated reenactment和online preference过滤/早停有潜在增量，Jan27日精度与合成JSON-LD午夜不证明实际时刻；需原发布时间的可核记录或完整落窗区间。
- 历史来源目录：OpenAI/Anthropic/Meta/Qwen/DeepMind/MiMo和Hunyuan“全部”历史目录缺失，Seed/DeepSeek当前精选目录不证明历史完整。准确入口、失败与停止范围、可接受替代逐源见[SOURCE_STOPS](../_sources/daily-20260128/SOURCE_STOPS.md)。只在当窗dated目录或具体漏项原发布到达时重开对应source/ID。GoogleResearch/Z.ai/ERNIE/MiniMax可见排序区间的检查仍有效，不随其他缺口推倒重扫。

Keel nativeJan27日精度及OCR2 nativeJan28日精度不能确认全家族落窗，已在12个arXiv日期保留家族内，各只一次请求。仅Submitted晚于截止不能排除家族其他原发布更早；不指定虚构归属日。贡献关闭项不为无关日期再建请求。

## 6. 复核

复核者：root（独立非作者）。

结论：通过

root已实际核最终六部分、来源停点、原始日期包络及64表/证据映射；复用已完成的64/64必要源复核和2项Books POST。root实际检查首批完整原AB准入与代表排除、纠正Submitted/metadata误用及成熟recipe共同误收，仅重开受影响集合。全部64候选精确v1的必要机制、评价/配置和直接反侧已分批核验；21项受影响深入、43项标准，4个中心争议终态不授正面Evidence。2项实际Books写入及前后邻接/末注POST、5项具体已有覆盖均独立通过。关闭侧具名实际完整AB分层样本至少19/30：17067；17277/17645/17212/17443/17699/17722/17507/17879/18226；17197/17716/18204/17982/17418/18116/18146/18203/18386，18386安全信号另实际core复核。其余11项未声称完整独立AB验证，共同误理由关联判断已按校准纠正。实际分批原源、停止范围与判断详见REVIEWS/SCREENING；14个必要日期保留及历史目录缺口终态隔离。root完成六部分汇总语义验收并亲自重跑V3与限定cached/unstaged diff检查通过；不把关闭抽检称全量验证。

机器校验：`python3 scripts/validate_research.py --report papers/2026/01/28/README.md`通过（V3；不证明语义真值）；64唯一候选/64同标题同URL证据小标题、全64日期包络落窗及评分/处置数量核对通过。83个本地引用（10个唯一目标）存在；64份必要HTML/PDF carrier存在，5个本日Markdown无尾随空白/缺EOF换行；新增README/REVIEWS的no-index diff-check与两处Books的scoped unstaged/cached diff-check均通过。未stage、commit、push，既有无关工作树与暂存修改保留。整日语义已获root独立验收通过。
