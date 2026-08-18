# AI Research Weekly — 2025-W21

> Coverage Window: 2025-05-19～2025-05-25 (ISO Monday–Sunday)
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 127/127 owner rows; 116/116 retained Full Source Reviews; 11/11 low closures
> Discovery / Archive Completion: Conditional — 1 noncanonical P0 identity gap
> Historical Books Gate: Closed

## Executive Summary

旧三项基线已被完整 discovery replay 取代。本周最终账目为 **127 个 canonical owner：60 个 25～30 分、56 个 20～24 分、11 个低于 20 分**。全部 116 个 retained family 均有独立、非模板化 Full Source Review；11 个低分 family 均有身份、日期、六维评分与拒绝边界；`Review Pending = 0`。

W22 中九个按 arXiv v1 日期应归 W21 的 family 已回拨；BARREL (`2505.13529`) 明确保留为 W20 spillback，不进入 W21 算术。五个 revision dispute 都具有稳定 primary identity，并冻结 event-time 数值边界，因此不是 pending。唯一未闭合项是账外发现标签 `Teaching Models to Lie`：无法唯一映射 title/author/arXiv/DOI，故 Discovery / Archive Completion 保持 `Conditional`，不得伪造分数或 Source Review。

本轮只闭合 Weekly evidence。Candidate Evidence Gate 已通过，但 Historical Books Gate 仍关闭；本文件不授权任何 Books 写入。

## Coverage Window and Limitations

- Owner 以官方 first-public date、GitHub Release/tag 或 arXiv v1 日期判定；后续 revision 只作为同一 Source Family 的演进证据。
- 机构站点、arXiv、Google Scholar、OpenAlex、DBLP、Hugging Face discovery feed 与 AI Infra release/RFC/PR 按固定顺序重放；Scholar/OpenAlex 等只用于发现和去重，机制结论回到 primary source。
- 历史回填不补造 Daily；本次访问与复核日期为 2026-08-24。
- 作者或厂商 benchmark 只在披露的 model、hardware、precision、length、batch/concurrency、SLO 与 evaluator 条件内成立；未披露字段保持 `Not Disclosed`。
- `Teaching Models to Lie` 缺唯一身份，保留为账外 P0 material request；不影响 127 个已识别 canonical owner 的 Candidate Evidence Gate。

## 1. 模型与研究机构

按固定机构顺序重放 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。保留 Claude 4、Anthropic API agent capability、ASL-3 safeguards、Google I/O 相关版本事实、NLWeb 与 llm-d launch；只有公告而无公开内部机制的条目固定为 `Version Fact / Mechanism Not Disclosed`。

## 2. 论文与学术来源

按 arXiv v1 日期重放 2025-05-19～2025-05-25，并以论文 HTML/PDF、appendix、作者 repository/artifact 完成机制核验；后续 revision 不产生新的 W21 事件。学术候选覆盖 training/reasoning、evaluation/security、multimodal/world model、agent/workflow、KV/cache/scheduling 与 observability，不以 discovery 排名替代全文证据。

## 3. AI Infra 与工程项目

按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA 的官方 release/RFC/PR/repository 路径重放。llm-d 与 vLLM V0 deprecation RFC 进入机制/提案审查；Transformers v4.52.1 与 JAX v0.6.1 仅作为低分版本事实归档。

## Canonical Source Ledger

Legend: `S` source-complete retained; `L` low-score closure; `D` disputed version boundary; `F` version fact / mechanism not disclosed.

| # | Candidate / Source Family | First public | Primary identifier / URL | Score | State | Owner / routing |
|---:|---|---|---|---:|---|---|
| 1 | llm-d community launch | 2025-05-20 | https://developers.redhat.com/articles/2025/05/20/llm-d-kubernetes-native-distributed-inferencing | 27 | S | W21 |
| 2 | Claude 4 | 2025-05-22 | https://www.anthropic.com/news/claude-4 | 22 | S/F | W21 |
| 3 | User-level DP follow-up | paper v1 2024-07-10; blog 2025-05-23 | https://arxiv.org/abs/2407.07737 | 23 | S | paper owner 2024; follow-up W21 |
| 4 | AdaptThink | 2025-05-19 | https://arxiv.org/abs/2505.13417 | 24 | S | W21 |
| 5 | BRPO / AnytimeReasoner | 2025-05-20 | https://arxiv.org/abs/2505.13438 | 24 | S | W21 |
| 6 | Efficient Agent Training for Computer Use | 2025-05-20 | https://arxiv.org/abs/2505.13909 | 27 | S | W21 |
| 7 | RLVR-World | 2025-05-20 | https://arxiv.org/abs/2505.13934 | 23 | S | W21 |
| 8 | UniVG-R1 | 2025-05-20 | https://arxiv.org/abs/2505.14231 | 20 | S | W21 |
| 9 | Visual ARFT | 2025-05-20 | https://arxiv.org/abs/2505.14246 | 24 | S | W21 |
| 10 | Scaling Law for QAT | 2025-05-20 | https://arxiv.org/abs/2505.14302 | 29 | S | W21 |
| 11 | Vid2World | 2025-05-20 | https://arxiv.org/abs/2505.14357 | 28 | S | W21 |
| 12 | Reasoning Models Better Express Confidence | 2025-05-20 | https://arxiv.org/abs/2505.14489 | 26 | S | W21 |
| 13 | Hunyuan-Game | 2025-05-20 | https://arxiv.org/abs/2505.14135 | 22 | S | W21 |
| 14 | Latent Flow Transformer | 2025-05-20 | https://arxiv.org/abs/2505.14513 | 23 | S | W21 |
| 15 | Self-Braking Tuning | 2025-05-20 | https://arxiv.org/abs/2505.14604 | 24 | S | W21 |
| 16 | Quartet | 2025-05-20 | https://arxiv.org/abs/2505.14669 | 29 | S | W21; W22 spillback |
| 17 | Reward Reasoning Model | 2025-05-20 | https://arxiv.org/abs/2505.14674 | 24 | S | W21 |
| 18 | BAGEL / Emerging Properties in Unified Multimodal Pretraining | 2025-05-20 | https://arxiv.org/abs/2505.14683 | 28 | S | W21 |
| 19 | Scaling Reasoning, Losing Control | 2025-05-20 | https://arxiv.org/abs/2505.14810 | 26 | S | W21 |
| 20 | RL-Tango | 2025-05-21 | https://arxiv.org/abs/2505.15034 | 24 | S | W21 |
| 21 | Entropy Minimization in LLM Reasoning | 2025-05-21 | https://arxiv.org/abs/2505.15134 | 21 | S | W21 |
| 22 | BanditSpec | 2025-05-21 | https://arxiv.org/abs/2505.15141 | 29 | S | W21 |
| 23 | Scaling DiT via muP | 2025-05-21 | https://arxiv.org/abs/2505.15270 | 25 | S | W21 |
| 24 | Web-Shepherd | 2025-05-21 | https://arxiv.org/abs/2505.15277 | 29 | S | W21 |
| 25 | Adaptive Self-Recovery Reasoning | 2025-05-21 | https://arxiv.org/abs/2505.15400 | 24 | S | W21 |
| 26 | LASER-D adaptive length reward | 2025-05-21 | https://arxiv.org/abs/2505.15612 | 24 | S | W21 |
| 27 | Soft Thinking | 2025-05-21 | https://arxiv.org/abs/2505.15778 | 23 | S | W21 |
| 28 | dKV-Cache | 2025-05-21 | https://arxiv.org/abs/2505.15781 | 29 | S | W21 |
| 29 | VerifyBench: Benchmarking Reference-based Reward Systems | 2025-05-21 | https://arxiv.org/abs/2505.15801 | 26 | S | W21 |
| 30 | MMaDA | 2025-05-21 | https://arxiv.org/abs/2505.15809 | 28 | S | W21 |
| 31 | Streamline Without Sacrifice / ProxyV | 2025-05-21 | https://arxiv.org/abs/2505.15816 | 24 | S | W21 |
| 32 | Pixel Reasoner | 2025-05-21 | https://arxiv.org/abs/2505.15966 | 20 | S | W21 |
| 33 | QuickVideo | 2025-05-22 | https://arxiv.org/abs/2505.16175 | 29 | S | W21 |
| 34 | Embodied MEMENTO | 2025-05-22 | https://arxiv.org/abs/2505.16348 | 27 | S | W21; W22 spillback |
| 35 | AceReason-Nemotron | 2025-05-22 | https://arxiv.org/abs/2505.16400 | 25 | S | W21 |
| 36 | Tool-Star | 2025-05-22 | https://arxiv.org/abs/2505.16410 | 29 | S | W21 |
| 37 | WebAgent-R1 | 2025-05-22 | https://arxiv.org/abs/2505.16421 | 29 | S | W21 |
| 38 | Jenga / Dynamic Token Carving | 2025-05-22 | https://arxiv.org/abs/2505.16864 | 24 | S | W21 |
| 39 | LLaDA-V | 2025-05-22 | https://arxiv.org/abs/2505.16933 | 23 | S | W21 |
| 40 | NovelSeek (renamed InternAgent in later revision) | 2025-05-22 | https://arxiv.org/abs/2505.16938 | 26 | S/D | W21; title lineage pinned |
| 41 | Dimple | 2025-05-22 | https://arxiv.org/abs/2505.16990 | 23 | S | W21 |
| 42 | GoT-R1 | 2025-05-22 | https://arxiv.org/abs/2505.17022 | 23 | S | W21 |
| 43 | QwenLong-L1 | 2025-05-23 | https://arxiv.org/abs/2505.17667 | 30 | S | W21; W22 spillback |
| 44 | TabSTAR | 2025-05-23 | https://arxiv.org/abs/2505.18125 | 25 | S | W21; W22 spillback |
| 45 | Flex-Judge | 2025-05-24 | https://arxiv.org/abs/2505.18601 | 26 | S | W21; W22 spillback |
| 46 | VerIPO | 2025-05-25 | https://arxiv.org/abs/2505.19000 | 24 | S | W21; W22 spillback |
| 47 | Data-centric compression | 2025-05-25 | https://arxiv.org/abs/2505.19147 | 25 | S | W21; W22 spillback |
| 48 | PATS | 2025-05-25 | https://arxiv.org/abs/2505.19250 | 24 | S | W21; W22 spillback |
| 49 | DeepResearchGym | 2025-05-25 | https://arxiv.org/abs/2505.19253 | 29 | S | W21; W22 spillback |
| 50 | NLWeb | 2025-05-19 | https://blogs.microsoft.com/blog/2025/05/19/introducing-nlweb/ | 27 | S | W21 |
| 51 | Anthropic API code execution / MCP connector / Files API | 2025-05-22 | https://www.anthropic.com/news/agent-capabilities-api | 22 | F/S | W21 |
| 52 | Anthropic ASL-3 safeguards | 2025-05-22 | https://www.anthropic.com/news/activating-asl3-protections | 27 | S | W21 |
| 53 | Gemini Diffusion experimental preview | 2025-05-20 | https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-diffusion/ | 19 | L/F | archive only |
| 54 | Gemini universal-assistant / world-model vision | 2025-05-20 | https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-universal-ai-assistant/ | 18 | L/F | archive only |
| 55 | Veo 3 / Imagen 4 launch family | 2025-05-20 | https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/ | 18 | L/F | archive only |
| 56 | Gemma 3n preview | 2025-05-20 | https://developers.googleblog.com/en/introducing-gemma-3n/ | 19 | L/F | archive only |
| 57 | Transformers v4.52.1 | 2025-05-22 | https://github.com/huggingface/transformers/releases/tag/v4.52.1 | 18 | L/F | archive only |
| 58 | JAX v0.6.1 | 2025-05-21 | https://github.com/jax-ml/jax/blob/main/CHANGELOG.md#jax-061-may-21-2025 | 17 | L/F | archive only |
| 59 | Distilling LLM Agent into Small Models with Retrieval and Code Tools | 2025-05-23 | https://arxiv.org/abs/2505.17612 | 26 | S | W21 |
| 60 | Reasoning Model is Stubborn / ReasoningTrap | 2025-05-22 | https://arxiv.org/abs/2505.17225 | 24 | S | W21 |
| 61 | One RL to See Them All: Visual Triple Unified Reinforcement Learning | 2025-05-23 | https://arxiv.org/abs/2505.18129 | 23 | S/D | W21; title lineage pinned |
| 62 | PhyX | 2025-05-21 | https://arxiv.org/abs/2505.15929 | 22 | S | W21 |
| 63 | QwenLong-CPRS | 2025-05-23 | https://arxiv.org/abs/2505.18092 | 26 | S | W21 |
| 64 | EvoSearch | 2025-05-23 | https://arxiv.org/abs/2505.17618 | 22 | S | W21 |
| 65 | MOOSE-Chem3 | 2025-05-23 | https://arxiv.org/abs/2505.17873 | 22 | S | W21 |
| 66 | VeriThinker | 2025-05-23 | https://arxiv.org/abs/2505.17941 | 24 | S | W21 |
| 67 | Direct3D-S2 | 2025-05-23 | https://arxiv.org/abs/2505.17412 | 23 | S | W21 |
| 68 | s3: You Don't Need That Much Data to Train a Search Agent via RL | 2025-05-20 | https://arxiv.org/abs/2505.14146 | 26 | S | W21 |
| 69 | AudioTrust | 2025-05-22 | https://arxiv.org/abs/2505.16211 | 23 | S | W21 |
| 70 | FullFront | 2025-05-23 | https://arxiv.org/abs/2505.17399 | 19 | L | archive only |
| 71 | TemplateRL / TAPO title-lineage family | 2025-05-21 | https://arxiv.org/abs/2505.15692 | 23 | S/D | W21; v1 title pin required |
| 72 | Trinity-RFT | 2025-05-23 | https://arxiv.org/abs/2505.17826 | 25 | S | W21 |
| 73 | CUB: Benchmarking Context Utilisation Techniques for Language Models | 2025-05-22 | https://arxiv.org/abs/2505.16518 | 23 | S | W21 |
| 74 | Interactive Post-Training for Vision-Language-Action Models (RIPT-VLA) | 2025-05-22 | https://arxiv.org/abs/2505.17016 | 24 | S | W21 |
| 75 | ReflAct | 2025-05-21 | https://arxiv.org/abs/2505.15182 | 23 | S | W21 |
| 76 | NOVER | 2025-05-21 | https://arxiv.org/abs/2505.16022 | 23 | S | W21 |
| 77 | Not All Models Suit Expert Offloading | 2025-05-21 | https://arxiv.org/abs/2505.16056 | 26 | S | W21 |
| 78 | Keep Security! / CoPriva | 2025-05-21 | https://arxiv.org/abs/2505.15805 | 23 | S | W21 |
| 79 | FREESON | 2025-05-22 | https://arxiv.org/abs/2505.16409 | 23 | S | W21 |
| 80 | Thinkless | 2025-05-19 | https://arxiv.org/abs/2505.13379 | 26 | S | W21 |
| 81 | OSWorld-G / Jedi | 2025-05-19 | https://arxiv.org/abs/2505.13227 | 27 | S | W21 |
| 82 | VSA sparse attention | 2025-05-19 | https://arxiv.org/abs/2505.13389 | 29 | S | W21 |
| 83 | LatentSeek | 2025-05-19 | https://arxiv.org/abs/2505.13308 | 24 | S | W21 |
| 84 | MM-PRM | 2025-05-19 | https://arxiv.org/abs/2505.13427 | 25 | S | W21 |
| 85 | FedSVD | 2025-05-19 | https://arxiv.org/abs/2505.12805 | 26 | S | W21 |
| 86 | R3 reward model | 2025-05-19 | https://arxiv.org/abs/2505.13388 | 25 | S | W21 |
| 87 | GS-Jacobi / TarFlow | 2025-05-19 | https://arxiv.org/abs/2505.12849 | 27 | S | W21 |
| 88 | Low-Rank Clone | 2025-05-19 | https://arxiv.org/abs/2505.12781 | 26 | S | W21 |
| 89 | Neurosymbolic Diffusion | 2025-05-19 | https://arxiv.org/abs/2505.13138 | 25 | S | W21 |
| 90 | AutoMat | 2025-05-19 | https://arxiv.org/abs/2505.12650 | 24 | S | W21 |
| 91 | CompeteSMoE | 2025-05-19 | https://arxiv.org/abs/2505.13380 | 24 | S | W21 |
| 92 | QZO | 2025-05-19 | https://arxiv.org/abs/2505.13430 | 24 | S | W21 |
| 93 | PiFlow | 2025-05-21 | https://arxiv.org/abs/2505.15047 | 24 | S | W21 |
| 94 | VisualQuality-R1 | 2025-05-20 | https://arxiv.org/abs/2505.14460 | 21 | S | W21 |
| 95 | RICE cognitive experts | 2025-05-20 | https://arxiv.org/abs/2505.14681 | 24 | S | W21 |
| 96 | Distillation source matters | 2025-05-20 | https://arxiv.org/abs/2505.14464 | 24 | S | W21 |
| 97 | Vittle | 2025-05-20 | https://arxiv.org/abs/2505.13946 | 24 | S | W21 |
| 98 | Latent knowledge elicitation | 2025-05-20 | https://arxiv.org/abs/2505.14352 | 22 | S | W21 |
| 99 | AgentIF | 2025-05-22 | https://arxiv.org/abs/2505.16944 | 25 | S | W21 |
| 100 | Think-RM | 2025-05-22 | https://arxiv.org/abs/2505.16265 | 25 | S | W21 |
| 101 | TinyV | 2025-05-20 | https://arxiv.org/abs/2505.14625 | 26 | S | W21 |
| 102 | LaViDa | 2025-05-22 | https://arxiv.org/abs/2505.16839 | 26 | S | W21 |
| 103 | FoVer | 2025-05-21 | https://arxiv.org/abs/2505.15960 | 27 | S | W21 |
| 104 | SafeKey | 2025-05-21 | https://arxiv.org/abs/2505.16186 | 25 | S | W21 |
| 105 | OViP | 2025-05-21 | https://arxiv.org/abs/2505.15963 | 25 | S | W21 |
| 106 | TON selective reasoning | 2025-05-22 | https://arxiv.org/abs/2505.16854 | 25 | S | W21 |
| 107 | SophiaVL-R1 | 2025-05-22 | https://arxiv.org/abs/2505.17018 | 26 | S | W21 |
| 108 | BYE backdoor cleaning | 2025-05-22 | https://arxiv.org/abs/2505.16916 | 26 | S | W21 |
| 109 | SpatialScore | 2025-05-22 | https://arxiv.org/abs/2505.17012 | 24 | S/D | W21; v1/current drift |
| 110 | OCR Heads | 2025-05-21 | https://arxiv.org/abs/2505.15865 | 23 | S | W21 |
| 111 | VLM-R3 | 2025-05-21 | https://arxiv.org/abs/2505.16192 | 26 | S | W21 |
| 112 | LLM retraction / admit mistakes | 2025-05-21 | https://arxiv.org/abs/2505.16170 | 26 | S/D | W21; v1 mechanism retained, current v4 numerics not backported |
| 113 | vLLM V0 deprecation RFC | 2025-05-22 | https://github.com/vllm-project/vllm/issues/18571 | 24 | S | proposal only |
| 114 | MMMG | 2025-05-23 | https://arxiv.org/abs/2505.17613 | 27 | S | W21 |
| 115 | Implicit multi-hop scaling | 2025-05-23 | https://arxiv.org/abs/2505.17923 | 25 | S | W21 |
| 116 | NFT negative-aware fine-tuning | 2025-05-23 | https://arxiv.org/abs/2505.18116 | 26 | S | W21 |
| 117 | SVL spiking V-L pretraining | 2025-05-23 | https://arxiv.org/abs/2505.17674 | 22 | S | W21 |
| 118 | MSPGT | 2025-05-23 | https://arxiv.org/abs/2505.18244 | 19 | L | abstract/metadata sufficient only for narrow theoretical-position rejection; mechanism claims frozen |
| 119 | MUG-Eval | 2025-05-20 | https://arxiv.org/abs/2505.14395 | 19 | L | abstract/metadata sufficient only for narrow benchmark-relevance rejection; detailed results frozen |
| 120 | Just as Humans Need Vaccines, So Do Models: Model Immunization to Combat Falsehoods | 2025-05-23 | https://arxiv.org/abs/2505.17870 | 18 | L | archive only; position paper |
| 121 | MemeReaCon | 2025-05-23 | https://arxiv.org/abs/2505.17433 | 19 | L | archive only |
| 122 | Reasoning Path Compression | 2025-05-20 | https://arxiv.org/abs/2505.13866 | 24 | S | W21; `INFER-KV-CACHE` |
| 123 | Lessons from Defending Gemini Against Indirect Prompt Injections | 2025-05-20 | https://arxiv.org/abs/2505.14534 | 27 | S | W21; `PLATFORM-SECURITY` |
| 124 | The Hallucination Tax of Reinforcement Finetuning | 2025-05-20 | https://arxiv.org/abs/2505.13988 | 25 | S | W21; `TRAIN-GRPO` |
| 125 | Be Careful When Fine-tuning On Open-Source LLMs | 2025-05-21 | https://arxiv.org/abs/2505.15656 | 27 | S | W21; `PLATFORM-SECURITY` |
| 126 | How Should We Enhance the Safety of Large Reasoning Models | 2025-05-21 | https://arxiv.org/abs/2505.15404 | 22 | S | W21; `TRAIN-SFT` |
| 127 | This Time is Different / Toto + BOOM | 2025-05-20 | https://arxiv.org/abs/2505.14766 | 26 | S | W21; `PLATFORM-MONITORING` |

