# AI Research Weekly — 2025-W02

> Coverage Window: 2025-01-06～2025-01-12
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Rebuild Started: 2026-08-17
> Accessed: 2026-08-17
> Weekly Evidence Gate: Passed — 46/46 scoring rows；44/44 `20+` Full Source Review；2/2 low-score disposition
> Books Integration: Deferred by user request

## Executive Summary

旧档只保留 vLLM 2024 Retrospective，遗漏了本周密集出现的 reasoning self-evolution、search-in-reasoning、
World Foundation Model、visual-token compression、scientific/GUI/research Agent、多模态 retrieval 与 executable
evaluation 等证据。按 2025-01-06～12 owner window 重放，并继续扫描后续工作日页面直到连续两个工作日
不再出现本周 owner 后，原检查点恢复 35 个可评分候选并完成审计；W03 replay 又发现
Transformer-Squared（v1 2025-01-09）与 Tensor Product Attention（v1 2025-01-11）此前被错误留在 grace exclusion。
两项已回拨 W02 并完成全文、实现、实验合同、limitations、artifact 与 owner 审计。随后继续关闭 grace
identity gap 时确认 ChemAgent（arXiv:2501.06590，v1 2025-01-11）也属于 W02。继续审计 01-14～15 的
延迟发现页面后，又回拨 MinMo、O1 Replication Journey Part 3、VideoAuteur、SPAM、Grad-Mimic、Padding Tone
与 3DIS-FLUX。前六项达到 20 分并进入全文审计，3DIS-FLUX 进入低分 disposition。W03 的后续页
继续暴露 Beyond Sight / FuSe（v1 2025-01-08）这一延迟归属项；已回拨 W02，完成论文、项目页、
代码与数据 artifact 联读。W02 最终以 46 个评分行重新验收通过。本阶段不修改 Books。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-08-17。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- discovery closure 不再使用固定三工作日假设：从 2025-01-13 起继续扫描，直到连续两个后续工作日
  页面不再出现 01-06～12 owner。只把 arXiv v1 / 官方 first-public date 落在 01-06～12 的候选回拨
  W02；01-13 起首次公开的论文归 W03，不因在后续页面出现而吞入本周。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- NVIDIA Cosmos WFM 论文 v1 2025-01-07 与开放平台材料属于同一 Source Family；论文负责机制与实验，
  平台页面/仓库只负责 artifact 与版本边界。
- Microsoft Research rStar-Math v1 2025-01-08 属于本周；2025-01-20 才公开的 code 是后续 artifact node，
  不改写 event date。
- 其他机构页面若只重发论文摘要，不另行计分。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata
交叉检查。Hugging Face 日榜只用于发现，`Published` 对齐 arXiv first-public 后再决定 owner week。

### Discovery Census

| Candidate | Primary ID | First Public | Current State | Initial System Relevance |
| --- | --- | --- | --- | --- |
| rStar-Math | arXiv:2501.04519 | 2025-01-08 | Full Source Review Complete | MCTS、verified trajectory、PPM 与 self-evolution |
| Search-o1 | arXiv:2501.05366 | 2025-01-09 | Full Source Review Complete | reasoning 内 agentic retrieval、document refinement 与 batch control |
| Cosmos World Foundation Model Platform | arXiv:2501.03575 | 2025-01-07 | Full Source Review Complete | data curation、tokenizer、AR/diffusion WFM 与 physical-AI platform |
| LLaVA-Mini | arXiv:2501.03895 | 2025-01-07 | Full Source Review Complete | early-layer pre-fusion 与 extreme visual-token compression |
| Towards System 2 Reasoning / Meta-CoT | arXiv:2501.04682 | 2025-01-08 | Full Source Review Complete | latent reasoning process、search/data/training taxonomy |
| Agent Laboratory | arXiv:2501.04227 | 2025-01-07 | Full Source Review Complete | literature→experiment→report 的 research workflow |
| URSA | arXiv:2501.04686 | 2025-01-08 | Full Source Review Complete | multimodal CoT understanding 与 verification contract |
| InfiGUIAgent | arXiv:2501.04575 | 2025-01-08 | Full Source Review Complete | GUI action、reasoning/reflection data 与 environment state |
| Sa2VA | arXiv:2501.04001 | 2025-01-07 | Full Source Review Complete | dense grounded image/video representation |
| MotionBench | arXiv:2501.02955 | 2025-01-06 | Full Source Review Complete — PDF used; arXiv HTML mismatch recorded | motion evidence、frame rate 与 Through-Encoder fusion |
| PPTAgent | arXiv:2501.03936 | 2025-01-07 | Full Source Review Complete | deck-level artifact generation 与 evaluation |
| Diffusion as Shader | arXiv:2501.03847 | 2025-01-07 | Full Source Review Complete | 3D-aware control as diffusion rendering branch |
| OpenOmni | arXiv:2501.04561 | 2025-01-08 | Full Source Review Complete | zero-shot omnimodal alignment 与 emotional speech output |
| Dolphin | arXiv:2501.03916 | 2025-01-07 | Full Source Review Complete | thinking/practice/feedback closed-loop research Agent |
| Segmenting Text and Learning Rewards | arXiv:2501.02790 | 2025-01-06 | Full Source Review Complete | segment reward granularity for RLHF |
| GeAR / Generation Augmented Retrieval | arXiv:2501.02772 | 2025-01-06 | Full Source Review Complete | retrieval-localization dual path 与 generated evidence |
| Modern GAN Baseline | arXiv:2501.05441 | 2025-01-09 | Full Source Review Complete | GAN modernization 与 diffusion comparison boundary |
| Autoregressive Pre-training from Videos / Toto | arXiv:2501.05453 | 2025-01-09 | Full Source Review Complete | video-as-sequence pretraining evidence |
| DriveBench / VLM Reliability for Autonomous Driving | arXiv:2501.04003 | 2025-01-07 | Full Source Review Complete | reliability/data/metric contract for embodied use |
| Centurio | arXiv:2501.05122 | 2025-01-09 | Full Source Review Complete | multilingual VLM data/architecture drivers |
| SWE-Fixer | arXiv:2501.05040 | 2025-01-09 | Full Source Review Complete — v1 PDF used; arXiv HTML mismatch recorded | efficient repository issue resolution training |
| VideoRAG | arXiv:2501.05874 | 2025-01-10 | Full Source Review Complete | video retrieval、multimodal evidence 与 cost boundary |
| SCRIT / Self-Evolving Critic | arXiv:2501.05727 | 2025-01-10 | Full Source Review Complete | synthetic critique、自验证与 scalable oversight |
| LlamaV-o1 | arXiv:2501.06186 | 2025-01-10 | Full Source Review Complete — Disputed efficiency accounting | step-level visual reasoning metric 与 curriculum |
| OmniManip | arXiv:2501.03841 | 2025-01-07 | Full Source Review Complete | object-centric interaction primitive 与 spatial constraint |
| OVO-Bench | arXiv:2501.05510 | 2025-01-09 | Full Source Review Complete | online video understanding、streaming state 与 evaluator |
| Migician | arXiv:2501.05767 | 2025-01-10 | Full Source Review Complete | free-form multi-image grounding identity |
| Multiagent Finetuning | arXiv:2501.05707 | 2025-01-10 | Full Source Review Complete | diverse reasoning chains 与 self-improvement |
| ReFocus | arXiv:2501.05452 | 2025-01-09 | Full Source Review Complete — dataset count inconsistency recorded | visual editing action as intermediate reasoning state |
| ConceptMaster | arXiv:2501.04698 | 2025-01-08 | Full Source Review Complete | multi-concept video personalization without test-time tuning |
| Multi-subject Open-set Video Personalization | arXiv:2501.06187 | 2025-01-10 | Full Source Review Complete | identity/state composition in video generation |
| Domain-adaptive Post-training for Financial LLMs | arXiv:2501.04961 | 2025-01-09 | Full Source Review Complete — event date corrected | domain data、continued pretraining 与 instruction tuning branch |
| Transformer-Squared / Self-adaptive LLMs | arXiv:2501.06252 | 2025-01-09 | Full Source Review Complete — W03 spillback recovered | SVF expert、task dispatch、two-pass adaptive weights |
| Tensor Product Attention / T6 | arXiv:2501.06425 | 2025-01-11 | Full Source Review Complete — W03 spillback recovered | contextual Q/K/V factorization 与 architecture-native KV compression |
| ChemAgent / Self-updating Library | arXiv:2501.06590 | 2025-01-11 | Full Source Review Complete — grace identity gap recovered | planning/execution/knowledge memory、runtime update 与 evaluator/refinement |
| MinMo | arXiv:2501.06282 | 2025-01-10 | Full Source Review Complete — delayed discovery spillback | aligned speech model、streaming decoder、duplex-control state 与 latency contract |
| O1 Replication Journey Part 3 | arXiv:2501.06458 | 2025-01-11 | Full Source Review Complete — delayed discovery spillback | long-reasoning distillation、test-time token budget 与 domain-knowledge boundary |
| VideoAuteur | arXiv:2501.06173 | 2025-01-10 | Full Source Review Complete — delayed discovery spillback | action→caption→visual-state hierarchy 与 long-video continuity |
| SPAM | arXiv:2501.06842 | 2025-01-12 | Full Source Review Complete — delayed discovery spillback | spike-aware clipping、optimizer-state reset 与 sparse momentum |
| Grad-Mimic / Mimic Score | arXiv:2501.06708 | 2025-01-12 | Full Source Review Complete — delayed discovery spillback | reference-weight direction、per-sample utility 与 data-selection control loop |
| Padding Tone | arXiv:2501.06751 | 2025-01-12 | Full Source Review Complete — delayed discovery spillback | padding representation、causal intervention 与 architecture-dependent behavior |
| Beyond Sight / FuSe | arXiv:2501.04693 | 2025-01-08 | Full Source Review Complete — delayed discovery spillback | language-grounded heterogeneous sensors、action policy 与 partial-observability contract |
| 3DIS-FLUX | arXiv:2501.05131 | 2025-01-09 | Low-score Rejected — delayed discovery spillback | narrow multi-instance DiT attention-mask renderer case |

### Grace-window Exclusions

2025-01-14～15 页面中的 BIOMEDICA、WebWalker、MiniMax-01 等 first-public date 从 2025-01-13 起，
归 W03；它们只证明 grace replay 已执行，不计入 W02 分母。MinMo、O1 Replication Journey Part 3、
VideoAuteur、SPAM、Grad-Mimic、Padding Tone 与 3DIS-FLUX 的 v1 实际落在 01-09～12，已回拨 W02。
Beyond Sight / FuSe 虽在 W03 的延迟页面中被再次发现，但 v1 为 2025-01-08，也已回拨 W02；后续 ICRA
接收、代码和数据发布作为同一 Source Family 的 artifact/revision，不另行计分。
Transformer-Squared
（v1 2025-01-09）与 Tensor Product Attention（v1 2025-01-11）虽在后续页面出现，owner date仍在 W02，
已从错误 exclusion 回拨并完成 Full Source Review。Process Reward Model lessons已唯一定位为 arXiv:2501.07301、
v1 2025-01-13，归 W03；ChemAgent已唯一定位为 arXiv:2501.06590、v1 2025-01-11，回拨 W02审计。

DPO Kernels 虽在 2025-01-09 榜单出现，但 arXiv v1 为 2025-01-05，已回拨 W01 并完成 Full Source
Review；不在 W02 重复计分。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留并已完成：vLLM 2024 Retrospective and 2025 Vision（2025-01-10）。
- fixed-source release ledger 确认 Transformers 4.48.0（2025-01-10）与 llama-cpp-python 0.3.6
  （2025-01-08）落在本周。前者因 release packaging、attention abstraction 与 assisted decoding contract
  达到 20 分并完成官方 Release/相关 PR 审计；后者仅为 upstream pin 与 streaming lock 修复，低分保留。
  其余项目以相邻 release boundary 闭合，不把普通 commit 自动提升为候选。

### Engineering Release Ledger

| Candidate | Official Date | Evidence Status | Final Disposition |
| --- | --- | --- | --- |
| Transformers 4.48.0 | 2025-01-10 | Official Release + relevant merged PRs verified | Full Source Review Complete；Weekly Only — Version Bundle |
| llama-cpp-python 0.3.6 | 2025-01-08 | Official tag + versioned changelog verified | Low-score Rejected；upstream pin / scoped bugfix |

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Cosmos World Foundation Model Platform | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| rStar-Math | 5 | 4 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Domain-adaptive Post-training for Financial LLMs | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| DriveBench | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| SCRIT / Self-Evolving Critic | 5 | 4 | 5 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| OmniManip | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| URSA | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Search-o1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Segmenting Text and Learning Rewards | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| GeAR / Generation Augmented Retrieval | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Autoregressive Pre-training from Videos / Toto | 4 | 4 | 4 | 5 | 4 | 5 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| SWE-Fixer | 4 | 4 | 5 | 5 | 5 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Multiagent Finetuning | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| ReFocus | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Tensor Product Attention / T6 | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Transformer-Squared / Self-adaptive LLMs | 5 | 4 | 4 | 5 | 5 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| ChemAgent / Self-updating Library | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| SPAM | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| Grad-Mimic / Mimic Score | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| MinMo | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| VideoAuteur | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| O1 Replication Journey Part 3 | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Padding Tone | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Beyond Sight / FuSe | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Towards System 2 Reasoning / Meta-CoT | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| LLaVA-Mini | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Sa2VA | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| MotionBench | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| PPTAgent | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| OpenOmni | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Centurio | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| OVO-Bench | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Migician | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Multi-subject Open-set Video Personalization | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Diffusion as Shader | 4 | 4 | 4 | 5 | 3 | 4 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Agent Laboratory | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| InfiGUIAgent | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Dolphin | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| VideoRAG | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| ConceptMaster | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| LlamaV-o1 | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Full Review Complete；Disputed — Books Frozen |
| Modern GAN Baseline | 4 | 3 | 3 | 5 | 3 | 4 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| vLLM 2024 Retrospective and 2025 Vision | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| Transformers 4.48.0 | 2 | 3 | 4 | 5 | 4 | 2 | 20/30 | Full Review Complete；Weekly Only — Version Bundle |
| llama-cpp-python 0.3.6 | 2 | 3 | 4 | 5 | 2 | 1 | 17/30 | Low-score Rejected；upstream pin / scoped bugfix |
| 3DIS-FLUX | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Low-score Rejected；narrow renderer case，缺少独立系统机制 |

> 43 个论文/Research 候选达到 20 分并完成全文、实验合同和 limitations 审计；工程 release 已完成一项
> 20 分 Source Review。两个低分候选均保留 identity/date/rejection 核验。

### Low-score Disposition Ledger

| Candidate | First Public | Verification | Rejection Reason |
| --- | --- | --- | --- |
| llama-cpp-python 0.3.6 | 2025-01-08 | official release/tag/changelog verified | upstream pin 与 scoped streaming lock fix，不能建立新的通用 runtime/concurrency 结论 |
| 3DIS-FLUX | 2025-01-09 | arXiv v1 method/evaluation/ablation verified | 以 FLUX joint-attention mask 扩展既有 3DIS 的窄域 renderer case；系统 owner、可移植 contract 与长期适用面不足 |

### Deep Analysis 1 — vLLM 2024 Retrospective and 2025 Vision

- First Public: 2025-01-10
- Status: Official project retrospective
- Primary Source: https://vllm.ai/blog/2025-01-10-vllm-2024-wrapped-2025-vision
- Evolution Relationship: Direct Evolution

#### Why

vLLM 团队把 V0 运行经验收束为 V1 架构目标，提示 serving engine 的扩展瓶颈已从单项 kernel 转向 scheduler、request state 与 execution loop 的共同复杂度。

#### Principle and Mechanism

来源是路线回顾而非正式 release；它提出 V1 重构方向，但具体机制须以后续 V1 alpha 文章和代码为准。

#### Trade-off and Evidence Boundary

路线图能解释设计动机，却不能证明性能或稳定性；本周仅作为后续 V1 事件的前置证据。

#### Connection and Evolution

知识树位置：第 46、52 章。Worth Watching；与 W05 的 V1 正式机制联合审查。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### vLLM 2024 Retrospective and 2025 Vision

- **Candidate / Week / Score:** vLLM 2024 Retrospective and 2025 Vision / 2025-W02 / 20/30。
- **Source Family ID:** `vllm-v0-to-v1-runtime`；与 W05 V1 Alpha 联读。
- **Source Type:** 官方项目 retrospective/roadmap Blog，不是论文、release notes 或性能报告。
- **First-public Date / Revision History:** 2025-01-10 发布；页面未提供可审计 revision history。
- **Direct Primary Sources:** vLLM 官方全文，
  https://vllm.ai/blog/2025-01-10-vllm-2024-wrapped-2025-vision。
- **Related Primary Sources:** W05 V1 Alpha 官方 architecture Blog 与其链接的 repository/code paths。
- **Access and Verification Status:** Verified as official project statement；路线愿景可核验，尚不能将
  计划项当作已发布行为。
- **Full-read Coverage:** 已读 2024 feature/hardware/model retrospective、community/usage 部分、V1
  motivation、2025 vision 与全部引用链接说明；没有 method/evaluation/limitations 章节可读。
- **Original Problem:** vLLM V0 在快速增加 quantization、prefix cache、chunked prefill、speculative
  decoding、structured output、distributed serving 等功能时，execution paths 与内部复杂度同步增长。
- **Why the Previous Design Was Reasonable:** V0 先验证 PagedAttention、continuous batching 与开放生态，
  以增量功能响应多模型、多硬件需求，是早期项目扩张阶段的合理选择。
- **Changed Constraint:** feature breadth、hardware diversity 与 production adoption 使局部扩展不再只
  是 kernel 问题，而成为 scheduler、request state 与 execution loop 的可维护性问题。
- **Mechanism:** 本来源只提出 V1 将采用更开放、模块化架构并重构核心；未披露统一 scheduler、
  EngineCore 或 persistent batch 的完整机制，这些只能由 W05 source family 证明。
- **State Ownership:** Not Disclosed；文章没有定义 scheduler/worker 间 request state owner。
- **Control Flow / Data Flow:** Not Disclosed；只列出 V0 能力与 V1 方向。
- **Implementation Details:** 公开 V0 已支持的能力类别与 V1 development intention；没有稳定 API、
  code path 或兼容性 contract。
- **Evaluation Setup:** Not Disclosed；这是 retrospective/roadmap，没有受控 workload、measurement protocol 或 V0/V1 性能实验。
- **Baselines / Ablations / Sensitivity:** Not Disclosed；无受控 V0/V1 对照、feature ablation 或 hardware/workload sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 文章列举生态覆盖，但没有把
  性能数字绑定为统一 workload contract，因此本次不提取性能结论。
- **What the Evidence Actually Proves:** 证明项目方在 2025-01-10 已把 V0 technical debt 与 V1
  architecture rewrite 设为公开演进方向。
- **What It Does Not Prove:** 不证明 V1 已完成、稳定、兼容或更快，也不证明任何 roadmap item 的
  production semantics。
- **Limitations / Threats to Validity:** retrospective 由项目方撰写，目标偏愿景；缺少 code-level
  mechanism、失败经验分解与独立 benchmark。
- **Trade-offs / New Failure Modes:** rewrite 可降低长期耦合，但会引入 feature parity、migration、
  compatibility 与 alpha regression 风险；本来源尚未量化这些风险。
- **Where the Previous Design Still Applies:** V0 在 V1 feature parity 未完成、旧硬件或既有 integration
  上仍是合理路径；roadmap 不能静默废弃已验证的 V0 contract。
- **Evolution Relationship:** `Direct Evolution`，但它只负责记录“为什么重构”，机制由 W05 负责。
- **ROADMAP Node:** Ch46 主 owner，Ch52 负责 scheduler 的跨引擎原则。
- **Target and Adjacent Chapters Read:** 已读 Ch45～47 与 Ch50～52 的 architecture、memory、scheduling
  边界。
- **Existing Coverage:** Ch46 已覆盖 vLLM runtime；当前没有必要把年度功能清单写入正文。W05 联读
  后再判断是否补 V0→V1 的 state/control evolution。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；年度愿景没有独立于 W05 V1 source family 的新机制。
  不能在 W05 Source Packet 完成前关闭 source family。
- **Changed Files or Rejection Reason:** 不改 Books；功能愿景由 W05 的 V1 primary evidence 与 Ch46 当前架构覆盖。
- **Open Questions:** 哪些 V0 paths 被统一、哪些 feature/hardware 在 alpha 期缺失，以及迁移期两个
  engine 的 correctness/observability contract 如何并存。

### rStar-Math

- **Candidate / Week / Score:** rStar-Math / 2025-W02 / 28/30。
- **Source Family ID:** `rstar-math-self-evolved-search`。
- **Source Type:** arXiv primary research paper；event-time code 尚未公开。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续修订与 2025-01-20 code
  release 只作为 revision/artifact nodes，不改写本周事件日期。
- **Direct Primary Sources:** arXiv v1 HTML/PDF，https://arxiv.org/html/2501.04519v1。
- **Related Primary Sources:** 作者后续 repository 只用于核验 artifact evolution；本 packet 的机制和实验
  以 v1 正文为准。
- **Access and Verification Status:** Verified；v1 正文 26 页与影响主张的表格、算法和附录均可读。
- **Full-read Coverage:** metadata、Introduction/Related Work、MCTS 与 code-augmented CoT、PPM、四轮
  self-evolution、training-data construction、全部 benchmark、baseline/ablation、discussion 与 appendix。
- **Original Problem:** 小模型缺少高质量深思考轨迹；依赖 frontier teacher 蒸馏既昂贵，也把 teacher
  的错误与风格固定进训练数据。
- **Why the Previous Design Was Reasonable:** rejection sampling 与 outcome reward 只需终局答案，监督
  成本低，在可验证数学题上能快速过滤错误答案；teacher distillation 则提供现成的长推理轨迹。
- **Changed Constraint:** 当目标变为让 1.5B～7B policy 自己产生并改进推理时，只看终局答案无法区分
  途中哪些步骤可信，也无法稳定训练 process reward。
- **Mechanism:** 以自然语言步骤加可执行 Python 构造 MCTS 节点；用终局答案验证回传 Q-value；从
  同一状态的高低 Q-value continuation 构造成对偏好，训练 pairwise Process Preference Model；再用该
  PPM 引导后续搜索，迭代产生新的 SFT trajectories。
- **State Ownership:** search tree 拥有 node/visit/Q-value；Python executor 只返回运行结果；terminal
  answer checker 拥有最终任务判定；PPM 是由旧 policy trajectory 派生的版本化 evaluator，不能充当永恒真值。
- **Control Flow / Data Flow:** problem → 多次 MCTS rollout → NL/code step 执行 → terminal verification
  → Q-value backprop → pair construction → PPM update → 下一轮 guided search → correct trajectories → policy SFT。
- **Implementation Details:** 四轮 self-evolution；约 74.7 万道数学题；默认每题 16 rollouts，困难题再
  增 16；每轮选两个正确轨迹进入 SFT。作者报告训练数据生成可在 4×40GB A100 上执行，但这不是完整
  端到端成本合同。
- **Evaluation Setup:** 1.5B～7B policy；MATH、AIME、AMC、OlympiadBench、CollegeMath、GSM8K、
  Gaokao；test-time 8 或 64 trajectories。结果是作者实验，不是独立复现。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 GPT distillation、random selection、rejection
  sampling；比较 ORM、pointwise Q model 与 pairwise PPM；验证 search/sample 数变化。未给出完整端到端
  能耗、wall-clock 与 failure recovery 成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露 1.5B～7B 模型及部分
  4×A100-40GB data-generation 条件；precision、完整 batch/concurrency、length distribution 与 SLO
  `Not Disclosed`，不提取跨系统吞吐结论。
- **What the Evidence Actually Proves:** 在作者选定的可执行数学任务与模型族中，search 产生的相对
  process preference 能替代单纯 outcome filtering，并形成可重复的 policy/evaluator 共演化循环。
- **What It Does Not Prove:** 不证明每个可执行步骤在语义上正确，不证明对不可自动验证任务有效，
  也不证明小模型已摆脱外部题库、规则与 terminal verifier。
- **Limitations / Threats to Validity:** 无独立 limitations 章节；核心风险是 self-training 的相关误差、
  benchmark contamination、搜索计算放大，以及 executor 只能验证可运行性。一般任务仍需测试、人工或多方验证。
- **Trade-offs / New Failure Modes:** 以大量 rollout 与执行换更细粒度 supervision；同时引入 reward/policy
  共漂移、PPM 偏差放大、错误但可执行步骤、search tree 成本与 event-time artifact 缺失。
- **Where the Previous Design Still Applies:** 终局判定足够可靠且预算受限时，rejection sampling 仍更简单；
  有高质量 teacher 时，distillation 仍可降低早期探索成本。
- **Evolution Relationship:** `Direct Evolution`：outcome filtering → process preference → evaluator-guided
  search → policy/evaluator self-evolution；不是“自训练取代所有外部监督”。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；`TRAIN-GRPO`（Ch33）接 trajectory lifecycle，
  `AGENT-PLANNING`（Ch79）接 test-time search。
- **Target and Adjacent Chapters Read:** 已核对 Ch30～34 与 Ch79 的 objective、verifier、trajectory、
  search 与 evidence 边界。
- **Existing Coverage:** Books 已有 reward/verifier 与 typed trajectory 原则；是否需要补“search-derived
  process preference 的闭环”必须等 Books 阶段逐段去重。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；用户明确要求先完成 Weekly。
- **Open Questions:** 如何用独立 held-out verifier 阻止 policy/PPM 共漂移；不可自动验证任务如何构造
  低成本但不自证循环的 process evidence。

### Search-o1

- **Candidate / Week / Score:** Search-o1 / 2025-W02 / 26/30。
- **Source Family ID:** `search-o1-agentic-retrieval-in-reasoning`。
- **Source Type:** arXiv primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 revision 不改写 owner week。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05366v1。
- **Related Primary Sources:** 文中使用的 Bing Search 与 Jina Reader 是实验依赖，不作为本论文机制主张的
  独立证据。
- **Access and Verification Status:** Verified；正文、算法、prompts、evaluation 和 appendix 可读。
- **Full-read Coverage:** metadata、Introduction/Related Work、agentic search、Reason-in-Documents、batch
  inference、全部 QA/reasoning evaluation、retrieval-scale analysis、prompts 与 appendix。
- **Original Problem:** 标准 RAG 在推理开始前一次性塞入文档；长链推理直到中途才暴露知识缺口时，
  初始 query 已过时，而直接追加全文会制造 context overload。
- **Why the Previous Design Was Reasonable:** pre-retrieval 简单、延迟可控、易批处理；当问题只有一个
  明确知识缺口时，top-k context 足以支撑生成。
- **Changed Constraint:** reasoning-intensive 问题的 query 随中间状态变化，且网页噪声、长度与来源数量
  使“多取文档”不能线性提升有效证据。
- **Mechanism:** reasoning model 在 CoT 中生成 search query；系统取 Bing top-10 snippets 并经 Jina
  Reader 打开候选页面；Reason-in-Documents 先在每份材料内推理与压缩，再把相关知识返回主 CoT；
  batch controller 管理多个序列的搜索与继续生成。
- **State Ownership:** main reasoning trace 拥有当前问题状态；retriever 拥有候选集合；per-document
  refinement 产生派生 evidence view；外部网页不因被检索就成为可信事实。
- **Control Flow / Data Flow:** prompt → reasoning → search trigger/query → top-10 snippets → URL selection
  → document read/refinement → compressed evidence → resume reasoning → final answer；检索失败可回退直接推理。
- **Implementation Details:** QwQ-32B-Preview；Bing US-EN top-10；Jina Reader；最大 32,768 tokens；
  temperature 0.7、top-p 0.8、top-k 20、repetition penalty 1.05；作者实现 batch inference 与失败回退。
- **Evaluation Setup:** GPQA、数学、LiveCodeBench，以及 NQ、TriviaQA、HotpotQA、2Wiki、MuSiQue、
  Bamboogle；使用 Pass@1、EM/F1；8×A800-80GB。网页内容与搜索排序会随时间变化。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 direct reasoning、standard top-10 RAG 与
  RAgent，并分析检索文档数量；没有把 search/read 网络延迟、供应商失败和 prompt-injection 防护纳入
  production SLO，也没有完整组件 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型、8×A800-80GB、最大长度与
  sampling 参数已披露；precision、实际 batch/concurrency 分布、web latency 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 workload 上，把检索动作放进 reasoning loop，并先对
  文档做 query-conditioned refinement，比一次性静态拼接更适合随推理变化的知识缺口。
- **What It Does Not Prove:** 不证明搜索结果正确、来源可信或答案可复现；不证明对所有 QA、代码或数学
  任务优于受控知识库 RAG。
- **Limitations / Threats to Validity:** live web freshness、US-EN search bias、reader extraction failure、
  prompt injection、来源相互抄袭、回退路径的选择偏差，以及缺少独立 provenance/citation correctness gate。
- **Trade-offs / New Failure Modes:** 以多轮搜索和文档内推理换更精确的 context；新增网络成本、长尾
  latency、context contamination、恶意页面、循环搜索与压缩丢失关键限定条件。
- **Where the Previous Design Still Applies:** 受控 corpus、低延迟 SLO、查询意图稳定或 evidence 已知时，
  offline index + 单次 RAG 更可复现、更便宜，也更容易治理。
- **Evolution Relationship:** `Direct Evolution`：static retrieval → reasoning-triggered retrieval →
  document-local refinement → resumed reasoning；不是 search 对 RAG 的替代。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；Ch75 接 context packing，Ch79 接 search policy，
  Ch81 接 durable workflow。
- **Target and Adjacent Chapters Read:** 已核对 Ch75～81 的 Context、RAG、Memory、Tool、Planning、
  Reflection 与 Workflow owner 边界。
- **Existing Coverage:** Ch76 已覆盖 query/compression/stopping joint policy；Books 阶段需判断本文是否只
  作为受限案例，不能在 Weekly 阶段先行写入。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 如何把 provenance、source trust、prompt-injection isolation 与 reproducible snapshot
  纳入 reasoning-time retrieval contract；何时应停止搜索并接受不确定答案。

### Cosmos World Foundation Model Platform

- **Candidate / Week / Score:** Cosmos World Foundation Model Platform / 2025-W02 / 28/30。
- **Source Family ID:** `nvidia-cosmos-1-world-foundation-platform`。
- **Source Type:** arXiv primary technical report；模型、tokenizer、guardrail 与 artifact 组成联合平台证据。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续模型/仓库版本是同 family 的演进节点。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.03575v1。
- **Related Primary Sources:** NVIDIA 官方 model/repository artifacts 只用于核验公开权重、配置和 guardrail
  边界；本 packet 不用后来版本改写 v1 实验。
- **Access and Verification Status:** Verified；正文 1,600 余行、公式、实现、实验、post-training use
  cases、guardrails 与 appendix 均可读。
- **Full-read Coverage:** data curation、continuous/discrete tokenizer、diffusion/AR WFM、parallelism、
  Medusa、diffusion decoder、Video2World/post-training、multi-view/action conditions、evaluation、guardrails、
  limitations/failure examples 与 appendix。
- **Original Problem:** physical-AI 团队缺少可复用的视频表示、未来观测生成与条件控制底座；各应用从
  原始视频、tokenizer、生成器和安全过滤器分别搭建，数据与 artifact contract 无法共享。
- **Why the Previous Design Was Reasonable:** 专用 simulator 与任务模型可提供明确状态和物理规则，
  在封闭 domain 中可解释、可验证；通用 video generator 则适合无结构视觉生成，但不承担动作闭环。
- **Changed Constraint:** 训练规模、场景多样性与稀有事件需求推动共享 pre-trained video prior；同时
  physical-AI 需要 current observation、text、action、camera/trajectory 等多种条件，而不只是 text-to-video。
- **Mechanism:** 平台先清洗视频并用连续/离散 tokenizer 压缩；一支以 latent diffusion 迭代去噪，另一支
  以离散 token autoregressive next-token prediction；Video2World 加 observation/text cross-attention，
  post-training 再接 action、instruction、camera、trajectory 和 multi-view condition。激进离散压缩造成模糊时，
  用 conditional diffusion decoder 从 discrete latent 恢复 continuous latent 细节。
- **State Ownership:** tokenizer 拥有 representation identity；base WFM 拥有生成分布而非真实环境；
  condition encoder 拥有 text/action/camera schema；guardrail 分别在输入和输出边界裁决。真实环境状态仍由
  simulator/sensor/controller 拥有，不能交给生成视频。
- **Control Flow / Data Flow:** curated video → tokenizer → continuous/discrete latent → diffusion 或 AR
  WFM → optional conditional post-training → optional diffusion decoder → RGB video → post-guard；pre-guard
  在生成前处理 prompt。
- **Implementation Details:** diffusion 分支为 7B/14B Text2World/Video2World，AR 分支为 4B/12B base 与
  5B/13B Video2World；AR 使用 Llama-style blocks、3D position encoding 与 text cross-attention；离散压缩
  DV8×16×16，连续压缩 CV8×8×8；平台另提供 prompt upsampler、Medusa 与 pre/post guardrails。
- **Evaluation Setup:** tokenizer reconstruction、生成质量、3D/physics consistency、instruction/action/
  multi-view human/automatic metrics；作者另在 8×H100-80GB、BF16、320×512、10 FPS、Physical-AI 视频上
  测试低分辨率 AR+Medusa throughput。数字不得外推到原分辨率、其他模型或闭环控制。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 tokenizer compression、AR/diffusion 分支、
  Medusa heads、base 与 conditional variants、VideoLDM/multi-view baselines；训练总能耗、数据 license 分布、
  guardrail operating point 与真实机器人闭环 sensitivity 未完整披露。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型规模、部分 H100/BF16、
  320×512/10-FPS 与 token/frame throughput 条件已披露；训练 fleet、服务 batch/concurrency、端到端 latency
  与控制 SLO 不完整，因此只保留绑定条件的作者实验。
