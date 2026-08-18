# AI Research Weekly — 2025-W15

> Coverage Window: 2025-04-07～2025-04-13
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 41/41 Scored Owners Reconciled
> Discovery / Archive Gate: Conditional Open
> Historical Books Gate: Closed

## Executive Summary

W15 已从旧的 28-owner lower bound 修正为 **41 个 scored owner identities：34 个 20+、7 个低分**。原有 20 份 strict packet 经复核保留；A2A 通过收窄到 launch-day 可证事实完成 replacement review；W16 明示的 13 个 pre-04-14 family 已全部按 arXiv v1 回拨，并各自完成 Full Source Review。最终 ordinary Review Pending、Blocked、Disputed 均为 0。

Candidate Evidence Gate 通过；Discovery / Archive Completion Gate 仍为 Conditional Open，因为缺少可复算的 Scholar/OpenAlex/DBLP/Crossref 全量导出，并且 A2A 2025-04-09 source tree 没有 cryptographic pin。该 P3 archive gap 不影响当前收窄后的机制结论，但禁止把后来 schema 字段回投到首发日。

Historical Books Gate 保持关闭。本周恢复只修复 Weekly 证据，不写 Books。

## Coverage Window and Limitations

- ISO window 为 Monday 2025-04-07 至 Sunday 2025-04-13。
- arXiv 论文按 v1 first-public date 归档；manuscript date、HF submission date 与后来 revision 不替代事件日期。
- benchmark 结论严格绑定论文披露的模型、数据、硬件、precision、length、batch/concurrency 和 evaluator contract；Not Disclosed 不做推断。
- 13 个 W16 spillback 已回拨 W15；vLLM v0.8.4 的 2025-04-14 首发仍属于 W16。
- A2A exact event-time repository tree 保留 Archive P3 请求；当前只保留公告和可验证的 launch-level task boundary。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序完成重放。Kimi-VL、A2A、Google ADK、Ironwood、Nova Sonic 等保留为本周事件；Nemotron 模型卡自报 2025-03-18，回拨 W12，不以 04-08 权重活动重复计分。

## 2. 论文与学术来源

按 arXiv → Scholar → OpenAlex → DBLP → Semantic Scholar/Hugging Face discovery → Crossref metadata 重放并回到 primary source。W16 的 Seaweed、GigaTok、MineWorld、VLM-R1、PixelFlow、Pangu Ultra、SpecReason、PRIMA.cpp、VL-Rethinker、AgentRewardBench、AI Scientist-v2、DUMP、MLRC-Bench 均按 v1 日期返回 W15。

## 3. AI Infra 与工程项目

固定 Infra 顺序已复核。SGLang v0.4.5 保留；TensorRT-LLM v0.18.1 与 Transformers v4.51.1/2 完成低分闭合；vLLM v0.8.4 留 W16，vLLM Q2 roadmap issue 回 W13。

## Corrected Score Ledger

| Candidate | N | I | P | R | K | L | Total | Disposition |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kimi-VL | 4 | 4 | 3 | 4 | 4 | 3 | 22 | Weekly Only — Experimental |
| Agent2Agent / A2A | 4 | 5 | 5 | 5 | 5 | 4 | 28 | Refine Candidate — narrowed launch boundary |
| Google ADK v0.1.0 | 3 | 4 | 5 | 5 | 5 | 4 | 26 | No Change — Existing contract |
| Ironwood TPU | 4 | 5 | 4 | 5 | 4 | 3 | 25 | Weekly Only — Hardware fact |
| Amazon Nova Sonic | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Weekly Only — Mechanism not disclosed |
| Hogwild! Inference | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Refine Candidate |
| HybriMoE | 4 | 5 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| VAPO | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Refine Candidate |
| OLMoTrace | 5 | 5 | 5 | 5 | 5 | 3 | 28 | Refine Candidate |
| SmolVLM | 4 | 4 | 5 | 5 | 4 | 4 | 26 | Refine Candidate |
| One-Minute Video Generation with TTT | 5 | 4 | 3 | 5 | 4 | 4 | 25 | Emerging / Experimental |
| T1 / Tool-integrated Verification | 4 | 4 | 4 | 5 | 5 | 4 | 26 | Refine Candidate |
| Quantization Hurts Reasoning? | 4 | 5 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| A Sober Look at Progress in LM Reasoning | 4 | 5 | 5 | 5 | 5 | 4 | 28 | Refine Candidate |
| SkillWeaver | 5 | 4 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| Auditing Model Substitution in LLM APIs | 4 | 5 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| Scaling Laws for Native Multimodal Models | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Refine Candidate |
| Missing Premise exacerbates Overthinking | 4 | 4 | 4 | 5 | 5 | 3 | 25 | Refine Candidate |
| DDT | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Emerging / Experimental |
| C3PO | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Emerging / Experimental |
| SGLang v0.4.5 | 4 | 5 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| Seaweed-7B | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Refine Candidate |
| GigaTok | 5 | 4 | 4 | 5 | 5 | 4 | 27 | Refine Candidate |
| MineWorld | 5 | 5 | 4 | 5 | 5 | 3 | 27 | Refine Candidate |
| VLM-R1 | 4 | 4 | 4 | 5 | 5 | 4 | 26 | Refine Candidate |
| PixelFlow | 5 | 4 | 3 | 5 | 4 | 4 | 25 | Emerging / Experimental |
| Pangu Ultra | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Refine Candidate |
| SpecReason | 5 | 5 | 5 | 5 | 5 | 3 | 28 | Refine Candidate |
| PRIMA.cpp | 5 | 5 | 5 | 5 | 5 | 3 | 28 | Refine Candidate |
| VL-Rethinker | 5 | 4 | 4 | 5 | 5 | 4 | 27 | Refine Candidate |
| AgentRewardBench | 4 | 5 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| The AI Scientist-v2 | 5 | 4 | 4 | 5 | 5 | 3 | 26 | Emerging / Experimental |
| DUMP | 5 | 4 | 4 | 5 | 5 | 3 | 26 | Refine Candidate |
| MLRC-Bench | 4 | 5 | 5 | 5 | 5 | 3 | 27 | Refine Candidate |
| Nova Reel 1.1 | 2 | 3 | 4 | 5 | 3 | 1 | 18 | Weekly Only — Product fact |
| TensorRT-LLM v0.18.1 | 1 | 3 | 3 | 5 | 3 | 1 | 16 | Weekly Only — Dependency revision |
| Transformers v4.51.1/2 | 1 | 3 | 4 | 5 | 4 | 1 | 18 | Weekly Only — Patch facts |
| Gemini 2.5 Flash preview | 2 | 3 | 4 | 5 | 3 | 2 | 19 | Weekly Only — Version fact |
| VCR-Bench | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — Benchmark |
| MM-IFEngine | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — Dataset/eval case |
| SoTA with Less | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — Author experiment |

`N/I/P/R/K/L` 分别为 Technical Novelty / System Impact / Practical Value / Source Reliability / Project Relevance / Longevity。

### Deep Analysis 1 — Kimi-VL

- First Public: 2025-04-10
- Status: arXiv v1; open weights; Experimental
- Primary Source: https://arxiv.org/abs/2504.07491
- Evolution Relationship: Layering / Dependency

#### Why

多模态 agent 需要同时压缩视觉 token、保持高分辨率细节并控制语言 decoder 的 activated compute。

#### Principle and Mechanism

论文将 native-resolution vision encoder、MoE language decoder、长上下文与 reasoning post-training 组合。

#### Trade-off and Evidence Boundary

低 activated parameter 不等于低端到端成本；视觉编码、token 数、KV cache 和多轮工具环境仍可能主导 latency。

#### Connection and Evolution

知识树位置：第 21～25、62、74 章。Worth Watching；作者 benchmark 不进入正文。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Kimi-VL

