# A105 — FlexNPU04415首次必要 / 正式6分 / actual Ch55最小两段PRE

最新行政事实：reader R107–108唯一actualPOST已实际采用，整合生效/指定窄位释放，新增I22＋旧Kimi1合23，以下未POST为历史过程，不第三技术。

A107过程：reader R105–106首次必要/正式6分/actual Ch55小gap与原两段PRE逐字通过，无修句；root本轮fresh双锚新窄授后已逐字真实SAVE/完整自读＋本人true-H2单注，当前只待唯一非writer actualPOST，不预I23/DAY。下列未获授权/待PRE均为A105过程，不再当前待办，I22保持。

仅本日Jun04补窗；R89–91本项完整题摘/收窄准入/精确v1联合日证复用，不第三。CAS R103–104唯一actualPOST已实际采用，新增I21＋旧Kimi1合22；仅本人注/Source/Report行政同步、V3先通过，不第三技术。本项尚无Books新授权/SAVE/注/POST/I。

## 精确原件与实际读取

`2606.04415v1` *FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location*。原abs/notice/exact DOI见SUP_TITLE_STOP_BATCH4_20261025.md，Submitted-v1 `2026-06-03T03:49:34Z`，registered `2026-06-04T01:58:12.000Z`，findable/arxiv.content；最早Jun04 08:00BJT至最晚09:58:12BJT完整同日，R89–91通过。v2 Jun08不混入本v1；未见withdrawn/correction信号的既有notice有效复用。

官方HTML `https://arxiv.org/html/2606.04415v1`真实404，未当正文已读；官方PDF `https://arxiv.org/pdf/2606.04415v1` GET200/1009669bytes，SUP_2606.04415v1_20261025.pdf，SHA256 `44401566f0df70afe433925a6842eb6586fe6a0f1ece629c47667409fa39d460`。11页，实际读取正文p1–10/§1、§3.1–3.5、§4.1–4.4/T1–4及结论，related work只作原作者关系说明不代那些论文已核；不读无关refs/p11。p4–5与p9–10完整重取避免首次输出截断；p9完整像素实际看T3/T4与相邻§4.4（渲染/private/tmp/flexnpu-0605-p9.png），图2–6只读说明而未核全部曲线像素，不采用其精确曲线值。未核代码/性能复现/真实服务。

## 必要机制与直接反侧

§3.1–3.2：LD_PRELOAD client截获AscendCL内存、stream/event、同步、model/operator launch等selected APIs，将op/virtual handles/metadata/args描述符经shared-memory发给per-device userspace daemon；daemon做virtual→physical对象映射并入队。大tensor不经控制path复制，仍在framework host/device memory；这不是无内存搬动或一般零拷贝证明，也未完整列出所有API/并发/error-path语义测试。验证请求是作者描述，不代多租户安全证明。控制/数据快路径与policy profiling分离，缓存映射/批量bookkeeping减查找，不保证所有API/应用透明。

§3.3–3.4：Prefill/Decode逻辑实例分开，daemon独立phase queues，用pending ops、recent time、bandwidth pressure、decode progress/active sequence、queue occupancy/device utilization调整dispatch ratio；bandwidth饱和后可给Prefill算力机会，decode backlog又提高Decode份额。是时分派发/stream调度，不依赖hardware spatial partition；stream priority/resource group为可选enforcement。论文未披露完整phase识别协议、阈值/反馈周期/控制方程、具体映射切换/stream-event同步验证或内存隔离，不能补造可执行recipe、强抢占或保证不干扰。KV locality只定性减少不必要搬动，未闭无搬运/ownership-handoff实现，不借virtual handle代KV兼容。

§3.5明确full SLO autoscale、transparent live migration、failure recovery在范围外；不将“substrate enables”当这些能力已实现。虚拟对象并不自动成为租户隔离/故障完成/可迁移状态。全部proxy、IPC、排队、profile、映射与切换仍费。

§4.1–4.2/T1：910C、CANN标准栈但driver/CANN/vLLM具体版本未披露；Distill-Llama-8B/vLLM TP1/maxseq512/maxlen2048/maxbatchtokens10240/mem.9，AISBench gsm8k、rate10/batch384/maxout1024，temp.5/topk10/topp.95/seed1214/repetition1.03，五次均值total token throughput977.6928→988.2675（+1.08%）。无variance/CI/质量一致性和per-call latency，不能以小差额签统计零overhead/唯一异步overlap因果；生成参数不证明生成token与正确率相同。

