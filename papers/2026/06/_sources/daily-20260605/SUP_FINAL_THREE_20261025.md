# 06-05 最后三项：必要证据与具体 Books 判断

最终逐项落实：R119由root实际读回RAMPART原单段/完整上下段/真H2简注、Multi-SPIN原两段/完整上下组/真H2简注后通过，两个整合生效；EvalStop具体Ch31已有覆盖已R118通过。当前34正式=27整合/6已有覆盖/1DistIL争议，本批无剩余写入或审阅待办；R120完整日级验收通过，Report完成。以下R118保存前/待POST措辞仅保历史，不重开有效层。

当前落实（R118）：root一次独立必要/actualowner校准通过三项5/5/6。**EvalStop校正为具体已有覆盖**：actual Ch31“训练停止不能只看 Training Loss 或 Reward Model Score”两完整段已承载eval→patience stop proposal→training owner提交→scheduler消费释放及参数模拟/误停/费用，不能因作者漏读该具体段误写仅报告；原证据/5分保留，不新写正文或注。RAMPART原单段与Multi-SPIN原两段已按新窄授分别真SAVE Ch75排序段后/exemplar前、Ch48异步段marker后/稀疏gate前，各加真H2下简洁来源注；完整新增/直接双侧/本人注已自读，待root唯一actualPOST，不预两项I。写前快照目录 `/private/tmp/jun05-last-two-save.6cBdUz/`。下文提案时的“未写/仅报告”均保留作判断历史，不覆盖本段。

仅补2026-06-04北京时间自然日。RAMPART的R89–91、EvalStop/Multi-SPIN的R97完整题摘、准入及Jun04联合日证有效复用，不再取日期或初筛。以下首次读取精确v1必要域并给正式评分，独立复核未完成前不声称整合。原件均官方HTML GET200：04628为224136bytes/SHA256 `bba34cafede7e54c509177e1b1cc495825249cca8b28d0faeef63bd4e8f78ef1`；04145为247839bytes/`c1063c261da2edf71aa598e2b85eb5c56d2e8c92f0545dc498d4e10e1ede6c2a`；04581为462642bytes/`ab97209f328e368c55254575b6c60472a3949cba26cb20a6cc399dc1ec0da618`。本地原件为本目录 `SUP_<arxivID>v1_20261025.html`。没有实现/复现实验或生产测试。

## RAMPART — 2606.04628v1

