# Jan28 最后一批具体 Books 比较（待 PRE / 窄锁）

## 最新层级（恢复后的实际结果）

新增61已到必要证据/具体Books安全终态：35整合48段16owner、11已有覆盖、9仅报告、6中心争议；全部35实际正文/完整邻接/自身末注 POST与状态轻核已由非作者通过，窄锁释放。下文旧待Source/待Books/待锁/PRE仅拟文为历史阶段；未变有效Source/PRE/POST复用，不代表当前普通队列。原64保护，最终六部分已融入README，V3进行态通过，最终DAY尚待。

复用本日 exact-v1 必要 Source，逐项位置见 independent:61–68/93/95/103，未把下载算审阅。本文是具体采用包，不另计候选。author 已实际比较下列正文；非作者结论未到前不授 Books 关闭。

## 六项非写处置

- **18067：已有覆盖，AGENT-PLANNING / Ch79**。实际202–228候选谱系、局部fast-fail与完整evaluator、训练teacher/运行controller分责承载最低长期结论：快速局部通过不等完整任务或正确性。本文STG命名/小控制域遍历、宽域随机corner、golden时序比对与IGR/MCTS具体配方留日报，不声称这些配方已有覆盖；有限pass-fraction不是formal coverage，Area×Latency未验power，CONV反侧及reset/reference改协议不改变既有分责。
- **18137：已有覆盖，AGENT-PLANNING / Ch79**。实际10–40规划目标/预算、87–107局部粒度与整体目标、153–196已编码feasibility/执行与语义分责，承载局部步骤成功不保证最终所有约束同时满足。DeepPlanning静态solution-centric synthetic任务、travel模型parse/codechecker与shopping exactproduct及失败交集留报告，不称implicit/global计数、unique-optimum构造或400call预算已有覆盖，也不以140失败分母造因果或比例。
- **18125：仅报告**。实际Ch72 236–259 policy-bound detector→local decision、347–366 placeholder/restoration权限说明未命中不认证匿名、local不代consent。本文可保optional pre-send UI与flagged/unflagged行为观察；10学生固定先无panel后有、模拟服务与qualitative观察不足以修正长期“agency改善privacy”的因果解释。UI效果不是已经被书中复制；效用、restoration安全与artifact未核均留界限。
- **18468：仅报告**。实际Ch66 119–145明确quality对象、scorer identity与proxy/geometry需要真实任务验收；Ch12 306–336明确读数与能力分开。本篇50采样至少一次correct的latent proxy、firstcorrect/firstdegrade survival相关是可保的局部测量协议，但尚未校准潜在知识、持续准确或内部因果，因此不增加“latent knowledge导致训练更快”稳定机制。不因单模型/小样本关闭贡献；PH时间聚合、right-censor与HR/分母冲突反侧留报告。
- **18483：已有覆盖，PLATFORM-EVALUATION-SYSTEM / Ch66**。实际497–515 cue/context构念与目标/非目标属性交叉回归承载最低长期结论：对一属性干预后须分别验目标、非目标与条件人口，聚合改善不能代组合保持。本篇humor/persuasion五级ordinal、secondary prompt、先看judge的18人判断配方没有被复制到书；Spearman不是幅度校准、局部提示不证内部独立、rho=1精确统计争议留日报。
- **18527：仅报告**。实际Ch22 99–104 effective utilization及345–379 selector目标/读取与dense质量分责，Ch76 494–540 retrieval排序与最终support分责，均未假设longctx奖励必与KV压缩相容。本篇奖励输出格式与对应eval prompts共同变化、局部32K训练与128K–1M对照可保为任务专化/压缩失配证据；没有控制足够条件支持普遍替RAG或新增通用attention/压缩机制，最优压缩39.7仍低RAG43.8、RA全部退与finance AO反退应进日报。不称该篇recipe已覆盖，也不以主题相似关闭贡献。

## 17471 → AGENT-WORKFLOW / Ch81

实际78–118执行合法性、activation与lattice worklist已读；未有持续patch循环的双向PoV去重与provider-worker/协调器失败分账。拟放Task State Alignment之前，一段：

