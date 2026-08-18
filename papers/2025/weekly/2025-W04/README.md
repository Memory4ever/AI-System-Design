# AI Research Weekly — 2025-W04

> Coverage Window: 2025-01-20～2025-01-26
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Rebuild Started: 2026-08-18
> Accessed: 2026-08-18
> Backfilled: 2026-07-31
> Weekly Evidence Gate: Passed — 53/53 candidates have final evidence dispositions；44/44 `20+` candidates have non-template Full Source Review；9/9 low-score candidates have identity/date/score/rejection verification
> Books Integration: Deferred by user request

## Executive Summary

旧档只保留 DeepSeek-R1、Kimi k1.5 与 Chain of Agents，明显漏掉 2025-01-20～26 同期的 Agent
trajectory learning、MoE routing objective、GUI-native interaction、multimodal reward/evaluation、long-video
state、flow-model alignment 与 compiler release。W05 replay 进一步发现 2025-01-26 首发的 Qwen2.5-VL，已按
owner week 回拨；Qwen2.5-1M 又因 Hugging Face 延迟收录而在 W05 被发现，但其 arXiv v1 同为 1 月26日，
也已回拨。后续 W05 discovery replay 又暴露 9 项 arXiv v1 实际发表于 1 月20～26日的延迟发现候选；
当前重放建立 53 项候选身份，其中 44 项达到 20 分；DeepFlow 也因 arXiv v1 为 1 月24日从 W05 回拨，
Transformers 4.48.1 则按 1 月20日 tag 日期以低分兼容性补丁回拨。
DeepSeek-R1、Kimi k1.5 与 Chain of Agents 的旧 Source Review 仅作为已读 seed；其余候选按
primary source 补齐非模板化 Full Source Review 前，W04 Gate 保持 Open。Books Integration 明确关闭。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；本轮访问日期为 2026-08-18。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- Hugging Face 01-22～24 页面用于延迟发现；事件归属以 arXiv v1 / official release date 为准。EMO2
  的 v1 实际属于 W03，已回拨而不在本周重复计分。Video Depth Anything、TPO 与 EmbodiedEval 的
  arXiv HTML 当前错误映射到无关 author-response 页面，正文将使用同 ID PDF/abs 与 artifact 闭合。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- DeepSeek-R1 release / report、Kimi k1.5、Hunyuan3D 2.0、UI-TARS、InternLM-XComposer2.5-Reward
  与相关 repository/model artifacts 作为 Source Family 联读；只有公告、没有公开机制的事实不会反推实现。
- Qwen2.5-VL 的 2025-01-26 官方 release 为本周事件；2025-02-19 technical report 只作为同一 Source Family
  的后续 primary evidence，用于核验机制，不重复制造 W08 事件。
- Qwen2.5-1M 的 arXiv v1 日期同为 2025-01-26；Hugging Face 1月28日 discovery 与旧站 1月27日文章显示
  不能替代 first-public date，模型、training、sparse Prefill 与 BladeLLM runtime 作为一个 family 联读。
- Chain of Agents 的 2025-01-23 Google Research follow-up 是同一 2024 paper family 的机构解释节点，
  不把原论文重新计为 2025 新机制。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

### Discovery Census

| Candidate | Primary ID | First Public | Current State | Initial System Relevance |
| --- | --- | --- | --- | --- |
| Agent-R | arXiv:2501.11425 | 2025-01-20 | Full Source Review Complete | MCTS revision trajectories、policy-relative error recovery |
| Mobile-Agent-E | arXiv:2501.11733 | 2025-01-20 | Full Source Review Complete | hierarchical mobile workflow、Tips/Shortcuts 与 invalid-state failure |
| Demons in the Detail | arXiv:2501.11873 | 2025-01-20 | Full Source Review Complete | micro-batch→global-batch MoE load-balancing semantics |
| MMVU | arXiv:2501.12380 | 2025-01-21 | Full Source Review Complete | expert-annotated video evaluation 与 text-only shortcut detection |
| Continuous 3D Perception / CUT3R | arXiv:2501.12387 | 2025-01-21 | Full Source Review Complete — W06 discovery spillback | recurrent persistent scene state、read/write separation 与 online metric pointmaps |
| UI-TARS | arXiv:2501.12326 | 2025-01-21 | Full Source Review Complete | rule/framework→native GUI model、unified action traces |
| Hunyuan3D 2.0 | arXiv:2501.12202 | 2025-01-21 | Full Source Review Complete | shape→texture→asset pipeline 与 artifact boundary |
| InternLM-XComposer2.5-Reward | arXiv:2501.12368 | 2025-01-21 | Full Source Review Complete | multimodal reward reused across RL、selection、data cleaning |
| Video Depth Anything | arXiv:2501.12375 | 2025-01-21 | Full Source Review Complete — PDF used；HTML mismatch preserved | long-video depth state、key-frame reference alignment |
| Condor | arXiv:2501.12273 | 2025-01-21 | Full Source Review Complete — v1 PDF + official artifact | knowledge-tree synthetic SFT data、self-reflection refinement |
| Taming Teacher Forcing | arXiv:2501.12389 | 2025-01-21 | Full Source Review Complete — PDF used；HTML mismatch preserved | masked autoregressive video generation 与 inference mismatch |
| EmbodiedEval | arXiv:2501.11858 | 2025-01-21 | Full Source Review Complete — v1 identity + artifact + later official text；HTML mismatch preserved | interactive embodied evaluation、environment state |
| DeepSeek-R1 | arXiv:2501.12948 | release 2025-01-20；paper v1 2025-01-22 | Full Source Review Complete — provisional seed | pure RL→cold start→multi-stage RL/SFT→distillation |
| Qwen2.5-VL | official release / arXiv:2502.13923 | release 2025-01-26；report v1 2025-02-19 | Full Source Review Complete — W05 spillback | native-resolution vision、dynamic FPS、absolute-time MRoPE 与 multimodal state identity |
| Qwen2.5-1M | arXiv:2501.15383 / official release | 2025-01-26 | Full Source Review Complete — W05 spillback | progressive long-context training→DCA/sparse prefill→DCPP/TAG runtime |
| Humanity's Last Exam | arXiv:2501.14249 | 2025-01-24 | Full Source Review Complete — W05 discovery spillback | frontier benchmark construction、private holdout 与 calibration boundary |
| Chain-of-Retrieval Augmented Generation | arXiv:2501.14342 | 2025-01-24 | Full Source Review Complete — W05 discovery spillback | iterative retrieval state、rejection-sampled chains 与 test-time search |
| RL + Transformer / ICRL | arXiv:2501.14176 | 2025-01-24 | Full Source Review Complete — W05 discovery spillback | trajectory-conditioned adaptation under partial observability |
| Redundancy Principles for MLLM Benchmarks | arXiv:2501.13953 | 2025-01-20 | Full Source Review Complete — delayed discovery | dimension、instance 与 cross-benchmark redundancy |
| RealCritic | arXiv:2501.14492 | 2025-01-24 | Full Source Review Complete — W05 discovery spillback | critique effectiveness measured by downstream correction |
| Baichuan-Omni-1.5 | arXiv:2501.15368 | 2025-01-26 | Full Source Review Complete — W05 discovery spillback | image/audio/video/text representation and staged alignment |
| ARWKV | arXiv:2501.15570 | 2025-01-26 | Full Source Review Complete — W05 discovery spillback | Transformer-to-RWKV conversion via hidden-state and output distillation |
| Parameters vs FLOPs / MoE Sparsity | arXiv:2501.12370 | 2025-01-21 | Full Source Review Complete — delayed discovery | total parameters、active compute 与 optimal sparsity scaling |
| CodeMonkeys | arXiv:2501.14723 | 2025-01-24 | Full Source Review Complete — W05 discovery spillback | serial/parallel test-time compute、executable tests 与 candidate selection |
| DeepFlow | arXiv:2501.14417 | 2025-01-24 | Full Source Review Complete — W05 discovery spillback | serverless request/job/task、FlowServe、typed KV movement、PD-aware scheduling 与 fast scale-out |
| Kimi k1.5 | arXiv:2501.12599 | 2025-01-22 | Full Source Review Complete — provisional seed | long-rollout RL、partial trajectory 与 long2short |
| VideoLLaMA 3 | arXiv:2501.13106 | 2025-01-22 | Full Source Review Complete | vision-centric tokens、image/video understanding contract |
| FilmAgent | arXiv:2501.12909 | 2025-01-22 | Full Source Review Complete | durable multi-agent film-production workflow |
| Test-Time Preference Optimization | arXiv:2501.12895 | 2025-01-22 | Full Source Review Complete — HTML mismatch resolved | textual feedback as iterative inference-time optimization |
| Autonomy-of-Experts | arXiv:2501.13074 | 2025-01-22 | Full Source Review Complete | independent experts、routing autonomy 与 conditional capacity |
| O1-Pruner | arXiv:2501.12570 | 2025-01-22 | Full Source Review Complete | accuracy-constrained reasoning-length optimization |
| Pairwise RM | arXiv:2501.13007 | 2025-01-22 | Full Source Review Complete | pairwise knockout selection、ranking cost/quality trade-off |
| Debate Helps Weak-to-Strong Generalization | arXiv:2501.13124 | 2025-01-21 | Full Source Review Complete | debate as supervision protocol、judge capability boundary |
| SRMT | arXiv:2501.13200 | 2025-01-22 | Full Source Review Complete | shared recurrent memory for partially observed multi-agent coordination |
| Fast3R | arXiv:2501.13928 | 2025-01-23 | Full Source Review Complete | many-view 3D reconstruction as one-forward-pass state fusion |
| Improving Video Generation with Human Feedback | arXiv:2501.13918 | 2025-01-23 | Full Source Review Complete | multidimensional reward→Flow-DPO/RWR/NRG branches |
| Sigma / DiffQKV | arXiv:2501.13629 | 2025-01-23 | Full Source Review Complete | Q/K/V asymmetric capacity、KV efficiency 与 domain data |
| Image Generation with CoT | arXiv:2501.13926 | 2025-01-23 | Full Source Review Complete | verifier-guided stepwise image generation |
| Video-MMMU | arXiv:2501.13826 | 2025-01-23 | Full Source Review Complete | professional-video knowledge acquisition evaluation |
| Temporal Preference Optimization | arXiv:2501.13919 | 2025-01-23 | Full Source Review Complete — v1 PDF used；HTML mismatch preserved | localized/comprehensive temporal preference pairs |
| Imagine-E | arXiv:2501.13920 | 2025-01-23 | Full Source Review Complete | capability taxonomy for text-to-image systems |
| Hallucinations in Drug Discovery | arXiv:2501.13824 | 2025-01-23 | Full Source Review Complete | hypothesis generation vs executable scientific validation |
| Chain of Agents follow-up | Google Research / arXiv:2406.02818 | 2025-01-23 follow-up；paper v1 2024-06-04 | Full Source Review Complete — provisional seed | chunked context propagation 与 compression error |
| Reasoning Language Models: A Blueprint | arXiv:2501.11223 | 2025-01-20 | Low-score Verified — Weekly Only / Survey Blueprint | taxonomy与x1 prototype；非独立primary mechanism |
| TokenVerse | arXiv:2501.12224 | 2025-01-21 | Low-score Verified — Weekly Only | modulation-space multi-concept personalization narrow case |
| GPS as a Control Signal | arXiv:2501.12390 | 2025-01-21 | Low-score Verified — Weekly Only；PDF/abs used after HTML mismatch | narrow geolocation-conditioned generation case |
| Panoramic Interests / SCAPE | arXiv:2501.11900 | 2025-01-21 | Low-score Verified — Weekly Only | personalized headline generation；纠正初始 panorama 主题误识别 |
| PAINT / Fixing Imbalanced Attention | arXiv:2501.12206 | 2025-01-21 | Low-score Verified — Weekly Only / Experimental | narrow multimodal attention correction case |
| One-Prompt-One-Story | arXiv:2501.13554 | 2025-01-23 | Low-score Verified — Weekly Only / Experimental | tuning-free consistent T2I narrow case |
| EchoVideo | arXiv:2501.13452 | 2025-01-23 | Low-score Verified — Weekly Only / Experimental | identity-preserving human-video narrow case |
| MatAnyone | arXiv:2501.14677 | 2025-01-24 | Low-score Verified — Weekly Only / Narrow Vision Mechanism | target-assigned video matting、region-adaptive memory propagation；不形成通用 runtime state 结论 |

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

### Fixed-source Release Ledger

| Candidate | Primary ID | Event Date | Current State | Evidence Boundary |
| --- | --- | --- | --- | --- |
| Triton 3.2.0 | official release / `RELEASE.md` | 2025-01-22 | Full Source Review Complete — Version Fact / Mechanism Not Disclosed | release snapshot、compatibility与promotion workflow；无独立 feature ledger |
| JAX 0.5.0 | official changelog | 2025-01-17 | Owner W03 | 已归前周，不重复计分 |
| Transformers 4.48.0 | official release | 2025-01-10 | Owner W02 | 已归前周，不重复计分 |
| Transformers 4.48.1 | official release tag `v4.48.1` | 2025-01-20 | Low-score Verified — Weekly Only / Patch Release | 修复 gradient accumulation、Phi bias 与 Moonshine generate regression；不形成新的长期架构机制 |

其余固定工程源尚在 release/tag/RFC 复核中；普通 commit、model-support 列表与无机制 patch 不自动升级为候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| DeepSeek-R1 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| Kimi k1.5 | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| UI-TARS | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Qwen2.5-VL | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Qwen2.5-1M | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| Agent-R | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Demons in the Detail | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Improving Video Generation with Human Feedback | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Sigma / DiffQKV | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Mobile-Agent-E | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| InternLM-XComposer2.5-Reward | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Image Generation with CoT | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| VideoLLaMA 3 | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| MMVU | 4 | 5 | 5 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Continuous 3D Perception / CUT3R | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Test-Time Preference Optimization | 4 | 5 | 5 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Autonomy-of-Experts | 5 | 4 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Pairwise RM | 4 | 5 | 5 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Temporal Preference Optimization | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| EmbodiedEval | 4 | 5 | 5 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Video Depth Anything | 4 | 5 | 5 | 5 | 3 | 1 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Taming Teacher Forcing | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| FilmAgent | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| O1-Pruner | 4 | 4 | 5 | 5 | 4 | 1 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| SRMT | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Fast3R | 4 | 4 | 5 | 5 | 3 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Video-MMMU | 3 | 5 | 5 | 5 | 4 | 1 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Hunyuan3D 2.0 | 4 | 4 | 5 | 5 | 3 | 1 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Condor | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Debate Helps Weak-to-Strong | 4 | 4 | 4 | 5 | 4 | 1 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Imagine-E | 3 | 4 | 5 | 5 | 4 | 1 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Triton 3.2.0 | 3 | 5 | 5 | 5 | 4 | 0 | 22/30 | Full Review Complete；Weekly Only — Version Fact / Mechanism Not Disclosed |
| Chain of Agents follow-up | 3 | 4 | 4 | 5 | 4 | 1 | 21/30 | Full Review Complete；Books Pending — Integration Deferred |
| Hallucinations in Drug Discovery | 3 | 4 | 4 | 5 | 3 | 1 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| Chain-of-Retrieval Augmented Generation | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| CodeMonkeys | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Humanity's Last Exam | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Parameters vs FLOPs / MoE Sparsity | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Baichuan-Omni-1.5 | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| RealCritic | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Redundancy Principles for MLLM Benchmarks | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| RL + Transformer / ICRL | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| ARWKV | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| DeepFlow | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete；Books Pending — Integration Deferred |
| Reasoning Language Models: A Blueprint | 2 | 3 | 4 | 5 | 3 | 2 | 19/30 | Low-score Verified；Weekly Only — Survey Blueprint |
| TokenVerse | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — Narrow Personalization |
| PAINT / Fixing Imbalanced Attention | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — Narrow Experimental Case |
| One-Prompt-One-Story | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — Narrow Experimental Case |
| EchoVideo | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified；Weekly Only — Narrow Experimental Case |
| MatAnyone | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified；Weekly Only — Narrow Video-Matting State Case |
| GPS as a Control Signal | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified；Weekly Only — Narrow Conditioning Case |
| Panoramic Interests / SCAPE | 3 | 3 | 4 | 5 | 2 | 1 | 18/30 | Low-score Verified；Weekly Only — Domain Personalization |
| Transformers 4.48.1 | 1 | 2 | 4 | 5 | 3 | 1 | 16/30 | Low-score Verified；Weekly Only — Patch Release |

### Deep Analysis 1 — DeepSeek-R1

- First Public: 2025-01-20 (release); 2025-01-22 (paper v1)
- Status: Official release + arXiv v1
- Primary Source: https://arxiv.org/abs/2501.12948
- Evolution Relationship: Direct Evolution

#### Why

当可自动验证的任务提供稳定 outcome reward 时，推理能力可以通过大规模 RL 扩展；但只优化正确性会暴露可读性、语言一致性和 reward hacking 风险。

#### Principle and Mechanism

R1-Zero 从 base model 直接进行规则奖励 RL；R1 再加入 cold-start data、reasoning-oriented RL、rejection sampling/SFT 与面向一般能力和偏好的第二阶段 RL。

#### Trade-off and Evidence Boundary

纯 RL 展示 emergence，却产生可读性与语言混杂问题；多阶段 pipeline 改善可用性，但重新引入数据生产、筛选偏差与更复杂的训练闭环。蒸馏迁移的是行为分布，不等于小模型复制完整训练机制。

#### Connection and Evolution

知识树位置：`TRAIN-GRPO`（Ch33）主 owner，handoff `TRAIN-SFT`、`TRAIN-RLHF`、`TRAIN-DPO` 与 `PLATFORM-EVALUATION-SYSTEM`。Full Review Complete；Books Pending — Integration Deferred。

### Deep Analysis 2 — Kimi k1.5

- First Public: 2025-01-22
- Status: arXiv v1; Experimental
- Primary Source: https://arxiv.org/abs/2501.12599
- Evolution Relationship: Principle Reuse

#### Why

reasoning RL 的系统上限不仅由优化算法决定，也由长 rollout、采样吞吐、reward 可靠性与 train-inference mismatch 决定。

#### Principle and Mechanism

论文组合 long-context scaling、改进 policy optimization、在线数据生成与 long2short 方法，并披露训练基础设施优化。

#### Trade-off and Evidence Boundary

长 CoT 增加 test-time compute 与 rollout 成本；long2short 降低服务成本，却可能丢失探索多样性。作者 benchmark 不能外推到开放域可靠性。

#### Connection and Evolution

知识树位置：`TRAIN-GRPO`（Ch33）与 `TRAIN-CHECKPOINT`（Ch35），handoff `MODEL-LONG-CONTEXT`、`TRAIN-DISTRIBUTED-TRAINING` 与 `INFER-SCHEDULING`。Full Review Complete；Books Pending — Integration Deferred。

### Deep Analysis 3 — Chain of Agents

- First Public: 2024-06-04（论文）；2025-01-23（Google Research follow-up）
- Status: Google Research official blog + paper
- Primary Source: https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/
- Evolution Relationship: Explanatory Analogy

#### Why

超长输入可以被拆成多个 context window 的协作处理，但这把单模型 memory 限制转化为跨 agent 信息压缩和误差传播。

#### Principle and Mechanism

worker agents 顺序读取 chunks 并传递中间表示，manager 汇总答案。

#### Trade-off and Evidence Boundary

分块扩展可处理长度，却增加调用成本、信息瓶颈和不可逆摘要误差；不应把它写成对原生长上下文的替代。

#### Connection and Evolution

知识树位置：`AGENT-CONTEXT`（Ch75）主 owner，handoff `MODEL-LONG-CONTEXT`、`AGENT-RAG`、`AGENT-WORKFLOW` 与 `AGENT-MULTI-AGENT`。Full Review Complete；Books Pending — Integration Deferred。

## Full Source Review

### DeepSeek-R1

- **Candidate / Week / Score:** DeepSeek-R1 / 2025-W04 / 29/30。
- **Source Family ID:** `deepseekmath-grpo-r1zero-r1`；与 DeepSeekMath 的 GRPO 原始定义联读。
- **Source Type:** 官方 model release + 作者论文；论文后发表于 Nature。
- **First-public Date / Revision History:** release 2025-01-20；arXiv v1 2025-01-22；v2
  2026-01-04。本文按最新版 v2 复核，同时保留 2025 first-public identity。
- **Direct Primary Sources:** arXiv abstract、86 页 v2 PDF 全文及 appendix，
  https://arxiv.org/abs/2501.12948；https://arxiv.org/pdf/2501.12948；官方 repository/model cards。
- **Related Primary Sources:** DeepSeekMath/GRPO 原始论文 https://arxiv.org/abs/2402.03300；
  R1 distill model cards 只用于 artifact facts，不替代训练论文。
- **Access and Verification Status:** Verified；latest paper、method、evaluation、failed attempts、
  limitations 与 appendix 可访问。训练硬件规模、完整数据配方和 production serving contract 未披露。
- **Full-read Coverage:** 已读 metadata/revisions、Abstract、Introduction、Related Work、R1-Zero、
  GRPO/reward、R1 cold start/multi-stage pipeline、distillation、evaluation setup/results、failed attempts
  （PRM/MCTS）、limitations、conclusion 与关键 appendix。
- **Original Problem:** reasoning 能力通常依赖大量人工 reasoning demonstrations；若 outcome 可验证，
  能否从 base model 用 RL 激发探索，同时把 emergent behavior 变成可读、可部署的一般 assistant。
- **Why the Previous Design Was Reasonable:** SFT/cold-start demonstrations 给出格式、语言和稳定行为；
  PPO-style critic 提供 baseline；process reward 尝试更细 credit assignment。它们分别解决 sparse
  terminal reward、输出可读性与优化方差。
- **Changed Constraint:** 大规模可验证 math/code prompts 和 rule-based outcome reward 提供较低歧义
  的反馈，而 critic/value model 又是额外大模型状态与训练成本。
- **Mechanism:** R1-Zero 从 DeepSeek-V3-Base 直接用 GRPO 和 accuracy/format rewards 做 pure RL；
  R1 加入少量 cold-start reasoning data→reasoning-oriented RL→rejection sampling 形成 reasoning 与
  non-reasoning SFT data→全能力 SFT→第二阶段 RL（verifiable reasoning + preference/helpfulness/safety）。
  Distillation 用 R1 生成数据训练更小 dense models。
- **State Ownership:** actor policy、reference policy、optimizer 与 rollout policy versions 由 training
  runtime 拥有；group rewards 属同 prompt trajectory batch；verifier/reward functions 是独立评价接口。
  生成的 CoT 不是 production workflow authoritative state。
- **Control Flow / Data Flow:** prompt→同 policy group rollouts→rule/reward evaluation→group-relative
  normalized advantage→clipped/reference-regularized update；R1 pipeline 另将 successful samples 经
  rejection/filtering 变成 SFT data，再进入第二轮 RL。
- **Implementation Details:** 论文披露 GRPO objective、accuracy/format reward、data stages、distillation
  与部分 sampling/evaluation；未披露完整 cluster topology、rollout serving implementation、policy
  synchronization cadence 或故障恢复。
- **Evaluation Setup:** math（AIME/MATH-500 等）、code（LiveCodeBench/Codeforces 等）、knowledge、
  instruction following 与 general benchmarks；比较 R1-Zero、R1、distilled models 及公开/闭源 baselines。
- **Baselines / Ablations / Sensitivity:** R1-Zero vs multi-stage R1 是关键路线对比；论文还报告 PRM
  因 step definition、annotation/reward hacking 而难扩展，MCTS 因 token search space 与 value model
  训练困难未成为主路线。不是所有组件都有严格独立 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base/model family 已披露，
  但训练 GPU 数、precision、global batch、rollout concurrency 与 serving TTFT/TPOT contract 未完整
  公开；因此不在 Books 写成本或吞吐数字。
- **What the Evidence Actually Proves:** 在可验证任务与作者设置中，pure RL 可以出现 self-reflection、
  verification 与更长 reasoning；同时 R1-Zero 的 readability/language mixing 暴露了 pure outcome
  optimization 的边界，多阶段数据与 RL 对可用模型仍不可或缺。
- **What It Does Not Prove:** 不证明 human demonstrations 已无价值，不证明 GRPO 对所有 domain 优于
  PPO/DPO，不证明 hidden CoT faithful，也不证明蒸馏模型复制了 teacher 的训练机制或开放域可靠性。
- **Limitations / Threats to Validity:** structured output/tool use、token efficiency、language mixing、
  prompt sensitivity 与 software-engineering RL 成本仍有限；reward hacking 与 evaluator contamination
  可能存在；很多训练系统条件 Not Disclosed。
- **Trade-offs / New Failure Modes:** 移除 critic 降低 learned value state，却增加 group rollout 成本、
  within-group variance sensitivity、reward interface 风险与 policy/rollout version synchronization；
  multi-stage pipeline 改善可用性但增加 data lineage、selection bias 与 restore complexity。
- **Where the Previous Design Still Applies:** SFT/cold start 适合格式、语言与稀有行为；PPO critic 在
  group comparison 不稳定或 dense value signal 有益时仍合理；DPO 适合已有 preference pairs 且不希望
  on-policy rollout 的场景。
- **Evolution Relationship:** `Direct Evolution`：DeepSeekMath GRPO→R1-Zero pure RL→R1 multi-stage，
  三者是约束变化下的共存路线，不是后者否定前者。
