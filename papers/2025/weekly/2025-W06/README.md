# AI Research Weekly — 2025-W06

> Coverage Window: 2025-02-03～2025-02-09
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Rebuild Started: 2026-08-18
> Accessed: 2026-08-18
> Backfilled: 2026-07-31
> Weekly Evidence Gate: Passed — 78 candidates identified；72/72 `20+` Full Source Reviews complete；6/6 low-score candidates verified
> Books Integration: Deferred by user request

## Executive Summary

旧档将本周错误记为“无保留候选”。固定来源与 2 月3～10日 discovery replay 首轮恢复 63 个可唯一定位的
Source Family；W07 推荐页反向核验又发现 7 篇 arXiv v1 实际发表于 2 月5～9日，必须按 first-public date
回拨 W06：The Curse of Depth、Social-Deduction MARL、LM2、Hierarchical Drafting、Gemstones、CTRL 与
NoLiMa。W07 全量 replay 又暴露 7 个此前未入 owner week 的 family：CODESIM、APE、Hypencoder、
arXiv:2502.05415 的事件时 v1（Show-o Turbo，而非 5 月重写后的 UniCMs）、Competitive Programming、
Éclair 与 CAD-Editor。W08 look-ahead 进一步发现 `Jailbreaking to Jailbreak` 虽在 2 月 17 日推荐页出现，
arXiv v1 实际为 2 月 9 日；该 family 已按 first-public date 回拨 W06，并完成事件时全文、威胁模型、
工作流、实验与 Appendix 审计。当前 census 因此为 78 项，低分校准复核后 72 项达到 `20+` 全文门槛，
6 项进入低分核验。当前完成 OmniHuman-1、PRIME、
DeepRAG、FastKV、vLLM 0.7.2、SmolLM2、LIMO、recurrent-depth latent reasoning、Sliding Tile Attention、
QuEST、BOLT、Satori、QLASS、On-device Sora、KVFundaBench/ShotKV、AlphaGeometry2、ScoreFlow、VideoRoPE、
SCONE、InferenceGuard、Transformer World Models、LongDPO、VideoJAM、Inverse Bridge Matching Distillation、
Demystifying Long CoT、Teacher Hacking、Token Assorted、PyCapsule、ConceptAttention、UltraIF、Goku、
Self-Backtracking、DuoGuard、Symbolic World Models、CMoE、CodeSteer、VectorQ 与 Gemini 2.0 GA 的非模板化
Full Source Review；并进一步闭合 MGA、HMA、particle inference、Speak Easy、verification scaling 与 Preference
Leakage，以及 Direct Alignment、AlignVLM、ZebraLogic、ACECODER、AStar、JUMP、ReasoningWeekly、RandLoRA、
Improved Latent Consistency、COCONut-PanCap、SynCD、AIM、3D point-regularized video generation、SliderSpace、
MakeAnything 与 TwinMarket。原有 67 个 `20+` 候选与本轮新增 CODESIM、APE、Hypencoder、Show-o Turbo
均已完成事件时版本全文审计。特别地，arXiv:2502.05415 的 v1 与 v2 标题和方法发生实质变化，不能用
当前 UniCMs metadata 覆盖 2 月事件。Transformers 4.48.3、MLX 0.22.1、LayerTracer、Competitive
Programming、Éclair 与 CAD-Editor 六个低分候选也完成来源、日期、评分与拒绝边界核验。W06 延迟发现的
2025-01-21 CUT3R 已按 arXiv v1 回拨 W04 并重新通过前周 Gate。
本阶段不修改 Books，Historical Books Gate 关闭。

## Coverage Window and Limitations

- 事件归属使用官方发布日期、GitHub Release 时间或 arXiv v1；Hugging Face 推荐日只用于发现。
- arXiv、Google Scholar、OpenAlex、DBLP 用于 discovery/去重，Semantic Scholar 与 Hugging Face 补充召回，Crossref 仅交叉核验 metadata。
- W06 Evidence Gate 已在 W07/W08 look-ahead spillback 后重新通过；72 个 `20+` family 均完成 Method、Evaluation、Appendix、limitations 与 artifact/版本边界，6 个低分候选完成 identity/date/score/rejection 核验。
- 作者 benchmark 只代表披露的模型、数据、硬件、精度、长度、batch/concurrency 与 evaluator；未披露字段写 `Not Disclosed`。
- Gemini 2.0 GA、Transformers 4.48.3 与 MLX 0.22.1 只按公开版本事实判断；未公开内部机制不从产品能力反推。
- 历史回填不补造 Daily；本轮访问日期统一为 2026-08-18。

## 1. 模型与研究机构

### Source Coverage

按固定顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、
Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、
StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Google Gemini 2.0 Flash GA / Flash-Lite preview、SmolLM2 technical report、OmniHuman-1。
- Gemini 2.0 本周只证明 model/API availability、multimodal input/text output、1M context 与公开 safety process；机制未披露。
- W06 推荐页中的 CUT3R v1 为 1月21日，已回拨 W04；不在本周重复计分。

## 2. 论文与学术来源

### Discovery Census

- `20+` 主线：PRIME、DeepRAG、FastKV、SCONE、Almost Surely Safe Alignment、Improving Transformer
  World Models、LongDPO、VideoJAM、Inverse Bridge Matching Distillation、Satori、QLASS、KV Cache
  Compression fundamental-abilities study、SmolLM2、LIMO、Demystifying Long CoT、Teacher Hacking、
  Token Assorted、LLM Guided Self-Debugging、AlphaGeometry2、ConceptAttention、BOLT、UltraIF、ScoreFlow、
  latent-reasoning test-time scaling、Goku、VideoRoPE、Sliding Tile Attention、QuEST、Self-Backtracking、
  DuoGuard、Symbolic World Models、CMoE、On-device Sora、CodeSteer 与 VectorQ。
- 校准提升至 `20+`：Direct Alignment Algorithms are a Blur、Preference Leakage、AlignVLM、ZebraLogic、
  ReasoningWeekly、RandLoRA、improved latent-consistency training、ACECODER、Sample/Scrutinize/Scale、
  COCONut-PanCap、multi-image synthetic data、AStar、particle-based inference scaling、JUMP、
  activation-informed merging、MGA、Physical Understanding in Video Generation、HMA 与 Speak Easy。
- 校准后提升至 `20+`：SliderSpace、MakeAnything 与 TwinMarket；低分核验：LayerTracer。
- W07 discovery spillback 至 `20+`：The Curse of Depth、Training Language Models for Social Deduction with MARL、LM2、Hierarchical Drafting、Gemstones、Teaching Language Models to Critique via RL / CTRL 与 NoLiMa；七者 v1 均在 2025-02-05～09，不能按推荐日留在 W07。
- W07 完整推荐页二次回拨：CODESIM、APE、Hypencoder 与 arXiv:2502.05415 的事件时 v1（Show-o Turbo）达到 `20+`；Competitive Programming、Éclair 与 CAD-Editor 完成低分核验。arXiv:2502.05415 v2 的 UniCMs 是 5 月 revision，不得倒灌成 W06 事件。
- W08 look-ahead 回拨：`Jailbreaking to Jailbreak`（arXiv:2502.09638）v1 为 2025-02-09；Hugging Face 2025-02-17 只是推荐日期。该 family 达到 `20+`，已完成事件时版本 Full Source Review。

## 3. AI Infra 与工程项目

### Fixed-source Release Ledger

| Candidate | Primary ID | Event Date | Current State | Evidence Boundary |
| --- | --- | --- | --- | --- |
| vLLM 0.7.2 | GitHub release `v0.7.2` + linked PR/code | 2025-02-06 | Full Review Complete | prefix-cache identity与structured-decoding PR已核验；其余不可稳定读取的PR仅保留release fact |
| Transformers 4.48.3 | GitHub release `v4.48.3` | 2025-02-07 | Low-score Verified | patch/compatibility fact；无独立长期机制结论 |
| MLX 0.22.1 | GitHub release `v0.22.1` | 2025-02-06 | Low-score Verified | signed tag/version fact；release未披露独立机制 |

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| vLLM 0.7.2 | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| OmniHuman-1 | 5 | 4 | 4 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| PRIME / Process Reinforcement through Implicit Rewards | 5 | 5 | 4 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| FastKV | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| DeepRAG | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| SmolLM2 | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| LIMO | 5 | 5 | 4 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Latent Reasoning Test-Time Scaling | 5 | 5 | 4 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Sliding Tile Attention | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| QuEST | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| On-device Sora | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| BOLT | 5 | 5 | 4 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Satori | 5 | 5 | 4 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| QLASS | 5 | 5 | 5 | 5 | 4 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| KV Cache Compression Fundamental-Abilities Study | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| AlphaGeometry2 | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| ScoreFlow | 5 | 4 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| VideoRoPE | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| SCONE / Scaling Embedding Layers | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Almost Surely Safe Alignment | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Improving Transformer World Models | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| LongDPO | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| VideoJAM | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Inverse Bridge Matching Distillation | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Demystifying Long Chain-of-Thought | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Teacher Hacking | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Token Assorted | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| LLM Guided Self-Debugging | 4 | 4 | 5 | 5 | 4 | 1 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| ConceptAttention | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| UltraIF | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Goku | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Self-Backtracking | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| DuoGuard | 4 | 5 | 5 | 5 | 4 | 1 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Symbolic World Models via Test-time Scaling | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| CMoE | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| CodeSteer | 4 | 4 | 5 | 5 | 4 | 1 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| VectorQ / Adaptive Semantic Prompt Caching | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| Gemini 2.0 Flash GA / Flash-Lite Preview | 2 | 5 | 5 | 5 | 3 | 0 | 20/30 | Full Review Complete — Weekly Only / Version Fact / Mechanism Not Disclosed；Books Deferred |
| The Curse of Depth | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Social-Deduction MARL | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| LM2 / Large Memory Models | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Hierarchical Drafting | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| Gemstones / Multi-Faceted Scaling Laws | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| CTRL / Teaching Language Models to Critique via RL | 4 | 4 | 4 | 5 | 5 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| NoLiMa | 4 | 4 | 5 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Transformers 4.48.3 | 1 | 3 | 4 | 5 | 2 | 1 | 16/30 | Low-score Verified — patch/compatibility version fact |
| MLX 0.22.1 | 1 | 3 | 3 | 5 | 2 | 1 | 15/30 | Low-score Verified — tag/version fact；mechanism not disclosed |
| Direct Alignment Algorithms are a Blur | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Preference Leakage | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Review Complete；Books Pending — Integration Deferred |
| AlignVLM | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| SliderSpace | 4 | 3 | 3 | 5 | 3 | 2 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| MakeAnything | 4 | 3 | 4 | 5 | 3 | 1 | 20/30 | Full Review Complete；Books Pending — Integration Deferred |
| ZebraLogic | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| ReasoningWeekly / PhD Knowledge Not Required | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| RandLoRA | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| Improved Latent Consistency Training | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| ACECODER | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Sample, Scrutinize and Scale | 4 | 5 | 4 | 5 | 5 | 3 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| COCONut-PanCap | 3 | 4 | 4 | 5 | 3 | 2 | 21/30 | Full Review Complete；Books Pending — Integration Deferred |
| Multi-Image Synthetic Data | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| TwinMarket | 3 | 3 | 4 | 5 | 4 | 2 | 21/30 | Full Review Complete；Books Pending — Integration Deferred |
| AStar / MCTS for Multimodal Reasoning | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| LayerTracer | 3 | 3 | 3 | 5 | 3 | 1 | 18/30 | Low-score Verified — Weekly Only / Narrow-domain principle reuse |
| Particle-Based Inference Scaling / Rollout Roulette | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| JUMP / Universal Multi-Prompt Jailbreak | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| Activation-Informed Model Merging | 4 | 4 | 4 | 5 | 3 | 2 | 22/30 | Full Review Complete；Books Pending — Integration Deferred |
| MGA / Pretraining Data Reformulation | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Physical Understanding in Video Generation | 4 | 4 | 4 | 5 | 4 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| HMA / Learning Real-World Action-Video Dynamics | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete；Books Pending — Integration Deferred |
| Speak Easy | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Jailbreaking to Jailbreak | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Review Complete；Books Pending — Integration Deferred |
| CODESIM | 4 | 3 | 4 | 5 | 5 | 2 | 23/30 | Full Review Complete；Books Pending — Integration Deferred |
| APE / Adaptive Parallel Encoding | 5 | 5 | 5 | 5 | 5 | 2 | 27/30 | Full Review Complete；Books Pending — Integration Deferred |
| Hypencoder | 5 | 4 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Books Pending — Integration Deferred |
| Show-o Turbo / arXiv:2502.05415v1 | 5 | 4 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete；Revision identity corrected；Books Pending — Integration Deferred |
| Competitive Programming with Large Reasoning Models | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only / Capability Evidence |
| Éclair | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only / Domain Application |
| CAD-Editor | 4 | 3 | 3 | 5 | 2 | 2 | 19/30 | Low-score Verified — Weekly Only / Domain Application |

## Deep Analysis

本周 Deep Analysis 只保留三个已经通过全文 Gate 的长期机制：mixed-condition data scaling、online
implicit process reward，以及 prefill-stage KV/hidden-state compression。其他候选在 Full Source Review
完成前不写深入结论。

### Deep Analysis 1 — OmniHuman-1

- **Why:** 单条件 human animation 依赖强过滤，丢掉大量包含有效运动先验但与 audio/pose 弱相关的数据。
- **Principle / Mechanism:** 以 text→audio→pose 的条件强度顺序做三阶段 mixed-condition training；弱条件使用更多数据/更高训练比例，强条件低比例加入以减少 shortcut domination。
- **Trade-off:** 数据利用率和动作多样性提高，但条件冲突、CFG calibration、identity/temporal drift 与分段长视频状态成为新风险。
- **Connection / Evolution:** `MULTIMODAL-GENERATIVE-PARADIGMS` 主 owner，handoff `TRAIN-DATA` 与 world-state/identity 边界。

### Deep Analysis 2 — PRIME

- **Why:** outcome-only RL 的最终奖励稀疏，人工 process labels 又昂贵且可能把错误推理路径固化。
- **Principle / Mechanism:** 从在线 policy rollouts 的正确/错误结果学习 implicit PRM，以 policy/reference log-ratio 差分形成 token/step reward，再与 outcome verifier 一起进入 advantage estimate。
- **Trade-off:** 改善作者 math/code 任务的 sample efficiency，但新增 reward-policy co-adaptation、PRM drift、verifier dependence 与 double-forward 成本；不能外推为所有 PPO/value model 冗余。
- **Connection / Evolution:** `TRAIN-RLHF` / `TRAIN-GRPO` 的 credit-assignment 分支，handoff evaluation/verifier contract。

### Deep Analysis 3 — FastKV

- **Why:** 传统 KV pruning 在所有层跑完整 prompt 后才选 token，减少 decode memory 却不能降低 prefill TTFT；head-wise unequal budgets 又可能被最长 head 拖慢。
- **Principle / Mechanism:** 在中间层用 attention 识别 task-relevant tokens，同时压缩 hidden sequence；后续层只处理筛选后的 token，并为 KV 保留统一 budget。
- **Trade-off:** prefill compute 与 KV memory 可一起下降，但早期错误选择无法恢复，filter-layer/task sensitivity、position/causal semantics 和 kernel shape 成为新风险。
- **Connection / Evolution:** `INFER-PREFILL`→`INFER-KV-CACHE`→`INFER-SCHEDULING`，属于 selective state materialization，而不是“无损长上下文”。

## Full Source Review

### OmniHuman-1

- **Candidate / Week / Score:** OmniHuman-1 / 2025-W06 / 25/30。
- **Source Family ID:** `omnihuman-mixed-condition-human-animation`。
- **Source Type:** arXiv v1 paper + official project page。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；后续 revision 不改变 W06 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01061v1；https://arxiv.org/abs/2502.01061；https://omnihuman-lab.github.io/。
- **Related Primary Sources:** Seaweed/MMDiT、human-animation baselines 与 causal 3D VAE 只作为依赖和比较。
- **Access and Verification Status:** Full Source Review Complete；Method、training ratios、inference、evaluation、ablation 与公开 project samples 已核验。
- **Full-read Coverage:** 已读 Introduction/Related Work、omni-condition architecture、三阶段 training、CFG annealing、long-video continuation、data/evaluation、ratio ablation 与 conclusion。
- **Original Problem:** audio/pose 单条件模型为稳定训练大量过滤视频，丢弃包含动作、镜头和交互先验的数据，导致规模化受限。
- **Why the Previous Design Was Reasonable:** 单条件数据语义清晰、同步/pose监督强、训练更稳定；小数据和受控头像任务不需要承担多条件冲突。
- **Changed Constraint:** 希望覆盖全身、风格、物体交互与多种驱动方式，训练必须利用不同标注强度的大规模异构视频。
- **Mechanism:** 从 text/image 弱条件到 audio、pose 强条件渐进训练；强条件任务复用弱条件数据，且条件越强训练比例越低，防止模型依赖强 shortcut；reference/video tokens 共享 DiT self-attention。
- **State Ownership:** reference image 拥有 appearance identity；text/audio/pose 分别拥有语义、节奏与几何动作约束；DiT latent 拥有生成状态；前段尾帧作为长视频 continuation state。
- **Control Flow / Data Flow:** video/image→causal 3D VAE→latent；audio→wav2vec/MLP/cross-attention，pose→heatmap encoder/channel concat，reference→packed tokens；flow-matching denoising→video segment→尾帧传给下一段。
- **Implementation Details:** MMDiT backbone、audio adjacent-frame features、pose adjacent-frame features、temporal-zeroed reference RoPE、audio/text CFG 与 annealing。
- **Evaluation Contract:** 18.7K 小时 human-related data，其中约13%满足 lip-sync/pose过滤；CelebV-HQ、RAVDESS 与 CyberHost test set，比较 portrait/body animation baselines与主客观指标。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 SadTalker、Hallo、VExpress、Loopy、CyberHost 等；核验 audio training ratio 与 mixed-condition ablation；未提供完整模型规模/训练集群和 serving latency。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 原文未形成完整 hardware/precision/batch/concurrency/SLO contract；长视频受显存与分段状态限制，作者指标不可外推到生产吞吐。
- **What the Evidence Actually Proves:** 在作者训练和测试范围内，按条件强度组织数据/训练比例能利用原本被强过滤丢弃的数据，并改善多条件 human animation。
- **What It Does Not Prove:** 不证明数据规模单独导致全部收益、不证明任意多模态条件可同样混合，也不证明视频质量等同物理正确性或可控 embodied behavior。
- **Limitations / Threats to Validity:** 私有大规模数据、模型/集群披露有限；评测依赖自动感知指标和受限人类样本；分段长视频可能累积 identity/motion drift。
- **Trade-offs / New Failure Modes:** 数据复用增加同时带来 condition leakage、强条件 shortcut、冲突 gradient、CFG artifact、lip/gesture mismatch 与 segment-boundary discontinuity。
- **Where the Previous Design Still Applies:** 单头像、单驱动、严格受控域用专用模型更简单；强 pose 控制和高保真场景可保留两阶段显式 controller。
- **Evolution Relationship:** `Direct Evolution`：single-condition filtered data→mixed weak/strong conditions→ratio-aware curriculum→segment continuation state。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23、`TRAIN-DATA` Ch27、`MULTIMODAL-WORLD-MODELS` Ch25。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～27 的 condition identity、generation objective、world-state 与 data contract。
- **Existing Coverage:** Books 已覆盖 modality-specific encoding 与 generation branches；本 family 提供 mixed-condition data-scaling 分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不保留脱离数据/metric contract 的作者排名。
- **Open Questions:** 条件冲突如何在线监控；segment state如何版本化/回滚；隐私、授权与身份滥用如何进入生成 pipeline gate。

### PRIME / Process Reinforcement through Implicit Rewards

- **Candidate / Week / Score:** PRIME / 2025-W06 / 26/30。
- **Source Family ID:** `prime-online-implicit-process-reward`。
- **Source Type:** arXiv v1 research paper + official model/code artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；后续 revision 同 family 核验。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01456v1；https://arxiv.org/abs/2502.01456。
- **Related Primary Sources:** RLOO、REINFORCE、PPO、GRPO 和 DPO/implicit-reward derivation只定义 optimizer/baseline genealogy。
- **Access and Verification Status:** Full Source Review Complete；公式、online PRM update、advantage、算法、训练、ablation、zero experiments 与 appendices 已核验。
- **Full-read Coverage:** 已读 RL/dense-reward背景、implicit PRM derivation、online training loop、outcome/process reward组合、model/data、sample efficiency、PRM update、algorithm/value ablation 与 limitations。
- **Original Problem:** outcome reward 只在序列末端出现，长 reasoning 的 credit assignment 高方差；显式 PRM 需要昂贵且语义模糊的 step labels。
- **Why the Previous Design Was Reasonable:** outcome verifier 可自动执行且不约束推理风格；value model/GAE 是通用降方差工具；人工 PRM 在可标注域提供局部监督。
- **Changed Constraint:** reasoning rollout 更长、错误路径更多，需要 dense signal，同时不希望另建大规模 step-level 标注集。
- **Mechanism:** 用正确/错误 outcome 训练隐式 PRM；以 policy/reference token log-ratio累积为隐式 value，相邻差分为 process reward；每轮先更新 PRM再用于 policy advantage，可与 RLOO/REINFORCE/GRPO/PPO组合。
- **State Ownership:** outcome verifier 拥有终局正确性；implicit PRM 拥有 step reward estimate；reference policy 定义相对基线；policy/rollout buffer 拥有当前 sampling distribution。
- **Control Flow / Data Flow:** prompt→policy rollouts→outcome labels→online implicit-PRM update→token rewards重算/缓存→outcome+process advantage→policy update→下一轮分布变化。
- **Implementation Details:** single/double-forward、online/offline PRM、reward normalization、RLOO/GRPO/REINFORCE/PPO variants；PRM与policy共演化是机制核心。
- **Evaluation Contract:** Qwen2.5-Math-7B base + lightweight SFT，数学与代码 benchmarks；与 outcome-only RL、offline/frozen PRM、不同 advantage/value用法比较。
- **Baselines / Ablations / Sensitivity / Overhead:** 核验 sample-efficiency、online update、single/double-forward、不同 RL algorithm、PRM as reward/value、zero-start 与 model scale；结果集中可自动验证任务。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B/32B实验、数据量和训练 steps部分披露；硬件、precision、rollout并发、长度分布与wall-clock/SLO不完整。
- **What the Evidence Actually Proves:** 在作者 math/code 设置中，online implicit process reward 比 outcome-only 或冻结 PRM 更高效，并可作为多个 policy-gradient estimator 的附加 reward。
- **What It Does Not Prove:** 不证明所有 PRM 应替代 value model、不证明开放域主观任务同样成立，也不证明隐式 reward 对 reward hacking 或 distribution shift 稳健。
- **Limitations / Threats to Validity:** ground-truth verifier依赖、单一模型家族、PRM/policy共适应、benchmark contamination 与训练系统细节不全；“generic”仅指作者测试算法。
- **Trade-offs / New Failure Modes:** 减少人工标签却新增 online reward drift、policy-PRM feedback loop、reference mismatch、reward scale竞争、double-forward计算和错误 verifier 放大。
- **Where the Previous Design Still Applies:** outcome-only RL适合短轨迹/可靠终局奖励；显式人工PRM适合安全关键、可审计步骤；critic/value仍适合连续控制或成熟actor-critic环境。
- **Evolution Relationship:** `Alternative Branch`：outcome-only MC→human/process labels→offline PRM→online implicit PRM；不是对 PPO/value learning 的普遍否定。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；handoff `TRAIN-PPO` Ch32、`TRAIN-GRPO` Ch33、`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～34 与 Ch66 的 data/reward/verifier/optimizer boundary。
- **Existing Coverage:** Books 已区分 outcome/process/verifier；本研究增加 online co-adaptation 分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把作者 2.5×/benchmark gains 外推为通用训练效率。
- **Open Questions:** PRM drift怎样检测；reference多久刷新；错误 verifier 如何隔离；跨节点 rollout/reward version怎样写入 checkpoint lineage。

### DeepRAG

- **Candidate / Week / Score:** DeepRAG / 2025-W06 / 26/30。
- **Source Family ID:** `deeprag-stepwise-retrieval-mdp-calibration`。
- **Source Type:** arXiv v1 paper + author artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；后续 revision 同 family，不改变 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01142v1；https://arxiv.org/abs/2502.01142。
- **Related Primary Sources:** Self-RAG、Search-o1、AirRAG、classifier/confidence adaptive retrieval 只作前代分支。
- **Access and Verification Status:** Full Source Review Complete；MDP、binary-tree synthesis、imitation/calibration、evaluation、ablation、prompts 与 limitations 已核验。
- **Full-read Coverage:** 已读 knowledge-boundary背景、state/action/reward定义、tree search、minimal-retrieval trajectory、chain of calibration、datasets/baselines/metrics、retrieval-cost与component ablation。
- **Original Problem:** 固定 retrieve-everything 成本高且引入噪声；模型自报“知道/不知道”又未校准，单次检索决策无法随 decomposition 演化。
- **Why the Previous Design Was Reasonable:** always-retrieve 简单、可重复，能降低 parametric hallucination；classifier/threshold在稳定域易监控；单次RAG适合简单问题。
- **Changed Constraint:** 多跳问题需要逐步分解，每个 subquery 的 parametric/retrieval边界不同，系统要联合优化正确性与检索成本。
- **Mechanism:** 把 reasoning建模为MDP；每步选择 continue/terminate 与 retrieve/parametric；binary tree枚举两类知识路径，用正确且检索成本最小的轨迹做 imitation，再构造 preference data校准 atomic decisions。
- **State Ownership:** partial solution拥有子问题/中间答案/文档；retriever拥有external evidence；policy拥有分解和action；reward把终局正确性与累计retrieval cost绑定。
- **Control Flow / Data Flow:** question→subquery→binary retrieve/parametric branch→intermediate response写入state→continue/terminate→final verifier/cost→trajectory selection→SFT/preference calibration。
- **Implementation Details:** binary-tree offline synthesis、minimal-cost correct path、Chain of Calibration；runtime model不需要独立线性分类头，但依赖训练时搜索和可靠答案判定。
- **Evaluation Contract:** 多跳 QA datasets、不同 LLM backbones与 RAG baselines；报告 answer accuracy、retrieval次数/比例和路径分析；retriever/corpus版本属于实验合同。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 always/no retrieval、classifier/confidence/LLM-based adaptive RAG；核验 imitation/calibration、tree-search depth 与 retrieval cost；离线树搜索成本不能从在线指标中消失。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型/数据和retrieval settings部分披露；GPU、precision、index size、并发、P95 latency与freshness SLO不完整。
- **What the Evidence Actually Proves:** 在作者 QA 设置中，把检索决策放进逐步 state/action并用搜索生成监督，可在保持/提高准确率时减少不必要检索。
- **What It Does Not Prove:** 不证明模型真正知道自身知识边界、不证明开放web freshness/poisoning下稳定，也不证明离线tree cost对生产总体成本可忽略。
- **Limitations / Threats to Validity:** benchmark/corpus静态、终局正确性可得、synthetic trajectory与teacher bias；retrieval failure、contradiction、index更新和security证据有限。
- **Trade-offs / New Failure Modes:** 少检索降低成本，却增加错误parametric branch的不可恢复性；更多状态和校准数据带来trajectory explosion、stale corpus identity与reward shortcut。
- **Where the Previous Design Still Applies:** always-retrieve适合高风险、证据必须可引用的任务；简单single-hop可用一次检索；显式classifier适合稳定域与可审计policy。
- **Evolution Relationship:** `Direct Evolution`：always/no retrieval→single adaptive gate→stepwise retrieve/parametric actions→cost-aware calibrated trajectory。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；handoff `AGENT-CONTEXT` Ch75、`AGENT-MEMORY` Ch77、`AGENT-PLANNING` Ch79 与 Ch66 evaluation。
- **Target and Adjacent Chapters Read:** 已核对 Ch75～79 和 Ch66 的 information state、evidence identity、planning与evaluation boundary。
- **Existing Coverage:** Books 已覆盖 adaptive retrieval 与 knowledge boundary；本 paper 的MDP/calibration实例是否refine正文待Books Gate。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不复制脱离retriever/corpus/model的准确率数字。
- **Open Questions:** retrieval failure怎样进入transition；document provenance/freshness如何写进state；错误parametric branch能否rollback；离线tree生成成本如何摊销。

### FastKV

- **Candidate / Week / Score:** FastKV / 2025-W06 / 27/30。
- **Source Family ID:** `fastkv-prefill-token-select-hidden-kv-compression`。
- **Source Type:** arXiv v1 systems/algorithm paper + author artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；后续 revision 同 family。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01068v1；https://arxiv.org/abs/2502.01068。
- **Related Primary Sources:** SnapKV、AdaKV、HeadKV、GemFilter 定义 head-wise与filter-layer前代，不作为FastKV独立证据。
- **Access and Verification Status:** Full Source Review Complete；算法、layer/token selection、KV budget、runtime/evaluation、ablation、limitations 与 implementation 细节已核验。
- **Full-read Coverage:** 已读 long-context/KV背景、TSP layer、attention aggregation、hidden-state pruning、后续layer KV compression、benchmarks、latency/memory、budget/layer sensitivity 与 appendix。
- **Original Problem:** KV cache随长度线性增长；多数 pruning 仍让完整prompt通过所有层，只降低decode memory，不降低prefill计算和TTFT。
- **Why the Previous Design Was Reasonable:** 全token prefill保持每层语义和exact causal computation；head-wise保留适合不同attention pattern；KV-only pruning对现有engine侵入较小。
- **Changed Constraint:** 长prompt下 prefill本身成为延迟/算力瓶颈，且 unequal head budgets会让kernel被最长序列拖慢。
- **Mechanism:** 在 Task-Specific Prompt layer 聚合 attention识别全局重要token，保留 observation window与高分token；压缩 hidden sequence后传入更深层，并为各层生成固定budget KV cache。
- **State Ownership:** filter/TSP layer拥有token selection decision；compressed hidden sequence拥有后续计算域；各层KV cache拥有选中token state；position identity必须跨压缩保留。
- **Control Flow / Data Flow:** full prompt进入前若干层→TSP attention score→选token/压hidden→后续层只计算子序列→per-layer KV selection→decode读取压缩cache。
- **Implementation Details:** layer-level selection避免head-length imbalance，hidden/KV两阶段压缩；budget、observation window、TSP layer和pooling是主要旋钮。
- **Evaluation Contract:** LLaMA/Mistral等 long-context models，在 LongBench/RULER等任务比较 full KV、SnapKV/AdaKV/HeadKV/GemFilter；报告 accuracy、prefill latency、throughput和memory。
- **Baselines / Ablations / Sensitivity / Overhead:** 核验不同 KV/hidden budgets、TSP layer、sequence length、task类别与baseline；选择开销和kernel shape受实现影响。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露模型、长度、budget与实验GPU/部分precision；结果多为单请求或受控batch，生产并发、P95/P99与mixed-length SLO不完整。
- **What the Evidence Actually Proves:** 作者设置中，中间层选择后同时压缩hidden compute和KV state，可比只在末端做KV pruning更直接降低prefill成本。
- **What It Does Not Prove:** 不证明对任意任务/模型无损，不证明attention score始终等同因果重要性，也不证明混合batch/continuous batching下收益线性保留。
- **Limitations / Threats to Validity:** task/layer sensitivity、早删不可恢复、position/relative attention语义、长尾query shift与作者benchmark范围；缺跨模型在线校准。
- **Trade-offs / New Failure Modes:** 降低TTFT/memory却引入selection false negative、filter-layer miscalibration、cache identity变化、kernel fragmentation与debug不可解释性。
- **Where the Previous Design Still Applies:** exact/full attention适合高风险或信息均匀prompt；KV-only pruning适合prefill不关键、engine侵入要小；retrieval/chunking适合可显式分段语料。
- **Evolution Relationship:** `Direct Evolution`：full prefill+full KV→post-prefill KV pruning→filter-layer token selection→hidden+KV co-compression。
- **ROADMAP Node:** `INFER-PREFILL`（Ch43）主 owner；handoff `INFER-KV-CACHE` Ch45、`INFER-PAGED-ATTENTION` Ch47、`INFER-SCHEDULING` Ch56。
- **Target and Adjacent Chapters Read:** 已核对 Ch42～47 与 Ch54～56 的 request state、prefill/decode、cache identity、memory和batching边界。
- **Existing Coverage:** Books 已覆盖 KV eviction/tiering；FastKV增加 prefill compute-domain shrink 分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；性能数字不脱离模型/GPU/length/budget与batch contract外推。
- **Open Questions:** continuous batching怎样组织不同压缩shape；selection metadata如何纳入prefix cache key；误删能否触发fallback；跨tenant fairness如何计费。

### vLLM 0.7.2

- **Candidate / Week / Score:** vLLM 0.7.2 / 2025-W06 / 27/30。
- **Source Family ID:** `vllm-0.7.2-runtime-state-and-extension-contract`。
- **Source Type:** official GitHub release + merged PRs + tagged code family。
- **First-public Date / Revision History:** release 2025-02-06；tag `v0.7.2` / commit `0408efc`；PRs在发布前合入，不作为重复事件。
- **Direct Primary Sources:** https://github.com/vllm-project/vllm/releases/tag/v0.7.2；https://github.com/vllm-project/vllm/pull/12621；https://github.com/vllm-project/vllm/pull/12368。
- **Related Primary Sources:** release-linked `#12608`、`#12676`、`#12637`、`#11330`、`#12785`、`#12727`；无法稳定读取的PR详情只保留release-level事实。
- **Access and Verification Status:** Full Source Review Complete；release、prefix-cache collision PR 与 structured-decoding thread-pool PR 已核验；部分linked PR页面访问不稳定，未据此扩写机制或性能结论。
- **Full-read Coverage:** 已读release全部 highlights/core/security/V1 changes，核验 cache hash 起点、Python 3.12 行为、thread-pool控制与batch边界；slot unification和256-byte alignment仅保留官方release事实。
- **Original Problem:** serving runtime同时承担模型扩展、request slot、prefix state、structured output与kernel布局；这些优化若没有明确identity/ownership合同，会让性能改动转化为错缓存、调度分裂或不可复现行为。
- **Why the Previous Design Was Reasonable:** 固定内置model implementation、串行logits processor与简单hash chain在模型集合小、batch低、单进程可信输入下易维护；prefill/decode分开slot也映射了不同执行阶段。
- **Changed Constraint:** backend覆盖扩大、高batch structured decoding、跨请求prefix reuse与V1统一scheduler使共享状态、并发和安全边界同时进入hot path。
- **Mechanism:** release引入Transformers backend入口；可配置thread pool跨batch sequences并行logits processors；prefix-cache hash chain不再以可预测常量起始；V1逐步统一prefill/decode slot allocation；部分kernel/layout优化保持为版本事实。
- **State Ownership:** scheduler拥有request/slot lifecycle；prefix cache拥有block identity及parent hash chain；logits processor线程池只拥有sequence-local处理任务；backend adapter拥有model compatibility边界。
- **Control Flow / Data Flow:** request→model/backend resolution→scheduler分配slot→prefix block lookup/hash validation→prefill/decode执行→batched logits交给可选线程池→约束后token返回；cache命中不得绕过content identity。
- **Implementation Details:** `VLLM_LOGITS_PROCESSOR_THREADS`控制跨sequence线程池；prefix hash从进程随机化字符串种子开始以提高主动碰撞难度，但仍非密码学无碰撞；release声明V1 slot统一、KV 256-byte alignment与compiled MoE path，未把release数字当通用benchmark。
- **Evaluation Contract:** release只给局部场景声明：DeepSeek layout/compiled MoE与high-batch structured decoding；没有统一披露model、GPU、precision、prompt/decode length、concurrency和SLO的完整横向合同。
- **Baselines / Ablations / Sensitivity / Overhead:** thread-pool收益依赖batch与processor成本；hash方案以安全/性能权衡说明而非benchmark；其他性能百分比缺完整复现实验，本审计不保留为通用结论。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** DeepSeek和high-batch场景有定性/局部数字；硬件、precision、长度、batch、并发与tail-latency未成套披露，均记 `Not Disclosed`。
- **What the Evidence Actually Proves:** 该release把extension、shared-cache identity、structured-output并发与scheduler slot作为同一runtime版本的显式工程问题；PR #12621具体证明非密码学hash起点也可能形成安全边界。
- **What It Does Not Prove:** 不证明Transformers backend与native implementation性能等价、不证明hash绝无碰撞、不证明线程越多越快，也不证明release中的吞吐百分比可跨模型/硬件复用。
- **Limitations / Threats to Validity:** release聚合多PR且评测合同不完整；部分linked PR读取受限；版本行为会继续演化，必须绑定tag；randomized hash提升主动碰撞门槛但不提供cryptographic guarantee。
- **Trade-offs / New Failure Modes:** 扩展性提高却扩大compatibility/test matrix；线程池可能带来GIL/oversubscription/ordering风险；cache identity加强增加hash成本；slot统一提高调度一致性但扩大共享allocator故障域。
- **Where the Previous Design Still Applies:** 低batch、简单processor可保持串行；安全敏感多租户可选更强digest；受支持native model path仍适合追求稳定性能；独立prefill/decode资源池在PD架构中仍成立。
- **Evolution Relationship:** `Layering / Dependency`：model-specific engine→backend extension contract；phase-local slots→统一request-state allocation；opportunistic prefix reuse→identity/security-aware shared state。
- **ROADMAP Node:** `INFER-VLLM`（Ch50）主 owner；handoff `INFER-CONTINUOUS-BATCHING` Ch46、`INFER-PAGED-ATTENTION` Ch47、`INFER-SCHEDULING` Ch56 与 `PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch46～52、Ch56 与 Ch72 的batch、cache、engine、scheduler和tenant boundary。
- **Existing Coverage:** Books 已覆盖vLLM request/KV lifecycle；本family增加cache identity和extension/concurrency合同，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；未写Books；未保留缺完整workload contract的43%/5%为通用事实。
- **Open Questions:** cryptographic cache key何时值得成本；thread-pool如何与engine线程/CPU affinity协调；统一slot在PD/disaggregated runtime中由谁拥有；backend fallback如何进入decision trace。

### SmolLM2 / Data-Centric Training of a Small Language Model

- **Candidate / Week / Score:** SmolLM2 / 2025-W06 / 27/30。
- **Source Family ID:** `smollm2-data-centric-small-lm-lifecycle`。
- **Source Type:** arXiv technical report + official datasets/model/code artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-02-04；后续revision与model cards属同family。
- **Direct Primary Sources:** https://arxiv.org/html/2502.02737v1；https://arxiv.org/abs/2502.02737；official Hugging Face SmolLM2/SmolTalk/FineMath/Stack-Edu artifacts linked by report。
- **Related Primary Sources:** Nanotron、Datatrove、LightEval用于training/data/evaluation实现；比较模型只定义baseline。
- **Access and Verification Status:** Full Source Review Complete；data construction、mixture stages、architecture/training、context extension、SFT/DPO、evaluation与appendices已核验。
- **Full-read Coverage:** 已读背景、FineMath/Stack-Edu构建与分类器、small-scale ablation、11T multi-stage mixture、2K→8K extension、base evaluation、SmolTalk synthesis/filtering、SFT/DPO、small variants与conclusion。
- **Original Problem:** 小模型容量有限，简单增加通用web tokens会被低质量和能力配比浪费；公开instruction数据又不能补齐数学、约束、重写和function calling缺口。
- **Why the Previous Design Was Reasonable:** 固定大规模混合减少pipeline复杂度；单阶段训练对较小token budget更稳定；复用公开SFT/DPO数据成本低且便于比较。
- **Changed Constraint:** 1.7B模型被过训练到约11T tokens，边际收益更多取决于数据筛选、阶段配比和能力target，而非只扩参数；部署又要求8K context和指令能力。
- **Mechanism:** 先用小规模消融筛选data sources，再按阶段观察能力缺口调整web/math/code/education比例；后期context extension与decay；post-training用合成+过滤+去重的SmolTalk做SFT，再以UltraFeedback做DPO。
- **State Ownership:** dataset manifest拥有source/filter/license/provenance；mixture schedule拥有阶段比例；checkpoint拥有model/optimizer/context状态；teacher/filter model拥有synthetic-label偏差；evaluation suite拥有能力反馈。
- **Control Flow / Data Flow:** raw corpora→educational/math classifiers与dedup→mixture experiments→四阶段pretraining/checkpoints→long-context extension→SmolTalk synthesis/filter→SFT→DPO→base/instruct evaluation反馈下一轮data choice。
- **Implementation Details:** 1.7B Llama2-like model、49,152 tokenizer、WSD schedule、256 H100、约11T tokens；训练分0–6T、6–8T、8–10T和10–11T decay；SFT 2 epochs/8K，DPO 2 epochs/1K。
- **Evaluation Contract:** 与Llama3.2-1B、Qwen2.5-1.5B等比较base/instruct benchmark；包含held-out MMLU-Pro/NQ/TriviaQA、math/code、HELMET/NIAH、IFEval/MT-Bench；数据和prompt protocol仍决定解释边界。
- **Baselines / Ablations / Sensitivity / Overhead:** 报告data source/mixture、question能力、context extension、SFT dataset与DPO preference dataset比较；stage 3出现未解释loss spike；未分离所有阶段的compute贡献。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1.7B、256 H100、11T tokens、2K→8K和部分optimizer/batch披露；precision、完整wall-clock/energy、serving concurrency与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者1.7B训练合同内，小规模data ablation、分阶段mixture和targeted post-training共同获得竞争力；模型容量与数据质量/配比是耦合系统。
- **What It Does Not Prove:** 不证明11T tokens或某一数据集单独造成收益、不证明小模型普遍优于较大模型，也不证明teacher生成和benchmark过滤消除了contamination/bias。
- **Limitations / Threats to Validity:** 多项改动同时发生、训练昂贵难完全复现、teacher/filter依赖、benchmark overlap风险、未解释loss spike与不完整precision/energy披露。
- **Trade-offs / New Failure Modes:** data curation提高sample utility，却新增classifier bias、mixture overfitting、teacher monoculture、provenance复杂度与多阶段checkpoint/rollback成本；过训练降低模型体积但增加一次性compute。
- **Where the Previous Design Still Applies:** 单阶段高质量混合适合更小模型/较短预算；大模型在复杂能力仍有headroom；公开通用SFT适合低成本baseline；固定2K context适合edge memory约束。
- **Evolution Relationship:** `Direct Evolution`：scale generic tokens→quality filtering→capability-aware staged mixture→context extension→targeted SFT/DPO；不是“data取代architecture”。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-PRETRAINING` Ch28、`TRAIN-SFT` Ch29、`TRAIN-DPO` Ch34、`MODEL-LONG-CONTEXT` Ch22与`TRAIN-CHECKPOINT` Ch35。
- **Target and Adjacent Chapters Read:** 已核对 Ch22、Ch27～29、Ch34～35 的data/objective/context/checkpoint边界。
- **Existing Coverage:** Books已有data quality和mixture观点；本family提供“small ablation→stage feedback→artifact lineage”的完整训练闭环，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；不复制孤立benchmark排名，不修改Books。
- **Open Questions:** mixture变化怎样归因；teacher/filter版本如何进入dataset lineage；loss spike怎样复盘；overtraining与端侧lifecycle总成本如何比较。

### LIMO / Less Is More for Reasoning

- **Candidate / Week / Score:** LIMO / 2025-W06 / 25/30。
- **Source Family ID:** `limo-curated-hard-example-reasoning-sft`。
- **Source Type:** arXiv v1 paper + official dataset/model artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-05；后续revision同family。
- **Direct Primary Sources:** https://arxiv.org/html/2502.03387v1；https://arxiv.org/abs/2502.03387。
- **Related Primary Sources:** Qwen2.5-32B-Instruct backbone、DeepSeek-R1 solution teacher与OpenThoughts/NuminaMath baselines定义依赖，不把teacher能力归给SFT机制。
- **Access and Verification Status:** Full Source Review Complete；selection pipeline、training、same-backbone baselines、question/solution/backbone/scale ablations与limitations已核验。
- **Full-read Coverage:** 已读Introduction/related work、817样本构建、difficulty与diversity filtering、solution来源/人工检查、training/evaluation、data quantity、question/solution quality、backbone与parameter-scale analyses、conclusion。
- **Original Problem:** reasoning SFT通常把数据量当主旋钮，但大量容易、重复或低质量链可能只教格式，无法激活base model已有的数学知识和长推理组织能力。
- **Why the Previous Design Was Reasonable:** 大数据覆盖长尾任务、降低人工选择偏差，并适合能力不足的base model；简单随机采样便于规模化和复现。
- **Changed Constraint:** 强base model已含较多数学先验，训练目标转为用少量高难度、高质量、可验证轨迹触发和组织已有知识，data utility而非count成为瓶颈。
- **Mechanism:** 由大候选池经模型成功率筛难度、embedding/类别保diversity，再从official/human/strong-model solutions中做正确性与组织质量筛选；以817条样本对Qwen2.5-32B-Instruct SFT。
- **State Ownership:** candidate pool拥有问题分布；difficulty filters拥有selection policy；teacher/human solution拥有reasoning trajectory；base checkpoint拥有latent prerequisite knowledge；verifier与benchmark拥有可观测正确性。
- **Control Flow / Data Flow:** problem pool→多模型difficulty filtering→diversity sampling→solution generation/official answers→correctness与人工quality filtering→SFT→MATH/AIME/AMC/Olympiad evaluation→quality/backbone/scale ablation。
- **Implementation Details:** 817 training examples；主要backbone Qwen2.5-32B-Instruct；与OpenThoughts 114K、NuminaMath100K等同backbone SFT比较；另用不同难度500题、solution quality和Qwen1.5/2.5及3B–72B系列分析。
- **Evaluation Contract:** 数学竞赛benchmarks，模型采样与pass@k/majority等协议按论文；作者数字只绑定Qwen-family、curated math data和特定inference设置，不代表开放域reasoning。
- **Baselines / Ablations / Sensitivity / Overhead:** 同backbone大数据baseline、data-size、question difficulty、solution quality、pretrained backbone与parameter size均被检查；selection/teacher/人工筛选成本没有计入“817样本”的表面规模。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型、样本和训练超参部分披露；训练/推理GPU、precision、完整length distribution、并发与SLO不完整，记 `Not Disclosed`。
- **What the Evidence Actually Proves:** 对作者选择的强Qwen base和math benchmarks，少量高难度高质量轨迹可超过若干大规模SFT baselines；data utility依赖base knowledge、question难度和solution结构。
- **What It Does Not Prove:** 不证明817是普适阈值、不证明少数据优于多样高质量大数据、不证明能力来自SFT而非base/teacher选择，也不证明开放域、代码或安全任务同样成立。
- **Limitations / Threats to Validity:** 单一模型家族和数学域、teacher/selection bias、benchmark contamination、difficulty由现有模型定义、人工筛选不可完全复现；data construction总成本被sample count掩盖。
- **Trade-offs / New Failure Modes:** 降低optimizer steps和存储，却增加curation/teacher/verifier成本、覆盖不足、hard-example overfit、风格模仿与selection feedback loop。
- **Where the Previous Design Still Applies:** 弱base或新领域仍需要大规模覆盖；多任务/开放域需广泛data；可审计安全策略需要明确负例与policy coverage，而非只选难题。
- **Evolution Relationship:** `Alternative Branch`：quantity-first SFT→quality filtering→difficulty/diversity-aware curation→base-capability-conditioned minimal SFT；新分支不否定规模化数据。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；handoff `TRAIN-DATA` Ch27、`TRAIN-PRETRAINING` Ch28与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～31 与 Ch66 的data、base knowledge、SFT objective、reward/evaluation边界。
- **Existing Coverage:** Books已强调quality over raw count；本family补充base capability × difficulty × solution quality的条件化机制，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；作者benchmark只作受限证据，不写Books。
- **Open Questions:** selection成本怎样计入sample efficiency；跨teacher/backbone是否复现；难度filter会不会排除新型推理；如何检测benchmark或solution contamination。

### Scaling up Test-Time Compute with Latent Reasoning / Recurrent Depth

- **Candidate / Week / Score:** Latent Reasoning Test-Time Scaling / 2025-W06 / 26/30。
- **Source Family ID:** `recurrent-depth-latent-test-time-compute`。
- **Source Type:** arXiv v1 research paper + author model/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-07；后续revision同family。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05171v1；https://arxiv.org/abs/2502.05171。
- **Related Primary Sources:** Universal/looped Transformers、deep equilibrium、continuous CoT、early exit与speculative decoding仅定义前代/替代分支。
- **Access and Verification Status:** Full Source Review Complete；architecture/objective、stability failures、800B-token training、scaling evaluation、adaptive exit、KV sharing、continuous state与self-speculation已核验。
- **Full-read Coverage:** 已读Introduction/related work、prelude-recurrent-core-coda结构、randomized recurrence与input injection、training instability、model/data/compute、scaling/evaluation、zero-shot runtime interventions、mechanistic analysis、appendix相关实验。
- **Original Problem:** 固定depth Transformer为所有token/问题支付相同层数；verbal CoT把额外compute绑定到可见token，增加sequence/KV成本并暴露/固化reasoning trace。
- **Why the Previous Design Was Reasonable:** 固定depth易训练、并行和编译，KV每层结构规则；显式CoT可监督、可审计并复用标准decoder runtime。
- **Changed Constraint:** 不同token与问题难度差异扩大，希望在不生成更多reasoning tokens、也不训练独立draft模型的情况下按需扩test-time compute。
- **Mechanism:** prelude后反复执行共享权重recurrent core，训练时随机unroll并每步注入input；coda输出token。推理可按successive-state KL早停、限制循环KV budget、复用前token latent state，或用少iteration draft、多iteration verify。
- **State Ownership:** recurrent hidden state拥有token内部latent computation；shared K/V projections定义跨recurrence cache兼容性；exit policy拥有停止决定；verifier recurrence拥有accepted token truth；sequence KV仍拥有跨token历史。
- **Control Flow / Data Flow:** token/input→prelude→随机initial state+input injection→recurrent core多步→KL/预算决定continue/exit→coda logits；self-speculation先浅迭代draft N tokens，再深迭代verify并复用已算state。
- **Implementation Details:** 3.5B recurrent-depth model、约800B tokens；sandwich block和较低LR用于避免norm instability、state collapse及模型忽略recurrent state；KV可循环覆盖固定recurrence slots。
- **Evaluation Contract:** math/code/academic benchmarks与MT-Bench等，比较固定参数/compute模型并扫recurrence depth；训练compute接近更大固定模型，推理最多对照约50B等效compute；作者设置不是serving SLO实验。
- **Baselines / Ablations / Sensitivity / Overhead:** 检查recurrence steps、model scale、training stability、early-exit threshold、KV budget、warm-start与fixed-depth baselines；早停/自推测多为preliminary或zero-shot intervention。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 3.5B/800B tokens和部分训练compute披露；完整硬件拓扑、precision、batch、并发、P95/P99与energy `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者模型与任务中，训练好的recurrent depth可在测试时通过增加迭代改善部分能力，并自然支持per-token早停、共享/有界KV和self-speculative分支。
- **What It Does Not Prove:** 不证明latent iteration等同可靠推理、不证明更多steps单调改善、不证明zero-shot exit/speculation在生产吞吐或安全任务稳定，也不证明优于同总训练/推理成本的大固定模型。
- **Limitations / Threats to Validity:** 单一中等规模模型、昂贵预训练、norm/collapse failure、作者benchmark、runtime/kernel未成熟；latent轨迹难审计，KL convergence不等同语义正确。
- **Trade-offs / New Failure Modes:** adaptive compute减少易token浪费，却引入不规则iteration、batch divergence、exit miscalibration、circular KV overwrite、latent state leakage和深迭代tail latency。
- **Where the Previous Design Still Applies:** 固定depth适合规则batch和compiler优化；显式CoT适合需要可审计reasoning；外部draft适合现有checkpoint无须重训；固定KV适合严格correctness。
- **Evolution Relationship:** `Alternative Branch`：fixed depth→verbalized test-time tokens / early-exit heads→pretrained recurrent depth→adaptive latent iterations+shared state；是并行分支而非替代链。
- **ROADMAP Node:** `MODEL-TRANSFORMER-LAYER`（Ch17）主 owner；handoff `MODEL-SAMPLING` Ch20、`INFER-KV-CACHE` Ch45、`INFER-SPECULATIVE-DECODING` Ch48与`INFER-SCHEDULING` Ch56。
- **Target and Adjacent Chapters Read:** 已核对 Ch16～20、Ch44～48与Ch56的layer depth、token state、cache、verification和batch scheduling边界。
- **Existing Coverage:** Books覆盖固定depth、early exit和speculation；本family增加从架构训练到runtime policy的recurrent-depth分支，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；不把qualitative latent trajectories当作因果机制证明。
- **Open Questions:** exit policy如何校准到quality/SLO；不同recurrence depth如何continuous batch；循环KV覆盖如何审计；latent reasoning在安全评测中如何提供可执行证据。

### Fast Video Generation with Sliding Tile Attention

- **Candidate / Week / Score:** Sliding Tile Attention / 2025-W06 / 27/30。
- **Source Family ID:** `sliding-tile-attention-video-dit-kernel-codesign`。
- **Source Type:** arXiv paper + official FastVideo code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-06；v2 2025-05-26；v3 2025-06-04。当前HTML为v3，W06 event按v1归属，后续revision只用于机制核验。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04507；https://arxiv.org/html/2502.04507；https://github.com/hao-ai-lab/FastVideo。
- **Related Primary Sources:** HunyuanVideo、FlashAttention-3、ThunderKittens、FlexAttention、CLEAR/NATTEN/Swin与Delta-DiT定义model/kernel baselines。
- **Access and Verification Status:** Full Source Review Complete；method、mask geometry、kernel pipeline、training-free search、finetuning、evaluation、appendices与revision history已核验。
- **Full-read Coverage:** 已读3D attention瓶颈、SWA mixed-block问题、STA公式/算法、producer-consumer kernel、head-wise window search、distillation finetune、kernel/E2E/human evaluation、baselines与future work。
- **Original Problem:** Video DiT把时空tokens展平成超长序列，full attention二次复杂度主导延迟；普通3D sliding-window虽降FLOPs，却因mixed blocks和mask计算无法转化为wall-clock收益。
- **Why the Previous Design Was Reasonable:** full 3D attention表达全局时空交互且易映射dense kernels；token-wise SWA保持局部语义精确，早期video models规模较小时实现简单。
- **Changed Constraint:** 720P/5秒视频约115K latent tokens，attention成为端到端主瓶颈；硬件执行效率而非理论稀疏率成为系统约束。
- **Mechanism:** 令同一3D tile内queries共享key-tile窗口，使attention矩阵只有dense/empty blocks；producer warpgroup异步选择并加载KV，consumer只算dense blocks；每head/step窗口由少量prompts profiling或稀疏finetune确定。
- **State Ownership:** tile layout拥有token→block identity；mask profile拥有layer/head/timestep窗口；producer拥有KV movement与sparse selection；consumer拥有dense math；teacher full attention提供finetune target。
- **Control Flow / Data Flow:** video latent→tile reorder→profile lookup→producer从HBM加载选中KV至SRAM circular buffer→consumer dense attention→diffusion step；可先full attention若干steps再切STA。
- **Implementation Details:** tile size对齐FlashAttention block；ThunderKittens/FA3 producer-consumer实现；16 prompts做training-free mask search；更高稀疏度时以attention/final/output losses finetune，论文披露8×H100约8小时。
- **Evaluation Contract:** HunyuanVideo 117 frames、1280×768、latent(30,48,80)、bf16、head dim128、24 heads，并在H100测kernel/E2E latency；质量含human eval、VBench、SSIM、PSNR、CD-FVD；另测FLUX/Wan revision。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较FA2/FA3、CLEAR、NATTEN、Swin、Delta-DiT；检查sparsity、window/head specialization、training-free与finetune；revision间E2E数字变化，必须绑定版本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100、HunyuanVideo、bf16、115.2K seq、单生成latency较完整；batch/concurrency、P95/P99、energy与多租户SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者video/image DiT合同中，按kernel tile重构局部稀疏能消除mixed-block浪费，使部分理论稀疏转化为实际延迟下降。
- **What It Does Not Prove:** 不证明所有heads/prompts长期局部、不证明质量完全无损、不证明对LLM causal attention或mixed-batch同样成立，也不证明作者峰值倍数跨GPU/版本稳定。
- **Limitations / Threats to Validity:** 单一主video model、16-prompt profile、human/automatic quality局限、window/tile整除约束、v1-v3数字变化和kernel portability风险。
- **Trade-offs / New Failure Modes:** 更高MFU换来tile granularity误差、profile drift、边界artifact、global dependency丢失、specialized kernel维护与不规则shape fallback。
- **Where the Previous Design Still Applies:** full attention适合短序列/全局依赖/正确性优先；普通SWA适合已有高效1D kernel；spatial-temporal factorization或step distillation可在不同bottleneck下更优。
- **Evolution Relationship:** `Direct Evolution`：dense full 3D→token-wise sparse mask→tile-aligned block sparsity→profile/finetune specialization；与caching/step reduction是`Layering / Dependency`。
- **ROADMAP Node:** `INFER-TENSORRT-LLM`（Ch49，execution-plan owner）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24、`MODEL-SELF-ATTENTION` Ch14与`INFER-GPU-MEMORY` Ch54。
- **Target and Adjacent Chapters Read:** 已核对 Ch14、Ch24、Ch42～50与Ch54的attention semantics、generation workload、kernel plan和memory boundary。
- **Existing Coverage:** Books已覆盖kernel/layout co-design；STA提供3D sparse geometry→dense block execution的受限案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；纠正first-public为2025-02-06，不把v3数字回写成v1当日事实。
- **Open Questions:** profile如何在线失效；tile identity怎样进入compile cache；跨GPU架构如何fallback；局部窗口与global safety/content consistency如何联合验证。

### QuEST / Stable Training with Low-bit Weights and Activations

- **Candidate / Week / Score:** QuEST / 2025-W06 / 27/30。
- **Source Family ID:** `quest-low-bit-qat-distribution-trust-gradient`。
- **Source Type:** arXiv paper + official code/kernel artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-07；v2 2025-06-10。当前HTML为v2，后续kernel/revision证据不改变W06 owner。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.05003；https://arxiv.org/html/2502.05003；paper-linked official code。
- **Related Primary Sources:** STE/LSQ、Hadamard rotation、PTQ baselines和Blackwell low-precision support定义前代与hardware assumption。
- **Access and Verification Status:** Full Source Review Complete；distribution fitting、trust estimator、training algorithms、scaling laws、precision search、formats/sparsity、GPU kernels、runtime与appendices已核验。
- **Full-read Coverage:** 已读QAT背景、MSE-optimal quantization、Hadamard normalization、gradient error分析/trust mask、W1A1～W4A4 experiments、scaling fits、overtraining regime、kernel pipeline与future work。
- **Original Problem:** PTQ在低bit weights+activations精度下降；传统QAT用STE传播被量化噪声污染的梯度，极低bit训练不稳定，且理论bit savings未必有可执行kernel。
- **Why the Previous Design Was Reasonable:** BF16训练梯度可信且工具链成熟；PTQ不需重训；STE简单低开销；8-bit在早期hardware/accuracy下是稳健折衷。
- **Changed Constraint:** deployment成本推动W4A4甚至更低precision，且小模型被overtrain后runtime而非训练compute成为目标；需要训练算法与integer kernel共同闭合。
- **Mechanism:** Hadamard transform使weights/activations更接近可拟合分布，按MSE选scale；只信任quantization error低于半bin宽的梯度，用trust mask过滤高误差分量，再inverse transform把梯度扩散回原域。
- **State Ownership:** FP master weights拥有优化状态；quantized forward tensors拥有执行状态；scale/format和trust mask拥有projection/gradient contract；kernel拥有packing/dequantization layout。
- **Control Flow / Data Flow:** BF tensors→Hadamard→MSE-optimal scale/quantize/pack→low-bit matmul→BF output；backward在quantized state上算16-bit gradients→trust mask→inverse Hadamard→更新master weights。
- **Implementation Details:** 每linear forward两次HT、backward两次IHT；支持INT1–4/FP4/sparsity；runtime由Hadamard kernel、Triton quant-pack、CUTLASS INT4 GEMM+register dequant与CUDA Graph组成。
- **Evaluation Contract:** Llama-family 30M–1.6B、C4、约100 tokens/parameter及overtraining分析，比较BF16与QAT methods；RTX4090 per-layer kernel包含quant/dequant和Hadamard overhead；7B runtime部分是proportional shape而非已训练7B。
- **Baselines / Ablations / Sensitivity / Overhead:** bitwidth、Hadamard/trust estimator、weight-only、FP4/sparsity、scaling law与training stability均有分析；training仍用16-bit backward，低bit不等于end-to-end低bit训练成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 30M–1.6B训练、W1A1–W4A4、RTX4090 layer kernels披露；完整training cluster、sequence/batch、serving concurrency与SLO不完整。
- **What the Evidence Actually Proves:** 在作者模型/数据尺度中，distribution fitting+trust gradient可稳定极低bit QAT，W4A4呈更优accuracy-size/runtime frontier，并有可执行INT4 kernel原型。
- **What It Does Not Prove:** 不证明1-bit模型部署最优、不证明4-bit对所有architecture/data/hardware Pareto最优，也不证明7B/更大模型或end-to-end serving获得线性speedup。
- **Limitations / Threats to Validity:** 最大训练规模1.6B、scaling extrapolation、C4/Llama单族、hardware-specific kernel、backward仍高精度、later v2 revision与真实fleet workload缺失。
- **Trade-offs / New Failure Modes:** 低bit降低memory/MatMul成本，却增加transform/packing、scale/mask state、kernel依赖、gradient starvation风险与格式迁移成本；极低bit需更多data/parameters弥补有效容量。
- **Where the Previous Design Still Applies:** BF16适合训练稳定/研究迭代；PTQ适合已有checkpoint；8-bit适合广泛hardware；weight-only适合activation outlier强或kernel不足的场景。
- **Evolution Relationship:** `Direct Evolution`：BF training+PTQ→STE QAT→distribution-normalized QAT→trust-aware gradient→training/runtime co-designed low-bit artifact。
- **ROADMAP Node:** `TRAIN-PRETRAINING`（Ch28）主 owner；handoff `TRAIN-CHECKPOINT` Ch35、`INFER-TENSORRT-LLM` Ch49与`INFER-GPU-MEMORY` Ch54。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～28、Ch35、Ch49～50与Ch54的precision、artifact、kernel和runtime boundary。
- **Existing Coverage:** Books已有quantization分支；QuEST补充QAT gradient trust与hardware-executable artifact链，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；v2 kernel结果与7B extrapolation均明确版本/证据边界。
- **Open Questions:** trust mask如何跨distributed shards复现；scale/mask是否进入checkpoint schema；larger MoE/long-context是否保持scaling；fleet真实energy/latency如何验证。

### BOLT / Bootstrap Long Chain-of-Thought

- **Candidate / Week / Score:** BOLT / 2025-W06 / 26/30。
- **Source Family ID:** `bolt-bootstrap-long-cot-sft-online-dpo`。
- **Source Type:** arXiv v1 paper + official model/data artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-06；无后续arXiv revision。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.03860；https://arxiv.org/html/2502.03860。
- **Related Primary Sources:** Llama-3.1-70B-Instruct bootstrapping model、ORMs、TRL/DPO与Arena-Hard/MT-Bench/WildBench等定义teacher/reward/evaluation依赖。
- **Access and Verification Status:** Full Source Review Complete；bootstrapping、query mixture、generation/filtering、SFT、online DPO、training/evaluation、reward/backbone/algorithm ablations与appendix已核验。
- **Full-read Coverage:** 已读problem/related work、10-example ICL bootstrapping、domain mixture、ORM filtering、SFT、online sampling/pair construction/DPO、7B/8B/70B setup、trajectory、reward model/initial model/algorithm ablations。
- **Original Problem:** LongCoT复制常依赖o1-like teacher或昂贵人工轨迹，域又集中math/code；但普通instruct model已有部分规划/反思能力，缺少稳定格式与在线改进闭环。
- **Why the Previous Design Was Reasonable:** 强teacher distillation直接提供高质量long traces；ShortCoT成本低、易评测；大SFT数据在无可靠verifier时更可控。
- **Changed Constraint:** 希望不依赖专有LongCoT teacher，用开放instruct model和少量手工示例启动跨域长推理，并通过模型自身sampling扩展。
- **Mechanism:** 用10条long-form ICL示例让强ShortCoT model生成候选；按格式和outcome reward过滤；对目标model做LongCoT SFT；再在线采样responses，用reward model构造preference pairs做DPO迭代。
- **State Ownership:** seed examples拥有format prior；bootstrap model拥有生成偏差；ORM拥有external-solution ranking；SFT checkpoint拥有LongCoT format；online policy拥有当前sampling distribution。
- **Control Flow / Data Flow:** mixed queries→ICL bootstrap多responses→format/ORM filter→LongCoT SFT→online rollouts→ORM ranking/pairs→DPO update→下一轮policy。
- **Implementation Details:** bootstrap使用Llama-3.1-70B-Instruct；目标Mistral-7B/Llama-8B/70B；DPO基于TRL；7B/8B约单8×H100 14小时，70B约8节点20小时。
- **Evaluation Contract:** Arena-Hard-SC、MT-Bench、WildBench、ZebraLogic、MATH500等；比较initial、SFT、online stages和reward models；judge/reward与response length会影响结果。
- **Baselines / Ablations / Sensitivity / Overhead:** reward model、initial backbone、online algorithms与stage trajectory有消融；bootstrapping/ORM inference成本和长output serving成本不能从训练样本数中消失。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model scale/GPU hours部分披露；precision、完整token lengths、sampling并发、training energy和serving SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 作者模型/benchmark下，强ShortCoT可经少量format seeds产生可训练LongCoT data，SFT后再用online preference training继续改进。
- **What It Does Not Prove:** 不证明没有distillation依赖——bootstrap/ORM仍是teacher；不证明长输出本身等同reasoning或跨域可靠，也不证明DPO优于所有online RL。
- **Limitations / Threats to Validity:** reward/judge bias、length/style confound、bootstrap model门槛、chain correctness不可直接验证、benchmark contamination与多阶段归因困难。
- **Trade-offs / New Failure Modes:** 降低专有teacher依赖，却新增seed/ORM monoculture、verbose reward hacking、错误反思、sampling成本、policy-reward co-drift和长序列latency。
- **Where the Previous Design Still Applies:** 专有teacher适合追求最高质量；ShortCoT适合低延迟；domain verifier可靠时RL可替代ORM pair；人工轨迹适合安全关键可审计步骤。
- **Evolution Relationship:** `Alternative Branch`：LongCoT teacher distillation→few-shot self-bootstrap→SFT format acquisition→online preference refinement；不是“无teacher”。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；handoff `TRAIN-DPO` Ch34、`MODEL-SAMPLING` Ch20与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch20、Ch27～34与Ch66的data generation、SFT、preference、reward与judge boundary。
- **Existing Coverage:** Books覆盖SFT→preference branch；BOLT提供bootstrap lineage和hidden teacher costs案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；“without distillation”按论文机制重新限定，不作字面无teacher结论。
- **Open Questions:** internal thoughts如何验证；ORM/seed versions怎样进入dataset lineage；verbosity和correctness如何解耦；online rounds何时停止/rollback。

### Satori / Chain-of-Action-Thought and Restart-and-Explore

- **Candidate / Week / Score:** Satori / 2025-W06 / 25/30。
- **Source Family ID:** `satori-coat-restart-explore-reasoning-rl`。
- **Source Type:** arXiv paper + official open data/model/code family。
- **First-public Date / Revision History:** arXiv v1 2025-02-04；v2 2025-06-02；v3 2025-06-16。当前HTML为v3，event归W06且revision不重复计分。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.02508；https://arxiv.org/html/2502.02508。
- **Related Primary Sources:** Qwen2.5-Math-7B base、PPO、Go-Explore、ORM与公开artifacts定义依赖。
- **Access and Verification Status:** Full Source Review Complete；COAT、format tuning、RAE、reward design、iterative RL、evaluation、ablation、data synthesis与appendices已核验。
- **Full-read Coverage:** 已读search/reasoning背景、meta-action representation、10K format tuning、positive/negative restart buffers、PPO/bonuses/ORM、300K RL、round-2、math/OOD tests、reflection/RAE/preference ablations。
- **Original Problem:** external verifier+multi-sample search成本高；单模型CoT常只连续展开，遇到早期错误难返回中间状态，稀疏终局奖励又让长horizon RL低效。
- **Why the Previous Design Was Reasonable:** best-of-N/tree search无需改变model；普通CoT兼容decoder；从prompt重新采样状态简单且避免错误prefix污染。
- **Changed Constraint:** 希望把continue/reflect/restart/explore动作内化到7B model，并从失败/成功partial trajectories继续学习，减少每次从根重算。
- **Mechanism:** 用special meta-action tokens把reasoning写成COAT；小规模format tuning教语法；RAE从正负轨迹随机回退并追加reflect token形成initial-state buffer；PPO结合终局正确性、reflection bonus与ORM preference bonus迭代更新。
- **State Ownership:** text trajectory拥有可见reasoning state；positive/negative restart buffers拥有partial-state provenance；policy拥有action distribution；rule verifier/ORM拥有reward；meta tokens定义control action。
- **Control Flow / Data Flow:** problem→format-tuned COAT rollout→correct/incorrect split→random backtrack+reflect→restart buffer→PPO rollout→rule/reflection/preference rewards→policy update→round-2再生成state。
- **Implementation Details:** Qwen2.5-Math-7B base；10K format data、300K RL data；从correct/incorrect trajectories采样backtrack states；正轨改错受罚、负轨纠错获bonus。
- **Evaluation Contract:** zero-shot pass@1 math benchmarks与BGQA/CRUX/StrategyQA/TableBench/MMLU-Pro STEM；同base Qwen instruct、其他模型和large-FT ablation；结果绑定作者prompt/answer verifier。
- **Baselines / Ablations / Sensitivity / Overhead:** COAT vs CoT、reflection bonus、RAE、preference bonus、offline/online buffers、iterative rounds和300K FT vs RL均检查；生成restart数据和ORM成本未被简单样本数覆盖。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B/data规模和训练配方部分披露；完整硬件、precision、trajectory length、rollout并发、wall-clock与serving SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数学训练和有限OOD benchmarks中，显式meta-actions、restart-state distribution与RL组合优于若干同base/SFT baselines，并能从partial failure继续探索。
- **What It Does Not Prove:** 不证明模型真正执行可靠search、不证明self-correction在无verifier开放域成立，也不证明RL单独造成全部收益或部署时无需外部验证。
- **Limitations / Threats to Validity:** math-centric verifier、visible trace真实性、reward hacking、special-token format依赖、OOD benchmark有限、later revision bleed与restart buffer distribution偏差。
- **Trade-offs / New Failure Modes:** 减少root restart浪费，却增加buffer provenance、错误prefix放大、reflection loop、reward-model依赖、long-output latency与不可见state coverage gap。
- **Where the Previous Design Still Applies:** external search适合无需重训和强verifier任务；plain CoT适合简单问题；从root重启适合prefix已污染；人工可审计workflow适合安全关键操作。
- **Evolution Relationship:** `Direct Evolution`：linear CoT→explicit meta-actions→partial-state restart→rewarded self-correction→iterative state redistribution。
- **ROADMAP Node:** `TRAIN-PPO`（Ch32）主 owner；handoff `TRAIN-RLHF` Ch31、`TRAIN-GRPO` Ch33、`AGENT-PLANNING` Ch79与`AGENT-REFLECTION` Ch80。
- **Target and Adjacent Chapters Read:** 已核对 Ch31～34、Ch79～80与Ch66的RL state、reward、planning/reflect和evaluation boundary。
- **Existing Coverage:** Books已有reflection与reasoning RL分支；Satori增加restart-state ownership和reward组合案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；不把latent intent或作者OOD结果外推成general reasoning。
- **Open Questions:** restart prefix如何版本化/去毒；reflection bonus怎样避免loop；ORM drift如何监控；visible COAT与实际causal computation如何区分。

### QLASS / Q-Guided Language Agent Stepwise Search

- **Candidate / Week / Score:** QLASS / 2025-W06 / 26/30。
- **Source Family ID:** `qlass-agent-exploration-tree-q-guided-inference`。
- **Source Type:** arXiv v1 paper + official code/data commitment。
- **First-public Date / Revision History:** arXiv v1 2025-02-04；无后续revision。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.02584；https://arxiv.org/html/2502.02584。
- **Related Primary Sources:** ReAct、ETO、PPO、RFT、Best-of-N、WebShop/ALFWorld/SciWorld定义policy、training和environment baselines。
- **Access and Verification Status:** Full Source Review Complete；behavior cloning、tree construction、Q update/distillation、Q-guided decoding、evaluation、fewer-label/base-policy ablations与appendix已核验。
- **Full-read Coverage:** 已读agent/process-reward背景、Q-learning formalization、pipeline algorithms、state/action/tree definitions、zero-reward pruning、QNet training/generation、datasets/baselines/budget、ablations和discussion。
- **Original Problem:** interactive agent只在trajectory末端获reward，trajectory-level preference无法告诉哪个action破坏长期成功；直接language-action Q-learning又面临巨大action space和样本低效。
- **Why the Previous Design Was Reasonable:** behavior cloning稳定复用expert traces；outcome reward最容易从environment获得；Best-of-N/trajectory DPO无需学习step value。
- **Changed Constraint:** ALFWorld/SciWorld等长interaction中需要在每一步考虑未来value，同时保持有限environment/search budget和较少人工标注。
- **Mechanism:** 先behavior cloning；用policy在同一task root构建exploration tree，零终局reward分支停止扩展；从叶到根递归备份Q-values形成step supervision；训练QNet并在每步对候选actions评分引导generation。
- **State Ownership:** environment拥有observation/terminal reward；tree node拥有history/state/action/children/Q；policy生成候选；QNet拥有distilled long-term value；expert data提供initial behavior。
- **Control Flow / Data Flow:** expert trajectories→SFT policy→environment rollouts/tree→terminal reward backup→state-action-Q dataset→QNet→test-time candidate actions→Q-guided choice→new observation循环。
- **Implementation Details:** base policy/QNet主要为Llama-2-7B-Chat；WebShop 1,938、SciWorld 1,483、ALFWorld 3,321 train trajectories；同search budget比较，Q-guided decoding增加多candidate scoring。
- **Evaluation Contract:** three fixed simulators、seen/unseen splits、平均terminal reward、one-shot evaluation；4/8 A6000，WebShop约1–2天、其他4–5天；temperature在methods间不完全相同。
- **Baselines / Ablations / Sensitivity / Overhead:** SFT、RFT、PPO、Best-of-N、ETO与closed models；减少annotations和不同base policy有实验；tree construction/QNet inference/environment calls是额外成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B、4/8 A6000、dataset turns和days披露；precision、parallel environment count、token lengths、online latency与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在三个静态interactive benchmarks与作者search budget内，从exploration tree蒸馏step Q-value可比trajectory-only baselines改善terminal reward，并在较少annotation下保留部分效果。
- **What It Does Not Prove:** 不证明QNet估计真实最优Q、不证明开放web或nonstationary tools稳定，也不证明额外tree/environment成本小于收益或Q-guided action可安全执行。
- **Limitations / Threats to Validity:** simulator determinism、terminal reward稀疏/可能错、policy-induced tree coverage、max-backup overestimation、temperature不一致、7B单族和安全/rollback未评估。
- **Trade-offs / New Failure Modes:** step guidance改善credit assignment，却新增QNet drift、tree coverage bias、value overestimation、candidate latency、environment cost与错误高Q action放大。
- **Where the Previous Design Still Applies:** SFT适合短任务/高质量expert；trajectory DPO适合无需step annotation；Best-of-N适合可并行且oracle可靠；rule workflow适合高风险动作。
- **Evolution Relationship:** `Direct Evolution`：outcome-only behavior cloning→trajectory self-improvement→exploration-tree value backup→stepwise Q-guided inference。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79）主 owner；handoff `AGENT-WORKFLOW` Ch81、`AGENT-REFLECTION` Ch80、`PLATFORM-EVALUATION-SYSTEM` Ch66与`TRAIN-RLHF` Ch31。
- **Target and Adjacent Chapters Read:** 已核对 Ch76～81、Ch31与Ch66的信息/动作state、workflow、reward与evaluation boundary。
- **Existing Coverage:** Books已有planning/search/value boundary；QLASS补充exploration-tree→QNet→runtime decision链，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；不把simulator benchmark写成production agent autonomy。
- **Open Questions:** QNet/observer版本怎样进入decision trace；tool failure和cost如何进Q backup；错误action如何rollback；nonstationary environment下何时重建tree。

### On-device Sora / Training-Free Mobile Video Diffusion Runtime

- **Candidate / Week / Score:** On-device Sora / 2025-W06 / 27/30。
- **Source Family ID:** `on-device-sora-mobile-video-diffusion-runtime`。
- **Source Type:** arXiv v1 paper + author repository + CC BY full-text mirror used for access recovery。
- **First-public Date / Revision History:** arXiv v1 2025-02-05；v2 2025-03-31并出现新arXiv entry/title variant。W06以v1 identity为owner，后续revision不重复计分。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04363；https://github.com/eai-lab/On-device-Sora。
- **Related Primary Sources:** CC BY v1 full-text copy at https://www.researchgate.net/publication/388848174_On-device_Sora_Enabling_Diffusion-Based_Text-to-Video_Generation_for_Mobile_Devices 用于恢复arXiv PDF/HTML访问；Open-Sora/CoreML定义backbone/runtime依赖。
- **Access and Verification Status:** Full Source Review Complete；arXiv identity/revision、v1 full text、official code layout、method、implementation、evaluation、ablation与limitations已核验；记录arXiv HTML错页异常。
- **Full-read Coverage:** 已读mobile constraints、Open-Sora pipeline、LPL derivation、TDTM merge/unmerge、CI-DL overlap/cache model、CoreML conversion、iPhone/A6000 evaluation、VBench、component ablations与limitations。
- **Original Problem:** video diffusion需要多次STDiT denoising、每步大量时空attention，模型又超出手机内存；单纯量化/重训成本高且不能分别处理steps、tokens和model residency三种瓶颈。
- **Why the Previous Design Was Reasonable:** 完整denoising保持数值轨迹；不合并tokens保留时序细节；整模型驻留避免I/O；cloud GPU提供足够memory/compute并简化runtime。
- **Changed Constraint:** iPhone 15 Pro仅约3.3GB可用内存和2.15 TFLOPS，需在不重训backbone的前提下同时降低迭代次数、每步token计算和峰值驻留。
- **Mechanism:** LPL在rectified-flow后段用当前flow方向按剩余步长做比例跃迁；TDTM沿时间平均相邻tokens、attention后unmerge；CI-DL把T5/STDiT/VAE拆block，prefetch下一block与当前inference重叠，并按运行时余量保留部分反复使用blocks。
- **State Ownership:** scheduler拥有denoising step/leap；TDTM映射拥有merged↔original temporal identity；block loader拥有host/package→GPU residency；retained-block set拥有跨step cache；CoreML artifact拥有device-specific executable。
- **Control Flow / Data Flow:** text→T5 block streaming→latent→STDiT repeated steps；每step可merge temporal tokens→attention→unmerge；到阈值执行LPL提前终止；下一block加载与当前block执行重叠；VAE分块decode输出视频。
- **Implementation Details:** PyTorch T5/STDiT/VAE转换为MLPackage；iOS18/iPhone15Pro；连续两帧token无相似度搜索直接平均；dynamic loading测block内存并决定retain数量；repository公开conversion与Xcode流程。
- **Evaluation Contract:** iPhone15Pro对比NVIDIA A6000 Open-Sora；68 frames、256×256 VBench多类别；LPL/TDTM不同启用steps；CI-DL分别测STDiT/T5 load-overlap；192/256分辨率报告component与E2E三次均值。
- **Baselines / Ablations / Sensitivity / Overhead:** no-method、单独LPL/TDTM/CI-DL及All；检查leap/merge起始step、T5与STDiT load/compute imbalance、VBench；作者成本对比不是等价TCO合同。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** iPhone15Pro GPU 2.15TFLOPS/3.3GB、A6000 48GB、Open-Sora、68 frames/256×256和单生成latency披露；precision、energy、thermal throttling、batch/concurrency与tail SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者Open-Sora/CoreML/iPhone合同中，分别优化step、token和residency可组合降低数分钟级生成延迟，并让超内存模型可执行。
- **What It Does Not Prove:** 不证明手机速度等同A6000；不证明VBench近似等价人类/物理质量；不证明privacy自动成立，也不证明三机制对所有diffusion schedulers/models通用。
- **Limitations / Threats to Validity:** 单设备/单backbone、低分辨率、三次均值、无energy/thermal、NPU未用、arXiv v1/v2 identity变化、repository转换步骤含已知VAE crash workaround。
- **Trade-offs / New Failure Modes:** leap可能偏离denoising trajectory；temporal average损失快速运动；streaming引入I/O stalls、block eviction/thrash、artifact incompatibility；retain策略挤占activation memory。
- **Where the Previous Design Still Applies:** cloud GPU适合低latency/高resolution；完整steps适合质量优先；不merge适合高速运动；整模型驻留适合memory充足；量化/distillation可与本方法形成其他分支。
- **Evolution Relationship:** `Layering / Dependency`：cloud resident runtime→model streaming；full steps→trajectory leap；full temporal tokens→merge/unmerge；三个层次组合而非单一替代。
- **ROADMAP Node:** `INFER-GPU-MEMORY`（Ch54）主 owner；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24、`INFER-TENSORRT-LLM` Ch49与`INFER-SCHEDULING` Ch56。
- **Target and Adjacent Chapters Read:** 已核对 Ch24、Ch42～50、Ch54～56的generation state、execution plan、memory residency与scheduler boundary。
- **Existing Coverage:** Books已覆盖offload/tiering；本family增加edge端step/token/residency联合优化链，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06；先前full-text blocker经CC BY v1 copy与official repository闭合，不保留错误blocked状态。
- **Open Questions:** thermal/energy如何进入SLO；block cache如何防止thrash；merge/leap决策怎样按prompt动态校准；CoreML artifact与model revision如何追踪。

### KV Cache Compression Fundamental-Abilities Study / ShotKV

- **Candidate / Week / Score:** Can LLMs Maintain Fundamental Abilities under KV Cache Compression? / 2025-W06 / 27/30。
- **Source Family ID:** `kvfundabench-shotkv-semantic-integrity`。
- **Source Type:** arXiv v1 paper；后续 v2～v4 仅作 revision genealogy。
- **First-public Date / Revision History:** v1 2025-02-04，题为 *Can LLMs Maintain Fundamental Abilities under KV Cache Compression?*；v2 2025-05-21；v3/v4 2026-05-08/12 改题为 *Semantic Integrity Matters* 并扩展 ICML 2026 版本。W06 只使用 v1 的方法与实验，后续版本不倒灌。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.01941；https://arxiv.org/html/2502.01941v1。
- **Related Primary Sources:** StreamingLLM、SnapKV、H2O、PyramidKV、PyramidInfer 与 ChunkKV 只定义被测前代；v4 仅说明同 family 后续演化。
- **Access and Verification Status:** Full Source Review Complete；v1 metadata、Method、六类任务、六种压缩方法、ShotKV、实验、Appendix 与 limitations 已核验，并隔离 v4 revision bleed。
- **Full-read Coverage:** 已读 KV/cache compression 定义、evaluation protocol、task/model/method setup、六项 observation、ShotKV prefill/decode 分离、many-shot结果、discussion、超参数、详细表格与伪代码。
- **Original Problem:** 既有 KV compression 多用 NIAH/LongBench 这类稀疏检索验证，在这些任务上保真不代表 arithmetic、code、safety 或长生成的高密度依赖仍完整。
- **Why the Previous Design Was Reasonable:** attention sink、heavy-hitter 或 recent-token selection 能显著降显存，且稀疏检索任务确实只依赖少量 token；统一 retention policy 也最容易实现和调参。
- **Changed Constraint:** workload 从“找到少数证据”转向 few-shot reasoning 与长生成，重要状态不再是孤立 token，而是必须整体保留的示例与推理链；prefill 与新增 decode token 的语义角色也不同。
- **Mechanism:** KVFundaBench 按知识、常识、算术、代码、安全与长生成切片测压缩退化；ShotKV 对 prefill shot 按跨层/头 attention 聚合评分并整段保留、一次压缩后冻结，对 decoding KV 使用独立动态策略。
- **State Ownership:** benchmark contract 拥有 task/metric/compression ratio；prefill compressor 拥有 shot boundary、ranking 与固定 prompt KV；decode policy 拥有生成期 KV budget；runtime 必须保留两类 cache identity。
- **Control Flow / Data Flow:** prompt shots→prefill attention统计→shot-level排序/预算选择→固定 prefill KV；每个生成 token→decode KV append/compress→与固定 prompt KV 联合 attention→下一个 token。
- **Implementation Details:** v1 使用 lm-evaluation-harness、A40；比较 StreamingLLM、SnapKV、H2O、PyramidKV、PyramidInfer、ChunkKV；ShotKV 以完整 shot 为选择单位并把 prefill/decode budget 解耦。
- **Evaluation Contract:** MMLU、CommonsenseQA、GSM8K、HumanEval、JailBreakV、LongGenBench 与 many-shot GSM8K；Llama-3.1-8B/base/instruct、DeepSeek-R1-Distill-Llama-8B；多压缩率；自动任务指标。
- **Baselines / Ablations / Sensitivity / Overhead:** FullKV 与六种 selection baseline；按 task、compression ratio、model type、prompt/shot length 与 chunk粒度分析；v1 未给出完整 production latency、continuous-batching 或 prefix-sharing overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** NVIDIA A40；三种 8B models；prompt shot/ratio 按实验变化；precision、batch、并发、prefix sharing、tail latency 与 service SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 v1 合同中，不同任务对 KV 删除的敏感度明显不同，算术/代码/安全与长生成在激进压缩下可早于稀疏检索失效；保留完整 few-shot semantic unit 是可行的条件性分支。
- **What It Does Not Prove:** 不证明 40% 是通用安全阈值，不证明 R1 类模型天然抗压缩，不证明 attention score 等于因果重要性，也不证明 v4 的延迟数字属于 v1。
- **Limitations / Threats to Validity:** 模型规模与 benchmark 有限、单 A40、自动 scorer、作者明确未覆盖更大模型和更多方法；task identity 在真实混合流量中未知，ShotKV 又依赖可识别 shot boundary。
- **Trade-offs / New Failure Modes:** semantic-unit retention 减少片段化，却可能保留冗余长 shot、饿死非 shot 证据；双 policy 增加 metadata、budget conflict、cache-key 与 fallback 复杂度；错误 task classification 会选错压缩率。
- **Where the Previous Design Still Applies:** 稀疏 retrieval、短回答、边界不清的 prompt 或极简 runtime 仍适合 token/head级 policy；显存充足和高可靠任务保留 FullKV；chunk policy 在语义边界不等于 shot 时仍合理。
- **Evolution Relationship:** `Direct Evolution`：统一 token retention→task-sensitive evaluation→semantic-unit-aware prefill retention + independent decode policy；不是宣称后者普遍替代前者。
- **ROADMAP Node:** `INFER-KV-CACHE`（Ch45）主 owner；handoff `INFER-PREFILL` Ch43、`INFER-PAGEDATTENTION` Ch47、`INFER-SCHEDULING` Ch56 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch43～47、Ch54～56 与 Ch66 的 cache identity、prefill/decode、paging、memory budget、scheduling 和 evaluation contract。
- **Existing Coverage:** Books 已覆盖 KV 生命周期与压缩分支；本 family 增加“评测任务密度决定压缩安全性”和 semantic-unit ownership，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；明确排除 2026 v4 新标题、ICML 状态与新增结果对 2025 事件的污染。
- **Open Questions:** 在线如何识别 reasoning density；shot boundary 如何进入 cache key；混合 batch 怎样分配两类 budget；压缩失真如何触发 per-request fallback。

### AlphaGeometry2

- **Candidate / Week / Score:** AlphaGeometry2 / 2025-W06 / 25/30。
- **Source Family ID:** `alphageometry2-neuro-symbolic-search`。
- **Source Type:** arXiv v1 paper；official code link 作为 artifact identity。
- **First-public Date / Revision History:** v1 2025-02-05；v2 2025-02-28澄清 abstract/introduction并更新 diagram generation；v3 2025-12-08增加 inequality rules 与代码链接。W06 以 v1 为证据边界。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.03544；https://arxiv.org/html/2502.03544v1。
- **Related Primary Sources:** AlphaGeometry/AG1 是直接前代；Gemini、TongGeometry 与 IMO 2024 system 只定义组件/比较背景。
- **Access and Verification Status:** Full Source Review Complete；v1 domain language、formalization/diagram、DDAR、synthetic data、SKEST、LM setup、results 与 appendices 已核验。
- **Full-read Coverage:** 已读 DSL coverage、linear equations/locus/non-constructive support、double points、C++ symbolic engine、point pruning、300M synthetic theorems、parallel search trees、analysis string、IMO-AG-50 与 hard-shortlist evaluation。
- **Original Problem:** AG1 的 DSL 只能形式化部分几何题，symbolic engine 不处理 double points 且搜索效率受限；LM 与 prover 只通过“auxiliary point / success”窄接口协作。
- **Why the Previous Design Was Reasonable:** 小 DSL 和固定规则容易保证 sound deduction，beam search 简单可控，LM 只提辅助构造能把不可靠生成与符号证明隔离。
- **Changed Constraint:** 目标扩展到 2000～2024 IMO 几何全集，需要表示移动对象、线性关系、locus 与非构造题，并在固定推理预算中探索更深/更宽的辅助构造。
- **Mechanism:** 扩展 DSL 与 DDAR；SKEST 并行运行不同宽深/提示/模型的 search trees，失败节点把与原题相关的已证 facts 写入 shared database；analysis string 将可证、假设目标后可证、数值图上成立的 facts 分层反馈给 LM。
- **State Ownership:** formalizer/DSL 拥有可表达问题；DDAR 拥有 sound facts/proof；每棵树拥有 branch-local auxiliary construction；shared DB 只拥有去除分支私有点后的可迁移 facts；LM 拥有 proposal 而非证明 authority。
- **Control Flow / Data Flow:** natural-language problem→formalization/diagram→DSL premises→多 search trees 提 auxiliary points→DDAR deduction→成功则返回 proof；失败则过滤并共享 facts→analysis string 更新后继续提案。
- **Implementation Details:** 更精简规则与更快 C++ DDAR、double-point normalization、reverse-topological point pruning；多种树宽/深和 forced predicate prefixes；Gemini-based LM 在约 300M synthetic theorems 上训练。
- **Evaluation Contract:** IMO-AG-50（45道 2000～2024 IMO geometry formalized为50实例）及30道可形式化 hardest shortlist；主要指标 solve rate；perplexity只作为与 proof search 不等价的 proxy。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 AG1、TongGeometry及多 AG2 配置比较；覆盖 DSL、engine、search/knowledge sharing 与 LM差异；未把组件收益完全因果拆分，搜索时间/调用成本也不构成 production SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Gemini-based专用 LM、synthetic theorem corpus 与 parallel search披露；具体硬件、precision、完整 token length、并发成本和 wall-clock SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在可形式化的 Olympiad geometry 域中，扩大 representation、增强 verifier、让隔离 search branches 共享已证事实并改进 proposal model 可共同提高 solve coverage。
- **What It Does Not Prove:** 不证明通用数学推理达到金牌水平，不证明自然语言端到端完全可靠，也不能把 84% 归因给单一 LM 或单一 search 机制。
- **Limitations / Threats to Validity:** 6个 IMO problems 在 v1 DSL 中不可形式化，2个受缺失高级几何规则/长搜索限制；手工 formalization、封闭符号域、选择的历史题与系统共演化都限制外推。
- **Trade-offs / New Failure Modes:** 更大 DSL/engine 提高覆盖但扩大 formalization与rule maintenance；shared facts 降重复搜索却可能放大错误过滤或污染所有树；多树/多模型提高覆盖同时增加 compute、dedup与termination复杂度。
- **Where the Previous Design Still Applies:** 可表达且搜索浅的问题继续适合单树/小 DSL；证明规则不成熟或事实不可验证时不应共享；通用开放域仍需独立 formalizer、verifier 与 human review。
- **Evolution Relationship:** `Direct Evolution`：LM proposal + symbolic verifier→更大 formal language/engine→多样 search trees + verified knowledge sharing；属于 neuro-symbolic workflow 演进而非纯模型 scaling。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79）主 owner；handoff `AGENT-WORKFLOW` Ch81、`AGENT-MULTI-AGENT` Ch82 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch66、Ch78～82 的 tool authority、planning/search state、workflow evidence、branch sharing 与 multi-agent coordination boundary。
- **Existing Coverage:** Books 已有 search、verified shared constraints 与 evaluator-driven workflow；本 family 提供 DSL→verifier→search→knowledge-sharing 的完整受限演进案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把作者“gold-medalist”标题外推成开放域模型能力。
- **Open Questions:** natural-language formalizer 的错误率怎样进入总 solve rate；shared fact 如何 version/retract；组件 ablation 能否分离 DSL、engine、LM 与 search 收益；证明时间如何纳入 service budget。

### ScoreFlow

- **Candidate / Week / Score:** ScoreFlow / 2025-W06 / 24/30。
- **Source Family ID:** `scoreflow-score-dpo-workflow-generator`。
- **Source Type:** arXiv v1 paper + author repository identity。
- **First-public Date / Revision History:** arXiv v1 2025-02-06；截至访问日无后续 arXiv revision。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04306；https://arxiv.org/html/2502.04306v1；https://github.com/Gen-Verse/ScoreFlow。
- **Related Primary Sources:** ADAS、AFlow、GPTSwarm、DPO/PPO/SFT 只定义 workflow-search 与 optimizer baselines。
- **Access and Verification Status:** Full Source Review Complete；representation、Score-DPO derivation、iterative algorithm、datasets、baselines、ablation、cost与appendices已核验。
- **Full-read Coverage:** 已读 code workflow space、operator set/validity constraint、score-sampling、score-weighted ranking objective、theorems、六 benchmark setup、cross-model tests、iteration/cost分析、generator prompt/operators与algorithm。
- **Original Problem:** 手工 workflow 不可扩展，graph/template search 限制 conditional state；离散反思/MCTS搜索昂贵且易早收敛，而普通 pairwise DPO 丢失 evaluator score 幅度并受 noisy pair 影响。
- **Why the Previous Design Was Reasonable:** 静态 workflow 易审计，graph 明确通信边；离散搜索无需训练 generator，pairwise preference 对不同 scorer scale 更稳健。
- **Changed Constraint:** 跨 QA/code/math 的 task-specific workflow 数量增长，需要能表示 loop/condition/code、复用量化 execution feedback，并降低昂贵 optimizer API 调用。
- **Mechanism:** generator 为每题生成 Python workflow 与 operators；executor 运行并打分；按 score 构造 preference pairs，enhanced sampling提高有信息 pair概率，Score-DPO把 score distance并入 ranking loss；迭代更新 generator 至收敛/预算终止。
- **State Ownership:** generator checkpoint 拥有 proposal policy；workflow artifact 拥有 code/operator graph；executor environment 拥有运行结果；evaluator version 拥有 score；preference dataset 拥有 pair、score与iteration lineage；controller 拥有停止条件。
- **Control Flow / Data Flow:** task→采样 k 个合法 workflow→executor执行→score→构造/重采 preference pairs→Score-DPO LoRA更新 generator→下一轮；最终 workflow 仍需独立执行验证。
- **Implementation Details:** 默认 Llama-3.1-8B-Instruct generator + vLLM，GPT-4o-mini executor temperature 0，LoRA，2×A6000；operators含 programmer/reviewer/reviser/ensemble/customizable；代码 representation 支持 condition/loop。
- **Evaluation Contract:** HumanEval、MBPP、GSM8K、MATH level-5 subset、DROP 与 HotpotQA；1:4 validation/test；三次运行均值；任务对应 exact/solve/pass metrics，由 GPT-4o-mini 等 executor 执行。
- **Baselines / Ablations / Sensitivity / Overhead:** IO、CoT、SC、MedPrompt、MultiPersona、Self-Refine、ADAS、AFlow；pipeline内替换 SFT/PPO/DPO；换 generator/executor、迭代曲线与 cost；缺少独立 held-out workflow safety 和 production failure injection。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2×A6000、Llama/Qwen generator、GPT-4o-mini/GPT-4o/DeepSeek executors披露；precision、workflow token length、并发、API queue、tail SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在六个封闭 benchmark 和作者 evaluator contract 中，带量化 score 的 iterative generator fine-tuning 是替代离散 workflow search 的可行分支，并在该设置优于列出的 baselines。
- **What It Does Not Prove:** 不证明 8.2% 对其他 tasks/models/scorers成立，不证明生成代码安全、workflow有因果最优性，也不证明 test execution与真实业务 outcome 等价。
- **Limitations / Threats to Validity:** evaluator 与 executor 同源偏差、三次均值、测试集选择、generated-code sandbox/权限未形成生产 contract；Score-DPO 理论条件只在作者轨迹中近似满足约91.1%，不是普遍保证。
- **Trade-offs / New Failure Modes:** 连续优化提高 sample reuse 但需训练/版本化 generator；score幅度带来信息也放大 scorer calibration error；代码空间更灵活却增加不可终止、side effect、dependency与security failure。
- **Where the Previous Design Still Applies:** workflow少且高风险时手写 state machine 更可审计；无可靠量化 score 时 pairwise/human review更稳健；小搜索空间可继续用 discrete/MCTS；有 executable oracle 时 deterministic search优先。
- **Evolution Relationship:** `Alternative Branch`：manual/static→discrete code-workflow search→score-conditioned learned generator；它改变 proposal policy，不转移 executor/verifier/deployment authority。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `TRAIN-DPO` Ch34、`AGENT-PLANNING` Ch79、`AGENT-MULTI-AGENT` Ch82 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch34、Ch66、Ch79～82 的 preference objective、evaluator-driven search、durable state、execution authority与coordination tax。
- **Existing Coverage:** Books 已覆盖 evaluator-driven workflow search；本 family 增加“量化 score 如何进入 workflow-generator preference update”的受限分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把 benchmark solve rate写成生产 workflow reliability。
- **Open Questions:** score calibration漂移怎样检测；generated code如何sandbox/replay；generator更新怎样避免test contamination；workflow lineage与executor/model版本怎样绑定。

### VideoRoPE

- **Candidate / Week / Score:** VideoRoPE / 2025-W06 / 25/30。
- **Source Family ID:** `videorope-spatiotemporal-position-identity`。
- **Source Type:** arXiv v1 paper；后续 revisions 属同一 family。
- **First-public Date / Revision History:** v1 2025-02-07；v2 2025-04-27；v3 2025-05-30。W06 以 v1 HTML 与其实验为证据，后续 revision 不重复计分。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.05173；https://arxiv.org/html/2502.05173v1。
- **Related Primary Sources:** Vanilla RoPE、TAD-RoPE、RoPE-Tie、M-RoPE 与 Qwen2-VL 只定义前代/初始化 baseline。
- **Access and Verification Status:** Full Source Review Complete；v1 position design、V-NIAH-D、training/evaluation、module ablations、128K appendix与频率分析已核验。
- **Full-read Coverage:** 已读 1D→3D position问题、低频 temporal allocation、diagonal layout、adjustable spacing公式、training data/settings、LongVideoBench/MLVU/Video-MME/VideoHallucer/V-NIAH-D、ablation与supplement。
- **Original Problem:** 把 1D RoPE 直接扩成 video 的 t/x/y 分配会破坏空间对称、让时间维使用高频周期并出现远位置 collision，且 video/text token index密度不匹配。
- **Why the Previous Design Was Reasonable:** 1D RoPE 对文本简单有效；M-RoPE 将维度分给三轴，是最直接的多模态推广；固定连续 index 易与现有 attention kernel兼容。
- **Changed Constraint:** 长视频同时需要时间远距辨别、空间 patch 相对几何、文本前后缀连续位置，并在训练只见 8K 时外推到更长视觉序列和周期 distractors。
- **Mechanism:** 将低频 rotary dimensions 分配给 temporal axis；x/y 高频维度交错；每帧中心沿 `(t,t,t)` diagonal推进、patch围绕中心偏移；用可调 `delta` 缩放 frame间 temporal spacing并保持前后文本线性衔接。
- **State Ownership:** position-index builder 拥有 modality/span/frame/patch identity与delta；model config/checkpoint 拥有维度分配；KV cache保存已旋转 K 的position语义；serving runtime不得在reuse/packing时重编号破坏 identity。
- **Control Flow / Data Flow:** text/video/text tokenization→按 modality 生成3D indices→Q/K各维旋转→attention；video frame中心沿diagonal，spatial patch偏移，ending text从视频终点继续统一index。
- **Implementation Details:** 以 Qwen2-VL-7B vision encoder与Qwen2-7B LLM初始化；2 fps、最多128 frames、动态分辨率控制token数；训练窗口8192；推理用vLLM支持32K以上。
- **Evaluation Contract:** LLaVA-Video-178k子集约154K videos/1.3M pairs；LongVideoBench、MLVU、Video-MME、VideoHallucer、V-NIAH/V-NIAH-D；比较8K/16K/32K/64K并有128K补充。
- **Baselines / Ablations / Sensitivity / Overhead:** Vanilla/TAD/M-RoPE；依次加入 diagonal layout、low-frequency temporal allocation、adjustable spacing，并测x/y交错与delta；未隔离所有data/training variance和production KV/cache overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 704 A100 GPU-hours、batch128、Qwen2-based 7B、train 8K、eval至64K/128K、2fps；precision、serving concurrency、KV bytes、TTFT/TPOT与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 Qwen2-based video LLM合同中，position frequency/layout/spacing是可独立设计的系统状态，三项组合改善列出的长视频理解、检索与 hallucination benchmarks。
- **What It Does Not Prove:** 不证明位置编码单独产生时间因果理解，不证明64K token等于64K有效视频信息，也不证明该分配对所有head dimensions、fps、vision encoders通用。
- **Limitations / Threats to Validity:** 单主干与训练配方、synthetic distractor、有限真实长视频、最大帧数与tokenization耦合；作者未提供跨模型/硬件延迟、position drift或cache reuse failure测试。
- **Trade-offs / New Failure Modes:** 低频时间轴减少collision却降低近邻时间分辨率；delta错配fps会扭曲速度；3D identity增加packing/cache-key复杂度；外推仍可能遇到未训练频率、视觉encoder与memory上限。
- **Where the Previous Design Still Applies:** 短视频或单图继续可用 M-RoPE/2D；固定fps/窗口内任务不必引入动态spacing；只处理文本时 vanilla RoPE最简单；显式temporal module是另一条分支。
- **Evolution Relationship:** `Direct Evolution`：1D sequence position→3D axis allocation→frequency-aware temporal axis + symmetric layout + modality-density spacing；不是对内容建模或long-context runtime的替代。
- **ROADMAP Node:** `MODEL-POSITION-ENCODING`（Ch13）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23、`MODEL-LONG-CONTEXT` Ch22、`INFER-KV-CACHE` Ch45。
- **Target and Adjacent Chapters Read:** 已核对 Ch12～14、Ch22～23 与 Ch43～45 的 representation、position、attention、long-context、prefill和KV position identity。
- **Existing Coverage:** Books 已覆盖 RoPE 与 position-id runtime约束；本 family 增加 video三轴 frequency/layout/spacing 的演进案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；作者 benchmark数字保持在完整 model/data/length/hardware合同内。
- **Open Questions:** variable fps与frame dropping如何更新delta；跨请求prefix/video chunk reuse如何校验3D identity；低频分配怎样随head dimension变化；有效利用长度怎样单独测量。

### SCONE / Scaling Embedding Layers

- **Candidate / Week / Score:** SCONE / 2025-W06 / 24/30。
- **Source Family ID:** `scone-contextualized-offloaded-ngram-embedding`。
- **Source Type:** arXiv v1 paper；后续 NeurIPS 2025 revisions 属同一 family。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-05-18；v3 2025-10-23（NeurIPS 2025 camera-ready）。W06 只以 v1 为事件证据。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.01637；https://arxiv.org/html/2502.01637v1。
- **Related Primary Sources:** BPE/tokenization、GPT-2/OLMo 与大词表 scaling 只定义基础架构和比较。
- **Access and Verification Status:** Full Source Review Complete；v1 f-gram构造、training/inference、storage/lookup、WebText/OLMo scaling、ablation与implementation appendices已核验。
- **Full-read Coverage:** 已读大词表稀疏更新问题、SCONE architecture/algorithms、CPU/NVMe layout、latency方法、max n、f-gram count与learner size scaling、matched-parameter baselines、OLMo corpus结果与实现细节。
- **Original Problem:** 直接扩大 vocabulary/input embedding会使大量稀有 rows 在固定 token budget下更新不足，同时扩大 output softmax、accelerator memory与decode成本；只增深主干又增加每token FLOPs。
- **Why the Previous Design Was Reasonable:** 单 token table lookup极快、weight tying省参数，扩大词表能缩短序列；主干 scaling 具有成熟 dense compute路径和更通用的context modeling能力。
- **Changed Constraint:** 希望把额外 training compute 转成 lexical/contextual capacity，却维持原 vocabulary、output projection和accelerator-resident inference FLOPs/memory。
- **Mechanism:** 从训练语料选高频2～n-grams；独立小 Transformer 将每个f-gram映射为contextualized token embeddings并与主模型联合训练；训练后预计算大表，CPU/NVMe按最长匹配查询，base token embedding仍驻加速器用于decode。
- **State Ownership:** tokenizer拥有base ids；f-gram vocabulary/version拥有sequence→row identity；learner checkpoint拥有生成表的training lineage；offline materializer拥有table artifact；CPU/NVMe store与lookup runtime拥有residency/cache；main model拥有融合后的input contract。
- **Control Flow / Data Flow:** corpus→统计/选择f-grams→joint training main+f-gram transformer→materialize lookup table；inference时tokens→最长f-gram查询→embedding传GPU→与base表示结合→main decoder；输出仍走原词表。
- **Implementation Details:** 最大 n 多数为5；in-memory matrix+hash dictionary，NVMe用LMDB；d=2048、FP16 table；WebText GPT-2规模与 OLMo-like 1B context2048；lookup最多每token 4次查询。
- **Evaluation Contract:** WebText validation/WikiText-103 perplexity，128M/419M/589M main与matched larger baselines；f-grams 512K→100M；OLMo corpus上10M/1B表与0.7B～1.9B models；lookup按100K batches测量。
- **Baselines / Ablations / Sensitivity / Overhead:** 直接大 vocabulary、相同 training-time参数的larger main models；max n、table size、f-gram learner size、CPU vs NVMe、batch sensitivity；未给真实分布式prefetch、tail latency和fleet TCO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** storage test为64-core Xeon/512GB/NVMe、d2048 FP16；OLMo-like 1B/context2048；训练硬件、decode GPU、并发、cache hit、p99与SLO部分 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者语料与模型规模中，input lexical capacity可从accelerator compute移到训练期生成和off-accelerator lookup，且table/learner扩大与perplexity改进相关。
- **What It Does Not Prove:** 不证明固定 FLOPs 等于固定端到端 latency/TCO，不证明 1B table 在生产可运维，不证明 lexical capacity优于主干context compute于所有语言/任务，也不证明序列长度减少。
- **Limitations / Threats to Validity:** 主要是perplexity、有限模型/语料；1B table约7.7TB NVMe，查询实验与真实多租户I/O差异大；外部 commercial token rate被用作参照而非同平台 baseline；artifact refresh成本未测。
- **Trade-offs / New Failure Modes:** 少GPU FLOPs换来TB级artifact、CPU/NVMe bandwidth、hot-key skew、cache miss与transfer；f-gram表与tokenizer/data drift会失配；训练多一个model并增加materialization/checkpoint lineage。
- **Where the Previous Design Still Applies:** 内存/存储受限、小模型/小数据、词法模式弱或对open-vocabulary泛化更重要时普通 embedding 更合理；提高主干宽深在需要组合推理时仍成立；大 vocabulary可在短序列收益更大时保留。
- **Evolution Relationship:** `Alternative Branch`：扩大 vocabulary或main model→保持output contract、扩展contextualized input table→把容量迁到training + memory hierarchy；不是通用 scaling law。
- **ROADMAP Node:** `MODEL-EMBEDDING`（Ch12）主 owner；handoff `MODEL-TOKENIZER` Ch11、`TRAIN-PRETRAINING` Ch28、`INFER-GPU-MEMORY` Ch54 与 `PLATFORM-RESOURCE-SCHEDULING` Ch65。
- **Target and Adjacent Chapters Read:** 已核对 Ch11～13、Ch27～28、Ch54、Ch57～65 的 vocabulary/embedding、data lineage、training artifact、memory hierarchy与resource ownership。
- **Existing Coverage:** Books 已有 token row→hashed n-gram capacity分支；SCONE增加独立learner、materialized artifact与off-accelerator lookup的完整状态链，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不复用 v3 camera-ready结论替代 v1，也不把perplexity改进写成通用服务收益。
- **Open Questions:** table如何分片/热更新；tokenizer与table revision如何原子切换；lookup p99与GPU stall如何治理；训练/存储/能耗怎样进入同一TCO contract。

### Almost Surely Safe Alignment / InferenceGuard

- **Candidate / Week / Score:** On Almost Surely Safe Alignment of LLMs at Inference-Time / 2025-W06 / 24/30。
- **Source Family ID:** `inferenceguard-safety-state-augmented-decoding`。
- **Source Type:** arXiv v1 paper；v2/v3 属同一 revision family。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-02-05；v3 2025-06-20。W06 使用 v1 题名、理论假设与实验，不把后续修订静默合并。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.01208；https://arxiv.org/html/2502.01208v1。
- **Related Primary Sources:** cMDP/safe RL、RLHF、Best-of-N、beam search、ARGS、RECONTROL与token-wise cost model只定义理论前代/实验 baseline。
- **Access and Verification Status:** Full Source Review Complete；v1 cMDP、state augmentation、latent-space theorem、critic/scoring/diversity、PKU-SafeRLHF实验、proof assumptions与qualitative appendix已核验。
- **Full-read Coverage:** 已读 expected vs almost-sure constraint、safety budget state、penalty construction、latent mapping、Bellman/optimal-policy assumptions、critic双头、block sampling、baselines、dataset/metrics、reward-safety-latency trade-off与 proofs。
- **Original Problem:** 训练后安全 alignment 昂贵且可能改变模型；普通 inference-time reward reranking以期望/Lagrangian权衡 helpfulness和safety，无法保证单条轨迹不越过累计 safety budget。
- **Why the Previous Design Was Reasonable:** RLHF可把安全偏好内化，Lagrangian只需一个可调乘子；BoN/beam/token reranking无需修改base weights，部署接口简单且可按需求调trade-off。
- **Changed Constraint:** 目标从“平均更安全”提升为相对给定 cost model 的trajectory级累计约束，同时要求不反向训练base LLM并控制test-time search成本。
- **Mechanism:** 把 safety budget tracker `z` 加入 cMDP state，以越界大惩罚转成 unconstrained objective；在LLM latent state训练小critic预测safe probability与future task cost；block采样候选，critic过滤/排序，失败token frequency驱动diversity search。
- **State Ownership:** base LLM拥有proposal distribution；constraint tracker拥有每轨迹剩余budget；cost models定义task/safety measurement；critic checkpoint拥有近似value；decoder controller拥有beam/block history、failure-frequency与termination；policy gate拥有实际允许动作。
- **Control Flow / Data Flow:** prompt/partial output→base LLM采样token block→更新 latent/safety state→critic判safe并估future cost→选择继续或高惩罚拒绝；无safe candidate时避开失败token重采→完成轨迹后用task/safety models评估。
- **Implementation Details:** critic两输出分别预测安全与future cost；阈值0.5；终局安全预算满足才用task cost，否则给大惩罚；block sampling近似保持与reference分布相近，base weights不更新。
- **Evaluation Contract:** PKU-SafeRLHF 37,400 train/3,400 test；每train prompt由base model采5条轨迹训练critic；Alpaca-7B与Beaver-v3-7B；指标为reward model、token-wise safety cost、budget10 safety rate与seconds/response。
- **Baselines / Ablations / Sensitivity / Overhead:** BoN、beam、ARGS、RECONTROL及其Lagrangian/safety-augmented版本；比较reward-safety-time与cost distribution；未提供 cost-model calibration drift、adversarial adaptive attack或生产并发SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 两个7B base models与PKU数据披露；硬件、precision、block length、beam/sample count完整配置、batch/concurrency、p95/p99与服务SLO部分 `Not Disclosed`。
- **What the Evidence Actually Proves:** 若给定cost/state mapping满足论文假设、存在有限成本最优policy且惩罚足够大，latent augmented MDP具有理论上的almost-sure约束结论；实际 InferenceGuard 在作者 benchmark呈现条件性reward/safety/time权衡。
- **What It Does Not Prove:** 不保证现实世界安全、cost model正确或对分布外攻击稳健；critic近似求解不自动满足定理前提；“almost surely”不是零风险，也不覆盖tool side effects。
- **Limitations / Threats to Validity:** guarantee相对于learned cost与强连续性/可行action假设；单数据集/两7B模型；baseline被作者扩展；无human red-team、calibration confidence、model drift、拒答公平性或部署故障测试。
- **Trade-offs / New Failure Modes:** trajectory gate强化约束但增加多次sample/critic latency；cost false positive导致过度拒答，false negative破坏保证；budget/latent state不同步、critic drift、search exhaustion与diversity penalty可降低helpfulness或卡死。
- **Where the Previous Design Still Applies:** 训练期 alignment仍适合稳定广泛行为；简单output filter适合低预算风险；Lagrangian适合软约束与连续trade-off；高风险tool action仍需deterministic policy/approval，不由text decoder独占authority。
- **Evolution Relationship:** `Layering / Dependency`：training alignment→test-time reranking→trajectory safety-state augmentation；它把constraint state加入decode control，但依赖cost model且不能替代外部security gate。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `INFER-SCHEDULING` Ch56、`PLATFORM-EVALUATION-SYSTEM` Ch66 与 `AGENT-WORKFLOW` Ch81。
- **Target and Adjacent Chapters Read:** 已核对 Ch56、Ch66、Ch71～73 与 Ch79～81 的 inference budget、evidence、threat model、governance、planning约束和workflow authority。
- **Existing Coverage:** Books 已强调 safety evaluation与external policy gate；本 family 增加 per-trajectory safety state与theorem-assumption boundary，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；保留 `Status: Experimental`，不把形式保证改写成实际deployment guarantee。
- **Open Questions:** critic/cost drift怎样在线校准；状态跨 speculative/parallel decoding如何保持；无safe candidate时系统怎样fail closed；tool/action cost如何进入同一budget。

### Improving Transformer World Models for Data-Efficient RL

- **Candidate / Week / Score:** Improving Transformer World Models for Data-Efficient RL / 2025-W06 / 24/30。
- **Source Family ID:** `transformer-world-model-dyna-warmup-nnt-btf`。
- **Source Type:** arXiv v1 paper；后续 revisions 属同一 Source Family。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-06-02；v3 2025-07-16。W06 只使用 v1 的方法、67.42% reward、27.91% score 与实验合同，不让后续摘要的 69.66 倒灌。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.01591；https://arxiv.org/html/2502.01591v1。
- **Related Primary Sources:** Dyna、IRIS、DreamerV3、Craftax 与 purejaxrl 只定义前代、环境和实现起点。
- **Access and Verification Status:** Full Source Review Complete；v1 Method、算法、PPO/world-model实现、hyperparameters、ablation、rollout comparison、Craftax-full preliminary result 与 conclusion 已核验。
- **Full-read Coverage:** 已读 model-free baseline、Dyna with warmup、patch NNT、block teacher forcing、1M-step evaluation、每层 ladder ablation、world-model rollout error、qualitative failure、算法与 Appendix。
- **Original Problem:** 只用真实环境的 model-free RL 数据效率有限；只用 learned world model imagination 训练 policy 又会把建模误差变成训练分布，并受不稳定视觉 token identity 与逐 token rollout 延迟影响。
- **Why the Previous Design Was Reasonable:** model-free PPO 避免 model bias；纯 imagination 能最大化 world-model复用；VQ-VAE 与 autoregressive teacher forcing 是成熟的图像离散化和 likelihood 训练接口。
- **Changed Constraint:** Craftax-classic 同时具有随机地图、partial observability、稀疏 achievement hierarchy 与 1M environment-step预算，要求 world model 提高样本效率又不能污染 policy。
- **Mechanism:** policy 立即消费真实 rollout；world model 经过 `T_BP` warmup 后才生成较短 imagined rollout；视觉按独立 patch 用静态 nearest-neighbor codebook 编码；block teacher forcing 在同一未来 time slice 联合建模并并行采样全部 tokens。
- **State Ownership:** environment 拥有真实 transition；replay buffer 拥有 real trajectories；TWM checkpoint 拥有近似 transition；policy/critic 拥有 action/value；warmup controller 拥有 imagination启用时点；NNT codebook 拥有稳定 token identity。
- **Control Flow / Data Flow:** real environment rollout→立即 PPO update并写 replay→更新 TWM→达到 warmup 后从 replay observation 启动短 imagined rollout→再次 PPO update；imagined state 不回写为真实事实。
- **Implementation Details:** Craftax observation为63×63、9×9个7×7 patches；48 environments、real horizon 96；TWM imagined horizon 20；PPO基于purejaxrl，policy为CNN+低维GRU，NNT codebook仅在遇到远离现有码的patch时扩展。
- **Evaluation Contract:** Craftax-classic 22 achievements、1M environment steps；reward为achievement success算术均值，score为几何聚合；160条长度20轨迹用于TWM比较；Craftax-full只给preliminary result。
- **Baselines / Ablations / Sensitivity / Overhead:** MFRL、IRIS、DreamerV3与逐层移除Dyna、NNT、patch、BTF、warmup；最佳MBRL为67.42±0.55 reward/27.91±0.63 score，去Dyna为55.02±5.34/18.79±2.14，`T_BP=0`为33.54±10.09/12.86±4.05；未形成production latency/SLO合同。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 最佳MFRL在单A100上约15分钟训练1M steps；TWM/policy规模、48 env、horizon与patch配置披露；precision、完整MBRL wall-clock、distributed concurrency与service SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者v1 Craftax合同中，真实与短imagined数据混合、延迟启用 imagination、稳定patch token identity和time-slice并行训练均对最终样本效率有独立贡献。
- **What It Does Not Prove:** 不证明 learned world model 等于环境事实，不证明所有任务都应从VQ-VAE切换到NNT，不证明background planning优于decision-time planning，也不证明人类分数比较可外推为通用智能。
- **Limitations / Threats to Validity:** 单一2D游戏族、patch结构与环境高度契合；world model仍产生不可行transition；Craftax-full证据初步；组件共同演进且hardware/训练成本披露不完整。
- **Trade-offs / New Failure Modes:** warmup减少早期污染却延迟 imagined data收益；短rollout限制compounding error也限制长程规划；静态NNT便于建模却可能扩大codebook；BTF并行采样牺牲同time-slice token依赖；real/imagined policy updates会引入新鲜度与权重配比问题。
- **Where the Previous Design Still Applies:** 环境便宜或model bias高时model-free RL更稳健；精细连续视觉仍可用learned tokenizer；需要每步lookahead时decision-time planning仍合理；world model未校准时禁止imagined update。
- **Evolution Relationship:** `Direct Evolution`：model-free real rollout→pure-imagination background planning→warmup后的real+short-imagined Dyna；token side从moving VQ code→patch factorization→stable NNT + BTF。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `TRAIN-RLHF` Ch31、`TRAIN-PPO` Ch32、`AGENT-PLANNING` Ch79 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch24～26、Ch31～32、Ch66与Ch79的生成模型、action-conditioned transition、policy update、evaluation和planning边界。
- **Existing Coverage:** Books 已区分video generation、world model与simulator，并强调imagination不是事实；本 family 增加 warmup、real/imagined ownership 与 time-slice tokenization 的可审计演进，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；v2/v3结果不作为W06事实，未修改Books。
- **Open Questions:** imagination启用怎样用模型误差而非固定step触发；real/imagined advantage怎样校准；codebook扩展如何版本化；world-model hallucination怎样触发rollback。

### LongDPO

- **Candidate / Week / Score:** LongDPO / 2025-W06 / 23/30。
- **Source Family ID:** `longdpo-process-preference-long-form`。
- **Source Type:** arXiv v1 paper；后续 revision/ACL版本属于同一family。
- **First-public Date / Revision History:** v1 2025-02-04；v2 2025-05-20。W06严格采用v1文本与实验。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.02095；https://arxiv.org/html/2502.02095v1。
- **Related Primary Sources:** LongWriter、LongGenBench、DPO、MCTS与UltraFeedback只定义模型、benchmark与前代objective。
- **Access and Verification Status:** Full Source Review Complete；v1 MCTS、global memory、critique refinement、step-pair construction、training、evaluation、human study与appendix已核验。
- **Full-read Coverage:** 已读process supervision动机、node expansion/value/backprop、七原则reward、memory pool、低分chosen refinement、2.5k WildChat采样、DPO训练、LongBench-Write/LongGenBench/general benchmarks、human reliability与case study。
- **Original Problem:** long-form response 的终局 preference 无法定位局部事实漂移、遗漏或结构失败；普通DPO把整篇文档压成一个chosen/rejected pair，credit assignment粗且容易用长度/风格shortcut。
- **Why the Previous Design Was Reasonable:** outcome pair标注和sequence-level DPO简单、成本低、与现有preference pipeline兼容；短回答中的局部错误常能由终局分数反映。
- **Changed Constraint:** 16K/32K长文包含多段依赖与事实一致性，单次终局评分难以产生足够密度的纠错信号，且直接穷举step pairs成本过高。
- **Mechanism:** 以MCTS扩展最多4层、每节点4个children、每节点最多2048 tokens；reward model按七原则评估suffix；global memory在selection时维持已建立事实；chosen reward低于2.5时用外部critique改写，再构造step-level preference pairs用于DPO。
- **State Ownership:** tree node拥有局部prefix；global memory拥有跨step事实约束；generator checkpoint拥有proposal；70B evaluator/critic拥有proxy reward与critique；preference dataset拥有pair和生成lineage；DPO reference拥有更新坐标。
- **Control Flow / Data Flow:** instruction→MCTS expansion→suffix score/backprop→memory-constrained selection→低分chosen外部critique/refinement→step pair→与UltraFeedback混合→packed DPO update→独立long/general evaluation。
- **Implementation Details:** LongWriter-Llama3.1-8B与LongWriter-Qwen2.5-7B；Llama-3.1-70B-Instruct作reward/critique；从WildChat随机2.5k instructions收集pairs，lr 1e-6、cosine schedule、max length 32768 packing、seed42、250 steps。
- **Evaluation Contract:** LongBench-Write-en、LongGenBench 16K/32K、TruthfulQA、MMLU、GSM8K；各方法使用相同decoding设置；GPT-4o judge做三次一致性检查，并由三名本科/研究生annotators比较diversity、consistency、informativeness。
- **Baselines / Ablations / Sensitivity / Overhead:** base LongWriter、普通DPO与LongDPO；有memory/critique与评价可靠性分析，但缺少完整组件因果拆分、跨judge校准、tree search成本和生产吞吐测量。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B/8B policy、70B evaluator、max 32,768 tokens、250 steps披露；GPU、precision、batch、MCTS并发、训练/生成时长、p95/p99与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者两类LongWriter backbone与列出的long-form benchmark中，MCTS生成的step preference数据是比其普通DPO baseline更有效的条件性训练分支，并未明显牺牲所测general tasks。
- **What It Does Not Prove:** 不证明process steps是真实因果分解，不证明70B/GPT-4o judge无偏，不证明所有长文本任务受益，也不证明32K输出在production中事实一致。
- **Limitations / Threats to Validity:** 2.5k prompt、单类reward/critique模型、有限human annotators、自动judge与作者模型同分布；global memory construction、evaluator calibration、MCTS成本与跨域失败披露有限。
- **Trade-offs / New Failure Modes:** 更细credit提升可定位性却增加tree/evaluator调用；memory维持一致性也可能固化早期错误；critique提高pair margin却引入teacher bias；step segmentation和packing会改变length distribution与reference logprob语义。
- **Where the Previous Design Still Applies:** 短任务、可靠终局verifier或预算严格时sequence-level DPO更简单；高风险事实任务仍需外部retrieval/verifier；memory不可验证时不应成为事实authority。
- **Evolution Relationship:** `Direct Evolution`：outcome pair→MCTS生成step pair→memory/critique增强的process preference；不是用process label取代最终结果验证。
- **ROADMAP Node:** `TRAIN-DPO`（Ch34）主 owner；handoff `TRAIN-RLHF` Ch31、`AGENT-WORKFLOW` Ch81、`AGENT-MEMORY` Ch77 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch31～34、Ch66、Ch77与Ch79～81的preference objective、length bias、memory provenance、search与workflow evidence。
- **Existing Coverage:** Books 已覆盖DPO pair、reference identity、length distribution与offline shift；本 family增加long-form process pair的生成链与memory/critic新状态，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把作者自动judge分数写成通用写作质量。
- **Open Questions:** memory中的事实如何验证/撤回；step pair如何避免同源judge偏差；MCTS调用成本怎样进入training budget；长pair的token weighting如何防length shortcut。

### VideoJAM

- **Candidate / Week / Score:** VideoJAM / 2025-W06 / 23/30。
- **Source Family ID:** `videojam-joint-appearance-motion-inner-guidance`。
- **Source Type:** arXiv v1 paper；project samples为辅助artifact。
- **First-public Date / Revision History:** v1 2025-02-04；v2 2025-05-26。W06只使用v1方法与实验。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.02492；https://arxiv.org/html/2502.02492v1。
- **Related Primary Sources:** Flow Matching、DiT、RAFT、Classifier-Free Guidance与VBench只定义前代组件/评价。
- **Access and Verification Status:** Full Source Review Complete；v1 motivation、joint representation、Inner-Guidance公式、training/evaluation、ablation、implementation、limitations与appendix已核验。
- **Full-read Coverage:** 已读frame-permutation诊断、appearance/motion dual I/O、optical-flow representation、guidance依赖分析、4B/30B训练、VideoJAM-bench、人评/VBench、组件ablation、SDEdit probe与limitations。
- **Original Problem:** video flow-matching objective可在大部分denoising阶段对frame permutation近乎不敏感，模型优先拟合appearance而非时间变化，导致动作停滞、方向错误或物理不连贯。
- **Why the Previous Design Was Reasonable:** 单一pixel/latent velocity objective直接复用image diffusion/flow模型，数据和架构接口简单；text CFG能提升prompt alignment而无需额外motion labels。
- **Changed Constraint:** 高质量视频不仅要求逐帧美观，还要求5秒/128帧中的coherent motion；继续单纯扩数据/参数不能保证objective对时间扰动敏感。
- **Mechanism:** 用RAFT从原训练视频派生RGB optical-flow表示；增加输入线性层和appearance/motion双输出头，让共享latent同时预测两种velocity；推理时将模型自己的noisy motion prediction置空构造Inner-Guidance，与text guidance联合校正appearance output。
- **State Ownership:** base video latent拥有appearance状态；motion latent/flow拥有相邻帧位移proxy；shared DiT checkpoint拥有联合representation；sampler拥有每step motion estimate和guidance scales；RAFT只生成训练target，不是推理真值。
- **Control Flow / Data Flow:** video→RAFT motion representation→二者加噪并投影到shared latent→DiT→双头预测appearance/motion velocity；inference并行计算conditional、text-unconditional与motion-blank分支→组合velocity→下一denoising step。
- **Implementation Details:** 原训练集随机3M samples（小于3%）；4B用32×A100、batch32、50k iterations，30B用256×A100、batch256、35k iterations；256×256、128 frames、24fps、fixed lr 5e-6，默认`w1=5,w2=3`。
- **Evaluation Contract:** 128条holdout prompt组成VideoJAM-bench，覆盖basic/complex/rotational/physics motion；VBench appearance/motion、人类visual quality/text alignment比较与SDEdit probe；网页512²样例使用额外super-resolution，论文量化实验为256²。
- **Baselines / Ablations / Sensitivity / Overhead:** Sora、Kling、base DiT及去text guidance、去Inner-Guidance、去optical flow、IP2P-style guidance；guidance scale与motion step probe；proprietary baseline的模型/采样合同不完全可比。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4B/30B、32/256 A100、batch32/256、128 frames、24fps、256²披露；precision、完整训练时长、sampling steps实际时延、并发、显存与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者DiT与数据合同中，显式motion auxiliary target让training objective更关注时间结构，模型自身motion prediction可作为条件性self-guidance并改善所测motion指标/人评。
- **What It Does Not Prove:** 不证明生成模型学到causal physics/world dynamics，不证明optical flow是真实运动原因，不证明对所有视频架构通用，也不证明优于proprietary模型的比较受同一生成合同控制。
- **Limitations / Threats to Validity:** 低分辨率与RGB flow使zoom-out小物体运动信号弱，复杂物体交互仍失败；RAFT bias、单一内部base模型、128-prompt benchmark与自动/人评限制外推。
- **Trade-offs / New Failure Modes:** 双表示增强motion却增加target生成、output channels和训练state；Inner-Guidance需额外分支并可能放大错误motion；强motion guidance可能损害appearance/text；flow对遮挡、镜头运动和小物体不稳。
- **Where the Previous Design Still Applies:** 静态/低motion视频或成本敏感生成仍适合单appearance objective；有可靠轨迹/3D状态时可选显式controller；需要可控因果transition时应使用world model而非把video quality当替代证据。
- **Evolution Relationship:** `Layering / Dependency`：appearance-only flow matching→joint appearance-motion training→self-conditioned motion guidance；它增强生成objective，不等同于world-model演进。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23与`MULTIMODAL-WORLD-MODELS` Ch25。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25 的representation identity、AR/diffusion分支、iterative correction与video-generation/world-model边界。
- **Existing Coverage:** Books 已区分生成质量与环境transition；本 family增加appearance/motion objective与self-guidance的受限演进，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不保留脱离分辨率、帧数、硬件和evaluator的headline benchmark。
- **Open Questions:** RAFT误差如何传播；motion/appearance guidance怎样动态校准；额外sampler分支的latency是多少；何种physical benchmark能区分视觉连贯与因果正确。

### Inverse Bridge Matching Distillation

- **Candidate / Week / Score:** Inverse Bridge Matching Distillation / 2025-W06 / 23/30。
- **Source Family ID:** `ibmd-diffusion-bridge-inverse-distillation`。
- **Source Type:** arXiv v1 paper；v2属同一revision family。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-08-18。W06以v1为唯一事件证据。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.01362；https://arxiv.org/html/2502.01362v1。
- **Related Primary Sources:** I2SB、DDBM、DBIM、CBD/CBT与consistency distillation定义teacher/baseline。
- **Access and Verification Status:** Full Source Review Complete；v1 inverse formulation、theorems、alternating algorithm、conditional/unconditional experiments、hyperparameters、discussion与limitations已核验。
- **Full-read Coverage:** 已读DBM/bridge matching、coupling inverse problem、inner bridge model、generator objective、algorithm、ImageNet inverse problems、Edges→Handbags/DIODE translation、train/test behavior、appendix hyperparameters与licenses。
- **Original Problem:** Diffusion Bridge Models能处理data-to-data transition，但推理需多次teacher evaluations；已有distillation多为conditional或无法把DBM压到one-step，普通consistency目标不恢复原teacher drift。
- **Why the Previous Design Was Reasonable:** 多步bridge integration忠实离散化teacher动态；conditional accelerator可利用已知source/target结构；普通consistency避免反传through teacher，训练更稳且内存较低。
- **Changed Constraint:** 希望同一方法同时支持conditional/unconditional DBM和one/multi-step sampling，并只依赖source-side samples而不需要target-domain training data。
- **Mechanism:** 将distillation写成寻找generator coupling的inverse problem，使其bridge-matching drift接近teacher；用额外bridge network近似当前generator coupling，交替更新bridge与generator；generator loss比较teacher posterior estimate与learned bridge estimate并反传through三者。
- **State Ownership:** teacher checkpoint拥有目标drift；student generator拥有source/noise→target coupling；auxiliary bridge checkpoint拥有当前student coupling estimate；source sampler拥有`x_T`；optimizer/controller拥有交替更新节奏与EMA。
- **Control Flow / Data Flow:** sample source `x_T`和noise→generator产`x_0`→bridge path sample`x_t`→更新auxiliary bridge拟合student coupling→同批再次前向teacher/bridge/generator→差分loss更新student→推理只运行student。
- **Implementation Details:** student/bridge从teacher checkpoints初始化；batch256、EMA0.99；支持generator适配noise输入；实验含I2SB五类ImageNet 256² inverse tasks和DDBM两类image translation，详细lr/iterations按setup配置。
- **Evaluation Contract:** 4× super-resolution（bicubic/pool）、JPEG restoration QF5/QF10、128² center inpainting、Edges→Handbags 64²、DIODE-Outdoor 256²；指标NFE、FID、classification accuracy或Inception Score，部分baseline数字引用原论文。
- **Baselines / Ablations / Sensitivity / Overhead:** I2SB/DDBM teacher、DBIM、CBD、CBT及传统inverse baselines；比较1/2/4/更多NFE和train/test样例；未提供跨seed统计、wall-clock/energy、统一重跑所有baselines或完整stability sensitivity。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** batch256与图像分辨率披露；GPU型号、precision、训练wall-clock、sampling latency、并发与SLO `Not Disclosed`；作者明确student训练约需teacher训练3×内存。
- **What the Evidence Actually Proves:** 在列出的I2SB/DDBM image contracts中，inverse bridge formulation能学习保留teacher行为的少步/一步student，且可同时用于conditional与unconditional bridge family。
- **What It Does Not Prove:** 不证明所有任务达到teacher质量、不证明4×–100×等step reduction等于同等wall-clock收益、不修复teacher过拟合或mode collapse，也不证明无需source distribution访问。
- **Limitations / Threats to Validity:** 交替优化昂贵，需反传teacher+bridge+generator并约3×内存；图像任务有限，baseline部分来自文献；teacher缺陷会被忠实蒸馏，DIODE案例明确复现mode collapse。
- **Trade-offs / New Failure Modes:** 推理减少NFE却把成本前移到高内存训练；auxiliary bridge引入新checkpoint、新鲜度与不稳定性；one-step吞吐更高但可能损失diversity/faithfulness；teacher failure被压缩后更难发现。
- **Where the Previous Design Still Applies:** 无法承受distillation训练或teacher频繁变化时多步DBM更合适；高保真/可调compute任务保留multi-step；只需conditional特例时较轻CBD/CBT仍可能更经济。
- **Evolution Relationship:** `Alternative Branch`：multi-step DBM→conditional acceleration/consistency branch→inverse-coupling distillation；不是所有diffusion任务的单向替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `INFER-REQUEST-LIFECYCLE` Ch42与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch42与Ch66的diffusion correction、representation、request compute budget与evidence contract。
- **Existing Coverage:** Books 已覆盖iterative generation与latency/quality branch；本 family增加DBM inverse distillation及训练成本转移，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把NFE reduction改写成未测量的production speedup。
- **Open Questions:** 交替优化如何检测collapse；teacher revision如何触发student/bridge重建；少步质量怎样按request自适应；3×训练内存的TCO何时值得。

### Demystifying Long Chain-of-Thought Reasoning in LLMs

- **Candidate / Week / Score:** Demystifying Long Chain-of-Thought Reasoning in LLMs / 2025-W06 / 24/30。
- **Source Family ID:** `demystifying-long-cot-training-contract`。
- **Source Type:** arXiv v1 paper + official code repository。
- **First-public Date / Revision History:** v1 2025-02-05；截至访问日无后续arXiv revision。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.03373；https://arxiv.org/html/2502.03373v1；https://github.com/eddycmu/demystify-long-cot。
- **Related Primary Sources:** QwQ-32B-Preview、Qwen2.5-Math、DeepSeek-R1、Kimi k1.5、MATH/WebInstruct与PPO/REINFORCE++只定义teacher、data和baseline。
- **Access and Verification Status:** Full Source Review Complete；v1 SFT/RL experiments、reward公式、data filtering、base-model exploration、system bottlenecks、hyperparameters与limitations已核验。
- **Full-read Coverage:** 已读constructed/emergent long CoT、rejection sampling、Cosine Reward与repetition/discount、WebInstruct-462k、rule/model verifier、base-model RL、behavior measurement、PPO vs REINFORCE observation、Appendix tables/algorithms。
- **Original Problem:** “longer CoT、SFT、RL compute、aha moment”常被混成单一因果叙事；缺少对初始化数据、reward shaping、verifier coverage、compute和测量方法的系统拆分。
- **Why the Previous Design Was Reasonable:** SFT蒸馏可快速注入长轨迹，终局correctness reward简单可验证，response length容易观测；短实验可先检查可行性。
- **Changed Constraint:** 14K-token generation带来高方差rollout和straggler，稀疏reward容易length hacking；可人工验证数据不足，base model已有行为又会混淆“emergence”。
- **Mechanism:** 比较constructed与teacher-emergent CoT的SFT/RL初始化；Cosine Reward按correctness与length给终局分数并可叠加repetition penalty；从WebInstruct-462k生成/过滤verifiable数据；同时检查base model行为频率与RL compute。
- **State Ownership:** SFT dataset拥有teacher/provenance与rejection结果；policy/critic/reference拥有RL状态；verifier version拥有correctness边界；reward config拥有length/penalty语义；rollout trace拥有behavior与token length；scheduler承担straggler。
- **Control Flow / Data Flow:** teacher生成CoT→ground-truth/rejection filter→SFT checkpoint→PPO rollouts→rule/model verifier→correctness+length reward/GAE→policy update→按任务accuracy、length与behavior pattern分开评价。
- **Implementation Details:** Llama-3.1-8B；long CoT由QwQ-32B-Preview蒸馏，short CoT由Qwen2.5-Math-72B-Instruct；RL context为prompt2048+generation14336，batch512、8 episodes×16 samples、actor lr5e-7、critic lr9e-6、KL0.01。
- **Evaluation Contract:** MATH-500、AIME2024、TheoremQA、MMLU-Pro-1k；WebInstruct经MinHash为462k，生成2条/prompt后过滤得约189k responses/115k prompts；model verifier为Qwen2.5-Math-7B-Instruct，short-answer extraction用Llama-3.1-8B-Instruct。
- **Baselines / Ablations / Sensitivity / Overhead:** constructed vs emergent SFT、SFT vs SFT+RL、classic vs cosine reward、reward参数、repetition penalty、discount、MATH/WebInstruct mixture、rule/model verifier、base RL与REINFORCE++观察；大量组合但不是统一full factorial。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型、context、batch、episodes/samples、lr披露；GPU型号、precision、总训练时间、rollout并发、p95 straggler、energy与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者8B/MATH/WebInstruct合同中，SFT不是理论必需但能提高有限compute下效率；reward shape可显著操纵length/stability；diverse noisy data在适当verifier/filter下可改善部分OOD指标。
- **What It Does Not Prove:** 不证明长输出等于更强推理，不证明“aha moment”由RL新生，不证明PPO普遍优于REINFORCE++，也不证明web数据或cosine参数跨模型可复用。
- **Limitations / Threats to Validity:** 单主干/有限seed与benchmark；teacher/verifier同源能力、自动answer matching和大量hyperparameter选择；作者明确REINFORCE++未充分tune，且长CoT系统瓶颈仍未解决。
- **Trade-offs / New Failure Modes:** SFT提高稳定性却可能复制teacher模式；length shaping抑制爆长也可能截断必要推理；model verifier扩大覆盖却引入judge error；长rollout增加KV、同步等待与checkpoint state；web filtering会选择性丢弃难题。
- **Where the Previous Design Still Applies:** 可靠短答案任务继续使用rule verifier与短CoT；预算小可先SFT；无稳定verifier时不宜扩大RL；需要低延迟时length cap/直接回答分支仍合理。
- **Evolution Relationship:** `Alternative Branch`：short/constructed SFT→teacher-emergent long SFT→verifiable RL与reward shaping→noisy-data scaling；不是“越长越先进”的单向路线。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；handoff `TRAIN-SFT` Ch29、`TRAIN-PPO` Ch32、`TRAIN-GRPO` Ch33、`INFER-SCHEDULING` Ch56与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～33、Ch56和Ch66的SFT provenance、reward hacking、rollout lifecycle、straggler与verifier contract。
- **Existing Coverage:** Books 已覆盖reward hacking、verifier scope与sequence/token credit；本 family增加length reward、data/filter/compute联合实验与“行为存在不等于新涌现”边界，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把作者观察写成所有reasoning model的训练定律。
- **Open Questions:** verifier uncertainty如何进入advantage；long rollout怎样异步调度而不改变on-policy语义；length reward怎样避免任务偏置；behavior emergence需要何种causal measurement。

### Teacher Hacking

- **Candidate / Week / Score:** On Teacher Hacking in Language Model Distillation / 2025-W06 / 24/30。
- **Source Family ID:** `teacher-hacking-offline-distillation-proxy-gap`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** v1 2025-02-04；截至访问日无后续revision。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.02671；https://arxiv.org/html/2502.02671v1。
- **Related Primary Sources:** Goodhart/reward hacking、T5/Flan-T5、XSum、WMT14和Natural Instructions只定义理论类比、model/data前代。
- **Access and Verification Status:** Full Source Review Complete；v1 formal definitions、two-stage setup、metrics、offline/online experiments、diversity/budget/model/loss/mixture ablations、hyperparameters与conclusion已核验。
- **Full-read Coverage:** 已读oracle→teacher→student pipeline、sequence divergences、held-out proxy/golden curves、offline vs teacher/student online sampling、polynomial convergence deviation、dataset/model-size/loss ablations、offline-online mixture与Appendix tables。
- **Original Problem:** distillation只观察student接近teacher的proxy objective；teacher本身是ground-truth分布的近似，student可能持续改善proxy却远离真正目标，而普通train/validation overfitting检查未必发现。
- **Why the Previous Design Was Reasonable:** 固定teacher-generated dataset可缓存、吞吐稳定、训练可复现；soft logits比hard labels携带更多分布信息；teacher通常确实比student强。
- **Changed Constraint:** 长时间优化和有限prompt diversity会让student利用teacher/dataset的代理偏差；现实中又无法直接访问ground-truth distribution来计算golden metric。
- **Mechanism:** 建立semi-synthetic oracle→teacher→student链；在held-out prompts上同时测student-to-teacher proxy divergence与student-to-oracle golden divergence；比较固定offline、online teacher和online student sampling，并用prompt diversity、generation budget和proxy convergence偏离诊断hacking。
- **State Ownership:** Flan-T5-XL oracle只在实验中定义golden proxy；teacher checkpoint拥有被蒸馏分布；student checkpoint拥有优化状态；offline dataset拥有固定prompt/response lineage；online sampler拥有当前生成分布；metric evaluator拥有model pair与sampling config。
- **Control Flow / Data Flow:** oracle生成小SFT集→teacher/student初始化→teacher在prompt distribution上提供soft target→student update；offline固定responses或每步online采样→held-out prompts计算proxy/golden curves→比较hacking与mitigation。
- **Implementation Details:** oracle Flan-T5-XL 3B；T5-1.1 small77M/base250M/large800M；XSum、WMT14 en-de、Natural Instructions；softmax temperature1；典型batch32/64、input 80～2048、output80～256、lr3e-4、最高703,125 steps。
- **Evaluation Contract:** 三种sequence-level distance（forward/reverse KL与JS-like）在held-out prompts上估计；offline训练50 epochs观察长期趋势；降低prompt diversity但保持dataset size、每prompt增加2/3 generations、不同teacher/student size/loss与10/50/90% offline mixtures。
- **Baselines / Ablations / Sensitivity / Overhead:** offline vs online teacher/student，prompt diversity、generation budget、三datasets、三model sizes、forward/reverse/JS loss与offline-online mixture；oracle不是现实ground truth，未提供human/task quality或deployment drift测试。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data/steps/batch/length披露；GPU、precision、wall-clock、online generation latency/concurrency、storage与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在semi-synthetic T5合同中，固定offline distillation可出现proxy继续改善而golden恶化；增加prompt/response diversity和少量online student data可缓解；proxy convergence偏离是该设置中的候选诊断信号。
- **What It Does Not Prove:** 不证明Flan-T5 oracle是真实ground truth，不证明所有offline distillation都会hacking，不证明polynomial deviation是充分检测器，也不证明online generation在现实teacher中无偏。
- **Limitations / Threats to Validity:** controlled oracle定义本身是近似；encoder-decoder T5与三tasks限制外推；golden metric在真实系统不可得；online sampling更贵且可能受student drift，WMT diversity结果也与其他tasks不一致。
- **Trade-offs / New Failure Modes:** offline caching高效却收窄覆盖；online sampling改善diversity但增加teacher/student serving成本与非确定性；多responses/prompt提高局部support不等于prompt diversity；proxy monitor可能误报/漏报。
- **Where the Previous Design Still Applies:** teacher高度可靠、prompt support稳定且训练短时offline distillation仍经济；有真实labels时优先独立golden evaluation；低预算可混入少量online data而非完全重构pipeline。
- **Evolution Relationship:** `Principle Reuse`：RL reward hacking的proxy-gap原则复用于distillation；工程演进为fixed offline targets→diversity-aware generation→online/offline mixture，而不是宣称online永远替代offline。
- **ROADMAP Node:** `TRAIN-SFT`（Ch29）主 owner；handoff `TRAIN-DATA` Ch27、`TRAIN-RLHF` Ch31与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～31与Ch66的数据provenance、distillation/SFT objective、proxy hacking、held-out evaluation和release evidence。
- **Existing Coverage:** Books 已覆盖demonstration provenance与reward Goodhart；本 family补充distillation中proxy/golden分离、offline diversity与online mixture的受限证据，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把semi-synthetic oracle写成现实真值。
- **Open Questions:** 无oracle时golden drift如何近似；online mixture比例怎样按成本/风险自适应；teacher更新如何隔离dataset/version；proxy convergence detector怎样跨loss校准。

### Token Assorted

- **Candidate / Week / Score:** Token Assorted: Mixing Latent and Text Tokens for Improved Language Model Reasoning / 2025-W06 / 23/30。
- **Source Family ID:** `token-assorted-discrete-latent-reasoning-traces`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** v1 2025-02-05；截至访问日无后续revision。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.03275；https://arxiv.org/html/2502.03275v1。
- **Related Primary Sources:** VQ-VAE、iCoT、Pause Token、MetaMathQA、DART-MATH、ProntoQA/ProsQA只定义压缩、baseline和数据合同。
- **Access and Verification Status:** Full Source Review Complete；v1 VQ-VAE、replacement strategy、synthetic/math experiments、ablation、attention analysis、hyperparameters与appendices已核验。
- **Full-read Coverage:** 已读latent code训练、partial left-to-right replacement、random mixing、maze/logical/math设置、Sol-Only/CoT/iCoT/Pause baselines、token efficiency、replacement ablation、模型与数据细节。
- **Original Problem:** 显式CoT中大量token用于语言连贯而非核心状态转换，推理轨迹拉长training/inference compute；完全删除CoT又可能失去有效depth与可学习监督。
- **Why the Previous Design Was Reasonable:** 文本CoT可读、可监督、直接兼容tokenizer和next-token loss；curriculum逐步删减中间步骤能平滑适应，但训练阶段多且调参复杂。
- **Changed Constraint:** 需要在保留部分可见reasoning/solution的同时压缩早期轨迹，并让已预训练LLM快速接纳全新latent vocabulary。
- **Mechanism:** VQ-VAE把16个text tokens压成1个离散code（codebook1024）；只从左侧替换前`m`个CoT tokens，保留后续文本；训练时随机采样替换上限和`m`，让模型同时见多种latent/text比例。
- **State Ownership:** VQ encoder/codebook/decoder拥有latent token语义；extended tokenizer/checkpoint拥有新vocabulary identity；training sample拥有replacement boundary；LLM KV/sequence state混合latent与text；最终答案仍由text verifier评估。
- **Control Flow / Data Flow:** prompt+CoT+solution→按chunk训练VQ-VAE→选定左侧boundary并替换为code ids→加`boLatent/eoLatent`→LLM next-token training→推理生成混合轨迹和text solution。
- **Implementation Details:** VQ-VAE训练100k steps、Adam、lr1e-5、batch32、chunk16/codebook1024；Llama-3.2-1B/3B与Llama-3.1-8B在MetaMathQA训练1 epoch、batch32、packing4096并搜索4个lr。
- **Evaluation Contract:** Keys-Finding Maze 100k、ProntoQA 9k、ProsQA 17,886；MATH/GSM8K及Fresh-Gaokao、DeepMind-Math、College-Math、OlympiadBench-Math、TheoremQA；accuracy与生成token数分开报告。
- **Baselines / Ablations / Sensitivity / Overhead:** Sol-Only、full CoT、iCoT、Pause Token；all/curriculum/Poisson/random left-to-right replacement、attention分析与DART-MATH复验；未提供真实decode latency/KV/energy或latent code漂移测量。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 1B/3B/8B、packing4096、batch32与数据规模披露；GPU、precision、训练wall-clock、serving batch/concurrency、TTFT/TPOT与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者任务/模型合同中，部分离散latent replacement可比其text-only CoT baseline缩短轨迹并维持或提升部分accuracy，random mixing比所测curriculum/all-replace更易适应新tokens。
- **What It Does Not Prove:** 不证明latent token忠实表达真实推理，不证明平均17% token reduction等于相同比例wall-clock收益，也不证明codebook对分布外任务稳定或可解释。
- **Limitations / Threats to Validity:** VQ reconstruction与task correctness非同一目标；单codebook/固定16×compression、有限模型和math/logical tasks；缺少跨seed、cache/kernel、code collapse与人工faithfulness验证。
- **Trade-offs / New Failure Modes:** 序列更短但新增VQ训练、vocabulary/version与embedding冷启动；latent不可读使debug/audit更难；错误code可能压缩并隐藏多步错误；混合boundary增加packing/cache identity。
- **Where the Previous Design Still Applies:** 高可审计任务保留完整text CoT；短任务无需压缩；连续latent可作为另一分支；无法绑定codebook revision时不应复用latent cache。
- **Evolution Relationship:** `Alternative Branch`：完整text CoT→curriculum/internalization→random mixed discrete latent/text；不是“不可见推理”必然替代可读轨迹。
- **ROADMAP Node:** `MODEL-TOKENIZER`（Ch11）主 owner；handoff `MODEL-EMBEDDING` Ch12、`TRAIN-SFT` Ch29、`MODEL-KV-CACHE` Ch19与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch11～12、Ch19～20、Ch29与Ch66的token identity、embedding、autoregressive state、SFT provenance与evidence boundary。
- **Existing Coverage:** Books 已覆盖tokenizer/checkpoint/cache identity；本 family增加task-derived latent vocabulary和mixed reasoning trace的受限分支，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把token count reduction外推为未测量的服务加速。
- **Open Questions:** codebook/tokenizer如何原子版本化；latent trace怎样可审计；code collapse如何检测；真实GPU kernel能否兑现长度收益。

### Large Language Model Guided Self-Debugging / PyCapsule

- **Candidate / Week / Score:** Large Language Model Guided Self-Debugging Code Generation / 2025-W06 / 23/30。
- **Source Family ID:** `pycapsule-two-agent-execution-debug-loop`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** v1 2025-02-05；v2 2025-03-31。W06只使用v1正文与实验。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.02928；https://arxiv.org/html/2502.02928v1。
- **Related Primary Sources:** HumanEval/ET、MBPP/ET、BigCodeBench、AgentCoder、MapCoder、LDB与Docker只定义benchmark、baseline和sandbox前代。
- **Access and Verification Status:** Full Source Review Complete；v1 two-agent workflow、signature/example/error/test modules、Docker execution、benchmarks、attempt breakdown、case studies与appendix已核验。
- **Full-read Coverage:** 已读programmer/executor responsibilities、prompt inference、code/library artifacts、execution feedback、error refinement、case testing、three-model evaluation、0～5 attempts、failure examples与module details。
- **Original Problem:** 单次code generation缺少执行证据；复杂multi-agent方案调用成本高；原始compiler/test error噪声大，反复塞回prompt会造成context污染和无效debug循环。
- **Why the Previous Design Was Reasonable:** direct/CoT生成调用少；多agent角色分工可并行探索；原始error message保留完整证据且无需额外parser。
- **Changed Constraint:** 需要在有限调用中生成可执行Python、安装依赖、运行hidden/public tests并利用错误反馈，同时隔离不受信代码。
- **Mechanism:** programmer agent生成`main.py`/`requirements.txt`并负责fix；executor在轻量Docker中安装依赖、执行tests并返回status；signature converter、example-call detection、error handler与case testing把输入/反馈规范化；最多多轮修复。
- **State Ownership:** programmer conversation拥有proposal/history；executor container拥有process/files/dependencies；test harness拥有pass/fail authority；error handler拥有裁剪后的diagnostic；controller拥有attempt budget与termination；模型不拥有真实正确性。
- **Control Flow / Data Flow:** task/tests→推断signature/example call→programmer生成代码/依赖→Docker执行→status/error→refine diagnostic→programmer fix→重复至success或预算耗尽→保留artifact与test evidence。
- **Implementation Details:** 两agent而非大型角色群；executor入口shell安装requirements并运行`main.py`；MBPP可从首个test推断函数签名但不泄露expected output；attempt 0为初始解，后续最多5次fix。
- **Evaluation Contract:** HumanEval 164、MBPP 974、BigCodeBench 1,140及ET扩展tests；GPT-4-Preview-1106、GPT-3.5-Turbo-1106、Qwen2.5-Coder-Instruct；PyCapsule三次运行报告mean/std，部分baseline数字取自原报告且AgentCoder未复现。
- **Baselines / Ablations / Sensitivity / Overhead:** Direct、CoT、Self-Planning、AgentCoder、MapCoder、LDB；按debug attempt分解增量成功率并展示diminishing returns；缺少module-by-module完整ablation、sandbox attack和同成本统一重跑。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型版本、benchmark、attempt budget披露；LLM API hardware/precision、prompt length、Docker并发、dependency install latency、p95/p99与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者Python benchmark合同中，受测试驱动的两角色loop和结构化error feedback可提高累计pass rate；后续attempt边际贡献递减。
- **What It Does Not Prove:** 不证明生成代码安全或适用于repository级软件，不证明两agent普遍优于所有multi-agent，也不证明hidden test pass等于spec正确；不可复现baseline限制排名。
- **Limitations / Threats to Validity:** 小函数任务、测试oracle与Python限定；private-test-derivedsignature有benchmark leakage风险；Docker隔离/网络/secret policy未完整披露；部分baseline非同run，调用成本和failure taxonomy不足。
- **Trade-offs / New Failure Modes:** execution提高grounding却引入任意代码、依赖供应链、资源泄漏和sandbox escape；error压缩降噪也可能丢根因；多轮提高累计成功率但放大cost/history contamination和oscillation。
- **Where the Previous Design Still Applies:** 低风险简单函数可direct generation；无可靠tests时human review优先；大型repo需durable workspace、权限和change review，不能直接复用轻量loop。
- **Evolution Relationship:** `Layering / Dependency`：single-pass code→execution feedback→structured two-agent debug workflow；executor/verifier authority在模型外，agent数量不是单向演进。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `AGENT-TOOL-CALLING` Ch78、`PLATFORM-SECURITY` Ch72与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch66、Ch72、Ch78～82的tool proposal、sandbox authority、durable workflow、termination与multi-agent coordination tax。
- **Existing Coverage:** Books 已覆盖persistent interpreter、sandbox和verifier loop；本family提供轻量programmer/executor分层及attempt decay案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把benchmark pass rate写成生产代码可靠性。
- **Open Questions:** container权限/网络怎样最小化；debug history何时压缩/回滚；test leakage如何审计；attempt budget怎样按边际收益停止。

### ConceptAttention

- **Candidate / Week / Score:** ConceptAttention: Diffusion Transformers Learn Highly Interpretable Features / 2025-W06 / 23/30。
- **Source Family ID:** `conceptattention-dit-output-space-saliency`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** v1 2025-02-06；v2 2025-06-01；v3 2025-06-17。W06使用v1机制与评测。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04320；https://arxiv.org/html/2502.04320v1。
- **Related Primary Sources:** Flux/SD3、DAAM、TextSpan、CLIP/DINO与ImageNet-Seg/PascalVOC只定义backbone/baseline/evaluation。
- **Access and Verification Status:** Full Source Review Complete；v1 attention formulation、output-space projection、datasets/baselines、single/multi-class evaluation、ablation与qualitative appendix已核验。
- **Full-read Coverage:** 已读MM-DiT attention、concept embedding construction、cross/self attention、output vs key/value/cross-attention spaces、noise/layer aggregation、segmentation metrics、human annotation ambiguity与appendix pseudo-code。
- **Original Problem:** raw prompt cross-attention只覆盖prompt内词，并且attention weight不等于经过value/output mixing后的representation；为额外concept改prompt又会改变生成图像。
- **Why the Previous Design Was Reasonable:** cross-attention map容易提取且与text-image连接直观；CLIP/DINO probe成熟；segmentation可提供量化localization proxy。
- **Changed Constraint:** 需要在不重训、不改变原prompt/image的情况下查询open-set concept，并判断MM-DiT内部representation是否包含可定位语义。
- **Mechanism:** 将独立concept tokens与image tokens送入Flux MMAttn参数，允许concept cross-attend image并self-attend其他concept；取得每层concept/image attention output vectors，线性投影得patch saliency，再跨18层聚合。
- **State Ownership:** Flux checkpoint拥有frozen representation；concept query set拥有解释问题；VAE/noise setting拥有输入状态；probe缓存拥有layer outputs；threshold/annotation版本拥有segmentation verdict；saliency不拥有causal authority。
- **Control Flow / Data Flow:** real image→VAE latent+noise→frozen Flux forward并缓存MMAttn outputs；concept tokens独立查询→output-space similarity→layer average→threshold/multiclass argmax→对annotation计算mIoU/Acc/mAP。
- **Implementation Details:** PyTorch Flux-Schnell distilled model、18 MMAttn layers；real images而非生成图；class名简化为单token；patch score按mean threshold二值化，multi-class按最高concept score。
- **Evaluation Contract:** ImageNet-Segmentation 4,276 images/445 categories；PascalVOC 930 single-class与1,449 multi-class images；metrics为mIoU、pixel/patch accuracy、mAP，且作者承认annotation ambiguity。
- **Baselines / Ablations / Sensitivity / Overhead:** TextSpan、TransInterp、DINO attention、DAAM SDXL/SD2、Flux raw cross-attention；比较CA/key/value/output spaces、softmax、cross/self/both/neither、layers/noise；无因果intervention或跨DiT family验证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Flux-Schnell与dataset规模披露；GPU、precision、image resolution/batch、probe latency/memory、并发与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在冻结Flux-Schnell和两segmentation datasets中，attention output-space的线性concept-image相似度比所测cross-attention/interpretability baselines更好地匹配标注区域。
- **What It Does Not Prove:** 不证明DiT生成时因果依赖该feature，不证明saliency是忠实解释，不证明mIoU等于可控性/安全性，也不证明对所有多模态DiT通用。
- **Limitations / Threats to Validity:** 单backbone、class-known setup、中心物体偏置、简化单token label与人工annotation ambiguity；linear decodability和causation未分离，hardware overhead未测。
- **Trade-offs / New Failure Modes:** training-free probe便宜但可能产生相关性幻觉；open-set concept扩大查询能力也增加prompt/query敏感性；跨层平均可稳定map却掩盖层间机制差异；threshold影响排名。
- **Where the Previous Design Still Applies:** 需要因果结论时使用activation intervention；UNet/CLIP/DINO继续适合相应architecture；生产解释需多probe、counterfactual与human review。
- **Evolution Relationship:** `Principle Reuse`：raw attention visualization→representation-space probe→output-space concept localization；属于evidence ladder提升，不是机制真相的替代。
- **ROADMAP Node:** `WORLDVIEW-REPRESENTATION`（Ch5）主 owner；handoff `MODEL-SELF-ATTENTION` Ch14、`MULTIMODAL-REPRESENTATION` Ch23与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch5、Ch14、Ch23～24与Ch66的decodability/correlation/causation、attention输出、多模态representation和evaluation evidence。
- **Existing Coverage:** Books 已区分linear probe与因果机制；本family提供MM-DiT output-space saliency案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把zero-shot segmentation排名写成内部因果解释。
- **Open Questions:** intervention是否验证saliency方向；跨Flux/SD3与不同noise是否稳定；probe latency如何控制；annotation disagreement如何进入uncertainty。

### UltraIF

- **Candidate / Week / Score:** UltraIF: Advancing Instruction Following from the Wild / 2025-W06 / 23/30。
- **Source Family ID:** `ultraif-constraint-evaluation-question-data-pipeline`。
- **Source Type:** arXiv v1 paper + official repository identity。
- **First-public Date / Revision History:** v1 2025-02-06；v2 2025-09-28。W06用明确锁定的v1 PDF，不混入EMNLP/v2变化。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04153；https://arxiv.org/pdf/2502.04153v1；https://github.com/kkk-an/UltraIF。
- **Related Primary Sources:** ShareGPT、OpenHermes2.5、No Robots、AutoIF、Evol-Instruct、DPO/NCA与五个instruction benchmarks只定义data/baseline/objective。
- **Access and Verification Status:** Full Source Review Complete；arXiv v1 PDF的decomposition、UltraComposer、Generate-then-Evaluate、SFT/iterative DPO/NCA、training/evaluation、ablation、prompts与appendix已核验。
- **Full-read Coverage:** 已读constraint/eval-question generation、composer training、iterative augmentation、response pair construction、strong-to-weak/self-alignment、10k→200k scaling、five IF benchmarks、general capability与training config。
- **Original Problem:** 手工constraint可验证但同质；自由LLM instruction evolution更丰富却难保证response满足复杂约束；仅按复杂度扩增会把错误监督同步放大。
- **Why the Previous Design Was Reasonable:** 人工rules可执行且准确，prompt evolution成本低；SFT对chosen response简单稳定；强teacher可提供高质量合成数据。
- **Changed Constraint:** 希望从真实user instruction分布学习多样constraint，同时为每个constraint产生可执行/可问答的quality check，并支持小teacher self-alignment。
- **Mechanism:** 70B模型把真实instruction分解为simple query、constraints和evaluation questions；训练8B UltraComposer从simple query重建复杂instruction+questions；迭代加constraints，生成K responses并逐question评估形成chosen/rejected；先SFT，再iterative DPO，末轮用NCA修正DPO margin偏置。
- **State Ownership:** source dataset拥有real instruction provenance；decomposer/composer checkpoints拥有synthetic transformation；eval question set拥有constraint rubric；generator/evaluator version拥有response与judgment；pair dataset/reference checkpoint拥有iteration lineage。
- **Control Flow / Data Flow:** ShareGPT等instruction→70B decomposition/questions→8B composer SFT→iterative complexification→8B/70B生成K responses→question-wise evaluation→chosen/rejected→SFT→iterative DPO/NCA→held-out evaluation。
- **Implementation Details:** UltraComposer由Llama-3.1-8B-Instruct训练；strong-to-weak用70B生成/评估并训练8B-Base，self-alignment用8B-Instruct；8×A100 80GB、bf16、ZeRO-3、FlashAttention2、Xtuner；data scale 10k/8k至175k+20k。
- **Evaluation Contract:** IFEval、Multi-IF、InfoBench、LiveBench IF subset、FollowBench；另测math/reasoning/coding/general conversation；IFEval/Multi-IF含function-verifiable指标，其余部分由LLM judge，benchmark信息不用于data construction按作者声明。
- **Baselines / Ablations / Sensitivity / Overhead:** ShareGPT SFT、Evol-Instruct、Conifer、AutoIF；strong-to-weak/self-alignment、SFT vs iterative DPO、scale-up和general capability；缺少independent evaluator、constraint contradiction/red-team和完整生成成本统计。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8×A100 80GB、bf16、ZeRO-3、8B/70B与data规模披露；sequence length/batch细节在appendix，在线生成并发、LLM calls tail latency与production SLO未形成服务合同。
- **What the Evidence Actually Proves:** 在作者8B/70B与五benchmark合同中，从真实instruction分解出的constraint+question可作为合成、rejection和preference data接口，并在所测同budget baselines上提升instruction-following。
- **What It Does Not Prove:** 不证明evaluation question正确或独立，不证明8B self-evaluation无自洽偏差，不证明200k数据普遍追平instruct model，也不证明benchmark无语义近邻污染。
- **Limitations / Threats to Validity:** generator/evaluator同源、synthetic constraint可冲突、LLM-judge偏差、公开instruction contamination与单model family；later v2/venue变化不属于W06证据。
- **Trade-offs / New Failure Modes:** learned constraints提高多样性却降低形式可验证性；question rubric增强过滤但把judge version变成数据state；iterative curriculum提升难度也会累积错误；self-alignment可能闭环放大偏差。
- **Where the Previous Design Still Applies:** 格式/数值等hard constraints优先程序验证；高风险领域保留人工数据；低预算可只做SFT；judge不可靠时不能生成preference pairs。
- **Evolution Relationship:** `Direct Evolution`：handcrafted constraints→free instruction evolution→real-instruction decomposition + evaluation questions→SFT/iterative preference learning；不是用LLM judge替代所有verifier。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-SFT` Ch29、`TRAIN-DPO` Ch34与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～29、Ch34与Ch66的数据provenance、synthetic pipeline、SFT/pair objective和evaluator independence。
- **Existing Coverage:** Books 已覆盖constraint-aware synthetic data与held-out verifier；本family增加constraint→evaluation question→pair data的闭环状态，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；v2/EMNLP事实不倒灌，未修改Books。
- **Open Questions:** question correctness如何校准；constraint冲突如何检测；judge/model版本如何绑定dataset；self-alignment怎样防闭环漂移。

### Goku

- **Candidate / Week / Score:** Goku: Flow Based Video Generative Foundation Models / 2025-W06 / 23/30。
- **Source Family ID:** `goku-joint-image-video-flow-training-system`。
- **Source Type:** arXiv v1 technical report。
- **First-public Date / Revision History:** v1 2025-02-07；v2 2025-04-07；v3 2025-04-08。W06采用v1公开系统合同。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04896；https://arxiv.org/html/2502.04896v1。
- **Related Primary Sources:** rectified flow、joint image-video VAE、FlashAttention、sequence parallelism、FSDP、MegaScale、ByteCheckpoint与VBench/UCF-101只定义组件和评价。
- **Access and Verification Status:** Full Source Review Complete；v1 architecture、flow objective、image/video training stages、SP/FSDP/checkpoint/fault tolerance、data curation/balancing、evaluation与appendix已核验。
- **Full-read Coverage:** 已读3D VAE、2B/8B transformer、joint vs image/video specialization、resolution curriculum、I2V conditioning、parallelism/activation checkpoint/recovery、160M image+36M video pipeline、caption/filter/balance与T2I/T2V/I2V评测。
- **Original Problem:** image与video独立模型重复学习appearance；video全时空attention产生长sequence和显存压力；原始internet视频编码、镜头、OCR、motion与semantic分布不稳定，长训练还暴露故障/checkpoint成本。
- **Why the Previous Design Was Reasonable:** 独立image/video pipeline优化简单；latent VAE+flow transformer是成熟生成架构；data parallel与固定分辨率便于训练和调试。
- **Changed Constraint:** 希望统一image/video representation并扩到高分辨率长视频，同时让大集群训练可恢复、可保存且数据分布可控。
- **Mechanism:** 3D joint VAE把image视为T=1；shared rectified-flow transformer混合image/video minibatch，先低分辨率学习semantic-motion再逐级升分辨率；full attention结合FlashAttention+sequence parallel/FSDP，细粒度activation checkpoint、MegaScale recovery与ByteCheckpoint；data pipeline过滤/重caption/按86子类平衡。
- **State Ownership:** VAE checkpoint拥有latent identity；transformer checkpoint拥有joint flow；data catalog拥有license/source/filter/caption/tag；parallel runtime拥有shards/SP group；fault controller拥有health/restart；ByteCheckpoint拥有训练state版本。
- **Control Flow / Data Flow:** raw media→standardize/clip/filter/caption/tag/balance→joint VAE latent→resolution-stage minibatch→flow loss→SP/FSDP execution→checkpoint/recovery；I2V把首帧latent broadcast并channel concat，经MLP对齐。
- **Implementation Details:** 160M image-text（100M public+60M internal）与36M video-text（11M public+25M internal）；resolution 288×512→480×864→720×1280；full attention、FlashAttention、SP、FSDP、activation checkpoint与fault-tolerant save/load。
- **Evaluation Contract:** GenEval、DPG-Bench、MJHQ-30K、UCF-101 zero-shot与VBench；UCF-101用Tarsier-34B生成captions并由2B Goku生成13,320 videos于三分辨率，以I3D计算FVD/IS；commercial leaderboard比较非统一合同。
- **Baselines / Ablations / Sensitivity / Overhead:** 多公开/商业T2I/T2V baselines、模型size/resolution与数据阶段；报告系统优化但缺少parallel/component ablation、故障注入结果、同数据规模对照、端到端训练成本与能源。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 2B/8B与分辨率/data规模披露；GPU型号/数量、precision、tokens/frames、global batch、checkpoint时延、故障率、生成并发与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** v1报告给出joint image-video flow model所需的数据、representation、resolution curriculum和大规模训练组件的连贯系统设计，并在作者evaluation合同中达到报告结果。
- **What It Does Not Prove:** 不证明每个infra组件带来多少质量/吞吐，不证明商业模型比较公平，不证明数据授权/覆盖充分，也不证明联合训练总优于专用模型。
- **Limitations / Threats to Validity:** 大量proprietary data与未披露hardware；系统ablation不足、自动caption/tag/filter误差；benchmark与leaderboard时间点有限，安全/版权/physics failure未系统评估。
- **Trade-offs / New Failure Modes:** joint model复用appearance却产生modality/data-ratio干扰；full attention质量高但通信昂贵；SP/FSDP/checkpoint提高可扩展性也增加拓扑/恢复状态；synthetic oversampling可平衡类别同时放大生成偏差。
- **Where the Previous Design Still Applies:** 单一低分辨率任务用专用模型更简单；window/sparse attention适合更长视频；小集群不必承担复杂fault/checkpoint stack；高可信数据应优先人工治理。
- **Evolution Relationship:** `Layering / Dependency`：separate latent generators→joint image-video latent/flow→resolution/data curriculum→fault-tolerant distributed training；不是单篇benchmark驱动的替代关系。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `TRAIN-DATA` Ch27、`TRAIN-PRETRAINING` Ch28、`TRAIN-DISTRIBUTED-TRAINING` Ch36与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～24、Ch27～28、Ch36～41与Ch66的joint representation、data contract、parallel/checkpoint/recovery和evidence边界。
- **Existing Coverage:** Books 已覆盖AR/diffusion/flow分支与distributed training contract；本family提供joint visual model/data/infra共设计案例，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不保留脱离数据、分辨率与evaluator的leaderboard headline。
- **Open Questions:** image/video sampling ratio如何控制negative transfer；SP与checkpoint的真实效率是多少；data rights/provenance如何审计；生成physics如何独立评估。

### Self-Backtracking

- **Candidate / Week / Score:** Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models / 2025-W06 / 23/30。
- **Source Family ID:** `self-backtracking-learned-search-control-token`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** v1 2025-02-06；v2 2025-02-23。W06只使用v1实验。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04404；https://arxiv.org/html/2502.04404v1。
- **Related Primary Sources:** Stream of Search、GSoS、DFS/beam/BoN、DPO/RPO与Countdown只定义search、baseline和task。
- **Access and Verification Status:** Full Source Review Complete；v1 MDP framing、backtracking data/objective、inference/search、自-improvement、dataset/baselines、ablation、training details与limitations已核验。
- **Full-read Coverage:** 已读valid-state/next-action split、error trajectory construction、backtrack token、depth/breadth algorithm、expert iteration、500k Countdown data、seen/new targets、b/N/error/ratio/temperature analyses与appendix。
- **Original Problem:** external verifier/PRM搜索提高test-time reasoning但调用昂贵；纯optimal-path SFT不会学习识别错误状态和回退位置；盲目长CoT容易overthinking。
- **Why the Previous Design Was Reasonable:** beam/DFS/BoN简单且模型无须重训；external verifier可独立判断；optimal solution SFT提供干净路径并避免错误模仿。
- **Changed Constraint:** 希望模型自己发出何时/回到何处的backtrack signal，同时在inference保留breadth/depth扩展并将成功搜索轨迹反哺fast path。
- **Mechanism:** 构造与optimal问题相同的error/backtracking trajectories，以`<backtrack>`和prefix位置监督valid-state；inference在模型发token时回退到对应prefix并扩展候选；expert iteration从搜索成功轨迹构造新optimal data自改进。
- **State Ownership:** serialized trajectory拥有状态/action；backtrack token/prefix pointer拥有rollback意图；beam controller拥有实际分支、depth/breadth与budget；model checkpoint拥有learned proposal/evaluation proxy；task verifier只在数据/最终评估定义正确性。
- **Control Flow / Data Flow:** optimal+error traces→SFT/DPO-style训练→beam采样候选→model继续或发backtrack→controller恢复prefix并扩展→成功trajectory进入expert iteration→新checkpoint再评估。
- **Implementation Details:** Countdown四个numbers、target≤100；train500k且optimal/backtracking各半，seen/new target test各5k；Llama3.2-1B/3B，4×A800、DeepSpeed Stage2、FP32/BF16、128 tokens、batch16、lr1e-5、3 epochs、temperature0.7。
- **Evaluation Contract:** Countdown exact solution accuracy；比较seen/new targets、SFT greedy/beam16、DPO/RPO、DFS b32/64、SoS/GSoS与Self-Backtracking；分析branch factor、sample budget、error type、data ratio、temperature和self-improvement。
- **Baselines / Ablations / Sensitivity / Overhead:** 多search/training baselines和b/N/ratio分析；仅单算术域/短128-token轨迹，缺少external-verifier error comparison、wall-clock/token cost、rollback correctness和跨任务复验。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4×A800、1B FP32/3B BF16、length128、batch16、3 epochs披露；beam并发内存、KV rollback成本、latency/throughput与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在Countdown和作者小模型合同中，显式backtrack supervision与controller search可优于所测optimal-only和search baselines，并能用成功搜索轨迹改进后续greedy/fast behavior。
- **What It Does Not Prove:** 不证明模型internal verifier可靠、不证明无需external verifier、不证明40% headline适用于开放域，也不证明serialized prefix等价于真实环境state rollback。
- **Limitations / Threats to Validity:** 作者明确只验证Countdown且需扩到更广任务/更大模型；自动构造error、short context和exact verifier使问题远比开放域简单；compute-normalized比较有限。
- **Trade-offs / New Failure Modes:** learned backtrack减少独立verifier调用但使错误判断不可见；rollback扩展提高覆盖却增加KV/branch state；模型可过早回退或循环；expert iteration会放大搜索器偏差与数据污染。
- **Where the Previous Design Still Applies:** 有强symbolic verifier时外部search更可信；简单任务greedy最经济；真实工具side effect不可仅靠prefix rollback；高风险流程需durable checkpoint和审批。
- **Evolution Relationship:** `Direct Evolution`：optimal-path imitation→external search/verifier→learned backtrack proposal + external branch controller→expert-iteration fast path；authority没有完全内化。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79）主 owner；handoff `TRAIN-SFT` Ch29、`MODEL-KV-CACHE` Ch19、`AGENT-WORKFLOW` Ch81与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch19、Ch29、Ch66、Ch79～81的search state、rollback、training data、verifier与workflow authority。
- **Existing Coverage:** Books 已覆盖search、branch state和rollback不能撤销side effect；本family增加learned backtrack token与expert iteration分支，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把单任务40%提升外推为通用reasoner。
- **Open Questions:** prefix/KV rollback如何原子化；learned valid-state怎样校准；循环如何终止；tool side effect与branch rollback怎样对齐。

### DuoGuard

- **Candidate / Week / Score:** DuoGuard / 2025-W06 / 24/30。
- **Source Family ID:** `duoguard-minimax-generator-classifier-safety`。
- **Source Type:** arXiv v1 paper + official code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-07，题为 *DuoGuard: A Two-Player RL Framework for Multilingual LLM Guardrails*；v2 2026-06-15 改题并扩展论证。W06 只采用 v1 的问题、机制与实验合同。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.05163；https://arxiv.org/html/2502.05163v1；https://github.com/yihedeng9/DuoGuard。
- **Related Primary Sources:** LlamaGuard、ShieldGemma、DPO/RPO 与所用六组 safety benchmarks 只定义 baseline、训练算子和 evaluation dependency。
- **Access and Verification Status:** Full Source Review Complete；v1 minimax formulation、data generation/filtering、classifier/generator update、training setup、multilingual evaluation、ablation 与 limitations 已核验，并与 2026 v2 隔离。
- **Full-read Coverage:** 已读 Abstract、Introduction、related work、two-player objective、synthetic preference construction、classifier retraining、实验数据/模型/超参、六组 benchmark、filtering ablation、效率比较、appendix 与公开代码说明。
- **Original Problem:** guard model 依赖固定人工 safety data，难覆盖多语言和不断变化的攻击；单向 adversarial generation 又可能只产生容易、重复或偏离 taxonomy 的样本。
- **Why the Previous Design Was Reasonable:** 静态监督数据便于审计、复现和控制类别分布；独立 classifier 小而快；人工或固定 red-team corpus 在 threat model 稳定时成本可控。
- **Changed Constraint:** 多语言输入和攻击分布持续变化，需要让 generator 主动寻找当前 classifier 的薄弱区域，同时避免把低质量、自相矛盾或明显拒答文本直接回灌训练。
- **Mechanism:** generator 依据 safety category 生成每题八个多语言 safe/unsafe 变体，当前 classifier 选择误分类样本；generator 自评分、长度差与拒答短语过滤形成 preference levels，再以 DPO/RPO 风格更新 generator；classifier 每轮在累积对抗数据上从头训练，构成近似 minimax 交替优化。
- **State Ownership:** safety taxonomy 和 seed corpus 拥有 policy meaning；generator checkpoint 拥有攻击分布；classifier checkpoint 拥有当前判定边界；filter/rating 规则拥有 admission gate；benchmark translation 拥有语言映射误差。
- **Control Flow / Data Flow:** multilingual seeds/category→generator 采样 safe/unsafe variants→self-rating/length/refusal filter→classifier 找 misclassified cases→构造 preference pairs 更新 generator→累积数据从头训练 classifier→六组 benchmark 重评。
- **Implementation Details:** v1 使用 dolphin-2.9.4-llama3.1-8b 作为 generator、Qwen2.5-0.5B 加 binary/multilabel head 作为 classifier，覆盖 12 类 harmful taxonomy；种子以英语为主，并含法语、西语和德语；训练使用 bf16/AdamW，附录分别披露 classifier 与 generator 的 learning rate、batch、gradient accumulation、epoch 和 DPO/RPO 参数。
- **Evaluation Contract:** 在 XSTest、ToxicChat、OpenAI Moderation、BeaverTails、RTP-LX、XSafety 上以 F1 比较 guard models；前四组被翻译用于多语言评测；作者另测单输入 latency，但未披露完整 batching/concurrency/serving SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 LlamaGuard3、ShieldGemma 等 guard baselines，并检查 filtered/unfiltered synthetic data 与交替轮次；generator sampling、翻译、self-rating 和 classifier 重训的总成本没有形成端到端 production overhead 合同。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100 80GB cluster、8B generator、0.5B classifier、bf16 与部分训练 batch/length 已披露；cluster 数量、完整 inference batch/concurrency、P95/P99、不同语言 token length 与 release SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者四语数据和六组 benchmark 合同中，generator/classifier 交替与质量过滤能持续暴露当前 guard 的误分类区域，并改善所测平均 F1；小 classifier 在作者单输入设置中比所测 8B guard 更快。
- **What It Does Not Prove:** 不证明 minimax neural game 收敛到通用安全、不证明四语结果覆盖 29 种基础语言、不证明翻译 benchmark 等价原生攻击，也不证明作者 latency 数字可外推到多租户 serving。
- **Limitations / Threats to Validity:** 英语种子占比高、翻译与 self-rating 可能共享 generator 偏差、taxonomy 只覆盖已知类别、F1 隐含 operating point，且公开实验不能覆盖 adaptive deployment attacker。
- **Trade-offs / New Failure Modes:** 自适应 red-team 提升覆盖却引入 generator/classifier 共适应、synthetic collapse、filter blind spot、类别漂移、false-positive 成本和昂贵的迭代重训；更小 classifier 也可能牺牲开放域鲁棒性。
- **Where the Previous Design Still Applies:** 固定 threat model、强审计要求或低更新频率时，人工 curated data 与静态 guard 更易治理；高风险场景仍需规则、policy engine、human review 与多层 defense，而不是单一 learned classifier。
- **Evolution Relationship:** `Direct Evolution`：静态 guard data→单向 adversarial augmentation→generator/classifier 交替 minimax→带质量 gate 的持续 safety-data lifecycle；与 runtime policy enforcement 是 `Layering / Dependency`。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `TRAIN-DATA` Ch27、`TRAIN-RLHF` Ch31、`TRAIN-DPO` Ch34与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch27、Ch31、Ch34、Ch66 与 Ch71～73 的 data provenance、preference objective、operating point、tenant policy 和 release evidence 边界。
- **Existing Coverage:** Books 已覆盖 threat model、policy taxonomy 与 evaluator contract；本 family 增加持续 adversarial data/guard 共演化机制，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把作者平均 F1、单输入 latency 或 2026 v2 理论表述写成 2025 通用事实。
- **Open Questions:** classifier/generator 版本如何与 policy taxonomy 联合发布；native multilingual red-team 怎样替代翻译；false-positive operating point 如何按租户校准；持续训练怎样防止旧攻击遗忘。

### Generating Symbolic World Models via Test-time Scaling

- **Candidate / Week / Score:** Symbolic World Models via Test-time Scaling / 2025-W06 / 23/30。
- **Source Family ID:** `symbolic-world-model-pddl-test-time-scaling`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-07；v2 2025-05-08，后续进入 TMLR。W06 使用 v1 的方法与实验版本。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04728；https://arxiv.org/html/2502.04728v1。
- **Related Primary Sources:** PDDL、VAL、A*、IPC domains、NL2Domain/Prob2Domain 与 Qwen/Llama/GPT baselines 定义 symbolic representation、validator、planner 与 comparison dependency。
- **Access and Verification Status:** Full Source Review Complete；v1 task formalization、BoN ranking、iVML refinement、PDDL validation/planning、dataset、模型比较、scaling curves、failure analysis 与 limitations 已核验。
- **Full-read Coverage:** 已读 Abstract、Introduction、background/related work、NL/Problem-to-Domain pipeline、BoN 与 iVML algorithm、validator/planner loop、283/332 domain tasks、model/scale comparisons、结果、错误类型、appendix prompts 与 examples。
- **Original Problem:** 从自然语言或有限 problem instances 手写 PDDL domain 成本高；LLM 单次生成容易产生语法合法但语义错误、漏 predicate/action 或不可规划的 world model。
- **Why the Previous Design Was Reasonable:** 人工 symbolic model 可解释、可验证并能复用成熟 planner；单次 LLM translation 成本低，适合简单 domain 或有人审阅的辅助建模。
- **Changed Constraint:** domain 数量与复杂度增长，希望用 inference compute 而非重新训练来提高完整 symbolic model 的成功率，并让 executable validator/planner 参与选择。
- **Mechanism:** 对同一描述采样 N 个完整 PDDL candidates，以 token log-likelihood 排序保留 K 个；iVML 让模型对候选和验证反馈进行 verbalized critique/refinement，随后用 VAL 做语法/一致性校验并以 A* 检查问题可解性。
- **State Ownership:** natural-language specification 拥有意图但可能含歧义；PDDL candidate 拥有显式 transition schema；VAL 拥有语法/类型合法性；planner 拥有在给定 problem 下的可达性证据；LLM critique 只拥有 proposal，不拥有最终真实性。
- **Control Flow / Data Flow:** domain description/problems→LLM 采样 PDDL→log-likelihood rank→iVML critique/refine 多轮→VAL validate→A* solve associated problems→选择通过 candidate 或报告 failure。
- **Implementation Details:** v1 在 IPC 衍生的 283 个 NL2Domain 与 332 个 Prob2Domain cases 上测试 Qwen2.5 0.5B～72B、coder variants、Llama3.1、Yi、GPT-4o/o1；Qwen zero-shot temperature 0.7，BoN-8，iVML-5，并使用 PDDL/VAL/A* 工具链。
- **Evaluation Contract:** 成功要求生成完整 PDDL domain，能够通过 validator 并使关联 problems 被 planner 求解；比较 model scale、直接生成、BoN 与 iVML+BoN，结果只绑定这些 domain descriptions/problems 与 planner contract。
- **Baselines / Ablations / Sensitivity / Overhead:** 扫模型规模、BoN sample 数与 iVML iterations，并比较直接生成/采样选择/迭代 refinement；多候选 token 成本、validator/planner wall time 与 failure retry 增长，但未给 production latency/SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 模型家族、BoN-8、iVML-5 和 task 数披露；硬件、precision、prompt/output length 分布、batch、并发、token cost、P95/P99 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 PDDL 数据与 executable validation 合同中，增加采样并用 verbalized refinement/工具校验能显著提高若干模型生成可规划 domain 的成功率。
- **What It Does Not Prove:** 不证明生成 domain 与人类真实意图语义等价，不证明 PDDL 能表示开放世界、连续动力学或部分可观测环境，也不证明 test-time scaling 始终优于人工建模或专门训练。
- **Limitations / Threats to Validity:** fully observable、deterministic symbolic worlds，动作执行无噪声；validator 只查形式约束，关联 problems 覆盖有限，LLM 可能生成能过测试却语义错误的 domain；硬件/成本合同不完整。
- **Trade-offs / New Failure Modes:** 显式 model 带来可验证规划，却引入 specification gap、test-suite overfitting、candidate-selection bias 和采样成本；更多 refinement 也可能稳定地修饰错误 ontology。
- **Where the Previous Design Still Applies:** 小而稳定的 safety-critical domain 仍适合专家手写/审计 PDDL；连续、随机或隐状态环境需要 learned dynamics、simulator 或 belief-state model；简单任务直接 tool plan 更经济。
- **Evolution Relationship:** `Layering / Dependency`：natural-language task→显式 symbolic transition model→validator/planner→test-time candidate/refinement scaling；与 learned latent world model 是 `Alternative Branch`，不是替代关系。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `AGENT-PLANNING` Ch79与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch25～26、Ch66 与 Ch79～81 的 environment state、transition authority、planner/verifier、workflow state 和 real-observation boundary。
- **Existing Coverage:** Books 已区分生成、predictive、causal/controllable world model；本 family 增加显式 symbolic world model 与 executable planning-evidence 分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把 v1 成功率外推到真实环境，也不把后续 TMLR revision 当作本周新事件。
- **Open Questions:** 如何检测“可规划但语义错误”；有限 problem set 能否形成充分 specification test；symbolic/learned state 如何互相校准；planner cost 如何纳入 agent SLO。

### CMoE / Fast Carving of Mixture-of-Experts

- **Candidate / Week / Score:** CMoE / 2025-W06 / 24/30。
- **Source Family ID:** `cmoe-dense-ffn-activation-carving`。
- **Source Type:** arXiv v1 paper + official code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-06，题为 *CMoE: Fast Carving of Mixture-of-Experts for Efficient LLM Inference*；v2 2025-05-24；v3 2026-04-23 改题为 *Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis*。W06 隔离 later title/result bleed。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04416；https://arxiv.org/html/2502.04416v1；https://github.com/JarvisPei/CMoE。
- **Related Primary Sources:** LLaMA-MoE、MoEfication、sparse FFN、activation sparsity、LoRA 与 load-balancing literature 只定义前代和 comparison branch。
- **Access and Verification Status:** Full Source Review Complete；v1 activation analysis、ATopK、shared/routed expert carving、analytical router、optional adaptation、load balancing、evaluation、ablation、hardware 与代码合同已核验。
- **Full-read Coverage:** 已读 Abstract/Introduction/related work、neuron activation profile、shared-expert selection、balanced clustering/assignment、router construction、scale/bias adaptation、PPL/downstream evaluation、sparsity sensitivity、calibration/fine-tuning 和 appendix。
- **Original Problem:** 预训练 dense FFN 每 token 激活全部 neurons；从零训练 MoE 或蒸馏成本高，简单剪枝又破坏已学能力。希望把已有 dense checkpoint 重构成条件计算，而非重训完整模型。
- **Why the Previous Design Was Reasonable:** dense FFN 路径固定、质量稳定、kernel 和 checkpoint 简单；训练原生 MoE 可共同学习 experts/router；静态 pruning 在 workload 稳定且压缩率温和场景易部署。
- **Changed Constraint:** 已有 dense LLM 的推理成本成为瓶颈，需要少量 calibration 和可选轻量适配，将 neuron-level activation sparsity转化为 shared/routed expert execution。
- **Mechanism:** 用少量 calibration 统计 ATopK neuron activation；高频 neurons 组成 shared experts，其余按共同激活关系做 balanced K-means/linear assignment形成 routed experts；代表 neurons/activation statistics 构造 analytical router，并可学习 scale 与 auxiliary-loss-free balancing bias 做轻量适配。
- **State Ownership:** dense FFN weights 保留知识；activation profile 拥有 workload-specific carving evidence；expert partition 拥有 neuron placement；router 拥有 token dispatch；shared experts 提供常驻容量；balancing bias 拥有 runtime load correction。
- **Control Flow / Data Flow:** calibration tokens→记录 neuron activation/co-activation→选择 shared neurons→balanced cluster routed experts→构造 router→token 执行 shared+top routed experts→可选 LoRA/scale/bias adaptation→测质量和 active ratio。
- **Implementation Details:** v1 处理 Llama2-7B/Llama3-8B；使用 8 个长度 2048 calibration examples；可选 2048 samples、1 epoch Adam/LoRA rank 8 alpha 32 的轻量适配；作者代码给出 carving、router 与 evaluation pipeline。
- **Evaluation Contract:** WikiText-2/C4 perplexity，以及 BoolQ、PIQA、SciQ、WinoGrande、ARC-C、HellaSwag accuracy；比较 dense、LLaMA-MoE 和不同 active ratio，在单 H800 PCIe 80GB/CUDA 12.6 上报告部分 inference 行为。
- **Baselines / Ablations / Sensitivity / Overhead:** 检查 shared/routed split、router/adaptation 与 activation ratio；高 sparsity 下 PPL/accuracy 明显下降；v1 没有在真实 expert-parallel All-to-All、多请求 batching 或 production SLO 下证明端到端 speedup。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 单 H800 PCIe 80GB、Llama2-7B/Llama3-8B、calibration length 2048 与 CUDA 12.6 披露；inference precision、batch/concurrency、network topology、P95/P99、memory cap 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者两类 dense checkpoint 和文本任务合同中，activation-guided carving 能在无需 full retraining 的情况下形成可执行 shared/routed expert 结构，并呈现 active ratio 与质量的连续 trade-off。
- **What It Does Not Prove:** 不证明 dense-to-MoE 总能提速、不证明 analytical router 等价联合训练 router、不证明在 expert parallel、长上下文或不同 domain 保持 partition，也不证明后续 revision 的 headline 属于 v1。
- **Limitations / Threats to Validity:** 两个相近模型族、极小 calibration、单 GPU、有限 PPL/task suite、缺少 topology/communication cost；activation distribution drift 会使 partition/router 失配。
- **Trade-offs / New Failure Modes:** 减少 active neurons 换来 calibration/profile state、router error、expert imbalance、shared expert hot spot、fragmented kernels 和 distributed All-to-All；更低 active ratio 会快速损失质量。
- **Where the Previous Design Still Applies:** dense FFN 适合小 batch、固定低延迟和硬件不善于 sparse dispatch；原生 MoE 适合可承担预训练并需大总容量；静态 pruning 适合模型/工作负载长期固定。
- **Evolution Relationship:** `Alternative Branch`：dense FFN→static pruning / native MoE→activation-guided dense-to-MoE carving→可选轻量 router adaptation；不是原生 MoE 的通用替代。
- **ROADMAP Node:** `MODEL-MOE`（Ch21）主 owner；handoff `MODEL-FFN` Ch16、`INFER-TENSORRT-LLM` Ch49与`INFER-SCHEDULING` Ch56。
- **Target and Adjacent Chapters Read:** 已核对 Ch16、Ch21、Ch36～37、Ch49 与 Ch56 的 FFN semantics、router/dispatch、expert placement、communication 和 scheduling 边界。
- **Existing Coverage:** Books 已覆盖 router、active/total parameters、load balance 与 All-to-All；本 family 增加 post-hoc dense checkpoint carving 分支，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不保留脱离 active ratio、model、hardware 与 communication contract 的速度 headline。
- **Open Questions:** calibration drift 如何触发 re-carving；expert partition 怎样写入 model artifact；分布式 placement 如何避免 shared hot spot；router adaptation 是否破坏原 dense behavior。

### CodeSteer

- **Candidate / Week / Score:** CodeSteer / 2025-W06 / 23/30。
- **Source Family ID:** `codesteer-code-text-mode-steering-symbolic-tasks`。
- **Source Type:** arXiv v1 identity + official full publication + author code/model/data artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-02-04；v2 2025-05-29；后续发表于 ICML/PMLR。W06 event 归属 v1，后续正式全文只用于闭合机制与实验，不改变 first-public date。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.04350；https://proceedings.mlr.press/v267/chen25x.html；https://github.com/yongchao98/CodeSteer-v1.0。
- **Related Primary Sources:** SymBench、TaskLLM APIs、code interpreter、SFT/DPO 与 symbolic checker 依赖定义 task、execution environment 和 training operators。
- **Access and Verification Status:** Full Source Review Complete；arXiv v1 identity/revision、official PMLR full paper、author repository/model/data artifacts中的 steering loop、training trajectory、checker、37-task evaluation、ablation 与 limitations 已核验；事件时 v1 PDF/HTML transport gap 明确记录。
- **Full-read Coverage:** 已读 Abstract、Introduction/related work、CodeSteerLLM interaction protocol、code/text selection、self-answer/symbolic checkers、SymBench、trajectory construction、SFT/DPO setup、model/task baselines、generalization、hardware/cost与component ablations。
- **Original Problem:** LLM 在 symbolic tasks 上有时应直接语言推理，有时应生成/执行代码；固定 prompt 或单次模式选择不能随中间失败切换，纯 code 也会被不必要实现和执行错误拖累。
- **Why the Previous Design Was Reasonable:** text-only reasoning 无 sandbox 风险且对小题直接；always-code 提供可执行精确性；人工 routing 或单 prompt 在任务类型稳定时简单、成本可预测。
- **Changed Constraint:** task complexity、model capability 与中间答案质量随轮次变化，需要一个较小 controller 观察完整 history，动态要求 TaskLLM 使用 code/text、修正或结束，并以 executable checks 提供反馈。
- **Mechanism:** CodeSteerLLM 每轮读取问题、历史与当前答案，发出 code/text steering prompt 或 final decision；TaskLLM 重新作答。self-answer checker 再让 TaskLLM 生成并执行验证代码，symbolic checker 规则化分析循环、搜索、数值和组合复杂度，反馈下一轮是否换策略。
- **State Ownership:** TaskLLM 拥有候选解答；CodeSteerLLM 拥有 mode/continuation proposal；conversation history 拥有迭代状态；sandbox 拥有代码 side effects/result；checker 拥有局部可执行证据但不等于真实世界 authority；outer loop 拥有 stop/budget。
- **Control Flow / Data Flow:** task→steerer 选择 text/code prompt→TaskLLM answer/code→sandbox执行→self-answer/symbolic checks→结果回到 steerer→继续、换模式或 finalize；成功轨迹进入 SFT，偏好 pair 进入 DPO。
- **Implementation Details:** SymBench 含 37 类 adjustable-complexity symbolic tasks（28 seen、9 unseen）；构造 12,043 条 SFT success trajectories 与 5,480 个 DPO pairs；Llama3.1-8B full fine-tuning，SFT 10 epochs、lr 1e-5，DPO 6 epochs、lr 5e-6、beta 0.1、batch 4。
- **Evaluation Contract:** 以 37 个 symbolic task 的 executable/task-specific success 比较 base TaskLLM、prompt agent、o1/DeepSeek 等 baselines和 CodeSteer variants；closed APIs 固定为作者当时版本，结果不等价开放域 agent correctness。
- **Baselines / Ablations / Sensitivity / Overhead:** 消融 DPO、data augmentation、symbolic checker、self-answer checker 与 trained vs prompt steerer；每轮增加 controller/API/checker/sandbox 调用，论文报告任务成功但没有完整 token、latency、cost、failure-recovery SLO。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 4×H100 80GB 用于训练，通常 1×H100 推理并有 4-GPU hardware comparison；8B steerer、训练 epochs/batch披露；precision、完整上下文/输出长度、API concurrency、P95/P99 与 production SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 SymBench 和所测 TaskLLMs 中，受训练的多轮 mode controller 加 executable/checker feedback 比固定 text/code 与若干 prompt/training ablation 取得更高任务成功率。
- **What It Does Not Prove:** 不证明 controller 学到通用 planning、不证明 checker 能检测语义/安全错误、不证明 arbitrary code execution 可安全生产化，也不证明 closed-model headline 可跨版本复现。
- **Limitations / Threats to Validity:** synthetic symbolic suite、seen/unseen task族仍相近、checker与task可能共享 blind spot、API版本漂移、code sandbox安全和额外调用成本；repo-scale、真实 side effect、长时 workflow 未验证。
- **Trade-offs / New Failure Modes:** 动态选模式提高适配性，却增加 controller误导、history膨胀、checker false confidence、sandbox escape、non-determinism、重复调用成本和 stop-loop failure。
- **Where the Previous Design Still Applies:** 简单可判定任务固定 text/code 更快；高风险环境应使用 typed tools 而非自由代码；已有可靠 planner/router 时不必训练独立 steerer；不可回滚 side effect 需要 durable workflow/approval。
- **Evolution Relationship:** `Direct Evolution`：fixed text or code mode→prompt routing→trained multi-turn mode controller→checker/sandbox feedback loop；与 durable workflow 是 `Layering / Dependency`。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79）主 owner；handoff `AGENT-TOOL-CALLING` Ch78、`AGENT-REFLECTION` Ch80、`AGENT-WORKFLOW` Ch81与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch66 与 Ch78～81 的 tool proposal、planner state、verifier authority、sandbox side effect、stop condition 和 durable recovery 边界。
- **Existing Coverage:** Books 已覆盖 planning/tool/reflection/workflow 责任分离；本 family 增加 code/text execution-mode steering 的受限 controller 案例，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不把 PMLR 后续发布时间当事件日，也不把作者 benchmark 提升外推为通用 agent 能力。
- **Open Questions:** steerer 与 TaskLLM 版本如何联合校准；checker disagreement 如何升级；sandbox权限怎样最小化；mode switching 如何纳入 token/latency budget和durable trace。

### VectorQ / Adaptive Semantic Prompt Caching

- **Candidate / Week / Score:** VectorQ / Adaptive Semantic Prompt Caching / 2025-W06 / 26/30。
- **Source Family ID:** `vectorq-adaptive-semantic-prompt-cache`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-06，题为 *Adaptive Semantic Prompt Caching with VectorQ*；v2 2025-04-04、v3 2025-05-27、v4 2025-09-26，v5 2026-02-21 改题为 *vCache: Verified Semantic Prompt Caching*。W06 只采用 v1，later formal guarantees 不倒灌。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.03771；https://arxiv.org/html/2502.03771v1。
- **Related Primary Sources:** semantic cache、vector search、Bayesian posterior sampling、HNSWLIB、gte-large-en-v1.5、Llama3.1-8B 与五组 datasets 定义前代、index、model和evaluation dependency。
- **Access and Verification Status:** Full Source Review Complete；v1 cache state、三段区域、posterior/re-evaluation policy、算法、correctness definition、datasets、hardware、threshold/uncertainty experiments 与 limitations 已核验，并隔离 v2-v5。
- **Full-read Coverage:** 已读 Abstract、Introduction/related work、static semantic cache failure、VectorQ entry schema、Incorrect/Uncertain/Correct regions、Bayesian update/re-evaluation、convergence intuition、五组 workload、implementation、hit/error/latency evaluation 和 sensitivity。
- **Original Problem:** 固定 cosine threshold 的 semantic cache 将“相似 prompt”直接视为“同一答案”，阈值过低产生错误复用，过高又失去 hit；不同 query/domain 的 embedding neighborhood 可靠性并不一致。
- **Why the Previous Design Was Reasonable:** exact cache correctness清楚但 hit 低；static semantic threshold无训练、实现简单，在模型温度低、domain窄且错误成本可接受时能节省重复生成。
- **Changed Constraint:** 希望在不预先知道全局最优阈值的情况下，让每个 cached embedding 从 fresh-LLM comparison 学习自己的安全复用区域，并允许用户调节 error/hit trade-off。
- **Mechanism:** 每个 vector entry 存 prompt embedding、response、Incorrect/Uncertain/Correct 三段距离边界与 posterior；nearest-neighbor 后，Incorrect miss、Uncertain 强制 fresh re-evaluation、Correct 按 posterior 概率抽查；比较 cached/fresh response 后收缩/扩展区域并更新信念，错误区域单调扩大，最坏退回 exact match。
- **State Ownership:** model/version+generation config 拥有 response semantics；embedding model/index 拥有 neighbor identity；cache entry 拥有 response和局部边界/posterior；uncertainty gate 拥有 operating point；fresh LLM call 是当前 comparison authority。
- **Control Flow / Data Flow:** prompt→embedding→HNSW nearest entry/cosine distance→按三段区域 hit/miss/re-evaluate→必要时 fresh LLM→字符级比较→更新 entry boundary/posterior→返回 cached 或 fresh response。
- **Implementation Details:** GCP N1 instance，f1-micro CPU + T4 16GB；Llama3.1-8B via Ollama、temperature 0；gte-large-en-v1.5 embeddings、HNSWLIB/cosine；在 E-Commerce classification、CommonsenseQA、Amazon Instant Video reviews、ComQA 与 combined benchmark 上每设置约 600 entries。
- **Evaluation Contract:** correctness 定义为 deterministic temperature-0 条件下 cached response 与 fresh LLM 输出字符完全一致；测 cache hit、error 和请求 latency，并扫 static threshold 与 VectorQ uncertainty gate。它不是 semantic truth 或 human preference evaluator。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 exact/static semantic cache 与不同 threshold/gate；报告的最高 hit/error 改善绑定这五组workload、单模型/embedding；index lookup、posterior update很小，但 warm-up/re-evaluation和多租户一致性未完整评估。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** N1 CPU、T4 16GB、Llama3.1-8B、temperature 0、embedding/index披露；precision、prompt/output length、batch、并发、cache size/TTL、P95/P99 与 tenant SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 deterministic 单模型工作负载中，per-entry adaptive region 和 probabilistic verification可比固定全局 threshold 提供更可控的 hit/error trade-off，并在错误累积时趋向保守复用。
- **What It Does Not Prove:** 不证明字符相同等于语义正确、不证明 stochastic sampling/模型升级后仍有效、不证明所有 embedding/domain 的局部边界稳定，也不证明作者峰值 12×/92% 可跨 workload 外推。
- **Limitations / Threats to Validity:** 单模型、单embedding、单GPU、低并发与窄数据；exact-string metric、温度0、无 tenant/privacy/TTL/model revision、embedding drift、adversarial collision 和 distributed invalidation。
- **Trade-offs / New Failure Modes:** adaptive verification降低静默错误却引入 warm-up miss、posterior state、抽查成本、non-stationary drift、poisoned neighborhood、cache isolation和失效传播；更保守 gate 会退化为低 hit。
- **Where the Previous Design Still Applies:** exact cache适合严格相同请求；static threshold适合低风险稳定 domain；KV/prefix cache适合相同 token prefix且保持exact computation；高风险回答应始终重新推理/验证。
- **Evolution Relationship:** `Direct Evolution`：exact response cache→global-threshold semantic cache→per-entry adaptive boundary→probabilistic verification；与 token-prefix/KV cache 是 `Alternative Branch`，不可混为同一 correctness contract。
- **ROADMAP Node:** `PLATFORM-GATEWAY`（Ch62）主 owner；handoff `INFER-REQUEST-LIFECYCLE` Ch42、`PLATFORM-EVALUATION-SYSTEM` Ch66与`PLATFORM-MULTI-TENANCY` Ch71。
- **Target and Adjacent Chapters Read:** 已核对 Ch42、Ch45、Ch59、Ch62、Ch66 与 Ch71 的 request/model identity、exact KV semantics、gateway cache、evidence与tenant isolation边界。
- **Existing Coverage:** Books 覆盖 prefix/KV reuse identity 与 gateway policy；本 family 增加 semantic response cache 的 adaptive verification branch，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06；不导入 v2-v5 guarantees，也不把 semantic response cache写成 KV cache。
- **Open Questions:** model/embedding revision如何原子失效；不同tenant能否共享posterior；stochastic output如何定义correctness；poisoning和privacy如何进入admission policy。

### Gemini 2.0 Flash GA / Flash-Lite Preview

- **Candidate / Week / Score:** Gemini 2.0 Flash GA / Flash-Lite Preview / 2025-W06 / 20/30。
- **Source Family ID:** `gemini-2-0-flash-ga-flash-lite-preview-2025-02`。
- **Source Type:** official model release announcement + later official model card for revision context。
- **First-public Date / Revision History:** 2025-02-05：Gemini 2.0 Flash API general availability、Flash-Lite public preview与 Pro experimental update；Gemini 2.0 Flash model card 后于 2025-04-15 更新。W06 只把 2月5日 release node 计为事件。
- **Direct Primary Sources:** https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-updates-february-2025/。
- **Related Primary Sources:** https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-0-Flash-Model-Card.pdf；later API/model lifecycle documentation 只用于 revision/deprecation context，不反推 launch-day mechanism。
- **Access and Verification Status:** Full Source Review Complete — `Weekly Only / Version Fact / Mechanism Not Disclosed`；官方 announcement 的 availability、modalities、context/capability statements 与后续 model-card evidence boundary 已核验。
- **Full-read Coverage:** 已读官方 2月5日发布全文、产品/开发者 availability、Flash/Flash-Lite/Pro定位、公开 modality/context/tool statements及later model card的scope、evaluation/safety说明；没有公开architecture/training/runtime可供机制全文审计。
- **Original Problem:** Gemini 2.0 experimental family 需要稳定 API release、低成本型号和面向高复杂度任务的实验型号，使开发者能选择质量、context 和 price/latency tier。
- **Why the Previous Design Was Reasonable:** experimental endpoint允许快速迭代和反馈；单一旗舰型号减少能力矩阵/版本治理；模型内部设计不公开可保护实现并避免把产品接口绑定到特定架构。
- **Changed Constraint:** 开发者需要 production-available Flash、成本更低的 Flash-Lite preview和更大 context/更强能力的 Pro experimental，同时要求明确的 endpoint/version/status 边界。
- **Mechanism:** `Not Disclosed`。官方材料公开的是 model family、API/AI Studio/Vertex AI availability、输入/输出 modality、context 与部分 tool/capability contract，没有披露网络结构、训练 recipe、serving topology、cache、router 或 scheduler。
- **State Ownership:** Google 拥有服务端 model alias/version与endpoint lifecycle；customer deployment拥有选定model ID、region、prompt/tool policy；API contract拥有公开 capability；内部 weights/runtime state `Not Disclosed`。
- **Control Flow / Data Flow:** client选择endpoint/model→提交公开支持的 multimodal input→Google-managed service执行未披露模型/runtime→返回text/tool-related output；preview/experimental/GA状态决定兼容性和变更风险。
- **Implementation Details:** announcement 声明 Flash GA 可通过 Gemini API、Google AI Studio 与 Vertex AI 使用，Flash-Lite 为 public preview；Flash 支持 multimodal input/text output并公开 1M context，Pro experimental另公开更大context与部分tools。内部实现 `Not Disclosed`。
- **Evaluation Contract:** announcement/model card提供厂商 benchmark/safety evaluation，但完整hardware、serving path、prompt/output distribution、并发、precision与SLO不足，故本审计不保留脱离条件的 leaderboard 数字。
- **Baselines / Ablations / Sensitivity / Overhead:** official release没有可审计 architecture/training/runtime ablation；不同 family tier 的price/quality positioning是产品声明，不是机制归因。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 公开 model family、部分 context/modalities；hardware、parameter count、precision/quantization、batch、concurrency、cache、P95/P99和服务内部SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 2025-02-05 官方已将 Gemini 2.0 Flash 推为 API GA，并提供 Flash-Lite preview 与 Pro experimental family node；开发者可据公开接口管理能力和release-stage选择。
- **What It Does Not Prove:** 不证明任何内部模型/训练/推理机制，不证明厂商 benchmark 对目标 workload成立，也不证明 GA 意味着固定alias、长期可用或跨区域相同性能。
- **Limitations / Threats to Validity:** 主要来源是产品公告；model card晚于事件日；内部机制、硬件、runtime与完整SLO未披露，后续alias/deprecation会改变当前可用性但不能改写历史事件。
- **Trade-offs / New Failure Modes:** managed GA降低自运维成本却增加provider dependency、alias/version drift、区域/配额差异、数据治理和不可观测内部failure；preview低成本tier带来兼容性和质量变动风险。
- **Where the Previous Design Still Applies:** self-hosted/open-weight model适合要求可审计weights/runtime和离线部署；固定version endpoint适合严格复现；experimental endpoint适合早期探索但不应直接承担关键SLO。
- **Evolution Relationship:** `Layering / Dependency`：experimental model family→GA/preview/experimental product tiers→versioned deployment contract；这是发布治理演进，不是模型架构演进。
- **ROADMAP Node:** `PLATFORM-MODEL-REGISTRY`（Ch59）主 owner；handoff `PLATFORM-AI-PLATFORM` Ch57、`PLATFORM-MODEL-SERVING` Ch61、`PLATFORM-EVALUATION-SYSTEM` Ch66与`PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch57～62、Ch66 与 Ch72 的 immutable artifact identity、managed endpoint、capability contract、release evidence与security boundary。
- **Existing Coverage:** Books 已覆盖 model/version/serving contract；本 node 只提供版本事实，没有新增长期机制，Books 阶段应按 `Weekly Only` 去重。
- **Integration Decision:** `Books Pending — Integration Deferred；Weekly Only / Version Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 仅更新 W06；因内部 mechanism 与 workload contract 未披露，不进入机制正文，也不将后续 model card 当 launch-day source。
- **Open Questions:** model alias是否可长期复现；preview→GA时capability/evaluator如何迁移；managed endpoint需保留哪些外部evidence以支持release gate。

### MAGA / Massive Genre-Audience Reformulation to Pretraining Corpus Expansion

- **Candidate / Week / Score:** MGA / Pretraining Data Reformulation / 2025-W06 / 28/30。
- **Source Family ID:** `maga-genre-audience-pretraining-corpus-expansion`。
- **Source Type:** arXiv v1 research paper + author dataset/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-06；v2 2025-05-19。W06 只使用 v1 的标题、方法与实验合同，v2 仅用于识别同一 Source Family。
- **Direct Primary Sources:** https://arxiv.org/html/2502.04235v1；https://arxiv.org/abs/2502.04235；https://huggingface.co/datasets/bytedance-research/MAGACorpus。
- **Related Primary Sources:** SmolLM-Corpus/FineWeb-Edu 原始数据说明与作者附录中的 tool-model、resource、pretraining 配置；后续 ByteDance-Seed artifact 只作 revision lineage。
- **Access and Verification Status:** Full Source Review Complete；v1 Method、training/evaluation、prompt ablations、collapse analysis、limitations、tool implementation、resource analysis 与 prompts 已核验。
- **Full-read Coverage:** 已读 metadata/revision、Introduction/Related Work、两阶段 reformulation/cleaning、134M～13B pretraining、500B/700B budget experiments、validation-loss analysis、strict/relaxed prompt ablations、appendix resource/model/evaluation/prompts。
- **Original Problem:** 高质量自然文本增长慢于模型与训练 token 预算；简单重复只能在有限 epoch 内维持效率，依赖大模型或复杂 seed 系统的 synthesis 又难以扩展。
- **Why the Previous Design Was Reasonable:** 过滤真实 Web 数据保留真实分布和 provenance；有限重复无需引入生成偏差；大 teacher 与人工 seed 能直接控制质量，在数据预算较小时更稳健。
- **Changed Constraint:** 训练预算扩大到数百 B/万亿 token，而高质量 unique tokens 受限；需要把已有文档转换成更多表达分布，同时控制生成、判断与清洗成本。
- **Mechanism:** 对每篇原文先生成五组 genre-audience pair，再按 pair 重写；以允许表达变化但要求仍可追溯原文的 Limited Consistency 评分筛选，最后以启发式清理高频模板与低关键词覆盖样本。LLM labeler/judger 蒸馏成 W8A8 task-specific 3.3B MoE tool models执行大规模生成。
- **State Ownership:** 原文与 provenance 拥有知识来源；genre-audience pair 拥有变换意图；labeler/judger 与 Limited Consistency 拥有接受策略；cleaner 拥有模板/覆盖规则；dataset recipe 拥有真实与 synthetic token mixing/epoch contract。
- **Control Flow / Data Flow:** 195B FineWeb-Edu-dedup 文档→LLM 生成 pair/判断样本→训练量化 SLM tools→每文档五路 reformulation→score/heuristic cleaning→770B MAGACorpus→按 Baseline/MAGA-Only/MAGA-Mix 或 budget recipe 训练。
- **Implementation Details:** 作者披露 3.3B MoE tools、W8A8、五路 reformulation、Llama3-style 134M/377M/1.7B/7B/13B models、WSD 0.1% warmup/75% stable/25% decay；生成两阶段分别约 `256×64` 与 `1024×130` H100 GPU-hours，Ascend 910B2 约需四倍时长。
- **Evaluation Contract:** 134M/377M/1.7B 最多训练 1T tokens，并以 LightEval 的 ARC、HellaSwag、WinoGrande、MMLU、GSM8K 等评测；另在 500B 与 700B token budget 下比较 repetition、upsampling 与 MAGA expansion，较大模型延伸至 13B。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较原 corpus、MAGA-Only、MAGA-Mix、Full-FineWeb-Edu、Upsample-EDU；strict prompt 保真但限制变化，relaxed prompt 在 MAGA-Only 下知识维度 collapse，Limited Consistency 为作者合同中的折衷；SLM score≥3 rate 92.06%，LLM 为93.11%。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** synthesis H100/Ascend GPU-hours、tool W8A8、model/token budget已披露；pretraining cluster topology、完整 precision/batch/sequence、并发、energy 与 serving SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 Llama3-style model、数据配比与评测中，genre-audience reformulation 可比有限重复/upsampling提供更多有效训练信号，且收益随所测 model scale 增大；单一 validation loss 不能充分判定作者所测 synthetic-data failure。
- **What It Does Not Prove:** 不证明可无限合成高质量数据、不证明新信息真实、不证明所有语种/领域/架构同样获益，也不证明 validation loss 失去通用诊断价值或 MAGA 避免长期 model collapse。
- **Limitations / Threats to Validity:** judge prompt明确容许原文外信息，可能放大 hallucination；同源 labeler/judger bias、单一 corpus/model family、moderate-scale实验、benchmark contamination、license/provenance 与真实数据混合比例均限制外推。
- **Trade-offs / New Failure Modes:** unique expression 增加、重复下降，但引入 synthetic provenance、judge preference、模板残留、事实漂移、domain imbalance、tool-version drift 与昂贵离线生成；更松的变换目标会牺牲知识保真。
- **Where the Previous Design Still Applies:** 真实数据过滤适合事实/provenance敏感领域；有限重复适合小预算；强 teacher/seed system 适合需严格任务结构；retrieval 或数据授权可在不生成新事实时扩充覆盖。
- **Evolution Relationship:** `Direct Evolution`：real-data filtering→controlled repetition/upsampling→seed/rephrase synthesis→genre-audience expansion+limited-consistency gate；与 data mixture/evaluation 是 `Layering / Dependency`。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `TRAIN-PRETRAINING` Ch28、`PLATFORM-EVALUATION-SYSTEM` Ch66 与 artifact/provenance contract。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～28 的 data/objective boundary、Ch59 artifact identity 与 Ch66 evidence contract。
- **Existing Coverage:** Books 已覆盖 data quality、dedup 与 synthetic-data 风险；本 family 补充“表达分布扩展—接受策略—训练配比—collapse 诊断”完整机制，但本轮不做 Books Integration。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度 Weekly 账本；不把 v2 artifact、作者 headline 或未绑定条件的 benchmark 写入 Books。
- **Open Questions:** 如何在生成阶段强制 factual provenance；judge/source-family 如何去相关；synthetic ratio 何时触发 collapse；跨语种、MoE 与长周期训练能否复现 scaling trend。

### HMA / Learning Real-World Action-Video Dynamics with Heterogeneous Masked Autoregression

- **Candidate / Week / Score:** HMA / Learning Real-World Action-Video Dynamics / 2025-W06 / 28/30。
- **Source Family ID:** `hma-heterogeneous-action-video-dynamics`。
- **Source Type:** arXiv v1 research paper + author project page。
- **First-public Date / Revision History:** arXiv v1 2025-02-06；截至本次核验无后续 arXiv revision。
- **Direct Primary Sources:** https://arxiv.org/html/2502.04296v1；https://arxiv.org/abs/2502.04296；https://liruiw.github.io/hma。
- **Related Primary Sources:** Open-X、Ego4D/EPIC、Robomimic、Language Table 与 HPT 原始资料定义数据、transfer 与 evaluation contract。
- **Access and Verification Status:** Full Source Review Complete；method、heterogeneous stems/heads、masked autoregression、pretraining scaling、simulator/policy/synthetic-data experiments与limitations已核验。
- **Full-read Coverage:** 已读 Introduction/Related Work、passive/forward/full dynamics、action heterogeneity、quantized/soft-token MAR、architecture/training/inference、40-dataset/3M-trajectory scaling、post-training applications、failure cases与limitations。
- **Original Problem:** robot interaction data跨 embodiment/action schema高度异构、真实评测昂贵危险；传统 video generation 未必对 action 可控，慢速 diffusion simulator 又难进入实时闭环。
- **Why the Previous Design Was Reasonable:** per-robot policy/simulator可保留明确 action semantics；passive video model利用大量无动作视频；物理 simulator拥有可解释 state/reward，真实机器人测试提供最终证据。
- **Changed Constraint:** 希望共享多 embodiment 的 video dynamics，并以有限 target data迁移到 policy evaluation、synthetic data与action generation；系统同时要求视觉保真、action controllability与较低交互延迟。
- **Mechanism:** 每个 embodiment 使用独立 action input stem/output head，共享 spatial-temporal Transformer trunk；spatial attention双向、temporal attention causal。随机顺序 masked autoregression预测 quantized 或 soft video tokens，action modulation注入低层动作；full dynamics另预测 action tokens。
- **State Ownership:** embodiment-specific stems/heads拥有 action schema；shared trunk拥有跨域 dynamics representation；video/action tokens拥有 observation/action history；mask schedule拥有生成顺序；外部 policy/annotator拥有 action 与 success truth。
- **Control Flow / Data Flow:** heterogeneous trajectories→domain-specific action encoding→shared trunk在 observation/action context 上预测 future masked tokens→iterative unmask/diffusion soft-token generation→post-train为 simulator/evaluator/generator/policy→环境或人工反馈验证。
- **Implementation Details:** 每 frame 256 video tokens与64 repeated action tokens；mask ratio按 cosine schedule；μP 扩 model，action projector Xavier gain 0.1；diffusion HMA 推理含 time、patch-unmask、continuous-token diffusion 三层迭代。
- **Evaluation Contract:** 35 real-robot、3 human-video、2 simulation datasets，总计约3M trajectories/40 embodiments；按 dataset count、trajectory count、3M～400M sparse parameters缩放，以 perplexity、PSNR/SSIM/LPIPS/FID/FVD、ΔPSNR及 action perturbation metrics评估。
- **Baselines / Ablations / Sensitivity / Overhead:** passive/forward/full dynamics；concat/add/cross-attention/modulation action fusion；VQ 与 soft token、pretraining/finetuning、数据/embodiment/model scale。forward dynamics优于 passive，full dynamics未优于 forward，作者归因于 VQ token 对 action prediction 不适配。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model 3M～400M sparse params、40 datasets/3M trajectories、train horizon 12、inference可超100 steps已披露；训练硬件、precision、batch、并发、control-frequency/P95 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数据与任务中，共享 trunk+typed action interfaces可在异构 embodiment 上稳定预训练，action-conditioned MAR比 passive video更可控；预训练可帮助有限数据 transfer，并支持若干 simulator/policy用途。
- **What It Does Not Prove:** 不证明 learned video dynamics 是真实物理 simulator、不证明长 horizon causal correctness、不证明能替代真实 robot evaluation，也不证明摘要中的15×适用于所有 simulator；Robomimic policy evaluation平均32秒，MuJoCo为9秒。
- **Limitations / Threats to Validity:** controllability受数据限制，dropping/catching等物理细节失败；learned evaluator需人工 success annotation；policy/action generation有限，未在复杂真实机器人、长 horizon planning/MPC 中验证。
- **Trade-offs / New Failure Modes:** heterogeneous sharing提高数据利用，却引入 schema/calibration mismatch与domain interference；MAR降延迟但引入 mask/order与tokenizer误差；learned simulation会累积 state drift、action insensitivity与不可见 reward error。
- **Where the Previous Design Still Applies:** physics simulator适合可建模环境和精确 reward；per-embodiment model适合 schema差异大/数据足；diffusion适合质量优先；真实机器人测试仍是 deployment gate。
- **Evolution Relationship:** `Direct Evolution`：passive video prediction→action-conditioned forward dynamics→heterogeneous shared dynamics→simulator/evaluator/policy coupling；不是从 video quality 到 physical correctness 的等价替代。
- **ROADMAP Node:** `MULTIMODAL-WORLD-MODELS`（Ch25）主 owner；handoff `MULTIMODAL-EMBODIED-VLA` Ch26、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26 的 representation/generation/world-state/action boundary，以及 Ch66 的 executable evidence boundary。
- **Existing Coverage:** Books 已区分 video generation、world model 与 embodied loop；HMA 提供 heterogeneous action schema、state ownership与 learned-evaluator failure 的受限案例，本轮只登记 Books Pending。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；纠正“15×”证据边界，不把 image metric 或短程 correlation 外推为 physical fidelity。
- **Open Questions:** action schema/clock如何版本化；rollout state drift如何检测/rollback；synthetic trajectories何时反噬 policy；learned evaluator需要何种真实校准集和 safety envelope。

### Particle-Based Monte Carlo Inference-Time Scaling

- **Candidate / Week / Score:** Particle-Based Inference Scaling / Rollout Roulette / 2025-W06 / 27/30。
- **Source Family ID:** `particle-monte-carlo-inference-time-scaling`。
- **Source Type:** arXiv v1 research paper；后续同 family revisions/rename。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-02-04；v3 2025-02-11；v4 2025-06-05；v5 2025-08-14。W06 锁定 v1 标题、算法与实验，后续 “Rollout Roulette” 名称不回写成当日事实。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01618v1；https://arxiv.org/abs/2502.01618。
- **Related Primary Sources:** Qwen2.5-Math PRM、Math-Shepherd、DVTS/Best-of-N/weighted BoN 与 Particle Gibbs/parallel tempering原始算法定义比较分支。
- **Access and Verification Status:** Full Source Review Complete；probabilistic formulation、PF/PG/PT algorithms、reward aggregation、evaluation、budget allocation、temperature/PRM ablations与appendix已核验。
- **Full-read Coverage:** 已读 state-space formulation、approximate likelihood、particle filtering/resampling、PG reference trajectory、PT special case、models/rewards/tasks/baselines、scaling/ablation/budget allocation、limitations与算法appendix。
- **Original Problem:** Best-of-N 与 deterministic tree/beam search容易围绕 reward-model mode 过度利用错误分数；固定 branching/depth也未显式表示对 partial trajectory 的不确定性。
- **Why the Previous Design Was Reasonable:** BoN embarrassingly parallel且实现简单；beam/tree search集中算力于高分候选，在 reward可靠、branch较少时能减少浪费；majority vote无需独立 process reward。
- **Changed Constraint:** test-time budget扩到多轨迹且 PRM 不完美，需要既利用高分 partial answer，又维持样本多样性，并比较 particle count、iteration与parallel-chain三种预算轴。
- **Mechanism:** 将 partial response视为 state、LLM continuation为 transition、PRM为近似 likelihood；N 个 particles按 reward softmax随机 resample，再各自生成下一步。Particle Gibbs保留上一 iteration reference trajectory；parallel tempering在不同 temperature chains间交换状态。
- **State Ownership:** 每个 particle拥有自己的 partial-token/KV trajectory；reward model拥有非真值权重；resampler拥有 lineage/duplication决定；reference trajectory与temperature chain分别拥有跨 iteration/chain 状态。
- **Control Flow / Data Flow:** prompt→N initial particles→partial rewards→softmax weights→stochastic ancestor sampling→并行 transition→重复至停止→final particles/selector；PG/PT增加 reference 或 chain-exchange控制面。
- **Implementation Details:** v1 使用 model-based aggregation 组合 partial-answer reward；实验主要执行 single-iteration PF与有限 PG/PT special cases，完整 parallel tempering算法虽给出但未被完整实验验证。
- **Evaluation Contract:** Llama-3.2-1B、Llama-3.1-8B、Qwen2.5-Math-1.5B/7B，在 MATH500 与 AIME 2024 上比较 Pass@1、BoN、weighted BoN、DVTS；主表 budget=64 model generations，主要 PRM 为 Qwen2.5-Math-PRM-7B。
- **Baselines / Ablations / Sensitivity / Overhead:** reward model/aggregation、policy temperature、particle数、PG iteration、parallel groups；在100题 MATH500 subset上分配 `N×T×M`，较大 N 通常优于同预算更多 iteration，PG并未稳定优于等预算 PF。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/reward/budget/tasks披露；GPU型号、precision、token lengths、KV复制开销、batch/concurrency、latency/throughput/P95 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者数学任务与 PRM 合同中，stochastic resampling PF优于所测 BoN/WBoN/DVTS，并能在相同 generation budget 下探索长尾正确轨迹；budget allocation影响效果。
- **What It Does Not Prove:** 不证明 PF 的 headline准确率跨 task/reward/model成立，不证明概率推断保证语义正确，不证明 PG/PT扩展优于 PF，也不证明 token/GPU成本或服务延迟优于树搜索。
- **Limitations / Threats to Validity:** 仅数学 benchmarks、作者 PRM、AIME样本小、closed-model headline对比条件不等价；reward hosting增加 latency，smaller model需 prompt engineering，temperature依问题/模型变化。
- **Trade-offs / New Failure Modes:** stochasticity保留多样性但增加方差与复现难度；resampling会 particle collapse，错误 reward 会复制错误 lineage；多 particle KV/state带来memory、cancellation、fairness与tail-latency压力。
- **Where the Previous Design Still Applies:** BoN适合无 partial reward或调度简单；beam/tree适合精确 verifier和结构化行动；self-consistency适合答案聚合；单样本适合强 latency/cost SLO。
- **Evolution Relationship:** `Alternative Branch`：single sample→BoN/majority→deterministic tree/beam→probabilistic particle resampling→iterative/tempered chains；新分支不取代可靠 verifier 下的 deterministic search。
- **ROADMAP Node:** `INFER-SCHEDULING`（Ch56）主 owner；handoff `AGENT-PLANNING` Ch79、`INFER-KV-CACHE` Ch45 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch45、Ch48、Ch51～56 的 token/state scheduling，以及 Ch66、Ch79 的 verifier/planning boundary。
- **Existing Coverage:** Books 已覆盖 test-time compute与 scheduling；本 family 增加 particle lineage、stochastic resampling与三轴 budget contract，本轮不写入 Books。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；不把 v5 rename/后续结果或 closed-model对比当作 v1 通用结论。
- **Open Questions:** particle KV如何共享/回收；resampling怎样保持tenant fairness；reward drift如何触发fallback；lineage、random seed和decision trace如何审计。

### Speak Easy / Multilingual Multi-Step Jailbreak Evaluation

- **Candidate / Week / Score:** Speak Easy / 2025-W06 / 27/30。
- **Source Family ID:** `speak-easy-multilingual-multistep-jailbreak`。
- **Source Type:** arXiv v1 research paper + benchmark/evaluation artifact。
- **First-public Date / Revision History:** v1 2025-02-06；v2 2025-06-16；v3 2025-08-02。W06 conclusions锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.04322v1；https://arxiv.org/abs/2502.04322。
- **Related Primary Sources:** HarmBench、AdvBench、SORRY-Bench、MedSafetyBench 与 GCG/TAP 原始资料定义 attack/evaluation baselines。
- **Access and Verification Status:** Full Source Review Complete；HarmScore构造、人类标注、attack workflow、selection models、四 benchmark/三 target models、ablations与appendices已核验。
- **Full-read Coverage:** 已读 harmfulness attributes、response augmentation/human annotation、HarmScore、query decomposition/language diversification/response selection、实验设置、ASR/HarmScore、人类一致性、step/language/selector ablations与ethics边界。
- **Original Problem:** 单轮、单语拒答评测低估真实攻击者将危险请求拆解、跨语言改写并从多轮结果中挑选可执行信息的能力；binary ASR又难区分模糊讨论与可行动伤害。
- **Why the Previous Design Was Reasonable:** 单轮 benchmark便于复现、成本低且隔离模型响应；固定语言减少翻译噪声；binary judge适合大规模筛查明显 refusal/non-refusal。
- **Changed Constraint:** deployment面对stateful multi-turn、multilingual与组合攻击，攻击者会主动选择不同轮次/语言的最佳片段；评价需同时描述 actionability 与 informativeness。
- **Mechanism:** 把恶意 query拆成默认3个步骤，在默认6种语言分别查询；收集各轮多语响应，以分别训练的 actionability/informativeness selectors选择并组合。HarmScore由两属性共同衡量，而非只判 non-refusal。
- **State Ownership:** conversation history拥有跨步上下文；language/translation layer拥有语义变换；target model拥有每轮response；selectors拥有选择偏差；evaluator/HarmScore policy拥有 harm taxonomy与operating point。
- **Control Flow / Data Flow:** harmful query→step decomposition→多语言翻译→逐步 target-model calls→candidate responses→actionability/informativeness scoring→selected/combined output→ASR、HarmScore与human comparison。
- **Implementation Details:** 默认3 steps、6 languages（English、Simplified Chinese、Ukrainian、Turkish、Zulu、Thai），Azure Translator；selectors以 Llama-3.1-8B 在独立 preference data 上 fine-tune。
- **Evaluation Contract:** target GPT-4o、Qwen2-72B-Instruct、Llama-3.3-70B；Direct Request、GCG-T、TAP-T；HarmBench200、AdvBench520、SORRY-Bench450、MedSafetyBench450；默认三步六语，比较ASR与HarmScore。
- **Baselines / Ablations / Sensitivity / Overhead:** steps 1/3/5、languages 1/3/6/9、random/fixed/oracle/learned selector；三步到五步 ASR上升但 HarmScore略降，六到九语几乎不再提高 HarmScore，说明不是单调扩展。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** target/selector models、benchmarks、step/language counts披露；hardware、precision、prompt/output lengths、API并发、latency/cost与deployment SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者攻击与 judge合同中，stateful multilingual decomposition显著增加所测模型产生 actionable/informative harmful content 的概率，并暴露单轮单语评测的 coverage gap。
- **What It Does Not Prove:** 不证明所有语言或模型同样脆弱，不证明 HarmScore等价真实世界伤害或内容正确，不证明攻击成功能绕过产品层全部防护，也不证明平均增量可外推新版本。
- **Limitations / Threats to Validity:** 翻译服务与 selector引入偏差；HarmScore优先 relevance而非事实正确；benchmark/target version有限；危险响应的人类标注与组合方式影响 operating point。
- **Trade-offs / New Failure Modes:** 更真实的多轮覆盖提高 recall，却显著增加请求/评审成本、false positive、跨语言 policy drift、history poisoning和复合信息 leakage；防御若只看单轮会失去 cumulative-risk state。
- **Where the Previous Design Still Applies:** 单轮单语测试仍适合快速回归和local policy；人工 red team适合开放攻击；tool/execution sandbox适合验证从文本到真实行为的差距。
- **Evolution Relationship:** `Direct Evolution`：single-turn refusal test→adversarial suffix/search→multi-step stateful decomposition→multilingual candidate selection→cumulative harm evaluation。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66 与 `AGENT-WORKFLOW` Ch81。
- **Target and Adjacent Chapters Read:** 已核对 Ch66～73 的 evidence/security/release gate 与 Ch74～81 的 context/workflow state boundary。
- **Existing Coverage:** Books 已覆盖 threat model与 multi-turn state；本 family 提供 language×step×selection 的 attack surface和 cumulative-risk contract，本轮只登记待集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；不复述危险示例，不把 ASR/HarmScore headline当作 deployment exploit probability。
- **Open Questions:** production guard如何跨语言累积risk；translation/selector identity如何进入trace；防御如何区分 benign decomposition；模型更新后怎样控制重测成本。

### Sample, Scrutinize and Scale / Verification-Scaled Sampling Search

- **Candidate / Week / Score:** Sample, Scrutinize and Scale / 2025-W06 / 26/30。
- **Source Family ID:** `sampling-search-verification-scaling`。
- **Source Type:** arXiv v1 research paper + official Google Research code/benchmark artifact。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-02-20。W06 使用v1 PDF与v1实验合同。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.01839v1；https://arxiv.org/abs/2502.01839；https://github.com/google-research/google-research/tree/master/sampling_based_search。
- **Related Primary Sources:** AIME、Berkeley MATH、LiveBench 与 self-consistency/verifier基线资料定义任务与比较口径。
- **Access and Verification Status:** Full Source Review Complete；v1 37页 PDF 的 method、scaling、verification prompts/rewriting、experiments、technical details、benchmark与appendices已核验。
- **Full-read Coverage:** 已读 sampling/verification两轴、implicit scaling、long-tail case、cross-response comparison、rewrite/CoT verification、smaller-model/ablation、technical setup、verification benchmark、related work与附录 prompts/cost细节。
- **Original Problem:** random sampling增加 Pass@k，但 majority/self-consistency会收敛到高概率答案并错过长尾正确解；verifier本身又可能随候选池扩大而失准。
- **Why the Previous Design Was Reasonable:** self-consistency便宜、无需独立 verifier且可平均随机错误；single response满足低 latency；CoT有利于生成推理并可直接复用标准模型。
- **Changed Constraint:** test-time compute预算扩到数百 candidates，需要区分 search compute 与 verification compute；困难任务的正确答案可能极稀有，选择器必须识别长尾而非众数。
- **Mechanism:** 生成 `k_inf` 个随机候选；对每个候选做 `k_verif` 次自然语言 self-verification并平均分；接近最高分的候选再两两比较 tie-break。跨候选差异定位错误，verifier先将 CoT改写为更模块化/形式化结构再评审。
- **State Ownership:** candidate pool拥有 search diversity；每候选的verification samples拥有不确定性；score/tie threshold拥有commit policy；pairwise comparison拥有最终选择；benchmark truth只用于离线评估。
- **Control Flow / Data Flow:** question→并行 sampling→逐候选多次 correctness scoring→保留最高分0.05范围→pairwise comparisons→winner commit；大池同时增加 correct-candidate出现率与可验证的高质量候选比例。
- **Implementation Details:** 默认 Gemini v1.5-Pro-002/Flash-002；`k_inf=200`、temperature 1.5、`k_verif=50`、verification temperature 1、max output 8192；成本过高时先10次评分丢弃低分候选。
- **Evaluation Contract:** AIME 2024（15题）、Berkeley MATH500、LiveBench Math/Reasoning；主scaling图从一次200 candidates×每候选50 scores的primary run中以20 random seeds subsample；headline表因成本只做单次run。
- **Baselines / Ablations / Sensitivity / Overhead:** Pass@1、Consistency@200/1000、Verification@200、o1-preview公开/作者API数值；Main/Shortened/Without-Rewrite/Split-Context prompts。去掉rewrite或拆分context会提高FPR/FNR，Olympiad子任务未优于consistency。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Google Cloud API models、200×50 scale与8192 max tokens披露；底层hardware/precision、实际token usage、parallelism、wall-clock、cost distribution、P95 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 Gemini版本与四类reasoning benchmark中，同时扩 search 与 verification可在self-consistency饱和后继续改善，并显示更大候选池可提高“存在更易验证正确解”的概率。
- **What It Does Not Prove:** 不证明更多sampling总会改善、不证明 self-verification可靠、不证明单次headline超过 o1构成模型通用能力排序，也不证明这种极高调用量满足生产成本/延迟。
- **Limitations / Threats to Validity:** AIME样本小、closed API模型、同模型生成/评审相关偏差、昂贵配置单次run、benchmark truth与prompt engineering敏感；comparison保证至少一解正确并不代表线上条件。
- **Trade-offs / New Failure Modes:** embarrassingly parallel search换来巨额 token/call成本；verifier false negative会丢弃稀有正确解，false positive会commit fluent错误；候选池、score与tie-break引入状态、取消、fairness和trace负担。
- **Where the Previous Design Still Applies:** self-consistency适合答案分布集中且低成本；external symbolic verifier适合可执行问题；single pass适合 latency敏感；trained reward/verifier适合高复用 workload。
- **Evolution Relationship:** `Direct Evolution`：single response→self-consistency→sample-and-verify→cross-response comparison+rewrite→search/verification joint scaling；与 particle/tree search 是 `Alternative Branch`。
- **ROADMAP Node:** `INFER-SCHEDULING`（Ch56）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66、`AGENT-REFLECTION` Ch80 与 `AGENT-WORKFLOW` Ch81。
- **Target and Adjacent Chapters Read:** 已核对 Ch48、Ch51～56 的 proposal/commit与budget scheduling，以及 Ch66、Ch79～81 的 verifier/workflow boundary。
- **Existing Coverage:** Books 已覆盖 sampling与 verifier；本 family补充 search/verification双预算、rewrite适配与 long-tail selection，但本轮不写入 Books。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；headline比较保留 model/date/task/call-budget，不外推为一般推理效率。
- **Open Questions:** 如何以early stopping/upper bound降低10k级调用；generator/verifier如何去相关；continuous batch如何分配search与verification公平性；decision trace如何复现。

### Preference Leakage / Generator–Judge Relatedness in LLM Evaluation

- **Candidate / Week / Score:** Preference Leakage / 2025-W06 / 25/30。
- **Source Family ID:** `preference-leakage-generator-judge-relatedness`。
- **Source Type:** arXiv v1 research paper + official code artifact。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-05-24；v3 2026-03-04。W06锁定v1，后续修订不倒灌。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.01534v1；https://arxiv.org/abs/2502.01534；https://github.com/David-Li0406/Preference-Leakage。
- **Related Primary Sources:** Arena-Hard、AlpacaEval2.0、UltraFeedback 与 LLM-as-a-judge bias文献定义 task/judge comparison。
- **Access and Verification Status:** Full Source Review Complete；v1 PDF 的 relatedness定义、main/extended experiments、PLS/manual annotation、data-mixing/category/detection分析与appendix已核验。
- **Full-read Coverage:** 已读 abstract/introduction/related work、same/inheritance/family formalization、generator-student-judge pipeline、models/data/training/judging、human comparison、inheritance/family/learning-method/mixing analyses、classification probe、limitations/evidence boundary。
- **Original Problem:** synthetic data generator与LLM judge常被当成独立组件；若两者同模型、继承或同family，generator的style/wording preference可能经student训练回流给judge，造成隐蔽自我偏好。
- **Why the Previous Design Was Reasonable:** LLM synthesis与judge显著降低标注成本；使用同一强模型/family可保持task instruction一致；对未知模型 lineage 缺少可操作的独立性指标。
- **Changed Constraint:** synthetic training和LLM-as-judge同时进入模型生命周期，evaluation provenance不再只关心 benchmark overlap，还必须描述 generator、student、judge的 lineage/relatedness。
- **Mechanism:** 分别用GPT-4o、Gemini-1.5-Flash、Llama-3.3-70B生成UltraFeedback answers，fine-tune Mistral-7B/Qwen2.5-14B students；再由三个相关judge做pairwise比较，以 related judge相对平均win-rate的偏移构造 Preference Leakage Score，并用人工标注交叉检查。
- **State Ownership:** generator/version拥有 synthetic style；training corpus与student checkpoint承载 preference；judge/version拥有 evaluation policy；lineage graph拥有 same/inheritance/family relation；human labels提供独立但有限参照。
- **Control Flow / Data Flow:** instructions→不同 generator responses→SFT student variants→Arena-Hard/AlpacaEval pairwise outputs→不同 judges评分→PLS/manual comparison→继承、family、learning method、mix ratio与category analyses。
- **Implementation Details:** generators/judges含 GPT-4o-2024-11-20、Gemini-1.5-Flash、Llama-3.3-70B-Instruct-Turbo；students为Mistral-7B-v0.1与Qwen2.5-14B；另比较 SFT/DPO/ICL、same/different instructions及 manual/other-synthetic mixing。
- **Evaluation Contract:** Arena-Hard 与 AlpacaEval2.0 pairwise judging，多个generator/student/judge组合；PLS测related judge对其related student相对其他judge的偏移，人工标注用于检查模型真实性能差异与bias方向。
- **Baselines / Ablations / Sensitivity / Overhead:** same model、inheritance、same family；student size；SFT/DPO/ICL；same/different instruction；synthetic contamination ratio与manual/other-synthetic mixing；student recognition与BERT response-family classification probe。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/version、datasets与evaluation流程披露；fine-tuning hardware/precision、token lengths、batch、judge sampling/concurrency、cost/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者模型和pairwise合同中，judge偏好与generator lineage相关，且可经synthetic data与student训练保留；mixing和不更新参数的ICL会改变但不必然消除该偏差。
- **What It Does Not Prove:** 不证明所有同family judge必然偏置、不证明observed win-rate差全由leakage导致、不证明PLS是因果识别量，也不允许由closed-model行为推断具体training-data overlap。
- **Limitations / Threats to Validity:** model/benchmark组合有限、closed lineage不透明、response质量接近时bias更显著、judge position/style/length等偏差可能混杂；较大student更易leak只是作者解释而非普遍因果。
- **Trade-offs / New Failure Modes:** 复用同family降低集成成本却污染evaluation independence；多judge/人工校准提高可信度但增加成本与disagreement；lineage未知会形成不可审计 release gate。
- **Where the Previous Design Still Applies:** 同模型judge适合开发期快速反馈；规则/executable evaluator适合可验证任务；独立人评适合高风险发布；ICL可在避免参数吸收时作为替代。
- **Evolution Relationship:** `Direct Evolution`：benchmark data leakage→judge positional/style bias→generator–judge relatedness leakage→lineage-aware evaluation provenance；不是简单要求“永远换judge”。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `TRAIN-DATA` Ch27、`TRAIN-SFT` Ch29、model registry lineage与 release governance。
- **Target and Adjacent Chapters Read:** 已核对 Ch27～29、Ch59、Ch66～73 的 data/artifact/evidence/governance boundary。
- **Existing Coverage:** Books 已要求 evaluator identity与provenance；本 family补充 generator→student→judge 三方 lineage和 independence failure，Books判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；不把作者 PLS 当成跨模型通用指标，不推断closed training data。
- **Open Questions:** 如何给generator/judge lineage签名；independence需要跨vendor还是跨training corpus；multiple judges如何聚合并暴露correlated error；release gate怎样设最低独立证据。

### The Differences Between Direct Alignment Algorithms are a Blur

- **Candidate / Week / Score:** Direct Alignment Algorithms are a Blur / 2025-W06 / 24/30。
- **Source Family ID:** `direct-alignment-objective-factorization-study`。
- **Source Type:** arXiv v1 research paper + mathematical proofs/experimental appendix。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-05-19；v3 2026-05-08。W06锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01237v1；https://arxiv.org/abs/2502.01237。
- **Related Primary Sources:** DPO、ORPO、ASFT、IPO、SimPO、NCA、Cal-DPO、APO-Zero原始论文与UltraChat/UltraFeedback/TL;DR评测资料定义算法和数据合同。
- **Access and Verification Status:** Full Source Review Complete；v1 objectives/proofs、SFT/temperature generalization、3B/8B experiments、SFT-fraction study、appendix hyperparameters与limitations已核验。
- **Full-read Coverage:** 已读 RLHF/DAA preliminaries、ASFT/ORPO等价与上界、gradient relation、pairwise/pointwise区分、base/SFT初始化、β sensitivity、SFT质量、training/generation details、proofs与toy/Pareto appendices。
- **Original Problem:** 直接偏好优化算法被按“有无reference”“odds或ratio”“one/two-stage”命名为不同范式，但实现中的SFT初始化、temperature、pairwise结构与数据量经常不受控，比较结果难以解释。
- **Why the Previous Design Was Reasonable:** 每个新loss强调不同理论动机，单阶段可减少独立SFT流程，reference-free可节省checkpoint/forward；在各自原始合同内，按算法名比较有实际工程意义。
- **Changed Constraint:** 算法数量增多且benchmark差异很小，需要把objective拆成可控因子，判断性能来自loss形式、pairwise/pointwise、SFT初始化还是β/data，而非名称。
- **Mechanism:** 证明ASFT为chosen likelihood+rejected unlikelihood的BCE形式，ORPO与ASFT存在直接关系；移除内嵌SFT项后可作为SFT后的二阶段alignment，并向odds reward加入β。以gradient/实验对照pairwise与pointwise objective。
- **State Ownership:** SFT checkpoint拥有instruction prior；reference/base policy拥有相对reward基线；preference pair拥有chosen/rejected关系；β拥有update强度/implicit trust region；judge benchmark拥有最终外部评价。
- **Control Flow / Data Flow:** base model→可选SFT subset checkpoint→同一preference data上运行不同factorized objective/β→生成responses→AlpacaEval2/ArenaHard或TL;DR GPT judge→比较Pareto与confidence intervals。
- **Implementation Details:** Llama3.1-8B UltraChat/UltraFeedback为主，另含Llama3.2-3B与Reddit TL;DR；max length 4096/1024、batch128、Adam、1～2 epochs、DeepSpeed、FlashAttention2；SFT fractions 1/3/5/10/25/50/100%。
- **Evaluation Contract:** AlpacaEval2 LC/WR、ArenaHard和TL;DR side-by-side；learning rate与β grid search，比较DPO/IPO/SimPO/NCA/Cal-DPO/APO-Zero/ORPO/ASFT的base或SFT initialized variants。
- **Baselines / Ablations / Sensitivity / Overhead:** SFT presence/size、β、pointwise/pairwise、implicit reward form、base vs SFT initialization；5～10% SFT已带来显著增益，但raw base方案仍未匹配full-SFT后alignment。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 3B/8B、length、batch、optimizer、memory stack披露；GPU数量/型号、precision、wall-clock/energy与serving SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者3B/8B与三套数据/评测中，SFT初始化和pairwise/pointwise结构解释了大量差异；加入β并二阶段化可显著改善ORPO/ASFT，且无单一DAA跨设置稳定占优。
- **What It Does Not Prove:** 不证明所有DAA本质等价、不证明pairwise永远更好、不证明SFT必须用全量或judge win-rate等价human alignment，也不外推到更大模型/安全域。
- **Limitations / Threats to Validity:** 数据/benchmark有限、GPT evaluator bias、3B～8B规模、hyperparameter search预算与sequence normalization选择会混杂；部分confidence intervals重叠。
- **Trade-offs / New Failure Modes:** 因子化比较提高可解释性却增加grid-search成本；SFT先验改善稳定性但可能限制preference更新；pairwise提高相对排序却不校准absolute quality，pointwise可能独立推高/压低概率。
- **Where the Previous Design Still Applies:** 单阶段适合流程/存储受限且任务接近preference data；reference-free适合无可靠base snapshot；pointwise适合independent labels；经典RLHF适合显式reward重用和online exploration。
- **Evolution Relationship:** `Principle Reuse`：RLHF三阶段→direct preference objectives→single-stage合并→factorized SFT/β/pairwise design space；不是按发布时间的替代链。
- **ROADMAP Node:** `TRAIN-DPO`（Ch34）主 owner；handoff `TRAIN-SFT` Ch29、`TRAIN-RLHF` Ch31 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch29～34 的post-training分支和Ch66 judge contract。
- **Existing Coverage:** Books 已把DPO/PPO/GRPO写成条件分支；本 family补充“算法名→可控设计因子”的比较原则，本轮仅登记待集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06与年度账本；不把作者win-rate增量写成通用alignment提升。
- **Open Questions:** objective factor在online data中是否保持；β与KL/length normalization如何统一；独立human/executable evaluator会否改变排序；MoE/70B+规模是否仍由pairwise结构主导。

### AlignVLM / Convex-Hull Vision–Language Connector

- **Candidate / Week / Score:** AlignVLM / 2025-W06 / 23/30。
- **Source Family ID:** `alignvlm-vocabulary-convex-hull-connector`。
- **Source Type:** arXiv v1 research paper + training/evaluation appendix。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-11-02。W06锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01341v1；https://arxiv.org/abs/2502.01341。
- **Related Primary Sources:** SigLIP、Llama3、BigDocs-7.5M、DocDownstream与VLMEvalKit/DocVQA等primary资料定义encoder、data与evaluation contract。
- **Access and Verification Status:** Full Source Review Complete；architecture/equations、three-stage training、document benchmark、connector/embedding analysis、noise robustness、VCR/appendix案例已核验。
- **Full-read Coverage:** 已读 VLM alignment背景、vision tiling/SigLIP、Align connector/convex-hull argument、MLP/VET alternatives、三阶段训练、nine document benchmarks、connector/semantic/noise analyses、qualitative failures与appendix。
- **Original Problem:** 普通MLP把visual features直接投影到LLM embedding space，可能落在pretrained text manifold之外；另建visual embedding table又增加未对齐参数，尤其document OCR/structure任务对小误差敏感。
- **Why the Previous Design Was Reasonable:** MLP connector简单、连续、低成本，可让end-to-end training自行学习alignment；visual table为视觉提供独立容量，不受text vocabulary限制。
- **Changed Constraint:** limited multimodal data与较小LLM需要更强inductive bias，目标是让visual representation落入LLM已学习可解释的区域，同时保持连续patch信息而非硬token化。
- **Mechanism:** visual feature经两层projection+LayerNorm得到对整个LLM vocabulary的softmax分布，再对冻结/当前text embedding matrix加权求和；每个visual token成为text embeddings convex hull中的dense mixture，随后与text tokens拼接给LLM。
- **State Ownership:** vision encoder拥有patch features；Align logits/probabilities拥有跨模态mapping；LLM embedding matrix定义目标几何；tiling拥有image-shape identity；training stage拥有哪些组件可更新。
- **Control Flow / Data Flow:** image→最多9 tiles→14×14 patches→SigLIP-400M→Align vocabulary distribution→weighted text-embedding mixtures→concat query embeddings→Llama autoregressive answer；三阶段逐步从alignment到document pretraining再instruction tuning。
- **Implementation Details:** Llama3.2-1B/3B和Llama3.1-8B；Stage2使用BigDocs-7.5M并全模型训练，Stage3用DocDownstream且冻结vision encoder、更新LLM+Align；vocabulary约128K，分析显示distribution dense、单token最高概率仅0.0118。
- **Evaluation Contract:** DocVQA、InfoVQA、DeepForm、KLC、WTQ、TabFact、ChartQA、TextVQA、TableVQA，经VLMEvalKit评测；同数据regime内与MLP/VET connector和base VLM比较，另列半透明/闭源SOTA作背景。
- **Baselines / Ablations / Sensitivity / Overhead:** MLP、Visual Embedding Table、Align；representation similarity/nearest tokens、VCR easy/hard、Gaussian noise σ=3。作者3B合同中MLP平均降25.54，Align降1.67，但不是通用鲁棒性保证。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/encoder/tiles/data与benchmarks披露；training GPUs、precision、batch、image resolution distribution、latency/memory/concurrency/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者document数据与模型中，把visual features约束为text-embedding dense convex combinations优于同训练regime的MLP/VET，并在所测feature noise下更稳健。
- **What It Does Not Prove:** 不证明mixture对应可解释词义、不证明convex hull包含所有视觉概念、不证明跨自然图像/video/audio同样有效，也不证明优于训练数据更强的SOTA。
- **Limitations / Threats to Validity:** 主要document任务、有限models、training/hardware细节不足、dense 128K projection可能昂贵；qualitative例子仍有OCR错误，后续v2不可倒灌。
- **Trade-offs / New Failure Modes:** reuse language geometry降低OOD输入，却可能压缩非语言视觉细节；full-vocab softmax带来compute/memory，embedding drift会改变视觉表示identity，tiling/patch order和OCR noise仍需管理。
- **Where the Previous Design Still Applies:** MLP适合数据充足/低延迟；visual table适合视觉概念超出语言几何；discrete visual tokenizer适合generative compression；cross-attention适合保持独立modality state。
- **Evolution Relationship:** `Alternative Branch`：direct projection→separate visual codebook→text-embedding convex mixture；与native multimodal pretraining是 `Layering / Dependency` 而非替代。
- **ROADMAP Node:** `MULTIMODAL-REPRESENTATION`（Ch23）主 owner；handoff `MODEL-EMBEDDING` Ch12、`MODEL-TOKENIZER` Ch11与`TRAIN-DATA` Ch27。
- **Target and Adjacent Chapters Read:** 已核对 Ch11～12、Ch23～24、Ch27的identity、fusion与data boundary。
- **Existing Coverage:** Books 已覆盖modality-specific encoder、shared token space与fusion；本family补充convex-mixture connector及embedding-version coupling，本轮不修改Books。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06与年度账本；closed/SOTA表不作为公平因果比较，noise结果绑定σ=3与作者模型。
- **Open Questions:** full-vocabprojection如何稀疏/分片；embedding更新后cache/artifact如何失效；audio/video连续状态是否被语言几何过度压缩；representation identity怎样进入serving contract。

### ZebraLogic / Complexity-Controlled Logical Reasoning Evaluation

- **Candidate / Week / Score:** ZebraLogic / 2025-W06 / 24/30。
- **Source Family ID:** `zebralogic-complexity-controlled-reasoning-benchmark`。
- **Source Type:** arXiv v1 benchmark/systematic evaluation paper + Z3-generated dataset。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-07-15。W06锁定v1 model snapshot与dataset/evaluation contract。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01100v1；https://arxiv.org/abs/2502.01100。
- **Related Primary Sources:** Z3、LMSYS/Arena、RewardBench、evaluated model cards与logic-grid task definitions用于交叉解释，不替代作者实验。
- **Access and Verification Status:** Full Source Review Complete；CSP formulation、dataset generator、search-space/Z3-conflict metrics、model/test-time scaling、token analysis、self-refinement与appendices已核验。
- **Full-read Coverage:** 已读 problem/dataset generation、unique-solution/minimal-clue procedure、theoretical/effective complexity、one-shot evaluation、model-size scaling、BoN/majority/RM/self-verify、hidden/visible token analysis、related work与prompts/appendices。
- **Original Problem:** static reasoning benchmarks缺少可控难度，难区分模型记忆、线性deduction与需要backtracking的search；只看平均accuracy会掩盖随complexity突然崩溃。
- **Why the Previous Design Was Reasonable:** 人工benchmark更自然，单一accuracy便于leaderboard；model-size和CoT长度是可获得的proxy；通用reward model降低每任务构建verifier成本。
- **Changed Constraint:** 需要把任务difficulty与state-space/backtracking显式绑定，测试参数规模、sample数量、verifier与reasoning tokens能否跨complexity threshold。
- **Mechanism:** 随机生成attribute/value solution grid与clues，逐步删clue仍保持unique solution；把puzzle形式化为CSP，以search-space size分Small～X-Large，并让Z3运行32次的平均conflicts作为effective backtracking complexity。
- **State Ownership:** generated solution/clues拥有ground truth；CSP variables/constraints拥有formal state；Z3 conflicts拥有solver-relative difficulty；candidate grids/reasoning traces与selector分别拥有inference/commit state。
- **Control Flow / Data Flow:** sample attributes/values→generate solution/clues→remove clue while uniqueness holds→Z3 complexity→one-shot prompt model→parse JSON grid→grid/cell accuracy→按size/conflicts分析model/compute scaling。
- **Implementation Details:** 所有模型共用prompt、greedy decode和parser；o1因不支持greedy运行3次取best。BoN最多128 candidates，另比较majority、Skywork reward model、self-verify与oracle selector。
- **Evaluation Contract:** grid-level exact match与cell accuracy；模型覆盖open/proprietary，从小模型到Llama3.1-405B、GPT-4o/o1/Claude/DeepSeek-R1；complexity bins `<10^3`、`10^3～10^6`、`10^6～10^9`、`>10^9`。
- **Baselines / Ablations / Sensitivity / Overhead:** model size、BoN32/128、oracle/majority/RM、自验证、hidden/visible reasoning tokens、Z3 conflicts；oracle Pass@k远高于可实现selectors，majority随N增大不保证继续改善。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model versions、sample counts、prompting与complexity披露；API hardware/precision、output cap、batch/concurrency、cost/latency SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在合成logic-grid合同中，accuracy随formal/effective complexity急剧下降，单纯参数扩展、通用reward和self-verify无法兑现oracle candidate coverage；test-time compute瓶颈包含selector质量。
- **What It Does Not Prove:** 不证明LLM普遍不会逻辑推理、不证明Z3 conflicts是人类/LLM绝对难度、不证明更长hidden tokens因果导致成功，也不证明oracle曲线可由实际系统达到。
- **Limitations / Threats to Validity:** synthetic templates/one-shot format、closed model不透明、o1取best而非同decode、API版本漂移、reward不专用、后续R1结果与v2 revisions会影响snapshot。
- **Trade-offs / New Failure Modes:** 可控复杂度提高诊断性但降低生态有效性；exact-grid metric严格却放大单cell error；更多sampling增加coverage同时增加selector、cost与state管理问题。
- **Where the Previous Design Still Applies:** 自然benchmark适合真实语言分布；cell metrics适合局部进展；symbolic solver适合可形式化任务；majority适合答案分布集中；model scaling仍改善低/中复杂度。
- **Evolution Relationship:** `Direct Evolution`：static average benchmark→generated unique CSP→search-space bins→solver-conflict effective complexity→search/verification scaling audit。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `AGENT-PLANNING` Ch79、`AGENT-REFLECTION` Ch80与`INFER-SCHEDULING` Ch56。
- **Target and Adjacent Chapters Read:** 已核对 Ch56、Ch66～67、Ch79～81的compute/evidence/planning boundary。
- **Existing Coverage:** Books 已区分model capability、harness与verifier；本family补充complexity-conditioned contract和oracle-vs-selector gap，本轮只登记。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06与年度账本；不把closed-model token分析写成内部机制证明。
- **Open Questions:** 如何构造跨domain complexity axis；Z3 conflict是否能预测LLM difficulty；specialized verifier能否缩小oracle gap；长trace如何评估过程正确性。

### AceCoder / Automated Test-Case Synthesis for Code Reward and RL

- **Candidate / Week / Score:** ACECODER / 2025-W06 / 24/30。
- **Source Family ID:** `acecoder-test-synthesis-code-reward-rl`。
- **Source Type:** arXiv v1 research paper + dataset/reward-model artifact。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-02-06；v3 2025-02-10；v4 2025-05-24。W06锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01718v1；https://arxiv.org/abs/2502.01718。
- **Related Primary Sources:** Magicoder/StackPyFunction seed datasets、HumanEval/MBPP/BigCodeBench/LiveCodeBench与Reinforcement++资料定义data、execution与RL contract。
- **Access and Verification Status:** Full Source Review Complete；test synthesis/filtering、preference construction、RM/BoN、RL setups/results、ablations与reward-hacking boundary已核验。
- **Full-read Coverage:** 已读 formulation/RM/PPO、AceCode-89K generation/filter/pairs、on-policy RM、7B/32B training、four benchmark families、BoN scaling、general RM comparison、test-filter/backbone ablations、rule/RM RL与related work。
- **Original Problem:** general reward models偏好style而非程序correctness；code RL需要大量可执行tests，但许多instruction data没有可靠test suite，直接用生成tests会含错误或环境噪声。
- **Why the Previous Design Was Reasonable:** binary pass/fail是强ground truth但只适用于已有tests；general RM覆盖广且无需sandbox；human/teacher preference可处理非执行quality。
- **Changed Constraint:** 需要把大量code instructions转成execution-grounded preference/reward data，并让RM与policy输出分布接近，支持BoN和RL而不为每题人工写tests。
- **Mechanism:** 从三个seed sources取问题/参考程序，用Qwen2.5-Coder-32B-Instruct合成tests与candidate programs；按candidate pass-rate过滤noisy tests，得到89K questions/300K tests；只用0.2～0.8 pass-rate差且排除0-pass无效程序构造on-policy pairs，full-tune scalar RM。
- **State Ownership:** problem/reference程序拥有spec proxy；tests/sandbox拥有executable oracle；filter阈值拥有data acceptance；candidate program/pass vector拥有preference state；RM与policy checkpoints拥有learned scoring/generation state。
- **Control Flow / Data Flow:** seed problem+reference→synthetic tests→candidate execution/pass matrix→test filtering→preference pairs→AceCode-RM→BoN selection或RL rollout→rule/RM reward→policy update→held-out executable benchmarks。
- **Implementation Details:** RM 7B/32B，last-token scalar head；LlamaFactory、DeepSpeed ZeRO-3、bf16、batch128、1 epoch、8×A100约24h。RL用hard 25% subset、rollout batch256、每题8 programs、batch128、lr5e-7、8×H100约6h。
- **Evaluation Contract:** HumanEval/MBPP Plus、BigCodeBench completion/instruct full/hard、LiveCodeBench V4；BoN最多64；RL从Qwen2.5 7B base/instruct与其他初始policy出发，比较rule reward和AceCode-RM。
- **Baselines / Ablations / Sensitivity / Overhead:** greedy/average/oracle/RM BoN、InternLM/Skywork RMs、with/without test filter、RM backbone match、rule vs RM RL。filter平均改善但个别benchmark下降；RM RL可退化，作者归因reward hacking。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A100/H100、bf16、model/batch/epoch/rollout披露；sandbox isolation、test timeout、sequence lengths、inference concurrency、wall-clock distribution与serving SLO不完整。
- **What the Evidence Actually Proves:** 在作者Python/code数据与benchmarks中，自动test经过execution-based filtering后可训练比通用RM更适合code selection的RM；rule reward对某些RL设置比learned RM稳健。
- **What It Does Not Prove:** 不证明synthetic tests等价完整spec、不证明RM提升所有model/task、不证明作者平均分跨数据污染/语言成立，也不证明RL improvement来自general reasoning而非benchmark-adjacent execution patterns。
- **Limitations / Threats to Validity:** test generator/reference可能共同错误，0-pass可能是环境而非code，sandbox/package依赖、seed/benchmark contamination、Python偏重、RM-policy family相关性与reward hacking限制外推。
- **Trade-offs / New Failure Modes:** executable signal更客观却增加sandbox成本、安全风险与flaky tests；过滤提高precision但丢掉hard/环境错误样本；learned RM降低online execution成本但再次引入proxy gaming。
- **Where the Previous Design Still Applies:** rule reward适合tests可靠且可执行；general RM适合风格/解释；human review适合spec不完整；static SFT适合sandbox成本过高；formal verification适合高保证代码。
- **Evolution Relationship:** `Direct Evolution`：general preference RM→available-test rule reward→synthetic tests→execution-filtered pairs→code-specific RM→rule/RM RL分支。
- **ROADMAP Node:** `TRAIN-RLHF`（Ch31）主 owner；handoff `TRAIN-GRPO` Ch33、`PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-SECURITY` Ch72与Agent tool sandbox。
- **Target and Adjacent Chapters Read:** 已核对 Ch31～34、Ch66、Ch72与Ch78～81的reward/evaluator/execution boundary。
- **Existing Coverage:** Books 已覆盖executable reward与reward hacking；本family补充test lifecycle、filter threshold和rule-vs-RM演进，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06与年度账本；作者headline绑定Python benchmarks/BoN/RL合同，不外推通用coding-agent能力。
- **Open Questions:** synthetic test如何做mutation/coverage；sandbox state如何复现；RM何时fallback在线执行；跨语言/build-system与hidden tests如何迁移。

### AStar / MCTS-Automated Structured Thinking for Multimodal Reasoning

- **Candidate / Week / Score:** AStar / MCTS for Multimodal Reasoning / 2025-W06 / 23/30。
- **Source Family ID:** `astar-mcts-multimodal-thought-cards`。
- **Source Type:** arXiv v1 research paper + algorithm/evaluation appendix；后续同family title/revision。
- **First-public Date / Revision History:** v1 2025-02-04；v2 2025-02-08；v3 2025-05-30；v4 2026-01-21；v5 2026-02-28。W06仅使用v1 “MCTS-Automated Structured Thinking”合同。
- **Direct Primary Sources:** https://arxiv.org/html/2502.02339v1；https://arxiv.org/abs/2502.02339。
- **Related Primary Sources:** Qwen2-VL、MathVista/MathVerse/MathVision/GAOKAO-MM、AR-MCTS、Mulberry与vLLM primary资料定义base/task/runtime比较。
- **Access and Verification Status:** Full Source Review Complete；v1 action space、MCTS card construction、adaptive reasoning/verification、benchmarks、efficiency/OOD/ablations与appendix implementation已核验。
- **Full-read Coverage:** 已读 structured-reasoning背景、six actions、UCT/expansion/simulation/backprop、500-seed thought cards、card matching、reason/verify、four benchmark groups、tree baselines、OOD/ablation、algorithm details与implementation。
- **Original Problem:** multimodal direct prediction缺少稳定长推理；per-query MCTS昂贵，teacher rationale distillation又依赖大量proprietary data，固定reasoning template无法适配不同visual problems。
- **Why the Previous Design Was Reasonable:** online tree search按题探索、无需训练；large teacher distillation把search cost离线化；fixed CoT prompt简单可复现，适合任务分布较窄。
- **Changed Constraint:** 只有少量seed与有限inference iterations，希望把多题search提炼成可复用高层reasoning pattern，并按新题选择而非每题重建大树。
- **Mechanism:** 定义visual parsing/system analysis/one-step/CoT/divide-and-conquer/self-reflection六actions；对500 seeds用MCTS生成valid paths并归纳thought cards；新题匹配五张cards作为外部guidelines，再由MLLM adaptive reason并以self-consistency或outcome RM验证。
- **State Ownership:** MCTS nodes拥有question+partial reasoning；action space拥有transition vocabulary；process/outcome rewards拥有search value；thought-card store拥有跨题derived strategy；matcher/verifier拥有selection/commit policy。
- **Control Flow / Data Flow:** seed multimodal problems→MCTS selection/expansion/simulation/backprop→best paths→card synthesis→target problem→card match→guided reasoning→self-consistency/outcome verification→answer。
- **Implementation Details:** v1使用0.5K prior samples、每sample平均5 search iterations；vLLM，temperature0.8、top-p0.9、max1024 tokens，Ubuntu22.04+A100-80GB；Qwen2-VL 2B/7B为主要backbones。
- **Evaluation Contract:** MathVista、MathVerse、MathVision及general/OOD tasks（MMStar、ChartQA、GAOKAO-MM）；比较general/math-specialized/closed MLLMs和AR-MCTS/Mulberry，另测data量、iterations与component ablations。
- **Baselines / Ablations / Sensitivity / Overhead:** random actions/card/selection、无self-consistency、不同card数量/verification；作者报告每组件均有贡献，0.5K/5 iterations对比34.5K/更多iterations与260K training-data方案，但成本口径并不完全等价。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** A100-80GB、Qwen2-VL、sampling/max tokens、seed/iterations披露；GPU数量、precision、image resolution、batch/concurrency、per-query latency/cost/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者multimodal benchmarks中，从小seed MCTS paths归纳thought cards并复用，可改善所测Qwen2-VL reasoning并减少相对tree baselines的在线iterations。
- **What It Does Not Prove:** 不证明cards是因果/通用认知结构、不证明比同成本fine-tuning或prompt search更优、不证明OOD结果排除benchmark contamination，也不证明后续v5 thought-card机制等同v1。
- **Limitations / Threats to Validity:** card/action人为定义、reward/verifier偏差、closed baseline不等价、small seed可能过拟合、图片/task coverage有限；论文未单列limitations，以上为method/evaluation可见边界。
- **Trade-offs / New Failure Modes:** amortized search降在线成本，却引入derived-memory provenance、card staleness/mismatch、reward-shaped pattern、selector error和错误strategy复用；card数量增大也会占context。
- **Where the Previous Design Still Applies:** per-query MCTS适合novel high-value题；teacher distillation适合稳定大数据；direct CoT适合低延迟；tool/symbolic solver适合可执行视觉数学。
- **Evolution Relationship:** `Direct Evolution`：direct prediction→online structured search→teacher rationale distillation→search-derived reusable thought cards→adaptive card+verification；后续revision另行审计。
- **ROADMAP Node:** `AGENT-PLANNING`（Ch79）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23、`AGENT-MEMORY` Ch77、`AGENT-REFLECTION` Ch80与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～26、Ch77～81与Ch66的representation/derived strategy/verifier boundary。
- **Existing Coverage:** Books 已覆盖planning与derived memory；本family补充MCTS→thought-card amortization和provenance failure，本轮不修改Books。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06与年度账本；v2～v5 title/mechanism/results不作为W06事件证据。
- **Open Questions:** thought card如何版本化/淘汰；matcher置信度怎样触发full search；错误card如何归因rollback；跨model/action schema是否可迁移。

### JUMP / Universal Multi-Prompt Jailbreaking

- **Candidate / Week / Score:** JUMP / Universal Multi-Prompt Jailbreak / 2025-W06 / 23/30。
- **Source Family ID:** `jump-universal-multiprompt-jailbreak-defense`。
- **Source Type:** arXiv v1 attack/defense research paper + appendix experiments。
- **First-public Date / Revision History:** v1 2025-02-03；截至核验无后续arXiv revision。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01154v1；https://arxiv.org/abs/2502.01154。
- **Related Primary Sources:** AdvBench、BEAST、AdvPrompter、AutoDAN、GPTFuzzer、SmoothLLM、Llama Guard原始资料定义attack/defense baselines与judge。
- **Access and Verification Status:** Full Source Review Complete；objective、BEAST→JUMP*/JUMP/JUMP++、perplexity constraint、victims/metrics、transfer/defense/ablation、hyperparameters与limitations已核验。
- **Full-read Coverage:** 已读 prompting/finetuned attacks与defenses、universal multi-prompt objective、beam mutation/evaluation/constraint、AdvBench split、open/closed victims、ASR/perplexity、baseline/transfer/defense results、appendix setup与limitations。
- **Original Problem:** per-input adversarial suffix搜索成本高、泛化弱；单个universal prompt覆盖不足，而纯优化suffix通常高perplexity、易被filter检测。
- **Why the Previous Design Was Reasonable:** individual search能贴合具体target；single universal prompt部署简单；perplexity filter便宜；handcrafted templates可读且可迁移部分语义攻击。
- **Changed Constraint:** 攻击者希望用一组prompts覆盖多malicious instructions/模型，同时控制naturalness；防御也需面对“任一prompt成功”而非单prefix。
- **Mechanism:** 将目标改为对instruction set最小化“prompt set中最佳suffix”的loss；JUMP*把BEAST beam搜索扩成multi-prompt mutation/evaluation，JUMP按inverse perplexity temperature重采样候选；JUMP++加入handcrafted initialization。作者还反向优化DUMP defense prompt。
- **State Ownership:** prompt set/beam拥有universal attack population；mutator生成suffix；victim loss/evaluator拥有fitness；perplexity constraint拥有stealth policy；Llama Guard/string judge拥有ASR标签；defense prompt拥有counter-policy。
- **Control Flow / Data Flow:** AdvBench train instructions→initialize multi-prompts→token mutation/beam expansion→victim target-loss evaluation→perplexity-constrained resampling→prompt set→test instructions/transfer victims→ASR@k、PPL与defense evaluation。
- **Implementation Details:** victims含Llama2/3-7/8B、Mistral7B、Vicuna7B、Gemma7B及GPT-3.5/4/4o transfer；metrics为string refusal、Llama Guard与perplexity；defense每case time limit 300/480秒，SmoothLLM/DUMP各50 augmentations。
- **Evaluation Contract:** AdvBench沿AdvPrompter train/test split；比较AdvPrompter、AutoDAN、GPTFuzzer、BEAST/JUMP variants；报告ASR@1/@10、不同judge、perplexity、open→closed transfer与SmoothLLM/DUMP defense。
- **Baselines / Ablations / Sensitivity / Overhead:** single vs multi-prompts、JUMP*无PPL、JUMP constrained、JUMP++ handcrafted、initialization、ASR/PPL trade-off、transfer、defense augmentation；结果高度依赖初始化与evaluator。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** victim/proxy models、beam/timeout/augmentation部分披露；GPU/precision、完整token/call成本、parallelism、API versions与production SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者AdvBench/模型/judge合同中，prompt set优化比单prompt提高覆盖，perplexity constraint与handcrafted seed可在ASR/stealth间折衷；transfer和defense均存在显著条件依赖。
- **What It Does Not Prove:** 不证明攻击在真实产品policy/tool环境成功、不证明PPL等价可读性/不可检测、不证明Llama Guard/string ASR等价真实伤害，也不证明DUMP是普适防御。
- **Limitations / Threats to Validity:** JUMP难兼顾可读性与效率，JUMP++依赖handcrafted initialization；AdvBench/target-prefix窄、judge bias、closed API drift和攻击披露风险限制外推。
- **Trade-offs / New Failure Modes:** multi-prompt提高coverage却扩大storage/search/evaluation成本；stealth约束降低可检测性但可能牺牲ASR；训练型defense可能过拟合已知attacks并影响benign utility。
- **Where the Previous Design Still Applies:** per-input search适合高价值target；single universal prompt适合小attack surface；simple filters适合快速guardrail；semantic/policy/tool-level defenses适合真实deployment。
- **Evolution Relationship:** `Direct Evolution`：individual adversarial suffix→single universal prompt→universal prompt set→perplexity-constrained set→handcrafted initialization；defense是对抗共演化分支。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66、`AGENT-CONTEXT` Ch75与`AGENT-WORKFLOW` Ch81。
- **Target and Adjacent Chapters Read:** 已核对 Ch66～73与Ch74～81的threat/evaluator/context/workflow boundary。
- **Existing Coverage:** Books 已覆盖adversarial prompt与defense co-evolution；本family补充set-valued attack state和ASR–stealth trade-off，本轮仅登记。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新W06与年度账本；不复述危险prompt，不把作者ASR当作deployment compromise概率。
- **Open Questions:** prompt-set coverage如何定义；defender如何按family去重攻击；PPL以外的semantic detector怎样评估；attack/defense traces如何安全保存。

### ReasoningWeekly / PhD Knowledge Not Required

- **Candidate / Week / Score:** ReasoningWeekly / PhD Knowledge Not Required / 2025-W06 / 22/30。
- **Source Family ID:** `reasoningweekly-general-knowledge-verifiable-reasoning`。
- **Source Type:** arXiv v1 benchmark paper + dataset/evaluation protocol；后续同 family title revision。
- **First-public Date / Revision History:** v1 2025-02-03，题为 “PhD Knowledge Not Required”；v2 2025-02-06；v3 2025-03-31；v4 2025-11-26 改题为 ReasoningWeekly。W06 锁定 v1，后续 revision 仅用于 family lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01584v1；https://arxiv.org/abs/2502.01584。
- **Related Primary Sources:** NPR Sunday Puzzle transcript/data origin，以及 o1、o3-mini、Gemini Thinking、DeepSeek-R1 的官方 model/system materials只定义被测对象，不替代本文测量。
- **Access and Verification Status:** Full Source Review Complete；v1 dataset construction、prompt/evaluator、model configuration、main results、give-up/stuck/uncertainty分析、reasoning-length曲线与 conclusion 已核验。
- **Full-read Coverage:** 已读 Abstract、Related Work、13年 transcript清洗、context/alternative-answer处理、zero-shot contract、595题结果、失败案例、32K/128K预算复测、length plateau 与 conclusion；v2～v4结论未回灌 W06。
- **Original Problem:** 专家型 benchmark 难以由普通 reviewer 理解和验证，可能掩盖模型在一般知识搜索、约束满足和停止决策上的能力差异。
- **Why the Previous Design Was Reasonable:** 高难数学、代码和学科题可推动 frontier ceiling，并提供可自动评分答案；对专业能力评估仍不可替代。
- **Changed Constraint:** 推理模型开始消耗大量 test-time tokens，系统不仅要测最终正确率，还要测普通人可验证的问题、搜索失败、commit行为和预算耗尽。
- **Mechanism:** 从13年 NPR off-air weekly challenges构建近600题数据，补齐日期/地域上下文、移除多解题并规范答案；模型零样本自由生成，以大小写/标点无关的 gold phrase inclusion判分，再分析显式放弃、重复、正确答案后撤销和 reasoning length。
- **State Ownership:** dataset revision拥有题目与gold identity；model runtime拥有reasoning trace/token budget；answer extractor拥有commit边界；evaluator拥有字符串正确性；人工分析拥有failure taxonomy。
- **Control Flow / Data Flow:** transcripts→人工清洗/过滤→595 challenges→各model zero-shot generation→reasoning/final-answer split→phrase evaluator→accuracy/length/failure analysis→budget policy问题。
- **Implementation Details:** o1/o1-mini temperature 1；Gemini Thinking default 0.7；R1 temperature 0.6、top-p 0.95、output cap 32,768；GPT-4o/Sonnet temperature 0.2、top-p 0.95；另对两个最坏case以128K复测。
- **Evaluation Contract:** 595道美国文化偏重的wordplay/general-knowledge puzzles；o1、o3-mini、o1-mini、Gemini 2.0 Flash Thinking Experimental 01-21、DeepSeek-R1，GPT-4o-2024-11-20与Claude-3-5-sonnet-20241022作非reasoning baselines；指标为phrase-match accuracy、unfinished/give-up counts和reasoning length分布。
- **Baselines / Ablations / Sensitivity / Overhead:** 不同model/reasoning effort与32K→128K budget sensitivity；R1在142/595 reasoning中显式give up，50题触及32K未结束；两个最坏case扩至128K仍各有2/10未完成。没有同模型多seed全面方差或人工多评审者一致性。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/API版本、temperature、top-p与32K/128K length已披露；hardware、precision、batch/concurrency、latency/cost和deployment SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在该 v1 dataset/prompt/evaluator下，模型排序与专业知识benchmark不同；可观察到放弃、反复搜索、找到正确答案后继续探索和预算内不终止等运行时failure。
- **What It Does Not Prove:** 不证明一般推理能力可由单一美国文化题集代表，不证明可见reasoning是完整内部过程，不证明约10K或3K token拐点可外推其他task/model，也不证明string inclusion等价解释正确。
- **Limitations / Threats to Validity:** U.S.-centric language/culture、transcript清洗与gold completeness、single prompt、API/model drift、不同模型可见trace语义不等价；论文未提供完整human baseline和污染审计。
- **Trade-offs / New Failure Modes:** 可验证题降低审查门槛，却引入文化偏差；增加token budget提高部分准确率但放大成本、尾延迟和non-termination；过早wrap-up又可能截断可恢复搜索。
- **Where the Previous Design Still Applies:** 专业benchmark仍适合domain competence；短固定预算适合低延迟服务；tool-backed/executable evaluator适合可形式化任务；人工审查适合多解或文化语义题。
- **Evolution Relationship:** `Layering / Dependency`：domain-hard benchmark→human-verifiable hard search→trace/failure analysis→budget-aware stopping and commit policy；不是用新题集替代专业评测。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `INFER-SCHEDULING` Ch56与`AGENT-REFLECTION` Ch80。
- **Target and Adjacent Chapters Read:** 已核对 Ch66～68 的evidence contract，以及 Ch56/80的budget、stop和commit边界。
- **Existing Coverage:** Books 已区分能力、harness与deployment evidence；本 family 新增 human-verifiability 和 reasoning non-termination measurement，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；不保留脱离prompt/model/version/budget的headline accuracy。
- **Open Questions:** 如何建立跨文化等价题集；何种stop controller可在尾延迟与可恢复搜索间校准；trace不可见模型如何测non-termination与premature commit。

### RandLoRA

- **Candidate / Week / Score:** RandLoRA / 2025-W06 / 22/30。
- **Source Family ID:** `randlora-full-rank-random-basis-peft`。
- **Source Type:** arXiv v1 / ICLR 2025 paper + official code artifact。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-03-12；W06机制与实验锁定v1。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.00987v1；https://arxiv.org/abs/2502.00987；https://github.com/PaulAlbert31/RandLoRA。
- **Related Primary Sources:** LoRA、VeRA、NoLA、DoRA与full fine-tuning原始资料定义rank/parameter/memory baselines。
- **Access and Verification Status:** Full Source Review Complete；25页v1 PDF的SVD动机、random-basis parameterization、theorem、vision/language/multimodal experiments、rank/sparsity/activation/loss-landscape ablations、runtime与limitations已核验。
- **Full-read Coverage:** 已读 Introduction/Related Work、LoRA rank study、Method/Convergence、21视觉数据集、CLIP与8项commonsense tasks、CKA/mode connectivity、sparse bases、training-time appendix、proof与hyperparameters。
- **Original Problem:** LoRA通过低秩更新降低trainable state，但在需要更高更新rank的任务上，即便增加参数也可能出现性能平台。
- **Why the Previous Design Was Reasonable:** 许多迁移任务的有效更新近似低维；LoRA显著降低optimizer/gradient memory、实现成熟且易合并，资源受限和小数据场景收益明确。
- **Changed Constraint:** 复杂vision-language或大数据适配可能需要覆盖更完整的singular spectrum，同时仍无法承担full fine-tuning的可训练参数规模。
- **Mechanism:** 将更新写成多组固定、线性独立的random low-rank basis之和，只学习basis两侧的diagonal scaling；在论文假设下各项及其和几乎必然full rank，以更粗的SVD近似换取更广的rank coverage。
- **State Ownership:** base weight保持冻结；random bases是固定artifact；diagonal scaling拥有trainable adaptation state；rank/basis count/sparsity拥有capacity contract；merged update拥有部署状态。
- **Control Flow / Data Flow:** pretrained weight→初始化fixed random bases→forward组合full-rank update→只对diagonal scales反传/优化→adapter checkpoint→可选merge进base weight。
- **Implementation Details:** vision侧ViT-B/14、ViT-B/32、ViT-L/14、ViT-H/14；language侧Qwen2-0.5B、Phi3-3B、Llama3-8B；LLM训练3 epochs、LR 1e-4、dropout 0.05，RandLoRA basis rank随model取6/10/15，basis count约149/153/136。
- **Evaluation Contract:** 21个image-classification datasets的few/full-data设置、CLIP vision-language分类与8个commonsense datasets；15K与170K language data；比较FT、LoRA、VeRA、NoLA、部分DoRA，报告accuracy、VRAM、training time、CKA和loss landscape。
- **Baselines / Ablations / Sensitivity / Overhead:** equal-parameter LoRA/RandLoRA、更新rank、random distribution、66%～99% sparsity、data size、architecture；推荐稀疏度可接近dense表现，过高稀疏度退化；训练时间随大矩阵明显增加。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** vision主要single RTX4090/A100，Llama3与ViT-H/14用A100；CLIP accumulated batch 128，LLM batch 16/8/4；precision、sequence length、concurrency与SLO `Not Disclosed`。作者表中Llama3-8B RandLoRA约为LoRA的167% training time、102% memory，最佳大配置另报告最高212% time increase，不能跨配置混用。
- **What the Evidence Actually Proves:** 在作者模型、数据与参数匹配下，full-rank random-basis update可在部分高适配需求场景缩小LoRA与FT差距，尤其CLIP/较大language data；收益与任务和budget相关。
- **What It Does Not Prove:** 不证明所有adapter都受rank而非optimization限制，不证明随机basis最优，不证明相同trainable parameters等于相同FLOPs/wall time，也不证明对生成式LLM、长序列或生产训练普遍更优。
- **Limitations / Threats to Validity:** 计算overhead与缺少优化kernel；理论界依赖每个random factor能近似SVD block的假设；任务/模型规模有限；full Llama3 FT未因资源限制运行，部分比较缺少完整等成本基线。
- **Trade-offs / New Failure Modes:** 扩大rank coverage但增加basis组合matmul、checkpoint metadata和kernel复杂度；固定随机basis可能conditioning差；高capacity在15K小数据上也会过拟合。
- **Where the Previous Design Still Applies:** LoRA适合小数据、低rank任务和成熟serving；full FT适合最高质量且资源充足；VeRA/NoLA适合极小parameter budget；DoRA等分支适合不同weight decomposition假设。
- **Evolution Relationship:** `Alternative Branch`：full FT→low-rank adapter→random ultra-compact basis→full-rank random-basis adapter；不是LoRA的无条件替代。
- **ROADMAP Node:** `TRAIN-LORA`（Ch30）主 owner；handoff `TRAIN-PRETRAINING` Ch28、`PLATFORM-MODEL-REGISTRY` Ch59与execution/kernel owner。
- **Target and Adjacent Chapters Read:** 已核对 Ch28～31、Ch35与Ch59的trainable state、checkpoint、artifact identity和部署合并边界。
- **Existing Coverage:** Books 已覆盖LoRA的rank/optimizer-state trade-off；本 family 补充“parameter count不等于update rank”分支，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；训练开销和accuracy严格绑定作者配置。
- **Open Questions:** random basis如何做conditioning/seed复现；adapter合并后如何追踪basis provenance；何时由rank diagnostic触发LoRA→full-rank branch。

### Improved Training Technique for Latent Consistency Models

- **Candidate / Week / Score:** Improved Latent Consistency Training / 2025-W06 / 22/30。
- **Source Family ID:** `latent-consistency-robust-outlier-training`。
- **Source Type:** arXiv v1 generative-model training paper。
- **First-public Date / Revision History:** v1 2025-02-03；v2 2025-03-25；W06锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01441v1；https://arxiv.org/abs/2502.01441。
- **Related Primary Sources:** consistency training/distillation、latent diffusion、OT coupling与robust loss原始论文定义baseline genealogy。
- **Access and Verification Status:** Full Source Review Complete；latent/pixel统计分析、五项训练改动、公式、实验、component ablation与appendix已核验。
- **Full-read Coverage:** 已读 preliminaries、latent TD outlier分析、Cauchy loss、small-timestep diffusion loss、minibatch OT、adaptive c、NsLN、CelebA-HQ/LSUN/FFHQ实验、ablation与conclusion。
- **Original Problem:** pixel-space improved consistency training迁移到VAE latent后性能显著下降，1～2 step优势被严重的temporal-difference outlier与训练方差抵消。
- **Why the Previous Design Was Reasonable:** Pseudo-Huber在pixel data可抑制一般outlier；consistency objective直接优化跨noise-level一致性，避免多步sampling；标准LayerNorm和独立noise pairing实现简单。
- **Changed Constraint:** latent representation的重尾/impulsive outlier更强，且早期small timestep的consistency target不稳定，原robustness常数与normalization不再匹配数据统计。
- **Mechanism:** 以Cauchy loss进一步压低极端TD影响；small timesteps加入diffusion loss；minibatch OT重配noise-data降低variance；按discretization curriculum自适应robustness scale c；移除LayerNorm multiplicative scale形成NsLN。
- **State Ownership:** VAE拥有latent distribution；noise schedule/discretization拥有time state；consistency network与EMA target拥有prediction state；OT matcher拥有batch pairing；loss scheduler拥有robustness policy。
- **Control Flow / Data Flow:** image→VAE latent→sample/reassign noise pair→相邻noise levels→consistency prediction/EMA target→Cauchy TD loss；small t并行diffusion loss→adaptive c/NsLN稳定反传→1/2-step sampler。
- **Implementation Details:** VE forward process、Exp discretization从10增长至640 steps；POT library执行minibatch OT，作者报告约0.93% training-time overhead；输出为256×256、1或2 NFE。
- **Evaluation Contract:** CelebA-HQ、LSUN Church与FFHQ latent datasets，CIFAR-10 pixel diagnostic；FID/Recall，1/2-NFE；同architecture/noise scheduler对比iLCT、LDM/LFM及pixel/latent generative baselines。
- **Baselines / Ablations / Sensitivity / Overhead:** 逐项加入Cauchy、small-t diffusion、OT、adaptive c、NsLN；在CelebA-HQ 1-NFE/1400 epochs同配置ablation中各组件连续改善。不同forward process和NFE使跨方法headline不可直接等价。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** dataset、resolution、epochs、total batch与NFE部分披露；GPU/accelerator、precision、wall time、concurrency与serving SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者latent image设置中，训练失败与TD重尾/variance相关，组合robust loss、early diffusion regularization、OT、adaptive scale和NsLN可显著改善iLCT的1/2-step FID/Recall。
- **What It Does Not Prove:** 不证明五组件在large text-to-image/video同样叠加，不证明1-step在同等forward process/compute下优于所有diffusion/flow方法，也不证明NsLN普适优于LayerNorm。
- **Limitations / Threats to Validity:** 数据集和分辨率有限，未覆盖text conditioning/video；组件组合存在交互而非完全独立因果；hardware和完整成本缺失；VAE latent选择影响outlier统计。
- **Trade-offs / New Failure Modes:** 强robustness可能忽略稀有但有效的大残差；OT引入batch-global coupling和额外状态；small-t双目标需调权；NsLN移除scale会限制某些feature rescaling能力。
- **Where the Previous Design Still Applies:** pixel-space consistency可继续用Pseudo-Huber；多步diffusion适合质量优先；标准LN适合activation统计稳定；独立noise pairing适合极简或小batch训练。
- **Evolution Relationship:** `Direct Evolution`：pixel consistency training→latent迁移失败→statistical diagnosis→robust loss/variance control→few-step latent generation；是训练稳定化，不是生成范式替代宣言。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `TRAIN-PRETRAINING` Ch28与execution/sampling章节。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch28与推理sampling章节的representation statistics、objective和NFE边界。
- **Existing Coverage:** Books 已覆盖AR/diffusion/iterative correction分支；本 family 提供latent统计改变训练loss的机制证据，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；作者FID只保留在完整forward-process/NFE/data合同内。
- **Open Questions:** VAE/DiT规模扩大后outlier tail如何变化；OT在distributed batch中如何确定性复现；robust c能否由在线statistics自动控制。

### COCONut-PanCap

- **Candidate / Week / Score:** COCONut-PanCap / 2025-W06 / 21/30。
- **Source Family ID:** `coconut-pancap-mask-grounded-caption-data`。
- **Source Type:** arXiv v1 dataset/multimodal research paper + dataset task contract。
- **First-public Date / Revision History:** v1 2025-02-04；截至核验无更早同family事件，W06使用v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.02589v1；https://arxiv.org/abs/2502.02589。
- **Related Primary Sources:** COCO2017、COCONut-S、Objects365、LLaVA-NeXT、GLaMM、SD3与panoptic metrics的原始资料定义source data和baselines。
- **Access and Verification Status:** Full Source Review Complete；dataset construction、human editing、PGC task/model、I2T/T2I/VQA/referring-segmentation实验、ratio ablation与limitations已核验。
- **Full-read Coverage:** 已读动机、143K split/statistics、panoptic-mask-guided two-round annotation、PanCaper、metrics/baselines、caption/PGC/generation/downstream experiments、synthetic-human mixture与limitations。
- **Original Problem:** web image-text pairs规模大但caption浅且不准确；纯synthetic dense caption可扩展却容易漏对象/属性，短COCO captions又无法监督region-level grounding和完整scene description。
- **Why the Previous Design Was Reasonable:** web/synthetic captions成本低、规模大；COCO human captions质量高且任务成熟；独立segmentation/caption任务简化标注与模型接口。
- **Changed Constraint:** fine-grained VLM和生成模型需要同一数据项同时表达thing/stuff regions、属性、关系、全局scene与可追踪mask grounding，并控制人工成本。
- **Mechanism:** 用COCONut-S panoptic masks决定必须覆盖的region/set-of-marks；商业VLM生成region-aware初稿，人工逐项校正，再合并成dense grounded caption；建立Panoptic Grounded Captioning任务与PanCaper baseline。
- **State Ownership:** image ID拥有样本identity；panoptic mask/region ID拥有spatial grounding；caption spans拥有语义描述；human edit log拥有quality gate；dataset split/version拥有reproducibility。
- **Control Flow / Data Flow:** COCO/Objects365 image→COCONut panoptic masks→set-of-marks/VLM draft→human region corrections→merged grounded caption→instruction/generation training→caption/PGC/VQA/referring/T2I evaluation。
- **Implementation Details:** 118K COCO2017 train images与25K COCONut-val（含COCO val和20K Objects365）构成约143K；平均203词、11句；caption模型可加入mask-pooled features，inference使用kMaX-DeepLab proposals。
- **Evaluation Contract:** LLaVA-NeXT/Llama3-8B detailed captioning、LISA+/GLaMM/PanCaper PGC、SD3-medium T2I，以及VQA和referring segmentation；CAPTURE/CIDEr/BLEU/METEOR/ROUGE、PQ、FID等按task使用。
- **Baselines / Ablations / Sensitivity / Overhead:** 在相同23K detailed-caption instruction量下比较多种synthetic caption来源；20K human vs 100K synthetic、mask pooling、human/synthetic ratio。作者报告加入25%人工数据时CAPTURE/FID改善，但只适用于其split/model/evaluator。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data规模与caption length披露；训练硬件、precision、batch/concurrency、annotation cost/time与serving SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者任务合同中，以panoptic inventory约束caption coverage并加入human correction，可提高所测grounded description和下游理解/生成质量；少量高质量人工数据与synthetic data具有互补性。
- **What It Does Not Prove:** 不证明mask completeness等于语义完整、不证明任意commercial VLM+human流程同样有效、不证明FID/CAPTURE充分衡量grounding，也不证明143K规模可替代web-scale data。
- **Limitations / Threats to Validity:** 人工标注难扩展；COCO/Objects365域和category bias；mask proposal误差会在inference传播；VLM draft可能锚定编辑者；不同baseline额外pretraining data不完全等价。
- **Trade-offs / New Failure Modes:** 结构化grounding提升coverage/auditability，却增加mask/version/annotation成本；dense caption可能过描述或固化annotation ontology；错误region ID会同时污染language和vision supervision。
- **Where the Previous Design Still Applies:** web-scale synthetic captions适合coverage；短human captions适合通用caption benchmark；独立segmentation适合低耦合系统；domain-specific schema适合高精度垂直场景。
- **Evolution Relationship:** `Layering / Dependency`：short global caption→synthetic dense caption→mask-constrained draft→human-verified grounded caption→joint perception/generation supervision。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～28与Ch66的数据identity、grounding、generation和evaluation contract。
- **Existing Coverage:** Books 已覆盖multimodal data provenance和alignment；本 family 补充mask作为caption coverage contract及human/synthetic mixture证据，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；不保留脱离dataset/model/metric的作者headline。
- **Open Questions:** region-caption span如何做版本化；draft anchoring如何测量；annotation quality、license与identity provenance怎样进入registry。

### Generating Multi-Image Synthetic Data / SynCD

- **Candidate / Week / Score:** Multi-Image Synthetic Data / SynCD / 2025-W06 / 22/30。
- **Source Family ID:** `syncd-multi-image-consistent-customization-data`。
- **Source Type:** arXiv v1 paper + author project/repository + dataset/model artifacts；后续ICCV accepted version同family核验。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；v2 2025-10-13；ICCV 2025 proceedings为后续publication node。W06锁定v1，后续材料仅用于核对family与公开artifact。
- **Direct Primary Sources:** https://arxiv.org/abs/2502.01720；https://www.cs.cmu.edu/~syncd-project/；https://github.com/nupurkmr9/syncd；https://openaccess.thecvf.com/content/ICCV2025/html/Kumari_Generating_Multi-Image_Synthetic_Data_for_Text-to-Image_Customization_ICCV_2025_paper.html。
- **Related Primary Sources:** https://huggingface.co/datasets/nupurkmr9/syncd；Objaverse、FLUX、SDXL/IP-Adapter与DreamBench原始资料定义data/model/baseline依赖。
- **Access and Verification Status:** Full Source Review Complete；arXiv identity/revision、作者project、CVF全文索引、official code/data的generation、MSA/warping、training/inference、ablation、runtime与limitations已核验；arXiv/CVF PDF直传失败已记录但不再阻塞正文核验。
- **Full-read Coverage:** 已读 problem/data pipeline、deformable/rigid branches、masked shared attention公式与warping、filtering、encoder training、guidance normalization、benchmarks、dataset-size/component ablations、implementation appendix与limitations。
- **Original Problem:** test-time optimization personalization昂贵；tuning-free encoders通常用互不相关的single-image data训练，缺少“同一object跨pose/background/light保持identity”的supervision。
- **Why the Previous Design Was Reasonable:** per-object optimization可精确拟合少量reference；single-image internet datasets容易规模化；独立reference encoder保持inference简单。
- **Changed Constraint:** 希望single forward personalization同时支持1～3张reference，保留细粒度identity又遵循新text composition，真实multi-view paired data不足。
- **Mechanism:** 为deformable objects用详细描述+FLUX并通过foreground masked shared attention同步生成；为rigid objects引入Objaverse multi-view depth与cross-view feature warping；DINOv2/aesthetic过滤形成SynCD；训练时target与reference features共享attention，推理时归一化text/image guidance vectors缓解过曝。
- **State Ownership:** object cluster ID拥有identity；3D asset/camera/depth拥有rigid correspondence；foreground mask拥有跨图信息边界；reference features拥有conditioning state；text/image guidance分别拥有composition与identity控制量。
- **Control Flow / Data Flow:** category/object description+background prompts/3D views→parallel diffusion with MSA/warping→quality/identity filtering→约90K object clusters×2～3 images→reference/target training→normalized dual guidance→customized image。
- **Implementation Details:** deformable与rigid走不同data path；attention只允许每图访问其他图foreground，隔离background；官方dataset card约90K objects、17.5GB；repo提供SDXL/FLUX reimplementation与最多3 reference inference。
- **Evaluation Contract:** DreamBench及customization benchmarks，比较optimization-based与encoder-based methods；DINOv2 image alignment、CLIP/text alignment和human/qualitative评估；3B与12B variants、1/3 references、single-object setting。
- **Baselines / Ablations / Sensitivity / Overhead:** 去掉warping、去掉MSA、去掉detailed descriptions、100→1K→10K→约95K dataset size；MSA改善cluster identity，rigid warping进一步改善，较小data更易过拟合。作者实现附录报告shared-attention长序列与双forward带来额外推理成本。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** accepted artifact披露H100 mixed-precision bfloat16与单次sampling实现成本片段；事件时完整GPU count、training batch/steps、resolution组合、concurrency与SLO不完整，后续FLUX repo行为不可反推v1全部实验。
- **What the Evidence Actually Proves:** 在作者single-object customization合同中，显式跨图identity coupling生成的synthetic clusters可改善encoder-based personalization；MSA、rigid warping、data scale和guidance normalization各有受限证据。
- **What It Does Not Prove:** 不证明synthetic identity等于真实object一致性、不证明multi-object/compositional scenes成立、不证明后续FLUX reimplementation等同v1模型，也不证明所测metric覆盖版权、bias或身份滥用。
- **Limitations / Threats to Validity:** 仅single object；3D assets/category覆盖有限；synthetic generator bias被继承；DINO/aesthetic filter偏好可能缩窄分布；跨图attention成本随reference tokens增长；best-of-four qualitative selection影响展示。
- **Trade-offs / New Failure Modes:** 合成paired supervision降低真实采集成本，却引入generator/filter feedback loop；MSA增强identity但可能复制背景或artifact；warping提高rigid consistency但依赖depth/correspondence；dual guidance需校准过曝与prompt adherence。
- **Where the Previous Design Still Applies:** per-object optimization适合少量高价值subject；真实multi-view拍摄适合高真实性；single-image encoders适合低成本通用服务；3D-specific方法适合几何可得的rigid objects。
- **Evolution Relationship:** `Direct Evolution`：per-object optimization→single-image tuning-free encoder→synthetic multi-image cluster→identity-coupled encoder→normalized multi-condition inference。
- **ROADMAP Node:** `TRAIN-DATA`（Ch27）主 owner；handoff `MULTIMODAL-REPRESENTATION` Ch23、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24与platform asset/provenance章节。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～28与Ch58～59的identity、generation、synthetic data和artifact provenance边界。
- **Existing Coverage:** Books 已覆盖synthetic data和multimodal condition identity；本 family 补充multi-image cluster作为监督单位及MSA/warping生成链，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；后续ICCV/FLUX材料不计为W06新事件。
- **Open Questions:** synthetic cluster如何检测identity drift；reference token增加时attention成本如何界定；multi-object identity与license/provenance如何隔离。

### Activation-Informed Model Merging

- **Candidate / Week / Score:** Activation-Informed Model Merging / 2025-W06 / 22/30。
- **Source Family ID:** `aim-activation-saliency-model-merge`。
- **Source Type:** arXiv v1 model-merging paper + official code/checkpoints。
- **First-public Date / Revision History:** v1 2025-02-04；v2 2025-06-14；v3 2025-11-06；W06锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.02421v1；https://arxiv.org/abs/2502.02421；https://github.com/ahnobari/ActivationInformedMerging。
- **Related Primary Sources:** DARE、TIES、WIDEN、Task Arithmetic、AWQ与Llama-2-13B expert checkpoints原始资料定义merge/calibration baselines。
- **Access and Verification Status:** Full Source Review Complete；v1 activation-error derivation、AIM relaxation、five merge algorithms、six benchmarks、hypervolume metric、omega ablation、reproducibility artifacts与evidence boundary已核验。
- **Full-read Coverage:** 已读 background/continual-learning analogy、activation saliency公式、merge wrapper、calibration data、experts/baselines/metrics、20 merge cases、omega sensitivity、appendix checkpoints/code/data与conclusion。
- **Original Problem:** weight-space merge把fine-tuned deltas组合时会破坏base model中对通用能力重要的weights；单benchmark改善又可能掩盖其他能力退化。
- **Why the Previous Design Was Reasonable:** task arithmetic/TIES/DARE只需checkpoints、不需训练数据，部署便宜；weight magnitude和delta conflict是直接可操作信号；每个expert单独服务仍可保真。
- **Changed Constraint:** 希望一个artifact整合多个expert并保留generalist能力，需要区分“相同delta对不同activation channel造成的输出影响”，同时用multi-objective而非单分数判断。
- **Mechanism:** 用Pile validation calibration输入记录base model各层channel activation magnitude，形成base-weight saliency；先由任意merge algorithm得到delta，再按saliency和omega缩小对重要base weights的更新，因此AIM是algorithm-agnostic post-merge relaxation wrapper。
- **State Ownership:** base checkpoint拥有reference parameters；expert checkpoints拥有task deltas；calibration set/activation statistics拥有saliency；merge algorithm拥有delta composition；omega拥有base retention与expert transfer折衷。
- **Control Flow / Data Flow:** base+same-origin experts→chosen merge algorithm→merged delta；calibration prompts→base activations→saliency map→omega-weighted delta relaxation→merged artifact→six-benchmark/Pareto-HV evaluation。
- **Implementation Details:** Llama-2-13B base与code/instruction/math experts；Pile validation calibration；五种merging methods、2/3 expert四种组合；AIM实验固定omega 0.4并另做sweep；公开code、calibration data和merged checkpoints。
- **Evaluation Contract:** HumanEval、MBPP、MMLU、MATH、GSM8K、IFEval；除单项accuracy外，以base+experts的Pareto frontier计算normalized hypervolume gain，观察merged model是否新增multi-objective coverage。
- **Baselines / Ablations / Sensitivity / Overhead:** AIM on/off跨20个merge cases、omega sensitivity；作者称80% cases HV改善，但若干GSM8K/IFEval等单项下降，表明regularization不是单调收益。缺少不同calibration distribution/size和独立base family系统ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** checkpoint/benchmark/calibration来源披露；hardware、precision、calibration sample count/length、merge wall time、serving concurrency与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在这组三个Llama-2-13B experts、五种merge方法和六指标下，activation-conditioned relaxation经常改善multi-objective balance，并揭示base retention与expert gain的omega折衷。
- **What It Does Not Prove:** 不证明activation magnitude是通用因果importance、不证明对不同base/architecture/quantized adapters成立、不证明HV选择代表deployment utility，也不证明merged artifact可替代保留专家routing。
- **Limitations / Threats to Validity:** 单一base family/三个experts；WizardMath权重为公开copy、可能与baseline原实验不一致；Pile calibration distribution假设；benchmark contamination与metric normalization影响HV；论文未单列完整limitations。
- **Trade-offs / New Failure Modes:** 无训练merge保持便宜但引入calibration-data governance、saliency staleness与omega tuning；保护base权重会削弱expert delta；一个merged artifact的局部退化可能被aggregate HV掩盖。
- **Where the Previous Design Still Applies:** 独立expert routing适合高保真/可回滚；简单task arithmetic适合相近任务；continual fine-tuning适合数据可得；ensemble适合容量和latency允许。
- **Evolution Relationship:** `Layering / Dependency`：weight-only delta merge→conflict/sparsity处理→activation-informed base protection→multi-objective artifact gate。
- **ROADMAP Node:** `PLATFORM-MODEL-REGISTRY`（Ch59）主 owner；handoff `TRAIN-LORA` Ch30、training checkpoint章节与`PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch30、Ch35、Ch58～60与Ch66的artifact lineage、merge state、evaluation/release gate。
- **Existing Coverage:** Books 已覆盖checkpoint lineage和artifact promotion；本 family 补充calibration-derived merge state及Pareto gate，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；80%/13% headline不脱离20 cases/六benchmarks复述。
- **Open Questions:** saliency如何跨calibration domains版本化；merge artifact如何记录source experts/omega；怎样将worst-case regression加入HV之外的release gate。

### Towards Physical Understanding in Video Generation

- **Candidate / Week / Score:** Physical Understanding in Video Generation / 2025-W06 / 23/30。
- **Source Family ID:** `pointvid-3d-point-regularized-video-generation`。
- **Source Type:** arXiv v1 video-generation research paper + dataset construction appendix。
- **First-public Date / Revision History:** v1 2025-02-05；v2 2025-10-23；W06锁定v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.03639v1；https://arxiv.org/abs/2502.03639。
- **Related Primary Sources:** I2VGen-XL、SVD、DynamiCrafter、Grounded-SAM-2、SpaTracker、ZoeDepth、VBench与VideoPhy原始资料定义backbone、pseudo-label和evaluation依赖。
- **Access and Verification Status:** Full Source Review Complete；PointVid pipeline、joint video-point diffusion、DDIM reconstruction/rigidity regularization、training contract、quantitative/qualitative evaluation、ablation与limitations已核验。
- **Full-read Coverage:** 已读2D-video局限、3D tracking data生成、coordinate representation/filtering/interpolation、architecture augmentation、three losses、70K/387 clips实验、component ablation、appendix与limitations。
- **Original Problem:** 只在2D pixel sequence上训练的视频模型可生成视觉运动，却容易在遮挡、接触和out-of-plane变化中发生手/物体morphing；appearance quality不等于物理一致性。
- **Why the Previous Design Was Reasonable:** 大规模RGB video易得，2D diffusion可复用成熟image backbone；显式3D标注昂贵，许多镜头只需视觉连贯而非可控动力学。
- **Changed Constraint:** task-oriented/contact-rich video需要shape、motion和depth关系跨帧保持，必须给模型某种可优化的3D state而不要求完整mesh/simulator。
- **Mechanism:** 用首帧foreground masks采样pixels，SpaTracker跟踪3D coordinates、ZoeDepth补depth，经KDTree插值与Kalman filter形成PointVid；扩展UNet联合diffuse RGB+point channels；从DDIM还原的point output计算reconstruction和rigidity losses，并与diffusion loss联合优化。
- **State Ownership:** RGB latent拥有appearance；tracked point tensor拥有partial geometry/motion；mask/query identity拥有跨帧对应；DDIM sampler拥有noise-free reconstruction；loss weights拥有semantic/geometry balance。
- **Control Flow / Data Flow:** raw video→Grounded-SAM-2 masks→foreground-biased queries→SpaTracker/ZoeDepth 3D trajectories→interpolation/filtering→video-point latent→joint diffusion→DDIM z0→point recon/rigid regularization→RGB+trajectory generation。
- **Implementation Details:** 约70K public+proprietary videos，448×256、16 frames；augmentation stage在8×A100、batch 4训练，regularization stage在1×A100、batch 4；gradient checkpointing仅保留DDIM最后一步gradient以控制memory。
- **Evaluation Contract:** 387 clips test batch；I2VGen-XL base，另与SVD、DynamiCrafter qualitative比较；VBench subject/background consistency、motion smoothness、aesthetic/imaging quality与VideoPhy physical commonsense；重点观察contact/shape conservation。
- **Baselines / Ablations / Sensitivity / Overhead:** same-data RGB-only finetune→joint point augmentation→full regularization三级ablation，隔离data与point contribution；未系统扫描point density、tracker error、loss weights和compute overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 8/1 A100、448×256×16、batch 4披露；precision、training steps、inference NFE/latency、concurrency与SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者backbone/data/test contract内，partial 3D trajectory作为联合modality并加point-space regularization，可改善所测temporal/shape/physical-plausibility指标和案例。
- **What It Does Not Prove:** 不证明模型学得general physics或causal world dynamics，不证明pseudo 3D coordinates准确，不证明benchmark分数等于真实安全/可执行行为，也不证明结果跨backbone/resolution/长视频成立。
- **Limitations / Threats to Validity:** 3D-awareness受point resolution和foreground coverage限制；tracker/depth/segmentation误差形成teacher bias；proprietary data、387 clips和UNet backbone限制复现/外推；定性案例选择风险。
- **Trade-offs / New Failure Modes:** 3D auxiliary state减少morphing但增加pseudo-label pipeline、存储和训练成本；稀疏/错误track会把几何artifact写入模型；geometry loss过强可能牺牲semantic/aesthetic quality。
- **Where the Previous Design Still Applies:** 纯RGB video diffusion适合规模与视觉质量优先；显式simulator/mesh适合强控制；optical flow适合2D motion；world model适合action-conditioned planning而非单纯生成。
- **Evolution Relationship:** `Direct Evolution`：2D video diffusion→pseudo 3D trajectory augmentation→joint latent state→explicit geometry regularization；与world model是`Explanatory Analogy`，不是等价关系。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-WORLD-MODELS` Ch25、`MULTIMODAL-EMBODIED-VLA` Ch26与`TRAIN-DATA` Ch27。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～27 的representation、generation、world-state/action和data boundary。
- **Existing Coverage:** Books 已强调video generation不等于world model；本 family 提供partial geometry regularization的中间演进节点，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度账本；“physical understanding”保持作者命名，正文只写physical-plausibility evidence。
- **Open Questions:** point confidence如何进入loss；长视频trajectory identity如何维护；action-conditioned数据能否把视觉plausibility推进到controllable transition。

### SliderSpace

- **Candidate / Week / Score:** SliderSpace / 2025-W06 / 20/30。
- **Source Family ID:** `sliderspace-diffusion-capability-decomposition`。
- **Source Type:** arXiv v1 paper + official project/repository/artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；W06 锁定 v1，未发现事件周内后续 revision。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01639v1；https://arxiv.org/abs/2502.01639；https://github.com/rohitgandikota/sliderspace；https://sliderspace.baulab.info/。
- **Related Primary Sources:** official repository 中的训练脚本、预训练 sliders 与数据用于核对可复现路径；Concept Sliders、weights2weights 与 NoiseCLR 只作为作者比较分支。
- **Access and Verification Status:** Full Source Review Complete；v1 Method、公式、实验、user study、appendix、ablation、limitations 与 artifact 均已核验。
- **Full-read Coverage:** 已读 Introduction/Related Work、latent diffusion/LoRA 背景、distribution sampling、semantic PCA、slider objective、三类应用、transfer、hyperparameter/encoder ablation、user study 与 limitations。
- **Original Problem:** 同一 prompt 下 diffusion model 的输出分布包含大量难以用语言预先指定的变化；现有控制通常要求用户先命名属性，无法系统暴露模型已经能够生成的 variation axes。
- **Why the Previous Design Was Reasonable:** prompt、reference image 或人工属性向量提供直接、可解释的控制目标，在目标明确时比无监督发现更省计算，也避免把 embedding 偏差误当作真实语义结构。
- **Changed Constraint:** 面向探索式创作、蒸馏模型 mode collapse 与未知 capability discovery 时，用户并不知道应先定义哪些控制维度；需要从输出分布自身恢复可组合方向。
- **Mechanism:** 对固定 prompt 以不同 seeds 采样约 5,000 个生成过程，用 final-image extrapolation 估计各 timestep 的最终图像；经 CLIP 等 semantic encoder 得到 embedding，PCA 提取正交主方向；再为每个方向训练 cross-attention LoRA，使 adapter 引起的 embedding difference 与对应 principal component 对齐。
- **State Ownership:** base diffusion model 拥有生成分布；sample/timestep 集合拥有 observation corpus；semantic encoder 定义可见的语义几何；PCA basis 拥有方向 identity；每个 LoRA 拥有可缩放、可组合的控制状态。
- **Control Flow / Data Flow:** prompt+seeds→diffusion trajectories→final-image extrapolation→semantic embeddings→PCA directions→逐方向 LoRA training→slider scale/composition→controlled generation。
- **Implementation Details:** 主实验使用 4-step SDXL-DMD；默认发现 32/64 个方向，随机稀疏激活 3 个 sliders；另在 SDXL、SDXL-Turbo 与 FLUX Schnell 上验证；64 directions 在单张 A100、低于 24GB VRAM、约 2 小时完成，repository 给出 A6000/A100 的实现说明。
- **Evaluation Contract:** concept decomposition 对每个 concept 生成 2,500 samples，以 DreamSim 测 diversity、CLIP 测 prompt alignment；art-style 分支以 4,388 位 artist proxy distribution 做 FID 与 1,000 对 grid user study；COCO-30K 分支检验 distilled-model diversity；person→police/athlete/dog 检验 transfer。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 base SDXL-DMD、LLM-expanded prompts、SDXL、Concept Sliders 和人工 artist prompts 比较；appendix 检查 timestep、semantic encoder、sample count 与训练选择；作者报告同数 sliders 比 Concept Sliders 快约 4 倍，但每次 discovery 仍约 2 小时。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 单 A100、<24GB VRAM、SDXL-DMD/SDXL/Turbo/FLUX 与 sample counts 已披露；precision、LoRA batch、在线交互 latency/concurrency 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者模型、encoder 和评测合同内，输出分布的 semantic PCA directions 可以训练成可组合 LoRA controls，并改善所测 diversity/utility 或逼近指定 style distribution。
- **What It Does Not Prove:** 不证明 PCA 方向是模型内部的因果 concept，不证明正交 embedding effect 等于人类语义独立性，不证明恢复了完整 capability space，也不证明对所有 prompt、文化概念和 diffusion architecture 稳定。
- **Limitations / Threats to Validity:** 方向由 semantic encoder 的训练偏差与分辨率决定；artist proxy/user study 有选择偏差；约 5,000 samples 和逐方向训练成本较高；distilled-model 结论不能外推到所有 mode collapse。
- **Trade-offs / New Failure Modes:** 从人工预设控制转向自动 discovery 提高覆盖与探索性，却把 ontology 权交给 encoder/PCA；方向会随 prompt、seed corpus、encoder 和 timestep 改变，版本化、命名、组合冲突与有害能力暴露成为新问题。
- **Where the Previous Design Still Applies:** 属性已知、低延迟或需强语义保证时，prompt/reference/manual slider 更直接；内部 causal analysis 应使用 activation/intervention 方法；无需交互控制时 base model 更简单。
- **Evolution Relationship:** `Direct Evolution`：predefined attribute control→sampled output manifold→semantic spectral decomposition→adapterized controls；对 internal interpretability 仅为 `Explanatory Analogy`。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `WORLDVIEW-REPRESENTATION` Ch5、`TRAIN-LORA` Ch30 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25 的 representation/generation/world-state boundary、Ch30 adaptation 与 Ch66 evidence contract。
- **Existing Coverage:** Books 已覆盖 generative controls 与 LoRA，但未显式拥有“以输出分布发现控制维度”的机制节点；本轮只建立 Weekly evidence，不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 评分由 19 调整为 20：Project Relevance 2→3，理由是它补足 capability decomposition、control identity 与 evaluation boundary，而非单一创作 UI。
- **Open Questions:** 方向 identity 如何跨 model/version/prompt 保持；能否以 causal intervention 验证 PCA direction；如何检测组合 slider 的非线性交互与安全风险。

### MakeAnything

- **Candidate / Week / Score:** MakeAnything / 2025-W06 / 20/30。
- **Source Family ID:** `makeanything-procedural-sequence-generation`。
- **Source Type:** arXiv v1 paper + official code repository。
- **First-public Date / Revision History:** arXiv v1 2025-02-03，v2 2025-02-05；W06 机制与实验锁定 v1，v2 只作 revision lineage。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01572v1；https://arxiv.org/abs/2502.01572；https://github.com/showlab/MakeAnything。
- **Related Primary Sources:** FLUX.1-dev、HydraLoRA、ProcessPainter 与 GRID 只作为 backbone/先行设计；不以二手 demo 代替论文实验。
- **Access and Verification Status:** Full Source Review Complete；v1 Method、公式、dataset、training、evaluation、ablation、appendix prompts、limitations 与 official artifact 已核验。
- **Full-read Coverage:** 已读 Introduction/Related Work、DiT background、two-stage architecture、serpentine layout、asymmetric LoRA、conditional flow matching、ReCraft、21-task dataset、evaluation、ablation 与 limitations。
- **Original Problem:** 过程教程是有顺序、有中间状态的视觉序列；逐帧 video 模型成本高且数据少，单图生成模型只保证最终画面，难以同时生成跨领域且阶段一致的 creation process。
- **Why the Previous Design Was Reasonable:** 独立生成单步图像或为每个领域训练专用 LoRA 能直接优化局部质量；video representation 保留时间轴；在数据充足或任务单一时，这些方案比统一 grid 更自然。
- **Changed Constraint:** 21 个领域的数据规模从 50 到 10,000 不等，需要共享跨域过程先验又避免小域过拟合，并支持从文本生成过程及从最终产物反推一种可行过程。
- **Mechanism:** 将 4/9 帧按 2×2/3×3 serpentine grid 排列，使时间相邻帧在 2D token grid 中也相邻；共享 LoRA 矩阵 A 表示跨任务知识，多个 task-specific B_i 与权重组合；Stage 1 学 text→process grid，合并 LoRA 后 Stage 2 把 clean final-frame image tokens 与 noisy sequence latents、text tokens拼接，经 multimodal attention 和 conditional flow matching 预测前 8 帧。
- **State Ownership:** grid cell/serpentine position 拥有 step identity；shared A 拥有跨域 subspace，B_i 拥有 domain adaptation；merged FLUX checkpoint 拥有 Stage-1 knowledge；ReCraft condition token 拥有 final-artifact constraint。
- **Control Flow / Data Flow:** tutorial frames→4/9-frame serpentine grid+GPT-4o captions→asymmetric-LoRA flow-matching training→merge into FLUX→final image VAE/token condition+noisy earlier frames→ReCraft LoRA→plausible procedural grid。
- **Implementation Details:** 21 tasks、超过24K sequences，前10类9帧、其余4帧；FLUX.1-dev、CAME optimizer、1024 resolution、LoRA rank 64、learning rate 1e-4、batch 2；Stage 1/Stage 2 分别 40K/15K steps。
- **Evaluation Contract:** 每个21-task生成20 sequences；以 GPT-4o、human rating 与 CLIP 评估 alignment/coherence/usability；与 ProcessPainter、Paints-Undo、Ideogram 比较，并对 base model、普通 LoRA 与 asymmetric LoRA 做三类 task ablation。
- **Baselines / Ablations / Sensitivity / Overhead:** ablation 支持 asymmetric shared/specialized factor 对若干 task 的作用，但不同 task 指标并非单调；未隔离 serpentine layout 与 dataset scale，未系统扫描 rank、grid order、frame count、condition strength 或 CAME contribution。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** FLUX.1-dev、1024²、rank 64、batch 2、40K/15K steps 已披露；GPU 数量/型号、precision、训练时长、inference steps/latency、concurrency 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在固定 4/9-step grid 与作者数据/评测下，2D spatial locality 可被复用来承载有限 procedural order；shared-A/task-B adaptation 和 final-image conditioning 能改善所测跨域 sequence quality。
- **What It Does Not Prove:** 不证明模型恢复了真实历史制作过程或因果工序，不证明 grid 等价于任意长时序/video，不证明对 unseen physical processes 正确，也不证明 GPT-4o/human coherence 等于可执行教程安全性。
- **Limitations / Threats to Validity:** 最大1024×1024、最多9步；网络数据与 GPT-4o annotations 可能含错误；per-domain size 极不均衡；20 samples/task 较小；baseline/backbone 与训练预算未完全对齐；hardware 未披露。
- **Trade-offs / New Failure Modes:** grid 把 sequence generation 降为成熟 image-generation problem，却固定了长度、分辨率和 reading order；asymmetric LoRA 提高共享但可能发生 negative transfer；final-artifact inversion 天生多解，容易生成“看似合理但从未发生”的步骤。
- **Where the Previous Design Still Applies:** 连续动作与实时控制适合 video/world model；高可信操作流程应使用 structured program、retrieval 与 verifier；单域数据充分时独立 LoRA 更简单；仅要终图时普通 T2I 不必承担 sequence state。
- **Evolution Relationship:** `Principle Reuse`：2D spatial attention→serpentine temporal layout；`Alternative Branch`：video temporal model vs grid process representation；ReCraft 是 output-conditioned reconstruction，不是 causal world model。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `MULTIMODAL-WORLD-MODELS` Ch25、`TRAIN-DATA` Ch27 与 `TRAIN-LORA` Ch30。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25、Ch27 与 Ch30 的 representation、generative factorization、world-state、data 和 adaptation boundary。
- **Existing Coverage:** Books 已区分 generation 与 action-conditioned transition，但缺少把有限过程映射为2D grid的受限分支；本轮只完成 Weekly evidence。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 评分由 19 调整为 20：Project Relevance 2→3，因为它提供 sequence-state representation 与 shared/specialized adapter 的通用 trade-off，不只是 tutorial 产品。
- **Open Questions:** 如何从 fixed grid 迁移到可变长度而不丢 step identity；怎样验证过程可执行性与因果顺序；shared A 的 domain interference 如何测量和回滚。

### TwinMarket

- **Candidate / Week / Score:** TwinMarket / 2025-W06 / 21/30。
- **Source Family ID:** `twinmarket-llm-multi-agent-market-simulation`。
- **Source Type:** arXiv v1 paper + official repository/artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-03；v2 2025-02-05、v3 2025-05-16、v4 2025-05-23、v5 2025-10-18；W06 锁定 v1，later revisions/repository 只用于 lineage，不把后续事件倒灌。
- **Direct Primary Sources:** https://arxiv.org/html/2502.01506v1；https://arxiv.org/abs/2502.01506；https://github.com/freedomintelligence/TwinMarket。
- **Related Primary Sources:** Xueqiu/Snowball、CSMAR 与 SSE50 数据定义、A-share auction rules及传统 ABM literature用于校验输入/环境假设；不把金融媒体结果当机制证据。
- **Access and Verification Status:** Full Source Review Complete；v1 framework、data initialization、BDI roles、dynamic social graph、market loop、100/1,000-agent experiments、appendices、prompts 与 repository 已核验。
- **Full-read Coverage:** 已读 Introduction/Related Work、micro/macro framework、workflow、results、scale-up、dataset/persona appendices、social propagation、trading system、validation metrics 与完整 prompt inventory。
- **Original Problem:** 传统 rule-based ABM 能复现 stylized facts，却难以表达 profile、private information、belief update、social influence 与交易环境之间的动态反馈；单个 LLM agent 又不能形成宏观涌现。
- **Why the Previous Design Was Reasonable:** 显式规则可校准、可解释、计算便宜且易做 counterfactual；固定 social graph 和 homogeneous information 简化因果分析，避免把 foundation-model bias 混入社会机制。
- **Changed Constraint:** 若研究 rumor cascade、opinion leader、自我实现预期和异质投资者，需要让 perception、belief、social graph、orders 与 market price 在同一闭环内共同演化，同时保留可观测 micro/macro state。
- **Mechanism:** 由 Snowball/交易数据采样 persona、bias、initial records 与 belief；每个用户以 BDI 拆分 belief、desire(query/search) 与 intention(social/trading)；recommendation 控制 perception field，interaction 形成 propagation chain 与动态相似性网络；buy/sell/hold orders 经 price/time priority、±10% limit 与最大成交量撮合，更新价格、持仓和次日 belief。
- **State Ownership:** persona/bias/portfolio/history 属于 user state；BDI roles 拥有 belief/goal/action；recommendation/social graph 拥有 visibility 与 propagation；order book/market engine 拥有 price、volume、position commit；news/rumor input 拥有 external information state。
- **Control Flow / Data Flow:** real user/market data→synthetic profile+belief initialization→daily information retrieval/perception→BDI planning→forum/trading intentions→post propagation+order matching→price/position/social-graph update→next-day belief→micro/macro validation。
- **Implementation Details:** v1 主实验为100个 GPT-4o users、10个由 SSE50 聚合的指数、2023-06-15～11-15 五个月；允许 buy/sell/hold，波动或参与度越界提前终止；另扩到1,000 agents；repository 提供 prompts、simulation modules 与 data preparation lineage。
- **Evaluation Contract:** micro 层观察 belief、bias 与 self-fulfilling loop；macro 层与 historical index 比较 fat tails、leverage effect、volume-return、volatility clustering；rumor intervention 比较 baseline；1,000-agent appendix 报告 RMSE/MAE/correlation/lag，但其数据归一化与预测 protocol 不充分。
- **Baselines / Ablations / Sensitivity / Overhead:** 与传统 ABM stylized facts 进行概念比较并做正常/rumor、100/1,000 agents 分支；缺少不同 LLM、无 social graph、无 BDI、不同 recommendation/order rules 的系统 ablation，也未报告 token/cost/latency scaling。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** GPT-4o、100/1,000 agents、10 indexes、五个月与 daily loop 已披露；API snapshot、prompt/token length、parallelism、hardware、成本、失败重试、wall-clock、concurrency 与 SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者初始化、prompts、推荐/交易规则与历史数据合同内，LLM agents 可形成可检查的 information→belief→action→market feedback loop，并复现若干 stylized statistics 与 rumor-response patterns。
- **What It Does Not Prove:** 不证明 agent cognition 等同真实投资者，不证明模拟有预测能力或真实因果识别，不证明 1,000-agent metric 不含 historical leakage/normalization artifact，也不证明换模型、市场或规则仍成立。
- **Limitations / Threats to Validity:** persona 与 bias 由采样和 GPT-4o scoring构造；fundamental metrics按 simulated/real price ratio调整，可能把真实轨迹泄漏进环境；同一模型同时驱动多个角色会造成 correlated policy；没有正式 limitations section、cost/hardware/seed variance 与强 ABM baselines。
- **Trade-offs / New Failure Modes:** 可表达行为与社会反馈，但显著增加 hidden state、nondeterminism、cost、cascade amplification 与 replay difficulty；推荐器、prompt、order rules 或真实数据锚定可能制造预期的“涌现”，单个 hallucination 可经 social graph 放大。
- **Where the Previous Design Still Applies:** 需要 causal clarity、可校准参数或大规模 Monte Carlo 时传统 ABM 更合适；预测与风控应使用真实市场模型；单 Agent 适合 isolated decision evaluation；静态 social graph适合控制变量实验。
- **Evolution Relationship:** `Layering / Dependency`：heterogeneous agent state→bounded information field→durable social propagation→environment commit→macro feedback；不是“更多 agents 必然更真实”的 `Direct Evolution`。
- **ROADMAP Node:** `AGENT-MULTI-AGENT`（Ch82）主 owner；handoff `AGENT-WORKFLOW` Ch81、`PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-OBSERVABILITY` Ch67 与 `PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch81～83 的 workflow/multi-agent/MCP boundary，并回看 Ch66～67、Ch72 的 evaluation、traceability 与 threat model。
- **Existing Coverage:** Books 已覆盖 coordination tax、shared state 与 error amplification；本 family 增加 environment feedback、information visibility 与 endogenous state commit 的受限案例，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 评分由 18 调整为 21：Project Relevance 2→4、Longevity 1→2；理由是其可复用价值在多 Agent state/visibility/environment feedback contract，而非金融预测结论。
- **Open Questions:** 如何区分真实 emergence 与 prompt/rule/data leakage；怎样记录每次 belief/action/market commit 的 lineage；模型异质性、failure injection 与 cost-normalized scale-up 会否改变结果。

### The Curse of Depth in Large Language Models

- **Candidate / Week / Score:** The Curse of Depth / 2025-W06 / 24/30。
- **Source Family ID:** `curse-of-depth-layernorm-scaling`。
- **Source Type:** arXiv v1 paper + author code。
- **First-public Date / Revision History:** arXiv v1 2025-02-09；v2 2025-07-01，后续 2026 revisions 不改变 W06 owner；本审计只把 v1 的 130M～1B training results 当事件时证据。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05795v1；https://arxiv.org/abs/2502.05795；https://github.com/lmsdss/LayerNorm-Scaling。
- **Related Primary Sources:** 论文引用的 Pre-LN、Post-LN、DeepNorm、Mix-LN 与 layer-pruning 原始工作仅作 baseline/evolution context。
- **Access and Verification Status:** `Full Review Complete`；v1 Method、proof assumptions、pretraining/SFT、appendices 与 code identity 已核验。
- **Full-read Coverage:** metadata、Introduction、layer-pruning setup、Pre/Post-LN analysis、LayerNorm Scaling、pretraining、SFT、variance/deep-layer analysis、proof appendices、loss curves 与 conclusion。
- **Original Problem:** Pre-LN 稳定了深层 Transformer 的训练，但某些现代 LLM 的后段层对 pruning/perturbation 异常不敏感，训练投入未必转化为有效表示变换。
- **Why the Previous Design Was Reasonable:** 把 LN 放在 residual branch 前可缓解 gradient instability，是大规模 decoder 训练的可靠默认；Post-LN 在更深网络中更容易出现优化不稳定。
- **Changed Constraint:** 模型加深后不仅要“能稳定训练”，还要确保每层 residual branch 相对主干保持足够信号，避免深层 Jacobian 接近 identity。
- **Mechanism:** 论文把 Pre-LN residual variance 随深度累积与 block derivative identity 化联系起来，并将第 `l` 层 LN 输出乘以 `1/sqrt(l)`，把理论 variance upper bound 从 exponential 收紧到 sub-quadratic polynomial。
- **State Ownership:** residual stream 拥有累积表示与 variance；每层 LN/scaling 决定 branch 注入幅度；optimizer/data 决定经验训练轨迹；pruning evaluator 只观测移除单层后的任务变化。
- **Control Flow / Data Flow:** residual state→LN→depth-dependent scale→attention/FFN→residual add；训练后逐层删除→SQuAD/MMLU performance drop→与 variance/Jacobian 分析交叉验证。
- **Implementation Details:** LLaMA-like 130M/250M/350M/1B，RMSNorm+SwiGLU；LayerNorm Scaling 无可学习参数或额外超参；Adam，至 350M 学习率 `1e-3`、1B 为 `5e-4`。
- **Evaluation Contract:** 130M/250M/350M/1B 分别训练 2.2B/3.9B/6.0B/8.9B tokens；比较 Post-LN、DeepNorm、Mix-LN、Pre-LN 与 scaled Pre-LN 的 perplexity，并在 Commonsense170K 后评测八项任务；另对 BERT-Large、Mistral/Llama2/DeepSeek/Qwen 做单层 pruning。
- **Baselines / Ablations / Sensitivity / Overhead:** normalization baselines、scaled initialization、variance curves 与 deep-layer pruning；未提供更大训练规模、跨 optimizer/data 的系统 sensitivity，也未测量端到端硬件 overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/tokens/optimizer/lr 已披露；accelerator、precision、sequence length、batch、parallelism、wall-clock、并发与 SLO 为 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 v1 小中型 LLaMA-like training contract 中，depth-dependent LN scaling 降低 variance、改善 loss 与多数 downstream tasks；layer pruning 也揭示所测 Pre-LN families 的后层敏感度较低。
- **What It Does Not Prove:** 不证明 Pre-LN 是所有深层低效的唯一因果源，不证明可直接外推到 7B+ pretraining；单层 pruning robustness 也不等同于该层没有协同作用。
- **Limitations / Threats to Validity:** 理论采用零均值、normal、independent 等简化假设；不同模型的 pruning benchmark 不完全相同；v1 training 最高 1B，hardware/seed 未披露；后续 revision 不能倒灌。
- **Trade-offs / New Failure Modes:** scaling 保留 Pre-LN stability 且几乎无参数成本，但固定 depth schedule 可能与不同 residual/normalization/optimizer 配方失配；更强 branch signal 也可能改变早期训练稳定性。
- **Where the Previous Design Still Applies:** 已有稳定、充分验证的 Pre-LN recipe；浅层或 residual scale 已校准的模型；无法承担新 normalization 风险的 continued training/serving artifact。
- **Evolution Relationship:** `Alternative Branch`：Post-LN 的深层表达贡献与 Pre-LN 的优化稳定性形成旧 trade-off；LayerNorm Scaling 尝试在 Pre-LN 内重新分配 depth-wise branch strength，而非宣告 Pre-LN 失效。
- **ROADMAP Node:** `MODEL-TRANSFORMER-LAYER`（Ch17）主 owner；handoff `TRAIN-PRETRAINING` Ch28 与 `WORLDVIEW-SCALING-LAW` Ch7。
- **Target and Adjacent Chapters Read:** 已核对 Ch16～18 的 FFN/Transformer/decoder-only boundary，并回看 Ch7、Ch28 的 scaling 与 training contract。
- **Existing Coverage:** Books 已覆盖 Pre-LN/Post-LN 与 residual stability；本 family 增加“稳定性不等于层利用率”的证据分支，本阶段不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06 spillback；不把作者的 root-cause wording 或 later 7B claim 写成通用事实。
- **Open Questions:** depth schedule 是否应随 residual statistics 自适应；在不同 parallelism、precision 与 optimizer 下能否保持收益；layer utility 应如何超越单层 pruning 度量。

### Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning

- **Candidate / Week / Score:** Social-Deduction MARL / 2025-W06 / 23/30。
- **Source Family ID:** `social-deduction-listen-speak-marl`。
- **Source Type:** arXiv v1 / AAMAS paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-09；AAMAS 2025 publication 属同一 Source Family，不改变 W06 first-public owner。
- **Direct Primary Sources:** https://arxiv.org/html/2502.06060v1；https://arxiv.org/abs/2502.06060。
- **Related Primary Sources:** RWKV 与 CleanRL/PPO 是模型和实现依赖；不替代本论文的 environment-grounded communication evidence。
- **Access and Verification Status:** `Full Review Complete`；正文、environment、losses、self-play failures、evaluation、hyperparameters/compute 与 broader impact 已核验。
- **Full-read Coverage:** metadata、related work、POMG formulation、Among Us environment、RL/listening/speaking/world-model losses、cooperative training、ablation/generalization、failure modes、appendices。
- **Original Problem:** 多 Agent 语言沟通的最终 team reward 稀疏；human demonstrations 昂贵；模型即使会生成自然语言，也未必会听取证据或发出能改变队友正确 belief 的消息。
- **Why the Previous Design Was Reasonable:** outcome RL 直接对齐胜负，behavior cloning 保持人类可读语言，固定 scripted communication 易于稳定训练；这些方案分别适合有 demos 或任务信号密集的环境。
- **Changed Constraint:** 在部分可观察、长轨迹、无 human demonstrations 的 social deduction 中，需要把 communication quality 与可验证环境状态连接，同时防止共同训练形成投机 convention。
- **Mechanism:** 将 listening 训练成从 action-observation history/discussion 预测 imposter；speaking reward 使用消息前后其他 crewmates 对真实 imposter belief 的变化；再与 RL、natural-language KL、behavior cloning 与 world-model loss联合，并冻结一名 crewmate 抑制共同退化。
- **State Ownership:** environment 拥有 hidden role、tasks、legal actions 与 terminal reward；各 agent 的 RWKV recurrent state 拥有私有 history/belief；speaker message更新共享 discussion；teammate prediction变化生成 communication reward。
- **Control Flow / Data Flow:** observation/action token stream→agent policy→gameplay或最多20-token message→其他 agents belief query→influence reward→PPO-style update；self-play迭代同时更换 imposter/部分 crewmates。
- **Implementation Details:** RWKV policy利用 constant per-token recurrent compute处理数万 token trajectories；主实验用1.5B模型；训练随机化 `1x3/2x2/2x3` layout、3/4/5 tasks，固定4 crewmates+1 imposter。
- **Evaluation Contract:** base environment为 `2x2` rooms、4 tasks/crewmate、5 players；3个独立 seed，比较 base RWKV、RL、listening、speaking及组合；评测 win rate、belief accuracy、message behavior和跨 layout/task/player generalization。
- **Baselines / Ablations / Sensitivity / Overhead:** 169M～7B base scaling，RL/L/S loss ablation、adaptive imposter、frozen crewmate与 environment variants；论文记录 silence convention、wait-at-start 与 action-token leakage 等 failure injection式观察。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 单张 A40 48GB；各 model 48小时内；RL collection batch 30 environments、优化并行6 trajectories；optimizer AdamWScheduleFree、lr `3e-4`；precision与production SLO未披露。
- **What the Evidence Actually Proves:** 在作者 Among Us sandbox 中，environment-grounded belief signal可让较小 LM 学到更有用的 listening/speaking，并相对 standard RL 提高团队 win rate。
- **What It Does Not Prove:** 不证明消息真实、不证明自然语言 convention 可迁移到开放环境或人机团队，也不证明更多/共同学习的 Agents 单调改善系统。
- **Limitations / Threats to Validity:** scene target由设计者手工指定；messages仍出现无证据断言；sandbox规则与角色数窄；共同训练会产生近乎完美但不可泛化的 collusion-like strategy。
- **Trade-offs / New Failure Modes:** dense communication reward改善 credit assignment，却可奖励操纵 belief 而非 truth；frozen partner恢复异质性但限制 joint adaptation；world-model loss保语言能力但增加目标耦合。
- **Where the Previous Design Still Applies:** 有高质量 human demonstrations 时 imitation更可控；简单 coordination可用结构化协议；高风险场景应优先 verifier、权限边界与可审计消息，而非纯 emergent communication。
- **Evolution Relationship:** `Direct Evolution`：terminal team reward→listening state prediction→speaker influence reward→heterogeneous self-play；每一步增加可学习信号，也新增 convention、deception 与 reward-hacking 风险。
- **ROADMAP Node:** `AGENT-MULTI-AGENT`（Ch82）主 owner；handoff `AGENT-WORKFLOW` Ch81、`PLATFORM-EVALUATION-SYSTEM` Ch66 与 `PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch81～83 的 workflow/multi-agent/MCP boundary，并回看 Ch66、Ch72 的 executable evidence 与 threat model。
- **Existing Coverage:** Books 已覆盖 coordination tax、shared state 与 error amplification；本 family 提供 communication reward 与 emergent convention 的具体机制证据，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；不把作者 doubled-win-rate headline 外推到开放域 Agent cooperation。
- **Open Questions:** influence reward如何约束 truthful evidence；怎样识别跨 Agent convention leakage；冻结角色、population diversity 与 adversarial partner应如何进入 deployment contract。

### LM2 / Large Memory Models

- **Candidate / Week / Score:** LM2 / 2025-W06 / 24/30。
- **Source Family ID:** `lm2-gated-auxiliary-memory`。
- **Source Type:** arXiv v1 paper + official repository。
- **First-public Date / Revision History:** arXiv v1 2025-02-09；后续 revision 不改变 W06 owner；本审计锁定 v1 architecture/evaluation。
- **Direct Primary Sources:** https://arxiv.org/html/2502.06049v1；https://arxiv.org/abs/2502.06049；https://github.com/convergence-ai/lm2。
- **Related Primary Sources:** BABILong、RMT 与 Llama-3/3.2 作为 benchmark/backbone/baseline来源。
- **Access and Verification Status:** `Full Review Complete`；architecture equations、pretraining corpus、benchmark tables、memory ablation、test-time analysis、appendix与repo identity已核验。
- **Full-read Coverage:** metadata、motivation、memory information flow、cross-attention/gates、pretraining、BABILong/general benchmarks、module-depth ablation、representation/test-time adaptation、related work与appendix。
- **Original Problem:** 标准 decoder把长期信息全部留在 token history/KV 中，跨长上下文的多步关系检索与更新成本高；外部 RAG又把检索和模型内部推理割裂。
- **Why the Previous Design Was Reasonable:** causal self-attention提供精确 token访问且易于端到端训练；RAG把可更新事实放到外部 index；segment recurrence以较低改动扩展上下文。
- **Changed Constraint:** 系统希望在保留 normal token path 的同时，让模型拥有可写、可忘、随 inference更新的补充状态，而非每次只从静态上下文重算。
- **Mechanism:** 每层加入 `N x d x d` memory bank；input embeddings与memory做cross-attention定位/读取，再用input gate写入 `tanh(E_mem)`、forget gate保留旧memory，形成 `M_{t+1}=g_in*tanh(E_mem)+g_forget*M_t`。
- **State Ownership:** token residual/KV仍属于decoder request；auxiliary memory由各decoder block持有并在forward/token steps更新；gates拥有写入/遗忘控制；论文未给出跨session persistence与rollback owner。
- **Control Flow / Data Flow:** tokens+position→decoder representation→memory cross-attention read→main token path融合→input/forget gates更新memory→下一层/下一token继续；test-time heatmap用于观测slot attention shift。
- **Implementation Details:** Llama-like 16 blocks、d=2048、FFN=8192、32 attention heads/8 KV heads；每层2048个memory slots；1.2B backbone+0.5B memory=1.7B。
- **Evaluation Contract:** pretraining corpus含28B synthetic textbook/story与220B FineWeb-Edu（排除Python）；BABILong 10 tasks、0K～128K；比较 Llama-3.2-1.2B、parameter-matched vanilla Llama-1.7B、RMT-1.7B与RAG baseline，并补一般 benchmarks。
- **Baselines / Ablations / Sensitivity / Overhead:** memory插入1/6/12/16 blocks 的 perplexity ablation；memory representation、test-time updates；缺少 slot count/forget dynamics、污染与跨session reset 的系统 sensitivity；额外0.5B参数是显著 overhead。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model、corpus与1K～128K lengths披露；accelerator、precision、batch、parallelism、latency、memory bandwidth、concurrency与SLO均 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者 1.7B 与 BABILong contract 中，贯穿多层的可写 memory modules优于所列匹配 baselines，并且 memory attention在test-time forward中会随目标问题改变。
- **What It Does Not Prove:** heatmap变化不证明slot语义或因果记忆；不证明超长真实文档、多人session、在线污染下可靠，也不证明其成本优于扩大KV/RAG。
- **Limitations / Threats to Validity:** synthetic benchmark占主导、hardware/runtime成本未报告、backbone/data并非所有baseline完全匹配；memory capacity很大，cross-attention复杂度与更新稳定性边界不足。
- **Trade-offs / New Failure Modes:** 得到可更新内部state，却增加参数、带宽、write/forget drift、污染、reset/rollback与并发隔离问题；把memory放入更多层改善作者指标但训练收敛更慢/成本更高。
- **Where the Previous Design Still Applies:** 短上下文、静态事实、强 provenance需求适合普通 attention/RAG；严格跨租户隔离时外部显式memory比隐式可写state更易审计。
- **Evolution Relationship:** `Alternative Branch`：full attention/RAG/segment recurrence→gated in-model memory；它改变状态位置与更新方式，不是对 KV cache 或 external retrieval 的直接替代。
- **ROADMAP Node:** `MODEL-LONG-CONTEXT`（Ch22）主 owner；handoff `AGENT-MEMORY` Ch77、`INFER-KV-CACHE` Ch45 与 `PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch21～23 的 MoE/long-context/multimodal boundary，并回看 Ch45、Ch72、Ch77 的 runtime state、security与derived memory。
- **Existing Coverage:** Books 已区分 context、KV、RAG与Agent memory；本 family增加 architecture-level writable memory分支，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；不保留脱离额外参数、训练数据和synthetic benchmark的平均提升 headline。
- **Open Questions:** memory slot如何获得稳定identity/provenance；跨request是否重置；并发batch中的write isolation、checkpoint与rollback如何实现。

### Hierarchical Drafting based on Temporal Locality

- **Candidate / Week / Score:** Hierarchical Drafting / 2025-W06 / 25/30。
- **Source Family ID:** `hierarchical-drafting-temporal-locality`。
- **Source Type:** arXiv v1 paper + benchmark artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-08；后续 revision 不改变 W06 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05609v1；https://arxiv.org/abs/2502.05609。
- **Related Primary Sources:** https://github.com/hemingkx/Spec-Bench；Spec-Bench用于实验脚本/数据合同，不替代HD方法论文。
- **Access and Verification Status:** `Full Review Complete`；algorithm、database construction/order、verification、实验/ablation、appendix与benchmark artifact已核验。
- **Full-read Coverage:** metadata、speculative decoding背景、database drafting、three-level hierarchy、algorithm、datasets/models/baselines、main results、latency/acceptance/access-order analyses与appendices。
- **Original Problem:** trainable draft model有训练/维护成本，单一database drafting虽免训练却受token source覆盖和lookup latency影响，跨任务速度不稳定。
- **Why the Previous Design Was Reasonable:** draft model可学习target分布并提高acceptance；single source retrieval简单且在重复上下文/RAG等强locality任务有效；autoregressive decode没有draft overhead。
- **Changed Constraint:** serving工作负载同时包含 request-local repetition、target-model惯用输出与通用语料统计，需要按收益/延迟逐层扩大候选源，而不是总查最大库。
- **Mechanism:** 建立 context-dependent `D_c`、model-dependent `D_m`、statistics-dependent `D_s`；按 temporal locality从高到低检索，候选不足才访问下一层；target model并行verify draft set并用新输出更新 `D_c`。
- **State Ownership:** request/ongoing generation拥有 `D_c`；target-family response corpus拥有 `D_m`；shared corpus拥有 `D_s`；target verifier拥有最终token commit，database只提出候选。
- **Control Flow / Data Flow:** recent suffix→query `D_c`→不足则 `D_m`→再不足 `D_s`→构造draft set/mask→target parallel verification→接受前缀并生成fallback token→更新 `D_c`→下一轮。
- **Implementation Details:** suffix retrieval与三库hierarchical access；多候选使用special attention mask并行验证；model/statistics sources实验包括ShareGPT/UltraChat/TheStack等，数据库规模最高约12GB。
- **Evaluation Contract:** Spec-Bench六类任务（conversation、translation、summarization、QA、math、RAG）；Vicuna-v1.3 7/13/33B与Llama-2-chat 7/13B；`T=0`及`T=1`，测draft latency、acceptance/accepted length与wall-clock speedup。
- **Baselines / Ablations / Sensitivity / Overhead:** autoregressive、PLD/REST/LADE等database drafting以及SpS/MEDUSA；single/two/three database ablation、access order、token source/quality、output length与temperature；单次运行，作者称run差异小。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 7B/13B用单 A100-40GB PCIe、33B用单 A100-80GB PCIe，FP16；batch/concurrency/P95 SLO未披露；headline `>1.5x`仅限作者 `T=0` Spec-Bench合同。
- **What the Evidence Actually Proves:** 在所测单GPU模型/任务中，按locality分层访问可比单库更稳地平衡acceptance与draft latency，并保持target-model lossless verification。
- **What It Does Not Prove:** 不证明高并发、continuous batching、prefix sharing或不同storage topology下仍加速；也不证明比训练式draft在所有模型/任务更优。
- **Limitations / Threats to Validity:** single-run、旧模型family、单GPU/FP16、离线database freshness与构建成本未计入；最大库可能提高acceptance却慢于autoregressive。
- **Trade-offs / New Failure Modes:** 免draft训练但引入多库identity、freshness、memory footprint、lookup contention与tenant leakage；层级顺序不匹配workload会把低延迟收益耗尽。
- **Where the Previous Design Still Applies:** 高acceptance且稳定的trainable draft适合固定target；短输出/低复用适合AR；单一局部库适合明确高locality且容量受限的场景。
- **Evolution Relationship:** `Principle Reuse`：CPU/cache memory hierarchy的locality排序迁移到draft sources；在speculative decoding中属于proposal层演进，verify/commit contract保持不变。
- **ROADMAP Node:** `INFER-SPECULATIVE-DECODING`（Ch48）主 owner；handoff `INFER-GPU-MEMORY` Ch54、`INFER-SCHEDULING` Ch56 与 `PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch47～49 的 paged state/speculation/execution boundary，并回看 Ch54、Ch56、Ch72 的memory、scheduling与tenant isolation。
- **Existing Coverage:** Books 已覆盖draft/verify/commit与artifact compatibility；本 family增加 retrieval source hierarchy 和 drafting-latency trade-off，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；不把 `>1.5x` 脱离单GPU、model、temperature与task合同保留为通用结论。
- **Open Questions:** multi-tenant database如何隔离；continuous batching中lookup和verification shape如何协调；database freshness/eviction/poisoning由谁负责。

### Gemstones / A Model Suite for Multi-Faceted Scaling Laws

- **Candidate / Week / Score:** Gemstones / 2025-W06 / 25/30。
- **Source Family ID:** `gemstones-multifaceted-scaling-laws`。
- **Source Type:** arXiv v1 paper + open checkpoint/metric/code artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-07；后续 v2/v3 不改变 W06 owner；本审计锁定 v1 fits、training caveats与artifact规模。
- **Direct Primary Sources:** https://arxiv.org/html/2502.06857v1；https://arxiv.org/abs/2502.06857；https://github.com/mcleish7/gemstone-scaling-laws。
- **Related Primary Sources:** Dolma、Chinchilla/Kaplan等仅作data与fit baseline；工业模型参数用于comparison而非机制证明。
- **Access and Verification Status:** `Full Review Complete`；architecture/data/training、three fit approaches、GPU-hours analysis、ablation、failure appendix与FLOP accounting已核验。
- **Full-read Coverage:** metadata、related work、model suite design、learning-rate transfer、fit procedures、width/depth/tokens laws、resampling sensitivity、GPU-time/overtraining分析、appendices与code identity。
- **Original Problem:** 传统 scaling law把 architecture/hyperparameters压缩成parameter count，容易把特定model family、checkpoint selection与parallel runtime的经验当作普适处方。
- **Why the Previous Design Was Reasonable:** FLOPs和parameter/token law给昂贵训练提供低维预算工具；冻结width/depth/lr可控制变量并降低pilot成本。
- **Changed Constraint:** 真实系统同时优化loss、wall-clock、training/inference cost与hardware utilization；width/depth、cooldown、learning rate、fit subset和parallelism都会改变处方。
- **Mechanism:** 释放跨parameter/width/depth/token/lr/cooldown的checkpoint grid，分别用binning/convex-hull/parametric fits重估law；再用实测optimizer step time把FLOPs prescription映射到GPU-hours与overtraining选择。
- **State Ownership:** checkpoint/metric ledger拥有每个训练点；fit pipeline拥有样本选择、FLOP定义与loss surface；runtime/parallelism拥有wall-clock；最终architecture decision由workload/cost目标决定。
- **Control Flow / Data Flow:** architecture+training config→Dolma training/checkpoints→held-out 100M-token log perplexity→多种selection/fit→FLOPs/GPU-hours frontier→sensitivity/overtraining decision。
- **Implementation Details:** up to 2B parameters；>4000 checkpoints、累计>10T tokens；主run每模型350B Dolma tokens、context 2048、world batch 2048 sequences；每2B tokens保存checkpoint；AdamW，AMD MI250X多节点 tensor+data sharding，无pipeline parallelism。
- **Evaluation Contract:** fixed in-distribution 100M-token validation；比较多种fit方法、token cutoffs、embedding counting、lr/cooldown subset、integer constraints和law forms；报告FLOPs及实测step-time推导的GPU hours。
- **Baselines / Ablations / Sensitivity / Overhead:** learning-rate halving、cooldown、删除<120B token点、Huber delta与law form；极端wide models出现loss spike，作者rollback/微调lr，部分patched runs在350B后仍diverge。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** AMD MI250X多节点、TP+data sharding；model≤2B、seq 2048、world batch 2048、350B tokens；GPU数量、precision、topology、通信、并发与SLO未完整披露。
- **What the Evidence Actually Proves:** scaling prescription对architecture、checkpoint selection、fit形式与runtime metric敏感；在作者无PP的MI250X实现中，过窄模型的GPU-hours代价远高于FLOPs差异，适度overtrain小模型的预测loss penalty较小。
- **What It Does Not Prove:** 不证明wide/shallow在其他parallelism/hardware一定time-optimal，不证明2B以下fit能精确处方frontier-scale模型，也不证明validation loss等于downstream/product utility。
- **Limitations / Threats to Validity:** 单data family、≤2B、固定context与training recipe；极端shape instability和manual rollback；GPU-hours受实现影响；fit结果对筛选敏感。
- **Trade-offs / New Failure Modes:** 多维pilot提高处方可信度但显著增加实验/ledger成本；用wall-clock替代FLOPs更贴近工程，却把compiler/kernel/topology的暂时特性写入law。
- **Where the Previous Design Still Applies:** 早期粗预算、固定architecture family与稳定hardware上，经典parameter/token law仍是低成本起点；FLOPs仍适合跨runtime比较algorithmic work。
- **Evolution Relationship:** `Direct Evolution`：single-axis compute-optimal law→architecture-aware fit→runtime-aware frontier→uncertainty-aware decision；不是用新law覆盖旧law，而是逐步显式化其隐藏条件。
- **ROADMAP Node:** `WORLDVIEW-SCALING-LAW`（Ch7）主 owner；handoff `TRAIN-PRETRAINING` Ch28 与 `TRAIN-DISTRIBUTED-TRAINING` Ch36。
- **Target and Adjacent Chapters Read:** 已核对 Ch6～8 的 capacity/scaling/emergence边界，并回看 Ch28、Ch36～41 的training与parallel runtime。
- **Existing Coverage:** Books 已强调scaling law是经验合同；本 family补强“fit pipeline与runtime也属于law”的大规模artifact证据，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；50% FLOPs/200% GPU-hours overspend只保留在作者TP-only contract内。
- **Open Questions:** 如何为fit不确定性建立release gate；不同PP/FSDP/compiler/hardware下aspect ratio frontier如何迁移；downstream能力和inference cost如何共同进入law。

### Teaching Language Models to Critique via Reinforcement Learning / CTRL

- **Candidate / Week / Score:** CTRL / 2025-W06 / 24/30。
- **Source Family ID:** `ctrl-execution-grounded-critique-rl`。
- **Source Type:** arXiv v1 paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-05；v2 2025-11-29；W06只使用v1 pipeline与实验。
- **Direct Primary Sources:** https://arxiv.org/html/2502.03492v1；https://arxiv.org/abs/2502.03492。
- **Related Primary Sources:** TACO、CodeContests、LiveCodeBench、MBPP+与JudgeBench提供training/evaluation contract；GRPO是优化依赖。
- **Access and Verification Status:** `Full Review Complete`；reward derivation、SFT/RL pipeline、data curation、benchmarks、compounding/error/efficiency analysis与appendices已核验。
- **Full-read Coverage:** metadata、motivation、critic objective、execution-guided synthesis、GRPO、experiments、generator transfer、difficulty/test-time scaling、JudgeBench、implementation prompts/hyperparameters与credit-assignment appendix。
- **Original Problem:** self-critique没有外部grounding时常无法纠错；human critique labels难规模化；scalar reward能判别却不能给generator可执行的修复方向。
- **Why the Previous Design Was Reasonable:** unit-test execution feedback精确但缺解释；SFT human critique可读但昂贵；discriminative RM适合ranking；固定single-pass generation成本低且避免迭代退化。
- **Changed Constraint:** 希望critic从可执行结果学习“什么反馈会让固定generator改对”，并在test time迭代，同时控制正确答案被改坏和运行超时。
- **Mechanism:** sandbox将initial solution测试结果映射成hints以合成SFT critiques；RL阶段固定generator，将critic生成的feedback交给generator revision，以修订后执行reward训练critic，使用group-relative advantage和KL约束。
- **State Ownership:** sandbox/tests拥有可执行真值；critic拥有feedback policy；generator拥有proposal/revision policy且训练时固定；workflow拥有每轮solution/critique/reward lineage。
- **Control Flow / Data Flow:** problem→initial solution→sandbox tests→hinted critique synthesis/SFT→critic sampled critiques→fixed generator revisions→sandbox reward→GRPO update；inference可重复critique-revision多轮。
- **Implementation Details:** Qwen2.5-Coder-32B-Instruct critic/generator；TACO 26,443清洗至18,820训练问题；SFT batch256、max2048、bf16、1 epoch；RL batch1024、mini-batch256、group8、KL .001、prompt1536/response768、2 epochs。
- **Evaluation Contract:** CodeContests、LiveCodeBench 2024.08～11、MBPP+与JudgeBench；Qwen2.5-Coder及GPT-4o generator；5 seeds；Pass@1、wrong→right `Delta_up`、right→wrong `Delta_down`、F1、timeout与code similarity。
- **Baselines / Ablations / Sensitivity / Overhead:** zero-shot、execution feedback、self-critique、CTRL-SFT、GPT-4o critic、多轮1～5与7/14/32B inference scaling；正文显示更多轮可提高难题但普通critic也会compound errors。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/batch/length/bf16/decoding已披露；GPU、节点、wall-clock、sandbox capacity、concurrency与production SLO为 `Not Disclosed`；inference initial/critique temperature .7，revision greedy，max1024 tokens。
- **What the Evidence Actually Proves:** 在作者coding/test合同中，以“反馈后generator能否通过tests”为reward可训练更actionable critic，并在若干generator/benchmark上改善迭代修订。
- **What It Does Not Prove:** 不证明critique事实正确或可迁移到无executable verifier领域；不证明weak-to-strong是普遍scalable oversight；也不保证更多轮单调改善。
- **Limitations / Threats to Validity:** reward依赖测试覆盖与固定generator可修复性；training/eval均以code为主；hardware/cost缺失；critic可能学习generator-specific漏洞；timeout由10.54%升至16.61%。
- **Trade-offs / New Failure Modes:** 获得自然语言credit assignment与test-time scaling，但新增sandbox成本、test leakage、reward hacking、正确解回退、长/慢修订与多轮state explosion。
- **Where the Previous Design Still Applies:** verifier完备时直接execution-guided search更简单；高质量human critique适合安全/规范问题；低延迟场景优先single-pass或bounded retry。
- **Evolution Relationship:** `Direct Evolution`：scalar execution result→hinted critique SFT→downstream-outcome RL→iterative critique/revision；反馈从解释结果演进为影响下一步action的policy。
- **ROADMAP Node:** `AGENT-REFLECTION`（Ch80）主 owner；handoff `TRAIN-RLHF` Ch31、`PLATFORM-EVALUATION-SYSTEM` Ch66 与 `AGENT-WORKFLOW` Ch81。
- **Target and Adjacent Chapters Read:** 已核对 Ch79～81 的planning/reflection/workflow boundary，并回看 Ch31、Ch66 的reward与executable evaluator contract。
- **Existing Coverage:** Books 已覆盖reflection需要外部证据和bounded loop；本 family提供downstream-correction reward的具体训练机制，本阶段不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；106.1% relative headline不脱离低base rate、CodeContests、model与iteration合同外推。
- **Open Questions:** critic/generator版本如何共同登记；test coverage和sandbox nondeterminism如何进入reward lineage；何时应停止迭代以避免timeout/regression。

### NoLiMa / Long-Context Evaluation Beyond Literal Matching

- **Candidate / Week / Score:** NoLiMa / 2025-W06 / 24/30。
- **Source Family ID:** `nolima-latent-association-long-context-eval`。
- **Source Type:** arXiv v1 benchmark paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-07；v2/v3 后续扩展不改变 W06 owner；W06使用 v1 的12-model contract。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05167v1；https://arxiv.org/abs/2502.05167。
- **Related Primary Sources:** NIAH、RULER、HELMET、BABILong 与所测model cards只用于benchmark/model contract交叉核验。
- **Access and Verification Status:** `Full Review Complete`；needle/haystack construction、filtering、models、metric、placement/hop/inversion/distractor/CoT analyses与appendices已核验。
- **Full-read Coverage:** metadata、benchmark motivation、related benchmarks、needle templates、semantic/conflict filtering、haystack construction、12-model evaluation、effective-length metric、ablations、prompts与full needle set。
- **Original Problem:** 常见 NIAH 在query和needle间有literal overlap，模型可依赖词面匹配，导致advertised context length与需要关联推理的有效长度混淆。
- **Why the Previous Design Was Reasonable:** literal needle可隔离位置检索与“lost in middle”，易合成、易评分；真实RAG也常有关键词重合，因此是有价值的基础层测试。
- **Changed Constraint:** 要评估长上下文中的semantic association与distractor resistance，必须让短上下文任务本身可解，同时去掉query-relevant passage的字面捷径和冲突事实。
- **Mechanism:** 设计1/2-hop和default/inverted needle templates；Contriever召回相似词并人工过滤surface distractors，再用分块LLM检查冲突；将needle插入多本书拼接haystack，并以base score 85%定义effective length。
- **State Ownership:** benchmark generator拥有needle/question/answer identity；haystack filter拥有distractor/conflict policy；model API/version拥有推理行为；evaluator拥有normalized score与effective-length threshold。
- **Control Flow / Data Flow:** question-keyword/latent-associated needle→filter haystack→5 random haystacks×58 pairs×26 positions→model prompt→short answer或bounded CoT→exact/normalized scoring→length curve。
- **Implementation Details:** 每个context length 7,540 tests；每次snippet<250 tokens，haystack>60K tokens；needle 26个等间隔位置；CoT≤3句或192 generated tokens；instruction-tuned chat templates。
- **Evaluation Contract:** v1评测5个closed-source与7个open-weight models，claimed context≥128K；对1K～32K主表，并分析placement、1/2-hop、inversion、CoT和added lexical distractors；effective threshold=`0.85 x base score`。
- **Baselines / Ablations / Sensitivity / Overhead:** 与普通NIAH/RULER/HELMET/BABILong的lexical-overlap统计对照；needle placement、last-2K control、hop/inversion、CoT与distractor ablation；未报告API cost/latency或多次sampling variance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** closed API deployment hardware/precision不可见；open-weight serving hardware、batch/concurrency也未披露；model revisions、chat templates、context 1K～32K、generation cap与sampling规则是主要可复现合同。
- **What the Evidence Actually Proves:** 在作者v1合成benchmark中，去掉literal overlap并增加latent association后，12个模型的normalized performance随长度明显下降，claimed window不能替代任务条件下的effective length。
- **What It Does Not Prove:** 不证明attention mechanism是唯一瓶颈，不证明表中effective length适用于所有任务，也不证明真实RAG系统同样下降；threshold 85%是benchmark选择。
- **Limitations / Threats to Validity:** template/synthetic needles、books distribution、filter model bias、manual inspection、closed API版本漂移与单一短答案评分；主表只到32K，作者结论不能外推到所有claimed window。
- **Trade-offs / New Failure Modes:** 去除词面捷径增强semantic stress，但也把retrieval、association、reasoning与instruction following混在同一分数；严格filter可能使数据偏离真实噪声分布。
- **Where the Previous Design Still Applies:** literal NIAH适合定位/position baseline；真实产品需另测domain docs、retriever与answer verifier；BABILong等多步事实任务覆盖不同能力轴。
- **Evolution Relationship:** `Layering / Dependency`：literal position retrieval→latent association→conflicting distractors→bounded reasoning；每层增加一个约束，不能用后一层否定前一层测试价值。
- **ROADMAP Node:** `PLATFORM-EVALUATION-SYSTEM`（Ch66）主 owner；handoff `MODEL-LONG-CONTEXT` Ch22、`INFER-PREFILL` Ch43 与 `INFER-KV-CACHE` Ch45。
- **Target and Adjacent Chapters Read:** 已核对 Ch65～67 的registry/evaluation/observability boundary，并回看 Ch22、Ch43、Ch45 的model/runtime context contract。
- **Existing Coverage:** Books 已区分claimed/effective context和workload contract；本 family补充“lexical shortcut是隐藏变量”的benchmark机制，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；不把GPT-4o 8K等表格结果写成模型通用context上限。
- **Open Questions:** 如何拆分retrieval/association/reasoning error；closed model revision如何冻结；真实RAG corpus的lexical-gap和conflict分布如何构造可复现测试。

### CODESIM / Simulation-Driven Multi-Agent Code Generation

- **Candidate / Week / Score:** CODESIM / 2025-W06 / 23/30。
- **Source Family ID:** `codesim-simulation-driven-code-workflow`。
- **Source Type:** arXiv v1 paper + official NAACL Findings paper + author code/results artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-08；NAACL 2025 Findings 是同一 family 的后续正式版本，不作为新的 W06 事件。
- **Direct Primary Sources:** https://arxiv.org/pdf/2502.05664v1；https://arxiv.org/abs/2502.05664。
- **Related Primary Sources:** https://aclanthology.org/2025.findings-naacl.285/；https://github.com/kagnlp/CodeGenerator；https://huggingface.co/ashraful/CodeSIM/tree/main/results。
- **Access and Verification Status:** `Full Review Complete`；事件时 v1 全文、后续正式论文、算法、prompt、公开代码合同、结果日志与limitations已联合核验。
- **Full-read Coverage:** metadata、motivation、planning/coding/debugging agents、simulation prompts、adaptive traversal、7 benchmarks、baselines、language/generalization tests、p/d与sample-I/O ablations、API/token analysis、error analysis、limitations和appendix prompts。
- **Original Problem:** 外部编译器驱动的 iterative debugger 只能修复已有代码，若初始计划或算法理解错误，后续局部 patch 很难恢复。
- **Why the Previous Design Was Reasonable:** direct generation 与 compiler feedback 状态少、控制流短、可执行测试提供强 oracle；当题目简单或首稿质量高时，额外 agent 循环只增加成本。
- **Changed Constraint:** 在竞争编程和复杂 program synthesis 中，错误常先发生在 problem understanding 与 plan，而不只是 syntax/runtime；需要在生成代码前验证算法状态转换。
- **Mechanism:** Planning Agent 生成计划并用 sample input/output 逐步模拟；Coding Agent 将计划转成代码并执行公开样例；失败后 Debugging Agent 读取 plan、code 与 log 修复，超过 d 次后回到规划，最多执行 p 个周期。
- **State Ownership:** workflow controller拥有 p/d budget 与阶段状态；planning agent拥有候选计划；sandbox/test harness拥有可执行 observation；debugger拥有补丁提案；hidden evaluator拥有最终 correctness commit。
- **Control Flow / Data Flow:** problem→plan→simulated trace/feedback→refined plan→code→sample execution/log→debug loop或re-plan→hidden tests；LLM output只产生 proposal，测试结果决定分支但不证明 hidden correctness。
- **Implementation Details:** 官方实现暴露 model、dataset、strategy 参数并依赖 ExecEval/Docker 执行；事件时算法给 basic tasks 设置 p=5、d=5，competitive tasks通常 p=3、d=3，CodeContest/GPT-4 为 p=3、d=5。
- **Evaluation Contract:** HumanEval、HumanEval-ET、EvalPlus、MBPP、MBPP-ET、APPS、CodeContest；metric为 pass@1；backbones包括 ChatGPT、GPT-4、GPT-4o-2024-08-06、Llama、Gemma、Mixtral；结果只属于这些 prompt、sample-I/O与执行合同。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 Direct、CoT、Self-Planning、Analogical、Reflexion、LATS、MapCoder；测试 simulation、p/d、sample-I/O、synthetic I/O、外部 debugger 与 token/API 成本；synthetic I/O 反而降低 9.3%，说明额外 verifier data 可能污染控制流。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API模型版本部分披露，open models为 Gemma2-9B、Mixtral-8x7B、Llama-3.1-8B/70B；硬件、精度、batch、并发与SLO `Not Disclosed`；作者报告每题平均约13.64K tokens，对照 direct约560 tokens。
- **What the Evidence Actually Proves:** 在作者七个 benchmark、prompt、budget 与 sample-I/O合同内，把 plan simulation 放在 code generation 前、并保留 re-plan 分支，可提高 pass@1；可执行 feedback 是 workflow state，而非一句“多 Agent 更强”。
- **What It Does Not Prove:** 不证明 agent 数量本身导致收益，不证明公开样例通过等于 hidden correctness，不证明对真实大型代码库、长期维护、性能或安全成立。
- **Limitations / Threats to Validity:** token/API成本远高于 direct；公开样例少且可能不覆盖错误；论文只测 functional correctness，未测运行时/内存优化；生成代码必须 sandbox；API模型可漂移。
- **Trade-offs / New Failure Modes:** 以更多 planning/debug calls换取更早纠错；新增错误模拟、自洽但错误的 plan、test overfitting、sandbox escape、循环不收敛、预算耗尽和不可复现 API 行为。
- **Where the Previous Design Still Applies:** 短小、约束明确、有强编译/测试反馈且首稿成功率高的任务，单 Agent direct→test→repair 更便宜、更容易审计。
- **Evolution Relationship:** `Direct Evolution`：direct code→external-debug loop→plan-first workflow→simulation-verified plan→bounded re-plan/debug；新阶段把 failure detection 前移，但没有取代 executable tests。
- **ROADMAP Node:** `AGENT-WORKFLOW`（Ch81）主 owner；handoff `AGENT-PLANNING` Ch79、`AGENT-REFLECTION` Ch80、`PLATFORM-EVALUATION-SYSTEM` Ch66 与 `PLATFORM-SECURITY` Ch72。
- **Target and Adjacent Chapters Read:** 已核对 Ch78～82 的tool/planning/reflection/workflow/multi-agent边界，并回看 Ch66、Ch72 的verifier与sandbox contract。
- **Existing Coverage:** Books已有 durable workflow、proposal/commit 与 executable artifact原则；本 family补充“plan simulation先于code commit”的演进证据，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；headline pass@1不脱离模型版本、prompt、p/d、sample-I/O和hidden test合同外推。
- **Open Questions:** plan simulation如何用独立oracle而非同源LLM校验；test/sandbox版本怎样进入trace；p/d budget如何按边际收益停止；side effect任务怎样支持rollback。

### APE / Adaptive Parallel Encoding

- **Candidate / Week / Score:** APE / 2025-W06 / 27/30。
- **Source Family ID:** `ape-adaptive-parallel-context-encoding`。
- **Source Type:** arXiv paper + official implementation/project artifact。
- **First-public Date / Revision History:** arXiv v1 2025-02-08；后续 v2 在 2025-02-12，不改变 W06 owner。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05431；https://arxiv.org/abs/2502.05431；https://github.com/Infini-AI-Lab/APE。
- **Related Primary Sources:** https://infini-ai-lab.github.io/APE-Page/；vLLM、MInference、PCW 与 CEPE 仅作实现和baseline关系核验。
- **Access and Verification Status:** `Full Review Complete`；背景、attention几何、公式、实现、RAG/ICL/LOFT/CRAG实验、component ablation、efficiency、appendices与limitations已核验。
- **Full-read Coverage:** metadata、CAG与parallel-encoding背景、distribution misalignment、shared prefix/temperature/scaling、hierarchical softmax derivation、FlashAttention-compatible merge、4类实验、H100 latency contract、long-context comparison、cache combinatorics与limitations。
- **Original Problem:** sequential CAG 每个请求把检索上下文重新拼接并 prefill，TTFT随上下文长度增长；传统 prefix cache 只复用特定排列，组合变化导致命中率和存储爆炸。
- **Why the Previous Design Was Reasonable:** sequential encoding保留完整token order与cross-context attention，语义最接近训练分布；prefix cache对稳定前缀精确、无需改变attention。
- **Changed Constraint:** RAG/ICL context来自可独立存储、频繁重组的chunks，且工作负载是长输入短输出；需要让chunk KV可独立预计算、按查询组合复用。
- **Mechanism:** 各context独立编码并复用position；用shared prefix对齐初始KV方向，用temperature T校准context attention sharpness，用scaling S校准context mass，再将context与query/generated token的softmax统计分块合并。
- **State Ownership:** content store拥有chunk bytes与revision；encoder/model revision拥有KV identity；APE cache拥有独立chunk KV；request planner拥有chunk集合/顺序与T/S；attention kernel拥有归一化统计和output merge；decoder拥有后续token state。
- **Control Flow / Data Flow:** ingest context→按model/tokenizer/position/prefix生成chunk KV→request检索chunks→加载多组KV→分别计算context/non-context attention statistics→按APE公式merge→decode；chunk cache是proposal state，query attention决定实际使用。
- **Implementation Details:** context与non-context KV分开计算并以hierarchical softmax合并，可与FlashAttention类kernel兼容；prefix长度、T与S在小validation set上greedy search；无prefix时先加入两个换行符再搜索10/20/40 token prefix。
- **Evaluation Contract:** ChatRAG-Bench、LongBench、ICL、LOFT、CRAG；base models含 Llama-3/3.1-8B-Instruct、Mistral-7B-Instruct-v0.3、Gemma-2-9B-it与Llama-2-7B-chat的CEPE比较；efficiency固定query/output 256 tokens、context 2K～128K、batch 1/4。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较sequential、naive parallel、PCW、CEPE、MInference及long-context方法；分别消融prefix、T、S；shared prefix贡献最大，T单独收益小；复杂推理如GSM8K保真下降，且T/S对context分布敏感。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** efficiency用单张H100、Llama-3.1-8B-Instruct、vLLM、2K～128K context、256 query+generation、batch 1/4；精度、并发、p99与SLO `Not Disclosed`；4.5x/28x只绑定该合同。
- **What the Evidence Actually Proves:** 在作者CAG合同内，独立chunk KV并非只需拼接；必须校准attention distribution，才能同时获得可组合复用与接近sequential的质量。
- **What It Does Not Prove:** 不证明任意context关系可由独立编码保留，不证明100% cache hit等于更低fleet cost，不证明对所有模型、长上下文推理和线上并发成立。
- **Limitations / Threats to Validity:** T/S需按context长度、数量和内容校准；独立编码削弱context间关系；cache identity还依赖model/tokenizer/prefix/position/config；论文未披露multi-tenant invalidation和p99。
- **Trade-offs / New Failure Modes:** 用cross-context interaction与校准复杂度换取组合复用和低prefill；新增stale KV、错误cache key、distribution drift、chunk-order/position歧义、显存/存储压力与不同请求shape的调度碎片。
- **Where the Previous Design Still Applies:** 少量context、跨段关系强、query与context高度耦合或cache复用率低时，sequential encoding更稳健；固定共享前缀场景传统prefix cache更简单且exact。
- **Evolution Relationship:** `Direct Evolution`：sequential prefill→prefix cache→naive parallel chunk KV→distribution-aware parallel encoding；它扩展cache identity与attention algebra，而非消除long-context语义成本。
- **ROADMAP Node:** `INFER-PREFILL`（Ch43）主 owner；handoff `INFER-KV-CACHE` Ch45、`AGENT-RAG` Ch76、`MODEL-LONG-CONTEXT` Ch22 与 `INFER-SCHEDULING` Ch56。
- **Target and Adjacent Chapters Read:** 已核对 Ch42～45 的request/prefill/decode/KV生命周期、Ch54～56 memory/PD/scheduling，以及 Ch75～77 context/RAG/memory边界。
- **Existing Coverage:** Books已有prefix identity、prefill/decode分离与RAG provenance；本 family补充可组合chunk KV必须同时版本化attention calibration，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；98%/93%、4.5x与28x均保留模型、任务、H100、长度和batch边界。
- **Open Questions:** T/S能否按request在线估计；chunk间依赖怎样检测并回退sequential；KV revision/invalidation如何跨tenant治理；mixed batch如何计费和避免fragmentation。

### Hypencoder / Query-Specific Retrieval Function

- **Candidate / Week / Score:** Hypencoder / 2025-W06 / 24/30。
- **Source Family ID:** `hypencoder-query-conditioned-retrieval-function`。
- **Source Type:** arXiv v1 research paper。
- **First-public Date / Revision History:** arXiv v1 2025-02-07；v2 2025-05-01 为后续修订，不作为 W06 新事件。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05364；https://arxiv.org/abs/2502.05364。
- **Related Primary Sources:** MSMARCO、TREC DL、BE-Base、ColBERT、SPLADE、DRAGON、FollowIR与TOT原始资料仅用于数据/基线合同核验。
- **Access and Verification Status:** `Full Review Complete`；理论边界、hyperhead/q-net、approximate search、training、in/out-domain与hard-task evaluation、efficiency sensitivity和depth ablation已核验。
- **Full-read Coverage:** metadata、IR背景、inner-product separability论证、architecture/公式、q-net conversion、graph search、training pairs/loss、datasets、baselines、significance tests、latency-quality曲线、2/4/6/8-layer ablation与conclusion。
- **Original Problem:** bi-encoder用可索引单向量与inner product换取大规模检索效率，但query-document关系被固定线性score限制；cross-encoder表达力强却无法预计算文档。
- **Why the Previous Design Was Reasonable:** inner product支持ANN、索引成熟、延迟低、状态简单；在大规模first-stage retrieval中，它是可部署性的关键约束，而非错误设计。
- **Changed Constraint:** harder、instruction-conditioned与tip-of-the-tongue查询需要更复杂的relevance boundary，同时仍需保留单文档向量和近似检索。
- **Mechanism:** query encoder的全部token表示经hyper-head生成小型query-specific q-net权重；预计算的768维document vector直接进入q-net评分；graph search从初始候选出发，迭代扩展文档邻居，避免全库执行非线性score。
- **State Ownership:** document encoder/index拥有静态向量与邻接图；query encoder/hyper-head拥有临时q-net；search controller拥有visited/candidate/frontier；q-net拥有query-specific score；evaluator拥有relevance labels与metrics。
- **Control Flow / Data Flow:** documents→768D embeddings+100-neighbor graph；query→token embeddings→q-net weights；initial candidates→q-net score→top frontier→neighbor expansion/early stop→ranked results；每query生成的权重不写回document index。
- **Implementation Details:** BERT-base-uncased query/document encoders；q-net默认6个768维linear layers加projection、residual/ReLU/LayerNorm；batch 64/device、128 total；passage 196 tokens、query 32 tokens；Margin-MSE加in-batch CE。
- **Evaluation Contract:** MSMARCO 8.8M passages/503K train queries，TREC DL 2019/2020、MSMARCO Dev、BEIR-like OOD、DL-HARD、TOT、FollowIR；报告nDCG/MRR/Recall与p-MRR；approximate search graph每文档100 neighbors。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较BM25、ANCE、TCT-ColBERT、TAS-B、CL-DRD、BE-Base及参考ColBERTv2/SPLADE/DRAGON/RepLLaMA/cross-encoder；扫描initial candidates、nCandidates、maxIter、early stop与q-net depth 2/4/6/8；8层未继续改善。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** search latency用单张NVIDIA L40S、BF16、MSMARCO约8.8M passages；Efficient-1为59.6ms、Efficient-2为231.1ms、exhaustive为1769.8ms；并发、p99与SLO `Not Disclosed`；训练设备数量未完整披露。
- **What the Evidence Actually Proves:** 在作者检索合同内，可把query信息编码进评分函数而保持document预计算，并通过graph approximation在质量与延迟间选 operating point。
- **What It Does Not Prove:** 不证明非线性query-specific score普遍优于modern larger retrievers，不证明59.6ms是线上p99，不证明索引更新、分片和multi-tenant成本可忽略。
- **Limitations / Threats to Validity:** 训练依赖teacher labels与MSMARCO分布；部分hard datasets样本小；approximate graph参数与corpus耦合；q-net per-query生成和GPU residence增加调度状态；v1未给完整生产TCO。
- **Trade-offs / New Failure Modes:** 以更复杂query compute、动态权重和graph controller换取更强matching；新增frontier miss、teacher bias、graph staleness、q-net数值不稳定、GPU batching困难和tenant isolation问题。
- **Where the Previous Design Still Applies:** 高吞吐、简单semantic matching、严格CPU/内存预算或成熟ANN生态下，bi-encoder inner product仍更便宜；高精度小候选集可继续用cross-encoder rerank。
- **Evolution Relationship:** `Alternative Branch`：bi-encoder ANN与cross-encoder rerank之间增加“静态document state + 动态query function”分支；不是对两者的单向替代。
- **ROADMAP Node:** `AGENT-RAG`（Ch76）主 owner；handoff `PLATFORM-RESOURCE-SCHEDULING` Ch65、`PLATFORM-EVALUATION-SYSTEM` Ch66 与 `AGENT-CONTEXT` Ch75。
- **Target and Adjacent Chapters Read:** 已核对 Ch75～77 的context/retrieval/memory identity，并回看 Ch65～67 的resource/evaluation/observability contract。
- **Existing Coverage:** Books已有retrieval→rerank与embedding index边界；本 family补充“score function本身也可成为query state”的替代分支，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06；59.6ms不脱离L40S/BF16/8.8M corpus/approximation参数外推。
- **Open Questions:** q-net如何continuous batch；graph/index/model revision如何原子切换；per-query weights如何隔离与缓存；quality-latency operating point如何按tenant SLO选择。

### Show-o Turbo / arXiv:2502.05415 Event-Time v1

- **Candidate / Week / Score:** Show-o Turbo / arXiv:2502.05415v1 / 2025-W06 / 24/30。
- **Source Family ID:** `show-o-turbo-arxiv-id-repurposed-to-unicms`。
- **Source Type:** event-time arXiv v1 paper + official code；revision-identity correction。
- **First-public Date / Revision History:** v1 2025-02-08 标题为 `Show-o Turbo: Towards Accelerated Unified Multimodal Understanding and Generation`；v2 2025-05-18 改题为 `UniCMs` 且方法叙述重构。W06只审计v1，v2不得覆盖事件身份。
- **Direct Primary Sources:** https://arxiv.org/html/2502.05415v1；https://arxiv.org/pdf/2502.05415v1；https://arxiv.org/abs/2502.05415。
- **Related Primary Sources:** v1所链接official implementation；Show-o原论文只用于teacher/base mechanism核验。
- **Access and Verification Status:** `Full Review Complete`；v1 metadata、method、公式、training、evaluation、ablation与appendices已核验，并明确记录同一arXiv ID的标题/机制revision boundary。
- **Full-read Coverage:** unified-model背景、Show-o AR/masked decoding、Jacobi fixed-point、multimodal trajectory construction、consistency distillation、trajectory segmentation/curriculum、regularization、T2I/MMU evaluation、sampling/depth ablations、CFG与appendices。
- **Original Problem:** unified multimodal model对text用AR、对image用iterative masked decoding；两条生成路径都受逐步采样延迟限制，却缺少共同可蒸馏的trajectory表示。
- **Why the Previous Design Was Reasonable:** text AR保证causal factorization与质量，image masked refinement支持并行修正；模态分支尊重了不同输出结构，避免强行共享错误独立假设。
- **Changed Constraint:** 一个unified model需要同时降低text token与image sampling steps，且不能为每个模态维护完全独立的加速训练方案。
- **Mechanism:** 用Jacobi parallel decoding把AR text generation重写为fixed-point refinement trajectory；image沿Show-o masked-token trajectory；从teacher终点构造global consistency objective，并用trajectory segmentation、curriculum与regularization训练student在更少步接近终点。
- **State Ownership:** teacher sampler拥有deterministic text/image trajectories；segment scheduler拥有training interval；student拥有consistency mapping；CFG/top-k sampler拥有inference proposal；task evaluator拥有quality commit。
- **Control Flow / Data Flow:** prompt/modal input→teacher AR或masked trajectory→切分trajectory pairs→student consistency training→few-step text/image refinement→metric/evaluator；Jacobi guess是proposal，fixed point或step budget决定停止。
- **Implementation Details:** text trajectory使用greedy Jacobi，image trajectory含CFG；4→2→1 segment curriculum；full-parameter training优于LoRA的speed-quality组合；无regularization时collapse；top-k缓解few-step output uncertainty。
- **Evaluation Contract:** T2I用GenEval/HPS/ImageReward/CLIP Score，image-to-text用Flickr30K/NoCaps/TextCaps，MMU用POPE/MME/MMMU；比较Show-o、Jacobi与Show-o Turbo，在256/512 resolution及2/4/8 step等设置审计。
- **Baselines / Ablations / Sensitivity / Overhead:** ablate segment数、full tuning vs LoRA、regularization、top-k和CFG；naive Jacobi不加速原Show-o，证明trajectory distillation而非解码器替换承担收益；few-step质量、理解指标与速度存在不一致变化。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** text speed在单张RTX 4090测量；base为Show-o，image 256/512 resolution，部分ablation解码16 text tokens；training hardware、precision、batch、concurrency、p99/SLO `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者Show-o合同内，跨模态统一的价值来自共享“trajectory-to-endpoint”训练抽象；仅在inference套Jacobi不足以获得加速，curriculum与regularization决定稳定性。
- **What It Does Not Prove:** 不证明text与image有相同概率分解，不证明few-step速度普遍保持所有MMU/T2I质量，不证明v2 UniCMs结论可追溯为v1事件时证据。
- **Limitations / Threats to Validity:** v1没有独立limitations section；部分caption/understanding指标下降；teacher trajectory与CFG成本未计入部署总成本；training硬件和线上并发未披露；arXiv ID后续内容重写造成引用漂移。
- **Trade-offs / New Failure Modes:** 以distillation compute、teacher trajectory storage与regularization换取few-step采样；新增student collapse、fixed-point不收敛、跨模态负迁移、quality-speed operating point漂移和source identity污染。
- **Where the Previous Design Still Applies:** 质量优先、分布外输入、长开放文本或无需共享训练栈时，原AR text与iterative image decoding更稳健；LoRA在理解保真优先时仍可能比full tuning合适。
- **Evolution Relationship:** `Principle Reuse`：AR/Jacobi与masked diffusion不是同一机制，但都被重述为iterative trajectory后复用consistency distillation；不能写成单向替代。
- **ROADMAP Node:** `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）主 owner；handoff `INFER-SPECULATIVE-DECODING` Ch48、`TRAIN-PRETRAINING` Ch28 与 `PLATFORM-MODEL-REGISTRY` Ch59。
- **Target and Adjacent Chapters Read:** 已核对 Ch23～25 representation/generation/world-state边界，回看 Ch28、Ch48 与 Ch59 的training/proposal-commit/artifact identity合同。
- **Existing Coverage:** Books已有AR、diffusion、masked/block refinement的alternative branches；本 family补充trajectory-level principle reuse和revision identity风险，本轮不集成。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅补 W06并纠正年度索引中的UniCMs误归；不把v2标题或5月机制倒灌到2月。
- **Open Questions:** 如何为被重写的arXiv ID建立content hash；teacher trajectory成本如何计入lifecycle；fixed-point停止如何按模态校准；v1→v2是否应拆成两个source family alias。

### Jailbreaking to Jailbreak

- **Candidate / Week / Score:** Jailbreaking to Jailbreak / 2025-W06 / 26/30。
- **Source Family ID:** `j2-agentic-multi-turn-red-teaming`。
- **Source Type:** arXiv v1 research paper + author research page；敏感 attack prefix 与完整 prompts 未公开。
- **First-public Date / Revision History:** arXiv v1 2025-02-09；Hugging Face 2025-02-17 推荐日不是事件日期；本周锁定 v1。
- **Direct Primary Sources:** https://arxiv.org/html/2502.09638v1；https://arxiv.org/abs/2502.09638；https://scale.com/research/j2。
- **Related Primary Sources:** HarmBench、ActorAttack、Best-of-N、Bijection 与 browser-agent jailbreak work 只用于 threat model 和 baseline genealogy。
- **Access and Verification Status:** Full Source Review Complete；Method、workflow、HarmBench setup、baseline comparison、qualitative failure analysis、judge prompts 与 workflow Appendix 已核验；作者为防滥用未公开关键 jailbreak prefix。
- **Full-read Coverage:** 已读 Abstract、Introduction、Background、J2 construction、strategy set、planning/attack/debrief cycles、50-behavior tuning、200-behavior evaluation、related work、conclusion 与 Appendix B/C；附录攻击样例只核验结构，不复制敏感内容。
- **Original Problem:** 人工 red teaming 能根据失败迭代策略但昂贵且难复现；传统自动攻击可扩展，却常依赖白盒梯度、固定字符串搜索或缺少跨轮策略记忆。
- **Why the Previous Design Was Reasonable:** 人类评测在开放式语义攻击上判断力强；单轮/算法攻击更容易标准化、隔离和计量；把 refusal model 当 attacker 会首先触发其自身 safeguard。
- **Changed Constraint:** frontier model 具有足够的规划、说服和 in-context adaptation 能力，而公开 API 只提供黑盒输入输出；评测系统需要在不访问权重的情况下规模化探索 multi-turn failure modes。
- **Mechanism:** 人类先形成可迁移的 attacker conversation prefix，使 refusal-trained model 愿意 red-team；随后 J2 在 9 类策略上执行 planning→T-turn attack→external-judge debrief，失败轨迹保留在 attacker context 中循环最多 N 次，策略耗尽时 reset cycle history。
- **State Ownership:** 人类 prefix 拥有 attacker role/policy initialization；J2 context 拥有策略、失败轨迹和自我修订状态；target model 拥有独立 conversation history；外部 judges 拥有 workflow stop signal 与最终 ASR commit。
- **Control Flow / Data Flow:** harmful behavior+strategy→J2 planning→J2/target 交替消息（双方分别映射为 user input）→GPT-4o workflow judge→J2 debrief/self-score→继续 cycle 或切换策略→独立 ActorAttack judge 复核最终 success。
- **Implementation Details:** 9 个手工策略、拒绝字符串检测与恢复提示、按 attacker 调节 T、默认 N=6、temperature-0 judges；target 看不到 attacker 的 lecture/planning/debrief history，attacker 保留全部失败 cycles。
- **Evaluation Contract:** 先用 HarmBench 50 个 standard text behaviors 选择 attacker、cycle 与 turns，再在 200 个 val+test behaviors 上比较 GPT-4o、Gemini-1.5-Pro、Sonnet-3.5 与 Llama-3.1-405B targets；ASR 需同时通过 workflow judge 和 ActorAttack judge。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 GCG、PAIR、PAP、CipherChat、CodeAttack、Best-of-N、ActorAttack、Bijection 与人工攻击；分析 attacker backbone、strategy-set size、cycle count 和 turn count；更多 turns 会因 goal drift 降低 ASR，未提供 token/cost latency accounting。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** proprietary API models 与 Llama-3.1-405B；硬件、precision、完整 context length、batch、并发、wall-clock 与 production SLO 均 Not Disclosed；N/T/strategy count 只定义 query workflow。
- **What the Evidence Actually Proves:** 在作者 HarmBench 黑盒合同和双 judge operating point 下，被人类 jailbreak 后的强模型能把失败轨迹转为后续策略，并以多轮自动 red teaming 暴露 refusal safeguard 的 capability-composition failure。
- **What It Does Not Prove:** 不证明报告 ASR 可跨模型版本、policy、judge 或真实部署复现；不证明 J2 优于所有自动攻击或安全训练无效；也不证明自动 judge 能替代人工安全审查。
- **Limitations / Threats to Validity:** 关键 prefix 未公开导致不可完全复现；策略由单个有经验 red teamer 整理；proprietary model drift、judge bias、HarmBench 覆盖范围、危险样例删减和成本未披露限制外推。
- **Trade-offs / New Failure Modes:** 以更高 query/context/judge 成本换取策略适应与可扩展性；同时新增 attacker safeguard 被降级、失败轨迹污染、goal drift、judge reward hacking、跨模型 prefix transfer 和工具型 agent 触发现实伤害的风险。
- **Where the Previous Design Still Applies:** 高风险发布仍需人工红队、受控沙箱和独立审计；单轮/白盒攻击在可访问权重、需要严格复现或成本受限时更合适；static refusal 对低互动面仍是必要防线。
- **Evolution Relationship:** `Direct Evolution`：manual semantic red teaming→fixed automated attacks→LLM attacker with iterative failure memory；`Layering / Dependency`：J2 叠加而非替代 sandbox、independent judge 与 human review。
- **ROADMAP Node:** `PLATFORM-SECURITY`（Ch72）主 owner；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66、`AGENT-REFLECTION` Ch80、`AGENT-WORKFLOW` Ch81 与 `AGENT-PLATFORM` Ch84。
- **Target and Adjacent Chapters Read:** 已核对 Ch66、Ch71～73、Ch80～84 的 threat model、evaluation operating point、workflow state、tool boundary 与 release gate。
- **Existing Coverage:** Books 已覆盖 adaptive red teaming、judge uncertainty 与 agent sandbox；本 family 提供“先破坏 attacker safeguard，再组合 attacker+target”的 capability-composition failure，Books 判断延期。
- **Integration Decision:** `Books Pending — Integration Deferred`。
- **Changed Files or Rejection Reason:** 仅更新 W06 与年度 cursor；不复制敏感 prompts，不修改 Books。
- **Open Questions:** 如何给 attacker/target/judge/policy 建立版本闭包；如何在保持可复现的同时限制危险 artifact；ASR 如何加入人工抽样、judge disagreement 与 per-query cost；tool-enabled targets 如何建立不可逃逸的副作用隔离。

## Low-Score Verification Ledger

重评分后共有 6 个低分候选，均已完成 identity、event date、score 与 rejection boundary 核验；低分不等于来源不可靠，而是没有形成新的、可长期复用的 AI System mechanism owner。

- **Transformers 4.48.3 / 16/30:** official release 2025-02-07；修复Python 3.9 compatibility、dynamic RoPE device、`num_items_in_batch` kwargs与PaliGemma2 generation。`Low-score Verified — Weekly Only / Patch Fact`；没有形成独立长期机制，后续若追踪dynamic RoPE或batch-loss contract应回到具体PR，而非把patch release当设计证据。
- **MLX 0.22.1 / 15/30:** official signed tag/release 2025-02-06；release正文未披露独立feature或机制说明。`Low-score Verified — Weekly Only / Version Fact / Mechanism Not Disclosed`；不可从版本号或asset反推ABI、kernel或runtime行为。
- **LayerTracer / 18/30:** arXiv v1 2025-02-03；已读 20K layered-SVG dataset、4/9-frame serpentine grid、rank-256 LoRA、20K+20K steps、image-conditioned diffusion、raster differencing/morphology 与 vtracer vectorization、50-prompt/50-image evaluation、46人 user study 和 limitations。它证明在作者窄域合同内，“生成分层 raster blueprint→逐层 vectorize/deduplicate”可降低优化式 SVG pipeline 的时间与 path count；但主要复用与 MakeAnything 相同的 grid/LoRA principle，依赖 vtracer 手工参数，复杂/OOD 图像失败，样本规模小，且 Table 1 把 `CLIP-Score↓` 标为越低越好却将 33.76 加粗为最佳，metric direction 自相矛盾。`Low-score Verified — Weekly Only / Narrow-domain Application / Principle Reuse`；不建立新的 Books owner。
- **Competitive Programming with Large Reasoning Models / 19/30:** arXiv v1 2025-02-03；论文比较 o1、early o3 与手工 o1-ioi pipeline，证明在其 IOI/Codeforces 合同内 general-purpose reasoning RL 的 capability 可超过领域heuristics。它没有公开训练机制、模型规模、硬件或可复现 runtime，且主要是 capability evidence，与本周 PRIME/CodeSteer/CODESIM 的系统机制 owner 重叠。`Low-score Verified — Weekly Only / Capability Evidence / Mechanism Not Disclosed`。
- **Éclair / 19/30:** arXiv v1 2025-02-06；identity、document-level OCR/layout/reading-order/semantic-class task 与human-annotated benchmark已核验。它是高价值 data-ingestion application，但本轮没有形成超出既有 multimodal representation、data curation 与 RAG parsing 的独立长期机制；headline accuracy不在缺少完整deployment contract时外推。`Low-score Verified — Weekly Only / Domain Application`。
- **CAD-Editor / 19/30:** arXiv v1 2025-02-06；identity、automated triplet synthesis与locate-then-infill decomposition已核验。该方法在文本CAD编辑窄域复用“先定位mutable span再局部生成”的通用原则，但数据依赖LVLM差异摘要，几何validity、artifact revision与真实CAD workflow未形成新的全书owner。`Low-score Verified — Weekly Only / Domain Application / Principle Reuse`。

## Evidence Level

- OmniHuman-1、PRIME、DeepRAG、FastKV、SmolLM2、LIMO、recurrent-depth latent reasoning、Sliding Tile Attention、QuEST、BOLT、Satori、QLASS、On-device Sora、KVFundaBench/ShotKV、AlphaGeometry2、ScoreFlow、VideoRoPE、SCONE、InferenceGuard、Transformer World Models、LongDPO、VideoJAM、IBMD、Demystifying Long CoT、Teacher Hacking、Token Assorted、PyCapsule、ConceptAttention、UltraIF、Goku、Self-Backtracking、DuoGuard、Symbolic World Models、CMoE、CodeSteer 与 VectorQ：作者 primary paper / artifact，`Status: Experimental`；只证明作者实验合同。
- vLLM 0.7.2：official release + 可访问PR完成family review；部分linked PR只能支持版本事实。Gemini 2.0已完成release/model-card边界审计，结论仍为`Weekly Only / Version Fact / Mechanism Not Disclosed`。
- Transformers 4.48.3与MLX 0.22.1：低分官方patch/version fact，已完成拒绝核验。
- 校准提升的 22 个 academic candidates 已全部完成 Full Source Review；SynCD 的 arXiv/CVF PDF 直传异常由作者项目、official repository/dataset 与 CVF 全文索引联合恢复，并保留 transport boundary。
- SliderSpace 只证明 encoder-weighted output variation 可转为 controls；MakeAnything 只证明 fixed-grid procedural representation；TwinMarket 只证明作者环境内的 multi-agent feedback loop。三者均不得外推为 causal interpretability、真实历史重建或市场预测。
- The Curse of Depth、Social-Deduction MARL、LM2、Hierarchical Drafting、Gemstones、CTRL 与 NoLiMa 均完成事件时 arXiv v1 Full Source Review；分别限定在作者 normalization、sandbox MARL、1.7B memory architecture、单 GPU speculative decoding、≤2B scaling suite、code-execution critique 与 synthetic long-context benchmark 合同内。
- CODESIM、APE、Hypencoder、Show-o Turbo 与 Jailbreaking to Jailbreak 均完成事件时全文审计；其中 arXiv:2502.05415 的 v1/v2 内容身份漂移已显式隔离，不能把当前 UniCMs metadata 当作 2 月技术事实；J2 则明确隔离 2 月 9 日 v1 与 2 月 17 日推荐日期。
- LayerTracer、Competitive Programming、Éclair、CAD-Editor 与两个 official patch/version fact 已完成低分拒绝核验；W06 不再有 `Verification Pending`。
- 社区观点未作为机制证据；跨 family 的 evolution connection 是本项目推断。

## Cross-Week Deduplication

- CUT3R / arXiv:2501.12387 v1 为 2025-01-21，已回拨 W04；W06 只保留 discovery trail。
- Gemini 2.0 的 2024-12 experimental introduction 与 2025-01 app rollout 不在本周重复计分；本周 node 仅为 2月5日 API GA/Flash-Lite preview。
- 同一论文后续 revision、项目页或 release 与 v1 共享 Source Family，不创建重复评分行。

## Knowledge Tree Position

- OmniHuman-1 → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23/25/27。
- PRIME → `TRAIN-RLHF`（Ch31），handoff Ch32/33/66。
- DeepRAG → `AGENT-RAG`（Ch76），handoff Ch75/77/79/66。
- FastKV → `INFER-PREFILL`（Ch43），handoff Ch45/47/56。
- vLLM 0.7.2 → `INFER-VLLM`（Ch50），handoff Ch46/47/56/72。
- SmolLM2 → `TRAIN-DATA`（Ch27），handoff Ch22/28/29/34/35。
- LIMO → `TRAIN-SFT`（Ch29），handoff Ch27/28/66。
- recurrent-depth latent reasoning → `MODEL-TRANSFORMER-LAYER`（Ch17），handoff Ch20/45/48/56。
- Sliding Tile Attention → `INFER-TENSORRT-LLM`（Ch49），handoff Ch14/24/54。
- QuEST → `TRAIN-PRETRAINING`（Ch28），handoff Ch35/49/54。
- BOLT → `TRAIN-SFT`（Ch29），handoff Ch20/34/66。
- Satori → `TRAIN-PPO`（Ch32），handoff Ch31/33/79/80。
- QLASS → `AGENT-PLANNING`（Ch79），handoff Ch31/66/80/81。
- On-device Sora → `INFER-GPU-MEMORY`（Ch54），handoff Ch24/49/56。
- KVFundaBench / ShotKV → `INFER-KV-CACHE`（Ch45），handoff Ch43/47/56/66。
- AlphaGeometry2 → `AGENT-PLANNING`（Ch79），handoff Ch66/81/82。
- ScoreFlow → `AGENT-WORKFLOW`（Ch81），handoff Ch34/66/79/82。
- VideoRoPE → `MODEL-POSITION-ENCODING`（Ch13），handoff Ch22/23/45。
- SCONE → `MODEL-EMBEDDING`（Ch12），handoff Ch11/28/54/65。
- InferenceGuard → `PLATFORM-SECURITY`（Ch72），handoff Ch56/66/81。
- Transformer World Models → `MULTIMODAL-WORLD-MODELS`（Ch25），handoff Ch31/32/66/79。
- LongDPO → `TRAIN-DPO`（Ch34），handoff Ch31/66/77/81。
- VideoJAM → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23/25。
- Inverse Bridge Matching Distillation → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch42/66。
- Demystifying Long CoT → `TRAIN-RLHF`（Ch31），handoff Ch29/32/33/56/66。
- Teacher Hacking → `TRAIN-SFT`（Ch29），handoff Ch27/31/66。
- Token Assorted → `MODEL-TOKENIZER`（Ch11），handoff Ch12/20/43/45。
- PyCapsule → `AGENT-WORKFLOW`（Ch81），handoff Ch78/79/80/82。
- ConceptAttention → `WORLDVIEW-REPRESENTATION`（Ch5），handoff Ch14/23/24/66。
- UltraIF → `TRAIN-DATA`（Ch27），handoff Ch29/31/34/66。
- Goku → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23/25/28/36/49。
- Self-Backtracking → `AGENT-PLANNING`（Ch79），handoff Ch31/66/80/81。
- DuoGuard → `PLATFORM-SECURITY`（Ch72），handoff Ch27/31/34/66。
- Symbolic World Models → `MULTIMODAL-WORLD-MODELS`（Ch25），handoff Ch66/79。
- CMoE → `MODEL-MOE`（Ch21），handoff Ch16/49/56。
- CodeSteer → `AGENT-PLANNING`（Ch79），handoff Ch66/78/80/81。
- VectorQ → `PLATFORM-GATEWAY`（Ch62），handoff Ch42/66/71。
- Gemini 2.0 GA → `PLATFORM-MODEL-REGISTRY`（Ch59），handoff Ch57/61/66/72；仅版本事实。
- SliderSpace → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch5/30/66；只按 output-distribution decomposition 记录。
- MakeAnything → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch25/27/30；不视为 causal world model。
- TwinMarket → `AGENT-MULTI-AGENT`（Ch82），handoff Ch66/67/72/81；不把 stylized-fact reproduction 视为 predictive validity。
- The Curse of Depth → `MODEL-TRANSFORMER-LAYER`（Ch17），handoff Ch7/28；保留 Pre-LN stability 与 depth utilization 的共存边界。
- Social-Deduction MARL → `AGENT-MULTI-AGENT`（Ch82），handoff Ch66/72/81；communication influence reward不等于truthfulness。
- LM2 → `MODEL-LONG-CONTEXT`（Ch22），handoff Ch45/72/77；architecture-level writable memory与KV/RAG并列。
- Hierarchical Drafting → `INFER-SPECULATIVE-DECODING`（Ch48），handoff Ch54/56/72；database只proposal，target verifier拥有commit。
- Gemstones → `WORLDVIEW-SCALING-LAW`（Ch7），handoff Ch28/36；fit pipeline与parallel runtime属于scaling contract。
- CTRL → `AGENT-REFLECTION`（Ch80），handoff Ch31/66/81；以修订后的execution outcome训练feedback policy。
- NoLiMa → `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff Ch22/43/45；claimed context不能替代latent-association effective length。
- CODESIM → `AGENT-WORKFLOW`（Ch81），handoff Ch66/72/79/80；plan simulation把验证前移，但hidden executable tests仍拥有commit。
- APE → `INFER-PREFILL`（Ch43），handoff Ch22/45/56/76；independent chunk KV需要attention calibration与完整cache identity。
- Hypencoder → `AGENT-RAG`（Ch76），handoff Ch65/66/75；属于static document state与dynamic query function的替代分支。
- Show-o Turbo → `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch28/48/59；v1 trajectory distillation与v2 UniCMs必须按revision隔离。
- Jailbreaking to Jailbreak → `PLATFORM-SECURITY`（Ch72），handoff Ch66/80/81/84；attacker、target 与 judge 必须分别版本化，不能把高 ASR 当作普适部署事实。
- Competitive Programming、Éclair 与 CAD-Editor → `Weekly Only`；分别是mechanism-not-disclosed capability evidence、document ingestion应用和CAD领域principle reuse。
- LayerTracer → `Weekly Only / Narrow-domain Principle Reuse`；不建立新的 Books owner。

## Recommended Action

- W06 `Weekly Evidence Gate` 已重新通过：78/78 candidates 均有 disposition，72/72 `20+` Full Source Review 与 6/6 low-score verification 全部闭合。
- Forward cursor 可进入 W07；Historical Books Gate 继续关闭，不因 Weekly 通过而启动 Books Integration。

## Event-Date Daily Decision

历史回填不创建 Daily。真实 event date、spillback 与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

`Historical Books Gate: Closed`。用户明确要求先完成 2025 Weekly；72 个已完成 Source Review 均标记
`Books Pending — Integration Deferred`，不代表已经写入 Books。6 个低分候选只保留 Weekly disposition，不支持长期正文。

## Ignored Noise

- 不保留旧内容重发、无 primary source 的媒体转述、未绑定 workload contract 的 benchmark headline。
- Hugging Face/Scholar 的推荐和排序只是 discovery signal，不是 event date、可靠性或技术新颖度证明。
- 普通 issue/commit、model-support 清单和无机制 patch 不因数量多而形成独立候选。

## Repository Changes

- 用 78 项候选 census 替换旧版错误的 “No Material Update” 周报，并把两个patch release纳入低分分母。
- 完成 72/72 个 `20+` 候选的非模板化 30 字段 Full Source Review；W07/W08 look-ahead 回拨的 12 个高分 family 均已按 v1 日期完成全文、实验、limitations、artifact与owner审计。
- 将 `Jailbreaking to Jailbreak` 按 2025-02-09 v1 回拨 W06；明确 Hugging Face 2025-02-17 是 discovery signal，不是 event date。
- 纠正 arXiv:2502.05415 的事件身份：2025-02-08 v1 是 Show-o Turbo，2025-05-18 v2 才是 UniCMs；同一 identifier 的实质内容重写已记录为 revision risk。
- UltraIF 的普通 HTML 在本轮返回错误，已改用锁定事件时版本的 arXiv v1 PDF 完成全文范围审计，没有用当前 v2 或摘要替代。
- On-device Sora的arXiv HTML错页/PDF访问问题已通过arXiv metadata、CC BY v1全文副本与official repository三方闭合。
- Gemini 2.0 GA 明确保留为版本事实，不反推内部机制；CodeSteer 则记录事件时 arXiv transport gap 与后续 official publication/artifact 的联合核验边界。
- 完成 Transformers 4.48.3、MLX 0.22.1、LayerTracer、Competitive Programming、Éclair 与 CAD-Editor 的低分 version/identity/rejection 核验。
- 将 CUT3R 按 2025-01-21 v1 回拨 W04，完成全文审计并重新通过前周 Gate。
- 未修改 Books；未 stage、commit 或 push。

## Open Questions

- vLLM 0.7.2 的 V1 scheduler slot、prefix-cache hash 与 structured decoding changes 分别由哪些 PR/code path 证明？
- KV selection/compression 方法在 continuous batching、prefix sharing 与 fallback 下如何保持 cache identity？
- reasoning RL 的 verifier、PRM、policy 和 rollout version 如何进入 checkpoint/replay contract？
- W06 high-score Full Review Pending 与 low-score Verification Pending 均已归零；W07 spillback Gate 重新通过后才恢复 W08，后续推荐页若再暴露 2月3～9日 owner 仍须回拨重开。

## Sources

- OmniHuman-1 — https://arxiv.org/html/2502.01061v1；https://arxiv.org/abs/2502.01061；https://omnihuman-lab.github.io/（First Public: 2025-02-03；Accessed: 2026-08-18）
- PRIME — https://arxiv.org/html/2502.01456v1；https://arxiv.org/abs/2502.01456（First Public: 2025-02-03；Accessed: 2026-08-18）
- DeepRAG — https://arxiv.org/html/2502.01142v1；https://arxiv.org/abs/2502.01142（First Public: 2025-02-03；Accessed: 2026-08-18）
- FastKV — https://arxiv.org/html/2502.01068v1；https://arxiv.org/abs/2502.01068（First Public: 2025-02-03；Accessed: 2026-08-18）
- Gemini 2.0 model updates — https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-updates-february-2025/（Published: 2025-02-05；Accessed: 2026-08-18）
- vLLM 0.7.2 — https://github.com/vllm-project/vllm/releases/tag/v0.7.2（Published: 2025-02-06；Accessed: 2026-08-18）
- vLLM prefix-cache collision avoidance — https://github.com/vllm-project/vllm/pull/12621（Merged: 2025-02-05；Accessed: 2026-08-18）
- vLLM structured-decoding thread pool — https://github.com/vllm-project/vllm/pull/12368（Merged: 2025-02-05；Accessed: 2026-08-18）
- Transformers 4.48.3 — https://github.com/huggingface/transformers/releases/tag/v4.48.3（Published: 2025-02-07；Accessed: 2026-08-18）
- MLX 0.22.1 — https://github.com/ml-explore/mlx/releases/tag/v0.22.1（Published: 2025-02-06；Accessed: 2026-08-18）
- SCONE — https://arxiv.org/abs/2502.01637；https://arxiv.org/html/2502.01637v1（First Public: 2025-02-03；Accessed: 2026-08-18）
- Almost Surely Safe Alignment / InferenceGuard — https://arxiv.org/abs/2502.01208；https://arxiv.org/html/2502.01208v1（First Public: 2025-02-03；Accessed: 2026-08-18）
- KV Cache Fundamental-Abilities Study / ShotKV — https://arxiv.org/abs/2502.01941；https://arxiv.org/html/2502.01941v1（First Public: 2025-02-04；Accessed: 2026-08-18）
- Improving Transformer World Models — https://arxiv.org/abs/2502.01591；https://arxiv.org/html/2502.01591v1（First Public: 2025-02-03；Accessed: 2026-08-18）
- LongDPO — https://arxiv.org/abs/2502.02095；https://arxiv.org/html/2502.02095v1（First Public: 2025-02-04；Accessed: 2026-08-18）
- VideoJAM — https://arxiv.org/abs/2502.02492；https://arxiv.org/html/2502.02492v1（First Public: 2025-02-04；Accessed: 2026-08-18）
- Inverse Bridge Matching Distillation — https://arxiv.org/abs/2502.01362；https://arxiv.org/html/2502.01362v1（First Public: 2025-02-03；Accessed: 2026-08-18）
- Demystifying Long CoT — https://arxiv.org/abs/2502.03373；https://arxiv.org/html/2502.03373v1；https://github.com/eddycmu/demystify-long-cot（First Public: 2025-02-05；Accessed: 2026-08-18）
- Teacher Hacking — https://arxiv.org/abs/2502.02671；https://arxiv.org/html/2502.02671v1（First Public: 2025-02-04；Accessed: 2026-08-18）
- SmolLM2 — https://arxiv.org/abs/2502.02737（First Public: 2025-02-04；Accessed: 2026-08-18）
- LIMO — https://arxiv.org/abs/2502.03387（First Public: 2025-02-05；Accessed: 2026-08-18）
- AlphaGeometry2 — https://arxiv.org/abs/2502.03544；https://arxiv.org/html/2502.03544v1（First Public: 2025-02-05；Accessed: 2026-08-18）
- ScoreFlow — https://arxiv.org/abs/2502.04306；https://arxiv.org/html/2502.04306v1；https://github.com/Gen-Verse/ScoreFlow（First Public: 2025-02-06；Accessed: 2026-08-18）
- Latent Reasoning Test-Time Scaling — https://arxiv.org/abs/2502.05171（First Public: 2025-02-07；Accessed: 2026-08-18）
- VideoRoPE — https://arxiv.org/abs/2502.05173；https://arxiv.org/html/2502.05173v1（First Public: 2025-02-07；Accessed: 2026-08-18）
- Sliding Tile Attention — https://arxiv.org/abs/2502.04507；https://arxiv.org/html/2502.04507（First Public: 2025-02-06；Accessed: 2026-08-18）
- QuEST — https://arxiv.org/abs/2502.05003（First Public: 2025-02-07；Accessed: 2026-08-18）
- On-device Sora — https://arxiv.org/abs/2502.04363；https://github.com/eai-lab/On-device-Sora；https://www.researchgate.net/publication/388848174_On-device_Sora_Enabling_Diffusion-Based_Text-to-Video_Generation_for_Mobile_Devices（First Public: 2025-02-05；Accessed: 2026-08-18）
- BOLT — https://arxiv.org/abs/2502.03860；https://arxiv.org/html/2502.03860（First Public: 2025-02-06；Accessed: 2026-08-18）
- Satori — https://arxiv.org/abs/2502.02508；https://arxiv.org/html/2502.02508（First Public: 2025-02-04；Accessed: 2026-08-18）
- QLASS — https://arxiv.org/abs/2502.02584；https://arxiv.org/html/2502.02584（First Public: 2025-02-04；Accessed: 2026-08-18）
- Token Assorted — https://arxiv.org/abs/2502.03275；https://arxiv.org/html/2502.03275v1（First Public: 2025-02-05；Accessed: 2026-08-18）
- LLM Guided Self-Debugging / PyCapsule — https://arxiv.org/abs/2502.02928；https://arxiv.org/html/2502.02928v1（First Public: 2025-02-05；Accessed: 2026-08-18）
- ConceptAttention — https://arxiv.org/abs/2502.04320；https://arxiv.org/html/2502.04320v1（First Public: 2025-02-06；Accessed: 2026-08-18）
- UltraIF — https://arxiv.org/abs/2502.04153；https://arxiv.org/pdf/2502.04153v1（First Public: 2025-02-06；Accessed: 2026-08-18；event-time v1 PDF fallback）
- Goku — https://arxiv.org/abs/2502.04896；https://arxiv.org/html/2502.04896v1（First Public: 2025-02-07；Accessed: 2026-08-18）
- Self-Backtracking — https://arxiv.org/abs/2502.04404；https://arxiv.org/html/2502.04404v1（First Public: 2025-02-06；Accessed: 2026-08-18）
- DuoGuard — https://arxiv.org/abs/2502.05163；https://arxiv.org/html/2502.05163v1；https://github.com/yihedeng9/DuoGuard（First Public: 2025-02-07；Accessed: 2026-08-18）
- Symbolic World Models — https://arxiv.org/abs/2502.04728；https://arxiv.org/html/2502.04728v1（First Public: 2025-02-07；Accessed: 2026-08-18）
- CMoE — https://arxiv.org/abs/2502.04416；https://arxiv.org/html/2502.04416v1；https://github.com/JarvisPei/CMoE（First Public: 2025-02-06；Accessed: 2026-08-18）
- CodeSteer — https://arxiv.org/abs/2502.04350；https://proceedings.mlr.press/v267/chen25x.html；https://github.com/yongchao98/CodeSteer-v1.0（First Public: 2025-02-04；Accessed: 2026-08-18）
- VectorQ — https://arxiv.org/abs/2502.03771；https://arxiv.org/html/2502.03771v1（First Public: 2025-02-06；Accessed: 2026-08-18）
- Gemini 2.0 Flash model card — https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-0-Flash-Model-Card.pdf（Updated: 2025-04-15；Accessed: 2026-08-18；later revision context only）
- SliderSpace — https://arxiv.org/html/2502.01639v1；https://arxiv.org/abs/2502.01639；https://github.com/rohitgandikota/sliderspace；https://sliderspace.baulab.info/（First Public: 2025-02-03；Accessed: 2026-08-18）
- MakeAnything — https://arxiv.org/html/2502.01572v1；https://arxiv.org/abs/2502.01572；https://github.com/showlab/MakeAnything（First Public: 2025-02-03；Accessed: 2026-08-18）
- TwinMarket — https://arxiv.org/html/2502.01506v1；https://arxiv.org/abs/2502.01506；https://github.com/freedomintelligence/TwinMarket（First Public: 2025-02-03；Accessed: 2026-08-18）
- LayerTracer — https://arxiv.org/html/2502.01105v1；https://arxiv.org/abs/2502.01105；https://github.com/showlab/LayerTracer（First Public: 2025-02-03；Accessed: 2026-08-18）
- The Curse of Depth — https://arxiv.org/html/2502.05795v1；https://arxiv.org/abs/2502.05795；https://github.com/lmsdss/LayerNorm-Scaling（First Public: 2025-02-09；Accessed: 2026-08-18）
- Social-Deduction MARL — https://arxiv.org/html/2502.06060v1；https://arxiv.org/abs/2502.06060（First Public: 2025-02-09；Accessed: 2026-08-18）
- LM2 — https://arxiv.org/html/2502.06049v1；https://arxiv.org/abs/2502.06049；https://github.com/convergence-ai/lm2（First Public: 2025-02-09；Accessed: 2026-08-18）
- Hierarchical Drafting — https://arxiv.org/html/2502.05609v1；https://arxiv.org/abs/2502.05609；https://github.com/hemingkx/Spec-Bench（First Public: 2025-02-08；Accessed: 2026-08-18）
- Gemstones — https://arxiv.org/html/2502.06857v1；https://arxiv.org/abs/2502.06857；https://github.com/mcleish7/gemstone-scaling-laws（First Public: 2025-02-07；Accessed: 2026-08-18）
- CTRL — https://arxiv.org/html/2502.03492v1；https://arxiv.org/abs/2502.03492（First Public: 2025-02-05；Accessed: 2026-08-18）
- NoLiMa — https://arxiv.org/html/2502.05167v1；https://arxiv.org/abs/2502.05167（First Public: 2025-02-07；Accessed: 2026-08-18）
- CODESIM — https://arxiv.org/pdf/2502.05664v1；https://arxiv.org/abs/2502.05664；https://aclanthology.org/2025.findings-naacl.285/；https://github.com/kagnlp/CodeGenerator（First Public: 2025-02-08；Accessed: 2026-08-18）
- APE — https://arxiv.org/html/2502.05431；https://arxiv.org/abs/2502.05431；https://github.com/Infini-AI-Lab/APE（First Public: 2025-02-08；Accessed: 2026-08-18）
- Hypencoder — https://arxiv.org/html/2502.05364；https://arxiv.org/abs/2502.05364（First Public: 2025-02-07；Accessed: 2026-08-18）
- Show-o Turbo / arXiv:2502.05415v1 — https://arxiv.org/html/2502.05415v1；https://arxiv.org/pdf/2502.05415v1；https://arxiv.org/abs/2502.05415（First Public: 2025-02-08；v2 renamed/reworked as UniCMs on 2025-05-18；Accessed: 2026-08-18）
- Jailbreaking to Jailbreak — https://arxiv.org/html/2502.09638v1；https://arxiv.org/abs/2502.09638；https://scale.com/research/j2（First Public: 2025-02-09；Accessed: 2026-08-18）
- Competitive Programming with Large Reasoning Models — https://arxiv.org/abs/2502.06807（First Public: 2025-02-03；Accessed: 2026-08-18）
- Éclair — https://arxiv.org/abs/2502.04223（First Public: 2025-02-06；Accessed: 2026-08-18）
- CAD-Editor — https://arxiv.org/abs/2502.03997（First Public: 2025-02-06；Accessed: 2026-08-18）