## Candidate Scoring

Dimensions: Technical Novelty (TN), System Impact (SI), Practical Value (PV), Source Reliability (SR), Project Relevance (PR), Longevity (L), each 0–5.

| # | Candidate / Source Family | TN | SI | PV | SR | PR | L | Total | Decision |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | llm-d community launch | 4 | 5 | 5 | 5 | 4 | 4 | 27 | Retained |
| 2 | Claude 4 | 4 | 4 | 3 | 5 | 3 | 3 | 22 | Retained |
| 3 | User-level DP follow-up | 4 | 4 | 4 | 5 | 3 | 3 | 23 | Retained |
| 4 | AdaptThink | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 5 | BRPO / AnytimeReasoner | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 6 | Efficient Agent Training for Computer Use | 4 | 4 | 5 | 4 | 5 | 5 | 27 | Retained |
| 7 | RLVR-World | 4 | 4 | 4 | 4 | 3 | 4 | 23 | Retained |
| 8 | UniVG-R1 | 3 | 3 | 3 | 4 | 4 | 3 | 20 | Retained |
| 9 | Visual ARFT | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 10 | Scaling Law for QAT | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 11 | Vid2World | 5 | 4 | 5 | 4 | 5 | 5 | 28 | Retained |
| 12 | Reasoning Models Better Express Confidence | 4 | 4 | 4 | 4 | 5 | 5 | 26 | Retained |
| 13 | Hunyuan-Game | 3 | 4 | 4 | 4 | 4 | 3 | 22 | Retained |
| 14 | Latent Flow Transformer | 3 | 4 | 4 | 4 | 4 | 4 | 23 | Retained |
| 15 | Self-Braking Tuning | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 16 | Quartet | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 17 | Reward Reasoning Model | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 18 | BAGEL / Emerging Properties in Unified Multimodal Pretraining | 5 | 5 | 5 | 4 | 4 | 5 | 28 | Retained |
| 19 | Scaling Reasoning, Losing Control | 4 | 5 | 5 | 4 | 4 | 4 | 26 | Retained |
| 20 | RL-Tango | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 21 | Entropy Minimization in LLM Reasoning | 3 | 4 | 4 | 4 | 3 | 3 | 21 | Retained |
| 22 | BanditSpec | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 23 | Scaling DiT via muP | 5 | 4 | 4 | 4 | 4 | 4 | 25 | Retained |
| 24 | Web-Shepherd | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 25 | Adaptive Self-Recovery Reasoning | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 26 | LASER-D adaptive length reward | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 27 | Soft Thinking | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Retained |
| 28 | dKV-Cache | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 29 | VerifyBench: Benchmarking Reference-based Reward Systems | 4 | 5 | 5 | 4 | 4 | 4 | 26 | Retained |
| 30 | MMaDA | 5 | 4 | 5 | 4 | 5 | 5 | 28 | Retained |
| 31 | Streamline Without Sacrifice / ProxyV | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 32 | Pixel Reasoner | 3 | 3 | 3 | 4 | 4 | 3 | 20 | Retained |
| 33 | QuickVideo | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 34 | Embodied MEMENTO | 4 | 5 | 5 | 4 | 5 | 4 | 27 | Retained |
| 35 | AceReason-Nemotron | 4 | 4 | 5 | 4 | 4 | 4 | 25 | Retained |
| 36 | Tool-Star | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 37 | WebAgent-R1 | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 38 | Jenga / Dynamic Token Carving | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 39 | LLaDA-V | 4 | 3 | 4 | 4 | 4 | 4 | 23 | Retained |
| 40 | NovelSeek / InternAgent title-lineage family | 4 | 4 | 5 | 4 | 5 | 4 | 26 | Retained |
| 41 | Dimple | 4 | 4 | 4 | 4 | 3 | 4 | 23 | Retained |
| 42 | GoT-R1 | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Retained |
| 43 | QwenLong-L1 | 5 | 5 | 5 | 5 | 5 | 5 | 30 | Retained |
| 44 | TabSTAR | 4 | 5 | 4 | 4 | 4 | 4 | 25 | Retained |
| 45 | Flex-Judge | 4 | 4 | 5 | 4 | 5 | 4 | 26 | Retained |
| 46 | VerIPO | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 47 | Data-centric compression | 4 | 4 | 4 | 4 | 4 | 5 | 25 | Retained |
| 48 | PATS | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 49 | DeepResearchGym | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 50 | NLWeb | 4 | 4 | 5 | 5 | 5 | 4 | 27 | Retained |
| 51 | Anthropic API code execution / MCP connector / Files API | 3 | 4 | 4 | 5 | 3 | 3 | 22 | Retained |
| 52 | Anthropic ASL-3 safeguards | 5 | 4 | 4 | 5 | 4 | 5 | 27 | Retained |
| 53 | Distilling LLM Agent into Small Models with Retrieval and Code Tools | 4 | 5 | 5 | 4 | 4 | 4 | 26 | Retained |
| 54 | Reasoning Model is Stubborn / ReasoningTrap | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 55 | One RL to See Them All | 4 | 4 | 4 | 4 | 3 | 4 | 23 | Retained |
| 56 | PhyX | 3 | 4 | 4 | 4 | 4 | 3 | 22 | Retained |
| 57 | QwenLong-CPRS | 5 | 5 | 4 | 4 | 4 | 4 | 26 | Retained |
| 58 | EvoSearch | 4 | 3 | 3 | 4 | 4 | 4 | 22 | Retained |
| 59 | MOOSE-Chem3 | 4 | 4 | 3 | 4 | 3 | 4 | 22 | Retained |
| 60 | VeriThinker | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 61 | Direct3D-S2 | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Retained |
| 62 | s3: You Don't Need That Much Data to Train a Search Agent via RL | 5 | 5 | 4 | 4 | 4 | 4 | 26 | Retained |
| 63 | AudioTrust | 4 | 3 | 4 | 4 | 4 | 4 | 23 | Retained |
| 64 | TemplateRL / TAPO title-lineage family | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Retained |
| 65 | Trinity-RFT | 5 | 4 | 4 | 4 | 4 | 4 | 25 | Retained |
| 66 | CUB: Benchmarking Context Utilisation Techniques for Language Models | 4 | 3 | 4 | 4 | 4 | 4 | 23 | Retained |
| 67 | Interactive Post-Training for Vision-Language-Action Models (RIPT-VLA) | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 68 | ReflAct | 4 | 4 | 4 | 4 | 3 | 4 | 23 | Retained |
| 69 | NOVER | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Retained |
| 70 | Not All Models Suit Expert Offloading | 5 | 5 | 4 | 4 | 4 | 4 | 26 | Retained |
| 71 | Keep Security! / CoPriva | 4 | 3 | 4 | 4 | 4 | 4 | 23 | Retained |
| 72 | FREESON | 4 | 4 | 3 | 4 | 4 | 4 | 23 | Retained |
| 73 | Thinkless | 4 | 4 | 4 | 4 | 5 | 5 | 26 | Retained |
| 74 | OSWorld-G / Jedi | 5 | 5 | 4 | 4 | 4 | 5 | 27 | Retained |
| 75 | VSA sparse attention | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Retained |
| 76 | LatentSeek | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 77 | MM-PRM | 4 | 4 | 5 | 4 | 4 | 4 | 25 | Retained |
| 78 | FedSVD | 4 | 4 | 4 | 4 | 5 | 5 | 26 | Retained |
| 79 | R3 reward model | 4 | 4 | 4 | 4 | 4 | 5 | 25 | Retained |
| 80 | GS-Jacobi / TarFlow | 5 | 5 | 5 | 4 | 4 | 4 | 27 | Retained |
| 81 | Low-Rank Clone | 4 | 5 | 5 | 4 | 4 | 4 | 26 | Retained |
| 82 | Neurosymbolic Diffusion | 4 | 4 | 5 | 4 | 4 | 4 | 25 | Retained |
| 83 | AutoMat | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 84 | CompeteSMoE | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 85 | QZO | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 86 | PiFlow | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 87 | VisualQuality-R1 | 4 | 4 | 3 | 4 | 3 | 3 | 21 | Retained |
| 88 | RICE cognitive experts | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 89 | Distillation source matters | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 90 | Vittle | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 91 | Latent knowledge elicitation | 4 | 3 | 3 | 4 | 4 | 4 | 22 | Retained |
| 92 | AgentIF | 4 | 4 | 5 | 4 | 4 | 4 | 25 | Retained |
| 93 | Think-RM | 4 | 4 | 4 | 4 | 5 | 4 | 25 | Retained |
| 94 | TinyV | 5 | 4 | 4 | 4 | 4 | 5 | 26 | Retained |
| 95 | LaViDa | 5 | 5 | 4 | 4 | 4 | 4 | 26 | Retained |
| 96 | FoVer | 4 | 5 | 5 | 4 | 5 | 4 | 27 | Retained |
| 97 | SafeKey | 4 | 4 | 5 | 4 | 4 | 4 | 25 | Retained |
| 98 | OViP | 4 | 4 | 4 | 4 | 5 | 4 | 25 | Retained |
| 99 | TON selective reasoning | 4 | 4 | 4 | 4 | 4 | 5 | 25 | Retained |
| 100 | SophiaVL-R1 | 5 | 5 | 4 | 4 | 4 | 4 | 26 | Retained |
| 101 | BYE backdoor cleaning | 4 | 5 | 5 | 4 | 4 | 4 | 26 | Retained |
| 102 | SpatialScore | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 103 | OCR Heads | 4 | 4 | 4 | 4 | 3 | 4 | 23 | Retained |
| 104 | VLM-R3 | 5 | 4 | 4 | 4 | 4 | 5 | 26 | Retained |
| 105 | LLM retraction / admit mistakes | 5 | 5 | 4 | 4 | 4 | 4 | 26 | Retained |
| 106 | vLLM V0 deprecation RFC | 4 | 3 | 4 | 5 | 4 | 4 | 24 | Retained |
| 107 | MMMG | 4 | 4 | 5 | 4 | 5 | 5 | 27 | Retained |
| 108 | Implicit multi-hop scaling | 4 | 4 | 4 | 4 | 5 | 4 | 25 | Retained |
| 109 | NFT negative-aware fine-tuning | 5 | 4 | 4 | 4 | 4 | 5 | 26 | Retained |
| 110 | SVL spiking V-L pretraining | 3 | 3 | 4 | 4 | 4 | 4 | 22 | Retained |
| 111 | Reasoning Path Compression | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Retained |
| 112 | Lessons from Defending Gemini Against Indirect Prompt Injections | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Retained |
| 113 | The Hallucination Tax of Reinforcement Finetuning | 4 | 4 | 4 | 4 | 5 | 4 | 25 | Retained |
| 114 | Be Careful When Fine-tuning On Open-Source LLMs | 5 | 5 | 4 | 4 | 5 | 4 | 27 | Retained |
| 115 | How Should We Enhance the Safety of Large Reasoning Models | 3 | 3 | 3 | 4 | 5 | 4 | 22 | Retained |
| 116 | This Time is Different / Toto + BOOM | 4 | 4 | 4 | 5 | 5 | 4 | 26 | Retained |
| 117 | Gemini Diffusion experimental preview | 3 | 2 | 3 | 5 | 3 | 3 | 19 | Archive only |
| 118 | Gemini universal-assistant/world-model vision | 2 | 2 | 2 | 5 | 3 | 4 | 18 | Archive only |
| 119 | Google generative-media launch (Veo 3 + Imagen 4) | 3 | 2 | 2 | 5 | 3 | 3 | 18 | Archive only |
| 120 | Gemma 3n preview | 3 | 3 | 3 | 5 | 3 | 2 | 19 | Archive only |
| 121 | Transformers v4.52.1 | 1 | 3 | 4 | 5 | 3 | 2 | 18 | Archive only |
| 122 | JAX v0.6.1 | 1 | 3 | 3 | 5 | 3 | 2 | 17 | Archive only |
| 123 | FullFront | 2 | 2 | 2 | 5 | 4 | 4 | 19 | Archive only |
| 124 | MSPGT | 3 | 2 | 2 | 4 | 4 | 4 | 19 | Archive only |
| 125 | MUG-Eval | 3 | 2 | 3 | 4 | 4 | 3 | 19 | Archive only |
| 126 | Model Immunization to Combat Falsehoods | 2 | 2 | 2 | 4 | 4 | 4 | 18 | Archive only |
| 127 | MemeReaCon | 2 | 2 | 3 | 4 | 4 | 4 | 19 | Archive only |
### Deep Analysis 1 — llm-d community launch

- First Public: 2025-05-20
- Status: Official open-source project launch
- Primary Source: https://developers.redhat.com/articles/2025/05/20/llm-d-kubernetes-native-distributed-inferencing
- Evolution Relationship: Direct Evolution

#### Why

传统 Service/round-robin 不理解 KV locality、prefill/decode 阶段、adapter 与 SLO，单 engine 也不拥有 Kubernetes fleet 的全局状态。

#### Principle and Mechanism

llm-d 以 vLLM 为 data plane，结合 Inference Gateway、KV-aware routing、PD disaggregation 与 Kubernetes-native lifecycle，形成可替换组件的 distributed inference stack。

#### Trade-off and Evidence Boundary

模块化避免单体锁定，却新增组件版本矩阵、跨层观测、状态一致性和责任边界；项目发布不等于所有路径已生产成熟。

#### Connection and Evolution

知识树位置：第 48、49、51、52、57、58 章。Must Read；与 KServe/Gateway/Dynamo 建立边界。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Claude 4

- First Public: 2025-05-22
- Status: Official release + system card; vendor evaluation
- Primary Source: https://www.anthropic.com/news/claude-4
- Evolution Relationship: Direct Evolution

#### Why

长时 coding/agent workload 需要在 reasoning 中调用工具，并把跨轮次状态外化到文件或 memory。

#### Principle and Mechanism

官方发布披露 extended thinking with tool use、parallel tools 与通过文件保存事实的产品行为；内部实现未知。

#### Trade-off and Evidence Boundary

外化 memory 提高 continuity，也带来 provenance、staleness、权限和 prompt injection 风险；benchmark 无法分离模型与 harness。

#### Connection and Evolution

知识树位置：第 52、62、73～77 章。Worth Watching；与 Memory/Tool章节交叉审查。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 3 — User-level differential privacy for LLM fine-tuning

- First Public: 2025-05-23
- Status: Google Research official blog + paper
- Primary Source: https://research.google/blog/fine-tuning-llms-with-user-level-differential-privacy/
- Evolution Relationship: Direct Evolution

#### Why

record-level DP 不能限制同一用户多条记录的累计影响；真实对话和个性化数据的隐私单元通常是 user。

#### Principle and Mechanism

研究把 user-level clipping/sampling/accounting 用于 LLM fine-tuning，并分析 user contribution 不均衡的优化问题。

#### Trade-off and Evidence Boundary

更强隐私单元提高保护语义，却降低有效样本量、增加噪声与训练复杂度；utility 结论取决于用户分布和 privacy budget。

#### Connection and Evolution

知识树位置：第 25、62、68 章。Must Read；与 W12 inference-time DP 形成层次关系。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。


## Full Source Review

### llm-d community launch

- **Candidate / Week / Score:** llm-d community launch / 2025-W21 / 27/30。
- **Source Family ID:** `LLMD-2025-LAUNCH`。
- **Source Type:** 官方项目发布、创始 proposal、开源仓库。
- **First-public Date / Revision History:** 项目于 2025-05-20 公开；当前 proposal 页面后来随项目重组而更新，因此只把其中明确写作 initial goals/design choices 的内容用于 2025 机制重建，2026 component/release 事实不回投到首发版本。
- **Direct Primary Sources:** llm-d 首发公告；`llm-d` founding proposal；项目仓库与 launch-time architecture description。
- **Related Primary Sources:** vLLM、Gateway API Inference Extension 与 NIXL 各自文档；它们证明依赖层能力，不证明 llm-d 的端到端成熟度。
- **Access and Verification Status:** Verified。公告、proposal 与 repository documentation 均可访问；首发时各 component 的精确 commit matrix 未在公告完整冻结。
- **Full-read Coverage:** 已阅读 launch announcement、proposal 的 goals/non-goals、四项 primary techniques、三层 runtime、design choices、user stories 与 success criteria；同时检查当前仓库说明以识别术语演化，未把后续 release 能力写成 2025 已实现事实。
- **Original Problem:** 单一 engine 或 Kubernetes Service 只掌握局部执行/endpoint 状态，无法同时利用 prefix locality、prefill/decode 分工、硬件差异、queue pressure 与 fleet lifecycle。
- **Why the Previous Design Was Reasonable:** 单副本、共享无状态 replica 与 round-robin 在模型较小、请求短、cache reuse 弱且副本近似同质时简单、可恢复、易运维。
- **Changed Constraint:** 大模型、长 prompt、shared-prefix、PD 分离和多硬件 pool 使 request placement 影响 TTFT、tail latency、cache reuse 与 accelerator efficiency。
- **Mechanism:** founding proposal 把系统拆为 inference scheduler、vLLM data plane 与 remote prefix cache，并把 tiered prefix cache、disaggregated serving、LLM-aware load balancing、autoscaling 作为四条独立但可组合的 scale path；scheduler-directed RPC 在 latency/throughput 间选择，而非把所有逻辑塞进 engine。
- **State Ownership:** engine 拥有 token execution 与本地 KV；scheduler 拥有 routing/flow-control decision；remote cache 层拥有可跨 replica 扩展的 prefix state。proposal 特别区分 replica-local in-memory cache 与 durable/disaggregated cache，避免把 replica 无意变成唯一事实 owner。
- **Control Flow / Data Flow:** request 经 Inference Gateway/selector 进入 scheduler，scheduler 根据 workload 与 cache/queue signal 选择 replica 或 prefill/decode path；KV data 通过 engine/NIXL path 转移，metadata/routing signal 与 tensor data path 分离。
- **Implementation Details:** vLLM 提供 point-to-point disaggregated serving；NIXL 抽象 KV transfer；Kubernetes API 表达 pool/workload；upstream-first 与可替换 component 是设计选择。proposal 不是 production conformance specification。
- **Evaluation Setup:** 首发 proposal 只定义 scale、perf/$ at target latency 与 operational toil 等 success criteria；没有一个绑定 model、hardware、length、concurrency、precision 与 SLO 的统一结果集。
- **Baselines / Ablations / Sensitivity:** Not Disclosed at launch。首发材料没有给出完整 round-robin、monolithic runtime 与各组件消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Disclosed as a complete workload contract；因此不保留首发性能外推。
- **What the Evidence Actually Proves:** 证明 llm-d 的长期设计意图是模块化 distributed inference stack，并明确 ownership 分层与四类扩展机制。
- **What It Does Not Prove:** 不证明所有路径在 2025-05 已 production-ready，不证明任一组件组合对所有模型/硬件优于单体 runtime，也不证明 current repository 行为等同首发状态。
- **Limitations / Threats to Validity:** launch material 带项目愿景性质；component 快速演进会造成术语与 API drift；缺少首发 commit-pinned、端到端 workload contract。
- **Trade-offs / New Failure Modes:** 模块化换来替换性，却新增版本矩阵、metric freshness、cross-layer tracing、KV ownership/invalidation、partial failure、policy conflict 与升级顺序。
- **Where the Previous Design Still Applies:** 小模型、弱 prefix reuse、低并发或单 pool 场景仍可用单 engine/简单 load balancing，避免 control-plane tax。
- **Evolution Relationship:** `Direct Evolution`：single-engine optimization → fleet-aware routing/cache/PD composition；不是 vLLM、KServe 或 Gateway 的替代品。
- **ROADMAP Node:** Ch48、Ch49、Ch51、Ch52、Ch57、Ch58。
- **Stable Owner:** `INFER-DYNAMO` with `INFER-KSERVE-TOPOLOGY`, `INFER-SCHEDULING` and `PLATFORM-GATEWAY` handoffs。
- **Target and Adjacent Chapters Read:** 已阅读 Ch47～52 与 Ch57～59；Ch48 拥有 distributed runtime，Ch58 拥有 gateway/EPP boundary，Ch49/57 拥有 KServe topology/control-plane boundary。
- **Existing Coverage:** 现有 Ch48 已解释 request/control/state path、KV-aware routing 与 disaggregation；Ch58 已解释 Gateway–EPP–engine scheduler 分工，但尚需在 Books Gate 与 KServe/Gateway 候选联审后确认是否缺少“local cache 与 durable cache ownership 分离”这一演进节点。
- **Integration Decision:** `No Change — Already Covered`；Ch48/49 已区分 engine data plane、distributed runtime 与 Kubernetes control plane。
- **Changed Files or Rejection Reason:** 不改 Books；source family 用于确认分层，不重复 release architecture。
- **Open Questions:** 能否找到 2025-05 精确 commit/tag 以冻结 component/API matrix；首发四条 path 分别在哪个 release 达到可重复 workload contract。

### Claude 4

