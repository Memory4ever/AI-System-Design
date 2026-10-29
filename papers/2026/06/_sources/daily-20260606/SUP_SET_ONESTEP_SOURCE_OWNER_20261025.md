# SET / One-Step Action：首次必要、具体owner与采用提案

作者`supp_jun06_close`，2026-10-25，仅Daily2026-06-06补Jun05。完整AB/notice/Jun05联合资格复用R29，不第三日期；本包不自签独核或新I。实际读取精确v1必要机制、主评价与直接反侧，未核代码、图像素、真实设备或复现。

## SET 2606.05495v1

[原件](https://arxiv.org/html/2606.05495v1) §3–5、Alg1–3对应正文、T1–2/caption。拟2+1+2=5：job graph的worker-local资源绑定与steal后retarget是具体设计差额，reach1只GPU runtime，durability2为capture/replay与buffer寿命分工；不把通用event或安全原则重复计分。标准审阅已经读足，因可能实际小gap加深至buffer/dispatch反侧。

旧batch末同步确保资源复用合理，却让先结束stream等最慢batch。SET每worker持stream、graph executable与device buffers；host submitter预先更新参数、装入per-worker ready queue，dispatcher取free worker，本地无job才steal。被steal的graph原来绑定victim memory，launch前必须重绑到执行worker的input/buffers/output；stream末callback才把worker归还free pool。准备好的job、可用worker、活跃buffer是不同状态，减少host polling不取消两host threads、队列锁/搜寻或retarget费用。

必要边界：§4称每worker唯一executable，同时per-worker queue保存fully prepared executables；Alg/正文未完整说明多个queued jobs是否独立exec、参数update与in-flight replay隔离，不能从概念描述签发全部并发无race。work-stealing遍历peer queues，不把O(1)共享同步宣传等同所有调度最坏O(1)，也不宣device-resident或CPU-free。只采用资源绑定与完成后回收这一可解释接口，不补其未证实现。

§5仅RTX3090/Xeon6330/192GB及RTX5090/i7-11700/128GB、Ubuntu22.04/CUDA12.8/C++20/O2；六workloads含BP单层训练、GEMM/KNN，非完整LLM服务。同步/graph基线单stream，batch/queue才有多worker；queue wrapper也被改为CUDA Graph，不是原系统原封重跑。T1对queue在BP/GEMM仅1.01附近、部分小batch近同；KNN共享锁与Hotspot带宽压力是不同瓶颈。T2平均overhead ratios不等文中54.64%/18.62%聚合口径，未披露全repeat/CI、各shape/precision/完整请求人口及p99/SLO，不采统一普胜或端到端LLM净加速。全部graph准备/驻留副本、host threads/锁、steal更新、callback与传输都计费。

actual `INFER-TENSORRT-LLM` Ch49“从逐Kernel Launch到Persistent Executor”完整graph段组已读：现有rolling cache只拥有capture完成后replay；FlashInfer段拥有prepared descriptor/query-length寿命；FlashRT段拥有static/swap/mutable状态及固定地址。这三组没有承载跨worker窃取已绑定graph时的buffer重绑定和stream末归还机制；Ch56 FlowPrefill的operator-safe preemption亦不是这个job调度接口。不是再补一条“metadata应有效”的泛化限定。拟单段插入Ch49 FlashRT-PAI独立marker后、Moira首段前，仅该小gap；须root确认协调，当前未写Books。

拟正文：

> 重放的资源绑定还可以随执行worker变化，而不是一份准备好的graph可直接交给任意空闲stream。一个任务并行分支让各worker持有自己的stream与buffer，host预备job后优先取本地队列，空队列才窃取其他worker的工作；被窃取graph原来绑定的input、中间buffer和output须先重定向到实际执行worker，stream末完成callback才归还该worker供后续复用。[SET的受限runtime对照](https://arxiv.org/html/2606.05495v1)支持这种准备、绑定、执行与回收分工，不证明所有queued graph的参数更新已与in-flight replay正确隔离；遍历peer queue也不因共享同步较少就成为全调度常数复杂度。两host线程、队列锁、graph准备与副本、重绑定、callback和搬运都付费，六个局部workload的吞吐不能替完整LLM尾SLO。绑定或寿命无法证明、并发不抵调度开销时，保独占buffer的静态graph、原batch同步或已验runtime，不由可launch批准并发安全。

## One-Step Action 2606.05737v1

[原件](https://arxiv.org/html/2606.05737v1) §3–5、T1–6、A/B/D/E/F直接控制与caption。拟2+1+2=5：仍用标准velocity/CFM，只改训练time抽样使noise endpoint得到支持，是不同于teacher蒸馏/初始化/endpoint corrector的具体替代；reach1动作生成组件，durability2为condition-target与solver支持边界。为Book小gap读足horizon/condition/replanning与配置反侧，不把低维本身当单步充分条件。

主文x_t=t*x1+(1-t)*x0，t=0 noise、t=1 data；noise-shift t=u/[1+(alpha-1)(1-u)]，alpha>1偏向noise。A的OpenPI坐标相反；不能混用两端或把alpha越大越好。平方velocity目标人口最优是conditional mean，若条件仍留不兼容动作模式，一步可平均掉模式；“观察丰富/动作紧凑”是解释与诊断，不是已证明方差定理。Pure-noise改独立noise输入，是不同stress-test，无普通多步插值轨迹；toy另外有CE，不说全论文所有实验无auxiliary objective。

标准LIBERO四suite各10task×50episodes；tiny B64/50k、full B256/150k，SigLIP/PaliGemma slices、4-layer action head与32-interface仅7physical维loss；T4 full32某些full-encoder反更好，mask7不是必要recipe。T1高noise可令单步改善却让10步崩落，过强shift也伤单步；T2 H40单步仍落后uniform10，T3去state几乎归零；这些控制支持训练/条件/目标复杂度共同决定，不证明单一因果定律。F的LIBERO-Plus全18配对单步不弱，但部分horizon shift反退，不能挪作跨所有任务普胜。LIBERO-Pro mean44.2vs43.5，swap均2.6，局部鲁棒性很弱。真机YAM三task单步各5trial、10步取official同checkpoint baseline rate而非本轮paired重跑；不授精确显著性或general safety。

E清楚区分flow_steps、action_horizon与replan_steps；H10 r1会从约85降到33，而长horizon旧full-action-loss的人口未按mask7重训，不把全部表拼成同一checkpoint控制。较低noise-endpoint MSE/cosine是有限256sample诊断，不认证ODE全轨迹或控制成功；未统一披露全部training seed/CI、硬件/精度/完整wallclock，不把一次head forward当sensor-to-actuator deadline。训练schedule/condition编码、全部policy与重规划、真实闭环回归均计费。

actual唯一 `MULTIMODAL-EMBODIED-VLA` Ch26 L430–480完整段组已读：已有fixed-point/LoopVLA/GeCO是迭代field与停止，two-point probe是已有expert的测试时budget，MM-ABC改endpoint参数化，learned near-action start与corrector另改模块/目标，均未有“保持velocity/目标而偏训练time到推理起点”的替代。拟在MM-ABC独立marker之后、learned endpoint初始化首段之前单段；不是把现有安全/费用通用句再写一次，须root确认协调，未写Books。

拟正文：

> 一步动作生成也可以先改变原训练目标在哪里获得样本，而不更换velocity head、增加teacher或学习初始化：在标准条件flow matching中，将训练time向噪声端偏移，使推理第一步读取的位置得到更多监督。[受限One-Step Action控制](https://arxiv.org/html/2606.05737v1)中，丰富观察、语言与state条件下的紧凑action chunk支持这一轻量替代，但条件平方目标仍可能平均不兼容动作，多模态性不能仅凭动作维度排除。高噪偏置可改善单步却伤多步，过强偏置、变长horizon或移除state也会退步，因此须把训练schedule、condition、action horizon、flow steps与实际replanning interval一起对照；求解一步不等真实环境只执行一步。训练与encoder、全部重规划和闭环回归继续付费，有限模拟与每task五次真机试验不认证普遍条件集中、最优shift或物理deadline。条件或质量失配时，保原time分布、多步Flow、较短chunk和独立controller，不由head少forward自授执行安全。

## R33采用与两项实际保存（2026-10-25）

root R33首次必要/正式各5/实际owner与原两单段通过，并精确授权。SET最终位置修正为完整rolling费用段“这把重复shape…”结束后、Moira首段前，不沿上文旧拟位在FlashRT marker后拆组；当前Ch49正文L253/独立marker254，trueH2 Review notes L2722/本人完整来源注2724。OneStep保持MM-ABC完整组及独立marker后/learned near-action完整首段前，当前Ch26正文467/marker468，trueH2 2277/本人来源注2279。行号可能随并发平移，采用完整内容锚。

作者`supp_jun06_close`已按两原单段逐字真实保存，各只一独立marker/trueH2下本人一注；随后实际完整自读新增、直接上/下整段与本人整注。SET上rolling成本/反侧完整且下Moira完整；OneStep上MM-ABC两段及marker、下learned初始化首段完整。程序逐字比较两原稿、唯一正文marker/trueH2和限定diffcheck通过，未改旧组/他人注或并发修改。已立即报root精确位置供唯一非writer POST；此处未预记I或DAY，不重复独立行政验收。

R34唯一nonwriter actualPOST已通过，两指定窄位整合生效，SET I13/OneStep I14；只同步既成，不第三原证/owner/正文，不授整日DAY。
