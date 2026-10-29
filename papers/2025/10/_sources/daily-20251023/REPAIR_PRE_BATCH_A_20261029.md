# 三项完整 PRE：仅以下精确插入位

writer Locke；sole reader Chandrasekhar。本稿尚未写入Books。支持/直接反侧见本日REPAIR_EVIDENCE；实际owner及相邻交接已读，禁止全章锁。每项只加一段、独立marker及唯一H2 Review notes后的本人注，不改现有段/他注。三者均6分，具体长期差额触发深入而非以数量配额决定。

## A1 TokenCake / INFER-SCHEDULING / Ch56

文件：`books/part-05-inference-system/56-inference-scheduling.md`。现有ProgramState与实际tool progress已有覆盖；新差额是预计停等窗必须同时容纳搬运与被借用空间的其它计算，不是有等待就可offload。邻Ch55仅PD交接，Ch57仅平台生命周期，不迁移owner。

### 完整前邻接（保持）

“工具正在运行”仍不是足够的 progress state。调用前的历史均值、工具名或 self-declared duration 无法知道本次何时完成，长调用的排序甚至可能反转；若工具在 stdout、artifact 或 protocol notification 中已经暴露阶段进度，harness 应在 KV retain/offload/restore 决策点读取这一信号。工具只拥有自身 progress observation，cache manager 仍拥有真实 KV residency，scheduler 才能提交迁移计划。无流式信息、输出不可解析或人工等待时，系统必须承认 opaque state，回退保守 lease/timeout，而不是制造精确 ETA。公开证据只覆盖四个工具生态与三个 serving extension，生产收益受 signal coverage 限制。

### 完整新增稿与独立 marker