- **Candidate / Week / Score:** Kimi-VL / 2025-W15 / 22/30。
- **Source Family ID:** `moonshot-kimi-vl-a3b-2025`。
- **Source Type:** arXiv technical report、official repository、open weights/model cards。
- **First-public Date / Revision History:** arXiv v1 2025-04-10，v2 2025-04-15，v3 2025-06-23；v3加入Kimi-VL-A3B-Thinking-2506。W15 event应以v1为first-public，2506能力属于后续revision，不得倒写进4月release。
- **Direct Primary Sources:** 《Kimi-VL Technical Report》v1/v3 HTML/PDF；MoonshotAI/Kimi-VL repository；released model cards/config。
- **Related Primary Sources:** Moonlight/Muon、DeepSeek-V3、SigLIP、Kimi k1.5 papers仅用于依赖机制。
- **Access and Verification Status:** Verified；report完整方法、训练、data、infrastructure、evaluation、limitations与appendix已读取，repo deployment路径已核验。
- **Full-read Coverage:** metadata/revisions、MoonViT/projector/MoE、Muon、四阶段pretraining、SFT/long-CoT/RL、data pipeline、4D parallelism、benchmarks/sensitivity、limitations、appendix。
- **Original Problem:** open VLM需要兼顾native-resolution、长视频/文档、语言能力、long-CoT和可部署active compute；fixed-resolution dense VLM会在视觉细节、token预算与decoder成本之间冲突。
- **Why the Previous Design Was Reasonable:** fixed-size vision encoder和dense decoder提供固定shape、简单batching与稳定kernel；短context、普通VQA或资源有限时，它们仍可能比native-resolution+MoE+128K更高效。
- **Changed Constraint:** 输入分辨率、图像数量、视频/文档长度变化极大，同时希望语言decoder只激活约2.8B参数并支持128K及reasoning post-training。
- **Mechanism:** 400M MoonViT从SigLIP-SO-400M继续训练，结合插值absolute embeddings和2D RoPE处理可变分辨率；flatten/packing后用pixel shuffle做2×2空间压缩，再由two-layer MLP投到LLM dimension。decoder为Moonlight MoE，16B total/2.8B active，从5.2T text checkpoint继续2.3T joint training。最终通过RoPE base 50K→800K和两次4×扩展把8K激活到128K。
- **State Ownership:** vision encoder拥有patch/2D position representation，projector拥有视觉压缩接口，MoE router/experts拥有decoder conditional compute；training system拥有packing、data/RNG、DP/EP/PP/CP groups；serving runtime仍拥有visual token budget、KV、expert placement和tool/workflow state。
- **Control Flow / Data Flow:** raw variable-resolution images/video/doc → MoonViT → flatten/pack → pixel-shuffle + MLP → multimodal token stream → MoE decoder → standard autoregressive output。训练顺序为ViT-only → joint pretrain → cooldown → 32K→128K long-context → joint SFT → long-CoT SFT → RL。
- **Implementation Details:** post-text pretraining共4.4T tokens：ViT 2T+0.1T、joint 1.4T、cooldown 0.6T、long-context 0.3T；long stage用25% long + 75% short replay。SFT 32K/128K各1 epoch。RL为online policy mirror descent变体，binary correctness reward + KL regularization、length penalty、curriculum/prioritized sampling。
- **Evaluation Setup:** general/academic/math/OCR/document/video/agent benchmarks；NIAH覆盖text/video到128K；reasoning token-length sensitivity显示MathVista约4K后饱和，而更难任务未必相同。Appendix列出benchmark规模/metric；闭源baselines多为author-reported/API snapshots。
- **Baselines / Ablations / Sensitivity:** 对比dense/MoE VLMs、Instruct/Thinking variants；给出thinking length曲线、NIAH区间和多任务表。缺少对MoonViT、2D RoPE、pixel shuffle、MoE、long-stage各组件的完整独立ablation与统一compute-normalized比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** report披露4D DP/EP/PP/CP、ZeRO-1、selective activation checkpointing，并声称相对7B dense VLM约60% training throughput提升；GPU/accelerator型号、precision、global batch、topology与测量细节未完整披露。repo示例默认32K，可配置131,072；online concurrency/TTFT/TPOT/SLO未披露。
- **What the Evidence Actually Proves:** 作者实现并开放了native-resolution vision + MoE decoder + staged long-context/reasoning training的完整系统组合；在披露任务下给出作者实验和受限sensitivity证据。
- **What It Does Not Prove:** 不证明2.8B active等于2.8B端到端成本，不证明128K有效组合任意长视频/文档，不证明agent benchmark代表生产workflow，也不证明60% throughput可跨hardware/topology复现。
- **Limitations / Threats to Validity:** 作者明确attention capacity约3B级、复杂domain/language-heavy任务受限；benchmark/vendor/API公平性、缺硬件合同；v3混入6月2506结果，容易污染4月event；NIAH不等同多证据推理。
- **Trade-offs / New Failure Modes:** native resolution保留细节却使visual token/packing动态；pixel shuffle降token但可能丢局部信息；MoE节省active GEMM却增加expert通信；long replay维护短能力却增加训练成本；RL length penalty减overthinking但可能过早截断。
- **Where the Previous Design Still Applies:** fixed-resolution/dense/short-context VLM在shape稳定、低延迟或单机deployment下仍合理；非thinking Instruct model适合不需长推理的perception任务。
- **Evolution Relationship:** `Layering / Dependency`：SigLIP/fixed encoder + text MoE → native-resolution multimodal joint training → long-context activation → long-CoT/RL；2506是后续revision，不覆盖v1。
- **ROADMAP Node:** 主 owner第24章；第21、22、23、25、32、62、74章为handoff。
- **Target and Adjacent Chapters Read:** 已读第23章数据、第24章Pretraining、第25章SFT；核对第21、22、32、62、74章边界。
- **Existing Coverage:** 第24章已有objective/step/stability/activation checkpointing，第23章已有distribution/packing/lineage，第21/22章已有MoE/long-context原理；尚缺“多模态能力生产必须同时版本化视觉token contract、joint-data mixture与parallelism”的具体整合机制，但需与全年VLM sources去重。
- **Integration Decision:** `Weekly Only — Experimental Model Case`；多模态 staged training 证据不足以改变 Ch23～25 的通用 contract。
- **Changed Files or Rejection Reason:** 不改 Books；保留 vision-token/data-mixture/parallelism 的待验证问题。
- **Open Questions:** v1与v3具体method差异；4D parallel topology/precision/global batch；native-resolution token budget到serving SLO的映射；agent benchmark scaffold与拒绝处理。

### Agent2Agent / A2A

- **Candidate / family / date / revision:** 28/30, `google-a2a-protocol-2025`; Google announcement first-public 2025-04-09. Archived Google-hosted docs and official v0.1.0 were read, but v0.1.0 and the 2025-06-23 Linux Foundation transfer are later revisions, not launch-day schema.
- **Sources / full-read:** launch announcement; `google-a2a.github.io/A2A/specification/`; `a2a-protocol.org/v0.1.0/specification/`; official repo revision history. Read Agent Card, Task, Message/Part, Artifact, JSON-RPC/HTTP, SSE, push, auth, errors and security. Exact 04-09 commit is a P3 archive gap.
- **Problem / old design / changed constraint:** same-process function calls are simplest when one runtime owns identity, memory and retry. Cross-vendor opaque agents need discovery, long tasks and partial artifacts without exposing internals.
- **Mechanism / state / flow / implementation:** Agent Card advertises endpoint/skills/modalities/auth; server-owned Task advances through lifecycle states; Messages/Parts carry input; Artifacts carry output. Client owns request identity, credentials, retry/cancel/subscription; server owns transitions/finalization; transport owns delivery. Discover → authenticate → JSON-RPC task/message → sync result or SSE chunks → authenticated push → cancel/terminal.
- **Evaluation / workload:** no benchmark, ablation, hardware/model/precision/length/batch/concurrency/SLO contract. Ecosystem participation proves intent, not interoperability reliability.
- **Proves / does not prove:** proves a public remote opaque-agent task boundary and launch-level HTTP(S), JSON-RPC, SSE, Agent Card/task/artifact concepts. Does not prove exactly-once, secure defaults, production conformance, or later fields existed on 04-09.
- **Trade-off / failures / coexistence:** avoids N×M adapters but adds identity, auth delegation, idempotency, partial-artifact, retry/cancel race, webhook forgery, schema negotiation and tracing failures. Typed in-process calls remain better in one trust domain.
- **Evolution / owner / decision:** `in-process orchestration → remote opaque-agent task protocol`; owner `AGENT-MULTI-AGENT` Ch82, adjacent `AGENT-MCP` Ch83 and `AGENT-PLATFORM` Ch84. `Refine — Existing Argument Candidate`. Ordinary review is complete because claims are narrowed; exact source tree remains Archive P3 only.

### Google Agent Development Kit v0.1.0

