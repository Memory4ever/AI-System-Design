# AI Research Weekly — 2025-W45

> Coverage Window: 2025-11-03～2025-11-09
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：Kimi K2 Thinking、SGLang Diffusion。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：Kimi K2 Thinking（2025-11-06）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 保留：SGLang Diffusion（2025-11-07）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kimi K2 Thinking | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；不以 benchmark 修改正文 |
| SGLang Diffusion | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；作为 runtime abstraction 边界 |

### Deep Analysis 1 — Kimi K2 Thinking

- First Public: 2025-11-06
- Status: Official open-weight model card
- Primary Source: https://huggingface.co/moonshotai/Kimi-K2-Thinking
- Evolution Relationship: Direct Evolution

#### Why

agentic reasoning 需要跨多轮保留 thinking/tool state，而不仅是单轮增加 token budget。

#### Principle and Mechanism

官方模型卡披露 thinking 与 tool-call 行为；训练机制与独立复现不足。

#### Trade-off and Evidence Boundary

长 horizon 提高复杂任务覆盖，也放大上下文、成本、state corruption 与 parser compatibility。

#### Connection and Evolution

知识树位置：第 20、29、52、74～77 章。Worth Watching；不以 benchmark 修改正文。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

### Deep Analysis 2 — SGLang Diffusion

- First Public: 2025-11-07
- Status: Official open-source project/blog
- Primary Source: https://www.lmsys.org/blog/2025-11-07-sglang-diffusion/
- Evolution Relationship: Principle Reuse

#### Why

serving runtime 的 scheduler、API 与 kernel orchestration 原语可扩展到 image/video diffusion，但 state 与 iteration semantics 不同。

#### Principle and Mechanism

项目把多类 diffusion models 接入 SGLang runtime 与 kernel stack。

#### Trade-off and Evidence Boundary

统一平台降低运维碎片，不应隐藏 LLM token decode 与 diffusion denoising 的状态、batching 和 SLO 差异。

#### Connection and Evolution

知识树位置：第 45、47、53 章。Worth Watching；作为 runtime abstraction 边界。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### Kimi K2 Thinking