- **ROADMAP Node:** `TRAIN-GRPO`（Ch33）主 owner；handoff `TRAIN-SFT`、`TRAIN-RLHF`、`TRAIN-DPO`、`TRAIN-CHECKPOINT` 与 `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** 已读 Ch24～32，重点复核 Ch27～31；并核对 Ch62 的 evaluation
  evidence 边界。
- **Existing Coverage:** Ch29 已写入 R1-Zero→R1 完整演进、pure RL 与 multi-stage 同时成立、PRM/
  MCTS failed attempts 与不得泛化的边界；当前内容已按 v2 revision 与最终 Gate 复核。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate 关闭。
  与 limitation，不追加发布摘要。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不修改 Books，不外推作者 benchmark。
- **Open Questions:** open-domain/non-verifiable reward 的扩展、rollout policy freshness、reward
  contamination、token efficiency 与可恢复 multi-stage checkpoint contract。

### Kimi k1.5

- **Candidate / Week / Score:** Kimi k1.5 / 2025-W04 / 27/30。
- **Source Family ID:** `kimi-k1-5-long-cot-rl-runtime`。
- **Source Type:** 官方作者 technical report / arXiv（Experimental）。
- **First-public Date / Revision History:** v1 2025-01-22；v2 2025-03-05；v3 2025-05-28；
  v4 2025-06-03；按 v4 全文复核。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.12599；
  https://arxiv.org/html/2501.12599。
- **Related Primary Sources:** Mooncake、Megatron、vLLM 只作为论文披露 infrastructure dependencies；
  未把其独立 benchmark 合并为 k1.5 证据。
- **Access and Verification Status:** Verified；method、RL infrastructure、evaluation/ablation 与 appendix
  可访问。proprietary model/weights、完整训练数据与 cluster size 未公开。
- **Full-read Coverage:** 已读 metadata/revisions、Introduction、long-CoT SFT、online policy mirror-
  descent variant、reward/data/sampling、long2short 四路线、pretraining、partial rollouts、hybrid
  train/inference deployment、checkpoint engine、sandbox、evaluation、ablation、conclusion 与 appendix。
- **Original Problem:** long-CoT RL 需要昂贵且长度差异极大的 rollouts；若按完整 trajectory 同步迭代，
  长样本形成 straggler，并使 training GPU 等待 inference；服务又承受更高 token cost。
- **Why the Previous Design Was Reasonable:** 完整 on-policy rollout 语义清楚、实现简单；分离 training/
  inference pools 保持 runtime 独立；long CoT 允许更充分探索。这些选择在短 rollout 和资源充足时合理。
- **Changed Constraint:** context 扩展到 128K、multimodal/verifiable tasks 与大规模 RL 后，tail length、
  weight transfer、GPU idle time 和 sandbox throughput 共同成为训练系统瓶颈。
- **Mechanism:** online policy mirror-descent variant 用 binary/rule or learned reward 与 KL regularization；
  curriculum/prioritized sampling 和 length reward 提升样本效率；partial rollout 以固定 token budget 分段，
  未完成 segment 进入 replay buffer，当前 segment 保持 on-policy、历史 segment 可复用；long2short 采用
  weight merge、shortest-correct rejection sampling、DPO 或 length-aware RL。
- **State Ownership:** central master 协调 rollout workers、trainer、reward models 与 replay buffer；
  replay buffer 持有 segment/trajectory state；etcd 持有 hybrid deployment global metadata；Checkpoint
  Engine 管 vLLM lifecycle 与 transferred model shards；sandbox 持执行环境 state。
- **Control Flow / Data Flow:** prompt→async rollout segments→replay buffer→reward/code execution→trainer
  update；train phase offload Megatron，Mooncake/RDMA 传 converted weights 给 vLLM→rollout→终止 vLLM
  释放 CUDA graph/NCCL/driver memory→恢复 training。
- **Implementation Details:** Kubernetes sidecars colocate Megatron/vLLM；shared-memory HF conversion 处理
  PP/EP 后保留 TP shards；Checkpoint Engine + etcd 广播状态；code sandbox 用 crun、cgroup reuse、
  tmpfs overlay。切换时间与 sandbox 数字是作者环境结果。
- **Evaluation Setup:** text、math/coding、vision reasoning；MMLU/IF-Eval/C-Eval、AIME 2024/MATH-500/
  LiveCodeBench/Codeforces、MMMU/MathVista/MathVision；long vs short CoT、context/model-size scaling、
  negative gradients、curriculum sampling 与 long2short 比较。
- **Baselines / Ablations / Sensitivity:** 与公开/闭源模型及 ReST/uniform sampling 比较；较小模型可用
  更长 CoT 追近较大模型，但较大模型通常 token-efficient；具体表格混合不同 provider/eval 来源，
  不能当严格同环境系统 benchmark。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 最终 RL context 128K；模型规模、
  training GPU 数、precision、global batch 和 rollout concurrency 未完整披露；sandbox 表基于 16-core
  machine；没有 production TTFT/TPOT SLO。
- **What the Evidence Actually Proves:** 作者系统把 variable-length rollout、weight handoff 与 executable
  reward 视为同一 RL data plane，并展示 partial rollout/hybrid deployment 的具体 state flow；long2short
  是 token-efficiency 分支，而非证明 long CoT 已无必要。
- **What It Does Not Prove:** 不证明 partial rollout 在任意 policy objective 下无 bias，不证明作者
  benchmark 等同开放域可靠性，也不证明 terminate/restart vLLM 是所有系统的最优资源回收方案。
- **Limitations / Threats to Validity:** proprietary model/data/cluster；没有独立复现；partial historical
  segments 的 staleness/importance correction 细节不足；conclusion 明确长-context RL efficiency、
  credit assignment 与 overthinking 仍未解决。
- **Trade-offs / New Failure Modes:** 分段减少 straggler，却引入 trajectory identity、buffer consistency、
  stale prefix 与 loss masking；colocation 提高 utilization，却增加 lifecycle coordination、weight format
  conversion、global metadata 和 restart failure；sandbox 成为安全/容量边界。
- **Where the Previous Design Still Applies:** 短 rollout 可直接同步生成；严格 on-policy 要求高时可拒绝
  historical reuse；独立 training/inference pools 在隔离与易运维优先时仍合理；long CoT 在高难任务仍
  是探索分支。
- **Evolution Relationship:** `Principle Reuse` with R1 on reasoning RL；在 system 层形成完整 rollout
  state lifecycle，不是 GRPO 或 R1 的同义实现。
- **ROADMAP Node:** `TRAIN-GRPO`（Ch33）与 `TRAIN-CHECKPOINT`（Ch35）；handoff `MODEL-LONG-CONTEXT`、
  `TRAIN-DISTRIBUTED-TRAINING`、`TRAIN-TENSOR-PARALLEL` 与 `INFER-SCHEDULING`。
- **Target and Adjacent Chapters Read:** 已读 Ch27～37，重点 Ch29、31、32、34、36/37；并核对
  Ch46、Ch52 与 Ch59 的 inference/cluster scheduling 边界。
- **Existing Coverage:** Ch29 已有 rollout/update pipeline 但未展开 partial rollout；Ch31 已定义 RLHF
  多模型 consistent snapshot；是否加入 k1.5 案例需与后续 RL runtime 候选去重。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不修改 Books，保留 staleness、credit 与恢复边界供后续判断。
- **Open Questions:** partial rollout 的 policy-lag correction、segment-level credit assignment、etcd/
  replay recovery、sandbox trust 与 train-inference artifact equivalence。

### Chain of Agents

- **Candidate / Week / Score:** Chain of Agents / 2025-W04 / 21/30。
- **Source Family ID:** `chain-of-agents-long-context-followup`。
- **Source Type:** 2024 NeurIPS/arXiv 作者论文 + 2025 Google Research 官方 follow-up Blog。
- **First-public Date / Revision History:** 论文 arXiv v1 首发 2024-06-04；Google Research Blog 发布
  2025-01-23。原 Weekly 把 Blog 日期当候选 first public，现纠正为“2025 官方 follow-up”，不是
  2025 新论文。
- **Direct Primary Sources:** https://arxiv.org/abs/2406.02818；
  https://arxiv.org/html/2406.02818；Google Research 官方 Blog。
- **Related Primary Sources:** NeurIPS 2024/OpenReview 页面；arXiv 正文作为可访问完整版本。
- **Access and Verification Status:** Verified；论文 method、experiment、analysis、ablation、limitations
  与 appendix 可读；closed model internals 与 API latency/cost 明细未披露。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、Algorithm 1、worker/manager stages、
  complexity proof、9-dataset setup、RAG/full-context/multi-agent baselines、lost-in-middle analysis、
  manager/order/multi-path ablations、limitations、implementation appendix 与官方 Blog 全文。
- **Original Problem:** RAG 可能漏掉低语义相似度但必要的 hop；full context 超过 window 或出现
  lost-in-the-middle。问题是如何在有限窗口内遍历全部 source 并保留跨 chunk evidence。
- **Why the Previous Design Was Reasonable:** RAG 只读少量相关 chunks，成本低且 provenance 清晰；
  full context 避免显式摘要链，在长度可容纳且模型有效利用时保真；两者仍是强 baseline。
- **Changed Constraint:** source 长度超过单模型有效窗口，任务还要求跨 chunk multi-hop reasoning 或
  non-query summarization，单次 retrieval/query relevance 不足。
- **Mechanism:** 按原顺序切 chunks；worker `W_i` 接收 query、当前 chunk 与上一 worker 的自然语言
  communication unit `CU_{i-1}`，输出 `CU_i`；最后独立 manager 只读 `CU_l` 生成答案。论文理论上
  将 dense full-context encoding 从 `O(n^2)` 写为分块 `O(nk)`，但仍有逐 worker decoding/call latency。
- **State Ownership:** `CU_i` 是 chain-local derived message，由下一 worker 消费；manager 只拥有最终
  synthesis call。没有 durable authoritative shared state、retry log、tenant identity 或 provenance
  pointer contract。
- **Control Flow / Data Flow:** source→ordered chunks→sequential worker calls/压缩更新→final manager；
  multi-path variant 改变阅读顺序并用 vote/judge 聚合。串行 chain 的 critical path 随 chunk 数增长。
- **Implementation Details:** 同一 backbone 通常用于 workers/manager；8K worker window；task-specific
  instructions 让 CU 成为 evidence/summary/code summary。论文没有公开 production orchestration code
  或 failure recovery semantics。
- **Evaluation Setup:** HotpotQA、MuSiQue、NarrativeQA、Qasper、QuALITY、QMSum、GovReport、BookSum、
  RepoBench-P；PaLM 2 text-bison/unicorn、Gemini Ultra、Claude 3 Haiku/Sonnet/Opus；按任务使用 F1、
  exact match、ROUGE geometric mean 或 code similarity。
- **Baselines / Ablations / Sensitivity:** Vanilla full-context、RAG（300-word chunks + reranker）、parallel
  Merge、Hierarchical；ablation 去 manager、right-to-left/permutation、multi-path vote/judge；manager 与
  order 均显著影响结果，表明不是“多 agent 数量”本身产生收益。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露 model API/window 与
  dataset 平均长度/agent 数，但 hardware、precision、batch、concurrency、wall-clock latency、cost 和
  production SLO 均 Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 9 datasets/6 models 设置中，顺序 communication+manager
  比所选 RAG/full-context/parallel multi-agent baselines 更好，并缓解部分 lost-in-the-middle；worker
  state compression 与 manager 分工是可被 ablation 的机制。
- **What It Does Not Prove:** 不证明输入“无限”可无损处理，不证明优于所有 modern long-context/RAG，
  不证明 communication unit 保留 provenance/correctness，也不证明 multi-agent 自主协作优于固定 workflow。
- **Limitations / Threats to Validity:** 论文承认 LLM-to-LLM communication 未专门训练、未探索 debate，
  cost/latency 仍需 routing 优化；serial summary error 可累积，closed APIs 与 benchmark metrics 限制复现。
- **Trade-offs / New Failure Modes:** 全 source traversal 换来线性 call/token cost和 serial latency；
  bounded CU 是信息瓶颈，早期误删不可恢复；顺序敏感、manager confusion、provider drift 与 retry
  duplication 成为新故障。
- **Where the Previous Design Still Applies:** query 可检索且证据稀疏时 RAG 更便宜；source 能完整放入
  effective context 且需要高保真时 full context 更简单；有结构化 state/parallelizable tasks 时 DAG/
  typed artifacts 优于自然语言串行链。
- **Evolution Relationship:** 与 long context/RAG 是 `Explanatory Analogy`；从系统角度更接近 fixed
  sequential workflow，不应因多次调用就写成 autonomous multi-agent replacement。
- **ROADMAP Node:** `AGENT-CONTEXT`（Ch75）主 owner；handoff `MODEL-LONG-CONTEXT`、`AGENT-RAG`、
  `AGENT-WORKFLOW` 与 `AGENT-MULTI-AGENT`。
- **Target and Adjacent Chapters Read:** 已读 Ch22、Ch70～73、Ch75～78；重点复核 Ch71/72/78。
- **Existing Coverage:** Ch71 已说明 compression loss、source links 与 typed state；Ch78 已说明 fixed
  role sequence 更像 workflow、message 不是 authoritative state。论文没有突破这些框架。
- **Integration Decision:** `Books Pending — Integration Deferred`；旧 `No Change` 结论作为 provisional input，不在 Weekly rebuild 阶段重用。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；论文没有证明链式摘要替代 long context 或 retrieval。
- **Open Questions:** CU provenance/rollback、error detection、parallelism、retry idempotency、真实 API
  cost/SLO，以及后续 structured handoff 是否能缓解 serial information bottleneck。

### Agent-R

- **Candidate / Week / Score:** Agent-R / 2025-W04 / 27/30。
- **Source Family ID:** `agent-r-revision-trajectory-self-training`。
- **Source Type:** 作者论文 + 官方 repository。
- **First-public Date / Revision History:** arXiv v1 2025-01-20；后续 revision 作为同一 family，不重复计分。
- **Direct Primary Sources:** https://arxiv.org/html/2501.11425v1；https://arxiv.org/abs/2501.11425；https://github.com/bytedance/Agent-R。
- **Related Primary Sources:** AgentGym、WebShop、ScienceWorld、TextCraft 与 ETO 只作为 environment/baseline contract，不替代本文机制证据。
- **Access and Verification Status:** Full Source Review Complete；正文、公式、三轮数据、训练设置、baseline、ablation、case 与 appendix 已核验。
- **Full-read Coverage:** metadata、Introduction、POMDP/MCTS、revision-trajectory construction、actor-selected transition point、iterative SFT、三环境评测、trajectory/iteration/multitask analyses、prompts 与 cases。
- **Original Problem:** 只克隆成功轨迹不会训练错误检测与恢复；长交互又通常只有 terminal reward，人工逐步 critique 昂贵。
- **Why the Previous Design Was Reasonable:** expert/optimal trajectory SFT 简单、监督稳定且避免失败数据污染；在短任务和可获得专家轨迹时仍合理。
- **Changed Constraint:** 部分可观测、多轮环境中的错误会级联或形成 loop，训练数据必须表达“何时偏离、怎样回到可行路径”。
- **Mechanism:** MCTS 从共享前缀产生 good/bad branches；当前 actor 找到自己可识别的首个错误点，将 bad prefix、revision signal 与相邻 good suffix 拼为 revision trajectory，再与 good/general data 混合迭代 SFT。
- **State Ownership:** environment 拥有 transition/reward；MCTS tree 拥有 branch/visit/value；actor 决定 transition point；dataset pipeline 拥有 revision lineage；新 checkpoint 重新生成下一轮数据。
- **Control Flow / Data Flow:** instruction→MCTS rollouts→terminal reward 分组→actor 扫描 bad actions→splice good suffix→revision/good/general mixture→SFT→下一轮重新采样。
- **Implementation Details:** Llama-3.1-8B-Instruct 在 AgentGym 上训练；WebShop/SciWorld/TextCraft 各自使用不同 rollout 数与 reward threshold；revision signal 来自十个模板。
- **Evaluation Setup:** 三个 text-interactive environments，测试集分别 200/200/100；比较 task reward，并分析首错定位、loop、iteration 与 single/multi-task training。
- **Baselines / Ablations / Sensitivity:** GPT-4o/Llama/AgentLM/Agent-FLAN、ETO、Direct-Revision、optimal-only、good-only、不同迭代与 task mixture；优势依赖作者 simulator/reward。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base model 与数据规模公开；GPU、precision、batch、rollout concurrency、wall-clock、token cost 与 production SLO 未披露。
- **What the Evidence Actually Proves:** 在三种作者环境中，显式训练 revision trajectories 比只用成功轨迹或末尾纠错更能恢复错误并减少 loop；transition point 是可消融机制。
- **What It Does Not Prove:** 不证明 actor 能在开放环境可靠定位真实首错，不证明 splice 后轨迹具因果一致性，也不证明 self-training 不会放大 evaluator/model 共因错误。
- **Limitations / Threats to Validity:** text simulator 与 terminal reward 边界窄；同 actor 参与数据定位和最终策略；无独立复现、真实 side effect、权限或 adversarial observation。
- **Trade-offs / New Failure Modes:** 得到 recovery supervision，却支付 MCTS rollout 与环境执行成本；新增 branch provenance、splice consistency、reward hacking、dataset drift 与 iteration rollback 问题。
- **Where the Previous Design Still Applies:** 短、确定、专家轨迹充足的任务仍适合 imitation；安全关键动作应由外部 verifier/constraint 拒绝，而不是等模型自我反思。
- **Evolution Relationship:** `Direct Evolution` from success-only imitation to failure-aware trajectory learning；与 runtime reflection 是 layering，不等同。
- **ROADMAP Node:** `AGENT-REFLECTION`（Ch80）主 owner；handoff `TRAIN-SFT`（Ch29）、`AGENT-WORKFLOW`（Ch81）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch29、Ch66、Ch79～82；重点核对 reflection、workflow state 与 evaluator authority。
- **Existing Coverage:** Books 已区分 critique、verifier 与 rollback，但 revision-data lineage 和 policy-relative transition point 仍是候选增量；本阶段不作吸收判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate 关闭。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不修改 Books，不复制 +5.59% 等脱离 environment/model/evaluator 的数字。
- **Open Questions:** transition-point calibration、branch splice 的 state validity、iteration rollback、real side-effect replay 与独立 verifier 应如何设计。

### Mobile-Agent-E

- **Candidate / Week / Score:** Mobile-Agent-E / 2025-W04 / 26/30。
- **Source Family ID:** `mobile-agent-e-hierarchy-experience-shortcuts`。
- **Source Type:** 作者论文 + benchmark/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-20；后续 revision 不改变 W04 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2501.11733v1；https://arxiv.org/abs/2501.11733。
- **Related Primary Sources:** Mobile-Eval-E、AppAgent、Mobile-Agent v1/v2 与 GPT-4o/Gemini/Claude snapshots 是 harness/baseline dependencies。
- **Access and Verification Status:** Full Source Review Complete；architecture、state formulas、benchmark、metrics、efficiency analyses、failure appendix 与 action/shortcut lists 已核验。
- **Full-read Coverage:** metadata、hierarchical framework、Manager/Perceptor/Operator/Reflector/Notetaker、Tips/Shortcuts update、error escalation、Mobile-Eval-E、backbone comparison、efficiency、limitations 与 appendices。
- **Original Problem:** 每次移动任务从零规划会重复推理、重复错误，并在跨 app 长任务中累积 perception/action failure。
- **Why the Previous Design Was Reasonable:** 单一 ReAct loop 或无持久经验的多组件 pipeline 易实现、状态少，也避免把旧 UI 经验误用于新界面。
- **Changed Constraint:** 任务变长且含重复 subroutines，系统需要分离高层目标与低层动作，并复用可验证经验来降低成本。
- **Mechanism:** Manager 管 plan/subgoal；Perceptor、Operator、Action Reflector、Notetaker分工；连续失败触发 escalation；长期 memory 分为自然语言 Tips 与带 precondition 的可执行 Shortcuts。
- **State Ownership:** Manager owns plan/subgoal/progress；Perceptor owns current visual parse；Reflector owns action outcome；Notetaker owns facts；memory store owns Tips/Shortcuts及其 preconditions。
- **Control Flow / Data Flow:** screenshot→perception→Manager subgoal→Operator action→environment transition→Reflector verification→notes/progress；重复成功/失败轨迹经 experience reflectors 更新 Tips/Shortcuts。
- **Implementation Details:** pure-vision OCR/icon grounding/captioning，不读 XML；失败先由 Operator局部处理，连续失败再上报 Manager；Shortcut 是 atomic-operation sequence。
- **Evaluation Setup:** Mobile-Eval-E 的 long-horizon multi-app tasks，使用 satisfaction、action accuracy、reflection accuracy 与 termination error；比较三个 commercial backbones。
- **Baselines / Ablations / Sensitivity:** AppAgent、Mobile-Agent v1/v2；with/without self-evolution、不同 backbone、Shortcut 与 Tips 贡献及 efficiency；评测仍由作者设备/任务集决定。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API model snapshots 与动作数可见；设备版本、并发、端到端 latency/cost、hardware/precision 与生产 SLO 未形成完整合同。
- **What the Evidence Actually Proves:** 在作者 mobile harness 中，层级职责、action reflection 与复用经验共同改善长任务成功和重复 subroutine 成本；appendix 真实展示 invalid-precondition shortcut failure。
- **What It Does Not Prove:** 不证明角色数量本身产生能力，不证明 Shortcut 可跨 UI/version 安全复用，也不证明 benchmark 成功等于权限、隐私与支付场景可部署。
- **Limitations / Threats to Validity:** perception error 会误触 Shortcut；自动生成 Shortcut 可缺步骤；closed backbones、有限 task/device distribution 与人工 metric 影响外部效度。
- **Trade-offs / New Failure Modes:** 复用换取更少调用，却新增 precondition freshness、schema/version identity、经验污染、权限扩大、错误复用、delete/supersede 和 compensation。
- **Where the Previous Design Still Applies:** 一次性任务或高变化 UI 适合从 primitives 重新规划；高风险操作应使用 typed tool/API 与 human confirmation，不依赖像素 Shortcut。
- **Evolution Relationship:** `Layering / Dependency`：single loop→role-separated workflow→derived memory；不是“更多 Agent 必然更好”。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `AGENT-MEMORY`（Ch77）、`AGENT-TOOL`（Ch78）、`AGENT-MULTI-AGENT`（Ch82）与 `PLATFORM-SECURITY`（Ch72）。
- **Target and Adjacent Chapters Read:** 已读 Ch76～84 与 Ch66/72，重点核对 information/action/workflow state ownership。
- **Existing Coverage:** Books 已要求 executable skill 有 precondition、provenance 与 rollback；本文提供 mobile-specific invalid-state evidence，但是否 refine 等待 Books 阶段。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把作者 success percentages 写成跨设备 Agent 可靠性。
- **Open Questions:** Shortcut 的 versioned precondition、permission scope、dry-run、compensation、provenance、revocation 和 cross-device calibration 如何实现。

### Demons in the Detail: Global-batch Load-Balancing Loss

- **Candidate / Week / Score:** Demons in the Detail / 2025-W04 / 27/30。
- **Source Family ID:** `moe-global-batch-load-balancing-loss`。
- **Source Type:** 作者论文。
- **First-public Date / Revision History:** arXiv v1 2025-01-20；W04 固定 v1 机制与实验合同。
- **Direct Primary Sources:** https://arxiv.org/html/2501.11873v1；https://arxiv.org/abs/2501.11873。
- **Related Primary Sources:** Switch/DeepSeek/Qwen MoE 与 aux-free routing 只作为 baseline/architecture background。
- **Access and Verification Status:** Full Source Review Complete；公式、sync/buffer算法、三模型训练、domain specialization、shuffle ablation 与结论已核验。
- **Full-read Coverage:** metadata、LBL derivation、parallel micro/global semantics、selection-count synchronization、GA buffer、120B/400B-token experiments、PPL/tasks、specialization 与 token-distribution ablation。
- **Original Problem:** 在每个 micro-batch 上平衡 expert 会把本应形成 domain specialization 的单一序列强制均摊到所有 experts。
- **Why the Previous Design Was Reasonable:** micro-batch LBL 本地可算、通信少，并能防止 expert collapse 与 EP straggler；在 batch 多样或小规模训练时有效。
- **Changed Constraint:** 大模型的 micro-batch 常只有少量序列，而 global batch 跨 DP/GA 含多域；loss 的统计作用域开始改变 router 学到的语义。
- **Mechanism:** 跨 parallel groups 同步每个 expert 的 selection frequency `f_i`，再与各组 gating probability 计算 global LBL；节点不足时在 GA steps 累积 count buffer 近似 global batch。
- **State Ownership:** router produces scores；parallel group owns local counts；collective produces synchronized counts；GA buffer owns optimizer-step scoped approximation and resets after step。
- **Control Flow / Data Flow:** token→router/top-k→local expert counts→all-reduce counts→global frequency→auxiliary gradient；GA path 在 optimizer boundary 前累积并清空。
- **Implementation Details:** 只通信 `N_expert` 维 count vector，不传 token×expert matrix；实验覆盖 3.4A0.6B、15A2.54B、43A6.6B，DP/EP 与不同 balance batch size。
- **Evaluation Setup:** 120B/400B tokens，global batch 512/1024；held-out PPL、HellaSwag、MMLU、ARC-Challenge、GSM8K 及 code/math/literature expert-frequency analysis。
- **Baselines / Ablations / Sensitivity:** micro LBL、sync global LBL、GA-buffer approximation、aux-free、shuffle-micro；shuffle 结果帮助区分“更多 tokens”与“跨序列分布”。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型 active/total 参数、tokens、global/micro batch 和 8-GPU/node context 部分披露；GPU 型号、precision、sequence length、network 与 step-time overhead 未完整披露。
- **What the Evidence Actually Proves:** 在作者三种 MoE 规模/数据合同中，LBL 的统计作用域会改变 specialization 与任务/PPL；count-vector synchronization 是可实现的 global approximation。
- **What It Does Not Prove:** 不证明 global balance 对所有 routing/data mixtures 更好，不证明 specialization 本身因果提升下游，也不证明通信在任意拓扑可忽略。
- **Limitations / Threats to Validity:** 作者栈/数据与超参未完全公开；缺 latency/network overhead 曲线、更多 seeds、capacity overflow/failure 分析和 production inference evidence。
- **Trade-offs / New Failure Modes:** 放松 sequence-level 均衡换取 specialization，却新增 count collective、GA-buffer staleness、optimizer-boundary reset、跨 rank一致性与 domain skew 风险。
- **Where the Previous Design Still Applies:** batch 本身多样、通信昂贵或需要严格每序列 expert coverage 时 micro LBL 仍合理；aux-free routing 是另一分支。
- **Evolution Relationship:** `Direct Evolution`：local statistic→global statistic；强调 objective semantics 与 parallel scope 耦合，而非简单换 loss 常数。
- **ROADMAP Node:** `TRAIN-MOE`（Ch36）主 owner；handoff `MODEL-MOE`（Ch21）、`TRAIN-TENSOR-PARALLEL`（Ch37）与 `TRAIN-COMMUNICATION`（Ch40）。
- **Target and Adjacent Chapters Read:** 已读 Ch21、Ch35～41，重点核对 router objective、EP dispatch 与 collective contract。
- **Existing Coverage:** Books 已描述 routing/load balance/capacity，但统计作用域与 GA buffer 的语义耦合可能是机制增量；等待 Books 阶段判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不保留脱离模型/data/batch/network 的精度增益。
- **Open Questions:** count sync overhead、buffer recovery、data-parallel skew、capacity overflow 与 inference expert placement 是否需要联合优化。

### MMVU

- **Candidate / Week / Score:** MMVU / 2025-W04 / 24/30。
- **Source Family ID:** `mmvu-expert-video-evaluation`。
- **Source Type:** benchmark paper + dataset/code/project artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；后续 benchmark snapshot 属同一 family。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12380v1；https://arxiv.org/abs/2501.12380；https://github.com/yale-nlp/MMVU；https://huggingface.co/datasets/yale-nlp/MMVU。
- **Related Primary Sources:** 32 个被测 model/system cards 与 CC-licensed video sources只用于 identity，不把各自声明计作 MMVU 结论。
- **Access and Verification Status:** Full Source Review Complete；construction、annotation/validation、splits、prompts、model configs、error taxonomy 与 appendices 已核验。
- **Full-read Coverage:** metadata、related benchmarks、subject/textbook/video selection、expert recruitment/pay、QA+rationale+knowledge annotation、validation、3,000-example stats、32-model eval、CoT/direct、human error analysis 与 prompts。
- **Original Problem:** 许多 video benchmark 可凭文字/常识 shortcut，且只给答案，无法区分 perception、domain knowledge 与 reasoning failure。
- **Why the Previous Design Was Reasonable:** general video QA 便于扩展和自动评分；multiple choice 成本低；在测基本感知/检索时足够。
- **Changed Constraint:** 专业视频任务要求确实观看视频、调用领域知识并解释推理；评测需要可审计 rationale 与 required-knowledge reference。
- **Mechanism:** textbook-guided 27-subject coverage；专家从 CC videos 创建 QA、solution rationale 与 knowledge；二次专家验证 video necessity/正确性；隐藏 2,000 test，1,000 validation。
- **State Ownership:** dataset record owns video/question/options/answer/rationale/knowledge/model identity；test server should own hidden labels；model run owns prompt/frame sampling/output。
- **Control Flow / Data Flow:** subject/textbook→concept→video selection→expert QA/rationale→independent validation/revision→frozen split→model prompting→exact/LLM-assisted scoring→human error analysis。
- **Implementation Details:** 3,000 questions、1,529 unique videos、4 disciplines/27 subjects；1,858 MCQ + 1,142 open-ended；3,072 initial examples中 523 revised、72 removed。
- **Evaluation Setup:** 32 frontier models，direct vs CoT prompts；accuracy across disciplines/question types；对四个模型各抽 50 errors 做人工 taxonomy。
- **Baselines / Ablations / Sensitivity:** 与 broad video/multidiscipline benchmarks作构造比较；CoT/direct comparison与text-only shortcut checks；没有系统研究 frame sampler、video compression、prompt variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model snapshots与部分 configs公开；provider hardware/precision、frame/token budget完整统一性、batch/concurrency、latency/cost和SLO未披露。
- **What the Evidence Actually Proves:** MMVU 提供比仅答案更细的 expert-video evidence contract，并暴露视觉误读、知识误用、text reliance与逻辑矛盾等可定位错误。
- **What It Does Not Prove:** 不证明 CoT faithful，不证明模型排名跨 API revision 稳定，不证明 benchmark accuracy 等于真实专业决策安全。
- **Limitations / Threats to Validity:** 只有 3,000 examples、CC-video selection bias、expert/rubric disagreement、hidden-test维护与污染风险；开放题 scoring 也可能引入 evaluator bias。
- **Trade-offs / New Failure Modes:** expert annotation提升证据密度但成本高、覆盖窄、更新慢；rationale可能成为泄漏或单一规范答案；online leaderboard需版本与访问治理。
- **Where the Previous Design Still Applies:** 大规模基础感知回归仍适合自动/通用 benchmark；高风险专业能力需要 simulation、artifact execution与human review，不能只依赖 MMVU。
- **Evolution Relationship:** `Direct Evolution`：answer-only video QA→evidence-rich expert evaluation；与 production evaluation是 layering。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-OBSERVABILITY`（Ch67）。
- **Target and Adjacent Chapters Read:** 已读 Ch23～26、Ch65～69；重点核对 evaluation unit、model/run identity 与 evidence hierarchy。
- **Existing Coverage:** Ch66 已要求 workload/model/evaluator identity 与 error taxonomy；MMVU提供 multimodal expert-rationale case，是否 refine 等待 Books 阶段。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不复制模型排行榜或把 CoT correlation 写成 causal/faithful reasoning。
- **Open Questions:** frame sampling与provider版本如何冻结；开放题 evaluator 如何校准；expert disagreement、contamination与专业风险如何进入 release gate。

### UI-TARS

- **Candidate / Week / Score:** UI-TARS / 2025-W04 / 28/30。
- **Source Family ID:** `ui-tars-native-gui-agent-action-traces`。
- **Source Type:** 作者技术报告 + 官方 repository。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；后续 revision 与 UI-TARS 版本属于同一 family，不在 W04 重复计分。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12326v1；https://arxiv.org/abs/2501.12326；https://github.com/bytedance/UI-TARS。
- **Related Primary Sources:** Qwen2-VL、OSWorld、AndroidWorld、Aguvis 与 OS-Atlas 作为 backbone/harness/baseline；不把其各自声明并入 UI-TARS 证据。
- **Access and Verification Status:** Full Source Review Complete；evolution、data pipeline、action schema、reflection/DPO、training、offline/online evaluation 与 appendix cases 已核验。
- **Full-read Coverage:** metadata、rule/framework/native evolution、perception tasks、unified actions、6M tutorials、thought augmentation、online trace bootstrapping、reflection pairs、Agent DPO、三阶段 50B-token training、10+ benchmark contract 与案例。
- **Original Problem:** 依赖 accessibility tree、专用 grounding module、手写 prompt/workflow 的 GUI agent 能快速落地，却难随平台变化共同学习 perception、reasoning 与 action。
- **Why the Previous Design Was Reasonable:** rule/RPA 在稳定界面可预测、可审计；模块化 framework 可替换组件、隔离权限并复用 frontier API，生产上仍有明确控制面价值。
- **Changed Constraint:** 跨 web/mobile/desktop 的界面、动作与任务分布持续变化，而端到端多步轨迹稀缺；人工为每个平台维护桥接规则开始成为扩展瓶颈。
- **Mechanism:** 仅以 screenshot 感知；用跨平台统一但带 platform-specific optional action 的 schema 训练 grounding/action；以 GUI tutorials 与 thought augmentation 注入多步结构；在线执行轨迹经 rule→VLM score→human review，再以 error-correction/post-reflection SFT 与 corrected-vs-error DPO 回流。
- **State Ownership:** environment 拥有真实 UI state；model context 拥有有限 observation/action/thought history；action schema 拥有可执行边界；trace pipeline 拥有 environment/model/version lineage；human/VLM filters 拥有数据 admission，而非运行时真值。
- **Control Flow / Data Flow:** instruction+screenshot+recent history→thought/action proposal→environment transition→new screenshot→success/failure filter→error localization/correction pair→SFT/DPO→下一 checkpoint 与新 online traces。
- **Implementation Details:** Qwen2-VL 2B/7B/72B 持续训练约 50B tokens；perception 数据自 screenshot+metadata 构造五类任务；action space 包含 click/tap、type、scroll、hotkey、Finished 与 CallUser；context 保留最近 observation 且最大 32K。
- **Evaluation Setup:** perception、grounding、offline trajectory 与 online OSWorld/AndroidWorld；OSWorld screenshot-only、15/50-step budgets、369 tasks、三次运行均值；AndroidWorld 116 tasks/20 apps。
- **Baselines / Ablations / Sensitivity:** GPT-4o/Claude Computer Use、frameworks 与 native models；SFT/DPO、System-1/System-2、in/out-of-domain comparisons；没有把 data component、environment drift、model scale 与 evaluator variance 完全正交拆分。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model scale、约 50B tokens、32K context 与 step budget公开；训练 hardware、precision、batch、online VM concurrency、端到端 latency/cost与 production SLO 未形成完整合同。
- **What the Evidence Actually Proves:** 在作者固定 GUI harness 中，统一视觉—动作训练、反思轨迹和偏好对比能形成可消融的端到端 agent policy；动态环境评测比离线 grounding 更接近真实闭环。
- **What It Does Not Prove:** 不证明 end-to-end model 在权限、安全、回滚和可观测性上替代模块化 workflow；不证明 benchmark 差距跨模型版本稳定，也不证明像素动作比 typed API 更安全。
- **Limitations / Threats to Validity:** 在线环境覆盖有限且可漂移；trace filtering 部分依赖 VLM/human；closed baselines、step budget、不可行任务处理与 screenshot-only contract 影响比较；论文缺独立复现与 production side-effect study。
- **Trade-offs / New Failure Modes:** 统一参数减少手工 glue，却把模块错误耦合进同一 policy；新增 coordinate/action schema drift、trace contamination、filter common-mode error、silent mis-grounding、permission leakage 与 checkpoint rollback。
- **Where the Previous Design Still Applies:** 稳定、重复、强合规 GUI 仍适合 RPA；可用 API/typed tool 时应优先显式 contract；高风险动作保留 deterministic workflow、policy check 与 human confirmation。
- **Evolution Relationship:** `Alternative Branch`：rule-based→modular framework→native policy 并非单向替代；native model 可作为 workflow 中的 proposal node，控制权仍由外部 runtime 持有。
- **ROADMAP Node:** `AGENT-TOOL-CALLING`（Ch78）主 owner；handoff `AGENT-PLANNING`（Ch79）、`AGENT-REFLECTION`（Ch80）、`AGENT-WORKFLOW`（Ch81）与 `MULTIMODAL-REPRESENTATION`（Ch23）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23、Ch77～81 中 action proposal、observation trust、reflection、workflow state 与 memory provenance 段落。
- **Existing Coverage:** Books 已明确“模型输出只是 proposal”、tool contract 与 deterministic spine；UI-TARS 的新增价值是 native action-policy 训练链及其与外部 control plane 的共存证据，留待后续 Books Gate 判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不复制排行榜，也不把作者“framework→native”叙事写成生产系统必然替代路线。
- **Open Questions:** GUI/environment version 怎样进入 trace identity；DPO pair 是否保持 state-valid；CallUser、permission、dry-run、compensation 与 trace revocation 如何联动。

### Hunyuan3D 2.0

