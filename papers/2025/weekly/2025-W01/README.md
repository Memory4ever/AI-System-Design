# AI Research Weekly — 2025-W01

> Coverage Window: 2024-12-30～2025-01-05
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Rebuild Started: 2026-08-17
> Accessed: 2026-08-17
> Weekly Evidence Gate: Passed — 37/37 Full Source Reviews; 13/13 low-score dispositions; adaptive spillback closed
> Books Integration: Deferred by user request

## Executive Summary

本周旧档案只保留 Titans，明显低估了同周的 research density。重新按 first-public date 回放后，
已确认至少四条长期系统路线：test-time memory、reasoning-aware serving、software-engineering
Agent 的 environment/verifier contract，以及 reasoning token efficiency。多模态方向又恢复出五个达到
`20+` 的独立机制节点：对象身份与运动控制解耦、object-centric video representation、视觉 tokenizer
与 generator 的 latent geometry contract、多视觉 encoder 融合，以及 real-world video restoration 的
时空窗口与 causal VAE 设计。它们补足了旧档案最明显的召回缺口。

`Found` 与 `Full Source Review` 分开计数；原有 23 项 `20+` 候选已完成全文、评分与 Source Family 复核，
5 项低分候选也已完成 identity、日期与拒绝理由核验。W02 discovery replay 随后发现，Hugging Face
在 2025-01-06～09 才列出一批 arXiv v1 实际发表于 2025-01-01～05 的论文；它们必须按 first-public
date spill back 到 W01。复核后新增 14 项 `20+` Full Source Review 和 8 项低分 rejection，候选总账
扩展为 37 项完整审计与 13 项低分记录。DPO-Kernels 直到 01-09 才进入聚合页，证明固定“三工作日”
grace 仍会漏项；本周改以连续两个后续 business-day 页面不再发现 W01 owner 作为 closure 条件。
当前 Gate 暂保持 Open，直到新增 packet、分母与跨周去重全部通过验收；本阶段不修改 Books。

## Coverage Window and Limitations

- ISO week-year 采用 Monday～Sunday；W01 包含 2024-12-30 与 2024-12-31。
- 事件归属采用官方发布日期、GitHub Release 时间或 arXiv v1，而不是 Hugging Face 收录日、arXiv
  编号年份或后续 revision。
- 固定来源顺序为模型与研究机构 → arXiv / 学术来源 → AI Infra 与工程项目。
- Google Scholar、OpenAlex、DBLP、Semantic Scholar 与 Hugging Face 用于 discovery / 去重；机制结论
  回到 arXiv、作者 artifact 或官方工程材料。Crossref 只做 metadata 交叉检验。
- 当前可访问 HTML 常为后续 revision；凡用 v2 补充实验或 limitations，都会与本周事件时 v1 区分。
- discovery replay 不采用固定三工作日截断；任何 spillback 均以 arXiv v1 或官方 first-public date 为 owner，
  不以榜单日期为 owner。本轮回放到 2025-01-09 仍发现 DPO-Kernels（v1 2025-01-05），随后 01-10 与
  01-13 连续两个 business-day 页面不再出现 W01 owner，才作为 grace-window closure 证据。
- 历史回填不补造 Daily；本周未进入 Books Integration。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序复查 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、
Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、
InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- Microsoft RD-Agent 的 2025-01-02 英文说明已完成 identity/date 核验：它复述的是 2024-09-12
  中文官方说明所披露的同一 Research/Development feedback loop，GitHub release ledger 中首个可见
  `v0.3.0` 也发布于 2024-10-21。2025-01-02 没有可核验的新 tag、论文或机制，因此判定为旧内容
  再发布，回拨 2024 owner week，不在 W01 重复计分。
- Microsoft Research 的 WeAudit 论文 v1 于 2025-01-02 首次公开，已按完整 HCI 论文读取，保留为
  user-engaged audit workflow Source Family；不是把 Microsoft 摘要当 primary evidence。
- Photorealistic Avatar Challenge 于 2025-01-03 公布了 causal、1080p/30FPS、RTX 4090、blind test 与
  subjective MOS 的完整 workload/evaluator contract，作为官方 evaluation-design event 审计；它没有模型结果。
- “Accelerating Multilingual RAG Systems”网页在 2025-01-02 重新呈现，但官方 video owner date 为
  2024-11-29，内容又是 MIRACL/NoMIRACL/MIRAGE-Bench 的既有综合，回拨 2024 owner week。

## 2. 论文与学术来源

### Discovery Census

以下表格是本周候选账本，不等于全部已经通过 Evidence Gate。

| Candidate | Primary ID | First Public | State | Notes |
| --- | --- | --- | --- | --- |
| Titans: Learning to Memorize at Test Time | arXiv:2501.00663 | 2024-12-31 | Full Source Review Complete | 模型内部 test-time memory |
| Efficiently Scaling LLM Reasoning with Certaindex / Dynasor | arXiv:2412.20993 | 2024-12-30 | Full Source Review Complete | reasoning-aware serving |
| Training Software Engineering Agents and Verifiers with SWE-Gym | arXiv:2412.21139 | 2024-12-30 | Full Source Review Complete | environment、Agent、verifier 联合 contract |
| Do NOT Think That Much for 2+3=? | arXiv:2412.21187 | 2024-12-30 | Full Source Review Complete | reasoning efficiency 与 length preference |
| TangoFlux | arXiv:2412.21037 | 2024-12-30 | Full Source Review Complete | flow matching 与 audio preference construction |
| HumanEval Pro and MBPP Pro | arXiv:2412.21199 | 2024-12-30 | Full Source Review Complete | self-invoking code evaluation |
| HUNYUANPROVER | arXiv:2412.20735 | 2024-12-30 | Full Source Review Complete | data synthesis 与 guided tree search |
| 2.5 Years in Class | arXiv:2501.00958 | 2025-01-01 | Full Source Review Complete | instructional-video multimodal corpus |
| CodeElo | arXiv:2501.01257 | 2025-01-02 | Full Source Review Complete | executable competition-code evaluation |
| LTX-Video | arXiv:2501.00103 | 2024-12-30 | Full Source Review Complete | realtime video latent diffusion |
| MLLM-as-a-Judge for Image Safety | arXiv:2501.00192 | 2024-12-31 | Full Source Review Complete | policy objectification、cascaded judge 与 synthetic-label boundary |
| ProgCo | arXiv:2501.01264 | 2025-01-02 | Full Source Review Complete | pseudo-program verification 与 verifier/response dual refinement |
| A3: Android Agent Arena | arXiv:2501.01149 | 2025-01-02 | Full Source Review Complete | dynamic GUI environment、harness/evaluator boundary 与 revision evolution |
| Dynamic Scaling of Unit Tests for Code Reward Modeling | arXiv:2501.01054 | 2025-01-02 | Full Source Review Complete | executable reward、verifier budget 与 metric contract |
| Understanding and Mitigating Bottlenecks of State Space Models | arXiv:2501.00658 | 2024-12-31 | Full Source Review Complete | contraction、recency、depth 与 over-smoothing 的条件化关系 |
| TAPE: Contextualized Equivariant Positional Encoding | arXiv:2501.00712 | 2025-01-01 | Full Source Review Complete | layer-wise contextual position state 与 equivariant addressing |
| VideoAnydoor | arXiv:2501.01427 | 2025-01-02 | Full Source Review Complete | 对象 identity 与 trajectory-conditioned motion 解耦 |
| VideoRefer Suite | arXiv:2501.00599 | 2024-12-31 | Full Source Review Complete | object-centric video data、representation 与 evaluation contract |
| Reconstruction vs. Generation / VA-VAE + LightningDiT | arXiv:2501.01423 | 2025-01-02 | Full Source Review Complete | visual tokenizer latent geometry 与 generator convergence |
| Unifying Specialized Visual Encoders / MERV | arXiv:2501.01426 | 2025-01-02 | Full Source Review Complete | 多视觉 expert 的 token alignment、fusion 与 placement trade-off |
| SeedVR | arXiv:2501.01320 | 2025-01-02 | Full Source Review Complete | real-world video restoration、3D window attention 与 causal VAE |
| WeAudit | arXiv:2501.01397 | 2025-01-02 | Full Source Review Complete | user-engaged audit 的 investigate/deliberate/evidence workflow |
| CVPR 2025 Photorealistic Avatar Challenge | Microsoft Research official program | 2025-01-03 | Full Source Review Complete | causal realtime workload 与 subjective evaluation contract |
| EnerVerse | arXiv:2501.01895 | 2025-01-03 | Full Source Review Complete | chunk-wise video diffusion、sparse memory 与 action policy coupling |
| Scaling Laws for Floating Point Quantization Training | arXiv:2501.02423 | 2025-01-05 | Full Source Review Complete | precision、scale 与 quantization target 的条件化 scaling law |
| VisionReward | arXiv:2412.21059 | 2024-12-30 | Full Source Review Complete | decomposed multimodal reward 与 Pareto preference construction |
| BoxingGym | arXiv:2501.01540 | 2025-01-02 | Full Source Review Complete | active experiment design 与 executable scientific evaluation |
| VITA-1.5 | arXiv:2501.01957 | 2025-01-03 | Full Source Review Complete | vision、speech input/output 的 native token pipeline |
| AutoPresent | arXiv:2501.00912 | 2025-01-01 | Full Source Review Complete | executable artifact generation、render feedback 与 evaluator contract |
| ToolHop | arXiv:2501.02506 | 2025-01-05 | Full Source Review Complete | locally executable multi-tool benchmark 与 invocation failure taxonomy |
| Personalized Graph-Based Retrieval | arXiv:2501.02157 | 2025-01-04 | Full Source Review Complete | graph-local profile、retrieval locality 与 identity/freshness boundary |
| Virgo | arXiv:2501.01904 | 2025-01-03 | Full Source Review Complete | textual long-thought transfer into multimodal reasoning |
| Segment-Level Direct Preference Optimization | arXiv:2501.01821 | 2025-01-03 | Full Source Review Complete | social-agent error localization 与 equal-length segment preference |
| LUSIFER | arXiv:2501.00874 | 2025-01-01 | Full Source Review Complete | multilingual encoder 到 English-centric embedding LLM 的 staged alignment |
| Auto-RT | arXiv:2501.01830 | 2025-01-03 | Full Source Review Complete | automated red-team strategy search 与 progressive reward control |
| REINFORCE++ | arXiv:2501.03262 | 2025-01-04 | Full Source Review Complete | critic-free policy optimization 的 v1 mechanism bundle |
| DPO Kernels | arXiv:2501.03271 | 2025-01-05 | Full Source Review Complete | semantic embedding、kernel transform 与 divergence selection 的 preference branch |
| Graph Generative Pre-trained Transformer | arXiv:2501.01073 | 2025-01-02 | Low-score Rejected — 19/30 | graph generation 专用 autoregressive formulation，通用系统 owner 增量有限 |
| Test-time Computing Survey | arXiv:2501.02497 | 2025-01-05 | Low-score Rejected — 19/30 | 有价值的 taxonomy，但没有独立 primary experiment 或新 mechanism |
| GS-DiT | arXiv:2501.02690 | 2025-01-05 | Low-score Rejected — 19/30 | 3D Gaussian diffusion 的领域实现，跨系统机制证据不足 |
| Graph-Aware Isomorphic Attention | arXiv:2501.02393 | 2025-01-04 | Low-score Rejected — 19/30 | graph isomorphism inductive bias，AI System longevity 较窄 |
| DepthMaster | arXiv:2501.02576 | 2025-01-05 | Low-score Rejected — 18/30 | monocular depth specialization，未形成通用 runtime/evaluation contract |
| Ingredients | arXiv:2501.01790 | 2025-01-03 | Low-score Rejected — 18/30 | 视觉生成 recipe aggregation，机制归因和长期 owner 不够清楚 |
| Generalizable Origin Identification | arXiv:2501.02376 | 2025-01-04 | Low-score Rejected — 18/30 | synthetic-image attribution 的领域检测器，威胁模型覆盖有限 |
| MagicFace | arXiv:2501.02260 | 2025-01-04 | Low-score Rejected — 17/30 | identity-specific image generation，系统设计外延有限 |
| MapEval | arXiv:2501.00316 | 2024-12-31 | Low-score Rejected — 18/30 | 领域 benchmark，未改变通用 evaluation mechanism |
| Nested Attention | arXiv:2501.01407 | 2025-01-02 | Low-score Rejected — 19/30 | 狭窄 personalization 分支，长期系统影响有限 |
| Population Aware Diffusion | arXiv:2501.00910 | 2025-01-01 | Low-score Rejected — 19/30 | time-series synthetic-data objective，领域边界较窄 |
| SeFAR | arXiv:2501.01245 | 2025-01-02 | Low-score Rejected — 18/30 | fine-grained action recognition 的 task-specific SSL 设计 |

### Cross-year Exclusions

Hugging Face 在 12 月 30～31 日重新收录了多篇更早公开的论文。以下条目不属于 W01，不在本周
重复评分：HuatuoGPT-o1（2412.18925）、1.58-bit FLUX（2412.18653）、Task Preference
Optimization（2412.19326）、Explanatory Instructions（2412.18525）、Med-MAT compositional
generalization（2412.20070）、OneKE（2412.20005）以及 OS-Genesis（2412.19723）。它们应回拨
first-public date 所属的 2024 owner week，而不是由 2025-W01 吞并。

## 3. AI Infra 与工程项目

按固定工程顺序复查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、
Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、
MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- Certaindex / Dynasor 的系统实现随论文 Source Family 联读，不重复作为 GitHub Release 计分。
- fixed-source release ledger 的相邻边界如下；边界均来自项目官方 Release 或 PyPI release history，
  不以博客转载日期推断版本事件。

| Project family | Previous boundary before W01 | Next boundary after W01 | W01 disposition |
| --- | --- | --- | --- |
| vLLM | v0.6.6, 2024-12-27 | v0.7.0, 2025-01-27 | 窗口内无 release |
| SGLang | v0.4.1, 2024-12-25 | 后续版本进入 W02+ | 窗口内无 release |
| Transformers | 4.47.1, 2024-12-17 | 4.48.0, 2025-01-10 | 窗口内无 release |
| Accelerate | 1.2.1, 2024-12-13 | 1.3.0, 2025-01-17 | 窗口内无 release |
| DeepSpeed | 0.16.2, 2024-12-18 | 0.16.3, 2025-01-21 | 窗口内无 release |
| MLX | 0.21.1, 2024-12-06 | 0.22.1, 2025-02-06 | 窗口内无 release |
| llama-cpp-python | 0.3.5, 2024-12-10 | 0.3.6, 2025-01-08 | 窗口内无 release |
| ONNX Runtime | 1.20.1, 2024-11-21 | 1.21.0, 2025-03-08 | 窗口内无 release |
| KServe | v0.14.x owner family | v0.15.0, 2025-03-31 | 窗口内无 release |

PyTorch、JAX、CUDA、Triton、NVIDIA Dynamo、TensorRT-LLM、Ray、Kubeflow、Kubernetes、
Megatron-LM、Unsloth、llama.cpp 与 OpenXLA 的官方 release/tag history 也未显示 2024-12-30～
2025-01-05 内可独立计分的 release。零散 commit/PR 不因“发生在本周”自动升级；只有形成公开、
可定位的 RFC、release 或长期机制变化才进入候选账本。

## Candidate Scoring

37 项 `20+` 候选的评分均已在 Full Source Review 后复核；其中 14 项由 2025-01-06～09 discovery
grace window spill back。低分 ledger 的 13 项也已完成 identity、日期、评分与拒绝理由核验。

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Certaindex / Dynasor | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review；Books Pending — Integration Deferred |
| SWE-Gym | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Full Review；Books Pending — Integration Deferred |
| Titans | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Full Review；Books Pending — Integration Deferred |
| EnerVerse | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Full Review；Books Pending — Integration Deferred |
| Scaling Laws for FP Quantization Training | 5 | 5 | 4 | 5 | 4 | 2 | 25/30 | Full Review；Books Pending — Integration Deferred |
| REINFORCE++ | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Full Review；Books Pending — Integration Deferred |
| DPO Kernels | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Full Review；Books Pending — Integration Deferred |
| Do NOT Think That Much | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review；Books Pending — Integration Deferred |
| Reconstruction vs. Generation / VA-VAE + LightningDiT | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Review；Books Pending — Integration Deferred |
| 2.5 Years in Class | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| VideoRefer Suite | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| Unifying Specialized Visual Encoders / MERV | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| SeedVR | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| VisionReward | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| BoxingGym | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| VITA-1.5 | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review；Books Pending — Integration Deferred |
| CodeElo | 4 | 4 | 5 | 4 | 4 | 2 | 23/30 | Full Review；Books Pending — Integration Deferred |
| Dynamic Scaling of Unit Tests | 4 | 4 | 5 | 4 | 4 | 2 | 23/30 | Full Review；Books Pending — Integration Deferred |
| TAPE: Contextualized Equivariant Positional Encoding | 5 | 4 | 3 | 4 | 4 | 3 | 23/30 | Full Review；Books Pending — Integration Deferred |
| WeAudit | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Review；Books Pending — Integration Deferred |
| LTX-Video | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review；Books Pending — Integration Deferred |
| HUNYUANPROVER | 4 | 4 | 4 | 5 | 3 | 3 | 23/30 | Full Review；Books Pending — Integration Deferred |
| AutoPresent | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review；Books Pending — Integration Deferred |
| ToolHop | 4 | 4 | 5 | 5 | 4 | 1 | 23/30 | Full Review；Books Pending — Integration Deferred |
| A3: Android Agent Arena | 4 | 4 | 4 | 4 | 4 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| State Space Model Bottlenecks | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Full Review；Books Pending — Integration Deferred |
| TangoFlux | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| ProgCo | 4 | 3 | 4 | 5 | 4 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| Personalized Graph-Based Retrieval | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| Virgo | 4 | 3 | 4 | 5 | 4 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| Segment-Level DPO | 4 | 3 | 4 | 5 | 4 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| LUSIFER | 4 | 3 | 4 | 5 | 4 | 2 | 22/30 | Full Review；Books Pending — Integration Deferred |
| Auto-RT | 4 | 4 | 4 | 5 | 4 | 1 | 22/30 | Full Review；Books Pending — Integration Deferred |
| MLLM-as-a-Judge for Image Safety | 3 | 4 | 4 | 4 | 4 | 2 | 21/30 | Full Review；Books Pending — Integration Deferred |
| HumanEval Pro / MBPP Pro | 3 | 3 | 4 | 5 | 4 | 2 | 21/30 | Full Review；Books Pending — Integration Deferred |
| VideoAnydoor | 4 | 3 | 4 | 5 | 3 | 2 | 21/30 | Full Review；Books Pending — Integration Deferred |
| CVPR 2025 Photorealistic Avatar Challenge | 3 | 3 | 4 | 5 | 3 | 2 | 20/30 | Full Review；Books Pending — Integration Deferred |

### Low-score and Engineering Exclusion Ledger

| Candidate | Score | Identity / Date Check | Rejection Reason |
| --- | ---: | --- | --- |
| Nested Attention | 19/30 | arXiv v1 2025-01-02 | query-dependent values 是可信 personalization 分支，但实验限于 SDXL faces/pets 与作者 user study，未形成跨任务 system contract |
| Population Aware Diffusion | 19/30 | arXiv v1 2025-01-01 | population loss 与 same-step sampling 有方法价值，但聚焦 time-series synthetic data，训练成本明显增加且未改变通用 AI System owner |
| MapEval | 18/30 | arXiv v1 2024-12-31 | 700 道 map reasoning benchmark 暴露能力缺口，但主要是 domain coverage 增量，没有新 evaluator/runtime mechanism |
| SeFAR | 18/30 | arXiv v1 2025-01-02 | dual temporal elements、moderate perturbation 与 teacher stabilization 属于 narrow FAR/SSL 设计，跨系统 longevity 有限 |
| finetrainers CogVideoX T2V LoRA support | 16/30 | Hugging Face project log 2025-01-03 | 工程支持事件，未披露新的训练机制、稳定 release contract 或长期系统设计变化 |
| Graph Generative Pre-trained Transformer | 19/30 | arXiv v1 2025-01-02 | graph-token ordering 与 generative pretraining 是可信任务机制，但证据集中于 graph generation，未改变通用 model/runtime contract |
| Test-time Computing Survey | 19/30 | arXiv v1 2025-01-05 | taxonomy 有长期索引价值，但属于 secondary synthesis，没有新的 primary experiment，不能用综述替代被引用论文的 Source Review |
| GS-DiT | 19/30 | arXiv v1 2025-01-05 | Gaussian-splatting diffusion 是 3D generation 分支，evaluation 与 artifact 尚不足以建立独立 AI System owner |
| Graph-Aware Isomorphic Attention | 19/30 | arXiv v1 2025-01-04 | attention 中的 graph-isomorphism bias 有方法价值，但实验与应用边界较窄，未改变当前通用 attention/system 结论 |
| DepthMaster | 18/30 | arXiv v1 2025-01-05 | monocular depth 的 diffusion-prior adaptation 属于 domain specialization，缺少跨任务 serving/evidence contract |
| Ingredients | 18/30 | arXiv v1 2025-01-03 | 汇集 image-generation training ingredients，但变量耦合使机制归因较弱，不以 recipe list 进入长期知识树 |
| Generalizable Origin Identification | 18/30 | arXiv v1 2025-01-04 | 生成图像来源识别值得安全跟踪，但 threat model、生成器覆盖与分布迁移不足以支撑通用治理结论 |
| MagicFace | 17/30 | arXiv v1 2025-01-04 | identity-conditioned generation 的局部改进，未形成可迁移的状态所有权或系统演进机制 |

## Deep Analysis

### 1. Test-time memory：从“读更多历史”到“更新执行期状态”

Titans 在 dense attention 与固定 recurrent state 之间增加可在 test time 更新的参数化 memory。
它解决的不是 durable Agent Memory，而是 sequence model 如何在有限 attention window 外保留可学习
状态。收益来自新的 state path；代价也因此变为错误写入、遗忘、更新稳定性、session ownership、
replica divergence 与 rollback。旧方案没有失效：短上下文精确依赖仍适合 dense attention，严格
provenance / delete / freshness 仍应交给外部 retrieval 或 durable memory。

### 2. Reasoning-aware serving：从固定 token budget 到可观测的动态资源分配

Certaindex 观察到 reasoning program 的答案常在预算耗尽前稳定；Dynasor 把这个 signal 提升为
early exit、token allocation 与 program-aware scheduling 的共同控制量。新机制获得更好的 deadline
attainment，却把“稳定但错误”、probe overhead、threshold calibration、gang scheduling fairness、
prefix identity 与 starvation 变成系统责任。它不是简单的“更短回答”，也不能由单个 benchmark
外推到所有 reasoning workload。

### 3. Agent capability：模型、environment、scaffold、verifier 必须联合计量

SWE-Gym 证明训练 software-engineering Agent 时，真正的训练单元不是孤立 prompt/answer，而是
repository、可执行 environment、tests、Agent scaffold、trajectory 与 verifier 的组合。更通用的
OpenHands workflow 提供灵活 action space，却增加 horizon 和训练难度；更专用的 MoatlessTools
降低搜索空间，却把更多 human engineering 固化进 harness。作者的 on-policy self-improvement 负结果
说明“有环境反馈”不自动等于稳定自举。

## Full Source Review

### Titans: Learning to Memorize at Test Time

- **Candidate / Week / Score:** Titans / 2025-W01 / 27/30。
- **Source Family ID:** `titans-miras-test-time-memory`。
- **Source Type:** 作者论文；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 于 2024-12-31；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00663；https://arxiv.org/html/2501.00663。
- **Access and Verification Status:** Verified；正文、公式、实验、ablation 与核心 appendix 可访问。
- **Full-read Coverage:** metadata、Introduction、Preliminaries、Neural Long-term Memory、三种 memory
  integration、parallelization、language/needle/BABILong/time-series/genomics evaluation、efficiency、
  ablation、Related Work、Conclusion 与核心 appendices。
- **Original Problem:** attention 保留显式 token-to-token access，却随长度扩大 compute/cache；固定
  recurrent state 成本有界，却必须把历史压进有限状态。
- **Why the Previous Design Was Reasonable:** 前者优化短中上下文高保真依赖，后者优化流式与有界内存。
- **Changed Constraint:** workload 需要累积远超局部 attention window 的历史，而又不能每次展开全部
  token pairs。
- **Mechanism:** neural memory 用 associative loss gradient 在 test time 更新 MLP fast weights；
  gradient magnitude 作为 surprise，并组合 momentum 与 data-dependent decay。三种 integration 分别
  把 memory 作为 context、layer 或 gate 与局部 attention 组合。
- **State Ownership / Control and Data Flow:** fast weights 与 short-term token window 由 model execution
  拥有；representation 形成 key/value objective，surprise 驱动写入，读出再与 attention 串联或 gated
  merge。论文未定义 tenant/session durable ownership。
- **Implementation Details:** 披露 objective、update rule、parallel scan/chunking 与 integration；未披露
  production isolation、checkpoint/rollback、错误写入检测和 replica synchronization。
- **Evaluation Contract:** language modeling、common-sense、needle、BABILong、time-series、DNA；最长
  context claim 与性能只属于作者设置。统一的 hardware、precision、batch、并发、TTFT/TPOT SLO
  contract 未完整披露，因此不外推数字。
- **What the Evidence Proves / Does Not Prove:** 证明作者设置中 online parametric memory 可与 local
  attention 组合并改善所选任务；不证明其替代 dense attention、RAG、KV cache 或 Agent durable memory。
- **Limitations / Trade-offs / Failure Modes:** synthetic retrieval 比重、同源实现与评测、production
  contract 缺失；新增污染、漂移、遗忘、跨请求泄漏、replica divergence 与 rollback 风险。
- **Where the Previous Design Still Applies:** 精确短依赖继续用 dense attention；严格 provenance、权限、
  freshness、delete 继续用 external memory；有界流式任务可用固定 recurrent state。
- **Evolution Relationship:** `Direct Evolution`（attention/recurrent memory hybrid）；与 Agent Memory 为
  `Principle Reuse`。
- **ROADMAP Node:** Owner `MODEL-LONG-CONTEXT`，Current Ch22，Legacy Ch22；handoff `AGENT-MEMORY`，
  Current Ch77，Legacy Ch73。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** multi-tenant ownership、bad-memory detection、rollback 与 replica consistency。

