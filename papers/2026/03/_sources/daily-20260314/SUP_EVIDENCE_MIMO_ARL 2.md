# MiMo ARL-Tangram 必要 Source / actual owner PRE

作者 mar14_supplement。官方 [March13原页](https://mimo.xiaomi.com/paper/arl-tangram) 完整题摘、12作者和linked `/papers/arl-tangram.pdf` 已核；`SUP_PDF_MIMO_ARL.raw` 精确25页官方稿，首标题/作者与原页同稿，PDF自身为13019v1。日级官方日期按新增Mar13自然日合同由root独核通过，不请求小时，较晚arXiv不覆盖作者先公开。实际读§2.4、§3–6完整必要机制/配置/评价/反侧、Alg1与AppendixA目标近似；p17完整图9/Table1视觉核验。未读全附录拓扑DP/proofs、代码或复现。

## 准入 / 评分

长存活trajectory/task预留工具环境和reward服务导致空闲资源→action-level pooled allocation但长期状态保留，并按单key elasticity/profile做近似ACT调度→需要把外部CPU/GPU/API资源租约与environment/service identity分开验收，不能仅加rollout generation并行。2+2+2=6最低标准；Ch33实际状态/资源释放差额必要深入，不将成熟FCFS、DP、cgroup或LRU原则重复计高分。

## 必要机制和不采用

§3–4：tool/reward原子调用一action，vector包含CPU/GPU/内存/APIquota，legal resource ranges可离散；只假定一个key resource控制elasticity，Tori/E(m)m需profile。FCFS避免starvation作为选择，不是总ACT全局最优；min资源可容纳prefix按key split，greedy evict末项、候选topologyDP、剩余completion heap近似(depth2/3)，unknown/non-scalable取min。实际目标是queue+exec之和，不是RL完整group-ready、trainer-tail或质量。AppendixA文字/伪码只支持其近似思路，未核为可执行无bug配方；不采用全局最优/公平或精确极短action保证。

§5：CPU AOE每docker.exec前调cgroup/cpuset，进程终结回收CPU但容器mem长期保留，同trajectory固定node/NUMA倾向，core独占；资源调整本身不让串行任务自动parallel，作者修改pytest命令仍需test执行语义等价检查。GPU EOE初始化每legal DoP服务的CPU invariant copy；resident缓存或evict/restore后执行，动作结束不立即卸载；at-most-one action/GPU，但服务可多缓存。**evict不回写依赖服务state跨调用不变**，不能外推有变状态/所有环境；distinctDoP当distinctservice，cell/chunk和LRU是拓扑/缓存选择而非生产隔离认证。quota/concurrency manager分别核限制，不能用GPU利用率替API许可。

§6.1–6.4：RL up to48×8 Hopper、VeRL异步/sequence rollout；外部CPU15×256 AMD+2.4TB、GPU5×8未指型号high-end GPU+3TB hostRAM，资源可缩slice。coding、MOPD、DeepSearch批1280/2048/2048，Qwen3-32B/MiMoV2Flash具体每workload映射/precision/token lengths未充分给；proprietarySWEBench scaffold/BrowserComp与GPTOSS judge、9teacher固定4TP或5×8rewardbaseline，API最多3retry/600s。平均十steps1.4/1.5倍只限两workload；MOPD完整step受最长trajectory支配，ACT降低不等完整RLstep同倍。

low concurrency SGLang略低latency，单DeepSearch reward restore使其稍慢；同batch1024可10reward仅29%baselineGPU保持同ACT并不是全平台费率/所有任务71.2%。CPU1536使K8s控制面timeout，超大倍率含baseline过载；768cores更少multiplex机会。fixedDoP trace消融控制elasticallocation局部，不隔离全部实现/流量语义。Table1视觉核：GPU sys .201/.240 对 exec .621/.705，约32%/34%，**正文“约25% execution”分母不一致**，不照录该比例；对完整queue+exec+sys的2048 case约22%，3072 dominatedqueue15.05。restore overhead确实不可忽略。重复seed/CI、quality-preserving训练结果、onlineSLO/独立租户安全与故障恢复未披露/未核；厂商已部署是其事实声明，非我们的生产验收。

## 具体 owner 与拟两段

唯一owner `TRAIN-GRPO` Ch33。实际读完整1373–1391 rollout服务化局部（generation资源预测/迁移、完整group ready/Venus、同步梯度重叠、环境历史身份），Ch31 62–84 cluster-level orchestrator概要及Ch32入口。Ch31跨任务控制面不等action-specific状态/资源释放，Ch36通信/训练native work不是该外部调用接口。既有Ch33 action-level措辞只作generation重叠，不承载CPU保mem/GPU invariant-copy及elasticprofile边界，具体缺口。拟在“Rollout变成服务”首段之后、同步rollout长度历史之前两段；共享Books未写，交root独核后窄写：

外部工具与 reward 服务还会把“保留环境状态”误做成“整条 trajectory 持续占住执行资源”。可将一次不可交错的工具或评分调用定义为 action，分别声明 CPU/GPU/内存、并发或周期 quota 的约束，再让长期 environment/service identity 与短期执行租约分离：CPU 动作结束释放执行 cores，却保留容器内存和同轨迹所在节点；GPU 服务按可用并行度恢复或复用缓存，结束后可继续驻留，只在需要空间时驱逐。GPU 驱逐不回写只在服务状态跨调用不变、有可信 host copy 时成立，不能把有状态工具一律当可丢弃推理实例。<!-- source-family:SF-2026-MIMO-ARL-TANGRAM -->

[受限行动级资源对照](https://mimo.xiaomi.com/papers/arl-tangram.pdf)再以预先 profile 的单一主要弹性资源估计时长，按合法资源范围、FCFS 与近似排队/执行完成时间选择并行度；这是有成本的调度 heuristic，不是全局最优或完整训练更新更早就绪的保证。内存驻留、CPU 配额/并行测试语义、GPU restore/拓扑缓存及 API 限额都需分别验收；平均调用更快仍可被最长 trajectory 支配，低并发或单服务也可能因 restore 更慢。保持 policy/group admission 与训练质量独立，profile 漂移、可变服务状态、预算或可靠性未通过时，回退固定并行度、静态预留与已验收环境，而不由平均 ACT 或资源节省批准训练分布和生产 SLO。

待root实际Source/PRE独核后才写；尚未POST/DAY，不因准备好等待无关来源。