- **Candidate / Week / Score:** Hunyuan3D 2.0 / 2025-W04 / 22/30。
- **Source Family ID:** `hunyuan3d2-shape-texture-asset-pipeline`。
- **Source Type:** 作者技术报告 + 官方 repository / released models。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；后续 model/repository revisions 属同一 family 的 artifact 演进。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12202v1；https://arxiv.org/abs/2501.12202；https://github.com/Tencent-Hunyuan/Hunyuan3D-2。
- **Related Primary Sources:** DINOv2、Stable Diffusion 2.1、Trellis、Michelangelo、Craftsman 与 texture baselines 仅作依赖/比较。
- **Access and Verification Status:** Full Source Review Complete；ShapeVAE、flow DiT、Paint、view selection、texture baking、training、三层 evaluation、user study 与 Studio extensions 已核验。
- **Full-read Coverage:** metadata、representation background、importance/uniform point sampling、SDF VAE、multi-resolution latent、dual/single-stream DiT、flow matching、geometry-aware views、reference/multiview attention、UV inpaint、implementation、shape/texture/asset metrics 与应用。
- **Original Problem:** 单一 3D generative model 难同时保证高频几何、条件一致的多视图纹理和可交付 mesh/UV artifact；生成图像不等于生产级 3D 资产。
- **Why the Previous Design Was Reasonable:** voxel/point/implicit/mesh 专用模型和分开的 texturing pipeline 易针对单一表示优化；传统 mesh simplification、UV baking 与 inpainting 可控且仍是可靠后处理。
- **Changed Constraint:** 高分辨率资产需要把 image conditioning、geometry detail、view consistency、occlusion coverage 与 downstream editability 串成同一 artifact lifecycle。
- **Mechanism:** importance+uniform sampled points 经 cross-attention 压缩为可变长度 ShapeVAE tokens并解码 SDF mesh；flow DiT 在无固定 3D-grid position 的 latent 上生成 shape；Paint 用 reference/multiview/geometry attention 生成 8～12 views，再 SR、UV baking 与 inpainting。
- **State Ownership:** ShapeVAE latent owns geometry representation；mesh/SDF owns geometric truth；camera/view set owns coverage；multiview images own provisional appearance；UV map owns committed texture artifact；Studio 后处理拥有 derived assets。
- **Control Flow / Data Flow:** image/text→condition preprocessing→flow ODE latent generation→SDF/marching cubes mesh→geometry-aware view selection→multiview diffusion→SR→UV projection/inpaint→optional simplify/animate。
- **Implementation Details:** latent sequence 最长 3072并做 multi-resolution training；DINOv2 Giant 518×518 condition；Paint 从 SD2.1 ZSNR 初始化，512²、80k steps、batch 48、LR 5e-5、1000 warmup；view dropout 从 44 views 采 6。
- **Evaluation Setup:** ShapeVAE reconstruction、image-conditioned shape generation、texturing 与 end-to-end textured assets 分开评测；使用 IoU、ULIP/Uni3D、CLIP/FID/CMMD/LPIPS及 50 volunteers×300 unselected outputs user study。
- **Baselines / Ablations / Sensitivity:** open baselines 与匿名 closed Model 1/2/3；importance sampling、representation和pipeline comparisons；缺少 end-to-end latency、failure attribution、seed variance 与每个模块的完整 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Paint 的 resolution/steps/batch/LR与 latent length公开；GPU、precision、full parameter counts、shape training budget、pipeline latency/throughput、concurrency与 SLO 未完整披露。
- **What the Evidence Actually Proves:** 在作者数据和 rendering-based contract 下，分离 shape/texture 责任、可变 latent resolution 与 geometry-aware multiview coverage 是可执行的高分辨率资产管线。
- **What It Does Not Prove:** 不证明 image-level metric 等于 topology/editability/physics correctness，不证明匿名 closed-model comparison 可复现，也不证明同一 monolithic model 应吞并全部传统 CG stages。
- **Limitations / Threats to Validity:** self-collected dataset 未充分披露；render metric 可能掩盖背面、UV seam、mesh manifold与 rigging failure；模块误差级联且用户研究/closed baselines 外部效度有限。
- **Trade-offs / New Failure Modes:** 分阶段带来可替换和可检查边界，却新增 geometry-texture identity、camera convention、occlusion hole、view inconsistency、UV commit、derived-asset provenance 与重跑成本。
- **Where the Previous Design Still Applies:** 已有精确 CAD/mesh 时无需重生成 shape；低多边形、UV repair、rigging 等传统算法在可控性/成本上仍更合适；2D-only workload 不应支付 3D artifact 成本。
- **Evolution Relationship:** `Layering / Dependency`：表示→shape generation→multiview texture→committed asset；不是 diffusion 对传统几何管线的直接替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-WORLD-MODELS`（Ch25）与 `PLATFORM-MODEL-REGISTRY`（Ch59）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23～26 的 representation、generation、world-state boundary 与 physical-action contract，并核对 Ch59 artifact identity。
- **Existing Coverage:** Ch24 已区分生成范式与 commit boundary；本文的稳定增量是 shape/texture/asset 多阶段 ownership，而非排行榜，是否 refine 留待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不保留脱离 dataset/rendering/匿名 baseline 的性能数字。
- **Open Questions:** mesh/UV/schema 如何版本化；模块级 retry 怎样避免 geometry-texture mismatch；physical validity、editability与 end-to-end latency 应如何进入 evaluation contract。

### InternLM-XComposer2.5-Reward

- **Candidate / Week / Score:** InternLM-XComposer2.5-Reward / 2025-W04 / 26/30。
- **Source Family ID:** `internlm-xcomposer25-multimodal-reward-lifecycle`。
- **Source Type:** 作者论文 + 官方 weights / training recipe repository。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；后续 model/checkpoint 更新按同一 reward family 追踪。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12368v1；https://arxiv.org/abs/2501.12368；https://github.com/InternLM/InternLM-XComposer。
- **Related Primary Sources:** VL-RewardBench、RewardBench、RM-Bench、IXC-2.5 与 PPO/BoN/data sources 构成 evaluation/training dependencies。
- **Access and Verification Status:** Full Source Review Complete；preference construction、score head/loss、freezing、PPO、BoN、data cleaning、benchmarks、length-bias ablation 与 future limits 已核验。
- **Full-read Coverage:** metadata、related reward work、text/image/video preference pipeline、model/loss/training、three applications、PPO equations/config、RM/policy evaluation、length/style sensitivity、BoN ablation、cleaning examples 与 conclusion。
- **Original Problem:** 文本 reward model 不能可靠评价 image/video-conditioned answers；缺公开多模态 RM 使训练、test-time selection 与数据治理分别使用不一致 evaluator。
- **Why the Previous Design Was Reasonable:** prompt-as-judge 易部署且可解释；domain-specific hallucination filters 在窄任务更便宜；文本 RM 在纯语言工作负载上数据更丰富。
- **Changed Constraint:** 同一 LVLM lifecycle 横跨多模态 chat、RL rollout、N-way candidate selection 和 instruction-data cleaning，需要可复用且低成本的 scalar preference signal。
- **Mechanism:** 在 IXC-2.5 上冻结 vision encoder/projector，训练 LLM+平均 token hidden-state score head，用 chosen/rejected pairwise loss；同一 RM 为 PPO reward/critic init、BoN selector 和低分数据过滤器。
- **State Ownership:** preference record owns prompt/modality/chosen/rejected/judge lineage；RM checkpoint owns scoring policy；PPO run owns policy/reference/critic identity；BoN run owns candidate set+seed；data pipeline owns quarantine decision。
- **Control Flow / Data Flow:** multimodal prompt→responses→GPT-4o/verifier preference→pair filtering/length constraint→RM training→(PPO rollout | BoN ranking | data scoring)→独立 benchmark/human checks。
- **Implementation Details:** 7B base；vision encoder/projector frozen；RM LR 1e-5、batch 256；chat PPO LR 5e-5、batch 256、gamma .99、GAE beta .95、clip epsilon .2；BoN 论文实验 N=4。
- **Evaluation Setup:** VL-RewardBench 1,250、RewardBench 2,985、RM-Bench 1,237；policy 在 WildVision/MIA/MM-MT/MM-Vet及 knowledge/reasoning/text-rich benchmarks评估，多项开放题由 GPT-4o judge。
- **Baselines / Ablations / Sensitivity:** proprietary/generative/scalar RMs、SFT vs PPO、with/without response-length constraint、BoN；论文明确发现 judge 偏爱更长回答，会让无长度约束 policy 获得更高 benchmark 分数。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/batch/LR/PPO超参公开；hardware、precision、sequence/video frame budget、rollout concurrency、training wall time、serving latency/cost与 SLO 未披露。
- **What the Evidence Actually Proves:** 在作者 preference/evaluation contract 中，一个 discriminative multimodal RM 可跨训练、selection 与 cleaning 复用；length constraint ablation 实证表明 evaluator policy 会改变“优化所得能力”的表象。
- **What It Does Not Prove:** 不证明同一 scalar 在三个决策面都校准，不证明低 reward 样本必然错误，不证明 LLM-as-judge 改善代表 human preference 或真实 task correctness。
- **Limitations / Threats to Validity:** preference 部分来自 GPT-4o/verifier，存在 common-mode bias；style/content sensitivity、开放题 judge bias、缺 video RL benchmark、无独立复现与 calibration/uncertainty 曲线。
- **Trade-offs / New Failure Modes:** 共享 RM 降低 evaluator 碎片化，却扩大单点偏差的 blast radius；新增 reward drift、policy-relative miscalibration、selection overfitting、误删 rare data 与 RM/policy version skew。
- **Where the Previous Design Still Applies:** verifiable math/code 应优先 executable reward；高风险清洗保留 quarantine+human review；窄域 classifier或规则在成本/可解释性上可能更好。
- **Evolution Relationship:** `Layering / Dependency`：preference model→training reward / inference selector / data gate；三个消费面共享 evidence source，但必须保持不同 operating point。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；handoff `TRAIN-PPO`（Ch32）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch27、Ch30～33 与 Ch66 中 preference、reward correctness、policy-relative state、evaluation independence 和 data admission 段落。
- **Existing Coverage:** Books 已覆盖 Reward hacking 与独立 Evaluation；本文提供“同一 RM 跨 lifecycle 复用”及 length/judge common-mode bias 的受限证据，留待 Books Gate 判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不复制 leaderboard，不把 RM score 当作 correctness 或通用数据质量标签。
- **Open Questions:** 三消费面的 calibration/threshold 是否应分开；RM 与 policy 如何联合版本；quarantine/review/restore怎样避免 rare-mode data 被永久删除。

### Video Depth Anything

- **Candidate / Week / Score:** Video Depth Anything / 2025-W04 / 23/30。
- **Source Family ID:** `video-depth-anything-temporal-head-keyframe-state`。
- **Source Type:** 作者论文 PDF + project/repository artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；当前同 ID HTML 错映射到无关 author response，v1 PDF/abs 保留为 authoritative event artifact。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.12375；https://arxiv.org/pdf/2501.12375v1；https://github.com/DepthAnything/Video-Depth-Anything。
- **Related Primary Sources:** Depth Anything V2、DepthCrafter、DepthAnyVideo、ChronoDepth 与 NVDS 作为 backbone/baselines。
- **Access and Verification Status:** Full Source Review Complete；v1 PDF 的 architecture、loss、long-video inference、training data、evaluation、latency、ablation 与 appendix 已核验；HTML mismatch 未被静默忽略。
- **Full-read Coverage:** metadata、MDE/video-depth history、frozen encoder+STH、OPW→SE→TGM derivation、key-frame/overlap stitching、five video+five image datasets、latency、loss/window/data ablations、long-video cases 与 conclusion。
- **Original Problem:** 强 image-depth foundation model 逐帧推理会 flicker；video diffusion 或 flow/pose prior 能增强时序一致性，却受窗口长度、速度和外部几何误差限制。
- **Why the Previous Design Was Reasonable:** 单帧模型数据多、泛化强、便宜；光流/pose 对应关系在短而稳定的相邻帧中提供显式几何约束；diffusion适合追求细节的短片段。
- **Changed Constraint:** 几分钟视频要求在固定 32-frame compute window 中维护全局 scale/shift 与局部平滑，同时不能破坏 image foundation 的表示。
- **Mechanism:** 冻结 Depth Anything V2 encoder，只训练带 4 个低分辨率 temporal-attention layers 的 STH；TGM 在同坐标且 ground-truth depth change<0.05 区域匹配 temporal depth gradient；推理用 8 overlap+2历史 key frames+22 new frames，重算后线性插值 overlap。
- **State Ownership:** frozen encoder owns per-frame features；STH owns window-local temporal state；key-frame set carries historical scale/shift anchor；overlap owns handoff blend；output video shares one affine scale/shift evaluation identity。
- **Control Flow / Data Flow:** frames→encoder(batch-folded time)→STH→window depth→select historical key frames+overlap→next 32-frame window→scale-consistent interpolation→committed depth stream。
- **Implementation Details:** 550K labeled video frames + 0.62M unlabeled images/self-training；final N=32、To=8、Tk=2、key interval=12；window 16/32/48 sensitivity shows 32 best cost-quality point。
- **Evaluation Setup:** five zero-shot video datasets（up to 500 frames）+ five image datasets；AbsRel/δ1/TAE after one video-wide scale-shift alignment；long-case includes 7,320-frame self-captured video。
- **Baselines / Ablations / Sensitivity:** DAv2、NVDS(+DAv2)、ChronoDepth、DepthCrafter、DepthAnyVideo；VideoAlign/OPW/SE/TGM losses、OA/OI/OI+KR、window sizes、video-only vs image distillation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** latency measured per 518×518 frame on one A100：VDA-L FP32 67ms、VDA-S FP32 9.1ms；baselines mix FP16/FP32；training hardware/batch、concurrency、memory、pipeline I/O与 SLO未披露，数字不可横向泛化。
- **What the Evidence Actually Proves:** 在作者数据/metrics 下，轻量 temporal head+TGM+historical key frames 能在固定窗口中降低漂移，并以接近单帧 backbone 的延迟处理更长视频；组件有明确 ablation。
- **What It Does Not Prove:** 不证明“任意长”无界不漂移，不证明 relative depth 可满足机器人 metric geometry，也不证明跨 precision baseline latency 公平或 500-frame metric 捕获分钟级 failure。
- **Limitations / Threats to Validity:** TGM 只在低变化区域计算，会回避 dynamic object/edge；Sintel short movie domain 上落后；OA 在 500 frames看似接近但 4-minute case 才显 drift；缺独立复现与内存/吞吐曲线。
- **Trade-offs / New Failure Modes:** 冻结 backbone保留泛化且省训练，却限制 temporal representation；key frames压制 drift但会传播错误历史；overlap重算/插值增加 compute、boundary latency与 stale-anchor failure。
- **Where the Previous Design Still Applies:** 静态 image、短片与逐帧无一致性要求仍用 DAv2；已有可靠 pose/flow 的 geometry pipeline可保留显式约束；高画质离线短片可接受 diffusion成本。
- **Evolution Relationship:** `Direct Evolution`：stateless frame estimate→window-local temporal head→overlap handoff→sparse historical anchors；与 world model 仅为 state principle reuse，不等于 action-conditioned dynamics。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`INFER-KV-CACHE`（Ch45）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23～25 的 temporal identity/state、Ch45 cache ownership 与 Ch66 workload/evaluator identity 段落。
- **Existing Coverage:** Books 已有 temporal aliasing、persistent state 与 window handoff原则；本文提供 key-frame anchor/overlap commit 的窄机制证据，留待 Books Gate 判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；明确保留 HTML identity anomaly，并将作者 latency 绑定 A100、518²与 precision。
- **Open Questions:** key-frame corruption怎样检测/rollback；metric depth/calibration如何接入；长视频 state checkpoint、I/O backpressure与 multi-stream batching如何设计。

### Taming Teacher Forcing / MAGI

- **Candidate / Week / Score:** Taming Teacher Forcing for Masked Autoregressive Video Generation / 2025-W04 / 23/30。
- **Source Family ID:** `magi-complete-teacher-forcing-frame-ar-video`。
- **Source Type:** 作者论文 PDF + project artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；当前 HTML 错映射到无关 author response，v1 PDF/abs 作为事件版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.12389；https://arxiv.org/pdf/2501.12389v1；https://magi-video-generation.github.io/。
- **Related Primary Sources:** MAR、MaskGIT、OmniTokenizer、GameNGen、Diffusion Forcing、Kinetics-600 与 UCF-101构成 architecture/data/baseline dependencies。
- **Access and Verification Status:** Full Source Review Complete；v1 PDF 的 problem formulation、CTF attention、exposure-bias controls、architecture、training、ablation、benchmark 与 long-range limits 已核验。
- **Full-read Coverage:** metadata、patch/frame-level factorization、MTF gap、CTF equations/masks、interval/noise embeddings、spatial-temporal Transformer+diffusion head、datasets/hyperparameters、FVD/FID、component ablation、KV cache、100-frame cases、related work与 conclusion。
- **Original Problem:** patch-level AR 具有清晰 causality/KV cache却串行步数多；masked frame model 可并行生成 frame 内 tokens，却在训练时把 masked history 当条件、推理时依赖完整自生成 history。
- **Why the Previous Design Was Reasonable:** raster/patch AR 与 language objective一致且可精确 cache；masked generation利用双向上下文提高 frame quality；固定条件窗口易训练、易控制内存。
- **Changed Constraint:** 长视频既需要 frame 内并行，又需要 frame 间 causal state/KV reuse；训练条件必须模拟推理时实际可见的完整历史，而不是另一种 mask/noise distribution。
- **Mechanism:** Complete Teacher Forcing 让每个 masked target frame 只看完整 observation history 与自身 masked tokens；frame内以 MAR-style diffusion head迭代 64 steps，frame间 causal；dynamic interval+embedding扩大 motion horizon，dynamic noise+level embedding模拟自生成 history error。
- **State Ownership:** observation frames own committed history；masked frame is mutable proposal；temporal attention mask defines visibility；KV cache owns committed frame state；interval/noise embeddings own training condition identity。
- **Control Flow / Data Flow:** committed frames+masked next frame→causal temporal/spatial attention→iterative denoise frame→commit→append KV→下一 frame；training额外采 interval与noise level。
- **Implementation Details:** interleaved 2D spatial/1D temporal Transformer、MAR MLP diffusion head；interval vocabulary 1～25、noise level 1～5；Kinetics LR2e-4/batch256/150 epochs，UCF LR1e-4/batch128/1400 epochs，256²、16/17 training frames。
- **Evaluation Setup:** Kinetics-600 50K generated videos at 64² FVD；UCF-101 2,048 videos at 256² FVD；first-frame/unconditional/video-prediction settings；64 masked iterations per generated frame。
- **Baselines / Ablations / Sensitivity:** MTF vs CTF、with/without dynamic interval/noise、AR/NAR baselines、same/different VAE comparisons、KV-cache timing；MTF有稍低 per-frame FID而 CTF有更好 sequence FVD，显示 metric trade-off。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training data/resolution/epochs/batch/LR与 frame count公开；hardware、precision、parameter scale、latency axes values、memory、parallel batch/concurrency与 production SLO 未完整披露。
- **What the Evidence Actually Proves:** 在 UCF/Kinetics作者设置中，条件可见性本身会造成训练—推理 gap；CTF及 interval/noise controls 对 FVD有消融支持，frame-level causality可复用 KV cache并从16-frame训练外推到部分100-frame案例。
- **What It Does Not Prove:** 不证明 100-frame generation普遍连贯，不证明 FVD等于 controllable world dynamics；不证明 CTF优于所有 diffusion/NAR，尤其 VAE、resolution与计算预算不同。
- **Limitations / Threats to Validity:** 100-frame成功集中于静态背景/周期运动，diving等非周期动作退化；FVD对未知未来动作不合适；没有 action conditioning、physical consistency、独立复现或完整 runtime成本。
- **Trade-offs / New Failure Modes:** frame-level factorization减少 AR steps并可 cache，却每帧仍需 64次修正；完整历史改善 causality但扩大 KV；noise/interval增强 robustness却新增 condition-control mismatch、motion-speed drift与 error accumulation。
- **Where the Previous Design Still Applies:** 图像或短视频可用 masked/NAR并行；需要 exact token likelihood 的离散序列保留 patch AR；固定短窗口/低延迟场景不一定需要长历史 KV。
- **Evolution Relationship:** `Alternative Branch`：patch AR、masked/NAR 与 frame-level masked-AR 各自交换 causality、parallelism、cache 与 correction cost；CTF修复的是 visibility contract，不是通用替代结论。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-WORLD-MODELS`（Ch25）、`INFER-KV-CACHE`（Ch45）与 `INFER-SPECULATIVE-DECODING`（Ch48）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23～25、Ch45与Ch48中 factorization、editable/committed state、training/inference mismatch、cache与correction边界。
- **Existing Coverage:** Ch24 已有 AR/diffusion/masked、commit 与 mismatch 主线；CTF给出“历史可见性契约”窄证据，是否作为受限案例进入正文留待 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把 +23% FVD 脱离 UCF/first-frame/作者配置传播，也不将 video generation称作 world model。
- **Open Questions:** frame commit能否保留可回滚边界；KV在长视频如何压缩/淘汰；interval/noise calibration怎样与用户 motion/control contract 对齐。

### EmbodiedEval

- **Candidate / Week / Score:** EmbodiedEval / 2025-W04 / 24/30。
- **Source Family ID:** `embodiedeval-interactive-predicate-evaluation`。
- **Source Type:** arXiv v1 metadata + 官方 repository/dataset/simulator + 后续作者正式全文用于机制交叉核验。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；v2 2025-04-11；后续 CVPRW 2026版本只作同 family 机制/appendix核验，不改变 W04 event date或冒充 v1实验版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.11858；https://github.com/thunlp/EmbodiedEval；https://embodiedeval.github.io/；https://openaccess.thecvf.com/content/CVPR2026W/Viscale/html/Cheng_EmbodiedEval_Evaluate_Multimodal_LLMs_as_Embodied_Agents_CVPRW_2026_paper.html。
- **Related Primary Sources:** official dataset、LEGENT simulator、predicate/metrics/action code，以及 AI2-THOR/HSSD/Objaverse/Sketchfab scene sources。
- **Access and Verification Status:** Full Source Review Complete with version boundary；v1 identity/abstract、artifact control flow/code、later official full Method/Evaluation/Appendix已核验；arXiv experimental HTML错映射与16MB PDF抓取限制被显式记录。
- **Full-read Coverage:** v1 metadata/revision、task taxonomy、unified input/output、scene/task construction、annotation/QC、simulator episode、predicate success、22-model/human/random setup、Succ/GcS/SPL、step/temperature analyses、error taxonomy、appendix action/predicate与 repository execution path。
- **Original Problem:** 静态 image/video benchmark不测 action→environment transition；传统 embodied benchmark又常要求专用连续控制、3D point或segmentation output，无法公平接入通用 MLLM。
- **Why the Previous Design Was Reasonable:** 静态 benchmark便宜、确定、易扩展；task-specific simulator对导航/操作提供精确物理接口；连续 action更接近机器人控制。
- **Changed Constraint:** 要测“通用 MLLM 作为 embodied agent”，需统一 observation/action schema，同时保留跨 navigation、interaction、social、attribute/spatial QA 的真实环境状态变化。
- **Mechanism:** simulator以 task+egocentric observation history+有限 action options驱动闭环；model只 proposal movement/interaction/answer；environment执行并返回 observation/feedback；predicates判断终态/过程；错误 answer或超过24 steps终止。
- **State Ownership:** simulator owns authoritative world state/nav graph；history owns observations/actions/feedback；action list owns admitted choices；predicate set owns success criteria；agent不能直接读取隐藏 state。
- **Control Flow / Data Flow:** reset(scene,start)→append first-person view→model选择 option→environment step→append observation/action/feedback→predicate judge→success/wrong-answer/max-step terminal→aggregate metrics/error review。
- **Implementation Details:** 328 tasks、125 scenes、5 categories、575 predicate instances、1,533 options；8 expert annotators，至少3人复核，expert demonstration+non-expert human feasibility；repository约20GB simulator data且支持 local/remote model execution。
- **Evaluation Setup:** 22 MLLMs+random+non-expert human；image models读448² observation history，video models读egocentric video；max 24 steps；Succ、multi-goal GcS与 path-weighted SPL；temperature 0作标准。
- **Baselines / Ablations / Sensitivity:** model families、random/human；按 task length、temperature、task category与 error taxonomy分析；缺 environment seed/retry、prompt/model snapshot、history compression及 harness sensitivity 的完整正交消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/API identities、448²、24-step cap与 simulator requirements 部分公开；provider hardware/precision、history token/frame budget、latency/cost、concurrency、simulator FPS与 production SLO 未完整披露。
- **What the Evidence Actually Proves:** 在统一有限动作的作者 simulator 中，静态多模态能力不能直接推出交互成功；predicate/GcS/SPL 能把最终成功、部分目标与路径效率分开，错误集中于 grounding、exploration、spatial reasoning与 planning。
- **What It Does Not Prove:** 不证明模型在连续控制或真实机器人同样失败/成功，不证明有限 option list 排除 action formulation难度后仍代表开放世界 autonomy，也不证明 2026正式版数字与 v1完全相同。
- **Limitations / Threats to Validity:** 任务/场景规模有限、合成与公开资产有 selection bias；action options泄露可行空间；sim-to-real、物理扰动、权限/安全与 irreversible action未覆盖；model/API revisions与后续论文修订需冻结。
- **Trade-offs / New Failure Modes:** 统一离散 action降低接入成本并提高可复算性，却牺牲控制连续性；predicate可执行但可能漏掉路径伤害；长 history提高信息却带来 context/cost与 stale observation。
- **Where the Previous Design Still Applies:** 静态 benchmark适合 perception回归；专用 robotics benchmark仍负责控制精度与物理真实性；真实部署需 hardware-in-loop、safety envelope与human override。
- **Evolution Relationship:** `Layering / Dependency`：static capability eval→interactive simulator→predicate-grounded artifact evidence→real/physical gate；不是用单一 simulator替代全部评测。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-EMBODIED-VLA`（Ch26）、`AGENT-PLANNING`（Ch79）与 `AGENT-TOOL-CALLING`（Ch78）。
- **Target and Adjacent Chapters Read:** 已复核 Ch26、Ch65～67、Ch78～81 的 evaluation ladder、workload identity、tool proposal、planning/exploration与 workflow evidence边界。
- **Existing Coverage:** Ch66已区分 model/harness/tool/environment；EmbodiedEval提供 predicate-owned partial/full success与有限 action-space的受限案例，留待 Books Gate 判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；明确隔离 v1事件与 later official全文，不把 25%/97.26% 脱离 model snapshot、simulator、action space和版本传播。
- **Open Questions:** v1与正式版逐表差异如何机器核对；history/window policy如何冻结；predicate coverage、unsafe-but-successful path与 sim-to-real failure如何进入 release gate。

### Condor

- **Candidate / Week / Score:** Condor / 2025-W04 / 22/30。
- **Source Family ID:** `condor-world-knowledge-tree-sft-refinement`。
- **Source Type:** arXiv technical report + 官方 dataset/repository artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；截至本次核验无后续 arXiv revision；后续 ACL 2025 接收事实不改变 W04 event date。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.12273；https://arxiv.org/pdf/2501.12273；https://github.com/InternLM/Condor；https://huggingface.co/datasets/internlm/Condor-SFT-20K。
- **Related Primary Sources:** xTuner、OpenCompass 与 CompassJudger-1 只作为训练/评测依赖；其结论不替代 Condor 正文。
- **Access and Verification Status:** Full Source Review Complete；experimental HTML 无法正确打开，已用同 ID v1 PDF、abs metadata、official repository 与 dataset 闭合。
- **Full-read Coverage:** metadata、Introduction/Related Work、World Knowledge Tree、Void/Refine pipeline、training/evaluation、data/model/task scaling、self-iteration、analysis、limitations 与 appendix prompts/examples。
- **Original Problem:** 高质量人工 SFT 数据供给收紧；seed-based synthesis 容易复制原始问题分布，纯自生成又可能放大噪声与幻觉。
- **Why the Previous Design Was Reasonable:** 人工 curated 数据提供高可信边界；seed-instruction evolution 保持任务可解释；外部 reward/filter 能阻止明显坏样本进入训练。
- **Changed Constraint:** 需要以较低人工成本扩展知识主题、任务类型与难度，同时让同一模型生成和修订大规模候选。
- **Mechanism:** 用 8,400+ tags 的动态 World Knowledge Tree 选择主题路径，再组合 7 类任务与三档难度生成约 200K QA；Condor Refine 让同一模型输出 strengths/weaknesses/suggestions，并据此重写 response；最后对数据做 SFT 与受控 scaling/self-iteration 实验。
- **State Ownership:** tree/tag snapshot、task/difficulty template 与 source provenance 属 data pipeline；Void/Refine dataset revisions 属 artifact registry；训练 checkpoint 与 judge versions 分别由 training/evaluation runtime 拥有。
- **Control Flow / Data Flow:** root/trending tags→hierarchical expansion→tag path+task+difficulty prompt→question/initial response→structured critique→refined response→dataset version→SFT→frozen benchmark/judge evaluation。
- **Implementation Details:** 单模型完成 synthesis/refinement；公开 Condor-SFT-20K 子集与 prompts；论文用 xTuner、初始学习率 2e-5、3 epochs，生成约 200K Void 与 200K Refine 数据；完整数据 lineage/filter threshold 未完全披露。
- **Evaluation Setup:** Qwen2.5、InternLM2.5、Llama3.1 的 7B～72B variants；8 个 human-preference benchmarks 以 GPT-4o 或 CompassJudger-1-32B 评判，另含 ground-truth knowledge QA；greedy inference。
- **Baselines / Ablations / Sensitivity:** official RLHF/instruct models、Tulu/EvolInstruct/WildChat/Magpie；Void vs Refine、model family/size、difficulty、data fraction、tag/task proportion与 self-iteration；缺独立人类 blind audit、generator/judge disentanglement 与多轮污染消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model families、learning rate、epochs、data sizes 与 judge identities公开；训练 hardware、precision、batch、sequence length、generation concurrency、cost、latency与 SLO 未披露。
- **What the Evidence Actually Proves:** 在作者数据、模型与 judge contract 下，tag/task/difficulty expansion 加 self-critique refinement 的 SFT 数据可改善多项被测 chat-preference 指标，并呈现一定数据/model-size sensitivity。
- **What It Does Not Prove:** 不证明 self-generated data 比人工数据更真实，不证明 judge score 等价于人类偏好，不证明多轮 self-iteration不会 model collapse，也不证明 20K/200K 规模可无条件外推。
- **Limitations / Threats to Validity:** generator、critic、refiner可能共享盲点；trending tags 有时效/版权/安全风险；model judge bias、benchmark contamination、数据去重与多轮幻觉积累均未完全闭合。
- **Trade-offs / New Failure Modes:** tree 提高 coverage 可解释性却引入 taxonomy drift；self-reflection 降低表面错误却可能强化自信幻觉；单模型降成本却增加 correlated failure；数据 scaling 增加收益同时放大 lineage/revocation成本。
- **Where the Previous Design Still Applies:** 高风险领域仍需专家数据与独立 verifier；窄域任务可继续使用 seed-based controlled synthesis；外部 reward/filter 在 self-critique 同源性过高时仍必要。
- **Evolution Relationship:** `Direct Evolution`：human/seed SFT→tag-driven coverage expansion→self-reflection refinement→受版本约束的 self-iteration；后者是数据工厂分支，不否定人工 gold data。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-SFT`（Ch29）、`AGENT-REFLECTION`（Ch80）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch27～29、Ch66 与 Ch80～81 的 data lineage、SFT contract、judge boundary 与 reflection state。
- **Existing Coverage:** Ch27 已覆盖 synthetic-data lineage、quality filter 与 contamination；Condor 提供“coverage taxonomy→critique refinement→versioned dataset”的受限案例，留待 Books Gate 判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；纠正 census 中把 Condor 误写为 embodied/multimodal evaluation 的初始描述，不修改 Books。
- **Open Questions:** tree update 怎样保留可重放 taxonomy；generator/critic/judge 如何去相关；数据撤回如何传播到 checkpoint；多轮 self-iteration何时开始放大幻觉或同质化。

### VideoLLaMA 3

- **Candidate / Week / Score:** VideoLLaMA 3 / 2025-W04 / 25/30。
- **Source Family ID:** `videollama3-vision-centric-avt-difffp`。
- **Source Type:** arXiv paper + 作者代码/model artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；v2 2025-01-23；v3 2025-06-24；本周按 v1 identity、以可访问论文正文核验机制并隔离后续 revision bleed。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13106v1；https://arxiv.org/abs/2501.13106；https://github.com/DAMO-NLP-SG/VideoLLaMA3。
- **Related Primary Sources:** SigLIP、Qwen2.5、COYO-700M、InternVL2、VideoMME/MMVU 等仅作为 backbone/data/baseline contract。
- **Access and Verification Status:** Full Source Review Complete；Method、training stages/data、implementation、evaluation protocols、limitations 与 repository identity 已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、AVT、DiffFP、VL3-Syn7M、四阶段训练、video-centric/streaming/grounding data、implementation、image/video benchmarks、protocol、discussion/limitations。
- **Original Problem:** 固定分辨率视觉 encoder 丢失细节；逐帧堆叠 token 让长视频上下文冗余且昂贵；高质量 video-text 数据少于 image-text 数据。
- **Why the Previous Design Was Reasonable:** 固定 resolution 便于预训练与 kernel 规划；均匀帧采样和完整 patch 保留直接证据；image/video 分开训练减少跨模态干扰。
- **Changed Constraint:** 模型需同时处理任意分辨率图像、最长约 180 帧视频、streaming interleaving 与 temporal grounding，又不能让视觉 token 超出 LLM context budget。
- **Mechanism:** AVT 用 2D-RoPE 替换 vision encoder absolute position 以支持动态分辨率；视频每帧 2×2 空间下采样，DiffFP 以相邻 pixel patch L1 distance、阈值 0.1 删除后续冗余 patch；SigLIP→projector→Qwen2.5 经 vision adaptation、alignment、multi-task、video-centric 四阶段训练。
- **State Ownership:** frame sampling/timestamp 与 patch coordinates 属 input pipeline；encoder/projector/compressor revisions 属 model artifact；pruned-token mask、stream order 与 context budget 属 request representation state。
- **Control Flow / Data Flow:** media decode@1fps→最多180帧→dynamic-resolution tokenization→spatial downsample→adjacent-patch DiffFP→projector→interleaved timestamp/text sequence→LLM decode。
- **Implementation Details:** 2B/7B variants；projector为两层 GELU MLP；max token 16,384、vision token 10,240（video eval扩到16K）；多阶段 differential learning rates；VL3-Syn7M 经 aspect/aesthetic/CLIP/KNN/recaption构建，video stage约2.7M conversations。
- **Evaluation Setup:** image OCR/document/chart/math/general benchmarks；video general、long-video、temporal reasoning、grounding；video最多180帧，disable sampling，多选 prompt 与 timestamp regex/mIoU protocol固定。
- **Baselines / Ablations / Sensitivity:** 同尺寸/同类公开 MLLMs 与 prior VideoLLaMA；AVT/DiffFP/data-stage贡献有设计说明与部分比较，但缺完整 threshold/frame-rate/resolution正交 ablation、end-to-end latency和真实 streaming backpressure实验。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes、token/frame上限、采样率和解码策略公开；training/eval hardware、precision、batch/concurrency、TTFT/throughput、real-time SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者训练与 benchmark contract 下，动态空间位置、受控 token compression 与 image→video curriculum 可共同维持较强图像/视频理解；论文也证明结果依赖专用 video data与 protocol。
- **What It Does Not Prove:** 不证明 pixel L1 threshold保留所有语义变化，不证明 token减少按比例降低 latency，不证明 image pretraining 可替代 video temporal supervision，也不证明可实时处理 live video。
- **Limitations / Threats to Validity:** video data质量/多样性、real-time compute与未见 audio/speech modality均由作者承认；frame sampling可能错过短事件，DiffFP对低像素差的语义变化存在 false prune。
- **Trade-offs / New Failure Modes:** AVT保留多尺度细节却增加动态 shape；DiffFP降低上下文占用却引入阈值/时序 identity；四阶段 curriculum提高迁移却扩大 dataset/model version coupling与 catastrophic forgetting治理。
- **Where the Previous Design Still Applies:** 固定 resolution适合稳定窄域和静态 batching；完整帧/patch在法证、快速细节或阈值不可信时更合理；专用 video encoder对严格时序任务仍可独立优化。
- **Evolution Relationship:** `Direct Evolution`：fixed-resolution/full-frame tokens→dynamic-resolution AVT→redundancy-aware DiffFP→timestamp/interleaved streaming representation；是条件分支而非统一替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `TRAIN-DATA`（Ch27）、`MODEL-LONG-CONTEXT`（Ch22）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch22～24、Ch27 与 Ch66 的 representation identity、token budget、data curriculum与 evaluation contract。
- **Existing Coverage:** Ch23 已拥有 codec/token compression、timestamp/provenance 与 modality routing；VideoLLaMA 3 补充 pixel-difference pruning和 image→video curriculum的受限证据，留待 Books Gate判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；benchmark数字未脱离 frame/token/model/protocol传播，也未修改 Books。
- **Open Questions:** DiffFP mask怎样进入 cache identity；live stream如何处理late frames和clock drift；threshold能否按任务/运动自适应；token reduction何时转化为真实TTFT/throughput收益。

