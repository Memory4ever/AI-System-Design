# Jun11 补查必要证据与单篇交接

作者supp_jun11；目标增补窗2026-06-10自然日。root完成canonical独核§1–14后，唯一余项与DAY写权已交非writer jun11_review；实际准入/必要/PRE/窄授/POST以同日SUP_REVIEW_20261026.md为准，root不第三Methods。本文件保留单篇准备时原唯一稿与历史“待”用语，不是自签；42项现37实际I/2具体NC/3中心H，候选普通必要/Books待办0，37指定窄位全已实际POST释放，非writer唯一DAY§101已实际通过；本句仅行政同步，不增加第二审阅。

## A1 MiMo Code: Scaling Coding Agents to Long-Horizon Tasks

原件：https://mimo.xiaomi.com/blog/mimo-code-long-horizon ；官方正文日期June 10, 2026。当前原件可读server-rendered正文；入口官方首页Paper/Blog。不存在必要正文访问阻塞。轻查未见withdraw/correction标记。精确事件是厂商工程说明，不以GitHub更新时间代替发布日期；正文含工具语法“尚未迁移”的未来态，未冒充全部设计已上线。

### 准入与必要证据

原有约束：长coding会话把临界满窗才压缩、让主执行器同时维护笔记；新增可核机制是独立writer在低于满窗的多个检查点提前增量抽取，保持single-writer的结构记录，再于rebuild时装配当前工作集。需要重新考虑压缩是否只能是预算耗尽时的单次操作、以及“谁负责生成状态视图”和“谁拥有最终替换权”是否能混同。拟2+2+2=6；为具体现owner差额读到必要机制、评价和直接反侧后停止，不扫描无关安装或代码提交。

已实际读取§1动机、§2.1–2.4、§3.1–3.5、§4.1–4.2、§5.1–5.2及各NOTE：

- §3.1：主循环继续时后台writer生成结构状态；新窗口rebuild从持久文件重建。逻辑会话跨多个cycle，物理窗口仍有界。
- §3.2：抽取自身也需要剩余空间，且高利用率下抽取质量可能下降；公开触发点约20%、45%、70%，各次增量更新，最后rebuild不是一次临界救急。本文没有阈值敏感性/独立抽取质量对照，不能把这些比例写成普遍最优。
- §3.3–3.5：独立writer整理11类字段，每结构文件仅一个writer；执行器只读结构状态，notes为例外写通道；恢复注入任务、checkpoint、部分用户原文、project/global memory、notes与索引。历史SQLite原文可回读。single-writer只约束写竞争，不等价最新tail或未投递输入已原子纳入；本文未给正式snapshot/compare-and-commit证明。
- §2：Max Mode默认5候选，judge后仅执行一条，作者称约4–5倍token成本；Goal独立模型检查终止条件，误阻比误放常见，环境测试失败是一个来源；constrained CLI语法明确尚未迁移，不能把该节计划写成实现验收。Dynamic Workflow用脚本和持久每次agent结果来管理编排，已有Ch81确定性主干，不另立owner。
- §4：7天Dream、30天Distill是厂商给定维护策略，不是本研究证明的最优周期；持久化、检索、全历史、维护和独立writer/verification均计费。
- §5.1：作者自己限定标准单issue benchmark无法充分衡量其多轮memory/goal/cross-session目标；不能据组合系统分数唯一归因writer。
- §5.2：576开发者、474私有仓库、1213个有明确胜负的A/B pairs，相同target model对比harness；≤200步接近50%，>200步作者称>65%。人口依赖已产生执行步数、排除无明确胜负样本、同一开发者/仓库相关和未知置信区间均限制因果/泛化；不同组件一起变，不证明提前writer独立收益。未披露生产硬件/精度/并发/SLO，未复现或核实现。

### 当前owner实际比较

已完整读PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE；ROADMAP AGENT-CONTEXT=Ch75。实际Ch75 §“原文是事实状态，摘要只是可替换的派生视图”已有immutable history/raw fallback，§“Compaction从Blocking Rewrite演进为带Commit的后台状态转换”第一完整段已有snapshot watermark→background proposal→fidelity check→compare-and-commit，第二完整段已有双份Context/取消重做/版本冲突费用，第三完整段已有Qwen durable commit和MiMo PR2702最新tail/deferred input修复。Ch74/76交接与Ch77开头已读；Ch81 Deterministic Spine已有required gates/terminal criteria分责。

现有段落拥有后台commit与恢复安全边界，但没有把“提前分段抽取”与“临界满窗提交”分成两个预算时点；本项拟补且仅补这一小层。若root认为其没有新增长期差额，可改具体已有覆盖，不为制造diff写书。

### 唯一字面稿PRE（待root核必要证据/现owner/逐字与窄授）

owner：`books/part-07-agent/75-context.md`，上述Compaction小节第一完整段后、原第二段“并行化能隐藏一部分压缩延迟”前插一自然段；不改直接两侧。

抽取与提交还可以使用不同的预算时点：由独立writer在窗口尚有余量时多次增量整理任务、约束、未决动作和原文引用，到真正换窗时再组装这些状态，而不是等满窗才同时做理解、压缩与恢复。[一份长任务coding runtime说明](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)给出这种前移分支；每文件single-writer可减少写竞争，却不证明后台视图覆盖最新tail，更不能代替上文的base revision与提交检查。提前writer、持久文件与回读原文增加后台计算、存储和失效维护，抽取不完整时仍需同步补齐或保留原历史。作者同模型harness A/B没有隔离writer，固定触发比例也未经独立最优性验证，不能从长任务组合胜率推出该机制净收益或任意长会话无损。<!-- source-family:SF-2026-MIMO-CODE-LONG-HORIZON -->

本人Review note唯一稿：

- `SF-2026-MIMO-CODE-LONG-HORIZON` — Daily2026-06-11补Jun10；[官方工程说明](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)§3.1–3.5/§5及§2 NOTE，2+2+2=6。只补提前多次writer抽取与后续rebuild提交的预算分工，不采固定比例最优、single-writer即原子最新或harness组合收益唯一归因；语法迁移仍计划态、全费用/原文回退保留。未核代码/复现，root必要Source/现owner/逐字PRE与实际POST均未预签。

## A2 Piper: A Programmable Distributed Training System — 2606.11169v1

精确原件：https://arxiv.org/html/2606.11169v1 。完整题摘与日期见SUP_ADMISSION本项；拟2+2+2=6。已实际读§3 challenges、§4.1 API（IR/placement、Replicate/Shard/Split/Order）、§4.2 compiler、§4.3 centralized/worker/stream/communication/memory、§5、§6.1–6.4。以下只采用“并行策略声明可以编译为显式计算/通信依赖计划，runtime不需逐策略重写”的条件分支，不冒称任意并行已自动支持。

### 必要证据与直接反侧

- §4.1–4.2：模型annotation形成Chunk；Place/Replicate/Shard插入P2P或collective，Split复制microbatch子图，Order追加时序边。统一global DAG同时表达model data dependency与user temporal dependency，每Chunk/Comm带device/stream。编译形成每设备计划，runtime保留依赖而非预设每并行维度独立。
- §4.1有具体边界：Shard当前只沿dim0且要求前后与Replicate布局相配；任意GSPMD式组合是future work；每model-state bucket仅允许同placement chunks，tied embeddings跨placement尚未实现。Split/Order依赖contiguous sub-DAG。不是“所有合法策略都可直接编译”。
- §4.3.1：ready任务按downstream dependency数量启发式选择，不是最短路径/全局最优。对非critical子图很多小task、critical/noncritical通信共stream等会差；§4.1还承认可能调度阻塞critical path的allreduce。
- §4.3.2：跨stream消费者等CUDA event，通信组各rank必须保持一致collective次序。P2P send/receive分stream且每stream有独立communicator，把约束缩成每方向顺序；下游需按上游microbatch产出次序消费，不满足者当前reject。buffer最后consumer完成事件与调度/释放分开。并行计划不是共享资源无竞争保证。
- §5要求模型fully traceable；TorchDynamo混合eager虽存在，但本系统不由此支持任意dynamic graph。runtime用Ray，未实际运行artifact。
- §6：4个AWS EC2节点、每节点8A100，节点内NVLink、节点间EFA；比较Megatron-LM0.18.0/DeepSpeed0.18.9/TorchTitan0.2.2，Qwen3 1B/9B、PP/DP/EP不同配置，不能合为单个通用吞吐数字。精度/SLO未在必要段明确，Not Disclosed，不用于数字采用。
- §6.1：Megatron需要PP外层，所以作者把节点内流量route至PCIe来模拟低带宽，这是非同物理placement对照；Megatron融合kernel单microbatch约30ms、Piper约40ms，不能归因为编译IR唯一收益。
- §6.2：Piper每backward重约梯度减少驻留，但额外通信；TorchTitan少reshard节省通信却占更多内存，因此batch可容纳差异不是免费收益。Table2简单DP ZeRO1 throughput Piper8641、TT8637、DeepSpeed9352、Megatron9942，Piper不总最快。文中一处把ZeRO2误写parameter sharding，不沿用该标签错误，采用其显式gradient/weight lifetime说明。
- §6.3：DualPipeV共用有限Qwen配置，有TT OOM、kernel实现差异和线程同步替代解释；§6.4随PP/DP线性扩大global batch，是weak scaling，不证明fixed-batch强缩放、长期收敛或生产容错。

### 当前owner与唯一PRE

已读Ch36§“并行策略怎样消费通信原语”及Ch36§“从手写Plan到可校准的并行规划器”全部（含下方直接跨Phase开头），Ch35/37交接。现owner拥有planner proposal/runtime admission与profile校准，不含把用户策略变换显式编译成统一计算/通信DAG及communicator顺序限制的具体中间接口。唯一owner `TRAIN-DISTRIBUTED-TRAINING`；不去Ch38重复DualPipe或Ch39重复ZeRO机制。

唯一插点：Ch36“从手写 Plan 到可校准的并行规划器”最后完整段“自动搜索获得的是更大的设计空间覆盖……只拥有这些机制如何被组合、验证和回退。”后、下一标题“从Phase串行到依赖驱动的跨Phase重排”前。原直接两侧不改。