停等期间释放KV还须通过一份时间上的准入，而不只确认当前没有Decode：预计工具空隙应足以覆盖卸载、恢复以及借用这份空间的其它工作，否则搬运可能延长恢复关键路径。可先卸出未共享历史，再按预计回调时点渐进预留和预取；复制已发出、旧GPU块已能重用、恢复状态已可消费是不同事件，真实完成前不能重复分配。[TokenCake的受限实现](https://arxiv.org/html/2510.18586v1)支持这一空间—等待联合分支，但工具调用在评价中由模拟时长替代，预测误差、CPU容量和双向传输争用仍会使收益消失，混合优先级也不保证所有任务公平。时长预测、驻留副本、预留和实际搬运均计费；调用短、ETA不可靠或恢复延迟超预算时，保留原驻留、保守预留和反应式恢复，不由停等标签或平均吞吐批准生产SLO。

<!-- source-family:SF-2025-ARXIV-2510-18586 -->

### 完整后邻接（保持）

多租户公平也不能只按长期 token share 衡量。更强的隔离合同把每个 token 在独占 fair-share 资源下的预计完成时刻作为 baseline，并要求共享执行最多增加可配置的 `δ`；scheduler 据此产生 per-token deadline，同时把 compute waiting 与 KV eviction/restore delay 一起计入。它用模型误差、保留部分 KV、可能降低 packing 效率的代价，换取 TTFT、TBT 与 TTLT 的上界；当前 SGLang 实现与 `δ=3s` 实验不证明跨 GPU、跨 workload 或任意性能模型都满足保证。估计失准或硬件缺乏细粒度隔离时，应回退静态 partition、保守 admission 或更宽的 request-level SLO。

### 本人注与注位完整邻接

置于唯一 `## Review notes` 后、下列原首注前：

本人注：`SF-2025-ARXIV-2510-18586` — Locke，Daily2025-10-23补Oct22；exact-v1 §3–7.4必要，2+2+2=6。仅工具停等窗/其它可填工作与KV搬运准入深入；保工具模拟、优先级方向/公平未闭、CPU/网络全费，不授真实tool分布或生产SLO。未核实现/复现，整体PRE/真实SAVE/完整自读/sole actualPOST仅按本日canonical实际层。

原首注保持：

- `SF-2025-ARXIV-2510-13668` — Daily2025-10-17补Oct16；R3唯一必要exact-v1 S3–6，2+2+2=6，仅持续剩长proposal/不迁移选项与迁移全费差额深入。保request70/15/15、20步间隔0.38%口径、vLLM0.9.2/4×4090D/1P3D/R1DistillQwen7B W8A8/ShareGPT-Alpaca、10Gbps TBT反侧、8–256 oracle模拟和stream非exact-once；未核实现/复现，PRE/SAVE/完整自读/solePOST按实际canonical。

## A2 CAD / TRAIN-DISTRIBUTED-TRAINING / Ch36

文件：`books/part-04-training-system/36-distributed-training.md`。已有有界pool冻结step样本并在pool内分配sequence/head；新稿是无参数core attention从含权重路径逻辑拆开，query-shard可独立重批、设备又可原地改派，并非把已有pool改名。Ch35保存训练事务、Ch37拥有参数矩阵TP，不占它们的机制。

### 完整前邻接（保持）

这条路线获得更小的 straggler tail，却新增 all-to-all bytes、CPU planning、metadata broadcast、KV dedup、
floating-point operation reorder 与 topology-sensitive pool/tile 参数。更大的 pool 提高聚合范围，也会增加通信；
overlap 只能隐藏中段，first dispatch 和 final return 仍暴露。现有证据绑定 Qwen3-30B-A3B、256K/1M packed
sequences、mbs=1 与 NVIDIA NVLink/RoCE，且没有证明 bitwise-equivalent gradient、sparse/linear attention、
完整 DistCA/WLB-LLM end-to-end superiority 或跨 topology 收益。短 context、轻 skew 或控制开销占主导时，
packing + Ulysses 仍更合理；统一高带宽域内，global pool 也仍是可比较分支。数据 packing identity 归第 27 章，
PP bubble 与 schedule 归第 38 章，本章只拥有跨并行维度的 workload redistribution contract。

### 完整新增稿与独立 marker

另一种拆分不是扩大固定pool，而是把不含模型参数的core attention从投影和MLP路径中逻辑分离：query可切成较细工作项，分别读取所需完整K/V，再按预计算量、传输与当前负载重批和放置；含参数路径仍维持自己的训练布局。[CAD的受限分支](https://arxiv.org/html/2510.18121v1)还允许GPU在原地切换执行角色，因此逻辑独立池不等于两套永久隔离硬件，也不免除KV驻留和双缓冲成本。调度只改变算子执行位置，不能改变样本、梯度依赖与step身份；query小片过细或上下文较短时，首尾通信与规划可能盖过均衡收益。原H200/TP8及指定长序列负载支持这一替代，不把重实现且未含全部延期执行优化的基线差额当通用领先或逐bit梯度保证。Profiling、重批、传输、驻留和角色切换均计费；拓扑、依赖或净收益失配时，回到原训练布局、有界pool与成熟Attention执行。

<!-- source-family:SF-2025-ARXIV-2510-18121 -->

### 完整后邻接（保持）

有界 pool 仍常按互不相交的 SP groups 执行；当一个 step 同时包含少量超长与大量短样本，选择组大小又会把长样本的容量需求传给短样本。一条不同的执行分支把 rank 排成对齐的二叉 SP tree，允许同一 GPU 在同一 attention pass 参与路径上多个层级的 nested groups：长序列用上层大组，短序列填下层小组。Planner 在 token budget 内以模型 profiling 的 communication prologue、compute、epilogue 代价搜索长前缀并贪心放置短尾；executor 再用各自保持 issue order 的 compute/communication queues 交错不同节点，防止后发 collective 抢走前发关键路径带宽。<!-- source-family:SF-2026-ARXIV-2609-22755 -->

### 本人注与注位完整邻接

置于唯一 `## Review notes` 后、下列原首注前：

本人注：`SF-2025-ARXIV-2510-18121` — Locke，Daily2025-10-23补Oct22；exact-v1 §4–6.3/8必要，2+2+2=6，仅无参数CA池/query-shard重批与原地角色切换差额深入。保H200/TP8、短context通信反侧、基线重实现/缺deferred execution及KV驻留/规划全费，不授bitwise梯度或普遍领先；未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

原首注保持：

- `SF-2025-ARXIV-2510-05476` — Cicero，Daily2025-10-09补Oct08BJT；[cMPI exact-v1](https://arxiv.org/html/2510.05476v1)A149首次必要§2/T1、§3全/API T2及§4全部决定文字，2+2+2=6，仅CPU MPI跨host DAX对象/RMA与每pair SPSC消费者深入。保coherence/原子/完整指令序未认证、CPU复制与大包反退、TCP非RDMA与模拟/collective future及全费，不采零拷贝/AI全链净速或通用并发proof。未核曲线像素/MPICH代码/跨机复现；PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

## A3 R2BC / MULTIMODAL-EMBODIED-VLA / Ch26

文件：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。现有human/robot/sim来源对齐不含一次只示范一成员、其余当前policy造成协作人口这条采集接口；不归Ch82语言Agent编排。相邻Ch25只环境预测，Ch27接数据lineage，不复写。

### 完整前邻接（保持）

后一步没有否定前一步。越远离真实 embodiment，数据越容易扩展，action semantics 越弱；越接近真实 robot，成本越高，物理证据越强。

### 完整新增稿与独立 marker

多机器人协作还可以把示范的控制负担与联合执行人口分开：每个episode只由人示范一名成员，其余成员运行各自当前policy，再将被示范成员的观察—动作写入对应buffer并周期性更新BC；轮换被示范者，让数据逐步包含同伴policy造成的状态变化，而不要求人同时控制整队。[R2BC的有限模拟与三机器人对照](https://arxiv.org/html/2510.18085v1)支持这条采集分支，不证明各policy独立训练就能收敛到任意协作最优，也不等部署感知完全分散：实机仍用中心相机与派生测距，零介入导航的差额也未显著。全部示范、同伴rollout、重训、标定和后续人工纠正均计费；同伴持续漂移、恢复状态未覆盖或真实感知失配时，保留固定同伴/联合示范、可信BC与独立controller，必要时接管，不由较少同步遥操批准无人安全。

<!-- source-family:SF-2025-ARXIV-2510-18085 -->

### 完整后邻接（保持）

多来源先使用同一动作shape仍不够，还须分开坐标、身体与时间：可将机器人末端和人手代理都映到相机frame，把URDF或人类数据源的morphology条件只交给action expert，并按物理时长而非统一步数构造chunk。[ACE-Ego的受限分支](https://arxiv.org/html/2606.17200v1#S3)再让真实robot动作承担主目标，对human伪动作按通道及局部平滑代理重权后提供辅助监督；这些代理不是可校准的物理正确率，归一权重也不等给每个来源设置绝对贡献上限。统一frame没有消除标定、IK、身体动力学与controller，平滑过滤还可能削弱真实快速动作。Drop-one与数据增加对照不独立识别全部收益，少量human增强trial和桌面任务不能签发跨本体或接触安全。视频恢复/筛选、morphology编码、分桶padding、混合训练和真实闭环回归都付费；伪标签、坐标或目标控制不可靠时，保留native示教、robot-only训练、明确时长与独立controller，不让更多human视频或共享接口替代物理验收。<!-- source-family:SF-2026-ARXIV-2606-17200 -->

### 本人注与注位完整邻接

置于唯一 `## Review notes` 后、下列原首注前：

本人注：`SF-2025-ARXIV-2510-18085` — Locke，Daily2025-10-23补Oct22；exact-v1 III–VIII必要，2+2+2=6，单成员轮换示范/同伴当前policy/独立buffer差额深入。保VMAS10seed、三HeRo+/中心ArUCo和mock LiDAR、五实机初态/3s介入及navigation p=.0773反侧；人工负担/收敛未证，示范重训/标定全费。未核实现/复现，不授分散感知或物理安全；PRE/SAVE/全自读/sole actualPOST仅本日实际层。

原首注保持：

- `SF-2025-ARXIV-2510-15720` — Daily2025-10-21补Oct20；Lorentz首次exact-v1§3.2 Theorem5/8、§4 Theorem1/Remark1与§5.1/5.2，writer核Theorem5，2+1+2=5，期望风险预算/critic sup误差接口深入。保初始budget、2Delta/(1-gamma)条件与正文slack口径差异，不抄完整recipe；三seed/SafetyGym有reward反退与cost波动越线，非每轨迹硬安全。未核实现/复现，shield端到端硬件成本Not Disclosed。
