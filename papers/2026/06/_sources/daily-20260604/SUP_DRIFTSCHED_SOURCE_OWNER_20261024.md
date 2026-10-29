# DriftSched 02982 最小必要Source / actual同family纠错 / 两段PRE

作者supp_20260604_author。R27准入/Jun03联合日证复用，2+1+2=5不改分。因actual Ch56同family旧正文与exact-v1支持边界有具体冲突，深入受影响域。HTMLfirst正文II–V已读：II-C/D/E/G/H/I/J，III与IV-B–J各表及V futurework为必要支持/反侧；无需遍历refs/code，未核figure像素、实现或复现。完整直取HTML剥标TEXT83133字符保存在SUP_CORE_2606.02982v1_TEXT_20261024.txt，无工具truncation marker；数学保留原HTML文本/LaTeX重复渲染。前一次18000token输出工具截断未采用，改30000token完整取回；不沿截断记录签Source。

## 必要证据及未证明

II-C用Tbudget=Tinput+Tbase×Bruntime×Stenant×Finput，short≤128/medium≤512/long>512；语义shortQA/summary/technical/report与runtimeclass不同。II-J式5–6在完成后以Bmeasured=Tactual/Tbase进行EMA；B初始化1、类别bias反馈到未来admission，不是当前request的在线remaining predictor。Tactual明确只是whitespace-delimited word count，非实际tokenizer token，更不等wallclock服务成本。算法没有在这些式子中消除Stenant/Finput的影响，故不当普适无偏校准公式；不照抄为生产recipe。V明确online reclassification of queued requests/adaptive queue reordering为futurework，不能把旧Book的“按Decode进展更新优先级/持续重排”归该实测。

III/表II: 单NVIDIA L4 24GB/72W/PCIe4x16，Xeon6 24c48t/32GB DDR5，Ubuntu22.04，CUDA12.2/driver535.288.01，PyTorch2.4+cu121/vLLM developmentbuild无exactcommit，Qwen1.5-1.8B-Chat FP16；FastAPI/Redis。每run3000requests/50clients/batch32/wait.01s、3独立runs，约1180unique prompts。1000calibration+2000stress但后段继续在线更新，并非冻结heldout测试；prompt长度/输出cap/temperature及到达率完整矩阵Not Disclosed，不授真实Poisson/生产trace或跨模型结论。

III-B明确除误差对照外所有scheduler比较BIAS=ON。IV-G/T7：开关bias的MAE平均38.80%、RMSE40.49%下降只估计代理，不提供同schedulerON/OFF尾延迟因果差额。IV-E/T3、IV-H/T4：ON的SJFvsFIFO P99 526.363vs630.205s，std5.028/1.502仅3run描述，非显著性保证；不能把这16%写成bias校正因果收益。IV-F/T6 shortwait2.87s/long396.59s，对FIFO166.89/258.04，长侧负面成立。T5 SJF Premium226.60s/Batch94.91s，Priority Premium77.32/Batch426.72，说明全局延迟与tenant区别，不授硬fairness/不存在starvation。IV-I/J utilization85–92%、memory约14.5GB、GPUexecution P50约10.5/P99约11.3s近似不变，只支持本配置差额主要在排队，不证明推理runtime本身加速。校准请求/完成状态/telemetry/Redis维护/重排及失败请求全费不能省略；可选代码未核不阻塞上述负侧结论。

## actualowner与最小修正理由

ROADMAP owner唯一INFER-SCHEDULING Ch56。完整读本章1592–1624 estimate/TokenDrift/NetworkOracle及相关138–146点估计/CVaR/FuelGauge、205–214影子价格与独立predictor分责；旧同family note1837–1841仅作身份路由不继承旧采用充分性。Ch55开篇/物理handoff、Ch57平台资产与契约职责已定点读，不复制调度机制。

旧同family两段实际把完成间反馈写成当前Decode进展重排，并借“作者实验”共同托底。不能主题NC或只加末注隐藏差额。建议只替换原H3下的两段（保原H3、semantic binding、完整两侧、旧note日期/归属），明确完成→未来admission与本requestsensor两层；再补测量proxy和ON/OFF归因反侧。以下原稿尚未独立Source/owner/PRE、未授实际写，不先计I。

完整上锚：