§4.3/T2–3：DeepSeek-R1 W8A8 CloudMatrix384/384×910C；static6P2D中6×16 P＋2×144 D，对照动态3×128，allocation/并行布局一起改变，非仅dispatch ratio单因素。文字P DP32-EP32/D DP288-EP288并未完整交代logical/physical映射，不替作者修其拓扑。给定TTFT≤1s/TPOT≤50ms部署目标下，T3总throughput单位RPS：1024/1024为489.84→618.18（26.33%），1024/4096为146.63→154.18（5.15%）；T2另一瓶颈表1K/4K总53与T3 146.63不是可默认为同一条件，完整差异未解释。无逐请求tail/目标通过比例、到达率/负载搜索、质量和run CI，不外推生产goodput或所有流量同收益。

§4.4/T4：Qwen2.5-7B对静态同置，不是上项静态分池；200req、rate4/maxseq4、四长度、两次均值，设备数量/TP/精度等未充分给出，arrival rate等maxseq并不量纲自证所有系统必过载。动态改为两进程并调度，分离/调度因素未独立消融。吞吐三项+3.57/+3.36/+.16%，256/1024为−.52%；只有两run无区间不能采“within noise”已证。TTFT109941.5/488099/118164.5/506536.5ms→331/331.5/8568.5/8311.5ms，像素核实后两为8秒以上，直接反驳正文“across all sub-second”；仍可支持该backlog配置大幅改善，不签全部1s门槛或请求尾部。TPOT约20–22ms/变化约±3%，未证输出质量/完整公平性；五次T1与两次T4不混人口。未扩大附件以追未采用的绝对SLO/零开销。

## 正式评分与actual owner

Design Delta2＋System Reach2＋Durability2＝6：只给selected-runtime API虚拟对象/控制快路径与phase temporal dispatch接口跨应用—设备控制边界这一分支，改变无空间分区时必须改框架或静态分池的选择；不按Ascend品牌、384卡、TTFT数字或成熟LD_PRELOAD/KL等原则加分。已确认长期小gap，深入受影响机制与直接反侧足即止。

唯一owner `INFER-PD-DISAGGREGATION` Ch55。实际读核心break-even/全费，EAServe SM mask＋Decode专池、Bullet独立queue/stream动态SM份额完整段及其marker，直接下共享DRAM/PNM硬件完整段；邻Ch54容量与Ch56多时域调度真实开篇。另定点读Ch63 Cross-API sharing完整两段：scheduler partition/runtime同步memory-safety分责与硬隔离回退已覆盖，不能因同“虚拟化”或新名造diff。现Ch55已经讲动态阶段份额/队列/SLO边界，**不重复这些成熟结论**；尚未具体承载不依赖空间分区、由runtime API virtual objects/daemon描述符分派落实phase temporal share的第三控制位置及其透明性证据限界。exact family/题名在Books无同事件必要链，不以缺marker认定gap。拟仅两段于现Bullet完整段及其独立marker后/PNM完整段前；不是Ch63再造整平台虚拟化章节。

### 完整直接上锚（保独立marker）

