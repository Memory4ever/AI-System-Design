# TRiMS17449：有限采样/截断与尺度接口待独核

resume_mar17，2026-10-11，仅03-20补03/19。原完整题摘/日级夹证与2+1+2=5复用本日批5独核§13；必要原证与actualowner准备，不自授Source/PRE/safe/DAY，不写Books。

## 1. 必要实际源与停止

[exact-v1](https://arxiv.org/html/2603.17449v1)§3–4/Eq1 L144–224、§5/T1–2/直接限制 L225–329；A1–2/Alg1 L392–461、B1/评价/对照 L463–540、C/Eq8与D1/T4/T5及D3仅受影响阈值 L541–603。没有读E案例图像或代码，不核整份references/附录图片；HTML返回包含未采范围不计审阅。current official abs轻量身份/history仅v1，无具体纠错触发，不开版本差。

§3的递归Lk=min(Lk-1,li)，错答案赋16384，只证明该有下界样本最小序列收敛。该对象取决于模型/prompt/sampling/正确性oracle/长度上限，全部错时也收敛16384而不提供正确路径；极限不等其他policy/latent路径的必要推理长。有限样本只给当前支持中的观测上界，RL更新采样分布，不由“在原能力内”句证明支持/极限不变。A1只保留前16次至少正确一次的问题，再每difficulty至少50，512次曲线属条件人口，不能称无选择偏差。

## 2. 直接数学反侧与不采范围

A2 Alg1按correct lengths的sorted unique T累加无间隔权重的survival概率，且m数的是L<t而注释称Pr(X>t)。独立反例：n=2，correct lengths=[100,200]，k=2；真实不放回二抽样最短恒为100，伪码在t=100加1、t=200因n-m<k跳过，返回101。k=1返回100+1+1/2=101.5而真实均值150。错误不靠零correct端例；伪码还在最终平均只含solved问题，unsolved16384不进同一人口。这不支持宣称unbiased SCPT/已测固有必要下界，未采用此算法recipe或headline MSL充分性。需要一次定点修复：给出含token长度间隔、边界严格性及unsolved人口一致的估计器/最小数值trace，并区分固定policy支持极限与在线更新目标。

可独立核验的有限接口在§4：已采样group若有正确回答长度<2048选较短档，否则4096；Qwen3改为2048/4096/8192三级，不把这视为逐题连续MSL值。顺序/是否重采或截断完成答案的实际runtime未披露，不补成部署scheduler。全零/全一组在advantage前被过滤，改变有效训练人口且已支付采样；Eq1仍以同题mean居中，只把分母换为整个batch reward std。对于非退化binary组，sumA²=G*groupvar/batchvar，稀疏组的相对权重因此改变，不等梯度范数证书、无偏或所有任务稳定。数值zero-batch守护及全未保留batch退路仍必要，不自行授实现已核。

## 3. 关键评价/费用与直接失败

R1-distill-Qwen1.5/7B数学训练DeepScaleR/verl；8A80080GB、batch512、300update、G16、FSDP/CPUoffload、温度1/topP1、checkpoints10steps已披露。B1 beta.001与C KL objective分开：不加KL到reward不等不加KL正则。推理温度.6/max16384、AIME16次重复披露，但inferHW/precision/batch/concurrency/SLO、其他数据seeds/CI、弃样/512探测/选择checkpoint/全训练与验证费未齐。

T1 7B AIME51.7→49.6、Olympiad54.8→54.4，不是allbenchmark准确改善；D1 T4 Level2 .9333→.9111/Level5 .6567→.6493与文字everytier维持冲突，D4 T5 Qwen3 AIME57.9→53.5/MATH91.6→91/Olympiad58.2→57.9，Avg -.63属相对平均而非每task同值。5.4同其他hyperparams的group-vs-batch尺度对照支持受限稳定观察，不单独证明完整dynamic/truncation三部件因果；图像maxadv/AMC曲线不授像素复验数字。B4使用不同公开trained checkpoints，只有部分同dataset，不把same-base当same-total-budget。关键字减少不是必要推理步骤真值；IPT=Acc/avgToken与预算并发图不等完整latency/费用。

## 4. actual sole owner 与最小差额

实际Ch33 90–155：107已有同题mean+按difficulty桶batchstd的分工，140–150已有zero-group/生成前admission/探测后front人口。但没有把当前有限correct-length档位与零方差组过滤、全batch尺度联成同一受限训练条件；也未区分fixedpolicy样本最小收敛和online更新的预算sensor。Ch32/34入口实际读，PPO clipping/偏好离线非此人口接口。拟sole TRAIN-GRPO，原107 difficulty-bucket完整段后/109 speech-text比较人口前两段；旧每题/std桶/普通outcome保持。若独核认为实际覆盖足，须指出上述具体联结承载段落，不因忙降分/NC/EX。

## 5. 两段逐字 PRE（待非准备者裁，未授写）

正确轨迹的长度还可以作为训练预算的有限探测信号，但采样到的最短长度只是当前模型、prompt、采样和verifier条件下的观测值，不是完成任务的固有必要长度。错答案赋一个长度上限后反复取最小，即使所有样本都错也会收敛；有限正确样本的最小值不能认证新的policy或其他表示路径的下界。一个受限分支从当前group是否已经出现较短的正确回答选择粗截断档位，并在advantage前过滤全零/全一组；它改变的是预算和有效训练人口，而不是获得在线正确性oracle。探测/弃样仍付费，样本最小与截断后的最终正确率要分验，不能由输出更短证明必要推理均保留。

[有限截断训练对照](https://arxiv.org/html/2603.17449v1)仍按同题reward mean居中，却把归一化分母改为整个batch的reward标准差；非退化二值组的总advantage平方因此按本组方差与batch方差之比缩放，而非每组固定同一能量。共享尺度并不认证梯度稳定或无偏，零batch方差/无保留组须有退路，筛组和截断也会改变训练人口。实验存在任务和难度切片反退，有限最短路径估计器的无偏/普遍下界不采用；更多探测、完整rollout、验证、调参和训练均计费，不把token/IPT收益当全链时延。Verifier或预算信号失配、质量回归时，保留普通outcome GRPO、每题或已校准分桶尺度和更宽的rollout预算，以独立答案质量、人口覆盖与全费验收。<!-- source-family:SF-2026-ARXIV-2603-17449 -->

静态源注：`SF-2026-ARXIV-2603-17449` — [TRiMS exact-v1](https://arxiv.org/html/2603.17449v1)§3–5/Eq1/T1–2及A1–2/Alg1、B/C与D1/D3必要反侧；只有限correct-length预算/筛组与batch尺度接口，不采用unbiased SCPT/固有必要下界、完整runtime recipe或普遍压缩保持；人口选择、任务反退、zero守护及全费保留，未核代码/复现。

支持及关键反证够此提案即停止。中心数学外推与可核有限接口是否可分采交非准备者独核，原5分保持，不自授center终态/NC或整合。

## 6. 授权窄写与 writer 实际读回

resume_mar17：reader独核§20有限Source/actualowner/两PRE正式通过，root明确授Ch33本family两段及静态注唯一窄锁。原107完整分桶段后逐字插入两PRE，仅第一段加同family来源marker；原speech/text人口段与其他日期内容保持。writer实际顺读98–123完整前后链与末6行自身/邻注，限定diffcheck0；未将该写入算非writer POST或DAY。待reader一次完整局部及自身注actualPOST，Books注不复制流程身份。