- **Candidate / Week / Score:** Claude 4 / 2025-W21 / 22/30。
- **Source Family ID:** `ANTHROPIC-CLAUDE4-2025-05`。
- **Source Type:** 官方 announcement + 124 页 system card。
- **First-public Date / Revision History:** 2025-05-22；system card 后于 2025-07-16 做脚注/格式修订，并于 2025-09-02 修正 Claude Code Impossible Tasks 数字，故当前 PDF 的被修正数字不冒充发布日原值。
- **Direct Primary Sources:** Claude 4 announcement；Claude Opus 4 & Sonnet 4 System Card（May 2025，含 changelog）。
- **Related Primary Sources:** Anthropic extended-thinking/tool-use API 文档仅用于产品 contract；第三方 customer quotes 不作为机制证据。
- **Access and Verification Status:** Verified。announcement 与完整 system card 可访问；model architecture、post-training objective、tool-policy training 与 memory implementation 未披露。
- **Full-read Coverage:** 已覆盖 system card 的 model/training characteristics、release process、safeguards、agentic safety、alignment assessment、model welfare、RSP capability assessments、cyber/CBRN 与附录；announcement 的 benchmark methodology、extended thinking with tools、parallel tools、file-backed memory 与 API contract 已联读。
- **Original Problem:** 长时 coding/agent task 需要在多步 reasoning 中获取外部 observation，并在 context 之外保存可恢复状态；仅靠一次 completion 或不可审计 hidden reasoning 无法提供 durable continuity。
- **Why the Previous Design Was Reasonable:** 对短任务，单次 context 内 reasoning 与串行 tool call 更简单，也减少文件写入、权限和 stale state 风险。
- **Changed Constraint:** task horizon 延长到多工具、多文件与多小时执行，单 context 的容量、恢复和 provenance 边界暴露。
- **Mechanism:** 官方只公开产品行为：extended thinking 可与 tool use 交替、tools 可并行、developer 提供本地文件访问时模型可创建/维护 memory files；thinking summary 由较小模型压缩。内部 routing、training 与 write policy 未披露。
- **State Ownership:** 模型生成 tool/file proposals；host application/Claude Code 与文件系统拥有执行和持久状态。system card 没有证明模型本身拥有 durable memory subsystem。
- **Control Flow / Data Flow:** model reasoning → tool proposal → host execution → observation 返回 reasoning；file-backed memory 是显式 artifact path，不是参数更新。并行 tool 的 join、conflict 与 retry contract 未在 release 中完整公开。
- **Implementation Details:** 两个模型均为 hybrid reasoning modes；官方披露训练数据类别、截止时间、过滤与 release safety levels，但架构、参数量、optimizer、tool-training recipe 为 Not Disclosed。
- **Evaluation Setup:** announcement 的 SWE-bench 使用 bash/file-edit scaffold；high-compute variant 包含 parallel attempts、visible-test rejection 与 internal scorer；TAU-bench 将 step cap 从 30 提至 100。system card 评估覆盖 computer use、agentic coding、prompt injection、reward hacking 与 capability thresholds。
- **Baselines / Ablations / Sensitivity:** 有 model/snapshot 与 scaffold comparison，但没有把 model、harness、tool access、parallel sampling 各自贡献完整消融；后续 system-card 数字还发生修订。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API context/pricing 与部分 reasoning budget有披露；训练硬件、precision、batch、production concurrency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明公开 product contract 支持 reasoning–tool interleave、parallel tool proposals 与 host-provided file state；也证明 agent benchmark 结论强依赖 scaffold、step budget 与 selection method。
- **What It Does Not Prove:** 不证明“模型具有长期记忆”这一内部机制，不证明数小时 autonomous claim 可脱离 harness/权限成立，不证明 benchmark gain 来自某个已公开 training mechanism。
- **Limitations / Threats to Validity:** vendor-run evaluations、snapshot drift、system-card number corrections、rare-scenario elicitation 与 classifier-based analysis限制外推；system card 自身多次强调评估集不能覆盖所有 attacks。
- **Trade-offs / New Failure Modes:** tool/reasoning interleave提高适应性，却增加 prompt injection、observation poisoning、parallel side-effect conflict、budget exhaustion 与 audit burden；file memory增加 continuity，也新增 provenance、staleness、authorization、deletion 与 poisoning。
- **Where the Previous Design Still Applies:** 短、低风险、可一次验证的任务仍应优先无持久 memory、少工具与 deterministic workflow。
- **Evolution Relationship:** `Layering / Dependency`：model capability 只能在 host tool/workflow/memory contracts 上交付，不是 Workflow runtime 的替代。
- **ROADMAP Node:** Ch52、Ch62、Ch73～77。
- **Stable Owner:** `AGENT-TOOL-CALLING` with `AGENT-WORKFLOW` handoff。
- **Target and Adjacent Chapters Read:** 已阅读 Ch52、Ch62、Ch72～77；Memory、Tool Calling 与 Workflow 已明确 host/runtime ownership。
- **Existing Coverage:** Ch73 已区分 context 与 durable memory，Ch74 已写“模型输出只是 proposal”，Ch77 已写 deterministic spine。公开材料主要是 product/version evidence，暂未发现可独立沉淀的新内部机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；model、harness 与 platform attribution 已由 Ch62/74～77 覆盖。
- **Open Questions:** Anthropic 是否公开过 file-memory write/retention policy、parallel tool conflict contract 与可复现 agent harness artifact。

### User-level differential privacy for LLM fine-tuning

- **Candidate / Week / Score:** User-level differential privacy for LLM fine-tuning / 2025-W21 / 23/30。
- **Source Family ID:** `GOOGLE-ULDP-2407.07737`。
- **Source Type:** 2024 primary research paper + 2025 Google Research follow-up。
- **First-public Date / Revision History:** 论文 arXiv v1 首发 2024-07-10；Google Research 于 2025-05-23 再解释该工作。此前将 2025 Blog 日期写成技术 first-public date 不准确，本次已纠正。
- **Direct Primary Sources:** arXiv:2407.07737 全文；Google Research 2025 follow-up；论文公开 accounting/software references。
- **Related Primary Sources:** 并行工作 arXiv:2406.14322 用于 related-work 边界，不混并实验结论。
- **Access and Verification Status:** Verified。论文 HTML、公式、appendices 与实验 setup 可访问；真实部署 attack audit 与非英语/多模态数据未覆盖。
- **Full-read Coverage:** 已阅读 metadata、Introduction、ELS/ULS algorithms、tight accounting、variance analysis、synthetic mean estimation、LM setup/results、related work、discussion、privacy-attack说明及 A–G appendices（accounting implementation、datasets、group-size heuristic、sensitivity/personalization）。
- **Original Problem:** record-level adjacency只限制一条 example 的影响；用户贡献多条高度相关记录时，不能表达“移除一个用户全部数据”的保护语义。
- **Why the Previous Design Was Reasonable:** example-level sampling/clipping易于向量化，且在用户贡献少、样本近似独立或 privacy target 本来就是 record 时，计算更直接。
- **Changed Constraint:** assistant/chat/email 等数据天然按 user 聚集、贡献数不均且存在 within-user correlation；同时 LLM fine-tuning 受固定 accelerator budget 限制。
- **Mechanism:** ELS 从每用户最多 `G_ELS` 条记录组成 pooled dataset，做 example sampling/clipping，再通过 tight accountant提升到 user-level guarantee；ULS 先采样用户，对每个用户最多 `G_ULS` 条 example gradient 求平均，再做 per-user clipping/noise。选择 `(G_ULS, cohort M)` 本身是 compute–noise trade-off。
- **State Ownership:** privacy ledger/accountant 属于 training control plane；user grouping与contribution bounds属于dataset governance；optimizer只消费已经裁剪/加噪的aggregate，不能自行推断用户身份。
- **Control Flow / Data Flow:** user-partitioned dataset → user/example sampling → bounded group contribution → per-example or per-user gradient → clipping → Gaussian noise → optimizer；privacy parameters与sampling schedule共同进入accounting。
- **Implementation Details:** model 用 Praxis，ELS 用 JAX/tf.data，ULS 用 Dataset Grouper + FAX并行化，实验运行于 PAX；论文给出 dp_accounting 实现与 Estimate-and-Double heuristic。
- **Evaluation Setup:** C4-minus 预训练 400k steps、batch 512；Stack Overflow fine-tune 10k steps、CC-News 2k steps；TPU v3 `4x4/8x8/16x16` slices；Stack Overflow 与按 base-domain 分组的 CC-News；`delta=n^-1.1`，多组 epsilon/compute budgets。
- **Baselines / Ablations / Sensitivity:** 比较 ELS、ULS 与 no fine-tuning；扫描 group/cohort size、epsilon、compute budget、用户数 accounting 假设，并有 personalization 与 heuristic validation。没有真实 production attack benchmark。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TPU topology、预训练 batch 与 steps披露；模型规模/precision/sequence length/online concurrency/SLO未完整披露，因此 utility 结论不外推到任意 LLM。
- **What the Evidence Actually Proves:** 在论文的两个 user-partitioned text dataset 与固定 compute budget 下，ULS在强 privacy、较大 compute 或 within-user gradient diversity较高时通常优于ELS；tight accountant让ELS/ULS可公平比较。
- **What It Does Not Prove:** 不证明ULS总优于ELS，不证明形式DP自动抵抗所有实现/side-channel攻击，也不证明domain-based CC-News grouping等于真实用户。
- **Limitations / Threats to Validity:** CC-News用domain代理user且accounting假设用户数可放大10倍；仅两个text datasets；模型/序列细节不全；shuffle实现与理论subsampling存在implementation boundary；hyperparameter tuning影响utility。
- **Trade-offs / New Failure Modes:** user-level语义更强，却要求可靠identity/grouping、贡献上限、per-user compute sharding与ledger composition；共享账号、设备迁移、跨产品identity会让adjacency错误。
- **Where the Previous Design Still Applies:** record-level threat model、单记录用户、用户边界不可信或compute极紧时，ELS仍可能更合适；论文也明确存在ELS胜出的设置。
- **Evolution Relationship:** `Direct Evolution`：record privacy unit → user privacy unit；与 inference-time privacy filter 是 `Layering / Dependency`，两者不替代。
- **ROADMAP Node:** Ch25、Ch62、Ch68。
- **Stable Owner:** `PLATFORM-SECURITY`。
- **Target and Adjacent Chapters Read:** 已阅读 Ch25、Ch62、Ch67～69；Ch68 当前已有 privacy unit、grouping、clipping/noise/accounting 与 composition 论证。
- **Existing Coverage:** Ch68 已准确吸收“先定义 privacy unit 再选机制”及 user grouping/ledger 边界；最终复核未把单篇实验中的 `G` 与 cohort `M` 写成通用配方。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，明确 user adjacency、clipping、accounting 与 utility。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/68-security.md`。
- **Open Questions:** 项目平台怎样定义跨workspace/shared-account adjacency；privacy ledger如何与data deletion、retraining和跨run composition对齐。

### 4. AdaptThink — 24/30

`ADAPTTHINK-2025`; arXiv paper + artifact, W21 v1; method/eval/appendix verified. Uniform long reasoning was reasonable when difficulty unknown; wasted tokens and easy/hard heterogeneity motivate learned difficulty-aware routing. Policy owns continue/stop; reward pipeline owns correctness/length shaping; serving enforces cap. Qwen/math author experiments and ablations show a Pareto shift under supplied prompts, not calibrated difficulty or domain-general savings; hardware/precision/concurrency/SLO incomplete. Premature stopping and reward gaming are new failures; fixed budgets remain safer under predictable tasks. Owner `TRAIN-RLHF` with `INFER-SCHEDULING` handoff; adjacent chapters checked; `Emerging / Experimental`; open: out-of-domain calibration.

### 5. BRPO / AnytimeReasoner — 24/30

`BRPO-2505.13438`; paper/code; v1 2025-05-20; full read. Fixed-budget policies were simple but cannot expose a quality–cost curve. Training samples budgets and optimizes budget-relative outcomes; trainer owns rollout/budget distribution, serving chooses a budget. Setup discloses DeepSeek-R1-Distill-Qwen-1.5B, 40,315 math prompts, group 8, 2k–8k budgets, 8×A100-80GB, ~30h, four summaries/budget and <10% reported overhead. This proves author math Pareto results, not arbitrary-domain anytime optimality. Failures: train/serve budget mismatch, summary overhead and low-budget collapse. Owner `TRAIN-RLHF` with inference handoff; `Emerging`; open: dynamic SLO policy.

### 7. Efficient Agent Training for Computer Use — 27/30

`EAT-COMPUTER-USE-2025`; paper, environment and code; W21 v1; method, implementation, eval, ablations and appendices read. Offline imitation is reasonable when actions are stable, but UI outcomes are interactive and error compounding changes the constraint. Environment-grounded RL uses executable feedback; runtime owns UI state and side effects, trainer owns rollouts/rewards/checkpoints, model proposes actions. Author computer-use harness proves gains under that opportunity set, not deployment autonomy; model/harness/evaluator attribution is not fully isolated and UI nondeterminism threatens validity. Costs live-environment expense, contamination and unsafe actions. Owner `AGENT-WORKFLOW` + `TRAIN-RLHF`; adjacent tool/eval chapters checked; `Integrate candidate`; open: deterministic replay and safety envelope.

### 8. Visual ARFT — 24/30

`VISUAL-ARFT-2025`; arXiv paper/artifact, W21; full method/eval/appendix read. Text-only outcome rewards miss visual grounding; verifiable visual rewards and RL add grounded checks. Environment/evaluator owns evidence and reward, policy owns proposals. Selected VLM tasks/models show author gains but do not establish general grounding; precision, end-to-end latency and deployment SLO incomplete. Verifier shortcuts and synthetic-answer bias remain. Owner `TRAIN-RLHF` with `MULTIMODAL-REPRESENTATION`/evaluation handoffs; `Emerging`; open: adversarial verifier audit.

### 9. Scaling Law for QAT — 29/30

`QAT-SCALING-2025`; paper/artifact, W21; derivation, scaling experiments and appendices read. Per-model QAT sweeps were reasonable at small scale but expensive at frontier scale. The work models quantization error/scaling to transfer settings; training owns fake-quant/calibration state and serving owns deployed representation/kernel. Results support studied architectures/bitwidths and disclosed training conditions, not every model/hardware; deployment latency/concurrency/SLO is separate. New failures are proxy-law misspecification, calibration drift and kernel mismatch; local tuning remains appropriate off-distribution. Owner `INFER-TENSORRT-LLM` with training handoff; `Integrate candidate`; open: independent hardware replication.

### 10. Vid2World — 28/30

`VID2WORLD-2025`; paper/project/artifact, W21; full method, implementation, eval, ablations, appendices. Video continuation is reasonable for appearance modeling but actions demand controlled transitions. Action-conditioned token/state prediction couples observation and action; environment model owns latent state/action schema, planner consumes rollouts, Agent memory does not own world truth. Text-game/web/robot/video experiments prove utility in supplied simulators, not causal fidelity/open-world safety; hardware/precision/SLO not fully comparable. Failure is plausible imagery with wrong dynamics and compounding imagined error. Owner `MULTIMODAL-WORLD-MODELS`; adjacent generative/embodied chapters checked; `Integrate candidate`; open: persistent-state correction.

### 11. Reasoning Models Better Express Confidence — 26/30

`REASONING-CONFIDENCE-2025`; behavioral paper/data, W21; full methods, calibration analyses and appendices read. Token probability is easy but conflates linguistic choice with proposition confidence; explicit elicitation changes the observation channel. Model produces confidence statements, evaluator owns truth labels/calibration bins. Selected reasoning models/tasks show better expression under certain protocols, not self-knowledge, factual correctness or deployment calibration; sampling/prompt/judge choices matter. Risks confident systematic error and over-trust; external evidence remains required. Owner `PLATFORM-EVALUATION-SYSTEM`; adjacent hallucination/evidence chapters checked; `Refine candidate`; open: selective prediction operating points.

### 12. Quartet — 29/30

`QUARTET-2505.14669`; paper/artifact, v1 2025-05-20; full systems/eval/ablation read. Monolithic KV placement was simple on one engine, but long-context/fleet workloads expose tiering and transfer cost. Quartet decomposes KV/state paths into workload-aware tiers; runtime owns request/model/position identity and migration, scheduler owns placement. Author model/hardware/length tests prove conditional speed/memory gains, not universal scheduling; precision/concurrency/SLO only as disclosed in paper. New failures: migration tail, stale identity, tier imbalance. Local KV remains best under high locality and no pressure. Owner `INFER-KV-CACHE`; adjacent paging/distributed chapters checked; W22 spillback corrected; `Integrate candidate`; open: failure recovery semantics.

### 13. Reward Reasoning Model — 24/30

`REWARD-REASONING-MODEL-2025`; paper/code, W21; full training/eval/ablation read. Scalar opaque rewards are cheap but hard to audit. The judge generates structured evaluative reasoning before a score; judge owns rubric/evidence state, trainer consumes a versioned score. Selected judge benchmarks show author gains, not faithfulness or unbiased reward; no proof rationale causally produced the score. Costs tokens, latency, bias and self-justifying explanations. Scalar rule verifiers remain better where outcomes are executable. Owner `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: rationale intervention tests.

### 14. BAGEL — 28/30

`BAGEL-2025`; model report, code/model card; W21 v1; architecture/data/eval/appendices read. Separate modality stacks were reasonable for isolated tasks but fragment representation and cross-modal generation. BAGEL uses shared sequence modeling with modality encoders/decoders; model owns token representation, training owns mixture, serving owns modality batching. Broad vendor/author benchmarks show feasibility, not a universally optimal shared space; data mixture/hardware/production SLO remain partially disclosed. Cross-modal interference and mixed-workload tail are new failures. Owner `MULTIMODAL-REPRESENTATION`; adjacent generation/training chapters checked; `Integrate candidate`; open: representation identity/provenance.

### 15. MMaDA — 28/30

`MMADA-2025`; paper/code/model, W21; full masked-diffusion method, decoding, eval, ablations, appendix. Left-to-right AR is natural for text and caching but limits parallel revision across modalities. MMaDA maintains a mutable mask/confidence set and commits subsets per denoise step; model owns representation, decoder owns mutable generation state. Author benchmarks show competitive/gain cases, not diffusion replacing AR; latency depends on steps, block size and kernels, and hardware/concurrency/SLO are not universal. Failures: confidence misordering, iterative overhead and cache incompatibility. Owner `MULTIMODAL-GENERATIVE-PARADIGMS`; `Integrate candidate`; open: exactness/rollback contract.

### 16. Web-Shepherd — 29/30