### Efficiently Scaling LLM Reasoning with Certaindex / Dynasor

- **Candidate / Week / Score:** Certaindex / Dynasor / 2025-W01 / 29/30。
- **Source Family ID:** `certaindex-dynasor-reasoning-aware-serving`。
- **Source Type:** 作者论文与作者 artifact；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 2024-12-30；v2 2025-05-27。事件归 v1，
  本次用 v2 HTML 补足后续实验与 limitations，但不改变事件日期。
- **Direct Primary Sources:** https://arxiv.org/abs/2412.20993；https://arxiv.org/html/2412.20993；
  https://github.com/hao-ai-lab/Dynasor。
- **Access and Verification Status:** Verified；全文、公式、系统设计、evaluation 与 appendix 可访问。
- **Full-read Coverage:** metadata、Introduction、Background、Certaindex definitions/theory、Dynasor 三层
  design、implementation、offline/online evaluation、ablation/sensitivity、appendix、limitations、code link。
- **Original Problem:** CoT、self-consistency、MCTS 与 Rebase 使用固定 token/sample budget，即使答案已经
  稳定仍继续消耗 decode compute；通用 LLM scheduler 看不到 program-level convergence。
- **Why the Previous Design Was Reasonable:** 固定预算容易隔离请求、预测资源并避免过早终止；token-level
  scheduler 对普通 autoregressive workload 足够通用。
- **Changed Constraint:** reasoning program 内部存在多路径、reward 与中间答案状态，resource value 随
  execution 演化，固定 budget 和 request-oblivious scheduling 开始浪费 deadline budget。
- **Mechanism:** probe-in-the-middle 周期性取得中间答案后丢弃 probe tokens；CoT 用 sliding-window answer
  consistency，multipath 用 normalized semantic entropy，reward-guided program 用 normalized reward 形成
  certaindex。Dynasor 以 Reasoning Program abstraction、application runtime resource allocator、system
  runtime scheduler 三层消费这一 signal。
- **State Ownership / Control and Data Flow:** program 持有 certaindex、resource knob 与 execution state；
  scheduler 读取 program signal，联合 gang scheduling、approximate SJF、starvation escalation 分配资源；
  prefix cache manager 与 context manager 保存可恢复 program state。
- **Implementation Details:** 基于 SGLang 0.3.3.post1，约 1.5K Python LOC，其中核心 runtime 约 500 LOC；
  backend abstraction 允许替换 serving engine。未集成 PD disaggregation 与 chunked prefill。
- **Evaluation Contract:** Runpod A100 80GB；SC 单 GPU，MCTS/Rebase 两 GPU；Poisson arrivals，P90 deadline
  attainment；deadline 根据超过 100 次 oracle trial 的 difficulty 估计。CoT 还覆盖 DeepSeek distilled
  Qwen 7B/14B/32B、AIME24/AMC23/MATH500、最高 16K token 与不同 probe interval。
- **What the Evidence Proves:** 作者设置中，稳定性 signal 可驱动 early exit 与资源调度；在披露 workload
  内减少 token 并提升 deadline-constrained sustainable rate。饱和 memory-bound 场景平均 throughput
  未必提升。
- **What It Does Not Prove:** 不证明稳定等于正确，不证明作者的最高 3.3x 对其他模型、硬件、并发、SLO
  或 serving backend 成立，也不证明 threshold 可跨 workload 迁移。
- **Limitations / Trade-offs / Failure Modes:** threshold 过激会降 accuracy；probe 有 overhead；新增 confidently
  wrong early exit、program fairness、gang starvation、cache identity、side-channel 与 multitenant manipulation。
- **Where the Previous Design Still Applies:** 无可靠 progress signal、正确性代价高、短回答或极低负载时，
  固定 budget 与普通 token scheduler 更简单可控。
- **Evolution Relationship:** `Direct Evolution`（token-aware → reasoning-program-aware scheduling）；与
  length preference training 为 `Layering / Dependency`，不是替代关系。
- **ROADMAP Node:** Owner `INFER-SCHEDULING`，Current Ch56，Legacy Ch52；handoff `AGENT-WORKFLOW`，
  Current Ch81，Legacy Ch77。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** signal spoofing、fairness、PD integration、chunked prefill、跨 replica program state。

### Training Software Engineering Agents and Verifiers with SWE-Gym

- **Candidate / Week / Score:** SWE-Gym / 2025-W01 / 28/30。
- **Source Family ID:** `swe-gym-agent-environment-verifier`。
- **Source Type:** 作者论文、dataset、code 与 model artifact；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 2024-12-30；v2 2025-06-06。事件归 v1，v2
  用于补足 ICML revision 的实验与限制。
- **Direct Primary Sources:** https://arxiv.org/abs/2412.21139；https://arxiv.org/html/2412.21139；
  https://github.com/SWE-Gym/SWE-Gym。
- **Access and Verification Status:** Verified；全文、appendix、artifact links 与实验细节可访问。
- **Full-read Coverage:** metadata、Introduction、Related Work、dataset construction、OpenHands 与
  MoatlessTools training、rejection sampling、verifier、training/inference scaling、ablations、appendix、
  limitations、impact statement。
- **Original Problem:** SWE-Bench 提供 evaluation，却没有可规模训练的 repository-level executable
  environment；孤立 code task 不能训练长 horizon 的 issue-resolution loop。
- **Why the Previous Design Was Reasonable:** 静态 benchmark 可复现、成本较低，synthetic function task
  易生成；general Agent scaffold 避免每类 issue 都手写 workflow。
- **Changed Constraint:** policy improvement 需要可执行 reward、repository context、trajectory 与失败样本；
  inference scaling 还需要能判断完整 action-observation trace 或 patch 的 verifier。
- **Mechanism:** 从 358 repos 的 64,689 raw issues 过滤并人工构造 11 个 Python repos、2,438 instances
  的 executable environments；SWE-Gym Lite 230。以 successful trajectories 做 rejection-sampling fine-tuning，
  并训练 outcome verifier 对多候选 Agent trajectory 排序。
- **State Ownership / Control and Data Flow:** environment 持有 codebase、dependency 与 tests；Agent scaffold
  持有 context/action history；policy 生成 tool actions；test result 形成 trajectory label；verifier 消费 issue、
  context、patch 或完整 trace，输出 success probability。
- **Implementation Details:** environment 构造约 200 human hours、10K CPU core hours、6TB Docker images；
  OpenHands 为通用 turn-taking scaffold，MoatlessTools 为阶段化专用 workflow。训练使用 Qwen2.5-Coder-
  Instruct 7B/14B/32B，核心训练集为 491 条成功 trajectories。
- **Evaluation Contract:** SWE-Bench Verified/Lite；不同 scaffold、policy/verifier size、temperature、候选数 k、
  per-instance cap、on/off-policy mixture 与 empty-patch rate 均有披露。最大 turns 30/50；作者报告数字不能
  外推到其他 repo、语言、tool harness 或 production SLO。
- **Baselines / Ablations / Sensitivity:** general vs specialized workflow；zero-shot vs fine-tuned；on-policy、
  off-policy 与 mixture verifier data；7B vs 32B verifier；trajectory、instance 与 repository scaling；instance cap。
- **What the Evidence Proves:** executable environment 可同时支持 policy 与 verifier training；作者设置中
  fine-tuning 和 verifier reranking 改善所选 SWE-Bench resolution；mixed on/off-policy verifier data 优于单一来源。
- **What It Does Not Prove:** 不证明 model-alone capability；tests 通过不等于 patch 语义、安全与 maintainability；
  也不证明在线 self-improvement 自动稳定。通用 scaffold 的 on-policy + off-policy self-improvement 从
  15.3 降至 8.7，是重要负结果。
- **Limitations / Trade-offs / Failure Modes:** 只有 Python、11 repos；环境与 tests 可能不完整；人力与 storage
  成本高；specialized workflow 降低 horizon 却增加 human engineering；verifier 继承 test/harness bias；
  容易出现 easy-task sampling bias、reward hacking 与 malicious-code misuse。
- **Where the Previous Design Still Applies:** 小范围稳定任务适合专用 workflow；需要开放探索的任务适合通用
  scaffold；无法建立可信 executable verifier 时，human review 与静态 evaluation 仍不可替代。
- **Evolution Relationship:** `Layering / Dependency`：model policy → executable environment → Agent scaffold →
  verifier → inference-time selection；不是单纯增加 model size 的直接演进。
- **ROADMAP Node:** Owner `AGENT-WORKFLOW`，Current Ch81，Legacy Ch77；supporting `PLATFORM-EVALUATION-SYSTEM`
  Current Ch66 / Legacy Ch62 与 `TRAIN-DATA` Current Ch27 / Legacy Ch23。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** test oracle 完整性、repository contamination、security sandbox、human collaboration 与
  verifier calibration。

### Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs

- **Candidate / Week / Score:** Do NOT Think That Much / 2025-W01 / 25/30。
- **Source Family ID:** `overthinking-length-preference-reasoning-efficiency`。
- **Source Type:** 作者论文；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 2024-12-30；v2 2025-02-01。v2 加入 DeepSeek-R1
  结果；本周事件仍以 v1 为准。
- **Direct Primary Sources:** https://arxiv.org/abs/2412.21187；https://arxiv.org/html/2412.21187。
- **Access and Verification Status:** Verified；全文、公式、evaluation 与 appendix 可访问。
- **Full-read Coverage:** metadata、Introduction、solution distribution、outcome/process efficiency metrics、
  self-training、SFT/DPO/RPO/SimPO、response simplification、evaluation、related work、conclusion、case/prompt appendix。
- **Original Problem:** test-time compute scaling 常把“更多 tokens/solutions”当成单调收益，但简单问题上，
  早期已得到正确答案后仍重复生成相似 solution rounds。
- **Why the Previous Design Was Reasonable:** 难题需要搜索、reflection 与 verification；固定长 budget 避免
  过早截断，且在缺少可靠 difficulty estimator 时实现简单。
- **Changed Constraint:** reasoning model 进入大规模 serving 后，token cost 与 latency 成为一等约束；compute
  需要随 task difficulty 与 marginal information gain 调整。
- **Mechanism:** outcome efficiency 用首次正确答案前 token 占比衡量有效计算；process efficiency 用经
  Llama-3.3-70B 聚类后 distinct solutions 的 token 占比衡量策略多样性。训练从 QwQ-32B-Preview 的 10 个
  samples 选 shortest / first-correct / reflection / greedily-diverse response，使用 SFT 或 preference optimization
  学习更短但保留必要 reflection 的行为。
- **State Ownership / Control and Data Flow:** 该方案把 efficiency preference 固化进 model weights；training
  pipeline 生成多样 response、按 correctness/length/diversity 构造 pairs，再由 SimPO 等 objective 更新模型。
  它不在 runtime 暴露可独立审计的 early-exit state。
- **Implementation Details:** PRM12K 用于 self-training；QwQ-32B-Preview 是可 post-train 平台；比较 SFT、DPO、
  RPO、SimPO 与三种 simplification。未披露 production hardware、serving concurrency 或 latency SLO。
- **Evaluation Contract:** ASDIV、GSM8K、MATH500，并在 GPQA/AIME24 验证；比较 QwQ-32B-Preview、
  DeepSeek-R1 与 conventional LLM。作者报告 MATH500 token reduction 等结果必须绑定该 model/data/training
  setting，不能外推到其他 reasoning model。
- **What the Evidence Proves:** 在作者数学 benchmark 与 QwQ post-training 设置中，后续 solution rounds 常
  重复；length/diversity-aware preference data 可减少 tokens。First-Correct 最短，但会伤害难题；保留一次
  reflection 是 accuracy-efficiency trade-off。
- **What It Does Not Prove:** correctness detector 与 solution clustering 依赖 evaluator；不证明所有长 CoT
  都是浪费，也不证明压缩后的模型在开放域、tool use 或 adversarial task 上保持 capability。
- **Limitations / Trade-offs / Failure Modes:** benchmark 以数学为主；judge/model bias；preference 可能造成
  underthinking、削弱 rare hard-task exploration；训练期压缩缺少 runtime 可解释 stop reason。
- **Where the Previous Design Still Applies:** 难度未知、错误代价高、需要探索多种策略时，较长 budget、
  external verifier 或 runtime adaptive compute 仍合理。
- **Evolution Relationship:** 与 Certaindex 为 `Alternative Branch / Layering`：一个把效率写入 weights，另一个
  在 runtime 观测 program state；两者可叠加但不能互相替代。
- **ROADMAP Node:** Owner `TRAIN-DPO`，Current Ch34，Legacy Ch30；handoff `INFER-SCHEDULING`，
  Current Ch56，Legacy Ch52。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** 怎样避免 underthinking、如何校准 difficulty、如何让 runtime 暴露可审计 stop reason。

### TangoFlux: Flow Matching and CLAP-Ranked Preference Optimization

- **Candidate / Week / Score:** TangoFlux / 2025-W01 / 22/30。
- **Source Family ID:** `tangoflux-crpo-audio-flow-alignment`。
- **Source Type:** 作者论文、代码、模型与 preference dataset；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 2024-12-30；v2 2025-04-10。事件归 v1，
  v2 用来补足作者后续披露的实验细节，不改变本周归属。
- **Direct Primary Sources:** https://arxiv.org/abs/2412.21037；https://arxiv.org/html/2412.21037；
  https://github.com/declare-lab/TangoFlux。
- **Access and Verification Status:** Verified；Method、公式、training/evaluation、ablations、human-eval
  appendix 与 artifacts 可访问。
- **Full-read Coverage:** metadata、Introduction、VAE/text/duration conditioning、MMDiT/DiT architecture、
  rectified flow、CRPO 三阶段、DPO-FM/CRPO objective、training data、objective/human evaluation、online/offline
  ablation、reward-model test、sampling sensitivity、related work、conclusion 与相关 appendices。
- **Original Problem:** diffusion-based text-to-audio 需要较多 sampling steps；audio alignment 又缺少像代码测试
  或 gold answer 那样便宜、可验证的 preference oracle。
- **Why the Previous Design Was Reasonable:** diffusion 路线成熟且质量稳定，human preference labels 语义强；
  static preference dataset 容易复现，也避免模型不断用自己的分布生成训练样本。
- **Changed Constraint:** 希望用开放数据、较少 sampling steps 生成长音频，并把 prompt adherence 纳入训练；
  human labeling 成本无法随每轮 model distribution 扩展。
- **Mechanism:** frozen audio VAE 把 44.1kHz stereo waveform 压成 latent；FLAN-T5 与 duration embedding 条件化
  6 个 MMDiT + 18 个 DiT blocks。rectified flow 学习从 noise 到 audio latent 的 velocity。CRPO 每轮从 prompt
  bank 采样、由当前 policy 为每个 prompt 生成多份 audio、用 CLAP cosine similarity 选 winner/loser，再对
  rectified flow 做 preference optimization。
- **State Ownership / Control and Data Flow:** checkpoint `pi_k` 生成本轮 samples；CLAP proxy judge 持有排序
  control；preference dataset 属于 iteration-scoped derived data；训练生成 `pi_k+1`。这是训练期循环，不是
  runtime RL，也不是 human preference 的等价替代。
- **Implementation Details:** 515M model；pretrain WavCaps 80 epochs，5×A40、global batch 80；AudioCaps
  fine-tune 65 epochs；CRPO 每轮 20K prompts、每 prompt 5 samples、20K pairs、8 epochs，共 5 rounds。
  winner 的 flow-matching loss 被加回 DPO-FM，作为 anchor 抑制 winner/loser loss 同时漂移。
- **Evaluation Contract:** AudioCaps 886-sample split；10s evaluation clip、50 sampling steps、CFG 4.5；同一
  A40 比较 inference time；objective metrics 为 FD/KL/CLAP/IS。human evaluation 使用 50 个 GPT-4o 生成并
  人工筛选的 OOD prompts，每个 sample 至少 4 个 annotators，评 OVL 与 REL。
- **Baselines / Ablations / Sensitivity:** AudioLDM2、Stable Audio Open、Tango2；online vs reused static data；
  CRPO vs Audio-Alpaca/BATON；CLAP best-of-N；CRPO loss vs DPO-FM；CFG、sampling steps 与 human ranking。
- **What the Evidence Proves:** 在作者 audio workload 中，rectified flow 可用较少 steps 生成 audio；online
  preference refresh 延后 static-data saturation；加入 winning flow loss 比纯 DPO-FM 更稳定。CLAP 能作为
  本实验的 proxy ranking signal，但结论仍受其 embedding bias 约束。
- **What It Does Not Prove:** 不证明 CLAP 等价于 human preference，也不证明作者的 3.7s 对其他 hardware、
  precision、batch 或 serving SLO 成立；不证明 online self-generated preference 可无限自举。
- **Limitations / Trade-offs / Failure Modes:** proxy reward 可能 reward-hack；online generation 成本高；训练
  最终出现 saturation；human set 只有 50 prompts；pseudostereo、30s crop/pad 与 AudioCaps domain 限制外推。
  winning-loss anchor 降低 drift，却限制 preference margin 的激进优化。
- **Where the Previous Design Still Applies:** 有高质量人工 feedback、domain shift 大或 proxy judge 未校准时，
  static/human preference 仍更可信；质量优先且 latency 不敏感时，多步 diffusion 仍是有效分支。
- **Evolution Relationship:** `Alternative Branch`（diffusion → rectified flow）与 `Principle Reuse`（language
  DPO → continuous generative model alignment）。
- **ROADMAP Node:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24，Legacy N/A；handoff
  `TRAIN-DPO`，Current Ch34，Legacy Ch30。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** CLAP calibration、proxy reward gaming、跨 domain human agreement 与 online data lineage。

### HumanEval Pro and MBPP Pro: Self-invoking Code Evaluation

- **Candidate / Week / Score:** HumanEval Pro / MBPP Pro / 2025-W01 / 21/30。
- **Source Family ID:** `codeeval-pro-self-invoking-code-benchmarks`。
- **Source Type:** 作者论文、benchmark 与 repository；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 2024-12-30；v2 2024-12-31，均属于 W01。
- **Direct Primary Sources:** https://arxiv.org/abs/2412.21199；https://arxiv.org/html/2412.21199；
  https://github.com/CodeEval-Pro/CodeEval-Pro。
- **Access and Verification Status:** Verified；全文、benchmark recipe、prompts、model list、error examples 与
  artifact 可访问。
- **Full-read Coverage:** metadata、Introduction、Related Work、problem/solution/test construction、20+ model
  evaluation、base-vs-instruct、confusion matrix、CoT、error analysis、BigCodeBench-Lite Pro generalization、
  limitations、model/prompt/error appendices。
- **Original Problem:** HumanEval/MBPP 主要测单函数生成；BigCodeBench 测 external API use，但不直接检查
  模型能否生成一个 base function，再正确理解、调用并组合自己的产物解决更复杂问题。
- **Why the Previous Design Was Reasonable:** 单函数 benchmark 规模小、可执行、容易形成稳定 pass@k；它们
  很适合测局部 synthesis，但并未声称覆盖 repository workflow 或 compositional code use。
- **Changed Constraint:** coding system 需要跨中间 artifact 维持 function identity、signature、types 与调用关系；
  单点 pass 不能代表 multi-step composition 正确。
- **Mechanism:** DeepSeek-V2.5 基于原题生成语义相关但更复杂的 self-invoking problem、candidate solution 与
  test inputs；controlled Python execution 生成 expected output；iterative execution checks 和 human review 修正
  solution/spec/test，直到 canonical solution 通过。另从 BigCodeBench-Lite 构造 57 个 Pro tasks 检查迁移。
- **State Ownership / Control and Data Flow:** base problem 与 generated function 是第一阶段 artifact；complex
  problem 显式依赖该 artifact；execution harness 持有 tests 与 expected outputs；human reviewer 拥有最终
  benchmark acceptance，而不是把 LLM 生成 test 直接当 ground truth。
- **Implementation Details:** 原始 generated solution/test 第一轮通过率仅 64.0%（HumanEval Pro）与 84.7%
  （MBPP Pro），经 execution + manual review 三轮达到 canonical 100% pass；这证明 benchmark pipeline 自身
  也需要 verifier，不是 benchmark score 的模型结论。
- **Evaluation Contract:** HumanEval Pro/MBPP Pro 与原 benchmark 成对比较；open models greedy decode，API
  models temperature 0.2；pass@k；zero/one-shot；20+ proprietary/open models；CoT subset；BigCodeBench-Lite Pro
  57 tasks。hardware、serving concurrency、latency SLO 不适用于此 capability benchmark。
- **Baselines / Ablations / Sensitivity:** base vs instruct checkpoints、with/without CoT、base task pass vs Pro pass
  confusion、error taxonomy、HumanEval/MBPP 到 BigCodeBench-Lite generalization。
- **What the Evidence Proves:** 作者 benchmark 中，多数 model 在 self-invoking composition 上低于对应 base
  tasks；instruction tuning 的相对增益并不稳定；execution/manual verification 显著提高 generated benchmark
  的 test reliability。
- **What It Does Not Prove:** 不等价于 repository-level software engineering、tool-use Agent 或 production code
  quality；任务由单一 model family生成且仍受原 benchmark contamination、Python-only 与 problem diversity 限制。
- **Limitations / Trade-offs / Failure Modes:** 只有 Python；继承 HumanEval/MBPP 题型；generated problem 可能
  带 teacher bias；tests 只能证明覆盖到的行为；manual review 提高可信度但降低规模化速度。AssertionError、
  NameError、type/value/index errors 暴露 artifact interface 的失败，而不只是“推理不够”。
- **Where the Previous Design Still Applies:** 需要快速测局部 synthesis 时原 HumanEval/MBPP 仍合理；需要
  repository/environment feedback 时应使用 SWE-Gym/SWE-Bench；self-invoking benchmark 位于两者之间。
- **Evolution Relationship:** `Direct Evolution`（single function → composed self-produced artifact）；与 SWE-Gym
  为 `Layering / Dependency`，不是互相替代。
- **ROADMAP Node:** Owner `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62；handoff
  `AGENT-WORKFLOW`，Current Ch81，Legacy Ch77。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** teacher-model bias、contamination、test oracle coverage 与多语言/repository generalization。

### HUNYUANPROVER: Data Synthesis and Guided Tree Search for Formal Proof

- **Candidate / Week / Score:** HUNYUANPROVER / 2025-W01 / 23/30。
- **Source Family ID:** `hunyuanprover-iterative-data-guided-tree-search`。
- **Source Type:** 作者技术报告；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2024-12-30；v2 2024-12-31；v3
  2025-03-21。W01 事件按 v1 归属；当前可访问 HTML 为 v3，后续 revision 只用于补充证据边界。
- **Direct Primary Sources:** https://arxiv.org/abs/2412.20735；https://arxiv.org/html/2412.20735。
- **Access and Verification Status:** Verified；正文、公式、算法、实验、消融和 prompts appendix 可访问。
- **Full-read Coverage:** metadata、Introduction、Related Work、scalable data synthesis、iterative tactic data
  generation、BFS/MCTS、policy-confidence/PRM/distance critics、implementation、MiniF2F evaluation、data/search
  ablations、Conclusion 与核心 appendices。
- **Original Problem:** formal theorem proving 同时受限于高质量 Lean tactic trajectory 稀缺和搜索空间巨大；
  仅让模型一次生成完整 proof 难以利用 proof-assistant 的中间状态反馈，朴素 step search 又把大量预算消耗在
  无法完成的分支上。
- **Why the Previous Design Was Reasonable:** whole-proof generation 控制流简单，适合模型已有完整 proof prior
  的问题；BFS 加 policy confidence 无需额外 critic 标注，且每一步都能由 Lean 立即判定 tactic 是否合法。
- **Changed Constraint:** 要把 7B 模型扩展到更难的 formal problems，训练数据必须持续增长，同时 inference
  需要区分“语法合法但离证明更远”和“仍可能到达证明”的状态。
- **Mechanism:** 系统先将约 30M 内部数学题各采样 8 次 autoformalization，经 grammar/rule filtering 得到约
  20M Lean statements；再用当前 prover 对未解题执行 BFS，保存成功 tactic trajectories、rejection-finetune，
  过滤过早已解的 easy statements，并把未完成状态转成新命题，循环十余轮。search 侧将 Lean state 作为节点、
  tactic 作为边；除 policy confidence 外，训练能否到达成功叶子的 PRM，以及用八层 binary-tree special tokens
  表示最多 64 个剩余步骤的 distance critic。distance tuple 以 coarse-to-fine 顺序比较候选状态。
- **State Ownership / Control and Data Flow:** prover 提议 tactic；LeanDojo/Lean engine 拥有可执行 correctness
  oracle 并产生新 proof state；search controller 拥有 frontier、dedup、budget 与 node score；critic 只排序状态，
  不拥有证明真值。成功轨迹回流训练集，形成 data-generation 与 policy/search 的闭环。
- **Implementation Details:** prover 由 Hunyuan 7B fine-tune；最多 4 epochs，sequence length 4096，batch
  256，learning rate 从 2e-5 余弦衰减到 1e-6，并依据 MiniF2F validation 选 checkpoint。BFS 每步采样 8 个
  tactics，温度 0.7/0.8/1.0/1.1 各 2 个，字符串级 proof-state dedup；MCTS 版本移除 rollout simulation，
  以 critic value 和 UCB 选择/扩展节点。
- **Evaluation Contract:** MiniF2F 244 validation + 244 test；LeanDojo；whole timeout 3600s、step timeout
  60s、最多 800 search steps。主表的 HunyuanProver v16 使用 `600 passes × 8 tactics × 400 iterations`
  记账；hardware、precision、wall-clock、energy、并发与 production SLO 为 `Not Disclosed`，因此不能把
  sample-budget 比较外推成端到端成本优势。
- **Baselines / Ablations / Sensitivity:** 与 Lean-STaR、InternLM2.5-StepProver、DeepSeek-Prover-V1.5
  比较；迭代数据在早期持续增益，v8 之后将约 2.75B tokens 扩至约 4.25B 的边际收益变小，v12 后删除早期
  easy data 又带来提升。v16 的 BFS+policy confidence 为 64.75%，BFS+distance critic 为 68.44%；不同
  model versions 上 MCTS+PRM 优于 BFS+policy confidence，但论文因算力限制没有分别消融 MCTS 与 PRM。
- **What the Evidence Proves:** 在作者的 Hunyuan 7B、MiniF2F 与规定 search budget 下，iterative tactic
  data curation 与 critic-guided state ordering 能改善 formal proof completion；distance critic 相对同版本
  policy-confidence BFS 的增益具有直接消融证据。
- **What It Does Not Prove:** 不能单独归因 MCTS 或 PRM 的收益；不能证明更大的 synthetic corpus 本身充分，
  也不能证明 MiniF2F 结果泛化到所有 Lean libraries、其他 proof assistants、informal math 或 production
  Agent planning。作者报告的 68.4% 不具有统一 hardware/latency contract。
- **Limitations / Trade-offs / Failure Modes:** autoformalization/filtering 可能生成偏置或狭窄命题；iterative
  self-training 会放大当前 prover 的可解分布；删除 easy data 提高难度但可能损害基础覆盖；critic misranking、
  state-string dedup collision、search-budget explosion 与 model/validation coupling 都会造成失败。distance
  target 被截断到 64，且“更接近证明”不保证该分支最终可解。
- **Where the Previous Design Still Applies:** proof prior 强、预算小的任务仍适合 whole-proof generation；
  没有可靠 critic 或 critic domain-shift 时，BFS/policy confidence 更简单可审计；训练数据稀缺时，人工验证的
  formal corpus 仍是防止 synthetic feedback loop 漂移的锚点。
- **Evolution Relationship:** `Direct Evolution`（whole proof → proof-state interactive search）与
  `Layering / Dependency`（executable Lean feedback → iterative data synthesis → learned critic guidance）。
- **ROADMAP Node:** Owner `AGENT-PLANNING`，Current Ch79，Legacy Ch75；handoff `TRAIN-DATA`，Current
  Ch27，Legacy Ch23，以及 `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** 独立 MCTS/PRM ablation、跨 theorem/library generalization、critic calibration、synthetic
  data provenance，以及在固定 wall-clock/energy contract 下 guided search 是否仍占优。

