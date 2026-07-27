# AI Research Weekly — 2025-W44

> Coverage Window: 2025-10-27～2025-11-02
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：gpt-oss-safeguard、SGLang-JAX。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：gpt-oss-safeguard（2025-10-29）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 保留：SGLang-JAX（2025-10-29）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| gpt-oss-safeguard | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；作为 policy-as-data 的受限案例 |
| SGLang-JAX | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；沉淀 backend portability 的分层边界 |

### Deep Analysis 1 — gpt-oss-safeguard

- First Public: 2025-10-29
- Status: Official open-weight research preview
- Primary Source: https://openai.com/index/introducing-gpt-oss-safeguard/
- Evolution Relationship: Direct Evolution

#### Why

固定 label classifier 难以覆盖组织特定、持续变化的安全 policy；把 policy 文本作为运行时输入可提高可配置性。

#### Principle and Mechanism

Safety Reasoner 接收 taxonomy/policy 与待分类内容，通过 reasoning 输出分类；模型是 gpt-oss 的 safety fine-tune。

#### Trade-off and Evidence Boundary

可编程 policy 降低重训频率，却增加 prompt injection、policy ambiguity、latency 与理由不忠实风险；research preview 不替代 deterministic controls。

#### Connection and Evolution

知识树位置：第 62、68、74、77 章。Must Read；作为 policy-as-data 的受限案例。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

### Deep Analysis 2 — SGLang-JAX

- First Public: 2025-10-29
- Status: Official open-source project/blog
- Primary Source: https://www.lmsys.org/blog/2025-10-29-sglang-jax/
- Evolution Relationship: Layering / Dependency

#### Why

TPU 原生 serving 不能简单复用 CUDA kernel 路径，但上层 request/KV/scheduler contract 仍有复用价值。

#### Principle and Mechanism

SGLang-JAX 以 JAX/XLA/Pallas 实现 attention/MoE kernels，并复用 RadixCache、overlap scheduler、EP 与 speculative decoding semantics。

#### Trade-off and Evidence Boundary

共享上层架构减少语义分裂，backend-specific kernels 保留性能；代价是 feature parity、编译 shape、debugging 与双实现维护。

#### Connection and Evolution

知识树位置：第 45、47、50～52 章。Must Read；沉淀 backend portability 的分层边界。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### gpt-oss-safeguard