`WEB-SHEPHERD-2025`; paper, benchmark, code; W21; full process-reward/harness/eval/appendix read. Final-answer rewards are cheap but cannot localize invalid browser actions. Web-Shepherd grounds process scoring in browser state and action validity; environment owns state, judge owns rubric/evidence, policy owns proposals. Tests prove improvements in supplied web harness, not model-only ability or open-web robustness; opportunity, evaluator and UI drift confound attribution. Costs benchmark maintenance and judge bias. Owner `AGENT-WORKFLOW` + `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: frozen replay corpus.

### 17. dKV-Cache — 29/30

`DKV-CACHE-2025`; systems paper/artifact, W21; full design, implementation, workload and ablations read. Engine-local KV is simplest until prefix reuse and PD/fleet movement make locality global. dKV externalizes/distributes KV with explicit request/model/token-position identity and transfer protocol; engine owns execution view, cache service owns durable/tiered bytes, scheduler owns placement. Reported gains bind model, hardware, length, batch/concurrency and paper SLO; not universal. Failures: transfer tails, invalidation, partial writes, stale metadata. Owner `INFER-KV-CACHE`; adjacent distributed runtime checked; `Integrate candidate`; open: ownership during retry.

### 18. QuickVideo — 29/30

`QUICKVIDEO-2025`; paper/code, W21; full video diffusion execution, cache/reuse, eval and ablations read. Dense full-resolution every denoise step was straightforward but wastes work. The pipeline reuses/reduces temporal-spatial computation while scheduler tracks denoise-step state and cache validity. Author speedups are bound to listed video models, GPUs, resolution/steps and quality metrics; they do not prove perceptual equivalence or online SLO. New failures are stale reuse and metric-blind artifacts; baseline remains safer for exact quality. Owner `MULTIMODAL-GENERATIVE-PARADIGMS` with `INFER-TENSORRT-LLM` handoff; `Integrate candidate`; open: concurrency/tail measurements.

### 19. QwenLong-L1 — 30/30

`QWENLONG-L1-2505.17667`; paper/code/model; v1 2025-05-23; full curriculum/RL/eval/appendix/artifact read. Long-context SFT was reasonable but lacks exploration and difficulty progression. Progressive curriculum plus outcome-verifiable RL makes trainer own difficulty/rollout/policy-version state; runtime only supplies long context. Tests show gains on disclosed long-context reasoning benchmarks, not unlimited extrapolation, factuality or serving efficiency; long rollout hardware/precision details are paper-bound. Costs extreme rollout memory, verifier brittleness and curriculum overfit. Owner `TRAIN-RLHF` + `MODEL-LONG-CONTEXT`; W22 spillback corrected; `Integrate candidate`; open: retrieval vs weight-memory attribution.

### 20. TabSTAR — 25/30

`TABSTAR-2505.18125`; paper/code, v1 2025-05-23; full data serialization/pretraining/eval/ablation read. Per-table feature engineering remains strong and simple for stable schemas; many heterogeneous tables motivate transferable schema-aware representation. Data pipeline owns column/type/label identity and leakage controls; model consumes serialized schema/values. Cross-dataset tests show transfer in selected tabular corpora, not replacement of GBDT or robustness to schema drift. Costs tokenization overhead, leakage and numeric precision. Owner `TRAIN-DATA`; W22 spillback corrected; `Emerging`; open: time-split and leakage audit.

### 21. Embodied MEMENTO — 27/30

`MEMENTO-2505.16348`; paper/project, v1 2025-05-22; full personalization memory method/eval/appendix read. Stateless embodied policies are safer/simple but cannot adapt to recurring users. Explicit user/episode memory is retrieved into policy decisions; environment/user profile owns provenance and deletion, runtime owns retrieval, model proposes action. Benchmark gains do not prove safe real-world personalization, correct user identity or physical reliability. New failures: stale/private preferences, unsafe transfer and memory poisoning. Owner `AGENT-MEMORY` + `MULTIMODAL-EMBODIED-VLA`; W22 spillback corrected; `Integrate candidate`; open: supersession/consent.

### 22. PATS — 24/30

`PATS-2505.19250`; paper/artifact, v1 2025-05-25; full method/eval/ablation read. Frozen policies are predictable but cannot exploit task-time feedback. PATS introduces bounded test-time adaptation/search; runtime owns temporary adaptation state, evaluator supplies feedback, deployment owns rollback. Author tasks show conditional gains, not stable continual learning or safe production mutation; hardware/latency/SLO incomplete. Risks contamination, drift, latency and irreproducibility; frozen policy remains preferable under strict audit. Owner `AGENT-PLANNING`; W22 spillback corrected; `Emerging`; open: transactional rollback.


### 23. Flex-Judge — 26/30

`FLEX-JUDGE-2505.18601`; paper/artifact, v1 2025-05-24; full text-supervision, transfer, multimodal eval and limitations read. Modality-specific judges need costly labels; structured textual reasoning supervision transfers decision patterns to image/video/molecule judgment. Judge owns rubric/evidence; trainer owns text data; downstream evaluation must calibrate each domain. Competitive author results with fewer labels do not prove unbiased, faithful or domain-valid evaluation, especially molecule tasks with sparse benchmarks; hardware/latency/SLO incomplete. Costs longer inference and reasoning-style bias. Owner `PLATFORM-EVALUATION-SYSTEM`; W22 spillback corrected; `Integrate candidate`; open: human operating-point calibration.

### 24. VerIPO — 24/30

`VERIPO-2505.19000`; paper/code, v1 2025-05-25; full optimization, verifier, experiments and appendix read. Static preference data is simple but goes stale against an improving policy. Verifier-informed policy optimization couples generation and checking while trainer owns versioned policy/verifier snapshots and rollout provenance. Author reasoning benchmarks show gains under their verifier; not proof verifier correctness or general alignment. Risks verifier hacking, stale scores and feedback loops; fixed rule verifiers remain better where possible. Owner `TRAIN-RLHF`; W22 spillback corrected; `Emerging`; open: off-policy correction and adversarial verifier tests.

### 25. Data-centric compression — 25/30

`DATA-CENTRIC-COMPRESSION-2505.19147`; position paper, v1 2025-05-25; full argument/taxonomy/examples read. Codec-centric comparison is reasonable for fixed workloads but hides data distribution, task and evaluation drift. The paper makes dataset/task/evidence contract a first-class compression input; it proposes a research frame, not an implemented universal algorithm. It proves conceptual coverage only, not benchmark superiority; no hardware/model/precision/length/concurrency/SLO result exists to generalize. Costs governance and multi-objective evaluation complexity. Owner `TRAIN-DATA` with execution handoff; W22 spillback corrected; `Refine candidate`, explicitly position evidence; open: executable data-quality contract.

### 26. DeepResearchGym — 29/30

`DEEPRESEARCHGYM-2505.19253`; paper, API docs and site, v1 2025-05-25; full retrieval/evaluation/human-study/artifact read. Commercial live search is useful but unreproducible and costly. The gym fixes ClueWeb22/FineWeb corpora, dense retrieval + DiskANN rankings and a Researchy Questions extension; environment owns corpus/index snapshot, judge owns needs/faithfulness/report-quality rubric. Author studies show comparable performance/rankings and judge–human alignment, not real-web freshness or perfect judgment. Costs corpus staleness and LLM-judge dependence. Owner `PLATFORM-EVALUATION-SYSTEM` + `AGENT-WORKFLOW`; W22 spillback corrected; `Integrate candidate`; open: corpus/version retention.

### 27. NLWeb — 27/30

`MICROSOFT-NLWEB-2025-05`; official announcement, schema/spec and repo, first public 2025-05-19; verified across design docs. Sites already publish structured content but conversational agents need a common query/action surface. NLWeb maps Schema.org/RSS/JSONL into retrieval and conversational endpoints/MCP; publisher owns source content/provenance, host owns retrieval/execution, model emits responses/proposals. It proves an open interface and implementation direction, not universal retrieval quality, security or production maturity; no stable workload benchmark. Risks stale indexing, prompt injection and ambiguous authority. Owner `AGENT-RAG` with `AGENT-MCP` handoff; adjacent context/tool chapters checked; `Integrate candidate`; open: authorization and provenance enforcement.

### 28. Anthropic API code execution / MCP connector / Files — 22/30

`ANTHROPIC-API-2025-05-22`; official API/product docs, first public 2025-05-22; verified interface, internal mechanisms undisclosed. Direct model text was reasonable for bounded tasks; agent workloads need sandboxed compute, remote connectors and durable artifacts. Host/API owns sandbox, credentials/files and side effects; model proposes calls. Evidence proves public product contracts only; no internal training mechanism or complete workload/hardware/concurrency/SLO benchmark is disclosed. Risks connector trust, artifact leakage and confused deputy; direct calls remain safer for small tasks. Owner `AGENT-TOOL-CALLING`; `Weekly Only — Version Fact`; open: sandbox isolation and retention details.

### 29. Anthropic ASL-3 safeguards — 27/30

`ANTHROPIC-ASL3-2025-05`; official RSP/safeguards report, 2025-05-22; control taxonomy and threat assumptions read. Capability-only evaluation cannot constrain access after a provisional CBRN threshold. The declared system layers classifiers, monitoring, restricted access, egress controls, bounty and two-person authorization; governance owns threshold/release decision, security plane owns enforcement, model is only one component. It proves declared controls, not zero residual risk or independent efficacy. Missing operating-point details constrain inference. Costs false positives, operational burden and bypass composition. Owner `PLATFORM-SECURITY/GOVERNANCE`; `Integrate candidate` as bounded case; open: auditable control efficacy.

### 30. Agent Distillation — 26/30

`AGENT-DISTILLATION-2025`; paper/artifact, W21; full trajectory distillation, task setup, baselines and appendix read. Calling a large teacher each step is flexible but expensive; distilled trajectories/skills train a smaller policy. Environment owns executable ground truth, teacher owns demonstrations, student owns learned policy, runtime owns action validation. Author harness proves transfer in selected interactive tasks, not general autonomy or safety. Risks teacher-error amplification, schema mismatch and compounding action errors; teacher-at-runtime remains useful for long-tail tasks. Owner `AGENT-WORKFLOW` + `TRAIN-SFT`; `Integrate candidate`; open: provenance and failure-aware filtering.

### 31. Scaling Reasoning, Losing Control — 26/30

`SCALING-REASONING-CONTROL-2025`; paper/data, W21; full experimental protocols, model comparisons and appendices read. More test-time reasoning is reasonable for hard problems but changes refusal/compliance/control behavior. The study separately measures task ability and controllability across reasoning budgets; evaluator owns policy labels and model owns generated trajectory. Results establish model/benchmark-specific trade-offs, not a monotonic law. Harness, prompt and sampling choices limit validity; hardware/SLO irrelevant or undisclosed. Risks capability gain with weaker steering. Owner `PLATFORM-EVALUATION/GOVERNANCE`; `Refine candidate`; open: deployment-time selective budget gates.

### 32. BanditSpec — 29/30

`BANDITSPEC-2025`; paper/code, W21; full algorithm, regret/selection, implementation, evaluations and ablations read. Static speculative draft choice is simple under stable acceptance but poor when workload/model pairs vary. Online bandit selection tracks candidate acceptance/cost; target model retains commit authority, scheduler owns statistics/exploration. Reported throughput/latency binds exact model pairs, hardware, lengths and concurrency; not universal. Risks exploration regret, stale stats and tail variance; static choice remains best in stable loads. Owner `INFER-SPECULATIVE-DECODING`; `Integrate candidate`; open: nonstationary reset and SLO-aware objective.

### 33. VerifyBench — 26/30

`VERIFYBENCH-2025`; paper/dataset/artifact, W21; taxonomy, construction, evaluation and appendices read. Outcome accuracy conflates solving and checking; explicit verification tasks isolate error detection. Dataset owns labels, evaluator owns rubric, model produces verdict/evidence. Results measure selected verifier tasks/models, not real-world truth or faithful rationales; contamination/judge choices are threats. Costs another evaluation layer and uncertain operating point. Owner `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: executable verifier subset and calibration.

### 34. WebAgent-R1 — 29/30

`WEBAGENT-R1-2025`; paper/code/environment, W21; full online RL, action schema, eval, ablations and artifact read. Offline web imitation was easy but mismatches interactive state. Online rollouts use environment feedback/executable success; browser owns state, trainer owns rollouts/rewards, policy proposes actions. Author benchmarks show system gains, not model-only ability or open-web reliability; harness opportunity and UI drift confound attribution. Risks unsafe side effects, nondeterminism and reward exploitation. Owner `AGENT-WORKFLOW`; `Integrate candidate`; open: sandboxed deterministic replay.

### 35. OneRL — 23/30, disputed

`ONERL-2025`; accessible arXiv versions and code read; W21 v1 identity retained but current title/version lineage differs. A unified RL recipe is proposed across reasoning settings, with trainer owning rollout, reward and policy version. Experiments support selected model/task cases, not a universal recipe; event-time numeric claims cannot be reused until v1 PDF is pinned. Risks hidden recipe changes, verifier dependence and instability. Owner `TRAIN-RLHF`; adjacent PPO/GRPO branches checked; `Disputed` rather than silent reuse; missing material: event-time v1 PDF/metadata export.

### 36. PhyX — 22/30

`PHYX-2025`; paper/dataset/code, W21; full benchmark construction, evaluators, baselines and limitations read. Answer matching is inadequate for physics processes; PhyX adds structured/executable physics reasoning checks. Dataset/simulator owns state and labels, evaluator owns verdict. Author results expose current-model gaps, not general physical competence or simulator fidelity. Domain coverage and generated items limit validity; hardware/SLO not material. Owner `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: real-measurement validation.

### 37. QwenLong-CPRS — 26/30

`QWENLONG-CPRS-2025`; paper/artifact, W21; full progressive training/reward/eval read. Static long-context tuning under-samples difficulty transitions. Curriculum/progressive reward schedules assign trainer ownership of stage, context length and rollout versions. Disclosed long-context tasks show gains, not arbitrary extrapolation or online serving benefit; model/hardware conditions are paper-specific. Risks curriculum overfit and reward shortcuts. Owner `TRAIN-RLHF` + `MODEL-LONG-CONTEXT`; `Integrate candidate`; open: retrieval-controlled ablation.

### 38. EvoSearch — 22/30

`EVOSEARCH-2025`; paper/code, W21; search algorithm, archive/evaluator, experiments and appendix read. Single-pass proposal is cheap but weak for open-ended discovery. Iterative mutation/selection keeps an explicit candidate archive; planner owns search control, evaluator owns score/evidence, artifact store owns lineage. Selected search tasks show improvement, not scientific novelty or judge correctness. Costs many calls and convergent judge bias. Owner `AGENT-PLANNING`; `Emerging`; open: diversity/provenance guarantees.

### 39. MOOSE-Chem3 — 22/30

`MOOSE-CHEM3-2025`; paper/code/data, W21; workflow, retrieval/evaluation and limitations read. Free-form chemistry ideation lacks evidence trace; the agent structures literature search, hypothesis and critique. Workflow store owns provenance, tools own retrieved evidence, model proposes hypotheses. Benchmarks/human ratings do not prove autonomous discovery or physical correctness; literature bias and evaluator expertise limit validity. Costs tool/citation failures and unsafe extrapolation. Owner `AGENT-WORKFLOW`; `Emerging`, domain case only; open: wet-lab verification contract.

### 40. VeriThinker — 24/30

`VERITHINKER-2025`; paper/code, W21; verifier-aware training/inference, baselines, ablations and appendix read. Unchecked long traces can amplify error. Separate verification scores guide revision/training; verifier owns judgment state, policy owns proposal, trainer owns coupling. Author math/reasoning gains do not prove faithful CoT or verifier correctness. Added cost and feedback hacking are key failures; direct rule verification remains preferable where available. Owner `TRAIN-RLHF` with evaluation handoff; `Emerging`; open: verifier intervention tests.

### 41. Direct3D-S2 — 23/30

`DIRECT3D-S2-2025`; paper/artifact, W21; representation, generation/reasoning pipeline, tests and appendix read. 2D proxies are convenient but lose 3D state/geometry. Direct spatial representation makes 3D state an explicit object used across stages; model owns latent representation, renderer/simulator owns physical realization. Selected synthetic/benchmark results show feasibility, not real geometry fidelity or physical safety. Costs memory, view inconsistency and representation drift. Owner `MULTIMODAL-REPRESENTATION`; `Emerging`; open: cross-view identity.

### 42. s3 — 26/30

`S3-2025`; paper/code, W21; efficient reasoning sampling/selection, eval, sensitivity and appendices read. One deterministic trace is cheap but leaves search headroom; indiscriminate self-consistency is costly. s3 allocates samples/tokens and selects using verified outcomes; serving owns budget, evaluator owns selection. Results are model/math-task-specific and not a generic SLO curve; hardware/concurrency details constrain cost claims. Risks correlated samples and evaluator bias. Owner `MODEL-SAMPLING` + `TRAIN-RLHF`; `Integrate candidate`; open: adaptive stopping calibration.

### 43. AudioTrust — 23/30

`AUDIOTRUST-2025`; paper/dataset, W21; threat taxonomy, data, models, evaluations and limitations read. Text-only safety evaluation misses audio perturbations/content. AudioTrust binds attacks and operating conditions to modality-specific tests; dataset owns labels/noise, evaluator owns policy taxonomy. It proves gaps for tested models/languages/noises, not universal audio robustness. Costs coverage maintenance and uncertain transfer. Owner `PLATFORM-EVALUATION/SECURITY`; `Emerging`; open: multilingual/streaming SLO.

### 45. Template-RL / TAPO — 23/30, disputed

`TEMPLATE-RL-TAPO-2025`; accessible versions/code read; event-time title/revision lineage unresolved. Typed templates/actions constrain free-form rollouts; workflow owns schema and validator, policy fills choices, trainer owns rewards. Author tasks indicate structured exploration benefits, not generality; event-time numbers frozen pending v1 PDF. Risks template blind spots and version drift. Owner `TRAIN-RLHF` + `AGENT-WORKFLOW`; `Disputed`; missing material: v1 PDF/metadata.

### 46. Trinity-RFT — 25/30

`TRINITY-RFT-2505.17826`; report/repo, v1 2025-05-23; full architecture, modes, implementation examples and limitations read. Separate one-off trainers fragment sync/async, online/offline and on/off-policy designs. Decoupled core makes policy/experience freshness explicit; trainer owns policy versions and backpressure, environment connector owns interactions, data pipeline owns trajectories. Examples demonstrate extensibility, not one mode’s superiority or production performance; no common model/hardware/SLO benchmark. Risks stale trajectories and complex failure recovery. Owner `TRAIN-DISTRIBUTED-TRAINING`; `Integrate candidate`; open: consistency contract.

### 47. Context Faithfulness — 23/30

`CONTEXT-FAITHFULNESS-2025`; paper/dataset, W21; construction, metrics, baselines and appendix read. Correct answers can ignore/contradict supplied evidence. The benchmark separates answer correctness from evidence use; dataset owns evidence, evaluator owns entailment/attribution labels. Selected tasks and LLM judges show measurable gaps, not real-world truth or causal use of context. Costs judge uncertainty and annotation ambiguity. Owner `PLATFORM-EVALUATION-SYSTEM`; `Refine candidate`; open: executable citation checks.

### 48. Interactive VLA — 24/30

`INTERACTIVE-VLA-2025`; paper/project, W21; full closed-loop architecture, action representation, experiments and limitations read. Open-loop VLM action sequences are simple but cannot correct state changes. The VLA alternates observation, action proposal, controller execution and new observation; environment/controller own physical state and safety, model owns proposal. Simulation/benchmark gains do not establish real-world safety, calibration or control-frequency SLO. Risks latency, compounding perception error and unsafe action chunks. Owner `MULTIMODAL-EMBODIED-VLA`; `Emerging`; open: hardware loop and override.

### 49. ReflAct — 23/30

`REFLACT-2025`; paper/code, W21; reflection/action state machine, eval and ablation read. Immediate action is efficient but lacks correction; free-form reflection may amplify errors. Runtime persists observation/action/revision state and validates effects; model proposes revisions. Harness gains do not prove reflection faithfulness or deployment robustness; extra turns raise latency/cost. Deterministic workflows remain better for known procedures. Owner `AGENT-REFLECTION/WORKFLOW`; `Refine candidate`; open: rollback and evidence-gated reflection.

### 50. NOVER — 23/30

`NOVER-2025`; paper/artifact, W21; novelty/verifier mechanism, evaluation and limitations read. Unconstrained search generates duplicates/unsupported claims. Explicit novelty/evidence scoring gates archive admission; archive owns identity, verifier owns evidence contract, planner owns search. Author tasks show better selection under their judge, not objective novelty or truth. Risks judge monoculture and false rejection. Owner `PLATFORM-EVALUATION-SYSTEM` with planning handoff; `Emerging`; open: independent human/executable checks.

### 51. Not All Models Suit Expert Offloading — 26/30

`MOE-LRC-2505.16056`; https://arxiv.org/abs/2505.16056; v1 2025-05-21; paper and reproduction artifact read. Static expert residency is fastest if memory fits; memory-constrained serving motivates offload, but cache benefit depends on local routing consistency rather than a universal prefetch assumption. The paper defines Segment Routing Best Performance and Segment Cache Best Hit Rate and analyzes 20 MoE LLMs; runtime owns expert identity/residency while the measurement harness owns segment/cache state. It supports an architecture-conditioned offload suitability diagnostic, not an implemented production offloader or universal speedup. New failures are treating oracle hit-rate bounds as realized performance and ignoring multi-tenant interference. Owner `MODEL-MOE`; `Refine candidate`; open: connect metrics to realized latency/energy under exact hardware.

### 52a. Keep Security! / CoPriva — 23/30

`KEEP-SECURITY-2505.15805`; https://arxiv.org/abs/2505.15805; v1 2025-05-21; benchmark construction, policy categories, direct/indirect attacks, ten-model evaluation and limitations read. Ordinary contextual QA is helpful by default, but enterprise contexts introduce non-disclosure policies that must override answerability. Context owner supplies policy and protected facts; evaluator owns leakage labels; model generates the answer but does not own authorization. Results show tested models often answer correctly while violating policy, especially under indirect attacks; they do not prove a complete prevention mechanism. Risks include policy ambiguity, benchmark-specific attacks and false assurance. Owner `PLATFORM-SECURITY`; `Refine candidate`; open: executable policy enforcement and calibrated blocking.

### 52b. FREESON — 23/30

`FREESON-2505.16409`; https://arxiv.org/abs/2505.16409; v1 2025-05-22; CT-MCTS algorithm, corpus graph/traversal, five QA evaluations and comparisons read. A separate dense retriever is efficient and modular, but its representation bottleneck can miss the generator's evolving information need. FREESON makes the reasoning model traverse a corpus with Corpus-Traversing MCTS; corpus nodes/edges and search tree are mutable state, while the final generator consumes the selected path. Author gains show the branch can match or exceed tested retriever-based systems on selected QA, not that learned retrieval is obsolete or evidence is automatically faithful. Costs are many model calls, traversal bias and hard-to-audit search. Owner `AGENT-RAG` with planning handoff; `Emerging`; open: corpus-scale latency, provenance and deterministic replay.


For every item below, metadata/v1/revision, Introduction/Related Work, complete Method/formulas/algorithm, Implementation, evaluation tables/ablations/sensitivity, limitations and consequential appendices/artifacts were read from the linked paper/repo. Hardware/model/precision/length/batch/concurrency/SLO fields not stated by authors are explicitly `Not Disclosed`, not inferred.

### 59. AutoMat — 24/30

`AUTOMAT-2505.12650`, https://arxiv.org/abs/2505.12650, v1 2025-05-19. Manual microscopy interpretation is slow; physics-guided closed loop generates hypotheses for 2D monolayer iDPC-STEM. Instrument/data pipeline owns observations and calibration, model proposes structures, physical checks retain authority. Experiments prove workflow utility in disclosed material/microscopy settings, not autonomous materials discovery or broad microscopy. Risks model-confirmation loops and instrument bias. Owner `AGENT-WORKFLOW` + evaluation domain path; `Emerging`; open: blinded lab replication.

### 60. CompeteSMoE — 24/30

`COMPETESMOE-2505.13380`, https://arxiv.org/abs/2505.13380, v1 2025-05-19. Top-k routers optimize learned logits but can collapse/load-imbalance. Expert neural-response competition supplies routing; model owns router/expert state, distributed runtime owns placement/capacity. A 5.1B VLM and ablations demonstrate conditional gains, not frontier-scale/network efficiency. Risks irregular communication and unstable specialization. Owner `MODEL-MOE` + training/runtime handoff; `Emerging`; open: multi-node routing overhead.

### 61. QZO — 24/30

`QZO-2505.13430`, https://arxiv.org/abs/2505.13430, v1 2025-05-19. Backprop stores gradients/optimizer states; quantized zeroth-order tuning estimates directional derivatives from losses. Trainer owns perturbation seeds and quantized weights, no gradient state. Authors report 4-bit results comparable with MeZO, ~3× lower memory and a 2-bit Llama2-13B case; this does not prove equal convergence across tasks or lower wall time on every device. Noise/slow convergence are failures. Owner `TRAIN-LORA`; `Emerging`; open: full time/energy contract.

### 62. PiFlow — 24/30

`PIFLOW-2505.15047`, https://arxiv.org/abs/2505.15047, v1 2025-05-21. Greedy scientific proposal lacks uncertainty-aware exploration. Min-max regret/information-gain search with QwenMax chooses experiments/hypotheses; workflow owns evidence/archive, model proposes. Surrogate tasks show search behavior, not real scientific discovery or calibrated uncertainty. Risks model-judge coupling and surrogate mismatch. Owner `AGENT-PLANNING` with `AGENT-WORKFLOW` handoff; `Emerging`; open: physical experiment loop.

### 63. VisualQuality-R1 — 21/30

`VISUALQUALITY-R1-2505.14460`, https://arxiv.org/abs/2505.14460, v1 2025-05-20. Single scalar image-quality labels are expensive and opaque. Pairwise RL-to-reason trains evaluative comparisons; judge owns rubric and model emits reasoning/score. Author visual benchmarks show gains but method is slow/memory-heavy, uses a single prompt family and lacks broad human operating-point validation. Owner `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: prompt/rater sensitivity.

