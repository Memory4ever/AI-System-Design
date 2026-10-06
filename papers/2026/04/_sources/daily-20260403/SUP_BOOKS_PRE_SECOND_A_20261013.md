# 第二批前三项唯一owner差额与逐字PRE请求

## 当前actual层

root actual PRE核后授Ch27/22两窄锁，作者已写核准两段及本人静态注。root nonwriter POST实际Ch27 1146～1167/本人1372、Ch22 177～200/本人1204通过：完整原OPUS/gradient子空间与位置index保留，surrogate/validation/全部费、linear storage非time/float边界近文，两锁释放。00028原Ch43 PRE因原证LQ=1 decode已撤，Ch43未写；改唯一Ch44 PRE经root actual读单请求/HBM→R batching/MoE交接后授单段/静态注。作者实际Ch44单段126/本人344及完整111～139写后顺读，待root nonwriter POST，未DAY。

随后root actual nonwriter POST实际Ch44 111～140/本人344通过，单段与Source/PRE的decode阶段、CTA供给及metadata完整费用一致，Ch44窄锁释放；Ch43保持未写。

root已实际必要Source通过，未授本文件任一Books锁。完整重读当前AGENTS/ROADMAP/PROJECT_CONTEXT/学习理念/写作指南及相关2026checkpoint；实际owner局部与相邻交接已读。以下每项仅拟正文及本人静态注，不改其它family。

## 00001 / TRAIN-DATA / Ch27

文件`books/part-04-training-system/27-data.md`。现OPUS段已拥有raw-vs-optimizer有效update、linearization/proxy/Hessian近似及费用，不重复它。差额是**subset成员与非负权重的联合残差目标**及raw Gram/target-preconditioner分责，不把Gram换成一组独立cosine。实际顺读Ch27 1133–1178、Ch26开篇与Ch28开篇。

完整PRE锚：现完整OPUS段（从“在线选择若依赖梯度”至“trainer 仍独占最终 update commit。<!-- source-family:SF-2026-ARXIV-2602-05400 -->”）之后，下一段完整首句“选择几何也可以来自小目标集的梯度子空间，而不是当前 optimizer 的有效 update”之前。拟两段：

仅按每个候选与目标方向的对齐排序，还没有处理多个被选样本怎样共同构成一次更新。另一条条件分支把选择写成集合残差：候选保留 raw gradient 的 Gram 关系，先用单位权重的残差匹配筛成员，再对这组成员求非负权重并聚合。Adam 当前方差状态则通过线性化移到目标梯度一侧，避免把每个候选都重复送过完整非线性更新算子。这样选择器同时提出成员和权重，但匹配的是冻结上一时刻方差后的局部 surrogate，不是精确优化当前 Adam 的真实效用；二阶效用解释还需要相应 Hessian 简化。