- **What the Evidence Actually Proves:** 证明 tokenizer、两类生成范式、conditional post-training、decoder
  与 guardrail 可以被组织为同一 physical-video foundation platform，并在作者数据与评测中支持多种条件生成。
- **What It Does Not Prove:** 不证明生成视频等于 causal simulator，不证明 action-conditioned prediction
  能产生安全策略，也不证明 10-FPS 视频生成满足机器人闭环延迟、动力学或校准要求。
- **Limitations / Threats to Validity:** 作者展示 object appearance、blur/artifact 与较小模型 corruption；
  视觉质量/偏好不等于物理可行性。数据 provenance、rare-event fidelity、guardrail false positive/negative 与
  independent reproduction 仍有限。
- **Trade-offs / New Failure Modes:** aggressive token compression 降低训练/推理成本，却丢失细节并需更
  昂贵 diffusion decoder；diffusion 提升画质但迭代慢，AR 可复用 LLM runtime/Medusa 但误差逐 token 放大；
  统一平台增加 artifact compatibility、condition schema 与 guardrail drift 风险。
- **Where the Previous Design Still Applies:** 需要守恒定律、可验证碰撞和安全控制时，传统 simulator 仍是
  权威环境；只需高质量离线视频时 diffusion 分支合理；需要低延迟 sequential prediction 时 AR 分支可能更合适。
- **Evolution Relationship:** `Layering / Dependency`：video generation prior → observation-conditioned prediction
  → action/camera/trajectory-conditioned branch → closed-loop system；报告只覆盖前三层的大部分，不证明最后一层。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；Ch23 接 tokenizer identity，Ch24 接
  AR/diffusion branch，Ch26 接 physical-action boundary，`TRAIN-DATA` 接 curation。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 的 representation、generation、world state 与
  embodied control 边界，以及 training data handoff。
- **Existing Coverage:** Ch25 已明确 video generation、predictive environment model 与 controllable world
  model 的层级；Books 阶段只应补长期缺口，不复制平台型号表。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 如何用 action-outcome、counterfactual consistency 与 closed-loop safety evidence 取代
  视觉偏好；tokenizer/decoder/condition/guardrail 版本如何形成可回滚的统一 artifact identity。

### LLaVA-Mini

- **Candidate / Week / Score:** LLaVA-Mini / 2025-W02 / 25/30。
- **Source Family ID:** `llava-mini-prefusion-visual-compression`。
- **Source Type:** arXiv primary research paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 revision 不改写 owner week。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.03895v1。
- **Related Primary Sources:** LLaVA-1.5 与 Video-LLaVA 仅作为作者 baseline/source lineage。
- **Access and Verification Status:** Verified；method、training、11 image/7 video benchmark、ablation 与
  appendix 均可读。
- **Full-read Coverage:** early-layer token analysis、query compression、modality pre-fusion、两阶段训练、
  全部 benchmark、token/layer ablation、efficiency claims、qualitative examples 与 conclusion。
- **Original Problem:** 标准 MLLM 把数百视觉 tokens 送入每层 LLM；visual token 数随 frame 数线性增长，
  prefill attention、KV state 与长视频容量迅速成为瓶颈。
- **Why the Previous Design Was Reasonable:** 保留 patch tokens 避免早期不可逆信息损失，让深层 cross-modal
  attention 可按问题选择细节；在短图像输入和通用任务上是稳健起点。
- **Changed Constraint:** 视频与多图 workload 需要把视觉状态压缩到远少于原 patch 数，而简单 pooling/
  token dropping 会丢失 query-relevant information。
- **Mechanism:** CLIP ViT-L/336 产生视觉 tokens；query compression 用文本条件 query 提取视觉状态；
  与 LLM 同型的 decoder-only modality pre-fusion block 先把视觉信息写入文本 tokens，再向主 LLM 只保留
  一枚视觉 token，试图把跨模态融合前移到较浅层。
- **State Ownership:** vision encoder 拥有 patch representation；pre-fusion module 拥有 query-conditioned
  compressed state；主 LLM 接收压缩视图而非原始视觉证据。压缩后丢失的信息没有 downstream rollback owner。
- **Control Flow / Data Flow:** image/video → CLIP tokens → projector/query compression → modality pre-fusion
  with text → one/few visual tokens + enriched text tokens → Vicuna decoder → answer。
- **Implementation Details:** Vicuna-7B、CLIP ViT-L/336、与 LLaVA-1.5 相同训练数据；默认一枚 visual token
  和四层 pre-fusion；两阶段训练，作者披露 batch 256、AdamW、stage learning rates 与 epoch 配置。
- **Evaluation Setup:** 11 个 image 与 7 个 video benchmarks；比较 LLaVA-1.5、Video-LLaVA 等；作者报告
  FLOPs/latency/可容纳 frame 数，但硬件、完整输入长度、batch/concurrency 与 SLO 没有形成统一 workload contract。
- **Baselines / Ablations / Sensitivity / Overhead:** 去掉 pre-fusion、改变 visual-token 数、改变 pre-fusion
  层数并在相近 FLOPs 下对比；结果显示 compression token 数和 pre-fusion depth 是联合设计。未充分测量
  fine-grained localization、极端运动与分布外长视频的 sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型、vision encoder、训练 batch、
  learning rate/epoch 已披露；作者 latency 所用完整硬件、precision、请求 concurrency 与 production SLO
  `Not Disclosed`，故不把 “one token” 写成通用延迟结论。
- **What the Evidence Actually Proves:** 在作者模型、数据与 benchmark 上，把一部分视觉-文本融合前移，
  可以在强压缩视觉 token 的同时保留接近 baseline 的平均任务表现；pre-fusion 比机械 token dropping 更重要。
- **What It Does Not Prove:** 不证明单 token 无损，不证明所有视觉任务或超长视频都保持细节，也不证明
  FLOPs 降幅等同端到端 serving latency/goodput 提升。
- **Limitations / Threats to Validity:** 无独立 limitations 章节；平均 benchmark 可能掩盖细粒度定位和
  temporal aliasing；prompt-conditioned compression 会把 query 选择偏差前移并使后续无法恢复原 patch evidence。
- **Trade-offs / New Failure Modes:** 大幅减少 LLM-side sequence/KV 成本，却增加前置 fusion compute、
  query coupling 与不可逆 information bottleneck；问题变化、多轮追问或需要新局部细节时可能必须重做视觉编码。
- **Where the Previous Design Still Applies:** 高精度 grounding、OCR、开放式后续提问或压缩错误不可接受时，
  保留更多视觉 tokens、late fusion 或可回读外部视觉 memory 仍更合理。
- **Evolution Relationship:** `Alternative Branch`：full visual-token late fusion ↔ query-conditioned early
  pre-fusion/compression；不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；`INFER-PREFILL`（Ch43）与
  `INFER-KV-CACHE`（Ch45）接 runtime cost boundary。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～24 的 representation/fusion 与 generation 边界，
  以及 Ch42～46 的 request、prefill、decode、KV 与 batching handoff。
- **Existing Coverage:** Ch23 已有 modality fusion、rate-distortion 与 failure modes；Books 阶段需判断是否
  用该研究深化“query-conditioned irreversible compression”，而非追加产品式案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 多轮对话中 query 改变后如何复用或更新 compressed visual state；如何用 task-specific
  distortion 而非平均 benchmark 决定 compression ratio。

### Towards System 2 Reasoning / Meta-CoT

- **Candidate / Week / Score:** Towards System 2 Reasoning in LLMs / 2025-W02 / 25/30。
- **Source Family ID:** `meta-cot-latent-search-training`。
- **Source Type:** 理论/路线型 arXiv research paper，包含受限实验，不是已交付的单一算法系统。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续 revision 作为同一 family 补充。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04682v1。
- **Related Primary Sources:** 文中 Big MATH、GPT-NeoX asynchronous RL infrastructure 与 cited search/PRM
  工作是组成路线的 related evidence，不能把各自结论合并成已验证端到端系统。
- **Access and Verification Status:** Verified；全文、公式、实验、pipeline proposal、infrastructure、open
  questions 与 MCTS/A* appendix 均可读。
- **Full-read Coverage:** Meta-CoT latent-variable formulation、generator-verifier gap、best-of-N/search、
  process supervision、Meta-RL、instruction/RL pipeline、Big MATH curation、async infrastructure、regret analysis
  与 prompts/appendices。
- **Original Problem:** 教科书式最终解答通常删去了探索、失败与回溯；直接学习线性 CoT 只拟合“被整理过的
  solution”，未必学习产生该 solution 的 latent search process。
- **Why the Previous Design Was Reasonable:** 对常规任务，短而线性的 CoT 能把计算展开到多个 token，数据易收集、
  训练稳定；best-of-N 只需并行采样与终局 verifier，是增加 inference compute 的低耦合方案。
- **Changed Constraint:** 难题需要非线性探索、回溯和 variable compute；随着样本数增加，oracle pass@k 与
  majority vote 的差距暴露出 generator-verifier gap，却也放大搜索与 verifier 成本。
- **Mechanism:** 将未写入最终解答的探索写成 latent Meta-CoT；用 MCTS/A* 产生 search traces，线性化为
  instruction data，再以 process supervision 和 RL 学习何时扩展、回退和停止；论文还提出 Meta-RL 可学习
  reasoning algorithm，而非只记住单条轨迹。
- **State Ownership:** external search controller 拥有 frontier/branch/value；PRM/verifier 拥有候选评价；
  policy 只生成 proposal。若 search 被“内化”到 token stream，branch state 与真实 verifier evidence 仍不能
  因不可见而被假定存在。
- **Control Flow / Data Flow:** problem → policy proposals → search expansion → verifier/value → branch selection
  /backtrack → linearized Meta-CoT data → SFT → online RL / new rollouts。论文提出 shared-memory async path，
  但它是 infrastructure prototype，不证明整条 pipeline 已规模化验证。
- **Implementation Details:** 受限实验以 Llama-3.1-8B 和 Numina MATH 为主，比较 greedy、majority vote、
  pass@k 与 search；Big MATH 目标是构造百万级可验证问题；GPT-NeoX 路线用 CUDA IPC 共享训练/推理权重内存。
- **Evaluation Setup:** MATH 500 problem subset 等数学任务；部分图表复用或联读 cited studies；大量结论
  是理论推断、hypothesis 和 research agenda，不是统一 benchmark 的因果证明。
- **Baselines / Ablations / Sensitivity / Overhead:** 分析训练数据量、k、greedy/majority/oracle；未完成
  policy×verifier×search 的全面 scaling law、开放任务验证、独立 ablation 或 production reliability 评估。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 公开 Llama-3.1-8B 与部分数据/采样
  条件；完整 hardware、precision、batch/concurrency、rollout length 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 论文把“最终 CoT”和“产生它的搜索过程”形式化为不同对象，并用
  受限数学实验说明额外采样/验证仍有 headroom；也给出可实现的 data→search→SFT→RL 分层路线。
- **What It Does Not Prove:** 不证明 o1/R1 内部实现了所述算法，不证明 Meta-CoT 是唯一解释，也不证明
  pure RL、linearized search 或异步共享权重已经组合成稳定生产系统。
- **Limitations / Threats to Validity:** 作者明确列出 verifier gap、open-ended verification、CoT faithfulness、
  search scaling 与 data quality；数学终局可验证性使结果不能外推科学推导和主观任务。
- **Trade-offs / New Failure Modes:** 显式搜索提高可检查性却增加 branching compute；内化 search 降低
  orchestration overhead，却隐藏状态与失败分支；async RL 降低同步成本但引入 off-policy/staleness 风险。
- **Where the Previous Design Still Applies:** 简单问题、低延迟任务或可靠 verifier 缺失时，直接 CoT、
  short SFT 和 bounded best-of-N 仍更可控。
- **Evolution Relationship:** `Direct Evolution`：linear CoT → sampled alternatives → explicit search/process
  supervision → learned search policy；各阶段可共存，不是单向替换。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；`TRAIN-GRPO`（Ch33）接 rollout lifecycle，
  `AGENT-PLANNING`（Ch79）接 search state，`TRAIN-DISTRIBUTED-TRAINING`（Ch36）接 async runtime。
- **Target and Adjacent Chapters Read:** 已核对 Ch31～36 与 Ch79 的 reward、trajectory、training/runtime
  和 planning owner 边界。
- **Existing Coverage:** Books 已覆盖 verifier、trajectory freshness 和 search planning；Books 阶段需逐条
  判断哪些是新机制，不能把论文路线图整体抄入正文。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 如何观测内化 search 的真实 branch/rollback；如何在开放任务建立不与 policy 同源的
  verifier；joint policy/verifier/search scaling law 是否稳定。

### Agent Laboratory

- **Candidate / Week / Score:** Agent Laboratory / 2025-W02 / 24/30。
- **Source Family ID:** `agent-laboratory-research-workflow`。
- **Source Type:** arXiv primary systems/workflow paper + official artifact lineage。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；本 packet 以 event-time v1 为准。
- **Direct Primary Sources:** arXiv v1 PDF，https://arxiv.org/pdf/2501.04227v1。
- **Related Primary Sources:** official repository 与 mle-solver/paper-solver artifacts 只用于实现边界；未以
  LLM reviewer 输出替代人工评估。
- **Access and Verification Status:** Verified；56 页 PDF 可读，HTML unavailable 不构成正文缺口。
- **Full-read Coverage:** Literature Review、Experimentation、Report Writing 三阶段，PhD/Postdoc/ML Engineer
  roles、commands/prompts、human feedback、cost/time/success、human/LLM review、MLE-Bench 与 limitations。
- **Original Problem:** research Agent 常把 idea generation、代码执行和写报告压成一次长调用；中间资产、
  人工接管点、失败恢复和责任边界不可见。
- **Why the Previous Design Was Reasonable:** 单 Agent loop 原型简单，适合验证工具调用；若任务短且实验已知，
  多角色 workflow 的协调成本可能大于收益。
- **Changed Constraint:** 端到端研究包含 literature、plan、data、code、execution、interpretation 与 report，
  各阶段使用不同工具和验收标准，且需要让人审阅、修改或继续扩展。
- **Mechanism:** 把流程拆成 Literature Review → Experimentation → Report Writing；PhD/Postdoc 对话生成与
  修订计划，ML Engineer 通过 mle-solver 准备/运行实验，paper-solver 生成报告；每阶段保存结构化输出并允许
  human feedback/refinement。
- **State Ownership:** workflow 拥有阶段和 artifact lineage；执行环境拥有 code/results；human researcher
  拥有研究目标与最终接受；LLM reviewer 只是启发式 evaluator，不能拥有 scientific truth。
- **Control Flow / Data Flow:** topic → paper search/full text → literature review → plan → data/code → experiment
  results → interpretation → report → review/refinement → human continuation。
- **Implementation Details:** 支持 gpt-4o、o1-mini、o1-preview backends；通过明确 command protocol 调用
  literature 和 solver tools；prompts/phase descriptions 在 appendix 公开。
- **Evaluation Setup:** 若干预设/自定义 ML topics、用户研究、LLM 与 human reviewers，以及 10 个 text/tabular
  MLE-Bench tasks；记录阶段级 cost、time、success。作者报告模型间质量差异，但样本量与 task domain 受限。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较三个 model backends，并在 MLE-Bench 与 MLAB、
  OpenHands、AIDE 对照；其他系统 invalid submissions 被排除后再平均，降低直接可比性；没有系统组件 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API model versions 与货币/时间成本已
  披露；底层 hardware、precision、token-length distribution、并发与 production SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 将研究工作拆为 durable phases、角色与 artifacts 可以形成可操作的
  human-agent research assistant，并让成本/失败定位到阶段，而非只看到最终报告。
- **What It Does Not Prove:** 不证明自动生成研究具有科学新颖性、可重复性或可替代研究者；LLM self-review
  分数不等于真实同行评议。
- **Limitations / Threats to Validity:** 作者明确承认 self-evaluation、图表质量、主观 idea evaluation、
  domain breadth 与 human replacement 边界；human reviewer 给出的总体质量/贡献不高，且 literature phase
  failure rate 明显。
- **Trade-offs / New Failure Modes:** 分阶段提高审计与接管能力，却增加 handoff、context loss、artifact
  mismatch、模型版本漂移和多 evaluator 不一致；报告写作还可能消耗大部分成本。
- **Where the Previous Design Still Applies:** 已知实验模板、单次脚本或低风险 exploratory task 仍适合
  单 Agent/人类直接执行，不必引入完整 role graph。
- **Evolution Relationship:** `Direct Evolution`：single loop → phase-separated artifacts → human-gated durable
  workflow；不是“更多 persona 就更自治”。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；Ch78 接 tool contract，Ch79/80 接 plan/reflection，
  Ch82 接 role coordination，`PLATFORM-EVALUATION-SYSTEM`（Ch66）接 evidence gate。
- **Target and Adjacent Chapters Read:** 已核对 Ch78～84 与 Ch66 的 action、planning、workflow、multi-agent
  和 evidence 边界。
- **Existing Coverage:** Books 已强调 workflow state 与 executable artifacts；是否需要补 research-specific
  phase ownership 留待 Books 阶段。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 如何让 experiment environment、dataset/version、code/result 与 report claim 强绑定；
  如何用外部 reproducibility gate 取代自评闭环。

### URSA

- **Candidate / Week / Score:** URSA / 2025-W02 / 26/30。
- **Source Family ID:** `ursa-multimodal-math-process-verifier`。
- **Source Type:** arXiv primary model/training paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续 weights/data/code 为 artifact nodes。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04686v1。
- **Related Primary Sources:** URSA model/data/code releases用于 artifact verification；Gemini-1.5-Flash-002
  是数据生成器依赖，不是 ground truth。
- **Access and Verification Status:** Verified；正文、算法、实验、ablation、hyperparameter/time appendix 可读。
- **Full-read Coverage:** hybrid vision-language architecture、960K alignment、MMathCoT-1M、DualMath-1.1M、
  error locating/misinterpretation engines、PRM training、Best-of-N、OOD evaluation、ablation 与 appendices。
- **Original Problem:** 多模态数学错误来自两条路径：视觉解释错误与逻辑推理错误；只用终局答案或文本 PRM
  无法定位二者，也不能可靠选择视觉 CoT。
- **Why the Previous Design Was Reasonable:** general MLLM 加 answer-only math data 成本低；文本 math LLM
  已有推理能力，用 projector 接视觉 encoder 是快速建立 domain baseline 的合理方案。
- **Changed Constraint:** test-time scaling 需要 process verifier，而 verifier 必须同时看图像-文本一致性与
  逻辑 continuation；单一 synthetic error source 会让 reward model 学到狭窄 shortcut。
- **Mechanism:** SAM-B+SigLIP-L 经 MLP 接 Qwen2.5-Math-7B-Instruct；三阶段训练 960K alignment、1M CoT
  SFT、1.1M dual-view process data。逻辑错误用 rollout/binary search 定位最早不可恢复步骤，视觉错误用人工
  插入的 image misinterpretation 生成；URSA-RM-7B 用 binary classification 评分轨迹并做 Best-of-N。
- **State Ownership:** base MLLM 拥有 proposal；dual-view RM 拥有 step score，不拥有原图真值；answer checker
  与 synthetic generator 分别提供弱标签。视觉 grounding evidence 必须与逻辑 reward 分开追踪。
- **Control Flow / Data Flow:** multimodal problem → N CoT rollouts → logical/visual error synthesis → step pairs
  → RM training → N candidate trajectories → RM selection → final answer。
- **Implementation Details:** 三阶段 learning rate 1e-4/1e-5/5e-6、epoch 1/2/2、batch 64/128/128，FSDP；
  16 samples 构造 process data；作者为 hybrid architecture 适配 vLLM inference。
- **Evaluation Setup:** MathVista、MathVerse、DYNAMATH、WE-MATH、GeoQA 等；默认 32×H100-HBM3，data
  generation/error locating 使用 16×H100，分别约 28/20 小时；Best-of-N 到 N=64。
- **Baselines / Ablations / Sensitivity / Overhead:** general/math MLLM baselines；CoT augmentation、error
  locating 与 misinterpretation components ablation；部分任务 N 增大到 32 后收益趋平/回落。未给独立复现、
  full data-license audit 或部署 SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型、GPU、batch、epochs、时间与
  sampling 参数较完整；训练/推理 precision、序列/图像长度、在线 concurrency 和 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者多模态数学 contract 下，将视觉误解与逻辑错误作为不同
  process supervision sources，可训练一个比单一 error source 更好的 Best-of-N selector。
- **What It Does Not Prove:** 不证明 RM step score 是真实因果归因，不证明 synthetic error 覆盖真实部署错误，
  也不证明对通用多模态或开放式证明任务有效。
- **Limitations / Threats to Validity:** generator 与 verifier 可能共享偏差；binary search 假设错误之后不可恢复，
  不适合自我修正轨迹；作者结果显示视觉识别/计算硬技能和部分 logic/position subsets 仍弱。
- **Trade-offs / New Failure Modes:** 双视角数据提高 error coverage，却增加昂贵 rollout、teacher dependence、
  标签噪声与 verifier shortcut；Best-of-N 提高选择机会，也按 N 放大 inference compute。
- **Where the Previous Design Still Applies:** 视觉不是核心、终局验证可靠或预算严格时，text PRM/outcome
  verifier 更简单；视觉感知本身不可靠时应先改善 representation，而非只加 reasoning reward。
- **Evolution Relationship:** `Layering / Dependency`：multimodal alignment → CoT SFT → dual-view process
  reward → test-time selection；后层不修复前层所有 perception failure。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；`MULTIMODAL-REPRESENTATION`（Ch23）接 visual
  evidence，`PLATFORM-EVALUATION-SYSTEM`（Ch66）接 verifier contract。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～24、Ch29～33 与 Ch66 的 representation、SFT、reward
  和 evaluation 边界。
- **Existing Coverage:** Books 已有 verifier 与 multimodal identity 原则；是否增加 dual-view reward 分支留待
  Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 可恢复/回溯式 CoT 如何替代单调错误假设；真实视觉错误分布如何独立于 teacher 合成；
  verifier 的 calibration 是否跨 benchmark 稳定。

### InfiGUIAgent

- **Candidate / Week / Score:** InfiGUIAgent / 2025-W02 / 24/30。
- **Source Family ID:** `infigui-native-reasoning-reflection`。
- **Source Type:** arXiv primary model/Agent paper + official repository lineage。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续 artifact 不改写 event date。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04575v1。
- **Related Primary Sources:** official repository用于 resource/config核验；baseline benchmark papers只提供任务定义。
- **Access and Verification Status:** Verified；method、datasets、experiments、cases 与 references 可读。
- **Full-read Coverage:** Stage-1 GUI grounding/QA/tool data、reference-augmented annotation、Stage-2 hierarchical
  reasoning、expectation/reflection、next-state auxiliary task、benchmarks、cases 与 conclusion。
- **Original Problem:** GUI Agent 只看当前截图、依赖 accessibility tree 或只输出单步 action 时，无法维护
  多步目标、验证上一步是否生效，也难跨平台复用不一致的 textual metadata。
- **Why the Previous Design Was Reasonable:** accessibility tree/Set-of-Marks 提供低成本结构和可定位元素；
  单步 imitation 在确定性 UI 中简单、延迟低，也不要求模型显式维护计划状态。
- **Changed Constraint:** raw screenshot 部署、跨 mobile/web/desktop 与长任务要求模型同时做视觉 grounding、
  strategic decomposition、tactical action 和 outcome checking。
- **Mechanism:** Stage 1 混合 GUI understanding/grounding/QA、general vision 与 function-calling SFT，并加入
  box/point reference annotation；Stage 2 从既有 trajectories 合成 Reflection → strategic/tactical reasoning →
  Action → Expectation 循环，另训练 `(observation, action) → next-state description` 辅助任务。
- **State Ownership:** environment/screenshot 拥有 observed state；trajectory 拥有 historical action；model
  expectation 是 proposal，不是实际 next state；reflection 必须比较 previous expectation 与新 observation。
- **Control Flow / Data Flow:** goal + recent screenshot/history → reflection on prior action → strategic subgoal →
  tactical grounded action → executor/environment → new screenshot → expectation mismatch check。
- **Implementation Details:** Stage 1 聚合 mobile/web/desktop GUI datasets 与非 GUI/tool data；Stage 2 使用
  GUIAct、AMEX、Android-in-the-Zoo 和 aligned examples。论文公开样本构成，但未公开完整 optimizer/hardware contract。
- **Evaluation Setup:** raw-screenshot grounding across mobile/desktop/web，以及 GUI reasoning/task benchmarks；
  比较 proprietary/open-source baselines。结果主要测离线数据和作者 benchmark，不等同真实长程环境 success。
- **Baselines / Ablations / Sensitivity / Overhead:** 多模型横向比较；未提供清晰的 Stage-2 component ablation、
  failure recovery rate、action side-effect cost 或不同 history-window sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 公开 2B model variant 与训练数据规模；
  hardware、precision、optimizer、sequence/image length、batch/concurrency、control latency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数据与 benchmark 上，先建立 raw-GUI grounding，再用合成的
  hierarchical/expectation-reflection trajectories 做 SFT，可形成一套显式 state-action reasoning interface。
- **What It Does Not Prove:** 不证明模型在开放桌面环境中可靠完成长任务，不证明 expectation 是因果 world
  model，也不证明无需 accessibility/API metadata。
- **Limitations / Threats to Validity:** reasoning data 由已有正确 action 反向合成，strategic/tactical text 可受
  hindsight leakage；expectation 虽不看 next state，action 本身来自轨迹；缺少在线干预、错误恢复与安全评测。
- **Trade-offs / New Failure Modes:** raw screenshot 提升 portability，却增加 OCR/grounding ambiguity；显式
  reflection 提高可审计性，却增加 token/latency、历史污染与“合理化既有 action”的风险。
- **Where the Previous Design Still Applies:** API/accessibility tree 可用且受信时，结构化 metadata 更精确、
  便宜；短任务或硬实时 UI 可保留模块化 planner/executor，而不是全部内化进模型。
- **Evolution Relationship:** `Layering / Dependency`：visual grounding → hierarchical proposal → action execution
  → expectation/observation comparison；训练时合成循环不等于部署时闭环已验证。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；Ch78 接 side-effect contract，Ch79/80 接 plan/
  reflection，Ch23 接 raw multimodal representation。
- **Target and Adjacent Chapters Read:** 已核对 Ch23 与 Ch78～82 的 representation、tool、planning、reflection、
  workflow 与 multi-agent 边界。
- **Existing Coverage:** Books 已把 model output 定义为 proposal、environment outcome 定义为 evidence；本文
  是否形成 GUI-specific长期缺口留待 Books 阶段。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** 如何在未知 UI transition、partial failure 与 destructive action 下验证 reflection；
  structural metadata 与 screenshot 应如何按 trust/latency 联合路由。

### Sa2VA

- **Candidate / Week / Score:** Sa2VA / 2025-W02 / 25/30。
- **Source Family ID:** `sa2va-dense-grounded-image-video`。
- **Source Type:** arXiv primary model/data paper + official code/model/data artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 artifact/revision 作为同 family 节点。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04001v1。
- **Related Primary Sources:** project page、official Hugging Face model/data 与 code 只核验公开 artifact。
- **Access and Verification Status:** Verified；正文、implementation、ablation、appendix 与 failure cases 可读。
- **Full-read Coverage:** unified task representation、LLaVA/SAM-2 coupling、SEG token、tracking memory、Ref-SAV
  annotation、multi-task co-training、全部 benchmark/ablation、implementation 与 failure appendix。
- **Original Problem:** video MLLM 擅长开放问答却不能输出像素级时空对象，SAM-2 擅长 segmentation/tracking
  却不理解开放语言；把两者作为外部 tools 串联会丢失 end-to-end grounding signal。
- **Why the Previous Design Was Reasonable:** 专用 segmentation 与 chat model 分离时，每个模块可独立升级、
  性能边界清晰，也避免 dense mask tokens 污染 LLM context。
- **Changed Constraint:** interactive video 任务要求同一输入同时产生文本、mask/masklet、visual-prompt answer，
  并在遮挡和长文本下保持 object identity。
- **Mechanism:** image/video/prompt 映射为 LLM tokens；LLM 输出文本与特殊 `[SEG]` hidden state；该 state
  作为 SAM-2 decoder prompt 生成 mask。关键帧 mask 写入 SAM-2 memory，跟踪其余帧；SAM-2 memory/decoder
  与 MLLM 解耦，训练时只让 SEG bridge 回传 grounding signal。
- **State Ownership:** LLM 拥有语义选择，`[SEG]` 是跨模块引用；SAM-2 拥有像素 mask 与 tracking memory；
  object identity 若在文本、SEG 和 memory 间错配，没有单一组件能自动纠正。
- **Control Flow / Data Flow:** text/image/video/visual prompt → MLLM → text + SEG → SAM-2 key-frame mask →
  tracking memory → masklets；chat-only 路径不调用 mask output。
- **Implementation Details:** XTuner，LoRA fine-tune LLM，perception model 冻结，最大 8,192 tokens；8×A800-80GB
  训练约 48 小时；Ref-SAV 自动标注超过 72k expressions，并人工核验约 2k objects 作为 benchmark。
- **Evaluation Setup:** image/video referring segmentation、image/video chat、grounded caption 与 visual-prompt
  tasks；多尺寸模型与公开 baselines；结果是作者实验。
- **Baselines / Ablations / Sensitivity / Overhead:** 数据类型 removal、single/repeat/multiple SEG token、模型/
  数据 scale；VQA 数据增加可能损害 segmentation，证明 multi-task balance 不是免费收益。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** GPU、80GB、训练时间、8,192 context
  与 LoRA 披露；precision、batch、视频长度分布、在线 concurrency/latency/SLO 不完整。
- **What the Evidence Actually Proves:** 在作者任务合同中，一个语义 token bridge 可连接开放语言选择与冻结的
  dense tracker，并通过 joint training 保留多任务能力。
- **What It Does Not Prove:** 不证明 `[SEG]` 足以承载任意对象关系，不证明长视频在线跟踪可靠，也不证明
  joint model 优于所有模块化 tool pipeline。
- **Limitations / Threats to Validity:** 作者明确报告长视频/复杂指代表达、遮挡、camera motion、在线模式
  不见全局内容，以及 VQA/segmentation 数据冲突；自动 annotation 还依赖大模型一致性检查。
- **Trade-offs / New Failure Modes:** token bridge 降低跨模块通信，但压缩 object identity；冻结 SAM-2 保留
  tracking prior，却限制端到端适配；joint training 引入 negative transfer、SEG omission/repetition 与 stale memory。
- **Where the Previous Design Still Applies:** 高风险像素任务、需独立校准或 specialist 可替换时，模块化
  MLLM→explicit tool call→segmenter 更可审计。
- **Evolution Relationship:** `Layering / Dependency`：open-ended semantic proposal → SEG reference → specialist
  dense state；不是把 segmentation 完全内化到 LLM。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；Ch26 接 perception-to-action，
  `AGENT-TOOL-CALLING`（Ch78）接模块化替代分支。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 与 Ch78 的 representation、state identity、physical
  handoff 与 tool boundary。
- **Existing Coverage:** Ch23 已覆盖 modality/reference identity；Books 阶段再判断是否需要 SEG bridge 案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** long-video object identity 如何 version/rollback；何时应共享 token，何时应暴露明确的
  segmentation tool contract。

### MotionBench

- **Candidate / Week / Score:** MotionBench / 2025-W02 / 26/30。
- **Source Family ID:** `motionbench-fine-grained-video-motion`。
- **Source Type:** arXiv primary benchmark/architecture paper + official dataset/code。
- **First-public Date / Revision History:** arXiv v1 2025-01-06；CVPR 2025 version 是后续 publication node。
- **Direct Primary Sources:** arXiv v1 PDF，https://arxiv.org/pdf/2501.02955v1；official repository
  https://github.com/zai-org/MotionBench。
- **Related Primary Sources:** CVF accepted paper用于 publication metadata，不改写 event-time v1。
- **Access and Verification Status:** Verified；arXiv HTML 当前错误显示无关 LaTeX 页面，故以同 ID v1 PDF、
  abs metadata 与 official repository 三方核验，身份冲突已显式记录。
- **Full-read Coverage:** benchmark taxonomy/curation/annotation、model comparison、compression families、TE Fusion、
  high-frame-rate/data experiments、ablation、appendix、limitations 与 artifact instructions。
- **Original Problem:** 通用 video benchmarks 偏 event/story-level，平均稀疏采样会直接丢失瞬时动作、顺序、
  次数和相对位置；而增加帧数又超过 LLM sequence 与 memory budget。
- **Why the Previous Design Was Reasonable:** uniform sparse sampling 和 pre/post-encoder pooling 实现简单，能在
  固定 token budget 下复用 image VLM，对慢变化或故事级问题仍有效。
- **Changed Constraint:** motion-level perception 要高 frame rate；浅层 compression 在 frame 独立编码之后才
  融合，已丢失跨帧高层对应关系。
- **Mechanism:** MotionBench 以 5,385 videos/8,052 multiple-choice questions 覆盖六类 motion tasks；TE Fusion
  将相邻 k 帧在 visual encoder 各层进行 group self-attention，再做 spatial-temporal compression，使固定 decoder
  token budget 内保留更深的 temporal relation。
- **State Ownership:** dataset item 拥有 video/question/answer；visual encoder 拥有 frame-group temporal state；
  decoder 只看到压缩 tokens。answer distribution、source license 和 hidden test server 属于 evaluator contract。
- **Control Flow / Data Flow:** dense frames → grouped through-encoder fusion → compressed video tokens → LLM →
  answer；benchmark dev/test 与 leaderboard 分离。
- **Implementation Details:** 比较 pre-encoder、post-encoder、QFormer、adaptive pooling、patchification 与 TE；
  公平 architecture study 使用 224×224、10k iterations、global batch 768、相同 open-source data。