### FilmAgent

- **Candidate / Week / Score:** FilmAgent / 2025-W04 / 23/30。
- **Source Family ID:** `filmagent-role-workflow-virtual-production`。
- **Source Type:** arXiv paper + 作者 project/code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；截至本次核验无后续 revision。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12909v1；https://arxiv.org/abs/2501.12909；https://github.com/HITsz-TMG/FilmAgent。
- **Related Primary Sources:** AgentVerse、MetaGPT、VideoDirectorGPT 与 virtual-production references只作 workflow/baseline背景；Sora webpage case不是可复现系统对照。
- **Access and Verification Status:** Full Source Review Complete；architecture、algorithms、workflow、JSON artifact、human evaluation、case、prompts 与 limitations 已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、3D space/action/camera assets、role definitions、Critique-Correct-Verify、Debate-Judge、三阶段 workflow、experiments、preference analysis、Sora discussion、limitations、JSON/prompt appendix。
- **Original Problem:** 端到端 film production横跨 plot、角色、script、动作、camera与渲染；单次生成容易产生跨场景不一致和不可执行动作。
- **Why the Previous Design Was Reasonable:** 单 agent/CoT调用少、协调成本低；生成式视频适合快速自由创作；人工 crew提供丰富隐性知识与最终审美判断。
- **Changed Constraint:** 目标变成在预定义 3D 世界中产出可执行、跨场景一致的长 artifact，需要不同责任角色围绕同一 script state反复校验。
- **Mechanism:** director生成角色/scene outline；screenwriter形成带位置/动作的 script；director、actor以 Critique-Correct-Verify修订；两名 cinematographer独立 proposal并 Debate-Judge；final JSON绑定位置、动作、shot与speech duration后交 simulator拍摄。
- **State Ownership:** director owns stage approval/commit；screenwriter owns mutable script；actors own persona constraints；cinematographers propose shots；3D engine owns executable action/camera/world state；history不是唯一 authoritative artifact。
- **Control Flow / Data Flow:** idea→profiles/scene outline→draft dialogue/position/action→critique/revise/verify loop→actor feedback aggregation→parallel camera proposals→debate/judge→committed JSON→3D simulation/render。
- **Implementation Details:** 15 locations、65 actor positions、272 shots/9 types、21 actions；GPT-4o-2024-05-13，collaboration最多3轮；JSON记录 scene/move/action/shot/current positions，speech audio决定 line duration。
- **Evaluation Setup:** 15人工构思且适配预建空间的 ideas；CoT、Solo、Group零样本；plot/profile/camera用5点Likert，随机50 actions评 accuracy；另做修订前后 preference与有限Sora case。
- **Baselines / Ablations / Sensitivity:** CoT vs same-framework Solo vs Group能分开 decomposition和collaboration；o1网页单 agent仅作弱对照；缺角色数量、轮数、prompt、judge、cost/latency、rater agreement与真实自由场景的系统消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model snapshot和3轮上限公开；provider hardware/precision、token/call cost、并发、render hardware/time、影片长度与 production SLO未完整披露。
- **What the Evidence Actually Proves:** 在15个受限idea、预建3D动作/镜头空间和作者human-eval中，显式分工与critique/debate流程优于同模型单体变体，且结构化artifact可交给确定性simulator执行。
- **What It Does Not Prove:** 不证明增加agent数量普遍优于强单agent，不证明结果外推开放3D场景、真实电影制作或任意video generation，也不证明Sora比较公平可复算。
- **Limitations / Threats to Validity:** idea/asset selection、小样本human rating、同模型角色相关错误与无rater统计；预定义动作/镜头提高可执行性同时限制任务难度；细粒度control与multimodal feedback不足。
- **Trade-offs / New Failure Modes:** role separation提升局部检查却增加通信/token/一致性成本；judge简化commit却形成单点偏差；预建world保证physics却牺牲开放性；JSON可重放却需schema/version/migration治理。
- **Where the Previous Design Still Applies:** 短创意和低风险草图可用单 agent；自由视频生成适合快速视觉探索；人工 director在高审美、法律或不可逆发布中仍应拥有最终权威。
- **Evolution Relationship:** `Layering / Dependency`：single prompt→task decomposition→role-scoped critique/debate→committed executable artifact→deterministic environment execution；不是 multi-agent 必然替代单agent。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `AGENT-MULTI-AGENT`（Ch82）、`AGENT-REFLECTION`（Ch80）与 `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）。
- **Target and Adjacent Chapters Read:** 已复核 Ch80～82、Ch24～26 与 Ch66 的 reflection/workflow/multi-agent、artifact commit和human-evidence边界。
- **Existing Coverage:** Ch81 已覆盖 deterministic spine、agentic nodes、artifact commit/replay；FilmAgent提供 role-scoped mutable state→committed JSON→simulator 的受限案例，留待 Books Gate判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把 3.98/5 或 Sora case外推为通用 multi-agent能力，不修改 Books。
- **Open Questions:** script/asset/schema revisions如何迁移；角色反馈冲突如何留下 decision trace；render/action失败如何retry/compensate；怎样以真实时延、cost和rater agreement复核multi-agent净收益。

### Test-Time Preference Optimization

- **Candidate / Week / Score:** Test-Time Preference Optimization / 2025-W04 / 24/30。
- **Source Family ID:** `tpo-textual-feedback-test-time-alignment`。
- **Source Type:** arXiv paper + 官方 code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；v2 2025-02-14；v3 2025-06-20；W04按v1事件归属，后续版本不作为新事件。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.12895；https://arxiv.org/pdf/2501.12895v1；https://github.com/yafuly/TPO。
- **Related Primary Sources:** TextGrad、FsfairX-LLaMA3-RM、Tulu 3、AlpacaEval/Arena-Hard等仅作implementation/reward/evaluation依赖。
- **Access and Verification Status:** Full Source Review Complete；此前 experimental HTML mismatch 已用同 ID v1 PDF/abs核对，当前同 ID正文可访问；机制、实验、compute analysis与limitation闭合。
- **Full-read Coverage:** metadata/revisions、Introduction/Related Work、textual optimization形式化、initialization/cache/loss/gradient/update/termination、model/RM/benchmark setup、results、width/depth、compute comparison、instruction-following limitation与appendix prompts/cases。
- **Original Problem:** training-time RLHF/DPO把偏好写入参数，更新慢且难适应请求级新偏好；传统Best-of-N只比较静态候选，不能利用反馈连续改写。
- **Why the Previous Design Was Reasonable:** 参数更新可把稳定偏好摊销到大量请求；BoN实现简单且并行；数值reward提供统一排序接口。
- **Changed Constraint:** 偏好可能按请求变化，且已有大模型能理解自然语言critique；系统可用更多test-time compute换即时适配而不改权重。
- **Mechanism:** 先采样N个response并由RM打分，缓存best/worst；policy生成比较式textual loss，再生成textual gradient和N个修订候选；新候选重新评分入cache，重复D轮，最后提交最高reward response。
- **State Ownership:** frozen policy/reward-model revisions属serving artifact；candidate/reward cache、critique、textual gradient与iteration budget属request-scoped workflow state；RM不拥有最终事实真值。
- **Control Flow / Data Flow:** query→N samples→RM scoring/cache→best/worst comparison→textual critique→update instruction→N revised samples→rescore/merge→stop at D→commit argmax candidate。
- **Implementation Details:** TextGrad prompt scaffold、vLLM generation；temperature 0.7、top-p 0.95，默认N=5、benchmark D=2，curve最多D=5；Llama-3.1 70B SFT/Instruct/DPO与Mistral 22B，两个8B reward models。
- **Evaluation Setup:** AlpacaEval2、Arena-Hard、HH-RLHF、BeaverTails、XSTest、MATH-500；official settings，HH-RLHF抽500；RM平均分、judge win-rate、refusal/compliance、pass@1与5次采样reward标准差。
- **Baselines / Ablations / Sensitivity:** SFT/DPO/Instruct、recursive revision、Best-of-N；width 5～20、depth、不同policy/RM；小型8B instruct失败案例揭示instruction-following前提；缺真实用户在线偏好、RM adversarial shift与端到端延迟/SLO实验。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/RM、N/D、4096 max context与estimated PFLOPs公开；hardware、precision、vLLM batch/concurrency、TTFT/TPOT、RM latency和生产SLO未披露。
- **What the Evidence Actually Proves:** 在作者模型、RM与benchmark contract中，反馈驱动的sequential revision可比静态BoN更有效地提高同一RM/关联judge指标，并呈现width/depth收益及instruction-following门槛。
- **What It Does Not Prove:** 不证明输出更符合真实人类或事实，不证明test-time成本低于已摊销training-time alignment，不证明reward model不可被过拟合，也不证明小模型或低延迟服务适用。
- **Limitations / Threats to Validity:** policy与RM可能共享偏差；循环主动优化同一RM而产生reward hacking；benchmark judge相关性、cache selection bias、随机采样和prompt sensitivity限制外推。
- **Trade-offs / New Failure Modes:** 不改权重获得请求级适配和可解释critique，却把成本、状态与失败移到在线critical path；更多width/depth提高搜索机会，也增加tail latency、RM blast radius、候选隐私和non-deterministic replay。
- **Where the Previous Design Still Applies:** 稳定高频偏好仍适合RLHF/DPO摊销；严格延迟SLO适合greedy/小N；RM不可信时独立verifier、rule gate或human review更可靠。
- **Evolution Relationship:** `Alternative Branch`：training-time parameter alignment 与 request-time context optimization分担不同时间尺度；TPO内部则是 BoN→反馈式revision→width/depth联合test-time scaling。
- **ROADMAP Node:** `AGENT-REFLECTION`（Ch80）主 owner；handoff `TRAIN-RLHF`（Ch31）、`INFER-SCHEDULING`（Ch56）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch31～34、Ch56、Ch66 与 Ch79～81 的 preference state、test-time budget、judge boundary与stopping policy。
- **Existing Coverage:** Ch80 已区分feedback source、executable diagnosis与stopping；TPO补充candidate cache→best/worst critique→textual update的具体在线分支，留待Books Gate判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；compute和benchmark数字保持model/RM/N/D/context边界，不修改Books。
- **Open Questions:** 如何用独立holdout verifier检测RM over-optimization；candidate cache如何加密/过期；budget怎样进入scheduler；失败修订如何rollback而不丢失已验证部分。

### Autonomy-of-Experts

- **Candidate / Week / Score:** Autonomy-of-Experts / 2025-W04 / 24/30。
- **Source Family ID:** `aoe-self-selecting-expert-activation-norm`。
- **Source Type:** arXiv research paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；v2 2025-01-23；本周按v1 identity核验。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13074v1；https://arxiv.org/abs/2501.13074；https://arxiv.org/pdf/2501.13074v1。
- **Related Primary Sources:** Mixtral、Phi-3.5-MoE、Switch/GShard、RedPajama 与 LM Evaluation Harness只作preliminary model/data/baseline contract。
- **Access and Verification Status:** Full Source Review Complete；router-removal motivation、AoE layer algorithm、factorization、small/4B training、selection/load/throughput ablations与appendices已核验。
- **Full-read Coverage:** metadata、Introduction/Background、pretrained router-removal probe、low-rank expert architecture、Top-K/Top-P/expert-choice、load/confidence analyses、efficiency/memory、4B scaling、conclusion与appendix alternative metrics。
- **Original Problem:** standard MoE把“谁适合处理token”的判断交给独立router；router无法直接观察expert内部能力，错误选择会让expert被迫适应不匹配token并浪费训练步。
- **Why the Previous Design Was Reasonable:** 小router便宜、可直接预测Top-K、易施加capacity/load loss，并在推理前避免所有expert做前置计算。
- **Changed Constraint:** 若expert中间activation norm能作为自身匹配度，decision和execution可共享表示；但必须把全expert probe成本压到可接受范围。
- **Mechanism:** 每个expert先用W_down产生低维activation；拼接所有W_down为单次matrix multiplication，按每个expert activation L2 norm排序；Top-K用缓存继续W_up/gated FFN，其他abort；router被移除，仍可加aux load loss。
- **State Ownership:** expert weights同时拥有selection signal与execution；Top-K/aux loss定义selection policy；runtime仍拥有token dispatch、capacity、placement与All-to-All，AoE并未删除这些系统责任。
- **Control Flow / Data Flow:** token hidden state→all-expert low-rank projection/cache→per-expert norm→Top-K/softmax→selected experts continue compute→weighted combine；未选cache终止。
- **Implementation Details:** small setup 12 layers/12 heads/8 experts/top-2，732M total/247M active，100B RedPajama tokens、4.2M-token batch；4B/1.18B-active model；d_low控制projection/cache，alpha_aux=0.01。
- **Evaluation Setup:** small models对ARC-E、PIQA、SIQA、WinoGrande、HellaSwag、MNLI、QNLI、SST-2等zero/three-shot；4B model同类任务；pretrained Mixtral/Phi probes在8×A800-80G、batch 50；training throughput/memory另测但hardware未在该表附近完整披露。
- **Baselines / Ablations / Sensitivity:** traditional MoE±aux loss、factorized gate、large router；d_low 64/128/256/512；Top-P、expert-choice；L1/L2/L∞ selection与node choices；load/confidence entropy；缺多机expert-parallel、production decode、小batch和更大模型验证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** probe硬件8×A800-80G与部分batch公开；training model/token/global-batch公开；training hardware、precision、sequence length、distributed topology、decode concurrency和SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者从头训练的732M/4B配置中，activation-norm self-selection可达到略高task平均分与接近传统MoE的training throughput；d_low呈质量/内存/吞吐trade-off。
- **What It Does Not Prove:** 不证明router普遍无用，不证明activation norm等价于可解释expert能力，不证明97% throughput在expert parallel或decode成立，也不证明更大/多模态/production models保持收益。
- **Limitations / Threats to Validity:** 任务与规模有限、confidence entropy不等于正确路由；all-expert low-rank probe增加memory和compute；pretrained no-router probe为OOD；分布式通信、capacity overflow与failure recovery未测。
- **Trade-offs / New Failure Modes:** decision/execution耦合减少router mismatch，却让expert内部scale承担双重语义；d_low太小产生rank bottleneck，太大增加noise/cache；expert activation scale drift会同时影响质量、负载和placement。
- **Where the Previous Design Still Applies:** standard router在低延迟、小batch、成熟EP kernel与独立可控routing policy时仍合理；hash/domain routing适合明确先验；aux loss/capacity仍可用于强负载SLO。
- **Evolution Relationship:** `Alternative Branch`：external learned router→expert-internal low-rank self-evaluation；两者共享Top-K、load/dispatch/placement contract，不是AoE删除MoE系统问题。
- **ROADMAP Node:** `MODEL-MOE`（Ch21）主 owner；handoff `TRAIN-DISTRIBUTED-TRAINING`（Ch36）与 `INFER-EXECUTION`（Ch49）。
- **Target and Adjacent Chapters Read:** 已复核 Ch16、Ch21～22、Ch36～40与Ch49的router语义、load balance、EP/All-to-All和execution mapping。
- **Existing Coverage:** Ch21 已覆盖router-owned assignment、population routing与placement边界；AoE提供“selection signal进入expert内部”的实验分支，留待Books Gate判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把作者accuracy/throughput外推到生产EP，不修改Books。
- **Open Questions:** activation norm怎样跨checkpoint校准；EP时低维probe/dispatch能否融合；capacity overflow与expert starvation如何处理；scale drift如何监测和rollback。

### Pairwise RM

- **Candidate / Week / Score:** Pairwise RM / 2025-W04 / 24/30。
- **Source Family ID:** `pairwise-rm-knockout-best-of-n`。
- **Source Type:** arXiv paper + 官方 dataset/code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；v2 2025-02-10；W04按v1事件归属。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13007v1；https://arxiv.org/abs/2501.13007；https://github.com/THU-KEG/PairwiseRM。
- **Related Primary Sources:** NumiaMath、MATH-500、OlympiadBench、Gemini-1.5-flash、Llama/Qwen与ORM/PRM baselines只作data/annotation/evaluation contract。
- **Access and Verification Status:** Full Source Review Complete；pairwise verifier、knockout algorithm、Pairwise-443K generation、training/evaluation、critic comparison、limitations与appendix已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、ORM/PRM background、generative pairwise labels、team/knockout flow、dataset filtering/generation/annotation、training、BoN16/32/64、difficulty analysis、critic comparison、limitations/ethics/future work。
- **Original Problem:** scalar ORM/PRM对不同候选独立打分，分数未必可跨answer稳定比较；多个候选都被判“正确”时难确定最终解。
- **Why the Previous Design Was Reasonable:** scalar score便于排序、cache和并行；PRM提供step-level feedback；majority vote不需训练额外selector且对同答案聚类有效。
- **Changed Constraint:** math BoN会生成大量不同答案和推理路径，系统更需要相对判别“这两个谁更可信”，而非假定绝对reward calibration稳定。
- **Mechanism:** generative Pairwise RM同时读problem和两条solution，输出CoT verification与两个correctness labels；候选按final answer分team，跨team配对淘汰，胜者晋级；同判正确时随机晋级，直到剩一条或只剩同team。
- **State Ownership:** generator owns candidate set；answer normalizer owns team identity；Pairwise RM owns comparison evidence而非truth；tournament scheduler owns bracket/random seed；final verifier/release gate应独立。
- **Control Flow / Data Flow:** sample N solutions→normalize/group answers→construct cross-team pairs→parallel pairwise verify→eliminate/advance→repeat rounds→early stop/single winner→final answer。
- **Implementation Details:** NumiaMath从约859K过滤至425,943问题；Llama-3.1-8B-Instruct每题采24解（temperature1.0/top-p0.5）；Gemini-1.5-flash标2.2M comparisons，保留双判正确的1.3M并按格式筛到443K SFT样本。
- **Evaluation Setup:** MATH-500与OlympiadBench；候选来自Llama-3.1-8B/70B-Instruct和Qwen2.5-7B-Instruct；BoN 16/32/64 accuracy；另用Qwen生成8K单解/4K pairs比较critic accuracy。
- **Baselines / Ablations / Sensitivity:** 多个ORM/PRM、majority vote、同数据critic model、majority/probabilistic critic组合、difficulty slices；缺bracket permutation/random seed、label-noise、answer-normalizer、latency/cost与out-of-domain sensitivity的完整消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** candidate/model/N与sampling参数公开；training/serving hardware、precision、context length、pair batch/concurrency、round latency、cost与SLO未披露。
- **What the Evidence Actually Proves:** 在作者math数据和BoN contract中，相对验证+tournament比被测scalar reward models和多数投票提高部分accuracy，尤其在作者定义的困难slice；也暴露多轮verification latency。
- **What It Does Not Prove:** 不证明pairwise比较传递、排序一致或跨领域有效，不证明relative improvement代表绝对通用收益，不证明teacher-generated labels无偏，也不证明随机tie不影响结果。
- **Limitations / Threats to Validity:** 训练标签来自单一proprietary teacher；过滤“判断正确”的comparison可能选择性偏差；final-answer grouping/normalization可错；tournament路径依赖、非传递偏好与多轮延迟未充分量化。
- **Trade-offs / New Failure Modes:** pairwise context提供cross-validation却将O(N)比较、round barrier和bracket state放入请求路径；并行可降wall time但增加GPU/cost；错误早轮淘汰不可恢复，tie/random seed影响复算。
- **Where the Previous Design Still Applies:** calibrated ORM适合低延迟全排序；PRM适合定位中间错误；majority vote在答案聚类稳定且verifier不可靠时仍强；executable verifier优先于learned judge。
- **Evolution Relationship:** `Alternative Branch`：scalar outcome/process score→relative pairwise verification→knockout selection；不是pairwise取代所有reward model，而是改变selection protocol与state。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `AGENT-REFLECTION`（Ch80）、`INFER-SCHEDULING`（Ch56）与 `TRAIN-RLHF`（Ch31）。
- **Target and Adjacent Chapters Read:** 已复核 Ch31、Ch56、Ch65～67与Ch80的reward/judge、evidence acquisition、budget与revision边界。
- **Existing Coverage:** Ch66 已覆盖judge不是truth、relative/listwise evidence与budgeted acquisition；Pairwise RM提供answer-team+tournament的受限 math案例，留待Books Gate判断。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；数据表一处正文“443M”与paper title/abstract/repository的443K冲突按443K记录并保留来源边界；不修改Books。
- **Open Questions:** 如何检测non-transitive cycles；bracket怎样随机化并报告variance；early elimination能否appeal/rollback；pairwise verifier与final release authority如何分离。

### Improving Video Generation with Human Feedback

- **Candidate / Week / Score:** Improving Video Generation with Human Feedback / 2025-W04 / 27/30。
- **Source Family ID:** `videoreward-flow-alignment`。
- **Source Type:** arXiv paper + preference dataset / reward-model artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04 固定 v1 的数据、机制与实验合同。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13918v1；https://arxiv.org/abs/2501.13918。
- **Related Primary Sources:** VideoGen-Eval、GenAI-Bench、VideoScore、LiFT 与 VisionReward 只用于 benchmark/baseline contract；rectified flow 与 Diffusion-DPO 用于机制来源核验。
- **Access and Verification Status:** Full Source Review Complete；preference construction、BTT ties、reward architecture、Flow-DPO/RWR/NRG、training、evaluation、ablation 与 appendix 已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、182K preference collection、multi-dimensional reward、flow matching、三种 alignment branch、VideoGen-RewardBench、human evaluation、beta/noisy-latent ablation、appendix prompt/training details。
- **Original Problem:** 现代 text-to-video 的 visual quality、motion quality 与 text alignment 不能由单一自动分数可靠代表；即使得到偏好模型，也需要区分训练时更新生成器与推理时引导采样。
- **Why the Previous Design Was Reasonable:** 单一 reward、pointwise scoring 与 cleaned-latent evaluator 接口简单；普通 flow matching 保留 base distribution；人工评估可直接判断最终视频，适合较小规模迭代。
- **Changed Constraint:** 视频错误具有多维、时序和 tie-heavy 特征，且 flow model 中间态是 noisy latent；reward 若只在 clean output 上可导，不能稳定指导中间 denoising/flow trajectory。
- **Mechanism:** 三个 special tokens 分别预测 VQ/MQ/TA；BTT loss 显式处理 ties。Flow-DPO 用 preferred/rejected video pair 更新 flow policy，Flow-RWR 以 reward 加权训练，Flow-NRG 则训练 noisy-latent reward，并在 inference 对 latent 施加 reward gradient guidance。
- **State Ownership:** dataset pipeline owns pair/tie/dimension labels；reward model owns conditional scores而非truth；flow trainer owns policy/reference state；sampler owns noisy latent与guidance schedule；human eval/release gate独立。
- **Control Flow / Data Flow:** prompt→多模型生成候选→三人标注/冲突复核→pairwise/tie dataset→multi-head reward training→选择 Flow-DPO、RWR 或 NRG branch→生成→benchmark/human audit。
- **Implementation Details:** dataset覆盖12个模型、16K prompts、108K videos与约182K pairwise annotations；reward backbone为Qwen2-VL-2B，视觉encoder全量训练、LLM linear layers LoRA；noisy-latent reward是NRG可导引导的关键接口。
- **Evaluation Setup:** VideoGen-RewardBench含人工构建26.5K triplets，GenAI-Bench覆盖较早模型；reward用ties-included/excluded pairwise accuracy，alignment在作者T2V bases与TA/TA-Hard等prompts上比较自动指标和human preference。
- **Baselines / Ablations / Sensitivity:** VideoScore、LiFT、VisionReward；Flow-DPO/RWR/NRG；constant vs timestep beta；clean vs noisy-latent reward；不同reward dimension。缺跨base模型、跨长度、seed与生产latency的完整敏感性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** reward训练披露Qwen2-VL-2B、2 fps、448×448、batch 32、lr 2e-6、2 epochs与约72 A800 GPU-hours；生成模型、视频长度/分辨率随实验项变化；precision、serving concurrency与SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者数据与flow-model设置中，多维pair/tie reward可用于评价并支持训练时或推理时三条alignment分支；noisy-latent training是中间态gradient guidance成立的必要条件之一。
- **What It Does Not Prove:** 不证明reward等于真实视频质量，不证明Flow-DPO/RWR/NRG存在通用优先级，不证明作者收益可跨model、codec、video length或human population外推，也不证明无reward hacking。
- **Limitations / Threats to Validity:** labels与prompts分布有限；候选来自12个模型会形成model-family bias；自动reward与human preference可能共偏；NRG增加sampling compute；论文未给完整production workload或OOD safety分析。
- **Trade-offs / New Failure Modes:** 多维reward提高诊断性却增加标签、模型与权重校准；training-time alignment固化偏好并需重训，inference guidance可调但增加每步反向/采样成本；reward hacking、dimension conflict与noisy gradient会产生新失败。
- **Where the Previous Design Still Applies:** clean-output ORM适合离线排序；人工评估适合高风险release；未对齐的base flow model保留分布多样性；低延迟场景可拒绝NRG guidance。
- **Evolution Relationship:** `Alternative Branch`：final-output human preference→multi-dimensional reward→training-time Flow-DPO/RWR 与 inference-time Flow-NRG；三条分支不是单向替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `TRAIN-RLHF`（Ch31）、`TRAIN-DPO`（Ch34）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23～25、Ch31、Ch34与Ch65～67的generation state、preference proxy、evaluation contract和evidence boundary。
- **Existing Coverage:** Ch24已有proposal/correction与multimodal reward边界，Ch31/34已有preference proxy；本研究提供flow模型下training/inference alignment分叉的完整受限案例。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；所有性能数字绑定作者模型、数据、视频设置与硬件，不修改Books。
- **Open Questions:** 三维reward如何做Pareto或policy weighting；NRG的每step成本与稳定性如何量化；OOD model/long-video的calibration如何检测；reward与release authority怎样隔离。

### Sigma / DiffQKV

- **Candidate / Week / Score:** Sigma / DiffQKV / 2025-W04 / 27/30。
- **Source Family ID:** `sigma-diffqkv-asymmetric-attention`。
- **Source Type:** arXiv architecture/system paper + official implementation artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04按v1归属，后续revision仅作同family核验。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13629v1；https://arxiv.org/abs/2501.13629。
- **Related Primary Sources:** GQA/MQA、FlashAttention-2、KV-cache compression、PagedAttention与作者system-domain benchmark定义用于比较边界。
- **Access and Verification Status:** Full Source Review Complete；Q/K/V differential study、AugQ、FlexHeadFA、system/general data、hardware profiling、long-context sensitivity、limitations与appendix已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、1B/100B-token controlled studies、five observations、DiffQKV/GroupSharing/AugQ、FlexHeadFA、KET/CEET setup、prefix/output sweep、system-domain corpus/AIMicius、general evaluation、appendices与future work。
- **Original Problem:** GQA通常把K/V head数绑定，但KV cache的两个分量未必有相同冗余；若统一压缩，可能用不必要的V损失换取有限内存收益。
- **Why the Previous Design Was Reasonable:** balanced GQA接口规则、kernel成熟且短上下文效率好；MQA/GQA以统一KV head group简化layout、broadcast与cache管理。
- **Changed Constraint:** 长prefix和长output使KV traffic/footprint主导，而controlled experiments显示K比V更可压缩，Q又不进入cache、可以用额外capacity补偿质量。
- **Mechanism:** DiffQKV独立设置Q/K/V head count与head dimension，压缩K多于V并增宽Q；GroupSharing映射不平衡head；FlexHeadFA从FlashAttention-2扩展独立K/V address indices，以执行不对称layout。
- **State Ownership:** model architecture owns head geometry；checkpoint/config owns projection与group mapping；KV allocator owns不同K/V shape与identity；kernel/runtime ownsaddress map与layout；scheduler不得把不同config cache混用。
- **Control Flow / Data Flow:** hidden state→asymmetricQ/K/V projection→GroupSharing映射→FlexHead attention→仅K/V按各自layout写cache→decode逐步读取；AugQ只增加当前step compute，不进入KV cache。
- **Implementation Details:** controlled 1B models为22 layers、hidden 2048并用100B FineWeb-Edu tokens；Sigma-1.5B示例采用4 K heads、16 V heads和augmented Q；H100 profiling比较Cuda Event和nsys kernel time。
- **Evaluation Setup:** architecture sweeps比较K/V压缩与Q/FFN增容；效率在单张NVIDIA H100 80GB上扫描prefix/output length；另训练system-domain与general-domain 1.5B模型进行任务评估。
- **Baselines / Ablations / Sensitivity:** GQA standard、不同K/V head与dimension、AugQ vs AugF、GroupSharing、kernel/cuda-event两种测量、prefix/output grid。缺多GPU、batch/concurrency、不同GPU、quantization与paged allocator的系统消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100 80GB、Sigma/Std 1.5B与最长64K prefix/output披露；profiling实现与序列网格公开；precision、batch/concurrency、TTFT/TPOT与production SLO未形成完整合同。
- **What the Evidence Actually Proves:** 在作者受控模型中K/V有不同压缩敏感性，Q增容与FFN增容可叠加；在披露H100、长上下文单模型profile下，K cache减少可越过AugQ额外compute并形成收益。
- **What It Does Not Prove:** 不证明K总比V可压缩，不证明33.36%适用于短context、其他GPU、batching或production server；作者数据不证明domain model通用更好，也不证明不平衡layout已被所有runtime高效支持。
- **Limitations / Threats to Validity:** 关键结论来自1B/1.5B规模；短上下文CEET可比Std慢40.11%；system corpus和benchmark具作者域偏；缺independent replication、fleet cost和failure analysis。
- **Trade-offs / New Failure Modes:** 减K cache换取AugQ compute、特殊kernel与更复杂config/cache identity；长context收益伴随短context回归；kernel fallback、shape mismatch、checkpoint conversion与cache corruption成为新风险。
- **Where the Previous Design Still Applies:** balanced GQA适合短context、成熟kernel和跨框架可移植性；MQA适合极端cache约束；post-training eviction/prompt compression适合不能重训architecture的资产。
- **Evolution Relationship:** `Alternative Branch`：balanced GQA→separate K/V scaling + AugQ→specialized flexible-head kernel；与paged cache/eviction是layering而非替代。
- **ROADMAP Node:** `MODEL-ATTENTION`（Ch15）主 owner；handoff `INFER-KV-CACHE`（Ch45）与 `INFER-TENSORRT-LLM`（Ch49）。
- **Target and Adjacent Chapters Read:** 已复核 Ch14～16、Ch44～46与Ch48～50的attention geometry、KV capacity、kernel plan和workload contract。
- **Existing Coverage:** Ch15已有MHA→MQA/GQA质量/容量分支，Ch45/49已有logical KV与kernel/layout边界；Sigma提供K/V非对称设计与短/长context交叉点证据。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；33.36%保留为H100、1.5B、64K/64K作者profile，不修改Books。
- **Open Questions:** 不同scale和layer是否应有不同K/V ratio；paged allocator如何表达异构K/V blocks；quantization与DiffQKV是否叠加；short-context routing能否避免回归。

### Image Generation with CoT

- **Candidate / Week / Score:** Image Generation with CoT / 2025-W04 / 25/30。
- **Source Family ID:** `autoregressive-image-parm-verification-reflection`。
- **Source Type:** arXiv paper + reward/data artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04固定v1实验结论。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13926v1；https://arxiv.org/abs/2501.13926。
- **Related Primary Sources:** Show-o、GenEval、LLaVA-OneVision、ORM/PRM、DPO与test-time compute文献用于baseline和机制依赖。
- **Access and Verification Status:** Full Source Review Complete；ORM/PRM、iterative DPO、reward guidance、PARM/PARM++、self-correction、data recipes、ablation与appendix已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、task/setup、ORM-vs-PRM、DPO迭代、training/test-time组合、PARM三任务、PARM++ reflection、自修正SFT、GenEval、implementation/data appendix与additional results。
- **Original Problem:** autoregressive image token generation也存在路径不稳定，但语言CoT的step verifier不能直接迁移：早期图像模糊不可判，晚期分支又趋同。
- **Why the Previous Design Was Reasonable:** final-output ORM只需判断完成图像；PRM在语言推理中可定位步骤错误；DPO把偏好固化进参数，best-of-N在无需重训时提供简单选择。
- **Changed Constraint:** 图像中间态的可观察性随step变化，统一step score既会误判早期模糊状态，也难区分已收敛路径；reflection还需要跨模态诊断而非纯文本自批评。
- **Mechanism:** PARM先判断当前step是否清晰可评，再预测其通向高质量终局的potential，最后对剩余paths作outcome ranking；PARM++对最终图像生成misalignment diagnosis，模型以prompt、旧图和诊断进行最多3轮self-correction。iterative DPO与test-time verification可组合。
- **State Ownership:** generator owns image-token trajectory；verifier ownsprovisional evidence而非truth；branch controller ownsN candidates、pruning与iteration；reflection text是derived diagnosis；accepted image由final gate提交。
- **Control Flow / Data Flow:** prompt→AR image candidates→ORM/PRM/PARM阶段性判断→prune/rank→可选DPO/reward-guided training→PARM++ final audit→diagnosis→image self-correction→accept/stop。
- **Implementation Details:** Show-o为generation baseline，LLaVA-OneVision-7B为zero-shot/fine-tuned verifier；ORM ranking约288K examples，PARM appendix披露120K clarity、80K potential与200K BoN-selection data；best-of-N设N=20。
- **Evaluation Setup:** GenEval六类compositional criteria；比较baseline、zero/fine-tuned ORM/PRM、DPO/iterative DPO、训练与test-time组合、PARM/PARM++及reflection ablation。
- **Baselines / Ablations / Sensitivity:** ORM vs PRM、alignment vs verification、三种组合、PARM stages、reflection on/off、自修正SFT。缺不同generator、verifier family、N/iteration cost、human preference与OOD prompt的完整敏感性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model和N=20公开；training hardware、precision、image-token length、batch、并发、每图latency/cost与SLO未完整披露，因此作者百分比不外推。
- **What the Evidence Actually Proves:** 在Show-o+GenEval作者设置中，final ORM优于直接套用PRM；训练时alignment与test-time verification表现出互补；stage-aware potential判断和external diagnosis可改善作者指标。
- **What It Does Not Prove:** 不证明生成图像在语义上“推理”，不证明PARM diagnosis真实或因果，不证明+10%可跨generator/benchmark外推，也不证明反复自修正不会reward hack或退化。
- **Limitations / Threats to Validity:** 单一AR generator与自动benchmark；verifier和training data可能共偏；self-correction SFT本身使baseline下降2%；N=20与最多3轮带来显著未量化compute。
- **Trade-offs / New Failure Modes:** verifier提高路径选择却引入branch compute、judge bias与early pruning；parameter alignment降低每次搜索但可能改写原能力；reflection允许局部修复，也可能循环、过修正或把错误诊断固化。
- **Where the Previous Design Still Applies:** single-pass生成适合低延迟；final ORM适合中间态不可观察时；DPO适合稳定偏好和重复流量；human review适合高风险创作与无法自动scoring的内容。
- **Evolution Relationship:** `Layering / Dependency`：AR candidate generation→outcome verification→stage-aware potential verification→external diagnosis and bounded correction；与DPO形成training/test-time两条互补分支。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `AGENT-REFLECTION`（Ch80）、`TRAIN-DPO`（Ch34）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23～25、Ch33～34、Ch65～67与Ch79～81的AR commit、preference optimization、verifier和reflection stopping边界。
- **Existing Coverage:** Ch24已有proposal/verification/correction主线，Ch80已有external feedback和stop/escalate；该论文提供图像中间态可观测性改变verifier设计的具体证据。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把CoT名称当成faithful reasoning证据，不修改Books。
- **Open Questions:** PARM分数如何校准；branch pruning如何保留diversity；diagnosis是否能由独立视觉/规则证据验证；compute budget和停止策略怎样联合优化。

### Temporal Preference Optimization

- **Candidate / Week / Score:** Temporal Preference Optimization / 2025-W04 / 24/30。
- **Source Family ID:** `video-lmm-temporal-preference-optimization`。
- **Source Type:** arXiv paper + official code/data/checkpoint artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；v2 2025-01-30；v3 2025-09-01。W04按v1归属并以v1 PDF复核。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.13919；https://arxiv.org/pdf/2501.13919v1。
- **Related Primary Sources:** LongVA、LLaVA-Video、LongVideoBench、MLVU、Video-MME与DPO定义用于training/evaluation contract。
- **Access and Verification Status:** Full Source Review Complete；experimental HTML错映射仍保留，已用同ID v1 PDF闭合method、data、training、ablation、appendix与artifact声明。
- **Full-read Coverage:** metadata/revisions、Introduction/Related Work、DPO formulation、localized/comprehensive data generation、LLM post-filter、SFT+DPO objective、LongVA/LLaVA-Video settings、three benchmarks、ablation、reproducibility与implementation appendix。
- **Original Problem:** long-video LMM可能依赖均匀采样或语言先验回答，却没有学会把问题绑定到真正相关的temporal segment；普通response preference没有构造这种因果对照。
- **Why the Previous Design Was Reasonable:** SFT用完整视频问答学习一般能力；均匀frames简单可扩展；人工偏好直接但昂贵；标准DPO无需显式reward model。
- **Changed Constraint:** 长视频中relevant evidence稀疏，系统能通过替换为irrelevant或incomplete clips自动产生“看见正确证据/看不全或看错证据”的contrastive responses。
- **Mechanism:** localized pair用ground-truth relevant frames生成preferred response、irrelevant frames生成rejected；comprehensive pair以完整视频为preferred、incomplete segment为rejected；LLM post-filter剔除不一致pairs，再以DPO loss与SFT loss混合更新video-LMM。
- **State Ownership:** dataset curator owns clip manipulation与pair provenance；teacher/post-filter ownsquality filter而非truth；policy/reference checkpoints与SFT mix由trainer owns；video frame selection identity必须随example保存。
- **Control Flow / Data Flow:** annotated video/query/relevant frames→construct relevant/full and irrelevant/incomplete clips→same LMM生成responses→LLM post-filter→preference tuple→DPO+SFT training→long-video evaluation。
- **Implementation Details:** LLaVA-Video分支从原178K SFT data抽子集生成10K preference pairs；LongVA与LLaVA-Video分别设置beta/alpha；训练使用8×A100 80GB、batch 64；代码、数据和weights声明公开。
- **Evaluation Setup:** LongVideoBench、MLVU、Video-MME；LongVA-7B和LLaVA-Video-7B bases；报告无/有字幕条件，并比较TPO前后。
- **Baselines / Ablations / Sensitivity:** base models、TPO without/with post-filter、localized/incomplete与irrelevant mix ratio 10:0到0:10；缺frame-budget、clip-length、teacher/filter错误、不同base size和seed的完整敏感性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B bases、8 A100 80GB、batch64与10K pairs公开；precision、具体frame/token budget、训练时长、serving concurrency/latency/SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者两个7B bases和三个benchmark上，构造temporal contrastive pairs并保留SFT mix可改善作者long-video scores；post-filter与平衡两类negative在reported setup中有增益。
- **What It Does Not Prove:** 不证明模型真正学会causal temporal reasoning，不证明收益可跨sampling policy/video domain/teacher外推，不证明自动negative没有shortcut，也不证明production长视频成本下降。
- **Limitations / Threats to Validity:** negatives由裁剪规则产生，可能留下人工模式；LLM filter引入teacher bias；benchmark答案可能受字幕/语言prior影响；frame/token与latency contract不完整。
- **Trade-offs / New Failure Modes:** 自动pair降低人工成本却可能优化clip-manipulation shortcut；DPO提高grounding但可能损伤general SFT能力，因此引入alpha mix；保存clip lineage和filter version成为新的data governance状态。
- **Where the Previous Design Still Applies:** 普通SFT适合无temporal annotation数据；retrieval/frame selection可在不改模型时降成本；完整视频输入在证据稠密或定位器不可信时仍合理。
- **Evolution Relationship:** `Direct Evolution`：full-video SFT→temporal counterfactual preference pairs→post-filtered DPO+SFT；不是用偏好训练取代frame retrieval或完整输入。
- **ROADMAP Node:** `TRAIN-DPO`（Ch34）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`MODEL-LONG-CONTEXT`（Ch22）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch22～24、Ch31～35与Ch65～67的temporal identity、DPO pair、data lineage和benchmark boundary。
- **Existing Coverage:** Ch34已有pair provenance、synthetic negative与SFT mix边界；该论文提供用时间片段干预构造偏好的multimodal实例，等待Books Gate判断是否新增机制。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；HTML mismatch未被删除，benchmark保留model/GPU/data/filter条件，不修改Books。
- **Open Questions:** negative clip是否引入可检测shortcut；relevant-frame annotation成本如何扩展；post-filter disagreement如何审计；retrieval和TPO如何联合而不重复优化。

### O1-Pruner

- **Candidate / Week / Score:** O1-Pruner / 2025-W04 / 23/30。
- **Source Family ID:** `o1-pruner-length-harmonizing-finetuning`。
- **Source Type:** arXiv paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；W04按v1机制与实验归属。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12570v1；https://arxiv.org/abs/2501.12570。
- **Related Primary Sources:** PPO、DPO、SFT、MATH/GSM8K/GaoKao与Marco-o1/QwQ model artifacts用于baseline定义。
- **Access and Verification Status:** Full Source Review Complete；length disharmony、constrained objective、off-policy PPO-style loss、data/baselines、results、lambda/difficulty ablation与conclusion已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、instance/distribution length analysis、problem setup、Lagrangian objective、reference sampling、PPO-style loss、model/data/baselines/metrics、time-cost、lambda与difficulty analysis。
- **Original Problem:** long-thought model不会按instance difficulty稳定分配token；某些短trajectory已正确，继续生成只增加延迟和成本。
- **Why the Previous Design Was Reasonable:** 长CoT扩大搜索与verification机会；prompt控制不改参数；SFT/DPO用最短正确解提供直接conciseness signal；PPO trust-region降低大更新风险。
- **Changed Constraint:** 同一prompt可从reference policy预采样多条不同长度/正确性的responses，使效率目标能相对于该prompt自身baseline定义，而非全局固定长度阈值。
- **Mechanism:** 对每题预采K条reference responses，估计平均长度和accuracy；Length-Harmonizing Reward结合reference-length/current-length ratio与accuracy相对baseline的Lagrange penalty，再以off-policy PPO-style clipped objective训练。
- **State Ownership:** reference policy ownssampling distribution；dataset storesper-prompt baseline statistics；verifier ownsaccuracy signal；trainer ownsactor/optimizer/lambda；serving runtime仍需要独立budget/stop policy。
- **Control Flow / Data Flow:** prompt→reference K samples→verify accuracy/count tokens→compute per-prompt mean baseline→assign length-accuracy reward→off-policy clipped update→math benchmark/latency proxy evaluation。
- **Implementation Details:** 论文在Marco-o1-7B与QwQ-32B相关设置上研究；SFT选两条最短正确解，DPO以短正确为chosen、最长为rejected；主方法用reference samples构造approximate advantage。
- **Evaluation Setup:** MATH、GSM8K与数学GaoKao test sets；metrics为accuracy、average output length和作者定义AES；另比较生成time-cost。
- **Baselines / Ablations / Sensitivity:** fast-solving prompt、SFT、DPO；lambda=0/1/2/5；按题目难度切片。缺K、sampling temperature、verifier error、跨领域、长上下文和production queueing敏感性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model families和token length metric公开；training/inference hardware、precision、K、batch/concurrency、prompt length、KV footprint、TTFT/TPOT与SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者数学任务与models上，output length与accuracy不是单调关系；相对reference的length-accuracy reward可得到作者定义的折中点，lambda提高通常同时提高accuracy和length。
- **What It Does Not Prove:** 不证明更短CoT更faithful或更易验证，不证明token数等于实际cost，不证明方法优于动态serving budget/early exit，也不证明跨任务保留能力。
- **Limitations / Threats to Validity:** accuracy verifier适用于可验证math而非开放域；AES是作者proxy；off-policy data受reference覆盖限制；缺hardware latency、seed variance和generalization/forgetting分析。
- **Trade-offs / New Failure Modes:** 减少reasoning token可降decode work，却可能截断难题探索；预采样K次把成本移到训练data生成；错误verifier或偏置lambda会奖励短但脆弱的答案。
- **Where the Previous Design Still Applies:** 长CoT适合难度未知且verification稀疏的任务；prompt/serving budget适合不重训资产；SFT/DPO适合高质量短解数据充分时。
- **Evolution Relationship:** `Alternative Branch`：fixed long reasoning→prompt/SFT/DPO conciseness→per-prompt reference-relative constrained RL；它优化policy分布，不替代runtime stop/scheduling。
- **ROADMAP Node:** `TRAIN-GRPO`（Ch33）主 owner；handoff `TRAIN-DPO`（Ch34）、`INFER-SCHEDULING`（Ch56）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch31～35、Ch55～56与Ch65～67的relative reward、DPO branch、reasoning budget和cost/evidence contract。
- **Existing Coverage:** Ch33已有group-relative reward与trajectory lifecycle，Ch56已有budget-aware scheduling；O1-Pruner提供per-prompt length baseline作为另一relative-control branch。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不将token reduction写成真实硬件speedup，不修改Books。
- **Open Questions:** K与temperature如何影响baseline；verifier噪声下约束是否稳定；可否在线按difficulty分配budget；length、KV memory和queue SLO如何联合优化。

### SRMT

- **Candidate / Week / Score:** SRMT / 2025-W04 / 23/30。
- **Source Family ID:** `srmt-shared-recurrent-memory-mapf`。
- **Source Type:** arXiv paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-22；W04固定v1事件与实验合同。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13200v1；https://arxiv.org/abs/2501.13200。
- **Related Primary Sources:** RMT、MAMBA、QPLEX、ATM、RATE、POGEMA、RHCR与Follower planning用于baseline/evaluation contract。
- **Access and Verification Status:** Full Source Review Complete；POMAPF formulation、shared-memory architecture、training、Bottleneck/POGEMA evaluation、ablations、memory analysis与appendix已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、Dec-POMDP formulation、spatial encoder/actor-critic、RMT memory pooling/broadcast、Bottleneck与lifelong MAPF metrics、decentralized/planning baselines、training hyperparameters和memory analysis。
- **Original Problem:** 部分可观察multi-agent pathfinding中，每个agent只见局部state；显式预测或消息协议成本高，独立memory又无法传播其他agent的意图。
- **Why the Previous Design Was Reasonable:** independent recurrent memory避免通信与central bottleneck；central planner拥有全局state并能协调；explicit message让协议可解释；memoryless reactive policy成本最低。
- **Changed Constraint:** 多agent需要在狭窄通道和拥堵地图隐式协调，同时希望保持shared decentralized policy与对未见地图/更多agents的可扩展性。
- **Mechanism:** 各agent把局部observation编码并更新recurrent memory；每步pool所有agent working-memory tokens，形成shared memory并广播回每个agent，再由shared actor policy独立选择action。
- **State Ownership:** environment owns authoritative positions/goals；每agent owns local observation/history；shared-memory operator owns pooled latent snapshot；shared policy parameters由trainer owns；latent memory不是可审计事实或durable Agent memory。
- **Control Flow / Data Flow:** global state→per-agent local observations→spatial encoder→individual recurrent memory→global pool/broadcast→per-agent attention/core→actor actions→joint transition/reward→next step。
- **Implementation Details:** homogeneous agents共享policy；ResNet spatial encoder+actor-critic；MAPF ablations含RMT、Attention、Empty、GRU；LMAPF配置披露8 heads/512 hidden、batch16384、8 workers、1e9 steps与11×11 observation patch。
- **Evaluation Setup:** two-agent Bottleneck sparse/dense reward；POGEMA Maze/Random/Puzzle/Warehouse/MovingAI；CSR、ISR、SoC、throughput、cooperation、OOD、scalability等metrics。
- **Baselines / Ablations / Sensitivity:** MAMBA、QPLEX、ATM、RATE、RRNN、RMT、Attention、Empty、GRU；另比较RHCR/MATS-LP/MAPF-GPT/Follower等planning/hybrid methods。缺通信噪声、agent dropout、stale memory、heterogeneous agents和network cost消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** network sizes、batch、workers、steps、episode length和observation patch公开；hardware、precision、wall-clock、message bytes/latency与real-time SLO未披露。
- **What the Evidence Actually Proves:** 在作者Bottleneck与POGEMA设置中，pooled/broadcast recurrent latent memory相较多种decentralized ablations改善部分coordination/OOD/scalability指标；central RHCR仍在多个coordination指标更强。
- **What It Does Not Prove:** 不证明implicit memory可解释、可安全通信或优于central planning，不证明扩展到异构/开放Agent，不证明latent pooling解决长期credit或durable memory governance。
- **Limitations / Threats to Validity:** toy/gridworld和shared homogeneous policy；global pooling假定同步可见所有memory；通信成本、failure recovery、安全与现实传感/action误差未量化；部分结论依赖复合normalized metrics。
- **Trade-offs / New Failure Modes:** implicit broadcast降低手工protocol设计，却引入O(agent count) shared state、同步barrier、latent entanglement和poisoning；decentralized action保留scalability但无法达到central planner的全局协调上限。
- **Where the Previous Design Still Applies:** independent policy适合弱耦合/通信受限；central planner适合全局state可用和高冲突；explicit message适合需要审计/权限的协作；hybrid planning在拥堵环境仍有优势。
- **Evolution Relationship:** `Alternative Branch`：independent recurrent memory→pooled latent broadcast→learning/planning hybrid；不是通用Agent memory或多Agent通信的单向替代。
- **ROADMAP Node:** `AGENT-MULTI-AGENT`（Ch82）主 owner；handoff `AGENT-MEMORY`（Ch77）、`MULTIMODAL-WORLD-MODELS`（Ch25）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已复核 Ch25、Ch66、Ch76～78与Ch81～83的environment authority、memory boundary、coordination tax与workflow ownership。
- **Existing Coverage:** Ch82已有single-agent baseline、communication tax、central/decentralized拓扑；SRMT提供implicit latent broadcast与central-planner coexistence的受限MAPF案例。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把gridworld throughput外推到LLM Agent，不修改Books。
- **Open Questions:** shared latent如何做permission/poisoning isolation；agent dropout和async step怎样恢复；communication bytes/critical path多大；何时切换central planner或hybrid。

### Fast3R

- **Candidate / Week / Score:** Fast3R / 2025-W04 / 23/30。
- **Source Family ID:** `fast3r-many-view-pointmap-reconstruction`。
- **Source Type:** arXiv paper + official project artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04固定v1机制、训练与系统profile。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13928v1；https://arxiv.org/abs/2501.13928；https://fast3r-3d.github.io/。
- **Related Primary Sources:** DUSt3R、MASt3R、Spann3R、COLMAP/SfM与作者code artifact用于representation和baseline contract。
- **Access and Verification Status:** Full Source Review Complete；pointmap objective、all-to-all architecture、position interpolation、parallel implementation、training/profile、pose/reconstruction、ablation与appendix已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、problem/loss、encoder/fusion/local-global heads、view-index masking、memory-efficient implementation、training data/details、A100 profile、pose/3D/4D evaluation、view/model/data scaling、local-head ablation与postprocess appendices。
- **Original Problem:** SfM/DUSt3R把N views降成pairwise matching与global alignment，产生O(N²) work、scene-specific optimization和累积误差，且每次只利用局部上下文。
- **Why the Previous Design Was Reasonable:** 几何pipeline有显式camera model、可解释constraint和高精度上限；pairwise learned pointmap降低端到端训练难度；incremental memory避免一次容纳所有views。
- **Changed Constraint:** 扫描/重建需要数十到上千unordered views，GPU与Transformer并行能力使joint representation可能比pairwise materialization+alignment更可扩展。
- **Mechanism:** 每图CroCo ViT编码patch；带image-index position的所有patch进入12-layer all-to-all fusion transformer；DPT heads同时预测local/global pointmaps及confidence。训练从1000 index pool随机选20 views，使未见view slots具有插值/掩码训练信号。
- **State Ownership:** first image defines global coordinate frame；each view owns local frame；model outputs pointmaps/confidence而非authoritative geometry；optional ICP/Gaussian splat/bundle adjustment owns postprocess state。
- **Control Flow / Data Flow:** unordered RGB views→per-view patches→index identity→joint fusion→local/global pointmaps+confidence→optional local-to-global ICP / reconstruction artifact→pose/geometry evaluation。
- **Implementation Details:** encoder ViT-B；fusion 12 layers/12 heads/dim768/MLP4；pool N'=1000；512² training、N=20、batch64、6.5K steps、64 A100约6.13天；FlashAttention与view/model parallel用于扩展。
- **Evaluation Setup:** CO3Dv2 pose；7-Scenes、Neural RGB-D、DTU reconstruction；single-A100 time/memory从2到1500 views、每view 512×384；训练数据约2000 scans与1300 videos/50 classes。
- **Baselines / Ablations / Sensitivity:** COLMAP/PixSfM/pose methods、DUSt3R/MASt3R/Spann3R；view-count scaling、position interpolation、local head、model/data scale；缺camera-order/reference choice、dynamic scenes、noise/calibration、multi-GPU与precision sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 64×A100 training；single A100 profile；512×384 views与view-count/time/peak GiB公开；training precision、A100 memory variant、serving concurrency与real-time SLO未完整披露。
- **What the Evidence Actually Proves:** 在作者datasets和hardware中，joint many-view pointmap regression避免显式O(N²) pair materialization/global alignment，并可处理远多于训练N的view slots；quality与额外views相关。
- **What It Does Not Prove:** 不证明单forward无postprocess、不证明全局attention真正线性扩展、不证明输出满足物理/metric geometry或动态场景，不证明取代SfM/SLAM在安全关键应用中的可解释约束。
- **Limitations / Threats to Validity:** global attention仍随总patch token平方增长；global frame依赖first image；训练范围有限；local detail需ICP对齐；作者没有系统量化坏views、calibration、motion或distributed failure。
- **Trade-offs / New Failure Modes:** joint fusion移除pairwise alignment barrier，却把所有views放进共享attention/memory；learned implicit alignment减少手工阶段，却失去显式constraint diagnostics；bad/reference view可污染全局输出。
- **Where the Previous Design Still Applies:** SfM/BA适合需要几何invariant和可修正约束；pairwise/incremental适合streaming、内存受限或在线SLAM；hybrid postprocess适合高精度交付。
- **Evolution Relationship:** `Alternative Branch`：explicit SfM pipeline→pairwise learned pointmaps+global alignment→joint many-view pointmaps；后者不是对几何/增量路线的通用替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MULTIMODAL-WORLD-MODELS`（Ch25）与 `INFER-TENSORRT-LLM`（Ch49）。
- **Target and Adjacent Chapters Read:** 已复核 Ch22～25与Ch48～50的representation/coordinate identity、world-state authority、attention scaling和execution contract。
- **Existing Coverage:** Ch23已有coordinate/artifact identity与fusion contract；Fast3R提供unordered many-view identity、global reference和joint-state fusion的3D实例。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；作者FPS/time绑定view count、resolution、single A100和postprocess边界，不修改Books。
- **Open Questions:** reference image失效如何恢复；global attention怎样分层/稀疏化；confidence如何校准并驱动postprocess；streaming incremental与joint correction如何共存。

