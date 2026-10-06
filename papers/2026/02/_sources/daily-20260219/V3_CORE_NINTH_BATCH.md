# 第九批必要核心

五项完整精确v1题摘经root实际准入校准；15400仅一次决定准入core，不默认全文。日期各identity Submitted与原Created/Registered共同完全落窗，不借相邻ID、Updated。尚未运行实现或复现。

## 2602.15397v1 ActionCodec — 2+1+2=5，必要核心/直接反侧完成

[精确v1](https://arxiv.org/html/2602.15397v1) §4–6/Fig3/6/Tables1/3/5、A1设置/A4定义定点actual读。动作codec并非重构最低就最好：邻近chunk overlap与token budget、语言alignment、token相互依赖分别对照，independent Perceiver仅crossattention可减少早token扰动传播；不是codes统计独立证书。RVQ后训练freeze encoder/主codebook补残差，不以高fidelity牺牲首级稳定性。AppendixD承认确定映射固定A时H(C|A)=0，改定义局部噪声proxy；§4将该proxy放熵分解不当严格统一随机变量定理，OR也不是测得真实条件熵。

验证SmolVLM2-256M/Goal、8RTX3090/B128/30k与comparison2.2B/4A10080/B128/30k分开；tokenizer100k/B8192预训练LIBERO+Bridge+DROID不是免费、VQbaseline各官方checkpoint/统计对齐非完全同上游预算。comparison每task50trials，FAST padding/truncation特别适配、bin/string horizon8 vsAction20，Table3的0.9s/22action/s不是相同horizon统一延迟，更非control deadline安全。独立token95.5 vsKI94.3反侧，RVQ移除95.2仅−.3pp；SO100 co-training还增加22.9Kcommunity数据，recoveries非只有codec因果。xArm82.5 vs74.1局部；多seed/CI、precision和Table3硬件完整cost未披露。只采重构与下游可学习性/扰动传播分账，非全embodiment/平台无关或“零degradation”保证。

## 2602.15449v1 TAROT — 2+1+2=5，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15449v1) §3–4/Table1–4/Limitations、AppendixB/C实际读。同problem/reference生成四testtier并用reference验证；分配alpha与reward权w分账，训练前按baseline能力从固定portfolio选schedule，实际非连续在线adaptive。tiers结构长度/token diversity/character transitions及GPT4o标签代理不是真实困难总序。Table1 epoch.2/.4/.6 staged，不同weight/order分支不是同一个“一律easy→hard”。

约15kPython、o3/o4最高reasoning effort生四tier（作者o4表述不补造具体模型），任一tier不通过reference就剔除，reference本身/生成器bias与coverage未除。GRPO单epoch/G8/LR1e−6/B8或大模型B4/input1024/output4096/8A10080 CUDA12.4/PT2.6，eval4A10080/B64/Python3.11/每test10s timeout；precision/seed/CI及teacher生成cost未给。Table3相同test suite avg-reward/Pass@All对照支持局部，但TAROT(Best)跨策略选最优与base提升不全等单因素；1.5BHumanEval+55.49低Pass@All56.10，Gemma9BMBPP59.2低base59.6，7B LCB BasicOnly反优，不授能力越高普遍hard-first。仅Python/静态capability规则，执行费用与curriculum选择费用另算。

## 2602.15456v1 LatentSourcePreferences — 2+1+2=5，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15456v1) §2–4/Fig1–7、AppendixA/C实际读。语义相同内容仅source身份/credentials变且pair顺序控制，direct问偏好与indirect任务选项排名分开；political20/world60/research50/ecomm70 source、12模型，preferences随context/身份表示变，不凭cooccurrence解释因果起源。topic NEJM96%vsCV19%等说明有合理context条件，不把所有来源依赖叫错误/伦理缺陷。

AllSides3855event每3篇非内容相同现实子实验，shown/hidden/swapped/DoNotBeBiased与全部order平衡：swap会改choices、提示避免偏差未稳定修复，只此人口。seller反侧：costprompt最低价48.4→70%、speed53.9→69.3%，不能由news失败说prompt一律无效或BuyBox一致即真值。temperature0/SGLang/XGrammar结构输出（含PR修改）、Qwen tooltoken bias−100、L40/A40/A100/H100/H200不同GPU、precision/batch/完整费用未披露，语义合成数据与现实内容差异分账。未识别pretrain/posttrain因果，未验证人类合意偏好或真实购买损益；排名相关/统计显著≠规范正确。Books需actualowner，不因成熟source-bias主题自动新增。

## 2602.15332v1 DRTC — 2+1+2=5，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15332v1) §3–5实际读。单次on-policy greedy已实现trace每16token候选、K8 entropy/margin/JS启发式pivot，非训练得到的选择器；attention mask只在receiver预测位置屏蔽早先chunk，同时固定已实现prefix，不重采continuation。筛过baseline top-token logit、以局部分布差/端点logprob方向作relevance/gate，再MAD尺度与clipping加权；raw-logit curvature/turn-angle只是诊断，不是直接score或新优化器。

四小reasoning models、24slice相同greedy，C0vsC8相关1是构造校验而非因果证明。learned-vs-random chunk/pivot局部magnitude +.039–.178但proximity2–3倍，distant/shuffle控制不等outcome groundtruth。MATH500/R1Qwen1.5固定K8，median trace2694/IQR2131–3068，gap.409/95%CI.354–.453，355/500positive；pivot按分布变化选择与同类metric评价可能贡献选择效应。Gini/top5质量集中不证明其余token无信息；gate敏感性rho.97–.99不能证最优。§5明确不是correctness级因果、circuit identification或跨domain通用归因。chunk granularity/固定continuation只局部信息流，多chunk×pivot forward成本另算，硬件/precision/完整成本Not Disclosed。Books owner比较/独立源尚待。

## 2602.15356v1 CPUFreeMPI — 2+2+2=6，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15356v1) §3/5/6实际读。persistent setup与fastpath分离；MPI_Match permanent pair仅双方persistent，不接管所有非阻塞/generalized requests。MPI_Queue按GPU stream排start/wait，每start有匹配wait，同queue、host不能再Wait/Cancel、enqueue错误all-or-none；标准MPI路径共存。Slingshot11/libfabric DWQ triggered counters由GPU increment触发fi_write，completion counters经fi_atomic回localbuffer，再GPU polling；CPU仍做setup。普通send还需receiver-ready CTS+localstart，ready-send只能在应用已保证ready时省去。

约500 DWQ entries、每operation至多2个，耗尽时CPUenqueue可能block/deadlock，CPUprogress fallback失去CPU-free；stream wait/priority调度责任仍属应用，不授无CPU万能保证。Frontier MI250X4/node8GCD64GB/Slingshot11 200Gb4NIC；Tuolumne4MI300A128GB共享/node，ROCm6.2.4/6.4、CrayMPICH8.1.31/9.0.1、libfabric1.22/1.15.2。pingpong1B–1GB、5trials95CI，baseline每send两kernel+sync vs全部预enqueue最佳情形；medium latency减少12–49%/14–59%，大包Frontier8MB+反增2.7–4.9%、Tuolumne16MB+反增8.6–18%。

GameOfLife halo8point、5×1000iteration、Frontier2/30GB/Tuolumne2/62GB、1–1024nodes不同GPU/node；30GB最大mean485.4 Cray4096rank vs622.2 ready8192rank的28%不是同GPU资源配对加速。2GB regular≥512ranks反慢；Tuolumne最大scale1/2GPU-node Cray更好，4GPU-node相反；<8KB regular多CTS较Cray unexpectedhardware差，bounce优化未实现。只该网络/halo协议，不泛化LLM collective/端到端训练或8192GPU普遍性能。软件公开声称不等实现核验，通信precision/模型质量不适用。Books owner比较/独立源尚待。