- **Candidate / Week / Score:** Kimi K2 Thinking / 2025-W45 / 23/30。
- **Source Family ID:** `KIMI-K2-THINKING-2025-11`。
- **Source Type:** official model card、weights/config 与 serving instructions。
- **First-public Date / Revision History:** 2025-11-06；作为 W28 Kimi K2 release/technical-report family 的 thinking/QAT 后训练分支，不重算 base architecture 为本周新发现。
- **Direct Primary Sources:** Moonshot AI official Hugging Face model card、config与 weights metadata。
- **Related Primary Sources:** Kimi K2 technical report与 W28 Source Review；用于继承 base architecture，避免从 Thinking card 反推未披露训练过程。
- **Access and Verification Status:** Verified for public artifact、architecture/config、evaluation harness；post-training data、QAT recipe、hardware与完整 serving contract Not Disclosed。
- **Full-read Coverage:** 已阅读完整 model card 的 architecture、native INT4、tool-call format、deployment、benchmark setup、run counts、context-overflow handling与 limitations，并核对 config/weights metadata。
- **Original Problem:** 长 horizon reasoning/agent workflow 需要在多轮工具交互中维持计划与状态，同时 1T MoE 的 decode cost 使高 reasoning budget 更昂贵。
- **Why the Previous Design Was Reasonable:** 短 CoT 或独立 tool call 更容易控制 context、latency 与 parser failure；BF16 权重避免量化训练复杂度和兼容风险。
- **Changed Constraint:** search/tool benchmark允许百级步骤和 96K～128K thinking budget；长轨迹放大 decode cost，也要求 context overflow 时有明确历史保留策略。
- **Mechanism:** 1T total/32B active、61层、384 routed experts选8加1 shared、MLA、256K context；post-training QAT 产生原生 INT4 weight-only MoE；工具调用使用专门格式并在部分评测中保留 reasoning state。
- **State Ownership:** model生成 reasoning/tool call；harness维护工具结果、step budget与context overflow；serving runtime负责量化 kernel、KV与调度；外部 evaluator拥有任务终止与正确性。
- **Control Flow / Data Flow:** prompt+tools → reasoning → tool call → tool result追加 → 下一轮 reasoning；超过 context 时评测 harness隐藏既往 tool outputs而非证明模型自身具备稳定 memory compaction。
- **Implementation Details:** 所有公布 benchmark 使用 INT4；model card称 native INT4 QAT相对未量化约2× generation speed，但未披露 hardware、batch、kernel与SLO，不能泛化。
- **Evaluation Setup:** tool/search任务最高 300 steps，HLE最高120；thinking budget 96K/128K、context 256K、temperature 1；不同 benchmark 使用不同 tools、judge、run count，card有逐项说明。
- **Baselines / Ablations / Sensitivity:** 对同类模型给 benchmark comparison；没有公开 BF16 vs QAT 的质量/速度完整消融，也没有工具错误、context compaction策略与 step budget sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** K2 Thinking、INT4、256K context和若干 max thinking/steps已披露；hardware、batch、concurrency、arrival process、TTFT/ITL SLO Not Disclosed。
- **What the Evidence Actually Proves:** artifact支持长 context、专门 tool syntax与原生 INT4；在作者指定 harness/预算中可完成长工具链任务。
- **What It Does Not Prove:** 不证明“200～300次稳定调用”是生产 reliability，不证明量化在任意 runtime 2×，也不公开 agent training具体机制。
- **Limitations / Threats to Validity:** vendor benchmark、超大 token/step budget、context overflow时丢弃旧 tool output、不同 judge/tooling；质量、成本与可靠性高度依赖 harness。
- **Trade-offs / New Failure Modes:** 更长 horizon提高任务覆盖，却新增 tool-state corruption、context truncation、循环/超预算、parser mismatch、量化 kernel依赖与长尾资源占用。
- **Where the Previous Design Still Applies:** 短交互、严格 SLO、高可预测成本或工具副作用高时，较短 reasoning budget、显式 workflow与较小模型仍更合理。
- **Evolution Relationship:** `Direct Evolution`：base MoE → reasoning/tool post-training → long-horizon harness+quantized serving；能力来自模型、harness与runtime组合，不能归因给单一层。
- **ROADMAP Node:** Ch20、Ch29、Ch52、Ch74～77。
- **Target and Adjacent Chapters Read:** 已读 Ch20、Ch28～29、Ch51～52、Ch73～77；具体观点已由 Ch20/52/77 覆盖。
- **Existing Coverage:** provisional mapping认为 Ch77已有 workflow state观点；是否新增“context overflow policy属于 harness state”需逐段去重。
- **Integration Decision:** `No Change — Already Covered`；Ch20/52/77 已覆盖 reasoning budget、context overflow 与 workflow state ownership。
- **Changed Files or Rejection Reason:** 不改 Books；产品 benchmark 不增加新机制。
- **Open Questions:** 原生 INT4 QAT recipe、BF16 quality delta、tool-state保留与 overflow policy、真实 runtime workload contract。

### SGLang Diffusion

