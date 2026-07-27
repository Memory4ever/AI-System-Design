# AI Research Weekly — 2026-W02

> Coverage Window: 2026-01-05～2026-01-11
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Discovery Recall Re-audit: 2026-08-07
> Books Integration Review: 2026-08-13 — 5/5 dispositions complete; Discovery Recall remains open

## Executive Summary

原周报只保留了 NVIDIA 的组合发布，遗漏了四篇直接触及 AI System 机制的论文。补充检索与
全文核验后，本周更重要的长期信号是四种不同层次的“间接性”：MoEBlaze 用 compact routing
metadata 代替 materialized routed activations；kNN-MoE 在冻结 parametric router 的前提下以
retrieval memory 修正 expert assignment；AIConfigurator 用 calibrated operator database 与
iteration model 代替对每个 serving configuration 的 GPU 穷举；Crystal-KV 以 attention-derived
recency/frequency state 代替保留全部 reasoning KV。四者都以新增状态换取更低的在线或训练成本，
也分别引入 metadata scaling、reference-set drift、calibration freshness 与错误 eviction 风险。

## Coverage and Source Coverage

- 模型与研究机构：固定顺序扫描后保留 NVIDIA open models / data / tools 发布。
- 论文与学术来源：重新检查 arXiv 2026-01 的 `cs.CL`、`cs.DC` 及其 `cs.LG/cs.AI`
  cross-list，恢复 Routing by Analogy、Crystal-KV、MoEBlaze 与 AIConfigurator。四篇均已回到 arXiv
  abstract、HTML 全文和 revision history，而不是用推荐页或搜索摘要支撑结论。
- AI Infra：NVIDIA 生态发布仍属于 portfolio fact；AIConfigurator 的 framework adapter 与
  launch-file generation 属于论文实现，不等同于 vLLM、SGLang、TensorRT-LLM 或 Dynamo
  官方承诺。
- 国内机构与部分历史页面、`cs.AI/cs.LG` 月度目录的完整枚举仍受访问限制；本周完成的是
  已命中来源的候选恢复与全文 Gate，不宣称目录级全量召回已经关闭。

## Discovery Recall Reconciliation

- **Original retained:** 1（NVIDIA portfolio）。
- **Newly recovered at `>=20/30`:** 4（Routing by Analogy、Crystal-KV、MoEBlaze、AIConfigurator）。
- **Cross-list / revision deduplication:** 四篇论文均按 arXiv ID 去重；Routing by Analogy 的
  2026-05-25 v2 只用于核验 revision，不创建 W21 新事件。
- **Full Source Reviews:** 5/5 retained candidates 已有非模板化 packet；其中四篇恢复论文均
  覆盖 method、implementation、evaluation、limitations/future work 与关键 appendix 入口。
- **Unresolved:** arXiv 月度目录不能在当前环境中形成机器可复算的全类别 hit census，故 W02
  Discovery Recall Gate 仍为 `Open — Partial Recall Repair`；这不影响已恢复候选的来源真实性。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| NVIDIA open models, data and tools | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching；Weekly only |
| Routing by Analogy / kNN-MoE | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Experimental；Refine Ch21 |
| Crystal-KV | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Experimental；Refine Ch45 |
| MoEBlaze | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Integrate Ch49 |
| AIConfigurator | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Integrate Ch56 |

## Full Source Review

### NVIDIA open models, data and tools

- **Candidate / Week / Score:** NVIDIA open models, data and tools / 2026-W02 / 23/30；
  `Source Family ID: nvidia-ces-2026-open-asset-portfolio`。
- **Source Type / Dates:** NVIDIA 官方组合发布；2026-01-05 首次公开，本轮访问
  2026-08-01。它不是一篇统一 technical report，也不是单一模型 release。
- **Direct / Related Primary Sources:** 官方发布页及其链接的 Nemotron、Cosmos、Alpamayo、
  GR00T、Clara、GitHub、Hugging Face 和 NIM 入口；未使用 CES 媒体转述支撑机制。