- **Candidate / Score / Source Family / Dates:** 26/30，`google-adk-python-initial`；official launch与GitHub v0.1.0均为2025-04-09，event-time release commit `e95bfd2`已核验。
- **Problem / Previous Design / Changed Constraint:** prompt+tool demo在单Agent下足够轻量，但复杂应用需要显式multi-agent composition、tool auth、callbacks、code execution、async runtime、evaluation与deployment adapter。
- **Mechanism / Ownership / Flow:** v0.1.0公开multi-agent、tool authentication、rich tools/MCP、callbacks、built-in code execution、async runtime以及experimental Live/CFC；Session/runner拥有conversation event，tool/callback边界拥有effect state。request → agent/subagent → tool/callback → event append → response。
- **Evaluation / Evidence Boundary:** release和event-time commit证明初版framework surface，不证明Google产品内部采用相同实现、production SLO或后续session/memory/artifact功能在W15已经存在。hardware、model、precision、batch、concurrency与SLO不适用或未披露。
- **Trade-off / Previous Design / Evolution:** code-first graph提高可测试性与orchestration clarity，却引入framework state、callback ordering、event replay和adapter compatibility；简单single-agent函数调用仍可更轻。属于`prompt demo → typed agent runtime`的`Direct Evolution`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-PLATFORM` / Ch84，handoff `AGENT-WORKFLOW` Ch81；已读Ch81～84。Ch84已有session/artifact/runtime contract，可用v0.1.0作受限实现案例，最终为`No Change — Already Covered`；待验证首发dependency snapshot与callback recovery语义。

### Ironwood TPU

- **Candidate / Score / Source Family / Dates:** 25/30，`google-ironwood-tpu7-announcement`；official 2025-04-09，04-23页面更新只作related revision。
- **Problem / Previous Design / Changed Constraint:** 通用accelerator在训练/推理混合时合理；thinking、MoE与embedding-heavy inference把压力推向HBM capacity/bandwidth、scale-up communication和sparse access。
- **Mechanism / State Boundary:** 公告披露256/9216-chip配置、per-chip 192GB HBM、7.37TB/s HBM bandwidth、1.2TB/s bidirectional ICI、SparseCore与vendor peak compute；hardware拥有physical memory/network/failure domain，compiler/runtime仍拥有placement、collective与scheduling。
- **Evidence / Non-evidence:** 只证明vendor hardware contract，不证明microarchitecture、compiler contract或model-matched latency/throughput/power/SLO；peak TFLOPs/EFLOPs不能写成应用性能。
- **Trade-off / Previous Design / Evolution:** 更大scale-up fabric与memory system支持inference co-design，却提高pod failure domain、cooling、placement与cost约束；小规模、标准GPU生态或portability优先时旧方案仍合理。
- **Owner / Adjacent / Decision / Open:** `INFER-TENSORRT-LLM` / Ch49（execution-plan/hardware co-design owner），handoff Ch56、Ch63；已读Ch48～50并核对Ch56/63。最终为`Weekly Only — Hardware Contract Fact`；待公开matched workload与compiler/runtime行为。

### Amazon Nova Sonic

- **Candidate / Score / Source Family / Dates:** 24/30，`amazon-nova-sonic-v1`；official AWS launch 2025-04-08，model ID `amazon.nova-sonic-v1:0`。
- **Problem / Previous Design / Changed Constraint:** STT→LLM→TTS pipeline易替换和独立验证，但每个边界会丢prosody/turn-taking并累积latency；speech-to-speech要求bidirectional session、interrupt和tool event。
- **Mechanism / Ownership / Flow:** 可验证的是HTTP/2 bidirectional streaming同时接收audio/events并输出audio/text/tool events，支持function calling/RAG；client/session拥有audio stream、prompt/tool config和interrupt lifecycle，service内部model机制未披露。
- **Evidence / Non-evidence / Trade-off:** announcement证明API/session behavior，不证明end-to-end neural architecture或质量/latency数字可泛化。统一stream减少application orchestration，却增加vendor session state、duplex backpressure、barge-in与partial tool-call recovery；合规或可替换性优先时modular pipeline仍合理。
- **Evolution / Owner / Adjacent / Existing Coverage:** `modular speech pipeline → unified bidirectional service session`；owner `PLATFORM-SERVING` / Ch60，handoff Ch23/Ch78；已读Ch59～61并核对Ch23/78。
- **Decision / Open:** `Weekly Only — Version Fact / Mechanism Not Disclosed`；待公开model architecture、session isolation、latency/concurrency与failure-recovery contract。

### Hogwild! Inference

- **Candidate / Score / Source Family / Dates:** 28/30，`hogwild-concurrent-attention`；arXiv:2504.06261 v1 2025-04-08、v2 04-09；后续v3/v4只作revision。
- **Problem / Previous Design / Changed Constraint:** sequential long-CoT保留单一history和简单commit，但latency由长推理主导；显式task decomposition又需预设协作结构。新分支让同权重workers共享可并发更新的KV。
- **Mechanism / Ownership / Flow:** worker读取common prompt、peer blocks与自己的block，用RoPE query re-rotation支持block reorder；段落边界把完成步骤commit到common history。runtime拥有shared KV block identity、visibility、worker-local frontier、paragraph commit和rollback。
- **Evaluation Contract:** QwQ-32B，GSM8K×5 synthetic与LIMO 817；对sequential early-stop/no-stop、Skeleton-of-Thought、self-consistency。证明作者任务中zero-shot shared memory可改善wall-clock/quality，不证明通用multi-agent收益或production scheduler安全。
- **Trade-off / Previous Design / Evolution:** 额外worker compute换latency，新增shared-state污染、position假设、同步/公平/rollback和重复分支；简单或不可分任务仍宜single worker。属于`single decode frontier → concurrent shared-state frontiers`的`Alternative Branch`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `INFER-KV-CACHE` / Ch45，handoff Ch56/Ch82；已读Ch44～46并核对Ch56/82。Ch45已有cache identity/commit，但并发visibility是缺口，最终为`Refine — Existing Argument Candidate`；待验证multi-tenant isolation、partial-write recovery与exact commit semantics。

### HybriMoE

- **Candidate / Score / Source Family / Dates:** 27/30，`hybrimoe-cpu-gpu-expert-runtime`；arXiv:2504.05897，唯一v1 2025-04-08；作者代码入口已核验。
- **Problem / Previous Design / Changed Constraint:** static CPU/GPU expert mapping在activation稳定时简单，却无法适应expert结构/大小和load波动。
- **Mechanism / Ownership / Flow:** dynamic intra-layer CPU/GPU balance、impact-driven inter-layer prefetch与score-based expert cache；runtime拥有residency、activation EMA、prefetch priority和CPU/GPU queues。router → split execution → cross-layer prefetch → cache update。
- **Evaluation Contract:** 基于kTransformers/llama.cpp kernels，三种MoE LLM；作者报告相对SOTA hybrid framework平均prefill 1.33×、decode 1.70×，必须绑定其hardware/model/context/batch。concurrency与SLO未披露，不外推到cluster serving。
- **Trade-off / Previous Design / Evolution:** 动态适配换统计滞后、cache thrash、prefetch misprediction、PCIe congestion和CPU tail；显存足够或activation稳定时GPU-only/static mapping仍合理。属于`static placement → telemetry-driven typed expert placement`的`Direct Evolution`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `INFER-GPU-MEMORY` / Ch54，handoff Ch56/Ch21；已读Ch53～55并核对Ch21/56。Ch54已有tiering/residency，但expert-score ownership可增强，最终为`Refine — Existing Argument Candidate`；待验证multi-tenant fairness、state invalidation和data-center topology。

### VAPO

- **Candidate / Score / Source Family / Dates:** 28/30，`vapo-value-rl-long-cot`；arXiv:2504.05118 v1 2025-04-07、v2 04-08、v3 04-11；事件使用v1/v3同周证据并保留revision差异。
- **Problem / Previous Design / Changed Constraint:** vanilla PPO/value learning在短response和dense reward下可控；long-CoT的value bias、length heterogeneity与sparse binary reward放大不稳定性。
- **Mechanism / Ownership / Flow:** value pretraining、decoupled/length-adaptive GAE、asymmetric clipping、token-level loss、positive-example LM loss与group sampling；trainer拥有policy/value/reference、token mask、length statistics、advantage和group buffer。rollout → correctness → value/GAE → length-conditioned credit → clipped updates。
- **Evaluation Contract:** Qwen-32B pretrained，AIME24，5000 steps；作者报告60.4并与vanilla PPO、R1-Zero、DAPO比较，component ablations均下降。hardware、global batch、topology与SLO未充分披露。
- **Evidence / Trade-off / Previous Design:** 证明integrated recipe在作者数学设置稳定有效，不证明单组件因果或跨领域优越；收益换额外value model/pretraining、更多hyperparameters、long-sequence variance和verifier bias。小任务或value不可校准时group-only/behavior cloning仍合理。
- **Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** `vanilla PPO → long-CoT-specific value/credit controls`；owner `TRAIN-PPO` / Ch32，handoff Ch31/33；已读Ch31～33。Ch32缺length-adaptive value branch，最终为`Refine — Existing Argument Candidate`；待验证跨model/domain、matched compute与reward-hacking。

### OLMoTrace

- **Candidate / Score / Source Family / Dates:** 28/30，`olmo-training-data-trace`；arXiv:2504.07096 v1 2025-04-09，v2 07-08；W15使用v1。
- **Problem / Previous Design / Changed Constraint:** 公开训练数据只证明可审计意图，无法把output实时定位到3.2B documents / 4.6T tokens；full semantic attribution又代价高且因果含义模糊。
- **Mechanism / Ownership / Flow:** maximal verbatim spans → unigram-rarity filter → infini-gram suffix-array retrieval → merge/rerank/coloring；index拥有token/doc offsets，query service拥有span、match、merge/rank state，SSD suffix arrays提供`O(L log N)`查询。
- **Evaluation Contract:** 64-vCPU、256GB RAM、40TB SSD；98 conversations、平均458-token output，steps1–3平均4.46s；human/LLM relevance，GPT-4o judge-human correlation 0.73。证明verbatim trace可实时化，不证明causal attribution、supporting evidence或citation。
- **Trade-off / Previous Design / Evolution:** exact match可解释但漏paraphrase，common phrase误命中，index/storage/update、privacy/delete与lineage成本高；闭源数据或semantic attribution仍需其他方法。属于`dataset disclosure → indexed traceability`的`Direct Evolution`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-TRACE` / Ch69，handoff Ch27/66；已读Ch68～70并核对Ch27/66。Ch69已有lineage/trace但缺training-data retrieval contract，最终为`Refine — Existing Argument Candidate`；待验证deletion propagation、model revision和非verbatim support。

### SmolVLM