- **Candidate / Week / Score:** SGLang Diffusion / 2025-W45 / 22/30。
- **Source Family ID:** `SGLANG-DIFFUSION-2025-11`。
- **Source Type:** official engineering Blog、repository implementation/roadmap。
- **First-public Date / Revision History:** 2025-11-07；本记录固定初始公开范围，后续 batching/quantization/cache支持不回写为 launch 能力。
- **Direct Primary Sources:** LMSYS/SGLang official Blog；SGLang `multimodal_gen` repository path与 FastVideo integration references。
- **Related Primary Sources:** SGLang scheduler/kernel docs、FastVideo official repository；用于确认 reuse boundary。
- **Access and Verification Status:** Verified for launch architecture and stated feature scope；production workload、failure semantics与independent benchmark Not Disclosed。
- **Full-read Coverage:** 已阅读 pipeline/stage abstraction、denoise/VAE path、USP/CFG/TP parallelism、FastVideo增强、benchmark图、limitations与2026 roadmap。
- **Original Problem:** image/video diffusion serving与LLM serving共享GPU orchestration、API、distributed kernels等基础设施，却有不同的迭代状态和数据形状；独立栈造成运维碎片。
- **Why the Previous Design Was Reasonable:** Diffusers/FastVideo等专用runtime能直接表达 denoising loop、VAE与media preprocessing，不必迁就 token scheduler abstraction。
- **Changed Constraint:** 平台希望用同一 serving/runtime团队维护多模态生成，并复用并行和kernel优化，同时避免把差异藏掉。
- **Mechanism:** `ComposedPipelineBase`由多个 `PipelineStage`组合，典型为denoise stage与VAE decode；复用scheduler/kernel orchestration，分布式采用USP（Ulysses+Ring）、CFG parallel与tensor parallel。
- **State Ownership:** pipeline编排器拥有stage DAG/lifecycle；denoise stage拥有timestep/latent state；VAE stage拥有decode state；scheduler负责device/batch placement；distributed backend负责sharding/collective。
- **Control Flow / Data Flow:** text/media input → encode/conditioning → repeated latent denoise → VAE decode → media output；与 autoregressive token-by-token KV演进不是同一 state machine。
- **Implementation Details:** 基于并增强 FastVideo fork；launch强调多模型接入，但 batching、quantization、cache/attention enhancements仍在 roadmap，不能称与LLM serving feature parity。
- **Evaluation Setup:** 作者图表在 H100/H200 上对若干 image/video pipelines与 Diffusers baseline比较，报告 1.2～5.9×；公开页面未给每张图完整 batch、resolution、steps、precision、warmup与SLO合同。
- **Baselines / Ablations / Sensitivity:** 有 Diffusers baseline与不同并行策略展示；缺跨resolution/denoise steps、并发、队列、冷启动、quality和fault sensitivity的完整消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100/H200与部分模型可辨识；resolution、frames、steps、precision、batch、concurrency和端到端SLO不完整，性能数字不得外推。
- **What the Evidence Actually Proves:** 通用 serving runtime可以通过pipeline/stage边界复用 orchestration 和并行原语，而仍为 diffusion保留专门 state/data path。
- **What It Does Not Prove:** 不证明一个 token scheduler 可直接服务 diffusion、不证明统一栈总是更快/更简单，也不证明 production-ready feature parity。
- **Limitations / Threats to Validity:** launch benchmark条件不完整；roadmap能力未实现；fork同步、media quality与多stage backpressure未充分披露。
- **Trade-offs / New Failure Modes:** 统一控制面降低重复建设，却引入stage backpressure、latent/activation memory峰值、quality/performance coupling、fork drift与跨pipeline调试。
- **Where the Previous Design Still Applies:** 单一模型、research迭代或专用 quality pipeline 中，Diffusers/FastVideo等专用栈更直接；统一runtime适合需要共同运维和跨模型资源治理的平台。
- **Evolution Relationship:** `Principle Reuse`：复用scheduler/parallel/kernel原则，但 token decode 与 denoising 是不同 state machine；不是直接替代关系。
- **ROADMAP Node:** Ch45、Ch47、Ch53。
- **Target and Adjacent Chapters Read:** 已读 Ch45～47、Ch52～54；Ch53 的 platform boundary 已覆盖共享控制面与独立 state machine。
- **Existing Coverage:** Ch53 已用 control/data/evidence plane 覆盖“可共享平台 contract，不共享 workload state machine”；本候选不再重复写入。
- **Integration Decision:** `No Change — Already Covered`；Ch53 的 control/data plane 已允许共享平台 contract 而保留不同 runtime state machines。
- **Changed Files or Rejection Reason:** 不改 Books；避免把新 workload family 写成通用 serving 等价。
- **Open Questions:** batching/backpressure、multi-stage failure recovery、quality regression、pipeline cache与统一SLO schema。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- Kimi K2 Thinking → 第 20、29、52、74～77 章（Direct Evolution）
- SGLang Diffusion → 第 45、47、53 章（Principle Reuse）

## Recommended Action

- Kimi K2 Thinking：Worth Watching；不以 benchmark 修改正文
- SGLang Diffusion：Worth Watching；作为 runtime abstraction 边界

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W45/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- Kimi K2 Thinking 的 QAT、tool-state 与 overflow policy 如何拆分模型、harness、runtime责任？
- SGLang Diffusion 的 stage backpressure、failure recovery和 quality/SLO contract如何定义？

## Sources

- Kimi K2 Thinking — https://huggingface.co/moonshotai/Kimi-K2-Thinking（First Public: 2025-11-06；Accessed: 2026-07-31）
- SGLang Diffusion — https://www.lmsys.org/blog/2025-11-07-sglang-diffusion/（First Public: 2025-11-07；Accessed: 2026-07-31）
- SGLang repository — https://github.com/sgl-project/sglang/tree/main/python/sglang/multimodal_gen（Accessed: 2026-07-31）