### Video-MMMU

- **Candidate / Week / Score:** Video-MMMU / 2025-W04 / 23/30。
- **Source Family ID:** `video-mmmu-knowledge-acquisition-evaluation`。
- **Source Type:** arXiv benchmark paper + project/dataset artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04固定v1 dataset与evaluation contract。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13826v1；https://arxiv.org/abs/2501.13826；https://videommmu.github.io/。
- **Related Primary Sources:** MMMU/MMMU-Pro、Video-MME、LMMs-Eval及被测model cards用于benchmark lineage和runner contract。
- **Access and Verification Status:** Full Source Review Complete；dataset/annotation、Perception-Comprehension-Adaptation taxonomy、model/human setup、transcript study、knowledge delta、error analysis与appendices已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、30 subjects/6 disciplines、video selection、10-option QA、expert/o1 QA、models/input/evaluator、track/discipline results、audio transcript、pre/post adaptation protocol、wrong/right transitions、100-case errors、prompts与annotation appendix。
- **Original Problem:** 常见video QA测“模型是否答对视频问题”，无法区分读取信息、理解概念与把新知识迁移到新题；也无法知道video输入是帮助还是破坏原有正确判断。
- **Why the Previous Design Was Reasonable:** 单次video QA易标准化；accuracy清晰；字幕可降低speech/OCR障碍；静态pretrained knowledge benchmark避免before/after配对复杂性。
- **Changed Constraint:** 若目标是knowledge acquisition，必须测同一能力在看视频前后如何变化，并同时计入Wrong-to-Right收益与Right-to-Wrong遗忘/干扰。
- **Mechanism:** 每个教育视频构造Perception、Comprehension、Adaptation三阶段MCQ；Adaptation先无video答，再看video重答；以transition统计定义knowledge change，而非只看post-video accuracy。
- **State Ownership:** dataset owns video/question/answer/discipline/cognitive-stage identity；runner owns frames/transcript/prompt；model response是observation；rule extractor ownsparse result；benchmark不拥有模型内部“learned knowledge”。
- **Control Flow / Data Flow:** professional video→expert multi-stage QA→model pre-video Adaptation answer→video/transcript input→Perception/Comprehension/Adaptation answers→regex extraction→accuracy + W2R/R2W/knowledge delta→error audit。
- **Implementation Details:** 30 subjects、6 disciplines；concept-introduction与problem-solving videos；每题10 options；annotations经cross-check、o1 language/correctness辅助与domain expert review；LMMs-Eval rule pipeline解析option/number。
- **Evaluation Setup:** 多个proprietary/open LMMs与human senior-undergraduate baseline；平均video 506.2s、75.7 questions/benchmark统计；按tracks、disciplines、audio transcript与adaptation transitions报告micro accuracy。
- **Baselines / Ablations / Sensitivity:** random/human、多模型、with/without audio transcript、before/after video、discipline slices与100-case error taxonomy；缺frame sampling/token budget、prompt order、contamination、judge/extractor sensitivity和variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model snapshots公开到论文级；video duration公开；frame count、resolution、context tokens、hardware、batch/concurrency、cost与SLO未统一披露。
- **What the Evidence Actually Proves:** 在该dataset/protocol中，post-video accuracy可掩盖R2W退化；audio transcript对理解有帮助但在作者Adaptation结果中并非单向增益；error包含method selection、calculation、misread和extraction等不同planes。
- **What It Does Not Prove:** 不证明模型永久学习或更新参数，不证明knowledge delta等于一般学习能力，不证明模型差距可跨frame policy/snapshot外推，也不证明human baseline代表专家上限。
- **Limitations / Threats to Validity:** MCQ/10 options与regex有格式偏差；video、course和model pretraining contamination未知；Adaptation题构造与原知识匹配依赖annotator；部分4% annotation/5% extraction error被确认。
- **Trade-offs / New Failure Modes:** pre/post protocol提高因果可读性却增加题目配对与contamination控制；字幕增加可访问性也可能引入distractor；聚合delta若不保留W2R/R2W会再次丢失方向信息。
- **Where the Previous Design Still Applies:** 单次video QA适合perception/comprehension smoke test；open-ended评估适合真实生成能力；human/executable grading适合无法用MCQ代表的专业任务。
- **Evolution Relationship:** `Direct Evolution`：post-video accuracy→cognitive-stage slices→pre/post transition evidence；不是把benchmark score写成模型“获得知识”的事实。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `TRAIN-DATA`（Ch27）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23、Ch27与Ch65～67的input identity、dataset lineage、transition metric、error attribution和evidence boundary。
- **Existing Coverage:** Ch66已有evaluation subject、slice与state transition证据；Video-MMMU提供W2R/R2W不能被净分数替代的multimodal案例。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不把作者模型排行或human gap外推，不修改Books。
- **Open Questions:** frame/transcript预算怎样改变delta；如何检测training contamination；open-ended adaptation如何验证；model snapshot和API drift如何复现。

### Debate Helps Weak-to-Strong Generalization

- **Candidate / Week / Score:** Debate Helps Weak-to-Strong Generalization / 2025-W04 / 22/30。
- **Source Family ID:** `debate-ensemble-weak-to-strong-supervision`。
- **Source Type:** arXiv paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；此前census写成01-22，已按submission metadata纠正且仍属W04。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13124v1；https://arxiv.org/abs/2501.13124。
- **Related Primary Sources:** OpenAI weak-to-strong benchmark、debate/consultancy/market-making、Qwen model report与reward-ensemble work用于protocol lineage。
- **Access and Verification Status:** Full Source Review Complete；W2SG setup、debate generation、weak ensemble、student training、four tasks、PGR、alternative oversight、ensemble/turn ablations与limitations已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、debate prompts/protocol、strong-to-weak transcript distillation、ensemble construction、weak labels/strong student、SciQ/BoolQ/CosmosQA/AnthropicHH、aux/pro confidence losses、consultancy/market-making、seed/cardinality/turn ablations与limitations。
- **Original Problem:** 若supervisor比student弱，直接weak labels不能可靠监督strong capability；scalable oversight可以从strong model提取信息，但judge本身仍弱。
- **Why the Previous Design Was Reasonable:** 直接weak supervision成本低；ensemble降低单模型方差；consultancy只需一个strong call；human/weak judge在可理解任务上仍是明确authority。
- **Changed Constraint:** strong model可能包含weak supervisor欠缺的知识但不可信；让两个strong instances为相反答案辩论，可把可检查arguments作为context交给多个weak models，而非要求weak judge独立发现答案。
- **Mechanism:** binary question的正确/错误answer随机分配给两debater，三轮互相反驳；transcript增强训练数据；多个weak models在不同debate seeds上训练并ensemble出supervision labels，再训练strong student。
- **State Ownership:** debate runner ownsanswer assignment/turns/transcript/seed；weak ensemble ownsprovisional label distribution；ground truth仅用于实验；student trainer ownsdataset/checkpoint；weak label不是truth authority。
- **Control Flow / Data Flow:** task+answer pair→strong-model debate transcripts→seed-diverse weak-model fine-tuning→ensemble prediction/labels→strong-student training→ground-truth test/PGR evaluation。
- **Implementation Details:** tasks转成balanced binary classification；debate transcript附入prompt；默认三轮；比较standard/probability/auxiliary objectives。具体model sizes接近而非superhuman gap。
- **Evaluation Setup:** SciQ、BoolQ、CosmosQA、AnthropicHH；报告accuracy与performance gap recovered，相对ground-truth weak/strong ceilings。
- **Baselines / Ablations / Sensitivity:** plain finetune、confidence aux/pro losses、consultancy、market-making、single weak、ordinary/debate ensemble、ensemble cardinality、shared/different seed与1～6 debate turns。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model families和turn count披露；hardware、precision、batch、transcript tokens、inference/training cost、concurrency与SLO未完整披露。
- **What the Evidence Actually Proves:** 在四个作者binary NLP设置和有限weak/strong gap中，seed-diverse debate transcript ensemble比被测alternatives提高PGR；超过三轮未继续增益且可下降。
- **What It Does Not Prove:** 不证明debate从真正superhuman/deceptive model提取truth，不证明arguments faithful或ensemble independent，不证明PGR代表安全alignment，也不证明开放问题/工具环境有效。
- **Limitations / Threats to Validity:** binary tasks、已知candidate answers与近尺度models简化问题；ground truth用于研究评估；同一model family错误相关；cost、adversarial collusion和judge manipulation未充分测试。
- **Trade-offs / New Failure Modes:** debate增加evidence diversity，也倍增calls、transcript与coordination；ensemble降variance却可能形成correlated consensus；长辩论带来context overload、instruction drift和persuasive falsehood。
- **Where the Previous Design Still Applies:** direct supervision适合supervisor足够强；consultancy适合成本受限；task decomposition/executable verifier适合可拆解任务；单weak model适合低风险/高可验证场景。
- **Evolution Relationship:** `Alternative Branch`：fixed weak labels→strong-model argument extraction→seed-diverse weak ensemble→strong-student supervision；不是debate自动产生truth。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `TRAIN-RLHF`（Ch31）与 `AGENT-MULTI-AGENT`（Ch82）。
- **Target and Adjacent Chapters Read:** 已复核 Ch31、Ch65～67与Ch81～83的weak judge、ensemble evidence、coordination tax和decision authority。
- **Existing Coverage:** Ch66已有judge≠truth与rater disagreement，Ch82已有debate topology和correlated error；论文提供weak-supervisor training pipeline的受限证据。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；纠正v1日期，不把PGR写成superhuman alignment证明，不修改Books。
- **Open Questions:** deceptive/colluding debaters下怎样验证；weak ensemble如何估计相关性；argument provenance如何保存；何时停止debate或切换deterministic evidence。

### Imagine-E