- **Evaluation Setup:** 多个 proprietary/open VLM，MotionBench dev/test 六类 accuracy，并联读 MVBench、LVBench、
  VideoMME；另发布 5k fine-grained motion description videos。具体训练 GPU 未披露。
- **Baselines / Ablations / Sensitivity / Overhead:** compression family、frame rate、compression ratio、training
  data 与 benchmark cross-check；作者仍观察多数模型低于实用阈值，高 frame rate 并未消除理解缺口。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** resolution、iterations、global batch 与
  frame settings部分披露；GPU、precision、token length、serving concurrency/latency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** motion-level QA 是被通用 benchmark 稀释的独立 evaluation contract；
  在作者受控训练中，把 temporal fusion 前移/贯穿 encoder 比浅层压缩更能承受高 compression ratio。
- **What It Does Not Prove:** 不证明 TE 对所有视频任务最优，不证明 multiple-choice accuracy 等于真实环境
  motion understanding，也不证明高 frame rate 可在生产成本内实现。
- **Limitations / Threats to Validity:** 作者承认 geographic/cultural/context bias；MCQ 有 option/guessing bias，
  web/synthetic/public sources分布与真实部署不同；HTML mismatch 需要 archive tooling fallback。
- **Trade-offs / New Failure Modes:** 更深 temporal fusion 保留 motion，却增加 encoder compute、组边界、
  long-range aliasing 与实现复杂度；更高 frame rate 提升观测机会，也挤压空间分辨率和 LLM token budget。
- **Where the Previous Design Still Applies:** 慢变化、低成本、story-level summarization 或硬件受限时，稀疏采样
  与浅层 pooling 仍合理；关键是 workload contract，不是单向替代。
- **Evolution Relationship:** `Direct Evolution`：sparse frames → shallow compression → through-encoder temporal
  fusion；与长视频 memory 是 layering，不是同一问题。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；`PLATFORM-EVALUATION-SYSTEM`（Ch66）
  接 benchmark contract，`INFER-PREFILL`（Ch43）接 token/compute cost。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～24、Ch43 与 Ch66 的 representation、generation、prefill
  与 evidence boundary。
- **Existing Coverage:** Ch23 已有 temporal aliasing/rate-distortion；Books 阶段判断是否需要“fusion depth”分支。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；记录并绕过 arXiv HTML 身份异常。
- **Open Questions:** 如何把 motion MCQ 升级为 executable/causal evaluation；encoder fusion 的质量收益是否能
  抵消 production TTFT 与 memory cost。

### PPTAgent

- **Candidate / Week / Score:** PPTAgent / 2025-W02 / 25/30。
- **Source Family ID:** `pptagent-edit-based-artifact-workflow`。
- **Source Type:** arXiv primary Agent/workflow/evaluation paper + official code/data。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 artifact/revision 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.03936v1。
- **Related Primary Sources:** official Agent/PPTEval code 与 Zenodo10K data用于 artifact contract。
- **Access and Verification Status:** Verified；method、experiments、human agreement、prompts/API appendix 与
  limitations 可读。
- **Full-read Coverage:** problem formulation、reference analysis、slide clustering/schema、outline-to-slide mapping、
  executable edit actions、REPL correction、PPTEval、500-presentation configurations、ablation 与 limitations。
- **Original Problem:** text-to-slide 从空白 canvas 逐元素生成，既要发明内容又要解决空间/style 约束，常产生
  无法执行、布局冲突和跨页不连贯。
- **Why the Previous Design Was Reasonable:** 从零生成不依赖 reference license/compatibility，适合简单模板或
  独特视觉；单页生成也易并行。
- **Changed Constraint:** deck 是跨页 artifact；布局、功能角色和 content schema 需要继承，单页局部最优不能
  保证全局 coherence。
- **Mechanism:** Stage I 按功能/视觉相似度聚类 reference slides，抽取 layout/content schema；Stage II 先生成
  deck outline，把 source sections 和 reference slide 分配给每页，再输出 executable edit actions 修改 reference；
  REPL error feedback 最多两轮修正。PPTEval 分 content/design/coherence。
- **State Ownership:** reference deck 拥有 style/layout prior；outline 拥有 deck-level content allocation；每页
  edit program 拥有变更；renderer/REPL 拥有 executable correctness；evaluator score 不拥有设计真值。
- **Control Flow / Data Flow:** source document + reference deck → clusters/schemas → outline → slide assignment →
  code actions → render/error → bounded correction → deck → multi-dimensional evaluation。
- **Implementation Details:** hierarchical clustering threshold 0.65；HTML/API representation；实验每配置
  5 domains×10 docs×10 references，最多两轮 correction；open models 用 vLLM 部署在 8×A100，总约 500 GPU-hours。
- **Evaluation Setup:** 12～64 slides、source text 2,048～20,480 chars；模型/方法比较、success、Content/Design/
  Coherence；4 名研究生对真实与生成 decks 打分，LLM-human correlation 在 coherence 上较弱。
- **Baselines / Ablations / Sensitivity / Overhead:** 去 outline/structural info/schema、比较模型与 correction
  iterations；没有覆盖强交互、动画、复杂 nested shapes 或 production editing latency。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A100 与总 GPU-hours、文档/页数范围
  披露；precision、batch/concurrency、单 deck latency/SLO 不完整。
- **What the Evidence Actually Proves:** 对结构化 presentation workload，复用 reference artifact 并生成
  bounded executable edits，比从零逐元素生成更容易保持 layout/coherence，并能把失败暴露给 renderer。
- **What It Does Not Prove:** 不证明 LLM evaluator 能替代设计评审，不证明 95% success 足以生产，也不证明
  reference style 的授权、可访问性与兼容性已解决。
- **Limitations / Threats to Validity:** 作者报告 nested group parsing、overlap、style inconsistency 和非绝对
  success；human sample有限，coherence correlation 低于 design，模型评审可能偏视觉表面。
- **Trade-offs / New Failure Modes:** edit-based workflow降低生成自由度与空间搜索，却引入 reference selection、
  schema extraction、license/provenance、stale layout 和 executable action side effects。
- **Where the Previous Design Still Applies:** 没有合适 reference、需要原创 visual language 或简单一页 artifact
  时，从零模板生成仍合理。
- **Evolution Relationship:** `Direct Evolution`：text-to-elements → reference/schema planning → executable edits →
  render feedback；与 general workflow 是 principle reuse。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；Ch78 接 executable tool contract，Ch66 接 artifact
  evaluation，Ch80 接 bounded correction。
- **Target and Adjacent Chapters Read:** 已核对 Ch78～81 与 Ch66 的 proposal/action/evidence/workflow 边界。
- **Existing Coverage:** Books 已覆盖 artifact-producing workflow；Books 阶段只在存在长期机制缺口时 refine。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** reference deck provenance/compatibility 如何版本化；如何用 renderer invariants、human gate 与
  content factuality共同形成 release contract。

### Diffusion as Shader

- **Candidate / Week / Score:** Diffusion as Shader / 2025-W02 / 24/30。
- **Source Family ID:** `diffusion-as-shader-3d-tracking-control`。
- **Source Type:** arXiv primary generative-model paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 revision 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.03847v1。
- **Related Primary Sources:** CogVideoX、SpatialTracker、Depth Pro/MoGE、SAM/FLUX 是 pipeline dependencies。
- **Access and Verification Status:** Verified；method、training、five tasks、ablation、runtime 与 failure cases 可读。
- **Full-read Coverage:** 3D tracking representation、condition DiT injection、real/synthetic data、object/camera/
  mesh/motion control、baselines、depth-vs-tracking、point density、runtime、limitations。
- **Original Problem:** camera embeddings 或逐帧 depth 只描述局部结构，不能显式关联同一 3D point 跨帧身份，
  diffusion model 必须自己推断 motion correspondence。
- **Why the Previous Design Was Reasonable:** depth/ray/camera condition 生成便宜、接口紧凑；静态场景或简单
  camera path 下足以提供几何方向。
- **Changed Constraint:** object motion、遮挡重现、motion transfer 与 manipulation 需要跨帧一致的 3D identity，
  同时又要复用已有 I2V diffusion prior。
- **Mechanism:** 将首帧坐标归一化为稳定 RGB，渲染随时间移动的 colored 3D points 形成 tracking video；
  VAE 编码后送入复制自前 18/42 blocks 的 condition DiT，经 zero-initialized linear 注入冻结的 CogVideoX
  denoiser，类似 ControlNet 的附加条件路径。
- **State Ownership:** tracker/mesh/camera pipeline 拥有 3D point identity；condition DiT 只消费该控制状态；
  diffusion generator 拥有像素 proposal，不拥有真实物理状态。
- **Control Flow / Data Flow:** image + mesh/depth/video tracker → 3D tracking video → VAE latent → condition DiT
  → frozen denoising DiT (50-step DDIM) → VAE decode → video。
- **Implementation Details:** real MiraData + Mixamo synthetic，少于 10k videos，49 frames、720×480；4,900 points；
  AdamW lr 1e-4、2,000 steps、effective batch 64；8×H800 训练 3 天。
- **Evaluation Setup:** camera control、motion transfer、mesh-to-video、object manipulation 等；MotionCtrl/
  CameraCtrl baselines；DAVIS/MiraData 50-video validation，PSNR/SSIM/LPIPS/FVD 与 human/qualitative comparisons。
- **Baselines / Ablations / Sensitivity / Overhead:** depth condition vs 3D tracking、900～8,100 points；4,900
  是质量/追踪成本折中。单 H800、480×720、49 frames、50 DDIM steps 约 2.5 分钟。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H800 数量、分辨率、frames、steps、
  batch 与 runtime 披露；precision、concurrency 与 interactive SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数据/任务中，带跨帧 point identity 的 tracking condition 比逐帧
  depth 更能保持受控视频一致性，并可通过小规模 adapter-like condition branch 复用 base diffusion model。
- **What It Does Not Prove:** 不证明生成满足真实动力学或 causal control，不证明单目 depth/tracker error 可容忍，
  也不适合实时闭环。
- **Limitations / Threats to Validity:** input image 与 tracking geometry 不兼容会触发 scene transition；无 point
  区域不可控；高质量 control 依赖现有 video/animated mesh、depth 和 tracker，pipeline error 可级联。
- **Trade-offs / New Failure Modes:** 显式 3D identity换 temporal control，却增加 tracking/geometry preparation、
  condition storage 和 50-step latency；冻结 base 保留 prior，却限制纠正结构冲突。
- **Where the Previous Design Still Applies:** 简单 camera motion、无需 object identity 或低准备成本时，ray/depth
  condition 更轻；真实 closed-loop control 应使用 simulator/sensor state，而非生成视频。
- **Evolution Relationship:** `Alternative Branch`：compact camera/depth condition ↔ explicit 3D tracking video；
  后者用更重状态换跨帧 identity。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；Ch25 接 world-model boundary，
  Ch26 接 physical control non-equivalence。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 的 representation、generation、world state 与 action 边界。
- **Existing Coverage:** Ch24 已覆盖 iterative correction/cache/rollback；Books 阶段再判断是否需要 3D condition
  identity 分支。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02。
- **Open Questions:** tracking uncertainty 如何传入 diffusion；condition/source/base-model 版本如何共同决定可复现
  artifact identity；何时视觉控制证据足以升级为 world-model claim。

### OpenOmni

- **Candidate / Week / Score:** OpenOmni / 2025-W02 / 25/30。
- **Source Family ID:** `openomni-language-pivot-speech-output`。
- **Source Type:** arXiv primary multimodal model/training paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续 revision/artifact 属于同一 family，不改写 event date。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04561v1。
- **Related Primary Sources:** O2S-300K、EO2S-9K 与所用 speech/image encoders 只作为数据和依赖边界；本 packet
  不用后续模型介绍反推 v1 实现。
- **Access and Verification Status:** Verified；method、五个训练 sub-stages、数据、超参数、multimodal/speech/
  emotion evaluation 与 appendix 可读。
- **Full-read Coverage:** architecture、language-pivot alignment、AR/NAR speech generation、CTC、DEPO、数据构造、
  implementation tables、benchmark、ablation/案例、conclusion 与 appendix。
- **Original Problem:** 原生 image-text-speech 三模态配对稀缺；串联 ASR/LLM/TTS 又会把语义、音色和情感状态
  切成不可联合优化的多个接口。
- **Why the Previous Design Was Reasonable:** 模块化 ASR/TTS 数据充足、可独立校准和替换；两模态 alignment 也
  避免昂贵的全组合数据，是可靠性优先场景的合理方案。
- **Changed Constraint:** 交互式 omnimodal 模型希望在同一对话状态中并行产生 text/speech，并用少量 tri-modal
  数据连接 image、speech 与 language，而不是为每个模态对收集大规模配对。
- **Mechanism:** speech/image encoder 分阶段对齐同一 LLM representation，以 language 作为 pivot；speech decoder
  采用 MoE 与小型 decoder-only 网络，可走 AR 或 CTC-based NAR discrete-unit 路径；DEPO 用 context-congruent
  与 neutral speech-unit preference pair 更新 policy，reference 固定为前一阶段模型。
- **State Ownership:** LLM hidden state 拥有共享语义 proposal；speech decoder/CTC 拥有 unit alignment；vocoder
  拥有 waveform realization；emotion label/preference 只定义训练偏好，不拥有真实用户情绪。
- **Control Flow / Data Flow:** image/audio/text → modality encoder → shared LLM → text token 与 speech branch 并行
  → AR 或 NAR unit sequence → vocoder；DEPO 只更新 speech policy branch。
- **Implementation Details:** 五个阶段分别控制 LLM freeze；公开 batch、learning rate、warmup 与 epoch；speech-text
  alignment 使用公开语料和约 1,600 小时 O2S 子集，image-text 使用 LLaVA-Pretrain/MMEvol，最终模型为 7B。
- **Evaluation Setup:** OmniBench、visual-language benchmarks、AIShell-2/LibriSpeech recognition/synthesis 与
  EO2S-9K bilingual emotion classification；全部是作者报告。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 omnimodal/VLM/speech models，并报告 DPO 前后情感分类；
  没有完整拆分 language-pivot、少量 tri-modal data、AR/NAR branch 的独立贡献或端到端 latency sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B、各阶段 batch/lr/epoch 与数据规模披露；
  hardware、precision、streaming chunk、first-audio latency、concurrency、RTF 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数据和 evaluator 下，分阶段的 language-pivot alignment 能把多种
  input/output 接到同一 LLM，并且 speech-unit preference optimization 改变其情感分类结果。
- **What It Does Not Prove:** 不证明不同模态已形成完全共享的因果语义空间；不证明“self-aware”或真实 empathy；
  没有 workload contract 时也不证明 production real-time。
- **Limitations / Threats to Validity:** 大量 speech 来自 synthesis，继承 TTS/teacher bias；emotion preference
  将复杂语境压成九类并以 neutral 为 loser；benchmark 与训练数据存在 domain/evaluator dependence。
- **Trade-offs / New Failure Modes:** language pivot 降低配对数据需求，却可能形成 language bottleneck；NAR CTC
  提高并行性，却弱化自回归 prosody control；并行 text/speech 还会引入两路内容不一致与 vocoder failure。
- **Where the Previous Design Still Applies:** 高风险语音、需逐模块审计、低资源语言或精确 prosody control 时，
  ASR→LLM→TTS/AR pipeline 仍更易校准和回滚。
- **Evolution Relationship:** `Layering / Dependency`：双模态 alignment → language pivot → 少量 tri-modal bridge →
  parallel speech output → preference-shaped expression；不是用统一模型静默替代模块化链路。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；Ch24 接 generation branch，`TRAIN-DPO`
  （Ch34）接 preference optimization，Ch42～44 接 streaming inference contract。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～24、Ch31～34 与 Ch42～45 的 representation、generation、
  preference 与 request-state 边界。
- **Existing Coverage:** Books 已有 modality identity、preference evidence 与 streaming contract；是否加入 language
  pivot/NAR speech 受限案例留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；标题中的 real-time/self-aware 不作为独立事实写入长期结论。
- **Open Questions:** language bottleneck 对非语言声学信息的损失如何测量；text/speech divergence 如何检测；
  chunk-level latency、cancel/rollback 与 emotion preference provenance 如何进入 deployment contract。

### Dolphin

- **Candidate / Week / Score:** Dolphin / 2025-W02 / 24/30。
- **Source Family ID:** `dolphin-closed-loop-auto-research`。
- **Source Type:** arXiv primary Agent/workflow paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 revision/artifact 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.03916v1。
- **Related Primary Sources:** supplementary prompts、Aider/Ollama 与任务 baseline 只用于实现/任务 contract。
- **Access and Verification Status:** Verified；methods、实验设置、两轮 closed loop、idea/cost analysis、cases 与
  supplementary material 可读。
- **Full-read Coverage:** retrieval/task-attribute idea generation、independence/novelty filtering、plan/code/debug、
  result feedback、CIFAR-100/ModelNet40/SST-2 evaluation、ablation/cost、prompts 与 cases。
- **Original Problem:** one-shot research Agent 可以产生想法或论文，但实验结果不回流，失败想法会重复出现，
  “新颖”文本也不等于可执行且有效的假设。
- **Why the Previous Design Was Reasonable:** 单轮 idea generation 成本低、易人工审阅；scope-limited AutoML 在
  固定搜索空间里更易比较，也避免开放式代码执行的状态和安全复杂度。
- **Changed Constraint:** 目标扩展为开放式实验时，需要把 retrieval、idea、implementation、execution 与
  observed result 连接成可迭代 workflow，而不是只产出自然语言 proposal。
- **Mechanism:** 从 50 篇候选中按 task attribute/score 过滤文献，生成每轮 20 个 ideas；用 embedding 做
  independence filtering；生成实验计划与代码，最多五次 error-traceback debugging；成功/失败摘要写入
  experience bank，并把有效想法反馈给下一轮 prompt。
- **State Ownership:** literature store 拥有来源；idea bank 拥有 proposal/相似度；sandbox 拥有 executable outcome；
  benchmark metric 拥有局部反馈；LLM summary 只是 derived memory，不能替代原始 log/artifact。
- **Control Flow / Data Flow:** task → paper retrieval/filter → idea batch → plan/code → bounded debug → experiment
  result → analysis/experience bank → next-loop generation；失败执行不会自动成为科学反证。
- **Implementation Details:** idea/feedback 使用 gpt-4o-2024-08-06；code agent 为通过 Ollama 部署的 DeepSeek-v2.5；
  20 ideas/loop、两个 loops、independence threshold 0.8、最多五次 debugging。
- **Evaluation Setup:** CIFAR-100/WRN-28-10、ModelNet40/PointNet、SST-2/BERT-base；以能提高复现 baseline 的
  ideas 数、平均/最大 accuracy improvement、idea novelty 与调用成本评估。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 naive、naive retrieval 与 task-attribute filtering；每项任务
  40 ideas，仅 5～6 个提高 baseline；缺少独立 held-out search budget、multiple-testing correction 与长期复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** agent 模型、retrieval/loop/debug 配置披露；
  training hardware、precision、各实验 batch、并发、wall-clock 与 workflow SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在三个受限 ML task 和作者预算下，实验结果回流能形成可执行的两轮
  research workflow，并筛出少量提高复现 baseline 的 modifications。
- **What It Does Not Prove:** 不证明 ideas 具有科学新颖性、能跨数据集泛化或优于专家研究；accuracy 搜索也
  不证明机制解释成立。
- **Limitations / Threats to Validity:** idea novelty 依赖 LLM judge；同一 benchmark 同时指导搜索和报告收益，
  存在 multiple-comparison、validation overfitting 与 success-only selection；只有两个 loops/三个任务。
- **Trade-offs / New Failure Modes:** feedback 减少重复失败并提高局部适应，却可把 evaluator bias、数据泄漏和
  spurious gain 固化进 memory；开放代码执行还增加 supply-chain、resource runaway 与 artifact provenance 风险。
- **Where the Previous Design Still Applies:** 搜索空间清晰、预算严格或结论高风险时，人工 gate、预注册实验与
  scope-limited AutoML 更可审计；one-shot proposal 也适合只需 brainstorming 的阶段。
- **Evolution Relationship:** `Direct Evolution`：one-shot idea → retrieval/filter → executable experiment → feedback
  memory → next iteration；科学验证仍需外部 held-out/human gate。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；Ch77 接 derived memory，Ch79/80 接 planning/reflection，
  Ch66 接 evaluation contract。
- **Target and Adjacent Chapters Read:** 已核对 Ch66 与 Ch77～82 的 evidence、memory、planning、reflection、
  workflow 与 multi-agent 边界。
- **Existing Coverage:** Books 已覆盖 artifact-producing workflow 和 evidence gate；是否加入“benchmark feedback
  can overfit the research loop”这一机制缺口留待 Books 阶段。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；论文提升数字不外推为自治科学发现能力。
- **Open Questions:** 如何把 train/validation/held-out research budget 分离；失败实验、环境版本和负结果如何保留；
  哪个 verifier 可以阻止 workflow 持续优化 evaluator 而非科学问题。

### Segmenting Text and Learning Their Rewards

- **Candidate / Week / Score:** Segmenting Text and Learning Their Rewards / 2025-W02 / 26/30。
- **Source Family ID:** `segment-level-reward-rlhf`。
- **Source Type:** arXiv primary RLHF/reward-model paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-06；后续 revision 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.02790v1。
- **Related Primary Sources:** Phi-3/Llama-3 checkpoints 与 AlpacaEval/Arena-Hard/MT-Bench 只定义 backbone 和
  evaluator contract。
- **Access and Verification Status:** Verified；method、公式、training/evaluation、ablation、sensitivity、appendix
  与明确 limitations 可读。
- **Full-read Coverage:** sequence/token reward background、entropy segmentation、Bradley–Terry objective、
  location-aware normalization、interpolation、PPO、hybrid ablations、cutoff sensitivity、conclusion/limitations。
- **Original Problem:** sequence-level reward 只在终局给 credit，token-level reward 又把语义不完整的 token 当作
  action；二者分别造成 credit 稀疏和 attribution 不稳定。
- **Why the Previous Design Was Reasonable:** binary sequence preference 易采集且直接对应用户选择；token-level
  reward 提供最密信号，在短回复或局部错误可独立标注时仍有效。
- **Changed Constraint:** 长回复的质量由语义片段共同形成，只有 sequence preference label，却希望 PPO 得到
  比终局更密、又不把 token 过度解释为独立 action 的反馈。
- **Mechanism:** 用 SFT policy 在 token 位置的 Shannon entropy 超阈值处切 segment；segment reward 经总和后
  用 Bradley–Terry sequence preference loss 训练；on-policy segment 的位置/长度分布用 location-aware function
  归一化；segment reward 按长度均分插值到 token 后供 PPO。
- **State Ownership:** SFT policy entropy 定义边界 proposal；reward model 拥有 learned segment score；preference
  pair 只约束总排序，不能唯一决定每段真值；PPO rollout 拥有 on-policy segment distribution。
- **Control Flow / Data Flow:** preference sequences → entropy boundaries → segment scores/sum → pairwise loss →
  reward model；policy rollout → dynamic segments → position normalization/interpolation → PPO update。
- **Implementation Details:** 以 Phi-3-mini 3.8B 与 Llama-3 8B 系列 policy/reward variants 验证；主 cutoff 1.75，
  比较 1.5～2.25；较有效设置平均 10～22 tokens（约 3～7 words）一段。
- **Evaluation Setup:** free-form dialog-like preference data；PPO 后在 AlpacaEval 2、Arena-Hard、MT-Bench 等
  instruction-following benchmark 评估；含 model-judge 指标，均为作者实验。
- **Baselines / Ablations / Sensitivity / Overhead:** bandit/sequence、sentence、token、segment 及混合 reward；
  比较 normalization、no/repeat/even-split interpolation 和 entropy cutoff；未披露完整 training overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** backbone 与 cutoff/segment length 披露；
  GPU、precision、batch、rollout concurrency、端到端训练成本/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者的 dialog/PPO/evaluator contract 内，语义片段粒度、位置归一化和
  even-split credit 比若干 sequence/token baselines 产生更好的 benchmark 结果，并存在可见 cutoff sensitivity。
- **What It Does Not Prove:** 不证明 segment score 是因果 credit 或人类真实局部偏好；不证明可扩展到 math/code、
  更大模型或 PPO 之外算法，也不证明 judge preference 没有 style/length bias。
- **Limitations / Threats to Validity:** 作者明确限制在 free-form dialog、instruction benchmarks 与 PPO；边界依赖
  SFT policy/domain，policy 更新又会改变 on-policy distribution；sequence label 对 segment decomposition 欠定。
- **Trade-offs / New Failure Modes:** segment-level 信号在稀疏与过细之间折中，却引入 boundary drift、位置归一化
  偏差和 reward hacking；过短段失去语义，repeat reward 又会过罚长回复，zero-padding 可稀释负段。
- **Where the Previous Design Still Applies:** 终局可精确验证的 math/code 可保留 outcome reward；可获得真实局部
  标注且错误局部独立时 token/sentence reward 更直接；短回复无需额外 segmentation complexity。
- **Evolution Relationship:** `Alternative Branch`：sequence reward ↔ token reward → entropy-defined semantic segment；
  它是在 credit granularity 上取条件分支，不宣称统一替代。
- **ROADMAP Node:** `TRAIN-PPO`（Ch32）主 owner；`TRAIN-RLHF`（Ch31）接 preference underdetermination，
  `TRAIN-GRPO`（Ch33）接 group/outcome alternative。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～34 的 SFT、preference、reward、PPO/GRPO/DPO 分工。
- **Existing Coverage:** Books 已有 reward/evidence 非等价与算法分支；是否补入“action granularity 也是 RLHF
  system contract”留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把作者 judge benchmark 写成普适 RLHF 优势。
- **Open Questions:** segmentation policy 与 online policy 漂移如何 version；如何用 human segment annotations
  校准 learned decomposition；math/code 的 executable verifier 应怎样与 segment reward 组合。

### Modern GAN Baseline

- **Candidate / Week / Score:** The GAN is dead; long live the GAN! A Modern Baseline GAN / 2025-W02 / 22/30。
- **Source Family ID:** `r3gan-modern-adversarial-baseline`。
- **Source Type:** arXiv primary generative-model/architecture paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 revision 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05441v1。
- **Related Primary Sources:** StyleGAN2、RpGAN/R1/R2、modern ResNet 与 diffusion baselines 只用于演进/比较。
- **Access and Verification Status:** Verified；roadmap configs、theory/method、implementation、datasets、FID/recall、
  compute、ablation、discussion 与 limitations 可读。
- **Full-read Coverage:** Config A→E removal/rebuild、relativistic loss/regularization、symmetric residual architecture、
  grouped convolution/init、FFHQ/CIFAR/ImageNet/Stacked-MNIST experiments、recall、compute 与 appendices。
- **Original Problem:** 经典 GAN baseline 混入 mapping/style/noise、equalized learning rate、lazy regularization 等
  历史技巧，使研究者难区分 adversarial objective 的边界与旧 backbone/optimization technical debt。
- **Why the Previous Design Was Reasonable:** StyleGAN2 技巧在当时解决训练不稳、perceptual control 和高分辨率
  质量问题；diffusion 后来以更稳定训练和 coverage 成为更易扩展的默认生成分支。
- **Changed Constraint:** 现代 residual architecture、normalization/initialization 与 optimizer practice 改变后，应先
  建立无预训练 feature leakage 的简洁强 baseline，再判断 GAN 是否因 objective 本身失去价值。
- **Mechanism:** Config B 移除 StyleGAN-specific components；Config C 使用 well-behaved relativistic paired GAN
  与 R1/R2 gradient penalties；Config D 改为 generator/discriminator 对称 ResNet；Config E 加 inverted bottleneck、
  grouped convolution 与 fix-up-style initialization，形成 R3GAN。
- **State Ownership:** generator 拥有 one-step sample proposal；discriminator/regularizer 拥有相对 real/fake training
  signal；FID feature space 只是 evaluator，不能拥有 perceptual fidelity 或 coverage 真值。
- **Control Flow / Data Flow:** noise/label → one generator evaluation → image；real/fake pair → discriminator relative
  score + gradient penalties → alternating G/D updates。
- **Implementation Details:** FFHQ roadmap 的 G/D 约各 25M；identity mapping、transition layer、1×1–3×3–1×1
  residual blocks，group size 16；不同数据集调节容量和训练 schedule。
- **Evaluation Setup:** Stacked MNIST、CIFAR-10、FFHQ-256、ImageNet-32/64；比较 modern GAN/diffusion，以
  FID-50K、recall、NFE、参数与训练成本报告结果。
- **Baselines / Ablations / Sensitivity / Overhead:** A→E 逐步 ablation、regularization/architecture/init 分析；作者
  报告 recall 通常接近或略低于 diffusion，且一阶生成不等于端到端服务延迟最优。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 部分实验使用 8×L40、8×A6000，
  ImageNet 使用 A100/H100，并披露天/小时级成本；precision、完整 batch、serving concurrency/SLO 不完整。
- **What the Evidence Actually Proves:** 在作者数据与 tuning budget 下，移除历史耦合并采用稳定 adversarial
  objective/现代 backbone 后，GAN 仍可得到有竞争力的 FID，并保留 one-NFE sampling 特性。
- **What It Does Not Prove:** 不证明 GAN 普遍优于或会替代 diffusion；FID 优势不等同 human preference、mode
  coverage 或可控性，也不能从 image benchmark 外推到 text/video。
- **Limitations / Threats to Validity:** FID 可受 evaluator feature leakage 与有限 sample bias 影响；各方法 training
  compute/tuning 不是完全等价；高分辨率/大规模数据、conditioning 和真实 deployment 未充分覆盖。
- **Trade-offs / New Failure Modes:** one-step sampling 降低 NFE/latency，却保留 adversarial instability、mode drop、
  discriminator overfit 与 alternating-state complexity；diffusion 以多步 compute 换更平滑的 optimization/correction。
- **Where the Previous Design Still Applies:** diffusion 在 coverage、可编辑/迭代 correction、复杂 conditioning 或
  稳定 scaling 优先时仍合理；GAN 在严格 sampling latency 与受控 image domain 下可作为条件分支。
- **Evolution Relationship:** `Alternative Branch`：旧 GAN tricks → minimalist failure → stable objective + modern
  backbone；与 diffusion 是并存的 latency/coverage trade-off，不是时间顺序替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；Ch28 接 training objective，Ch49
  接 execution-plan/NFE boundary。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch27～29 与 Ch48～50 的 generation、training 与
  execution boundary。
- **Existing Coverage:** Ch24 已保留 AR/diffusion/masked/block branches；Books 阶段再判断是否需要补 adversarial
  one-step branch，不能仅凭 FID 追加产品式案例。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不采纳“GAN 已复活/取代 diffusion”的标题式结论。
- **Open Questions:** 在相同训练 compute/human evaluation 下 quality/coverage 如何变化；one-NFE 优势在 VAE、
  transport、batching 后是否仍主导端到端 SLO；高分辨率与多模态 conditioning 是否稳定。

### GeAR / Generation Augmented Retrieval

- **Candidate / Week / Score:** GeAR / Generation Augmented Retrieval / 2025-W02 / 26/30。
- **Source Family ID:** `gear-generation-augmented-retrieval`。
- **Source Type:** arXiv primary retrieval/model paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-06；后续 revision/artifact 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.02772v1。
- **Related Primary Sources:** event-time paper承诺 code/data/model 经 review 后发布；后续 artifact 只用于复现，
  不倒推 v1 已公开实现。
- **Access and Verification Status:** Verified；method、objectives、inference modes、datasets、training、comparisons、
  analysis、appendix 与 limitations 可读。
- **Full-read Coverage:** bi-encoder/fusion/decoder、synthetic triples、CL+LM loss、retrieval/localization/generation、
  QA/RIR evaluations、ablation、hyperparameters、data construction 与 limitations。
- **Original Problem:** bi-encoder 把 query-document 关系压成一个 scalar similarity，适合大规模召回，却无法解释
  文档内哪段证据负责匹配；预切细 chunk 又增加索引/编码成本并破坏上下文。
- **Why the Previous Design Was Reasonable:** 独立编码使 document embedding 可离线缓存，ANN retrieval 可扩展；
  对短 passage 或只需 top-k 的场景，scalar similarity 是成本最低的充分接口。
- **Changed Constraint:** RAG/citation/long-document retrieval 同时需要 corpus-scale recall 与 query-specific
  evidence localization，希望训练 retrieval representation 时就保留细粒度关系。
- **Mechanism:** 以 `(query, document, relevant unit)` triples 训练；共享参数的 query/fusion encoder 在每层以
  cross-attention 融合 document，causal decoder 生成相关 unit；bi-encoder 用 contrastive loss，decoder 用 LM
  loss。部署时只召回可仍走 bi-encoder，localization/generation 才启用较重分支。
- **State Ownership:** corpus index 拥有可缓存 document embedding；fusion attention 拥有 query-conditioned
  token weights；decoder output 是 evidence proposal，不是原文身份或 citation truth。
- **Control Flow / Data Flow:** offline document encoding/index → query bi-encoding/ANN → optional selected-document
  fusion → attention localization/AR generation → downstream RAG；training 额外走 CL+LM dual objective。
- **Implementation Details:** BERT-base initialization；PAQ 采样 30M，RIR 合成/去重/过滤 5.8M triples；10 epochs，
  batch 48/16，AdamW，16×AMD MI200-64GB；context 上限 512 tokens。
- **Evaluation Setup:** PAQ、SQuAD、NQ、TriviaQA 与 synthetic RIR；document retrieval、unit localization、generation
  分别用 recall/MAP、EM/F1、ROUGE；held-out QA 测迁移，均为作者实验。
- **Baselines / Ablations / Sensitivity / Overhead:** pretrained/retrained SBERT、E5、BGE、GTE；`w/o LM` 显示
  generation objective 主要改善 localization，未普遍改善 raw retrieval；fusion/generation 增量 latency 未完整量化。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 16×MI200-64GB、BERT-base、512 tokens、
  batch/epochs披露；precision、ANN scale、query concurrency、fusion latency 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数据合同下，将生成作为 training auxiliary objective 可以改善
  query-conditioned unit localization；纯 retrieval 路径仍可只执行 bi-encoder，因此不增加该路径在线计算。