这一分工须共同保存 candidate/target 梯度、optimizer state、投影方式、成员与权重，特别不能把旧的逐坐标二阶 moment 直接投影成新的低维二阶状态。[受限选择实验](https://arxiv.org/html/2604.00001v1)中，少用样本而维持相同步数仍有任务低于完整训练；目标 validation 梯度既已参与选择，最终质量就须由另留的 held-out 人口验收。候选与目标 backward、投影、Gram、非负求解及状态维护都计费；近似、目标分布或总预算不可靠时，保留独立方向排序、随机/分层子集和完整数据基线，不让集合残差替 trainer 提交更新。<!-- source-family:SF-2026-ARXIV-2604-00001 -->

本人静态注拟加在Review notes首段之后：`SF-2026-ARXIV-2604-00001`，v1§3.2～3.5/Alg1/§4.1～4.4，2+2+2=6；限定surrogate/target-preconditioner/raw Gram、unit filter→NNLS，270K/5%及同step非同compute，QwenMMLU46.23<46.59、validation选择隔离、未复现。

## 00004 / MODEL-LONG-CONTEXT / Ch22

文件`books/part-02-model/22-long-context.md`。现179–194把位置/训练有效性与容量分开，接index一致性，但未解释native/scaled关系恢复或dense关系目标的memory与compute分责。实际读175–205、65–170及Ch21/23开篇交接。完整锚“因此这条路线的主要输出是模型有效性，不是系统容量。”后，`### 位置索引一致性需要保持内容与可见性不变`前。拟两段：

位置扩展还可能先损伤原短窗口内的关系。一个受限恢复分支让 teacher 使用 native RoPE、student 使用 scaled RoPE，在原窗口上匹配每行归一化的 Q–Q、K–K 与 V–V 关系，再以较轻的长序列 continued training 适配新距离。前一阶段约束内部关系保持，后一阶段才接触长窗训练分布；关系 loss 下降不等于原 teacher 能力完整恢复，更不保证新的距离已有效。[受限对照](https://arxiv.org/html/2604.00004v1)同时存在短任务恢复不足与长检索低于普通 CPT 的切片，因而普通长训、较小 scaling 或原 checkpoint 仍各有合理位置。

关系蒸馏不必把整张平方大小的概率图留在显存中：先逐行累计 teacher/student 的 log-sum-exp，再按 tile 重算概率及梯度，可以保留同一个 dense 关系目标而只保存线性规模的行统计。这里节省的是驻留中间状态，pairwise 计算及反向重算仍随长度二次增长；数学梯度一致也不意味着浮点 reduction 的 bitwise 一致。双模型前向、重算、适配参数与后续 CPT 均进入预算，不能把较少蒸馏 tokens 或线性 workspace 当成 linear Attention、总训练免费或部署 TTFT 保证。数值、短长任务或总成本验收失败时，回到原 dense 目标/常规 CPT，并分别记录位置、训练目标与实现版本。<!-- source-family:SF-2026-ARXIV-2604-00004 -->

本人注：v1§3.1～3.4/Alg1/Eq4～7、Tables1～2，6分因具体差额深入；native/scaled、row-FKL、LSE-recompute只linear storage非time，Llama2短51.87<54.69、Llama3RULER68.3<81.3，未核实现/复现。

## 00028 / INFER-DECODE / Ch44（修正阶段归属，未授锁）

文件`books/part-05-inference-system/44-decode.md`。root实际原证指出LQ=1是低head decode；原Ch43 PRE会误导，已撤、不曾写Ch43。实际Ch44 65～158“单请求难以喂满GPU”及Ch43/45交接；owner已有请求batch提高weight reuse，但未解释同一single-query attention内部CTA供给与长度guard，不把两种并行性混合。

完整锚：完整段“`R` 增大通常提高 arithmetic intensity 和 token throughput，但会增加 KV 占用、每轮 work 和排队。更高吞吐并不自动意味着更低 TPOT。”后，下一`## MoE 怎样改变 Decode 的执行形态`前。拟一段：

请求 batching 之外，single-query Attention 自身也可能缺少足够并行 tiles：batch 与 KV-head 数很小时，按历史长度禁止 sequence split 的阈值可能使设备闲置，即使该历史并不长。一条[Hopper 上的局部 FA3 decode 分支](https://arxiv.org/html/2604.00028v1)在 query length=1、四个 key-block、低 tile 供给的受测形状上放宽 split，较短或已饱和形状保持原路径；它增加并行工作，同时增加分块统计与合并成本，不减少完整 Attention 的数学工作。metadata 预计算后才有清楚的 kernel 收益，将它放回完整路径后改善很小，因此历史长度、batch、KV heads、tile 预算、metadata 与合并必须共同作为 guard 和成本身份。纯 BF16 kernel 对照不授任意 short-context、完整 TPOT 或服务 SLO；实际请求无净收益、shape 越界或数值验收失败时保留原 kernel 配置。<!-- source-family:SF-2026-ARXIV-2604-00028 -->

本人注：v1§2～5/Table1，2+1+2=5，具体shape guard深入；C++nblk4/LK512、batch1/HKV1or2低tile split3，≤384与饱和保原。H100 BF16 CUDAgraph交错A/B，precomputedmetadata约1.21/1.24×，否则约1～1.05×，未核代码/合并/复现。
