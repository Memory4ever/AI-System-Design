# Deopt-Reopt 06063：首次必要／拟5／actual Ch49小gap

作者`supp_jun06_close`，2026-10-25，仅Daily2026-06-06补Jun05。R31完整AB/notice/Jun05联合资格与准入有效复用；未核图像素、代码、实机或复现，不第三日期。本提案不预I或独核通过。

## 必要机制与反侧

实际读[exact-v1](https://arxiv.org/html/2606.06063v1) III–VI/TI–II及workflow/caption。拟2+1+2=5：在LLM输入端先去除CPU-specific展开/布局再翻CUDA，是source representation的具体选择与负面控制，reach1局部codegen pipeline，durability2为输入结构/预算/成功条件分离；不把“等预算/正确性重要”等成熟原则计新机制。

输入为aarch64/NeoverseV2已优化C++，含NEON intrinsics/tiling/prepacking；三阶段D+R依次deopt、translate、reopt，每段维持接口/目标shape/数值tolerance，deopt不看target hardware；Direct省deopt。Single-shot分别3对2LLMcalls；Direct-3再给一轮reopt作3call控制，失败translation就停、不用于追加translation/retry，因此是successful-trial performance控制而不是equal-budget feasibility控制。任何later reopt失败保last passing code，阶段无passing则失败。

Iterative每phase至多3generation，每轮共享1PM提出策略、3PG候选、每候选最多1repair，选择correct最短LOC作为deopt、correct最快runtime作为reopt。PG共享PM不算独立样本，统计按50trial末值；deopt没有更短正确candidate时carry原input（11/1110成功trial），LOC只是simplification proxy，不等结构可移植性。Direct与D+R各phase都有相同搜索机会，但D+R多一个phase，不能称总调用预算匹配。

硬件GH200/72coreNeoverseV2/H100，NVHPC25.9/CUDA12.6/cuDNN9.5.1/NVPL25.9/ArmPL25.07.1；O120/Q235 via Cerebras T.5/max16384、O120 medium、无固定seed/provider precision未记录。每kernel实际shape与数值验收见TI，主要FP64而Conv2D FP32、DD/DF双word特别精度；reference是正确性oracle/粗性能landmark，部分不同精度/未优化，不能授vendor库性能胜出。onewarmup/five runs取minimum，CUDA events在data placement后，排H2D/D2H与validation；不采完整application净加速。

50trial/arm：single 24cases中18可检，MannWhitney+BH-FDR后5favorDR/3favorD，conv2d两model较清楚，但DDGEMM方向随model翻转；Direct-3仅unadjusted exploratory，19可检4/4相平，不把三call后仍显著个案当全部因果。Iterative23可检5DR/2D，O120差距多被搜索缩小，Q235的conv2d/ddgemm/bgemm仍大；Q235fft都约1GFLOP远低reference，passing不等高性能。D+R对feasibility可增可减，Q235spmm/gemm single皆0；conditional median是成功子人口，不能乘成功率当期望值或删失败宣全费收益。未来shape/layout/sparsity/boundary未验，fixed-call best-of-N/failure-inclusive分析未做。模型调用、PM/PG/repair、全部compile/失败/校验/数据传输与最终真实应用都计费。

## actual唯一owner及有限差额

唯一`INFER-TENSORRT-LLM` Ch49实际读章开头与Ch48/50交接、GeneratedKernel typed-schedule IR完整段、CuIR lift-transfer-lower完整两段/2605.05023 start/end及下面MoE开头；并对读前部恢复高层IR/源kernel重用段。现有CuIR强调“已有可信GPU expert kernel可保留目标结构，只迁semantic delta”，缺“只有已CPU优化source时，先去掉源硬件结构可能释放目标GPU映射、也可能毁掉有用结构”的替代分支。该差额是输入变换本身，不是单加更严格benchmark警句；不接管通用Agent规划或Ch66评测owner。

拟插Ch49 CuIR完整组end marker后、下一H3 MoE量化标题前单段。当前未写Books，待root确认具体gap/精确位并协调。

拟正文：

> 可复用的source若来自另一种硬件，保留全部优化结构也未必最有利。对已经CPU向量化、展开或预打包的C++，一条LLM移植分支先在原接口和数值验收下简化源代码，再翻译并为GPU重优化；它试图恢复算法结构，不是让模型任意改语义，也不同于上段保留高质量GPU kernel的IR迁移。[Deopt-Reopt的受限十二kernel对照](https://arxiv.org/html/2606.06063v1)有卷积获益，也有丢掉源结构后退步，更多Direct搜索还会缩小差距，因此源简化是可选候选而非跨硬件必经步骤。额外reoptimization的三call控制没有匹配translation失败重试预算，成功trial的runtime中位数也不代表包含失败和搜索的端到端收益；原shape上的数值通过不保证未见layout或边界。全部模型调用、候选编译/repair、失败校验和最终搬运执行均付费，结构、数值或净预算不支持时，保直接移植、原专家kernel/库与可信编译器，不由更少LOC或局部快例批准部署。

## R35采用与真实SAVE（2026-10-25）

root R35首次必要/正式5/actual Ch49小gap及原一段通过，仅授CuIR完整end marker后/MoE H3前与trueH2本人一注。作者`supp_jun06_close`已逐字真实保存，当前正文2697/独立marker2698、trueH2 Review notes2725/本人注2727；完整自读新增、直接上CuIR两段与end、下MoE H3及首段和本人整注。原稿逐字/正文marker唯一及限定diffcheck通过，已立即交root唯一非writer actualPOST；未预I15/DAY，不另增行政核查轮。以完整内容锚为准，行号可随并发平移。

root R36唯一非writer实际POST已通过，I15生效/指定窄位释放；Report及作者A40已同步既成，不重核source/owner或增行政审查，不授整日DAY。
