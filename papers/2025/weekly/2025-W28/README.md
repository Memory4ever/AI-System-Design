# AI Research Weekly — 2025-W28

> Coverage Window: 2025-07-07～2025-07-13
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Kimi K2 release。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：Kimi K2 release（2025-07-11 (release); 2025-07-28 (report v1)）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kimi K2 release | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；报告全文在 Books 阶段联合复核 |

### Deep Analysis 1 — Kimi K2 release

- First Public: 2025-07-11 (release); 2025-07-28 (report v1)
- Status: Official open-weight release; report published later
- Primary Source: https://github.com/moonshotai/Kimi-K2
- Evolution Relationship: Direct Evolution

#### Why

agentic model 不只需要增大 MoE 容量，还需要稳定的大规模训练、可验证 tool-use post-training 与 serving ecosystem 协同。

#### Principle and Mechanism

官方仓库披露 1T-total/32B-active MoE、MuonClip、tool-use post-training 与部署接口；完整技术报告的 first-public date 落在 W31，机制阅读需回链本周 release 并注明版本。

#### Trade-off and Evidence Boundary

低 activated compute 不消除总权重、expert communication 与 memory footprint；Muon 的规模化稳定性、agent benchmark 和部署成本都受作者条件限制。

#### Connection and Evolution

知识树位置：第 21、24、29、32、45、74 章。Must Read；报告全文在 Books 阶段联合复核。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### Kimi K2 release

- **Candidate / Week / Score:** Kimi K2 release / 2025-W28 / 27/30。
- **Source Family ID:** `KIMI-K2-2507.20534`（与 W31 technical report 联读）。
- **Source Type:** official release、open weights/model card、repository；technical report 于 2025-07-28 后发。
- **First-public Date / Revision History:** model/weights release 2025-07-11；technical report arXiv v1 2025-07-28、v2 2026-02-03。7 月 11 日事件只确认 release-time contract；报告细节记录在 W31，不回写成 release 当日已公开事实。
- **Direct Primary Sources:** Moonshot/Kimi official K2 announcement、`moonshotai/Kimi-K2` repository/model card、released base/instruct weights。
- **Related Primary Sources:** arXiv:2507.20534 v1/v2；Moonlight/Muon optimizer lineage；serving engine integration docs 仅作可运行性证据。
- **Access and Verification Status:** Verified for release, weights, license/model shape and public usage contract；训练机制须由 W31 report 补证，内部 production serving policy Not Disclosed。
- **Full-read Coverage:** 已阅读 release/model card/repository 的 model shape、context、chat/tool template、deployment notes、license/use policy 与公开 evaluation table；并对照后发报告全文确认哪些机制在 release 页面未披露。
- **Original Problem:** 让 open-weight model 同时具备大容量、较低 active compute 与 agent/tool behavior，并能被外部 runtime 实际部署。
- **Why the Previous Design Was Reasonable:** dense model 与普通 chat checkpoint 的权重/serving contract 更简单；将 agent logic 留给外部 workflow 也可减少 model-side protocol coupling。
- **Changed Constraint:** 1T 级总容量、32B active compute、128K context 与 tool-intensive workload 同时出现，要求 MoE routing、模板、parser、KV 与多机 serving 形成可交付 artifact contract。
- **Mechanism:** release-time 可确认 1T total/32B active MoE、128K context、base/instruct checkpoints 与 tool-use template；MuonClip、15.5T training、agentic data/RL 与训练并行属于后发 report evidence，不是 7 月 11 日 release page 独立证明。
- **State Ownership:** model artifact 拥有 immutable config/weights/tokenizer/template；serving runtime 拥有 expert placement、KV、parser 与 admission；workflow 拥有 tool side effects；这些 owner 不因“agentic model”标签合并。
- **Control Flow / Data Flow:** prompt/tool schema → tokenizer/chat template → distributed MoE forward → model emits text/tool proposal → runtime parser → authorized workflow/tool execution；release 不公开内部训练 control flow。
- **Implementation Details:** public artifact 暴露 MLA/MoE config 与 custom-code/runtime requirements；具体 MuonClip、pipeline/expert parallel、activation offload 等在 W31 packet 核验。
- **Evaluation Setup:** release/model card 列出 coding、math、agent benchmarks；不同任务使用不同 scaffolds/sampling，hardware、production concurrency、TTFT/TPOT/SLO 不形成统一 contract。
- **Baselines / Ablations / Sensitivity:** release 有 cross-model table 但无同 data/compute 消融；optimizer/architecture ablation 只在技术报告出现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1T/32B active、128K context 与部分 deployment precision 支持可核；release benchmark hardware、batch/concurrency、KV capacity 与 SLO mostly Not Disclosed。
- **What the Evidence Actually Proves:** 证明该日可取得、检查并自行部署一个 1T/32B-active open-weight model 及其 interface contract；证明开放 artifact 把 model/runtime compatibility 交给部署者。
- **What It Does Not Prove:** 不证明 MuonClip 是稳定训练的唯一原因，不证明 agent benchmark 等于可靠 workflow，更不证明任意硬件上的 throughput、cost 或 SLO。
- **Limitations / Threats to Validity:** release-oriented evidence 缺少训练/消融；benchmark scaffold 异构；权重开放后 safety、parser、quantization 与 runtime patch 责任转移给 operator。
- **Trade-offs / New Failure Modes:** sparse active compute 降低每 token 理论计算，却新增 expert placement/All-to-All、large artifact distribution、parser mismatch、quantization drift 与 multi-node failure surface。
- **Where the Previous Design Still Applies:** 规模较小、低并发、互联受限或追求简单升级/回滚时，dense model 或更小 MoE 更合理；non-agent chat 不需要复杂 tool parser。
- **Evolution Relationship:** `Layering / Dependency`：open-weight MoE release contract 依赖 training 与 runtime 两条链；W31 report 补充“为何能训练”，不把 release 变成第二篇论文。
- **ROADMAP Node:** Ch21、Ch24、Ch31～32、Ch45～48、Ch74。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20～24、Ch31～33、Ch44～48、Ch73～75 的章节边界；主 owner 尚待 Books Gate 在 MoE、distributed training 与 serving runtime 之间择一。
- **Existing Coverage:** Ch21 已覆盖 active/total parameters、routing 与 All-to-All；Ch45～48 已覆盖 model artifact 到 runtime contract。release 本身主要是 Version/Product Fact，是否新增机制取决于 W31 report 的 MuonClip 与 training/agent environment 证据。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；机制判断归并 W31 technical report。
- **Changed Files or Rejection Reason:** 不改 Books；避免 release 与 report 重复计入。
- **Open Questions:** release-time model card 精确版本、可复现 serving matrix、quantization accuracy、production failure data 与第三方完整复现。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- Kimi K2 release → 第 21、24、29、32、45、74 章（Direct Evolution）

## Recommended Action

- Kimi K2 release：Must Read；报告全文在 Books 阶段联合复核

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W28/README.md。
- 新增 release-time Full Source Review；本阶段未修改 Books，等待与 W31 technical report 合并 disposition。

## Open Questions

- Kimi K2 的 release contract 与后发训练机制应由哪个章节作为主 owner，留待 Evidence Gate 后确定。

## Sources

- Kimi K2 release — https://github.com/moonshotai/Kimi-K2（First Public: 2025-07-11 (release); 2025-07-28 (report v1)；Accessed: 2026-07-31）
- Kimi K2 technical report — https://arxiv.org/abs/2507.20534（v1: 2025-07-28；v2: 2026-02-03；Accessed: 2026-07-31）