> 当主要压力是同一GPU内的阶段干扰，而不是跨池容量不足，还可把Prefill和Decode拆成独立队列与stream，在同一GPU内动态分配SM份额，而不要求两套完整设备池。[一种受限实现](https://arxiv.org/html/2507.06608v1#S4)以kernel饱和profile和KV流量代理估计阶段代价、调整SM份额，并以请求长度和年龄修正Prefill排序；这区别于让Decode继续专池的Encode–Prefill共驻，但SM划分仍不隔离共享显存带宽。模型估计与异步重配也不提供任意负载的硬SLO：单独把资源偏向Decode可推迟Prefill，短请求优先又可能伤长尾，两者须按同一请求人口共同验收。profile、layout准备、重配/调度、拆批重复权重读取与所有KV状态均付费，不能把不同GPU数量的基线或局部迭代延迟当同预算goodput。成本模型失配、重配不稳定、队列公平性或尾延迟不过关时，保留静态份额、chunked共批或独立PD池，并绑定实际producer/consumer及状态恢复边界，不由逻辑阶段分离宣称带宽、内存或输出正确性已隔离。
> <!-- source-family:SF-2025-ARXIV-2507-06608 -->

### 完整直接下锚

> SM 份额之所以不能代表带宽份额，还因为 Decode 为发出足量并行内存请求，可能需要占用不少 SM，即使算术本身很轻。[一种共享 DRAM 的硬件替代分支](https://arxiv.org/html/2610.26131v1#S4)把完整 Decode 计算放在 HBM logic-die 的 PNM，让 GPU 处理 Prefill；两路共享原 DRAM/TSV，由同一 memory controller 决定请求时序，payload 按已排定时序直接转发，不等于绕过仲裁或凭空增加带宽。共享只读参数也约束两阶段采用相同 TP/EP mapping，mutable KV 仍须按阶段单 owner，并在交接时保证 GPU 写入对 PNM 可见；少一次搬运不等于取消 handoff。Prefill 优先可缓解其饥饿，却会短暂阻塞 Decode，batch 失配与较长输出也会改变收益。证据来自 cycle 模拟、综合缩放和指定热模型，另加 PNM 计算、buffer/控制与功热成本，不是同总硅预算的实机胜负；无对应硬件、需要独立 mapping 或净质量/SLO 不合时，原 SM 份额、chunked 共驻和同构两池仍合理。<!-- source-family:SF-2026-ARXIV-2610-26131 -->

## 原两段最小PRE（R105逐字通过；A107已真实SAVE待唯一POST）

缺少可用空间分区时，阶段控制还可以下沉到应用与设备之间的runtime API，而不必先改模型或把每个worker永久绑定专池。可在API边界截获内存、stream/event和launch等操作，用虚拟handle表示应用所见对象，由每设备用户态daemon映射真实对象并接收轻量描述符；大tensor不穿过控制通道。Prefill/Decode保持逻辑分开，再按各队列积压、近期执行时间和带宽压力调整派发份额。[一项AscendCL分支](https://arxiv.org/pdf/2606.04415v1)采用这种时分/stream控制，不把“更多派发机会”等同硬件空间隔离；stream/event顺序、异步完成、对象寿命与错误回传仍须另验，虚拟handle也不自动证明KV迁移或故障恢复正确。

这条路径把侵入框架的代价换成API覆盖、映射、IPC、排队和profile成本，而不是获得零开销或通用SLO。其有限NPU对照同时改变PD实例布局或进程分离，不能把全部差额唯一归给动态ratio；小模型backlog表中长输入TTFT仍约8秒以上，与正文“全部亚秒”不同，均值吞吐也不证明尾延迟、质量和公平性。应绑定runtime/API版本、虚拟—物理对象、同步与phase识别协议及实际设备/并行布局，联合验完整请求质量和TTFT/TPOT；强隔离、live migration与故障恢复不能由透明代理代签。覆盖不足、映射或完成边界不明、控制振荡或净收益不合时，保直接runtime路径、固定共置/chunked执行或已验独立PD池，不让“无需改应用”免除状态与端到端验收。<!-- source-family:SF-2026-ARXIV-2606-04415 -->

## 精确停止

本单篇首次必要/正式6分/actual Ch55小gap/原两段PRE ready待唯一reader，不等余四Batch4与两cue。无新Books授权/SAVE/本人注/POST/I；当前I22保持。有限stop/最终六节/DAY仍ordinary，04032日期隔离/DistIL争议不冒普通0/外阻；State/index/他日未改，无stage/commit/push。

## A107 — root新窄授后真实SAVE与selfread，待唯一actualPOST

恢复重读AGENTS/当前合同/Prompt/来源Daily与arxiv恢复、ROADMAP/Books三公共上下文、本日路由与A105、实际完整读回R105–106，不第三原AB/date/必要/PRE。root本轮fresh双锚明确新窄授后，仅上述原两段逐字保存Ch55 Bullet完整段及独立2507-06608 marker后/PNM2610-26131完整段前，新增正文family marker1＋章末本人单注1，唯一true-H2 Review notes正确。全文新两段/完整直接上段及其marker/完整直接PNM下段/本人整注已实际selfread；虚拟对象/时分调度非空间隔离、同步完成寿命error另验、布局/进程混杂、长输入8秒反侧、全费及原方案退路均保留，没有扩大采用或修句。

写前快照 `/private/tmp/flexnpu-0605-save.vqPT3n/ch55-before.md`。before SHA256 `cc6a2e9699da11553e255c5f39e8fe9b860a888f2eeae1a54558e2265191410c`；after `a3d6dec3fa5931a2f12185a88c47728ccb55029dc7b6cd8460bdb57dd6c55aab`。限定检查：仅逆除本原两段及本人单注/新增分隔后整个Ch55字节等写前；原两侧/独立marker/他注及并发内容全部保护，不以hash或inverse代实际阅读。

Report本项/当前状态已同步R105–106有效和A107真实SAVE，仅待唯一非writer actualPOST；总I22不变，不预I23/DAY。V3普通Books枚举仍如实失败，不冒暂缓/改合同脚本。阶段仅本项窄写和POST交接，ready立即释放，不展开下一篇/保留跨阶段授权；State/index/他日未改，无stage/commit/push。
