# AI Research Weekly — 2025-W38

> Coverage Window: 2025-09-15～2025-09-21
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：DRA resource health in Pod status、DRA consumable capacity。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 本组无达到保留门槛的候选。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 保留：DRA resource health in Pod status（2025-09-17）。
- 保留：DRA consumable capacity（2025-09-18）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DRA resource health in Pod status | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；作为 observability handoff |
| DRA consumable capacity | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Must Read；可能补全 GPU sharing 的多维资源边界 |

### Deep Analysis 1 — DRA resource health in Pod status

- First Public: 2025-09-17
- Status: Official alpha feature explanation
- Primary Source: https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/
- Evolution Relationship: Direct Evolution

#### Why

设备被分配不等于设备持续健康；AI job 若看不到 GPU health，只能从超时或错误间接推断。

#### Principle and Mechanism

alpha feature 允许 DRA driver 把 device health 报到 Pod status。

#### Trade-off and Evidence Boundary

可见性提高诊断能力，但 status freshness、driver correctness 与自动恢复 policy 仍需上层定义。

#### Connection and Evolution

知识树位置：第 59、63、69 章。Worth Watching；作为 observability handoff。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

### Deep Analysis 2 — DRA consumable capacity

- First Public: 2025-09-18
- Status: Official alpha feature explanation
- Primary Source: https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/
- Evolution Relationship: Direct Evolution

#### Why

设备共享若只表达“多个 Pod 引用同一设备”，无法声明和防止 capacity overcommit。

#### Principle and Mechanism

consumable capacity 为可共享 device 定义可计量容量与分配。

#### Trade-off and Evidence Boundary

细粒度共享提高利用率，却要求可靠 capacity model、隔离和 accounting；GPU 算力、显存与带宽并非单一可加资源。

#### Connection and Evolution

知识树位置：第 59～61、67 章。Must Read；可能补全 GPU sharing 的多维资源边界。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### DRA resource health in Pod status