- **Access and Full-read Coverage:** Verified as official portfolio fact；已检查资产类别、开放
  data/code/model 入口、deployment 入口与厂商采用说明。各子项目的训练、评测和生产拓扑没有
  统一披露，故为 `Mechanism Not Disclosed` at portfolio level。
- **Problem / Previous Design / Changed Constraint:** 单独发布 weights 便于模型试验，却把 data、
  training recipe、domain tooling、evaluation、license 与 runtime compatibility 留给使用方拼接；
  多垂直领域交付使这些对象需要作为同一资产供应链治理。
- **Mechanism / Ownership / Flow:** 官方可验证的是多个独立 asset families 经 GitHub、Hugging
  Face、build.nvidia.com 与 NIM 交付；不能据此推断它们共享 registry schema、训练 pipeline、
  control plane 或 production evidence graph。
- **Implementation / Evaluation Contract:** 页面包含若干厂商 benchmark 与 adoption case，但不同
  model、dataset、hardware、precision、length、batch、concurrency 和 SLO 不可合并；组合发布没有
  可比较的统一 ablation。
- **Evidence Boundary / Limitations:** 证明 NVIDIA 同日交付模型、数据、代码和部署入口；不证明
  “open”拥有同一 license/provenance，也不证明生态资产在任意平台上可互换或达到生产就绪。
- **Trade-offs / Previous Design Still Applies:** 组合生态减少 discovery 与 bootstrap 成本，却扩大
  license、lineage、compatibility、security scanning 和 version coupling；只交付最小 weights 的路径
  在研究复现与跨厂商 runtime 中仍更中立。
- **Evolution / ROADMAP:** `Layering / Dependency`；`PLATFORM-FOUNDATIONS` 为主 owner（当前
  Ch57 / Legacy Ch53），相邻 `PLATFORM-MODEL-REGISTRY`（Ch59 / Legacy Ch55）与
  `PLATFORM-PRODUCTION`（Ch73 / Legacy Ch69）。已读当前 Ch57～59、Ch73；现有章节已经把模型、
  数据、runtime 与 evidence 视为不同平台对象。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；不修改
  Books。开放资产组合是厂商案例，不足以形成新的平台机制。
- **Open Questions:** 是否会出现跨模型、数据与 runtime 的统一 SBOM、license、lineage、EvalSpec
  和 compatibility manifest？

### Routing by Analogy / kNN-MoE

- **Candidate / Week / Score:** Routing by Analogy / 2026-W02 / 23/30；
  `Source Family ID: knn-moe-retrieval-augmented-routing`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 首次公开 2026-01-05，v2 修订
  2026-05-25，本轮访问 2026-08-07。事件归属 v1 所在 W02；v2 只补充核验，不重复计分。
- **Access and Full-read Coverage:** 已阅读 arXiv metadata、Introduction/Related Work、memory
  construction、adaptive routing、实验设置、baselines、ablation、latency/VRAM、limitations、
  conclusion 与相关 appendix 指针。
- **Original Problem / Previous Design / Changed Constraint:** frozen parametric router 在训练分布内
  成本低且行为稳定，但遇到 distribution shift 时不能利用已知相似样本的局部最优 expert
  assignment；逐请求优化 routing logits 或在线 fine-tuning 又把昂贵更新放回 critical path。
- **Mechanism / State Ownership / Flow:** 系统离线对 reference tokens 的 routing logits 做局部优化，
  以 hidden representation 为 key、局部最优 logits 为 value 建立 per-layer memory；在线检索 KNN，
  用平均相似度生成置信系数，在 continuous logit space 混合 parametric 与 retrieved logits，再做
  Top-K Softmax。reference memory 与 index 是新增状态；模型参数和原 router 保持冻结。
