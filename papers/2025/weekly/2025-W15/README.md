# AI Research Weekly — 2025-W15

> Coverage Window: 2025-04-07～2025-04-13
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Kimi-VL。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 本组无达到保留门槛的候选。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：Kimi-VL（2025-04-10）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Kimi-VL | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；作者 benchmark 不进入正文 |

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

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- Kimi-VL → 第 21～25、62、74 章（Layering / Dependency）

## Recommended Action

- Kimi-VL：Worth Watching；作者 benchmark 不进入正文

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W15/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- Kimi-VL 的最终 Books disposition 等全年 multimodal / training source families 去重后决定。
- W15 不得把 2025-06 v3 / Thinking-2506 结果当作 2025-04 v1 已有结论。

## Sources

- Kimi-VL — https://arxiv.org/abs/2504.07491（First Public: 2025-04-10；Accessed: 2026-07-31）
- Kimi-VL HTML — https://arxiv.org/html/2504.07491（v3 revision: 2025-06-23；Accessed: 2026-07-31）
- Kimi-VL repository — https://github.com/MoonshotAI/Kimi-VL（Accessed: 2026-07-31）
