# AI Research Weekly — 2025-W35

> Coverage Window: 2025-08-25～2025-08-31
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Kubernetes v1.34 and DRA GA。重点是约束、机制、trade-off 与演进，不是发布热度。

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

- 保留：Kubernetes v1.34 and DRA GA（2025-08-27）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kubernetes v1.34 and DRA GA | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Must Read；refine GPU Scheduler/Platform 的资源语义 |

### Deep Analysis 1 — Kubernetes v1.34 and DRA GA

- First Public: 2025-08-27
- Status: Official stable release
- Primary Source: https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/
- Evolution Relationship: Direct Evolution

#### Why

GPU/TPU/NIC 不能只用整数 extended resource 描述；异构设备选择、配置、共享与健康状态需要独立资源 API。

#### Principle and Mechanism

Kubernetes v1.34 将 DRA core 升为 GA，以 ResourceClaim 等对象将 device request 与具体分配解耦，并继续扩展 sharing/health。

#### Trade-off and Evidence Boundary

更强表达力改善调度与可移植性，却增加 driver、claim lifecycle、scheduler integration 和迁移复杂度；GA core 不代表所有扩展均 GA。

#### Connection and Evolution

知识树位置：第 53、56、59～61、69 章。Must Read；refine GPU Scheduler/Platform 的资源语义。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### Kubernetes v1.34 DRA core GA

- **Candidate / Week / Score:** Kubernetes v1.34 and DRA GA / 2025-W35 / 26/30。
- **Source Family ID:** `K8S-DRA-1.34`（W36/W38为GA core之上的follow-ups）。
- **Source Type:** official release blog/notes、stable API/docs、KEP-4381与implementation changes。
- **First-public Date / Revision History:** Kubernetes v1.34 release 2025-08-27；DRA GA深度说明2025-09-01。stable core与同版alpha/beta扩展必须分开。
- **Direct Primary Sources:** v1.34 release notes/blog；DRA GA blog；`resource.k8s.io/v1` API docs、KEP-4381。
- **Related Primary Sources:** kube-scheduler/kubelet DRA implementation；W36 design follow-up与W38 alpha features。
- **Access and Verification Status:** Verified for API/lifecycle/feature-state；vendor GPU driver支持、scale/performance与production failure behavior按driver而异。
- **Full-read Coverage:** 已阅读release/DRA blogs、stable kinds、claim allocation workflow、admin/prioritized-list边界、KEP graduation状态与limitations；核对GA core与alpha/beta gates。
- **Original Problem:** Device Plugin的整数extended resource只表达“要N个设备”，难以声明属性、配置、共享、独立claim生命周期与scheduler-visible topology。
- **Why the Previous Design Was Reasonable:** 整卡exclusive allocation简单、稳定且易做bin-packing；vendor plugin在设备模型单一时减少API面。
- **Changed Constraint:** GPU/TPU/NIC异构、可分区/共享、多种fallback与跨Pod复用要求scheduler理解结构化request而非opaque integer。
- **Mechanism:** stable API引入DeviceClass、ResourceClaim/Template、ResourceSlice与Pod `resourceClaims`；driver发布available devices/attributes，claim描述需求，scheduler原子选择可访问设备并写allocation，kubelet调用driver完成node-local prepare/unprepare。
- **State Ownership:** driver拥有ResourceSlice/device truth；admin拥有DeviceClass/policy；scheduler拥有claim allocation decision；kubelet/driver拥有node prepare state；workload只引用claim。
- **Control Flow / Data Flow:** driver advertises slices → user/template creates claim → scheduler filters node+device/CEL constraints → writes allocation → Pod binds → kubelet prepares device → container runs → teardown/release。
- **Implementation Details:** `resource.k8s.io/v1`默认启用且不再break core API；admin access/prioritized list为beta而非GA core。GA稳定的是结构化allocation contract，不是所有sharing/health功能。
- **Evaluation Setup:** Kubernetes release/KEP以conformance、API review、implementation maturity为证据，不提供AI workload吞吐benchmark。
- **Baselines / Ablations / Sensitivity:** 与Device Plugin/extended resources按expressiveness比较；没有统一GPU scheduler utilization、queueing或failure-rate实验。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 不适用model/precision/length；driver/device/cluster scale、scheduler latency与SLO Not Disclosed，必须按具体driver测试。
- **What the Evidence Actually Proves:** core allocation state machine与API达到stable，可作为platform长期resource contract；它把request/advertisement/allocation/prepare分离。
- **What It Does Not Prove:** 不证明MIG、time-slicing、GPU memory或fabric由core自动实现，也不证明DRA本身提高utilization或支持gang scheduling。
- **Limitations / Threats to Validity:** 依赖vendor driver correctness与ResourceSlice freshness；claim lifecycle/RBAC更复杂；alpha/beta能力不受GA兼容承诺覆盖。
- **Trade-offs / New Failure Modes:** expressiveness与可移植性提高，却新增driver/control-plane state、stale advertisement、allocation/prepare split-brain、RBAC与upgrade compatibility。
- **Where the Previous Design Still Applies:** homogeneous exclusive GPU、简单batch或driver未成熟时extended resources/Device Plugin仍合理；gang/queue仍由Kueue/Volcano等上层owner处理。
- **Evolution Relationship:** `Direct Evolution`：opaque integer device plugin → structured DRA beta → stable claim-based core；后续capacity/health是layering，不覆盖exclusive allocation。
- **ROADMAP Node:** Ch57～60、Ch63～64、Ch68。
- **Target and Adjacent Chapters Read:** 已阅读 Ch56～61、Ch62～64、Ch67～69；Ch59 的 DRA 段落已按 feature-state 最终复核。
- **Existing Coverage:** Ch59已有GPU scheduler/claim contract，Ch57/58覆盖declarative control plane。长期缺口是明确GA core不等于sharing、health或gang semantics。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch59，明确 GA core 与 sharing/health/gang 的边界。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/59-gpu-scheduler.md`。
- **Open Questions:** driver conformance、large-cluster scheduler cost、claim recovery、upgrade skew与具体GPU driver支持矩阵。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- Kubernetes v1.34 and DRA GA → 第 53、56、59～61、69 章（Direct Evolution）

## Recommended Action

- Kubernetes v1.34 and DRA GA：Must Read；refine GPU Scheduler/Platform 的资源语义

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W35/README.md。
- 更新 books/part-05-ai-infrastructure/59-gpu-scheduler.md。

## Open Questions

- DRA driver、scheduler 与 admission policy 的跨版本兼容矩阵仍需部署验证。

## Sources

- Kubernetes v1.34 and DRA GA — https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/（First Public: 2025-08-27；Accessed: 2026-07-31）
