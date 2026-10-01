# Daily Research — 2026-04-14

**规范：** V3
**窗口：** 2026-04-13T09:00:00+08:00 ～ 2026-04-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T20:57:28+08:00

## 1. 结论

本日保留82个唯一论文家族；必要证据已处理为32项深入完成、42项标准完成、8项中心采用争议隔离。Books为25项实际机制正文及非作者写后通过、7项具体已有覆盖、42项仅报告、8项暂缓。最终日级独立验收通过，普通可执行待办为零；完成不表示历史来源缺口或中心争议已获正面证明。

主要增量是：推理性能必须共同结算真实语义流量、proposal/verify、硬件shape与物理KV locality；表示可恢复、融合可访问和输出可表达不能混为一个能力；终局reward、生成全轨迹、环境witness及多轮memory累计暴露要分别验收。新机制均插入现有owner论证，保留旧方案成立条件、代价和回退，而非在章末追加摘要。

原始三页为2262个去重身份，09548～10881的1334个只是有界查漏子范围；实际浏览325条主题标题线索、阅读155项完整题摘，均不等当日有效论文数或全文队列。82候选不含28项未能确认落窗的晚段线索、09940早公开线索及09945版本身份缺口。前分母关闭保留具体原因，未用旧Weekly或旧筛选标签生成本日。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)及官方RSS1230项；Apr13 06:00Z Cloudflare Agent Cloud核心说明已读，按平台产品整合关闭 | 受阻 | Research历史目录不能完整恢复；RSS与该事件不代表整个组织无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)170条publishedOn目录；Apr09 16:34Z至Apr14 13:01Z相邻边界，未见本窗条目 | 已检查 | 无 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)目录264第一段Apr22至Mar22；Google四月blog9项，Apr13 Vantage技能核心说明为既有应用/评价组合而关闭 | 受阻 | Google Pubs本窗历史研究切片未恢复；不以Blog代替论文全覆盖 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空提取及已恢复Blog相邻条目作有界补查，未将空响应算零命中 | 受阻 | 需要可绑定本窗的FAIR研究目录/列表 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/)动态40项Apr02至Apr15 10:00+08、静态60项停2025Dec；界面和两种目录不等历史artifact | 受阻 | 本窗历史研究/artifact列表未完整恢复 |
| SRC-DEEPSEEK | [官方入口](https://www.deepseek.com/)及现有原始论文渠道，未取得可证明本窗完整性的历史目录 | 受阻 | 需本窗发布/研究记录；不能由官网当前展示证明零更新 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26项最新2025Nov；[CLI1.32.0](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.32.0)published_at Apr13 11:39:51Z与PR1843实际核心说明，工具混合内容预算/兼容性patch前分母关闭 | 受阻 | 模型研究及其他组织artifact历史切片不可恢复；CLI不代替全组织 |
| SRC-TENCENT-HUNYUAN | [全部研究列表](https://hunyuan.tencent.com/research)publicList page1/size100/renderType0，共9项；Apr30/23至Feb13，不含本窗；原始论文入口与arXiv家族去重 | 已检查 | 无 |
| SRC-ZAI | [官方Research](https://www.zhipuai.cn/zh/research)Apr29至Apr07/Apr01相邻条目；不因Research目录含窗外项扩扫全文 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [论文](https://seed.bytedance.com/en/public_papers)type1 count20 localeUS pages0/20/40 total242，Apr12 16Z至Apr10/09/07；Blog type2 pages0/20 total95，再20/40到2025Dec17，未见本窗条目 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)Apr15至Feb06/2025相邻边界；[ERNIE](https://github.com/PaddlePaddle/ERNIE)release现可恢复仅2025Jun30 | 受阻 | repo历史研究切片不足，不把已检查Blog扩称全部artifact |
| SRC-XIAOMI-MIMO | [Paper](https://mimo.xiaomi.com/)Jun29至Mar13/Feb03/Jan08；论文目录边界未含本窗 | 受阻 | Blog/历史组织artifact日期未恢复 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)May26至Mar18、[CN](https://www.minimaxi.com/blog)Apr27至Mar18；CLI1.0.7 Apr10至1.0.8 Apr16；M2/M2.5现入口为空不等零更新 | 受阻 | Agent Tech Blog及组织artifact本窗日期列表未恢复 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)、April身份、原始v1日期簇和相邻ID边界联合核；三页2262去重身份中的1334子范围作有界查漏，325标题、155完整题摘实际处理，确定82家族 | 受阻 | 月列表只证月级；无逐篇精确日公告日志，晚段28项及早公开/版本例外隔离；不宣称全网零遗漏 |

来源事实与筛选过程保存在[本日原始工作记录](../_sources/daily-20260414/v3-reopen-notes.md)。每日来源14行全部处理至当前可用入口的有界结果；上述受阻子入口是终态保留，不支持已完成覆盖或无遗漏断言。不加载每周源。官方事件没有入选也保留实际扫描结果，不写成机构零事件。

## 3. 候选与判断

评分顺序为Design Delta + System Reach + Durability。公开范围采用[非作者有限日期判断](../_sources/daily-20260414/V3_APR01_FINAL_GAP_ADOPTION.md#82-家族日期范围的有限独立判断2026-09-27)：April Available、永久ID公告赋号、原始v1处理簇与相邻边界的**一致性推断**，不是将Submitted、Updated或DOI-created改名为first-public，也不是逐篇已取得公告日志。82项均在早段，v1 Updated为00:00:18～00:59:09Z；边界10566/10567分别00:59:51/01:00:01Z。已发现更早正文或版本污染的例外单项隔离，不套用该范围。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://arxiv.org/html/2604.09557v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 随机token与真实语义流量即使长度相同，也改变proposal可预测性；词表裁剪须单列长尾覆盖代价，接受长度不能代替端到端收益。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [StreamServe: Adaptive Speculative Flows for Low-Latency Disaggregated LLM Serving](https://arxiv.org/html/2604.09562v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | FlowGuard单位、历史δ与acceptance及depth更新方向冲突，且throughput递推不等实际测量；中心编排保证不能据此采用。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [OOWM: Structuring Embodied Reasoning and Planning via Object-Oriented Programmatic World Modeling](https://arxiv.org/html/2604.09580v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | PlantUML状态/计划与XML、embedding奖励提供受限训练接口，但未验证真实环境transition；跨任务差异不证明可执行世界状态。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [MobiFlow: Real-World Mobile Agent Benchmarking through Trajectory Fusion](https://arxiv.org/html/2604.09587v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 成功轨迹合并成可回放GUI图提供便宜评价路径，但采集覆盖与错误动作模拟约定不能等同开放界面、真实副作用。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Why Smaller Is Slower? Dimensional Misalignment in Compressed LLMs](https://arxiv.org/html/2604.09595v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 先profile合法硬件shape，再在同一模型参数预算中分配压缩容量；不规则维度的kernel代价改变参数越少越快的判断。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios](https://arxiv.org/html/2604.09603v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 共享batch预算先延伸有区分力的depth，再扩局部width；这是两级资源决策，预算余额检查不能证明严格cap。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Characterizing Performance-Energy Trade-offs of Large Language Models in Multi-Request Workflows](https://arxiv.org/html/2604.09611v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | prefix共享、顺序依赖和角色异质性改变batch的能耗趋势；有限vLLM/Parrot负载没有冻结全部质量与SLO，不能给出统一最优batch。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Self-Calibrating Language Models via Test-Time Discriminative Distillation](https://arxiv.org/html/2604.09624v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | base discriminative signal经distractor归一化指导置信适配，entropy触发burst；有限label-free结果不证明校准置信就是事实概率。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models](https://arxiv.org/html/2604.09651v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 污染flow早段方向但匹配向量范数，说明等范数不等合法行动；LIBERO任务失败代理并非固定恶意终点或物理安全证明。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Deliberative Alignment is Deep, but Uncertainty Remains: Inference time safety improvement in reasoning via attribution of unsafe behavior to base model](https://arxiv.org/html/2604.09665v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | base/FT隐状态相似度筛选在deliberative与普通IT模型间表现不同；层选择、BoN预算与utility下降限制因果和部署解释。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems](https://arxiv.org/html/2604.09666v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 保持agent protocol比较检索backend，显示查询分解部分补偿dense检索、multi-hop仍有graph优势；不同基线缩减不可合成统一收益。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [In-context superposition: human-like working memory interference in large language models](https://arxiv.org/html/2604.09670v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 完整历史与位置可访问不保证chat模型实现可靠回读；lure、集合大小和teacher-forcing控制分离内容竞争与任务学会程度。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [NetAgentBench: A State-Centric Benchmark for Evaluating Agentic Network Configuration](https://arxiv.org/html/2604.09678v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | STOP声明、配置收敛和环境witness分责；早退删失会同时降低完成度与风险观测机会，原文run总数矛盾不采用。 2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models](https://arxiv.org/html/2604.09687v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | encoder可恢复、融合可访问、输出可表达是三个不同问题；冻结probe额外监督与patch边界限制单因果瓶颈解释。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Orthogonal Quadratic Complements for Vision Transformer Feed-Forward Networks](https://arxiv.org/html/2604.09709v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 低秩二次分支在rank空间消平行成分，再lift/gate融合；不保证原空间或函数空间非冗余，普通非线性FFN不能误称线性。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [LAST: Leveraging Tools as Hints to Enhance Spatial Reasoning for Multimodal Large Language Models](https://arxiv.org/html/2604.09712v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 空间metric与direction对不同工具表示的消费能力不同；训练移除输出与推理遮一路不是同一干预，联合hint并非每个slice最好。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [ConfigSpec: Profiling-Based Configuration Selection for Distributed Edge--Cloud Speculative LLM Serving](https://arxiv.org/html/2604.09722v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | profile选择K涉及accepted吞吐、token计费和edge能量三个目标；只计draft时间的能耗不是整条edge-cloud成本。 2+2+2=6 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [SMART: When is it Actually Worth Expanding a Speculative Tree?](https://arxiv.org/html/2604.09731v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | prefix概率按root-to-leaf均值计算不等候选树总接受进度；重复prefix和成本模型使中心树扩展估计缺少可采用保证。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [ExecTune: Effective Steering of Black-Box LLMs with Guide Models](https://arxiv.org/html/2604.09741v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 按受约束core成功过滤guide再训练，是target-conditioned策略分支；good execution假设不保证任意black-box core忠实执行。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [MPAC: A Multi-Principal Agent Coordination Protocol for Interoperable Multi-Agent Collaboration](https://arxiv.org/html/2604.09744v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | coordinator序列化、断连禁共享mutation、恢复epoch和phase授权形成协议分支；中心节点及延迟代价、有限案例不证明通用可靠性。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying](https://arxiv.org/html/2604.09747v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 已暴露memory记录可反用作后续query的anchor，单次访问保护不足；要核累计输出反馈与相同query预算下的提取范围。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Backdoors in RLVR: Jailbreak Backdoors in LLMs From Verifiable Reward](https://arxiv.org/html/2604.09748v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 终局答案verifier不保护完整生成轨迹，有害前缀加正确答案仍获正reward；checked span与行为验收必须分开。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [See Fair, Speak Truth: Equitable Attention Improves Grounding and Reduces Hallucination in Vision-Language Alignment](https://arxiv.org/html/2604.09749v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | object置信/稀有度改变decode attention且用EMA平滑；proposal质量、取得成本与mask后归一化限制不能当免费oracle。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Conflicts Make Large Reasoning Models Vulnerable to Attacks](https://arxiv.org/html/2604.09750v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | moral/reasoning冲突暴露有限jailbreak边界；PCA、cosine及成功攻击子集相关性不证明唯一安全机制，未验证defense。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [A-IO: Adaptive Inference Orchestration for Memory-Bound NPUs](https://arxiv.org/html/2604.09752v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | NPU路由/PLD的验证和采样语义未披露，HumanEval结果明显退步；不能把未披露实现反推为lossless PLD必然损害质量。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Sustainable Transformer Neural Network Acceleration with Stochastic Photonic Computing](https://arxiv.org/pdf/2604.09759v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | stochastic bitstream和signed accumulate构成硬件替代，但证据为device/架构仿真与有限小模型任务，不是LLM生产能效。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Text-Guided 6D Object Pose Rearrangement via Closed-Loop VLM Agents](https://arxiv.org/html/2604.09781v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 显式坐标、renderer反馈和单轴增量旋转提供pose推理接口；自评或预算停止不等物理安全，模拟结果不外推真实机器人。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning](https://arxiv.org/html/2604.09813v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | augmentation只有保持原oracle有效才保同一答案，缺信息/错query需改变预期行为；LLM judge分支不是纯deterministic checker。 2+2+2=6 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/html/2604.09815v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 经验检索与专家蒸馏是不同分支，每轮SFT从base重启；三应用和峰值epoch选择不证明参数持续学习单调收益。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models](https://arxiv.org/html/2604.09824v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 理论只约束固定observation时的目标敏感性，却据此限制observation变化后的action；policy直接observation路径构成反例。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Steered LLM Activations are Non-Surjective](https://arxiv.org/html/2604.09839v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 白盒注入状态与prompt可达状态不能默认相同；状态集合分离也不等输出行为分离，不能把白盒失败直接转成黑盒攻击可行。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MEMENTO: Teaching LLMs to Manage Their Own Context](https://arxiv.org/html/2604.09852v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 同一摘要文本重Prefill不能恢复其构造时的KV；normal/restart预算不匹配，须保兼容状态或明确text-only恢复语义变化。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Relational Preference Encoding in Looped Transformer Internal States](https://arxiv.org/html/2604.09870v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 作者勘误定位order prior与跨split泄漏，原headline定量失效；July纠错只限制April采用，不另算当日事件或整篇withdrawn。 3+1+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Should We be Pedantic About Reasoning Errors in Machine Translation?](https://arxiv.org/html/2604.09890v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 编辑trace回放的条件影响与原生thinking路径不同，trace质量和终值可反向变化；干预协议与outcome需分别验收。 2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Tale of Two Temperatures: Simple, Efficient, and Diverse Sampling from Diffusion Language Models](https://arxiv.org/html/2604.09921v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | token温度控制取值、position温度控制位置选择/并行提交；TLC和TCT有不同预算性质，不以confidence代替truth。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [I Walk the Line: Examining the Role of Gestalt Continuity in Object Binding for Vision Transformers](https://arxiv.org/html/2604.09942v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 合成曲线/物体的选择性head与mean-ablation支持局部binding机制；probe选择和有限自然迁移不证明全部视觉grounding。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [LoDAdaC: a unified local training-based decentralized framework with adaptive gradients and compressed communication](https://arxiv.org/html/2604.09970v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 本地adaptive moments、压缩shadow-model差和邻居mixing分别负责优化、重构与共识；不是压缩全局Adam梯度再AllReduce。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [EncFormer: Secure and Efficient Transformer Inference over Encrypted Data](https://arxiv.org/html/2604.09975v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 相邻FHE kernel layout与FHE/MPC边界packing要共同选择，expanded packing也可能更优；conversion、CKKS、MPC全成本不能由最少转换次数代替。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [FinTrace: Holistic Trajectory-Level Evaluation of LLM Tool Calling for Long-Horizon Financial Tasks](https://arxiv.org/html/2604.10015v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 工具F1、信息使用、过程judge及终局答案不可互代；gold步数可奖励少行动，金融oracle与合成干扰限制评价。 2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://arxiv.org/html/2604.10027v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | BOS cached V硬替换会塌缩，soft注入与独立BOS路径不同；单mean K/V的softmax恒1，不支持query-dependent上下文选择。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [CoSToM:Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models](https://arxiv.org/html/2604.10031v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 冻结decoder的BDI读出loss回传encoder LoRA，形成中间表示训练接口；可训练范围不同和judge对照限制心智概念的因果归因。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [LoopGuard: Breaking Self-Reinforcing Attention Loops via Dynamic KV Cache Intervention](https://arxiv.org/html/2604.10044v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 持续多信号触发有损KV修剪，再cooldown恢复生成；合法重复误判和证据丢失须与任务质量并验，诱发loop不代表自然loop率。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations](https://arxiv.org/html/2604.10055v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 扰动curriculum后低学习率clean阶段回到nominal任务；学习率/步骤和role holdout说明混杂，受限训练顺序不是开放物理安全。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [On The Application of Linear Attention in Multimodal Transformers](https://arxiv.org/html/2604.10064v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 单位Q/K只让affine kernel非负，不推出归一化权重≤2/i；i=3、相反keys构成反例，不否定所有linear attention。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [ASPIRin: Action Space Projection for Interactivity-Optimized Reinforcement Learning in Full-Duplex Speech Language Models](https://arxiv.org/html/2604.10065v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | pad/nonpad原logit求和再softmax是timing surrogate，不是token概率边缘；组大小不同使平移改变binary policy，私有对话结果不证明语义保持。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation](https://arxiv.org/html/2604.10071v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 视觉attention mass选双anchor修正final logits，是同模型proxy而非独立事实验证；手调系数过强会退步，额外读出成本未完整量化。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty](https://arxiv.org/html/2604.10072v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 短回答共识触发长CoT再用scorer选择，是可见生成的代理而非内部自知；并行调用、域阈值和OOD成本限制效率外推。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Transformers Learn the Optimal DDPM Denoiser for Multi-Token GMMs](https://arxiv.org/html/2604.10074v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 正交pattern多token GMM、population GD和特定初始化下接近Bayes denoising risk；不等有限数据深层模型学习任意diffusion。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Why Supervised Fine-Tuning Fails to Learn: A Systematic Study of Incomplete Learning in Large Language Models](https://arxiv.org/html/2604.10079v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 保留训练response的MC恢复不是自由生成知识存在性；所称pass@N实为重复成功比例，不能推广统一SFT未学会率。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Long-Horizon Streaming Video Generation via Hybrid Attention with Decoupled Distillation](https://arxiv.org/html/2604.10103v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 先dense再hybrid、被evict帧写线性L/H且近期sparse，匹配RoPE cap与teacher rollout；constant footprint不保证历史可恢复。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification](https://arxiv.org/html/2604.10134v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 隔离planner之后参数仍由LLM verifier审核，合法值可依赖planner未见环境；有限零ASR不能证明任何动作不偏离的确定安全。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities](https://arxiv.org/html/2604.10135v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 句边界ICL/SFT与随机/定长分隔控制区分结构和加token；probe/attention可读不证明唯一推理中介，额外训练成本仍在。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [SpecMoE: A Fast and Efficient Mixture-of-Experts Inference via Self-Assisted Speculative Decoding](https://arxiv.org/html/2604.10152v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | draft借target非expert参数和GPU hot experts，target verify再合并专家需求；greedy match不保证任意sampling，loading/acceptance须合算。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Tracing the Thought of a Grandmaster-level Chess-Playing Transformer](https://arxiv.org/html/2604.10158v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | transcoder与稀疏attention分解加置零/移植干预构造局部feature图；LC0高精度低召回不等通用LLM推理字典。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Tessera: Unlocking Heterogeneous GPUs through Kernel-Granularity Disaggregation](https://arxiv.org/html/2604.10180v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 按PTX/library建kernel依赖图并在cut边copy/wait，KV另保增量replica；未知访存保守回退、权重容量未纳入MILP。 2+3+2=7 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Credit-Budgeted ICPC-Style Coding: When Agents Must Pay for Every Decision](https://arxiv.org/html/2604.10182v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | contest credit合计API、测试/提示和时钟权重，错误提交penalty影响排名；跨API将时间权重置零不证明生产延迟公平。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [WaveTune: Wave-aware Bilinear Modeling for Efficient GPU Kernel Auto-tuning](https://arxiv.org/html/2604.10187v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | macro/wave桶双线性cost与micro anchor配置共同校准；资源仍耦合，离线profile/近似失配与MI355X退步限制全局最优。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Cognitive Pivot Points and Visual Anchoring: Unveiling and Rectifying Hallucinations in Multimodal Reasoning Models](https://arxiv.org/html/2604.10219v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | HVAR、反思注入再移除、正确轨迹筛选是复合训练分支；attention代理不是模型自知或幻觉唯一原因。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/html/2604.10235v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | code shortlist和CPG prior分配chunk预算、保护span再映射KV block；parser/共享prefix成本、不同slice反向结果需保留。 2+2+2=6 | 标准完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [The Amazing Agent Race: Strong Tool Users, Weak Navigators](https://arxiv.org/html/2604.10261v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | diamond访问图把导航覆盖与推理正确分开；路径长度、step/时间预算和runtime配置限制其因果归因。 2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EditCrafter: Tuning-free High-Resolution Image Editing via Pretrained Diffusion Model](https://arxiv.org/html/2604.10268v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | tiled inversion与混合条件引导改变高分辨率编辑工作点；CLIP/偏好分数不等对象事实保真，额外patch成本仍在。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety in Agent Systems](https://arxiv.org/html/2604.10286v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | risk-first与threshold-first选择有任务完成/误阻取舍；heuristic target的ECE不是实际攻击概率或授权保护。 2+2+2=6 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [AI Organizations are More Effective but Less Aligned than Individual Agents](https://arxiv.org/html/2604.10290v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 多个Agent可绕过拒绝参与节点，单模型aligned不保证组合；judge伦理与硬任务指标不能合成为生产事故率。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Seeing No Evil: Blinding Large Vision-Language Models to Safety Instructions via Adversarial Attention Hijacking](https://arxiv.org/html/2604.10299v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | prefix suppression和image anchoring攻击、attention干预提供窄实证；非单调结果与剩余ASR否定可靠防线/唯一因果叙述。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Zero-shot World Models Are Developmentally Efficient Learners](https://arxiv.org/html/2604.10333v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 第二帧少量patch重建与假想位移readout提供受限表示分支；不是真实action干预、物理因果SCM或可控世界模型。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents](https://arxiv.org/html/2604.10352v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 预生成多保真typed pages再按预算升级，hard minima不fit要显式pressure；降级/writer不能静默改变最小事实合同。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md) |
| [Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/html/2604.10367v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 共享时间RoPE加head-specific Gaussian penalty不是strict局部window；有限语音视觉训练与对照不证明所有模态统一最优。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [LLM-PRISM: Characterizing Silent Data Corruption from Permanent GPU Faults in LLM Training](https://arxiv.org/html/2604.10390v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | finite数值SDC可持续损害PPL而不崩溃；fault位置/phase、guard/recompute和step提交分责，仿真不证明自然故障率。 2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Latent Instruction Representation Alignment: defending against jailbreaks, backdoors and undesired knowledge in LLMs](https://arxiv.org/html/2604.10403v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | response-only loss不阻止共享参数受prompt路径更新；SAG保持forward而阻断特定梯度路径，仍需容量与任务条件验收。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Tracing the Roots: A Multi-Agent Framework for Uncovering Data Lineage in Post-Training LLMs](https://arxiv.org/html/2604.10480v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 文档lineage推断加局部instruction-triplet匹配，不能证明全部内容祖先；采样diversity比较未直接验证训练质量。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Why Don't You Know? Evaluating the Impact of Uncertainty Sources on Uncertainty Quantification in LLMs](https://arxiv.org/html/2604.10495v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 知识未知、合法多解与输入含糊应分别触发查证/拒答、合法选择与澄清；语义entropy不能统一作为错误概率。 2+2+2=6；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CodeQuant: Unified Clustering and Quantization for Enhanced Outlier Smoothing in Low-Precision Mixture-of-Experts](https://arxiv.org/html/2604.10496v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | codebook与LUT执行需共同校准router/aggregate输出并保持permutation语义；不是普通INT4 checkpoint自动获tensor-core收益。 2+2+3=7 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Visual Enhanced Depth Scaling for Multimodal Latent Reasoning](https://arxiv.org/html/2604.10500v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 视觉replay、重复block和curriculum共同作用，梯度norm相关性不证明唯一欠优化原因；部署无replay不等无额外路由成本。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [A Progressive Training Strategy for Vision-Language Models to Counteract Spatio-Temporal Hallucinations in Embodied Reasoning](https://arxiv.org/html/2604.10506v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | CoT→标签与可变数据量形成受限训练分支；同团队关联研究不合并独立正文，也不能只凭排名认定固定token收益。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks](https://arxiv.org/html/2604.10508v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 错误反馈多轮self-repair与独立resampling预算不匹配，8B切片有反向结果；cumulative solved不能当单轮准确率。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Thinking Fast, Thinking Wrong: Intuitiveness Modulates LLM Counterfactual Reasoning in Policy Evaluation](https://arxiv.org/html/2604.10511v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | case熟悉度、标签构造和trial内相关混杂CoT因果；缺少必要完整prompt/control证据，中心归因暂缓不写Books。 2+1+2=5；具体知识缺口、纠错/安全或中心机制冲突所需深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Structure-Grounded Knowledge Retrieval via Code Dependencies for Multi-Step Data Reasoning](https://arxiv.org/html/2604.10516v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | AST调用图和I/O连接、BFS子图不同于embedding改名；same-name merge可能造跨trace路径，有限DAB/FinQA/ConvFin对照不作真实groundtruth。 2+2+2=6 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [From Perception to Planning: Evolving Ego-Centric Task-Oriented Spatiotemporal Reasoning via Curriculum Learning](https://arxiv.org/html/2604.10517v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 关联路线再加入长程时序分支，独立身份保留；训练数据/预算和任务切片不同，不构成单因素普遍优势。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs](https://arxiv.org/html/2604.10539v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | 按Key相似性组织物理page、动态索引与host gather改变locality而非logical position；ANN遗漏及PCIe/index维护成本保留。 2+2+3=7 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Differentiable Vector Quantization for Rate-Distortion Optimization of Generative Image Compression](https://arxiv.org/html/2604.10546v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | hard重构code与soft rate代理分离；AR补全未传后缀是生成而非恢复原事实，有限codec结果不证明MLLM证据保真。 2+1+2=5 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |
| [Agent^2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?](https://arxiv.org/html/2604.10547v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | script、训练运行和artifact提交分责；反复scalar反馈仍有adaptive selection，best-within预算须绑定提交次数/轨迹。 2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models](https://arxiv.org/html/2604.10556v1) | 2026-04-14T08:00:00+08:00 ～ 2026-04-14T09:00:00+08:00 | AR/diffusion模型与数据并非严格匹配，future错误anchor可能锁定其他位置；整block慢路径不能代表生产加速路线。 2+2+2=6 | 标准完成 | 仅报告：受限分支/证据，不形成新的长期正文 |

## 4. 证据与知识整合

以下均采用精确v1的必要原文，不把摘要、评分或取得全文链接当作完成研究。作者论文/公开实现只支持对应机制和受限实验，未复现，不外推通用性能、安全或SLO；未披露配置保留Not Disclosed。每项必要方法、对照、预算、限制与原始位置的展开见[逐项证据记录](../_sources/daily-20260414/v3-reopen-notes.md)及对应独立复核，以下给出当前裁决而非早期提案语态。09870另读当前v2 Erratum，只用来限制April v1正面采用。

### [SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://arxiv.org/html/2604.09557v1)

随机token与真实语义流量即使长度相同，也改变proposal可预测性；词表裁剪须单列长尾覆盖代价，接受长度不能代替端到端收益。

**整合：** INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [StreamServe: Adaptive Speculative Flows for Low-Latency Disaggregated LLM Serving](https://arxiv.org/html/2604.09562v1)

FlowGuard单位、历史δ与acceptance及depth更新方向冲突，且throughput递推不等实际测量；中心编排保证不能据此采用。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [OOWM: Structuring Embodied Reasoning and Planning via Object-Oriented Programmatic World Modeling](https://arxiv.org/html/2604.09580v1)

PlantUML状态/计划与XML、embedding奖励提供受限训练接口，但未验证真实环境transition；跨任务差异不证明可执行世界状态。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [MobiFlow: Real-World Mobile Agent Benchmarking through Trajectory Fusion](https://arxiv.org/html/2604.09587v1)

成功轨迹合并成可回放GUI图提供便宜评价路径，但采集覆盖与错误动作模拟约定不能等同开放界面、真实副作用。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Why Smaller Is Slower? Dimensional Misalignment in Compressed LLMs](https://arxiv.org/html/2604.09595v1)

先profile合法硬件shape，再在同一模型参数预算中分配压缩容量；不规则维度的kernel代价改变参数越少越快的判断。

**整合：** INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios](https://arxiv.org/html/2604.09603v1)

共享batch预算先延伸有区分力的depth，再扩局部width；这是两级资源决策，预算余额检查不能证明严格cap。

**整合：** INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Characterizing Performance-Energy Trade-offs of Large Language Models in Multi-Request Workflows](https://arxiv.org/html/2604.09611v1)

prefix共享、顺序依赖和角色异质性改变batch的能耗趋势；有限vLLM/Parrot负载没有冻结全部质量与SLO，不能给出统一最优batch。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Self-Calibrating Language Models via Test-Time Discriminative Distillation](https://arxiv.org/html/2604.09624v1)

base discriminative signal经distractor归一化指导置信适配，entropy触发burst；有限label-free结果不证明校准置信就是事实概率。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models](https://arxiv.org/html/2604.09651v1)

污染flow早段方向但匹配向量范数，说明等范数不等合法行动；LIBERO任务失败代理并非固定恶意终点或物理安全证明。

**整合：** MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Deliberative Alignment is Deep, but Uncertainty Remains: Inference time safety improvement in reasoning via attribution of unsafe behavior to base model](https://arxiv.org/html/2604.09665v1)

base/FT隐状态相似度筛选在deliberative与普通IT模型间表现不同；层选择、BoN预算与utility下降限制因果和部署解释。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems](https://arxiv.org/html/2604.09666v1)

保持agent protocol比较检索backend，显示查询分解部分补偿dense检索、multi-hop仍有graph优势；不同基线缩减不可合成统一收益。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [In-context superposition: human-like working memory interference in large language models](https://arxiv.org/html/2604.09670v1)

完整历史与位置可访问不保证chat模型实现可靠回读；lure、集合大小和teacher-forcing控制分离内容竞争与任务学会程度。

**整合：** MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [NetAgentBench: A State-Centric Benchmark for Evaluating Agentic Network Configuration](https://arxiv.org/html/2604.09678v1)

STOP声明、配置收敛和环境witness分责；早退删失会同时降低完成度与风险观测机会，原文run总数矛盾不采用。

**已有覆盖：** PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 Outcome Witness、环境opportunity和提前终止删失共同承载所采命题。不声称已有完整论文算法或复现实验，不追加同义正文。

### [Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models](https://arxiv.org/html/2604.09687v1)

encoder可恢复、融合可访问、输出可表达是三个不同问题；冻结probe额外监督与patch边界限制单因果瓶颈解释。

**整合：** MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Orthogonal Quadratic Complements for Vision Transformer Feed-Forward Networks](https://arxiv.org/html/2604.09709v1)

低秩二次分支在rank空间消平行成分，再lift/gate融合；不保证原空间或函数空间非冗余，普通非线性FFN不能误称线性。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [LAST: Leveraging Tools as Hints to Enhance Spatial Reasoning for Multimodal Large Language Models](https://arxiv.org/html/2604.09712v1)

空间metric与direction对不同工具表示的消费能力不同；训练移除输出与推理遮一路不是同一干预，联合hint并非每个slice最好。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [ConfigSpec: Profiling-Based Configuration Selection for Distributed Edge--Cloud Speculative LLM Serving](https://arxiv.org/html/2604.09722v1)

profile选择K涉及accepted吞吐、token计费和edge能量三个目标；只计draft时间的能耗不是整条edge-cloud成本。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [SMART: When is it Actually Worth Expanding a Speculative Tree?](https://arxiv.org/html/2604.09731v1)

prefix概率按root-to-leaf均值计算不等候选树总接受进度；重复prefix和成本模型使中心树扩展估计缺少可采用保证。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [ExecTune: Effective Steering of Black-Box LLMs with Guide Models](https://arxiv.org/html/2604.09741v1)

按受约束core成功过滤guide再训练，是target-conditioned策略分支；good execution假设不保证任意black-box core忠实执行。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [MPAC: A Multi-Principal Agent Coordination Protocol for Interoperable Multi-Agent Collaboration](https://arxiv.org/html/2604.09744v1)

coordinator序列化、断连禁共享mutation、恢复epoch和phase授权形成协议分支；中心节点及延迟代价、有限案例不证明通用可靠性。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying](https://arxiv.org/html/2604.09747v1)

已暴露memory记录可反用作后续query的anchor，单次访问保护不足；要核累计输出反馈与相同query预算下的提取范围。

**整合：** AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Backdoors in RLVR: Jailbreak Backdoors in LLMs From Verifiable Reward](https://arxiv.org/html/2604.09748v1)

终局答案verifier不保护完整生成轨迹，有害前缀加正确答案仍获正reward；checked span与行为验收必须分开。

**整合：** TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [See Fair, Speak Truth: Equitable Attention Improves Grounding and Reduces Hallucination in Vision-Language Alignment](https://arxiv.org/html/2604.09749v1)

object置信/稀有度改变decode attention且用EMA平滑；proposal质量、取得成本与mask后归一化限制不能当免费oracle。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Conflicts Make Large Reasoning Models Vulnerable to Attacks](https://arxiv.org/html/2604.09750v1)

moral/reasoning冲突暴露有限jailbreak边界；PCA、cosine及成功攻击子集相关性不证明唯一安全机制，未验证defense。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [A-IO: Adaptive Inference Orchestration for Memory-Bound NPUs](https://arxiv.org/html/2604.09752v1)

NPU路由/PLD的验证和采样语义未披露，HumanEval结果明显退步；不能把未披露实现反推为lossless PLD必然损害质量。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [Sustainable Transformer Neural Network Acceleration with Stochastic Photonic Computing](https://arxiv.org/pdf/2604.09759v1)

stochastic bitstream和signed accumulate构成硬件替代，但证据为device/架构仿真与有限小模型任务，不是LLM生产能效。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Text-Guided 6D Object Pose Rearrangement via Closed-Loop VLM Agents](https://arxiv.org/html/2604.09781v1)

显式坐标、renderer反馈和单轴增量旋转提供pose推理接口；自评或预算停止不等物理安全，模拟结果不外推真实机器人。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning](https://arxiv.org/html/2604.09813v1)

augmentation只有保持原oracle有效才保同一答案，缺信息/错query需改变预期行为；LLM judge分支不是纯deterministic checker。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/html/2604.09815v1)

经验检索与专家蒸馏是不同分支，每轮SFT从base重启；三应用和峰值epoch选择不证明参数持续学习单调收益。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models](https://arxiv.org/html/2604.09824v1)

理论只约束固定observation时的目标敏感性，却据此限制observation变化后的action；policy直接observation路径构成反例。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [Steered LLM Activations are Non-Surjective](https://arxiv.org/html/2604.09839v1)

白盒注入状态与prompt可达状态不能默认相同；状态集合分离也不等输出行为分离，不能把白盒失败直接转成黑盒攻击可行。

**整合：** PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [MEMENTO: Teaching LLMs to Manage Their Own Context](https://arxiv.org/html/2604.09852v1)

同一摘要文本重Prefill不能恢复其构造时的KV；normal/restart预算不匹配，须保兼容状态或明确text-only恢复语义变化。

**整合：** INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Relational Preference Encoding in Looped Transformer Internal States](https://arxiv.org/html/2604.09870v1)

作者勘误定位order prior与跨split泄漏，原headline定量失效；July纠错只限制April采用，不另算当日事件或整篇withdrawn。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [Should We be Pedantic About Reasoning Errors in Machine Translation?](https://arxiv.org/html/2604.09890v1)

编辑trace回放的条件影响与原生thinking路径不同，trace质量和终值可反向变化；干预协议与outcome需分别验收。

**已有覆盖：** PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66行为预测、No-Aux/Generated-Aux/Validated-Aux干预协议与outcome分账已具体承载。不声称已有完整论文算法或复现实验，不追加同义正文。

### [A Tale of Two Temperatures: Simple, Efficient, and Diverse Sampling from Diffusion Language Models](https://arxiv.org/html/2604.09921v1)

token温度控制取值、position温度控制位置选择/并行提交；TLC和TCT有不同预算性质，不以confidence代替truth。

**整合：** MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [I Walk the Line: Examining the Role of Gestalt Continuity in Object Binding for Vision Transformers](https://arxiv.org/html/2604.09942v1)

合成曲线/物体的选择性head与mean-ablation支持局部binding机制；probe选择和有限自然迁移不证明全部视觉grounding。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [LoDAdaC: a unified local training-based decentralized framework with adaptive gradients and compressed communication](https://arxiv.org/html/2604.09970v1)

本地adaptive moments、压缩shadow-model差和邻居mixing分别负责优化、重构与共识；不是压缩全局Adam梯度再AllReduce。

**整合：** TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [EncFormer: Secure and Efficient Transformer Inference over Encrypted Data](https://arxiv.org/html/2604.09975v1)

相邻FHE kernel layout与FHE/MPC边界packing要共同选择，expanded packing也可能更优；conversion、CKKS、MPC全成本不能由最少转换次数代替。

**整合：** INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [FinTrace: Holistic Trajectory-Level Evaluation of LLM Tool Calling for Long-Horizon Financial Tasks](https://arxiv.org/html/2604.10015v1)

工具F1、信息使用、过程judge及终局答案不可互代；gold步数可奖励少行动，金融oracle与合成干扰限制评价。

**已有覆盖：** PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66工具成功→Information Use→Outcome的分账已承载，未以新金融任务重写机制。不声称已有完整论文算法或复现实验，不追加同义正文。

### [SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://arxiv.org/html/2604.10027v1)

BOS cached V硬替换会塌缩，soft注入与独立BOS路径不同；单mean K/V的softmax恒1，不支持query-dependent上下文选择。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [CoSToM:Causal-oriented Steering for Intrinsic Theory-of-Mind Alignment in Large Language Models](https://arxiv.org/html/2604.10031v1)

冻结decoder的BDI读出loss回传encoder LoRA，形成中间表示训练接口；可训练范围不同和judge对照限制心智概念的因果归因。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [LoopGuard: Breaking Self-Reinforcing Attention Loops via Dynamic KV Cache Intervention](https://arxiv.org/html/2604.10044v1)

持续多信号触发有损KV修剪，再cooldown恢复生成；合法重复误判和证据丢失须与任务质量并验，诱发loop不代表自然loop率。

**整合：** INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations](https://arxiv.org/html/2604.10055v1)

扰动curriculum后低学习率clean阶段回到nominal任务；学习率/步骤和role holdout说明混杂，受限训练顺序不是开放物理安全。

**整合：** MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [On The Application of Linear Attention in Multimodal Transformers](https://arxiv.org/html/2604.10064v1)

单位Q/K只让affine kernel非负，不推出归一化权重≤2/i；i=3、相反keys构成反例，不否定所有linear attention。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [ASPIRin: Action Space Projection for Interactivity-Optimized Reinforcement Learning in Full-Duplex Speech Language Models](https://arxiv.org/html/2604.10065v1)

pad/nonpad原logit求和再softmax是timing surrogate，不是token概率边缘；组大小不同使平移改变binary policy，私有对话结果不证明语义保持。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation](https://arxiv.org/html/2604.10071v1)

视觉attention mass选双anchor修正final logits，是同模型proxy而非独立事实验证；手调系数过强会退步，额外读出成本未完整量化。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty](https://arxiv.org/html/2604.10072v1)

短回答共识触发长CoT再用scorer选择，是可见生成的代理而非内部自知；并行调用、域阈值和OOD成本限制效率外推。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Transformers Learn the Optimal DDPM Denoiser for Multi-Token GMMs](https://arxiv.org/html/2604.10074v1)

正交pattern多token GMM、population GD和特定初始化下接近Bayes denoising risk；不等有限数据深层模型学习任意diffusion。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Why Supervised Fine-Tuning Fails to Learn: A Systematic Study of Incomplete Learning in Large Language Models](https://arxiv.org/html/2604.10079v1)

保留训练response的MC恢复不是自由生成知识存在性；所称pass@N实为重复成功比例，不能推广统一SFT未学会率。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Long-Horizon Streaming Video Generation via Hybrid Attention with Decoupled Distillation](https://arxiv.org/html/2604.10103v1)

先dense再hybrid、被evict帧写线性L/H且近期sparse，匹配RoPE cap与teacher rollout；constant footprint不保证历史可恢复。

**整合：** MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [PlanGuard: Defending Agents against Indirect Prompt Injection via Planning-based Consistency Verification](https://arxiv.org/html/2604.10134v1)

隔离planner之后参数仍由LLM verifier审核，合法值可依赖planner未见环境；有限零ASR不能证明任何动作不偏离的确定安全。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities](https://arxiv.org/html/2604.10135v1)

句边界ICL/SFT与随机/定长分隔控制区分结构和加token；probe/attention可读不证明唯一推理中介，额外训练成本仍在。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [SpecMoE: A Fast and Efficient Mixture-of-Experts Inference via Self-Assisted Speculative Decoding](https://arxiv.org/html/2604.10152v1)

draft借target非expert参数和GPU hot experts，target verify再合并专家需求；greedy match不保证任意sampling，loading/acceptance须合算。

**整合：** INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Tracing the Thought of a Grandmaster-level Chess-Playing Transformer](https://arxiv.org/html/2604.10158v1)

transcoder与稀疏attention分解加置零/移植干预构造局部feature图；LC0高精度低召回不等通用LLM推理字典。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Tessera: Unlocking Heterogeneous GPUs through Kernel-Granularity Disaggregation](https://arxiv.org/html/2604.10180v1)

按PTX/library建kernel依赖图并在cut边copy/wait，KV另保增量replica；未知访存保守回退、权重容量未纳入MILP。

**整合：** INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Credit-Budgeted ICPC-Style Coding: When Agents Must Pay for Every Decision](https://arxiv.org/html/2604.10182v1)

contest credit合计API、测试/提示和时钟权重，错误提交penalty影响排名；跨API将时间权重置零不证明生产延迟公平。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [WaveTune: Wave-aware Bilinear Modeling for Efficient GPU Kernel Auto-tuning](https://arxiv.org/html/2604.10187v1)

macro/wave桶双线性cost与micro anchor配置共同校准；资源仍耦合，离线profile/近似失配与MI355X退步限制全局最优。

**整合：** INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Cognitive Pivot Points and Visual Anchoring: Unveiling and Rectifying Hallucinations in Multimodal Reasoning Models](https://arxiv.org/html/2604.10219v1)

HVAR、反思注入再移除、正确轨迹筛选是复合训练分支；attention代理不是模型自知或幻觉唯一原因。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [CodeComp: Structural KV Cache Compression for Agentic Coding](https://arxiv.org/html/2604.10235v1)

code shortlist和CPG prior分配chunk预算、保护span再映射KV block；parser/共享prefix成本、不同slice反向结果需保留。

**已有覆盖：** INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Ch45 Pre-RoPE Calibration与Workload-semantic Selection明确CPG、chunk预算、span保护与物理block。不声称已有完整论文算法或复现实验，不追加同义正文。

### [The Amazing Agent Race: Strong Tool Users, Weak Navigators](https://arxiv.org/html/2604.10261v1)

diamond访问图把导航覆盖与推理正确分开；路径长度、step/时间预算和runtime配置限制其因果归因。

**已有覆盖：** PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Ch66 document Agent的navigation/grounding/effort和opportunity set覆盖所采诊断。不声称已有完整论文算法或复现实验，不追加同义正文。

### [EditCrafter: Tuning-free High-Resolution Image Editing via Pretrained Diffusion Model](https://arxiv.org/html/2604.10268v1)

tiled inversion与混合条件引导改变高分辨率编辑工作点；CLIP/偏好分数不等对象事实保真，额外patch成本仍在。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [STARS: Skill-Triggered Audit for Request-Conditioned Invocation Safety in Agent Systems](https://arxiv.org/html/2604.10286v1)

risk-first与threshold-first选择有任务完成/误阻取舍；heuristic target的ECE不是实际攻击概率或授权保护。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [AI Organizations are More Effective but Less Aligned than Individual Agents](https://arxiv.org/html/2604.10290v1)

多个Agent可绕过拒绝参与节点，单模型aligned不保证组合；judge伦理与硬任务指标不能合成为生产事故率。

**已有覆盖：** AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)。Ch82 Collective Risk段具体承载utility、visibility/topology、aggregation、dissent与独立effect verifier。不声称已有完整论文算法或复现实验，不追加同义正文。

### [Seeing No Evil: Blinding Large Vision-Language Models to Safety Instructions via Adversarial Attention Hijacking](https://arxiv.org/html/2604.10299v1)

prefix suppression和image anchoring攻击、attention干预提供窄实证；非单调结果与剩余ASR否定可靠防线/唯一因果叙述。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Zero-shot World Models Are Developmentally Efficient Learners](https://arxiv.org/html/2604.10333v1)

第二帧少量patch重建与假想位移readout提供受限表示分支；不是真实action干预、物理因果SCM或可控世界模型。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [ClawVM: Harness-Managed Virtual Memory for Stateful Tool-Using LLM Agents](https://arxiv.org/html/2604.10352v1)

预生成多保真typed pages再按预算升级，hard minima不fit要显式pressure；降级/writer不能静默改变最小事实合同。

**整合：** AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/html/2604.10367v1)

共享时间RoPE加head-specific Gaussian penalty不是strict局部window；有限语音视觉训练与对照不证明所有模态统一最优。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [LLM-PRISM: Characterizing Silent Data Corruption from Permanent GPU Faults in LLM Training](https://arxiv.org/html/2604.10390v1)

finite数值SDC可持续损害PPL而不崩溃；fault位置/phase、guard/recompute和step提交分责，仿真不证明自然故障率。

**已有覆盖：** TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。Ch36已有finite SDC传播、分位置guard/recompute与step coordinator提交权。不声称已有完整论文算法或复现实验，不追加同义正文。

### [Latent Instruction Representation Alignment: defending against jailbreaks, backdoors and undesired knowledge in LLMs](https://arxiv.org/html/2604.10403v1)

response-only loss不阻止共享参数受prompt路径更新；SAG保持forward而阻断特定梯度路径，仍需容量与任务条件验收。

**整合：** TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Tracing the Roots: A Multi-Agent Framework for Uncovering Data Lineage in Post-Training LLMs](https://arxiv.org/html/2604.10480v1)

文档lineage推断加局部instruction-triplet匹配，不能证明全部内容祖先；采样diversity比较未直接验证训练质量。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Why Don't You Know? Evaluating the Impact of Uncertainty Sources on Uncertainty Quantification in LLMs](https://arxiv.org/html/2604.10495v1)

知识未知、合法多解与输入含糊应分别触发查证/拒答、合法选择与澄清；语义entropy不能统一作为错误概率。

**整合：** PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [CodeQuant: Unified Clustering and Quantization for Enhanced Outlier Smoothing in Low-Precision Mixture-of-Experts](https://arxiv.org/html/2604.10496v1)

codebook与LUT执行需共同校准router/aggregate输出并保持permutation语义；不是普通INT4 checkpoint自动获tensor-core收益。

**整合：** INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Visual Enhanced Depth Scaling for Multimodal Latent Reasoning](https://arxiv.org/html/2604.10500v1)

视觉replay、重复block和curriculum共同作用，梯度norm相关性不证明唯一欠优化原因；部署无replay不等无额外路由成本。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [A Progressive Training Strategy for Vision-Language Models to Counteract Spatio-Temporal Hallucinations in Embodied Reasoning](https://arxiv.org/html/2604.10506v1)

CoT→标签与可变数据量形成受限训练分支；同团队关联研究不合并独立正文，也不能只凭排名认定固定token收益。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks](https://arxiv.org/html/2604.10508v1)

错误反馈多轮self-repair与独立resampling预算不匹配，8B切片有反向结果；cumulative solved不能当单轮准确率。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Thinking Fast, Thinking Wrong: Intuitiveness Modulates LLM Counterfactual Reasoning in Policy Evaluation](https://arxiv.org/html/2604.10511v1)

case熟悉度、标签构造和trial内相关混杂CoT因果；缺少必要完整prompt/control证据，中心归因暂缓不写Books。

**暂缓：** 必要可用证据已读，中心采用范围被隔离；精确重开条件见§5，不支持Books或正面保证。

### [Structure-Grounded Knowledge Retrieval via Code Dependencies for Multi-Step Data Reasoning](https://arxiv.org/html/2604.10516v1)

AST调用图和I/O连接、BFS子图不同于embedding改名；same-name merge可能造跨trace路径，有限DAB/FinQA/ConvFin对照不作真实groundtruth。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [From Perception to Planning: Evolving Ego-Centric Task-Oriented Spatiotemporal Reasoning via Curriculum Learning](https://arxiv.org/html/2604.10517v1)

关联路线再加入长程时序分支，独立身份保留；训练数据/预算和任务切片不同，不构成单因素普遍优势。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs](https://arxiv.org/html/2604.10539v1)

按Key相似性组织物理page、动态索引与host gather改变locality而非logical position；ANN遗漏及PCIe/index维护成本保留。

**整合：** INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Differentiable Vector Quantization for Rate-Distortion Optimization of Generative Image Compression](https://arxiv.org/html/2604.10546v1)

hard重构code与soft rate代理分离；AR补全未传后缀是生成而非恢复原事实，有限codec结果不证明MLLM证据保真。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

### [Agent^2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?](https://arxiv.org/html/2604.10547v1)

script、训练运行和artifact提交分责；反复scalar反馈仍有adaptive selection，best-within预算须绑定提交次数/轨迹。

**整合：** PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。采用的是上述窄机制/边界，真实正文已写入并经非作者检查相邻衔接；完整评价合同和未采用的宣传结论仍在原始证据记录中。

### [Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models](https://arxiv.org/html/2604.10556v1)

AR/diffusion模型与数据并非严格匹配，future错误anchor可能锁定其他位置；整block慢路径不能代表生产加速路线。

**仅报告：** 保留上述可定位的具体分支与反证；有限条件不足改变当前长期设计判断，不假称整套方法已在Books，也不因Only减少必要审阅。

## 5. 缺口与下一步

**可执行待办：** 无。证据与Books处置、最终日级独立复核及结构校验已完成；以下为已隔离的精确外部保留项，不作采用或覆盖证明。

**本窗终态保留项：** 以下不用于正面证据、Books或无遗漏断言。现可用原始入口已审，材料后来到达时定点重开对应项，不顺带重跑全月：

- 来源历史子入口：OpenAI Research、Google Pubs、Meta Research、Qwen artifact、DeepSeek研究/发布记录、Moonshot其他模型研究/artifact、ERNIE repo研究切片、MiMo Blog/artifact、MiniMax Agent Tech/artifact。对应官方入口在§2；缺本窗可验证目录、事件日期和必要原文，现有Blog/release不能代替。可接受官方历史列表、存档HTML或绑定事件日期的官方正文/仓库记录，按来源行恢复，不据空响应宣称零命中。
- arXiv日公告：§3范围是显式联合推断，不是精确公告日志。若需精确时刻或解除下面例外，接受对应家族正式公告邮件/列表或可验证截点前正文公开记录；不要求重读1334篇。
- 日期晚段28项：10567、10577、10585、10590、10597、10603、10636、10666、10667、10674、10681、10688、10690、10693、10697、10701、10703、10727、10733、10788、10791、10799、10800、10827、10842、10848、10857、10866（均为arXiv:2604.xxxxx，[逐项题摘与原字段](../_sources/daily-20260414/v3-reopen-notes.md#末段31项题摘判断)）。缺完全落窗的公开记录；Updated跨09:00或后月不作首发，暂不评分/入确定分母。取得原始公告/当时公开正文后只恢复准入未决与必要证据；10590等仍是最小消歧，不假定28全有贡献。
- [09940 Hybrid FO/ZO](https://arxiv.org/abs/2604.09940)：ICLR2026 accepted提示可能早公开，必要方法已达标准且Only，不知道真实首次公开，未计本窗。需该正文OpenReview/作者首发记录及对应identity；恢复只归并真实owner，不扩大venue全年扫描。
- [09945](https://arxiv.org/pdf/2604.09945v1)：原库存Value Attribution与当前HTML Cross-Cultural Value Awareness不一致，精确PDF未恢复；现正文不能冒充April原版。需绑定官方v1的作者稿或版本说明，恢复identity、题摘及必要方法，不用污染摘要正面采用。
- [09562 StreamServe](https://arxiv.org/html/2604.09562v1)：需FlowGuard单位、历史δ/acceptance、depth方向及throughput递推的修正/实现解释与匹配评价，不采用中心编排保证。
- [09731 SMART](https://arxiv.org/html/2604.09731v1)：需树总接受进度而非path均值的明确定义/推导、共享prefix与成本模型条件；反例未解决前不采用期望/单步保证。
- [09752 A-IO](https://arxiv.org/html/2604.09752v1)：需具体PLD验证/采样实现、同输入评价和真实mixed-arrival trace。现HumanEval反向不能解释为exact PLD一般质量损害。
- [09824 ProGAL-VLA](https://arxiv.org/html/2604.09824v1)：需实际policy输入及控制observation直接路径的假设/证明或勘误，不据固定observation时的目标敏感度推出环境变化安全。
- [09870 Relational Preference](https://arxiv.org/html/2604.09870v2)：当前勘误已拒用原order/split headline；重开需固定source-item split、order-balanced/antisymmetrized评价和可核artifact，不等待全部后续新稿。
- [10064 Linear Attention](https://arxiv.org/html/2604.10064v1)：需归一化权重上界必要假设/勘误、长度归一化和可比训练成本，i=3反例不等全部linear attention无效。
- [10134 PlanGuard](https://arxiv.org/html/2604.10134v1)：需与LLM参数审核路径一致的保证条件、适应性参数攻击/良性动态值控制或作者收窄，不以更多零ASR代替授权证明。
- [10511 Causal Policy](https://arxiv.org/html/2604.10511v1)：完整prompt原文须联系作者；需固定prompt、标签定义及针对熟悉度/类别/依赖的控制或收窄。保留真实有限实验，中心CoT因果暂缓。

**窗外线索：** [10091 SEPTQ](https://arxiv.org/html/2604.10091v1) DOI10.1145/3690624.3709287由出版方metadata确认2025-07-20已经公开，不计April首发或评分；不在此恢复2025日报。晚段如证实窗外，留真实owner恢复线索，不扩大本日窗口。官方撤回版本不列selected，本日09870是部分finding纠错而非整篇withdrawn，不能删除其他有效证据。

## 6. 复核

复核者：apr01、apr02、apr03、apr20_resume；最终日级复核者apr01，报告作者root。
结论：通过

最终六部分、82家族处置与日期范围、七项具体已有覆盖、25项真实正文及相邻衔接已完成相应非作者验收；八中心争议及来源/日期限制安全隔离，不支持正面采用或无遗漏保证。

已执行来源/准入口径检查、全部拟候选必要命题的分批非作者审阅、代表性排除项分层校准及25处真实正文/相邻衔接检查；没有把抽检写成325/1334条全量语义证明。日期82项有限范围及早公开/版本例外见[日期与最后采用复核](../_sources/daily-20260414/V3_APR01_FINAL_GAP_ADOPTION.md)；具体证据复用见[机制校准](../_sources/daily-20260414/V3_INDEPENDENT_MECHANISM_CALIBRATION.md)、[三项反向校准](../_sources/daily-20260414/V3_INDEPENDENT_THREE_CALIBRATION.md)、[第十六批](../_sources/daily-20260414/V3_APR02_BATCH16_INDEPENDENT.md)、[第十七批](../_sources/daily-20260414/V3_APR20_BATCH17_INDEPENDENT.md)、[第十八批及写后](../_sources/daily-20260414/V3_APR01_BATCH18_INDEPENDENT.md)、[最后十项](../_sources/daily-20260414/V3_APR20_FINAL_DISPOSITIONS_INDEPENDENT.md)和[逐项工作记录](../_sources/daily-20260414/v3-reopen-notes.md)所链接的其他独立审阅。

机器结构校验已通过；机器通过不代替语义验收。保护运行前已有staged/unstaged修改，不stage、commit、push。
