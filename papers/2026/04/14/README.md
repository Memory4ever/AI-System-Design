# Daily Research — 2026-04-14

**规范：** V3
**窗口：** 2026-04-13T09:00:00+08:00 ～ 2026-04-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-14T13:23:09+08:00
**窗口说明：** 用户授权仅补来源遗漏；保留原窗口、82候选整行日期/评分及连续原§4，不迁移旧材料。
**补充窗口：** 2026-04-13 ～ 2026-04-13
**冻结候选日期：** [原报告](../_sources/daily-20260414/baseline-before-supplement-20261014.md)

## 1. 结论

本轮仅补Apr13 BJT完整自然日，新增38个唯一材料家族：32项必要深入完成、2项标准完成、4项中心争议终态隔离；Books为30实际整合（15唯一owner、60正文段）、1具体已有覆盖、3仅报告、4暂缓。30处新写的正文/完整局部邻接/本人末注均已非作者实际POST通过。另AdaCubic、Seed CAF、BiasedSwarm三个必要first-public资格门隔离，不计确定候选、不评分、不进Books。普通可执行待办0，独立reader已实际六部分DAY通过；保存完成态仅由同一独核尾区的实际FINAL确认，不用旧完成标签替代。

原82整行/日期/评分、原小时窗和连续原§4完整冻结，未受影响的必要证据、25真实旧整合POST与7具体已有覆盖按层复用，不计本次新写；旧完成声明不是补查证明。合计120家族＝64深入完成/44标准完成/12争议；Books55整合/8已有覆盖/45仅报告/12暂缓。来源历史slice、日期资格与中心争议均不支持无遗漏、正面Coverage/Evidence或性能/安全保证。

新增知识集中于producer与consumer的支持域：完整条件/声学滚窗适配、静态本体条件、finite-Δ课程、camera轨迹producer、显式rule学习、逐video参数decoder与量化执行分责；评价/路由侧保pair实验配置、synthetic或reference的证据权限、generated formal target和runtime state。所有新写保近文反侧、全部费用与回退，不把小模型/理论/负面或模块组合当准入或硬排。

以下为原窗口已验收且未变化的有效结果，仅按层复用：

本日保留82个唯一论文家族；必要证据已处理为32项深入完成、42项标准完成、8项中心采用争议隔离。Books为25项实际机制正文及非作者写后通过、7项具体已有覆盖、42项仅报告、8项暂缓。最终日级独立验收通过，普通可执行待办为零；完成不表示历史来源缺口或中心争议已获正面证明。

主要增量是：推理性能必须共同结算真实语义流量、proposal/verify、硬件shape与物理KV locality；表示可恢复、融合可访问和输出可表达不能混为一个能力；终局reward、生成全轨迹、环境witness及多轮memory累计暴露要分别验收。新机制均插入现有owner论证，保留旧方案成立条件、代价和回退，而非在章末追加摘要。

原始三页为2262个去重身份，09548～10881的1334个只是有界查漏子范围；实际浏览325条主题标题线索、阅读155项完整题摘，均不等当日有效论文数或全文队列。82候选不含28项未能确认落窗的晚段线索、09940早公开线索及09945版本身份缺口。前分母关闭保留具体原因，未用旧Weekly或旧筛选标签生成本日。

## 2. 来源覆盖

