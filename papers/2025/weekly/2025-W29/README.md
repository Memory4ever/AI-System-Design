# AI Research Weekly — 2025-W29

> Coverage Window: 2025-07-14～2025-07-20
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：SGLang Multiple Token Prediction integration。重点是约束、机制、trade-off 与演进，不是发布热度。

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

- 保留：SGLang Multiple Token Prediction integration（2025-07-17）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SGLang Multiple Token Prediction integration | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；与 EAGLE-3、SpecForge 合并审计 |

### Deep Analysis 1 — SGLang Multiple Token Prediction integration

- First Public: 2025-07-17
- Status: Official engineering blog; project benchmark
- Primary Source: https://www.lmsys.org/blog/2025-07-17-mtp/
- Evolution Relationship: Direct Evolution

#### Why

MTP 在低并发可能减少 decode iterations，但在高并发和 PD/EP 组合中，verification compute 与 batch shape 决定真实收益。

#### Principle and Mechanism

SGLang 将 MTP 与 expert parallelism、PD disaggregation 组合，并给出 draft/verify 的部署路径。

#### Trade-off and Evidence Boundary

plug-in 接口降低采用门槛，却不消除 acceptance、verification、CUDA Graph shape 与 workload sensitivity；项目最高吞吐数字不得外推。

#### Connection and Evolution

知识树位置：第 44、47、51、52 章。Must Read；与 EAGLE-3、SpecForge 合并审计。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### SGLang Multiple Token Prediction integration