- **Candidate / Week / Score:** Imagine-E / 2025-W04 / 22/30。
- **Source Family ID:** `imagine-e-t2i-capability-evaluation`。
- **Source Type:** arXiv benchmark/report。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04固定v1 prompts、models与scoring观察。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13920v1；https://arxiv.org/abs/2501.13920。
- **Related Primary Sources:** CLIPScore、HPSv2、Aesthetic Score、GPT-4o judge与六个被测model官方facts用于scorer/model identity。
- **Access and Verification Status:** Full Source Review Complete；六类capability taxonomy、全部subtasks/samples、四类scorer/human tables、model comparison、complexity与conclusion已核验。
- **Full-read Coverage:** metadata、motivation、structured output、realism/physical consistency、domain tasks、challenging scenarios、multi-style、36 scoring tables、qualitative cases、task complexity、metric-human disagreement与conclusion。
- **Original Problem:** 常用T2I指标和简单prompts无法区分结构化输出、文字/OCR、物理一致性、domain diagram、异常场景和style等不同能力，单总分会掩盖failure taxonomy。
- **Why the Previous Design Was Reasonable:** CLIPScore/HPS/Aesthetic可自动大规模比较；单prompt suite成本低；human rating更贴近直觉；model leaderboard便于沟通。
- **Changed Constraint:** T2I开始承担table/chart/equation/UI/code、science/robotics/autonomous-driving、multilingual/OCR和multi-image等异构任务，输出是否“好看”不再等于任务正确。
- **Mechanism:** 构造六大类、多subtask prompt suite；六个models生成样本；同时用CLIPScore、HPSv2、Aesthetic、GPT-4o与human评分比较，保留每task结果和metric disagreement而非只给一个rank。
- **State Ownership:** prompt suite ownsintent/task/rubric；model/version ownsoutput；automatic/judge/human scorer each ownsconditional measurement；benchmark没有production release authority。
- **Control Flow / Data Flow:** taxonomy→prompt instances→six model generation→per-task qualitative inspection→four automated/judge metrics+human score→slice comparison/disagreement→capability/failure report。
- **Implementation Details:** models为FLUX.1、Ideogram2.0、DALL-E3、Midjourney、SD3与Jimeng；tasks覆盖structured、realistic/physical、specific domain、challenging、multi-style等；论文大量保留图例和per-task tables。
- **Evaluation Setup:** 每task对六model输出评分；CLIP/HPS/Aesthetic、GPT-4o和human并列；没有统一披露所有API snapshot、seed、image size、sample count/annotator协议与置信区间。
- **Baselines / Ablations / Sensitivity:** 跨model与跨scorer对比、多task difficulty；并非训练论文，无机制ablation；缺prompt paraphrase、seed、model version drift、rater count/agreement和statistical uncertainty。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model names公开；closed model版本、sampler/seed/steps、resolution、hardware、latency/cost、concurrency与SLO大多未统一披露。
- **What the Evidence Actually Proves:** 在作者selected prompts/outputs中，不同scorer与human经常不一致；T2I failure必须按task/rubric切片；视觉质量和结构/文字/物理正确性不可互换。
- **What It Does Not Prove:** 不证明任一model总体最好，不证明GPT-4o等价human，不证明selected qualitative samples可估计population performance，也不证明domain image可用于科学/安全决策。
- **Limitations / Threats to Validity:** prompt和sample selection可能主观；closed model漂移不可复算；human protocol与uncertainty披露不足；多数“intelligence”结论来自output inspection而非executable validation。
- **Trade-offs / New Failure Modes:** 广taxonomy提高coverage但降低每slice样本/统计力；多scorer暴露分歧却需要决策policy；LLM judge更语义化也会带来版本、bias与自相关。
- **Where the Previous Design Still Applies:** automated embedding/aesthetic metrics适合大规模初筛；human review适合审美/开放目标；domain-specific executable checks应取代通用judge作为高风险正确性证据。
- **Evolution Relationship:** `Direct Evolution`：single aesthetic/alignment score→capability taxonomy+slices→scorer disagreement evidence；不是创建一个更大的leaderboard。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `PLATFORM-OBSERVABILITY`（Ch65）。
- **Target and Adjacent Chapters Read:** 已复核 Ch23～25与Ch65～67的output contract、failure taxonomy、judge/human disagreement和uncertainty。
- **Existing Coverage:** Ch66已有claim contract、slice、judge/human边界；Imagine-E提供T2I异构任务下metric disagreement的广覆盖但低统计强度案例。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；不复制model排行榜，不修改Books。
- **Open Questions:** 如何公开prompt/output/version；每slice需要多少样本；结构/文字任务如何引入OCR/parser/executable scorer；human与judge分歧如何进入release policy。

### Triton 3.2.0

- **Candidate / Week / Score:** Triton 3.2.0 / 2025-W04 / 22/30。
- **Source Family ID:** `triton-3.2-release-snapshot`。
- **Source Type:** official GitHub release/tag + release PR/process documentation。
- **First-public Date / Revision History:** release branch cut 2024-10；PyPI/tag release 2025-01-22；无3.2.1 patch release。
- **Direct Primary Sources:** https://github.com/triton-lang/triton/releases/tag/v3.2.0；https://github.com/triton-lang/triton/pull/5618；https://github.com/triton-lang/triton/blob/main/RELEASE.md。
- **Related Primary Sources:** `release/3.2.x` branch、verified tag commit `9641643`、PyTorch/vLLM downstream test policy；普通社区Windows build不作证据。
- **Access and Verification Status:** Full Source Review Complete as release fact；tag、date、promotion PR、compatibility与release process已核验；独立3.2 feature changelog未公开，机制明确标记Not Disclosed。
- **Full-read Coverage:** release page/tag、PR conversation/commits、release history/compatibility matrix、branch/test/promotion流程、cherry-pick criteria与current branch identity；未用后续版本feature list反推3.2。
- **Original Problem:** compiler/runtime消费者需要可安装、可锁定且被downstream验证的稳定snapshot，而main branch持续变化不能直接充当production artifact。
- **Why the Previous Design Was Reasonable:** commit pin可精确复现；nightly尽早暴露兼容性；source build允许自定义backend；旧版3.1保持已验证环境不动。
- **Changed Constraint:** release/3.2.x已通过Triton、PyTorch与vLLM nightly/downstream流程，需要受控promotion到PyPI并冻结Python/manylinux compatibility。
- **Mechanism:** 这次可核实的变化是release pipeline事实：在release branch启用PyPI promotion、merge到verified commit并打v3.2.0 tag；不是公开的compiler feature proposal或kernel mechanism。
- **State Ownership:** repository branch/tag owns source snapshot；CI/promotion workflow ownswheel publication；PyPI ownsdistributed artifact；consumer lockfile/container ownsdeployment version；model/runtime benchmark由下游owns。
- **Control Flow / Data Flow:** branch cut→periodic main sync/cherry-pick→Triton+PyTorch+vLLM nightly tests→select validated commit→enable promotion→signed tag/PyPI wheels→consumer pin→downstream validation/rollback。
- **Implementation Details:** v3.2.0支持CPython 3.9～3.13、manylinux glibc2.17+ x86-64；PR #5618仅改release promotion path并讨论tag-trigger/security fragility；没有可靠release-note feature ledger。
- **Evaluation Setup:** 官方流程声明Triton test suite及PyTorch/vLLM nightly branches参与验证；具体test matrix、hardware、pass rates、performance regression thresholds未在release page披露。
- **Baselines / Ablations / Sensitivity:** version pin/nightly/source-build是替代运维分支；没有论文式baseline或ablation；未把3.1→3.2 commit diff自动解释成稳定feature清单。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Disclosed；release compatibility只覆盖Python/manylinux，不构成GPU/model/precision/kernel performance或SLO声明。
- **What the Evidence Actually Proves:** 2025-01-22存在官方signed v3.2.0 snapshot与PyPI promotion；官方当前release history确认日期、compatibility和downstream validation流程。
- **What It Does Not Prove:** 不证明任何kernel更快/更正确，不证明某项compiler pass在3.2首次可用，不证明对特定GPU/model生产兼容，也不证明PR流程无供应链风险。
- **Limitations / Threats to Validity:** release页面没有feature notes；当前RELEASE.md是后续制度文档，能核验历史表与流程但不等于2025当日全部流程；branch diff过大且不应替代curated mechanism evidence。
- **Trade-offs / New Failure Modes:** binary snapshot降低源码漂移，却增加wheel/ABI/backend兼容与supply-chain ownership；promotion automation降低手工成本，tag/secret保护错误可能误发布；升级可获得fix也会引入regression。
- **Where the Previous Design Still Applies:** pin 3.1适合已验证栈；nightly适合提前兼容；source build适合自定义backend；production应在model/kernel/workload上重测而非相信版本号。
- **Evolution Relationship:** `Layering / Dependency`：compiler source→validated release snapshot→downstream runtime adoption；本事件不构成compiler mechanism演进。
- **ROADMAP Node:** `INFER-TENSORRT-LLM`（Ch49，通用execution-plan/kernel owner）主 owner；handoff `PLATFORM-ARTIFACT-MANAGEMENT`（Ch59）与 `PLATFORM-MODEL-SERVING`（Ch62）。
- **Target and Adjacent Chapters Read:** 已复核 Ch48～50、Ch58～60与Ch61～63的compiler plan、artifact identity、compatibility validation和deployment rollback。
- **Existing Coverage:** Ch49已有Triton/kernel DSL机制，Ch59已有artifact immutability；3.2.0只增加versioned release案例，不提供值得沉淀的新机制。
- **Integration Decision:** `Weekly Only — Version Fact / Mechanism Not Disclosed`；Books Integration Deferred且未来也不应仅凭tag修改正文。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；因无独立feature ledger，不把release写成性能或compiler机制更新。
- **Open Questions:** 事件时commit对应的完整test matrix是否可取得；wheel provenance/SBOM如何验证；下游如何做kernel correctness/performance canary和rollback。

### Hallucinations in Drug Discovery

- **Candidate / Week / Score:** Hallucinations in Drug Discovery / 2025-W04 / 20/30。
- **Source Family ID:** `llm-hallucinated-molecule-description-classification`。
- **Source Type:** arXiv experimental paper。
- **First-public Date / Revision History:** arXiv v1 2025-01-23；W04固定v1实验结论。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13824v1；https://arxiv.org/abs/2501.13824。
- **Related Primary Sources:** MolT5、SMILES、HIV/BBBP/Clintox/SIDER/Tox21 datasets、HHM hallucination scorer与被测model artifacts用于实验contract。
- **Access and Verification Status:** Full Source Review Complete；prompt design、classification formulation、seven models/five datasets、baselines、cross-generator results、size/temperature/language analyses、attention case与appendices已核验。
- **Full-read Coverage:** metadata、Introduction/Related Work、SMILES→description generation、binary next-token classification、SMILES/MolT5/LLM-description conditions、models/datasets/ROC-AUC、cross-source/size/temperature/language analyses、attention case、prompts和full tables。
- **Original Problem:** LLM难直接解析SMILES；domain translator生成faithful description可能丢失信息，而general LLM会产生不faithful但与分子模式相关的文字。问题是这些派生文本能否作为feature expansion改善分类。
- **Why the Previous Design Was Reasonable:** 直接SMILES保留原始结构；MolT5 description追求faithfulness；domain model与molecular graph methods避免自然语言幻觉；严格拒绝hallucination对科学结论安全合理。
- **Changed Constraint:** classification evaluator只看标签ROC-AUC，派生文字即使不faithful也可能激活模型已有chemical associations；这允许把它当stochastic feature proposal而非事实。
- **Mechanism:** 同一SMILES由不同LLM生成≤256-token description；再将SMILES+description+task instruction输入目标LLM，以Yes/No token概率做property classification；比较空description、MolT5和交叉LLM-generated conditions。
- **State Ownership:** SMILES与dataset label是实验authoritative input；generated description是untrusted derived feature；classifier probability不是scientific claim；任何drug hypothesis需要independent domain/executable validation。
- **Control Flow / Data Flow:** molecule SMILES→generator LLM description→hallucination score→target LLM prompt→Yes/No probabilities→ROC-AUC→cross-generator/temperature/language analysis；无wet-lab或molecular docking验证。
- **Implementation Details:** 七models含Llama-3/3.1、Ministral、Falcon3-Mamba、ChemLLM、GPT-3.5、GPT-4o；默认temperature0.6、max new tokens256；five datasets各选binary property/label。
- **Evaluation Setup:** HIV 4113、BBBP205、Clintox148、SIDER143、Tox21 783 test samples（表中counts）；ROC-AUC；SMILES-only与MolT5 description baselines；跨generator/model平均比较。
- **Baselines / Ablations / Sensitivity:** model size、temperature、language、description source、hallucination score与single attention case；缺prompt paraphrase/seed、class imbalance uncertainty、molecular scaffold split、classical/graph baselines和prospective validation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model names、temperature与256 output cap公开；API snapshots、hardware、precision、batch/concurrency、prompt tokens、cost与SLO未披露。
- **What the Evidence Actually Proves:** 在作者五个small classification test sets与prompt setup中，某些不faithfulLLM descriptions与更高ROC-AUC相关，且source model影响结果；temperature改变hallucination score但未呈简单performance关系。
- **What It Does Not Prove:** 不证明hallucination包含正确chemistry、不证明发现新drug、不证明因果机制、不证明模型可取代molecular representation/assay，也不证明18.35是绝对百分点之外的通用收益。
- **Limitations / Threats to Validity:** 数据集小且class imbalance明显；无scaffold/time split披露；多模型/API可漂移；自然语言可能泄露dataset priors；attention不是causal explanation；无实验室或external replication。
- **Trade-offs / New Failure Modes:** stochastic feature expansion可能提高proxy score，却产生不可解释、不可复算、prompt-injection与虚假scientific narrative风险；若把derived text误当事实，收益会变成安全债务。
- **Where the Previous Design Still Applies:** faithful domain translation、graph/SMILES model与retrieval适合科学解释；direct SMILES保留原始证据；高风险drug discovery必须使用domain verifier、simulation/assay和human review。
- **Evolution Relationship:** `Explanatory Analogy`：raw structured input→faithful textual projection→untrusted stochastic feature proposal→independent validation；不是“应保留hallucination”的通用技术演进。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `TRAIN-DATA`（Ch27）、`AGENT-REFLECTION`（Ch80）与 `PLATFORM-SECURITY`（Ch71）。
- **Target and Adjacent Chapters Read:** 已复核 Ch27、Ch65～67、Ch70～72与Ch79～81的derived data provenance、proxy metric、domain validation和untrusted content边界。
- **Existing Coverage:** Ch66已有proxy不等于truth与executable/domain evaluation；该论文是“有用但不真实feature”必须隔离evidence authority的反例型案例。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，但极可能保持受限案例而非核心机制。
- **Changed Files or Rejection Reason:** 仅更新 W04 Weekly；标题中的drug discovery不外推到discovery outcome，不修改Books。
- **Open Questions:** scaffold split下是否仍成立；描述是否只是label prior；怎样对derived text做taint tracking；何种domain verifier能证明它不是虚假相关。

### Qwen2.5-1M

- **Candidate / Week / Score:** Qwen2.5-1M / 2025-W04 / 29/30。
- **Source Family ID:** `qwen2-5-1m-training-extrapolation-sparse-runtime`。
- **Source Type:** 作者 technical report、官方 release、open-weight model card 与公开 inference fork/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-26；v2 2025-03-05。旧 Qwen Blog 显示 1月27日、
  新站显示1月26日，归档以可核验的 arXiv v1 为准；Hugging Face 1月28日仅是 discovery date。
- **Direct Primary Sources:** https://arxiv.org/html/2501.15383v1；https://arxiv.org/abs/2501.15383；
  https://qwen.ai/blog?id=qwen2.5-1m；https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M。
- **Related Primary Sources:** DCA、YaRN、MInference 与 vLLM 是 family dependencies；各自原始论文/代码
  只解释依赖机制，不把其独立 benchmark 合并为 Qwen2.5-1M 结果。
- **Access and Verification Status:** Full Source Review Complete；v1 全文、公式、training stages、inference
  architecture、evaluation contract 与 model card 可访问。BladeLLM 完整源码、训练集群、线上并发/SLO 未公开。
- **Full-read Coverage:** 已读 metadata、Introduction/Architecture、natural+synthetic data、five-stage pretraining、
  long-instruction synthesis、two-stage SFT/offline RL、DCA+YaRN、MInference/chunked prefill/sparsity refinement、
  sparse/MoE kernels、DCPP、TAG scheduling、long/short evaluation、speed setup、conclusion 与 artifact notes。
- **Original Problem:** 1M context 同时暴露四个不同瓶颈：模型未见过远距离位置、natural data 的长依赖弱、
  dense Prefill 计算/activation超限，以及串行 scheduler/model-runner/decoder 与固定 PP chunks 形成 bubbles。
- **Why the Previous Design Was Reasonable:** 4K/32K训练便宜且数据密度高；dense attention语义精确、规则且易验证；
  固定 chunk PP 简单；同步 scheduler 等待真实 token 后再分配 KV，correctness直观。短输入/低并发时这些仍合理。
- **Changed Constraint:** context 从128K推进到1M后，位置外推、effective utilization、activation、Attention FLOPs、
  pipeline imbalance 与 CPU orchestration 必须联合解决，单独增加 `max_position_embeddings` 不够。
- **Mechanism:** training 从4K→32K→65K→131K→262K progressive extension，并调整 RoPE base、混入 synthetic
  FIM/retrieval/reordering与长短样本；两阶段 SFT 保留短任务，短样本 offline RL 对齐。Inference 用 DCA remap
  + YaRN scaling 外推至1M，MInference vertical/slash sparse selection 与 chunked prefill/refinement降成本；BladeLLM
  以跨硬件 sparse/MoE kernels、按 attention cost 动态 chunk 的 DCPP 和 Scheduler/Runner/Decoder 三进程 TAG 执行。
- **State Ownership:** training pipeline 拥有 data/length/RoPE stage；model artifact 拥有 256K-trained capability；
  DCA/sparsity profile 属 runtime compatibility state；scheduler 拥有 request/KV reservation，runner 拥有 model-step，
  decoder 拥有 token→text stream。预测性 KV allocation 需要 token/result reconciliation。
- **Control Flow / Data Flow:** long documents→synthetic dependency tasks→progressive pretrain→short then mixed-long SFT→
  short preference RL→versioned model；serving request→DCA/YaRN positions→chunk-wise sparse candidate selection→DCPP
  prefill→KV state→TAG scheduler anticipates next token allocation→runner→decoder/API。
- **Implementation Details:** open models 7B/14B GQA，trained to262K、serve to1M；MInference 用 per-head offline
  sparsity config、last-query selection、chunk内最后64 tokens与1M refinement；DCPP按历史 KV 导致的 attention cost
  调整 chunk size；TAG用shared memory queues分离三进程。具体 BladeLLM实现并未完整开源。
- **Evaluation Setup:** long tasks含 Passkey、RULER（≤128K）、LV-Eval（≤256K）、LongBench-Chat（≤100K），
  另测short benchmarks；TTFT speed在A100/H20、1M contexts、batch1，7B TP4、14B/Turbo TP8，对比full attention。
- **Baselines / Ablations / Sensitivity:** progressive length stages、DCA on/off、sparse refinement与full attention、128K
  counterparts、short/long post-training对比；多项 engine optimization以组合方案呈现，TAG/DCPP缺独立端到端ablation，
  vendor API baseline与open model运行条件也不完全同构。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TTFT实验披露A100/H20、7B/14B/Turbo、
  1M input、TP4/TP8、batch1；precision未在speed段明确，concurrency>1、output length、TPOT、tail SLO与network
  topology未完整披露。3.2～6.7×只能绑定该作者contract。
- **What the Evidence Actually Proves:** 在作者模型与实验中，long-context capability需要training distribution、
  position policy与runtime共同演化；chunked sparse Prefill、cost-aware PP chunks和异步CPU stages在披露条件下可行。
- **What It Does Not Prove:** 不证明accepted 1M等于普遍effective utilization，不证明DCA/MInference对所有模型
  无损，不证明batch1 TTFT speedup转化为多租户goodput，也不证明预测性allocation没有rollback/recovery代价。
- **Limitations / Threats to Validity:** 厂商自评、部分synthetic/private data、BladeLLM闭源边界、长任务长度上限
  多低于1M、component ablation不完整；sparse pattern从短序列校准会drift，DCA discontinuity本身可破坏selector。
- **Trade-offs / New Failure Modes:** progressive training降低直接1M训练成本却增加stage/checkpoint lineage与短能力
  遗忘风险；DCA扩长却改变相对位置；sparse selection节省work却可能漏evidence；chunking降activation/干扰却增加
  scheduling metadata；TAG减少CPU串行等待却引入anticipated-token、queue lag、cancellation与reconciliation failure。
- **Where the Previous Design Still Applies:** dense full attention适合短context/strict exactness；训练长度内原生RoPE
  更简单；固定 chunks适合cost均匀；同步scheduler适合低并发/易恢复；RAG适合证据可检索且不需把全部原文放进window。
- **Evolution Relationship:** `Direct Evolution`：short training→progressive long training→training-free extrapolation→
  sparse/chunked Prefill→cost-aware pipeline与async runtime；每层解决不同约束，并非后者替代前者。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Ch22）主 owner；handoff `INFER-PREFILL`（Ch43）、
  `INFER-TENSORRT-LLM`（Ch49，execution owner）与 `INFER-SCHEDULING`（Ch56）。
- **Target and Adjacent Chapters Read:** 已读 Ch22、Ch43～45、Ch49 与 Ch56；核对 accepted/effective/system length、
  chunked Prefill state commit、KV identity、execution plan 与 scheduling/admission 边界。
- **Existing Coverage:** 这些章节已有长上下文联合约束、sparse selection cost、chunked Prefill与async scheduling主线；
  本 family 是否补充 DCPP/TAG 的演进证据留待后续 Books Gate，本阶段不修改或预先宣称吸收。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate 关闭。
- **Changed Files or Rejection Reason:** 仅回拨更新 W04 Weekly 与年度索引；不修改 Books，不保留脱离contract的倍率。
- **Open Questions:** TAG predicted KV allocation怎样处理 rejected speculative tokens/cancellation；DCPP cost model如何校准；
  sparse profile如何按domain/length/version invalidation；1M下多租户TTFT/TPOT、failure recovery与prefix reuse如何组合。

### Qwen2.5-VL

- **Candidate / Week / Score:** Qwen2.5-VL / 2025-W04 / 27/30。
- **Source Family ID:** `qwen2-5-vl-native-resolution-time-alignment`；release 与后续 technical report 联读。
- **Source Type:** 官方模型发布、作者 technical report、model card 与开源 artifact。
- **First-public Date / Revision History:** 官方 release 2025-01-26；technical report v1 2025-02-19。事件归 W04，
  后续报告只补强同 family 机制证据，不在 W08 重复计分。
- **Direct Primary Sources:** https://qwenlm.github.io/blog/qwen2.5-vl/；
  https://arxiv.org/html/2502.13923v1；https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct。
- **Related Primary Sources:** Qwen2-VL 与 Qwen2.5 LLM 报告仅用于前代 architecture/base-model contract；
  Transformers integration 只证明 artifact 可执行，不替代模型机制证据。
- **Access and Verification Status:** Full Source Review Complete；官方 release、report 全文、architecture、
  data/training recipe、evaluation tables 与 model card 可访问。独立复现、完整数据清单、训练集群与线上 SLO 未披露。
- **Full-read Coverage:** 已读 metadata、Introduction、vision encoder/native resolution、dynamic FPS、absolute-time
  MRoPE、pretraining data/three-stage recipe、SFT/DPO、filtering/rejection sampling、VQA/OCR/spatial/video/agent
  evaluation、model configurations、conclusion 与 artifact usage/limitations；报告无独立 Limitations 章节，按披露缺口记录。
- **Original Problem:** 固定分辨率和固定 frame sampling 会扭曲空间尺度、丢失真实时间间隔，并使图像/视频
  token 数与计算负载失配；通用 VLM 还需要同时服务文档、grounding、长视频和 GUI action。
- **Why the Previous Design Was Reasonable:** 固定 resize、normalized coordinates 与固定 FPS 产生规则 tensor
  shape，便于 batching 和训练；冻结视觉 encoder + projector 降低重训成本；短视频中相对 frame index 足够。
- **Changed Constraint:** 原生尺寸、不同长宽比、小时级视频与秒级定位要求 representation 保留实际空间尺度和
  时间速率，而 token length 变化又把 load balance、packing 与 Serving admission 变成系统问题。
- **Mechanism:** 以 Qwen2.5 LLM 初始化 decoder，从头训练 ViT；14×14 patch、相邻四 patch 经 MLP merger
  压缩；多数 vision layers 用 window attention，仅四层 full attention；图像 native dynamic resolution，视频
  dynamic FPS；MRoPE temporal ids 与 absolute time 对齐。三阶段 pretraining 从 vision alignment 逐步解冻并
  增加 long sequence/video/agent data，post-training 使用 SFT + DPO。
- **State Ownership:** vision preprocessor 拥有 resize、patch、FPS 与 timestamp mapping；ViT/merger 拥有 visual
  token representation；LLM 拥有 joint sequence state；model/card version 拥有 artifact identity；GUI/environment
  才拥有真实 action outcome，模型生成的 coordinates/actions 不是 authoritative environment state。
- **Control Flow / Data Flow:** image/video + sampling metadata→native-size resize/patching 或 dynamic-FPS frames→
  window/full ViT→four-patch merger→multimodal sequence + time-aligned MRoPE→Qwen decoder→text、coordinates、
  timestamps 或 action proposal；实际 tool execution 必须由外部 controller 验证和提交。
- **Implementation Details:** ViT hidden size 1280、32 layers、window 112×112，仅 layers 7/15/23/31 full attention；
  three sizes 3B/7B/72B，pretraining 4.1T tokens；前两阶段 pack 至 8192，第三阶段 32768。配置是该 family
  的公开实现事实，不外推为多模态模型通用最优值。
- **Evaluation Setup:** 作者在 general VQA、document/OCR、spatial grounding、video understanding/grounding、
  GUI/phone agent 与 pure-text benchmarks 上比较同规模和 frontier baselines；不同表的模型、prompt、resolution、
  evaluator 与 proprietary access 并不统一。
- **Baselines / Ablations / Sensitivity:** 与 Qwen2-VL、InternVL 等模型对比；报告给出 architecture/training recipe，
  但缺少 window attention、absolute-time MRoPE、dynamic FPS 与 data scale 的完整独立 ablation，也缺 production
  latency/throughput sensitivity，因此不能把全部收益归因于单一机制。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes、token counts 与 training pack
  lengths披露；训练硬件规模、precision、global batch、video decode cost、serving concurrency、TTFT/TPOT 与
  control-loop deadline未形成完整 contract。release 的“小时级视频”不是所有硬件/SLO 下的保证。
- **What the Evidence Actually Proves:** 该公开 family 确实把空间/时间采样信息推进 representation contract，
  并用 window attention 与 packing 处理 variable-length 计算；作者设置中支持多类 multimodal tasks。
- **What It Does Not Prove:** 不证明 native dynamic representation 普遍优于固定 encoder/projector，不证明视觉
  agent 输出可安全执行，不证明长视频全程有效利用，也不证明厂商 benchmark 可跨模型、硬件或 evaluator 外推。
- **Limitations / Threats to Validity:** 厂商自评、训练数据部分私有、component ablation 不完整、长视频 effective
  utilization 与 temporal calibration 证据有限；绝对坐标依赖 resize/preprocess identity，GUI 环境变化会破坏 action。
- **Trade-offs / New Failure Modes:** 保留真实尺度和时间减少 normalization distortion，却造成 variable token
  length、load imbalance、admission/cost不确定与 cache identity扩张；window attention降低视觉计算但限制局部层
  的全局交互；统一视觉 agent 增加 coordinate drift、stale screenshot、unsafe action 与 environment mismatch。
- **Where the Previous Design Still Applies:** 固定 resolution/FPS 适合规则 batch、窄域和严格 latency；冻结 encoder +
  projector 适合数据有限或独立升级视觉模块；外部 OCR/detector/controller 在可审计性与安全边界优先时仍合理。