### 64. RICE cognitive experts — 24/30

`RICE-2505.14681`, https://arxiv.org/abs/2505.14681, v1 2025-05-20. Aggregate reasoning scores hide latent specialization. nPMI identifies cognitive experts from response patterns; evaluation pipeline owns task/response matrix, model internals remain observational. DeepSeek-R1/Qwen3-235B cases show identifiable patterns, not causal modules or transfer to other models. Risks multiple-comparison artifacts. Owner `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: intervention validation.

### 65. Distillation source matters — 24/30

`DISTILL-SOURCE-2505.14464`, https://arxiv.org/abs/2505.14464, v1 2025-05-20. Treating all teacher traces as equivalent ignores source distribution. A 1.89M-query corpus from three teachers controls source/mixture; data pipeline owns teacher/provenance, student trainer owns sampling. Results show teacher source materially changes reasoning, not a universal best teacher; paper lacks explicit limitation section and hardware/SLO generality. Risks copying style/errors and benchmark leakage. Owner `TRAIN-DATA` with `TRAIN-SFT` handoff; `Refine candidate`; open: provenance-weighted mixing.

### 66. Vittle — 24/30

`VITTLE-2505.13946`, https://arxiv.org/abs/2505.13946, v1 2025-05-20. Full fine-tuning is costly under distribution shift. A bottleneck/KL-controlled adaptation targets compact internal changes; trainer owns bottleneck state. Tests span 45 datasets and 30 shifts with 7B/13B tuning, showing conditional robustness; early-layer convergence failure and KL sensitivity limit generalization. Hardware/production SLO incomplete. Owner `TRAIN-LORA`; `Emerging`; open: online rollback.

### 67. Latent knowledge elicitation — 22/30

`LATENT-KNOWLEDGE-2505.14352`, https://arxiv.org/abs/2505.14352, v1 2025-05-20. Output-only audits may miss encoded but unspoken knowledge. Probes/SAEs inspect a controlled Taboo model; evaluator owns labels/probe, model activation is observational state. Proof-of-concept shows elicitation in that setup, not general deception detection or semantic truth. Probe leakage and noncausality are threats. Owner `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: causal interventions/OOD.

### 68. AgentIF — 25/30

`AGENTIF-2505.16944`, https://arxiv.org/abs/2505.16944, v1 2025-05-22. Short instruction tests miss long agent constraints. Benchmark has 707 instructions, 50 agent tasks, mean 1,723 words and 11.9 constraints; harness owns constraints and executable/annotated checks. Results prove difficulty in English/Chinese semi-manual tasks, not universal instruction following. Annotation/judge ambiguity and environment opportunity remain. Owner `PLATFORM-EVALUATION-SYSTEM` + Agent; `Integrate candidate`; open: executable constraint coverage.

### 69. Think-RM — 25/30

`THINK-RM-2505.16265`, https://arxiv.org/abs/2505.16265, v1 2025-05-22. Scalar reward models struggle on complex comparisons. SFT on long evaluative CoT plus rule-reward RL and pairwise RLHF trains a reasoning judge; judge owns rubric/trace. Ablations compare longest vs shortest CoT and benchmarks show author gains, not rationale faithfulness or unbiased reward. Costs latency and judge self-consistency bias. Owner `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: causal rationale tests.

### 70. TinyV — 26/30

`TINYV-2505.14625`, https://arxiv.org/abs/2505.14625, v1 2025-05-20. Large verifiers are costly. A compact verifier trained with GRPO and boxed-answer extraction reduces evaluation footprint; judge owns verdict, parser owns answer contract. Math-only experiments show author efficiency/accuracy, not general verification or robust parsing. Risks format gaming and domain collapse. Owner `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: non-math/executable tasks.

### 71. LaViDa — 26/30

`LAVIDA-2505.16839`, https://arxiv.org/abs/2505.16839, v1 2025-05-22. AR VLM decoding is serial; diffusion enables parallel refinement. Complementary masking, prefix KV and timestep shift align vision/language masked generation; decoder owns mutable mask/timestep state. Author tasks show competitive performance with ~8% training slowdown, but scale gap and iterative latency remain; not proof of AR replacement. Owner `MULTIMODAL-GENERATIVE-PARADIGMS`; `Integrate candidate`; open: serving concurrency/cache.

### 72. FoVer — 27/30

`FOVER-2505.15960`, https://arxiv.org/abs/2505.15960, v1 2025-05-21. Natural-language reasoning lacks exact verification. Z3/Isabelle-generated FoVer40K trains Llama3.1-8B/Qwen2.5-7B and tests 12 reasoning benchmarks; formal tool owns proof truth, model owns translation/proposal. Results suggest formal-to-informal transfer, not theorem-prover completeness or arbitrary reasoning. Translation errors remain. Owner `PLATFORM-EVALUATION-SYSTEM` + `AGENT-TOOL-CALLING`; `Integrate candidate`; open: proof-carrying answers.

### 73. SafeKey — 25/30

`SAFEKEY-2505.16186`, https://arxiv.org/abs/2505.16186, v1 2025-05-21. Output-only refusal misses dangerous reasoning trajectories. Manually identified key sentences supervise early safety intervention; evaluator owns labels, runtime gates continuation. Tests are reasoning-only; multi-turn behavior, over-refusal and automatic key detection remain open. It proves a bounded intervention, not complete safety. Owner `PLATFORM-SECURITY`; `Emerging`; open: operating point and automation.

### 74. OViP — 25/30

`OVIP-2505.15963`, https://arxiv.org/abs/2505.15963, v1 2025-05-21. Static visual preference pairs miss policy evolution. Six-stage online DPO uses diffusion counterfactuals; trainer owns versioned policy/preference data. Reported 17h on 7×A800-40G shows feasibility but synchronization overhead and incomplete metrics limit generalization. Risks stale preferences and synthetic counterfactual bias. Owner `TRAIN-DPO`; `Emerging`; open: wall-clock/quality decomposition.

### 75. TON selective reasoning — 25/30

`TON-2505.16854`, https://arxiv.org/abs/2505.16854, v1 2025-05-22. Always-on CoT wastes cost. Thought-dropout SFT plus GRPO trains a selective policy; trainer owns mask/reward, serving owns budget. Tests cover 3B/7B synthetic/general/math/agent VQA, not larger models or production SLO; reward details limit replication. Premature no-think routing is the failure. Owner `TRAIN-RLHF` + inference handoff; `Integrate candidate`; open: confidence calibration.


### 76. SophiaVL-R1 — 26/30

`SOPHIAVL-R1-2505.17018`, https://arxiv.org/abs/2505.17018, v1 2025-05-22; full method/reward/eval/artifact read. Standard VLM tuning is answer-centric; RL adds multi-step visual reasoning incentives. Trainer owns rollout/reward, model owns visual/text proposal, evaluator owns ground truth. Author benchmark gains do not prove grounded/faithful reasoning; no explicit limitation section and full hardware/concurrency/SLO is incomplete. Risks reward shortcuts and verbose rationalization. Owner `TRAIN-RLHF` + multimodal/evaluation handoff; `Integrate candidate`; open: visual evidence intervention.

### 77. BYE backdoor cleaning — 26/30

`BYE-2505.16916`, https://arxiv.org/abs/2505.16916, v1 2025-05-22; full defense mechanism, threat model, experiments and appendices read. Generic fine-tuning may preserve a backdoor. BYE identifies/removes malicious behavior while attempting to retain utility; artifact owner must track base provenance and sanitizer version. Tested attacks/models show bounded cleaning, not universal removal; no explicit limitation section and adaptive attackers remain. Costs utility loss and false assurance. Owner `PLATFORM-SECURITY` + artifact governance; `Integrate candidate`; open: adaptive/compound triggers.

### 78. SpatialScore — 24/30, disputed numeric version

`SPATIALSCORE-2505.17012`, https://arxiv.org/abs/2505.17012, v1 2025-05-22; current HTML is later revision. v1 abstract reported roughly 28K/11 datasets/9 tools while current revision reports 5K/30 tasks/23 datasets/12 tools; therefore numeric claims are event-time disputed. The stable mechanism evaluates spatial reasoning through tool-assisted tasks and explicit spatial state; evaluator owns task/tool truth. Current results do not retroactively prove v1 corpus properties. Owner `PLATFORM-EVALUATION-SYSTEM` + embodied handoff; `Disputed` for counts, mechanism `Emerging`; required material: v1 PDF.

### 79. OCR Heads — 23/30

`OCR-HEADS-2505.15865`, https://arxiv.org/abs/2505.15865, v1 2025-05-21; full head-masking, attention analysis, eval and limitations read. Aggregate VLM accuracy hides OCR-specialized attention heads. Masking interventions identify heads and sink redistribution; model owns attention state, evaluator owns OCR labels. Results support causal contribution in tested models/up to ~8k context, not universal head taxonomy; model diversity is limited. Risks brittle pruning and attention-as-explanation. Owner `MODEL-SELF-ATTENTION` + multimodal representation; `Emerging`; open: cross-model replication.

### 80. VLM-R3 — 26/30

`VLM-R3-2505.16192`, https://arxiv.org/abs/2505.16192, v1 2025-05-21; full region-action policy, VLIR, R-GRPO, eval/artifact read. Text-only visual CoT cannot actively inspect regions. A region proposal/action loop changes image evidence available to the reasoner; environment owns crop/region state, policy proposes actions. Qwen2.5-VL with GPT-4o-generated rationales and benchmark gains do not prove independent grounding or general tool use; explicit limitations are sparse. Owner `MULTIMODAL-REPRESENTATION` + `AGENT-TOOL-CALLING`; `Integrate candidate`; open: teacher/rationale ablation.

### 81. When LLMs Admit Mistakes / retraction — 26/30

`RETRACTION-2505.16170`, https://arxiv.org/abs/2505.16170, v1 2025-05-21; current v4 is Aug-2026, so event-time results are version-pinned. Full behavioral/probe/steering study read. Retraction is separated from initial answer correctness; linear probes track momentary model belief and activation steering changes retraction within tested models. Llama/Qwen/Olmo 7B, Wikidata/Celebrity and LLM judge do not establish truth detection, intent or larger-model generality. Owner `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: v1 PDF and OOD causal replication.

### 82. vLLM V0 deprecation RFC — 24/30

`VLLM-RFC-18571`, https://github.com/vllm-project/vllm/issues/18571, opened 2025-05-22; full RFC/discussion read. Maintaining V0 and V1 split engineering effort; proposal freezes V0 after v0.9 and migrates/removes paths. Project maintainers own compatibility roadmap; users own migration. The RFC lists temporary gaps (encoder-decoder, draft speculation, Neuron, HPU) and permanent drops (prompt adapter, V100, per-request structured output), but proves a proposed plan—not that removal occurred. No benchmark mechanism. Owner `INFER-TENSORRT-LLM`; `Weekly Only — RFC / version governance`; open: release-by-release completion.

### 83. MMMG — 27/30

`MMMG-2505.17613`, https://arxiv.org/abs/2505.17613, v1 2025-05-23; full benchmark/data/eval/appendix read. Single-modality tests miss compositional modality combinations. MMMG defines 49 tasks, 937 instructions and four modality combinations; dataset/evaluator owns task identity and scoring. Human validation covers 37 tasks/1,886 questions/3 annotators with 94.3% agreement. Tests across 24 models reveal gaps but depend partly on proprietary models and limited task coverage; not a universal multimodal measure. Owner `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: executable and longitudinal subsets.

### 84. Implicit multi-hop reasoning scaling — 25/30

`IMPLICIT-MULTIHOP-2505.17923`, https://arxiv.org/abs/2505.17923, v1 2025-05-23; full controlled theory/experiments/appendix read. End-to-end memorization can appear as reasoning. Controlled GPT-2-style experiments vary hop depth/data and find data needs grow exponentially with hops while depth grows roughly linearly; curriculum helps but does not remove the barrier. Synthetic construction proves a scaling phenomenon in that family, not real LLM generalization or a universal exponent. Owner `WORLDVIEW-SCALING-LAW` with `MODEL-TRANSFORMER-LAYER` handoff; `Refine candidate`; open: architecture/data-distribution replication.

### 85. NFT negative-aware fine-tuning — 26/30

`NFT-2505.18116`, https://arxiv.org/abs/2505.18116, v1 2025-05-23; full objective derivation, on-policy equivalence, experiments and appendix read. SFT only increases positive likelihood and ignores rejected mass. NFT uses an implicit negative policy; under strict on-policy assumptions the authors derive equivalence to a GRPO-like update. 7B/32B math experiments support the claim in-domain, not general preference alignment or equivalence off-policy. Risks negative sampling bias and instability. Owner `TRAIN-DPO` with `TRAIN-RLHF` handoff; `Integrate candidate`; open: off-policy boundary.

### 86. SVL spiking vision-language pretraining — 22/30

`SVL-2505.17674`, https://arxiv.org/abs/2505.17674, v1 2025-05-23; full triple-alignment, reparameterizable integration, tests and appendix read. Dense V-L pretraining is accurate but energy-costly; spike representation seeks sparse event-driven compute. Model owns spike/representation state; hardware runtime determines whether theoretical sparsity becomes savings. 3D/downstream tasks show feasibility, not wall-energy benefit on deployed neuromorphic hardware; hardware/energy contract is incomplete. Owner `MULTIMODAL-REPRESENTATION` with execution handoff; `Emerging`; open: measured energy/latency.

### 87. Thinkless — 26/30

`THINKLESS-2505.13379`, https://arxiv.org/abs/2505.13379, v1 2025-05-19; full mode-control training/eval/ablation read. Always-on long CoT wastes tokens; a learned think/no-think policy adapts compute. Trainer owns mode labels/reward, serving owns maximum budget. Author benchmarks show a quality–cost Pareto improvement, not calibrated domain-general routing. Premature cheap-path selection is the new failure; fixed/no-thinking remains apt for simple deterministic tasks. Owner `TRAIN-RLHF` + `INFER-SCHEDULING`; `Integrate candidate`; open: risk-aware threshold.

### 88. OSWorld-G / Jedi — 27/30

`OSWORLD-G-2505.13227`, https://arxiv.org/abs/2505.13227, v1 2025-05-19; full generator/environment/training/evaluation read. Human-authored GUI tasks are scarce. Procedural task generation plus executable verification expands training/eval; environment owns ground truth/UI state, policy acts, generator owns task proposal. Results show gains in OSWorld-like harness, not real-desktop autonomy; UI nondeterminism and generator bias constrain validity. Owner `AGENT-WORKFLOW` + evaluation; `Integrate candidate`; open: reproducible snapshots.

### 89. VSA trainable sparse attention — 29/30

`VSA-2505.13389`, https://arxiv.org/abs/2505.13389, v1 2025-05-19; full architecture/training/eval/ablation read. Fixed sparse patterns are kernel-friendly but task-blind. Trainable sparse routing learns token interactions; model owns masks/router, runtime must support irregular kernels. Author long-context results bind model/length/hardware, not every workload; communication/kernel overhead can erase theoretical sparsity. Risks router instability and load imbalance. Owner `MODEL-SELF-ATTENTION` + execution handoff; `Integrate candidate`; open: distributed kernel contract.

### 90. LatentSeek — 24/30

`LATENTSEEK-2505.13308`, https://arxiv.org/abs/2505.13308, v1 2025-05-19; full latent-search method/eval/appendix read. Discrete CoT is auditable but token-expensive. Continuous hidden-state search compresses/explores reasoning before output; model owns latent trajectory, runtime only observes final tokens. Selected reasoning gains do not prove interpretability, faithfulness or generality; hidden state cannot be externally verified. Owner `MODEL-TRANSFORMER-LAYER` with evaluation handoff; `Emerging`; open: causal state probes.

### 91. MM-PRM — 25/30

`MM-PRM-2505.13427`, https://arxiv.org/abs/2505.13427, v1 2025-05-19; full multimodal process reward training/eval read. Outcome-only VLM supervision cannot identify bad visual steps. Step-level grounded scoring makes judge own image evidence/rubric and trainer consume versioned rewards. Benchmark gains show usefulness under supplied annotations, not faithful reasoning or causal grounding. Risks judge shortcut and expensive labels. Owner `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: executable visual checks.

### 92. FedSVD — 26/30

`FEDSVD-2505.12805`, https://arxiv.org/abs/2505.12805, v1 2025-05-19; full federated algorithm, communication analysis, experiments and appendix read. Sending dense updates is simple but bandwidth-heavy. Low-rank/SVD factors reduce communication; clients own local factors/data, server owns versioned aggregate. Results depend on client heterogeneity, model and network assumptions; privacy/security is not automatic and production SLO absent. Risks rank mismatch, aggregation drift and leakage. Owner `TRAIN-DISTRIBUTED-TRAINING`; `Integrate candidate`; open: secure aggregation composition.

### 93. R3 reward model — 25/30

`R3-2505.13388`, https://arxiv.org/abs/2505.13388, v1 2025-05-19; full reasoning/rubric reward-model training/eval/ablation read. Direct scalar judgment is efficient but opaque. R3 reasons over rubric/evidence before score; judge owns rubric/trace, trainer consumes score. Author benchmarks show gains, not faithful rationales or unbiased evaluation; inference cost and bias remain. Rule/executable checks remain better where available. Owner `PLATFORM-EVALUATION-SYSTEM`; `Integrate candidate`; open: causal rationale ablation.

### 94. GS-Jacobi / TarFlow — 27/30

`GS-JACOBI-2505.12849`, https://arxiv.org/abs/2505.12849, v1 2025-05-19; full iterative/parallel generation method, implementation, eval and sensitivity read. Strict serial decoding is exact but slow. Jacobi-like block updates/flow proposal allow parallel refinement; decoder owns provisional block state and only convergence/verification grants commit. Speedups bind model/hardware/length and quality criteria; not universal exactness. Risks non-convergence, rollback and kernel overhead. Owner `INFER-SPECULATIVE-DECODING` / generative branch; `Integrate candidate`; open: deterministic commit criteria.

### 95. Low-Rank Clone — 26/30

`LOW-RANK-CLONE-2505.12781`, https://arxiv.org/abs/2505.12781, v1 2025-05-19; full clone/compression algorithm, query budget, tests and appendix read. Full teacher replication is expensive. Low-rank surrogate approximates behavior under bounded queries/parameters; trainer owns queried dataset/provenance, student owns approximation. Results show task-level similarity, not semantic/safety equivalence or resistance to extraction abuse. Risks hidden failure modes and copied bias. Owner `TRAIN-SFT`; `Integrate candidate`; open: behavioral coverage/security boundary.

### 96. Neurosymbolic Diffusion Models — 25/30

`NESYDM-2505.13138`, https://arxiv.org/abs/2505.13138, v1 2025-05-19; full symbolic constraint integration, denoising, eval and appendix read. Pure diffusion handles uncertainty but may violate hard rules. Symbolic constraints guide mutable denoise state; solver owns constraint truth, model owns proposal distribution. Selected domains show better constraint satisfaction, not general exactness or scalable solver integration. Risks infeasible constraints and solver bottlenecks. Owner `MULTIMODAL-GENERATIVE-PARADIGMS`; `Integrate candidate`; open: proof/rollback semantics.

### 98. RLVR-World — 23/30