- **Candidate / Score / Source Family / Dates:** 26/30，`smolvlm-efficient-vlm`；arXiv:2504.05299，唯一v1 2025-04-07。
- **Problem / Previous Design / Changed Constraint:** 大VLM通过增加encoder/LM和visual tokens获取能力，但on-device/低内存场景必须重新分配encoder、LM、context和data预算。
- **Mechanism / Ownership / Flow:** image splitting/video frames → SigLIP → pixel shuffle → MLP projection → interleaved tokens → small LM；比较vision/LM capacity、2K→16K context、shuffle、position tokens、media markers、user masking、text mix与tiny CoT mix。
- **Evaluation Contract:** 256M/500M/2.2B family，31 benchmarks；135M/360M在>8K失败、1.7B至16K较稳，约14% text维持语言，tiny CoT mix有益而过多有害。RAM是cost proxy，不是统一latency/SLO。
- **Trade-off / Previous Design / Evolution:** aggressive shuffle节省token却损OCR/localization，较大encoder会挤占tiny LM capacity；固定分辨率、短输入或服务器场景旧设计仍合理。属于`scale-up → constraint-driven capacity rebalance`的`Alternative Branch`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-REPRESENTATION` / Ch23，handoff Ch24/26/27/42；已读Ch22～24并核对相关章节。Ch23已有token budget但缺small-VLM system allocation，最终为`Refine — Existing Argument Candidate`；待验证device latency、energy和task-specific allocation。

### One-Minute Video Generation with TTT

- **Candidate / Score / Source Family / Dates:** 25/30，`ttt-one-minute-video`；arXiv:2504.05298，唯一v1 2025-04-07。
- **Problem / Previous Design / Changed Constraint:** full attention在短视频保真且kernel成熟，Mamba state便宜；约100K-token长视频下attention昂贵，而fixed hidden state可能不足。
- **Mechanism / Ownership / Flow:** 在pretrained 5B video DiT中加入hidden-state-as-MLP的TTT layers，通过test-time update形成long-sequence state；runtime拥有每层fast-weight、update rule、request isolation、rollback和commit。
- **Evaluation Contract:** 对Mamba2、Gated DeltaNet、sliding/local attention；100 videos/method human eval。作者报告minute-long setting领先，但18秒条件下Gated DeltaNet反而更好；kernel受register spill与async ordering限制。
- **Evidence / Trade-off / Previous Design:** 证明TTT在作者超长视频设置可成为更强state branch，不证明短序列或production更优；收益换state contamination、rollback、跨request隔离和kernel复杂度。短序列/固定窗口仍宜attention或linear recurrence。
- **Evolution / Owner / Adjacent / Existing Coverage / Decision / Open:** `full attention → compact recurrence → learned fast-weight state`的`Alternative Branch`。owner Ch24，handoff Ch25/Ch22；已读Ch23～25并核对Ch22。最终为`Emerging / Experimental`；待验证independent quality、kernel maturity、state reset与serving SLO。

### T1 / Tool-integrated Verification

- **Candidate / Score / Source Family / Dates:** 26/30，`t1-tool-integrated-verifier`；arXiv:2504.04718 v1 2025-04-07，v2 2026-06-01只作later revision。
- **Problem / Previous Design / Changed Constraint:** learned verifier在纯语义任务可泛化，但small verifier难记计算与事实；可执行任务可先用工具排除确定错误，再用learned verifier排序残余候选。
- **Mechanism / Ownership / Flow:** ToolV作为calculator/code/search/retrieval rejection filter，再交PRM或generative RM；runtime拥有candidate set、tool call/result、reject reason与score。candidate → tool filter → learned verifier → selection。
- **Evaluation Contract:** Llama3.2-1B；MATH500、GSM8K，比较PRM/GenRM、ToolV及组合。作者结果证明所测可执行任务的tool filter有增益，不证明开放域tool correctness或tool latency收益；false negative一旦reject无法恢复。
- **Trade-off / Previous Design / Evolution:** 外置memorization burden换tool failure、sandbox、timeout、freshness和false-negative风险；纯语义或工具不可靠时learned verifier仍必要。属于`learned verifier → tool filter + learned ranker`的`Layering`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66，handoff Ch78/56；已读Ch65～67并核对Ch78。Ch66已有executable verifier但缺two-stage false-negative boundary，最终为`Refine — Existing Argument Candidate`；待验证tool calibration、rollback和cost-aware ordering。

### Quantization Hurts Reasoning?

- **Candidate / Score / Source Family / Dates:** 27/30，`quantized-reasoning-contract`；arXiv:2504.04823 v1 2025-04-07，v2 08-18；事件锁v1。
- **Problem / Previous Design / Changed Constraint:** low-bit serving降低memory/bandwidth，在普通language task中常近似无损；long-CoT让weight/KV/activation error跨步骤累积，tail reasoning更敏感。
- **Mechanism / Ownership / Flow:** 比较AWQ/GPTQ weight-only、KVQuant/QuaRot KV、SmoothQuant/QuaRot/FlatQuant/MXFP4 W-A-KV；runtime必须把precision profile、calibration data、cache format、kernel/backend和model revision绑定为同一execution identity。
- **Evaluation Contract:** 多个DeepSeek-R1-distill、QwQ models；AIME120、MATH500、GSM8K、GPQA-Diamond、LiveCodeBench，多sampling。W4通常接近原精度但model/task dependent，W3与4-bit W-A-KV风险显著；hardware/topology/batch/concurrency/SLO不完整时不作系统性能外推。
- **Trade-off / Previous Design / Evolution:** memory/bandwidth收益换reasoning-tail risk、calibration drift与backend portability；普通语言或宽松SLO仍可能使用更低bit。属于`accuracy-average quantization gate → reasoning-tail workload contract`的`Refine`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `INFER-TENSORRT-LLM` / Ch49，handoff Ch45/66；已读Ch48～50并核对Ch45/66。Ch49已有precision admission但缺long-CoT tail contract，最终为`Refine — Existing Argument Candidate`；待验证真实latency/cost、mixed precision与online drift。

### A Sober Look at Progress in LM Reasoning

- **Candidate / Score / Source Family / Dates:** 28/30，`reasoning-eval-reproducibility`；arXiv:2504.07086 v1 2025-04-09，v2 10-06；W15使用v1。
- **Problem / Previous Design / Changed Constraint:** 单次benchmark score便于比较，但seed、sampling、prompt/template、extractor、truncation、framework、hardware/backend可改变紧邻ranking。
- **Mechanism / Ownership / Flow:** versioned evaluation contract、多seed、container、deterministic settings、统一extractor和公开outputs；evaluator拥有model artifact、prompt、decoder、seed、hardware、engine/kernel与extractor identity。
- **Evaluation Contract:** 同model跨5 clusters差异可约6–8pp；相同A100/container仍有variation，更新stack也会波动；作者建议小AIME至少30 seeds并报告mean/std。只证明所测model/task/stack，不支持“RL普遍无效”。
- **Trade-off / Previous Design / Evolution:** 更严格复现增加运行与存储成本，仍不能消除floating-point/backend nondeterminism；快速regression仍可用少seed，但不能作细粒度ranking。属于`point score → versioned distributional evidence`的`Direct Evolution`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-EVALUATION-SYSTEM` / Ch66，handoff Ch69/31；已读Ch65～67并核对Ch69/31。Ch66已有EvalSpec但可加强backend/seed identity，最终为`Refine — Existing Argument Candidate`；待验证跨stack reproducibility和成本下限。

### SkillWeaver