### 2.5 Years in Class: From Loose Web Pairs to Temporally Aligned Interleaved Data

- **Candidate / Week / Score:** 2.5 Years in Class / 2025-W01 / 24/30。
- **Source Family ID:** `multimodal-textbook-instructional-video-corpus`。
- **Source Type:** 作者论文、project、dataset/code artifact；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-01-01；v2 2025-01-03；v3
  2025-01-27；v4 2025-05-13。W01 按 v1 归属；当前 HTML 为 v4，ICCV 2025 正式版本属于后续
  publication node，不重复作为本周新事件。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00958；https://arxiv.org/html/2501.00958；
  https://github.com/DAMO-NLP-SG/multimodal_textbook；https://multimodal-interleaved-textbook.github.io/。
- **Access and Verification Status:** Verified；全文、supplement、training/evaluation repository 与 sample
  schema 可访问；完整原始 700GB images 未在本轮下载或重跑。
- **Full-read Coverage:** metadata/revisions、Introduction、Related Work、taxonomy/video collection、video/clip/
  keyframe pipeline、dataset statistics、similarity analysis、LLaVA/Idefics2 evaluation、Cheat Test、image-order
  intervention、ASR/OCR/keyframe ablations、implementation/human-evaluation/sample-construction appendices、
  limitations、ethics/license 与 repository data/training/evaluation contract。
- **Original Problem:** image-text pairs 丢失跨图顺序，webpage interleaved corpora 又包含广告、logo、松散
  图文关系和低知识密度；VLM 因而可能学到同页共现，却没有学习一个知识讲解随时间推进的多模态上下文。
- **Why the Previous Design Was Reasonable:** web crawl 成本低、覆盖广、规模容易扩展；单图配对适合局部
  alignment，网页 sample 也保留一部分自然上下文。它们优化的是 coverage 和 throughput，而非教学过程的
  temporal coherence。
- **Changed Constraint:** knowledge/reasoning workload 需要多个 diagram、formula、spoken explanation 按顺序
  对齐；同时长视频平均约 86 个 keyframes，不能直接作为多数 VLM context 的单个 training sample。
- **Mechanism:** GPT-4o 生成四层 taxonomy（Subject → Course → Sub-course → Knowledge Point），据此检索
  159,565 个 English YouTube instructional videos；metadata/ASR 多级过滤保留约 75K。Whisper-large-v3
  产生带时间戳 ASR，Qwen2-72B-Instruct 重写口语文本，DeepSeek-V2 与 Llama3-70B 双重过滤；ASR 段落
  决定 10–20 秒 clip 边界，VideoLlama2 caption 与 GTE-Qwen2 embedding 判断视听相关性，SSIM 选取
  keyframes，InternVL2 提取/过滤 OCR，最后按时间顺序交错 frame、OCR 与 ASR。
- **State Ownership / Control and Data Flow:** source video ID、clip timestamps 与 keyframe ordinal 定义原始
  provenance；taxonomy/metadata filter 决定召回与排除；ASR timestamps 拥有 text-frame temporal join；
  sample builder 拥有 context packing，并用 `End of Video` token 标记拼接边界。若跨视频压满 context，
  throughput 提高，但原始 video boundary 必须仍可恢复。
- **Implementation Details:** pipeline 过滤约 53% 视频，得到 22,697 class hours、6.5M keyframes、约
  259M ASR + 500M OCR tokens，并组成 610K samples；平均每 sample 10.7 images、1,297 text tokens。
  repository 保留 video ID/timestamp/keyframe number naming，以及 LLaVA/Idefics2 pretraining 和 few-shot
  evaluation scripts。作者人工抽查 100 samples/1,421 images，但该抽样没有覆盖 chemistry。
- **Evaluation Contract:** 对 LLaVA-1.5-7B 做 continual pretraining；对 Idefics2-8B 同时测试 random-projector
  scratch setting 与已在 OBELICS 预训练后的 continual setting。MMC4/OBELICS 均等量采样 610K，并使用
  相同 training parameters；评测 TextVQA、OKVQA、ScienceQA-IMG、MathVista、MathVision、MathVerse 的
  0/1/2/4-shot，Idefics2 扩至 8-shot；随后统一使用 LLaVA-665K SFT。完整 GPU 数、precision、global batch、
  sequence-length distribution、训练时长和能耗为 `Not Disclosed`，不能外推绝对效率。
- **Baselines / Ablations / Sensitivity:** 对比 paired/web interleaved datasets；`Cheat Test` 检查模型能否从
  prompt 中找回完全相同的 test example；20/50/100% sample image-order shuffle 检查顺序依赖；去除 ASR
  refinement、OCR，或以 pixel/CLIP 替换 SSIM keyframe selection。作者设置中 raw ASR、缺 OCR 和过密/过稀
  keyframes 都降低平均结果，说明 pipeline 不是单一“更多 token”变量。
- **What the Evidence Proves:** 在等 sample count 和作者训练设置中，instructional-video derived、时序交错的
  corpus 相对选定 web corpora 改善若干 knowledge/reasoning 与 few-shot tasks；顺序打乱对本数据的伤害大于
  对 MMC4，证明其 sample 中存在可被训练利用的顺序信号；ASR/OCR/keyframe ablations 支持多级 curation
  各自有贡献。
- **What It Does Not Prove:** InSI-SIM 高不等价于因果或教学质量；Cheat Test 测的是复制/定位显式答案的
  context access，不等价于一般 in-context reasoning；作者实验不能证明 video corpus 普遍优于所有 web data，
  也不能证明生成能力，因为 image tokens 不计算训练 loss。没有独立复现或完整成本 contract。
- **Limitations / Trade-offs / Failure Modes:** taxonomy 和 metadata/ASR judge 会形成 language/domain/model
  selection bias；ASR 重写可能删改细节，OCR noise 会污染公式；SSIM 适合 slide/diagram 的结构变化，却可能
  错过语义变化或保留视觉冗余；跨 clip/video packing 提高利用率但削弱长程 lecture continuity。English-only、
  100-sample manual audit、source copyright/privacy 与原视频删除/freshness 都限制可复用性。数据集 CC-BY
  声明不替代每个 source content 的原始许可。
- **Where the Previous Design Still Applies:** 需要大规模 broad coverage、单图 alignment 或低成本 crawl 时，
  paired/web corpora 仍合理；需要完整 temporal dynamics 时应保留 video tokens 而非仅 keyframes；对法律或
  高风险知识，人工审核和来源许可清单优先于纯 LLM filtering。
- **Evolution Relationship:** `Direct Evolution`（image-text pair → interleaved webpage → temporally aligned
  instructional sequence）；与 multimodal representation 为 `Layering / Dependency`，与 data curation 为
  canonical training-data mechanism。
- **ROADMAP Node:** Owner `TRAIN-DATA`，Current Ch27，Legacy Ch23；handoff
  `MULTIMODAL-REPRESENTATION`，Current Ch23，Legacy N/A，以及 `PLATFORM-EVALUATION-SYSTEM`，Current
  Ch66，Legacy Ch62。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** source-license ledger、ASR rewrite fidelity、chemical-domain audit、video-boundary packing
  ablation、跨语言/年龄层覆盖，以及在等 token/compute 而非等 sample count 时优势是否保持。

### CodeElo: Executable Oracle, Environment Alignment and Human-comparable Rating

- **Candidate / Week / Score:** CodeElo / 2025-W01 / 23/30；全文审计后 Source Reliability 由 5 调为 4，
  因完整 submission scaffold 未开放，且论文的 proprietary-model count 存在 3/4 内部不一致。
- **Source Family ID:** `codeelo-codeforces-executable-rating-benchmark`。
- **Source Type:** 作者论文、project page、dataset；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-01-02；v2 2025-01-03；均属于 W01。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01257；https://arxiv.org/html/2501.01257；
  https://codeelo-bench.github.io/；https://huggingface.co/datasets/Qwen/CodeElo。
- **Access and Verification Status:** Paper and dataset verified；完整自动提交/evaluation scaffold 在事件时因
  Codeforces policy 和风险评估未公开，因此 end-to-end reproduction 不能标记为 verified。
- **Full-read Coverage:** metadata/revisions、Introduction、Related Work、problem collection/classification、
  online submission oracle、Elo derivation、experiment setup、model/contest/problem/tag/pass@n results、C++/Python
  comparison、rating variance、discussion/limitations/ethics、model/decoding/Elo/special-judge appendices，以及
  project/dataset schema。
- **Original Problem:** competitive-programming benchmark 若在本地依赖公开或生成 tests，会遗漏 hidden
  adversarial cases、special judges 和 interactive problems；不同机器又改变 time-limit outcome。即使 pass@n
  可执行，也无法直接与参加同一 contest 的 human rating 对齐。
- **Why the Previous Design Was Reasonable:** offline tests 可复现、不会依赖外部平台、不会污染 judge queue，
  并适合 function-level benchmark；pass@n 简单且能测 sampling diversity。它们没有承诺复现完整 Codeforces
  contest contract。
- **Changed Constraint:** evaluation 目标变为完整 contest-level algorithm design，需要 hidden tests、special
  judge、runtime/memory limit、multiple attempts、difficulty-weighted scoring 和 human comparison 同时成立。
- **Mechanism:** benchmark 保留 Codeforces 原始 HTML 结构与 division/problem-rating/algorithm-tag metadata，
  选择 2024-05-04～11-04 的 54 场、387 题；从 model output 解析 code block，通过 bot 直接提交官方平台，
  只把 official `Accepted` 当成功。每题最多 8 次，失败尝试计 penalty，不计模型生成时间；模型在每场 contest
  的 rank 被放入真实 human ranking，再解单调 Elo 方程得到 expected rating，最后跨 contest 平均降方差。
- **State Ownership / Control and Data Flow:** benchmark 拥有 problem snapshot、prompt、model samples 与 attempt
  ledger；Codeforces 拥有 hidden tests、special judge、execution environment、verdict 与 human standings；rating
  calculator 将 score/penalty 转成 rank，再映射为 Elo。oracle 和 benchmark 由不同主体拥有，提高 verdict
  真实性，却引入外部平台 availability、policy、version 和 rate-limit 依赖。
- **Implementation Details:** 测试排除模型几乎无法完成的纯 Div.1，覆盖 Div.1+2/2/3/4；同一 C++ CoT prompt；
  open models 通过 vLLM，temperature 0.7、top_p 0.8、top_k 20、repetition penalty 1.1、max output 4096，
  QwQ-32B-Preview 为 32768；proprietary APIs 使用默认参数。论文摘要称 30 open + 3 proprietary，setup
  写 30 open + 4 proprietary，而主表只列 3；该数量冲突不影响机制，但降低结果账本可信度。
- **Evaluation Contract:** 387 problems/54 contests；最多 8 submissions/problem；模型假设首分钟提交且不计
  time penalty；official score 和 failed-attempt penalty；Codeforces 2024-11 human-rating distribution；C++ 为
  主评测语言。open-model hardware、GPU count、precision、batch/concurrency、vLLM version、API sampling
  defaults、wall-clock/cost 和 failure-retry policy 为 `Not Disclosed`，模型间 serving cost 不可比较。
- **Baselines / Ablations / Sensitivity:** 与 APPS、CodeContests、TACO、xCodeEval、USACO、LiveCodeBench 的
  oracle/update/environment/rating contract 比较；按 division、problem rating、16 个高频 tags 分析；pass@1/2/4/8；
  若干模型 C++ vs Python；54 contests 的 rating distribution/variance。没有独立比较“相同 outputs 在 weak offline
  tests 与 Codeforces hidden tests 上的 false-positive rate”，`zero false positives` 是 official verdict contract，
  不是经验估计。
- **What the Evidence Proves:** official online judge 能统一 hidden tests、special/interactive judge 与 execution
  limit；在固定 prompt、attempt budget 和所选 contest snapshot 下，可把 model contest rank 映射到同场 human
  ratings，并观察 language、difficulty 与 algorithm-tag sensitivity。跨 54 场平均确实降低 mean-rating variance。
- **What It Does Not Prove:** Elo 不是一般 software-engineering 能力、repository workflow、maintainability 或
  security；模型生成时间被忽略，human 可读题/调试方式不同，因此“human-comparable”仅限 contest score/rank
  mapping。C++ 优势可能同时来自 runtime limit、训练分布、prompt 与 token budget，不能只归因为语言效率。
- **Limitations / Trade-offs / Failure Modes:** external oracle 带来平台变更、账号封禁、queue pressure、网络失败、
  hidden test 演进和复现权限风险；最多 8 次可能低估可持续调试能力，更多尝试又污染平台并造成资源影响；
  contest independence/IID 是 rating aggregation 假设；近期题降低 contamination 但不消除公开 editorial/solution
  leakage。code-block parse、compile-language selection、API nondeterminism 与 submission failure 需要独立记账。
- **Where the Previous Design Still Applies:** CI/offline regression、private repository、安全审计和高频 model
  iteration 仍应使用本地可控 tests；function-level capability 用 HumanEval/MBPP，composition 用 Pro variants，
  repository Agent 用 SWE-Gym/SWE-Bench。CodeElo 只占 competition algorithm + official judge 这一层。
- **Evolution Relationship:** `Direct Evolution`（public/offline tests → platform-owned executable oracle）与
  `Alternative Branch`（pass@n ↔ difficulty/attempt-aware Elo）；和 HumanEval Pro、SWE-Gym 组成不同粒度的
  executable-evidence ladder，而非单向替代。
- **ROADMAP Node:** Owner `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62；handoff
  `AGENT-WORKFLOW`，Current Ch81，Legacy Ch77。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** event-time scaffold/commit、submission failure accounting、hidden-test revision stability、
  等 wall-clock/cost 的 model comparison、contest-IID 假设，以及 Codeforces 明确授权后的可复现运行方式。

### LTX-Video: Moving Compression and Final Denoising Across the VAE Boundary

- **Candidate / Week / Score:** LTX-Video / 2025-W01 / 23/30。
- **Source Family ID:** `ltx-video-holistic-vae-diffusion`。
- **Source Type:** 作者论文、repository 与 model artifact；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv 仅 v1，2024-12-30；后续 LTXV releases 与
  LTX-2 属于独立演进节点，不能倒灌为 W01 证据。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00103；https://arxiv.org/html/2501.00103；
  https://github.com/Lightricks/LTX-Video；https://huggingface.co/Lightricks/LTX-Video。
- **Access and Verification Status:** Verified；论文 Method、experiments、limitations 与公开 inference/model
  artifact 可访问；event-time training corpus、完整训练 recipe 与独立 reproduction 为 `Not Disclosed`。
- **Full-read Coverage:** metadata、Introduction、Video-VAE/shared objective/rGAN/noise injection、Video
  Transformer/RoPE/QK norm、text/image conditioning、rectified-flow training、data preparation、training/evaluation、
  VAE/RoPE/denoising ablations、limitations/social impact/conclusion，以及 repository runtime contract。
- **Original Problem:** video DiT 的 full spatiotemporal attention 随 token 数二次增长；常见 VAE + latent
  patchifier 虽减小序列，却仍在 VAE 与 transformer 之间保留冗余。进一步压缩会损失高频细节，并使 residual
  noisy latent 对 decoder 成为 out-of-distribution input；额外 latent/pixel upsampler 又增加一次大模型运行。
- **Why the Previous Design Was Reasonable:** 中等压缩保留更丰富的局部细节，独立 VAE/DiT/upsampler 容易分别
  训练和替换；patchifier 只改变 transformer tokenization，不迫使 autoencoder 承担更强 representation contract。
- **Changed Constraint:** 目标是让 5 秒高分辨率视频的端到端生成短于播放时间，token budget 和 denoising
  steps 成为首要约束，同时不能完全牺牲 temporal consistency 与 pixel detail。
- **Mechanism:** 把 patchifying 从 transformer input 前移到 causal Video-VAE encoder，使用 32×32×8
  spatiotemporal downsampling 与 128 latent channels，得到 1:192 representation compression、1:8192
  token-to-pixel ratio；1.9B/28-block DiT 在该 latent 上做 full self+cross attention。rectified-flow transformer
  完成 latent-to-latent steps，带 timestep conditioning 的 VAE decoder 在 `[0,0.2]` noise range 学习最后一次
  latent-to-pixel denoise，以 pixel-space losses 补偿压缩细节；rGAN 让 discriminator 比较同一原图/重建对。
- **State Ownership / Control and Data Flow:** VAE encoder 拥有 pixels → compressed latent 的 representation
  boundary；transformer 拥有大部分 noise schedule/latent trajectory；decoder 同时拥有最后一次 denoise 与 pixel
  reconstruction。image-to-video 通过 per-token timestep/noise ownership 表达：conditioning-frame tokens 取低
  timestep，其他 tokens 从纯噪声开始，而不是引入独立 condition token/model。
- **Implementation Details:** 3D causal convolutions，首帧单独 latent frame；multi-layer decoder noise injection；
  T5 text encoder + cross attention；normalized fractional RoPE 以 pixels/seconds 和原 FPS 表达时空坐标；Q/K
  先 RMSNorm。公开实现可运行 inference，但当前 repository 已包含多年后的 13B/distilled/LTX-2 路线，不能
  将其性能和配置归入 W01 的 1.9B paper model。
- **Evaluation Contract:** speed claim 为单个 NVIDIA H100、1.9B before-distillation model、5 秒/121 帧、
  24 fps、768×512、20 diffusion steps、约 2 秒；质量 survey 使用 1,000 T2V prompts + 1,000 I2V pairs、
  5 秒/768×512、所有模型 default config、40 steps、20 participants、blind pairwise preference。precision、
  batch、compile/kernel、warmup、memory、concurrency、power、end-to-end text encode/decode boundary 未完整披露。
- **Baselines / Ablations / Sensitivity:** 与相近 scale 的 Open-Sora Plan、CogVideoX 2B、PyramidFlow 比较；
  standard GAN vs rGAN reconstruction；exponential vs inverse-exponential RoPE training loss；decoder timestep
  0.05 denoising vs timestep 0.0 no-denoising internal user study。没有同时隔离 compression ratio、latent channels、
  patchifier placement 与 decoder-denoise 的完整 factorial ablation。
- **What the Evidence Proves:** 在作者模型和固定 H100 workload 下，高 compression + full spatiotemporal
  attention 可达到所报 latency；rGAN、RoPE frequency 和 final decoder denoise 在作者 ablations/user study 中
  改善相应 reconstruction/training/preference signals。它证明的是跨 VAE/DiT boundary 的责任重分配可行。
- **What It Does Not Prove:** 不证明 1:192 普遍是最佳 compression，不证明 H100 单请求 speed 可外推到
  consumer GPU、batch serving 或其他 resolution/duration；20-person preference 不是客观 temporal correctness，
  也不能证明 video generation 是 causal world model。训练数据规模、license mix 与 compute 未披露。
- **Limitations / Trade-offs / Failure Modes:** 过度压缩产生 blur/texture/motion artifacts；decoder 同时承担
  reconstruction 和 denoise，耦合训练与升级；rGAN/noise injection 可能生成 plausible 而非 faithful detail；
  prompt wording 敏感、最长约 10 秒、domain/multiview/editing 未充分测试。per-token timestep 提高条件统一性，
  但 condition corruption/schedule calibration 成为新状态；公开权重降低门槛也增加 deceptive-content 风险。
- **Where the Previous Design Still Applies:** 细节/可逆重建优先时用较低压缩；模块独立演进或可审计 pipeline
  可保留独立 upsampler；长视频可采用 hierarchical/cascaded generation；预算允许时更多 diffusion steps 仍是
  质量分支。LTX 不是对这些方案的否定。
- **Evolution Relationship:** `Direct Evolution`（moderate VAE compression + transformer patchifier →
  VAE-owned aggressive compression）与 `Alternative Branch`（separate upsampler ↔ decoder-owned final denoise）。
- **ROADMAP Node:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24，Legacy N/A；handoff
  `INFER-TENSORRT-LLM`，Current Ch49，Legacy Ch45，以及 `MODEL-POSITION-ENCODING`，Current Ch13，Legacy Ch13。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** event-time commit/config、precision/kernel/timing boundary、compression-channel factorial
  ablation、pixel faithfulness、batch/concurrency scaling、training data/license contract 与 longer-video state strategy。

### MLLM-as-a-Judge: From Monolithic Safety Prompting to Policy-Aware Cascaded Evidence

- **Candidate / Week / Score:** MLLM-as-a-Judge for Image Safety without Human Labeling / 2025-W01 / 21/30。
- **Source Family ID:** `clue-constitution-image-safety-judge`。
- **Source Type:** 作者论文；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2024-12-31；v2 2025-04-06。事件按 v1
  归入 W01；当前 HTML 为 v2，只用于补齐修订后的实验与 appendix，不把四月修订倒灌成本周新事件。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00192；https://arxiv.org/html/2501.00192。
- **Related Primary Sources:** paper 未提供可唯一确认的官方 code、dataset release 或 event-time artifact；
  因此实现可复现性保持 `Not Disclosed`，不以第三方复现或搜索摘要替代。
- **Access and Verification Status:** Verified for paper；Method、公式、实验、消融、效率与关键 appendices
  可访问；artifact 与真实生产数据验证不可访问。
- **Full-read Coverage:** metadata/revisions、Introduction、Background、rules objectification、relevance scanning、
  precondition extraction、两种 debiased token-probability strategies、cascaded reasoning、完整算法、OS Bench
  construction、zero-shot/fine-tuned baselines、per-rule results、component ablations、efficiency appendix 与 Conclusion。
  论文没有独立 Limitations / Threats to Validity 章节，因此以下边界由实验合同和方法依赖逐项推导。
- **Original Problem:** 传统 image-safety classifier 依赖按固定规则人工标注并 fine-tune；规则更新会造成
  labeling/training lag。直接把整份 constitution 与图像交给 MLLM 又同时受到规则主观性、长规则集负担和
  model yes/no bias 影响，既昂贵也不稳定。
- **Why the Previous Design Was Reasonable:** supervised classifier 在稳定 taxonomy 和足够标注下能获得明确
  decision boundary、离线 calibration 与低延迟 serving；单次 whole-constitution query 则实现简单，保留规则
  原文并减少多阶段系统状态。它们分别优化稳定 policy 和低工程复杂度，而非频繁变化规则。
- **Changed Constraint:** safety policy 需要比模型更新更频繁，且单图通常只关联少量规则；系统希望把绝大多数
  样本放在便宜的 fast path，同时为 borderline cases 保留更昂贵的 reasoning path。
- **Mechanism:** CLUE 先让 LLM 对规则 objectiveness 打分并迭代改写到至少 9/10，同时允许 policy owner
  调整关键阈值；再以 CLIP similarity（默认 0.22）逐图过滤不相关规则。Llama-3.1-70B-Instruct 离线把每条
  规则展开为逻辑完整的 AND/OR precondition chain；在线 judge 以 `p(Yes)/(p(Yes)+p(No))` 得分，并用
  no-image prior 与移除 central-object region 后的得分差校正模型 bias。只有落在不确定区间的 rule-image pair
  才进入 free-form CoT，再要求 JSON 汇总；最终输出 safe/unsafe 及违反规则集合。
- **State Ownership / Control and Data Flow:** policy owner 拥有 constitution、objectified wording 和可调阈值；
  preprocessing pipeline 拥有 rule version、precondition chain 与 embedding；relevance scanner 只拥有候选缩减，
  不能作最终 verdict；MLLM judge 产生 rule-level score、reasoning 和 violated-rule IDs；deployment release gate
  或 human adjudicator 仍应拥有最终 enforcement。若 rule version、judge version、threshold 与 evidence 未绑定，
  同一图像无法复现当时判定。
- **Implementation Details:** relevance threshold 为 0.22；central-object extraction 使用 object words、OWLv2
  与 0.05 detection threshold。bias correction 以 no-image score 构造 `alpha1=-0.3*M(None,c)`、
  `alpha2=0.8*(1-M(None,c))`，并以 `beta=0.6` 比较移除中心区域前后得分；中心区域小于图像 1% 时改用
  crop。论文披露 prompts 与 algorithm，但没有 event-time repository、依赖版本、determinism 或 policy rollout
  implementation。
- **Evaluation Contract:** OS Bench 由 14 条 objectified sexual/violence rules 构造；每条规则约 40–60 unsafe
  images，并配等量 borderline-safe images，总计约 700 unsafe + 700 safe。unsafe/safe prompts 由 LLM 生成，
  再交给 text-to-image diffusion model 并过滤低质量或错配样本。评测 Qwen2-VL-7B-Instruct、
  InternVL2-8B-AWQ、LLaVA-v1.6-34B 与 InternVL2-76B，指标为 precision/recall/accuracy/F1。hardware 仅在
  efficiency appendix 披露：InternVL2-8B-AWQ + TurboMind / 1×A100 为 22.23 秒/图，LLaVA-34B + SGLang /
  1×A100 为 42.71 秒/图，InternVL2-76B + TurboMind / 4×A100 为 101.83 秒/图；GPU 型号显存、precision
  （除 AWQ 名称外）、batch、concurrency、图像尺寸、warmup、runtime version 与 SLO 为 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity:** 比较 prior-knowledge direct/CoT、whole-constitution direct/CoT、Q16、
  SD Safety Checker、LAION NSFW detector 与 LLaVA Guard。作者 OS Bench 上四个 CLUE variants 的 recall
  为 88.9%～95.9%、accuracy 为 86.2%～94.8%；但 fine-tuned baselines 是从各自训练分布直接迁移到作者新
  taxonomy，不能据此宣称 label-free 方法普遍优于 supervised training。rule objectification 的单规则案例由
  74% 到 98%；relevance scanner 保留 96.6% ground-truth rules 并过滤 67%；InternVL2-8B 去掉 debias 后
  accuracy/F1 从 87.4%/.879 降至 66.6%/.746；去掉 precondition extraction 降至 82.7%/.823。中心区域机制
  只使 recall 90.5%→91.2%，并把每图 cascaded reasoning 次数从 1.32 降至 1.16，属于小幅受限增益。
- **What the Evidence Proves:** 在作者合成 OS Bench、objectified rule set 和四个指定 MLLM 上，把长 policy
  拆成版本化 rule candidates，并以 relevance filter、precondition、bias-corrected fast score 和 slow reasoning
  cascade 组合，比单次 direct/CoT query 更准确；component ablations 支持多个阶段各自贡献。它也说明 policy
  state、judge state 与 execution cost 可以分层拥有。
- **What It Does Not Prove:** “without human labeling”不等于没有人类 policy ownership：人仍定义/调整规则
  和阈值。OS Bench label 源于生成 prompt 与过滤逻辑，不能证明真实 prevalence、文化/群体差异、复杂背景、
  adversarial robustness 或跨 taxonomy 泛化；同一合成流程构造任务与测量结果，可能存在 synthetic shortcut。
  论文也不证明 MLLM judge 可替代 production human appeal、release gate 或 independently labeled audit set。
- **Limitations / Trade-offs / New Failure Modes:** objectification 降低语言歧义，却可能把规范争议伪装成
  几何阈值；rule-by-rule processing 增加 version、ordering、conflict 与 completeness 管理；relevance false negative
  会在 judge 前静默漏检；precondition extraction 错误会被离线复用并放大；central-object detector 和 image crop
  引入额外 model bias；fast/slow thresholds 若未经真实分布 calibration，会在 cost、recall 与 false positive 间漂移。
  CoT 输出还需要 schema validation、privacy control 与可审计 retention。
- **Where the Previous Design Still Applies:** policy 稳定、风险边界清楚且 latency 严格时，经过真实标注与校准的
  classifier 仍更简单可靠；规则数量少时 whole-constitution prompt 可作为低运维 baseline；高风险 enforcement
  必须保留 independent human-labeled audit、appeal 和 human override。CLUE 更适合作为候选生成、triage 或
  label-assistance layer，而非无条件替代人工治理。
- **Evolution Relationship:** `Direct Evolution`（monolithic judge query → rule-decomposed cascaded judge）、
  `Layering / Dependency`（policy objectification → relevance → fast score → slow reasoning → release decision）与
  `Alternative Branch`（zero-shot adaptable judge ↔ calibrated supervised classifier）。
- **ROADMAP Node:** Owner `PLATFORM-SECURITY`，Current Ch72，Legacy Ch68；handoff
  `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62，以及 `PLATFORM-MONITORING`，Current Ch67，
  Legacy Ch63。