[原文](https://arxiv.org/html/2606.04628v1)。实际读§2.1–2.6全部接口、§3.1–3.2/F1–2完整文字图注、§4/T5及§6的直接安全/协调保证；未读图曲线像素、代码或后版。所采不是纯RAM、OrderedDict、五算子、registry命名或zero-token宣传，而是原文受控位置实验引出的**block组合及内部顺序也是compile-time变量**。

### 支持与直接反侧

- Registry保存content/priority/source/author/removable/run等字段；compile依次gate→ordered walk→budget cutoff→access count，evict为显式操作而非compile自动触发。默认MiniLM只看前256tokens，cosine不能分相同词汇相反意图；fine-grained block与换encoder均增加编目/embedding成本。UUID、removable与provenance本身不是权限证明，未核实现。
- §3是31-block firmware seed的合成probe：任务要求500Hz/PB7/TIM4输出，关键块含虚构无参函数名；checker只检查非注释行的literal，**不检查真实调用/编译/完整任务正确性**。空registry 0/20、单block15–20/20的首段与后段18–20/20口径并存，不统一数字。五模型Q4/Ollama/RTX5080、每格20任务；Qwen3-8B三task seeds，其他模型各一run，不能当多域独立复制或稳定CI。
- 单块移动会同时改变绝对位置与邻接内容，原文明确承认混杂。将关键块与两输出format邻居作为三块组移动，关键块位于组后时在局部post-cliff区域好于组前/单块；替换两format块为中性filler后bump减弱但未消失，故只能说邻接贡献未完全解释，不证明attention内部因果或固定通用最优位置。五模型复用同seed/task/scaffold，相同绝对位置不等跨领域规律；小模型full-stack与大模型plain/scaffold不同，不采小模型普胜。
- Gate为1405 vs4367 tokens，成功仅5/20=25%；“恢复promoted83%”只是该低分分母，不写成83%绝对可靠性。每次embedding/gate、compile、全部probe/失败推理和回归均付费；方法调用不产生prompt token，不代表0CPU/GPU/通信/工作流成本。T5约35万是每次转交都额外调用模型的naive上界示例，非实测工作流或合理baseline净收益。
- Schema present100%/evicted0%只是该未知名字的输出probe，未披露该子实验独立样本数。§2.3/4/6从“没送schema”推到任意prompt不能调用/立即权限撤销/transparent erasure过强：已有模型知识、历史、其他目录与真正executor未被控制。只采该条件观察，不采安全保证；可见view移除不删除模型参数/其他state，也不替服务端授权。§2.6承认well-ordered writes、同registry无并发；fork COW是继承私有地址空间，不等跨进程实时共享修改，GIL不构成跨进程一致性。直接引用只支持同进程/预编排交接，不采任意零通信多Agent协调。

### 评分与 actual owner

Design Delta2＋System Reach1＋Durability2＝**5**。评分给position×local composition的受限替代组装操作和控制变量分离，不给成熟bookkeeping/权限原则加分。安全主张直接反侧一并深入，中心安全保证不采用，局部组装证据仍独立成立。

实际读 `AGENT-CONTEXT` Ch75:82–122 assembly完整组、262–286 semantic-policy/bookkeeping、653–666 mutation/owner，邻Ch74/76开篇；并定点读Ch78:16–72实际executor/schema授权和Ch82:12–65共享证据/成本。现文承载显式filter/rank/place、相关性不等authority、相邻turn连续span和state-owner提交；这些不为原文registry再复制一遍。尚未承载的是**同一关键指令的位置效应与局部format邻居混杂，须固定composition再测位置，并允许cluster内部顺序作独立设计变量**。不是仅因缺family marker认gap。

拟一段，插在Ch75 `排序不能只看 embedding similarity...`完整段后、`当检索内容用于改写下一份prompt...`完整段前；不改相邻原文，不赋Ch77持久化owner，也不写安全保证。

> 把内容选入Context后，放置还可以按有关联的块组，而不总是独立给每块排一个位置。一个受限做法先固定关键指令及其输出格式邻居，整体移动该组并改变组内先后，再与单块移动及中性邻居替换比较，以区分绝对位置和局部内容组合。[RAMPART的合成指令probe](https://arxiv.org/html/2606.04628v1#S3)中，关键块跟在两format块之后可改善部分位置，替换邻居后残余信号仍在；它不证明统一attention机制或所有任务的固定最优位置。这个分支增加分块、诊断调用、编排和回归成本，literal出现也不是实际任务完成；任务、模型或邻接内容改变时，应重验或保留简单固定排序/完整指令。未进入这次view的schema不等于executor撤权，授权仍由工具执行边界检查。<!-- source-family:SF-2026-ARXIV-2606-04628 -->

## EvalStop — 2606.04145v1

[原文](https://arxiv.org/html/2606.04145v1)。实际读§2–5/完整Alg1/T1–5/F2–5文字图注，A/T6参数与B/T7、C/T8–9直接反侧。没有实际RLHF轨迹、代码或系统运行；原文自己把真实trace replay列为主要缺失验证。

### 支持与直接反侧

- Alg1只看job type/已到checkpoint的eval与连续下降计数；score相等/上升清零，RLHF k2/DPO k3。下一次schedule先terminate/release/save best，再交任意base scheduler；不是新RLHF优化算法、置信检测或“不可逆下降”判定。k次连续下降只保证相对最近score下降，**不保证global-best恰在k次之前**，原文该说明过强；另存best identity/持久化和安全终止需要真实实现核验。
- simulator200jobs/5tenants/5seeds、Poisson λ1job/min、32/64同构GPU、preempt2min；RLHF60%参数化峰0.55–.75后降.10–.30，40%healthy单调凹加噪，两者loss都在.5–.7plateau。隐藏标签的whitelist只阻直接读label；标签与待检eval曲线形状是同一生成模型，**不是独立真实reward-hacking标签**。本实验不能证明现实eval下降就是reward hacking、world truth或训练今后不恢复，也不证明任何loss-only特征都无法区分。
- E2 T1中SRTF1124±59→1018±53 JCT、waste34.5→26.9%，作者给Welch p.03/<.001；仅5seeds且未给配对/多重比较校正，不外推生产。固定stop0.5 JCT622更小却healthy FPR64.5%，说明此模拟的人口内JCT单指标会奖励误杀；不是现实FPR估计。FPR/precision的精确定义、eligible/censoring人口和T1“每个RLHF都stop”却64.5%FPR而非100%的关系未充分披露，不替补实现。Jain公平“within noise”未给具体数值/CI，不能签公平无损。
- T2 SJF gain6.5%反驳文字“所有9–25%”；T4 σ.05时recall88.9/FPR7.2%，σ.12为69.6/14%，不能泛写稳定98/99。Gaussian iid噪声不代表correlated/heavy-tail。k1文字127与Fig3 caption160差额保留，采用T8=127不合并。T9 30%eval的waste29.8低于20%34.2，非随频率单调；低stop下分母人口及计量协议未闭，不强作规律。
- A固定eval1/3/5min确实占GPU，不能说完全忽略eval费用；但eval频率作为外置扫描参数，不是联合调度决策。checkpoint保存/载入、真实网络/gradient accumulation/elastic、模型/precision/输入输出与安全取消协议未披露/不适用于此模拟，不把64GPU当真实硬件测试。误停后后续QA、tenant效用、best真实持久与恢复成本均需另验。固定预算/人审early-stop在简单场景仍合理。

### 评分与 Books 提案

Design Delta1＋System Reach2＋Durability2＝**5**：对研究中的stop-before-reschedule接口和模拟中quality误杀—resource指标冲突给标准审阅，不把成熟early stopping、释放GPU或proxy原则说成新机制。正式保留候选，不因实验较弱删除已读证据。

原拟仅报告，经R118 actual-owner复核校正为**已有覆盖：TRAIN-RLHF Ch31“训练停止不能只看 Training Loss 或 Reward Model Score”**。作者本轮实际补读该标题下两完整段：明确按版本Evaluation Run生产downstream evidence、RLHF controller依持续下降/不确定性/patience提出stop proposal、training owner提交、scheduler只消费资源释放；第二段已保额外eval/延迟/judge drift/误停/公平、固定预算/多窗口或人工回退、Poisson/slot GPU/两分钟抢占及参数化LoRA/DPO/RLHF曲线边界。这不是从Ch31泛proxy风险或Ch63资源原则推断覆盖，也不是说现章实现了具体detector；所采机制与模拟证据边界已在唯一owner承载，无需新增正文/注。真实trace、独立质量标签和完整误停/保存成本若改变选择，再定点重开Books判断。

## Multi-SPIN — 2606.04581v1

[原文](https://arxiv.org/html/2606.04581v1)。实际读§II–VI/Eq1–39/Alg1/TI与Fig3–8文字图注；为整数最优/alpha单调边界定点读AppendixD–G，不扩A–C全部证明/图曲线像素/代码。数学形式从HTML math alttext实际读，不从摘要88%反推机制。

### 支持与关键边界

- 一轮同步设备draft+uplink，收齐K个后server一次batchverify，后返回prefix。同构L/alpha时每轮产出KΣ_{l=0}^L alpha^l；clock为 `L max_k(Tsk+Qtok/(Bk rk)) + Tver(K)`。固定L时minimax带宽唯一解等化各用户per-token latency，`Bk=Qtok/[rk(vartheta−Tsk)]`；这是已知静态参数、无限细OFDMA和正带宽条件下的模型解，不是公平定律。较慢compute/坏channel为了追齐会获更多带宽，与“只按acceptance分配”不同。
- 异质Lk时同一barrier仍在，clock变为 `max_k Lk(Tsk+Qtok/(Bk rk)) + Tver(K)`；不是取消同步或async inference。固定整数Lk可等化整段latency，`Bk=Qtok Lk/[rk(phi−LkTsk)]`，phi>max LkTsk、总带宽B。长度和带宽不能各自独立调，因为拉长某端会改变共同最慢界与全体份额；这是可采用的具体资源模型/接口增量。
- alpha按dataset的经验mean，模型假设各position iid且当前task/profile已知；Eq12计算的是保留prefix再加replacement/bonus的**本轮输出进度**，不是只accepted-draft的计数。mean alpha不能保证真实prefix survival或每request质量，部署新流量须估计/重验。目标sum-output/共同clock不含最低用户goodput/fairness/尾SLO，不授fairness。
- V.C两步relaxation后声称不改原整数最优，但D只证带宽不等式tight，没有证整数连续放松/独立round无损；E最后一句直接诉round规则，未补离散全局最优。Alg1按bounded phi/lambda grid算continuous再round、重新解phi，检查预算仅给模型可行候选，不证明任意grid覆盖整数optimum；零/边界L、grid resolution与完整舍入验收未闭，不采“线性复杂度恢复全局最优”。IV.B derivative式正倒数却标<0有漏负号；真实root关系给带宽增大clock下降，不能照抄错式。
- Remark2“Bk随alpha严格增”在F对beta求导时将共享phi/lambda当常数，且integer round可成平台；没有证明重新优化全部公共变量后的全局严格比较。只可描述连续固定共同控制量下的倾向，不把它写成任意异构/网络的资源分配反转定理，不必为未采用该保证扩全部proof。
- 经典ratio accept/校正从成熟算法引用；网络只保1024词概率并Q_B16，却没有给截断/重新归一化/尾部calibrated residual协议和误差界。不能因“量化negligible”或标准公式就签真实分布保持。OFDMA rate用已知每round常量channel/continuous B，忽略downlink/控制开销，Tver只拟合K的affine而不显式含max draft/padding/prefix length；实际zero padding、KV状态/tokenizer与cache回滚另需验。这里不授exactness、真实端到端SLO或通信安全。
- VI仅M4Pro测每token延迟再抽±15%造设备人口，serverA100拟合Tver；单cell K20/B10MHz、独立blockfading为通信模型，非20台真实端侧/真实无线部署。TinyLlama1.1B/Llama2-7B与Qwen3.5 .8B/27B四数据集，alpha从sample估计，每device50prompts×10随机channel/compute。precision/序列长度/完整timing/实现与seedCI未披露。88%相对固定L8+平均带宽且仅最小B，带宽增大gain收窄；不能授最优baseline普胜。P2P单device vs多deviceaggregate也非同并发端到端倍率。所有profile、alpha估计、搜索/调度、PMF截断编码、控制/上下行、两端KV与padding成本均需另计。

### 评分与 actual owner

Design Delta2＋System Reach2＋Durability2＝**6**。评分给共同uplink预算下的draft长度—straggler barrier联合控制；不是普通speculation、OFDMA名称、88%或未经证明整数最优。只采用条件资源模型，中心最优/严格alpha比较及分布保持不作为正面证据。

实际读 `INFER-SPECULATIVE-DECODING` Ch48:78–95 WISV/HyCo网络与语义分责、337–366联合depth/verify与per-request异步完整组；也看Ch47/49开篇交接。现文已有端侧通信协议、acceptance不是goodput、同步barrier与async替代、ragged预算/公平，不需重复这些通用句。最小未承载差额是**保持同步barrier时，接入网络总带宽约束使每用户长度和份额不能独立求最优，固定长度应先等化对应clock**。把具体joint resource模型放Ch48，集群placement与通用无线优化不在这里另开owner。

拟原Ch48 `<!-- source-family:arxiv:2609.17943v1 -->`（前方完整per-request异步段）后、`更细的请求预算也不要求在每个 draft depth...`完整段前，以下两段，不改邻接：

> 不消除同步barrier时，端侧draft还可与共享接入带宽联合分配。设设备k起草Lk个token、每token计算Tsk，上传每token概率记录Qtok，所得带宽Bk与频谱效率rk；一轮等待可近似写成 `max_k Lk(Tsk+Qtok/(Bk rk))`，再加server的batch验证时间。[Multi-SPIN的条件模型](https://arxiv.org/html/2606.04581v1#S5)在给定长度、已知稳定参数和可连续分配带宽时，先等化各端整段draft-upload时间，再比较长度组合；统一长度下等化的是每token时间。因而改变一端长度也会改变共同最慢界与带宽份额，不能把各请求的单机最优长度与平均带宽直接拼成共同最优方案。
>
> 这只是proposal资源控制，不接管target验证与提交。模型用逐位置iid的平均acceptance估计输出进度、忽略下行并把验证时间近似成batch-size函数，不能直接描述真实prefix survival、padding/长上下文或尾延迟；连续放松、整数取整与有限搜索也没有自动获得离散全局最优。Profile、acceptance估计、搜索、完整概率上传与控制往返均计费，截断概率后的residual与状态回滚须另验，sum-goodput不保证每用户公平。链路、人口或净费失配时，保留固定短draft、保守带宽/同步batch或target-only，再用完整轮次和质量回归验收，不从低带宽下相对固定baseline的局部收益签发exactness或SLO。<!-- source-family:SF-2026-ARXIV-2606-04581 -->

## 本批状态

三项必要与正式评分/具体owner提案已完成作者层，待root一次独立核验；RAMPART5分单段和Multi-SPIN6分两段均未获得写授权、未SAVE/注/POST/I。EvalStop5分拟仅报告，不以访问/费时/Books已有覆盖降分或删候选。SaliMory原两段已按root新窄授真实SAVE，root R117唯一actualPOST已通过，当前可采用I25；无额外行政轮。普通下一步仍是本批独核/具体必要写入、finite发现stop及最终六节/DAY，不冒外部归零。
