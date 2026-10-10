# 10360 One Token, Two Fates：必要Source与缓存方向接口PRE（待非作者）

仅03-13补充Mar12 BJT自然日。第三完整v1题摘准入与DATE3/独核§23日级夹证有效复用；本次直接重对 `SUP_ABS3_10360.txt` 完整题名/五作者/10pages/AB/history，v1 SubmittedMar11T03:19:46Z、registeredMar12T01:59:36Z与有效正常公告下界夹Mar12日级，无当前可见撤回/纠错或venue信号。不扩全版本或别日报。官方 exact-v1 https://arxiv.org/html/2603.10360v1 GET200/261886bytes/UTC2026-10-10T01:23:22.418354Z，`SUP_CORE_10360.raw/txt` 及 MANIFEST_RESULT.json已保存。

## 实际增量与拟评分

已有视觉对比可每次产生派生图像或对输出logits做差→本文在prefill/首次t=0仅随机保留少量原vision tokens做K路negative，读取原/负输入浅层hidden差分→按层平均并缓存，后续t>0生成重复用这份初始方向、归一化插入当前hidden；中层另读原图+增强图context插值。这改变**输入特定差分的生产时刻与后续状态消费寿命**，不只是CRC/causal名字、增强/steering旧原则或跨主题联想。

拟 **Design2+Reach1+Durability2=5**：差分方向从每步新输入probe转成首次生产后复用的重要接口2，单多模态decoder路径1，原/删token输入、层与位置、生成进度和缓存失效资格需共同绑定的可复用生命周期约束2。未借SCM、training-free、已有pre/post causal原则或性能声誉抬分。只拟采用受限cache生产/消费分责；具体Ch23目前未承载这个时刻差额，触发必要局部深入，强纯视觉/因果/稳定方向与低费承诺反侧已读。不拟采用“纯幻觉原因”、普遍去偏、所有任务提高或端到端1.06保证。Source/PRE待非作者，评分与正式结果不预授。

## 实际读到的必要原件

直接精确v1 §2.1–2.4全部（290–1145）/Eq1–14、§3.1–3.4全部/Tables1–4（1146–1752）、§4.1–4.4全部/Table5/必要pruning和强度文本（1753–2025），及§5–6直接比较/结论（2025–2080）。读的是原table数据，不用“均最佳”正文代数字；Figures只caption/正文，未检查pixels/精确曲线或代码。首次全章rg输出截断，不认证全章；目标owner局部96–124另完整读足。无新PDF/代码/复现或前版diff需求。

SVC：随机horizontal flip、Gaussian blur radius5、salt-pepper0.2增强图的encoder tokens与原tokens concat，Eq4前层hidden作query对V_syn读context，Eq5 `(1−λs)H+λsC` 插值，不是未归一残差相加。Lc16/λs.06。Flip会改变方向语义，噪声/blur可能删除目标，故不能把“增强保持所有视觉真值”作为前提；拟采用不依赖空间真值保持或图像精数。

CRC：Eq6–8在t=0原tokens及K=3随机pruned negatives各仅保Nh=5做前向到1…Lc；`v_l=mean(H_org−H_neg)` 缓存“for all subsequent processing steps”。Eq9–11在t>0将当前hidden和方向分别norm，**正加**λc .1方向再恢复当前hidden原norm。图4/架构正文将它叫hallucination direction并说subtract/away，逐字式10却加original−negative，而理论末段又说加缺失视觉信号；这是direction语义/符号的披露差别，采用边界依据原式，不擅改为负号或据名字裁定整个机制无效。

§2.1 H是sequence，原/剪token输入长度不同；直接整矩阵相减、prefill方向复用到decode的同位置对应/广播、position mask、norm零向量处理未由这些式闭合。可能实现仅取对应text/last token，但本次没有artifact确认，不能补造精确可执行recipe或断言代码一定bug。低维hook接口若要实施，必须显式补层、位置/shape及失效规则；书稿只述受限proposal，不认证已经做到。

Eq12–14明设相同加性 `E_shared(Q,B)`，相减在此条件下消除共同项，还需local线性才能把 `E(V)−E(Vneg)` 写作 `E(V−Vneg)`。删token会改变position/attention和视觉×文字interaction，没有证据证明真实网络两个shared项同一；原文相同Q并不足以推出同一视觉无关hidden分量。简单形式h(q,v)=qv就说明差分随q变，并非独立纯视觉真值；后续生成q_t/状态变化，首次差分也未必是每步方向。本反侧只是隔离强因果/时间稳定保证，不推所有实际效果消失。Norm保持只固定幅度，不认证语义/能力；t-SNE close不是in-distribution或SCM资格证书，TAM case不是唯一机制。

## 关键评价、反侧与成本

LLaVA1.5/MiniGPT4/Shikra/InstructBLIP，线性projector与QFormer分支；本文核心配置通用Lc16/λs.06/K3/Nh5/λc.1。具体模型size/精确revision、hardware、precision、input/output长度（除CHAIR64/128 newtokens）、batch/并发、seed/CI、测时是否含warmup及probe制备 Not Disclosed 于所读必要设置，不填生产SLO。

