# Daily Research — 2025-09-27

**规范：** V3
**窗口：** 2025-09-26T09:00:00+08:00 ～ 2025-09-27T09:00:00+08:00
**窗口说明：** 用户授权仅补已有2025 Daily来源遗漏；原候选日期、评分、窗口与连续旧§4冻结复用，新增只前一完整BJT自然日。
**补充窗口：** 2025-09-26 ～ 2025-09-26
**冻结候选日期：** [补查前原报告](../_sources/daily-20250927/baseline-before-supplement-20261013.md)
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-25T20:36:49+08:00

## 1. 结论

本日42个材料家族均达到对应最低审阅层并完成逐项处置：18实际整合（含旧TEQUILA）、16具体已有覆盖、1仅报告、7项中心强主张争议。主要增量是把验证筛选、训练/部署状态、表示消费、检索粒度与judge读出分别绑定其真实证据人口和完整费用；少步、低参数量、共享前缀或更高proxy分均不自动授予同质净收益、正确性或安全。

四主题查询与相关标题浏览已按实际分页/停止位置有界收束；宽导航不是逐项全文队列，未宣称全球无遗漏。普通研究、owner、待写/POST与在途均无，五个历史来源限制和七项中心争议按§5隔离；Helmholtz R94完整DAY、作者104真实完成保存及Helmholtz R95唯一FINAL已通过，本日闭合，不以单篇POST代日级验收。

历史权限：原三候选的日期、评分、小时窗与连续旧§4及有效Source/POST保留，旧完成标签仅对应当时范围，不验收本轮遗漏修复。具名证据与实际处置见[本轮canonical](../_sources/daily-20250927/REPAIR_20261025.md)。

## 2. 来源覆盖

