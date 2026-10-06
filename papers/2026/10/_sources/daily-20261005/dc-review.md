# 2026-10-05 DC 七项必要证据审阅

作者：oct04_daily（本轮明确切换到 10/05）；范围仅七项已独立题摘准入材料。窗口 `[2026-10-04T09:00:00+08:00,2026-10-05T09:00:00+08:00)`。本文件不是 Daily Gate，也不是非作者复核通过。未运行 artifact 或复现实验。

## 日期、版本和审阅身份

主作者已核本批公告 10/05 08:00 BJT；本作者重新实际取得七个 current abs，全部只有 v1，history/页面未见 withdrawn、retracted、erratum、corrected 标记（见 `dc-current-history.json`）。提交时刻不当作公开日：02522 是 10/01 21:52:30 UTC；其余分别 10/02 10:07:36、12:20:29、13:29:40、14:43:42、15:02:00、15:33:33 UTC。首公开归属须结合主作者公告证据，不由这些 history 时间推断。

Coda/AFORE 接收了主作者实际已读切片交接，但以下采用判断均由本作者继续实际读必要原文与反侧。HTML 优先；Beaver exact-v1 HTML 404，exact-v1 PDF reader 失败，官方 current PDF 成功且页1明确 `2610.02522v1`，current history 仅 v1，故不是原源隔离。PDF截图入口失败，必要正文、公式与 figure-caption 数字可读；没有视觉验收或硬件复现。

评分顺序为 Design Delta / System Reach / Durability。六分项目因具体长期缺口深入受影响内容，不因要写书而改分。全部性能数字是作者测量，不是本地复现。以下 Books 为写前建议；root 后续许可窄写后仍须非作者 POST。

## 1. SF-2026-ARXIV-2610-02522 — Beaver