`RLVR-WORLD-2505.13934`, https://arxiv.org/abs/2505.13934; v1 2025-05-20, current HTML v2 2025-10-25; paper, appendices and artifact read with event-time identity pinned. Teacher-forced world models were reasonable because next-state likelihood is dense and stable, but it does not directly optimize decoded transition usefulness. RLVR-World samples a state/action-conditioned next-state sequence, decodes it, and applies verifiable environment-specific rewards with GRPO. The dataset/environment owns state and reward truth; the model owns the proposed transition; the trainer owns rollout/reference-policy state. Text games use 76,369 transitions across 31 ByteSized32 games and 2,954 test cases with DeepSeek-R1-Distill-Qwen 1.5B/7B; web uses a 7K WebArena subset; robot/video uses 256-bin action dimensions plus L1 and LPIPS rewards. Compute is disclosed per branch (text SFT 4xA100-80G 6.5h, RLVR 8xA100-80G 22.5h; web SFT 8xA100-40G 17h, RLVR 8xH100-80G 25h; robot tokenizer/transformer hundreds of GPU-hours and RLVR on 4xA100-40G). Ablations support the reward/training contribution under these contracts, not causal or counterfactual world understanding, cross-dataset video generalization, or a universal advantage over likelihood training. Failure modes include reward aliasing, simulator bias and visually plausible but causally wrong transitions; supervised learning remains appropriate where likelihood matches downstream use. Owner `MULTIMODAL-WORLD-MODELS`; adjacent embodied/RL/evaluation nodes checked; `Emerging / Experimental`; open: OOD interventions and reward robustness.

### 99. UniVG-R1 — 20/30

`UNIVG-R1-2505.14231`, https://arxiv.org/abs/2505.14231; v1 2025-05-20; full method, data, evaluation, ablations and appendix read. Direct coordinate supervision was reasonable for referring segmentation, but difficult queries need an explicit reasoning path and binary final reward loses localization structure. UniVG-R1 warm-starts on about 90K chain-of-thought grounding examples, then applies GRPO with IoU-derived reward and difficulty-aware weighting. The policy owns textual/coordinate proposals; image/annotation pipeline owns mask truth; trainer owns group rollouts and weights. Stage-one data is about 76K+14K and stage two 7K+3K; zero-shot tests include LISA, LLMSeg, ReVOS and ReasonVOS, and the paper repairs a MIG-Bench issue. Pure RL underperforms the CoT-SFT starting point by 7.07 points, so the evidence supports layering rather than RL replacement. Hardware, precision, serving latency/concurrency and broad safety are not disclosed. It proves conditional gains in the supplied visual-grounding contract, not faithful rationales or universal visual reasoning. Risks are synthetic-rationale bias, IoU reward shortcuts and dataset-specific difficulty weights. Owner `TRAIN-RLHF` with `MULTIMODAL-REPRESENTATION`/`PLATFORM-EVALUATION-SYSTEM` handoffs; `Emerging`; open: human-grounded trajectory audit.

### 100. Hunyuan-Game — 22/30

`HUNYUAN-GAME-2505.14135`, https://arxiv.org/abs/2505.14135; v1 2025-05-20; technical report, method/evaluation sections and stated limitations read. Frame/video generation is reasonable for appearance synthesis, but interactive game content changes the constraint to long temporal consistency, controllability and asset/pipeline compatibility. The report combines large image/video curation pipelines with a game-oriented generation stack; data pipelines own filtering/provenance, model owns visual proposals, external engines and artists retain authoritative world/asset state. It reports billion-scale images and millions of videos with multiple domain pipelines, but does not disclose a reproducible hardware/precision/length/batch/concurrency/SLO contract, a complete shared baseline, or clean component ablations. It proves that the disclosed production-oriented system was assembled and evaluated by the authors, not a causal world model, playable-state correctness or general industrial superiority. Failure modes include distorted physics, action inconsistency, temporal drift and opaque data provenance; conventional asset pipelines remain preferable where editability and determinism dominate. Owner `MULTIMODAL-GENERATIVE-PARADIGMS` with world-model/embodied handoff; `Weekly Only / Experimental system report`; open: reproducible control and state-transition evaluation.

### 101. Latent Flow Transformer — 23/30

`LATENT-FLOW-TRANSFORMER-2505.14513`, https://arxiv.org/abs/2505.14513; v1 2025-05-20; full derivation, method, experiments and appendices read. Deleting layers is a simple compression baseline but assumes a discrete mapping from deep to shallow computation. The paper learns continuous-depth latent transport with flow matching and introduces Flow Walking to distill multiple layers into fewer transitions. Original checkpoints own boundary hidden states; the learned flow owns intermediate latent dynamics; the compressed runtime owns the reduced transition schedule. On Pythia-410M, compressing 6/24 layers reports KL 0.407 versus 0.529 for a skip-two baseline, and distilling 12 layers to one reports KL 0.736 versus 0.932 for skip-three. These controlled comparisons support a mechanism for that model, not large-model scaling, semantic equivalence or production speedup; hardware, kernel overhead and serving SLO are incomplete. Failures include off-manifold transport, compounding approximation error and task-specific degradation; direct pruning remains rational when retraining is unavailable. Owner `MODEL-TRANSFORMER-LAYER` with compression/execution handoff; `Emerging`; open: downstream and larger-scale causal tests.

### 102. Self-Braking Tuning — 24/30

`SELF-BRAKING-2505.14604`, https://arxiv.org/abs/2505.14604; v1 2025-05-20, current v4 2025-10; event-time identity pinned and full current paper/appendix/artifact read, with later numerics not silently backported. Fixed maximum lengths are reliable cost guards but cannot distinguish useful verification from overthinking. SBT-E/D adds an overthinking score and example/difficulty-aware braking during tuning; trainer owns braking labels/thresholds and policy state, serving still owns hard caps. It uses 92K OpenR1-Math examples, Qwen2.5-Math-1.5B/7B and Llama-3.2-1B/Llama-3.1-8B, 64 Ascend H910B-64G, max length 16,384 and three epochs; inference uses A100, temperature 0.7 and eight samples. Reported 30–60% token reduction is conditional and some accuracy drops remain. Evidence supports a tunable Pareto branch, not calibrated uncertainty or domain-general early stopping. New failures are premature braking, threshold drift and terse unsupported answers; deterministic fixed budgets remain safer under hard SLOs. Owner `TRAIN-RLHF` with `INFER-SCHEDULING`; `Emerging`; open: retrieve v1 PDF for exact event-time result table.

### 103. RL-Tango — 24/30

`RL-TANGO-2505.15034`, https://arxiv.org/abs/2505.15034 and https://github.com/kaiwenzha/RL-Tango; v1 2025-05-21; method, objectives, experiments, ablations and code documentation read. A frozen or SFT-trained verifier is simple and stable, but becomes stale as the generator changes and can be reward-hacked. Tango alternates RL updates for a generator and a generative process verifier. The verifier learns textual step judgments from outcome-level correctness; the generator combines outcome and step advantages with a decayed weighting; class-aware verifier updates address all-negative collapse. Trainer owns the two policy versions and rollout coupling; verifier owns sampled judgments, not ground truth; answer checker owns outcome truth. Tests span 7B/8B models, five competition-math and four OOD reasoning tasks plus ProcessBench across three RL algorithms. Author gains and ablations show benefit under that closed-loop contract, not faithful step labels, stability under open domains or immunity to collusive co-adaptation; GPU/precision/concurrency/SLO is not disclosed. Risks are generator-verifier collusion, non-stationarity, stochastic reward variance and doubled training cost; fixed executable verifiers remain superior where exact. Owner `TRAIN-RLHF` with `PLATFORM-EVALUATION-SYSTEM`; `Emerging`; open: independent verifier audit and compute disclosure.

### 104. Entropy Minimization in LLM Reasoning — 21/30

`ENTROPY-MIN-2505.15134`, https://arxiv.org/abs/2505.15134; v1 2025-05-21; theorem, training/inference variants, baselines, appendices and limitation section read. Supervised/RL adaptation is reasonable when labels or rewards exist; the changed constraint is label-free adaptation. EM-FT/EM-RL minimize output entropy, while EM-INF optimizes or temperature-scales logits online; model logits are the mutable state and no external truth enters the update. Adaptive temperature is a critical baseline: it lowers entropy while preserving logit order, unlike optimized logits that can reorder non-top choices in high-uncertainty cases. Evaluation covers math, SciCode and alignment tasks using pass@1-style contracts, but hardware is undisclosed. The paper explicitly shows failure on Llama-3.1-8B math and individualistic-value reasoning when base capability/confidence is not informative. Thus entropy reduction is not confidence calibration or correctness and should be a baseline, not a universal solution. Failure modes are confident error amplification, distribution collapse and online latency. Owner `MODEL-SAMPLING` with training/evaluation handoff; `Emerging`; open: calibration and selective-risk curves.

### 105. Scaling Diffusion Transformers Efficiently via muP — 25/30

`DIT-MUP-2505.15270`, https://arxiv.org/abs/2505.15270; v1 2025-05-21; derivation, DiT/PixArt/MMDiT experiments, appendices, compute and limitations read. Retuning hyperparameters at each scale is reasonable at small scale but becomes prohibitive. The paper derives a maximal-update parameterization for mainstream diffusion Transformers so proxy-width/base hyperparameters transfer to target scale. Trainer owns parameterization/base-width metadata, optimizer hyperparameters and proxy/target lineage. It tests DiT-XL/2, PixArt-alpha 0.04B→0.61B and MMDiT 0.18B→18B; the 18B setup uses 820M image-text pairs at 256x256, batch 4,096 and 200K steps. A width-288 proxy costs 104 A100-80GB hours and the DiT target about 224 A100-80GB days; proxy search is reported as 5.5% of one PixArt run and 14.5% of one MMDiT run / 3% of manual-tuning cost. Baselines, learning-rate/width/data sensitivity and human alignment tests support transfer under these architectures, not an optimal proxy size or universal optimizer/schedule transfer. Risks are proxy-task mismatch and hidden data/architecture interactions; direct tuning remains useful when the target is small or distribution shifts. Owner `TRAIN-PRETRAINING`; `Integrate candidate`; open: independent replication and proxy-selection rule.

### 106. Adaptive Self-Recovery Reasoning — 24/30

`ASRR-2505.15400`, https://arxiv.org/abs/2505.15400; v1 2025-05-21, v2 2025-05-23; current paper, appendices and training tables read, with version boundary recorded. Uniform long reasoning was reasonable when difficulty was unknown; many easy queries instead continue after a correct answer. The method adds a no-think prefix and a dynamic length penalty activated only after group accuracy crosses a threshold, preserving exploration before compressing. Trainer owns group accuracy, curriculum window and reward; serving owns the final budget. DeepSeek-R1-Distill-Qwen-1.5B/7B across five math benchmarks uses 32 A100-80GB SXM GPUs; disclosed settings include batch 128, 24K length, LR 5e-7, beta 0.5, alpha 1.0 and window 2,048. Reported reductions of 32.5%/25.7% accompany pass@1 drops of 1.2/0.6 points. Ablations and cases support a conditional efficiency trade-off, not an intrinsic self-recovery mechanism, larger-model/domain generality or calibrated stopping. Risks are activation-threshold gaming and suppressing useful backtracking. Owner `TRAIN-RLHF` with inference handoff; `Emerging`; open: v1 numeric table and non-math tests.

### 107. LASER-D adaptive length reward — 24/30

`LASER-D-2505.15612`, https://arxiv.org/abs/2505.15612; v1 2025-05-21; full framework, baselines, scale/OOD analyses, qualitative appendix and limitations read. Hard truncation is a strong, simple baseline because it directly enforces a budget, but it treats every query alike and marks all over-budget trajectories wrong. LASER adds length shaping; LASER-D selects difficulty-aware target lengths; LASER-DE further adapts the efficiency pressure. Trainer owns target-length enumeration and reward; model owns reasoning trajectory; serving retains hard caps. DeepScaleR-Preview 40K trains DeepSeek-R1-Distill-Qwen 1.5B/7B/32B; tests cover MATH500, OlympiadBench, AIME2024, AMC2023 plus GPQA/LSAT/MMLU. The 1.5B result reports +6.1 points with 63% fewer tokens on AIME24, while larger settings show different Pareto points; hardware/precision is undisclosed. Behavioral analysis indicates less redundant backtracking but relies partly on keywords and GPT-4.1-mini classification, so it does not prove hidden reasoning quality. The explicit limitation is math-centric verification; code/agent validity remains open. Failure modes are short wrong answers and hyperparameter sensitivity; truncation remains preferable for strict predictable ceilings. Owner `TRAIN-RLHF`; `Emerging`; open: executable non-math evaluators.


### 108. Soft Thinking — 23/30

`SOFT-THINKING-2505.15778`, https://arxiv.org/abs/2505.15778; v1 2025-05-21; full method, math/code evaluation, analysis and appendix limitation read. Discrete CoT is auditable and distribution-matched but serial and potentially verbose. Soft Thinking feeds the probability-weighted mixture of vocabulary embeddings as the next internal concept token, using output probabilities as a bridge between decoupled hidden/output and input-embedding spaces; Cold Stop returns to discrete output once sufficiently confident. The decoder owns a mutable soft-token trajectory; no external verifier or persistent state is introduced. Training-free tests use QwQ-32B, DeepSeek-R1-Distill-Qwen-32B and DeepSeek-R1-Distill-Llama-70B on four math and three coding benchmarks, reporting small pass@1 gains and 11.6–22.4% math / 16.1–19.1% code token reductions; hardware, precision, latency/concurrency and SLO are undisclosed. Greedy decoding is an important baseline, but the study does not establish faithfulness, semantic compression or universal speedup. The paper explicitly notes concept tokens are OOD because base models were trained on discrete sequences, causing long-chain instability or collapse. Discrete CoT remains safer for auditability and exact tool contracts. Owner `MODEL-TRANSFORMER-LAYER` with `MODEL-SAMPLING`; `Emerging`; open: trained soft-token robustness and wall-clock measurements.

### 109. Streamline Without Sacrifice / ProxyV — 24/30

`PROXYV-2505.15816`, https://arxiv.org/abs/2505.15816 with final ICML/PMLR paper https://proceedings.mlr.press/v267/wu25s.html and artifact https://github.com/penghao-wu/ProxyV; v1 2025-05-21; full method/results/supplement and artifact documentation read. Token pruning is a rational efficiency branch but can remove small text, objects or grounding details. ProxyV instead keeps all visual tokens while routing expensive attention/FFN work through a smaller proxy-token set; lightweight two-layer guided-update MLPs transfer each spatial proxy back to its full-token group. Model/runtime owns layer-start choice and proxy/full-token state; prefill engine owns the realized kernel path. Across six LLM backbones and DocVQA/ChartQA/InfoVQA/OCRBench/TextVQA plus RefCOCO/document parsing, the Vicuna-1.5-7B examples report 36–46% lower prefill FLOPs and 31–41% lower time at 101–102.4% relative fine-grained score. Comparisons with VisionZip/PyramidDrop and a non-spatial variant support computation-reduction as an alternative branch, not proof of zero information loss. Results depend on fixed vision/text token ratios and eager-attention settings; start layers appear selected using the same redundancy suite and repeated-run/error-bar evidence is absent. Risks are layer/backbone sensitivity and proxy bottlenecks; pruning remains rational where dense detail is irrelevant. Owner `MULTIMODAL-REPRESENTATION` with `INFER-TENSORRT-LLM`; `Emerging`; open: held-out start-layer selection and FlashAttention kernels.

### 110. Pixel Reasoner — 20/30

`PIXEL-REASONER-2505.15966`, https://arxiv.org/abs/2505.15966; v1 2025-05-21; full trajectory construction, curiosity reward, experiments, ablations and appendix read. Text-only VLM reasoning is simple but cannot change the visual evidence it sees. Pixel Reasoner lets a policy invoke visual operations and observe transformed pixels, warm-starting on 7,500 trajectories (5,500 GPT-4o-synthesized pixel-space plus 2,000 text-space) and then applying curiosity-driven RL on another 7,500 examples. The environment owns image/video operation state and errors; model proposes operations/answers; trainer owns exploration reward. Qwen2.5-VL-7B is compared with tool-free and tool-using baselines on V*Bench, TallyQA-complex, MVBench-test and InfoVQA; ablations remove RL, curiosity, warm start and correction data. The reported gains establish that the supplied operation opportunity can help, not that the reasoning trace is faithful or deployable without a sandbox. Hardware, precision, operation latency and concurrency/SLO are undisclosed. Data covers only a small set of operations/domains; tool errors, unsafe crops/transforms and synthetic-teacher bias are new failures. Owner `AGENT-TOOL-CALLING` with `MULTIMODAL-REPRESENTATION`; `Emerging`; open: executable provenance and broader operation safety.

### 111. Jenga / Dynamic Token Carving — 24/30

`JENGA-VIDEO-2505.16864`, https://arxiv.org/abs/2505.16864, later NeurIPS paper https://proceedings.neurips.cc/paper_files/paper/2025/file/75b2a6632ab7b9196e9cb93750986e45-Paper-Conference.pdf, and artifact https://github.com/JIA-Lab-research/Jenga; v1 2025-05-22; paper, appendix/failure cases and code/README paths read. Dense full-resolution attention at every denoise step is exact and easy to reason about, but 100K+ video tokens and many steps make it impractical. Jenga combines Attention Carving—3D space-filling-curve ordering, head-aware block top-k selection and a Triton sparse kernel—with Progressive Resolution, which predicts a clean latent, upsamples, re-noises and continues at higher resolution; a text-attention amplifier counters low-resolution field-of-view drift. Runtime owns provisional denoise state, resolution transitions, sparse masks and scheduler; model weights remain unchanged. Author contracts include HunyuanVideo 720x1280x125 frames/50 steps on one H800 (1625s to 310/225/184/157s across presets), 8xH800 paths, Hunyuan-I2V 1088x832x125f, Wan2.1-1.3B 832x480x81f and 14B 1280x720x81f. VBench/architecture comparisons, component presets and cross-model tests support conditional acceleration, not universal quality preservation. Later appendix notes static/clear-boundary and I2V degradation from latent resizing; VAE decode-resize-encode would add about 50s. Failures include missed attention blocks, temporal flicker and resolution-transition artifacts; dense attention remains safer for boundary-critical scenes. Owner `INFER-TENSORRT-LLM` with `MULTIMODAL-GENERATIVE-PARADIGMS`; `Integrate candidate`; open: event-time v1 versus later artifact/revision delta.

### 112. LLaDA-V — 23/30

`LLADA-V-2505.16933`, https://arxiv.org/abs/2505.16933; v1 2025-05-22, v2 2025-06-04; current paper, training table, benchmark suite and limitations read with revision boundary recorded. Autoregressive visual instruction tuning is mature and cache-friendly, but enforces serial text generation. LLaDA-V maps SigLIP2 features through a two-layer MLP into LLaDA-8B, trains bidirectional masked diffusion over multimodal dialogues and decodes by repeated low-confidence remasking. The decoder owns the mutable mask/timestep state; vision tower owns image features; trainer owns staged data/attention objective. The stages disclose 558K alignment, 10M single-image, 2M multimodal, 900K reasoning and 3M balanced samples; batch 64/256, max lengths 8,192/16,384 and component learning rates. Eighteen benchmarks and matched LLaMA3-V comparisons support feasibility/data scaling, not overall superiority; AI2D/RealWorldQA and high-resolution handling expose losses. Hardware, precision, end-to-end latency/concurrency and SLO are not disclosed. High-resolution split/resize may reduce efficiency/accuracy and hallucinations remain. Owner `MULTIMODAL-GENERATIVE-PARADIGMS`; `Emerging`; open: fair wall-clock/KV comparison.

### 113. Dimple — 23/30

`DIMPLE-2505.16990`, https://arxiv.org/abs/2505.16990 and https://github.com/yu-rp/Dimple; v1 2025-05-22; full objective, alignment/instruction tuning, confident decoding, ablations, discussion and artifact read. Autoregressive MLLMs provide stable causal decoding, but generation is serial. Dimple adapts the Dream/Qwen2.5 discrete diffusion LM to vision and uses confidence-ranked unmasking so multiple tokens commit per iteration; structure priors constrain output format/length. Decoder owns mask/confidence/iteration state; prefilling and vision alignment are separate. Dimple-7B uses 1.3M samples / 0.8B tokens and is compared mainly with LLaVA-1.5/NEXT, Eagle and Qwen-VL families on 13 benchmarks. It reports 62.4 average versus 58.5 for LLaVA-NEXT and iterations near response-length/3, with 1.5–7x prefilling speedup in tested settings. Different base LMs and 20x+ data gaps make several baselines only lower/upper references; hardware, precision, wall-clock concurrency and SLO are undisclosed. Full attention remains quadratic and random decoding affects meaningful length. It proves a viable branch, not AR replacement. Owner `MULTIMODAL-GENERATIVE-PARADIGMS`; `Emerging`; open: matched-base/data and serving tests.

### 114. GoT-R1 — 23/30

