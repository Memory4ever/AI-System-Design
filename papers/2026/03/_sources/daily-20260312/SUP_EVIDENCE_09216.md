# 2603.09216 — PIM-SHERPA必要Source/PRE/实际POST通过

[exact-v1](https://arxiv.org/html/2603.09216v1)。第二包root实际完整题摘/current准入通过。current仅v1、13pages/13figures，无现页撤回/纠错/accepted先稿信号，不为证明没有信号扩扫历史。拟评分2+2+2=6：cache属性/host–PIM阶段布局重要替代分支，跨host/cache/device边界，可复用的权重驻留与转换约束；owner具体gap触发受影响内容深入。

## 日期与必要阅读范围

SUP_EXACT_BATCH2.json保存原字段：Tue10Mar05:39:03UTC提交；官方no-advance finalID/DOI与deadline提供earliest Tue20EDT=Mar11BJT08下界；arxiv.content owning、findable DOI created Mar11UTC02:08:10/registered02:08:11为already-discoverable上界。两界同03-11BJT，只夹证arxiv日，不用Submitted/Updated/registration单独当公开，不捏exact公告。无具体先稿线索；请root原字段独核后授日期。

作者实际读取v1§1/2.1–2.4的必要定义、§3全、§4/5/6/7全HTML文字与嵌入Tables2–4，未把搜索摘要或正文页面可打开当读完；图中未提供文字的精确点位未采用，不声称独立读完全部图像/附件。支持与直接反侧足够，停止无关RelatedWork与全部引用。

## 核心机制：cache属性不等布局

§2.4/3.1：此类请求触发的PIM每次DRAM read对应MAC；若权重cacheable，cachehit会吞掉应到controller的命令，hardwareprefetch/unintendedrequests也影响同步。Prefill GEMM又依赖缓存权重反复复用，因此同一权重“逻辑可见/布局正确”不保证阶段执行语义；non-cacheable对这个执行模型必要，不推广所有PIM架构。

§3.2：复制cacheable host-friendly与non-cacheable PIM-aware全权重是合理简单baseline，但模型已接近端侧DRAM容量时近乎翻倍；硬件地址translation的FACIL只能解决layout，不自动解决cache attribute，不能用logicalview覆盖访问属性。此文FACIL-O另假定其解决属性冲突，是oracle对照非实际原硬件。

§4.1–4.4：保留单份PIM-aware权重于non-cacheable区域，为Prefill创建小cacheable host-friendly buffer。Swizzledcopy按矩阵坐标→DRAM bank/row/addressmap找到源，复制时重排成hostfriendly，既有GEMM backend不改。DDB两个buffer各按最大FF matrix大小，当前GEMM与下一权重copy并行；QKVO合组、FF0四份分配至Q/K/V/O阶段，避免在memory-bound非线性/Norm/attention阶段发copy。copy/compute两线程组每层同步，buffer必须遵循完成再交接（本书推断）。OWR单buffer，先swizzle/copy再GEMM，省显式并行同步但必付串行copy。OWR每step创建/join两线程组不等零线程开销。

原文字“decoder layer”与Q/K/V/O/FF projections层级混用；采用最大weight matrix容量规则，不将FF=4H写成任意模型硬配方。§4作者Llama3.2示意2*H*4H totalbuffer，实际§6对1B每buffer32MB，两缓冲比单缓冲多32MB，所有模型target矩阵依真实shape另算。

## 关键评价：功能/时间/容量分账

§5 GalaxyS24+、Exynos2400（CortexX4、A720六big/middlecore，四用于GEMM、二copy；A520不用）、LPDDR5X8533四channel68.264GB/s，BF16、Llama3.2 1B/3B、batch1。6core算力321GFLOPS是peak非利用率；使用四计算核是六核尾效应，不能当所有host最佳固定配置。

决定性限制：该设备CMA-backed可non-cacheable contiguous区域约1GB，完整1B/3B权重至少2.4GB/6GB无法放入。Prefill时间用dummy noncacheable权重测copy+GEMM，功能用真实权重但cacheable源转换后对原ExecuTorch outputs；两者不是同一次完整模型实机执行。Decode时间PIMLibrary发dummy noncacheable请求的LPDDR5X-PIM emulation；功能另接PIMSimulator真实权重+input地址与CPU输出比较。没有实际LPDDR-PIM设备直接验证GEMV正确性。Table4 realHBM-PIM与AMDMI100 HBMemulation误差0.14–3.54%只验证对应GEMV请求时序线索，不自动证明完整手机simulateddecode误差/质量/production。

§6内存47.8–49.7%是relative to weight duplication所需DRAM，不是KV可接纳并发、全应用峰值或已测power。1Bhostweights2.47GB，PIMpadding多80MB；3Bhost6.4GB。比FACIL-O还要付一/二cacheablebuffer，内存不是绝对减半/理论最优。

SL64–192 input/output有限作者end-to-end emulation组合，不能写真实完整手机运行。DDB在SL128–192接近oracle TTFT，OWR3B/SL192的16.7TPS仍是上述路径；OWR总保留串行SMC1B约.6s/3B1.4s。DDB两copythreads1B.89s/3B2.54s，noncacheable→cacheable实测约慢两倍且仅约1/4peakBW，原§3.3分析预测SL16可隐藏，实际约SL128才成立，短SL32 contention可令DDB不优OWR，SL64–96与oracle差2.5–19%。schedulerslot争用/GQA K小matrix仍critical，不按MAX公式签必重叠。

§7高FLOP/B平台（Jetson/Blackwell）可令SL128TTFT仅约理论1/3，长prompt摊销是作者推断不是GPU/NPU实测；precision仅BF16、energy/thermal/repeatedruns/CI/concurrency/requesttail与完整SLO Not Disclosed，noqualitybenchmark认证。不采“普遍product-level/适用所有系统/软件零成本”。

## actual owner与逐字提案（未写Books）

唯一owner `INFER-GPU-MEMORY`：[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)“Physical Layout与Accessor View可以分离”。作者实际读当前562–591完整局部、640–657交接、737–767末段，及Ch53/55开篇；前三段拥有单physical object logicalview与translation，一般映射/一致性成本不能承载cachehit吞命令的访问属性约束及软件cacheable staging分支。后CD-PIM two/two pseudo-bank阶段分工解决资源并行，不替本项attribute；不静默替代该硬件分支。拟插现有physical/logicalview sourcecomment后、CD-PIM正文前。正式逐字两段供root必要Source/PRE：

但 accessor view 还不足以决定访问的执行语义：在由 DRAM 请求触发计算的近存系统里，一次权重读取若命中 host cache，预期的计算命令就没有到达 memory controller；Prefill GEMM 又需要缓存复用。仅转换地址或布局不能同时满足这两个条件。容量允许时，分别保留 cacheable 的 host 布局与 non-cacheable 的 PIM 布局，是简单的合理基线；容量逼近单模型大小时，一个软件替代分支保留单份非缓存 PIM 权重，只将当前所需矩阵 swizzle/copy 到小 cacheable buffer，供原有 GEMM 使用。[必要机制](https://arxiv.org/html/2603.09216v1#S4)以双缓冲重叠下一矩阵搬运，或用单缓冲串行转换换取简单顺序；buffer 的布局、访问属性、复制完成和消费者交接须共同明确，这是由接口推得的责任，不能把地址可见直接当成可执行。<!-- source-family:SF-2026-ARXIV-2603-09216 -->

省去全模型副本仍支付 buffer、swizzle、copy threads 与同步，并依赖计算时间足以覆盖搬运。短输入、较高 FLOP/B、non-cacheable 访问较慢或线程争用，会让转换重新进入关键路径；单缓冲始终保留串行 copy，双缓冲也不保证完全隐藏。[有限评价](https://arxiv.org/html/2603.09216v1#S5)把手机 dummy 权重时间、cacheable 真权重功能检查与 PIM 仿真分开，因为设备连续非缓存区装不下完整模型；它不是完整 LPDDR-PIM 实机部署验收。所报容量节省只相对双权重基线，不认证任务质量、并发或 SLO。硬件属性、质量或净收益不成立时，保留双副本、直接 host 执行或原地址转换路径，不用较少常驻 bytes 签发统一加速保证；bank 分工仍可在其各自条件下共存。<!-- source-family:SF-2026-ARXIV-2603-09216 -->

拟本人末注（保留提案时态）：`SF-2026-ARXIV-2603-09216` — Daily2026-03-12补查；exact-v1§2.4/3–7，2+2+2=6，cache属性/命令触发与layout不同、软件staging具体差额深入。CMA约1GB装不下完整BF16模型，时间dummy/功能cacheable真权重/decode仿真分账；47.8–49.7%只相对weightduplication，oracle FACIL-O非实际属性保证，短SL/高FLOP-B/线程争用反侧与copy费用近正文。未核artifact/复现、真实LPDDR-PIM功能/质量或完整SLO；必要Source/逐字PRE待非作者核，root写后须非writer actualPOST，不授DAY。

当前实际：root独核原日期字段及v1§2.4/3–7文字/Tables2–4，并补§6必要255–260，Source/逐字PRE通过，已写Ch54两段。非writer supplement_20260312实际顺读新581/583、570–619完整邻接及本人941末注，回对本轮原证，actualPOST通过。cache属性不是viewtranslation、单双buffer条件/费、实机/仿真功能时间分账、旧CD-PIM与load-ready共存均一致。root负责本人注同步，作者不写共享章，不授DAY。