- **Candidate / Score / Source Family / Dates:** 27/30，`skillweaver-derived-executable-skills`；arXiv:2504.07079，唯一v1 2025-04-09。
- **Problem / Previous Design / Changed Constraint:** 每次从atomic browser action重新规划最少状态、易回溯，却重复探索且难迁移成功策略；长期Agent需要可执行、可测试、可撤销的derived skill。
- **Mechanism / Ownership / Flow:** explore site → abstract reusable API → generate test inputs → execute/debug/hone → version skill library → downstream invocation。artifact拥有signature/code/tests/provenance/site schema，registry拥有version/supersession，sandbox拥有effect authority。
- **Evaluation Contract:** GPT-4o-2024-08-06 temperature0.3；WebArena 812 tasks与4 live sites/57 tasks。作者报告relative gains，但不证明跨website/schema drift或weak-model transfer普遍成立。
- **Trade-off / Previous Design / Evolution:** skill复用换DOM drift、permission side effect、skill poisoning、false verification和supersession complexity；高风险动作或稳定小任务仍宜人工API与contract tests。属于`history retrieval → derived executable artifact`的`Direct Evolution`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-PLATFORM` / Ch84，handoff Ch77/78/81；已读Ch81～84并核对Ch77/78。Ch84已有skill lifecycle但可补“no exception ≠ semantic success”，最终为`Refine — Existing Argument Candidate`；待验证oracle、schema drift和delete/rollback。

### Auditing Model Substitution in LLM APIs

- **Candidate / Score / Source Family / Dates:** 27/30，`llm-api-model-integrity-audit`；arXiv:2504.04715 v1 2025-04-07，v2 09-29；事件锁v1。
- **Problem / Previous Design / Changed Constraint:** behavioral benchmark适合监控quality drift，却难证明provider实际运行advertised model，尤其面对quantization、random routing、benchmark evasion和metadata restriction。
- **Mechanism / Ownership / Flow:** 比较text classifier、identity prompting、MMD、benchmark、greedy/logprob与activation proof，最后以TEE attestation绑定model artifact和execution environment；registry拥有declared identity，attester拥有measurement/key chain，monitor只拥有behavior evidence。
- **Evaluation Contract:** output-only方法对INT8/FP8、小比例mixture和engine nondeterminism区分能力有限；v2 provider table/TEE数字不倒写。证明output-only不能给strong identity guarantee，不证明TEE supply chain/side channel完备。
- **Trade-off / Previous Design / Evolution:** cryptographic identity增加attestation、driver/firmware trust、performance与observability成本；behavior monitoring仍适合drift/SLO但不是identity proof。属于`behavioral evidence → measured execution identity`的`Layering`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `PLATFORM-SECURITY` / Ch72，handoff Ch59/66；已读Ch71～73并核对Ch59/66。现有章节有attestation但缺API-substitution threat model，最终为`Refine — Existing Argument Candidate`；待验证key rotation、multi-tenant proof和fallback semantics。

### Scaling Laws for Native Multimodal Models

- **Candidate / Score / Source Family / Dates:** 28/30，`native-multimodal-scaling`；arXiv:2504.07951 v1 2025-04-10、v2 04-11；后续revision不倒写。
- **Problem / Previous Design / Changed Constraint:** late fusion复用mature encoder，在少数据与快速adaptation时合理；from-scratch native multimodal需要比较fusion、parameter、token与FLOP allocation。
- **Mechanism / Ownership / Flow:** 457 models、early/late fusion统一FLOP contract并拟合loss scaling；modality-agnostic MoE让router学习specialization。training system拥有mixture/token/FLOP contract，router/runtime拥有expert routing/placement/communication。
- **Evaluation Contract:** 0.3–4B active、250M–400B tokens、多mixture；16 H100、160k steps/300B tokens示例。early/late slope接近，early在小compute更优；sparse early fusion同active cost表现更好，但extreme-scale extrapolation和私有数据影响未闭合。
- **Trade-off / Previous Design / Evolution:** early fusion简化deployment却需from-scratch data/token calibration；late fusion在少数据和encoder复用时仍合理；MoE增加capacity/communication failure。属于`late fusion reuse ↔ native early fusion`的`Alternative Branch`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-REPRESENTATION` / Ch23，handoff Ch21/28；已读Ch22～24并核对Ch21/28。Ch23已有fusion branches但缺compute-normalized scaling evidence，最终为`Refine — Existing Argument Candidate`；待验证loss-downstream correlation、extreme-scale和serving cost。

### Missing Premise exacerbates Overthinking

- **Candidate / Score / Source Family / Dates:** 25/30，`missing-premise-overthinking`；arXiv:2504.06514 v1 2025-04-09、v2 04-11。
- **Problem / Previous Design / Changed Constraint:** fully specified hard tasks奖励持续推理，但真实query可能缺关键premise；同一persistence会放大length和错误自洽，而non-reasoning LM反而更早clarify。
- **Mechanism / Ownership / Flow:** 构造missing-premise slices，分析critical-thinking出现位置与overthinking pattern，并验证reasoning-response distillation传播该行为；workflow应在planning前拥有premise-sufficiency/ask-or-abstain gate。
- **Evidence / Non-evidence:** 证明所测datasets/models存在MiP-overthinking与distillation contagion，不证明所有long-CoT或test-time scaling有害；缺production query distribution、utility与SLO。
- **Trade-off / Previous Design / Evolution:** reasoning persistence提升可解难题，却损害abstain/clarify和latency；完整题目或可验证search仍适用旧recipe。属于`always-reason → premise-aware route/clarify`的`Direct Evolution`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `AGENT-PLANNING` / Ch79，handoff Ch66/31；已读Ch78～80并核对Ch66/31。Ch79已有uncertainty/stop但缺missing-premise gate，最终为`Refine — Existing Argument Candidate`；待验证calibration、clarification cost与distillation mitigation。

### DDT / Decoupled Diffusion Transformer

- **Candidate / Score / Source Family / Dates:** 24/30，`ddt-frequency-decoupled-diffusion`；arXiv:2504.05741 v1 2025-04-08。
- **Problem / Previous Design / Changed Constraint:** 单一DiT block统一建模global与detail，结构简单、kernel成熟，却产生low/high-frequency optimization conflict与跨step重复compute。
- **Mechanism / Ownership / Flow:** asymmetric large encoder + small decoder拆分global encoding与detail decoding；相邻denoising steps共享encoder state，dynamic programming选择sharing frequency。sampler/runtime拥有step-cache identity与staleness policy。
- **Evaluation Contract:** ImageNet256，DDT-B/L/XL；80 epochs/400k steps、batch256、Euler250/no CFG；比较ratio和decoder类型。证明该任务的convergence/quality与受限sharing，不证明text/video或low-step sampler通用。
- **Trade-off / Previous Design / Evolution:** split引入interface bottleneck，cache/share带staleness和quality loss；短生成或成熟DiT kernel仍可原结构。属于`uniform block → frequency-specialized stages + temporal reuse`的`Alternative Branch`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24；已读Ch23～25。Ch24已有sampler/cache boundary，最终为`Emerging / Experimental`；待验证跨modal、low-step、kernel latency和cache invalidation。

### C3PO

- **Candidate / Score / Source Family / Dates:** 24/30，`c3po-test-time-expert-remix`；arXiv:2504.07964，唯一v1 2025-04-10。
- **Problem / Previous Design / Changed Constraint:** pretrained router提供低延迟静态起点，但单sample可能需要不同expert mixture；test-time adaptation尝试用相似成功样本修正critical layers。
- **Mechanism / Ownership / Flow:** reference-set neighbors构造mode/kernel/average-loss surrogate，仅优化critical layers/core experts/last-token mixing weights；runtime新增reference index、neighbor label和per-request routing override。
- **Evaluation Contract:** 两个MoE、六个benchmarks；last5 layers、last token、kNN=3最好，作者报告7–15pp。hardware、runtime、latency和large-production MoE未披露；不证明neighbor leakage-free或OOD可靠。
- **Trade-off / Previous Design / Evolution:** test-time gradient/neighbor search换latency、privacy/poisoning与freshness风险；没有trusted similar samples时pretrained routing仍合理。属于`static router → per-request local adaptation`的`Experimental Branch`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `MODEL-MOE` / Ch21，handoff Ch56；已读Ch20～22并核对Ch56。现有章节已有routing state但缺reference-owned override，最终为`Emerging / Experimental`；待验证leakage、online cost、fallback和cacheability。

### SGLang v0.4.5

- **Candidate / Score / Source Family / Dates:** 27/30，`sglang-v045-hybrid-runtime`；official discussion/release 2025-04-07。
- **Problem / Previous Design / Changed Constraint:** 单engine continuous batching曾足够；Llama4、speculation、MoE expert communication与PD disaggregation要求runtime同时管理多类state和dependency。
- **Mechanism / Ownership / Flow:** release集成Llama4、FA3、EAGLE3、DeepEP与disaggregated prefill/decode；runtime拥有KV/session identity、draft/verify state、expert groups与prefill/decode handoff。quantization依赖vLLM是breaking dependency fact，不是新算法。
- **Evaluation Contract / Evidence Boundary:** release证明功能/compatibility，不提供matched model/hardware/precision/length/batch/concurrency/SLO；bundle中各子机制必须回到linked source，不能把版本号写成单一speedup。
- **Trade-off / Previous Design / Evolution:** feature integration减少用户拼装，却放大state compatibility、rollback、dependency和debug surface；单模型/单节点时较简单runtime仍合理。属于`single engine → typed hybrid-state runtime`的`Layering`。
- **Owner / Adjacent / Existing Coverage / Decision / Open:** `INFER-SGLANG` / Ch51，handoff Ch48/55；已读Ch50～52并核对Ch48/55。Ch51已有framework-as-runtime contract，可补版本案例，最终为`Refine — Existing Argument Candidate`；待验证state handoff、rollback与matched workload。

### Seaweed-7B