- **Candidate / Week / Score:** SGLang Multiple Token Prediction integration / 2025-W29 / 25/30。
- **Source Family ID:** `SGLANG-MTP-2025-07`。
- **Source Type:** official engineering blog、reproduction issue/commands、SGLang implementation documentation。
- **First-public Date / Revision History:** official blog 2025-07-17；reproduction issue opened 2025-07-13。当前 SGLang 已继续演进，review 只把 2025 当时列出的 compatibility matrix 和限制视作事件事实。
- **Direct Primary Sources:** LMSYS/SGLang MTP blog；`sgl-project/sglang#7998` reproduction instructions；2025-era SGLang speculative decoding code/config。
- **Related Primary Sources:** DeepSeek-V3 MTP architecture、DeepEP、Mooncake PD transfer 与 SGLang large-scale EP blog，用于解释依赖而不合并 benchmark。
- **Access and Verification Status:** Verified for documented algorithm, commands and author benchmark contract；exact commit/container、precision、network topology 与 independent reproduction Not Disclosed。
- **Full-read Coverage:** 已阅读 blog 全文的 draft/verify path、acceptance length、feature integration、两个 case study、best practices、future work；核对 reproduction issue 的 launch flags、batch/length、PD/EP topology 与当时“不支持 overlap scheduling”限制，并定位对应 runtime options。
- **Original Problem:** autoregressive decode 每轮只提交一个 token；当 target forward 的 GPU 并行资源未被充分利用时，serial dependency 限制 output throughput。
- **Why the Previous Design Was Reasonable:** single-token decode state最简单、无需 draft/verify state；continuous batching和overlap scheduling在高 batch时已能提升 utilization，且不依赖高 acceptance。
- **Changed Constraint:** DeepSeek-V3 自带轻量 MTP module，同时 production 需要与 DP Attention、large-scale EP、PD disaggregation、CUDA Graph 等机制组合；孤立实现 MTP 不足以上线。
- **Mechanism:** draft path 先给出若干候选 tokens，target model 在一次并行 verification 中接受最长匹配 prefix并从首个拒绝处 resample；收益由 average acceptance length 与 verification/draft overhead共同决定。
- **State Ownership:** request scheduler拥有sequence与batch placement；draft worker拥有candidate tree/window；target worker拥有 authoritative logits/accepted prefix；PD runtime拥有KV传输；acceptance telemetry只用于 tuning，不能改变模型语义。
- **Control Flow / Data Flow:** target extend 产生首 token → draft extend/decode 产生候选 → target parallel verify → commit longest accepted prefix/resample → 更新 KV/request state → next iteration；跨 PD/EP 时各 stage 还需一致的 expert/KV placement。
- **Implementation Details:** 2025 integration列出 DP Attention、EPLB、DeepEP、Two Batch Overlap、PD disaggregation、CUDA Graph 和多 attention backends；但 MTP 当时尚不能与 overlap scheduling 同时开启，issue 命令显式使用 `--disable-overlap-schedule`。
- **Evaluation Setup:** small case：DeepSeek-V3、2 decode nodes/16×H200、每 rank 2 concurrent、65,536 input/4,096 output；无 overlap/MTP baseline 51 tok/s/rank，overlap-only 60.4，3/4-token MTP 为81.5/82.0且 acceptance 2.18/2.44。large case：16 nodes/128×H200、4 prefill+12 decode、每 rank 128 concurrent、2,000/100、draft=2，报告相对同一无 overlap/MTP baseline +14.2%。
- **Baselines / Ablations / Sensitivity:** small case分开报告 baseline、overlap-only 与 MTP-only，但未报告 overlap+MTP；比较 3/4-token window。large case只给相对增益，缺绝对吞吐、tail latency及 draft/acceptance sweep。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H200数量、model、input/output、concurrency与60.4 tok/s/rank应用阈值披露；precision/quantization、interconnect、TTFT/TPOT percentile、arrival process与exact software commit Not Disclosed。
- **What the Evidence Actually Proves:** 在作者两组特定 DeepSeek-V3/H200 配置中，MTP integration可运行于PD+EP并改善output throughput；acceptance length是可观测的主要收益信号。
- **What It Does Not Prove:** “最高60%”不是相对当时最佳 overlap baseline；它来自 MTP-only 对无 overlap baseline。也不证明任意 model、batch、sampling或SLO下保持同等收益与输出 bitwise deterministic。
- **Limitations / Threats to Validity:** vendor/author-only benchmark；MTP与overlap互斥使比较不完整；precision/network/version缺失；高 batch时draft增加的compute可抵消串行节省；sampling实现可能影响“identical output”表述。
- **Trade-offs / New Failure Modes:** 用额外 draft compute、KV/metadata、verify scheduling换取更少target iterations；新增acceptance collapse、candidate window过长、CUDA Graph shape膨胀、PD/EP state mismatch与公平性变化。
- **Where the Previous Design Still Applies:** 高并发已使 target充分利用、acceptance低、短 output、显存紧或需最简单确定性路径时，single-token decode + batching/overlap仍合理。
- **Evolution Relationship:** `Layering / Dependency`：autoregressive decode → speculative draft/verify → 与 batching/EP/PD 联合调度；MTP不是对continuous batching或overlap的替代。
- **ROADMAP Node:** Ch43～44、Ch47～48、Ch51～52。
- **Target and Adjacent Chapters Read:** 已阅读 Ch42～45、Ch46～48、Ch50～52；Ch44 已按本 packet 修正“60%”比较基线的证据边界。
- **Existing Coverage:** Ch44已解释lossless verification与acceptance/overhead模型，Ch52已覆盖token scheduling；真正新增证据是 MTP 与 PD/EP/overlap 的 compatibility contract，而非算法定义。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch44，作为 MTP 进入 PD/EP runtime 的 compatibility evidence。
- **Changed Files or Rejection Reason:** 已复核 `books/part-04-inference-system/44-speculative-decoding.md`；不保留 60% 宣传口径。
- **Open Questions:** exact commit/precision/network、overlap+MTP后续公平对比、tail latency、non-greedy sampling contract与低 acceptance fallback。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- SGLang Multiple Token Prediction integration → 第 44、47、51、52 章（Direct Evolution）

## Recommended Action

- SGLang Multiple Token Prediction integration：Must Read；与 EAGLE-3、SpecForge 合并审计

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W29/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- MTP 在高并发、低 acceptance 或 verification 饱和时的收益边界仍需按 workload 实测。

## Sources

- SGLang Multiple Token Prediction integration — https://www.lmsys.org/blog/2025-07-17-mtp/（First Public: 2025-07-17；Accessed: 2026-07-31）
- SGLang reproduction issue #7998 — https://github.com/sgl-project/sglang/issues/7998（Opened: 2025-07-13；Accessed: 2026-07-31）
