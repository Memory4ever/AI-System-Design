# MFS2603.17456v1：必要Source与唯一owner差额/PRE

03-20仅补03-19自然日，resume_mar17准备；未写Books，未授Source/PRE独立通过或安全完成。原2+2+2=6拟评分不改。官方exact-v1完整题摘已与root准入校准有效复用；current v2 Sep19改名Nuska只作当前修订说明，不混用v2摘要、不开版本diff。日期夹证原值见SUP_FIRST_DATE_FIELDS：官方ID不预发及公告规则与registered03/19T02:32:42Z上下界均为03/19BJT，属于日级推断，不补确切公开时刻；交root独核。

## 必要原证与停止范围

[exact-v1 HTML](https://arxiv.org/html/2603.17456v1)，实际§2–7、A.1假设、B/Alg1及soft-enforcement。web原定位§3–4 L130–295；§5–6 L295–371；§7 L373–393；A.1 L507–518；B L544–607。支持/反侧够，停止，不读全部证明、图像拟合、代码或旧修订。

普通stage-agnostic流策略不区分远端prefix恢复、层内collective与P→D transfer的消费时刻。论文将一次Prefill的依赖层/剩余laxity带到网络：remote KV先具备目标层消费依赖；collective在当前层阻塞compute；P2D并非阻塞Prefill compute，却仍须赶在请求TTFT剩余预算内。RMLQ从低优先级开始，只有随着剩余时间/层推进使MLU阈值或消费依赖接近才Promote；没有双向反复降优先级，完成/层事件更新以减少连续LLF排序。MLU=剩余bytes/(剩余time×可用带宽折减)，是估算，不是已兑现服务；大于1已不可行，几何阈值经验参数，不采普遍最优recipe。RLI=目标层−当前层；最小RLI优先的Theorem1只在理想计算、无限可分无成本抢占、单瓶颈专用带宽的Prefill makespan模型内，不能授真实共享fabric下全请求TTFT最优。

跨batch RED用deadline最大gap划tight/loose并折合有效deadline，目的是减轻极少urgent请求让整batch搭便车；也会削弱该个体的urgent优先权，非全人口公平保证。延迟估计用离线compute profile/traffic矩阵与瓶颈port负载，不把估算可行性当硬SLO。Alg1的drop集合H有全局budget，候选池包括前面batch，可能移除当前或较高优先batch的最大瓶颈负载请求；B正文明确实际为soft Scavenger class，在网络空闲或实际延迟低于保守估计时机会服务，而非一律丢弃完成请求。主队列attainment改善必须同时记延后人口、原总人口分母、最终完成和已耗compute/transfer，不能以mainqueue的局部TTFT批准全体端到端goodput（分账要求是本书工程推断）。daemon/coordinator收流arrival/completion和batch矩阵，NCCL/Mooncake适配，submit/permit/completion与RDMA/DSCP strictpriority把网络决策执行出来；有限硬件classes/capping、hostpolling及状态陈旧仍有代价。

§6真实集群8servers×4RTX3090＝32GPU，2CX5 100Gbps/server、PCIe3，Ubuntu22.04/CUDA12.8/PyTorch2.8/NCCL2.28，P/D各16GPU；Mixtral8x7B FP16/topk2/TP1/EP8，QwenConv均2k/50%reuse，Agent1k/65%，Poisson，512warmup后1024eval，batch8192tokens与指定rate。关键限制：输出固定1token，只测TTFT，不能授TPOT/正常长Decode收益。SLO=3×低负载TTFT，CCT/earliness/attainment不是统一生产SLO。256server scale项是Vidur＋flow模拟，A100 profile/NVSwitch900GBps/NIC200Gbps，MoE与Dense并行/trace形状不同，不作真实256集群或统一baseline无混杂。FS/SJF/EDF（implicit流缺deadline回FS）/Karuna是作者指定比较，不等所有现代联合scheduler。正文local数值只作为其条件内作者报告，不采用headline倍率。§7未评TP/PP、多模型未评；GPUinitiated需要CPU辅助的开销仅定性讨论。独立重复次数/置信区间、controller/协调/Scavenger最终完成与全费用分账未充分披露；不采性能/硬SLO/公平性通用结论。

## actualowner与相邻交接

ROADMAP明确INFER-SCHEDULING/Ch56 `books/part-05-inference-system/56-inference-scheduling.md`。实际完整L17–73 runtime四层/admission，L373–435 iteration/抢占与executor权责、L1513–1543 estimator/网络costoracle交接均相关对读；没有relative-layer消费时刻驱动同fabric Defer/Promote或soft-prune class解释，非主题NC。Ch55 L136–157已有共享KV/collective争用和硬件物理路径隔离，但不拥有请求/层剩余预算决定网络流优先级；其handoff正确性及状态ownership保留。Ch57 L1–65只拥有平台control/data/evidence plane，不接管flow urgency。新差额是消费阶段不同、网络优先级可延期/提升与被软延后人口的分账；不重复物理隔离、SLO预算或通用优先级已有结论。

## 拟逐字PRE（root独核前未授写）

拟Ch56原SLO-aware Admission保守margin段后（当前L73）、P/D两池容量段标题前，新增以下小节与两段。后续实际定位须顺读确认，未ownBooks。

### 同一 Fabric 的流优先级应跟随数据消费阶段

请求的剩余 SLO 预算还会经过网络。共享 fabric 上统一 FIFO、按 bytes 排序或固定流类别，在低争用、消费时刻接近时简单可控；远端 prefix 恢复、当前层 collective 与 P→D KV handoff 同时出现后，流大小相同却不代表阻塞同一段计算。一个 stage-aware 分支将目标消费层、当前执行层、剩余 bytes 与剩余时间交给网络调度：暂时不阻塞计算的流先延后，随依赖层推进或预算收紧再提升优先级，避免把未来可重叠的传输持续压在当前 collective 前面。请求调度器提供 deadline 与 batch 身份，executor 提供实际层进度，网络控制面通过 permit、completion 和有限优先级 classes 执行；优先级不能代替第55章的 KV 有效性与 handoff 提交。<!-- source-family:SF-2026-ARXIV-2603-17456 -->

延后/提升用离散阈值减少连续重排，却新增 profile、traffic matrix、host 协调与陈旧状态风险。过载时按瓶颈负载把部分请求转入在网络空闲或实际延迟低于保守估计时机会服务的低优先级队列，可以保护主队列，却必须连同这些延后请求、已耗计算/传输和最终完成共同计费，不能把主队列的 TTFT 达标率当全人口 goodput。[MFS exact-v1 §3–7/B](https://arxiv.org/html/2603.17456v1)支持这个网络阶段接口；作者真实 RTX3090 集群将输出限制为1个 token，较大规模为模拟，不能据此保证正常 Decode 的 TPOT、多模型公平性或生产 SLO。理想单链路、无成本抢占模型中的最小相对层序结果，也不是共享网络的普遍最优证明。网络优先级不可用、预测漂移、争用很弱或隔离要求更强时，固定队列、保守 admission、rate limit 或第55章的物理隔离仍是合理分支。<!-- source-family:SF-2026-ARXIV-2603-17456 -->

静态本人源注拟：`SF-2026-ARXIV-2603-17456`，MFS exact-v1 §3–7/A.1/B，采用relative-layer/剩余预算→Defer/Promote网络接口与soft Scavenger人口分账；不采全局LLF最优、全人口硬SLO、正常Decode收益或headline倍率。RTX3090实测1token/TTFT与256server模拟分开；controller/预测/soft延后最终完成及全部费用边界保留。未核代码或复现实验。