本轮按Apr13日期和ROADMAP主题检查14每日源，未加载每周组；只复用本日旧入口中未变的历史目录层，同时读新的官方core。下表当前三项已检查只指声明的Research目录切片，十项机构及arXiv必要历史入口受阻已精确隔离；arXiv辅助检索另外受限，不是完成Coverage或组织无遗漏。原窗口来源记录仍由[原本日记录](../_sources/daily-20260414/v3-reopen-notes.md)支持，不拿旧Complete授补查。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)；当前Research入口、旧RSS1230的Apr13 06Z身份；Cloudflare官方core本次重读 | 受阻 | R2具体贡献EX；Research历史目录不足 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)；当前Research初始10及旧170 publishedOn层，Apr09 16:34Z→Apr14 13:01Z边界未变 | 已检查 | 限该Research目录，不等所有author artifact |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)；当前DeepMind264第一段Apr22→Mar22；Google April Blog9，Apr13 Vantage core重读 | 受阻 | R2具体EX非应用标签；Google Pubs历史切片缺 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)；当前Research空提取及旧Blog相邻身份层 | 受阻 | FAIR可绑定Apr13的Research列表缺；空响应非零 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/)；旧动态40 Apr02→Apr15/静态60层；本次完整page_config API60条date/title/id止2025Dec23；retrieval HTTP200仅2651707/4781799 bytes，35s停止 | 受阻 | `SUP_Qwen-current-config_20261014.json`完整；retrieval partial不授读完，本窗其他Research/artifact不足 |
| SRC-DEEPSEEK | [DeepSeek](https://www.deepseek.com/)；当前官网入口定位、旧Research Jun24→Feb25及动态Apr24→Dec01目录未变层 | 受阻 | 当前展示不能证明本窗历史切片完整 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)；当前Blog26最新2025Nov07；CLI1.32.0 Apr13 11:39:51Z core4及PR1843旧有效同事件核 | 受阻 | 100K/unknown-type局部patch具体EX；其他模型/组织artifact历史缺 |
| SRC-TENCENT-HUNYUAN | [全部Research](https://hunyuan.tencent.com/research)；当前Research空提取；旧publicList page1/size100/renderType0 total9 Apr30/23→Feb13层；本次IAB42.6s timeout/kernel reset | 已检查 | 限公开全部目录有效边界；browser失败不授UI已读或组织零更新 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)；当前日期排序Research目录实际覆盖到Apr01切片，相邻Apr29→Apr07→Apr01 | 已检查 | 有查看更多，不称全站完整；不扩窗外正文 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)；当前论文20/246 page1止May26；旧type1 US count20 tokens0/20/40 total242 Apr12 16Z→Apr10/09/07，type2 Blog95 tokens0/20/40止2025Dec17；CAF11521官方repo/v1题摘具名重开 | 受阻 | Apr13 CMS目录不授CAF正文首公开；单项日期门隔离 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)；当前Blog10 Apr15→Feb06→2025；repo仅2025Jun30 release旧有效层 | 受阻 | Blog边界有限，repo其他历史Research/artifact不足 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)；当前Paper8 Jun29→Mar13→Feb03；Blog15无日期 | 受阻 | Paper目录边界不含Apr13，无日期Blog不授零 |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)；当前EN12 May26→Mar18/CN redirect及旧Apr27→Mar18；AgentTech3 Sep19/Sep22/Oct08日期；旧CLI Apr10 1.0.7→Apr16 1.0.8层 | 受阻 | 不读窗外全文；model/artifact/AgentTech历史切片缺 |
| SRC-ARXIV | [官方月列表](https://arxiv.org/list/cs.CL/2026-04?show=2000)的有界相关标题与173主题元数据；实际停止/接口限制见下段 | 受阻 | 必要历史日公告未完整恢复，辅助检索受限；非逐篇正式日公告，不授全分类召回；具体first-public例外在§5 |

实际查询/停止：arXiv submitted-range被服务端改写为quoted而返回61456/23815的失败响应，只浏览首150/100无关标题，不作主题Coverage/队列；tight title API rate exceeded、历史日列表cache miss。DataCite `doi:10.48550/arxiv.2604.* AND created:[2026-04-13 TO 2026-04-13]` 加language/transformer/attention/LLM/MoE/diffusion/world/VLA/agent/GPU/training/inference/kernel/memory/optimizer/representation标题主题实际173单页，created只作发现；999宽请求截断无效。正确月入口 `/list/cs.<cat>/2026-04?show=2000` 中CL/LG/AI实际完整前缀1693/1165/755及目标08549–09547切片65/105/26；DC/PL/IR/MA/AR/OS/PF完整响应的目标分别9/5/23/16/5/2/0；RO partial完整前缀556止19946、目标24。CV初partial590止05527未达目标，不计覆盖；合法 `skip=600&show=500` 的partial436完整项05621→09710包含目标119，目标区间完整后停止，不追尾部。错误2604路径InvalidYear和show800的400响应均只是失败接口，不作零命中。

以上目标元数据去重381身份，与173交133，都是线索inventory，不是381题摘已筛或强制全文队列；实际只处理具名相关线索。173中31与已有Apr13同事件身份去重，后续月线索中已有有效候选身份56也只作定点去重，不把邻日候选/评分继承。具名正文/机构core及当前withdraw/correction轻信号按下述有效审阅处理；未返回尾部、未具名库存不授已审或EX。原件和独核在[唯一本日补查记录](../_sources/daily-20260414/SUP_SOURCES_20261014.md#2-本轮实际来源与准入)，不另建账本。

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
| [WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models](https://arxiv.org/html/2604.08558v1) | 2026-04-13 | 完整conditioning永久可读、仅generated acoustics滚窗，并用teacher/curriculum让consumer适配改变的读域。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning](https://arxiv.org/html/2604.08780v1) | 2026-04-13 | 已知静态engineering spec进入encoder与逐步learned dynamics，真实posterior和跨本体reward尺度另分责。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Discrete Meanflow Training Curriculum](https://arxiv.org/html/2604.08837v1) | 2026-04-13 | 由FM初始化，finite-Δ stopped自目标课程渐缩，再进入连续MF的末JVP阶段，修正全程无JVP/廉价一步话术。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation](https://arxiv.org/html/2604.09212v1) | 2026-04-13 | canonical absolute speaker/content/order生成每agent相对role视图，身份、读入角色和authority不能合并。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md) |
| [Adaptive Simulation Experiment for Large Language Model Policy Optimization](https://arxiv.org/html/2604.08779v1) | 2026-04-13 | 在有限policy集上按pairwise信息分配实验预算以辨识winner，理论winner/探索条件与经验停止规则分责。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/html/2604.08646v1) | 2026-04-13 | branch-specific Q与早中晚KV交互构造temporally-localized edit配对，改变训练support而非只增加编辑条数。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/html/2604.08719v1) | 2026-04-13 | 训练中冻结视频generator但反传损失，并仅回送预测视频适配planner；online规划丢generator、offline自反馈另计。 1+2+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning](https://arxiv.org/html/2604.09378v1) | 2026-04-13 | bundled classifier权重、attacker parser与普通runtime代码联合触发，modelartifact审核不能替effect-time权限门。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Precise Shield: Explaining and Aligning VLLM Safety via Neuron-Level Guidance](https://arxiv.org/html/2604.08881v1) | 2026-04-13 | activation/down-column共同importance proxy确定局部LoRA更新面，安全transfer与utility回归必须共同验收。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [DrBencher: Can Your Agent Identify the Entity, Retrieve Its Properties and Do the Math?](https://arxiv.org/html/2604.09251v1) | 2026-04-13 | 代码重算gold只认证计算路径，不认证实体/属性和题意真值，筛难人口与browse×compute误差分层。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LLM-Rosetta: A Hub-and-Spoke Intermediate Representation for Cross-Provider LLM API Translation](https://arxiv.org/html/2604.09360v1) | 2026-04-13 | typed IR的preserve/strip信息责任与request-scoped stream state分开，结构往返不授跨provider语义保真。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-GATEWAY [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [CIR+CVN: Bridging LLM Semantic Understanding and Petri-Net Verification for Concurrent Programs](https://arxiv.org/html/2604.09318v1) | 2026-04-13 | generated CIR verification target、SID诊断与独立existentialgoal gate分责，不让形式自洽认证源码对应。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [TouchAnything: Diffusion-Guided 3D Reconstruction from Sparse Robot Touches](https://arxiv.org/html/2604.08945v1) | 2026-04-13 | known contact pose与触觉depth/normal/mask转换成virtualcamera条件，整体diffusion prior和触觉softloss共同补全。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation](https://arxiv.org/html/2604.09497v1) | 2026-04-13 | reference-based triplet encoder提供评分接口，synthetic标签/human agreement与真实parser-fallback消费者证据分开。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism](https://arxiv.org/html/2604.09544v1) | 2026-04-13 | signed harmful-gradient减absolute benign保护的坐标干预，在generation/refusal/recognition等不同协议验收，不授真实独立harm子空间。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering](https://arxiv.org/html/2604.09297v1) | 2026-04-13 | failuretrace驱动bundle编辑/optimizer提示，再按pass-cost archive与parent-relative guard选择，发布门仍独立。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：AGENT-PROMPT [Ch74](../../../../books/part-07-agent/74-prompt.md) |
| [SCoRe: Clean Image Generation from Diffusion Models Trained on Noisy Images](https://arxiv.org/html/2604.09436v1) | 2026-04-13 | 原生成样本经lowpass后另跑SDEdit，spectral-cutoff到noise-level是待校准代理，不是原图无偏恢复。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Dynamic Ranked List Truncation for Reranking Pipelines via LLM-generated Reference-Documents](https://arxiv.org/html/2604.09492v1) | 2026-04-13 | 生成pivot定义相对cutoff/滑窗stride与跨窗参照；有限judge验证不是每query强制门，earlycut质量/全费需近文。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning](https://arxiv.org/html/2604.09529v1) | 2026-04-13 | mask-KL/entropy构造visual伪target、reasoning confidence与negative visual-token credit分责，不把adv负值当答案必错。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Tango: Taming Visual Signals for Efficient Video Large Language Models](https://arxiv.org/html/2604.09547v1) | 2026-04-13 | 扩展候选后按locality/diversity cluster选最高attention代表，metric的ST-RoPE不认证真实实体/单调距离或无损merge。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Litmus (Re)Agent: A Benchmark and Agentic System for Predictive Evaluation of Multilingual Models](https://arxiv.org/html/2604.08970v1) | 2026-04-13 | reduced可读corpus与combined gold分开，在五缺证scenario评价预测；语言近邻与同family都只人口代理。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EGLOCE: Training-Free Energy-Guided Latent Optimization for Concept Erasure](https://arxiv.org/html/2604.09405v1) | 2026-04-13 | 逐step decoded-Tweedie CLIP repulsion与prompt-retention共同改变latent，是软目标和额外链，不能当concept安全擦除。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AssemLM: Spatial Reasoning Multimodal Large Language Models for Robotic Assembly](https://arxiv.org/html/2604.08983v1) | 2026-04-13 | fixed/moving几何相关特征投到LLM embedding、9D pose以201bins固定9tokens监督，geometry warmup不授全LM SE3保证。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Modality-Aware Zero-Shot Pruning and Sparse Attention for Efficient Multimodal Edge Inference](https://arxiv.org/html/2604.08971v1) | 2026-04-13 | active-mask只进入saliency observer，经训练后offline materialize合法attention/FFN子网，不是request动态能耗controller。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios](https://arxiv.org/html/2604.09377v1) | 2026-04-13 | domain taxonomy造数后实际调用all-candidates生成质量/费用标签，type-mixture预测是有限经验router接口，不授ELBO校准。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：PLATFORM-GATEWAY [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [Integrated Electro-Optic Attention Nonlinearities for Transformers](https://arxiv.org/html/2604.09512v1) | 2026-04-13 | MZM clipped近似非线性、积分/格式/noise与重训consumer共同定义支持域，器件波形速度不授全Transformer降本。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [CT-1: Vision-Language-Camera Models Transfer Spatial Reasoning Knowledge to Camera-Controllable Video Generation](https://arxiv.org/html/2604.09201v1) | 2026-04-13 | 图像/语言camera-context提出Euclidean轨迹分布，以多尺度target监督后交video消费者，轨迹与渲染证据分责。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Automated Instruction Revision (AIR): A Structured Comparison of Task Adaptation Strategies for LLM Systems](https://arxiv.org/html/2604.09418v1) | 2026-04-13 | labelled cluster局部contrast学IF/THEN规则，再以mistake/anchor最小修订，自报rule-ID非因果或语义certificate。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：AGENT-PROMPT [Ch74](../../../../books/part-07-agent/74-prompt.md) |
| [TinyNeRV: Compact Neural Video Representations via Capacity Scaling, Distillation, and Low-Precision Inference](https://arxiv.org/html/2604.09220v1) | 2026-04-13 | 同骨架缩width的逐video参数decoder以teacher low/high/focal目标适配，再独立验权重量化consumer和实际执行。 2+1+2=5；具体owner差额所需深入 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Event-Driven Temporal Graph Networks for Asynchronous Multi-Agent Cyber Defense in NetForge_RL](https://arxiv.org/html/2604.09523v1) | 2026-04-13 | irregular event interval驱动hidden ODE推进/arrival gate与时间discount credit，engine duration规则和actor/critic观察另分责。 2+2+2=6；具体owner差额所需深入 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Artifacts as Memory Beyond the Agent Boundary](https://arxiv.org/html/2604.08756v1) | 2026-04-13 | 含确定性environment artifact/reference的history支持删除冗余观察，但不授动作/value充分性或物理memory节约。 2+1+2=5；必要受影响命题深入 | 深入完成 | 仅报告：具体观察不改变长期接口，见§4 |
| [Ge²mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer](https://arxiv.org/html/2604.08894v1) | 2026-04-13 | nonuniform activation编码与group/window布局形成有限SNN操作点观察，但未取得新的通用consumer或质量—总费接口。 2+1+2=5；标准 | 标准完成 | 仅报告：具体观察不改变长期接口，见§4 |
| [Discrete Token Modeling for Multi-Stem Music Source Separation with Language Models](https://arxiv.org/html/2604.09371v1) | 2026-04-13 | 固定stem条件分解与codec-roundtrip评价错位是局部观察，未新增拟采的顺序/分离约束或总费选择。 2+1+2=5；标准 | 标准完成 | 仅报告：具体观察不改变长期接口，见§4 |
| [AlphaLab: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs](https://arxiv.org/html/2604.08590v1) | 2026-04-13 | experiment debrief持久playbook供后续actor消费与独立promotion门已由Ch80具体承载；自建eval漏错/搜索波动不授playbook独立因果。 2+1+2=5；必要受影响命题深入 | 深入完成 | 已有覆盖：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)，episode/playbook消费与采用门 |
| [Hierarchical Kernel Transformer: Multi-Scale Attention with an Information-Theoretic Approximation Analysis](https://arxiv.org/html/2604.08829v1) | 2026-04-13 | causal score/downsample之外的全序列融合gate仍访问future，严格/ε因果中心主张与物理费用必须隔离。 2+1+2=5；必要受影响命题深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Multi-Agent Decision-Focused Learning via Value-Aware Sequential Communication.](https://arxiv.org/html/2604.08944v1) | 2026-04-13 | value-aware代理有有限潜力，但TV/value下界方向、实际inner/IFT与committed-action消费不一致，中心保证争议。 2+2+2=6；必要受影响命题深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Semantic Rate-Distortion for Bounded Multi-Agent Communication: Capacity-Derived Semantic Spaces and the Communication Cost of Alignment](https://arxiv.org/html/2604.09521v1) | 2026-04-13 | capacity-derived quotient提出通信结构边界，但rate下界factor/support、proxy upper和当前block重建对象未闭，中心采用隔离。 2+2+3=7；必要受影响命题深入 | 争议 | 暂缓：中心采用隔离，见§5 |
| [Risk-seeking conservative policy iteration with agent-state based policies for Dec-POMDPs with guaranteed convergence](https://arxiv.org/html/2604.09495v1) | 2026-04-13 | 有限agent-state联合action/nextstate与risk-CPI改变优化对象；α0反例及fixedλ到退火objective映射未闭，中心收敛暂缓。 2+2+2=6；必要受影响命题深入 | 争议 | 暂缓：中心采用隔离，见§5 |

 补充候选以下38项只归Apr13 date-only。依据官方ID在公告赋号、Apr12 Sunday常规公告/无holiday、April Available、v1 Apr13处理簇与08548/08549/09547/09548相邻边界的有限一致性推断；不把Submitted/Updated/DOI-created孤证改作first-public，不授正式逐篇日公告或全网first，具名先稿例外单项隔离。QWM及NetForge采用exact-v1题名，不用current后版本标题/摘要回填。

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


### Apr13补充：逐家族证据与实际处置

以下补充不改动上方连续原§4；必要命题读到关键机制/评价/反证即止，未核代码或复现，未读无关附件不作block。每项只按唯一family计数。

### [WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models](https://arxiv.org/html/2604.08558v1)

精确v1，2+1+2=5；必要源范围及配置：Daily 2026-04-14 supplement Apr13，supp_apr14_author；[WAND exact-v1](https://arxiv.org/html/2604.08558v1)必要§2–4/Tables1–5，2+1+2=5，具体 gap 深入。仅采用完整 conditioning/仅 acoustic rolling 读域及 teacher/curriculum 适配，不授 fixed-P 外 O(1)、各语言普适无损或生产 SLO；SparkTTS 中文 CER 2.14→2.35 与感知质量反侧保留。未复现实验；日期仅官方 April 身份＋原始 v1 簇/相邻 batch/正常 Sunday 公告的有限 Apr13 date-only 合证，不拿 March Submitted 作首发。

生成对象的局部性还可以把保留域分成完整条件与滚动历史，而不必把条件也压进固定 quota。对自回归语音，目标文本、参考音频和任务标签规定内容与声线，生成声学 token 主要支撑近邻连续性；一条受限分支永久保留该请求的 conditioning KV，只对 generated acoustics 保留 W 个近期位置。完整文本等条件有 P 个 token 时，活动读集与 cache 仍为 O(P+W)；只有 P 固定、codec rate 与窗口合同不变，才相对生成步数有常数上界。注意力质量集中只提供候选局部性，不能认证远处语义可以无损删除。

从 full-attention 训练的模型直接删历史可能损坏内容，因此还要让 consumer 适配部署读域：由 ground-truth acoustic CE 和 full-attention teacher 分布约束学生，再渐缩 window 并将 soft mask 变成部署限制。这增加 teacher、适配数据、训练与新模型身份，distillation 不恢复 exact FullKV。[WAND 的必要对照](https://arxiv.org/html/2604.08558v1)中，三种 AR-TTS、固定语音 rate、100 小时英语/一轮适配及 Seed-TTS EN/ZH 只支持该受测分支；SparkTTS 中文 CER 和部分感知指标仍退步，不能说全部语言无损或任意长文本/声学输出都已保真。新条件增长、远程韵律/证据依赖、质量或真实费用失配时，扩大窗口并重新适配，或保留完整历史与成熟 FullKV；服务并发与 SLO 继续独立验收。

Books整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，source-family `SF-2026-ARXIV-2604-08558` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning](https://arxiv.org/html/2604.08780v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08780v1)标题Toward Hardware-Agnostic Quadrupedal World Models via Morphology Conditioning，必要III–VI/TI、PME/RSSM/ARN与sameμPPO/B2反侧。2+2+2=6具体gap深入，只采用static-spec条件transition与distribution-bound迁移；不授sufficient statistic、隐状态独立、普适物理/真实安全/WM唯一因果。未核代码或复现。

若没有可信的解析传播器，但机器人质量、肢长和关节构型在部署前已知，也不必全靠运动历史把它们重新辨识。一条不同于解析 ego 分解的分支将这些 engineering specifications 编成静态条件，分别进入 observation encoder 和每一步 learned recurrent dynamics；真实 observation 仍更新 posterior，想象 rollout 才使用 prior，policy消费其 latent。这把可预先声明的本体条件与运行中的动态估计分责，不证明隐状态已经统计独立，也不让规格书替代摩擦、执行器背隙或真实传感反馈。跨本体训练的 reward 范围可以逐本体用分位数/EMA归一，但该尺度状态不是不同 reward 语义等价的证书。

显式条件化增加规格解析、归一、异质采样和 reward-scale状态，并把训练支持域变成迁移边界。[QWM的必要对照](https://arxiv.org/html/2604.08780v1)将同一形态向量提供给 model-free policy，支持 learned dynamics的受限迁移分支；但 held-out Go1/ANYmal-D 的插值成功与重型 B2 的失败同时存在，不能说任意本体零适配或 universal physics。作者选定两本体的实机运行不授物理安全、唯一因果或无模型失配。规格错误、未知接触/负载或训练域外时，应重校准并恢复本体专用模型、可信 simulator/解析残差路径与短 horizon真实反馈；单本体、规格缺失或隐式辨识已足够时，原 monolithic dynamics 仍合理，动作提交继续由第26章 controller验收。

Books整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，source-family `SF-2026-ARXIV-2604-08780` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Discrete Meanflow Training Curriculum](https://arxiv.org/html/2604.08837v1)

精确v1，2+1+2=5；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08837v1)§2–5/T1–5，2+1+2=5具体gap深入，只采用FM初始化/finiteΔ自目标课程/末JVP责任与稳定ceil。保2k+2k预算、noCFG/extra127条件、ImageNet96epstage5发散及48ep一步FID不胜多步；T4百分比误标不采。未复现或核实现。

少步模型的训练预算也可以沿目标近似的难度分阶段，而不只改变部署的求值次数。直接用瞬时场和区间平均速度的微分关系监督 MeanFlow，会支付 JVP，并在有限预算下遇到优化困难；另一条受限分支从已经训练的 Flow Matching 模型开始，用有限时间间隔构造 stopped 自目标，逐阶段缩小间隔，最后才切回连续 MeanFlow 的 JVP 目标。这改变的是训练目标、近似尺度和导数计算责任，不是部署时运行这些课程阶段，也不是全程免 JVP 或精确一步积分。

离散间隔变细还会暴露新的稳定性压力。DMF 的受限图像对照中，CIFAR-10把原 FM 预训与后续适配共同计入四千 epoch；ImageNet latent 路线又使用额外样本估计速度、robust loss和无 CFG 配置，不能只把适配 epoch 当总成本。后者在较细的第五阶段曾发散，48 epoch 的一步 FID 仍不及原多步模型，因此阶段变多不等质量或稳定性单调变好。finite target 的额外 forward、末段 JVP、初始化和校准均付费；latent、间隔、质量或费用失配时，缩短离散课程、重新校准转段点，或保留原 FM、多步 solver 与成熟蒸馏，而不从 per-batch速度推出通用端到端加速。[必要机制与反侧](https://arxiv.org/html/2604.08837v1)。

Books整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，source-family `SF-2026-ARXIV-2604-08837` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation](https://arxiv.org/html/2604.09212v1)

精确v1，2+1+2=5；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09212v1)§2.1/2.2/3.4T3/3.5T4/5与AppL，2+1+2=5具体gap深入；只采用canonical absolute speaker→deterministic per-agent view。保DS p=.460、two-agent/cap20/temp0、probe非人格真值与echo人口口径争议；不授allpartners同authority、多Agent已实测、零echo/安全。未核实现/复现。

排序和去重之前，共享对话还要保留“谁说了什么”。同一条全局 transcript 不能原样当作每个 Agent 的 user/assistant 历史：某位伙伴的 assistant turn 对另一位 Agent 并不是自产生回答。可先用绝对 speaker identity 保存原 content 与顺序，再为当前消费者确定性映射 SELF/PARTNER 等相对角色。角色视图不改写 canonical history，也不把所有伙伴的内容合并为同一种事实或权限；原身份仍用于追溯与冲突处理。

这增加消费者身份、view revision 和重放规则，而不是又生成一份不可回查的摘要。[SPASM的受限双Agent对照](https://arxiv.org/html/2604.09212v1)支持该输入接口分支，但 English instruction-tuned、固定温度与最多二十条 utterances 的结果不证明开放协作中的人格保持或零 echo。Embedding probe不是偏好真值，DeepSeek的motivation维度未显著改善；echo人审人口的正文/表注口径亦未统一，不能把局部人工一致率扩到全部记录。角色/来源不能可靠恢复、多人接口未校准或消费者行为退步时，保留原typed transcript与显式speaker标签，不让相对role获得授权。Multi-Agent委派与实际执行仍由第82章承担。

Books整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)，source-family `SF-2026-ARXIV-2604-09212` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Adaptive Simulation Experiment for Large Language Model Policy Optimization](https://arxiv.org/html/2604.08779v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08779v1)§2–4.3/5.1–5.2，2+2+2=6具体保证边界深入；只采finite配置/pair实验分配→受限winner识别，不授finitePAC/全prompt最优/安全；保uniqueCondorcet/非传递反侧、iidstationary/structuredFisherlocal/探索非退化、heuristicρ未直接理论支持、真实30×10oracle/CI90/判错随机及全部费用。未核代码/复现。

若目标不是估计完整排名，而是在冻结的有限部署配置中选出一个候选，比较预算还可以按“当前哪些 pair 最能区分胜者”分配。先冻结 prompt、guardrail、temperature、任务分布与 judge；每次在同一随机任务上比较两个配置的输出，更新 pairwise evidence，再决定下一对。未经结构约束时直接估各对胜率；采用 Bradley–Terry 分支时，可用局部分离的 Fisher 信息引导分配，并保留 forced exploration 与正则化状态。这优化的是实验采样，不让被挑中的配置因“可部署”而取得事实或安全资格。

分配规则与停止证书须分别核验。[LLM-PO的条件分析](https://arxiv.org/html/2604.08779v1)把有限集合、iid/stationary comparison及unique Condorcet winner等作为识别条件；有maxmin候选不等于一定存在逐对胜出的Condorcet winner，偏好环或judge漂移会改变问题。结构化分支还需模型、探索support与信息矩阵成立，Fisher只提供local surrogate。作者实跑的heuristic停止阈值未获同一理论直接支持，有限小任务的PCS与较少query不能认证任意预算δ-PAC或全prompt最优；真实oracle也来自有限预采样，rule/LLM judge仍有条件偏差。预采样、候选生成、judge、分配求解与复验全计费；支持不足、环关系或测量身份变化时，保留均匀预算、原始pair evidence与Unknown/并列，重新定义选择目标而不硬停授予winner。

Books整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，source-family `SF-2026-ARXIV-2604-08779` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/html/2604.08646v1)

精确v1，2+1+2=5；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08646v1)§3.1–3.3/4.1–4.5/T2–3/5，2+1+2=5具体gap深入；仅jointbranch Q/KV读域与temporal edit-pair support，不采ConcatK shape/收益唯一因果/仅100K总预算/zero-shotimage。保百万主线与100Kedit-only差异、82sample/80video Qwen3VL32B/短clip反侧与全部費。未核实现/复现。

视频编辑的训练配对还必须覆盖“改动从何时发生”，而不只有全片持续存在的变化。先编辑首帧再传播，在目标始终开启时简单合理，却难以提供片中新增或消失的监督。一条受限构造分支共同去噪source与target视频，各自保留query，再在选定阶段交换或拼接两branch的KV，使它们共享场景而容许局部时序差异；早、中、晚阶段的互动读域不同，不是对源视频做任意真因果干预。生成的aligned pair仍须核内容、时序和未编辑区域，不能因共享attention就授事实对齐。

配对构造的收益还要与底座适配分开。[InsEdit的必要消融](https://arxiv.org/html/2604.08646v1)同时涉及生成/重建/保留初始化、image-video配比和prompt人口，不能把最终质量独归KV交互。合法SwapKV/ConcatKV分支可作接口说明，ConcatK公式的KV长度未闭合，不照录唯一recipe；main Stage2百万级generation/editing与100K edit-only消融也不是同一总预算。合成与过滤、语义encoder、双branch去噪、适配和50步部署均付费，短clip的VLM judge不认证长时关系保持或数据真值。互动失配、长程/复杂关系失败或净成本不合算时，保留可靠人工/原始pair、首帧传播或显式mask编辑，按temporal support与最终质量独立验收。

Books整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，source-family `SF-2026-ARXIV-2604-08646` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/html/2604.08719v1)

精确v1，1+2+2=5；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08719v1)§3.1–3.5/4.1–4.4/T1/3/4，1+2+2=5具体gap深入；只采training self-generated video feedback/online planner/offline video分责，不把offline control反馈移植到training实现。保Vicuna7B/SD1.5/AnimateDiff、8H80050k三阶段与matchediterations非FLOPs、worldquery+generator联变、longhorizon退化；4.1未来帧计数不闭不采完整recipe，不授真实safety/运行SLO。未核artifact/复现。

共享监督之外，还可以把生成的未来观测回送训练中的planner，而不让在线动作路径每次都运行视频生成器。一条受限分支由LLM不同query分别形成waypoint与world条件，视频generator消费后者；单步联合训练后，冻结generator，在短展开中把预测视频再次送入感知/语言路径，让生成损失继续更新planner。这是训练期的自生成feedback与参数适配，不是已经执行的未来观测，也不同于plan-first只让image消费计划。

[LMGenDrive的有限驾驶对照](https://arxiv.org/html/2604.08719v1)在线只输出planning并丢弃diffusion，离线视频路线才持续自回馈；两者的费用、累计误差与验收人口必须分开。移除world query/generator联变、相同iteration不等相同FLOPs，故不认证视频监督唯一因果；长horizon生成会漂移，CARLA闭环DS不授真实道路安全或最坏deadline。预训视觉、联合与多步训练、离线视频、真实观测和controller全部计费；生成反馈失配、规划回归或成本不合算时，保留专用planner、原联合监督与短horizon真实反馈，不把好看的未来帧交为事实或动作许可。

Books整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，source-family `SF-2026-ARXIV-2604-08719` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning](https://arxiv.org/html/2604.09378v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09378v1)§2–4.3/6/C–D，2+2+2=6安全深入；只采parser→bundledclassifier→threshold→payload分责，不采BA功能真值/ASR事故率/host突破或防御有效。保13skills8trigger+5controls、571/396与sweep500/348分母、primaryA800/English/sim/canary与全部费。未核artifact或复现。

Skill产物还可能把“何时走哪个分支”藏进附带的learned classifier，而不把恶意指令写进本次prompt。外部作者同时控制parser、weights与代码时，可以将普通参数组合规范化为classifier输入，再以阈值决定执行声明功能还是另一个payload分支。代码仍含实际effect，权重只是隐藏条件；审清说明或少量良性调用不能替代parser、model、threshold和代码的联合产物身份，也不能让该classifier批准权限。

[BadSkill的受限模型实验](https://arxiv.org/html/2604.09378v1)将负例路由正确率与trigger-aligned分支率分开；前者不证明所有声明任务正确，后者也不是实际窃取事故率。攻击者预制接口/模型/分支、English轻量模拟及写marker的canary，不证明突破正确host权限或production stack；部分已知触发表现与普通utility也不能授已验证防御。模型训练、产物审核、组合probe、sandbox和effect-time检查均计费；来源、更新或条件覆盖不可信时，隔离model-bearing skill、保留最小权限与独立effect approval，再用受限行为核验决定是否放行。普通可信无模型wrapper仍可保留较轻检查，不把opaque weights当作免审代码。

Books整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，source-family `SF-2026-ARXIV-2604-09378` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Precise Shield: Explaining and Aligning VLLM Safety via Neuron-Level Guidance](https://arxiv.org/html/2604.08881v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08881v1)§3.1–3.3/Eq5–12/Alg1/4.1–4.4与必要C/D，2+2+2=6安全深入；只采probe→FFN row-masked LoRA接口，不采true safety子空间、全部utility保持、<.03%等总费或唯一实现。保Llama MMVet55.2→54/53.9、MGSM67.7→66.1、1280human>92%无双评/CI披露、Qwen TR争议数值不采、partial transfer与全部费。未核实现/复现。

更新面还可以由受限行为probe提出，而不只按rank或层名选择。对FFN中间坐标，分别从带refusal的有害输入与良性输入，由平均activation与down-projection列共同构成重要性代理，取有害top-K与良性top-K的差集，再用row mask约束up/gate的LoRA增量。这把“在哪里更新”与低秩因子分责；所选坐标只是该probe人口的候选支持，不是已识别独立的安全语义，也不保证删除了所有通用能力干扰。

[PreciseShield的必要多语/多模态对照](https://arxiv.org/html/2604.08881v1)只支持该受限适配分支，跨语言/模态transfer仍部分且不对称；neuron数量或重叠与ASR相关不能独归语言相似性或唯一safety机制。MM-Vet/MGSM存在退步，单judge与有限human核也不授无bias；原masked-update公式与伪码forward不完全一致，不发布唯一训练recipe。probe、refusal标签、mask身份、适配、完整forward/backward与utility回归均付费，少量trainable参数不等总训练省费。人口、模型坐标或utility失配时，重新probe并回归原LoRA/完整适配与独立policy检查，不让adapter或activation放大替代第72章外部权限/安全gate。

Books整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，source-family `SF-2026-ARXIV-2604-08881` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [DrBencher: Can Your Agent Identify the Entity, Retrieve Its Properties and Do the Math?](https://arxiv.org/html/2604.09251v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09251v1)§3.1–3.3/4.1/5.1–5.2/AppA，2+2+2=6评价资格深入；只采answer-first codegold与question/entity/property语义资格、difficulty-filter人口分责，不重引科学应用。保354→268/159双评α.30/作者adjudication、V1/V2各10/τ.5温.7/1、过滤5%vs评分2%、3call/defaultAPI及全部费；低分不授唯一失败因果。未核实现/复现。

可执行gold也可以在出题前生成：先从冻结源取得entity链与参数，由template代码计算答案，再将线索和计算需求写成问题，最后重算并检查泄漏或歧义。这减少“先写题再猜答案”的失配，却只证明代码消费了给定参数；源值陈旧、把中间entity属性错归目标或把关系释义改写过头，都能让重算完全一致而问题仍错。Question、entity/property路径、源snapshot、formula/code和gold因此应可共同回查，不让executable reference自签语义真值。

难度过滤另改变最终人口：先以closed-book多次作答排除简单题，再让生成模型带browser/code工具复测，保留下的不是自然请求分布，也不保证新Agent同样困难。[DrBencher的必要人审](https://arxiv.org/html/2604.09251v1)中，354生成题经人审仅268可用，排除陈旧源后才提高的有效率不能覆盖原分母；双评子集的一致性仍低且经作者裁定，后续低answer accuracy不独自定位检索或计算根因。构造、取源/重算、两阶段tool验证、独立语义审核均付费；源版本、entity归属或题意不能确认时，修正并版本化gold、隔离该题或保留人工/稳定任务基线，不把筛出的难题或大样本自动授benchmark可信。

Books整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，source-family `SF-2026-ARXIV-2604-09251` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [LLM-Rosetta: A Hub-and-Spoke Intermediate Representation for Cross-Provider LLM API Translation](https://arxiv.org/html/2604.09360v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09360v1)§3.1–3.2/4.3/5.2–5.4/5.6/6.1–6.3，2+2+2=6协议边界深入；只采preserve同provider/strip跨provider分责和request-scopedtypedstream，不采普适semantic/transitive保持、無损或serviceSLO。保unsupported/topk/cachecontrol丢失与warnings、255/10/6测试人口、自写test循环风险、CPython3.10单硬件与proxy额外hop；未核artifact/实际API部署。

协议normalize还要区分“回到同一provider格式”与“换到另一provider”。可用中立typed IR保存message/content、tool call和generation controls，并在preserve模式另存provider-specific metadata，使同格式往返可检查结构保持；strip模式或目标不支持的字段却会丢失cache、sampling等能力。这不是所有provider语义本来相同，warnings也不认证丢字段无影响。Gateway应显式判断本请求哪些字段可转、哪些是不可降级合同，不兼容时拒绝或固定原provider，而非用JSON成功替代会话语义验收。

流式转换另需request-scoped状态：current block、tool-call identity/name、未完整的argument buffers，以及提前到达的finish/usage事件。累计part与delta、隐式与显式block边界不是可直接拼接的同一对象；转译只交付格式与顺序，不执行tool或批准effect。[LLM-Rosetta的有限测试](https://arxiv.org/html/2604.09360v1)支持四schema下的接口分支，255条stream测试与10条cross-provider案例不授所有API演进或transitive保真，自写测试与六个外部compliance案例亦有限。映射维护、buffer、校验、serialization和额外proxy hop都计费；字段新变、stream重建失败或总成本不成立时，重核adapter或保留provider-native客户端/原直连，不从converter微时延推出生产SLO。

Books整合：PLATFORM-GATEWAY [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md)，source-family `SF-2026-ARXIV-2604-09360` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [CIR+CVN: Bridging LLM Semantic Understanding and Petri-Net Verification for Concurrent Programs](https://arxiv.org/html/2604.09318v1)

精确v1，2+2+2=6；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.09318v1)§3.1–3.2/4.1/4.3/5.1–5.4/6.1–6.6，2+2+2=6具体target/采用边界深入；只generatedCIR/SIDdiagnostic与独立existentialgoal，不采arbitrarysource/fullsoundcomplete/统一接受recipe。保Alg1与Pattern5advisory接受口径、Pattern3deadlock叙述疑点、unknown spurious、9patterns/<250states/k≤3/d≤2/|D|≤3及未核artifact/生产规模；

形式化目标也可以在生成阶段改变验证对象，而不先从任意源码恢复并发关系。针对受限并发骨架，可先让模型提出全局命名的shared resources、保护映射与带statement identity的控制流，再由deterministic checker检查结构，机械翻译为有限状态的verification net；counterexample以原statement identity回指局部repair。这样把resource identity显式化，减少alias恢复压力，但证明对象是生成的模型，不是同一次生成的真实源码或原自然语言需求。

修掉已编码bug也不证明保留了要求的行为：还可独立检查指定critical outcomes是否至少在一个状态可达，拒绝通过删行为变得“无bug”的候选。[CIR/CVN的必要受限评价](https://arxiv.org/html/2604.09318v1)只支持这个验证接口，existential goal不是所有schedule的liveness；unknown过近似可能产生spurious path，goal释义与源码对应仍另验。算法与正文对advisory warning/接受规则以及一个bug-free例子的口径未闭合，不发布统一solver/repair保证。九个小pattern、有限变量与少轮修复不能代表生产规模，结构生成/检查、state exploration、修复与目标核验都付费；状态爆炸、目标遗漏或模型—源码对应不明时，保留源码静态/动态分析、独立语义检查与人工澄清，不由formal模型自一致批准真实程序。

Books整合：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md)，source-family `SF-2026-ARXIV-2604-09318` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [TouchAnything: Diffusion-Guided 3D Reconstruction from Sparse Robot Touches](https://arxiv.org/html/2604.08945v1)

精确v1，2+1+2=5；必要源范围及配置：Daily2026-04-14补Apr13，supp_apr14_author；[exact-v1](https://arxiv.org/html/2604.08945v1)§3.1–3.3/4.1–4.3/5，2+1+2=5具体bridge差额深入；只knowncontactpose/tactile depth-normal-mask→virtualcamera→整体prior提案与tactile softloss，不授arbitraryobject/未触实物真值或测得区hard保护。保280sim6categories/20touch、real14定性/不同sensor estimator与population、错texthallucination、A1001h+40min与全部费；未核实现/复现。

局部几何证据还可以由触觉而非视觉碎片提供。给定已配准的contact pose，先将触觉图估计为depth、normal与contact mask，再转成带位姿的virtual-camera rays，使原视觉重建器消费这些局部约束；预训练2D diffusion prior为欠约束的整体shape提供提案，触觉loss继续约束测得patch。测得patch、传感器估计、text条件和prior补全应保不同来源，不能因合成mesh连续就把未触区域当新观测或真实接触几何。

稀疏约束与生成prior还要分别付费：[TouchAnything的受限分支](https://arxiv.org/html/2604.08945v1)先以implicit SDF作低分辨率优化，再转显式tetrahedral表示以较高分辨率refine。20touch的模拟对象与固定实物不能认证任意物体，错误text会使未触区域hallucinate，更多文字也不保证更准。Sensor estimator、pose配准、场查询/渲染、两阶段优化与真实几何校验均计费，单A100每object约1小时再40分钟不是实时感知。接触/配准不可靠、prior支撑不足或费用过高时，保留触觉原patch、显式几何约束与专用重建，追加可靠观测或人工核验；推测shape仍不取得world dynamics或controller动作权。

Books整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，source-family `SF-2026-ARXIV-2604-08945` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference-Based LLM Evaluation](https://arxiv.org/html/2604.09497v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§2–5/§8/C，2+1+2=5具体scorer-gap深入；仅训练triplet encoder与parser-fallback/consumer合同分责。保English/objective/reference、synthetic训练/主标签、3212/11human agreement非独立holdout真值、C修正独立性、1M/EuroBERT210M/1ep/8MI250x/20GPUh与Nemotron全费、generated-token FLOP非总费。未核实现/复现。

对有参考答案的客观文本任务，还可以不先强迫输出符合固定抽取格式，而将question、candidate与reference共同交给受训的bidirectional encoder，直接提出正确/错误判定。这是scorer的替代分支，不改变真实消费者的schema：评估可理解一份格式不合规的答案，生产接口仍可拒收。先用可靠规则抽取、失败时才走encoder的hybrid人口，也与每题都作语义判定不同；前者省调用却保留成功抽取后的matching误差，不能用回收的accuracy消掉contract failure。

[BERT-as-a-Judge的受限对照](https://arxiv.org/html/2604.09497v1)支持English、客观且有reference的QA分支；训练triplets来自synthetic judge，主表accuracy亦对synthetic标签，有限human一致率不使encoder成为真值。由agreement修正human accuracy还依赖错误独立性，不能直接迁移到开放生成、多语或多模态。标签制作、训练、完整input encoding、规则/fallback与独立人审全计费，按generated-token估的FLOPs不认证端到端倍率；格式、reference资格或人口漂移时，重核scorer/holdout或保留任务规则、人工判定与Unknown，不让更高语义分数替实际contract、policy或outcome验收。

Books整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，source-family `SF-2026-ARXIV-2604-09497` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism](https://arxiv.org/html/2604.09544v1)

精确v1，2+2+2=6；必要源范围及配置：Apr14补Apr13，exact-v1§2–5/A/C/I1/J，2+2+2=6安全深入；仅signed harmful proposal−absolute benign preservation及生成/拒答/解释/检测协议分责。保prefix†条件、Qwen解释−18%/检测−11%与Llama detection/core纠缠，412preservation/raw-format与singlegradient代理不授独立子空间、全utility或EM唯一因果；完整runtime/precision未披露不造SLO。未核代码/复现。

改变能力访问还可在固定权重上做受限剪枝诊断，而不只改activation或训练独立module。分别以指定有害输出和良性任务构造校准集，用带符号的weight–gradient代理提出生成支持，再以良性绝对重要性集合排除需保护的坐标，删除差集后分别测生成、拒答、识别与解释。该接口能提出“哪些行为随同一局部参数干预改变”的反证，所选集合仍依赖校准人口与loss，并不是已找到真实独立的harm知识子空间。

[有限剪枝对照](https://arxiv.org/html/2604.09544v1)中，较少有害生成并不等于模型不懂危害或已经安全；有些所谓保留能力须强制response prefix绕过拒答才测得，与无prefix可用性分开。Qwen的解释与检测仍退步，Llama的检测剪枝与核心语言行为纠缠，不能概括所有能力无损或把局部干预独归emergent misalignment的唯一原因。校准样本、梯度/坐标保存、剪枝模型身份及分协议红队/utility回归全付费；模型、标签或能力人口失配时保留原模型与较轻output policy，重核诊断或停止剪枝，不让权重稀疏、拒答率或judge分数撤销外部tool authorization与effect-time gate。

Books整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，source-family `SF-2026-ARXIV-2604-09544` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [SkillMOO: Multi-Objective Optimization of Agent Skills for Software Engineering](https://arxiv.org/html/2604.09297v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§2–5/T1–4，2+1+2=5具体bundle支持域差额深入；仅failuretrace-driven bundle edits/optimizer prompt共同状态、pass-cost archive与parent−.05 guard分责，不授三objective/heldout泛化/净省费。保GLM5/三最大bundle/GPT5.4扩40test/pop1/5gen/10run及search2.2676/1.8611/1.7641、no-skill成本反侧与编辑非唯一因果；

搜索对象也可从一份prompt变成有依赖的skill bundle：任务solver先产生失败trace和pass/cost，另一个消费者提出删除、替换、重排或重写的child，并更新下一轮使用的optimizer提示。每个child仍需重新执行原任务；可按pass与调用cost保存非支配archive，再以parent-relative质量guard拒绝明显回退。这分别拥有候选生成、局部继承约束和最终operating-point选择；relative guard不是固定绝对发布门，optimizer提示也不得在同一反馈上自行提高verifier权限。

[SkillMOO的有限三任务对照](https://arxiv.org/html/2604.09297v1)支持这一bundle-search分支，runtime只是末级tie-break，不是另一个独立优化目标。最大原bundle、单模型、population1/五代及同扩展test反馈不证明held-out任务泛化；删除/替换频率只是观察，不能独归某类编辑因果。原bundle与空skill在不同质量/费用点仍可合理，共同计入全部solver、optimizer、test扩展与搜索花费，不能用HV相对小分母提升替净收益或break-even。新任务、verifier或依赖身份变化、质量退步或搜索摊销不成立时，保留已核bundle/人工改写与独立holdout，不从Pareto archive批准部署。

Books整合：AGENT-PROMPT [Ch74](../../../../books/part-07-agent/74-prompt.md)，source-family `SF-2026-ARXIV-2604-09297` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [SCoRe: Clean Image Generation from Diffusion Models Trained on Noisy Images](https://arxiv.org/html/2604.09436v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1III-A–D/Eq4–8/IV-A–B/T1–2/V，2+1+2=5具体再生接口gap深入；只原生成→lowpass→SDEdit及cutoff/再加噪时钟分责，不采unknown-noise盲recipe/逐图clean真值。保10%clean/90%noise、CIFAR50k800kb128/FID50k、SIDD8160/520kb64，f.05 SIDD29和CIFARMix f.4 45.7反侧；完整runtime/hardware未披露、第二条去噪链付费。未核实现/复现。

频谱还可以只控制一次生成后的再生，而不重新训练noise schedule：先从原模型完成采样，低通掉候选高频污染，再以受限再加噪时刻启动第二段SDEdit，让原denoiser重新提出细节。Cutoff与第二段时钟共同定义保留—再生取舍，可由径向平均power的signal/noise crossover提出对应；频带是统计代理，不意味着高频全是噪声或低频就是正确语义，也不恢复这张图的真实clean endpoint。

[SCoRe的有限噪声混合对照](https://arxiv.org/html/2604.09436v1)仅支持该受测再生分支：P0被写为clean power而前段又使用training-mixture统计，如何仅凭未知噪声校准未闭，不发布盲用recipe。Cutoff换值会退步，部分CIFAR混合噪声配置输给post-denoiser/NR-GAN；分布FID更好亦不认证逐图去噪真值。原训练、频谱统计、原完整生成、lowpass与第二段去噪全计费，免新增训练不等免时延，hardware/总runtime未披露。噪声不按频带分离、纹理损失或费用不合算时，保留原采样、可靠post-denoiser/数据清理与独立质量核验，不从频谱crossover签发语义保持。

Books整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，source-family `SF-2026-ARXIV-2604-09436` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Dynamic Ranked List Truncation for Reranking Pipelines via LLM-generated Reference-Documents](https://arxiv.org/html/2604.09492v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§3/3.1–3.2/4.3–4.5/T2–4/F5，2+1+2=5具体在线参照预算gap深入；仅generated τ2 reference与Dyn/Avg、listwise共pivot window/stride分责。不采relevance真值/普适parallel排名或Eq> <未闭完整recipe；保200–512token/UMBRELAproxy/BM25早截反退/firstretriever依赖/F5四seed非全表、SU含generation但hardware/precision/concurrency/SLO未披露及全部费。未核实现/复现。

重排预算也可以由query-specific参照提出，而不固定每次取前N篇：先生成一份指定中等相关等级的reference文档，用同一retriever给它和真实候选评分，仅把参照以上的候选送入pointwise/pairwise重排。此时参照控制工作集，不是来自corpus的新证据；生成本身及另一个judge对参照等级的有限验证都只是代理，不能认证所有被跳过的文档都无用。若使用独立calibration人口的平均参照阈值，则与当前query的动态参照分别保存，不把两者称同一个控制合同。

Listwise路径另可不先截断全部候选，而把同一参照加入各非重叠window，按相对次序分组后再作一次末窗口重排；另一分支按每窗高于参照的数量改变stride。这用共享参照减轻顺序overlap，却不证明跨窗次序正确或relevance是真值。[Generated Pivot的有限对照](https://arxiv.org/html/2604.09492v1)有BM25动态早截质量损失、非重叠window并非处处胜，预算依赖第一阶段召回与生成参照质量。生成/判断参照、全部window与末轮调用均计费，受测SU含生成时间却不授生产SLO，equal分数与尾部处理未闭不发布唯一recipe。漏证风险、参照漂移或净收益不合算时，扩大候选/overlap或保留原固定深度、原reranker与独立support核验，不以较少IPQ批准答案。

Books整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，source-family `SF-2026-ARXIV-2604-09492` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning](https://arxiv.org/html/2604.09529v1)

精确v1，2+2+2=6；必要源范围及配置：Apr14补Apr13，exact-v1§3–5/A/C/E1，2+2+2=6具体代理监督/落点差额深入；仅80%mask KL/entropy→batch-relative pseudo target、negative visual-token重权，不采perception真值/negative=wrong/联合correct probability。保1500Gemini caption AUROC.746/SRCC.496、13bench/10binECE、12k15ep/BF16/8rollout/H200240/450/1900GPUh、8B+15/140s及4B+12/100s额外步费，5seed仅inference；

置信监督缺少视觉标签时，还可把视觉描述与后续推理分成不同输出段，用原图与高比例遮罩图的logit变化、以及描述token的entropy构造受限伪目标，再经batch-relative标准化映射给视觉confidence。答案正确性仍由原verifier持有；两份自报confidence的harmonic组合只是训练读出，不是感知/推理联合正确概率。遮罩敏感性说明分布改变，不认证原描述已grounded，batch-relative目标也不能跨人口当绝对perception真值。

信用落点另可仅在视觉描述段、且组内advantage为负时，按该token伪certainty调节原惩罚；negative advantage是相对综合reward较差，不一定答案wrong，更不授错误原因真值。[VL-Calibration的受限训练](https://arxiv.org/html/2604.09529v1)将双confidence、伪监督与重权共同改变，有限caption judge相关性和ECE不能证明每一模块独立因果或safe release。遮罩第二forward、完整rollout、confidence tokens与训练/校准全付费，局部额外step开销不等总费用；entropy/KL单项还会产生不同失稳。代理、parser、人口或质量回归失配时，保留普通outcome advantage、可信视觉标签与独立外置校准器，不由自报置信替答案、policy或effect验收。

Books整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，source-family `SF-2026-ARXIV-2604-09529` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Tango: Taming Visual Signals for Efficient Video Large Language Models](https://arxiv.org/html/2604.09547v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§4–5/必要A-B，2+1+2=5具体表示gap深入；仅expanded topK/每cluster maxattention选择、merge-distance ST-RoPE分责，不采单调距离/entity真值/无损。保A800/三models/32–64–32frames/60-40预算/α1.5/K7、crowdabstract失败/OCRproxy偏置、Other含projector/pooling/pruning与无重复CI披露；

输入token选择与合并还可承担不同的支持约束：固定Top-K容易把预算集中在同一区域，一条受限分支先扩展高attention候选池，再按feature聚类，每类保留一个高分代表；另一份预算才用于相似token的average merge。视频可先将持续相似的位置聚成时间段，再在merge的距离中加入时间/空间坐标旋转的局部性prior。选择代表、合并表示与恢复位置是不同接口，attention/cluster不认证对象身份或语义完整。

坐标旋转在该metric中保持norm，不推出距离随时间单调衰减，也不使average pooling无损。[Tango的有限视频对照](https://arxiv.org/html/2604.09547v1)只支持所测三模型/采样帧与预算分配，crowd和抽象场景仍会失败，attention代理亦可能偏向OCR/text。Global query、sink筛除、分段/聚类、pooling、projector和最终大模型全计费；含Other处理的Video-MME墙钟不能扩成任意服务SLO。候选尾部证据、局部性、质量或净费用失配时，增加保留量，回退原dense/固定选择或有序pooler，并独立验任务支持，不由token数下降签发所有模态保真。

Books整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，source-family `SF-2026-ARXIV-2604-09547` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Litmus (Re)Agent: A Benchmark and Agentic System for Predictive Evaluation of Multilingual Models](https://arxiv.org/html/2604.08970v1)

精确v1，2+2+2=6；必要源范围及配置：Apr14补Apr13，exact-v1§3–5/7及必要B/C/D/H4，2+2+2=6具体evidence/gold人口差额深入；仅reduced readablecorpus vscombinedgold与5缺证scenario。不采family=checkpoint/跨任务尺度/全部DAG因果，保1500/6×5×50、MAE10.3vs12.7而QnA21.6%、code30.6→retry54.6、agent temp1/direct .7、lang2vec代理/人审plausibility非精度与总费未披露。未核实现/复现。

对尚无目标语言或模型直接测量的能力预测，evaluation还须把“预测时能读的证据”与“评价时持有的gold”分开。可从较完整的paper corpus建立目标，再删去一部分论文形成只读evidence corpus，分别测同language/model都有证据、缺model、目标语言缺证而有相近/远语言证据以及两者都缺的条件。这样能检查系统在缺证时是否把transfer猜测当直接观察，而不让检索到几篇近似研究就自称已经测过目标模型。

[Litmus的受限预测评价](https://arxiv.org/html/2604.08970v1)仍以model family而非精确checkpoint定义“同model”，gold跨paper的配置与标注噪声也未消失；0–100缩放须限compatible metric，不授跨任务统一量尺。1500题的numeric预测误差、comparative准确率与code执行是不同对象，扩KB、feature libraries及prompt共同改变不能独归DAG或某模块因果。Corpus/gold核验、语言距离代理、工具/重试与判分全部计费，未披露总API/latency不外推部署收益；证据不足、family身份或metric失配时，应保留区间/Unknown、直接测量或独立专家核验，不由流畅解释或human plausibility评分批准真实能力。

Books整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，source-family `SF-2026-ARXIV-2604-08970` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [EGLOCE: Training-Free Energy-Guided Latent Optimization for Concept Erasure](https://arxiv.org/html/2604.09405v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§4/5/6与必要B/D，2+1+2=5安全反证深入；仅decoded-estimate dualenergy→noisy latent的soft suppression/retention分责，不采safe support/硬擦除/完整Alg1同步recipe。保SD1.4/50step/CFG7.5/K3与scheduler改动、ESD P4D.583→.589/MMA.406→.417反退、CLIP/style盲区与classifier不认非真实删除、N×K额外链及hardware/runtime/seed未披露。

采样中的suppression也可以只优化当前noisy latent，而不改条件K/V或持久weights。先从当前去噪估计解码一份clean-image proposal，用image-text代理同时提出远离目标概念的repulsion与靠近原prompt的retention，再将组合梯度回到latent；每个选定denoising step内可做有限多次更新。两项energy分别拥有抑制目标与保持条件的软取舍，不构成安全support、硬删除或retain全能力保证；解码提案和CLIP相似性也不取得真实概念存在权。

[EGLOCE的有限生成对照](https://arxiv.org/html/2604.09405v1)仍有攻击切片反退，scheduler替换也改变比较条件；更强更新可因画面失真让classifier不再识别目标，或降低代理分数但人眼几乎不变。因此要把代理抑制、实际可见内容与retain质量分开，不由较低ASR自签safe release。完整recipe的latent/噪声更新同步未闭，只采用目标/执行接口；额外decode/encoder、gradient与每步内循环都付费，training-free不等低时延。目标/observer、画质或净费用失配时，保留原模型与output policy、独立人审或更简单局部编辑，不让energy优化批准跨channel遗忘或生产放行。

Books整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，source-family `SF-2026-ARXIV-2604-09405` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [AssemLM: Spatial Reasoning Multimodal Large Language Models for Robotic Assembly](https://arxiv.org/html/2604.08983v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1III-B/IV-A–C及必要A1/C1/C3/C5，2+1+2=5具体几何语言接口gap深入；仅fixed/moving branch correlation+pose-context投影、9D/201bins9tokens与warmup→CE分责，不采Eq3或全LM exactSE3/泛化安全。保130k9:1组合均入train/test、IKEA3cat/BenchDesk有限unseen、4A100/H10080/12ep/b4/temp1、真实330ep/4task各30seeds/预定义grasp/50.8%与blocks9/30plug13/30反侧，Flower几何口径不照recipe；

几何关系也可以先在点云encoder里形成，再送入语言消费者，而不把全部坐标序列化为文本。对fixed与moving两对象，分别保留形状与位姿特征，以fixed的形状分支和moving的位姿分支构造相关表示，再加入fixed位姿context并投影到LLM token embedding空间；输出端则把translation与连续rotation表示规范化、离散成固定数量的pose tokens。Input几何、投影与output bin/坐标恢复共同定义接口，定长token只减少表示歧义，不保证投影后LLM具有exact SE(3)等变性或姿态真值。

[AssemLM的受限对照](https://arxiv.org/html/2604.08983v1)先用geometry warm-up再只对pose span计CE，几何底座与语言适配分别付费；encoder相关式对translation的完整条件未给，不照录全模型等变recipe。主train/test的category-source组合都出现，IKEA有限新source/类别与真实asset追加长适配也不能合成任意零样本控制；serialized point文本对learned encoder更不是纯LLM架构因果。Pose token、归一尺度、点采样、投影/训练及真实重建/控制回归全计费，局部pose或Chamfer成功不授碰撞/闭环安全。坐标/量化、对象匹配或质量失配时，保留原点云、专用几何匹配与连续pose读出，让第26章的controller和真实反馈另行验收，不由语言解码批准装配动作。

Books整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，source-family `SF-2026-ARXIV-2604-08983` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Modality-Aware Zero-Shot Pruning and Sparse Attention for Efficient Multimodal Edge Inference](https://arxiv.org/html/2604.08971v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§4.1–4.6/5/6.3–6.4/7，2+1+2=5具体结构产物gap深入；仅mask-conditioned observer/saliency→offline固定结构与consumer支持域，不采动态能耗controller/任意checkpoint免训练/exactSparseAttend。保task gates_apply=False、GQA mapping需合法后端/pairedFFN、L40训练三时序负载、checkpoint6.07→4.36非RAM/GPU24.50→24.32 vsPixel256.28→157.43、gate9.10/4.96/4.97%与全部费用，precision/batch/T/seed/总费/SLO有限披露不外推。未核代码/复现。

当输入条件改变的是可用modality，部署分支还可先选择结构，再为选定结构形成产物，而不把availability当同shape参数热换。先让backbone在缺模态curriculum下训练，另以activation–gradient saliency监督只读availability mask的observer；task路径本身不经过该gate。离线固定platform mask后，observer提出head/channel重要性，再按目标比例筛结构，成对裁剪投影与FFN并核后端可表示性。这用训练支持与额外observer换有条件的subnetwork，不是对任意checkpoint免训练或逐请求的真实能耗controller。

[SentryFuse的受限多模态时序对照](https://arxiv.org/html/2604.08971v1)支持该materialization分支；head到KV-group映射、保留单位、固定mask与模型revision应随产物保存，proxy排序不认证每个未见mask或完整dense质量。Sparse attention又是另一变化，未被显式算的query使用context替代，不能与结构剪枝合成exact保证。Checkpoint大小不是peak RAM，GPU时延几乎不变却在Pixel更明显，不能由GFLOPs比例推出各硬件同幅收益。Curriculum、saliency backward、observer训练/求值、结构重建、编译与质量回归全付费；缺模态support、合法shape或总质量—成本失配时，保留dense/静态已核分支、重训或重新profile，而不让mask与gate自签免验部署。

Books整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，source-family `SF-2026-ARXIV-2604-08971` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Task-Aware LLM Routing with Multi-Level Task-Profile-Guided Data Synthesis for Cold-Start Scenarios](https://arxiv.org/html/2604.09377v1)

精确v1，2+2+2=6；必要源范围及配置：Apr14补Apr13，exact-v1§3–4及必要synthesis-cost/假设反侧，2+2+2=6具体cold-start支持域gap深入；仅taxonomy synth→allcandidate quality/cost标签与type-mixture预测分责，不采Eq6→7/9实际ELBO或trueposterior/校准。保4×2000/7:1:2、17880/15200 QA与不同judge协议、domain .5402优于difficulty .5274、LR五runs非全主表、造数14.34/10.03非总费及hardware/runtime/SLO ND。未核实现/复现。

缺少本域带标签请求时，路由训练还可先从domain描述构造受限task taxonomy，按profile生成QA、去重，再实际调用冻结的全部候选模型取得quality与token-cost标签。Query先提出task-type分布，各model的type-conditioned预测再按该分布混合，最后按声明的quality/cost权重排序；这里训练的支持域来自synthetic generator与taxonomy，不是对真实请求已经观测到的能力，也不能让高utility越过硬资格。

[TRouter的有限冷启动对照](https://arxiv.org/html/2604.09377v1)只支持该经验预测接口，类型单标签不是真实posterior，task/model条件独立也须按人口检验。正文reverse-KL与one-hot CE方向、marginal-mean MSE与期望conditional likelihood未闭，不采用“实际训练已实现同ELBO/校准保证”；更细taxonomy也非处处更优。合成QA、全部候选回答/判分、训练与真实holdout回归全计费，造数报价不是总预算，LR五runs不能推广到主表。Domain、candidate价格/身份或质量代理漂移时，补真实calibration、退回静态/已核router或保留Unknown，不从synthetic低费推出通用路由收益、latency或安全。

Books整合：PLATFORM-GATEWAY [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md)，source-family `SF-2026-ARXIV-2604-09377` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Integrated Electro-Optic Attention Nonlinearities for Transformers](https://arxiv.org/html/2604.09512v1)

精确v1，2+2+2=6；必要源范围及配置：Apr14补Apr13，exact-v1II–IV与必要S2/S4–6，2+2+2=6具体hybridconsumer/物理费用资格深入；仅clipped MZM transfer/integration与trainedconsumer、格式×noise分责，不采exactSoftmax/全芯片或运行SLO。保10GBaud实测σ.098/.088高于GPT失效>.01、4bit ViT σ.02退步、124M/bf16/1024/b512/5k2.6Bt vsquant1.5k/noise2.5k、不融合不同budget与S2 noise式未闭；410/205ns是pipeline估算含信号链非外部GPU总费。未核实现/实芯全模型复现。

专用单元也可以只接管attention的非线性，而不替代矩阵乘或完整模型执行。一个hybrid分支用Mach–Zehnder调制器的上升响应近似exponential，先以一段光强序列积分形成分母，再让第二段通过下降响应近似reciprocal；elementwise sigmoid分支则只需一段饱和响应。DAC/ADC格式、clipping范围、bias、积分与noise共同定义这份近似算子，非负性和norm相近不等exact Softmax或unit-sum，consumer需按对应transfer重新训练/校准。

[Electro-Optic单元的必要评价](https://arxiv.org/html/2604.09512v1)将器件波形测量与模型仿真分开：10GBaud/5bit序列不是实芯完整Transformer，受训GPT-2的lowbit结果也不能与不同步数noise配置合并为同预算。尤其受测高baud噪声高于模型可容忍区间，不能由快速波形推出可用高速度模型；noise公式口径未闭，只保校准/支持域，不发布唯一recipe。两段或一段编码、laser/RF/thermal/TIA/converters、模型重训与跨设备搬运全计费，410/205ns链估算不是完整GPU路径或服务SLO。格式、动态范围、noise或质量失配时，保留数字Softmax/sigmoid、已核fused kernel或重新校准/降低速度，不从单非线性估算签发全模型降本。

Books整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，source-family `SF-2026-ARXIV-2604-09512` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [CT-1: Vision-Language-Camera Models Transfer Spatial Reasoning Knowledge to Camera-Controllable Video Generation](https://arxiv.org/html/2604.09201v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§3–4及必要6.1/6.3/6.4，2+1+2=5具体camera-producer/consumer差额深入；只采用语义condition→Euclidean轨迹分布/多尺度target监督→video接口，不采SE3/Lipschitz或CAM完整recipe。保CT200K伪pose、CameraBench100双expert观看视频与重绘混杂、VBench dynamic反退、32GPU型号/precision ND、224²b512lr1e-5、单GPU22.81+429.02s/28.91+39.48GB及完整总费/SLO边界。

给定运动条件的生成器还可以由独立producer供值，而不是要求用户手写每个camera pose。一个分支将图像和语言汇聚为camera-context表示，条件DiT在Euclidean pose序列上提出可能的轨迹，再将转换后的camera条件交给视频消费者；训练以Haar多尺度的预测—目标差赋不同权重，倾向保留整体运动、减少局部抖动。这是轨迹分布与渲染的接口分责，不是辨识唯一SE(3)运动、观测真值或可执行动作；CAM供值与learnable embedding的精确连接未闭，不发布完整recipe。

[CT-1的受限对照](https://arxiv.org/html/2604.09201v1)以伪pose/VLM标注和人工caption建立训练支持，以两专家共同接受generated video作100例评价，不能用它独立认证轨迹物理正确；81.6相对64.9是16.7个百分点，而动态程度仍有反退。轨迹训练、频域损失、全部pose生成和后续视频采样共同计费，单GPU13step轨迹22.81s另有49frame视频429.02s，不是实时控制或免开销插件。标注、camera转换、语义或运行预算失配时，保留给定已校准轨迹、原视频生成器或显式simulator；动作权限和物理安全仍由真实controller验收。

Books整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，source-family `SF-2026-ARXIV-2604-09201` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Automated Instruction Revision (AIR): A Structured Comparison of Task Adaptation Strategies for LLM Systems](https://arxiv.org/html/2604.09418v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§3.1–3.3/§4–6，2+1+2=5具体labelled-contrast→rule修订支持域差额深入；K5 inputcluster/output分布balance、THEN/IF/exception与mistake/anchor分责，不采ruleID因果/anchor语义certificate或未测online更新。保test64/30/78/60/60异metric、dev8/5/12/60/60、GPT4.1mini/GPT5reflection/QA5.1judge、AIR95.31<GEPA96.88/QA42.08<81.67/IE35.90<36.54、PUPA8steps5无改善b3、完整tokens与美元/runtime/hardware/seedsCI ND。

规则集也可从带标签的局部对照学习，而不是仅汇总人工追加的约束。先按input语义分cluster，再用output分布相对全局的差异调整局部样本，避免每个cluster只有一种结果；A/B对照提出IF/THEN规则，按相近THEN合并IF并保留例外，后续错误样本与规则关联的anchor共同约束最小改写。这里cluster定义候选的训练支持，规则ID只是模型报告的参与线索，不是因果归因；anchor通过也不认证所有旧语义保持，最终部署仍需独立regression。

[AIR的五任务对照](https://arxiv.org/html/2604.09418v1)支持有限显式规则适配，但不授通用赢家：source-specific QA中42.08不优于原prompt、低于KNN81.67，结构化提取亦有反退。聚类、全部base/reflection调用、合并/修订、dev选择与独立test共同计费，各角色token账不能代替总美元或latency；持续增量更新尚未实验。噪标、冲突合并、anchor覆盖或质量回归时，保留人工短prompt、原规则/例子检索或参数适配，不让可读规则和自报ID自行批准删除guard、安全或上线。

Books整合：AGENT-PROMPT [Ch74](../../../../books/part-07-agent/74-prompt.md)，source-family `SF-2026-ARXIV-2604-09418` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [TinyNeRV: Compact Neural Video Representations via Capacity Scaling, Distillation, and Low-Precision Inference](https://arxiv.org/html/2604.09220v1)

精确v1，2+1+2=5；必要源范围及配置：Apr14补Apr13，exact-v1§3.2–3.4/4.1–4.7必要表，2+1+2=5具体per-video参数容量×输出teacher适配×量化consumer差额深入；Gaussian low/high/focal不是latent wavelet删带，Eq7端点/focal完整recipe不采。保四video各自300ep拟合、teacher额外全费、BBB INT6PTQ27.84→26.92/INT4QAT27.12→KD27.66、权重量化后反量化floatconv非硬INT、L4b1FP FPS不迁移低bit、无训练全wall/energy/SLO保证。

视频表示还可以把容量写进逐video拟合的decoder权重，而不是共享latent词表。固定depth、stride与输出分辨率、只缩width时，teacher的RGB重建可分成Gaussian low-pass与高频残差，分别约束student，并按高频teacher–student差异加权关注难恢复位置；随后PTQ或QAT另选择权重格式。这适配的是小decoder的训练目标，不改变推理骨架，也不证明高频误差就是语义损失；teacher与量化consumer必须分别携带身份。

[TinyNeRV的局部操作点](https://arxiv.org/html/2604.09220v1)限四个各自拟合的720×1280视频，不是未见视频encoder泛化。INT6 PTQ存在27.84→26.92dB退步，INT4 QAT再加KD的27.12→27.66只支持该配置；低bit评估先dequant再float卷积，L4 batch1浮点FPS不能当INT4硬kernel速度。Teacher拟合、额外forward、distill/QAT和实际重建全计费，GFLOP/权重体积也不是总费用。细节或算子支持失配时保留较宽浮点decoder/原训练目标或已有codec，真实低bit执行仍须第49章验证，不从模拟bit-width批准端到端吞吐或无损压缩。

Books整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，source-family `SF-2026-ARXIV-2604-09220` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Event-Driven Temporal Graph Networks for Asynchronous Multi-Agent Cyber Defense in NetForge_RL](https://arxiv.org/html/2604.09523v1)

精确v1，2+2+2=6；必要源范围及配置：Apr14补Apr13，exact-v1Event-Driven Temporal Graph Networks题名，§3–6及必要8/B，2+2+2=6具体event-clock→hidden/credit分责差额深入；不采用currentv3 JAX suite、fullsim2real、安全或独立模块因果。保Δt/50clip、duration/preemption/tie/silentdrop是engine定义、local TFIDF/日志actor vsnoisefreecritic、RK4四NFE、双方共同换算法、NoBeta56656/NoGAT56565接近57135、mock/Docker不同人口、10seeds median末20%无CI、10vs17.2policySPS/A10040或80/32CPU2.5M8h与全费/SLO ND。

环境真正按不规则事件推进时，还要把“这次等待多久”交给学习消费者，而不只保存认知轮数。一个受限policy分支在观测到达时编码当前有效图，在两次到达之间按elapsed interval推进hidden dynamics，再用新观测作gated update；训练以interval相关discount形成TD/advantage，不把不同duration的transition都当等长step。Duration、preemption、同刻tie和并发上限仍由environment engine规定，graph mask只是该engine的候选支持，不是现实动作授权；local actor与privileged central critic的观察责任也要分开。

[NetForge_RL exact-v1的必要对照](https://arxiv.org/html/2604.09523v1)只支持event-clock到state/credit的接口，固定单步RK4四NFE和额外graph读取都付费。红蓝双方共同换算法、自建reward和mock/Docker人口不同，不授架构唯一因果、消除sim-to-real或真实安全；NoBeta/NoGAT回报接近full也限制单模块话术。10seed末段median不是已披露CI，policy10SPS低于baseline17.2，mock10k环境SPS不代替含policy总速率。时钟、observability、动力学或engine规则失配时，保留显式离散controller、更完整状态/真实回归与同步step基线，不把学习到的事件状态当真实世界authority。

Books整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，source-family `SF-2026-ARXIV-2604-09523` 的实际两段及本人末注已由非作者独立POST通过；这是本轮新写，不把旧25处计入。

### [Artifacts as Memory Beyond the Agent Boundary](https://arxiv.org/html/2604.08756v1)

2+1+2=5，深入完成。确定性environment artifact只有在history已包含其值或reference时，才支持删除其可推出的冗余观察；不是任意memory外置或动作/value充分性。精确v1§2–5、AppA必要Theorem1证明与B1/B2：容量是可学习参数，replay固定排除；13×13 grid/30seed的QL输入crop随capacity变，DQN dynamic path失败，linear400 p=.11不显著，每pairα=.05未披露multiplicity校正。不能把路径收益唯一归因主动外存或把参数差当runtime bytes。只保条件冗余与有限RL观察；当前不改变Agent durable读/删接口，Books0且非已有覆盖。新的动作/value支持或实际外存读域才定点重开。

### [Ge²mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer](https://arxiv.org/html/2604.08894v1)

2+1+2=5，标准完成。精确v1§4.1–4.3/5.1–5.3的nonuniform ExpGIF只在训练的量化activation映射/maxspike条件下lossless；group-window/global-stride/channel混合、KV时间平均与末stage vanilla各有限支持。Tables混architecture/参数/288输入/预训负载，energy为SOP估算而非实芯耗能。保新增coding/布局观察，但本拟命题未分离code/group/hybrid layout取得新的通用质量—总费操作点或consumer接口；不是因SNN、小ViT、成熟组合或无芯片单独排除，不称NC。Books0；若有绑定consumer与可比布局的新命题再重开。

### [Discrete Token Modeling for Multi-Stem Music Source Separation with Language Models](https://arxiv.org/html/2604.09371v1)

2+1+2=5，标准完成。精确v1§2.1–2.5/3.1–3.3/4.1–4.3/5：frozen HCodec12.5Hz的acoustic/semantic各16RVQ1024；continuous mixture prefix与跨轨KV支持固定vocals→drums→bass→other，非任意prompt轨顺序。23kh BSRoFormer伪gold、8A10080/35ep/4s mono/b24与50专业测试；baseline/reference均codec往返，不证原waveform保真。ViSQOL3.55不胜3.62/3.71、drums3.44低于3.77–3.88，NISQA为speech proxy，无sample-alignment/SI-SNR；parallel3.49vs3.55无CI。完整codec/生成/训练费用和runtime/precision/SLO ND保留。具体贡献为fixed-stem条件分解/评价错位观察；未新增拟采用的顺序、分离约束或质量—总费用选择，不改变Ch24实际AR依赖/teacher-forcing/codec验收解释，不假称具体multi-stem NC。Books0；新consumer/顺序/分离约束或可比总费才重开。

### [AlphaLab: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs](https://arxiv.org/html/2604.08590v1)

2+1+2=5，深入完成。精确v1§2/3.1–3.2/3.4–3.5/5及必要G silent-corruption/费用段，仅kernel/pretraining与campaign反馈，不引入科学/交通金融应用。拟采用debrief→持久playbook供后续actor/strategist消费以及独立verifier/采用门：Ch80实际episode evidence→actor prompt/state/reset/budget/revision/rollback和lesson/held-out/promotion两组论证已经承载，并非主题相似；不说Alpha等同learned meta-policy或全部queue/实证都NC。五次fullPhase3 .994±.025与no-playbook .9941/单次full .9697不授独立稳健因果，自建Critic/Tester/Imax不是oracle，G有metric漏错/leaderboard污染且无sandbox。single-shot<$1 vsfull$150–200+GPU/greedy$50不同总费，50experiment/20min<100M speedrun保有限范围。Books无新写；新受控调度/控制约束才重开。

### [Hierarchical Kernel Transformer: Multi-Scale Attention with an Information-Theoretic Approximation Analysis](https://arxiv.org/html/2604.08829v1)

2+1+2=5，争议。精确v1§3.2–3.6/4/5/6：causal downsampling与score mask不能修Eq7全序列mean→MLP→α(X)的future读取路径；50trial/T32梯度诊断不是任意token严格因果证明。PSD仅对满足M_s PSD的对称surrogate，实际负eigenvalues；rank2d只linear-term近似、H4/λ1衰减不授实际mixture普遍界。synthetic/IMDB/sequential CIFAR、A100/B16/d128/H4/L3/3seed保有限noncausal分类观察，中心strict/εcausal采用隔离。T1024 peak1729/552=3.13×与正文约2×不符，train30.3/20.8=1.46×、infer10.2/6.1=1.67×；4/3只attention score不是总费。Books0；需causal gate定义/实现或作者收窄与物理成本解释才定点重开。

### [Multi-Agent Decision-Focused Learning via Value-Aware Sequential Communication.](https://arxiv.org/html/2604.08944v1)

2+2+2=6，争议。精确v1§4/Eq9–10/Alg1–2/§5及必要C1/C3：TV/Pinsker上界不能推出action偏差下界，reward Lipschitz不能推出正value差下界；常数reward或忽略message即反例，两个独立上界也未证明DFL误差更小。实际inner Lmodel+λLaware与IFT只Lmodel Hessian不一致，强凸/可逆不授神经critic；全部obs消息先生成再priority读取predecessor subset，不是共享已commit actions或已证Stackelberg。保value-aware代理和10seed SMAC有限观察，不能用Only平滑中心necessity/执行保证冲突。Books0；修正定理/支持假设、action消费次序与真实inner对应才重开，不遍其他附件。

### [Semantic Rate-Distortion for Bounded Multi-Agent Communication: Capacity-Derived Semantic Spaces and the Communication Cost of Alignment](https://arxiv.org/html/2604.09521v1)

2+2+3=7，争议。精确v1Defs2/3/13、Prop11/Thm18/Cor26、§8/10与必要F/H/J/M：Thm18的cM下界与H仅pconfuse*cM不等，positive mass不授uniform subclass confusion，代表intent可为中间点需重界；λ=.5时proxy W+.5mismatch不能作full W+1mismatch+ΔV的upper。two-block-old quotient参数与当前iid独立不证明当前intent reconstruction恰达WZ，bounded-FSC即时achievability还缺decoder存储/延迟对象。保common-history/coarsening/intent测量/oneway iid/shrinkingε框架与有限FSC/sample proxy，但中心最低rate/phase guarantee隔离。Books0；factor/support/proxy与当前block操作存储延迟修复才重开。

### [Risk-seeking conservative policy iteration with agent-state based policies for Dec-POMDPs with guaranteed convergence](https://arxiv.org/html/2604.09495v1)

2+2+2=6，争议。精确v1§3.2/Props3.1–3.3/Alg1、4.1/4.2/5及必要F/H/D：joint(action,nextagentstate)有限controller、fixed-other/time-coordinate known fullmodel occupancy/Q与risk/CPI确有潜力。Prop3.3任意α包含α(k)=0恒等，nongreedy初策不进入G；H从J收敛跳局部策略最优，未给非零/充分进展。fixedλ风险J的Props也不授Alg退火λ→0的risk-neutral全程单调/收敛；poly按显式joint/product state模型，不等随agents数多项式。四MASPlan/两agent，α/λ五seed调参再五initialization报best，runtime mean/SD不同于主best或CI/等算预算，部分任务reactive足够、Mars Z4未测、baseline可更快。中心采用争议Books0；修progress、退火objective对应及model-size口径才重开，不扩proof。

## 5. 缺口与下一步

**本轮补充可执行待办：** 无。来源、证据、Books与独立六部分DAY已处理到安全终态；以下外部保留项不当普通队列，亦不作正面证据或覆盖证明。补窗仅核公开日期、不追精确时刻，不把原晚段或版本身份迁入。


**Apr13补充终态保留项：** 以下不计正面证据/Books/无遗漏，也不把日期门塞入确定候选。

- [AdaCubic09437](https://arxiv.org/html/2604.09437v1)：正文有具名OpenReview pZBQ7J37lk先稿，forum及api2挑战403，无法确认正文首公开日期。需title-bound作者公开首稿或可验证OpenReview首次公开metadata；只重开归属/合并。必要算法Source已读，Alg2 while容差方向与文字相反、SGD PPL/35.16min优于Ada42.4min等反侧有效，但不授日期/精确solver实现。
- [Seed Continuous Adversarial Flow11521](https://arxiv.org/abs/2604.11521v1)：Apr13 CMS目录/Apr12 16Z字段和v1 SubmittedApr13不能证明Apr13首次公开正文，ID属另一公告簇。需官方作者正文/仓库release的Apr13公开绑定记录，按具体family恢复日期和必要命题，不能用推荐日回填。
- [BiasedSwarm08963](https://arxiv.org/html/2604.08963v1)：ICLR2026accepted具名 [OpenReview原稿](https://openreview.net/pdf?id=mo7u21GoQv)与题作者摘要一致，但forum/raw api2实际403 ChallengeRequiredError，没有first-public metadata。需该稿可验证初次公開记录/作者公开首稿；搜索“7monthsago”不作日期。必要Source反侧保留：printed probability/Gini是polarization代理、非真实bias概率；k−1式与例子k口径不一致、depth非单调、topology与history/calls混杂、neutral示例本身人口提示及Gemini身份未闭，不授普遍安全或mitigation。
- [HKT08829](https://arxiv.org/html/2604.08829v1)：重开需全序列gate因果定义/实现或作者收窄与完整物理费用口径，有限gradient不能解除中心future路径。
- [SeqComm08944](https://arxiv.org/html/2604.08944v1)：需修TV/value下界方向、inner/IFT对应与committed-action消费接口，或明确收窄为所测代理，不用更多指标平滑中心保证。
- [SemanticRateDist09521](https://arxiv.org/html/2604.09521v1)：需修factor/uniform-support条件、metric upper与当前block的decoder存储/延迟对象，不授最低rate/phase或即时FSC保证。
- [RS-CPI09495](https://arxiv.org/html/2604.09495v1)：需非零/充分进展步长、fixedλ到actual退火objective的对应证明与显式model-size口径；α0与值收敛不等局部策略最优。
- §2十项机构历史子入口及arXiv逐篇日公告受限：需绑定Apr13的官方historical list/作者artifact或公告，而不是更多当前首页。三checked仅目录slice；Seed日期门新列不静默沿旧已检查。保留范围只恢复对应入口，不重扫组织历年、全月或173/381库存。

**原窗口终态保留项（未迁移）：** 以下不用于正面证据、Books或无遗漏断言。现可用原始入口已审，材料后来到达时定点重开对应项，不顺带重跑全月：

- 来源历史子入口：OpenAI Research、Google Pubs、Meta Research、Qwen artifact、DeepSeek研究/发布记录、Moonshot其他模型研究/artifact、ERNIE repo研究切片、MiMo Blog/artifact、MiniMax Agent Tech/artifact。对应官方入口在§2；缺本窗可验证目录、事件日期和必要原文，现有Blog/release不能代替。可接受官方历史列表、存档HTML或绑定事件日期的官方正文/仓库记录，按来源行恢复，不据空响应宣称零命中。
- arXiv日公告：§3范围是显式联合推断，不是精确公告日志。本次仅在解除下面日期例外时，接受对应家族正式公告邮件/列表或可验证截点前正文公开记录；不要求重读1334篇。
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

本轮补充复核者：supp_apr14_reader，报告补充作者supp_apr14_author。结论：通过（实际六部分DAY，见独核R44；完成态FINAL只认保存后独核记录）。来源有限入口/停止R28、R34及接口修复层实际核；38拟入选必要命题、1具体NC/3Only/4争议与3日期资格按受限范围完成独核；30新写实际正文、完整上下邻及本人末注POST通过，作者仅同步本人注/实读回后释放所有窄锁。

否定侧按来源×主题×具体理由分层：官方core层Cloudflare/OpenAI（接入/GA、不公开新执行状态协议）与Google Vantage（human技能评分而非AI可靠性盲区）2/2本次实际独读；Moonshot CLI1.32.0/PR1843局部预算兼容patch 1项复用本日有效同事件core层，不重复宣称新审；arXiv安全集成层PAEdge09493 1/1完整题摘/必要安全core/评价及VI本次独读，十固定命令同管线没有独立误判/模块控制，不授judge真值。合计4具名EX中3本次实际独读、1有效层复用，不因产品/教育/军事/edge/组合标签硬排；后者可接受身份及命题未变的复用，不冒充全库存抽样。其他旧EX只按本日明确同事件层去重；173/381 inventory中未具名/未逐项题摘的范围未作EX或全量独抽，31/56身份去重数也不是语义审阅数。全部带纠错/安全/设计反证信号的具名新排除PAEdge已实读相关必要层。

机器层：V3结构校验通过，120候选/120唯一arXiv、140本地引用/33路径零missing；82原行/日期评分、原window与连续原§4（26,004字符/41,573 UTF8字节）冻结保持；README/SUP限定cached与unstaged diff-check通过，不称全仓clean。实际六部分DAY由非作者通过，完成态FINAL以保存后独核记录为准，不重Source或30POST。独核时间/范围在[唯一补查记录reader尾区](../_sources/daily-20260414/SUP_SOURCES_20261014.md#r44-实际六部分-day-通过2026-10-14)。以下旧验收只复用未变化的82层：

复核者：apr01、apr02、apr03、apr20_resume；最终日级复核者apr01，报告作者root。
结论：通过

最终六部分、82家族处置与日期范围、七项具体已有覆盖、25项真实正文及相邻衔接已完成相应非作者验收；八中心争议及来源/日期限制安全隔离，不支持正面采用或无遗漏保证。

已执行来源/准入口径检查、全部拟候选必要命题的分批非作者审阅、代表性排除项分层校准及25处真实正文/相邻衔接检查；没有把抽检写成325/1334条全量语义证明。日期82项有限范围及早公开/版本例外见[日期与最后采用复核](../_sources/daily-20260414/V3_APR01_FINAL_GAP_ADOPTION.md)；具体证据复用见[机制校准](../_sources/daily-20260414/V3_INDEPENDENT_MECHANISM_CALIBRATION.md)、[三项反向校准](../_sources/daily-20260414/V3_INDEPENDENT_THREE_CALIBRATION.md)、[第十六批](../_sources/daily-20260414/V3_APR02_BATCH16_INDEPENDENT.md)、[第十七批](../_sources/daily-20260414/V3_APR20_BATCH17_INDEPENDENT.md)、[第十八批及写后](../_sources/daily-20260414/V3_APR01_BATCH18_INDEPENDENT.md)、[最后十项](../_sources/daily-20260414/V3_APR20_FINAL_DISPOSITIONS_INDEPENDENT.md)和[逐项工作记录](../_sources/daily-20260414/v3-reopen-notes.md)所链接的其他独立审阅。

机器结构校验已通过；机器通过不代替语义验收。保护运行前已有staged/unstaged修改，不stage、commit、push。