- **Implementation / Evaluation Contract:** 论文在 OLMoE、gpt-oss-20b 与 Qwen3-30B-A3B 上，使用
  GPQA、MMLU、SuperGPQA、USMLE、MedMCQA、MBPP 的 disjoint reference/test split，对比 zero-shot、
  retrieval 5-shot、full SFT 与 router-only SFT，并做 paired bootstrap。IVFPQ 使用 8-bit index、
  32 centroids 和 1/8 hidden dimension；硬件只明确披露 memory construction 使用单张 A100 80GB。
- **Evidence Boundary:** 作者实验支持在给定模型、六项 benchmark 和同分布 labeled reference set
  下改进 aggregate accuracy；部分单项差异不显著。它不证明 retrieval router 在开放域、强 shift、
  expert-parallel 通信或 production SLO 下普遍优于 frozen router / SFT。
- **Trade-offs / Failure Modes / Previous Design Still Applies:** retrieval 把在线优化换成 memory、index、
  provenance、refresh 和 per-token lookup；reference drift、错误 pseudo-label 与相似度失准会把错误
  assignment 注入 router。v2 报告 1k reference 时 IVFPQ 相对 zero-shot 约增加 3.67% latency、9.43%
  VRAM，但条件不能外推。无可靠 reference 或 tight latency budget 时原 frozen router 仍更合理。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`；主节点 `MODEL-MOE`，当前
  Ch21 / Legacy Ch21；相邻 `INFER-SCHEDULING`（当前 Ch56 / Legacy Ch52）与 `AGENT-MEMORY`
  （当前 Ch77 / Legacy Ch73）。已读 Ch20～22 与运行时 handoff。
- **Integration Decision:** `Refine — Existing Argument`；已在 Ch21 将 frozen parametric router
  扩展为“可选检索修正 + 置信度混合 + versioned memory + observable fallback”，并保留无可靠
  reference 或 tight latency budget 时原 router 的成立条件。
- **Open Questions:** memory 的 freshness、tenant isolation、delete/supersession、expert-parallel
  placement 与 rollback 怎样进入 router contract？

### Crystal-KV

- **Candidate / Week / Score:** Crystal-KV / 2026-W02 / 24/30；
  `Source Family ID: crystal-kv-answer-first-cot-eviction`。
- **Source Type / Dates / Revision:** arXiv primary paper v1，首次公开 2026-01-05，本轮访问
  2026-08-07。arXiv ID 的数值顺序不能代替 metadata 日期，因此归入 W02。
- **Access and Full-read Coverage:** 已阅读 metadata、CoT/KV compression background、answer-first
  observation、attention-based LRFU、adaptive layer/head budget、implementation algorithm、CodeForces /
  MATH-500 evaluation、baseline、parameter sensitivity、discussion 与 conclusion。论文没有独立
  Limitations / Threats 章节，且公开代码链接仍为 placeholder，记为 `Artifact Not Available`。
- **Original Problem / Previous Design / Changed Constraint:** FullKV 在短输出或 fidelity-first 场景中
  保留完整因果历史，语义最清楚；StreamingLLM/H2O/SnapKV 等按近期 token generation 的局部 attention
  近似做 eviction，也适合所有输出 token 都重要的普通生成。长 CoT 把大量 KV 放在隐藏 think stage，
  workload objective 变成最终 answer correctness，局部、均匀 token utility 假设因而受到挑战。
- **Mechanism / State Ownership / Flow:** 每个新 KV 先作为 PotentialKV；以当前 attention 的 top-p hit
  mask 更新 per-entry Combined Recency/Frequency score 与 last-hit time，cache 满时淘汰低 CRF 项；
  `lambda` 在 LRU 与 LFU 之间控制衰减。周期性 allocator 再按各 layer/head 的聚合 CRF / budget 调整
  容量。论文把最终保留项解释为 CrystalKV、被淘汰项解释为 SlipKV，但在线算法并不能直接观察
  “是否支持最终正确答案”，这仍是基于 attention pattern 的 proxy。
- **Implementation / Evaluation Contract:** DeepSeek-R1-Distill Llama-8B、Qwen-14B、Qwen-32B；
  CodeForces 仅保留 difficulty <1500 与 MATH-500，每题 temperature 0.6、top-p 0.95、`k=8` samples；
  workstation 为 3× NVIDIA RTX PRO 6000 Blackwell。长序列 throughput 表只使用 Llama-8B、总 HBM
  288 GB、平均约 9,350/18,700 tokens，并比较 FullKV 与 Crystal-KV 的 fixed/ratio budget。
- **Evidence Boundary:** 作者实验支持在上述 reasoning models、任务与采样条件下，CRF eviction 和
  adaptive allocation 在给定 budget 上优于所列 baselines；论文报告的 90.89% HBM saving、平均
  7.57× throughput 与最高 1.24× response speedup 必须与模型、序列、最大可并行 batch 的推导方式
  绑定。没有公开 artifact、线上 arrival/concurrency trace、tail SLO 或跨模型复现，不能把“answer-first”
  proxy 写成已证明的普适 KV 语义。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** eviction 不可逆，错误 proxy 会删掉
  延迟生效的证据；per-entry/per-head CRF、动态 budget 与不规则 KV 长度增加 metadata、kernel layout、
  fragmentation 和 calibration 成本。FullKV 在短 CoT、强 correctness contract 或内存充足时仍是基线；
  静态/均匀压缩在 hardware kernel 与 workload 更规则时仍可能更易优化。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution`：FullKV → token-uniform local-attention
  eviction → CoT-aware eviction → answer-oriented proxy + adaptive layer/head budget。主节点
  `INFER-KV-CACHE`，当前 Ch45 / Legacy Ch41；相邻 Ch47 PagedAttention、Ch54 GPU Memory 与 Ch56
  Scheduling。已读 Ch44～47，确认逻辑 utility 与物理 block management 的边界。