- **What It Does Not Prove:** 不证明 generated text 是忠实 citation，不证明 cross-attention 是因果解释，也不证明
  512-token fusion 可直接扩到 enterprise corpus 或低延迟 RAG。
- **Limitations / Threats to Validity:** 作者明确限制 synthetic data 多样性与 512 context；LLM rewrite 可形成
  template/teacher bias；RIR train/test 同合成 pipeline，retrieval/localization evaluator 可能偏向其定义。
- **Trade-offs / New Failure Modes:** dual objective 用 training/selected-doc compute 换可定位性，却增加 synthetic
  data provenance、objective interference、attention-as-explanation 与 generated-evidence hallucination 风险。
- **Where the Previous Design Still Applies:** corpus-scale first-stage retrieval、短 passage、严格 p99 latency 或必须
  原文引用时，bi-encoder + explicit span/reranker 更简单；GeAR 重分支应只用于有限 top-k。
- **Evolution Relationship:** `Layering / Dependency`：cached bi-encoder recall → selected-doc fusion → localization/
  generation；重路径叠加在召回之后，而非取消传统 retriever。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；Ch75 接 context provenance，Ch66 接 evidence evaluator，
  Ch43 接 selected-document prefill cost。
- **Target and Adjacent Chapters Read:** 已核对 Ch66、Ch74～77 与 Ch42～45 的 evaluation、context/RAG/memory
  和 inference cost 边界。
- **Existing Coverage:** Books 已覆盖 retrieve→rerank→ground 与 citation identity；是否加入“generation as training
  regularizer, not online source”分支留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；候选名称纠正为 Generation Augmented Retrieval，不沿用
  discovery 阶段误写的 Graph-enhanced Agent。
- **Open Questions:** generated unit 如何绑定原文 span/hash；fusion 分支如何按 uncertainty/budget 触发；在长文、
  multilingual corpus 和 ANN distribution shift 下，CL/LM objective interference 是否稳定。

### Autoregressive Pre-training from Videos / Toto

- **Candidate / Week / Score:** An Empirical Study of Autoregressive Pre-training from Videos / Toto / 2025-W02 / 26/30。
- **Source Family ID:** `toto-autoregressive-video-pretraining`。
- **Source Type:** arXiv primary representation/pretraining paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 revision/artifact 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05453v1。
- **Related Primary Sources:** tokenizer/backbone/downstream benchmark papers定义依赖与对照，不替代 v1 证据。
- **Access and Verification Status:** Verified；approach、data/tokenization、design ablations、nine downstream analyses、
  scaling、appendix 与 limitations 可读。
- **Full-read Coverage:** causal objective、LLaMA/GPT-2/Mamba comparison、data mixture、dVAE/VQGAN、layer probing、
  recognition/forecasting/tracking/robotics/object permanence、scaling law、generation 与 limitations。
- **Original Problem:** 视觉表征通常用 image-level discriminative/masked objective；它们对 temporal transition、
  future state 与 object permanence 的学习目标并不显式统一。
- **Why the Previous Design Was Reasonable:** image encoder/MAE 训练稳定、token 数较低，在分类和 dense vision 上
  表现强；视频专用 architecture 又可用 temporal inductive bias 提高效率。
- **Changed Constraint:** 希望同一 next-token objective 从大量 image/video 学到可迁移的 spatial/temporal state，
  并观察规模、layer 和任务之间的关系，而不是为每个视频任务建立单独 objective。
- **Mechanism:** 每帧独立量化为 16×16 discrete tokens，16 帧串成 4,096-token causal sequence；LLaMA-style
  decoder 预测下一视觉 token。下游通过不同层 feature 的 attention probe、fine-tuning 或 label propagation 使用
  learned state；训练 mix 结合 ImageNet/Ego4D/Kinetics/HowTo100M。
- **State Ownership:** tokenizer 拥有离散 visual vocabulary；causal sequence 拥有 raster/frame order；Transformer
  hidden state 是 predictive representation；probe/controller 才拥有下游 task decision。
- **Control Flow / Data Flow:** frames/images → frozen dVAE tokens → causal Transformer → layer features/next-token
  logits → task-specific probe/fine-tune/RL policy；generation 只是同一 objective 的一个输出用途。
- **Implementation Details:** 8k-token dVAE vocabulary、每帧 256 tokens、16 帧/stride 4、4,096 context；数据池约
  100k 小时/2.5T tokens，实际训练约 1T tokens；120M、280M、1.1B variants。
- **Evaluation Setup:** ImageNet/K400、Ego4D forecasting、DAVIS tracking、simulated Franka/Kuka manipulation、
  object permanence、layer probing 与 compute-loss scaling；不同任务使用 probe/fine-tune/RL，不能混成单一能力分数。
- **Baselines / Ablations / Sensitivity / Overhead:** architecture、tokenizer、frame order、image/video mix、layer/head、
  causal/full attention 与 model scale；视觉 loss 呈 power law，但作者明确不可直接与 GPT-3 coefficient 比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/token/data/context/frame settings披露；
  v1 HTML 未披露完整 GPU、precision、global batch、wall-clock、serving concurrency/SLO。
- **What the Evidence Actually Proves:** 在作者数据与 downstream protocols 中，causal visual-token pretraining 随
  scale 降低 validation loss，并产生可用于多类图像/视频任务的 layer representations。
- **What It Does Not Prove:** 不证明 next-token video model 是 causal world model，不证明优于 discriminative models；
  simulated manipulation transfer 也不证明 real-world physical control。
- **Limitations / Threats to Validity:** 作者明确指出 internet-video quality、frame redundancy、tokenizer ceiling 与
  非 end-to-end 学习；设计选择主要由 ImageNet 决定，dense/fine-grained/long temporal tasks 未充分验证。
- **Trade-offs / New Failure Modes:** 统一 causal objective 简化任务接口，却把 tokenizer error、raster order 和
  redundant frames 写入 state；长 token sequence 放大 compute，independent frame tokenization 丢失显式 motion identity。
- **Where the Previous Design Still Applies:** discriminative/masked encoder 在有限 compute、dense prediction 或
  classification accuracy 优先时仍更强；专用 video architecture 对长时序/高分辨率更高效。
- **Evolution Relationship:** `Alternative Branch`：image discriminative/masked representation ↔ causal visual-token
  prediction；后者再通过 task head 迁移，不自动升级为 world model。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；Ch24 接 AR generation，Ch25 接 world-model
  claim boundary，Ch28 接 pretraining objective。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch27～29 与 Ch43 的 representation、generation、world
  state、training objective 与 token-cost 边界。
- **Existing Coverage:** Books 已覆盖 visual token/rate-distortion 与 world-model distinction；是否加入“预测目标产生
  representation 但不等于 controllable dynamics”案例留待 Books 阶段。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把作者 scaling coefficient与语言模型作性能排名。
- **Open Questions:** temporal-aware tokenizer 能否减少冗余而不丢 object identity；同 compute 下 AR 与 masked/
  contrastive objective 的 transfer frontier；action-conditioned data 何时使 predictive representation升级为 world state。

### DriveBench

- **Candidate / Week / Score:** DriveBench / 2025-W02 / 27/30。
- **Source Family ID:** `drivebench-vlm-grounding-reliability`。
- **Source Type:** arXiv primary benchmark/reliability paper + official benchmark artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 revision/artifact 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04003v1。
- **Related Primary Sources:** official project/dataset links用于 artifact contract；DriveLM/nuScenes/BDD-X 定义来源
  数据边界。
- **Access and Verification Status:** Verified；construction、corruptions、tasks、models、metrics、experiments、human
  evaluation、appendices、broader impact 与 limitations 可读。
- **Full-read Coverage:** 19,200 frames/20,498 QA、15 corruptions + clean/text-only、four driving tasks、12 VLMs、
  fine-tuning/data imbalance、accuracy/language/GPT metrics、human subset 与 all detailed results。
- **Original Problem:** driving VLM 可在 language metric/GPT score 上显得可靠，却可能只根据问题文本、先验和
  majority class猜测；当视觉损坏甚至缺失时，流畅解释掩盖 grounding failure。
- **Why the Previous Design Was Reasonable:** open-loop QA、BLEU/ROUGE/GPT score 成本低且能复用现有 driving
  annotations；clean-image average 适合早期比较，不要求真实车辆闭环。
- **Changed Constraint:** safety-critical deployment 需要区分“回答看似合理”与“决策实际依赖传感器”，并评估
  corruption awareness、abstention 与 metric blind spots。
- **Mechanism:** 从 DriveLM-nuScenes 构建 perception/prediction/planning/behavior QA，对图像施加 15 类 corruption，
  加 clean/text-only 极端对照；比较 accuracy、language/GPT/GPT-context metrics，并以 human subset验证 corruption
  实际破坏视觉信息。
- **State Ownership:** sensor frame/corruption metadata 拥有观测条件；QA label/graph 拥有离线 reference；VLM
  explanation 是 proposal；GPT evaluator 只拥有 rubric score，不拥有 physical correctness。
- **Control Flow / Data Flow:** source frame/QA → clean/corrupted/text-only variant → VLM answer/explanation → multiple
  metrics/human comparison → reliability diagnosis；没有 vehicle actuation 或 closed-loop transition。
- **Implementation Details:** 19,200 frames、20,498 QA、三类 question、12 个 open/commercial VLM、17 settings；
  human evaluation从 200 keyframes 中抽 15 个并避免 corruption overlap。
- **Evaluation Setup:** single/multi-view driving perception、prediction、planning、behavior 与 corruption identification；
  clean-to-corrupt/text-only degradation、fine-tuned DriveLM-Agent、MCQ/open-ended/grounding。
- **Baselines / Ablations / Sensitivity / Overhead:** 模型×corruption×metric 对照、text-only negative control、human
  comparison、data imbalance analysis；没有真实 trajectory intervention、collision/safety outcome 或 closed-loop SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model names、dataset/settings披露；API/model
  versions之外的 hardware、precision、prompt length、batch/concurrency、latency/SLO 不构成统一合同。
- **What the Evidence Actually Proves:** 在该 dataset 中，一些 VLM 在视觉完全缺失时仍保持高 language/GPT/部分
  accuracy score，说明这些 benchmark/metrics 可被 textual prior 和 class imbalance满足，不能证明 visual grounding。
- **What It Does Not Prove:** 不证明全部 VLM 在真实驾驶必然失败，也不证明 text-only相对分数等于事故风险；
  language explanation reliability 不能外推到 trajectory/action model。
- **Limitations / Threats to Validity:** 作者明确限制在 DriveLM、有限 12 模型与 language outputs；单帧/有限 context、
  GPT rubric、human 小样本和人工 corruption 与真实 sensor fault 分布不同。
- **Trade-offs / New Failure Modes:** negative controls 暴露 shortcut，增加 evaluation matrix/cost；corruption-aware prompt
  可能提升 disclosure，却产生只在被问时承认的 performative awareness，仍无自动 fail-safe。
- **Where the Previous Design Still Applies:** open-loop QA 适合低成本 regression 与解释质量测试；但 safety gate 必须
  叠加 sensor-grounding counterfactual、trajectory simulator/closed loop 和 explicit abstention contract。
- **Evolution Relationship:** `Direct Evolution`：clean average → corruption robustness → text-only negative control →
  metric/human cross-check → future closed-loop safety evidence。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；`MULTIMODAL-EMBODIED-VLA`（Ch26）接
  physical-action boundary，Ch68/70 接 observability/security release gate。
- **Target and Adjacent Chapters Read:** 已核对 Ch25～26 与 Ch65～70 的 world/action、evidence、observability、
  governance 与 safety boundary。
- **Existing Coverage:** Books 已区分 model/harness/environment/deployment autonomy；是否加入“missing-modality negative
  control”作为通用 evaluation mechanism 留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把 benchmark 分数或作者安全警告外推成 production claim。
- **Open Questions:** 如何把 sensor dropout/corruption映射为 operational fault model；grounding、abstention 与 safe-stop
  的 release threshold；多帧、多传感器和 trajectory outcome 如何防止 text shortcut。

### Centurio

- **Candidate / Week / Score:** Centurio / 2025-W02 / 25/30。
- **Source Family ID:** `centurio-multilingual-vlm-data-mixture`。
- **Source Type:** arXiv primary multimodal training/data/evaluation paper + official model/project artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 revision/artifact 同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05122v1。
- **Related Primary Sources:** project/model cards与 SMPQA artifact用于版本/benchmark contract；不替代论文实验。
- **Access and Verification Status:** Verified；research questions、controlled mixtures、training/data、14-task suite、
  ablations、full tables、qualitative cases 与 limitations 可读。
- **Full-read Coverage:** 7→100 languages、English/non-English ratio、pretraining vs instruction tuning、synthetic OCR、
  language fidelity、LLM/backbone comparisons、Centurio training、all appendices 与 limitations。
- **Original Problem:** multilingual VLM 常把 language coverage、multicultural knowledge 与 text-in-image OCR 混成
  一个平均分；团队也不知固定数据预算应优先增加语言数还是单语样本比例。
- **Why the Previous Design Was Reasonable:** English-centric high-quality datasets覆盖任务最完整，少数高资源语言
  降低 translation/annotation cost；冻结 image encoder 可保留视觉能力并减少训练风险。
- **Changed Constraint:** 面向全球用户的 image-text system 需要在固定总预算下覆盖低资源语言、输出语言 fidelity
  与非 Latin script OCR，同时避免 English capability 被稀释。
- **Mechanism:** 固定总 data budget，逐步从 7 扩到 100 languages并调 English/non-English比例；分别控制 pretraining
  与 instruction tuning mix；为每语言加入 synthetic OCR，并比较 frozen/unfrozen vision encoder；据此训练 Aya/Qwen
  backbone 的 Centurio variants。
- **State Ownership:** dataset manifest 拥有 language/task/source identity；machine translation 拥有派生 lineage；
  tokenizer/LLM 与 image encoder分别限制 language generation和 visual text；average score不拥有文化知识真值。
- **Control Flow / Data Flow:** English source → translation/language allocation + native/synthetic OCR → multimodal
  pretraining → instruction tuning → task/language-tier/fidelity evaluation → mixture revision。
- **Implementation Details:** 100 languages；LoRA rank 256/alpha 512 applied to LLM，部分实验 image encoder frozen，
  OCR实验解冻；batch 32、one epoch、encoder lr 1e-6、LoRA/MLP 1e-4，Centurio stages用 5e-5/3e-5。
- **Evaluation Setup:** 14 tasks/56 language-task combinations，按 resource tier 汇总，并比较 13 LVLMs；包含 xGQA、
  XM3600、XVNLI、MaRVL、M3Exam、xMMMU、SMPQA grounding/naming 等。
- **Baselines / Ablations / Sensitivity / Overhead:** language count、English ratio 1～90%、pretraining ratio、uniform/
  non-uniform allocation、synthetic OCR、vision encoder freeze、LLM backbone；最佳区间依 task/tier变化。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** backbone、LoRA、batch、lr、epoch披露；GPU、
  precision、sequence/image resolution、wall-clock、serving concurrency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者固定-budget/MT/evaluation contract 中，扩大语言 coverage 到 100
  没有观察到显著统一“multilinguality curse”；约 25～50% non-English 数据常是较好折中，synthetic OCR 对
  Latin scripts 更有效。
- **What It Does Not Prove:** 不证明 25～50% 是通用最优配比，不证明 multilingual competence 等于 multicultural
  knowledge；也不证明 MT data 对 native fluency、toxicity或文化语境无损。
- **Limitations / Threats to Validity:** 作者明确区分 multilingual 与 multicultural；MT 带 translationese/低资源
  错误，现有 metrics未充分捕获生成质量；task/language coverage不均使 tier average掩盖局部退化。
- **Trade-offs / New Failure Modes:** 扩语言覆盖降低单语数据密度并引入 translation lineage；synthetic OCR扩展
  监督却可固化 font/script generator bias；解冻 image encoder改善 OCR，也可能损伤一般视觉表征。
- **Where the Previous Design Still Applies:** 单市场/法规域、极高 native quality 或数据预算很小时，少语言高质量
  native data更合理；文化知识需要独立 corpus/evaluator，不能靠翻译配比替代。
- **Evolution Relationship:** `Alternative Branch`：English-centric quality → few-language depth ↔ many-language coverage
  → task/script-aware mixture；不是语言数越多越先进的单向路线。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；`MULTIMODAL-REPRESENTATION`（Ch23）接 OCR/modality
  boundary，Ch66 接 multilingual evaluation contract。
- **Target and Adjacent Chapters Read:** 已核对 Ch23、Ch27～29 与 Ch66 的 representation、data lineage、objective
  和 evidence boundary。
- **Existing Coverage:** Books 已覆盖 data mixture/provenance 与 multilingual modality identity；是否加入 budgeted
  coverage-depth trade-off 留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把作者数据 sweet spot 外推为所有模型/语言的固定配方。
- **Open Questions:** native/MT/synthetic data 如何分别版本化与赋权；非 Latin OCR为何未同等受益；怎样用 per-language
  worst-case、fidelity与culture-aware gates替代宏平均。

### SWE-Fixer

- **Candidate / Week / Score:** SWE-Fixer / 2025-W02 / 26/30。
- **Source Family ID:** `swe-fixer-retrieve-then-edit`。
- **Source Type:** arXiv primary software-engineering/model-training paper + official repository。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 model/data/code release同 family。
- **Direct Primary Sources:** arXiv v1 PDF，https://arxiv.org/pdf/2501.05040v1；official repository，
  https://github.com/InternLM/SWE-Fixer。
- **Related Primary Sources:** SWE-bench Lite/Verified定义 evaluation environment；Qwen2.5定义 base models。
- **Access and Verification Status:** Verified；arXiv HTML 当前错误显示 NeurIPS formatting template，故用同 ID v1
  PDF、abs metadata与 official repository闭合并保留异常。
- **Full-read Coverage:** motivation/related work、retrieval/edit pipeline、JsonTuning/post-processing、110K collection/
  filtering/CoT rationalization、training setup、SWE-bench results、retrieval/edit/pipeline ablations与 appendices。
- **Original Problem:** repository issue resolution若依赖 frontier Agent自行探索，open models难获得可验证 trajectory；
  复杂多级 pipeline又使训练数据和错误归因成本过高。
- **Why the Previous Design Was Reasonable:** Agent可动态调用工具并处理未知路径；Agentless式多级 localization对强模型
  可逐步缩小搜索空间，在环境可复现时也能利用测试反馈。
- **Changed Constraint:** 目标是训练可复现的 open model，缺少廉价执行环境和高质量 Agent trajectories，因而需要把
  问题压成能用历史 issue-patch监督的少量子任务。
- **Mechanism:** BM25先从 repository召回 30 files，再由 7B retriever基于 file skeleton选 defective files；72B editor
  读取完整候选文件并输出 path/original/modified block结构。JSON/schema/syntax/snippet checks失败时最多重采样五次。
- **State Ownership:** repository snapshot拥有代码真值；BM25/retriever拥有候选集合；editor output是 patch proposal；
  evaluator environment/tests才拥有该 snapshot下的 executable verdict。
- **Control Flow / Data Flow:** issue + repo → BM25 top-30 → skeleton retriever → selected full files → editor reasoning/
  structured edits → deterministic apply/syntax checks → SWE-bench tests；没有在线 debug loop。
- **Implementation Details:** 2.3K repos/331K raw instances，经可解析、≤3 modified files等过滤为 110K；retrieval
  80K、editing/CoT 70K；Qwen2.5 7B/72B，64K context，96×A800、global batch 96、xtuner-lite。
- **Evaluation Setup:** SWE-bench Lite 300 instances与 human-validated Verified；developer-written tests判 resolve；
  作者报告 Lite 23.3%、Verified 30.2%，只代表该 model/pipeline/version。
- **Baselines / Ablations / Sensitivity / Overhead:** BM25 top-3/30、readme、file content、32K/64K、dataset size、line
  numbers、CoT与 retrieval granularity；更高 recall不必然提高 end-to-end resolve，体现 pipeline coupling。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 96×A800、7B/72B、64K、global batch 96披露；
  precision、training time、inference concurrency/latency/cost/SLO不完整。
- **What the Evidence Actually Proves:** 在作者筛选数据与 SWE-bench合同内，coarse-to-fine file retrieval加结构化
  edit可训练为 open-model pipeline；retrieval precision/recall必须由最终 executable resolve共同判断。
- **What It Does Not Prove:** 不证明 patch语义正确超出测试覆盖，不证明适用于多文件/非 Python/环境损坏任务；
  Best@1 benchmark也不等于 production coding-agent可靠性。
- **Limitations / Threats to Validity:** v1无独立 limitations节；数据主动过滤 >3 files/长 context/不可解析 patch，
  CoT由看过 gold patch的 GPT-4o rationalize，存在 hindsight leakage；训练集来自 merged PR而非独立 correctness proof。
- **Trade-offs / New Failure Modes:** 固定两段 pipeline降低 Agent state和训练成本，却把 retriever miss变成不可恢复错误；
  skeleton压缩会丢动态关系，structured replacement可能误匹配，test suite可能接受 overfit patch。
- **Where the Previous Design Still Applies:** 需要跨文件探索、运行时诊断、test generation或依赖修复时，tool-using Agent/
  iterative workflow仍必要；小而可定位的 issue更适合简化 pipeline。
- **Evolution Relationship:** `Alternative Branch`：open-ended Agent ↔ deeply staged Agentless → trainable two-stage
  retrieve/edit；后者以更窄任务分布换可训练性和成本。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；Ch76接 repository retrieval，Ch78接 edit/tool side effect，
  Ch66接 executable evaluation。
- **Target and Adjacent Chapters Read:** 已核对 Ch66 与 Ch76～82 的 retrieval、tool、planning、workflow、evaluation边界。
- **Existing Coverage:** Books 已有 proposal→action→evidence与 coding workflow原则；是否加入“training decomposition应按
  error recoverability设计”留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；显式记录 HTML/PDF身份冲突，不使用错配 HTML。
- **Open Questions:** 训练时 gold-file/editor 与部署时 retriever误差如何联合优化；环境/test identity如何版本化；怎样恢复
  retriever miss并检测 test-overfitting patch。

### VideoRAG

- **Candidate / Week / Score:** VideoRAG / 2025-W02 / 24/30。
- **Source Family ID:** `videorag-multimodal-corpus-retrieval`。
- **Source Type:** arXiv primary RAG/multimodal systems paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；后续 revision/artifact同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05874v1。
- **Related Primary Sources:** WikiHowQA/HowTo100M、InternVideo2、LLaVA-Video-7B、Whisper定义 dataset/model dependencies。
- **Access and Verification Status:** Verified；method、datasets、baselines、metrics、implementation、retrieval/generation
  variants、ablation与 conclusion可读。
- **Full-read Coverage:** text/video embedding、ASR fallback、top-k video retrieval、VT generation、oracle/random controls、
  4-frame/32-frame sampling、four answer metrics与 modality ablations。
- **Original Problem:** text RAG丢失动作/视觉过程；只给定单个视频再找关键帧不解决 corpus selection；视频没字幕时
  text-only index又失去可检索语义。
- **Why the Previous Design Was Reasonable:** transcript/caption可复用成熟 text index与 LLM，存储和 latency低；已知视频内
  frame retrieval适合用户上传、会议录像等 bounded corpus。
- **Changed Constraint:** 面向开放 instructional corpus时，系统需先找 relevant video，再把 visual与 speech/text evidence
  一起交给 generator，并在无字幕时恢复可查询文本。
- **Mechanism:** offline用 InternVideo2分别编码 video与 text/ASR transcript并拼接归一化 embedding；query text embedding
  检索 top videos；生成阶段由 LLaVA-Video消费 sampled frames、transcript或二者；无字幕则 Whisper生成 auxiliary text。
- **State Ownership:** corpus manifest拥有 video/version；ASR transcript是派生 artifact；retriever拥有 top-k proposal；
  frames/transcript各自是 evidence views，generator answer不拥有引用真值。
- **Control Flow / Data Flow:** video → 4-frame embedding + transcript/ASR embedding → index；query → retrieval → selected
  videos → 32 frames/1fps + text → LVLM answer → answer metrics。
- **Implementation Details:** retrieval每视频 uniform 4 frames；generation最多 32 frames或短视频按 1fps全取；InternVideo2
  dual encoders、LLaVA-Video-7B generator、Whisper ASR。
- **Evaluation Setup:** WikiHowQA queries/answers与 HowTo100M query-video corpus重合部分；Naive、BM25/DPR TextRAG、
  TextVideoRAG、T/V/VT与 oracle；ROUGE-L、BLEU-4、BERTScore、G-Eval。
- **Baselines / Ablations / Sensitivity / Overhead:** random/retrieved/oracle videos与 text-only/visual-only/joint retrieval/generation；
  未充分报告 corpus规模增长、top-k、frame budget、ASR error与 latency sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model与 sampling policy披露；hardware、precision、
  corpus/index size、batch/concurrency、end-to-end latency/cost/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 instructional QA合同中，relevant video优于 random，视觉帧加入生成可提升
  多种 answer metrics，text+visual embedding对 text query retrieval有效。
- **What It Does Not Prove:** 不证明生成 faithfully grounded、不证明 frame sampler捕获关键过程，也不证明其优于等成本的
  high-quality text documentation或可扩展到 web-scale corpus。
- **Limitations / Threats to Validity:** 论文无独立 limitations节；WikiHow/HowTo query overlap与 instructional domain窄，
  reference answer来自文本网页；G-Eval/overlap metrics可能奖励风格，ASR/LVLM错误可级联。
- **Trade-offs / New Failure Modes:** 多模态 evidence保留视觉信息，却增加 index/storage/prefill和 modality disagreement；
  4-frame retrieval便宜但易 temporal alias，32-frame generation仍可能漏关键瞬间。
- **Where the Previous Design Still Applies:** 文本已完整描述答案、带宽/隐私受限或 corpus超大时，TextRAG仍更经济；
  已知视频时用 frame-level retrieval可避免 corpus search。
- **Evolution Relationship:** `Layering / Dependency`：text corpus RAG → video-level retrieval → frame/transcript evidence →
  multimodal generation；各层需保留独立 identity和 failure attribution。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；Ch23接 multimodal evidence identity，Ch43/45接 visual prefill/cache cost，
  Ch66接 grounding evaluation。
- **Target and Adjacent Chapters Read:** 已核对 Ch23、Ch43～45、Ch66 与 Ch74～77 的 representation、inference、evidence、RAG边界。
- **Existing Coverage:** Books 已覆盖 multimodal retrieval与 evidence provenance；是否加入 two-budget frame sampling案例留待 Books。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不保留脱离 corpus/frame/model contract的 benchmark数字。
- **Open Questions:** query-adaptive frame budget如何设计；ASR/frame evidence冲突如何裁决；video clip/time-span citation如何
  绑定 answer并支持 cache invalidation。

### SCRIT / Self-Evolving Critic

- **Candidate / Week / Score:** SCRIT / Self-Evolving Critic / 2025-W02 / 27/30。
- **Source Family ID:** `scrit-reference-grounded-self-critic`。
- **Source Type:** arXiv primary scalable-oversight/self-training paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；后续 revision/artifact同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05727v1。
- **Related Primary Sources:** PRM800K、ProcessBench、RealCritic与 math datasets定义 evaluator/source-solution边界。
- **Access and Verification Status:** Verified；formulation、data generation/filtering、self-validation、training、two evaluation
  protocols、ablation/cases与 full appendix可读。
- **Full-read Coverage:** direct/contrastive critic、correct-incorrect/correct-correct pairing、four-stage critique、correction
  validation、solution classification、SFT config、cross-benchmark evaluation与 failure examples。
- **Original Problem:** direct critique容易 rubber-stamp错误解；依赖 human/frontier teacher的 critic supervision昂贵，
  且无法解释如何监督“当前最强模型”。
- **Why the Previous Design Was Reasonable:** 人工/强模型 critique提供直接高质量语言标签；outcome checker在数学题上便宜，
  适合先筛终局正确性而不必标每一步。
- **Changed Constraint:** 希望从同级模型自身的 correct/incorrect solutions构建大量 step-level critique，并要求生成的 correction
  可由终局答案过滤，而不是只信 fluent critique。
- **Mechanism:** 用 correct reference先做概念/策略分析，再逐步检查 target、标 first error、生成 correction；correct-incorrect与
  correct-correct pairs增加负/正例；模型自身重解 correction，只有 final answer正确的 critique进入 self-training。
- **State Ownership:** problem/ground-truth answer拥有 outcome contract；reference solution是辅助路径而非唯一证明；critic输出
  `(step critiques, correctness/error index, correction)`；self-validator与generator同源，不能视为独立 judge。
- **Control Flow / Data Flow:** problems + sampled solutions → answer-based correct/incorrect split → reference pairing → contrastive
  critique → corrected solution → outcome validation/filter → critique SFT → evaluation/new data cycle。
- **Implementation Details:** Qwen2.5-72B-Instruct；SFT用 open-instruct、32×A100（4×8）、FP16、ZeRO-3、batch 256、
  lr 5e-6、1 epoch、warmup 0.03、model parallel 8，训练数小时。
- **Evaluation Setup:** deliberately incorrect、balanced与 own-solution Critic-and-Correct；PRM800K/ProcessBench error
  identification；跨 ARC-C、College Math、GPQA、GSM8K、MATH、Minerva、MMLU STEM、OlympiadBench。
- **Baselines / Ablations / Sensitivity / Overhead:** base Qwen与 o1-mini、direct vs contrastive、pair composition、data scale与
  self-validation；部分 own-solution tasks改善有限或退化，不能只报告平均。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 72B、32×A100、FP16、batch/lr/epoch/parallel披露；
  generation sampling、total critique tokens、inference latency/concurrency/SLO不完整。
- **What the Evidence Actually Proves:** 在可用 final-answer verifier的 math domains中，reference-grounded contrastive critique
  加 outcome-filtered correction能构造 self-training data，并在作者多数 critic benchmarks改善该 model。
- **What It Does Not Prove:** 不证明 self-critic独立于 policy bias，不证明 correction final answer正确意味着每步 critique正确；
  更不证明可扩展到开放领域 scalable oversight。
- **Limitations / Threats to Validity:** reference/validator/generator共享 model family与数据先验，可能共错；math answer可验证性
  远强于 policy/science/code；correct solution也可能有无效步骤，final-answer filter无法定位其原因。
- **Trade-offs / New Failure Modes:** 无外部 teacher降低监督成本，却引入 correlated verification、reference anchoring、self-confirmation
  与 synthetic-data collapse；更严格 filtering提高 precision但缩小覆盖并丢弃困难分布。
- **Where the Previous Design Still Applies:** 开放式价值判断、高风险 policy或无 executable verifier时仍需 human/independent model；
  outcome-only checker对只关心终局且路径不重要的任务更简单。
- **Evolution Relationship:** `Direct Evolution`：direct critique → correct-reference contrast → executable/outcome correction check →
  self-training；不是消除外部 oversight，而是把它缩到 problem/answer contract。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；Ch66接 critic/evaluator independence，Ch80接 runtime reflection，Ch33接
  verifiable outcome training branch。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～34、Ch66 与 Ch79～81 的 training、evaluation、reflection/workflow边界。
- **Existing Coverage:** Books 已覆盖 verifier同源风险与 derived feedback；是否加入 contrastive-reference→self-validation演进留待 Books。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；“scalable oversight”限定为可验证数学实验，不作开放域结论。
- **Open Questions:** 如何用独立 verifier或 held-out generator打破 correlated error；first-error label如何校准；open-ended任务中
  哪种 artifact可替代 final answer。

### LlamaV-o1

- **Candidate / Week / Score:** LlamaV-o1 / 2025-W02 / 23/30。
- **Source Family ID:** `llamav-o1-visual-step-reasoning`。
- **Source Type:** arXiv primary multimodal reasoning/benchmark paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；后续 revision需单独核对是否修正效率表述。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06186v1。
- **Related Primary Sources:** VRC-Bench/PixMo/LLaVA-CoT数据与 baseline定义 training/evaluation lineage。
- **Access and Verification Status:** Verified with dispute；正文、tables、appendix可读，但效率数字/复杂度陈述内部冲突。
- **Full-read Coverage:** VRC-Bench construction/manual review、reference-based metric、curriculum stages、full-parameter training、
  beam inference、six benchmarks、ablations/runtime table与 appendices。
- **Original Problem:** visual CoT benchmark多只看终局或用 reference-free fluentness metric；stage-level reasoning/beam又会重复
  model calls，难同时比较步骤正确性与 inference cost。
- **Why the Previous Design Was Reasonable:** final-answer accuracy客观且便宜；reference-free metric允许多条有效 reasoning path；
  stage decomposition给每阶段明确输出，易人工检查。
- **Changed Constraint:** 图表/OCR/科学/文化视觉题需要定位哪一步错，并希望训练从 caption/summary过渡到 structured reasoning，
  同时控制 test-time search成本。
- **Mechanism:** VRC-Bench由 GPT-4o生成 reasoning后人工修正；GPT-4o对 generated与 ground-truth steps作多维 reference-based评分；
  model先在 PixMo练 summary/caption，再在 LLaVA-CoT-100k练固定阶段输出，部署使用 beam search选择路径。
- **State Ownership:** image/question拥有输入；人工验证的 reference chain是 evaluator anchor而非唯一合法推理；beam state拥有候选
  prefix/score；GPT-4o metric只拥有 rubric judgment。
- **Control Flow / Data Flow:** task samples → synthetic steps → human correction → curriculum SFT → beam candidates → answer/
  step metric；没有 executable visual verifier。
- **Implementation Details:** 超过 1,000 samples/4,173 verified steps/8 categories；超过 25%自动步骤被人工修正；full-parameter
  fine-tune on 8×A100-80GB；具体 lr/epochs/batch在 appendix。