- **Evolution Relationship:** `Direct Evolution`：fixed spatial/temporal sampling→native dynamic resolution→dynamic FPS
  + absolute-time position；`Layering / Dependency`：representation→grounding→agent proposal，不等于感知模型取代 controller。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MODEL-LONG-CONTEXT`（Ch22）、
  `MULTIMODAL-WORLD-MODELS`（Ch25）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch22～25，重点复核 Ch23 的 representation/time/provenance identity、
  Ch22 的 accepted/effective/system length 区分与 Ch25 的 observed state / action-authority boundary。
- **Existing Coverage:** Ch23 已有 dynamic representation、time/provenance 与 modality admission 主线；本 family
  为其提供完整机制证据，但是否 refine 正文属于后续 Books Gate，本阶段不预判修改。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate 关闭。
- **Changed Files or Rejection Reason:** 仅回拨更新 W04 Weekly 与年度索引；不修改 Books，不复制 capability/benchmark 清单。
- **Open Questions:** preprocess/FPS/coordinate identity 如何进入 cache key；long-video effective utilization 如何按
  event distance验证；variable visual tokens如何与batch/SLO联合调度；action proposal如何绑定fresh observation和权限。

### Humanity's Last Exam

- **Candidate / Week / Score:** Humanity's Last Exam / 2025-W04 / 27/30。
- **Source Family ID:** `hle-frontier-closed-ended-evaluation`。
- **Source Type:** arXiv v1、公开 dataset/project 与作者 evaluation protocol。
- **First-public Date / Revision History:** v1 2025-01-24；后续题集和模型结果会更新，本周只归属 v1 benchmark contract。
- **Direct Primary Sources:** https://arxiv.org/html/2501.14249v1；https://arxiv.org/abs/2501.14249；https://lastexam.ai/。
- **Related Primary Sources:** 论文列出的模型/system card只说明被测对象；不把其厂商主张并入 HLE 机制证据。
- **Access and Verification Status:** Full Source Review Complete；正文、review process、prompt、model versions与appendix可访问。
- **Full-read Coverage:** 已读 metadata、related work、collection、两轮专家review、LLM difficulty filtering、private holdout、evaluation prompt、accuracy/calibration、model versions与discussion。
- **Original Problem:** MMLU类封闭式学术benchmark趋于饱和，无法分辨frontier模型差异，也不能揭示错误时的置信度。
- **Why the Previous Design Was Reasonable:** 固定题集、自动评分和宽领域覆盖低成本可复算；在未饱和且污染较低时仍是有效能力proxy。
- **Changed Constraint:** frontier模型对旧题集接近天花板，公开题集又面临训练污染与benchmark gaming。
- **Mechanism:** 面向专家长尾知识收集原创、不可简单检索的短答案/多选题，经模型失败筛选和两轮专家review，公开主体并保留private holdout，同时要求模型报告confidence以测calibration。
- **State Ownership:** dataset release拥有题目/答案/review revision；private evaluator拥有holdout；evaluation run拥有model、prompt、modality与confidence output identity。
- **Control Flow / Data Flow:** 专家submission→frontier-model difficulty filter→human review/refinement→public/private split→versioned model execution→exact-match/choice scoring+RMS calibration→带条件的能力声明。
- **Implementation Details:** v1含3000题、跨百余学科，约10%含图像、80% exact-match；这些是版本事实，不外推为通用最优benchmark配比。
- **Evaluation Setup:** 多个frontier模型按附录prompt作答并给出0–100% confidence；DeepSeek-R1仅测text subset；model revisions列于appendix。
- **Baselines / Ablations / Sensitivity:** 以旧benchmark饱和度与多model横向结果作参照；缺少对review rubric、题型/学科配比和private/public split的系统ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API模型版本有记录；hardware、precision、batch、并发、latency和cost多未披露，因此只解释能力/校准，不作系统性能比较。
- **What the Evidence Actually Proves:** v1说明专家构题+模型筛选+人工review+private holdout可形成当时未饱和的封闭式学术能力测量，并暴露错误高置信现象。
- **What It Does Not Prove:** 不证明HLE等于通用智能、开放式研究、部署可靠性或长期不会饱和；低分也不定位失败来自知识、推理、视觉还是harness。
- **Limitations / Threats to Validity:** collection由“让当前模型失败”选择，随模型迭代发生selection drift；题型、语言、贡献者和专家领域分布有限；公开部分会污染。
- **Trade-offs / New Failure Modes:** frontier difficulty提高分辨率，却放大样本选择偏差、版本漂移、私有集不可审计与过拟合；exact scoring便宜，却压缩开放式过程质量。
- **Where the Previous Design Still Applies:** 稳定、低成本、面向已知技能的公开benchmark仍适合回归测试；高风险deployment还需system/trajectory/runtime evidence。
- **Evolution Relationship:** `Direct Evolution`：饱和公开题集→模型失败筛选+专家review→private holdout+calibration；不是用更难题替代完整Evaluation System。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主owner；handoff Ch23、67、71。
- **Target and Adjacent Chapters Read:** 已读 Ch65～67，并核对 Ch23 multimodal identity与 Ch71 governance；确认HLE只拥有dataset/evidence层。
- **Existing Coverage:** Ch66已有subject/distribution/scorer/uncertainty/release chain；HLE提供frontier benchmark decay与calibration案例，是否写入Books留待后续Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅回拨W04及年度索引；不把作者模型分数复制进Books。
- **Open Questions:** private holdout如何支持外部审计；题集迭代如何保持跨版本可比性；difficulty filtering如何避免把当前模型盲点固化为能力定义。

### Chain-of-Retrieval Augmented Generation

- **Candidate / Week / Score:** Chain-of-Retrieval Augmented Generation / 2025-W04 / 28/30。
- **Source Family ID:** `corag-iterative-retrieval-reasoning`。
- **Source Type:** arXiv v1、作者artifact与实验appendix。
- **First-public Date / Revision History:** v1 2025-01-24；本周按v1归档，后续revision不另计事件。
- **Direct Primary Sources:** https://arxiv.org/html/2501.14342v1；https://arxiv.org/abs/2501.14342。
- **Related Primary Sources:** Llama、E5与KILT/multi-hop datasets是依赖和baseline，不把其独立结论合并为CoRAG证据。
- **Access and Verification Status:** Full Source Review Complete；method、training、test-time scaling、analysis、prompts与appendix可访问。
- **Full-read Coverage:** 已读metadata、RAG related work、retrieval-chain rejection sampling、next-action training、greedy/best-of-N/tree decoding、setup、robustness、stop behavior与implementation details。
- **Original Problem:** 单次retrieve-then-generate把最初query和top-k结果一次性提交，复杂multi-hop问题中检索错误无法随新证据修正。
- **Why the Previous Design Was Reasonable:** 单检索路径状态少、成本低、易缓存和引用；问题可一次表达且retriever recall高时仍合理。
- **Changed Constraint:** multi-hop查询需要根据中间答案重写subquery，且test-time compute budget成为可调系统资源。
- **Mechanism:** 用rejection sampling从仅有最终答案的数据生成subquery/subanswer chains，微调模型按当前state预测下一action；推理时以chain length、best-of-N或tree search扩展计算，并学习停止。
- **State Ownership:** retriever/index拥有corpus snapshot；CoRAG controller拥有query/evidence/answer chain与budget；generator拥有next-action proposal，最终answer需绑定所用evidence。
- **Control Flow / Data Flow:** original query→subquery→retrieve passages→intermediate answer→updated state→repeat/stop→final answer；parallel chains再由scoring/selection合并。
- **Implementation Details:** v1以Llama-3.1-8B和E5-large为主要open setup，训练chain来自自动采样；最大chain length与sample count显式控制cost。
- **Evaluation Setup:** multi-hop QA与KILT任务，比较few-shot、single-step fine-tuned RAG、iterative RAG和Search-o1；指标含EM/F1，表内不同模型规模/上下文受控程度有限。
- **Baselines / Ablations / Sensitivity:** 比较L=1/6/10、greedy、best-of-4/8与tree search，并分析rejection sampling迭代、robustness、generalization和learn-to-stop。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型/检索器/chain budgets披露；hardware、precision、并发、index latency、token cost与tail SLO未形成完整serving contract。
- **What the Evidence Actually Proves:** 作者设置中，显式retrieval state与迭代query reformulation优于同数据single-step baseline，增加chain/sample budget可提高部分任务结果。
- **What It Does Not Prove:** 不证明更多retrieval steps单调有效、不证明所有RAG任务需要agentic search，也不证明EM提升能转化为citation fidelity或production goodput。
- **Limitations / Threats to Validity:** 自动chain可能含错误rationale；retriever/corpus固定；selection依赖答案可判定性；硬件/延迟/污染与权限未充分测量。
- **Trade-offs / New Failure Modes:** iterative retrieval提高修正机会，却引入query drift、证据重复、错误链自强化、停止失败、成本爆炸和跨step authorization/provenance负担。
- **Where the Previous Design Still Applies:** single-shot lexical/dense RAG适合简单事实、低延迟和高recall语料；预定义query decomposition适合流程稳定、需审计的领域。
- **Evolution Relationship:** `Direct Evolution`：single retrieval→stateful chain→parallel/tree test-time search；每层用更多状态与成本换覆盖，不是单向替代。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主owner；handoff `AGENT-CONTEXT`（Ch75）、`AGENT-WORKFLOW`（Ch81）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）。
- **Target and Adjacent Chapters Read:** 已读 Ch75～77、Ch81与Ch66；核对query dialect、index identity、derived state和trajectory evidence边界。
- **Existing Coverage:** Ch76已有iterative retrieval、query drift与budget contract；该family补充训练chain与test-time search证据，是否refine正文留待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不保留脱离retriever/corpus/chain budget的EM倍率。
- **Open Questions:** chain中错误evidence如何撤销；selection/verifier在无唯一答案任务如何训练；多租户budget、ACL与cache key如何进入同一state contract。

### RL + Transformer / In-Context Reinforcement Learning

- **Candidate / Week / Score:** RL + Transformer / ICRL / 2025-W04 / 23/30。
- **Source Family ID:** `icrl-trajectory-conditioned-adaptation`。
- **Source Type:** arXiv v1实验论文。
- **First-public Date / Revision History:** v1 2025-01-24；后续revision作为同family核验，不改变owner week。
- **Direct Primary Sources:** https://arxiv.org/html/2501.14176v1；https://arxiv.org/abs/2501.14176。
- **Related Primary Sources:** Llama 3.1、IA3、DQN/Polyak averaging是依赖；不把其通用能力归因于本实验。
- **Access and Verification Status:** Full Source Review Complete；正文、公式、环境、实验与结论可访问。
- **Full-read Coverage:** 已读POMDP/DQN背景、trajectory serialization、action-token loss、IA3 setup、in/out-distribution、behavior stitching、data quality、non-stationarity与exploration实验。
- **Original Problem:** 传统RL policy通常把适应写回parameters或专用state，部署时难以仅靠近期interaction迅速适应未知/变化环境。
- **Why the Previous Design Was Reasonable:** stationary task中固定policy推理简单、可预测；在线更新参数成本高且有稳定性/安全风险。
- **Changed Constraint:** partial observability、少样本新任务和环境transition变化要求policy从trajectory history中即时调整。
- **Mechanism:** 把state、action、非零reward和episode boundary序列化进Transformer context，以RL objective微调Llama 3.1 8B IA3 adapters；仅action tokens计loss，模型在context内近似Q-based adaptation。
- **State Ownership:** environment拥有真实transition/reward；trajectory buffer/context拥有近期interaction；frozen base+adapter拥有训练后的adaptation prior；模型输出只是action proposal。
- **Control Flow / Data Flow:** observation/reward history→tokenized trajectory→Transformer conditions Q/action→environment executes→new observation/reward append→context内策略变化。
- **Implementation Details:** 以POMDP和离散环境为主，目标网络用Polyak averaging；整段history输入，episode用special tokens分隔。
- **Evaluation Setup:** unseen in-distribution、OOD、behavior stitching、低质量数据、non-stationary变化和exploration，主要为受控小型RL环境。
- **Baselines / Ablations / Sensitivity:** 比较不同target update系数、history/interaction条件与数据质量；缺大规模真实工具环境和长期memory ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露Llama 3.1 8B与IA3；hardware、precision、context cost、batch、并发与实时控制deadline未形成完整contract。
- **What the Evidence Actually Proves:** 受控实验中，RL训练的Transformer能利用context内trajectory改善后续action，并对部分distribution shift表现适应。
- **What It Does Not Prove:** 不证明任意LLM成为通用problem solver，不证明适应可安全迁移到开放环境，也不证明长context状态优于显式belief/filter或parameter update。
- **Limitations / Threats to Validity:** toy/synthetic environments、离散action/reward、单模型family和有限horizon；reward可靠且history可放入context，与production差异大。
- **Trade-offs / New Failure Modes:** 免在线parameter update换来context增长、recent-history bias、reward poisoning、episode boundary错误与不可持久化；探索不足仍无法由序列建模自动解决。
- **Where the Previous Design Still Applies:** stationary/高风险控制用固定policy+显式state estimator更易验证；离线retraining适合长期稳定变化；短context任务无需trajectory learner。
- **Evolution Relationship:** `Alternative Branch`：parameter adaptation/explicit RL state ↔ context-conditioned ICRL；不是Transformer取代RL controller。
- **ROADMAP Node:** `AGENT-REFLECTION`（Ch80）主owner；handoff `AGENT-MEMORY`（Ch77）、`AGENT-WORKFLOW`（Ch81）与Ch25 world state。
- **Target and Adjacent Chapters Read:** 已读 Ch77、80、81与Ch25；核对derived memory、environment authority、feedback provenance和rollback边界。
- **Existing Coverage:** Ch80已有execution feedback与policy proposal边界；该paper补充context内适应案例，是否进入正文留待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不采用“general-purpose”标题作通用结论。
- **Open Questions:** context压缩后适应是否保真；adversarial reward/observation如何隔离；跨session state何时应写入memory而不是继续留在prompt。

### Redundancy Principles for MLLM Benchmarks

- **Candidate / Week / Score:** Redundancy Principles for MLLM Benchmarks / 2025-W04 / 25/30。
- **Source Family ID:** `mllm-benchmark-redundancy-audit`。
- **Source Type:** arXiv v1 empirical evaluation study。
- **First-public Date / Revision History:** v1 2025-01-20；Hugging Face后续收录不改变owner week。
- **Direct Primary Sources:** https://arxiv.org/html/2501.13953v1；https://arxiv.org/abs/2501.13953。
- **Related Primary Sources:** 20余benchmark和数百MLLM结果是分析输入；各benchmark论文仅定义其score，不证明本论文结论。
- **Access and Verification Status:** Full Source Review Complete；framework、metrics、experiments、recommendations与appendix可访问。
- **Full-read Coverage:** 已读dimension/instance/cross-benchmark redundancy定义、SRCC/PLCC/R2、top-k analysis、实验数据与practice recommendations。
- **Original Problem:** 多模态benchmark快速增加，但不同维度、样本和同域benchmark可能重复测同一ranking，浪费evaluation cost并制造虚假覆盖感。
- **Why the Previous Design Was Reasonable:** 新benchmark可快速覆盖新能力、降低单一题集偏差；模型与任务尚少时重复度并非首要成本。
- **Changed Constraint:** benchmark和模型数量扩大后，评测矩阵成本、解释冲突与重复ranking成为平台负担。
- **Mechanism:** 用跨模型performance vectors计算维度相关、实例子集稳定性和同域benchmark ranking一致性，再以top-k模型敏感性区分全局与frontier冗余。
- **State Ownership:** benchmark version拥有items/dimensions/scorer；evaluation registry拥有model-result matrix；redundancy audit拥有sampling、correlation和top-k policy。
- **Control Flow / Data Flow:** versioned result matrix→dimension correlation→instance subsampling→cross-benchmark ranking comparison→anchor/merge/retire proposal→人工review。
- **Implementation Details:** 采用SRCC、PLCC、R2等相关指标并比较Top/Bottom model subsets；相关性阈值与domain grouping不是自然常数。
- **Evaluation Setup:** 汇总数百MLLM在20余benchmark上的公开/复现实验结果，分析MMBench等维度、sample count和同域benchmark。
- **Baselines / Ablations / Sensitivity:** 比较不同correlation metrics、sample sizes和Top/Bottom subsets；缺对future model、distribution shift和score uncertainty的纵向验证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 研究对象是已有evaluation scores；底层hardware/precision/prompt多异构且未统一，不支持runtime性能结论。
- **What the Evidence Actually Proves:** 在所收集矩阵中，部分维度、样本和benchmark ranking高度相关，冗余必须相对model population/top-k operating point判断。
- **What It Does Not Prove:** 不证明高相关benchmark语义等价、不证明可直接删除任一题集，也不证明历史相关性在新模型或新prompt下稳定。
- **Limitations / Threats to Validity:** 聚合结果的harness/prompt/version不统一；correlation不等于相同failure coverage；公开leaderboard有选择偏差。
- **Trade-offs / New Failure Modes:** 压缩eval suite降低成本，却可能删除稀有slice、掩盖frontier differentiation并让anchor benchmark成为单点gaming目标。
- **Where the Previous Design Still Applies:** 新能力、high-risk slice和不同threat model仍需要专用benchmark；小suite在低成本回归中更实用。
- **Evolution Relationship:** `Direct Evolution`：增加benchmark→建立result matrix→冗余审计→风险保留的suite治理；不是数量越少越好。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主owner；handoff Ch65 data lineage与Ch71 governance。
- **Target and Adjacent Chapters Read:** 已读 Ch65～67、Ch71；核对EvalSpec、slice、uncertainty、evidence registry与release authority。
- **Existing Coverage:** Ch66已有benchmark decay和slice/uncertainty；本研究补充suite-level redundancy治理，Books是否refine待后续Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不根据单一correlation阈值删除任何长期知识。
- **Open Questions:** 如何把failure taxonomy和风险权重纳入冗余；异构harness结果如何校准；何时用conditional coverage而非ranking correlation。

### RealCritic

- **Candidate / Week / Score:** RealCritic / 2025-W04 / 25/30。
- **Source Family ID:** `realcritic-effectiveness-driven-critique-eval`。
- **Source Type:** arXiv v1 benchmark/method paper与human-evaluation appendix。
- **First-public Date / Revision History:** v1 2025-01-24；后续revision视为同family。
- **Direct Primary Sources:** https://arxiv.org/html/2501.14492v1；https://arxiv.org/abs/2501.14492。
- **Related Primary Sources:** CriticBench与被测模型用于baseline；不把其自评或system card当作RealCritic因果证据。
- **Access and Verification Status:** Full Source Review Complete；method、dataset、experiment、human protocol、post-check与prompts可访问。
- **Full-read Coverage:** 已读open-loop critique问题、closed-loop effectiveness metric、self/cross/iterative modes、8 reasoning tasks、human validation、selection strategy与appendix。
- **Original Problem:** 以critique文本是否像“好批评”作open-loop评分，可能奖励措辞正确但无法帮助修正答案的反馈。
- **Why the Previous Design Was Reasonable:** 直接标注critique质量便宜、无需重新执行solver；final answer不可自动验证时仍可能是唯一proxy。
- **Changed Constraint:** reasoning模型把critique用于self/cross、多轮修正，需要测量反馈是否真实改变downstream solution。
- **Mechanism:** 将critique交给solver生成refined solution，以从错误到正确的转化衡量effectiveness，并分别构造self/cross和single/iterative critique modes；human review校验旧benchmark误判。
- **State Ownership:** input solution和ground truth属于task dataset；critique/refinement trajectory属于evaluation run；judge/scorer只拥有measurement，不拥有任务真值。
- **Control Flow / Data Flow:** problem+initial solution→critic feedback→solver revision→task verifier→effectiveness score；多轮模式重复并保留trajectory。
- **Implementation Details:** 八类reasoning task和多种frontier/open模型；post-check和priority filtering用于提高样本质量，但引入额外model/judge依赖。
- **Evaluation Setup:** 比较self/cross与iterative critique，测多个model；human evaluators检查critique quality和旧benchmark误判。
- **Baselines / Ablations / Sensitivity:** 对比CriticBench式open-loop proxy、不同critic/solver pairing及轮数；缺跨domain、tool execution和真实side-effect任务验证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model版本和task可定位；hardware、precision、token budget、并发、latency和cost未形成系统contract。
- **What the Evidence Actually Proves:** 在所测reasoning tasks中，critique对后续修正的effect可揭示open-loop评分遗漏，self/cross和迭代模式表现不同。
- **What It Does Not Prove:** 不证明corrected answer完全由critique导致、不证明更多轮更好，也不证明benchmark覆盖开放式workflow可靠性。
- **Limitations / Threats to Validity:** solver capability与critic quality耦合；ground-truth verifier集中于可判定任务；model-generated filtering可能循环偏差。
- **Trade-offs / New Failure Modes:** closed-loop更接近作用结果，却增加solver confound、token/cost和trajectory variance；critic可针对特定solver“过拟合”。
- **Where the Previous Design Still Applies:** low-cost component regression、不可执行的开放反馈仍可用human/open-loop rubric；但不能独立作release gate。
- **Evolution Relationship:** `Direct Evolution`：text-quality proxy→downstream correction→self/cross/iterative trajectory；是evidence ladder，不是旧scorer失效。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主owner；handoff `AGENT-REFLECTION`（Ch80）与Ch67 observability。
- **Target and Adjacent Chapters Read:** 已读 Ch66～67与Ch79～81；核对component/process/outcome evaluation、trajectory identity和execution feedback边界。
- **Existing Coverage:** Ch66已有outcome/trajectory ladder，Ch80拥有reflection mechanism；该family提供closed-loop critique案例，Books决策后置。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不保留无token/model contract的模型排名。
- **Open Questions:** 如何分离critic与solver贡献；多轮何时停止；不可自动验证任务怎样构造actionable-outcome scorer并控制judge contamination。

### Baichuan-Omni-1.5

- **Candidate / Week / Score:** Baichuan-Omni-1.5 / 2025-W04 / 25/30。
- **Source Family ID:** `baichuan-omni-1-5-staged-multimodal-alignment`。
- **Source Type:** arXiv technical report、官方repository与model artifacts。
- **First-public Date / Revision History:** v1 2025-01-26；后续artifact/revision作为同family演进节点。
- **Direct Primary Sources:** https://arxiv.org/html/2501.15368v1；https://arxiv.org/abs/2501.15368；https://github.com/baichuan-inc/Baichuan-Omni-1.5。
- **Related Primary Sources:** image/audio encoders、audio codec与各benchmark定义作为依赖；不合并其独立结果。
- **Access and Verification Status:** Full Source Review Complete；architecture、data、training、evaluation、repository可访问；完整训练数据/cluster未公开。
- **Full-read Coverage:** 已读metadata、multimodal data cleaning/synthesis、visual/audio branches、audio tokenizer、image-text→image-audio-text→omni pretraining、SFT与language/image/video/audio/medical evaluation。
- **Original Problem:** 分别拼接视觉、音频和文本模块容易造成modality interference，且理解与端到端语音生成需要不同表示粒度。
- **Why the Previous Design Was Reasonable:** 专用encoder+projector可独立升级、数据需求低、故障隔离清楚；只做理解或单模态服务时仍更简单。
- **Changed Constraint:** omni interaction要求图像、视频、音频、文本共同进入backbone，并从语义理解走到声学生成而不显著损伤各模态。
- **Mechanism:** 视觉分支与audio encoder/tokenizer提供modality representations；约500B多模态数据经清洗/合成；训练按image-text、image-audio-text、omni-modal pretraining再multimodal SFT逐步解冻/对齐。
- **State Ownership:** preprocessing/encoder/tokenizer拥有modality artifact和采样identity；backbone拥有联合sequence state；audio decoder拥有waveform reconstruction；dataset stages拥有mixture/provenance。
- **Control Flow / Data Flow:** raw image/video/audio/text→modality-specific preprocessing/encoding→joint token sequence→staged pretraining/SFT→理解输出或audio tokens→waveform decoder。
- **Implementation Details:** 7B model与独立audio tokenizer；report披露多阶段data composition和branch设计，具体cluster、optimizer完整contract与production streaming未闭合。
- **Evaluation Setup:** language、image、video、audio、omni和medical benchmark；部分baseline数字来自官方报告/其他论文，部分由作者复现，表中用标记区分。
- **Baselines / Ablations / Sensitivity:** 多model横向比较；缺对每个training stage、data mixture、tokenizer与branch独立ablation，难将收益归因单一机制。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B与data/tokenizer facts披露；training/serving hardware、precision、batch、streaming latency、并发和SLO未完整公开。
- **What the Evidence Actually Proves:** 公开family展示在一个7B backbone上组合多模态理解和audio generation、并以staged alignment维持多任务能力的可行路径。
- **What It Does Not Prove:** 不证明500B等价于高质量有效token、不证明normalized benchmark平均值代表生产交互，也不证明native omni必然优于modular pipeline。
- **Limitations / Threats to Validity:** 厂商自评、私有/合成数据、baseline条件异构、component ablation和runtime contract不足；医疗结果不等于临床安全。
- **Trade-offs / New Failure Modes:** 统一backbone促进cross-modal transfer，却引入data ratio interference、codec/version coupling、不同采样时钟、长sequence和生成安全问题；staged training增加checkpoint lineage与遗忘风险。
- **Where the Previous Design Still Applies:** frozen encoder+projector适合窄域、数据少和独立升级；专用ASR/TTS链在低延迟、可审计或音质优先时仍合理。
- **Evolution Relationship:** `Layering / Dependency`：专用encoders→joint representation→staged omni alignment→audio generation；不是用统一模型否定模块化系统。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主owner；handoff Ch24生成范式、Ch27数据与Ch66评测。
- **Target and Adjacent Chapters Read:** 已读 Ch23～24、Ch27和Ch66；核对modality/artifact identity、generation boundary、data mixture与evaluation contract。
- **Existing Coverage:** Ch23已有projector/shared/native分支和codec identity；该report提供staged omni案例，是否吸收具体机制待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不复制厂商normalized scores或医疗能力主张。
- **Open Questions:** staged mixture如何测interference；audio tokenizer与backbone版本如何迁移；streaming interruption、turn state与safety如何进入runtime/eval contract。

### ARWKV

- **Candidate / Week / Score:** ARWKV / 2025-W04 / 23/30。
- **Source Family ID:** `arwkv-transformer-to-rnn-distillation`。
- **Source Type:** arXiv v1、开源checkpoint与repository。
- **First-public Date / Revision History:** v1 2025-01-26；论文明确为ongoing work，后续版本不得反写v1事实。
- **Direct Primary Sources:** https://arxiv.org/html/2501.15570v1；https://arxiv.org/abs/2501.15570；https://github.com/yynil/RWKVInside。
- **Related Primary Sources:** Qwen2.5与RWKV-7是teacher/base architecture dependencies；其独立能力不并入ARWKV证据。
- **Access and Verification Status:** Full Source Review Complete；architecture、三阶段conversion、evaluation、ablation与artifacts可访问。
- **Full-read Coverage:** 已读GQA→RWKV-7 time-mixing替换、hidden-state alignment、word-level KL distillation、SFT/DPO、evaluation、gate/freeze/teacher-size ablation与future work。
- **Original Problem:** 重新从头预训练linear-RNN成本高，而直接换掉attention会破坏Transformer已经学习的representation和输出分布。
- **Why the Previous Design Was Reasonable:** 从头pretraining使architecture与optimization共同适配，证据最干净；标准Transformer在long-context retrieval和并行训练上成熟。
- **Changed Constraint:** 希望把已有Transformer知识迁移到fixed-state recurrent inference，降低token生成时KV增长，同时避免完整pretraining预算。
- **Mechanism:** 保留RMSNorm/SwiGLU，将GQA替换为RWKV-7 time mixing；先对齐teacher/student hidden states，再用token-level KL做knowledge distillation，最后SFT+DPO恢复instruction behavior。
- **State Ownership:** teacher checkpoint拥有source distribution；student conversion checkpoint拥有architecture mapping；RWKV recurrent state拥有decode history摘要；training stages拥有各自optimizer/data lineage。
- **Control Flow / Data Flow:** Qwen teacher→attention replacement→hidden-state alignment→KL output distillation→SFT/DPO→RWKV recurrent decode state逐token更新。
- **Implementation Details:** 论文以7B为主并提到32B→7B teacher；stage 2仅约20M tokens的作者事实需绑定其dataset/teacher，不代表通用conversion成本。
- **Evaluation Setup:** language benchmarks与state-tracking任务，比较不同gate、MLP freeze和teacher size的distilled 7B variants。
- **Baselines / Ablations / Sensitivity:** ablate gate、是否冻结MLP、teacher 7B/32B；缺等预算从头RWKV预训练、长context retrieval和production decode系统比较。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 摘要提及另一QRWK 32B路径在16 AMD MI300X/8小时；该事实不是主要ARWKV 7B完整contract，precision、length、batch、并发/SLO不充分。
- **What the Evidence Actually Proves:** 在作者设置中，可通过representation/output distillation把Transformer checkpoint转换为RWKV-style student并保留部分能力。
- **What It Does Not Prove:** 不证明“pretrain不再需要”、fixed recurrent state无长程信息损失，或ARWKV在相同硬件/精度/SLO下优于Transformer。
- **Limitations / Threats to Validity:** ongoing work、实验规模有限、teacher/data dependence强、长context与系统指标不足；artifact evolution可能偏离v1。
- **Trade-offs / New Failure Modes:** conversion节省从头训练却引入teacher bias、stage coupling和silent capability loss；fixed state降低KV增长，却增加不可逆压缩、state corruption和checkpoint incompatibility。
- **Where the Previous Design Still Applies:** 从头pretraining适合新architecture充分验证；Transformer适合需精确随机访问历史、成熟kernel和训练并行的场景；hybrid attention/RNN是中间分支。
- **Evolution Relationship:** `Alternative Branch`：Transformer pretrain→architecture conversion/distillation→recurrent decode；不是RNN取代attention的线性进化。
- **ROADMAP Node:** `MODEL-ATTENTION`（Ch15）主owner；handoff `MODEL-LONG-CONTEXT`（Ch22）、Ch28 pretraining与Ch44 decode/KV state。
- **Target and Adjacent Chapters Read:** 已读 Ch14～17、Ch22、Ch28与Ch44～45；核对attention semantics、state compression、training lineage和runtime memory边界。
- **Existing Coverage:** Ch15/22已有quadratic、linear/recurrent分支和历史状态压缩；该conversion family是否补充distillation路线待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；标题中的“Pretrain is not what we need”不作为结论。
- **Open Questions:** recurrent state corruption如何恢复；teacher/student tokenizer与layer mapping如何版本化；相同quality/SLO下训练+服务总成本如何比较。

### Parameters vs FLOPs / MoE Sparsity Scaling

- **Candidate / Week / Score:** Parameters vs FLOPs / MoE Sparsity Scaling / 2025-W04 / 27/30。
- **Source Family ID:** `moe-parameters-active-flops-optimal-sparsity`。
- **Source Type:** arXiv v1 scaling-law empirical study与appendix。
- **First-public Date / Revision History:** v1 2025-01-21；延迟聚合发现不改变owner week。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12370v1；https://arxiv.org/abs/2501.12370。
- **Related Primary Sources:** MoE architecture与Chinchilla-style scaling是理论/实验依赖，不将其独立结果合并。
- **Access and Verification Status:** Full Source Review Complete；公式、IsoFLOP fit、setup、downstream/CoT analysis、limitations与appendix可访问。
- **Full-read Coverage:** 已读total/active parameters定义、top-k/expansion/granularity、compute-optimal fit、training-budget sensitivity、downstream reasoning、FLOP estimator与limitations。
- **Original Problem:** MoE可增加total parameters而不同比增加active FLOPs，使dense scaling中“参数量≈每token计算”的单轴capacity失效。
- **Why the Previous Design Was Reasonable:** dense模型里total/active parameters接近，单一N和training FLOPs足以给出近似compute-optimal recipe。
- **Changed Constraint:** sparsity将stored capacity、active compute、training tokens、communication和inference workload解耦，需要多约束选择operating point。
- **Mechanism:** 在固定total training compute和/或parameter budget下训练不同sparsity/size模型，拟合IsoFLOP surfaces，估计total parameters与active FLOPs的最优组合，并检查downstream/CoT偏离。
- **State Ownership:** architecture spec拥有experts/top-k/granularity；training planner拥有token/compute budget；router/runtime拥有实际activation与communication；evaluation拥有up/downstream contract。
- **Control Flow / Data Flow:** budget constraints→model/sparsity grid→pretraining runs→loss surface fit→candidate optimum→downstream and inference-sensitive validation→deployment feasibility review。
- **Implementation Details:** 明确区分N与Na并修正MoE FLOP估计；论文中的最优sparsity是所测model/data/budget family条件结果。
- **Evaluation Setup:** 多个training budgets和model sizes，pretraining loss/perplexity及下游任务；附录含长度控制CoT和不同sparsity reasoning sensitivity。
- **Baselines / Ablations / Sensitivity:** dense与不同sparsity、预算、size、downstream/CoT对比；未覆盖真实expert parallel network、load imbalance和serving batching。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training recipe在appendix披露部分参数；端到端hardware topology、precision、EP communication、serving concurrency和SLO不足，不能直接推生产最优。
- **What the Evidence Actually Proves:** 在作者实验范围内，最优sparsity随parameter/compute约束变化；相同pretraining perplexity下更稀疏模型在部分reasoning任务可能更弱。
- **What It Does Not Prove:** 不证明越稀疏越好、不证明FLOPs等于wall-clock/cost，也不证明fit可外推到更大规模、不同router、数据或hardware。
- **Limitations / Threats to Validity:** 规模与任务有限、curve extrapolation、FLOP proxy忽略communication/memory/router imbalance，downstream selection有限。
- **Trade-offs / New Failure Modes:** 增加inactive capacity可提升参数效率，却减少每token active compute并增加expert placement、routing、cold expert与all-to-all成本；reasoning可能先退化。
- **Where the Previous Design Still Applies:** dense适合小规模、低延迟、通信受限和稳定能力；低sparsity/高active compute适合reasoning或无法容纳大expert set的系统。
- **Evolution Relationship:** `Direct Evolution`：dense single-axis scaling→N/Na two-axis sparsity→training/inference/hardware joint optimum；新轴不否定dense branch。
- **ROADMAP Node:** `MODEL-MOE`（Ch21）主owner；handoff `TRAIN-MOE`（Ch36）、Ch37 tensor parallel与Ch49 execution planning。
- **Target and Adjacent Chapters Read:** 已读 Ch21、Ch36～37、Ch40与Ch49；核对router objective、expert dispatch、collective和hardware feasibility。
- **Existing Coverage:** Ch21已有capacity/compute/communication三约束；该paper补充scaling fit与reasoning边界，Books修改待后续Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不把作者optimal sparsity或FLOP fit写成通用配置。
- **Open Questions:** 如何把network/memory/goodput加入scaling law；router imbalance与expert reuse如何改变Na；reasoning regression能否由更多test-time compute补偿。

### CodeMonkeys

- **Candidate / Week / Score:** CodeMonkeys / 2025-W04 / 28/30。
- **Source Family ID:** `codemonkeys-serial-parallel-test-time-software-workflow`。
- **Source Type:** arXiv v1、作者project、代码与数据artifact。
- **First-public Date / Revision History:** v1 2025-01-24；后续artifact更新作为同family，不重计事件。
- **Direct Primary Sources:** https://arxiv.org/html/2501.14723v1；https://arxiv.org/abs/2501.14723；https://scalingintelligence.stanford.edu/pubs/codemonkeys/。
- **Related Primary Sources:** SWE-bench Verified定义环境/ground truth；其他agents仅作baseline，不合并其机制证据。
- **Access and Verification Status:** Full Source Review Complete；system stages、state machines、hyperparameters、cost、limitations与artifact可访问。
- **Full-read Coverage:** 已读relevance ranking、edit/test state machines、serial/parallel scaling、candidate test voting、selection trajectory、SWE-bench setup、DeepSeek appendix、cost与limitations。
- **Original Problem:** 并行采样可提高“至少一个候选正确”的coverage，但若没有可执行feedback和可靠selection，覆盖无法转化为最终solve rate。
- **Why the Previous Design Was Reasonable:** 单trajectory agent成本低、state简单，模型足够强或issue简单时无需candidate pool；现成framework利于快速迭代。
- **Changed Constraint:** repo-scale问题需要更多context、反复execution反馈和多个候选，test-time compute必须在serial depth、parallel breadth和selection之间分配。
- **Mechanism:** 先让LLM阅读/排序repo files；每个issue并行运行edit与standalone test生成/修正state machines；candidate tests互相执行投票，再用专用multi-turnselection trajectory选final patch。
- **State Ownership:** repository snapshot/environment拥有ground truth；每个trajectory拥有workspace/edit/test/history；orchestrator拥有budget、candidate pool与selection；generated tests是imperfect evidence而非truth。
- **Control Flow / Data Flow:** issue+repo→file relevance→N parallel edit/test loops→execution feedback→candidate×test result matrix→vote/selector trajectory→final patch→official harness。
- **Implementation Details:** serial compute由每个state machine最大completion次数控制，parallel compute由independent machines数控制；test以standalone Python/exit code传递可执行反馈。
- **Evaluation Setup:** SWE-bench Verified，论文主要系统用多trajectory和candidate selection；报告约$2300预算和作者solve rates，仅代表其模型/API/时间点。
- **Baselines / Ablations / Sensitivity:** 比较serial/parallel scaling、selection方法、relevance context和外部candidate ensemble；每阶段仍有明显oracle gap。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API model、sample counts与dollar budget较明确；provider hardware/precision不可见，wall-clock、并发上限、tail latency和rate limit不完整。
- **What the Evidence Actually Proves:** 在固定SWE-bench环境中，serial execution feedback+parallel candidates+explicit selection可把sampling coverage的一部分转为final resolution。
- **What It Does Not Prove:** 不证明更多agents/samples单调有效、不证明generated tests可靠，也不证明SWE-bench成绩代表生产软件工程、安全或maintainability。
- **Limitations / Threats to Validity:** 单benchmark、API/model依赖、test leakage/weak verifier风险、成本高；selector可能偏好通过错误tests的patch。
- **Trade-offs / New Failure Modes:** breadth提高coverage却增加cost/rate pressure；depth改善修正却可能循环；generated tests提供feedback却可错判；共享repo并行会引入workspace isolation与artifact contamination。
- **Where the Previous Design Still Applies:** 单agent适合简单issue/低预算；human review适合高风险变更；静态tests和deterministic tools在可验证domain仍优于model-generated verifier。
- **Evolution Relationship:** `Direct Evolution`：single trajectory→serial feedback→parallel candidates→evidence-based selection；每层引入新的state owner和failure surface。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主owner；handoff Ch78 tools、Ch80 reflection、Ch82 multi-agent与Ch66 evaluation。
- **Target and Adjacent Chapters Read:** 已读 Ch78～82与Ch66；核对tool proposal/commit、durable workflow、parallel isolation、verifier与outcome gate。
- **Existing Coverage:** Ch81/82已有serial/parallel compute、candidate selection和error amplification；该paper提供software-workflow证据，Books决策后置。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不复制作者solve-rate或成本为通用系统结论。
- **Open Questions:** generated test如何校准false positive；candidate workspaces怎样隔离并复算；预算控制何时停止；selector如何证明未利用benchmark artifact泄漏。

### DeepFlow

- **Candidate / Week / Score:** DeepFlow / 2025-W04 / 29/30。
- **Source Family ID:** `deepflow-serverless-flowserve-state-aware-serving`。
- **Source Type:** arXiv v1 production-system paper与Huawei Cloud/Ascend official references。
- **First-public Date / Revision History:** v1 2025-01-24；W05聚合发现不改变owner week，后续revision不反写v1实现。
- **Direct Primary Sources:** https://arxiv.org/html/2501.14417v1；https://arxiv.org/abs/2501.14417。
- **Related Primary Sources:** vLLM/SGLang/DistServe/Mooncake等只解释baseline/dependency；不将其独立结果并入DeepFlow。
- **Access and Verification Status:** Full Source Review Complete；platform、FlowServe、RTC、DistFlow、scheduling、scaling与evaluation可访问；完整production code/trace未公开。
- **Full-read Coverage:** 已读request-job-task、JE/TE/cluster manager、microkernel/NPU-centric/SPMD、async scheduler、RTC/DistFlow、PD colocated/disaggregated study、locality/PD-aware algorithm、prewarm/DRAM/NPU-fork与全部实验。
- **Original Problem:** 多租户AI workload时长和shape异构，LLM serving又因KV locality、PD分池和cold start变成分布式有状态系统，普通serverless+无状态load balancing无法同时满足SLO与利用率。
- **Why the Previous Design Was Reasonable:** monolithic replica、load-only routing和storage-load启动状态少、故障边界简单；短prompt、低reuse、稳定流量或小规模集群仍合理。
- **Changed Constraint:** prefix cache、phase disaggregation、Ascend topology与突发扩缩容要求平台同时管理logical workload、tensor identity/residency、placement和readiness。
- **Mechanism:** request→job→task统一post-training/serving；JE拆任务、TE执行、cluster manager扩缩；FlowServe以central master+SPMD executors运行，RTC统一block/cache relation，DistFlow移动memory-semantic tensors；scheduler联合load/locality/PD，scale path用prewarm、DRAM preload、NPU link和fork。
- **State Ownership:** request/job/task属于serverless control plane；JE拥有decomposition/routing；FlowServe master拥有scheduling/index decisions；RTC拥有tensor relation/residency；executors拥有physical blocks；cluster manager拥有membership/health/readiness。
- **Control Flow / Data Flow:** HTTP request→JE→job/tasks→TE group→RTC match/cost model→async populate via DistFlow→central scheduler token plan→SPMD execution→PD KV transfer→decode；metrics/health→cluster manager→prewarm/load/scale。
- **Implementation Details:** FlowServe Python control + C++ RTC/DistFlow；prefix/ID hybrid index，NPU/DRAM tiers，HCCL P2P或SuperPod copy backend；PP chunk分布和DP RTC replicas为v1实现事实。
- **Evaluation Setup:** 34B TP=4 offline decode、internal约2K input/200 output online trace，RPS 0.2–1.2；PD 2P2D/2P1D与4 colocated；fast scaling、loading和production cluster数据。
- **Baselines / Ablations / Sensitivity:** 比较FlowServe versions、sync/async、PD ratios/colocation、prefill/decode regions、locality/load/PD-aware scheduling和scaling techniques；组合优化缺完全独立ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Ascend NPU、34B、TP4、2K/200、RPS与部分TPOT/JCT条件披露；具体NPU generation、precision、batch、network load、tenant mix和tail SLO不全，倍率不可外推。
- **What the Evidence Actually Proves:** 在作者生产/实验环境中，显式tensor state、phase/workload type与readiness可进入serverless serving control loop；PD/colocation最优区域依请求shape变化。
- **What It Does Not Prove:** 不证明serverless抽象消除state、不证明PD总优于colocation、不证明central scheduler或作者64-instance scale数字跨hardware/topology成立。
- **Limitations / Threats to Validity:** 厂商自测、internal trace/code、Ascend-specific stack、failure/recovery与multi-tenant fairness数据有限；operator-level A/E disaggregation仍属future work。
- **Trade-offs / New Failure Modes:** 统一control plane提高resource sharing，却扩大blast radius；central index简单但有IPC/freshness瓶颈；reuse/locality会造热点；async predicted allocation和prefetch引入stale state/cancel/reconcile；prewarm降低冷启动却占保留容量。
- **Where the Previous Design Still Applies:** colocated TE适合短prompt/长decode或transfer不划算；load-only routing适合低reuse；cold load适合稀有模型；engine-local KV适合缩小failure domain。
- **Evolution Relationship:** `Direct Evolution`：stateless serverless→typed request/job/task→state-aware engine→PD/locality-aware fleet→readiness-aware fast scaling；每层新增owner和failure semantics。
- **ROADMAP Node:** `INFER-DYNAMO`（Ch52，distributed runtime responsibility）主owner；handoff Ch51 cache identity、Ch55 PD、Ch56 scheduling、Ch57 platform foundations与Ch63 resource scheduling。
- **Target and Adjacent Chapters Read:** 已读 Ch51～57与Ch63；核对request/control/state paths、transfer commit、PD coexistence、admission/readiness与platform/controller边界。
- **Existing Coverage:** Ch52/55/56已有state-aware routing、PD region和control loop；DeepFlow提供Ascend/serverless production family，是否refine正文待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Books Gate关闭。
- **Changed Files or Rejection Reason:** 仅更新W04与年度索引；不复制脱离model/hardware/RPS/SLO的倍率或64-instance headline。
- **Open Questions:** RTC/DistFlow在worker failure下的generation/rebuild；central JE/cluster manager如何隔离租户；PD heatmap如何在线校准；prewarm保留容量怎样计费与回收。

### Continuous 3D Perception / CUT3R

- **Candidate / Week / Score:** Continuous 3D Perception Model with Persistent State / 2025-W04 / 25/30。
- **Source Family ID:** `cut3r-continuous-3d-persistent-scene-state`。
- **Source Type:** arXiv v1 research paper + official project/repository artifact。
- **First-public Date / Revision History:** arXiv v1 2025-01-21；W06 的 2 月10日 discovery 推荐页不改变 W04 owner；后续 revision 仅作同 family 核验。
- **Direct Primary Sources:** https://arxiv.org/html/2501.12387v1；https://arxiv.org/abs/2501.12387；https://cut3r.github.io/。
- **Related Primary Sources:** DUSt3R、MASt3R、Spann3R、MonST3R 与 MegaSaM 只定义 pairwise/global-alignment、spatial-memory 与 optimization baselines，不替代本论文证据。
- **Access and Verification Status:** Full Source Review Complete；正文、公式、训练/数据、online evaluation、ablation、runtime 与 supplement 关键内容已核验。
- **Full-read Coverage:** 已读 metadata、Introduction/Related Work、state-input interaction、virtual-view query、loss/data/training、depth/pose/reconstruction/novel-view tasks、online/offline baselines、state-size与sequence-order ablation、limitations/conclusion。
- **Original Problem:** pairwise 3D reconstruction 需要事后 global alignment，静态 spatial memory 难处理动态场景，per-video optimization 又无法随观测流在线更新统一世界坐标。
- **Why the Previous Design Was Reasonable:** pairwise matching 和显式全局优化提供可解释几何约束；静态场景、小批图像与最高精度优先时，离线 bundle/global alignment 仍更稳健。
- **Changed Constraint:** 输入变成长视频、无序照片或动态场景，系统需要边到达边更新、无需相机标定，并在共同坐标系持续输出而不是等待全序列结束。
- **Mechanism:** 把场景压缩为 recurrent state tokens；每帧 image tokens 与 state 通过双 decoder 双向交互，分别执行 state update 与 state readout；pose token 和三个 heads 输出 self/world pointmaps、confidence 与 6-DoF pose；virtual raymap 只读 state、不写入新内容。
- **State Ownership:** recurrent state tokens 拥有跨帧 latent scene summary；image tokens 拥有当前 observation；pose token 拥有 view-level motion；world frame 由首帧定义；virtual query 是只读访问者，不拥有新事实。
- **Control Flow / Data Flow:** image stream→ViT tokens→与 previous state cross-attend→new state + context-enriched frame tokens→metric pointmaps/pose；virtual camera raymap→shared decoder readout→unseen-view geometry/color，且不提交 state update。
- **Implementation Details:** learnable initial state、interconnected decoder blocks、DPT self/world heads、MLP pose head与 raymap encoder；冗余监督使 pose-only、single-view depth 等部分标注数据也可参与训练。
- **Evaluation Contract:** 在 Sintel、TUM-dynamics、ScanNet、KITTI、Bonn、7-Scenes、NRGBD 等任务比较 video depth、camera pose、3D reconstruction 与 novel-view prediction；online 与需要 test-time optimization 的方法分组报告。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 DUSt3R/MASt3R global alignment、Spann3R、MonST3R、MegaSaM 等；核验 state token count、input order、frame length、metric/world supervision 与 query branch；速度数字绑定论文设备和数据集，不能跨系统外推。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露训练/评测模型配置与部分 FPS，但 production hardware、precision、并发、长期 state retention、tail latency 与 SLO 不完整；17 FPS/倍数仅属于作者测试合同。
- **What the Evidence Actually Proves:** 在作者数据与任务中，固定大小 recurrent latent state 能把逐帧观测对齐进统一坐标并支持在线 pointmap/pose 输出；只读 virtual query 可从已写 state 生成未观测视角预测。
- **What It Does Not Prove:** 不证明 latent state 是可审计的完整世界模型、不证明无限序列无遗忘，也不证明对开放世界动态拓扑、闭环行动或安全关键机器人控制可靠。
- **Limitations / Threats to Validity:** state 是有损压缩；首帧 world-frame 锚定可能积累漂移；动态对象与静态背景仍可能混淆；作者 benchmark、训练数据覆盖和无显式 uncertainty calibration 限制外推。
- **Trade-offs / New Failure Modes:** 去掉 global optimization 获得在线性，却引入不可逆 state overwrite、顺序敏感、漂移、过期动态对象、query hallucination 与恢复/回滚困难；固定 state 容量把内存增长换成遗忘风险。
- **Where the Previous Design Still Applies:** 最高几何精度、完整序列可用或需要闭环校正时，显式 SfM/SLAM/global alignment 仍合理；短序列和静态场景可用 pairwise/spatial memory 减少隐藏状态风险。
- **Evolution Relationship:** `Direct Evolution`：pairwise pointmaps→offline global alignment→static spatial memory→recurrent persistent latent state；virtual-view readout 是在同一 state 上叠加的只读查询层。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `MULTIMODAL-EMBODIED-VLA` Ch26、`AGENT-MEMORY` Ch77 与 State 横轴。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 的 representation/world-state/action boundary，以及 Ch77 的 derived memory/provenance 边界。
- **Existing Coverage:** Ch25 已区分 observation generation、action-conditioned transition 与 persistent world state；CUT3R补充 perception-only recurrent state 的前代分支，但 Books 判断按用户要求延期。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete，Historical Books Gate 关闭。
- **Changed Files or Rejection Reason:** 仅回拨更新 W04 与年度索引；不修改 Books，不把作者 FPS 或 benchmark 排名写成通用系统结论。
- **Open Questions:** state 何时 supersede/expire 动态事实；如何 checkpoint、branch、rollback 与跨设备迁移；如何校准 virtual-view uncertainty；加入 action 后怎样区分 prediction error 与 control-induced transition。

## Low-Score Verification Ledger

| Candidate | First-public / Revision | Verified Primary Source | Final Rejection Reason |
| --- | --- | --- | --- |
| Reasoning Language Models: A Blueprint — 19/30 | v1 2025-01-20；v2/v3同周；v4 2025-06-11 | arXiv identity、abstract、blueprint/x1 scope与revision history已核验 | 综述/统一框架主要组织既有RL、search、supervision与test-time compute，不构成本周独立机制证据；保留为discovery map |
| TokenVerse — 19/30 | v1 2025-01-21 | arXiv identity、abstract、modulation-space word directions与project page identity已核验；experimental HTML错配被记录 | 单图、多概念T2I personalization的optimization case，未改变本书通用representation/generation结论；不升级为Full Source Review |
| PAINT / Fixing Imbalanced Attention — 19/30 | v1 2025-01-21；v2/v3 2025-03-24/26 | arXiv v1 HTML/abs、local+summary/spatial token selection、head-specific modulation与MSCOCO scope已核验 | 单dataset、plug-in attention intervention；62.3%作者结果缺跨model/workload长期系统证据，保留Experimental |
| One-Prompt-One-Story — 19/30 | v1 2025-01-23；v2/v3 2025-01-30/02-05 | arXiv v1 HTML/abs、single concatenated prompt、singular-value reweighting、identity cross-attention和limitations目录已核验 | training-free consistent-story narrow branch；不改变通用diffusion state/identity owner，且作者“free-lunch”不作系统结论 |
| EchoVideo — 19/30 | v1 2025-01-23；v2 2025-02-27 | arXiv v1 HTML/abs、IITF、two-stage stochastic shallow-feature use与evaluation scope已核验 | identity-preserving human-video的专用feature-fusion recipe；缺跨base/long-video/system contract，保留Experimental |
| GPS as a Control Signal — 18/30 | v1 2025-01-21；v2 2025-01-22 | arXiv abs与同ID PDF identity、GPS+text diffusion conditioning、SDS 3D extraction scope已核验；HTML错配保留 | 地理metadata控制是有用但窄的conditioning实例，不形成新的通用生成范式；位置隐私/偏差使其不宜脱离domain contract外推 |
| Panoramic Interests / SCAPE — 18/30 | v1 2025-01-21；v2 2025-01-28 | arXiv HTML/abs、LLM attribute extraction、long/short-term stylistic-content fusion与PENS scope已核验 | 初始被误识别为panorama视觉论文，实际是个性化headline generation；领域推荐/生成case不属于AI System主干，纠正身份后维持低分 |
| MatAnyone — 18/30 | v1 2025-01-24；v2 2025-03-25 | arXiv v1 identity、完整 HTML、region-adaptive memory fusion、training/data/ablation 与 limitations 已核验 | first-frame target mask→frame-wise memory update 对 video matting 有效，但证据受特定 task、dataset 与作者评测限制；不能外推为通用 long-video/world-state runtime |
| Transformers 4.48.1 — 16/30 | release 2025-01-20；commit `2e752ea` | 官方 GitHub release tag、三项修复说明与关联 PR identity 已核验 | 补丁修复 gradient-accumulation condition、Phi bias 与 Moonshine wrapper regression；属于 compatibility/correctness maintenance，不新增可迁移的系统机制 |

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- DeepSeek-R1 → `TRAIN-GRPO`（Ch33），handoff Ch29、31、34、35、66
- Kimi k1.5 → `TRAIN-GRPO`（Ch33）/`TRAIN-CHECKPOINT`（Ch35），handoff Ch22、36、56
- Chain of Agents → `AGENT-CONTEXT`（Ch75），handoff Ch22、76、81、82
- Agent-R → `AGENT-REFLECTION`（Ch80），handoff Ch29、66、81
- Mobile-Agent-E → `AGENT-WORKFLOW`（Ch81），handoff Ch77、78、82、72
- Demons in the Detail → `TRAIN-MOE`（Ch36），handoff Ch21、37、40
- MMVU → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch23、67
- UI-TARS → `AGENT-TOOL-CALLING`（Ch78），handoff Ch23、79～81
- Hunyuan3D 2.0 → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、25、59
- Qwen2.5-VL → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch22、25、27、66
- Qwen2.5-1M → `MODEL-LONG-CONTEXT`（Ch22），handoff Ch43、49、56
- InternLM-XComposer2.5-Reward → `TRAIN-RLHF`（Ch31），handoff Ch27、32、66
- Video Depth Anything → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch25、45、66
- Taming Teacher Forcing / MAGI → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch25、45、48
- EmbodiedEval → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch26、78、79
- Condor → `TRAIN-DATA`（Ch27），handoff Ch29、66、80
- VideoLLaMA 3 → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch22、27、66
- FilmAgent → `AGENT-WORKFLOW`（Ch81），handoff Ch24、80、82
- Test-Time Preference Optimization → `AGENT-REFLECTION`（Ch80），handoff Ch31、56、66
- Autonomy-of-Experts → `MODEL-MOE`（Ch21），handoff Ch36、49
- Pairwise RM → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch31、56、80
- Improving Video Generation with Human Feedback → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch31、34、66
- Sigma / DiffQKV → `MODEL-ATTENTION`（Ch15），handoff Ch45、49
- Image Generation with CoT → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch34、66、80
- Temporal Preference Optimization → `TRAIN-DPO`（Ch34），handoff Ch22、23、66
- O1-Pruner → `TRAIN-GRPO`（Ch33），handoff Ch34、56、66
- SRMT → `AGENT-MULTI-AGENT`（Ch82），handoff Ch25、66、77
- Fast3R → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch25、49
- Video-MMMU → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch23、27
- Debate Helps Weak-to-Strong → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch31、82
- Imagine-E → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch24、65
- Triton 3.2.0 → `INFER-TENSORRT-LLM`（Ch49），handoff Ch59、62；Weekly Only — Version Fact
- Hallucinations in Drug Discovery → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch27、71、80
- Humanity's Last Exam → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch23、67、71
- Chain-of-Retrieval Augmented Generation → `AGENT-RAG`（Ch76），handoff Ch75、81、66
- RL + Transformer / ICRL → `AGENT-REFLECTION`（Ch80），handoff Ch25、77、81
- Redundancy Principles for MLLM Benchmarks → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch65、71
- RealCritic → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch67、80
- Baichuan-Omni-1.5 → `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch24、27、66
- ARWKV → `MODEL-ATTENTION`（Ch15），handoff Ch22、28、44
- Parameters vs FLOPs / MoE Sparsity → `MODEL-MOE`（Ch21），handoff Ch36、37、49
- CodeMonkeys → `AGENT-WORKFLOW`（Ch81），handoff Ch66、78、80、82
- DeepFlow → `INFER-DYNAMO`（Ch52），handoff Ch51、55～57、63

