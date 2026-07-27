# AI Research Weekly — 2025-W37

> Coverage Window: 2025-09-08～2025-09-14
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Qwen3-Next。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：Qwen3-Next（2025-09-10）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Qwen3-Next | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；作为模型架构→runtime co-design 案例 |

### Deep Analysis 1 — Qwen3-Next

- First Public: 2025-09-10
- Status: Official open-weight architecture release
- Primary Source: https://qwen.ai/blog?from=research.latest-advancements-listHugging&id=4074cca80393150c248e508aa62983f9cb7d27cd
- Evolution Relationship: Direct Evolution

#### Why

dense attention + dense FFN 的每-token成本随 context 和容量扩展；下一阶段需要同时稀疏 attention、稀疏 experts 并保持训练稳定与 serving 可实现。

#### Principle and Mechanism

Qwen3-Next 组合 hybrid attention、high-sparsity MoE、训练稳定技术与 multi-token prediction，目标是提高 training/inference efficiency。

#### Trade-off and Evidence Boundary

双重稀疏降低理论 FLOPs，却增加 state type、kernel coverage、routing imbalance、通信与 cache layout 复杂度；官方效率数据必须绑定硬件与实现。

#### Connection and Evolution

知识树位置：第 14、16、17、21、22、45、46 章。Must Read；作为模型架构→runtime co-design 案例。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### Qwen3-Next

- **Candidate / Week / Score:** Qwen3-Next / 2025-W37 / 27/30。
- **Source Family ID:** `QWEN3-NEXT-2025-09`。
- **Source Type:** official model card、architecture/config、deployment documentation、vendor evaluation。
- **First-public Date / Revision History:** official release/model card 2025-09-10；后续 framework support 与 checkpoint 不倒灌为初始能力。
- **Direct Primary Sources:** Qwen3-Next official Blog；Qwen3-Next-80B-A3B-Instruct model card/config；SGLang 与 vLLM deployment recipes。
- **Related Primary Sources:** Gated DeltaNet、YaRN、RULER；W29 MTP 与 W40 DSA 只作机制分支对照。
- **Access and Verification Status:** Verified for architecture、artifact、deployment contract与vendor evaluation；training topology、optimizer、data composition、kernel benchmark contract与production SLO Not Disclosed。
- **Full-read Coverage:** 已阅读model card的Highlights、完整architecture/config、training stage、capability/long-context tables、runtime requirements、MTP deployment、YaRN 1M extension、sampling与failure guidance；官方未发布独立technical report。
- **Original Problem:** total capacity与context同时扩展时，dense FFN和全dense attention使每token计算、KV/state与通信成本共同增长。
- **Why the Previous Design Was Reasonable:** dense attention保留任意token精确交互且kernel成熟；dense FFN和较低expert数更易优化、调试与跨backend部署。
- **Changed Constraint:** 15T-token training、256K原生context与80B total/3B active目标要求在容量、长度和active compute之间重新分配预算。
- **Mechanism:** 48 layers按12组重复“3个Gated DeltaNet+MoE、1个Gated Attention+MoE”；attention为16Q/2KV、DeltaNet为32V/16QK；MoE含512 routed experts、每token激活10个并加1 shared expert；MTP提供训练辅助与可选speculative path。
- **State Ownership:** DeltaNet recurrent state与attention KV由model/runtime共同定义；MoE router拥有expert assignment，serving engine拥有TP/EP、cache与MTP verification；YaRN config由部署者显式选择。
- **Control Flow / Data Flow:** token hidden state → 三层DeltaNet recurrent update/稀疏expert → 一层Gated Attention KV access/稀疏expert → MTP heads训练或runtime draft/verify；长于262,144时额外YaRN配置改变position mapping。
- **Implementation Details:** 80B total/3B activated、48 layers、hidden 2048；native 262,144，官方用static YaRN验证到约1.01M。MTP不由Transformers普遍支持，需SGLang/vLLM专用路径；官方示例为TP4，启动失败时建议降到32K。
- **Evaluation Setup:** capability表为vendor harness；1M RULER每长度260 samples（13 subtasks×20），Qwen3-Next用YaRN而Qwen3-2507用DCA，方法不同；10×吞吐与10%训练成本没有公开完整硬件、batch、精度、并发与SLO。
- **Baselines / Ablations / Sensitivity:** 有同族模型、长度与若干runtime配置比较；缺hybrid-vs-dense、MoE sparsity、stability tricks和MTP的受控消融，缺static YaRN短context影响的系统评测。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/active parameters、TP4示例、262K/1.01M长度披露；GPU型号、precision、batch/concurrency、TTFT/TPOT与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 公开artifact证明hybrid recurrent/attention、high-sparsity MoE与MTP可组合进同一模型/runtime contract；官方文档也明确吞吐收益依赖实现、MTP并非通用framework能力。
- **What It Does Not Prove:** 不证明10×吞吐跨硬件/workload成立，不证明1M context等于1M有效利用，不证明双重稀疏普遍优于dense/GQA，也不证明vendor benchmark独立可复现。
- **Limitations / Threats to Validity:** 无独立technical report；训练配方与hardware缺失；RULER方法不完全同构；static YaRN会影响短context；Instruct仅non-thinking mode。
- **Trade-offs / New Failure Modes:** active FLOPs与长程成本下降，但新增recurrent state、偶发global attention、expert routing、kernel coverage、MTP acceptance与position-scaling配置；backend缺实现会把理论效率变成fallback或启动失败。
- **Where the Previous Design Still Applies:** 短context、低并发、backend覆盖不足、需要完全精确token交互或更易审计行为时，dense/GQA与较低稀疏度仍合理。
- **Evolution Relationship:** `Layering / Dependency`：linear/recurrent compression与selective dense attention分工；MoE减少active FFN；MTP复用模型训练artifact做推理draft。三者不是单一“新attention替代旧attention”。
- **ROADMAP Node:** Ch14～17、Ch21～22、Ch44～46。
- **Target and Adjacent Chapters Read:** 已阅读 Ch13～22与Ch43～47；Ch22为architecture/context主owner，Ch44只接收MTP handoff。
- **Existing Coverage:** Ch22已有dense→hybrid→sparse路线和有效context边界；新增价值在“state类型与runtime coverage同时增加”，不能只重复型号规格。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，强调 hybrid state types 与 runtime coverage 一起增加。
- **Changed Files or Rejection Reason:** 已复核 `books/part-02-model/22-long-context.md`；MTP 仅 handoff Ch44。
- **Open Questions:** DeltaNet state memory/rollback、expert parallel topology、MTP acceptance、long-context quality与跨backend性能仍缺完整公开contract。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- Qwen3-Next → 第 14、16、17、21、22、45、46 章（Direct Evolution）

## Recommended Action

- Qwen3-Next：Must Read；作为模型架构→runtime co-design 案例

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W37/README.md。
- 新增 Qwen3-Next 候选级 Full Source Review；本阶段未修改 Books。

## Open Questions

- 双重稀疏的state ownership、kernel覆盖与MTP收益是否足以refine Ch22，待Books Gate。

## Sources

- Qwen3-Next — https://qwen.ai/blog?from=research.latest-advancements-listHugging&id=4074cca80393150c248e508aa62983f9cb7d27cd（First Public: 2025-09-10；Accessed: 2026-07-31）
- Qwen3-Next model card — https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct（Published: 2025-09-10；Accessed: 2026-07-31）