`GOT-R1-2505.17022`, https://arxiv.org/abs/2505.17022; v1 2025-05-22, current HTML v2 2026-04-12; current full paper/appendices read with event-time claims pinned. Direct text-to-image generation is low-latency but struggles with dense compositional/spatial prompts. GoT-R1 first trains a textual generation chain-of-thought, then uses online GRPO with an MLLM-based dual-stage reward over prompt–reasoning semantics/spatial layout, prompt–image quality and reasoning–image grounding. Policy owns reasoning/image tokens; external MLLM owns learned reward judgments, not truth; trainer owns rollout/reference state. Janus-Pro-1B/7B is pretrained for 70K steps on LAHR/JourneyDB/FLUX-GoT and run for 1K GRPO steps on T2I-CompBench/LAION-Aesthetics prompts. T2I-CompBench/GenEval, multi-reward ablations and three-run stability tests support the combined reward under that setup, while HPS-only ablation demonstrates reward hacking. Hardware/precision/concurrency is undisclosed; explicit CoT raises author-reported latency about 30%, >10-object boxes degrade, and reward quality depends on the MLLM. Owner `MULTIMODAL-GENERATIVE-PARADIGMS` with evaluation/RL handoff; `Emerging`; open: v1 PDF and executable spatial rewards.

### 115. Reasoning Model is Stubborn / ReasoningTrap — 24/30

`REASONINGTRAP-2505.17225`, https://arxiv.org/abs/2505.17225 with project/dataset https://reasoningtrap.github.io/; v1 2025-05-22; full OpenReview text, dataset cards, experiments and limitation section read. Standard reasoning benchmarks reward familiar solution patterns, so stronger pattern reuse is normally rational; modified constraints expose when that prior overrides the prompt. ReasoningTrap creates conditioned AIME/MATH500 and redesigned puzzles and measures pass@1 plus a paragraph-level perception score. Prompt/dataset owns modified constraints; evaluator owns exact/LLM-judged correctness; model reasoning is observed, not treated as ground truth. Tests span Qwen2.5/QwQ/Qwen3, DeepSeek V3/R1, OpenAI, Gemini and Claude families with 16 samples per main question; paired base/reasoning comparisons show reasoning variants often adhere less despite strong standard scores. Budget forcing and prompt hints do not consistently fix the issue. This supports three observed modes—interpretation overload, input distrust and partial instruction attention—not that RL itself is the causal component or that rigidity generalizes beyond math/puzzles. Proprietary hidden reasoning and LLM judging limit attribution. Owner `PLATFORM-EVALUATION-SYSTEM` with prompt/context handoff; `Integrate candidate`; open: causal training ablation and non-math executable diagnostics.

### Reasoning Path Compression — 24/30

- **Candidate / Week / Score:** Reasoning Path Compression / 2025-W21 / `4/4/4/4/4/4 = 24`.
- **Source Family ID / Type:** `RPC-2505.13866`; primary paper plus author code.
- **Event Date / Revision:** v1 2025-05-20; v2 2025-10-24. W21 owns v1; v2 is revision evidence only.
- **Direct / Related Primary Sources:** https://arxiv.org/abs/2505.13866, https://arxiv.org/pdf/2505.13866v1, https://github.com/jiwonsong-dev/ReasoningPathCompression; full-KV, H2O, TOVA and LightThinker are comparison branches in the paper.
- **Access and Verification Status / Full-read Coverage:** Verified. v1 PDF, current HTML, revision history and artifact were read across metadata, Background, semantic-sparsity analysis, algorithm/equations, selection-window mechanism, experiments, interval/window ablations and appendices.
- **Original Problem:** long generated reasoning paths make output-side KV state a memory/throughput bottleneck.
- **Why the Previous Design Was Reasonable:** retaining every KV entry preserves exact causal attention and avoids deleting a token that becomes relevant later.
- **Changed Constraint:** 16K–32K reasoning outputs contain repeated re-derivations, so full-history state grows faster than useful information.
- **Mechanism:** at each compression interval, recent queries score older positions; RPC preserves the selector window and top-ranked past positions under a compression ratio, then compacts KV without changing weights.
- **State Ownership:** runtime owns position identity, compression epochs and physical K/V compaction; the model supplies attention/query signals but does not own eviction policy.
- **Control / Data Flow:** decode → accumulate KV → interval → score old positions from recent queries → select/compact → update position map → resume decode.
- **Implementation Details:** training-free; interval, selector-window size and ratio remain workload parameters, not model constants.
- **Evaluation Contract:** AIME 2024/LiveCodeBench accuracy plus throughput/memory; v1 covers QwQ-32B and DeepSeek-R1-Distill-Qwen-7B, 8K/16K/32K lengths, batch 16 and one-/four-H100 paths. The headline is up to 75% generated-KV reduction and 1.60x throughput with 1.2-point AIME pass@1 loss.
- **Baselines / Ablations / Sensitivity / Overhead:** full KV, H2O/TOVA and reasoning-compression baselines; interval/window sensitivity; scoring and compaction overhead can erase benefit when too frequent.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/H100/length/batch are partly disclosed; precision, multi-tenant concurrency and production SLO are not. No universal speedup is inferred.
- **What the Evidence Proves / Does Not Prove:** it proves a conditional accuracy–memory–throughput Pareto improvement; it does not prove exact decoding, future irrelevance of evicted tokens or dominance on short/non-reasoning workloads.
- **Limitations / Threats:** past attention cannot know future relevance; math/code concentration and author implementation limit transfer.
- **Trade-offs / New Failure Modes:** approximation, tuning and remapping complexity; silent deletion of a dependency needed later.
- **Where the Previous Design Still Applies:** short, exactness-sensitive or memory-unconstrained inference should retain full KV.
- **Evolution Relationship:** `Alternative Branch`: exact full history → output-aware approximate retention; it layers on allocation/paging.
- **ROADMAP / Adjacent Chapters Read:** owner `INFER-KV-CACHE` Ch45; Ch44–47 and Ch56 boundaries checked.
- **Existing Coverage / Integration Decision:** `Integrate — New Mechanism` candidate after the Books Gate; preserve full KV as the baseline branch.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: expose eviction confidence to rollback/verification and reconcile with prefix reuse/speculative rollback.

### Lessons from Defending Gemini Against Indirect Prompt Injections — 27/30

- **Candidate / Week / Score:** Gemini indirect-prompt-injection defense report / W21 / `5/5/4/5/4/4 = 27`.
- **Source Family ID / Type:** `GOOGLE-IPI-2505.14534`; Google DeepMind primary security report.
- **Event Date / Revision:** v1 and only version 2025-05-20.
- **Direct Primary Source:** https://arxiv.org/abs/2505.14534 and full v1 HTML/PDF.
- **Access / Full-read Coverage:** Verified across threat model, Actor-Critic/Beam/TAP/Linear attacks, datasets, ASR/NRR/ADR/TPR/FPR, adaptive evaluation, Gemini 1.5/2.5 results, adversarial training, in-context/classifier/reflection/perplexity/attention defenses and appendices.
- **Original Problem:** untrusted retrieved data shares a model context with trusted instructions and can steer tool calls or exfiltrate private data.
- **Why the Previous Design Was Reasonable:** prompt hierarchy and alignment suffice when context is trusted and actions are low impact.
- **Changed Constraint:** attackers adapt, retrieved content is adversarial, and agent tools grant access to user data/permissions.
- **Mechanism:** continuously generate attacks against the current model, measure attack and benign-rejection operating points, combine adversarial training with instruction/data separation and runtime defenses, then re-attack the combined system.
- **State Ownership:** host owns trust labels, provenance, permissions and enforcement; evaluator owns attacks/thresholds; model outputs are proposals.
- **Control / Data Flow:** trusted intent + untrusted data → model/tool proposal → transform/classifier/reflection → policy gate → action; adversarial results feed defense/training versions.
- **Implementation Details:** spotlighting, paraphrasing, retrieved-data/user-instruction classifiers, self-reflection, perplexity and attention tracking are evaluated separately and in combinations.
- **Evaluation Contract:** Google-specific email/data-exfiltration scenarios and Gemini versions; metric choice differs for in-context and classifier defenses. Production hardware, precision and SLO are undisclosed.
- **Baselines / Ablations / Sensitivity / Overhead:** undefended, non-adaptive/adaptive attacks and individual/combined defenses. False positives, text degradation and extra tokens/model calls are explicit costs; self-reflection is prompt-sensitive.
- **What It Proves / Does Not Prove:** adaptive testing changes measured robustness and defense in depth is necessary; no defense eliminates prompt injection, and training cannot replace least privilege/authorization.
- **Limitations / Threats:** vendor/scenario/language dependence, synthetic/adversarial data, detector thresholds and undisclosed production configuration.
- **Trade-offs / New Failure Modes:** lower ASR costs benign rejection and latency; classifiers drift and become a new attack/supply-chain surface.
- **Where the Previous Design Still Applies:** simple prompting only for trusted read-only low-impact contexts; deterministic controls remain superior for known action contracts.
- **Evolution Relationship:** `Layering`: alignment → adversarial training → adaptive evaluation → host-enforced instruction/data and permission boundaries.
- **ROADMAP / Adjacent Chapters:** owner `PLATFORM-SECURITY` Ch72; handoff `AGENT-TOOL-CALLING` Ch78, `PLATFORM-EVALUATION-SYSTEM` Ch66 and `AGENT-WORKFLOW` Ch81.
- **Existing Coverage / Integration Decision:** `Integrate — New Mechanism` candidate; retain the threat/evaluation loop, not vendor percentages.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: version attack corpora/operating points per model-tool policy and keep authorization deterministic.

### The Hallucination Tax of Reinforcement Finetuning — 25/30

- **Candidate / Week / Score:** Hallucination Tax of RFT / W21 / `4/4/4/4/5/4 = 25`.
- **Source Family ID / Type:** `HALLUCINATION-TAX-2505.13988`; primary paper and SUM dataset construction.
- **Event Date / Revision:** v1 and only version 2025-05-20.
- **Direct Primary Source:** https://arxiv.org/abs/2505.13988 and v1 full HTML/PDF.
- **Access / Full-read Coverage:** Verified across method, SUM generation, models, RFT setup, five mixture ratios, solvable/unanswerable/OOD/factual evaluation, learning dynamics and Limitations.
- **Original Problem:** correctness-only RFT suppresses refusal because every training item is answerable, producing confident answers on insufficient inputs.
- **Why the Previous Design Was Reasonable:** when tasks guarantee answerability and have executable verifiers, answering every prompt maximizes task reward.
- **Changed Constraint:** real workloads contain underspecified/unanswerable queries; selective prediction matters alongside accuracy.
- **Mechanism:** synthesize unanswerable math variants, mix them into RFT and reward recognition/refusal as a valid outcome. This changes the learned boundary; it is not an inference-time confidence estimator.
- **State Ownership:** data pipeline owns answerability labels/mixture; reward owns answer/refusal outcome; evaluator separately owns solvable accuracy and unanswerable refusal.
- **Control / Data Flow:** solvable corpus → synthesize/validate unanswerable variants → configure ratio → RFT rollouts/reward → dual selective evaluation.
- **Implementation Details:** DeepScaleR has 40,307 items; 300 evaluation and 40,007 training base; ratios 0/1/10/30/50% over Qwen2.5 and Llama instruction/non-instruction variants.
- **Evaluation Contract:** refusal on unanswerable math and accuracy on answerable math plus OOD/factual transfer. Hardware, precision, batch, concurrency and production SLO are incomplete.
- **Baselines / Ablations / Sensitivity / Overhead:** standard 0% RFT, five ratios, multiple models and learning curves. Ten percent is an observed point, not a universal constant; higher ratios can reduce answerable accuracy.
- **What It Proves / Does Not Prove:** standard RFT can degrade abstention and answerability-aware data can restore part of it; refusal is not calibrated uncertainty or proof of introspection.
- **Limitations / Threats:** synthetic math, limited models/domains, evaluator sensitivity and incomplete deployment contract.
- **Trade-offs / New Failure Modes:** over-refusal, synthetic artifacts and subgroup risk hidden by one mixture.
- **Where the Previous Design Still Applies:** pure outcome RFT for guaranteed-answerable executable tasks; hard policy gates still protect high-impact unknowns.
- **Evolution Relationship:** `Direct Evolution`: correctness-only RFT → answerability-aware selective RFT → calibrated release/evaluation gate.
- **ROADMAP / Adjacent Chapters:** owner `TRAIN-GRPO` Ch33; handoff `PLATFORM-EVALUATION-SYSTEM` Ch66 and `PLATFORM-SECURITY` Ch72.
- **Existing Coverage / Integration Decision:** `Refine — Existing Argument`; do not call abstention knowledge-boundary introspection.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: selective-risk metric/calibration and interaction with evidence retrieval.

### Be Careful When Fine-tuning On Open-Source LLMs — 27/30

- **Candidate / Week / Score:** downstream fine-tuning data extraction / W21 / `5/5/4/4/5/4 = 27`.
- **Source Family ID / Type:** `FT-EXTRACTION-2505.15656`; primary security paper plus code/data.
- **Event Date / Revision:** v1 2025-05-21; v2 2026-04-03 / ICLR 2026. W21 is pinned to v1.
- **Direct Primary Sources:** https://arxiv.org/abs/2505.15656, https://arxiv.org/pdf/2505.15656v1 and linked artifact.
- **Access / Full-read Coverage:** Verified. v1 identity/event paper, current full HTML, attack/defense appendices and artifact were checked; v2-only DP/robustness additions are revision evidence.
- **Original Problem:** a malicious base-model creator can implant behavior that later memorizes and reveals private downstream fine-tuning queries through black-box access.
- **Why the Previous Design Was Reasonable:** checksum/version pinning ensures reproducibility and normal tuning assumes the base artifact is benign.
- **Changed Constraint:** model weights are a supply-chain attack surface; the upstream attacker controls the base but sees only the downstream endpoint after private tuning.
- **Mechanism:** backdoor-train a special instruction/trigger into the base; downstream fine-tuning strengthens query-distribution memorization; crafted black-box prompts elicit memorized private queries.
- **State Ownership:** registry owns identity/signature/provenance; downstream trainer owns private data/recipe; attacker owns malicious upstream weights/query strategy.
- **Control / Data Flow:** malicious checkpoint → private SFT/LoRA/quantized tuning → deployed API → attacker trigger/sampling → extracted query candidates → match scoring.
- **Implementation Details:** v1 covers four model families from 3B–32B and two 5K-sample datasets plus detection studies. Later appendices examine DP-SGD, LoRA, quantization and safety alignment; later numbers are not backported.
- **Evaluation Contract:** query match ratio/BLEU, downstream utility and black-box access. High extraction is conditional on the constructed backdoor, not prevalence evidence for open models.
- **Baselines / Ablations / Sensitivity / Overhead:** clean/non-backdoored paths, model sizes, epochs and detection. v2's DP-SGD leakage/utility/roughly 1.5x training overhead remains revision evidence.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model scale/dataset size disclosed; event-time hardware/precision/serving contract incomplete.
- **What It Proves / Does Not Prove:** the attack is constructible and ordinary tuning need not erase it; it does not show clean models routinely steal data or that rates generalize.
- **Limitations / Threats:** two datasets, query-only extraction focus, constructed attacker, similarity measurement and revision drift.
- **Trade-offs / New Failure Modes:** provenance/scanning/DP add cost and may reduce utility; behavioral scans can miss adaptive triggers; signatures cannot make malicious weights benign.
- **Where the Previous Design Still Applies:** versioning remains necessary for reproducibility but insufficient for trust; internally trained bases change likelihood, not proof obligations.
- **Evolution Relationship:** `Direct Evolution`: versioned checkpoint → provenance-attested checkpoint → behavioral/supply-chain gate before private tuning.
- **ROADMAP / Adjacent Chapters:** owner `PLATFORM-SECURITY` Ch72; handoff `PLATFORM-MODEL-REGISTRY` Ch59, `TRAIN-SFT` Ch29, `TRAIN-LORA` Ch30.
- **Existing Coverage / Integration Decision:** `Integrate — New Mechanism` candidate for model supply-chain threat modeling.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: false-negative-bounded scanning and registry trust-domain/data-class contracts.

### How Should We Enhance the Safety of Large Reasoning Models — 22/30

- **Candidate / Week / Score:** LRM safety SFT empirical study / W21 / `3/3/3/4/5/4 = 22`.
- **Source Family ID / Type:** `LRM-SAFETY-SFT-2505.15404`; primary paper plus released code/data.
- **Event Date / Revision:** v1 2025-05-21; v2 2026-04-20 / ACL 2026. Event claims are pinned to v1.
- **Direct Primary Sources:** https://arxiv.org/abs/2505.15404, https://arxiv.org/pdf/2505.15404v1 and linked artifact.
- **Access / Full-read Coverage:** Verified with version boundary: v1 PDF and current paper/revision metadata across setup, five risky patterns, short/template reasoning, ablations and limitations.
- **Original Problem:** distilling apparently safe long reasoning responses can preserve risky trace patterns and fail to teach safer behavior.
- **Why the Previous Design Was Reasonable:** teacher imitation is simple, auditable and more stable/cheap than safety RL.
- **Changed Constraint:** safety depends on reasoning-data structure/filtering, not only final refusal; reasoning length is not itself a safety guarantee.
- **Mechanism:** identify five risky patterns, filter/rewrite distilled traces, compare default long CoT with short/template reasoning and ablate SFT recipe choices.
- **State Ownership:** data pipeline owns taxonomy/filtering/trace version; trainer owns SFT config; evaluator owns harmful-query labels and attack/refusal operating points.
- **Control / Data Flow:** harmful prompt → teacher trace → pattern label/filter/rewrite → SFT → reasoning model → safety/capability evaluation.
- **Implementation Details:** event-time scope is 7B reasoning models and SFT branches; released artifacts support recipe inspection.
- **Evaluation Contract:** safety/attack behavior and capability retention on selected harmful/reasoning tasks; production serving hardware/precision/concurrency/SLO are not claimed.
- **Baselines / Ablations / Sensitivity / Overhead:** default CoT, filtered/revised, short/template and config ablations; authors limit ablation to 7B and leave RL-based safety open.
- **What It Proves / Does Not Prove:** data/trace patterns matter and longer reasoning is unnecessary for measured safety; it does not prove template reasoning universally safe or SFT sufficient for agents.
- **Limitations / Threats:** 7B-only ablations, selected taxonomy/tasks, teacher/filter bias, SFT-only scope and v1/v2 drift.
- **Trade-offs / New Failure Modes:** filtering discards useful data; templates overfit refusal patterns; safety gain may hide capability loss or fail adaptively.
- **Where the Previous Design Still Applies:** direct distillation remains a baseline with independently audited teacher data; runtime authorization remains outside SFT.
- **Evolution Relationship:** final-answer SFT → trace-aware curation → independent runtime policy/evaluation.
- **ROADMAP / Adjacent Chapters:** owner `TRAIN-SFT` Ch29; handoff `PLATFORM-SECURITY` Ch72 and `PLATFORM-EVALUATION-SYSTEM` Ch66.
- **Existing Coverage / Integration Decision:** `Emerging / Experimental`; not a universal safety recipe.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: out-of-sample predictive value of five patterns and RL/larger-scale replication.

### This Time is Different / Toto + BOOM — 26/30

- **Candidate / Week / Score:** observability TSFM and benchmark / W21 / `4/4/4/5/5/4 = 26`.
- **Source Family ID / Type:** `TOTO-BOOM-2505.14766`; paper, open model/inference/eval and benchmark.
- **Event Date / Revision:** v1 2025-05-20; v2 2025-11-04. W21 owns v1; v2 is revision evidence.
- **Direct Primary Sources:** https://arxiv.org/abs/2505.14766, https://arxiv.org/html/2505.14766v1 and linked Hugging Face/GitHub artifacts.
- **Access / Full-read Coverage:** Verified across v1 architecture/training/evaluation/appendices, current revision, BOOM docs and artifact surface.
- **Original Problem:** per-metric and general TSFMs are poorly matched to multivariate observability telemetry with heterogeneous scale, missingness and correlations.
- **Why the Previous Design Was Reasonable:** per-series statistical models are cheap/interpretable for stable metrics; general TSFMs avoid bespoke maintenance.
- **Changed Constraint:** fleets create many correlated, nonstationary metrics, demanding observability-specific representation and evaluation.
- **Mechanism:** Toto is a 151M decoder-only TSFM with observability-oriented input handling/normalization; BOOM contains 350M observations across 2,807 Datadog telemetry series.
- **State Ownership:** telemetry pipeline owns timestamp/schema, missingness, normalization and windows; model owns forecast state; incident truth/alert policy remain outside it.
- **Control / Data Flow:** typed metrics → window/normalize → Toto context → forecast → error/evidence aggregation → separate anomaly/alert policy.
- **Implementation Details:** pretraining mixes observability, public and synthetic data; weights, inference/eval scripts and BOOM data/code are Apache-2.0 artifacts.
- **Evaluation Contract:** BOOM and public forecasting benchmarks with MAE/MSE and disaggregated series properties. v2 profiles one A100 40GB, context 2,048 and horizon 480; those compute values are revision evidence.
- **Baselines / Ablations / Sensitivity / Overhead:** statistical/general TSFMs, architecture/data-mixture ablations, BOOM/public comparisons and variate-scaling compute. Forecasting is not incident diagnosis.
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model size and later profiling partly disclosed; full v1 topology, precision, concurrency, alert latency and SLO incomplete.
- **What It Proves / Does Not Prove:** observability is a distinct workload and author forecasting gains hold under stated contracts; forecast error does not equal root-cause or alert quality.
- **Limitations / Threats:** one vendor's telemetry, leakage/representativeness, thresholding and no independent replication.
- **Trade-offs / New Failure Modes:** shared model reduces bespoke maintenance but adds drift, schema coupling, inference cost and false confidence.
- **Where the Previous Design Still Applies:** seasonal/statistical rules remain preferable for stable low-dimensional safety-critical metrics.
- **Evolution Relationship:** `Alternative Branch`: per-series model → general TSFM → observability-specialized TSFM; alert/evidence stays separate.
- **ROADMAP / Adjacent Chapters:** owner `PLATFORM-MONITORING` Ch67; handoff Ch66, Ch69 and Ch73.
- **Existing Coverage / Integration Decision:** `Integrate — New Mechanism` candidate as workload-contract evidence, not a monitoring replacement.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: forecast-to-alert calibration and cross-tenant/vendor/topology transfer.

