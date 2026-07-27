# AI Research Weekly — 2025-W46

> Coverage Window: 2025-11-10～2025-11-16
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：JAX-Privacy 1.0。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：JAX-Privacy 1.0（2025-11-12）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| JAX-Privacy 1.0 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；与 user-level DP 形成 theory→runtime 链 |

### Deep Analysis 1 — JAX-Privacy 1.0

- First Public: 2025-11-12
- Status: Google Research official library/research release
- Primary Source: https://research.google/blog/differentially-private-machine-learning-at-scale-with-jax-privacy/
- Evolution Relationship: Direct Evolution

#### Why

DP 理论落地到 foundation-model training 时，per-example clipping、noise、accounting、microbatching 与 distributed sharding 必须共同正确。

#### Principle and Mechanism

JAX-Privacy 提供 clipping、correlated noise、batch construction、privacy accounting 与 auditing primitives，并适配 JAX parallelism。

#### Trade-off and Evidence Boundary

库降低误实现风险，却不能替用户选择 privacy unit、budget 与 threat model；分布式效率优化必须保持 accounting 等价。

#### Connection and Evolution

知识树位置：第 23～25、32、62、68 章。Must Read；与 user-level DP 形成 theory→runtime 链。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### JAX-Privacy 1.0

- **Candidate / Week / Score:** JAX-Privacy 1.0 / 2025-W46 / 25/30。
- **Source Family ID:** `JAX-PRIVACY-2025-11`。
- **Source Type:** Google Research official Blog、open-source library/documentation、algorithm references。
- **First-public Date / Revision History:** Blog发表于 2025-11-12并称 JAX-Privacy 1.0；当前 repository citation仍显示 0.4.0/2025且持续演进，公开版本标签存在歧义，任何实现事实须 pin具体release/commit。
- **Direct Primary Sources:** Google Research Blog；`google-deepmind/jax_privacy` repository README/docs/source。
- **Related Primary Sources:** DP-SGD、DP-FTRL、matrix-factorization correlated noise、DP accounting与 empirical auditing论文/库；用于核验原语语义，不把library packaging算作新算法。
- **Access and Verification Status:** Verified for library design and public APIs；Blog的“1.0”与repository可见版本对应关系 `Not Fully Resolved`；具体训练配置的privacy guarantee必须重新计算。
- **Full-read Coverage:** 已阅读 clipping/noise/batch construction、DP-SGD/DP-FTRL、matrix factorization、microbatch/padding、JAX `vmap`/`shard_map`、accounting、canary/auditing、repository caveats与citation/version metadata。
- **Original Problem:** 大模型分布式训练中，per-example gradient、clipping、noise、microbatch、padding和sharding若分散实现，容易使“代码运行”与声明的邻接关系/accountant不一致。
- **Why the Previous Design Was Reasonable:** 研究代码或单机 DP-SGD 直接实现易于验证；较小模型上不需要复杂 sharding、correlated noise与高吞吐batch orchestration。
- **Changed Constraint:** foundation-model scale要求将DP机制嵌入 JAX SPMD训练，同时降低 per-example gradient memory/compute，并保留formal accounting与empirical audit。
- **Mechanism:** library组合per-example clipping、Gaussian或correlated noise、batch/microbatch构造、DP-SGD/DP-FTRL optimizer、matrix-factorization queries、privacy accountant与canary/auditing；`vmap`/`shard_map`承载并行执行。
- **State Ownership:** training loop拥有sampling/step/optimizer state；DP optimizer拥有clipping/noise state；accountant拥有privacy-event composition；distributed runtime拥有sharding；operator拥有privacy unit、adjacency、budget和threat model。
- **Control Flow / Data Flow:** sample/microbatch → per-example gradient → norm/clipping → aggregate → calibrated noise/correlated query → optimizer update；每一步privacy event进入accountant，canary/audit作为独立经验检查而非formal proof替代。
- **Implementation Details:** padding与microbatch影响clipping与sample rate；matrix-factorization noise跨step相关，必须让runtime state与accountant事件一致。repository明确包含research components/rough edges，不等于 turnkey compliance。
- **Evaluation Setup:** Blog/repository展示可扩展训练构件和示例；没有一个统一公开的model、hardware、dataset、epsilon/delta、batch、steps、throughput与quality benchmark可支持普遍效率结论。
- **Baselines / Ablations / Sensitivity:** 算法文献分别比较DP-SGD、DP-FTRL与matrix factorization；launch材料没有把所有原语置于相同 workload contract 的完整ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** JAX accelerator/SPMD支持已披露；具体hardware、model、precision、sequence length、global/micro batch、steps、epsilon/delta与training SLO Not Disclosed。
- **What the Evidence Actually Proves:** 大规模DP训练需要把机制、分布式执行、accounting与auditing作为同一runtime contract；library公开了可检查的组合点。
- **What It Does Not Prove:** 不证明使用library就获得DP、不替用户选择user-level还是example-level邻接、不证明任意sharding/gradient accumulation与accountant等价，也不证明经验攻击未发现泄露即可替代formal guarantee。
- **Limitations / Threats to Validity:** version标签歧义、research-code caveat、配置组合复杂、sampling与distributed semantics易漂移；auditing只覆盖选择的canary/attack。
- **Trade-offs / New Failure Modes:** 统一库减少重复错误，却新增 accountant/runtime version coupling、correlated-noise state恢复、padding/sample-rate错误、checkpoint replay、distributed RNG与配置审计复杂度。
- **Where the Previous Design Still Applies:** 小模型、单机或只需简单 DP-SGD时，更小且可形式化验证的实现可能更安全；非敏感训练不应无条件承担DP效用/吞吐成本。
- **Evolution Relationship:** `Direct Evolution`：DP theorem/optimizer → scalable JAX execution → accountant+audit operational contract；工程封装不改变隐私定义，反而要求更严格的配置一致性。
- **ROADMAP Node:** Ch23～25、Ch32、Ch62、Ch68。
- **Target and Adjacent Chapters Read:** 已读 Ch23～25、Ch31～32、Ch62、Ch67～69；Ch68 为主 owner。
- **Existing Coverage:** provisional Ch68修改已提到 clipping/noise/accounting；必须重新核对是否清楚区分 privacy definition、mechanism、runtime与audit。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，区分 privacy definition、mechanism、distributed runtime 与 audit。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/68-security.md`。
- **Open Questions:** 1.0 artifact对应commit、distributed RNG/checkpoint恢复、gradient accumulation/padding与accountant等价性的测试方式。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- JAX-Privacy 1.0 → 第 23～25、32、62、68 章（Direct Evolution）

## Recommended Action

- JAX-Privacy 1.0：Must Read；与 user-level DP 形成 theory→runtime 链

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W46/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- 分布式 clipping/noise 优化是否与声明的 accountant 等价，仍需配置级审计与测试。

## Sources

- JAX-Privacy 1.0 — https://research.google/blog/differentially-private-machine-learning-at-scale-with-jax-privacy/（First Public: 2025-11-12；Accessed: 2026-07-31）
- JAX-Privacy repository — https://github.com/google-deepmind/jax_privacy（Accessed: 2026-07-31）
