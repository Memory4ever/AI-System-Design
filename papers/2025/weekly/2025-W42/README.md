# AI Research Weekly — 2025-W42

> Coverage Window: 2025-10-13～2025-10-19
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：PyTorch 2.9。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 本组无达到保留门槛的候选。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 保留：PyTorch 2.9（2025-10-15）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| PyTorch 2.9 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；重点审查第 32 章 communication backend contract |

### Deep Analysis 1 — PyTorch 2.9

- First Public: 2025-10-15
- Status: Official stable release
- Primary Source: https://pytorch.org/blog/pytorch-2-9/
- Evolution Relationship: Direct Evolution

#### Why

多 GPU kernel、第三方扩展与异构后端需要稳定的 memory/communication primitives，而不只是 graph compiler 的单机优化。

#### Principle and Mechanism

2.9 引入 symmetric memory、稳定 libtorch ABI 更新、graph-break control 与更多 wheel/backend 支持；这些属于版本化实现事实。

#### Trade-off and Evidence Boundary

symmetric memory 简化多 GPU kernel 编程，但不会消除 topology、collective choice 和 ownership；稳定 ABI 改善扩展生态，也限制部分内部演进自由度。

#### Connection and Evolution

知识树位置：第 32、33、36、45 章。Must Read；重点审查第 32 章 communication backend contract。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### PyTorch 2.9

- **Candidate / Week / Score:** PyTorch 2.9 / 2025-W42 / 25/30。
- **Source Family ID:** `PYTORCH-2.9-2025-10`。
- **Source Type:** official release Blog、signed GitHub release notes、API documentation。
- **First-public Date / Revision History:** 2025-10-15；2.9 tag/release notes固定版本事实，后续nightly/current docs不回写为2.9能力。
- **Direct Primary Sources:** PyTorch 2.9 release Blog；official v2.9.0 release notes/tag；Symmetric Memory API/docs。
- **Related Primary Sources:** NVSHMEM、Triton distributed programming、ProcessGroup/NCCL/UCC；只用于层次对照。
- **Access and Verification Status:** Verified for feature/API maturity and release notes；Symmetric Memory production adoption、fault semantics与end-to-end benchmark Not Disclosed。
- **Full-read Coverage:** 已阅读release Blog全部feature groups、Symmetric Memory primitives/collectives/Async TP、stable libtorch ABI preview、compile control与wheel variants；核对release notes中的breaking changes与API-Unstable标记。
- **Original Problem:** ProcessGroup collective把通信封装在kernel边界外，难以表达remote tensor direct access、compute/communication在单kernel交错及MoE特化dispatch/combine。
- **Why the Previous Design Was Reasonable:** NCCL/UCC collective提供成熟的group semantics、topology optimization与广泛backend coverage，应用不需管理对称映射和remote pointer。
- **Changed Constraint:** fused distributed kernels、NVLink/IB-GDA、MoE All-to-All和Async TP希望把通信原语下沉进Triton/CUDA kernel。
- **Mechanism:** symmetric tensors在参与rank映射相同shape/layout的memory；kernel可one-sided put/get访问remote buffer，并使用one/two-shot all-reduce、multimem all-gather和`all_to_all_vdev`类MoE primitives；NVSHMEM plugin提供transport。
- **State Ownership:** framework/runtime负责symmetric allocation、rank registration与lifetime；kernel author负责ordering/synchronization与访问模式；transport负责remote access；ProcessGroup仍负责传统collectives。
- **Control Flow / Data Flow:** ranks共同分配/注册symmetric memory → kernel用rank-relative remote address读写 → synchronization/collective completion → tensor进入后续compute；错误、peer loss和cleanup需跨层处理。
- **Implementation Details:** PyTorch 2.9中Symmetric Memory明确为API-Unstable；stable libtorch ABI仍是preview；wheel variants为experimental。release不等于所有backend/device成熟。
- **Evaluation Setup:** release Blog给feature说明和示例；无统一model、hardware、message size、topology、batch/concurrency或SLO benchmark。
- **Baselines / Ablations / Sensitivity:** 功能上与ProcessGroup collective对照；无公开one-sided vs NCCL/UCC的完整message-size/topology sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** CUDA/NVSHMEM和IB-GDA能力被提及；GPU型号、interconnect、model、precision、shape、concurrency与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明framework正在增加“kernel内remote memory + specialized collective”的编程层，通信边界可从library call下沉到kernel。
- **What It Does Not Prove:** 不证明替代NCCL/UCC/ProcessGroup、不证明性能普遍更高、不证明API/failure semantics稳定，也不证明跨vendor portability。
- **Limitations / Threats to Validity:** API-Unstable、transport/hardware依赖、ordering与lifetime更显式、release缺完整benchmark、current docs可能混入后续变化。
- **Trade-offs / New Failure Modes:** 更强fusion/one-sided访问减少launch和中间同步，却新增registration、symmetric layout、memory lifetime、ordering、peer failure、topology与debugging复杂性。
- **Where the Previous Design Still Applies:** 常规data/gradient collective、跨vendor backend、稳定API与故障边界优先时ProcessGroup+NCCL/UCC仍是默认；小规模/无fusion需求不必承担新substrate成本。
- **Evolution Relationship:** `Layering / Dependency`：MPI/ProcessGroup collective → optimized collective libraries → symmetric remote-memory substrate → kernel-specialized distributed algorithm；后者扩展表达力，不否定前者。
- **ROADMAP Node:** Ch32～33、Ch36、Ch45、Ch50。
- **Target and Adjacent Chapters Read:** 已阅读 Ch31～37、Ch44～46与Ch49～50；Ch32应owned training communication abstraction，Ch45/50只做runtime handoff。
- **Existing Coverage:** Ch32已有collective/backend分层但缺one-sided symmetric memory分支；这是潜在机制缺口，不应写release feature list。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch32，新增 one-sided symmetric-memory 通信分支。
- **Changed Files or Rejection Reason:** 已更新 `books/part-03-training-system/32-distributed-training.md`；不把 unstable API 写成通用替代。
- **Open Questions:** API stabilization、failure semantics、NVSHMEM/NCCL共存、跨vendor path、memory registration成本与真实MoE/TP workload sensitivity。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- PyTorch 2.9 → 第 32、33、36、45 章（Direct Evolution）

## Recommended Action

- PyTorch 2.9：Must Read；重点审查第 32 章 communication backend contract

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W42/README.md。
- 新增 PyTorch 2.9 候选级 Full Source Review；本阶段未修改 Books。

## Open Questions

- Symmetric Memory 是否足以作为 Ch32 的新通信分支，待和NCCL/UCC/one-sided语义去重后决定。

## Sources

- PyTorch 2.9 — https://pytorch.org/blog/pytorch-2-9/（First Public: 2025-10-15；Accessed: 2026-07-31）
- PyTorch v2.9.0 release — https://github.com/pytorch/pytorch/releases/tag/v2.9.0（Published: 2025-10-15；Accessed: 2026-07-31）