**评分：2+2+2=6；标准＋sharing 边界缺口深入。** [官方 v1 PDF](https://arxiv.org/pdf/2610.02522) §4.1–4.3、§5、§6.1–6.3、§8 与必要 AppD。原证据 `dc-beaver-pdf.txt`、`dc-beaver-core.txt`、`dc-beaver-final-core.txt`。

拟采用命题：SM 分区不隔离 HBM；预创建互补 Green Context pairs 使 slot 边界只重绑后续 launch，不搬走在途 blocks。逐 vRAN block bitmap 在所需 HBM 区间置位；可获得 PTX 的协作 co-tenant 在安全 gate 前等待，不能撤回已发内存请求。SM sizer 是同质 workload 拟合后组合＋经验 tail reserve，不是 WCET。

实验：Aerial25-3，主要 H200141GB，28配置，0.5ms slot/1.5ms uplink deadline，每项50,000 slots。GC-only 与 Beaver 同 SM split，仅 guard 差异；全栈 vLLM Llama3.3-70B/Mistral24B，13 memory-heavy cells、56:76 split，p99.9 1.467/1.426ms，miss<0.1%，保留74/73%吞吐。A100/GB10/GH200跨设备使用 Llama3-8B，不能混同70B。LLM precision、batch/concurrency、生成长度与 engine revision 在采用证据中 Not Disclosed。某些动态/downlink切片零 observed miss 不授绝不miss；不证明恶意租户隔离、多 co-tenant、多GPU或不可改写 kernel。guard/profile/降速均付费；不支持或收益不足应独占/硬隔离。

Books：`PLATFORM-GPU-SCHEDULER` Ch63“GPU Sharing 的语义不同”，实际读现有154–180：已有 compute partition≠timing、PTX grid splitter、fault-domain 分责，缺的是**后续 launch 选择与在途 block 不变、HBM新traffic协作抑制和per-block clearing**。建议两段 Direct Refinement，不复制模型/论文清单，不修改 Ch49/54。邻章62/64实际读定位，不赋予请求调度或 gang owner 新责任。

## 2. SF-2026-ARXIV-2610-03088 — Coda

**评分：2+2+2=6；标准＋具体调度缺口深入。** [exact-v1 HTML](https://arxiv.org/html/2610.03088v1) §4.1–4.3、§5–7、AppA。原证据 `core-2610.03088-{a,b,c}.json`、`dc-coda-ca.json`、`dc-coda-runtime.json`、`dc-coda-profile.json`。

Logical ready 只定义 eligibility。Cstate=restore+load+prefill，按 wait-aging 降成本排序，Wmax优先的是 oldest **HBM-feasible**；实现 bounded frontier最多64，不是所有 request 的硬等待上限。工具执行时间不计 ready-wait。Prototype/evaluation 未配置SSD，Tload=0；不能声称SSD tier收益已测。Context-aware attention 在**同一已参与集合**内按 materialized length 切cohort，KV更新与dense/MoE遍历仍一次，只增加 attention launches；成本模型、额外launch allowance、held-out residual与最低收益 gate决定是否拆，unsupported/out-of-domain回退整批。不是替换continuous batching，也不是cohort提前交付token。

实验：Qwen3-Coder-30B-A3B-FP8单GPU replica、Qwen3-235B-A22B-FP8八GPU replica；1/4/16 A10080GB配置，TraceLab Q1/2/3到达3/5/7req/s，比较CacheWise、SMetric、vLLM。30B对最强基线output throughput +4.2–12.1%，SLO throughput +15.9–44.3%，但采用切片未披露具体SLO thresholds/backend revision，故不以此定义生产承诺。Table1 M1 TA-only SLO throughput 12.788→12.370退步，full CA13.917；vLLM Q3p95TBT反增6.1%，SMetric Q2/Q3更低TBT但更低并发/吞吐。Profiles绑定模型/GPU/KV/topology/engine，变化需重校；split/fragmentation/CPU-shadow拷贝和预测误差付费。

Books：`INFER-SCHEDULING` Ch56实际读414–428 length/prefix regrouping，1428+workflow release与pinning，59+SLO admission。差额是**不改请求集合而仅拆attention execution、额外launch保守收益gate，以及ready state-prep/HBM-feasible frontier**；现有aging与cache routing不重复。建议放prefix-length小节两段；A/F topology责任仍Ch55。

## 3. SF-2026-ARXIV-2610-03203 — AFORE

**评分：2+2+2=6；标准＋exact demand/lookahead缺口深入。** [exact-v1 HTML](https://arxiv.org/html/2610.03203v1) §3、§5.1–5.2、§6、§7。原证据 `core-2610.03203-{a,b,c,d}.json`。

AFD中当前真实gate/top-k可早于FFN执行取得，demand prefetch不是未来router预测。按tile而非token数估makespan；显露migration代价=max(0,copy duration−available window)，净收益>0才安装replica。固定primary、reservedslots和上一target activeweights保护；host mailbox/ring plan绑定step/layer/microbatch/source，all readers取完才复用，stale/out-of-order拒绝，target compute等copyevent。原top-k occurrence按不交叠区间分配后还原原组合weights，不是改router语义或所有移动态保证fullyhidden。

实验：GLM4.5Air110B，2节点×8A100；intra300GB/s、inter50GB/s/bond；ShareGPT/FineWeb/CodeForces/GSM8K，同AFD runtime/allocation/batch/layout比较Static、EPLB、HarMoEny、Lina、Libra。对最强基线 output +10.1–17.6%、P95ITL−7.1–9.5%；具体precision/batch sizes采用证据未披露，不补写。no-prefetch/no-overlap消融支持本实现相应收益。324迁移target样本 exposed=0，copy均值.453–.495ms、window2.008–2.119ms，不证明任意动态负载零暴露。EP128 planner245.81us来自200target回放，不是128GPU端到端。Mailbox、计数传播、replica容量、copy与dispatch争用付费。

Books：`INFER-SCHEDULING` Ch56实际读523–602，已有“预测性working-set control”与predictor/planner/epoch、window约束。Ch55 205–305已具conditional A/F topology。新差额仅**真实早到router demand与预测信号分开、tile净收益减exposedcopy、计划身份/reader与activeweights/copyevent否决**；建议接预测性分支，不另建AFD论文节。

## 4. SF-2026-ARXIV-2610-03286 — VenusRL

**评分：2+3+2=7；深入。** [exact-v1 HTML](https://arxiv.org/html/2610.03286v1) §3、§4.1–4.3、§5.1–5.2、§6.1–6.4。原证据 `core-2610.03286-{a,b,c}.json`、`dc-venus-ablation.json`。

完整group由最慢trajectory决定可消费时点，优化下一B个group ready而非单独GPUutil；length predictor只是heuristic。一个priority跨framework slots、prefill-token admission、decode retraction、trajectory级KV refs和request orchestration；引用在trajectory结束而非turn结束释放。Admission与eviction消费同scheduler-iteration原子snapshot；高priority容量不足时controlled demotion保护剩余residency。最后valid weight version升最高priority，是受限调度规则，不采用“任意任务无偏/不discard”保证。环境manager按active growth+template coldstart reserve提高admission，仍有OOM后pause/migrate；group-template page pool只共享immutable页、写入private CoW，不是安全认证。

实验：4server32Hopper（16rollout/16train）、180CPUcore/1.8TB pernode、900GB/sNVLink/400Gb/sIB；Qwen3-4B/32B、OpenSWE45,320 Docker environments、GRPO group8/temp.7、128K output/300turn cap、weight-version threshold2、SGLang0.5.17、HiCache。Slime/RollFlash/ThunderAgent框架及算法参数一致；speedup范围1.05–4.24依baseline/config而变，bs16 async1.5/2只有1.06–1.17。Reward曲线仅bs32 async1.5代表设置，version heatmap100steps Qwen4B，不能授所有设置质量等价。400GB environment node native100→placement743→sharing905；905是native的9.05倍，不重复正文“905%”为提高905%。Lifecycle Pause在256 sandbox19.2→24.8s、Resume4.9→6.2s，不能全称negligible。OOM实例迁移2.70s vsnative3.68s，有暂停与预测误差成本；不采用89%成本普遍降本。

Books：`TRAIN-GRPO` Ch33实际读1260–1370：已有group完整性、提前梯度而非commit、version window与staleness invariant。缺口是**下一完整group-batch criticalpath目标以及priority跨slot/token/KV snapshot的一致执行**，不是再解释异步或GRPO。建议两段紧接rollout-service开头；environment dense placement仅在局限反侧作实例，不扩平台/安全章。Ch32/34邻接需写前重读定位。

## 5. SF-2026-ARXIV-2610-03394 — EdgeAgent

**评分：2+2+2=6；标准；仅报告。** [exact-v1 HTML](https://arxiv.org/html/2610.03394v1) §3.1–3.2、§4.1–4.5、§5generalizability。原证据 `core-2610.03394-{a,b,c}.json`、`dc-edge-counter.json`。

UMA共享output disjoint columns＋logical DAG barrier等both producers，不以共享地址取消completion；CPU SME packing与GPUlinear weights加载时定分片。固定hardware-aligned总16draftslots，以HAL accepted **count** EMA而非acceptance ratio分残余budget，先保Lmin，要求N×Lmin≤16；这个有限公式不授未测并发、硬公平等待界或最优。Toolstall只在verification boundary suspend/yield，KV metadata留原UMA，不能把“不重新prefill”称全部零成本或任意离散GPU免搬运。

实验：M4 32GB/120GB/s、10CPU/10GPU，部分M4Pro64GB/273GB/s、14CPU/20GPU；DeepSeek-R1-Distill-Llama8B/Llama3.1-8B FP16/EAGLE3，N2–4。Trace synthesizer混LongBench/MBPP/ToolBench 1:2:2、Poisson arrivals、synthetic log-uniform工具暂停；peak throughput取消arrival delays。GPU-only Batch-SD每request固定L16，不与全系统16pool当“相同budget”笼统比较。UMA层1.29×；HAL比对应UMA配置额外1.05–1.17×；最大1.77×是N4模拟1–100s tool stalls（213.1→120.6s）。Packing13–16s包含makespan、kernel峰值另排packing。无任务质量/随机sampling law等价验收，portability段是推论非离散GPU实測。

Books：实际读 `INFER-SPECULATIVE-DECODING` Ch48 218–266（accepted progress/verification cost/opportunity cost、calibration、packed controller与target commit）；Ch54 UMA容量与同步段仅作旁证。HAL+16slot+UMA是具体实例，不代表exact HAL已有覆盖；本次没有需要修正的长期判断，**仅报告，不强行新增HAL规则或论文清单**。

## 6. SF-2026-ARXIV-2610-03415 — RailWave

**评分：2+2+2=6；标准＋physical execution缺口深入。** [exact-v1 HTML](https://arxiv.org/html/2610.03415v1) §2.1–3.3、§4、AppA.1/A.3/A.4/A.5必要切片。原证据 `core-2610.03415-{a,b}.json`、`dc-rail-config.json`、`dc-rail-overhead.json`。

固定logical D/token→expert后，source-localRailBalance按eligibleRails重分owner→proxy，rail-symmetric bijection条件下平衡**单source贡献**，不授全局ingress均等。Cyclic waves每node至多一个incoming/outgoing peer，完整覆盖orderedpair，控制receiver incast但增加serializedwaves。选路按payload/railskew/receiverconcentration，near frozen calibratedanchor才用替代，其他Joint；Joint不是永不退步。所有rank共同path/wave且dispatch–combine pair固定plan，combine按savedmetadata返回原token，不改placement/router。

实验：各4node32H800/H20、NVLink、RDMA200Gb/sports，DeepEP2.1.0，129GINcontexts/16commSM；physicalfabric type NotRecorded。BF16 hidden7168，GLM4.5Air106B training DAPO-Math routingrecords/45layers、controlled Ring/Moderate/Extreme replay。5.84×H800/4.36×H20是GPU-event dispatch–combine区间，不含CPUplanning/index/prepacking，也非整训练step；图sum每layer相应quantile不等整step tail quantile。Frozenanchors12unseen requests只4switch、其余Joint；1.061–1.196×只switch分母，fallback独立measurement差异是noise不selectorgain。Packing额外Sequential→Pipelined降低2.87–3.68%，仍付费；配置workspace约4.11GiB/GPU。稳定低incast/smallpayload时轻路径可能更好，未知topology需重校。

Books：`TRAIN-DISTRIBUTED-TRAINING` Ch36实际读282–305relay/capacity与650–684dispatch semantic；已有“placement不独保rail”却缺**空间balance与同时receiver入流degree两个控制维度**。建议接295+relay分支两段，明确fixedD、bijective条件、singlecontribution非全局均等与serializedcost。不是接入新EP库或改Ch37分片。

## 7. SF-2026-ARXIV-2610-03457 — Cross-Facility

**评分：2+3+2=7；深入。** [exact-v1 HTML](https://arxiv.org/html/2610.03457v1) §3.1–3.3、§4Tables1–4、§5Limitations。原证据 `core-2610.03457-{a,b}.json`。

Elastic token-weightedNesterov outer update拒绝stale merge-round delta，singlecontributor用fullstep；globalstep=maxcontributorsteps不等实际总tokens。DARL中心authority账本unassigned/leased/committed，同N/K/seed digest、global blockshuffle、按实际commitrate分lease，heartbeatTTL回收untouched/inflightlease，checkpoint在blockcommit之前。该ordering与有限ledger支持受限coverage，**不授controlserver宕机、networkpartition、durability/原子故障或任意exactly-once**。Slurm test-only probes+realized-walltime discount+probeage决定建议submissions；迟开job未lease数据、running jobs不受replan干扰，不把队列prediction当reservation。

实验：真实Snellius H100/LUMI与Frontier MI250X，Qwen3-0.6B/C4，20,000steps；BF16 WAN消息1.32GiB，three-site heldoutPPL34.7 vscentral28.2（centralhigherLR24.5），two-site37.5且19h48 vscentral5h41。单model/singleepoch/topology、无downstreambenchmark。H1000round1774.2scompute/107sother overhead（5.7%），不等所有质量代价消失。23.8hledger2070granted/2045committed/25returned/fourdepartures＝1.2%reclaimed，sumcounts不单独证明no twice-trained。Table4是100B规划scenario，明确0%barrier/no-requeuegap且placeholders参数仍在方法中，不作真实wallclock speedup。HTTPblob161.8s vsgrpc176s是本实现tensor serialization，不是通用HTTP比gRPC快。

Books：`TRAIN-DISTRIBUTED-TRAINING` Ch36实际读1420–1475跨地域/quorum、950–1015故障恢复与data cursor；旧正文已有revision/aggregation/checkpoint责任，但缺**membership弹性不能替代epoch data-coverage lease ledger、checkpoint-before-consumptioncommit和迟开job只在启动后lease**。建议在跨站聚合段两段；Ch35保留持久恢复owner，queueprojection不作为scheduler生产证据。Ch35/37邻接需写前定位。

## 作者处置与交接

七项均达到上述采用范围的必要原源审阅，无普通pending或外部原源隔离。Books建议为六项窄机制整合＋EdgeAgent仅报告；最终写入状态以实际patch/root POST为准。共同current-history无修订轻量核已完成；没有读取其他日期候选/旧Weekly，没有扩检core池、全附录或旧版本比较。

root授权在本文件保存后窄写 Ch56/33/36/63；写后再更新以下状态，不自行写“root通过”：

`Books writeback: root 授权范围内六项窄机制已写 Ch56/33/36/63；non-author POST: root 已实际核六处正文/相邻段及必要原源，通过，四章锁已释放。` 该项确认来自 root 的实际复核回执，不授 runtime/exactly-once/硬deadline，也不代替 Daily 总 Gate。作者仅写正文机制＋相邻反侧/来源 binding，不改 LS/index/正式日报或分支/暂存/提交。