- **Integration Decision:** `Refine — Existing Argument`；已在 Ch45 的 Eviction/Offload 之后补入
  workload-aware eviction 演进，明确 attention 不是 causal oracle、错误淘汰不可逆，且 FullKV、
  静态策略、recompute/offload 在相应约束下继续成立。
- **Open Questions:** 如何用 causal intervention 而非 attention proxy 验证 answer contribution；跨请求
  batching、PagedAttention block、rollback 与 model/version drift 下怎样维护 CRF 和 budget contract？

### MoEBlaze

- **Candidate / Week / Score:** MoEBlaze / 2026-W02 / 27/30；
  `Source Family ID: moeblaze-materialization-free-moe-training`。
- **Source Type / Dates:** arXiv primary systems paper v1；首次公开 2026-01-08，本轮访问
  2026-08-07，无后续 revision。
- **Access and Full-read Coverage:** 已阅读 metadata、背景、forward/backward data flow、dispatch
  data structures、atomic-free construction、SwiGLU checkpoint/kernel co-design、完整实验、related
  work 与 conclusion/future work。
- **Original Problem / Previous Design / Changed Constraint:** token dropping/padding 用固定 capacity
  换取实现简单，dropless routing 保留模型质量却需要动态 compact/sort/materialize。随着 token 数、
  Top-K 和 hidden dimension 增大，routed activation 与 SwiGLU intermediates 的 HBM footprint / traffic
  成为瓶颈，稀疏计算不再自动意味着低内存成本。
- **Mechanism / State Ownership / Data Flow:** 不再为 dispatched tokens 建立完整 activation buffer，
  而是保存 expert-token indices、offsets、inverse token-expert mapping 与 position map；expert kernel
  从原始未排列 tensor on-the-fly gather，并在第二个 MLP 后直接 reduction。backward 复用 reverse
  mapping；SwiGLU 只 checkpoint 必要 intermediates，其余在 fused backward 中 recompute。