原有效响应与本轮新响应分别在[本日_sources](../_sources/daily-20250927/)；旧[fetch-log](../_sources/daily-20250927/fetch-log.json)未改，真实URL/UTC执行时间/status/exit/bytes/SHA分别见原`SUP_curl-*`及本轮`REPAIR_*`/`ROOT_*`的同名request JSON。[十四源有限停止包](../_sources/daily-20250927/SUP_SOURCE_20261013.md)与[本轮查询/具名增量](../_sources/daily-20250927/REPAIR_20261025.md)共同界定已查范围；仅metadata跨窗，不加载窗外正文作本日证据。以下不借旧完成声明。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮Research403，RSS200/1287items；BJT Sep26仅AARP原06GMT，同事件完整core关闭有效复用；旧tool-output属于冻结原BJT27事件不搬移 | 已检查 | RSS只是实际订阅切片，不授Research全集/所有修订；当前Function calling不倒填2025兼容性 |
| SRC-ANTHROPIC | 本轮Research真实Flight/RSC 179出现/176唯一slug-title条目/170唯一日期值，Sep26无字段，Feynman§3实际解析通过 | 已检查 | 限当前实际Research目录，不授未收录历史或互联网无事件 |
| SRC-GOOGLE-AI | 本地月Blog/Pub timeout、DeepMind首查TLS失败；本日web月Blog首12/2页Sep30→Sep25→Sep11夹窗停；DeepMind page2真实200/265目录仅Oct30→Sep29→Sep24→Sep18邻接；Pub web首15/11615、Year排序/2025facet680，只有年份 | 受阻 | Blog/DeepMind有限窗口邻接已恢复，不重已验窗外稿；Pub历史日证/未收录事件受限，680/265非研究队列 |
| SRC-META-AI | 首查Research/p5本地timeout；本日web真实global_search p5 2939混合目录，只publication Oct13→Sep24→Sep23→Sep22→Sep15窗口邻接，停元数据 | 受阻 | Person/Blog/publication非全局单调历史全集，无当前Sep26项不授Research全Coverage；需具名原事件或有限历史页 |
| SRC-QWEN | 注册Hugo页及本日page_config200，完整非时间排序60项date/title逐一检查，Sep26无项 | 已检查 | 限实际数组，无具名触发不扫全模型/仓库；不授全部历史发布/修订无遗漏 |
| SRC-DEEPSEEK | 本日home/updates200，updates实际Sep29 V3.2Exp→Sep22 Terminus夹窗后止日期层，未重窗外release | 已检查 | 限官方可见发布目录，不是研究/修订全史 |
| SRC-MOONSHOT | 本日Kimi Blog200，Nov07/06→Sep16/05目录夹窗后停，未见本日项 | 已检查 | 限官方可见Blog切片，无具名触发不全扫GitHub历史 |
| SRC-TENCENT-HUNYUAN | 首查Research200；本日正确publicList POST page1/size100/renderType0，code0/list9/total9，可提取且最早display转BJT2026-02-03，止metadata | 受阻 | 当前全部2026不能恢复2025历史，不称浏览器执行/0论文；需具名2025原稿/有限历史目录 |
| SRC-ZAI | 本日Research p1/p2均200，p2十八dated至2025Dec07/真实没有更多，止目录 | 受阻 | 最早仍晚于Sep26，历史切片缺失；createAt不充first-public，需具名原事件 |
| SRC-BYTEDANCE-SEED | 本日真实paper18/94、blog18/45、next20/has_more；PublishDate转BJT、UpdateTime和pin分开。paper非pinOct22/21→Sep22两项→Sep02/01，blog非pinOct23→Aug21；逐项pin日期无Sep26后止首片 | 已检查 | 旧缺数组已恢复，不请求全年94；只支持两实际第一页/邻接，不授未收录历史无事件或全球无遗漏 |
| SRC-BAIDU-ERNIE | 本日Blog p1/p2均200，p2 Oct16→Sep12→Aug14/Jun30越窗、真实末页1/2/上一页，止日期层 | 已检查 | 限官方当前Blog分页；导航哨兵不算文章，不全扫GitHub |
| SRC-XIAOMI-MIMO | 本日首页8Paper Oct21→Sep19→Jun04夹窗，15Blog；fresh runtime/routes和两个async首页chunk实际恢复，More仅展开同数组无分页请求；routes具名HSS Dec19/安全Dec18,2025及2026日期 | 已检查 | 部分Blog仍undated、未收录历史不授Sep26零事件/全Coverage；两错误非async路径404保留，不读窗外正文 |
| SRC-MINIMAX | 本日EN12/CN13 dated cards，EN最早Oct27/CN至Jan15夹窗后停；Agent/llms200，当前三篇Oct08/Sep22/Sep19均2026，无2025历史分页出口 | 受阻 | 不沿旧“仅一篇”；公司Blog有限范围已处理，Agent2025历史仍需具名原事件/有限历史索引，不研究2026 |
| SRC-ARXIV | 本轮正确submitted发现代理Sep24T18～Sep25T18Z，显式词形/别名及分类/机制Boolean AND时间桶，原请求REPAIR_ATOM_*_P1：Model94/94、Systems53/53、Agents57/57、Multimodal83/83，287出现/211身份，R11实际核有限查询停止。相关标题导航仅十二类同代理首200/470，末20838/Sep25T07:23:52Z；其余270不是已读不相关或Methods队列。旧385/287及36精确AB有效层仅复用，不代新代理覆盖 | 已检查 | 四主题/有界标题停止及实际具名cue经R55/60核；42家族必要/具体处置已闭，未将导航余量变为待审队列；DataCite本轮只具名日期原字段，不是主题检索。合法S+2025规则L+同DOI/arxiv.content/findable registered U按本轮包核，非Submitted公开/catchup或截跨日；不授全学科召回/全球无遗漏 |
| 表外：[OpenAI Developer Community](https://community.openai.com/t/images-and-files-as-function-call-outputs/1360081) | 搜索触发仅该原帖JSON及身份恢复，必要Function calling官方说明，未扫论坛 | 已检查 | 原帖仅支持发布事实，完整2025 schema未取得/未采用 |
| 表外：[Kwai-Klear/CE-GPPO](https://github.com/Kwai-Klear/CE-GPPO) | 具名Sep26作者News与2509.20712v1身份，必要v1及current-v5受影响纠错，Feynman§4–10实际Source/Ch33No Change通过；未扫整个仓库/八月报告 | 已检查 | 原作者研究披露事件非arXiv公告/globalfirst，当前ERC不代CE实现；未核artifact或复现 |
| 表外：[Chimera原作者项目](https://github.com/CHIzhP/Chimera) | 原身份/窄P及Sep26 Upload仅提交、Sep27代码分责复用；本轮同DOI唯一v1 S与L/U联合已R2实际核，arxiv公告整段BJT Sep29，不属补充Sep26 | 已检查 | 不把Upload/代码移日或绕v1采用；原必要Source/Ch66仅准备，非本日正式评分/Books。只在具名更早正文实际公开事件到达时定点恢复，不重原方法 |
| 表外：[Tencent AngelSlim](https://github.com/Tencent/AngelSlim) | 仅具名TEQUILA News25/09/26算法release、实际Paper2509.23809与同owner tequila/TernaryQuant链接；精确v1 HTML必要§2–4/AppendixC，200/exit0/217739bytes原件及请求保存本日；Feynman§26–28日门/Source/5分实际通过 | 已检查 | 只该release家族，不扫全repo；v1是后续稿机制补证，非Sep26同字节paper/current branch实现认证。未核代码运行/复现/生产SLO；具体PRE§29及actual非writerPOST§30已通过，root已接纳并释放锁，当前无Books锁/待办，不把实际整合当实现/复现保证 |
| 补检：[web search](https://www.google.com/) | 本日四主题/arxiv.org域/Sep26字符串及GUI/BRT/Metacognition/G-Cite、OjaKV/Zeppelin、最后StructPrune/SelfJudge/Chimera具名日期有限线索，回原版本/作者出口后停 | 检索受限 | 搜索/第三方笔记只发现不授日期/证据；无命中不证明无事件，不无限全网absence，具体必要日门依§5重开 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Images and files as function call outputs](https://community.openai.com/t/images-and-files-as-function-call-outputs/1360081) | 2025-09-27T00:53:38.546+08:00 | 文本/JSON结果不能直接返回多模态artifact → 新支持图片/文件tool output → observation载荷选择改变；2+1+1=4（Design Delta/System Reach/Durability） | 已关闭 | 仅报告：provider接口支持类型的版本事实，不提供新的通用授权/正确性机制，不改Books |
| [CE-GPPO: Controlling Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning](https://arxiv.org/abs/2509.20712v1) | 2025-09-26 | 旧GPPO已有双beta分段保梯度 → 本稿clip外符号分支的熵动态条件、阶段切换与高熵未必增益反侧 → 重看更新资格与探索/质量取舍；2+1+2=5；日期仅原作者研究披露，非arXivfirst | 深入完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)具体stop-gradient/sign/ratio控制、Jacobian/entropy/预算边界与配置身份；精确配方和局部结果仅报告，No Change |
| [Tequila: Trapping-free Ternary Quantization for Large Language Models](https://arxiv.org/abs/2509.23809v1) | 2025-09-26 | 原ternary QAT零区latent只走量化近似路径 → 输入无关C与原ternary路径联合训练/导出 → 改变算子身份与容量/费用取舍；2+1+2=5；日期仅官方算法release，非arXivfirst | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)QAT首段后两段实际已写/本人顺读，具体PRE§29/非writer实际POST§30通过，root已接纳并释放锁 |
| [Dynamic Reasoning Chains through Depth-Specialized Mixture-of-Experts in Transformer Architectures](https://arxiv.org/abs/2509.20577v1) | 2025-09-26 | 统一深度计算约束 → 专家深度职责与learned router组装路径 → 重看计算分配/执行预算；2+1+2=5，R2准入/联合日通过 | 争议 | 暂缓：R6一次必要采用/中心D1通过；原复杂度上界无法支持所宣子线性，保原5不EX/降分 |
| [Verification Limits Code LLM Training](https://arxiv.org/abs/2509.20837v1) | 2025-09-26 | 测试复杂度/数量与放宽通过阈值的条件对照改变合成训练筛选资格；2+1+2=5，R3准入/联合日通过 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)retention后/12546前原单段及本人注真实保存/完整自读，R12 solePOST通过，新增整合生效/窄位释放 |
| [RollPacker: Mitigating Long-Tail Rollouts for Fast, Synchronous RL Post-Training](https://arxiv.org/abs/2509.21009v1) | 2025-09-26 | 长尾rollout的tail batching与rollout/reward/train资源分工改变同步训练预算选择；2+2+2=6，R3准入/联合日通过 | 争议 | 暂缓：R8一次必要采用/中心D2通过；最快响应选择不一般保policy分布，原6保留 |
| [Go With The Flow: Churn-Tolerant Decentralized Training of Large Language Models](https://arxiv.org/abs/2509.21221v1) | 2025-09-26 | 异构志愿节点/链路失稳下flow重路由改变有效microbatch与延迟责任；2+2+2=6，R3准入/联合日通过 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL [Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)failure后/sensor双段前原单段及本人注真实保存，R25 solePOST通过，I4生效/位释放 |
| [SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips](https://arxiv.org/abs/2509.21271v1) | 2025-09-26 | GH200紧耦合CPU/GPU/C2C改变权重offload、casting与优化器阶段分工；2+2+2=6，R3准入/联合日通过 | 深入完成 | 整合：TRAIN-ZERO [Ch39](../../../../books/part-04-training-system/39-zero.md)目标coldstate段后/UVM前，较宽搬运+GPUcast与尾bucket状态放置原段已保存，R45唯一POST通过；STV完整恢复保证未采 |
| [Nova: Real-Time Agentic Vision-Language Model Serving with Adaptive Cross-Stage Parallelization](https://arxiv.org/abs/2509.21301v1) | 2025-09-26 | 单GPU视觉编码/prefill/decode的弹性空间分配及Pareto调度改变延迟/吞吐取舍；2+2+2=6，R3准入/联合日通过 | 标准完成 | 已有覆盖：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)模型身份组批、stage readiness与SM干扰画像/在线SLO分责，经作者16→R17具体NC通过，Book0 |
| [Meta-Memory: Retrieving and Integrating Semantic-Spatial Memories for Robot Spatial Reasoning](https://arxiv.org/abs/2509.20754v1) | 2025-09-26 | 文本化记忆漏目标 → 独立位置扩召回并回原图核对/查询地图 → 重看检索支持和证据身份；2+1+2=5，R7最小N准入通过 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)STaR完整段后/写时经济性前原单段与本人注真实保存，R22 solePOST通过，I3生效/位释放 |
| [Document Summarization with Conformal Importance Guarantees](https://arxiv.org/abs/2509.20461v1) | 2025-09-26 | 句级重要性阈值校准改变摘要coverage/recall资格；2+1+2=5，R13准入/联合日实际通过 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)goal完整段后/SWE前原单段与本人注真实保存，R26 solePOST通过，I5生效/位释放 |
| [Myosotis: structured computation for attention like layer](https://arxiv.org/abs/2509.20503v1) | 2025-09-26 | 树结构矩阵求逆结合稀疏/递归改变序列算子成本；2+1+2=5，R13准入/联合日实际通过 | 深入完成 | 整合：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)LUCID完整双段后/Parallax前原单段及本人注真实保存，R39 solePOST通过，I7生效/位释放 |
| [Complexity-Driven Policy Optimization](https://arxiv.org/abs/2509.20509v1) | 2025-09-26 | entropy乘disequilibrium替探索bonus，改变均匀探索边界；2+1+2=5，R13准入/联合日实际通过 | 深入完成 | 整合：TRAIN-PPO [Ch32](../../../../books/part-04-training-system/32-ppo.md)总loss后ReferenceKL与熵系数反馈间原单段及本人注真实保存，R36 solePOST通过，I6生效/位释放 |
| [Theoretical Bounds for Stable In-Context Learning](https://arxiv.org/abs/2509.20677v1) | 2025-09-26 | 固定表示谱条件与校准估计改变ICL长度资格；2+1+2=5，R13准入/联合日实际通过 | 争议 | 暂缓：R16首包→作者20唯一必要实际采用，中心D3隔离谱-alone到一般ICL分布稳定/校准继承保证；原5与有限proxy观察保留、不正面Book |
| [Cryptographic Backdoor for Neural Networks: Boon and Bane](https://arxiv.org/abs/2509.20714v1) | 2025-09-26 | 密码触发改变watermark/auth/IP协议的验证与攻击权限；2+2+2=6，R13准入/联合日实际通过 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)组件替换/副本归属及完整签名freshness/独立权限消费者，作者35→R34具体NC3通过；强安全不采 |
| [Parallel Thinking, Sequential Answering: Bridging NAR and AR for Efficient Reasoning](https://arxiv.org/abs/2509.20744v1) | 2025-09-26 | NAR中间trace与AR答案分工改变质量/总费选择；2+2+2=6，R13准入/联合日实际通过 | 争议 | 暂缓：作者33→R32有限必要/中心D4成立，唯一对照更换answer模型且未测两段总费，不能归因NAR互补/净省；原6保持 |
| [SFT Doesn't Always Hurt General Capabilities: Revisiting Domain-Specific Fine-Tuning in LLMs](https://arxiv.org/abs/2509.20758v1) | 2025-09-26 | 小LR/TALR与双质量对照改变domainSFT遗忘取舍；2+1+2=5，R13准入/联合日实际通过 | 标准完成 | 已有覆盖：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)09195/InfoSFT/ConservativeSFT具体承担detached权重、原分母/整体步幅、低概率学习与双质量/全费；R42具体NC通过 |
| [Aligning Inductive Bias for Data-Efficient Generalization in State Space Models](https://arxiv.org/abs/2509.20789v1) | 2025-09-26 | LTI频谱与任务谱初始化改变样本效率成立条件；2+1+2=5，R13准入/联合日实际通过 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)固定basis后/算术语义前监督任务统计首层预校准原段已保存，R46唯一POST通过；有限谱/归一目标强桥不采 |
| [Zero-Shot Privacy-Aware Text Rewriting via Iterative Tree Search](https://arxiv.org/abs/2509.20838v1) | 2025-09-26 | reward引导分段rewrite搜索与实际隐私验收分责；2+1+2=5，R13准入/联合日实际通过 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)30848/21496/14464及trajectory具体承担候选改写、预算best非安全、保义代理与独立释放权；R48具体NC通过 |
| [FS-DFM: Fast and Accurate Long Text Generation with Few-Step Diffusion Language Models](https://arxiv.org/abs/2509.20624v1) | 2025-09-26 | 多步离散扩散预算约束→stepbudget一致性训练/更新及teacher蒸馏→训练与采样质量/费用分工；2+2+2=6，R27准入/联合日通过 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)组合一致/SnapFlow/step条件与离散rate-Euler-hazard的具体消费者；R43具体NC通过 |
| [TyphoonMLA: A Mixed Naive-Absorb MLA Kernel For Shared Prefix](https://arxiv.org/abs/2509.21081v1) | 2025-09-26 | absorb省HBM却不便共享前缀复用→shared naive/nonshared absorb混合→kernel表示与费用选择；2+2+2=6，R27准入/联合日通过 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)scan费用后/scancompiler前，同次attention共享展开/私有latent兼容LSE汇合原段已保存，R44唯一POST通过 |
| [Data-Centric Elastic Pipeline Parallelism for Efficient Long-Context LLM Training](https://arxiv.org/abs/2509.21275v1) | 2025-09-26 | 长短序列/PP容量利用冲突→split/pack与stage-aware chunk checkpoint联排→数据形状/activation预算共同选择；2+2+2=6，R27准入/联合日通过 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL [Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)完整1F1B参数版本段后/SplitBackward前原段及本人注已真实保存/完整自读，R51 solePOST通过，I11生效/位释放 |
| [KeyWorld: Key Frame Reasoning Enables Effective and Efficient World Models](https://arxiv.org/abs/2509.21027v1) | 2025-09-26 | 冗余帧计算/关键transition→轨迹简化标签与关键帧生成/轻插值→生成预算与物理有效性分验；2+2+2=6，R27准入/联合日通过 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)09595完整组后/02278前原段及本人注已真实保存/完整自读，R52 solePOST通过，I12生效/位释放 |
| [Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning](https://arxiv.org/abs/2509.20616v1) | 2025-09-26 | 多轮稀疏reward→专家轨迹转单轮taskreasoning及成功概率桥→重看训练代理与真实长程执行资格；2+2+2=6，R50准入/联合日通过 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)专家trace独立条件/局部组reward与部署偏离人口、Ch26真实handoff分责具体承载，作者96→R86具体NC15通过；Book0 |
| [Scaling Laws are Redundancy Laws](https://arxiv.org/abs/2509.20721v1) | 2025-09-26 | 经验幂律→协方差谱冗余/有限样本risk推导与Transformer推广→重看指数与表示假设；current不严肃说明必须有限核，不预全证；2+1+2=5，R50准入/联合日通过 | 争议 | 暂缓：R53首备→作者61实际必要采用，谱假设下effective dimension发散，指数/最优参数及真实模型桥未闭，中心D5；原5不改 |
| [WeFT: Weighted Entropy-driven Fine-Tuning for dLLMs](https://arxiv.org/abs/2509.20863v1) | 2025-09-26 | dLLM去噪步/token贡献异质→entropy权重SFT→重看监督预算/生成质量；非现GIFT后版；2+1+2=5，R50准入/联合日通过 | 争议 | 暂缓：作者59→R56有限必要一次采用；打印mask/权重及非线性时间采样到积分目标桥不闭，中心D6；原5/局部观察保留 |
| [CORE: Full-Path Evaluation of LLM Agents Beyond Final State](https://arxiv.org/abs/2509.20998v1) | 2025-09-26 | 终态等价隐藏危险路径→DFA合法tool路径与prefix/harm/效率读出→改变agent执行评价；2+2+2=6，R50准入/联合日通过 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)typed路径/receipt、合法替代路径与过程/终态/危害/费用分账具体承载，作者70→R66具体NC9通过；Book0 |
| [Automatic Red Teaming LLM-based Agents with Model Context Protocol Tools](https://arxiv.org/abs/2509.21011v1) | 2025-09-26 | 手工toolpoison只概念演示→自动生成恶意MCPtool及检测逃逸对照→重看工具metadata信任/红队资格；2+2+2=6，R50准入/联合日通过 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)工具metadata信任/poison与代理检测、真实副作用及释放权限分责，作者74→R69具体NC10通过；Book0 |
| [Mechanism of Task-oriented Information Removal in In-context Learning](https://arxiv.org/abs/2509.21012v1) | 2025-09-26 | ICL相关解释不足→lowrank removal干预/denoisinghead消融→重看fewshot选择性读出与因果证据；2+1+2=5，R50准入/联合日通过 | 标准完成 | 已有覆盖：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)任务信号形成/答案读出、状态消费/重学、probe/干预/行为权限具体承载，作者93→R84具体NC13通过；Book0 |
| [DELTA-Code: How Does RL Unlock and Transfer New Programming Algorithms in LLMs?](https://arxiv.org/abs/2509.21016v1) | 2025-09-26 | 有限passK失败与新策略混同→受控问题族/奖励课程及OOD分轴反侧→重看RL可学/可迁移资格；2+1+2=5，R50准入/联合日通过 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)生成器/oracle、真实支持域与parse/执行/算法迁移分验具体承载，作者97→R87具体NC16通过；Book0 |
| [Behind RoPE: How Does Causal Mask Encode Positional Information?](https://arxiv.org/abs/2509.21042v1) | 2025-09-26 | 显式位置编码解释不足→causalmask本身的近邻偏置及与RoPE组合→重看位置关系/模型身份；2+1+3=6，R50准入/联合日通过 | 标准完成 | 已有覆盖：MODEL-POSITION-ENCODING [Ch13](../../../../books/part-02-model/13-position-encoding.md)mask可见性/hidden顺序、期望cov到QK及norm/residual/MLP边界具体承载，R58具体NC7通过；current受影响域已核 |
| [Best-of-$\infty$ -- Asymptotic Performance of Test-Time Compute](https://arxiv.org/abs/2509.21091v1) | 2025-09-26 | 固定N多数投票成本→agreement自适应停止/跨模型权重有限优化→重看无限极限与有限预算；2+1+2=5，R50准入/联合日通过 | 深入完成 | 整合：MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md)固定N裁决后/ACT-SC前计数与未见类别posterior停止原段及本人注真实保存，R81唯一POST通过，I15生效/位释放 |
| [TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them](https://arxiv.org/abs/2509.21117v1) | 2025-09-26 | 分值/成对排序不一致→概率期望与双向likelihood聚合→重看judge对象/一致性与正确性；2+2+2=6，R50准入/联合日通过 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)硬化score/BT段后/Jury前概率读出与双向比较原段真实保存，R75唯一POST通过，I14生效/位释放 |
| [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154v1) | 2025-09-26 | outcome与process二分→组内prefix重叠的隐含credit和lambda改动→重看step/trajectory资格；2+1+2=5，R50准入/联合日通过 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)共享token的ΣωA/clip活跃分支、真实ancestry与loss权重/正则身份具体承载，作者91→R82具体NC11通过；Book0 |
| [Mixture of Thoughts: Learning to Aggregate What Experts Think, Not Just What They Say](https://arxiv.org/abs/2509.21164v1) | 2025-09-26 | 异构专家只route/多轮输出聚合→冻结expert共享latent投影+primarycrossattention→重看内部协作和全费；2+2+2=6，R50准入/联合日通过 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)完整09173第二段inline后/Behavioral belief前持续整模型latent交互原段与本人注真实保存，R92唯一POST通过，I17生效/位释放 |
| [SGMem: Sentence Graph Memory for Long-Term Conversational Agents](https://arxiv.org/abs/2509.21212v1) | 2025-09-26 | 事实/summary丢跨粒度关联→sentencegraph连turn/round/session并取raw+derived→重看memory组织/读取资格；2+1+2=5，R50准入/联合日通过 | 标准完成 | 已有覆盖：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)bounded扩展、raw/derived反向source join、细宽读取和组件/全费具体承载，R62具体NC8通过；Book0 |
| [Query-Centric Graph Retrieval Augmented Generation](https://arxiv.org/abs/2509.21237v1) | 2025-09-26 | entity/doc粒度成本与关系取舍→生成query索引及多跳chunk检索→重看图粒度/索引质量；2+1+2=5，R50准入/联合日通过 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)AudioBoost完整组后/02377前syntheticQA节点经membership回原chunk原段真实保存，R68唯一POST通过，I13生效/位释放 |
| [Tree Search for LLM Agent Reinforcement Learning](https://arxiv.org/abs/2509.21240v1) | 2025-09-26 | 链rollout重复prefix/稀疏reward→共享prefix树及树内外credit→重看训练人口/过程监督资格；2+2+2=6，R50准入/联合日通过 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)可重放prefix分叉、相关叶人口、局部/全局baseline与真实KV/权重具体承载，作者92→R83具体NC12通过；Book0 |
| [RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2509.21243v1) | 2025-09-26 | 轻量VLA丢空间信息→复用registertoken注入actionexpert→重看表示保留与动作质量费用；2+2+2=6，R50准入/联合日通过 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)条件压缩/动作消费、额外encoder费用与共同normalizer竞争具体承载，作者94→R85具体NC14通过；原6保持/Book0 |
| [It's Not You, It's Clipping: A Soft Trust-Region via Probability Smoothing for LLM RL](https://arxiv.org/abs/2509.21282v1) | 2025-09-26 | 硬clip丢梯度→向行为分布线性混合后ratio→重看更新trust资格与探索；2+1+2=5，R50准入/联合日通过 | 争议 | 暂缓：作者68→R63必要一次采用；mixture相对KL界不约束实际policy小trust、β0只常数梯度缩放，中心D7；原5/局部经验保留 |
| [SD3.5-Flash: Distribution-Guided Distillation of Generative Flows](https://arxiv.org/abs/2509.21318v1) | 2025-09-26 | flowfewstep质量/设备费→timestep共享与split-timestep蒸馏+执行优化→重看目标归因与净成本；2+2+2=6，R50准入/联合日通过 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)完整K-DMD08303后/逐对象teacher前轨迹score状态及分区训练后单权重合并原段真实保存，R93唯一POST通过，I18生效/位释放 |
| [RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards](https://arxiv.org/abs/2509.21319v1) | 2025-09-26 | 自然feedback难直接作reward → 二元原则及entailment RM、推理时原则定制 → 重看偏好监督对象与reward/验收分责；2+2+2=6，作者65→R60准入/联合日通过 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)28078解释监督后/DeCert前原则条件二元满足RM原段与本人注真实保存，R91唯一POST通过，I16生效/位释放 |

原tool-output/CE-GPPO/TEQUILA及代表性AARP排除的有效层复用；A*与其余窗外导航只作真实归属路由，不移入本窗。全部候选的日期、分数与证据权限分别维护，个别正面采用不授所有来源全覆盖。

## 4. 证据与知识整合

### [Images and files as function call outputs](https://community.openai.com/t/images-and-files-as-function-call-outputs/1360081)

采用原帖post1837147/version1，created_at与updated_at同为`2025-09-26T16:53:38.546Z`，未用搜索显示日期推定。原[JSON](../_sources/daily-20250927/tool-output-post.json)全文核心是tool function可返回images/files而不仅JSON/text。发帖者Edwin Arbus的OpenAI角色由其原自述与官方ack恢复；当前staff=false/Regular原值保留，不把论坛管理员标志当当时雇佣/发布权限证据。

必要读取当前官方[Function calling](https://developers.openai.com/api/docs/guides/function-calling)“Formatting results”：文字结果与image/file对象array有不同representation。该当前文档并非2025精确快照，因此不采用当前模型名、完整字段、兼容范围或安全行为作当时事实。没有benchmark、实际API执行、SDK代码核验或生产可靠性证据。

实际读`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)10–55：environment observation回到Context、tool identity/version与typed output/error schema、executor负责validation/authorization。新发布只落在某provider允许的载荷版本，没有新的普适权限/正确性机制，故仅报告而非强造Books增量；不是按“原原则未变”排除实际发布贡献。交接见[CALIBRATION_HANDOFF](../_sources/daily-20250927/CALIBRATION_HANDOFF.md)。

### [CE-GPPO: Controlling Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning](https://arxiv.org/abs/2509.20712v1)

采用[精确v1正文](https://arxiv.org/html/2509.20712v1)，Sep26事件依据[作者项目News](https://github.com/Kwai-Klear/CE-GPPO)，不拿Sep25 Submitted或当前ERC代码作为Sep26实现/全球first；新双beta/stop-gradient公式在原GPPO2508.07629v1已存在，本篇新增限熵动态条件证据/阶段切换与质量反侧。v1 Eqs8–10将beta1用于ratio<1-epsilon且A<0、beta2用于ratio>1+epsilon且A>0，otherwise仍ratio*A；sg只解耦forward/backward。beta=0只使这两个原PPO停止枝零梯度，不使全部forward标量逐处等价PPO。系数界不界全部参数梯度、Jacobian、KL或长期训练；原文§3.2把beta作用方向反写，与公式及§5.1相反，不能拼成统一recipe。

A.2是tabular-softmax/小步/centered-A局部近似。v1 Eq23错误将E_pi[pi*A]等同E_pi[A]=0，pi=(0.9,0.1)、A=(1,-9)分别给0.72与0；不采用该消项，Eq22完整covariance不因这步自动失效。当前精确v5受影响Step4已直接保留covariance、修掉错误消项，但方法beta反向文字仍在；当前补证不倒填v1或授深网熵普遍定理。Feynman实际§5–9完成这些正确性域独核；不遍历版史/2026全文。

作者数学切片：MathSub30K/9gram处理、DS-R1-Distill-Qwen1.5B/7B，8rollouts/16k训练、lr1e-6、最多1000steps/约10epochs、noKL；评测AIME24/25 32k、其他16k，avg32与MATH500 avg4分账。Table1平均54.9/67.5对DAPO52.4/64.5，但本文DAPO只是GRPO+clip-higher，不是原DAPO完整系统。Table2 CE54.9/GSPO54.3、AIME24反低42.0/42.5、AMC23打平；Fig2 caption AIME25/正文AIME24不拼数。高entropy不单调改善，585step切beta是局部调参，CISPO局部collapse不证明CE任意配置稳定。硬件/precision、完整预算、重复训练seed/不确定性、主表beta与选择协议Not Disclosed；不授完全去污染、总算力公平、生产SLO或复现。

`TRAIN-GRPO` Ch33原203–221具体forward/backward、正负sign/ratio、stop-gradient与软gate完整邻接，原698–722 IS-weight clip语义/配置身份，实际承载长期采用命题；不是只凭主题相似或声称已有CE全部公式。Ch32 PPO ratio/clip与reference职责、Ch34离线preference交接保护。Feynman实际已有覆盖/No Change通过，无新长期缺口、Books写入/锁/POST；精确配方和局部实验仅报告。全部有限原证/实际读域及current差额见[单篇包§5–8](../_sources/daily-20250927/SUP_CEGPPO_20261013.md)，不重复正文/权重审阅。

### [Tequila: Trapping-free Ternary Quantization for Large Language Models](https://arxiv.org/abs/2509.23809v1)

采用[精确v1](https://arxiv.org/html/2509.23809v1)§2–3/Eqs1–8、§4/Tables1–3与AppendixC的必要域；原[AngelSlim News](https://github.com/Tencent/AngelSlim)25/09/26明确released ternary quantization algorithm并链接同paper/code，支持Sep26算法release。v1 SubmittedSep28/v2Oct17只保版本角色，不宣Sep26论文first、当时同字节稿或current分支全部为release实现。Feynman§26–28日门/准入/5分及受影响正确性深入实际通过，原件200/exit0及217739bytes身份保存，不代理语义核。

§3.2在原ternary输出之外加入deadzone latent形成的输入无关C；Eq8含原量化STE输入路径和辅助bias直接梯度，不是全部QAT真导数/无STE。D集合/scale/阈值切换仍须选择与处理，不给一般收敛或trapping-free保证；activation近似对称不证明含sign(x)分支与C逐输入等价。per-weight learned lambda与实验固定默认.001分责，不拼统一训练recipe。AppendixC三权重4bit index＋1bit sign另有channel bias、scale与activation LUT：只导三值码而遗漏C不是同算子，log2(3)信息量不等整模型1.58bit或零费，不授TensorRT/GPU已有支持。

质量人口为Llama3.2-1B/3B、UltraFineWeb10Btokens/G128、16H100训练/seq1024/lr1e-4、lm-eval zero-shot。Table1含GPQA/Table2不含，均值不混；1B ARC-e/c对BF16差.9/.8pp，而3B差4.3/7.6pp，3B ARC-c .346低于TWN .351，1B WinG也落后BF16，不能采用全部任务胜出/任意尺寸<1pp。Table2异尺寸/100B与带星有限10B复现不作同预算单因果。lambda过大bias支配、过小无效，粒度标签正文per-token/表per-tensor不一致，局部消融不授任意配置稳健。CPU速度另为Intel8263C、.7B/3B/LUT路径，不与1B/3B质量拼同quality3x；作者bias-add<.1%非E2E免费。完整线程/batch/concurrency、prompt/output测时协议、精度/seed/CI/SLO Not Disclosed，未核实现/运行或复现。完整强反侧见[单篇§3–4](../_sources/daily-20250927/SUP_TEQUILA_20261013.md)。

实际Ch49 QAT首段已有准备费用/fake-quant，后文已有latent→codes导出一致性与额外高精度FFN/router，但原本未承载同deadzone latent输入无关C、混合梯度和逐输出channel bias联合导出。唯一owner及完整邻接已actual比较，具体PRE Feynman§29通过；root窄锁下已在QAT首段后、原“QAT 的在线 forward…”前实际插入两段（当前1038/1040）及自身末note，保输入/输出维、阈值与元数据费用、非等价及普通QAT/较高位fallback，无headline性能或paper收纳小节。作者已顺读实际两段/完整局部邻接及自身注，unstaged仅6add/0delete，既有其他任务cached20add/0delete逐字未变。Feynman§30已actual顺读真实正文/完整邻接/own note并通过非writerPOST，root也已实际读回接纳并释放锁；采用落实1，不授代码运行/复现或日级DAY/FINAL。

### [Dynamic Reasoning Chains through Depth-Specialized Mixture-of-Experts in Transformer Architectures](https://arxiv.org/abs/2509.20577v1)

必要有限原域经Helmholtz R6一次实际采用，中心D1有效；保原5与候选，不以EX/降分代争议。严谨反例是原O(n)上界允许路由成本Troute=n，此时k log n+n非O(k log n)，不是已测本实现必Omega(n)；激活深度更少不补齐这个复杂度桥梁。原表局部观察与两均值差额、任务/预算/人评未披、全部路由与expert训练费用保持。正面效率/解释性强采用不入Books，重开只需明确原执行成本/假设及可比评价全费接桥；未核实现或复现。

### [Verification Limits Code LLM Training](https://arxiv.org/abs/2509.20837v1)

R4首次有限必要→作者8唯一另一角色回精确v1 §2–6/9及必要A/B实际采用通过。固定Command7B SFT、默认70K合成+70K公共code+5%通用/3seed平均、六bench 1-shot pass@1按人口加权；留存条数同不等总token/生成费同。测试复杂度、数量与通过门槛改变过滤后难度/解支持，较强tests下局部宽门有益，弱tests和多teacher部分语言仍退。41K配对所谓correct是tests均值.85而非形式证明，human300的100fail/200pass重采样、27 unsure与有限专家tests不认证自然流量真值；A1 judge身份及MBPPPlus原tests差异保留。全部生成/执行feedback/扫参/人审/训练回归费用另计，未核代码/复现。Ch27 retention后/12546前的原单段/standalone/本人注已真实保存、自读并获R12唯一actualPOST通过，I2生效/窄位释放；只诊断要求，不称已完成固定总预算对照。

### [RollPacker: Mitigating Long-Tail Rollouts for Fast, Synchronous RL Post-Training](https://arxiv.org/abs/2509.21009v1)

作者7首次有限必要经Helmholtz R8一次实际采用/中心D2通过。短round超发prompt及response、只保最快完成，不只是重排同样本；R0=8/eta1.25发10保8，在policy各半出短A/慢B时，保留B频率为771/2048而非1/2，reader独立枚举1024结果相同。prompt最终见到、不提前改weights和按已选样本数归一gradient不校正该response选择。保作者有限validation曲线/分组收益，不宣所有质量必降或表虚构。128H800是总cluster、各7/14/32B用16/32/64GPU及8/16/32k，累积T2收益不全归tail；eta1.5长序列反退、MPS无fault隔离、profile/过量生成/重生/迁移与hostgradient全费保。原6候选与局部观察保留，严格分布/等质净费强采用不入Books，待具体选择校正/目标与匹配质量预算接桥。

### [Go With The Flow: Churn-Tolerant Decentralized Training of Large Language Models](https://arxiv.org/abs/2509.21221v1)

精确v1完整AB/身份与合法联合日门已R3通过，原6保持。有限必要III–VII已作者14→R15一次实际采用：局部flow匹配/重路由与保存activation补算依赖stage参数同步，timeout只suspect、每stage至少一活节点；不授exactly-once/Byzantine或任意churn同SGD。Eq1仅cost proxy、1024dim/18heads配置冲突、5GPU模拟地理节点/50–500Mb/s及部分baseline反退、全部控制/恢复/聚合费用保留。Ch38固定mapping failure之后、完整sensor双段之前尚缺局部流恢复的参数/迭代接纳责任；作者22原三项经R21整体PRE/root本轮fresh新授、作者26真实保存/完整自读，R25唯一actualPOST通过，I4生效且指定窄位释放。原checkpoint退路/sensor绑定与他注保全，不第三Source；见[本轮§14–15/22/26](../_sources/daily-20250927/REPAIR_20261025.md)。

### [SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips](https://arxiv.org/abs/2509.21271v1)

精确v1完整AB/身份与合法联合日门已R3通过，原6保持。GH200上placement/casting/尾bucket与STV有限必要经作者17→R18一次实际采用，见[本轮§17](../_sources/daily-20250927/REPAIR_20261025.md)：GPU casting搬FP32可能比CPU cast搬FP16更便宜，尾bucket驻GPU可隐藏CPU更新；STV需恢复optimizer状态和已消费暂定权重的forward，文中未交完整失败重算桥，不从loss曲线授精确等价。保有限硬件/人口、baseline差异与全部profile/传输/回滚费；TRAIN-ZERO/Ch39目标coldstate后/UVM前补入较宽搬运/GPUcast与尾bucket放置及失败依赖资格，R45唯一POST通过；STV精确恢复强桥仍隔离。

### [Nova: Real-Time Agentic Vision-Language Model Serving with Adaptive Cross-Stage Parallelization](https://arxiv.org/abs/2509.21301v1)

R5首次有限必要→作者10唯一另一角色回精确v1 II-B/C、III-A–E、IV/V/VI受限域实际采用通过。三worker/samepriority streams、prefill/decode共享weights，vision/prefill不共跑，decode与两者弹性分连续SM；HBM/L2仍共享且可竞争。E1–4是profile/平均长度/无队列理想枚举，pending代arrival/E5为启发式；M/G/1稳定前提不由自适应策略保证，表V lambda.8利用率1.08已超载，500请求max非硬最坏界。vision层buffer/H2D/events有费，省约91.95%仅vision显存，K3–5 E2E对raw反退；4090全部baseline也卸vision。CogAgent13B BF16/A6000或4090/AndroidLab与Poisson及私有interval重缩只该人口，未验所有框架最优、完整SLO或复现。完整画像/队列/驻留/迁移/质量回归费与静态/单stage退路保留，INFER-SCHEDULING/Ch56的model-identity组批、stage-local readiness/份额干扰profile与在线SLO分责经作者16→R17具体NC通过，Ch54 ready-buffer接口仅角色复用，无新Book/注。

### [Meta-Memory: Retrieving and Integrating Semantic-Spatial Memories for Robot Spatial Reasoning](https://arxiv.org/abs/2509.20754v1)

同DOI精确v1 S=Sep25T05:22:52Z、L=Sep26T00:00Z与registered U=Sep26T01:44:13.000Z的合法联合日门已R3通过。原III-A/B决定性核心经R7一次实际采用，2+1+2=5：同entry保caption/embedding、四帧合图与位姿；SSR文字top-k后回图，caption漏对象时以位置半径扩候选，再筛/回图；MI地图不等真实可走路径或当前环境truth。标准必要IV/V/VI已R10一次实际采用，六scene270题/15m容差、三runs/人类协议、逐scene反退与offline robot/静态场景/全部云调用费用均保留。Ch77缺少caption漏实体时独立位置扩召回且回原图验支持的consumer；作者19/R19整体PRE→本轮fresh新授→作者23真实保存/完整自读→R22唯一POST通过，I3生效/指定窄位释放。STaR完整inline和后缓存经济性双段保全；只该有条件扩召回接口，不授机器人现场安全，见[本轮§11/19/23](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Document Summarization with Conformal Importance Guarantees](https://arxiv.org/abs/2509.20461v1)


R14首备→作者18唯一非准备者回精确v1 S2–6/E4–15/A1.1–2/C5实际必要采用，原5保持。按document标签召回校准抽取阈值，交换性下只marginal lower coverage，ties不继承所印tight upper、alpha端点/空标签须定义；beta<1允许漏标签，标签非全现实重要性。400split/五dataset与SBERT或GPT标签/局部反退/全context逐句评分费保留，abstractive不继承coverage。Ch75原goal/leave-one-out/future-obligation未承担按整份文档标签召回校准摘录门的consumer；[作者24原三项](../_sources/daily-20250927/REPAIR_20261025.md)经R23整体PRE/root本轮fresh新授、作者27真保存/完整自读，R26唯一actualPOST通过，I5生效/窄位释放。goal完整段后/SWE前，公式及后续全部绑定保全；非无损、逐件或生产安全保证。
### [Myosotis: structured computation for attention like layer](https://arxiv.org/abs/2509.20503v1)

原日/5沿R13，作者21→R20有限必要通过。tree-sparse系统的dense inverse可经上下Schur消息实现，fixedblock/平衡树/资源与可逆pivot约束复杂度，非exactsoftmax或causalcache；sign/rhs不统一不拼recipe，分类布局/控制混杂、LRA反退与全费保。当前Ch14 LUCID只预条件Value再读取，Parallax是learnedprobe，未承担整树逆混合；作者34→R33整体PRE/root本轮独立fresh新授→作者44真保存/完整自读→R39 solePOST通过，I7生效/位释放。原双段/完整两侧与本人注全保，未核代码或复现；[必要/原稿/实存](../_sources/daily-20250927/REPAIR_20261025.md)。
### [Complexity-Driven Policy Optimization](https://arxiv.org/abs/2509.20509v1)

原日/5沿R13，作者25→R24有限必要通过。C=entropy×disequilibrium保完整productrule，不detach，uniform仍零梯度，概率方向非共享theta保证；小离散环境/三seed跨系数聚合非LLM/连续action或免调参，全费保持。Ch32原总loss与熵系数反馈不接目标形状接口，作者32→R31整体PRE/root本轮fresh新授→作者41真存/完整自读→R36 solePOST通过，I6生效/窄位释放。原ReferenceKL/12324绑定及总loss/ordering围栏未拆；[具体证据与原稿](../_sources/daily-20250927/REPAIR_20261025.md)。
### [Theoretical Bounds for Stable In-Context Learning](https://arxiv.org/abs/2509.20677v1)


R16首备→作者20唯一非准备者回必要v1与current-v3受影响桥实际采用，原5保持、中心D3隔离。固定表示谱floor不自动保证黑盒LLM重采样输出分布：iid Rademacher谱恒1，合法首demo-sensitive generator两prompt输出TV1概率仍1/2；这只反无generator约束的谱-alone蕴含，不反额外ridge/Lipschitz条件。v1矩阵/Alg1 margin与doubling置信、accuracy knee非分布稳定、经验quantile/alpha不继承worst-direction保证均保；v3已澄清proxy并有later有限resampling，不倒填2025。局部谱proxy观察与全费留报告，正面保证不入Book，重开条件见[作者20](../_sources/daily-20250927/REPAIR_20261025.md)。
### [Cryptographic Backdoor for Neural Networks: Boon and Bane](https://arxiv.org/abs/2509.20714v1)

原日/6沿R13，root首备→作者29唯一另一角色实际必要采用。黑盒固定verifier的签名路由不等不可移除模型属性；不防删wrapper/蒸馏提取，签名不防合法pair重放、首图局部message非全batch/session，HMAC mod类碰撞不能用256bit界。局部图像分类/100trigger、25.8倍decode与密钥/路由/审计全费保，强安全不采。作者35→R34具体Ch72 NC3：组件可替换、取证非预防/副本逐一排除及完整签名/freshness/原子消费已承担有限消费者，非同算法或已实现本协议；不加段/marker/注。[必要包](../_sources/daily-20250927/ROOT_NECESSARY_20261025.md)/[当前比较](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Parallel Thinking, Sequential Answering: Bridging NAR and AR for Efficient Reasoning](https://arxiv.org/abs/2509.20744v1)

原日/6沿R13，作者33→R32有限必要/中心D4通过。Mercury NAR trace后，答案分别Mercury/GPT5 auto，唯一对照同时换answer模型，缺同answer有无NAR/AR trace与总预算控制，不能识别所谓互补/忠实因果。20/10/20题加权78/52合法，原unweighted文字冲突只保口径，不指表值无分母；未足判定/重复CI。无两段latency/NFE/token/auto隐藏推理/完整API费用，NAR并行非零费。原6候选与局部观察保留，强互补/净省不入Books；重开需具名matched控制及可核质量/全费，见[作者33/R32](../_sources/daily-20250927/REPAIR_20261025.md)。

### [SFT Doesn't Always Hurt General Capabilities: Revisiting Domain-Specific Fine-Tuning in LLMs](https://arxiv.org/abs/2509.20758v1)

原日/5沿R13，作者36→R35有限必要通过。小LR是domain/general配对tradeoff非越小越好；TALR实际unnormalized p^(1/tau)、stop-gradient/floor.01、全supervisedtokens N平均，tau为batch各sequence平均loss的median，不是全权重归一。它同时重分token并缩整体步幅，未有meanweight-matched控制不能全归hardtoken异质性；低p非错误/无用。CoT rejection34,176与labelonly49k、general低基线任务剔除及checkpoint选择split未闭、部分任务反退保留；tilting非AdamW/accuracy通用定理。16–32A100/训练/teacher/搜索/概率与双质量回归全费，未核全proof/像素/代码复现。TRAIN-SFT/Ch29的09195/InfoSFT/ConservativeSFT已具体承担detached权重、原分母/整体步幅与低q学习/双质量，R42具体NC通过；[必要§36/R35](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Aligning Inductive Bias for Data-Efficient Generalization in State Space Models](https://arxiv.org/abs/2509.20789v1)

精确v1准入/联合日与原5沿R13；root首备→[作者31](../_sources/daily-20250927/REPAIR_20261025.md)唯一另一角色回S2–5/C1–2/D1–5/E/F实际必要采用。固定LTI的PSD kernel/白化SVD成立，但有限Toeplitz不等采样频响精确谱：a=.5/L2的trace9/4与频响模方和40/9不等；归一loss对C乘2不变而J乘4，且证明/实现任务谱对象不同，不能授普遍泛化定理。任务有标签crosscov首层预校准可作受限分支，低频轻退/ListOps不系统、四层S4D/5seed聚合/非LM或selective、全部标签/预拟合/主训与重校准费保留。MODEL-LONG-CONTEXT/Ch22固定basis/21454后、算术01765前已补入监督任务统计首层预校准原段，R46唯一POST通过；强理论隔离不自动全family D；[root必要包](../_sources/daily-20250927/ROOT_NECESSARY_20261025.md)存精确原件与边界。

### [Zero-Shot Privacy-Aware Text Rewriting via Iterative Tree Search](https://arxiv.org/abs/2509.20838v1)

原日/5沿R13，作者42→R37有限必要通过。只persona/PII segment条件的候选与reward-guided UCT逐段生成，不是DP/已证泄漏门；accept符号冲突且预算尽返best不failclosed。准确segment假设/实际F1低、NLI与Flair同源代理不认证联合隐私，3.07ASR无足够channel/prior/人口，未改token亦可能泄漏；A10具体失败/别称保留。ECHR全改质量低原文/5句，Distinct2尺度不闭；top-p5/设备2026引用异常不改日门或擅修recipe。42.5min/100=25.5s非印51s，市场租价非总账单，所有对齐/树/模型/人审与发布费用保。PLATFORM-SECURITY/Ch72的30848/21496/14464和trajectory已具体承担候选改写、budgetbest非安全、保义与独立释放权，R48具体NC通过；[§42/R37](../_sources/daily-20250927/REPAIR_20261025.md)。

### [FS-DFM: Fast and Accurate Long Text Generation with Few-Step Diffusion Language Models](https://arxiv.org/abs/2509.20624v1)

原6/精确v1与联合Sep26日门沿作者28→R27（S Sep24T23:59:05Z、L Sep26T00Z、U Sep26T01:41:05.000Z，完整同BJT26日）。R29首备→作者39唯一另一角色有限必要实际采用通过：h条件化/EMA shortcut teacher/累计rate与path/KL训练保有限采样budget分支。B1 holding-time jump与C2字面Euler不同，h.9/线性scheduler例Euler负stay而jump.9合法、endpoint未闭，不拼运行recipe/四阶保证。PPL为reference proxy、1024NFE反退/训练token预算不同、128只NFE比；teacher额外训练/EMA与完整采样/独立回归费均计，artifact soon/release口径保。MULTIMODAL-GENERATIVE-PARADIGMS/Ch24组合一致/SnapFlow/step条件及CTMC/Euler/hazard完整消费者已具体覆盖，R43具体NC通过；[§39/R29](../_sources/daily-20250927/REPAIR_20261025.md)。

### [TyphoonMLA: A Mixed Naive-Absorb MLA Kernel For Shared Prefix](https://arxiv.org/abs/2509.21081v1)

原6/精确v1与联合Sep26日门沿R27（S Sep25T12:32:02Z、L Sep26T00Z、U Sep26T01:52:05.000Z）。root首备→作者37唯一实际必要采用：sharedprefix展开/private latent两路按兼容空间/softmax分母LSE合并，不能平均已归一输出或任意交换矩阵。局部kernel吞吐非全Serving，384NPU/FP8约3%只是预算估算非单卡实测，制备/驻留/投影/profile/dispatch/通信/数值质量全费。INFER-TENSORRT-LLM/Ch49 scan费用后/scancompiler前已补入同时分历史域的物理表示与LSE汇合原段，R44唯一POST通过；[必要包](../_sources/daily-20250927/ROOT_NECESSARY_20261025.md)/[原三项§43](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Data-Centric Elastic Pipeline Parallelism for Efficient Long-Context LLM Training](https://arxiv.org/abs/2509.21275v1)

原6/精确v1与联合Sep26日门沿R27（S Sep25T15:01:25Z、L Sep26T00Z、U Sep26T01:56:42.000Z）。root首备→作者38唯一实际必要采用，只InfiniPipe/EPP不反投current Concertina/DPP/MEPipe。1F1B flush域内costmesh split/pack、长先分组与stage/chunk checkpoint联排；K/V/dKV寿命不随checkpoint取消，所有logicalsequence/mask/target权重与optimizer边界另验。DP/MILP仅受限cost域最优，CPU求解/profile与所有重算/驻留通信计费；4×8A800/20iteration均值无最终quality/gradient等价，不能授sameSGD或全框架净省。TRAIN-PIPELINE-PARALLEL/Ch38完整1F1B参数版本段后/SplitBackward前已补入token切片/KV-dKV寿命与重算分责，R51唯一POST通过；[有限原域§38](../_sources/daily-20250927/REPAIR_20261025.md)。

### [KeyWorld: Key Frame Reasoning Enables Effective and Efficient World Models](https://arxiv.org/abs/2509.21027v1)

原6/精确v1与联合Sep26日门沿R27（S Sep25T11:35:40Z、L Sep26T00Z、U Sep26T01:50:47.000Z）。R30首备→作者40唯一实际必要采用：GTpose/RDP关键标签、文本/初图条件keyframe生成、gap与FILM插值分工，不是action-conditioned真实控制。RDP端点/尺度与gap时长误差、质量/对象指标多项反退和密度非单调保；headline5.68可由附录聚合得到，原两表spatial时间差不私修。81帧5秒视频生成约170–182秒非实时闭环，人审对象/PSNR非安全。所有标签/预训域训/插值/独立物理与任务验收费，未核真机/代码复现；MULTIMODAL-GENERATIVE-PARADIGMS/Ch24完整09595后/02278前已补入关键帧监督/gap预测与插帧时间接口，R52唯一POST通过；[§40/R30](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning](https://arxiv.org/abs/2509.20616v1)

精确v1/原6及Sep26联合日门保持。root有限必要→作者81回S2–5/定义/式1–21/定理与T1–4实际采用：固定唯一专家路径的动作概率乘积不等全任务success，专家状态训练不证明未见状态改善，强all-states假设不由GRPO自动满足；理想population/unclip fixedpoint不签有限训练。70B成功rejection→SFT→单轮GRPO的四小任务局部SR保留，ASST条件成功人口/14B表文冲突、缺等总compute多轮对照与全部专家/训练/环境费用保。Ch33已具体写专家trace独立条件及局部reward、真实部署偏离人口；作者96→R86具体NC15通过，Book0。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Scaling Laws are Redundancy Laws](https://arxiv.org/abs/2509.20721v1)

精确v1/原5与联合Sep26日门经R50通过；reader R53首备后作者61唯一另一角色回S2–5/A1.1/A1.4/A1.14实际必要采用，中心D5成立。打印beta>1、lambda_i~i^(-1/beta)使effective dimension无限；计数应t^-beta，所印有限variance/指数因而无桥。另独立微分复核最优regularizer倒beta、全s严格凸性反例，不能由upperbound升真实risk Theta。NTK/LN可逆、SGD≈ridge和受控kernel drift是强假设非真实LLM已证；合成Gaussian/AR1/RFF图不能补真实Transformer/数据验证和全训练费。当前“不严肃研究”说明保留但不当正式撤回/默EX；原候选5分不改，只隔离普遍redundancy law/指数配方/Transformer推广，不入Books。重开需一致合法谱/有限维与risk上下界/真实模型桥；[必要采用§61](../_sources/daily-20250927/REPAIR_20261025.md)。

### [WeFT: Weighted Entropy-driven Fine-Tuning for dLLMs](https://arxiv.org/abs/2509.20863v1)

精确v1/原5与联合Sep26日门沿R50。作者59→R56一次有限必要采用：先mask全部答案估entropy，再改变token去噪时间/训练权重；打印Alg1的answer mask、beta参考与最终loss资格不一致，可达0/0，未私补实现。非线性时间变换缺密度/Jacobian，不能由原积分推出该采样目标；中心D6隔离强执行/理论桥，不否局部观察。39/64/83%为相对base增益恢复，非总准确率提升，实际对SFT均值差2.58/2.08/1.51pp且若干任务反退。LLaDA8B/LoRA、4H100、额外训练约24%及全部估熵/训练/评价费保；未核代码/复现，不入Books。重开需一致mask/时间测度/目标与匹配质量全费，见[§59](../_sources/daily-20250927/REPAIR_20261025.md)。

### [CORE: Full-Path Evaluation of LLM Agents Beyond Final State](https://arxiv.org/abs/2509.20998v1)

精确v1/原6与联合Sep26日门沿R50；作者66→R61有限必要通过。DFA对有限参数化tool路径分类，压缩合法selfloop后以LD/Kendall/prefix等读出；模拟state不是真实副作用rollback，efficiency选不超过raw长度的最大gold而非最短，HLR只是离线候选非实际修复。14world文字/15表行、validrun条件人口与全部DFA/gold/trace/执行费保。作者70→R66具体NC9：Ch66的01771/AuditKIT/ProcedureAware组及Artifact→Process→EnvironmentEvolution、危害witness和异步clock已具体承担typedtrace/receipt、合法替代路径、过程与终态分账、早停误读与调用数非真实成本；不声称实现同五指标。无新正文/marker/注；见[§66/70](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Automatic Red Teaming LLM-based Agents with Model Context Protocol Tools](https://arxiv.org/abs/2509.21011v1)

精确v1/原6及联合Sep26日门沿R50；reader R65首备→作者71实际必要采用。自动生成MCP tool metadata/poison与重试、指定task/candidate人口和代理检测对照不证明真实用户攻击频率或防御安全，工具运行/数据外传与judge接受分开；受限成功/拒绝及全攻击、检测、模型调用/回归费保。作者74→R69具体NC10：Ch72现工具description/schema和运行时内容均不取得authority，检测proxy与side-effect/释放gate具体分责已承载，不把红队高命中当生产风险。Book0。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Mechanism of Task-oriented Information Removal in In-context Learning](https://arxiv.org/abs/2509.21012v1)

精确v1/原5及联合Sep26日门保持；reader R72首备→作者87实际采用、R80角色复用。监督affine低rank filter/截断未来context、flux几何probe与DH消融不等自然ICL唯一机制；rank不限制任意缩放后的输出variance，unseenlabel不证全induction关闭，8B/Qwen未近0及局部instruction反退保。作者93→R84具体NC13：Ch5任务形成/答案读取、原状态消费/adapter重学、probe/干预/行为及充分/必要分责已具体承载；非声称实现TVS。标签、head搜索、全部训练/回归费用保，Book0。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [DELTA-Code: How Does RL Unlock and Transfer New Programming Algorithms in LLMs?](https://arxiv.org/abs/2509.21016v1)

精确v1/原5及Sep26联合日门保持；R77首备→作者89回S2–4/S6/A1–3具名域实际采用，R84角色复用。Manufactoria 0/128只有限零命中，不是零support或预训从未见FSM；dense warmup→binary、成功trace进prompt与feedback替EOS均改变条件人口。结构/参数/组合/transformative分轴不混，跨family反退、物理oracle容差与过滤人口保。新语法、可执行测试和内部算法仍须分验；生成/审校/课程、16H100训练及独立泛化全费保。作者97→R87当前Ch66具体NC16通过，Book0，不列外阻。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Behind RoPE: How Does Causal Mask Encode Positional Information?](https://arxiv.org/abs/2509.21042v1)

精确v1/原6与联合Sep26日门沿R50；reader R54首备→作者63回v1 S3–6/E1–4/A1.1–2/B/D及current-v4受影响LayerNorm域实际采用。v1期望Gram递推不能无条件继承随机归一后均值，二token反例保；v4 cross/√d不收敛0，保large-d近似与有限实测，不授全pair精确式或任务因果收益。局部20B训练/attention均值、1000docs与全部模拟/训练/评测费保。作者64→R58具体NC7：Ch13完整mask可见性/hidden顺序、G(d)期望cov→QK对齐的norm/residual/MLP/input假设及positionid/cache身份已有消费者，非精确坐标/PE替代/无限长度保证。无新段/marker/注；见[§63–64](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Best-of-$\infty$ -- Asymptotic Performance of Test-Time Compute](https://arxiv.org/abs/2509.21091v1)

精确v1/原5及Sep26日门保持；作者77→R71有限必要通过。答案计数及未见类别质量的Dirichlet/DP后验近似用于继续采样/停止，mode非truth、近似BF非已校准有限delta；跨model离线gold权重、池内重复、不可解析删除/MC/tie及完整预采/驻留/在线费用保。作者85原三项/R79纯PRE后经本轮fresh新授，88真实保存Ch20固定N段后/ACT-SC前并完整自读；R81唯一actualPOST通过，I15生效/位释放。未授严格MILP tie等价、全预算最优或实现/SLO。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them](https://arxiv.org/abs/2509.21117v1)

精确v1/原6及Sep26日门保持；R67首备→作者72实际必要采用。硬score读出改为完整候选概率的期望，双向likelihood先对齐同候选再聚合，改变测量接口而不认证真实正确；候选tokenization、长度归一、顺序/人口与概率可得性必须绑定，局部一致性/准确率和调用费用分账。作者75原三项/R70纯PRE后本轮fresh新授，80真实保存Ch66硬化score段后/Jury前并自读，R75唯一actualPOST通过，I14生效/位释放。全部teacherforce/双向judge及独立质量核验费保持，不授通用无bias。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154v1)

精确v1/原5及Sep26日门保持；root首备→作者82实际必要采用，R74角色复用。固定prefix未clip线性项可重组，但任意subset/n0定义不自动成树，alive方向与clip前后平均不等；lambda权重同时改整个loss/KL与梯度尺度，不是获得语义PRM。group/LR/step共变、局部Qwen/Llama反退及全部prefix/rollout/validation费保。作者91→R82具体NC11：Ch33共享scoregradient乘ΣωA、clip活跃分支、真实ancestry与loss/正则身份已直接承载。Book0，不认可全树/反exploitation保证。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Mixture of Thoughts: Learning to Aggregate What Experts Think, Not Just What They Say](https://arxiv.org/abs/2509.21164v1)

精确v1/原6及Sep26日门保持；作者78→R73有限必要通过。冻结多个完整模型经共享宽度/分段crossattention交互，primary发布token；同伴仍逐步decode/保有独立KV与历史，异构tokenizer不同步不等相同文本位置，跨词表KL未闭。1.545B是全45.75B池的可训比例，非单7B代价；正确drop-one均值/小收益、单seed与不配平消融及全backbone/交互训练费保。root当前owner首包→作者99实际回Ch21/82完整论点采用：生成前融合尚未承担持续latent交互，Ch82原段经R89整体PRE/本轮fresh新授后101真实保存/完整自读，R92唯一actualPOST通过，I17生效/位释放。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [SGMem: Sentence Graph Memory for Long-Term Conversational Agents](https://arxiv.org/abs/2509.21212v1)

精确v1/原5与联合Sep26日门沿R50；作者60→R57有限必要通过。七index中句级seed扩展语义/结构邻接、回parent原chunk并合raw/derived；语义边非事实、初始cap不约束全部扩展，同K非同token。LongMemEval/LoCoMo有限同源judge/抽样及配置共变保，LCFull .558高SGMem最佳.542，SGMemS K10 .614低K5 .644；RAGSMFI .680实际高于.676，不作反退。作者67→R62具体NC8：Ch77 boundedanchor/evidencepack、raw-derived反向source join、SegTreeMem细宽读取和组件拆分/全费已有具体承载，句均值仅该接口实例。无新段/marker/注；见[§60/67](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Query-Centric Graph Retrieval Augmented Generation](https://arxiv.org/abs/2509.21237v1)

精确v1/原5与联合Sep26日门沿R50；作者62→R59有限必要通过。每chunk合成QA、cos筛选、QA语义邻接加source-membership，在线seed扩展后回原chunk；QA非事实、cos非faithfulness/图非逻辑，初始cap非总候选上限。同源Qwen72B生成/回答/judge、首500及同K非token匹配，null/切片反退、temperature/模型尺寸/k-n文字冲突及全部制备/更新/在线费用保。作者69原三项经R64整体纯PRE及本轮fresh新授，73真实保存Ch76 AudioBoost完整组后/02377前并完整自读，R68唯一actualPOST通过，I13生效/窄位释放；只采用QA-node经membership回原chunk的消费粒度，不授QA事实或全图正确。见[§62/69](../_sources/daily-20250927/REPAIR_20261025.md)。

### [Tree Search for LLM Agent Reinforcement Learning](https://arxiv.org/abs/2509.21240v1)

精确v1/原6及Sep26日门保持；作者79→R74必要通过。forest共享前缀/agentstep扩展产生相关叶，intra/inter归一合并不认证过程真值；E4成本漏M/变长与二路径总概率1假设不推广实际clip/std/KL，only-intra崩与同预算/质量未闭保。作者92→R83具体NC12：Ch33固定prefix+可重放环境的分叉、局部与全局baseline坐标、ancestry/有效权重、KV与wall预算已具体承载。所有搜索/重复叶/训练/回归费用保，Book0。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2509.21243v1)

精确v1/原2+2+2=6及Sep26日门保持；作者83→R76必要通过。新learned-query MHA把全部patch压成两summary并拼入最终action crossattention，不是免费复用既成register；scalar g非输入动态gate，零K/V仍占softmax分母，不能证明关支。两token/训练peak共变、实机Stack80→76、表文增量差与聚合/训练/闭环全费保。作者94→R85具体NC14：Ch26辅助tokens投影/语义共同action消费、descriptor瓶颈与normalizer竞争已具体承载，Book0；日志“原5”仅转写纠正，不改原6。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [It's Not You, It's Clipping: A Soft Trust-Region via Probability Smoothing for LLM RL](https://arxiv.org/abs/2509.21282v1)

精确v1/原5与联合Sep26日门沿R50；作者68→R63一次有限必要采用。tildeπ=(1−α)πθ+απold的TV收缩/相对KL凸性界合法，但不约束实际πθ固定小半径；β0固定old/advantage时仅常数梯度缩放，AdamW也不私认固定LR等价。二元old稀有概率趋0使tildeKL无界，故中心实际trust保证D7，不否局部经验/降分。Qwen.5/1.5B有限数学、reuse/LR/调参共变，noclip多格胜出、CI相交非等价，同源reasoningjudge非truth，全部采样/训练/选择/回归费用保。强更新/无KL稳定不入Books，重开需非平凡实际policy/优化与rollout一致的trust条件和匹配质量全费；见[§68](../_sources/daily-20250927/REPAIR_20261025.md)。

### [SD3.5-Flash: Distribution-Guided Distillation of Generative Flows](https://arxiv.org/abs/2509.21318v1)

精确v1/原6及Sep26日门保持；作者84→R78必要通过。学生轨迹少数时刻直接供teacher/proxy读入，不是endpoint任意重加噪的同梯度保证；split-time分支训练再权重插值为单部署模型，不是运行多expert或函数无损。guidance/GAN印式未闭、8B synthetic源、GenEval选比、FID/2step反退、8bit更慢和移T5质量下降均保，全训练/teacher/proxy/部署转换费计入。root首owner→作者99实际回Ch24完整论点采用，两独立选择有小gap，原段经R90整体PRE/本轮fresh新授后102真实保存/完整自读，R93唯一actualPOST通过，I18生效/位释放。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

### [RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards](https://arxiv.org/abs/2509.21319v1)

精确v1/原6及联合Sep26日门经65→R60校准，S2025-09-25T16:19:06Z与2025L/Sep26T00Z、同DOI/arxiv.content/findable U/Sep26T01:57:46.000Z整个区间同BJT Sep26。作者86→R80有限必要一次采用：从人类feedback抽原则/支持片段/yes-no标签，原则条件scalar或生成式RM再供actor消费；RapidFuzz/共识非faithfulness，partial/分歧过滤改变人口，logodds非truth/校准。GenRM reward符号/缺token惩罚、macro/micro与judge协议/局部BT反侧保，T6为8H100节点小时非GPUhours，全部筛选/人审/RM/actor/调参费用保。Ch31可换原则的二判训练接口小gap原三项98经R88整体PRE/本轮fresh新授后100真实保存/完整自读，R91唯一actualPOST通过，I16生效/位释放。SciReasoner21320仅完整题摘明确AI for Science范围外，不评分/追无影响日期。 详见[本日证据与处置](../_sources/daily-20250927/REPAIR_20261025.md)。

## 5. 缺口与下一步

无普通可执行研究、日期、owner、待写/POST或在途。42项已按18整合/16具体已有覆盖/1仅报告/7中心争议逐项处置；Helmholtz R94完整DAY已通过，作者据此完成态真实保存/自读；Helmholtz R95唯一FINAL已通过，本日闭合，无剩余执行或验收步骤；保留下述终态边界，不另开研究债。

本窗终态保留项：下述历史来源限制与七项中心强主张争议被明确隔离；隔离部分不用于正面证据、Books采用或无遗漏断言，也不授性能/安全保证。定点重开条件分别按具名原事件/有限历史目录，或各对应§4所列一致公式、证明桥梁与匹配对照/完整费用执行。

中心争议不作外部访问故障：20577路由复杂度、21009完成时间选择偏差、20677谱proxy到ICL分布稳定、20744跨模型因果/总费、20721合法谱与risk指数、20863采样测度/打印目标、21282混合KL到实际policy trust共七项，均保候选/原分/局部正侧而隔离强采用。具体反证和可接受重开条件各见§4对应原件；无待取得未读材料被伪装成终态。

已隔离的外部来源限制见§2：Google Publications、Meta、Hunyuan、Z.ai、MiniMax Agent的2025历史切片不完整，只支持实际查到的目录范围，不支持零事件/全覆盖或无遗漏。具名原事件或有限历史目录到达时，只恢复相应来源/身份，不重已有效机构层或全年目录。

22343当前版本官方撤回，不能仅补日期即恢复采用；需明确恢复/纠正的精确版本及受影响结论。22211后来架构变化不反投2025v1；Chimera联合界已明确其arXiv公告为BJT Sep29，Sep26 Upload只是提交、Sep27代码不迁日。原必要准备与旧日期/作者出口记录保留，不混成本日正面证据。

旧33/113保留身份与有效已读层，只作偏后提交代理的路由，不作为本轮全量AB/日门/Methods队列。原缓存提交范围均已晚于Sep25纽约14时，按适用2025日程最早可能arXiv公告不早于BJT Sep29；这不提供各项实际公告日或全球首次公开，也不关闭学术贡献。已有六具名作者出口、Chimera Upload/代码角色判断复用，没有已取得未读的Sep26原研究发布页；不为排除所有假想早稿重开全池。A*原S Sep26T17:51:26同理不属Sep26的arXiv公告，潜力与具名早稿线索仅留真实归属恢复。具体范围见[本轮停止§58](../_sources/daily-20250927/REPAIR_20261025.md)、[旧日期包](../_sources/daily-20250927/SUP_DATE_20261013.md)与[旧分层](../_sources/daily-20250927/NARROW12_SCREENING.md)。22526科学应用范围暂缓理由保持。

tool-output仅采用冻结原发布事实；未取得完整2025 schema不阻塞这一4分处置，若要主张当时具体兼容性/实现，才恢复精确官方文档或release artifact。不借当前文档倒填。

## 6. 复核

复核者：Helmholtz（R94完整DAY及R95唯一FINAL，01a16737-3510-7e20-ae82-0dc7308a5f2b）；root容量交接记录仅为协调说明，非额外验收。

结论：通过

[R94完整DAY](../_sources/daily-20250927/REPAIR_REVIEW_20261025.md)已实际顺读全六节，核来源主题/Boolean/词形与别名、实际分页/停止点、具名日期准入/必要与最终Books处置、分层排除抽检及终态保留。42家族＝18实际整合（含旧TEQUILA有效POST）/16具体已有覆盖/1仅报告/7中心争议，全部最低层及处置闭合；本轮17项实际写后及最后R91–93唯一POST均通过，窄位全释放，无普通研究/日期/owner/待写/POST或在途。

分层排除复核不冒全量：旧Feynman SUP_INDEPENDENT §19有效抽检为新普通R/O题摘3/3、旧20关闭首四+尾五9/20及AARP核心，另11不称本轮全重读；新增20447/PINN、20615/LatentTwins与21320科学应用排除和22343撤回/22211后版变化/Chimera日期风险按具名实际层核。宽标题余量未读且非排除队列；未见共同错误理由须扩查受影响集合。五机构历史限制与七中心争议不获正面Coverage/Evidence或Books采用，精确重开条件保留在§5和各证据段。

原三行/小时窗/连续旧§4、42个exact标题与URL证据绑定及本地引用实际检查通过；V3与限定working diffcheck通过只证明接口/格式。日级语义依据为Helmholtz R94；作者104完成态真实保存/全六节自读后，[Helmholtz R95唯一FINAL](../_sources/daily-20250927/REPAIR_REVIEW_20261025.md)已实际通过。root容量交接记录已澄清为协调说明，不新增验收或重复计日；本尾仅纠正最终pointer，不追加第三核验，不改index/State或他日，未核代码/运行复现或生产保证。
