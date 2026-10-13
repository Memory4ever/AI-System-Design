# DBB2603.18444 exact-v1：必要Source / sole owner / 最小PRE

准备者resume_mar18，2026-10-11，独立恢复只Daily2026-03-21补BJT03/20。实际重读当前AGENTS、研究/Report/适用Sources、统一prompt、ROADMAP、本日STOP；Books背景/学习方法/写作指南、LS路由、actual Ch33及Ch32/34开篇已读。不写Books、不自己授非准备者PASS、不计safe/DAY。

## 1. 身份与必要证据

[精确v1](https://arxiv.org/html/2603.18444v1)，首批准入/root独校及官方日级arXiv夹证见原SUP_FIRST_ADMISSION/DATE_FIELDS，限定归03/20，不冒其他地方未先公开。评分2+2+2=6，对象为每题折扣二值统计→baseline/scale消费者与偏差—方差边界，不给Beta conjugacy成熟原则新分。当前官方事件页身份与首批有效检查可复用。

实际必要读取：§2.2/Eq2–3的组内样本方差与无KL目标，§3.1–3.3/Eq4–20/Algorithm1，§4.1–4.2/Table1，§5.1–5.4/Tables2–3及MSE测量人口，Appendix A Table4/B.1–B.4/Eq22–37（中心理论条件）、C Table5/配置和选checkpoint。未遍历References、完整图点、代码或版本史，未复现。

同题q初始化alpha=beta=1；每次再次rollout后以lambda折扣原两项，再加当前成功数S和失败数N−S。历史只保存每题两scalar，不重放旧response/logprob，不改变新response仍来自当前behavior。以alpha/(alpha+beta)及该概率的Bernoulli variance构造当前advantage所需统计；原称posterior variance的Eq13实际上是plug-in Bernoulli reward variance，不是Beta随机参数p的variance（后者还有alpha+beta+1分母），不能把两者混写为不确定度证书。历史与当前共同参与baseline，是biased shrinkage，不是独立旧policy轨迹的无偏复用。

有限正参数在精确算术下使plug-in方差非零，但并不推出gradient有效、真实正确性或方差统一下界：lambda=.5、连续全错时alpha=.5^t，beta趋16（N8），故p及其variance趋0；有限precision亦无作者保证。非平稳MSE Eq19/37含历史偏差平方，不能授无条件低于当前均值。独算条件反例：history alpha1/beta15、lambda=.5、当前N8且p=1，DBB均值17/32而当前samplemean确定1，后者MSE0，前者正偏差平方。只是理论普遍外推反证，不称作者实测无效。

Appendix B明确假定给定整个p序列后各S独立；实际policy由此前rewards更新，condition on未来p序列未自动保此独立，需要额外设计/假设。可用其固定条件分解解释shrinkage，不把式34一般LLM自适应训练中无covariance的variance保证采用。保中心理论争议，不删该反证/降分/EX。

## 2. 评价、费用与直接反侧

Qwen3-1.7B/8B-Base、DAPO-Math-17k（实际17391→17280，prompt≤1024）、verl/Math-Verify、4/8H200；RePO两scale均8H200，所以1.7B replay比较非同设备。rolloutbatch128/updatebatch64、N8、4epochs/1080steps、responsecap4096/8192、AdamW 1e-6 constant无warmup；train temp/top-p1/1，eval .6/.95，precision、完整并行/软件commit、重复seed/置信区间、端到端时间/能耗Not Disclosed。不作额外memory为零断言：每题统计、checkpoint/同步及更多生成tokens仍付费。

Table1所选DBB相对GRPO在所测六ID+三OOD平均更高（1.7B ID+3.22/OOD+12.49，8B +2.42/+6.92），但Appendix C将普通方法clip-low/high=.2/.28，DBB单独改为.98/.98；总收益不能唯一归折扣统计，未控制clip联合变化。DBB响应更长，等1080steps/N8不等token或wallclock成本。Validation含五ID集，Olympiad/OOD只在每实验最佳checkpoint测试；lambda0.5/0.75依据Table2同ID趋势选择，不授无选择偏差/泛化因果。指标原文混用Acc@8/Avg@8，不自行当pass@8。

Table2 1.7B lambda1平均26.29<GRPO26.74，MATH67.30<68.37/Minerva25.55<25.74/AMC23.33<23.61/Olympiad28.65<29.41；8B lambda.75 Minerva39.48<lambda.25的39.98，平均最优不等各任务最优。§5.3仅1.7B GRPO训练随机10%题再采128条作有限p proxy，不是true p/独立DBB-trained path；lambda.95/1的MSE不胜，N≤16只相应proxy测量。额外128analysis rollouts不进入训练但诊断有费用，不支持无额外实验成本。Table3 DrGRPO有限1.7B/λ.5平均+1.96，但同样不自动解除clip/预算混杂。

## 3. Actual sole owner 与差额

唯一owner TRAIN-GRPO，books/part-04-training-system/33-grpo.md。实际80–170同题mean/std/零方差与filter→objective，480–556完整核理论组依赖→generalist prior→全局累计shrinkage→prompt admission，Ch32/34开篇交接。现510–524是跨任务generalist value prior+边际停止，526明确**全局**reward/groupmeans（并声明不是每题bank）；528后复用prompt signal只决定重新采哪些题、仍普通GRPO评分。尚缺同题重复访问的两项折扣成功/失败统计实际直接进入baseline/scale、与trajectory replay及admission三者分开的接口。不能主题相似NC，也不为Beta公式新增第二owner。

拟仅一段在526全局统计后/528prompt采样前；写前须root协调最新锁与actual邻接。能否采用的裁定问题：以上有限统计消费者有方法和局部实验支持，可否独立于无条件MSE/不崩溃/成本与归因强claim采用？若不能则中心争议本窗隔离，不绕成泛泛history原则。

## 4. 一段逐字PRE

历史支持也可以限定在同一 prompt 的重复访问，而不是跨题共享 prior 或重放旧 trajectory：一条二值 outcome 分支为每题保存成功与失败两项统计，先折扣历史，再并入当前 policy 新采样的结果，以收缩后的成功概率及其 Bernoulli 尺度参与当前 advantage。它改变的是 baseline/scale 的证据人口，不是保存旧 response 后直接训练，也不自行决定哪些题获准 rollout。Prompt、reward、policy 漂移、访问次序、折扣系数与两项状态须共同标识；正的初始统计只使有限精确算术下的尺度非零，不认证有效梯度或永久远离退化，历史失配仍可能使偏差抵消方差收益。[受限原证](https://arxiv.org/html/2603.18444v1)的数学对照同时放宽 clipping、选择折扣与最佳 checkpoint，生成长度也变化，不能把全部提升或等更新次数归为统计器独立收益与等成本。每题状态、同步/恢复、调参与完整 token 费用应一并比较；漂移、重复访问不足或质量/总预算失配时，保留当前同题 mean/std 与数值保护、无历史分支及普通 rollout，不授无条件更低 MSE、无损或全训练稳定。<!-- source-family:SF-2026-ARXIV-2603-18444 -->

## 5. 静态注PRE

- `SF-2026-ARXIV-2603-18444` — Daily2026-03-21补03/20；[DBB精确v1](https://arxiv.org/html/2603.18444v1) §3/Eq11–20/Algorithm1、§4–5/Tables1–3、Appendix B/C。2+2+2=6，必要差额深入：同题折扣成功/失败状态→baseline/scale消费者，不重放旧轨迹；非平稳偏差、条件独立、plug-in尺度非Beta参数variance、无统一非零下界、clip/选checkpoint/更长输出与完整费用近文；不采普遍低MSE/稳定或零资源保证，未核实现/复现。

等待非准备者必要Source/actualowner/PRE。未授权写、未计safe/DAY。

2026-10-11 root非preparer正式Source/actualowner/逐字PRE PASS：实际精确v1 §2–3/Eq2–20/Algorithm1、Tables1–2/§5.1–5.3关键反侧、B.3–4/C/Table5；actualCh33完整488–543与74–133及Ch32/34开篇。两统计直接baseline/scale差额独立于全局bank/admission，可受限采用；plug-in与条件独立、clip共同变化、更多token费用等近文边界不变。root授Ch33本一段+静态注窄锁，写后root一次nonwriter实际POST；不预支safe/DAY，不改其他正文。

2026-10-11落实/一次nonwriter actualPOST正式PASS：作者按原逐字写Ch33 528及本人静态末注（当前3198，实际行号可随并发先前family位移），实际510–546/末注逐字回对与限定diffcheck无输出；root随后实际完整516–546及本人末注/邻注对原PRE和必要Source正式POST通过，明确全局prior→同题统计→promptadmission分责完整，Ch33锁释放。只单项安全实际整合，不更新静态注加入验收身份，不授DAY。