- **Target and Adjacent Chapters Read:** 本阶段按用户要求不做 Books Integration；仅用 ROADMAP 确认 owner，
  未把章节现状当成 disposition 证据。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** v1 与 v2 方法/结果差异、event-time code/config、独立 human-labeled real-world test、
  cross-cultural policy review、rule-conflict semantics、threshold calibration/appeal contract，以及在固定并发与
  latency SLO 下 cascade 是否仍有成本优势。

### ProgCo: Verification Program and Answer Must Evolve as Separate Mutable State

- **Candidate / Week / Score:** ProgCo / 2025-W01 / 22/30。
- **Source Family ID:** `progco-program-driven-self-correction`。
- **Source Type:** arXiv v1、ACL 2025 final paper 与作者 repository；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-01-02；v2 2025-05-27；ACL 2025
  proceedings 于 2025-07 发布。本周以 v1 为 event anchor；v2/ACL 和当前 repository 只用于恢复完整 Method、
  limitations、prompts 与 artifact，不把 acceptance 或后续代码发布重复计为 W01 事件。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01264；
  https://aclanthology.org/2025.acl-short.73/；https://aclanthology.org/2025.acl-short.73.pdf；
  https://github.com/songxiaoshuai/progco。
- **Access and Verification Status:** Verified；final paper 的 Method、公式、实验、ablation、limitations 与
  prompts appendix 可访问，repository 包含 IFEval/GSM8K/MATH pipeline 与 Python-tool path；event-time commit、
  API snapshot 与完整 cost reproduction 不可确认。
- **Full-read Coverage:** metadata/revision、Introduction、Method、ProgVe/ProgRe 公式与 algorithm、Related Work、
  IFEval/GSM8K/MATH setup、三类 model、four self-correction baselines、main results、verification/refinement
  ablations、iteration sensitivity、self-consistency comparison、case studies、limitations、prompts、implementation
  appendix，以及 repository quick-start/目录/依赖与 real-Python-tool route。
- **Original Problem:** intrinsic self-correction 把同一个模型同时当 answer generator、error detector 和 critic。
  模型若漏检错误或生成错误 feedback，refinement 不仅无效，还会把正确答案改错；自然语言 checklist 又难表达
  数学中的 reverse constraint 和复杂 AND/branch logic。
- **Why the Previous Design Was Reasonable:** vanilla reflection/self-refine 只有 response 与 feedback 两类状态，
  调用少、通用且不需要 tool runtime；checklist 将条件显式化，适合 IFEval 这类原子约束。任务简单、外部 verifier
  不存在或延迟预算严格时，这些方案的低控制复杂度是合理选择。
- **Changed Constraint:** complex reasoning 要求 verifier 能表达结构化、可逐步执行的反向检查；与此同时 verifier
  自身也可能错误，系统不能把一次 self-generated feedback 当成 immutable truth。
- **Mechanism:** ProgVe 在看到初始回答之前，根据问题生成 pseudo verification function，避免被当前答案锚定；
  同一 LLM 再扮演 executor，将当前回答送入函数逐步执行，并把 execution trace 转成 feedback。通过则 early stop，
  未通过则 ProgRe 先生成可保持原答案的 temporary response，再对新旧 response 做 contrast、抽取 insight 并从
  原问题重新生成答案；同时结合 response 与 feedback 重写 verification program，供下一轮使用。数学题的 program
  从候选答案逆推已知条件；instruction following 则逐项执行 constraint checks。
- **State Ownership / Control and Data Flow:** orchestration loop 拥有 immutable input、current response、current
  verifier、execution result、feedback、temporary response、contrast insight、iteration budget 与 stop state；模型只
  提议/解释这些对象。若接入 Python，tool runtime 只拥有确定性运算结果，不拥有最终语义 verdict。response 与
  verifier 是两个会共同漂移的 mutable states，必须分别 version、trace、回滚；`pass` 是 generated feedback，不能
  等价于 external correctness oracle。
- **Implementation Details:** 论文用 Azure GPT-3.5-Turbo-0613 (16K)、GPT-4o-0806 和
  Llama-3.1-8B-Instruct；后者经 FasterTransformer 推理。temperature 为 0，其余参数默认；baseline 与 ProgCo
  均使用随长度调整的 1–3 个 demonstrations。数学答案先 regex，对未匹配项再由 GPT-4o-mini 判等；repository
  提供各 dataset pipeline、`max_cur_turn`、API configuration，以及可选 Python API service。GPU、precision、
  batch/concurrency、FasterTransformer commit、API seed/version retention 与 token/cost ledger 为 `Not Disclosed`。
- **Evaluation Contract:** IFEval 全测试集，严格 prompt/instruction 指标；GSM8K 1,319 test；MATH 从 5,000 test
  随机抽 500。比较 Llama-3.1-8B-Instruct、GPT-3.5 与 GPT-4o，最多一轮或三轮 correction。GPT-3.5 三轮下
  IFEval strict prompt/instruction 相对 initial 分别 +4.80/+3.47，GSM8K +7.28、MATH +8.0；这是作者 benchmark、
  prompts 与 evaluator contract 下的百分点变化，不是通用 self-correction rate。
- **Baselines / Ablations / Sensitivity:** baseline 为 Vanilla-Reflex、Self-Refine、Self-Reflection 与 CheckList；
  另以 3/5/10 samples 的 vote/reflex/select 与 ProgCo 早停比较。GPT-3.5 GSM8K 三轮中，去掉 contrast/regenerate
  后 accuracy 83.78→79.08，correct-to-incorrect transition 15.42→35.18；去掉 verifier reflection 后平均轮次
  0.88→1.06；去掉 program feedback 后 incorrect-to-correct 47.75→30.5。Python executor 只带来受限小幅增益：
  GPT-3.5 IFEval +2.14、MATH +0.4，GPT-4o 分别 +3.51/+1.2。没有对等 token、latency 或 dollar budget 的
  baseline，也没有 independent model judge audit。
- **What the Evidence Proves:** 在三组作者任务和三种模型上，结构化 pseudo-program 比自然语言 check 更容易
  召回部分错误；将 response correction 与 verifier correction 分开、并在二者之间做 contrast，能减少一部分
  correct-to-incorrect 回归。ablation 直接支持“verifier 也是可错状态，不能只改答案”这一系统结论。
- **What It Does Not Prove:** pseudo-program 由同一模型生成和“执行”，并未形成独立证据源；它可能只是更强的
  structured prompting，而不是真正 code execution。三套 benchmark 不证明事实核验、长程 Agent、tool side effect、
  safety 或真实 workflow 泛化；GPT-4o-mini evaluator 也引入额外 model dependency。作者的 accuracy 提升不能在
  缺少 token/cost/SLO 对齐时宣称优于 self-consistency 或 external verifier。
- **Limitations / Trade-offs / New Failure Modes:** 论文只验证 instruction-following 和数学；LLM executor 不擅长
  大规模精确运算；长 prompts/demonstrations 和多次 model calls 增加 latency/cost。独立生成 verifier 降低 answer
  anchoring，却可能遗漏 answer-specific failure；共同 refinement 提高恢复能力，也可能让错误 answer 与错误 verifier
  相互适配后假通过。新增 verifier drift、non-deterministic pass、prompt injection、tool sandbox、trace growth、
  stop-condition calibration 与 rollback 责任。
- **Where the Previous Design Still Applies:** 外部 deterministic test、compiler、proof assistant 或 environment
  oracle 可用时，应优先使用独立 verifier；简单 instruction constraint 适合 checklist；低延迟任务可保留单次回答；
  需要 search diversity 的数学题仍可用 self-consistency。ProgCo 是没有强 oracle 时的 structured intrinsic branch，
  不是 external evidence 的替代品。
- **Evolution Relationship:** `Direct Evolution`（free-form reflection → checklist → pseudo-program verification）、
  `Layering / Dependency`（verifier proposal → execution trace → feedback → answer/verifier dual refinement）与
  `Alternative Branch`（intrinsic pseudo-execution ↔ external deterministic verifier / multi-sample selection）。
- **ROADMAP Node:** Owner `AGENT-REFLECTION`，Current Ch80，Legacy Ch76；handoff `AGENT-WORKFLOW`，
  Current Ch81，Legacy Ch77，以及 `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62。
- **Target and Adjacent Chapters Read:** 本阶段只做 Weekly；依据 ROADMAP 定位 owner，不打开 Historical Books
  Integration Gate，也不把当前章节覆盖度当成 `No Change` 证据。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** v1 与 final 的结果/方法差异、event-time code commit、per-stage token/latency/cost、独立
  verifier calibration、same-model correlated error、tool sandbox 与 verifier/response rollback semantics。

### A3: From Static Action Accuracy to Environment-Owned Trajectory Evidence

- **Candidate / Week / Score:** A3: Android Agent Arena / 2025-W01 / 22/30；全文审计后 Source Reliability
  由 5 调为 4，因为事件时自动 evaluator 只由 50 个任务人工核验，双 judge 的 0.03 misjudgment claim 没有验证
  independence，且 event-time artifact 不可定位。当前 essential-state/A3RM 结果属于后续 revisions。
- **Source Family ID:** `a3-android-agent-arena-dynamic-evaluation`。
- **Source Type:** arXiv v1/v2/v3、作者 project/repository；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 2025-01-02；v2 2025-02-18；v3 2026-01-12。
  v1 标题为 `A3: Android Agent Arena for Mobile GUI Agents`，覆盖 21 apps/201 tasks、function evaluator 与
  whole-task commercial-LLM evaluation；v2 改为 20 apps/201 tasks，并正式加入 final/sequence/essential-state
  三条 evaluator branch 与 ESAR；v3 改题为 `with Essential-State Procedural Evaluation`，收缩到 20 apps/100
  tasks，引入 A3RM、Qwen3-VL、DAPO 与 2025 后发 agents。只有 v1 机制与结果属于 W01，v2/v3 记录为
  `Direct Evolution`，绝不倒灌为事件时证据。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01149；https://arxiv.org/pdf/2501.01149v1；
  https://arxiv.org/pdf/2501.01149v2；https://arxiv.org/html/2501.01149；
  https://github.com/YuxiangChai/AITK。
- **Access and Verification Status:** v1/v2/v3 papers verified；当前 AITK repository verified as later artifact；
  W01 对应 commit、21-app emulator image、task snapshot 和原始 agent trajectories 为 `Not Disclosed / Unverified`。
- **Full-read Coverage:** 三版 metadata/title/scope diff；v1 Introduction/Related Work、controller/translator/evaluator、
  unified action space、task taxonomy、function/LLM evaluators、InternVL2/GPT-4o/AppAgent experiments、error cases、
  limitations/conclusion；v2 essential-state/ESAR 与 evaluator voting evolution；v3 AITK reset/trajectory suite、A3RM
  data/training/evaluator experiments、window/cost study、risks/generalization appendix；当前 repository emulator
  duplication、resume、trajectory visualization、human annotation、custom task 与 A3RM evaluation paths。
- **Original Problem:** static next-action benchmark 以 ground-truth history 喂给每一步，错误不会改变后续 state，
  因而测不到 error propagation、recovery、stop condition、online content 和 multi-frame information query；已有
  dynamic benchmark 又多依赖少量 offline/open-source apps 与 task-specific code。
- **Why the Previous Design Was Reasonable:** static frame/action matching 数据易规模化、可复现、无需账号/网络和
  外部 app version，适合测 screen grounding；instrumented open-source apps 可读取内部状态，给出确定性 oracle 和
  稳定 reset。它们优化 controlled correctness，而非 ecological validity。
- **Changed Constraint:** mobile Agent 要在 mainstream third-party online apps 上执行多步 operation 与信息查询；
  每个动作会改变真实环境，app UI/content/version 不受 benchmark owner 控制，且不同训练集 action schema 不一致。
- **Mechanism:** v1 以 Appium controller 获取 screenshot/XML/history，translator 将不同 agent action schema 归一为
  CLICK/SCROLL/TYPE/ENTER/BACK/HOME/COMPLETE/IMPOSSIBLE/Open/Long Press/WAIT 等 device commands；loop 到
  agent complete 或 max steps，再由 evaluator 判定。201 tasks 分 operation、single-frame query、multi-frame query，
  难度按 human steps。canonical branch 为人工验证的 per-task function：XML/OCR element matching、action-coordinate
  matching 或组合；scalable branch 用 GPT-4o/Gemini 读取 final 或 XML sequence，agreement 时接受、disagreement
  时交给 human。v2 才把 task 分解为 essential states，以 sliding window 对 partial progress 计 ESAR；v3 再将
  trajectory capture/reset 与 evaluator model 训练产品化为 AITK/A3RM。
- **State Ownership / Control and Data Flow:** app/vendor/network 拥有 external truth 和 dynamic content；emulator/
  controller 拥有 device lifecycle、account snapshot、screenshot/XML/action trace；translator 拥有 action-schema
  normalization；agent 只拥有 proposal/history；task function 或 judge 拥有 evidence interpretation，human audit
  拥有 disputed verdict。版本、locale、account、time、network、app state、trajectory 和 evaluator revision 若未共同
  固化，success rate 不可复算。
- **Implementation Details:** v1 基于 Appium；controller → agent → translator → device 循环，最终 evaluator 读取
  state/trajectory。function generation 实验中 GPT-4o 只生成 24% 全部正确函数，27% generated lines 被 coding
  experts 判为错误，说明 LLM 更适合 scaffold 而非无人审核 oracle。whole-task evaluator 在 50 tasks 上人工核验，
  GPT-4o 84%、Gemini 1.5 Pro 80%；作者以两者 agreement 估计误判约 0.03，但没有披露 error correlation、类别分层、
  confidence interval 或 disagreement rate。当前 AITK 的 clean-base AVD duplication、crash replacement、resume 与
  trajectory persistence 是后续 artifact，不能视为 v1 已公开实现。
- **Evaluation Contract:** v1 为 21 mainstream apps/201 distinct tasks；动态结果测试 AMEX + AndroidControl
  fine-tuned InternVL2-8B、GPT-4o+Set-of-Mark 与 AppAgent。InternVL2 在 static AndroidControl high-level subsets
  报 51.8%～73.7%，low-level 为 83.0%～92.1%；进入 A3 后 easy/medium/hard 仅 23.4/5.6/2.0%，AppAgent
  为 30.8/7.0/2.0%，所有 agent multi-frame query 为 0%。device 型号/Android/app version、network snapshot、
  account/locale、trial count、randomness、agent prompt、training compute、latency/cost、hardware/precision 和 SLO
  多数 `Not Disclosed`，所以数字只能说明作者 snapshot 下的 static-to-dynamic gap。
- **Baselines / Ablations / Sensitivity:** v1 不是严格 factorized ablation；比较 static vs dynamic、fine-tuned model vs
  commercial model vs AppAgent scaffold、operation vs query、easy/medium/hard，并列出 wrong click、meaningless
  action、typing before focus、cannot stop 四类 failure。v2/v3 的 essential-state、judge voting、sliding-window 与
  A3RM 是后续机制证据；不用于重新解释 v1 排名。
- **What the Evidence Proves:** v1 直接证明同一 fine-tuned agent 在 teacher-history static evaluation 和 self-owned
  trajectory dynamic environment 间存在巨大 gap；一旦 action 改变 state，grounding、planning、information memory、
  recovery 与 termination 会共同决定结果。人工验证 function 提供较强 oracle，但 task expansion 成本高；LLM judge
  能减少部分 coding/human workload，却在小样本审计中仍约 16%～20% 不一致。
- **What It Does Not Prove:** 21-app snapshot 不等于完整真实世界，也不证明商业 LLM model capability 本身优于
  smaller GUI model；AppAgent 同时改变 foundation model、exploration、prompt 和 scaffold。authors 的双-judge
  0.03 不能在未知 error correlation 下当成 measured accuracy；v1 也没有 essential-state reward model、稳定 reset
  artifact 或 v3 agent leaderboard，不能用后发版本填补事件时缺口。
- **Limitations / Trade-offs / New Failure Modes:** online apps 提高 ecological validity，却引入 version drift、账号/
  地域/时间/价格变化、网络波动、登录和 privacy 风险；统一 action space 增强兼容性，也可能掩盖原生 tool semantics；
  function oracle 精确但脆弱且人工昂贵，LLM judge 灵活却有 correlated hallucination。真实 state transition 暴露
  recovery 能力，也让一次误触产生购买、消息或导航等 side effect；benchmark 必须增加 sandbox、spend/permission
  envelope、cleanup、idempotency、human abort 与 audit retention。
- **Where the Previous Design Still Applies:** component-level grounding regression 继续用 static benchmark；需要
  deterministic correctness 与 CI 时使用 instrumented open-source/offline apps；高风险 side effects 使用 API mock
  或 sandboxed clone；低频固定任务可保留人工验证 function。online arena 是 deployment-readiness layer，不替代这些
  下层 tests。
- **Evolution Relationship:** `Direct Evolution`（static next-action → interactive online trajectory → v2 essential-state
  partial progress → v3 specialized reward model/toolkit）；`Layering / Dependency`（environment reset → action adapter →
  trajectory → evaluator → human adjudication）；`Alternative Branch`（deterministic function oracle ↔ semantic LLM judge）。
- **ROADMAP Node:** Owner `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62；handoff
  `AGENT-PLATFORM`，Current Ch84，Legacy Ch80，以及 `AGENT-WORKFLOW`，Current Ch81，Legacy Ch77。
- **Target and Adjacent Chapters Read:** Weekly-only phase；仅解析 Stable Node，不进入 Books，不把 v3 current
  artifact 当作 W01 integration decision。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** event-time repository/commit、21 apps 与 201 tasks snapshot、app/device/account/workload manifest、
  repeated-run variance、judge disagreement/error correlation、side-effect sandbox、v1→v2 task/app diff，以及后续
  A3RM 是否在 unseen apps/tasks 与独立 human audit 上保持 calibration。

### Dynamic Scaling of Unit Tests: From Fixed Verifier Budget to Difficulty-conditioned Executable Evidence

- **Candidate / Week / Score:** Dynamic Scaling of Unit Tests for Code Reward Modeling / 2025-W01 / 23/30；
  全文审计后 Source Reliability 由 5 调为 4。论文、模型、数据与代码均公开，但 FAR/FRR 使用非标准定义，
  multiple-test quality metric 又把 selection 与 per-solution correctness 混合，动态分配相对固定 budget 的
  gold-pass-rate 增益较小，故不能按 discovery 阶段评分保留满分可靠性。
- **Source Family ID:** `coderm-dynamic-unit-test-verifier-budget`。
- **Source Type:** 作者论文、project page、model/data cards 与官方代码；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv 仅有 v1，提交于 2025-01-02 04:33:31 UTC；
  ACL 2025 接收与后续 artifact 更新属于 publication/artifact evolution，不作为 W01 新事件重复计分。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01054；https://arxiv.org/html/2501.01054；
  https://code-reward-model.github.io/；https://github.com/RUCKBReasoning/CodeRM；
  https://huggingface.co/KAKA22/CodeRM-8B；https://huggingface.co/datasets/KAKA22/CodeRM-UnitTest。
- **Access and Verification Status:** Verified；论文 Method、公式、实验、ablations、appendices 及当前公开模型、
  约 60K synthetic training data、Docker execution environment、preprocess/inference/evaluation code 均可访问。
  event-time commit hash 与当时依赖镜像未在论文中冻结，复现仍需自行固定 revision。
- **Full-read Coverage:** metadata、Introduction/Related Work、unit-test scaling pioneer study、CodeRM-8B synthetic
  data construction、quality control、best-of-N reward、difficulty probe、dynamic allocation objective/greedy algorithm、
  HumanEval+/MBPP+/LiveCodeBench setup、reward baselines、unit-test quality、data/dynamic ablations、sampling sensitivity、
  error examples、limitations、metric definitions、training/evaluation appendices，以及 model/data/code artifacts。
- **Original Problem:** code reward model 若直接打一个 scalar，判定依据难以审计；deterministic unit tests 可执行，
  但固定生成少量 tests 容易漏掉边界条件，固定大量 tests 又把相同 verifier compute 分给难度不同的问题。
- **Why the Previous Design Was Reasonable:** 固定 test budget 容易复算、容量规划和公平比较；hand-written tests
  具有明确 provenance；pass count 是可执行证据，比同一 LLM 的主观评分更接近任务语义。它的不足是 coverage，
  而不是 deterministic execution 本身失效。
- **Changed Constraint:** best-of-N 将每题扩展为最多 100 个 candidate solutions；verification cost 随 solution ×
  unit-test 乘积增长，且简单题较早饱和、困难题需要更多 discriminative tests。系统需要在固定总 budget 下决定
  每题增加 verifier compute 的边际价值。
- **Mechanism:** pioneer study 对每题采样最多 200 个 solutions 与 100 组 unit tests，以各 solution 通过的 test
  数量排序。CodeRM-8B 从 CodeFeedback-Filtered-Instruction 与 TACO 取题，Llama3.1-70B 过滤/规范化题解并生成
  tests；tests 先在 reference solution 上执行，失败时带 Python feedback repair，再保留能拒绝弱模型错误答案的
  tests，用其 SFT Llama3.1-8B。动态分配先以当前 tests 对 policy solutions 的 pass rate 近似题目难度，再用
  hidden-state 两层 probe 预测该 pass rate；在总 verifier budget 下，以 `q(x,b)=1-(1-lambda(x))^b` 的边际收益
  贪心分配额外 tests。
- **State Ownership / Control and Data Flow:** policy 拥有 candidate-solution distribution；unit-test generator 只
  提议 verifier programs；Python sandbox 执行并拥有每个 solution/test 的 pass/fail observation；ranking controller
  聚合 pass count 并选择 candidate；difficulty probe 与 budget allocator 拥有每题 test 数量。reference solution、
  generated tests、execution image、candidate set、probe version 与 allocation trace 必须共同版本化，否则 reward
  不能复算。unit-test model 不拥有 ground truth，执行通过也只证明被生成 tests 覆盖的行为。
- **Implementation Details:** CodeRM-8B 基于 Llama3.1-8B-Instruct，model card 标记 BF16；训练集公开约 60K
  高质量 synthetic Python tests。Best-of-N 主实验每题 100 个 solutions、100 个 unit-test inferences；temperature
  0.8、top-p 0.95，frequency/presence penalty 为 0。论文写全部 models 在 8×NVIDIA A800 上部署/推理，但同时
  包含 GPT-3.5 与 GPT-4o-mini API policies，无法据此判定 proprietary calls 的实际 hardware；open-model precision、
  batch、concurrency、runtime version、wall-clock 与 SLO 也为 `Not Disclosed`。