- **Implementation Detail / New State:** 为避免 global radix sort 和 atomic contention，论文构造
  `L × E` dense token-expert map，再做 per-expert count、prefix sum 与 tile-local scan。它减少大型
  routed activations，但 dense metadata 自身随 token 数与 expert 数增长，不能被描述成“无状态”。
- **Evaluation Contract:** 单张 NVIDIA H100，PyTorch 2.0.1、CUDA 12.1；七组 synthetic MoE layer
  configuration，input dimension 512～2048、4～16 experts、Top-K 1～4、batch 16/32、sequence
  512～2048；baseline 为 MegaBlocks。计时只覆盖一个 MoE layer 的 Sparse-to-Sparse forward +
  backward，排除 optimizer update；memory 用 saved tensor hooks 统计 activation。
- **Evidence Boundary:** 在上述单卡 micro/system-kernel contract 中，作者报告 SiLU speedup
  1.4×～3.7×、SwiGLU 2×～6.2×及配置相关的 activation savings。论文没有多节点 all-to-all、完整
  transformer、optimizer、收敛或 end-to-end training evidence；“可扩展到 distributed”是 future work。
- **Trade-offs / Failure Modes / Previous Design Still Applies:** 收益来自少 materialization、fusion 与
  recomputation，代价是 hardware-specific kernels、index construction、recompute 和更复杂 backward；
  小 L/K 时收益缩小。固定-capacity/padded path 在小模型、predictable load 或 portability 优先时仍合理。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution`：capacity/padding → dropless dynamic
  routing → materialization-free indexed routing。主节点从 provisional 的训练章节纠正为
  `INFER-TENSORRT-LLM` execution-plan owner（当前 Ch49 / Legacy Ch45）；Ch21 拥有 router 语义，
  Ch36/40 拥有训练并行与通信 handoff。已读 Ch21、Ch35～36、Ch40 与 Ch49～50。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch49 写入“activation materialization
  → compact metadata → on-the-fly gather/direct reduce → selective recomputation”的执行演进，并明确
  单卡单层结果不能外推到分布式端到端训练或收敛。
- **Open Questions:** `L × E` metadata 在数百 experts 与多节点下的上限是什么；如何与 all-to-all、
  load balance、expert capacity 和 fault recovery 共同工作？

### AIConfigurator

- **Candidate / Week / Score:** AIConfigurator / 2026-W02 / 28/30；
  `Source Family ID: aiconfigurator-slo-aware-serving-search`。
- **Source Type / Dates:** NVIDIA authors 的 arXiv primary systems paper v1；首次公开 2026-01-09，
  本轮访问 2026-08-07，无后续 revision。
- **Access and Full-read Coverage:** 已阅读 metadata、background/motivation、五段 workflow、static /
  aggregated / disaggregated models、operator decomposition/database、MoE correction、evaluation、
  case study、related work 与 conclusion。论文没有独立 limitations 或 ablation section，已显式记为
  `Not Disclosed`，不把缺失内容补写成事实。
- **Original Problem / Previous Design / Changed Constraint:** 手工 benchmark 在单一框架和固定
  workload 下直接可信，但 framework、parallelism、KV budget、CUDA Graph、chunked prefill 与 SLO
  组合形成巨大 configuration space；逐项起服务、加载权重和压测的成本随模型与 GPU 数增长。
- **Mechanism / Ownership / Control Flow:** offline PerfDatabase 按 hardware/framework 保存 GEMM、
  attention、communication 与 memory primitive measurements；TaskRunner 根据 workload descriptor、
  topology、SLO 和 valid flags 生成候选；InferenceSession 以 iteration/operator model 预测 TTFT/TPOT；
  Pareto Analyzer 筛选；Generator 输出 version-compatible launch file。推荐状态由数据库版本、模型
  spec、framework adapter、workload contract 与 SLO 共同决定，而非一个静态“最佳参数”。
- **Disaggregated Flow:** prefill/decode 分池时先分别估计候选，以 transmission correction 修正 TTFT，
  再用 `min(R_pre, R_dec)` 做 rate matching，并扫描 worker counts / GPU allocations；这说明 PD
  disaggregation 的配置问题是受 SLO 约束的双队列配平，不是固定拓扑选择。
- **Evaluation Contract:** aggregated fidelity 使用单个 8×H100 SXM 80GB 节点，Qwen3-32B dense FP8
  与 Qwen3-235B MoE FP8，TensorRT-LLM 1.0.0，并以 vLLM 0.11.0 做 Qwen3-32B cross-framework
  验证；ISL 128～4096、OSL 128～512、concurrency 4～128、TP/EP 1～8。disaggregated 部分使用
  两个各 8×Hopper/NVLink 节点、DeepSeek-V3 671B、TensorRT-LLM、ISL 5k/6k、OSL 1k、TTFT 5s。
- **Evidence Boundary:** 作者测得的 MAPE、Pareto 与 throughput improvement 只证明已校准 NVIDIA
  hardware、列明版本、模型与 workload 区间中的 selection fidelity；TTFT >1s outliers 被过滤，且
  disaggregated overall throughput MAPE 为 25.49%。不证明未校准 hardware/framework 或 workload
  drift 下仍准确，也不证明 disaggregation 通常优于 aggregation。
- **Trade-offs / Failure Modes / Previous Design Still Applies:** GPU 搜索成本被转移为离线 calibration、
  schema/adaptor maintenance、freshness detection 与 prediction error。kernel、scheduler 或 driver
  升级会令 database stale；modeling outlier 可能误删真实排队风险。新硬件、新 kernel 或强 tail-SLO
  场景仍需 silicon validation，不能取消 targeted benchmarking。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`：manual benchmark → analytical
  primitive model → calibrated iteration model → SLO-aware configuration search → generated launch
  contract。主节点 `INFER-SCHEDULING`（当前 Ch56 / Legacy Ch52），邻接 Ch49 execution、Ch55 PD
  Disaggregation 与 Ch57 Platform。已读 Ch55～57，避免把配置搜索混入毫秒级 iteration scheduling。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch56 增加慢时间尺度配置搜索，保留
  targeted silicon validation，补齐 calibration identity、prediction uncertainty、freshness、fallback
  与 rollback，未保留作者 benchmark 数字。