- **Candidate / Week / Score:** gpt-oss-safeguard / 2025-W44 / 24/30。
- **Source Family ID:** `OPENAI-GPT-OSS-SAFEGUARD-2025-10`。
- **Source Type:** official research-preview Blog、technical report、model card。
- **First-public Date / Revision History:** 2025-10-29；本记录只使用发布日可见的 research preview、报告与权重说明，后续 moderation 产品变化不回写为该模型能力。
- **Direct Primary Sources:** OpenAI announcement；《Research Preview of gpt-oss-safeguard》technical report；gpt-oss-safeguard-120b model card。
- **Related Primary Sources:** gpt-oss base model card与 Harmony response format；仅用于确认继承架构和运行接口。
- **Access and Verification Status:** Verified；训练数据、训练算力、完整 policy 分布与 production traffic contract Not Disclosed。
- **Full-read Coverage:** 已阅读全文的 motivation、model/training overview、internal multi-policy、Moderation 2022、ToxicChat、instruction hierarchy、jailbreak、limitations、deployment guidance，并核对 model card 的架构、Harmony 与非 chat-model 警告。
- **Original Problem:** 固定 taxonomy classifier 对组织特定且持续变化的 policy 需要重标注、重训练；通用模型直接判定又难以保证一致输出与成本。
- **Why the Previous Design Was Reasonable:** 专用 classifier 延迟低、输出稳定、易校准，在 policy 稳定且有足够标签时通常更可靠。
- **Changed Constraint:** policy 数量、语言与产品 surface 持续变化，长尾规则很难为每一项维护独立大规模数据集。
- **Mechanism:** 在 inference 时把 policy 文本与待审内容共同输入 safety reasoner，由从 gpt-oss 经人类专家判断数据 RFT 得到的模型生成 reasoning 与 label；120B/20B 继承 base architecture 与 Harmony format。
- **State Ownership:** policy owner 负责规则文本与版本；reasoner 负责非确定性解释/分类；调用方负责 schema parsing、timeout、fallback、审计与最终 enforcement。
- **Control Flow / Data Flow:** 高召回小 classifier 可先 triage → policy+content 进入 safety reasoner → Harmony reasoning/final label → deterministic enforcement/人工升级；报告建议 defense in depth，而非单点替代。
- **Implementation Details:** 公开 120B/20B 权重；模型不是面向最终用户的 chatbot；raw CoT 可能 hallucinate 且未保证 faithful，不能作为唯一审计证据。
- **Evaluation Setup:** internal 多 policy gold set、Moderation 2022、ToxicChat，以及 instruction-hierarchy/jailbreak evaluations；比较 internal reasoner、gpt-5 thinking 与 gpt-oss-safeguard 两个尺寸。
- **Baselines / Ablations / Sensitivity:** internal accuracy 中 120B/20B 为 46.3/43.6，internal reasoner 52.2，gpt-5 thinking 43.2；公开 moderation 数据集上给 F1；没有 policy 长度、语言、adversarial distribution 与 latency sensitivity 的完整公开消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型尺寸与公开数据集已披露；hardware、precision、policy/content length、batch、concurrency、latency SLO Not Disclosed。报告称部分内部 launch 中 reasoner 最高占总 compute 16%，不能外推。
- **What the Evidence Actually Proves:** policy-as-data 可以在同一模型上支持多 taxonomy，并在给定作者评测中达到可用分类质量；也证明团队实际采用“廉价 triage + 昂贵 reasoner”的分层成本模型。
- **What It Does Not Prove:** 不证明优于有大量领域标签的专用 classifier，不证明 CoT faithful，不证明抗 prompt injection，也不证明 production reliability 或成本普遍可接受。
- **Limitations / Threats to Validity:** internal set 不公开；专用 classifier 在数万标签时可能更优；20B jailbreak 评测弱于 base；instruction hierarchy 常未优于 base；模型生成理由可能错误。
- **Trade-offs / New Failure Modes:** policy 更新免重训、覆盖长尾，却引入 policy ambiguity、prompt injection、nondeterminism、长尾 latency、parser failure、policy/model version coupling 与解释误导。
- **Where the Previous Design Still Applies:** 高频稳定规则、严格 latency、可校准阈值和高质量标签充分时，专用 deterministic classifier 仍应承担主路径；reasoner适合灰区、异步复核或快速迭代 policy。
- **Evolution Relationship:** `Direct Evolution`：固定 classifier → policy-conditioned reasoner → tiered classifier/reasoner/enforcement；后者扩展 policy flexibility，不否定旧方案的低延迟与可校准性。
- **ROADMAP Node:** Ch62、Ch68、Ch74、Ch77。
- **Target and Adjacent Chapters Read:** 已读 Ch62、Ch68、Ch74、Ch77 及相邻章节；Ch68 为主 owner，Ch77 仅接 deterministic enforcement handoff。
- **Existing Coverage:** Ch68 原有 defense-in-depth 缺少 policy-as-data 边界，本轮已补充；Ch77 只承接 workflow enforcement handoff。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，沉淀 policy-as-data 与 deterministic enforcement 边界。
- **Changed Files or Rejection Reason:** 已更新 `books/part-05-ai-infrastructure/68-security.md`。
- **Open Questions:** policy versioning、跨语言一致性、reasoning faithfulness、cache/replay 边界、fallback 与 adversarial robustness 如何形成可审计 runtime contract。

### SGLang-JAX