持续修复循环不能只按文本相似度合并新故障与补丁：先用已有 patch 重跑新 crash 的 PoV，再用新 patch 检查已存 PoVs，可分别识别故障重复和补丁覆盖；两者都是给定测试证据的去重提议，不是语义正确或漏洞完全相同的证明。Provider workers 可各自保留静态质量偏好、并行生成，再由独立 coordinator 接收候选，减少限流耦合，却不消除协调器单点。[受限漏洞修复对照](https://arxiv.org/html/2601.17471v1)的 plausible/test-pass 与人工正确仍有差距，坏 symlink 还能让初始化漏掉任务；内文与伪码的精确去重谓词冲突不拼可执行保证。PoV、patch版本、worker/provider与合并收据应保留，重测和额外API调用付费；coverage或controller资格不足时，回分开追踪、完整原测试与人工审核，不由去重命中自动关闭修复。<!-- source-family:SF-2026-ARXIV-2601-17471 -->

## 17915 → AGENT-WORKFLOW / Ch81

实际lattice两段与Task State Alignment交接已读；缺非单调belief全文修订与label damping/硬预算分开。拟接lattice两段后、一段：

若任务需要撤销旧诊断，而不是只在 lattice 上单调增加 assessment，还可以给每个节点保存 label、evidence summary 与邻居 inbox，让模型只提局部 belief，确定的 controller 在整个 belief 改变时重激活邻居。判断 label 未变不等于 evidence 未变；只按 label flips 做 damping 不能约束同标签文字反复修订，因此每节点访问上限与总体预算应独立保留。[受限故障定位对照](https://arxiv.org/html/2601.17915v1)的正确性依赖完整数据、可靠 local policy 与图可达，发现图的 frontier 不是已证明真实原因；局部 controller 消融不授语义 fixed point，某模型输入token还增加。图、inbox、revision与停止原因共同记录，重复生成/传播计费；证据不全、震荡或预算耗尽时回原始日志、单调可证明子域、人工核验与Unknown，不以停机签发正确诊断。<!-- source-family:SF-2026-ARXIV-2601-17915 -->

## 18302 → TRAIN-PRETRAINING / Ch28

实际70–98 future/teacher/intralayer Semantic Tube目标完整局部已读；缺跨layer jump正则，非同一沿token位移。拟Semantic Tube段后，一段：

表示正则还可沿模型深度定义，而不是只沿 token 序列约束方向：若监督主要从最后 hidden layer 读出，较大转向可能集中在末层；仅惩罚末层角度又可能把转向移到倒二层。一个条件分支把相邻 layers 的 angular change 加权纳入全部层目标，显式选择控制对象与深度权重，而不把角度小等同于语义冗余或训练稳定。[受限 JREG 对照](https://arxiv.org/html/2601.18302v1)支持此控制分支，单任务仍有退步，early-exit实验也不授任意删除层；读取/保存中间状态、额外正则与深度重新调参增加内存和训练费用。权重、层集合、原NTP目标与held-out任务共同验收，几何prior不适配或净成本不值时，降低/关闭正则、保留原训练与真实任务检验，不由layer角度曲线自签表达能力保持。<!-- source-family:SF-2026-ARXIV-2601-18302 -->

## 18418 → TRAIN-DATA / Ch27

实际Collection protocol 54–90上下游生成/annotation/partition已读，缺未来PR差分重建与真实environment交互样本来源分开。拟collection示例后、主动partition之前，一段：

Agent训练语料中的“原生交互”也须按生成权限拆开：利用未来 PR diff 选择相关文件，再由模型重建任务 summary，能提供带工具格式的上下文，却不是当时真实 Agent 已观察的轨迹；在容器环境实际调用工具、运行测试得到的记录则有不同 observation provenance。两流都可用于训练，但重建依据、环境版本、过滤前人口与 passing selection 不能合成一个“真实成功轨迹”标签。[受限 agent-native 预训练](https://arxiv.org/html/2601.18418v1)还将全部tokens的预训练与mask user/tool的SFT区分，并改变阶段/数据预算，局部结果不证明某一来源独自造成普遍推理能力。重建、环境执行、测试过滤和训练都计费，test-pass仍非correct；来源泄漏、分布不匹配或任务回归时，保留真实日志与独立验证、分流训练及普通语料，不让格式或未来diff替当时观察签证。<!-- source-family:SF-2026-ARXIV-2601-18418 -->

## 18321 → MULTIMODAL-REPRESENTATION / Ch23

实际Fusion 397–423 early/late/cross接口已读；缺先生成perception文本再条件reasoning的显式中间对象，其来源并非盲单模态。拟Late fusion之后、Cross-attention之前，一段：

决策层融合还可以先生成各模态的 perception 描述，再在这些文本与原输入上推理，让中间解释可检查；但生成先后不自动使观察独立。若 audio描述仍以visual描述和完整输入为条件，它就是联合推断，而不是一份新的盲音频证据；后续偏好训练奖励解释与答案一致，也不验证真实情绪或内部因果。[受限视听情绪对照](https://arxiv.org/html/2601.18321v1)使用大规模合成标签、ASR过滤与模型judge，数据、阶段和格式共同变化，不能把局部增益全归两段感知。应保存原模态、可见性、perception producer及judge版本，生成解释/偏好样本和额外训练计费；描述失真或缺模态外推失败时，回独立encoder、原始信号与真实标签核验，不把易读文本当独立感知真值。<!-- source-family:SF-2026-ARXIV-2601-18321 -->

## 18393 → MULTIMODAL-REPRESENTATION / Ch23

实际Cross-attention 411–423方向/producer/consumer接口已读；缺audio-query视觉KV与训练特权teacher/audio-only部署分账。拟Cross-attention首段后，一段：

融合方向也须与部署可见性分开：局部 audio Q-Former 先形成 queries，再读取视觉 encoder 的 keys/values，可以让多模态teacher使用声音指向的视觉上下文；之后在共同词表上用teacher伪标签与soft分布监督audio-only student，部署不再获得视觉输入。训练中把gold字幕嵌入画面、按gold interval对齐，并不是自然盲ASR获得了额外事实；teacher训练与冻结蒸馏、student可更新部件须各有身份。[受限字幕辅助蒸馏](https://arxiv.org/html/2601.18393v1)的student局部WER改善远未达到teacher表现，不授完整能力无损迁移。额外视觉训练、teacher前向、对齐和标签费用不能由student部署省输入抹掉；同步、字幕权限或域条件不可靠时，回原audio-only训练、真实配对观察与独立转录评价，不让特权teacher自签部署感知质量。<!-- source-family:SF-2026-ARXIV-2601-18393 -->

## 18491 → PLATFORM-EVALUATION-SYSTEM / Ch66

实际63–93五种成功/交集、119–145代理身份已读；缺trajectory binary verdict与risk source/failure mode/harm诊断粒度单独验收。拟五层交集后、Ch67交接前，一段：

Policy/Safety的一次binary verdict还不能认证诊断粒度：指出trajectory不安全、定位风险来源、分类failure mode与说明可能伤害，是不同标签和决策对象。Binary分数较高时，细粒度诊断仍可能很弱；应保存taxonomy、trajectory/tool人口、每轴标签来源和人工/模型judge分工，不把多项描述压成统一可信解释。[受限 SAFER对照](https://arxiv.org/html/2601.18491v1)的合成平衡人口与工具隔离支持这项测量差额，最佳failure-mode分数仍低，额外诊断监督也非等预算因果。标签与多轴审核计费，likelihood扰动代理不认证内部因果，诊断错误或标签资格不足时回binary拒绝/升级、原轨迹与独立人工审查；只有外部policy owner能决定是否放行，细致解释不代安全gate。<!-- source-family:SF-2026-ARXIV-2601-18491 -->

## 18771 → AGENT-MEMORY / Ch77

实际126–139 item retention、184–207read recency/metadata已读，audit额外actual1142–1166 valid/transaction time与1455–1465eviction闭包；缺write/add与read刷新事件分开。拟Recency高不代表正确段后，一段：

Recency还必须明确由什么事件刷新：只在write/add更新的writeTime衡量最近写入，读取不刷新它，因而按此时间保newest不是read-based LRU。自然语言dependency trace可以安排检索新文档、读取旧事实与生成结论，却不等于runtime强制的typed DAG；事实、来源与write event仍分别保留，reuse次数也不授正确性。[受限MemoSearch对照](https://arxiv.org/html/2601.18771v1)训练时每episode空memory，推理可跨question持久化，这两种人口不能共同认证长期记忆策略。容量/eviction、reader与跨题有效期要另验，检索、写入、训练与回读原源均付费；旧事实冲突、依赖将被驱逐或跨题质量回退时，保留episode隔离、显式读写事件与原文核验，不从高recency或复用率签发事实保持。<!-- source-family:SF-2026-ARXIV-2601-18771 -->