- **Open Questions:** calibration artifact 如何 version、失效检测和回滚；prediction uncertainty 如何
  进入 candidate pruning；tail queueing 与 failure recovery 如何纳入 model？

## Evidence Level

NVIDIA 页面可证明组合发布事实；四篇 arXiv 论文可证明作者公开的方法与受限实验。任何性能数
都绑定各自 hardware、model、precision、length、batch/concurrency 与 SLO/measurement contract；
单卡 MoE layer、已校准 serving search 和 labeled-reference routing 均不得外推成通用生产结论。

## Cross-Week Deduplication

后续单个 Nemotron、Cosmos 或 GR00T 更新按首次公开日期单独去重，不重复计算 1 月 5 日组合
发布；Routing by Analogy 的 v2 不作为新事件；后续 MoE routing/memory 与 configuration search
论文按 source family 比较 changed constraint，而不是仅按标题相似去重。
Crystal-KV 只按 2026-01-05 的 v1 metadata 计入 W02；后续 reasoning-aware KV work 应与 R-KV、RaaS、
KVzap 分清 objective、online signal 与 cache-layout constraint。

## Knowledge Tree Position

`MODEL-MOE`（Ch21）、`INFER-KV-CACHE`（Ch45 / Legacy Ch41）、`INFER-TENSORRT-LLM`
（Ch49 / Legacy Ch45）、`INFER-SCHEDULING`（Ch56 / Legacy Ch52）与 `PLATFORM-FOUNDATIONS`
（Ch57 / Legacy Ch53）。四篇论文分别提供 router memory、reasoning-KV eviction、conditional
execution data movement 与 serving configuration search，不应合并成一条直接替代路线。

## Recommended Action