- **Candidate / Week / Score:** SGLang-JAX / 2025-W44 / 25/30。
- **Source Family ID:** `SGLANG-JAX-2025-10`。
- **Source Type:** official engineering Blog、open-source repository/documentation。
- **First-public Date / Revision History:** 2025-10-29；本记录固定 launch 时 feature set，repository 后续演进单独按版本核验。
- **Direct Primary Sources:** LMSYS/SGLang official launch Blog；`sgl-project/sglang-jax` repository README、examples/config。
- **Related Primary Sources:** JAX `shard_map`、Pallas 与 TPU documentation；仅用于解释 compiler/kernel substrate。
- **Access and Verification Status:** Verified for architecture and launch scope；independent reproduction、production failure semantics与跨 TPU generation portability Not Disclosed。
- **Full-read Coverage:** 已阅读 runtime architecture、RadixAttention/RadixCache、overlap scheduler、Pallas attention/MoE、EAGLE2/3、RPA v3、EP MoE、benchmark配置、limitations与 roadmap，并核对 repository 的 run/config surface。
- **Original Problem:** CUDA-centric serving runtime 的上层调度语义有价值，但 kernel、collective、graph compilation 与 device memory path 不能原样搬到 TPU/JAX。
- **Why the Previous Design Was Reasonable:** 为 CUDA/NCCL/Triton 专门优化可减少 abstraction overhead，并快速利用成熟 GPU kernels；单 backend 时双实现成本没有必要。
- **Changed Constraint:** 相同模型与 serving semantics 需要覆盖 TPU，同时保持 prefix reuse、continuous batching、speculative decoding 与 EP，而不是重建另一套互不兼容的产品层。
- **Mechanism:** 上层复用 OpenAI API、RadixCache 与 overlap scheduler；下层以 JAX/XLA、Flax、`shard_map`、Pallas kernels 实现 attention/MoE，并预编译离散 batch-size graphs；CPU 准备 batch N+1 与 TPU 执行 batch N 重叠。
- **State Ownership:** scheduler 拥有 request/batch lifecycle；RadixCache 拥有 prefix/KV index；JAX/XLA 拥有 executable/shape compilation；Pallas/collective kernels 拥有 device-local data movement。
- **Control Flow / Data Flow:** request 入队与 prefix match → 选择已编译 batch shape → CPU 准备下批、TPU执行当前批 → KV/Radix state 更新 → token streaming；speculative path 增加 draft/verify 与 non-causal mask。
- **Implementation Details:** RPA v3 对 verify workload 调整 mask/cache；EPMoE 使用 MegaBlox/ragged all-to-all，少于约 64 个大 expert 时保留 FusedMoE fallback；Blog 示例包含 TP=4 TPU、BF16、page size 128、最大 requests 256。
- **Evaluation Setup:** 作者在 TPU 配置上报告 CPU scheduling gap 与 Qwen3-32B MoE/serving 对比；图表为 launch benchmark，不是跨 GPU/TPU cost-normalized study。
- **Baselines / Ablations / Sensitivity:** 作者称 CPU gap 从 12ms→38μs、另一配置 7ms→24μs；EPMoE 在典型配置相对 native `ragged_dot` 的 end-to-end ITL 改善 3～4×；缺完整 request mix、sequence-length、arrival process、SLO 与 compiler-cache sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TPU generation/拓扑并非所有图表均清楚；Qwen3-32B、BF16、TP4、page 128、max requests 256仅覆盖部分实验；输入输出长度、arrival、并发分布与 SLO不完整。
- **What the Evidence Actually Proves:** 同一 serving contract 可以分层复用到 JAX/TPU，同时必须保留 compiler-与 kernel-specific backend；作者实现也证明 overlap 与 shape precompile 是 TPU serving 的关键控制面问题。
- **What It Does Not Prove:** 不证明一个 kernel 实现可跨 backend 复用、不证明 feature parity、成本更低或所有模型更快；Blog benchmark 不能外推至生产流量。
- **Limitations / Threats to Validity:** launch 时 PD disaggregation、hierarchical KV 等仍在 roadmap；预编译 shape 集合会带来冷启动/coverage trade-off；双 backend 调试和语义一致性成本高。
- **Trade-offs / New Failure Modes:** 上层统一减少平台碎片，却新增 graph-cache miss/recompile、shape explosion、backend parity drift、collective/topology差异与跨层 profiling 难度。
- **Where the Previous Design Still Applies:** CUDA-only、kernel maturity 优先或 feature parity要求高时原 SGLang GPU path 更合理；JAX/TPU path服务不同硬件 contract，而非普遍替代。
- **Evolution Relationship:** `Layering / Dependency`：共享 request/KV/scheduler semantics → backend compiler/runtime → hardware-specific kernels/collectives；portability来自清晰边界，不是消除差异。
- **ROADMAP Node:** Ch45、Ch47、Ch50～52。
- **Target and Adjacent Chapters Read:** 已读 Ch44～52；Ch45 为 portability 主 owner，Ch47 仅保留 runtime implementation handoff。
- **Existing Coverage:** provisional mapping称已有调度/KV分层；是否缺少“semantic portability vs kernel portability”需在 Ch45～52逐段核验。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch45，区分 semantic portability 与 kernel portability。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/45-tensorrt-llm.md`；不外推 vendor benchmark。
- **Open Questions:** graph cache 的容量/淘汰、TPU fault semantics、PD disaggregation、跨 backend differential testing 与相同 workload contract 下的 cost/performance。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- gpt-oss-safeguard → 第 62、68、74、77 章（Direct Evolution）
- SGLang-JAX → 第 45、47、50～52 章（Layering / Dependency）

## Recommended Action

- gpt-oss-safeguard：Must Read；作为 policy-as-data 的受限案例
- SGLang-JAX：Must Read；沉淀 backend portability 的分层边界

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W44/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- gpt-oss-safeguard 的 policy versioning、reasoning faithfulness 与 fallback 怎样进入可审计 runtime contract？
- SGLang-JAX 的 graph cache、backend parity 与 fault semantics 怎样验证？

## Sources

- gpt-oss-safeguard — https://openai.com/index/introducing-gpt-oss-safeguard/（First Public: 2025-10-29；Accessed: 2026-07-31）
- gpt-oss-safeguard technical report — https://cdn.openai.com/pdf/08b7dee4-8bc6-4955-a219-7793fb69090c/Technical_report__Research_Preview_of_gpt_oss_safeguard.pdf（Published: 2025-10-29；Accessed: 2026-07-31）
- gpt-oss-safeguard-120b model card — https://huggingface.co/openai/gpt-oss-safeguard-120b（Accessed: 2026-07-31）
- SGLang-JAX — https://www.lmsys.org/blog/2025-10-29-sglang-jax/（First Public: 2025-10-29；Accessed: 2026-07-31）
- SGLang-JAX repository — https://github.com/sgl-project/sglang-jax（Accessed: 2026-07-31）