当配置变化会改变下一轮 batch、KV 驻留或迁移路径时，给每个 request 贴一条固定 service-time 曲线还不够：模拟的 scheduler/memory manager 应先根据当前状态决定本轮工作，再生成对应 operator DAG、KV load/store/transfer 与 collective 依赖，交给执行模拟器结算 contention，完成结果再反馈下一轮决策。否则 routing/cache 策略改变了资源竞争，却仍消费旧时间表，规划器便无法观察自身选择的后果。[LLMServingSim 2.0 v1 §3–4](https://arxiv.org/html/2602.23036v1) 支持这种反馈接口；A6000/H100 的有限校准中，聚合时长误差小于时间序列误差，不能用平均误差认证 tail SLO。Profile 的模型、kernel、batch 与运行身份、GPU/host 的不同 KV 粒度都须绑定，CXL/PIM 分支仍是模拟而非实芯部署。采样 profiling、任务图构建和详细 contention 模拟也有费用；状态或 profile 失配、费用难摊销时，保留较粗容量估计并用真实 trace/shadow 对账，不把可模拟的硬件配置视为生产能力。<!-- source-family:SF-2026-ARXIV-2602-23036 -->

受影响原组（H3和binding保留，仅换中间两段）：

### Token Drift 改变剩余工作时，要重算队列承诺

Admission 时用预测输出长度估算 service time，在长度稳定时足以支持 SJF 或静态优先级；推理过程中真实生成长度偏离估计后，
继续沿用旧排序会让短请求被误判成长请求、长请求持续占用设备，并把最初的预测误差放大成 tenant starvation。调度器应把
`admission estimate / observed tokens / remaining-work estimate / queue age / SLO slack` 保存在同一 request state，按 decode
进展更新优先级。Estimator 只提供 hint，scheduler 才拥有队列顺序与 preemption commit。

持续重排减少 token drift 带来的 head-of-line blocking，却会引入重排开销、预测震荡和对长请求的不公平；观察窗口太短时，
还可能把正常 early variance 当成永久趋势。估计不稳定或 aging threshold 触发时，应回退带 aging 的 SJF、FIFO/EDF 或保守
reservation。作者实验只支持其多租户 workload 与 QoS 设置，不证明某个更新频率或权重适用于任意模型和 tail SLO。

<!-- semantic-body-binding:SF-DRIFTSCHED-TOKEN-DRIFT -->

拟替换两段：

Admission 时按预测长度给请求排序，在分布稳定时是便宜的基线；当某类请求的实际输出持续偏离估计，可以把完成后的观测长度与该类基准长度之比做平滑，更新其 bias，再供后续请求的 admission estimate 使用。[受限漂移校正实验](https://arxiv.org/html/2606.02982v1#S2.SS10)把语义类别、估计工作量与 tenant 策略分开，但这不是按当前 Decode 进度持续重排已入队请求：该在线 reclassification/reordering 仍列为未来工作。Estimator 只提交估计，scheduler 才拥有顺序；若要消费当前 request 的 remaining work，还须另验进度 sensor、重排时效与实际 runtime state。

误差变小也不能直接签发尾延迟收益：该实验的输出长度是空白分词代理而非 tokenizer-exact token，bias 开/关对照报告估计误差，SJF 与 FIFO 的延迟比较则均启用 bias，因而未隔离校正本身对尾延迟的贡献。SJF 的整体延迟改善还伴随长请求等待增加和 Premium 服务差异变弱，不能把全局平均排序等同 tenant QoS。校准流量、遥测、状态维护与队列操作均计费，模型或流量漂移时重验长度口径、误差、调度及各租户结果；证据不足或净收益不成立时，保留静态基准、带 aging 的队列、FIFO/EDF 或保守 reservation，不以收敛 bias 代替硬 SLO。

完整下锚：

### Network Cost Oracle 只提交 Placement Score

已有 KV 的 decode instance 未必是最便宜的目标：缓存可能位于远端拓扑，迁移会占用关键链路；本地重算有时反而更快。
因此 disaggregated scheduler 应联合比较 `KV location/bytes + topology revision + measured transfer time + target queue/service time +
TTFT slack`，在 local hit、remote transfer、recompute 与 reject/degrade 之间选择。Cache manager 拥有 residency 和 transfer
receipt，network oracle 只提供代价，scheduler 才能提交 decode placement。

网络感知选择减少盲目搬运，却依赖拓扑、带宽和队列测量；cost model 漂移、传输失败或 placement 后发生拥塞时，会增加
重路由、重复 KV 和尾延迟。网络不可观测、KV 很小或复用弱时，locality-first、least-loaded 或直接 recompute 仍更稳。
exact-v1 只支持作者 fat-tree、prefill/decode pool 与插件式 scorer 的实验，不证明对任意集群或生产 SLO 最优。

<!-- semantic-body-binding:SF-NETKV -->

本人trueH2注拟：`SF-DRIFTSCHED-TOKEN-DRIFT`：Daily2026-06-04补Jun03，exact-v1 II–V必要域，2+1+2=5因旧samefamily attribution冲突局部深入；仅完成后类别bias→未来admission，queued reclassification/reordering仍future，不继承旧Decode-progress实测归因。保wordproxy非exacttokens、ON/OFF误差与ON调度延迟两人口、单L4/单模型/三run与长job/tenant反侧及全费。不授因果尾SLO、完整EMA recipe或实现复现；待独立PRE/新授/实际POST。

