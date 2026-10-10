# Min-Seek09855：thought admission 与位置重编码分开

当前处置：root必要源/actual owner PRE及正文418/420、完整410–435邻接/自身末注actualPOST均通过，Ch45锁释放；本项5分受影响深入整合已正式同步。以下提案历史保留，不重开已有效审阅或未采用保证，非DAY。

exact-v1 https://arxiv.org/html/2601.09855v1；准入已独校准，拟2+1+2=5标准，Ch45位置与lossy state差额必要深入。必要原件increment-minseek-method-eval-20261008.json实际§3.1/3.2及§4.1–4.3/Limitations，不扩references。

机制：始终保prompt+首thought PT1；追加RC仅保最短且同长度更早者，严格更短才替换。每个新cycle只能消费PT1/当前最短RC，与当前生成RC共同形成下一选择，不要求存所有旧thought。Length是避免长失败路径的proxy，非判断正确或证据可丢的authority；深层KV仍携带旧conditioning不等完整history保真。answer时小模型直接end-think、大模型允许最终cycle再answer，两个consumer/cache状态不同。

位置接口：K_no_pos/V常驻保留集，每次cycle开始复制K并连续编码position0…|KV|−1；cycle内双K/K_no_pos+V更新，结束丢rotatedK，保prepositionK/V。不是只改metadata，也不是物理compact后原logicalpositions不变；新的attention位置距离明确不同，不授恢复fullhistoryattention或只有RoPE校准。若每PT1/RC/answer长度≤u且保留RC数≤Ibar并(|Ibar|+2)u<contextmax，作者得到bounded activeKV下总emittedlength线性attention计算；不是任意singlecycle无长度限/无限horizon无损/全部费用线性。

支持/反侧：DeepSeekR1DistillQwen1.5/7B、五reasoning任务，M0/2/4/6/10/20/50/100/inf实际仍soft32768tokenstop，no-end-think两variant处理不同；single generation peritem/每M same seed、temperature.6/top_p.95。Normalized任务平均非pooledaccuracy；7B AMC是反侧例外，1.5/7B总体长M局部稳定不证明普遍sweetspot去除。timing只M0/10/20隔离运行，BudgetForcing平均慢44%/29.4%限定该测量，不能倒算普遍speedup/P99；作者preliminary双K未测显著slowdown非free。两份K/复制reencode/选择及额外cycle都费，hardware/precision/batch/concurrency/SLO/多seedCI NotDisclosed。易任务增加compute，保standardgeneration/fixedbudget/FullKV回退。

日期：increment-datacite-09855-20261008.json Submitted Jan14T20:30:55Z，正常公告最早Jan16UTC01；Updated-v1 Jan16T01:05:05Z/正式IDregisteredJan16T02:41:05Z给存在上界，与已核ID不可预发规则限定普通arXiv事件Jan16BJT，非submitted/registered单独firstpublic。current原件increment-minseek-current-20261008.json onlyv1/FindingsEACL2026，无已见撤回纠错安全声明；necessary原文无直接更早项目全文链接，不授互联网零早稿。

actual owner作者完整Ch45:409–466：已有PackCache多轴rebase、LoopGuard退化触发keepindex且保logicalposition、QueryMemory survivingrow remap保持原identity及PreRoPE校准，均不是shortestcycle替换后主动改为连续新modelpositions。长期具体差额为**可选择改变位置语义的重构cycle cache state**，不是一般保留budget。拟在workload-aware eviction下LoopGuard两段后最小一段：thought长度只提保留候选，preposition双K重编码主动形成新consumer距离、保有损/边界u与复制费用，不能宣称原identity不变或模型因果attention崩溃已证；原FullKV/中止重试共存。只Ch45一处，不另Ch20讲完整BudgetForcingrecipe。待root necessary/actual owner PRE与窄锁后写，本包不自授通过/DAY。
