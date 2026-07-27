# AI Research Weekly — 2025-W52

> Coverage Window: 2025-12-22～2025-12-28
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：SpecBundle and SpecForge v0.2。重点是约束、机制、trade-off 与演进关系。

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

- 保留：SpecBundle and SpecForge v0.2（2025-12-23）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SpecBundle and SpecForge v0.2 | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；完成 EAGLE-3→MTP→training→artifact 演进链 |

### Deep Analysis 1 — SpecBundle and SpecForge v0.2

- First Public: 2025-12-23
- Status: Official open-source release/blog
- Primary Source: https://www.lmsys.org/blog/2025-12-23-spec-bundle-phase-1/
- Evolution Relationship: Direct Evolution

#### Why

draft model 的可用性受 target version、训练分布和 runtime integration 约束；只发布算法不足以形成可复用 serving artifact。

#### Principle and Mechanism

SpecBundle 为多类目标模型发布 EAGLE-3 draft weights，并用 SpecForge 训练/再生成数据，形成 versioned bundle。

#### Trade-off and Evidence Boundary

预训练 draft 降低采用成本，却新增 artifact provenance、target compatibility、acceptance drift 与持续重训责任；最高 speedup 仍绑定项目设置。

#### Connection and Evolution

知识树位置：第 44、47、55、62 章。Must Read；完成 EAGLE-3→MTP→training→artifact 演进链。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### SpecBundle and SpecForge v0.2

- **Candidate / Week / Score:** SpecBundle and SpecForge v0.2 / 2025-W52 / 24/30。
- **Source Family ID:** `EAGLE3-SPECFORGE-SPECBUNDLE-2025`（W10 EAGLE-3 → W29 MTP/SpecForge → W52 artifact bundle）。
- **Source Type:** LMSYS/SGLang official engineering Blog、documentation、repository与released model collection。
- **First-public Date / Revision History:** 2025-12-23 v0.2/Phase 1；后续reasoning/VLM phases在roadmap中，不作为已实现能力。
- **Direct Primary Sources:** SGLang/LMSYS launch Blog；SpecForge repository/docs；SpecBundle docs/model collection。
- **Related Primary Sources:** EAGLE-3 paper与SGLang speculative decoding runtime docs；机制源回链旧周。
- **Access and Verification Status:** Verified forpublished workflow/artifacts/API与roadmap；每个bundle的完整hardware/workload benchmark及长期compatibility Not Disclosed。
- **Full-read Coverage:** 已阅读问题背景、data generation、online/offline training、multi-backend `Eagle3TargetModel`、Perfect-Blend、released sizes、performance图、documentation、roadmap与repository interface。
- **Original Problem:** speculative decoding算法即使有效，使用者仍需为每个target version生成数据、训练draft、接入runtime；缺可用draft artifact时部署门槛高。
- **Why the Previous Design Was Reasonable:** 自训draft能精确匹配私有target/data与runtime，避免第三方artifact漂移；少量稳定模型不需公共bundle治理。
- **Changed Constraint:** 开源target数量和版本增长，target-specific数据生成/训练昂贵且各backend实现重复；社区需要可追踪draft weights与统一训练接口。
- **Mechanism:** SpecForge统一online/offline data generation/training；v0.2定义`Eagle3TargetModel.generate_eagle3_data`以接入SGLang/HF Transformers backend。SpecBundle Phase1发布target-specific EAGLE-3 draft weights，作者用SGLang重生成target outputs，使training distribution匹配实际模型。
- **State Ownership:** target model/version拥有logit/hidden distribution；draft artifact registry拥有weights、training data/provenance与compatibility；runtime拥有verify/acceptance state；operator拥有upgrade/rollback policy。
- **Control Flow / Data Flow:** pin target checkpoint/template/tokenizer → backend生成target data → train EAGLE-3 draft → package bundle metadata → runtime加载target+draft → monitor acceptance/speed/quality → target变化触发retrain/revalidate。
- **Implementation Details:** Perfect-Blend约1.4M样本，原EAGLE常用ShareGPT+UltraChat约320K；backend扩展只需实现一个target-data方法，但不意味着hidden-state/schema天然兼容。
- **Evaluation Setup:** 作者比较公开draft/standard decoding，并展示不同8B到1T target的acceptance/end-to-end speedup；launch页报告最高4×，但各图完整hardware、batch、prompt/output、concurrency、precision与SLO并非统一披露。
- **Baselines / Ablations / Sensitivity:** data regeneration/distribution alignment与旧公开weights对照；缺target小版本、tokenizer/template变化、long context、reasoning output与productionarrival sensitivity完整研究。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** target size范围与部分模型已披露；GPU、precision、input/output length、batch/concurrency、TTFT/ITL/P99、quality guardrail不完整，4×不得外推。
- **What the Evidence Actually Proves:** speculative decoding采用成本不仅由算法决定，还由target-specific训练artifact、backend接口、provenance与持续验证决定；项目已公开一批具体weights/workflow。
- **What It Does Not Prove:** 不证明所有target可获得4×、不证明bundle长期兼容、不证明draft质量在target更新后保持，也不证明production-ready仅凭作者声明。
- **Limitations / Threats to Validity:** Phase1只含instruct models；long-context、VLM、MTP finetuning仍在roadmap；vendor benchmark、artifact lineage与每bundle metadata完整度需逐项核查。
- **Trade-offs / New Failure Modes:** 预训练bundle降低入门成本，却新增target/tokenizer/template mismatch、acceptance drift、artifact supply chain、rollback、license与registry lifecycle。
- **Where the Previous Design Still Applies:** 私有模型、快速变化target、特殊domain或严格provenance时仍应自行生成/训练draft；低吞吐/短输出无需承担draft lifecycle成本。
- **Evolution Relationship:** `Direct Evolution`：EAGLE-3 mechanism → SpecForge repeatable training/data pipeline → SpecBundle versioned deployable artifact；不是新算法替代旧算法，而是从论文到operational supply chain。
- **ROADMAP Node:** Ch44、Ch47、Ch55、Ch62。
- **Target and Adjacent Chapters Read:** 已读 Ch43～45、Ch47、Ch55、Ch62；Ch44 为 speculative artifact lifecycle 主 owner。
- **Existing Coverage:** Ch44 provisional已写artifact provenance/compatibility；需核对是否完整保留target pinning、acceptance drift、rollback与旧自训路径适用条件。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch44，target-coupled draft weights 成为 versioned artifact。
- **Changed Files or Rejection Reason:** 已复核 `books/part-04-inference-system/44-speculative-decoding.md` 的 target pinning、acceptance drift 与 rollback。
- **Open Questions:** bundle manifest最低字段、target patch版本兼容、automatic retrain threshold、acceptance/quality canary与rollback。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- SpecBundle and SpecForge v0.2 → 第 44、47、55、62 章（Direct Evolution）

## Recommended Action

- SpecBundle and SpecForge v0.2：Must Read；完成 EAGLE-3→MTP→training→artifact 演进链

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W52/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- target 更新、acceptance drift 与 draft artifact 回滚的自动化 policy 仍待生产验证。

## Sources

- SpecBundle and SpecForge v0.2 — https://www.lmsys.org/blog/2025-12-23-spec-bundle-phase-1/（First Public: 2025-12-23；Accessed: 2026-07-31）
- SpecForge repository — https://github.com/sgl-project/SpecForge（Accessed: 2026-07-31）
- SpecBundle documentation — https://docs.sglang.io/SpecForge/SpecBundle/index.html（Accessed: 2026-07-31）