### AceReason-Nemotron — 25/30

- **Candidate / Week / Score:** AceReason-Nemotron / W21 / `4/4/5/4/4/4 = 25`.
- **Source Family ID / Type:** `ACEREASON-NEMOTRON-2505.16400`; NVIDIA paper plus released models.
- **Event Date / Revision:** v1 2025-05-22, v2 2025-05-29, v3 2025-06-05. W21 is pinned to v1; later pass@1024 additions are revision evidence.
- **Direct Primary Sources:** https://arxiv.org/abs/2505.16400, https://arxiv.org/html/2505.16400v1 and linked NVIDIA Hugging Face models.
- **Access / Full-read Coverage:** Verified across v1 GRPO/rewards, data curation, curriculum, evaluation, difficulty/length/on-policy/domain-order ablations, appendices and model release.
- **Original Problem:** public reasoning results omit enough data/training detail to separate RL gains from a strong distilled initialization.
- **Why the Previous Design Was Reasonable:** SFT/distillation is stable and compute-efficient for 7B/14B and remains the correct baseline.
- **Changed Constraint:** push beyond distilled policy with verifiable math/code outcomes while avoiding long-rollout instability and false reward.
- **Mechanism:** start from DeepSeek-R1-Distill-Qwen-7B/14B; math-only GRPO with exactly one update per rollout group and staged 8K→16K→24K→32K difficulty curriculum; then code-only RL with executable tests.
- **State Ownership:** trainer owns policy/reference versions, rollout groups and curriculum; SymPy/sandbox verifiers own binary outcome truth; vLLM owns rollout execution.
- **Control / Data Flow:** curated prompt + answer/tests → group rollouts → math/code verification → normalized advantage → one update → stage/domain transition.
- **Implementation Details:** veRL/token-level GRPO, vLLM 0.7.3, beta/KL and entropy-loss coefficient 0, batch 128, group 8 at 8K and 16 thereafter, AdamW LR 1e-6, 128 H100s. Math verifier pins antlr/SymPy; code uses full test cases.
- **Evaluation Contract:** temperature 0.6, top-p 0.95, max 32,768; AIME24/25, MATH500, HMMT/BRUMO, LiveCodeBench, EvalPlus and Codeforces with avg@k/pass@1.
- **Baselines / Ablations / Sensitivity / Overhead:** distilled starts, SFT/RL and same-scale models; hard/easy filtering, 8K start/length extension, multiple versus single updates, math→code stages. Authors attribute roughly 80% of RL time to generation.
- **What It Proves / Does Not Prove:** verifiable RL improves the stated 7B/14B bases under this recipe; it does not prove universal RL superiority, optimal curriculum or complete verifier coverage.
- **Limitations / Threats:** two bases/scales, author-curated verifiable prompts, possible contamination, test-suite false results and 128-H100 reproducibility cost.
- **Trade-offs / New Failure Modes:** rollout cost, entropy collapse under stale/multiple updates, curriculum overfit and reward hacking through weak tests.
- **Where the Previous Design Still Applies:** distillation/SFT under smaller compute, weak verifiers or sufficient teacher behavior.
- **Evolution Relationship:** `Direct Evolution`: distilled base → verifiable math RL → executable code RL.
- **ROADMAP / Adjacent Chapters:** owner `TRAIN-GRPO` Ch33; adjacent Ch29, Ch31–34 and Ch36.
- **Existing Coverage / Integration Decision:** `Refine — Existing Argument`; keep verifier quality and policy freshness explicit.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: compute-matched distillation and distributed policy-staleness contracts.

### Tool-Star — 29/30

- **Candidate / Week / Score:** Tool-Star / W21 / `5/5/5/4/5/5 = 29`.
- **Source Family ID / Type:** `TOOL-STAR-2505.16410`; primary paper plus implementation.
- **Event Date / Revision:** v1 and only version 2025-05-22; paper is marked work in progress.
- **Direct Primary Sources:** https://arxiv.org/abs/2505.16410, https://arxiv.org/html/2505.16410v1 and linked repository.
- **Access / Full-read Coverage:** Verified across trajectory synthesis, filtering, cold-start SFT, hierarchical rewards, GRPO/self-critic DPO, inference recovery, benchmarks, ablations/scaling, implementation appendices and limitations.
- **Original Problem:** prompts do not reliably teach when to select/combine/recover from several tools; single-tool RL has simpler credit assignment.
- **Why the Previous Design Was Reasonable:** prompt-only or one-tool flows are cheap/modular and remain best for narrow deterministic tasks.
- **Changed Constraint:** open-ended tasks combine search, browsing and code; observations/errors are mutable environment state and credit spans calls.
- **Mechanism:** synthesize/filter tool trajectories, cold-start SFT, then alternate GRPO under hierarchical rule rewards with self-critic DPO. Training uses search/browser/code; inference adds debugger, rule-based backtracer and chain refiner.
- **State Ownership:** runtime owns registry, permission, provenance, sandbox and retry/rewind; policy proposes calls; reward code owns answer/format/collaboration credit; trainer owns policy/reference versions.
- **Control / Data Flow:** query → tool proposal → host execution → observation → repeat → reward/GRPO → sampled preference pair/DPO; failures route through debugger/backtracer/refiner.
- **Implementation Details:** Qwen2.5/Llama 0.5B–3B; tool outputs masked from loss. Self-critic DPO: LR 5e-7, cosine, 0.1 warmup, ZeRO-3, FlashAttention 2, global batch 64, bf16, context 4,096, beta 0.3. GPU model/count undisclosed.
- **Evaluation Contract:** ten main math/knowledge benchmarks plus GAIA/HLE; Qwen2.5-72B judge for computational reasoning and token-F1 for QA. Wikipedia-2018/E5 supports four QA tasks; others may use web/browser.
- **Baselines / Ablations / Sensitivity / Overhead:** backbone, RAG, search/code assistants, multi-tool prompting/ReCall; remove cold start, hierarchical reward or self-critic; scale only to 3B. Helper/tool token, latency and cost are not fully normalized.
- **What It Proves / Does Not Prove:** the full package improves author results and major stages contribute; it does not isolate policy-only gain or prove safe/faithful/general tool use.
- **Limitations / Threats:** work-in-progress, small models, judge/corpus dependence, helper-model confounding, undisclosed hardware, no side-effect safety evaluation.
- **Trade-offs / New Failure Modes:** more calls, credit/non-determinism, search poisoning, browser-summary error, unsafe code, wrong rewind and lossy chain refinement.
- **Where the Previous Design Still Applies:** prompt/single-tool deterministic workflows under known call graphs, strict latency and side effects.
- **Evolution Relationship:** `Layering`: tool proposal → observed tool state → multi-tool training → failure-aware workflow; more tools are not monotonic progress.
- **ROADMAP / Adjacent Chapters:** owner `AGENT-TOOL-CALLING` Ch78; handoff Ch33, Ch34, Ch72 and Ch81.
- **Existing Coverage / Integration Decision:** `Integrate — New Mechanism`; keep host control separate from model learning.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: full helper/tool cost accounting and authorization/rollback around learned backtracking.

### NovelSeek / InternAgent title-lineage family — 26/30

- **Candidate / Week / Score:** NovelSeek (later InternAgent) / W21 / `4/4/5/4/5/4 = 26`.
- **Source Family ID / Type:** `NOVELSEEK-INTERNAGENT-2505.16938`; primary multi-agent system paper, project page and generated/baseline code.
- **Event Date / Revision:** v1 2025-05-22 and v2 2025-05-25 are W21; v3 2025-07-22 renames to InternAgent. W21 title/numerics are pinned to NovelSeek v1/v2. One family, not two events.
- **Direct Primary Sources:** https://arxiv.org/abs/2505.16938, https://arxiv.org/html/2505.16938v1, current v3, project page and linked repository.
- **Access / Full-read Coverage:** Verified but `Disputed` at revision boundary. v1 architecture/roles/formulas/debug/planning, 12 setups/metrics, implementation, results/cost, ablations, human evaluation, conclusion and repository were read; v3 title/metadata checked.
- **Original Problem:** idea-only agents do not close a research loop; hypotheses must become code, experiments, evidence and revision.
- **Why the Previous Design Was Reasonable:** human-led experiments with LLM assistance preserve judgment for small, complex or high-cost tasks.
- **Changed Constraint:** heterogeneous repo-level tasks require artifact state, experiment history and human feedback across specialized handoffs.
- **Mechanism:** survey/code-review agents construct context; idea agents generate/evolve proposals with human feedback; methodology agent makes executable plans; planning/coding/debug agents run multi-round experiments and adapt from errors/metrics while recording decisions.
- **State Ownership:** survey archive owns literature/provenance; repo/sandbox owns code/environment; workflow ledger owns configs, metrics and decisions; models only propose mutations; human experts accept.
- **Control / Data Flow:** task+repo → survey/review → idea tree → critique → methodology → plan → code mutation → sandbox → metric/error → adaptive next plan → retained artifact.
- **Implementation Details:** v1 uses GPT-4o for survey/review/idea/orchestration and Claude 3.7 Sonnet for coding/debug; 50 papers, 15 initial ideas, three descendants each, top five, up to four evolution rounds, four debug attempts, Aider/OpenHands caps five/three.
- **Evaluation Contract:** 12 chemistry/molecular/power/time-series/genomics/NLP/vision/point-cloud/VLM tasks with native metrics, baseline/Dolphin comparisons, ten ideas per main task and runtime/cost/executable-improvement rates. A100-hours and API costs are separate.
- **Baselines / Ablations / Sensitivity / Overhead:** baseline, Dolphin, selected AI-Scientist-V2/AI-Researcher, adaptive-evolution ablation and repeated few-shot chemistry. Not every task has matched/repeated evidence.
- **What It Proves / Does Not Prove:** the durable idea→method→code→experiment loop yields executable improvements in disclosed tasks; it does not establish autonomous truth/novelty, independent reproducibility or human superiority.
- **Limitations / Threats:** heterogeneous metrics/baselines, small runs, proprietary models, leakage, selection/judge bias and incomplete rollback/security.
- **Trade-offs / New Failure Modes:** cost, experiment-selection bias, environment drift, metric gaming, unsafe mutations and compounding handoff errors.
- **Where the Previous Design Still Applies:** human-led workflow for wet-lab, safety-critical/high-cost or non-executable evidence.
- **Evolution Relationship:** `Direct Evolution`: idea → method → durable experiment workflow → evidence-driven revision; multi-agent roles are layering.
- **ROADMAP / Adjacent Chapters:** owner `AGENT-WORKFLOW` Ch81; handoff Ch79, Ch82, Ch66 and Ch72.
- **Existing Coverage / Integration Decision:** `Integrate — New Mechanism` candidate; retain `Disputed` title/numeric boundary.
- **Changed Files / Open Questions:** Weekly only; Books frozen. Open: replayable artifact schema and archived v1→v2→v3 diff.

## Final low-score verification ledger

Dimensions are `Technical Novelty / System Impact / Practical Value / Source Reliability / Project Relevance / Longevity`, each 0–5. These rows are archive decisions, not Full Source Reviews. A low decision is closed only where exact identity/date plus the primary abstract or official announcement is sufficient to establish the narrow rejection boundary; no unavailable Method/result is inferred.

| Candidate | Six-dimensional scores | Total | Evidence available | Rejection boundary |
|---|---:|---:|---|---|
| Gemini Diffusion experimental preview | 3/2/3/5/3/3 | 19 | Exact Google announcement, 2025-05-20 | Experimental product fact; architecture, training and reproducible workload contract not disclosed. |
| Gemini universal-assistant/world-model vision | 2/2/2/5/3/4 | 18 | Exact Google vision post, 2025-05-20 | Strategic direction, not a released mechanism or evaluated system artifact. |
| Google generative-media launch (Veo 3 + Imagen 4) | 3/2/2/5/3/3 | 18 | Exact official launch post, 2025-05-20 | Version/product capabilities without sufficient public mechanism and comparable evaluation contract. |
| Gemma 3n preview | 3/3/3/5/3/2 | 19 | Exact developer preview, 2025-05-20 | Preview behavior/specification; later full-release facts cannot be backported to W21. |
| Transformers v4.52.1 | 1/3/4/5/3/2 | 18 | Exact GitHub release/tag, 2025-05-22 | Patch/release fact; no independent long-lived mechanism conclusion. |
| JAX v0.6.1 | 1/3/3/5/3/2 | 17 | Exact changelog, 2025-05-21 | Breaking release fact, important operationally but not a new AI-System mechanism. |
| FullFront | 2/2/2/5/4/4 | 19 | Exact paper/artifact, 2025-05-23 | Narrow benchmark; useful archive evidence but insufficient to change the platform/evaluation design argument. |
| MSPGT | 3/2/2/4/4/4 | 19 | Exact arXiv identity/date and abstract/metadata | Theoretical interpretability proposal; full Method/intervention/revision evidence was not available in this lane, so all mechanism/numeric claims remain frozen. Abstract is sufficient only to reject below 20 as unvalidated theory. |
| MUG-Eval | 3/2/3/4/4/3 | 19 | Exact arXiv identity/date and abstract/metadata | Multilingual proxy benchmark with reported correlation; full task construction/sensitivity evidence unavailable here. Abstract is sufficient only for a narrow below-20 relevance decision, not for adopting the proxy. |
| Model Immunization to Combat Falsehoods | 2/2/2/4/4/4 | 18 | Exact position paper, 2025-05-23 | Research agenda plus illustrative case, not a mature validated system mechanism. |
| MemeReaCon | 2/2/3/4/4/4 | 19 | Exact paper identity/date and abstract | Narrow contextual-meme benchmark; does not yet alter the general multimodal/context evaluation contract. |

Low arithmetic result: **11/11 totals recomputed and matched**. `Review Pending=0` for the low ledger. MSPGT and MUG-Eval retain explicit evidence limits rather than an invented full-read status.

## Owner corrections, spillback and exclusions

- W21 owner spillbacks found in W22 and restored to W21: `TabSTAR` (2505.18125), `QwenLong-L1` (2505.17667), `Quartet` (2505.14669), `Data-centric compression` (2505.19147), `Embodied MEMENTO` (2505.16348), `PATS` (2505.19250), `Flex-Judge` (2505.18601), `VerIPO` (2505.19000), and `DeepResearchGym` (2505.19253).
- `BARREL` is arXiv:2505.13529 v1 2025-05-18. It is a W20 owner and must appear in W21 only as an explicit cross-week spillback/exclusion.
- `ColorBench` is arXiv:2504.10514 (April owner); `PRING` first appeared 2025-05-26 (W22). The combined “Color/PPI” row was never a canonical family and is removed from W21 scoring.
- “MindGap” and “Clinical prediction commentary” were non-unique discovery labels with no exact W21 identity; they are excluded, not silently scored.
- “Teaching Models to Lie” remains a **P0 Identity** discovery gap. Nearby deception/backdoor papers are not substituted. Required material: original title and author, arXiv/DOI, or the original discovery export/link.

## Explicit version/dispute ledger

| Family | Stable identity | Disputed boundary | Final disposition |
|---|---|---|---|
| NovelSeek / InternAgent | arXiv:2505.16938, v1 2025-05-22 | Later rename to InternAgent | Mechanism review retained; W21 title pinned to v1 lineage. |
| One RL to See Them All | arXiv:2505.18129, v1 2025-05-23 | Title/revision lineage and event-time numeric claims | Mechanism retained; event-time numbers frozen pending v1 PDF pin. |
| TemplateRL / TAPO | arXiv:2505.15692, v1 2025-05-21 | Title changed from template-guided framing to TAPO lineage | Mechanism retained; v1 title/numerics remain disputed until v1 PDF is archived. |
| SpatialScore | arXiv:2505.17012, v1 2025-05-22 | v1 and current corpus/task/tool counts differ | Mechanism retained; no current counts backported to W21. |
| When LLMs Admit Mistakes / retraction | arXiv:2505.16170, v1 2025-05-21 | Current v4 is 2026 | v1 mechanism retained; later results treated as revision evidence only. |

Disputed count: **5**. None is `Review Pending`; each has a stable primary identity and a frozen event-time claim boundary.

## Candidate Evidence Gate

```text
Canonical scored owners: 127/127
25–30: 60
20–24: 56
<20: 11
Retained Full Source Review: 116/116
Low closures: 11/11
Review Pending: 0
Disputed: 5 (source-complete; event-time boundary frozen)
P0 noncanonical identity gap: 1
Candidate Evidence Gate: PASSED
Discovery / Archive Completion: CONDITIONAL
Historical Books Gate: CLOSED
```

## Evidence Level

- 官方 Blog / Release 只证明公开版本事实；内部机制未披露时固定为 `Version Fact / Mechanism Not Disclosed`。
- arXiv 作者实验默认是条件化 evidence，不等于独立复现；每个 packet 明确证明与未证明内容。
- 五个 dispute 均已绑定稳定 identity 与 revision boundary；当前来源可读，不计为 pending。
- 跨来源技术关系以 `Direct Evolution`、`Layering / Dependency`、`Alternative Branch` 或 `Explanatory Analogy` 明示。

## Cross-Week Deduplication

- W22 spillback 回拨 W21：TabSTAR、QwenLong-L1、Quartet、Data-centric compression、Embodied MEMENTO、PATS、Flex-Judge、VerIPO、DeepResearchGym。
- BARREL (`2505.13529`) 的 v1 日期为 2025-05-18，owner 是 W20；W21 只保留 routing note，不计分也不计 strict packet。
- NovelSeek / InternAgent、OneRL、TemplateRL / TAPO、SpatialScore、When LLMs Admit Mistakes 均按同一 Source Family 处理 revision，不重复计分。
- MindGap、Clinical prediction commentary 与 Color/PPI 是不可唯一解析或跨周拼接的 discovery fragments，已排除；ColorBench 归 W16，PRING 归 W22。

## Knowledge Tree Position

116 个 retained packet 已逐项记录 Stable Node owner 与 adjacent-chapter handoff。主要 owner 分布于 `TRAIN-*`、`INFER-*`、`MULTIMODAL-*`、`PLATFORM-*` 与 `AGENT-*`；一个机制只保留一个 canonical owner，跨章只作 handoff。

## Recommended Action

- Candidate evidence 已闭合，可作为后续 Source-Family Books Gate 的输入；本轮不执行 Books Integration。
- 对五个 dispute 保留现有机制结论，但冻结 event-time title/numerics，不以后续 revision 回写 2025 事实。
- 对 P0 `Teaching Models to Lie` 只接受可唯一识别材料，不以相邻 deception/backdoor paper 替代。

## Event-Date Daily Decision

Historical Backfill 不补造 Daily；所有事件日期、revision 与 evidence boundary 直接记录在本 Weekly。

## Books Integration Decision

`Books Frozen — Historical Books Gate Closed`。Candidate Evidence Gate 通过不等于 Archive Completion；本周未修改 Books。

## Ignored Noise

- 忽略二手转述、旧内容重发、无 primary identity 的标题片段、缺条件 benchmark 宣传与纯可用性更新。
- discovery 排名、引用量和后续 revision 不替代 first-public date、机制正文与事件时证据。

## Repository Changes

- 以 127-row canonical ledger 替换旧三项 provisional baseline。
- 写入 116 份独立 retained Full Source Review、11 个 low closures、五个 dispute boundary、W20/W22 routing 与一个账外 P0 material request。
- 未修改 Books、年度索引、ROADMAP、DECISIONS 或其他 Weekly。

## Open Questions

- `Teaching Models to Lie` 的精确 title、authors、arXiv/DOI 或原始 discovery-export row 是什么？
- 是否能归档 OneRL、TemplateRL/TAPO 与 SpatialScore 的 event-time v1 PDF，以将冻结边界转为可重放 artifact？
- llm-d 是否存在 2025-05 launch-time commit/tag matrix，可进一步固定 component/API compatibility？

## Missing Material Request

```text
Priority: P0 Identity
Week: 2025-W21
Known label: Teaching Models to Lie
Missing: exact title plus author, arXiv/DOI, official project link, or original discovery-export row
Why insufficient: multiple deception/backdoor papers are plausible; substitution would fabricate identity/date/score
Acceptable alternative: original result URL, PDF title page, BibTeX, screenshot with title/authors, or archive export
Suggested filename: 2025-W21-teaching-models-to-lie-identity.*
Recovery audit: identity/date/revision, dedup, six-dimensional score, and strict review if score >=20
```

## Sources

Primary-source URLs are preserved in the canonical ledger and each Full Source Review. Discovery-only indexes were used for recall/dedup and are not cited as mechanism evidence.