POPE Tables1随机/popular/adversarial三split平均，MSCOCO LLaVA ours86.79/F187.04>原84.79/85.61，InstructBLIP ours84.59低VCD84.81/VISTA84.87/ONLY84.90；GQA MiniGPT ours71.40低ONLY71.99，InstructF1 80.29低VISTA80.34/ONLY80.32，不能“所有模型所有指标均最佳”。CHAIR Table2 LLaVA64 Sen18.1较ONLY19.2好、Ins8.4却差ONLY7.5/VCD7.9；Instruct128 Sen39.4/Ins11.5差VISTA36.2/10.4。正文把18.1/16.7称CHAIR_I但table列是Sen，保持表人口，不偷换为instance指标。生成上限两档不是实际caption相同长度或完整recall/全能力保证。

Table3只MME两模型且local gain不大；MMHal96题/GPT4评、图6本文说八类均优，本次未看pixels，不采用其全类精确比较/真实人类正确性。Table5 LLaVA POPE原图SVC/增强SVC、masked-negative CRC/pruned-negative CRC、组合局部更好，支持两接口有局部收益，不由一模型两dataset消融授所有任务唯一协同/纯shared消除。

Table4作者token latency32.1 vsGreedy30.3ms（1.06），memory14924 vs14257MB；低于部分其他附加方法不等原baseline更省，token/ms是相应吞吐单位非多请求服务吞吐。缺硬件、batch、长度、warmup范围及端到端probe/encoder制备账，不认证全费用只6%或通用runtime。K/λs/λc/Nh用LLaVA POPE gridsearch选，调参人口/重复不明；更K更费、Nh5效果在特定576原tokens/对象existence任务，不是任意encoder固定五token有效。缓存减少重复负侧计算，但不能抵全部K路prefill、增强图编码、双视图tokens驻留与逐层hook成本。

## actual唯一owner与差额

ROADMAP `MULTIMODAL-REPRESENTATION` Ch23。实际96–124全局部直接顺读：原MOH移对象diagnostic、SCR two-pass空间搬运、early/late soft-mask、VLI anchor/context派生视图hidden差分及加性正交条件、音频原/静音input-specific差分到最后读出。已有hidden差分非真值、强干预/旁侧质量和全费用约束，不能借这些成熟论点计新增；但没有**prefill随机剪原tokens→按层首次方向cache→所有后续生成步骤复用**的时刻/位置与失效分责。Ch17拥有通用residual intervention、Ch66拥有grounding评价，不新增二owner；不以所有幻觉问题都需此cache或主题相似泛NC。

拟插在VLI两段后、音频差分之前两段，保图像派生原分支与音频consumer承接。只有非作者Source/owner/PRE与root协调窄写后再实际POST。

### 逐字PRE

差分方向还可以在生成开始时生产，再缓存给后续步骤消费，而不每步重造派生图像。一条受限视觉分支保留原输入，只为负侧随机剪掉大部分 vision tokens，在首次前向比较原/负输入的浅层 hidden，按层平均差值；后续生成把这个初始方向与当前 hidden 分别归一化，组合后恢复当前幅度，中层另从原图与增强图 tokens 读取 context。原/负输入、采样、层、对应 token 位置和缓存有效期共同定义接口；删 token 改变长度与位置，不能隐含补齐矩阵对齐，更不能因保存幅度就认证语义不变。

[One Token, Two Fates 的有限对照](https://arxiv.org/html/2603.10360v1)支持这条局部分支，但初始差分不是每步的真实幻觉原因。共同语言偏差的消除依赖相同加性分量，剪 token 后的非线性视觉—文本交互和后续状态变化未由这个假设覆盖；增广图也可能改变任务真值。局部对象问答、caption 和消融有收益，也有更强基线切片，单 token 测时不替完整 K 路 probe、编码、驻留、hooks 与调参费用。输入语义、方向有效期、旁侧任务或总预算失配时，保留原 forward、已验证的局部干预与独立 grounding，而不让 cached hidden 差分批准事实或部署。<!-- source-family:SF-2026-ARXIV-2603-10360 -->

## 最小停点

必要Source/actual owner与逐字PRE ready，拟5分局部差额深入，待非作者按原源和当前owner核。未写Books/未formal，未读pixels/代码不伪造外部受阻；不授因果强保证、复现或DAY。

## 后续实际完成（覆盖上述准备停点）

root非准备者实际必要Source/Ch23完整邻接/PRE通过后窄写VLI后/音频前两段；SUP_POST_10360.md记录本作者非Books writer实际順读109–131完整局部/本人末注并回Eq6–11，PASS。root实际接纳、本人末注同步PASS并释放本两段窄锁；已formal第32项，5分必要局部深入/唯一MULTIMODAL-REPRESENTATION Ch23整合。未授DAY、alignment/sign实现、因果真值或全费用，原受限采用和反侧不变。