规划器与执行器之间还可使用显式计算/通信图，而不是为每组并行旋钮另写runtime：从模型注解取得可调度chunk，用placement、replication、sharding和microbatch/order指令改写同一全局DAG，再编译每设备的stream与依赖计划。[一份可编程训练系统的受限实现](https://arxiv.org/html/2606.11169v1#S4)展示这种接口；数据依赖、跨stream完成和通信组内一致次序仍须保留，增加stream不能取消collective顺序。原实现只接纳可完整trace的模型、限定sharding组合与符合上游产出次序的pipeline，不授任意动态图或全策略自动正确；启发式调度也可能把非关键通信放到关键路径。图编译、CPU dispatch、communicator、临时buffer与更频繁reshard全计费，省驻留可能增加通信。有限Qwen/A100对照的拓扑模拟、kernel差异和扩batch缩放不证明普遍净吞吐或收敛等价；图/次序不可验证或收益不足时，已验静态plan和手调runtime仍合理。<!-- source-family:SF-2026-ARXIV-2606-11169 -->

本人note唯一稿：

- `SF-2026-ARXIV-2606-11169` — Daily2026-06-11补Jun10；Piper [exact-v1](https://arxiv.org/html/2606.11169v1)§3–6必要机制/主对照/直接反侧，2+2+2=6。只策略指令→统一compute/communication DAG→每设备计划接口，保fully-traceable/限定shard与P2P顺序、启发式失败/所有费用；PCIe模拟、kernel差额与weak scaling不授任意策略正确/全局最优/生产收敛。未核代码/复现；root必要Source/现owner/逐字PRE和实际POST均未预签。

## A3 DiffusionGemma — June10官方发布/开发说明

原件：[发布](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)、[开发说明](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/)，两者均官方June10 2026，未以HF createdAt当公开日。当前model card `google/diffusiongemma-26B-A4B-it` SHA `f7f5b7f5fa82ffc52addd066915886d497f5517b`（API lastModified July15）已读ModelOverview/Benchmark/CoreCapabilities/BestPractices/Limitations，仅作当前补充，不冒称June10历史逐字卡。采用的长期命题直接由有日期发布与开发说明支持，不依赖July新增字段。轻查两官方页及卡未见withdraw/correction；不下载权重或运行服务。

准入：单用户AR decode常受参数搬运限制→新公开26B MoE/3.8B active模型用256-token uniform discrete canvas、因果prefill与块内双向refinement，明确以低并发吞吐/较低质量换路线→需把“请求batch已摊参数读取”作为block diffusion净收益边界，不从新模型名或4x宣传准入。拟2+1+2=5；涉及Ch24具体条件缺层需读足必要证据。

### 必要机制、评价与反侧（已实际读）

- 发布§Why diffusion/Trade-off：相对单用户AR，整块并行增加每次参数读取的工作；高QPS下AR已有跨请求batch，diffusion并行decode收益递减、可能成本更高；低compute-to-bandwidth的统一内存设备不保证同等加速。发布明确质量低于标准Gemma4，后者仍适合最高质量生产，不把替代分支写成全局升级。
- 开发说明§Architecture/BlockAutoregressiveDenoising：初始prompt causal prefill，256-token canvas块内bidirectional反复去噪，整块完成后再由causal encoder重算并追加KV，再生成下一块。不能把临时双向KV直接当稳定历史；该commit解释在现Ch24已有，不另重复。
- 开发说明Sudoku：base约0%、SFT后80%、示例48步vs12步，训练/任务改变，不证明通用self-correction或sampler早停因果；不采用这组数字进入Books。
- 发布singleH100/RTX5090的TPS与4x没有完整输入/输出长、batch精确值、重复运行或SLO；只保其低并发设计范围，不复述为同质量端到端实测结论。模型card当前H100/FP8/lowbatch与质量表亦是作者证据；AIME69.1<88.3、LiveCodeBench69.1<77.1、MRCR32<44.1表明质量不等价，HLE no tools反向更好也不消除其他维度差额。没有合并不同sampler/precision协议。
- 当前card BestPractices给entropy-bound选择、非选token全renoise、平均entropy与连续两步argmax稳定双条件早停；这些是model-dependent计算停止而非事实verifier。由于card是July current，本窗不主张阈值已是June10原样，也不把它写进本次长期稿。
- 代价：反复去噪、全canvas活跃计算、causal KV重算/commit、workspace/cache、prompt视觉编码、训练适配、调度及任务质量回归。没有生产并发/SLO或完整预算证明。

### 实际owner与唯一字面稿

已读Ch24“Block Diffusion：局部自回归与块内并行”完整主干及cache/causal重算分支（1578–1642）、UniformCorruption目标段（1097–1105）、统一成本模型/ParallelProgress（1889–1939）和Ch23/25开头交接。owner唯一 `MULTIMODAL-GENERATIVE-PARADIGMS`；现正文拥有block内/间、临时KV/稳定KV、NFE与active compute分账，不重复。具体未明说的差额是：跨token并行与已有跨请求batch会竞争同一算术强度收益，且hardware compute/bandwidth比改变适用范围。

唯一插点：Ch24 `### Parallel Progress 与 Active Compute 是两条独立成本轴`第一完整段“Block denoising每次参数读取……状态管理。”后、下一段“一次去噪求值的活跃计算也可以沿网络深度分配”前；原两侧不改。

跨token并行还应与服务已有的跨请求batch一起比较：低并发、单用户AR的参数读取尚未摊薄时，canvas可以用更多活跃位置换算术强度；高QPS已经把AR批量计算填满后，同一refinement反而可能增加费用，而低compute-to-bandwidth设备也未必获得相同收益。[DiffusionGemma的官方发布与开发说明](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/)展示这种低并发分支，仍需块内反复去噪、完成后causal重算KV再提交，且发布明确承认相对AR的质量取舍。模型求值、cache刷新和质量回归都计费，局部TPS或更少串行步不能代替同质量、同batch及同硬件的端到端验收；高并发、严格质量或预算不合时，原AR或更保守块宽继续合理。<!-- source-family:SF-2026-GOOGLE-DIFFUSIONGEMMA -->

本人note唯一稿：

- `SF-2026-GOOGLE-DIFFUSIONGEMMA` — Daily2026-06-11补Jun10；[官方发布](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)及[开发说明](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/)Jun10，2+1+2=5；只跨token/跨request batch算术强度分工与硬件比值适用界，保质量下降、反复去噪/cleanKV重算和全费，不采4x/TPS为等质量SLO。July current card SHA f7f5b7f5fa82ffc52addd066915886d497f5517b仅补证、不当June10历史卡；未核代码/复现。root必要Source/actual owner/PRE与POST未预签。

## A4 The Role of Feedback Alignment in Self-Distillation — 2606.11173v1

[精确HTML](https://arxiv.org/html/2606.11173v1)，2+1+2=5，首批AB/date已root§1通过。已实际必要读§2 Eq3–4、§3.1–3.2、§4.1–4.3/Fig3–7与§6限制，Appendix A.1 prompt在§4.3可决定的规则已清楚，不为完整prompt/代码再扩。只采用“保正确prefix的逐字锚点、不给错误step同样锚点”的受限反馈结构差额，不采用induction-head因果或完整梯度无偏结论。

### 必要证据与限制

- §3：student onpolicy rollout；固定初始base policy禁LoRA作selfteacher，只有student更新。RefSol用参考解作teacher context；StepAlignFB额外用QwQ32B critic读取同一学生轨迹+reference，复制正确步骤，只修错误/未完成部分。二者不是给student直接模仿critic新整条轨迹。
- §2 Eq4/Fig3–7：带feedback与不带feedback的同prefix token logprob差可局部改变更新信号；完整引用错误原attempt再附纠错时，错token仍被copy anchor强化；只说correct不复制正确token时，teacher也会对原正确表述给负差；保留正确prefix并在首错处停止逐字复制是paper实际观察的有效prompt条件。
- 论文把这种现象解释为induction-head copying，但没有head-level干预，故只保conditional logratio/readout现象，不把attention因果已证。Eq3D方向/§3.2forward KL措辞与Eq4类policygradient说明不直接拼成无偏实现。
- §3.2：Qwen3-1.7B solver，QwQ32B frozen critic，4H100、bf16、LoRAr64/alpha128，OpenMathReasoning经72B passrate、1.7B难度/format过滤后仅312题，282训练/30评；rollout上限2048、最多7epoch。先筛critic可解/student困难问题，结论不涵盖任意错误密度或critic不会题目。
- §4.1：Avg/Majority/Pass@12每metric分别从steps10–70挑最好checkpoint，并非一份固定模型的统一成绩；同30题反复选点，不能当独立finaltest。GRPO G8与SD G1“matched generation compute”不含critic/teacher全费用与相同prompt曝光，在此不采用16.11点为完整同预算增益。
- §6：高质量critic提高成本与复杂度，reference可跨训练复用，rollout-specific critique每次重算；单dataset/solver–critic配对，token长度也增加。所有critic生成、selfteacher评分、rollout与训练/选点均计费。未核artifact或复现。

### Actual owner与唯一PRE

已读Ch29§“Rollout-conditioned Distillation应按证据归因”完整段、§“PrivilegedTeacherEvidence必须做差分验证”完整各分支、§“ContextDistillation”至teacherstate段及Ch28/30开头交接。现owner拥有reference差分、反馈条件teacher/无反馈student、错误suffix与trajectory分工，没有写“同一反馈中哪些原token应逐字复制”的双反例；不在Ch31重复一般processreward。

唯一插点：Ch29 ContextDistillation概念段“这与让teacher另写一条……不能只用distillation一个名称代替训练合同。”后、下一“如果目标改成从rawdocuments更新参数知识”前；原两侧不改。

反馈本身怎样复述student，也会改变这份同prefix监督。一个受限数学自蒸馏对照让critic逐字保留正确步骤，在首个错误处改写而不再复制错token：完整照引错误attempt再附纠正，可能继续强化原错误；仅说“这步正确”却省略原表述，也可能让teacher因偏好另一解法而压低本来正确的token。因而反馈是否正确、是否对齐轨迹与逐字锚点放在哪里应分开验收，不从正负logprob差自签步骤真值或induction-head因果。[该局部证据](https://arxiv.org/html/2606.11173v1#S4.SS3)只来自经难度/格式筛选的小数学集与固定solver–critic，逐指标挑选checkpoint也不是独立最终测试；critic、teacher评分与更长轨迹全计费。反馈不可核、错误太早或额外费用不合时，可靠reference、普通蒸馏与外部verifier仍是退路，不把对齐格式作为普遍优于整解或GRPO的保证。<!-- source-family:SF-2026-ARXIV-2606-11173 -->

本人note唯一稿：

- `SF-2026-ARXIV-2606-11173` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11173v1)§2–4/F3–7/§6必要，2+1+2=5。只反馈逐字锚点保正确prefix/不复述错step的受限差额；保30题/反复checkpoint选优、G8/G1与全critic费用、single配对、gradient措辞与induction仅假设，不授无偏过程credit/真值或同全预算优势。未核代码/复现，root必要Source/actualowner/PRE与POST未预签。

## A5 Full-Duplex Speech Interactivity — 2606.11167v1（具体已有覆盖提案）

[精确HTML](https://arxiv.org/html/2606.11167v1)；root§8/9已校准2+1+2=5，准入仅因为受限负面证据，不是四轴reward加总。actual必要读§3.3–3.4、§4.1–4.3、§5.1–5.3/T2–3、Limitations、D2，支持与直接反侧足够，不读完整语音生成recipe或发布模型代码。

### 保留命题

即使训练reward同时含交互时序和文本相关性/自然度，所用会话语料与共同优化仍可损失未被judge实际覆盖的行为维度；需要分别验交互quality、文本quality与Safety-task行为。不能把快响应或合作backchannel当安全保持证据。

- §3.4/4.3：pause/turn/backchannel/interruption规则reward之外，仅对turn/interruption加ASR转录→Qwen3-235B judge的relevance/naturalness分数，并分别归一化再合优势。这不是安全reward；语音时间由并行textstream间接控制，不覆盖没有textstream的full-duplex模型。
- §4：Moshi/PersonaPlex两个同类模型，Fisher或Seamless两种数据；每轴至多2000 segments；100epoch、每epoch32segments、G16、32H100，β.01；prefixcontext从0渐增30s。不是固定相同语言内容/recording分布的纯风格干预，数据量、风格、条件多变，不作单因果归因。
- §5.2/T2：PersonaPlex Fisher的Safety instruction3.596→3.288/task3.260→3.000，turnfluency3.841→3.695；Seamless未呈同样反退。D2展示Fisher后输出短碎的合作backchannels；base示例本来就未拒有害请求，故不能写“原安全模型被训练破坏”或估计真实伤害概率。作者将现象归于Fisher合作风格是合理解释，不是已隔离因果。
- §4.2/Limitations：Safety只是FullDuplexBenchv2自动examinerGPTRealtime、fastpacing≤60s及Gemini2.5Flash评分的一个任务族；没有真实人类交互验证。v1Backchannel脚本曾有generatedaudio未resample到16kHz的bug，作者修后重评，旧引用分数不可混比；v1/v2分开。§5.3另有pause/turn相反代价与去LLMjudge大退，不能据加judge声称解决所有安全。
- 所有ASR、judge、RLrollout、前置context、GPU训练和独立安全评估均计费，未披露完整precision/seed置信区间和生产SLO，未核artifact/复现。

### Actual owner与NC

已实际读Ch31§“多目标Reward的Bottleneck聚合不能冒充HardConstraint”完整前两段、§“Evaluation必须独立于RewardModel”完整人口列表及其后“把多个reward组成ensemble，也不自动补齐未被任何判据覆盖的质量维度”完整段，邻近前后完整（包括后方2606.06976决策/置信反向段）。现正文明确要求分验refusal/style/capability/safety，且明确ensemble多个channel不能为未覆盖维度背书；比本研究的一种speech局部实例更一般且边界一致。该负面观察提供新的受限佐证，不改变owner内的现有具体判断，不为凑diff追加speech特例段。

Books提案：**已有覆盖** — `TRAIN-RLHF` / `books/part-04-training-system/31-rlhf.md`，真实正文`Evaluation必须独立于RewardModel`下ensemble盲区段。无Books写入/本人注，不预签root必要证据/NC或日级。

## A6 PiSO — 2606.10890v1（中心精确最优性争议，安全终态）

[精确HTML](https://arxiv.org/html/2606.10890v1)；准入2+1+3=6保留，不因中心证明冲突删池或降分。实际必要读§2、§3.1–3.3、§4主表、Appendix C.10受影响证明；未核代码或复现。当前v2为Oct16修订，current摘要措辞已变；不以其数字或修改内容回填Jun10 v1，也不据此推定作者已经承认下述错误。

### 可支持机制及直接反侧

固定有限RTN grid下，单channel的scale改变归属仅发生于有限breakpoints，区间内部的输出重建误差为凸二次式，可枚举闭包最小值并增量维护alpha/beta/Hq；一般每channel O(D²|grid|)，对角近似以丢失交互精度换较低开销。该受限机制不等全网络最优。§3.2独立分组忽略cross-group项，sequential仅贪心考虑先前误差；GPTQ/Qronos的误差补偿改变RTN归属，§3.3 interleave不是联合全局最优。限制BF16自由scale，不直接覆盖MX/NVFP4受限scale。

§4校准128×2048 WikiText2训练片段，WT2 validation PPL与ARC-Easy/Challenge/HellaSwag LightEval，Llama3与Qwen2.5 instruct、W2/W3/W4。低bit RTN仍可严重失真；decoupled PiSO+Qronos有反退（例如Llama1B PPL197→216、3B68.9→84.8、8B49.5→76.0），不能照抄consistent普遍改善。训练/校准时间、H/G统计及存储和后续真实低bit kernel执行分开，论文不是端到端服务复现。

### 中心反例及必须保留的版本纠正

原件位置：[§2 notation](https://arxiv.org/html/2606.10890v1#S2.SS0.SSS0.Px1)规定RTN ties **rounding up**，X为高精度输入、tildeX为部分量化模型输入；[§3.1 Eq5–7](https://arxiv.org/html/2606.10890v1#S3.SS1)明确允许cross-activation X≠tildeX。[C.10](https://arxiv.org/html/2606.10890v1#A3.Thmtheorem10)从各半开区间的infimum推进到全局infimum必能attain；其Case2只得inf≤相邻闭包最小≤E(boundary)，又用E(boundary)≥inf声称三者全等，缺少反向界。证明自己也明确边界处E与原piece的phi可能不同。

作者的数学反例（本次分析，不冒称论文实验）：取scalar w=-1，grid={-1,0,1}，X=3，tildeX=1，遵照原文ties-up。0<s<2时q=-1，E(s)=(-3+s)²；s≥2时q=0，E(s)=9。在s=2，w/s=-1/2，ties-up取0；全局infimum为1但不attain，闭包clamp到2的原piece值1并非实际RTN误差9。参数满足原文有限grid/正scale/cross-activation定义，足以直接质疑“精确全局最优scale必存在/闭包clamp即取得”的无条件命题；不否定区间内部二次结构或实测数据。此前私信的正w+ties-even草例不符合原文tie定义，已明确撤回并用本负w例替代，不作为有效证据。

root§14已实际独立核notation/Eq2/§3.1/C10整proof及C9前提：w可为任意非零实数，负w反例合法；C9只要求positive transitions distinct，本例唯一正breakpoint2亦满足。修正反例与中心精确attainment证明缺口通过，候选仍6、中心争议/Books暂缓；不采用exact-global、不写泛warning，也不据此否认区间内部二次结构或所有实测数据。可接受重开材料为精确v1条件补充/有效边界处理证明或明确采用修订事件的真实日期，不能用current v2摘要消除v1问题。已读Ch49校准粒度与PTQ/QAT、未来补偿邻接，仅作owner定位，无Books写入。

## A7 ReasonAlloc — 2606.11164v1（具体已有覆盖提案）

[精确v1](https://arxiv.org/html/2606.11164v1)，root首批准入5分（2+1+2），不是因hierarchy命名或收益数字。实际读§4 demand定义/三模型与跨任务范围、§5全部必要分配、§6–8主结果/效率/消融、Appendix C fallback与I校准/随机性；不读无关case study或实现仓库。

机制：固定R-KV重要性/冗余score，离线≤8 AIME-style prompts的attention-mass demand给每层预算；在线每128 decode tokens在层内pool head-token scores、取全层kth threshold、按各head超过阈值条数提议容量，再用power/clip/归一化平滑，交原selector淘汰。layer分配与head分配/选择器分开，但不是所有scorer/attention kernel已验证兼容。原文只在少数R1 distill架构上观察layer需求相对task更稳定（跨架构distance .0503对跨task .0132），不将“architecture决定”或“deep layers负责holistic verification”升格因果事实。Appendix C所谓fully dynamic layer fallback实际只在本请求prefill估计，后续固定layer预算，不是每步decode重分层，也未见单列fallback效果。

对照与反侧：主准确率R1-Llama8B/R1-Qwen14B/AceReason14B，MATH500/AIME2024，temperature.6/top-p.95，每题8样本的pass@1，16k/32k输出cap、单decoding seed；准确率8×H20。直接比较同R-KV scorer的uniform与Pyramid-RKV有局部归因价值，不能把prefill SnapKV与动态方法差异全归budget。Table1 AIME layer-only在768/1024/1536/2048/3072预算低于uniform，full在2560低于layer-only（53.34/55），非所有组件/点单向胜出。超参数人工试一条AIME prompt，并非无调优或独立所有任务选参。

RTX4090/24GB吞吐在各方法可容纳的最大batch测，16k FullKV batch2/39.66TPS而压缩batch8/218.82TPS；5.52倍不是同batch同质量SLO。分配开销在一个HF/PyTorch attention-hook实现、每128步刷新可摊销，不支持任意GQA/head-ragged layout透明接入；precision未明确，未核artifact。离线探测、全head score与threshold、floor配置、实际compaction/metadata和质量回归都付费。

原式预算保护边界：§5.2 Eq1–3先clip再归一化并逐项floor，单凭该式不保证作者声称的exact sum或最终floor。作者分析反例为B10、n2、raw=(0,100)、power.5、clip[1.25,10]：clip后(1.25,10)，再缩放floor得(1,8)，sum9且首项小于1.25；实际实现若有余数/重投影修补须另核，本文没有据此宣称运行代码一定越cap或不安全。它进一步支持既有“proposal不等硬容量验收”，不采用原文strict conservation措辞。

Actual owner已读Ch45“Model-driven GC只能提出Eviction…”之后完整CoT→adaptive layer/head budget链、其后proxy/不可逆删除/metadata-fragmentation/layout及model-workload/budget/fallback段，以及“Multimodal KV选择必须区分Prefill key统计与Decode query需求”完整两段。前者已经承载同score下数量分配与选择的分责、动态head/layer及物理映射和质量回归；后者已明确prefill proxy不授权decode需求。也读EvolKV完整段：离线task-fitness预算不是未来充分性且hard cap另验；邻章44/46已有请求级decode/capacity职责。

Books提案：**已有覆盖** — `INFER-KV-CACHE`，Ch45上述完整CoT预算链及prefill/decode统计区别；本研究补同scorer受限实证但不改变原具体判断，有限model波形不另造“Reasoning Wave”长期定律。无新增正文/本人注，待root必要/actualowner/具体NC独核，不预完成。

## A8 Recoverable but Not Stationary — 2606.10929v1（唯一稿提案）

[精确v1](https://arxiv.org/html/2606.10929v1)，root B2已校准2+1+3=6。实际读§3定义与selection/report区别、§4局部定理特别4.3、§5.1–5.3全部主反侧、§6；深入仅固定低秩snapshot与恢复轨迹的差额，不采用新search/steering算法或所有定理。

核心：task plane定义为checkpoint处per-task minibatch梯度协方差top-r；恢复trajectory prefix则需要先真实运行若干恢复步。四层128维两head约0.5M synthetic Transformer，四digit任务copy/reverse/sort/mod-add，多任务20k→单任务10k遗忘→100步恢复，三seed。matched steps/step size下，每一步都投影回同一旧plane的恢复EM .10/.07，对full .30；同固定r的plane主角度overlap在100步从1降到.12–.17，是方向漂移而非rank增长。DistilGPT2 rank16 sort→mod-add、GPT2 rank8 reverse→sort两组各三seed，50步恢复，前10/20步span含最终displacement约77%/90%，旧local plane约15%、pre-interference<2%；完整轨迹span含最终位移是构造恒等式，不算新最优算法。恢复人口/适配任务仍很窄，不承诺大LLM一般遗忘/恢复比例。

§4.3固定Hessian二次loss的GD位移落Krylov span只为解释局部方向会转；非线性时H随步变化，不能把单H公式变完整Transformer恢复器。§4.1 Gaussian useful-projection在固定per-coordinate sigma下的维度无关，不等固定总扰动范数/固定曲率误差下无维度代价；拟稿不采用该旁命题。§5.3 billion-scale有效rank在Qwen3B/MLP能区别same-norm random-sketch control，但Qwen7B与control接近，不能把有限minibatch的rank上限当模型固有lowrank。搜索/steering只作反侧：14 lanes中structured胜matchedrandom仅9，OLMo BoolQ目标+1.2伴side mean−17；不采普遍无副作用或“无需标签”的表述。basis/梯度统计、真实恢复、搜索与新旧任务验证都有成本；precision、完整硬件/seed统计未披露部分记Not Disclosed，未核代码/运行。

Actual owner：`TRAIN-LORA`，Ch30当前167–173低维初始化→可训练basis→TLoRA冻结A的完整链及前后完整段，已实读；399–411多expert静态分离后梯度重新耦合链也已读。后者讨论expert间重新聚类，不能替代同一任务的初始/遗忘点局部plane并非整段恢复支集；前者已有漂移回退但缺上述snapshot/trajectory的具体判断。因此拟只在TLoRA完整段独立marker后、下一“冻结随机基座是另一种训练假设”标题前一段，不改原冻A结论或重复expert重分组。Ch29概念/Ch31交接已读，目标是适配更新空间，不另设owner。

### 唯一literal（待root必要/actualowner/PRE，未写Books）

一次checkpoint上的低秩梯度，也不等整段适配都落在同一张“任务平面”：冻结一次估计的basis时，应同时检查它是否仍覆盖后续恢复所需方向，而不只检查当时的谱能量。[受限synthetic Transformer对照](https://arxiv.org/html/2606.10929v1#S5)中，每步都投回同一旧plane明显弱于自由恢复，同固定rank的plane方向也随步漂移；GPT-2 LoRA的短轨迹span较好覆盖最终位移，但其受约束恢复中local plane也可接近自由更新，不能把最终位移投影率直接当约束训练上限。这不否定低秩更新，而是区分局部rank、固定更新支集与跨步轨迹。轨迹span必须先支付真实恢复与梯度观测，不是免费知道最终方向的算法；固定Hessian的Krylov解释也不覆盖任意非线性训练。大模型有限batch得到的低rank还可能与随机采样control无法区分，不能据小模型比例直接选部署rank。Basis准备、恢复、统计和独立新旧任务回归都计费；方向稳定且质量已验时，冻结basis仍更省状态，漂移或恢复不足时则重估、更宽/可训练basis、普通LoRA或full update，而不以单点低rank保证不遗忘。<!-- source-family:SF-2026-ARXIV-2606-10929 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10929` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10929v1)§3/4.3/5.1–5.3/6，2+1+3=6。只局部task plane≠跨步恢复支集，保小任务/固定r漂移/真实trajectory准备费用与Qwen7B sampling-control反侧，不采全局线性、免标签/免代价恢复、泛化遗忘比例。未核代码/复现；root必要/actualowner/PRE与实际POST待核，不预签。

jun11_review首备的必要补层已实际采用：Appendix C/T8，GPT2 LoRA local-plane受约束恢复finalEM .090对Full .098、gain .052/.060，确实接近；原§5.2也将此诊断与几何结论分开。作者无需第三次重复Methods/C，已把唯一稿“synthetic/GPT2同时明显弱”改为只synthetic，并近文保LoRA反侧；原初稿及修正缘由保留在版本diff，不删除直接反证。更新后唯一稿尚待reviewer实际PRE及root窄位授权，未写Books。

## A9 When to Align, When to Predict — 2606.11190v1（reviewer首备已实际采用）

[精确v1](https://arxiv.org/html/2606.11190v1)，2+2+3=7保留。作者先粗读§3/4，不拿未核公式做完整证据；jun11_review随后首备实际§3、§4.1–4.4、Appendix A1–A7/B非科学recipe/Algorithm1与C/Fig9，作者已实际采用其完整必要与反侧，只补owner/唯一稿，不第三遍Methods。§4.5科学应用不进入本次研究采用链。

可支持命题：固定瓶颈k、线性映射、block-diagonal spiked population下，CA对两侧协方差whiten后按cross-covariance谱取方向，CP仅source whiten；有用signal与correlated nuisance竞争各自目标下的前k方向。满signal恢复须最差信号谱值仍超最强nuisance；变target/source或target nuisance方差会改变两目标的相对选择，配对、较大共享相关或较低总重建MSE均不能认证任务signal。C/Fig9给CP总MSE更低而signal recovery更差的直接反侧。

必须同时保留：同质/固定窄瓶颈四相图不是任意非线性模型的普遍阈值。§4.2 nonlinear CP在nuisance完全相关ν1时可因瓶颈过宽同时编码signal+nuisance，绕过窄线性模型的失败预测；不能把这种偏离藏掉。A7 partial recovery只给at-least-r保证，r0不能仅凭下界推所有signal失败。COCO Appendix B的I→T用CE而非MSE，T→I用像素MSE，probe的source也分别image/text，不以约10pp归因纯方向，更非一般线性定理的完整验证。§4.4/Alg1诊断需要小量外部标签、5fold Ridge/elbow区分signal/nuisance，近spiked的独立冻结表征较合理，rawPCA proxy更不可靠；不是无监督数据自动分型。

实际owner：`MULTIMODAL-REPRESENTATION`。已读Ch23§“对齐不是把向量拉近这么简单”首centroid/pair段、后norm路径与控制完整相邻链，以及前“任务贡献与当前可靠性不能共用一个Gate”完整段；现有较小modality gap≠更好consumer，尚未承载whitening两侧不对称时shared nuisance与signal在固定容量内竞争、prediction方向不同与MSE反侧这条objective选择边界。Ch22/24开篇交接已读，不将flow生成或domain科学应用搬进表示owner。

### 唯一literal（仅首centroid/pair段marker后、下一“对齐路径还取决于是否保留feature模长”前，待PRE/窄授）

配对关系也不保证共享方向就是任务信号：两路共同出现的背景或采集因素，同样可能占据有限表示容量。在线性、固定窄瓶颈且signal/nuisance可分的[受限分析](https://arxiv.org/html/2606.11190v1#S3)中，双边白化的跨模态对齐与只白化输入侧的跨模态预测，对这些方向使用不同谱排序；较低预测重构误差仍可伴更差signal恢复，交换source/target也会改变条件。因此选择alignment还是prediction，应同时验任务signal、相关nuisance与预测方向，而不是只验配对相似或MSE。该相图不认证任意深网：过宽非线性瓶颈可同时编码两者，基于少量标签与近线性特征的诊断也不是无监督真值；partial-recovery下界为零不证明完全失败。标签、协方差/谱估计、训练与独立任务probe都付费，换目标或输入人口后需重验；条件不满足时保留原对比目标、明确监督或独立单模态读出，不让统计共享替语义充分性签字。<!-- source-family:SF-2026-ARXIV-2606-11190 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11190` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11190v1)§3/4.1–4.4/A1–A7/B/C-F9由jun11_review首备，作者实际采用必要层并读actualCh23，2+2+3=7。仅CA/CP谱竞争与source方向/MSE反侧；保spiked/固定k、overcapacity、r0下界非失败及COCO目标/probe混杂，不采科学应用、普遍非线性相图或无标签诊断。未核代码/复现；必要/PRE与POST不预签。

## A10 Arbiter — 2606.10747v1（受限主动检测差额）

[精确v1](https://arxiv.org/html/2606.10747v1)；2+2+2=6经root§12门槛→jun11_review决定事实/日期cue复核。作者实际§3、§4.1/4.2、§5 T2–T7已读；reader首备§4.3/5/6必要并实际采用，不重复其Methods。Jun6 AITC口头同题报告原件与有限早稿路径详SUP_ADMISSION末，reader§22已核；事件记Jun10 arXiv正文，不冒称全球首次传播。

必要命题仅：同neutral-prompt Qwen2.5 risky-financial organism人口内，black-box Ask+Log相对只等公开消息，F1 .12→.51，无systemprompt/CoT权限，不能把absent public misalignment证据当同预算可识别性已经充分；也不是只借auditor参与者命名。Ask-only .28→Ask+Log .51，不把组合收益归因纯query；logging在同aligned-baseline人口增加AvgFP .10→1.15，不能把更多可疑记录当已证实危险。T2 risky-prompt条件反而PureObs1.0/AskLog.92，工具不必单调提高准确率；不同backboneauditor亦差很大，不能用audit框架名自授通用能力。

评价边界：三agent/30turn固定roundrobin、五条conversation variants，每格n20 runs抽样；不是20独立真实任务或自然开源任意模型人口。weight-vs-prompt及aligned baseline有Qwen/Gemma/topic变化，不能拿该跨人口差直接断言所有weightmisalignment更难。受测agent弱于auditor、宽CI限制泛化。预算是words和固定inspection proxy而非真实tokens/GPU费/latency；turn的message-round定义不签生产实时拦截。系统prompt与CoT访问是额外特权，不属于无需内部信息blackbox结论；未核artifact/攻击实现/复现。

Actual owner `AGENT-MULTI-AGENT`，已读Ch82“Fleet oversight…”完整两段与marker，前directed runtime controller完整后继和后“角色正确性…”完整段；前者拥有confidence/calibration/group相关性/人工预算，不含auditor按预算主动向成员取新证据与只读conversation的差额；后者role obligation不是主动检测权限。拟一段放Fleet oversight最后完整marker后/角色正确性标题前，保持本段只audit proposal、不增加control或rollback权限。Ch81/83生命周期交接当前已有，不复制安全gate/工具协议。

### 唯一literal（待PRE/窄授）

监督还可以主动获取新观察，而不只对既有对话重打分：在授权预算内向某个成员追问，把回答与公开轨迹并列留证，再决定是否需要外部复核。[受限三Agent对照](https://arxiv.org/html/2606.10747v1#S5)中，同一权重诱导、neutral-prompt人口的主动问询加记录比纯观察发现更多异常，两格都未读取system prompt或CoT；这只说明该人口下可取得的信息不同，不证明回答忠实或审计器可靠。记录也会放大误报，额外读取内部prompt/trace更不能与black-box检测混比；tool budget和message轮次不等真实延迟。五条模拟对话、较强auditor与有限backbone尚不支持自然开放团队安全，追问、记录、存储和独立验证全部计费。Auditor只提出需检查的成员与证据，不由可疑分数自动授予阻断/回滚权限；交互会污染任务、权限不足或误报代价较高时，保留只读监控、确定性检查和人工升级，而不把无报警当对齐保证。<!-- source-family:SF-2026-ARXIV-2606-10747 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10747` — Daily2026-06-11补Jun10 arxiv正文；[exact-v1](https://arxiv.org/html/2606.10747v1)§3–6/T2–7，2+2+2=6。作者与jun11_review分工必要已实际采用，只neutral同人口/无SP-CoT的active问询+log相对passive；保早Jun6 talk非更早正文证、五对话/强auditor/wordbudget、组合与误报/特权限制，不授真实misalignment识别/生产实时或控制权限。未核实现/复现；PRE/POST待核。

## A11 K-Forcing — 2606.10820v1（joint-noise语言采样）

[精确v1](https://arxiv.org/html/2606.10820v1)，rootB2准入2+1+3=6；实际§3.1–3.4、§4.1–4.3/T1–3、C1 KV规则、D1/D2成本/评测。只联合noise→token mapping与准备/状态边界，不采用MDLM“lossless NFE lower bound”的一般定理，也不展开无关proof/temperature扩展/代码。

机制：k iid uniform noise经过可共享prefix noise的因果Transformer映射为k个greedy token，不是独立无noise MTP marginals；递归inverse-CDF teacher仅证明联合mapping表达的存在，不证明有限student学成后等分布。以真实data反演noise有teacher/data分布与窄CDF bin数值问题，先forward uniform→teacher target训k1，再用旧k模型两次顺序rollout训2k，经历1→2→4。fullycausal设计每noise独立position+sharedoutputhead，避免把k随机决策塞单hidden bottleneck。

状态/费用：C1每轮仅保真实context token的KV，noise KV丢弃，下一轮重新输入上一k个真实token及k个fresh noise（2k新输入）；不是k输出已经同时拥有永久KV、也非无额外token。相同stride仅本实验固定长度batch更规整，不认证不同长度请求/EOS/任意scheduler无需padding和realignment。每stage500k steps/batch512、8H100，实际dense training mask导致O(k²)相对AR成本，O(k)blocksparse是futurekernel；末100k fullFP32、前400kFP16，不能借普通BF16AR成本宣传蒸馏便宜。Noise encoder约5.9M，主干108M LM1B/124M OWT、12层，128/1024context，非已验证industrial-scale model。

直接对照：同H100/BF16/KV/FlashAttn2，1024prefix、固定completion length，batch4/16/128、warmup后5run generated tokens（含special）/wallclock。T1 k4速度高但LM1B GenPPL104.8→127.6/win42.9%、OWTwin39.4%；OWT GenPPL更低24.97却judge更差，是typicality≠quality反侧。Judge Qwen3.5-27B强制A/B无tie，截EOS、随机顺序，无human/任务truth认证。T2noise inversion vsselfforcing也换了监督teacher及前置training预算，不把NLL差全归单机制；noise-conditioned NLL比context-only AR低不证明target likelihood优于AR。T3NFE把fullsize draft/verify按两次forward计，不等FLOPs/真实speculative wallclock，原文也未作所有paradigm同serving端到端TPS比较。完整服务SLO/longCoT/大LLM/安全未测，未核代码/复现。

Actual owner `MODEL-DECODER-ONLY`：已读Ch18完整“内部预测粒度可以不同于输出粒度”密集NTP→conceptclock→causal shift/stateidentity→MTP退路→证据段以及紧邻“历史状态生产与最终预测…”完整段。现有latentconcept仍外部逐token输出，不含固定k噪声联合采样和noise仅本轮状态的差额；Ch24/48分别保生成范式与exact verifier，不能把新mapping称无损speculation。拟只conceptclock证据段SF2609-10715 marker后/历史生产标题前一段+trueH2本人注，不重复整套batching或cache原理。

### 唯一literal（待必要/PRE/窄授）

多个未来位置也可以共享随机输入来形成联合样本，而不只是各自预测一个边缘分布：先给k个独立uniform变量，再让因果noise-conditioned网络用前缀噪声共同决定一块k个token，避免显式枚举词表的k次方组合。[受限语言模型分支](https://arxiv.org/html/2606.10820v1#S3)先蒸馏单token映射，再由旧k模型两次rollout教2k；递归inverse-CDF只证明理想映射存在，不保证学到的单pass保持原AR分布。它用固定输出stride换更规整的batch，却把分布误差交给训练：k较大仍损质量，noise-conditioned低NLL或外部Gen-PPL较低都不等更好文本。Noise KV只属本轮，下一轮须重新处理已生成真实tokens，不能把临时noise当永久历史；多轮teacher/全模型训练、实际dense mask、重处理与完整服务回归都付费。证据仍是约百M模型与固定短completion，不签任意大模型/EOS/连续batching SLO；需要原分布保证时保留exact speculative verification，准备或质量不合时回到普通AR/MTP，不以固定k输出自动批准无损采样。<!-- source-family:SF-2026-ARXIV-2606-10820 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10820` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10820v1)§3/4/C1/D1D2，2+1+3=6。只noise jointmapping/1→2→4准备与noise临时KV，保百M/短context、质量反侧、不同teacher/NLL条件、O(k²)真实训练与NFE非全费，不采用无损/通用serving或MDLM一般lowerbound。未核代码/复现；必要/actualowner/PRE/POST待独核。

## A12 A Theory on Flow Matching — 2606.10089v1（采样桥接中心争议，安全终态）

[精确v1](https://arxiv.org/html/2606.10089v1)，2+1+3=6。合法Jun10日期与完整AB新准入见SUP_ADMISSION末及reader§20。jun11_review首备实际§3完整理论/§4核心设置结果、C完整采样sketch及F1–F2/Th3.5相关完整proof；没有完整读A梯度或B/E泛化证明，不认证其全部定理。作者作为非首备者已实际只核C1/F1原假设/整proof、F2受影响近文、Eq1与Ass4，中心两个冲突一致，无重复无关Methods。

原拟命题为两层ReLU过参数化GD→conditional velocity泛化→样本W1距离；但最后桥接目前不能正面采用：

- [C1](https://arxiv.org/html/2606.10089v1#A3)/[F1](https://arxiv.org/html/2606.10089v1#A6)只假设compact K/nonempty interior、density≥pmin、L-Lipschitz f、每r≤diamK的球体积下界，声称sup|f|≤(2^(d+1)L^d E|f|/(βpmin))^(1/(d+1))。证明选r=M/(2L)直接用只在r≤diamK成立的几何界，没有分支或小振幅前提。独立数学反例：d1、K[0,1]、Xuniform、β=pmin=1、全R恒f100合法满足L1上界；结论100≤20矛盾，r50确实超diam1。不是论文实验或运行复现；只反驳按印文的一般lemma，不否定可能加大小项/局部条件后能修补。
- Eq1线性μ(t)=t、σ(t)=1−t满足Ass4的幅值/一阶导有界，但固定x0下v_t(x|x0)=(x−x0)/t，关于x的Lip常数1/t无全[0,1]的固定B0上界。F2/Th3.5将Ass4推进成用于真实/近似ODE两状态的统一Gronwall系数，未有端点截断/可积系数或邻接条件修补；沿真实配对轨迹的常velocity不认证任意近似轨迹上的同界。

其他首备必要已采用但不当修补：Alg1 source为x0|x1而非一般独立Gaussian，实验N(x1,I)，新采样P0不能自动叫标准Gaussian；固定source条件生成接口需明确。MNIST/Fashion实验PCA7/500sample/200Euler、slicedW1不证完整W1。局部优化/泛化链与经验可能仍有价值，未核的独立定理不因此宣布错误；拟采样主张确实依赖上述具体lemma，不能把小模型标签当排除理由或用较低slicedW1掩盖它。

reader§25已汇入作者非首备实际核并作6/争议/Books暂缓；未写泛提醒入Ch24，不借争议消耗普通待办。重开只需覆盖r超diam的有效L1→sup桥接、明确时间端点/真实近似轨迹的Lip条件及其支撑的采样定理；或按真实新日期处理具名修订。当前不作正面W1/训练充分性保证，不支撑Books或全网无误；无无限理论/代码追查。

## A13 Mean Flow Distillation — 2606.11155v1（区间目标与梯度近似分账）

[精确v1](https://arxiv.org/html/2606.11155v1)，2+1+3=6 rootB2已校准。实际§3、§4.1–4.4/Alg1、§5.2/5.3、B3/B6、C3及F限制。只时间平均的目标/成立条件/训练费用与直接反侧，不读完整occupancy应用recipe、全部图或artifact。

关键区别：student单步generator没有自己的瞬时probability-flow field，另训auxiliary flow以近似student分布，假设理想aux可准确恢复该场；在同一student noisy state Xs起步，分别沿teacher/aux的场积分s→t，以displacement/(t−s)相减作为guidance，不是直接让generator吐出的单个endpoint等于teacher轨迹。Theorem4.1/4.3为Lip场、正定divergence、时间对fullsupport、理想精确aux及零期望目标的充分条件，不授finite误差/有限步solver或有限训练student的等分布。

实际训练省掉solver Jacobian（Eq18→20固定guidance），不是精确目标gradient；B6承认方向cosine常低/负、缺紧误差界，不能因原gradient反而训练不好就称identity为真实gradient。Alg1辅助10步/学生1步；SANA1.6B aux rank64约34M trainable，训练仍过完整backbone，部署丢aux只表示没有这份推理分支，不退还训练费用。mean-fieldODE积分是主要成本，small step并非单调更好。

方差边界：B3 boxcar平均可衰减被视为高频的误差，也会平滑真实高频变化；C3的1/K依赖零均值、同方差、跨积分步IID噪声，确定teacher沿相关trajectory/系统偏差不自动满足。其Eq46把variance difference写成减号而后近似2σ²，不能照作通用variance恒等式；loss violin较窄也不等完整参数gradient variance已隔离相同预算。只采受限平滑直觉与实测稳定性，不授普遍1/K/低频无偏或必要省Jacobian定理。

直接评价：SANA1.6B text-to-image、LAIONaesthetic6.5+，多感知/文本分数与相对teacher sample的DINO-FID；DMD2/SenseFlow的PickScore/HPS部分更好、不同感知/GAN组合限制归因，不称全面支配。§5.3同RTXPRO6000约MFD25GPUh/20GB、VSD22/20、CD4/15、DMD230/50是各完整配方，不叫免费或所有预算更优。reader首备A.3.2缺层已实际采用：明确BF16、1024²、batch1、3000步/finalcheckpoint、teacherCFG4.5，不能把本项precision写未披露；仅未给的比较配置/不确定性保NotDisclosed。未核代码/复现，不重复reader该recipe。

Actual owner Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS`，已读Few-step Distillation整节中K-DMD同状态多teacher完整段与SD3.5Flash后继完整两段、邻接初段quality/privacy与主FlowMatching平均velocity分支。现有同状态局部/分布目标分责不含沿同起点两流的区间displacement作guidance、理想零目标与近似gradient分开的具体差额；MeanFlow image-like head属于输出参数化，不能代替本分布蒸馏接口。拟只K-DMD段marker后/下一“少步学生的score条件还可以…”段前一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

同一noisy state上的蒸馏目标，还可以从某一瞬时velocity改为一段位移：另训flow估计当前student分布，从同一起点分别沿它与teacher的场积分，再比较区间平均速度。这个[受限分支](https://arxiv.org/html/2606.11155v1#S4)把generator和描述其分布的辅助场分开，时间平均可能缓和高频误差，却不自动消除相关噪声、系统偏差或真实快速变化；1/K方差缩放还依赖跨步IID等额外条件。Lip场、充分时间覆盖、理想aux与零目标下的分布匹配，也不证明实际省掉solver Jacobian的guidance就是精确gradient或必达同一解。辅助更新、两条ODE积分、solver/步长搜索与完整质量回归都付费，部署丢aux不让准备免费；更小步长和更多平均亦可退步。状态支持、aux跟踪或质量—总费不足时，保留瞬时/原分布蒸馏、更长采样与teacher，而不从更窄loss曲线批准普遍稳定、无偏或无损少步。<!-- source-family:SF-2026-ARXIV-2606-11155 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11155` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11155v1)§3–4/5.2–5.3/B3/B6/C3/F，2+1+3=6。仅aux分布场/同起点区间位移guidance，保理想zero/fullsupport、solver-Jacobian近似、IID方差假设/相关误差与全准备费，不采Eq46或普遍1/K/精确梯度/零部署总费。未核实现/复现；必要/owner/PRE/POST待独核。

## A14 GASLoC — 2606.11081v1（通信节奏改变优化语义）

[精确v1](https://arxiv.org/html/2606.11081v1)，2+2+2=6 rootB2已校准。实际§3/Alg1、§4/T1–3、B协议、C Local-DAdam定义、E1 outeroptimizer与F模拟反侧；不扩大AppendixA完整证明或代码。

原增量不是“localsteps+gossip+outermomentum”的名称组合：inner optimizer保局部轨迹，outer接收从当前本地起点到邻居**post-local**参数的pseudo-gradient；随机permutation产生对称pair/ring，改变同步图而非只删AllReduce调用。C明确DAdam原H1混pre-update参数再加本地delta；H>1延迟这套mix后纠偏依赖旧起点，形成不同Local-DAdam，不得把其反退称原DAdam本来支持H30又失败。outermomentum把低频局部轨迹与mixing耦合，不能套同步Adam等价；paperSGD/L-smooth/unbiased有限方差的Proposition2不证明实际AdamW+Nesterov任意非IID/故障收敛。

评价：FineWeb、Llama2 tokenizer、134M/551M、2.7B/11Btokens、context2048、global2Mtokens、BF16，各method调localLR和outerNesterov。部分4H100/node NVLink+IB实际训练，但所有134M与551M n>8模拟多个logicalworker/GPU，不能当32独立节点实测。T1 H30 ring32:3.81对DiLoCo3.53；T3 551M/16replica twopeer2.72对DiLoCo2.67，稀疏通信仍可损质量，所有方法也未胜DDP质量。local-DAdam只是controlled延迟变体，不外推所有original overlaps。

异构§4.2为8A100nodes、1Gbps/一worker100或200Mbps模拟网络、相同总tokens，straggler通过减少H_i补通信，等tokens不等每worker曝光/轨迹不变；sym perworker timing upperbound不处理directed/asymmetric协议，不将估算max混合界当端到端必然时间支配。F70B/16workers×8GPU、peak4.5PF/40%MFU是理论利用率，不是70B已训。faulttolerance只在failed exchange可skip/reschedule假设下说明，未实证故障恢复/任意async免barrier；random schedule、inner/outermoments、局部H与数据进度均须恢复/计费。seed/errorbars及真实SLO未披露处不补造，未核实现/复现。

Actual owner `TRAIN-DISTRIBUTED-TRAINING`，Ch36§从本机协作到分布式执行内LocalSGD异构、局部参数切片、2604.24708与adaptivegossip2604.09970的完整段链及其后posterior分支已读。现正文已讲optimizerhistory和模型重建估计分责，却未明确改变mix发生时点/使用pre-vs-postlocal状态就改变算法与baseline资格；此处只补该窄差额。Ch35/37开篇交接已读，不新增共享State/拓扑章。拟09970独立marker后/“若目标不是找到一个参数最小点…”前一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

降低gossip频率也不只是把原通信调用每隔H步执行一次：在H步本地更新之后，用旧起点参数作共识纠偏，与从本地起点到邻居更新后参数构造outer pseudo-gradient，是两种优化轨迹。[受限预训练对照](https://arxiv.org/html/2606.11081v1#S3)将后一接口与随机对称peer交换结合，说明inner/outer optimizer、pre/post-local状态和通信图须共同定义，不能让延迟混合的派生baseline继承原每步算法名称。随机稀疏图减少每轮邻居数，仍支付拓扑协调、共识误差与本地漂移；减少慢worker的localsteps也改变其数据曝光，不授同步Adam等价、任意异步或故障恢复。百M模型的同token对照仍有质量差额，70B利用率只是模拟，SGD条件下的界不证明实际AdamW/Nesterov全部配置。内外moments、H、peer schedule与数据进度共同恢复并结算调参/通信费用；混合或质量失配时缩短local interval、加密交换或保留DiLoCo/同步完整collective，不由少peer与估算墙钟签发无损扩展。<!-- source-family:SF-2026-ARXIV-2606-11081 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11081` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11081v1)§3–4/B/C/E1/F，2+2+2=6。只pre/post-local纠偏与inner/outer/gossip接口耦合，保LocalDAdam派生资格、logicalworkers/同token非曝光、sparse质量差/70B模拟及SGD与fault假设，不采同步等价/普遍速度。未核代码/复现；必要/owner/PRE/POST待独核。

## A15 Provenance Tracking — 2606.10937v1（中心bisimulation争议）

[精确v1](https://arxiv.org/html/2606.10937v1)，rootB3准入2+2+2=6。jun11_review首备实际§2.3–3.3/§4.1–4.3/Alg1/§5，完整核心与实现/直接评价已存review§32；作者实际采用，只独立核Def2.4/2.5/Th2.6及§3.1–3.3完整中心关系，不重复实现Methods/代码。

中心冲突经非首备者实际确认：原F continuation本来携Σ labels，Conv→ReLU与ConvReLU首观察不同，§3.1未定义forget-label/value quotient就称原final F denotation相同，不能从tensor复合相等推出该labeled final-coalgebra相同。§3.2列出的完整R确仅入口/两个action对/termination，Conv action后继s1与fused后继s2未成R对；A只是Σ*×Σ′抽象关系，没有weak/tau或多步lifting的正式规则使Def2.5方块成立，近文也未补。§3.3值等价自动lift到更细观测同样无新条件。不是因为数学标签排除，也不表示所有合适weak-bisimulation形式化均不可能；当前中心“已由coinduction保证”的采用链不足。

已实际采用reader实现层：frontend operator anchor贯穿Relay；fusion聚合span，split复制span，到KIR粒度稳定可去metadata。§4.2/Alg1实际aux pass及每pass @inject_span(pre,post,node_map)维护correspondence，不是从最终非单射图恢复唯一历史或无需pass instrumentation/IR metadata。modifiedMNIST21→7 operators、编译.17→.18s，MobileNet139→66、3.57→4s，是约5/12%编译instrumentation而非推理延迟；不认证全部lineage coverage/正确性、任意闭源模型或零开销。

Actual Ch49计算图开篇、等价表达/typed IR完整链与“Lowering与低精度执行…CommitBoundary”完整段已读；现正文已有数值/shape/资产身份与动态恢复不唯一的边界。若删去不闭合的bisimulation，实际span聚合/复制还是既有metadata传播，未获得另一个足以承载初筛新正确性保证的独立长程接口；不能为凑I把通用“数值等价非provenance”另写一次。因此保6分中心争议、Books暂缓，不降分/删候选、不用访问故障作借口。重开只需给符合Def2.5的完整R/多步或weak观察规则及其与实际span维护一致的正确性条件/覆盖证据；不扩全部kernel或假想实现。本项待reader汇总作者实际核为唯一终态复核，不要求第三Methods。

## A16 Express Language Modeling — 2606.10944v1（reader首备已实际采用）

[精确v1](https://arxiv.org/html/2606.10944v1)，2+2+3=7，rootB3准入。reader§34首备实际§2–3/Alg1–5/§4–5、B memory/runtime、D/E/F直接整proof与I1–I3；作者实际采用必要/直接反侧，只补actualowner/唯一稿，不第三遍Methods。

可支持窄命题：面向全input的一份noncausal coreset不能直接保证各prefix；按几何blocks维护带weight的多级summary与currentblock，先query旧cache+自身KV，再更新summary，用受限noncausal halving条件构造causal prefix接口。fixed target s下cache≤6s、KH workspace10sd是该结构/固定s的容量界，不等所有runtime常量；Th3/F误差含exp(2R²/√d)、value norm与本例prob≥1/2，不授任意norm、所有层生成等分布或一次无失败算法。近似attention影响后续KV，层内误差界不自动关闭整网误差。

82x为A6000 attention核而非全模型端到端；PPL可为原1.06倍，任务质量/资源是取舍。MATH61%cache/56%time是有限曲线，I3按每题选realized配置不等统一hard cap或同SLO；time仅32层attention三部分、一次timed，不混作整个LLM服务的稳定速度。weight、metadata、RNG/stage、currentblock与summary共同定义状态，压缩/合并/weighted读取/新老KV与实际回归全付费；未核artifact/代码/复现，不扩大offline coreset完整recipe。

Actual owner `MODEL-SELF-ATTENTION`：已读Ch14“改变算子之后，转换与执行必须分别验收”完整概念、视频structured factors后继及冷启动转换段；固定summary/latent路线原本不等该softmax coreset的prefix消费协议。Ch13/15开篇交接已读，Ch22拥有全历史可寻址选择、Ch45持物理KV，不复制它们的容量/分页论证。拟在本节首概念完整段后/“少算关系还可以不直接删除attention edges…”前一段+trueH2本人注。

### 唯一literal（待owner/PRE/窄授）

面向整段输入得到的近似summary，也不能直接交给causal decoder读取每个prefix：它可能含未来记录，或只保证全段的误差。一个[受限coreset分支](https://arxiv.org/html/2606.10944v1#S3)因此按几何block维护带weight的多级summary与当前块，当前query先读旧summary和自身KV，再更新缓存；因果资格、权重与压缩阶段必须一起保存。这样可把满足条件的noncausal近似转成有界prefix接口，却没有变成exact attention：误差仍依query/key范数、value尺度与随机成功条件，改变当前输出后也会改变后续KV。固定目标大小的cache界不等每题事后选配置都满足同一hardcap，attention核时间更不是全模型速度；合并、重压缩、weighted读取、metadata/RNG和质量回归均计费。高范数、长程证据或误差累积失配时，扩大summary、提高精度或保留dense/原有稀疏路径，不由单层coreset保证签发整段生成分布与服务SLO。<!-- source-family:SF-2026-ARXIV-2606-10944 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10944` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10944v1)§2–5/B/D–F/I1–I3由jun11_review§34首备，作者实际采用/读actualCh14，2+2+3=7。只weighted geometric summary的prefix query-before-update接口，保norm/value/prob、后续KV、固定s/每题选点、核非全模型/一次计时与压缩全费，不授exact/普遍服务保证。未核代码/复现；PRE/POST待核。

## A17 Attention Amnesia — 2606.11052v1（reader首备已实际采用）

[精确v1](https://arxiv.org/html/2606.11052v1)，2+2+2=6。reader§35实际§3/4经验/5–7所有主表与消融、J-K/L直接反侧及I Eq89–90，作者实际采用仅实证/QK局部干预层，不重复Methods或Markov理论。不同架构/数据的CoT-SFT可损长NIAH，preQK+post其余参数是新的混合asset；QK restoration或正交对齐并非精确回到原routing，也非所有SFT/所有架构损失。

直接反侧全保：Jet S2@256K11.6→restore7.6更坏；Hype9B67.2→SFT9.4→restore19.6远未pre，math/GSM亦可损。T3 Hype5B/OpenThoughts S3@256K pre75.2→SFT91.4→restore79.4，该格SFT本已提高且restore损害；§7.2叙述错把pre当SFT，不当该格修复收益。Tulu/Qwen反侧限制普遍性，未使用I Eq89→90忽略向量抵消的normsum下界；旁证明不足不删除实证、不用H替普通局部结论。checkpoint同源/层shape与QK、VO/其他post参数身份共同保存，评价人口/长度与SFT转换诊断/完整回归费用独立；未核运行/代码/复现。

Actual owner `TRAIN-SFT`：已实读Ch29“整体Activation相似不能证明内部能力未重排”完整两段+marker以及下一Scaffold概念完整两段；现有平均表征诊断不能代逐组件干预和pre/post混合asset的能力取舍，非仅复述SFT会遗忘。Ch28/30开篇/适配空间交接已读。拟该11426完整marker后/Scaffold主标题前一段+trueH2本人注，不扩模型attention教科书或复制多篇SFT退化。

### 唯一literal（待owner/PRE/窄授）

局部干预还可把“更新了什么”与“损伤了什么”分开检查：CoT-SFT后分别验长程检索与推理，再只把Q/K换回同源pre-SFT版本，让其余参数保留post-SFT，比较重新组合的行为。[受限hybrid模型对照](https://arxiv.org/html/2606.11052v1)支持路由投影与其他更新承担不同责任，却不证明旧Q/K精确恢复原routing或所有退化都由它造成；部分长度/模型修复反而更差，原SFT已提高的切片也可能被换回破坏，推理收益同样需回归。两checkpoint、层shape、投影集合和混合资产须共同登记，不能把它当原任一模型的无损补丁；SFT、诊断、转换与长程/数学双侧验收都计费。不具备兼容资产、质量或净费用不合时，保留原post-SFT/原base、较窄适配或可信replay，而不由平均activation相似或一个NIAH恢复点批准能力保持。<!-- source-family:SF-2026-ARXIV-2606-11052 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11052` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11052v1)§3–7/J-K/L及I受影响由jun11_review§35首备，作者实际采用实证并读actualCh29，2+2+2=6。只preQK/post其余的受限干预，保Jet反退/Hype9B远未pre/T3§7.2口径/数学回退与资产全费，不采Markov普遍定理、Eq89–90下界或精确恢复。未核实现/复现；PRE/POST待核。

## A18 Flow-DPPO — 2606.11025v1（同state Gaussian divergence不等硬trust region）

[精确v1](https://arxiv.org/html/2606.11025v1)，2+1+2=5。实际§2.1、§3.1–3.3、§4主表/4.2、AppendixE完整方向性反侧/F资源；只closed per-step KL+实际mask，不认证全部performance theorem/附录proof。对同state、相同正定isotropic covariance的两Gaussian，KL=||mean_old−mean_new||²/(2σ²)，已采action的logratio另有ε·d/σ随机项；这消掉的是同state的action MC误差，不是state分布/advantage/全gradient方差。实际mask在KL超δ且A(r−1)>0时丢该term，另留“纠偏”term。E明确ratio sign只是KL变化方向heuristic，正负不保证散度增减；预测mask的mean自由向量推导不含共享networkJacobian，尚未实证，不当已交付改进。当前点mask也不是更新后投影或pathwise hardcap，不能由bounded surrogate penalty自授monotonic reward。

评价SD3.5Medium/FLUX2klein9B/FLUX1dev，GenEval2约20k synthetic train/800eval及PickScore域外/CLIP/HPS，多reward等权GDPO；T1 SD3.5原FlowDPPO CLIP .345低于FlowGRPO .358/Guard .353，FLUX2+CPS GenEval55.2低于无CPS57.7，非allmetrics/allvariant全胜。KL-reference越低不直接等遗忘越低或rewardhack消失；direction/δ与multi-epoch消融仅指定recipe局部支持。F H20/96GB，总main90kGPUh、含全部约140k；LoRA r32/64，512²，10/14steps、G16×64groups、mixODE/SDE随机前三个step于前半段，η.8；没有独立seed/precision完整披露处不补造。预测mask/longvideo未来方向不算已实现，未核代码/复现。

Actual Ch32“KL penalty与PPO clipping不是同一约束”完整节及前clipping、后完整loss交接已读；现有sampled estimator选择没有同state Gaussian正covariance消action采样噪声与ratio-sign非divergence方向这个限定接口。Ch31/33训练职责交接已读；Ch24持flow sampler，不复制其采样路径论证。拟该节末“Estimator choice会影响bias、variance和计算”完整段后/完整PPOloss标题前一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

动作分布具有可算结构时，还可将“采到了哪个动作”与“同一state下分布变了多少”分开：对共享同一正协方差的Gaussian新旧策略，用均值位移直接求KL，再决定哪些ratio–advantage项继续更新。[受限flow微调分支](https://arxiv.org/html/2606.11025v1#S3)由此去掉单action ratio的部分采样噪声，却仍有state/advantage与模型求值费用；协方差变化或零噪声端点不能照用这个简式。实际超阈值mask还用A(r−1)的符号区分向外/纠偏项，但该符号不保证共享参数更新后KL真的下降，未验证的预测mask也不是已部署能力。旧/新分布KL、reference penalty和更新后硬trust region是三件事；当前点少更新不授单调reward、全状态hardcap或无遗忘。旧均值/方差身份、rollout、当前前向、mask与质量回归都计费；结构、质量或预算失配时保留原clipping、独立KL监测与重采样，不由closed-form divergence批准无损稳定。<!-- source-family:SF-2026-ARXIV-2606-11025 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11025` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11025v1)§2–4/E/F，2+1+2=5。只同state等正covariance Gaussian KL与ratio-sign mask分责；保E方向heuristic/预测未验证、当前mask非hardprojection、质量/全费反侧，不采普遍monotonic或variancefree。未核实现/复现；必要/PRE/POST待独核。

## A19 CPPO — 2606.10968v1（累计divergence不是prefix ratio）

[精确v1](https://arxiv.org/html/2606.10968v1)，2+1+3=6。实际§3.1/3.2条件与§3.3–3.4/Alg1、§4全部对照/消融、AppendixD原配置/评测；不遍历AppendixB全部proof，不采用无条件monotonic guarantee。

新mask不改原token ratio×groupadvantage loss，改变的是分配divergence资格：w从1降至.8，所以单token允许δ/w后部稍松；S/W累计weighted divergence另给prefix预算，含首步δ slack。两条约束交由one-token shifted cumsum，已被masked token也纳入后继S，不是简单全response平均也不是prefix likelihoodratio。只有A(r−1)>0的outward项受资格限制，correction例外及sharedparameter使其不等实际新policy逐prefix满足hardcap。Base δb取**完整response**D的P90再clamp[min,2min]，是postrollout训练mask的序列配置，不是在线生成只见prefix的sensor。

理论与实践分开：finite horizon、boundedreward、真实fullTV与逐prefix条件才给residual bound/Abel比较；late权重放宽有1/wmin代价，initialslack另加低阶项，不能说无成本强界。实际TopK20+sample+other是fullTV的**lower bound**，不是上界或完整policy散度证书；相同proxy/δ的matchedDPPO比较能支持这套mask局部作用，却不使约束满足原定理。方向性ratio例外同样不是KL/TV保证。

四Qwen3 1.7B/post/Base、8BBase、30BA3BBase，DAPOmath17k，8k/G8或16k/G16，verLGRPO，AdamW1e−6、zero-variance过滤/noentropy/noRefKL。AIME24/25/26 Avg@16验证温度.7/topp.95，报告各自matched horizon中最佳**验证**mean checkpoint而非独立最终test；Tstop1120/680/490/560、各模型update数不同，不能跨模型直归因更长horizon。ordered-vs-shuffled与单constraint消融支持位置/累计分责，softgate相近不授unique最佳；同Qwen数学人口不外推全任务。硬件/precision/seedCI未披露记未披露，cumsum/divergence取值与rollout/选点均付费，未核代码/复现。

Actual Ch32 prefixratio/positionclip完整段、2610.29999精确prefix恒等与实用surrogate完整段、后N-step完整段均已读。现有是累计**likelihoodratio**及方差/校准，非本项累计**distribution-divergence**的token/prefix双预算；主题相同不当已有覆盖。拟2610.29999完整段marker后/下一N-step独立binding前一段+trueH2本人注，避开A18另一指定小节；不改原prefix ratio逻辑。

### 唯一literal（待必要/PRE/窄授）

前缀风险还可约束“累计改变了多少分布”，而不去累乘已采token的likelihoodratio：用位置权重让前部token的divergence额度较紧，同时累计每个prefix的weighted divergence，决定本token的向外更新是否仍可保留。[受限CPPO分支](https://arxiv.org/html/2606.10968v1#S3)把单token额度与prefix额度分开，但后部放宽、首步slack及纠偏例外都属于实际规则，不能当成免费更强的全路径hardcap。训练中的Top-K/other TV只是full-vocabulary TV的下界，matched proxy下的收益不证明真实散度也满足理论阈值；完整response算出的自适应额度更不是线上prefix-only sensor。需共同保存rollout law、有效长度/位置、divergence分区、权重和cumsum规则，并计入评分、mask、rollout与选点费用。数学验证集择优不等独立发布测试，漂移/质量或全费不合时，保原token/N-step ratio、已验uniformdivergence规则与更频繁重采，不由更多被保留的更新项签发单调改进。<!-- source-family:SF-2026-ARXIV-2606-10968 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10968` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10968v1)§3–4/D，2+1+3=6。只weighted token+prefix divergence双额度，保TopK-TV下界非full保证、initialslack/correction/后部松界、整responseδb与bestvalidation及全费，不采无条件monotonic/hardcap。未核实现/复现；必要/PRE/POST待独核。

## A20 Provenance-Grounded Gate — 2606.11127v1（reader首备实际采用）

[精确v1](https://arxiv.org/html/2606.11127v1)，2+1+2=5。作者实际采用reader§37首备§2–4/Limitations、B1–B5/C/D/E的必要与直接反侧，不重复Methods。生成绑定append-only原chunk，source-conditioned faithfulness与不读source的quality gate有不同拒绝人口；hall失败再生、quality失败critique/rewrite是不同路由。低Jaccard不证明独立/充分；rewrite只重入reward，保持事实是意图，不认证改后忠实。exact对retrieved的14B反侧、8B sequential R-L低于unfiltered、同Qwen而非跨family、hall5000对others约3000以及正文/配置/百分比冲突均保，不采用通用scale主效应。BERTScore不是claim真值，recover yield不是下游效用；全部生成/原source存储、judge、再生/重写、复评及训练费用独立。未核代码/复现。

Actual owner `TRAIN-DATA`：Ch27 Synthetic节首概念完整段、02908两完整后继段及lineage1026–1044实际已读，Ch28开篇/Ch23→Ch24→Ch25表示—生成—状态边界已读。旧Review notes的11127 trace声称已吸收双gate/diagnosed repair，但目标正文未见对应具体机制；不能由trace替实际正文签已有覆盖。当前generator/judge共同盲区概念未表达“给定原chunk的faithfulness”与“无source quality”两条资格，且改写后的资格不得从旧样本继承。拟本节首概念段后/02908“面向会修改环境…”前原一段+trueH2本人注，不改旧trace日期。

### 唯一literal（待PRE/窄授）

生成监督已有原始依据时，还应把“忠于给定source”与“适合拿来训练”拆成两道资格：先把生成物绑定不可静默替换的原chunk，再分别用读source的faithfulness gate与不读source的quality gate提出保留或拒绝。[受限双gate分支](https://arxiv.org/html/2606.11127v1)按失败类型再生或critique后重写，但拒绝人口不同不证明两门独立充分，回收更多样本也不保证下游更好；改写后仅重过quality门尤其不能继承旧faithfulness资格，需另验事实与来源关系。原chunk、generator/judge、原样本、失败理由、修订与实际训练人口共同保存；同系列judge的相似结果不是跨家族真值，较强gate或顺次筛选亦有质量反退。生成、证据存储、全部重试/改写/复评和训练均计费；source缺失、改写资格或独立效用不稳时，保留原样本/隔离记录、可信人工核验与较窄原始数据，不由留存率或judge规模批准监督正确。<!-- source-family:SF-2026-ARXIV-2606-11127 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11127` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11127v1)§2–4/B–E由reader§37首备，作者实际采用并实读Ch27 owner，2+1+2=5。只原chunk faithfulness/无source quality及修订后资格分责；保14B/8B反侧、同Qwen/训练人口不配平/全费，不采独立充分、回收即效用或通用scale；旧trace不代正文，不迁旧日期。未核实现/复现，PRE/POST待独核。

## A21 FlowBP — 2606.11075v1（reader首备实际采用）

[精确v1](https://arxiv.org/html/2606.11075v1)，2+2+2=6。作者实际采用reader§40的§3–5/A2–4/B/C2必要，不重复Methods/全部D图或代码。无autograd完整Euler缓存state/velocity，active旧state detached重forward而inactive读cache；Sparse可重构原离散endpoint，但backward为截断directsum，Bridge仅一个alpha缩放输入Jacobian，forward同值不等fullgradient/无偏或reward必增。O(K)activation不删O(N)cache、完整25step采样及reward/VAE/encoder重forward费；一个Jacobian深度不等范数全局有界，alpha大仍可退。T4局部endpoint控制有效，不是所有K/权重/预算配平。GenEval Bridge singleobj反退、Sparse整体低于DRaFTLV/position差；学习scorer非人类真值。B明确bf16activation/fp32master/seed42/clip1/8–16H20、512²/25train50evalsteps、250/300iteration/batch64；不凭无wallclock量表编省费。snapshot版本/seed/schedule/CFG是同轨迹前提，跨更新旧cache不是当前rollout。可微reward适用、surrogate bias和原梯度回退保留。

Actual owner `TRAIN-RLHF`：已实际读Ch31 Sequence reward整节的credit接口、21654 costate完整段/完整binding及下一Harm Horizon首段，系统成本完整首两段与状态列表，Ch30/32开篇训练职责交接已读。Costate近似并未承载“采样endpoint身份不变而梯度图主动改变”的接口；具体差额落在21654完整end binding后/Harm Horizon标题前原一段+trueH2本人注，不复制Ch24 sampler数学或写普遍稳定。

### 唯一literal（待PRE/窄授）

连续可微sampler还可将“实际采到哪张图”与“奖励沿哪些路径反传”分开：先无autograd跑完同一Euler轨迹并缓存state/velocity，再只在少量detached旧state上重forward，其余步读取cache；受限[FlowBP分支](https://arxiv.org/html/2606.11075v1)可重构原离散endpoint，却主动截断backward，不能因此称full-gradient等价、无偏或真实reward必升。跨段Bridge只让一次缩放后的输入Jacobian参与，不是任意参数下的范数上界，系数过大仍可退。Activation随活跃点缩小不删除完整采样、全轨迹缓存、reward/VAE与重forward费用；缓存须绑定同一参数snapshot、seed、schedule和CFG，不能跨更新冒充当前轨迹。局部endpoint控制不保证所有composition或推理质量不损，surrogate与原路径须在同质量/全费预算下比较；代理、梯度偏差或净收益不合时，保留原反传、更保守活跃集合或可验证policy-gradient，不由前向同值签发等价优化与无条件稳定。<!-- source-family:SF-2026-ARXIV-2606-11075 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11075` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11075v1)§3–5/A2–4/B/C2由reader§40首备，作者实际采用并实读Ch31，2+2+2=6。只无grad采样/active重forward与backward surrogate分轨，保Jacobian非范数保证、O(N)缓存与采样全费、composition反退及同snapshot限制，不采fullgradient/无偏/普稳。未核实现/复现，PRE/POST待独核。

## A22 ADAS — 2606.10829v1（reader首备实际采用）

[精确v1](https://arxiv.org/html/2606.10829v1)，2+1+3=6。作者实际采用reader§45的§3–7/A–E必要，不重复Methods或F全部表/代码。Eq3每次greedy将candidate→已选token的attention按已选uncertainty折扣；base stopping/cardinality规则不变，固定k控制支持subset内选择的差额，不等adaptive实际reveal数/NFE固定。Eq3不是Eq4有向setutility完整marginal（漏reverse/self），B敏感性近似不证依赖误差上界；仅采用实际规则/局部对照，非一般最优。90点80好10坏/跨相关配置CI非seed，alpha40同HumanEval六点选优，不能授无调参普效。最后层取attention禁FlashAttention；4GH200node、Dreambatch4/LLaDAbatch2、256/512cap/temp0原条件，3.1%perforward归一不是服务SLO；提取、驻留与greedy全费。

Actual owner `MULTIMODAL-GENERATIVE-PARADIGMS`：Ch24 Masked generation首概念、AXON完整段/marker及下一软卷积完整段与独立marker、后entropy22248两段实际已读，Ch23/25开篇交接已读。AXON给未来剩余mask找anchor，entropy规则决定接纳量，均未承载同一批内candidate→selected方向依赖的softdiscount；差额不复制confidence/pace。拟AXON完整marker后/“即使仍使用masked-token模型…”完整软卷积段前一段+trueH2本人注。

### 唯一literal（待PRE/窄授）

即使本轮允许揭示的数量已经确定，也还要选择哪些位置共同提交：逐个取最高confidence可能把相互依赖的位置放入同一批，却仍按旧状态独立预测。一个[受限attention折扣分支](https://arxiv.org/html/2606.10829v1#S4)在greedy选入位置后，按已选位置的不确定性与candidate指向它的attention，软降低后续candidate的分数；原cardinality/停止规则继续负责“选多少”，不能从规则未改推出实际揭示量或总NFE不变。固定k对照支持这项局部选择，但attention不是条件依赖真值，该方向性规则也不是一般双向setutility的精确marginal或最优保证。参数随regime换优，部分运行点质量更差；读取末层attention可失去原FlashAttention路径，矩阵驻留、提取与greedy选择都计费，per-forward均值开销不授服务SLO。依赖代理、质量或净预算不合时，保留confidence排序、较小parallelbatch与原sampler，不由同轮更分散或少forward批准联合分布保持。<!-- source-family:SF-2026-ARXIV-2606-10829 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10829` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10829v1)§3–7/A–E由reader§45首备，作者实际采用并实读Ch24，2+1+3=6。只固定预算内directional greedy折扣，保Eq3非一般setmarginal、规则不变非实际count固定、10负点/参数选择/attention全费，不授依赖真值、一般最优或SLO。未核实现/复现，PRE/POST待独核。

## A23 SmallEP — 2606.10493v1（仅小EP复制/局部归约分支）

[精确v1](https://arxiv.org/html/2606.10493v1)，2+2+2=6。实际必要§2.2.3/Fig2–3、§3.1前提与完整§3.2/Fig6、§4.1/4.2/Fig13–14、4.7/T2及§6直接硬件反侧；没有展开3.3–3.5 overlap/CPUkernel/线程同步全recipe、全部decode实验或代码。已通过gate的是具体SmallEP，不拿五模块组合/Cloud-grade标签准入。

SmallEP先AllGather未排序token使各rank持全[N,D]，各自gate/sort并仅计算本地expert；先把本地expert贡献weighted reduce成[N,D]，再All-to-All这些partial并在原属rank最终归约。不是删除gate、把局部expert算两次或简单AllReduce全矩阵。原文以EP数S不大于每token activeexperts A为有利范围；普通dispatch按top-A复制流量，而本分支复制输入/重复gate来减少combine前的expert维度。印刷N·D“bytes”未带activation dtype，不能直接当字节公式或任意S下流量严格上界；保dtype/布局/实际分片/回传映射并按实测profile选择。每rankgate/sort重复/完整token驻留是真成本，偏斜较小只是所测小EP平均大量experts的经验，不授无straggler。

§2.2.3为20K-token单decoder层CP2+EP2控制，加入SmallEP层latency再降18%（作者数据，不是完整服务SLO）；DSL P1.64x对singleGPU同时有更多GPU/CP和streamloading，不能独归SmallEP。平台2×EPYC9355/24DDR5-6400channels约1.15TB、2×RTX5090/32GB、PCIe无GPU-P2P目标；FP8R1/KimiK2及INT4对照。4K短前缀transfer主导无优势，长>8K KT AMX多为不同原平台估计不能当同机实测；4.7 V3.1/Kimi官方对比少量退分且generation设置不完全同一，只支持有限兼容质量而非bitwise不变。未披露请求arrival/tail统计不补生产SLO。低VRAM少ringbuffer会损transfer重叠、hostDRAM带宽影响decode；复制、gate/sort、packing、partialbuffer/collectives、权重stream全费。未核实现/复现。

Actual owner `TRAIN-DISTRIBUTED-TRAINING`：Ch36 collective语义/AllGather-AlltoAll表、ThunderEP完整两段/marker与其后skew/placement完整两段已实际读，Ch35/37开篇及Ch21门控—分布式执行交接已读。现有hostshared路径/rail重排保持已定logicaldemand，不承载先复制全部token、局部weightedreduce改变需求的窄条件。拟ThunderEP2609-40093完整marker后/“MoE的token→expert skew又…”前原一段+trueH2本人注，不复制Ch21模型数学或其他四模块。

### 唯一literal（待必要/PRE/窄授）

小EP还有一条改变logical traffic而非只选物理路径的分支：当rank数少、每token仍激活多个expert且PCIe交换成为瓶颈时，可先AllGather未排序token，在每rank重复gate/sort，只计算本地expert，再把同token的本地加权贡献先归成一份partial后交换、最终合并。[SmallEP的受限设计](https://arxiv.org/html/2606.10493v1#S3.SS2)用输入复制和重复门控换掉部分按expert展开的dispatch/combine，收益依rank数、激活数与真实拓扑，不是大EP也应复制全batch。完整token驻留、gate/sort、partialbuffer、交换及dtype字节都计费，weightedpartial必须保原token/expert/route和归回位置；局部通信与20K单层延迟改善不签完整服务SLO，短前缀还可能由权重搬运主导。rank增多、稀疏收益不足、容量或质量回归时，保留普通路由后All-to-All与原collective，而不从小EP人口推导任意GPU数、tail或训练反向同样加速。<!-- source-family:SF-2026-ARXIV-2606-10493 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10493` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10493v1)§2.2.3/3.1–3.2/4.1–4.2/4.7/6必要，2+2+2=6。只SmallEP全token复制/本地gate/先weightedpartial的条件交换，保dtype/冗余驻留、20K单层非SLO/短prefix和异平台估计反侧；不授五模块全栈普效。未核实现/复现，必要/PRE/POST待独核。

## A24 miniReranker — 2606.10759v1（reader首备实际采用）

[精确v1](https://arxiv.org/html/2606.10759v1)，2+1+2=5。实际采用reader§48首备§2/3.1/interaction3.2/4主表控制/5/Limit/C2/D3–4/F1，只补actualowner/稿，不重复Methods或扩EE/pruning。Textquery→visualdoc时vision-first产生跨querydoccache；visualquery→textdoc则queryprefix仅同请求candidate间复用，不借前者offline摊销。Instruction/template、model/位置与模态顺序绑定；IB仅在band保有限交互并显式mask适配，不是任意旧模型免训剪掉边。末位直读首段遮61.5→61.0而跨段交互遮→5.5，支持最终读出可不依赖直接首段但中间融合仍必要，不以这组控制授一般因果/所有层相同。VF有GD反退，IB/mini质量损；top100 online预cached<1%非含构建/驻留/刷新全费且非同质量。F1构造曲线只摊销动机，不采用break-even常数。未核artifact/复现。

Actual owner `AGENT-RAG`：Ch76三种文档消费/KV身份、FusionRAG完整两段/marker与下一节完整开头已实际读，Ch75/77开篇交接已读。现有chunk重条件化/privateoverlay不等重排输入顺序来决定何方可缓存，亦无“最终query可间接读融合带但不能全删跨段”的窄反证。拟FusionRAG2601-12904完整marker后/下一主小节前原一段+trueH2本人注，不复制物理KV/分页owner。

### 唯一literal（待PRE/窄授）

重排阶段还应先决定哪一端能成为不变prefix：text-query读visual-document时，visual-first可让文档KV跨query复用；visual-query读多个text候选时，可复用的却只是本请求内的queryprefix，不能承诺同样的离线文档摊销。[受限多模态重排分支](https://arxiv.org/html/2606.10759v1#S3)还保留窄层带来融合两段：最终读出少直读首段不等可以删掉全部跨段交互，显式mask适配及中间融合仍是前提。应绑定model、instruction/template、模态顺序、位置与交互带，保留原文档及重建路径；改变序列或mask会改变模型，不是任意旧checkpoint的免费cache开关。排序质量在部分任务/稀疏配置会下降，预cache后的online时间不含编码、训练、KV驻留/刷新与reader核验全费；复用率、交互质量或净预算不合时，保留完整cross-encoder、较宽交互带或普通重排，不由末位attention稀疏或局部快照签发端到端同质量加速。<!-- source-family:SF-2026-ARXIV-2606-10759 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10759` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10759v1)§2/3.1–3.2/4/5/Limit/C2/D3–4/F1由reader§48首备，作者实际采用并实读Ch76，2+1+2=5。只跨querydoc与请求内querycache资格/窄交互带，保遮挡反侧、显式适配/质量退步和全部cache费，不采预cachedonline为全链或任意免训。未核实现/复现，PRE/POST待独核。

## A25 ASTRA-sim 3.0 — 2606.10440v1（细粒度控制/数据路径与共同拓扑）

[精确v1](https://arxiv.org/html/2606.10440v1)，2+2+2=6。实际必要§3全部、4.1–4.7完整模型/表示/转换及5.1–5.5全部直接案例与限制；未核运行模拟器或代码。Alpha-beta把一次transfer压成固定latency+bandwidth，会遗漏control与data争用，也遗漏kernel共享CU/HBM。新表示将Chakra kernel拆成workgroup/wavefront、Load/Store/Waitcnt/Reduce与semaphoreacquire/release等primitive，MSCCL++ put/get/signal/wait转换为这些操作，在同一GPU/network模型调度。控制polling/ready与实际payload分开，128B cacheline WavefrontRequest走NoC/remote网络；Reduce只是占用可配置cycles，不是完整binary/ISA执行。roundrobin CU与可调驻留、loopunroll/outstanding限制是模型假设，control仅wavefront0且单cacheline，不能自动授任意GPU内存序准确。

InfraGraph以带属性有向图/可复用device/component/link/instance展开成hierarchicalID拓扑，并给Simple/ns3/HTSim translator供共同输入；同graph不等backend全部拥塞/路由/协议语义自动等价。§5明确generic power-of-two GPU仅展示usecase、不验证特定产品：8×4NoC、128CU、1TiB/s NoClink、4TiB/s memory、1TiB/s scaleup/1us，每GPU448endpoint。32GPU reduce-scatter get较优因受控读后可接reduce；16GPU allgather反向，get request被data response阻塞，fairarbitration缩差。这是关键反侧：get/put选择取决于collective与control/data仲裁，不是get消除所有同步的通用律。Unroll/outstanding增大只带宽bound有利且饱和，小latencybound无对应收益。128GPU/57344endpoint、1–256MiB/128B粒度的wallclock证据只是模拟成本/吞吐，非真实训练速度；8GPU 1MB ring/Clos ns3的FCT/无droploss只属该模拟流，不授无丢包硬件/通用生产SLO。没有真实GPU timing校准/errorbar，不能由high-fidelity标签签绝对准确；trace/转换/拓扑标注/参数校准/模拟运行均计费。

Actual owner `TRAIN-DISTRIBUTED-TRAINING`：Ch36 alpha-beta完整公式/变量/“这个模型不是benchmark公式”完整段、其后“通信时间与全网字节效率”完整代数分解/限制段已实际读，Ch35/37交接可复用。现有模型警戒不具体表达cacheline控制请求与payload共用资源可反转get/put排名以及共同输入不自动校准backend。拟“这个模型不是benchmark公式…”完整段后/“通信时间与全网字节效率需要不同账目”标题前原一段+trueH2本人注，与A23 SmallEP不冲突。

### 唯一literal（待必要/PRE/窄授）

当协议差额小到被控制路径决定时，单一transfer的alpha-beta还需下钻：把collective kernel拆成workgroup/wavefront的load、store、等待和semaphore动作，让控制请求与payload按cacheline共同争用CU、NoC、内存和链路。[受限细粒度模拟分支](https://arxiv.org/html/2606.10440v1#S4)显示get可在reduce-scatter中方便读后归约，却在all-gather中因控制请求被data阻塞而落后put，仲裁策略又能改变差额；不能从一种collective推出普遍最佳通信原语。带属性的共同拓扑图可供多个backend转换，仍须核各backend的路由、拥塞和时序假设，图相同不自动证明预测准确。Trace展开、控制/数据参数校准、拓扑转换和细粒度模拟都付费；generic GPU案例与模拟吞吐只支持设计探索，不是实机训练或服务SLO。缺少目标硬件校准、模型过期或模拟成本不值时，保留较粗profile/alpha-beta与实测原collective，不由更细粒度或high-fidelity名称替真实性签字。<!-- source-family:SF-2026-ARXIV-2606-10440 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10440` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10440v1)§3/4.1–4.7/5.1–5.5必要，2+2+2=6。只cacheline控制/数据共同争用与InfraGraph共同输入，保get/put反转、generic模型/未实机校准、backend差异和全费用，不授绝对精度/真实训练SLO。未核运行模拟或代码，必要/PRE/POST待独核。

## A26 FlowTracer — 2606.10646v1（answer可达attention流只是重权代理）

[精确v1](https://arxiv.org/html/2606.10646v1)，2+1+2=5。实际必要§3完整式1–6/Th3.1及3.2遮挡、§4主表/所有直接消融、§5完整限制、C2–3/D2与E1干预设置；未读F全部可视化或核代码。attention跨layer/head聚为时序有向非负图，反向h为到answer sink的weightedpathsum，h>0才以W_ik h(k)/h(i)重归一成outflow1，再从question给单位sourceflow计算throughput；这是给定线性图上的代数守恒，不自动表示真实模型value/MLP/residual与梯度或attention因果。answer区域局部化/零h guard须定义，不能从原文未完整spellout的answerterminal状态补出一般算法证明。实际用中层attention、top40%/gamma1.5重权GRPO surrogate，正负advantage同向放大，不改verifier真值也不是校准contribution。

§3.2/E1 GSM8K随机500、逐句截断前20%token attentionmask再生成，支持该干预下highflow更敏感；不是仅删除一个语义推理步骤，T1“correctness reverse”与E1 correctnesschange方向描述不一，不采精确safe→unsafe/正确变错因果率。D2结构delimiter恢复大多数收益，语义词较小补充；answer格式只是同boxed区域内部变化，不能外推无局部target的工具轨迹。5.3明确wronganswerflow不能鉴别局部有用推理/正确性，PRM可互补。

Qwen3Base4/8B与Llama3.1/3.2有限数学/Countdown/CrossThinkQA，1K/8K；samecriterion控制但40%/gamma/中层经验选优，不是所有regime均衡。T7大gamma/continuousrawflow显著退，top60部分任务低于GRPO，rank较稳不等flow是校准权重。ROLL actor_train Megatron/actor_infervLLM/权重刷新；C3 64prompt×8、lr1e−6、warmup20、500/600step、无KL/entropy、难度/长度过滤。硬件只8/16GPU未指型号、precision/seedCI未详，不补造。C2“disable eager”与attentionmaterialization描述不补为已核实现，采用额外forward+完整attention驻留/flow提取/全部rollout更新收费；T6 2.1–4.5%特定训练step比率非通用低成本。D末peaktrackingEMA本就单调，不由图无跌证明稳定训练。未核artifact/复现。

Actual owner `TRAIN-GRPO`：Ch33 SequenceReward开头uniformadvantage/完整粗糙性说明、CorVer完整后段及其后semanticpooling完整段已实际读，Ch32/34开篇消费交接可复用。既有外部corpus/semanticpooling不承载answer-conditioned多跳h重归一与rank而非数值权重。拟“这比learnedtokenvalue简单…”完整段后/CorVer首段前原一段+trueH2本人注，不复制Ch14attention组件。

### 唯一literal（待必要/PRE/窄授）

没有逐步真值时，还可只把内部交互图当重权提案：将attention聚成时序DAG，先计算各节点到指定answer区域的加权路径量，再在可达量为正处重归一outflow，从question传播流并按throughput挑选少量token，适度放大其原signed advantage。[FlowTracer的受限分支](https://arxiv.org/html/2606.10646v1#S3)保的是这张非负图上的局部守恒，不是真实推理、value/MLP/residual计算或无偏梯度的守恒；通向错误答案的路径同样可得高分，answer区域与零可达guard须显式定义。原流值直接连续重权或过度放大还会损质量，排名与温和离散mask不能当校准因果贡献，结构delimiter的收益也不可改称语义步骤已验证。额外attention前向、矩阵驻留、图计算、调参和全部rollout/更新均付费，选层/比例与snapshot共同绑定；目标区域不清、代理或独立质量回归时，保留uniform advantage、可信process标签及原verifier，不由更细flow批准步骤正确或普遍稳定。<!-- source-family:SF-2026-ARXIV-2606-10646 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10646` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10646v1)§3–5/C2–3/D2/E1必要，2+1+2=5。只answer可达h重归一/flow-rank温和重权，保局部图守恒非因果真值、零h/target、continuous/大gamma反侧及attention全费，不采peakEMA证明稳定或通用无偏。未核实现/复现，必要/PRE/POST待独核。

## A27 Compression and Generalization — 2606.11045v1（两信息通道不能互相代签）

[精确v1](https://arxiv.org/html/2606.11045v1)，2+2+3=7。实际深入§2–3完整条件/Th1/Cor2–3/Alg1、§4–6主结果/限制、AppendixB完整checkpoint proof与C1–3 CI直接证明、D数据/预算、E3隔离与J完整stress/detection协议；不扩Arelatedwork、全部prompt例或复现实验。Output机制：将explorer transcript压成固定B-token消息，仅给fresh reproducer与Dtrain，无旧code/validationAPI；descriptionlength界仅约束固定decoder的reproducer h_m，close agreement不把explorer原模型也变成有formalCI。Input机制：evalharness只回“是否超当前best”1bit，Tmax/Kmax/δj预先固定，runningbest第j改进由firstbit1+共j个1的transcript决定，最多C(Tmax−1,j−1)种，finiteclass union给同时checkpoint界。短prompt与一bit不是单一证书；还需iid有界loss/固定独立随机种子/decoder、Dval只经受控通道到模型，不能把实测实际K/T事后挑作预算。

AppendixB paddedtranscript/固定counterfactual decoder与stratifiedunion已读；C为Bernoulli mean KL-inversion、不是任意MSE/logloss/BPB通用同宽CI，holdout是独立populationproxy非定理直接对象，CI不重叠才支持相应population进步。题名“doesn'toverfit”不作无条件律。主实验8不同任务/同ClaudeOpus三角色，32/64token复现41checkpoint中38过单侧5%relativegap，不是精确等价/100%复现；emptybaseline仅初轮支持知识确实经消息。Laddervs scalar每条件3runs，五classification才采用Bernoulli CI，不能把1bit换算成只泄露一次1bit：整transcript与查询/改进预算共同决定界。

J stress同时改变aggressiveprompt/fullsampleaccess并缩部分Dval/加labelnoise，102checkpoint中38超过10%valholdoutgap，128tokenreproducer5%gap触发38真阳/6其他；这些定义内经验不是单独compression因果、全欺骗/泄漏检测器或部署敏感率。预训练/重用checkpoint污染仍可旁路，Dtrain/Dval独立性未由小holdoutgap证明，未来fresh数据是重开条件之一。CPUtabular/单A100或H100 NLP、8A100/H100vision/LM、单H100diffusion，每train5–10min限时，训练precision未统一披露。Explorer全部训练/查询、compressor及audits、freshreproducer最多3attempt、holdout/harness/隔离收费，短消息不等省全部研究费。未核artifact/沙箱实现或复现。

Actual owner `PLATFORM-EVALUATION-SYSTEM`：Ch66 publicvalidation2604-20200完整两段、limitedprecision feedback2610-28798完整段及下一datawithheld2601-16344完整两段已实际读，Ch65/67开篇owner交接已读。已有噪声门/有限精度不替两端隔离的再实现对象、onebit全transcript预定预算及不同证书边界。拟28798完整marker后/“文件可见性已明确…”前原一段+trueH2本人注；Ch66与Jun12共享活动须root确认此具体肩部，未写Books。

### 唯一literal（待必要/PRE/root冲突确认）

控制反馈后，还可分别检验研究策略是否能离开原验证环境：把探索结果压成预定长度消息，交给只见训练集的fresh agent重新实现；另在探索端只返回“是否优于当前best”一bit，并预先限制查询总数与改进次数。[受限压缩研究](https://arxiv.org/html/2606.11045v1#S3)把两条证据分开：短消息的description-length界只约束reproducer，复现接近原分数不把原explorer也授予同一置信区间；one-bit ladder则按整个受预算约束的transcript，为相应running-best checkpoint给同时界，不是一次反馈少便自动无过拟合。保证仍需iid/有界评价、固定解码与独立随机性、没有文件/预训练污染旁路，不能事后按已见结果挑预算；Bernoulli区间也不直接搬给任意loss。强制开放验证样本的压力实验中复现会暴露部分虚高，但并未验证通用泄漏检测器。隔离、全部探索训练/查询、压缩与重新训练及独立holdout均计费；通道、条件或复现质量不清时，保留原隐藏test/独立复验与Unknown，不由短prompt、低bit数或一个小gap批准泛化。<!-- source-family:SF-2026-ARXIV-2606-11045 -->

本人note唯一稿：`SF-2026-ARXIV-2606-11045` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.11045v1)§2–6/B/C1–3/D/E3/J必要，2+2+3=7。只output再实现与inputladder两证书分责，保固定预算/decoder/iid/旁路条件、Bernoulli范围、stress复合干预与全部费用，不采原explorer由复现获CI或通用泄漏检测。未核实现/复现，必要/PRE/POST待独核。

## A28 Dynamic Linear Attention — 2606.10650v1（reader首备实际采用）

[精确v1](https://arxiv.org/html/2606.10650v1)，2+1+2=5。作者实际采用reader§52的§2必要定义/§3全部机制/Alg1–2/Th3.1与Cor3.2完整证明及§4主表/全部直接控制；不重复Methods/图像素/代码。有限接口为信息变化proxy决定沿当前summary累计或新开chronologicalstate，capacity满时只在相邻states按(sumscore)/(sumcount)挑最低对有损merge，state/count/score共同累加，query以受训权重读取。这是学习过的有损状态协议，不是任意旧KV免训淘汰或固定K条便无限恢复。误merge不可逆，信息score非语义真值。

正文与Alg1高变化token是否先Merge再append、score定义Eq13/15以及Alg2是否包含Eq18 querylambda不闭，当前不拼合执行recipe。Th3.1只是heterogeneity上界，Cor3.2比较特定跨changepoint的bound不证明真实误差更大/所有fixedpolicy差，更不证明proxy正优化该bound；不采用普遍优越或完整Mamba/Delta等价。4A100/50B从零训练/16K、Mamba780M和Delta1.3B、K30，单A100效率prefill+1decode非长服务SLO；T1/T5数值冲突不抄统一涨幅，RULER部分弱Transformer/FDA0，K40或阈值变化可退。precision/seedCI未详不补；score/RMSNorm、相邻搜索/搬移、readweights与训练回归全费，不因普通公式recipe缺口泛H。

Actual owner `MODEL-LONG-CONTEXT`：Ch22固定状态/任意细节边界520、linearstate概念与“在固定状态与完整历史之间选择保存粒度”首完整MemoryCaching段、后31367完整段及远期bank完整后两段已实际读；Ch21/23模型—模态边界已读。固定间隔可增长slots与按访问图剪cache没有替代给定K下动态边界/相邻merge及countscore共同恢复的接口。拟MemoryCaching首完整段末“没有productionkernel、迁移、租户隔离和端到端SLO证据”后/“保存粒度还可由递推访问图决定…”前一段+trueH2本人注。

### 唯一literal（待PRE/窄授）

状态条数若还要固定，就必须说明边界怎样形成、容量满后丢掉什么，而不能只缩短checkpoint间隔。一条[受限动态state分支](https://arxiv.org/html/2606.10650v1#S3)用信息变化proxy提出继续当前summary或新开一份，满额时只在时间相邻的states中选择低score/count对合并，并共同保存summary、token计数、累计score与顺序，再由受训query读权消费。给定K约束的是条数，不是任意细节可恢复；误merge不可逆，proxy或heterogeneity上界都不认证语义保真与真实误差最小。训练softgate与推理hardboundary需共同验收，原算法/公式未闭部分不拼成通用执行recipe；更多state或更激进阈值也有质量反退。边界评分、相邻搜索/搬移、读权、全部训练与回归均付费，单步decode效率不是完整长生成SLO；状态语义、质量或净费用不合时，保留固定边界、单state、显式历史或原hybrid，不由动态分段批准无限记忆与普遍更优。<!-- source-family:SF-2026-ARXIV-2606-10650 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10650` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10650v1)§2–4/Alg1–2/Th3.1/Cor3.2由reader§52首备，作者实际采用并读Ch22，2+1+2=5。只动态边界/相邻有损merge/计数score顺序共同恢复，保recipe未闭/bound非实际优越、K/阈值反侧与全费用，不授无损/免训/服务SLO。未核实现/复现，PRE/POST待独核。

## A29 KATE — 2606.10875v1（经验粒度与当步候选宽度的受限对照）

[精确v1](https://arxiv.org/html/2606.10875v1)，2+1+2=5。实际必要§3–4完整机制/主表/消融、Alg1–2、Limitations、D1–2/E/F直接配置与反侧；未深入G训练全recipe、B/C全部prompt例或代码。准入对象不是检索+parallel+SFT/RL组合，而是instance/ST原轨迹或ES具体summary对intent脚本/文字、width候选对强制intent/reflection/state hint的受限选择。ST/ES相近且任务/model换优，intent推断/抽象可能丢细节；allknowledge叠加并非普增。Hint可退，parallel在每个真实history状态提出候选，经一致或聚合仅执行选定call，Alg1不是先对环境执行四份副作用；其准确不替授权/幂等。§3.3把width写depth与前后Alg不符不照抄术语。

BFCLV3每scenario200，相同taskdescription但环境动态不同；训练100Base、按even/odd sampleID拆分，非完全tasktemplate语义隔离。Base训练GT经验是监督而非无teacher；AppWorld90train中81GPT4o正确示例建库，按TestN/C执行state/unit checks。Qwen3 8/32B有限两benchmark，MiniLM检索/相关toolset先限域、threshold.5、topK/dedup；同描述和已知toolset限制未见新工具迁移。T1 32B MissP无PS48>full42、noExp MissF48>full41等反侧，T2 AppWorld32BTestC TGC ST8.6>full7.4、SGCMemp1.4>full.7；LlamaF knowledgeonly12.75>full11.25，不能授width总好/能力上限已证。D单run声明与F新增两seed mean/std同时存在，保主表与三seed口径分开，不造全single/noCI；结果相关seed不外推全部scales。

E仅10Base点cost，8Bfull1.894x tokens/815vs332time，32B1.294xtokens/529vs584，selfconsistency比LLM聚合可更便宜，不能说小额开销或samebudget优于depth。A800/A100/vLLM最大multithread、T0vsparallelT1/N4同时变化，不隔离纯width；precision训练不借推理补。全部GT/经验summary与intent建库、embedding/filter、候选sampling/聚合、真实调用及训练回归付费。judgegpt5mini error分类不是因果成因。保普通schema/docs、较窄可信实例及N1；未核artifact/复现，不采用组合一体化普效。

Actual owner `AGENT-TOOL-CALLING`：Ch78 ToolContract完整首概念/参数与最小权限/显式文档模板段、ToolDiscovery标题/下一CIPR完整两段已实际读，Ch77/79交接已读。工具schema/skill抽象与接口一致性未承载在相同可执行任务上选实例级经验还是抽象intent、当步宽采还是强制深提示的经验反侧。拟ToolDiscovery主标题后/“接口一致性要比较等价动作…”子标题前原一段+trueH2本人注，不把经验授予runtime权限。

### 唯一literal（待必要/PRE/窄授）

工具已可发现时，仍要决定给模型何种经验以及怎样花当步推理预算：在同一任务上分别比较具体成功trajectory/局部操作summary与抽象intent脚本，另比较强制逐项反思提示和从同一真实history提出多个候选再聚合。[受限tool-use对照](https://arxiv.org/html/2606.10875v1#S3)中具体经验常比抽象intent更有效，额外深提示亦可退，但这不证明实例永远更好或更多候选总获益；更难任务和部分模型中knowledge-only/其他聚合仍可更强。候选只是proposal，选定后才执行一个call，不允许用sampling名义并发真实副作用；权限、参数和幂等继续由原executor验收。经验来自训练GT、同模板拆分与已知toolset过滤仍限制迁移，温度与候选数变化也不是纯width因果。建库/检索、全部候选与聚合、调用和独立回归均计费；经验支持、质量或净预算不合时，保留原schema/docs、较窄可信示例和单次选择，不由更长解释、经验数量或总体均分批准可靠执行。<!-- source-family:SF-2026-ARXIV-2606-10875 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10875` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10875v1)§3–4/Alg1–2/Limit/D–F必要，2+1+2=5。只instance-vs-intent与当步width-vs-hint的受限对照/仅选定call执行；保hardtask/knowledgeonly反侧、温度预算/同模板GT/seed口径与全费，不授组合普效或权限。未核实现/复现，必要/PRE/POST待独核。

## A30 JANUS — 2606.10852v1（固定fact池不等平衡呈现或真实说服）

[精确v1](https://arxiv.org/html/2606.10852v1)，2+1+3=6。实际必要§2全部定义/式1–8/构造、§3主表/分域、§4–5限制、D1–3完整prompt/judge/人审与E配对signflip/BH；未读F全部qualitative或核artifact。160构造场景/8domain，每份3favorable+3adverse六facts，同人设/同shuffle输入neutral vsgoal。准入窄差额是固定事实支持后，selection覆盖几乎不变仍可ordering/framing改变；不因此认证每输出无新增假fact，更未测真实人类决策/说服。Neutral要求onlyprovidedfacts但goal prompt改role/受众/组织目标且没有同句限制，不能把差额唯一归单个latentgoal或诚实性；角色/约束组合是实际干预。

五metric各自有代理边界：selection按match事实数，emphasis按句token均分给多facts，不等认知注意；ordering分母全部正负factpairs，遗漏也会提高1−adversefirst，不能看单维就断定真实顺序全变；specificity仅数值set交集不核单位/主体绑定，framing读matched句/事实/极性/goal的Qwen3-8B分−1/0/1，不测读者netimpression。主Table2ordering/framing明显而selection接近0支持联合诊断盲区，不能排除matcher漏配或事实外输出。所有facts由GPT5.5生成/作者修订，20场景双作者校准κ.87后分工+flagcrossreview，是合成场景label非外部事实真值。

D matching人工100unit=600binary决策一致587/600，present54/65召回漏11，highoverall有absentmajority；framing100按Qwen标签33/34/33抽，exact79/100、κ.685，非自然全人口无偏准确率。SameQwen系自评可能共偏，少量人审不授所有模型句标签真值。E itempaired 200k signflip/60tests BH，signexchangeability为条件，mean0本身不推出该对称；无重复seed/采样不确定性不可由跨item检验抹除。平均五维native尺度不同仅描述不能作统一风险/能力排名。

D模型/默认API+本地bf16，70B4bit/batch1、Qwen8batch4/14batch2/32batch1，thinking只finaloutput；API deepseek-chat/reasoner不独立锁精确V4版本/检查时间，主8B与70B混精度/资产/训练，不能推规模或thinking因果。D1本地singleA10080GB已披露，API后端/完整API版本/seed未详不补造；构造/验证/配对全部生成、matching/framing、人审与统计均计费。§5明确singleturn constructed/equalaggregate/nonvalidatedweighting，不外推自然沟通、真实危害/缓解已实现。未核实现/复现。

Actual owner `PLATFORM-EVALUATION-SYSTEM`：Ch66 18280完整probe前段与完整outputacceptance/framing直接段、下一26242完整后段已实际读；现分母/硬拒答警戒没有固定fact pool下coverage与呈现方式分离的配对诊断。拟“输出验收随后保留全部请求…”完整段后/“当评价目标本身来自hiddenstateprobe时…”前原一段+trueH2本人注；Ch66共享先root精确确认，不改原18280断言。

### 唯一literal（待必要/PRE/root冲突确认）

事实覆盖通过后，还可固定同一份正反材料、受众与输入顺序，对比中性任务和带组织角色/目标的呈现，分别核是否遗漏、分配多少文字、先说哪类事实与怎样措辞。[JANUS的受限配对](https://arxiv.org/html/2606.10852v1#S2)中覆盖变化很小仍可伴顺序与framing移动，说明“提到了全部fact”不足以批准平衡表达；但固定输入不认证输出没有新错fact，角色/目标/约束共变也不识别单一动机，更未测真实读者被说服。句fact匹配和framing judge是需人审的代理，数字set保留不证明单位/主体绑定，遗漏还可能混入ordering分数；应保逐fact对应、原始回答、各维分母与配对条件，不能只报五维平均。场景构造、全部配对生成、判分/人审和统计均付费；材料极性、judge或真实受众效度不足时，保留人工逐项核对与明确Unknown，不由字面覆盖、一个均分或参数规模签发沟通忠实与安全。<!-- source-family:SF-2026-ARXIV-2606-10852 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10852` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10852v1)§2–5/D1–3/E必要，2+1+3=6。只固定fact池coverage与呈现分离；保role/goal/限制共变、匹配/分母/合成标签及signflip条件、API身份与全费，不授字面全真/真实说服或规模因果。未核实现/复现，必要/PRE/POST待独核。

## A31 Metaprogramming — 2606.10933v1（reader首备实际采用）

[精确v1](https://arxiv.org/html/2606.10933v1)，2+1+2=5。作者实际采用reader§66的§2/3.2–3.5/4、A1–4/A6–12、B6–7与G2必要，不重复Methods/C全部代码/F全部示例。可支持熟悉hostlanguage先显式表达cell/pointer/BCD/branch状态、生成陌生目标source、测试后改generator再生的接口；同sessionhelper复用非外部旧解。G2 genericlibrary额外给primitives/allocator与Befunge simulator/notes非perproblem已解源码，TextvsLib Sonnet/mini提高而Haiku不动；有可执行helper不是任何模型都能正确组合。

No-meta的A12同时去bash/可执行host工具+限扩展名，不是纯删除内部策略，其余固定的宣传收窄；token效率仅前20题观察性output含thinking计数，不是随机额外tokens因果。固定80题4tier按顺序同workspace可复用、每题3hidden且一次6/6才solved；A8 3local/1hidden另协议，不混。§2 aggregate与A12 pertest反馈不一，G onehidden不替主3hidden；不授已核隐藏隔离。Headline单session，额外session sanity与ablation两session均值不同；B6序列正相关使Wilson/bootstrap不认证iid覆盖，低公开频率不证训练无污染；KimiK2.5表述对identifier kimi-k2-thinking不补资产。全部hostgenerator、generichelper、解释器/sandbox、测试/hidden反馈、tokens与回归计费，未核artifact/复现。

Actual owner `AGENT-TOOL-CALLING`：Ch78 Agent-friendlytool完整概念/typed计算链与两完整后段、下一ResourceLowering完整问题/authority链已实际读，Ch77/79交接可复用。确定性工具与已审checkedlowering不替模型先造hostgenerator再生成陌生语言目标的提案层，以及文字建议vs可执行helper可用性的条件差额；不自称该生成器已被独立形式验证。拟Agentfriendlytool末“这与RAG是PrincipleReuse…”完整段后/ResourceLowering主标题前一段+trueH2本人注。

### 唯一literal（待PRE/窄授）

目标语言陌生时，工具还可让模型先在熟悉host language中显式维护分配、指针和控制状态，再由generator生成目标source，测试失败后修generator并重新生成，而不每次手补脆弱目标文本。[受限陌生语言对照](https://arxiv.org/html/2606.10933v1#S3)支持把可执行generic primitives/helper与纯文字建议分开提供和验收；有库不等所有模型会组合，也不把生成工具变成语义正确性证书。禁metaprogramming的控制同时减少bash/host执行权限，不能把全部差额唯一归内部策略；观察到outputtokens相关亦不是额外预算的随机因果。Generator/helper、目标语言解释器、版本/测试及跨题复用状态共同定义资产，所有构建、测试反馈、生成与回归都计费；状态映射、兼容或净效用不足时，保留直接编写、可信编译链与独立测试，不由helper存在或少量hidden通过批准任意DSL与生产正确性。<!-- source-family:SF-2026-ARXIV-2606-10933 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10933` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10933v1)§2/3.2–3.5/4/A1–4/A6–12/B6–7/G2由reader§66首备，作者实际采用并读Ch78，2+1+2=5。只hostgenerator/目标source分责与textvs可执行helper，保权限共变/观察tokens非因果、hidden/相关session及全费，不授内部唯一原因/形式正确性。未核实现/复现，PRE/POST待独核。

## A32 MemVenom — 2606.10742v1（reader首备实际采用，仅防御接口）

[精确v1](https://arxiv.org/html/2606.10742v1)，2+2+2=6。作者实际采用reader§70的§3.1–3.2/4全部直接主表/控制、A/C/D/E1–2/E4–5/H Alg1必要，不重复Methods/F全轨迹/OCRrecipe/code，不写攻击操作。graph memory里被直接召回的visualcue可沿边扩展未单独topK命中的goal/priority组件，召回集/扩展集/实际输入集需分账；相似度触发不授读取后指令authority。R/conditionalP(A|R)与jointP(R∩A)不同，R>0才有条件率；Ret0行ASRa94.12不当实际零召回条件概率，无Pri仍75.18不说三模块各绝对必要。

Threat memory写权限与triggerbearing observation出现不同，原blackboxvictim仍用imageencoder/surrogatememoryoptimization，不由conditionaltrigger结果推memoryonly自动大规模激活。E4 browser/server/statecheck支持localhost示范credit/canary/placeholder目标，不等真实支付/泄漏/删除。三framework共享同recall/Qdrant+Kuzu接口非三独立原生memory；BU/PU QwenVLjudge且T2部分退，不能授正常utility不损/隐匿已普证。两个轻防御不推provenance隔离/可信scope gate全无效；CI/样本/全硬件precision与优化API费用未详不造。所有建库/图扩展/embedding/影像读取、source核验与独立action验收收费，未核实现/复现。只采用防御闭包接口，非万能防御保证。

Actual owner `AGENT-MEMORY`：Ch77 poisoning完整write→persistence→recall→adoption→externalconsequence→selectiverepair链/完整checkpoint说明/Repair双目标段及后prooftrace首段实际读；GraphMemory关系provenance1837完整两段/marker亦实读，Ch76/78交接可复用。旧链分关有效，但relationcanonicalization写入侧没有实际列出visualcue召回后沿图暴露的扩展消费集，低topK召回不自动封住另一组件。拟checkpoint末“Workflow层必须继续验证authorization、实际sideeffect和恢复证据”完整段后/Repair双目标前一段+trueH2本人注，保旧链不重复攻击recipe。

### 唯一literal（待PRE/窄授）

图记忆还会把直接召回扩成另一份消费集合：visual cue命中后，关联边可把没有单独进入Top-K的文本或优先级记录一并交给模型。因此要分别保存直接hit、沿边展开与最终policy实际读到的内容，并在读取后继续核谁有指令authority，而不是只按节点命中率验安全。[受限多模态poisoning证据](https://arxiv.org/html/2606.10742v1)支持这一闭包风险，但激活依赖trigger-bearing观察与已有写权限，conditional成功不等自然出现率或只写记忆便能任意触发；本地沙箱目标也不代表真实泄漏/付款。隔离与修复需追关联节点/edge、派生文本和原source，另验必要benignmemory，不能靠清空库或提高相似阈值自签完整防御。图展开、影像/embedding读取、来源回核与独立action验证均付费；来源、边闭包或scope无法核实时，隔离相关条目并保留原无外部记忆/可信context与executor权限门，不让跨模态相互一致或可达性取得新authority。<!-- source-family:SF-2026-ARXIV-2606-10742 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10742` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10742v1)§3–4/A/C/D/E1–2/E4–5/H由reader§70首备，作者实际采用并读Ch77，2+2+2=6。只直接召回/graph扩展/实际读入闭包与adoptionauthority分关，保条件人口/trigger权限、localhost非真实损害与benignutility/全费，不写攻击recipe或万能防御。未核实现/复现，PRE/POST待独核。

## A33 Query Recycling — 2606.10709v1（零方差是当前policy的随机观察）

[精确v1](https://arxiv.org/html/2606.10709v1)，2+1+2=5。实际必要§3.4全部pool规则/式1–3、3.2–3.3环境/SFT前提、4完整主表/直接消融、5/Limitations及B全部softrecycling，未扩3.1所有querygenerationrecipe/A全图或代码。K个条件独立binaryrewardrollout时Pzv=p_t^K+(1−p_t)^K；当时全对/全错只是有限group观察，policy改进或漂移均可使其重回mixedoutcome。Recycling保留此前未贡献gradient的题供后续重新rollout，仅移除已被选入实际update的signalbearing题，过量mixed但未消费也保留；k有界oversample与后续资格分开，不改advantage真值。B明确未抽题keep prior weight，故§3.4简式else1不解读成每步把全部已消费题复活；本次不重构代码，保存currentpool/consumedset/behavior版本是协议要求。

条件iid不覆盖相关rollout/judge误差，较大K更少zv不证题固有难度；samepolicy也可能仅resampling已恢复mixed，观察rescues不能全归真实能力增长。Qwen3 1.7/4B、sameSFT6.3k/GPT4.1mini teacher、10k英文ClueWeb22 RLpool，B32/K4/k1或2，fixed84.5ktrajectorybudget，660vs330updates非等optimizerexposure/tokens/工具费。k2对k2控制支持recycling局部收益，但T2 1.7PopQA54.2<GRPO54.4，4BMSQ41.3<B-DAPO41.8/Trivia89.9<90.8，不授全task普胜。K8更费只此配置；softalpha.1未扫不证明binary最优。Eight inference Pass1 runs/SE不是重复训练seedCI；train DRGym→test liveSERPER、GPTjudge共享/时间变化，priorwork多数据和模型/复现协议不完全同，不作全面7B优势。硬件precision/完整wallclock未详不造，fixedpool枯竭/信号比例变小仍限制horizon，online生成/denserprocess组合未实测。所有失败/弃rollout、重评/维护、teacher/SFT/RL和live工具/评价费用独立，未核artifact/复现。

Actual owner `TRAIN-GRPO`：Ch33 zero-variance完整式/说明、2602-06375 admission完整两段及DAPO dynamicfilter/更新分布完整段实际读，Ch32/34交接可复用。现有coverage回查与动态补采没有将“本次未有差分”与“已消费过有效梯度”变成跨step不同pool资格；不是仅复述zero variance。拟06375完整两段末“质量或代理校准失准时停止过滤，继续以真实组reward更新”后/下一Pareto探测段前一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

零方差还不应被永久写成题目标签：同一题在有限group里全对/全错，是给定policy和采样预算的一次观察，后来能力变化、漂移或仅重采样都可能重新产生差分。[受限query-recycling分支](https://arxiv.org/html/2606.10709v1#S3.SS4)因而将此前没有贡献更新的题保留在activepool，只有真正选入update的signal-bearing题才消费掉；有界过采样负责本轮多看多少，pool资格负责后续还可看谁，不能混作同一预算或在线难度真值。需保存pool/consumed身份、policy、group和实际消费记录，失败与过量未用rollout仍付费；匹配trajectory数不等tokens、工具调用或optimizer exposure相同。较多rescues不独立证明能力增长，固定pool也会逐渐失去信号，局部收益并非各任务单调。判分、人口或净预算失配时，保留原mixed-group补采、随机coverage与普通epoch计划，不由一次全零永久删题，也不由循环重试承诺无限有效学习。<!-- source-family:SF-2026-ARXIV-2606-10709 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10709` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10709v1)§3.2–3.4/4/5/Limit/B必要，2+1+2=5。只零方差未消费与已消费signal题的跨step pool资格，保iid/resampling混杂、matchedtrajectory非全费/updates、局部反退与枯竭，不授固有难度/无限horizon。未核实现/复现，必要/PRE/POST待独核。

## A34 Continual Upcycling — 2606.10722v1（局部FFN门控可伤readout而非全部记忆）

[精确v1](https://arxiv.org/html/2606.10722v1)，2+1+2=5。实际必要§3完整bank/predictor/softsurrogate与硬件限制、§4训练条件、§5主表、§6.1/6.2直接负侧和AppendixB完整phase/token/taskrepair；未展AppendixA完整200Mrecipe或代码。每层低秩predictor用64channelbank内top16再sigmoidgate替换nativegate，hardforward/softsurrogatebackward经LM训练；0.26B额外参数、dense从零8T8K再4T32K阶段晚期接入，sparseweightdecay.06vsdense.1，不说任意开源dense模型一键/纯门控单变量。GPU实际仍算denseup/gate后mask，只主要downprojection能稀疏消费；ideal4xactivechannels非实测4x端到端。

拟采用是具体负面/修复：整体RULER/短任务接近dense仍可能在CWE12–16K出现cliff；单层7 normcalibrateddensefallback在prompt预处理、特别末Q&A后缀可恢复部分CWE，而decodeonly弱。B50独立随机任务seed按512步扫长度，不是50trainingruns。B NIAH稀疏.7136→final64repair.7111未改善，CWE局部修复同时MMLU.702→.628/.632；最大长度仍明显弱dense，不能称general longcontextfix/全部记忆恢复/唯一层普适。Sameunitintervention支持routing相关狭窄读出假说，不证全部内容早已正确存储。Channelbalance两bias未优于none只此continualstage，不从FFN细粒度通道推expert-levelbalance无用。

T2 AIME24/25、LiveCodeBench/SimpleQA等稀疏也可弱dense4x，不用平均loss签全能力；训练总费用/硬件precision与matching细节未详不造，收益和0.26B/不同WD/新增训练曝光分账。Predictor/归一/topk、索引/gather、校准densefallback与任务双侧回归付费；原dense、较轻稀疏或不启该fallback继续合理。未核代码/复现。

Actual owner `MODEL-FFN`：Ch16 SwiGLU完整gate/维度/成本概念、2509-00454完整activation稀疏段与独立marker、后2605-01973条件gate完整段已实际读，Ch15/17开篇交接已读。现门控零比例/实际省算不替单层prompt后缀routing对CWE/NIAH/短任务的相反结果。拟00454独立marker后/“当同一基础模型要随任务…”条件activation段前原一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

稀疏门控的验收还需按层、phase与任务拆开：一个受限bank-wise分支为每层增加低秩predictor，在固定channel bank内只保部分通道，hardforward配softsurrogate继续训练。[局部fallback对照](https://arxiv.org/html/2606.10722v1#S6.SS2)中，短任务和整体长窗均值接近dense，仍可在特定长CWE读出出现cliff；只将一层的prompt末问答后缀换成校准denseactivation，可救回部分CWE，却不修NIAH且伤MMLU，不能把它叫恢复全部记忆或通用长窗补丁。应共同记录predictor、bank/mask、layer、prefill/decode与校准人口，分别验远程检索、局部读出和短任务；GPU若仍先算denseup/gate，activechannel少也不省这两项投影。预测/选择、稀疏布局、额外参数/训练、fallback与双侧回归都计费；读出、质量或真实省算不合时，保留原dense/较轻稀疏和不启局部修补，不由较低loss、平均稀疏率或一个召回恢复点批准能力保持。<!-- source-family:SF-2026-ARXIV-2606-10722 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10722` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10722v1)§3–6/B必要，2+1+2=5。只bankpredictor语义/局部phase后缀fallback及CWE-NIAH-MMLU取舍，保密集upgate仍付费/额外参数WD与全费，不授全记忆恢复/4x墙钟或expertbalance无用。未核实现/复现，必要/PRE/POST待独核。

## A35 SSR-Merge — 2606.10617v1（经验二阶路由不自证单步全域充分）

[精确v1](https://arxiv.org/html/2606.10617v1)，2+1+3=6。实际必要§3完整式1–15/Th3.1/Alg1、§4主协议/主表/消融代价、G1–3 calibration反侧及H1–4完整统计证明；未展C/D/F全扩展任务或全部qualitative像素/代码。Acomb按任务stack/Bcombconcat，rankr→Kr，按taskcalibration的Z=AcombX累加GramG与taskblockguideQ，R=QG^-1并可fold进B。G/Q可流式累加，节省rawfeature驻留但每LoRA层仍需统计平方空间，K/r增大付费；非数据自由/免费无推理校准。合并后fixeddenseweight无单独router，不等保留Kr未foldedLoRA与单r执行开销相同，所谓zero latency限吸收后路径，不是全部发布成本为零。

理论精确收窄：§3.3 Eq6“Bcomb†Bk=Ek”一般不成立（例如Bcomb=[b,b]，两block的pseudo投影均半权而非选择），除非适当fullcolumnrank；不采用该逐block等式。拟采有限层线性回归不需该错误中介：由Q的block定义可直接得BcombQ=ΣYkZkᵀ，若Gram可逆，BcombR就是目标Y对Z的OLS，因此只校准样本上的线性outputMSE最小，不是全生成分布、任务质量或无干扰。作者证明里outputprojection归identity并不使one-step代表所有timesteps。H完整推导需可应用统计集中、wellconditioned population Gram λmin≥μ>0及经验扰动≤μ/2、crosscovariance界；相关token数N≫Kr本身不确保独立有效N、非奇异或良态，更不保证单prompt/timestep普遍足够。G有限FLUX K9一/多step及K3五模板/五seed对照只局部鲁棒。

FLUX1dev/A100、10DreamBoothsubjects/r32/lr1e−4/500step，各LoRA训练/校准费用另付；single独立subject oracle不等真实上界，DINO/CLIP对训练reference不是人审真值或全能力保持。K9保留90%左右仍有损，不称无损；Composition100prompt/K2–4 GroundingDINO最高confidencebox/未检出零，allKdetected不是精确身份/空间/安全证书。FFHQ400train/100test软件顺序editreference非自然真值。T2 mergeK9 34.26s快TIES却慢DARE20.95，不把stage费当端到端省费。G5seed只K3、未披露完整generationprecision/batch/SLO不补；统计/校准/求解、rank资产/fold、原LoRA训练与独立多任务回归全计费。未核实现/复现，不因错误中介扩大H到可独立核的有限OLS接口。

Actual owner `TRAIN-LORA`：Ch30“多个Adapter能否直接相加”与开放池admission完整段、跨backbone谱兼容完整前后段已实际读，Ch29/31开篇交接可复用。现兼容/功能coupling门没有按taskcalibrationGram/guide进行固定层路由的接口，正好承接相加前提。拟“多个Adapter能否直接相加”主标题后/开放池CompositionAdmission子标题前单段+trueH2本人注，不改原跨base/权限链。

### 唯一literal（待必要/PRE/窄授）

同基座adapter直接相加若仍相互干扰，可把各down-projection纵向stack、up-projection横向concat，在这份Kr维空间内按各任务校准特征累积Gram与taskblockguide，再求固定线性router并吸收进up-projection。[受限二阶路由分支](https://arxiv.org/html/2606.10617v1#S3)在Gram可逆时可匹配该校准人口的线性output最小二乘，却不由层内MSE最小推出全生成任务无冲突。相关token很多不保证Gram良态、独立有效样本或单prompt/单timestep全域充分，原文逐block伪逆选择等式亦不能一般沿用；需保存任务/层、校准prompt与时间、统计精度、条件数和真实合并资产。流式统计省rawfeature驻留，不免每层平方统计、求解、原LoRA训练和多任务回归，Kr资产未fold时也不同于单r部署。校准支持、数值或质量不合时，保留分离adapter、原相加/可信选择与更多校准，不由training-free或router可fold批准无损、零全费或普遍最优。<!-- source-family:SF-2026-ARXIV-2606-10617 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10617` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10617v1)§3–4/G/H必要，2+1+3=6。只taskcalibrationGram/guide固定层路由/可fold，保Eq6非一般成立而直接BQ关系可核、Gram/统计支持/相关token/单步限制、rank与全费，不授全生成无冲突/单步全域充分。未核实现/复现，必要/PRE/POST待独核。

## A36 CLP — 2606.10935v1（reader首备实际采用；非exact分支）

[精确v1](https://arxiv.org/html/2606.10935v1)，2+1+2=5。作者实际采用reader§76的III相关MTP/nativeHead0比较、IV完整机制/Eq2–7/Alg1、V所有主表/thresholdquality控制、VI完整局限/费用/内存；不重复Methods或引用对照原系统裁决。每轮nativeLMargmax给当前prefix anchor、同hidden MTP提出后续span，CLP从固定hidden预测连续正确span长类别，以maxclassconfidence阈值控制接受量；不是逐token targetverify，最大类概率不是整段正确率。未验证bonus改变后prefix，只有每轮L0或额外每token实际吻合target才保greedy轨迹。明确不采用zero-loss/exact/unconditionalclaim，但窄spanproposal机制不因经验局限泛H。

WikiText2 max128/20ktrain与1000validation同时CLPtrain/eval，15生成prompt TPS/3gram重复率<.02及未量化manualinspection不证任务/事实/长窗质量；highτ可慢greedy，k4CLP1.166略弱singlethreshold1.168。Eq5 k(d+1)与k2参数4611vs应3074、head编号/accuracy.58/.64对表.14–.18不统一，不拼完整recipe/新数字；0.5/1.5/7Bint8与72B估计非规模因果，EAGLE-style自制head非原系统公平对照。236M两head/1.5B16%fp16额外参数等同费用不能用CLP小linear层忽略；RTX3090训练75+5+3min不借推理硬件/precision/batch/SLO。离线label/hidden提取、head训练/logits、KV/prefix更新与threshold调参/全质量回归均付费，未核artifact/复现。

Actual owner `INFER-SPECULATIVE-DECODING`：Ch48“它不是近似替代”完整效用仲裁首段、distributedtoken/hidden verify完整段、后声学草稿两级仲裁完整两段已实际读；Ch47/49开篇交接已读。已有draft优于target的utilityroute不等nativeanchor+未验证bonus以lengthclassifier门控的非exact分支；不放进exact接受证明内。拟该效用仲裁首完整概念段后/“草稿与target分在端侧…”分布式verify完整段前一段+trueH2本人注。

### 唯一literal（待PRE/窄授）

即使每轮第一个token仍来自原LM head，也不能据此承诺额外span无损：同一hidden上的MTP可提出后续tokens，再由长度classifier及confidence门决定接纳多少，但未逐个target验证的bonus一旦提交，就改变下一轮prefix。[受限CLP分支](https://arxiv.org/html/2606.10935v1)因此应标为近似spanproposal，而非exact speculative decoding；最大类别概率不是整段正确率，只有退到零bonus的原AR或真正验证吻合的路径才保相应greedy轨迹。Classifier训练/校准人口、head与backbone、阈值和KV更新要共同绑定，少量prompt的TPS/低重复率不替独立任务质量；保守阈值也可能比原AR更慢。全部hidden/label制备、MTP与gate训练、额外参数/logits和质量回归均计费；误差、校准或净收益不合时，保零bonus原AR或已验draft-and-verify，不由native首token、轻classifier或zero-loss名称签发完整生成分布与生产加速。<!-- source-family:SF-2026-ARXIV-2606-10935 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10935` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10935v1)III–VI由reader§76首备，作者实际采用并读Ch48，2+1+2=5。只nativeanchor/lengthgate额外span的近似接口，保未verifybonus改变prefix、confidence非整段正确、验证复用/有限TPS与全head费，不采zero-loss/exact。未核实现/复现，PRE/POST待独核。

## A37 SpenseGPT — 2606.10445v1（可被现成GEMM消费的区域与剪枝顺序）

[精确v1](https://arxiv.org/html/2606.10445v1)，2+2+2=6。实际必要§3完整表示/式1–13/选择与SparseGPT先后、§4.1–4.2.5完整配置/主表/速度与全部直接消融、Limitations；未核code或图像逐像素/复现。将MLP共享intermediate索引分为dense与2:4两区，up/gate按outputsplit将结果拼合，down按inputsplit对同outputaccumulate，避免activationexpand与专用混合tilekernel。选择可以不连续，部署前共同置换up/gate行和down列成连续区域；数学未剪枝置换保函数，不说明重新选择2:4 groups与有损pruning后也等价。denseindices置右/back再SparseGPT左→右重构，使其保留作compensationbuffer，是训练产物构造顺序，不只是运行时随便layout。T5相同selectedindices留原位或前移质量大退支持这项条件，不证明所有剪枝器都右侧最佳。

SpenseGPT+三投影Wanda-style独立评分/归一后合成top-p，proxy不精确求组合最优；Eq5 floor(pN)到N对文字“最后p%”数量不合，不照录cardinalityrecipe，downindex评分式row/column约定也不拼代码。保同intermediateidentity/实际densecount、groups/置换/逆映射、SparseGPT顺序与输入校准人口。attention未剪、MLP25/37.5对50%不同资源而非同压缩比质量纯比较。Qwen32B/Seed36B，128s1K校准×16K，质量max32K生成、两模型不同temp/thinkingbudget、三seed均值；T2某AIME/IFEval/LCB低dense、37.5SeedAIME+弱plain，不授全任务无损或plus必优。

速度B200/FP8/vLLM/batch32/sequence4096、25%sparsity有限最多1.2x，Fig1小M sparse可慢dense，非低并发/所有shape/TTFT-P99保证；PATCH仅Ampere当时artifact不代表概念整体不能支持新GPU，AMD库存在不等已测AMD。Prune单B2001.33/1.52h plain、1.87/2.15h plus，校准/排序/重构/packing/双GEMM+accumulate及全质量回归付费；速度不能拼不同比例最佳质量。校准分布移位/底层库效率限制明确，未核实现/复现。

Actual owner `INFER-TENSORRT-LLM`：Ch49“两种稀疏性…”完整06402两段、2509-23410混合tile完整段/独立marker及2610-28947稀疏量化完整后段已实际读，Ch48/50执行交接已读。现tilemix共享artifact没有替连续intermediate区可用两现成GEMM、以及剪枝前置右影响compensation的接口。拟23410独立marker后/“稀疏和量化可以组合…”前原一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

混合稀疏也可沿MLP共享intermediate坐标切成连续dense区与2:4区，让up/gate分别计算输出片段，down对输入片段的结果累加，从而复用现成dense/sparse GEMM而不扩大activation。一个[受限Spense分支](https://arxiv.org/html/2606.10445v1#S3)先选择要保护的索引，再共同置换up/gate行与down列；剪枝前把dense索引放在SparseGPT尚可补偿的后部，和仅在部署时重排是不同决定，相同索引放前仍可严重损质量。未剪枝的置换恒等不替有损分组/重构签字，独立敏感度评分也非组合最优，需保存实际dense数量、2:4组、置换及校准/重构顺序。双GEMM/accumulate、索引与packing、校准剪枝和任务回归均计费；小M可比dense慢，B200/FP8大batch的decode收益不授低并发或全SLO。库/shape、校准支持或质量—费用失配时，保原dense、已验纯2:4或较高dense比例，不由更自由格式或单核稀疏峰值批准无损与通用加速。<!-- source-family:SF-2026-ARXIV-2606-10445 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10445` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10445v1)§3/4/Limit必要，2+2+2=6。只连续dense/2:4区现成GEMM与剪枝前后置索引补偿条件，保Eq5数量不照抄、近似评分/质量反退、小M/特定B200路径和全费，不授无损/通用SLO。未核实现/复现，必要/PRE/POST待独核。

## A38 PCAF — 2606.10435v1（causal successor record与local LM分工）

[精确v1](https://arxiv.org/html/2606.10435v1)，2+1+3=6。实际必要§3完整式1–12/record/空bucketgate/成本、§4.1–4.6完整fullAR与diagnostic协议/表1–6/敏感性、§5–6全部限制；未核Triton/JAX代码或图像素/复现。Localcausalconv产生parametricnexttoken分布；record以causalngramhash address、localhidden连续key及已观察successor tokenvalue分开，query候选最多K后连续score/recencysoftmax得到successorcache分布，与localLM由learnedgateconvexmix，空候选λ0。FullAR第t预测只能用successor已在prefix出现的record（i<t，valuex_i+1≤x_t），不是从整teacherforcedsequence随取future；没核实现不认证完整kernel因果。hash同token最多K/固定B的索引容量不等任意语义记忆、完整features/workspace常数；原O(T+Kd)每sample单query不直接当fullAR总复杂度/online服务常数，semanticsoftoverlap路由另有候选成本，非hash无成本等价。

303M fullAR TPUv4-32/JAX XLA非GPU Triton，T1024/2048、表中samebatch32对比与可容batch256另列；precision/完整训练budget参数未在本必要明确处不造。主headlinebestval非独立test，PG19semantic1024 best50.94而final59.85弱dense56.30；contextbranchPG19best也弱dense，不能普胜。41M多seedNTdiagnostic并非fullAR生成，RTX3060 26M组件消融亦只NT，不能把40Mtok/s直接混主303M吞吐。K32→64/T4096 PPL改善而吞吐2.28→1.68M，semanticS增加有质量/吞吐和top1不单调；无cache的localconv更快，证明memory非免费。S6 bucketoverflow丢record/重复collision降recall，Mamba未匹配完整测试、下游zero-shot/代码/音频未证；模型scale与routingprofile共同变化非semantic必然更好因果。

顺序位置、record可见性/保留策略、addresshash/semanticrouter、key/query、gate/snapshot须共同恢复；token successor身份只保已记录词，不认证答案事实。建表/路由/候选驻留/评分/词表输出、全部训练/调参与完整生成回归全费。只取boundedcandidate接口与局部LM组合的有限quality-resource分支，不授无碰撞/无限记忆/通用线性SLO。

Actual owner `MODEL-LONG-CONTEXT`：Ch22 fixedstate/完整历史、1128保存粒度完整MemoryCaching/DLA/31367与最后远期memorybank完整两段、下一外部工作集首概念已实际读，Ch21/23交接复用。现summary/压缩KV不等以已观察token successor为value、address与连续评分分离后与localLM分布混合。拟“RAG仍适合需要ACL、删除和精确引用…”完整远期bank段后/外部工作集主标题前一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

保留的也可以是可寻址的“旧context→已观察successor token”记录，而非summary或全部KV：先用causal token hash提出有限候选，再用连续key/query与recency评分形成successor分布，同local parametric LM由受训gate混合，空bucket回原local路径。[PCAF的受限分支](https://arxiv.org/html/2606.10435v1#S3)把address与value resolution分开，却不从hash命中推出语义相似或事实正确；每个预测位置只能读successor已在其prefix出现的记录，整序列teacher forcing也须保这份可见性。每bucket最多K会丢记录，重复/碰撞可损召回，候选数有界不等全部feature、建表或full-AR运行成本恒定。更多K/semantic容量能改善局部PPL却付吞吐，best validation与next-token诊断也不替完整生成质量。路由/保留规则、key/gate、记录位置与snapshot共同保存，建表、驻留、评分和训练回归均计费；碰撞、长程关系或净质量—费用不合时，保留localLM、较大候选、显式历史/原hybrid与外部取证，不由稀疏读取批准无限记忆、无泄漏kernel或通用加速。<!-- source-family:SF-2026-ARXIV-2606-10435 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10435` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10435v1)§3–6必要，2+1+3=6。只causal successor record/有限候选与localLMgate分责，保位置可见性/未核kernel、collision/保留、fullAR与NT/批量分开及全费，不授常数全内存/无限历史或普遍速度。未核实现/复现，必要/PRE/POST待独核。


## A39 Bootstrapped Flow Q-Learning — 2606.10613v1

实际采用reader§81精确v1§3/4全部Eq9–26、§5–7、D/E/F/H/I/J的首次必要层，不重复Methods。有限机制是同state自compose的stop-gradient大区间target，与conditional velocity小区间anchor共同识别flowmap；velocity-like参数化保持Δ0 identity并避免弱信号。只composition有退化解，λ0/1与preconditioning反侧保；Bernoulli混合仅给定两loss估计无偏，不是actor/Q梯度无偏。E2小t负r/Uniform域及Qnorm零guard不发布recipe；finiteΔ没有全局自举收敛或分布等价保证。6seed×50episode有限offlineD4RL结果有Hopper/Walker/AntMaze反退；A100PCIe80G/Xeon5317、batch2500三千批frequency不是单请求851Hz，且onepassFQL更快。当前policy双forward、EMA actor/doublecritic/Qgrad、数据/搜索与完整控制验收均付费。未读实现/运行，不认证全部理论或真实control安全。实际Ch24少步蒸馏组合一致首完整段、前DMF两完整段、后Koopman完整段及双端map边界段已读；Ch23/25交接已读。已有teacher组合正则没有承担自bootstrap退化与conditionalvelocity边界的具体分工，拟该段后仅一段。

Actual owner `MULTIMODAL-GENERATIVE-PARADIGMS`，拟少步蒸馏组合一致完整概念段后/提升observables固定矩阵段前仅原一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

组合一致还可以由当前模型自己提供长区间target，而不另训distillation teacher：同一conditioning state下，将两段短flow map的复合作stop-gradient目标，并以已知conditional velocity在小区间锚定，避免只学组合律时连错误的identity map也能自洽。[BFQ的受限分支](https://arxiv.org/html/2606.10613v1#S4)用velocity-like参数化保持零间隔identity与训练信号，但有限间隔、近似优化和critic误差仍不授全局自举收敛、精确分布或一步动作安全；两个loss的随机混合无偏也不是policy gradient无偏。“无独立teacher”仍支付两段policy forward、target/critic、离线数据与调参，批量生成频率不是单请求闭环时延。保存时间域、边界target、state/noise支持、当前与target身份及实际费用，原算法未闭的时间/归一guard不拼执行recipe；退化、Q外推或净质量—费用不合时，保原多步flow、独立teacher/可信监督与control gate，不由自一致性批准无损one-step替换。<!-- source-family:SF-2026-ARXIV-2606-10613 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10613` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10613v1)必要，原6分；仅上述有限接口，直接反侧与全费用近文保留，不授无损/全局保证/通用SLO。未核实现/复现，必要/PRE/POST待独核。

## A40 RATrain — 2606.10415v1

末期行政身份核由reader实际abs/HTML对照采用：exact-v1 abs标题为RATrain，与原B5及报告一致；当前exact-v1 HTML页首显示LifeTrain，而正文runtime仍RATrain、作者与摘要同一。保持精确ID/v1与原候选标题，不由此认证历史逐字同bytes，不新增修订事件或阻塞。

本作者已实际读exact-v1§3完整调度/FSR/优化重叠、§4完整operatorbackend/搜索、§5完整runtime、§6完整设置/主要结果/消融/误差与伸缩。Dense1F1B原图不改；每layer最后accumulation后GradSync→UpdateShard→PrefetchW，必须在下一forward读前ready，不是每microbatch更新。FSR保checkpoint/释放activation，在forward或idle中恢复短生存buffer，资源/窗口不足回backward现场恢复；保存条数与Ninflight/短buffer/workspace共同memory计费。MT3000 DDR/GSM/AM/SM与FP16operatorbackends是具体条件，不能外推GPU-HBM免费overlap。Planner profile+exposed max(0,latency-window)有限argmin，非全局优化/全部候选内存保证。perstagequeue/localcompletion/preallocatedreuse/关键边界transferpriority仍需真实先后。C4同数据序/optimizer/globalbatch，所有MT基线共用backend，是策略适配非原Megatron/DeepSpeed端到端运行；A800参考不成严格跨硬件归因。7B1.028Btokens loss近不证明bitwisegradient或全收敛；70B20.48Mtokens短验，256→1024同batch增大是weakscale非fixedbatch。§6.7同Qwen32config1790.13对§6.3 1592.51口径不闭不合绝对数，各单disabled倍率不相乘；MAC利用率不当全MFU、profile误差只selectedconfigs。完整profile/queue/recovery/transfer/短buffer和回归付费，未核代码/复现。实际Ch36 planner全部概念/完整Piper邻接及下一Phase段，Ch35/37交接已读；增量是编译DAG之外stage-local恢复/更新prefetch窗口资格，非换名overlap。

Actual owner `TRAIN-DISTRIBUTED-TRAINING`，拟Piper11169完整段marker后/从Phase串行主标题前仅原一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

显式DAG之外，stage-local runtime还可在不改1F1B与gradient accumulation的前提下搬移状态生产时机：只保activation checkpoint，在可用forward/idle窗口提前恢复backward所需张量，并在该layer最后一次累积完成后依次同步梯度、更新shard、预取新weight，赶在下一次合法读取前ready。[RATrain的受限实现](https://arxiv.org/html/2606.10415v1#S3)让队列/事件和短生存恢复buffer承担这份合同，不是每microbatch更新，也不靠重排取消数据依赖；窗口、共享memory或传输资源不足时仍须现场恢复/等待。Planner须同时计inflight checkpoints、恢复buffer/workspace、暴露通信与profile误差，预分配复用也不能跨未完成读写复用。所测MT3000内存层级与共用operator backend下的策略对照，不授GPU通用收益、bitwise更新等价或完整收敛；各关闭组件倍率不相乘。Profiling、恢复、weight搬运与完整loss/运行回归均计费，deadline、内存或净吞吐失配时保原backward重算、较保守静态plan与已验runtime，不以更高MAC利用率批准全训练加速。<!-- source-family:SF-2026-ARXIV-2606-10415 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10415` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10415v1)必要，原6分；仅上述有限接口，直接反侧与全费用近文保留，不授无损/全局保证/通用SLO。未核实现/复现，必要/PRE/POST待独核。

## A42 UniSVQ — 2606.10520v1

实际采用reader§89 exact-v1§2/3完整Eq4–9、§4/5全部主设置/主表/直接消融/Limit、A1/A2必要层，不再Methods。每d维word为A整数向量+B，按block把activation先右乘A、同integerW混合乘并加B偏移，代替任意VQ查表；X_iA仍浮点，weight-only兼容不是pureINT或A/KV也2bit。customfusedCUDA/FWHT不是原生tensorcore/GEMM路径已验，Limit optimizedGEMM交互未探索。保存RHT/LDLQ/整数code/共享A,B/packing/校准人口；Gaussian初始化只渐近论证非d4有限格保证，20float每矩阵不是整网，40/2048=1/51.2不沿1/64。Qwen4/Llama/QuIP#/Qtip反优、T5/T7模型字段冲突不合数字。A100batch1/gen1024/3timingrun比GPTQ慢且质量不同，promptlen/actprecision/CUDA全栈/SLO未详；3.87Gpeak不证4G卡可部署。1024×2048校准、Hessian/LDL、8B模型在单A100调参约6h与activation变换/偏移/全回归付费，未核实现/复现。ActualCh49 10496两完整productLUT段/Aristotle完整后段、E8-QAT导出段、Ch48/50交接已读；现任意centroid/LUT与escape不等仿射integer格可交换消费这份接口。拟10496限制段后原一段。

Actual owner `INFER-TENSORRT-LLM`，拟10496 productLUT完整实现限制段后/重复weight在线乘积复用段前仅原一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

避免任意向量码本lookup，还可将每个低位word限制为共享仿射整数格：重构是小矩阵A作用于integer codes再加B，于是每block乘法可先对activation做A变换，再消费integer权重，另加共享偏移。[UniSVQ的受限接口](https://arxiv.org/html/2606.10520v1#S3)用较小仿射参数换取这种可交换消费，但限制了表示自由度；变换后的activation仍为浮点，不能把weight-only兼容说成纯INT GEMM、activation/KV同位宽或原生tensor core已验。实际custom fused路径与optimized GEMM集成尚有边界，有限格初始化也不由渐近Gaussian论证获得无损保证。RHT/LDL校准、整数codes、A/B、packing与activation变换/偏移共同定义asset，全部制备与执行回归计费；有限batch1计时慢于另一scalar路径、部分质量弱于VQ也须保留。格式、质量或净费用失配时，保任意VQ配匹配consumer、成熟scalar量化或高精度，不由更小码本metadata批准全模型同质量加速。<!-- source-family:SF-2026-ARXIV-2606-10520 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10520` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10520v1)必要，原6分；仅上述有限接口，直接反侧与全费用近文保留，不授无损/全局保证/通用SLO。未核实现/复现，必要/PRE/POST待独核。


## A41 DiRL — 2606.10346v1

本作者实际读exact-v1§3完整式1–12、§4完整设置/主表/泛化/所有直接消融与direction/perturbation/费用分析、Limit、A完整gradient桥、B全超参、C全部MATH-R/M标签协议。用初始policy最后prompt位hidden的D+−D−均值差k固定；token sigmoid(h·k)给最终层loglikelihood敏感度proxy加权，response平均hidden·k正负分组；相对reasoning组的reward-weighted余弦平方聚合，经分组minmax后对正组加/负组减，clip后再组内标准化，不改PPO/KL。完整MATH7500由GPT4o打分分R/M，另外GSM8K/MGSM/MMLUPro等跨数据集对比；这是标签与人口差异代理，零阈值未center，不认证causal reasoning/memorization、token真理或novelty与正确性同义。labels不直接替verifier，但通过k间接影响shaping，不能称无标签监督。k稳定angle/同标签classification不证明跨域语义恒定；KL也不数学保证hiddengeometry。

Eq10分母整个group而Eq11只sumR，R权重未再归一，即使所有reference共线也可因R外权重质量使nu>0，不称精确新方向/正交残差。Phi仅最终层hidden敏感度，不是整网gradient：每token不同Jacobian/权重、sum后方向与实际parameterupdate角度没有Eq16一般桥接，不采用其所有层factor/角度保证；W转置维度表述不照抄recipe。空reference nu0明确，同分minmax/零normguard未完整发布不补代码。错误但被标R也可软化惩罚，不以未验证主观方向覆盖verifier。Noalpha/NoSub/NoMR/NoShape有限消融支持接口，不认证各组件普遍必要/纯reasoning因果；GSM-Symbolic提升是行为proxy，MMLUPro与direction构造人口交叉，不称完全隔离OOD。4H10080G/Qwen3-1.7/4Base/MATH7500/batch16/group16/8192与12288maxresponse，LR5e-7/KL.001；默认λ主文1.5/1.5与B表1.0冲突不选唯一recipe，precision/总updates/训练seedCI未披露。T4 35.7→40.2/68.4→80.5sec/step是13/18%慢，不是免费或全训练比；向量/readout/组矩阵/标签校准与全回归费用保留。未核代码/图像逐点/复现。实际Ch33 DQO完整概念/marker、后正确组稀有度完整段及Ch32/34交接已读，旧semantic-diversity未承载固定contrast方向改变token权重/参考人口及正负shaping这一具体差额。

Actual owner `TRAIN-GRPO`，拟DQO04784完整marker后/同题正确rollout稀有度分支前仅原一段+trueH2本人注。

### 唯一literal（待必要/PRE/窄授）

多样性也可先声明要鼓励哪一种表示差异：从初始policy的两类对比prompt取得固定hidden方向，用它给token的最终层敏感度proxy加权，并把rollouts分组，只相对指定参考组计算新颖度，再对两组作相反符号的reward shaping。[DiRL的受限分支](https://arxiv.org/html/2606.10346v1#S3)改变的是bonus权重与参考人口，不认证被分为“reasoning”的文本真的推理、另一组只是记忆，或hidden proxy的角度就是全参数更新方向；不同token的Jacobian不能由一个加总向量自动消去。Reference子集的权重与零范数/同分处理须声明，不把余弦平方分数当精确独立信息；错而被标为正组的回答也可能少受惩罚。应绑定对比数据/标签、policy与层位、固定方向、group/权重及verifier，独立检查解法与迁移，不能用同一方向读出的比例上涨自证机制。校准、读出、向量矩阵与全部rollout/训练回归计费；方向漂移、proxy或净质量失配时，保原outcome GRPO、较弱bonus与可信独立评价，不由更多新颖文本批准新推理能力或免费探索。<!-- source-family:SF-2026-ARXIV-2606-10346 -->

本人note唯一稿：`SF-2026-ARXIV-2606-10346` — Daily2026-06-11补Jun10；[exact-v1](https://arxiv.org/html/2606.10346v1)§3–4/Limit/A–C必要，2+1+2=5。只固定contrast方向的tokenproxy/参考人口/符号shaping，保Eq10subset权重/非整网gradient、标签与同proxy自证边界、λ冲突和13/18%step费，不授causal reasoning/exactnovelty或普遍收益。未核实现/复现，必要/PRE/POST待独核。