五个候选已完成逐项 Books disposition 和周级反向检查。四篇机制论文已按单一 owner 融入现有论证；
NVIDIA portfolio 只保留为版本事实。W02 Discovery Recall Gate 仍为 Open，因此未来若恢复新候选，
必须重新打开本周 Source-Family Books Review，不能据本次结果宣称档案召回完整。

## Event-Date Daily Decision

2026-01-05、01-08、01-09：直接记入 Weekly；历史回填不创建 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete — 5/5 dispositions；Archive Discovery Gate Open`。

- NVIDIA portfolio：`Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；
- Routing by Analogy：`Refine — Existing Argument` → `MODEL-MOE` / Ch21；
- Crystal-KV：`Refine — Existing Argument` → `INFER-KV-CACHE` / Ch45；
- MoEBlaze：`Integrate — New Mechanism` → `INFER-TENSORRT-LLM` / Ch49；
- AIConfigurator：`Integrate — New Mechanism` → `INFER-SCHEDULING` / Ch56。

周级 Review 重新核对了五个 Source Family 的全文范围、日期/revision、性能条件、主 owner 与相邻章节。
反向检查确认正文没有把四篇作者实验写成普适结论，也没有用检索 router、reasoning eviction、indexed
execution 或预测式配置搜索覆盖原方案。

## Ignored Noise

未披露条件的横向 benchmark、CES 产品清单、二次媒体摘要，以及只在标题层命中但尚未完成
全文与 20/30 评分的论文；后者不得被当成已拒绝候选。

## Repository Changes

- 2026-08-07：补回四篇遗漏的 primary papers、评分、完整 Source Review 与 recall limitation；
  无历史 Daily 或 Books 修改。
- 2026-08-13：完成 W02 独立 Books Gate。更新 Ch21、Ch45、Ch49、Ch56；修正 MoEBlaze 与
  AIConfigurator 的 provisional owner；同步本周 disposition、章节映射与 evidence boundary。

## Open Questions

1. 开放模型生态怎样携带 dataset lineage、license、evaluation 与 runtime compatibility？
2. MoE routing memory 与 materialization-free dispatch 能否在 expert-parallel、多租户和动态负载下
   保持可验证的 correctness / freshness？
3. serving configurator 的 calibration freshness、prediction uncertainty 与 rollback 应由谁拥有？
4. reasoning-aware KV eviction 的 semantic proxy 怎样与 block layout、batch scheduling 和 correctness
   rollback 共同设计？

## Sources

- NVIDIA, “NVIDIA Unveils New Open Models, Data and Tools to Advance AI Across Every
  Industry,” published 2026-01-05; accessed 2026-07-31:
  https://blogs.nvidia.com/blog/open-models-data-tools-accelerate-ai/
- NVIDIA Research archive: https://blogs.nvidia.com/blog/category/nvidia-research/
- Routing by Analogy, arXiv v1 published 2026-01-05, v2 revised 2026-05-25;
  accessed 2026-08-07: https://arxiv.org/abs/2601.02144 ;
  HTML reviewed: https://arxiv.org/html/2601.02144v2
- Crystal-KV, arXiv v1 published 2026-01-05; accessed 2026-08-07:
  https://arxiv.org/abs/2601.16986 ; HTML reviewed: https://arxiv.org/html/2601.16986v1
- MoEBlaze, arXiv v1 published 2026-01-08; accessed 2026-08-07:
  https://arxiv.org/abs/2601.05296 ; HTML reviewed: https://arxiv.org/html/2601.05296v1
- AIConfigurator, arXiv v1 published 2026-01-09; accessed 2026-08-07:
  https://arxiv.org/abs/2601.06288 ; HTML reviewed: https://arxiv.org/html/2601.06288v1
- arXiv January 2026 `cs.CL` / `cs.DC` monthly listings, accessed 2026-08-07:
  https://arxiv.org/list/cs.CL/2026-01 and https://arxiv.org/list/cs.DC/2026-01