- **Evaluation Contract:** HumanEval+、MBPP+ 与 2024-01～09 LiveCodeBench functional subset；LiveCodeBench
  仅 168 queries。四个 policies 为 Llama3-8B、Llama3-70B、GPT-3.5、GPT-4o-mini。作者在同样 100 次 verifier
  inference budget 下比较 Llama unit-test generators、ArmoRM、MBR-Exec、CodeT 与 MPSC；但不同方法每次生成
  的 tests/specs 数量和执行代价不同，equal inference count 不等价于 equal tokens、latency、energy 或 sandbox cost。
- **Baselines / Ablations / Sensitivity:** 对比 random solution、Llama3.1-8B/70B generated tests 与 CodeRM-8B；
  synthetic data 的 zero-shot、无 quality control、带 quality control；固定 tests 与 predicted/gold difficulty 动态分配；
  unit-test count、solution count 与 problem difficulty sensitivity。作者观察增加 tests 通常改善 selection，困难题收益
  更大，但当 solution pool 增长时可能出现针对有限 tests 的 adversarial solutions；dynamic allocation 在 gold pass
  rate 下相对 fixed allocation 的提升仍很小，论文也承认 response-budget 方法直接迁移到 reward budget 未必合适。
- **What the Evidence Proves:** 在上述 Python function-generation workload 与作者 candidate distribution 中，
  扩大独立生成并执行的 unit-test set 能提高 best-of-N selection；经 synthetic quality control 训练的 8B generator
  可接近 70B test generator 的选择效果；difficulty-conditioned allocation 展示了“verification compute 也可调度”的
  可行性。主表提升只能绑定具体 policy/benchmark，例如 HumanEval+ 上 Llama3-8B 从 53.58 到 72.01，不能脱离
  100 solutions、100 tests 与作者 harness 写成通用 18.43-point 收益。
- **What It Does Not Prove:** 不证明 generated tests 是完整 correctness oracle，也不证明更多 tests 单调提高安全性；
  不证明 difficulty probe 对新 language、repository task、proprietary model hidden state 或 distribution shift 可用。
  proprietary API policy 无法直接提供同构 hidden state，因此动态机制不能无条件落地。论文的 FAR 定义为
  `FP/(FP+TP)`（实际更接近 `1-precision`），FRR 定义为 `FN/(FN+TN)`，均非通常分类定义；multiple-test setting
  又只把最高 ranked candidate 标为 positive、其余为 negative，多个正确 solutions 可能被当作 negative。因此相关
  accuracy/F1/FAR/FRR 不能当作独立的 per-solution verifier calibration 证据。
- **Limitations / Trade-offs / New Failure Modes:** 更多 tests 提高 coverage，却线性增加 generation 与 sandbox
  execution；相似或共享 blind spot 的 tests 只有数量、没有独立性。过滤流程以 reference solution 为 oracle，若题解、
  prompt 或 dependency 有错会固化错误 tests；以弱模型 wrong solutions 筛选会过拟合其 error distribution。新增
  reward hacking、flaky/nondeterministic tests、resource-exhaustion tests、sandbox escape、dependency drift、test leakage、
  difficulty miscalibration 与 hard-case starvation。probe savings 还要扣除 hidden-state access、训练和在线推断成本。
- **Where the Previous Design Still Applies:** safety-critical 或 repository CI 应优先保留人工/规范派生 tests、compiler、
  proof assistant 与 environment oracle；题目短、固定 budget 足够或需要严格 fairness 时固定 tests 更简单；没有 hidden
  state 或 difficulty calibration 时可按 observable execution statistics 分桶，而不是假设动态 allocator 可迁移。
- **Evolution Relationship:** `Direct Evolution`（single scalar judge → generated executable tests → scaled test ensemble →
  difficulty-conditioned verifier budget）；`Layering / Dependency`（test proposal → sandbox execution → evidence aggregation →
  candidate selection）；`Alternative Branch`（fixed auditable budget ↔ adaptive efficiency）。
