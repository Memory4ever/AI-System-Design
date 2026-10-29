# Optimal Splitting 19149：必要证据与最小写入提案

root 准备，仅03-21补03-20自然日；非独立PASS，不计安全处置或DAY。题摘准入复用本日有限65项校准，不扩大来源或附件队列。

## 贡献与身份

[exact-v1](https://arxiv.org/html/2603.19149v1)把共享预训练与K个独立领域续训放在同一个预算中，拟合何时分支及分支后投入；有限增量是**剩余预算下的联合最优分配不同于最早边际分支点**，不是“CPT一定更好”或MoE token路由。拟2+2+2=6，跨基础训练/领域交付预算接口；采用长期缺口深入核必要内容，不给成熟Scaling原则另加分。作者已记录official v1/currentheader、DataCite created03-20T02:29:47Z/registered48Z与v1Updated03-20T01:16:16Z日级夹证；提交03-19T17:07:05Z本身不作公开时刻，非preparer核落窗后才列确定新增。HTML内部August24日期不改归属，也不据此冒版本对比；只采用当前可取的exact-v1有限机制。

## 实际读取与停止

root实际读取exact-v1 §3.1–3.2、§4–7；初次HTML正文局部截断已用原始HTML定点补齐§4–7。随后实际A/B/D、E.3、G.1–2，仅预算、optimizer/routing和拟合反侧；未遍历全部图、其他附录、代码或复现实验。

- §3/5：共享模型用D tokens预训练后复制K份，各自领域CPT D′；同模型尺寸预算D+K D′=D_T。领域分区/embedding/router本身亦有成本；不是只加一份CPT、不等全K权重免费驻留，也不等token-level MoE或合并回单模型。
- §4经验联合loss拟合以N/D/D_k与跨域转移项预测；E_delta和幂律渐近是所选函数假设，不是架构通用定理。G.1显式参数不可识别风险、范围约束、Huber/basin-hopping与剔除loss>4/<.5；不能R²高即认证可移植配方。
- §5先问最早边际分支点（K乘共享边际导数与单域导数的比较），再给定总budget找最优共享阶段t_s，后二者可能不同。图4脚注以一个domain loss近似所有领域sum；domain8拟合不能当所有domain严格最优证明。§5.1描述130 vsTable1 640测试数量矛盾，H/Table7训练测试数亦不同，隔离精确拟合计数，不据此引用统一预测精度。
- §6.1 DCLM decoder 100M至2.7B、16balanced clusters、batch1024/seq1024；1.3B 120/240/360B预算实验的t_s仅near fit，不是每点实际最优。§6.2有单760M PT优于其他分支预算区域。§6.3总FLOP匹配6.7B/140Btokens时，1.3B split不及6.7B，2.7B才局部更好；不能headline“普遍同预算超越两倍模型”覆盖反侧。
- §6.3.1/E.2 Pile为每个domain统一用most frequent routed expert，不是每文档prefix路由质量测量。D/E.3 QA按question/context；validation首32tokens router，R@1 .8775 vs64 .9663只是full-document cluster retrieval，不是最佳expert质量/安全保证。领域混淆/上下文变化会有额外错路成本。
- §6.4两cluster任务子集1–3点回退；K改变会重新分区，不能固定domain再机械外推收益。A reset CPT optimizer，PT-only固定LR/warmup10000 vsCPT reset后固定LR，表示初始化/optimizer共同影响，不作纯数据隔离因果；C数据重复与完整allK训练预算均保留。
- B成本仅H100 1.3B/2.7B约100Btokens GPUh报告，非匹配端到端CPU/GPU fleet、完整routing/storage/SLO。§7异步便宜硬件/私有数据为潜在用途，不授实测速度、隐私或生产保证。precision、runtime版本、推理concurrency/长度/SLO Not Disclosed；训练token预算不可等同服务latency。

支持与关键反侧已足，停止无关附件。报告只采用联合预算与局部可比较选择；数值律、最佳配方、纯数据因果、通用QA优势和部署私密性均不进入正文。

## Actual owner与差额

`TRAIN-PRETRAINING` Ch28实际1149–1183完整Scaling段：参数/tokens/compute/data四轴、固定family经验边界、循环共享执行/压缩预算已覆盖。未承载**先共享后分K领域时，有限budget同时拥有共享与全部分支成本，最早边际分支与预算终点最优不同**。Ch27归数据分区/provenance，Ch29行为SFT，不另建owner或重复解释router实现。建议generic compute-optimal完整段后、循环共享段前两段；无重大结构变化。

## 最小PRE（待非preparer核）

共享预训练再分成多个领域模型，还增加了一个预算维度：共享表示让每个分支复用已学能力，但继续训练共享模型与分别训练领域模型会争用同一份总预算。若固定模型尺寸、分成K个等预算领域，先共享训练D个tokens、每个分支再训练D′个tokens，训练账应计为D+K D′，而不是只登记一份续训。数据相近或预算较小时，保持共享更合理；领域差异足够大、剩余预算允许专门学习时，才比较分支方案。数据分区与领域归属由第27章负责，本章负责共享阶段和全部分支之间的资源分配。<!-- source-family:SF-2026-ARXIV-2603-19149 -->

不能只在“领域训练的边际收益刚高于共享训练”时立刻分支：这给出最早有利的切换点，未必给出固定预算结束时质量最好的切换点。应在声明的模型家族、领域划分和训练配方下，用有限对照估计共享与领域训练的联合质量前沿，并同时保留单模型从头训练、持续共享和较少分支的baseline。[受限训练对照](https://arxiv.org/html/2603.19149v1#S6)支持这种比较，不证明所有规模与预算都应分支；路由错误、完整专家权重驻留、重复训练与索引开销仍要计入，训练FLOPs相近也不等于端到端耗时、服务SLO或隐私保证更好。领域划分不稳定、任务跨域或小预算下分支回退时，保留共享模型而非强行专家化。

静态注：- `SF-2026-ARXIV-2603-19149`：[Optimal Splitting exact-v1](https://arxiv.org/html/2603.19149v1)，§3–7/A/B/D/E.3/G，仅共享PT与K分支CPT联合预算、最早边际点与总预算最优分责。保留单模型优势区、1.3B对6.7B反侧、领域聚合而非逐文router评价、optimizer/partition混杂、拟合可识别性/计数矛盾与完整成本；不授普遍最佳分支、privacy/异步hardware实测、recipe或复现。

## resume_mar18 非准备者有限复核

恢复本21实际重载当前合同/ROADMAP/Books上下文后，独立打开official exact-v1 AB/currentheader/history与真实DataCite字段：唯一v1 Submitted03/19T17:07:05Z，created03/20T02:29:47Z、registered48Z、v1Updated03/20T01:16:16Z、AvailableMar/statefindable，与本批日级夹证一致，仅支持BJT20 arXiv事件限定归属，不冒别处无先稿。exact-v1 PDF封面March20,2026，HTML封面August24；不以HTML渲染日期移动归属，也不声称全版本已比对。

本人实际HTML §3.1–3.2/4/Eqs3.1–5.2/5–7（L117–290）、A/B的optimizer与成本、D/E.1/E.3（L357–425/455–468）和G.1–2拟合/外推（L473–496），不遍无关图或附件。K个独立续训的D+K D′、固定预算优化与零CPT处的边际导数比较确为不同问题；domain8代理和130/640矛盾不能认证全领域精确最优。实际§6.3.2 1.3B输6.7B、§6.2单760M有优势区、Table2子集退步与K变化重分区均保留。A重置optimizer/不同warmup不授纯数据因果，E.3前缀cluster retrieval不授最佳expert质量；B GPUh不是端到端生产费用。D披露lm-eval-harness commit及cloze格式，不把这个评价版本称ND；训练/runtime部署配置、precision、并发、SLO仍未足以认证生产比较。

实际Ch28完整1152–1188 scaling→循环共享→压缩预算，以及Ch27/29开篇，确认既有四轴预算没有解释共享阶段与全部K分支的有限预算联合分配、最早边际切换与终点最优分责。原两literal PRE/静态注只采用这条条件接口，反侧与退路在正文；Source/date/actual sole owner/PRE正式有限PASS，2+2+2=6不变。未写/未授actualPOST，不预支safe或DAY；无需扩大recipe、证明或版本史。

## 一次实际nonwriter POST

root solewriter授权窄写后，resume_mar18非writer实际顺读Ch28完整1152–1180、新1163/1165及末九行/本人1880与MUD/Muon等邻注，逐字回原两PRE/本人静态注及已独核的必要原证一致。四轴预算→共享/K分支终点分配→循环共享容量/执行深度的推进成立，不把独立专家化等同MoE，不删除单模型、较少分支、route错误和完整成本反侧。marker/本人注各唯一，限定diff-check空；实际POST正式有限PASS，待root接纳释放窄锁与归并I。无需动态改静态注身份或重审源，不授DAY。

## root 实际窄写

非准备者PRE通过后root sole writer在generic compute-optimal完整段后、循环共享前写两批准段，actual Ch28 1163/1165及末尾1880静态注；本人实际1152–1178完整前后读回逐字一致，scoped diff-check空。待resume_mar18非writer一次实际正文/完整邻接/自身注POST；未计安全或DAY，不改旧有效内容/验收身份。
