# AI Research Weekly — 2025-W08

> Coverage Window: 2025-02-17～2025-02-23
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Accessed: 2026-08-18
> Audit Status: Candidate Evidence Gate Passed — 65 owner families；64 Full Source Reviews complete；1 low-score verified；0 pending
> Historical Books Gate: Closed — Weekly evidence only

## Executive Summary

旧版周报只保留 AI co-scientist，并错误地把学术来源和工程项目写成“无候选”。本轮以
2025-02-17～2025-02-23 的 arXiv v1、官方 Blog 与 GitHub Release 重放 discovery，已经恢复
65 个本周 owner family 线索，并识别 4 个属于 W07 的 spillback。AI co-scientist、MLGym、
Qwen2.5-VL、SigLIP 2、SuperGPQA、LoRA Knowledge Capacity、Soundwave、Embedding Space Capacity、S*、Magma、RDLM、Logic-RL、SWE-Lancer、TrustGen、MMTEB、HumanUP、SongGen、Small Model Learnability Gap、Multimodal Mamba、RAD、Decomposed Reward Models、MoM、FLAG-Trader、SoFar、Craw4LLM、PC-Agent、S2R、Selective Question Answering、SafeRoute、RelaCtrl、YOLOv12、CLIPPER、Explorer、Template-Anchored Safety、NExT-Mol、video-SALMONN-o1、InfiR、LongPO、Temporal Heads、LongWriter-V、Intuitive Physics from Natural Videos、Autellix、Sailor2、Thinking Preference Optimization、HermesFlow、Atom of Thoughts、Dynamic Concepts Personalization、RealSyn、Diffusion-Sharpening、Revisiting Test-time Scaling of o1-like Models、AlphaMaze、PAFT、CoSyn、LServe、From RAG to Memory、LoRAM、Text2World、HeadInfer、AdaptiveStep、AIDE、Model-guidance、Transformers v4.49.0、Accelerate v1.4.0 与 vLLM v0.7.3 已经完成 Full Source Review；Quantum Error Correction with RL 已完成低分来源/日期/拒绝核验；MUDDFormer 已按 arXiv v1 的 2025-02-13 日期回拨 W07 并完成 Full Source Review。65/65 owner family 均有最终 disposition，W08 Candidate Evidence Gate 通过；本轮仍不进入 Books Integration。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；本轮访问日期统一为 2026-08-18。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。
- Hugging Face `2025-W08` 发现页覆盖 2 月 16～22 日，早于本 ISO week 的 2 月 16 日论文必须
  spillback 到 W07；推荐日期不替代 arXiv v1 日期。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 已完成：AI co-scientist 官方 Blog event（2025-02-19）。
- 已完成 Qwen2.5-VL technical report、SigLIP 2、Magma、Sailor2 与 HermesFlow；其余机构论文仍待逐项核验；论文身份与
  正文审计仍在第 2 组记录，不把机构署名重复计为第二个事件。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 发现页初始恢复 64 个具备唯一 arXiv 身份的候选线索；其中 2 个按 v1 日期 spillback W07，
  当前 61 个论文 family 进入 W08 的 Full Source Review / low-score verification 队列。连同 AI co-scientist
  Blog event 与 3 个 engineering release，本周共有 65 个 owner family。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本周确认 vLLM v0.7.3（2025-02-20）、Transformers v4.49.0（2025-02-17）和 Accelerate
  v1.4.0（2025-02-17）。SGLang v0.4.3 发布于 2025-02-14，归 W07，不在本周重复计分。

## Discovery and Ownership Ledger

`Status` 只表达材料处理进度；`Review Pending` 不等于已保留，也不沿用旧周报评分。最终六维
评分只在读完 primary source 后写入 Candidate Scoring。

### 模型与研究机构 / arXiv

| Candidate | Primary ID | First Public | Owner / Status |
| --- | --- | --- | --- |
| AI co-scientist | Google Research Blog | 2025-02-19 | W08 / Full Source Review Complete |
| Qwen2.5-VL Technical Report | arXiv:2502.13923 | 2025-02-19 | W08 / Full Source Review Complete |
| MLGym | arXiv:2502.14499 | 2025-02-20 | W08 / Full Source Review Complete |
| SigLIP 2 | arXiv:2502.14786 | 2025-02-20 | W08 / Full Source Review Complete |
| SuperGPQA | arXiv:2502.14739 | 2025-02-20 | W08 / Full Source Review Complete |
| LoRA Knowledge Capacity | arXiv:2502.14502 | 2025-02-20 | W08 / Full Source Review Complete |
| Soundwave | arXiv:2502.12900 | 2025-02-18 | W08 / Full Source Review Complete |
| Embedding Space Capacity | arXiv:2502.13063 | 2025-02-18 | W08 / Full Source Review Complete |
| S*: Test Time Scaling for Code Generation | arXiv:2502.14382 | 2025-02-20 | W08 / Full Source Review Complete |
| Magma | arXiv:2502.13130 | 2025-02-18 | W08 / Full Source Review Complete |
| Continuous Diffusion Model for Language Modeling | arXiv:2502.11564 | 2025-02-17 | W08 / Full Source Review Complete |
| Logic-RL | arXiv:2502.14768 | 2025-02-20 | W08 / Full Source Review Complete |
| SWE-Lancer | arXiv:2502.12115 | 2025-02-17 | W08 / Full Source Review Complete |
| Trustworthiness Guideline for Generative AI / TrustGen | arXiv:2502.14296 | 2025-02-20 | W08 / Full Source Review Complete |
| MMTEB | arXiv:2502.13595 | 2025-02-19 | W08 / Full Source Review Complete |
| Learning Getting-Up Policies for Humanoid Robots | arXiv:2502.12152 | 2025-02-17 | W08 / Full Source Review Complete |
| SongGen | arXiv:2502.13128 | 2025-02-18 | W08 / Full Source Review Complete |
| Small Models Struggle to Learn from Strong Reasoners | arXiv:2502.12143 | 2025-02-17 | W08 / Full Source Review Complete |
| Multimodal Mamba | arXiv:2502.13145 | 2025-02-18 | W08 / Full Source Review Complete |
| RAD: Training an End-to-End Driving Policy via 3DGS-based RL | arXiv:2502.13144 | 2025-02-18 | W08 / Full Source Review Complete |
| Preference PCA / Decomposed Reward Models | arXiv:2502.13131 | 2025-02-18 | W08 / Full Source Review Complete |
| Quantum Error Correction with Reinforcement Learning | arXiv:2502.14372 | 2025-02-20 | W08 / Low-score verified |
| MoM: Mixture-of-Memories | arXiv:2502.13685 | 2025-02-19 | W08 / Full Source Review Complete |
| FLAG-Trader | arXiv:2502.11433 | 2025-02-17 | W08 / Full Source Review Complete |
| SoFar | arXiv:2502.13143 | 2025-02-18 | W08 / Full Source Review Complete |
| Craw4LLM | arXiv:2502.13347 | 2025-02-19 | W08 / Full Source Review Complete |
| PC-Agent | arXiv:2502.14282 | 2025-02-20 | W08 / Full Source Review Complete |
| S2R: Teaching LLMs to Self-verify and Self-correct | arXiv:2502.12853 | 2025-02-18 | W08 / Full Source Review Complete |
| Selective Question Answering under Test-time Scaling | arXiv:2502.13962 | 2025-02-19 | W08 / Full Source Review Complete |
| SafeRoute | arXiv:2502.12464 | 2025-02-18 | W08 / Full Source Review Complete |
| RelaCtrl | arXiv:2502.14377 | 2025-02-20 | W08 / Full Source Review Complete |
| YOLOv12 | arXiv:2502.12524 | 2025-02-18 | W08 / Full Source Review Complete |
| CLIPPER | arXiv:2502.14854 | 2025-02-20 | W08 / Full Source Review Complete |
| Explorer: Web Trajectory Synthesis | arXiv:2502.11357 | 2025-02-17 | W08 / Full Source Review Complete |
| Safety Mechanisms Anchored in Template | arXiv:2502.13946 | 2025-02-19 | W08 / Full Source Review Complete |
| NExT-Mol | arXiv:2502.12638 | 2025-02-18 | W08 / Full Source Review Complete |
| video-SALMONN-o1 | arXiv:2502.11775 | 2025-02-17 | W08 / Full Source Review Complete |
| InfiR | arXiv:2502.11573 | 2025-02-17 | W08 / Full Source Review Complete |
| LongPO | arXiv:2502.13922 | 2025-02-19 | W08 / Full Source Review Complete |
| Temporal Heads | arXiv:2502.14258 | 2025-02-20 | W08 / Full Source Review Complete |
| LongWriter-V | arXiv:2502.14834 | 2025-02-20 | W08 / Full Source Review Complete |
| Intuitive Physics from Natural Videos | arXiv:2502.11831 | 2025-02-17 | W08 / Full Source Review Complete |
| Autellix | arXiv:2502.13965 | 2025-02-19 | W08 / Full Source Review Complete |
| Sailor2 | arXiv:2502.12982 | 2025-02-18 | W08 / Full Source Review Complete |
| Thinking Preference Optimization | arXiv:2502.13173 | 2025-02-17 | W08 / Full Source Review Complete |
| HermesFlow | arXiv:2502.12148 | 2025-02-17 | W08 / Full Source Review Complete；Disputed Formula |
| Atom of Thoughts | arXiv:2502.12018 | 2025-02-17 | W08 / Full Source Review Complete |
| Dynamic Concepts Personalization | arXiv:2502.14844 | 2025-02-20 | W08 / Full Source Review Complete |
| RealSyn | arXiv:2502.12513 | 2025-02-18 | W08 / Full Source Review Complete |
| Diffusion-Sharpening | arXiv:2502.12146 | 2025-02-17 | W08 / Full Source Review Complete；Disputed Objective / Efficiency Contract |
| Revisiting Test-time Scaling of o1-like Models | arXiv:2502.12215 | 2025-02-17 | W08 / Full Source Review Complete |
| AlphaMaze / GRPO | arXiv:2502.14669 | 2025-02-20 | W08 / Full Source Review Complete；Disputed Result Contract |
| PAFT | arXiv:2502.12859 | 2025-02-18 | W08 / Full Source Review Complete |
| Scaling Text-Rich Image Understanding | arXiv:2502.14846 | 2025-02-20 | W08 / Full Source Review Complete |
| LServe | arXiv:2502.14866 | 2025-02-20 | W08 / Full Source Review Complete |
| From RAG to Memory | arXiv:2502.14802 | 2025-02-20 | W08 / Full Source Review Complete |
| Train Small, Infer Large / LoRAM | arXiv:2502.13533 | 2025-02-19 | W08 / Full Source Review Complete；Disputed Recovery Contract |
| Text2World | arXiv:2502.13092 | 2025-02-18 | W08 / Full Source Review Complete |
| HeadInfer | arXiv:2502.12574 | 2025-02-18 | W08 / Full Source Review Complete |
| AdaptiveStep | arXiv:2502.13943 | 2025-02-19 | W08 / Full Source Review Complete；Disputed Efficiency / Label Contract |
| AIDE | arXiv:2502.13138 | 2025-02-18 | W08 paper event / Full Source Review Complete；family first public 2024-04-04 |
| Diffusion Models without Classifier-free Guidance / Model-guidance | arXiv:2502.12154 | 2025-02-17 | W08 / Full Source Review Complete；Disputed Scope Claim |

### Engineering Releases

| Candidate | Primary ID | First Public | Owner / Status |
| --- | --- | --- | --- |
| Transformers v4.49.0 | GitHub tag `v4.49.0` | 2025-02-17 | W08 / Full Source Review Complete |
| Accelerate v1.4.0 | GitHub tag `v1.4.0` | 2025-02-17 | W08 / Full Source Review Complete |
| vLLM v0.7.3 | GitHub tag `v0.7.3` | 2025-02-20 | W08 / Full Source Review Complete |

### Spillback / Deduplication

| Candidate | Primary ID | First Public | Disposition |
| --- | --- | --- | --- |
| You Do Not Fully Utilize Transformer Representation Capacity | arXiv:2502.09245 | 2025-02-13 | Move to W07；not counted in W08 |
| OctoTools | arXiv:2502.11271 | 2025-02-16 | Move to W07；not counted in W08 |
| MUDDFormer | arXiv:2502.12170 | 2025-02-13 | Move to W07；Full Source Review complete；not counted in W08 |
| SGLang v0.4.3 | GitHub tag `v0.4.3` | 2025-02-14 | W07 engineering event；not counted in W08 |

## Candidate Scoring

当前表只列已经通过完整证据核验的候选；其余条目不得在只读摘要的情况下写入最终分数。

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| AI co-scientist | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Full Source Review Complete；Books Pending |
| MLGym | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete；Books Pending |
| Qwen2.5-VL Technical Report | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete；Books Pending |
| SigLIP 2 | 4 | 5 | 4 | 5 | 4 | 4 | 26/30 | Full Source Review Complete；Books Pending |
| SuperGPQA | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete；Books Pending |
| LoRA Knowledge Capacity | 3 | 4 | 3 | 4 | 5 | 4 | 23/30 | Full Source Review Complete；Books Pending |
| Soundwave | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete；Books Pending |
| Embedding Space Capacity | 5 | 4 | 2 | 4 | 5 | 5 | 25/30 | Full Source Review Complete；Books Pending |
| S*: Test Time Scaling for Code Generation | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete；Books Pending |
| Magma | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete；Books Pending |
| Continuous Diffusion Model for Language Modeling | 5 | 4 | 3 | 4 | 5 | 4 | 25/30 | Full Source Review Complete；Books Pending |
| Logic-RL | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review Complete；Books Pending |
| SWE-Lancer | 4 | 5 | 4 | 5 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| TrustGen | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| MMTEB | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| HumanUP | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| SongGen | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Small Model Learnability Gap | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Multimodal Mamba | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete；Books Pending |
| RAD: 3DGS-based Reinforcement Learning for End-to-End Driving | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| Decomposed Reward Models / Preference PCA | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Low-weight Quantum Error-Correcting Codes with RL | 5 | 2 | 3 | 4 | 1 | 3 | 18/30 | Low-score verified；Weekly Only |
| MoM: Mixture-of-Memories | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete；Books Pending |
| FLAG-Trader | 3 | 4 | 3 | 4 | 5 | 4 | 23/30 | Full Source Review Complete；Books Pending |
| SoFar | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| Craw4LLM | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete；Books Pending |
| PC-Agent | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Source Review Complete；Books Pending |
| S2R: Self-verification and Self-correction via RL | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Selective Question Answering under Test-time Scaling | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| SafeRoute | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| RelaCtrl | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Source Review Complete；Books Pending |
| YOLOv12 | 4 | 4 | 5 | 3 | 4 | 4 | 24/30 | Full Source Review Complete；Books Pending |
| CLIPPER | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Explorer: Web Trajectory Synthesis | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| Template-Anchored Safety | 5 | 5 | 3 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| NExT-Mol | 5 | 4 | 3 | 4 | 4 | 5 | 25/30 | Full Source Review Complete；Books Pending |
| video-SALMONN-o1 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Source Review Complete；Books Pending |
| InfiR | 3 | 5 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| LongPO | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| Temporal Heads | 4 | 3 | 3 | 4 | 5 | 5 | 24/30 | Full Source Review Complete；Books Pending |
| LongWriter-V | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| Intuitive Physics from Natural Videos | 5 | 4 | 3 | 4 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Autellix | 5 | 5 | 5 | 3 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| Sailor2 | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| Thinking Preference Optimization | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete；Books Pending |
| HermesFlow | 5 | 4 | 3 | 3 | 5 | 4 | 24/30 | Full Source Review Complete；Disputed；Books Frozen |
| Atom of Thoughts | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Full Source Review Complete；Books Pending |
| Dynamic Concepts Personalization | 5 | 4 | 3 | 3 | 5 | 5 | 25/30 | Full Source Review Complete；Books Pending |
| RealSyn | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| Diffusion-Sharpening | 5 | 4 | 3 | 2 | 5 | 4 | 23/30 | Full Source Review Complete；Disputed；Books Frozen |
| Revisiting Test-time Scaling of o1-like Models | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Full Source Review Complete；Books Pending |
| AlphaMaze / GRPO | 3 | 3 | 3 | 1 | 4 | 4 | 18/30 | Full Source Review Complete；Disputed；Weekly Only / Books Frozen |
| PAFT | 3 | 4 | 5 | 3 | 5 | 4 | 24/30 | Full Source Review Complete；Books Pending |
| CoSyn / Scaling Text-Rich Image Understanding | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| LServe | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| From RAG to Memory / HippoRAG 2 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete；Books Pending |
| Train Small, Infer Large / LoRAM | 5 | 4 | 3 | 2 | 5 | 5 | 24/30 | Full Source Review Complete；Disputed；Books Frozen |
| Text2World | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| HeadInfer | 5 | 5 | 4 | 3 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending |
| AdaptiveStep | 4 | 4 | 4 | 2 | 5 | 5 | 24/30 | Full Source Review Complete；Disputed；Books Frozen |
| AIDE | 4 | 5 | 5 | 3 | 5 | 5 | 27/30 | Full Source Review Complete；Books Pending — No Change Candidate |
| Diffusion Models without Classifier-free Guidance / Model-guidance | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Full Source Review Complete；Disputed Scope Claim；Books Frozen |
| Transformers v4.49.0 | 2 | 4 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete；Weekly Only — Version/Integration Fact |
| Accelerate v1.4.0 | 2 | 4 | 4 | 5 | 5 | 3 | 23/30 | Full Source Review Complete；Books Pending — No Change Candidate |
| vLLM v0.7.3 | 3 | 5 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete；Books Pending — No Change Candidate |

### Deep Analysis 1 — AI co-scientist

- First Public: 2025-02-19
- Status: Google Research official prototype
- Primary Source: https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- Evolution Relationship: Layering / Dependency

#### Why

科学发现任务把 agent 的目标从生成答案扩展到提出、比较、演化和验证假设。

#### Principle and Mechanism

官方原型使用多 agent 角色和 tournament-style comparison 迭代研究提案，并有人类和实验反馈。

#### Trade-off and Evidence Boundary

更长 workflow 增加探索覆盖，但 evaluator bias、实验成本、领域安全与责任归属成为系统约束。

#### Connection and Evolution

知识树位置：第 62、74～78 章。Worth Watching；不依据个案结果外推自治科研能力。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Low-score Verification Ledger

| Candidate | First-public | Primary Source | Score | Final Disposition |
| --- | --- | --- | ---: | --- |
| Discovering highly efficient low-weight quantum error-correcting codes with reinforcement learning | 2025-02-20 | https://arxiv.org/abs/2502.14372 | 18/30 | Identity/date/abstract and DBLP metadata verified；novel domain RL search, but quantum-code construction is outside the current AI System knowledge tree and adds no reusable model/training/runtime/platform mechanism beyond already-owned RL search principles。Weekly Only；no Books owner。 |

## Full Source Review

### AI co-scientist

- **Candidate / Week / Score:** AI co-scientist / 2025-W08 / 22/30。
- **Source Family ID:** `google-ai-co-scientist-workflow`。
- **Source Type:** Google Research official Blog + arXiv/Nature author paper + extensive supplementary methods。
- **First-public Date / Revision History:** Blog 2025-02-19；paper v1 2025-02-26、v2 2026-06-29，后成为
  2026 Nature paper。W08 归档的是 Blog event；本轮按 v2 157-page author manuscript 核验，同时明确其中
  Gemini 2.5/3、GPT-5.4 等 2026 revision 内容不是 2025 已知事实。
- **Direct Primary Sources:** https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/；
  https://arxiv.org/abs/2502.18864；https://arxiv.org/pdf/2502.18864。
- **Related Primary Sources:** Gemini technical reports 定义 base-model capability；paper 所引 wet-lab protocols、
  databases 与 benchmark papers 定义验证环境，不公开 production deployment。
- **Access and Verification Status:** Verified；Blog、42-page main paper 与 115-page supplement 可访问。源码、
  scheduler implementation 与 production topology未公开，相关细节按 `Not Disclosed` 处理。
- **Full-read Coverage:** 已读 metadata/revisions、Abstract/Introduction/Related Work、architecture/Methods、六类
  agents、task queue/context memory、Elo tournament、human interaction、tools、203/15/11-goal evaluations、
  wet-lab studies、agent ablations、limitations/discussion、safety/red-team、pseudocode/prompts 与相关 supplement。
- **Original Problem:** scientific ideation 不只是一次 retrieval+answer，而是长期生成、查新、批判、比较、
  合并、实验设计与验证；单模型一次调用难维持 diverse hypotheses、全局 tournament state 与来源新颖性。
- **Why the Previous Design Was Reasonable:** 人类 scientist/peer review 对 novelty、feasibility 与实验风险有
  domain authority；单 agent/search pipeline 状态少、容易审计；brute-force parallel sampling 在有强 verifier
  的闭域任务可简单扩展。
- **Changed Constraint:** 希望用可扩展 test-time compute 探索开放 hypothesis space，并允许 expert 持续
  修改目标/约束；需要异步 workers、持久状态和评审反馈，而不是仅延长单条 CoT。
- **Mechanism:** Supervisor 解析 research goal/config，维护 asynchronous task queue并动态分配 Generation、
  Reflection、Ranking、Proximity、Evolution、Meta-review workers；pairwise debate 形成 Elo tournament；
  proximity graph 去重/聚类；Meta-review 的全局反馈追加到后续 prompts；persistent context memory 保存系统/
  agent state 与 summary statistics，支持长时运行和 restart。
- **State Ownership:** scientist 拥有 goal、constraints 与最终 selection；Supervisor 拥有 authoritative queue、
  allocation/terminal decision 与 progress statistics；specialized agents产生 hypotheses/reviews；tournament 拥有
  pairwise/Elo state；context memory持久化 agent/system state。paper 未披露 transaction、lease/idempotency schema。
- **Control Flow / Data Flow:** expert goal/documents→plan configuration→Supervisor enqueue→Generation/search→
  Reflection novelty/correctness review→Ranking debate/Elo→Proximity dedupe/cluster→Evolution refine/combine→
  Meta-review aggregate feedback→statistics/context checkpoint→再次 weighted scheduling→expert review→wet-lab。
- **Implementation Details:** Python 3.11.7；all agents 基于 Gemini 2.0 in original study；workers 通过 customized
  prompts/strategies 与 web/database/AlphaFold-like tools工作；Supervisor定期写 context memory并根据 queue/
  tournament stats调整 agent sampling。durable store、exact queue、retry与compute scheduler Not Disclosed。
- **Evaluation Contract:** 203 research goals 的 auto-Elo trajectory；15 expert-curated biomedical goals 与 frontier
  models/experts比较；11 goals blinded expert review；GPQA 用于 Elo concordance；三个 biomedical validations，
  包括从 2,300 approved drugs×34 cancers 搜索、expert筛选和 AML cell-line assays。
- **Baselines / Ablations / Sensitivity / Overhead:** base LLMs/human best guesses；Generation strategies、Reflection with/
  without search、simple vs debate ranking、Evolution、Proximity、Meta-review ablations。search 将已发表 ideas 的
  auto-novelty score从 6.14 降至2.38；多数指标仍由 system/LLM auto-evaluation，不能视为外部 ground truth。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base Gemini 2.0 variants；hardware、
  precision、worker concurrency、token/compute budget与tail SLO Not Disclosed。专家 setup <1h、final review约3h
  是三个案例的人工时间，不是端到端 system SLO。
- **What the Evidence Actually Proves:** author system展示了显式 role decomposition、async queue、persistent
  context 与 tournament feedback 的可运行组合；ablation 支持 external search 对 novelty grounding 和部分
  specialized agents 对作者指标有贡献；少量 expert-in-loop wet-lab提供“值得继续验证”的初步证据。
- **What It Does Not Prove:** 不证明系统自治完成科学发现、不证明 Elo 等于真实 hypothesis quality、不证明
  三个 biomedical cases 可跨领域外推，也不证明 multi-agent 本身优于等计算的强 single-agent baseline；
  in-vitro viability 不是 pre-clinical/clinical validation。
- **Limitations / Threats to Validity:** open-access literature遗漏付费 prior art 与 negative results；来源本身
  可错误/不可复现；模型 hallucination；Elo/self-judge circularity、small expert samples、revision混入更新模型；
  wet-lab 选择有人类筛选。paper明确验证仍 preliminary，可能 homogenize directions/加剧 reproducibility crisis。
- **Trade-offs / New Failure Modes:** 增加 exploration 与 restartability，却引入 queue starvation、duplicate
  work、stale tournament scores、Elo gaming/evaluator bias、context contamination、source poisoning、budget/
  stopping policy、artifact provenance、unsafe intermediate hypotheses 与责任边界；更多 agents 不等于独立证据。
- **Where the Previous Design Still Applies:** 单 agent+human review适合窄任务/低预算；确定性 pipeline适合
  regulated assays；人类 literature review/peer review 与 staged experiment仍是 epistemic gate，不可被 Elo 替代。
- **Evolution Relationship:** `Layering / Dependency`：long-running workflow 将 model/search/evaluator/memory/
  physical validation 组合；不是 frontier model capability 的单独升级，也不是 scientist replacement。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Current Ch81；Legacy Ch77）主 owner；`AGENT-MEMORY`、
  `AGENT-PLANNING`、`AGENT-MULTI-AGENT`、`PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`
  通过 handoff 连接。
- **Target and Adjacent Chapters Read:** 已读 Current Ch66、Ch72、Ch77、Ch79、Ch81～82，并最终核对 Ch81 对
  scientific workflow、physical feedback、state/termination/evaluator risk 的描述。
- **Existing Coverage:** Current Ch81 已覆盖 durable workflow、human/physical gate 与 scientific-discovery 案例；
  本轮仅确认 owner 与证据边界，不重新判断现有 Books 正文是否应保留或修改。
- **Integration Decision:** `Books Pending — Integration Deferred`；本任务只完成 Weekly evidence，不沿用旧版
  `No Change` 结论作为新 Books Gate 结果。
- **Changed Files or Rejection Reason:** Weekly evidence only；未修改 Books。
- **Open Questions:** queue/lease/retry/idempotency contract、Elo calibration/independent verifier、claim-level
  provenance、safe intermediate-state policy、compute accounting、negative-result access与跨领域 replication。

### MLGym

- **Candidate / Week / Score:** MLGym: A New Framework and Benchmark for Advancing AI Research Agents / 2025-W08 / 25/30。
- **Source Family ID:** `meta-mlgym-research-agent-evaluation`。
- **Source Type:** arXiv v1 research paper + author repository / benchmark artifact。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 12:28 UTC；arXiv submission history
  currently lists only v1。Current HTML carries a later author-date string, so event-time claims are locked to v1 metadata
  and v1 paper rather than inferred from current repository state。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14499；https://arxiv.org/html/2502.14499；
  https://github.com/facebookresearch/MLGym。
- **Related Primary Sources:** paper-referenced SWE-Agent supplies the default harness lineage；the author repository
  publishes configs、tasks、results、trajectories and container setup。Later repository changes are implementation
  evolution, not evidence of the 2025 experiment unless tied to an event-time commit。
- **Access and Verification Status:** Verified；v1 HTML/PDF structure and public repository are accessible。Provider-side
  model serving topology, exact proprietary model weights and complete environment images used for every original run are
  Not Disclosed。
- **Full-read Coverage:** read metadata、Introduction/capability levels、Related Work、framework architecture、Agent/
  Environment/Dataset/Task/Tool interfaces、13 benchmark tasks、experimental setup、AUP metric、results、cost、failure
  and action analysis、Discussion/Limitations、Ethics、Appendix compute/failure/memory analysis、prompts and repository
  structure / installation contract。
- **Original Problem:** research-agent evaluation often changes model, scaffold, environment and task simultaneously, then
  collapses heterogeneous outcomes into incomparable scores；open-ended ML work also produces weights、code、policies or
  strategies rather than a single answer artifact。
- **Why the Previous Design Was Reasonable:** code benchmarks and Kaggle-like tasks offer cheap deterministic checks,
  fixed submission formats and clear leaderboards；single-task scores are easy to reproduce and diagnose when the output
  schema and verifier are uniform。
- **Changed Constraint:** an AI research workflow must edit code, run experiments, consume data, train models and submit
  task-specific artifacts across CV、NLP、RL、game theory and data science。Evaluation therefore needs a common control
  environment while preserving per-task verifier and resource contracts。
- **Mechanism:** MLGym exposes Agent、Environment、Dataset and Task abstractions through a Gymnasium-style shell loop。
  Each task config binds datasets、read-only evaluation scripts、dependencies、starter code、training timeout and expected
  artifact；a SWE-Agent-derived ReAct harness receives typed tool documentation, acts one command per step, can validate
  repeatedly and terminates through submit。AUP performance profiles normalize heterogeneous task metrics without claiming
  that their raw units are interchangeable。
- **State Ownership:** the environment owns workspace, permissions, command observations, step/cost/time limits and terminal
  status；task config owns dataset/evaluator/artifact schema；agent owns proposed edits and commands；validate/submit scripts
  own authoritative score production。The optional memory module stores experiment notes and embeddings, but does not own
  final task success。
- **Control Flow / Data Flow:** task config + dataset + starter artifact → isolated non-root container workspace → prompt /
  action history → one shell/tool action → environment observation → optional memory write/read or literature lookup →
  validate against read-only evaluator → iterate under step/cost/timeout budget → submit artifact → per-task metric → AUP
  aggregation and trajectory/failure analysis。
- **Implementation Details:** task definitions are configuration-driven；local datasets are copied read-only；evaluation
  scripts are read-only；Docker/Podman isolates execution；tooling includes search/view/edit、Python/Bash、validation,
  submission, Semantic Scholar lookup, PDF parsing and a JSON+embedding memory with top-k cosine retrieval。Experiments use
  the SWE-Agent tools and validation command；current repository documents Python 3.11 and GPU-capable containers, but
  current main is not treated as the exact event-time artifact。
- **Evaluation Contract:** 13 open-ended tasks span data science、3-SAT、iterated games、CV、NLP and RL；five models are
  run through the same harness, with four attempts/seeds where reported。The paper distinguishes Best Attempt from Best
  Submission, per-task raw metrics, AUP performance profiles, API cost, termination categories, completion and action mix。
- **Baselines / Ablations / Sensitivity / Overhead:** each task ships a domain baseline/starter, including simple CNNs,
  NanoGPT, PPO and game strategies。Models are o1-preview、Gemini-1.5-Pro、Claude-3.5-Sonnet-20241022、
  Llama-3.1-405B-Instruct and GPT-4o；all except o1 use temperature 0 and top-p 0.95。The study compares model outcomes and
  memory traces but does not provide an equal-compute scaffold ablation or prove the AUP ranking is invariant to task mix,
  normalization or budget。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Llama-3.1-405B-Instruct was served from an
  FP8 open-weight checkpoint on Meta internal servers；other models use provider APIs。Per-task compute limits and average
  runtimes appear in the appendix；commands have a 1,800-second ceiling and runs expose a 50-step prompt budget in the
  published configuration。Exact accelerator types for all tasks、provider hardware、batching/concurrency and production
  SLO are Not Disclosed；API price is historical experiment cost, not a stable systems benchmark。
- **What the Evidence Actually Proves:** a common sandbox can host heterogeneous, executable research artifacts while
  preserving task-specific validation；the published trajectories show frontier models often improve supplied baselines,
  mainly through implementation and hyperparameter work。Failure analysis demonstrates that artifact-format/evaluation
  errors, cost limits, context exhaustion and runtime faults are part of measured capability rather than removable noise。
- **What It Does Not Prove:** it does not show autonomous scientific discovery, novel algorithms or Level-2+ research
  capability；the authors explicitly observe mostly baseline improvement。It does not isolate model capability from the
  chosen SWE-Agent harness, task suite, evaluator access or repeated validation, and does not establish a universal model
  ranking or deployment-safety conclusion。
- **Limitations / Threats to Validity:** only 13 ML-centered tasks and five 2024-era models；heterogeneous metrics and
  normalization choices affect aggregate ranking；agents can repeatedly query the test evaluator and, in game tasks, inspect
  opponent strategies；proprietary model/API drift and historical pricing reduce later reproducibility；novelty is not
  directly measured, some runs fail to produce valid artifacts, and current repository changes may diverge from v1 runs。
- **Trade-offs / New Failure Modes:** standardized isolation and typed artifacts improve comparability but introduce
  container/image drift、task-config mistakes、evaluator leakage/gaming、permission bugs、invalid submission schemas,
  expensive repeated validation and aggregate-metric sensitivity。Persistent research memory preserves good configurations
  but adds stale or misleading notes, retrieval errors and provenance requirements。
- **Where the Previous Design Still Applies:** deterministic unit tests and fixed CSV/code benchmarks remain preferable for
  narrow tasks with one artifact schema；human review remains necessary for novelty, scientific validity and safety；a single
  task metric is more interpretable than cross-task AUP when only one workload matters。
- **Evolution Relationship:** `Layering / Dependency`：extends code-agent sandboxes into an executable research-evaluation
  environment and adds heterogeneous artifact / metric contracts；it does not replace model-only or task-specific evaluation。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）canonical owner；`AGENT-WORKFLOW`
  and `AGENT-MEMORY` own durable execution and experiment-note state；`AGENT-MULTI-AGENT` is not implied by the benchmark。
- **Target and Adjacent Chapters Read:** read Ch66 evaluation contract and Agent Ch80～82 boundary；verified that MLGym
  belongs to executable Agent evaluation rather than Workflow or Multi-Agent mechanism ownership。
- **Existing Coverage:** Ch66 already separates model、system、runtime and Agent/outcome evaluation and treats harness,
  tools, environment, budget and trajectory as subject identity。MLGym supplies a strong source packet for this claim but
  the present Weekly-only phase does not decide whether the chapter needs text changes。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added Weekly score, exact review packet, event-time revision boundary and owner；no Books change。
- **Open Questions:** which event-time repository commit/container digest reproduces v1；how much repeated validate access
  leaks test signal；whether AUP is stable under task reweighting and budget normalization；how to version evaluator artifacts,
  provider adapters, GPU allocation and research-memory provenance across benchmark revisions。

### Qwen2.5-VL Technical Report

- **Candidate / Week / Score:** Qwen2.5-VL Technical Report / 2025-W08 / 27/30。
- **Source Family ID:** `qwen2-5-vl-native-resolution-temporal-representation`。
- **Source Type:** author technical report + official model card + framework release integration。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 18:00 UTC；submission history lists only v1。
  Transformers v4.49.0 added its model integration on 2025-02-17, but the framework event is recorded separately and
  cannot move the technical report before its first-public date。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13923；https://arxiv.org/html/2502.13923；
  https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct；https://github.com/huggingface/transformers/releases/tag/v4.49.0。
- **Related Primary Sources:** Qwen2-VL defines the predecessor MRoPE/dynamic-resolution contract；the published
  3B/7B/72B model artifacts expose architecture and processor configuration。The old Qwen2.5-VL GitHub path currently
  redirects to Qwen3-VL, so it is not used as event-time implementation evidence without a pinned commit。
- **Access and Verification Status:** Verified；v1 report and official 7B model card are readable。Training code, data
  manifests, exact hardware/topology, per-stage optimizer schedule and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read metadata、Introduction/related architecture lineage、ViT/merger/LLM architecture、window
  attention、native dynamic spatial resolution、dynamic FPS and absolute-time MRoPE、pretraining data and three stages、
  SFT/DPO post-training、rejection-sampling filter、all reported image/document/grounding/video/GUI evaluations、Conclusion,
  model-card processor/runtime requirements and framework-release integration。No dedicated ablation or limitations section exists。
- **Original Problem:** fixed image resizing distorts spatial scale and creates uniform token budgets, while frame-index-only
  video position loses real elapsed time when FPS varies；full ViT attention makes native high resolution quadratically costly,
  and loosely coupled perception outputs are insufficient for fine-grained grounding and GUI action proposals。
- **Why the Previous Design Was Reasonable:** fixed-resolution encoders produce regular batches, predictable FLOPs and
  stable pretrained artifacts；frame order is adequate when sampling rate is fixed；full attention preserves global visual
  interaction；relative coordinates simplify augmentation and cross-resolution normalization。
- **Changed Constraint:** one model must accept images with different aspect ratios, long videos with variable sampling,
  documents, spatial grounding and UI trajectories while preserving a shared language decoder and supporting 3B～72B
  deployment points。Token count, timing and modality identity therefore become variable runtime state rather than static input shape。
- **Mechanism:** a from-scratch ViT uses 14×14 patches, groups adjacent four patch features through a two-layer MLP merger,
  and applies window attention in most blocks with four full-attention layers。Images map native dimensions to variable token
  sequences；videos group two frames per temporal patch, train with dynamic FPS, and align MRoPE temporal IDs to absolute
  timestamps while height/width retain spatial IDs。The resulting visual sequence feeds a Qwen2.5 decoder。
- **State Ownership:** processor owns resize-to-multiple-of-28, pixel/token limits, FPS and timestamp metadata；ViT owns
  spatial/temporal feature extraction；merger owns 4-patch compression and projection；MRoPE IDs own coordinate/time identity；
  LLM decoder owns causal language/action-token generation。The model does not own real device state merely because it emits
  GUI actions。
- **Control Flow / Data Flow:** image/video + native dimensions/FPS → processor chooses pixels/frames → 2D/3D patches →
  window/full-attention ViT → four-patch merger → variable-length visual tokens with temporal/height/width position IDs →
  Qwen2.5 decoder + text context → language, structured coordinates or function-like action proposal。Serving then must account
  for modality encode cost and expanded sequence length before admission。
- **Implementation Details:** ViT hidden size 1,280 with 32 layers/16 heads; window size 112 and full-attention blocks
  7/15/23/31；3B/7B/72B decoders differ in hidden/layer/KV-head dimensions。Training uses CLIP-style ViT initialization,
  vision-language alignment and end-to-end stages；reported pretraining progresses through visual、multimodal and 32K
  long-context stages totaling 4.1T tokens。Post-training freezes ViT and performs SFT then DPO；reasoning data uses
  ground-truth rejection sampling plus code-switch/length/repetition and visual-grounding filters。
- **Evaluation Contract:** author benchmarks cover general VQA、OCR/document parsing、spatial grounding/counting、video
  understanding/localization、pure text and GUI Agent tasks across three model sizes and multiple proprietary/open baselines。
  Video evaluation caps each sample at 768 frames and 24,576 video tokens；online GUI success and offline exact-match/grounding
  metrics are separate evidence planes。
- **Baselines / Ablations / Sensitivity / Overhead:** comparison includes Qwen2-VL predecessor, InternVL2.5, Molmo,
  Grounding-DINO and provider models。The report gives broad benchmark tables but no controlled ablation isolating window
  attention, absolute-time MRoPE, data scale, filtering or post-training, and no end-to-end latency/memory overhead comparison。
  Some GUI baselines receive Set-of-Mark while Qwen does not, so those rows are not a pure architecture comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes are 3B/7B/72B；training token stages
  use 8,192/8,192/32,768 sequence lengths；video evaluation caps 768 frames / 24,576 visual tokens。Training/inference
  accelerator topology、precision、batch/concurrency、TTFT/TPOT and production SLO are Not Disclosed。The model card
  suggests FlashAttention 2 and lets users bound visual tokens, but that is operational guidance rather than benchmark proof。
- **What the Evidence Actually Proves:** the report specifies a coherent representation contract that combines variable
  spatial resolution, variable video sampling and absolute time inside shared multimodal position IDs；public artifacts support
  implementation and serving integration。Author evaluations show the resulting family is competitive on the listed tasks
  under their protocols and preserves substantial text capability。
- **What It Does Not Prove:** it does not establish that window attention or absolute-time MRoPE individually causes the
  reported gains, that “hours-long video” means all evidence is retained, or that visual grounding equals safe computer use。
  It does not prove lower end-to-end cost, production goodput, cross-hardware behavior, independent benchmark reproduction or
  universal superiority over fixed-resolution/projector architectures。
- **Limitations / Threats to Validity:** no explicit limitations/ablation section；large private/synthetic data and internal
  filtering prevent full reproduction；benchmark contamination and model-specific prompting are not fully resolved；variable
  visual-token budgets complicate fairness；absolute timestamp encoding still depends on correct FPS metadata and sampling,
  while 768-frame caps can discard events in long video。
- **Trade-offs / New Failure Modes:** native resolution reduces distortion but creates token-count variance, load imbalance,
  memory/admission uncertainty and resolution-dependent cost；window attention lowers local compute but risks missed global
  relations between full-attention refresh layers；absolute-time MRoPE adds clock/FPS metadata dependence；structured action
  outputs add coordinate calibration, parser and environment-state failure modes。Frozen-ViT post-training limits catastrophic
  visual drift but may cap task-specific perception adaptation。
- **Where the Previous Design Still Applies:** fixed-resolution/fixed-FPS pipelines remain preferable for regular batching,
  edge predictability and calibrated sensors；full attention is appropriate for short visual sequences requiring exact global
  interaction；specialist OCR/detector/controller stacks remain more auditable where perception or physical actions carry high risk。
- **Evolution Relationship:** `Direct Evolution` from Qwen2-VL representation: preserves encoder→merger→decoder layering,
  then changes temporal identity and ViT execution to support variable-resolution/variable-FPS workloads；`Layering / Dependency`
  toward Agent use because action execution still belongs to a separate environment/workflow contract。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；new node）canonical owner；`MODEL-LONG-CONTEXT`
  owns sequence-capacity implications, `INFER-REQUEST-LIFECYCLE` owns serving admission, and `AGENT-TOOL-CALLING` /
  `MULTIMODAL-EMBODIED-VLA` own action execution boundaries。
- **Target and Adjacent Chapters Read:** read Ch22 long-context boundary、Ch23 representation contract and Ch24 generation
  handoff；verified that this source changes input representation/position identity rather than generative factorization。
- **Existing Coverage:** Ch23 already explains modality/coordinate/artifact identity, dynamic token expansion, fusion and
  admission handoff。Qwen2.5-VL provides a bounded case for native resolution plus absolute-time identity；this Weekly phase
  does not decide whether existing prose should be changed。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added Weekly score, full packet, model-card/runtime boundary and event-time owner；no Books change。
- **Open Questions:** exact data lineage and filtering rates；per-component ablations；training/inference hardware and energy；
  robustness to wrong/missing FPS、frame drops and reordered clips；cache identity across pixel/FPS settings；independent long-video
  evidence retrieval; safe GUI action verification and real-world failure recovery。

### SigLIP 2

- **Candidate / Week / Score:** SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding,
  Localization, and Dense Features / 2025-W08 / 26/30。
- **Source Family ID:** `google-siglip2-multilingual-dense-representation`。
- **Source Type:** arXiv v1 research paper + official implementation/checkpoint artifact。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 18:08 UTC；submission history currently lists
  only v1。This Weekly records the paper event and does not infer an earlier event from later repository state。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14786；https://arxiv.org/html/2502.14786；
  https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md。
- **Related Primary Sources:** original SigLIP defines the predecessor sigmoid image-text objective；LocCa、DINOv2 and
  masked-image/self-distillation work define reused components。The official big_vision page publishes fixed-resolution and
  NaFlex checkpoints plus their preprocessing/implementation requirements。
- **Access and Verification Status:** Verified；v1 HTML and official checkpoint/implementation page are accessible。
  WebLI examples, exact data curation implementation, full training artifacts and event-time repository commit are Not Disclosed。
- **Full-read Coverage:** read metadata/history、Abstract、Introduction、Related Work、architecture and tokenizer、data
  mixture、two-stage training recipe、captioning/localization decoder objectives、self-distillation、masked prediction、
  active curation/distillation、NaFlex、all classification/retrieval/dense/localization/VLM/multilingual/fairness evaluations、
  Appendix implementation/data/evaluation details、Conclusion and official checkpoint compatibility notes。No dedicated
  limitations section or component-complete ablation exists。
- **Original Problem:** the original global image-text contrastive objective learns strong retrieval/classification features
  but supplies weak supervision for local regions, dense prediction and multilingual/culturally diverse inputs；fixed square
  resizing also discards native aspect ratio and ties one checkpoint to a narrow resolution contract。
- **Why the Previous Design Was Reasonable:** a two-tower encoder with one global image embedding supports efficient
  retrieval, regular tensor shapes and reusable frozen features；fixed resolution makes batching and positional embeddings
  predictable；a single sigmoid pairwise objective avoids the global softmax coupling of conventional contrastive learning。
- **Changed Constraint:** one representation family is expected to serve global retrieval, dense/localized perception,
  multilingual text and variable-aspect-ratio documents/images across model and token budgets。Global correspondence alone
  no longer supplies all required supervision, while production consumers still need backward-compatible encoder artifacts。
- **Mechanism:** SigLIP 2 retains image/text towers and the sigmoid image-text objective, then jointly adds an auxiliary
  decoder trained for captioning, referring-expression prediction and grounded captioning。At roughly 80% of training it
  switches to a second stage that adds EMA-teacher local/global self-distillation and 50% masked-patch prediction。Online
  data curation and small-model distillation alter the training distribution；NaFlex variants preserve native aspect ratio
  and train one checkpoint across variable patch-sequence lengths。
- **State Ownership:** the data pipeline owns language mixture, active curation and image/text pairing；vision/text towers
  own reusable embeddings；the auxiliary decoder owns training-only caption/localization supervision and is not part of the
  released encoder contract；EMA teacher owns slowly updated target state；NaFlex preprocessing owns patch sequence length,
  padding and aspect-ratio identity；downstream consumers own task heads and operating thresholds。
- **Control Flow / Data Flow:** WebLI image-text pairs → language/data sampling and curation → image patches + 64-token
  text → vision/text towers → sigmoid pair objective + auxiliary decoder caption/localization objectives → late-stage global/
  local teacher views and masked student patches → shared representation update → fixed-resolution or NaFlex checkpoint →
  downstream zero-shot retrieval/classification, dense probe, VLM or localization consumer。
- **Implementation Details:** training uses WebLI (10B images / 12B alt-texts / 109 languages) with a reported 90% English,
  10% non-English mixture；Gemma 256k tokenizer and length 64；Adam, peak LR 1e-3, decoupled weight decay 1e-4, gradient
  norm 1, batch 32k, 20k warmup and 40B examples。The auxiliary decoder performs three forwards per example but is discarded
  after training。Up to 2,048 TPUv5e devices and FSDP are reported。Official checkpoints span ViT-B/L/So400m/g；standard
  variants reuse SigLIP ViT/two-tower code with a new tokenizer/vocab, while NaFlex requires dedicated ViT and preprocessing。
- **Evaluation Contract:** frozen/zero-shot classification and image-text retrieval；XM3600 retrieval across 36 languages；
  frozen dense probes for segmentation, depth and surface normals；VLM transfer；referring-expression localization；cultural/
  geographic diversity and representation-bias tests。Comparisons span equal-size SigLIP predecessors, external encoders and
  multiple token sequence lengths, but task protocols differ and are not a production latency/cost contract。
- **Baselines / Ablations / Sensitivity / Overhead:** same-scale SigLIP is the main predecessor；LocCa, CLIP-family,
  DINOv2 and other encoders appear by task。Fixed-resolution and NaFlex variants are compared across token lengths；small-model
  distillation and broad recipe effects are discussed。The paper does not provide a factorial ablation that isolates each
  objective, curation choice, data mixture or stage, and does not report end-to-end training/serving overhead for each component。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** up to 2,048 TPUv5e for training；ViT-B 86M,
  L 303M, So400m 400M and g 1B checkpoints；batch 32k and 40B training examples；text length 64；multiple image token
  lengths/resolutions。Precision, inference hardware, online batching/concurrency, latency/throughput and production SLO are
  Not Disclosed；checkpoint benchmark numbers cannot be converted into serving efficiency claims。
- **What the Evidence Actually Proves:** the authors implemented a backward-compatible encoder family whose combined
  training recipe improves their reported global, multilingual, dense and localization evaluations over comparable SigLIP
  checkpoints；NaFlex demonstrates that native aspect ratio and variable resolution can be exposed as one representation
  artifact rather than separate fixed-resolution models。Official checkpoints make the artifact contract inspectable。
- **What It Does Not Prove:** the evidence does not identify which added component causes each gain, establish that NaFlex
  dominates fixed resolution on every image distribution, or prove universal multilingual/cultural fairness。It does not prove
  lower production cost, cross-hardware efficiency, robustness under distribution shift or independent reproduction of WebLI training。
- **Limitations / Threats to Validity:** private WebLI construction and online curation reduce reproducibility；the multi-change
  recipe confounds causal attribution；no dedicated limitations section；some subgroup fairness gains are small or absent；
  dense probes and VLM transfer depend on downstream heads/prompts；training scale and proprietary infrastructure restrict
  sensitivity analysis, while current repository artifacts may differ from the event-time implementation。
- **Trade-offs / New Failure Modes:** richer objectives improve locality and transfer but add decoder forwards, EMA teacher,
  multiple views, masked inputs, staging complexity and data-policy state；discarding the decoder keeps inference simple but
  loses an explicit deployed localization module。NaFlex reduces resize distortion and checkpoint proliferation yet introduces
  variable sequence length, padding/batching variance, positional/preprocessing compatibility risk and less predictable admission cost。
- **Where the Previous Design Still Applies:** original/fixed-resolution SigLIP remains appropriate for regular image shapes,
  predictable batching and global retrieval/classification；specialist dense models remain preferable when pixel-level calibration
  and task-specific guarantees dominate representation reuse；separate resolution checkpoints can simplify constrained edge deployment。
- **Evolution Relationship:** `Direct Evolution` from SigLIP at the representation/training-contract layer；`Alternative Branch`
  between fixed-resolution and NaFlex artifacts；`Layering / Dependency` toward VLM, retrieval and dense consumers rather than
  replacement of their task-specific heads or evaluation contracts。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23；new node）canonical owner；`TRAIN-DATA` and
  `TRAIN-PRETRAINING` own curation/objective execution；`INFER-REQUEST-LIFECYCLE` owns variable-token admission；
  `PLATFORM-EVALUATION-SYSTEM` owns downstream evidence contracts。
- **Target and Adjacent Chapters Read:** read Ch22 long-context boundary、Ch23 multimodal representation and Ch24
  generative paradigms；verified that SigLIP 2 changes encoder supervision/artifact shape, not autoregressive or diffusion generation。
- **Existing Coverage:** Ch23 already treats modality/coordinate/artifact identity, native-resolution token expansion and
  variable serving cost。This source adds a bounded evolution case from global contrastive representation to multi-objective
  local/dense supervision, but the Weekly-only phase does not decide whether Books prose should change。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added Weekly score, full review packet, artifact compatibility and evidence boundary；no Books change。
- **Open Questions:** event-time code commit and preprocessing/version identity；component-level causal ablations；WebLI
  provenance/deletion and curation policy；precision/energy/serving cost；NaFlex batching/admission behavior；independent fairness
  and dense-transfer reproduction；whether released checkpoints preserve claimed behavior under later tokenizer/framework changes。

### SuperGPQA

- **Candidate / Week / Score:** SuperGPQA: Scaling LLM Evaluation across 285 Graduate Disciplines / 2025-W08 / 25/30。
- **Source Family ID:** `map-supergpqa-long-tail-evaluation-contract`。
- **Source Type:** arXiv v1 benchmark paper + later revision history + author dataset/evaluation repository。
- **First-public Date / Revision History:** v1 submitted 2025-02-20 17:05 UTC；v2 2025-02-27；v3 2025-03-05；
  v4 2025-03-28。W08 event claims are grounded in the 256-page v1 PDF；v4 HTML and current repository are used to
  inspect revision/artifact continuity, not projected backward as W08 facts。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14739v1；https://arxiv.org/pdf/2502.14739v1；
  https://arxiv.org/abs/2502.14739；https://github.com/SuperGPQA/SuperGPQA。
- **Related Primary Sources:** author project page and published Hugging Face dataset/leaderboard/responses expose benchmark
  artifacts；GPQA、MMLU-Pro、MMLU-Redux and LIME define predecessor benchmark and data-quality practices。Current artifacts
  require their own revision identity before reproducing v1 results。
- **Access and Verification Status:** Verified；v1 PDF, metadata/revision history and public repository are accessible。
  Exact event-time dataset snapshot/commit, complete source screenshots, all proprietary API responses and accelerator inventory
  are Not Disclosed or not pinned by the paper。
- **Full-read Coverage:** read v1 metadata, Abstract/Introduction, collection pipeline, source screening, transcription,
  rule/LLM/expert quality inspection, statistics, all main experiments, subfield prompt sensitivity, 24-prompt robustness,
  BoN/majority voting, discipline discrimination, Related Work, contribution boundary and appendices covering examples,
  annotation tutorial, filtering rules, expert rubric, discipline statistics, prompts, source lists and per-model/per-field results；
  checked v2-v4 history and repository inference/config/artifact contract。The paper has no dedicated limitations section。
- **Original Problem:** mainstream benchmarks concentrate on a small set of popular disciplines and can saturate or hide
  long-tail professional weaknesses；a single aggregate accuracy also cannot reveal whether a model lacks knowledge, reasoning,
  prompt robustness or coverage in a specific domain。
- **Why the Previous Design Was Reasonable:** MMLU/GPQA-style fixed multiple-choice sets are cheap to run, easy to score
  deterministically and support broad model comparison；smaller curated datasets make expert validation and contamination analysis
  more tractable than a 285-subfield corpus。
- **Changed Constraint:** evaluation is expected to cover graduate-level knowledge in 285 subfields, including agriculture,
  light industry and service disciplines, while retaining difficult questions and enough samples per subfield。At this scale,
  expert-only authoring is expensive, but unconstrained crowdsourcing/LLM generation creates ambiguity, wrong answers and leakage。
- **Mechanism:** experts first select credible source material；crowd annotators translate/rewrite questions into multiple-choice
  form and may use an LLM to propose distractors；rule checks enforce schema, option count, perplexity and embedding-similarity
  thresholds；multiple frontier models flag invalid, ambiguous, trivial or field-mismatched items；experts with web access review
  suspicious questions and revise easy items。The final dataset is sliced by discipline/field/subfield and difficulty, then scored
  at sample and taxonomy-aggregated levels under fixed zero/five-shot prompts。
- **State Ownership:** source experts own reference provenance and initial correctness judgment；crowd annotators own
  transcription proposals；rule and LLM filters own suspicion/quality labels but not final truth；expert reviewers own accepted
  answer and taxonomy；dataset release owns item/version identity；evaluation harness owns prompt, model adapter, decoding and
  aggregation；release decisions remain with downstream users, not the leaderboard。
- **Control Flow / Data Flow:** textbook/credible-source question + screenshot → expert source screening → crowd translation/
  conversion/distractor proposal → schema/plagiarism/similarity checks → multi-model validity, solvability, field and discrimination
  labels → expert review/rewrite → versioned item with answer/difficulty/taxonomy → model prompt and response → deterministic option
  extraction/scoring → sample/subfield/field/discipline slices → robustness or sampling analysis。
- **Implementation Details:** v1 reports 26,529 questions across 13 disciplines, 72 fields and 285 subfields, with at least
  50 per subfield and an average 9.67 options；over 80 expert annotators participate。Duplicate detection uses all-MiniLM-L6-v2
  embeddings with cosine threshold 0.90 and Faiss；rule checks constrain 4～10 options and Qwen2.5-0.5B perplexity <=100。
  Current repository supplies Python inference configs, local vLLM acceleration, API workers and published response files, but
  is not treated as the exact v1 environment without a pinned commit/dataset revision。
- **Evaluation Contract:** reasoning/chat models use zero-shot prompts；base models use five-shot prompts；main runs use
  temperature 0, maximum 32K new tokens for reasoning models and 4K for others。Reported outputs include overall sample,
  macro-style subfield/field/discipline, difficulty and discipline scores。Prompt robustness uses 24 semantically equivalent
  styles on Qwen2.5 0.5B～72B；BoN and majority voting reuse 32 temperature-0.7 samples for two selected models。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons cover 6 reasoning families/modes, 28 chat and 17 base
  models in v1-era tables；sensitivity checks add/remove subfield labels, vary 24 prompts and compare N=1～32 sampling/voting。
  Dataset discrimination uses mean, SD, CV and top-three/bottom-three gaps。There is no controlled audit of annotation-stage
  removal, source-language mix, expert agreement, contamination, alternative taxonomy weighting or equal-compute model ranking。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/version and generation caps are reported；
  current repository examples expose local batch controls and 128 API workers, and local open models can run via vLLM。Event-time
  accelerator types, precision, batch/concurrency per result, retry/rate-limit policy, total token/cost budget, latency and SLO are
  Not Disclosed；therefore benchmark rankings are not throughput or cost comparisons。
- **What the Evidence Actually Proves:** the authors built and released a large taxonomy-indexed multiple-choice evaluation
  with explicit human/LLM/rule quality stages；v1 results demonstrate large score variation across model versions, task difficulty
  and disciplines under the stated prompts。Prompt/sampling analyses show that subject label, wording and aggregation strategy
  are part of the measured system, not neutral presentation details。
- **What It Does Not Prove:** a low score does not prove absence of professional competence or AGI, and a high score does not
  prove deployable domain performance。The study cannot isolate knowledge from reasoning, training contamination, translation,
  prompt/parser or inference budget；it does not validate model behavior on open-ended work, tools, current facts, safety or
  real professional outcomes, nor establish a universal model ranking across versions and providers。
- **Limitations / Threats to Validity:** 77.2% of items are concentrated in science, engineering and medicine；many sources
  originate from or are translated out of Chinese textbooks, creating cultural/language and possible pretraining-overlap bias；
  LLM-generated distractors and LLM-based filtering create shared-model circularity；expert agreement/error rates and a complete
  contamination audit are absent；multiple-choice format rewards elimination；proprietary API/model drift and revisioned dataset/
  harness artifacts reduce reproducibility。No explicit limitations chapter collects these threats。
- **Trade-offs / New Failure Modes:** scale and taxonomy improve long-tail visibility but increase provenance, copyright,
  annotation-consistency and slice-imbalance risk；LLM filters lower expert cost but can delete novel hard items or preserve shared
  misconceptions；expert correction improves quality but creates reviewer drift and high labor cost；macro aggregation protects
  small subfields yet changes ranking sensitivity；BoN raises apparent accuracy while multiplying compute and requiring an oracle
  selector that is not available in ordinary deployment。
- **Where the Previous Design Still Applies:** small expert-written benchmarks remain preferable for strong contamination
  control, mechanistic diagnosis and frequent refresh；open-ended executable evaluations are necessary for professional workflows；
  production replay and human outcome studies remain authoritative when intended use differs from graduate multiple-choice QA。
- **Evolution Relationship:** `Direct Evolution` from broad academic QA benchmarks toward taxonomy- and provenance-aware
  long-tail evaluation；`Layering / Dependency` with executable/system evaluation rather than a replacement；BoN/voting are
  `Alternative Branches` whose compute and selector contracts must be compared separately。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）canonical owner；`TRAIN-DATA`
  owns source/annotation lineage, `MODEL-CAPABILITY` owns capability taxonomy, and `PLATFORM-COST` owns inference-budget accounting。
- **Target and Adjacent Chapters Read:** read Current Ch65 scheduling boundary, Ch66 Evaluation System and Ch67 Monitoring；
  verified that SuperGPQA owns an EvalSpec/dataset/scorer case, not model architecture or online-health monitoring。
- **Existing Coverage:** Ch66 already requires subject identity, distribution, slice, uncertainty and scorer version；it also
  warns that benchmark values are conditional evidence。SuperGPQA supplies a bounded case for taxonomy coverage and collaborative
  quality control, while its imbalance, contamination and prompt-budget boundaries prevent a new universal conclusion。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added Weekly score, v1/v4 revision boundary, 30-field source packet and owner；no Books change。
- **Open Questions:** event-time dataset/commit hashes；per-item source and license audit；expert inter-rater agreement；
  contamination against each evaluated model；taxonomy/macro-weight sensitivity；parser failure rates；equal-token/equal-cost ranking；
  refreshed private/professional outcome validation and a formal benchmark retirement policy。

### LoRA Knowledge Capacity

- **Candidate / Week / Score:** How Much Knowledge Can You Pack into a LoRA Adapter without Harming LLM? / 2025-W08 / 23/30。
- **Source Family ID:** `airi-lora-knowledge-packing-forgetting`。
- **Source Type:** arXiv v1 experimental paper + author code/data/adapter artifact；later revisions used only for evolution tracking。
- **First-public Date / Revision History:** v1 submitted 2025-02-20 12:31 UTC；v2 2025-02-25；v3 2025-03-24。
  W08 evidence is locked to the 14-page v1 Llama-3.1-8B study；the Mistral experiment visible in current v3 is a later
  revision and is not projected backward into the event-time claim。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14502v1；https://arxiv.org/pdf/2502.14502v1；
  https://github.com/AIRI-Institute/knowledge-packing。
- **Related Primary Sources:** original LoRA defines low-rank update parameterization；DBpedia/TriviaQA provide factual
  sources；lm-evaluation-harness defines MMLU/TruthfulQA execution。Current Hugging Face datasets and adapters are useful
  artifacts but require event-time revision hashes for exact reproduction。
- **Access and Verification Status:** Verified；v1 PDF and public repository with data-generation, training, analysis and
  sample-adapter paths are accessible。Exact event-time commit/environment lock, accelerator type, full run logs and all
  adapter checkpoints are Not Disclosed。
- **Full-read Coverage:** read v1 metadata, Abstract/Introduction, Related Work, LoRA and knowledge-category definitions,
  reliability/undesirable-effect metrics, DBpedia/TriviaQA data construction, paraphrase/highly-known augmentation, LoRA
  training, train/test overlap rationale, all accuracy/shift/MMLU/TruthfulQA analyses, shift attribution, Conclusion,
  Limitations, Ethics and appendices for benchmark tables, prompts, category/shift examples and ARC/LogiQA；checked repository
  scripts/data/model artifacts and v2/v3 history without treating later Mistral evidence as v1。
- **Original Problem:** parameter-efficient updates can insert task or factual behavior cheaply, but freezing base weights
  does not guarantee preservation of the model's previous answers, calibrated refusal or reasoning behavior。Adapter “capacity”
  therefore cannot be judged only by training recall or trainable parameter count。
- **Why the Previous Design Was Reasonable:** RAG/few-shot context keeps changing facts outside weights and remains easier
  to cite or roll back；full fine-tuning offers a larger update space；ordinary LoRA is attractive when deployment needs a small
  versioned delta and repeated retrieval latency or a full checkpoint copy is undesirable。
- **Changed Constraint:** the experiment asks whether 1～3,000 facts classified as unknown to one base model can be made
  recallable while retaining already-known facts and external QA behavior。Training-set composition, not merely rank, becomes
  an explicit control variable because facts share entities, relations and answer targets。
- **Mechanism:** classify DBpedia question-answer facts as Unknown/MaybeKnown/HighlyKnown by repeated few-shot responses；
  sample Unknown facts for training and optionally add one or ten paraphrases or HighlyKnown facts per unknown；train rank-1
  LoRA on MLP down/gate/up projections；then measure trained-fact recall, positive Unknown→HighlyKnown shifts, negative
  HighlyKnown→Unknown shifts, refusal/diversity collapse and external benchmark movement。
- **State Ownership:** immutable base revision owns prior parametric behavior；adapter owns the learned low-rank delta；data
  pipeline owns fact/alias/template identity and Unknown/HighlyKnown labels relative to one prompt/model policy；training config
  owns rank/modules/hyperparameters；evaluation harness owns prompts, sampling, substring matching and benchmark metrics；Registry
  must own base-adapter compatibility and promotion/rollback evidence。
- **Control Flow / Data Flow:** DBpedia triples/TriviaQA → templated QA + aliases → ten four-shot probes classify each fact →
  sample 1/10/50/100/500/3,000 Unknown items → optional paraphrase or HighlyKnown augmentation → rank-1 LoRA training →
  ten distinct four-shot evaluation prompts → fact-category shifts/refusal/answer-frequency analysis + MMLU/TruthfulQA/ARC/
  LogiQA checks → accept, revise data mixture or reject adapter。
- **Implementation Details:** v1 uses Llama-3.1-8B-Instruct；10 epochs, learning rate 1e-3, batch 16, rank 1, alpha 2,
  dropout 0.1 and target modules `down_proj`, `gate_proj`, `up_proj`。The fact pool has 21,036 DBpedia QA pairs classified
  into 14,373 Unknown, 3,931 MaybeKnown and 2,732 HighlyKnown。Training items are intentionally retained in the evaluation
  pool to test memorization, so trained-fact accuracy is not held-out generalization。
- **Evaluation Contract:** each adapter is probed ten times with four distinct TriviaQA examples per prompt；an answer is
  counted by reference/alias substring。Intrinsic metrics include trained-fact accuracy and positive/negative category shifts；
  response refusal/unique-answer concentration diagnoses behavioral collapse。External evaluation uses 5-shot MMLU,
  0-shot TruthfulQA MC1/MC2, plus appendix ARC/LogiQA；key plots report min/max across three seeds where stated。
- **Baselines / Ablations / Sensitivity / Overhead:** baseline is the unmodified Llama checkpoint；factorial grid varies
  Unknown count and zero/one/ten paraphrase or HighlyKnown additions。The authors explored learning rate/rank but v1 final tables
  expose a fixed rank-1 recipe and do not provide a complete hyperparameter sensitivity or equal-token control。No RAG, full-
  fine-tuning, alternative PEFT or independently tuned early-stopping baseline is evaluated。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Llama-3.1-8B-Instruct, rank 1, batch 16 and
  ten epochs are disclosed；the paper notes high computational cost but accelerator model/count, precision, sequence length,
  gradient accumulation, wall time, energy, inference concurrency and production SLO are Not Disclosed。Those omissions forbid
  a training-efficiency or serving-capacity comparison。
- **What the Evidence Actually Proves:** under this one base model, fact-generation scheme, rank-1 MLP adapter and evaluation
  policy, increasing or rebalancing factual examples changes both target recall and unrelated behavior；high train recall can
  coexist with negative knowledge shifts, lower external benchmark scores, reduced refusal and overrepresented answers。This
  supports adapter promotion gates broader than loss and trained-fact accuracy。
- **What It Does Not Prove:** it does not establish a universal number of facts that fit in LoRA, a causal capacity law for rank,
  or that adapters store discrete knowledge independently of the base。It does not show held-out factual generalization, isolate
  data duplication from optimizer/epoch effects, prove MMLU is pure reasoning or TruthfulQA is complete truthfulness, or compare
  the same knowledge-update contract against RAG/full fine-tuning/model editing。
- **Limitations / Threats to Validity:** v1 covers one 8B instruct model, one rank/modules recipe and templated DBpedia facts；
  knowledge categories depend on ten prompts and substring aliases, so “Unknown” is policy-relative；training/evaluation overlap
  makes recall a memorization check；MMLU/TruthfulQA proxies and small-seed min/max do not isolate mechanisms；early stopping,
  same-domain/range augmentation and few-shot category conditioning remain unexplored；the later Mistral result cannot repair v1 scope。
- **Trade-offs / New Failure Modes:** a compact adapter lowers trainable/checkpoint state but can overwrite answer distributions,
  suppress uncertainty, amplify frequent targets and silently degrade unrelated slices；mixing known facts or paraphrases may improve
  one metric while increasing token/training cost or another regression。More evaluation prompts improve category confidence but
  add model-dependent labeling cost and can still miss alternative correct forms。
- **Where the Previous Design Still Applies:** RAG remains preferable for fast-changing, auditable or deletable facts；prompt/
  few-shot control is better for reversible low-volume updates；full fine-tuning remains reasonable when broad behavioral change
  and sufficient data/compute justify it；plain LoRA is appropriate when its small artifact and base reuse are paired with explicit
  regression, refusal and answer-distribution gates。
- **Evolution Relationship:** `Principle Reuse` of LoRA parameterization for factual update；`Alternative Branch` versus RAG,
  prompt context, model editing and full fine-tuning。The paper refines the evaluation contract rather than replacing the original
  low-rank mechanism or deriving a direct capacity-scaling law。
- **ROADMAP Node:** `TRAIN-LORA`（Current Ch30；Legacy Ch26）canonical owner；`TRAIN-DATA` owns fact mixture/provenance,
  `PLATFORM-EVALUATION-SYSTEM` owns regression/refusal/slice gates, and `PLATFORM-MODEL-REGISTRY` owns base-adapter lineage。
- **Target and Adjacent Chapters Read:** read Current Ch29 SFT, Ch30 LoRA and Ch31 RLHF；verified that the contribution is
  an adapter data/evaluation boundary, not a new optimization objective or preference-learning method。
- **Existing Coverage:** Ch30 already states that rank/module choice defines update space, adapter artifacts need base lineage,
  and parametric recall is not reasoning/generalization。This source adds bounded evidence that small trainable state does not
  imply small behavioral blast radius；the Weekly-only phase does not decide whether the chapter needs refinement。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-only score/review packet, separated v3 Mistral revision and recorded artifact/
  evaluation boundaries；no Books change。
- **Open Questions:** event-time commit/environment and all adapter hashes；rank/module/epoch/early-stop sensitivity；held-out
  paraphrase/relation/entity generalization；equal-token and RAG/full-FT/model-editing comparisons；confidence/refusal calibration；
  data deletion and adapter unlearning；whether later revisions reproduce under identical base/tokenizer/harness versions。

### Soundwave

- **Candidate / Week / Score:** Soundwave: Less is More for Speech-Text Alignment in LLMs / 2025-W08 / 25/30。
- **Source Family ID:** `soundwave-speech-text-alignment-shrinking`。
- **Source Type:** arXiv v1 experimental paper + official architecture/inference repository；later model-weight release is a
  revision node, not W08 mechanism evidence。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 14:36 UTC；official repository records architecture
  and inference-code release on 2025-02-18, demo on 2025-02-19 and weights on 2025-05-03。The paper has no later arXiv revision；
  W08 is locked to v1 and event-time code availability, while the May weight release is retained only for reproducibility lineage。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.12900；https://arxiv.org/pdf/2502.12900；
  https://github.com/FreedomIntelligence/Soundwave。
- **Related Primary Sources:** Whisper Large V3 supplies the frozen audio encoder contract；Llama 3.1 supplies the language
  backbone；Qwen2-Audio and AIR-Bench define important author-selected baselines/evaluation protocols。Their reported training
  data and scores are not normalized experiments under Soundwave's exact data, task, model and serving contract。
- **Access and Verification Status:** Verified from the 27-page v1 PDF and official repository。arXiv HTML is unavailable,
  so the corresponding PDF was read；the current repository exposes architecture, inference code and weights, but no pinned
  event-time commit, training pipeline, full dataset manifest or independent reproduction。
- **Full-read Coverage:** read metadata, Abstract/Introduction, complete three-stage Method, module/state diagrams, alignment and
  shrinking equations, dynamic task sampling, dataset construction/licensing tables, all main evaluation tables, alignment/data/
  shrinking/task-ratio analyses, appendices for prompts/examples/results, Conclusion, Limitations and Ethics；checked repository
  file layout, inference requirements, model release timeline and license。
- **Original Problem:** a pretrained speech encoder produces long frame-level sequences in a representation space different from
  the subword embeddings consumed by an LLM。Naively projecting every frame forces the language model to learn both cross-modal
  alignment and temporal compression from expensive annotated data, increasing prefill state and optimization coupling。
- **Why the Previous Design Was Reasonable:** a single projector/resampler plus end-to-end instruction tuning is simple, preserves
  dense acoustic evidence and works when large paired corpora and compute are available；fixed-rate convolution/pooling has predictable
  shapes and avoids relying on CTC confidence。Separate ASR plus text LLM pipelines remain auditable and modular for transcription-first use。
- **Changed Constraint:** the target is broad speech-to-text behavior with roughly ten-thousand hours rather than hundreds of
  thousands, while retaining useful nonverbal cues and reducing the audio sequence presented to an 8B LLM。Data efficiency,
  representation compatibility and prefill length therefore become coupled design constraints rather than independent tuning choices。
- **Mechanism:** stage I freezes Whisper Large V3 and the LLM, trains a projection-plus-Transformer alignment adapter against the
  LLM's shared token embeddings with auxiliary CTC, and concatenates adjacent audio features；stage II uses CTC peaks to select
  content positions while a cross-attention shrinking adapter retrieves tone/pitch/context from the original sequence and trains LoRA；
  stage III performs speech/text SFT。A temperature schedule gradually changes task sampling from data-proportional toward balanced。
- **State Ownership:** the frozen audio encoder owns acoustic feature extraction；alignment adapter owns speech-to-token-space
  representation；CTC logits own provisional boundary/confidence state；shrinking adapter owns selected-token state plus retrieved
  acoustic context；LoRA owns language-backbone adaptation；dataset pipeline owns transcript/sound-label/task provenance；inference
  runtime owns audio preprocessing, prompt/template, generated-token state and latency measurement。
- **Control Flow / Data Flow:** waveform → 16 kHz features → frozen Whisper encoder → alignment adapter → auxiliary CTC tokens/
  peaks → content-position selection + cross-attention over full aligned features → compressed speech embeddings → prompt/text
  embeddings → LoRA-adapted Llama autoregressive decode；training flows alignment-only → joint shrinking/LoRA → mixed-task SFT,
  with scheduled task sampling and stage-specific frozen/trainable modules。
- **Implementation Details:** paper reports approximately 635M frozen audio-encoder, 144M alignment, 67M shrinking, 8B frozen LLM
  and 55M LoRA parameters。Filtered ASR retains samples with Whisper-medium WER below 10%；roughly 8k sound categories are manually
  annotated and clearer audio is normalized around three seconds。The paper distinguishes about 9,856.91 unique audio hours from
  14,068.77 task-reused hours；SFT contains 2,651,493 examples / 5,358.54 hours, 98.61% of speech data is English。
- **Evaluation Contract:** closed tasks cover LibriSpeech/CoVoST2-style ASR and translation, emotion and vocal-sound datasets；
  open tasks use AIR-Bench speech/sound/chat protocols。Analysis experiments use LibriSpeech, eight A800 GPUs and 4,000 steps；
  the shrinking table reports WER, compressed sequence ratio and TTFT, while conversation/intelligence retention uses author-selected
  text and speech tasks。Exact evaluator versions and all decoding prompts/settings are only partially disclosed。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include Qwen2-Audio and prior speech LLMs；alignment analysis
  compares no alignment stage and a projection adapter, but authors note alignment benefit cannot be fully separated from training
  method。Shrinking compares CTC selection with/without auxiliary cross-attention and fixed-rate adapters；data analysis compares
  1k versus 10k hours, and task-ratio experiments test mixtures。No equal-data/equal-parameter/equal-compute reproduction, component
  factorial study, multilingual ratio sweep or production concurrency study is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** analysis discloses eight A800 GPUs, Llama3.1 ~8B,
  Whisper Large V3, module sizes and 4,000 steps；repository inference requires at least 21GB GPU memory and examples use FP16 audio
  features。Main training precision, sequence-length distribution, optimizer batch/accumulation, serving GPU/runtime, TTFT batch/
  concurrency and production SLO are Not Disclosed。The reported 72 ms TTFT and 2.5% sequence ratio therefore remain table-local。
- **What the Evidence Actually Proves:** in the authors' v1 setup, explicitly separating alignment from content-dependent sequence
  shrinking produces a trainable speech-LLM pipeline；CTC-selected tokens plus auxiliary cross-attention retain more ASR accuracy than
  selection without auxiliary context, and present much shorter sequences to the LLM than fixed-rate baselines。Results support treating
  representation identity and sequence-state compression as distinct system contracts。
- **What It Does Not Prove:** it does not prove universal 50x data efficiency, that CTC shrinking dominates every resampler, or that
  2.5% compression preserves all acoustic/paralinguistic information。It does not isolate every stage causally, establish production
  latency/throughput gains, demonstrate multilingual/music robustness, or show that an integrated speech LLM should replace modular ASR。
- **Limitations / Threats to Validity:** nearly all speech training data is English；sound labels are comparatively small and the
  optimal speech/text/task ratio is unknown；music and multilingual results are weak；larger backbones are untested；AIR-Bench and data-
  scale comparisons inherit judge/task/model differences；training code, exact dataset revisions, event-time commit and complete
  leakage/license audit are absent；paper is an author preprint without independent reproduction。
- **Trade-offs / New Failure Modes:** content-adaptive shrinking reduces LLM sequence state but adds CTC-boundary errors, two-adapter
  version coupling and loss of low-confidence acoustic events；cross-attention recovers context at additional compute/memory cost；manual
  cleaning improves efficiency but raises labor, provenance and domain-bias costs；task balancing protects small tasks yet can over-sample
  noisy categories。An apparently correct transcript can still discard emotion, speaker or timing evidence needed downstream。
- **Where the Previous Design Still Applies:** dense/fixed-rate resampling remains preferable when exact temporal detail or predictable
  kernels matter；large-scale end-to-end training is reasonable when data/compute and broad coverage are available；separate ASR + text
  LLM remains stronger for inspectable transcripts, independent component upgrades and conservative production failure isolation。
- **Evolution Relationship:** `Direct Evolution` from generic projection/fixed-rate resampling toward explicitly aligned and
  content-dependent speech token state；`Layering / Dependency` on pretrained audio/LLM representations；`Alternative Branch` versus
  modular ASR pipelines and dense audio-token models, not a universal replacement。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Current Ch23）canonical owner；`TRAIN-DATA` owns speech/task provenance and
  mixture, `TRAIN-SFT` owns instruction-stage policy, `INFER-PREFILL-DECODE` owns compressed-sequence latency accounting, and
  `PLATFORM-EVALUATION-SYSTEM` owns multilingual/audio-task evidence contracts。
- **Target and Adjacent Chapters Read:** read Current Ch22 Long Context, Ch23 Multimodal Representation and Ch24 Multimodal
  Generative Paradigms；verified that Soundwave is a representation/sequence-interface case, not a new language-generation paradigm。
- **Existing Coverage:** Ch23 already separates modality encoder, connector, token identity and temporal alignment, and warns that
  compression is a semantic contract rather than only an optimization。Soundwave adds a bounded mechanism case for decoupling alignment
  from content-dependent shrinking；whether that warrants prose refinement remains deferred to the Historical Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1/artifact lineage, score, exact 30-field review, workload/evidence boundaries and
  canonical owner；removed the obsolete HTML blocker；no Books change。
- **Open Questions:** event-time repository commit and training code；dataset/sample/license hashes；CTC threshold and boundary-error
  sensitivity；equal-data/equal-compute resampler baselines；multilingual/music/domain-shift performance；production TTFT/throughput under
  fixed hardware, precision, length, batch and concurrency；rollback/compatibility across encoder, adapter, LoRA and tokenizer versions。

### Embedding Space Capacity

- **Candidate / Week / Score:** Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding
  Space Capacity / 2025-W08 / 25/30。
- **Source Family ID:** `airi-hidden-embedding-capacity-per-sample-optimization`。
- **Source Type:** arXiv v1 experimental paper + author code/data/notebook artifact；ACL camera-ready and Mamba additions are
  later revision nodes。
- **First-public Date / Revision History:** v1 submitted 2025-02-18 17:08 UTC；v2 camera-ready 2025-06-05；v3 2025-06-22。
  W08 evidence uses the 14-page v1 Transformer-only study。Mamba experiments, entropy-coder comparison, ACL acceptance/oral status
  and later appendix changes are tracked as June evolution, not projected backward into the February event。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13063v1；https://arxiv.org/html/2502.13063v1；
  https://arxiv.org/pdf/2502.13063v1；https://github.com/yurakuratov/hidden_capacity。
- **Related Primary Sources:** Prompt Tuning supplies the frozen-model/trainable-vector mechanism；RMT/AutoCompressor/ICAE/gist
  tokens define deployable memory/context-compression predecessors；PG-19, post-October-2024 AO3 texts and GloVe-word sequences
  define the three uncertainty regimes。Later artifact claims must be tied to their revision rather than used as v1 evidence。
- **Access and Verification Status:** Verified for v1 paper and current author repository；repository exposes training wrapper,
  model code, scripts, preprocessing, URL list and analysis notebooks。Exact event-time commit/environment, raw run logs, random
  seeds and a frozen February data snapshot are Not Disclosed；current repository also contains later-revision material。
- **Full-read Coverage:** read v1 metadata, Abstract/Introduction, all Related Work branches, Method/equations, complete experiments
  on model/data/capacity/uncertainty/vector scaling/utilization, Discussion, Limitations, Broader Impact and appendices for model/training
  details, fanfic collection, all results and representation geometry；checked current artifact structure and v2/v3 update history while
  excluding later Mamba/entropy evidence from W08 conclusions。
- **Original Problem:** input embeddings have thousands of finite-precision coordinates, yet ordinary tokenization spends one vector
  per token and practical learned context compressors recover far less information than a simple bit-count upper bound suggests。
  It is unclear whether the bottleneck is vector capacity, pretrained decoder utilization or the encoder that must construct the vector。
- **Why the Previous Design Was Reasonable:** one-token/one-row embeddings give stable identity, cheap lookup and compositional
  processing；RAG preserves source text externally；learned compressors amortize encoding over many samples and optimize downstream
  utility rather than exact reconstruction。Their lower ratios are acceptable because online systems cannot run an optimizer per prompt。
- **Changed Constraint:** to measure a capacity ceiling rather than build a deployable compressor, encoding cost may be unbounded
  per sample and the frozen decoder can be used as part of the codebook。The experiment must separate information contributed by the
  vector from tokens the LM predicts from its parameters, and compare texts with different baseline uncertainty rather than length alone。
- **Mechanism:** for each text, randomly initialize one or more `[mem]` vectors prepended to the sequence, freeze all model weights
  and optimize only those vectors with next-token cross-entropy；decode from `[mem]` and measure 0.99-threshold Decoding Capacity,
  Token Gain over the no-memory LM and cross-entropy Information Gain。Natural, post-release fanfic and random-word sequences separate
  language predictability from vector-conditioned information；K-vector runs test scaling of the storage interface。
- **State Ownership:** frozen checkpoint/tokenizer owns the decoder prior and vocabulary；each text owns a unique optimized `[mem]`
  artifact；optimizer/config owns its construction path；dataset pipeline owns text, length and novelty identity；evaluation harness owns
  teacher-forcing, threshold and baseline subtraction。A practical memory service would additionally need vector-checkpoint-tokenizer
  compatibility, access control, deletion and integrity ownership, none of which the experiment implements。
- **Control Flow / Data Flow:** source text → tokenize/length slice → initialize K trainable vectors → prepend vectors plus teacher-
  forced prefix → frozen LM next-token loss → AdamW updates only `[mem]` → stop at perfect training reconstruction or 5,000 steps →
  decode/evaluate with and without `[mem]` → token gain/cross-entropy reduction/capacity threshold → compare model, domain and K slices。
- **Implementation Details:** v1 covers Pythia 160M/410M/1.4B/2.8B, OPT-1.3B, OLMo-1B, Sheared-LLaMA-1.3B and Llama 1B/3B/8B；
  `[mem]` dimension equals model input hidden size。AdamW uses learning rate 0.01, betas 0.9/0.9, weight decay 0.01, maximum 5,000
  steps and early stop at token accuracy 1.0。For each tested length, 50 texts are sampled；current code wraps Hugging Face models and
  includes single/multiple-vector scripts and analysis notebooks。
- **Evaluation Contract:** PG-19 and post-model fanfics use length grid 64～3,072 tokens；random data samples words from top-100k
  GloVe vocabulary。Decoding Capacity is the longest grid point exceeding 0.99 token accuracy under the paper's teacher-forced
  evaluation；Token Gain subtracts unconditioned correct predictions；Information Gain subtracts cross-entropy。Values are averaged
  over text samples and must not be compared across different vocabularies without normalization。
- **Baselines / Ablations / Sensitivity / Overhead:** no-`[mem]` LM is the principal baseline；model families/sizes, natural versus
  recent versus random text, sequence length and K=1～16/32 vectors form sensitivity axes。The study compares observed vector use to
  a finite-bit upper bound, but does not train a shared encoder or compare equal encoding time against RAG, autoencoders, gist tokens,
  KV compression or classical codecs in v1；architecture/pretraining factors are confounded across checkpoints。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** each run uses one A100 80GB；up to four GPUs execute runs
  in parallel；5,000-step optimization takes seconds for small/short cases and 10～20 minutes for larger/longer cases。Model sizes,
  hidden/vocabulary dimensions and length grid are disclosed；optimization precision, batch/concurrency, generation settings, storage
  dtype/serialization, online encoding latency budget, throughput and SLO are Not Disclosed。Therefore ratios are capacity probes, not serving gains。
- **What the Evidence Actually Proves:** under per-sample gradient optimization and the v1 teacher-forced/reconstruction contract,
  frozen LMs admit input vectors that strongly reduce sequence uncertainty；capacity varies substantially across checkpoints, correlates
  more directly with baseline cross-entropy than raw token length, and grows approximately with additional vectors in the tested ranges。
  Recent fanfic/random-word controls show the effect is not explained only by memorized PG-19 text or ordinary language predictability。
- **What It Does Not Prove:** it does not provide an encoder that discovers these vectors cheaply, demonstrate downstream QA/reasoning
  utility, lossless free-running generation under production settings, or a storage codec with stable finite-bit serialization。It does
  not prove larger parameter count alone causes higher capacity, that utilization diagnoses training completeness, or that 1,568× is a
  general ratio across texts, tokenizers, precisions and models；the 120k-token book estimate is an extrapolation, not an experiment。
- **Limitations / Threats to Validity:** per-sample optimization is far more expensive than the saved input compute；0.99 teacher-
  forced token accuracy can hide cascading free-generation errors；finite-bit upper bound assumes usable independent coordinates while
  optimized vectors may require unstated precision；50 samples/length and coarse grid limit threshold resolution；model-family factors
  are confounded；random GloVe words can split into multiple tokenizer tokens。Appendix geometry finds same-text solutions scattered,
  non-unique and not linearly connected, weakening semantic retrieval and interpolation assumptions。
- **Trade-offs / New Failure Modes:** dense latent state can reduce visible sequence length but transfers cost to encoder optimization,
  version-coupled decoding and opaque access control；higher compression removes token-level provenance, selective deletion and human
  inspection；small perturbation/quantization or wrong checkpoint may corrupt the whole sequence；multiple valid codes complicate dedup,
  similarity search and canonical identity。Keeping raw tokens costs attention/KV but preserves explicit boundaries and partial recovery。
- **Where the Previous Design Still Applies:** ordinary token sequences remain preferable for online prompts, exact provenance and
  model-independent storage；RAG remains better for mutable, citeable and deletable knowledge；learned/amortized compressors are required
  when encoding latency matters；KV pruning/sparse Attention remain separate execution branches when exact reconstruction is unnecessary。
- **Evolution Relationship:** `Explanatory Analogy` for the upper bound of prompt/context/memory compression, not a deployable
  successor；`Principle Reuse` of prompt tuning and recurrent memory；`Alternative Branch` versus token/KV compression and external retrieval。The work changes
  the question from “what ratio does this encoder achieve?” to “how much uncertainty can this decoder-controlled vector remove?”。
- **ROADMAP Node:** `MODEL-EMBEDDING`（Current Ch12）canonical owner；`MODEL-LONG-CONTEXT` owns sequence-capacity implications,
  `AGENT-MEMORY` owns persistent/retrievable memory semantics, and `INFER-KV-CACHE` / `INFER-MEMORY-OPTIMIZATION` own runtime state cost。
- **Target and Adjacent Chapters Read:** read Current Ch11 Tokenizer, Ch12 Embedding, Ch13 Position Encoding and Ch22 Long Context；
  verified that the contribution is a capacity/evidence boundary for continuous input state, not an Agent memory implementation or KV engine。
- **Existing Coverage:** Ch12 already distinguishes token embeddings from contextual/sentence state and treats vector geometry as learned,
  while Ch22 separates accepted length, utilization and system capacity。This source adds an upper-bound experiment showing that stored
  information, semantic usefulness and amortized encoder cost are different contracts；Books refinement remains deferred。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-only score/review, excluded June Mamba/entropy/ACL revision evidence, recorded exact
  experimental and geometry boundaries and canonical owner；no Books change。
- **Open Questions:** event-time commit/seeds/environment；free-running exact-match and perturbation/quantization robustness；shared
  encoder quality/cost frontier；stable vector identity and checkpoint migration；downstream retrieval/reasoning utility；privacy,
  provenance, delete and access-control semantics；controlled scaling law across architecture, pretraining and vocabulary families。

### S*: Test Time Scaling for Code Generation

- **Candidate / Week / Score:** S*: Test Time Scaling for Code Generation / 2025-W08 / 26/30。
- **Source Family ID:** `novasky-sstar-code-test-time-workflow`。
- **Source Type:** arXiv v1 experimental systems paper + official implementation/evaluation artifact。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 09:18 UTC；official repository announcement and code
  release dated 2025-02-21。No later arXiv revision；W08 owner date is the paper v1 event, with code as next-day artifact evidence。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14382；https://arxiv.org/html/2502.14382v1；
  https://arxiv.org/pdf/2502.14382v1；https://github.com/NovaSky-AI/SkyThought/tree/main/skythought/test-time-scaling。
- **Related Primary Sources:** LiveCodeBench v2/v4 and CodeContests define the executable benchmark contract；DSPy generates
  prompts；SkyThought provides generation, execution, baseline and cached-selection scripts。CodeMonkeys, self-debugging and
  majority voting define adjacent parallel/sequential branches, not interchangeable baselines for repository engineering。
- **Access and Verification Status:** Verified；15-page v1 HTML/PDF and official code directory are accessible。Repository exposes
  scripts/config examples and links result artifacts, but exact event-time commit, container image, complete API-model snapshots,
  sandbox implementation and all generated outputs were not independently replayed。
- **Full-read Coverage:** read metadata, Abstract/Introduction, Related Work, complete two-stage Method/algorithm, experimental setup,
  all main results, comparison tables, CodeContests transfer, temperature/sample/ICL/debugging/selection ablations, Conclusion,
  Limitations and prompt appendix；checked official directory layout, dependencies, run order and example command。
- **Original Problem:** parallel sampling can put a correct program in the candidate set but lacks a reliable selector；sequential
  self-debugging can improve one trajectory but saturates and may overfit a few public tests。Code offers executable feedback, yet
  generated expected outputs and unconstrained LLM judging remain unreliable for distinguishing near-correct programs。
- **Why the Previous Design Was Reasonable:** zero-shot is cheap；majority vote works when correct outputs dominate；single-trajectory
  debugging minimizes sandbox/model calls；generated tests provide extra coverage without private tests。Each remains suitable when
  latency/cost dominates, candidate errors are independent, or trusted public tests already separate solutions。
- **Changed Constraint:** additional inference compute is available and candidate programs can be sandboxed, but private tests remain
  hidden。The workflow must spend budget on both candidate coverage and selection discrimination, rather than treat pass@N as delivered accuracy。
- **Mechanism:** generate N independent programs at temperature 0.7；for each, execute public tests and perform up to R feedback-guided
  revisions；cluster surviving candidates by outputs on synthesized inputs；for each output-cluster pair, ask an LLM for an input likely
  to distinguish representative programs, execute both, return real outputs to the judge, accumulate pairwise wins and select from the
  highest-scoring cluster。
- **State Ownership:** generator owns candidate text, not correctness；sandbox owns execution result/error；public tests own early
  repair feedback；adaptive-input generator owns proposed distinguishing inputs；execution owns observed outputs；LLM judge owns local
  pairwise preference only；workflow owns candidate lineage, cluster graph, budget/stopping and final selection；private tests own evaluation truth。
- **Control Flow / Data Flow:** problem + public tests → N parallel generations → sandbox execute → feedback + candidate revision up
  to R or public-pass → generic synthesized inputs → execute all candidates → output clusters → pairwise adaptive input synthesis →
  sandbox outputs → judge comparison → cluster scores → random member of winning cluster → private-test Pass@1 evaluation。
- **Implementation Details:** main configuration uses N=16, temperature 0.7, no top-p and two debugging rounds；DSPy constructs prompts。
  Official artifact uses Python, DSPy 2.6.2, PyTorch and vLLM, separates baselines/dev/final/oracle/cached-selection scripts, and shows
  a 32-thread, release_v2, N=16 example。Paper states sandboxing but does not fully disclose isolation/resource/network policy。
- **Evaluation Contract:** development/ablation uses non-overlapping LiveCodeBench v4 (Aug～Nov 2024)；final LiveCodeBench v2 has
  511 problems across 182 easy/206 medium/123 hard；CodeContests adds 165 problems。Pass@1 is primary delivered metric, Pass@N is
  oracle coverage；models span Qwen2.5-Coder, GPT-4o-mini, distilled R1, QwQ and o1 references under provider/model snapshots stated in paper。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines are zero-shot, majority vote and self-debugging on the same models；
  ablations vary temperature, N, ICL retrieval, context retention, generated tests, debugging rounds and selection policy。Adaptive
  selection averages 57.5 versus 53.8 public-only/53.1 generated-tests/55.6 judge at N=8 on v4；no equal-dollar/deadline frontier,
  selector-model sweep, sandbox-failure ablation or statistical repetition is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** largest open-model experiment takes one day on eight H100s；
  N=16 and R=2 are disclosed。Precision, vLLM version, prompt/output lengths, batch scheduling, API concurrency/rate limits, per-problem
  token/sandbox calls, wall-time distribution, cost and production SLO are Not Disclosed；all experiments are conducted once。
- **What the Evidence Actually Proves:** within the two competition-code benchmarks and disclosed policy, mixing parallel candidates,
  execution feedback and adaptive distinguishing inputs improves final Pass@1 over the selected zero-shot/majority/self-debug baselines
  across tested models。Ablations support separating coverage from selection and using real execution outputs instead of asking a model
  to predict test outputs。
- **What It Does Not Prove:** it does not prove smaller models generally surpass larger/reasoning models at equal compute/cost, that
  adaptive selection is correct without private tests, or that gains transfer to repository-scale engineering, stateful services,
  nondeterministic programs or production side effects。It does not establish compute-optimal N/R allocation or independent reproducibility。
- **Limitations / Threats to Validity:** competition programs have compact specs and cheap deterministic execution；public-test reuse
  can induce overfitting；generated distinguishing inputs can be invalid or out of domain；same/provider-related models create correlated
  generation/judge errors；single runs lack variance；closed model drift harms reproduction。The paper internally reports 85.7 versus
  86.7 and 88.5 versus 88.7 in different sections, so headline decimals are not treated as stable evidence。
- **Trade-offs / New Failure Modes:** hybrid scaling raises coverage but multiplies model, sandbox and pairwise-comparison work；more
  candidates create quadratic cluster comparisons and correlated wrong solutions；feedback loops can repair syntax while entrenching
  public-test hacks；unsafe code, resource exhaustion, flaky execution, invalid inputs and judge order bias become workflow failures。
  Caching reduces repeat cost but adds candidate/environment identity and stale-result invalidation。
- **Where the Previous Design Still Applies:** zero-shot or one repair remains preferable under tight latency/cost；majority voting
  remains useful when outputs form trustworthy equivalence classes；deterministic comprehensive tests should directly select without an
  LLM judge；human review and repository CI remain necessary for multi-file changes, security, maintainability and irreversible effects。
- **Evolution Relationship:** `Direct Evolution` from parallel sampling or sequential debugging to a hybrid workflow；`Layering /
  Dependency` on sandbox execution and candidate identity；`Alternative Branch` versus reward-model/tree search and exhaustive tests。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Current Ch81；Legacy Ch77）canonical owner；`MODEL-SAMPLING` owns N/temperature policy,
  `AGENT-REFLECTION` owns feedback-guided local repair, `PLATFORM-EVALUATION-SYSTEM` owns executable benchmark truth, and
  `PLATFORM-COST` owns token/sandbox budget accounting。
- **Target and Adjacent Chapters Read:** read Current Ch80 Reflection, Ch81 Workflow and Ch82 Multi-Agent plus Ch20 Sampling；verified
  S* is a durable candidate/verification workflow, not evidence that multiple agents or a new decoding distribution are inherently better。
- **Existing Coverage:** Ch20 already separates Coverage from Selection and Ch81 already distinguishes parallel branches from sequential
  artifact refinement。S* supplies a bounded code-execution case and pairwise distinguishing-input mechanism；Books refinement remains deferred。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added exact v1/code packet, score, owner and paper-number discrepancy；no Books change。
- **Open Questions:** event-time commit/container/result hashes；valid-input and sandbox policy；per-stage token/call/cost/latency curve；
  repeated-seed confidence intervals；selector model/order calibration；compute-optimal N/R；repository-task transfer；cache identity,
  retry/idempotency and handling nondeterministic or stateful programs。

### Magma

- **Candidate / Week / Score:** Magma: A Foundation Model for Multimodal AI Agents / 2025-W08 / 27/30。
- **Source Family ID:** `microsoft-magma-multimodal-agentic-pretraining`。
- **Source Type:** arXiv v1 multimodal/VLA research paper + official project page + official repository/model artifact lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 18:55 UTC；no later arXiv revision。Official repository
  records inference code on 2025-02-23, model weights on 2025-02-25, CVPR acceptance on 2025-02-26, training code on 2025-03-09,
  SoM/ToM generation code on 2025-03-16 and processed datasets in April。W08 evidence uses the v1 paper and 2025-02-23 inference
  artifact only；later code, weights and datasets verify lineage/reproducibility boundaries but are not projected backward as event-time artifacts。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13130；https://arxiv.org/html/2502.13130v1；
  https://arxiv.org/pdf/2502.13130v1；https://microsoft.github.io/Magma/；https://github.com/microsoft/Magma。
- **Related Primary Sources:** official `microsoft/Magma-8B` model page and repository training/data-processing paths define later
  artifact behavior；Open-X-Embodiment, SeeClick, Vision2UI, Ego4D, Something-Something v2, ScreenSpot, Mind2Web, AITW,
  SIMPLER and LIBERO define upstream/downstream contracts。They do not independently reproduce Magma's headline results。
- **Access and Verification Status:** Verified；29-page v1 HTML, supplementary methods/tables, project page and official repository are
  accessible。Event-time full-training code, immutable data manifests, exact commit hashes, checkpoints, seeds and end-to-end replay are
  unavailable；those fields remain `Not Disclosed` or later-artifact evidence rather than inferred facts。
- **Full-read Coverage:** read metadata, Abstract/Introduction/Related Work, problem definition, complete SoM/ToM methods and algorithms,
  modeling/pretraining, dataset construction, all UI/robot/spatial/image/video evaluations, mixture/interface ablations, training appendix,
  dataset/evaluation appendix, limitations/responsible-AI guidance and official repository installation/preprocessing/training/inference notes。
- **Original Problem:** a single multimodal agent should preserve general visual-language understanding while grounding and proposing
  actions in both 2D digital and 3D physical environments；raw image-text/video corpora lack action labels, while UI coordinates and
  6/7-DoF robot actions use incompatible spaces。Naively mixing them can create gradient conflict instead of transferable action intelligence。
- **Why the Previous Design Was Reasonable:** separate UI and robot policies keep action schemas, embodiments, sensors and safety cases
  explicit；domain-specific VLA finetuning uses scarce but authoritative trajectories；standard image/video instruction tuning preserves
  semantic breadth。These branches remain easier to validate when tasks, environments or real-time controllers differ materially。
- **Changed Constraint:** VLA trajectory data is scarce relative to image/video corpora, and scaling separate policies repeats pretraining
  while losing cross-domain transfer。The workload therefore needs a shared supervision interface that can harvest spatial-temporal signals
  from heterogeneous observations without pretending that digital clicks and physical controls are the same actuator contract。
- **Mechanism:** convert outputs to textual tokens；encode UI actions as textual coordinates/boxes and quantized robot actions with 256
  rarely used LLM tokens；overlay numbered Set-of-Mark candidates for actionable-region grounding；extend marks through future frames as
  Trace-of-Mark trajectories for planning。CoTracker traces, camera-motion homography, foreground/background motion filtering, K-Means
  sampling and CLIP text-video filtering turn unlabeled videos into surrogate action supervision, then a shared ConvNeXt visual encoder and
  Llama-3 decoder optimize autoregressive verbal, spatial and action tokens over the joint corpus。
- **State Ownership:** source datasets own raw observations/actions and license/provenance；preprocessing owns candidate boxes, marks,
  traces, filtering thresholds and derived-label lineage；model owns token probabilities/proposed action representation, not environment
  truth；OmniParser/DOM/view hierarchy own UI candidate proposals at evaluation；external agent/controller owns execution authority；robot,
  simulator or UI environment owns committed state；human operator owns authorization and intervention。
- **Control Flow / Data Flow:** image/UI/video/robot trajectory → dataset-specific candidate/action extraction → SoM overlay and optional
  CoTracker ToM → camera-motion correction/foreground clustering/filtering → normalized/quantized spatial-action tokens + visual tokens +
  task text → joint autoregressive pretraining → optional domain finetuning → model proposes mark/coordinate/action/trace → external module
  validates and executes → environment outcome is measured。The model prediction never commits a side effect by itself。
- **Implementation Details:** default model uses Llama-3-8B plus ConvNeXt-XXLarge, about 8.6B parameters；global variable-resolution encoding
  supports UI images up to roughly 2000 pixels, with 512 base resolution and at most four crops for UI/image data, one crop for video/robotics。
  Pretraining uses batch 1024, base LR `1e-5`, constant schedule, AdamW and 3 epochs；jobs use at most 32 NVIDIA H100 or 64 AMD MI300 GPUs。
  SoM/ToM uses grid `s=15`, global-motion threshold `eta=2`, foreground threshold `epsilon=2` and CLIP cutoff 0.25。
- **Evaluation Contract:** approximately 39M pretraining samples include 2.7/2.8M UI screenshots, 9.4M image-language-action triplets
  from 326K OXE trajectories/23 datasets, more than 25M samples from about 4M shot-consistent video clips and image-text data。Evaluation
  spans ScreenSpot/VisualWebBench, SIMPLER's Bridge/Google embodiments, Mind2Web/AITW, four WidowX tasks, LIBERO, VSR/BLINK/SpatialEval and
  image/video QA；real robot uses about 50 demonstrations per task and 10 matched-initial-state trials, LIBERO uses 10 trajectories per task。
- **Baselines / Ablations / Sensitivity / Overhead:** compares domain-specific UI-only and OXE-only training, naive joint ACT, full mixed
  data without SoM/ToM and full SoM/ToM；the ablation shows naive UI+robot mixing can hurt both domains, video alone gives limited gains,
  while the shared surrogate interface improves the authors' UI and SIMPLER metrics。ToM validation reports 0.89 precision on 1,320
  YouCook2-BB clips one second ahead。No equal-compute data-mixture sweep, threshold sensitivity, independent replication, seed variance,
  failure-denominator analysis or end-to-end system-cost comparison is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Llama-3-8B + ConvNeXt-XXLarge / about 8.6B；training maximum
  32 H100 or 64 MI300, batch 1024, 3 epochs, base LR `1e-5`, 512 base image resolution and 1/4 crops。Training precision, sequence-token
  length, distributed topology, wall-clock, power/cost, inference concurrency, controller frequency, action latency/tail SLO and safety
  deadline are `Not Disclosed`；repository examples use BF16 or optional 4-bit NF4 inference but are not the paper's training precision contract。
- **What the Evidence Actually Proves:** within the authors' datasets and harnesses, SoM/ToM provides an executable shared supervision
  interface and the controlled mixture ablation supports its contribution over naive heterogeneous mixing。The paper also demonstrates one
  parameter set can be adapted/evaluated across UI, robot and general multimodal tasks without proving those action spaces are operationally identical。
- **What It Does Not Prove:** it does not prove one foundation model is safer or cheaper than modular policies, that visual traces are
  causal plans, that simulator/UI success transfers to open-world deployment, or that all gains come from SoM/ToM rather than data,
  backbone, evaluator and tuning differences。SpatialEval used standard option matching before the official pipeline existed；author-run
  benchmark/SOTA claims and ten-trial robot results are not general production evidence。
- **Limitations / Threats to Validity:** action labels derived from tracking can follow correlated motion rather than causal control；
  homography and thresholds may fail under parallax, occlusion or camera motion；UI evaluation relies on external proposals/ground-truth
  candidates；robot samples and trials are small；dataset mixture/provenance and exact event-time artifact are incomplete。Instructional
  identities/activities are not globally representative, and model/evaluator/data-source coupling limits external validity。
- **Trade-offs / New Failure Modes:** a shared interface expands data reuse and transfer but adds annotation error, quantization loss,
  mark clutter, proposal recall dependence, coordinate/action-token ambiguity, gradient interference, embodiment mismatch and correlated
  model/controller failures。Derived traces increase planning horizon at lower token cost than frame prediction, but can encode camera or
  tracker artifacts as action intent；joint checkpoints also complicate domain-specific rollback, certification and data deletion。
- **Where the Previous Design Still Applies:** separate perception/planner/controller pipelines remain preferable for hard real-time or
  safety-critical robotics；domain-specific UI/robot policies remain simpler when action schemas and distributions are stable；raw
  image/video instruction tuning remains appropriate for semantic understanding；real demonstrations remain authoritative where surrogate
  visual motion cannot determine actuator commands；human approval and independent safety envelopes remain mandatory for side effects。
- **Evolution Relationship:** `Direct Evolution` from domain-specific VLA/data silos to shared surrogate supervision；`Layering /
  Dependency` on trackers, proposal models, dataset lineage and external controllers；`Alternative Branch` versus latent-action/video-token
  pretraining and modular task-specific policies。It does not represent an unconditional replacement of those branches。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Current Ch26）canonical owner；`MULTIMODAL-REPRESENTATION` owns shared spatial/token
  interface semantics, `TRAIN-DATA` owns derived-label provenance/mixture, `AGENT-TOOL` owns authorized digital side effects and
  `PLATFORM-EVALUATION-SYSTEM` owns simulator/real-environment evidence contracts。
- **Target and Adjacent Chapters Read:** read Current Ch25 World Models, Ch26 Embodied AI/VLA and Ch27 Data；verified that Magma's main
  contribution is representation-to-action supervision and bounded execution, not evidence of a causal World Model or autonomous controller。
- **Existing Coverage:** Ch26 already separates action proposal from low-level control, preserves VLM-conditioned/module-specific branches
  and requires human/safety authority；Ch27 already treats derived multimodal/action data as executable training policy with lineage。
  Magma adds a concrete shared-surrogate-interface branch and its failure modes, but whether to refine those arguments remains a later Books Gate decision。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1/project/repository Source Review, six-dimensional score, event-time artifact boundary,
  canonical owner and evaluation/Responsible-AI limits；no Books change。
- **Open Questions:** event-time source/data/checkpoint hashes；full pretraining mixture weights and licenses；tracker/proposal error propagation；
  equal-compute modular baseline；seed/confidence intervals；controller frequency and end-to-end action latency；unsafe-action rejection,
  human override and recovery；cross-embodiment calibration；independent SIMPLER/real-robot reproduction。

### Continuous Diffusion Model for Language Modeling

- **Candidate / Week / Score:** Continuous Diffusion Model for Language Modeling / 2025-W08 / 25/30。
- **Source Family ID:** `kaist-riemannian-diffusion-language-model`。
- **Source Type:** arXiv v1 theoretical/experimental generative-model paper + official implementation/checkpoint lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 08:54 UTC；official repository initial commit
  `342a09c` is also dated 2025-02-17。v2 2025-10-23 and NeurIPS 2025 status are later revision nodes；W08 mechanism and
  evaluation claims are locked to v1, while current code/checkpoints are used only to inspect artifact continuity。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.11564；https://arxiv.org/html/2502.11564v1；
  https://arxiv.org/pdf/2502.11564v1；https://github.com/harryjo97/RDLM；
  https://github.com/harryjo97/RDLM/commits/master/。
- **Related Primary Sources:** D3PM, SEDD, MDLM, MD4, Plaid/BFN and Fisher-Flow papers define discrete/continuous diffusion
  baselines；Text8, LM1B, CIFAR-10 and promoter-DNA datasets define evaluation domains。Most baseline headline values are imported
  from prior papers rather than rerun under one hardware/runtime contract。
- **Access and Verification Status:** Verified；v1 HTML/PDF, all derivations/appendices, generated samples and official code/config
  instructions are accessible。Repository exposes five commits and later checkpoints, but event-time environment lock, raw run logs,
  hardware, exact seeds for headline tables and independent reproduction are unavailable。
- **Full-read Coverage:** read metadata/revisions, Abstract/Introduction, discrete-diffusion and information-geometry background,
  complete Riemannian process/likelihood/objective/approximation derivation, token-sequence factorization, dimension splitting,
  Related Work, all language/image/DNA experiments and analyses, derivation appendix, experimental details, uncurated samples,
  Future Directions, Impact Statement and official repository configs/training/sampling/checkpoint instructions。
- **Original Problem:** discrete diffusion can revise many token positions in parallel but makes irreversible jumps between categorical
  states, discarding continuous refinement signals；unconstrained continuous relaxations ignore categorical geometry, while simplex/flow
  methods had weaker results or poor scaling to large vocabularies。A coherent bridge between these formulations was missing。
- **Why the Previous Design Was Reasonable:** autoregressive factorization gives exact append-only token semantics, stable likelihood
  training, mature KV caching and streaming；masked/discrete diffusion keeps the state categorical and avoids a vocabulary-dimensional
  continuous input。Those branches remain simpler when exact ordering, low-step streaming or large pretrained scale matters more than revision flexibility。
- **Changed Constraint:** the target generation contract wants bidirectional parallel refinement and controllability without giving up
  categorical probability geometry；training must also avoid simulating a high-dimensional manifold SDE for every sample, and large
  vocabularies make a single categorical sphere abruptly convergent and too wide for modest networks。
- **Mechanism:** map categorical probabilities `p_i` to the positive hypersphere by `u_i=sqrt(p_i)` under Fisher-Rao geometry；represent
  masked/uniform discrete transition paths as continuous bridge processes and learn endpoint-token probabilities rather than divergent
  terminal drift。Mix masked and uniform paths, train a cross-entropy likelihood-bound surrogate with importance sampling over difficult
  times, approximate bridge marginals by a Riemannian normal whose parameters are precomputed from low-dimensional radial projections,
  and split a vocabulary index into base-`b` digits so generation occurs on a product of smaller manifolds。
- **State Ownership:** tokenizer owns categorical vocabulary/BOS/EOS and index-to-digit identity；noise scheduler owns path/time state；
  precomputed radial tables own approximate transition parameters；denoiser owns provisional endpoint probabilities for all positions；
  sampler/SDE integrator owns mutable continuous states and step budget；final projection owns committed categorical tokens；runtime owns
  sequence length, stopping and artifact identity。Intermediate hypersphere state is not a committed token sequence。
- **Control Flow / Data Flow:** token sequence → one-hot/category distribution → square-root hypersphere coordinates or split digit
  coordinates → sample time and approximated bridge state from cached radial parameters → Diffusion Transformer predicts endpoint-token
  probabilities → cross-entropy/importance-weighted update；generation starts from masked/uniform mixture → repeated manifold drift/noise
  steps update all positions → fixed BOS/EOS constrain length → terminal projection yields discrete tokens → likelihood/quality evaluation。
- **Implementation Details:** language experiments use 12-layer Diffusion Transformers with RoPE；Text8 has 92.4M parameters,
  vocabulary 28 and length 256；LM1B has 110M parameters, 768 hidden size, 12 heads, BERT-base-uncased tokenizer and length 128。
  Both train 1M iterations with batch 512, AdamW and EMA 0.9999；repository uses Python 3.9/PyTorch 2.3.1 and examples show one GPU
  for Text8, four GPUs plus three digit tokens for LM1B。Precomputed radial approximation is claimed about 50x faster than per-step simulation。
- **Evaluation Contract:** Text8 fixed 90M/5M/5M characters and BPC；LM1B fixed tokenizer/length 128 and PPL/NLL；CIFAR-10
  pixel modeling uses a 35M/10-layer model, 100K steps and batch 128；promoter DNA uses 100K length-1024 sequences, a 13.3M
  20-layer CNN, 88,470/3,933/7,497 split, 100K steps, batch 256 and 300 generation steps。Language tables compare 92M/110M-class models。
- **Baselines / Ablations / Sensitivity / Overhead:** compares AR/any-order AR, discrete diffusion, continuous diffusion and flow
  baselines；ablates drift-MSE versus CE versus CE+time importance sampling, high-dimensional manifold versus top-k features versus
  dimension splitting, and simulated versus approximated bridge distributions via MMD。It does not report equal-hardware latency,
  generation-step sensitivity, quality-speed Pareto, memory/communication cost, repeated seeds or large-model scaling。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/length/batch contracts are 92.4M/256/512 for Text8
  and 110M/128/512 for LM1B；paper hardware, precision, learning-rate value, training wall-clock, sampling step count for language,
  memory, batch/concurrency at inference, TTFT/streaming cadence, throughput and SLO are `Not Disclosed`。Repository GPU counts are
  runnable examples, not a cross-baseline performance contract。
- **What the Evidence Actually Proves:** the paper supplies a mathematically explicit connection between categorical diffusion paths
  and continuous flows on the statistical manifold；its v1 experiments show the proposed geometry, radial approximation, CE objective,
  time sampling and dimension splitting form a trainable small/medium-scale system that improves reported likelihood metrics over the
  selected diffusion baselines in those datasets。The approximation MMD and ablations support the internal mechanism, not production speed。
- **What It Does Not Prove:** it does not prove diffusion language modeling is faster or better than AR at equal compute, memory,
  hardware and delivered quality；it does not demonstrate instruction following, reasoning, long context, controllable generation,
  large-parameter scaling, online adaptive step budgets or serving integration。Imported baseline scores and approximate likelihood bounds
  are not an independent end-to-end reproduction or exact wall-clock comparison。
- **Limitations / Threats to Validity:** language models are only 92M/110M with length 128/256 and dated datasets；paper has no explicit
  limitations section beyond future work；bridge sampling uses an approximation and calibrated scale for small dimensions；dimension
  splitting introduces a new token code whose digit errors may correlate；generated LM1B samples visibly contain poor grammar/repetition；
  hardware, seeds, variance, language sampling steps and safety/content behavior are omitted。
- **Trade-offs / New Failure Modes:** continuous mutable states preserve revision signals and allow parallel-position refinement, but
  require multiple full-sequence denoiser passes, numerical manifold operations, scheduler/radial-table identity and a terminal commit。
  Dimension splitting makes large vocabularies learnable while multiplying per-token subcoordinates and permitting invalid/inconsistent
  digit combinations；approximate bridge tables reduce training cost but add calibration drift；non-append-only output complicates KV reuse,
  streaming, prefix caches and downstream side-effect boundaries。
- **Where the Previous Design Still Applies:** AR remains preferable for mature large-scale checkpoints, streaming, low-latency short
  output and append-only tool protocols；discrete masked diffusion remains simpler when categorical semantics and established samplers are
  sufficient；unconstrained latent/flow methods may suit domains with natural continuous embeddings；small vocabularies do not require
  dimension splitting, and exact simulation remains useful for validating the approximation。
- **Evolution Relationship:** `Direct Evolution` from discrete categorical jumps to geometry-preserving continuous refinement；`Principle
  Reuse` of diffusion mixture/flow matching and Fisher-Rao geometry；`Alternative Branch` to AR and discrete masked diffusion。It is not
  evidence of a universal sequence-generation replacement or a deployed runtime transition。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24）canonical owner；`MODEL-SAMPLING` owns final stochastic output
  policy, `TRAIN-PRETRAINING` owns objective/data execution, and `INFER-KV-CACHE` / `INFER-EXECUTION` own mutable-state/cache/runtime consequences。
- **Target and Adjacent Chapters Read:** read Current Ch23 Multimodal Representation, Ch24 Generative Paradigms and Ch25 World Models；
  verified RDLM belongs to the AR↔discrete/continuous diffusion branch and commit semantics, not World Models or deployed inference evidence。
- **Existing Coverage:** Ch24 already owns probability factorization, mutable token state, masked/block diffusion, correction and commit
  boundaries, and explicitly warns that fewer serial steps do not prove lower latency。RDLM adds a geometry-preserving continuous branch,
  simulation-free training approximation and dimension-splitting trade-off；Books refinement remains a later Gate decision。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked Source Review, score, event-time commit, mechanism/evaluation limits and canonical
  owner；kept v2/NeurIPS/checkpoints as later lineage and made no Books change。
- **Open Questions:** v1 exact environment/run hashes；language sampler steps and quality-latency frontier；hardware/precision/energy；
  dimension-splitting invalid-code rate and ablation over base `b`；approximation error at generation scale；large-model/long-context
  scaling；conditional/instruction/reasoning quality；mutable-state cache protocol；independent reproducibility and safety evaluation。

### Logic-RL

- **Candidate / Week / Score:** Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning / 2025-W08 / 24/30。
- **Source Family ID:** `logic-rl-rule-verifier-post-training`。
- **Source Type:** arXiv v1 reasoning-RL paper + official code/data/reward artifact。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 17:49 UTC；arXiv currently exposes only v1。
  The official repository is retained as artifact lineage, but its event-time initial commit was not recoverable from the public pages read；
  later README news and current code are not projected backward as proof of the exact W08 run。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14768；https://arxiv.org/html/2502.14768v1；
  https://arxiv.org/pdf/2502.14768v1；https://github.com/Unakar/Logic-RL；
  https://github.com/Unakar/Logic-RL/blob/main/main_grpo.sh；
  https://github.com/Unakar/Logic-RL/blob/main/verl/utils/reward_score/kk.py；
  https://github.com/Unakar/Logic-RL/blob/main/examples/data_preprocess/kk.py。
- **Related Primary Sources:** the Knights-and-Knaves generator paper supplies the procedural task；REINFORCE++, PPO, GRPO and
  DeepSeek-R1/DeepSeekMath define the compared online-RL branches；AIME 2021–2024 and AMC 2022–2023 supply cross-domain evaluation sets。
  These sources define lineage and baselines, not an independent reproduction of Logic-RL。
- **Access and Verification Status:** Verified with artifact mismatch；v1 metadata, complete HTML/PDF and current official repository are
  accessible。The paper reports modified REINFORCE++, train batch 8, rollout `N=8`, max response 4096 and learning rate `4e-7`；the
  public `main_grpo.sh` instead selects GRPO, train batch 64, rollout `n=16`, max response 2048 and learning rate `3e-7`。Therefore the
  repository proves an executable related recipe, not reproduction of the paper's headline run。
- **Full-read Coverage:** read metadata and sole revision；Abstract/Introduction；procedural data, prompt, format/answer reward and
  modified REINFORCE++ equations；training schedule；K&K, algorithm, token-correlation, aha-moment, OOD math, RFT, curriculum and
  response-length experiments；Discussion/Future Work；Related Work；base-versus-instruct and qualitative appendices；repository README,
  training launcher, preprocessing and reward implementation。
- **Original Problem:** reasoning-oriented rule RL was difficult to study reproducibly because large released models did not expose the
  full training loop, natural math corpora mix uncontrolled difficulty, and sparse outcome reward allows shortcut formats and reward hacking。
- **Why the Previous Design Was Reasonable:** SFT/RFT directly imitates accepted trajectories and is stable, cheap and offline；PPO uses a
  learned critic for lower-variance credit；GRPO removes the critic with same-prompt group statistics；natural math data offers real task
  diversity。Those choices remain valid when demonstrations are trustworthy, a critic is affordable, or procedural rules cannot express quality。
- **Changed Constraint:** the experiment needs a small, controllable and exactly checkable reasoning environment where difficulty can be
  varied, answer correctness can be computed automatically, and online policy exploration can be separated from corpus memorization。
- **Mechanism:** generate unique-solution Knights-and-Knaves puzzles with 2–8 people and Boolean-composition difficulty；train on fewer
  than 5K 3–7-person examples；force exactly one ordered `<think>`/`<answer>` pair；combine binary format reward with exact parsed-role
  reward；optimize Qwen2.5-7B-Instruct-1M using modified REINFORCE++, moving reference KL from token reward into the loss and using the
  non-negative ratio-minus-log-ratio KL estimator；sample mixed difficulty for 3600 steps rather than requiring staged curriculum。
- **State Ownership:** generator owns puzzle identity, statements, difficulty and unique ground truth；prompt/template owns response schema；
  rollout policy and its version own sampled trajectories/log probabilities；reward parser owns tag order and complete name-role mapping；
  reference policy owns the KL anchor；optimizer owns policy update state；evaluation harness owns K&K split/perturbation and AIME/AMC identity。
- **Control Flow / Data Flow:** procedural puzzle + ground truth → base/instruct chat template → current policy samples a group of responses
  at temperature 0.7 → parser validates exactly-once ordered tags → exact role matcher emits format and answer rewards → return/advantage and
  reference KL form the policy loss → update policy → periodically evaluate in-distribution/OOD K&K, perturbed training examples and external math sets。
- **Implementation Details:** the paper trains 3600 steps with constant LR `4e-7`, temperature 0.7, train batch 8, eight rollouts, KL
  coefficient 0.001 and maximum response 4096；Qwen2.5-7B-Instruct-1M is the selected starting checkpoint。The repository uses verl,
  vLLM 0.6.3, PyTorch 2.4.0/CUDA 12.1, FSDP offload and documents 4×A100 80GB, but its published launcher is a different GRPO recipe
  with placeholders and the conflicting parameters listed above。
- **Evaluation Contract:** K&K accuracy spans 2–8-person puzzles, with 3–7 used for training and 8-person treated as OOD；local
  inconsistency memorization perturbs Boolean expressions and statement order；AIME 2021–2024 and AMC 2022–2023 test cross-domain math；
  training curves compare reward, validation accuracy, response length and KL。Exact evaluation sample counts, decoding repetitions,
  seeds, confidence intervals and event-time model-selection protocol are `Not Disclosed`。
- **Baselines / Ablations / Sensitivity / Overhead:** compares Qwen base/instruct and several external models on K&K；compares PPO,
  GRPO and REINFORCE++ training curves；RFT versus RL under the proposed memorization score；curriculum versus mixed difficulty；positive
  and negative length-growth examples；token/language correlations。It lacks equal-code/hyperparameter disclosure for algorithm comparisons,
  reward-component ablation, robust seed sensitivity, parser-adversarial tests, compute-normalized sample efficiency and artifact reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper model is Qwen2.5-7B-Instruct-1M；length 4096, batch 8,
  rollout group 8, 3600 steps, LR `4e-7`, temperature 0.7 and KL 0.001。Paper hardware, precision, optimizer detail, wall-clock, tokens,
  evaluation concurrency and SLO are `Not Disclosed`；repository documents 4×A100 80GB for its conflicting GRPO launcher, so the reported
  138% PPO slowdown is not a portable hardware/runtime result。
- **What the Evidence Actually Proves:** under this procedurally verified 7B setup, rule rewards plus strict output parsing support stable
  online training and large gains on the authors' K&K evaluation, including the held-out 8-person level；their curves show response length
  alone is neither necessary nor sufficient for higher validation reward, and staged curriculum offers little practical gain over the mixed
  schedule in this experiment。The study also provides useful negative evidence against interpreting a single sudden verbal pattern as an “aha moment”。
- **What It Does Not Prove:** it does not establish that RL generally learns abstract reasoning while SFT merely memorizes, that specific
  thinking words cause success, that language mixing causes failure, or that Logic-RL transfers broadly beyond the reported AIME/AMC curves；
  it does not prove REINFORCE++ generally dominates GRPO/PPO, because code/configuration and equal-compute conditions are incomplete；it
  does not validate process-level reasoning correctness, production safety or long-horizon Agent behavior。
- **Limitations / Threats to Validity:** one synthetic puzzle family and one main 7B checkpoint dominate the evidence；format reward and
  exact parser may shape visible reasoning style；the claimed “nearly unhackable” reward lacks adversarial proof；qualitative examples are
  selected；token associations are correlational；the memorization metric covers only two local perturbations；AIME/AMC results are presented
  mainly as relative curves；hardware, seeds and uncertainty are absent；the official launcher does not reproduce the paper recipe。
- **Trade-offs / New Failure Modes:** deterministic verifiers make rollout scalable and auditable but narrow the objective to what the
  parser can see；strict tags suppress shortcut outputs while adding format brittleness and schema gaming；online exploration can discover
  better trajectories but multiplies generation cost and policy-version state；longer responses improve search capacity in some runs while
  increasing token cost and opportunity for drift；synthetic controllability reduces ambiguity but risks generator/template overfitting。
- **Where the Previous Design Still Applies:** SFT/RFT remains appropriate for trusted demonstrations, low-cost offline iteration and
  open-ended quality without exact checkers；PPO remains useful when a learned value function can improve temporal credit；GRPO remains a
  valid critic-free branch when group rollouts are cheap and implementation is verified；human/process evaluation remains necessary when
  final-answer equivalence does not establish safe or faithful reasoning。
- **Evolution Relationship:** `Direct Evolution` from offline trajectory imitation to rule-verified online exploration；`Alternative Branch`
  among PPO, GRPO and REINFORCE++ estimators；`Layering / Dependency` on procedural generation, parser authority, policy/reference identity
  and evaluation harness。It is not a universal succession in which rule RL replaces SFT or learned reward models。
- **ROADMAP Node:** `TRAIN-GRPO`（Current Ch33）canonical owner because the durable contribution is critic-free/grouped online-RL and
  verifier lifecycle；`TRAIN-PPO` owns learned-critic and clipped-ratio comparison, `TRAIN-RLHF` owns reward/KL authority, and
  `PLATFORM-EVALUATION-SYSTEM` owns independent cross-domain evidence。
- **Target and Adjacent Chapters Read:** read Current Ch32 PPO, Ch33 GRPO and Ch34 DPO；verified that Logic-RL belongs in the online
  verifier/rollout branch, while DPO remains an offline preference-pair alternative and the paper's algorithm ranking is contract-specific。
- **Existing Coverage:** Ch33 already explains group rollouts, verifier exploit surfaces, sequence-level credit, policy identity and the
  principle that named GRPO implementations may change KL/reduction semantics；Ch32 preserves critic-based PPO and KL-estimator boundaries；
  Ch34 preserves offline DPO。Logic-RL adds a bounded procedural-verifier case and artifact-mismatch lesson, but Books refinement is deferred。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked paper/artifact review, 24/30 score, explicit paper-versus-launcher mismatch,
  causal/evaluation limits and canonical owner；no Books change。
- **Open Questions:** event-time repository commit and exact paper configuration；paper code/hash and optimizer/precision；K&K split sizes,
  seeds and confidence intervals；absolute AIME/AMC scores and decoding contract；equal-compute PPO/GRPO/REINFORCE++ comparison；reward
  hacking red-team；process-validity verifier；cross-generator/domain/model scaling；independent reproduction of the claimed transfer。

### SWE-Lancer

- **Candidate / Week / Score:** SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering? /
  2025-W08 / 28/30。
- **Source Family ID:** `openai-swelancer-real-world-coding-evaluation`。
- **Source Type:** arXiv benchmark paper + official public benchmark/container artifact + private-holdout lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 18:41 UTC and v2 submitted 2025-02-19 06:48 UTC；
  W08 claims are locked to v2, the last revision inside the ISO week。v3 (2025-02-24) and v4 (2025-05-29) are later
  revision nodes。The original repository was archived 2025-07-18 and redirected to OpenAI Frontier Evals；the later runnable
  set documents 198 adjusted offline tasks rather than all 237 Diamond IC tasks, so it is not silently substituted for the W08 artifact。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.12115；https://arxiv.org/pdf/2502.12115v2；
  https://github.com/openai/SWELancer-Benchmark；https://github.com/openai/frontier-evals/tree/main/project/swelancer。
- **Related Primary Sources:** SWE-bench/SWE-bench Verified define repository-task and unit-test lineage；Expensify issue/proposal/
  payout records define task provenance；Playwright supplies hidden end-to-end browser execution。Later Frontier Evals migration is
  artifact evolution only, not evidence for the original reported model runs。
- **Access and Verification Status:** Verified with historical-artifact limitation；v2 full PDF, all appendices and official repository
  lineage are accessible。Original public repository contents and image are no longer exposed at a pinned event-time commit through the
  current landing page；the private `$499,200` holdout, proprietary model execution and all hidden tests are not publicly inspectable。
- **Full-read Coverage:** read metadata and revision history；Introduction/Related Work；task definitions, construction, payouts and
  E2E grading；experiment setup and all main results；pass@k, reasoning-effort and user-tool ablations；Discussion, Limitations, Future
  Work, Impact Statement；appendices on category/contamination, benchmark comparison, scaffold/hardware, curation and test review,
  grader hacking, prompts, qualitative trajectories, user-tool use, holdout construction, dataset composition and example tasks；official
  archived/migrated repository documentation。
- **Original Problem:** code-generation and repository benchmarks can be saturated, narrowly self-contained or selected around existing
  unit tests；they often omit full-stack user behavior, management choices, long issue context, tool latency and the economic heterogeneity
  of real work。A high unit-test score therefore need not measure whether an Agent can deliver a complete commercial feature or bug fix。
- **Why the Previous Design Was Reasonable:** HumanEval-style functions and SWE-bench unit tests are cheap, deterministic, redistributable
  and easy to run across many models；single repositories and fixed patches simplify contamination analysis；component tests precisely
  localize failures。They remain valuable for fast regression and mechanism diagnosis even when they do not represent full product behavior。
- **Changed Constraint:** the evaluation subject is now a coding Agent operating on a large full-stack product snapshot with terminal tools,
  multi-file dependencies and delayed UI evidence；success must include actual user workflow and, for manager tasks, selecting among plausible
  proposals。The harness must prevent future-commit/internet leakage while preserving realistic code browsing and debugging opportunity。
- **Mechanism:** curate 1,488 previously paid Expensify/Upwork tasks；split 764 IC patch tasks and 724 manager proposal-selection tasks；
  freeze the pre-fix codebase；run agents without Internet/Git remote in a Docker environment；grade IC patches using hidden Playwright E2E
  tests written and triple-reviewed by professionals；grade manager choices against the historical accepted proposal, independently checked
  at 99% agreement；expose an optional user tool that executes a scripted workflow and returns trace/HTML/log artifacts without the final grader verdict。
- **State Ownership:** task record owns issue, proposals, historical price and pre-fix commit；container image owns dependencies and network
  boundary；Agent scaffold owns tool calls, edits and submitted patch/decision；user tool owns delayed browser trajectory and screenshots；
  hidden E2E suite owns executable IC verdict；historical manager choice plus validation owns proposal verdict；split registry owns public versus
  private contamination boundary；run record owns model, reasoning effort, temperature, attempt count, timeout and payout aggregation。
- **Control Flow / Data Flow:** issue/proposals + frozen repository + price → isolated no-network container → model browses and edits or
  selects a proposal → optional scripted user workflow emits trace/HTML/log evidence → IC patch is applied and hidden E2E tests execute, or
  manager JSON is compared with validated historical choice → per-task pass/fail → pass@1/pass@k, task count and payout-weighted aggregates →
  category, tool and test-time-compute analysis。
- **Implementation Details:** v2 uses Microsoft Azure Standard D2as v4 VMs with 2 vCPUs/8GB RAM and a prebuilt Docker image；the appendix
  separately states 64GB shared-memory and 192GB container maximum, a resource-description inconsistency that cannot be resolved from the
  paper。Agents receive at most 100 tool calls and 3 hours, temperature 1.0, no Internet or future commits and normally one rollout；the user
  tool may take 90–120 seconds and writes Playwright traces/screenshots/HTML to the workspace。
- **Evaluation Contract:** the full set contains 764 IC tasks worth `$414,775` and 724 manager tasks worth `$585,225`；Diamond contains
  237 IC tasks worth `$236,300` and 265 manager tasks worth `$264,500`；the remaining `$499,200` is private。IC requires all applicable
  hidden E2E tests to pass；manager requires the accepted proposal。Results report pass@1, payout/earn rate, task category/price slices,
  pass@k for GPT-4o/o1, o1 reasoning effort and user-tool on/off；each default run is one sample, so variance is explicitly unresolved。
- **Baselines / Ablations / Sensitivity / Overhead:** evaluates `gpt-4o-2024-08-06`, o1 at low/medium/high reasoning effort and
  `claude-3-5-sonnet-20240620` with a common basic scaffold；compares IC versus manager, public versus full set, tool on/off, price/task
  slices and up to seven attempts。It does not isolate prompt/scaffold variants, repeated pass@1 variance for all models, equal token/API cost,
  grader coverage sensitivity, repository diversity or alternative payout weighting；private-holdout reproducibility is unavailable。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** agent CPU/container contract is 2 vCPU/8GB VM, 100 tool calls,
  3 hours, temperature 1.0 and pass@1；provider hardware, model precision, context actually consumed, token budget, API concurrency, wall-clock
  distribution, cost and production SLO are `Not Disclosed`。The 90–120-second user-tool latency is a harness observation, not an inference SLO。
- **What the Evidence Actually Proves:** the authors constructed a large, economically weighted set of one-product freelance tasks with
  professional hidden E2E grading and a public/private contamination split；under the disclosed 2025 scaffold, tested frontier models solved
  a minority of IC tasks and more manager tasks。More attempts and higher o1 reasoning effort improved this benchmark；qualitative traces
  support the diagnosis that models often localize files quickly but fail to understand complete root cause or verify all product behavior。
- **What It Does Not Prove:** payout is not a calibrated causal measure of task difficulty, engineering value or labor displacement；the
  experiment does not show what the same models achieve with different scaffolds, clarifying questions, multimodal issue evidence, human
  collaboration or production access；one Expensify/Upwork population does not represent infrastructure, backend or long-term engineering；
  hidden E2E pass does not prove maintainability, security or absence of regression beyond test coverage。
- **Limitations / Threats to Validity:** one repository/platform and mostly frontend bug fixes；freelance work is more bounded than full-time
  ownership；text-only agents cannot view issue videos/screenshots or generated screenshots；no clarification channel；public-task contamination
  remains possible；one rollout has high variance；manager ground truth may encode historical organizational preference；tests can miss unusual
  correct solutions；private holdout and event-time artifact are not fully auditable；current public runner dropped 39 original Diamond IC tasks。
- **Trade-offs / New Failure Modes:** hidden E2E workflows reduce trivial unit-test gaming and measure integration behavior, but are expensive,
  slow, stateful and susceptible to browser flakiness, environment drift and incomplete scenario coverage；real payouts add an intuitive weight
  while importing market/team/time confounders；private tasks reduce contamination while preventing full external reproduction；the user tool
  increases observability but adds delayed traces, timeout policy and an affordance that different models exploit unequally。
- **Where the Previous Design Still Applies:** unit/component tests remain the correct first gate for cheap deterministic regression and root-
  cause localization；SWE-bench-style multi-repository samples better test repository diversity；public benchmarks remain necessary for
  reproducibility；human review, code review and security testing retain authority for ambiguous requirements, maintainability and high-impact
  deployment；single-attempt evaluation is appropriate where retries are operationally disallowed, while pass@k measures search coverage only。
- **Evolution Relationship:** `Direct Evolution` from self-contained/unit-test coding evaluation to full-stack hidden E2E and workflow state；
  `Layering / Dependency` on frozen artifacts, container/network isolation, browser tooling and professional verification；`Alternative Branch`
  between public reproducibility and private contamination resistance。It does not replace component tests or human engineering review。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66）canonical owner；`AGENT-TOOL` owns action/trace affordance,
  `AGENT-WORKFLOW` owns durable coding execution, `PLATFORM-SECURITY` owns sandbox/permission risk, and `PLATFORM-COST` owns compute/API
  accounting rather than using payout as service cost。
- **Target and Adjacent Chapters Read:** read Current Ch65 KAI Scheduler, Ch66 Evaluation System and Ch67 Monitoring；verified that the
  stable contribution is an evaluation subject/environment/scorer contract, not a scheduler, telemetry pipeline or claim about production economics。
- **Existing Coverage:** Ch66 already binds Agent evaluation to model/scaffold/tool/environment identity, distinguishes pass@k search from
  repeated reliability, and evolves final-answer scoring into executable artifact, process and environment evidence；it also preserves final/
  component tests beside stateful E2E gates。SWE-Lancer adds a bounded real-task/E2E/payout case, but Books refinement remains deferred。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v2-locked 30-field review, score, repository migration/subset boundary, owner and exact
  workload contract；no Books change。
- **Open Questions:** v1→v2 content diff and event-time repository/image digest；why VM and container memory disclosures conflict；original
  237-task public image/test availability；hidden-test flakiness and false-rejection rate；independent reproduction；payout/difficulty calibration；
  scaffold/token/API-cost normalization；multimodal and clarification ablations；cross-repository infrastructure/backend coverage；private-holdout governance。

### TrustGen

- **Candidate / Week / Score:** On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and
  Perspective / 2025-W08 / 26/30。
- **Source Family ID:** `trustgen-dynamic-trustworthiness-evaluation`。
- **Source Type:** arXiv survey/benchmark paper + official project page + open-source evaluation toolkit。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 06:20 UTC；v2 2025-04-28、v3
  2025-05-11、v4 2025-09-30、v5 2026-05-15。W08 claims are locked to v1；the later NAACL 2025 demo
  paper, ICLR 2026 version and current toolkit are revision/artifact lineage, not silently back-projected evidence。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.14296；https://arxiv.org/pdf/2502.14296v1；
  https://howiehwong.github.io/TrustGen.pdf；https://trustgen.github.io/；
  https://github.com/TrustGen/TrustEval-toolkit。
- **Related Primary Sources:** TrustLLM supplies the predecessor static LLM trustworthiness benchmark；the later
  TrustEval NAACL demo documents toolkit evolution；official repository history records continued pipeline and bug-fix
  changes after W08。They are used to define lineage and artifact boundaries, not to upgrade v1 results。
- **Access and Verification Status:** Verified with event-time artifact limitation；arXiv metadata, the author-hosted
  full paper, official project page and repository are accessible。arXiv HTML for v1 was unavailable；the repository does
  not expose a release/tag or immutable dataset manifest tied to the 2025-02-20 paper snapshot, and its visible history
  continues from 2025-02-23 onward, so current `main` is not treated as the exact v1 implementation。
- **Full-read Coverage:** read metadata/revision history；Abstract, Introduction and Background；corporate/governance
  review and related benchmarks；all guidelines；TrustGen design, three modules and model table；T2I, LLM and VLM
  evaluation sections across truthfulness, safety, fairness, robustness, privacy, ethics and advanced-risk dimensions；
  other generative modalities and downstream-application survey；all discussion subsections and Conclusion；relevant
  appendices containing model identities, prompt templates, generated examples and evaluation instructions；official
  project, toolkit pipeline, documentation and commit lineage。
- **Original Problem:** static trustworthiness suites age quickly, can leak into training and usually measure one modality
  or one risk taxonomy。Separately maintained safety, fairness, privacy and robustness scores cannot explain whether
  changes reflect a new model, a new population, a new prompt transformation or a changed evaluator。
- **Why the Previous Design Was Reasonable:** frozen datasets and deterministic scorers are cheap, comparable and easy
  to reproduce；single-dimension suites provide sharper diagnosis and stable longitudinal regression。They remain the
  correct first gate when the population and threat model are stable, and they avoid letting a generator or judge mutate
  the test while it is being used for a release decision。
- **Changed Constraint:** foundation models evolve rapidly across text, image and vision-language interfaces；new attacks,
  social expectations and deployment contexts appear after a benchmark freezes；prompt form itself changes results。
  Evaluation therefore needs a versioned construction pipeline rather than only a static file and terminal score。
- **Mechanism:** derive a cross-disciplinary guideline/taxonomy, then instantiate a three-stage pipeline：Metadata Curator
  acquires or refreshes source material through dataset pools, web-browsing agents or model generation；Test Case Builder
  converts it into labeled cases using programmatic, attribute-guided, principle-guided or LLM-based generation；Contextual
  Variator paraphrases, changes length or changes question format to probe prompt sensitivity。Human checks are inserted
  for selected generated data；model responses are scored with dimension-specific programmatic, model-based or dataset
  metrics and normalized before per-dimension/overall reporting。
- **State Ownership:** guideline/taxonomy revision owns the intended trust dimensions；metadata source and curator revision
  own the candidate population；dataset-pool snapshot owns frozen inputs；builder prompt/code/model own generated cases and
  labels；variator prompt/model own contextual variants；target-model/API configuration owns responses；metric/judge prompt
  and model own verdicts；human-review protocol owns sampled validation；report aggregation owns normalized dimension scores。
- **Control Flow / Data Flow:** governance/domain sources + dataset pools + generated metadata → curator and deduplication →
  dimension-specific case builder → optional human validation → contextual variants → 8 T2I, 19 LLM and 10 VLM targets in
  the v1 tables → programmatic/model/human-assisted scorers → normalized per-task and per-dimension evidence → modality-level
  aggregate and qualitative cross-dimension discussion。
- **Implementation Details:** curator strategies are Web-Browsing Agent, Dataset Pool Maintainer and Model Generation；case
  builders use Attribute-Guided, Principle-Guided, Programmatic and LLM paraphrasing branches；the variator supports format,
  length and paraphrase transformations。The paper reuses established datasets, retrieves current Wikipedia/fact-checking
  material, generates adversarial/privacy/fairness cases and uses task-specific judges such as VLM/LLM evaluators；the toolkit
  exposes metadata download, dynamic generation, variation, response generation, judging, metric and HTML-report stages。
- **Evaluation Contract:** v1 evaluates 8 T2I, 19 LLM and 10 VLM configurations；coverage differs by modality rather than
  assuming every dimension is measurable everywhere。Metrics are transformed so higher is better, scaled to 0–100 and then
  averaged for summary views；case-level contracts include accuracy, refusal/compliance, perturbation consistency, leakage,
  preference/fairness and judge-based image/text criteria。The paper itself warns that a high aggregate does not establish
  reliability or trustworthiness in every context。
- **Baselines / Ablations / Sensitivity / Overhead:** compares dynamic QA/fact-checking data with predecessor static pools,
  original versus perturbed/context-varied cases and open/proprietary or size-related slices across three modalities。It does
  not provide a controlled ablation for curator versus builder versus variator, longitudinal contamination measurement,
  alternate judge families, human-review sample-size sensitivity, aggregation weights, generation cost or repeated full-pipeline
  variance。The LLM robustness section excludes several APIs from one open-ended analysis because temperature could not be
  fixed at zero, directly exposing provider-configuration confounding。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** target model names/versions are tabulated, but
  provider hardware, numerical precision, exact context/output lengths, batch, concurrency, end-to-end latency, generation/
  judge cost, energy and production SLO are `Not Disclosed`。Temperature is set to zero where supported；some proprietary
  APIs do not permit that setting。No hardware-normalized performance claim is accepted。
- **What the Evidence Actually Proves:** the authors operationalized a broad trustworthiness taxonomy into a modular,
  multi-modal test-construction and scoring workflow, published substantial task-level results and an implementation lineage,
  and demonstrated that model rankings and weaknesses vary by dimension, modality, prompt form and evaluator contract。The
  paper also supplies direct evidence that an aggregate trust score can hide bottlenecks and utility/safety interactions。
- **What It Does Not Prove:** generated freshness does not prove absence of training contamination；paraphrase diversity does
  not prove deployment representativeness；LLM/VLM judges and human spot checks are not universal ground truth；an arithmetic
  mean across heterogeneous dimensions is not a calibrated deployment-risk probability；cross-sectional model comparisons do
  not prove that open weights, scale or a vendor policy caused the observed result；the design does not demonstrate continuous
  production operation or reduced real-world harm。
- **Limitations / Threats to Validity:** taxonomy and guideline choices are normative and stakeholder-dependent；different
  modalities receive different tasks and metrics；synthetic/test-generation models can reproduce their own blind spots；judge
  identity and prompt sensitivity introduce correlated error；dataset pool, web content and API models drift；sample sizes,
  human-review agreement, seeds and costs are unevenly disclosed；temperature is not controlled for all providers；the overall
  average suppresses severity and critical slices；event-time code/data hashes and an independent reproduction are absent。
- **Trade-offs / New Failure Modes:** dynamic generation improves freshness and adaptation but gives the evaluator mutable
  state, making historical comparability, cache identity, provenance and rollback harder；cross-modality normalization enables a
  compact dashboard but can imply false commensurability；LLM-assisted construction scales coverage while creating generator-
  judge self-confirmation, prompt injection and label drift；human validation raises confidence but adds cost and sampling bias。
- **Where the Previous Design Still Applies:** frozen golden suites remain preferable for cheap deterministic regression and
  release-blocking invariants；domain-specific expert tests remain authoritative for medical, legal, physical or security risk；
  executable verifiers should replace model judges where behavior is formalizable；human red teams remain necessary for novel
  semantic attacks；separate dimension scores and severity slices should be preserved even when an overview score is shown。
- **Evolution Relationship:** `Direct Evolution` from static single-modality benchmark files to versioned metadata → case →
  contextual-variation pipelines；`Layering / Dependency` on frozen suites, evaluator calibration, human review and artifact
  provenance；`Alternative Branch` between longitudinal comparability and continually refreshed discovery。Dynamic evaluation
  extends rather than invalidates static regression suites。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66）canonical owner；`PLATFORM-SECURITY` owns threat
  model and enforcement, `PLATFORM-MONITORING` owns production observation, and modality chapters own representation-specific
  failure mechanisms rather than the evaluation control plane。
- **Target and Adjacent Chapters Read:** read Current Ch65 KAI Scheduler, Ch66 Evaluation System and Ch67 Monitoring；also
  checked Ch71 Multi-Tenancy, Ch72 Security and Ch73 Production Best Practice to keep evaluation evidence separate from policy
  authority, telemetry and release enforcement。
- **Existing Coverage:** Ch66 already defines `intended use → subject/population/failure taxonomy → versioned evidence →
  scorer/uncertainty → decision`；it binds dataset/environment/scorer revisions, contamination limits, dynamic versus frozen
  suites and judge disagreement。TrustGen supplies a strong historical case for that evolution, but does not expose a new durable
  mechanism missing from the chapter；the Source Family must still be considered explicitly at the later Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked 30-field review, final score, revision/artifact boundary, evaluation
  contract and owner；no Books change。
- **Open Questions:** exact v1 repository commit, environment and dataset hashes；v1→v5 taxonomy/data/result diff；per-module
  ablations；human validation sampling/agreement；judge calibration and cross-family transfer；curator provenance/deletion and
  web-content poisoning；severity-aware aggregation；cost/latency/energy；longitudinal rank stability；independent reproduction；
  which dynamic cases should be promoted into an immutable release-blocking suite。

### MMTEB

- **Candidate / Week / Score:** MMTEB: Massive Multilingual Text Embedding Benchmark / 2025-W08 / 27/30。
- **Source Family ID:** `mmteb-multilingual-embedding-evaluation`。
- **Source Type:** arXiv benchmark paper + versioned result artifact + official MTEB evaluation repository。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 10:13 UTC；v2 2025-04-08、v3
  2025-06-08、v4 2025-11-13。W08 facts and counts are locked to v1；later ICLR acceptance, paper revisions and
  current multimodal MTEB behavior are lineage evidence, not silently back-projected event-time facts。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13595；https://arxiv.org/html/2502.13595v1；
  https://arxiv.org/pdf/2502.13595v1；
  https://github.com/embeddings-benchmark/results/tree/9a79f7e07542ad2f5cb47490fa1e5ac2ba57d7a8。
- **Related Primary Sources:** https://github.com/embeddings-benchmark/mteb；
  https://github.com/embeddings-benchmark/results；the original MTEB paper and benchmark/task papers define
  predecessor contracts。Current repositories are used to verify maintained lineage only；the paper-pinned results commit
  is the event-time artifact boundary。
- **Access and Verification Status:** Verified with implementation-version caveat；v1 HTML/PDF, metadata, appendices and
  paper-pinned result commit are accessible。The paper states that debugging caused multiple MTEB package versions to be
  used；all models used the same task version within a task, but the entire experiment was not run on one immutable package
  revision。Exact environment/container and dataset snapshot for every result are not supplied as one manifest。
- **Full-read Coverage:** read metadata and all revisions；Abstract, Introduction, construction, quality control,
  accessibility optimizations, task-selection algorithm, benchmark construction, model/evaluation settings, multilingual
  results, English-v1/v2 analysis, Related Work, Conclusion and all Limitations；Appendix B task contracts/metadata, Appendix C
  clustering/retrieval/code optimizations, Appendix D task/language overview, Appendix E full results, Appendix F abstention,
  Appendix G exact model revisions/prompts/version caveat and Appendix H benchmark/task tables；official code/results lineage。
- **Original Problem:** embedding evaluation was fragmented across language, domain and task silos；running a broad suite was
  costly enough to exclude low-resource communities, while a small convenience suite could preserve average performance yet
  miss language- or task-specific regressions。The challenge is therefore both coverage and affordable evidence selection。
- **Why the Previous Design Was Reasonable:** compact English-centric suites were cheaper, easier to reproduce and enabled
  stable longitudinal model comparison；domain-specific retrieval or classification benchmarks provided sharper diagnosis。
  A full corpus remains the safer reference when small model differences, tail languages or absolute scores matter。
- **Changed Constraint:** production embeddings serve multilingual retrieval, clustering, classification, bitext, code and
  long-document workloads；hundreds of tasks and millions of documents make exhaustive evaluation expensive, and high-resource
  languages can dominate a naive average。The evaluation system needs an explicit population contract plus controlled reduction。
- **Mechanism:** collect more than 500 quality-reviewed tasks with task metadata；flag near-random, near-perfect or model-
  indistinguishable tasks using two baseline models and expert review；reduce clustering cost by encoding a stratified 4% corpus
  sample and reusing it across 10 sets；reduce retrieval corpora by TREC-style pooling from BM25, multilingual-e5-large and
  e5-Mistral-Instruct top-250 results, sampling at most 1,000 queries and 250,000 documents；cache shared bitext embeddings；then
  treat per-task model scores as features and iteratively remove the most predictable task under leave-one-model-out linear
  regression while preserving language/category coverage and error thresholds。
- **State Ownership:** task implementation and dataset revision own examples/splits；task metadata owns language, domain,
  source, annotation and license claims；pooling models and parameters own retrieval candidates；sampling seed and subset own
  reduced corpora；model revision/prompt/MTEB task version own each run；benchmark registry owns selected tasks；metric and Borda
  aggregation own rankings；result JSON owns runtime, emissions and environment metadata disclosed per run。
- **Control Flow / Data Flow:** contributed dataset + metadata + implementation → contributor/main-team review + two-model
  sanity checks → initial scope → license/translation/domain filtering → representative-model execution → leave-one-model/task
  predictability estimation → diversity/error constraints + manual review → versioned benchmark → frozen model revisions/prompts
  → task metrics → mean/category-weighted/Borda views → result repository and leaderboard。
- **Implementation Details:** classification samples 8–16 examples per label and repeats logistic-regression evaluation 10
  times；clustering uses K-means and V-measure；retrieval downsampling pools lexical and two dense retrievers；bitext caching turns
  shared-language work from repeated pairwise encoding toward language-linear reuse。The paper pins 12 Hugging Face model revisions
  and a results commit, but explicitly says multiple MTEB versions were used during debugging；current `main` cannot substitute
  for that historical environment。
- **Evaluation Contract:** v1 reports a collection of 500+ tasks in 10 categories and more than 250 languages excluding the
  broad bitext count；constructed suites include MTEB(Multilingual), Europe, Indic and zero-shot English v2。The representative
  evaluation covers 12 public models from MiniLM/MPNet/LaBSE through multilingual-e5 and two 7B Mistral-based embedders；reports
  task/category means and Borda rankings。Instruction-following retrieval is shown but excluded from category averages because
  support is incomplete。The v1 text itself conflicts on final counts：Table 1 says 132 multilingual tasks while prose says 131；
  English v2 is 41 in Table 1 while a later comparison references 40, so counts are not silently normalized。
- **Baselines / Ablations / Sensitivity / Overhead:** original versus optimized clustering/retrieval tasks, full English v1
  versus optimized/selected v2, and 12-model cross-task rankings provide reduction sensitivity。Nine English clustering tasks
  across 13 models average 0.9634 Spearman and 16.11x speedup；optimized English replacements correlate 0.97 Spearman/0.99
  Pearson with v1 before final task selection, while final v2 reports 0.90/0.96。There is no independent reproduction, no
  causal ablation separating all quality filters, no confidence interval for cross-family generalization and no exhaustive
  sensitivity to alternative pooling models, seeds or task-selection thresholds。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** the English v2 case reports 3.11 hours for
  GritLM-7B and 0.81 hours for all-MiniLM-L12 on one H100, using about 2% of documents and 6% of characters relative to v1；
  exact GPU SKU/memory, software image, precision, sequence-length distribution, batch, concurrency, power and production SLO
  are `Not Disclosed` in that summary。These numbers are benchmark-run evidence, not serving throughput or universal cost。
- **What the Evidence Actually Proves:** the authors built a large multilingual task collection and a reproducible-enough
  procedure for deriving smaller suites；on the selected public models/tasks, stratified reuse, pooled hard negatives and
  correlation-based task selection substantially reduced evaluation work while mostly preserving relative rankings。Results also
  show model size alone did not determine multilingual rank and that language/training coverage matters under this benchmark。
- **What It Does Not Prove:** it does not prove the reduced suite preserves rankings for future model families, sparse/different
  embedding architectures or deployment distributions；mean/Borda rank is not calibrated product utility；the model comparison
  does not causally isolate instruction tuning, scale or pretraining language mix；hard-negative pooling may miss documents that
  a novel retriever uniquely ranks；more languages or tasks do not automatically mean balanced or unbiased coverage。
- **Limitations / Threats to Validity:** human translations can create English leakage；task/language distribution remains
  skewed toward high-resource languages；metadata/domain taxonomy and collaboration credit are imperfect；datasets vary in source,
  annotation and quality；manual task replacement adds judgment；representative-model selection can overfit the reduced benchmark；
  mixed MTEB package versions weaken whole-run reproducibility；task-count inconsistencies, missing seed/environment manifest,
  compute cost and carbon impact, contamination and unequal prompt support limit comparison validity。
- **Trade-offs / New Failure Modes:** broader coverage increases representativeness but raises compute, governance and maintenance
  cost；task reduction makes routine evaluation accessible but can erase rare-language or novel-architecture failures；hard-negative
  pooling concentrates discrimination yet inherits pool-model blind spots；caching reduces redundant encoding but requires document,
  preprocessing, model and embedding identity；Borda reduces scale sensitivity but hides effect size；a living registry improves
  freshness while weakening historical comparability unless suites and result artifacts are frozen together。
- **Where the Previous Design Still Applies:** a small fixed golden set remains appropriate for fast regression；the complete
  corpus remains appropriate for close leaderboard decisions or unfamiliar model families；domain-specific expert suites remain
  necessary for legal, medical, code or product traffic；online quality and human outcome evidence remain necessary after offline
  embedding scores；simple averages are useful only when their population and weighting match the decision。
- **Evolution Relationship:** `Direct Evolution` from narrow fixed suites to versioned multilingual task populations and
  cost-aware subset construction；`Layering / Dependency` on immutable dataset/model/prompt/scorer artifacts and domain slices；
  `Alternative Branch` between exhaustive reference evaluation and reduced routine regression。The reduced suite does not replace
  the reference suite；it is a hypothesis whose rank-preservation boundary must be revalidated as model families change。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66）canonical owner；`MODEL-EMBEDDING` owns token/
  sentence representation distinctions, `AGENT-RAG` owns retrieval use, `PLATFORM-COST` owns evaluation resource accounting and
  `PLATFORM-OBSERVABILITY` owns run telemetry rather than benchmark judgment。
- **Target and Adjacent Chapters Read:** read Current Ch65 KAI Scheduler, Ch66 Evaluation System and Ch67 Monitoring；also
  read Ch11 Tokenizer, Ch12 Embedding and Ch13 Position Encoding to ensure the benchmark is not misfiled as a representation
  mechanism and that sentence/document embeddings remain distinct from token embeddings。
- **Existing Coverage:** Ch66 already defines EvalSpec identity, frozen versus dynamic suites, task/slice coverage, scorer
  uncertainty and evidence-cost trade-offs；Ch12 already separates token embeddings from sentence/document embeddings。MMTEB
  supplies a strong cost-aware benchmark-selection case and an explicit model-family generalization failure mode, but the later
  Books Gate must decide whether that nuance changes the existing chapter rather than appending a paper summary。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked 30-field review, final score, count/version conflicts, reduction
  mechanism, reproducibility boundary, Stable Node owner and event-time artifact links；no Books change。
- **Open Questions:** exact per-run MTEB package revisions, container/driver and dataset hashes；why v1 reports 131/132 and
  40/41 task counts；alternate pool-model/seed/threshold sensitivity；future-model rank preservation；per-language uncertainty and
  weighting；contamination and license audit；human-review agreement；full cost/energy contract；independent reproduction；criteria
  for promoting reduced tasks into an immutable release-gating suite。

### HumanUP

- **Candidate / Week / Score:** Learning Getting-Up Policies for Real-World Humanoid Robots / 2025-W08 / 26/30。
- **Source Family ID:** `humanup-two-stage-sim2real-recovery`。
- **Source Type:** arXiv/RSS robotics paper + official project page + later official simulation-training repository。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 18:59 UTC；v2 2025-04-27 and RSS 2025
  acceptance followed later。W08 mechanism and experiments are locked to v1；the public code/revised paper are lineage evidence,
  not treated as if an immutable implementation artifact existed on the event date。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.12152；https://arxiv.org/html/2502.12152v1；
  https://arxiv.org/pdf/2502.12152v1；https://humanoid-getup.github.io/。
- **Related Primary Sources:** https://github.com/RunpeiDong/HumanUP provides the later Isaac Gym simulation-training
  release；Unitree G1 documentation and the paper-cited PPO/online-adaptation works define platform/predecessor contracts。
  Later repository behavior is not used to assert event-time code availability or real-robot deployment details。
- **Access and Verification Status:** Verified with event-time artifact limitation；v1 HTML/PDF, supplement/reward tables,
  project videos and later official repository are accessible。No event-time commit, trained checkpoint, posture/terrain manifest,
  real-trial log or controller firmware image is pinned to 2025-02-17；hardware safety and real-world percentages therefore remain
  author experimental claims rather than independently reproducible results。
- **Full-read Coverage:** read metadata/revisions；Abstract, Introduction, all related-work branches；two-policy architecture,
  Stage I/II rewards and curricula；collision/posture/control/domain randomization；platform/simulation configuration；all simulated
  baselines, metrics, ablations and learning curves；real-world terrain results, temperature/efficiency and failure analysis；
  Limitations/Discussion；supplementary Stage I/II reward formulas/weights；project demos and repository scope。
- **Original Problem:** fall recovery is non-periodic, contact-rich and sparsely rewarded；a humanoid may begin in many prone/
  supine configurations on unknown surfaces。A policy that merely finds a successful simulated motion may use infeasible speed,
  torque or body contacts and therefore fail or damage hardware when transferred to a real robot。
- **Why the Previous Design Was Reasonable:** hand-designed trajectories are deterministic, easy to certify and work under a
  narrow nominal posture/surface；model-based planning exposes constraints；one-stage locomotion RL works when contact is mostly
  periodic feet-ground interaction and dense velocity rewards guide learning。These remain safer where environments are bounded,
  recovery states are enumerated or verification matters more than coverage。
- **Changed Constraint:** full-sized humanoid recovery must discover an unknown whole-body contact sequence, generalize across
  initial configurations and terrain, meet 50 Hz actuator deadlines and respect joint/torque/thermal limits。Applying all deployment
  constraints from the start makes sparse-reward exploration too difficult；ignoring them produces undeployable motion。
- **Mechanism:** decompose prone recovery into roll-over then supine get-up；train a Stage I PPO discovery policy with sparse task
  and soft-symmetry rewards under simplified collision, canonical starts and weak regularization；extract its state trajectory,
  slow it by 8x, then train a Stage II PPO policy to track that reference under full collision mesh, randomized postures/terrain/
  dynamics and stronger torque, velocity, smoothness and safety regularization。This separates feasibility discovery from
  deployability refinement rather than asking one objective to solve both simultaneously。
- **State Ownership:** simulator/URDF owns collision and dynamics state；posture dataset owns initial-state distribution；Stage I
  policy owns exploratory action proposals and discovered reference trajectory；Stage II policy owns deployable proposals；online
  adaptation latent owns estimated extrinsics；PD controller owns 50 Hz command execution；robot sensors own proprioception；safety
  metrics/logs own torque/joint/thermal evidence；physical environment owns actual outcome。Policy output is not safety authority。
- **Control Flow / Data Flow:** randomized/canonical robot state + proprioceptive history + extrinsic latent → Stage I 868-D
  observation → 23-D action and discovery rollout → 8x temporal interpolation → Stage II tracking target + full URDF + randomized
  posture/terrain/dynamics → deployable action → 50 Hz PD control → physical contact/outcome → success, jitter, energy, limit and
  temperature evidence。Prone execution composes roll-over and get-up policies sequentially。
- **Implementation Details:** both policies are MLPs trained with PPO；input combines 54-D extrinsic latent, 74-D current
  proprioception and ten historical states；wrist DoFs are disabled, leaving 23 actions on a 29-DoF Unitree G1；Isaac Gym runs
  contact simulation at 1,000 Hz while the low-level PD controller runs at 50 Hz。Stage II uses 10k train and 10k held-out poses
  for each of supine/prone sets produced by randomized joints, a 0.5 m drop and 10 s settling。Training uses about 5B simulation
  sampling steps；exact optimizer schedule, compute fleet, wall time and event-time code image are not fully disclosed in v1。
- **Evaluation Contract:** three simulated tasks—supine get-up, prone-to-supine roll-over and their sequential composition—use
  the full URDF and held-out posture sets；metrics include success, head height/orientation, third-derivative action/joint jitter,
  energy and torque/DoF safety scores with threshold 0.8 and equal peak/duration weighting。Real tests cover six disclosed terrain
  types from concrete through roughly 10-degree grass slope and snow, comparing HumanUP, no-posture-randomization and built-in G1
  controller；aggregate trial denominator and per-condition repetition protocol are not fully stated in prose。
- **Baselines / Ablations / Sensitivity / Overhead:** compares a character-animation RL reward baseline, Stage-I-only, simplified-
  URDF Stage II, no posture randomization, hard symmetry, single-stage full-constraint training and the built-in controller。The
  single-stage variant fails to learn；Stage-I-only succeeds partially but has unsafe jitter/energy；simplified URDF performs well
  in simulation yet fails 5/5 flat real trials；posture randomization and soft rather than hard symmetry improve held-out success。
  There is no equal-compute model-based controller, alternate simulator, reward-weight sensitivity, multiple robot instance or seed-
  level independent reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** physical platform is Unitree G1, 23 commanded DoFs,
  IMU/motor encoders and 50 Hz PD control；simulation is Isaac Gym at 1,000 Hz。Training GPU model/count, numerical precision,
  environment concurrency, wall time, energy, inference hardware, policy latency distribution and deadline-miss rate are `Not
  Disclosed`。Authors report about 6 s get-up versus nearly 11 s built-in motion and aggregate 78.3% get-up/98.3% roll-over success,
  but these are the disclosed real-test setup, not a production SLO or cross-platform benchmark。
- **What the Evidence Actually Proves:** within the authors' G1 and terrain contract, separating unconstrained trajectory discovery
  from constrained tracking can reconcile sparse-reward exploration with sim-to-real requirements；ablations directly show that
  simulation task success alone does not establish deployability and that contact geometry/posture distribution materially affect
  real transfer。The real demonstrations establish feasibility across more conditions than the supplied controller baseline。
- **What It Does Not Prove:** it does not prove arbitrary fallen-posture recovery, generalization to other robots or contacts,
  formal safety, immunity to collision/thermal damage, production availability or autonomous recovery after an uncontrolled fall；
  success percentages do not identify the causal contribution of every reward/randomization component；simulation metrics do not
  substitute for a complete real-trial denominator, near-miss/intervention log or certified controller evidence。
- **Limitations / Threats to Validity:** one robot design and a small disclosed terrain set；simulator contact mismatch；reward-
  underspecification yields non-human motions such as raised hands；real-test denominator/randomization and independent replication
  are limited；built-in controller is a narrow but not equal-capacity baseline；policy switching for prone recovery introduces an
  unstated transition boundary；no perception beyond proprioception, dynamic obstacles, damage assessment, fall detection, battery/
  thermal policy, emergency-stop or long-run hardware wear study；later code is not the event-time artifact。
- **Trade-offs / New Failure Modes:** two stages reduce objective interference but add reference-trajectory identity, handoff and
  distribution mismatch；slowing improves smoothness but increases exposure time；full collision improves transfer while raising
  simulation cost；randomization broadens robustness but can underfit nominal motion；soft symmetry preserves asymmetric recovery but
  enlarges search；policy composition adds switch-state failure；learned recovery can exceed a fixed trajectory yet create opaque
  torque allocation, simulator exploitation and unsafe out-of-distribution action failures。
- **Where the Previous Design Still Applies:** a verified hand trajectory remains preferable on known flat surfaces and controlled
  starts；model-based/MPC or hard constraints remain necessary for safety-critical contacts；teleoperation/human recovery remains the
  fallback for damaged hardware, unknown obstacles or failed state estimation；one-stage RL remains reasonable when reward is dense,
  contacts simple and deployment constraints do not block exploration。
- **Evolution Relationship:** `Direct Evolution` from canonical hand-coded recovery to learned contact-sequence discovery plus
  deployability refinement；`Layering / Dependency` on accurate simulation, state estimation, low-level PD control and an independent
  safety envelope；`Alternative Branch` between deterministic verified skills and broader learned policies。Stage II does not erase
  Stage I, and HumanUP does not erase the narrow controller that remains useful inside its validity region。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Current Ch26）canonical owner despite not being a language-conditioned
  VLA；`MULTIMODAL-WORLD-MODELS` owns simulator/state-transition semantics, `TRAIN-PPO` owns the optimizer family and
  `PLATFORM-EVALUATION-SYSTEM` owns physical evidence contracts。
- **Target and Adjacent Chapters Read:** read Current Ch25 World Models, Ch26 Embodied AI/VLA and Ch27 Data；verified that
  the durable contribution is the physical control/evidence boundary and curriculum handoff, not a new PPO algorithm or a generic
  claim about dataset construction。
- **Existing Coverage:** Ch26 already separates proposal from controller authority, defines simulation-to-real dimensions,
  physical evidence ladders and verified-skill coexistence；HumanUP adds a precise historical case showing why unconstrained motion
  discovery and deployable control regularization can require separate stages。Later Books Gate must decide whether this refines the
  existing curriculum/control argument rather than appending a robotics-paper summary。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked 30-field review, final score, two-stage state/control flow, simulation/
  real evidence boundary, code-release lineage and Stable Node owner；no Books change。
- **Open Questions:** event-time code/checkpoint/container and exact v1→v2 diff；training hardware, precision, wall time and seeds；
  full real-trial denominator/randomization/intervention logs；policy-switch condition and recovery on switch failure；latency/deadline
  distribution；damage, thermal and emergency-stop contract；alternate simulator/robot/terrain transfer；reward/randomization
  sensitivity；independent reproduction and long-run wear/safety evidence。

### SongGen

- **Candidate / Week / Score:** SongGen: A Single Stage Auto-regressive Transformer for Text-to-Song Generation / 2025-W08 / 26/30。
- **Source Family ID:** `songgen-single-stage-text-to-song`。
- **Source Type:** arXiv research paper + official project page + later official repository/checkpoint lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 18:52 UTC；v2 2025-05-30 and ICML 2025
  acceptance are later revision nodes。The project announced paper/demo on 2025-02-19；Mixed_Pro checkpoint, Interleaving checkpoint,
  MusicCaps test set and training code followed during March～July。W08 mechanism/evaluation claims are locked to v1；later artifacts
  improve lineage inspection but are not projected backward as event-time reproducibility。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13128；https://arxiv.org/html/2502.13128v1；
  https://arxiv.org/pdf/2502.13128v1；https://liuzh-19.github.io/SongGen/。
- **Related Primary Sources:** https://github.com/LiuZH-19/SongGen is the later official code/checkpoint lineage；the paper-cited
  X-Codec, MERT, FLAN-T5, Demucs, Whisper and MusicCaps sources define component/evaluation contracts。Current repository state is
  not treated as proof that code, checkpoints, processed data or environment manifests existed on 2025-02-18。
- **Access and Verification Status:** Verified with event-time artifact limitation；v1 HTML/PDF, project demos and current official
  repository are accessible。No immutable W08 training/inference commit, checkpoint, processed-data manifest, license ledger or container is public；
  repository news dates confirm the principal checkpoints/training code were released later。
- **Full-read Coverage:** read metadata/revision history；Abstract, Introduction and Related Work；architecture, mixed/dual-track
  formulations, lyric/voice/text conditioning, codec delay pattern and losses；data collection/filtering；three-step training and
  curriculum；objective/subjective evaluation, all tables/ablations and attention visualization；limitations/ethics/conclusion；
  appendix training, baseline, metric and listener details；project page and repository release chronology/current scope。
- **Original Problem:** text-to-music systems usually generate instrumental audio, while text-to-song additionally requires intelligible
  lyrics, speaker identity, vocal quality and synchronization between voice and accompaniment。Cascading lyrics-to-vocal and
  accompaniment systems expose separation/alignment interfaces；a mixed waveform model can instead ignore weak vocals because the
  accompaniment dominates the acoustic learning signal。
- **Why the Previous Design Was Reasonable:** instrumental generators avoid unreliable lyric alignment and source separation；a cascade
  lets specialized vocal/accompaniment modules be trained, upgraded and debugged independently；mixed-track generation uses the exact
  distribution listeners consume and has the shortest sequence。These designs remain rational when modular control, high-fidelity
  stems, low inference cost or established component artifacts matter more than a unified decoder。
- **Changed Constraint:** the target workload must jointly preserve semantic text relevance, sung phonemes, optional timbre and musical
  harmony while producing synchronized audio in one generative contract。Weak vocal energy, imperfect song datasets and eight-layer
  residual codec sequences cause the shared decoder to spend capacity on accompaniment and expose ordering/sequence-length choices that
  instrumental generation does not face。
- **Mechanism:** encode 16 kHz audio with X-Codec at 50 frames/s into eight 1,024-entry residual codebooks and apply a codebook-delay
  autoregressive pattern。Mixed mode predicts the final mixture；Mixed Pro adds auxiliary vocal-token heads and loss only during training
  (`L_mixed + 0.1 L_vocal`) then removes those heads at inference。Dual-track mode predicts vocal and accompaniment synchronously,
  either concatenating codebooks in parallel with standard/A-V/V-A delay or interleaving tracks temporally；lyrics use VoiceBPE plus a
  six-layer encoder, optional three-second voice uses frozen MERT features, text uses frozen FLAN-T5, and the decoder cross-attends to
  their projected conditioning sequence。
- **State Ownership:** X-Codec owns acoustic token/codebook identity and waveform reconstruction；VoiceBPE/lyrics encoder owns phonetic
  conditioning；MERT owns reference-voice features；FLAN-T5 owns caption features；SongGen decoder owns autoregressive proposal state；
  delay/interleaving policy owns track synchronization；dataset pipeline owns separation/transcription/caption provenance；runtime owns
  KV, sequence order and commit；codec decoder owns audible output。Auxiliary vocal heads do not exist at inference and therefore cannot
  own serving state。
- **Control Flow / Data Flow:** raw songs → Demucs stems → VAD segmentation/energy filtering → dual-Whisper agreement and CLAP filtering
  → lyric/caption/voice-conditioned training examples → condition encoders/projections → autoregressive decoder under mixed or dual-track
  token schedule → codec tokens → X-Codec decoder → waveform；evaluation normalizes outputs to -14 dB LUFS and sends five generations
  per method to objective metrics, while a 36-sample subset receives 20-listener MOS judgments。
- **Implementation Details:** reported model has a 24-layer, 1,024-hidden decoder and six-layer, 1,024-hidden lyric encoder (about 1.3B
  parameters in the official repository)。Training uses roughly 540k English vocal clips / 2,000 hours selected from an 8,000-hour
  source pool；Step 1 aligns all modalities, Step 2 drops voice condition 50% and performs staged freeze/unfreeze fine-tuning, Step 3
  fine-tunes on a 100k high-quality subset。Dual-track models initialize from mixed Step 1；early codebooks receive larger curriculum
  weights before balancing。Authors report about 400k steps on 16 A100 80GB GPUs, batch 16/GPU, AdamW and cosine scheduling。
- **Evaluation Contract:** 326 English-vocal MusicCaps prompts with pipeline-added lyrics and claimed no training overlap；objective FAD,
  KL, CLAP, phoneme error rate from Distil-Whisper and speaker similarity from Resemblyzer；five random samples per method averaged；
  subjective study uses 36 prompts × 20 listeners and 1～5 MOS for overall, relevance, vocal quality, harmony and speaker similarity。
  Baselines include Stable Audio Open, MusicGen, an internally fine-tuned Parler-TTS and commercial Suno for subjective comparison。
- **Baselines / Ablations / Sensitivity / Overhead:** Mixed Pro improves Mixed under the author contract；A-V Interleaving is the best
  reported dual-track order, while Parallel shortens sequence and generally loses quality。Ablations cover high-quality fine-tuning,
  codebook-weight curriculum, lyric tokenizer/encoder/cross-attention and X-Codec versus Encodec/DAC。There is no equal-compute
  comparison across all baselines, broad seed confidence interval, dataset-filter sensitivity, track-order controller, inference latency,
  memory, throughput or concurrency study；interleaving explicitly doubles temporal sequence length relative to parallel packing。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training: approximately 1.3B model, 16×A100 80GB,
  400k steps, 16 examples/GPU, English clips averaging about 15 seconds and capped at 30 seconds；precision, gradient accumulation,
  interconnect, wall time and energy are Not Disclosed。Evaluation uses 326 prompts and five samples/method；inference hardware,
  precision/quantization, sampling parameters, batch, concurrency, KV memory, RTF/TTFT, throughput and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' 16 kHz English-song dataset and evaluation pipeline, one autoregressive
  decoder can model codec tokens for mixed or synchronized dual-track generation；auxiliary vocal supervision can improve a mixed output
  without adding an inference head；track ordering/packing changes quality-cost behavior；data filtering, lyric-specific encoding and
  codebook curriculum materially affect the reported operating point。
- **What It Does Not Prove:** it does not prove general song quality across languages/genres/long durations；phoneme correctness beyond
  an imperfect speech ASR proxy；speaker consent or safe cloning；end-to-end superiority over a well-tuned cascade；production latency/
  goodput；that Interleaving dominates Parallel at equal compute；that attention maps establish causal lyric alignment；or that
  “single-stage” removes the external codec, conditioning encoders, data pipeline and waveform decoder。
- **Limitations / Threats to Validity:** English-only, 16 kHz, maximum 30-second outputs；sung-speech ASR inflates PER；small subjective
  subset and imperfectly matched baselines；author-selected/source-separated/pseudo-labeled data；unknown license, performer consent and
  dataset leakage details；no independent reproduction or event-time code/checkpoint；no long-form structure, streaming, rare-voice,
  multilingual, adversarial prompt, copyright, deepfake-abuse or serving-resource evaluation。
- **Trade-offs / New Failure Modes:** unified decoding removes a cascade boundary but couples codec, condition encoders and decoder
  versions；Mixed is cheap but can bury vocals；auxiliary vocal supervision improves learning yet introduces train/inference objective
  mismatch；Parallel preserves shorter sequences but weakens track interaction；Interleaving strengthens causal synchronization while
  doubling sequence length/KV pressure；voice conditioning adds identity misuse risk；automatic separation/transcription/filtering scales
  data but propagates correlated label/provenance errors。
- **Where the Previous Design Still Applies:** instrumental generators remain sufficient without lyrics；cascades remain better when
  users need editable stems, independent component upgrades or explicit safety/provenance gates；mixed mode remains attractive for low
  latency and memory；parallel dual-track packing remains preferable when sequence/KV cost dominates；human production remains necessary
  for licensed identity, long-form composition and auditable creative control。
- **Evolution Relationship:** `Direct Evolution` from instrumental/mixed audio AR toward vocal-aware supervision and synchronized
  multi-stream generation；`Alternative Branch` between mixed, parallel and interleaved state layouts；`Layering / Dependency` on codec,
  conditioning and data-quality contracts。Interleaving does not replace Parallel, and unified decoding does not erase modular cascades。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24）canonical owner；
  `MULTIMODAL-REPRESENTATION` owns codec/codebook identity, `TRAIN-DATA` owns source/separation/transcription provenance,
  `INFER-PREFILL-DECODE` owns autoregressive runtime state and `PLATFORM-SECURITY` owns voice/copyright threat policy。
- **Target and Adjacent Chapters Read:** read Current Ch23 Multimodal Representation, Ch24 Multimodal Generative Paradigms and Ch25
  World Models；also read Ch27 Data to keep source filtering/provenance out of the generation-paradigm owner。Ch24 owns factorization,
  track-state layout and commit/cost trade-offs；SongGen is not a world model and its codec is not a new generic representation law。
- **Existing Coverage:** Ch23 already defines residual-codebook identity/rate-distortion and audio sequence state；Ch24 already derives
  AR versus iterative generation from factorization, mutability and commit protocol；Ch27 owns provenance and data filtering。SongGen
  contributes a strong multi-stream AR case where supervision and serialization policy trade learning bias against sequence cost, but a
  future Books Gate must integrate that mechanism into the existing evolution rather than append a product/paper description。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked 30-field review, final score, audio-token/track state ownership, data and
  evaluation contracts, later-artifact lineage and Stable Node owner；no Books change。
- **Open Questions:** immutable event-time code/checkpoint/data/license/container；exact v1→v2 diff；precision/accumulation/wall time/
  energy；data-source authorization and performer consent；dataset-filter and codec sensitivity；equal-compute mixed/parallel/interleaving
  comparison；long-form/streaming behavior；sampling and serving contract；speaker-cloning safeguards；independent reproduction and
  multilingual/genre/generalization evidence。

### Small Model Learnability Gap

- **Candidate / Week / Score:** Small Models Struggle to Learn from Strong Reasoners / 2025-W08 / 26/30。
- **Source Family ID:** `small-model-learnability-gap-mix-distillation`。
- **Source Type:** arXiv research paper + official project page + current official code/data/checkpoint repository + later ACL publication。
- **First-public Date / Revision History:** arXiv v1 2025-02-17 18:56 UTC；v2 2025-02-22 16:23 UTC, still inside W08；
  v3 2025-11-13 and Findings of ACL 2025 publication are later lineage。W08 evidence is locked to v2, the last public revision in
  the ISO week；later publication/artifacts do not upgrade the event-time experiment contract。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.12143；https://arxiv.org/html/2502.12143v2；
  https://arxiv.org/pdf/2502.12143v2；https://small-model-gap.github.io/。
- **Related Primary Sources:** https://github.com/Small-Model-Gap/Small-Model-Learnability-Gap exposes current LLaMA-Factory/
  lm-evaluation-harness forks, scripts, datasets and checkpoints；https://aclanthology.org/2025.findings-acl.1301/ records later
  publication/DOI。Repository commit chronology was not recoverable in this pass, so current artifacts are lineage rather than proof
  of an immutable 2025-02-22 environment。
- **Access and Verification Status:** Verified with event-time artifact limitation；W08 v2 HTML/PDF, project page and current official
  repository are accessible。No paper-pinned commit, exact dataset/model hashes, container/driver image, teacher-output manifest or
  per-run seed log is attached to v2；artifact-to-table reproduction remains unverified。
- **Full-read Coverage:** read metadata and all revisions；Abstract/Introduction/Preliminaries；experiment setup, Long-CoT and large-
  teacher gaps；domain-knowledge/base-vs-instruct/style-shift analyses；Mix-Long/Mix-Large mechanism and ratio sweep；Related Work,
  Conclusion/Future Work；Appendix model/training/evaluation contracts, all detailed benchmark tables and examples；project page,
  current repository training/evaluation instructions and later ACL metadata。
- **Original Problem:** direct sequence distillation assumes a more capable teacher produces universally better demonstrations。For a
  small student, however, very long reasoning traces or a distant teacher distribution may spend much of the fixed token/gradient budget
  on style and intermediate states the student cannot internalize, reducing held-out reasoning performance despite higher-quality labels。
- **Why the Previous Design Was Reasonable:** strong-teacher distillation is simple, reuses already-correct outputs and often works when
  teacher/student support overlaps；long CoT exposes decomposition/backtracking and benefits larger students；single-source SFT gives an
  immutable dataset and clear attribution。It remains appropriate when the student has sufficient capacity/domain knowledge, teacher
  outputs match deployment, or mixture-control evidence is unavailable。
- **Changed Constraint:** deployment seeks small (roughly <=3B in this study) reasoning models, while demonstrations differ in length,
  teacher size, style and in-domain knowledge。Student capacity and initialization change which target distribution is learnable；data
  quality therefore cannot be ordered by teacher benchmark alone。
- **Mechanism:** construct matched MATH problem-response sets from long versus short CoT teachers and large versus small teachers, then
  SFT a scale sweep of Qwen/Llama students。Measure `Delta_Long=P_Long-P_Short` and `Delta_Large=P_Large-P_Small`；for mitigation,
  Mix-Long samples long and short traces, and Mix-Large samples large- and small-teacher traces。The reported default uses a challenging:
  easier ratio of 1:4 (`alpha=0.2`), selected by a Qwen2.5-3B sweep across five math benchmarks。
- **State Ownership:** teacher checkpoint/decoding owns demonstration distribution；pairwise correctness filter owns admitted examples；
  mixture manifest/alpha/random seed owns sampling exposure；student checkpoint/tokenizer owns learnability and parameter state；SFT
  runtime owns loss/update trajectory；evaluation harness/judge owns measured correctness。Teacher strength does not own the final data
  policy, and response length is a diagnostic rather than correctness authority。
- **Control Flow / Data Flow:** 7,500 MATH prompts → teacher greedy responses/rejection sampling → retain prompt pairs both compared
  teachers solve correctly → build long/short or large/small response artifacts → fixed or mixed sampling manifest → full/LoRA SFT by
  student size → zero-shot greedy generation up to 16k tokens → exact-answer extraction, then Qwen-32B judge fallback → five-benchmark
  score and output-length/style diagnostics。
- **Implementation Details:** Qwen2.5 0.5B～32B and Llama 1B～70B student sweep；QwQ-32B-Preview versus Qwen2.5-32B for
  long/short traces, plus Qwen 72B/3B, Llama 70B/8B and Gemma 27B/9B teacher comparisons。Below 14B uses full fine-tuning
  (LR 1e-5, 2 epochs, 4 devices, batch 2/device)；larger models use full-target LoRA (LR 1e-4, 2 epochs, batch 1/device,
  warmup 0.03)；both cap sequence length at 16,384 and use cosine scheduling on 4×A100-SXM4-80GB, EPYC 7763, 512GB RAM。
- **Evaluation Contract:** training prompts are MATH 7.5k；evaluation covers MATH, GSM8K, AMC 2023, AIME 2024 and English
  OlympiadBench。Default zero-shot greedy decode with 16k max tokens；exact match first, Qwen-32B-Instruct judge fallback。Mix
  results focus on Qwen2.5-3B-Instruct and Llama3.2-3B-Instruct；reported averages weight benchmarks equally despite very different
  sizes/difficulty, and test-time inference cost is not normalized by generated-token count。
- **Baselines / Ablations / Sensitivity / Overhead:** compares long/short, large/small teacher, DeepSeek-R1-32B long CoT and both mixes；
  sweeps mixture alpha and contrasts general versus math-expert, base versus instruct, multiple model families and shifted token styles。
  Missing: repeated seeds/confidence intervals, compute/token-matched datasets, factorial separation of length from teacher identity/style,
  alternative correctness filters/judges, held-out domains, contamination audit and training/inference cost curves。Mixing adds dataset,
  sampling and reproducibility overhead even though the loss remains ordinary SFT。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training hardware is 4×A100-SXM4-80GB plus 512GB
  host RAM；students span 0.5B～70B, full SFT below 14B and LoRA above；max train/eval length 16,384, 2 epochs, micro-batch 2
  or 1/device。Precision, gradient accumulation/global batch, interconnect, wall time, energy, seeds and teacher-generation hardware are
  Not Disclosed；serving batch/concurrency, latency, throughput, quantization and SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the disclosed math/data/model/evaluator contract, smaller Qwen/Llama students often gain
  less or regress relative to shorter/closer-teacher traces, while larger students more often benefit from long/large-teacher traces；a
  fixed 20% challenging-trace mixture improves the two studied 3B students across most reported metrics；domain-specialized/instruct
  initialization correlates with a smaller gap, and long-teacher SFT strongly changes speaking-style tokens。
- **What It Does Not Prove:** no universal <=3B threshold, causal intrinsic-capacity law or guarantee that small teachers are better；
  no separation of trace length, correctness, teacher family, style and distribution distance；no evidence outside mathematical reasoning,
  for RL/on-policy distillation, deployment latency, factual/safety tasks or future model families；and no proof that alpha=0.2 is a
  transferable optimum。Judge-assisted final-answer scoring does not prove intermediate reasoning correctness。
- **Limitations / Threats to Validity:** one 7.5k training-domain source；small AIME/AMC test sets and average-score instability；
  possible training/evaluation contamination；model-family and teacher confounding；single-run uncertainty；teacher outputs filtered only
  where compared systems are both correct, changing the retained distribution；post-hoc “intrinsic capacity/distribution shift” explanation
  is suggestive rather than causal；later code may differ from v2；no privacy/license/cost/energy analysis of generated traces。
- **Trade-offs / New Failure Modes:** simpler/closer traces reduce student mismatch but may omit useful search/backtracking；challenging
  traces add strategy diversity yet consume length/gradient budget and induce imitation of verbal tics；mixtures hedge both branches but
  add alpha selection, duplicate/conflicting targets, curriculum drift and manifest identity；large teachers may improve correctness but
  cost more to generate and create a wider support gap；judge fallback can introduce evaluator-family bias。
- **Where the Previous Design Still Applies:** pure long/strong-teacher distillation remains suitable for larger/domain-expert students,
  verified complex traces and workloads where search structure matters；pure short/small-teacher SFT remains simpler for tight latency/
  capacity budgets；human demonstrations remain preferable for policy, safety or domains without reliable verifiers；on-policy/logit
  distillation remains a separate branch when student-state coverage rather than offline target complexity is the main mismatch。
- **Evolution Relationship:** `Direct Evolution` from one-source hard sequence distillation to student-conditioned demonstration mixture；
  `Alternative Branch` among short, long, weak-teacher, strong-teacher and mixed datasets；`Layering / Dependency` on teacher identity,
  correctness filtering, student initialization and EvalSpec。Mix Distillation does not replace strong-teacher KD；it makes the selection
  policy conditional on student/workload evidence。
- **ROADMAP Node:** `TRAIN-SFT`（Current Ch29）canonical owner；`TRAIN-DATA` owns derived-response provenance and mixture manifests,
  `TRAIN-PRETRAINING` owns student prior/domain capacity, `TRAIN-LORA` owns parameterization for >14B runs and
  `PLATFORM-EVALUATION-SYSTEM` owns benchmark/judge evidence。
- **Target and Adjacent Chapters Read:** read Current Ch27 Data, Ch28 Pretraining, Ch29 SFT and Ch30 LoRA；verified that the mechanism
  changes SFT target-distribution scheduling, not the next-token objective, LoRA mathematics or a universal model-scaling law。
- **Existing Coverage:** Ch27 already defines mixture as executable training policy；Ch29 already states teacher strength is not a total
  order and separates offline/on-policy distillation, repetition and scheduling；Ch28 owns prior/domain capability, Ch30 parameterization。
  This paper supplies an early scale-conditioned offline-mixture case, but Books integration must refine the existing evolution rather
  than append its 1:4 recipe or “<=3B” headline as a law。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added W08-v2-locked 30-field review, final score, mixture/state ownership, hardware/evaluation
  contract, causal limits, later-artifact lineage and Stable Node mapping；no Books change。
- **Open Questions:** exact v1→v2 changes and v2→v3/ACL artifact mapping；event-time commit, dataset/checkpoint digests and seeds；
  independent reproduction/confidence intervals；length-matched and compute-matched causal study；cross-domain/model-family threshold；
  verifier/judge sensitivity；contamination and trace provenance/license；adaptive alpha under fixed token budget；interaction with RL,
  on-policy distillation, quantization and serving SLO。

### Multimodal Mamba

- **Candidate / Week / Score:** Multimodal Mamba: Decoder-only Multimodal State Space Model via Quadratic to Linear Distillation /
  2025-W08 / 27/30。
- **Source Family ID:** `mmmamba-transformer-to-ssm-distillation`。
- **Source Type:** arXiv research paper + event-time official code/weight release + model artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-02-18 18:59 UTC；official repository records initial code and weights
  on 2025-02-19；v2 2025-03-18 is later lineage。W08 claims are locked to v1 plus the dated initial release；current repository
  can inspect implementation lineage but is not silently substituted for an immutable event-time commit。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13145；https://arxiv.org/html/2502.13145v1；
  https://arxiv.org/pdf/2502.13145v1；https://github.com/hustvl/mmMamba。
- **Related Primary Sources:** official mmMamba-linear/hybrid model artifacts, HoVLE teacher artifact and cited Mamba-2/SSD paper define
  weight/state contracts。Repository documentation exposes conversion/distillation entry points, but no paper-pinned commit/container or
  immutable benchmark log was identified；v2 remains a later revision node。
- **Access and Verification Status:** Verified with reproducibility boundary；v1 full text, formulas/tables and official repository/model
  release are accessible。The exact event-time commit, dataset manifest, teacher checkpoint digest, CUDA/Triton/driver versions, seeds
  and raw latency/memory traces are not pinned, so author results are not independently reproduced。
- **Full-read Coverage:** read metadata/revisions；Abstract/Introduction/Related Work；Transformer and Mamba-2 equations；seeding,
  all three distillation stages and linear/hybrid architecture；training/evaluation implementation；nine-benchmark comparison；fixed-
  prompt and long-context efficiency experiments；stage/init/attention-count/placement ablations；Conclusion；official repository
  release notice, source layout, getting-started and artifact lineage。
- **Original Problem:** decoder-only VLMs inherit Transformer Attention's quadratic Prefill and sequence-growing KV state；retraining a
  native linear multimodal model from scratch needs specialized pretrained backbones and large multimodal data。Naively swapping every
  Attention layer for an SSM changes the state semantics so sharply that inherited multimodal behavior collapses。
- **Why the Previous Design Was Reasonable:** encoder-plus-LLM VLMs reuse mature vision/language artifacts and isolate modality failures；
  decoder-only Transformers preserve exact token-addressable history, strong pretrained capabilities and mature kernels；training an SSM
  from scratch avoids teacher bias。These remain better for short context, exact retrieval, independent component upgrades, mature
  serving stacks or when distillation error is less acceptable than KV cost。
- **Changed Constraint:** long high-resolution multimodal sequences and long reasoning make pairwise Attention/KV capacity dominant, but
  academic budgets cannot repeat full pretraining。The conversion must preserve a 2.6B teacher's multimodal function while replacing
  token-addressable history with a fixed recurrent matrix state and offering a controllable quality-efficiency frontier。
- **Mechanism:** inherit Transformer `W_Q/W_K/W_V/W_O` into corresponding Mamba-2 projections；initialize decay gate near one,
  causal convolution as identity and new output gate to mimic the old layer。Stage 1 uses equal teacher-layer inputs and MSE to train only
  SSM-specific parameters；Stage 2 MSE-aligns all Mamba-2 mixer parameters layerwise；Stage 3 feeds each end-to-end model independently
  and minimizes output KL。Pure variant converts all 32 layers；hybrid preserves 8 head-interleaved Attention layers among 24 Mamba-2。
- **State Ownership:** Transformer teacher owns reference intermediate/output distributions；weight converter owns parameter mapping；
  Mamba layer owns fixed matrix state/decay/convolution/gate；Attention layers in hybrid own exact KV slices；frozen MLP and text/image
  embeddings own inherited feature transforms；distillation runtime owns stage/optimizer/checkpoint state；serving runtime owns recurrent
  state/KV lifecycle。A fixed state is compressed computation, not a provenance-preserving memory archive。
- **Control Flow / Data Flow:** HoVLE weights + multimodal SFT sequence → per-layer parameter conversion/mimetic initialization → Stage-1
  teacher-input layer MSE → Stage-2 whole-mixer layer MSE → Stage-3 independent end-to-end KL → linear or hybrid checkpoint → recurrent
  Prefill/Decode state (plus sparse exact-KV layers in hybrid) → benchmark outputs and hardware measurements。
- **Implementation Details:** HoVLE has 32 Transformer layers/2.6B parameters；mmMamba is 2.7B。Linear converts all layers and trains
  14.7% of parameters；hybrid uses 24 Mamba-2 + 8 Transformer layers and trains 11.2%。Distillation uses SOLO's 1.7M language/image-
  text SFT samples, 8×A800 80GB, BF16, ZeRO-2, AdamW, clip 5.0, WSD 10% warmup/decay；Stages 1/2 each 20k steps,
  batch 128, LR 1e-3/5e-4；Stage 3 20k steps, batch 64, LR 5e-5；weight decay 0.05。
- **Evaluation Contract:** capability: MME-perception, MMBench-EN, averaged POPE, SEED, MMMU, MM-Vet, TextVQA, ScienceQA-Image and
  GQA with heterogeneous public baselines/recipes。Fixed prompt efficiency: one image, “Describe the image specifically,” 768 visual
  tokens for HoVLE/mmMamba, exactly 256 output tokens, total Prefill+Decode time on one RTX 4090。Long-context curve measures next-token
  latency and GPU memory versus synthetic/constructed context length on the same 4090, with 103K headline and HoVLE OOM at 128K。
- **Baselines / Ablations / Sensitivity / Overhead:** compares encoder-based, decoder-only, Transformer and recurrent VLMs；factorial
  inclusion of three stages, scratch versus inherited versus mimetic initialization, 0/1/2/4/8/32 Attention layers and four layer
  placements。No repeated-run variance, equal-quality/equal-training-data baseline, long-context task accuracy, recurrent-state reset/
  migration test, batch/concurrency sweep, stage compute accounting or production kernel/failure study；hybrid adds dual state/runtime。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training: 2.7B student, 8×A800 80GB, BF16, ZeRO-2,
  1.7M samples, 20k steps per stage, batch 128/128/64；interconnect, wall time, energy and seeds Not Disclosed。Inference: single RTX
  4090, one fixed image/prompt, 256 output tokens, 768 visual tokens for focal models；long context to 128K and 103K headline；precision,
  batch/concurrency, sampling, TTFT/TPOT split, power and SLO Not Disclosed。
- **What the Evidence Actually Proves:** in the authors' HoVLE/SOLO/hardware contract, mimetic initialization plus progressive local-
  to-global distillation preserves materially more VLM behavior than direct replacement；pure recurrent and interleaved hybrid checkpoints
  form a measured quality-state-cost frontier；fixed recurrent state substantially reduces long-context next-token memory/latency on a
  single 4090, while the hybrid retains more teacher quality at higher state cost。
- **What It Does Not Prove:** no universal Transformer-to-SSM conversion guarantee；no exact preservation of teacher distribution or rare-
  token retrieval；no real long-document/video task quality at 103K；no production throughput/tail-latency/energy benefit；no evidence
  that a decoder-only SSM dominates encoder-based VLMs at equal data/compute/quality；and no portability across architectures, hardware,
  quantization or multimodal schemas。20.6x is not a general serving speedup。
- **Limitations / Threats to Validity:** single teacher/model scale and SFT dataset；heterogeneous benchmark recipes and parameter counts；
  no event-pinned environment or independent reproduction；fixed one-request 4090 microbenchmark；quality at long lengths unmeasured；
  compressed state may forget exact evidence；hybrid state lifecycle/failure recovery absent；stage compute excludes teacher-forward and
  artifact creation from simple “trainable parameter” narratives；paper has no explicit limitations section despite these constraints。
- **Trade-offs / New Failure Modes:** pure SSM removes growing KV but loses exact addressing and teacher fidelity；hybrid restores periodic
  Attention at the price of dual recurrent/KV identity, placement and migration；mimetic seeding reduces optimization shock while coupling
  student layout to teacher parameters；three stages improve transfer but add checkpoints, frozen/trainable-set transitions, teacher
  compute and recovery semantics；fixed state introduces overwrite/decay, stream contamination and reset/isolation failures。
- **Where the Previous Design Still Applies:** full Transformer remains preferable for short context, exact evidence retrieval, mature
  kernels and auditability；encoder-based composition remains useful for independently versioned vision backbones；from-scratch SSM
  training remains valid with enough data/compute or a different target architecture；pure SSM fits memory-bound long streams, while hybrid
  fits workloads requiring more exact interaction and accepting residual KV cost。
- **Evolution Relationship:** `Direct Evolution` from pretrained Transformer VLM to progressively distilled recurrent/hybrid state；
  `Alternative Branch` among all-Attention, pure SSM and mixed layers；`Layering / Dependency` on representation, teacher artifact and
  runtime state management。Linear state does not replace exact Attention universally；hybrid makes coexistence explicit。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Current Ch22）canonical owner；`MODEL-TRANSFORMER-LAYER` owns Attention/MLP layer
  anatomy, `MULTIMODAL-REPRESENTATION` owns image/text token identity, `TRAIN-SFT` owns distillation objective/stages,
  `INFER-KV-CACHE` and `INFER-EXECUTION` own recurrent/KV state execution and hardware kernels。
- **Target and Adjacent Chapters Read:** read Current Ch21 MoE, Ch22 Long Context and Ch23 Multimodal Representation；also read Ch29
  SFT's distillation branches。Verified that the durable mechanism is the exact-history versus compressed-state migration and coexistence
  boundary, not a new visual tokenizer, generic SFT law or benchmark-list insertion。
- **Existing Coverage:** Ch22 already separates exact KV, recurrent/compressed state and hybrid Attention, including migration/state-
  continuity contracts；Ch23 owns representation identity；Ch29 owns local/global distillation semantics。mmMamba adds a concrete
  progressive architecture-conversion chain, but future Books work should refine the existing state-evolution spine rather than append
  speed claims or treat Mamba as Attention's successor。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added v1-locked 30-field review, final score, architecture/state flow, complete training and
  hardware contracts, benchmark boundaries, event-time code lineage and Stable Node mapping；no Books change。
- **Open Questions:** paper-pinned commit/checkpoint/dataset/container and exact v1→v2 diff；teacher-forward/total compute and energy；
  long-context retrieval/video/reasoning quality；recurrent state size/layout/precision and reset/migration/isolation；batch/concurrency,
  quantization and multi-GPU serving；seed variance；equal-data/compute baselines；independent reproduction and production crossover。

### RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning

- **Candidate / Week / Score:** RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning /
  2025-W08 / 28/30。
- **Source Family ID:** `rad-3dgs-closed-loop-driving-rl`。
- **Source Type:** arXiv research paper + official project page + later official code/artifact lineage。
- **First-public Date / Revision History:** arXiv v1 2025-02-18 18:59 UTC；W08 claims are locked to v1。The official
  repository states that the paper was released on 2025-02-18, core RL code followed on 2025-09-28 and reconstructed 3DGS
  environments on 2025-11-04；NeurIPS 2025 paper and 2026 RAD-2 are later lineage, not W08 event evidence。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13144；https://arxiv.org/html/2502.13144v1；
  https://arxiv.org/pdf/2502.13144v1；https://hgao-cv.github.io/RAD/。
- **Related Primary Sources:** https://github.com/hustvl/RAD records later core-code lineage；the NeurIPS 2025 proceedings
  version is later peer-reviewed publication evidence。No event-time code, 3DGS environment snapshot, dataset manifest or raw rollout log was public with v1。
- **Access and Verification Status:** Verified with reproducibility boundary；v1 full text, equations, tables, appendix and project
  demonstrations are accessible。Later repository code can inspect mechanism lineage but cannot reproduce the event-time paper without
  the original environments, data, checkpoint, commit and execution image。
- **Full-read Coverage:** read metadata；Abstract/Introduction/Related Work；policy architecture；three-stage training；3DGS-policy
  interaction；reward modeling；PPO/GAE and auxiliary objectives；dataset/evaluation setup；all baseline, ratio, reward and objective
  ablations；qualitative results；Limitations/Conclusion；action-space and hyperparameter appendix；project page and repository timeline。
- **Original Problem:** imitation-learned end-to-end driving policies see expert-state distributions and optimize open-loop action
  matching；small action errors change the future observation distribution, while rare collision/avoidance states are underrepresented。
  Real-world closed-loop RL is unsafe and costly, and conventional game-engine sensor simulation has a realism gap for image policies。
- **Why the Previous Design Was Reasonable:** IL uses abundant human demonstrations, is stable, avoids unsafe exploration and preserves
  human-like smoothness；modular/game-engine simulators offer explicit control and repeatability；open-loop evaluation is cheap。They remain
  preferable when reactive environments, precise physics, certified safety or high-fidelity 3DGS reconstruction are unavailable。
- **Changed Constraint:** the policy must learn under its own induced state distribution and safety-critical deviations, yet exploration
  must stay off-road。Photorealistic 3DGS log reconstructions make image-conditioned rollout scalable enough to test a hybrid RL+IL branch,
  while limited action horizon and dense safety signals control exploration cost。
- **Mechanism:** perception pretraining supervises BEV/map/agent tokens；planning pretraining uses 2000h demonstrations to initialize
  decoupled lateral/longitudinal action distributions；reinforced post-training runs 32 parallel workers over independently reconstructed
  3DGS clips。A kinematic bicycle model updates ego pose every step, the renderer produces the next observation, four event rewards feed
  lateral/longitudinal GAE and clipped PPO, directional dense auxiliary losses reshape the whole action distribution, and interleaved IL
  updates regularize human alignment。The selected operating point uses a 4:1 RL:IL step ratio。
- **State Ownership:** logged demonstrations own human trajectories and labels；each 3DGS environment owns visual scene reconstruction,
  map/agent annotations and log-replayed non-ego trajectories；worker owns episode pose/state/action/reward；rollout buffer owns versioned
  trajectories；old policy/value heads own sampling probabilities and advantage baselines；trainer owns PPO/IL schedule and parameters；
  controller/kinematic model owns executed ego transition。Rendered state is simulator evidence, not real-road truth。
- **Control Flow / Data Flow:** real demonstrations → perception labels and IL action anchors → initialize image encoder/planning head →
  sample risky clips and fit 3DGS environments → worker observes multi-view frames/map/agent/image tokens → policy samples 0.5-second
  lateral/longitudinal action → bicycle model advances ego pose while other actors replay logs → renderer/reward system emits next state
  and four event signals → rollout buffer → GAE/PPO plus dense objectives alternating with IL → periodically broadcast policy → closed-loop
  evaluation on held-out reconstructed clips。
- **Implementation Details:** action horizon is 0.5 s；lateral displacement has 61 anchors from -0.75 m to 0.75 m and longitudinal
  displacement is separately discretized。Only image encoder and 256-d planning/value heads update in reinforced post-training；BEV,
  map and agent components remain frozen。Planning pretraining uses AdamW, LR 1e-4 cosine, batch 512 and 30k steps；RL uses LR 5e-6,
  32 workers, RL batch 32, IL batch 128, gamma 0.9, lambda 0.95, lateral/longitudinal clips 0.1/0.2, 2 m/40-degree deviation thresholds。
- **Evaluation Contract:** 2000h real expert driving supplies pretraining data；4305 high-risk dense-traffic clips become independent
  3DGS scenes, with 3968 for RL and 337 unseen reconstructed environments for closed-loop evaluation。Metrics are dynamic/static/total
  collision ratios, positional/heading/combined deviation, Average Deviation Distance and longitudinal/lateral jerk。VAD, GenAD and VADv2
  are trained with the same human-demonstration amount；RAD reports CR 0.089 versus 0.270--0.341 in this benchmark。
- **Baselines / Ablations / Sensitivity / Overhead:** compares pure IL, pure RL and 2:1/4:1/8:1 RL:IL；ablates each reward source,
  each dense auxiliary objective and PPO；compares three IL baselines and qualitative scenarios。Pure RL lowers collision versus IL but
  worsens ADD；8:1 worsens deviation/jerk, supporting a conditional safety-alignment trade-off。No real-road policy test, reactive-actor
  ablation, renderer-fidelity sensitivity, random-seed confidence interval, equivalent game-engine baseline or end-to-end compute study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** policy parameter count, camera count/resolution, accelerator,
  precision, interconnect, wall time, energy, rendering FPS and deployment SLO are Not Disclosed。Training discloses 32 rollout workers,
  RL batch 32, IL batch 128 and planning batch 512；control horizon is 0.5 s。Worker count is rollout parallelism, not production traffic
  concurrency, and no latency/jitter/stale-action contract is reported。
- **What the Evidence Actually Proves:** in the authors' non-reactive, held-out 3DGS dense-traffic benchmark, closed-loop hybrid
  post-training changes the policy's induced-state behavior and reduces collision/deviation metrics relative to same-demonstration IL
  baselines；ratio, reward and objective ablations show that PPO exploration, safety shaping and IL regularization contribute differently。
  It also demonstrates an executable separation between environment reconstruction, rollout ownership and policy update。
- **What It Does Not Prove:** it does not prove real-road safety, causal understanding, sim-to-real transfer, general collision avoidance,
  superiority to reactive simulators, or that 3DGS visual fidelity is control sufficient。The 3x headline is specific to 337 reconstructed
  clips and disclosed baselines；it does not establish production reliability, deadline compliance, rare-event coverage or certification。
- **Limitations / Threats to Validity:** other traffic participants are log replay and cannot react to ego actions；3DGS has weaknesses on
  non-rigid pedestrians, unseen views and low light；reward/termination relies on reconstructed geometry and expert path；high-risk clip
  selection narrows population；no event-time artifact, seeds, uncertainty, hardware or external reproduction；full environment and actor
  behavior may leak source-log assumptions into train/eval even with scene split。
- **Trade-offs / New Failure Modes:** IL regularization reduces policy drift but can preserve expert shortcuts；RL explores recovery states
  but can optimize renderer/reward artifacts and reduce smoothness；discrete decoupled actions accelerate learning but discard coupled
  dynamics；early termination avoids noisy rendered states but hides recovery-after-failure；parallel stale-policy rollouts require version
  control；3DGS realism increases asset cost and can create photorealistic yet non-causal counterfactuals。
- **Where the Previous Design Still Applies:** pure IL remains suitable for stable behavior cloning, scarce safe simulators and smoothness-
  first systems；verified modular planners/controllers remain preferable for interpretable constraints and certification；game-engine or
  physics simulators remain stronger when reactive actors/contact dynamics matter；real-world validation and safety monitors remain
  mandatory even when 3DGS RL is used as a post-training layer。
- **Evolution Relationship:** `Direct Evolution` from open-loop imitation to closed-loop policy-induced training；`Layering / Dependency`
  from demonstrations to 3DGS environment, PPO and IL regularization；`Alternative Branch` among pure IL, pure RL and hybrid updates；
  `Principle Reuse` of executable-environment evaluation。The new branch supplements rather than replaces IL and explicit simulation。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Current Ch26）canonical owner；`MULTIMODAL-WORLD-MODELS`
  owns simulator/world-state evidence boundary, `TRAIN-RLHF` and `TRAIN-PPO` own reward/PPO mechanics, and
  `PLATFORM-EVALUATION-SYSTEM` owns closed-loop evaluation/denominator contracts。
- **Target and Adjacent Chapters Read:** read Current Ch25 World Models and Ch26 Embodied AI/VLA end to end；read Ch31 RLHF,
  Ch32 PPO and Ch66 Evaluation System for reward, rollout and evidence ownership。Verified that the durable contribution is the
  IL-to-closed-loop hybrid control/evidence chain, not a generic autonomous-driving benchmark result。
- **Existing Coverage:** Ch25 already separates controllable simulator evidence from real environment truth and requires intervention-
  conditioned evaluation；Ch26 already owns action horizon, controller authority, sim-to-real and physical evidence ladder；Ch31/32 own
  proxy reward, on-policy state and clipping；Ch66 owns subject/environment/denominator identity。Future integration should refine their
  handoff around non-reactive digital twins and hybrid IL/RL, not append a paper summary or collision number。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added W08-v1-locked 30-field review, final score, three-stage state/control flow, disclosed
  evaluation/training contract, simulator and artifact limitations, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** event-time code/checkpoint/environment/data manifests and exact later-paper diff；policy architecture/parameter count,
  sensors, accelerator, precision, renderer throughput and total compute；reactive-agent and renderer-fidelity tests；real-road denominator,
  intervention/near-miss/deadline evidence；seed confidence intervals and environment leakage；stale-policy worker semantics；reward hacking,
  recovery after termination and independent reproduction。

### Decomposed Reward Models: Rethinking Diverse Human Preference Learning through PCA

- **Candidate / Week / Score:** Rethinking Diverse Human Preference Learning through Principal Component Analysis / 2025-W08 /
  26/30。
- **Source Family ID:** `decomposed-reward-models-preference-pca`。
- **Source Type:** arXiv research paper + paper-linked public datasets/models + later ACL Findings publication lineage。
- **First-public Date / Revision History:** arXiv v1 2025-02-18 18:55 UTC；W08 evidence is locked to v1。The ACL Findings
  2025 publication is later peer-reviewed lineage and is not used to move the event date or silently replace event-time claims。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13131；https://arxiv.org/html/2502.13131v1；
  https://arxiv.org/pdf/2502.13131v1。
- **Related Primary Sources:** paper-linked `mixture2_and_safe_pku` preference dataset, Gemma-2B-RM, Llama3-8B-RM,
  Gemma-2-9B-it, RewardBench and RPR define the experimental identities；https://aclanthology.org/2025.findings-acl.1019/
  is later publication lineage。No author code repository, immutable environment or PCA artifact was linked in v1。
- **Access and Verification Status:** Verified with reproducibility boundary；v1 full text, equations, tables, figures, appendix,
  limitations and linked model/data identities are accessible。No event-time code, dependency lock, feature dump, PCA basis, exact dataset
  revision, checkpoint digest or hardware record was found, so reported results are author experiments rather than reproduced evidence。
- **Full-read Coverage:** read metadata；Abstract/Introduction；Bradley-Terry preliminary；vector preference formulation；Taylor/PCA
  approximation and sign ambiguity；basis construction and HyRe-style adaptation；datasets/models/baselines；head diversity,
  RewardBench/RPR adaptation, attribute-correlation and sensitivity experiments；Related Work；Conclusion；Limitations/Ethics；all
  appendix ablations and implementation details。
- **Original Problem:** a scalar reward model compresses heterogeneous, sometimes conflicting preferences into one total order and tends
  to reflect majority labels；fine-grained multi-attribute annotations can preserve structure but are expensive。The system needs a way to
  expose multiple reward directions from widely available binary chosen/rejected pairs and adapt them with a small user-specific set。
- **Why the Previous Design Was Reasonable:** a single Bradley-Terry head is cheap, produces one stable scalar interface and is easier to
  optimize/audit；explicit attribute labels give semantic owners；trained multi-head models can learn task-directed dimensions。These remain
  preferable when a release policy requires a fixed global rubric, labels are available, or unconstrained latent directions are unsafe。
- **Changed Constraint:** personalization and plural preferences require more than one ordering, while per-user retraining and fine-grained
  labeling do not scale。A frozen feature extractor already contains high-dimensional response differences, so the design asks whether
  reusable directions can be recovered offline and reweighted at evaluation/runtime with only a few preference examples。
- **Mechanism:** compute `z_i = phi(x,y_chosen)-phi(x,y_rejected)`, center/normalize differences and apply PCA；each eigenvector and its
  negative become candidate linear reward heads over the frozen representation。The paper derives only an approximate relation between a
  regularized Bradley-Terry direction and a covariance eigenvector under small-logit Taylor expansion；PCA itself maximizes unsupervised
  variance。At test time, losses on a small adaptation set are softmaxed into coefficients that combine 100 signed heads into one reward。
- **State Ownership:** model/checkpoint owner controls feature geometry `phi`；dataset owner controls pair provenance and population；PCA
  job owns centering, eigenbasis, signs/order and version；adaptation session owns user examples, normalization and head weights；reward
  service owns the resulting composite scalar and revision；policy/evaluator owns how that scalar is consumed。A PCA component has no
  authoritative semantic label merely because it correlates with a benchmark slice。
- **Control Flow / Data Flow:** versioned preference pairs → frozen model embeddings for chosen/rejected responses → difference matrix
  `N x d` → centering/default scikit-learn PCA → signed top-100 reward heads → small attribute/user adaptation set → per-head BT loss →
  softmax mixture coefficients → composite reward scores → RewardBench/RPR decisions and attribute-correlation analysis。
- **Implementation Details:** training data has 550k mixed human/GPT-labeled pairs；backbones are Gemma-2B-RM, Llama3-8B-RM and
  Gemma-2-9B-it。PCA uses scikit-learn defaults；experiments use 50 principal vectors plus negative directions as 100 heads。Single-/
  shared-head baselines train one epoch with batch 16；test-time adaptation uses n=15 RewardBench or n=5 RPR examples and reports 20
  sampled adaptation-set repetitions；feature backbone remains frozen。
- **Evaluation Contract:** RewardBench measures Chat, Chat Hard, Safety and Reasoning；RPR uses five categories with more than 80 samples
  each。DRM, trained heads and random signed heads share the 100-head HyRe adaptation mechanism except the non-adaptive single head。
  Tables report accuracy/average and standard deviation over adaptation resamples；separate max-head analysis is an oracle diagnostic, not
  the deployed mixture result。Gemma-2-9B-it tests whether an instruction model can supply features。
- **Baselines / Ablations / Sensitivity / Overhead:** compares single head, trained shared-base ensemble, uniform/Gaussian random heads and
  PCA heads across three backbones；sweeps adaptation-set size and number of heads, with instability at n=3 and saturation around 100；
  visualizes all head scores and cross-attribute coefficient correlations。Missing: supervised multi-attribute oracle at equal labels,
  subgroup fairness, cross-dataset temporal drift, adversarial preference injection, feature/PCA version migration, latency/memory cost and
  policy-optimization outcomes。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models are Gemma-2B-RM, Llama3-8B-RM and Gemma-2-9B-it；
  training baseline batch is 16, dataset 550k pairs, adaptation n=5/15 and 100 signed heads。Accelerator, precision, sequence lengths,
  embedding-extraction/PCA wall time and memory, reward-serving batch/concurrency, tail latency, policy-rollout budget and SLO are Not
  Disclosed；therefore “lightweight/scalable” is not a measured production contract。
- **What the Evidence Actually Proves:** under the authors' frozen-backbone, mixed-preference, RewardBench/RPR setup, PCA directions in
  chosen-minus-rejected embeddings provide a more useful reweighting basis than tested scalar, trained-ensemble and random-head baselines；
  a small labeled adaptation set changes the operating point without updating backbone weights；different directions correlate with
  different benchmark attributes and performance saturates conditionally with more examples/heads。
- **What It Does Not Prove:** PCA eigenvectors are not proven to be true, causal or universal human preference factors；orthogonality in
  model feature space does not imply ethical independence or semantic disentanglement；max-over-head results do not represent an automatic
  selection policy；the experiments do not prove improved aligned generation, minority protection, real-user satisfaction, stable online
  personalization or immunity to reward hacking/bias。
- **Limitations / Threats to Validity:** the key PCA connection is an approximation with small inner-product and normalization assumptions；
  component sign is arbitrary；dataset mixes human and GPT labels and can encode source bias；only a fraction of 2048/4096 signed heads is
  inspected；attribute names are benchmark correlations；adaptation reuses a small labeled subset of the target population；no psychology/
  user study, code artifact, hardware, cross-time stability, confidence beyond resampling or independent reproduction。
- **Trade-offs / New Failure Modes:** decomposition exposes alternative reward directions but multiplies artifact/version/state surfaces；
  frozen features make adaptation cheap but couple all semantics to backbone revision；few-shot mixing can overfit or amplify malicious/
  idiosyncratic examples；PCA prioritizes variance, potentially elevating nuisance/bias；signed heads may express harmful inversions；one
  final weighted scalar can again hide conflicts unless coefficients and per-head evidence remain visible。
- **Where the Previous Design Still Applies:** scalar RM remains appropriate for one stable policy/rubric and minimal runtime state；
  explicitly labeled multi-objective heads remain stronger when dimensions must be named, governed and audited；per-user fine-tuning may
  fit persistent high-value users with sufficient data；random/ensemble uncertainty remains useful when no trustworthy PCA dataset exists。
- **Evolution Relationship:** `Direct Evolution` from one scalar reward to a versioned latent reward basis；`Alternative Branch` among
  explicit multi-attribute labels, learned multi-head ensembles, PCA heads and user-specific training；`Layering / Dependency` on frozen
  feature geometry and test-time adaptation。DRM does not replace scalar reward consumption or preference governance by itself。
- **ROADMAP Node:** `TRAIN-RLHF`（Current Ch31）canonical owner；`MODEL-EMBEDDING` owns representation geometry,
  `PLATFORM-EVALUATION-SYSTEM` owns attribute/scorer evidence and `PLATFORM-SECURITY` owns preference-data, harmful-direction and policy
  boundaries。PPO/DPO consume reward/preference signals but do not own decomposition semantics。
- **Target and Adjacent Chapters Read:** read Current Ch30 LoRA, Ch31 RLHF and Ch32 PPO；also read Ch66 Evaluation System。Verified
  that the durable addition is scalar-reward-to-versioned-basis evolution plus new ownership/failure modes, not a PCA tutorial or a list of
  benchmark gains；Ch30 remains an adjacent parameterization branch, not the mechanism owner。
- **Existing Coverage:** Ch31 already defines scalar Bradley-Terry reward, preference-population drift, reward hacking and RM/policy
  versioning, but does not yet give multidimensional reward basis an explicit lifecycle；Ch66 already requires population, scorer, slices
  and uncertainty。Future Books work may refine the existing pipeline with basis/adaptation identity and semantic-boundary warnings；it
  should not call PCA components “interpretable preferences” without qualification or append per-benchmark accuracy tables。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added W08-v1-locked 30-field review, final score, PCA/BT approximation boundary, basis/adaptation
  state flow, dataset/model/evaluation contracts, later-publication lineage and Stable Node mapping；no Books change。
- **Open Questions:** exact arXiv-to-ACL revision diff and event-time artifact；dataset/checkpoint/PCA-basis digests and preprocessing；
  compute, latency and storage；cross-model/dataset/time basis stability；component sign/semantic governance；real-user and minority-group
  evaluation；robustness to poisoned adaptation sets；calibrated multi-objective conflict handling；policy-optimization outcomes and reward
  hacking；whether supervised semantic heads outperform at equal annotation budget。

### MoM: Linear Sequence Modeling with Mixture-of-Memories

- **Candidate / Week / Score:** MoM: Linear Sequence Modeling with Mixture-of-Memories / 2025-W08 / 27/30。
- **Source Family ID:** `mom-routed-linear-recurrent-memory`。
- **Source Type:** arXiv technical report + author implementation repository + later revision/publication lineage。
- **First-public Date / Revision History:** arXiv v1 2025-02-19 12:53 UTC；v2 2025-05-06、v3 2025-10-09、v4
  2025-11-18。W08 evidence is locked to v1；later varlen implementation, model artifacts and ICLR 2026 acceptance are lineage,
  not event-time facts。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13685；https://arxiv.org/html/2502.13685v1；
  https://arxiv.org/pdf/2502.13685v1；https://github.com/OpenSparseLLMs/MoM。
- **Related Primary Sources:** https://github.com/OpenSparseLLMs/Linear-MoE is later integration lineage；Gated DeltaNet,
  RetNet, GLA, GSA and Transformer++ papers define baselines。The current repository README and ICLR/OpenReview version are used only
  to identify artifact evolution where they postdate W08。
- **Access and Verification Status:** Verified with version boundary；v1 HTML/PDF, equations, tables, appendix and current author
  repository are accessible。No immutable event-time commit, checkpoint digest, environment lock or independent reproduction was established；the
  September 2025 varlen implementation cannot be attributed to the February v1 event。
- **Full-read Coverage:** read metadata/revisions；Abstract/Introduction/Preliminary；router, recurrent update rules, memory mixing and
  shared-memory equations；v1 optimization description；training setup；recall, commonsense, LongBench, mixed-vs-expanded-memory,
  efficiency, loss and hyperparameter ablations；Related Work/Conclusion；MoM-vs-MoE, datasets and complete appendix tables；author
  repository dependencies, training/evaluation commands and later artifact notes。
- **Original Problem:** linear attention, SSM and linear RNN families compress all prior tokens into one fixed-size recurrent state。
  This removes sequence-growing KV storage but makes unrelated information compete for the same update surface, especially on
  recall-intensive tasks。
- **Why the Previous Design Was Reasonable:** one recurrent state gives linear training complexity, constant state size and simple
  per-token decode；forget/input gates cheaply control overwrite。Dense attention/KV remains stronger when exact token-addressable history
  is affordable；a single recurrent state remains attractive for short, local or memory-constrained workloads。
- **Changed Constraint:** longer and more heterogeneous sequences require greater recall capacity without returning to a KV cache that
  grows with sequence length。Simply widening one state increases capacity but does not isolate mutually interfering content, so state
  organization rather than only state size becomes the design variable。
- **Mechanism:** a learned linear router softmaxes over `M` memories, selects top-`k` and renormalizes selected weights。Each selected
  memory has memory-specific K/V projections and receives the underlying linear-recurrent update；unselected memories remain unchanged。
  A shared memory is updated by every token, while the query reads the weighted mixture of selected local memories plus shared memory。
- **State Ownership:** each layer owns router parameters, shared recurrent state and `M` local recurrent states；the router owns token-to-
  memory assignment and mixture weights；each local memory's K/V projections own its representation coordinate。Request/session reset,
  state serialization, migration, tenant isolation and router revision compatibility are Not Disclosed。
- **Control Flow / Data Flow:** token state → router scores → top-`k` memory ids/weights → memory-specific K/V projections → selected
  recurrent-state updates while other states remain unchanged → shared-state update → per-memory query outputs / weighted mixture →
  RMSNorm, Swish and output projection。Training groups routed subsequences for linear-recurrent processing；v1 only states reuse of
  Triton/chunkwise operators, while explicit varlen reorder kernels belong to later lineage。
- **Implementation Details:** v1 experiments instantiate MoM with Gated DeltaNet, four local memories, top-2 activation and one shared
  memory；the framework presents compatible update rules for LA, Lightning, RetNet, HGRN2, GLA, Mamba2, DeltaNet, Gated DeltaNet, TTT
  and Titans。Current repository requires PyTorch >=2.5, Triton >=3.0 and FLA-related dependencies, but these are current artifact facts,
  not a proven v1 lock。
- **Evaluation Contract:** 340M/24-layer/d=1024 models train on 15B SlimPajama tokens；1.3B/24-layer/d=2048 models use 100B tokens。
  Recall evaluation covers FDA, SWDE, SQuAD, NQ, TriviaQA and DROP with input truncated to 2K；commonsense/language-modeling uses
  WikiText, LAMBADA, ARC, HellaSwag, PIQA and WinoGrande；LongBench reports category averages。All results are author experiments。
- **Baselines / Ablations / Sensitivity / Overhead:** compares Transformer++, RetNet, HGRN2, GLA, GSA and Gated DeltaNet；matches
  training tokens and approximately parameter count, with some 1.3B baselines from public same-configuration weights。Tests expanded
  single memory versus routed memories, memory/activation counts `(2,1),(3,2),(4,2),(8,2)`, shared-memory removal, training loss and
  generated-1K-token speed/memory curves。No equal-quality production throughput, routing-collapse stress or multi-seed uncertainty study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 340M uses batch 0.5M tokens, 15B tokens and 0.25M warmup；
  1.3B uses batch 2M tokens, 100B tokens and 1B warmup；both use AdamW, lr 3e-4, cosine schedule, weight decay 0.01 and grad clip 1.0。
  Context is 2K for recall tasks；accelerator, precision, node/GPU count, training wall time, inference batch/concurrency and tail SLO are
  Not Disclosed in v1。Current repository's 4-node/8-GPU example is later operational guidance, not v1 experimental evidence。
- **What the Evidence Actually Proves:** within the authors' two model scales and disclosed datasets, routed multiple recurrent states
  outperform tested single-state linear baselines on average, with the clearest gains on recall-intensive tasks；the expanded-single-state
  comparison supports separation as more useful than equal activated capacity in two update families；shared memory and memory-count
  choices materially affect the tested operating point。
- **What It Does Not Prove:** the results do not prove elimination of memory interference, exact token recall, universal superiority over
  attention, production latency/throughput, arbitrary-length quality, or portability to every listed update rule。`O(1)` decode refers to
  asymptotic state with fixed `M,k,d`; it does not mean zero routing/state cost or constant quality as context grows。
- **Limitations / Threats to Validity:** v1 has no dedicated limitations section；English-heavy SlimPajama and small/model-specific tests,
  2K recall truncation, category-averaged LongBench, mixed trained/open checkpoints, single reported seed for loss, missing hardware and
  no independent reproduction constrain generality。The paper's specialization labels are post-hoc token inspection, not causal semantics。
- **Trade-offs / New Failure Modes:** more isolated state increases fixed memory, K/V projection parameters, routing and kernel/layout
  complexity；top-`k` can collapse, imbalance or partition related evidence；shared memory reintroduces interference；route changes across
  model revisions can invalidate serialized state。Sparse subsequences complicate batching, state reset/migration and fault recovery, and
  exact provenance/deletion is weaker than token-addressable KV or external memory。
- **Where the Previous Design Still Applies:** dense attention/KV remains appropriate for exact recall, short contexts and mature kernels；
  one recurrent state remains simpler when interference is low or device state is scarce；hybrid attention-recurrence remains preferable
  when selected exact retrieval layers justify sequence-growing state；external retrieval remains necessary for mutable, cited or deletable
  knowledge。
- **Evolution Relationship:** `Direct Evolution` from one gated recurrent state to a routed bank plus shared state；`Principle Reuse` of
  MoE top-k routing without sharing MoE's FFN-capacity objective；`Alternative Branch` against wider single state, dense attention/KV and
  hybrid recurrence-attention。Later varlen kernels are implementation evolution, not proof of the v1 runtime claim。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Current Ch22）canonical owner；`MODEL-MOE` owns routing analogy and load-balance concepts,
  `INFER-KV-CACHE` owns token-addressable state comparison, and `INFER-EXECUTION` owns irregular token grouping/kernel mapping。
- **Target and Adjacent Chapters Read:** read Ch21 MoE, Ch22 Long Context and adjacent Ch23 Multimodal Representation；also checked Ch19
  model-side KV, Ch45 inference KV and Ch49 execution-engine ownership。The owner is long-context state organization, not FFN expert
  capacity or a serving-framework feature。
- **Existing Coverage:** Ch22 already contrasts dense KV, hybrid recurrent state and migration from dense checkpoints；Ch21 already owns
  router/load-balance failure modes。Future Books work may refine Ch22's state-capacity evolution from gating → wider state → routed state
  bank → hybrid/token-addressable state, with short handoffs to Ch21/45/49；it must not append benchmark tables or call MoM a KV replacement。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added W08-v1-locked 30-field review, score, revision/artifact boundary, state/control flow,
  disclosed training/evaluation contract, non-proven claims, failure modes, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** event-time commit/checkpoints/config/dependency lock；v1 speed-figure hardware, precision and exact numbers；multi-seed
  uncertainty；router auxiliary loss and collapse under domain shift；state reset/migration/serialization and multi-tenant isolation；quality
  beyond 2K/32K and adversarial recall；equal-quality end-to-end throughput；exact diff across v2-v4 and later varlen integration。

### FLAG-Trader: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading

- **Candidate / Week / Score:** FLAG-Trader / 2025-W08 / 23/30。
- **Source Family ID:** `flag-trader-llm-policy-ppo`。
- **Source Type:** arXiv research paper + later ACL Findings publication lineage；no event-time code repository linked。
- **First-public Date / Revision History:** arXiv v1 2025-02-17 04:45 UTC, v2 2025-02-18, v3 2025-02-19；W08 uses
  v3, the last in-window revision。ACL Findings 2025 is later publication lineage, not a second event。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.11433；https://arxiv.org/html/2502.11433v3；
  https://arxiv.org/pdf/2502.11433v3。
- **Related Primary Sources:** https://aclanthology.org/2025.findings-acl.716/ is later peer-reviewed lineage；InvestorBench and
  FinRL papers define the comparison environment。No paper-linked immutable code, dataset snapshot or trained checkpoint was found。
- **Access and Verification Status:** Verified with reproducibility boundary；v3 full text, algorithms, hyperparameters, tables and
  limitations are accessible。Artifact, transaction-cost implementation, data digests and seeds are not disclosed, so returns are author
  backtest evidence only。
- **Full-read Coverage:** read metadata/revisions；Abstract/Introduction/Related Work；POMDP, state/action/reward definitions；prompt,
  partial-finetuning actor/critic, PPO/GAE algorithms；six-asset setup, dates, hardware, metrics, tables and selection rule；Conclusion,
  Limitations/Risk and appendices/hyperparameters；later ACL record。
- **Original Problem:** static LLM prompting does not optimize a policy for sequential environment feedback, while conventional trading
  RL struggles to combine textual and numerical state。The desired system must turn an LLM action distribution into a policy that can
  be updated by executable outcome reward。
- **Why the Previous Design Was Reasonable:** prompted LLM agents avoid expensive on-policy training and preserve base-model behavior；
  conventional RL uses compact numerical states and explicit risk controls。Both remain preferable when environment feedback is sparse,
  non-stationary, costly or unsafe to optimize directly。
- **Changed Constraint:** a repeated buy/hold/sell environment exposes delayed outcome feedback and requires adaptation across a sequence,
  not independent text completions。Full-model tuning is expensive, so only top LLM layers and separate heads are made trainable。
- **Mechanism:** template the market/account state as text；frozen lower LLM layers produce shared features, trainable upper layers feed a
  policy head and value head；invalid actions are masked。Rollouts collect state/action/reward transitions；GAE estimates advantage and PPO
  clips the policy ratio while value and entropy terms jointly update heads and trainable LLM layers。
- **State Ownership:** environment owns price/news/account transition and reward；prompt schema owns textual state identity；rollout buffer
  owns trajectories and old-policy probabilities；actor/critic share mutable upper-layer weights but own separate heads；deployment policy
  owner must own model/prompt/risk revision。Paper does not define durable replay/version/rollback semantics。
- **Control Flow / Data Flow:** market/account state → deterministic text template → frozen layers → trainable layers → masked action
  distribution/value → sampled buy/hold/sell → environment transition → Sharpe-increment reward → rollout buffer → GAE/returns → PPO
  minibatch update → new policy → next rollout。
- **Implementation Details:** SmolLM2-135M-Instruct；13,860 timesteps, one environment, 40-step rollout, one update epoch, lr 5e-4,
  gamma .95, GAE lambda .98, clip .2, entropy .05, value .5, KL .05, fp16, grad accumulation 8, minibatch 32 and max episode 65。
  Exact frozen/trainable layer split, optimizer identity, tokenizer/prompt digest and seeds are Not Disclosed。
- **Evaluation Contract:** MSFT/JNJ/UVV/HON/TSLA test 2020-10-01 through 2021-05-06 after 2020-07-01 through 09-30 warm-up；
  BTC test 2023-04-05 through 11-05 after 02-11 through 04-04 warm-up。Metrics are cumulative return, Sharpe, annualized volatility and
  max drawdown；reported trajectory is chosen by median metrics, prioritizing median Sharpe when epochs differ。
- **Baselines / Ablations / Sensitivity / Overhead:** compares buy-and-hold and InvestorBench prompting across 13 proprietary/open models。
  It does not compare against a same-135M supervised/no-RL model, numeric PPO with equal features/compute, transaction-cost/slippage variants,
  multiple seeds, rolling out-of-time windows or risk-constrained objective；therefore LLM contribution and PPO contribution are not isolated。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** FLAG model 135M, fp16, minibatch 32, one environment；inference
  temperature .6。Paper says <10B models use two RTX A6000, 10B–65B four A6000 and >65B eight A100 80GB, but does not disclose exact
  FLAG training placement, sequence length, wall time, serving latency/concurrency or SLO。
- **What the Evidence Actually Proves:** in the authors' six historical single-asset trajectories, a partially trainable 135M LLM actor-
  critic can be optimized end-to-end with PPO and achieves the reported operating points against the tested prompt-only baselines。It is a
  concrete example of external environment reward changing model policy parameters rather than only ranking static responses。
- **What It Does Not Prove:** it does not prove profitable deployment, causal superiority of language representation, stable optimal-policy
  convergence, robustness across market regimes, value after fees/slippage/tax/market impact, or advantage over equal-budget conventional RL。
  Larger prompt-only models versus tuned 135M are not an equal-training comparison。
- **Limitations / Threats to Validity:** six assets, one contiguous test window per market, median-trajectory selection, no seeds/error bars,
  no transaction-cost and leakage audit, unspecified data provenance, no code, non-stationarity and prompt bias。Reward optimizes return
  proxy without explicit risk constraints；financial outcomes are high-variance and cannot be generalized from this backtest。
- **Trade-offs / New Failure Modes:** environment gradients provide direct adaptation but add rollout cost, policy lag, reward hacking,
  non-stationary critic error and catastrophic change in shared upper layers。Text encoding is convenient but can lose numeric precision；
  shared actor/critic representation can couple errors；invalid-action masks prevent syntax errors but not unsafe concentration or stale data。
- **Where the Previous Design Still Applies:** prompt-only LLM remains safer for advisory/non-executable use；feature-extractor plus governed
  numeric policy better isolates language semantics from action authority；conventional RL is simpler for fully numerical state；human/risk
  approval remains required for high-stakes deployment。
- **Evolution Relationship:** `Layering / Dependency` from prompt action generation to environment-coupled actor-critic training；`Principle
  Reuse` of PPO rather than a new PPO algorithm；`Alternative Branch` between prompt-only agent, LLM feature extractor, partially tuned LLM
  policy and conventional policy network。
- **ROADMAP Node:** `TRAIN-PPO`（Current Ch32）canonical owner；`TRAIN-RLHF` owns reward/proxy governance, `AGENT-WORKFLOW` owns durable
  environment execution, `PLATFORM-EVALUATION-SYSTEM` owns backtest contract and `PLATFORM-SECURITY` owns action authority/risk boundaries。
- **Target and Adjacent Chapters Read:** read Ch31 RLHF, Ch32 PPO and Ch33 GRPO；checked Ch66 Evaluation, Ch72 Security and Ch81 Workflow
  ownership。The durable content is environment-coupled policy training/evidence boundary, not financial strategy advice。
- **Existing Coverage:** Ch32 already explains actor, critic, rollout, GAE, clipping, version alignment and reward correctness；Ch81 already
  separates model proposal from durable execution。Future Books work would at most add a short non-language environment-reward branch and
  high-stakes backtest gate；the paper does not justify a finance chapter or benchmark table。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added W08-v3-locked 30-field review, score, POMDP/state flow, disclosed backtest/hardware contract,
  equal-comparison gaps, high-stakes failure modes, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** event-time code/data/checkpoint/prompt and layer-split digests；fees, slippage, market impact and leakage；seeds and
  rolling regime tests；equal-feature/equal-compute numeric PPO and no-RL ablations；risk-constrained reward, live shadow evaluation,
  intervention/rollback and independent reproduction。

### SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

- **Candidate / Week / Score:** SoFar / 2025-W08 / 28/30。
- **Source Family ID:** `sofar-semantic-orientation-6dof`。
- **Source Type:** arXiv research paper + author project page + later official code/model/dataset/evaluation artifact lineage。
- **First-public Date / Revision History:** arXiv v1 2025-02-18 18:59 UTC；v2 2025-09-24，later accepted as
  NeurIPS 2025 Spotlight。W08 event is locked to v1；v2 is used to verify the mature mechanism and evidence boundary, not as a
  second W08 event or proof that September appendices/artifacts were public in February。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.13143v1；https://arxiv.org/pdf/2502.13143v1；
  https://arxiv.org/html/2502.13143v2。
- **Related Primary Sources:** https://qizekun.github.io/sofar/；https://github.com/qizekun/SoFar；
  https://github.com/Zhangwenyao1/SimplerEnv-SOFAR；https://huggingface.co/collections/qizekun/sofar。
- **Access and Verification Status:** Verified with revision/artifact boundary。v1 metadata, abstract, first-public time and the
  48.7% Open6DOR / 74.9% SIMPLER headline are accessible；the 37 MB v1 PDF exceeded the current fetch path's content limit。
  The full v2 HTML, appendices, project, current code, checkpoints/datasets and evaluation repository are accessible；therefore details
  absent from v1 abstract are marked as later-revision evidence rather than silently backdated event facts。
- **Full-read Coverage:** read v1 metadata/abstract/revision record；v2 Abstract/Introduction/Related Work；semantic-orientation
  definition, OrienText300K construction/validation, PointSO architecture/loss, 6-DoF scene graph and planning flow；real/sim robot
  setups, Open6DOR V2, SIMPLER and SpatialBench evaluations；semantic-orientation, scale, fusion and detector ablations；training recipes,
  model sizes, failure distribution, limitations, broader impacts and artifact documentation；author project/current repositories。
- **Original Problem:** VLM spatial reasoning usually localizes objects and coarse relations but does not expose task-relevant object
  orientation。A robot that knows where a USB, knife or cup is still cannot infer the plug-in, cutting or handle direction needed for
  6-DoF manipulation。
- **Why the Previous Design Was Reasonable:** canonical frames, CAD templates, quaternions and task-specific pose estimators are precise,
  compact and verifiable when object classes, fixtures and calibration are fixed；position-only scene graphs are sufficient for coarse
  pick-and-place。Their limitation appears in open-vocabulary objects where the relevant axis depends on instruction and function。
- **Changed Constraint:** open-world language instructions select different functional axes for the same object, while partial RGB-D
  observations, unseen shapes and multiple embodiments prevent a single category template from defining all useful orientations。
- **Mechanism:** define semantic orientation as a language-conditioned unit vector `s_l^X = F(X,l)` on the sphere；build
  OrienText300K from filtered Objaverse multi-view assets and language-view annotations；PointSO patchifies point clouds with FPS/KNN and
  PointNet, injects a frozen CLIP text feature into every 3D Transformer layer, and predicts the vector under cosine loss。SoFar asks a
  VLM for task objects/orientation phrases, uses Florence-2+SAM and RGB-D to recover object point clouds, calls PointSO, constructs a
  6-DoF scene graph, then asks the VLM for target position/orientation before a grasp/motion stack executes it。
- **State Ownership:** sensor/calibration pipeline owns RGB-D and coordinate transforms；detector/segmenter owns instance masks；PointSO
  owns provisional phrase-conditioned direction estimates；the scene graph owns object ID, centroid, size and orientation-set revision；
  VLM owns a proposed target transform；grasp/motion controller owns executable trajectory；environment and verifier own outcome truth。
  Calling semantic orientation “reference-frame-free” describes the language interface, not the final robot execution frame。
- **Control Flow / Data Flow:** instruction+RGB-D → VLM extracts task object phrases and functional directions → Florence-2/SAM masks →
  depth+calibration form object point clouds → PointSO predicts semantic unit vectors → versioned 6-DoF scene graph → VLM decomposes
  desired transform → grasp/trajectory proposal → robot controller → environment transition → observation/verifier → optional re-perception
  and replan。The later closed-loop demo uses a second VLM check; its transaction, deadline and safety semantics are Not Disclosed。
- **Implementation Details:** later v2 reports PointSO-S/B/L with 11.4M/19.0M/43.6M parameters, frozen CLIP ViT-B/32, 10K
  input points, 512 patches of 32 points, random rotation/partial-view/noise augmentation and cosine objective。OrienText300K filters
  roughly 800K Objaverse assets to 350K+ objects and renders 8M views；a 208-sample manual validation reports 88.3% filtering and
  97.1% annotation accuracy。Current repository uses Python/PyTorch, Florence-2, SAM, PointSO and optional Qwen2.5-VL/API VLMs；
  event-time commit, dependency lock and released checkpoint/data state are Not Disclosed。
- **Evaluation Contract:** v1 exposes author-reported 48.7% Open6DOR and 74.9% SIMPLER results。Later v2 defines Open6DOR V2
  with 4,535 tasks across position/rotation/6-DoF tracks, SIMPLER Google Robot and Widow-X tasks, 223 human-annotated four-choice
  SpatialBench samples, and 60 real-world tasks across >100 objects with three trials per task。Those v2 details sharpen the evidence
  contract but are not assumed to have been public at the W08 event date。
- **Baselines / Ablations / Sensitivity / Overhead:** compares GPT-4V, Dream2Real, VoxPoser, Open6DOR-GPT, Octo/OpenVLA and
  spatial VLM/VLA baselines under different perception/execution contracts。Later ablation changes no-CoT/no-orientation 6-DoF overall
  14.2 to orientation-only 45.8 and full 48.7；PointSO-Base average rises 42.58→72.46 from 15K→350K data；addition fusion beats
  reported alternatives and Florence-2 is compared with Grounding DINO/YOLO-World。Baseline training data, detector, controller and
  evaluation opportunity are not fully equal, so the headline is not a model-only comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** later v2 trains PointSO variants and SoFar-LLaVA on
  8×H800；PointSO batch 256 for 300 epochs, SoFar-LLaVA batch 128 for two epochs。Open6DOR perception table reports 8.5 s for
  SoFar and Libero execution about 40 s；precision, VLM token length, API/network latency, concurrent robots, control frequency, power and
  tail SLO are Not Disclosed。These figures do not establish real-time production control。
- **What the Evidence Actually Proves:** the author system operationalizes a useful separation between open-vocabulary functional
  direction and execution-frame pose；PointSO predicts language-conditioned 3D directions, and the later controlled ablation supports that
  supplying orientation state—not CoT alone—improves the authors' Open6DOR rotation/6-DoF metrics。The paper also demonstrates that a
  modular perception→typed scene state→proposal→controller path can connect VLM reasoning to simulated and limited real actions。
- **What It Does Not Prove:** it does not prove reference frames are unnecessary, universal open-world 6-DoF competence, causal world
  understanding, safety certification, real-time control, robustness to arbitrary occlusion/symmetry/calibration drift, or superiority over
  every end-to-end VLA。Current code/artifacts do not prove event-time reproducibility, and author benchmarks do not transfer unchanged to
  other robots, cameras, controllers or SLOs。
- **Limitations / Threats to Validity:** v1 full-text access gap in this run；later-revision/artifact drift；GPT-4o-generated data and
  small manual annotation audit；author-created benchmarks and component-dependent comparisons；Open6DOR has about 8% initially satisfied
  scenes；real tasks have three trials；no broad independent reproduction。Later failure audit attributes 31% of failures to grasping, 23%
  to semantic orientation, about 20% to detection, plus VLM planning, collisions/deadlocks and workspace omissions。
- **Trade-offs / New Failure Modes:** semantic directions generalize beyond fixed categories but add phrase ambiguity, object symmetry,
  multi-axis inconsistency and language/data bias。A modular pipeline improves diagnosability and component replacement but multiplies stale
  state, coordinate-transform, detector, depth, grasp, collision and planner failure modes；closed-loop re-perception reduces open-loop
  exposure but adds latency, verifier error and repeated-action risk。
- **Where the Previous Design Still Applies:** canonical CAD/fixture frames remain better for standardized industrial parts and certified
  cells；category-specific pose models remain efficient when vocabulary is closed；position-only planning remains adequate for tolerant
  pick-and-place；verified skills and low-level controllers remain necessary for contact-rich, high-rate or high-consequence tasks。
- **Evolution Relationship:** `Direct Evolution` from position-only to orientation-aware scene state；`Layering / Dependency` from
  semantic direction to calibrated pose, controller and feedback；`Alternative Branch` between canonical/template pose, modular semantic
  orientation and end-to-end VLA；`Principle Reuse` of language-conditioned typed state rather than language directly owning actuators。
- **ROADMAP Node:** `MULTIMODAL-EMBODIED-VLA`（Current Ch26）canonical owner；`MULTIMODAL-REPRESENTATION` owns
  point/language representation identity, `MULTIMODAL-WORLD-MODELS` owns predictive transition, and
  `PLATFORM-EVALUATION-SYSTEM` owns benchmark/run evidence。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch25 World Models, Ch26 Embodied AI/VLA and Ch66
  Evaluation。Ch26 already owns coordinate/action/controller/safety boundaries；SoFar is a future constrained case, not a new chapter or
  permission to move control authority into the VLM。
- **Existing Coverage:** Ch23 already defines modality, coordinate, artifact and provenance identity；Ch26 already gives the modular
  perception→proposal→controller evolution, state ownership, coordinate mismatch and evaluation ladder。Future Books work could refine
  Ch26's position→canonical pose→function-conditioned semantic direction→typed target pose route, but must not append SoFar tables or
  call the language interface physically reference-frame-free。
- **Integration Decision:** `Books Pending — Integration Deferred`；Source-Family evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added revision-bounded 30-field review, score, state/control flow, later evaluation/hardware
  contract, ablation, failure distribution, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** exact v1→v2 content diff and event-time artifact；v1 full PDF text；independent replication；symmetric/ambiguous
  objects and multi-vector consistency；calibration/occlusion sensitivity；confidence and abstention；closed-loop deadline/idempotency；
  collision-aware planning；real trial denominator across robots；tail latency, control rate, intervention and safety evidence。

### Craw4LLM: Web Crawling Should Optimize Training Utility, Not Only Graph Popularity

- **Candidate / Week / Score:** Craw4LLM / 2025-W08 / 26/30。
- **Source Family ID:** `craw4llm-quality-aware-web-crawling`。
- **Source Type:** arXiv paper + author repository + later ACL Findings record。
- **First-public Date / Revision History:** arXiv v1 2025-02-19 00:31 UTC；v2 2025-02-24、v3 2025-06-23。
  W08 mechanism and evaluation claims are locked to v1；v2/v3 and the later ACL 2025 record are lineage evidence only。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13347v1；https://arxiv.org/abs/2502.13347；
  https://github.com/cxcscmu/Craw4LLM。
- **Related Primary Sources:** https://aclanthology.org/2025.findings-acl.712/；the DCLM scorer and ClueWeb22 papers define
  the quality signal and static crawl graph, but do not independently reproduce Craw4LLM。
- **Access and Verification Status:** Verified with artifact and event-time boundaries；v1 HTML, metadata/revisions and current
  author repository are accessible。The event-time immutable environment, model checkpoint, crawl snapshot digest and executable
  reproduction manifest are not public；later ACL/v3 material is not projected backward into W08。
- **Full-read Coverage:** read v1 metadata, Abstract/Introduction/Related Work, Algorithm 1, scorer/frontier state, ClueWeb22 setup,
  DCLM pretraining recipe, all main result and overlap/correlation analyses, implementation/runtime disclosure, limitations and
  conclusion；checked repository layout and later revision/publication lineage。
- **Original Problem:** crawl-then-filter can download and retain a large raw corpus even though the final pretraining pipeline rejects
  most pages。A crawler optimized for broad discovery or graph popularity does not necessarily prioritize pages that improve a target model under
  a fixed data and compute budget。
- **Why the Previous Design Was Reasonable:** random/graph-connectivity crawling provides broad, scorer-independent coverage；global
  indegree and PageRank-like signals are cheap conceptual proxies for importance, while post-filtering preserves a reusable raw archive
  and separates network acquisition from rapidly changing model-quality policy。
- **Changed Constraint:** when fetch/storage cost and website load matter, and a usable pretraining-influence scorer already exists,
  the quality signal can move upstream into the frontier scheduler。The system goal changes from maximizing graph coverage to maximizing
  downstream model utility per acquired document, without assuming that popular pages are always useful training data。
- **Mechanism:** start from seed URLs, fetch the current batch, add pages to the crawled corpus, extract outlinks, score each unseen
  discovered page with a pretraining-influence classifier, and place its URL in a priority queue；the next batch is the top-scoring
  frontier。The loop stops when the target corpus size is reached。This is a selection-policy change, not a new foundation-model objective。
- **State Ownership:** seed set plus scorer/model/version own the crawl policy；visited set `V` owns URL deduplication；priority queue
  `Q` owns the ranked frontier；crawled set `P` owns the selected corpus；fetcher owns the observed page snapshot；the later data pipeline
  and training run own final filtering, manifests and checkpoint lineage。No single headline “crawl ratio” covers all these states。
- **Control Flow / Data Flow:** `seed → fetch batch → extract outlinks → fetch/score unseen pages → priority queue → dequeue top-n
  frontier → repeat → 20M-document corpus → tokenize/pretrain 411M DCLM model → downstream evaluation`。Because scoring an unseen page
  requires obtaining its content, `P` (selected/crawled corpus) and `V` (all visited/fetched pages) must be reported separately。
- **Implementation Details:** the paper simulates crawling over the English ClueWeb22-A graph from 10K random seeds；batch size is
  10K URLs per iteration and the target is 20M documents。The scorer is DCLM fastText。A priority queue replaces FIFO/random or global
  indegree ordering；the public repository contains the simulator and training/evaluation entry points, but not an event-time frozen
  crawl snapshot/checkpoint/container bundle。
- **Evaluation Contract:** final datasets contain 20M documents / 32.9B tokens。Each dataset trains a 411M decoder-only Transformer
  (24 layers, 8 heads, model width 1024, head dimension 128, sequence length 2048) with the DCLM 4× Chinchilla recipe and is evaluated
  on 23 reported task entries / 22 unique downstream tasks using centered accuracy。Each training experiment is run once。
- **Baselines / Ablations / Sensitivity / Overhead:** compares random and global-indegree crawlers at 1×/2×/4× acquisition budgets
  plus an oracle that applies the scorer to the full 45× pool。For the DCLM scorer, centered accuracy is 0.2133 for Craw4LLM 1×,
  0.1748/0.1964 for random 1×/2×, 0.1556/0.1865 for indegree 1×/2× and 0.2239 for oracle。The paper analyzes
  oracle overlap over crawl progress and reports about 0.61/0.60 1-hop/2-hop score correlation。No multi-seed error bars,
  scorer-removal test, live-network A/B test or diversity/fairness ablation is disclosed。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** pretraining uses 8×NVIDIA L40S for about 1 day 12 hours
  per run；crawl simulation uses two Intel Xeon E5-2630 v3 processors, 16 total cores, 125 GiB RAM and SSD, with v1 reporting about
  one day for the 20M crawl。Training precision, tokenizer details, crawler concurrency, network bandwidth, request politeness,
  tail latency, failure/retry policy and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under this static English ClueWeb22 simulation, DCLM scorer, 20M/32.9B-token corpus and
  411M-model contract, moving the quality signal into frontier prioritization changes graph traversal and improves average downstream
  centered accuracy over the tested random/indegree baselines；it reaches 95.3% of the reported oracle score。It supports co-designing
  collection policy with downstream data utility。
- **What It Does Not Prove:** it does not prove real-web traffic reduction, production crawl throughput, legal/compliance safety,
  multilingual or live-web generalization, larger-model scaling, scorer independence or universal quality。The 21% headline compares
  selected crawl set sizes；once every visited/scored page is counted, the paper estimates 48%, so it is not literal total HTTP reduction。
- **Limitations / Threats to Validity:** static crawl simulation omits robots.txt, rate limits, fetch failures, content drift, malicious
  pages, revisit/freshness policy and distributed queue recovery。Global indegree receives graph information unavailable to a local live
  crawler。Selection and oracle share the DCLM quality family, introducing circularity risk；one training run per condition provides no
  uncertainty estimate；English ClueWeb22 and a 411M model bound external validity。
- **Trade-offs / New Failure Modes:** utility-aware crawling can reduce low-value acquisition and improve model-targeted yield, but
  adds inference cost, a large scored frontier, scorer/version coupling and recovery state。A biased scorer can collapse language/domain
  coverage, amplify existing model preferences, create feedback loops, starve fresh or niche sources and turn policy updates into
  irreproducible corpus drift。Fetching pages for scoring also consumes the resource the scheduler is supposed to save。
- **Where the Previous Design Still Applies:** connectivity-first crawling remains appropriate for broad discovery, search indexing,
  cold start, weak/unstable scorers and diversity preservation；post-filtering remains useful when bulk acquisition is cheap, raw archives
  must support many downstream objectives, or governance requires independent reprocessing。Hybrid/multi-objective frontiers are a
  branch, not proof that graph signals are obsolete。
- **Evolution Relationship:** `Direct Evolution` for `connectivity/popularity crawl → crawl then quality-filter → quality-aware
  prioritized frontier`；next pressure is a multi-objective scheduler combining utility, coverage, freshness, politeness, legal/risk and
  failure recovery rather than maximizing a single learned score。
- **ROADMAP Node:** owner `TRAIN-DATA` (Current Ch27, Legacy Ch23)；handoffs to `TRAIN-PRETRAINING`, `PLATFORM-COST` and
  `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** read Ch27 Data and Ch28 Pretraining, plus ROADMAP Part IV contract；Ch27 owns collection,
  filtering, mixture, provenance and executable data policy, while Ch28 owns the optimization run and cannot retroactively validate the
  corpus。Cost/security remain platform handoffs rather than crawl-policy owners。
- **Existing Coverage:** Ch27 already states that collection protocol defines the upstream sample distribution and that filtering can
  bias language/domain coverage, but it does not yet trace the evolution from post-hoc filtering to an upstream utility-aware frontier or
  distinguish selected corpus state from every page fetched for scoring。This is a real future refine candidate, not a new chapter。
- **Integration Decision:** `Books Pending — Integration Deferred`；Weekly evidence complete, Historical Books Gate closed。
- **Changed Files or Rejection Reason:** added W08-v1-locked 30-field review, final score, `P/V/Q` state ownership, exact evaluation
  contract, 21% versus 48% accounting boundary, limitations, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** independent real-web replication；event-time commit/data/checkpoint/container；scorer drift and calibration；
  multilingual/domain diversity guardrails；quality-versus-coverage Pareto frontier；robots/politeness/legal policy；distributed queue
  checkpoint/recovery；exact fetch/inference/network cost and whether benefits survive larger models and unrelated quality scorers。

### PC-Agent: Hierarchical GUI Automation Needs Explicit Perception, Task and Feedback State

- **Candidate / Week / Score:** PC-Agent / 2025-W08 / 24/30。
- **Source Family ID:** `pc-agent-hierarchical-gui-workflow`。
- **Source Type:** arXiv research paper + author repository；the currently visible repository is later artifact lineage, not a
  paper-pinned event-time implementation。
- **First-public Date / Revision History:** arXiv v1 2025-02-20 05:41 UTC；v2 2025-02-21 02:54 UTC。Both revisions belong to W08；
  this review uses v1 for the event-time mechanism and checks v2 metadata as same-week lineage。The repository already contained older
  Mobile-Agent code in 2024, while the updated PC-Agent code and PC-Eval files appeared in March 2025, so current files are not projected
  backward as the exact February artifact。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14282v1；https://arxiv.org/abs/2502.14282；
  https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent。
- **Related Primary Sources:** the paper's PC-Eval task definitions and the repository's later `PC-Eval.json`, agent prompts and
  perception/action modules expose evaluation and implementation lineage；they do not independently reproduce the paper results or
  disclose the event-time environment。
- **Access and Verification Status:** Verified with revision and artifact boundaries。The complete v1 HTML and current author repository
  are accessible；an immutable event-time commit, model/API snapshot, Windows image, application versions, prompt bundle and executable
  reproduction manifest are Not Disclosed。
- **Full-read Coverage:** read v1 metadata, Abstract/Introduction/Related Work, Active Perception Module, hierarchical Manager/Progress/
  Decision/Reflection agents, action space and control loop, PC-Eval construction, main comparison, component/model ablations, recovery
  analysis, appendices, limitations and conclusion；checked the current repository layout, prompts, perception helpers and release lineage。
- **Original Problem:** desktop tasks contain dense visual and accessibility elements, inter-application dependencies and long action
  sequences。A monolithic screenshot-to-action agent must simultaneously remember the global objective, infer subtask dependencies,
  ground coordinates, diagnose failures and decide the next action, so errors and stale context compound across the trajectory。
- **Why the Previous Design Was Reasonable:** a single agent minimizes coordination calls and shared-state ambiguity；native accessibility
  APIs or direct application APIs are cheaper and more deterministic when available；short, low-risk tasks with a strong base model do not
  necessarily benefit from extra roles or natural-language handoffs。
- **Changed Constraint:** cross-application workflows require explicit dependency state and communication between subtasks, while PC
  interfaces mix accessibility-visible controls with text or icons that need visual/OCR grounding。The system must separate global
  decomposition, local progress, action proposal and post-action diagnosis without assuming one observation channel is complete。
- **Mechanism:** Active Perception combines accessibility-tree elements rendered as set-of-mark boxes with an intention-conditioned OCR
  path for target text。The Manager decomposes the instruction into parameterized subtasks and passes results through a communication hub；
  the Progress Agent summarizes local progress；the Decision Agent selects a constrained GUI action；the Reflection Agent compares pre/post
  screenshots and classifies the action as wrong, ineffective or correct, feeding the diagnosis into subsequent decisions。
- **State Ownership:** the Manager owns the subtask dependency graph, ordering and inter-subtask result hub；the Progress Agent owns an
  advisory summary, not authoritative workflow state；the Decision Agent proposes an action；the automation runtime executes it；the
  Reflection Agent owns advisory visual diagnosis, not commit or rollback。The paper does not expose durable workflow authority,
  transaction boundaries, permissions, leases, idempotency keys or a side-effect journal。
- **Control Flow / Data Flow:** `instruction → Manager decomposition/parameterization → active subtask → Progress summary → accessibility/
  OCR observation → Decision action proposal → pyautogui execution → before/after Reflection → progress update → Manager result hub and
  next dependency`。A retained conversation/progress prefix can guide later actions, but it is not an event-sourced replay of external state。
- **Implementation Details:** the paper uses `pywinauto` to obtain interactive accessibility elements, set-of-mark overlays, OCR for
  text localization and `pyautogui`-style GUI actions。The action vocabulary includes opening apps, click/double-click, text selection,
  typing, drag, scroll, shortcuts and stop。The current repository separates chat/API, crop, icon localization, text localization, merge
  strategy and prompt modules, but its later state cannot prove the exact v1 runtime behavior。
- **Evaluation Contract:** PC-Eval contains 25 instructions decomposed into 79 subtasks across Chrome, Word, Excel, Notepad, Clock,
  Calculator, Outlook and File Explorer。Three annotators perform human evaluation。The default hierarchy uses GPT-4o for all four agents
  and OpenOCR；single-agent, UFO and Agent-S comparisons use the same action space and GPT-4o where reported。
- **Baselines / Ablations / Sensitivity / Overhead:** reported subtask/instruction success is 76%/56% for PC-Agent, 55.7%/24% for Agent-S,
  43%/12% for UFO and 41.8%/8% for the GPT-4o single agent。Removing Active Perception, Manager or Reflection yields 58.2%/20%,
  50.6%/12% and 48.1%/12%。With the hierarchy, Gemini 2, Claude 3.5, Qwen2.5-VL and GPT-4o achieve 55.7%/28%, 63.3%/40%,
  32.9%/12% and 76%/56%；the weak-backbone result shows that extra orchestration can reduce rather than monotonically improve capability。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** GPT-4o is the default agent model and OpenOCR is the OCR
  component。Hardware, precision, context length, token/API budget, agent concurrency, latency distribution, cost, retry policy and SLO are
  Not Disclosed。The results therefore cannot support an equal-cost or production-latency comparison。
- **What the Evidence Actually Proves:** on this small Windows productivity benchmark with human scoring, explicit active perception,
  hierarchical task/progress/action state and before/after feedback form a workable integration；the component ablations support their
  relevance under the authors' setup。The model ablation also supplies counter-evidence to the claim that multi-agent scaffolding is always
  beneficial。
- **What It Does Not Prove:** it does not prove that hierarchy alone causes the gain at equal calls/cost, that visual reflection restores
  external state, that the workflow is durable or crash-safe, or that PC-Agent generalizes beyond the eight tested applications。It also
  does not establish production authorization, privacy, irreversible-side-effect safety or an executable correctness oracle。
- **Limitations / Threats to Validity:** 25 instructions, human judgment, no repeated seeds/error bars and no automatic end-state verifier
  limit statistical and correctness claims。Comparisons entangle role count, prompts and model calls；accessibility/OCR state can be missing
  or stale；screenshot deltas can miss hidden application state；the later repository is not the event-time artifact。
- **Trade-offs / New Failure Modes:** role separation reduces prompt overload and localizes responsibilities, but adds calls, latency,
  handoff loss, contradictory summaries and multiple stale views of the same workflow。Active perception improves dense-element grounding
  but creates accessibility/OCR merge conflicts。Reflection can detect visible no-ops yet can incorrectly bless a visually plausible but
  semantically wrong side effect；without a transaction log, retry can duplicate irreversible actions。
- **Where the Previous Design Still Applies:** a single agent or direct API remains preferable for short tasks, strong native semantics,
  tight latency/cost budgets and low side-effect risk。Hierarchical orchestration becomes plausible when tasks are decomposable and the
  communication tax is lower than the context and error-recovery benefit；it is a conditional branch, not a one-way replacement。
- **Evolution Relationship:** `Direct Evolution` for `monolithic screenshot-action loop → specialized perception → instruction/subtask/
  action-state decomposition → bottom-up feedback`；the next pressure is durable typed workflow state, authorization, idempotent execution,
  executable evaluation and rollback-aware side-effect handling。
- **ROADMAP Node:** owner `AGENT-WORKFLOW` (Current Ch81, Legacy Ch77)；handoffs to `AGENT-MULTI-AGENT`, `AGENT-TOOL`,
  `AGENT-REFLECTION` and `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** read Ch78 Tool Calling, Ch79 Planning, Ch80 Reflection, Ch81 Workflow and Ch82 Multi-Agent。
  Tool Calling owns typed proposal/execution authority；Planning owns dependency graphs；Reflection owns evidence-backed diagnosis；Workflow
  owns durable authoritative state；Multi-Agent owns task/state/communication decomposition。PC-Agent remains a bounded GUI case across
  these owners rather than a new canonical mechanism owner。
- **Existing Coverage:** current Books already state that perception is a tool, action proposal is not execution authority, subgoals require
  dependency state, reflection requires evidence, workflow progress must be durable and multi-agent gains depend on decomposability versus
  communication tax。PC-Agent adds useful bounded evidence and the weak-backbone counterexample, but no new long-lived mechanism requiring
  immediate Books modification while the Historical Books Gate is closed。
- **Integration Decision:** `Books Pending — Integration Deferred`；likely future disposition is `No Change — Already Covered` or a small
  evidence-bound refinement after the 2025 Evidence Gate, not a paper-summary insertion。
- **Changed Files or Rejection Reason:** added a revision-bounded 30-field review, final score, role/state ownership, control flow,
  evaluation contract, failure modes, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** event-time commit and environment image；application/API/model snapshots；equal-call/equal-cost ablation；automatic
  end-state verifier；hidden-state and accessibility/OCR disagreement handling；permissions, secret handling, idempotency, crash recovery,
  irreversible-side-effect policy, tail latency and independent reproduction。

### S2R: From Imitating Long Traces to Training a Verify-and-Correct Action Grammar

- **Candidate / Week / Score:** S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning / 2025-W08 / 26/30。
- **Source Family ID:** `s2r-verify-correct-reasoning-rl`。
- **Source Type:** arXiv v1 research paper + author code/data repository + later ACL 2025 publication lineage。
- **First-public Date / Revision History:** arXiv v1 2025-02-18 13:40 UTC；no later arXiv revision is listed。The later ACL 2025
  publication and current repository are lineage, not additional W08 events。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12853v1；https://arxiv.org/abs/2502.12853；
  https://github.com/NineAbyss/S2R。
- **Related Primary Sources:** https://aclanthology.org/2025.acl-long.1104/；the repository supplies SFT/RL data, online/offline
  training scripts and Qwen evaluation tooling。Current `main` is not an immutable paper-pinned environment and does not independently
  reproduce the reported results。
- **Access and Verification Status:** Verified with artifact boundary。The only arXiv version, full HTML, equations, appendices and current
  author repository are accessible；event-time commit, container, dataset/checkpoint digests and run logs are Not Disclosed。
- **Full-read Coverage:** read metadata, Abstract/Introduction/Related Work, solve/verify action grammar, behavior-initialization data,
  masked SFT objective, outcome RLOO, process group-based RL, offline RL, all main/cross-domain/ability analyses, baselines, prompts,
  hyperparameters, environment, metric definitions, offline filtering/baseline ablations, risk discussion and current artifact layout。
- **Original Problem:** small and medium base models do not reliably acquire long-horizon reasoning merely by receiving a prompt to think
  longer。Distilling long traces requires a strong teacher and can teach stylistic length without teaching when an intermediate answer is
  wrong, whether to retry, or when to stop。
- **Why the Previous Design Was Reasonable:** direct SFT on correct solutions is simple, stable and cheap；long-CoT distillation can transfer
  useful paths when the teacher is strong；outcome-only RL avoids hand-labeling every intermediate step。For short or already-easy tasks,
  an explicit verify/correct loop adds tokens and opportunities to overturn a correct answer。
- **Changed Constraint:** the target is adaptive test-time effort on weaker policies using small behavior data and automatically checkable
  answers。Training must expose failed attempts without optimizing their tokens as desired solutions, then assign credit either to the final
  answer or to typed intermediate solve/verify actions。
- **Mechanism:** inference is represented as an alternating action sequence `solve → verify → solve` after an `incorrect` parse, or
  `solve → verify → <end>` after a `correct` parse。Stage 1 builds one-to-four-round trajectories from the base model's own distinct failed
  attempts, confirmative verifications and a final correct solution；masked SFT optimizes every verification plus only the final correct
  solution and `<end>`。Stage 2 branches into trajectory-level RLOO or action-level group-based process RL, with online and offline forms。
- **State Ownership:** the policy owns generated solve/verify text；a parser maps free-form verification conclusions to binary state；the
  golden-answer verifier owns correctness labels；the data builder owns difficulty bins, trajectory length and filtering；`pi_old` owns the
  rollout snapshot, `pi_ref=pi_SFT` owns the KL anchor, and the optimizer owns parameter updates。The model's self-verdict is an observation,
  not authoritative ground truth。
- **Control Flow / Data Flow:** `problem → sample base-policy attempts → golden check → external confirmative verification/refinement →
  filter and assemble failed-attempt/verification/final-correct trajectory → masked SFT → sample typed trajectories → parser + rule rewards →
  outcome or process advantage → clipped/KL-constrained update → greedy benchmark evaluation`。Offline RL adds prompt-difficulty filtering,
  rejection of malformed/overlong trajectories and fixed-dataset updates。
- **Implementation Details:** confirmative verification asks a model to assess an answer without re-solving, then uses GPT-4o to refine
  phrasing and append a parseable conclusion；invalid judgments are filtered。SFT masks failed solve attempts, preserving them as context but
  not positive token targets。Outcome RLOO uses the final solution reward and leave-one-out baseline over four samples；process RL assigns
  separate solve/verify rewards and groups actions by preceding reward context。Offline runs sample eight trajectories per prompt, retain
  moderate-difficulty prompts, reject malformed sequences and cap trajectories at 20 actions。
- **Evaluation Contract:** behavior initialization uses 4,614 MATH examples for Llama-3.1-8B-Instruct, 4,366 for Qwen2-7B-Instruct and
  3,111 for Qwen2.5-Math-7B；RL uses 9,601 or 10,000 prompts。Evaluation uses greedy Pass@1 on MATH500, AIME 2024, AMC 2023,
  College Math, text-only OlympiadBench, GSM8K and GaokaoEn 2023, plus FOLIO, CRUXEval, StrategyQA and MMLU-Pro STEM for the
  Qwen2.5-Math cross-domain check。
- **Baselines / Ablations / Sensitivity / Overhead:** compares base/instruct models, equal-size original-solution and QwQ long-CoT SFT,
  reported frontier/reasoning models, behavior initialization, online outcome/process RL and offline variants。Verification analysis separates
  overall accuracy from correct-answer and incorrect-answer slices；correction analysis separates incorrect-to-correct from correct-to-
  incorrect transitions。Offline ablations vary prompt-accuracy ranges and baseline grouping；several external baselines are copied from
  their reports rather than rerun under one compute contract。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** PyTorch 2.1.1, BF16, 32×H20 96GB or 32×A100Pro 40GB for
  training；single A100 40GB with vLLM 0.5.4 for inference。SFT batch 32, learning rate `5e-6`, three epochs and max length 6K/8K；
  online RL batch 64, forward batch 256, four samples per prompt, learning rate `5e-7`, 500 steps, temperature 0.7 and clip 0.2。
  Wall time, FLOPs, energy, token totals, cost, inference output lengths, concurrency and latency/SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under three 7B/8B base models and the disclosed math-centric contract, structured behavior
  initialization plus rule-reward RL improves the authors' greedy accuracy and measured verification/correction rates。For Qwen2.5-Math-7B,
  behavior initialization moves MATH500 from 51.0% to 81.6%, while online outcome RL reaches 84.4%；these are bounded author results, not a
  general scaling law。The process/outcome comparison supports different credit-assignment branches rather than one universal winner。
- **What It Does Not Prove:** it does not prove that generated natural-language verification is faithful internal reasoning, that the same
  model is an independent oracle, or that self-correction improves open-ended and non-verifiable tasks。It does not provide equal-compute
  evidence against every baseline, deployment latency/cost, multi-seed uncertainty, adversarial verifier robustness or production safety。
- **Limitations / Threats to Validity:** training and primary evaluation are math-heavy；cross-domain evidence uses one model and four
  benchmarks。Trajectory construction conditions on eventually reaching a correct answer and uses external judge/refinement, creating
  selection and teacher leakage。Difficulty is estimated from the same policy's sampled accuracy；parser conventions and exact-answer
  matching can be gamed。The paper has no dedicated limitations section, and its brief risk claim does not analyze verifier hacking,
  misleading rationales, extra compute or capability misuse。
- **Trade-offs / New Failure Modes:** typed alternation makes credit assignment and stopping observable, but consumes longer sequences,
  more rollout compute and a brittle parser/reward pipeline。Process rewards offer denser supervision yet can over-constrain exploration or
  reward convincing intermediate text；outcome rewards preserve path freedom yet give coarse credit and can reinforce accidental success。
  Self-verification can accept a wrong answer, reject a correct one, loop, learn formatting hacks or correlate with the original error。
- **Where the Previous Design Still Applies:** direct answer/SFT remains suitable for easy, short and latency-sensitive tasks；long-CoT
  distillation remains useful when a strong teacher and high-quality traces exist；outcome-only RL remains preferable when only terminal
  correctness is reliable；external verifiers/search remain necessary when same-policy error correlation or high-risk correctness dominates。
- **Evolution Relationship:** `Direct Evolution` for `correct-solution imitation → long-trace imitation → typed trial-and-error behavior
  initialization → outcome/process RL → adaptive attempts`；`Alternative Branch` for online versus offline RL and outcome versus process
  credit。The next pressure is calibrated independent verification, explicit compute budgets and evidence-backed stopping beyond exact-answer math。
- **ROADMAP Node:** owner `TRAIN-GRPO` (Current Ch33, Legacy Ch29)；handoffs to `TRAIN-SFT`, `TRAIN-RLHF`, `TRAIN-PPO`,
  `AGENT-REFLECTION`, `MODEL-SAMPLING` and `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** read Ch29 SFT, Ch31 RLHF, Ch32 PPO, Ch33 GRPO, Ch79 Planning, Ch80 Reflection and Ch66
  Evaluation。Part IV owns parameter training and reward/rollout contracts；Part VII owns inference-time evidence-backed repair；Evaluation
  owns verifier calibration and workload evidence。The natural-language action loop does not move training ownership into Agent runtime。
- **Existing Coverage:** Ch29 already owns masked demonstration targets and teacher/selection bias；Ch31–33 already distinguish proxy reward,
  KL anchor, rollout policy, process versus outcome supervision and verifiable reasoning；Ch80 already states that same-model critique is weak
  evidence and stopping must be bounded。S2R contributes a strong, explicit bridge between behavior grammar and RL credit assignment, but
  Historical Books Gate is closed and no paper-summary insertion is warranted now。
- **Integration Decision:** `Books Pending — Integration Deferred`；future Books Gate should consider `Refine — Existing Argument` for the
  SFT-to-reasoning-RL evolution, while preserving the external-verifier and compute-budget boundary。
- **Changed Files or Rejection Reason:** added the complete version-locked Source Review, score, action/state ownership, online/offline and
  process/outcome branches, workload contract, limitations, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** event-time commit, immutable data/checkpoint/environment and run logs；multi-seed confidence intervals；equal-token/
  equal-FLOP/cost comparisons；parser/judge sensitivity；reward hacking and adversarial verification；longer/open-ended tasks；calibrated
  stop/abstain behavior；independent replication and whether gains persist when verification requires external tools or evidence。

### Selective Question Answering: From Always-answer Accuracy to Risk-conditioned Operating Points

- **Candidate / Week / Score:** Is That Your Final Answer? Test-Time Scaling Improves Selective Question Answering / 2025-W08 / 27/30。
- **Source Family ID:** `selective-qa-test-time-compute-risk-utility`。
- **Source Type:** arXiv v1 research paper + author code repository + later ACL 2025 publication lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 18:58:31 UTC；v2 was submitted 2025-07-18 and the
  ACL 2025 short-paper record is later publication lineage。W08 mechanism and evaluation claims are locked to v1；later AIME25/GPQA
  scripts and publication changes are not back-projected into the event-time evidence。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13962v1；https://arxiv.org/abs/2502.13962；
  https://github.com/wjurayj/final_answer。
- **Related Primary Sources:** https://aclanthology.org/2025.acl-short.50/ records the later accepted version。The current repository
  documents the generation → incremental-answer → plotting workflow, but `main` is not an immutable v1 commit and now includes AIME25
  and GPQA paths absent from the v1 paper。
- **Access and Verification Status:** Verified with revision/artifact boundary。The v1 HTML, equations, figures, appendices and current
  author repository are accessible；paper-pinned commit, container, model digests, raw per-example run artifacts and independent
  reproduction are Not Disclosed。
- **Full-read Coverage:** read metadata and both revision dates, Abstract, Introduction, Methods, compute-budget enforcement, confidence
  selection, experimental setup/results, utility definition and three risk scenarios, Related Work, Conclusion, explicit Limitations,
  Appendix background/implementation details, supplemental figures and current repository workflow。The later ACL page was read only for
  publication lineage, not as W08 mechanism evidence。
- **Original Problem:** test-time scaling work commonly reports accuracy under an always-answer, zero-penalty contract。That metric hides
  whether a model knows when not to answer and cannot compare systems when an incorrect response carries task-specific harm, human escalation
  is available, or deployment policy trades answer coverage against risk。
- **Why the Previous Design Was Reasonable:** always-answer accuracy is simple, reproducible and appropriate for exams or search settings
  where a guess has no extra penalty；natural EOS respects the model's learned stopping distribution；a single accuracy curve avoids choosing
  a subjective business utility。When refusal has no value and compute is cheap, abstention can trivially lower useful coverage。
- **Changed Constraint:** reasoning systems can spend variable sequential compute and operate in settings where correct, incorrect and
  abstained outcomes have different value。The deployment decision therefore needs a joint operating surface over compute budget,
  confidence threshold, coverage, conditional accuracy and error cost rather than one unconditional accuracy number。
- **Mechanism:** reasoning budget is represented by trace-token count and strictly forced: predicted end-of-thinking delimiters are ignored,
  `Wait` is appended when reasoning ends early, and the delimiter is force-decoded at the budget boundary。Answer confidence is the sum of
  answer-token log probabilities；a threshold accepts or abstains。Utility assigns `+1` to correct, `0` to abstain and task-specific
  `r_t` to incorrect answers, with v1 evaluating Exam `0`, Jeopardy `-1` and High-Stakes `-20` odds。
- **State Ownership:** runtime owns token budget, forced-continuation and stop policy；model decoding owns answer tokens and their local
  log probabilities；the selection policy owns threshold and accept/abstain decision；EvalSpec owns task loss, coverage definition and
  aggregation；deployment policy owns whether to answer, defer or request human review。Model confidence is an observation, not correctness
  authority, and the paper provides no external verifier。
- **Control Flow / Data Flow:** `question + model/checkpoint → fixed-budget forced reasoning trace → final three-digit answer + token
  log probabilities → confidence sum → threshold comparison → answer or abstain → correctness label + task-specific error cost → coverage,
  answered-question accuracy and utility surface`。A production extension would feed the observed operating point back to scheduling or
  human escalation, but v1 does not implement dynamic budget allocation。
- **Implementation Details:** v1 evaluates budgets from 500 to 8,000 reasoning tokens in steps of 100 and thresholds `{0.0, 0.5, 0.95}`。
  All AIME24 answers are normalized to three digits `000–999`, avoiding variable answer-token length in the confidence sum。Generation uses
  temperature 0, a modified vLLM path from the s1 evaluation stack, then extracts incremental answers and recreates plots in notebooks。
- **Evaluation Contract:** DeepSeek-R1-Distill-Qwen-32B and s1-32B are evaluated on the 30 English AIME24 problems。For every
  budget/threshold pair, the paper reports answered-question accuracy and response coverage, then evaluates the same runs under three utility
  functions。The contract measures selective numeric math QA, not open-ended generation, calibrated real-world deferral or production serving。
- **Baselines / Ablations / Sensitivity / Overhead:** the comparison is between two open 32B reasoning checkpoints, three thresholds and
  dense budget sweeps。Threshold zero is the conventional always-answer baseline；higher thresholds expose coverage/accuracy trade-offs。
  There is no held-out threshold calibration, alternative confidence estimator, external-verifier baseline, natural-EOS versus forced-budget
  ablation, compute-priced utility, multi-seed uncertainty or end-to-end latency/cost sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** one node with 4×H100 GPUs, about four hours, two 32B models,
  temperature 0, 500–8,000 reasoning tokens and 30 AIME24 questions are disclosed。H100 memory size, precision/quantization, checkpoint
  hashes, prompt/context length, batch/concurrency, power/cost, TTFT/TPOT and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under this small numeric-math contract, compute budget and confidence threshold form a two-dimensional
  operating surface rather than a single monotonic accuracy curve。Higher thresholds reduce coverage and can improve accuracy among answered
  items；with high thresholds, more compute can admit harder lower-confidence questions so conditional accuracy may fall while coverage and
  utility change differently。The author runs also show R1 separates correct and incorrect answer confidence more clearly than s1 under the
  reported conditions。
- **What It Does Not Prove:** it does not prove that longer reasoning monotonically improves correctness, answer log probability is calibrated
  probability, threshold `0.95` is optimal, or Jeopardy odds represent a universal risk policy。It does not show that forced `Wait` preserves
  natural decoding, that the result extends to variable-length/open-ended answers, or that selective answering alone is safe for medical,
  legal or physical-action systems。
- **Limitations / Threats to Validity:** only 30 AIME24 items, English math, two related 32B models and three hand-chosen risk levels are
  evaluated；thresholds are not calibrated on a separate set and no error bars are reported。Equal three-digit answers hide length
  normalization issues；confidence and correctness share the same model；forced continuation changes the decoding distribution。The utility
  assigns no abstention or compute cost and omits domain shift, human deferral quality, subgroup risk and verifier failure。
- **Trade-offs / New Failure Modes:** abstention reduces costly errors but can deny service, shift work to humans and hide weak coverage；more
  reasoning may discover correct answers but consumes KV/slots/energy and can move lower-confidence items across the acceptance threshold。
  Simple log-probability thresholds are inspectable but model/version/task dependent；forced budgets improve experimental control while
  introducing unnatural continuation, looping and truncated-final-answer risk。A risk-weighted scalar clarifies one policy but can conceal
  hard safety constraints and unequal error costs across slices。
- **Where the Previous Design Still Applies:** always-answer accuracy remains useful for zero-penalty exams and regression testing；natural
  EOS remains preferable for short or latency-sensitive requests and models with reliable stopping；fixed budgets remain easier to admit and
  reproduce when calibration data are scarce；external verifiers, rules or human review remain necessary when correctness and side effects
  dominate model-relative confidence。
- **Evolution Relationship:** `Direct Evolution` from `always-answer accuracy → confidence-conditioned coverage/accuracy surface →
  risk-weighted utility operating point`；`Layering / Dependency` toward scheduler budget allocation and Agent defer/continue policy；
  `Alternative Branch` between natural EOS, fixed forced budget, adaptive budget, parallel sampling and external verification。The paper
  does not establish a single replacement path among these branches。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Current Ch66；Legacy Ch62）canonical owner；`MODEL-SAMPLING` owns
  token/log-probability and stopping semantics, `INFER-SCHEDULING` owns resource/deadline allocation, `AGENT-PLANNING` owns continue/stop/
  defer decisions, and `PLATFORM-COST` / `PLATFORM-SECURITY` own resource and high-impact constraints。
- **Target and Adjacent Chapters Read:** read Ch66 Evaluation, Ch67 Monitoring and Ch70 Cost boundaries, plus Ch20 Sampling, Ch56
  Inference Scheduling and Ch79 Planning。Evaluation owns utility, coverage and operating-point evidence；the other chapters own how the
  signal is produced or acted upon, so this paper must not be duplicated as four independent mechanisms。
- **Existing Coverage:** Ch66 already requires risk-conditioned EvalSpec, complete subject identity, uncertainty, hard constraints and
  Pareto rather than blind scalar comparison；Ch20 already distinguishes forced test-time budget, confidence and correctness；Ch56 records
  actual budget/route in traces；Ch79 binds uncertainty, action cost and abstention。This source adds a precise bounded case for the joint
  `budget × threshold × coverage × utility` surface, but Historical Books Gate is closed。
- **Integration Decision:** `Books Pending — Integration Deferred`；future Books Gate should consider `Refine — Existing Argument` in
  Ch66, using the operating-surface mechanism without copying the AIME-specific threshold as a general policy。
- **Changed Files or Rejection Reason:** added the version-locked 30-field Source Review, final score, code/revision boundary, workload
  contract, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** event-time repository commit and exact v1 code path；held-out and slice-aware calibration；variable-length confidence
  normalization；natural-EOS/forced-budget ablation；dynamic budget allocation；compute and abstention costs；external verifier/human deferral
  quality；multi-seed uncertainty, domain shift, production SLO and independent replication。

### SafeRoute: From One Guard for Every Request to Pair-specific Safety Escalation

- **Candidate / Week / Score:** SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models /
  2025-W08 / 27/30。
- **Source Family ID:** `saferoute-pair-specific-safety-guard-routing`。
- **Source Type:** arXiv v1 research paper + public guard-model artifacts + later Findings of ACL 2025 publication lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 02:51:17 UTC；v2～v5 were submitted 2025-05-19～22。
  W08 claims are locked to v1；later revisions and Findings publication are lineage, not additional February events。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12464v1；https://arxiv.org/abs/2502.12464。
- **Related Primary Sources:** https://aclanthology.org/2025.findings-acl.105/；official Hugging Face model artifacts named by v1 are
  `meta-llama/Llama-Guard-3-1B`, `meta-llama/Llama-Guard-3-8B`, `ibm-granite/granite-guardian-3.0-8b`,
  `answerdotai/ModernBERT-large` and `meta-llama/Llama-3.1-8B-Instruct`。No author implementation repository is cited in v1 or
  uniquely recoverable from the paper metadata。
- **Access and Verification Status:** Verified with artifact limitation。The v1 HTML, equations, theorem/proof, all experiment sections,
  appendices and explicit limitations are readable；training code, event-time commit, router checkpoint, augmented dataset, container,
  raw traces and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read metadata and five-version history, Abstract/Introduction/Related Work, guard preliminaries, oracle observation,
  routing-label construction, paraphrase augmentation, frozen-feature parameterization, inference threshold, risk bound and proof, six-dataset
  setup, all baselines, both guard pairs, latency/FLOPs/large-use trade-offs, pooling/layer/augmentation ablations, jailbreak analysis,
  Conclusion, Limitations, Ethics and all appendices/model identifiers。
- **Original Problem:** always running a large safety guard adds latency and FLOPs to every request, while replacing it with a distilled small
  guard saves cost but misses a minority of cases the larger guard can classify correctly。Small-model uncertainty alone does not reveal
  whether the large guard would actually repair the error, so naive escalation can pay large-model cost without safety benefit。
- **Why the Previous Design Was Reasonable:** one large guard gives a simple and conservative control path；one small guard provides bounded
  latency and easier capacity planning；entropy or calibrated-confidence routing needs no paired error labels。When workload, policy and guard
  behavior are stable, these designs are easier to validate and fail over than a learned third decision component。
- **Changed Constraint:** production wants large-guard quality at closer-to-small-guard cost across prompt-only and prompt-response moderation。
  The useful escalation set is pair-specific: examples where this exact small guard is wrong and this exact large guard is correct under a
  fixed taxonomy, threshold and dataset—not every example on which the small guard is uncertain。
- **Mechanism:** construct target `t=1` only when the large guard predicts the ground-truth label correctly and the small guard predicts it
  incorrectly；all other pairs receive `t=0`。Paraphrase the labeled training pairs seven times, reuse the frozen small guard's final-layer
  last-token representation, and train a three-layer Bayesian binary router。At inference, route to the large guard when router score exceeds
  `epsilon`; otherwise return the small guard's harmfulness prediction。
- **State Ownership:** safety taxonomy, harmfulness label and decision threshold belong to the policy/evaluation contract；small and large
  guard checkpoints own their logits and representations；dataset builder owns pair-specific correction labels and synthetic paraphrases；
  router artifact owns escalation score/threshold；Gateway or serving control owns invocation and fallback；deterministic policy owner retains
  final allow/deny authority。The learned router and guards are sensors, not authorization principals。
- **Control Flow / Data Flow:** `prompt + optional response + policy/taxonomy → small guard forward → harmfulness logits + cached final-token
  representation → SafeRoute score → small-path verdict OR invoke paired large guard → selected guard verdict → deterministic enforcement /
  human escalation → trace guard/router/policy identities and outcome`。Training first runs both guards against labeled WildGuardMix to create
  the correction-target dataset, then augments and fits the frozen-feature router。
- **Implementation Details:** v1 uses a three-layer Bayesian network with affine + LayerNorm + ReLU except the output layer, diagonal-Gaussian
  posterior, `N(0,0.1)` prior, KL weight `0.01` and one Monte Carlo sample for train/inference。It trains 1,000 epochs with batch 512,
  approximately balanced target classes, Adam LR `0.001`, linear decay and 100 warmup steps；10% of WildGuardMix train is validation and
  Llama-3.1-8B-Instruct produces seven paraphrases per original pair。
- **Evaluation Contract:** train on WildGuardMix and evaluate prompt-only moderation on WildGuardMix-p, OpenAI Moderation and ToxicChat,
  plus prompt-response moderation on WildGuardMix, XSTest and HarmBench。Guard pairs are Llama-Guard-3-1B with either Llama-Guard-3-8B
  or Granite-Guardian-3-8B。Evidence includes routing-target F1 and downstream safety-F1 versus latency, FLOPs and large-model usage ratio。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines are small-only, large-only, 50% random, small-guard entropy, temperature,
  contextual and batch calibration, plus an oracle with true labels。Ablations vary pooling, representation source/layer and paraphrase count；
  five seeds are reported only for stochastic Random and SafeRoute。Threshold sweeps produce trade-off curves, but there is no policy-costed
  false-negative analysis, failover test, traffic-concurrency study or guard-version sensitivity experiment。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** one NVIDIA H200 GPU, 1B small guard, two alternative 8B large guards,
  8B paraphraser, batch 512 and five stochastic seeds are disclosed。H200 memory size, precision/quantization, prompt/response lengths,
  inference batching/concurrency, cold/warm cache, router/guard latency decomposition, throughput, power/cost and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** for the disclosed guard pairs and six public datasets, learning the pair-specific correction event
  routes rare useful escalations better than small-model entropy/calibration baselines and produces stronger author-measured safety-F1/
  compute trade-off curves on most datasets。The ablations support reusing the small guard's last-token final-layer feature and show the
  paraphrase benefit saturating under this setup。
- **What It Does Not Prove:** it does not prove large guards are always safer, the router preserves a required false-negative ceiling, or
  average F1 is an adequate production safety objective。It does not establish robustness to unseen attacks, taxonomy/policy revisions,
  new guard versions, adversarial router evasion, correlated blind spots, multilingual traffic, online batching or independent deployment。
  The theorem bounds expected BCE risk by router mismatch under a finite second-moment assumption; it is not a safety certificate。
- **Limitations / Threats to Validity:** v1 explicitly notes that router inputs encode only what the small guard knows; adding large-guard
  features can become slower than always running the large model。Router quality depends heavily on representative training data near the
  hard/easy boundary。Additional threats include synthetic-paraphrase artifacts, approximate class balancing that changes training priors,
  fixed benchmark taxonomies, average-F1 masking false-negative slices, untested version drift and no released implementation/run evidence。
- **Trade-offs / New Failure Modes:** adaptive escalation can save large-guard work, but adds a third artifact, threshold, training pipeline,
  cache/feature coupling and route decision to a security-critical path。Router false negatives silently keep a weak verdict；false positives
  erode latency/cost gains。Updating either guard changes target semantics and requires router recalibration/retraining；large-guard outage
  needs explicit fail-open/fail-closed or human fallback。Paraphrase augmentation improves coverage while potentially reproducing generator bias。
- **Where the Previous Design Still Applies:** large-only guard remains preferable for low-volume/high-risk traffic or weak router evidence；
  small-only remains valid for strict latency/cost paths with accepted residual risk；entropy/calibration remains simpler when pair labels are
  unavailable；deterministic rules and human review remain stronger for enumerable high-impact policies。Speculative-style layered execution
  does not replace independent enforcement or post-deployment monitoring。
- **Evolution Relationship:** `Direct Evolution` from `large guard everywhere → distilled small guard everywhere → uncertainty-based escalation
  → pair-specific correction routing`；`Alternative Branch` among small-only, large-only, calibrated entropy, learned router and deterministic/
  human escalation；`Layering / Dependency` toward Gateway execution, Evaluation operating points and Cost accounting。Later routing does not
  invalidate the simpler branches where their assumptions hold。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Current Ch72；Legacy Ch68）canonical owner；`PLATFORM-GATEWAY` owns trusted invocation/
  fallback, `PLATFORM-EVALUATION-SYSTEM` owns false-positive/negative and operating-point evidence, `PLATFORM-COST` owns resource accounting,
  and `INFER-SCHEDULING` owns serving resource/deadline decisions。
- **Target and Adjacent Chapters Read:** read Ch71 Multi Tenant, Ch72 Security and Ch73 Production boundaries, plus Ch62 Gateway, Ch66
  Evaluation, Ch70 Cost and Ch56 Inference Scheduling。Security owns the policy-bound sensor/authority and fail-safe contract；Gateway owns
  request-path enforcement, while Evaluation and Cost prevent a routing-F1 or average-latency curve from becoming a production safety claim。
- **Existing Coverage:** Ch72 already defines learned guard output as policy-bound sensor, preserves deterministic authorization and requires
  policy/version/evaluation/fallback identity；Ch62 owns fail-open/fail-close and request routing；Ch66 rejects average scores without risk
  slices。SafeRoute adds a concrete `small guard → pair-specific escalation → large guard` mechanism and its drift/failure state, but the
  Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Integration Deferred`；future Books Gate should consider `Refine — Existing Argument` in Ch72,
  preserving large-only, small-only, learned routing and deterministic enforcement as conditional branches rather than a product recipe。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, score, correction-target semantics, state/control path,
  evaluation and theorem boundary, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** author code/router checkpoint/augmented data and event-time environment；per-slice false-negative ceilings；policy/taxonomy
  and guard-version drift；adversarial routing attacks；multilingual/OOD coverage；large-guard failure policy；threshold calibration under real
  class priors；latency decomposition, batching/concurrency/SLO/cost；independent replication and continuous router retraining governance。

### RelaCtrl: From Uniform Control-branch Duplication to Relevance-budgeted Conditional Generation

- **Candidate / Week / Score:** RelaCtrl: Relevance-Guided Efficient Control for Diffusion Transformers / 2025-W08 / 25/30。
- **Source Family ID:** `relactrl-relevance-budgeted-dit-control`。
- **Source Type:** arXiv research paper + official project visualization page + later revision/publication lineage；no public author code or checkpoint artifact was identified。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 09:10:05 UTC；v2 submitted 2025-02-21 10:02:02 UTC and is the latest in-window owner revision。v3 2025-02-28、v4 2025-03-23 and v5 2026-02-26（AAAI 2026 comment）are later lineage and are not back-projected into W08。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14377v2；https://arxiv.org/abs/2502.14377；https://360cvgroup.github.io/RelaCtrl/。
- **Related Primary Sources:** https://arxiv.org/html/2502.14377v1 records the first-public paper；https://relactrl.github.io/RelaCtrl/ mirrors the visualization page。The pages expose examples and method figures, not implementation, immutable weights or run artifacts。
- **Access and Verification Status:** Verified with revision and artifact boundary。The complete latest in-week HTML, equations, proof appendix, training/evaluation appendices and project page are accessible；source code, event-time commit, checkpoint/data digests, optimizer recipe, raw runs and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read v2 metadata and five-version history, Abstract/Introduction/Related Work, relevance-prior construction, full architecture, RGLC/TDSM equations and theorem/corollary proofs, all four-condition comparisons, efficiency and component/placement ablations, training appendix, 27/13-block relevance checks, Flux experiment, community-model examples, Conclusion/Impact Statement and project page。No dedicated Limitations section exists。
- **Original Problem:** DiT controlled-generation branches commonly copy a fixed prefix of backbone blocks or concatenate extra control tokens。These designs preserve a strong frozen generator but spend similar capacity at every insertion point even when a control condition affects layers unequally, adding substantial parameter, FLOP and memory overhead。
- **Why the Previous Design Was Reasonable:** duplicating the first 13 PixArt blocks gives a simple one-to-one residual injection path, preserves pretrained main weights and avoids first discovering a task-specific placement policy；token concatenation keeps parameter growth small and lets ordinary attention mix condition information。When compute is available, implementation simplicity, predictable shapes or unseen conditions matter more than efficiency, uniform control remains a defensible baseline。
- **Changed Constraint:** high-resolution conditional generation makes duplicated attention/FFN work expensive, while the relevant control signal can concentrate in only part of a frozen DiT。The design must allocate insertion positions and per-position modeling capacity under a fixed quality/control budget rather than assume every layer deserves the same branch。
- **Mechanism:** first train a 27-copy-block PixArt-alpha control network, skip one control block at a time during inference and combine normalized FID/HDD ranks into a ControlNet Relevance Score。Select the top 11 positions rather than the first 13；at each selected point replace copied attention+FFN with a Relevance-Guided Lightweight Control block。Its Two-Dimensional Shuffle Mixer randomly partitions/shuffles channel-token space, applies grouped local attention, restores original ordering, and assigns wider channel groups to higher-relevance positions before zero-convolution residual injection。
- **State Ownership:** the frozen DiT owns base generation semantics；the condition extractor owns Canny/HED/depth/segmentation inputs；offline analysis owns CRS values and selected positions；the RGLC artifact owns per-position group configuration and residual parameters；sampler/runtime owns latent trajectory and inference schedule；evaluation owns FID/HDD/MSE-depth/mIoU/CLIP operating evidence。A high CRS is a workload-derived design signal, not semantic or causal layer authority。
- **Control Flow / Data Flow:** `image/text corpus → derive four control conditions → train full copied control branch → leave-one-block-out inference → rank FID and HDD impact → freeze top-k positions/capacity policy → train RGLC/TDSM branch → text + condition + timestep + corresponding frozen feature → shuffle/group attention → inverse recovery → zero-conv residual injection → diffusion sampling → quality/control/efficiency evaluation`。
- **Implementation Details:** RGLC adds a zero-convolved frozen feature to condition state, applies residual TDSM and another zero convolution before merging into the main branch。TDSM jointly shuffles spatial token and channel dimensions, computes attention inside local groups and inversely restores positions；the theorem lower-bounds expected interactive distance after random grouping, but does not establish semantic equivalence to global attention。The selected 11 positions and relevance-conditioned group widths are fixed artifact configuration, not an online request-adaptive scheduler。
- **Evaluation Contract:** a curated 1.73M-image dataset with aesthetic score at least 5.5 supplies HED, Canny, depth and segmentation conditions。Quantitative models train at 512 resolution and evaluate COCO val 5,000；qualitative models train at 1024 and test 1,000 high-quality images。All reported trials use five epochs on 16 NVIDIA A100 GPUs。Quality uses FID, CLIP-Aesthetics and CLIP Score；control uses HDD, MSE-depth or mIoU depending on condition。
- **Baselines / Ablations / Sensitivity / Overhead:** compares official Uni-ControlNet, UniControl, ControlNet-XS and ControlNext weights, while PixArt-delta and RelaCtrl are retrained under the same stated settings。Ablations compare first-13 with relevance top-13/12/11/10, original copied blocks versus RGLC, uniform versus relevance-conditioned TDSM capacity, 27- versus 13-block relevance profiles, and a Flux.1-dev extension。Most cross-backbone baselines are not equal-data/equal-training comparisons；no multi-seed uncertainty, joint-subset search or online-drift test is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** main efficiency numbers use PixArt-alpha, 512 resolution, BF16, batch 1 and one NVIDIA A100；CLIP/T5 encoder memory is excluded。The base is 611.15M parameters, 542.56 GFLOPs, 3.81s and 2,114 MiB；RelaCtrl adds 45.15M, 46.71 GFLOPs, 0.24s and 395 MiB under that contract。Flux.1-dev uses a 12B base, 512 resolution and 30 DDIM steps。A100 memory size, optimizer/LR/batch for training, inference concurrency, energy/cost and TTFT/tail SLO are Not Disclosed。
- **What the Evidence Actually Proves:** in the authors' PixArt setup, single-block deletion produces a non-uniform relevance profile with blocks 5–7 most influential, and relevance-selected top 11 performs comparably to the copied first 13 on the reported Canny metrics。Under the disclosed batch-1 A100 contract, RelaCtrl adds 7.38% base parameters and 8.61% base GFLOPs versus roughly 48–50% for the copied branch；the 15.3% headline is relative to the copied control-branch parameter scale, not the whole base model。The Flux appendix shows the mechanism can be instantiated on a second DiT family under the authors' measurements。
- **What It Does Not Prove:** it does not prove CRS is causal, stable across data/prompt/condition distributions, or transferable to arbitrary DiT layers；one-at-a-time deletion does not identify interactions or the globally optimal subset。The expected-distance theorem does not prove information preservation, semantic mixing quality or equivalence to full attention。The paper does not establish production serving goodput, training-cost amortization, universal image quality superiority or applicability to text diffusion and world-model control。
- **Limitations / Threats to Validity:** discovering the prior first requires training a full 27-block branch and many deletion evaluations；the same benchmark family helps select and validate top-k positions, risking selection overfit。CRS combines rank-normalized FID/HDD and can change with metric or condition；single-block ablation misses redundancy and synergy。Random shuffling adds stochastic implementation/replay risk。Some baselines use different backbones or data, no seed/error bars are provided, training details are sparse, project pages expose no executable artifact, and the paper has no dedicated limitation analysis。
- **Trade-offs / New Failure Modes:** relevance budgeting reduces repeated control work but adds an offline profiling pipeline, task-specific placement metadata and retraining/recalibration after backbone, condition or metric drift。Grouped shuffle attention lowers parameters/compute while risking missed structure, random-seed variance, irregular kernels and quality cliffs if a supposedly low-relevance layer becomes important。Fewer fixed positions improve static execution but cannot adapt to request-specific condition difficulty；online adaptation would add routing cost, dynamic shapes, cache/graph fragmentation and new failure recovery state。
- **Where the Previous Design Still Applies:** uniform copied ControlNet remains simpler when condition families are new, profiling is unaffordable, worst-case fidelity dominates or predictable dense kernels matter；token concatenation remains attractive when parameter storage dominates and extra sequence compute is acceptable；full/global attention remains appropriate when long-range structure cannot tolerate grouped approximation；fixed first-prefix insertion is easier to reproduce and govern for stable low-volume workloads。
- **Evolution Relationship:** `Direct Evolution` for `uniform copied control branch → per-layer relevance diagnosis → sparse insertion positions → relevance-conditioned local capacity`；`Alternative Branch` among copied blocks, token concatenation and relevance-budgeted control；`Layering / Dependency` from representation/condition identity to generation semantics, training and hardware execution。This is not evidence that relevance pruning should replace uniform control in every conditional generator。
- **ROADMAP Node:** canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）；handoffs to `MULTIMODAL-REPRESENTATION`, `TRAIN-PRETRAINING`, `INFER-TENSORRT-LLM` and `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** read Part III guide, Ch23 Representation, Ch24 Generative Paradigms and Ch25 World Models, plus relevant Ch28 Pretraining, Ch49 GPU Execution and Ch66 Evaluation boundaries。Ch24 owns conditional-generation factorization, branch allocation and commit/cost semantics；Ch23 owns condition representation identity, Ch49 owns realized kernels/execution plan, and Ch66 owns comparable quality/control/efficiency evidence。
- **Existing Coverage:** Ch24 already explains Diffusion's iterative state, full-work cost model, fixed versus trajectory-conditioned allocation and why step/FLOP reduction does not equal serving goodput；Ch23 preserves modality/condition identity and Ch66 requires full workload contracts。RelaCtrl adds the missing bounded evolution from uniform control duplication to offline relevance-guided insertion/capacity allocation, but it does not justify a generic layer-pruning rule and Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Integration Deferred`；future Books Gate should consider `Refine — Existing Argument` in Ch24, preserving uniform copied blocks, token concatenation and relevance-budgeted branches with their distinct profiling, kernel and drift costs。
- **Changed Files or Rejection Reason:** added the v2-locked 30-field Source Review, same-week/later-revision boundary, project-page artifact limitation, six-dimensional score, workload and theorem boundaries, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** exact v1→v2 delta and immutable source artifact；code/checkpoints/data manifest and random-shuffle seed semantics；optimizer, batch and full training cost；joint versus one-layer relevance interactions；held-out condition/backbone transfer；relevance drift and recalibration trigger；equal-training baseline reproduction；multi-seed uncertainty；concurrency, graph/kernel behavior, end-to-end decoder/encoder cost and production SLO。

### YOLOv12: From Global Attention as an Offline Luxury to Workload-shaped Real-time Vision

- **Candidate / Week / Score:** YOLOv12: Attention-Centric Real-Time Object Detectors / 2025-W08 / 24/30。
- **Source Family ID:** `yolov12-area-attention-r-elan-realtime-detection`。
- **Source Type:** arXiv v1 technical report + author repository；later NeurIPS 2025 designation and Turbo/current-repository changes are revision lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 04:20:14 UTC；the arXiv record contains only v1。The current repository records the public paper/demo on 2025-02-19, Turbo on 2025-03-09 and a repository/implementation switch on 2025-06-17；only the v1 paper is W08 mechanism evidence。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12524v1；https://arxiv.org/abs/2502.12524；https://github.com/sunsmarterjie/yolov12。
- **Related Primary Sources:** the current author repository exposes paper-v1.0 checkpoints/results and later Turbo, segmentation and classification lineage。Its update log explicitly states that the project switched away from the earlier Ultralytics implementation in June because of efficiency, memory and training-stability issues；current `main` therefore cannot be treated as an immutable February reproduction artifact。
- **Access and Verification Status:** Verified with event-time artifact limitation。The complete v1 HTML, formulas, tables, diagnostics, hyperparameters, explicit limitation and current author repository are accessible；a paper-pinned February commit, exact container/dependency lock, checkpoint/data digests, raw runs and independent reproduction are Not Disclosed。An attempted current-history recovery did not yield an immutable event-time commit, so no later code state is back-projected。
- **Full-read Coverage:** read metadata and complete v1 Abstract, Introduction, Related Work, Efficiency Analysis, Area Attention, R-ELAN, architectural design, experimental setup, all comparison/ablation/speed/diagnostic tables, visualization argument, conclusion, limitation, detailed training appendix and current repository installation/training/export/update/result sections。
- **Original Problem:** CNN-based YOLO detectors offered predictable hierarchical compute and real-time kernels, while global visual Attention provided stronger content-dependent interaction but paid quadratic token-pair work, unfavorable memory traffic and extra layout/partition overhead。The design problem was not “can Attention detect objects” but whether it could fit a fixed-resolution, millisecond-scale detector contract without losing trainability at larger model scales。
- **Why the Previous Design Was Reasonable:** convolution preserves spatial locality, regular memory access, multiscale hierarchy and mature kernels；global Attention was expensive, linear approximations could lose global dependency or become unstable, and windowed variants introduced partition/reverse overhead and reduced receptive fields。For edge, CPU, unsupported GPUs or predictable latency, a CNN-only YOLO remains a rational baseline rather than an obsolete stage。
- **Changed Constraint:** target hardware gained IO-aware exact-Attention kernels, but the application still fixed input at `640×640` and required the full detector to remain near existing YOLO latency。At the same time, inserting Attention into ELAN exposed scale-dependent convergence failures, so algorithmic factorization, operator choice, residual topology and training schedule had to be co-designed rather than optimized independently。
- **Mechanism:** Area Attention reshapes an `H×W` feature map into `l` vertical or horizontal regions, default `l=4`, and performs exact Attention within each region；the paper reduces the pair term from `2 n² h d` to `0.5 n² h d` while retaining quadratic scaling。R-ELAN replaces split-first aggregation with a bottleneck-style single feature map and adds a block-level input/output residual scaled by `0.01` for large models。The architecture keeps YOLO's hierarchy, uses only one final R-ELAN block, inherits early YOLOv11 stages, shifts projections to Conv2d+BN, narrows the MLP ratio, removes explicit position embeddings, adds a `7×7` depthwise/separable position perceiver on `V`, and relies on FlashAttention for IO efficiency。
- **State Ownership:** the checkpoint owns stage topology, region orientation/count, projections, MLP ratio, residual scale and position-perceiver weights；training runtime owns augmentation, optimizer, scale-specific recipe and convergence telemetry；the execution engine owns FlashAttention/TensorRT kernels, precision, layout and hardware support；the evaluation contract owns image preprocessing, COCO split, mAP computation and latency method。Neither a heat map nor the current repository owns causal truth about why the model improves。
- **Control Flow / Data Flow:** `640×640 image → hierarchical convolutional stages → feature map reshape into four areas → per-area Q/K/V Attention + position-perceiver value path → R-ELAN residual/aggregation → multiscale detector head → boxes/classes`；training adds `COCO sample → augmentation → forward/loss → SGD update`。Inference export maps the frozen graph to TensorRT FP16, while current Turbo/checkpoint paths are separate later artifacts。
- **Implementation Details:** the paper trains N/S/M/L/X from scratch for 600 epochs with SGD, three warmup epochs, linear `0.01→0.0001` learning-rate decay, momentum `0.937`, weight decay `5e-4`, global batch `32×8=256`, box/class/DFL gains `7.5/0.5/1.5`, Mosaic `1.0`, scale-dependent MixUp/copy-paste and last-ten-epoch Mosaic closure。Large L/X variants use residual scale `0.01`; N/S/M use MLP ratio `2`, while L/X use `1.2`。
- **Evaluation Contract:** COCO 2017 validation, five detector scales and `640×640` inputs form the primary quality contract。Main latency is reported on NVIDIA T4 with TensorRT FP16 as average milliseconds per image；separate speed studies use RTX 3080, A5000 and A6000 in FP32/FP16, and Area-Attention ablations also use Intel i7-10700K CPU。The paper does not define production queueing, pre/post-processing inclusion or tail SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** the main table compares YOLOv6/8/9/10/11 and RT-DETR variants；same-codebase speed tests cover YOLOv9/10/11/12 on three GPUs。Ablations isolate R-ELAN aggregation/residual/scale, Area Attention with and without FlashAttention, Conv/Linear × BN/LN, hierarchy, 300/500/600/800 epochs, position-perceiver kernels, position encoding, MLP ratio and FlashAttention。Not every published baseline was retrained under one data/recipe contract；no seed/error bars, shifted-region boundary ablation, joint component factorial or resolution sweep is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** training uses 8×NVIDIA A6000, batch 256 and 600 epochs；GPU memory size, precision, wall time, FLOPs/energy/cost and seed count are Not Disclosed。Main inference uses T4 + TensorRT FP16 at 640 pixels；N/S report 40.6/48.0 mAP, 6.5/21.4 GFLOPs, 2.6/9.3M parameters and 1.64/2.61 ms per image under that author contract。Inference batch, concurrency, warmup, TensorRT build/version details beyond the repository's later table, pre/post-processing and percentile SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' COCO-640 contract, a hierarchical detector combining regional exact Attention, scaled residual aggregation and hardware-aware operators can match the latency class of contemporary YOLO baselines while improving the reported mAP frontier。The no-FlashAttention Area ablation shows lower latency across N/S/X and CPU/GPU；R-ELAN tables show that residual scaling is required for reported L/X convergence；diagnostics show the chosen hierarchy, position perceiver, MLP ratio and FlashAttention are locally useful within this joint recipe。
- **What It Does Not Prove:** it does not prove Attention universally replaces convolution, Area Attention is linear, explicit position encoding is generally harmful, or a `0.01` residual scale transfers across architectures。It does not establish causality from qualitative heat maps, equal-compute superiority over every baseline, robustness/OOD/calibration, edge deployment safety, high-resolution behavior, production goodput or reproducibility of v1 from current `main`。Later Turbo numbers and task heads are not February results。
- **Limitations / Threats to Validity:** evidence is one dataset/task and fixed input size；Area Attention remains quadratic and its cost rises with resolution。Fixed equal regions may create boundary effects and no shifted/cross-region sensitivity is given。Training uses a long, augmentation-heavy 600-epoch recipe without cost or multi-seed uncertainty。Main latency omits batch/concurrency/tail and likely excludes some pipeline work；the paper's dedicated limitation section only names FlashAttention hardware support。A stated FP32 L-scale number is internally inconsistent with the surrounding tables, and the current repository's later implementation switch weakens event-time artifact reproducibility。
- **Trade-offs / New Failure Modes:** regional Attention trades global interaction for lower pair work and simpler kernels, but introduces region orientation/count, boundary isolation and resolution-sensitive cost。FlashAttention reduces IO but narrows hardware/software support；Conv+BN improves the tested execution path while adding batch-statistics and deployment-mode concerns。Scaled residuals stabilize large variants but create scale-sensitive initialization/checkpoint semantics；longer training raises cost。A fused fast model can still fail through preprocessing drift, unsupported kernels, TensorRT rebuild changes or unnoticed quality regressions at object-size/subgroup slices。
- **Where the Previous Design Still Applies:** CNN-only YOLO remains preferable on unsupported/CPU-heavy devices, small datasets, mature deployment stacks or when predictable regular kernels dominate；global Attention remains appropriate when cross-region interaction is essential and resolution/latency allow it；window/shifted Attention remains useful when explicit local connectivity is required；plain Vision Transformer hierarchies may still fit non-YOLO tasks；standard residual/LN/MLP ratios remain valid outside this detector recipe。
- **Evolution Relationship:** `Direct Evolution` for `CNN-only hierarchical detector → attention-centric detector constrained by quadratic/IO cost → regional exact Attention + IO-aware kernel → residual/aggregation stabilization at larger scales`；`Alternative Branch` among convolution, global/window/linear/area Attention；`Layering / Dependency` from position, residual and representation semantics to training and GPU execution。The next pressure is adaptive cross-region communication, reproducible event-time artifacts and end-to-end latency/robustness evidence across resolutions and devices。
- **ROADMAP Node:** canonical owner `MODEL-SELF-ATTENTION`（Current Ch14；Legacy Ch14）；handoffs to `MODEL-POSITION-ENCODING`, `MODEL-FFN`, `MODEL-TRANSFORMER-LAYER`, `MULTIMODAL-REPRESENTATION`, `TRAIN-PRETRAINING`, `INFER-TENSORRT-LLM` and `PLATFORM-EVALUATION-SYSTEM`。
- **Target and Adjacent Chapters Read:** read Part II guide and full Ch13 Position Encoding, Ch14 Self Attention, Ch15 Multi-Head Attention and Ch17 Transformer Layer；inspected the relevant Ch23 Representation, Ch28 Pretraining, Ch49 GPU Execution and Ch66 Evaluation boundaries。Ch14 owns Attention factorization/semantic connectivity；Ch13 owns positional assumptions, Ch17 owns residual topology, Ch23 owns visual representation identity, Ch28 owns the training recipe, Ch49 owns realized kernels and Ch66 owns comparable workload evidence。
- **Existing Coverage:** Ch14 already distinguishes quadratic pair work from FlashAttention IO execution and preserves model/runtime ownership；Ch13 separates explicit position mechanisms from convolutional spatial bias；Ch17 covers residual scaling as architecture semantics；Ch49 requires kernel/precision/hardware/workload identity。YOLOv12 adds a bounded, vision-specific evolution from global to region-shaped exact Attention plus scale-dependent residual stabilization, but its COCO/T4 results cannot become a general Attention design rule and Historical Books Gate is closed。
- **Integration Decision:** `Books Pending — Integration Deferred`；future Books Gate should consider `Refine — Existing Argument` in Ch14, with short handoffs to Ch17 and Ch49, preserving CNN, global/window/linear/area Attention as conditional branches rather than a replacement timeline。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, final score, event-time/current-repository boundary, mechanism/state/control path, complete workload contract, limitations, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February commit/checkpoint/container and exact later-repository migration mapping；TensorRT build, batch/warmup and pre/post-processing inclusion；training precision/time/energy/seeds；region orientation/shift/cross-boundary and resolution sensitivity；equal-recipe baselines；robustness/OOD/calibration and object-size/subgroup uncertainty；edge CPU/mobile power and tail SLO；independent reproduction and whether regional Attention remains favorable under modern kernels without the full joint recipe。

### CLIPPER: From Direct Long-document Prompting to Versioned Compressed-evidence Compilation

- **Candidate / Week / Score:** CLIPPER: Compression enables long-context synthetic data generation / 2025-W08 / 26/30。
- **Source Family ID:** `clipper-compressed-evidence-long-context-data`。
- **Source Type:** arXiv v1 research paper + author repository；arXiv v2 and COLM 2025 acceptance are later lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 18:58:03 UTC；v2 submitted 2025-08-05 and is outside W08。The current repository says datasets and models became available on 2025-02-19, but no immutable event-time commit or digest was recovered；W08 therefore uses the paper-v1 timestamp as the auditable first-public mechanism event and records the repository statement only as an unresolved artifact-date claim。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14854v1；https://arxiv.org/abs/2502.14854；https://github.com/chtmp223/CLIPPER。
- **Related Primary Sources:** the current author repository exposes generation scripts, prompts, data directories, evaluation code and a Hugging Face collection, but its six-commit current history is not a paper-pinned v1 environment。Later v2/publication material is revision lineage and is not back-projected into February claims。
- **Access and Verification Status:** Verified with artifact and internal-consistency limitations。The complete v1 HTML, method, evaluation, appendices, prompts, training recipes and current repository are readable；the exact February commit, dataset/model digests, raw runs, dependency/container lock and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read v1 metadata, Abstract, Introduction, Related Work, three-stage compression/claim/validation pipeline, human claim audit, chain-of-thought judge validation, SFT design, all evaluation tasks and tables, transfer results, cost accounting, contamination checks, limitations, false-claim taxonomy, HELMET metric correction, prompts, codebase and hyperparameter appendices, plus the current repository structure。
- **Original Problem:** generating supervised claims directly from an approximately 90K-token book asks a model to retain global narrative state, follow an output specification and avoid prompt artifacts in one pass。Using only excerpts makes generation easier but cannot produce claims whose truth depends on relations across chapters；using the whole book directly produced many invalid, misattributed, explicitly referenced or duplicate claims in the authors' audit。
- **Why the Previous Design Was Reasonable:** direct prompting preserves the original evidence and minimizes pipeline stages, while excerpt-level generation offers cheap localization and simple provenance。When documents are short, models are strong enough, claim volume is small or exact source wording matters, either approach avoids lossy intermediate representations and extra generator/validator dependencies。
- **Changed Constraint:** long-context training needs many book-grounded examples whose claims require global evidence, but context length alone does not guarantee instruction adherence or synthetic-label quality。The generation process must reduce reasoning load while retaining enough cross-chapter structure, track how derived evidence was produced and filter correlated generator errors before training smaller models。
- **Mechanism:** clean and segment each public-domain book；use GPT-4o to create a short book summary and Claude 3.5 Sonnet to create chapter outlines totaling roughly one tenth of the original token count；generate chapter- and book-level true/false claim pairs with reasoning from those compressed representations；deduplicate with Claude；validate claims against outlines with GPT-4o；then construct SFT rows whose input is the full original book and whose target is chain-of-thought plus verdict。Compression is therefore a derived evidence representation used to compile labels, not a lossless replacement for the source document。
- **State Ownership:** the corpus manifest owns book identity, license and split；cleaned chapters own source boundaries；summary/outline artifacts own compressor model, prompt and version；each claim owns scope, polarity and supporting chapter provenance；deduplication, model validation and human audit own separate verdicts；the SFT dataset owns book-disjoint train/validation/test lineage；the checkpoint and evaluation harness own learned behavior and measured results。No single judge response becomes ground truth without this lineage。
- **Control Flow / Data Flow:** `Project Gutenberg book → cleaning/chapter segmentation → book summary + chapter outlines → chapter/book-level true/false claims + reasoning → deduplication → outline-grounded model validation → sampled human audit → book-disjoint dataset split → full-book SFT input + reasoning/verdict target → long- and short-context evaluation`。
- **Implementation Details:** the corpus contains 479 English fiction books averaging about 90K tokens and 23 chapters, excluding books above 128K tokens。The pipeline produces about 19K claims；the reported training split has 16K claims, with roughly equal chapter- and book-level examples, plus 2K validation and 1K test claims from disjoint books。The compressed summary averages about 618 tokens and chapter outlines about 8,745 tokens versus roughly 90,437 source tokens。The current repository exposes scripts and prompts, but does not pin the exact February model/API snapshots or immutable generated artifacts。
- **Evaluation Contract:** CLIPPER-test uses 1,000 synthetic claim pairs from 53 held-out books；NoCha uses 1,001 human-authored claims over recent fiction up to 336K tokens。NarrativeQA, InfinityBench QA, MuSR and selected short-context LM Harness tasks test transfer and interference。Pair accuracy counts a pair correct only when both its true and false claims are classified correctly；the paper later removes HELMET's default ten-token output cap and replaces ROUGE-only scoring with a GPT-4o judge for narrative QA, changing the evaluator contract and adding judge dependence。
- **Baselines / Ablations / Sensitivity / Overhead:** experiments compare ProLong-512K-8B-Base, Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct before/after one-epoch SFT；training-data ablations compare book-level, chapter-level and mixed claims, and human analysis compares naive whole-book generation with CLIPPER。Learning rate is tuned only on a 2K ProLong subset；there are no multi-seed confidence intervals, equal-compute alternative compressors, independent judge family, complete pipeline-component factorial or reproduction on private/domain-specific documents。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SFT uses one epoch, learning rate `1e-6`, global batch 16 and 8 NVIDIA A100 GPUs；ProLong uses FlashAttention 2 with DeepSpeed Ulysses, while Qwen uses 360-LLaMA-Factory with zigzag ring attention。A100 memory size, training precision, optimizer details beyond the appendix, sequence packing, API concurrency, energy, tail latency and production SLO are Not Disclosed。The paper says an epoch takes about five hours in one section but later states roughly 50 hours for a “full test set” training run；the unresolved wording conflict is preserved rather than normalized。
- **What the Evidence Actually Proves:** under the authors' fiction-book pipeline, compression plus validation greatly improves sampled claim validity over naive full-book prompting and produces SFT data that raises pair accuracy on the synthetic held-out test and, more modestly, NoCha for the three tested 7B/8B models。The human audit reports 83.3% error-free claims for CLIPPER versus 26.9% for the naive baseline；59.4% of initial claims are removed as duplicates and 2.4% as invalid, showing that filtering is a material part of the mechanism。Data-branch ablations also show smaller models can benefit more from chapter-level than book-level claims, so global supervision is not a monotonic default。
- **What It Does Not Prove:** it does not prove compression preserves every fact, synthetic claims match human difficulty, the learned model performs faithful retrieval rather than exploiting task regularities, or the pipeline transfers to scientific, legal, multilingual or continuously revised corpora。The no-book prompt check does not rule out pretraining memorization。Author results do not establish a universal long-context improvement, production data economics or that one vendor's generator/validator/judge can provide independent correctness evidence。
- **Limitations / Threats to Validity:** training claims are synthetic and visibly easier than NoCha；compressor, generator, validator and evaluation judge can share model-family biases。The reasoning-groundedness judge is calibrated on only 66 human-audited samples, and only one of 72 manually checked validation pairs disagrees, leaving wide uncertainty at scale。Short-task transfer is mixed: InfinityBench QA can decline, and ProLong's reported IFEval score drops sharply after CLIPPER SFT, indicating capability interference rather than uniformly harmless specialization。Artifact pinning, seeds/error bars, full resource accounting and independent reproduction are absent；the training-time statement is internally inconsistent。
- **Trade-offs / New Failure Modes:** compressed evidence lowers context and generation cost while adding a lossy, versioned intermediate state that can omit relations before claims are created。Multi-model filtering improves precision but increases API cost, latency, correlated-bias risk and lineage complexity。Training on full books reconnects labels to raw context but still pays long-sequence training cost and can overwrite instruction-following or short-task behavior。A production pipeline must detect stale summaries after source revision, preserve rejected-claim audit trails, quarantine judge drift and support rollback of dataset and checkpoint versions。
- **Where the Previous Design Still Applies:** direct whole-document generation remains preferable for shorter inputs, strong models, low-volume expert review or tasks requiring exact quotations；excerpt/chapter generation remains cheaper when truth is local；retrieval-grounded human annotation remains stronger when consequences are high；human-authored evaluation remains necessary when synthetic difficulty or shared-model bias would hide failures。Compressed-evidence compilation is an additional branch, not a replacement for source-preserving supervision。
- **Evolution Relationship:** `Direct Evolution` for `whole-document prompt → chapter-local generation → compressed global evidence → multi-stage generate/deduplicate/validate → versioned long-context SFT artifact`；`Layering / Dependency` from corpus/provenance to SFT and evaluation；`Alternative Branch` among direct, excerpt-level, compressed-synthetic and human-authored supervision。The next pressure is independent verification, mutable-source invalidation and specialization-safe training rather than simply increasing context length。
- **ROADMAP Node:** canonical owner `TRAIN-DATA`（Current Ch27；Legacy Ch23）；handoffs to `TRAIN-SFT`, `MODEL-LONG-CONTEXT`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-COST` and `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** read full Ch27 Data and adjacent Ch28 Pretraining and Ch29 SFT, plus the relevant long-context contract in Ch22 and evaluation evidence in Ch66。Ch27 owns data compilation, derived evidence and lineage；Ch29 owns optimization/interference, Ch22 owns model context semantics, Ch66 owns comparable evaluation and Ch70/72 own cost/provenance governance。
- **Existing Coverage:** Ch27 already develops `generate → score/filter → versioned dataset` and treats synthetic data as specification compilation, while Ch66 requires evaluator identity and negative evidence。CLIPPER contributes a missing intermediate branch—lossy compressed evidence with explicit source/claim lineage—and unusually clear evidence that filtering cost and downstream capability regression belong to the data contract。It refines an existing argument rather than creating a new chapter, and Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DATA`, with short handoffs to SFT and Evaluation；future integration must preserve direct, local, compressed and human-authored branches and must include specialization regression, not only the positive long-context result。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, revision/artifact boundary, lossy-evidence mechanism, state/control lineage, full evaluation and cost constraints, negative transfer evidence, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February repository/data/model/prompt digests；whether the repository's 2025-02-19 availability statement can be tied to a signed event-time artifact；the paper's five-hour versus roughly 50-hour training wording；source-revision invalidation and claim-level provenance；independent compressor/validator/judge families；human-authored training comparison；multi-seed capability-interference frontier；non-fiction, multilingual and mutable-corpus transfer；precision, token/FLOP/energy and production cost/SLO accounting。

### Explorer: From Static Task Proposals to Environment-grounded Trajectory Compilation

- **Candidate / Week / Score:** Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents / 2025-W08 / 27/30。
- **Source Family ID:** `explorer-environment-grounded-web-trajectory-synthesis`。
- **Source Type:** arXiv research paper + official author repository；ACL 2025 Findings paper and current repository are later publication/artifact lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 02:13:48 UTC；v2 submitted 2025-02-19 01:38:06 UTC and is the latest W08 revision；v3/v4 on 2025-05-28/30 and ACL publication are later lineage。W08 mechanism and results are locked to v2；later code/publication state is not back-projected。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11357v2；https://arxiv.org/abs/2502.11357；https://github.com/OSU-NLP-Group/Explorer。
- **Related Primary Sources:** https://arxiv.org/html/2502.11357v1 establishes the first-public event。The current repository exposes training, evaluation and trajectory-generation code but has no release/tag or paper-pinned February digest；its ACL-era 31-commit state is supporting lineage, not an immutable v2 reproduction artifact。
- **Access and Verification Status:** Verified with event-time artifact limitation。The complete v2 paper, appendices, prompts, cost table, failure analysis and current code structure are accessible；exact v1→v2 semantic diff, February commit/data/checkpoint/container, raw evaluation runs and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read v1/v2 metadata and revision history, Abstract, Introduction, Related Work, website selection, proposer/refiner/summarizer/verifier pipeline, dataset statistics, all three benchmark contracts, result and scaling tables, modality/backbone ablations, generation and evaluation failure modes, Conclusion, Limitations, Ethics, training/evaluation/cost/reasoning/prompt appendices and current repository commands/layout。
- **Original Problem:** human web-agent trajectories are expensive and static LLM-written tasks are often detached from what a live site actually exposes。Tutorial-guided data covers common workflows but underrepresents domains and information-seeking；offline golden paths also penalize legitimate alternative actions and hide site drift。The data problem is therefore to discover feasible intents, execute them and verify outcomes at scale under mutable environments。
- **Why the Previous Design Was Reasonable:** human annotation provides clearer intent and expert oversight；homepage/task-first synthesis is cheap and predictable；tutorial replay supplies coherent procedures；sandboxed sites improve determinism。When tasks are high-risk, sites require credentials, reproducibility dominates or functional verifiers are unavailable, these narrower sources remain preferable to autonomous live-Web collection。
- **Changed Constraint:** a generalist multimodal Web Agent needs broad website/skill coverage and multi-step screenshot/A11y/action trajectories, but manually specifying every task does not scale。Task identity must adapt to product availability and page state while collection cost, access policy, safety boundaries and outcome validity remain explicit data-plane concerns。
- **Mechanism:** seed live sites from Similarweb and Tranco；a GPT-4o proposer reads the home-page screenshot and accessibility tree, proposes an abstract task and executes the first action；a refiner repeatedly updates both task description and next grounded action from the full history；a summarizer converts the completed action/screenshot history into a high-level intent；a verifier checks that intent against the trajectory, screenshots and final-page markdown。A Qwen2-VL-7B model later generates post-hoc action reasoning, and accepted trajectories become SFT data。
- **State Ownership:** the seed manifest owns URL/source and policy filters；Playwright/browser owns live page state and side effects；proposer/refiner own provisional task/action versions；trajectory store owns screenshot, HTML, A11y tree, grounded/natural-language action and history；summarizer owns derived final intent；verifier owns an admission verdict, not ground truth；dataset manifest owns accepted/rejected lineage and split；checkpoint/evaluation harness own learned policy and measured outcomes。
- **Control Flow / Data Flow:** `versioned URL seed → live browser observation → abstract task + first action → execute → updated observation/history → iterative task refinement + action → stop/safety boundary → trajectory summarization → model verification → accepted/rejected trajectory → optional post-hoc reasoning → SFT subset → offline/live evaluation`。
- **Implementation Details:** the authors run 60 parallel processes for 50 hours and generate 175K raw trajectories, retaining 94K successful trajectories across 49K URLs, about 720K screenshots, 33.3M elements and 830M tokens；mean trajectory length is 7.7 steps。From 40K selected trajectories they remove examples with more than two scroll actions, leaving about 30K for training Phi-3.5V and Qwen2-VL-7B。The action schema includes click/type/select/goto/search/scroll, while prompts stop at CAPTCHA, login or payment boundaries。
- **Evaluation Contract:** Mind2Web-Live starts from 104 tasks but the main table uses 83 consistently accessible tasks across 37 sites, viewport `1280×720`, and reports the maximum of three runs；the appendix reports all 104 tasks。Multimodal-Mind2Web is offline, uses top-50 DeBERTa candidates and always includes the ground-truth element, with a single train/eval run。MiniWob++ averages four runs over 46 simulated tasks。A separate 100-task in-domain live set uses an LLM-as-judge trajectory verifier。
- **Baselines / Ablations / Sensitivity / Overhead:** compares base and fine-tuned Phi-3.5V/Qwen2-VL-7B, API/general/agent baselines, synthetic-only versus Mind2Web versus mixed training, 25/50/100% data scale, text-only Phi-3-mini and LLaVA-Mistral backbones。Most external numbers are inherited rather than equal-environment reruns；there is no proposer/refiner/summarizer/verifier component ablation, verifier calibration against a substantial human/executable gold set, seed uncertainty for offline evaluation, or equal-cost human/tutorial/sandbox comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** all training uses NVIDIA H100 GPUs；repository commands use four processes, BF16 and FlashAttention。Reported runs use batch 64, two or ten epochs, learning rate `1e-5` or `4e-5`, and 1–17 training hours depending on data/model。GPU count for paper runs, H100 memory, optimizer, sequence packing, checkpoint size, evaluation concurrency, browser/network latency, energy and production tail SLO are Not Disclosed。Trajectory generation reports 60 processes and 50 hours, not a serving contract。
- **What the Evidence Actually Proves:** under the authors' live-Web collection and filtering contract, bottom-up exploration can produce a much larger multimodal trajectory corpus at the reported API cost, and SFT on a 30K subset improves both tested 4B/7B bases on the disclosed online/offline tasks。Phi-3.5V full-task success rises from 2.4% to 18.1% and Qwen2-VL-7B from 14.5% to 19.3% on the selected 83-task live set；data-scaling curves averaged over three runs improve as the retained subset grows。A 53.1% verifier acceptance rate also proves rejection is a major stage, not negligible cleanup。
- **What It Does Not Prove:** it does not prove the verifier's accepted trajectories are correct, broader URL count equals semantic/task diversity, synthetic trajectories outperform human data under equal cost, or results generalize to authenticated, transactional, adversarial or rapidly changing sites。The selected accessible-task maximum-over-runs protocol is not a stable production success rate；offline ground-truth-element inclusion weakens claims about end-to-end candidate discovery。Post-hoc reasoning does not prove the model used that rationale during action generation。
- **Limitations / Threats to Validity:** proposer, refiner, summarizer and verifier share GPT-4o and can share blind spots；final-page evidence can miss earlier harmful side effects or falsely accept partial completion。Scroll-count filtering changes the training distribution and may remove legitimate long-page tasks。Live-site access, CAPTCHA and unresponsive pages confound policy with environment；the main benchmark excludes 21 inaccessible tasks and chooses the best of three runs。No large human audit of accepted/rejected data, component causal ablation, immutable event-time artifact, website snapshot, multi-seed training or independent replication is reported。
- **Trade-offs / New Failure Modes:** environment-grounded exploration improves feasibility and coverage but sacrifices determinism, reproducibility and simple consent/rate-limit accounting。Backward intent construction lets the task fit actions, but can relabel aimless exploration as a coherent task or teach post-hoc rationalization。Shared-model verification lowers cost while amplifying correlated false accepts；aggressive filtering improves precision while narrowing rare skills。Parallel live crawling adds stale element IDs, page mutation, partial trajectories, duplicate side effects, policy violations and non-idempotent retry risk。
- **Where the Previous Design Still Applies:** human demonstrations remain strongest for high-impact workflows and ambiguous intent；tutorial-guided generation remains coherent for documented procedures；task-first synthesis is simpler when stable sandboxes and functional specifications exist；offline replay is preferable for reproducible regression；direct supervised grounding remains useful for local actions without long-horizon intent。Explorer is a data-acquisition branch, not a universal Agent runtime architecture。
- **Evolution Relationship:** `Direct Evolution` for `human/tutorial/task-first demonstrations → live exploration with provisional intent → iterative action-conditioned task refinement → summarize/verify → versioned trajectory data`；`Layering / Dependency` from environment/action identity to SFT, Workflow and Evaluation；`Alternative Branch` among human, tutorial, sandbox/specification-first and live exploration。The next pressure is independent outcome verification, immutable environment replay and policy-safe collection rather than URL count alone。
- **ROADMAP Node:** canonical owner `TRAIN-DATA`（Current Ch27；Legacy Ch23）；handoffs to `TRAIN-SFT`, `AGENT-WORKFLOW`, `AGENT-PLATFORM`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-COST` and `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** read the trajectory/synthetic-data spine of Ch27 and adjacent Ch29 SFT, plus the relevant offline/live workflow boundary in Ch81, feedback/data admission in Ch84 and trajectory-judge contract in Ch66；checked Ch70 cost and Ch72 action/safety boundaries。Ch27 owns acquisition and row lineage；Workflow owns deployed transitions, and Evaluation owns completion evidence。
- **Existing Coverage:** Ch27 already requires Web-Agent rows to preserve observation modality, action abstraction, browser revision, verifier and side-effect policy, and distinguishes open-semantic judge filtering from executable specification compilation。Explorer adds a concrete predecessor branch where task identity is refined from live action history, plus the critical evidence that access selection, best-of-run reporting and verifier rejection materially shape the dataset。The mechanism refines existing coverage; Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DATA`, with short handoffs to Workflow and Evaluation；future integration must preserve human/tutorial/task-first/sandbox/live-exploration branches and cannot promote the author verifier or URL scale to correctness/diversity truth。
- **Changed Files or Rejection Reason:** added the v2-locked 30-field Source Review, v1/v2/later-lineage boundary, full pipeline/state/evaluation contract, selection and shared-verifier limitations, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** exact v1→v2 semantic diff and immutable February commit/data/checkpoint/container；accepted/rejected human audit and verifier false-success calibration；website snapshot/robots/terms/rate-limit provenance；duplicate and non-idempotent side-effect handling；task-intent relabeling bias；scroll-filter skill loss；matched-cost human/tutorial/sandbox baselines；all-104-task and fixed-seed reporting；hardware/energy/browser tail cost；current repository compatibility with paper-v2 artifacts。

### Template-Anchored Safety: From Prompt-bound Refusal Shortcut to Generation-time Defense Sensor

- **Candidate / Week / Score:** Why Safeguarded Ships Run Aground? Aligned Large Language Models' Safety Mechanisms Tend to Be Anchored in The Template Region / 2025-W08 / 27/30。
- **Source Family ID:** `template-anchored-safety-mechanism`。
- **Source Type:** arXiv research paper；ACL 2025 publication is later lineage。No official author code, checkpoint or immutable experiment artifact was identified。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 18:42:45 UTC；v2 submitted 2025-06-03 and carries the ACL 2025 Main Conference lineage。W08 evidence is locked to v1；the later publication revision is not back-projected。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13946v1；https://arxiv.org/abs/2502.13946。
- **Related Primary Sources:** https://arxiv.org/html/2502.13946v2 is later revision lineage only。No author repository, release, model card or run artifact was found from the paper metadata and author links；community reproductions are not used as primary evidence。
- **Access and Verification Status:** Verified with artifact limitation。The complete v1 HTML, equations, tables, attack/defense appendices, prompts and explicit limitations are accessible；source code, model/config digests, raw runs, seeds and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read metadata and revision history, Abstract, Introduction, Related Work, problem definition, attention-shift analysis, linear probes, activation patching, TempPatch, generation-time detaching defense, all result/transfer tables, attack and hyperparameter appendices, template definitions, Conclusion and Limitations。The v1 text contains an internal dataset-label typo around `D_eval`; the review preserves the ambiguity rather than silently correcting it。
- **Original Problem:** instruction-tuned models often refuse harmful requests, yet jailbreaks can bypass the behavior without changing the underlying knowledge。The paper asks whether safety alignment is distributed across instruction semantics or has learned a shortcut concentrated in the fixed chat-template suffix immediately before generation。
- **Why the Previous Design Was Reasonable:** template tokens give every request a stable role/turn boundary and let supervised or preference training attach refusal behavior to a consistent generation interface。When model family, tokenizer, prompt serialization and policy remain fixed, such a low-cost anchor can be an effective safety prior；output guards and deterministic tool authorization can separately catch failures。
- **Changed Constraint:** adversarial prompts, template variants and local fine-tuning make a position-specific shortcut brittle。A security claim must therefore bind refusal behavior to model, tokenizer, template, policy and generation path, and distinguish prompt-time detection from response-time persistence instead of treating alignment as a checkpoint-only property。
- **Mechanism:** the authors first compare attention allocation for length-matched harmful/harmless instructions, then train difference-in-means linear probes on last hidden states。They patch harmless value states into harmful inputs to estimate a normalized indirect effect and identify a small set of template-position heads；TempPatch reuses harmless cached value states at those positions during harmful generation。For defense, a probe transferred from the template region monitors each generated token and adds the negative harmfulness direction to a selected residual layer when activation crosses a threshold。
- **State Ownership:** checkpoint owns learned attention/residual representations；tokenizer and chat-template artifact own serialization and template-position identity；prompt policy owns harmful/harmless taxonomy；attack harness owns source prompt, patched head/position set and cache mutation；generation runtime owns KV/value-state lifecycle and residual intervention；probe/threshold artifact owns a policy-bound sensor score；evaluation owns ASR/judge contract；deterministic gateway/tool authorization retains final enforcement authority。
- **Control Flow / Data Flow:** `request + policy → tokenizer/template serialization → prefill attention/value states → optional white-box patch at selected template heads → autoregressive generation → per-token hidden-state probe → thresholded residual steering → output/judge → independent enforcement and trace`。The analysis pipeline separately runs length-matched datasets, cross-validated probes, intervention sweeps and attack-specific evaluation。
- **Implementation Details:** six instruction-tuned model variants are analyzed: Gemma-2 2B/9B, Llama-2-7B-Chat, Llama-3.2-3B-Instruct, Llama-3-8B-Instruct and Mistral-7B-Instruct。The linear probe uses a harmful-versus-harmless mean-difference direction and five-fold cross-validation。TempPatch sweeps patch proportions from 10% to 90% on the analysis set；generation is greedy with maximum 512 tokens。The defense uses Llama-3-8B layer 13/position 4/alpha 1 and Gemma-2-9B layer 23/position 4/alpha 0.7, with thresholds derived from harmful/harmless response activations。
- **Evaluation Contract:** analysis uses harmful JailbreakBench requests and length-matched harmless Alpaca-Cleaned requests；evaluation references HarmBench, although one v1 sentence repeats the analysis-dataset symbol。Attacks are AIM, AmpleGCG and PAIR；PAIR uses Mixtral-8x22B as attacker, `gpt-4o-mini` as judge, 20 streams and depth 3, while AmpleGCG uses the recommended checkpoint, diverse beam 200 and maximum 20 suffix tokens。ASR is the main outcome；probe accuracy and normalized indirect effect are diagnostic surrogates。
- **Baselines / Ablations / Sensitivity / Overhead:** evidence progresses from attention correlation to probe separability, instruction-versus-template activation patching, head/proportion sweeps, cross-position response transfer and two-model defense tests。The reported mean probe accuracy is 98.7±0.7% across models。Defense ASR changes include Gemma-2-9B AIM 89.3→0, AmpleGCG 62.3→5.7 and PAIR 94.3→11.9；Llama-3-8B AIM 0→0, AmpleGCG 29.6→3.1 and PAIR 56.6→16.2。No benign-utility, over-refusal, adaptive-attack, seed, independent-detector or runtime-overhead study is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model identities, greedy decoding and 512-token maximum are disclosed。Hardware, accelerator count/memory, precision/quantization, input-length distribution, training/inference batch, concurrent requests, KV/cache overhead, latency, throughput, energy/cost and production SLO are Not Disclosed；the ASR numbers are not serving benchmarks。
- **What the Evidence Actually Proves:** under the authors' white-box interventions and benchmark contracts, harmful/harmless state is linearly separable near the template region, patching a small selected head set changes a compliance-probe surrogate more strongly at template than instruction positions, and a template-derived direction transfers into early response states。The proof-of-concept steering lowers measured ASR for three attacks on two tested models under selected probe/layer/threshold settings。
- **What It Does Not Prove:** attention weight is not causal explanation, linear separability is not a semantic or safety certificate, and hidden-state patching may create out-of-distribution states。The study does not prove all aligned models use this shortcut, the template is the only safety locus, TempPatch represents black-box attacks, or residual steering preserves benign helpfulness and production safety。It also does not establish robustness to adaptive attackers, new templates/tokenizers, quantization, fine-tuning, multilingual/long-turn/tool-use traffic or independent judges。
- **Limitations / Threats to Validity:** v1 explicitly says multiple models do not establish universality and some training approaches may mitigate the shortcut；the defense does not remove the learned shortcut and is only a proof of concept。Additional threats are analysis-selected heads/proportions/layers/thresholds, two-model defense scope, shared benchmark/judge assumptions, missing false-positive/negative calibration, no benign slice, no artifact or seeds, and the internal `D_eval` labeling inconsistency。
- **Trade-offs / New Failure Modes:** stable template anchoring makes alignment easy to learn and cheap to deploy but couples safety to serialization identity。Runtime monitoring can catch response-time drift but adds probe/version/threshold state, hidden-state access, latency and intervention risk；false negatives miss harmful continuations, while false positives can distort harmless output or cause over-refusal。A known steering direction invites adaptive evasion, and template/runtime changes can silently invalidate head positions and thresholds。
- **Where the Previous Design Still Applies:** training-level alignment remains the primary behavior prior；fixed templates remain useful when versioned and tested；prompt/output guards provide cheap layered sensors；deterministic authorization and sandboxing remain mandatory for tool effects；human escalation remains preferable for high-impact ambiguity。Generation-time steering is an experimental additional layer, not a replacement for these branches。
- **Evolution Relationship:** `Direct Evolution` for `training-level alignment → template-local shortcut diagnosis → white-box causal proxy → generation-time probe and steering`；`Layering / Dependency` toward Evaluation and runtime traceability；`Alternative Branch` among retraining, template diversification, external guardrails, residual steering and deterministic enforcement。The next pressure is template-invariant safety evidence and adaptive, utility-aware evaluation rather than stronger steering alone。
- **ROADMAP Node:** canonical owner `PLATFORM-SECURITY`（Current Ch72；Legacy Ch68）；handoffs to `MODEL-SELF-ATTENTION`, `MODEL-TRANSFORMER-LAYER`, `TRAIN-RLHF` and `PLATFORM-EVALUATION-SYSTEM`。Security owns the trust/policy boundary；model chapters own representation mechanics, Training owns how the shortcut is learned, and Evaluation owns attack/utility operating evidence。
- **Target and Adjacent Chapters Read:** read Ch71 Multi Tenant, Ch72 Security and Ch73 Production Best Practice, plus Ch66 Evaluation, Ch14 Self Attention, Ch17 Transformer Layer and Ch31 RLHF boundaries。Ch72 already treats refusal/classifiers as sensors and keeps tool authority outside model output；Ch66 requires run identity, slices and uncertainty；model chapters prevent attention/probe observations from being promoted to causal semantics。
- **Existing Coverage:** Ch72 already requires model, data, prompt, policy, tool and runtime identities, separates learned sensors from authorization and preserves output-time enforcement。This paper adds a concrete serialization-coupled failure path and a response-time sensor/steering branch, but its missing benign utility and adaptive robustness mean it refines the existing layered-defense argument rather than creating a new security primitive。Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `PLATFORM-SECURITY`, with short handoffs to Evaluation and model representation chapters。Future integration must preserve alignment, template versioning, external guards, runtime monitor and deterministic enforcement as conditional layers, and label steering `Experimental`。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, revision/artifact boundary, template/KV/residual state ownership, attack and defense evaluation contract, proof and non-proof boundary, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** official code/checkpoint/raw runs and immutable environment；v1 `D_eval` identity；seed and judge sensitivity；benign helpfulness/over-refusal and false-positive calibration；adaptive attacks against disclosed probe/steering；template/tokenizer/model-version drift；quantization/fine-tuning/multilingual/long-turn/tool-use transfer；runtime latency/KV overhead and concurrency；independent reproduction；whether diversified training removes rather than merely masks the shortcut。

### NExT-Mol: From Joint 2D/3D Generation to Representation-constrained Staged Generation

- **Candidate / Week / Score:** NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation / 2025-W08 / 25/30。
- **Source Family ID:** `next-mol-staged-1d-3d-generation`。
- **Source Type:** arXiv research paper + official author repository/checkpoint lineage + ICLR 2025 publication record。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 08:40:13 UTC；v2 submitted 2025-02-27, outside W08。The event-time mechanism and result claims are locked to v1；v2 and the current ICLR repository are later lineage, not W08 evidence replacements。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12638v1；https://arxiv.org/abs/2502.12638；https://github.com/acharkq/NExT-Mol。
- **Related Primary Sources:** https://openreview.net/forum?id=p66a00KLWN records the ICLR 2025 publication lineage；the current repository links MoLlama, DMT checkpoints and processed data through Hugging Face/OSF/Drive but exposes no release/tag or paper-pinned event-time digest。
- **Access and Verification Status:** Verified with versioned-artifact limitation。The complete v1 paper, equations, appendices, hyperparameters and current author repository are accessible；the anonymous event-time artifact, exact February commit, raw runs, dataset/checkpoint hashes and independent reproduction are Not Disclosed。The current README also states that open-sourcing remains in progress。
- **Full-read Coverage:** read metadata/revisions, Abstract, Introduction, Related Work, 1D LM, DMT diffusion/RMHA, cross-modal projector and three-stage training, all three evaluation tasks, baselines, ablations, sampling/batch/time/stability analyses, Conclusion, Ethics, Reproducibility, Limitations, methodology/training/evaluation appendices and current repository commands/checkpoint layout。
- **Original Problem:** joint diffusion over atom types, bonds and continuous coordinates can produce invalid molecular graphs and is limited by scarce high-quality 3D conformers；pure 1D molecular LMs exploit abundant strings and validity-preserving SELFIES but do not generate the 3D state required by physical tasks。The design problem is how to preserve discrete structural validity while adding continuous geometry and transferring abundant 1D knowledge into scarce 3D learning。
- **Why the Previous Design Was Reasonable:** joint equivariant diffusion keeps 2D/3D variables in one denoising process and can impose geometric symmetry directly；autoregressive coordinate generation offers an explicit factorization；specialized torsion/force-field methods embed strong chemistry priors。They remain sensible when end-to-end coupling, exact equivariance, small data or physical interpretability matters more than scaling a general Transformer。
- **Changed Constraint:** 1D molecule corpora reach billions while curated conformer sets are orders of magnitude smaller；invalid graph samples waste downstream 3D work。The system therefore needs a staged representation boundary that can leverage cheap discrete data without pretending a valid SELFIES sequence uniquely determines a correct conformer or desired physical property。
- **Mechanism:** MoLlama is a 960M decoder-only LM pretrained from scratch on 1.8B ZINC-15 molecules converted to SELFIES；task fine-tuning generates a valid 1D structure first。DMT then denoises only 3D atom coordinates while conditioning on atom and pair features through Relational Multi-Head Self-Attention。A bidirectional-attention projector maps causal SELFIES states to atom states, mean-pools multi-token atoms, inserts a learned hydrogen token and concatenates these features into DMT；training proceeds through standalone DMT, frozen-DMT projector/LoRA warmup and integrated fine-tuning。
- **State Ownership:** SELFIES/tokenizer and corpus manifest own discrete representation/validity rules；MoLlama owns 1D sequence distribution；RDKit mapping and projector own token-to-atom identity；2D graph owns atom/bond constraints；DMT owns provisional coordinate trajectory；sampler owns noise schedule/step count；property conditioner owns target value embedding；domain evaluator owns FCD/stability/RMSD/property-proxy evidence。No learned component owns chemical synthesis feasibility or deployment safety authority。
- **Control Flow / Data Flow:** `versioned molecule corpus → SMILES/SELFIES canonical or randomized serialization → MoLlama pretraining/fine-tuning → sample valid 1D molecule → SELFIES-to-atom mapping + graph features → DMT coordinate denoising → generated conformer ensemble → chemistry/property evaluators → retain/reject under domain policy`。Conditional generation injects the same property into a four-token LM soft prompt and DMT time embedding。
- **Implementation Details:** MoLlama uses 22 layers, hidden 2048, 32 query/4 KV heads, context 512, batch 512, AdamW, FlashAttention/FSDP and 555K steps over 145B tokens；pretraining uses four A100-40GB GPUs for about two weeks。DMT-B/L use 10/12 layers, 55M/150M parameters, atom/pair states and cosine diffusion；three-stage transfer warms projector/LoRA for 10 epochs and fine-tunes for 500。De novo and conditional tasks train separate task-specific weights rather than one shared universal checkpoint。
- **Evaluation Contract:** de novo generation uses GEOM-DRUGS and QM9-2014 with 10K sampled molecules and 2D/3D distribution, validity, uniqueness, novelty and geometry metrics；conditional generation trains six separate QM9 property models and measures MAE with a learned property classifier trained on a disjoint 50K half；conformer prediction uses GEOM-DRUGS/GEOM-QM9 splits, generates `2K` predictions per molecule with `K` references, and reports COV/AMR recall and precision at dataset-specific RMSD thresholds。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines include 1D MolGPT/MolGen, joint 2D/3D diffusion, equivariant diffusion, torsional diffusion/particle guidance, MCF and OMEGA/xTB。Ablations cover MoLlama transfer, unseen-scaffold slices, randomized SELFIES, DMT scale, sampler SNR, noise schedule, batch size and 5–100 sampling steps。The paper notes largest gains from 5→20 steps and diminishing returns beyond 50, but lacks multi-seed uncertainty, matched-compute architecture factorial, raw-run release and equal-hardware end-to-end generation comparisons。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** MoLlama pretraining hardware/time and task batch/epoch settings are disclosed；conditional models use four A100-80GB GPUs, repository conformer training references eight A100s, and one timing comparison uses an A100 GPU versus CPU-only OMEGA/xTB。Training precision/quantization, most task wall time/energy, dataloader/distributed efficiency, sampling concurrency, memory, tail latency and production SLO are Not Disclosed；CPU/GPU timing is not hardware-normalized。
- **What the Evidence Actually Proves:** within the disclosed molecule datasets and author evaluator contracts, staged SELFIES generation yields near-perfect reported validity and stronger distribution metrics than tested baselines；DMT improves conformer metrics over the tested scalable Transformer baseline, and adding MoLlama features improves selected COV/AMR and unseen-scaffold AMR slices。Property-conditioned two-stage models lower the learned-classifier MAE versus cited baselines。These results support representation-constrained factorization and 1D→3D transfer as viable branches。
- **What It Does Not Prove:** SELFIES validity is not synthesizability, drug efficacy, toxicity or physical stability；a learned property classifier is not quantum-chemistry ground truth；FCD/COV/AMR do not establish real discovery outcomes。The experiments do not prove general-purpose foundation-model behavior, strict unseen-chemistry generalization, end-to-end superiority under equal compute, or that non-equivariant DMT universally replaces geometric inductive bias。The authors' “chemical heuristics” explanation remains a hypothesis。
- **Limitations / Threats to Validity:** the paper explicitly reports remaining unseen-scaffold degradation, no randomized-SELFIES pretraining, causal MoLlama's representation limitation, no structure-based target-pocket generation and limited diffusion guidance。Additional threats include one-lowest-energy conformer selection in de novo GEOM training, learned proxy evaluators, task-specific checkpoints, no seeds/confidence intervals, missing artifact hashes and a current repository whose commands/settings differ from paper tables and require manual stopping or code edits for some evaluations。
- **Trade-offs / New Failure Modes:** staged generation converts one coupled validity problem into explicit interface contracts, but 1D errors or dataset bias feed every 3D sample and the chosen graph can exclude better geometric alternatives。The projector introduces token/atom/hydrogen alignment state；DMT adds iterative sampling cost and scheduler sensitivity；separate conditional checkpoints increase artifact sprawl。Randomized SELFIES improves diversity but complicates stable cross-modal mapping, so canonical serialization is used during transfer at the cost of less augmentation。
- **Where the Previous Design Still Applies:** joint 2D/3D diffusion remains useful when graph and geometry must co-adapt；equivariant/torsional/force-field models remain stronger priors for data-poor or precision-critical tasks；pure 1D generation is sufficient for screening without conformers；explicit physics simulation remains required for validated properties。NExT-Mol is a staged alternative, not a universal replacement。
- **Evolution Relationship:** `Direct Evolution` for `joint unconstrained 2D/3D generation → validity-constrained 1D proposal → conditioned 3D diffusion → 1D-to-3D representation transfer`；`Layering / Dependency` across representation, data, generation and domain evaluation；`Alternative Branch` versus joint equivariant diffusion, torsional models and physics-based conformer search。The next pressure is structure-conditioned generation, stricter scaffold splits, calibrated physical verification and end-to-end resource accounting。
- **ROADMAP Node:** canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）；handoffs to `MULTIMODAL-REPRESENTATION`, `MODEL-TOKENIZER`, `TRAIN-DATA`, `TRAIN-PRETRAINING`, `TRAIN-LORA` and `PLATFORM-EVALUATION-SYSTEM`。AI for Science remains a cross-owner route rather than a separate Part。
- **Target and Adjacent Chapters Read:** read Ch23 Representation, Ch24 Generative Paradigms and Ch25 World Models, plus Ch27 Data and Ch66 Evaluation boundaries。Ch24 owns staged AR/diffusion factorization and commit interfaces；Ch23 owns SELFIES/atom/projector identity；Data owns corpus/provenance, while Evaluation owns chemistry proxies and domain-claim limits。World Model is not the owner because no action-conditioned environment transition is modeled。
- **Existing Coverage:** Ch24 already distinguishes AR proposal, diffusion refinement, mutable state and commit boundaries but focuses on text/image/video/action workloads。NExT-Mol contributes a domain-specific case where a validity-preserving discrete proposal constrains a continuous diffusion stage and where abundant/ scarce modality data motivates transfer。The mechanism refines the staged-generation argument; scientific claims and domain evidence stay with Data/Evaluation。Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `MULTIMODAL-GENERATIVE-PARADIGMS`, with short handoffs to Representation and Evaluation。Future integration must preserve joint diffusion, staged SELFIES→3D, geometric inductive bias and explicit physics as conditional branches, and must not turn benchmark validity into drug-discovery truth。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, v2/current-artifact boundary, full two-stage state/control path, training and evaluation contracts, domain non-proof boundary, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February code/data/checkpoint/container and anonymous artifact lineage；v1→v2 semantic diff；current README versus paper hyperparameter drift；seed/confidence and matched-compute evidence；stricter scaffold/OOD tests；synthesizability/toxicity/energy validation；property-classifier calibration；joint-versus-staged error propagation；precision/energy/end-to-end cost and serving SLO；independent reproduction；structure-based target conditioning。

### video-SALMONN-o1: From Outcome-level Preference to Process-local Audiovisual Reasoning Alignment

- **Candidate / Week / Score:** video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model / 2025-W08 / 26/30。
- **Source Family ID:** `video-salmonn-o1-process-dpo`。
- **Source Type:** arXiv research paper + official author repository/demo/inference lineage + official model-checkpoint lineage + later ICML publication record。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 13:07:40 UTC；no later arXiv revision was listed at review time。The ICML 2025 publication, current repository and Hugging Face checkpoint are later lineage；they help inspect the released inference artifact but do not replace W08's v1 event state。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11775v1；https://arxiv.org/abs/2502.11775；https://github.com/BriansIDP/video-SALMONN-o1；https://huggingface.co/tsinghua-ee/video-SALMONN-o1。
- **Related Primary Sources:** https://github.com/bytedance/SALMONN supplies the author-family model lineage；the later ICML/OpenReview record establishes publication lineage but is not used to backfill event-time artifact claims。
- **Access and Verification Status:** Verified with event-time artifact limitation。The complete v1 paper, equations, appendices, current inference repository, demo and checkpoint are accessible；v1 promised code/SFT/pDPO data/checkpoints for later release, while the current repository has no immutable February tag and still labels training as “Coming soon”。The current Hugging Face card contains almost no training, evaluation, provenance, intended-use or safety contract。
- **Full-read Coverage:** read metadata, Abstract, Introduction, Related Work, architecture, visual/audio alignment, SFT data construction, process DPO derivation, rollout scoring and contrastive step selection, RivaBench construction, all main evaluation/ablation tables, training details, prompts/examples, Impact Statement, Appendix and current repository/model-card surfaces。
- **Original Problem:** audiovisual models can answer perception questions yet fail on reasoning-intensive video/audio tasks, and supervised explicit reasoning traces do not automatically improve the final answer。Outcome-only preference compares complete solutions but cannot identify which intermediate step first misread the scene or sound；online process reward/reranking adds a separate reward model or large inference-time sample budget。
- **Why the Previous Design Was Reasonable:** direct-answer SFT is cheap and avoids exposing unnecessary reasoning；full-path DPO uses a single pair label and preserves a simple offline loop；outcome reward or best-of-N is appropriate when only final correctness is observable。These branches remain sensible when traces are unreliable, step boundaries are ambiguous, or a deterministic verifier can judge only the terminal artifact。
- **Changed Constraint:** the target workload requires temporally interleaved vision and audio, while long generated solutions contain locally correct and incorrect steps。The training system needs a way to turn final-answer rollouts into step-local preference pairs without deploying an external process reward model or sampling 20 candidates at serving time。
- **Mechanism:** a SigLIP/Qwen2-based audiovisual model is first trained with ordinary and reasoning-intensive SFT data。For each difficult question, the pipeline samples full reasoning paths, compares complete solutions against the reference with GPT-4o, then selects intermediate steps whose token distributions are most sensitive to a small audiovisual-input perturbation。It rolls out multiple continuations from each selected prefix, estimates step quality from downstream answer correctness, and applies DPO to preferred/rejected next-step pairs under the same prefix and audiovisual context；the final objective combines process-level and full-path preference terms。
- **State Ownership:** video frame sampler owns visual temporal sampling；Whisper/Q-Former owns windowed audio representation；temporal interleaver owns audio/video token order；Qwen2 policy owns generated reasoning and answer tokens；reference policy anchors DPO log-ratios；trajectory builder owns prefix/step identity；GPT-4o/reference answer owns author-defined path labels；rollout evaluator owns empirical continuation correctness；perturbation/KL selector owns candidate-step priority。None of these states independently owns real-world audiovisual truth or safety authority。
- **Control Flow / Data Flow:** `video + audio → 2-fps visual frames and 0.2-s audio windows → temporal interleaving → SFT policy → sample ten full reasoning paths → retain failure-bearing questions → full-path judge pairs + selected intermediate prefixes → six continuations per selected step → downstream correctness estimate → hard/soft process preference pairs → pDPO + full-path DPO update → one-best generation → benchmark evaluator`。
- **Implementation Details:** the reported model uses SigLIP, a two-layer GELU visual aligner, Whisper-Large-v3 plus window-level Q-Former, and Qwen2-7B；visual/audio encoders and the LLM are frozen while LoRA/adapters/aligners provide trainable paths according to v1 wording。Video is sampled at 2 fps with at most 60 frames；audio produces 150 tokens per 30 seconds；LoRA uses rank 64 and alpha 256。SFT runs about 48 hours on 16 A100s and pDPO about 24 hours on 8 A100s；exact A100 memory, precision, optimizer/batch/context and reproducible event-time training code are Not Disclosed。
- **Evaluation Contract:** Video-MME without subtitles and NExT-QA test general video QA；RivaBench contains 1,912 five-choice Academic, 2,128 five-choice StandUp and 200 yes/no SynthDec questions。Academic/StandUp use YouTube audiovisual clips and expert annotation；SynthDec compares 100 Hunyuan-generated clips with 100 matched real YouTube clips。GPT-4o is given up to 30 images at 2 fps, whereas the author model can use up to 60 frames, so cross-model input contracts are not identical。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include contemporary audiovisual/video LLMs and SFT versus pDPO；some baseline values are imported rather than rerun under one environment。Ablations separate ordinary versus reasoning-intensive SFT data, direct answer versus explicit reasoning, SFT one-best, majority@20, outcome/process reward reranking@20 and pDPO one-best。The paper does not report equal-training-compute or equal-inference-compute comparisons, multi-seed uncertainty, audio-only/vision-only pDPO ablations, judge calibration, perturbation sensitivity sweeps, or end-to-end data-generation cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Qwen2-7B/SigLIP/Whisper-Large-v3, 2 fps, maximum 60 frames, 150 audio tokens per 30 seconds, LoRA rank 64/alpha 256 and aggregate A100 counts/times are disclosed。GPU memory, training/inference precision, quantization, sequence-length distribution, batch and gradient accumulation, rollout concurrency, memory, throughput, tail latency, energy, serving concurrency and SLO are Not Disclosed；reported benchmark accuracy is not a serving-performance claim。
- **What the Evidence Actually Proves:** under the author's data and evaluator contracts, pDPO one-best improves the reported SFT one-best rows from 62.9→65.6 on Video-MME, 78.2→82.3 on NExT-QA, 68.6→76.7 on RivaBench StandUp and 42.5→48.3 on Academic。It also outperforms the reported 20-sample majority/reward-reranking rows while using one sample at evaluation, supporting process-local offline preference optimization as a viable training branch。The SFT ablation is equally important: direct answering exceeds explicit reasoning before pDPO, so merely requesting a chain of thought is not the mechanism。
- **What It Does Not Prove:** the results do not show that visible reasoning is faithful, causal or interpretable；perturbation sensitivity is not proof that a step is factually wrong；GPT-4o/reference-based labels are not independent ground truth。The study does not establish general multimodal superiority, equal-compute advantage over online search/reranking, production latency, long-video behavior, multilingual robustness or general synthetic-video detection；SynthDec is a 200-item, one-generator-family slice。The headline gain over LLaVA-OneVision is not uniform across rows and must not replace exact table differences。
- **Limitations / Threats to Validity:** no explicit Limitations section, no multi-seed confidence intervals, no complete event-time artifact, no contamination analysis and no human calibration of generated training paths。Gemini-1.5-Pro and GPT-4o generate/check much of the reasoning data, and GPT-4o also helps label preference paths, creating correlated generator/judge bias。Questions are selected when SFT fails, so pDPO data emphasize a conditional hard subset；YouTube/domain and Hunyuan-only SynthDec sampling limit generalization。Prompt-template sensitivity, imported baselines, input-budget mismatch and the current repository's RivaBench/AVRBench naming drift weaken exact reproducibility。
- **Trade-offs / New Failure Modes:** process-local pairs move supervision closer to the failing prefix and avoid a serving-time 20-sample loop, but training now owns trajectory segmentation, prefix identity, perturbation policy, rollout budgets, judge versions and pair provenance。Sensitive steps may be uncertain yet correct；incorrect downstream answers can punish useful reasoning；shared model/judge biases can reinforce themselves。The pipeline adds substantial offline generation cost, frozen-backbone capacity limits and a new invalidation problem whenever template, tokenizer, frame/audio sampling, judge or reference policy changes。
- **Where the Previous Design Still Applies:** direct-answer SFT remains preferable for simple perception and latency-sensitive tasks；full-path DPO is sufficient when only terminal quality is observable；online best-of-N or verifier-guided search remains useful when test-time exploration is affordable and failures cannot be anticipated offline；external/human process supervision remains stronger when intermediate correctness must be independently grounded。pDPO is an additional branch, not a universal replacement。
- **Evolution Relationship:** `Direct Evolution` for `direct-answer SFT → explicit reasoning SFT → outcome-level preference → rollout-estimated process preference → one-best aligned inference`；`Layering / Dependency` across multimodal representation, synthetic data, trajectory evaluation and DPO；`Alternative Branch` versus external PRM, online reranking and human step labels。The next pressure is independent process evidence, immutable trajectory provenance, judge/perturbation calibration and matched-compute evaluation。
- **ROADMAP Node:** canonical owner `TRAIN-DPO`（Current Ch34；Legacy Ch30）；handoffs to `MULTIMODAL-REPRESENTATION`, `TRAIN-DATA`, `TRAIN-SFT` and `PLATFORM-EVALUATION-SYSTEM`。DPO owns the pairwise policy/reference objective and process-pair extension；Representation owns audiovisual temporal identity；Data/SFT own synthetic trace construction, while Evaluation owns judge, slice and benchmark validity。
- **Target and Adjacent Chapters Read:** read Ch33 GRPO, Ch34 DPO and Ch35 Checkpoint, plus Ch23 Multimodal Representation, Ch27 Data, Ch29 SFT and Ch66 Evaluation boundaries。Ch34 already derives sequence-level DPO and warns that pair identity, template and reference caches are versioned state；this paper contributes a process-local pair-construction branch, while Ch66 already prevents author judge/benchmark evidence from becoming a production truth claim。
- **Existing Coverage:** Ch34 covers full-response DPO, preference-data quality, offline distribution shift, pair identity and independent evaluation, but does not yet separate terminal pairs from rollout-derived intermediate-step pairs or their new trajectory/judge ownership。The evidence could later refine that evolution line, provided direct SFT, full-path DPO, human/external process labels and online search remain explicit alternatives。Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DPO`, with short handoffs to multimodal representation, Data/SFT and Evaluation。Future integration must preserve the negative SFT reasoning result, judge/perturbation uncertainty, training-versus-serving compute distinction and the fact that visible reasoning is not interpretability evidence。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, later-artifact boundary, audiovisual/trajectory state ownership, pDPO control path, exact evaluation deltas and non-proof limits, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February code/data/checkpoint/container and exact v1 training configuration；complete current training release；model-card provenance/intended-use/safety details；judge agreement and human step-label validation；perturbation magnitude/type sensitivity；audio-only/vision-only and process/full-path factorial ablations；equal-token/FLOP/cost comparison with online reranking and external PRM；multi-seed uncertainty；contamination, multilingual/long-video/domain-shift evidence；latency/energy/SLO and independent reproduction。

### InfiR: From Generic Token Scale to Capacity-aware Data and Stage Contracts

- **Candidate / Week / Score:** InfiR: Crafting Effective Small Language Models and Multimodal Small Language Models in Reasoning / 2025-W08 / 26/30。
- **Source Family ID:** `infir-capacity-aware-training-pipeline`。
- **Source Type:** arXiv research/technical report + later official Hugging Face model/checkpoint cards + dead/renamed author-repository lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 09:07:32 UTC and remains the only arXiv version。The official InfiX model collection and InfiR-1B Base/Instruct checkpoints were updated in July/August 2025, outside W08；their richer model cards are later lineage and cannot establish February artifact state。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11573v1；https://arxiv.org/abs/2502.11573；https://huggingface.co/InfiX-ai/InfiR-1B-Base；https://huggingface.co/InfiX-ai/InfiR-1B-Instruct。
- **Related Primary Sources:** https://huggingface.co/collections/InfiX-ai/infir-67b311b3bb33bc6fb81e5c74 records the later official collection；the paper points to https://github.com/Reallm-Labs/InfiR, which is not currently accessible under that identity。The current InfiXAI organization exposes later InfiR2/GUI projects, not an immutable W08 InfiR training artifact。
- **Access and Verification Status:** Verified with artifact and identity limitations。The complete v1 HTML/PDF content, equations, tables, appendix data lists and later Base/Instruct model cards/checkpoints are accessible；the paper-linked repository, event-time code/data/checkpoints, raw runs, exact data manifests and model digests are unavailable。The later card says “continual pretrained from Llama-3.2-1B,” while v1 only says training was based on that architecture, so initialization identity remains unresolved rather than inferred backward。
- **Full-read Coverage:** read metadata, Abstract, Introduction, pretraining data collection/filtering/recall/dedup/quality/decontamination, annealing and stage-specific offline evaluation, training details, SFT synthesis and rejection sampling, multimodal collection/cleaning/curriculum, all text/multimodal result tables, training observations, Conclusion, Limitation, general/math/code/long-CoT/multimodal appendices, data composition and later model cards。
- **Original Problem:** sub-2B models have limited parameter capacity but are asked to preserve reasoning, code and multimodal/GUI capability under a far smaller training and deployment budget。A generic “more tokens + one mixture + one evaluation” recipe can waste scarce capacity on noise, duplicates or easy synthetic patterns and can hide stage-specific regressions。
- **Why the Previous Design Was Reasonable:** broad web/code pretraining maximizes coverage；one static data mixture and perplexity provide cheap, stable control signals；full end-to-end multimodal tuning is simple；large-model SFT recipes reuse mature datasets。These choices remain reasonable when capacity is ample, stage boundaries are short, evaluation extraction is trustworthy, or domain specialization is not required。
- **Changed Constraint:** at roughly 1B parameters, information competition and gradient variance become visible sooner；a data mixture that improves pretraining metrics may not survive the same SFT, and large-model demonstrations may be poorly learnable。The pipeline therefore treats data selection, mixture, evaluation mode and trainable-parameter scope as stage- and capacity-dependent state rather than one fixed corpus recipe。
- **Mechanism:** raw web/math/code sources pass heuristic filtering, fastText reasoning-oriented recall, global MinHash deduplication, domain scorers/static code checks and token 10-gram benchmark decontamination。The 900B-token pretraining stage uses NLL/correct-option probability diagnostics for recall; a 40B-token annealing stage raises the share of high-quality math/code and synthetic data and switches to few-shot generation for precision。SFT combines open data, instruction evolution, Qwen2.5-32B generation, reward-model rejection sampling, sandbox code verification, domain/difficulty labels and millions of examples。Multimodal training proceeds from frozen-backbone projector alignment to ViT+adapter tuning and finally all-parameter tuning on difficult visual math/GUI trajectories。
- **State Ownership:** source manifests and licenses own raw-data identity；filters/fastText/scorers own selection policy；MinHash and 10-gram indexes own duplicate/contamination evidence；mixture manifest owns per-stage token allocation；checkpoint and optimizer own training progress；evaluation harness/parser owns stage metrics；teacher/reward/sandbox versions own synthetic-label provenance；SigLIP/projector/LLM freeze schedule owns multimodal parameter state。Model size alone owns neither privacy compliance nor edge deployability。
- **Control Flow / Data Flow:** `versioned raw corpora → heuristic/domain recall → dedup + quality + decontamination → capacity-aware mixture → 900B-token next-token pretraining → checkpoint/NLL and task diagnostics → 40B-token annealing + generation evaluation → synthetic/open SFT with reward/sandbox filtering → Base/Instruct artifact → caption alignment → staged multimodal unfreezing → text, vision and GUI benchmark evidence → release gate`。
- **Implementation Details:** v1 reports a Llama-3.2-1B architecture, 900B pretraining plus 40B annealing tokens, sequence length 4096, learning rate 1.4e-3, batch size 2048, one epoch per phase, NVIDIA NeMo with distributed optimization/DDP overlap, and 64 H800 GPUs for 90 hours (5,760 GPU-hours)。SFT uses a few million samples, Llama 3 chat template, response-only cross-entropy, four epochs, learning rate 2e-5, batch 128 and length 4096。InfiR-VL combines SigLIP-So400m, InfiR-1B and an MLP projector; exact multimodal token counts, optimizer, hardware and wall time are Not Disclosed。
- **Evaluation Contract:** Base uses few-shot MMLU/GSM8K/MATH/HumanEval/MBPP; Instruct uses zero-shot versions；long-CoT variants use AIME24, MATH500, AMC23, GPQA and OlympiadBench；multimodal uses MMMU, ScreenSpot and AndroidWorld。Dataset-selection experiments fine-tune Llama-3.2-1B under stated local recipes；COCO-caption similarity selects a 0.5 filter threshold from 2,500 pairs。Some comparison rows mix authors' reruns with parenthesized values claimed by baseline papers, so not all results share one harness or training budget。
- **Baselines / Ablations / Sensitivity / Overhead:** the paper compares raw/filtered data, pretraining mixtures, several public SFT datasets, math difficulty groups, code datasets, 200K versus 2M long-CoT samples and staged multimodal tuning observations。It reports that synthetic pretraining gains did not necessarily persist after identical SFT, motivating synthetic data only in annealing；harder math subsets can reduce data volume。However, there is no full factorial over filters/recall/dedup/decontamination, no equal-token pipeline ablation, no seeds/confidence intervals, no exact mixture sensitivity, no matched-compute architecture comparison and no end-to-end data-processing cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** v1 discloses 1B/1.6B model classes, 64 H800 GPUs, 5,760 pretraining GPU-hours, 4,096-token length and text-stage batch/LR/epoch settings。The later Base card adds BF16 mixed precision and a 2.47GB safetensors checkpoint, but this is not event-time evidence。Data-pipeline hardware, storage/network, optimizer-state memory, multimodal hardware, inference precision/quantization, device memory, latency, throughput, energy, concurrency and edge SLO are Not Disclosed；“edge deployable” is not benchmarked。
- **What the Evidence Actually Proves:** within the author's fixed 1B-scale recipes and benchmark harnesses, the complete pipeline produces stronger reported rows than Llama-3.2-1B on selected text tasks；InfiR-VL reports 76.3 ScreenSpot and 9.48 AndroidWorld while scoring 38.8 on MMMU。The training observations provide useful evidence that stage-specific evaluation, model-capacity-aware data selection, synthetic-data timing and multimodal freeze schedules can materially change outcomes。The 200K→2M long-CoT comparison supports data-scale sensitivity under that fine-tuning contract, not a universal scaling law。
- **What It Does Not Prove:** it does not isolate which pipeline component causes final gains, prove state of the art under equal architecture/token/compute/data, or show that a 1B model matches larger models generally。Ratios such as 2.26x can be inflated by a weak near-zero baseline and must not replace absolute rows；InfiR remains below Qwen2.5-1.5B on several tasks and below DeepSeek-R1-Distill-Qwen-1.5B on most hard-reasoning rows。Small model size does not prove privacy, environmental benefit or usable edge latency, and benchmark scores do not prove real OS control or safety。
- **Limitations / Threats to Validity:** v1 acknowledges standard-benchmark focus and untested real-world generalization。Additional threats include no immutable artifact, incomplete licenses/provenance, an inaccessible paper repository, later-card initialization ambiguity, mixed rerun/claimed baseline values, evaluation-parser errors found during development, no seeds, weak contamination guarantees and selection on the same benchmark families used for optimization。Appendix public-SFT rows can perform below the Llama Instruct baseline despite narrative dataset selection, and exact synthetic stages linking those rows to the final artifact are not decomposed。
- **Trade-offs / New Failure Modes:** aggressive capacity-aware filtering improves token efficiency but can remove rare knowledge, dialects or hard formats；reasoning recall and quality scorers import teacher bias；global dedup can collapse useful diversity；10-gram decontamination misses semantic leakage and can over-delete legitimate text。Stage-specific mixture/evaluation improves control but increases artifact/version state and risks benchmark overfitting。Staged multimodal unfreezing reduces early interference yet creates freeze-schedule coupling, catastrophic forgetting and connector shortcuts；millions of synthetic SFT samples can reinforce reward/judge bias。
- **Where the Previous Design Still Applies:** broader minimally filtered corpora remain useful for open-domain recall and rare-event coverage；static mixtures simplify reproducibility when domains are stable；perplexity/NLL remains a cheap pretraining sensor；fully joint multimodal training remains viable with abundant balanced data；smaller human-authored SFT sets are preferable when provenance and label quality dominate scale。Large or specialized models remain appropriate when very hard reasoning, multilingual breadth or robust perception exceeds small-model capacity。
- **Evolution Relationship:** `Direct Evolution` for `generic web/code mixture → reasoning-oriented retrieval and quality control → stage-specific pretraining/annealing mixture and evaluation → capacity-aware synthetic SFT → staged multimodal curriculum`；`Layering / Dependency` across Data, Pretraining, SFT, Representation and Evaluation；`Alternative Branch` versus broad-data scaling, large-model distillation and native multimodal pretraining。The next pressure is causal component ablation, immutable provenance, matched-compute scaling and actual device/SLO evidence。
- **ROADMAP Node:** canonical owner `TRAIN-DATA`（Current Ch27；Legacy Ch23）；handoffs to `TRAIN-PRETRAINING`, `TRAIN-SFT`, `MULTIMODAL-REPRESENTATION`, `PLATFORM-EVALUATION-SYSTEM` and edge/inference owners。Data owns selection, mixture and provenance；Pretraining/SFT own objectives and stage transitions；Representation owns fusion/freeze interfaces, while Evaluation owns parser, contamination and benchmark validity。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch27 Data, Ch28 Pretraining, Ch29 SFT and Ch66 Evaluation boundaries。Ch27 already states that no mixture is universal outside model scale/token budget/evaluation and treats synthetic generator/verifier lineage as state；Ch28 owns stage objective/checkpoint mechanics；Ch29 owns capacity-gap and demonstration quality；Ch23 owns projector/fusion identity。InfiR refines the cross-stage capacity-aware control loop rather than adding a new architecture node。
- **Existing Coverage:** the Books already cover data distribution specification, model-capacity/data coupling, synthetic-data selection bias, pretraining loss limits, SFT capacity mismatch, staged multimodal alignment and evaluation identity。InfiR adds one unusually complete end-to-end case connecting those owners, plus negative evidence that a local pretraining metric gain may disappear after SFT。This is a future refinement/connection candidate, not justification for copying the authors' exact mixture, filters or 5,760-GPU-hour recipe。Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DATA`, with short handoffs to Pretraining, SFT, Representation and Evaluation。Future integration should emphasize the stage-dependent data/evaluation contract and negative synthetic-data result, while keeping broad-data, static-mixture, human-data and joint-multimodal branches alive。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, later-model-card and dead-repository boundary, full data/stage/parameter ownership path, exact workload contract, internal inconsistencies, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February repository/code/data/checkpoint/container and model initialization identity；exact source/license/mixture manifests and filter retention rates；reward/teacher/scorer identities；component/equal-token ablations and multi-seed uncertainty；semantic contamination audit；multilingual/rare-domain/fairness regressions；multimodal hardware/data/token and freeze-schedule sensitivity；actual device memory/latency/energy/privacy/SLO evidence；independent reproduction；reconciliation of appendix SFT rows and current model-card architecture/training claims。

### LongPO: From Same-context Preference Pairs to Versioned Short-to-long Reference Contracts

- **Candidate / Week / Score:** LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization / 2025-W08 / 28/30。
- **Source Family ID:** `longpo-short-to-long-preference-optimization`。
- **Source Type:** arXiv research paper + official author repository + released data/checkpoint artifacts；ICLR 2025 publication is later venue lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 17:59:03 UTC and is the only arXiv version exposed by the metadata at review time。The repository README says `[2024.2.17] Release`, but that date conflicts with the paper event and appears to be a repository typo；the review does not silently rewrite it。Later 256K/512K experimental checkpoint cards are artifact lineage, not new W08 events。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13922v1；https://arxiv.org/abs/2502.13922；https://github.com/DAMO-NLP-SG/LongPO。
- **Related Primary Sources:** https://huggingface.co/DAMO-NLP-SG/Mistral-7B-LongPO-512K-EXP；https://openreview.net/forum?id=qTrEq31Shm。The 512K card explicitly labels 256K/512K as experimental rebuttal versions that may be under-converged or insufficiently tuned；current repository/card values are used to expose artifact drift, not to replace v1 results。
- **Access and Verification Status:** Verified with paper/artifact contract conflicts。The full v1 paper, equations, appendices, current training/data-generation code, released datasets and checkpoints are accessible；an immutable February commit/tag/container and a reconciled paper-to-code configuration manifest are Not Disclosed。Repository README date, optimizer/beta settings and RULER result rows conflict with v1 and remain versioned evidence limitations。
- **Full-read Coverage:** read metadata, Abstract, Introduction, Related Work, preliminary DPO derivation, single- and multi-turn LongPO objectives, self-instruction data generation, iterative 128K→256K→512K evolution, implementation, all long/short evaluation tables, ablation figures, appendices and current repository/card configuration。No explicit Limitations or Threats-to-Validity section exists in v1；limitations below are reconstructed from disclosed design and experiments。
- **Original Problem:** a model aligned at short context can retain useful task behavior yet fail when the same request is embedded in a much longer document。Long-context SFT requires expensive labeled sequences, while ordinary DPO needs a meaningful reference distribution on the same long input and can trade away short-context capability。The systems problem is therefore not only length extension, but constructing auditable preferences and a reference contract across different context regimes。
- **Why the Previous Design Was Reasonable:** RoPE extension plus long-context SFT directly teaches the target sequence length；standard DPO compares policy and reference under the same prompt, keeping likelihood ratios semantically aligned；retrieval or chunking avoids training the model over the full document。These remain preferable when labeled long examples exist, global evidence spans many chunks, exact same-context comparison matters, or a bounded retrieval system can satisfy the workload more cheaply。
- **Changed Constraint:** target lengths grow to 128K–512K while high-quality long-input answers, GPU memory and stable reference likelihoods become scarce。A short-context-aligned model may be a better teacher on a relevant chunk than on the full document, so preference generation, reference identity, context construction and iteration version must become explicit training state。
- **Mechanism:** sample a relevant short chunk from a long document, reverse-generate an instruction from that chunk, then let the short-context policy produce `y_S` from the chunk and `y_L` from the full long input。Treat `y_S` as chosen and `y_L` as rejected, but train both under the long input；replace standard same-context DPO reference ratios with a short-to-long constraint that compares the long-context policy against the frozen short-context model on the short input。Add sequence NLL for stabilization and use the trained 128K model as the next teacher for synthetic 256K/512K preference data。
- **State Ownership:** corpus/document manifest owns source and length；chunk sampler owns evidence-window identity；self-instruction generator owns instruction provenance；short and long serialized inputs own tokenizer/template/RoPE identity；chosen/rejected rows own teacher checkpoint and generation settings；reference/policy checkpoints own iteration stage；objective config owns beta/lambda and aggregation semantics；sequence-parallel runtime owns shard layout；evaluation harness/judge owns task slice and scoring contract。
- **Control Flow / Data Flow:** `versioned long document → eligible-length filter → short-chunk sample → reverse-generated instruction → short-input teacher answer y_S + full-input answer y_L → pair/provenance admission → long-input LongPO ratio + NLL update → 128K checkpoint → next-iteration teacher/data → experimental 256K/512K checkpoint → long/short evaluation`。
- **Implementation Details:** data comes from Book/ArXiv subsets of Long-Data-Collection and a GitHub subset of RedPajama；documents are filtered between 64K and the target length, chunks are at most 32K, up to four chunks are sampled per document, four instructions are generated and one is selected。The paper reports 45K Mistral and 32K Qwen pairs at 128K, then 16K/2.5K Mistral pairs at 256K/512K。V1 reports Adam, learning rate `5e-7`, DPO beta `0.1`, NLL lambda `0.01`, batch 8 and RoPE theta `1e7`；the current launcher instead exposes RMSprop, beta `0.01`, BF16/TF32 and batch 1×gradient accumulation 8。This is configuration drift, not a harmless implementation synonym。
- **Evaluation Contract:** InfiniteBench is restricted to En.Sum, En.QA and En.MC with contexts over 100K；RULER is reported at multiple lengths, but prose says Aggregation is excluded while the table/card include `AGG` and claim 13 tasks。LongBench-Chat uses GPT-4-Turbo-1106-Preview as judge；MMLU 5-shot, ARC-Challenge 25-shot, HellaSwag 10-shot and WinoGrande 5-shot test short capability。The phrase about filtering English LongBench-Chat samples is internally ambiguous and cannot define a clean slice without artifact-level reconstruction。
- **Baselines / Ablations / Sensitivity / Overhead:** compares base, long SFT, standard DPO, LongPO, SFT on chosen/rejected responses, removal of short-to-long constraint and removal of NLL；also reports 128K/256K/512K iterative stages and Mistral/Qwen backbones。Ablations are primarily figure trajectories without seed uncertainty。There is no causal audit of pair correctness, chunk/instruction sampling, truly cross-chunk tasks, equal-compute alternatives, beta/lambda sweeps, teacher-error amplification, multiple random seeds or independent reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** v1 uses Mistral-7B and Qwen2-7B, eight A800 80GB GPUs for 128K and sixteen A800 80GB GPUs for 256K/512K, DeepSpeed-Ulysses sequence parallelism and FlashAttention。Reported training throughput is 4,401/4,120/2,744 tokens/s at 128K/256K/512K。Paper text does not disclose precision；current code uses BF16/TF32 but is not configuration-identical。Wall time, optimizer memory, network topology, energy, inference concurrency, latency and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' synthetic pair construction and disclosed Mistral/Qwen harness, LongPO outperforms tested SFT and standard-DPO branches on the selected long-context rows while mostly preserving the reported short-task averages。For Mistral, v1 InfiniteBench average rises from 13.82 base and 30.03 SFT to 39.27 at 128K, then 39.65/41.21 at experimental 256K/512K。The experiments support short-context behavior as a useful conditional teacher and cross-context preference/reference design as a viable training branch；they do not establish a universal long-context scaling law。
- **What It Does Not Prove:** the sampled short answer is not externally verified and need not dominate the full-context answer；reverse-generating an instruction from one chunk structurally favors local evidence and does not prove global multi-chunk reasoning。The paper does not prove 512K production reliability, equal-compute superiority, universal short-capability preservation or a general win over GPT-4: the headline comparison uses only three InfiniteBench tasks, mixed baseline provenance and excludes stronger rows such as Llama-3.1-70B。Qwen short-task average decreases from 74.38 to 73.79, so “no degradation” is not literally universal。
- **Limitations / Threats to Validity:** teacher and student share model-family blind spots；synthetic instruction/pair selection can reward answerability from one local chunk and amplify teacher errors across iterations。No human/external pair audit, cross-document evidence task, multilingual/adversarial distraction test, seed interval or explicit limitations section is provided。Equation 14 prints an NLL term without an evident negative log, and the multi-turn formula aggregates probabilities in an unusual way；code must define the executable objective。Paper versus current code/card conflicts in optimizer, beta and RULER values prevent a single unqualified reproduction claim。
- **Trade-offs / New Failure Modes:** short-to-long referencing avoids asking an incompetent long-context reference to calibrate the pair, but compares probabilities conditioned on different inputs and can entangle context difficulty with preference。Synthetic local instructions reduce annotation cost while narrowing global reasoning coverage。Iterative self-evolution extends length with fewer examples, but introduces teacher-version lineage, error amplification and stage rollback requirements。Ulysses/FlashAttention make training feasible yet add topology/sharding constraints；full-length NLL stabilizes learning at additional compute and may overweight long chosen sequences。
- **Where the Previous Design Still Applies:** same-context DPO remains the cleaner choice when both reference and policy handle the target prompt；long SFT remains appropriate with trusted demonstrations；retrieval/chunking remains cheaper and more auditable when evidence is sparse；context-extension pretraining remains necessary for representation/position limits；human-verified long tasks remain preferable for global synthesis。128K can be the safer operating point when later experimental stages lack convergence evidence。
- **Evolution Relationship:** `Direct Evolution` for `long-context SFT / same-context DPO → short-context teacher generates cross-context pair → short-to-long reference constraint + NLL → versioned iterative length extension`；`Layering / Dependency` across Data, DPO, Long Context and Distributed Training；`Alternative Branch` versus retrieval, long SFT and continued pretraining。The next pressure is verified global-evidence pairs, executable objective/version identity, calibrated teacher succession and serving-cost evidence。
- **ROADMAP Node:** canonical owner `TRAIN-DPO`（Current Ch34；Legacy Ch30）；handoffs to `MODEL-LONG-CONTEXT`, `TRAIN-DATA`, `TRAIN-SFT`, `TRAIN-PRETRAINING`, `TRAIN-DISTRIBUTED-TRAINING` and `PLATFORM-EVALUATION-SYSTEM`。DPO owns the changed preference/reference objective；Long Context owns capability and position/attention limits；Data owns pair provenance；Distributed Training owns sequence parallel execution。
- **Target and Adjacent Chapters Read:** read Ch33 GRPO, Ch34 DPO and Ch35 Checkpoint, plus Ch22 Long Context, Ch27 Data, Ch28 Pretraining, Ch29 SFT, Ch36 Distributed Training and Ch66 Evaluation boundaries。Ch34 already owns pair/reference identity and chosen-likelihood risks but does not yet cover cross-context reference semantics；Ch22 already separates long-context capability from runtime cost。LongPO refines an existing DPO argument rather than creating a new knowledge node。
- **Existing Coverage:** the Books already explain same-input DPO log-ratio semantics, cached reference invalidation, data/version identity, long-context training versus serving and sequence-parallel runtime。LongPO adds a meaningful alternative branch in which teacher/reference inputs differ, plus iterative teacher succession and local-evidence selection bias。That mechanism is not currently redundant, but Historical Books Gate remains closed and no paper result is copied into Books in this phase。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DPO`, with short handoffs to Long Context, Data, Distributed Training and Evaluation。Future integration must preserve same-context DPO, retrieval and long-SFT branches, and must expose cross-input probability semantics, teacher lineage, global-evidence blind spots and artifact drift。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, full short-to-long mechanism/state/evaluation contract, iterative evolution, formula ambiguity, paper/code/card conflicts, Stable Node owner and deferred Books disposition；no Books change。
- **Open Questions:** immutable February code/data/checkpoint/container digest；reconciled optimizer/beta/NLL formula and multi-turn executable objective；paper-versus-card RULER table diff；human/external pair correctness；global multi-chunk and adversarial-distraction evaluation；teacher-error propagation and rollback；multi-seed/equal-compute sensitivity；precision/network/wall-time/energy and inference SLO；whether later 256K/512K artifacts converge under a fixed contract。

### Temporal Heads: From Readable Activation to Localized Temporal-recall Intervention

- **Candidate / Week / Score:** Does Time Have Its Place? Temporal Heads: Where Language Models Recall Time-specific Information / 2025-W08 / 24/30。
- **Source Family ID:** `temporal-heads-circuit-intervention`。
- **Source Type:** arXiv research paper；official author repository/data and ACL 2025 acceptance are later artifact/publication lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 and is the only arXiv version at review time。The paper was the complete event-time source；the official repository records paper preprint on 2025-02-20, ACL acceptance on 2025-05-15 and code/data release on 2025-05-30。Later artifacts are not projected backward into W08 reproducibility。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14258v1；https://arxiv.org/abs/2502.14258。
- **Related Primary Sources:** https://github.com/dmis-lab/TemporalHead；https://huggingface.co/datasets/dmis-lab/TemporalHead。The repository exposes seven notebooks and three commits but no event-time release/tag；its Python/PyTorch/CUDA environment and datasets document later reproduction lineage only。
- **Access and Verification Status:** Verified with event-time artifact limitation。The full v1 paper, equations, data statistics, ablation/editing appendices and explicit limitations are accessible；February code/data/commit/container, raw runs, seed records and independent reproduction are Not Disclosed。The paper's CRS equation contains an apparent definition ambiguity, so the executable later notebook is required for exact metric reconstruction。
- **Full-read Coverage:** read metadata, Abstract, Introduction, circuit and knowledge-circuit background, EAP-IG implementation, dataset construction, CRS, temporal-head identification, ablation, alias conditioning, activation injection/editing, Related Work, Conclusion, Limitations and all appendices covering causal tracing, data statistics, full results, hyperparameters and editing metrics；also inspected the later official repository structure and environment instructions。
- **Original Problem:** temporally changing facts cannot be modeled as timeless key-value records: the same subject/relation maps to different objects at different years。Behavioral probing can reveal model errors but not whether the forward path uses a specialized internal route, while global model editing may overwrite unrelated knowledge。The research question is whether a localized, causally testable subgraph mediates year-conditioned recall。
- **Why the Previous Design Was Reasonable:** black-box temporal QA directly measures user-visible correctness；retrieval and timestamped external stores provide updateable source-of-truth state；global fine-tuning/model editing can change many related facts；probe/readout analysis cheaply locates candidate information。These remain preferable when knowledge freshness, provenance, cross-document reasoning or production correctness matters more than explaining one frozen checkpoint's internals。
- **Changed Constraint:** stronger mechanistic claims require moving from decodability to intervention while controlling numeric-token shortcuts, static knowledge and general QA。At the same time, model/head identity, prompt serialization, pruning threshold, corrupted baseline and temporal dataset revision become part of the evidence object rather than incidental experiment settings。
- **Mechanism:** construct clean and temporally corrupted subject–relation–object prompts；use EAP-IG with integrated gradients to prune a TransformerLens computation graph into temporal knowledge circuits；find attention heads that recur in temporal circuits but not invariant circuits；zero those heads and measure candidate-object probability shifts；test indirect textual time aliases；finally extract a source prompt's attention value and inject its averaged vector at the target prompt's temporal-token position with a coefficient `lambda`。
- **State Ownership:** Wikidata-derived temporal rows own fact/time validity；clean/corrupt prompt pairs own counterfactual identity；tokenizer/model checkpoint own layer/head/token coordinates；EAP-IG config owns `ig_steps`, top-N and threshold；circuit artifact owns selected nodes/edges and CRS；ablation hook owns intervention scope；source/target prompt set and lambda own edit identity；evaluation harness owns candidate objects, answer matching and control datasets。A named head does not own durable fact truth。
- **Control Flow / Data Flow:** `versioned temporal fact + time → clean/corrupted prompts → baseline logits → EAP-IG edge attribution → thresholded circuit → recurrent temporal-head candidate → head ablation → temporal/invariant/QA comparison → alias-conditioned circuit → source activation extraction → target temporal-token injection → first-token/full-text validation`。
- **Implementation Details:** experiments use Llama-2-7B-Chat, Qwen1.5-7B-Chat and Phi-3-mini-4k-Instruct with TransformerLens；EAP-IG uses `split_qkv_input=true`, 100 integrated-gradient steps, top 5,000 edges and default threshold `0.1`。Each run uses one A100 80GB and is reported under 30 minutes。Temporal rows cover seven categories and 387 cases across 1996–2020/1999–2009；invariant controls contain 171 cases；general QA uses 11,313 TriviaQA and 2,585 Math-ChroKnowledge items。Editing sweeps `lambda∈{1,3,6}` with forward hooks。
- **Evaluation Contract:** temporal accuracy is a candidate-object probability measure rather than unrestricted generation accuracy；circuits are summarized with CRS, node/edge counts and selected years。Head ablation is compared against invariant facts and general QA；alias experiments use event-based textual time expressions；editing reports first-token probability shift and whether expected entity text appears。Zero-shot greedy inference is used, but precision, tokenizer revision, prompt-set digests and random seeds are Not Disclosed。
- **Baselines / Ablations / Sensitivity / Overhead:** main intervention is selected temporal-head ablation versus intact model, plus invariant/QA negative controls, numerical non-temporal controls, textual aliases, model-family replication and all-head editing heatmaps。Llama temporal average changes 29.7→25.6, Qwen 22.4→19.8 and Phi-3 35.4→26.0, while reported invariant/TriviaQA aggregates move little。There is no random-head matched control table, threshold/top-N/IG-step sensitivity, multiple seeds, fact-held-out discovery test, alternative circuit method, editing side-effect suite or matched global-edit/RAG baseline。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** three 3.8B/7B-class chat/instruct checkpoints and one A100 80GB are disclosed；each circuit run is under 30 minutes。Prompt lengths, batch size, precision, CUDA/kernel details at event time, full study GPU-hours, memory peaks, editing latency, concurrency, energy and production SLO are Not Disclosed。Later repository recommends Python 3.10.14+, PyTorch 2.4.0+ and CUDA 12.2, but those are not frozen v1 runtime facts。
- **What the Evidence Actually Proves:** for the disclosed frozen checkpoints and temporal datasets, EAP-IG repeatedly selects particular heads；ablating those selected heads reduces the tested temporal candidate probability more than aggregate invariant/QA controls, and related heads can appear under selected textual aliases。Activation injection can shift some target predictions without changing model parameters。This supports a localized routing contribution to year-conditioned recall in those cases and strengthens evidence beyond mere probe decodability。
- **What It Does Not Prove:** it does not prove time-specific facts are stored exclusively in those heads, that the heads have one human-readable function, or that their coordinates transfer across checkpoints。Low baseline temporal averages and aggregate controls do not establish per-example selectivity；editing the expected string does not verify full factual consistency, temporal reasoning or absence of collateral changes。The work does not show safe knowledge updating, current-fact freshness, GQA-wide applicability or production value over retrieval。
- **Limitations / Threats to Validity:** the authors acknowledge weak coverage of unstructured temporal QA and EAP-IG's inability to cleanly support GQA models；Llama-3 observations are therefore lower-fidelity exploratory evidence。Circuit selection and evaluation reuse related facts/prompts, model head locations vary, and alias CRS is lower。The printed CRS definition around Equation 6 appears not to make deviation explicitly depend on `P`, while Appendix delegates execution to `one_score`; exact faithfulness therefore depends on code。Later code release, no seeds/confidence intervals and no independent reproduction limit reliability。
- **Trade-offs / New Failure Modes:** pruning creates a readable sparse graph but can omit distributed/backup paths；lower thresholds recover backup heads while reducing interpretability。Hard ablation gives necessity evidence but can induce out-of-distribution residual states；activation injection is cheap and reversible yet depends on exact layer/head/token coordinates, coefficient tuning and source-prompt bias。Localized edits can improve one expected entity while corrupting neighboring years, other relations or generated continuations, none of which are comprehensively tested。
- **Where the Previous Design Still Applies:** behavioral temporal benchmarks remain the primary correctness check；RAG/versioned knowledge stores remain superior for fresh, attributable facts；global fine-tuning/editing remains useful when many related behaviors must change；probes remain cheap discovery tools；MLP/feature/subspace analyses remain necessary for distributed mechanisms。Temporal-head intervention is a mechanism-evidence branch, not a replacement for model or platform knowledge lifecycle。
- **Evolution Relationship:** `Direct Evolution` for `behavioral temporal QA → circuit attribution → localized ablation → alias control → activation intervention`；`Layering / Dependency` from representation evidence to Attention mechanics and Evaluation；`Alternative Branch` versus retrieval, global model editing and feature/subspace analysis。The next pressure is held-out causal replication, GQA-compatible tooling, side-effect auditing and provenance-aware temporal updates。
- **ROADMAP Node:** canonical owner `WORLDVIEW-REPRESENTATION`（Current Ch5；Legacy Ch5）；handoffs to `MODEL-SELF-ATTENTION`, `MODEL-TRANSFORMER-LAYER`, `PLATFORM-EVALUATION-SYSTEM`, `AGENT-RAG` and `AGENT-MEMORY`。Representation owns the correlation→intervention evidence ladder；Self-Attention owns Q/K/V/head mechanics；Evaluation owns external temporal correctness, while RAG/Memory own mutable knowledge state。
- **Target and Adjacent Chapters Read:** read Ch4 Why Models Learn, Ch5 What Neural Networks Learn and Ch6 Why Transformer, plus Ch14 Self-Attention and Ch66 Evaluation boundaries。Ch5 already distinguishes correlation, decodability, intervention and cross-model replication, and requires replacement/pruning faithfulness budgets；the paper is a concrete refinement case, not a new chapter or Self-Attention mechanism owner。
- **Existing Coverage:** Ch5 already states that localized intervention is stronger than readable activation but does not establish a complete mechanism, and that circuit evidence must report pruning thresholds, reconstruction/graph completeness, original-model interventions and model/prompt scope。Temporal Heads adds time-conditioned clean/corrupt design, negative controls, backup-path threshold behavior and coordinate/version fragility。This can refine a future example, but Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `WORLDVIEW-REPRESENTATION`, with short handoffs to Self-Attention and Evaluation。Future integration must present Temporal Heads as limited causal evidence, preserve RAG/global-edit alternatives and avoid the database-like claim that a few heads uniquely store time。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, event-time versus May artifact boundary, circuit/ablation/editing state flow, workload and score conditions, CRS/tool limitations, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February code/data/environment and prompt/model digests；CRS executable formula reconciliation；random-head and alternative-method controls；threshold/top-N/IG-step sensitivity；held-out fact and cross-checkpoint replication；GQA-compatible circuit extraction；per-example and neighboring-year collateral effects；activation-edit success denominator and side-effect suite；precision/total compute/edit latency；independent reproduction and comparison with provenance-aware retrieval/model editing。

### LongWriter-V: From Long-output SFT Distribution to Correlated Prefix-level Preference Reuse

- **Candidate / Week / Score:** LongWriter-V: Enabling Ultra-Long and High-Fidelity Generation in Vision-Language Models / 2025-W08 / 27/30。
- **Source Family ID:** `longwriter-v-output-length-iterdpo`。
- **Source Type:** arXiv research paper + official author repository/data/model lineage；ACM MM 2025 labeling and later Agent/Ruler additions are subsequent publication/artifact evolution。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 18:47:36 UTC and is the only arXiv version。The paper links the project, but the current 34-commit repository has no visible paper-pinned release/tag and includes later LongWriter-Agent-V/LongWrite-V-Ruler evolution；only v1 establishes W08 claims。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.14834v1；https://arxiv.org/abs/2502.14834；https://github.com/THU-KEG/LongWriter-V。
- **Related Primary Sources:** official repository links LongWriter-V-22K, MMLongBench-Write and model cards on Hugging Face, plus current evaluation/inference code。Those mutable artifacts support lineage and current inspectability but do not supply an immutable event-time environment or exact v1 run manifest。
- **Access and Verification Status:** Verified via the complete 31-page v1 PDF because arXiv HTML returned a cache miss；metadata and official repository identity are verified。Training hardware, precision, optimizer, batch size, DPO beta, decoding parameters, event-time commit/data/model hashes and raw judge/human-vote records are Not Disclosed。Several unit/slice counts conflict internally and remain evidence limitations。
- **Full-read Coverage:** read metadata, Abstract, Introduction, MMLongBench-Write and Ruler construction, controlled SFT-length experiment, plan-and-write data pipeline, single/multi-image/backtranslation sources, human correction workflow, SFT and IterDPO equations, GPT-feedback mixing, complete evaluation tables, human evaluation, all ablations, Related Work, Conclusion, Limitations, Ethics, annotation/prompt appendices and long output cases；inspected current repository training/evaluation/artifact links。
- **Original Problem:** long visual input capacity does not imply the model will produce long, coherent and image-grounded output。Visual instruction tuning is dominated by short captions/grounding answers, so autoregressive models learn an early-stop/short-response distribution；simply extending output introduces repetition and hallucination, while whole-document human preference annotation is expensive。
- **Why the Previous Design Was Reasonable:** short visual responses reduce decode cost, exposure error and hallucination surface；single-pass generation preserves one causal history；whole-response DPO matches the user-visible artifact；human revision gives direct quality feedback；caption→LLM pipelines decouple vision from long-form writing。These remain preferable for concise QA, latency-bound serving, globally coupled narratives or cases where per-segment acceptance could hide document-level inconsistency。
- **Changed Constraint:** professional/creative tasks may request 1,000–4,000+ words from 1–30 images, but only limited long-output demonstrations and 72 fully revised scripts are affordable。Length compliance, visual fidelity, section/page coverage and global coherence must therefore be modeled as separate contracts, and feedback reuse must expose segment/prefix dependency rather than pretending annotations are independent。
- **Mechanism:** first generate an outline with paragraph word budgets, then let GPT-4o write paragraphs sequentially conditioned on images, instruction, outline item and previous text；filter/augment single-image, synthetic multi-image and PPT inputs, and backtranslate exact length requirements into 5K instructions。SFT Qwen2.5-VL on a 10K long-output slice。For IterDPO, align each PPT page with original/revised script segments and create cumulative prefix preferences `(v<=i, y_w<=i, y_l<=i)` for every page, then mix 1,477 human-derived prefix pairs with 1,367 GPT-4o-ranked pairs。
- **State Ownership:** source dataset/license owns image/instruction provenance；image group/PPT page order owns visual sequence identity；GPT-4o outline and paragraph generator own synthetic-target lineage；length-unit and backtranslation prompt own request semantics；SFT manifest owns output-length distribution；annotator/reviewer owns correction provenance；segment alignment owns page-to-prefix boundaries；DPO row owns cumulative chosen/rejected/reference identity；judge/human-vote harness owns evaluation；serving owns decode/KV/stop state。
- **Control Flow / Data Flow:** `versioned images/instruction → long-output eligibility filter or multi-image/PPT synthesis → outline + paragraph budgets → sequential paragraph generation → concatenated SFT target → length-distribution sampling → SFT checkpoint → page-aligned model script → expert per-page revision → cumulative prefix pairs + GPT-ranked pairs → DPO checkpoint → length/quality/human evaluation → release gate`。
- **Implementation Details:** MMEvol 480K rows are filtered first by response length >128, then by GPT-4o long-output/image relevance to 8,115 single-image instructions；6,313 synthetic multi-image rows and 7,730 Zenodo10K PPT rows yield 22,158 examples。Five thousand instructions receive length backtranslation。The full dataset reports mean 2,037 and median 1,732, while training samples 10K rows averaging 2.8K；Qwen2.5-VL-7B/72B are trained three epochs at `1e-5`/`7e-6`, using 280×280 images and up to 30 images under a 32K context。Seventy-two valid human-revised scripts cost about one week/$1,000 and expand to 1,477 cumulative prefix pairs；final DPO uses 2,844 pairs。
- **Evaluation Contract:** MMLongBench-Write has six tasks ×20 examples =120, half Chinese and half English, split across professional and creative writing。`S_l` asymmetrically penalizes over/under requested length；GPT-4o-2024-08-06 scores relevance, accuracy, coherence, clarity, breadth/depth and reading experience, and overall `S` averages length and quality。Human comparison covers four models, 120 responses, two annotators and 720 votes per annotator。The paper also defines a small Ruler stress test, but says eight examples × four lengths =32 prompts while a result paragraph mentions 12 instructions。
- **Baselines / Ablations / Sensitivity / Overhead:** compares three proprietary VLMs, three open VLMs, caption+LLM baselines and trained 7B/72B models；SFT controls 10K datasets with mean output 0.8K/1.8K/2.8K and reports the fraction over 4K；ablates single-image, multi-image and backtranslation sources, cumulative iterative pairs and GPT feedback。Removing multi-image data causes the largest reported score drop；removing iterative pairs leaves overall score equal but lowers quality/PPT while increasing length。No matched-token/compute control, segment-boundary/cumulative-versus-independent pair ablation, multi-seed uncertainty, global-coherence checker or standard-capability regression test is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models are Qwen2.5-VL 7B/72B with disclosed learning rates, epochs, 32K context, 280×280 image resize, up to 30 images and 10K SFT/2,844 DPO rows。GPU type/count, precision, optimizer, batch/accumulation, beta/reference materialization, packing, training time/energy, generation max tokens, inference latency/throughput, concurrency and production SLO are Not Disclosed。Requested length is usually described in words, while several claims/table captions switch to tokens or inconsistent bins。
- **What the Evidence Actually Proves:** under the authors' 120-task bilingual benchmark and judge/human contracts, changing SFT output-length distribution materially changes generated length；the trained 7B closes much of the tested 72B gap, and adding the disclosed mixed DPO set improves automatic overall score from 81.8 to 84.6。The ablation supports multi-image/PPT coverage and GPT-ranked pairs as important in this recipe；prefix-level cumulative preferences are a feasible way to reuse scarce aligned corrections。
- **What It Does Not Prove:** generating the requested word count is not evidence of global coherence, factuality or visual grounding；72 PPT revisions do not establish six-task generality。Cumulative prefixes share annotations/tokens and are not 1,477 independent preference judgments。GPT-4o generates much SFT data, supplies captions, ranks AI feedback and judges quality, creating correlated preference；two-annotator win rates lack agreement/confidence reporting。The paper does not prove general superiority to GPT-4o, production-scale long decoding or that SFT data absence is the sole output-length bottleneck。
- **Limitations / Threats to Validity:** authors acknowledge 22K diversity limits, English/Chinese-only scope and high human-feedback cost；they also warn of misleading outputs beyond image content。Additional threats include training/evaluation task overlap in style, vague word/token units, Ruler 8-versus-12 count conflict, table-text length-bin mismatch, no immutable run artifact, no seeds, judge self-preference, no per-task human breakdown, and a source case that visibly repeats ideas despite the long-quality claim。Length score and mixed overall average can hide fidelity regression in individual slices。
- **Trade-offs / New Failure Modes:** long-output SFT shifts stop/length behavior but increases decode/KV cost, exposure error, repetition and fabricated detail。Plan-and-write supplies structure yet commits to an outline before discovering later evidence and uses synthetic paragraphs as targets。Cumulative prefix DPO localizes page corrections and improves annotation reuse, but early edits appear in many later pairs, overweighting prefixes and entangling local corrections with document history；segment alignment errors propagate。Mixing AI pairs adds coverage while importing judge/style bias。
- **Where the Previous Design Still Applies:** concise VLM answers remain best for latency and grounded QA；caption+LLM composition remains modular when vision caption fidelity is auditable；whole-document preference remains necessary for global narrative/argument structure；SFT-only remains simpler where preference data is weak；retrieval/citation and external verification remain necessary for professional factual reports；hierarchical Agent writing remains an inference-time alternative when retraining is unavailable。
- **Evolution Relationship:** `Direct Evolution` for `short visual SFT → length-distribution-controlled long SFT → outline/paragraph synthetic targets → human page-level correction → cumulative-prefix IterDPO + AI feedback`；`Layering / Dependency` across SFT, DPO, multimodal representation, decode runtime and Evaluation；`Alternative Branch` versus caption+LLM and inference-time writing agents。The next pressure is independent global-quality evidence, uncorrelated preference sources and resource-aware serving。
- **ROADMAP Node:** canonical owner `TRAIN-DPO`（Current Ch34；Legacy Ch30）；handoffs to `TRAIN-SFT`, `TRAIN-DATA`, `MULTIMODAL-REPRESENTATION`, `INFER-PREFILL-DECODE`, `INFER-KV-CACHE`, `AGENT-WORKFLOW`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。DPO owns cumulative-prefix preference semantics；SFT/Data own length curriculum and synthetic provenance；Inference owns long decode state/cost。
- **Target and Adjacent Chapters Read:** read Ch29 SFT, Ch33 GRPO, Ch34 DPO and Ch35 Checkpoint, plus Ch23 Representation, Ch43 Prefill/Decode, Ch45 KV Cache, Ch66 Evaluation and Ch81 Workflow boundaries。Ch34 already owns sequence-length effects, pair identity and style shortcuts but not correlated cumulative-prefix reuse；Ch29 owns output-length curriculum。One canonical DPO owner avoids duplicating the same mechanism across multimodal and Agent chapters。
- **Existing Coverage:** the Books already separate response length/format from correctness, require same prompt/template identity for DPO and warn that length shortcuts can improve pair likelihood without task quality。LongWriter-V adds a concrete evolution from whole-document correction to page-aligned cumulative preference prefixes and exposes the annotation-efficiency versus correlation trade-off。This is a future refinement candidate; Historical Books Gate remains closed。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DPO`, with short handoffs to SFT, Inference, Workflow and Evaluation。Future integration must preserve short-answer, SFT-only, whole-document DPO and Agent-writing branches, and must treat each prefix as correlated evidence rather than multiplied independent feedback。
- **Changed Files or Rejection Reason:** added the PDF-v1-locked 30-field Source Review, HTML-cache fallback record, length-curriculum and IterDPO state/control flow, workload/human/judge contracts, unit/slice conflicts, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable February code/data/model/container and exact current-to-v1 diff；word-versus-token and Ruler/bin reconciliation；GPU/precision/batch/optimizer/beta/decoding contract；prefix weighting and effective independent sample size；segment alignment sensitivity and whole-document coherence；judge-source separation and annotator agreement；standard capability regression, multi-seed/equal-compute results；copyright/privacy/source manifest；latency/KV/cost/energy/tail SLO and independent reproduction。

### Intuitive Physics from Natural Videos: From Pixel Reconstruction to Latent Surprise, Not Yet Action-conditioned World State

- **Candidate / Week / Score:** Intuitive physics understanding emerges from self-supervised pretraining on natural videos / 2025-W08 / 26/30。
- **Source Family ID:** `vjepa-intuitive-physics-latent-surprise`。
- **Source Type:** arXiv research paper + official Meta research repository with evaluation code, raw surprise outputs and figure-reproduction artifact。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 14:27:14 UTC and is the only arXiv version at review time。The v1 HTML header renders a later document date, but submission history is authoritative for W08 ownership；no later arXiv revision is projected backward。
- **Direct Primary Sources:** https://arxiv.org/html/2502.11831v1；https://arxiv.org/abs/2502.11831；https://github.com/facebookresearch/jepa-intuitive-physics。
- **Related Primary Sources:** the official repository contains the paper's processed performance, raw surprise tensors, figure notebook and V-JEPA/VideoMAEv2 evaluation code；it has no immutable event-time release/tag and does not expose the complete pretraining pipeline or all trained checkpoints used by the study。
- **Access and Verification Status:** Verified with reproducibility limitations。The complete 24-page v1 paper, equations, methods, evaluation protocol, hyperparameters, ablations and appendices are accessible；the official repository exposes evaluation artifacts。Exact event-time commit, full pretraining logs/checkpoints, seed manifests, dataset snapshots, cluster topology, total wall time and independent reproduction are Not Disclosed。
- **Full-read Coverage:** read metadata, Abstract, motivation and related design branches, violation-of-expectation protocol, latent prediction mechanism, all three benchmark analyses, property-level significance tests, masking/data/model-size ablations, Discussion, complete Materials and Methods, training/evaluation hyperparameters, context-sweep sensitivity, data-diversity appendix, private IntPhys test, contextualization-event caveat and per-property appendix；inspected official raw-result, figure and evaluation-code documentation。
- **Original Problem:** pixel-perfect future generation spends capacity on unpredictable texture, while text-only multimodal models are not trained to expose a calibrated sensory prediction error。Hand-coded object/3D simulators provide useful inductive bias but narrow the representation and environment contract。The question is whether a general self-supervised predictor can learn latent regularities from natural video that are sufficient to detect physically impossible continuations without task-specific fine-tuning。
- **Why the Previous Design Was Reasonable:** explicit simulators make objects, geometry and causal rules inspectable and controllable；pixel prediction preserves reconstructable observations and supports generation；MLLMs provide semantic reasoning through language；task-specific classifiers optimize directly for benchmark labels。They remain preferable for known dynamics, visual synthesis, instruction-conditioned explanation or calibrated deployment decisions；the paper's latent surprise branch solves a different evidence problem。
- **Changed Constraint:** the system must discard unpredictable low-level detail while preserving predictable structure, transfer out of distribution to synthetic/real violation pairs and produce a quantitative surprise signal without physics labels。This shifts the design target from reconstructing every pixel to learning which latent state components are predictable, but also makes encoder identity, temporal window, context sweep and surprise aggregation part of the evaluation contract。
- **Mechanism:** V-JEPA corrupts a video by masking spatiotemporal blocks；a context encoder processes visible patches, an EMA target encoder represents masked targets, and a predictor minimizes L1 distance between predicted and target latent representations。At evaluation, the first `C` frames condition prediction of `M` future-frame representations；L1 prediction error becomes time-local surprise, then average or maximum surprise distinguishes possible from impossible videos。The model is trained with block masking rather than the causal future task used at evaluation。
- **State Ownership:** dataset/version owns natural-video distribution；mask sampler owns visible/target partition；context encoder owns current latent observation；EMA target encoder owns slowly changing representation targets；predictor owns conditional latent estimate；frame skip, context length, window and stride own temporal contract；benchmark pair/property owns violation identity；surprise aggregation owns decision statistic；evaluation harness owns property-specific selection。None of these components owns an explicit persistent environment state or action policy。
- **Control Flow / Data Flow:** `versioned natural clip → patch/tubelet encoding + mask → context latent → predictor → EMA target latent → L1 representation loss` during pretraining；`OOD possible/impossible video → rolling C-frame context → M-frame latent prediction → observed target encoding → time-local surprise → property-specific context/aggregation → pairwise decision or single-video AUROC` during evaluation。
- **Implementation Details:** encoders are ViT-B/L/H with 16×16×2 tubelets, 16 frames at 224×224 and 5.33 fps；the predictor has 12 blocks and 384 embedding dimensions。Training uses RoPE split over height/width/time, AdamW, BF16, batch 3,072, 90,000 iterations, warmup 12,000, learning rate 2e-4→6.25e-4→1e-6, weight decay 0.04→0.4 and A100 80GB accelerators。Default masking unions eight 0.15-scale and two 0.7-scale spatial blocks；random-mask and causal-block alternatives are ablated。
- **Evaluation Contract:** frozen models are evaluated out of distribution on IntPhys dev (~360 videos), GRASP (~4,000) and InfLevel-lab (~4,000) using matched possible/impossible pairs；the private IntPhys test contains 3,600 videos per property。V-JEPA/VideoMAEv2 use prediction surprise, while Qwen2-VL-72B and Gemini 1.5 Pro answer a shuffled two-video text prompt at temperature zero。For every property the authors choose the context size maximizing performance；pairwise and single-video settings use different useful surprise aggregation。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines include random untrained networks (`n=20`), VideoMAEv2 pixel-space prediction, Qwen2-VL-72B, Gemini 1.5 Pro, human IntPhys results and a prior structured method。V-JEPA has five seeds for the property analysis；the paper varies block/causal/random masking, K710/SSv2/HowTo/VideoMix2M data, unique-video fraction, frame fraction, ViT size, frame skip, context and aggregation。It lacks equal-objective/equal-data retraining for all baseline families, a held-out context-selection set for GRASP/InfLevel, action-conditioned comparison, long-horizon rollout, planning/control outcome and end-to-end cost study。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** V-JEPA B/L/H, BF16, A100 80GB, batch 3,072, 16 frames, 224×224, 5.33 fps and 90,000 iterations are disclosed。How many A100s, interconnect/topology, per-run wall time, total GPU-hours, memory peak, exact baseline hardware/precision, evaluation batch/concurrency, online latency/throughput and production SLO are Not Disclosed。The deployment unit is a short video window, not a request-serving contract。
- **What the Evidence Actually Proves:** on the disclosed frozen checkpoints, datasets and property-tuned surprise protocol, latent prediction yields above-chance pairwise discrimination across three benchmarks and significantly exceeds random networks for several object-permanence, continuity, shape, support, gravity and inertia slices。The study also shows that representation-space prediction remains useful under several masking strategies and that data distribution matters: fixed compute with 128 hours of unique HowTo video can still exceed chance on tested properties。
- **What It Does Not Prove:** it does not prove the model learned a complete human-like physics engine, causal laws, object-centric state or an actionable world model。It does not establish uniform competence in collision, solidity, color, contextualized gravity or long-horizon interaction；pixel prediction and MLLM baselines differ in objective, data, interface and evaluation channel。The 128-hour result holds compute near 30 years of processed video through repetition, so it is not a low-compute sample-efficiency claim。
- **Limitations / Threats to Validity:** the authors report near-chance categories for interaction-heavy properties, 3–4 second memory and no action conditioning。Per-property context is selected on the evaluated property because GRASP/InfLevel lack clean splits, inflating attainable-capability interpretation relative to a deployable fixed protocol。GRASP permits spurious cues；InfLevel needs unseen contextualization events；relabeling it makes impossible clips inherently harder and also raises untrained-network scores。Baseline modalities use incomparable decision interfaces, repository artifacts are not event-time pinned, and no independent reproduction is reported。
- **Trade-offs / New Failure Modes:** latent prediction filters nuisance detail and exposes cheap surprise, but hides which physical variable failed and can treat semantic novelty as violation。EMA targets stabilize learning while adding target-lag/state-version coupling。Short windows reduce compute but lose delayed context；property-specific context maximizes evidence of available information but weakens fixed-policy generalization。Observer-only prediction avoids action-model complexity yet cannot separate passive correlation from controllable transition；surprise thresholds can drift with camera, compression and scene distribution。
- **Where the Previous Design Still Applies:** explicit simulators remain appropriate for safety-critical planning and known dynamics；pixel models remain appropriate when reconstructable/renderable output is required；object-centric state remains useful for compositional intervention；MLLMs remain useful for instruction and explanation；task-specific calibrated classifiers remain appropriate for fixed decisions。V-JEPA-style latent surprise is an alternative representation-learning and probing branch, not a replacement for these designs。
- **Evolution Relationship:** `Direct Evolution` for `pixel reconstruction → learned latent prediction → surprise-based violation probe`；`Layering / Dependency` from multimodal representation and self-supervised pretraining into world-model evaluation；`Alternative Branch` versus hand-coded simulator, object-centric dynamics and text-mediated MLLM reasoning。The next pressure is persistent state, longer context, action-conditioned transition, causal intervention and closed-loop outcome evidence。
- **ROADMAP Node:** canonical owner `MULTIMODAL-WORLD-MODELS`（Current Ch25；Legacy N/A）；handoffs to `MULTIMODAL-REPRESENTATION`, `MULTIMODAL-GENERATIVE-PARADIGMS`, `MULTIMODAL-EMBODIED-VLA`, `TRAIN-DATA`, `TRAIN-PRETRAINING` and `PLATFORM-EVALUATION-SYSTEM`。World Models owns the distinction between observation prediction, action-conditioned transition and controllable state；Representation owns latent identity；Evaluation owns surprise protocol and evidence boundary。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch24 Generative Paradigms, Ch25 World Models, Ch26 Embodied AI/VLA and Ch66 Evaluation System。Ch25 already separates video generation, predictive environment model and controllable world model, and identifies pixels-versus-latent, persistent state and intervention outcome；this family refines the observation-only latent-prediction rung rather than creating a new owner。
- **Existing Coverage:** Ch25 already states that observational next-state prediction is not equivalent to action-conditioned dynamics and that visual plausibility is weaker than intervention outcome。The paper adds a concrete learned-latent middle branch between explicit simulator and pixel generation, plus an important evaluation lesson: context/window/surprise policy and benchmark cue structure determine what “physics understanding” means。Historical Books Gate remains closed, so this is a future refinement candidate only。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `MULTIMODAL-WORLD-MODELS`, with short handoffs to Representation, Pretraining and Evaluation。Future integration should preserve explicit simulator, pixel-generation, object-centric and action-conditioned branches and must not translate pairwise surprise accuracy into world-model planning capability。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, latent prediction/state flow, full training and evaluation contract, property/context limitations, official artifact boundary, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** immutable event-time code/data/checkpoint/run manifest；GPU count/topology/total compute；fixed-context and held-out calibration results；matched-data/objective baseline retraining；camera/compression/domain sensitivity；long-memory and contextualization evidence；action-conditioned prediction and intervention；object/state interpretability；surprise calibration under distribution drift；closed-loop planning/control outcomes；independent reproduction。

### Autellix: From Request-level Fairness to Program-attained Service and Workflow-visible Locality

- **Candidate / Week / Score:** Autellix: An Efficient Serving Engine for LLM Agents as General Programs / 2025-W08 / 28/30。
- **Source Family ID:** `autellix-program-aware-agent-serving`。
- **Source Type:** arXiv systems research paper describing a vLLM-based Python/CUDA/C++ prototype；no author code repository, release or artifact is linked or discoverable under the paper identity at review time。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 18:59:30 UTC and is the only arXiv version。All W08 mechanism and benchmark claims are therefore locked to v1；later third-party summaries are not evidence。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13965v1；https://arxiv.org/abs/2502.13965。
- **Related Primary Sources:** no official source-code, configuration bundle, trace release, container, model manifest or reproducibility artifact was found。The paper cites vLLM v0.6.1 as its implementation substrate, but the unpublished 5K-line patch—not upstream vLLM—owns PLAS/ATLAS, session tracking, multi-engine coordination and bulk-swap behavior。
- **Access and Verification Status:** paper verified；artifact unverified。The complete v1 system paper, algorithms, formulas, workload contract, implementation description, testbed, all end-to-end plots and ablations are accessible。Exact queue thresholds/quanta, anti-starvation beta, multi-step interval, overprovision policy, 2,048-token routing sensitivity, trace seeds, source patch and raw measurements are Not Disclosed。
- **Full-read Coverage:** read metadata, Introduction, serving/agent background, call/program wait-time motivation, prefix-locality analysis, architecture, process table, PLAS/ATLAS formulas, discretized preemption, anti-starvation, KV swap, multi-engine routing, implementation, all workload/testbed/baseline/results sections, offline/timing/optimal/swap ablations, Discussion, Conclusion and relevant references；searched for but did not locate an official artifact。
- **Original Problem:** request schedulers optimize TTFT/TPOT for isolated calls, but an Agent program issues a dynamic sequence or DAG of calls separated by tools/humans。A long program can repeatedly re-enter a high-priority request queue, delaying a short program even when call-level preemption works；routing each call independently also destroys within-program prefix locality。The true user-visible object is program completion, not one call。
- **Why the Previous Design Was Reasonable:** stateless request APIs isolate tenants and failures, interoperate across clients and keep the engine independent of business workflow semantics；FCFS is simple and predictable；MLFQ mitigates long-call head-of-line blocking without trusting client workflow metadata；round-robin/least-used balance replicas without sticky-state bookkeeping。These remain preferable for shallow independent calls, weak prefix reuse, untrusted clients or systems where session recovery correctness dominates workflow latency。
- **Changed Constraint:** workloads now contain 6–160+ dependent/parallel LLM calls with unknown future DAGs, long-tailed decode lengths and cumulative prompts。The scheduler needs just enough program/thread history to optimize the emergent critical path while remaining non-clairvoyant, and routing must trade queue balance against recomputing program-specific KV rather than treating all prompts as equivalent。
- **Mechanism:** a stateful frontend annotates each call with session/program/thread IDs；a global process table accumulates service, waiting, engine and activity state。PLAS gives a single-thread program's new call the sum of completed call service；ATLAS approximates a dynamic DAG's attained critical path by propagating the maximum parent priority plus runtime。Priorities map into finite queues with quanta, demotion and wait/service-ratio promotion。Preemption uses multi-step scheduling and contiguous GPU↔CPU KV transfer；routing balances calls <=2,048 tokens and pins longer calls to the program's engine。
- **State Ownership:** orchestrator owns actual workflow, tool/action semantics and termination；frontend/session registry owns program/thread identity；process table owns attained service, wait, last activity and engine affinity；engine queue owns discretized priority/quanta；KV manager owns resident/swapped blocks；load balancer owns selected engine and threshold policy；meta-engine IPC owns request/future/result correlation；evaluation trace owns arrival and call graph。Scheduler hints do not authorize tools or rewrite workflow state。
- **Control Flow / Data Flow:** `local dynamic program → start_session → call tagged with program/thread → process-table priority lookup → priority queue/admission → token iterations → optional KV bulk swap/preemption → completion updates attained service → tool/human interrupt → next call`；multi-engine path adds `length/locality classification → least-used or sticky engine → IPC future → replica result → frontend`；end_session deletes table state。
- **Implementation Details:** the prototype adds about 5K lines of Python and CUDA/C++ over vLLM v0.6.1。Its frontend extends OpenAI Chat Completion/vLLM Python interfaces；the custom scheduler implements PLAS, ATLAS and MLFQ；the swap kernel gathers blocks into a contiguous host buffer for one transfer。Each engine replica is a Python process coordinated through `mp.Queue`/`mp.Pipe` by an asynchronous meta-engine。The frontend trusts a locally imported package and explicitly lacks protection against user modification。
- **Evaluation Contract:** complete ShareGPT conversations average 6.66 calls (max 80；256 prefill/277 decode tokens)；BFCLv3 averages 10.75 calls (max 70；735.06/34.14 tokens)；LATS/HotpotQA MCTS averages 159.7 calls (467.2/72.6 tokens)；Mixed samples the three equally。Programs arrive by a synthetic Poisson process。Program token latency is response time divided by generated tokens；for multi-thread programs it is critical-path response time divided by tokens across all threads。Throughput is programs/s at matched values of this metric。
- **Baselines / Ablations / Sensitivity / Overhead:** single-engine baselines are vLLM 0.6.1 FCFS, `vLLM-opt` with chunked prefill/prefix cache/multi-step scheduling and MLFQ atop that stack；all use the same max batch size。Multi-engine baselines are Round Robin and Least Used under the same PLAS/ATLAS scheduler。Ablations cover offline makespan, timing, clairvoyant SRPT simulation and swap kernel。No published sensitivity covers queue boundaries/quanta, beta, routing threshold, multi-step interval, workload mix, prefix mutation, session churn or scheduler-state failure。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** LLaMA-3.1-8B/70B and Falcon-180B use 1/4/8 A100-SXM4-80GB GPUs on one GCP a2-ultragpu-8g with NVLink, 1,360GB host memory, PCIe 4.0×16 and 2TB disk；multi-engine uses four 8B or two 70B replicas。Input/output/call distributions are disclosed per workload。Precision, tensor-parallel layout details, max batch value, KV block size, swap-space policy except one >1.2TB failure, networked multi-node behavior, exact SLO points and trace confidence intervals are Not Disclosed。
- **What the Evidence Actually Proves:** under the disclosed single-node A100 replay, program-aware attained-service scheduling improves the measured program-throughput/latency frontier over the three configured request-level baselines；the largest reported gains occur for heterogeneous mixed traces。Data-locality-aware routing improves over RR/Least Used under identical program scheduling, and the bulk-transfer/multi-step path reduces observed swap cost。The SRPT simulation also shows Autellix remains below a clairvoyant bound。
- **What It Does Not Prove:** the study does not prove 4–15× gains over current vLLM/SGLang/TensorRT-LLM, arbitrary real Agent traffic, multi-node fleets or tool-heavy wall-clock latency。External interrupt time is excluded even though it can dominate workflow completion。Program-token latency is nonstandard and, for parallel programs, divides critical-path time by tokens from all threads, so extra non-critical tokens can improve the metric without improving user outcome。It does not prove correctness, quality, fault tolerance, tenant isolation or safe client metadata。
- **Limitations / Threats to Validity:** no runnable artifact or raw traces are available；results use replayed/synthesized Poisson arrivals on one 8-GPU host。The 2,048-token locality rule and >90% within-program cache-hit observation are workload-specific。A mutable client can forge identity；process-table deletion, crash recovery, orphan sessions, retries and duplicate calls are unspecified。PLAS Equation 1 prints `c_k.id=c_i.id` while describing `c_j`, an apparent index typo；ATLAS avoids explicit dependency tracking despite critical-path language。No statistical uncertainty or adversarial fairness study is reported。
- **Trade-offs / New Failure Modes:** attained service reduces short-program blocking but can deprioritize legitimately long workflows；anti-starvation improves tail fairness while reintroducing interference。Preemption opens batching opportunities but increases active state, scheduler work and KV swap pressure；bulk transfers reduce fragmentation but require host buffer capacity and synchronization。Sticky locality saves prefill recompute but creates hotspots and stale affinity。Stateful sessions enable optimization but introduce spoofing, leakage, orphan cleanup, failover and exactly-once correlation problems。
- **Where the Previous Design Still Applies:** FCFS remains useful at low load or homogeneous calls；request-level MLFQ works when each request is the user-visible job；stateless APIs are safer for untrusted/multi-provider boundaries；RR/least-used work when prefixes are small or transport/recompute cheap；explicit DAG schedulers/compiler plans fit stable known workflows；clairvoyant estimates can outperform attained-service policies when reliable duration prediction exists。
- **Evolution Relationship:** `Direct Evolution` for `request FCFS → request MLFQ → program attained service → approximate dynamic critical-path service`；`Layering / Dependency` with KV swap/prefix locality and Agent workflow identity；`Alternative Branch` between stateless isolation, explicit DAG planning and non-clairvoyant stateful scheduling。The next pressure is durable/fenced session identity, failure semantics, online SLO calibration and joint tool/LLM critical-path scheduling。
- **ROADMAP Node:** canonical owner `INFER-SCHEDULING`（Current Ch56；Legacy Ch52）；handoffs to `INFER-KV-CACHE`, `INFER-SGLANG`, `INFER-DYNAMO`, `PLATFORM-GATEWAY`, `PLATFORM-EVALUATION-SYSTEM` and `AGENT-WORKFLOW`。Scheduling owns priority/preemption/fairness/locality decisions；Workflow owns business DAG and action state；Gateway owns trusted identity/routing boundary；KV chapter owns swap/reuse semantics。
- **Target and Adjacent Chapters Read:** read Ch45 KV Cache, Ch50 vLLM, Ch51 SGLang, Ch52 Dynamo, Ch55 PD Disaggregation, Ch56 Inference Scheduling, Ch62 Gateway, Ch66 Evaluation and Ch81 Workflow。Ch56 already owns multi-timescale scheduling, starvation and preemption/KV coupling；Ch81 already states that workflow visibility can improve serving without transferring business-state authority。Autellix supplies a concrete program-attained-service branch rather than a new chapter。
- **Existing Coverage:** current Books already progress from request/token scheduling to workflow-visible critical paths and explicitly separate orchestrator state from engine hints。Autellix adds PLAS/ATLAS, wait/service anti-starvation and locality-threshold state, while exposing the durability/security debt of a stateful frontend。This is meaningful refinement evidence, but Historical Books Gate remains closed and no paper result is copied into Books now。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `INFER-SCHEDULING`, with a short ownership handoff in `AGENT-WORKFLOW` and identity/failover handoff to Gateway。Future integration must retain stateless/FCFS/MLFQ/explicit-DAG alternatives and bind every performance claim to the vLLM 0.6.1, A100, replay and program-token-latency contract。
- **Changed Files or Rejection Reason:** added the v1-locked 30-field Source Review, request→program scheduling evolution, PLAS/ATLAS/state/preemption/locality flow, full workload/testbed metric contract, missing-artifact and formula/metric caveats, Stable Node mapping and deferred Books disposition；no Books change。
- **Open Questions:** official event-time code/commit/container and raw traces；queue thresholds/quanta/beta/multi-step and 2,048-token sensitivity；program-token-latency denominator audit；session authentication/fencing/TTL/failover/retry semantics；cross-tenant KV isolation；multi-node/network tests；real tool-latency traces；arrival burst/drift and fairness curves；modern baseline replication；quality/outcome-aware scheduling and independent reproduction。

### Sailor2: From Monolingual Replay to Versioned Multilingual Data and Training Contracts

- **Candidate / Week / Score:** Sailor2: Sailing in South-East Asia with Inclusive Multilingual LLMs / 2025-W08 / 28/30。
- **Source Family ID:** `sailor2-multilingual-continual-pretraining`。
- **Source Type:** arXiv technical report + earlier Sea AI Lab official release Blog + author repositories for data cleaning, mixture optimization, pretraining, post-training and evaluation + Hugging Face model artifacts。
- **First-public Date / Revision History:** the Sailor2 model family and roughly 500B-token claim were announced on 2024-12-03；arXiv v1 was submitted 2025-02-18 16:04:57 UTC and remains the only paper version。W08 owns the first public technical report, not the model-release event；the earlier Blog is predecessor evidence in the same Source Family, while mutable repository/model-card changes after W08 are supporting lineage only。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12982v1；https://arxiv.org/abs/2502.12982；https://sail.sea.com/blog/articles/55；https://github.com/sail-sg/sailor2；https://huggingface.co/sail/Sailor2-20B。
- **Related Primary Sources:** https://github.com/sail-sg/sailcraft implements the cleaning pipeline；https://github.com/sail-sg/regmix exposes mixture-search code；https://github.com/sail-sg/Megatron-Sailor2, https://github.com/sail-sg/oat, https://github.com/sail-sg/sailcompass and https://github.com/sail-sg/SEA-WildBench expose current training/alignment/evaluation lineage。None is an immutable bundle pinning every W08 run, dataset, checkpoint and dependency。
- **Access and Verification Status:** paper, official release, current code lineage and model weights verified；event-time end-to-end reproduction remains unverified。The main Sailor2 repository is mostly a release index, its linked components evolve independently and the 20B model card has a mutable commit history；hardware topology, precision, full optimizer state, immutable data manifests and raw runs are Not Disclosed。
- **Full-read Coverage:** read metadata and release chronology；Introduction/Related Work；all data sourcing, synthetic-data, cleaning and RegMix sections；model expansion, Zero-Bubble Pipeline Parallelism, vocabulary balancing, intra-document masking and two-stage CPT；SFT construction/selection, off-policy→on-policy preference tuning and ablations；long-context, speculative-decoding and pruning customizations；base/chat/translation/culture evaluations；analysis, future work and relevant appendices；inspected linked official repositories and 20B model artifacts。
- **Original Problem:** adapting a strong English/Chinese base model to many Southeast Asian languages is not solved by adding translated samples once。Low-resource corpora differ by orders of magnitude, web quality and tokenizer efficiency vary by language, continued training can overwrite existing capability, alignment reward models are mostly English-centric, and large vocabularies create pipeline imbalance。The system must jointly control data identity, mixture, parameter plasticity, training stages and evaluation slices。
- **Why the Previous Design Was Reasonable:** training from scratch gives full tokenizer/data/control ownership but is prohibitively expensive；uniform sampling is simple and preserves observed corpus frequencies；direct continual pretraining reuses mature base capability；single-stage SFT/DPO minimizes pipeline state；ordinary pipeline partitioning and unmodified draft models reduce implementation risk。These remain rational when languages have adequate balanced data, the base is not over-trained, forgetting is acceptable, or operational simplicity matters more than low-resource tail coverage。
- **Changed Constraint:** six target languages have fewer than 1B raw tokens and some have fewer than 1M；Qwen2.5 has already consumed 18T tokens, reducing plasticity；English/Chinese retention and thirteen SEA-language improvement must coexist；translated instructions are imbalanced across both language and domain；large vocabulary layers can equal roughly four transformer layers and interact badly with delayed weight-gradient computation。
- **Mechanism:** the pipeline constructs language-labelled raw, replay, translation and instruction corpora；SailCraft applies rule/model filtering and exact/near/URL/frequent-line deduplication；1,000 one-million-parameter RegMix proxy runs optimize stage-1 language weights；block expansion enlarges Qwen2.5 0.5B/7B/14B into 1B/8B/20B before CPT；stage 1 trains a broad 450B-token mixture, then stage 2 anneals on 60B effective tokens dominated by high-quality SEA subsets plus replay/instructions。Post-training follows broad SFT → balanced high-reward/high-perplexity SFT → off-policy DPO → on-policy DPO/distillation with a language-consistency verifier；long-context, speculative decoding and pruning are optional downstream branches。
- **State Ownership:** source manifests own URL/document/language/license/provenance identity；cleaning stages own retention and duplicate equivalence；tokenizer owns token accounting；mixture controller owns sample weights and proxy-objective assumptions；base/expanded checkpoints own capability lineage；trainer owns stage, optimizer and batch state；SFT/preference pipelines own prompts, translations, reward/perplexity labels and chosen/rejected pairs；verifier owns language-match policy；evaluation harness owns task translations, judge versions and scoring；registry/model card owns released artifact identity, not hidden training facts。
- **Control Flow / Data Flow:** `public web/PDF/replay/translation sources → language identification and layered filtering → raw per-language token ledger → proxy-mixture search → block-expanded base checkpoint → broad stage-1 CPT → high-quality/replay stage-2 annealing → broad SFT → balanced SFT → off-policy preference bootstrap → on-policy preference/distillation → optional long-context/speculative/pruned variants → slice-aware evaluation → versioned release`。Every arrow changes evidence and artifact identity；a model filename alone cannot reconstruct the path。
- **Implementation Details:** CPT uses Megatron-LM with ZB-H1, splitting input- and weight-gradient work, and redistributes transformer layers away from the last pipeline stage to compensate for vocabulary-layer FLOPs/memory；packed samples call `flash_attn_varlen` with document lengths to block cross-document attention。Stage 1 uses learning rate `1e-4` and global batch 1,024；stage 2 uses `1e-5` and batch 4,096。SFT uses 4.8M examples, then a balanced three-epoch subset selected by within-language/category reward and perplexity percentiles plus embedding deduplication。The paper selects LR-DPO after DPO/SimPO/LN-DPO/LR-DPO tuning, while the linked repositories expose current, not paper-pinned, implementations。
- **Evaluation Contract:** base models are compared on SailCompass, FLoRes-200 and language-specific QA/classification/translation suites；chat models use GPT-4o-0806-translated SEA-WildBench across eight languages, with GPT-4o-0806 simultaneously serving as reference opponent and judge。Cultural tests use 3-shot prompts and include translated CulturalBench plus regional datasets。Long-context variants train on 4B tokens for 1,000 steps and report RULER plus short-task/perplexity checks；CPT ablation post-trains vanilla Qwen2.5-7B and Sailor2-8B using the same downstream pipeline。This is an offline research contract, not a production latency/cost/safety SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons cover Qwen2.5/Qwen1.5→Sailor/Sailor2, same-post-training CPT ablation, multiple multilingual base/chat models, off-policy then on-policy preference stages, language-consistency verification, teacher distillation, long-context before/after and structured pruning。The report does not isolate block expansion from changed base model/data at equal compute, does not publish multi-seed uncertainty, full mixture-objective sensitivity, translation-quality human agreement, equal-token multilingual alternatives, ZB-H1 throughput/overhead numbers or end-to-end cost/energy accounting。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models are 1B/8B/20B expanded from Qwen2.5 0.5B/7B/14B；CPT effective-token tables disclose 450B + 60B, SFT batch 4,096 then 512, CPT batches 1,024/4,096, and optional context extensions to 32K/128K。GPU type/count, topology, precision, sequence length for main CPT, optimizer/betas, parallel degrees, wall time, peak memory, training FLOPs/energy, serving batch/concurrency/throughput/tail latency and production SLO are Not Disclosed。The current 20B weight tree is about 38.4GB but is not a training-memory or runtime claim。
- **What the Evidence Actually Proves:** within the disclosed author pipeline, language-aware cleaning/mixture plus two-stage CPT materially changes perplexity and downstream results for evaluated SEA languages, and same-post-training comparison supports a CPT contribution for Khmer/Lao under SEA-WildBench。The report also demonstrates executable system couplings: large vocabulary can unbalance pipeline stages；document boundaries change packed attention semantics；English-centric reward scoring needs an independent language-consistency constraint；post-training sequence matters for this model family。It provides public weights and component code lineage sufficient for inspection, not full reproduction。
- **What It Does Not Prove:** it does not prove block expansion alone prevents forgetting, that RegMix's one-million-parameter optimum transfers universally, that translated/synthetic data preserve cultural meaning, or that Sailor2 has GPT-4o-equivalent general capability。The SWB result uses the same GPT-4o version for translation, opponent and judging and may overestimate parse-error cases；perplexity and benchmark gains do not prove fairness, safety or production fitness。The abstract/release `400B SEA + 100B replay ≈500B` framing is not identical to the detailed 450B + 60B effective-token tables, so 500B and 510B are retained as differing accounting views rather than silently merged。
- **Limitations / Threats to Validity:** a December 2024 release precedes the February report, while current code/model cards are mutable and lack one signed event-time manifest。Most data is public web/PDF or machine translation, but exact source/license/consent/retention manifests are incomplete；quality classifiers are trained from translated positives and random CommonCrawl negatives；reward/judge models impose English-centric and shared-model bias。Hardware and total compute are absent, no multi-seed confidence is reported, low-resource slices are small, benchmark translations may alter difficulty and official artifacts do not reproduce the complete training graph from one commit。
- **Trade-offs / New Failure Modes:** replay preserves existing languages but consumes budget and may retain unwanted behavior；upsampling improves tail exposure but increases repetition/overfitting；synthetic translation adds coverage while importing translationese and teacher bias；block expansion creates plasticity but raises compute, memory and serving cost；two-stage curricula improve focus while introducing stage-order and checkpoint provenance debt；ZB-H1 reduces bubbles but lengthens activation lifetime near a large vocabulary head；language verification prevents obvious mismatch but can misclassify code-switching；shared judge/reference models create correlated evaluation error。
- **Where the Previous Design Still Applies:** from-scratch training remains suitable when tokenizer, data rights and architecture must be fully controlled；fixed natural-frequency sampling is defensible when deployment traffic follows it；no expansion is preferable when base plasticity is sufficient and deployment cost is constrained；single-stage CPT/SFT is easier to reproduce for balanced corpora；human regional evaluation is preferable for culturally sensitive decisions；standard decoder serving remains appropriate when the optional speculative draft lacks a verified workload advantage。
- **Evolution Relationship:** `Direct Evolution` for `uniform multilingual corpus → quality/language-aware mixture → broad CPT → high-quality annealing` and `single-stage alignment → broad SFT → balanced SFT → off-policy bootstrap → on-policy preference`；`Layering / Dependency` from tokenizer/data identity into training and evaluation；`Alternative Branch` between replay, model expansion, parameter-selective adaptation and training from scratch。The next pressure is immutable data lineage, culturally grounded evaluators, plasticity-aware base selection and cost-constrained multilingual serving。
- **ROADMAP Node:** canonical owner `TRAIN-DATA`（Current Ch27；Legacy Ch23）；handoffs to `TRAIN-PRETRAINING`, `TRAIN-SFT`, `TRAIN-DPO`, `TRAIN-DISTRIBUTED-TRAINING`, `MODEL-TOKENIZER`, `MODEL-LONG-CONTEXT`, `INFER-SPECULATIVE-DECODING` and `PLATFORM-EVALUATION-SYSTEM`。Data owns corpus identity, language/domain mixture and filtering contract；Pretraining owns checkpoint/plasticity/stage semantics；other nodes own their local mechanisms。
- **Target and Adjacent Chapters Read:** read Ch11 Tokenizer, Ch22 Long Context, Ch27 Data, Ch28 Pretraining, Ch29 SFT, Ch34 DPO, Ch36 Distributed Training, Ch48 Speculative Decoding and Ch66 Evaluation System。Ch27 already owns lineage, quality, mixture and synthetic-data risk；Ch28 owns continued training and forgetting；Ch29/34 own stage-specific supervision；Ch36 owns pipeline state；Ch48 owns exact verification；Ch66 owns translated benchmark and judge identity。
- **Existing Coverage:** current Books already separate data quantity from quality, synthetic-data provenance from capability claims, continued pretraining from post-training, and benchmark evidence from production truth。Sailor2 adds a coherent multilingual evolution chain and exposes cross-layer couplings among token accounting, mixture search, plasticity, pipeline partition, reward-language mismatch and translated evaluation。It is therefore a meaningful future refinement family, but not a reason to create a new owner or copy the report into multiple chapters。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DATA`, with short handoffs to Pretraining, SFT/DPO, Distributed Training, Long Context, Speculative Decoding and Evaluation。Historical Books Gate remains closed；future integration must preserve from-scratch/uniform/single-stage alternatives and must not write 500B, SWB or RULER results without their source and workload contracts。
- **Changed Files or Rejection Reason:** added the non-template 30-field, v1-locked Source Review；separated the 2024 model release from the 2025 technical-report event；reconstructed data→CPT→alignment→customization flow；recorded 500B/510B accounting, translated-judge and mutable-artifact limits；mapped one canonical Stable Node and deferred Books disposition；no Books change。
- **Open Questions:** immutable event-time source/data/license/checkpoint/container/run manifests；reconciliation of 500B headline and 510B detailed effective-token tables；exact tokenizer efficiency by language；GPU/precision/parallel/optimizer/compute/energy contract；RegMix transfer and mixture sensitivity；block-expansion equal-base/equal-data ablation；translation/cultural human agreement；reward/judge calibration and language-verifier code-switch behavior；multi-seed uncertainty；safety/fairness/privacy slices；speculative-decoding acceptance/latency contract；independent end-to-end reproduction。

### Thinking Preference Optimization: From Repeated Long-CoT SFT to Length-confounded Pairwise Preference

- **Candidate / Week / Score:** Thinking Preference Optimization / 2025-W08 / 24/30。
- **Source Family ID:** `thinkpo-length-preference-optimization`。
- **Source Type:** arXiv research paper + official author repository + released dataset/model artifacts referenced by the repository。
- **First-public Date / Revision History:** arXiv v1 was submitted 2025-02-17 19:56:21 UTC and remains the only paper version。The repository README says the paper was released on 2025-02-19, but arXiv metadata is the event-time authority；repository model releases on 2025-02-21 and dataset release on 2025-02-22 are artifact nodes in the same W08 Source Family, not separate scored events。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13173v1；https://arxiv.org/abs/2502.13173；https://github.com/uservan/ThinkPO。
- **Related Primary Sources:** the official repository links its ThinkPO dataset and four trained model artifacts and exposes current SFT/DPO/evaluation scripts。The repository has no release/tag or paper-pinned immutable W08 digest, so current code and artifacts establish lineage and inspectability rather than exact event-time reproduction。
- **Access and Verification Status:** v1 full text, metadata, appendices, current repository, training/evaluation entry points and artifact-release chronology verified；exact event-time code, dependency/container lock, dataset/checkpoint digests, raw runs and hardware contract remain unverified。No later arXiv revision exists。
- **Full-read Coverage:** read metadata, Abstract, Introduction, Motivation, two-stage training and data-curation method, all main tables, cross-model experiments, length-gap and data-composition ablations, Related Work, Conclusion, Limitations and appendices covering temperature sensitivity, additional datasets, training recipes and qualitative examples；inspected official repository quick-start, SFT/DPO commands, evaluation paths and release chronology。
- **Original Problem:** repeated SFT on a fixed long-chain-of-thought corpus can plateau, while collecting fresh high-quality long responses is expensive。The question is whether an already SFT-tuned policy can reuse the same long responses as preference winners and cheaply generated short responses as losers to create another learning signal。
- **Why the Previous Design Was Reasonable:** SFT offers stable token-level imitation, preserves a clear target response and avoids preference-pair construction；ordinary DPO uses explicit quality preferences rather than output length；online verifier/RL methods explore new trajectories and can optimize correctness directly。These remain preferable when concise answers are valuable, length is a poor quality proxy, pair quality cannot be controlled, or an executable verifier is available。
- **Changed Constraint:** the long-answer corpus already exists, additional long-answer generation is costly, and the SFT checkpoint still produces substantially shorter outputs than its DeepSeek-R1-derived teacher traces。The authors therefore treat response-length contrast as a low-cost weak preference signal after SFT rather than acquiring a new judged preference dataset。
- **Mechanism:** stage 1 SFT imitates about 17K Bespoke-Stratos long responses generated by DeepSeek R1 and filtered with GPT-4o-mini；stage 2 pairs each retained long response as `chosen` with a shorter Qwen2.5-Math-7B-Instruct response as `rejected`, then applies standard DPO against the SFT reference。The pair set contains 8,080 answer-match examples plus 2,000 examples where answers differ but satisfy the authors' correctness/format filtering。The objective does not identify reasoning quality separately from length, teacher identity, style, correctness and source-model differences。
- **State Ownership:** prompt and reference-answer records own task identity；DeepSeek-R1/Bespoke-Stratos lineage owns long-response generation；GPT-4o-mini and rule filters own acceptance decisions；Qwen2.5-Math-7B-Instruct owns short-response generation；the pair builder owns chosen/rejected and length-gap identity；SFT checkpoint/reference and DPO policy own model lineage；evaluation harness owns decoding temperature, answer extraction and benchmark scoring。None of those proxy owners becomes ground-truth reasoning authority。
- **Control Flow / Data Flow:** `math prompt/reference → long teacher response → correctness/format filter → SFT checkpoint → short student response → answer/format comparison → long/short preference pair → DPO update relative to SFT policy → sampled answer extraction → benchmark score and output-length analysis`。Because length, generator and response quality change together at pair construction, downstream correlation cannot isolate a causal “longer reasoning” variable。
- **Implementation Details:** repository commands use DeepSpeed ZeRO-3 for SFT and DPO；paper appendix reports DPO batch 48 and beta 0.01 for all models, with learning rates `1e-7` for DeepSeek-R1-Distill-Qwen-7B, `5e-7` for Bespoke-Stratos-7B, `3e-7` for the reproduced Bespoke-Stratos model, and `5e-7`/`8e-8`/`1e-7` for Qwen2.5 3B/7B/14B。Current scripts/data/models are mutable and do not pin the exact paper environment or all run seeds。
- **Evaluation Contract:** models are evaluated on MATH500, AIME 2024, GPQA-Diamond, GSM8K and OlympiadBench Math using sampling temperature 0.7；appendix repeats selected comparisons at 0.1 and 0.5。The paper reports accuracy and average generated length, including an AIME slice of only 30 questions。It does not report user latency, token cost, throughput, concurrency, energy or production SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include original and ThinkPO-tuned DeepSeek-R1-Distill-Qwen-7B, Bespoke-Stratos-7B, a reproduced Bespoke-Stratos checkpoint and Qwen2.5 3B/7B/14B；temperature sensitivity and 1K-example pair subsets with average length gaps 621, 1,525 and 4,758 tokens are tested。The smallest gap gives the best aggregate result in that ablation, while larger gaps can hurt。There is no equal-quality length-only intervention, equal-generated-token/equal-compute baseline, multi-seed confidence, judge-independent reasoning validation or end-to-end cost comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes are 3B, 7B and 14B；DPO batch is 48 and beta is 0.01；the authors' reproduced model reports average output length 9,117 before and 11,040 after ThinkPO at temperature 0.7。GPU type/count/topology, precision, maximum sequence length, gradient accumulation, optimizer details beyond learning rate, wall time, memory, FLOPs, energy, inference batch/concurrency and latency/SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' five mostly math/reasoning benchmarks and disclosed model recipes, an additional DPO stage constructed from long-as-chosen and short-as-rejected pairs usually increases output length and improves some aggregate accuracy results。For the reproduced model the reported average accuracy changes from 55.3 to 57.4 and average length from 9,117 to 11,040；the length-gap ablation shows pair construction matters and that a larger contrast is not monotonically better。
- **What It Does Not Prove:** it does not prove that length causes correct reasoning, that generated chain of thought is faithful, that repeated preference stages continually improve indefinitely, or that the method is compute/cost efficient。Several slices regress: the reproduced model's GSM8K score falls 93.9→93.0；DeepSeek 7B AIME falls 56.7→43.3；Bespoke MATH500 falls 84.0→82.8；Qwen 7B AIME and Qwen 14B GPQA also fall。Aggregate author results therefore cannot be promoted to a universal “think longer” rule。
- **Limitations / Threats to Validity:** the paper itself notes DPO sensitivity to beta and learning rate。In addition, length is confounded with teacher/model identity, style and correctness；there is no length-matched or equal-quality causal control, no multi-seed uncertainty, AIME is small, the domain mix is math-heavy, artifact identity is mutable and hardware/runtime cost is absent。Counting words such as “wait” or “hmm” is a style proxy, not faithful-process evidence；temperature replications do not replace independent run variance。
- **Trade-offs / New Failure Modes:** reusing long responses and cheaply generating short rejects reduces new data cost and can escape a fixed-SFT plateau；it also purchases more generated tokens, latency and truncation exposure, can reward verbosity or stylistic markers, may suppress concise correct answers and can regress individual tasks。Large length gaps may make the preference trivially separable and reduce useful quality learning；incorrect or source-correlated pairs can amplify teacher/filter bias。
- **Where the Previous Design Still Applies:** SFT remains the clean branch for behavior imitation；quality-labelled or correctness-filtered DPO is preferable when pair semantics can be observed；length-regularized DPO can preserve concision；online verifier/RL is preferable when exploration and executable correctness are available；direct concise decoding remains better for latency/cost-constrained workloads。ThinkPO is a post-SFT alternative branch, not a replacement for these designs。
- **Evolution Relationship:** `Direct Evolution` for `fixed long-CoT SFT → another preference stage reusing the same long responses`；`Alternative Branch` versus correctness-labelled DPO, length-regularized preference optimization and online verifier/RL；`Principle Reuse` of weak proxy supervision。The next pressure is to disentangle response quality from length and price accuracy gains against generated-token and latency budgets。
- **ROADMAP Node:** canonical owner `TRAIN-DPO`（Current Ch34；Legacy Ch30）；handoffs to `TRAIN-SFT`, `MODEL-SAMPLING` and `PLATFORM-EVALUATION-SYSTEM`。DPO owns pair/reference/objective semantics；SFT owns the predecessor imitation checkpoint；Sampling owns decoding length/temperature behavior；Evaluation owns task, answer extraction, uncertainty and cost-aware evidence。
- **Target and Adjacent Chapters Read:** read Ch29 SFT, Ch33 GRPO, Ch34 DPO, Ch35 Checkpoint and Ch66 Evaluation System, with sampling handoff checked in Ch20。Ch34 already explains sequence-length effects in log-ratio objectives and the risk of learning length/style/format shortcuts；Ch29 already requires separating correctness, format, output length and task latency；Ch66 already rejects proxy/judge scores as production truth。
- **Existing Coverage:** current Books already contain the core warning that pair construction and length distribution change DPO's learned signal。ThinkPO adds a useful bounded counterexample: even inside the authors' own protocol, larger chosen/rejected length gaps are not monotonically better and task slices can regress。It is therefore a future refinement candidate for the pair-construction trade-off, not a new mechanism owner and not evidence for “longer is better”。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DPO`。Historical Books Gate remains closed；future integration, if any, should use this only as a bounded empirical case for length confounding and retain SFT, correctness-labelled DPO, length regularization, verifier/RL and concise-decoding branches。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；corrected first-public date from discovery/repository wording to arXiv 2025-02-17；separated paper and artifact-release nodes；reconstructed pair-building and evaluation contracts；recorded negative slices and length-gap non-monotonicity；mapped one canonical Stable Node；no Books change。
- **Open Questions:** immutable W08 commit/data/checkpoint/container/run manifests；exact pair-filter code and counts by match/correctness class；equal-quality length-only intervention；teacher/source/style confound；length-regularized and equal-token/equal-compute baselines；multi-seed confidence；AIME small-sample uncertainty；non-math and multilingual transfer；faithful-process validation；truncation/verbosity/user-preference effects；hardware/precision/compute/energy；latency/cost/SLO and independent reproduction。

### HermesFlow: Homologous Multimodal Preference Loops with a Disputed Coupled Objective

- **Candidate / Week / Score:** HermesFlow: Seamlessly Closing the Gap in Multimodal Understanding and Generation / 2025-W08 / 24/30。
- **Source Family ID:** `hermesflow-homologous-multimodal-pairdpo`。
- **Source Type:** arXiv research paper + official implementation/data/checkpoint repository + Hugging Face checkpoint artifact + later NeurIPS revision lineage。
- **First-public Date / Revision History:** arXiv v1 was submitted 2025-02-17 18:57:51 UTC；v2 was submitted 2025-09-25 and records NeurIPS 2025 lineage。W08 is locked to v1；the 2025-02-18 checkpoint and February code release are artifact nodes in the same family, while v2/current repository changes are later supporting lineage and cannot replace v1 claims。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12148v1；https://arxiv.org/abs/2502.12148；https://github.com/Gen-Verse/HermesFlow；https://huggingface.co/Gen-Verse/HermesFlow。
- **Related Primary Sources:** Show-o supplies the 1.3B unified understanding/generation base；JourneyDB supplies the 5,000 homologous image-caption pairs；TIFA supplies generated question-answer probes。The current repository exposes curation, VQA, image generation, Pair-DPO training and iterative-update paths, but no release/tag or signed W08 commit/container/run manifest。
- **Access and Verification Status:** v1 full text, formulas, experiments, ablations, appendices, repository workflow and checkpoint identity verified；exact event-time source digest, raw runs, data/checkpoint hashes and line-level agreement between current training code and v1 objective remain unverified。The paper's central objective derivation is internally inconsistent, so the family is `Disputed` rather than merely `Experimental`。
- **Full-read Coverage:** read metadata/revision history, Abstract, Introduction, Related Work, next-token/DPO preliminaries, complete preference-data curation, Pair-DPO and self-play method, algorithm, all understanding/generation/gap tables, training/evaluation setup, user study, DPO/Pair-DPO/iteration/sample-richness ablations, Conclusion/limitations and formula/data appendices；inspected official repository installation, data schema, inference/VQA, pair construction, training and iterative-update workflow plus checkpoint card。
- **Original Problem:** a unified multimodal model can share one backbone while understanding and generation improve at different rates。Separate DPO pipelines optimize captions or images independently and do not express that both outputs originate from the same image-caption pair。The system question is whether shared semantic identity can couple two preference loops without acquiring external ranked data。
- **Why the Previous Design Was Reasonable:** independent understanding and generation objectives are easy to debug and allow each modality to use its best verifier；more supervised data can improve either side without self-generated label feedback；external human/judge preferences reduce same-model correlation。These remain rational when capability owners differ, proxy reliability is asymmetric, generation cannot be faithfully self-scored, or failure isolation matters more than cross-task coupling。
- **Changed Constraint:** the Show-o-style backbone already supports image→text and text→image, but high-quality paired preference labels are costly and the authors observe a larger generation deficit under their proposed measurement。The same 5,000 image-caption pairs can seed both directions, enabling a self-generated preference loop with common semantic identity。
- **Mechanism:** for each image, the model samples captions and ranks them by BERT similarity to the original caption；for each prompt, it samples images, generates TIFA/JourneyDB questions and ranks images by the same model's VQA accuracy, retaining generation winners only when the top score exceeds 0.6。Each record contains understanding and generation chosen/rejected pairs。Pair-DPO couples their two policy/reference preference margins, then regenerates candidates after each round and updates winners/losers against previous-round samples。
- **State Ownership:** homologous record owns image-caption identity；sampler owns candidate set and random seed；BERT scorer owns caption lexical/semantic proxy；TIFA/JourneyDB own QA probes and answers；the same MLLM owns both generation and self-VQA responses；pair builder owns thresholds, winner/loser and round lineage；policy/reference checkpoints own log-probability margins；evaluation harness/GPT-4o/user study own separate result evidence。No self-score becomes ground-truth perception or image quality。
- **Control Flow / Data Flow:** `JourneyDB image-caption pair → sample n captions and n images → BERT caption ranking + TIFA/JourneyDB self-VQA image ranking → homologous six-output preference record → policy/reference margins for both directions → Pair-DPO update → regenerate candidates → compare with previous winners/losers → next-round update → independent benchmark and user-study evidence`。Each iteration changes policy, data distribution and scorer behavior together, so round identity is part of the artifact contract。
- **Implementation Details:** the paper trains Show-o 1.3B for 3,000 steps with caption and generation batch 4, AdamW, weight decay 0.01, initial learning rate `2e-5`, cosine schedule and beta 0.2。Repository workflow uses 512×512 demo configuration, 50 image-generation steps and guidance scale 5 for curation, stores BERT/VQA scores in `pair_dpo_data.json`, launches `training/train_pairdpo.py`, and rewrites the same preference-data path for iterative rounds。Current README examples include a one-GPU launcher and do not pin the paper's eight-GPU run or all random seeds。
- **Evaluation Contract:** understanding uses POPE, MME, Flickr30k, VQAv2, GQA and MMMU；generation uses GenEval, DPG-Bench, MSCOCO-30K FID/CLIP-Score and a 35-user, 25-prompts-per-comparison study reporting 3,500 votes。The custom “gap” evaluates model answers for original images but asks GPT-4o to answer questions about generated images, then subtracts averages on those different evaluator paths。It is a diagnostic proxy, not a common calibrated capability scale or production SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** comparison includes quoted results from Show-o and other unified/diffusion/AR models, same-base understanding-only DPO, generation-only DPO, Pair-DPO rounds 0–3 and candidate-richness sensitivity。Most gain occurs in round 1；after round 2 generation is nearly flat, and too few samples can make both capabilities worse。The paper does not disclose equal-compute independent-DPO mixtures, multi-seed uncertainty, threshold/beta sensitivity, scorer replacement, held-out curation data or full sampling/training overhead across rounds。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Show-o/HermesFlow is 1.3B；paper training uses 8 NVIDIA A100 GPUs, batch 4 per caption/generation stream and 3,000 steps；repository examples use 512×512 images, 50 generation steps, guidance scale 5 and a one-GPU launcher。A100 memory, precision, gradient accumulation, candidate count `n`, sequence/image-token lengths, wall time, peak memory, full generated-sample count, evaluation concurrency, latency, throughput, energy and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' 5,000-pair Show-o/JourneyDB contract, self-generated paired data and repeated post-training correlate with improvements over the base on reported understanding and generation metrics；same-base ablations show the paired workflow reaches a different operating point than separately optimized DPO branches。The experiments also prove two system constraints inside this setup: preference quality depends on candidate richness, and iterative returns diminish quickly。
- **What It Does Not Prove:** it does not prove that understanding is universally stronger than generation, because the “gap” subtracts scores produced by different evaluators and protocols；it does not prove mutual causal transfer, unbiased self-improvement, generality across backbones or superiority to equal-compute independent objectives。Quoted cross-model benchmarks are not a single controlled run。GPT-4o/TIFA/BERT/self-VQA scores do not prove visual truth, user safety, diversity, provenance or production fitness。
- **Limitations / Threats to Validity:** v1 itself acknowledges evaluation on only one open unified backbone。More fundamentally, Equation 12 defines the two DPO losses additively, but Equations 13–15 replace that sum with `log sigmoid(Delta_Und * Delta_Gen)`；this is not an algebraic identity, and two negative margins yield a positive product, so the printed objective can reward both preferences moving in the wrong direction。BERT similarity can reward caption overlap over visual grounding；same-model VQA creates correlated self-confirmation；the generation threshold selects easy examples；iterations change scorer and policy together；no seeds/confidence, immutable run or complete compute accounting are reported。
- **Trade-offs / New Failure Modes:** homologous pairs reuse unlabeled data, preserve cross-direction provenance and can coordinate shared-backbone updates；they also multiply candidate-generation/VQA work and couple two noisy feedback channels。A weak modality or proxy can contaminate the other；product coupling can cause sign/pathological-gradient behavior；self-play may reinforce shared blind spots；fixed threshold and sample count create selection bias；iterative data overwrite complicates rollback, audit and reproducibility。
- **Where the Previous Design Still Applies:** independent caption/image DPO remains safer when verifiers differ or one modality must not perturb the other；supervised/human preference data is preferable for high-stakes quality；external or ensemble critics reduce same-model correlation；simple fixed datasets ease reproducibility；separate understanding encoder plus generation decoder remains appropriate when unified parameter sharing causes interference。A corrected additive or explicitly gated multi-objective loss is an alternative, not something v1 has proved equivalent to its product form。
- **Evolution Relationship:** `Direct Evolution` for `independent modality preference loops → homologous paired records → iterative regenerated preferences`；`Layering / Dependency` between representation identity, multimodal generation and post-training；`Alternative Branch` between additive multi-task DPO, gated/product coupling, human/external preference and independent modality objectives。The next pressure is mathematically valid coupling, independent calibrated critics and versioned round-level data/checkpoint lineage。
- **ROADMAP Node:** canonical owner `TRAIN-DPO`（Current Ch34；Legacy Ch30）；handoffs to `MULTIMODAL-REPRESENTATION`, `MULTIMODAL-GENERATIVE-PARADIGMS`, `TRAIN-DATA` and `PLATFORM-EVALUATION-SYSTEM`。DPO owns margin coupling and reference-policy semantics；Representation owns homologous/modality identity；Generation owns image sampling and mutable output；Data owns iterative preference lineage；Evaluation owns proxy comparability and uncertainty。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch24 Multimodal Generative Paradigms, Ch27 Data, Ch33 GRPO, Ch34 DPO and Ch66 Evaluation System。Ch34 already establishes correct DPO margin semantics and warns that pair proxies/shortcuts require independent evaluation；Ch23 owns cross-modal identity；Ch24 owns generation iteration/commit state；Ch66 already rejects same-source judges and incomparable proxies as truth。
- **Existing Coverage:** current Books already cover all stable principles needed to reject the paper's strongest generalization: shared tensor space is not shared semantics；self-generated proxy is not truth；two objective branches need explicit ownership；DPO margins cannot be coupled by an unjustified algebraic rewrite。HermesFlow contributes a concrete homologous-record and iterative-preference design branch, but its central printed objective must remain disputed until code/formula and independent evidence are reconciled。
- **Integration Decision:** `Disputed — Books Frozen`。Do not integrate the Pair-DPO product objective or the universal understanding-generation gap claim。After Historical Books Gate opens, only the stable data-lineage lesson may be reconsidered if the event-time implementation, corrected objective and independent evaluation become available；no Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；separated v1 from September v2/current NeurIPS artifact；reconstructed homologous data, self-play and evaluation contracts；recorded the Equation 12→15 non-equivalence and evaluator mismatch；mapped a canonical owner while freezing Books disposition。
- **Open Questions:** event-time commit/container/data/checkpoint/raw runs；actual implemented loss and exact v1→v2 formula/code change；formal analysis of negative/zero margins and gradient stability；additive/gated/product equal-compute ablation；candidate count/threshold/beta/seeds sensitivity；independent caption/image scorers；held-out curation/evaluation separation；round-level data lineage and rollback；cross-backbone/modality transfer；precision/wall-time/sample-generation cost/energy；latency/SLO and independent reproduction。

### Atom of Thoughts: Dependency-guided Contraction into an Unverified Reasoning State

- **Candidate / Week / Score:** Atom of Thoughts: Markov LLM Test-Time Scaling / 2025-W08 / 25/30。
- **Source Family ID:** `atom-of-thoughts-contracted-reasoning-state`。
- **Source Type:** arXiv research paper + official implementation repository + later NeurIPS/OpenReview lineage。
- **First-public Date / Revision History:** arXiv v1 was submitted 2025-02-17 16:52:42 UTC；v2 2025-03-23, v3 2025-11-28 and v4 2025-12-27 are later revisions。W08 is locked to v1；the NeurIPS 2025 OpenReview record is later publication lineage, not a second W08 event。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12018v1；https://arxiv.org/abs/2502.12018；https://github.com/qixucen/atom。
- **Related Primary Sources:** https://openreview.net/forum?id=qXSFkP0ELS records the later NeurIPS version。The paper adapts Chain-of-Thought, self-consistency, Self-Refine, Analogical Prompting, AFlow and Forest-of-Thought baselines；those sources define comparison ancestry, while the authors' adaptations and reported runs remain the evidence actually audited here。
- **Access and Verification Status:** v1 full text, formulas, algorithms, all main/appendix experiments, prompts, case studies, limitations and current official repository verified。The repository has no release/tag or immutable W08 commit, environment, prompt digest, raw run bundle or event-time model snapshot；current code establishes lineage, not exact reproduction of the February experiments。
- **Full-read Coverage:** read metadata/revision history, Abstract, Introduction, Related Work, probabilistic/Markov framing, DAG decomposition and contraction algorithm, all benchmark and test-time-scaling tables, cost comparison, decomposition/DAG ablations, Conclusion, Limitations, Ethics, implementation details, task prompts, BBH subsets, FoT/AFlow adaptations and successful/failed case studies；inspected the official repository's API abstraction, `atom`/`plugin` modes, supported datasets and current command surface。
- **Original Problem:** retaining an expanding reasoning history helps provenance, correction and backtracking, but long chains and search trees consume token/API budget and can distract the model with obsolete intermediate text。The system question is whether solved dependencies can be contracted into a smaller, self-contained next question without losing answer-critical state。
- **Why the Previous Design Was Reasonable:** full Chain-of-Thought preserves the visible derivation；tree/graph search preserves alternatives and rollback points；durable DAGs make dependency and parallelism explicit；RAG or external Memory preserves source evidence。These remain rational when auditability, correction, branching, exact facts or irreversible decisions matter more than compactness, and simple CoT remains cheaper for short tasks where decomposition overhead dominates。
- **Changed Constraint:** test-time budgets now permit repeated model calls, while many multi-hop tasks contain subquestions whose results can be summarized as conditions。The authors therefore trade persistent history for a smaller derived state, seeking depth without carrying every previous token into the final solver or downstream reasoning framework。
- **Mechanism:** for state `Q_i`, an LLM decomposes the question into ordered subquestions, annotates dependencies as a DAG, solves independent subquestions as known conditions and contracts dependent descriptions plus known results into a new self-contained question `Q_(i+1)`。The maximum path length of the initial graph bounds iteration depth；the terminal question is solved directly, or the contracted state is passed to another test-time framework as a plugin。The method calls the resulting transition “Markov”, but answer equivalence and information sufficiency are prompt-level assumptions rather than verified invariants。
- **State Ownership:** the original task and reference answer own problem identity；the decomposer owns subquestion order；the dependency annotator owns the temporary DAG；sub-solvers own derived answers；the contraction step owns the next natural-language state and its version；the final solver owns the proposed answer；the harness owns depth, call budget, decoding and scoring。The contracted text is derived state, not an authoritative replacement for raw evidence, intermediate provenance or environment state。
- **Control Flow / Data Flow:** `Q_i → JSON subquestions → ordered dependency annotation → temporary DAG → classify independent/dependent nodes → solve independent nodes → rewrite dependent content plus solved conditions into Q_(i+1) → stop at depth/terminal condition → direct solver or plugin framework → benchmark evaluator`。The paper imposes acyclicity by allowing a subquestion to depend only on earlier generated questions, so model-generated ordering affects which dependencies can be represented。
- **Implementation Details:** the current Python repository calls OpenAI-compatible chat APIs, offers standalone `atom` and preprocessing `plugin` modes, and includes entry points for MATH, GSM8K, BBH, MMLU, HotpotQA and LongBench-style tasks。Paper prompts ask the model to emit decomposition, dependency and contraction JSON；the February code/prompt/model snapshot is not pinned, and API service behavior is external mutable state。
- **Evaluation Contract:** the main study uses `gpt-4o-mini-0718`；the first 1,000 test examples are used for MATH, selected BBH multiple-choice subsets, MMLU-CF and HotpotQA, full GSM8K has 1,319 examples, and LongBench uses 400 MuSiQue/2WikiMultiHopQA examples。The reasoning-model comparison uses only the first 100 MuSiQue examples because of compute/stability constraints。Reported main averages place CoT at 73.7, AoT at 80.8 and three-run selector AoT* at 81.4 across the authors' task aggregate；these numbers are tied to that API, prompt, subset and evaluator contract。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines include CoT, five-sample CoT-SC, Self-Refine, Analogical Prompting, AFlow and an adapted FoT/ToT configuration with branch factor 3。The authors report three runs and ablate decomposition and DAG structure；AoT reports 83.6/95.0 on MATH/GSM8K versus 82.9/94.8 without decomposition and 82.7/94.3 without DAG。Depth analysis shrinks from 1,000 MATH examples at depth 1 to 207 at depth 5 while reported accuracy rises 83.2→92.7, so it is a progressively selected survivor cohort, not a same-population causal depth curve。FoT cost claims use author-modified implementations and do not disclose a complete equal-token/equal-call/equal-latency contract。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** experiments use hosted `gpt-4o-mini-0718`, with additional reported comparisons to o3-mini and DeepSeek-R1-style reasoning models；provider hardware, model precision and internal batching are Not Disclosed。Prompt/output lengths, temperature, seeds, API-call counts per example, retries, parallelism, rate limits, wall-clock latency, monetary cost, energy and production SLO are also Not Disclosed；therefore “lower computation” is not a deployable cost result。
- **What the Evidence Actually Proves:** under the authors' API, prompt, subset and evaluator setup, dependency-guided decomposition plus contraction reaches a different accuracy operating point from the tested baselines and can be layered before another search framework。The ablation suggests that both decomposition and explicit dependency prompts contribute within this implementation；the published failure cases independently demonstrate that contraction quality is a correctness-critical state transition rather than harmless summarization。
- **What It Does Not Prove:** the experiments do not prove a formal Markov property, semantic equivalence between `Q_i` and `Q_(i+1)`, universal improvement, calibrated lower cost, production latency benefit or superiority under equal token/call budgets。The o3-mini comparison changes model and workload conditions；AoT* adds selection calls；the depth curve does not prove that increasing depth improves the same cohort。Benchmark answers do not establish provenance retention, rollback safety or workflow durability。
- **Limitations / Threats to Validity:** dependency order is generated by the same model and the earlier-only rule can omit valid backward/future dependencies；a wrong decomposition or contracted condition propagates without a built-in detector, reflection or repair path。Natural-language contraction can delete constraints, units, temporal qualifiers or contradictory evidence；the appendix shows failed contractions that destroy independence or lead to wrong answers。API/model drift, modified baselines, selected task subsets, missing exact sampling/cost contract, lack of uncertainty bars and survivor bias in depth analysis further limit generalization。
- **Trade-offs / New Failure Modes:** contraction reduces visible history and can lower downstream context size, while decomposition exposes dependency structure and possible parallel work。It also adds multiple model calls, a lossy rewrite boundary and a new state owner；once raw intermediate evidence is discarded, a later solver cannot audit or roll back the error。Persisting graph, raw outputs and contraction lineage restores recoverability but gives back part of the token/storage/orchestration saving。
- **Where the Previous Design Still Applies:** full-history CoT remains suitable for short or audit-sensitive reasoning；tree/graph search remains appropriate when alternatives and backtracking matter；durable workflow DAGs remain necessary for tools, side effects and recovery；RAG/external Memory remains appropriate when source evidence must survive compression。A hybrid can pass a compact contracted view to the model while retaining typed facts and links to raw states outside the prompt。
- **Evolution Relationship:** `Direct Evolution` for `full visible reasoning history → temporary dependency DAG → contracted self-contained state → bounded downstream search`；`Layering / Dependency` with Context compression, Planning and cost/evaluation control；`Alternative Branch` versus full history, persistent tree/DAG search, retrieval and external Memory。The next pressure is a verifiable preservation contract, uncertainty-triggered fallback, provenance links and rollback rather than still more unverified compression depth。
- **ROADMAP Node:** canonical owner `AGENT-PLANNING`（Current Ch79；Legacy Ch75）；handoffs to `AGENT-CONTEXT`, `AGENT-WORKFLOW`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。Planning owns decomposition and dependency semantics；Context owns the lossy working-state view；Workflow owns durable execution/recovery rather than the reasoning compression；Evaluation owns subset/selection evidence；Cost owns API, token and outcome accounting。
- **Target and Adjacent Chapters Read:** read Ch75 Context, Ch79 Planning, Ch81 Workflow, Ch66 Evaluation System and Ch70 Cost。Ch79 already owns decomposition/DAG/call-growth trade-offs；Ch75 requires a preservation contract and raw-evidence fallback for compression；Ch81 separates temporary model state from durable transition history；Ch66 rejects selected subsets and proxy aggregates as universal truth；Ch70 requires actual state-dependent work rather than token-count slogans。
- **Existing Coverage:** the Books already contain the stable principles that decomposition should follow verifiable boundaries, compressed Context is derived/lossy state, and durable Workflow must retain recovery history。AoT contributes one useful bounded evolution branch—turning a temporary dependency graph into a smaller next-question state—but does not establish a new durable owner or verified Markov abstraction。A future refinement should connect Planning's decomposition section to Context's preservation contract without copying the paper's benchmark narrative。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `AGENT-PLANNING`。Historical Books Gate remains closed；future integration, if opened, may add contracted-state planning as a conditional branch only when raw lineage, preservation tests and fallback remain visible。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；separated February v1 from later revisions/OpenReview；reconstructed DAG, contraction, plugin and benchmark contracts；identified survivor selection in depth scaling and missing cost contract；mapped one canonical owner and four handoffs；no Books change。
- **Open Questions:** immutable W08 code/prompt/environment/run digest；exact API model snapshot, temperature, seeds, retry and concurrency settings；per-example token/call/latency/cost distributions；same-cohort randomized depth comparison；matched-budget baselines；dependency-order sensitivity；graph/parser failure rate；formal or empirical answer-equivalence tests；constraint/temporal/unit preservation slices；uncertainty detector and raw-state fallback；rollback/provenance overhead；tool/workflow extension；independent reproduction。

### Dynamic Concepts Personalization: Appearance Basis before Motion Residual

- **Candidate / Week / Score:** Dynamic Concepts Personalization from Single Videos / 2025-W08 / 25/30。
- **Source Family ID:** `dynamic-concepts-set-sequence-lora`。
- **Source Type:** arXiv research paper + official Snap Research project page and supplementary media；later SIGGRAPH 2025 publication lineage。
- **First-public Date / Revision History:** arXiv v1 was submitted 2025-02-20 18:53:39 UTC and remains the only arXiv version。The project page later labels the work SIGGRAPH 2025；that venue metadata is later publication lineage, not a new W08 mechanism event。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14844v1；https://arxiv.org/abs/2502.14844；https://snap-research.github.io/dynamic_concepts/。
- **Related Primary Sources:** the project page exposes the authors' supplementary videos and frames the same Set-and-Sequence mechanism。The paper uses Snap Video's non-public 11.5B DiT backbone and adapts public personalization baselines, but no official source-code, model-weight, training-data or immutable run artifact was released for this family。
- **Access and Verification Status:** v1 full text, formulas, architecture/training appendix, all quantitative tables, user study, limitations, prompts and official project media verified。No code, checkpoint, dataset manifest, raw generations, per-example scores, evaluator implementation, environment lock or independent reproduction is available；the family is `Experimental`, not reproducible evidence。
- **Full-read Coverage:** read metadata, Abstract, Introduction, all Related Work branches, flow-matching/LoRA preliminaries, two training stages, four regularization mechanisms, evaluation set/baselines/metrics, quantitative and qualitative results, composition and identity-leakage handling, user study, Limitations, Conclusion, full architecture/training appendix and prompt appendix；reviewed the official project explanation and supplementary-media role。
- **Original Problem:** a single video's subject identity and motion are entangled。Directly fitting one adapter can memorize appearance and motion together, reconstruct the training clip yet fail to preserve identity under new prompts, edit motion independently or compose multiple dynamic concepts without leakage。
- **Why the Previous Design Was Reasonable:** a single LoRA is simple, portable and preserves one artifact；UNet designs with separate spatial/temporal modules expose an architectural separation directly；image personalization plus image-to-video reuses mature components；encoder-based personalization avoids per-concept optimization。These remain preferable when the backbone already factorizes time, the task is static identity/style, latency and artifact count dominate, or broad zero-shot generalization matters more than fitting one clip。
- **Changed Constraint:** joint spatio-temporal DiTs improve video generation but no longer expose clean spatial and temporal layers。At the same time, one clip provides both an unordered appearance sample set and an ordered motion sequence。The authors therefore impose a factorization in adapter weight space rather than requiring the base architecture to provide one。
- **Mechanism:** Stage I shuffles frames, optimizes a high-rank LoRA `A1 B1` with static appearance/environment prompts and treats it as an identity basis。Stage II freezes `A1` and `B1`, adds `A1 B2`, and trains only the new coefficient matrix on the ordered video with static plus motion/camera prompts。Prior-preservation videos, heavy coefficient dropout, text-token masking and self-conditioning regularize the single-example fit；multi-concept composition jointly learns a shared basis/residual set and optionally adds infrequent stitched videos to reduce identity leakage。
- **State Ownership:** source videos and frame order own observation identity；frame sampler owns the unordered Set view；the full clip owns Sequence timing；prompt annotations own appearance/motion/environment labels；the base DiT identity, `A1/B1`, `B2`, dropout/mask policy and training stage own adapter lineage；stitched examples own composition regularization；sampler/CFG and evaluator own generated artifacts and scores。The learned basis is a parameterization hypothesis, not ground-truth semantic disentanglement。
- **Control Flow / Data Flow:** `single video → unordered frames + static prompt → train A1/B1 identity basis → freeze basis → ordered clip + static/dynamic prompt → train B2 motion residual → optional prior/stitched regularization → select/combine adapter coefficients and new prompt → diffusion sampling → identity/text/reconstruction/temporal metrics + human preference`。Stage identity and base/adapters must remain versioned because Stage II is only meaningful relative to the exact frozen Stage I artifact。
- **Implementation Details:** the base is an 11.5B latent-video DiT with MAGVIT-style causal autoencoder, effective `8×32×32` compression, 32 blocks, hidden size 4096, 32 heads, 3D-RoPE, 6,144-token attention window, T5 conditioning, FlashAttention and self-conditioning。The authors pretrain the base for 822K steps on 256 H100 GPUs in BF16/FSDP；personalization uses A100 80GB, batch 8, AdamW, constant `1e-4`, weight decay 0.01, gradient clipping 0.05, Stage-I/II coefficient dropout 0.8/0.5 and CFG 8。Final single-video runs use about 600/900 stage steps；complex multi-video motion uses 2K–2.5K Stage-II steps。No code ties these settings to an executable revision。
- **Evaluation Contract:** the curated evaluation set contains five human identities performing walking/dancing plus one two-person interaction scenario；local/global editing includes shirt/background changes and adding a glass。Metrics are CLIP text similarity, ArcFace identity similarity, frame-aligned MSE and adjacent-frame CLIP similarity as temporal coherence。The user study has ten participants comparing pairs on identity, motion, prompt adherence and overall preference；UNet baselines are omitted from that study after author qualitative screening。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include Textual Inversion, DreamBooth/LoRA, NewMove, DreamVideo and an author DiT adaptation of DreamMix, plus rank-1/rank-8, two-stage and regularized ablations。The reported final method trades slightly lower identity than DB-LoRA (`0.680` versus `0.703`) for higher CLIP-text (`0.239` versus `0.224`) at similar MSE/temporal score；the paper does not report seeds, confidence intervals, rank/dropout/step sensitivity, equal-compute tuning, held-out concepts, composition metrics or runtime overhead。The no-regularization 150+400-step run is said to take about 90 minutes, while final regularized runs are slower but wall time and GPU count are Not Disclosed。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base pretraining reports 256 H100 GPUs, BF16/FSDP, 17→121 frames, 512/1024 px and 24 fps；personalization reports NVIDIA A100 80GB, batch 8, up to 121 frames and 1024×576 examples。Number of A100s, personalization precision, gradient accumulation, memory peak, inference steps/sampler, generation latency, throughput, concurrency, storage, energy and production SLO are Not Disclosed。The 90-minute statement belongs to the simpler no-regularization setup, not the final method。
- **What the Evidence Actually Proves:** on the authors' five-identity editing set and private DiT, staged basis/residual optimization reaches a distinct reconstruction–identity–prompt operating point from tested adapters and author-adapted baselines。The ablation supports a practical ordering constraint in this setup: learning appearance from unordered frames before adding ordered motion changes editability, and the final regularization recovers reconstruction/identity lost by the unregularized two-stage branch。Qualitative cases expose multi-identity leakage as a real composition failure mode。
- **What It Does Not Prove:** it does not prove that `A1/B1` contains only identity, `B2` contains only motion, that the factorization transfers to other backbones/concepts, or that composition is semantically independent。A five-identity curated set and ten-person study do not establish a general benchmark。Adjacent-frame similarity can reward static or low-motion outputs；frame MSE can punish valid edits；ArcFace applies only to human identity。High percentages without trial counts/uncertainty do not prove population preference or production quality。
- **Limitations / Threats to Validity:** private base/data/code prevent reproduction；dataset and human-study scale are small；baseline ports are not all native or equally tuned；UNet methods are excluded from the user study；no motion ground truth, diversity, high-frequency-motion slice, multi-seed or independent evaluator is provided。Detailed prompts themselves encode appearance, environment and action, confounding learned factorization；same-basis composition can leak identity, and stitched-video/background-removal heuristics add another data-dependent branch。The authors acknowledge expensive per-concept optimization and weakness on erratic/rapid motion。
- **Trade-offs / New Failure Modes:** staged training creates a controllable adapter hierarchy and may preserve appearance while adding motion, but doubles optimization stages and couples every residual to one frozen basis/base revision。High rank supplies capacity while 0.8/0.5 dropout fights overfit, producing a sensitive capacity–regularization operating point。Freezing can protect identity yet lock Stage-I errors；residual composition can interfere；prompt detail can become a shortcut；stitched regularization can encode artificial boundaries；many per-user adapters create registry, privacy, deletion and serving-routing cost。
- **Where the Previous Design Still Applies:** one low-rank adapter remains suitable for a single fixed clip or static concept；full fine-tuning remains a capacity-first option with sufficient data；architecture-specific spatial/temporal modules remain clear when the backbone exposes them；image personalization plus image-to-video remains modular；feed-forward encoders are preferable for many users or low-latency onboarding。Explicit motion controls, trajectories or world models remain necessary when controllable dynamics rather than visual imitation is the contract。
- **Evolution Relationship:** `Direct Evolution` for `single entangled adapter → unordered-frame identity basis → frozen-basis motion residual → multi-concept residual composition`；`Layering / Dependency` between multimodal representation, diffusion generation, LoRA artifact lineage, data prompts and evaluation；`Alternative Branch` versus architecture-level factorization, one adapter, full fine-tuning and encoder-based personalization。The next pressure is feed-forward encoding, factorization interventions and scalable governed adapter lifecycle rather than ever-longer per-concept optimization。
- **ROADMAP Node:** canonical owner `MULTIMODAL-REPRESENTATION`（Current Ch23；Legacy N/A）；handoffs to `MULTIMODAL-GENERATIVE-PARADIGMS`, `TRAIN-LORA`, `TRAIN-DATA` and `PLATFORM-EVALUATION-SYSTEM`。Representation owns appearance/motion/time identity；Generation owns diffusion sampling and commit；LoRA owns parameter/update artifact semantics；Data owns single-video/prompts/prior/stitched lineage；Evaluation owns metric validity and generalization evidence。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch24 Multimodal Generative Paradigms, Ch27 Data, Ch30 LoRA and Ch66 Evaluation System。Ch23 already requires temporal/provenance identity and distinguishes continuous/discrete/hybrid representation；Ch24 owns video diffusion and final artifact evaluation；Ch30 covers rank, regularization, composition and base/adapter identity；Ch66 rejects small proxy suites as deployment truth。
- **Existing Coverage:** current Books already state that tensor compatibility is not semantic disentanglement and that LoRA factors/artifact composition do not prove independent behavior。This family adds a useful bounded representation branch: impose appearance/motion ordering in adapter parameter space when a joint DiT lacks an architectural split。A future refinement belongs near Ch23's representation-evolution line, with Ch30 retaining artifact/rank ownership；the paper's metric table and private-backbone claims should not enter prose。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `MULTIMODAL-REPRESENTATION`。Historical Books Gate remains closed；future integration may add Set-before-Sequence as an experimental conditional branch while preserving single-adapter, architecture-factorized and encoder-based alternatives。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；verified the sole revision and official project page；reconstructed staged parameter/data/evaluation contracts；bound hardware numbers to base-pretraining versus personalization phases；recorded metric, dataset, prompt and artifact limitations；mapped one canonical owner and four handoffs；no Books change。
- **Open Questions:** official code/checkpoint/dataset/raw generations；immutable base and adapter digests；exact A100 count, precision, wall time and inference sampler；rank/dropout/step/prompt sensitivity；motion-specific ground truth and high-frequency slices；identity/motion intervention disentanglement；held-out non-human concepts and cross-backbone transfer；composition/identity-leakage metrics；user-study trial/randomization/uncertainty；privacy/consent/deletion for personalized videos；adapter registry/routing/merge cost；independent reproduction。

### RealSyn: From Document Co-occurrence to Retrieved Pairing and Synthetic Augmentation

- **Candidate / Week / Score:** RealSyn: An Effective and Scalable Multimodal Interleaved Document Transformation Paradigm / 2025-W08 / 26/30。
- **Source Family ID:** `realsyn-interleaved-document-transformation`。
- **Source Type:** arXiv research paper + official project page + official implementation/artifact repository + released Hugging Face dataset artifacts；later ACM MM 2025 lineage。
- **First-public Date / Revision History:** arXiv v1 was submitted 2025-02-18 03:58:38 UTC；v2 was submitted 2025-04-17 and v3 on 2025-08-05。W08 is locked to v1；the current repository, dataset cards and ACM MM status are later artifact/publication lineage and cannot silently replace the February data contract。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12513v1；https://arxiv.org/abs/2502.12513；https://github.com/deepglint/RealSyn；https://garygutc.github.io/RealSyn/；https://huggingface.co/datasets/Kaichengalex/RealSyn15M。
- **Related Primary Sources:** the official repository links RealSyn15M/30M/100M artifacts and a download helper；OBELICS supplies the source interleaved documents；EVA02-CLIP E/14-plus, OFA, RAM++, ChatGPT-4 Turbo, LLaMA3-8B and vLLM supply filtering, retrieval, caption/tag synthesis, instruction generation and batched inference stages。These dependencies define the pipeline lineage, but their presence does not validate the resulting pair semantics or source rights。
- **Access and Verification Status:** v1 full text, formulas, all experiments/ablations/appendices, official project page, current repository and public dataset card/viewer verified。The repository does not expose the full extraction/filtering/retrieval/generation pipeline, event-time code digest, immutable source manifest, raw evaluation runs or model/container lock；current dataset artifacts are mutable and their row-count/license metadata does not fully reconcile with v1。Status is `Experimental` rather than independently reproducible。
- **Full-read Coverage:** read metadata/revision history, Abstract, Introduction, Related Work, complete image/text filtering, hierarchical retrieval, synthetic-text generation, semantic filtering, semantic-balanced sampling, CLIP training setup, all linear-probe/zero-shot/robustness/retrieval/captioning tables, data-size comparison, real/synthetic-text ablations, claimed scaling fit, Limitations, Ethics, Conclusion and the full implementation/prompt/result appendix；inspected the official repository structure, download links/notebook lineage, project page and current dataset card/viewer examples。
- **Original Problem:** multimodal interleaved documents contain images and nearby prose at web scale, but they do not provide a reliable one-to-one image-text pairing contract。Training CLIP-style models needs pairs, while using only alt text or adjacent sentences discards much of the document and using all co-occurring text injects unrelated descriptions。
- **Why the Previous Design Was Reasonable:** curated human pairs and alt text have clear local provenance；document-neighbour sentences are cheap and preserve source context；raw interleaved sequences suit multimodal language modelling without inventing pair identity；synthetic captions can add visual details when real text is sparse。These designs remain rational when grounding precision, rights lineage, deterministic reproduction or sequence-level context matters more than maximum pair count。
- **Changed Constraint:** the source corpus has hundreds of millions of images and billions of sentences, while stronger embedding models, approximate cluster search and language models make global retrieval and caption synthesis computationally feasible。The bottleneck shifts from collecting enough text to deciding which transformed association is trustworthy, diverse and governable。
- **Mechanism:** the pipeline extracts 336M images and 2.13B sentences from 118M OBELICS documents, filters them to 198M images and 0.84B sentences, embeds all retained sentences with EVA02-CLIP E/14-plus and clusters them into 2M groups。Each image first retrieves candidate clusters and then sentences inside those clusters；OFA captions, RAM++ tags, top retrieved text and 100K ChatGPT-4-Turbo-generated instructions supervise a LLaMA3-8B generator that produces synthetic descriptions。A CLIP-similarity band removes 29.7M extreme pairs, then 1M image clusters and per-cluster caps produce 15M/30M/100M subsets。
- **State Ownership:** source document/URL and acquisition revision own raw provenance；extracted image and sentence identities own source membership；filter versions and scores own retention decisions；embedding/checkpoint and cluster centres own retrieval geometry；retrieval rank owns the soft association；OFA/RAM++/instruction/generator revisions own synthetic text lineage；similarity band owns pair acceptance；image-cluster identity and cap own sampling weight；dataset manifest/split/license/digest own the released training artifact。A retrieved or generated text is a derived claim, not ground-truth description。
- **Control Flow / Data Flow:** `OBELICS documents → extract image/sentence pools → modality-specific filtering and deduplication → sentence embedding + 2M clusters → image-to-cluster and intra-cluster retrieval → real text candidates + OFA caption + RAM++ tags → 100K instruction synthesis → LLaMA3-8B generation through vLLM → image/synthetic-text similarity-band filter → image embedding + 1M semantic clusters → per-cluster cap → RealSyn15M/30M/100M manifest → CLIP training → multi-suite evaluation`。Because the pipeline pools records globally, source-document locality is no longer the pair invariant and must be retained separately if provenance is required。
- **Implementation Details:** image filtering uses dimension/aspect checks and EVA02-CLIP E/14-plus duplicate detection；sentence filtering removes emoji/URLs, enforces 3–81 words, CAT `C1 + action`, entropy above 0.3, GPT2-large perplexity 30–200 and deduplication。Hierarchical retrieval is reported as 40 hours on 8 NVIDIA A100 GPUs versus an estimated more than 10,000 hours for direct search。The generator is LLaMA3-8B fine-tuned on 100K ChatGPT-4-Turbo instruction examples and served with vLLM。The current repository mainly exposes figures, download helper and analysis notebook rather than an executable end-to-end pipeline。
- **Evaluation Contract:** standard CLIP training uses 224×224 images, text length 77, batch 4096, 32 epochs, AdamW learning rate `1e-3`, weight decay 0.2 and beta `(0.9, 0.98)` on 8 A100 80GB GPUs。Evidence includes linear probing on 20 datasets, zero-shot transfer on 20 datasets, robustness suites, Flickr30k/MSCOCO retrieval and selected captioning/MLLM extensions；comparisons use YFCC15M and LAION subsets at 15M/30M/100M scales。This is a representation-training contract, not a production data-quality or legal-compliance test。
- **Baselines / Ablations / Sensitivity / Overhead:** matched-scale comparisons report higher average results for the authors' transformed subsets under their recipe。Ablation shows one to three retrieved real texts improves average linear probing from 70.3 to 71.2, while four/five decline to 70.9/70.6；adding one to five synthetic texts monotonically declines from 70.2 to 69.1。Cars and Flowers regress because their concepts are underrepresented after balancing。The claimed data-scaling curve is fitted on 12M–60M and checked at 100M within one dataset/model family；there is no multi-seed uncertainty, equal-total-compute accounting, filtering-threshold sensitivity, generator replacement, contamination audit or full pipeline cost。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** retrieval reports 8 A100 GPUs and 40 hours；CLIP training reports 8 A100 80GB GPUs, 224×224 input, 77 text tokens, batch 4096 and 32 epochs。CLIP architecture size, training precision, gradient accumulation, storage/network bandwidth, complete preprocessing and LLM-generation GPU/time/token contract, peak memory, energy, concurrency, serving latency/throughput and production SLO are Not Disclosed。The paper's retrieval estimate cannot be read as end-to-end dataset-construction cost。
- **What the Evidence Actually Proves:** under the authors' OBELICS-derived pipeline and fixed CLIP recipe, retrieval-based real text plus semantic balancing produces a different and often stronger average representation operating point than tested matched-scale YFCC/LAION subsets。The ablations demonstrate two important negative results inside this contract: more retrieved text eventually adds noise, and more synthetic descriptions do not monotonically improve the trained representation。Balancing also leaves domain-specific regressions visible rather than eliminating them。
- **What It Does Not Prove:** the evidence does not establish universal dataset quality, factual or visual correctness of retrieved/generated descriptions, a general data-scaling law, superiority for arbitrary multimodal architectures, or production cost efficiency。It does not prove copyright permission, consent, PII removal, harmful-content control, withdrawal propagation or absence of train/evaluation contamination。Public artifact availability does not prove exact v1 reproduction when manifests and pipeline code are missing。
- **Limitations / Threats to Validity:** the same EVA02-CLIP family influences deduplication, retrieval, semantic filtering and balancing, creating representation-model circularity；global retrieval weakens document-local provenance；perplexity/entropy/category filters can suppress rare languages and legitimate complex text；the unusual upper similarity cutoff can remove genuinely strong pairs as well as OCR shortcuts。Deduplication and split algorithms are not fully disclosed；randomly choosing among texts introduces run nondeterminism；raw image URLs can rot；current 15M artifact metadata estimates roughly 13.54M rows while paper/repository naming reports 15,239,498；dataset-card licensing does not resolve source-level derivative rights。No independent reproduction, uncertainty or longitudinal artifact audit is reported。
- **Trade-offs / New Failure Modes:** retrieval recovers richer real-world prose without paying to caption every image, but changes pair identity from explicit annotation to model-scored association。Synthetic generation can normalize descriptions and add tags, but introduces hallucination, generator/style bias and substantial hidden compute；the negative ablation shows extra fluency can reduce downstream utility。Semantic caps improve coverage but can underweight important dense domains, make cluster/checkpoint drift part of dataset identity and still miss Cars/Flowers。Mutable URL-backed artifacts add availability, deletion and lineage failure modes。
- **Where the Previous Design Still Applies:** explicit human/alt-text pairs remain preferable for high-precision grounding and rights review；document-local adjacency remains better when source context and provenance are contractual；raw interleaved sequences remain appropriate for sequence-aware multimodal models；synthetic captions remain a conditional branch when a visual verifier and factuality checks exist；fixed stratified sampling remains easier to reproduce when embedding-cluster drift is unacceptable。
- **Evolution Relationship:** `Direct Evolution` for `explicit/local image-text pair → global embedding retrieval soft pair → real-plus-synthetic candidate set → similarity-filtered and cluster-balanced dataset`；`Layering / Dependency` with multimodal representation, pretraining and evaluation；`Alternative Branch` versus curated pairs, document-local interleaving and fully synthetic captioning。The next pressure is source-to-pair provenance, independent semantic verification, immutable manifests and policy-aware deletion rather than simply larger transformed subsets。
- **ROADMAP Node:** canonical owner `TRAIN-DATA`（Current Ch27；Legacy Ch23）；handoffs to `MULTIMODAL-REPRESENTATION`, `TRAIN-PRETRAINING`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-SECURITY`。Data owns selection/transformation/mixture/provenance；Representation owns image-text identity semantics；Pretraining owns CLIP optimization；Evaluation owns slice and contamination evidence；Security owns rights, privacy, deletion and untrusted-source policy。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch27 Data, Ch28 Pretraining, Ch66 Evaluation System and Ch72 Security。Ch27 already treats collection/filtering/mixing as an executable data specification and requires partition-level provenance/rights；Ch23 rejects tensor similarity as semantic truth；Ch28 separates loss improvement from capability proof；Ch66 requires distribution/slice/contamination evidence；Ch72 requires provenance, authorization, minimization and lifecycle threat boundaries。
- **Existing Coverage:** current Books already own filtering, deduplication, distribution weighting, immutable manifests, partition rights and evaluation boundaries。RealSyn adds a valuable conditional evolution branch: when interleaved documents lack explicit pairs, transform co-occurrence into retrieved soft associations before deciding whether synthetic text earns a place。Its strongest durable contribution is the negative trade-off that association count and synthetic-text count are not monotonic quality controls；it refines `TRAIN-DATA` rather than creating a new representation or foundation-model owner。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DATA`。Historical Books Gate remains closed；future integration may add retrieval-mediated pairing as a conditional data-transformation branch only with source lineage, immutable manifests and independent validation。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；separated February v1 from later ACM/repository/dataset-card lineage；reconstructed extraction, retrieval, generation, filtering, balancing and CLIP evaluation contracts；recorded negative synthetic-text ablation, domain regressions, artifact-count drift and governance gaps；mapped one canonical owner and four handoffs；no Books change。
- **Open Questions:** immutable v1 raw/source/transformed manifests and digests；complete pipeline code/container/checkpoints/random seeds；exact image/text deduplication and split algorithms；source-document-to-pair lineage after global pooling；source licenses, consent, PII/NSFW controls, opt-out/deletion and derivative propagation；URL rot and current row-count reconciliation；generator/checkpoint/instruction identities；similarity/entropy/perplexity/cluster-cap sensitivity；train/eval contamination；rare-language/domain bias；equal-compute and multi-seed reproduction；full preprocessing/generation compute, energy and storage contract。

### Diffusion-Sharpening: Amortizing Reward-guided Trajectory Search with a Disputed Objective

- **Candidate / Week / Score:** Diffusion-Sharpening: Fine-tuning Diffusion Models with Denoising Trajectory Sharpening / 2025-W08 / 23/30。
- **Source Family ID:** `diffusion-sharpening-trajectory-reward-amortization`。
- **Source Type:** arXiv research paper + official implementation repository；no release, checkpoint, dataset bundle or immutable experiment artifact。
- **First-public Date / Revision History:** arXiv v1 was submitted 2025-02-17 18:57:26 UTC and remains the sole arXiv version。The current 29-commit repository has no release/tag；it is supporting implementation lineage, not proof of the exact W08 run。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12146v1；https://arxiv.org/abs/2502.12146；https://github.com/Gen-Verse/Diffusion-Sharpening；https://raw.githubusercontent.com/Gen-Verse/Diffusion-Sharpening/main/train_rlhf_diffusion_sharpen_sdxl.py；https://raw.githubusercontent.com/Gen-Verse/Diffusion-Sharpening/main/train_sft_diffusion_sharpen_sdxl.py。
- **Related Primary Sources:** SDXL supplies the base model；Diffusion-DPO, DDPO, D3PO and IterPO supply fine-tuning branches；Demon, Free2Guide and Inference-Scaling supply inference-time trajectory-search branches；JourneyDB, Text-to-Image-2M, Pokemon-Blip, DrawBench and DiffusionDB supply training/evaluation inputs。Several baselines were author-adapted from papers or pseudo-code, so their original publications do not validate the fidelity of these ports。
- **Access and Verification Status:** full v1 text, equations, algorithms, all main/appendix experiments, user-study statement, grader prompt and current official source files verified。Paper equation, released code and configuration records contain unresolved semantic and reproducibility conflicts；there is no event-time commit, model/checkpoint, data split, raw run, environment/container or independent reproduction。Status is `Disputed`。
- **Full-read Coverage:** read metadata, Abstract, Introduction, all Related Work, diffusion/SDE preliminaries, posterior approximation, trajectory reward aggregation, SFT and RLHF algorithms/equations, every result/efficiency/ablation section, Conclusion, full baseline/dataset/training/evaluation appendices, user study, MLLM prompt and qualitative appendix；inspected repository structure, README launch recipes, reward interfaces and both released training paths, including candidate selection and executable loss construction。
- **Original Problem:** reward-driven diffusion alignment faces two costly branches。Single-timestep fine-tuning does not explicitly train the whole denoising path, while inference-time reward search can evaluate many candidates/steps for every request and therefore raises NFE and latency。The question is whether expensive trajectory exploration can be paid during training and amortized into a standard-cost generator。
- **Why the Previous Design Was Reasonable:** standard SFT has simple, stable denoising loss and curated ground truth；offline Diffusion-DPO uses explicit preference pairs and a frozen reference；online DDPO explores current-policy outputs；inference-time search can change reward or budget without retraining and keeps the base artifact immutable。These remain rational when reward changes frequently, auditability matters, training compute is scarce or search is needed only for a small high-value request slice。
- **Changed Constraint:** intermediate diffusion states can be decoded into approximate clean images and scored by differentiable or black-box reward models。Multiple noisy trajectories can therefore be compared before deployment；if their preferred transition pattern is learnable, request-time search work may be shifted into the artifact-training phase。
- **Mechanism:** sample `n` noise candidates from a randomly chosen timestep, advance each for up to `m` denoising steps, decode intermediate predicted clean images, aggregate reward over each path and choose high-reward trajectories。The SFT branch applies denoising loss along the selected path；the RLHF branch chooses best/worst paths online, compares policy and frozen-reference denoising losses and applies a Diffusion-DPO-style logistic update。Inference then uses the trained SDXL path without online reward search。
- **State Ownership:** prompt/image dataset owns conditioning identity；base SDXL, scheduler, CFG and VAE own diffusion dynamics；random timestep/noise seeds own candidate identity；trajectory state owns ordered latents and decoded approximations；reward model/version/prompt owns ranking；best/worst selector owns pair semantics；policy/reference checkpoints and beta own update identity；evaluator owns reported evidence。A high reward is scorer-relative evidence, not image truth or human preference by construction。
- **Control Flow / Data Flow:** `prompt or image-text pair → random timestep + n noisy latents → m-step DDIM transitions → decode predicted x0 at each step → scorer-specific path rewards → aggregate and select best/worst trajectory → SFT path loss or policy/reference pair loss → update UNet → standard-NFE inference → CLIP/composition/aesthetic/ImageReward/GPT-4o/user evaluation`。Training and inference costs must remain separate but jointly accounted because the method deliberately transfers work between phases。
- **Implementation Details:** paper uses SDXL with DDIM, nominal `T=50` and CFG 5；efficiency text reports `n=3`, three path steps and learning rate `1e-6`。Appendix instead reports AdamW without weight decay, betas `(0.0, 0.99)`, learning rate `5e-6` and batch 8。Repository examples use 512 resolution, per-device batch 1, gradient accumulation 4, FP16, learning rate `1e-6` and 10,000 steps；current code defaults to 1024 resolution, batch 16, learning rate `1e-4`, 25 inference steps, three trajectories/noisy latents and integer beta 2500。No source-pinned recipe reconciles these contracts。
- **Evaluation Contract:** main table compares SDXL and nine fine-tuning/search variants on CLIP, six T2I-CompBench slices, aesthetic score, ImageReward and GPT-4o-derived MLLM score。SFT uses JourneyDB, Text-to-Image-2M and Pokemon-Blip；RLHF samples 10,000 prompts from DrawBench, DiffusionDB and SFT sources。DrawBench evaluation generates one image per 200 prompts；T2I-CompBench searches two noises/two samples per prompt。The user-study appendix supplies only a preference figure and even describes compared outputs as videos, without participant, trial, randomization or uncertainty contract。
- **Baselines / Ablations / Sensitivity / Overhead:** authors report higher aggregate scores than tested baselines and a 500–1,000 versus 1,000–1,500 optimization-step convergence curve。Candidate-count ablation peaks around `n=3` rather than improving monotonically；path-step results improve to `m=3`, flatten at 4 and regress at 8 on most metrics。Demon and Inference-Scaling are author ports held to five minutes, Free2Guide is adapted from video pseudo-code, and the inference comparison alternates between 50-step SDXL, “default 100 NFE” and over-10,000-NFE search claims。No equal-FLOP/training-wall-time comparison, seeds, confidence, beta/reward sensitivity, reward-held-out evaluation or original-implementation parity is disclosed。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** SDXL-1.0 and 512/1024 repository options are known；paper appendix reports batch 8 but no hardware, precision, device count, gradient accumulation, wall time, peak memory, generated/decode/reward-call count, network/API cost or energy。README uses FP16, batch 1×accumulation 4 and 10,000 steps but is not an event-time run manifest。Inference NFE, latency and baseline ports use conflicting contracts；concurrency, throughput, tail latency and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' SDXL/scorer setup, selecting among multiple short denoising paths during fine-tuning reaches a different reported quality operating point while the resulting artifact can later use a standard sampler without an online reward search loop。The ablations establish within this setup that candidate/path breadth has an interior optimum and that adding training search is not monotonically beneficial。
- **What It Does Not Prove:** the experiments do not prove best end-to-end training efficiency, because each sharpening step performs multiple UNet/VAE/reward evaluations and only optimizer-step counts are compared。They do not prove arbitrary-reward alignment, human preference, scorer robustness, cross-model/modality transfer or lower lifecycle cost。Five-minute author ports and different NFE/configuration baselines are not a controlled universal inference comparison。
- **Limitations / Threats to Validity:** Equation 11 subtracts the reward gap outside `log sigmoid`；with fixed/detached rewards that term has zero gradient。Released code reproduces this structure, so reward magnitude affects logged scalar loss but only winner/loser selection affects gradient；the advertised reward-modulated DPO semantics are not implemented as stated。The code uses global `argmax/argmin` over flattened candidates, which can pair different prompts when effective batch exceeds one, while the appendix claims batch 8；it also collapses gathered timesteps to a maximum rather than preserving per-example identity。Paper/code learning rate, batch, step, beta and NFE contracts conflict；baseline ports, one-sample DrawBench, same-family reward/evaluation metrics, missing seeds and an unspecified/mislabeled user study further limit validity。
- **Trade-offs / New Failure Modes:** amortization removes request-time scorer/search dependencies and makes deployed latency predictable, but increases training generation, decode, reward and checkpoint cost and freezes one reward operating point into weights。Proxy hacking, candidate-selection bias, reference drift and loss-sign/configuration errors become artifact risks；changing policy or reward requires retraining。Global pair selection can violate same-prompt preference semantics；larger `n/m` raises memory and compute yet can regress quality。
- **Where the Previous Design Still Applies:** standard SFT remains preferable for reliable paired data and simple reproducibility；offline Diffusion-DPO remains appropriate for audited preference pairs；DDPO/online RL remains appropriate when current-policy exploration and correctly weighted reward matter；inference-time guidance/search remains useful when reward changes per request or only a small premium tier needs extra quality；unmodified SDXL remains the safest baseline when reward evidence is weak。
- **Evolution Relationship:** `Direct Evolution` for `single-timestep diffusion fine-tuning → short trajectory candidate search during training → best/worst path update → standard-cost deployed sampler`；`Alternative Branch` versus offline preference, on-policy RL and request-time search；`Layering / Dependency` between diffusion state, DPO pair semantics, evaluator identity and lifecycle cost。The next pressure is a mathematically/executably consistent objective and equal-total-compute evidence, not a larger unpriced search width。
- **ROADMAP Node:** canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）；handoffs to `TRAIN-SFT`, `TRAIN-DPO`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。Generation owns denoising trajectory/provisional-state semantics；SFT/DPO own update objectives and pair invariants；Evaluation owns scorer independence and uncertainty；Cost owns training-to-inference work transfer。
- **Target and Adjacent Chapters Read:** read Ch24 Multimodal Generative Paradigms, Ch29 SFT, Ch33 GRPO, Ch34 DPO, Ch66 Evaluation System and Ch70 Cost。Ch24 already treats denoising path, NFE, mutable state and training/inference mismatch as one contract；Ch34 requires same-prompt pair identity and executable log-ratio semantics；Ch66 rejects scorer/proxy aggregates as truth；Ch70 requires total work rather than optimizer-step slogans。
- **Existing Coverage:** current Books already contain the stable mechanism boundary: diffusion trajectory state can be optimized or searched, but proposal/reward/commit work and artifact/runtime cost must be jointly priced；DPO requires a valid same-condition pair and correct objective。This paper adds a concrete amortization branch, while its objective/configuration contradictions prevent the reported reward-modulated formula or “best efficiency” claim from entering durable prose。
- **Integration Decision:** `Disputed — Books Frozen`。Historical Books Gate remains closed；do not integrate the printed reward-modulated objective or efficiency claims。A future refinement may use only the conditional training-time-search → deployment-time-amortization branch after event-time code, pair semantics, objective gradient and equal-compute evaluation are reconciled。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；read the complete paper and official training paths；separated trajectory-state mechanism from disputed loss semantics；documented zero-gradient reward term, cross-prompt pair risk, configuration/NFE drift and unpriced training work；mapped one canonical owner and four handoffs；no Books change。
- **Open Questions:** immutable event-time commit/environment/model/data/run；exact effective batch and whether winner/loser are selected per prompt；correct reward-weighted objective and sign/beta convention；paper-to-code SFT/RLHF algorithm parity；learning-rate/batch/steps/NFE reconciliation；same-compute and wall-time baselines；UNet/VAE/reward/API call accounting；multi-seed confidence；reward/evaluator separation and adversarial proxy tests；human-study participants/trials/media/error；cross-backbone/modality/reward transfer；checkpoint/model card；latency/concurrency/energy/SLO and independent reproduction。

### Revisiting Test-time Scaling: Separating Trace Length, Sequential Revision and Parallel Coverage

- **Candidate / Week / Score:** Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities? / 2025-W08 / 26/30。
- **Source Family ID:** `o1-like-sequential-parallel-test-time-scaling`。
- **Source Type:** arXiv research paper + official evaluation repository；the work later appeared at ACL 2025, but the W08 event is locked to arXiv v1。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-17 07:21:11 UTC；v2 submitted 2025-03-03。W08 conclusions use v1；the later ACL publication records lineage, not new W08 facts。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12215v1；https://arxiv.org/abs/2502.12215；https://github.com/ZhiYuanZeng/test-time-scaling-eval。
- **Related Primary Sources:** the later author publication is https://aclanthology.org/2025.acl-long.232/；SGLang supplies the rollout runtime；OpenCompass and Qwen-Math evaluators define answer acceptance；the evaluated model artifacts are QwQ, DeepSeek-R1, R1-Distill-Qwen and LIMO。These dependencies define the experiment, but do not make output length a causal variable or evaluator agreement an oracle。
- **Access and Verification Status:** full v1 HTML, metadata, equations, tables, figures, limitations and appendices verified；current official repository, data, rollout, answer-evaluation, sequential-search and analysis paths inspected。No immutable February commit, environment/container, checkpoint digest, raw generation bundle, seeds or independent reproduction is available。Status: `Experimental`。
- **Full-read Coverage:** read metadata, Abstract, Introduction, Related Work, sequential-scaling setup, length/accuracy and self-revision analyses, forced-revision intervention, parallel-versus-sequential comparison, Shortest Majority Vote, Conclusion, Limitations and all visible appendices；inspected current repository launch, rollout, evaluation, keyword analysis, sequential search and shortest-majority implementation。The prompt appendix is absent from arXiv HTML conversion and was cross-checked against the repository rather than inferred。
- **Original Problem:** reasoning models are often described as scaling at test time because they emit longer chains of thought。The system question is whether length itself buys correctness, whether additional sequential self-revision repairs errors, and how that branch compares with spending the same nominal generated-token budget on independent candidates plus selection。
- **Why the Previous Design Was Reasonable:** a single long trajectory preserves one coherent state, reuses its prefix/KV, avoids candidate aggregation and can exploit feedback accumulated inside the trace。When external observations arrive serially, branch generation is expensive, or a strong model reliably self-corrects, sequential continuation remains a rational compute allocation。
- **Changed Constraint:** newer reasoning checkpoints expose long traces and can be forced to continue, while serving systems can also batch multiple independent samples。Test-time compute therefore needs an explicit policy over depth, width, stopping and selection rather than treating generated length as capability evidence。
- **Mechanism:** first stratify five samples per question by solution length and measure cohort accuracy；then force up to 40 continuations by removing the final answer/closing delimiter and appending whichever of `Wait` or `Alternatively` has higher next-token probability；compare that sequential branch with ten independent samples under an author-defined generated-token budget；finally cluster normalized final answers and score each answer group by `frequency / log(mean solution length)` for Shortest Majority Vote。
- **State Ownership:** model checkpoint/tokenizer/sampling config own trajectory distribution；question/prompt own condition identity；each rollout owns independent RNG and token history；sequential search owns revision index and inherited reasoning state；answer parser owns equivalence classes；selector owns final candidate choice；evaluator versions own correctness labels；runtime scheduler owns actual compute, memory and deadline envelope。Length is an observed property of a trajectory, not a correctness owner。
- **Control Flow / Data Flow:** `question → five temperature-0.7 rollouts capped at 32K → parse/evaluate answer → within-question length ranking and mixed-outcome analysis → optional forced continuation ×40 → revised answer transition statistics`，or `question → ten independent rollouts → normalize final answers → group/count/mean-length score → majority or shortest-majority selection → final evaluation`。Sequential depth and parallel width share the prompt but create different state, correlation and execution contracts。
- **Implementation Details:** authors use SGLang, temperature 0.7 and 32K maximum output；repository rollout requests `n=5` and groups generations by question。Sequential search repeatedly strips completion markers and resumes from inherited text；the analysis counts literal `Wait` and `Alternatively` as revision proxies。Current launch guidance for the full R1 uses tensor parallel 16 across two nodes, chunked prefill 8192 and memory fraction 0.8；this is current repository lineage, not a pinned W08 run manifest。Shortest Majority Vote is implemented as answer-group count divided by logarithmic average output length。
- **Evaluation Contract:** evaluated checkpoints include QwQ, DeepSeek-R1 671B, R1-Distill-Qwen 32B/14B/1.5B and LIMO；datasets are MATH-500, 90 AIME problems from 2022–2024, a random 500-example Omni-MATH subset and 198 GPQA-Diamond questions。A response is counted correct if either OpenCompass or Qwen-Math evaluator accepts it。Five samples per question support length cohorts；two- and sixteen-sample selection is reported on AIME and GPQA。No held-out dataset is reserved for deriving the length heuristic。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include natural length cohorts, correct-versus-incorrect traces within mixed-outcome questions, forced revision transitions, sequential 40-step search, parallel ten-sample pass@k/majority and shortest versus ordinary majority。Forced revision improves some shorter-starting 14B/32B/LIMO traces before oscillating, while QwQ/1.5B degrade；successful correction remains below 10% and wrong answers are often retained。Shortest Majority Vote sometimes improves ordinary majority but loses for R1-14B and QwQ on 16-sample AIME and is not significantly better on GPQA。No seed, confidence interval, significance test, equal-FLOP, same-wall-time, parser sensitivity or external-verifier ablation is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model identities, temperature 0.7, 32K output cap, five/ten samples and current full-R1 TP16/two-node launch guidance are known。Event-time GPU type/count, precision, effective batch, concurrency, prompt length, actual output-token distributions, prefill/KV cost, wall time, energy, memory peak, throughput and tail-latency SLO are Not Disclosed。The paper's “same token budget” comparison counts generated tokens, not a complete serving-cost contract。
- **What the Evidence Actually Proves:** in the authors' sampled checkpoints/datasets, longer naturally generated solutions are not a monotonic quality signal；within mixed-outcome questions, correct samples are often shorter；repeated self-continuation can preserve or introduce errors；and parallel sampling produces greater candidate coverage and often better final accuracy under the authors' generated-token accounting。Length-aware voting is a plausible conditional selector, not a universal rule。
- **What It Does Not Prove:** observed length/accuracy correlation does not prove that making an individual solution longer causes failure；length is also an outcome of difficulty, trajectory confidence and whether the model found a solution early。The experiments do not prove all reasoning models lack sequential scaling, that parallel sampling is cheaper under hardware/wall-time/SLO constraints, that shorter answers are intrinsically better, or that majority/length heuristics identify truth。`pass@k` is coverage, not selection accuracy。
- **Limitations / Threats to Validity:** five samples give noisy ranked curves；conditioning correct/incorrect length analysis on mixed-outcome questions introduces selection effects；forced `Wait`/`Alternatively` continuation is an artificial prompt intervention and lexical counts do not verify semantic self-correction。The permissive union of two answer evaluators can inflate acceptance；parser/evaluator disagreements are not reported。The heuristic is derived and evaluated on the same benchmark families, has no calibrated epsilon for very short outputs and lacks contamination, multilingual, domain-shift or independent replication evidence。The phrase “significantly outperforms” exceeds the disclosed statistical contract。
- **Trade-offs / New Failure Modes:** sequential continuation reuses state and can incorporate serial evidence, but creates correlated error, growing KV/tail latency, revision loops and answer regression。Parallel sampling increases coverage and can exploit batching, but duplicates prefill/decode state, consumes memory/concurrency and adds parser/selector failure。Majority vote fails under correlated modes；length penalties can suppress legitimately long proofs；forced continuation shifts the prompt distribution；a hard budget can truncate the final answer。
- **Where the Previous Design Still Applies:** one-pass greedy/low-temperature decode remains appropriate for deterministic low-cost tasks；single sequential reasoning remains appropriate when observations arrive serially or branch cost is high；verified sequential repair remains valuable when an external tool/process reward supplies new evidence；ordinary majority remains safer when length is not calibrated；executable verifier, pairwise judge, adaptive budget, abstention or human escalation remain alternatives when correctness matters。
- **Evolution Relationship:** `Direct Evolution` for `single unconstrained CoT → explicit sequential continuation and revision → independent parallel candidates → answer aggregation → length-aware conditional selection`；`Alternative Branch` between depth and width；`Layering / Dependency` between generation, parser, selector, verifier and scheduler。The next pressure is adaptive allocation over depth/width using calibrated evidence and a full cost/SLO contract, not a blanket preference for shorter traces。
- **ROADMAP Node:** canonical owner `MODEL-SAMPLING`（Current Ch20；Legacy Ch20）；handoffs to `AGENT-REFLECTION`, `AGENT-PLANNING`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。Sampling owns trajectory width/depth/stopping/selection policy；Reflection owns revision semantics；Planning owns search-budget allocation；Evaluation owns coverage-versus-selection evidence；Cost owns prefill/KV/concurrency/wall-time accounting。
- **Target and Adjacent Chapters Read:** read Ch20 Sampling, Ch79 Planning, Ch80 Reflection, Ch66 Evaluation System and Ch70 Cost。Ch20 already separates sequential budget forcing, parallel candidate coverage and selection；Ch79 treats search width/depth as bounded planning；Ch80 distinguishes self-critique from external verification；Ch66 requires evaluator/version/uncertainty boundaries；Ch70 rejects output tokens as a complete cost proxy。
- **Existing Coverage:** current Books already contain the stable depth-versus-width and coverage-versus-selection distinction。This paper adds a valuable negative-evidence branch: natural trace length is diagnostic rather than causal, repeated self-revision can amplify correlated error, and a cheap selector may exploit length only after workload-specific calibration。It refines the existing `MODEL-SAMPLING` argument rather than creating a new owner。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `MODEL-SAMPLING`。Historical Books Gate remains closed；future integration must preserve sequential revision's valid operating conditions and cannot turn Shortest Majority Vote into a universal policy。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；separated correlation from intervention, coverage from selection and generated tokens from lifecycle cost；reconciled main/appendix result boundaries and inspected official implementation paths；mapped one canonical owner and four handoffs；no Books change。
- **Open Questions:** immutable February commit/container/data/checkpoint/raw generations；exact model revision/tokenizer/prompt and evaluator versions；seed/retry/sampling and parser-failure distributions；same-question randomized length intervention；external-feedback sequential repair；same-FLOP/wall-time/KV/memory/concurrency comparison；selection accuracy conditional on coverage；held-out calibration for length penalty；multi-seed confidence/significance；difficulty/domain/language/contamination shifts；adaptive depth/width/stop/abstain policy；production latency/cost/energy/SLO and independent reproduction。

### AlphaMaze: A Useful SFT→GRPO Case with an Internally Contradictory Result Contract

- **Candidate / Week / Score:** AlphaMaze: Enhancing Large Language Models' Spatial Intelligence via GRPO / 2025-W08 / 18/30。
- **Source Family ID:** `alphamaze-symbolic-maze-sft-grpo`。
- **Source Type:** arXiv research paper + author model/data artifacts；no event-time code repository, immutable training environment, raw evaluation bundle or independent reproduction。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 16:05:18 UTC；v2 submitted 2025-02-21 and is the last W08 revision；v3 submitted 2025-02-25 and belongs to W09 revision lineage。This review reads v1 and v2, locks event claims to v2, and does not backport v3 changes。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14669v1；https://arxiv.org/html/2502.14669v2；https://arxiv.org/abs/2502.14669；https://huggingface.co/Menlo/AlphaMaze-v0.2-1.5B；https://huggingface.co/datasets/Menlo/Maze-Reasoning-v0.1；https://huggingface.co/datasets/Menlo/Maze-Reasoning-GRPO-v0.1。
- **Related Primary Sources:** DeepSeek-R1-Distill-Qwen-1.5B/7B supply base checkpoints；maze-dataset generates solvable 5×5 graphs；LLaMA-Factory supplies SFT；Unsloth/TRL and vLLM are stated GRPO/runtime dependencies。Current cards expose later model/data lineage, but do not prove the exact W08 experiment or reconcile the paper's result contradictions。
- **Access and Verification Status:** complete v1/v2 HTML, method, experiment, discussion, limitations, conclusion and v2 reset-data algorithms verified；current author model card and SFT/GRPO dataset viewers inspected。Core experimental claims conflict inside both W08 versions, so status is `Disputed` rather than merely incomplete。
- **Full-read Coverage:** read metadata and revision history；Abstract, Introduction, all Related Work, tokenized maze representation, baselines, SFT, reward design, GRPO pipeline, dataset construction, MazeBench, quantitative/qualitative results, Discussion, Limitations, Conclusion and v2 Appendix algorithms；inspected current model lineage, SFT/GRPO dataset sizes/schema and later hardware/run summaries。
- **Original Problem:** can a small text LLM learn spatial path planning when a maze is serialized into symbolic coordinates/walls, and does grouped policy optimization add value after supervised demonstrations teach the interface and valid trajectories？
- **Why the Previous Design Was Reasonable:** BFS/A* has exact state, deterministic transitions and optimality properties for known mazes；direct sequence SFT is cheap and auditable when demonstrations are available；step-by-step SFT can teach the serialization/protocol before RL。These remain preferable when the graph is fully observed, correctness matters or generalization beyond a narrow schema is not required。
- **Changed Constraint:** the authors want one generative policy to parse a serialized environment, emit trajectories and recover from wrong branches, while using an executable maze checker as reward。That motivates SFT for interface/behavior acquisition followed by GRPO for outcome-conditioned refinement。
- **Mechanism:** serialize each 5×5 cell as coordinate, wall and origin/target tokens；generate solvable mazes with randomized DFS；construct straight-success and synthetic wrong-path→`RESET`→correct-path demonstrations；SFT a Distill-Qwen-1.5B policy；then sample grouped outputs and combine path-step correctness, valid-movement and `<think>`-format rewards for LoRA GRPO；parse movement tokens and execute them against maze transitions for success。
- **State Ownership:** maze graph/origin/target own environment truth；serializer owns observation schema；demonstration generator owns wrong/correct path labels and reset messages；SFT checkpoint owns learned protocol；rollout group and old/reference/current policy identities should own GRPO statistics, but are not disclosed；reward functions own optimization signal；parser/simulator own executable success；checkpoint interval owns revision lineage。Natural-language chain of thought does not own spatial truth。
- **Control Flow / Data Flow:** `maze generator → graph + correct path → tokenized observation → straight/retry demonstration synthesis → SFT checkpoint → grouped GRPO rollouts → format/valid-step/path reward → LoRA update → 100-case MazeBench generation → movement parser → graph execution → success rate`。Reset demonstrations and online RL are separate training signals even though the paper sometimes attributes observed “self-correction” to GRPO。
- **Implementation Details:** v2 reports a 530K initial maze pool, 30K held-out set, balanced 250K straight + 250K retry SFT set, 150K GRPO source pool, 10 SFT epochs, LoRA GRPO in Unsloth with vLLM and checkpoints every 200 steps。Reward text states `+0.2 per solution step`, `+0.5` for valid movement tokens and `+0.25` for thinking format, but does not provide executable reward code, group size, normalization, KL, clipping, beta, learning rate, optimizer, sampling config or exact aggregation。Current cards expose 565K/182K rows and later SFT runs, creating mutable artifact drift。
- **Evaluation Contract:** MazeBench contains 100 randomly selected 5×5 mazes: 50 easy (1–4 steps), 40 medium (5–8) and 10 hard (9–13)。Outputs may contain extra text；the parser extracts movement tokens, executes them and scores success。The main v2 table reports untreated 1.5B/7B and a “Baseline-1.5B (SFT)” at 0%, AlphaMaze-SFT at 86% and AlphaMaze SFT+GRPO at 93%。No sample-level outputs, fixed benchmark manifest, decoding settings, uncertainty or independent evaluator are released。
- **Baselines / Ablations / Sensitivity / Overhead:** the paper compares base distilled models, direct-prediction SFT, step-by-step SFT and SFT+GRPO, and plots checkpoint scores。It does not isolate reset demonstrations from output format, SFT data volume, LoRA, reward components or GRPO；there is no A*/BFS control, same-data/equal-compute baseline, group-size/reward-weight sensitivity, seed, confidence interval or real ablation。The claimed “statistically significant” seven-point gain is unsupported by a disclosed statistical test；the 100-item benchmark gives only ten hard cases。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** event-time text names Distill-Qwen 1.5B/7B, LoRA and NVIDIA A6000 GPUs but omits count, precision, batch/group size, context/output length, optimizer, total rollout tokens, wall time, memory, energy and evaluation concurrency。Current model card later lists several 6×A6000 and 8×H200 SFT runs plus BF16 weights, but those mutable summaries are not a W08-pinned GRPO contract。Serving throughput, latency and SLO are Not Disclosed。
- **What the Evidence Actually Proves:** the public materials establish a concrete symbolic-maze dataflow, executable transition checker, reset-demonstration construction and an available AlphaMaze model/data family。They support SFT→outcome-RL as a plausible design branch and demonstrate that representation, parser and reward contracts jointly define the task。They do not supply a coherent numerical contract sufficient to attribute a seven-point gain to GRPO。
- **What It Does Not Prove:** the evidence does not prove that GRPO caused 86%→93%, that `<think>` denotes faithful reasoning, that self-correction emerged from RL rather than reset SFT, that distillation erased a base-model visual ability, or that text maze success transfers to images, robotics or physical navigation。A serialized graph is not raw vision；5×5 open-loop token execution is not embodied closed-loop control。
- **Limitations / Threats to Validity:** v1/v2 Abstract, Results and Discussion claim 86% SFT and 93% GRPO, while the same versions' Conclusion reports pretrained 75%, SFT 77%, says GRPO is only proposed/future work and asks future research to validate it。The table gives 0% to one SFT 1.5B baseline but 86% to another without a clean causal definition。GRPO step count alternates between 1,600 and 2,000 in v1；v2 reduces it to 1,600 but leaves the contradictory conclusion。Reward wording can favor longer valid sequences despite claiming efficiency；format reward and permissive parser can confound capability。Mutable data/model cards drift from paper counts and no event-time code/raw run closes the gap。
- **Trade-offs / New Failure Modes:** symbolic serialization makes state executable and verifier-friendly, but grows tokens, hard-codes one coordinate/wall ontology and can teach parser templates instead of transferable geometry。Reset SFT provides explicit recovery examples but may leak correction structure；GRPO removes critic state yet multiplies rollouts and reward exploitation surfaces。Step rewards can favor loops/verbosity；format rewards can dominate outcome；open-loop movement sequences cannot react to new observations；mutable datasets complicate deletion/provenance and reproduction。
- **Where the Previous Design Still Applies:** BFS/A* remains superior for fully known mazes；direct SFT remains appropriate for stable schemas and verified demonstrations；reset-augmented SFT remains a distinct cheaper branch for recovery behavior；PPO/value methods remain viable when state credit is learnable；visual encoders/VLA policies are required when perception or physical feedback is real；deterministic parsers and simulators remain final correctness authorities。
- **Evolution Relationship:** `Direct Evolution` for `deterministic graph solver / direct sequence imitation → step-by-step SFT → reset-demonstration SFT → grouped outcome optimization`；`Alternative Branch` between demonstration-based recovery and online GRPO；`Layering / Dependency` between representation, training objective, executable verifier and environment transition。Because result attribution is disputed, this is a design lineage, not validated superiority。
- **ROADMAP Node:** canonical owner `TRAIN-GRPO`（Current Ch33；Legacy Ch29）；handoffs to `TRAIN-SFT`, `MULTIMODAL-REPRESENTATION`, `AGENT-PLANNING`, `MULTIMODAL-EMBODIED-VLA` and `PLATFORM-EVALUATION-SYSTEM`。GRPO owns grouped policy update；SFT owns demonstrations/reset behavior；Representation owns symbolic schema；Planning/Embodied own graph-versus-physical control boundary；Evaluation owns executable success and causal attribution。
- **Target and Adjacent Chapters Read:** read Ch29 SFT, Ch33 GRPO, Ch23 Multimodal Representation, Ch79 Planning and Ch66 Evaluation System。Books already distinguish demonstration behavior from RL reward, group-relative estimation from verifier truth, symbolic representation from native modality input, plan text from environment transition and benchmark score from causal evidence。
- **Existing Coverage:** current Books already contain the durable mechanism and its failure boundaries；AlphaMaze adds a compact cross-layer case showing why serializer, retry demonstrations, reward and executable environment cannot be collapsed into “visual reasoning”。Its internally inconsistent results do not justify new Books prose or a mechanism update。
- **Integration Decision:** `Disputed — Weekly Only / Books Frozen`。Score falls below 20 after Source Reliability correction；Historical Books Gate is also closed。Do not integrate 86%→93%, self-correction emergence, distillation-loss or robotics-transfer claims。A future review may reconsider only if event-time code, immutable data/checkpoints and coherent raw evaluation reconcile v2。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1/v2-within-week Source Review；reconstructed data/reward/evaluation flow；separated reset-SFT behavior from GRPO attribution；documented v1/v2 internal result contradictions, mutable artifact drift and missing statistical/runtime contract；mapped one canonical owner and five handoffs；no Books change。
- **Open Questions:** immutable v2 source/data/model/container/run manifests；exact distinction among direct-SFT and AlphaMaze-SFT baselines；reconciliation of 75/77 versus 86/93 and “GRPO future work”；raw 100-case outputs/checkpoint curves；group size, old/reference policy, reward code/weights, KL/clipping/beta, sampling and optimizer；reset-SFT versus GRPO ablation；path-length optimality/loop penalties；fixed MazeBench IDs and leakage audit；multi-seed uncertainty/significance；larger/unseen topology and native visual input；closed-loop physical feedback；full compute/energy/SLO and independent reproduction。

### PAFT: From One Prompt String to a Versioned Prompt Distribution

- **Candidate / Week / Score:** PAFT: Prompt-Agnostic Fine-Tuning / 2025-W08 / 24/30。
- **Source Family ID:** `paft-prompt-distribution-sft`。
- **Source Type:** arXiv research paper；no official code repository, immutable prompt corpus, checkpoint, run manifest or independent reproduction。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 13:46:47 UTC；v2 submitted 2025-09-27 and v3 on 2025-10-17。W08 is locked to v1；later RLFT, theory, tool-use and revised efficiency claims are revision lineage and are not backported。
- **Direct Primary Sources:** https://arxiv.org/html/2502.12859v1；https://arxiv.org/abs/2502.12859。
- **Related Primary Sources:** the paper compares ordinary user-prompt SFT with TopAccuracy, BATprompt and ZOPO prompt-selection/optimization branches。Those publications define baseline ancestry, but only the PAFT v1 experiment is evidence for the reviewed result；the Hugging Face paper index is discovery metadata, not mechanism evidence。
- **Access and Verification Status:** v1 metadata, complete HTML, equations, algorithm, result tables, ablations and appendices verified。Prompt corpus, generator identities/versions, source code, checkpoint, environment, raw runs and independent replication are Not Disclosed。Status is `Experimental`。
- **Full-read Coverage:** read metadata/history, Abstract, Introduction, Related Work, candidate-prompt construction, dynamic fine-tuning algorithm, all datasets/baselines/results, inference/training-cost tables, K/epoch and prompt-count ablations, implementation appendix, prompt examples, ethics statement, Conclusion and Limitations。Later v2/v3 claims were checked only to prevent revision backporting。
- **Original Problem:** conventional SFT conditions every training example on one manually selected instruction template。A model can therefore learn the task and the accidental wording together, causing accuracy and output-format behavior to vary when a user expresses the same intent with a different prompt。
- **Why the Previous Design Was Reasonable:** one fixed prompt gives a stable interface, regular token cost, deterministic data preprocessing and a simple reproducible training contract。Selecting or optimizing one strong prompt is also cheaper when deployment owns a single versioned template and all callers pass through it。
- **Changed Constraint:** shared checkpoints serve multiple users, applications and prompt styles；the exact wording becomes a workload distribution rather than a constant。Training must therefore separate task semantics from surface form without assuming every production prompt can be centrally normalized。
- **Mechanism:** generate a candidate prompt pool using ten LLMs and few-shot/zero-shot strategies, split prompts into train/test groups, and during ordinary LoRA SFT sample one training prompt, reuse it for K gradient steps, then resample。The loss remains standard supervised next-token loss；novelty is prompt-distribution augmentation and sampling, not a new optimizer or objective。
- **State Ownership:** task examples and target labels own semantic supervision；prompt corpus, generator/version, semantic cluster and train/test partition own interface variation；the sampler and K own exposure schedule；checkpoint owns learned invariance；evaluator owns prompt-level outcome。Production gateway/template registry still owns accepted prompt versions and safety policy；the model does not own interface governance merely because it tolerates variants。
- **Control Flow / Data Flow:** task description/examples → external prompt generators and few-/zero-shot strategies → candidate prompt corpus → random train/test prompt split → sampled prompt reused for K steps + task example/label → LoRA update → one checkpoint → evaluation across 50 nominally unseen prompts → task accuracy distribution and runtime table。A production extension would add prompt telemetry, semantic clustering, drift detection and rollback rather than treating the synthetic pool as permanently representative。
- **Implementation Details:** v1 uses LLaMA3-8B with LoRA rank 8 on query/value projections, maximum sequence length 1,024, 20K SFT samples, learning rate `1e-4`, three epochs and default K=4。The method says ten LLMs each generate 20 few-shot and 20 zero-shot prompts, implying 400 prompts, then applies an 8:1 split；elsewhere the paper says over 450 prompts and 400 train/50 test prompts。The unexplained 400/450 and split-count drift is retained as a data-contract limitation。
- **Evaluation Contract:** five multiple-choice tasks are HellaSwag, PIQA, Winogrande, RACE-middle and RACE-high。All methods are evaluated on the same 50 held-out synthetic prompt strings；reported mean and standard deviation are across prompts, not across independently trained checkpoints or dataset samples。PAFT averages 87.57 ±1.57 versus 83.32 ±3.61 for the strongest listed aggregate baseline under this protocol。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines include base model, one user prompt, TopAccuracy, BATprompt and ZOPO。K∈{1,2,4,8}, K=1 with six epochs and varying prompt-pool size are explored；results suggest a broad plateau and diminishing returns, but no generator-family holdout, semantic-cluster split, adversarial/corrupted prompts, prompt-quality ablation, token-matched generic augmentation, multi-seed training, uncertainty test or independent reproduction is provided。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** the paper names A100, V100, RTX 4090 and L40 GPUs generally；the training-cost appendix explicitly reports RTX 4090 hours。Model is LLaMA3-8B, max length 1,024, LoRA rank 8, 20K samples, three epochs and learning rate `1e-4`。Precision, GPU count per run, batch/accumulation, decoding configuration, output-token counts, prompt lengths, cache state, concurrency, energy and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** within the authors' five-task, same-generator-family synthetic prompt split, training one checkpoint across prompt variants improves average accuracy and reduces prompt-to-prompt variance relative to the selected fixed/optimized-prompt baselines。It establishes prompt distribution as a trainable interface variable and shows that ordinary SFT can amortize some prompt search into the model artifact。
- **What It Does Not Prove:** it does not prove prompt agnosticism, robustness to human, adversarial, multilingual, cross-generator or production prompt shift, nor that synthetic strings represent user traffic。The 3.25× inference-time claim lacks token, hardware, precision, decoding, batch/concurrency and SLO boundaries and cannot be generalized；multiple-choice formatting/parser behavior may explain part of the runtime difference。Prompt-level standard deviation is not model-seed uncertainty, and selected-task comparisons do not establish general SOTA。
- **Limitations / Threats to Validity:** train/test prompts come from the same generator/strategy pool and are randomly split, so “unseen” primarily means string holdout rather than generator or semantic-distribution holdout。Prompt counts disagree；only ten examples are published；generator/model versions, filtering, duplicates and semantic diversity are unknown。The appendix says generation parameters were adjusted for correct output and validation was used while searching PAFT settings, leaving tuning-fairness ambiguity。No code, raw outputs, seeds, confidence tests, contamination audit or independent replication exists。
- **Trade-offs / New Failure Modes:** prompt randomization reduces dependence on one template and amortizes inference-time prompt search, but increases generation/filtering cost, training tokens and corpus lineage；poor or semantically shifted prompts can inject label ambiguity。Random sampling can under-cover hard regions, repeated K steps can correlate updates, synthetic generators can collapse style diversity, and model-side tolerance can hide unsafe or unsupported interfaces that should have been rejected by a gateway。A mutable prompt pool also needs invalidation, deletion and checkpoint lineage when policies change。
- **Where the Previous Design Still Applies:** fixed-prompt SFT remains preferable when the interface is centrally controlled, stable, safety-reviewed and latency-sensitive；single-prompt optimization remains useful when deployment has one template and retraining is costly；gateway normalization and schema validation remain necessary for strict APIs；adversarial/curriculum sampling is a later branch when random coverage misses important prompt regions。
- **Evolution Relationship:** `Direct Evolution` for `one fixed prompt → select/optimize one robust prompt → train over a prompt distribution → difficulty/adversarial/curriculum sampling → production prompt-distribution monitoring`；`Alternative Branch` between model-side invariance and gateway-side normalization；`Layering / Dependency` among prompt corpus, SFT sampler, checkpoint, evaluator and runtime interface policy。
- **ROADMAP Node:** canonical owner `TRAIN-SFT`（Current Ch29；Legacy Ch25）；handoffs to `TRAIN-DATA`, `AGENT-PROMPT`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。SFT owns prompt-distribution exposure；Data owns corpus lineage/coverage；Prompt owns runtime interface design；Evaluation owns distribution-shift evidence；Cost owns generation, training-token and serving accounting。
- **Target and Adjacent Chapters Read:** read Ch27 Data, Ch29 SFT, Ch66 Evaluation System, Ch70 Cost and Ch74 Prompt。Verified that the mechanism changes supervised training/data sampling, while runtime prompt construction, robustness evidence and lifecycle cost remain separate owners。
- **Existing Coverage:** Ch29 already treats chat template and output schema as part of the supervised interface contract；Ch74 treats prompts as versioned runtime artifacts。The missing durable branch is explicit training over a versioned prompt distribution, including generator/partition identity, semantic coverage and coexistence with gateway normalization。This is a refine candidate, not a new chapter or a claim that prompts no longer matter。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-SFT`。Historical Books Gate remains closed；future integration must retain fixed-template and gateway-normalization branches and must not copy the unbounded 3.25× runtime claim。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；reconstructed prompt-corpus/sampler/checkpoint/evaluator ownership；separated string holdout from distribution shift and task accuracy from complete serving cost；recorded prompt-count and tuning-contract drift；mapped one canonical owner and four handoffs；no Books change。
- **Open Questions:** immutable v1 prompt corpus, generator/version/filter/duplicate/semantic-cluster manifest；reconciliation of >450, 400 and 8:1 counts；generator-family/human/adversarial/multilingual holdouts；prompt-quality and token-matched augmentation ablations；K/curriculum sensitivity and multi-seed confidence；exact decoding/output/parser/runtime contract；training-token and prompt-generation API/energy cost；policy-change invalidation/deletion/rollback；production prompt drift, safety and independent reproduction。

### CoSyn: Executable Rendering Code as the Shared Data Specification

- **Candidate / Week / Score:** Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation / 2025-W08 / 28/30。
- **Source Family ID:** `cosyn-code-guided-text-rich-multimodal-data`。
- **Source Type:** arXiv research paper + author generation repository + released image/QA and pointing datasets + author evaluation datasets；no immutable W08 run bundle or independent reproduction。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 18:55:30 UTC；v2 submitted 2025-05-21 and later ACL publication belong to revision lineage。W08 claims are locked to v1。Current code/dataset cards are supporting artifact lineage and are not silently treated as the exact 20-pipeline/9-category event-time state。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14846v1；https://arxiv.org/abs/2502.14846；https://github.com/allenai/pixmo-docs；https://huggingface.co/datasets/allenai/CoSyn-400K；https://huggingface.co/datasets/allenai/CoSyn-point；https://huggingface.co/datasets/yyupenn/NutritionQA；https://huggingface.co/datasets/yyupenn/DocPointQA。
- **Related Primary Sources:** DataDreamer supplies generation-workflow lineage；Molmo supplies model architecture, crop preprocessing and human pointing baseline；PixMo-Docs is the predecessor data family。These sources define dependencies and alternatives, not independent validation of CoSyn's benchmark claims。
- **Access and Verification Status:** complete v1 HTML, formulas, all main/appendix experiments, prompts, hyperparameters and limitations verified；current official repository, dataset schemas/viewers/cards and evaluation scripts inspected。Exact W08 code commit, prompts for all pipelines, raw API responses, training checkpoint, environment/container, run logs and independent reproduction are Not Disclosed。Status is `Experimental`。
- **Full-read Coverage:** read metadata/history, Abstract, Introduction, Related Work, problem factorization, all CoSyn stages/renderers/persona design, dataset construction, model/training/evaluation setup, main results, synthetic-data/novel-domain/CoT/bias/pointing analyses, Conclusion, Limitations/Ethics, prompt/query/tool appendices, training details, diversity/scale/generator ablations and qualitative examples；inspected repository pipeline surface and four released dataset/evaluator artifacts。
- **Original Problem:** text-rich images such as charts, documents, diagrams and screenshots have sparse and biased image-question supervision。Natural collection and human annotation are expensive, while asking an LLM to describe a rendered image can introduce OCR/vision errors and weak spatial grounding before a training row even exists。
- **Why the Previous Design Was Reasonable:** curated human data offers realistic visual noise and direct task relevance；handwritten chart templates provide deterministic labels；caption-first synthetic generation is simple；ordinary in-domain SFT is strong when a stable academic dataset already matches deployment。These branches remain valuable where realism, human intent or certified labels matter more than scale。
- **Changed Constraint:** one pipeline must cheaply target many text-rich domains, create question/answer/explanation and pointing supervision, and preserve a representation from which both pixels and labels can be derived。The data system therefore needs an executable intermediate specification rather than independently generated image and text artifacts。
- **Mechanism:** factor generation as `P_LM(code | query) × P(image | code) × P_LM(text | code)`。A domain query selects a renderer-specific pipeline；persona-conditioned topic generation creates diversity；an LLM generates structured data and executable Python/HTML/LaTeX/SVG/etc.；a deterministic renderer produces the image；a second text-only LLM reads the code/data—not the pixels—to produce QA/explanation。For pointing, code is edited to render explicit target points, yielding coordinate labels tied to layout state。
- **State Ownership:** domain query/persona and pipeline version own coverage intent；generator model/prompt/sampling own code/data proposal；sandbox, dependencies, fonts/browser/renderer own pixel artifact；code/data and layout DOM own synthetic label truth relative to the specification；instruction model owns language transformation；dataset manifest owns row/source/license lineage；model checkpoint owns learned behavior；benchmark/evaluator owns reported outcome。Neither rendered code nor generated explanation owns real-world truth outside the encoded ontology。
- **Control Flow / Data Flow:** target domain → persona/topic → structured content → LLM-generated executable code → isolated renderer/dependency state → image + code/data lineage → LLM-generated question/answer/explanation → validation/filtering → versioned image/text dataset → VLM SFT → benchmark/pointing evaluator。For production-quality generation, code execution, renderer output and label consistency require separate admission gates and reproducible environment identities。
- **Implementation Details:** v1 describes 20 pipelines over 11 tools and nine categories, with 400K images and 2.7M instruction rows；Claude-3.5-Sonnet generates content/code and GPT-4o-mini generates instructions through DataDreamer caching/parallel workflows。The released repository currently exposes 25 pipelines, Python 3.10, external API keys and renderer/browser dependencies；the current CoSyn-400K card exposes 408,227 rows across ten subsets, while CoSyn-point exposes about 68.1K train rows versus v1's 65K。These are explicit artifact evolution, not corrections backdated into W08。
- **Evaluation Contract:** a CLIP ViT-L/14 336 vision encoder, MLP connector and Mistral-7B LLM follow Molmo preprocessing/training；dense-caption pretraining precedes SFT。The best supervised run mixes 138K evaluation-dataset images, roughly 1.1M auxiliary academic images and 400K synthetic images；the zero-shot row excludes evaluation training splits but uses auxiliary+synthetic data。Seven text-rich benchmarks use heterogeneous official metrics。NutritionQA is 50 real label photos with two questions each (100 examples in paper accounting) and an LLM-based semantic scorer；ScreenSpot and DocPointQA evaluate coordinate predictions。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include several open VLMs and proprietary APIs, data-mixture ablations, CoT versus short answers, human versus machine ChartQA slices, 7K targeted nutrition data, synthetic versus PixMo human pointing, single versus multiple render tools at 45K images, dataset scale and Claude versus GPT-4o generation at 100K charts。There is no full factorial over generator, prompt, persona, renderer, filter, data volume and model seed；no equal-token/equal-compute comparison to human or ordinary synthetic data；and no independent code-image-label audit rate。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** final training uses one TPU v3-128, batch 32, maximum sequence length 2,304, learning rate `1e-6`, 60K steps, 200 warm-up steps, cosine end factor 0.1 and about 30 hours；training crops are capped at 12 and test crops at 25。Precision, optimizer details, checkpoint size, API-generation concurrency/rate limits, renderer CPU/browser resources, data-filter cost, VLM inference batch/concurrency, TTFT/TPOT, energy and production SLO are Not Disclosed。Dataset generation cost is approximately $8,000 under historical provider pricing, not a portable cost constant。
- **What the Evidence Actually Proves:** under the authors' model and benchmark protocol, code-mediated synthetic data contributes incremental value beyond auxiliary/evaluation datasets, broad renderer diversity improves the tested ChartQA slice, and synthetic pointing can complement human pointing data。The released schema demonstrates a durable data-engineering pattern: preserve code, structured data, render output and QA together so a row's synthetic provenance can be inspected rather than storing only image-answer pairs。
- **What It Does Not Prove:** it does not prove pixels/labels are correct in reality, that code-guided data eliminates hallucination, that synthetic data generally beats human data, or that the model is a safe GUI Agent。The best model is trained on benchmark training data and is not a clean zero-shot comparison；proprietary baselines have unknown training exposure and different prompting。Coordinate accuracy is not tool authorization or completed action。CLIP/SBERT pairwise distance is a proxy, not semantic coverage, and 400K scaling on one chart workload is not a universal law。
- **Limitations / Threats to Validity:** generator and instruction model can share factual/style bias with filters；renderer and label derive from the same code ontology, so specification bugs can make image and answer consistently wrong。Real images contain camera, scan, font, occlusion, layout and cultural variation absent from renderers。English-only data, 100-example NutritionQA, 300-pair DocPointQA, heterogeneous metrics, checkpoint selection on validation, no seeds/confidence and likely benchmark/data contamination limit generalization。The NutritionQA scorer is another model and its exact semantic operating point is not human-calibrated in the paper。
- **Trade-offs / New Failure Modes:** executable code improves alignment, controllability, replay and cheap coordinate labels, but introduces untrusted-code execution, dependency/font/browser drift, nontermination/resource abuse, secret exposure, renderer nondeterminism and licensing/provider-policy lineage。Persona/tool diversity increases coverage but can amplify stereotypes and duplicated semantic templates；more test crops improve fine text evidence while increasing inference cost。Targeted synthetic data speeds domain adaptation but can overfit a synthetic visual style and requires domain experts to specify missing cases。
- **Where the Previous Design Still Applies:** human annotation remains necessary for real-world intent, ambiguity, safety and visual noise；hand-authored deterministic templates remain best for narrow regulated schemas；natural-data SFT remains stronger when representative examples are abundant；caption/image-conditioned generation remains useful when no executable specification exists；fixed render environments remain preferable for reproducible regression even if they reduce diversity。
- **Evolution Relationship:** `Direct Evolution` for `human/curated multimodal rows → handcrafted programmatic templates → LLM-generated annotations → code as shared image/label specification → targeted domain synthesis → failure- and production-distribution-driven generation`；`Layering / Dependency` among generator, sandbox/renderer, manifest, SFT and evaluator；`Alternative Branch` between executable synthetic specification and natural human evidence。
- **ROADMAP Node:** canonical owner `TRAIN-DATA`（Current Ch27；Legacy Ch23）；handoffs to `MULTIMODAL-REPRESENTATION`, `TRAIN-SFT`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-SECURITY`, `AGENT-TOOL` and `PLATFORM-COST`。Data owns row specification/provenance；Representation owns pixel/token identity；SFT owns optimization；Evaluation owns benchmark/grounding claims；Security owns generated-code execution；Tool owns action authority；Cost owns API/render/train/inference accounting。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch27 Data, Ch29 SFT, Ch66 Evaluation System, Ch70 Cost, Ch72 Security and Ch78 Tool Calling。Verified that the canonical mechanism is dataset specification/compilation, while pointing, executable-code security, evaluation and downstream action remain handoffs rather than duplicate owners。
- **Existing Coverage:** Ch27 already develops synthetic data from generate-and-filter toward Specification Compilation, but mostly through task/sandbox/tool state；CoSyn adds a strong multimodal branch in which executable render code jointly derives observation and label, plus the important failure that shared deterministic ontology can be consistently wrong。This can refine the existing evolution without adding a paper-summary section or claiming synthetic replacement of human data。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `TRAIN-DATA`。Historical Books Gate remains closed；future integration should add executable rendering as a conditional multimodal specification branch, preserve human/natural data and enforce sandbox, lineage and independent real-data evaluation。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；jointly audited paper, current generator repository, released dataset schemas and evaluation artifacts；separated event-time 20-pipeline/9-category claims from later 25-pipeline/10-subset artifact evolution；bound benchmark numbers to model/data/hardware/evaluator contracts；mapped one canonical owner and six handoffs；no Books change。
- **Open Questions:** immutable W08 code/prompt/model/API/environment/data manifests；all-pipeline execution/label error and rejection rates；sandbox/resource/network/secret policy；font/browser/renderer determinism；source/license/deletion lineage across provider terms；generator/persona/render/filter factorial and multi-seed evidence；human audit of factual, cultural and safety errors；real-image domain shift；independent NutritionQA scorer calibration；coordinate-to-action verification；full API/render/filter/train/inference cost, energy and SLO；independent reproduction。

### LServe: From Dense Paged KV to Profiled, Selected and Quantized History

- **Candidate / Week / Score:** LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention / 2025-W08 / 28/30。
- **Source Family ID:** `lserve-unified-hybrid-sparse-attention`。
- **Source Type:** arXiv systems paper + official project page + official OmniServe implementation repository；later MLSys 2025 acceptance and arXiv v2 lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 18:59:52 UTC；v2 submitted 2025-04-21。W08 is locked to v1；MLSys status and the current OmniServe repository are supporting publication/artifact lineage, not evidence that today's main branch equals the February experiment。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14866v1；https://arxiv.org/abs/2502.14866；https://hanlab.mit.edu/projects/lserve；https://github.com/mit-han-lab/omniserve。
- **Related Primary Sources:** QServe supplies the W4A8KV4 serving base；DuoAttention supplies offline retrieval/streaming-head identification；Quest supplies query-aware min/max page selection；MInference supplies a prefill-sparsity comparison；vLLM 0.6.3 supplies the dense PagedAttention baseline。These dependencies define the mechanism lineage, but do not independently validate LServe's end-to-end claims。
- **Access and Verification Status:** complete v1 HTML, formulas, system design, all evaluation/analysis sections and current official project/repository documentation verified。No immutable W08 commit/tag, converted model/profile artifact, raw run bundle, container or independent reproduction is published；the current repository integrates later QServe/LServe work and cannot be treated as an event-time snapshot。Status is `Experimental`。
- **Full-read Coverage:** read metadata/revision history, Abstract, Introduction, Background/Motivation, complete unified-sparsity design, static-head profiling, two-way KV paging, hierarchical page selection, reusable selection and CUDA indexing, all accuracy/efficiency tables and analyses, Related Work and Conclusion；inspected the official project page, installation contract, benchmark parameters, evaluation entry points and current OmniServe implementation surface。
- **Original Problem:** long-context inference has two different attention bottlenecks: Prefill repeatedly traverses a quadratic query-key region, while Decode reads an ever-growing KV history and becomes memory-bound。Quantization reduces bytes per iteration but not the number of iterations；prefill-only or decode-only sparsity leaves the other stage dominant。
- **Why the Previous Design Was Reasonable:** dense attention preserves every historical interaction and is the safest default for diffuse retrieval/aggregation；ordinary PagedAttention solves allocation and fragmentation without changing model semantics；KV quantization improves bandwidth without deleting history；static streaming masks are cheap and predictable；query-aware page selection preserves global candidates。Each remains preferable when exactness, broad model support, low setup cost or simple cache identity outweighs peak long-context throughput。
- **Changed Constraint:** contexts reach 64K–512K, long generation can make Decode dominate, quantized KV needs large physical pages for bandwidth, and dynamic relevance estimation needs small groups for discrimination。The serving system must therefore reconcile semantic selection granularity with hardware transfer granularity and optimize Prefill and Decode under one cache contract。
- **Mechanism:** offline DuoAttention-style gates rank heads and convert a target fraction, normally 50%, into sink-plus-local streaming heads；remaining retrieval heads stay dense during Prefill and use query-aware dynamic sparsity during Decode。LServe stores the two head groups in separate paged KV systems, adds per-logical-page channel-wise key min/max summaries, max-reduces logical scores into physical-page scores, selects top-K physical pages under a 4,096/8,192-token budget, and fuses static/dynamic sparse patterns with quantized attention kernels。
- **State Ownership:** model/checkpoint, adapter and quantization profile own tensor semantics；offline gates, threshold and sparsity quantile own head class；Prefill owns KV writes and min/max summaries；logical-page schema owns selection granularity；physical allocator/block table owns addresses and transfer granularity；page selector owns per-query selected pages and reuse epoch；sparse kernel consumes the decision。Scheduler, admission, fairness and request lifecycle remain external owners。
- **Control Flow / Data Flow:** `model + calibration/profile → head gates → retrieval/streaming partition → Prefill fused block-sparse attention → separate dense/streaming paged KV + logical-page summaries → Decode query → logical-page scores → max reduction to physical pages → top-K page table → reuse for C tokens → two-level sparse/quantized attention kernel → output token + updated KV/summary`。Changing any model/profile/page/budget identity invalidates reuse assumptions。
- **Implementation Details:** v1 implements CUDA/PTX kernels on QServe and TensorRT-LLM, compiled as PyTorch extensions。An iterator abstraction skips empty Prefill tiles；Decode uses physical iteration indices plus logical token indices, while streaming heads receive only sink/local entries。The current OmniServe repository exposes `static_sparsity`, sparse Prefill/Decode modes, `dynamic_attn_budget`, selection interval and sub-chunk/page controls, plus LongBench/NIAH and efficiency scripts；it requires specialized CUDA and block-sparse-attention builds。
- **Evaluation Contract:** models are Llama-3-8B GQA, Gradient long-context Llama-3-8B, Llama-2-7B MHA and Minitron-4B, with context up to 512K。Primary testbed is a server with 8 A100 80GB GPUs, two AMD EPYC 7763 CPUs（128 cores total）and 2TB RAM；some tests use one L40S 48GB。Software is PyTorch 2.5.0, CUDA 12.4 and cuDNN 9.2。Accuracy uses LongBench, NIAH and RULER；performance reports TTFT, per-token latency and throughput against vLLM 0.6.3, QServe, MInference, DuoAttention and Quest。
- **Baselines / Ablations / Sensitivity / Overhead:** baselines use W8A8 when supported, while QServe/LServe combine W4A8KV4 lineage with sparsity；Quest is limited to Llama-2 MHA。Ablations isolate static/dynamic sparsity, hierarchical logical-versus-physical pages, 4K/8K budgets and reuse intervals 1–16。At 128K, selector latency is 0.24ms versus 0.12ms sparse attention；reuse interval 4 cuts selector calls but RULER at 64K is 85.6/85.5 versus dense 86.8。No head-ratio/profile-dataset sensitivity, multi-seed uncertainty, equal-quality frontier, scheduler interaction or production trace is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** single-layer and end-to-end evidence spans A100 80GB and L40S 48GB, named 4B/7B/8B models and 4K–512K contexts；the QServe page-size microbenchmark uses Llama-3-8B, batch 32 and one A100；the speed-breakdown uses Llama-3-8B, batch 1。Main normalized throughput figures do not disclose a complete per-point batch/concurrency/output-length contract in the HTML；request arrival distribution, TTFT/TPOT percentiles, multi-tenant fairness, energy and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' kernels, profiles, models, hardware and benchmark workloads, static head sparsity, dynamic page selection and KV quantization can compose and improve tested long-context Prefill/Decode performance。The hierarchical page design recovers much of the accuracy lost when quantized physical pages are too coarse for importance estimation。LongBench averages remain close, while RULER explicitly exposes budget-dependent losses rather than proving exact equivalence。
- **What It Does Not Prove:** it does not prove that a constant KV budget preserves arbitrary long-context tasks, that hybrid sparsity is a universal “free lunch”, or that every model has 50% safely streamable heads。At 256K RULER, the 4K budget scores 75.7 versus dense 79.4；Qasper and SamSum also regress。The attention kernel may have bounded selected-token work, but the page selector remains linear in context。Microbenchmarks and normalized throughput do not establish multi-request tail SLO, fleet cost, fault recovery or general framework superiority。
- **Limitations / Threats to Validity:** the paper calls LongBench “10 benchmarks” while its visible table contains eight task rows；Figure 16's caption reports up to 4.5× dynamic-sparsity end-to-end speedup while the adjacent prose reports 7.7× at 256K。The paper asserts no significant reuse degradation without a disclosed significance test。Offline head classification may overfit calibration prompts；NIAH under-tests diffuse attention；average scores hide task/slice losses；baseline precision and supported architectures differ；no event-time artifact or independent reproduction closes implementation drift。
- **Trade-offs / New Failure Modes:** converting heads and pruning pages reduces work and memory traffic but makes attention approximate and model-profile-specific。Small logical pages improve selection, while large physical pages preserve bandwidth but pull unimportant neighbours into the budget。Min/max summaries add metadata and selection error；reuse can miss abrupt topic changes；separate head caches complicate prefix reuse, migration, invalidation and adapter identity；specialized kernels increase hardware/compiler maintenance。Quantization and sparsity errors can compound even when their speed mechanisms are orthogonal。
- **Where the Previous Design Still Applies:** dense PagedAttention remains preferable for exact retrieval, diffuse aggregation, unprofiled or rapidly changing models；KV-only quantization remains simpler when bandwidth dominates but deletion risk is unacceptable；static streaming remains useful for predictable local workloads；dynamic selection without head conversion fits models whose head roles are unstable；CPU/offloaded/tiered KV and retrieval-index approaches remain alternatives when capacity, not on-GPU attention work, is dominant。
- **Evolution Relationship:** `Direct Evolution` for `dense contiguous KV → paged dense KV → quantized pages → static head specialization → query-aware selected pages → logical/physical hierarchical paging → selection reuse + fused hybrid kernel`；`Layering / Dependency` among model profile, KV identity, allocator, selector and execution kernel；`Alternative Branch` versus exact dense, tiered/offloaded KV and external retrieval。The next pressure is selector asymptotics, adaptive quality budgets, profile drift, cache identity and scheduler-visible approximation policy。
- **ROADMAP Node:** canonical owner `INFER-KV-CACHE`（Current Ch45；Legacy Ch41）；handoffs to `MODEL-LONG-CONTEXT`, `INFER-PREFILL`, `INFER-DECODE`, `INFER-PAGED-ATTENTION`, `INFER-TENSORRT-LLM`, `INFER-SCHEDULING` and `PLATFORM-EVALUATION-SYSTEM`。KV owns history identity/selection state；Prefill/Decode own phase dataflow；PagedAttention owns logical/physical allocation；execution owns kernels；Scheduling owns request policy；Evaluation owns quality/SLO frontier。
- **Target and Adjacent Chapters Read:** read Ch22 Long Context, Ch43 Prefill, Ch44 Decode, Ch45 KV Cache, Ch47 PagedAttention, Ch49 execution plan/TensorRT-LLM, Ch56 Inference Scheduling and Ch66 Evaluation System。Verified that LServe's durable owner is selected KV history rather than a new framework chapter；kernel details and allocator semantics remain handoffs。
- **Existing Coverage:** current Books already explain KV as mutable request state, paging as logical-to-physical mapping, compression/eviction as conditional approximation and execution kernels as hardware-specific realization。LServe adds a useful missing evolution: semantic selection granularity and physical transfer granularity can be decoupled, but doing so introduces profile, summary, selection and reuse identities that must travel with the cache。It refines the KV-selection argument instead of becoming a product list。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `INFER-KV-CACHE`。Historical Books Gate remains closed；future integration may add hierarchical semantic/physical paging and selector-asymptotic pressure as an experimental branch, while preserving exact dense, quantized-only and tiered/offloaded alternatives。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；jointly audited paper, project page and current OmniServe artifact；reconstructed state/control flow and workload contract；recorded RULER/task losses, selector linearity, paper count/speedup inconsistencies and artifact drift；mapped one canonical owner and seven handoffs；no Books change。
- **Open Questions:** immutable W08 code/profile/model/container/run digests；calibration corpus and head-gate/threshold sensitivity；per-model/profile invalidation and adapter compatibility；exact W4A8KV4 conversion contract；raw main-figure batch/output/concurrency settings；quality-aware/adaptive token budgets；diffuse retrieval, code, Agent and adversarial long-context slices；selection-summary accuracy and abrupt-topic reuse failures；prefix sharing/migration/recovery semantics for split caches；multi-GPU/disaggregated serving；tail TTFT/TPOT/fairness/cost/energy；independent reproduction；reconciliation of eight-versus-ten tasks and 4.5×-versus-7.7× claims。

### From RAG to Memory: From Flat Similarity to Derived Relational Retrieval

- **Candidate / Week / Score:** From RAG to Memory: Non-Parametric Continual Learning for Large Language Models / HippoRAG 2 / 2025-W08 / 28/30。
- **Source Family ID:** `hipporag2-derived-relational-retrieval`。
- **Source Type:** arXiv research paper + official author implementation repository；later ICML 2025 and arXiv v2 lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-20 18:26:02 UTC；v2 submitted 2025-06-19。W08 is locked to v1；the later ICML status, repository capabilities and documentation are supporting lineage, not evidence that the mutable main branch reproduces the February run bit-for-bit。
- **Direct Primary Sources:** https://arxiv.org/html/2502.14802v1；https://arxiv.org/abs/2502.14802；https://github.com/OSU-NLP-Group/HippoRAG。
- **Related Primary Sources:** HippoRAG supplies the earlier phrase-graph and Personalized PageRank branch；NV-Embed-v2 supplies the main dense retriever；RAPTOR, LightRAG and GraphRAG are structure-augmented baselines。These sources define the comparison lineage but do not independently validate HippoRAG 2's authors' results。
- **Access and Verification Status:** complete v1 HTML, equations, tables, all appendices and current official repository documentation verified。No immutable W08 tag/commit, environment image, raw run bundle or independent reproduction is published；the current repository contains later vector-store, provider, update and deletion surfaces that must not be backdated into v1。Status is `Experimental`。
- **Full-read Coverage:** read metadata and revision history, Abstract, Introduction, Related Work and Background, complete indexing and retrieval method, recognition-memory filter, query-to-triple design, passage-node graph, PPR reset construction, experiments, cost analysis, ablations, sensitivity, error analysis, prompts, dataset details, limitations, conclusion and all result-bearing appendices；inspected the current official repository structure, reproduction entry points and release chronology。
- **Original Problem:** dense RAG is strong at direct factual lookup but treats passages as independent neighbours, while graph RAG can expose associative multi-hop structure yet often degrades simple factual retrieval or incurs expensive ontology construction。The system needs a way to retain dense evidence paths while deriving relational traversal without turning generated graph state into fact authority。
- **Why the Previous Design Was Reasonable:** lexical or dense top-k retrieval has simple ownership, update, deletion and latency semantics and remains strong when the answer is locally contained；earlier entity/phrase graphs can connect dispersed evidence and Personalized PageRank can surface multi-hop paths；hierarchical summaries can compress large corpora。Each avoids some of the model calls and mutable derived state introduced by the combined pipeline, and remains preferable for small, frequently changing, authorization-heavy or single-hop corpora。
- **Changed Constraint:** benchmark queries mix direct and associative evidence, relation wording varies across passages, a query may not name the graph's canonical entities, and every passage must remain reachable even when OpenIE misses a relation。A single similarity score or entity-only seed path therefore cannot preserve both factual recall and graph traversal under one retrieval contract。
- **Mechanism:** offline, an LLM performs schema-less OpenIE over passages, phrase nodes form an open graph, embedding similarity adds synonym edges above threshold 0.8, and passage nodes connect to their extracted phrases through `contains` edges。Online, the query is scored against passages and triples；the top five triples enter an LLM filter, accepted triples supply at most five phrase seeds, every passage also receives a dense-similarity reset score weighted by 0.05, and PPR with damping 0.5 ranks passage nodes。If no triple survives filtering, the path falls back to dense passage retrieval。
- **State Ownership:** source passage, document version, tenant and ACL own authoritative evidence；OpenIE model/prompt/version own derived triples；embedding model and synonym threshold own phrase equivalence edges；graph schema/build version own phrase, passage, synonym and contains edges；filter model/prompt own accepted query seeds；PPR reset weights and damping own traversal；index release owns the retrievable snapshot；the reader owns answer generation。The graph is a derived retrieval view, not a fact or user-memory authority。
- **Control Flow / Data Flow:** `versioned passages → OpenIE triples + phrase nodes → embedding-based synonym edges → passage nodes + contains edges → query → passage/triple embedding scores → top-5 triples → LLM recognition filter → phrase seeds + weighted dense passage seeds → PPR → ranked passages → bounded reader context → answer + source references`。A zero-seed filter result takes the explicit dense fallback；source, graph, filter and retriever identities must remain recoverable from the query trace。
- **Implementation Details:** the paper uses query-to-triple retrieval instead of NER-to-node or query-to-node, averages scores when multiple accepted triples map to one phrase, and optimizes the filter prompt with DSPy MIPROv2。Hyperparameters are tuned on 100 MuSiQue training examples；temperature is zero。The current repository implements a broader later system and offers reproduction/config surfaces, but without an event-time tag it is artifact lineage rather than a frozen W08 executable contract。
- **Evaluation Contract:** the paper samples 1,000 questions each from NQ, PopQA, MuSiQue, 2Wiki and HotpotQA, 124 from LV-Eval and 293 from ten NarrativeQA documents；corpora range from 4,111 to 22,849 passages。Retrieval uses passage Recall@5；QA uses token F1 and appendix exact match。The main extractor/filter/reader is Llama-3.3-70B-Instruct and the retriever is NV-Embed-v2；structure baselines are reproduced with the same LLM/retriever where applicable。
- **Baselines / Ablations / Sensitivity / Overhead:** QA F1 averages 59.8 for HippoRAG 2 versus 57.0 for NV-Embed-v2；Recall@5 averages 78.2 versus 73.4。The full multi-hop Recall@5 average is 87.1, versus 74.6 for NER-to-node, 59.6 for query-to-node, 81.0 without passage nodes and 86.4 without the LLM filter；the filter therefore adds only 0.7 points in that table。Passage-node weight 0.05 is selected from a sensitivity sweep；GTE, GritLM and NV retrievers improve on a MuSiQue subset after graph augmentation。No update/delete, contradiction, ACL, adversarial-poisoning, long-term growth, multilingual or production-latency ablation is reported。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Llama-3.3-70B-Instruct runs through vLLM tensor parallelism on four H100 GPUs；indexing 11,656 MuSiQue passages is reported at about 1.1 seconds per passage。A GPT-4o-mini-2024-07-18 Batch API alternative finishes in under 24 hours and under two US dollars under event-time pricing。HippoRAG 2 consumes 9.2M input and 3.0M output indexing tokens versus RAPTOR 1.7M/0.2M, LightRAG 68.5M/18.3M and GraphRAG 115.5M/36.1M。Precision, exact GPU batch, graph CPU/RAM/storage, online query latency, concurrency, energy, failure recovery and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' seven QA corpora, named retriever/LLM and retrieval/reader protocol, mixing dense passage seeds with derived phrase-graph traversal improves the reported average Recall@5 and QA F1。Passage nodes materially recover evidence that phrase-only traversal misses；query-to-triple seeding is much stronger than the tested entity/node alternatives；the same graph mechanism improves three tested retrievers on a MuSiQue subset。The paper's roughly 7% associative-memory claim is a selected multi-hop comparison, not a universal RAG gain。
- **What It Does Not Prove:** it does not prove human-like memory, general continual learning, online knowledge revision or that graph RAG replaces dense retrieval。There is no temporal stream, contradictory fact, supersession, deletion, authorization, rollback or replay experiment。The resource claim is only relative to LightRAG/GraphRAG: RAPTOR uses far fewer reported indexing tokens。QA/retrieval averages do not establish claim faithfulness, production latency, cost per good answer or safe multi-tenant operation。
- **Limitations / Threats to Validity:** OpenIE, synonym linking and LLM filtering can create correlated extraction and relevance errors；hyperparameters tuned on 100 MuSiQue examples may not transfer；fixed corpora hide change propagation and graph drift；average QA F1 and Recall@5 hide slice losses, including PopQA where the earlier HippoRAG is higher。Eighteen percent of filter cases produce no triples and fall back to dense retrieval；in half the examined failures at least half the linked phrase nodes already occur in supporting documents, so traversal/ranking still fails。Appendix Table 11 visibly pairs a Philippe-family query with Bank of America/FleetBoston triples, an artifact-integrity warning that is recorded rather than silently corrected。
- **Trade-offs / New Failure Modes:** graph augmentation increases associative paths but adds OpenIE cost, synonym calibration, mutable graph identity, PPR work and extra LLM filtering。Passage nodes protect dense recall but can dominate graph signals；synonym edges improve recall but can connect unrelated senses；PPR can amplify a wrong high-centrality bridge；dense fallback improves robustness but makes cost and quality path-dependent。Updates and deletion must invalidate triples, synonym links, contains edges, embeddings, caches and query traces；authorization filtering can disconnect paths and change rankings。
- **Where the Previous Design Still Applies:** dense or lexical top-k remains preferable for local evidence, high update frequency, strict ACL/delete propagation, low-latency serving or limited indexing budget；the earlier phrase graph remains viable when entity relations dominate and dense passage recall is less important；hierarchical summaries remain useful for coarse navigation；manual knowledge graphs remain appropriate where schema correctness and curation justify their cost。HippoRAG 2 is an additional branch, not a replacement hierarchy。
- **Evolution Relationship:** `Direct Evolution` for `dense passage similarity → phrase-graph retrieval → synonym-linked open graph → passage nodes that preserve dense evidence → mixed phrase/passage PPR seeds → explicit dense fallback`；`Layering / Dependency` among source corpus, derived graph, retriever, filter, PPR and reader；`Explanatory Analogy` to hippocampal memory, not mechanism proof；`Alternative Branch` versus lexical/dense top-k, curated KG and hierarchical summaries。The next pressure is governed incremental maintenance, source-level provenance, authorization-aware traversal, path-dependent SLO and measured answer faithfulness。
- **ROADMAP Node:** canonical owner `AGENT-RAG`（Current Ch76；Legacy Ch72）；handoffs to `AGENT-CONTEXT`, `AGENT-MEMORY`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-SECURITY` and `PLATFORM-COST`。RAG owns derived retrieval/index state；Context owns bounded visibility；Memory begins only when durable write/revision/forgetting semantics exist；Evaluation owns corpus/index/retriever/reader identity；Security owns ACL/delete propagation；Cost owns indexing and path-dependent query work。
- **Target and Adjacent Chapters Read:** read Ch75 Context's derived-view validity and bounded assembly, Ch76 RAG's ingestion, graph-grounded traversal, freshness/deletion and evaluation handoffs, Ch77 Memory's write/read/consolidate/supersede/delete boundary, Ch66 Evaluation System's versioned RAG subject contract, Ch70 Cost's outcome-bound resource accounting and Ch72 Security's ACL/delete-chain contract。This confirms that the paper refines RAG retrieval mechanics and only borrows a memory analogy。
- **Existing Coverage:** Books already state that embedding vectors and graph nodes are derived views, source evidence remains authoritative, online graph traversal has provenance/update/ACL/tail-latency costs, and RAG must not be conflated with durable Agent Memory。HippoRAG 2 adds a concrete missing mechanism chain: passage nodes and weighted dense reset mass can preserve factual retrieval while phrase seeds enable associative traversal, with an explicit zero-seed fallback。It should later refine the existing graph-grounded section, not create a paper list or a Memory chapter claim。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` in `AGENT-RAG`。Historical Books Gate remains closed；future integration may add mixed dense/relational reset state and fallback semantics as an experimental branch, while preserving dense, lexical, curated-KG and summary alternatives and explicitly rejecting the paper title as proof of durable Memory。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；audited the full paper, all result-bearing appendices and current official repository；reconstructed source/derived-state ownership and control flow；bound gains and costs to the disclosed contract；recorded filter fallback, table-integrity, maintenance and no-continual-learning boundaries；mapped one canonical owner and five handoffs；no Books change。
- **Open Questions:** immutable W08 code/config/container/model/index/run digests；exact v1 dataset preprocessing and released query/corpus hashes；OpenIE/filter error audit and independent human labels；Appendix Table 11 provenance；passage-node/phrase-seed/PPR sensitivity beyond MuSiQue tuning；online query latency, graph CPU/RAM/storage and path-dependent cost；incremental update, contradictory facts, source revision, delete-chain and ACL semantics；poisoning, multilingual/domain shift and long-term graph growth；claim faithfulness and abstention；multi-seed uncertainty and independent reproduction。

### LoRAM: Decoupling the Training Carrier from the Inference Base

- **Candidate / Week / Score:** Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models / LoRAM / 2025-W08 / 24/30。
- **Source Family ID:** `loram-pruned-training-full-base-inference`。
- **Source Type:** arXiv research paper + official author repository + current training/recovery code；later ICLR 2025 and arXiv v2 lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 08:39:15 UTC；v2 submitted 2025-03-15。W08 is locked to v1；v2/ICLR identity and current repository are later evidence lineage。The mask/recovery equation conflict remains visible in v2 and therefore is not resolved by publication revision。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13533v1；https://arxiv.org/abs/2502.13533；https://github.com/junzhang-zj/LoRAM；https://github.com/junzhang-zj/LoRAM/blob/main/loram/2_pruned_low_rank_matrix_training.py；https://github.com/junzhang-zj/LoRAM/blob/main/loram/3_recovered_low_rank_matrix_generation.py。
- **Related Primary Sources:** LoRA defines low-rank task updates；QLoRA reduces frozen-base storage；LLM-Pruner supplies the structured pruning path；SparseGPT supplies semi-structured/unstructured paths。They establish the mechanism lineage but do not independently reproduce LoRAM's recovered-adapter results。
- **Access and Verification Status:** complete v1 HTML, equations, all main/appendix experiments and current official training/recovery scripts verified。No immutable W08 tag, dependency lock, preprocessed dataset, aligned-pruned checkpoint, recovered adapter, raw run or container is published。The paper's core recovery formula conflicts with its mask definition, and the visible current q-projection recovery branch appears not to copy retained adapter values into the zero-initialized tensor。Status is `Disputed — Recovery Contract`；Books frozen。
- **Full-read Coverage:** read metadata and revision history, Abstract, Introduction, complete LoRA/prune/train/recover/align/quantize method, equations and algorithm, all convergence/downstream/recovery/alignment/scaling experiments, full experimental details, dimension/update visualizations, learning-rate tuning, domain task, cost analysis and trend appendix；inspected the current official repository layout, training code, structured recovery code and run documentation。
- **Original Problem:** LoRA reduces trainable gradients and optimizer state but still must load the full frozen base for every forward/backward pass；at 70B scale this base-storage term can dominate low-resource adaptation。Quantizing the same full base helps, yet the training carrier remains the deployment model even when many coordinates receive little task-specific update。
- **Why the Previous Design Was Reasonable:** ordinary LoRA trains and evaluates the adapter against the same base identity, so forward semantics, shapes, merge and rollback are simple；QLoRA further reduces frozen storage while preserving that identity；full fine-tuning retains maximum update freedom；training a smaller model is operationally simple when smaller inference quality is acceptable。These branches avoid LoRAM's pruning mask, alignment checkpoint and cross-shape adapter recovery contract。
- **Changed Constraint:** users want to customize a large inference model under a much smaller training-memory budget, while publishers can amortize one-time preprocessing/alignment across many downstream adapters。This permits separating the model that carries optimization from the base that later consumes the learned delta, but makes train-to-serve compatibility a first-class artifact problem。
- **Mechanism:** a publisher prunes the full base using random structured, LLM-Pruner structured, SparseGPT 4:8 semi-structured or unstructured pruning；optionally continues pretraining the pruned base on FineWeb/OpenWebMath to reduce knowledge mismatch and quantizes it to NF4。A user trains rank-8 LoRA factors on that pruned/aligned carrier。For structured pruning, recovery expands factor dimensions, zero-fills removed neuron/head coordinates and copies learned coordinates back into the full shape；the recovered adapter is then merged with or applied to the original unpruned base for inference。
- **State Ownership:** full-base revision owns inference semantics；pruning algorithm, mask and retained-index files own the training subspace；alignment corpus/config/checkpoint own carrier compatibility；quantization config owns stored representation；SFT data/objective and LoRA target/rank own the learned delta；recovery code/layout mapping own the full-shape adapter；registry owns the tuple `base + carrier + mask + alignment + adapter + recovery + quantization`；evaluation owns post-recovery behavioral evidence。
- **Control Flow / Data Flow:** `full base → pruning criterion/mask → compact structured or masked sparse carrier → optional alignment CPT → optional NF4 carrier → SFT LoRA on carrier → pruned adapter checkpoint → recovery by retained-index mapping/zero-fill → full-shape adapter → full base + recovered adapter → post-recovery evaluation`。The post-recovery artifact cannot inherit pre-recovery metrics because its base and computation graph differ。
- **Implementation Details:** v1 uses rank 8 adapters over attention Q/K/V/O, MLP up/gate/down and LLaMA-2 lm_head；LLaMA-3 excludes lm_head。Structured recovery reads saved pruned indices, allocates full-shape zero tensors and copies retained rows/columns；an optional `normA` path initializes some recovered A coordinates instead。The current repository has stage-numbered scripts but no packaged environment or frozen configs/checkpoints, its README still contains a placeholder clone URL, and main cannot be treated as a W08 executable snapshot。
- **Evaluation Contract:** models are LLaMA-2 7B/13B/70B and LLaMA-3.1 8B/70B。Default alignment mixes 102,400 instances each from FineWeb and OpenWebMath at length 512, about 105M tokens, batch 128 and up to 1,600 steps；a 200-step 13M-token point is highlighted。SFT uses OpenHermes/OpenOrca, batch 128, length 512, 400 steps and about 26.2M tokens；evaluation uses Alpaca perplexity, MathQA 1-shot, GSM8K 8-shot CoT strict match, six commonsense tasks 1-shot and HumanEval zero-shot Pass@1/10。
- **Baselines / Ablations / Sensitivity / Overhead:** comparisons include unadapted full bases, smaller-model LoRA and full-size LoRA, four pruning paths, alignment/no-alignment, recovery/no-recovery, 9.82×–28.56× parameter-storage points and tuned learning rates。The reported optimum is not monotonic: 12.84×–16.95× often beats 9.82×, while 28.56× degrades code performance。On the 13B online microbenchmark with 1,024 samples, batch 128, micro-batch 4 and length 512, LoRAM-Stru uses 29,799 MiB and 147.86s versus 7B LoRA 30,517 MiB/134.27s and 13B LoRA 51,661 MiB/206.07s。There is no full 70B peak-memory/time run table, equal-total-lifecycle cost, multi-seed or independent reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** experiments use NVIDIA A100 80GB, BF16, CUDA 12.2, PyTorch 2.4.0 and Transformers 4.45.1；QLoRAM stores the pruned carrier in 4-bit NF4 while compute remains BF16。The 15.81×/16.95× numbers are parameter-storage reduction ratios；table HBM values exclude low-rank overhead and do not include activations, buffers or alignment cost。The abstract's 20GB 70B-training and 15-GPU full-fine-tuning comparisons are not accompanied by a measured end-to-end 70B workload table。GPU count/topology, wall time/energy, data preprocessing, concurrency and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' specified LLaMA, pruning, alignment, SFT and evaluation workloads, training an adapter on a structured pruned carrier and expanding it for the full base can improve selected post-recovery perplexity and task scores while lowering stored carrier parameters。Recovery and alignment ablations show both stages affect the tested Alpaca perplexity。The 13B microbenchmark demonstrates a measured online memory/latency point comparable to 7B LoRA, not a full lifecycle or universal 70B result。
- **What It Does Not Prove:** it does not prove that most neurons are generally unnecessary for adaptation, that a 70B model can always be fine-tuned on any 20GB GPU, or that parameter reduction equals peak-memory, time, energy or cost reduction。It does not establish arbitrary task/model/adapter compatibility, inference savings, publisher alignment as negligible, or that recovered updates are mathematically equivalent to full-base LoRA。Selected downstream gains and tuned learning rates do not prove no capability regression elsewhere。
- **Limitations / Threats to Validity:** Eq.3 defines mask value 1 as retained and Eq.4 places the pruned update on that support, yet Eq.5 multiplies the pruned update by `1-M`；for same-shape masks this collapses the update to zero, while structured factors do not even share the full matrix shape required by that Hadamard expression。This contradiction persists in v2。The current code clarifies index-based dimension expansion, but one visible q-projection branch allocates a zero tensor and computes retained indices without an observable copy before saving；without the event-time commit/artifacts it cannot reconcile paper results。Tables report theoretical reductions for non-structured paths whose zeros do not reduce physical shape, and publisher/user cost separation can hide total system cost。
- **Trade-offs / New Failure Modes:** a smaller carrier reduces base storage but adds pruning/alignment preprocessing, mask and index artifacts, model-family-specific recovery code and a second base identity。Aggressive pruning reduces memory but can remove adaptation capacity；extra alignment reduces mismatch but costs tokens and can change knowledge；structured pruning is physically compact but recovery-sensitive, while unstructured pruning may retain dense shapes without kernel/storage benefit。Wrong mask polarity, target-module layout, head/GQA mapping, tokenizer/base revision or recovery code can produce a shape-valid but behaviorally wrong adapter。
- **Where the Previous Design Still Applies:** ordinary LoRA remains preferable when base/adaptor identity simplicity, portability and post-merge fidelity dominate；QLoRA remains simpler when the full quantized base fits；full fine-tuning remains justified for high update freedom and sufficient memory；small-model LoRA remains appropriate when inference also targets the small model；distillation/pruning to a compact deployment model is a different branch when inference cost, not only training cost, is the goal。
- **Evolution Relationship:** `Direct Evolution` for `full fine-tuning → LoRA trainable-state reduction → QLoRA frozen-base storage reduction → pruned training carrier → alignment of carrier/base knowledge → recovered full-shape adapter → full-base inference`；`Layering / Dependency` among pruning, alignment, SFT, recovery, registry and post-recovery evaluation；`Alternative Branch` versus same-base LoRA/QLoRA, small-model adaptation and compact-model deployment。The next pressure is an executable recovery specification, immutable carrier/adapter lineage, total lifecycle accounting and cross-task compatibility evidence。
- **ROADMAP Node:** canonical owner `TRAIN-LORA`（Current Ch30；Legacy Ch26）；handoffs to `TRAIN-PRETRAINING`, `TRAIN-SFT`, `TRAIN-CHECKPOINT`, `PLATFORM-MODEL-REGISTRY`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。LoRA owns the update parameterization and train/infer carrier split；Pretraining owns alignment objective；SFT owns supervision；Checkpoint/Registry own conversion lineage；Evaluation owns post-recovery equivalence/regression；Cost owns total publisher-plus-user work。
- **Target and Adjacent Chapters Read:** read Ch28 Pretraining's objective/precision/cost boundary, Ch29 SFT's masked supervision and artifact contract, Ch30 LoRA's base-forward storage, QLoRA, target modules and adapter lineage, Ch35 Checkpoint's conversion/equivalence gate, Ch59 Model Registry's base/adapter/quantization identity, Ch66 Evaluation System's full subject contract and Ch70 Cost's cost-to-quality accounting。The mechanism belongs in LoRA, but the unresolved recovery contract blocks Books integration。
- **Existing Coverage:** Books already explain that LoRA reduces trainable state without deleting base forward/activation cost, QLoRA reduces frozen-base storage, conversion creates a new artifact and base/adapter/layout/quantization identity must be versioned。LoRAM offers a genuinely new carrier/base split, but its durable lesson cannot be written as settled mechanism while the paper equation and public recovery implementation disagree。The Weekly retains the evolution and exact dispute rather than dropping the family。
- **Integration Decision:** `Disputed — Books Frozen` for `TRAIN-LORA`。Historical Books Gate remains closed；even after the archive gate opens, integration requires an executable mask/recovery contract or immutable artifact that reconciles Eq.5, structured dimension recovery and q-projection handling。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field, v1-locked Source Review；audited the full paper, all appendices and current official training/recovery paths；separated parameter-storage ratios from measured peak memory and total lifecycle cost；identified persistent Eq.3–5 mask contradiction and a visible recovery-code gap；mapped one canonical owner and six handoffs；froze Books rather than converting a disputed mechanism into a stable claim。
- **Open Questions:** immutable W08 commit/config/container/data/aligned-carrier/adapter/raw-run digests；author-confirmed mask polarity and executable Eq.5 replacement；q-projection recovery-copy semantics and exact code used for reported results；full 70B peak memory/time/throughput and GPU count；alignment wall time/energy and amortization volume；activation/buffer/optimizer accounting；post-recovery logits and broad capability regression；pruning/alignment/rank/target-module/seeds sensitivity；cross-model/task/quantizer transfer；artifact security and independent reproduction。

### Text2World: From Plausible Text to an Executable Symbolic Transition Contract

- **Candidate / Week / Score:** Text2World: Benchmarking Large Language Models for Symbolic World Model Generation / 2025-W08 / 27/30。
- **Source Family ID:** `text2world-symbolic-pddl-world-model-evaluation`。
- **Source Type:** arXiv research paper + official project page + author repository, benchmark, generation/evaluation scripts and mutable current configuration；later ACL Findings and arXiv v2 lineage。
- **First-public Date / Revision History:** arXiv v1 submitted 2025-02-18；v2 submitted 2025-02-24, outside W08。This review locks event-time claims to v1；v2, ACL 2025 Findings and current repository are later verification lineage, not W08 events。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13092v1；https://arxiv.org/abs/2502.13092；https://text-to-world.github.io/；https://github.com/Aaron617/text2world；https://github.com/Aaron617/text2world/blob/main/text2world/scripts/evaluate.py；https://github.com/Aaron617/text2world/blob/main/utils/text2world.yaml。
- **Related Primary Sources:** the released Hugging Face data viewer exposes the dataset；Tarski supplies parser/validator semantics；AgentGen supplies 601 synthetic domains for the paper's fine-tuning exploration；AgentInstruct supplies the later agent-training comparison。They support artifact lineage or inputs but do not independently reproduce Text2World's model ranking or semantic claims。
- **Access and Verification Status:** complete v1 HTML, metadata, all main experiments, error analysis, exploration, limitations and relevant appendices verified；official project, current repository, benchmark layout, evaluator path and model configuration inspected。No immutable W08 tag/commit, environment lock, API snapshot, raw generation manifest, seed log or complete fine-tuning artifact is published。Status: `Experimental — Books Pending`。
- **Full-read Coverage:** read Abstract, Introduction, formal world-model/task definitions, metric formulas, 1,801→264→103 construction pipeline, annotation/quality/contamination procedures, all 16-model results, correction analysis, syntax/semantic error taxonomy, test-time scaling, 2-shot, 601-domain fine-tuning, agent-training and concrete-description experiments, Related Work, Ethical Considerations, Limitation, prompt/domain examples and detailed result appendices；inspected repository generation/evaluation entry points and current model/runtime configuration。
- **Original Problem:** prior LLM world-model studies often evaluated downstream planning success or asked another LLM to judge generated dynamics。Those paths mix model construction, planner quality and judge randomness, making it hard to locate whether state variables, action preconditions or effects are wrong。Text2World asks the narrower question: can a model convert an abstract natural-language domain into a symbolic PDDL transition specification?
- **Why the Previous Design Was Reasonable:** end-to-end task success measures what an application ultimately cares about and avoids requiring one canonical symbolic representation；LLM judges scale to open-ended semantics；small hand-built PDDL suites are cheap to inspect。These approaches remain appropriate when formal schemas are unavailable, but their flexibility hides attribution and evaluator dependence。
- **Changed Constraint:** Agent and planning systems increasingly need auditable action contracts, while model-generated evaluators can share the generator's blind spots。The benchmark therefore needs a typed, parsable intermediate world model and component-level failure evidence, even at the cost of narrowing the environment to classical symbolic domains。
- **Mechanism:** define a domain as `D=<F,A>` with typed fluents and actions containing signature, parameters, preconditions and effects。The prompt reveals predicate/action signatures and high-level descriptions but withholds explicit dynamics；the LLM must synthesize PDDL。A deterministic validator checks syntax/executability；normalized Levenshtein similarity measures surface structure；for executable outputs, parsed predicates, parameters, preconditions and effects are compared with a reference using macro F1。An error-correction loop can return parser diagnostics for up to three repair attempts。
- **State Ownership:** source PDDL and double-reviewed annotations own benchmark reference state；the prompt owns the disclosed vocabulary but not hidden precondition/effect truth；the model owns a provisional domain proposal；Tarski owns parser-validity evidence；component comparison owns reference-match scores；human reviewers own semantic error labels；the correction loop owns attempt history；the environment, not the generated model or validator, would own real transition truth in any deployment。
- **Control Flow / Data Flow:** `public PDDL sources → validation/dedup/complexity filtering → expert-reviewed abstract description + gold domain → model proposal → parser/validator → optional syntax-error feedback → revised proposal → structural/component comparison → human semantic audit`。For use in an Agent, an additional missing path is `generated domain → planner → action → environment observation → transition reconciliation`；the paper does not execute that closed loop。
- **Implementation Details:** the released repository exposes 103-domain benchmark material, generation scripts, per-correction output files and an evaluator that parses the model/result identity from file names and compares initial/final generations。The current YAML sets temperature zero for most models and contains provider/model-specific context, token, dtype and GPU fields；it is mutable later lineage rather than a frozen W08 run manifest。The top-level evaluation script manually copies generated JSON into projects, so exact provenance depends on file naming and operator discipline rather than a sealed evaluation-run object。
- **Evaluation Contract:** 103 domains consist of 2 structurally similar but semantically distinct in-context examples and 101 test cases；descriptions average 851.6 GPT-2 tokens, gold domains 1,187.2, with 4.5 actions and 8.1 predicates on average。Six CS graduates annotate descriptions；two senior experts inspect each twice, with Fleiss kappa 0.82。Sixteen models from nine families run zero-shot CoT at temperature zero；open models use NVIDIA A100 80GB and proprietary models use official APIs。Model snapshot dates, API seeds, total GPU count, precision for every model, wall time, energy and monetary cost are Not Disclosed。
- **Baselines / Ablations / Sensitivity / Overhead:** the paper compares model families and sizes, zero versus three parser-guided corrections, two-shot prompting, full/LoRA fine-tuning on 601 AgentGen domains, LLaMA-2-70B agent training and abstract versus concrete descriptions。DeepSeek-R1 reaches 72.3% executable output without correction and 89.1% with three attempts；precondition/effect F1 moves 57.6/58.8 to 65.0/67.3。Concrete descriptions improve many rows, confirming that inferring hidden dynamics is harder than transcription。Few-shot helps Claude substantially but hurts GPT-4o-mini, and CodeLLaMA scaling is non-monotonic。There is no equal-token/equal-FLOP model-family control, seed confidence interval, held-out domain-family split, alternative validator, plan-execution metric or independent reproduction。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper disclosure is A100 80GB for open models and official APIs for proprietary models, temperature zero, model-specific context windows and up to three sequential repairs。Current config shows heterogeneous GPU counts/dtypes for some open models, but it is not pinned to the W08 run and cannot fill the historical contract。Batch, concurrency, exact output-token distributions, retry rate, API revision, full precision matrix, latency, cost, energy and production SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' frozen 101-domain reference and parser/component metrics, many tested models fail to emit parser-valid PDDL, and even the strongest measured model has substantial precondition/effect mismatch。Returning deterministic syntax diagnostics increases executable-output rates for most reported models。The human comparison shows an LLM semantic judge is near-random in the tested setup, and manual audit identifies missing/incorrect preconditions and effects as the dominant semantic-error family。The benchmark and code make these failure types inspectable rather than collapsing them into downstream success。
- **What It Does Not Prove:** parser-valid PDDL is not an executed plan and does not prove environmental correctness, physical feasibility or closed-loop Agent success。Levenshtein similarity is not semantic equivalence；single-reference component F1 can penalize alternative but equivalent formulations, which the authors label SurfaceDivergence。Cross-family ranking does not causally prove reinforcement learning creates better world models, because training data, model size, APIs and inference budgets differ。The n-gram probe lowers one contamination indicator but cannot prove absence of training exposure。Agent-training and fine-tuning rows show associations under different bases/data, not a causal world-model-to-agent-performance law。
- **Limitations / Threats to Validity:** only 103 manually selected domains and two exemplars limit scale and domain-family inference；complex cases over 40 predicates, 20 actions or 5,000 tokens are filtered out；human abstraction can omit or cue dynamics；PDDL covers declared symbolic state rather than partial observability, continuous dynamics or stochastic effects。ANOVA excludes anomalous zeros and aggregates heterogeneous model observations, so its significance must not be read as an independent causal estimate。Correction feedback is syntactic, while semantic gains can arise indirectly and remain reference-bound。No closed-loop plan execution, perturbation, long-horizon rollout, safety or production workflow is evaluated。
- **Trade-offs / New Failure Modes:** symbolic generation makes state/action contracts auditable and enables deterministic syntax feedback, but forces the world into a predefined vocabulary and one formalism。Reference matching localizes errors yet introduces representation bias；syntax repair improves operability while risking over-optimization to parser acceptance；abstract descriptions test inference but increase annotation ambiguity；concrete descriptions reduce ambiguity but turn the task toward transcription。A generated contract can be shape-valid while omitting a safety-critical precondition, creating a particularly dangerous false sense of executability。
- **Where the Previous Design Still Applies:** end-to-end environment success remains necessary when the real objective is task completion；domain simulators and hand-authored PDDL remain preferable where invariants must be guaranteed；LLM or human semantic judges remain useful for concepts not representable in the schema, provided their calibration is measured；free-form latent/video world models remain useful for high-dimensional observation prediction, but need separate intervention evidence。Text2World is a complementary symbolic diagnostic, not a replacement for these branches。
- **Evolution Relationship:** `Direct Evolution` for `free-form/indirect world-model evaluation → typed symbolic transition proposal → deterministic syntax validation → component-level semantic comparison → parser-guided repair`；`Layering / Dependency` from world model into planning/workflow and from evaluation harness into evidence；`Alternative Branch` versus learned latent dynamics, video prediction, hand-authored simulators and end-to-end environment evaluation。The next pressure is equivalence-aware semantic validation and closed-loop reconciliation of predicted versus observed transitions。
- **ROADMAP Node:** canonical owner `MULTIMODAL-WORLD-MODELS`（Current Ch25；Legacy N/A）；handoffs to `AGENT-PLANNING`, `AGENT-WORKFLOW`, `PLATFORM-EVALUATION-SYSTEM`, `TRAIN-SFT` and `MULTIMODAL-EMBODIED-VLA`。Ch25 owns action-conditioned transition contracts；Planning/Workflow consume and revise them；Evaluation owns subject/scorer/environment identity；SFT owns synthetic-domain supervision；Embodied VLA owns physical action authority and observation feedback。
- **Target and Adjacent Chapters Read:** read Ch24's proposal/correction/commit boundary, Ch25's simulator→latent→action-conditioned transition evolution, state ownership and intervention ladder, Ch26's physical-action authority and closed loop, Ch66's executable-evidence/scorer/dataset contract, Ch79's plan-as-state-transition hypothesis and Ch81's evaluator-driven durable workflow。Text2World fills a symbolic specification/evidence gap in Ch25 but cannot inherit Ch26's physical evidence or Ch66's release authority。
- **Existing Coverage:** Books already distinguish video generation, predictive environment models and controllable world models；state that planning consumes provisional transition hypotheses；and require executable artifacts plus environment evidence rather than judge scores alone。Text2World adds a durable mechanism bridge—typed preconditions/effects, deterministic parser feedback and component-level failure localization—while its parser-validity/semantic-equivalence boundary prevents a naive “executable means correct” conclusion。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` for `MULTIMODAL-WORLD-MODELS`。Historical Books Gate remains closed；a future integration should refine the symbolic-world-model and evidence-ladder branch, preserve hand-authored simulator/latent/video alternatives, and not copy model rankings or claim RL causality。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field v1-locked Source Review；audited the full paper, appendices, project, current benchmark/evaluator/config artifact；separated parser validity, reference similarity, semantic equivalence and environment truth；mapped one canonical owner and five handoffs；kept W08 as evidence-only and reduced ordinary pending by one。
- **Open Questions:** immutable W08 code/data/config/container/API/model/run digests；raw 101-case generations and correction traces；exact model snapshots, seeds, retry/token/cost/latency distributions；semantic-equivalence canonicalization beyond one reference；domain-family holdout and contamination audit；alternative parser/validator agreement；annotation ambiguity and independent human labels；equal-compute RL/non-RL comparison；plan execution, stochastic/continuous/partially observed domains；closed-loop transition calibration, safety-critical omission rate and independent reproduction。

### HeadInfer: Exact KV Offload Moves the Bottleneck from HBM Capacity to Host Memory and PCIe

- **Candidate / Week / Score:** HeadInfer: Memory-Efficient LLM Inference by Head-wise Offloading / 2025-W08 / 27/30。
- **Source Family ID:** `headinfer-head-wise-kv-offload`。
- **Source Type:** arXiv v1 systems paper + author repository + current implementation paths。
- **Event Date / First-public Date / Revision History:** arXiv v1 submitted 2025-02-18 06:26 UTC；metadata currently lists only v1。W08 evidence is locked to v1；the mutable repository is inspected only as artifact lineage and is not treated as a frozen event-time implementation。
- **Direct Primary Sources:** arXiv v1 HTML/metadata；paper algorithms, tables and appendices；author repository；current `main.py`, `headinfer/cache.py`, `headinfer/mp.py` and environment declaration。
- **Related Primary Sources:** Hugging Face `OffloadedCache` is the current layer-wise primitive reused by the public code；the paper compares chunked prefill, layer-wise offload and KIVI-style 4-bit KV, but those sources do not independently reproduce HeadInfer's measurements。
- **Access and Verification Status:** complete v1 paper, formulas, algorithms, roofline analysis, all main/appendix tables, ablation and portability appendix read；current repository and relevant code paths inspected。No immutable W08 tag/commit, release, frozen dependency lock, raw benchmark logs, real 1M/4M semantic-generation script or independent reproduction is available。Status: `Experimental — Books Pending`。
- **Full-read Coverage:** metadata；Abstract/Introduction/Related Work；head-wise decomposition and memory equations；chunked prefill, adaptive grouping and ping-pong transfers；implementation pseudocode；roofline analysis；LongBench v2/SCBench/NIAH/RULER setup；memory/latency/throughput tables；granularity ablation；70B pipeline-parallel experiment；all performance/memory appendices；sparse extension；repository README/code/environment。
- **Original Problem:** a million-token dense KV cache can exceed consumer-GPU HBM even when model weights fit。Chunked prefill reduces activation peaks but leaves the full KV resident；layer-wise offload still needs an entire layer's KV staging footprint, which can be too coarse when only a few GiB remain after weights/workspace。
- **Why the Previous Design Was Reasonable:** all-GPU FullKV gives the simplest exact semantics and highest Decode bandwidth；chunked prefill directly targets activation peaks；layer-wise offload matches Transformer execution order and existing cache abstractions；KV quantization/pruning is rational when a quality budget permits approximation。Their limits appear only when exact ultra-long single-request capacity dominates throughput。
- **Changed Constraint:** the target becomes one very long BF16 request on a 24.5GB RTX 4090 backed by hundreds of GiB of host DRAM and PCIe 4.0, while accepting extremely slow token generation。The objective shifts from high-throughput serving to feasibility under an HBM ceiling。
- **Mechanism:** partition every layer's KV by attention head, keep most head caches in preallocated/pinned CPU memory, stage one or several head groups through two GPU buffers, overlap next-head prefetch and prior-head eviction with current-head attention, and use chunked prefill to bound activations。Adaptive grouping uses coarse groups for shorter contexts and progressively finer groups as the KV footprint grows。
- **State Ownership:** the cache manager owns per-layer/per-head CPU and GPU placement, group size, preallocated buffers, transfer streams and completion；the attention runtime owns current query/head computation and may consume a group only after its transfer is visible；the Prefill controller owns chunk boundaries；the model/request identity owns sequence position, dtype and complete dense KV。The paper does not disclose production lease, cancellation, admission, retry or multi-tenant ownership semantics。
- **Control Flow / Data Flow:** prompt chunk → compute head K/V on GPU → append/update the authoritative head cache → async move cold head state to CPU while prefetching the next head into the alternate GPU buffer → compute per-head attention → concatenate all head outputs → repeat by layer/chunk；Decode repeats this transfer/compute pipeline for every generated token。
- **Implementation Details:** all weights remain on GPU；CPU KV and two GPU staging buffers are preallocated；the paper groups all heads below roughly 500K, then uses 2/4/8 groups up to 4M。The current public code maps each KV head to a pseudo-layer index and reuses Transformers' layer-wise `OffloadedCache` movement。Its headline 1M Decode path constructs zero-filled 1M caches and runs random one-token steps, while the real Prefill example is only 4×10,240 random tokens；therefore it is a footprint/timing demonstration, not a released semantic 1M/4M reproduction。
- **Evaluation Contract:** BF16 models include Llama-3-8B/70B, Llama-2-7B, Mistral-7B, Qwen2-7B and Gemma-2-9B；the long Llama-3-8B is Gradient's extended-context variant。Primary hardware is one RTX 4090 with 24.5GB HBM, 1TB DDR5, PCIe 4.0 x16 and measured 25GB/s pinned one-way transfer；70B uses eight RTX 4090 units with pipeline parallelism。Benchmarks are LongBench v2, SCBench, NIAH and RULER；batch is one for the core memory calculation, chunk size is commonly 10K。
- **Baselines / Ablations / Sensitivity / Overhead:** standard FullKV, chunked prefill, layer-wise offload and 4-bit KV quantization；head grouping 8→4→2→1 and chunk-size variants；memory, prefill/decode latency and context capacity tables。The paper does not provide continuous batching, concurrent tenants, arrival traces, tail SLO, energy/cost, equal-context quality across all baselines or a production engine comparison。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** RTX 4090 24.5GB, 1TB host DRAM, BF16, batch one, contexts from 1K to 4M。The setup text names four AMD EPYC 7B13 CPUs while Table 3 names EPYC 7V12；this hardware-identity conflict remains unresolved。Topology for the eight-4090 70B run, exact CPU affinity, concurrency and TTFT/TPOT SLO are Not Disclosed。
- **What the Evidence Actually Proves:** under the authors' single-request hardware contract, finer exact KV staging reduces the minimum resident GPU KV footprint below layer-wise granularity and makes contexts fit that otherwise OOM。At 1M the paper reports 1GB resident GPU KV and about 17GB total GPU memory while retaining 128GB total KV across tiers；at 4M it reports 3.91GB resident GPU KV and 500GB total KV。The grouping ablation supports a capacity/transfer-launch trade-off, and the latency tables expose the cost rather than proving a free speedup。
- **What It Does Not Prove:** it does not prove useful 4M model quality, production goodput, low-latency Decode, multi-request serving, host-memory efficiency or universal exactness of the optional sparse extension。At 1M the reported Decode rate is only 0.15 token/s (6.41s/token)；at 4M Prefill is 27,114s and Decode 27.2s/token。LongBench methods use different maximum context lengths, so score differences also reflect truncation/access。The current repository does not reproduce the headline semantic run。
- **Limitations / Threats to Validity:** CPU DRAM becomes the next hard ceiling；PCIe and host bandwidth dominate Decode；long-context model quality degrades on several RULER tasks；single-GPU/single-request results do not cover fragmentation, contention or scheduler fairness。Hardware naming is inconsistent；the public artifact is mutable and partial；no multi-seed or independent reproduction exists。The paper has no dedicated limitations section, so these boundaries are reconstructed from its tables, setup and artifact。
- **Trade-offs / New Failure Modes:** exactness avoids silent eviction/quantization error but exchanges scarce HBM for enormous host capacity, pinned-memory pressure, PCIe traffic, launch overhead and very high TPOT。Finer head granularity lowers residency but increases transfer/kernel frequency；coarser grouping improves efficiency but raises the HBM floor。New failures include transfer-stream ordering bugs, stale/misindexed head state, host OOM, pinned-memory exhaustion, PCIe contention, cancellation leaks and pipeline-rank visibility mismatch。
- **Where the Previous Design Still Applies:** FullKV remains preferable for short contexts and latency/throughput-sensitive Decode；chunked prefill is still the direct answer to activation peaks；layer-wise offload is simpler when a full layer fits；quantization/pruning remains a separate approximate branch when quality permits；distributed/tiered engines are preferable when fleet capacity, concurrency and tail SLO matter more than one-request feasibility。
- **Evolution Relationship:** `Direct Evolution` for `all-GPU FullKV → chunked prefill for activations → layer-wise exact KV offload → head-group exact KV offload`；`Alternative Branch` versus lossy quantization/eviction and distributed KV placement；`Layering / Dependency` with PagedAttention and scheduling。The next pressure is not finer granularity alone, but joint placement/admission that prices host capacity, transfer bandwidth and TPOT。
- **ROADMAP Node:** canonical owner `INFER-KV-CACHE`（Current Ch45；Legacy Ch41）；handoffs to `MODEL-LONG-CONTEXT`, `INFER-PREFILL`, `INFER-DECODE`, `INFER-PAGED-ATTENTION` and `INFER-GPU-MEMORY`。
- **Target and Adjacent Chapters Read:** read Ch22's model-level long-context boundary, Ch43 Prefill/chunking contract, Ch44 Decode/TPOT critical path, Ch45 lifecycle/offload/tiering/evidence boundary, Ch47 logical-to-physical block mapping and Ch54 HBM admission budget。HeadInfer belongs to Ch45 because it changes KV placement granularity and ownership；Ch43 owns activation chunking, Ch44 exposes transfer in TPOT, Ch47 owns block allocation and Ch54 owns full memory accounting。
- **Existing Coverage:** Books already state that offload trades transfer/SLO for capacity and describe recoverable host tiers, but do not yet derive why layer-wise staging can remain too coarse or connect head grouping to the HBM-floor/PCIe/launch trade-off。This is a real refine gap, not a new chapter；the paper's extreme-context numbers remain a constrained case rather than prose-level invariants。
- **Integration Decision:** `Books Pending — Refine Existing Argument Candidate` for `INFER-KV-CACHE`。A future Books pass may add the granularity evolution and capacity-versus-TPOT branch, while retaining FullKV, chunked prefill, layer offload, lossy compression and distributed placement as coexisting designs。Historical Books Gate remains closed；no Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field v1-locked review；audited complete paper/appendices and current public code；separated exact dense offload from optional sparse approximation；bound capacity/latency claims to the disclosed single-request hardware；recorded hardware/artifact conflicts；reduced ordinary pending by one。
- **Open Questions:** immutable W08 code/release/environment and raw benchmark logs；real 1M/4M semantic generation script and output checks；EPYC 7B13 versus 7V12 identity；eight-GPU topology；exact pinned-memory/NUMA policy；transfer overlap traces；host allocator and cancellation semantics；continuous batching, multi-tenant fairness, prefix sharing and PagedAttention integration；tail TTFT/TPOT/goodput/cost/energy；long-context quality at 1M/4M；independent reproduction。

### AdaptiveStep: Confidence-Defined Reward Boundaries Do Not Become True Reasoning Steps for Free

- **Candidate / Week / Score:** AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence / 2025-W08 / 24/30。
- **Source Family ID:** `adaptivestep-confidence-prm-tvd`。
- **Source Type:** arXiv v1 research paper + author repository + released model/data/environment lineage。
- **Event Date / First-public Date / Revision History:** arXiv v1 submitted 2025-02-19 18:35 UTC；v2 submitted 2025-05-31 and is outside W08。The current README says models/data were released 2025-01-31, while visible Hugging Face artifacts show February updates and no W08-frozen manifest；those earlier artifacts are recorded as prior lineage, but the mechanism/publication event remains the v1 paper in W08 rather than being silently backdated。
- **Direct Primary Sources:** arXiv v1 HTML/metadata；paper equations, tables and appendices；author repository README/training scripts/evaluation paths；current math TVD implementation；Hugging Face training/evaluation artifact pages。
- **Related Primary Sources:** OpenRLHF and vLLM provide the current training/serving substrate；GSM8K, MATH500, GSM-Symbolic, LeetCodeDataset and LiveCodeBench provide subject/verifier contracts。They do not independently prove that low policy confidence identifies causal reasoning boundaries or reproduce the reported efficiency claim。
- **Access and Verification Status:** complete v1 paper, all method/evaluation/generalization/feature sections and appendices read；current repository, training invocation, separate task/reward services, TVD implementation and visible artifact lineage inspected。No immutable W08 code/data/model/environment/run bundle, hardware log or independent reproduction exists。Status: `Disputed — Efficiency / Label Contract；Books Frozen`。
- **Full-read Coverage:** metadata/revisions；Abstract/Introduction/Related Work；confidence threshold and step division；rollout hard estimation；PRM objective；Token-level Value-guided Decoding；models/datasets/baselines/metrics/parameters；BoN/TVD；position/model/in-domain/cross-domain/mixed-data analyses；construction/feature statistics；Impact/Conclusion；all dataset/case appendices；training and evaluation artifact paths。
- **Original Problem:** sequence-level outcome reward gives poor local credit, but manually marking reasoning steps is expensive and rule-based newline/fixed-token boundaries need not coincide with actual decisions。The paper asks whether the policy's own low-probability tokens can cheaply choose denser PRM supervision points and later trigger token-level guidance。
- **Why the Previous Design Was Reasonable:** final-answer reward is easy to verify and avoids pretending a textual rationale is causally correct；newline/sentence boundaries are cheap, stable and tokenizer-independent enough for many datasets；manual process labels can encode domain semantics；fixed intervals produce a predictable annotation budget。They remain rational when policy confidence is unavailable, uncalibrated or unrelated to task decisions。
- **Changed Constraint:** process supervision must scale across math and code without domain-specific parsers or expert boundary labels, while preserving enough local signal for Best-of-N selection and online token intervention。
- **Mechanism:** sample 30 responses per question and retain token probabilities；choose the bottom 2% of token-confidence positions as boundaries；from every resulting prefix run eight continuations and label the step positive if any continuation reaches a verified final answer；train a PRM on the inserted placeholder positions。At Decode time, if Top-1 confidence falls below a threshold, TVD asks the policy for Top-M tokens, scores each extended prefix with the PRM and commits the highest-scoring token。
- **State Ownership:** the construction policy/version owns token probabilities and boundary locations；the rollout sampler/verifier owns binary labels；the PRM owns prefix scores and placeholder-token semantics；TVD owns confidence threshold, Top-M candidate set and commit；the task verifier owns final math/code correctness。Changing policy, tokenizer, temperature, threshold, rollout count or verifier changes the dataset identity。
- **Control Flow / Data Flow:** dataset question → policy sampling/log probabilities → global confidence quantile → boundary insertion → J continuation rollouts per prefix → executable/final-answer verification → binary labels → PRM training；online: policy next-token distribution → low-confidence trigger → Top-M prefix candidates → separate PRM scoring → one committed token → repeat until stop。
- **Implementation Details:** the current training script uses OpenRLHF PRM training with four visible GPUs, BF16, ZeRO-2, max length 8192, one epoch, batch 32/micro-batch 4 and the `ки` placeholder。The current TVD path starts separate task and reward OpenAI-compatible services, makes a one-token policy request, and on a trigger sends all Top-M extended prefixes to the reward service。This is a mutable implementation, not a frozen W08 environment；the exact data-construction code and event-time dependencies are not fully pinned。
- **Evaluation Contract:** math uses MetaMath-Mistral/Llama generation, GSM8K, MATH500 and GSM-Symbolic；code uses a DeepSeek-Coder-6.7B-derived LCD-DS, 1,745 collected training problems, 175 test problems and LiveCodeBench v4。BoN uses minimum step score and N up to 64；TVD compares accuracy/pass@1 against greedy and other PRMs。Training data comprise about 388K math and 49K code samples after 30 samples/question, deduplication and eight rollouts/step。
- **Baselines / Ablations / Sensitivity / Overhead:** Math-Shepherd, ER-PRM, code ORM, greedy Decode；confidence/random/hard rating positions；different construction policies；in-domain, cross-domain and mixed-data tests。There is no matched-compute ablation separating boundary choice from number/diversity of rating points, no sensitivity curve for the 2% quantile/J/Top-M/trigger threshold, no calibrated-confidence study and no measured TVD latency/token/cost overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** paper hardware, training precision, exact dependency/model revisions, prompt/output lengths, concurrency, wall-clock/token cost and SLO are Not Disclosed。Current scripts show BF16 four-GPU PRM training and up to 48 evaluation processes, but mutable code cannot backfill the historical run。Separate task/reward servers and per-trigger candidate scoring prove non-zero systems work even though its magnitude is unknown。
- **What the Evidence Actually Proves:** under the authors' frozen math/code datasets, verifier rules and model families, policy-relative low-confidence positions can produce a trainable PRM dataset；the resulting PRMs improve several reported BoN/TVD cells and retain some rating-position/in-domain transfer。Feature counts show selected positions differ from newline boundaries and concentrate on math expressions, conjunctions, comments and control tokens in those corpora。
- **What It Does Not Prove:** low probability is not a causal reasoning-step oracle, calibrated uncertainty or error signal；“any success in eight rollouts” estimates a rollout-policy-dependent event, not step correctness；cross-domain results are mixed and sometimes below greedy。The paper does not isolate AdaptiveStep from more/different supervision points, prove universal transfer, or show production latency/cost。The conclusion's “without additional inference overhead” conflicts with Eq.4 and the released dual-service Top-M PRM calls。
- **Limitations / Threats to Validity:** confidence is model/tokenizer/temperature dependent and can select rare lexical tokens rather than decisions；2% is justified by a human dual-process analogy rather than task sensitivity；hard labels have false negatives when eight rollouts miss a viable continuation and treat one lucky success as positive；minimum-step BoN amplifies one miscalibrated score。Eq.3 is written without the negative sign while called a loss, and the method alternates between a low-confidence token as the start versus end of a step。Dataset/code provenance, leakage, test quality and mutable artifact drift remain risks。
- **Trade-offs / New Failure Modes:** adaptive boundaries reduce hand-authored rules and concentrate labels, but couple reward semantics to one policy's confidence geometry。More local labels require many continuation rollouts；TVD may repair uncertain choices but adds Reward Model compute, synchrony and commit bias。Failures include confidence drift, threshold collapse, label leakage from verifier, PRM exploitation, Top-M exclusion of the correct token, latency spikes at uncertainty bursts, task/reward service version skew and irreversible early token commits。
- **Where the Previous Design Still Applies:** final-answer verifier/ORM remains preferable when outcomes are reliably executable and rationales are untrusted；manual or parser-defined steps remain stronger when domain state transitions are explicit；newline/fixed boundaries remain cheap baselines；BoN with an independent verifier is preferable when online latency permits parallel candidates；greedy/sampling remains preferable when PRM calibration or service overhead is unacceptable。
- **Evolution Relationship:** `Direct Evolution` for `sequence outcome → fixed/manual process boundary → policy-confidence boundary → rollout-labeled PRM → confidence-triggered token guidance`；`Alternative Branch` versus parser/environment-defined steps and full-trajectory selection；`Layering / Dependency` between Reward Model training, Sampling and Evaluation。The durable next pressure is to define decision boundaries from evidence/state transitions, not just model surprise。
- **ROADMAP Node:** canonical owner `TRAIN-RLHF`（Current Ch31；Legacy Ch27）；handoffs to `TRAIN-GRPO`, `MODEL-SAMPLING`, `PLATFORM-EVALUATION-SYSTEM` and `PLATFORM-COST`。RLHF owns Reward Model data/label lifecycle；GRPO owns process-credit consumption in policy updates；Sampling owns token commit；Evaluation owns verifier/metric validity；Cost owns rollout and online scoring budget。
- **Target and Adjacent Chapters Read:** read Ch30's parameter-update boundary, Ch31's Reward Model/proxy/data-distribution/sequence-credit pipeline, Ch32's critic/token-credit semantics, Ch33's process reward and typed decision-boundary branch, Ch20's Sampling/commit/evidence boundary and Ch66's process-label/verifier evidence ladder。AdaptiveStep refines Ch31's missing boundary-construction mechanism but does not replace Ch33's optimizer or Ch66's truth authority。
- **Existing Coverage:** Books already state that sequence reward does not locate causal tokens, process reward adds evaluator complexity, confidence is not correctness, and terminal verifier/process label are different Evidence Levels。The missing durable bridge is how boundary owner, rollout policy and verifier jointly define PRM labels；however the paper's efficiency and label contract conflicts must be resolved before integration。
- **Integration Decision:** `Disputed — Books Frozen`。A future review may extract only the conditional design question—policy-relative boundary selection versus fixed/manual/environment boundaries—after the inference-overhead claim, Eq.3 sign, boundary indexing and matched-budget evidence are reconciled。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field v1-locked review；audited complete paper/appendices and current artifact；separated surprise, boundary, rollout viability and causal correctness；recorded earlier mutable artifact lineage；froze Books because the public efficiency/executable contract conflicts；reduced ordinary pending by one。
- **Open Questions:** immutable v1 code/data/model/environment/run；actual artifact first-public timestamps；correct Eq.3 optimization sign；whether low-confidence token starts or ends a step；2%/rollout-count/Top-M/trigger sensitivity；confidence calibration across policy/tokenizer/temperature；matched point/compute baselines；rollout-label variance；per-trigger PRM calls, tokens, latency/cost/GPU and tail SLO；sandbox/test leakage and independent reproduction。

### AIDE: From Monolithic Agent History to Executable Candidate Lineage

- **Candidate / Week / Score:** AIDE: AI-Driven Exploration in the Space of Code / 2025-W08 paper event / 27/30。
- **Source Family ID:** `aide-executable-code-space-tree-search`。
- **Source Type:** arXiv v1 research paper + earlier official technical report + versioned author release + current code lineage + independent benchmark papers/artifacts。
- **Event Date / First-public Date / Revision History:** the formal paper was submitted as arXiv v1 on 2025-02-18 18:57 UTC and currently has no later arXiv revision。The Source Family itself was first public in Weco AI's 2024-04-04 technical report；repository tags `v0.1.2` and `v0.1.4` followed on 2024-04-26/29, and pre-paper `v0.2.0` was released on 2025-01-23。W08 therefore owns the formal-specification paper event, not the invention date of the mechanism。
- **Direct Primary Sources:** https://arxiv.org/html/2502.13138v1；https://arxiv.org/abs/2502.13138；https://www.weco.ai/blog/technical-report；https://github.com/WecoAI/aideml；https://github.com/WecoAI/aideml/tags；https://github.com/WecoAI/aideml/releases/tag/v0.2.0。
- **Related Primary Sources:** OpenAI MLE-bench paper/repository and METR RE-Bench report supply independently maintained evaluation contracts；current author `agent.py`, `journal.py` and configuration expose later mutable implementation lineage, not a paper-pinned W08 run。
- **Access and Verification Status:** verified with temporal and artifact boundary。The complete v1 paper, all appendices, 2024 first-public report, pre-paper release metadata, current core state/control paths, MLE-bench full method/appendices and METR report are accessible。The exact commit/container/run set used for Weco-Kaggle and the paper's consolidated results is not published as one immutable manifest。
- **Full-read Coverage:** metadata and version history；Abstract/Introduction/Preliminaries/Related Work；formal objective and Algorithm 1；search, coding and summarization operators；data preview；all Weco-Kaggle protocols/results/limitations；MLE-bench and RE-Bench result lineage；baseline specifications；code-complexity/cost appendices；all competition metadata；pre-paper releases；current Agent/Journal/config state and evaluation-code paths；MLE-bench setup, scaffold modifications, scaling experiments, contamination and limitations；METR task, time-budget, score and failure contracts。
- **Original Problem:** machine-learning engineering is an iterative search over executable programs, but conventional AutoML requires a human-defined configuration space, while a general ReAct-style Agent accumulates a long monolithic interaction history and often abandons failed attempts instead of comparing and refining reusable artifacts。
- **Why the Previous Design Was Reasonable:** grid/random/Bayesian search is reproducible and efficient when the variables are known；a single conversational trajectory is flexible when tasks have no scalar evaluator；human engineers are still superior when objectives are ambiguous, feedback is delayed, code changes span many files or domain judgment cannot be reduced to a metric。
- **Changed Constraint:** stronger code models can propose arbitrary implementations, and Kaggle-like tasks provide an executable program, bounded environment and scalar validation signal。The new bottleneck becomes how to retain many attempts without overflowing Context, choose a parent, isolate debugging from improvement and spend compute across repeated experiments。
- **Mechanism:** define solution space `S`, stateless evaluator `h(s)` and tree `T` whose node is a program plus score and whose edge records an attempted improvement。A hard-coded policy chooses a new draft, a still-debuggable broken leaf or the best non-buggy node；a coding operator emits one draft/debug/atomic-improvement child；a summary operator projects selected metrics, plans and diagnostics from the tree into a bounded prompt。Execution closes the loop and the best observed node is returned。
- **State Ownership:** the Journal owns candidate code, plan, parent/children, step, execution output, bug status, metric and derived summary；the executor owns process/resource isolation and observable terminal result；the evaluator/feedback model parses failure and metric direction；the search controller owns draft/debug/improve selection and budget；the code model proposes a child but does not own artifact truth or deployment authority。Dataset, holdout and scorer remain environment-owned ground truth。
- **Control Flow / Data Flow:** `task + data preview + budget → select parent or draft → model proposes plan/code → sandbox executes → feedback path classifies bug and extracts metric → Journal appends immutable lineage node → summary projects prior findings → search policy chooses the next branch → repeat → independent final grading`。This is an external artifact-search Workflow, not model-weight self-improvement。
- **Implementation Details:** the paper's policy first creates diverse drafts, probabilistically debugs buggy leaves within a maximum depth, then greedily improves the best valid node one atomic change at a time。The public Journal stores full program and execution lineage while prompts receive a compact summary。Pre-paper `v0.2.0` added reporting, Docker/WebUI and backend fixes；current `main` has materially newer model defaults and metric-direction reconciliation, so current code cannot be silently treated as the February evaluation artifact。
- **Evaluation Contract:** Weco-Kaggle covers 63 competitions；its Lite subset has 16 primarily CPU tabular tasks, manually reconstructed holdouts, GPT-4 Turbo and February 2024 leaderboard submissions。MLE-bench evaluates 75 offline competitions with a 24-hour limit, 36 vCPUs, 440GB RAM, 4095GiB SSD and one 24GB A10, plus 3 seeds normally and many more for AIDE GPT-4o/o1-preview rows；its AIDE config uses up to 2,000 steps, debug depth 20 and a 9-hour execution timeout。RE-Bench uses seven novel AI-R&D environments, executable scores and total-computer-time budgets, with human and Agent attempts under different allocations。
- **Baselines / Ablations / Sensitivity / Overhead:** Weco compares H2O AutoML with a 600-second search, LangChain AutoGPT and a human directing ChatGPT；MLE-bench compares modified AIDE, MLAB and OpenHands, four model backends, pass@k, CPU/one-A10/two-A10 and 24h/100h budgets；RE-Bench compares AIDE with simpler Modular scaffolding and humans over time。There is no clean factorial ablation of tree state, summarization, greedy selection, atomic edits, debug policy and model choice under one fixed workload, and purpose-built AIDE is not capacity-matched to the general scaffolds。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Weco-Kaggle hardware, package snapshot, precision, training batch and wall-clock budget are not fully disclosed；only early-2024 GPT-4 Turbo inference-cost plots are supplied。MLE-bench discloses GPT-4o-2024-08-06, o1-preview, Claude-3.5-Sonnet-20240620 or Llama-3.1-405B, one A10 baseline, 24 hours and separate attempts；model-training precision, token totals, concurrent runs, energy and production latency/SLO are Not Disclosed。RE-Bench permits task-specific hardware up to eight H100s and reports total computer time, not one serving contract。
- **What the Evidence Actually Proves:** the formal algorithm and open implementation establish a concrete, inspectable pattern for persisting executable candidate lineage outside the LLM Context and repeatedly using objective feedback to draft, repair and refine programs。Under MLE-bench's disclosed environment, AIDE is more persistent than the tested general scaffolds and, paired with o1-preview, earns a medal on 16.9% of competitions；additional attempts and time change the measured frontier。RE-Bench shows fast repeated experiments can outperform humans at short budgets on some tasks, while humans improve more at longer budgets。
- **What It Does Not Prove:** it does not prove tree search is the sole cause of benchmark gains, that greedy best-node selection is optimal, that scalar validation represents production quality, or that more iterations monotonically improve the final artifact。It does not establish autonomous long-horizon research, multi-file software reliability, safe deployment, generalization beyond objective-rich sandboxes or equal-cost superiority to expert workflows。The paper's MLE/RE rows are imported from related primary evaluations rather than rerun by one common author pipeline。
- **Limitations / Threats to Validity:** Weco holdouts differ from Kaggle private sets and expose test inputs；competition knowledge may contaminate models；leaderboard percentile aggregates heterogeneous tasks。MLE modifies every scaffold, grants a repeated validity server and observes invalid submissions/resource exhaustion；its 100-hour run can lose medals because AIDE's “best” selector is imperfect。RE-Bench has only seven environments, short feedback loops and visible scoring unlike much real research。The paper's greedy policy reaches local optima on larger codebases/multi-step changes；generated code complexity grows with steps, while current and event-time artifact identities drift。
- **Trade-offs / New Failure Modes:** persistent lineage prevents Context explosion and preserves failed evidence, but consumes LLM calls, training runs, storage and evaluation budget。Atomic edits improve attribution yet block coordinated refactors；greedy selection exploits quickly yet collapses diversity；summaries compress history yet can discard causal diagnostics。New failures include validation overfitting, evaluator/reward hacking, metric-direction error, stale environment summary, repeated deterministic bugs, resource exhaustion, sandbox escape, secret leakage, branch-local artifacts mistaken for committed truth and choosing a worse “best” node after evaluator noise。
- **Where the Previous Design Still Applies:** fixed AutoML remains stronger when a safe, typed low-dimensional search space exists；manual expert iteration remains appropriate for ambiguous objectives, slow/irreversible experiments and safety-critical release；a simple stateless Agent is cheaper for one-shot tasks；multi-step/multi-file work with partial observability needs a durable Workflow/DAG and explicit approvals rather than only a scalar solution tree。
- **Evolution Relationship:** `Direct Evolution` for `manual trial-and-error → fixed-configuration AutoML → LLM code-space draft/debug/improve tree → persistent evaluator-driven artifact population`；`Alternative Branch` versus monolithic ReAct, typed workflow and human-led experimentation；`Layering / Dependency` with sandbox, Evaluation System, artifact registry and derived Memory。Later population/Pareto and shared-constraint systems extend rather than invalidate AIDE's simpler greedy tree。
- **ROADMAP Node:** canonical owner `AGENT-WORKFLOW`（Current Ch81；Legacy Ch77）；handoffs to `AGENT-PLANNING`, `AGENT-REFLECTION`, `AGENT-MEMORY`, `AGENT-TOOL-CALLING`, `PLATFORM-EVALUATION-SYSTEM`, `PLATFORM-WORKLOAD` and `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** read Ch78 Tool Calling, Ch79 Planning, Ch80 Reflection, Ch81 Workflow and Ch66 Evaluation System。Workflow owns durable candidate/run/evaluator/selection state；Planning owns search policy and budget；Reflection owns evidence-backed repair；Evaluation owns holdout/scorer/uncertainty；Tool/Platform own execution, isolation and resource contract。
- **Existing Coverage:** Ch81 already derives evaluator-driven candidate search, artifact lineage, sandbox, held-out verification, multi-metric constraints, failed-run retention and the boundary between external artifact evolution and model self-improvement；it also extends greedy branch search with shared environment constraints and staged budget policy。AIDE supplies an earlier concrete lineage and strong failure evidence, but no missing first-principles mechanism requiring duplicate prose was found。
- **Integration Decision:** `Books Pending — No Change Candidate`。At a future Historical Books Gate, retain the current Ch81 argument and use AIDE only if a short historical bridge is needed；do not append its benchmark table or create an AIDE-specific section。No Books change now。
- **Changed Files or Rejection Reason:** added a non-template 30-field Source Review；separated 2024 family first-public date from the 2025 paper event；jointly audited the paper, pre-paper releases, current implementation lineage, MLE-bench and RE-Bench；bound benchmark claims to three distinct contracts；mapped one canonical owner；reduced W08 pending by one without modifying Books。
- **Open Questions:** immutable paper-run commit/container/dependency/data/holdout/result manifest；exact Weco per-task wall time, hardware and total execution cost；component ablation for tree, summary, atomic edit and search policy；held-out selection not reused during search；metric-direction and evaluator disagreement rate；multi-file/multi-objective support；branch diversity and uncertainty policy；sandbox/credential isolation；artifact commit/rollback semantics；production tail latency, cost, energy and independent reproduction。

### Model-guidance: Moving Conditional Emphasis from Sampling into Training

- **Candidate / Week / Score:** Diffusion Models without Classifier-free Guidance / Model-guidance / 2025-W08 / 26/30。
- **Source Family ID:** `model-guidance-training-time-cfg-amortization`。
- **Source Type:** arXiv v1 research paper + author implementation/checkpoint lineage。
- **Event Date / First-public Date / Revision History:** arXiv v1 was submitted on 2025-02-17 18:59 UTC and remains the only arXiv revision visible at access time。The public repository has no immutable W08 release/tag or paper-run manifest；current code is used to inspect executable semantics, not to backfill an event-time artifact identity。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.12154；https://arxiv.org/html/2502.12154v1；https://github.com/tzco/Diffusion-wo-CFG。
- **Related Primary Sources:** current author `train.py`, `sampler.py`, `test.py` and `models.py` expose target construction, label-drop state, optional CFG fallback and evaluation behavior；DiT/SiT/REPA are upstream implementation lineages, not independent reproduction of MG。
- **Access and Verification Status:** complete v1 HTML, formulas, Algorithm 1, all tables/figures, ablations, conclusion/impact statement and current core code paths verified。No paper-pinned commit, container, training log, per-seed result, hardware manifest or independent reproduction is available。Status: `Experimental — Disputed Scope Claim — Books Frozen`。
- **Full-read Coverage:** metadata/version history；Abstract/Introduction/Background/Related Work；CFG and distillation baselines；Bayesian derivation；MG diffusion/flow objectives；EMA/stop-gradient target；scale-aware, empty-class and automatic-scale variants；ImageNet setup；all quality/efficiency tables；drop-ratio, scale, model-input, empty-class, model-size and resolution ablations；figures and conclusion；repository README；current dataset, DDP, checkpoint, evaluation, target-construction, sampler, label-embedding and default-config paths。
- **Original Problem:** classifier-free guidance improves conditional image quality by mixing conditional and unconditional scores at every denoising step, but requires the model to learn an unconditional branch and normally doubles denoiser forwards at inference。The system question is whether the conditional-emphasis vector can be learned into the artifact instead of recomputed for every request。
- **Why the Previous Design Was Reasonable:** CFG is training-simple, architecture-agnostic and exposes a request-time guidance knob；one artifact can trade fidelity against diversity without committing to one training target。Its two forwards are acceptable when generation volume is low, guidance must remain adjustable or retraining is more expensive than serving compute。
- **Changed Constraint:** large denoisers and many sampling steps make the extra conditional/unconditional forward a material request-time cost。At the same time, stable EMA teacher state allows the same model family to estimate the score difference during training, creating an opportunity to amortize guidance into weights while retaining one conditional forward at deployment。
- **Mechanism:** MG changes the supervised target from the sampled noise/flow alone to that target plus a stop-gradient conditional-minus-unconditional prediction from an EMA model。For scale-aware variants, `w` is also an input；the student learns the calibrated score directly, so inference at `cfg_scale=1` uses one conditional forward。This is online self-distillation during training, not removal of conditional guidance semantics。
- **State Ownership:** the online model owns the learned single-pass proposal；the EMA copy owns teacher-target estimates；the empty-label/class-drop path owns unconditional score estimation；`w`, drop ratio and timestep cutoff own the quality/diversity operating point；the sampler owns whether one-pass MG or an additional vanilla-CFG wrapper executes；evaluation owns FID statistics and checkpoint selection。The paper title does not own the executable definition of “without CFG”。
- **Control Flow / Data Flow:** `ImageNet image + class → SD VAE latent → noisy/interpolated state → online conditional prediction`；after the configured start step, the EMA model evaluates conditional and empty-label branches, their stopped difference modifies the student target for selected examples/timesteps, AdamW updates the online model and EMA follows it。At inference, `latent noise + class → one MG denoiser forward/step → VAE decode` when `cfg_scale=1`；the released sampler can still concatenate conditional and empty-label batches and apply ordinary CFG when the scale exceeds one。
- **Implementation Details:** the paper randomly drops conditions and recommends `lambda` around 0.10～0.15；the current final-code defaults explicitly reserve 10% of each batch for label `1000`, begin MG after 100k steps, use fixed `mgw=1.45`, apply the teacher delta below a 0.75 timestep cutoff and evaluate FID periodically。The model is constructed with automatic dropout disabled, but the training loop performs explicit empty-label assignment；the teacher computes both conditional and unconditional predictions for MG examples。Thus request-time NFE falls, while training-time forward work and teacher state increase。
- **Evaluation Contract:** ImageNet class-conditional generation at 256² and 512²；Stable-Diffusion VAE maps 256² images to `32×32×4` latents。B/2 ablations train for 400k iterations with AdamW and global batch 256；DiT uses 1,000 sampling steps and SiT uses 250-step Euler-Maruyama。Primary metrics are FID-50K, sFID, IS, precision and recall；the code also performs periodic FID evaluation against supplied statistics。The paper reports single-sample time but does not disclose hardware, precision, batch or concurrency for that timing。
- **Baselines / Ablations / Sensitivity / Overhead:** compares DiT/SiT with and without CFG plus published pixel, latent-diffusion and AR rows；ablates `w`, conditional-drop ratio, scale-aware input, empty class, model size and 512² resolution。The best B/2 rows retain the empty class: DiT 7.24 versus 9.66 FID without it, and SiT 6.49 versus 9.03。Scale-aware input is slightly worse than fixed scale；automatic `w` is close to, not better than, manual search。There is no full accounting of extra EMA teacher forwards, training wall time/FLOPs, equal-total-compute baseline, seed variance, text conditioning, diverse datasets or serving concurrency/SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** models include DiT/SiT B/2, L/2 and XL/2；global training batch 256 and 400k B/2 iterations are disclosed。Training accelerator/count, precision, interconnect, wall time and energy are `Not Disclosed`；current code enables TF32 but is not a frozen paper run。Reported one-sample rates include DiT-XL/2 0.2 versus 0.1 image/s and SiT-XL/2 0.76 versus 0.39 image/s against CFG rows, with sampler steps as above；hardware, batch, concurrency, tail latency and production SLO are `Not Disclosed`。
- **What the Evidence Actually Proves:** under the authors' ImageNet class-conditional pipeline, an EMA-generated conditional/unconditional score difference can be moved into a training target, producing a model that reaches strong author-reported FID with one conditional forward per sampling step。Ablations show quality is sensitive to `w`, drop ratio and empty-class estimation, and that the single-pass artifact can still be wrapped with conventional CFG。The code independently confirms one-pass inference at scale one and explicit two-branch teacher work during training。
- **What It Does Not Prove:** it does not remove guidance semantics, unconditional estimation or the empty class from the best training recipe；it does not establish end-to-end training acceleration, since convergence-in-steps omits extra teacher forwards and no wall-time/equal-compute contract is given。It does not prove text-to-image/video generalization, universal two-times latency, production goodput, calibrated automatic scale, or that FID improvements imply prompt alignment, safety or perceptual superiority。
- **Limitations / Threats to Validity:** single dataset family and class labels；author-only evaluation；no seed intervals or independent reproduction；published-baseline timing/hardware comparability is incomplete；FID-guided hyperparameter tuning and periodic FID checkpoint inspection risk evaluation overfitting；precision drops slightly in some strongest rows while recall improves；automatic-scale rule is underspecified in the paper and absent from the released final defaults；current code may postdate the paper and lacks a release tag；the conclusion has no dedicated limitations section。
- **Trade-offs / New Failure Modes:** one-pass inference reduces request-time NFE and simplifies the hot path, but transfers cost to EMA storage, extra training forwards and artifact-specific target construction。Fixed `w` offers a cheaper/better reported point yet loses request-time flexibility；scale-aware input restores flexibility but adds conditioning state and slightly worsens reported FID。New failures include teacher-target drift, collapse from correlated self-targets, empty-label undertraining, FID-controller oscillation, training/inference scale mismatch, checkpoint-selection leakage and serving a one-pass artifact outside its trained conditioning range。
- **Where the Previous Design Still Applies:** ordinary CFG remains appropriate when guidance must be changed online, the base artifact already exists, training budget is scarce or the deployment can batch conditional/unconditional forwards efficiently。Pure conditional diffusion remains a simpler baseline when diversity matters and extra guidance is unnecessary；offline teacher distillation remains reasonable when a stronger/frozen teacher is available；MG is attractive when repeated high-volume inference can repay the additional training state and one operating region is stable。
- **Evolution Relationship:** `Direct Evolution` for `conditional model → conditional + unconditional CFG at every sampling step → EMA self-guided target during training → one-pass guided artifact`；`Alternative Branch` versus fixed pure conditional, request-time CFG, explicit classifier guidance and two-stage distillation；`Layering / Dependency` on VAE representation, EMA/checkpoint identity, sampler and Evaluation。The accurate durable description is guidance amortization, not categorical removal of CFG。
- **ROADMAP Node:** canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Current Ch24；Legacy N/A）；handoffs to `TRAIN-PRETRAINING` for teacher/objective state, `PLATFORM-EVALUATION-SYSTEM` for FID/selection validity and `PLATFORM-COST` for training-versus-serving amortization。
- **Target and Adjacent Chapters Read:** read Ch23 Multimodal Representation, Ch24 Generative Paradigms and Ch25 World Models。Ch24 owns diffusion trajectory and generation semantics；the VAE/code identity remains Ch23；MG has no action-conditioned transition and therefore is not a World Model。Training and cost chapters own the shifted work, not the generative-paradigm chapter。
- **Existing Coverage:** Ch24 already compares AR/diffusion factorization, mutable trajectory state, training/inference mismatch, sampler identity, NFE versus end-to-end cost and the rule that a paper's reduced steps do not prove serving goodput。MG adds a missing training-to-serving amortization branch, but its public scope claim conflicts with the executable best recipe and must not be integrated until the Historical Books Gate explicitly decides how to label that boundary。
- **Integration Decision:** `Disputed Scope Claim — Books Frozen`。A future Books pass may refine Ch24 with the conditional branch “request-time guidance → training-time guidance amortization,” but must state that the best reported/released training path retains an empty-label/unconditional estimator and extra EMA forwards；do not write “CFG eliminated,” copy the FID table or preserve the two-times speed claim without the hardware/workload contract。No Books change now。
- **Changed Files or Rejection Reason:** added a v1-locked non-template 30-field review；inspected equations, all experiments/ablations and current training/sampler/model/evaluation paths；separated inference-NFE evidence from total-training/serving cost；recorded the empty-class contradiction and Stable Node owner；reduced ordinary W08 pending by one without modifying Books。
- **Open Questions:** immutable event-time commit/checkpoint/container/run logs；training hardware, precision, wall time, FLOPs and energy including EMA teacher forwards；automatic-`w` update rule and held-out split；seed variance；why release defaults use fixed 1.45 despite adaptive claim；text/video conditioning；equal-total-compute and matched-hardware timing；batch/concurrency/tail-SLO behavior；teacher-target stability and independent reproduction。

### Transformers v4.49.0: Compatibility Surface Expansion Is Not a Unified Runtime Benchmark

- **Candidate / Week / Score:** Hugging Face Transformers v4.49.0 / 2025-W08 / 22/30。
- **Source Family ID:** `huggingface-transformers-v4.49.0-compatibility-surface`。
- **Source Type:** official GitHub Release/tag + release compare + merged PRs + tagged source tree and tests。
- **Event Date / First-public Date / Revision History:** official `v4.49.0` release published 2025-02-17 15:19 UTC，tagged at commit `a22a437`。The compare from `v4.48.3` records 315 commits, 1,359 changed files and 136 contributors。Later patches are revision lineage and are not used to rewrite the W08 contract。
- **Direct Primary Sources:** https://github.com/huggingface/transformers/releases/tag/v4.49.0；https://github.com/huggingface/transformers/tree/v4.49.0；https://github.com/huggingface/transformers/compare/v4.48.3...v4.49.0；tagged package/source and tests at `a22a437`。
- **Related Primary Sources:** merged PRs #35673/#35679 for typed/static generation cache；#35069 and processor PRs for fast-processor standardization；#35012/#36026/#36148 for GPTQModel, FP8 and HIGGS quantizer integration；#35848 for image-classification semantics；#35870/#36091 for default tensor/pipeline plans；#35164 for meta-device cache initialization。Model papers/cards linked by the release are separate Source Families and do not become release-wide mechanism evidence。
- **Access and Verification Status:** verified official release, immutable tag/commit, compare metadata, selected merged PR descriptions/diffs and tagged source/test surfaces。No release-wide benchmark artifact, fixed environment image, dependency/hardware matrix or production workload exists；status is `Full Source Review Complete — Version/Integration Fact`。
- **Full-read Coverage:** release metadata；all new-model, processor, breaking-change, quantization, generation, pipeline, framework/parallelism and bug-fix sections；tag/compare identity；selected Cache/GenerationConfig, image processor, quantizer, TP/PP plan, meta-cache and semantic-correctness PRs；target and adjacent Books chapters。Vendor model abstracts and their benchmark numbers were not reclassified as Transformers results。
- **Original Problem:** a general model framework must load many architecture, tokenizer/processor, cache, quantization and parallel-execution variants through stable public APIs。As coverage grows, a checkpoint can remain byte-identical while preprocessing, cache layout, quantizer backend or pipeline semantics changes its executable behavior。
- **Why the Previous Design Was Reasonable:** per-model modules and permissive legacy formats let maintainers add research models quickly；tuple KV caches were simple and widely supported；slow processors provided a reference path；AutoGPTQ and model-local parallel hints reflected the available backend ecosystem。These remain rational for pinned deployments and older integrations where compatibility matters more than a unified abstraction。
- **Changed Constraint:** multimodal and hybrid models increased processor/config diversity；`torch.compile`, static-shape execution and meta-device loading require explicit allocation contracts；multiple quantization backends need versioned adapters；tensor/pipeline plans and fixed-length caches must be represented before runtime；silent label/pipeline bugs show that nominal API compatibility does not guarantee semantic compatibility。
- **Mechanism:** the release expands Auto-class registries and model modules while standardizing several image processors and fast paths；Generation can instantiate `cache_implementation="static"` and returns a `Cache` object even when input used the legacy tuple form；quantization is routed through GPTQModel/FP8/HIGGS integration surfaces；model configs can carry default tensor and pipeline plans；meta-device cache initialization separates shape planning from physical allocation；corrective patches align classification activation, LayerNorm rename scope and VLM compile behavior。
- **State Ownership:** immutable tag and package version own framework identity；model/config classes own architecture and declared compatibility metadata；processor owns input transformation and post-processing semantics；`Cache` owns generated-token state representation；quantizer adapter owns conversion/load contract but the backend owns kernels；parallel plan owns mapping hints while the distributed runtime owns process/topology execution；application/platform owns the pinned dependency, hardware and regression evidence。
- **Control Flow / Data Flow:** model artifact/config/processor references → Auto registry resolution → processor normalization → model and optional quantizer load → cache implementation and parallel-plan selection → train/generate/pipeline execution → typed output/cache。Each arrow can change independently, so deployment identity must bind the complete compatibility tuple rather than only a weight digest。
- **Implementation Details:** nine named model integrations, CLI migration, processor refactors, quantization adapters, generation-cache migration and many correctness fixes land in one tag。The release is a broad integration batch, not one architecture；tests include fixed-length cache shapes, compiled-forward paths and device/backend cases, but the 315-commit surface also means a consumer cannot infer compatibility from semantic version alone without its own pinned regression suite。
- **Evaluation Contract:** evidence consists of upstream unit/integration/CI tests and PR-specific checks。There is no common model, hardware, precision, input/output length, batch, concurrency, latency/throughput, memory or SLO contract for v4.49.0。Numbers quoted in new-model descriptions belong to their authors' papers/cards under separate conditions。
- **Baselines / Ablations / Sensitivity / Overhead:** the release compare and targeted tests expose behavior differences from v4.48.3, including cache type/shape and corrected sigmoid-versus-softmax selection；they do not provide a controlled release-level ablation, dependency sensitivity matrix, compile/export parity matrix or measured cost of fast processors, static cache, quantizer adapters and TP/PP plans。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** heterogeneous model-specific CI only；a release-wide hardware list, model set, precision/quantization matrix, lengths, batch, concurrency, memory, TTFT/TPOT, throughput and production SLO are `Not Disclosed`。Backend support in an integration must not be read as performance portability。
- **What the Evidence Actually Proves:** at tag `a22a437`, the project intentionally broadened supported model/processor/quantizer families and migrated several execution surfaces toward typed, pre-declarable contracts。The semantic bug fixes prove that config and preprocessing are part of executable model identity；Cache/static-shape and parallel-plan PRs show a framework evolution from implicit Python objects toward runtime-visible state and plans。
- **What It Does Not Prove:** it does not prove that every new model is accurate, every fast processor is numerically identical, every quantizer preserves quality, static cache improves production goodput, default TP/PP plans are topology-optimal, or v4.49.0 is faster/safer than v4.48.3。It also does not disclose internal mechanisms of the integrated model families beyond their separate sources。
- **Limitations / Threats to Validity:** release notes aggregate many independent changes；optional dependency and hardware combinations exceed upstream CI；several breaking/corrective entries demonstrate behavioral drift；tag-level tests may not cover downstream custom code, remote model code, export/compile, mixed precision or distributed combinations。No signed environment or release-wide reproducibility bundle is supplied。
- **Trade-offs / New Failure Modes:** common typed APIs improve planning and interoperability but create migration work；static caches improve shape predictability while reserving capacity and requiring correct length bounds；fast processors reduce preprocessing bottlenecks but add parity/version risk；quantizer plugins expand choice while coupling optional dependencies, calibration metadata and kernels；default parallel plans reduce setup friction but may conflict with topology or backend assumptions。New failures include cache-format skew, processor semantic drift, quantizer/backend mismatch, stale plan metadata and silent result changes from config interpretation。
- **Where the Previous Design Still Applies:** legacy tuple caches remain necessary for pinned consumers；dynamic caches fit uncertain lengths and memory-sensitive workloads；slow processors remain reference/fallback paths；manually validated parallel plans remain preferable for heterogeneous clusters；a narrower pinned framework release is safer when a deployment needs a small compatibility matrix and long support horizon。
- **Evolution Relationship:** `Direct Evolution` from implicit/legacy cache and processor conventions toward typed cache, standardized processor and declarative plan surfaces；`Layering / Dependency` between model artifacts, framework adapters and serving runtime；`Alternative Branch` between static/dynamic cache, slow/fast processor and multiple quantizers。A later version does not erase the pinned older branch；it changes the compatibility and validation burden。
- **ROADMAP Node:** canonical owner `PLATFORM-MODEL-REGISTRY`（Current Ch59；Legacy Ch55）；handoffs to `INFER-KV-CACHE` for cache identity/lifecycle, `MULTIMODAL-REPRESENTATION` for processor identity, `TRAIN-DISTRIBUTED-TRAINING` for parallel-plan semantics and `PLATFORM-EVALUATION-SYSTEM` for regression evidence。
- **Target and Adjacent Chapters Read:** read Ch58 Kubeflow composition boundary, Ch59 Model Registry identity/evidence contract and Ch60 Training Operator runtime boundary；also checked Ch45 KV Cache and Ch66 Evaluation System owners。Ch59 owns the deployable compatibility tuple；Transformers does not become a model registry, scheduler or quality authority。
- **Existing Coverage:** Ch59 already defines behavior identity as weights + config + tokenizer/special tokens + template + adapters + quantization + runtime compatibility and requires target-hardware/runtime regression evidence。v4.49.0 supplies a concrete compatibility-drift case but no missing first principle；the durable Cache and processor mechanisms already have their own owners。
- **Integration Decision:** `Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate`。Historical Books Gate remains closed；a later Books pass should cite Ch59's existing contract rather than append a version feature list unless a separate Source Family establishes a new stable mechanism。
- **Changed Files or Rejection Reason:** added a non-template 30-field tag-locked review；separated model-family claims from framework integration evidence；mapped cache, processor, quantizer and parallel-plan changes to one asset-compatibility owner with short handoffs；reduced ordinary pending by one；no Books change。
- **Open Questions:** exact event-time CI matrix and dependency lock；fast/slow processor numerical parity by model/task；static/dynamic cache memory and correctness under compile/export；quantizer calibration/config portability；TP/PP plan topology assumptions；remote-code and downstream custom-model compatibility；signed SBOM/environment；upgrade rollback and production regression evidence。

### Accelerate v1.4.0: A Thin Wrapper Still Owns Distributed State Boundaries

- **Candidate / Week / Score:** Hugging Face Accelerate v1.4.0 / 2025-W08 / 23/30。
- **Source Family ID:** `huggingface-accelerate-v1.4.0-distributed-wrapper`。
- **Source Type:** official GitHub Release/tag + merged TP/DataLoader, torchao FP8, DeepSpeed FP8, memory-estimation and weak-reference fixes + tagged source/tests/examples。
- **Event Date / First-public Date / Revision History:** official `v1.4.0` released 2025-02-17 17:18 UTC at commit `b431d1f`。TP/DataLoader PR #3173 merged 2025-01-29 but first entered the packaged release in W08；later CLI/config maturation is revision lineage and is not backdated。
- **Direct Primary Sources:** https://github.com/huggingface/accelerate/releases/tag/v1.4.0；https://github.com/huggingface/accelerate/tree/v1.4.0；https://github.com/huggingface/accelerate/compare/v1.3.0...v1.4.0。
- **Related Primary Sources:** https://github.com/huggingface/accelerate/pull/3173；https://github.com/huggingface/accelerate/pull/3348；https://github.com/huggingface/accelerate/pull/3361；https://github.com/huggingface/accelerate/pull/3383；https://github.com/huggingface/accelerate/pull/3391。Transformers TP support and PyTorch/torchao/DeepSpeed are dependencies, not evidence that Accelerate owns their collective math or kernels。
- **Access and Verification Status:** verified immutable release/tag, complete release notes, tagged project contract and selected merged PR discussions/diffs/tests。The release explicitly labels torchao FP8 and in-house TP as initial support；no fixed environment or broad production matrix exists。Status: `Full Source Review Complete — Books Pending / No Change Candidate`。
- **Full-read Coverage:** release metadata and every change；tagged README/launcher/distributed abstraction；TP plugin and same-sample DataLoader contract；FP8 recipe/backend selection；DeepSpeed compatibility；memory estimator dtype correction；GradientState/DataLoader weak-reference lifetime fix；reported TP measurements and their caveats；target and adjacent Books chapters。
- **Original Problem:** researchers want one PyTorch loop to run on different device, mixed-precision and distributed backends without embedding launcher, rank, device placement, gradient, DataLoader and backend-specific boilerplate in the algorithm。The abstraction fails if it hides state that changes sample identity, precision, ownership or object lifetime。
- **Why the Previous Design Was Reasonable:** Data Parallel/FSDP and established FP16/BF16 paths covered most workloads；each rank receiving a distinct DataLoader shard is correct for data parallelism；strong references simplify singleton state management；backend-specific scripts expose semantics directly。They remain preferable when a workload needs mature support, exact backend control or minimal wrapper behavior。
- **Changed Constraint:** TP ranks jointly execute one model shard and therefore must observe the same input batch rather than independent DP shards；FP8 adds backend/recipe/calibration and hardware constraints；large-model memory estimation must respect requested dtype；long-lived GradientState references can retain prepared DataLoaders and leak host memory across repeated construction/destruction。
- **Mechanism:** `TorchTensorParallelPlugin` constructs a TP device mesh and relies on model TP-plan support；the DataLoader path duplicates the same samples across TP ranks while preserving different data across DP groups；`AORecipeKwargs` selects torchao FP8 through `Accelerator(mixed_precision="fp8")`；DeepSpeed FP8 compatibility and dtype-aware estimation refine adapter behavior；weak references break the GradientState→DataLoader lifetime cycle。
- **State Ownership:** user loop owns model objective and optimizer step；Accelerator/PartialState owns process-group, device, precision and plugin selection；TP plan owns parameter placement but PyTorch/Transformers own tensor-parallel execution；DataLoader shard/batch state owns sample identity；backend owns collective/kernel semantics；weak reference changes liveness observation, not DataLoader business ownership；application owns reproducibility and checkpoint lineage。
- **Control Flow / Data Flow:** config/constructor kwargs → distributed state/device mesh/backend selection → `prepare(model, optimizer, dataloader)` → model sharding/wrapping + DataLoader batch routing → forward/backward/collective → optimizer step → teardown。For TP, one logical batch must be broadcast/reused inside a TP group before sharded model computation；mixing TP and DP requires a two-dimensional group identity rather than one world-size number。
- **Implementation Details:** release exposes initial torchao FP8 through Python kwargs but not yet full `accelerate config`/YAML；TP support checks model plan availability and couples to Transformers/PyTorch interfaces；the PR explicitly notes the implemented master-fetch/distribute DataLoader paradigm and leaves the all-ranks-fetch-same-batch paradigm uncovered。The memory leak fix replaces GradientState-held DataLoader references with weak references；the estimator fix propagates `torch_dtype` rather than silently estimating another representation。
- **Evaluation Contract:** TP PR reports Granite-8B-Code-Base-128K and CodeLlama-7B runs with 4 GPUs, context 8,192/16,384, batch one and gradient checkpointing on/off；metric is max CUDA memory and tokens/sec/GPU。GPU model, precision, software stack, interconnect, warmup, step count and statistical variation are not disclosed in the visible contract；release-level FP8/memory-leak tests are functional rather than a uniform benchmark。
- **Baselines / Ablations / Sensitivity / Overhead:** single GPU, FSDP and TP rows expose capacity and local throughput；the PR itself warns that FSDP effective throughput multiplies across ranks while the displayed per-GPU TP number is not directly comparable。No DP×TP matrix, communication breakdown, loss/convergence parity, seed variance, batch scaling, dataloader-worker/streaming sensitivity, FP8 quality study or repeated-lifecycle leak curve is provided at release level。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4 unspecified GPUs；Granite/CodeLlama 7–8B；8K/16K；batch one；checkpointing on/off。Precision, GPU/NIC/topology, accumulation, total tokens, concurrency, host-memory curve, wall time, energy, tail latency and SLO are `Not Disclosed`。The release cannot support a hardware-independent speedup claim。
- **What the Evidence Actually Proves:** the tag adds an executable abstraction for making TP ranks share sample identity, selecting an initial torchao FP8 backend and correcting two state-accounting/lifetime bugs。It demonstrates that a “thin wrapper” still participates in correctness because rank grouping, batch routing, dtype accounting and object lifetime cross the user-loop/backend boundary。
- **What It Does Not Prove:** it does not prove TP is generally faster than FSDP, FP8 preserves convergence, every model has a valid TP plan, `prepare()` makes arbitrary scripts portable, combined TP×DP/DeepSpeed behaves correctly, or the memory leak is eliminated for every DataLoader lifecycle。The authors' PR measurements are not a production throughput contract。
- **Limitations / Threats to Validity:** initial APIs depend on specific Transformers/PyTorch/torchao/DeepSpeed versions；TP support is model-plan dependent；only one DataLoader acquisition paradigm is covered；benchmark hardware/precision is incomplete；release tests cannot exhaust backend combinations。Weak references can expose early collection if another owner is missing, while strong downstream references can still retain objects。
- **Trade-offs / New Failure Modes:** one loop across backends reduces boilerplate but hides more state behind `prepare()`；same-batch TP routing preserves math but may duplicate host work/transfer and requires correct group boundaries；FP8 lowers memory/compute cost but adds recipe/backend/hardware and quality drift；plugins improve composability but increase version skew。Failures include TP/DP group confusion, duplicated or skipped samples, unsupported plan, precision mismatch, incorrect memory admission and stale/leaked DataLoader state。
- **Where the Previous Design Still Applies:** plain PyTorch/torchrun remains better for unusual collectives or debugging；FSDP/DP remains preferable when parameter replication/sharding solves the bottleneck and effective throughput matters；FP16/BF16 remains safer without FP8 calibration/hardware support；rank-local DataLoader sharding remains correct for DP；strong explicit ownership is preferable when object lifetime must be deterministic。
- **Evolution Relationship:** `Direct Evolution` from single-axis DP wrapper toward typed TP groups and TP-aware input identity；`Layering / Dependency` on model TP plans, PyTorch collectives and backend precision kernels；`Alternative Branch` between explicit framework code and wrapper plugins, and between DP/FSDP/TP。Initial support is a new branch, not proof that it replaces mature distributed paths。
- **ROADMAP Node:** canonical owner `TRAIN-DISTRIBUTED-TRAINING`（Current Ch36；Legacy Ch32）；handoffs to the TP chapter for shard/collective math, `TRAIN-CHECKPOINT` for reproducible state, `PLATFORM-TRAINING-OPERATOR` for job/runtime submission and `PLATFORM-EVALUATION-SYSTEM` for parity/evidence。
- **Target and Adjacent Chapters Read:** read Ch35 Checkpoint, Ch36 Distributed Training and the following TP/PP/ZeRO route；also read Ch60 Training Operator boundary。Ch36 owns process group, sample identity, precision and communication invariants；Accelerate does not own workload admission, scheduler placement, checkpoint transaction or backend algorithms。
- **Existing Coverage:** Ch36 already requires preserving one optimizer-step semantic while mapping state/compute/communication to topology and warns that world size does not define parallel dimensions；Ch35 already binds dtype, sampler and layout to resumable identity；Ch60 separates runtime submission from parallel math。v1.4.0 is a concrete compatibility case, not a missing durable principle。
- **Integration Decision:** `Books Pending — No Change Candidate`。Historical Books Gate remains closed；a later Books pass should retain the existing distributed-state contract and avoid appending an Accelerate feature list unless another Source Family reveals a stable missing mechanism。
- **Changed Files or Rejection Reason:** added a non-template 30-field tag-locked review；bound TP rows to their incomplete workload contract；separated wrapper state from backend math；recorded initial-support and DataLoader-paradigm limits；reduced ordinary pending by one；no Books change。
- **Open Questions:** immutable benchmark environment/GPU/topology/precision；TP plan/model coverage；DP×TP and TP×checkpoint correctness；loss/convergence parity；DataLoader workers/streaming/resume identity；FP8 recipe/calibration/quality and hardware matrix；weak-reference lifecycle stress tests；multi-node failure/recovery；version compatibility and production observability。

### vLLM v0.7.3: Scheduling State Expands beyond a Request Queue

- **Candidate / Week / Score:** vLLM v0.7.3 / 2025-W08 / 27/30。
- **Source Family ID:** `vllm-v0.7.3-v1-scheduler-state-expansion`。
- **Source Type:** signed official GitHub Release/tag + compare + merged scheduler/cache/speculation/serialization/metrics/parallelism PRs + tagged source/tests/benchmarks。
- **Event Date / First-public Date / Revision History:** official `v0.7.3` released 2025-02-20 17:08 UTC at signed commit `ed6e907`；release contains 253 commits from 93 contributors。Earlier V1 alpha and individual merged PRs are predecessor lineage；later vLLM V1 defaults/releases are not backdated into W08。
- **Direct Primary Sources:** https://github.com/vllm-project/vllm/releases/tag/v0.7.3；https://github.com/vllm-project/vllm/tree/v0.7.3；https://github.com/vllm-project/vllm/compare/v0.7.2...v0.7.3。
- **Related Primary Sources:** https://github.com/vllm-project/vllm/pull/10235 for concurrent partial Prefill；#12755 for DeepSeek MTP；#12193/#13365 for initial n-gram speculation；#12922 for KV block-hash ownership；#12918 for msgpack core serialization；#12592/#12644/#13288 for cache/request/iteration metrics；#12996 and related PRs for V1 pipeline parallelism。Model cards and vendor-specific tuning claims remain separate evidence families。
- **Access and Verification Status:** verified signed release identity, complete highlights/changelog, compare, selected merged PR descriptions/diffs/tests and target chapters。Some PR pages intermittently timed out, but release/tag and available official PR/source surfaces uniquely establish identity and scope；no unresolved blocker remains。Status: `Full Source Review Complete — Books Pending / No Change Candidate`。
- **Full-read Coverage:** all release sections covering DeepSeek, V1, model/hardware support, engine features, performance and fixes；concurrent partial-prefill problem/design/workload/results and V0 boundary；V1 speculation, serialization, KV-hash ownership, metrics and pipeline-support surfaces；benchmark caveats；target/adjacent Books chapters。The 253-entry release is treated as a versioned source family, not 253 independent mechanisms。
- **Original Problem:** an inference engine that schedules only whole requests or a single partially-prefilled sequence can let a few very long prompts block medium/short arrivals and eventually starve Decode。At the same time, V1 must carry more typed state—LoRA, prefix identity, speculative proposals, pipeline ranks, metrics and wire messages—without losing correctness across scheduler/core/worker boundaries。
- **Why the Previous Design Was Reasonable:** full or one-at-a-time chunked Prefill maximizes large-matrix efficiency and keeps scheduling/KV accounting simple；a Python-object request path is easy to evolve；request-owned block hashes localize state；a mature V0 path remains safer while V1 lacks features。These remain rational for homogeneous prompts, low concurrency, short contexts, debugging or pinned deployments。
- **Changed Constraint:** multi-tenant traffic mixes many short prompts with a few 10K–200K prompts；one 130K prompt at a 512-token budget can occupy roughly 250 Prefill iterations and eliminate active Decode work。V1 feature parity adds pipeline groups, adapters, logprobs, sampling controls, speculative candidates and hardware backends, increasing state ownership and serialization/observability requirements。
- **Mechanism:** concurrent partial Prefill admits multiple partially-prefilled sequences per iteration while separately limiting how many “long” partial prefills may coexist, allowing shorter queued requests to bypass long ones；V1 adds n-gram proposal/verification, MTP path, LoRA/logprob/sampling support, pipeline execution and msgpack core requests；KV block hashes move from Request to KVCacheManager；new metrics expose prefix-cache hit rate, iteration token work and request timing。
- **State Ownership:** scheduler owns per-iteration token budget, partial-prefill slots, long-prompt classification and fairness policy；Request owns logical progress/constraints；KVCacheManager owns block/hash identity and reuse；speculator owns proposals while target verification owns commit；engine core/worker boundary owns serialized message schema；pipeline executor owns stage/rank execution；metrics registry owns observation definitions but not correctness or SLO policy。
- **Control Flow / Data Flow:** admitted request → tokenizer/input processor → waiting/running queues → scheduler classifies Prefill/Decode/speculative work → token budget and KV blocks reserved → model/pipeline execution → target verification/sampling → KV/progress commit → streamed output and metrics。Concurrent partial Prefill changes which waiting requests can advance in one iteration, not Transformer semantics。
- **Implementation Details:** V0 exposes `max_num_partial_prefills`, `max_long_partial_prefills` and a long-prompt threshold (default described as 4% of model context in the PR)；default one long partial Prefill preserves room for shorter work。The PR explicitly says the immediate mechanism is V0 and may inform a different V1 solution。V1 additions use msgpack for core messages, centralize KV hash state, add initial speculation and pipeline paths, and expand timing/cache/token histograms。
- **Evaluation Contract:** concurrent-Prefill PR uses Llama-3.1-8B-Instruct on one A100 80GB, request rate 12, ShareGPT-derived mixes: 900 short/100 medium, 990 short/10 duplicated approximately 100K-character prompts, and 850 short/140 medium/10 approximately 200K-character prompts。It compares base commit, feature disabled (`max=1`) and enabled (`max=4`) across TTFT percentiles and throughput。Other release claims—including 1.69× low-QPS MTP and 17% AMD latency reduction—belong to their PR-specific workloads, not one release-wide contract。
- **Baselines / Ablations / Sensitivity / Overhead:** partial-prefill comparison includes three traffic mixes and enabled/disabled settings；reported p90 TTFT roughly halves in the medium case, approaches 30× improvement in the constructed large case, and mixed throughput rises from 3,368 to 3,506 tokens/s while ITL is somewhat slower。There is no broad threshold/slot/request-rate sensitivity, multi-seed variance, TP/PP/multi-node test, quality parity, tenant fairness, cancellation/recovery or tail-goodput study across the complete release。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** primary scheduler case: one A100 80GB, Llama-3.1-8B-Instruct, prompt mixes up to approximately 200K characters, request rate 12 and max partial Prefills 1/4。Precision/quantization, exact token lengths, output-length distribution, batch/token cap beyond cited 512 example, software stack, warmup, repetitions and explicit TTFT/TPOT SLO are `Not Disclosed`。MTP/AMD/FA3 results have different hidden contracts and cannot be combined。
- **What the Evidence Actually Proves:** under the disclosed single-A100 synthetic ShareGPT mixes, separating partial-Prefill concurrency from the number of concurrently admitted very-long prompts reduces head-of-line blocking and improves several TTFT percentiles with a visible ITL/complexity trade-off。The release also proves that V1 was expanding typed scheduler/cache/speculation/serialization/metrics surfaces toward feature parity。
- **What It Does Not Prove:** it does not prove the default threshold or four slots are optimal, long jobs receive bounded fairness, mixed throughput always increases, the mechanism behaves identically in V1/multi-GPU/PD systems, MTP always yields 1.69×, or the whole release improves production goodput。Metrics availability does not prove metric correctness, alert thresholds or SLO compliance。
- **Limitations / Threats to Validity:** workload is deliberately constructed by character duplication；single GPU and one model omit distributed/cache-transfer effects；ITL degradation is noted；V0 mechanism is transitional；threshold is heuristic；output distribution, repeated trials and confidence are absent。Release breadth, hardware-specific code and initial V1 features enlarge compatibility/failure surface beyond the evaluated scheduler case。
- **Trade-offs / New Failure Modes:** more concurrent partial Prefills reduce short-request blocking but fragment compute, increase KV reservations and can slow Decode cadence；limiting long slots protects Decode/short work but may starve long prompts；centralized hash ownership improves reuse consistency but concentrates invalidation/state bugs；msgpack reduces serialization cost but introduces schema/version compatibility；speculation increases accepted progress only when proposals survive verification；pipeline support adds rank failure and bubble semantics。
- **Where the Previous Design Still Applies:** complete Prefill remains preferable for low-QPS or uniform prompts and maximum GEMM efficiency；one partial Prefill is simpler when memory is tight；V0 remains safer when V1 feature/backend parity is incomplete；no speculation remains preferable at low acceptance or constrained batch opportunity；request-local state remains easier for isolated engines without shared prefix reuse。
- **Evolution Relationship:** `Direct Evolution` from full Prefill → single chunked Prefill → multiple partial Prefills with long-class limits；`Layering / Dependency` between iteration scheduling, KV ownership, speculative commit, pipeline execution and metrics；`Alternative Branch` between V0 stable path and V1 expanding path。The release does not make every branch the new universal default。
- **ROADMAP Node:** canonical owner `INFER-SCHEDULING`（Current Ch56；Legacy Ch52）；handoffs to `INFER-PREFILL` for chunk semantics, `INFER-KV-CACHE` for hash/ownership, `INFER-SPECULATIVE-DECODING` for MTP/n-gram verification, `INFER-VLLM` for engine boundaries and `PLATFORM-OBSERVABILITY` for metric contracts。
- **Target and Adjacent Chapters Read:** read Ch43 Prefill, Ch45 KV Cache, Ch48 Speculative Decoding, Ch50 vLLM and Ch56 Inference Scheduling。Ch43 owns Prefill/KV progress, Ch48 proposal/verification, Ch50 engine composition, while Ch56 owns the cross-request token budget/fairness decision。The release is not a new platform owner。
- **Existing Coverage:** Ch43 already derives chunked-Prefill TTFT/TPOT/throughput trade-offs and warns that a long Prefill can starve Decode；Ch48 already covers n-gram and MTP branches；Ch56 already defines iteration scheduling over Prefill/Decode/speculative work and state-aware fairness。v0.7.3 supplies versioned implementation evidence but no missing durable argument。
- **Integration Decision:** `Books Pending — No Change Candidate`。Historical Books Gate remains closed；the later Books pass should keep the existing evolution and use this release only as bounded evidence, not append its feature list or headline multipliers。
- **Changed Files or Rejection Reason:** added a non-template 30-field signed-tag review；separated the durable concurrent-Prefill policy from 253 release items；bound numbers to the single-A100 constructed workload；mapped V0/V1, KV/speculation/serialization/metrics state to canonical owners；cleared the final W08 pending；no Books change。
- **Open Questions:** immutable benchmark dataset/command/output logs and repetition count；character-to-token length；precision/token cap/output distribution；threshold/slot/request-rate sensitivity；long-request starvation bound；multi-tenant fairness；V1-equivalent policy；multi-GPU/PP/PD/KV-transfer behavior；cancellation/failure/schema migration；MTP acceptance/verification cost；metric definitions, goodput and production SLO。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- AI co-scientist 的 Blog event 属于 W08，论文 v1（2025-02-26）属于 W09 revision/evidence node；两者共享
  `google-ai-co-scientist-workflow` Source Family，不重复计为两个独立机制。
- arXiv:2502.09245、arXiv:2502.11271、MUDDFormer（arXiv:2502.12170）和 SGLang v0.4.3 已按 first-public date spillback W07；MUDDFormer 的 2 月17日 recommendation/discovery date 不替代 2 月13日 v1 event date，且完整 Source Review 已在 owner Weekly 闭合；
  W08 只保存回拨记录，不进入本周分母。
- 后续 revision、模型卡补充和工程集成回链 owner family，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- AI co-scientist → `AGENT-WORKFLOW`（主 owner），并连接 `AGENT-MEMORY`、
  `AGENT-MULTI-AGENT`、`PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`。
- Soundwave → `MULTIMODAL-REPRESENTATION`（主 owner），并连接 `TRAIN-DATA`、`TRAIN-SFT`、
  `INFER-PREFILL-DECODE` 与 `PLATFORM-EVALUATION-SYSTEM`。
- Embedding Space Capacity → `MODEL-EMBEDDING`（主 owner），并连接 `MODEL-LONG-CONTEXT`、
  `AGENT-MEMORY` 与 inference memory state owners。
- S* → `AGENT-WORKFLOW`（主 owner），并连接 `MODEL-SAMPLING`、`AGENT-REFLECTION`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`。
- Magma → `MULTIMODAL-EMBODIED-VLA`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、
  `TRAIN-DATA`、`AGENT-TOOL` 与 `PLATFORM-EVALUATION-SYSTEM`。
- RDLM → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），并连接 `MODEL-SAMPLING`、
  `TRAIN-PRETRAINING`、`INFER-KV-CACHE` 与 `INFER-EXECUTION`。
- Logic-RL → `TRAIN-GRPO`（主 owner），并连接 `TRAIN-PPO`、`TRAIN-RLHF` 与
  `PLATFORM-EVALUATION-SYSTEM`；paper/artifact 配方差异属于 evidence boundary。
- SWE-Lancer → `PLATFORM-EVALUATION-SYSTEM`（主 owner），并连接 `AGENT-TOOL`、
  `AGENT-WORKFLOW`、`PLATFORM-SECURITY` 与 `PLATFORM-COST`。
- TrustGen → `PLATFORM-EVALUATION-SYSTEM`（主 owner），并连接 `PLATFORM-SECURITY`、
  `PLATFORM-MONITORING` 与 modality-specific evaluation handoff；动态 suite 不拥有 policy enforcement。
- MMTEB → `PLATFORM-EVALUATION-SYSTEM`（主 owner），并连接 `MODEL-EMBEDDING`、`AGENT-RAG`、
  `PLATFORM-COST` 与 `PLATFORM-OBSERVABILITY`；benchmark reduction 不拥有 representation mechanism。
- HumanUP → `MULTIMODAL-EMBODIED-VLA`（主 owner），并连接 `MULTIMODAL-WORLD-MODELS`、
  `TRAIN-PPO` 与 `PLATFORM-EVALUATION-SYSTEM`；learned policy 不拥有 actuator safety authority。
- SongGen → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、
  `TRAIN-DATA`、`INFER-PREFILL-DECODE` 与 `PLATFORM-SECURITY`；“single-stage” 不消除 codec、condition encoder、
  data pipeline 与 waveform decoder 的独立 contract。
- Small Model Learnability Gap → `TRAIN-SFT`（主 owner），并连接 `TRAIN-DATA`、`TRAIN-PRETRAINING`、
  `TRAIN-LORA` 与 `PLATFORM-EVALUATION-SYSTEM`；teacher strength 与 trace length 不构成脱离 student/workload 的总序。
- Multimodal Mamba → `MODEL-LONG-CONTEXT`（主 owner），并连接 `MODEL-TRANSFORMER-LAYER`、
  `MULTIMODAL-REPRESENTATION`、`TRAIN-SFT`、`INFER-KV-CACHE` 与 `INFER-EXECUTION`；固定 recurrent state
  不等于可逐 token 精确回读的 KV 或外部记忆。
- RAD → `MULTIMODAL-EMBODIED-VLA`（主 owner），并连接 `MULTIMODAL-WORLD-MODELS`、`TRAIN-RLHF`、
  `TRAIN-PPO` 与 `PLATFORM-EVALUATION-SYSTEM`；3DGS closed-loop evidence 不等于 real-road safety evidence。
- Decomposed Reward Models → `TRAIN-RLHF`（主 owner），并连接 `MODEL-EMBEDDING`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`；PCA variance direction 不等于已命名、已治理的人类价值。
- MoM → `MODEL-LONG-CONTEXT`（主 owner），并连接 `MODEL-MOE`、`INFER-KV-CACHE` 与 `INFER-EXECUTION`；
  routed recurrent state bank 不等于 token-addressable KV，也不等于 external memory。
- FLAG-Trader → `TRAIN-PPO`（主 owner），并连接 `TRAIN-RLHF`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`；历史回测不等于可部署 action authority。
- SoFar → `MULTIMODAL-EMBODIED-VLA`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、
  `MULTIMODAL-WORLD-MODELS` 与 `PLATFORM-EVALUATION-SYSTEM`；semantic orientation 的语言接口不取消
  camera/world/tool frame，也不把 VLM proposal 升级为 actuator authority。
- Craw4LLM → `TRAIN-DATA`（主 owner），并连接 `TRAIN-PRETRAINING`、`PLATFORM-COST` 与
  `PLATFORM-SECURITY`；quality-aware frontier 不拥有 downstream optimizer，也不能用 selected-corpus ratio 代替
  all-fetched network/accounting contract。
- PC-Agent → `AGENT-WORKFLOW`（主 owner），并连接 `AGENT-MULTI-AGENT`、`AGENT-TOOL`、
  `AGENT-REFLECTION` 与 `PLATFORM-EVALUATION-SYSTEM`；hierarchical role feedback 不等于 durable workflow、
  transaction rollback 或 production action authority。
- S2R → `TRAIN-GRPO`（主 owner），并连接 `TRAIN-SFT`、`TRAIN-RLHF`、`TRAIN-PPO`、
  `AGENT-REFLECTION`、`MODEL-SAMPLING` 与 `PLATFORM-EVALUATION-SYSTEM`；self-verdict 是 policy output，
  rule-based golden verifier 才是该实验的 reward authority。
- Selective Question Answering → `PLATFORM-EVALUATION-SYSTEM`（主 owner），并连接 `MODEL-SAMPLING`、
  `INFER-SCHEDULING`、`AGENT-PLANNING`、`PLATFORM-COST` 与 `PLATFORM-SECURITY`；answer log-probability
  是 model-relative selection signal，不是 correctness 或 high-stakes action authority。
- SafeRoute → `PLATFORM-SECURITY`（主 owner），并连接 `PLATFORM-GATEWAY`、`PLATFORM-EVALUATION-SYSTEM`、
  `PLATFORM-COST` 与 `INFER-SCHEDULING`；router/guard 都是 policy-bound sensors，不能替代 deterministic
  enforcement、fail-safe policy 或 human escalation。
- RelaCtrl → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、
  `TRAIN-PRETRAINING`、`INFER-TENSORRT-LLM` 与 `PLATFORM-EVALUATION-SYSTEM`；CRS 是特定 workload 的
  offline allocation signal，不是通用层重要性或在线 request-routing authority。
- YOLOv12 → `MODEL-SELF-ATTENTION`（主 owner），并连接 `MODEL-POSITION-ENCODING`、`MODEL-FFN`、
  `MODEL-TRANSFORMER-LAYER`、`MULTIMODAL-REPRESENTATION`、`TRAIN-PRETRAINING`、
  `INFER-TENSORRT-LLM` 与 `PLATFORM-EVALUATION-SYSTEM`；Area Attention 是 COCO-640 workload 下的
  regional exact-Attention branch，不是从 CNN 到 Attention 的通用替代结论。
- CLIPPER → `TRAIN-DATA`（主 owner），并连接 `TRAIN-SFT`、`MODEL-LONG-CONTEXT`、
  `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-COST` 与 `PLATFORM-SECURITY`；compressed evidence 是
  可追溯但有损的 label-compilation 中间态，不是 raw source 或独立 correctness oracle。
- Explorer → `TRAIN-DATA`（主 owner），并连接 `TRAIN-SFT`、`AGENT-WORKFLOW`、`AGENT-PLATFORM`、
  `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-COST` 与 `PLATFORM-SECURITY`；live exploration 生成的是
  environment-conditioned candidate trajectory，shared-model verifier verdict 不能自动成为 outcome truth。
- Template-Anchored Safety → `PLATFORM-SECURITY`（主 owner），并连接 `MODEL-SELF-ATTENTION`、
  `MODEL-TRANSFORMER-LAYER`、`TRAIN-RLHF` 与 `PLATFORM-EVALUATION-SYSTEM`；attention/probe/steering 是
  白盒机制证据与 policy-bound sensor，不是通用安全证书或 tool authorization authority。
- NExT-Mol → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、
  `MODEL-TOKENIZER`、`TRAIN-DATA`、`TRAIN-PRETRAINING`、`TRAIN-LORA` 与 `PLATFORM-EVALUATION-SYSTEM`；
  SELFIES validity 与 learned property proxy 不等于 synthesizability、physical truth 或 discovery outcome。
- video-SALMONN-o1 → `TRAIN-DPO`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、`TRAIN-DATA`、
  `TRAIN-SFT` 与 `PLATFORM-EVALUATION-SYSTEM`；rollout-estimated process preference 是受 judge、trajectory、
  perturbation 与 reference-policy identity 约束的训练分支，显式 reasoning trace 不等于 faithful explanation。
- InfiR → `TRAIN-DATA`（主 owner），并连接 `TRAIN-PRETRAINING`、`TRAIN-SFT`、
  `MULTIMODAL-REPRESENTATION` 与 `PLATFORM-EVALUATION-SYSTEM`；小模型的 mixture、synthetic data、
  evaluation mode 与 freeze schedule 是分阶段 contract，论文配方和 benchmark 不构成通用 recipe。
- LongPO → `TRAIN-DPO`（主 owner），并连接 `MODEL-LONG-CONTEXT`、`TRAIN-DATA`、
  `TRAIN-DISTRIBUTED-TRAINING` 与 `PLATFORM-EVALUATION-SYSTEM`；short-to-long reference 是跨输入条件的
  preference branch，不等于 same-context DPO，也不证明局部 chunk teacher 能覆盖全局长文推理。
- Temporal Heads → `WORLDVIEW-REPRESENTATION`（主 owner），并连接 `MODEL-SELF-ATTENTION`、
  `MODEL-TRANSFORMER-LAYER`、`PLATFORM-EVALUATION-SYSTEM`、`AGENT-RAG` 与 `AGENT-MEMORY`；局部
  ablation/injection 是受模型、prompt、threshold 与 hook 约束的机制证据，不等于几个 head 独占时间知识。
- LongWriter-V → `TRAIN-DPO`（主 owner），并连接 `TRAIN-SFT`、`TRAIN-DATA`、
  `MULTIMODAL-REPRESENTATION`、`INFER-PREFILL-DECODE`、`AGENT-WORKFLOW` 与
  `PLATFORM-EVALUATION-SYSTEM`；累计 prefix pair 提高反馈复用，但不是独立偏好样本数的等比扩张。
- Intuitive Physics from Natural Videos → `MULTIMODAL-WORLD-MODELS`（主 owner），并连接
  `MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`、
  `TRAIN-PRETRAINING` 与 `PLATFORM-EVALUATION-SYSTEM`；latent surprise 证明的是受限 observation-prediction
  evidence，不等于 action-conditioned transition、persistent state 或 planning authority。
- Autellix → `INFER-SCHEDULING`（主 owner），并连接 `INFER-KV-CACHE`、`INFER-SGLANG`、`INFER-DYNAMO`、
  `PLATFORM-GATEWAY`、`PLATFORM-EVALUATION-SYSTEM` 与 `AGENT-WORKFLOW`；program/thread metadata 是
  narrow scheduling hint，不是业务 DAG、tool authority 或 durable workflow truth。
- Sailor2 → `TRAIN-DATA`（主 owner），并连接 `TRAIN-PRETRAINING`、`TRAIN-SFT`、`TRAIN-DPO`、
  `TRAIN-DISTRIBUTED-TRAINING`、`MODEL-TOKENIZER`、`MODEL-LONG-CONTEXT`、
  `INFER-SPECULATIVE-DECODING` 与 `PLATFORM-EVALUATION-SYSTEM`；data/mixture identity 是主 contract，
  不把一个端到端技术报告拆成多个重复 owner。
- Thinking Preference Optimization → `TRAIN-DPO`（主 owner），并连接 `TRAIN-SFT`、`MODEL-SAMPLING` 与
  `PLATFORM-EVALUATION-SYSTEM`；长短 pair 是受 teacher、correctness、style 与 source-model identity 混杂的弱偏好，
  不把输出长度或 reasoning-style token 升级为 reasoning truth。
- HermesFlow → `TRAIN-DPO`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`TRAIN-DATA` 与 `PLATFORM-EVALUATION-SYSTEM`；homologous record
  保留跨方向身份，但 self-score 不拥有 truth，Equation 12→15 的非等价推导使 product objective 保持 `Disputed`。
- Atom of Thoughts → `AGENT-PLANNING`（主 owner），并连接 `AGENT-CONTEXT`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；temporary DAG 可指导 contraction，但自然语言 next-state
  只是 derived view，未通过 preservation/equivalence 检查时不能取代 raw reasoning、provenance 或 durable workflow state。
- Dynamic Concepts Personalization → `MULTIMODAL-REPRESENTATION`（主 owner），并连接
  `MULTIMODAL-GENERATIVE-PARADIGMS`、`TRAIN-LORA`、`TRAIN-DATA` 与 `PLATFORM-EVALUATION-SYSTEM`；
  appearance/motion basis-residual 是 staged parameterization，不等于已证明的语义 disentanglement。
- RealSyn → `TRAIN-DATA`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、`TRAIN-PRETRAINING`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-SECURITY`；retrieved/generated text 是 derived association，
  embedding similarity 与 cluster quota 不拥有 pair truth、source rights 或 universal data-quality semantics。
- Diffusion-Sharpening → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），并连接 `TRAIN-SFT`、`TRAIN-DPO`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；training-time trajectory search 可以把 request-time work
  amortize 到 artifact，但公开 reward term 的梯度、same-prompt pair identity 与完整成本保持 `Disputed`。
- Revisiting Test-time Scaling → `MODEL-SAMPLING`（主 owner），并连接 `AGENT-REFLECTION`、`AGENT-PLANNING`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；自然输出长度是 trajectory diagnostic，不拥有 correctness；
  sequential depth、parallel coverage 与 selection accuracy 必须在完整 compute / state / SLO contract 下分开核算。
- AlphaMaze → `TRAIN-GRPO`（主 owner），并连接 `TRAIN-SFT`、`MULTIMODAL-REPRESENTATION`、
  `AGENT-PLANNING`、`MULTIMODAL-EMBODIED-VLA` 与 `PLATFORM-EVALUATION-SYSTEM`；symbolic maze、reset
  demonstration、grouped policy update 与 executable transition 是分层 contract；86%→93% attribution 保持 `Disputed`。
- PAFT → `TRAIN-SFT`（主 owner），并连接 `TRAIN-DATA`、`AGENT-PROMPT`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；prompt pool 是 versioned training distribution，
  不能用 same-generator string holdout 代替生产 prompt shift，也不能用缺失 workload contract 的 runtime 表证明通用加速。
- CoSyn → `TRAIN-DATA`（主 owner），并连接 `MULTIMODAL-REPRESENTATION`、`TRAIN-SFT`、
  `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`、`AGENT-TOOL` 与 `PLATFORM-COST`；executable
  render code 同时派生 observation 与 label，但 shared ontology 的一致错误、sandbox、artifact drift 与 real-data gap 必须保留。
- LServe → `INFER-KV-CACHE`（主 owner），并连接 `MODEL-LONG-CONTEXT`、`INFER-PREFILL`、`INFER-DECODE`、
  `INFER-PAGED-ATTENTION`、`INFER-TENSORRT-LLM`、`INFER-SCHEDULING` 与 `PLATFORM-EVALUATION-SYSTEM`；
  semantic selection page 与 physical transfer page 可以分层，但 profile、summary、budget、reuse epoch 与 cache identity 必须一起版本化。
- From RAG to Memory / HippoRAG 2 → `AGENT-RAG`（主 owner），并连接 `AGENT-CONTEXT`、`AGENT-MEMORY`、
  `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY` 与 `PLATFORM-COST`；phrase graph、passage node、dense reset mass
  与 PPR 是 derived retrieval state，不是 durable Memory 或 fact authority，source/version/ACL/delete lineage 必须保持可追溯。
- LoRAM → `TRAIN-LORA`（主 owner），并连接 `TRAIN-PRETRAINING`、`TRAIN-SFT`、`TRAIN-CHECKPOINT`、
  `PLATFORM-MODEL-REGISTRY`、`PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；training carrier 与 inference base
  可以分离，但 mask、aligned carrier、adapter、recovery mapping、base 与 post-conversion evidence 必须组成不可拆的 lineage。
- Text2World → `MULTIMODAL-WORLD-MODELS`（主 owner），并连接 `AGENT-PLANNING`、`AGENT-WORKFLOW`、
  `PLATFORM-EVALUATION-SYSTEM`、`TRAIN-SFT` 与 `MULTIMODAL-EMBODIED-VLA`；PDDL proposal、parser validity、
  reference match、semantic equivalence 与 environment truth 是不同 evidence level，不能把可解析直接升级为正确 world transition。
- HeadInfer → `INFER-KV-CACHE`（主 owner），并连接 `MODEL-LONG-CONTEXT`、`INFER-PREFILL`、
  `INFER-DECODE`、`INFER-PAGED-ATTENTION` 与 `INFER-GPU-MEMORY`；head-wise exact offload 降低 resident
  HBM 下界，却把 host capacity、PCIe traffic、launch overhead 与 TPOT 带入同一 placement contract。
- AdaptiveStep → `TRAIN-RLHF`（主 owner），并连接 `TRAIN-GRPO`、`MODEL-SAMPLING`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；policy confidence、boundary、rollout viability、
  process reward 与 causal correctness 是不同状态，且 TVD 的 online scorer cost 不能被省略。
- AIDE → `AGENT-WORKFLOW`（主 owner），并连接 `AGENT-PLANNING`、`AGENT-REFLECTION`、
  `AGENT-MEMORY`、`AGENT-TOOL-CALLING`、`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-WORKLOAD` 与
  `PLATFORM-SECURITY`；Journal 中的 candidate、lineage、run 与 metric 是外部 artifact state，模型只提出变异，
  evaluator 与 Workflow 分别拥有证据和选择权。2025 论文事件不得覆盖 2024 Source Family first-public date。
- Model-guidance → `MULTIMODAL-GENERATIVE-PARADIGMS`（主 owner），并连接 `TRAIN-PRETRAINING`、
  `PLATFORM-EVALUATION-SYSTEM` 与 `PLATFORM-COST`；它把 request-time conditional/unconditional score difference
  amortize 到 training target，但最佳配方仍含 empty-label estimator 与额外 EMA forwards，不能命名为完全消除 CFG。
- Transformers v4.49.0 → `PLATFORM-MODEL-REGISTRY`（主 owner），并连接 `INFER-KV-CACHE`、
  `MULTIMODAL-REPRESENTATION`、`TRAIN-DISTRIBUTED-TRAINING` 与 `PLATFORM-EVALUATION-SYSTEM`；tag、config、
  processor、cache、quantizer 与 parallel plan 共同构成 executable compatibility identity，Release 不能替代下游 regression evidence。
- Accelerate v1.4.0 → `TRAIN-DISTRIBUTED-TRAINING`（主 owner），并连接 TP、`TRAIN-CHECKPOINT`、
  `PLATFORM-TRAINING-OPERATOR` 与 `PLATFORM-EVALUATION-SYSTEM`；thin wrapper 仍拥有 process-group、precision、
  batch-routing 与 object-lifetime boundary，但不拥有 collective math、kernel、scheduler 或 checkpoint transaction。
- vLLM v0.7.3 → `INFER-SCHEDULING`（主 owner），并连接 `INFER-PREFILL`、`INFER-KV-CACHE`、
  `INFER-SPECULATIVE-DECODING`、`INFER-VLLM` 与 `PLATFORM-OBSERVABILITY`；partial-Prefill slots、long-request
  limits、KV hash、proposal commit、wire schema 与 metrics 分属不同状态 owner，不能压缩成一个版本速度结论。

## Recommended Action

- AI co-scientist：Weekly evidence complete；Books Pending。
- Magma：Weekly evidence complete；Books Pending；不得把 3 月后的训练代码/数据倒写为 W08 event-time artifact。
- RDLM：Weekly evidence complete；Books Pending；small-model likelihood evidence 不外推为大模型 serving 收益。
- Logic-RL：Weekly evidence complete；Books Pending；公开 GRPO launcher 不作为论文 modified REINFORCE++ 结果的复现证明。
- SWE-Lancer：Weekly evidence complete；Books Pending；payout 只作该 benchmark 的 task weight，不外推为劳动替代或通用难度。
- TrustGen：Weekly evidence complete；Books Pending；v1 的动态评测机制与当前 toolkit/ICLR 版本分开版本化。
- MMTEB：Weekly evidence complete；Books Pending；缩减 suite 必须与完整 reference suite、pool models 与版本身份共存。
- HumanUP：Weekly evidence complete；Books Pending；simulation success、real feasibility 与 certified safety 保持分层。
- SongGen：Weekly evidence complete；Books Pending；mixed、parallel 与 interleaving 是不同成本/控制分支，后者不覆盖前者。
- Small Model Learnability Gap：Weekly evidence complete；Books Pending；1:4 mixture 与 <=3B 仅为作者实验 operating point。
- Multimodal Mamba：Weekly evidence complete；Books Pending；保留 Transformer、pure SSM 与 hybrid 的共存边界。
- RAD：Weekly evidence complete；Books Pending；保留 pure IL、pure RL、hybrid post-training 与显式 simulator 的共存边界。
- Decomposed Reward Models：Weekly evidence complete；Books Pending；把 scalar、explicit semantic heads、latent PCA basis 与
  per-user training 保留为条件分支。
- Quantum Error Correction with RL：18/30；Low-score verified；领域算法结果保留 Weekly，不强行映射 Books。
- MoM：Weekly evidence complete；Books Pending；保留 single state、routed state bank、hybrid 与 dense KV 的共存边界。
- FLAG-Trader：Weekly evidence complete；Books Pending；只沉淀 environment-coupled policy training 与 evidence gate。
- SoFar：Weekly evidence complete；Books Pending；保留 canonical pose、semantic orientation、controller 与 closed-loop VLA
  的共存边界，不把 9 月 revision/artifact 倒写为 2 月事实。
- Craw4LLM：Weekly evidence complete；Books Pending；保留 connectivity-first、post-filter 与 utility-aware frontier 的共存边界，
  并把 21% selected set 与 48% all-visited/fetched accounting 分开。
- PC-Agent：Weekly evidence complete；Books Pending；保留 single-agent/direct API 与 hierarchical GUI workflow 的条件分支，
  不把 visual recovery rate 写成 durable rollback。
- S2R：Weekly evidence complete；Books Pending；保留 direct SFT、long-CoT distillation、outcome/process reward 与 online/offline RL
  的条件分支，不把 same-model self-verification 写成独立 correctness oracle。
- Selective Question Answering：Weekly evidence complete；Books Pending；保留 always-answer、abstain、external verifier 与 human
  escalation 的条件分支，不把 0.95 threshold 或 Jeopardy utility 写成通用生产 operating point。
- SafeRoute：Weekly evidence complete；Books Pending；保留 large-only、small-only、calibrated uncertainty、pair-specific router 与
  deterministic/human enforcement 的条件分支，不把 routing F1 或平均 latency 曲线升级为安全保证。
- RelaCtrl：Weekly evidence complete；Books Pending；保留 copied block、token concatenation 与 relevance-budgeted control 的
  条件分支，不把单层删除分数写成通用因果层重要性，也不把 batch-1 GFLOPs reduction 写成 serving goodput。
- YOLOv12：Weekly evidence complete；Books Pending；保留 CNN、global/window/linear/area Attention 的条件分支，
  不把固定 COCO-640 与 T4 TensorRT FP16 结果外推为通用实时或高分辨率结论。
- CLIPPER：Weekly evidence complete；Books Pending；保留 direct、chapter-local、compressed-synthetic 与 human-authored
  supervision 的条件分支，并把 filtering cost、lossy evidence、judge dependence 与 specialization regression 写入同一 contract。
- Explorer：Weekly evidence complete；Books Pending；保留 human、tutorial、task-first、sandbox/specification-first 与 live
  exploration 的条件分支，不把 URL 数、shared verifier acceptance 或 selected-live maximum 写成 correctness/coverage truth。
- Template-Anchored Safety：Weekly evidence complete；Books Pending；保留 training alignment、template versioning、external guard、
  generation-time monitor/steering 与 deterministic enforcement 的分层，不把 probe accuracy 或受限 ASR 降幅升级为安全保证。
- NExT-Mol：Weekly evidence complete；Books Pending；保留 joint diffusion、staged SELFIES→3D、geometric inductive bias 与
  explicit physics 的条件分支，不把 validity/FCD/COV 或 property-classifier MAE 升级为药物发现或物理正确性。
- video-SALMONN-o1：Weekly evidence complete；Books Pending；保留 direct-answer SFT、explicit-reasoning SFT、full-path DPO、
  process-local DPO、external PRM 与 online reranking 的条件分支，不把 judge/rollout preference 写成真实过程 ground truth。
- InfiR：Weekly evidence complete；Books Pending；保留 broad/static data、capacity-aware filtering、stage-specific annealing、
  human/synthetic SFT 与 joint/staged multimodal training 的条件分支，不把小模型尺寸写成隐私、edge SLO 或可持续性证明。
- LongPO：Weekly evidence complete；Books Pending；保留 same-context DPO、long SFT、retrieval 与 short-to-long reference 的
  条件分支，并把 teacher succession、local-evidence bias、formula/config/result drift 纳入同一版本化 contract。
- Temporal Heads：Weekly evidence complete；Books Pending；保留 behavioral evaluation、probe、circuit intervention、RAG 与
  global editing 的证据/设计分支，不把局部 head location 或 activation injection 写成可部署 temporal truth store。
- LongWriter-V：Weekly evidence complete；Books Pending；保留 short response、long-output SFT、whole-document DPO、
  cumulative-prefix DPO 与 inference-time writing Agent 的条件分支，不把长度达标、GPT judge 或相关 prefix 数量写成质量 truth。
- Intuitive Physics from Natural Videos：Weekly evidence complete；Books Pending；保留 explicit simulator、pixel generation、
  object-centric dynamics、latent prediction 与 action-conditioned world model 的条件分支，不把 property-tuned surprise 写成完整物理理解。
- Autellix：Weekly evidence complete；Books Pending；保留 stateless FCFS、request MLFQ、program-attained service、
  explicit DAG scheduler 与 locality-aware routing 的条件分支，不把 replayed program-token latency 升级为生产 Agent SLO。
- Sailor2：Weekly evidence complete；Books Pending；保留 from-scratch、uniform mixture、direct CPT、model expansion、
  two-stage curriculum 与 parameter-selective adaptation 的条件分支，不把 500B、SWB 或 RULER headline 升级为通用结论。
- Thinking Preference Optimization：Weekly evidence complete；Books Pending；只作为 DPO pair construction 与 length
  confounding 的受限案例，保留 SFT、correctness-labelled/length-regularized DPO、verifier/RL 与 concise decoding 分支。
- HermesFlow：Weekly evidence complete；`Disputed — Books Frozen`；先解决 paper/code objective、两个 evaluator 的
  comparability 与独立 scorer，再判断 homologous preference lineage 是否值得沉淀。
- Atom of Thoughts：Weekly evidence complete；Books Pending；保留 full-history、persistent tree/DAG、retrieval 与
  contracted-state 分支，不把作者命名的 Markov property、selected-depth accuracy 或未披露的 cost claim 写成通用结论。
- Dynamic Concepts Personalization：Weekly evidence complete；Books Pending；保留 single adapter、architecture-factorized、
  Set-before-Sequence residual 与 feed-forward encoder 分支，不把私有 backbone、小型自建集或 proxy score 写成通用结论。
- RealSyn：Weekly evidence complete；Books Pending；保留 explicit/local pairs、global retrieval、synthetic augmentation 与
  raw interleaved sequences 的条件分支，不把平均 CLIP 改善、窄范围 curve fit 或公开 dataset card 写成通用质量、合规或 scaling law。
- Diffusion-Sharpening：Weekly evidence complete；`Disputed — Books Frozen`；先解决 zero-gradient reward term、cross-prompt
  pair risk、paper/code config 与 equal-total-compute evidence，再判断 trajectory amortization 是否值得 refine。
- Revisiting Test-time Scaling：Weekly evidence complete；Books Pending；保留 sequential revision、parallel sampling、ordinary
  majority、length-aware selector、external verifier 与 abstention 的条件分支，不把相关性写成长度的因果效应，也不把
  generated-token parity 写成完整 cost parity。
- AlphaMaze：18/30；Full Source Review complete；`Disputed — Weekly Only / Books Frozen`；在 v2 结果、结论、baseline、
  GRPO 实施与 event-time artifact 互相一致前，不吸收 86%→93%、emergent self-correction 或 robotics-transfer 结论。
- PAFT：Weekly evidence complete；Books Pending；保留 fixed template、single-prompt optimization、prompt-distribution SFT、
  gateway normalization 与后续 adversarial/curriculum sampling 的条件分支，不把 string holdout 写成 prompt agnosticism，
  也不把 3.25× 表格写成生产 serving 结论。
- CoSyn：Weekly evidence complete；Books Pending；保留 human/natural data、handwritten templates、caption-first synthesis 与
  executable render specification 的条件分支；未来只沉淀 code/image/label lineage、sandbox 和 independent real-data gate，
  不把作者 benchmark 或 current mutable artifact 写成 synthetic-data replacement law。
- LServe：Weekly evidence complete；Books Pending；保留 dense、quantized-only、static streaming、dynamic selected、
  hierarchical paging 与 tiered/offloaded KV 分支；不把 fixed 4K/8K budget、“free lunch”或作者 normalized throughput
  写成普适 exactness / production SLO，也不忽略 selector 的线性复杂度。
- From RAG to Memory / HippoRAG 2：Weekly evidence complete；Books Pending；保留 lexical/dense top-k、phrase graph、
  curated KG、hierarchical summary 与 mixed dense/relational PPR 分支；不把标题中的 Memory/continual learning、7% associative
  headline 或 mutable current repository 写成 durable Memory、在线更新或 production RAG 结论。
- LoRAM：Weekly evidence complete；`Disputed — Books Frozen`；在作者给出与 Eq.3–5 mask 定义、structured dimension
  recovery 和 q-projection code 一致的 executable contract 前，只保留 train-carrier/inference-base 分离的研究问题，
  不把 15.81×/16.95× parameter storage 或 20GB headline 写成 end-to-end memory/cost 结论。
- Text2World：Weekly evidence complete；Books Pending；保留 hand-authored simulator、symbolic transition specification、
  latent/video dynamics 与 end-to-end environment evaluation 的条件分支，不把 parser executability、单一 reference F1 或
  cross-family model ranking 写成环境正确性、RL 因果效应或 production Agent capability。
- HeadInfer：Weekly evidence complete；Books Pending；保留 FullKV、chunked prefill、layer-wise offload、head-group offload、
  lossy compression 与 distributed placement 的条件分支；不把单请求 capacity 写成 production throughput，也不把
  current simulation artifact 当作 1M/4M semantic reproduction。
- AdaptiveStep：Weekly evidence complete；`Disputed — Books Frozen`；在 zero-overhead、loss sign、boundary index、
  matched-budget 与 threshold sensitivity 得到可执行核验前，不把 low confidence 写成 reasoning truth，也不把 TVD
  写成无额外推理成本。
- AIDE：Weekly evidence complete；`Books Pending — No Change Candidate`；保留 fixed AutoML、monolithic Agent、
  greedy code-space tree、population/Pareto search 与 human-led research 的条件分支，不把 scalar evaluator、短反馈 sandbox
  或 2025 formal paper 写成通用 production workflow、模型自我改进或机制 first-public date。
- Model-guidance：Weekly evidence complete；`Disputed Scope Claim — Books Frozen`；只保留“推理期 guidance → 训练期
  guidance amortization”的候选路线，不把 one-pass NFE、FID 或 convergence-in-steps 写成完全消除 CFG、端到端训练加速或
  production serving speedup。
- Transformers v4.49.0：Weekly evidence complete；`Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate`；
  保留 legacy/typed cache、dynamic/static cache、slow/fast processor、manual/default parallel plan 与多 quantizer backend 的共存边界，
  不把 Release 功能表、上游 CI 或模型作者数字写成生产性能与完整兼容性证明。
- Accelerate v1.4.0：Weekly evidence complete；`Books Pending — No Change Candidate`；保留 explicit PyTorch、DP/FSDP/TP、
  rank-local/same-batch DataLoader 与 FP16/BF16/FP8 分支，不把 4 张未披露 GPU 上的作者 PR 表格写成通用速度结论。
- vLLM v0.7.3：Weekly evidence complete；`Books Pending — No Change Candidate`；保留 complete/single/multiple partial Prefill、
  V0/V1、no-speculation/n-gram/MTP 与 local/distributed engine 分支；不把 constructed single-A100 TTFT 或不同硬件 PR 数字
  合并成 Release-wide production goodput 结论。
- W08 的 65/65 owner family 已有最终 disposition；Candidate Evidence Gate 通过。按用户要求，forward cursor 在进入 W09 前暂停。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Historical Books Gate 关闭。本任务只重建 Weekly evidence；当前已完成的 AI co-scientist、MLGym、
Qwen2.5-VL、SigLIP 2、SuperGPQA、LoRA Knowledge Capacity、Soundwave、Embedding Space Capacity、S*、Magma、RDLM、Logic-RL、SWE-Lancer、TrustGen、MMTEB、HumanUP、SongGen、Small Model Learnability Gap、Multimodal Mamba、RAD、Decomposed Reward Models、MoM、FLAG-Trader、SoFar、Craw4LLM、PC-Agent、S2R、Selective Question Answering、SafeRoute、RelaCtrl、YOLOv12、CLIPPER、Explorer、Template-Anchored Safety、NExT-Mol、video-SALMONN-o1、InfiR、LongPO、Temporal Heads、LongWriter-V、Intuitive Physics from Natural Videos、Autellix、Sailor2、Thinking Preference Optimization、Atom of Thoughts、Dynamic Concepts Personalization、RealSyn、Revisiting Test-time Scaling、PAFT、CoSyn、LServe、From RAG to Memory / HippoRAG 2、Text2World 与 HeadInfer Source Family 标记为 `Books Pending — Integration Deferred`；AIDE、Accelerate v1.4.0 与 vLLM v0.7.3 标记为 `Books Pending — No Change Candidate`；Transformers v4.49.0 标记为 `Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate`；HermesFlow、Diffusion-Sharpening、AlphaMaze、LoRAM、AdaptiveStep 与 Model-guidance 标记为 `Disputed — Books Frozen`；Quantum Error Correction with RL 标记为 `Weekly Only — Low-score / Outside Knowledge-tree Scope`。W08 Weekly evidence 已闭合，
不修改 `books/`。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 幂等重建 `papers/2025/weekly/2025-W08/README.md` 的 discovery / ownership ledger。
- 完成 LongPO 的 v1 全文、公式、实验、appendix、repository 与 checkpoint-card 联合核验，并保留 paper/code/card drift。
- 完成 Temporal Heads 的 v1 全文、公式、EAP-IG、ablation/editing、appendix 与后续官方 artifact 联合核验。
- 完成 LongWriter-V 的 31 页 v1 PDF、数据/训练、IterDPO、评测、人类反馈、appendix 与官方 repository 联合核验。
- 完成 Intuitive Physics from Natural Videos 的 v1 全文、latent predictor、training/evaluation contract、
  context/data/model ablation、全部 appendix 与官方 evaluation artifact 联合核验。
- 完成 Autellix 的 v1 全文、PLAS/ATLAS、process table、preemption/KV swap、locality routing、
  workload/testbed、全部 ablation 与 artifact availability 核验。
- 完成 Sailor2 的 v1 全文、2024 release chronology、data/mixture、CPT、SFT/DPO、distributed-training、
  long-context/speculation/pruning、evaluation/ablation 与官方 component/model artifact 联合核验。
- 完成 Thinking Preference Optimization 的 v1 全文、pair construction、SFT→DPO pipeline、跨模型结果、
  length-gap/temperature ablation、appendix、repository 与 model/data release chronology 联合核验。
- 完成 HermesFlow 的 v1 全文、homologous preference curation、Pair-DPO/self-play、完整实验与 ablation、
  formula appendix、repository/checkpoint 联合核验，并把 objective 非等价与 evaluator mismatch 标记为 `Disputed`。
- 完成 Atom of Thoughts 的 v1 全文、DAG decomposition/contraction、plugin path、完整 benchmark、depth/cost/ablation、
  failure appendix 与 current repository 联合核验，并把 contraction preservation、survivor selection 与成本缺口写入证据边界。
- 完成 Dynamic Concepts Personalization 的 v1 全文、Set-and-Sequence LoRA、regularization、private-DiT contract、
  完整 ablation/user study/appendix 与官方项目页核验，并把 factorization、metric、dataset 与 artifact 缺口写入证据边界。
- 完成 RealSyn 的 v1 全文、interleaved-document extraction、hierarchical retrieval、synthetic generation、semantic filtering、
  balancing、完整 CLIP evaluation/ablation/appendix 与官方 repository/dataset artifact 联合核验，并把 negative ablation、
  global-pair provenance、artifact drift、rights 与完整成本缺口写入证据边界。
- 完成 Diffusion-Sharpening 的 v1 全文、trajectory/reward/SFT/RLHF mechanism、完整 evaluation/efficiency/ablation/appendix、
  grader prompt 与官方 SFT/RLHF source paths 联合核验，并把 zero-gradient reward term、cross-prompt pair risk、
  paper/code configuration drift 与 equal-total-compute 缺口标记为 `Disputed`。
- 完成 Revisiting Test-time Scaling 的 v1 全文、length/accuracy cohort、forced sequential revision、parallel sampling、
  Shortest Majority Vote、全部 appendix 与官方 evaluation repository 联合核验，并把 correlation/causality、coverage/selection、
  evaluator union、generated-token/accounted-cost 与 statistical-contract 边界写入 Source Review。
- 完成 AlphaMaze 的 v1/v2 周内 revision、symbolic maze、reset demonstration、SFT→GRPO dataflow、reward、MazeBench、
  appendix algorithms 与当前 author model/data artifacts 联合核验；因 Results/Discussion 的 86%→93% 与 Conclusion 的
  75%→77%/GRPO future-work 互相冲突，将评分校正为 18/30 并标记 `Disputed — Weekly Only / Books Frozen`。
- 完成 PAFT 的 v1 全文、prompt-pool construction、dynamic SFT sampler、五任务评测、K/epoch/prompt-count ablation 与
  training/inference cost appendix 核验；把 400/450 prompt count、same-generator split、prompt-level variance 与缺失
  decoding/hardware/token/SLO contract 写入证据边界，并标记为 `Books Pending — Refine Existing Argument Candidate`。
- 完成 CoSyn 的 v1 全文、code-mediated generation factorization、20-pipeline/11-renderer dataflow、data-mixture/CoT/
  diversity/scale/generator/pointing experiments、完整 appendix 与 current official code/dataset/evaluator artifacts 联合核验；
  分离 W08 的 20 pipelines/9 categories/400K/65K 与后续 25 pipelines/10 subsets/408,227/68.1K artifact lineage，
  并把 shared-ontology error、sandbox、real-data gap 与 benchmark/evaluator contract 写入 Source Review。
- 完成 LServe 的 v1 全文、offline head profiling、two-way paged KV、hierarchical logical/physical page selection、
  reusable selector、quantized sparse kernels、完整 accuracy/efficiency/ablation 与 current OmniServe artifact 联合核验；
  把 RULER/task loss、selector linearity、profile/cache identity、eight-versus-ten benchmark rows、4.5×/7.7× figure-text
  冲突与缺失的 production SLO contract 写入 Source Review。
- 完成 From RAG to Memory / HippoRAG 2 的 v1 全文、OpenIE/synonym/passages graph、query-to-triple filter、mixed reset PPR、
  dense fallback、七数据集评测、ablation/sensitivity/error/cost appendices 与 current official repository 联合核验；
  把 derived graph 与 fact/Memory authority 分离，并记录 18% zero-triple fallback、Table 11 artifact mismatch、RAPTOR
  cost exception、缺失 update/delete/ACL/online-SLO 与 current-repository drift。
- 完成 LoRAM 的 v1 全文、prune→align→SFT→recover→full-base inference dataflow、公式/算法、全部任务/ablation/
  scaling/cost appendices 与 current official training/recovery paths 联合核验；分离 parameter-storage、13B measured peak
  memory 与 total lifecycle cost，并因 Eq.3–5 mask contradiction、v2 未修复及 visible q-projection recovery gap 标记
  `Disputed — Books Frozen`。
- 完成 Text2World 的 v1 全文、PDDL transition specification、1,801→264→103 construction pipeline、parser/component metrics、
  16-model/correction/few-shot/fine-tuning/agent-training/concrete-description experiments、error/limitation appendices，以及官方
  project、current benchmark/evaluator/config artifact 联合核验；分离 parser validity、reference match、semantic equivalence 与
  environment truth，并把 v2/ACL/current repository 保留为后续 lineage。
- 完成 HeadInfer 的 v1 全文、head-wise KV decomposition、chunked prefill、adaptive grouping、ping-pong transfer、roofline、
  context/memory/latency/throughput/ablation/appendix 与 current public artifact 联合核验；分离 exact dense offload 与 optional
  sparse branch，记录 7B13/7V12 hardware conflict 及 simulation-only headline artifact，并把 1M/4M capacity 与 TPOT 一起保存。
- 完成 AdaptiveStep 的 v1 全文、confidence boundary、rollout hard label、PRM/TVD、BoN/transfer/generalization/feature
  appendices 与 current training/evaluation/model/data artifact 联合核验；分离 surprise、decision boundary、viability 与 causal
  correctness，并因 zero-overhead claim 对双服务 Top-M scorer、Eq.3 sign 与 step-index contract 冲突冻结 Books。
- 完成 AIDE 的 v1 全文、formal solution-tree algorithm、draft/debug/improve policy、Weco-Kaggle、MLE-bench、RE-Bench、
  全部 appendix、2024 technical report、pre-paper releases 与 current Journal/Agent lineage 联合核验；分离 2024 mechanism
  first-public 与 2025 formal-paper event，绑定三套不同 evaluation contract，并将其标记为 `Books Pending — No Change Candidate`。
- 完成 Model-guidance 的 v1 全文、公式、算法、全部实验/ablation、current training/sampler/model/evaluation paths 联合核验；
  分离单次推理 NFE 与完整训练/Serving 成本，确认最佳配方仍使用 empty-label estimator 与 EMA conditional/unconditional
  teacher forwards，并将“完全消除 CFG”标记为 `Disputed Scope Claim — Books Frozen`。
- 完成 Transformers v4.49.0 的 immutable tag、完整 Release、compare、selected Cache/processor/quantizer/parallel-plan/
  correctness PR 与目标章节联合核验；把模型发布、框架集成、typed compatibility contract、上游 CI 与 production
  evidence 分层，并标记为 `Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate`。
- 完成 Accelerate v1.4.0 的 immutable tag、完整 Release、TP/DataLoader、torchao/DeepSpeed FP8、dtype estimator 与
  weak-reference lifecycle PR 联合核验；把 process-group/sample/precision/lifetime contract 与 backend math 分层，
  并标记为 `Books Pending — No Change Candidate`。
- 完成 vLLM v0.7.3 的 signed tag、完整 Release/compare、concurrent partial Prefill、KV hash ownership、n-gram/MTP
  speculation、msgpack、metrics 与 pipeline-support PR 联合核验；把 single-A100 workload 与其他硬件 claim 分离，
  并标记为 `Books Pending — No Change Candidate`。
- W08 Candidate Evidence Gate 通过：65/65 owner family = 64 Full Source Reviews + 1 low-score verified；0 pending。
- 移除旧版“学术与工程无候选”和“Books Gate 已完成”的不实状态。
- 2025 Weekly evidence rebuild 进行中；本周没有进入 Books Integration。

## Open Questions

- W09 discovery replay 尚未开始；forward cursor 按用户要求暂停在 `Next: W09`。
- vLLM v0.7.3 缺 immutable benchmark dataset/log/repetition、character-to-token mapping、precision/output distribution、
  partial-slot/threshold/request-rate sensitivity、long-request fairness bound、V1-equivalent policy、multi-GPU/PP/PD、failure/
  schema migration、MTP acceptance cost 与 production goodput/SLO；当前不支持 Release-wide 性能结论。
- Accelerate v1.4.0 缺 immutable benchmark GPU/topology/precision/environment、TP-plan/model coverage、DP×TP/checkpoint
  correctness、loss parity、DataLoader streaming/resume identity、FP8 quality/hardware matrix、weakref lifecycle stress、
  multi-node recovery 与 production observability；当前不支持通用 TP/FSDP 速度排序。
- Transformers v4.49.0 缺 event-time 完整 CI/dependency/hardware matrix、fast/slow processor parity、static/dynamic cache
  compile/export/memory evidence、quantizer calibration portability、TP/PP topology contract、signed SBOM/environment 与生产升级/
  rollback regression；当前只支持 compatibility-surface migration，不支持 Release-wide 性能或完整可移植性结论。
- Model-guidance 缺 immutable event-time commit/checkpoint/container/run、训练硬件/precision/wall-time/FLOPs/energy、
  automatic-`w` 可执行规则与 held-out policy、seed variance、text/video conditioning、equal-total-compute/matched-hardware timing、
  batch/concurrency/tail-SLO 和 independent reproduction；最佳公开配方仍训练 unconditional/empty-label branch，因此 Books 保持冻结。
- AIDE 缺 immutable paper-run commit/container/dependency/data/holdout/result manifest、Weco per-task hardware/wall-time/total
  execution cost、tree/summary/atomic-edit/search-policy component ablation、独立 held-out selector、metric/evaluator disagreement、
  multi-file/multi-objective workflow、branch diversity/uncertainty、sandbox/credential isolation、artifact commit/rollback、tail SLO、
  energy 与 independent reproduction；当前只支持 objective-rich sandbox 中的 executable candidate-lineage branch，
  不支持通用 autonomous research、production workflow 或模型自我改进结论。
- AdaptiveStep 缺 immutable v1 artifact、artifact first-public timestamp reconciliation、Eq.3/sign 与 boundary index 说明、
  confidence calibration、2%/J/Top-M/trigger sensitivity、matched-compute ablation、rollout-label variance、online PRM
  tokens/latency/cost/SLO、sandbox leakage 与 independent reproduction；当前 Books 保持冻结。
- HeadInfer 缺 immutable W08 code/release/environment、raw logs、真实 1M/4M semantic run、CPU identity reconciliation、
  NUMA/pinned-memory/transfer traces、eight-GPU topology、continuous batching/prefix sharing/PagedAttention integration、
  cancellation/recovery、tail TTFT/TPOT/goodput/cost/energy 与 independent reproduction；当前只支持单请求 capacity branch，
  不支持 production serving superiority。
- Text2World 缺 immutable W08 code/data/config/container/API/model/run、raw generations/correction traces、精确 model snapshot/
  seed/retry/token/cost/latency、semantic-equivalence canonicalization、domain-family holdout、alternative validator、annotation
  ambiguity、equal-compute RL control、plan execution、continuous/stochastic/partial-observation environment、closed-loop transition/
  safety omission 与 independent reproduction；当前只支持 frozen symbolic benchmark 下的 proposal/validation/evidence branch，
  不支持真实环境正确性、RL causality 或 production Agent capability。
- LoRAM 缺 immutable W08 code/config/container/data/aligned-carrier/adapter/raw runs、作者确认的 mask polarity 与 Eq.5
  executable replacement、q-projection recovery semantics、完整 70B measured peak-memory/time/throughput/GPU contract、alignment
  amortization、activation/buffer/optimizer accounting、post-recovery logits/broad regression、multi-seed/cross-model evidence与独立复现；
  当前 paper/code contract disputed，不支持写入 Books。
- From RAG to Memory / HippoRAG 2 缺 immutable W08 code/config/container/model/index/run、精确 dataset preprocessing/hash、
  OpenIE/filter human audit、Table 11 provenance、跨数据集 PPR/seed sensitivity、online latency/storage/CPU/RAM、incremental
  update/contradiction/delete/ACL、poisoning/multilingual/graph-growth、claim faithfulness、multi-seed 与 independent reproduction；
  当前只支持作者 frozen-corpus protocol 下的 mixed dense/relational retrieval branch，不支持 durable Memory、continual update
  或通用 production RAG superiority。
- LServe 缺 immutable W08 code/profile/model/container/run、calibration/gate sensitivity、adapter/profile invalidation、
  raw main-figure batch/output/concurrency、adaptive quality budget、diffuse/adversarial workload、split-cache migration/recovery、
  multi-GPU/disaggregated tail SLO 与 independent reproduction；当前只支持作者环境下的 hybrid sparse-KV branch，
  不支持 constant-budget exactness、universal free lunch 或 production framework superiority。
- CoSyn 缺 immutable W08 code/prompt/model/API/environment/data manifests、全 pipeline execution/label rejection rate、
  sandbox/secret/resource policy、renderer determinism、provider-rights/deletion lineage、factorial/multi-seed、real-image shift、
  independent NutritionQA scorer calibration、coordinate-to-action evidence 与完整 lifecycle cost/SLO；当前只支持
  executable render specification 的 multimodal data branch，不支持 synthetic replacement、safe Agent 或普适 scaling law。
- PAFT 缺 immutable v1 prompt corpus、generator/version/filter/semantic-cluster manifest、400/450 与 8:1 split reconciliation、
  cross-generator/human/adversarial/multilingual holdout、token-matched augmentation、多 seed、完整 decoding/runtime/cost/SLO 与
  independent reproduction；当前只支持同一 synthetic generator family 内的 prompt-distribution SFT 分支，不支持
  prompt agnosticism 或 3.25× 通用 serving speedup。
- LongPO 仍缺 paper/code/card 一致的 optimizer、beta、NLL/multi-turn objective 与 RULER manifest；当前只支持
  short-to-long preference branch 的作者实验，不支持 512K production reliability 或通用 no-degradation 结论。
- Temporal Heads 缺 February code/data/environment、CRS executable formula、random-head/threshold sensitivity、held-out fact、
  GQA-compatible extraction 与 collateral-edit evidence；当前只支持受控 checkpoint/dataset 上的局部 causal contribution。
- LongWriter-V 缺 event-time artifact、word/token 与 Ruler/bin 口径 reconciliation、训练/runtime contract、prefix 有效独立样本量、
  judge-source separation、global coherence/collateral capability 与 production SLO；当前只支持作者 workload 下的训练分支。
- Intuitive Physics from Natural Videos 缺 immutable event-time run/checkpoint、fixed-context held-out calibration、matched-data
  baseline、长记忆、action-conditioned intervention 与 closed-loop outcome；当前只支持作者 protocol 下的 latent surprise evidence。
- Autellix 缺 official code/raw trace、参数 sensitivity、session fencing/failover、multi-node 与真实 tool latency；当前只支持
  vLLM 0.6.1、单机 A100 replay 下的 program-aware scheduling branch，不支持通用 4–15× 或生产 durability 结论。
- Sailor2 缺 immutable event-time source/data/license/checkpoint/container/run manifest、500B/510B token accounting reconciliation、
  GPU/precision/parallel/optimizer/compute contract、mixture/expansion sensitivity、translated-evaluation human agreement、
  reward/judge calibration、multi-seed、安全/公平/隐私与 serving SLO；当前只支持作者 pipeline 下的 multilingual data→CPT→alignment
  系统分支，不支持 GPT-4o-level、通用低资源语言或 production readiness 结论。
- Thinking Preference Optimization 缺 immutable event-time artifact、length-only causal control、equal-token/compute baseline、
  multi-seed、非数学迁移、faithful-process、hardware/runtime/cost/SLO 与独立复现；当前只支持作者 protocol 下的
  post-SFT weak-preference branch，不支持“更长导致更强”或 continual improvement 结论。
- HermesFlow 缺 event-time implementation、Equation 12→15 reconciliation、additive/gated/product ablation、独立 scorer、
  held-out data、round-level lineage、cross-backbone、multi-seed 与完整 compute/SLO；当前只能保留 homologous dataflow，
  不能吸收 product objective、universal capability gap 或 self-improvement generalization。
- Atom of Thoughts 缺 event-time code/prompt/run、exact API snapshot、sampling/retry/concurrency、same-cohort depth test、
  matched-budget baselines、dependency-order sensitivity、preservation/equivalence detector、raw-state fallback、rollback overhead 与
  独立复现；当前只支持 dependency-guided contraction 这一作者实验分支，不支持 formal Markov、universal scaling 或低成本结论。
- Dynamic Concepts Personalization 缺 code/weights/data/raw generations、immutable base/adapter identity、rank/dropout/prompt
  sensitivity、motion ground truth、held-out concepts、composition metric、user-study trial/uncertainty、完整 runtime/SLO 与独立复现；
  当前只支持作者 private-DiT 上的 staged basis/residual 分支，不支持已完成语义 disentanglement 或通用 video personalization 结论。
- RealSyn 缺 immutable v1 source/transformed manifests、完整 pipeline code/container/checkpoint、source-to-pair provenance、
  source-level license/consent/PII/NSFW/withdrawal contract、URL/row-count reconciliation、filter/cluster/generator sensitivity、
  contamination/multi-seed/equal-compute、完整 preprocessing/generation cost 与独立复现；当前只支持作者 CLIP protocol 下的
  retrieval-mediated pairing 分支，不支持 universal data quality、scaling law 或合规结论。
- Diffusion-Sharpening 缺 immutable event-time artifact、per-prompt pair selection、可执行且有非零 reward-gradient 的 objective、
  paper/code learning-rate/batch/step/NFE reconciliation、equal-total-compute/wall-time、multi-seed、独立 reward/evaluation、
  完整 user study、hardware/precision/energy/SLO 与独立复现；当前只支持 trajectory-search amortization 这一机制分支，
  不支持 reward-modulated DPO、best efficiency 或 arbitrary-reward alignment 结论。
- Revisiting Test-time Scaling 缺 immutable event-time artifact、same-question randomized length intervention、external-feedback
  sequential repair、parser/evaluator disagreement、held-out selector calibration、same-FLOP/wall-time/KV/concurrency comparison、
  uncertainty/significance、跨领域语言和 production SLO；当前只支持“长度不是单调质量代理、depth/width/selection 需分离”这一
  作者实验分支，不支持“长推理导致错误”“并行总是更便宜”或“短答案普遍更优”。
- AlphaMaze 缺 immutable v2 code/data/model/container/raw run、两个 SFT baseline 的准确定义、75/77 与 86/93 reconciliation、
  executable GRPO reward/objective、reset-SFT/GRPO ablation、fixed MazeBench manifest、seed/statistics、native perception 和
  closed-loop evidence；当前只支持 symbolic representation→SFT/reset demonstrations→grouped RL 的设计路线，不支持其核心
  GRPO 增益、自我纠错涌现、distillation-loss 或 robotics-transfer 结论。
- AI co-scientist 的持久状态、queue/retry、Elo calibration、provenance 与 safety contract 仍未完整公开。
- Soundwave 仍缺 event-time training code/data hashes；其 arXiv HTML 缺失已通过对应 v1 PDF 解决，不再构成 blocker。
- MMTEB 仍缺统一的 event-time environment/task manifest，且 v1 内部存在 131/132 与 40/41 的任务数口径冲突；
  这些属于可读来源中的 evidence limitation，不是未完成阅读。
- HumanUP 缺 event-time code/checkpoint、完整 real-trial denominator 与 controller safety/runtime 证据；当前可支持
  two-stage sim-to-real feasibility，不支持 certified 或开放环境自动恢复结论。
- SongGen 缺 event-time code/checkpoint/data/license manifest 与完整 serving contract；当前只支持作者 16 kHz、English、
  30-second workload 下的 multi-stream AR mechanism，不支持生产效率、长音乐或跨语言结论。
- Small Model Learnability Gap 缺 event-time commit/digests、seed-level uncertainty、length/compute-matched causal ablation 与
  cross-domain replication；“distribution shift / intrinsic capacity”保持作者解释，不升级为已证明机制。
- Multimodal Mamba 缺 paper-pinned runtime artifact、长上下文任务质量、state migration/isolation、并发与生产 SLO 证据；
  103K/20.6x 只保留为单 4090 next-token microbenchmark。
- RAD 缺 event-time code/environment/checkpoint、reactive-agent 与 renderer-fidelity sensitivity、real-road denominator、
  hardware/runtime/SLO、seed uncertainty 和 independent reproduction；3x collision headline 只属于作者 337-scene benchmark。
- Decomposed Reward Models 缺 event-time code/PCA artifact、hardware/runtime、跨模型与跨时间 basis stability、真实用户和
  subgroup 证据；component 的 benchmark correlation 不能升级为 causal/ethical preference semantics。
- MoM 缺 event-time commit/checkpoint/config lock、v1 efficiency hardware/precision、multi-seed 与 production SLO；
  2K recall 和作者 speed/memory 曲线不能外推成任意长上下文或通用 Serving 结论。
- FLAG-Trader 缺 event-time code/data/checkpoint、fees/slippage/market-impact、seeds、rolling regime 与独立复现；
  单一历史窗口的收益不能升级为部署证据。
- SoFar 缺本轮可提取的 v1 全文、event-time code/checkpoint/data digest、v1→v2 diff、独立复现、跨机器人 trial
  denominator、calibration/occlusion sensitivity、confidence/abstention、tail latency、control frequency 与 certified safety；
  v2 appendices 只作后验 mechanism/evidence boundary，不倒写为 W08 artifact state。
- Craw4LLM 缺 event-time crawl snapshot/checkpoint/container、真实网络与多语言复现、scorer drift/diversity guard、
  politeness/legal policy、distributed frontier recovery、完整 fetch+inference 成本与多 seed uncertainty；21% selected set 不等于
  total HTTP/request reduction。
- PC-Agent 缺 event-time commit/environment、应用/API/模型快照、equal-call/equal-cost ablation、自动 end-state verifier、
  hidden-state 与 accessibility/OCR 冲突处理，以及 permissions、idempotency、crash recovery、不可逆副作用和 tail SLO 证据；
  screenshot-based recovery 不能升级为 durable rollback。
- S2R 缺 event-time commit/data/checkpoint/container、multi-seed uncertainty、equal-token/FLOP/cost 对比、parser/judge
  sensitivity、对抗 verifier/reward-hacking、开放任务和独立复现；same-model self-verdict 不替代外部 evidence。
- Selective Question Answering 缺 event-time commit/model digest、held-out calibration、variable-length/open-ended answer evidence、
  natural-EOS 与 forced-budget ablation、compute/abstention/human-deferral cost、multi-seed uncertainty、domain shift、production SLO
  和独立复现；当前代码的 AIME25/GPQA 路径属于后续版本谱系，不倒写为 W08 v1 证据。
- SafeRoute 缺 author code/router checkpoint/augmented data、event-time environment、per-slice false-negative gate、guard/policy drift、
  adversarial routing、multilingual coverage、large-guard failure policy、真实 class prior 下阈值校准、并发/SLO/cost 与独立复现；
  理论 risk bound 不构成 deployment safety certificate。
- RelaCtrl 缺 author code/checkpoint/data manifest、optimizer 与完整 training-cost contract、shuffle seed/replay semantics、joint-layer
  interaction search、held-out condition/backbone transfer、relevance drift trigger、multi-seed uncertainty、kernel/concurrency/SLO 与
  independent reproduction；v1→v2 精确 delta 尚未由 immutable source diff 单独闭合。
- YOLOv12 缺 immutable February commit/checkpoint/container、TensorRT build 与 latency pre/post-processing boundary、training
  precision/time/energy/seeds、region orientation/shift/boundary/resolution sensitivity、equal-recipe baselines、robustness/OOD/
  calibration、edge power/tail SLO 与独立复现；当前 Turbo 和 2025-06 repository migration 不倒写为 W08 v1 artifact。
- CLIPPER 缺 immutable February commit/data/model/prompt digest、source-revision invalidation、independent verifier、human-authored
  training comparison、multi-seed interference frontier 与完整 compute/energy/SLO contract；五小时与约 50 小时的训练表述冲突
  保留为原文内部不一致，不能自行择一修正。
- Explorer 缺 immutable February commit/data/checkpoint/environment、accepted/rejected human audit、independent outcome verifier、
  website/policy provenance、idempotent side-effect recovery、matched-cost source baselines、fixed all-task multi-seed evidence与完整
  browser/network/energy/SLO contract；83/104 accessible subset 和 three-run maximum 必须跟随任何性能引用。
- Template-Anchored Safety 缺 official code/checkpoint/raw runs、v1 `D_eval` 唯一身份、seed/judge sensitivity、benign utility/
  over-refusal、adaptive attacks、template/tokenizer/model drift、quantization/fine-tuning/multilingual/long-turn/tool-use transfer、
  runtime overhead 与 independent reproduction；attention/probe/ASR evidence 不构成 production safety certificate。
- NExT-Mol 缺 immutable February artifact、v1→v2 diff、paper/current-repository config reconciliation、multi-seed/matched-compute、
  strict scaffold/OOD、synthesizability/toxicity/energy validation、property-proxy calibration、joint/staged error propagation、完整
  precision/energy/cost/SLO 与 independent reproduction；valid SELFIES 与 benchmark conformer 不构成 discovery outcome。
- video-SALMONN-o1 缺 immutable February code/data/checkpoint/container、完整 training release 与 model card、judge/human step-label
  agreement、perturbation sensitivity、audio/vision/process/full-path factorial、matched-compute online-search/PRM comparison、multi-seed、
  contamination/multilingual/long-video/domain-shift、latency/energy/SLO 与 independent reproduction；visible reasoning 与
  rollout-estimated preference 不构成 faithful process evidence。
- InfiR 缺 immutable February repository/code/data/checkpoint/container、初始化身份、source/license/mixture manifests、filter
  retention、teacher/reward/scorer versions、equal-token component ablations、multi-seed、semantic contamination、multilingual/
  rare-domain/fairness、multimodal hardware/token/freeze-schedule、device memory/latency/energy/privacy/SLO 与 independent reproduction；
  论文 appendix、后来的 model card 与 final benchmark 之间的 config/data lineage 仍需 reconciliation。

## Sources

- vLLM v0.7.3 official release — https://github.com/vllm-project/vllm/releases/tag/v0.7.3（Released: 2025-02-20；signed tag `ed6e907`；253 commits / 93 contributors；Accessed: 2026-08-18）
- vLLM v0.7.3 tagged source — https://github.com/vllm-project/vllm/tree/v0.7.3（Immutable engine/test/benchmark identity；Accessed: 2026-08-18）
- vLLM v0.7.2...v0.7.3 compare — https://github.com/vllm-project/vllm/compare/v0.7.2...v0.7.3（Release diff identity；Accessed: 2026-08-18）
- vLLM concurrent partial Prefill PR — https://github.com/vllm-project/vllm/pull/10235（V0 scheduler policy, single-A100 workload and TTFT/ITL trade-off；Accessed: 2026-08-18）
- vLLM MTP PR — https://github.com/vllm-project/vllm/pull/12755（DeepSeek MTP integration and low-QPS claim lineage；Accessed: 2026-08-18）
- vLLM n-gram speculative Decode PR — https://github.com/vllm-project/vllm/pull/12193（Initial V1 proposal/verification branch；Accessed: 2026-08-18）
- vLLM core msgpack PR — https://github.com/vllm-project/vllm/pull/12918（Core request schema/serialization lineage；Accessed: 2026-08-18）
- vLLM KV hash ownership PR — https://github.com/vllm-project/vllm/pull/12922（Request to KVCacheManager ownership migration；Accessed: 2026-08-18）
- vLLM V1 prefix-cache metric PR — https://github.com/vllm-project/vllm/pull/12592（GPU prefix cache hit-rate observation surface；Accessed: 2026-08-18）
- vLLM V1 request-timing metric PR — https://github.com/vllm-project/vllm/pull/12644（Request timing histogram lineage；Accessed: 2026-08-18）
- vLLM V1 pipeline-parallel PR — https://github.com/vllm-project/vllm/pull/12996（V1 pipeline execution lineage；Accessed: 2026-08-18）
- Accelerate v1.4.0 official release — https://github.com/huggingface/accelerate/releases/tag/v1.4.0（Released: 2025-02-17；tag `b431d1f`；complete release scope；Accessed: 2026-08-18）
- Accelerate v1.4.0 tagged source — https://github.com/huggingface/accelerate/tree/v1.4.0（Immutable wrapper/test/example identity；Accessed: 2026-08-18）
- Accelerate v1.3.0...v1.4.0 compare — https://github.com/huggingface/accelerate/compare/v1.3.0...v1.4.0（Release diff identity；Accessed: 2026-08-18）
- Accelerate TP/DataLoader PR — https://github.com/huggingface/accelerate/pull/3173（Initial TP plugin, same-batch routing, benchmark and explicit paradigm limits；Accessed: 2026-08-18）
- Accelerate torchao FP8 PR — https://github.com/huggingface/accelerate/pull/3348（Initial torchao FP8 recipe/backend integration；Accessed: 2026-08-18）
- Accelerate DeepSpeed FP8 PR — https://github.com/huggingface/accelerate/pull/3361（Backend compatibility lineage；Accessed: 2026-08-18）
- Accelerate dtype-estimation fix PR — https://github.com/huggingface/accelerate/pull/3383（Memory-estimation state correction；Accessed: 2026-08-18）
- Accelerate DataLoader weak-reference fix PR — https://github.com/huggingface/accelerate/pull/3391（GradientState/DataLoader lifetime correction；Accessed: 2026-08-18）
- Transformers v4.49.0 official release — https://github.com/huggingface/transformers/releases/tag/v4.49.0（Released: 2025-02-17；tag `a22a437`；complete release scope；Accessed: 2026-08-18）
- Transformers v4.49.0 tagged source — https://github.com/huggingface/transformers/tree/v4.49.0（Immutable framework/code/test identity；Accessed: 2026-08-18）
- Transformers v4.48.3...v4.49.0 compare — https://github.com/huggingface/transformers/compare/v4.48.3...v4.49.0（315 commits, 1,359 files, 136 contributors；integration breadth, not performance evidence；Accessed: 2026-08-18）
- Transformers static cache config PR — https://github.com/huggingface/transformers/pull/35679（Typed GenerationConfig/static-cache contract；Accessed: 2026-08-18）
- Transformers typed Cache migration PR — https://github.com/huggingface/transformers/pull/35673（Legacy input to Cache output migration；Accessed: 2026-08-18）
- Transformers ImageProcessorFast refactor PR — https://github.com/huggingface/transformers/pull/35069（Processor standardization lineage；Accessed: 2026-08-18）
- Transformers image-classification semantic fix PR — https://github.com/huggingface/transformers/pull/35848（Single/multi-label sigmoid/softmax correction；Accessed: 2026-08-18）
- Transformers pipeline-plan PR — https://github.com/huggingface/transformers/pull/36091（Config/model pipeline-plan surface；Accessed: 2026-08-18）
- Transformers meta-device cache PR — https://github.com/huggingface/transformers/pull/35164（Shape/allocation separation lineage；Accessed: 2026-08-18）
- LoRAM v1 — https://arxiv.org/html/2502.13533v1（First Public: 2025-02-19；event-time full text, equations, experiments and appendices；recovery equation disputed；Accessed: 2026-08-18）
- LoRAM metadata — https://arxiv.org/abs/2502.13533（v1: 2025-02-19；v2 on 2025-03-15 and ICLR 2025 lineage；v2 retains Eq.5 conflict；Accessed: 2026-08-18）
- LoRAM official repository — https://github.com/junzhang-zj/LoRAM（Current 52-commit implementation lineage；no immutable W08 tag/config/checkpoint/run；Accessed: 2026-08-18）
- LoRAM current training path — https://github.com/junzhang-zj/LoRAM/blob/main/loram/2_pruned_low_rank_matrix_training.py（Current QLoRAM training implementation；not event-time pinned；Accessed: 2026-08-18）
- LoRAM current recovery path — https://github.com/junzhang-zj/LoRAM/blob/main/loram/3_recovered_low_rank_matrix_generation.py（Current index-based zero-fill/copy implementation；visible q-projection copy gap；not event-time pinned；Accessed: 2026-08-18）
- From RAG to Memory / HippoRAG 2 v1 — https://arxiv.org/html/2502.14802v1（First Public: 2025-02-20；event-time full text, method, experiments and appendices；Accessed: 2026-08-18）
- From RAG to Memory metadata — https://arxiv.org/abs/2502.14802（v1: 2025-02-20；v2 on 2025-06-19 kept as later revision lineage；Accessed: 2026-08-18）
- HippoRAG official repository — https://github.com/OSU-NLP-Group/HippoRAG（Current implementation/reproduction lineage；no immutable W08 tag；later update/delete/provider surfaces not backdated；Accessed: 2026-08-18）
- LServe v1 — https://arxiv.org/html/2502.14866v1（First Public: 2025-02-20；event-time full text, equations, system design, evaluation and analysis；Accessed: 2026-08-18）
- LServe metadata — https://arxiv.org/abs/2502.14866（v1: 2025-02-20；v2 on 2025-04-21 kept as later revision lineage；Accessed: 2026-08-18）
- LServe official project page — https://hanlab.mit.edu/projects/lserve（Official method, paper and code identity；Accessed: 2026-08-18）
- OmniServe official repository — https://github.com/mit-han-lab/omniserve（Current integrated QServe/LServe implementation and benchmark interface；no immutable W08 tag；Accessed: 2026-08-18）
- CoSyn v1 — https://arxiv.org/html/2502.14846v1（First Public: 2025-02-20；event-time full text, all experiments and appendices；Accessed: 2026-08-18）
- CoSyn metadata — https://arxiv.org/abs/2502.14846（v1: 2025-02-20；v2/ACL lineage kept later；Accessed: 2026-08-18）
- CoSyn official generation repository — https://github.com/allenai/pixmo-docs（Current 25-pipeline implementation lineage；no immutable W08 tag；Accessed: 2026-08-18）
- CoSyn-400K dataset artifact — https://huggingface.co/datasets/allenai/CoSyn-400K（Current 408,227-row/10-subset schema and license lineage；not backdated into v1；Accessed: 2026-08-18）
- CoSyn-point dataset artifact — https://huggingface.co/datasets/allenai/CoSyn-point（Current pointing schema and approximately 68.1K train rows；Accessed: 2026-08-18）
- NutritionQA artifact — https://huggingface.co/datasets/yyupenn/NutritionQA（50-photo/two-question benchmark lineage and GPT-4o-mini semantic scorer；Accessed: 2026-08-18）
- DocPointQA artifact — https://huggingface.co/datasets/yyupenn/DocPointQA（300 question-point pair evaluation lineage；Accessed: 2026-08-18）
- PAFT v1 — https://arxiv.org/html/2502.12859v1（First Public: 2025-02-18；event-time full text, algorithm, experiments and appendices；Accessed: 2026-08-18）
- PAFT metadata — https://arxiv.org/abs/2502.12859（v1: 2025-02-18；v2/v3 later revision lineage not backported；Accessed: 2026-08-18）
- AlphaMaze v2 — https://arxiv.org/html/2502.14669v2（Last W08 revision: 2025-02-21；full text and appendix；internally disputed result contract；Accessed: 2026-08-18）
- AlphaMaze v1 — https://arxiv.org/html/2502.14669v1（First Public: 2025-02-20；initial W08 full text；Accessed: 2026-08-18）
- AlphaMaze metadata — https://arxiv.org/abs/2502.14669（v1/v2 in W08；v3 on 2025-02-25 kept as later revision；Accessed: 2026-08-18）
- AlphaMaze author model artifact — https://huggingface.co/Menlo/AlphaMaze-v0.2-1.5B（Mutable later model card/checkpoint lineage；not an immutable W08 GRPO run；Accessed: 2026-08-18）
- AlphaMaze SFT dataset artifact — https://huggingface.co/datasets/Menlo/Maze-Reasoning-v0.1（Mutable 565K-row dataset lineage；Accessed: 2026-08-18）
- AlphaMaze GRPO dataset artifact — https://huggingface.co/datasets/Menlo/Maze-Reasoning-GRPO-v0.1（Mutable 182K-row dataset lineage；Accessed: 2026-08-18）
- Revisiting Test-time Scaling v1 — https://arxiv.org/html/2502.12215v1（First Public: 2025-02-17；event-time full text；Accessed: 2026-08-18）
- Revisiting Test-time Scaling metadata — https://arxiv.org/abs/2502.12215（v1: 2025-02-17；v2: 2025-03-03；Accessed: 2026-08-18）
- Revisiting Test-time Scaling official repository — https://github.com/ZhiYuanZeng/test-time-scaling-eval（Current evaluation, rollout and sequential-search lineage；no immutable W08 run；Accessed: 2026-08-18）
- Revisiting Test-time Scaling ACL lineage — https://aclanthology.org/2025.acl-long.232/（Later author publication lineage；not treated as a new W08 event；Accessed: 2026-08-18）
- Diffusion-Sharpening v1 — https://arxiv.org/html/2502.12146v1（First Public: 2025-02-17；sole arXiv version；Accessed: 2026-08-18）
- Diffusion-Sharpening metadata — https://arxiv.org/abs/2502.12146（v1 submission history；Accessed: 2026-08-18）
- Diffusion-Sharpening official repository — https://github.com/Gen-Verse/Diffusion-Sharpening（Current 29-commit implementation lineage；no release/tag or immutable W08 run；Accessed: 2026-08-18）
- Diffusion-Sharpening RLHF source — https://raw.githubusercontent.com/Gen-Verse/Diffusion-Sharpening/main/train_rlhf_diffusion_sharpen_sdxl.py（Executable pair/loss/config lineage；objective and batch semantics disputed；Accessed: 2026-08-18）
- Diffusion-Sharpening SFT source — https://raw.githubusercontent.com/Gen-Verse/Diffusion-Sharpening/main/train_sft_diffusion_sharpen_sdxl.py（Executable SFT trajectory lineage；current main, not W08-pinned；Accessed: 2026-08-18）
- RealSyn v1 — https://arxiv.org/html/2502.12513v1（First Public: 2025-02-18；v1-locked evidence；Accessed: 2026-08-18）
- RealSyn metadata — https://arxiv.org/abs/2502.12513（v1: 2025-02-18；later revisions separated；Accessed: 2026-08-18）
- RealSyn official repository — https://github.com/deepglint/RealSyn（Current artifact/download lineage；no complete pipeline or immutable W08 digest；Accessed: 2026-08-18）
- RealSyn official project page — https://garygutc.github.io/RealSyn/（Official method/artifact overview and later ACM MM lineage；Accessed: 2026-08-18）
- RealSyn15M dataset artifact — https://huggingface.co/datasets/Kaichengalex/RealSyn15M（Mutable released artifact/card/viewer；row-count and source-rights boundaries retained；Accessed: 2026-08-18）
- Dynamic Concepts Personalization v1 — https://arxiv.org/html/2502.14844v1（First Public: 2025-02-20；sole arXiv version；Accessed: 2026-08-18）
- Dynamic Concepts Personalization metadata — https://arxiv.org/abs/2502.14844（v1 submission history；Accessed: 2026-08-18）
- Dynamic Concepts official project page — https://snap-research.github.io/dynamic_concepts/（Official explanation and supplementary-media lineage；no code artifact；Accessed: 2026-08-18）
- Atom of Thoughts v1 — https://arxiv.org/html/2502.12018v1（First Public: 2025-02-17；v1-locked evidence；Accessed: 2026-08-18）
- Atom of Thoughts metadata — https://arxiv.org/abs/2502.12018（v1: 2025-02-17；later revisions separated；Accessed: 2026-08-18）
- Atom of Thoughts official repository — https://github.com/qixucen/atom（Current implementation lineage；no release/tag or immutable W08 digest；Accessed: 2026-08-18）
- Atom of Thoughts OpenReview — https://openreview.net/forum?id=qXSFkP0ELS（Later NeurIPS 2025 publication lineage；Accessed: 2026-08-18）
- HermesFlow v1 — https://arxiv.org/html/2502.12148v1（First Public: 2025-02-17；v1-locked evidence；Accessed: 2026-08-18）
- HermesFlow metadata — https://arxiv.org/abs/2502.12148（v1: 2025-02-17；v2: 2025-09-25；Accessed: 2026-08-18）
- HermesFlow official repository — https://github.com/Gen-Verse/HermesFlow（Current code/data/training lineage；no release/tag or signed W08 digest；Accessed: 2026-08-18）
- HermesFlow checkpoint — https://huggingface.co/Gen-Verse/HermesFlow（Checkpoint release: 2025-02-18；mutable artifact lineage；Accessed: 2026-08-18）
- ThinkPO v1 — https://arxiv.org/html/2502.13173v1（First Public: 2025-02-17；Accessed: 2026-08-18）
- ThinkPO metadata — https://arxiv.org/abs/2502.13173（Only arXiv version: v1；Accessed: 2026-08-18）
- ThinkPO official repository — https://github.com/uservan/ThinkPO（Current code/data/model lineage；no release/tag or immutable W08 digest；Accessed: 2026-08-18）
- Sailor2 technical report v1 — https://arxiv.org/html/2502.12982v1（Technical report first public: 2025-02-18；Accessed: 2026-08-18）
- Sailor2 metadata — https://arxiv.org/abs/2502.12982（Only arXiv version: v1；Accessed: 2026-08-18）
- Sailor2 official release Blog — https://sail.sea.com/blog/articles/55（Model-family first public: 2024-12-03；Accessed: 2026-08-18）
- Sailor2 release index — https://github.com/sail-sg/sailor2（Current component links；no immutable W08 bundle；Accessed: 2026-08-18）
- Sailor2-20B model artifact — https://huggingface.co/sail/Sailor2-20B（Mutable model-card/weight lineage；Accessed: 2026-08-18）
- SailCraft data pipeline — https://github.com/sail-sg/sailcraft（Current cleaning/deduplication implementation lineage；Accessed: 2026-08-18）
- RegMix implementation — https://github.com/sail-sg/regmix（Current mixture-search implementation lineage；Accessed: 2026-08-18）
- Megatron-Sailor2 — https://github.com/sail-sg/Megatron-Sailor2（Current pretraining implementation lineage；Accessed: 2026-08-18）
- OAT — https://github.com/sail-sg/oat（Current post-training implementation lineage；Accessed: 2026-08-18）
- SailCompass — https://github.com/sail-sg/sailcompass（Current base-model evaluation lineage；Accessed: 2026-08-18）
- SEA-WildBench — https://github.com/sail-sg/SEA-WildBench（Current chat-evaluation lineage；Accessed: 2026-08-18）
- Autellix v1 — https://arxiv.org/html/2502.13965v1（First Public: 2025-02-19；Accessed: 2026-08-18）
- Autellix metadata — https://arxiv.org/abs/2502.13965（Only arXiv version: v1；Accessed: 2026-08-18）
- Intuitive Physics from Natural Videos v1 — https://arxiv.org/html/2502.11831v1（First Public: 2025-02-17；Accessed: 2026-08-18）
- Intuitive Physics from Natural Videos metadata — https://arxiv.org/abs/2502.11831（Only arXiv version: v1；Accessed: 2026-08-18）
- Intuitive Physics from Natural Videos official repository — https://github.com/facebookresearch/jepa-intuitive-physics（Evaluation code, raw surprises and figure artifact；no event-time release/tag；Accessed: 2026-08-18）
- LongWriter-V v1 PDF — https://arxiv.org/pdf/2502.14834v1（First Public: 2025-02-20；Accessed: 2026-08-18）
- LongWriter-V metadata — https://arxiv.org/abs/2502.14834（Only arXiv version: v1；Accessed: 2026-08-18）
- LongWriter-V official repository — https://github.com/THU-KEG/LongWriter-V（Current 34-commit artifact and later Agent/Ruler lineage；no v1-pinned release；Accessed: 2026-08-18）
- Temporal Heads v1 — https://arxiv.org/html/2502.14258v1（First Public: 2025-02-20；Accessed: 2026-08-18）
- Temporal Heads metadata — https://arxiv.org/abs/2502.14258（Only arXiv version: v1；Accessed: 2026-08-18）
- Temporal Heads official repository — https://github.com/dmis-lab/TemporalHead（Code/data released: 2025-05-30；later artifact lineage；Accessed: 2026-08-18）
- Temporal Heads official dataset — https://huggingface.co/datasets/dmis-lab/TemporalHead（Later artifact lineage；Accessed: 2026-08-18）
- LongPO v1 — https://arxiv.org/html/2502.13922v1（First Public: 2025-02-19；Accessed: 2026-08-18）
- LongPO metadata — https://arxiv.org/abs/2502.13922（Only arXiv version: v1；Accessed: 2026-08-18）
- LongPO author repository — https://github.com/DAMO-NLP-SG/LongPO（Current code/data/checkpoint lineage；paper/config drift retained；Accessed: 2026-08-18）
- LongPO 512K experimental checkpoint card — https://huggingface.co/DAMO-NLP-SG/Mistral-7B-LongPO-512K-EXP（Later experimental artifact lineage；Accessed: 2026-08-18）
- LongPO ICLR record — https://openreview.net/forum?id=qTrEq31Shm（Later publication lineage；Accessed: 2026-08-18）
- AI co-scientist — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/（First Public: 2025-02-19；Accessed: 2026-08-18）
- AI co-scientist paper — https://arxiv.org/abs/2502.18864（Paper v1: 2025-02-26；v2: 2026-06-29；Accessed: 2026-08-18）
- Hugging Face Papers 2025-W08 discovery feed — https://huggingface.co/papers/week/2025-W08（Discovery only；Accessed: 2026-08-18）
- vLLM v0.7.3 — https://github.com/vllm-project/vllm/releases/tag/v0.7.3（Released: 2025-02-20；Accessed: 2026-08-18）
- Transformers v4.49.0 — https://github.com/huggingface/transformers/releases/tag/v4.49.0（Released: 2025-02-17；Accessed: 2026-08-18）
- Accelerate v1.4.0 — https://github.com/huggingface/accelerate/releases/tag/v1.4.0（Released: 2025-02-17；Accessed: 2026-08-18）
- Template-Anchored Safety v1 — https://arxiv.org/html/2502.13946v1（First Public: 2025-02-19；Accessed: 2026-08-18）
- Template-Anchored Safety metadata — https://arxiv.org/abs/2502.13946（v1: 2025-02-19；v2: 2025-06-03；Accessed: 2026-08-18）
- NExT-Mol v1 — https://arxiv.org/html/2502.12638v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- NExT-Mol metadata — https://arxiv.org/abs/2502.12638（v1: 2025-02-18；v2: 2025-02-27；Accessed: 2026-08-18）
- NExT-Mol author repository — https://github.com/acharkq/NExT-Mol（Current ICLR-era artifact；no event-time tag/release；Accessed: 2026-08-18）
- NExT-Mol OpenReview — https://openreview.net/forum?id=p66a00KLWN（ICLR 2025 publication lineage；Accessed: 2026-08-18）
- video-SALMONN-o1 v1 — https://arxiv.org/html/2502.11775v1（First Public: 2025-02-17；Accessed: 2026-08-18）
- video-SALMONN-o1 metadata — https://arxiv.org/abs/2502.11775（Only arXiv version: v1；Accessed: 2026-08-18）
- video-SALMONN-o1 author repository — https://github.com/BriansIDP/video-SALMONN-o1（Current inference/demo lineage；training still marked “Coming soon”；no event-time tag；Accessed: 2026-08-18）
- video-SALMONN-o1 checkpoint — https://huggingface.co/tsinghua-ee/video-SALMONN-o1（Current BF16 checkpoint lineage；model-card contract incomplete；Accessed: 2026-08-18）
- SALMONN author-family repository — https://github.com/bytedance/SALMONN（Related model lineage；Accessed: 2026-08-18）
- InfiR v1 — https://arxiv.org/html/2502.11573v1（First Public: 2025-02-17；Accessed: 2026-08-18）
- InfiR metadata — https://arxiv.org/abs/2502.11573（Only arXiv version: v1；Accessed: 2026-08-18）
- InfiR Base model card/checkpoint — https://huggingface.co/InfiX-ai/InfiR-1B-Base（Updated: 2025-07-28 lineage；Accessed: 2026-08-18）
- InfiR Instruct model card/checkpoint — https://huggingface.co/InfiX-ai/InfiR-1B-Instruct（Updated: 2025-08-05 lineage；Accessed: 2026-08-18）
- InfiR official collection — https://huggingface.co/collections/InfiX-ai/infir-67b311b3bb33bc6fb81e5c74（Later artifact lineage；Accessed: 2026-08-18）
- InfiR paper-linked repository — https://github.com/Reallm-Labs/InfiR（Unavailable under current identity；Accessed: 2026-08-18）
- Selective Question Answering v1 — https://arxiv.org/html/2502.13962v1（First Public: 2025-02-19；Accessed: 2026-08-18）
- Selective Question Answering metadata — https://arxiv.org/abs/2502.13962（v1: 2025-02-19；v2: 2025-07-18；Accessed: 2026-08-18）
- Selective Question Answering code lineage — https://github.com/wjurayj/final_answer（Current `main` includes later AIME25/GPQA workflow；Accessed: 2026-08-18）
- Selective Question Answering ACL record — https://aclanthology.org/2025.acl-short.50/（Later publication lineage；Accessed: 2026-08-18）
- SafeRoute v1 — https://arxiv.org/html/2502.12464v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- SafeRoute metadata — https://arxiv.org/abs/2502.12464（v1: 2025-02-18；v2～v5: 2025-05-19～22；Accessed: 2026-08-18）
- SafeRoute ACL record — https://aclanthology.org/2025.findings-acl.105/（Later publication lineage；Accessed: 2026-08-18）
- RelaCtrl v2 — https://arxiv.org/html/2502.14377v2（Latest In-window Revision: 2025-02-21；Accessed: 2026-08-18）
- RelaCtrl metadata — https://arxiv.org/abs/2502.14377（v1: 2025-02-20；v2: 2025-02-21；v3～v5: later lineage；Accessed: 2026-08-18）
- RelaCtrl official project page — https://360cvgroup.github.io/RelaCtrl/（Visualization artifact only；Accessed: 2026-08-18）
- YOLOv12 v1 — https://arxiv.org/html/2502.12524v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- YOLOv12 metadata — https://arxiv.org/abs/2502.12524（Only arXiv version: v1；Accessed: 2026-08-18）
- YOLOv12 author repository — https://github.com/sunsmarterjie/yolov12（Current repository includes later Turbo/task heads and 2025-06 implementation migration；Accessed: 2026-08-18）
- CLIPPER v1 — https://arxiv.org/html/2502.14854v1（First Public: 2025-02-20；Accessed: 2026-08-18）
- CLIPPER metadata — https://arxiv.org/abs/2502.14854（v1: 2025-02-20；v2: 2025-08-05；Accessed: 2026-08-18）
- CLIPPER author repository — https://github.com/chtmp223/CLIPPER（Current repository is not an immutable v1 artifact；Accessed: 2026-08-18）
- Explorer v2 — https://arxiv.org/html/2502.11357v2（Latest In-window Revision: 2025-02-19；Accessed: 2026-08-18）
- Explorer metadata — https://arxiv.org/abs/2502.11357（v1: 2025-02-17；v2: 2025-02-19；v3/v4: later lineage；Accessed: 2026-08-18）
- Explorer author repository — https://github.com/OSU-NLP-Group/Explorer（Current ACL-era artifact；no paper-pinned release/tag；Accessed: 2026-08-18）
- MMTEB v1 — https://arxiv.org/html/2502.13595v1（First Public: 2025-02-19；Accessed: 2026-08-18）
- MMTEB versioned results — https://github.com/embeddings-benchmark/results/tree/9a79f7e07542ad2f5cb47490fa1e5ac2ba57d7a8（Paper-pinned artifact；Accessed: 2026-08-18）
- HumanUP v1 — https://arxiv.org/html/2502.12152v1（First Public: 2025-02-17；Accessed: 2026-08-18）
- HumanUP project — https://humanoid-getup.github.io/（Accessed: 2026-08-18）
- HumanUP code lineage — https://github.com/RunpeiDong/HumanUP（Later simulation-training release；Accessed: 2026-08-18）
- SongGen v1 — https://arxiv.org/html/2502.13128v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- SongGen project — https://liuzh-19.github.io/SongGen/（Paper/demo announced: 2025-02-19；Accessed: 2026-08-18）
- SongGen code/checkpoint lineage — https://github.com/LiuZH-19/SongGen（Later releases；Accessed: 2026-08-18）
- Small Model Learnability Gap v2 — https://arxiv.org/html/2502.12143v2（W08 latest revision: 2025-02-22；Accessed: 2026-08-18）
- Small Model Learnability Gap project — https://small-model-gap.github.io/（Accessed: 2026-08-18）
- Small Model Learnability Gap artifact lineage — https://github.com/Small-Model-Gap/Small-Model-Learnability-Gap（Accessed: 2026-08-18）
- Small Model Learnability Gap ACL record — https://aclanthology.org/2025.findings-acl.1301/（Later publication；Accessed: 2026-08-18）
- Multimodal Mamba v1 — https://arxiv.org/html/2502.13145v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- Multimodal Mamba code/weights — https://github.com/hustvl/mmMamba（Initial release: 2025-02-19；Accessed: 2026-08-18）
- RAD v1 — https://arxiv.org/html/2502.13144v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- RAD project — https://hgao-cv.github.io/RAD/（Accessed: 2026-08-18）
- RAD code/artifact lineage — https://github.com/hustvl/RAD（Core code released: 2025-09-28；Accessed: 2026-08-18）
- Decomposed Reward Models v1 — https://arxiv.org/html/2502.13131v1（First Public: 2025-02-18；Accessed: 2026-08-18）
- Decomposed Reward Models ACL record — https://aclanthology.org/2025.findings-acl.1019/（Later publication lineage；Accessed: 2026-08-18）
- Low-weight quantum error-correcting codes with RL — https://arxiv.org/abs/2502.14372（First Public: 2025-02-20；Low-score identity/date verification；Accessed: 2026-08-18）
- DBLP metadata for arXiv:2502.14372 — https://dblp.org/rec/journals/corr/abs-2502-14372.html（Metadata cross-check；Accessed: 2026-08-18）
- MoM v1 — https://arxiv.org/html/2502.13685v1（First Public: 2025-02-19；Accessed: 2026-08-18）
- MoM abstract and revision history — https://arxiv.org/abs/2502.13685（v1: 2025-02-19；v2: 2025-05-06；v3: 2025-10-09；v4: 2025-11-18；Accessed: 2026-08-18）
- MoM author repository — https://github.com/OpenSparseLLMs/MoM（Current artifact and later lineage；Accessed: 2026-08-18）
- FLAG-Trader v3 — https://arxiv.org/html/2502.11433v3（W08 latest revision: 2025-02-19；Accessed: 2026-08-18）
- FLAG-Trader revision history — https://arxiv.org/abs/2502.11433（v1: 2025-02-17；v2: 2025-02-18；v3: 2025-02-19；Accessed: 2026-08-18）
- FLAG-Trader ACL record — https://aclanthology.org/2025.findings-acl.716/（Later publication lineage；Accessed: 2026-08-18）
- SoFar v1 — https://arxiv.org/abs/2502.13143v1（First Public: 2025-02-18；event identity and abstract；Accessed: 2026-08-18）
- SoFar v2 full text — https://arxiv.org/html/2502.13143v2（Later revision: 2025-09-24；mechanism/evaluation boundary only；Accessed: 2026-08-18）
- SoFar project — https://qizekun.github.io/sofar/（Current project lineage；Accessed: 2026-08-18）
- SoFar repository — https://github.com/qizekun/SoFar（Current code/model/dataset lineage；Accessed: 2026-08-18）
- SoFar SIMPLER evaluation repository — https://github.com/Zhangwenyao1/SimplerEnv-SOFAR（Later evaluation lineage；Accessed: 2026-08-18）
- Craw4LLM v1 — https://arxiv.org/html/2502.13347v1（First Public: 2025-02-19；W08 mechanism/evaluation source；Accessed: 2026-08-18）
- Craw4LLM revision history — https://arxiv.org/abs/2502.13347（v1: 2025-02-19；v2: 2025-02-24；v3: 2025-06-23；Accessed: 2026-08-18）
- Craw4LLM repository — https://github.com/cxcscmu/Craw4LLM（Current author artifact lineage；Accessed: 2026-08-18）
- Craw4LLM ACL record — https://aclanthology.org/2025.findings-acl.712/（Later publication lineage；Accessed: 2026-08-18）
- PC-Agent v1 — https://arxiv.org/html/2502.14282v1（First Public: 2025-02-20；W08 mechanism/evaluation source；Accessed: 2026-08-18）
- PC-Agent revision history — https://arxiv.org/abs/2502.14282（v1: 2025-02-20；v2: 2025-02-21；Accessed: 2026-08-18）
- PC-Agent artifact lineage — https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent（Current repository；later than event-time paper；Accessed: 2026-08-18）
- S2R v1 — https://arxiv.org/html/2502.12853v1（First Public: 2025-02-18；mechanism/evaluation source；Accessed: 2026-08-18）
- S2R metadata — https://arxiv.org/abs/2502.12853（Only arXiv version: v1；Accessed: 2026-08-18）
- S2R author artifact — https://github.com/NineAbyss/S2R（Current code/data lineage；not a paper-pinned environment；Accessed: 2026-08-18）
- S2R ACL record — https://aclanthology.org/2025.acl-long.1104/（Later publication lineage；Accessed: 2026-08-18）
- SigLIP 2 — https://arxiv.org/abs/2502.14786（v1: 2025-02-20；Accessed: 2026-08-18）
- SigLIP 2 artifact — https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md（Accessed: 2026-08-18）
- SuperGPQA v1 — https://arxiv.org/abs/2502.14739v1（v1: 2025-02-20；Accessed: 2026-08-18）
- SuperGPQA artifact — https://github.com/SuperGPQA/SuperGPQA（Accessed: 2026-08-18）
- LoRA Knowledge Capacity v1 — https://arxiv.org/abs/2502.14502v1（v1: 2025-02-20；Accessed: 2026-08-18）
- LoRA Knowledge Capacity artifact — https://github.com/AIRI-Institute/knowledge-packing（Accessed: 2026-08-18）
- Soundwave v1 — https://arxiv.org/abs/2502.12900（v1: 2025-02-18；Accessed: 2026-08-18）
- Soundwave artifact — https://github.com/FreedomIntelligence/Soundwave（Architecture/inference code: 2025-02-18；weights: 2025-05-03；Accessed: 2026-08-18）
- Embedding Space Capacity v1 — https://arxiv.org/abs/2502.13063v1（v1: 2025-02-18；Accessed: 2026-08-18）
- Embedding Space Capacity artifact — https://github.com/yurakuratov/hidden_capacity（Accessed: 2026-08-18）
- S* v1 — https://arxiv.org/abs/2502.14382（v1: 2025-02-20；Accessed: 2026-08-18）
- S* artifact — https://github.com/NovaSky-AI/SkyThought/tree/main/skythought/test-time-scaling（Code release: 2025-02-21；Accessed: 2026-08-18）
- Magma v1 — https://arxiv.org/abs/2502.13130（v1: 2025-02-18；Accessed: 2026-08-18）
- Magma project — https://microsoft.github.io/Magma/（Accessed: 2026-08-18）
- Magma artifact — https://github.com/microsoft/Magma（Inference code: 2025-02-23；later training/data artifacts retained only as revision lineage；Accessed: 2026-08-18）
- RDLM v1 — https://arxiv.org/abs/2502.11564（v1: 2025-02-17；v2: 2025-10-23；Accessed: 2026-08-18）
- RDLM artifact — https://github.com/harryjo97/RDLM（Initial commit: 2025-02-17；later checkpoints/revisions retained as lineage；Accessed: 2026-08-18）
- Logic-RL v1 — https://arxiv.org/abs/2502.14768（v1: 2025-02-20；Accessed: 2026-08-18）
- Logic-RL artifact — https://github.com/Unakar/Logic-RL（Current launcher/reward/data code；paper-recipe mismatch retained；Accessed: 2026-08-18）
- SWE-Lancer v2 — https://arxiv.org/pdf/2502.12115v2（v1: 2025-02-17；v2: 2025-02-19；Accessed: 2026-08-18）
- SWE-Lancer artifact lineage — https://github.com/openai/SWELancer-Benchmark；https://github.com/openai/frontier-evals/tree/main/project/swelancer（Original repo archived/migrated；later 198-task subset not projected backward；Accessed: 2026-08-18）
- TrustGen v1 — https://arxiv.org/abs/2502.14296（v1: 2025-02-20；Accessed: 2026-08-18）
- TrustGen author paper — https://howiehwong.github.io/TrustGen.pdf（Accessed: 2026-08-18）
- TrustGen project — https://trustgen.github.io/（Accessed: 2026-08-18）
- TrustEval toolkit — https://github.com/TrustGen/TrustEval-toolkit（event-time snapshot not pinned；Accessed: 2026-08-18）
- Text2World v1 — https://arxiv.org/html/2502.13092v1（First Public: 2025-02-18；W08 mechanism/evaluation source；Accessed: 2026-08-18）
- Text2World metadata — https://arxiv.org/abs/2502.13092（v1: 2025-02-18；v2: 2025-02-24；Accessed: 2026-08-18）
- Text2World official project — https://text-to-world.github.io/（paper/code/data entrypoint；Accessed: 2026-08-18）
- Text2World author repository — https://github.com/Aaron617/text2world（current mutable benchmark/generation/evaluation lineage；no W08 tag；Accessed: 2026-08-18）
- Text2World evaluator — https://github.com/Aaron617/text2world/blob/main/text2world/scripts/evaluate.py（current parser/component evaluation path；Accessed: 2026-08-18）
- Text2World runtime configuration — https://github.com/Aaron617/text2world/blob/main/utils/text2world.yaml（current mutable model/runtime lineage；not a frozen W08 run contract；Accessed: 2026-08-18）
- HeadInfer v1 — https://arxiv.org/html/2502.12574v1（First Public: 2025-02-18；mechanism/evaluation/appendix source；Accessed: 2026-08-18）
- HeadInfer metadata — https://arxiv.org/abs/2502.12574（v1: 2025-02-18；only revision visible；Accessed: 2026-08-18）
- HeadInfer author repository — https://github.com/wdlctc/headinfer（current mutable artifact；no release/tag；Accessed: 2026-08-18）
- HeadInfer current cache path — https://raw.githubusercontent.com/wdlctc/headinfer/main/headinfer/cache.py（head-as-pseudo-layer mapping；Accessed: 2026-08-18）
- HeadInfer current multi-process simulation — https://raw.githubusercontent.com/wdlctc/headinfer/main/headinfer/mp.py（zero-cache decode simulation path；Accessed: 2026-08-18）
- HeadInfer current entrypoint — https://raw.githubusercontent.com/wdlctc/headinfer/main/main.py（short real-prefill versus 1M simulated-decode boundary；Accessed: 2026-08-18）
- AdaptiveStep v1 — https://arxiv.org/html/2502.13943v1（First Public: 2025-02-19；mechanism/evaluation/appendix source；Accessed: 2026-08-18）
- AdaptiveStep metadata — https://arxiv.org/abs/2502.13943（v1: 2025-02-19；v2: 2025-05-31；Accessed: 2026-08-18）
- AdaptiveStep author repository — https://github.com/Lux0926/ASPRM（current mutable training/evaluation lineage；Accessed: 2026-08-18）
- AdaptiveStep current TVD path — https://raw.githubusercontent.com/Lux0926/ASPRM/main/evaluation/math/TVD/tvd.py（separate task/reward services and per-trigger Top-M scoring；Accessed: 2026-08-18）
- AdaptiveStep current training path — https://github.com/Lux0926/ASPRM/tree/main/train（OpenRLHF/BF16/ZeRO-2 invocation；Accessed: 2026-08-18）
- ASPRM-M training dataset — https://huggingface.co/datasets/Lux0926/ASPRM-M-Training-Dataset（current 388K-row artifact；not a frozen W08 manifest；Accessed: 2026-08-18）
- ASPRM training/evaluation environment — https://huggingface.co/Lux0926/ASPRM-Training-Evaluation-Environment（current mutable packaged environment；Accessed: 2026-08-18）
- AIDE v1 — https://arxiv.org/html/2502.13138v1（Formal paper event: 2025-02-18；mechanism/evaluation/appendix source；Accessed: 2026-08-18）
- AIDE metadata — https://arxiv.org/abs/2502.13138（Only arXiv version: v1；Accessed: 2026-08-18）
- AIDE first-public technical report — https://www.weco.ai/blog/technical-report（Source Family first public: 2024-04-04；Accessed: 2026-08-18）
- AIDE author repository — https://github.com/WecoAI/aideml（current mutable implementation lineage；Accessed: 2026-08-18）
- AIDE tags — https://github.com/WecoAI/aideml/tags（v0.1.2: 2024-04-26；v0.1.4: 2024-04-29；v0.2.0: 2025-01-23；Accessed: 2026-08-18）
- AIDE v0.2.0 release — https://github.com/WecoAI/aideml/releases/tag/v0.2.0（pre-paper release metadata and changes；Accessed: 2026-08-18）
- AIDE current Agent path — https://raw.githubusercontent.com/WecoAI/aideml/main/aide/agent.py（current draft/debug/improve selection and evaluation lineage；not paper-pinned；Accessed: 2026-08-18）
- AIDE current Journal path — https://raw.githubusercontent.com/WecoAI/aideml/main/aide/journal.py（candidate/run/metric lineage state；not paper-pinned；Accessed: 2026-08-18）
- AIDE current configuration — https://raw.githubusercontent.com/WecoAI/aideml/main/aide/utils/config.yaml（later mutable defaults；not the W08 evaluation contract；Accessed: 2026-08-18）
- MLE-bench — https://arxiv.org/html/2410.07095（independent AIDE scaffold, hardware, runtime, scaling and limitation contract；Accessed: 2026-08-18）
- MLE-bench repository — https://github.com/openai/mle-bench（benchmark and environment artifact lineage；Accessed: 2026-08-18）
- RE-Bench report — https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/（independent seven-environment/time-budget evidence and limitations；Accessed: 2026-08-18）
- Model-guidance v1 — https://arxiv.org/html/2502.12154v1（First Public: 2025-02-17；method, experiments, ablations and conclusion；Accessed: 2026-08-18）
- Model-guidance metadata — https://arxiv.org/abs/2502.12154（Only arXiv version: v1；Accessed: 2026-08-18）
- Model-guidance author repository — https://github.com/tzco/Diffusion-wo-CFG（Current mutable code/checkpoint lineage；no immutable W08 release/tag；Accessed: 2026-08-18）
- Model-guidance current training path — https://github.com/tzco/Diffusion-wo-CFG/blob/main/train.py（Explicit empty-label split, EMA teacher delta, start step and FID loop；not event-time pinned；Accessed: 2026-08-18）
- Model-guidance current sampler — https://github.com/tzco/Diffusion-wo-CFG/blob/main/sampler.py（One-pass scale-one path and optional two-branch CFG wrapper；not event-time pinned；Accessed: 2026-08-18）
- Model-guidance current model path — https://github.com/tzco/Diffusion-wo-CFG/blob/main/models.py（Empty-label embedding and label-drop semantics；not event-time pinned；Accessed: 2026-08-18）
