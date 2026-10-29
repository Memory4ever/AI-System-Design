# arXiv — Live Daily 2026-10-24

窗口：2026-10-23 BJT。仅本文件与本批必要原件由 oct24_arxiv 写入；Report/Books/State 由 root 负责。

状态：来源与贡献筛选已收敛，完整题摘31家族、拟入30家族（29个v1+ATTUNE v2重要修订）、最终排除1；本代理23份Source-ready，另7篇由oct24_org负责；必要证据独立复核及Report/Books由reader/root继续。

## 2610.17528v2 ATTUNE — Source-ready（重要修订）

[HTML](https://arxiv.org/html/2610.17528v2)只读当前v2新增评价、§2.2.4/§3.1–3.2/§3.5/§4/§6.1–6.3，不做旧新全文比较。v2官方声明新增AutoModel/production/OpenRecipes，本窗不是v1首次公开；不重复家族评分。增量评价说明：四AutoModel recipes在同厂framework/container/H100复现（其中三within2%、Llama70B within8%published），再调优后对本地baseline+7–26%、对另机器/版本published+6–17%，两者勿混。此组1campaign、Opus5.5/web enabled、不同budget、无final remeasurement；不能与ported组3campaign、Opus4.8/web disabled/sandbox/broker、30×baseline-run GPUh budget、14step取4–13及final interleaved测量拼成统一随机实验。部分AutoModel模型曾参与开发，不是held-out generalization。

§6.1生产SFT三model跨H100/H200/B200，作者报65%jobs采用、平均1.7x；是厂商deployment observation非本地核验。OpenRecipes >60recipes/>20models为author catalogue，loss-curve check较严格，但不能证明任意新模型收敛。正文gate外置配置registry分known-invalid/valid/unknown，first-step loss parity；会放过只在optimizer update生效的fault和shifted mask，unknown flag需review，§6.3仍要求full training前置验证。因此采用“自动配置优化的速度必须绑定objective-equivalence与gate覆盖层级，benchmark收益由起始recipe与stack决定”，不采用“无人监督即可生产安全发布”。具体旧Books差异由root核；拟owner TRAIN-DISTRIBUTED-TRAINING。

## 发现收敛与明确分母

日期规则补核：已打开[arXiv官方availability](https://info.arxiv.org/help/availability.html)§Announcement Schedule及ID assignments；Thursday20:00 Eastern公告→Friday日列表，2026-10-22在America/New_York夏令时，日期换算落BJT10-23。Oct23官方new列表已实际出现具名ID，不是只拿提交+日程推“已经公开”；ID不可回溯月份也解释了8/9月提交但10月公告，非矛盾。这里保留官方日列表日期，未把日程推断改名为每篇实际发布时间。

本轮有界主题/同义查询及12分类2026-10-23官方日列表相关标题导航已停止；不建立整类题摘逐项关闭队列。完整题摘贡献判断共31个唯一家族：29个v1首次公告拟入家族、1个v2重要修订ATTUNE（同家族不重复评分）、1个最终排除MCPvsCLI。拟入/审阅分母30家族，其中我负责23份必要证据（前22+ATTUNE）均Source-ready，另7篇World/Action证据由oct24_org维护[SOURCE_WORLD_ACTION.md](./SOURCE_WORLD_ACTION.md)。这不是全学科召回计数，也不是把日列表183/339等条目数相加。

代表性title-only范围排除（不把标题不明者算已读题摘）：30170 wildfire hazard surrogate（领域应用/暂缓science）、30207 EEG inverse source（领域成像）、30180 protein-function retrieval（暂缓science）、31523 prostate MRI synthesis（领域医学）、30409 Cambium general commitment/BFT infrastructure（无明确模型系统机制连接）、31203 sparse graph domination（通用分布式图算法）、31201 reversible language L4（通用可逆编译非模型执行）、30469 urban mobility incentive（领域交通）。这些条目无需为不影响贡献处置的日期另建恢复请求，不计31题摘分母。

列表navigation可见的其余replacement若仅题名/版本变化且无明确重要修改说明，不当新候选；唯一明确触发ATTUNE已核。当前abs轻量撤回/撤稿检查已做，未发现影响本轮采用的withdrawn/retracted标记；不声称全版本历史无纠错。必要HTML可得；Apple HTML404通过官方PDF恢复。无因访问失败被删去的已准入候选；无本代理尚未读完的必要Source普通待办。Report/Books/independent review仍由root/reader完成，此“Source-ready”不等于DAY完成。


## 证据审阅批A（标准审阅完成；待独立证据复核）

### 2610.30206v1 MoEZip — Source-ready

原文：[HTML](https://arxiv.org/html/2610.30206v1)，已读§2–4.4与§6，采用命题只到“MoE prefix KV选择可同时保护上下文显著性与路由稳定”；不采用完整因果/通用最优保证。§3使用instruction-token router Fisher trace作为未来answer routing的方向无关proxy，softmax为1−Σg²；局部KL推导要求小、零均值、各向同性logit扰动，不等于任意KV删除定理。按instruction-to-context attention分配anchor，其余预算由KVZip/SnapKV填满，总KV量不变。

§4.1控制checkpoints、模板、decode、retention 0.1–0.9；Qwen3-30B-A3B-Instruct与GLM-4.7-Flash，LongBench12任务、RULER、4K–32K NIAH。关键反侧是query conditioning：§4.3 Table1同reconstruction query的可复用MoEZip-Recon在keep0.1为41.95、KVZip19.51，instruction-conditioned44.89但失去跨请求cache复用，故不能把全部收益归因routing。§4.4固定retained cache仅恢复instruction-routing，KVZip LongBench19.5→29.7但仍未达full53.7，证明路由只是部分损失来源。Fisher/anchor分配消融支持组件价值；黑盒API未暴露router与attention时不可直接实施。本档只采用质量/预算取舍，不宣称吞吐改进；硬件、batch、并发、SLO未用于此命题，Not Applicable；未执行代码或复现。评分2+2+2=6不变；拟owner INFER-KV-CACHE，Books由root核实际覆盖。

### 2610.30161v1 TauIndianBankBench — Source-ready

[HTML](https://arxiv.org/html/2610.30161v1)已读§2–6与Limitations。采用命题：数据库终态等价不足保证必要read/过程与“曾经非法写后恢复”的行为合规。§3.2将gold-chain required reads与write purity加在既有action matching上；动作检查为required-call集合匹配而非通用严格时序证明（同gold-call重复由一次匹配满足，实际顺序更多依赖参数依赖与模拟客户按步骤提问）；因此只能说明两类oracle互补，不能声称完整程序安全验证。

§4–5在同一recorded session上重评分隔离评分规则混杂：1000 synthetic English Indian retail-bank任务、50 families、assistant六模型，MiniMax-M2.7 customer温度0，最多200步/10失败tool；base单次，部分Gemma重复。final-only多接受65–120/1000会话（6.5–12pp），action-only也会漏终态错误。Table2/McNemar不是所有模型同向显著；在12B/E4B两个rule分歧数不显著。§3.2 600会话独立scorer一致，验证实现一致非用户模拟真实性；局限明确customer错误率未测、synthetic分布/单语言/单领域。用作评估设计反例而非bank部署ready。性能硬件/batch/SLO不适用，无runtime速度主张；未运行harness。2+2+2=6，拟owner PLATFORM-EVALUATION-SYSTEM。



### 2610.30154v1 baseVultra — Source-ready

[HTML](https://arxiv.org/html/2610.30154v1)已读§2与§3.3–3.6、结论。单dense candidate+diagonal gates+低秩辅助分支是预算重分配；消融Table5/6显示低秩分支主导收益，h(t−2)/EMA增益小于或接近seed波动，不能宣传二阶记忆为主因。TinyShakespeare三seed、formal H16三seed对比支持小容量选择，H32多数饱和；text8 Table2单run30epoch参数匹配约190K尚未收敛，baseVultra1.854bpc落后LSTM1.837/GRU1.849。效率仅matched-H dense recurrent FLOPs；实际实现比cuDNN慢3–6倍（per-step launch），不是wall-time加速。没有long-document LM或大规模foundation结论。不为数字采用补硬件附件；这里只采用capacity边界，性能部署命题不采用；未复现。评分2+1+2=5，MODEL-LONG-CONTEXT。

### 2610.30552v1 Repair Changes Which Layers to Remove — Source-ready

[HTML](https://arxiv.org/html/2610.30552v1)已读§3–7与Limitations。removed contiguous run用同least-squares map修复，选择应最小化repair后的残差/目标，而非intact cosine；二阶Fisher是对repair残差加权，非全新普遍压缩定理。exact枚举只在双层group最多删6组、单层最多3层；更重预算是启发式互比，不是53K覆盖任意网络全局最优。§7.1五model含Qwen3.8-27B held out，BF16单48GB GPU（27B双卡）、25/37.5%剪层、相同WikiText2 calibration和same repair，task objective另同task training文本；精度表同预算可比，但更低PPL不保证任务最好（14例中4例别subset高2–7pp）。只测一种repair、English/multiple choice，更新repair或目标须重选；未用吞吐数字或复现代码。2+1+2=5，INFER-TENSORRT-LLM。

### 2610.30151v1 Handshake overhead — Source-ready

[HTML](https://arxiv.org/html/2610.30151v1)已读§3–4.5、§5与§7（针对RTT/metadata命题）。官方SDK minimal echo server，host+client+relay均Apple silicon loopback，Python3.12.13、mcp2.0.0、a2a-sdk1.1.2、acp-sdk1.0.3；每cell50次discard5 warmup，cold RTT sweep20。relay按应用chunk双向各25ms，而非真实packet/transport RTT；不含TCP/TLS建立，SSE双chunk多付延迟，不能把230ms/61ms当普遍网络延迟。anonymous配置、单能力toy server；warm MCP特设1h public TTL（默认non-cacheable），0RTT要求era pinning+cached metadata；不是任意服务自动免费重连。token是o200k_base假想LLM reader线性成本估算非实际任务调用。官方[2026-07-28规范](https://modelcontextprotocol.io/specification/2026-07-28)确有stateless/per-request negotiation，但paper各SDK实现数字仍仅author measurement；本次不称独立复现。2+2+2=6，AGENT-MCP；采用分解方法和配置依赖，不保protocol绝对排名。

### 2610.30157v1 MCP vs CLI — 最终排除，强设计反证已定点检查

[HTML](https://arxiv.org/html/2610.30157v1)§III-A明确假设CLI=unrestricted host shell，MCP=properly configured server；§VII把CLI风险写architectural、MCP写operational，未在同权限/容器边界下比较。无sandbox变量对照，worked examples/表格token区间/经济模型不能支持“CLI根本无法权限隔离”；官方[MCP安全说明](https://modelcontextprotocol.io/specification/2026-07-28)也明确协议自身不能enforce安全原则，需实现access control。该观点不构成可归因的新安全机制/边界证据，保持排除、不评分、不进入Books。不是将安全反证静默漏审。

### 2610.30868v1 uGDS — Source-ready

[HTML](https://arxiv.org/html/2610.30868v1)已读§2.1–2.6/§3.3–3.4/§4–5。host持有NVMe controller队列、GPU buffer映射、in-flight refcount，DMA完成前不可释放；kernel仅setup/eventfd通知，非GPU kernel执行NVMe控制。独占unbind NVMe native driver、raw namespace/LBA接口非透明共享filesystem；跨NVMe/RDMA同步仍由application barriers负责。当前单local SSD；multi-SSD/NVMe-oF/occupancy-aware及ordering-aware scheduler是计划，不是现有能力。

§4.3揭示headline batch倍数含GDS首batch deferred setup；128KiB batch128稳态排首批后仅读1.74x/写1.28x，不能用30.69x代表大IO稳态。§4.6端到端A100-SXM4-40GB+990PRO/cross-root P2P、Qwen3-0.6B、vLLM0.20.1+cu129/LMCache0.5.1.dev35、SSD-only hits、禁vLLM APC；32K prompt medianTTFT1915→715ms和1K prompts concurrency1–256只说明此storage-hit workload。goodput是logical KV throughput无TTFT/TPOT SLO定义，不能当SLO-goodput。GDS16stream可部分缓解single-stream调度开销。§4.2 IOMMU disabled的microbench；exclusive设备/CPU轮询与安全隔离不是免费收益。未跑代码。代码PR历史早于paper（参考§27指Aug18 merged），不可称首次公开实现为10-23，但当前paper新证据属于本日公告。2+2+2=6，INFER-GPU-MEMORY。

### 2610.31479v1 Apple Silicon — Source-ready

[PDF](https://arxiv.org/pdf/2610.31479v1)已按PDF技能读§2.1–2.2/Appendix A.1–A.2与§3限制，HTML404后PDF可恢复，非外部阻塞。采用“speculation盈亏属于method/runtime/hardware/workload组合”，不是Apple上必然无效。主比较M2Pro/M3Ultra、MLX Qwen3-4B 4bit/BF16，100chat/tool prompts，mean1776输入/54–62输出、greedy/max512、batch=concurrency=1、warmup1+3测量；每adaptation各自AR baseline，绝对跨方法吞吐不可比。所有主比较E2E为负，BF16 Classic有+1.1% decode但−13.8%E2E；Appendix设置EAGLE3为单draft token/4bit head、Cascade只vertical，不等同论文最强配置。§2.2.3 Table2给M3Pro BF16 DFlash/DDTree分别+9.2%/+15.5%E2E，明确反驳“所有Apple组合都减速”。§2.2.2说明没matched backend ablation/kernel profiling，不能把Apple vs A100差距仅归硬件。KV剪枝没task-quality评测，不能把内存/时间节约当无损；public Metal async-copy是API gap非silicon不存在。未复现，未采用跨配置统一加速倍数或生产SLO保证。2+2+2=6，INFER-SPECULATIVE-DECODING。


## 有界补检与修订尾批（初筛时记录；当前审阅状态以上方证据段及REVIEW为准）

### [2610.30197 — Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation](https://arxiv.org/abs/2610.30197)

Submission history From: Jona Joy [view email] [v1] Wed, 21 Oct 2026 07:06:59 UTC (2,120 KB)。官方2026-10-23 new列表：前两cs.RO new，ATTUNE cs.DC replacement；BJT公开门为10-23。无撤回提示。

Abstract:Large language models (LLMs) are increasingly integrated into embodied robotic planning, yet standard benchmarks primarily evaluate end-to-end task completion in nominal environments, obscuring failure origins across the execution stack. We present Alpha, a systematic fault-injection and robustness-evaluation framework for LLM-driven manipulation in simulation. Alpha injects calibrated faults across perception (sensor lag), actuation (grip slip), kinematics (unreachable targets), and planning (planner-output corruption), alongside concurrent conditions. To separate physical vulnerabilities from planner sensitivities, we introduce a matched methodology pairing an LLM agent (Llama-3 via Ollama) against a deterministic Scripted Oracle planner across a balanced 150-episode matrix under identical seeds, geometries, and safety criteria. Across the matrix, the Oracle achieves 64.0% (48/75) success while the LLM achieves 44.0% (33/75) (paired McNemar p = 3.01 x 10^-4). Crucially, excluding planner-output corruption, performance across all physical and kinematic conditions is identical: 55.0% (33/60) for both planners with zero discordant pairs (McNemar p = 1.00). This demonstrates that physical actuator slip, kinematic reach boundaries, and perceptual staleness affect deterministic controllers and LLM planners equivalently. The performance gap is driven entirely by planner-output corruption (100% Oracle vs. 0% LLM), isolating the prompt-to-JSON serialization and validation interface rather than a cognitive reasoning deficit. We also audit 169 historical pilot attempts for transparency.

拟入2+1+2=5：matched oracle/LLM故障注入把物理扰动与planner-output corruption分离，改变cognitive failure归因；owner MULTIMODAL-EMBODIED-VLA；此处仅保留初筛拟判断，当前准入与审阅状态见REVIEW。

### [2610.30319 — TerraTransfer++: Demonstration-Free End-to-End Planner](https://arxiv.org/abs/2610.30319)

Submission history From: Zikang Xiong [view email] [v1] Wed, 21 Oct 2026 18:31:28 UTC (1,860 KB)。官方2026-10-23 new列表：前两cs.RO new，ATTUNE cs.DC replacement；BJT公开门为10-23。无撤回提示。

Abstract:End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all existing paradigms: imitation learning requires fleet-scale driving logs whose behavior distribution only thinly covers the safety-critical tail; closed-loop reinforcement learning in a photorealistic simulator, while offering diverse behaviors, is bottlenecked by sample-efficiency, per-step cost of rendering, and a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: at millions of rollout steps per second, one can obtain a state distribution with natural diversity in collisions, near-misses, and recoveries that no driving log contains, and a highly reactive policy emerges from a basic driving-quality reward. Our approach exploits this asymmetry. We pretrain a single policy by self-play, distill its rollouts into a flow-matching trajectory teacher that also plans, and train lightweight adapters on a frozen pretrained vision backbone to reproduce the latent space of either teacher through the action KL divergence, a batch-relational low-rank structural loss, and, for the planner, a trajectory-matching loss. Every target traces back to the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. From this one self-play teacher we obtain two end-to-end students: a closed-loop policy that outperforms every published imitation-based end-to-end method on the photorealistic 3D Gaussian splatting closed-loop benchmark HUGSim, and a planner that reaches 59.4 EPDMS on NAVSIM navhard, above every published method including DriveZero-Scale (57.1), and 95.5 PDMS on navtest, without human demonstrations.

拟入2+1+2=5：selfplay教师经flow trajectory与action KL/关系结构对齐frozen vision学生，以paired image/state替代expert trajectories；owner MULTIMODAL-EMBODIED-VLA；此处仅保留初筛拟判断，当前准入与审阅状态见REVIEW。

### [2610.17528 — ATTUNE: Agentic Throughput Tuning for LLM Training](https://arxiv.org/abs/2610.17528)

Submission history From: Leo Fan [view email] [v1] Tue, 13 Oct 2026 00:49:11 UTC (157 KB) [v2] Thu, 22 Oct 2026 17:55:03 UTC (158 KB)。官方2026-10-23 new列表：前两cs.RO new，ATTUNE cs.DC replacement；BJT公开门为10-23。无撤回提示。

Abstract:The throughput of an LLM training job depends on its recipe: how the model is split across GPUs, how memory is traded for compute, and which kernels and communication overlaps it uses. The best recipe changes with every model, accelerator and framework version. Automated tuners search a fixed space of knobs and check only that a job runs, so they miss levers outside that space and can ship a configuration that silently changes training. ATTUNE is a coding agent that tunes any working recipe unattended within a GPU-hour budget. Guided by a skill of search rules, scripts and lessons from past tuning campaigns, it diagnoses each run and changes one lever at a time. A correctness gate outside the agent refuses any argument known to change the training objective. ATTUNE tunes Amazon's production post-training recipes on H100, H200 and B200 clusters, raising throughput by 1.7x on average. It beats the published throughput of four of NVIDIA's own benchmark recipes on NVIDIA's AutoModel framework by 6-17%. On models held out from its development, it improves the strongest public recipes most where they were written for another setting, by up to 2.6x on MiniMax-M2, and least where the vendor tuned them for the same hardware. Given the same GPU-hour budget, it outperforms existing automated tuners, including Bayesian optimization, random search and OptiCo, a recent LLM-agent tuner. Its gain on GLM-4.5 is more than four times the best alternative's. The same coding agent without ATTUNE's skill gains less and fails half its launches. We release ATTUNE at this https URL and OpenRecipes, a leaderboard of tuned and verified training recipes, at this https URL.

拟入重要修订v2：官方comments明确新增AutoModel benchmark/production/OpenRecipes，非只版本号；初筛计划只审当前v2新增评价/正确性边界、不重读v1；该必要审阅已完成，当前结论见上方Source-ready段。指定10-14报告及source定点查17528/ATTUNE无命中；无已处理同事件证据。不重复家族评分；本窗修订新评价拟owner TRAIN-DISTRIBUTED-TRAINING。



## 证据批B：cache（标准完成，待独立复核）

### 2610.30791v1 Gandalf — Source-ready

[HTML](https://arxiv.org/html/2610.30791v1)方法与§5.1–5.8：hybrid模型full-attention旧prefix可复用而linear state随turn被supersede，历史hit count相近不代表未来SSD复用；按attention type、reuse价值与SSD写成本选择admission并以价格乘子控制wear预算。trace simulator经FEMU/replay校验而非跑坏真实SSD到寿命终点；寿命是TBW/DWPD估计，WAF=1忽略GC/wear-leveling，绝非实测7.3倍寿命保证。Kimi-K3 72%linear、100GB DRAM/1或4TB SSD、多TraceA/ClaudeCode/AIPerf，baseline扩两tier并各扫超参；容量/attention-state比例决定收益。§5.7 α=1在TraceA miss0.818高于LRU0.697，73x寿命以丢复用为价；“无损命中”不能泛化。§5.8 latency仅max(transfer,recompute)近似、10GB/s SSD→DRAM/50GB/s HBM/60K prefToken/s，不是实测生产SLO。只采用tier admission需计write endurance/attention语义，不采用绝对寿命与SLO保证。2+2+2=6，INFER-GPU-MEMORY。

### 2610.31169v1 SARIA — Source-ready

[HTML](https://arxiv.org/html/2610.31169v1)§4.2–4.5、§5：累计跨DRAM residency eviction/reuse决定SSD persistence；SSD hit先入HBM，prefill后部分晋升DRAM，按reuse recency与路径带宽取舍；coordinator防DRAM大burst压住慢SSD。TraceLab/WEKA无prompt原文，synthetic保token/block复用，单session最多1active、默认4inflight、仅生成首token测prefill，不能外推decode或真实文本quality。LMCache MP/Phoenix GDS，各baseline同优化底层，cumulative ablation隔离metadata/promotion/overlap/coordination。关键反侧§5末双SSD coordination比serial慢15.8%，而单SSD慢/快两组好18/20.7%，须按effective bandwidth调allowance，不是所有混合tier并行越多越好。耐久预算1DWPD随容量比例计算，不是寿命实测。headline两个比例对照不同：writes相对Full Duplicate，TTFT相对DRAM-only，不能拼成同一基线双赢。未复现；2+2+2=6，INFER-GPU-MEMORY。

### 2610.31098v1 RIFT — Source-ready

[HTML](https://arxiv.org/html/2610.31098v1)方法/实验与Limitations：static prompt saliency随output变陈旧，stat混近期token、dyn周期rescoring、ada减少刷新；sparse-mask compressibility训练需与同数据no-mask posttraining对照，正文Table6提供该控制。Table4 Qwen3.5-4B draft/8Kactive KV、4K output、draft11、low-entropy SPEED-Bench，dyn/ada acceptance优于H2O/TriAttention；Table5提高幅度在小budget大，大budget baseline已>95%full AL故增量小。采用“active drafter cache与alignment刷新取舍”，不是总KV内存减少或端到端加速：全文limitations明确full draft history仍需HBM/offloaded保留，active budget只约束drafting device；GPU粗测rescoring最高6%draft-decode开销，目标SRAM异构deployment未测。98% AL≠98%质量/throughput；不采用未测的异构加速。2+2+2=6，INFER-SPECULATIVE-DECODING。

### 2610.31633v1 BeNice — Source-ready

[HTML](https://arxiv.org/html/2610.31633v1)方法与§5：stochastic recurrence depth诱导contractive residual，末轮KV broadcast到首轮finetune使首轮residual兼容，不是参数共享自动允许KV共享。140M/370M/770M/1.3B Parcae-style >100B climbmix tokens、standard finetune与BeNice各自HP sweep、后者3seeds；first-layer KV preserved/naive patch诊断表明首轮接口是失配来源，须保留quality检查而非纯cache别名。KV quantization互补证据是测试配置，不推广任意mixer/precision。§5.3真实sglang内存测量与workload proxy分开：Mooncake trace保arrival/length/prefix，但GLM4.7开放权重中段loop构造proxy；23.6%throughput/p90 TTFT收益是memory-limited模拟proxy，不能说质量训练过的模型生产实测。低load近无收益，接近饱和才明显。未复现，未采用普遍contraction保证。2+2+2=6，MODEL-LONG-CONTEXT。


## 证据批C：retrieval / agent / evaluation（标准完成，待独立复核）

### 2610.31019v1 Chunk Recomputation — Source-ready

[HTML](https://arxiv.org/html/2610.31019v1)方法/结果/限制：120中英Wikipedia adjacent revisions、116 common-success，strict byte-identical previous-version reuse，frozen encoder/2048 retrieval-token budget、冻结长度参数；cost为重embed输入token比例不是钱/latency。固定chunk boundary drift把没改的文字变新payload；同1%插入位置干预支持该解释但未量化全部因果。fixed-size较recursive/CDC重算多，内容感知两者排序会随长度/语言翻转；CDC四中文失败必须保NA/敏感性，不只看成功池。recall差小且CI接触0不是等价证明，标注非多annotator独立裁决；grid仅cost没有质量，不能称全grid质量无损。30 arXivEdits外检只cost且不pool。采用dynamic KB chunker评估需同时测update recomputation和固定预算quality，非宣布CDC普胜。2+1+2=5，AGENT-RAG。

### 2610.30612v1 Fusion Tax — Source-ready

[HTML](https://arxiv.org/html/2610.30612v1)§IV–V/结论：Anserini BM25、BGE-small/base/large及MiniLM/Qwen3 embedding共五encoder、七BEIR、RRF/CombMNZ/interpolation，明确oracle max(component)非可部署上限，与always-dense两种tax分开。LOCO/5fold选weight隔离evaluation调参；SPLADE替换/encoder ladder反驳只因弱单路。fusion aggregate普遍有益不排斥query伤害；相关文档多数仍在top10但少量coverage丢失不能靠rerank修。cheap-feature router跨corpus meanAUC.59且没胜static interpolation，因此作者不是提供可靠自动“何时不融合”算法。crossencoder可修部分同时造成新hurt，不能保证消除tax。采用风险敏感per-query评估与目标语料sparse/dense balance，非否定hybrid或固定推荐RRF。运行硬件/latency不用于本质量命题，未复现。2+1+2=5，AGENT-RAG。

### 2610.31446v1 AMV-Guard — Source-ready

[HTML](https://arxiv.org/html/2610.31446v1)§2–5/Limitations：relevant/action-supporting/critical premise分层，verification价值取决它能否改变Proceed/Abstain而非单次belief熵。Proposition1仅固定p、abstainκ、单symmetric verifier r>1/2的expected-loss special case，无额外screens；成本大可无verify区，imperfect verifier高后果需直接abstain，perfect verifier例外。实用gate是一阶VOI+有限depth2 fallback，不是全长最优；premise extraction recall封顶、shared binary verifier/风险hyperedge是近似。ToolSandbox vs same-input static cost−33.9%，Gate-harm0≠端到端harm0（raw7.03%）；AppWorld只gate-core迁移且Gate-harm7.89%，不是完整pipeline跨环境保证。loss consequence部分手工/模拟，覆盖率与safe recall须同时看。采用action-conditioned验证边界不采用生产安全保证。2+2+2=6，AGENT-MEMORY。

### 2610.30769v1 Herding — Source-ready

[HTML](https://arxiv.org/html/2610.30769v1)§2–3/Discussion：48新合成song lyrics、agent先选4再推荐、累计计数回写后人可见，independent vs两级influence parallel worlds隔离内生feedback；13 homogeneous model populations、8 influence worlds测divergence/half-time rank correction。正文明确多数模型强影响下correction近0并非永不纠偏。人类基准音乐/audio/download/布局/选择数和LLM lyric/recommend不同，不能把差异全归LLM本质；无explicit collaboration/incentives、异构team/真实工作未证。可采用“前人输出成为后人可见流量信号会削弱独立证据、形成路径依赖”的局部反例，不推生产team必herd、不推高intelligence必safe。非吞吐研究，hardware/SLO不适用；未复现。2+1+2=5，AGENT-MULTI-AGENT。

### 2610.31355v1 Muffin — Source-ready

[HTML](https://arxiv.org/html/2610.31355v1)§3–4/限制：orchestrator按难度选单/多agent，多个agent共享compact findings buffer而private trace不共享，最后summarizer；同served模型、默认3agent/5step、4模型、vLLM 2/4H100、3runs，固定step不是固定token/latency预算。full-trace对照同pipeline直接禁selective-sharing：最后accuracy85→87.3但160.6K→41.9K tokens，支持lossy-summary质量/成本取舍非无损；summarizer有实质额外计算（44.9→59.2）不能全归异步buffer。k findings更多会伤小模型，过时/重复信息是成本。只测QA/reasoning无tool/environment/long-horizon，不能说生产异步执行可靠；无wall-clock async并行度控制不采用延时加速。2+1+2=5，AGENT-MULTI-AGENT。

### 2610.30635v1 Specification–Oracle Gaps — Source-ready

[HTML](https://arxiv.org/html/2610.30635v1)方法/§5–6：static五语言audit区分spec/base可推出与hidden name/path/literal，reference单名遮盖126/128无法编译为可执行干预，不仅相关观察。held-out94+103 cases独立expert blind，precision58/65=89.2%（79.4–94.7CI），recall13/14=92.9%（68.5–98.7CI）样本小；不是完美标注。35public runs中blocked80.6%失败vsmatched new-test48.4%，混杂控制/cluster CI仍非所有失败因hidden-name；去受影响tests leaderboard基本稳定、邻名次CI本已重叠，不能说整体排行失效。按repo得分可显著变；benchmark construction（release-note/LLM summaries vs test-aligned）决定漏洞频率。采用spec必须公开oracle需依赖/审计test要求，不把test pass作通用能力无偏指标。未执行audit；2+2+2=6，PLATFORM-EVALUATION-SYSTEM。


## 证据批D：diffusion（标准完成，待独立复核）

### 2610.30744v1 Random Remasking — Source-ready

[HTML](https://arxiv.org/html/2610.30744v1)§3–5：clean sequence上uniform remask-denoise构成Markov核；true denoiser核stationary data，不代表learned核必收敛。Proposition2 KL下一步≤mask-channel contraction×旧KL+denoiser误差ε，更多remask降前项却增重建难度，t=0无contraction；因此不是只加compute即可消灭model误差。TCT暴露自身trajectory错误、top-k揭示，实际argmax/early exit和理想stochastic核需分开。Sudoku-Hard/3SAT同compute budget256/32steps-per-token，same TCT checkpoint比ReMDM仍好，uniform-vs-low-confidence消融表明局部策略会破scaling；earlyexit省NFE但非全域正确停止oracle。LLaDA2.1mini16B/HumanEval+有自跑correction对照，但官方Q-mode数为引用不同protocol，不能同budget胜率合并。近log-linear只两logic任务，不外推开放语言长期scaling。2+1+2=5，MULTIMODAL-GENERATIVE-PARADIGMS。

### 2610.30920v1 DConstrain — Source-ready

[HTML](https://arxiv.org/html/2610.30920v1)§3–5与运行结果：cold把local transition编成context-param program，stack/env/history保symbolic；warm绑定reached config，模型forward可并行；token canonical effect聚合后Viterbi用max、sample用sum再恢复token。Theorem4.1 exact指同reference parser/initial config/candidate sets/acceptance condition下同token-language；sample exact是固定canvas上独立位置score乘积约束分布，不是整条DLM真实joint或语义正确。BFCL2495全池admission/completion/validity/semantic分母分开，latency common-success也按order分别构造，不能跨order cohort比吞吐。LLaDA2.2 TPS排prefill、DiffusionGemma含prefill，不能横model倍率。BFCL100%compile不表示通用JSON Schema全支持：JSB oneOf/allOf等片段不支持/resource budget失败；depth4与finite baseline公平比较。ablation显示eager env绑定cold14.61x、去group solve6.81x；本次只采用避免状态展开、精确后继与统计口径，不抄headline大倍率普遍加速。2+2+2=6，MULTIMODAL-GENERATIVE-PARADIGMS。

### 2610.31120v1 SetCommit — Source-ready

[HTML](https://arxiv.org/html/2610.31120v1)§3–4：置信+entropy-weighted local risk选择集合，bounded remask exchange保持host net quota；不是证明全局joint token正确。same-state intervention共享proposal/context/commit数/剩预算，仅变位置，较confidence/spacing/random/shuffled-risk controls支持coordination而非随机扰动。LLaDA8B/Dream7B GSM8K/MATH500/MBPP/HumanEval，与native/Fast fixed+adaptive/EB hosts成对；Dream改为deterministic top1所以是完整pipeline比较非纯selector，EB为作者reimplementation。quality target native128−3pp、budget/threshold网格找最低latency，非同质量精确等值；点估计还需区分置信区间。固定NFE有额外延迟（cached相对成本更大），收益来自少NFE抵消coordinator；选位置收益比remask大，后者仍有补益；frozen-config transfer有限。采用“集合commit与可修订是独立轴”，不作普适可并行性/无损/生产TPS保证。2+1+2=5，MULTIMODAL-GENERATIVE-PARADIGMS。

### 2610.31198v1 T2Quant — Source-ready

[HTML](https://arxiv.org/html/2610.31198v1)§3–5/Limitations：目标task无标签calibration prompts，固定FP reference trajectory/state重放候选bit，用committed-position KL×后续影响作surrogate，DP分配时间window activation bits；“全局最优”仅有限bit集合、非负整数additive cost的calibrated surrogate，不是非加性真实accuracy最优。三DLM六bench，与RTN/DLLMQuant/FAIR-Calib/STaR paired同sampler/prompt，heldout与calibration不交；相同4.00avg activation bits及同budget random schedule控制混精度本身。42/54单bench改善不是全部改善；calibrate4tokens/step迁移2可，8时整体质量崩且增益消失。仍需representative task prompts非任意未知任务免校准；硬件速度/energy/safety明确future work，平均bit预算不是等latency/算力保证。2+1+2=5，INFER-TENSORRT-LLM。

### 2610.31576v1 Learned Unmasking / OnTrack — Source-ready

[HTML](https://arxiv.org/html/2610.31576v1)§3/§5/§7：final-output token正确不等于early commit安全；trajectory-contraction teacher只把能直达reference后态的commit标正，控制teacher label/训练state/confidence/hidden features，856Kpolicy融合confidence+hidden。policy overhead profiling在测试配置给约10%NFE降低盈亏线，非跨hardware常数；采用命题是teacher语义和总cost校验，不抄普适阈值。数学训练→code、LLaDA8B→Dream7B单独迁移有益，但length+domain同时shift失败；高accuracy target常被training-free Fast/EB超过，hidden-features依赖prefix caching可损约2pp。官方Learn2PD checkpoint对照、LUP/TraceLock无可用checkpoint没纳入，不能称胜全部learned methods。采用moderate-target frontier而非全面优胜，未复现。2+1+2=5，MULTIMODAL-GENERATIVE-PARADIGMS。


## 实际 owner / 最小 PRE：cache4 + diffusion5（仅提案，未写Books）

已实际读取PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE与本日State；对下列目标论证及直接前后段全文读取，邻章只读交接与owner界面（Ch21/23/25/47–50/53/55）。下列PRE不授整合完成；root为唯一writer，reader需先核精确当前位置再准写。

### 30791 Gandalf：Ch54真实差额，拟整合

目标 `books/part-05-inference-system/54-gpu-memory.md`“扩展层级”；现303–319已有flash寿命/placement与Lachesis语义存活，但没有“同历史hit计数下full-attention prefix与superseded linear state的不同SSD未来复用”。

精确前侧：以“此时容量、placement 与 admission 要共同选择”开头、以 `<!-- source-family:SF-2026-ARXIV-2609-39131 -->`结尾的整段。
精确后侧：以“Flash placement 还要区分最近读写与语义存活时间”开头的整段（与后随Lachesis评价保原样）。

拟在两侧之间插入一段（与SARIA连写时按下面次序）：

> SSD 准入还须认识模型状态的更新语义，而不只累计访问次数。Full-attention 的旧 prefix 可以在多轮继续复用，hybrid 模型的 linear state 却可能在下一轮后被新状态取代；一个对象已经在 DRAM 命中过，未必还值得为它支付一次 flash 写入。可把 attention 类型、跨层复用机会与写耐久价格共同用于 admission，在保留 DRAM 热数据的同时过滤低预期复用状态。这是以重算和额外 miss 风险换寿命的条件分支，不是无损丢弃；[受限 trace 研究](https://arxiv.org/html/2610.30791v1)中部分价格设置确实降低命中，寿命仍是带单位写放大等假设的估计。状态语义、负载或介质不匹配时，保守 write-back、较低写入价格与显式重算仍应保留，不从访问计数或模拟年数签发实际寿命保证。<!-- source-family:SF-2026-ARXIV-2610-30791 -->

拟Review note：`SF-2026-ARXIV-2610-30791` — exact-v1方法/§5.1–5.8，2+2+2=6；只采attention-type与SSD未来复用分责，保WAF1/TBW估算、miss反退与全费，未核实现/复现。

### 31169 SARIA：同Ch54相邻真实差额，拟整合

与上项同一原前后侧，在Gandalf段后、原Flash-placement段前；原文的“何时值得搬”和capacity planning有原则，但未写跨DRAM residency admission、SSD-hit部分晋升及混源ingress协调失败界。

> SSD 中保留一份 DRAM 已覆盖的副本，也可能只增加写入而没有实际读收益。另一条分支跨多次 DRAM 驻留累计 eviction/reuse 历史，等出现“必须活过本次 DRAM 驻留”的证据才持久化；SSD 命中后只把部分状态从 GPU 晋升回 DRAM，避免一次全量复制挤走别的热数据。重新加载同时来自 DRAM 和 SSD 时，还须按两条有效路径的速率限制 DRAM burst，让慢 SSD 能持续前进，而不是把所有读一齐发出。[受限 agent-prefix replay](https://arxiv.org/html/2610.31169v1)支持这种联合控制，但双 SSD 配置中协调反而慢于串行，且测量只到首 token；额外历史、元数据、晋升流量与调速均计费，带宽估计或复用失配时应减小 promotion、重校准配额或回到串行加载，不把写量与 TTFT 的不同基线收益拼成同一保证。<!-- source-family:SF-2026-ARXIV-2610-31169 -->

拟note：`SF-2026-ARXIV-2610-31169` — exact-v1§4.2–4.5/§5，6分；仅跨residency persistence/部分晋升/混源进度，保synthetic reuse replay、首token与双SSD反侧，未复现。

### 31098 RIFT：Ch48真实差额，拟整合

目标 `books/part-05-inference-system/48-speculative-decoding.md`。现“Chain Depth 会累积 Attention Drift”属proposal表示漂移，“Attention 转换必须保持 Draft Function”属MHA→MLA结构转换，都未承载long-output令prefill-selected draft KV失效及active budget≠full-history budget。
精确前侧：以“并行 draft 还要分别解决两个容易混淆的问题”开头、以“把被拒状态重新纳入训练”结尾的整段。
精确后侧标题：`### Chain Depth 会累积 Attention Drift`及其原完整首段。

> Draft 的 cache 选择还有随输出增长而过时的问题：prefill 中重要的位置不一定持续支持后续长输出，固定活跃 KV 预算下可在近期 token 与历史显著位置间重新分配，并用较稀疏的自适应刷新摊薄重评分；训练时暴露稀疏 attention mask，则能单独改善压缩后的 target agreement。这些变化只提高 proposal 的可用性，target verifier 的接受权不变。[RIFT 的受限对照](https://arxiv.org/html/2610.31098v1)主要测 acceptance length，刷新还要求完整 draft 历史继续留在 HBM 或外存，所以较小 active cache 不是总 KV 消失，也不是端到端加速证书。全历史存储、评分、搬运、额外训练与验证都要计费；短输出、刷新成本高或 alignment 回归时，静态保守选择、较大预算和原 drafter 仍合理。<!-- source-family:SF-2026-ARXIV-2610-31098 -->

拟note：`SF-2026-ARXIV-2610-31098` — exact-v1方法/T4–6/Limitations，6分；只采decode-staleness/active budget分责；full history与rescoring全费，不采异构速度或总内存保证，未复现。

### 31633 BeNice：Ch22真实差额，拟整合

目标 `books/part-02-model/22-long-context.md`“选择器的成本如何摊薄：刷新、复用与地址状态”。现451–473覆盖层/head/source共享，不覆盖同权重recurrent depth中首轮与最终轮KV的兼容训练。
前侧：以“这用训练时的源/消费结构与 recent-budget 耦合换取更少重复状态”开头、结束 `<!-- source-family:SF-2026-ARXIV-2609-26368 -->`的整段。
后侧：以“共享selector还可以扩展访问的依赖深度”开头的完整multi-hop段。

> 反复执行同一组层还会产生另一种状态重复：权重虽然共享，每个 recurrence 的表示不同，默认仍各存一份 K/V。若训练让残差更新逐步趋近共同状态，可以把最终轮 KV 作为跨轮共享候选，但首轮的输入分布往往最不兼容，需要在后训练中显式暴露末轮 KV 并修复其 residual，而不能只给 cache 指针取别名。[受限 looped-model 研究](https://arxiv.org/html/2610.31633v1)用 stochastic depth 与此类兼容训练支持质量对照；它不证明普通 checkpoint 自动可共享，workload 加速又来自另构造的循环代理模型。适配训练、质量回归、缓存布局和完整运行状态均计费；首轮或任务质量失配时应保留独立 KV 或减少循环，不从固定参数量推固定推理内存或生产吞吐。<!-- source-family:SF-2026-ARXIV-2610-31633 -->

拟note：`SF-2026-ARXIV-2610-31633` — exact-v1方法/§5，6分；仅weight sharing不等KV sharing与首轮接口修复；quality-trained模型与proxy workload分账，未复现。

### 30744 Random Remasking：Ch24真实差额，拟整合

目标 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`“Self-revision”。现含provisional state与self-generated noise，但无uniform remask核的stationarity/model-error分责。
前侧整段以“Runtime trick 不足以保证模型会修正自己的错误”开头、以“其 batch-1 双卡结果不能写成 serving goodput”结尾。
后侧标题：`#### Iterative Generation 允许安全状态被重新 Mask`。

> 修正也可以不追着最低置信位置走，而在当前完整候选上均匀随机重掩码，再做 denoise，把每次更新写成 clean-sequence 上的 Markov 核。[受限理论与实验](https://arxiv.org/html/2610.30744v1)中，真实条件去噪器的核以数据分布为 stationary，但学得核还留下重建误差项：更多破坏可降低旧分布差异，也会增加恢复难度，不能由理想 stationary 推实际模型必收敛。训练暴露自己的修正轨迹、推理采用有限预算与稳定后提前退出，才形成可测的选择；逻辑任务近 log-linear scaling 不等开放语言通律。重掩码、训练和额外 forward 都付费；修正振荡、模型误差或净成本失控时，应减少重开并保留原采样与完整质量检查。<!-- source-family:SF-2026-ARXIV-2610-30744 -->

拟note：`SF-2026-ARXIV-2610-30744` — exact-v1§3–5/Prop1–2，5分；只true/model核分责，保ε项、argmax/earlyexit与有限任务，不授通用收敛/速度，未复现。

### 30920 DConstrain：Ch24真实差额，拟整合

现“Diffusion Constrained Decoding”只覆盖existential lookahead与soft accepted-mass，不覆盖精确weighted successor编译如何避免stack/field-history枚举。
前侧：以“一种受限分支是在每轮 proposal 时利用所有位置的并行分布做 lookahead”开头的整段及 `<!-- source-family:SF-2026-ARXIV-2602-00612 -->`。
后侧：以“连续 latent diffusion 没有每步可提交的 parser state”开头完整Diffinity段。

> “仍存在合法补全”只回答 feasibility；若要在候选图上找最高权重路径或按约束后的权重采样，还须构造相容后继及其概率质量。把 parser stack 与已经写过的字段全部展开为离线状态，可能因组合爆炸而被迫固定字段顺序；另一分支把局部 token 效果编为带上下文参数的程序，运行时才绑定到达的 stack/environment，并复用等效 token group。[DConstrain 的受限机制](https://arxiv.org/html/2610.30920v1)保持同一 parser、候选集合与接受条件下的 successor，以及固定候选图的 max/sum-product 目标，不是完整 DLM 真实 joint 或语义正确证明。程序、图构造与 CPU–model 重叠均有成本，schema 片段和资源预算也有限；超支持域或编译不划算时，保留完整输出校验、可完成性 verifier 或 AR constrained decoding，不由 BFCL 有效率推任意 JSON Schema 保证。<!-- source-family:SF-2026-ARXIV-2610-30920 -->

拟note：`SF-2026-ARXIV-2610-30920` — exact-v1§3–5/Th4.1/ablation，6分；只symbolic successor与objective-preserving grouping，保fixed-canvas/fragment/cohort及全费，未复现。

### 31120 SetCommit：具体已有覆盖（NC提案，不增正文/末注）

实际 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:1432`–1467：“并行解码若只按单 token confidence选择同一步提交位置”两段已有互补位置集合、selection仅proposal/额外attention和调度、信号失配回退top-k/减K/允许重开；其后“用跨步分布不稳定性分配Revision Budget”已有remask/revision与最终commit分权，接DMax provisional→修正→gate。SetCommit新文本entropy-distance proxy/预算中性exchange与same-state干预支持这些既有取舍，未给该proxy普遍联合正确性或额外长期必需state contract；因此不为泛化相同原则再加段。报告保同状态反证、Dream top1 pipeline变化与质量容差，NC须reader核的是这份实际正文而非只主题名称。

### 31198 T2Quant：Ch49真实差额，拟整合

目标 `books/part-05-inference-system/49-tensorrt-llm.md`“Build-time 与 Runtime-time”。现“Diffusion Decode Granularity”已有layer/step稀疏代价DP，但未拥有task-conditioned activation-bit calibration。
前侧：以“这条分支把控制开销前移到校准训练与 build-time”开头、以“仍是不同责任的共存分支”结尾整段。
后侧标题：`### 同一 Timestep 的跨迭代缓存是一条近似执行分支`。

> 静态预算也可以分配 activation 位宽，而不只分配跳算率；同一 diffusion 模型在不同任务和 denoising 阶段，对量化扰动的敏感性可能不同。可用代表性无标签 prompt 保存全精度参考轨迹，在相同状态重放各候选位宽，按局部分布偏移及后续影响构造校准代价，再在平均 bit 预算下选择每个时间窗口的精度。[受限任务/时间量化研究](https://arxiv.org/html/2610.31198v1)的动态规划只对有限候选与可加 surrogate 最优，不对真实非加性任务指标最优；平均 bits 相同也不等硬件 latency 相同。校准数据、全精度参考、所有候选重放、物理格式与 kernel 切换都计费，生成粒度或任务分布改变须重验；部署收益未验证或质量退步时，保留统一位宽和更保守高精度，不把量化预算直接换成能耗/速度保证。<!-- source-family:SF-2026-ARXIV-2610-31198 -->

拟note：`SF-2026-ARXIV-2610-31198` — exact-v1§3–5/Limitations，5分；只task/time activation precision与surrogate DP，保sampler/calibration身份及未测hardware效率，未复现。

### 31576 OnTrack：Ch24真实差额，拟整合

目标Ch24“Commitment Policy 可以从未来稳定轨迹学习”。现原首段用未来不再变化的token-local标签，缺“终值匹配可能提前commit后离开参考轨迹”的teacher语义差异。
前侧：以“固定置信阈值或 block schedule 假设所有 token 的收敛速度相似”开头、以“不证明其保持自回归式 exactness”结尾整段。
后侧：以“连续视频的提前结束还须分开输出、当前可读 KV 与下一 chunk 的历史”开头整段。

> 从轨迹学习时，还要区分“本轮 token 恰好等于最终答案”与“此时提交后仍能沿参考轨迹继续”。前一种标签可能过早放行本来正确、却改变了后续 conditioning 的 token；另一种 teacher 只允许能直接到达参考后态的 commitment，再把 confidence 和 hidden features 交给小控制器预测。[受限 learned-unmasking 对照](https://arxiv.org/html/2610.31576v1)支持这种标签分责，但不是参考轨迹即真值或控制器保持原分布：高准确率目标、同时改变领域和长度，以及扰动 hidden 的近似 cache 都可能使优势消失。Teacher 轨迹、policy 训练和逐步推理仍增加成本，少 NFE 须抵过完整控制开销；迁移或校准不合时，保留保守置信/entropy 策略与完整更新，不从局部盈亏阈值批准所有部署。<!-- source-family:SF-2026-ARXIV-2610-31576 -->

拟note：`SF-2026-ARXIV-2610-31576` — exact-v1§3/§5/§7，5分；只teacher trajectory-contraction与policy全费，保高目标/双shift/cached-feature反侧，未复现。

## 实际入口与停止点

执行日期：2026-10-24 Asia/Shanghai。官方 `https://arxiv.org/list/<category>/new` 当前页面均显示 `Showing new listings for Friday, 23 October 2026`；12分类为cs.CL、cs.LG、cs.AI、cs.DC、cs.CV、cs.RO、cs.AR、cs.PL、cs.OS、cs.PF、cs.IR、cs.MA。默认页显示全部（最多2000），标题导航到当页末尾；仅相关新命名机制取完整摘要，不将整类变成逐项题摘待办。跨分类以ID去重。列表在替换区只以明确机制/纠错说明定点触发，不能把所有replacement当重要修订。

主要有限查询（web搜索，每个只取引擎返回首批；结果未恢复窗内论文，不能据此称零命中）：`site:arxiv.org/abs/2610 "October 23" ("inference" OR "KV cache" OR "kernel")`；同前缀加 `("reinforcement learning" OR "training" OR "MoE")`；`("world model" OR "vision-language-action" OR "diffusion")`；`("agent" OR "memory" OR "retrieval")`。结果漂移到旧年，故使用官方日期列表的相关标题导航补检，不扩大到月列表逐项筛选。误开月列表cs.CL/cs.DC仅前50标题线索，不纳入窗口分母。

日期依据：官方上述日公告的具体ID条目支持首次列入23日批次；依arXiv公告日程其公开对应BJT 2026-10-23。不用v1提交日期冒充公开日期；部分长期审核稿v1提交早于本月，仍保留原记录。对已知更早正文需另行定点检查，不作全球首公开保证。轻量abs页检查撤回/撤稿字符串本批均无命中，不遍历历史。

## 初筛时记录（当前审阅状态以上方证据段及REVIEW为准）

以下保留首批和第二批的完整题摘与当时拟判断，仅作初筛依据；不作为当前 pending 状态。本代理23项Source-ready、另7项由oct24_org负责的分工保持不变。

### [2610.30154 — baseVultra: Compact Nonlinear Recurrence with Reallocated Capacity](https://arxiv.org/abs/2610.30154)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Linke Zhang [view email] [v1] Sun, 23 Aug 2026 14:31:35 UTC (46 KB)。

Abstract:Nonlinear recurrent networks remain useful for streaming sequence modeling, yet gated cell design is still dominated by LSTM and GRU. We study whether recurrent computation can be reallocated away from gate transforms and toward candidate generation. We propose baseVultra, a compact recurrent cell that concentrates the dense recurrent budget on a single H x H candidate-generation matrix, while replacing recurrent gate matrices with O(H) diagonal interactions. The candidate update combines this dense branch with two low-rank auxiliary branches, an EMA cache, and learnable output blending; the gates additionally receive lightweight second-order access to h_{t-2} through diagonal terms. On TinyShakespeare character-level language modeling, baseVultra achieves a validation loss of 1.594 in the compact one-layer 200K setting, compared with 1.604 for a parameter-matched LSTM and 1.616 for a parameter-matched GRU, while its dense recurrent matrix-vector computation is about 54% of GRU under matched hidden size for this configuration. On text8, a roughly 45x larger benchmark, baseVultra is competitive with full-gate cells (1.854 bpc vs. 1.849 for GRU and 1.837 for LSTM). On formal-language probes, the largest gains appear under constrained hidden-state capacity (0.991 vs. 0.761 GRU and 0.691 LSTM OOD2 accuracy on Counter at H=16) and vanish as hidden size grows. These results characterize where and when candidate-focused recurrent capacity allocation helps: the benefit is concentrated in compact regimes, while full-gate cells remain competitive at scale.

拟入：小状态容量下门控矩阵与候选生成的预算重分配给出有效边界，非以小规模结果拒收。拟分2+1+2=5；owner MODEL-LONG-CONTEXT。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。


## 第二批有限主题完整题摘（初筛时记录）

本批由cache/offload/draft、masked-diffusion commit/correction、world-model→action训练、RAG更新/评价盲区、memory verification/异步协作这些具体查询线索定点打开。标题命中不是准入规则；以下逐项完整题摘判断。未对宽列表剩余条目建立待关闭分母。

### [2610.30744 — Random Remasking Scales Masked Diffusion Inference](https://arxiv.org/abs/2610.30744)

Submission history From: Zhaoyi Zhou [view email] [v1] Thu, 22 Oct 2026 05:15:10 UTC (486 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Masked diffusion models (MDMs) generate sequences by progressively unmasking tokens, but errors introduced during decoding are typically irreversible. Recent work has shown that iterative correction can improve sample quality, yet existing theory fails to explain this given a learned, imperfect denoiser model. We re-formulate MDM inference as a Markov chain on the clean sequence space, defined by a remask-denoise kernel that randomly re-introduces masks and then denoises. This helps us analyze the actual denoising trajectory towards the data distribution. The analysis motivates Random Remask-Denoise (R$^2$D) inference, a purely test-time, finetuning-free, reward-free procedure. To further improve performance, we propose Trajectory Correction Training (TCT), a denoiser-training procedure that exposes the model to its own errors along the generation trajectory. On logical tasks, our approach exhibits a striking near-log-linear test-time scaling, achieving over 97% accuracy on hard Sudoku puzzles and over 99% accuracy on 3-SAT. Our approach also applies to pretrained models on actual language tasks, beating iterative correction baselines and the official Q-mode accuracy of LLaDA2.1-mini on HumanEval+.

拟入：不可逆commit→随机remask-denoise Markov核及训练轨迹纠错→增大test-time预算是否仍有效；2+1+2=5；MULTIMODAL-GENERATIVE-PARADIGMS。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30791 — Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving](https://arxiv.org/abs/2610.30791)

Submission history From: Jiayi Yao [view email] [v1] Thu, 22 Oct 2026 06:10:08 UTC (474 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:KV caching reduces the serving cost of large language models (LLMs), but the growing KV cache footprint is increasingly exceeds GPU and host-memory capacity. Therefore, people use SSD to expand the KV cache storage capacity with high I/O bandwidth. However, in production LLM workload, such as multi-round conversation and LLM agents, the total amount of KV cache writes significantly exceeds SSD capacity, shortening SSD lifetime from years to months. To improve SSD lifetime, a natural solution is to reduce the KV cache writes by gating the KV cache writes via historical access patterns. However, that significantly lowers the KV cache hit rate (and increase the LLM serving cost) since KV caches from different attention types might have identical historical access pattern but different future access patterns. Our insight is that, to reduce KV cache writes without hurting KV cache hit rate, one need to not only consider the access pattern, but also application-level information such as the attention type of KV cache. Leveraging this observation, we propose Gandalf , the first SSD KV cache offloading system with SSD life time awareness. Gandalf prioritize the admission of full-attention KV cache into SSD over the cache generated by other types of attention, which significantly increases SSD lifetime without sacrificing cache hit rate. Our evaluation shows that Gandalf extends the SSD lifetime by 7.3X on average, while having negligible impact on cache hit rate across multiple workload traces and wide range of hardware capacity. Gandalf design can be extended to other flash-based storage, such as High Bandwidth Flash (HBF).

拟入：仅访问历史不能区分attention类型未来复用→attention-aware SSD写入准入→寿命/命中率联合选择；2+2+2=6；INFER-GPU-MEMORY。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31169 — SARIA: Persistence-Aware KV Caching with Coordinated DRAM--SSD Reload for LLM Agents](https://arxiv.org/abs/2610.31169)

Submission history From: Hui Li [view email] [v1] Thu, 22 Oct 2026 12:25:27 UTC (1,004 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Multi-turn LLM agents usually reuse long context prefixes, making key value (KV) caching crucial for reducing prefill latency. SSDs provide a low-cost extension to limited DRAM capacity but introduce two key challenges. Eagerly persisting all KV cache blocks incurs substantial write traffic and rapidly consumes finite SSD endurance. Meanwhile, the small number of SSDs provisioned in typical GPU servers limits aggregate reload bandwidth, making SSD-resident KV cache much slower to retrieve than that in DRAM and inflating prefill latency.
We present \textsc{Saria} (Selective Admission and Reload for Inference Acceleration), a KV caching system that jointly manages DRAM and SSD by exploiting the session-level temporal locality of LLM agents to reduce SSD writes and accelerate cache reload. On the write path, \textsc{Saria} uses eviction and reuse history to selectively persist KV cache blocks that exhibit reuse opportunities beyond their DRAM residency, avoiding unnecessary writes for KV cache already hosted in DRAM. On the read path, \textsc{Saria} promotes selected SSD-hit KV cache blocks from GPU memory into DRAM after prefill, allowing subsequent reuse within the same session to reduce SSD read traffic while limiting DRAM contention. A transfer coordinator paces DRAM reads while SSD transfers are active, allowing both paths to make progress and efficiently share GPU ingress bandwidth.
We implement \textsc{Saria} on LMCache MP and evaluate it using workloads from TraceLab and WEKA, covering both full-attention and hybrid-attention models. The results show that \textsc{Saria} reduces SSD writes by 57.1--58.9\% compared with popular full duplicate caching and the mean time to first token (TTFT) by 42.3--79.7\% over DRAM-only caching.

拟入：DRAM/SSD重复持久化与reload争抢→选择准入、GPU→DRAM晋升及传输协调→联合优化写耐久和TTFT；2+2+2=6；INFER-GPU-MEMORY。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31098 — RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training](https://arxiv.org/abs/2610.31098)

Submission history From: Dor Tsur [view email] [v1] Thu, 22 Oct 2026 11:12:23 UTC (119 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Speculative decoding is a popular decode acceleration method. As such, it is particularly relevant to long-output generation, which requires an increasingly large KV cache. KV cache compression offers a way to constrain costs in long-context drafting. However, compression methods that focus on prefill information can lose relevance as the output length grows. We term this phenomenon decode staleness and show that it degrades draft model accuracy under selection-based KV cache compression. We introduce RIFT, a family of selection-based KV cache compression strategies that balance prefill information and recent generated tokens. We show that refreshing the KV cache selection during token generation significantly improves the drafter's quality at the cost of additional decode latency. To alleviate the refresh costs, we propose an adaptive KV refresh strategy that reduces the number of score calculations while retaining the drafter's quality. We further demonstrate how a compressibility-driven drafter training phase, based on sparse attention masks, can improve the drafter's quality under a compressed KV cache. Combined with compressibility training, RIFT enables Qwen3.5-4B, drafting for Qwen3.5-122B, to retain over 98% of its full-cache acceptance length on 32K-token inputs, 4K-token outputs, and an 8K-token KV cache budget.

拟入：prefill静态压缩在长输出过时→自适应刷新与可压缩性训练→drafter acceptance/刷新时延取舍；2+2+2=6；INFER-SPECULATIVE-DECODING。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31633 — BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing](https://arxiv.org/abs/2610.31633)

Submission history From: Hayden Prairie [view email] [v1] Thu, 22 Oct 2026 17:49:44 UTC (2,533 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Looped architectures scale quality while keeping parameter count fixed by repeatedly passing activations through the same block of layers. During inference, each recurrence generates independent KV-caches, causing memory to grow linearly. To address this challenge, prior work has proposed KV-sharing (i.e., sharing KV-caches across depth), finding that, in some cases, the KV-cache of the final recurrence can be shared with the earlier recurrences without quality loss, a property we denote as KV-shareability. However, the mechanisms underlying KV-shareability remain poorly understood, with even identically trained looped architectures not consistently exhibiting it. In this paper, we study how KV-shareability can be enabled in looped models. We propose a two-stage method: in the first stage, we use stochastic depth during pretraining, which induces contractive residual dynamics that drive representations toward a common limit across recurrences. In the second stage, we propose BeNice!, a post-training method that broadcasts the final recurrence's KV-cache into the first recurrence, training it to produce compatible residuals while preserving the original model's quality. As a result, BeNice! enables KV-shareability while matching standard finetuning's unshared validation perplexity. Using BeNice!, we show that KV-sharing is complementary to alternative KV-compression methods, composing with memory-efficient sequence mixers (e.g., multi-latent attention, Kimi delta attention) and low-precision KV-cache quantization (e.g., fp8, mxfp8, nvfp4). Finally, in simulated low-memory, long-context inference, KV-sharing improves cache hit rates by up to 31.4%, increases throughput by up to 23.6%, and reduces p90 time-to-first-token by up to 83.6%.

拟入：参数共享不等于KV共享→stochastic-depth收缩与末轮KV广播训练→looped模型的内存随深度增长能否打破；2+2+2=6；MODEL-LONG-CONTEXT。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30920 — DConstrain: Compiling Context-Parameterized Transitions for Diffusion Language Model Constrained Decoding](https://arxiv.org/abs/2610.30920)

Submission history From: Shidong Cao [view email] [v1] Thu, 22 Oct 2026 08:40:11 UTC (1,746 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Diffusion language models (DLMs) decode multiple tokens in parallel, so individually valid tokens can be incompatible together under a schema. Exact joint inference over a grammar graph enforces compatibility, but it requires token-labeled successors across many hypothetical parser configurations. Encoding stacks and field histories in compiled states can cause exponential growth, which forces prior exact decoders to fix property orders and exclude valid outputs. We present DConstrain, which compiles schemas into context-parameterized transition programs. Cold compilation specializes token consumption to local grammar states while retaining context-dependent stack operations, environment guards, and caller-dependent deferred parsing symbolically. Tracking field histories as runtime values supports arbitrary property order without enumerating field subsets offline. At runtime, warm compilation binds reached configurations to these programs to construct exact successors, overlapping with the model forward pass because graph construction requires no model scores. Furthermore, token-effect grouping merges tokens with identical compiled effects before runtime contexts are bound, so groups are reused across stacks and environments even when concrete successors differ. Objective-specific score aggregation and token restoration provably preserve both the Viterbi optimum and the token-labeled path distribution of ungrouped inference. Across three benchmarks and two DLM families, DConstrain compiles 100% of BFCL schemas under arbitrary property orders, whereas an optimized finite-state baseline compiles only 71.30-85.81%. Under arbitrary property order, it reduces BFCL end-to-end decoding latency by 6.65-46.26 times with 100% schema validity and raises DiffusionGemma's BFCL accuracy from 37.27% under fixed order to 81.56%.

拟入：schema编译把栈/field history展开导致爆炸→符号上下文程序+warm绑定+token effect grouping→保任意字段序和精确推断；2+2+2=6；MULTIMODAL-GENERATIVE-PARADIGMS。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31120 — SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding](https://arxiv.org/abs/2610.31120)

Submission history From: Yuannuo Feng [view email] [v1] Thu, 22 Oct 2026 11:33:49 UTC (742 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Diffusion language models generate multiple token positions in parallel, but few-step decoding makes parallel commitment difficult: tokens that appear reliable individually may be jointly inconsistent, while premature commitments can prevent later context-dependent refinement. In this paper, we introduce SetCommit, a training-free method for coordinated parallel token commitment. Instead of selecting tokens independently by confidence, SetCommit selects a commitment set that balances token reliability against local joint commitment risk, preserving conditioning opportunities for subsequent denoising steps. It further performs budget-neutral local exchanges, replacing vulnerable earlier commitments when newly revealed context supports more reliable alternatives. SetCommit requires no retraining or architectural modification and is compatible with existing diffusion decoding strategies. Experiments with LLaDA-8B and Dream-7B on GSM8K, MATH-500, MBPP, and HumanEval show accuracy/pass@1 gains of up to 7.4 percentage points over native decoding at 32 model evaluations. At common quality targets, geometric-mean incremental speedups range from $1.44$ to $1.74\times$. Code is available at this https URL.

拟入：独立置信commit不保联合一致→集合风险选择与预算中性local exchange→few-step commit策略；2+1+2=5；MULTIMODAL-GENERATIVE-PARADIGMS。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31198 — Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models](https://arxiv.org/abs/2610.31198)

Submission history From: Eliron Rahimi [view email] [v1] Thu, 22 Oct 2026 12:45:17 UTC (194 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Diffusion Language Models (DLMs) introduce unique quantization challenges due to their iterative denoising process. In this work, we reveal that quantization sensitivity is both taskand time-dependent, with different downstream tasks exhibiting distinct precision requirements across denoising steps. We further show that these patterns can be predicted without groundtruth labels or task-specific evaluation metrics. Building on these findings, we introduce T 2Quant, a task and time-aware mixedprecision quantization framework that uses a label-free sensitivity signal to optimally allocate activation precision across denoising steps under a fixed bit-width budget. Extensive experiments across three DLMs and six benchmarks demonstrate that T 2Quant consistently improves the average accuracy of existing quantization methods, achieving gains of up to 6.7 percentage points under the same budget.

拟入：统一bit不能适配task/time sensitivity→无标签信号分配denoise步精度→固定bit budget的配置选择；2+1+2=5；INFER-TENSORRT-LLM。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31576 — What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models](https://arxiv.org/abs/2610.31576)

Submission history From: Jinya Sakurai [view email] [v1] Thu, 22 Oct 2026 17:15:04 UTC (373 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Masked diffusion language models generate tokens in parallel, but their efficiency depends on which predictions are committed. Learned unmasking policies improve the speed--accuracy trade-off, yet differ in supervision, inputs, and capacity, obscuring which choices matter. We view supervised policies as distilling a decoding procedure through a teacher and examine independently what the teacher labels as committable, on which states the policy imitates it, what the policy observes, and how much the number of function evaluations (NFE) must decrease to offset policy overhead. We find that labeling predictions matching the final output is overly permissive at low NFE, and hidden states are weak alone but can complement confidence. About a 10% NFE reduction suffices to offset policy overhead for policies up to 7.5M parameters across tested settings. We therefore train a policy on trajectory-contraction targets, which accept only commitments staying on a reference trajectory, using confidence and hidden states. On LLaDA-8B-Instruct, the resulting 856K-parameter policy achieves the best accuracy--NFE frontier and highest throughput on GSM8K, is competitive at moderate targets on MATH-500 and HumanEval, and largely transfers to Dream-7B-Instruct.

拟入：learned unmasking标签、状态和容量混杂→控制研究指出最终输出匹配过宽、overhead盈亏点→teacher目标/策略容量选择；2+1+2=5；MULTIMODAL-GENERATIVE-PARADIGMS。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30814 — DRILL: Training World Models to Improve Policies, Not Predict Pixels](https://arxiv.org/abs/2610.30814)

Submission history From: Zhaolu Kang [view email] [v1] Thu, 22 Oct 2026 06:40:31 UTC (2,454 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:World models are increasingly used to reduce environment interaction when post-training vision-language-action (VLA) policies with reinforcement learning. Yet they are typically trained to predict pixels one step ahead, even though their role here is not merely to render visually faithful videos but to produce learning signals from imagined rollouts that improve the policy. We show that this mismatch is substantial: lower pixel MSE can produce worse policy gradients, and a world model trained for policy utility can yield better downstream policies despite 17% higher pixel MSE on the next frame. We propose the Downstream-Return Imagination Learning Loop (DRILL), a bilevel framework that updates the world model to maximize the policy's return after an inner GRPO update on imagined rollouts. DRILL has two instantiations. DRILL-VWI is a closed-form surrogate, requiring no additional simulator rollouts, that reweights prediction errors by policy visitation, the group-relative GRPO advantage, and model confidence. DRILL-IMG is a full meta-gradient method that differentiates through the inner update using truncated Hessian-vector products. We show that DRILL-VWI recovers the local one-step component of the DRILL-IMG meta-gradient under score-compatibility and small-residual assumptions. Across five manipulation simulators and two VLA backbones, DRILL-IMG raises mean success rate by 13.1 points over WMPO and 7.9 points over RLVR-World, and complements RLVR pretraining rather than competing with it. More broadly, we believe video world models for VLA reinforcement learning can be productively trained by the policy gradients they produce, not only by pixel-level prediction.

拟入：低pixel MSE未必好policy gradient→对GRPO内更新后return作双层优化→world-model训练目标从画面到决策用途；2+2+2=6；MULTIMODAL-WORLD-MODELS。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30320 — Self-Distilling Future Video Representations for World Action Models](https://arxiv.org/abs/2610.30320)

Submission history From: Suhyeok Jang [view email] [v1] Wed, 21 Oct 2026 18:33:13 UTC (2,967 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:World Action Models (WAMs) have emerged as a promising approach to learning generalist robot policies using rich spatiotemporal priors from pre-trained video diffusion models. A recent line of WAMs improves inference efficiency by conditioning a separate action decoder on intermediate future video representations extracted from a single denoising step, avoiding costly iterative denoising required for video generation. This design makes action prediction depend directly on the quality of these future representations. In this paper, we introduce Future REpresentation learning via self-Distillation with temporal context (FRED), a framework that trains WAMs to improve the quality of future video representations from noise in a single denoising step. Specifically, FRED uses self-distillation to predict future representations from noise, using representations extracted from ground-truth future observations as targets. We further condition the video model on historical observations, providing temporal context for predicting future representations better. Across diverse real-world manipulation scenarios, FRED consistently outperforms competing WAMs. It achieves particularly large gains on long-horizon and out-of-domain tasks under zero-shot environment generalization, and substantially improves human-to-robot skill transfer, reaching 50.0% task success on tasks absent from robot training data and demonstrated only in human videos, compared with 19.4% for the best competing WAM.

拟入：单步未来latent决定action质量→GT未来表征self-distill+历史条件→无需反复视频denoise的WAM表征训练；2+1+2=5；MULTIMODAL-EMBODIED-VLA。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30735 — When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies](https://arxiv.org/abs/2610.30735)

Submission history From: Luca Nunziante [view email] [v1] Thu, 22 Oct 2026 05:05:29 UTC (3,383 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Flow matching is now the dominant approach for vision-language action (VLA) robot policies, thanks to its expressiveness and simple training objective. However, inference for standard flow matching requires iteratively solving an ODE, limiting the control frequency at deployment. While several works have proposed novel methods to allow for single-shot action generation, we ask whether such additional objectives are actually necessary. We find that across six flow matching VLAs, one-step action generation largely matches multi-step sampling at scale: multi-step integration confers little to no consistent advantage at inference. We empirically find that this holds as long as models are sufficiently trained and have enough capacity. Practically, the implication is that for large VLAs, the single-step policy comes essentially for free from the multi-step model, enabling low-latency deployment without retraining, distillation, or auxiliary objectives.

拟入：默认flow policy多步ODE必要→六VLA充分训练/容量下单步近似反证→是否值得蒸馏/多步采样；2+1+2=5；MULTIMODAL-EMBODIED-VLA。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31423 — FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models](https://arxiv.org/abs/2610.31423)

Submission history From: Huixin Xu [view email] [v1] Thu, 22 Oct 2026 15:25:02 UTC (1,657 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation. Since reliable manipulation requires sufficient observation of objects, end-effectors, and their spatial relationships, multi-view inputs are widely used to provide complementary spatial information. However, our experiments show that existing VLA models do not fully exploit such multi-view complementarity. The policy tends to persistently rely on the wrist view, lacking the ability to dynamically adjust global-local view dependency across manipulation stages, which limits stage adaptability and robustness. To address this issue, we propose FocusVLA, a stage-aware multi-view routing framework. FocusVLA predicts future interaction intent from historical actions and uses it to guide dynamic view routing during action generation. By adaptively coordinating global and local observations across different task stages, FocusVLA improves multi-view utilization. On RoboTwin 2.0, FocusVLA improves the average success rate over the strongest baseline $\pi_{0.5}$ by 10.10 pp. In real-world evaluation, FocusVLA improves the success rate from 71.7\% to 85.0\%, achieving a 13.3\% gain over $\pi_{0.5}$. Moreover, the intent prediction and dynamic routing modules of FocusVLA can be integrated into existing VLA frameworks without modifying their core architectures.

拟入：多视角输入仍固定依赖wrist→历史action预测future intent驱动stage routing→任务阶段感知观测选择；2+1+2=5；MULTIMODAL-EMBODIED-VLA。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31613 — Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models](https://arxiv.org/abs/2610.31613)

Submission history From: Atiksh Bhardwaj [view email] [v1] Thu, 22 Oct 2026 17:40:19 UTC (4,987 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Vision-Language-Action (VLA) models can perform diverse manipulation tasks directly from visual observations and natural language instructions, but they remain prone to mistakes and unpredictable failures. Deploying these policies without continuous human supervision will require robust runtime monitors that detect when the policy has gone off-course. Existing monitors use external foundation models, such as vision-language models (VLMs) to supervise the policy, introducing significant complexity and computational cost for monitoring at runtime. In this work, we investigate an alternate approach: \textit{can a VLA's own internal activations provide the information needed to monitor its execution?} Our method trains linear probes on policy activations from demonstrations to estimate progress, then flags executions that deviate from expected progress. In experiments with the open-source VLA $\pi_{0.5}$ and across simulated and real-world manipulation tasks, this approach is competitive with or outperforms VLM-based monitors in task failure detection, as well as methods which require failure data for training. These findings suggest that simple probes of VLA internals can be used to develop reliable runtime monitors, opening a path toward building policies that can act reliably and monitor their execution without external foundation models.

拟入：external VLM监控成本高→demo上训练activation progress线性probe→不要求failure训练集的runtime failure检测；2+1+2=5；MULTIMODAL-EMBODIED-VLA。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30635 — What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks](https://arxiv.org/abs/2610.30635)

Submission history From: Ding Fei [view email] [v1] Thu, 22 Oct 2026 02:56:44 UTC (590 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Coding-agent benchmarks often describe a task in natural language but grade it with tests taken from the upstream project. Passing those tests can require information the description never states: a constant's name, a module path, an exact message. We call this a specification-oracle gap: where it exists, a benchmark also measures whether an agent reproduces upstream implementation details. We formalise the gap, including the inconsistencies that chains of dependent tasks add, and build a static audit for five languages that classifies every name-, path- and literal-level dependency of every scored test (held-out precision 89.2%, recall 92.9%). On SWE-Milestone (98 graded milestones, 35 published runs), 25 milestones contain a test that depends on an unstated, non-inferable name or path. Build units with such a dependency fail in 80.6% of runs, against 48.4% for comparable units without one, and withholding a single hidden name from the reference stops its unit's tests from compiling in 126 of 128 cases. The leaderboard's ranking is robust to removing the affected tests, but they shift scores within repositories and favour agents that reproduce upstream names. Across four further benchmarks, prevalence appears to follow construction: a third or more of the tasks are affected where specifications are release notes or LLM summaries, almost none where tasks are screened or written for their tests; how much a gap costs depends on how the harness grades. We release the audit, corrected filter lists and specification addenda.

拟入：test pass混入未在spec公开的名字/路径→静态audit和隐藏名干预→benchmark测任务还是upstream复现；2+2+2=6；PLATFORM-EVALUATION-SYSTEM。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31019 — Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking](https://arxiv.org/abs/2610.31019)

Submission history From: Yuning Bian [view email] [v1] Thu, 22 Oct 2026 09:54:17 UTC (109 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Chunking strategies for retrieval-augmented generation are almost always evaluated on a static snapshot, yet the documents underlying a knowledge base continue to change. Because chunks are embedded independently, a boundary that moves after an edit forces unchanged text to be re-embedded. We measure this update cost on 120 pairs of adjacent Chinese and English Wikipedia revisions for three stateless chunkers (non-overlapping fixed-size, recursive paragraph-first, and content-defined chunking) under a strict byte-identical reuse rule and a frozen dense encoder. On the 116-article common-success pool, with frozen, length-calibrated parameters, fixed-size chunking recomputes 57-68% of its full new-version embedding-input workload, recursive chunking 38-56%, and content-defined chunking 43-54% (it failed on 4 of 62 Chinese articles), while at these parameters mean evidence recall under a fixed 2048-token retrieval budget differs by less than two percentage points within either language. A cost-only parameter grid shows that the ranking of the two content-aware chunkers changes with chunk-length settings, whereas non-overlapping fixed-size chunking has the highest recomputation cost in every length-matched condition. Controlled edits and a verbatim-presence diagnostic support boundary drift as one contributor to recomputation of text already present in the previous version. Update cost is therefore a substantial, parameter-sensitive dimension that static retrieval evaluations do not expose and that should be reported alongside retrieval quality.

拟入：静态检索质量忽略edit后boundary drift→真实修订字节复用与固定token预算比较→chunker质量/更新成本共选；2+1+2=5；AGENT-RAG。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30612 — The Fusion Tax: A Diagnostic Analysis of When Hybrid Retrieval Hurts](https://arxiv.org/abs/2610.30612)

Submission history From: Aaditya Chauhan [view email] [v1] Thu, 22 Oct 2026 02:24:08 UTC (308 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Hybrid retrieval, which fuses a sparse lexical retriever with a dense neural one, is widely recommended in the software documentation surveyed in September 2026, usually with reciprocal rank fusion (RRF), on the strength of aggregate gains. We ask what fusion costs on individual queries, treating "do not fuse" as a first-class outcome, in the setting in which hybrid retrieval is deployed: a standard Anserini BM25, five dense encoders spanning 22M-596M parameters and three model generations, a learned-sparse (SPLADE) alternative, and a cross-encoder second stage, on seven BEIR datasets and three fusion functions. Even the best method, dense-weighted score interpolation, ranks relevant documents below the better of its two components on 13-48% of queries and below the deployable dense-only retriever on 8-21% (14-48% and 11-25% at a weight selected under leave-one-corpus-out validation), while beating dense-only in aggregate on every corpus with the primary encoder; the downside is significant under loss-averse risk-sensitive evaluation on six of the seven corpora. We call this loss the fusion tax. It is mostly a ranking effect that preserves recall in aggregate, it is most likely on the queries that only one retriever covers, and it persists across the encoder ladder and the SPLADE substitution. RRF carries the higher tax wherever the dense retriever is clearly stronger and only beats dense-only where the two components are balanced. Fusion failure is weakly predictable within a corpus but transfers unreliably across corpora, because the features that predict it change sign with the sparse-dense balance. A cross-encoder recovers part of the tax only where it is itself reliable. We distill these findings into guidance that keys the fusion decision to the measured sparse-dense balance of the target corpus.

拟入：aggregate hybrid增益遮蔽per-query损害→多encoder/跨corpus控制反例→融合应以target sparse-dense balance而非默认RRF选择；2+1+2=5；AGENT-RAG。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31446 — When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents](https://arxiv.org/abs/2610.31446)

Submission history From: Jiaqi Zhang [view email] [v1] Thu, 22 Oct 2026 15:43:50 UTC (470 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Long-lived agents act on memory carried across sessions, and many of their actions are irreversible, so a stale memory can turn directly into harm. Existing work improves the memory itself --- retrieving, refreshing, or reconciling entries --- yet whether an entry must be re-checked before acting is not a property of the entry: the same remembered address can be used unchecked for a routine shipment but should be re-confirmed before a valuable one. We therefore study \emph{action-conditioned memory verification}: given a candidate action, decide which of its memory premises to re-verify and when to proceed or abstain, balancing execution risk, abstention, and verification cost. We formulate this as a sequential stopping problem, in which a verification is worth its cost only if it can change what the agent does next; under suitable verifier reliability and cost conditions, increasing action consequence can move the same memory through proceed, verify, and direct-abstention regimes. Building on this formulation, \textsc{AMV-Guard} is a practical verification gate that extracts the premises a candidate action rests on, calibrates beliefs about whether they are wrong, and selects checks by bounded value of information (VOI). On ToolSandbox, relative to a static policy given the same inputs, it lowers mean verification cost by 33.9\% while keeping 100\% safe-proceed recall and 0\% Gate harmful, and raises Proceed coverage from 38.83\% to 44.17\%; in a gate-core transfer to AppWorld, which carries over the stopping/VOI core but not the full structured pipeline, it lowers verification cost by 21.3\% at a small cost in safe-proceed recall and task success. These results suggest that verification effort should be set by what an agent is about to do, not only by how reliable a memory appears.

拟入：memory可靠度本身不决定是否可行动→action-conditioned VOI stopping→核验/执行/弃权随后果变化；2+2+2=6；AGENT-MEMORY。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30769 — LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades](https://arxiv.org/abs/2610.30769)

Submission history From: Farnoosh Hashemi [view email] [v1] Thu, 22 Oct 2026 05:42:55 UTC (12,860 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic Music Lab experiment, we tested this vulnerability in large populations of LLM agents that recommended unfamiliar songs, with or without exposure to cumulative recommendation counts. Exposure led to runaway cascades that generated extreme and unpredictable collective recommendations increasingly divergent from a song's intrinsic appeal. Compared to humans, LLM populations were generally far more susceptible to herding behavior, and unlike humans, LLM cascades were less able to self-correct. This vulnerability has implications for multi-agent collaboration in recommender systems, automated evaluation, complex problem-solving, and unauthorized conspiracies.

拟入：multi-agent看见累计建议会内生放大→控制暴露/不暴露MusicLab实验→协作不等于独立多样证据；2+1+2=5；AGENT-MULTI-AGENT。需防把song模拟外推生产。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31355 — Muffin - A Shared Memory Buffer for Asynchronous AI Agents](https://arxiv.org/abs/2610.31355)

Submission history From: Ping-Lin Kuo [view email] [v1] Thu, 22 Oct 2026 14:36:46 UTC (3,916 KB)。精确v1；当前abs无withdrawn/retracted轻量命中；本日官方new/cross-list身份已定位。

Abstract:The rise of Agentic AI systems has changed the landscape of artificial intelligence by enabling strong reasoning capabilities through specialized multi-agent interaction with structured self-reflection. However, in target-driven reasoning tasks, single- and multi-agent systems are often on par in terms of performance gains. A major challenge is that failures often arise from an ineffective exchange of critical information during inter-agent interaction and coordination. Different from existing multi-agent debate paradigms that rely on synchronous turn-taking and sharing information across different agents, we propose an inter-agent protocol based on shared Memory bUFFer INference - referred to as MUFFIN - in an asynchronous agentic framework. In the first step, an orchestrator routes queries based on their reasoning demands and delegates demanding ones to a multi-agent setting, where a shared memory buffer provides asynchronous exchange of intermediate findings while an agent's private reasoning remains local. Our experiments show that our framework Muffin outperforms established competitors, achieving the best accuracy in 17 out of 20 of our benchmark settings, and provides a better quality-cost trade-off than multi-agent debate: Muffin improves accuracy by 19.2 accuracy points while using 77.4% fewer tokens, without requiring full-trace sharing.

拟入：同步debate/full trace共享成本→共享摘要buffer而private reasoning local、异步交换→quality/cost归因是否真由buffer产生；2+1+2=5；AGENT-MULTI-AGENT。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。



### [2610.30161 — TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents](https://arxiv.org/abs/2610.30161)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Prashant Devadiga [view email] [v1] Wed, 30 Sep 2026 15:16:21 UTC (272 KB)。

Abstract:Many Indian banks serve customers through FAQ pages and scripted chatbots. Assistants based on language models could respond faster and carry out requests such as blocking a card, but only if they give correct information and follow the bank's rules. These rules prescribe a procedure, a set of required steps, such as obtaining a closure quote before closing a deposit. Adapting models to this domain requires measuring how well they follow the procedure, before and after training. Benchmarks usually judge only the records left at the end of a conversation. Many required steps, however, leave the records unchanged, so an assistant that skips them can still be judged successful. We present TauIndianBankBench, an action-oriented benchmark of 1,000 Indian retail-banking tasks where an assistant helps a simulated customer. Besides the final records, it checks that the assistant took every required step and made no unrequested change. For every model, 6.5-12.0% of sessions are judged successful when only the final records are checked, although the assistant skipped a required step or made an unrequested change. Scoring both procedure and outcome shows more accurately how well language models perform in Indian retail banking.

拟入：仅终态判成功会漏掉不改变状态的必要步骤；新增过程/结果并审的实证盲区。拟分2+2+2=6；owner PLATFORM-EVALUATION-SYSTEM。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30151 — The Cost of Saying Hello: An Empirical Study of Handshake Overhead in AI Agent Communication Protocols](https://arxiv.org/abs/2610.30151)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Pranav Varshney [view email] [v1] Wed, 12 Aug 2026 03:51:22 UTC (52 KB)。

Abstract:Every interaction between AI agents begins with a handshake: the initiating agent must locate its counterpart, learn what it can do, and establish a session before the first useful message can be sent. Surveys of agent communication protocols name handshake overhead as an efficiency criterion, yet none report measurements. This paper presents the first empirical, phase-decomposed benchmark of the handshake in three major agent protocols: MCP (in both its 2025 initialize and 2026 discover eras), A2A, and ACP. Using each protocol's official SDK, we instrument every request for round trips, per-phase latency, wire bytes, and token cost across cold-start, warm-repeat, capability-mismatch, and degraded-metadata scenarios (N=50 per cell, on loopback and under an emulated 50 ms RTT). Round-trip count dominates handshake cost. A legacy MCP handshake takes three round trips and 230 ms at 50 ms RTT; A2A needs one round trip and 61.0 ms. Round trips are not the whole bill: when an LLM reads the counterpart's metadata, handshake cost scales with the counterpart's capability inventory at 24-107 tokens per capability, so a 200-capability counterpart spends 11% of a 200k-token context window before the agent reads its own task. MCP's own 2026 revision cuts its handshake from three round trips to two and, with era pinning, to zero on warm reconnects, protocol evolution that corroborates the cost we measure. We release the full harness, raw data, and analysis at this https URL.

拟入：握手开销从泛泛延迟拆为RTT、重连、元数据上下文消耗，可改变长能力目录协议选型。拟分2+2+2=6；owner AGENT-MCP。具体协议2026版本真实性仍需正文/官方规范核验，不能采用摘要版本宣传。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30157 — MCP vs CLI for AI Agents: A Comparative Analysis of Tool Integration Strategies for Autonomous Systems](https://arxiv.org/abs/2610.30157)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Arun Malik [view email] [v1] Wed, 29 Jul 2026 05:45:07 UTC (212 KB)。

Abstract:AI agents require interfaces to interact with external systems such as files, APIs, databases, and cloud services. Two competing paradigms have emerged: CLI (Command Line Interface), where agents execute shell commands directly, and MCP (Model Context Protocol), a structured JSON-RPC protocol providing governed, typed tool access. This paper presents a comparative analysis across 14 evaluation dimensions, supported by worked examples, security assessment against established compliance frameworks, and economic modeling. Our analysis indicates that CLI provides superior efficiency for single-user, local-only workflows, while MCP addresses requirements that CLI fundamentally cannot satisfy, including fine-grained access control, credential isolation, structured audit, and multi-tenant governance. We further examine how progressive disclosure techniques eliminate MCP's historical weakness (context window overhead), yielding token efficiency comparable to CLI while preserving its architectural benefits. A hybrid architecture is recommended for production systems. This analysis draws upon academic, government, and industry sources including NSA formal guidance (CSI U/OO/6030316-26), OWASP security standards, and economic modeling from BCG and Gartner.

拟排：完整摘要给出14维观点比较、worked examples与经济建模，但未显示隔离CLI包装、安全治理实现与协议本身作用的新机制或可归因证据；CLI无法满足权限隔离的普遍断言也不足采用。非因为主题或不够高分排除。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30206 — MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.30206)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Minsang Kim [view email] [v1] Wed, 21 Oct 2026 13:06:30 UTC (5,660 KB)。

Abstract:Mixture-of-Experts (MoE) language models scale model capacity efficiently by activating a small subset of parameters per token. However, in long-context inference, memory remains a major bottleneck because the KV cache grows linearly with sequence length. Existing KV cache compression methods reduce this cost for dense transformers, but overlook a problem specific to MoE: KV eviction can change which experts are selected during answer generation, degrading the generation quality. We propose MoEZip, a routing-aware KV cache compression for sparse MoE language models. To estimate the sensitivity of expert routing to perturbation, we propose a novel metric based on the Fisher information matrix of routing distributions. MoEZip combines this metric with attention weights for routing-aware scoring of contexts. Finally, we compose a complementary scoring system that combines eviction methods for dense and sparse-MoE architectures. Experiments show that MoEZip achieves robust performance under aggressive cache compression on various benchmarks. At a KV retention ratio of 10\%, MoEZip improves over the SoTA baseline by +24 and +20 points on average on LongBench and RULER, corresponding to 2.3$\times$ and 4.9$\times$ higher scores, respectively.

拟入：dense attention重要性不足保MoE路由；Fisher路由敏感度与attention联合评分改变KV逐出选择。拟分2+2+2=6；owner INFER-KV-CACHE。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30868 — uGDS: A User-Space Development Kit for High-Performance GPU Direct Storage](https://arxiv.org/abs/2610.30868)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Wei Jing [view email] [v1] Thu, 22 Oct 2026 07:45:58 UTC (453 KB)。

Abstract:Data-intensive GPU applications increasingly rely on NVMe SSDs to extend GPU memory. NVIDIA GPU Direct Storage (GDS) enables direct SSD-GPU transfers via PCIe peer-to-peer DMA, eliminating host staging. However, GDS retains three key limitations: (1) its control path traverses the kernel for every I/O request, introducing software overhead; (2) its stream-ordered path imposes strict total ordering even when workloads only require batch-level ordering; and (3) its closed-source user-space engine hinders diagnosis and custom scheduling.
We present uGDS, this https URL, an open-source user-space GPU Direct Storage library built on four principles: user-space control, unified cross-vendor abstraction, workload-aware scheduling, and end-to-end transparency. The host CPU manages the entire NVMe command lifecycle in user space, while payloads move via PCIe P2P DMA without consuming GPU compute. A minimal kernel module (this http URL) is used only for one-time privileged setup. uGDS partitions hardware queues between synchronous and batch traffic, enforces DMA-safe buffer lifetimes, and provides cuFile-compatible synchronous, batched, and stream-ordered APIs with polling or interrupt completion on both NVIDIA CUDA and AMD HIP.
Evaluated on an A100 with a Samsung 990 PRO, uGDS achieves up to 12.12x GDS's batch-read bandwidth and 30.69x its batch-write bandwidth (8- and 4-KiB requests, batch size 128), and reduces 4-KiB synchronous write latency by 84.1% with two threads. Its stream-ordered path sustains 5.49 GiB/s on a single stream, where GDS retains only 40.8% of its synchronous bandwidth. In LMCache, uGDS reduces median time-to-first-token (TTFT) by up to 62.7% and raises serving goodput by 2.63x. On AMD, uGDS achieves up to 1.19x hipFile's synchronous-write bandwidth.

拟入：host用户态控制与PCIe P2P数据路径分离、队列分区与生命周期约束，可改变SSD扩展KV的控制开销边界。拟分2+2+2=6；owner INFER-GPU-MEMORY。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.30552 — Repair Changes Which Layers to Remove: Exact Optima for Depth Pruning of Language Models](https://arxiv.org/abs/2610.30552)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Jianchang Su [view email] [v1] Thu, 22 Oct 2026 00:18:10 UTC (72 KB)。

Abstract:Depth pruning removes entire transformer layers to make large language models faster, and recent methods recover quality by replacing the removed layers with a training-free linear map. Which layers to remove, however, is chosen with heuristic scores whose distance from the best choice is unknown. We evaluate every subset of layer groups exactly (about 53,000 pruned models across four families, with and without repair) and find that the best layers to remove depend on the repair: linear repair absorbs the interaction among nearby layers and turns the optimum from a split layout into a contiguous block, so methods that choose layers without the repair miss the repaired optimum by up to 189%. We therefore select layers under the repair that will be applied. A greedy search at the cost of SLEB lowers perplexity by 20% to 66% relative to ReplaceMe on five models up to 27B parameters, and with a task objective it is up to 25 points more accurate given the same data. A second-order expansion of the loss yields a score that selects the repaired block from one forward and one backward pass of the intact model.

拟入：剪层选择必须在repair算子下评价；精确小空间枚举给出先选再修失败的证据，改变优化目标。拟分2+1+2=5；owner INFER-TENSORRT-LLM。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。

### [2610.31479 — Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon](https://arxiv.org/abs/2610.31479)

精确版本：v1。官方列表：本日new/cross-list；原始版本记录：Submission history From: Kyrylo Yemets [view email] [v1] Thu, 22 Oct 2026 16:04:40 UTC (2,021 KB)。

Abstract:Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads. Which optimizations retain their benefits when moved to Apple Silicon, and what determines their applicability? We evaluate four optimization families: KV-cache pruning, speculative decoding, ported GPU kernels, and post-training quantization. Experiments span four Apple machines under a common single-request decode workload, with matched RTX 4090 comparisons where possible. KV-cache pruning can reach up to 1.75 times end-to-end throughput on Apple but can reduce throughput on desktop NVIDIA GPUs. Under the common benchmark, all evaluated speculative decoding methods reduce throughput on Apple, despite reported 2-6 times gains on server GPUs. CUDA kernel designs transfer only partially: public Metal lacks asynchronous copy, and batch-one decode makes several serving-oriented mechanisms inapplicable, although transferable components yield up to 1.20 times decode throughput. Quantization gains vary by machine. Across four families, a reported speedup is not a portable property of a technique alone but a joint function of technique, runtime, hardware contract, and workload regime.

拟入：共同batch-one workload对四类加速作平台迁移反证；不是以局部/负面结果拒收。拟分2+2+2=6；owner INFER-SPECULATIVE-DECODING（具体owner由root按采用命题收窄）。

当前审阅状态见上方证据段及REVIEW；此处仅保留初筛题摘与原判断。


