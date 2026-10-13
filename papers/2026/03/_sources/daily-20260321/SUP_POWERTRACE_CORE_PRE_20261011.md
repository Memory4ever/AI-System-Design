# PowerTrace2603.18383v1：必要原证、实际 owner 差额与 PRE

03-21仅补03-20自然日，root准备，尚未独核或写Books。本日首批准入及日级日期依据复用 SUP_FIRST_ADMISSION；日期身份待整日独核，不授全年无遗漏。拟评分2+2+2=6，具体设施规划差额需深入。

## 原证与有限停止

[exact-v1 HTML](https://arxiv.org/html/2603.18383v1)实际§3.1–3.4、§4.1–4.5、§5.1–5.3已读；不遍历无关relatedwork、所有附录或代码，不声称复现。公开原段支持：配置专属功率状态分布/活动条件状态序列→server trace→rack/site sum；BiGRU使用未来活动，属于离线scenario，不是因果在线controller；FIFO/TTFT/TBT surrogate不重演真实batch/preempt/KV scheduler。Dense状态内独立采样、MoE状态内AR1只补部分持续性，特征不能看到expert routing；功率裁到训练观测范围，不能外推未见峰值。

评价为Azure DGX 8×A10080GB/H10080GB、vLLM0.10与TP配置；NVML/nvidia-smi250ms，七到达率各五次、四prompt集，模型Llama3.1 8/70/405B、R1蒸馏8/70B、gpt-oss20/120B，trace级70/15/15切分，五生成seed；精度、完整输入/输出分布、正式生产SLO未完整披露，不补造。实测server Poisson与设施合成分开：240server虚构布置、Azure一天请求snapshot随机offset、固定1kW非GPU/PUE1.3，不是测得真实场站。本文server能源/ACF/KS/NRMSE有限验证不能推出所有分布；MoE时序更差。Splitwise启发LUT是A100/Llama2表迁到Llama3.1 surrogate，不是原系统复现/公平统一调优。

直接反侧：§4.3 facility段正文TP4与Fig8 caption TP8不一致（不是§4.4）；§4.4 row先写跨5seed24hpeak≤600kW，后按P95超过cap搜rack数，不能采用具体密度/安全倍率；§4.4mean model平均值文字方向与Table3亦冲突。不采用这些数字或hard超配保证。组合接口/相关性依赖仍由§3/4.5/5.3独立支持，审阅者须裁是否可与局部争议分开采用。源明确constant PUE、隐藏runtime变化需重训和强相关削弱平滑。Future Agent与annual延伸属建议，不记已验证。

## 实际章节与差额

ROADMAP唯一 PLATFORM-COST/Ch70/Legacy66。实际Ch70 132–355和355–465已读，前置§资源时间与结果口径实际读过；Installed Power已有拓扑/冗余→feasible placement与what-if、其后EasyRider有硬件buffer/ramp分支，Generation Energy已有解析proposal+实测校准。没有将请求活动序列/配置状态功率分开、相关性/聚合时序与未来信息权限的具体设施trace接口，不能主题NC。Ch69首58 trace是请求critical path采集，Ch71首55 tenant身份/隔离；均不接管设施规划与功率外推。选择一处插Installed Power通用what-if段后/已有power-ramp paragraph前，连接“空间可部署性→时间上同时发生的功率”，保留全部旧内容。

## 拟逐字 PRE

空间上的可部署集合确定后，还要问这些服务器何时同时耗电。按铭牌功率相加保守且易复算，平均功率适合长期能量预算，但两者都抹掉请求排队、计算/空闲切换与跨机突发的重合。一条离线规划分支把请求到达先转换为活动序列，再用特定模型、硬件和并行配置的实测状态功率分布合成 server trace，最后按机架、行与站点聚合；改变流量场景可以复用配置模型，改变运行时仍可能需要重新校准。使用未来活动的序列模型只服务离线 what-if，不能直接拥有在线 admission、power cap 或安全控制权。<!-- source-family:SF-2026-ARXIV-2603-18383 -->

这种组合减少逐个场景全量测量，却把延迟代理、状态识别、服务器间相关性和设施附加功率引入误差预算。独立负载的峰值可能错开，强相关突发则会减少超配余量；聚合能平均部分随机误差，不能消除系统性偏差，更不能用总能量吻合证明峰值、ramp 或尾部安全。[受限功率合成研究](https://arxiv.org/html/2603.18383v1#S5)只核其 vLLM/DGX 配置与到达负载，MoE 隐藏路由的时序拟合更弱，固定 PUE 与功率观测范围也限制外推。实际场站应保留相关性压力场景和独立实测验收；资料不足、负载同步或运行时失配时，仍用保守铭牌/容量预算，而不是把合成 trace 当硬超配许可。<!-- source-family:SF-2026-ARXIV-2603-18383 -->

静态源注拟：`SF-2026-ARXIV-2603-18383`，[exact-v1](https://arxiv.org/html/2603.18383v1) §3–5；采用离线活动序列/配置功率状态/设施聚合接口及相关性边界。DGX A100/H100、vLLM0.10、250ms实测与固定PUE/1kW设施合成分开；MoE残差、隐藏scheduler与范围裁剪保留。不采TP caption冲突、P95/peak混用的rack倍率及局部mean文字冲突，不授在线因果控制、硬超配安全或通用收益，未核代码或复现。

## 非准备者必要 Source / actual owner / literal PRE 独核

2026-10-11 resume_mar18（非packet准备者/非Books writer）实际独立重载本03-21 AGENTS、研究/Report/Sources每日与arXiv、统一prompt、ROADMAP及本日STOP；Book背景/学习/写作合同和LS仅相关路由亦实际读。独立打开exact-v1官方HTML，完整实际读取§3.1–3.4/Eq1–11、§4.1–4.5/Tables1–3及Fig8/row标准/aggregation、§5.1–5.3；必要支持与直接反侧足够即停，没有全文附件/代码/复现或版本史展开。

**SOURCE/PRE正式PASS（限定独立接口采用）**。§3的configuration GMM→BiGRU activity状态→power sampling与server/rack/row/site sum、§4.5相关性/系统偏差及§5.3scope独立支撑两段受限离线组合接口，不依赖§4.4精确容量或Mean数值。确认BiGRU前后文读取未来、FIFO batch64 lifetime surrogate不是完整scheduler、power裁到training观测范围；Mixture不授真实prefill/decode物理状态身份，MoE AR1仅补局部相关、固定PUE/1kW另列假设。§4.2 gpt-oss20B energy11.2%、KS.48与prose“preserves energy well”/“well matched”也不授MoE普遍能量精度；两PRE未采用它们的强数字，因此不需扩写。

已窄纠packet反侧定位：Fig8 TP4/8在§4.3而非§4.4。实际Mean Table3 .85高于Ours .63却prose称低估、row peak5seed≤cap与P95停止标准混用成立，继续不采用具体比率/硬安全。原两段与本人静态注逐字读回，通过；不为局部错误暗改或认证这些强claim。

actual Ch70开篇资源时间/结果合同、132–355成本/installed power/相关power选择，以及355–395 generation-energy/actuator交接实际读取；重点完整270–294 InstalledPower→what-if→旧EasyRider→水耗，Ch69首58与Ch71首55边界已读。`PLATFORM-COST` sole差额成立，空间可部署性已有但活动/配置状态与相关聚合时序尚未承载；两PRE应放现284 familymarker后/286原ramp段前，不覆盖旧机制。静态注仅原证/必要范围/边界，不放验收过程。

不授写后POST/DAY；root协调本人窄写、完成后交resume_mar18一次实际完整局部/静态注非writerPOST。原日期夹证限定有效复用，非本次全源覆盖验收。

## 一次非writer actual POST

2026-10-11 resume_mar18实际完整顺读Ch70 270–305 InstalledPower→新增286/288→旧EasyRider→水耗/地域后交接，445–453本人453静态注及邻注；两正文逐字回有效PRE，静态注与必要§3–5原证边界一致。离线future权限、configuration身份/重训、相关性/系统偏差、观测裁剪/MoE限制与保守铭牌退路均近文，不采局部争议密度/Mean/cap数字，不扩大为真实设施、在线安全或通用收益。POST正式PASS，限定git diff --check无输出；不改Books注动态身份/验收流程，root可释放Ch70本family窄锁，正常归并本日实际整合（2+2+2=6），未授DAY。
