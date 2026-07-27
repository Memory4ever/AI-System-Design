# AI Research Weekly — 2025-W36

> Coverage Window: 2025-09-01～2025-09-07
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Kubernetes DRA GA design details。重点是约束、机制、trade-off 与演进，不是发布热度。

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

- 保留：Kubernetes DRA GA design details（2025-09-01）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kubernetes DRA GA design details | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；合并到 W35 Books 决策 |

### Deep Analysis 1 — Kubernetes DRA GA design details

- First Public: 2025-09-01
- Status: Official design follow-up
- Primary Source: https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/
- Evolution Relationship: Layering / Dependency

#### Why

release summary不足以解释 claim、device class、allocation 与 driver ownership。

#### Principle and Mechanism

官方 follow-up 补足 DRA API responsibilities，作为 W35 的证据包而非独立技术替代。

#### Trade-off and Evidence Boundary

API 解耦减少 scheduler 对设备细节的硬编码，但 correctness 转移到 drivers 和 admission/policy。

#### Connection and Evolution

知识树位置：第 56、59～61 章。Worth Watching；合并到 W35 Books 决策。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### Kubernetes DRA GA design details

- **Candidate / Week / Score:** Kubernetes DRA GA design details / 2025-W36 / 23/30。
- **Source Family ID:** `K8S-DRA-1.34`。
- **Source Type:** official GA design follow-up、stable API/docs/KEP。
- **First-public Date / Revision History:** 2025-09-01；解释同一v1.34 core GA，不是第二个独立功能release。
- **Direct Primary Sources:** Kubernetes DRA GA blog、DRA docs、`resource.k8s.io/v1` API/KEP-4381。
- **Related Primary Sources:** W35 release、W38 consumable capacity/resource health KEPs。
- **Access and Verification Status:** Verified；driver-specific behavior与performance仍Not Disclosed。
- **Full-read Coverage:** 已阅读core GA、beta/alpha清单、API kinds、allocation workflow、admin access、prioritized alternatives、binding/health/capacity边界与next steps。
- **Original Problem:** release headline容易把“DRA GA”误读为所有device sharing/health/readiness都stable，需要拆出feature maturity与owner。
- **Why the Previous Design Was Reasonable:** 单一release status便于沟通；旧extended resource路径对简单设备仍足够。
- **Changed Constraint:** 同一API family内core、admin access、prioritized list、capacity、binding、health处于不同maturity，生产平台必须按feature gate治理。
- **Mechanism:** core DeviceClass/Claim/Slice进入v1；admin access和prioritized list为beta；extended mapping、consumable capacity、binding conditions、resource health为alpha。
- **State Ownership:** API server存desired/allocation state；scheduler作selection；driver/kubelet维护device/prepare state；feature gates和RBAC由cluster operator拥有。
- **Control Flow / Data Flow:** request → stable claim allocation → optional gated features参与selection/status → node prepare；alpha信号不能提升为稳定控制动作。
- **Implementation Details:** admin access需namespace label授权；prioritized alternatives按顺序尝试且每Pod可能选择不同subrequest；health/capacity不是core GA的一部分。
- **Evaluation Setup:** API graduation/conformance evidence；无AI workload benchmark。
- **Baselines / Ablations / Sensitivity:** feature-state与旧API对比；无性能消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Applicable/Not Disclosed；按driver、cluster规模与scheduler profile验证。
- **What the Evidence Actually Proves:** 证明平台文档必须将API stability与feature maturity分开，不能把同release中的alpha字段写成GA能力。
- **What It Does Not Prove:** 不证明所有vendor drivers支持v1或所有DRA features；不证明自动故障恢复。
- **Limitations / Threats to Validity:** 文档随版本演进，current docs可能混入后续1.35/1.36；历史结论需固定v1.34 snapshot。
- **Trade-offs / New Failure Modes:** feature gating允许渐进演进，却增加control-plane skew、manifest portability与误配置风险。
- **Where the Previous Design Still Applies:** 无需高级选择/共享时stable core或旧extended resource即可，避免alpha dependencies。
- **Evolution Relationship:** `Layering / Dependency`：W35 stable core → W36 maturity map → W38 alpha observability/sharing；不是多次重复GA。
- **ROADMAP Node:** Ch57～60、Ch63～64。
- **Target and Adjacent Chapters Read:** 已阅读 Ch56～61与Ch62～64，并对照W35 owner。
- **Existing Coverage:** 应与W35合并为Ch59的一次refine；没有独立新机制值得重复写入。
- **Integration Decision:** `Refine — Existing Argument`；与 W35 合并为 Ch59 同一次 resource-contract refine。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/59-gpu-scheduler.md`；不重复写版本功能。
- **Open Questions:** operator如何固定feature-gate/version matrix、driver升级顺序与API skew测试。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- Kubernetes DRA GA design details → 第 56、59～61 章（Layering / Dependency）

## Recommended Action

- Kubernetes DRA GA design details：Worth Watching；合并到 W35 Books 决策

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W36/README.md。
- 更新 books/part-05-ai-infrastructure/59-gpu-scheduler.md（与 W35 联合 Source Packet）。

## Open Questions

- driver correctness、admission constraints 与 claim recovery 的责任边界仍需实现级验证。

## Sources

- Kubernetes DRA GA design details — https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/（First Public: 2025-09-01；Accessed: 2026-07-31）