- **Candidate / Week / Score:** DRA resource health in Pod status / 2025-W38 / 22/30。
- **Source Family ID:** `K8S-DRA-1.34`。
- **Source Type:** official Kubernetes feature documentation、KEP/API contract、v1.34 Blog。
- **First-public Date / Revision History:** Blog 2025-09-17；`DRAResourceHealth`为v1.34 alpha，不能与W35 core DRA GA混写。
- **Direct Primary Sources:** Kubernetes v1.34 resource-health Blog；official DRA resource health documentation/API。
- **Related Primary Sources:** W35 DRA core GA、W36 API details、W38 consumable capacity。
- **Access and Verification Status:** Verified for API/control flow/limitations；driver adoption、status latency distribution与production recovery evidence Not Disclosed。
- **Full-read Coverage:** 已阅读feature state、driver/kubelet streaming protocol、`allocatedResourcesStatus`/`resources.health` schema、cache与recovery行为、example、limitations和future work。
- **Original Problem:** claim allocation只说明设备被选中，不能告诉workload设备后来是Healthy、Unhealthy还是Unknown。
- **Why the Previous Design Was Reasonable:** node/device plugin日志与out-of-band monitoring避免Pod API频繁更新；scheduler只需在allocation时做资源决定。
- **Changed Constraint:** 长时AI任务、可共享设备和driver-owned health使应用、operator与recovery controller需要把“分配状态”和“运行健康”关联起来。
- **Mechanism:** driver通过`NodeWatchResources`向kubelet长流传递health；kubelet维护`healthInfoCache`，把已分配resource status写入ContainerStatus，值为Healthy/Unhealthy/Unknown。
- **State Ownership:** driver拥有原始health判定，kubelet拥有缓存/Pod status投影，scheduler仍拥有allocation；restart/remediation policy属于上层controller，不由health field自动执行。
- **Control Flow / Data Flow:** driver observation → streaming NodeWatchResources → kubelet persistent cache → allocatedResourcesStatus → user/controller诊断；terminated Pod不继续更新。
- **Implementation Details:** alpha feature gate；连接/更新超时会产生Unknown；当前timeout hard-coded；status只覆盖已分配resources。
- **Evaluation Setup:** API/behavior example；无GPU workload、freshness、failure-recovery或scale benchmark。
- **Baselines / Ablations / Sensitivity:** 与无Pod-level resource health的旧contract比较；无driver、node规模、更新频率敏感性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Applicable；device type、node count、update latency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明health被设计为driver→kubelet→Pod status的观测handoff，并明确Unknown与终止Pod限制。
- **What It Does Not Prove:** 不证明自动故障转移、driver health准确、status足够新，也不证明任何GPU vendor已production support。
- **Limitations / Threats to Validity:** alpha API、hard-coded timeout、driver trust、stream interruption、terminated Pod无更新；current docs可能随新版本变化。
- **Trade-offs / New Failure Modes:** 提高可诊断性，却新增stale/Unknown信号、status写放大、driver/kubelet skew和错误自动化风险。
- **Where the Previous Design Still Applies:** 快速任务、无driver health或只需node-level告警时out-of-band monitoring仍更简单；remediation仍需独立policy。
- **Evolution Relationship:** `Layering / Dependency`：W35 stable allocation contract → alpha runtime health observation；不是DRA GA自动包含health。
- **ROADMAP Node:** Ch59、Ch63、Ch69。
- **Target and Adjacent Chapters Read:** 已阅读 Ch58～64与Ch68～69；Ch59为resource lifecycle owner，Ch63/69仅handoff observability/recovery。
- **Existing Coverage:** Ch59 provisional已区分GA与alpha，但需核对是否明确driver/kubelet/controller三方ownership和Unknown semantics。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch59，保留 driver/kubelet/controller ownership 与 Unknown semantics。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/59-gpu-scheduler.md`。
- **Open Questions:** freshness SLO、driver attestability、Unknown阈值、Pod重启/迁移controller如何避免oscillation。

### DRA consumable capacity

- **Candidate / Week / Score:** DRA consumable capacity / 2025-W38 / 23/30。
- **Source Family ID:** `K8S-DRA-1.34`。
- **Source Type:** official Kubernetes alpha feature documentation、API/KEP、v1.34 Blog。
- **First-public Date / Revision History:** Blog 2025-09-18；`DRAConsumableCapacity`为v1.34 alpha。
- **Direct Primary Sources:** Kubernetes v1.34 consumable-capacity Blog；official DRA consumable capacity docs/API。
- **Related Primary Sources:** W35 core GA、W36 details、resource-health同族packet。
- **Access and Verification Status:** Verified for scheduler/API contract；vendor enforcement、GPU QoS isolation与production performance Not Disclosed。
- **Full-read Coverage:** 已阅读feature state、`allowMultipleAllocations`、capacity/request policy、default/min/step、share ID、distinct attribute、scheduler accounting和driver responsibility。
- **Original Problem:** “设备可共享”若只允许多个claim引用同一device，scheduler无法表达每次消耗多少，也无法防止声明容量超配。
- **Why the Previous Design Was Reasonable:** exclusive allocation边界清晰、隔离简单；MIG或预切片resource把容量固化成离散设备，scheduler无需连续accounting。
- **Changed Constraint:** time-slicing、NIC bandwidth、memory/compute partition等sharing希望动态组合请求，而不是预先枚举所有slice。
- **Mechanism:** device声明可消费capacity并允许multiple allocations；request按policy/default/min/step声明数量，scheduler跨ResourceClaims/Requests/namespaces累计，确保总allocation不超过capacity；ShareID/DistinctAttribute控制共享关系。
- **State Ownership:** driver发布capacity并在设备/进程层执行，scheduler拥有声明式admission/accounting，claim status记录allocation；workload request不等于runtime enforcement。
- **Control Flow / Data Flow:** driver inventory/capacity → ResourceSlice → claim/request quantity → scheduler累计/选择 → allocation status → driver prepare/enforce；release后容量回收。
- **Implementation Details:** alpha gate；多个capacity维度可以声明，但每个维度是否可加、如何隔离由driver定义；step/min/default影响fragmentation。
- **Evaluation Setup:** API examples与scheduler correctness contract；无GPU compute/memory/bandwidth isolation benchmark。
- **Baselines / Ablations / Sensitivity:** 与exclusive device和pre-partition slice比较；无fragmentation、fairness、bin-packing或noisy-neighbor敏感性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Applicable；GPU类型、share数量、QoS/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明Kubernetes能为driver声明的可加capacity做allocation-time accounting，并把多个sharing维度纳入DRA contract。
- **What It Does Not Prove:** 不证明GPU memory/compute/bandwidth可安全压成一个数，不证明driver强隔离、不证明性能可预测或公平。
- **Limitations / Threats to Validity:** alpha、driver-specific semantics、request/enforcement分离、fragmentation、cross-version skew；capacity可能是nominal而非实时可交付资源。
- **Trade-offs / New Failure Modes:** 提升利用率和表达力，却新增overcommit语义、碎片、noisy neighbor、accounting drift、claim recovery和admission/runtime不一致。
- **Where the Previous Design Still Applies:** hard isolation、strict latency或driver不支持多维enforcement时exclusive/MIG/static partition仍合理。
- **Evolution Relationship:** `Direct Evolution`：exclusive device → discrete partition → driver-declared consumable capacity；每阶段扩大flexibility也扩大enforcement责任。
- **ROADMAP Node:** Ch59～61、Ch67。
- **Target and Adjacent Chapters Read:** 已阅读 Ch58～61与Ch66～67；Ch59主owned allocation contract，Ch60/61只讨论capacity planning与contention结果。
- **Existing Coverage:** Ch59 provisional已有“request不是enforcement”边界；需验证是否完整保留多维资源不可简单相加与旧隔离方案共存条件。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch59，request 与 enforcement 分离。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/59-gpu-scheduler.md`；多维容量不简化为标量。
- **Open Questions:** driver如何证明capacity enforceability、multiple dimensions的dominant-resource policy、recovery后capacity reconciliation与tenant fairness。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- DRA resource health in Pod status → 第 59、63、69 章（Direct Evolution）
- DRA consumable capacity → 第 59～61、67 章（Direct Evolution）

## Recommended Action

- DRA resource health in Pod status：Worth Watching；作为 observability handoff
- DRA consumable capacity：Must Read；可能补全 GPU sharing 的多维资源边界

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W38/README.md。
- 两个 DRA 候选完成最终 disposition；第 59 章的 resource/health/capacity 边界已复核。

## Open Questions

- health status 的 freshness、driver trust 与自动恢复 policy 仍由上层系统定义。
- GPU memory、compute 与 bandwidth 是否可安全压成单一 consumable capacity 仍需设备实现证明。

## Sources

- DRA resource health in Pod status — https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/（First Public: 2025-09-17；Accessed: 2026-07-31）
- DRA consumable capacity — https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/（First Public: 2025-09-18；Accessed: 2026-07-31）
