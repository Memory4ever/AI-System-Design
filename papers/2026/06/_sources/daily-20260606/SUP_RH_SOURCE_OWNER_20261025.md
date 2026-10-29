# RH+ 2606.05511v1 首必要/actual owner/逐字PRE

作者supp_20260606_author，2026-10-25；[exact-v1](https://arxiv.org/html/2606.05511v1)、[本地原HTML转文字](SUP_RH_HTML_20261025.md)。A6/R4完整题摘/身份/Jun05联合日证有效复用，不重新抓日期。R4准入不等本次必要/评分/owner通过。

## 必要机制与反侧（首次待独核）

实际读完整必要§II–VI，非仅摘要。原host-centric interleave为主机并行访问合理，但在本文all-bank MAC_AB GEMV里，per-bank stride64跨过32column row，使每次MAC重付ACT/PRE。§II–III的nRC是同行ACT间隔，nCCDAB是MAC功率间隔，二者不是同一瓶颈。原模拟row-miss路径中channel轮换已使MAC间隔超过power间隔，因此仅松PC→NPC无收益；换布局/stride使同行多MAC后，row费用摊薄，power间隔才重新显露。

采用“先查实际地址/行命中，再调power约束”的局部设计纠正，不采paper对所有GEMV都nCCDAB irrelevant的泛化。§III给定5.2Gbps局部32MAC示例可复算2016→249/185tCK，但不照录完整执行recipe：其多channel发命令时序与聚合公式未在本次充分核成可实现调度。§VI离线K重排是新增artifact约束；真实浮点累加非一般结合/交换等价，故拒采用“commutative所以GEMV数值不变”的声明，须独立质量与kernel验收。HBM3-PIM是作者条件架构，不声明commodityGPU支持，未把引用JEDEC当已核PIM命令标准。

§IV AttAcc+Ramulator2.0周期模拟，IDD/DRAMPower式分项能耗；四个指定模型GPT175B/LLaMA65B/MT530B/OPT66B、TP8、5.2Gbps、batch1/4、输入输出128/2048、2048/128、2048/2048共24配置。模型/DRAM拓扑按原文，未重建其“five stacks”与TP8完整映射；precision、真实device、并发到达、尾延迟/SLO、端到端数值质量及重复统计未充分披露，不补。§V吞吐/energy/EDP是同模拟基线，不是制造芯片/生产GPU结果；attention不受MACstride优化、长输出其占比升高限制收益。能耗含background duration，EDP复合不能当第二份独立收益。精确曲线/硬件运行/实现复现未做，不采用全文数字为保证。

拟正式 `2+1+2=5`：D2为行局部性使power优化归因失效及布局替代；Reach1限PIMmemory/command组件，不给TP/多模型机械加分；Durability2为可复用局部性—可见瓶颈转换。虽5分，因具体修正PIM瓶颈解释/拟Bookgap，已深入受影响必要和反侧，不为降工作量改分。

## actual owner与直接邻接（首次待独核）

已按ROADMAP实际读Ch54开篇hierarchy/counter、容量与现有定制HBM硬件分支完整两段、固定动态占用下接；Ch44低batchweight读取段及Ch53/55开篇作交接。唯一owner `INFER-GPU-MEMORY` Ch54，不另建PIM章节、不在decode重复硬件机制。

现有Ch54具体承载①peak-BW下界不是实测瓶颈；②容量配置换BW/Cap和定制memory代价。但未解释bank-local compute可仍因row-address mapping反复ACT/PRE，以及松power间隔何时先无效后有效。拟插在现定制HBM第二完整段（末“而不是靠带宽承诺放行超容量请求。”）之后、H2“固定、动态与瞬时占用”之前，承接硬件替代分支后回容量占用；只原两段与独立marker/本人注，待rootfresh窄授。

## 逐字PRE（尚未批准/未保存Books）

把乘加移进DRAM bank，也不等于消除了memory-side等待。面向主机并行访问的地址交错可能让连续all-bank乘加反复跨row，每次重新支付activate/precharge；这时先放宽乘加的功率间隔，未必改善被row周期遮蔽的瓶颈。一条[受限PIM模拟分支](https://arxiv.org/html/2606.05511v1#S3)通过离线权重重排与同行连续访问摊薄row费用，之后功率间隔才重新成为可见限制。因而应先绑定物理映射、命令作用域、row命中与真实执行时序，再判断哪条memory约束值得优化，不能只比较标称带宽或单个timing参数。

这条分支增加权重布局产物、模拟校准与命令调度的验收成本，不自动适用于普通GPU或所有batch；attention与长输出的KV成本也不会随bank内乘加一起消失。周期/能耗模拟不证明制造芯片、数值质量或服务SLO，重排改变累加次序亦不能由代数交换性批准逐bit等价。映射、算术或完整费用不合时，保留原权重布局、已验证GPU/普通HBM路径与独立容量和质量检查，不用局部row-hit倍率放行生产请求。<!-- source-family:SF-2026-ARXIV-2606-05511 -->

本人注拟：`SF-2026-ARXIV-2606-05511` — supp_20260606_author，Daily2026-06-06补Jun05；exact-v1 §II–VI必要，拟2+1+2=5/唯一Ch54。仅PIM row映射遮蔽power间隔与布局/命令验收；保模拟/attention反侧、累加非逐bit等价与完整费用，不采执行recipe、芯片性能或服务SLO。未核图像素/代码/硬件或复现；首次必要/PRE、root新窄授、实际SAVE与唯一POST按后到事实记，不预I/DAY。