- **Evaluation Setup:** VRC-Bench加 MMStar、MMBench、MMVet、MathVista、AI2D、HallusionBench；模型平均与 step metric；
  单 A100比较 beam/runtime，均为作者实验。
- **Baselines / Ablations / Sensitivity / Overhead:** Llava-CoT/stage-level beam、curriculum/data variants、1～4 beams；表内 4-beam
  runtime同时出现 6.1与正文4.2 GPU-hours，且称 beam search model calls为 `O(1)`，证据不能闭合。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A100-80GB训练、单 A100 inference披露；precision、
  sequence/image length、batch/concurrency/SLO不完整，runtime accounting自相矛盾。
- **What the Evidence Actually Proves:** v1公开了一个 human-corrected visual step dataset、reference-based judge与 curriculum/beam
  组合；作者 benchmarks显示该组合的结果，但效率主张存在内部冲突。
- **What It Does Not Prove:** 不证明 reference chain是唯一正确路径，不证明 GPT-4o step score可靠，不证明 5× speedup或 `O(1)`
  beam scaling，也不证明可用于实时 visual reasoning。
- **Limitations / Threats to Validity:** benchmark/reasoning由 GPT-4o生成并由有限人工修订，metric又使用 GPT-4o，存在 generator-
  judge correlated bias；多任务合并平均掩盖类别差异；论文未系统讨论这些限制。
- **Trade-offs / New Failure Modes:** 固定 stage提升可读性却约束 alternative paths并增加 token；reference metric可定位偏差却惩罚
  合法不同推理；beam提高候选覆盖但增加 memory/compute，且当前 accounting不可复算。
- **Where the Previous Design Still Applies:** 有 executable answer checker时应优先验证终局/中间 artifact；开放问题可保留 reference-free
  多样性评估；严格 latency下 greedy/少 stage更合理。
- **Evolution Relationship:** `Alternative Branch`：final-answer metric ↔ reference-free process score → reference-anchored step score；
  structured curriculum与 test-time beam是 layering，不是同一机制。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；Ch23接 visual evidence，Ch31接 process feedback，
  Ch48接 beam/test-time compute。
- **Target and Adjacent Chapters Read:** 已核对 Ch23、Ch31～33、Ch48 与 Ch65～67 的 representation、reward/search、evaluation边界。
- **Existing Coverage:** Books 已要求 evaluator provenance与 workload contract；该论文暂不形成可吸收效率结论。
- **Integration Decision:** `Disputed — Books Frozen`；等待 v1纠错/代码或可复现实验澄清 runtime与 complexity。
- **Changed Files or Rejection Reason:** 仅更新 W02；保留争议，不能把相互矛盾的 GPU-hours写进 Books。
- **Open Questions:** 4-beam准确 runtime是4.2还是6.1 GPU-hours；`O(1)`指 model calls、wall-clock还是误写；metric对同样正确但
  不同 reasoning chain的 calibration如何验证。

### OmniManip

- **Candidate / Week / Score:** OmniManip / 2025-W02 / 27/30。
- **Source Family ID:** `omnimanip-object-centric-spatial-constraints`。
- **Source Type:** arXiv primary robotics/system paper + official project page。
- **First-public Date / Revision History:** arXiv v1 2025-01-07；后续 revision、project artifact 与 demonstration data 属同一 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.03841v1；official project page，
  https://omnimanip.github.io/。
- **Related Primary Sources:** Omni6DPose、GroundingDINO、SAM 与所用 single-view 3D generation、pose tracking 组件定义依赖边界。
- **Access and Verification Status:** Verified；method、算法、约束优化、real-robot setup、open/closed-loop comparison、failure case 与 conclusion 可读。
- **Full-read Coverage:** canonical primitive formulation、primitive/constraint extraction、RRC planning loop、6D tracking execution loop、
  12-task real-robot evaluation、ablation、demonstration generation 与 limitations。
- **Original Problem:** VLM 有高层语义与常识，但缺少精确 3D 操作表示；直接训练 VLA 又需要昂贵、robot-specific 的数据，
  因而高层意图难安全地变成低层可执行控制。
- **Why the Previous Design Was Reasonable:** task-specific keypoint/rule、6D pose template 与 VLA 在固定对象、固定机器人和充足
  demonstration 下可把感知到动作端到端优化；open-loop motion plan 在静态、标定良好环境中更简单且 latency 更低。
- **Changed Constraint:** open-vocabulary、unseen object 与动态位姿要求表示同时携带语义 affordance、细粒度几何和可被传统优化器消费的约束，
  并在执行时吸收感知误差与对象移动。
- **Mechanism:** 在 object canonical space 用交互点 $p\in\mathbb{R}^3$ 和方向 $v\in\mathbb{R}^3$ 表示 primitive，
  用 active/passive object 间 distance/angular constraint 形成 stage contract；VLM 负责筛对象、分阶段、选 primitive 与约束，
  RRC 通过 resample-render-check 修订规划，优化器再联合 constraint、collision、path loss 求 end-effector pose。
- **State Ownership:** scene/object manifest 与 RGB-D observation 拥有环境输入；canonical mesh/6D pose 拥有对象坐标变换；VLM/RRC
  只拥有 primitive proposal；执行 tracker 拥有当前 physical pose estimate；robot/environment outcome 才拥有动作是否成功的物理证据。
- **Control Flow / Data Flow:** RGB-D → VFM object masks → VLM task decomposition → single-view mesh + canonical pose →
  point/direction candidates → VLM constraints → render/check/resample → constrained pose optimization → robot action → 6D tracking feedback。
- **Implementation Details:** GroundingDINO/SAM 标前景，single-view network 生成 mesh，Omni6DPose 做 canonicalization/tracking；
  初始方向沿 principal axes，refinement 在预测方向周围均匀采样六个方向；执行持续更新 active/passive object pose。
- **Evaluation Setup:** Franka Panda、UMI fingers 与两台 RealSense D415；12 个真实操作任务，每任务 10 次并重置布局；
  前六项 rigid、后六项 articulated，比较 VoxPoser、CoPa、ReKep 与本系统 open/closed loop。
- **Baselines / Ablations / Sensitivity / Overhead:** closed loop 在作者合同中 rigid/ articulated 汇总为 68.3%/61.7%，open loop 为
  51.7%/45.0%；也比较 primitive sampling/canonical representation。VLM 调用、mesh/pose error、loop frequency 与 end-to-end latency
  未形成完整 sensitivity/overhead contract。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** robot、camera 与主要组件披露；VLM具体版本、GPU、precision、
  planning/execution Hz、VLM calls、latency/concurrency/SLO `Not Disclosed`，故“real-time”不能外推为固定控制频率。
- **What the Evidence Actually Proves:** 在作者 12-task、单机器人与重置布局合同内，canonical object primitive 能连接语义 proposal
  与几何优化，pose-tracking execution loop 相比 open-loop 具有更高作者实验成功率。
- **What It Does Not Prove:** rendering 后由 VLM 接受 proposal 不是物理正确性证明；实验不证明任意对象/机器人/遮挡下泛化，
  也不证明其优于经大规模真实数据训练的 VLA 或满足 production real-time/safety SLO。
- **Limitations / Threats to Validity:** 作者明确指出当前 pose representation 不支持 deformable objects、依赖生成 mesh 质量，且多次
  VLM 调用计算昂贵；小样本 real-robot trials、同一实验环境与组件耦合限制外部有效性。
- **Trade-offs / New Failure Modes:** 中间 primitive 可检查、可交给优化器且 robot-agnostic，却引入 mesh/pose/canonical-frame identity、
  VLM proposal hallucination、render-world gap 与多环 stale state；规划环成功但执行失败时必须区分 proposal、tracker、controller 与环境责任。
- **Where the Previous Design Still Applies:** 对固定工位、已知对象与 tight latency，手工 constraint、teach pendant 或 task-specific policy
  更便宜可靠；数据充足且需高频 reactive control 时 VLA/low-level policy 仍适合承担动作层。
- **Evolution Relationship:** `Layering / Dependency`：semantic VLM plan → canonical interaction contract → constrained optimizer →
  physical feedback；不是 VLM 替代 control，而是把不同时间尺度与证据层分开。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Ch26）主 owner；Ch25 接 world state，Ch78 接 tool/action proposal，
  Ch81 接 durable workflow，Ch66 接 physical evidence contract。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26、Ch66、Ch78～82 的 representation、world state、evaluation 与 action/workflow 边界。
- **Existing Coverage:** Books 已区分 high-level proposal、low-level controller 与 environment transition；是否加入 canonical primitive 作为
  inspectable action interface 留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把作者的“real-time”表述或成功率脱离 robot/task/loop contract 写成通用结论。
- **Open Questions:** planning render 如何与真实 scene state 对齐；pose/mesh provenance 如何版本化；controller frequency、VLM latency 与
  safety override 如何共同形成可复现 closed-loop SLO。

### OVO-Bench

- **Candidate / Week / Score:** OVO-Bench / 2025-W02 / 25/30。
- **Source Family ID:** `ovo-bench-online-video-temporal-contract`。
- **Source Type:** arXiv primary evaluation paper + official repository。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 dataset/code revision 属同一 family，需保留版本身份。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05510v1；official repository，
  https://github.com/JoeLeelyf/OVO-Bench。
- **Related Primary Sources:** 被评测 offline/online Video-LLM 的论文与接口定义 model access、streaming state 和 input policy。
- **Access and Verification Status:** Verified；task taxonomy、data/annotation pipeline、evaluation protocol、nine-model experiments、
  analyses、failure cases 与 stated limitations 可读。
- **Full-read Coverage:** Chain-of-Time framing、backward/real-time/forward task definitions、644-video/2,814-QA construction、
  timestamped evaluator、offline simulation、human baseline、per-task results 与 data/automation limitations。
- **Original Problem:** 传统 video benchmark 假设完整视频已存在，不能判断模型在指定时刻是否只用可见历史、能否记住过去，
  或在证据尚未出现时等待而非提前回答。
- **Why the Previous Design Was Reasonable:** 离线完整视频 QA 便于统一 frame sampling、重复评测与强模型比较；对剪辑、归档检索和
  post-hoc summary，未来帧本来就可用，不需要维护在线时间状态。
- **Changed Constraint:** live stream 令 evidence 随时间单调到达；同一个问题可能要求追溯过去、立即感知或等待未来事件，
  evaluator 必须绑定 query timestamp 与合法 observation window。
- **Mechanism:** 以问题时间 $t_0$ 定义三类 temporal contract：Backward Tracing 检索已发生事件，Real-Time Perception 读取当前/近邻窗口，
  Forward Active Responding 在证据出现前保持等待、出现后再 commit；沿 timeline 多次 query 检查响应状态。
- **State Ownership:** video/timestamp manifest 拥有合法 observation prefix；model/runtime memory 拥有历史压缩状态；response state
  拥有 wait/answer proposal；annotated event window 与 evaluator 拥有是否过早、过晚或答错的 verdict。
- **Control Flow / Data Flow:** timestamped video → query at $t_0$ → allowed prefix/current window → model state update → wait or answer →
  later frame/event → optional commit → temporal/task evaluator。
- **Implementation Details:** 644 个 unique videos、7 domains、2,814 QA、12 tasks；问题来自已有数据、MLLM 半自动生成与人工提出，
  使用视觉相关 distractor 和人工修订；multiple-choice 选项数 2～5，另有少量 open-ended questions。
- **Evaluation Setup:** 比较 offline multimodal、online multimodal、blind LLM 与 human；backward、六类 real-time perception 与
  forward active-response tasks 分开计分。offline models 通过构造 $[0:t_i]$ video clips 模拟在线访问。
- **Baselines / Ablations / Sensitivity / Overhead:** blind/text、offline/online 与 human comparisons揭示 temporal category差异；
  未充分对齐各模型 frame rate、compression/memory budget、API latency、cost 与 repeated-query overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型名单与 evaluator流程披露；各模型 hardware、precision、
  context/frame budget、stream ingestion rate、concurrency/latency/SLO 不统一或 `Not Disclosed`。
- **What the Evidence Actually Proves:** benchmark 把在线视频理解拆成 past/current/future 三种可审计时序责任，并在作者 644-video
  数据合同上观察到所测模型与 human 间差距。
- **What It Does Not Prove:** 把 prefix clip 重复喂给 offline model 不证明其拥有 persistent streaming runtime；分数不分离模型能力、
  frame sampler、memory policy、API availability 与 latency，也不证明 production event response 可靠性。
- **Limitations / Threats to Validity:** 可用 timestamp annotation 稀缺，自动 QA 质量不足且依赖大量人工，限制 domain/task diversity；
  web/dataset selection、multiple-choice distractor 与 human curation 会引入 bias。
- **Trade-offs / New Failure Modes:** temporal contract 能检测 future leakage 与 premature answer，却增加 clock/event identity、wait timeout、
  state retention 和 repeated-evaluation成本；等待可提高 evidence sufficiency，也会恶化 response latency。
- **Where the Previous Design Still Applies:** 完整录像已到齐的 archive QA、editing 与 batch analytics 仍应使用 offline evaluator；
  无需对未来事件主动响应时，不必承担在线 state/timeout contract。
- **Evolution Relationship:** `Direct Evolution`：full-video offline QA → timestamp-bounded prefix QA → persistent online state →
  event-triggered wait/commit；能力与 runtime contract 需分层验证。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；Ch23 接 video representation，Ch45/56 接 temporal cache/scheduling，
  Ch77 接 long-lived memory state。
- **Target and Adjacent Chapters Read:** 已核对 Ch23、Ch43～45、Ch56、Ch65～67 与 Ch76～77 的 video input、runtime state 和 evaluator 边界。
- **Existing Coverage:** Books 已强调 workload/evidence contract，但对“future evidence 尚未到达时 wait 也是一种可评测输出”覆盖不足；
  是否吸收留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把 offline clip simulation 写成真实 streaming engine，也不跨 model contract 比较效率。
- **Open Questions:** 如何统一 frame arrival、memory budget 与 answer deadline；wait/commit 的 utility 如何同时惩罚过早和过晚；
  evaluator 怎样识别模型是否偷看未来帧或重建了全前缀。

### Migician

- **Candidate / Week / Score:** Migician / 2025-W02 / 25/30。
- **Source Family ID:** `migician-free-form-multi-image-grounding`。
- **Source Type:** arXiv primary multimodal-model/data/benchmark paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；MGrounding/MIG-Bench/model revisions 属同一 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05767v1。
- **Related Primary Sources:** Qwen2-VL-7B、RefCOCO family 与组成 MGrounding/MIG-Bench 的 source datasets 定义 base/data lineage。
- **Access and Verification Status:** Verified；task definition、CoT probe、dataset transform、two-stage training、model merge、benchmark、
  ablations、implementation 与 limitations 可读。
- **Full-read Coverage:** free-form MIG taxonomy、CoT failure modes、MGrounding-630k composition、stage-1/stage-2 mixture、MIG-Bench
  construction、single/multi-image generalization、training data/model ablations 与 limits。
- **Original Problem:** MLLM 可分别做 multi-image understanding 与 single-image grounding，却难在自由问题中先判断跨图像关系、
  再把目标定位到正确图像和具体区域。
- **Why the Previous Design Was Reasonable:** 用文本 referring expression 连接理解与 grounding 可复用已有模型能力，步骤可检查、
  无需重新训练；固定 pair/query 的 grounding benchmark 也更容易消除歧义。
- **Changed Constraint:** free-form query 可能含视觉 reference、共性/差异、tracking 或多视角关系，目标身份只能由多张图联合决定，
  中间文本未必能无损表达抽象视觉信息。
- **Mechanism:** CoT branch 先 multi-image understanding 生成 referring text、再单图 grounding；end-to-end branch 用 MGrounding-630k
  做两阶段 instruction tuning：先混合广覆盖 MIG 与 general tasks，再用高质量 free-form MIG refine，并通过 stage-2 weight averaging
  平衡自由 grounding 与常规能力。
- **State Ownership:** ordered image set 与 per-image identity 拥有视觉上下文；query/reference 拥有目标关系；CoT text 是派生、可能有损的
  intermediate state；bounding box proposal 不拥有 object identity，human/benchmark annotation 才拥有定位 verdict。
- **Control Flow / Data Flow:** source datasets/images → MIG transformation + general-task mixture → stage-1 tuning → high-quality free-form
  tuning → weight merge；inference 为 multi-image/query → direct box，或 understanding text → single-image grounding。
- **Implementation Details:** MGrounding-630k 覆盖多类 MIG，stage mixture 用 single-/multi-image understanding 与 grounding 缓解遗忘；
  Qwen2-VL-7B、global batch 48、两阶段共 25k steps、lr 5e-6、8×A100-80GB。
- **Evaluation Setup:** MIG-Bench 覆盖 10 tasks、5.9k images、约 4.3k test instances；每个 instance 只有一个 clear target region，
  以 $Acc_{0.5}$ 判 IoU>0.5，并比较主流 MLLM、CoT 与 trained variants。
- **Baselines / Ablations / Sensitivity / Overhead:** direct prompting、CoT、不同 data type/scale、two-stage 与 model merge；也检查 conventional
  grounding/understanding generalization。缺少对图像数、分辨率、token budget、CoT latency 与 merge coefficient 的系统 sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B、8×A100-80GB、batch 48、25k steps、lr 披露；precision、
  image/token length、inference batch/concurrency/latency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 data/benchmark 合同内，multi-image understanding 与 grounding 并不会自动组合；
  专门的 mixture/two-stage training 提高 free-form MIG，CoT 是可用但有边界的组合 baseline。
- **What It Does Not Prove:** 不证明 end-to-end box 内部保留可审计 cross-image reasoning，不证明 70B 或开放世界 generalization，
  也不证明 IoU>0.5 等于正确理解关系、计数、身份或时间连续性。
- **Limitations / Threats to Validity:** 作者未验证 70B；复杂/杂乱场景仍定位不准；training/benchmark 主要集中 REC；source dataset
  transformation 与单一 clear target 可能弱化开放式多目标歧义。
- **Trade-offs / New Failure Modes:** 文本中间层可观察、可替换，却产生 error propagation、额外 latency 与 visual-to-text information loss；
  direct model 避免瓶颈但降低因果可解释性；两阶段/weight merge 可能掩盖 branch interference 与 calibration drift。
- **Where the Previous Design Still Applies:** 目标能用清晰文本描述、需要人审或组件可替换时，CoT/pipeline 更合适；
  单图或固定 image pair 的 conventional grounding 无需引入复杂 multi-image training。
- **Evolution Relationship:** `Alternative Branch`：single-image grounding + multi-image understanding → textual composition pipeline ↔
  end-to-end joint grounding；two-stage mixture 是减少 branch interference 的训练层，不是证明中间表示无用。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；Ch26 接 embodied grounding，Ch76 接 multi-image retrieval/context，
  Ch66 接 identity/localization evaluation。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26、Ch66、Ch75～77 的 representation identity、physical grounding 与 context/evidence边界。
- **Existing Coverage:** Books 已讨论 modality/reference identity；是否加入“可解释文本桥接与 joint representation 的有损/不可见 trade-off”留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把 benchmark improvement 外推为开放世界跨图像 identity 已解决。
- **Open Questions:** 多目标/动态图像怎样表达 target identity；model merge 如何校准两阶段冲突；是否可用 structured visual relation graph
  兼顾可审计性与低信息损失。

### Multiagent Finetuning

- **Candidate / Week / Score:** Multiagent Finetuning / 2025-W02 / 26/30。
- **Source Family ID:** `multiagent-finetuning-diverse-reasoning`。
- **Source Type:** arXiv primary post-training/multi-agent paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；后续 revision/code 属同一 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05707v1。
- **Related Primary Sources:** Phi-3、Mistral-7B、Llama-3 与 Arithmetic/GSM/MATH/MMLU 定义 model/task contract。
- **Access and Verification Status:** Verified；algorithm、generation/critic dataset construction、iterative training、evaluation、diversity metrics、
  hardware/config 与 appendices 可读。
- **Full-read Coverage:** single-agent self-training motivation、$N$-agent/$M$-round debate、pseudo-label/data filtering、generation/critic FT、
  repeated iterations、three core tasks、additional MATH/MMLU/zero-shot experiments、diversity analyses 与 limitations。
- **Original Problem:** 单模型用自身答案做 self-training 容易迅速同质化并遇到 diminishing returns；如果没有 external label，
  怎样从多个 reasoning trajectories 提取可学习信号而保留差异。
- **Why the Previous Design Was Reasonable:** single-agent SFT/STaR 成本低、部署简单；多数投票和 debate 在独立 error 假设下可通过冗余
  提高终局稳定性，无需人工标每条 reasoning path。
- **Changed Constraint:** 同一模型多次采样会相关且多样性随训练下降；系统希望利用 agent 间 disagreement、critique 与由错转对的 trajectory，
  但训练问题没有提供 answer annotation。
- **Mechanism:** 让 $N$ agents 进行 $M$ 轮 debate，以末轮 majority answer 作 pseudo-ground truth；generation agent 保留首轮与多数答案一致的
  trajectory，critic agent 学习从其他回答摘要修订自己，混合 correct-stays-correct 与 incorrect-to-majority examples；分别 full-finetune 后重复迭代。
- **State Ownership:** task input 拥有问题；各 agent checkpoint/trajectory 拥有局部 proposal；debate transcript 是共享派生状态；majority vote
  只拥有 pseudo-label，不拥有 truth；held-out ground-truth dataset 只在 evaluation 阶段拥有 correctness verdict。
- **Control Flow / Data Flow:** unlabeled prompt → independent first-round generations → summaries/critic rounds → final majority → generation/critic
  dataset filtering → distinct model finetunes → next iteration → held-out labeled evaluation。
- **Implementation Details:** 默认 3 agents/2 rounds，并在 appendix 扩到 5 agents；Phi-3 4B、Mistral 7B、Llama-3 8B 全参数训练，
  不使用 LoRA；各任务固定 500 unlabeled training prompts 与 500 held-out evaluation prompts。
- **Evaluation Setup:** Arithmetic、GSM、MATH 为主，appendix 扩到全难度 MATH、MMLU 与 zero-shot transfer；比较 base、single-agent FT、
  majority、debate、majority FT 与 proposed method，并报告多次 seed/consensus、embedding 与 reasoning pattern diversity。
- **Baselines / Ablations / Sensitivity / Overhead:** generation-only/critic、single/multiple iterations、agent/round count、3/5 agents与多种 diversity
  metrics；没有充分控制同等 token/compute budget，且 majority pseudo-label 的置信度/相关性 sensitivity 不完整。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** individual configs 为 2～4×A100-40GB 或 1～3×H100-80GB，
  full FT、batch 1、model-specific lr/epochs；论文另报总实验资源 8×A100-40GB + 4×H100-80GB、单组 inference约30～36小时。
  precision、token budget、serving concurrency/latency/SLO不完整。
- **What the Evidence Actually Proves:** 在作者小规模任务与固定 compute setup 中，以 debate disagreement 构造 generation/critic 数据可比
  single-agent self-training 保留更多 measured diversity，并提高所测模型的 held-out accuracy。
- **What It Does Not Prove:** majority answer 不是真值；结果不证明 agents 独立、不证明越多 agent 越好，也不证明该昂贵流程在开放域、
  长任务或等 token/energy budget 下仍优于强 single-agent search/verifier。
- **Limitations / Threats to Validity:** 作者明确承认 training/inference 显著更贵；同 base family、相似 prompt 与共享 debate 会产生相关错误；
  小规模 500-example contract、数学/选择题答案抽取和多数投票可能放大共同错误并形成 model collapse。
- **Trade-offs / New Failure Modes:** 多 agent 提供 trajectory diversity 与错误修订样本，却增加 checkpoint、communication、summary loss 与训练/推理成本；
  反复用 majority 自举可能让 minority-correct signal 被过滤，diversity metric 改善也不等于 epistemic independence。
- **Where the Previous Design Still Applies:** 有可靠 verifier/label、单模型仍有 headroom 或成本/SLO严格时，single-agent SFT、best-of-N、
  search 或 verifier-guided training 更简单；只有任务可分解且 disagreement 有信息时才值得多 agent。
- **Evolution Relationship:** `Alternative Branch`：single-agent self-training ↔ sampled majority → multi-round debate-derived data → iterative
  multiagent finetuning；核心变化是 pseudo-label/data ownership，不是 agent 数量的单向扩张。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；Ch36 接训练成本/并行，Ch66 接 pseudo-label evaluator，
  `AGENT-MULTI-AGENT`（Ch82）接 runtime diversity/communication tax。
- **Target and Adjacent Chapters Read:** 已核对 Ch28～31、Ch36、Ch66 与 Ch79～82 的 self-training、feedback、evidence 与 multi-agent边界。
- **Existing Coverage:** Books 已覆盖 multi-agent error amplification 与 single-agent headroom；是否加入“debate 作为 data generator、majority 不是 truth”
  的 training branch 留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不把作者 accuracy 或 diversity metric 外推为 production agent coordination收益。
- **Open Questions:** 如何估计 agent error correlation；怎样保留 minority-correct trajectories；用独立 verifier或 calibrated confidence替代 majority
  后，收益是否仍来自 multiagent机制；同 compute budget 下与 best-of-N/search如何比较。

### ReFocus

- **Candidate / Week / Score:** ReFocus / 2025-W02 / 26/30。
- **Source Family ID:** `refocus-visual-editing-chain-of-thought`。
- **Source Type:** arXiv primary multimodal reasoning/tool-use paper + official project page。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；后续 dataset/model/artifact 属同一 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.05452v1；official project，
  https://zeyofu.github.io/ReFocus/。
- **Related Primary Sources:** TableVQA、ChartQA、CharXiv、Phi-3.5-Vision 与 GPT-4o checkpoint 定义 data/model/evaluator contract。
- **Access and Verification Status:** Verified with metadata inconsistency；正文与附录反复给出 14k/14,344，v1 conclusion summary 另写 21k，
  该数量冲突已保留但不妨碍 method/evaluation review。
- **Full-read Coverage:** structured-image problem、editing tool API、iterative execution、six benchmark subsets、edit-type analyses、
  14,344-case SFT data/filtering、Phi-3.5-Vision comparison、appendix configs/prompts 与 qualitative cases。
- **Original Problem:** 图表/表格推理需要跨区域选择、排除干扰并反复回看视觉证据；纯文本 CoT 往往在一次 OCR/description 后失去
  image-space location 与注意焦点。
- **Why the Previous Design Was Reasonable:** OCR→text→reasoning 可复用成熟 LLM 和符号计算，端到端 VQA 则减少 tool/runtime surface；
  若图像结构简单或文本提取准确，二者都比多轮视觉编辑便宜。
- **Changed Constraint:** 多 subplot、长表格与相似 bars 使一次全图编码容易混淆；中间 reasoning state 需要携带“看哪里/忽略哪里”，
  而不只是自然语言解释。
- **Mechanism:** 模型生成受限 Python pseudo-code，调用 mask、box、highlight 等 image-edit tools；runtime 执行后把新图像作为下一轮输入，
  直到输出答案。训练数据保存 thought、editing code、focus bounding box、edited-image reasoning 与 answer。
- **State Ownership:** 原图与坐标 manifest 拥有 source evidence；tool call 拥有 edit proposal；edited image 是带 provenance 的派生 attention state，
  不能替代原图；answer evaluator 拥有 task verdict；GPT-4o-generated thought 不拥有 ground-truth reasoning。
- **Control Flow / Data Flow:** image/question → model thought + tool code → deterministic edit → derived image → model re-observation → repeated edit/answer；
  training path 再对正确 GPT-4o trajectories 过滤并 SFT Phi-3.5-Vision。
- **Implementation Details:** table coordinates 由 OpenCV contours/lines 推断，chart 使用 subplot/bar coordinates；temperature 0；
  15,059 ChartQA examples 中保留 14,344 条正确 trajectories，其中 12,819 含 visual editing。
- **Evaluation Setup:** VWTQ、synthetic VWTQ、VTabFact、CharXiv multi-subplot、ChartQA horizontal/vertical bars；比较 GPT-4o 两个 checkpoint、
  CoT baseline、VisProg、open VLM 与 oracle edited-image transfer，并做等数据 SFT 对照。
- **Baselines / Ablations / Sensitivity / Overhead:** mask/draw/highlight、正确/随机 edit、text input、oracle artifact、QA/CoT/VCoT supervision；
  多轮 API/tool latency、token/image processing cost、edit-error recovery 与最大步数未形成完整 sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** open-model inference 使用 4×Quadro RTX 8000、约40 GPU-hours；
  GPT-4o checkpoint、Phi-3.5-Vision与 temperature披露；SFT GPU/precision/batch、API latency/concurrency/SLO不完整。
- **What the Evidence Actually Proves:** 在作者 structured-image 数据与 evaluator合同内，改变 intermediate representation 为可执行视觉编辑
  能让模型重新观察更聚焦的证据，且其过滤后 supervision 比同数据 QA/文本 CoT 在所测 Phi-3.5-Vision 设置更有效。
- **What It Does Not Prove:** edited image 不增加 external knowledge，但可能编码由强模型/坐标工具提供的 oracle attention；结果不证明视觉编辑
  是通用 reasoning、更不证明每条 edit chain 忠实或 GPT-4 judge 无偏。
- **Limitations / Threats to Validity:** 论文无独立 limitations节；工具依赖预知/启发式 coordinates 与规则化 table/chart，GPT-4o 同时参与
  trajectory生成和答案判定；v1 的 14k 与 21k 描述冲突，复杂自然图像/错误 edit 的外部有效性未知。
- **Trade-offs / New Failure Modes:** visual state 可审计并减小 distractor，却增加 code execution、coordinate drift、destructive masking、
  derived-artifact lineage 与多轮成本；错误 edit 会删除关键证据并在后续被当成原始事实。
- **Where the Previous Design Still Applies:** OCR 可靠、结构可直接序列化或 latency严格时，text CoT/SQL/程序推理更稳；
  无可验证 edit schema 的开放视觉任务宜保持原图和 non-destructive crop/reference。
- **Evolution Relationship:** `Principle Reuse`：textual CoT → executable program-of-thought → provenance-preserving visual state transformation；
  它与 end-to-end attention 是替代/组合分支，不是视觉编辑必然取代模型内部注意力。
- **ROADMAP Node:** `AGENT-TOOL`（Ch78）主 owner；Ch23 接 visual representation，Ch66 接 evaluator/provenance，Ch81 接 iterative workflow。
- **Target and Adjacent Chapters Read:** 已核对 Ch23、Ch66 与 Ch76～82 的 representation、tool side effect、workflow 与 evidence边界。
- **Existing Coverage:** Books 已区分 proposal、tool execution 与 derived artifact；是否加入“中间推理状态可跨 modality 变换”留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；数量采用 appendix 可复算的 14,344，同时显式保留 v1 conclusion 的 21k 冲突。
- **Open Questions:** edit artifact 如何绑定原图 hash/region provenance；destructive mask 如何 rollback；真实 tool/runtime cost 下收益是否仍优于 crop/OCR；
  21k 是否为未披露合并版本或单纯笔误。

### ConceptMaster

- **Candidate / Week / Score:** ConceptMaster / 2025-W02 / 24/30。
- **Source Family ID:** `conceptmaster-decoupled-multi-concept-video`。
- **Source Type:** arXiv primary video-generation/model/data paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续 code/model/data release 属同一 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04698v1。
- **Related Primary Sources:** WebVid、BLIP-Diffusion、CelebV、CLIP、DINO、VBench 与 proprietary T2V backbone 定义 dependencies。
- **Access and Verification Status:** Verified；method、data pipeline、training implementation、MC-Bench、baseline/ablation 与 supplementary details 可读；
  backbone、hardware 和完整 artifact 不公开。
- **Full-read Coverage:** MCVC formulation、1.3M data construction、Q-Former representation、decoupled attention mapping（DAM）、latent DiT/
  rectified flow、283-case MC-Bench、naive/tuning baselines、architecture/data ablations 与 implementation appendix。
- **Original Problem:** 多个 reference concepts 同时注入 video generator 时会 identity mixing；single-concept fine-tuning 对每个新概念昂贵，
  image personalization→I2V 两段 pipeline 又会叠加 decoupling 与 temporal consistency error。
- **Why the Previous Design Was Reasonable:** DreamBooth/adapter 为单主体提供高 fidelity；先生成个性化首帧再动画化可复用 image models，
  在单主体、短视频与可接受 test-time tuning 时更简单。
- **Changed Constraint:** 多人物/动物/物体组合要求每个 reference image 与自己的 text label 绑定，同时保持整体 caption、motion 与 temporal quality，
  且新组合不能逐项再训练。
- **Mechanism:** CLIP image encoder 输出每个 concept 的 dense tokens，Q-Former提取表示；DAM 让各 concept embedding 分别通过 decoupled
  cross-attention 注入 latent diffusion transformer，避免先 concat 后 identity entanglement；T5 text branch控制整段语义，rectified flow生成视频。
- **State Ownership:** concept image/label pair 拥有 condition identity；Q-Former token是派生 representation；DAM拥有 concept-to-video-token
  attention proposal；generated pixels 不拥有身份真值，per-object detection/crop evaluator 才对局部 fidelity 评分。
- **Control Flow / Data Flow:** videos → shot/object/caption processing → multi-concept training tuples + auxiliary single-concept data →
  CLIP/Q-Former tokens + T5 caption → decoupled cross-attention/DiT denoising → generated video → global/local/temporal metrics。
- **Implementation Details:** 构建 >1.3M MCVC samples，辅以约300k BLIP-Diffusion images与60k CelebV，sampling 8:1:1；
  77 frames/5s/15fps；caption/reference condition dropout 50%/33%；冻结3D spatiotemporal self-attention并训练其余指定模块。
- **Evaluation Setup:** MC-Bench 283 samples覆盖六类多概念组合且与训练集无重叠；concept fidelity 用 CLIP-I/T，decoupling先由 OWLv2
  检测局部 box再算 CLIP/DINO，video quality用 VBench dimensions，并比较 image-personalization+I2V、DreamBooth 等。