- **ROADMAP Node:** Owner `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62；handoff `INFER-SCHEDULING`，
  Current Ch56，Legacy Ch52，以及 `AGENT-WORKFLOW`，Current Ch81，Legacy Ch77。
- **Target and Adjacent Chapters Read:** Weekly-only phase；Stable Node 用于 future integration positioning，本轮不打开
  Books Gate，也不把 existing coverage 当成吸收结论。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** event-time code/image revision、equal wall-clock/energy verifier budget、标准 calibration metrics、
  test diversity/independence、跨语言/repository generalization、sandbox threat model，以及只依赖 observable state 的
  dynamic allocation 是否能保留同等收益。

### SSM Bottlenecks: Stable Forgetting, Long-range Recall and the Depth–Smoothing Tension

- **Candidate / Week / Score:** Understanding and Mitigating Bottlenecks of State Space Models through the Lens of
  Recency and Over-smoothing / 2025-W01 / 22/30；全文审计后 Source Reliability 由 5 调为 4，因为理论只覆盖
  满足 diagonal/contraction 等假设的 recurrence，security claim 从 sequential CIFAR-10 perturbation 推断到 LLM
  jailbreak 而没有直接语言实验，mitigation 也只在 synthetic associative recall 上验证。
- **Source Family ID:** `ssm-recency-oversmoothing-polarization`。
- **Source Type:** arXiv v1/v2、ICLR 2025 paper 与作者代码/checkpoints；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 实际提交于 2024-12-31 22:06:39 UTC，不是旧表的
  2025-01-01；v2 于 2025-03-11。按 UTC first-public date，它仍属于 ISO 2025-W01。W01 结论以 29 页 v1 为
  event-time source；v2/ICLR 与当前代码只补充 artifact/version 边界，不倒灌成新的 W01 结果。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00658；https://arxiv.org/pdf/2501.00658v1；
  https://arxiv.org/html/2501.00658；https://github.com/VITA-Group/SSM-Bottleneck；
  https://openreview.net/forum?id=pymXpl4qvi。
- **Access and Verification Status:** v1/v2 paper、proofs、appendices、current code 与 downloadable-checkpoint path
  verified；OpenReview 页面当前受 challenge 阻挡，但 arXiv 与 repository 足以核验主要机制。repository 只有 6 个
  commits、无 release/tag；event-time commit 与完整 training environment 未冻结。
- **Full-read Coverage:** metadata/revision、SSM/S4/Mamba/linear-attention unified recurrence、recency theorem/proof、
  influential-score experiment、needle retrieval、CIFAR sequential corruption/target attack、depth–context scaling、
  low-pass/over-smoothing theorem/proof、HiPPO/selection/complex-parameter discussions、polarization mechanism、MQAR
  ablation、training-size appendix，以及 current attack/MQAR code and dependencies。
- **Original Problem:** diagonalized/selective SSM 用固定大小 recurrent state 避免 attention 的 quadratic pairwise
  compute 与不断增长的 KV state；但“能处理很长 sequence”不自动等于任意远 token 仍能以足够权重影响当前输出，
  validation perplexity 也可能掩盖 positional recall failure。
- **Why the Previous Design Was Reasonable:** `0 < A_t < 1` 的衰减使 recurrence 数值稳定、利于 length
  extrapolation，并给自然语言常见的局部依赖合理 inductive bias；diagonalization 与 selection 换取 parallel scan、
  compact state 和 content-dependent filtering。遗忘是稳定有限状态的设计预算，不是单纯缺陷。
- **Changed Constraint:** workload 从局部 next-token statistics 转向远距离 exact recall；一种直觉补偿是增加 depth
  扩大 effective receptive field，但 repeated mixing 又可能让 token/state representation 逐层失去区分度。系统必须在
  memory retention、state stability 与 representational sharpness 之间共同设计，而不是只扩大 context length label。
- **Mechanism:** 对 `h_t=A_t h_{t-1}+Delta_t b_t(x_t)`，Theorem 3.1 在 compact input、连续可微参数以及
  diagonal `A_t` 且每个元素严格位于 `(0,1)` 时，证明 distant token influence 以 `exp(-k(t-s))` 上界衰减；
  `A_max` 越小，recency 越强。深层堆叠扩大局部 kernel 的传播距离；另一方面，continuous S4 在 negative diagonal
  `A` 下表现为 low-pass filter，discrete theorem 在 `A_t+Delta_t<=1` 与 centered/non-expansive 条件下给出 memory
  pairwise distance contraction。mitigation 将 state-transition 的一个 channel 固定为 1 保留历史，另一个固定为 0
  保留当前 token sharpness，其余 channels 继续学习，形成 polarization。
- **State Ownership / Control and Data Flow:** recurrent layer 拥有 fixed-size hidden state；每步 `A_t` 决定旧状态
  retention，`Delta_t b_t(x_t)` 决定新信息写入，`c_t` 读取输出。all-one channel 相当于不衰减 accumulation path，
  all-zero channel 相当于 current-token path；跨 layer mixing 决定 state discrimination。该 state 是 model-execution
  state，不包含 external memory 的 provenance、delete、tenant isolation 或 exact token identity。
- **Implementation Details:** Mamba polarization 在 pre-exponential diagonal `A` 前置 0，使 `exp(Delta_t A)=1`；
  后置约 -1000，使另一 channel 指数后近似 0。current repository 基于 Zoology，development versions 为
  `mamba_ssm==1.1.4`、`causal_conv1d==1.1.0`、`transformers==4.43.3`，后来兼容 `mamba_ssm==2.2.4`；提供
  CIFAR attack、MQAR 与 4-GPU parallel-launch scripts，但硬件型号、precision、wall-clock、energy 与 production
  recurrence kernel overhead 为 `Not Disclosed`。
- **Evaluation Contract:** retrieval 对比 Mamba-Codestral-7B 与 Mistral-7B，在 10,240～22,528 token documents
  中改变 needle position；并非同 architecture/parameter/training data 的严格 controlled baseline。robustness 实验把
  CIFAR-10 的 32×32 RGB 像素 flatten 成 1,024-token causal sequence，并把 class token 固定在末尾；H3/RWKV/
  Mamba/Transformer 均 3 layers、hidden 32、state 64、100 epochs。depth scaling 用 Mamba、context 2,048/8,192、
  16～72 layers，约 100M～550M 参数与 2.5B～10B tokens。polarization 只在 64/128/256 KV-pair MQAR 上比较
  2/4-layer variants。
- **Baselines / Ablations / Sensitivity:** trained/untrained、130M/1.4B influential scores；Mamba-Codestral-7B vs
  Mistral-7B needle position；leading/trailing/random/target pixel corruption；depth × width × context；1-polarized、
  0-polarized、dual-polarized 与 default Mamba。4-layer dual-polarized MQAR 在 256 pairs 为 81.56，对 default
  4-layer 的 33.52；该数字只属于 synthetic setup，不能写成 general long-context gain。
- **What the Evidence Proves:** 在定理假设下，一层 diagonal contractive SSM 的 direct influence 随 distance
  指数衰减；在作者分析条件下 repeated state mixing 会收缩 representation differences。实验一致显示所测 Mamba
  的 positional recency、depth saturation，以及 zero/one channels 在 MQAR 中分别缓解 depth smoothing 与 long-range
  retention。它把“state compression 的代价”从泛化直觉推进到可检查的 transition-spectrum 条件。
- **What It Does Not Prove:** 不覆盖 non-diagonal、non-contractive、explicit skip/memory、hybrid attention 或不满足
  normalization assumptions 的所有 SSM；influence-gradient 上界不等同于 task-level impossibility。Mamba-Codestral
  与 Mistral 的 needle 对比混入 training/model differences。CIFAR 中 class token 被有意放在 sequence 末尾，作者也
  承认 mean pooling 或 middle token 更 robust；因此它不能证明真实 SSM LLM 更容易 jailbreak，论文 3.3 的语言安全
  结论应标记为作者推断，而非实验事实。MQAR 改善也不证明 language-model perplexity、quality 或 serving efficiency。
- **Limitations / Trade-offs / New Failure Modes:** 更接近 1 的 transition 延长记忆，也会累积噪声、放大 stale
  information 并削弱 forgetting；更接近 0 保持 local sharpness，却丢弃 history。增加 depth 扩大传播距离，同时增加
  compute、optimization burden 与 over-smoothing；延长 training context 可能减慢 smoothing，却增加训练成本。
  fixed all-one channel 可能无界积累、对 reset/boundary 敏感；fixed all-zero channel 牺牲该维历史容量。hybrid path
  还需要 scale/gate calibration，否则不同 channels 的 magnitude 和 gradient contribution 会失衡。
- **Where the Previous Design Still Applies:** local-dominant、streaming、strict O(1) recurrent state 或 sequence 很长但
  不要求 exact distant recall 的任务，decaying SSM 仍合理；需要 exact arbitrary-position retrieval 时 dense/sparse
  attention 或 external indexed memory 更直接；短 context 不应为修复不存在的 recall pressure 盲目增加 depth。
- **Evolution Relationship:** `Direct Evolution`（stable decaying recurrence → content selection → depth compensation →
  polarization）；`Alternative Branch`（compact recurrent state ↔ exact token-addressable attention/external memory）；
  与 Titans test-time parametric memory 为 `Principle Reuse`，不是同一种 state ownership。
- **ROADMAP Node:** Owner `MODEL-LONG-CONTEXT`，Current Ch22，Legacy Ch22；handoff `MODEL-ATTENTION`，
  Current Ch14，Legacy Ch14，以及 `PLATFORM-SECURITY`，Current Ch72，Legacy Ch68（只传递 threat hypothesis，
  不传递未经语言实验验证的 jailbreak claim）。
- **Target and Adjacent Chapters Read:** Weekly-only phase；本轮只解析 owner/handoff，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** non-diagonal/hybrid architectures 是否满足类似 bound、polarized channel 的长期 state magnitude、
  language-model downstream 与 kernel overhead、matched-model needle comparison、真实 prompt-order attack，以及在同
  parameter/token/compute budget 下 context-depth joint scaling 的规律。

### TAPE: From Fixed Position Bias to Layer-wise Contextual Addressing State

- **Candidate / Week / Score:** TAPE: Rethinking Addressing in Language Models via Contextualized Equivariant Positional
  Encoding / 2025-W01 / 23/30；统一使用论文方法名 TAPE，不再写成 CoPE。全文审计后 Source Reliability 由 5
  调为 4：证据来自作者、训练规模有限、SCROLLS 结果并非每项领先，且“minimal/negligible overhead”与作者表中
  相对 RoPE 增加约 13.9% FLOPs、fused attention throughput 仍低约 18.7% 的数据不应混写。
- **Source Family ID:** `tape-contextual-equivariant-positional-state`。
- **Source Type:** arXiv v1/v2、ICML 2025 paper 与作者代码；Status: Experimental。
- **Event Date / First-public Date / Revision History:** v1 于 2025-01-01 03:23 UTC；v2 于 2025-08-21。v1
  已包含 contextual position update、equivariance、arithmetic/C4/SCROLLS/Llama2 experiments 与 efficiency；v2 才
  新增 NC1 circuit representational-power theorem、state-tracking construction 及扩展实验。W01 不使用 v2 theorem
  支撑 event-time novelty，只把它记录为同 Source Family 的后续理论演进。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00712；https://arxiv.org/pdf/2501.00712v1；
  https://arxiv.org/pdf/2501.00712v2；https://github.com/VITA-Group/TAPE。
- **Access and Verification Status:** Verified；v1/v2 papers、appendices、current 51-commit repository、arithmetic
  submodule、pretrain/SCROLLS/Llama2 scripts 与 evaluation paths 可访问。无 release/tag，event-time commit、数据
  snapshot 与 fused kernel revision 未冻结。
- **Full-read Coverage:** metadata/version diff、position/content addressing framing、absolute/relative/RoPE/ALiBi/FIRE/
  NoPE background、tensorial positional features、permutation/O(R) equivariance、token mixing、position contextualization、
  RoPE initialization/PEFT、v1 propositions/proofs、arithmetic、C4→SCROLLS、Llama2 context extension/passkey、efficiency、
  architecture/YaRN ablations、limitations；另核验 v2 新增 NC1 theorem 只属于后续 revision，以及 repository contracts。
- **Original Problem:** fixed absolute/relative position encoding 为全 dataset 学一个静态 bias，容易把 distance decay
  当作普适规律；但 arithmetic、counting、algorithmic state tracking 等任务需要“哪一个位置重要”随当前 sequence
  content 和 layer computation 变化。纯 content similarity 又难以表达同值 token 的次序和相对角色。
- **Why the Previous Design Was Reasonable:** sinusoidal/RoPE/ALiBi 结构简单、cache identity 清晰、易与 fused
  attention 结合，并把 translation/relative-position bias 固化成稳定 inductive prior；自然语言大量依赖局部 content，
  fixed bias 往往已足够。它们优化通用性、效率和 extrapolation predictability，而非 instance-specific algorithmic address。
- **Changed Constraint:** 对同一 token sequence，不同 layer 可能需要先按 content 找到结构关系，再把该关系转成后续
  position-based address；静态 PE 无法在执行过程中积累这种 derived coordinate。设计必须允许 position state 可变，
  同时保留 token permutation 与 global position shift 下的稳定语义。
- **Mechanism:** TAPE 把 token feature `X` 与 tensorial position feature `E` 分开维护。每层 token mixer 的 attention
  logit联合 token query/key 与 position inner product；同一 attention weights 又线性组合 position features，生成中间
  `E~`。随后由 token-conditioned diagonal transformation 和 shared `W1/W2` 更新 position state，供下一层使用。
  约束 token/position tuple 的 permutation equivariance，以及最后一维 orthogonal transformation 下 token output invariant、
  position output equivariant；RoPE/random Fourier 的 global phase shift 因而不改变最终 token output。RoPE 是特定
  `L=R=2` initialization；PEFT 用 zero-initialized `W2` 保证初始行为回到 base model，只训练 contextualizer 和
  post-attention linear weights。
- **State Ownership / Control and Data Flow:** static RoPE 只由 token index/model config 定义；TAPE 的 `E^(l)` 则是
  request content、mask、layer、model revision 共同决定的 ephemeral derived state。`X^(l),E^(l),mask` 进入 layer，
  attention 同时更新 token 与 position paths，再由 position MLP 更新 `E`。因此 cache/recompute 不能只以 token IDs
  和 absolute offset 识别，至少要绑定 model/layer/mask 与 derived-position path；论文没有设计 production KV reuse、
  prefix sharing 或 distributed state transfer contract。
- **Implementation Details:** v1 使用 RoPE initialization，tensor position 形状扩展到 head/block/`L×R`，实验将
  position MLP intermediate `I` 设为 `4H`，权重可跨部分维度共享。代码继承 BiPE/LongLoRA，提供 C4 pretrain、
  SCROLLS fine-tune/generate/evaluate、Llama2-7B PEFT/perplexity/passkey scripts。repository 仍以内部名 `adape`
  表示 TAPE，arithmetic 为外部 submodule；这些版本依赖需共同固定才能复现。
- **Evaluation Contract:** arithmetic 使用 Addition Bucket 40 的 20M samples，训练最大 operand length 40、测试到
  80，每个 length pair 100 examples，严格 exact-match；比较 RoPE/RandPE/NoPE/FIRE。scratch LM 为约 155M
  decoder-only model，C4 sequence 1,024、batch 512、10K iterations，再在七个 SCROLLS tasks fine-tune。context
  extension 以 Llama2-7B 从 4,096 到 8,192，RedPajama fine-tune、Proof-pile/PG19 perplexity 与 1K～8K passkey；
  batch 64、1K iterations。hardware 只在 attention microbenchmark 披露 single A100；precision、A100 variant、
  end-to-end training/serving latency、KV memory、concurrency 与 SLO 为 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity:** arithmetic 与 RoPE/RandPE/NoPE/FIRE；SCROLLS 加 ALiBi/xPos；Llama2 PEFT
  与 LoRA/LongLoRA/Theta Scaling；rotation equivariance、tensor structure、attention/MLP contextualizer、20→40 vs
  40→80 difficulty、TAPE+YaRN。v1 arithmetic average 为 32.82%，FIRE 26.98%；较容易的 20→40 setting 仅 41.42
  vs 39.44。SCROLLS 中 TAPE 并非所有 tasks 第一，例如 Qasper 和 GovReport 分别落后 RandPE 与 ALiBi，不能写成
  universal superiority。
- **What the Evidence Proves:** 在作者的小规模 decoder-only、arithmetic、SCROLLS 与 Llama2-7B 8K PEFT contract
  内，layer-wise content-conditioned position state 是可训练的，并在多项 address-sensitive tasks 上优于所选 fixed-PE
  baselines；permutation/orthogonal equivariance 能在给定构造中保持 global shift invariance。它提供一种“位置不是只读
  metadata，而是可演化 intermediate state”的设计分支。
- **What It Does Not Prove:** v1 不证明 TAPE 可模拟 NC1；该 theorem 属于 2025-08 v2，且 constructive expressivity
  也不等于 SGD 会学到相应 algorithm。8K passkey 不等价于 natural long-context reasoning；155M/Llama2-7B 不能
  外推现代大模型、multimodal position 或 production serving。equivariance 保证特定 transformation consistency，不
  保证 factual robustness、OOD quality 或 cache correctness。
- **Limitations / Trade-offs / New Failure Modes:** dynamic `E` 提高 address expressivity，却使每层多一条 mutable state
  path，增加 FLOPs、memory traffic、kernel fusion 与 cache identity complexity。v1 batch1/seq1024 表中 TAPE 365.65G
  FLOPs vs RoPE 321.10G、180.69G vs 160.46G MACs；fused TAPE 3910 iterations/s vs RoPE 4810，故“接近”不等于
  零成本。context-conditioned positions 可能过拟合 content pattern、在 prompt injection 或 prefix reuse 时污染 derived
  address；partial recompute、chunked prefill、sequence packing 与 speculative rollback 都需明确恢复 `E^(l)` 的边界。
- **Where the Previous Design Still Applies:** 普通 language modeling、成本敏感 serving、需要成熟 fused kernels 或
  stable prefix/KV sharing 时 RoPE/ALiBi 更简单；仅需扩大 RoPE window 可优先 YaRN/interpolation/scaling；任务确实
  需要 instance-specific position algorithm、且额外 state path 能被工程化时才考虑 contextual PE。
- **Evolution Relationship:** `Direct Evolution`（absolute/fixed relative PE → trainable relative bias → context-conditioned
  counting/address → layer-wise derived position state）；`Layering / Dependency`（RoPE initialization → equivariant update →
  token mixing）；`Alternative Branch`（static cache-friendly coordinate ↔ adaptive address expressivity）。
- **ROADMAP Node:** Owner `MODEL-POSITION-ENCODING`，Current Ch13，Legacy Ch13；handoff `MODEL-ATTENTION`，
  Current Ch14，Legacy Ch14，以及 `MODEL-LONG-CONTEXT`，Current Ch22，Legacy Ch22。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只完成 Stable Node 定位，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** event-time commit/fused kernel、full-model而非 attention-only overhead、derived position 与 KV/prefix
  identity、chunk/packing/rollback semantics、现代大模型与更长 context 的 scaling，以及 v2 expressivity construction
  在 finite precision 和 learnability 条件下是否仍有工程意义。

### VideoAnydoor: Separating Object Identity from Motion-conditioned Video Editing

- **Candidate / Week / Score:** VideoAnydoor / 2025-W01 / 21/30。
- **Source Family ID:** `videoanydoor-identity-motion-video-editing`。
- **Source Type:** 作者论文；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 于 2025-01-02；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01427；https://arxiv.org/html/2501.01427。
- **Access and Verification Status:** Verified；正文、方法、实现、evaluation、ablation 与 limitations 可访问。
- **Full-read Coverage:** metadata、Introduction、Related Work、end-to-end architecture、pixel warper、semantic
  point tracking、reweighted diffusion loss、mixed-data construction、implementation、comparison、ablation 与 failure cases。
- **Original Problem:** 先编辑第一帧再传播的 two-stage pipeline 容易让 reference identity、遮挡与运动轨迹在时间上
  漂移；只把 reference feature 注入 video generator 又缺少明确 motion control。
- **Why the Previous Design Was Reasonable:** image editor 与 propagation model 可以分别复用成熟组件，训练与调试边界
  清楚；短片、弱运动或身份要求不高时，模块化 pipeline 的成本更低。
- **Changed Constraint:** workload 同时要求 reference object identity、box/point trajectory、遮挡和长时间 temporal consistency，
  两阶段误差开始累积。
- **Mechanism:** 3D U-Net 联合接收 source/masked/noisy latent video；DINOv2 tokens 表示 reference identity，pixel warper
  将 reference keypoints 对齐到轨迹，ControlNet-style multi-scale path 注入运动条件；region/trajectory reweighting 让训练目标
  更关注被编辑对象，real video 与 image-simulated video 混合训练补充运动覆盖。
- **State Ownership / Control and Data Flow:** reference image 提供 identity state，box/semantic point sequence 提供 motion
  state，warper 形成 frame-aligned condition，再由 denoiser 联合提交整段 video。模型没有提供跨请求 durable identity、编辑
  provenance、partial regeneration 或 rollback contract。
- **Implementation Details:** 基于 SDXL 与 motion modules，512×512，Adam `1e-5`，120K iterations，16×A100，batch 32；
  DDIM 50 steps、CFG 10、8 semantic points。precision、A100 variant、serving latency、concurrency 与 SLO 未披露。
- **Evaluation Contract:** 作者构建 200 条 Pexels video benchmark，使用 CLIP/DINO/PSNR 与 CoTracker AJ/δ/OA，并做
  human preference；所有数字只适用于该 object editing contract。
- **Baselines / Ablations / Sensitivity:** two-stage/injection baselines；移除 pixel warper、semantic points、reweighted loss，
  以及 real/simulated data variants。human-study 描述中的 annotator 数存在文本不一致，因此不把 win rate 当独立事实。
- **What the Evidence Proves / Does Not Prove:** 证明作者任务内把 identity 与 motion condition 分开建模、再端到端融合，
  可减少部分时序漂移；不证明任意对象、任意长视频、复杂 logo 或 production latency 下成立，也不证明取代模块化 pipeline。
- **Limitations / Trade-offs / New Failure Modes:** 多 condition path 增加 alignment、训练数据、inference compute 与 condition
  conflict；semantic tracker 错误会把 motion control 变成系统性漂移，复杂 logo 仍失败，custom benchmark 规模有限。
- **Where the Previous Design Still Applies:** 单帧质量优先、轨迹简单、数据不足或需要独立替换 editor/propagator 时，two-stage
  仍更易部署；不要求 reference identity 的普通 text-to-video 无需承担该 state contract。
- **Evolution Relationship:** `Direct Evolution`（first-frame edit + propagation → identity/motion-separated end-to-end editing）；
  与 object-centric representation 为 `Layering / Dependency`。
- **ROADMAP Node:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24；handoff
  `MULTIMODAL-REPRESENTATION`，Current Ch23。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只定位 owner/handoff，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** condition conflict、tracker failure detection、long-video state、partial rollback 与真实 serving cost。

### VideoRefer Suite: Object-centric Video Representation Is a Data-and-Evaluation Contract

- **Candidate / Week / Score:** VideoRefer Suite / 2025-W01 / 24/30。
- **Source Family ID:** `videorefer-object-centric-video-understanding`。
- **Source Type:** 作者论文、dataset/model project；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 于 2024-12-31；本周按 first-public date 归档。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.00599；https://arxiv.org/html/2501.00599。
- **Access and Verification Status:** Verified；data engine、model、benchmark、implementation、evaluation 与 limitations 可访问。
- **Full-read Coverage:** metadata、Introduction、Related Work、VideoRefer-700K construction、Analyzer/Annotator/Segmentor/
  Reviewer/Refiner pipeline、object token compression、three-stage-plus alignment training、benchmark、implementation、ablation、appendix。
- **Original Problem:** scene-level video-language tokens 会稀释指定对象的跨帧身份、属性与动作；人工构建 object-level
  video instruction data 又昂贵且难保持 mask/description consistency。
- **Why the Previous Design Was Reasonable:** uniform frame tokens 与 global pooling 接口简单、适合 scene QA；静态 region
  encoder 对 image grounding 足够，且避免额外 segmentation pipeline。
- **Changed Constraint:** question 指向具体、跨帧移动的 object，系统必须把 scene context 与 object trajectory/state 同时交给
  LLM，并知道自动生成的 object annotation 是否可信。
- **Mechanism:** 多 Agent data engine 由 Analyzer、Qwen2-7B Annotator、Grounding-DINO/HQ-SAM Segmentor、Reviewer
  与 Refiner 组成；模型在共享 visual encoder 后用 masks 做 spatial pooling，对相邻帧 object tokens 以 cosine similarity
  合并，再将 scene/object/text tokens interleave 输入 VideoLLaMA2.1。训练依次完成 image-text、region-text、high-quality
  learning 与 instruction tuning。
- **State Ownership / Control and Data Flow:** mask/track identity 由 data pipeline 与 object token compressor 共同定义；scene
  tokens 保存环境，object tokens 保存指定对象，LLM 只消费压缩后的 representation。错误 mask、错误合并或 reviewer false
  negative 会污染后续 instruction data，论文没有 durable provenance/versioning contract。
- **Implementation Details:** SigLIP SO400M visual encoder、Qwen2-based 7B LLM；alignment stages 使用 batch 256、`1e-3`
  或 batch 128、`2e-5`，各一 epoch。hardware、precision、wall-clock、inference latency、concurrency 与 SLO 未披露。
- **Evaluation Contract:** description benchmark 400 entries、GPT-4o judge；multiple-choice benchmark 198 videos/1,000 questions。
  Reviewer 的人工抽样混淆矩阵为 TP 88、FP 12、FN 36、TN 64，说明自动数据 Gate 并非 ground truth。
- **Baselines / Ablations / Sensitivity:** scene-only、object feature extraction/compression 与不同 model variants；benchmark 和
  data 均由作者构建，因此只能支持 in-domain mechanism comparison。
- **What the Evidence Proves / Does Not Prove:** 证明 object mask→跨帧 token→scene/object interleave 可把 referring-video
  问题变成明确 representation contract；不证明获得 pixel grounding、开放世界 tracking、跨 dataset 泛化或无偏 GPT judge。
- **Limitations / Trade-offs / New Failure Modes:** 增加 segmentation/reviewer 成本、mask provenance、track merge threshold、
  scene-object disagreement 与 judge dependence；论文明确不提供 grounding output，不能把 object understanding 写成 localization。
- **Where the Previous Design Still Applies:** scene description、短视频、无需指定实体或算力敏感时 global pooling 更简单；
  需要精确坐标/轨迹时应保留 detection/tracking state，不能只靠 compressed tokens。
- **Evolution Relationship:** `Direct Evolution`（scene-level video tokens → object-conditioned cross-frame representation）；
  `Layering / Dependency`（data engine → representation → benchmark）。
- **ROADMAP Node:** Owner `MULTIMODAL-REPRESENTATION`，Current Ch23；handoff `TRAIN-DATA`，Current Ch27，
  以及 `PLATFORM-EVALUATION-SYSTEM`，Current Ch66。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只完成 Stable Node 定位，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** track identity、annotation provenance、reviewer operating point、grounding extension 与 independent benchmark。

### Reconstruction vs. Generation: Latent Geometry Is an Interface, Not a Free Compression Win

- **Candidate / Week / Score:** VA-VAE + LightningDiT / 2025-W01 / 25/30。
- **Source Family ID:** `va-vae-lightningdit-latent-geometry`。
- **Source Type:** 作者论文与公开实现；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 于 2025-01-02；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01423；https://arxiv.org/html/2501.01423。
- **Access and Verification Status:** Verified；method、training recipe、comparisons、ablations 与 appendices 可访问。
- **Full-read Coverage:** metadata、reconstruction/generation tension、continuous VAE/VQGAN background、visual-foundation
  alignment losses、adaptive weighting、LightningDiT recipe、ImageNet evaluation、tokenizer/generator scale ablations、conclusion。
- **Original Problem:** 提高 latent channel dimension 通常改善 reconstruction，却让 generator 面对更难优化、几何结构更差的
  latent distribution；只报告 reconstruction quality 会把成本转移到后续 diffusion model。
- **Why the Previous Design Was Reasonable:** VAE 作为独立 compression component 易于优化与复用；低维 latent 减少生成
  compute，在小模型与有限数据下往往更稳定。
- **Changed Constraint:** high-fidelity image generation 需要更高容量 latent，同时 training budget 又要求 generator 快速收敛，
  tokenizer 与 generator 不能继续独立选型。
- **Mechanism:** VA-VAE 在 KL tokenizer 上加入 frozen vision foundation model 的 marginal cosine-similarity 与 distance-matrix
  alignment，并用 gradient-norm 自适应平衡；LightningDiT 结合 rectified flow、logit-normal timestep sampling、velocity-direction
  loss、SwiGLU、RMSNorm、RoPE 与 patch size 1，使 generator 更适配高维 latent。
- **State Ownership / Control and Data Flow:** tokenizer revision 决定 latent identity、scale 与 geometry，generator checkpoint
  必须与它绑定；image→latent→flow target→decoder 是一个联合 artifact contract。论文未设计跨版本 compatibility、registry
  metadata 或 production rollback。
- **Implementation Details:** ImageNet-256，tokenizer `f16d16/32/64`，pre-extracted latents；LightningDiT B/L/XL 训练 80/160
  epochs，另报告更长训练。hardware、precision、batch/concurrency、wall-clock 与 SLO 未披露。
- **Evaluation Contract:** class-conditional ImageNet-256 reconstruction/generation；比较 FID、reconstruction 与 convergence。
  “21.8×”基于 epoch/sample 对原始 DiT 的组合差异，不能归因于单一 alignment loss，更不能等价成硬件加速。
- **Baselines / Ablations / Sensitivity:** 不同 foundation encoders、loss components、latent dimensions、model scales 与 recipes；
  DINOv2 alignment 对高维 tokenizer 更有帮助，对低维设置并非同样成立。
- **What the Evidence Proves / Does Not Prove:** 证明作者 contract 下 latent geometry 会影响 downstream generator optimization，
  tokenizer 应以端到端生成目标共同评估；不证明该 loss 对文本/视频、其他 VAE、开放域数据或 production latency 通用。
- **Limitations / Trade-offs / New Failure Modes:** frozen encoder 注入其语义偏置，增加 loss/gradient calibration；高维 latent
  仍增加存储、I/O 与 generation compute，tokenizer-generator version mismatch 会导致静默质量退化；论文没有独立 limitations 节。
- **Where the Previous Design Still Applies:** reconstruction-only、edge deployment、低带宽 latent 或 generator capacity 有限时，
  低维 tokenizer 仍合理；没有匹配 generator 训练预算时不应只追求 reconstruction 指标。
- **Evolution Relationship:** `Direct Evolution`（reconstruction-only tokenizer objective → tokenizer/generator joint contract）；
  与系统 artifact identity 为 `Principle Reuse`。
- **ROADMAP Node:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24；handoff
  `MULTIMODAL-REPRESENTATION`，Current Ch23，以及 `TRAIN-PRETRAINING`，Current Ch28。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只完成 owner/handoff，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** cross-domain transfer、latent schema/versioning、hardware-normalized convergence 与 failure rollback。

### MERV: Multiple Visual Experts Turn Representation Choice into a Placement Problem

- **Candidate / Week / Score:** Unifying Specialized Visual Encoders / MERV / 2025-W01 / 24/30。
- **Source Family ID:** `merv-specialized-visual-encoder-fusion`。
- **Source Type:** 作者论文与 implementation artifact；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 于 2025-01-02；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01426；https://arxiv.org/html/2501.01426。
- **Access and Verification Status:** Verified；architecture、training、evaluation、ablation 与 limitations 可访问。
- **Full-read Coverage:** metadata、single-encoder boundary、four encoder objectives、temporal/spatial alignment、cross-attention
  fusion、frozen/full training、datasets、hardware、held-out evaluation、ablation、limitations。
- **Original Problem:** 单一 visual encoder 的 pretraining objective 很难同时保留 spatial detail、temporal action、image-language
  alignment 与 video-language semantics。
- **Why the Previous Design Was Reasonable:** 单 encoder 的 preprocessing、token schema、placement、versioning 与 latency 简单，
  在明确任务分布内可避免 expert redundancy。
- **Changed Constraint:** general video-language workload 跨越多个 visual subskills，单一 embedding space 成为 bottleneck；需要
  在不让 LLM 接收无限 tokens 的前提下联合多种 expert representation。
- **Mechanism:** 并行运行 DINOv2、ViViT、SigLIP、LanguageBind；按输入帧数对齐 temporal output，用 adaptive 2D average pooling
  对齐 spatial tokens，再线性投影到统一维度并以 cross-attention fusion。MERV-frozen 只训练 alignment，MERV-full 分阶段解冻 LLM。
- **State Ownership / Control and Data Flow:** 每个 encoder 持有独立 preprocessing/model revision，alignment layer 持有 token
  schema，fusion layer 决定下游可见信息；slowest expert、缺失 expert 与 version mismatch 都成为 runtime state，论文没有提供
  production fallback 或 per-expert freshness contract。
- **Implementation Details:** LLaMA2-7B，16 sampled frames，ViViT 32-frame input 输出对齐为 16；Video-LLaVA data。8×L40
  48GB 下少于 24 小时，8×H100 下约 8 小时，FSDP default。precision、serving latency、concurrency 与 SLO 未披露。
- **Evaluation Contract:** 多个 video QA/description datasets；部分 generation evaluation 使用 GPT-3.5-turbo-0613。作者明确指出
  既有 TGIF 报告存在不可比设置，故不把跨论文 leaderboard 当统一证据。
- **Baselines / Ablations / Sensitivity:** encoder removal、2D pooling alternatives、32/64/... visual tokens、cross-attention vs
  concatenation、frozen vs full。MERV-full 并非所有任务更好，64 tokens 只是作者设置内的峰值。
- **What the Evidence Proves / Does Not Prove:** 证明专业 encoder 的互补 representation 在作者任务内可经压缩/fusion 获益；
  不证明 encoder 越多越好，也不证明并行执行消除算力、显存、同步或 online latency 成本。
- **Limitations / Trade-offs / New Failure Modes:** 多 encoder 增加 memory、OOM、data preprocessing、license/version 与 placement
  复杂度；同步 barrier 由最慢 expert 决定，alignment 可能抹平专业特征，LLM/fusion 可把某 expert 静默忽略。
- **Where the Previous Design Still Applies:** 单一 modality/task、edge/latency-sensitive 或已有强 native multimodal encoder 时，
  单 encoder 更可控；expert 收益不足以覆盖 deployment tax 时不应堆叠。
- **Evolution Relationship:** `Alternative Branch`（single general encoder ↔ multiple specialized encoders）；`Layering / Dependency`
  （expert representation → token alignment → fusion → LLM）。
- **ROADMAP Node:** Owner `MULTIMODAL-REPRESENTATION`，Current Ch23；handoff `TRAIN-DISTRIBUTED-TRAINING`，
  Current Ch40，以及 `INFER-EXECUTION`，Current Ch49。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只定位跨层责任，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** expert selection/gating、heterogeneous placement、slow-expert fallback、schema versioning 与 end-to-end latency。

### SeedVR: Real-world Restoration Couples Receptive Field, Causal Compression and Workload Scale

- **Candidate / Week / Score:** SeedVR / 2025-W01 / 24/30。
- **Source Family ID:** `seedvr-real-world-video-restoration`。
- **Source Type:** 作者论文与 project artifact；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 于 2025-01-02；本周按 v1 归档。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01320；https://arxiv.org/html/2501.01320。
- **Access and Verification Status:** Verified；architecture、training data contract、implementation、evaluation、ablation 与
  limitations 可访问。
- **Full-read Coverage:** metadata、unknown-degradation problem、Swin-MMDiT、shifted 3D window attention、3D RoPE、causal
  video VAE、progressive/mixed training、datasets、metrics、window/VAE ablations、compute disclosure、limitations。
- **Original Problem:** real-world restoration 的 degradation 不可枚举；传统 regression 倾向平滑，full-attention diffusion 又随
  resolution×frames 快速增长，固定 shape 难支持不同长度与边界窗口。
- **Why the Previous Design Was Reasonable:** supervised restoration 对已知 degradation 可给稳定 fidelity；global attention 在较小
  video 上保留完整 interaction；非 causal VAE 适合离线整段编码。
- **Changed Constraint:** 720p、长视频、图像/视频混训与未知 degradation 同时要求较大 receptive field、可扩展 attention 和
  更强 temporal compression。
- **Mechanism:** Swin-MMDiT 交替 regular/shifted 3D large windows，以 3D RoPE 处理可变边界；causal video VAE 由 causal
  3D residual blocks 组成，空间压缩 8、时间压缩 4、latent channels 16；混合 image/video 的 native variable resolution，
  progressive training 学习 restoration prior。
- **State Ownership / Control and Data Flow:** degradation condition、noisy latent、window partition/shift、causal VAE temporal
  state 共同决定输出；window boundary 与 chunk identity 必须一致。论文没有定义 streaming cache、cross-chunk continuity、
  online backpressure 或 partial retry semantics。
- **Implementation Details:** 2.48B model，初始化自 SD3-Medium；256×H100-80G、每 GPU 约 150 个 720p frames、约 30K
  H100-hours。CVVAE 使用 32×H100、batch 5/GPU、115K iterations、17×256×256 clips。precision 未披露。
- **Evaluation Contract:** synthetic、real-world 与 AIGC video，统一到 720p；PSNR/SSIM/LPIPS/DISTS 与 NIQE/CLIP-IQA/
  MUSIQ/DOVER。window ablation 在 16×A100-80G、12.5K iterations；未披露 serving latency、concurrency 与 SLO。
- **Baselines / Ablations / Sensitivity:** restoration/generative baselines、VAE variants、regular/shifted and window-size settings。
  SeedVR 并非所有 distortion metrics 第一，强项更偏 perceptual/no-reference quality，不能写成统一 fidelity 胜出。
- **What the Evidence Proves / Does Not Prove:** 证明作者数据和 720p contract 下 large shifted 3D windows 与 causal VAE 可在
  质量/规模间形成可行点；不证明任意真实 degradation、streaming video、低延迟硬件或独立数据上通用。
- **Limitations / Trade-offs / New Failure Modes:** 内部约 1 亿 images/500 万 videos 不可复核；large window 增 compute，small
  window 因重复 text tokens 反而可能更慢；causal compression、chunk/window boundary 会引入 temporal seam，diffusion sampling
  仍昂贵。作者明确把 sampling efficiency 与 robustness 留作未来工作。
- **Where the Previous Design Still Applies:** degradation 已知、严格 PSNR、低延迟或 edge workload 仍适合专用 regression model；
  短小离线 video 可用 global attention，不能把 training-scale 设计直接外推 serving。
- **Evolution Relationship:** `Direct Evolution`（fixed-degradation regression → generative restoration；global attention → shifted
  3D windows）；`Layering / Dependency`（causal VAE → latent denoiser）。
- **ROADMAP Node:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Current Ch24；handoff `TRAIN-DATA`，Current Ch27，
  以及 `INFER-EXECUTION`，Current Ch49。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只完成 owner/handoff，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** external-data replication、sampling latency、window/chunk continuity、precision contract 与 edge deployment。

### WeAudit: From Expert-only Tests to Structured, User-engaged Audit Evidence

- **Candidate / Week / Score:** WeAudit / 2025-W01 / 23/30。
- **Source Family ID:** `weaudit-user-engaged-audit-workflow`。
- **Source Type:** arXiv/ACM HCI paper、Microsoft Research publication page 与 prototype description；Status: Experimental。
- **Event Date / First-public Date / Revision History:** arXiv v1 2025-01-02、v2 2025-01-03、v3 2025-01-09、v4
  2025-04-29；W01 按 v1 归档，v4 只补充最终 publication/limitations，不改写事件日期。
- **Direct Primary Sources:** https://arxiv.org/abs/2501.01397；https://arxiv.org/html/2501.01397；
  https://www.microsoft.com/en-us/research/publication/weaudit-scaffolding-user-auditors-and-ai-practitioners-in-auditing-generative-ai/。
- **Access and Verification Status:** Verified；全文、formative study、workflow、implementation、user study、results、limitations
  与 discussion 可访问。
- **Full-read Coverage:** metadata/revisions、Related Work、11-user/7-practitioner formative study、six design goals、Investigate/
  Deliberate loops、Explore/Inspect/Reflect/Report/Discuss/Verify activities、prototype implementation、45-user study、84 verifiers、
  10 practitioner interviews、qualitative/quantitative observations、four-month follow-up、limitations 与 power/compensation discussion。
- **Original Problem:** expert audit、static benchmark 与 generic crowdsourcing 会漏掉受影响用户的 lived experience；但开放式
  用户反馈又缺少 hypothesis、evidence、taxonomy、verification 和向工程团队传递 actionable report 的结构。
- **Why the Previous Design Was Reasonable:** 专家评测和固定 rubric 便于复现、聚合与 release Gate；majority vote 对有 ground
  truth 的 labeling 成本低。它们不适合把少数、上下文相关且尚无 ground truth 的 harm 当普通 label。
- **Changed Constraint:** generative model 的 input/output space 与 sociotechnical harm space 都很大，用户既是 evidence source，
  也是可能承担不可见劳动和伤害暴露的 stakeholder；系统必须保存分歧而非只压成平均分。
- **Mechanism:** workflow 由 Investigate 与 Deliberate 两个交叉迭代 loop 组成，细分 Explore、Inspect、Reflect、Report、
  Discuss、Verify。pairwise comparison 支持 hypothesis testing；prompt history、worked examples 与 underexplored-topic social
  augmentation 扩大探索；structured report 分离 observation、harm/to whom、envisioned fix 与 auditor context；verification 保存
  clarity、harmfulness、relevance、reasonableness 及 disagreement rationale。
- **State Ownership / Control and Data Flow:** model outputs/prompt history 是 observation evidence；auditor identity/context、report、
  tags、discussion 与 verification 是不同 provenance state。用户提出 claim，其他用户补充/反驳，practitioner 决定 triage；
  论文没有组织级 issue lifecycle、access control、retention/delete 或 remediation closure contract。
- **Implementation Details:** HTML/CSS/JavaScript + Django；Stable Diffusion 2.0 经 Replicate API；images 写 S3/DynamoDB，behavior
  logs 写 Lightsail SQLite，Lambda 承担 backend computation，Discourse 提供讨论。它是研究 prototype，不是 production blueprint。
- **Evaluation Contract:** formative study 11 users + 7 practitioners；main study 45 名美国大学学生，40-minute audit 与三周可选使用；
  84 Prolific workers 验证报告；10 industry practitioners 访谈；37 人获邀、17 人完成四个月 follow-up。没有 randomized control、
  production defect-removal rate、cross-model comparison 或 release SLO。
- **Baselines / Ablations / Sensitivity:** 研究以 formative prototype、usage logs、survey、discussion 与 interviews 做 triangulation，
  不是组件级 controlled ablation。worked examples viewed 与 report rate 的 `r=0.769` 是观察相关，不证明 causal effect；examples
  同时可能造成 anchoring/echo chamber。
- **What the Evidence Proves / Does Not Prove:** 证明一个可操作的 user-engaged audit state machine 能把开放探索、结构化报告、
  讨论和验证连接起来，并在该小规模 T2I study 中产生 practitioners 认为有用的 evidence；不证明系统降低真实 harm、可大规模
  运营、跨文化公平，或 majority verification 能定义主观 harm 的 ground truth。
- **Limitations / Trade-offs / New Failure Modes:** 用户样本以美国大学生为主，practitioners 多来自美国大公司，且访谈基于非本
  产品 context；scaffolding 会 priming，social signals 会 popularity bias，verification 会压低 minority/outlier evidence；新增
  harmful-content exposure、privacy、moderation、compensation、retention、abuse 与 organization power asymmetry。
- **Where the Previous Design Still Applies:** correctness/security regression、明确 policy rule 与可执行 oracle 仍应使用 expert/
  automated tests；user audit 是互补 evidence plane，不应替代 model card、red team、incident response 或 formal release Gate。
- **Evolution Relationship:** `Direct Evolution`（expert-only/static audit → structured participatory evidence workflow）；
  `Layering / Dependency`（observation → report → discussion/verification → practitioner triage）；与 crowdsourcing 为 `Principle Reuse`。
- **ROADMAP Node:** Owner `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62；handoff `PLATFORM-SECURITY`，
  Current Ch72，Legacy Ch68。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只完成 owner/handoff，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** minority evidence preservation、auditor safety/compensation、provenance/delete、anti-gaming、remediation closure 与
  production release Gate integration。

### CVPR 2025 Photorealistic Avatar Challenge: Benchmark Results Require a Workload Contract First

- **Candidate / Week / Score:** Microsoft Research CVPR 2025 Photorealistic Avatar Challenge / 2025-W01 / 20/30。
- **Source Family ID:** `cvpr25-photorealistic-avatar-evaluation-contract`。
- **Source Type:** 官方 challenge overview、rules、timeline 与 test protocol；Status: Official Program Fact。
- **Event Date / First-public Date / Revision History:** Microsoft Research announcement 2025-01-03；program 从 2025-01-15 开始，
  后续 rules/timeline 属于同一 Source Family，不反写为 W01 model result。
- **Direct Primary Sources:** https://www.microsoft.com/en-us/research/academic-program/photorealistic-avatar-challenge-cvpr-2025/challenge/；
  https://www.microsoft.com/en-us/research/academic-program/photorealistic-avatar-challenge-cvpr-2025/rules/；
  https://www.microsoft.com/en-us/research/academic-program/photorealistic-avatar-challenge-cvpr-2025/timeline/。
- **Access and Verification Status:** Verified；official task、tracks、input/output、hardware/latency、causality、blind set、metric 与
  judging protocol 可访问；本周没有 competition result。
- **Full-read Coverage:** challenge motivation、three tracks、enrollment/test clips、viewpoints、subjective dimensions、sample sizes、
  1080p/30FPS、RTX 4090、causal restriction、blind-set rules、submission and reporting requirements、timeline。
- **Original Problem:** PSNR/SSIM/LPIPS 等 distortion metrics 与 avatar realism/affinity 的 human perception 可能不一致；跨论文
  test set、viewpoint、causality 与 latency contract 不同，leaderboard 数字不可直接比较。
- **Why the Previous Design Was Reasonable:** automatic metrics 成本低、可重复、适合训练回路；离线 non-causal model 能利用未来帧
  获得更好画质，若 workload 本来不要求实时交互则完全合理。
- **Changed Constraint:** telepresence/avatar workload 要同时满足 identity、emotion、gesture、causality 与 real-time interaction，
  evaluation 必须先固定 enrollment、blind test、hardware 和 end-to-end frame deadline。
- **Mechanism:** 三个 track 分离 half-body real-time、half-body non-real-time 与 head-only non-real-time；real-time contract 为
  1080p 30FPS、RTX 4090 或同等 GPU、capture+encode+decode <33ms，所有 tracks 禁止使用 future frames。blind set 与 enrollment
  分离，主指标是 realism、resemblance、emotion accuracy、gesture accuracy 的 subjective mean，每 clip 至少 30 ratings。
- **State Ownership / Control and Data Flow:** enrollment clip 定义 avatar identity，test clip 驱动 causal rendering，organizer
  持有 blind set/ratings，participant 生成 output 并报告 parameters 与 frame time。规则没有规定跨 implementation 的计时 harness、
  power、precision 或 measurement variance，因此仍需复现审计。
- **Evaluation Contract:** 10 subjects、不同 enrollment/test days、speech/emotion/head-turn/gesture clips、0°/45° views、4K input 与
  1080p MP4 output；real-time track 绑定 4090-equivalent 和 33ms。最终 ranking 依赖 subjective MOS，不是论文模型结果。
- **What the Evidence Proves / Does Not Prove:** 证明 benchmark 设计可把 causality、hardware、deadline 与 subjective quality 写进
  同一 workload contract；不证明任何方法更优，也不证明 10 subjects/30 ratings 覆盖现实 population 或 production networking。
- **Limitations / Trade-offs / New Failure Modes:** subjective rating 昂贵且有 rater/culture variance；blind set 小，hardware
  equivalence 与计时边界仍可能不一致；严格 causal/33ms 会牺牲画质，non-real-time track 则不能支持交互 SLO。