## Recommended Action

- 44/44 `20+` 候选均完成 Full Source Review；43项 Books Pending — Integration Deferred，Triton 3.2.0为 Weekly Only version fact
- 9/9 个低分候选已完成 identity、日期、评分与拒绝理由核验；均为 Weekly Only，不进入 Books Gate

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 明确关闭。本轮只重建 Weekly discovery 与 evidence；完成的 43 个 Source Review 中42项标记
`Books Pending — Integration Deferred`，Triton 3.2.0标记 `Weekly Only — Version Fact`。旧版 `Refine / No Change` 只作为
provisional 历史输入，不代表本阶段重新作出 Books 决策。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 将旧版 3 项 seed 扩展为 53 项候选 census，完成日期、primary identity、Evidence 状态与六维评分的第一轮复核。
- 完成 DeepSeek-R1、Kimi k1.5 与 Chain of Agents 旧 packet 的 Books Deferred / Stable Node 校准。
- 新完成 Agent-R、Mobile-Agent-E、Demons in the Detail 与 MMVU 的 30 字段 Full Source Review；当前为
  44/44 `20+` complete，普通高分 `Review Pending = 0`；9/9 个低分候选也已完成 identity、日期、评分与拒绝理由核验。
- 新完成 UI-TARS、Hunyuan3D 2.0、InternLM-XComposer2.5-Reward、Video Depth Anything、MAGI 与 EmbodiedEval；三项 HTML mismatch 通过同 ID PDF/abs、官方 artifact或后续同 family 正式全文闭合，异常记录仍保留。
- 新完成 Condor、VideoLLaMA 3、FilmAgent、TPO、Autonomy-of-Experts 与 Pairwise RM；Condor/TPO 的 HTML 问题通过同 ID PDF/abs/artifact 闭合，并纠正 Condor 的初始主题描述。
- 新完成 VideoReward/Flow alignment、Sigma/DiffQKV、Image Generation with CoT、Temporal Preference Optimization、O1-Pruner 与 SRMT；保留短上下文回归、自动 verifier、synthetic negative 与 implicit latent broadcast 的证据边界。
- 新完成 Fast3R、Video-MMMU、Debate-W2SG、Imagine-E、Triton 3.2.0 与 Drug-Discovery hallucination；纠正 Debate v1 日期，Triton因缺独立feature ledger仅保留version fact。
- 关闭7项低分ledger；纠正 Panoramic Interests 的主题身份，保留 TokenVerse/GPS 的 experimental HTML mismatch，并将全部低分项定为 Weekly Only。
- W05 replay 发现 Qwen2.5-VL 1月26日 release 后，按 first-public date 回拨 W04；联读后续 technical report、
  model card 与目标/相邻章节，完成 30 字段 Source Review 后重新通过 Gate。
- W05 的1月28日 discovery 又发现 Qwen2.5-1M 的 arXiv v1 是1月26日；已回拨并全文核验 training→position
  extrapolation→sparse/chunked Prefill→DCPP/TAG 的完整演进，明确限制作者 batch-1 TTFT 证据。
- W05 的 1月27～28日 Hugging Face discovery 页面进一步回拨 HLE、CoRAG、ICRL、MLLM benchmark redundancy、
  RealCritic、Baichuan-Omni-1.5、ARWKV、MoE sparsity scaling 与 CodeMonkeys；9项均完成非模板化30字段全文审计，
  明确区分 benchmark/evaluation、representation、architecture conversion、scaling law 与 workflow state owner。
- 同一 replay 的 DeepFlow v1 也是 1月24日；已从W05回拨，完成serverless control、FlowServe、RTC/DistFlow、
  locality/PD-aware scheduling、fast scaling和受限production evidence的30字段审计。
- W05 fixed-source replay 发现 Transformers 4.48.1 的 tag 日期为1月20日；已回拨 W04，核验 release/commit/PR
  identity，并以16/30记录为兼容性补丁，不把correctness maintenance误写成长效新机制。
- W06 discovery replay 发现 MatAnyone 的 arXiv v1 为1月24日；已回拨 W04，完整核验 target-assigned
  video-matting memory flow、training/data与ablation，并以18/30保留为窄域 state-propagation case。同期
  “Fast Encoder-Based 3D” 对应 TracksTo4D 的 first-public 为2024年，未重复制造2025事件。
- W06 2月10日 discovery replay 又发现 Continuous 3D Perception / CUT3R 的 arXiv v1 为1月21日；已回拨
  W04，完成 recurrent state read/write、metric pointmaps、virtual-view readout、online evaluation、state
  compression trade-off 与 world-model owner 的全文审计，并重新通过 53/53 Gate。
- EMO2 按 arXiv v1 日期回拨 W03；Pairwise-443K 正文局部 `443M` 排版冲突按 title/abstract/artifact 的 443K 记录。
- 本次未修改 Books。

## Open Questions

- 纯 outcome reward 在开放域、不可自动验证任务中的可扩展边界仍未解决。
- long-rollout 的训练收益如何与 serving reasoning budget 联合优化，仍需跨系统证据。
- Chain of Agents 的中间摘要错误能否被可靠检测和恢复，尚未验证。
- GUI/native-agent trace 的 environment version、failure compensation 与 experience revocation 如何成为可复算 contract。
- global-batch LBL 的 collective overhead、GA buffer recovery 与 data-skew sensitivity 尚缺公开系统测量。
- W04 普通 `Review Pending = 0`；后续只在新primary evidence或跨周duplicate出现时幂等回开，不以Books尚未执行否定Weekly Gate。

## Sources

- DeepSeek-R1 — https://arxiv.org/html/2501.12948v1；https://arxiv.org/abs/2501.12948（First Public: release 2025-01-20；paper v1 2025-01-22；Accessed: 2026-08-18）
- Kimi k1.5 — https://arxiv.org/html/2501.12599v1；https://arxiv.org/abs/2501.12599（First Public: 2025-01-22；Accessed: 2026-08-18）
- Qwen2.5-VL release — https://qwenlm.github.io/blog/qwen2.5-vl/（First Public: 2025-01-26；Accessed: 2026-08-18）
- Qwen2.5-VL technical report — https://arxiv.org/html/2502.13923v1；https://arxiv.org/abs/2502.13923（Report v1: 2025-02-19；same-family verification；Accessed: 2026-08-18）
- Qwen2.5-VL model card — https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct（Release family artifact；Accessed: 2026-08-18）
- Qwen2.5-1M report — https://arxiv.org/html/2501.15383v1；https://arxiv.org/abs/2501.15383（First Public: 2025-01-26；Accessed: 2026-08-18）
- Qwen2.5-1M official release — https://qwen.ai/blog?id=qwen2.5-1m（First Public metadata: 2025-01-26；Accessed: 2026-08-18）
- Qwen2.5-1M model card — https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M（Release artifact；Accessed: 2026-08-18）
- Humanity's Last Exam — https://arxiv.org/html/2501.14249v1；https://arxiv.org/abs/2501.14249；https://lastexam.ai/（First Public: 2025-01-24；Accessed: 2026-08-18）
- Chain-of-Retrieval Augmented Generation — https://arxiv.org/html/2501.14342v1；https://arxiv.org/abs/2501.14342（First Public: 2025-01-24；Accessed: 2026-08-18）
- RL + Transformer / ICRL — https://arxiv.org/html/2501.14176v1；https://arxiv.org/abs/2501.14176（First Public: 2025-01-24；Accessed: 2026-08-18）
- Redundancy Principles for MLLM Benchmarks — https://arxiv.org/html/2501.13953v1；https://arxiv.org/abs/2501.13953（First Public: 2025-01-20；Accessed: 2026-08-18）
- RealCritic — https://arxiv.org/html/2501.14492v1；https://arxiv.org/abs/2501.14492（First Public: 2025-01-24；Accessed: 2026-08-18）
- Baichuan-Omni-1.5 — https://arxiv.org/html/2501.15368v1；https://arxiv.org/abs/2501.15368；https://github.com/baichuan-inc/Baichuan-Omni-1.5（First Public: 2025-01-26；Accessed: 2026-08-18）
- ARWKV — https://arxiv.org/html/2501.15570v1；https://arxiv.org/abs/2501.15570；https://github.com/yynil/RWKVInside（First Public: 2025-01-26；Accessed: 2026-08-18）
- Parameters vs FLOPs / MoE Sparsity — https://arxiv.org/html/2501.12370v1；https://arxiv.org/abs/2501.12370（First Public: 2025-01-21；Accessed: 2026-08-18）
- CodeMonkeys — https://arxiv.org/html/2501.14723v1；https://arxiv.org/abs/2501.14723；https://scalingintelligence.stanford.edu/pubs/codemonkeys/（First Public: 2025-01-24；Accessed: 2026-08-18）
- DeepFlow — https://arxiv.org/html/2501.14417v1；https://arxiv.org/abs/2501.14417（First Public: 2025-01-24；Accessed: 2026-08-18）
- Chain of Agents paper — https://arxiv.org/abs/2406.02818（First Public: 2024-06-04；Accessed: 2026-08-18）
- Chain of Agents Google Research follow-up — https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/（Published: 2025-01-23；Accessed: 2026-08-18）
- Agent-R — https://arxiv.org/html/2501.11425v1；https://github.com/bytedance/Agent-R（First Public: 2025-01-20；Accessed: 2026-08-18）
- Mobile-Agent-E — https://arxiv.org/html/2501.11733v1（First Public: 2025-01-20；Accessed: 2026-08-18）
- Demons in the Detail — https://arxiv.org/html/2501.11873v1（First Public: 2025-01-20；Accessed: 2026-08-18）
- MMVU — https://arxiv.org/html/2501.12380v1；https://github.com/yale-nlp/MMVU；https://huggingface.co/datasets/yale-nlp/MMVU（First Public: 2025-01-21；Accessed: 2026-08-18）
- UI-TARS — https://arxiv.org/html/2501.12326v1；https://github.com/bytedance/UI-TARS（First Public: 2025-01-21；Accessed: 2026-08-18）
- Hunyuan3D 2.0 — https://arxiv.org/html/2501.12202v1；https://github.com/Tencent-Hunyuan/Hunyuan3D-2（First Public: 2025-01-21；Accessed: 2026-08-18）
- InternLM-XComposer2.5-Reward — https://arxiv.org/html/2501.12368v1；https://github.com/InternLM/InternLM-XComposer（First Public: 2025-01-21；Accessed: 2026-08-18）
- Video Depth Anything — https://arxiv.org/abs/2501.12375；https://arxiv.org/pdf/2501.12375v1；https://github.com/DepthAnything/Video-Depth-Anything（First Public: 2025-01-21；Accessed: 2026-08-18；HTML mismatch preserved）
- Taming Teacher Forcing / MAGI — https://arxiv.org/abs/2501.12389；https://arxiv.org/pdf/2501.12389v1；https://magi-video-generation.github.io/（First Public: 2025-01-21；Accessed: 2026-08-18；HTML mismatch preserved）
- EmbodiedEval — https://arxiv.org/abs/2501.11858；https://github.com/thunlp/EmbodiedEval；https://embodiedeval.github.io/；https://openaccess.thecvf.com/content/CVPR2026W/Viscale/html/Cheng_EmbodiedEval_Evaluate_Multimodal_LLMs_as_Embodied_Agents_CVPRW_2026_paper.html（First Public: 2025-01-21；Accessed: 2026-08-18；later official text used only for same-family verification）
- Condor — https://arxiv.org/abs/2501.12273；https://arxiv.org/pdf/2501.12273；https://github.com/InternLM/Condor（First Public: 2025-01-21；Accessed: 2026-08-18；PDF used after HTML failure）
- VideoLLaMA 3 — https://arxiv.org/html/2501.13106v1；https://github.com/DAMO-NLP-SG/VideoLLaMA3（First Public: 2025-01-22；Accessed: 2026-08-18）
- FilmAgent — https://arxiv.org/html/2501.12909v1；https://github.com/HITsz-TMG/FilmAgent（First Public: 2025-01-22；Accessed: 2026-08-18）
- Test-Time Preference Optimization — https://arxiv.org/abs/2501.12895；https://arxiv.org/pdf/2501.12895v1；https://github.com/yafuly/TPO（First Public: 2025-01-22；Accessed: 2026-08-18；HTML mismatch resolved through same-ID sources）
- Autonomy-of-Experts — https://arxiv.org/html/2501.13074v1；https://arxiv.org/abs/2501.13074（First Public: 2025-01-22；Accessed: 2026-08-18）
- Pairwise RM — https://arxiv.org/html/2501.13007v1；https://github.com/THU-KEG/PairwiseRM（First Public: 2025-01-22；Accessed: 2026-08-18）
- Improving Video Generation with Human Feedback — https://arxiv.org/html/2501.13918v1；https://arxiv.org/abs/2501.13918（First Public: 2025-01-23；Accessed: 2026-08-18）
- Sigma / DiffQKV — https://arxiv.org/html/2501.13629v1；https://arxiv.org/abs/2501.13629（First Public: 2025-01-23；Accessed: 2026-08-18）
- Image Generation with CoT — https://arxiv.org/html/2501.13926v1；https://arxiv.org/abs/2501.13926（First Public: 2025-01-23；Accessed: 2026-08-18）
- Temporal Preference Optimization — https://arxiv.org/abs/2501.13919；https://arxiv.org/pdf/2501.13919v1（First Public: 2025-01-23；Accessed: 2026-08-18；HTML mismatch preserved）
- O1-Pruner — https://arxiv.org/html/2501.12570v1；https://arxiv.org/abs/2501.12570（First Public: 2025-01-22；Accessed: 2026-08-18）
- SRMT — https://arxiv.org/html/2501.13200v1；https://arxiv.org/abs/2501.13200（First Public: 2025-01-22；Accessed: 2026-08-18）
- Fast3R — https://arxiv.org/html/2501.13928v1；https://fast3r-3d.github.io/（First Public: 2025-01-23；Accessed: 2026-08-18）
- Video-MMMU — https://arxiv.org/html/2501.13826v1；https://videommmu.github.io/（First Public: 2025-01-23；Accessed: 2026-08-18）
- Debate Helps Weak-to-Strong Generalization — https://arxiv.org/html/2501.13124v1；https://arxiv.org/abs/2501.13124（First Public: 2025-01-21；Accessed: 2026-08-18）
- Imagine-E — https://arxiv.org/html/2501.13920v1；https://arxiv.org/abs/2501.13920（First Public: 2025-01-23；Accessed: 2026-08-18）
- Triton 3.2.0 — https://github.com/triton-lang/triton/releases/tag/v3.2.0；https://github.com/triton-lang/triton/pull/5618；https://github.com/triton-lang/triton/blob/main/RELEASE.md（Published: 2025-01-22；Accessed: 2026-08-18）
- Hallucinations in Drug Discovery — https://arxiv.org/html/2501.13824v1；https://arxiv.org/abs/2501.13824（First Public: 2025-01-23；Accessed: 2026-08-18）
- Reasoning Language Models: A Blueprint — https://arxiv.org/abs/2501.11223（First Public: 2025-01-20；Accessed: 2026-08-18）
- TokenVerse — https://arxiv.org/abs/2501.12224；https://token-verse.github.io/（First Public: 2025-01-21；Accessed: 2026-08-18；HTML mismatch preserved）
- PAINT / Fixing Imbalanced Attention — https://arxiv.org/html/2501.12206v1；https://arxiv.org/abs/2501.12206（First Public: 2025-01-21；Accessed: 2026-08-18）
- One-Prompt-One-Story — https://arxiv.org/html/2501.13554v1；https://arxiv.org/abs/2501.13554（First Public: 2025-01-23；Accessed: 2026-08-18）
- EchoVideo — https://arxiv.org/html/2501.13452v1；https://arxiv.org/abs/2501.13452（First Public: 2025-01-23；Accessed: 2026-08-18）
- GPS as a Control Signal — https://arxiv.org/abs/2501.12390；https://arxiv.org/pdf/2501.12390v1（First Public: 2025-01-21；Accessed: 2026-08-18；HTML mismatch preserved）
- Panoramic Interests / SCAPE — https://arxiv.org/html/2501.11900v1；https://arxiv.org/abs/2501.11900（First Public: 2025-01-21；Accessed: 2026-08-18）
- Transformers 4.48.1 — https://github.com/huggingface/transformers/releases/tag/v4.48.1（Published: 2025-01-20；Accessed: 2026-08-18）
- MatAnyone — https://arxiv.org/html/2501.14677；https://arxiv.org/abs/2501.14677（First Public: 2025-01-24；Accessed: 2026-08-18）
- Continuous 3D Perception / CUT3R — https://arxiv.org/html/2501.12387v1；https://arxiv.org/abs/2501.12387；https://cut3r.github.io/（First Public: 2025-01-21；Accessed: 2026-08-18）