- **Baselines / Ablations / Sensitivity / Overhead:** without Q-Former/DAM、concat-MLP、self-attention、naive two-stage 与 tuning-based baseline；
  未系统报告 concept count、similarity、occlusion、prompt complexity、sampler steps、latency/VRAM 与 detector-error sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** proprietary transformer T2V、77 frames/5s/15fps 与冻结策略披露；
  parameter count、GPU、precision、batch、training cost、inference latency/concurrency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者私有 backbone/data 与 283-case benchmark 合同内，显式分离 concept condition 并独立注入比
  所测 concat/self-attention/two-stage baselines 更能维持局部 identity metrics。
- **What It Does Not Prove:** 不证明 metrics 等于人类身份判断，不证明对任意概念数量/遮挡/交互可组合；未公开 backbone/hardware 使成本、
  可复现性与“无需 test-time tuning”的系统收益无法完整比较。
- **Limitations / Threats to Validity:** 无独立 limitations节；训练数据/基座私有，MC-Bench小且由相似 pipeline 构建；OWLv2检测失败会污染局部
  fidelity，CLIP/DINO可能偏好复制外观而非动作/关系正确。
- **Trade-offs / New Failure Modes:** decoupled identity降低 subject mixing，却增加 condition tokens、attention cost 与 entity-label binding state；
  过强 fidelity可能抑制 motion/pose变化，多主体 interaction 与相对尺度仍可能不自然。
- **Where the Previous Design Still Applies:** 单主体少样本、要求极高 likeness且可接受个体优化时 DreamBooth/adapter仍合理；
  image→I2V对首帧严格可控、短运动任务也更易调试。
- **Evolution Relationship:** `Alternative Branch`：per-concept tuning ↔ encoder-based zero-shot conditioning；single fused condition →
  entity-bound decoupled injection；它解决 identity routing，不等于解决 physical interaction。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；Ch23 接 condition identity，Ch25 接 temporal/world consistency，
  Ch66 接 multi-object evaluator。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26、Ch45 与 Ch66 的 conditioning、generation、temporal state 与 evidence边界。
- **Existing Coverage:** Books 已覆盖 diffusion condition/control 与 identity；是否加入 entity-bound attention routing 作为多条件组合案例留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；不保留脱离 proprietary model/data/metric contract 的“显著优于”或质量数字。
- **Open Questions:** concept token 如何随主体数量扩展；local detector错配怎样反馈；如何度量 identity、motion 与 interaction三者冲突；
  公开 backbone 上的成本和可复现性如何。

### Multi-subject Open-set Video Personalization / Video Alchemist

- **Candidate / Week / Score:** Multi-subject Open-set Video Personalization / 2025-W02 / 25/30。
- **Source Family ID:** `video-alchemist-open-set-multi-subject-personalization`。
- **Source Type:** arXiv primary video-generation/model/data/evaluation paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；后续 model/data/benchmark revision 属同一 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06187v1。
- **Related Primary Sources:** MSR-VTT、CogVideoX-5B autoencoder、CLIP、DINOv2 与 personalization baselines定义 dependencies。
- **Access and Verification Status:** Verified；architecture、data construction/augmentation、two-stage training、benchmark、ablation、inference CFG、
  hardware 与 explicit limitations 可读。
- **Full-read Coverage:** multi-subject/open-set formulation、subject-level fusion、reconstruction leakage、segmentation/data augmentation、
  MSRVTT-Personalization、latent DiT architecture、resolution/length curriculum、dual CFG 与 limitation appendix。
- **Original Problem:** 现有 video personalization 多限人脸、单主体或前景对象；从同一视频抽 reference/target 训练会把 pose、lighting、crop、
  background 与 identity 一起复制，形成 copy-and-paste overfit。
- **Why the Previous Design Was Reasonable:** reconstruction pairs 易自动收集且提供强 pixel-level supervision；single-subject/fixed-category model
  缩小 identity ambiguity；test-time tuning在少量重要主体上可换更高特异性。
- **Changed Constraint:** 系统需无需个体微调地组合 open-set foreground、多个 subjects 和 background，并允许姿态、尺度、光照与动作变化，
  因而 identity 必须与 incidental appearance factor 解耦。
- **Mechanism:** 对每个 segmented reference image，融合 image patch embeddings 与 entity word形成 subject-level tokens，拼接后通过每个 DiT block
  的独立 personalization cross-attention 注入；训练用 scale/blur/color/flip/shear/rotation 与 replacement sampling打断 reference-target捷径，
  inference对 text/image condition分别做 CFG。
- **State Ownership:** segmented reference + entity word 拥有 subject condition identity；augmentation manifest拥有派生 lineage；text condition拥有
  scene/action；DiT latent是生成状态；per-segment benchmark annotation拥有各主体 fidelity verdict。
- **Control Flow / Data Flow:** source video → shots/segments/caption/reference tuples → identity-preserving augmentation → stage-I generic video model →
  stage-II personalization → text/reference encoders → dual cross-attention denoising + dual CFG → generated video → segment-level evaluation。
- **Implementation Details:** latent DiT 使用 CogVideoX-5B autoencoder（temporal/height/width compression 4×8×8）、CLIP+DINOv2 patch tokens；
  fixed 24fps，多 resolution/17～289 frames batches；支持 256×144 最长12s，较高分辨率最长5s。
- **Evaluation Setup:** MSRVTT-Personalization基于 MSR-VTT clips，覆盖 face、single/multiple arbitrary subjects、foreground+background；
  用 per-object segments而非全图 similarity，结合 human/automatic quantitative、qualitative comparison 与 architecture/data ablation。
- **Baselines / Ablations / Sensitivity / Overhead:** test-time optimization、encoder-based image/video personalization、data augmentation、
  subject-word fusion、patch/class token与 CFG scales；多主体密度、segmentation error、长时 identity drift 与等成本 baseline仍不完整。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** stage I 256×A100-80GB、stage II 64 GPUs；24fps、resolution/length/batch
  sampling披露；precision、training duration、sampler steps的完整 latency、concurrency/SLO不完整。
- **What the Evidence Actually Proves:** 在作者大规模训练与 MSRVTT-Personalization合同内，显式 subject-word binding、patch-level condition、
  shortcut-breaking augmentation能降低所测 reconstruction overfit，并支持多类 open-set conditions。
- **What It Does Not Prove:** 不证明 segmentation/identity在开放世界无歧义，不证明生成视频保持因果/物理正确或长时 identity；高资源作者结果
  也不能外推到小模型/低成本部署。
- **Limitations / Threats to Validity:** 作者报告仍会复制 reference expression/pose，需要用户提供准确 segmentation，多主体时偶发不自然 composition/
  scale；多主体视频在训练分布中偏少，benchmark/metrics可能奖励外观复制。
- **Trade-offs / New Failure Modes:** augmentation促使 identity invariance，却可能删除细微身份特征；patch tokens保留局部细节但增加 condition compute；
  entity binding降低混合，却新增 segmentation、label、relative-scale 与 subject-count failure。
- **Where the Previous Design Still Applies:** face-only、single product/character或有高质量 few-shot 数据时，专用 encoder/test-time tuning更经济；
  首帧动画适合短视频与强 pose control。
- **Evolution Relationship:** `Direct Evolution`：reconstruction personalization → shortcut-aware augmentation → entity-bound multi-subject conditioning；
  与 ConceptMaster 是同周独立分支，前者强调 open-set/data leakage，后者强调 decoupled injection。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；Ch23 接 identity representation，Ch25 接 temporal state，
  Ch66 接 segment-level evaluation。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26、Ch45、Ch66 的 multimodal identity、generation、persistent state 与 evaluator边界。
- **Existing Coverage:** Books 已讨论 conditioning/identity 与 video generation；是否加入 shortcut-breaking augmentation→entity binding 演进留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；与 ConceptMaster 保持两个 source family，不按相似发布日期或任务合并结论。
- **Open Questions:** 无需人工 segmentation 的 identity contract如何建立；多主体 interaction/relative scale如何评测；长时 identity drift和 dual-CFG
  stability如何绑定 sampling cost。

### Demystifying Domain-adaptive Post-training for Financial LLMs / FinDaP

- **Candidate / Week / Score:** Demystifying Domain-adaptive Post-training for Financial LLMs / 2025-W02 / 28/30。
- **Source Family ID:** `findap-domain-adaptive-post-training`。
- **Source Type:** arXiv primary domain-training/evaluation paper + released data/model/leaderboard family。
- **First-public Date / Revision History:** arXiv v1 2025-01-09（旧 census 的 2025-01-08 已纠正）；后续 revision/artifact属同 family。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04961v1。
- **Related Primary Sources:** Llama-3-8B-Instruct、finance/general datasets、GPT-4o GenRM、DPO/LoRA papers定义 dependencies。
- **Access and Verification Status:** Verified；capability taxonomy、evaluation suite、data curation、CPT/IT/joint/LoRA/PA experiments、final recipe、
  appendices 与 limitations 可读。
- **Full-read Coverage:** seen/unseen-similar/unseen-novel split、text/prompt mixture、CPT/IT forgetting、sequential vs joint、full FT vs LoRA、
  on-policy GenORM/GenPRM preference construction、modified DPO、final evaluation 与 data/model caveats。
- **Original Problem:** domain adaptation 常被压成“多喂领域文本”或“做领域 SFT”，却混淆 concept acquisition、task imitation、instruction following、
  reasoning 与 general retention，导致收益/遗忘无法归因。
- **Why the Previous Design Was Reasonable:** CPT直接用无标注领域 corpus 学 concepts，IT高效教任务格式，LoRA降低成本，顺序 CPT→IT 允许两阶段
  独立数据规模和配置；在 domain/task窄且可回归测试时都合理。
- **Changed Constraint:** instruction-tuned base 在 CPT 后可能丢失对话/指令能力；只做 IT又改善 seen/similar tasks而难迁移新任务；finance还需要
  reasoning，因此必须把 data mixture、stage order、parameter update 与 evaluation capability共同设计。
- **Mechanism:** 先按 general/finance构建 CPT/IT mixture；CPT next-token 与 IT masked-instruction examples按等量下采样联合训练以让 concept与task
  同时更新，再以更高质量 curriculum继续；从 on-policy checkpoint采样轨迹，用 GPT-4o GenORM/GenPRM给 outcome/step correction，构造 preference，
  最后用含 NLL 项的 modified DPO alignment。
- **State Ownership:** corpus/prompt manifest拥有 domain/task/provenance；checkpoint拥有当前 concept/instruction state；GenRM输出是 preference proposal；
  benchmark split拥有 seen/novel contract但不是真实金融正确性全域；human/source answers才是基础监督。
- **Control Flow / Data Flow:** capability definition → held-out split/evaluator → general+finance text/prompts → CPT/IT joint mixture → checkpoint →
  on-policy trajectories → outcome/process feedback + corrections → chosen/rejected pairs → modified DPO → per-capability release gate。
- **Implementation Details:** 以 Llama-3-8B-Instruct为 base，curated prompt总量约3.16M；比较 CPT-In/Gen/Mix、IT-In/Gen/Mix；joint时将 CPT
  downsample至 IT 规模；LoRA rank 128（并比较32/512）；final recipe含两组 sequential curriculum的 joint CPT+IT 与 PA。
- **Evaluation Setup:** 将 finance/general能力分成 seen、unseen-similar、unseen-novel，覆盖 sentiment、stance、NER、summarization、knowledge、
  QA、reasoning、IF/chat；与 base、8B/70B open models与 GPT-4o 比较，但 metrics/task size各异。
- **Baselines / Ablations / Sensitivity / Overhead:** in-domain/general/mixed data、CPT/IT/joint/sequential、full FT/LoRA ranks、PA-In/Mix、
  GenORM/GenPRM preference与 loss variants；缺少跨 model family、compute-normalized data search与生产 finance evaluation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8B base、data counts、LoRA rank与 stage recipe披露；GPU、precision、sequence、
  global batch、training tokens/time/cost、inference concurrency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 Llama-3-8B/data/evaluation合同中，纯 CPT 会严重破坏 instruction following，general replay可减轻
  concept遗忘，joint CPT+IT比所测 sequential recipe更好地平衡 transfer，PA补充了 reasoning branch。
- **What It Does Not Prove:** 不证明同一 mixture/stage recipe适合其他 model family或领域；不证明 benchmark提升等于金融事实可靠/合规安全，
  也不证明 full FT普遍优于 LoRA——该差异只出现在作者 joint concept→task transfer设置。
- **Limitations / Threats to Validity:** 作者明确指出 unseen novel仍不足、全规模 empirical data search耗时，recipe可能不跨 model family；
  GPT-4o生成 responses/rewards带 correlated bias，finance benchmark/leaderboard可能混入训练相似性，hardware/token成本未披露。
- **Trade-offs / New Failure Modes:** joint training减少阶段间遗忘却把 mixture ratio与 optimizer interference绑在一起；general replay保留能力但稀释领域 token；
  full FT提高 transfer也提高成本/灾难遗忘风险；GenRM process signal更密集但可能制造 fluent错误 correction。
- **Where the Previous Design Still Applies:** 任务固定、数据少、需低成本隔离时 LoRA/IT更合理；base非 instruct或可在 IT恢复时 sequential CPT→IT更灵活；
  外部知识变化快时 RAG优于把所有事实写入权重。
- **Evolution Relationship:** `Alternative Branch`：domain CPT、task IT、PEFT与 preference alignment不是单一路径；该证据形成
  concept acquisition ↔ task adaptation → joint anti-forgetting → reasoning alignment 的条件化演进。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Ch28）主 owner；Ch27 接 data mixture/provenance，Ch29/30接 SFT/LoRA，Ch31/34接 preference/DPO，
  Ch35接 checkpoint identity，Ch66接 capability evaluation。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～35、Ch66 的 data、training branch、checkpoint 与 evidence contract。
- **Existing Coverage:** Books 已把 CPT/SFT/preference写成分支，但“在 instruct base 上 CPT 可先破坏 instruction state、joint mixture可改变 stage boundary”
  是否形成 refine 点留待 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W02；纠正 event date，不把 finance-specific mixture、LoRA或 benchmark数字外推为通用配方。
- **Open Questions:** 如何低成本预测 mixture效果；checkpoint如何测 concept/task/instruction三类 forgetting；独立 verifier能否降低 GPT-4o GenRM相关偏差；
  同 token/compute budget下 joint与 sequential差异是否稳定。

### Transformers 4.48.0

- **Candidate / Week / Score:** Transformers 4.48.0 / 2025-W02 / 20/30。
- **Source Family ID:** `transformers-v4.48.0-platform-release`。
- **Source Type:** official GitHub Release + merged PR/code-change evidence。
- **First-public Date / Revision History:** GitHub Release 2025-01-10；tag `v4.48.0` / commit `6bc0fbc`；patch releases另属修复节点。
- **Direct Primary Sources:** official release，https://github.com/huggingface/transformers/releases/tag/v4.48.0；release-packaging PR #35296，
  https://github.com/huggingface/transformers/pull/35296；assisted decoding multi-GPU PR #35116，
  https://github.com/huggingface/transformers/pull/35116。
- **Related Primary Sources:** release-linked attention refactor #35235、candidate-generator refactor #35009、assisted-generation pipeline #34504
  与各新增 model/quantization source families；它们不因进入同一 release bundle 而合并成一个机制结论。
- **Access and Verification Status:** Verified as version bundle；Release全文与可访问的 security/multi-GPU PR可核验，部分 linked PR页面超时，
  因而只记录 Release明确行为，不推断不可访问 code details。
- **Full-read Coverage:** new-model/quantization roster、VLM cleanup、conversion-script packaging、Nougat regex、Whisper decoding contract、attention
  abstraction、assisted-generation API/multi-GPU device fix 与 bugfix list。
- **Original Problem:** 快速增加 model/backend 后，模型内重复 attention implementations、conversion utilities、generation device/state 与输出 contract
  容易漂移；单个 release同时承担 feature adoption、compatibility、security packaging和breaking changes。
- **Why the Previous Design Was Reasonable:** model-local attention与conversion script让新架构可独立落地、便于从原作者 checkpoint迁移；
  candidate generation和device handling最初针对单设备路径，代码简单且符合早期 workload。
- **Changed Constraint:** 模型数量、SDPA/FlashAttention backend、多 GPU placement、speculative/assisted generation与供应链扫描共同扩张，
  需要共享抽象、明确 device ownership并缩小分发包攻击/合规 surface。
- **Mechanism:** Release将 backend-specific attention definitions移到公共层、保留 model attention owner；assisted decoding显式在 assistant/target
  device间移动 inputs并重构 candidate generator；release tooling从 wheel/release branch排除会读取 pickle/旧 `.bin` 的 conversion scripts。
- **State Ownership:** model file拥有 architecture-specific attention；common abstraction拥有 backend dispatch；assistant/target model各自拥有device/cache state；
  release manifest拥有 wheel内容；conversion script仍在 main供开发者显式使用，不属于 runtime import path。
- **Control Flow / Data Flow:** model/config → common attention backend + model-local semantics → generation/candidate state → device placement → target verify；
  source tree → release tooling filter → wheel manifest；这两条路径是同版独立机制，不应混成一个性能结论。
- **Implementation Details:** v4.48.0新增多类 text/vision/audio/multimodal models、VPTQ/HIGGS adapters；统一 Whisper short/long-form部分返回语义；
  conversion scripts从 release wheels删除但留在 main；multi-GPU fix针对 assistant/target不同device的input movement。
- **Evaluation Setup:** Release/PR tests与CI证明合并/发布状态；没有统一跨模型 benchmark。PR #35116作者明确指出 multi-GPU generation/cache tests仍少，
  这是测试覆盖边界而非性能证明。
- **Baselines / Ablations / Sensitivity / Overhead:** `Not Applicable / Not Disclosed` 作为综合 release；新增模型论文各自拥有实验，Release本身未做统一
  baseline、ablation、latency、memory或security exploit evaluation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 涉及多 GPU、Whisper short/long、quantization/model integrations，
  但 release不提供统一 hardware/model/precision/length/batch/concurrency/SLO contract。
- **What the Evidence Actually Proves:** v4.48.0确实发布了上述API/packaging/refactor行为；它显示通用 model framework在规模增长后需将
  architecture semantics、backend dispatch、generation state与release artifact boundary分开管理。
- **What It Does Not Prove:** 版本支持某模型不证明该模型论文主张；attention refactor不自动带来性能提升；删除 wheel内conversion scripts不证明
  所有 checkpoint supply-chain风险消失，multi-GPU fix也不证明所有 cache/generation组合正确。
- **Limitations / Threats to Validity:** release内容是异构 bundle，缺统一 workload/evaluation；部分 linked PR页面本次不可访问；breaking output semantics
  可能影响 downstream，release notes不能替代用户侧 compatibility tests。
- **Trade-offs / New Failure Modes:** 共享 attention layer减少重复与漂移，却提高公共抽象blast radius；device ownership显式化支持多GPU但增加transfer/cache
  mismatch；移除 conversion scripts缩小wheel surface，却把迁移工作推回开发者从 main获取并自行隔离。
- **Where the Previous Design Still Applies:** 实验性模型或独特kernel可先用model-local实现；受控离线转换仍需要脚本但应在sandbox处理不可信checkpoint；
  单设备生成无需复杂placement逻辑。
- **Evolution Relationship:** `Layering / Dependency`：model-local integration → shared backend contract；single-device candidate path → explicit
  assistant/target placement；source-complete wheel → capability-minimized release artifact。
- **ROADMAP Node:** `PLATFORM-MODEL-MANAGEMENT`（Ch58）主 owner；Ch49接 execution/backend abstraction，Ch48接 assisted decoding，
  Ch70接 supply-chain security。
- **Target and Adjacent Chapters Read:** 已核对 Ch48～50、Ch57～60 与 Ch69～71 的 execution、artifact、serving与security边界。
- **Existing Coverage:** Books已有 model artifact、backend dispatch与supply-chain原则；单个 release bundle不形成独立长期机制缺口。
- **Integration Decision:** `Weekly Only — Version Bundle`；Books Integration Deferred，且当前不建议仅因版本升级修改正文。
- **Changed Files or Rejection Reason:** 仅更新 W02；新增模型/量化算法回到各自 primary source family，不复制 release marketing摘要。
- **Open Questions:** common attention abstraction如何做跨backend conformance；multi-GPU cache/device组合的integration matrix何时闭合；
  conversion tooling如何以隔离、签名与provenance形式重新分发。

### Transformer-Squared / Self-adaptive LLMs

- **Candidate / Week / Score:** Transformer-Squared / Self-adaptive LLMs / 2025-W02 / 26/30。
- **Source Family ID:** `transformer-squared-self-adaptive-svf`。
- **Source Type:** arXiv primary research paper + official author implementation。
- **First-public Date / Revision History:** arXiv v1 2025-01-09；v2 2025-01-14；v3 2025-01-24。事件归属按 v1；本次以 v1 正文审计，后续版本只用于 revision identity。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06252v1；arXiv metadata，https://arxiv.org/abs/2501.06252；官方仓库，https://github.com/SakanaAI/self-adaptive-llms。
- **Related Primary Sources:** 仓库内 `svd_reinforce_hydra.py`、policy、task/evaluation 与 training/evaluation scripts；LoRA、IA3、DoRA 只作为论文定义的 baseline family。
- **Access and Verification Status:** Verified；v1 method、实验、ablation、appendix、efficiency discussion 与官方 artifact 可访问。
- **Full-read Coverage:** Abstract/Introduction、related PEFT/SVD work、SVD/CEM preliminaries、SVF 与三种 self-adaptation、RL objective、实验设置和结果、dispatch analysis、module/objective/parameterization ablation、cross-model transfer、few-shot sensitivity、efficiency appendix、limitations 与 repository usage均已核对。
- **Original Problem:** conventional fine-tuning把一个固定权重版本绑定到一个任务；当部署请求跨域变化时，要么维护大量 adapter/model replicas，要么依赖 prompt 临时诱导，缺少可组合、可回滚的参数级 adaptation state。
- **Why the Previous Design Was Reasonable:** full fine-tuning适合稳定、高价值任务；LoRA等低秩增量把 base冻结、成本与版本blast radius可控；prompt routing不改权重，最易部署。在任务先验稳定、样本充分或低延迟优先时，这些方案仍合理。
- **Changed Constraint:** 论文假设测试任务可能未在训练时准确枚举，但可从少量 prompt/few-shot evidence判断其属性；同时希望直接按可验证 task reward优化、只保存小型 expert state，并在推理时组合而非为每个任务训练完整模型。
- **Mechanism:** 对每个被适配权重做 $W=U\Sigma V^T$，冻结 $U,V,\Sigma$，只学习缩放全部 singular components 的向量 $z$，形成 $W'=U(\Sigma\odot\mathrm{diag}(z))V^T$；用带 KL penalty 的 REINFORCE 从 correctness reward训练 task expert。推理时用 prompt dispatch、classification expert或基于 held-out few-shot的 CEM 搜索来选择/线性组合多个 $z$，第二遍再以适配后的权重回答。
- **State Ownership:** base artifact拥有 $U,\Sigma,V$ 与 tokenizer；每个 task expert artifact拥有 versioned $z$、训练任务、reward/evaluator与 base compatibility；dispatcher/CEM拥有本请求的 mixture coefficients；serving replica拥有当前 materialized weights/cache；第一遍输出只是 selection evidence，不是真值。
- **Control Flow / Data Flow:** task data + executable/categorical reward → SVF/REINFORCE → versioned expert vectors → request/few-shot evidence → first-pass dispatch或 CEM → mixture coefficients → materialize/activate $W'$ → second-pass generation → evaluator/telemetry。切换 expert必须与 request/cache边界一致。
- **Implementation Details:** SVF使用 AdamW、learning rate $2\times10^{-3}$、global batch 256、gradient clipping与按验证集选择 KL coefficient；Llama3-70B及vision实验只改一半 layers以控内存。few-shot主设置保留10个样本、最多100轮 CEM；官方仓库公开训练、prompt/classifier/few-shot evaluation scripts与 FishFarm evaluator fork。
- **Evaluation Setup:** 训练 tasks为 GSM8K、MBPP-Pro、ARC-Easy、TextVQA，unseen测试含 MATH、HumanEval、ARC-Challenge及 VLM setting；base覆盖 Llama3-8B-Instruct、Mistral-7B-Instruct-v0.3、Llama3-70B-Instruct。比较 frozen base、LoRA、SVF以及三种 Transformer-Squared adaptation，并报告 dispatch matrix、two-pass时间和跨模型 transfer。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 LoRA、IA3、DoRA比较；消融 attention/MLP/both、REINFORCE vs next-token、SVF vs LoRA+RL、ordered vs shuffled singular values、3/5/10/20-shot与 CEM-light。第一遍对整套 MATH/HumanEval/ARC-C 分别约为第二遍耗时的13%/19%/47%；这是论文特定集合总时长，不是 per-request production SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型和训练 batch已披露；GPU型号、precision、序列长度、online batch/concurrency与 production SLO为 `Not Disclosed`。70B/vision只改半数 layers且作者明确受 GPU resources限制。
- **What the Evidence Actually Proves:** 在作者任务、base、reward与选择协议下，全秩 singular-value scaling能以少量可组合参数训练 expert；增加可靠 test-time task evidence后，三种 adaptation通常优于 frozen base和其 LoRA配置；two-pass与 CEM开销可测且不是零。
- **What It Does Not Prove:** 不证明任意未知任务都能被有限 expert span表示，不证明 dispatcher在开放世界可靠，不证明在线改权重可与 continuous batching/KV reuse安全共存，也不证明优于所有 PEFT训练预算、所有 RL算法或 production router。
- **Limitations / Threats to Validity:** expert能力受 base latent components限制；弱 base会产生 sparse reward；expert数量增大使 CEM一次性搜索成本增长；few-shot以小 held-out subset选最优配置，仍有 selection bias；硬件/precision/concurrency未披露，跨模型 transfer并不稳定改善。
- **Trade-offs / New Failure Modes:** 参数state小、可组合且可直接优化任务reward，但增加 base-expert compatibility、dispatcher误路由、mixture interference、weight materialization、cache invalidation、双遍延迟与回滚责任；错误 evaluator会把 reward hacking固化进 expert。
- **Where the Previous Design Still Applies:** 固定任务、高吞吐或严格单遍 latency继续适合静态 SFT/LoRA；只有少量请求且任务语义清楚时 prompt/context adaptation更简单；需要新增 base中不存在的知识时，单纯缩放 singular components不够。
- **Evolution Relationship:** `Alternative Branch`：static adapter per task → reusable singular-value experts → request-conditioned selection/composition；它不是 LoRA的普遍替代，而是用更强 online state/control换取适应性。
- **ROADMAP Node:** `TRAIN-LORA`（Ch30）主 owner；handoff `PLATFORM-MODEL-MANAGEMENT`（Ch58）、`INFER-TENSORRT-LLM`（Ch49）与 `INFER-SCHEDULING`（Ch56）。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～31 的 SFT/LoRA/RL边界、Ch49 的 execution plan、Ch56 的 request state/scheduling与 Ch57～59 的 artifact/version contract。
- **Existing Coverage:** Books已有 static PEFT与 model artifact原则，但“可组合 expert + online dispatcher + weight/cache consistency”应作为后续 Books Gate的候选；本轮不实施。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅修复 W02 owner、全文 Source Review、评分与年度 ledger；不修改 Books。
- **Open Questions:** expert数量扩大后如何分层检索而非全量 CEM；mixture权重、materialized weights与 KV cache如何共同命名；dispatcher不确定性、reward verifier偏差与跨租户 expert隔离怎样进入 release gate。

### Tensor Product Attention / T6

- **Candidate / Week / Score:** Tensor Product Attention / T6 / 2025-W02 / 28/30。
- **Source Family ID:** `tensor-product-attention-t6`。
- **Source Type:** arXiv primary architecture/systems paper + official author implementation。
- **First-public Date / Revision History:** arXiv v1 2025-01-11；2025-02～2026-01存在 v2～v7，后获 NeurIPS 2025 Spotlight。事件归属与机制审计以 v1 为准；后续版本不倒灌成 W02新事件。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06425v1；metadata/revision，https://arxiv.org/abs/2501.06425；官方 repository（旧 T6 URL现指向 TPA），https://github.com/tensorgi/TPA。
- **Related Primary Sources:** 仓库公开 model/config/data/decode/pretrain/evaluation paths；MHA、MQA、GQA、MLA与 RoPE作为论文直接比较/依赖。
- **Access and Verification Status:** Verified；v1 method、定理/证明、cache accounting、训练与 evaluation appendix、learning-rate ablation及 artifact均可访问。
- **Full-read Coverage:** Abstract/Introduction、MHA/MQA/GQA/RoPE/MLA background、contextual tensor factorization、RoPE compatibility proof、factorized KV cache、non-contextual equivalence、variants/T6 architecture、FineWeb-Edu实验、所有规模/benchmark表、appendix硬件/超参、learning-rate ablation、related work、conclusion与 repository结构均已核对。
- **Original Problem:** autoregressive MHA为每个 token、layer、head保存完整 K/V，cache随 context线性增长；MQA/GQA通过共享 head降内存却压缩表达分支，eviction/offload又引入信息丢失或 I/O latency。
- **Why the Previous Design Was Reasonable:** MHA给每个 head独立 K/V，表达灵活且 kernel成熟；MQA/GQA以静态 sharing换取简单、确定的 cache layout和 production效率；post-hoc eviction/offload无需重新训练架构。短上下文、成熟 kernel或已有 checkpoint场景下它们仍合理。
- **Changed Constraint:** 长上下文与并发使 per-token cache成为容量/SLO瓶颈，同时模型仍希望保留 token-conditioned head structure并兼容 RoPE；这要求压缩被缓存的表示本身，而不只是删 token或搬 tier。
- **Mechanism:** 对每个 token的 Q/K/V activation按 rank $R$分解为 head factor $A(x_t)$ 与 token-dimension factor $B(x_t)$的 tensor-product sum；RoPE只旋转 Q/K的 $B$ factor并保持相对位置性质。decode不缓存完整 $h\times d_h$ K/V，而缓存 $A_K,B_K,A_V,B_V$，每 token元素量从 $2hd_h$变为 $(R_K+R_V)(h+d_h)$；T6在 LLaMA式 block中以 TPA替换 attention。
- **State Ownership:** trained architecture/checkpoint拥有 factor ranks与 projection weights；每个 request/layer/token的 KV state由 factorized A/B tensors拥有；position owner对缓存的 key-B应用 RoPE；runtime kernel负责按相同 rank/schema重建或直接计算，不得把 TPA cache与 MHA/GQA cache同名复用。
- **Control Flow / Data Flow:** hidden state → A/B projections → RoPE on query/key B → contextual tensor-product Q/K/V → attention → output；prefill/decode将 factorized K/V按 architecture/rank/position identity提交到 cache，后续 token读取并参与 attention。
- **Implementation Details:** v1默认 $d_h=64$，TPA/TPA-KVonly使用 $R_K=R_V=2, R_Q=6$；提供 full TPA、KV-only、shared-B与 non-contextual variants。官方仓库含 pretraining、model、decode与 lm-evaluation-harness paths，但 production serving integration不是论文artifact范围。
- **Evaluation Setup:** 在 FineWeb-Edu-100B上训练约124M、353M、772/773M parameter models，调各 attention head数以匹配 MHA每层约 $4d_{model}^2$参数；AdamW、cosine、2000 warmup、global batch 480，约49B tokens后比较 train/validation loss、perplexity与 ARC/BoolQ/HellaSwag/OBQA/PIQA/WinoGrande/MMLU/SciQ的0/2-shot结果。
- **Baselines / Ablations / Sensitivity / Overhead:** baseline为 parameter-matched MHA、MQA、GQA、MLA；比较 full TPA、TPA-KVonly、small/medium/large scales与 learning-rate sensitivity。论文给出理论 cache ratio和质量结果，但未给生产 kernel latency、memory-bandwidth utilization、reconstruction overhead或 end-to-end concurrency/SLO ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** small 124M用4×A100、micro-batch 24/GAS5；medium 353M用8×A100、20/GAS3；large 772M用8×A100、15/GAS4；global batch 480。precision、训练/评测 sequence length、serving batch/concurrency与 SLO为 `Not Disclosed`。
- **What the Evidence Actually Proves:** v1给出 factorized cache的精确元素量与 RoPE兼容证明；在作者 parameter-matched、约49B-token、最高约773M设置中，TPA/TPA-KVonly通常达到更低 loss/perplexity与略高平均下游分数，并按选定 ranks将理论 KV元素量降约5～10倍。
- **What It Does Not Prove:** 不证明10× device-memory reduction会等价为10× throughput/最大并发；不证明可无训练替换现有 MHA/GQA checkpoint；不证明长上下文质量、production latency、kernel成熟度或在更大模型/不同数据/precision上普遍优于 MLA/GQA。
- **Limitations / Threats to Validity:** 结果限于单一 pretraining corpus、sub-billion scales与作者实现；head数为参数匹配而非完全相同 topology；precision/sequence length/SLO未披露；v1没有明确独立 limitations section，生产 decode overhead与 ecosystem support需外部复现。
- **Trade-offs / New Failure Modes:** cache更小且保留 contextual head factors，但把压缩从 runtime policy提升为 model architecture contract；增加 rank选择、factor projection/reconstruction kernel、cache schema/versioning与 checkpoint不可互换风险。rank过小损伤表达，rank过大吞噬节省；不匹配 RoPE/rank会静默破坏 attention。
- **Where the Previous Design Still Applies:** 已训练 MHA/GQA模型、短 context、算力而非 HBM受限、或依赖高度优化 FlashAttention/PagedAttention kernel时继续优先原方案；eviction/offload仍适合无需重训且可容忍其信息/I/O代价的系统。
- **Evolution Relationship:** `Alternative Branch`：full per-head KV → static head sharing/latent compression → contextual factorized activation cache；与 paging/tiering是 `Layering / Dependency`，可组合但解决不同层次的问题。
- **ROADMAP Node:** `INFER-KV-CACHE`（Ch45）主 owner；handoff `MODEL-SELF-ATTENTION`（Ch14）、`MODEL-LONG-CONTEXT`（Ch22）、`INFER-PAGED-ATTENTION`（Ch47）与 `INFER-TENSORRT-LLM`（Ch49）。
- **Target and Adjacent Chapters Read:** 已核对 Ch14、Ch19～22、Ch43～49 的 attention、decode state、long-context、cache identity、paging与 execution边界。
- **Existing Coverage:** Books已有 GQA/MLA、KV cache、paging/tiering原则；TPA提供 architecture-native contextual factor cache证据，但是否进入正文需后续 Books Gate按 owner章节去重，本轮不实施。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅修复 W02 owner、全文 Source Review、评分与年度 ledger；不修改 Books。
- **Open Questions:** 在同等 quality与完整 serving workload下，factor reconstruction/attention kernel能否把 HBM节省转成 TTFT/TPOT/throughput收益；cache block如何携带 architecture/rank/RoPE schema；能否从已有 GQA/MLA checkpoint稳定迁移而不重新预训练。