- **Where the Previous Design Still Applies:** training regression 继续需要 PSNR/SSIM/LPIPS；影视离线生成可使用 future frames；
  只有实时 telepresence 才需要严格 causal end-to-end deadline。
- **Evolution Relationship:** `Direct Evolution`（unbound image metrics → workload-bound causal/perceptual evaluation）；与 model
  architecture 无替代关系。
- **ROADMAP Node:** Owner `PLATFORM-EVALUATION-SYSTEM`，Current Ch66，Legacy Ch62；handoff
  `MULTIMODAL-EMBODIED-VLA`，Current Ch26（real-time perception/action contract analogy only）。
- **Target and Adjacent Chapters Read:** Weekly-only phase；只完成 evidence owner 定位，不打开 Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Open Questions:** standardized timing harness、rater calibration、network latency、power/precision disclosure 与 population coverage。

### EnerVerse: Chunk-wise Video World Model, Sparse Memory and Policy Coupling

- **Candidate / Week / Score:** EnerVerse / 2025-W01 / 26/30；Source Family ID `enerverse-video-world-model`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-03、v2 2025-02-10、v3 2025-11-16；https://arxiv.org/abs/2501.01895；https://arxiv.org/html/2501.01895。已阅读全文、方法、训练数据、仿真/真实实验、ablation 与 limitations；当前 HTML 的 v3 增补与 event-time v1 严格分开。
- **Problem → Changed Constraint → Mechanism:** 单步 action policy 难以显式预测动作后世界状态，整段 video diffusion 又缺少长程 memory 与可终止控制。EnerVerse 将未来按 chunk 自回归生成，以随机抽样历史帧形成 sparse memory，并用 EOS threshold 决定停止；multi-view 分支加入 ray map、view/spatial/temporal attention，policy head 复用第一步 denoising latent 预测 action chunk。状态由 video generator、memory sampler、EOS controller 与 action head 分层拥有，而不是把“生成视频”直接等同于 world understanding。
- **Implementation / Evaluation Contract:** 数据联合 RT-1、Taco-Play、ManiSkill、BridgeV1、LanguageTable、RoboTurk 与 Isaac Sim multiview；200 段 synthetic video 评 PSNR/FVD/user study；LIBERO 每 suite 独立模型、每 task 50 demonstrations、50 rollouts、3 seeds，并评 CALVIN 与真实机器人。v3 报告 RTX 4090 上 8-step action chunk 约 280ms，属于后续 revision；precision、batch、并发与完整 SLO 未披露。
- **Evidence Boundary / Trade-offs:** 证据支持“action-conditioned visual rollout + sparse history + policy latent reuse”在作者任务可行，不证明 video quality 与 control success 单调相关，也不证明生成器学到因果环境。新增 memory cross-task mismatch、EOS 误停、相机校准、多视角生成误差、sim-to-real 与 data-flywheel 自我强化风险。短视界、强 proprioception 或严格控制稳定性下，直接 policy / state estimator 仍更合理。
- **Evolution / Owner / Decision:** `Direct Evolution`（next observation → chunked action-conditioned transition）与 `Layering / Dependency`（visual rollout → policy proposal → environment feedback）。Owner `MULTIMODAL-WORLD-MODELS` Ch25；handoff `MULTIMODAL-EMBODIED-VLA` Ch26。`Books Pending — Integration Deferred`。Open: v1/v3 差异、真实控制频率、memory identity/reset、校准与安全 envelope。

### Scaling Laws for Floating-Point Quantization Training: Precision Is a Coupled Scaling Variable

- **Candidate / Week / Score:** Scaling Laws for Floating Point Quantization Training / 2025-W01 / 25/30；Source Family ID `fp-quant-training-scaling-law`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-05、v2 2025-05-13、v3 2025-06-04；https://arxiv.org/abs/2501.02423；https://arxiv.org/html/2501.02423。已读取 v1 metadata、方法、拟合公式、366 次训练、validation、ablation 与限制；后续 revision 不倒灌。
- **Problem → Changed Constraint → Mechanism:** 经典 scaling law 把参数量与数据量视为主要变量，却无法回答训练 GEMM 的 exponent、mantissa、block size 与量化 target 如何随模型/数据规模改变误差。论文把不可约损失、model/data scaling 和 quantization penalty 联合拟合，并分别扫描 P2/P4/P6、指数位、尾数位、scaling block 与六类量化输入，从而把 precision 从“固定实现细节”提升为 workload contract 的一部分。
- **Implementation / Evaluation Contract:** 366 个 41M～679M Transformer 用于拟合，1.2B 用于验证；作者公式显式耦合 `N、D、E、M、B`。结论只覆盖所用经典 Transformer、训练 GEMM 与作者量化器；hardware、训练 wall time、optimizer kernel、并发和 SLO 未披露。
- **Evidence Boundary / Trade-offs:** 证据支持低精度最优点依赖 scale、格式与量化对象，不支持把作者 4～8 bit 区间外推成所有架构/硬件的普遍最优。更低 precision 节省带宽/算力，却提高 scale metadata、overflow、rounding bias、optimizer-state 与 error attribution 复杂度。模型较小、数值敏感或硬件缺少原生格式时，BF16/FP16 仍可能更可靠。
- **Evolution / Owner / Decision:** `Direct Evolution`（parameter/data scaling → parameter/data/precision joint scaling）与 `Layering / Dependency`（law → training policy → kernel/hardware realization）。Owner `WORLDVIEW-SCALING-LAW` Ch7；handoff `TRAIN-PRETRAINING` Ch28、`INFER-TENSORRT-LLM` Ch49。`Books Pending — Integration Deferred`。Open: 非 Transformer、optimizer state、真实 energy/cost、hardware-native format 与 v1/v3 拟合差异。

### VisionReward: Decomposed Policy Dimensions Before Preference Optimization

- **Candidate / Week / Score:** VisionReward / 2025-W01 / 24/30；Source Family ID `visionreward-decomposed-multimodal-preference`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2024-12-30，后续 v2/v3/v4；https://arxiv.org/abs/2412.21059；https://arxiv.org/html/2412.21059。已读 taxonomy、annotation、reward model、MPO、MonetBench、训练设置、ablation 与边界；只把 v1 作为 W01 事件。
- **Problem → Changed Constraint → Mechanism:** 单一 scalar aesthetic/relevance reward 把多个政策维度压扁，偏好优化可能通过改善一维而伤害另一维。论文将图像/视频质量分成 9 个 dimensions、约 18～20 个 subdimensions 和 61～64 个 binary questions，用 CogVLM2 逐问评分，再以显式 logistic weights 合成；MPO 只选择在所有维度均 Pareto dominate 的 pair 进入 diffusion DPO。
- **Implementation / Evaluation Contract:** 数据约 81K samples、5M annotations，作者报告 annotator consistency 约 89.3%；图像训练 pair 约 44K，视频 1,795。CogVideoX-2B 示例由 22K prompts 每个生成 4 个候选，约 9,400 pairs，batch 32、lr 5e-6、beta 500、500 steps。硬件、并发和生产 SLO 未充分披露。
- **Evidence Boundary / Trade-offs:** 证据支持“先显式分解政策维度，再构造保守偏好 pair”能在作者 benchmark 改善受测指标；不证明 taxonomy 完整、weight 可跨文化复用或 reward 不会被 gaming。Pareto 条件降低冲突，却稀疏化可用 pair；binary QA 提高可审计性，却引入 question wording、annotator/model bias 与线性聚合假设。稳定单目标任务仍可使用 calibrated scalar reward。
- **Evolution / Owner / Decision:** `Direct Evolution`（monolithic reward → decomposed evidence → Pareto-safe preference）与 `Alternative Branch`（hard Pareto filtering ↔ learned multi-objective trade-off）。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `TRAIN-DPO` Ch34。`Books Pending — Integration Deferred`。Open: taxonomy governance、weight calibration、pair coverage、independent human audit 与 reward hacking。

### BoxingGym: Scientific Agent Evaluation Must Include Experiment Choice

- **Candidate / Week / Score:** BoxingGym / 2025-W01 / 24/30；Source Family ID `boxinggym-active-scientific-experiment`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-02、v2 2025-10-14；https://arxiv.org/abs/2501.01540；https://arxiv.org/html/2501.01540。已读 environments、agent loop、metrics、baselines、实验与 limitations；later-model rows 只属于后续 revision。
- **Problem → Changed Constraint → Mechanism:** 静态 QA 只测“给定证据后能否回答”，不测科学 Agent 是否会选择高信息量实验。BoxingGym 提供 10 个可执行 generative environments，让 Agent 以自然语言提出 experiment、读取 observation，并同时测 expected information gain、model discovery/explanation 与 goal prediction。Box's Apprentice 还在 10 次实验后写 PyMC model，以 symbolic posterior 指导后续选择。
- **Implementation / Evaluation Contract:** 每个 environment 运行 5 个 independent trials，在 0/1/3/5/7/10 次实验 checkpoint 评估并跨 run/environment 聚合；比较 GPT-4o 与 symbolic-model scaffold。模拟器、prompt、budget 与 evaluator 是能力合同的一部分，不能把结果归因给基础模型本身。
- **Evidence Boundary / Trade-offs:** 论文证明在预定义仿真范式里，实验选择和模型表达可以被联合、可执行地测量；不证明 Agent 能发现未知实验范式、处理真实仪器资源、安全或数据污染。显式 Bayesian model 增加 sample efficiency 与可解释性，也增加 model misspecification、code execution、posterior calibration 和 tool failure。任务简单或观测固定时，静态 benchmark 仍更便宜且可复现。
- **Evolution / Owner / Decision:** `Direct Evolution`（answering from observations → choosing observations）与 `Layering / Dependency`（experiment proposal → simulator → evidence → model update）。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `AGENT-WORKFLOW` Ch81。`Books Pending — Integration Deferred`。Open: v1 benchmark snapshot、resource-aware experiments、unsafe action constraints 与 real-lab validity。

### VITA-1.5: Native Multimodality Requires Separate Token and Timing Contracts

- **Candidate / Week / Score:** VITA-1.5 / 2025-W01 / 24/30；Source Family ID `vita-1-5-native-multimodal-io`；作者技术论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-03，v2 2025-01-16、v3 2025-01-21、v4 2025-10-24；https://arxiv.org/abs/2501.01957；https://arxiv.org/html/2501.01957。已读 architecture、三阶段训练、数据表、视觉/语音评测与 limitations。
- **Problem → Changed Constraint → Mechanism:** 把外部 ASR/TTS 接到文本 LLM 虽模块化，却丢失声学细节并引入多段延迟；直接混合图像、音频和文本又会产生 token rate 与 modality conflict。VITA-1.5 用 InternViT + adapter 表示视觉，以约 350M audio encoder 产生 12.5Hz 输入表示，并用 TiCodec 单一 1,024 codebook、40Hz speech token 与 speech decoder 端到端输出语音；三阶段分别建立 vision-language、audio-input 与 audio-output coupling。
- **Implementation / Evaluation Contract:** 视觉输入 448px、每图 256 tokens，并做 video frame sampling；vision corpus 表中约 22.1M QA/caption，audio-input 约 11K hours、audio-output 约 3K hours。评测覆盖视觉理解和 speech I/O，但 hardware、实时延迟、并发、precision、长对话 timing 与 SLO 未完整披露。
- **Evidence Boundary / Trade-offs:** 证据支持不同 modality 需要各自 encoder/tokenizer/rate，并可在共享 LLM 中联合；不证明 native pipeline 必然优于 modular ASR+LLM+TTS，也不公开端到端 serving state。native coupling 保留语音/视觉上下文，却增加数据对齐、token competition、codec artifact、modality interference、interrupt/turn-taking 与版本联动。需要独立升级、强可审计文本或低资源部署时，模块化 pipeline 仍成立。
- **Evolution / Owner / Decision:** `Direct Evolution`（text bottleneck → native modality tokens）与 `Alternative Branch`（end-to-end speech ↔ modular speech services）。Owner `MULTIMODAL-REPRESENTATION` Ch23；handoff `INFER-SCHEDULING` Ch56。`Books Pending — Integration Deferred`。Open: event-time config、real-time SLO、modality identity、barge-in 与 long-session state。

### AutoPresent: Artifact-Producing Agents Need Execution and Render Feedback

- **Candidate / Week / Score:** AutoPresent / 2025-W01 / 23/30；Source Family ID `autopresent-executable-slide-agent`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-01、v2 2025-06-19；https://arxiv.org/abs/2501.00912；https://arxiv.org/html/2501.00912。已读 SlidesBench、SlidesLib、generation/refinement flow、evaluators、training 与 limitations。
- **Problem → Changed Constraint → Mechanism:** 只生成 slide 文本无法保证 artifact 可打开、布局正确或视觉可读。AutoPresent 将自然语言翻译为调用 SlidesLib 的 Python/PPTX program，执行后渲染 screenshot；refinement 接收原 instruction、previous code 和 rendered image，再整体改写。状态包括 source instruction、program、execution result、rendered artifact 与 evaluation，而不是把最终文件视作不可解释 blob。
- **Implementation / Evaluation Contract:** SlidesBench 约 7K train/585 test、10 domains、3 种 instruction granularity；模型一次生成 3 个 samples，选第一个 executable。8B 模型 LoRA rank 128、alpha 32、batch 1、gradient accumulation 2、FP16、1 epoch、lr 3e-4。reference-based evaluator 比较 element/content/color/position；reference-free GPT-4o 评 text/image/layout/color，与两位 human 的 ICC 约 73.8～85.3；non-executable artifact 总分为 0。
- **Evidence Boundary / Trade-offs:** 证据支持 code execution + render feedback 比纯文本判断更接近 artifact correctness；不证明单页结果能外推到多页叙事、协作编辑或真实 brand constraints。代码表示提高可重放性，却引入 sandbox、dependency/version、font/layout nondeterminism、整页改写回归与 model-judge bias。简单模板填充仍可用 deterministic renderer。
- **Evolution / Owner / Decision:** `Direct Evolution`（text answer → executable artifact → rendered feedback）与 `Layering / Dependency`（proposal → execution → visual evidence → revision）。Owner `AGENT-WORKFLOW` Ch81；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: deck-level state、incremental patch、sandbox、human edit provenance 与 evaluator calibration。

### ToolHop: Tool Ability Is a Harness-Level Execution Contract

- **Candidate / Week / Score:** ToolHop / 2025-W01 / 23/30；Source Family ID `toolhop-multitool-executable-evaluation`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-05、v2 2025-01-07、v3/v4 2025-05；https://arxiv.org/abs/2501.02506；https://arxiv.org/html/2501.02506。已读 v1 construction、tool runtime、evaluation modes、models、error analysis 与 limitation。
- **Problem → Changed Constraint → Mechanism:** 单工具 benchmark 容易退化为 schema matching，不能区分工具选择、参数传递、跨工具依赖与最终答案错误。ToolHop 从 query 做 atomic decomposition，再生成和编译本地工具、迭代修正文档/代码，形成 995 queries、3,912 executable tools 与预定义可验证答案；评测 direct、mandatory-tool 与 free-choice 三种模式，并分别记录 answer correctness 与 invocation error。
- **Implementation / Evaluation Contract:** 论文覆盖 14 个 LLM、5 个 model families；工具在本地 deterministic environment 执行。hardware、batch、concurrency、真实 network/auth latency 与 production SLO 未披露；因此只能比较作者 harness 内的相对行为。
- **Evidence Boundary / Trade-offs:** 证据支持“tool-use capability = model + schema + orchestrator + runtime + evaluator”，并暴露调用错误；不证明训练提升、真实 API 可靠性或有副作用工具的安全。自动生成工具扩大覆盖，却可能把答案假设编码进工具；本地执行提高复现性，却省略 auth、rate limit、freshness、idempotency 和 rollback。目标固定且工具少时，静态 function-calling test 仍合理。
- **Evolution / Owner / Decision:** `Direct Evolution`（single-call schema → multi-hop executable tool graph）与 `Layering / Dependency`（selection → invocation → execution → verification）。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `AGENT-TOOL-CALLING` Ch78。`Books Pending — Integration Deferred`。Open: artifact snapshot、side-effect sandbox、equal-budget comparison、tool-doc leakage 与 evaluator false positive。

### Personalized Graph-Based Retrieval: Retrieval Locality Creates Identity and Freshness State

- **Candidate / Week / Score:** Personalized Graph-Based Retrieval / 2025-W01 / 22/30；Source Family ID `personalized-graph-rag-local-profile`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-04、v2 2025-05-31；https://arxiv.org/abs/2501.02157；https://arxiv.org/html/2501.02157。已读 v1 graph construction、retrieval、12 tasks、baselines、ablation 与 v2 limitations；后续 limitations 只用于说明证据边界。
- **Problem → Changed Constraint → Mechanism:** 只检索目标用户历史在交互稀疏时证据不足，使用全局语料又会冲淡个性。论文把 user-item interactions 建成 bipartite graph，以目标用户历史加共享 item 的邻居历史构成 local profile，再用 BM25 或 Contriever 取 top-5 片段进入 prompt。graph owner、profile builder、retriever 和 generator 分别拥有关系、候选范围、排序与回答。
- **Implementation / Evaluation Contract:** 12 个 generation/rating tasks；比较 No Retrieval、Random、LaMP；Llama-3.1-8B 与 GPT-4o-mini，local A100 80GB、最多 512 output tokens、GPT temperature 0.4；指标 ROUGE/METEOR/MAE/RMSE。未测试在线 graph update、delete、privacy、concurrency 或 latency SLO。
- **Evidence Boundary / Trade-offs:** 证据支持 graph-local neighbor evidence 在作者数据上可改善部分 personalization tasks，但 rating tasks 不一致，neighbor-only 有时胜过完整 profile；不证明图结构天然优于所有 retrieval。邻居扩大 evidence，却引入 identity leakage、popularity bias、stale edge、consent/delete 与 profile contamination。用户历史足够密集或隐私隔离严格时，target-only retrieval 仍更合适。
- **Evolution / Owner / Decision:** `Direct Evolution`（user-only history → graph-local evidence）与 `Alternative Branch`（graph locality ↔ semantic/global retrieval）。Owner `AGENT-RAG` Ch76；handoff `AGENT-MEMORY` Ch77、`PLATFORM-SECURITY` Ch72。`Books Pending — Integration Deferred`。Open: online freshness、edge provenance、deletion propagation、privacy budget 与 retrieval latency。

### Virgo: Textual Long-Thought Transfer Is Not the Same as Better Perception