- **Source/date/revision/full-read:** 27/30, `seed-seaweed-7b-video-foundation`, arXiv:2504.08685 v1 2025-04-11; manuscript date March 02 is not accepted as public date. Read data, VAE/DiT, stages, infra, optimization, evaluation, applications and references; project page checked.
- **Problem → mechanism:** brute-force DiT/GPU scaling is reasonable when quality dominates cost. Under bounded resources, ~100M filtered/captioned clips → causal 3D VAE (48×/64× compression) → 7B hybrid-stream DiT → staged pretraining/SFT/RLHF. BMF/Ray data processing, parallelism, runtime balance, activation checkpointing and fused kernels co-design training.
- **State/control/data:** data system owns provenance/filtering; VAE owns latent geometry; trainer owns weights/optimizer/RNG/parallel groups; serving owns sampler/step state. Raw video → filter/caption → latent → DiT → denoise → decode.
- **Evaluation:** 665k H100 GPU-hours; author human Elo and single-H100, 12-NFE latency comparison (~29.6s vs ~1837.9s for the stated Wan configuration). Batch/concurrency/SLO and independent reproduction absent; not universal 62×.
- **Boundary/trade-off/failures/coexistence:** proves workload-constrained co-design can be competitive in the authors’ setup, not universal cost optimality. Compression/fewer steps trade detail; filtering/caption/RLHF add bias; checkpointing/runtime add complexity. Larger/latent models remain valid when maximum quality dominates.
- **Owner/adjacent/disposition:** `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24; handoff `TRAIN-DATA` Ch27, Ch28/49. `Refine Candidate`.

### GigaTok

- **Source/date/revision/full-read:** 27/30, `gigatok-visual-tokenizer-scaling`, arXiv:2504.08736 v1 2025-04-11, v2 2025-08-24. Read tokenizer/regularization, scaling, generation/representation evaluation, ablations and appendix.
- **Problem → mechanism:** reconstruction-only optimization is rational locally, but larger tokenizers can create a latent distribution harder for the downstream AR model. AR probing detects this; pretrained-encoder semantic regularization limits latent complexity; 1D tokens, decoder-heavy asymmetric scaling and entropy loss enable billion-scale training.
- **State/control/data:** representation owns codebook/token identity; generator owns downstream learnability. Image → encoder/VQ → 1D code → AR generator → decoder. Admission must include downstream AR loss, not reconstruction alone.
- **Evaluation:** tokenizer to ~2.9B, AR model 1.4B, ImageNet 256; reconstruction/FID/IS/representation, 1D-vs-2D, capacity allocation, teacher/layer, entropy and regularization ablations. Hardware, precision, batch/concurrency/SLO incomplete.
- **Boundary/trade-off/failures/coexistence:** proves reconstruction and generation can diverge in this family, not that 3B tokenizers are system-optimal. Semantic teacher bias, decoder cost and entropy/fidelity trade-offs remain. Small tokenizers remain appropriate under memory/latency limits.
- **Owner/adjacent/disposition:** `MULTIMODAL-REPRESENTATION` Ch23, handoff Ch24/42. `Refine Candidate`.

### MineWorld

- **Source/date/revision/full-read:** 27/30, `microsoft-mineworld-interactive-world-model`, arXiv:2504.08388 only v1 2025-04-11; code/model linked. Read framework, tokenizers, parallel decode, dataset, action metrics, configs, experiments and limitations.
- **Problem → mechanism:** video generation is a useful prior but not a controllable simulator. Visual/action tokenizers interleave IDs for next-token training; spatially redundant frame tokens decode in parallel for reported 4–7 FPS.
- **State/control/data:** episode owns observation/action history; codebooks own representation; runtime owns KV and spatial commit frontier. Scene/action → tokens → AR transition → parallel next-frame tokens → observation; not Agent durable memory.
- **Evaluation:** Minecraft visual quality plus discrete action/camera following, open diffusion baselines and parallel-decode analysis. 4–7 FPS is model/hardware-specific; precision, concurrent sessions and control SLO incomplete.
- **Boundary/trade-off/failures/coexistence:** proves interactive action-following in this sandbox, not physical causality or sim-to-real. Parallelism trades dependency for latency; tokenization and rollout compound error. Serial AR/diffusion remain useful when fidelity dominates.
- **Owner/adjacent/disposition:** `MULTIMODAL-WORLD-MODELS` Ch25, handoff Ch26 and inference-state chapters. `Refine Candidate`.

### VLM-R1

- **Source/date/revision/full-read:** 26/30, `omai-vlm-r1-rule-reward`, arXiv:2504.07615 v1 2025-04-10, v2 04-14; repo checked. Read GRPO, REC/OVD rewards, implementation, SFT/RL comparison, reward hacking, data/model-scale ablations and discussion.
- **Problem → mechanism:** SFT is stable with demonstrations; visual labels enable rule rewards, but naive parsers/IoU can be gamed. Group rollouts receive format/correctness rewards and GRPO relative advantages; code supports LoRA, multi-node/multi-image/mixed modality.
- **State/control/data:** policy owns outputs; evaluator owns parser/IoU/reward version; trainer owns rollout group/reference/optimizer. Image/query → rollouts → executable reward → group advantage → update.
- **Evaluation:** Qwen2.5-VL scales on REC/OVD versus SFT and detection baselines; reward-hacking, data-quality and scale sensitivity. Hardware/precision/global batch/SLO not portable.
- **Boundary/trade-off/failures/coexistence:** proves gains and evaluator exploits in tested tasks, not emergent general visual reasoning. Rule rewards reduce judge variance but create hacking; LoRA constrains update rank. SFT remains rational for soft criteria and scarce rollouts.
- **Owner/adjacent/disposition:** `TRAIN-GRPO` Ch33, handoff Ch66/23. `Refine Candidate`.

### PixelFlow

- **Source/date/revision/full-read:** 25/30, `pixelflow-raw-pixel-flow`, arXiv:2504.07963 only v1 2025-04-10; code/models linked. Read flow math, cascade, architecture, schedules, ImageNet/T2I, solver/CFG/step sensitivity and limitations.
- **Problem → mechanism:** latent diffusion’s VAE saves compute but imposes a separate reconstruction ceiling. Shared-parameter multi-scale flow matching works in raw pixels: coarse kickoff → progressively higher resolution using patching, 2D RoPE, resolution embeddings and packing.
- **State/control/data:** sampler owns scale/ODE/CFG schedule; model owns one pixel objective. No separately versioned VAE. Coarse pixels → flow steps → refinement → final image.
- **Evaluation:** ImageNet256 FID/IS/sFID/precision/recall and T2I metrics; kickoff, patch, step, solver, CFG studies. Hardware, precision, batch/concurrency/SLO incomplete.
- **Boundary/trade-off/failures/coexistence:** proves viability, not universal superiority. Removing VAE restores pixel compute and cascade coupling; coarse errors persist. Latent diffusion remains rational for video and mature serving.
- **Owner/adjacent/disposition:** Ch24, `Emerging / Experimental`.

### Pangu Ultra

- **Source/date/revision/full-read:** 28/30, `huawei-pangu-ultra-ascend-dense`, arXiv:2504.07866 v1 2025-04-10, v2 04-11. Read architecture/stability, training system, Ascend runtime, evaluation, ablation and appendices.
- **Problem → mechanism:** Pre-LN is stable at moderate depth; 135B dense training exposes depth-scale activation/gradient and fleet loss spikes. Depth-scaled sandwich normalization controls residual scale, combined with a dense training stack across 8,192 Ascend NPUs.
- **State/control/data:** normalization owns per-layer signal scale; training owns parameter/optimizer/RNG/checkpoint; runtime owns parallel groups/collectives. Tokens → deep residual stack → loss; checkpoint/recovery must preserve distributed identity.
- **Evaluation:** 135B, 13.2T tokens, 8,192 Ascend NPUs; language/reasoning/code results, stability curves and norm ablations. Precision/topology/global batch/SLO incomplete; vendor evidence only.
- **Boundary/trade-off/failures/coexistence:** proves the recipe trained the reported model, not dense superiority or GPU portability. Extra norms add traffic/compute; dense avoids routing but pays full activation. Pre-LN remains valid at smaller scale.
- **Owner/adjacent/disposition:** `TRAIN-PRETRAINING` Ch28, handoff Ch36/40. `Refine Candidate`.

### SpecReason

- **Source/date/revision/full-read:** 28/30, `specreason-semantic-speculation`, arXiv:2504.07891 v1 2025-04-10, v2 2025-05-16; code linked. Read semantic acceptance, hierarchical token speculation, evaluation, thresholds and appendix.
- **Problem → mechanism:** exact speculation preserves distribution but misses semantic equivalence in long reasoning. A small model drafts an intermediate reasoning step; the large model judges/accepts/corrects; token speculation can layer below.
- **State/control/data:** runtime owns draft lineage, judge threshold, accepted prefix and rollback/commit. Query → semantic draft → base judgement → accept/correct → next step/final answer.
- **Evaluation:** QwQ-32B, Skywork-OR1-Preview-32B and R1-70B-class bases with ~1.5B drafters; AIME/MATH500/GPQA; author reports ~80% acceptance, 1.4–3× speedup and 0.4–9pp accuracy changes with threshold sensitivity. Hardware/concurrency/SLO incomplete.
- **Boundary/trade-off/failures/coexistence:** not exact decoding; false acceptance compounds error, false rejection loses speed, judge calls and rollback complicate scheduling. Exact speculation remains best where equivalence is mandatory.
- **Owner/adjacent/disposition:** `INFER-SPECULATIVE-DECODING` Ch48, handoff Ch44/56/66. `Refine Candidate`.

### PRIMA.cpp

- **Source/date/revision/full-read:** 28/30, `prima-cpp-home-cluster-inference`, arXiv:2504.08791 v1 2025-04-07; v3 2026-07-04 substantially expands authors/title/appendix. v1 is event evidence; full current paper and code reviewed as revision evidence.
- **Problem → mechanism:** single-device/homogeneous partition is simple when weights fit and links are fast. Consumer clusters have disk offload, mixed CPU/GPU, Wi-Fi and OS heterogeneity. mmap plus pipelined-ring parallelism overlaps disk/compute/communication and resolves prefetch-release conflict; Halda co-optimizes layer/device/backend assignment.
- **State/control/data:** layers own weights and KV follows layer placement; only activations cross devices; scheduler owns profile/placement/version/recovery. Token → assigned layer stages → ring activation → output.
- **Evaluation:** v1 four consumer nodes, quantized 30B–70B-class models, llama.cpp/exo/dllama baselines. v3 later adds 8B–70B, concurrency1–40, context1K–32K, network/energy/busy-system/large-pool and component ablations; do not backproject. No cloud availability SLO.
- **Boundary/trade-off/failures/coexistence:** proves co-optimization helps tested cluster, not universal privacy/fault tolerance. Adds profiling drift, churn, stragglers and recovery consistency. Single device remains preferable when fit/predictability dominate.
- **Owner/adjacent/disposition:** `INFER-SCHEDULING` Ch56, handoff Ch49/54. `Refine Candidate`.

### VL-Rethinker

- **Source/date/revision/full-read:** 27/30, `vl-rethinker-ssr-forced-reflection`, arXiv:2504.08837 v1 2025-04-10, v3 2025-05-08. Read GRPO, SSR, forced rethinking, data, benchmarks, ablations and prompts; v3 scores not backprojected.
- **Problem → mechanism:** on-policy GRPO avoids stale replay but equal-reward groups give zero advantage; outcome RL need not teach self-checking. SSR retains non-zero-advantage samples and prioritizes |A| with near-on-policy refresh. Forced Rethinking appends a trigger to some rollouts, retains correct revised traces and adds SFT loss.
- **State/control/data:** buffer owns trajectory/policy version/provenance; trainer owns rewards/advantages; trigger alters behavior distribution. Rollout → score → selective replay/trigger → corrected trace → update.
- **Evaluation:** ViRL39K 38,870; 7B/32B/72B; MathVista/MathVerse/MathVision/MMMU-Pro/EMMA/MEGA; up to 3 epochs, 8 responses/query, batch512, 1,024-query sync; component ablations. Hardware/precision/serving SLO absent.
- **Boundary/trade-off/failures/coexistence:** gains do not prove faithful reflection. Replay adds staleness/selection bias; forced triggers can teach performative reflection/length. Pure on-policy remains valid under rapid drift.
- **Owner/adjacent/disposition:** `TRAIN-GRPO` Ch33, analogy-only handoff Ch80. `Refine Candidate`.

### AgentRewardBench

- **Source/date/revision/full-read:** 27/30, `agentrewardbench-web-trajectory-judges`, arXiv:2504.08942 v1 2025-04-11, v2 2025-10-06. Read construction, expert labels, five environments, four agent LLMs, 12 judges, representation studies, errors and appendices.
- **Problem → mechanism:** deterministic rules are cheap but miss semantically valid paths/side effects; humans are costly. 1,302 trajectories get expert success/side-effect/repetition labels; rules and LLM judges are measured against them under multiple trace representations.
- **State/control/data:** evaluator owns environment/task/trace/final state/judge prompt-model-version/disagreement. Task → trajectory → rule/judge → calibrated label/error slice.
- **Evaluation:** five benchmark families, four generating LLMs, 12 judges; precision/recall/agreement analyses. No judge dominates; rules underreport success. Execution hardware and service SLO are not the target.
- **Boundary/trade-off/failures/coexistence:** evaluator choice changes scores; LLM judge is not truth. Flexible judges add drift/cost/bias/deceptive-trace risk. Rules remain best for executable effects; hybrid evidence required.
- **Owner/adjacent/disposition:** `PLATFORM-EVALUATION-SYSTEM` Ch66, handoff Ch69/81. `Refine Candidate`.

### The AI Scientist-v2

- **Source/date/revision/full-read:** 26/30, `sakana-ai-scientist-v2`, arXiv:2504.08066 only v1 2025-04-10; repo checked. Read tree search, experiment manager, VLM feedback, workshop evaluation, hyperparameters/prompts, generated papers, limitations and ethics.
- **Problem → mechanism:** templates give reproducibility but limit new domains. Progressive agentic tree search branches/prunes hypotheses; experiment manager owns code/runs; VLM figure feedback and results feed manuscript construction.
- **State/control/data:** workflow owns hypothesis lineage, diff, environment, run artifact, metric, figure and review; model only proposes. Hypothesis → code → execute → evaluate → branch/prune → paper/review.
- **Evaluation:** three autonomous ICLR-workshop submissions, one above reported acceptance threshold. N=3, workshop/reviewer selection and contamination/novelty not controlled; model/API/hardware/cost and total failure denominator incomplete.
- **Boundary/trade-off/failures/coexistence:** proves a narrow artifact workflow crossed review, not reliable scientific discovery. Search adds compute, p-hacking, corruption, reviewer gaming and provenance burden. Templates remain valid in regulated/high-cost science.
- **Owner/adjacent/disposition:** `AGENT-WORKFLOW` Ch81, handoff Ch66/72/84. `Emerging / Experimental`.

### DUMP

- **Source/date/revision/full-read:** 26/30, `dump-distribution-curriculum-rl`, arXiv:2504.09710 v1 2025-04-13, v3 2025-10-11; code checked. Read advantage/UCB algorithm, experiments, ablations, heuristic comparison, proofs and limitations.
- **Problem → mechanism:** uniform mixtures are stable when learnability matches, but heterogeneous reasoning groups saturate differently. Absolute advantage estimates distribution learnability; UCB combines mean advantage exploitation and low-count exploration to update GRPO sampling.
- **State/control/data:** scheduler owns distribution ID/count/statistics/probability; trainer owns rollouts/advantages/policy version. Sample distribution → rollout → advantage → UCB update → next mixture.
- **Evaluation:** multi-source/difficulty logic reasoning, uniform/heuristic/UCB baselines, convergence/final performance and sampling ablations. Hardware/precision/global batch are experiment-specific; serving SLO N/A.
- **Boundary/trade-off/failures/coexistence:** proves authors’ mixture gains, not universal data value. Reward noise/drift/sparse groups can corrupt UCB; it can explore unlearnable data. Uniform remains valid for stationary balanced mixtures.
- **Owner/adjacent/disposition:** `TRAIN-GRPO` Ch33, handoff `TRAIN-DATA` Ch27. `Refine Candidate`.

### MLRC-Bench

- **Source/date/revision/full-read:** 27/30, `mlrc-bench-research-agent`, arXiv:2504.09702 v1 2025-04-13, v3 2025-10-24; code/leaderboard checked. Read all method/experiment and appendices: seven tasks, objective metrics, protocol, scaffolds/models, cost/scaling, limitations, prompts and traces.
- **Problem → mechanism:** paper/LLM review measures plausibility; Kaggle tasks often measure engineering on solved problems. Seven research competitions provide repository-level editable method area, immutable evaluator/hidden test, dev snapshots, human baselines, resource limits and objective execution.
- **State/control/data:** evaluator owns task/repo/permissions/environment/test and snapshot lineage. Agent edits/runs dev → best-dev snapshot frozen → hidden test. Effectiveness normalizes baseline=0/top-human=100; efficiency/LLoC are auxiliary.
- **Evaluation:** seven modalities/tasks; 0.5–3.5h and 16/48GB limits; Quadro RTX8000 48GB or V100 16GB; normally 8 trials/config, MLAB step/time limits, five backbones/scaffolds. Best tested closes 9.3% gap; human/generated ideas not consistently helpful. Best-of-8 must be retained.
- **Boundary/trade-off/failures/coexistence:** proves subjective novelty misaligns with executable improvement in this suite, not all science/autonomy. Curation, baseline strength, leakage, API drift and best-of-N cost remain. Human review still owns novelty/ethics/causality.
- **Owner/adjacent/disposition:** Ch66, handoff Ch81. `Refine Candidate`.

### Low-score Closures

- Nova Reel 1.1 — official 2025-04-07, `amazon-nova-reel-11`, `2/3/4/5/3/1=18`; product fact, internal mechanism/eval absent.
- TensorRT-LLM v0.18.1 — release 2025-04-09, `tensorrt-llm-v018x`, `1/3/3/5/3/1=16`; same-family dependency revision.
- Transformers v4.51.1/2 — 2025-04-08/10, `transformers-v451x`, `1/3/4/5/4/1=18`; patch bundle, no single mechanism.
- Gemini 2.5 Flash preview — official 2025-04-09, `gemini-25-flash-preview`, `2/3/4/5/3/2=19`; version fact/mechanism undisclosed.
- VCR-Bench — arXiv:2504.07956 v1 2025-04-10, `3/3/3/4/3/3=19`; benchmark-only evidence.
- MM-IFEngine — arXiv:2504.07957 v1 2025-04-10, v2 04-27, `3/3/3/4/3/3=19`; dataset/evaluator case.
- SoTA with Less — arXiv:2504.07934 v1 2025-04-10, v2/v3 05-28/30, `3/3/3/4/3/3=19`; author experiment snapshot.

## Evidence Level

- 34/34 retained candidates：Strict Full Source Review Complete。
- 7/7 low-score candidates：Identity / Date / Score / Rejection Complete。
- Ordinary Review Pending / Blocked / Disputed：0 / 0 / 0。
- A2A 的 exact 2025-04-09 source tree 是 Archive P3，不被伪装成 candidate pending，也不用于推断 later-schema field。

## Cross-Week Deduplication

- 13 个 pre-04-14 families 从 W16 回拨 W15，W16 后续必须移除或只保留 routing note。
- Nemotron 回 W12；vLLM Q2 roadmap 回 W13；PaperBench v3 只作 W14 related evidence；vLLM v0.8.4 保留 W16。
- revision 只作为同一 Source Family 的演进节点，不重复评分。

## Knowledge Tree Position

Owner 覆盖 Multimodal、Training、Inference、Platform 与 Agent 的既有 Stable Node；本轮不创建新节点。A2A 由 AGENT-MULTI-AGENT 持有，并向 AGENT-MCP、AGENT-PLATFORM handoff。

## Recommended Action

保留 41 个 owner 的证据与演进关系，等待年度 Historical Evidence Gate 闭合后再逐 Source Family 决定 Books disposition。A2A 后续若取得 2025-04-09 commit bundle，可补强事件时 schema，但不扩大当前结论。

## Event-Date Daily Decision

Historical Backfill 不补造 Daily。所有事件日期直接记录在本 Weekly，spillback 只按 first-public date 路由。

## Books Integration Decision

**Books Frozen — Historical Gate Closed.**

## Ignored Noise

非技术机构动态、已由前后周持有的 revision、只有产品能力而无公开机制的公告，以及无法形成独立 AI-System mechanism 的候选未重复计分；低分项仍保留可审计拒绝。

## Repository Changes

- W15 owner ledger 从 28 修正为 41。
- 写回 A2A replacement review 与 13 个 W16 spillback Full Source Reviews。
- Candidate Evidence Gate 改为 Passed；Discovery / Archive Gate 保持 Conditional Open。
- 未修改 Books，未 stage、commit 或 push。

## Open Questions

- 能否取得 2025-04-09 A2A README/spec/schema 的 commit-pinned bundle 或可信 archive？
- 全年度结束时，如何对 W15/W16 spillback 与 later revision 做一次机器可复算的 family-level 去重？
- 哪些 Refine Candidate 最终改变 Books 的机制论证，哪些只作为既有 argument 的受限案例？

## Sources

- Kimi-VL — https://arxiv.org/abs/2504.07491（First Public: 2025-04-10；Accessed: 2026-07-31）
- Kimi-VL HTML — https://arxiv.org/html/2504.07491（v3 revision: 2025-06-23；Accessed: 2026-07-31）
- Kimi-VL repository — https://github.com/MoonshotAI/Kimi-VL（Accessed: 2026-07-31）
- Agent2Agent announcement — https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/（First Public: 2025-04-09；Full Source Review Complete — claims narrowed; Archive P3 remains；Accessed: 2026-08-22）
- Google ADK v0.1.0 — https://github.com/google/adk-python/releases/tag/v0.1.0（First Public: 2025-04-09；Full Source Review Complete；Accessed: 2026-08-22）
- Ironwood TPU — https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/（First Public: 2025-04-09；Full Source Review Complete；Accessed: 2026-08-22）
- Amazon Nova Sonic — https://aws.amazon.com/blogs/aws/introducing-amazon-nova-sonic-human-like-voice-conversations-for-generative-ai-applications/（First Public: 2025-04-08；Full Source Review Complete；Accessed: 2026-08-22）
- Hogwild! Inference — https://arxiv.org/abs/2504.06261（v1: 2025-04-08；Full Source Review Complete；Accessed: 2026-08-22）
- HybriMoE — https://arxiv.org/abs/2504.05897（v1: 2025-04-08；Full Source Review Complete；Accessed: 2026-08-22）
- VAPO — https://arxiv.org/abs/2504.05118（v1: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- OLMoTrace — https://arxiv.org/abs/2504.07096（v1: 2025-04-09；Full Source Review Complete；Accessed: 2026-08-22）
- SmolVLM — https://arxiv.org/abs/2504.05299（v1: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- One-Minute Video Generation with TTT — https://arxiv.org/abs/2504.05298（v1: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- T1 / Tool-integrated Verification — https://arxiv.org/abs/2504.04718（v1: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- Quantization Hurts Reasoning? — https://arxiv.org/abs/2504.04823（v1: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- A Sober Look at Progress in LM Reasoning — https://arxiv.org/abs/2504.07086（v1: 2025-04-09；Full Source Review Complete；Accessed: 2026-08-22）
- SkillWeaver — https://arxiv.org/abs/2504.07079（v1: 2025-04-09；Full Source Review Complete；Accessed: 2026-08-22）
- Auditing Model Substitution in LLM APIs — https://arxiv.org/abs/2504.04715（v1: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- Scaling Laws for Native Multimodal Models — https://arxiv.org/abs/2504.07951（v1: 2025-04-10；Full Source Review Complete；Accessed: 2026-08-22）
- Missing Premise exacerbates Overthinking — https://arxiv.org/abs/2504.06514（v1: 2025-04-08；Full Source Review Complete；Accessed: 2026-08-22）
- DDT / Decoupled Diffusion Transformer — https://arxiv.org/abs/2504.05741（v1: 2025-04-08；Full Source Review Complete；Accessed: 2026-08-22）
- C3PO — https://arxiv.org/abs/2504.07964（v1: 2025-04-10；Full Source Review Complete；Accessed: 2026-08-22）
- SGLang v0.4.5 — https://github.com/sgl-project/sglang/releases/tag/v0.4.5（First Public: 2025-04-07；Full Source Review Complete；Accessed: 2026-08-22）
- Nova Reel 1.1 — https://aws.amazon.com/blogs/aws/amazon-nova-reel-1-1-featuring-up-to-2-minutes-multi-shot-videos/（First Public: 2025-04-07；Low-score Closure；Accessed: 2026-08-22）
- TensorRT-LLM v0.18.1 — https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v0.18.1（First Public: 2025-04-09；Low-score Closure；Accessed: 2026-08-22）
- Transformers v4.51.1 — https://github.com/huggingface/transformers/releases/tag/v4.51.1（First Public: 2025-04-08；Low-score Closure；Accessed: 2026-08-22）
- Transformers v4.51.2 — https://github.com/huggingface/transformers/releases/tag/v4.51.2（First Public: 2025-04-10；Low-score Closure；Accessed: 2026-08-22）
- Gemini 2.5 Flash preview — https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-2025-sundar-pichai-keynote/（First Public: 2025-04-09；Low-score Closure；Accessed: 2026-08-22）
- VCR-Bench — https://arxiv.org/abs/2504.07956（v1: 2025-04-10；Low-score Closure；Accessed: 2026-08-22）
- MM-IFEngine — https://arxiv.org/abs/2504.07957（v1: 2025-04-10；Low-score Closure；Accessed: 2026-08-22）
- SoTA with Less — https://arxiv.org/abs/2504.07934（v1: 2025-04-10；Low-score Closure；Accessed: 2026-08-22）
- PaperBench v3 — https://github.com/openai/preparedness/blob/main/project/paperbench/paperbench.pdf（Related Evidence；canonical owner W14；Accessed: 2026-08-22）
- Rethinking Reflection — https://arxiv.org/abs/2504.04022（v1: 2025-04-05；spillback W14；Accessed: 2026-08-22）
- vLLM Q2 2025 roadmap — https://github.com/vllm-project/vllm/issues/15735（First Public: 2025-03-29；spillback W13；Accessed: 2026-08-22）

### Added spillback sources

- A2A launch: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- Archived A2A spec: https://google-a2a.github.io/A2A/specification/
- A2A v0.1.0: https://a2a-protocol.org/v0.1.0/specification/
- https://arxiv.org/abs/2504.08685 — Seaweed-7B, v1 2025-04-11
- https://arxiv.org/abs/2504.08736 — GigaTok, v1 2025-04-11
- https://arxiv.org/abs/2504.08388 — MineWorld, v1 2025-04-11
- https://arxiv.org/abs/2504.07615 — VLM-R1, v1 2025-04-10
- https://arxiv.org/abs/2504.07963 — PixelFlow, v1 2025-04-10
- https://arxiv.org/abs/2504.07866 — Pangu Ultra, v1 2025-04-10
- https://arxiv.org/abs/2504.07891 — SpecReason, v1 2025-04-10
- https://arxiv.org/abs/2504.08791 — PRIMA.cpp, v1 2025-04-07
- https://arxiv.org/abs/2504.08837 — VL-Rethinker, v1 2025-04-10
- https://arxiv.org/abs/2504.08942 — AgentRewardBench, v1 2025-04-11
- https://arxiv.org/abs/2504.08066 — AI Scientist-v2, v1 2025-04-10
- https://arxiv.org/abs/2504.09710 — DUMP, v1 2025-04-13
- https://arxiv.org/abs/2504.09702 — MLRC-Bench, v1 2025-04-13
- Routing evidence only: https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1 — self-reported release 2025-03-18

Accessed: 2026-08-24。