### ChemAgent / Self-updating Library

- **Candidate / Week / Score:** ChemAgent / Self-updating Library / 2025-W02 / 27/30。
- **Source Family ID:** `chemagent-self-updating-library`。
- **Source Type:** arXiv primary Agent/memory research paper + official author code/data/memory artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-11；submission history仅 v1。Hugging Face 2025-01-14收录不改变 owner date。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06590v1；metadata，https://arxiv.org/abs/2501.06590；官方 repository，https://github.com/gersteinlab/chemagent。
- **Related Primary Sources:** repository公开 SciBench-derived datasets、few-shot examples、plan/execution memory、trajectory outputs、config 与 dev/test runner；SciBench与 StructChem作为 evaluation/baseline依赖。
- **Access and Verification Status:** Verified；method、algorithm、实验、self-evolution、cost/error analysis、ablation、appendix limitations/prompts与 artifact结构可访问。
- **Full-read Coverage:** Abstract/Introduction、三类memory与atomic decomposition、library construction/retrieval/update、evaluation/refinement、四数据集setup/results、runtime self-evolution、token/cost、failure taxonomy、component/quality/shot ablations、other-model results、limitations、prompts/cases及 repository运行契约均已核对。
- **Original Problem:** chemistry问题把公式、单位、代码计算和多步推理耦合；固定 CoT/structured prompt每次从头求解，无法把已验证的子问题、策略和错误修正沉淀为可复用状态，早期小错会沿轨迹放大。
- **Why the Previous Design Was Reasonable:** direct/CoT最少外部状态；few-shot+Python可显式计算；StructChem用固定结构与反思提高可解释性。任务量小、知识变化快或 memory治理成本高时，无持久状态方案更简单且污染面更小。
- **Changed Constraint:** 重复处理同域问题时，许多 sub-task、公式与 plan可复用；同时不同问题只在关键条件上细微差异，系统需要可检索经验又不能把语义相似误当物理/化学等价，还要在运行中纠错和更新。
- **Mechanism:** 将 development solutions分解为带 condition、query、solution/guidance的 atomic units；持久保存 high-level Planning Memory与具体 Execution Memory，临时生成 Knowledge Memory。新任务先分解，用 Llama3 embeddings按阈值检索，逐 sub-task求解；evaluator检查知识/单位/目标一致性并触发 solution refinement或后续 plan重构；只有正确结果的 plan/execution units进入后续 runtime library。
- **State Ownership:** development corpus/ground truth拥有初始 evidence；Planning/Execution Memory分别拥有长期策略与条件化执行单元；Knowledge Memory是请求期临时状态，不应跨请求直接持久化；retriever拥有 candidate ranking；evaluator提出 correctness/update决策；library writer拥有 append/version/provenance。生成者本身不应兼任不可审计真值源。
- **Control Flow / Data Flow:** dev problem+solution → condition parse/verify → hierarchical sub-task/solution extraction → rank/filter → versioned library；test problem → decomposition → memory retrieval → sub-solution/code → knowledge/evaluator check → refine/replan → final answer → ground-truth correctness gate → append plan/execution memory → later requests。
- **Implementation Details:** reasoning最多检索2条 planning、4条 execution memory；cosine similarity基于 Llama3 embedding与阈值；accuracy使用0.01相对容差。官方仓库分离 memory/dataset/output/trajectory、dev与test modes，config可选择 base/evaluator model、temperature、timeout与 score/refine开关；README安装说明仍不完整。
- **Evaluation Setup:** SciBench的 QUAN、CHEMMC、ATKINS、MATTER按 dev/test切分；比较 GPT-4 `gpt-4-1106-preview`的 direct、few-shot+Python、StructChem、ChemAgent及去除memory/evaluate-refine variants，并在 Llama3.1-7B/70B、Qwen2.5-72B报告 additional results。self-evolution仅在 MATTER、去除 evaluate/refine后迭代测量并排除同题历史以减 leakage。
- **Baselines / Ablations / Sensitivity / Overhead:** 消融 Planning/Execution/Knowledge Memory、memory source quality（GPT-3.5/GPT-4/hybrid）、检索条数与 evaluate/refine。论文报告 GPT-4平均47.66→57.16相对 StructChem、无 evaluate/refine约12k tokens/$0.09、完整约23k tokens/$0.1725；library construction成本被排除，价格绑定当时 API且不代表当前成本/SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base/evaluator model与平均 token/cost部分披露；GPU、precision、per-request input/output split、batch、concurrency、latency percentile与 production SLO为 `Not Disclosed`。闭源 GPT结果还受服务版本变化影响。
- **What the Evidence Actually Proves:** 在四个 SciBench化学子集与作者协议下，结构化分解、可检索memory和 evaluator/refinement组合通常提高最终答案accuracy；memory quality、检索数量与关键条件错配会实质影响结果；正确性门控后的持续积累在 MATTER实验中呈改善趋势。
- **What It Does Not Prove:** 不证明 memory会单调改善、不证明 cosine相似能判断因果/条件等价、不证明“correct final answer”足以验证中间轨迹，也不证明该框架可安全用于 drug discovery、真实实验或开放世界持续学习。
- **Limitations / Threats to Validity:** dev/test来自同一 benchmark family且 dynamic memory仍用 test-stage correctness信号；closed-model版本、prompt和 evaluator耦合；initial library成本未计；规模实验有限，authors未验证更大 memory；官方 error analysis已观察错误理解、错误规划与高相似误检。
- **Trade-offs / New Failure Modes:** 将历史转成可复用typed state提高 sample efficiency与可审计性，却增加 provenance、supersession、contradiction、delete/rollback与租户隔离；更多memory可能提高均值同时增大方差；混合不同质量memory会混淆模型；错误 evaluator会把污染写回长期库。
- **Where the Previous Design Still Applies:** 一次性问题、低延迟、无可信 verifier、受监管知识必须由专家批准或跨域 drift很大时，stateless structured reasoning/curated RAG更安全；高质量人工 examples在窄域甚至可优于自动生成memory。
- **Evolution Relationship:** `Direct Evolution`：stateless structured reasoning → retrieved solved examples → typed planning/execution memory → correctness-gated derived memory；不是 parametric learning，也不能与 Agent conversation history等同。
- **ROADMAP Node:** `AGENT-MEMORY`（Ch77）主 owner；handoff `AGENT-CONTEXT`（Ch75）、`AGENT-RAG`（Ch76）、`AGENT-WORKFLOW`（Ch81）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch66、Ch74～78、Ch80～81 的 evidence、context/RAG/memory、reflection与 workflow state边界。
- **Existing Coverage:** Books已有 memory provenance、derived memory与 workflow checkpoint原则；本 family可补充“temporary knowledge vs persistent plan/execution”及 write gate的演进案例，但需留待 Books Integration Gate去重。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅修复 W02 owner、全文 Source Review、评分与年度 ledger；不修改 Books。
- **Open Questions:** final-answer correctness何时足以批准中间步骤；memory unit如何携带condition、source、evaluator、expiry与supersession；如何用 contradiction-aware retrieval、quarantine与 shadow evaluation阻止错误经验扩散。

### MinMo

- **Candidate / Week / Score:** MinMo / 2025-W02 / 28/30。
- **Source Family ID:** `minmo-aligned-duplex-speech-model`。
- **Source Type:** arXiv primary model/system report；v1 声明 code/models 将发布，事件时没有可核验实现 artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；仅 v1；Hugging Face 01-14 收录不改变 owner week。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06282v1；metadata，https://arxiv.org/abs/2501.06282。
- **Related Primary Sources:** 论文明确依赖 Qwen2.5-7B-Instruct、SenseVoice-Large 与 CosyVoice2；只用其公开接口解释 layering，不把相关项目结果并入 MinMo 证据。
- **Access and Verification Status:** Verified as author report；method、training stages、evaluation、latency decomposition 与 limitations 可读；事件时 code/model availability 未验证。
- **Full-read Coverage:** 已读 Introduction/related work、architecture、streaming decoder、data、四阶段训练、全部 speech understanding/generation/chat evaluation、duplex latency、结论、limitations 与 prompts appendix。
- **Original Problem:** cascaded ASR→LLM→TTS 丢失 paralinguistic state并累积延迟；native speech-text decoder又承受 speech/text 序列长度差、数据失衡与 text knowledge forgetting。
- **Why the Previous Design Was Reasonable:** cascade 可独立替换组件、错误边界清楚；native token stream 则统一训练/生成语义。语音数据有限、模块需独立合规或 turn-based latency 可接受时，两者仍合理。
- **Changed Constraint:** 系统要在保留 text LLM 能力的同时完成 streaming speech input/output、style control、user interruption 与 simultaneous listen/speak；control state 不能只在回合结束后更新。
- **Mechanism:** 在 Qwen2.5-7B 上连接 pretrained voice encoder/input projector；将每 5 个 text semantic vectors 与 15 个 speech tokens 交错输入 AR Voice Token LM，再由 chunk-aware flow/vocoder 输出；独立 duplex predictor持续判定 listen/speak/concede。
- **State Ownership:** text LLM拥有 linguistic state；voice encoder/projector拥有 acoustic observation；Voice Token LM 与 Token2wav拥有生成 state；duplex predictor拥有 turn-control decision；session runtime必须原子提交 interruption、discard/continue 与 output buffer状态。
- **Control Flow / Data Flow:** streaming audio → encoder/projector → text LLM → text token/hidden state → 5:15 semantic/speech-token interleave → chunk synthesis；并行 duplex predictor读取会话音频与上下文，触发 continue、concede或重新回答。
- **Implementation Details:** 总计约8B；voice encoder约636M、input projector约170M、voice LM约370M、duplex predictor约18M；依次进行 speech-to-text、text-to-speech、speech-to-speech、duplex alignment，text LLM只做 LoRA update。
- **Evaluation Setup:** 覆盖 ASR、translation、language/emotion/audio-event/speaker understanding、speech enhancement、TTS/style control、speech QA/dialogue 与 duplex prediction；数据表合计约1.4M小时，多项 closed/open baseline按各自指标比较。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 Whisper、Qwen2-Audio、SeamlessM4T、Moshi、Freeze-Omni、GLM-4-Voice等任务级比较；作者给出模块 latency decomposition，但没有统一端到端 ablation、负载敏感性或多并发测试。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** latency表使用两张 L20，分解为 predictor 250ms、speech-to-text 95/150ms、speech token 70ms、Token2wav 130ms；约600ms theoretical、800ms practical。precision、batch、并发、音频长度分布与 percentile SLO 未披露。
- **What the Evidence Actually Proves:** 在作者数据与模型组合中，staged alignment可获得广泛 speech task能力且维持大部分 text benchmark；AR streaming decoder和显式 turn predictor形成可测的 duplex pipeline。
- **What It Does Not Prove:** 不证明在开放噪声、多人重叠语音或生产并发下达到同样 latency/quality；不证明 aligned architecture普遍优于 native或cascade；作者 benchmark不等于真实对话安全性。
- **Limitations / Threats to Validity:** 作者承认 LoRA后的 instruction following仍需改进，且一对多 token与特殊符号造成长尾发音错误；大量自建/合成数据、closed baselines与缺少 artifact限制复现。
- **Trade-offs / New Failure Modes:** 保留 text backbone并分离 acoustic modules降低 catastrophic forgetting，却引入跨模块时间对齐、5:15 ratio、interruption race、stale audio/output buffer与 duplex false-positive/false-negative；更多 stage也增加数据/版本耦合。
- **Where the Previous Design Still Applies:** 合规要求独立 ASR/TTS、组件需快速替换、低并发 turn-based助手或可容忍更高 latency时，cascade更易审计；充足原生 multimodal data且接受重训时，native stream仍是可行分支。
- **Evolution Relationship:** `Alternative Branch`：cascade components ↔ native unified token stream ↔ aligned text backbone + typed speech modules + duplex controller；不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`TRAIN-PRETRAINING`（Ch28）、`INFER-REQUEST-LIFECYCLE`（Ch42）与 `INFER-SCHEDULING`（Ch56）。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～24、Ch27～30、Ch42～45 与 Ch55～56 的 modality identity、training stage、request state与 scheduling边界。
- **Existing Coverage:** Books已有 modality encoder/fusion与 streaming request state原则；MinMo提供 speech duplex control的完整受限案例，是否写入需后续 Books Gate去重。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅回拨 W02、补评分和 Full Source Review；不修改 Books。
- **Open Questions:** duplex predictor错误如何绑定安全回退；interruption时已生成 text/speech/KV如何一致撤销；audio chunk identity、jitter、backpressure与跨租户 isolation如何进入 serving contract。

### O1 Replication Journey Part 3

- **Candidate / Week / Score:** O1 Replication Journey Part 3 / 2025-W02 / 24/30。
- **Source Family ID:** `o1-replication-medical-inference-scaling`。
- **Source Type:** arXiv primary empirical research paper；无事件时官方代码/数据 artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-11；仅 v1；01-14 discovery页面不改变归属。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06458v1；metadata，https://arxiv.org/abs/2501.06458。
- **Related Primary Sources:** JAMA Clinical Challenge、Medbullets、MedQA为任务来源；o1-preview仅为 distilled journey data teacher，不能据此推断其内部 chain-of-thought。
- **Access and Verification Status:** Verified；全文、table、cases与 appendix可读；缺 code/data release，复现边界明确。
- **Full-read Coverage:** 已读 Introduction、benchmark selection、journey data synthesis、implementation、main results、length/difficulty analysis、generalization、conclusion与全部 failure cases appendix；论文无独立 limitations section。
- **Original Problem:** 单纯扩大模型或使用短 CoT不保证复杂医学问题得到更充分的 evidence integration；同时 proprietary reasoning不可直接审计，公开模型缺少长轨迹训练证据。
- **Why the Previous Design Was Reasonable:** direct answer和short CoT成本低、误差链短；domain model/pretraining直接补知识。在题目简单、知识不足或严苛 latency下，延长推理并非首选。
- **Changed Constraint:** benchmark包含更复杂病例与专业知识，作者希望用可见的 long-step/long-monologue traces测试“更多 inference tokens”是否在有知识前提下带来收益。
- **Mechanism:** 用 o1-preview生成并扩展 long-step/long-monologue supervised traces，微调 Qwen2.5-32B/72B与 Llama3.1-70B；推理时不做 tree search或 verifier，而让模型输出更长自反思轨迹。
- **State Ownership:** teacher输出拥有未公开的 synthetic rationale provenance；training dataset拥有 long-trace labels；model parameters内化策略；request runtime拥有 token budget与generated trace；最终答案 evaluator只拥有 exam accuracy，不拥有临床真值。
- **Control Flow / Data Flow:** selected medical question → teacher-generated long trace → preprocessing/SFT → open model → longer sequential generation → multiple-choice accuracy与 token-length analysis；没有在线搜索、external tool或 verifier loop。
- **Implementation Details:** 研究分 LongStep 与 LongMonolog两种 trace；作者明确目标是评估而非执行真实 differential diagnosis；选取 o1-mini困难样本引入 difficulty-selection bias。
- **Evaluation Setup:** JAMA 1,524 cases、Medbullets与MedQA；比较 direct、vanilla CoT、LongStep、LongMonolog及多个 7B～72B model；指标为 accuracy与 average output tokens。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比不同 model size、reasoning style、dataset difficulty和输出长度；没有等 compute/token budget的 search/verifier baseline、SFT data-size ablation、calibration或 clinical expert blind review。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models与约300～1,100 output tokens披露；训练/推理硬件、precision、input length、batch、concurrency、latency与SLO均 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者选取与蒸馏协议下，部分较大模型的长轨迹 SFT与更长输出相关并提高三项考试 accuracy；困难任务通常产生更长轨迹，LongStep/LongMonolog优劣依数据而异。
- **What It Does Not Prove:** 不证明输出越长越正确、不证明因果收益来自 inference compute而非 teacher data/selection、不证明适用于临床诊断，也不证明 proprietary o1机制被复制。
- **Limitations / Threats to Validity:** teacher distillation、困难样本筛选与答案泄漏风险；多选题accuracy弱化临床安全；无独立limitations、code和hardware；作者案例显示冗余反思可使弱模型迷失并答错。
- **Trade-offs / New Failure Modes:** 更长轨迹提供复核空间但线性增加token cost/latency，扩大 hallucination与错误自洽面；知识不足时“思考更久”会放大 confusion而非创造知识。
- **Where the Previous Design Still Applies:** 容易题、低延迟、高并发、知识缺口主导或需结构化 clinical guideline时，短推理、retrieval/tool和human review更适合；long trace只是一条条件分支。
- **Evolution Relationship:** `Alternative Branch`：direct/short CoT → long-trace distillation → test-time search/verifier（后续 family）；本论文只覆盖中间分支，不能代表完整 inference-time scaling。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；handoff `MODEL-SCALING-LAWS`（Ch8）、`TRAIN-RLHF`（Ch31）、`INFER-SCHEDULING`（Ch56）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch28～34、Ch52～56 与 Ch65～67 的 data/objective、test-time compute、SLO与 executable evaluation边界。
- **Existing Coverage:** Books已有“token budget不等于有效推理”及 verifier/evaluator边界；该 family可作为 domain-knowledge gating案例，待 Books Gate决定是否已有充分覆盖。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅回拨 W02并补 Source Review；不修改 Books。
- **Open Questions:** 如何用等token/等延迟比较 long trace、best-of-N、tree search与retrieval；怎样测 calibration、unsafe rationale与真实clinical outcome；teacher-derived traces如何治理 provenance与 contamination。

### VideoAuteur

- **Candidate / Week / Score:** VideoAuteur / 2025-W02 / 25/30。
- **Source Family ID:** `videoauteur-long-narrative-video`。
- **Source Type:** arXiv primary multimodal generation research paper；project/data/model availability按事件时公开范围处理。
- **First-public Date / Revision History:** arXiv v1 2025-01-10；后续 revision不改变 W02 owner。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06173v1；metadata，https://arxiv.org/abs/2501.06173。
- **Related Primary Sources:** CookGen由 YouCook2/HowTo100M筛选构建；SEED-X、EMU-2、SDXL、FLUX与I2V backbone只作为组件/baseline，不合并为同一 source family。
- **Access and Verification Status:** Verified；method、data pipeline、evaluation、ablation、implementation appendix与limitations可读。
- **Full-read Coverage:** 已读 Introduction/related work、CookGen采集/标注/过滤/逆生成验证、director两分支、visual-conditioned generation、loss/robustness、所有定量/人工评价、implementation、伪代码、示例与 limitations。
- **Original Problem:** 单 clip video model缺少跨多个步骤的 narrative state；只用文本或上一帧控制会在身份、动作顺序和视觉细节上漂移，且公开训练数据缺少 step-level action/caption/state对齐。
- **Why the Previous Design Was Reasonable:** independent clip和I2V pipeline结构简单、可用成熟backbone；短视频或允许scene reset时，局部质量比长期一致性更重要。
- **Changed Constraint:** 长教程/故事需要显式保存跨step的 action、caption与visual state，并把director输出的有噪latent传给生成器；continuity成为state contract而非单clip prompt问题。
- **Mechanism:** 先由 interleaved AR director按 history逐步生成 action→caption→visual embedding，或用 language-centric diffusion生成keyframe；再用持续 visual latent而非仅首帧条件化video model，并以noisy-latent adaptation提高对回归误差的鲁棒性。
- **State Ownership:** CookGen拥有 action/caption/clip alignment；director拥有 narrative history与next visual state；video generator拥有clip diffusion state；visual identity需由每步 latent与历史共同维持；ASR/action错误不能静默升级为 environment truth。
- **Control Flow / Data Flow:** raw cooking videos → caption/action extraction与temporal matching → aligned training tuples；user narrative → sequential action/caption/latent plan → per-step visual-conditioned clip generation → human/automatic continuity evaluation。
- **Implementation Details:** latent regression联合 cosine与MSE以保留方向和尺度；interleaved branch比较SEED-X/EMU-2，language branch比较SDXL/FLUX；generator训练加入 noisy visual embeddings。
- **Evaluation Setup:** CookGen源自30k+ raw videos；通过inverse generation、GPT-4o和6名human验证caption；比较latent/director策略、loss、keyframe vs visual embedding、noise augmentation，并用CLIP-T、FID/FVD与人工 aesthetic/realism/consistency/narrative评分。
- **Baselines / Ablations / Sensitivity / Overhead:** 有 MSE/cosine、director branch、latent family、conditioning与noise ablation；没有跨domain长视频、closed-loop action outcome、长期identity error accumulation随step数的系统曲线，也缺 serving cost/SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露组件与训练配置 appendix，但端到端hardware、precision、长序列step分布、batch/concurrency、生成latency和production SLO不完整，记为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在 cooking-domain与作者pipeline中，显式 action/caption/visual hierarchy及continuous latent conditioning提高若干生成/人工指标；latent direction和scale都重要，noisy-condition adaptation有用。
- **What It Does Not Prove:** 不证明生成器建立了causal world model、不证明视觉连续等于动作正确或物理可执行、不证明长视频任意扩展时不会累积漂移，也不证明一个director分支普遍胜出。
- **Limitations / Threats to Validity:** 作者承认ASR action noisy、场景局限于烹饪、生成存在identity与错误传播；GPT-4o评价非独立真值，部分backbone与数据处理复现成本高。
- **Trade-offs / New Failure Modes:** 分层state改善长程控制，却增加 action/caption/latent三层不一致、error propagation、teacher/evaluator bias与多stage版本耦合；逐clip生成还可能牺牲全局时间一致性。
- **Where the Previous Design Still Applies:** 短clip、广告镜头、允许人工keyframe或追求单帧质量时，independent T2V/I2V更简单；真实planning需action-conditioned simulator/physical feedback，不能由narrative video替代。
- **Evolution Relationship:** `Layering / Dependency`：independent clip → keyframe chain → typed narrative director + continuous visual state；到world model是后续约束变化，不是本论文已完成的Direct Evolution。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～27 与 Ch65～67 的representation、generation、world-state、data和evaluation边界。
- **Existing Coverage:** Books已区分video generation与world model；VideoAuteur补充“显式 narrative state”的受限演进案例，是否加入正文留待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅回拨 W02、补全文审计与 owner mapping；不修改 Books。
- **Open Questions:** step数增长时identity/causal error如何累积；action/caption/latent冲突由谁裁决；如何用可执行环境而非视觉偏好验证长期state；artifact是否能完整复现实验。

### SPAM

- **Candidate / Week / Score:** SPAM / 2025-W02 / 29/30。
- **Source Family ID:** `spam-spike-aware-adam`。
- **Source Type:** arXiv primary optimization/systems research paper + author code link。
- **First-public Date / Revision History:** arXiv v1 2025-01-12；v2 2025-02-28。owner与机制审计以v1为准。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06842v1；metadata，https://arxiv.org/abs/2501.06842；作者链接代码作为artifact boundary。
- **Related Primary Sources:** Adam/Adafactor、Adam-Mini、GaLore、momentum restart与architecture-level spike mitigation是论文baseline/演进依赖，不并作同一事件。
- **Access and Verification Status:** Verified；method、theory caveat、experiments、ablations、pseudocode、architecture/hyperparameters与appendix可读。
- **Full-read Coverage:** 已读gradient-spike观察/干预、preliminary regret analysis、moment reset、spike-aware clipping、sparse momentum、pretrain/SFT/QAT/RL/time-series/vision experiments、所有ablation、hyperparameters与limitations caveat。
- **Original Problem:** Adam的一次极大gradient会同时污染一阶/二阶moment，尤其二阶平方项与高decay使影响跨许多step残留；checkpoint rollback只处理结果，不修复optimizer-state机制。
- **Why the Previous Design Was Reasonable:** Adam用EMA平滑高方差gradient，gradient norm/value clipping简单成熟；正常分布、spike罕见或已有强监控/rollback时，持续moment提供稳定方向且无需新超参。
- **Changed Constraint:** 长时间、大规模训练使低频spike的累计代价很高；moment本身成为持久故障状态，且optimizer memory也限制规模，需要同时控制污染寿命和state容量。
- **Mechanism:** 定期清空一阶/二阶moment并做reset后cosine warmup；以当前gradient相对second-moment统计检测异常坐标并re-scale而保留方向；sparse variant仅维护抽样参数的moment，并在reset周期重新采样。
- **State Ownership:** optimizer拥有moment、reset interval、warmup phase、threshold与sparse mask；trainer拥有step/checkpoint；monitor拥有spike signal；恢复必须同时版本化model、optimizer、scheduler、mask与reset phase。
- **Control Flow / Data Flow:** gradients → spike detector/re-scaling → Adam update；每到 $\Delta T$ 清空moments、进入N-step warmup；sparse mode周期重采样mask。telemetry需关联spike、reset、loss与checkpoint。
- **Implementation Details:** 默认pretrain $\Delta T=500$、threshold 5000、warmup 150；不同规模/任务另设interval；60M～1B LLaMA在C4，另含7B SFT、QAT、RL、vision与time-series设置。
- **Evaluation Setup:** 以Adam、value/norm clip、Adafactor、architecture mitigation、Adam-Mini、GaLore等比较；报告perplexity/accuracy/reward/error与memory，部分SFT结果做10次重复。
- **Baselines / Ablations / Sensitivity / Overhead:** 消融moment reset、spike clipping、reset interval、warmup、threshold与sparse ratio；覆盖多任务但最大pretrain仅1B，且未给 wall-clock/communication/checkpoint overhead的完整production测量。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model、dataset和主要optimizer超参披露；GPU型号、precision、sequence length、global batch（各实验）、distributed topology、wall-clock/SLO并不完整，不能把质量差异外推成成本优势。
- **What the Evidence Actually Proves:** 在作者设置中，人工/观察spike会长期影响Adam moments；reset+targeted clipping通常改善所测训练结果，sparse momentum可降低optimizer state并保持部分质量。
- **What It Does Not Prove:** 不证明spike是所有大模型不稳定性的主要原因、不证明固定阈值/周期跨scale最佳，也不证明对大规模distributed training、不同precision或optimizer普遍优于现有恢复策略。
- **Limitations / Threats to Validity:** 理论分析明确限于convex-style假设且范围很窄；spike因果可能与data、overflow、normalization、collective error混杂；最大LLM scale有限，作者artifact与实验环境未覆盖生产故障。
- **Trade-offs / New Failure Modes:** 缩短污染寿命并降低state memory，却丢失长期moment信息、引入reset/warmup振荡、threshold误判与sparse-mask discontinuity；不一致恢复会让model与optimizer state语义错位。
- **Where the Previous Design Still Applies:** 训练平稳、规模较小、moment信号长期有用或已有可靠loss-scale/data filtering时，标准Adam+norm clip更简单；根因是坏数据/数值溢出时应先修复来源。
- **Evolution Relationship:** `Direct Evolution`：gradient clipping → persistent optimizer-state diagnosis → reset + spike-aware clipping → sparse/resettable moment；checkpoint rollback与它是`Layering / Dependency`。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Ch28）主 owner；handoff `TRAIN-CHECKPOINT`（Ch35）、`TRAIN-DISTRIBUTED-TRAINING`（Ch36）与 `PLATFORM-OBSERVABILITY`（Ch67）。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～29、Ch35～41 与 Ch66～68 的optimizer state、checkpoint completeness、distributed numerics与observability边界。
- **Existing Coverage:** Books已有loss spike、checkpoint与mixed-precision监控原则；SPAM提供“optimizer state也是故障持久层”的机制证据，待 Books Gate去重。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅回拨 W02并补 Full Source Review；不修改 Books。
- **Open Questions:** threshold如何随layer/precision/scale自适应；distributed shard间如何一致reset；sparse mask与ZeRO/checkpoint如何版本化；wall-clock与recovery saving何时抵消warmup代价。

### Grad-Mimic / Mimic Score