- **Candidate / Week / Score:** Virgo / 2025-W01 / 22/30；Source Family ID `virgo-multimodal-long-thought-sft`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-03、v2 2025-02-05；https://arxiv.org/abs/2501.01904；https://arxiv.org/html/2501.01904。已读 training recipe、data variants、MathVerse/MathVision/OlympiadBench/MMMU、length sensitivity 与 error analysis。
- **Problem → Changed Constraint → Mechanism:** 多模态模型有视觉输入但缺少长链数学 reasoning data；直接增加 visual CoT 成本高。Virgo 冻结 Qwen2-VL-72B visual encoder，训练 connector 与 LLM，先用 textual long-thought data 建立 reasoning behavior，再比较 QVQ visual distillation/self-distillation。它改变的是 reasoning policy，不是视觉 encoder 的感知能力。
- **Implementation / Evaluation Contract:** lr 7e-6、batch 128、10 epochs 并选第 5 epoch；没有 DPO/RLHF。评测四类多模态数学 benchmark；reasoning length 从约 2K 增至 4K 有益，8K 反而下降，作者归因于 math-dominated data。hardware、precision、compute、并发与服务 SLO 未披露。
- **Evidence Boundary / Trade-offs:** 证据支持 textual long-thought 能迁移部分 reasoning pattern，且更难任务受益更明显；不证明感知错误被修复，论文案例反而显示早期 perception error 会让长推理继续放大错误。更长输出增加训练/推理成本、verbosity 与错误累积。视觉证据简单或 latency 紧张时，短 reasoning 或显式 perception verifier 更合理。
- **Evolution / Owner / Decision:** `Principle Reuse`（text reasoning supervision → multimodal reasoning）而非视觉机制替代。Owner `TRAIN-SFT` Ch29；handoff `MULTIMODAL-REPRESENTATION` Ch23、`PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: data composition、perception verifier、length calibration、event-time checkpoint 与 independent replication。

### Segment-Level DPO: Preference Granularity Must Match Error Locality

- **Candidate / Week / Score:** Segment-Level Direct Preference Optimization / 2025-W01 / 22/30；Source Family ID `sdpo-social-agent-segments`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-03、v2 2025-02-27；https://arxiv.org/abs/2501.01821；https://arxiv.org/html/2501.01821。已读 SOTOPIA data construction、segment objective、training、ablation 与限制。
- **Problem → Changed Constraint → Mechanism:** whole-dialogue preference 把少量 social error 与大量正常 turns 一起归责，token/trajectory credit assignment 过粗。论文先用 GPT-4-turbo expert 行为做 BC；对 goal score <7 的 negative session，由 GPT-4o 定位错误 turn，再从 positive sessions 选取同长度 segment 配对。equal-length 条件消去 partition term，使 DPO 聚焦局部行为差异。
- **Implementation / Evaluation Contract:** Llama-3.1-8B、max length 4096；SFT batch 32、lr 1e-5、dropout 0.2；SDPO batch 32、beta 0.1、lr 1e-6。segment length 3 优于 5，动态 GPT-4o 定位优于固定窗口；不对称长度训练崩溃。hardware、precision、rollout cost 与生产并发未披露。
- **Evidence Boundary / Trade-offs:** 证据支持 preference unit 与 error locality 对齐可改善作者 social benchmark；不证明 GPT-4o 定位正确，也不证明社会目标分数是客观 reward。局部 segment 降低无关梯度，却可能漏掉长程因果、把正确 turn 错标或忽视 interaction partner。错误跨多轮、reward 可执行或长度不对称时，trajectory-level / verifier-based 方法仍成立。
- **Evolution / Owner / Decision:** `Direct Evolution`（whole trajectory preference → localized segment preference）与 `Alternative Branch`（model-located segment ↔ executable/human-labeled credit）。Owner `TRAIN-DPO` Ch34；handoff `AGENT-MULTI-AGENT` Ch82。`Books Pending — Integration Deferred`。Open: locator calibration、unequal-length objective、long-horizon causality、rater bias 与 reward provenance。

### LUSIFER: Cross-Lingual Embedding Can Be a Staged Interface Alignment Problem

- **Candidate / Week / Score:** LUSIFER / 2025-W01 / 22/30；Source Family ID `lusifer-multilingual-embedding-alignment`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-01、v2 2025-05-05、v3 2025-05-07；https://arxiv.org/abs/2501.00874；https://arxiv.org/html/2501.00874。已读 architecture、two-stage training、benchmark、ablations 与 per-task limitations。
- **Problem → Changed Constraint → Mechanism:** English-centric embedding LLM 的 task behavior 强，但语言覆盖受限；从头多语训练昂贵。LUSIFER 将 multilingual encoder 经最小 FF connector 接到 target embedding LLM：stage 1 冻结 target LLM，以 English masked reconstruction + autoregressive completion 对齐接口；stage 2 再联合做 embedding-specific fine-tuning。它复用 multilingual encoder 的 latent language coverage，而非假设 English data 自行产生多语能力。
- **Implementation / Evaluation Contract:** 5 类任务、123 datasets、14 languages，并有超过 100 languages 的 cross-lingual evaluation；ablation 比较 connector-only、frozen、alignment-only 与 finetune-only。完整两阶段整体最好，但 reranking 和若干语言/任务有回退；hardware、precision、training compute 与 serving SLO 未披露。
- **Evidence Boundary / Trade-offs:** 证据支持“能力模型 + 语言接口”可通过 staged alignment 组合；不证明 English-only alignment 对所有语言无损或 connector 是普遍最优。复用 encoder 降低训练成本，却增加两套 representation 的版本耦合、alignment drift、tokenization mismatch 与低资源语言隐藏退化。单语高精度或统一端到端训练资源充足时，专用 embedding model 仍合理。
- **Evolution / Owner / Decision:** `Layering / Dependency`（multilingual representation → connector alignment → embedding objective）与 `Alternative Branch`（compose specialists ↔ end-to-end multilingual model）。Owner `MODEL-EMBEDDING` Ch12；handoff `AGENT-RAG` Ch76。`Books Pending — Integration Deferred`。Open: per-language calibration、negative transfer、connector versioning、hardware cost 与 retrieval end-to-end effect。

### Auto-RT: Automated Red Teaming Adds a Search Controller, Not Ground Truth

- **Candidate / Week / Score:** Auto-RT / 2025-W01 / 22/30；Source Family ID `auto-rt-rl-red-team-strategy-search`；作者论文，Status: Experimental / Security Research。
- **Event / Sources / Access:** arXiv v1 2025-01-03；https://arxiv.org/abs/2501.01830；https://arxiv.org/html/2501.01830。已读 search algorithm、early termination、progressive reward、datasets、models、ablations、defense tests 与 responsible-use boundary。
- **Problem → Changed Constraint → Mechanism:** 固定 jailbreak prompts 覆盖窄，人工策略扩展慢；直接 RL search 又会在低潜力分支浪费 query，并追逐单一 judge。Auto-RT 搜索攻击策略，early-terminated exploration 剪掉低潜力 branch；progressive reward tracking 先在中间 downgraded models 上跟踪收益，在 final harmful-instruction response 激增前选策略，并配 reward shaping。
- **Implementation / Evaluation Contract:** HarmBench train/test、AdvBench 用于 downgrade models；16 个 open models 与两个 70B black-box models。指标包括 test top-100 ASR、sampling efficiency、semantic diversity 和 defense generalization；ablation ETE、PRT、reward shaping。hardware、并发、query cost、judge false-positive 与生产 SLO 未披露。
- **Evidence Boundary / Trade-offs:** 证据支持 search control 可提高作者 harness 下的攻击采样效率与多样性；不证明 ASR 是真实危害、judge 无偏或策略能稳定迁移到生产。自动化降低人工枚举成本，却增加 judge gaming、toxic model dependency、策略扩散、API cost 和安全访问控制。已知威胁、严格合规或低 query budget 下，curated test suite 与 human red team 仍必要。
- **Evolution / Owner / Decision:** `Direct Evolution`（static attacks → adaptive strategy search）与 `Layering / Dependency`（search policy → target/judge → evidence triage）。Owner `PLATFORM-SECURITY` Ch72；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: judge calibration、harm severity、query-budget parity、artifact access control 与 deployment defense validity。

### REINFORCE++ v1: Critic-Free RL Is a Mechanism Bundle, Not a Universal Successor

- **Candidate / Week / Score:** REINFORCE++ / 2025-W01 / 25/30；Source Family ID `reinforce-plus-plus-v1`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-04，v2 2025-04-03，后续持续修订至 v9 2025-11-10；https://arxiv.org/abs/2501.03262；https://arxiv.org/html/2501.03262v1。W01 只审计 v1；当前大幅重构版本的 global-normalization 论述、第三方验证和扩展实验不得反投射到 v1。
- **Problem → Changed Constraint → Mechanism:** PPO 的 critic 降低 variance，却增加一套模型状态、显存、训练不稳定源与调参成本；原始 REINFORCE 简单但 variance 大。v1 将 token-level KL、PPO clipping、minibatch multiple updates、reward normalization/clipping 与 batch advantage normalization 组合进无 critic policy-gradient pipeline，以降低工程成本同时保留 trust-region 风格约束。
- **Implementation / Evaluation Contract:** Llama-3.1-8B-SFT 与 Qwen2.5-7B，general/math datasets；beta 0.01/0.001、25K samples、每 prompt 4 rollouts、rollout batch 256、train batch 128、actor lr 5e-7、clip 0.2。效率表在 Llama-3 8B、70K samples、H100 条件下报告 PPO 60h、REINFORCE++ 42h；GPU 数、precision、sequence length、并发与完整 SLO 未披露。
- **Evidence Boundary / Trade-offs:** v1 证明作者配置下无需 critic 的组合可训练并降低所报时间；不证明每个组件独立贡献、理论优越或所有 RLHF workload 胜过 PPO。去掉 critic 节省状态，却将 variance 控制依赖 batch composition、reward scale、KL/clipping 与 repeated-update bias；小 batch、稀疏/非平稳 reward 时 critic 仍可能更稳。v1 ablation 与 theory 不足，后续 revision 不能补写成事件时证据。
- **Evolution / Owner / Decision:** `Alternative Branch`（actor-critic PPO ↔ normalized critic-free policy gradient），不是单向替代。Owner `TRAIN-RLHF` Ch31；handoff `TRAIN-PPO` Ch32、`TRAIN-GRPO` Ch33。`Books Pending — Integration Deferred`。Open: v1 artifact/commit、组件消融、同预算比较、reward shift、batch sensitivity 与 revision-family splitting。

### DPO Kernels: Richer Preference Geometry Trades Simplicity for Selection and Compute State

- **Candidate / Week / Score:** DPO Kernels / 2025-W01 / 21/30；Source Family ID `dpo-kernels-divergence-family`；作者论文，Status: Experimental。
- **Event / Sources / Access:** arXiv v1 2025-01-05、v2 2025-01-08、v3 2025-01-20；https://arxiv.org/abs/2501.03271；https://arxiv.org/pdf/2501.03271v1。v1 PDF 26 页已覆盖公式、kernel/divergence selection、12 datasets、results、overhead、limitations 与 ethics；当前 HTML 只辅助导航，不把 v3 扩展倒灌到 v1。
- **Problem → Changed Constraint → Mechanism:** 标准 DPO 用固定概率差和 reference constraint，难以表达“语义接近但 token probability 不同”或不同 tail/overlap geometry。论文把 probability signal 与 jina-embeddings-v3 semantic signal 混合，再施加 polynomial、RBF、spectral、Mahalanobis 或 hierarchical mixture kernel，并从 JS、Hellinger、Rényi、Bhattacharyya、Wasserstein、f-divergence 等分支中按数据统计选择组合。训练 loop 因而新增 embedding model、kernel parameters、covariance、mixture weights 与 selection metrics 等状态。
- **Implementation / Evaluation Contract:** v1 声称用 Llama 3.3 在 HH-RLHF、HelpSteer、Chatbot Arena 2023/2024、AlpacaFarm、PRM800k、SHP-2、UltraFeedback、Nectar、Orca、Capybara 等 12 datasets 上评 factuality/reasoning/truthfulness/safety/instruction following。hardware、base checkpoint 精确规模、precision、batch、sequence length、optimizer 与 wall time 未披露；图表主要给聚合 F1，缺少完整同预算复现合同。
- **Evidence Boundary / Trade-offs:** 证据说明 DPO 的 divergence 与 representation 可形成可设计分支，并报告作者任务上的增益；不证明 kernelized objective 普遍优于标准 DPO，也没有充分 component ablation、独立复现或 adversarial test。HMK 作者自报比 baseline 高 3～4× compute，并新增 kernel collapse、bandwidth/degree/covariance sensitivity、embedding bias、privacy leakage 与 preference perturbation 风险。数据/算力有限、reward geometry 简单或可审计性优先时，标准 DPO 仍更合理。
- **Evolution / Owner / Decision:** `Alternative Branch`（fixed probability geometry ↔ semantic/kernel/divergence family），不是 DPO 的单向替代。Owner `TRAIN-DPO` Ch34；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: v1/v3 delta、artifact、完整 hyperparameters、同计算预算 ablation、embedding model drift 与 selection overfitting。

## Evidence Level

- 论文与 artifact 均属于作者证据；Status: Experimental，不视为独立复现。
- 论文中的性能数字只属于其 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator
  contract；未披露字段记为 `Not Disclosed`。
- Hugging Face、Scholar、OpenAlex、DBLP、Semantic Scholar、Crossref 只承担 discovery / metadata 角色，
  不作为机制事实来源。
- 跨论文的演进关系属于本项目推断，已显式标注。

## Cross-Week Deduplication

- Titans 后续与 MIRAS 和 Google Research synthesis 作为同一 Source Family 的演进节点联读；不把后发
  说明当成 first public。
- Certaindex / Dynasor 论文与代码属于同一 Source Family，不重复计分。
- 本周对 2024-12-24～29 论文的 HF 二次收录已回拨 2024 owner week。
- Microsoft RD-Agent 2025-01-02 英文 Blog 与 2024-09-12 中文官方说明属于同一说明节点；仓库
  `v0.3.0` 又早于本周，故该页不是 W01 的新 Source Family event。
- Microsoft “Accelerating Multilingual RAG Systems”的 video owner date 是 2024-11-29；2025-01-02 页面更新不构成
  MIRACL/NoMIRACL/MIRAGE-Bench 的新 first-public event。
- VideoRefer 的 v1 日期属于 2024-12-31，虽然编号以 `2501` 开头仍归完整 ISO W01；MapEval 同理。
- 五个新增多模态 Source Family 与 LTX-Video、Multimodal Textbook 分别承担 editing、object representation、
  latent geometry、encoder fusion 与 restoration 角色，不因同属 video/multimodal 合并计分。
- 2025-01-06～09 HF discovery replay 中，所有 first-public date 属于 W01 的候选均已回拨；固定三工作日
  grace 被 DPO-Kernels 反例推翻。01-10 与 01-13 连续两个 business-day 页面不再出现 W01 owner，
  discovery ledger 才闭合。
- EnerVerse、VITA-1.5、VisionReward、PGraphRAG 与 REINFORCE++ 当前 HTML 均包含后续 revision；本周 packet
  以 v1 为事件边界，后续实现、实验和结论只用于标出 revision evolution，不重复计分也不反投射。
- REINFORCE++ v1 与后来大幅重写版本保留同一 Source Family 的 revision nodes；只有 v1 mechanism bundle
  属于 W01。ToolHop、Virgo、SDPO、LUSIFER 等后续小修同理。

## Knowledge Tree Position

| Source Family | Stable Owner | Current Chapter | Legacy Chapter | State |
| --- | --- | --- | --- | --- |
| Titans | `MODEL-LONG-CONTEXT` | Ch22 | Ch22 | Books Pending — Integration Deferred |
| Certaindex / Dynasor | `INFER-SCHEDULING` | Ch56 | Ch52 | Books Pending — Integration Deferred |
| SWE-Gym | `AGENT-WORKFLOW` | Ch81 | Ch77 | Books Pending — Integration Deferred |
| Overthinking / Length Preference | `TRAIN-DPO` | Ch34 | Ch30 | Books Pending — Integration Deferred |
| TangoFlux | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | N/A | Books Pending — Integration Deferred |
| HumanEval Pro / MBPP Pro | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| HUNYUANPROVER | `AGENT-PLANNING` | Ch79 | Ch75 | Books Pending — Integration Deferred |
| Multimodal Textbook | `TRAIN-DATA` | Ch27 | Ch23 | Books Pending — Integration Deferred |
| CodeElo | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| LTX-Video | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | N/A | Books Pending — Integration Deferred |
| MLLM-as-a-Judge | `PLATFORM-SECURITY` | Ch72 | Ch68 | Books Pending — Integration Deferred |
| ProgCo | `AGENT-REFLECTION` | Ch80 | Ch76 | Books Pending — Integration Deferred |
| A3 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| Dynamic Scaling of Unit Tests | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| SSM Recency / Over-smoothing | `MODEL-LONG-CONTEXT` | Ch22 | Ch22 | Books Pending — Integration Deferred |
| TAPE | `MODEL-POSITION-ENCODING` | Ch13 | Ch13 | Books Pending — Integration Deferred |
| VideoAnydoor | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | N/A | Books Pending — Integration Deferred |
| VideoRefer Suite | `MULTIMODAL-REPRESENTATION` | Ch23 | N/A | Books Pending — Integration Deferred |
| VA-VAE + LightningDiT | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | N/A | Books Pending — Integration Deferred |
| MERV | `MULTIMODAL-REPRESENTATION` | Ch23 | N/A | Books Pending — Integration Deferred |
| SeedVR | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | N/A | Books Pending — Integration Deferred |
| WeAudit | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| Photorealistic Avatar Challenge | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| EnerVerse | `MULTIMODAL-WORLD-MODELS` | Ch25 | N/A | Books Pending — Integration Deferred |
| FP Quantization Training Scaling Law | `WORLDVIEW-SCALING-LAW` | Ch7 | Ch7 | Books Pending — Integration Deferred |
| VisionReward | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| BoxingGym | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| VITA-1.5 | `MULTIMODAL-REPRESENTATION` | Ch23 | N/A | Books Pending — Integration Deferred |
| AutoPresent | `AGENT-WORKFLOW` | Ch81 | Ch77 | Books Pending — Integration Deferred |
| ToolHop | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Books Pending — Integration Deferred |
| Personalized Graph-Based Retrieval | `AGENT-RAG` | Ch76 | Ch72 | Books Pending — Integration Deferred |
| Virgo | `TRAIN-SFT` | Ch29 | Ch25 | Books Pending — Integration Deferred |
| Segment-Level DPO | `TRAIN-DPO` | Ch34 | Ch30 | Books Pending — Integration Deferred |
| LUSIFER | `MODEL-EMBEDDING` | Ch12 | Ch12 | Books Pending — Integration Deferred |
| Auto-RT | `PLATFORM-SECURITY` | Ch72 | Ch68 | Books Pending — Integration Deferred |
| REINFORCE++ v1 | `TRAIN-RLHF` | Ch31 | Ch27 | Books Pending — Integration Deferred |
| DPO Kernels | `TRAIN-DPO` | Ch34 | Ch30 | Books Pending — Integration Deferred |

## Recommended Action

1. W01 的 fixed-source ledger、延伸至 2025-01-09 的 discovery grace、37 项 Full Source Review 与 13 项低分
   rejection 已完成；通过最终结构、算术、重复与链接检查后，forward cursor 进入 W02。
2. W02 必须沿用前三个工作日 discovery grace，并将 first-public date 回拨到正确 owner week，避免再次
   把聚合页日期误当事件日期。
3. Books Integration 继续冻结；任何现有 Books 结论都不在本阶段复核或修改。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期、revision 与 evidence boundary 直接保存在本 Weekly。

## Books Integration Decision

`Deferred by user request`。本周只建立可供后续 Books 阶段消费的 primary-source evidence packet；
不修改 `books/`，不把旧档案中的 `Completed` 延续为当前结论。

## Ignored Noise

- 排除 first-public date 在窗口外的 HF 重收录、二手摘要、无 primary source 的转载与营销宣称。
- 排除 Microsoft RD-Agent 2025-01-02 英文再发布：核心内容已由 2024-09-12 中文官方说明公开，
  event-time repository 也没有本周新 release；后来的 2025-05 technical report 不得反写进 W01。
- MapEval、Nested Attention、Population Aware Diffusion、SeFAR 与 finetrainers CogVideoX T2V LoRA support
  已留下 identity/date/score/rejection 记录；它们不是“未发现”，而是未达到本项目 `20+` Full Review 门槛。
- GraphGPT、Test-time Computing Survey、GS-DiT、Graph-Aware Isomorphic Attention、DepthMaster、Ingredients、
  Generalizable Origin Identification 与 MagicFace 同样完成 identity/date/score/rejection；其中 survey 只承担
  discovery taxonomy，不能替代其引用的 primary research。
- 纯 task/domain 增量但不改变 AI System mechanism、evaluation contract 或 knowledge-tree owner 的论文，
  会在 identity/date 核验后以低分拒绝，不因排行榜热度抬高评分。
- 作者最高 benchmark 若缺 workload contract，不转写为通用性能结论。

## Repository Changes

- 重建 `papers/2025/weekly/2025-W01/README.md` 的 discovery census、candidate scoring、Source Family、
  37 份 Full Source Review、13 项低分拒绝 ledger、连续两页无 owner spillback 的 closure 与 deferred Books status。
- 未修改 Books、ROADMAP、DECISIONS 或 Learning State。

## Open Questions

- Certaindex 与 length-preference training 叠加时，runtime stop signal 如何避免重复优化和 underthinking？

## Sources

- Titans — https://arxiv.org/abs/2501.00663（First Public: 2024-12-31；Accessed: 2026-08-17）
- Certaindex / Dynasor — https://arxiv.org/abs/2412.20993；https://arxiv.org/html/2412.20993（First Public: 2024-12-30；Accessed: 2026-08-17）
- SWE-Gym — https://arxiv.org/abs/2412.21139；https://arxiv.org/html/2412.21139（First Public: 2024-12-30；Accessed: 2026-08-17）
- Do NOT Think That Much — https://arxiv.org/abs/2412.21187；https://arxiv.org/html/2412.21187（First Public: 2024-12-30；Accessed: 2026-08-17）
- TangoFlux — https://arxiv.org/abs/2412.21037（First Public: 2024-12-30；Accessed: 2026-08-17）
- HumanEval Pro / MBPP Pro — https://arxiv.org/abs/2412.21199（First Public: 2024-12-30；Accessed: 2026-08-17）
- HUNYUANPROVER — https://arxiv.org/abs/2412.20735（First Public: 2024-12-30；Accessed: 2026-08-17）
- Multimodal Textbook — https://arxiv.org/abs/2501.00958；https://arxiv.org/html/2501.00958；https://github.com/DAMO-NLP-SG/multimodal_textbook（First Public: 2025-01-01；Accessed: 2026-08-17）
- CodeElo — https://arxiv.org/abs/2501.01257；https://arxiv.org/html/2501.01257；https://codeelo-bench.github.io/；https://huggingface.co/datasets/Qwen/CodeElo（First Public: 2025-01-02；Accessed: 2026-08-17）
- LTX-Video — https://arxiv.org/abs/2501.00103；https://arxiv.org/html/2501.00103；https://github.com/Lightricks/LTX-Video；https://huggingface.co/Lightricks/LTX-Video（First Public: 2024-12-30；Accessed: 2026-08-17）
- MLLM-as-a-Judge — https://arxiv.org/abs/2501.00192；https://arxiv.org/html/2501.00192（First Public: 2024-12-31；Accessed: 2026-08-17）
- ProgCo — https://arxiv.org/abs/2501.01264；https://aclanthology.org/2025.acl-short.73/；https://github.com/songxiaoshuai/progco（First Public: 2025-01-02；Accessed: 2026-08-17）
- A3 — https://arxiv.org/abs/2501.01149；https://arxiv.org/pdf/2501.01149v1；https://arxiv.org/pdf/2501.01149v2；https://arxiv.org/html/2501.01149；https://github.com/YuxiangChai/AITK（First Public: 2025-01-02；Accessed: 2026-08-17）
- Dynamic Scaling of Unit Tests — https://arxiv.org/abs/2501.01054；https://arxiv.org/html/2501.01054；https://code-reward-model.github.io/；https://github.com/RUCKBReasoning/CodeRM；https://huggingface.co/KAKA22/CodeRM-8B；https://huggingface.co/datasets/KAKA22/CodeRM-UnitTest（First Public: 2025-01-02；Accessed: 2026-08-17）
- SSM Bottlenecks — https://arxiv.org/abs/2501.00658；https://arxiv.org/pdf/2501.00658v1；https://arxiv.org/html/2501.00658；https://github.com/VITA-Group/SSM-Bottleneck；https://openreview.net/forum?id=pymXpl4qvi（First Public: 2024-12-31；Accessed: 2026-08-17）
- TAPE: Contextualized Equivariant Positional Encoding — https://arxiv.org/abs/2501.00712；https://arxiv.org/pdf/2501.00712v1；https://arxiv.org/pdf/2501.00712v2；https://github.com/VITA-Group/TAPE（First Public: 2025-01-01；Accessed: 2026-08-17）
- VideoAnydoor — https://arxiv.org/abs/2501.01427；https://arxiv.org/html/2501.01427（First Public: 2025-01-02；Accessed: 2026-08-17）
- VideoRefer Suite — https://arxiv.org/abs/2501.00599；https://arxiv.org/html/2501.00599（First Public: 2024-12-31；Accessed: 2026-08-17）
- Reconstruction vs. Generation / VA-VAE + LightningDiT — https://arxiv.org/abs/2501.01423；https://arxiv.org/html/2501.01423（First Public: 2025-01-02；Accessed: 2026-08-17）
- Unifying Specialized Visual Encoders / MERV — https://arxiv.org/abs/2501.01426；https://arxiv.org/html/2501.01426（First Public: 2025-01-02；Accessed: 2026-08-17）
- SeedVR — https://arxiv.org/abs/2501.01320；https://arxiv.org/html/2501.01320（First Public: 2025-01-02；Accessed: 2026-08-17）
- MapEval — https://arxiv.org/abs/2501.00316（First Public: 2024-12-31；Accessed: 2026-08-17；Low-score identity/date check）
- Nested Attention — https://arxiv.org/abs/2501.01407；https://arxiv.org/html/2501.01407（First Public: 2025-01-02；Accessed: 2026-08-17；Low-score identity/date check）
- Population Aware Diffusion — https://arxiv.org/abs/2501.00910；https://arxiv.org/html/2501.00910（First Public: 2025-01-01；Accessed: 2026-08-17；Low-score identity/date check）
- SeFAR — https://arxiv.org/abs/2501.01245；https://arxiv.org/html/2501.01245（First Public: 2025-01-02；Accessed: 2026-08-17；Low-score identity/date check）
- WeAudit — https://arxiv.org/abs/2501.01397；https://arxiv.org/html/2501.01397；https://www.microsoft.com/en-us/research/publication/weaudit-scaffolding-user-auditors-and-ai-practitioners-in-auditing-generative-ai/（First Public: 2025-01-02；Accessed: 2026-08-17）
- CVPR 2025 Photorealistic Avatar Challenge — https://www.microsoft.com/en-us/research/academic-program/photorealistic-avatar-challenge-cvpr-2025/challenge/；https://www.microsoft.com/en-us/research/academic-program/photorealistic-avatar-challenge-cvpr-2025/rules/；https://www.microsoft.com/en-us/research/academic-program/photorealistic-avatar-challenge-cvpr-2025/timeline/（Announcement: 2025-01-03；Accessed: 2026-08-17）
- EnerVerse — https://arxiv.org/abs/2501.01895；https://arxiv.org/html/2501.01895（First Public: 2025-01-03；Accessed: 2026-08-17）
- Scaling Laws for Floating Point Quantization Training — https://arxiv.org/abs/2501.02423；https://arxiv.org/html/2501.02423v1（First Public: 2025-01-05；Accessed: 2026-08-17）
- VisionReward — https://arxiv.org/abs/2412.21059；https://arxiv.org/html/2412.21059（First Public: 2024-12-30；Accessed: 2026-08-17）
- BoxingGym — https://arxiv.org/abs/2501.01540；https://arxiv.org/html/2501.01540v1（First Public: 2025-01-02；Accessed: 2026-08-17）
- VITA-1.5 — https://arxiv.org/abs/2501.01957；https://arxiv.org/html/2501.01957（First Public: 2025-01-03；Accessed: 2026-08-17）
- AutoPresent — https://arxiv.org/abs/2501.00912；https://arxiv.org/html/2501.00912v1（First Public: 2025-01-01；Accessed: 2026-08-17）
- ToolHop — https://arxiv.org/abs/2501.02506；https://arxiv.org/html/2501.02506v1（First Public: 2025-01-05；Accessed: 2026-08-17）
- Personalized Graph-Based Retrieval — https://arxiv.org/abs/2501.02157；https://arxiv.org/html/2501.02157v1（First Public: 2025-01-04；Accessed: 2026-08-17）
- Virgo — https://arxiv.org/abs/2501.01904；https://arxiv.org/html/2501.01904v1（First Public: 2025-01-03；Accessed: 2026-08-17）
- Segment-Level DPO — https://arxiv.org/abs/2501.01821；https://arxiv.org/html/2501.01821v1（First Public: 2025-01-03；Accessed: 2026-08-17）
- LUSIFER — https://arxiv.org/abs/2501.00874；https://arxiv.org/html/2501.00874v1（First Public: 2025-01-01；Accessed: 2026-08-17）
- Auto-RT — https://arxiv.org/abs/2501.01830；https://arxiv.org/html/2501.01830（First Public: 2025-01-03；Accessed: 2026-08-17）
- REINFORCE++ v1 — https://arxiv.org/abs/2501.03262；https://arxiv.org/html/2501.03262v1（First Public: 2025-01-04；Accessed: 2026-08-17）
- DPO Kernels — https://arxiv.org/abs/2501.03271；https://arxiv.org/pdf/2501.03271v1（First Public: 2025-01-05；Accessed: 2026-08-17）
- Graph Generative Pre-trained Transformer — https://arxiv.org/abs/2501.01073（First Public: 2025-01-02；Low-score identity/date check；Accessed: 2026-08-17）
- Test-time Computing Survey — https://arxiv.org/abs/2501.02497（First Public: 2025-01-05；Low-score identity/date check；Accessed: 2026-08-17）
- GS-DiT — https://arxiv.org/abs/2501.02690（First Public: 2025-01-05；Low-score identity/date check；Accessed: 2026-08-17）
- Graph-Aware Isomorphic Attention — https://arxiv.org/abs/2501.02393（First Public: 2025-01-04；Low-score identity/date check；Accessed: 2026-08-17）
- DepthMaster — https://arxiv.org/abs/2501.02576（First Public: 2025-01-05；Low-score identity/date check；Accessed: 2026-08-17）
- Ingredients — https://arxiv.org/abs/2501.01790（First Public: 2025-01-03；Low-score identity/date check；Accessed: 2026-08-17）
- Generalizable Origin Identification — https://arxiv.org/abs/2501.02376（First Public: 2025-01-04；Low-score identity/date check；Accessed: 2026-08-17）
- MagicFace — https://arxiv.org/abs/2501.02260（First Public: 2025-01-04；Low-score identity/date check；Accessed: 2026-08-17）
- Accelerating Multilingual RAG Systems — https://www.microsoft.com/en-us/research/?p=1115469（Video owner date: 2024-11-29；Cross-week Exclusion；Accessed: 2026-08-17）
- Microsoft RD-Agent official pages and release ledger — https://www.microsoft.com/en-us/research/articles/rd-agent/（Published: 2024-09-12）；https://www.microsoft.com/en-us/research/articles/rd-agent-an-open-source-solution-for-smarter-rd/（English republication: 2025-01-02）；https://github.com/microsoft/RD-Agent/releases（Cross-week Exclusion；Accessed: 2026-08-17）
- vLLM release boundary — https://github.com/vllm-project/vllm/releases/tag/v0.6.6（Released: 2024-12-27；Accessed: 2026-08-17）
- SGLang release boundary — https://github.com/sgl-project/sglang/releases/tag/v0.4.1（Released: 2024-12-25；Accessed: 2026-08-17）
- Transformers release history — https://pypi.org/project/transformers/（4.47.1: 2024-12-17；4.48.0: 2025-01-10；Accessed: 2026-08-17）
- Accelerate release history — https://pypi.org/project/accelerate/（1.2.1: 2024-12-13；1.3.0: 2025-01-17；Accessed: 2026-08-17）
- DeepSpeed release history — https://pypi.org/project/deepspeed/（0.16.2: 2024-12-18；0.16.3: 2025-01-21；Accessed: 2026-08-17）
- MLX release history — https://pypi.org/project/mlx/（0.21.1: 2024-12-06；0.22.1: 2025-02-06；Accessed: 2026-08-17）
- llama-cpp-python release history — https://pypi.org/project/llama-cpp-python/（0.3.5: 2024-12-10；0.3.6: 2025-01-08；Accessed: 2026-08-17）
- ONNX Runtime release history — https://pypi.org/project/onnxruntime/（1.20.1: 2024-11-21；1.21.0: 2025-03-08；Accessed: 2026-08-17）
- KServe release boundary — https://github.com/kserve/kserve/releases/tag/v0.15.0（Released: 2025-03-31；Accessed: 2026-08-17）
- finetrainers release history — https://pypi.org/project/finetrainers/（First packaged release: 2025-03-05；the 2025-01-03 item is a project-log event, not a stable release；Accessed: 2026-08-17）
- Hugging Face discovery pages — https://huggingface.co/papers?date=2024-12-30；https://huggingface.co/papers?date=2024-12-31；https://huggingface.co/papers/date/2025-01-03；https://huggingface.co/papers/date/2025-01-06；https://huggingface.co/papers/date/2025-01-07；https://huggingface.co/papers/date/2025-01-08；https://huggingface.co/papers/date/2025-01-09（Discovery Only；Accessed: 2026-08-17）