- **Candidate / Week / Score:** Grad-Mimic / Mimic Score / 2025-W02 / 29/30。
- **Source Family ID:** `grad-mimic-reference-weight-data-selection`。
- **Source Type:** arXiv primary data-selection research paper；本次以v1事件版本审计。
- **First-public Date / Revision History:** arXiv v1 2025-01-12；后续多次revision至2026，W02只记录v1已公开机制，后续结果不倒灌。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06708v1；metadata/revisions，https://arxiv.org/abs/2501.06708。
- **Related Primary Sources:** DataComp、GraNd、AGRA、Grad-Match与CLIP是dataset/baseline依赖；不把2026 conference metadata当作2025事件证据。
- **Access and Verification Status:** Verified；method、algorithm、experiments、training configs、ablation与limitations可读。
- **Full-read Coverage:** 已读Introduction/related work、Mimic Score推导、online reweight与offline filter两阶段、noise simulation、DataComp、quality estimation、algorithm、hardware/config、temperature/layer/aggregation ablations与limitations。
- **Original Problem:** web-scale filtering依赖手写规则、target validation set或昂贵influence估计；它们难以量化单样本对学习方向的贡献，也容易把domain heuristic当作普遍quality。
- **Why the Previous Design Was Reasonable:** heuristic filter便宜、可解释且无需reference model；validation/influence方法能直接对齐目标任务。没有可信reference权重、跨域偏移大或per-sample gradient太贵时，旧方案更稳妥。
- **Changed Constraint:** 公开pretrained weights可作为“更优参数区域”的弱目标；系统希望在训练中动态reweight，并把跨step utility汇总为可复用离线filter，而不依赖私有validation set。
- **Mechanism:** 令 $v_t=\theta_{ref}-\theta_t$，用每个样本负gradient在该方向上的投影定义mimic score；softmax temperature控制batch内权重并更新模型；跨step聚合score后用阈值/聚类等生成data filter与quality estimate。
- **State Ownership:** reference artifact拥有目标weight/version与layer选择；trainer拥有current weights和per-sample gradients；scorer拥有time-varying utility；aggregator拥有sample-level history/filter；dataset registry拥有最终keep/drop及provenance。
- **Control Flow / Data Flow:** sample batch → per-sample gradient → 与reference-direction对齐 → normalized weight → training update；score history → aggregation/threshold → versioned filter → next dataset/model run。reference变化必须生成新filter identity。
- **Implementation Details:** 可只比较last MLP layer降低开销；temperature调节selection sharpness；Stage 2支持threshold、aggregation与ensemble filter。算法仍需要per-sample gradient，不能把“无需validation data”误写成“零额外成本”。
- **Evaluation Setup:** 六个image classification数据集注入label noise；DataComp small/medium上从头训练CLIP，5 epochs、batch 4096、12.8M/128M seen samples；比较selection、noise detection、training performance与filter transfer。
- **Baselines / Ablations / Sensitivity / Overhead:** 与SGD、GraNd、AGRA、Grad-Match及DataComp filters比较；消融temperature、reference layer、aggregation和dataset scale；缺LLM-scale token filtering、reference bias stress test与完整per-sample gradient wall-clock accounting。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** DataComp使用8×NVIDIA A100、batch4096；CLIP规模与seen samples披露；precision、I/O、distributed gradient实现、wall-clock与production SLO不完整。
- **What the Evidence Actually Proves:** 在作者图像/CLIP设置中，reference-weight方向能区分部分噪声样本、改善训练或组合现有filter，并提供与dataset noise/quality相关的信号。
- **What It Does Not Prove:** 不证明reference model方向是全局最优、不证明适用于生成式LLM/长期curriculum，也不证明高mimic score等于无偏、无毒或有版权许可的数据。
- **Limitations / Threats to Validity:** 作者明确承认不可靠reference会筛出suboptimal dataset；实验集中图像与CLIP，per-sample gradient成本、reference/data leakage和domain shift可能影响结论。
- **Trade-offs / New Failure Modes:** 从静态heuristic转为model-relative utility，能细粒度选择却把reference偏见、版本与目标函数固化进filter；feedback loop可能减少多样性、放大shortcut，并增加gradient计算/存储。
- **Where the Previous Design Still Applies:** safety/legal规则、rare-event保留、无可信reference、跨域探索或需要明确人类policy时，heuristic/stratified/human filter仍不可替代；mimic score应作为一条signal而非唯一gate。
- **Evolution Relationship:** `Direct Evolution`：handcrafted/static filters → target-data influence → pretrained-weight direction → online reweight + offline versioned filter；与data governance是`Layering / Dependency`。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-PRETRAINING`（Ch28）、`PLATFORM-MODEL-MANAGEMENT`（Ch58）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～29、Ch57～59与Ch65～67的数据contract、artifact identity与evidence边界。
- **Existing Coverage:** Books已有quality signal、dedup/filter与data mixture；本family补充“reference-relative gradient utility”的机制与治理风险，留待Books Gate判断。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅回拨 W02、补全文审计与评分；不修改 Books。
- **Open Questions:** LLM token/example级gradient成本如何控制；reference version更新是否导致filter churn；如何同时约束quality、diversity、safety、license与rare capability；filter feedback如何做shadow evaluation和rollback。

### Padding Tone

- **Candidate / Week / Score:** Padding Tone / 2025-W02 / 24/30。
- **Source Family ID:** `padding-tone-t2i-causal-analysis`。
- **Source Type:** arXiv primary mechanistic-interpretability paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-12；v2 2025-03-02。事件与机制审计以v1为准。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.06751v1；metadata，https://arxiv.org/abs/2501.06751。
- **Related Primary Sources:** Stable Diffusion、SDXL、FLUX与CLIP/T5是被测architecture families；论文不授权把单模型观察外推到全部diffusion模型。
- **Access and Verification Status:** Verified；方法、causal interventions、model comparisons、metrics、appendix与limitations可读。
- **Full-read Coverage:** 已读Introduction/related work、text-encoder intervention、diffusion-process intervention、attention analysis、cross-architecture结果、metrics/appendix、conclusion与limitations。
- **Original Problem:** padding常被当作纯batch-shape占位符，但经过text encoder/self-attention后可能携带prompt-context；下游diffusion是否读它取决于architecture/training，忽略会误判representation owner与优化安全性。
- **Why the Previous Design Was Reasonable:** fixed-length padding简化batching和kernel shape，attention mask通常意味着“无语义”；在frozen encoder或cross-attention模型中，许多pads确实影响小，移除/忽略合理。
- **Changed Constraint:** T2I pipeline把encoded prompt传入不同attention结构；trained text encoder、自注意力与joint token interaction可能把padding转成计算scratch/register，语义不再由token id单独决定。
- **Mechanism:** 论文分别在text encoding阶段替换prompt/pad representation，并在每个diffusion attention block做intervention；比较prompt-contextual pads、clean pads与prompt tokens，以CLIP/KID及attention观察定位信息在何处写入/读取。
- **State Ownership:** tokenizer只拥有pad id；text encoder输出拥有contextualized pad state；diffusion block可能把它当register继续更新；cache/batching优化必须以encoded representation与mask semantics命名，不能只按原token分类。
- **Control Flow / Data Flow:** prompt+padding → text encoder contextualization → prompt/pad representations → cross/self/joint attention diffusion → image；causal replacement在encoder或每个diffusion layer切断某一路径并观察输出变化。
- **Implementation Details:** 研究在多种T2I架构上发现三类行为：信息在encoder写入pad、在diffusion中使用/继续写入，或pads基本被忽略；FLUX与SDXL例子显示architecture/training不同导致结果不同。
- **Evaluation Setup:** 多prompt、多seed和若干T2I models；比较完整prompt、only pads、only prompt与clean pads，使用CLIP similarity、KID、attention map与生成样例。
- **Baselines / Ablations / Sensitivity / Overhead:** 有intervention location、token subset与model architecture对照；没有大规模prompt/domain coverage、human causal validation、runtime overhead或训练阶段的controlled counterfactual。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 被测model family与prompt/token设置部分披露；hardware、precision、batch/concurrency、latency/SLO不影响主要机制结论但均 `Not Disclosed`，不得用于性能推断。
- **What the Evidence Actually Proves:** 在被测模型/提示中，某些contextualized pads对输出有可干预的因果影响，且作用位置随text encoder是否训练、cross/self/joint attention结构变化。
- **What It Does Not Prove:** 不证明padding总是有语义、不证明attention map本身给出因果解释，也不证明去除pads必然降质或保留pads必然更好。
- **Limitations / Threats to Validity:** 作者承认model/prompt空间有限，CLIP/KID不覆盖全部视觉质量；intervention可能产生off-manifold representation，且结果依赖实现细节。
- **Trade-offs / New Failure Modes:** 将pads当无状态占位可获得简化与吞吐；将其视为contextual state提高正确性理解，却增加cache identity、mask compatibility与kernel优化约束。错误strip/merge pads会造成静默质量漂移。
- **Where the Previous Design Still Applies:** encoder输出对pads稳定为no-op、attention严格mask且conformance测试通过时，pad stripping/compaction仍合理；机制结论应逐architecture验证。
- **Evolution Relationship:** `Principle Reuse`：special token/no-op attention → contextual scratch/register → architecture-specific causal state；不是一种新generation algorithm。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MODEL-SELF-ATTENTION`（Ch14）、`MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `INFER-DYNAMIC-BATCHING`（Ch46）。
- **Target and Adjacent Chapters Read:** 已核对 Ch13～15、Ch23～24与Ch45～47的attention semantics、representation identity、generation与batch compaction边界。
- **Existing Coverage:** Books已有token/position/mask与modality representation；该paper提供“padding也可能成为mutable state”的因果案例，待Books Gate判断是否需refine。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅回拨 W02、补全文审计与owner mapping；不修改 Books。
- **Open Questions:** 如何建立跨model的pad-semantics conformance suite；quantization/compilation/prefix cache是否改变该行为；能否用训练约束显式规定pads的no-op或register contract。

### Beyond Sight / FuSe

- **Candidate / Week / Score:** Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding / 2025-W02 / 28/30。
- **Source Family ID:** `fuse-heterogeneous-sensor-language-grounding`；论文、项目页、代码、数据集和模型 checkpoint 属于同一 family，后续 ICRA 2025 接收不重复计分。
- **Source Type:** arXiv primary paper + 作者项目页 + 官方代码仓库 + 数据卡。
- **First-public Date / Revision History:** arXiv v1 2025-01-08；后续版本和 ICRA 2025 publication 不改变 W02 owner。
- **Direct Primary Sources:** arXiv v1 HTML，https://arxiv.org/html/2501.04693v1；metadata，https://arxiv.org/abs/2501.04693；项目页，https://fuse-model.github.io/；代码，https://github.com/fuse-model/FuSe；数据卡，https://huggingface.co/datasets/oier-mees/FuSe。
- **Related Primary Sources:** Octo、Open X-Embodiment、PaliGemma/PaliVLA、TVL 和 DIGIT sensors 是论文明确依赖的 base policies、pretraining data 与 sensor encoders；它们用于解释 layering，不把各自结果倒灌为 FuSe 证据。
- **Access and Verification Status:** Verified；论文 method、实现、真实机器人 evaluation、ablation、结论与 limitation 可读，代码、数据和 checkpoint 入口可核验。
- **Full-read Coverage:** 已读 metadata/revision、abstract、introduction、related work、FuSe objective 与两个 auxiliary losses、sensor encoders、language rephrasing、training setup、三类真实机器人任务、multimodal/compositional tests、loss ablation、Octo/PaliGemma-VLA 对照、conclusion/limitation，并核对 repository training/evaluation entry points 与 dataset card。
- **Original Problem:** 大规模 generalist robot policies 主要从 vision、proprioception 与 action 数据学习；touch/audio 数据稀缺且很少与 robot action 联合出现。直接把新传感器接入小规模 finetuning 容易让策略继续依赖预训练模态，在视觉遮挡等 partial-observability 场景失去新传感器价值。
- **Why the Previous Design Was Reasonable:** vision/proprioception/action 是现有大规模机器人数据的公共交集，统一 observation schema 能降低采集、校准与部署复杂度；视觉充分、任务简单时，额外 sensor、encoder 与同步成本未必值得。
- **Changed Constraint:** 操作环境出现遮挡、弱光、材质和声音区分等视觉不足条件，同时 heterogeneous sensor/action 联合数据远少于视觉数据；系统需要保留预训练策略的 generalization，又要让稀缺模态真正影响动作。
- **Mechanism:** FuSe 将 tactile image 经预训练 TVL encoder、audio spectrogram 经 ResNet26 encoder，并与 vision/proprioception token 一起送入策略 backbone；在 behavior-cloning action loss 之外增加 CLIP-style multimodal contrastive loss 与 sensory-grounded language-generation loss，使不同 sensor combination 通过自然语言语义对齐，降低新模态被忽略的风险。
- **State Ownership:** sensor adapter 拥有 modality-specific encoding；backbone observation tokens 拥有融合后的短期感知状态；language target 是跨模态语义桥而非环境真值；policy/action head 拥有当前动作输出；robot/environment feedback 才能确认动作结果。
- **Control Flow / Data Flow:** camera/tactile/audio/IMU/proprioception → modality encoder/tokenization → shared policy transformer → action prediction；训练时同一 observation 另经 fusion attention 形成 embedding，分别进入 contrastive alignment 和 language generation head；执行时 5 Hz delta end-effector command 驱动机器人，再由新 observation 闭环修正。
- **Implementation Details:** Octo 路径使用额外 generative transformer head；PaliGemma-based 3B VLA 可直接用语言建模 head。作者用模板标注再生成 20 个语义保持的 rephrasing，统一 objective 为 behavior cloning + generative + contrastive loss；公开仓库分别提供 Octo/PaliVLA training 与 evaluation entry points。
- **Evaluation Setup:** 26,866 条 teleoperation trajectories，WidowX 250 6-DoF arm，tabletop grasping、shopping-bag grasping 与 sound-button 三类任务；含 24 个训练物体、32 个 unseen test objects 等受限 object sets，每个 scenario 5 rollouts，并测试 visual/tactile ambiguity、cross-modal composition 与 alternative VLA backbone。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 Octo vision-only finetuning、Octo from scratch with all sensors、ResNet from scratch，并消融 contrastive/generative loss；两项 auxiliary losses联合在遮挡任务最关键。论文没有系统扫描 sensor dropout、annotation noise、loss weight、history length、control frequency、cross-robot calibration 或 end-to-end latency sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 50,000 steps、v5e-128 TPU pod、batch 1024、2,000 warmup、peak learning rate 3e-4；Octo 与 PaliGemma-based 3B VLA；observation history 0.4s、robot control 5 Hz、visual 640×480、DIGIT 320×240、audio 1s@44.1kHz。训练/inference precision、online concurrency、action deadline/tail latency、sensor synchronization jitter 与 safety SLO 为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在上述机器人、sensor、数据和任务合同内，语言对齐辅助目标能让两类预训练策略使用稀缺 touch/audio signals；vision-only 和 from-scratch baselines、loss ablation 共同支持“新模态不会因简单拼接自动生效”。
- **What It Does Not Prove:** 不证明 natural language 是所有 heterogeneous sensor 的最佳或无损 interlingua，不证明 zero-shot 跨任务/跨机器人泛化，也不证明作者摘要中的 20%+ 提升可脱离 task、object、rollout 与 baseline contract 外推。
- **Limitations / Threats to Validity:** 三类任务、单一 robot family、小规模 rollout 次数与人为模板/LLM rephrasing 限制 external validity；作者明确指出训练资源把 observation history 限制在 0.4s。缺 sensor failure、time alignment、closed-loop safety、long-horizon recovery 与独立复现。
- **Trade-offs / New Failure Modes:** language bridge 复用预训练语义并减少全组合 joint data 需求，但引入 annotation semantics、encoder calibration、modality collapse、sensor timestamp skew、missing-modality behavior 与 auxiliary-loss interference；增加 sensor/encoder 也提高训练算力、部署带宽、同步与故障诊断成本。
- **Where the Previous Design Still Applies:** 视觉充分、任务短、sensor reliability 较低或实时/成本预算严格时，vision+proprioception policy 仍更简单；大量同步 heterogeneous trajectories 可用时，直接 joint representation learning 也可能减少 language bottleneck。
- **Evolution Relationship:** `Layering / Dependency`：vision/proprioception generalist policy → heterogeneous sensor adapters → language-grounded auxiliary objectives → action-conditioned closed loop。它扩展 observation contract，不替代原策略 backbone，也不是 world model。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Ch26）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-DATA`（Ch27）、`TRAIN-SFT`（Ch29）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已核对 ROADMAP 的 Ch23～29 与 Ch66 owner/边界；Books 在本阶段只读定位、不写入。
- **Existing Coverage:** Ch23/26 已覆盖 modality identity、VLA perception→action loop 与 physical feedback 上位原则；FuSe 新增的是“稀缺 sensor 通过 language-grounded auxiliary objective 接入预训练 action policy”的受限演进节点，是否吸收须留待独立 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly Source Review 完成，但用户明确要求本阶段只完成 Weekly。
- **Changed Files or Rejection Reason:** 仅回拨并重验 W02，更新年度 ledger；不修改 Books，也不把项目页摘要当作论文全文替代。
- **Open Questions:** sensor timestamp/schema/version 如何成为 action-policy identity；sensor dropout 与错误语义桥怎样触发 fallback；更长 history、不同 robot/control rate 和无语言 joint alignment 下，收益与 failure boundary 是否保持。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- vLLM 2024 Retrospective and 2025 Vision → 第 46、52 章（Direct Evolution）
- rStar-Math → `TRAIN-RLHF`（Ch31），handoff `TRAIN-GRPO`（Ch33）与 `AGENT-PLANNING`（Ch79）
- Search-o1 → `AGENT-RAG`（Ch76），handoff Ch75、Ch79、Ch81
- Cosmos World Foundation Model Platform → `MULTIMODAL-WORLD-MODELS`（Ch25），handoff Ch23、Ch24、Ch26、`TRAIN-DATA`
- LLaVA-Mini → `MULTIMODAL-REPRESENTATION`（Ch23），handoff `INFER-PREFILL`（Ch43）与 `INFER-KV-CACHE`（Ch45）
- Meta-CoT → `TRAIN-RLHF`（Ch31），handoff Ch33、Ch36、`AGENT-PLANNING`（Ch79）
- Agent Laboratory → `AGENT-WORKFLOW`（Ch81），handoff Ch78～80、Ch82、`PLATFORM-EVALUATION-SYSTEM`（Ch66）
- URSA → `TRAIN-RLHF`（Ch31），handoff Ch23、Ch29～33、Ch66
- InfiGUIAgent → `AGENT-WORKFLOW`（Ch81），handoff Ch23、Ch78～80、Ch82
- Sa2VA → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch26、Ch78
- MotionBench → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch43、Ch66
- PPTAgent → `AGENT-WORKFLOW`（Ch81），handoff Ch78、Ch80、Ch66
- Diffusion as Shader → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch25～26
- OpenOmni → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24、Ch34、Ch42～44
- Dolphin → `AGENT-WORKFLOW`（Ch81），handoff Ch66、Ch77、Ch79～80
- Segmenting Text and Learning Their Rewards → `TRAIN-PPO`（Ch32），handoff Ch31、Ch33
- Modern GAN Baseline → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch28、Ch49
- GeAR → `AGENT-RAG`（Ch76），handoff Ch43、Ch66、Ch75
- Toto → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24～25、Ch28
- DriveBench → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch26、Ch68、Ch70
- Centurio → `TRAIN-DATA`（Ch27），handoff Ch23、Ch66
- SWE-Fixer → `AGENT-WORKFLOW`（Ch81），handoff Ch66、Ch76、Ch78
- VideoRAG → `AGENT-RAG`（Ch76），handoff Ch23、Ch43、Ch45、Ch66
- SCRIT → `TRAIN-RLHF`（Ch31），handoff Ch33、Ch66、Ch80
- LlamaV-o1 → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch23、Ch31、Ch48
- OmniManip → `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff Ch25、Ch66、Ch78、Ch81
- OVO-Bench → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch23、Ch45、Ch56、Ch77
- Migician → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch26、Ch66、Ch76
- Multiagent Finetuning → `TRAIN-SFT`（Ch29），handoff Ch36、Ch66、`AGENT-MULTI-AGENT`（Ch82）
- ReFocus → `AGENT-TOOL`（Ch78），handoff Ch23、Ch66、Ch81
- ConceptMaster → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、Ch25、Ch66
- Multi-subject Open-set Video Personalization → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、Ch25、Ch66
- FinDaP → `TRAIN-PRETRAINING`（Ch28），handoff Ch27、Ch29～35、Ch66
- Transformer-Squared → `TRAIN-LORA`（Ch30），handoff Ch49、Ch56、Ch58
- Tensor Product Attention / T6 → `INFER-KV-CACHE`（Ch45），handoff Ch14、Ch22、Ch47、Ch49
- ChemAgent → `AGENT-MEMORY`（Ch77），handoff Ch66、Ch75～76、Ch81
- MinMo → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24、Ch28、Ch42、Ch56
- O1 Replication Journey Part 3 → `TRAIN-SFT`（Ch29），handoff Ch8、Ch31、Ch56、Ch66
- VideoAuteur → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch25、Ch27、Ch66
- SPAM → `TRAIN-PRETRAINING`（Ch28），handoff Ch35～36、Ch67
- Grad-Mimic → `TRAIN-DATA`（Ch27），handoff Ch28、Ch58、Ch66
- Padding Tone → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch14、Ch24、Ch46
- Beyond Sight / FuSe → `MULTIMODAL-EMBODIED-VLA`（Ch26），handoff Ch23、Ch27、Ch29、Ch66
- Transformers 4.48.0 → `PLATFORM-MODEL-MANAGEMENT`（Ch58），handoff Ch48～50、Ch70

## Recommended Action

- vLLM 2024 Retrospective and 2025 Vision：Worth Watching；与 W05 的 V1 正式机制联合审查
- rStar-Math、Search-o1、Cosmos、LLaVA-Mini、Meta-CoT、Agent Laboratory、URSA、InfiGUIAgent：
  Full Review Complete；Books Pending — Integration Deferred
- Sa2VA、MotionBench、PPTAgent、Diffusion as Shader：Full Review Complete；Books Pending — Integration Deferred
- OpenOmni、Dolphin、Segmenting Text and Learning Their Rewards、Modern GAN Baseline：Full Review Complete；
  Books Pending — Integration Deferred
- GeAR、Toto、DriveBench、Centurio：Full Review Complete；Books Pending — Integration Deferred
- SWE-Fixer、VideoRAG、SCRIT：Full Review Complete；Books Pending — Integration Deferred
- LlamaV-o1：Full Review Complete；`Disputed — Books Frozen`，等待效率数字与复杂度表述澄清
- OmniManip、OVO-Bench、Migician、Multiagent Finetuning：Full Review Complete；Books Pending — Integration Deferred
- ReFocus、ConceptMaster、Multi-subject Open-set Video Personalization、FinDaP：Full Review Complete；
  Books Pending — Integration Deferred
- Transformer-Squared、Tensor Product Attention / T6：Full Review Complete；Books Pending — Integration Deferred；
  前者保留 dispatcher、two-pass、cache consistency 边界，后者保留 architecture-native cache 与 serving-kernel 证据边界
- ChemAgent：Full Review Complete；Books Pending — Integration Deferred；保留 typed memory、correctness write gate、
  provenance/rollback与 memory-quality failure boundary，不把 benchmark self-evolution外推为开放世界持续学习
- MinMo、O1 Replication Journey Part 3、VideoAuteur、SPAM、Grad-Mimic、Padding Tone：延迟发现 owner 已回拨，
  Full Review Complete；Books Pending — Integration Deferred
- Beyond Sight / FuSe：延迟归属项已回拨并完成论文、项目页、代码与数据卡联读；Books Pending — Integration Deferred
- Transformers 4.48.0：Full Review Complete；`Weekly Only — Version Bundle`
- llama-cpp-python 0.3.6、3DIS-FLUX：Low-score Rejected；保留来源与日期，不把 scoped release fix或窄域
  renderer extension提升为独立长期机制
- 论文/Research census 与 engineering ledger 的普通 `Review Pending = 0`

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

`Deferred by user request`。本阶段只修复 Weekly evidence；即使某个 Source Family 已完成 Full Review，
也统一记为 `Books Pending — Integration Deferred`，不修改 `books/`。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。
- llama-cpp-python 0.3.6 的 upstream pin与单一 streaming resource-lock fix已完成低分核验；它不支持新的通用 concurrency结论。

## Repository Changes

- 重新打开 `papers/2025/weekly/2025-W02/README.md`，将旧版 1 项候选扩展为 30 余项可追踪 discovery
  census，并把固定三工作日 grace 改为连续两个无 spillback 工作日的自适应闭合。
- 完成 rStar-Math、Search-o1、Cosmos、LLaVA-Mini、Meta-CoT、Agent Laboratory、URSA 与 InfiGUIAgent
  的全文 Source Review、评分、证据边界与 Stable Node mapping；补回 discovery census 遗漏的 GeAR。
- 完成 Sa2VA、MotionBench、PPTAgent 与 Diffusion as Shader 的全文 Source Review；MotionBench 的 arXiv
  HTML 身份异常已用同 ID v1 PDF、abs metadata 与 official repository 闭合并显式记录。
- 完成 OpenOmni、Dolphin、Segmenting Text and Learning Their Rewards 与 Modern GAN Baseline 的全文
  Source Review；分别收紧 real-time/self-aware、autonomous research、segment credit 与 GAN-vs-diffusion 的
  证据边界。
- 完成 GeAR、Toto、DriveBench 与 Centurio 的全文 Source Review；纠正 GeAR 名称/owner，并分别明确
  generation-assisted localization、visual next-token representation、missing-modality negative control 与 multilingual
  data-mixture 的适用边界。
- 完成 SWE-Fixer、VideoRAG、SCRIT 与 LlamaV-o1 的全文 Source Review；SWE-Fixer HTML错配以 v1 PDF/
  abs/repository闭合，LlamaV-o1的 runtime与复杂度冲突保留为 `Disputed`。
- 完成 OmniManip、OVO-Bench、Migician 与 Multiagent Finetuning 的全文 Source Review；分别区分规划检查与
  物理反馈、offline prefix simulation 与 streaming runtime、文本桥接与 joint grounding，以及 majority pseudo-label 与 truth。
- 完成 ReFocus、ConceptMaster、Video Alchemist 与 FinDaP 的全文 Source Review；纠正 FinDaP event date，并记录
  ReFocus v1 的 14,344/21k 数据量冲突，不把私有 video backbone 或 finance recipe 外推为通用结论。
- 完成 Transformers 4.48.0 Release/相关PR的 20分 Source Review，并对 llama-cpp-python 0.3.6完成低分
  identity/date/changelog/rejection核验；工程 release ledger普通 Pending清零。
- W03 replay 找回 Transformer-Squared 与 Tensor Product Attention 两个 W02 owner；均完成 v1全文、revision、
  artifact、实验合同、limitations、Stable Node与相邻章节审计，纠正原 grace exclusion。
- 关闭 grace identity gap时又定位 ChemAgent为 W02 owner，并完成三类memory、runtime写回、evaluator/refinement、
  self-evolution、cost/error analysis、ablation、artifact与 Agent章节边界审计；PRM lessons确认归 W03。
- 对 01-14～15 delayed-discovery 页面继续执行 owner-date replay，回拨 MinMo、O1 Replication Journey Part 3、
  VideoAuteur、SPAM、Grad-Mimic、Padding Tone与3DIS-FLUX；前六项完成非模板化30字段Full Source Review，
  3DIS-FLUX完成低分来源/日期/拒绝核验。
- W03 delayed page 又找回 Beyond Sight / FuSe（v1 2025-01-08），已完成论文、项目页、代码、数据与
  30字段 Full Source Review，并明确 sensor-language-action 的状态、闭环与 evidence boundary。
- W02 已通过 46/46 scoring、44/44 `20+` Full Source Review、2/2 low-score disposition、评分合计、
  30字段cardinality、日期/owner、Markdown与diff检查；2025 Weekly Evidence Rebuild继续进入W03，未修改Books。

## Open Questions

- W05 V1 Alpha source family 完成后，V0→V1 的重构动机是否形成 Ch46 的长期机制缺口。
- rStar-Math 的 PPM/policy 共演化如何设置独立 held-out gate；Search-o1 如何形成可复现、可防注入的
  web evidence contract。
- Cosmos 的 video prediction 如何被 action-outcome 闭环证据验证；LLaVA-Mini 的不可逆压缩如何支持
  多轮 query 变化。
- OpenOmni 的 text/speech divergence 与真实 streaming SLO 如何验证；Dolphin 如何避免 research loop
  过拟合同一 benchmark；segment reward 的 underdetermined credit 如何独立校准。
- GeAR generated unit 如何绑定原始证据；Toto predictive representation 何时才可升级为 action-conditioned world
  state；DriveBench 的离线 grounding gate 如何连接 closed-loop safety outcome。
- SWE-Fixer retriever miss如何恢复；VideoRAG的 clip/span citation如何绑定；SCRIT如何打破 generator/verifier同源偏差；
  LlamaV-o1的 4-beam runtime与 complexity表述如何澄清。
- OmniManip 如何版本化 mesh/pose 并量化真实控制频率；OVO-Bench 如何对齐 frame arrival、memory budget 与 deadline；
  Migician 如何保留可审计又不过度有损的跨图像关系；Multiagent Finetuning 如何识别 correlated majority error。
- ReFocus 的 21k 是否为笔误或未披露合并数据；多主体 video identity、motion 与 interaction如何在同一 evaluator中裁决；
  FinDaP joint recipe能否跨 model family、同 token/compute budget复现。
- Transformers common attention、multi-GPU candidate/cache 与 release conversion tooling如何形成可复现 conformance/security matrix。
- Transformer-Squared 的 expert mixture如何绑定 base/version/cache identity，dispatcher不确定性与 CEM成本如何进入在线 SLO；
  TPA的 factorized cache在生产kernel下能否把理论元素量节省转成稳定的 TTFT/TPOT/throughput收益。
- ChemAgent的 correctness write gate如何验证中间轨迹而非只看最终答案；跨版本/跨模型memory如何执行 provenance、
  contradiction、supersession、quarantine、delete与 rollback。
- MinMo的duplex false decision如何回退并一致撤销audio/text/KV state；O1 long-trace如何与search/verifier在等token预算下比较；
  VideoAuteur如何用可执行环境而非视觉偏好验证长期state。
- SPAM如何在ZeRO/sharded optimizer上同步reset与checkpoint；Grad-Mimic如何避免reference bias feedback loop；
  Padding Tone如何形成跨architecture的mask/pad conformance contract。
- FuSe 的 sensor timestamp/schema/version 如何进入 policy identity；sensor dropout、misalignment 与
  language-grounding error 如何进入 fallback/safety gate；更长 observation history 是否改变收益。

## Sources

- rStar-Math — https://arxiv.org/html/2501.04519v1（v1: 2025-01-08；Accessed: 2026-08-17）
- Search-o1 — https://arxiv.org/html/2501.05366v1（v1: 2025-01-09；Accessed: 2026-08-17）
- Cosmos World Foundation Model Platform — https://arxiv.org/html/2501.03575v1（v1: 2025-01-07；Accessed: 2026-08-17）
- LLaVA-Mini — https://arxiv.org/html/2501.03895v1（v1: 2025-01-07；Accessed: 2026-08-17）
- Towards System 2 Reasoning / Meta-CoT — https://arxiv.org/html/2501.04682v1（v1: 2025-01-08；Accessed: 2026-08-17）
- Agent Laboratory — https://arxiv.org/pdf/2501.04227v1（v1: 2025-01-07；Accessed: 2026-08-17）
- URSA — https://arxiv.org/html/2501.04686v1（v1: 2025-01-08；Accessed: 2026-08-17）
- InfiGUIAgent — https://arxiv.org/html/2501.04575v1（v1: 2025-01-08；Accessed: 2026-08-17）
- Sa2VA — https://arxiv.org/html/2501.04001v1（v1: 2025-01-07；Accessed: 2026-08-17）
- MotionBench — https://arxiv.org/pdf/2501.02955v1（v1: 2025-01-06；Accessed: 2026-08-17）
- MotionBench official repository — https://github.com/zai-org/MotionBench（Accessed: 2026-08-17）
- PPTAgent — https://arxiv.org/html/2501.03936v1（v1: 2025-01-07；Accessed: 2026-08-17）
- Diffusion as Shader — https://arxiv.org/html/2501.03847v1（v1: 2025-01-07；Accessed: 2026-08-17）
- OpenOmni — https://arxiv.org/html/2501.04561v1（v1: 2025-01-08；Accessed: 2026-08-17）
- Dolphin — https://arxiv.org/html/2501.03916v1（v1: 2025-01-07；Accessed: 2026-08-17）
- Segmenting Text and Learning Their Rewards — https://arxiv.org/html/2501.02790v1（v1: 2025-01-06；Accessed: 2026-08-17）
- Modern GAN Baseline — https://arxiv.org/html/2501.05441v1（v1: 2025-01-09；Accessed: 2026-08-17）
- GeAR / Generation Augmented Retrieval — https://arxiv.org/html/2501.02772v1（v1: 2025-01-06；Accessed: 2026-08-17）
- Autoregressive Pre-training from Videos / Toto — https://arxiv.org/html/2501.05453v1（v1: 2025-01-09；Accessed: 2026-08-17）
- DriveBench — https://arxiv.org/html/2501.04003v1（v1: 2025-01-07；Accessed: 2026-08-17）
- Centurio — https://arxiv.org/html/2501.05122v1（v1: 2025-01-09；Accessed: 2026-08-17）
- SWE-Fixer — https://arxiv.org/pdf/2501.05040v1（v1: 2025-01-09；Accessed: 2026-08-17）
- SWE-Fixer official repository — https://github.com/InternLM/SWE-Fixer（Accessed: 2026-08-17）
- VideoRAG — https://arxiv.org/html/2501.05874v1（v1: 2025-01-10；Accessed: 2026-08-17）
- SCRIT / Self-Evolving Critic — https://arxiv.org/html/2501.05727v1（v1: 2025-01-10；Accessed: 2026-08-17）
- LlamaV-o1 — https://arxiv.org/html/2501.06186v1（v1: 2025-01-10；Accessed: 2026-08-17）
- OmniManip — https://arxiv.org/html/2501.03841v1（v1: 2025-01-07；Accessed: 2026-08-17）
- OmniManip official project — https://omnimanip.github.io/（Accessed: 2026-08-17）
- OVO-Bench — https://arxiv.org/html/2501.05510v1（v1: 2025-01-09；Accessed: 2026-08-17）
- OVO-Bench official repository — https://github.com/JoeLeelyf/OVO-Bench（Accessed: 2026-08-17）
- Migician — https://arxiv.org/html/2501.05767v1（v1: 2025-01-10；Accessed: 2026-08-17）
- Multiagent Finetuning — https://arxiv.org/html/2501.05707v1（v1: 2025-01-10；Accessed: 2026-08-17）
- ReFocus — https://arxiv.org/html/2501.05452v1（v1: 2025-01-09；Accessed: 2026-08-17）
- ReFocus official project — https://zeyofu.github.io/ReFocus/（Accessed: 2026-08-17）
- ConceptMaster — https://arxiv.org/html/2501.04698v1（v1: 2025-01-08；Accessed: 2026-08-17）
- Multi-subject Open-set Video Personalization — https://arxiv.org/html/2501.06187v1（v1: 2025-01-10；Accessed: 2026-08-17）
- FinDaP — https://arxiv.org/html/2501.04961v1（v1: 2025-01-09；Accessed: 2026-08-17）
- Transformer-Squared — https://arxiv.org/html/2501.06252v1（v1: 2025-01-09；Accessed: 2026-08-17）
- Transformer-Squared metadata/revisions — https://arxiv.org/abs/2501.06252（Accessed: 2026-08-17）
- Transformer-Squared official repository — https://github.com/SakanaAI/self-adaptive-llms（Accessed: 2026-08-17）
- Tensor Product Attention / T6 — https://arxiv.org/html/2501.06425v1（v1: 2025-01-11；Accessed: 2026-08-17）
- Tensor Product Attention metadata/revisions — https://arxiv.org/abs/2501.06425（Accessed: 2026-08-17）
- Tensor Product Attention official repository — https://github.com/tensorgi/TPA（Accessed: 2026-08-17）
- ChemAgent — https://arxiv.org/html/2501.06590v1（v1: 2025-01-11；Accessed: 2026-08-17）
- ChemAgent metadata — https://arxiv.org/abs/2501.06590（Accessed: 2026-08-17）
- ChemAgent official repository — https://github.com/gersteinlab/chemagent（Accessed: 2026-08-17）
- MinMo — https://arxiv.org/html/2501.06282v1（v1: 2025-01-10；Accessed: 2026-08-17）
- O1 Replication Journey Part 3 — https://arxiv.org/html/2501.06458v1（v1: 2025-01-11；Accessed: 2026-08-17）
- VideoAuteur — https://arxiv.org/html/2501.06173v1（v1: 2025-01-10；Accessed: 2026-08-17）
- SPAM — https://arxiv.org/html/2501.06842v1（v1: 2025-01-12；Accessed: 2026-08-17）
- Grad-Mimic — https://arxiv.org/html/2501.06708v1（v1: 2025-01-12；Accessed: 2026-08-17）
- Padding Tone — https://arxiv.org/html/2501.06751v1（v1: 2025-01-12；Accessed: 2026-08-17）
- Beyond Sight / FuSe — https://arxiv.org/html/2501.04693v1（v1: 2025-01-08；Accessed: 2026-08-17）
- Beyond Sight / FuSe official project — https://fuse-model.github.io/（Accessed: 2026-08-17）
- Beyond Sight / FuSe official repository — https://github.com/fuse-model/FuSe（Accessed: 2026-08-17）
- Beyond Sight / FuSe dataset card — https://huggingface.co/datasets/oier-mees/FuSe（Accessed: 2026-08-17）
- 3DIS-FLUX — https://arxiv.org/html/2501.05131v1（v1: 2025-01-09；Accessed: 2026-08-17）
- Transformers 4.48.0 — https://github.com/huggingface/transformers/releases/tag/v4.48.0（Released: 2025-01-10；Accessed: 2026-08-17）
- Transformers release packaging PR #35296 — https://github.com/huggingface/transformers/pull/35296（Accessed: 2026-08-17）
- Transformers assisted decoding multi-GPU PR #35116 — https://github.com/huggingface/transformers/pull/35116（Accessed: 2026-08-17）
- llama-cpp-python 0.3.6 — https://github.com/abetlen/llama-cpp-python/releases/tag/v0.3.6（Tagged: 2025-01-08；Accessed: 2026-08-17）
- llama-cpp-python changelog — https://github.com/abetlen/llama-cpp-python/blob/main/CHANGELOG.md（Accessed: 2026-08-17）
- vLLM 2024 Retrospective and 2025 Vision — https://vllm.ai/blog/2025-01-10-vllm-2024-wrapped-2025-vision（First Public: 2025-01-10；Accessed: 2026-08-17）
