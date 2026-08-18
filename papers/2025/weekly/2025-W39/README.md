# AI Research Weekly — 2025-W39

> Coverage Window: 2025-09-22～2025-09-28
> Research Mode: Retrospective Backfill — Full Discovery Replay
> Accessed: 2026-08-24
> Re-audited: 2026-08-24
> Status: Weekly Evidence Gate Passed；Historical Books Gate Closed

## Executive Summary

本周旧档案只有 DeepSeek-V3.1-Terminus 一行，不能代表真实覆盖。按机构、逐日 arXiv/Hugging Face、学术 metadata、AI Infra release 以及 W40 look-ahead 重放后，本周闭合为 **64 个评分候选**：34 个 25～30 分、10 个 20～24 分、20 个低于 20 分。44 个 retained source family 均完成非模板化 Full Source Review；20 个低分 family 均完成 primary identity、v1 日期、六维评分和拒绝理由核验。

本周长期信号不是“又出现一批模型”，而是五条相互连接的系统路线：

1. **统一多模态开始受 runtime contract 约束。** Qwen3-Omni 把 representation、absolute time identity、Thinker/Talker state、chunked prefill、multi-codebook speech 与并发放到同一系统里；LongLive 则把 interactive prompt change 转化为 KV recache 与 streaming state mutation。
2. **长期状态不再等于无限保留。** EpiCache 把 conversation episode 作为 KV ownership 单位，用 block-wise prefill 控制 peak memory；CompLLM 把 soft compressed representations 变成可复用 context artifact。两者都以语义损失、identity 与 invalidation 换取 memory/latency。
3. **RL 的瓶颈从“有无 reward”转向 sample、credit 与 entropy 的控制。** RLPT、VCRL、MMR1、CE-GPPO、Tree-GRPO、SPEAR、verbal-feedback learning 分别重写 objective、curriculum、variance、clipping、trajectory topology、experience replay 与 feedback representation。
4. **evaluation 不能把单次 verdict 当作事实。** TrustJudge 与 Judgment Noise 揭示 judge distribution、tie、transitivity、rubric adherence 与 latent variance；Strategic Dishonesty 进一步说明 output-only monitor 可能被“故意给出错误有害答案”绕过。
5. **Agent 需要明确区分 information state、policy state 与 environment state。** LIMI、UserRL、Tree-GRPO、SPEAR、UltraHorizon 和 WoW 分别作用于 sparse demonstration、simulated-user gym、tree rollout、replay buffer、长时 harness 与 embodied world transition，不能被折叠成“增加 agent autonomy”。

未发现本周 owner-date 的 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime 或 OpenXLA 高影响 release；常规 patch 与文档更新不为增加数量而计分。

## Coverage Window and Limitations

- ISO window 已核验为 Monday 2025-09-22 至 Sunday 2025-09-28。
- 归档 owner 使用 official first-public date、GitHub release date 或 arXiv v1 date；Hugging Face recommendation/submission date 只用于 discovery，不能覆盖 v1。
- 逐日 discovery 覆盖 2025-09-22～09-26，并读取 09-29 feed 以捕获 Friday 09-26 才公开、Monday 才进入推荐流的论文；09-27～09-28 无常规 arXiv owner batch。
- Scholar、OpenAlex、DBLP、Semantic Scholar、Crossref 与 Hugging Face 只用于召回、身份和重复关系；技术结论回到 arXiv HTML/PDF、official report、repository 或 release。
- 后续 revision 可用于补足 limitation 与 artifact lineage，但不能倒灌为 v1 当日已披露事实。
- 作者/厂商性能数字均保持在论文 workload contract 内；未披露 model、hardware、precision、length、batch、concurrency 或 SLO 的字段明确记为 `Not Disclosed`。
- Historical Backfill 不创建 Daily；本轮只修改本 Weekly，不修改年度索引、Books、Learning State 或相邻 Weekly。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Google/DeepMind、Meta、Microsoft、NVIDIA、Amazon、Apple、Alibaba/Qwen、DeepSeek、ByteDance、Tencent、Moonshot、MiniMax、Baidu、Zhipu、01.AI、Mistral、Cohere、Hugging Face 及主要研究实验室。

- 保留：Qwen3-Omni Technical Report。
- 版本记录：DeepSeek-V3.1-Terminus；官方只披露 corrective scope，内部训练与 runtime mechanism 未公开。
- 机构论文仍按 arXiv v1 进入学术组，避免公告与论文重复计分。

## 2. 论文与学术来源

### Source Coverage

按 arXiv daily → Hugging Face Daily Papers → Scholar/OpenAlex/DBLP/Semantic Scholar discovery → Crossref metadata 的顺序重放；最终保留 43 个 research families，另有 19 个低分 research families 完成 closure。

- 训练与 post-training：RLPT、RLP、MAPO、VCRL、Thinking Augmented Pre-training、MMR1、CE-GPPO、PromptCoT 2.0、verbal feedback、SPEAR、MNPO、hidden-state RLVR、Q-Tuning、constrained-MDP distillation。
- Context / inference：EpiCache、CompLLM、Sequential DLM、SparseD、d2Cache、SLA、SINQ。
- Multimodal / world / embodied：Video models as zero-shot reasoners、SIM-CoT、ReflectDrive、LongLive、MinerU2.5、WoW、StableToken、HunyuanImage 3.0。
- Agent / evaluation / governance：LIMI、UserRL、Tree-GRPO、UltraHorizon、TrustJudge、Judgment Noise、Strategic Dishonesty、VideoScore2、ToolUniverse、MCPMark、Tool-Light、Rogue Scalpel、ChatInject。
- Multi-model execution：Mixture of Thoughts。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描 official release、RFC、PR 和 design docs。

- 本周无达到计分门槛的 owner-date release。vLLM v0.10.2、SGLang v0.5.2 等属于更早 owner 周；vLLM v0.11.0 属于 W40。
- Qwen3-Omni、LongLive、MinerU2.5 等论文引用的 vLLM/torch.compile/CUDA Graph 只作为论文实现条件，不伪装成相应框架的新 release。

## Candidate Scoring

| # | Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Qwen3-Omni Technical Report | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Must Read |
| 2 | LIMI: Less is More for Agency | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read |
| 3 | EpiCache | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 4 | Strategic Dishonesty | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Must Read |
| 5 | Reinforcement Learning on Pre-Training Data | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read |
| 6 | MAPO | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Read |
| 7 | CompLLM | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Must Read |
| 8 | Video Models Are Zero-Shot Learners and Reasoners | 5 | 4 | 4 | 4 | 4 | 5 | 26/30 | Must Read |
| 9 | SIM-CoT | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Must Read |
| 10 | VCRL | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Read |
| 11 | Thinking Augmented Pre-training | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read |
| 12 | UserRL | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Must Read |
| 13 | When Judgment Becomes Noise | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Must Read |
| 14 | ReflectDrive | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Must Read |
| 15 | Mixture of Thoughts | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Must Read |
| 16 | MMR1 | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Must Read |
| 17 | Tree Search for LLM Agent RL | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 18 | TrustJudge | 5 | 5 | 5 | 5 | 5 | 5 | 30/30 | Must Read |
| 19 | CE-GPPO | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Must Read |
| 20 | LongLive | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 21 | MinerU2.5 | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Must Read |
| 22 | Language Models Can Learn from Verbal Feedback Without Scalar Rewards | 5 | 4 | 4 | 4 | 4 | 5 | 26/30 | Must Read |
| 23 | SPEAR | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Must Read |
| 24 | UltraHorizon | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Must Read |
| 25 | WoW | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Read |
| 26 | PromptCoT 2.0 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 27 | StableToken | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Must Read |
| 28 | Multiplayer Nash Preference Optimization | 4 | 4 | 3 | 4 | 3 | 2 | 20/30 | Read |
| 29 | Sequential Diffusion Language Models | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read |
| 30 | Semantic-Space Exploration and Exploitation in RLVR | 4 | 4 | 3 | 4 | 3 | 2 | 20/30 | Read |
| 31 | ToolUniverse | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 32 | SparseD | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read |
| 33 | HunyuanImage 3.0 Technical Report | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Read |
| 34 | VideoScore2 | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Read |
| 35 | MCPMark | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 36 | Winning the Pruning Gamble / Q-Tuning | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Read |
| 37 | d2Cache | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 38 | SINQ | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read |
| 39 | The Rogue Scalpel | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read |
| 40 | SLA: Sparse-Linear Attention | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read |
| 41 | Tool-Light | 4 | 4 | 4 | 4 | 3 | 3 | 22/30 | Read |
| 42 | Constrained-MDP LLM Distillation | 4 | 4 | 4 | 4 | 3 | 3 | 22/30 | Read |
| 43 | ChatInject | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read |
| 44 | RLP: Reinforcement as a Pretraining Objective | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Must Read |
| 45 | DeepSeek-V3.1-Terminus | 4 | 3 | 3 | 3 | 3 | 3 | 19/30 | Weekly Only |
| 46 | Better Late Than Never | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject |
| 47 | Effective Reasoning Requires Good Demonstrations | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject |
| 48 | Hyper-Bagel | 4 | 3 | 4 | 3 | 3 | 2 | 19/30 | Reject |
| 49 | Soft Tokens, Hard Truths | 4 | 3 | 3 | 4 | 2 | 2 | 18/30 | Reject |
| 50 | Lavida-O | 4 | 3 | 4 | 4 | 2 | 1 | 18/30 | Reject |
| 51 | SimpleFold | 4 | 3 | 4 | 4 | 2 | 2 | 19/30 | Reject |
| 52 | Blueprints of Trust | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Reject |
| 53 | EmbeddingGemma | 3 | 3 | 4 | 5 | 2 | 2 | 19/30 | Weekly Only |
| 54 | Seedream 4.0 | 4 | 3 | 4 | 4 | 2 | 1 | 18/30 | Reject |
| 55 | SciReasoner | 4 | 3 | 4 | 3 | 3 | 2 | 19/30 | Reject |
| 56 | Hunyuan3D-Omni | 4 | 3 | 4 | 4 | 2 | 1 | 18/30 | Reject |
| 57 | Recon-Act | 4 | 4 | 4 | 3 | 2 | 2 | 19/30 | Reject |
| 58 | LayerNorm Induces Recency Bias | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Reject |
| 59 | EPO | 4 | 4 | 3 | 4 | 2 | 2 | 19/30 | Reject |
| 60 | Quantile Advantage Estimation | 4 | 3 | 3 | 4 | 2 | 2 | 18/30 | Reject |
| 61 | Variational Reasoning for Language Models | 4 | 3 | 3 | 4 | 3 | 2 | 19/30 | Reject |
| 62 | VoiceAssistant-Eval | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Reject |
| 63 | StateX | 4 | 3 | 3 | 4 | 2 | 2 | 18/30 | Reject |
| 64 | WebGen-Agent | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Reject |

### Scoring Ledger

- 25～30: 34 rows。
- 20～24: 10 rows。
- <20: 20 rows。
- Retained / Full Source Review: 44 rows。
- Total: 64 rows / 64 unique scoring families。

## Deep Analysis

### 1. Qwen3-Omni：从“多模态输入”到共享时间轴上的并发系统

**Why → Principle.** 早期 multimodal model 把 image/audio encoder 接到 LLM 前端，适合离线理解，却没有解决 streaming input、speech output、absolute timestamp、multi-turn history 与并发的共同状态问题。统一多模态的真正门槛不是 modality 数量，而是不同 token rate、position identity 和生成控制流能否在同一个 lifecycle 中保持一致。

**Mechanism.** Qwen3-Omni 用 Thinker/Talker MoE 分离 text reasoning 与 streaming speech；AuT 把 audio 压到 12.5 Hz；TM-RoPE 用 absolute temporal IDs 对齐 audio/video；Talker 用 multi-codebook + fixed-step MTP 生成 residual codecs，Code2Wav 用 causal ConvNet 从第一 frame 开始输出。Thinker chunk prefill 与 Talker prefill 异步重叠，使“representation architecture”直接进入 TTFT、KV state 和 concurrency contract。

**Trade-off / Evidence.** 作者报告的 234 ms 是特定 cold-start、model、vLLM、torch.compile/CUDA Graph 条件下的 theoretical first-packet latency；并发升高时表中 latency 明显增加。系统以更多 encoder、MoE routing、multi-codebook state、跨模块同步与独立 prompt policy 换取 unified interaction；它不证明所有 modality 无 degradation，也不证明任意 serving backend 可复现。

**Connection / Evolution.** `modality-specific encoder → shared representation → timestamp-aligned stream → split reasoning/speech control → runtime-visible concurrency` 是 direct evolution。文本-only、离线 ASR 或严格确定性 TTS 仍可能选择更小的专用 pipeline。

### 2. EpiCache：从 token eviction 到 episode-owned bounded state

**Why → Principle.** full KV 对短会话最准确，query-aware eviction 对一次问题也合理；但 long conversational QA 同时暴露两个新约束：post-prefill compression 无法限制 prefill peak memory，且当前 query 决定的 eviction 会伤害未来 turn。cache unit 因此必须从“对当前 token 重要”升级为“属于哪段可持续 conversation episode”。

**Mechanism.** EpiCache 在 block-wise prefill 后立刻 eviction，将 peak memory 约束在固定 budget；再将历史按 episode 聚类，每个 episode 保留独立 cache，并按 query 选择 episode；layer sensitivity 决定不同层的 KV budget。episode switch 时才发生主要 retrieval overhead，连续 turn 可摊销切换成本。

**Trade-off / Evidence.** 作者在三套 LongConvQA benchmark、所测模型和 2K～8K cache budget 下报告 accuracy、memory 与 latency，并做 block size、episode count、embedding encoder、RAG-like alternative 等 ablation。该证据不证明 topic clustering 在所有对话中稳定；错误聚类、episode identity drift 和跨层不一致可能把未来需要的信息永久删除。

**Connection / Evolution.** `full KV → query-local eviction → bounded block prefill → episode-owned cache → sensitivity-aware allocation` 是 direct evolution；external RAG 与 KV compression 是 alternative branches，不应互相覆盖。

### 3. Tree-GRPO：从独立完整轨迹到共享前缀的 process credit

**Why → Principle.** group RL 独立采样完整 agent trajectories 时，rollout token/tool-call cost 大量重复；outcome reward 又把同一标量赋给长链每一步。只增加 rollouts 会放大 cost，却不会自动解决 credit assignment。

**Mechanism.** Tree-GRPO 以完整 Thought-Action-Observation 为 node，先并行初始化多棵树，再从非叶节点展开新 branch。共享 prefix 减少重复 rollout，subtree leaves 的 outcome 差异在 branch point 形成 implicit step-level preference；intra-tree 与 inter-tree advantage 分别提供 process signal 与更稳定 baseline。

**Trade-off / Evidence.** 作者在 11 个 single-hop、multi-hop 与 web-agent QA datasets 上比较 chain/tree sampling，报告固定 budget 下更多 rollouts和更高任务结果；理论等价只在 binary preference 等假设下成立。共享 prefix 会降低 exploration breadth，tree scheduler 与 environment snapshot/side effect rollback 也成为新 owner。

**Connection / Evolution.** `independent trajectory → shared-prefix tree → subtree-relative credit → process preference` 是 direct evolution；短任务、便宜环境或无法 snapshot 的 side-effectful workflow 仍适合独立 chain。

## Full Source Review

### 1. Qwen3-Omni Technical Report

- **Candidate / Week / Score / Source Family / Type:** Qwen3-Omni / 2025-W39 / 30/30 / `ARXIV-2509.17765` / official technical report + model/code artifacts。
- **Event / Sources / Access / Full-read:** arXiv v1 2025-09-22；v1 HTML 的 architecture、pretraining、post-training、36 benchmark groups、non-degradation analysis、streaming/concurrency tables 与 appendix 已全文覆盖；official repository/model card 可访问。
- **Problem / Previous / Changed Constraint:** encoder-to-LLM 拼接对离线理解合理；统一 text/image/audio/video、real-time speech、40-minute audio 与 concurrent service 要求共同的 modality/time/state contract。
- **Mechanism / Ownership / Flow / Implementation:** AuT、vision encoder 与 TM-RoPE 负责 aligned representations；Thinker/Talker MoE 分别持有 reasoning/speech generation state；chunked prefill 异步流水，multi-codebook MTP + causal ConvNet 输出 speech。provider 持有 routing/checkpoint，runtime 持有 KV/chunk/batching。
- **Evaluation Contract:** 30B-A3B Thinker、3B-A0.3B Talker、vLLM + torch.compile/CUDA Graph；表中含 1/4/6 concurrency、audio/video theoretical first-packet latency 与 RTF。具体 GPU 型号、完整 precision/batch/SLO 并非全部披露。
- **Proof Boundary / Threats:** 证明作者实现把 multimodal architecture 和 streaming runtime 联结；不证明跨模型普遍无 modality degradation，也不把 vendor SOTA 外推。组件同步、timestamp collision、router imbalance、codec drift 与 policy split 是新增 failure modes。
- **Trade-off / Evolution / Previous Boundary:** 更低 latency 与统一交互换来多模块 state、异步协调和更复杂 regression；text-only/offline pipeline 仍合理。`Layering / Dependency`：representation → temporal alignment → split control → streaming service。
- **ROADMAP / Decision / Questions:** owner `MULTIMODAL-REPRESENTATION` Ch23；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24、`INFER-PREFILL` Ch43、`INFER-SCHEDULING` Ch56。`Books Pending — Integration Deferred`。Open: timestamp/KV identity、partial failure 和 cross-module rollback 如何验证？

### 2. LIMI: Less is More for Agency

- **Candidate / Week / Score / Source Family / Type:** LIMI / 2025-W39 / 25/30 / `ARXIV-2509.17567` / arXiv agent-training research + data/artifact links。
- **Event / Sources / Access / Full-read:** v1 2025-09-22，v2 2025-09-25；method、curation、training recipe、agent benchmarks、comparisons 与 appendix 已核验；later revision 仅补 lineage。
- **Problem / Previous / Changed Constraint:** 大规模 imitation corpus 对 broad instruction following 合理；long-horizon agency 的关键 behavior 可能集中在少量高质量 trajectories，规模扩张会稀释 tool/workflow structure。
- **Mechanism / Ownership / Flow / Implementation:** 精选 demonstrations → SFT agent policy → harness 执行工具 → outcome evaluation。dataset curator 拥有 trajectory quality/provenance，model 拥有 policy，harness 拥有 environment/tool opportunity。
- **Evaluation Contract:** 作者在多套 agent benchmarks 比较 sparse curated training 与更大 baselines；hardware、precision、serving concurrency 与 SLO `Not Disclosed`。结果同时依赖 model、data selection 和 harness。
- **Proof Boundary / Threats:** 证明所测模型可由少量精炼 agent examples 获益；不证明 data quantity 普遍无用，也不证明训练模型拥有 deployment autonomy。selection bias、benchmark overlap 和 curator knowledge 是威胁。
- **Trade-off / Evolution / Previous Boundary:** 少量数据降低训练成本并提高 signal density，却提高单样本错误与覆盖盲区影响；broad-domain pretraining/SFT 仍不可替代。Evolution 为 `Alternative Branch`：broad coverage + sparse high-leverage agency data。
- **ROADMAP / Decision / Questions:** owner `AGENT-WORKFLOW` Ch81，handoff `TRAIN-SFT` Ch29 与 `PLATFORM-EVALUATION-SYSTEM` Ch66。`Emerging / Experimental`。Open: 如何测量 demonstration marginal value、contamination 与 harness transfer？

### 3. EpiCache

- **Candidate / Week / Score / Source Family / Type:** EpiCache / 2025-W39 / 29/30 / `ARXIV-2509.17396` / arXiv systems research + implementation artifact。
- **Event / Sources / Access / Full-read:** v1 2025-09-22，later revisions 至 v4 2026-05-19；v1 method、algorithm、setup、baselines、ablation、efficiency、RAG alternative 与 appendices 已全文核验。
- **Problem / Previous / Changed Constraint:** full KV 准确但线性增长；post-prefill/query-only eviction 无法同时约束 peak memory 并服务未来 turns。LongConvQA 要求固定 budget 与跨 turn topic continuity。
- **Mechanism / Ownership / Flow / Implementation:** block prefill 后即时 eviction；history clustering 形成 episode-owned KV；query 选择 episode，layer sensitivity 分配 budget。runtime 持有 cache blocks，episode index 持有 semantic identity，policy 持有 budget/switch。
- **Evaluation Contract:** 三套 LongConvQA benchmark，延伸至 100K context；比较 full KV、KVzip、InfiniPot 与 RAG-like branch，cache budget 2K～8K，并测最多 10-token answer 的 per-turn latency、peak GPU memory 与 switch overhead。完整生产 concurrency/SLO 未披露。
- **Proof Boundary / Threats:** 证明所测环境中 bounded prefill + episode identity 优于比较项；不证明 clustering 对所有语言/任务稳定。episode drift、embedding error、evicted evidence 不可恢复和 layer budget mismatch 是关键风险。
- **Trade-off / Evolution / Previous Boundary:** memory/latency 下降换来 embedding、clustering、switch 与 irreversible eviction；短 context 或高精度任务仍应 full KV。`Direct Evolution`：token eviction → episode state ownership。
- **ROADMAP / Decision / Questions:** owner `INFER-KV-CACHE` Ch45；handoff `INFER-GPU-MEMORY` Ch54、`AGENT-MEMORY` Ch77。`Books Pending — Integration Deferred`。Open: cache identity、invalidation、rollback 与 RAG/KV 双重 provenance？

### 4. Strategic Dishonesty

- **Candidate / Week / Score / Source Family / Type:** Strategic Dishonesty / 2025-W39 / 29/30 / `ARXIV-2509.18058` / arXiv safety research。
- **Event / Sources / Access / Full-read:** v1 2025-09-22，v2 2025-09-23；EvilMath construction、frontier/open-model evaluation、activation probes、CoT monitors、fine-tuned deception control、limitations 与 appendices 已核验。
- **Problem / Previous / Changed Constraint:** 输出 harmfulness detector 假设危险模型会给出可执行 harmful answer；战略性模型可能故意提供貌似配合但错误的答案，使 output-only evaluation 低估 capability/intent。
- **Mechanism / Ownership / Flow / Implementation:** evaluator 诱导 harmful request 并区分 correctness 与 surface compliance；activation probe 读内部 state，CoT/output monitors 只读文本。provider 拥有 activations，external auditor 通常只有 black-box output。
- **Evaluation Contract:** frontier closed models 用于行为观察，open models 用于 probe；英文 EvilMath 与显式/implicit deception settings。probe/generalization 只在所测开放模型成立，部署 hardware/SLO 不适用。
- **Proof Boundary / Threats:** 证明 output behavior 与 internal intent/capability 可分离；不证明 probe 在 closed frontier models 可用，也不证明 CoT faithful。英文任务、induced deception 和 provider access 限制外推。
- **Trade-off / Evolution / Previous Boundary:** internal monitoring 可能提高检出，却扩大 privileged telemetry、privacy 与 adversarial adaptation 风险；output tests 仍是必要外层。`Layering / Dependency`：capability test → correctness-aware deception test → internal telemetry。
- **ROADMAP / Decision / Questions:** owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `PLATFORM-SECURITY` Ch72、`PLATFORM-TRACE` Ch69。`Books Pending — Integration Deferred`。Open: closed-provider audit、probe drift 与 privacy-preserving evidence？

### 5. Reinforcement Learning on Pre-Training Data

- **Candidate / Week / Score / Source Family / Type:** RLPT / 2025-W39 / 28/30 / `ARXIV-2509.19249` / arXiv training research。
- **Event / Sources / Access / Full-read:** v1 2025-09-23，v2 2025-09-25；objective derivation、data preparation、training variants、evaluation、contamination controls 与 appendix 已核验。
- **Problem / Previous / Changed Constraint:** next-token pretraining 规模大但监督局部；RLVR 能优化 long reasoning，却依赖 narrow verifiable tasks。目标是从原始 pretraining corpus 生成可扩展 RL signal。
- **Mechanism / Ownership / Flow / Implementation:** web text 经 dedup/PII masking/contamination removal 切成 segments；policy 用 autoregressive 或 masked-segment reasoning 预测目标 segment，再与真实 segment 计算 reward。data pipeline 拥有 ground truth，rollout engine 拥有 samples，verifier 拥有 reward。
- **Evaluation Contract:** 以 Qwen3-4B Base 等作者设置在 reasoning/knowledge benchmarks 比较 continued pretraining 与 RLPT variants；hardware、precision、batch/concurrency 与训练成本未完整披露。
- **Proof Boundary / Threats:** 证明 next-segment prediction 可构造无需人工标注的作者实验 RL objective；不证明提升来自 RL 而非额外 tokens/data mixture，也不保证网页 continuation 唯一正确。reward ambiguity、memorization 与 contamination 仍在。
- **Trade-off / Evolution / Previous Boundary:** 扩展 reward coverage 换来昂贵 rollout 与 underspecified verifier；普通 next-token objective 仍是稳定 base。`Alternative Branch`：likelihood learning + self-supervised sequence-level RL。
- **ROADMAP / Decision / Questions:** owner `TRAIN-PRETRAINING` Ch28；handoff `TRAIN-GRPO` Ch33、`TRAIN-DATA` Ch27。`Books Pending — Integration Deferred`。Open: compute-matched baseline、reward ambiguity 与 data governance？

### 6. MAPO

- **Candidate / Week / Score / Source Family / Type:** MAPO / 2025-W39 / 24/30 / `ARXIV-2509.18849` / arXiv RL research。
- **Event / Sources / Access / Full-read:** v1 2025-09-23，v3 2025-09-25；trajectory-certainty analysis、APD/reweight formula、Geo3K/EmoSet experiments、ablation 与 limitations 已读。
- **Problem / Previous / Changed Constraint:** GRPO group standardization 对一般 variance 合理；极高/低 certainty group 会出现 advantage reversion/mirror，固定归一化不再反映样本可学性。
- **Mechanism / Ownership / Flow / Implementation:** rollout reward 分布形成 trajectory certainty；高 certainty 用 advantage percent deviation，动态权重混合不同 advantage。trainer 拥有 group stats/weights，verifier 拥有 reward，policy 不应把 certainty 当 truth。
- **Evaluation Contract:** Qwen2.5-VL-7B、Geo3K 与 EmoSet，group size 8/12；比较 vanilla、GRPO、DAPO 及 ablation。跨 domain、长训练与硬件成本证据有限。
- **Proof Boundary / Threats:** 证明所测数据中动态 advantage 优于固定分支；不证明 certainty proxy 适用于稀疏失败或非 binary reward。论文承认极端失败时可能退化。
- **Trade-off / Evolution / Previous Boundary:** adaptive weighting 提高 signal 利用却增加 hyperparameter 与 feedback loop；reward 分布稳定时 standard GRPO 更简单。`Alternative Branch`。
- **ROADMAP / Decision / Questions:** owner `TRAIN-GRPO` Ch33。`Emerging / Experimental`。Open: reward noise、group size 与 certainty calibration sensitivity？

### 7. CompLLM

- **Candidate / Week / Score / Source Family / Type:** CompLLM / 2025-W39 / 27/30 / `ARXIV-2509.19228` / arXiv context-compression research。
- **Event / Sources / Access / Full-read:** v1 2025-09-23，v2 2026-07-02；v1 compressor architecture、segment reuse、baselines、latency/memory experiments、limitations 与 future work 已核验。
- **Problem / Previous / Changed Constraint:** raw-token context 最精确但 TTFT/KV 线性增长；text deletion 压缩破坏语义且难复用。多 query 长文档需要一次压缩、多次消费。
- **Mechanism / Ownership / Flow / Implementation:** 小 compressor 按 segment 生成 continuous embeddings，冻结 consumer LLM 读取 compressed representation；artifact 可跨 query 复用。compressor/version 拥有 representation identity，registry/cache 拥有 artifact，consumer 拥有 decode state。
- **Evaluation Contract:** Gemma3-4B 等所测 models、长 context QA、2× compression，并与无压缩及 LLMLingua-2 比较；作者报告 TTFT/KV 收益但完整 hardware、batch、concurrency、SLO 并未对全部结果披露。
- **Proof Boundary / Threats:** 证明 semantic QA 中 soft compression 可复用；不适合字符计数、typo 等 structure-sensitive 任务。representation/version drift、cache invalidation 与 lossy evidence 是风险。
- **Trade-off / Evolution / Previous Boundary:** 复用与 memory 收益换来预处理、semantic loss 和 artifact lineage；exact-text 任务必须 bypass。`Alternative Branch`：token pruning vs continuous compression。
- **ROADMAP / Decision / Questions:** owner `AGENT-CONTEXT` Ch75；handoff `INFER-PREFILL` Ch43、`PLATFORM-MODEL-REGISTRY` Ch59。`Books Pending — Integration Deferred`。Open: compressed artifact 的 schema、TTL 和 evidence citation 如何定义？

### 8. Video Models Are Zero-Shot Learners and Reasoners

- **Candidate / Week / Score / Source Family / Type:** Video-model zero-shot reasoning / 2025-W39 / 26/30 / `ARXIV-2509.20328` / arXiv research + project artifacts。
- **Event / Sources / Access / Full-read:** v1 2025-09-24，v2 2025-09-29；v1 formulation、tasks、prompt/video encoding、baselines、analysis 与 appendices 已读；v2 不改变 owner。
- **Problem / Previous / Changed Constraint:** video generator 通常只按 perceptual quality 评估；若生成模型学习 transition dynamics，它可能在不做 task-specific training 时承担 prediction/reasoning，但必须与语言模型能力分开验证。
- **Mechanism / Ownership / Flow / Implementation:** task/state 编码为 visual sequence，video model 生成 future frames/transformations，再由 task decoder 读出 answer。generator 拥有 transition prior，wrapper 拥有 encoding/decoding，benchmark harness 拥有 opportunity。
- **Evaluation Contract:** 多类视觉/状态 transformation tasks 与所测 video models；作者比较 zero-shot baselines 并做 prompt/representation analyses。生成质量 metric 不等于 physical correctness，hardware/SLO 不构成生产结论。
- **Proof Boundary / Threats:** 证明所测 generator 含可利用 transition knowledge；不证明其是 causal world model 或能安全控制真实环境。encoding leakage、decoder bias 与 benchmark construction 可混入能力。
- **Trade-off / Evolution / Previous Boundary:** 复用 generator 减少 task training，却带来高 sampling cost、stochasticity 和难校准 failure；显式 simulator/solver 仍适合可验证任务。`Principle Reuse`。
- **ROADMAP / Decision / Questions:** owner `MULTIMODAL-WORLD-MODELS` Ch25；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66。`Emerging / Experimental`。Open: transition fidelity、controllability 与 causal intervention 如何分离？

### 9. SIM-CoT

- **Candidate / Week / Score / Source Family / Type:** SIM-CoT / 2025-W39 / 26/30 / `ARXIV-2509.20317` / arXiv reasoning research + code。
- **Event / Sources / Access / Full-read:** v1 2025-09-24，v2 2025-09-25；latent-collapse analysis、objective、training-only decoder、GPT-2/Llama experiments、ablation、hyperparameters 与 appendices 已读。
- **Problem / Previous / Changed Constraint:** explicit CoT 可监督但 token 昂贵；implicit latent CoT 更短，却在增加 latent steps 时出现 semantic homogenization 和 training collapse。
- **Mechanism / Ownership / Flow / Implementation:** 每步 last hidden state 作为 latent token；training-only auxiliary decoder 将每个 latent 对齐对应 explicit step，step loss 与 answer loss 联合反传；inference 移除 decoder。
- **Evaluation Contract:** GSM8K-Aug 训练，GSM-Hard/MultiArith/SVAMP OOD，GPT-2 与 Llama 1B/3B/8B；比较 Coconut/CODI/explicit/no-CoT 及 latent-count ablation。任务域集中数学。
- **Proof Boundary / Threats:** 证明 step-level supervision 缓解所测 latent collapse；LM-head projection 不是完整 faithful explanation，也不证明 free-form reasoning 同样成立。
- **Trade-off / Evolution / Previous Boundary:** inference token 少但 training 多一个 decoder 和 explicit-step labels；explicit CoT 仍更可审计。`Direct Evolution`：answer-level → trajectory-level → step-level latent supervision。
- **ROADMAP / Decision / Questions:** owner `MODEL-DECODER-ONLY` Ch18；handoff `TRAIN-SFT` Ch29、`PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: latent semantics 如何跨 task/version 校验？

### 10. VCRL

- **Candidate / Week / Score / Source Family / Type:** VCRL / 2025-W39 / 24/30 / `ARXIV-2509.19803` / arXiv RL research。
- **Event / Sources / Access / Full-read:** v1 2025-09-24；variance curriculum、priority memory bank、objective、five benchmarks、ablation 与 appendices 已核验。
- **Problem / Previous / Changed Constraint:** static curriculum 会随 policy 能力变化而过期；uniform RLVR batches 包含全对/全错的 zero-signal groups。
- **Mechanism / Ownership / Flow / Implementation:** normalized group reward variance 作为当前 policy-relative difficulty；低 variance query 被替换，high-value query 进入 priority replay bank，momentum 与 age 更新 priority。
- **Evaluation Contract:** Qwen3-4B/8B Base，DAPO-Math-17K，5 math benchmarks；batch128、group16、4096 tokens、500 steps、8×H20-3e；比较 GRPO/DAPO/GSPO 并做 ablation。
- **Proof Boundary / Threats:** 证明特定 binary verifier 下 variance 可指导 curriculum；不证明低 variance 总是低价值，持续失败的 hard task 可能被永久排除。
- **Trade-off / Evolution / Previous Boundary:** 提高 gradient density 却增加 rollout-for-selection、replay staleness 与 coverage bias；uniform sampling 仍提供分布覆盖。`Layering / Dependency`。
- **ROADMAP / Decision / Questions:** owner `TRAIN-GRPO` Ch33；handoff `TRAIN-DATA` Ch27。`Emerging / Experimental`。Open: replay freshness 与 rare-hard coverage gate？

### 11. Thinking Augmented Pre-training

- **Candidate / Week / Score / Source Family / Type:** Thinking Augmented Pre-training / 2025-W39 / 28/30 / `ARXIV-2509.20186` / arXiv pretraining research。
- **Event / Sources / Access / Full-read:** v1 2025-09-24，later revisions 至 v4 2025-10-17；data-generation pipeline、training objective、100B-token setup、SFT transfer、ablations 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** raw next-token pretraining 提供答案分布但很少显式计算 trajectory；后训练再补 reasoning 可能太晚且依赖 teacher traces。
- **Mechanism / Ownership / Flow / Implementation:** 为 pretraining text 生成 interleaved thinking trajectories，将 reasoning tokens 与原文共同训练；data generator 持有 derived trace provenance，trainer 持有 mixture/objective，base model 吸收 reasoning prior。
- **Evaluation Contract:** 8B model、100B pretraining tokens，另以 2B-token Mixture-of-Thoughts SFT，比较 vanilla 与公开 models；作者报告多 benchmark 结果，training hardware/energy 与生成成本未完整披露。
- **Proof Boundary / Threats:** 证明所测 scale 下 augmented data 有收益；不证明 thinking text 是 faithful 因果过程，也不能排除额外 token/teacher-quality 作用。
- **Trade-off / Evolution / Previous Boundary:** early reasoning prior 换来昂贵 synthetic generation、style bias 和 provenance burden；raw corpus 仍提供 breadth。`Layering / Dependency`：raw data → derived reasoning data → post-training。
- **ROADMAP / Decision / Questions:** owner `TRAIN-PRETRAINING` Ch28；handoff `TRAIN-DATA` Ch27。`Books Pending — Integration Deferred`。Open: compute-matched 因果、trace 质量与 supersession？

### 12. UserRL

- **Candidate / Week / Score / Source Family / Type:** UserRL / 2025-W39 / 27/30 / `ARXIV-2509.19736` / arXiv interactive-agent RL research。
- **Event / Sources / Access / Full-read:** v1 2025-09-24；gym construction、simulated-user policies、reward variants、SFT cold-start、experiments 与 analysis 已读。
- **Problem / Previous / Changed Constraint:** static QA/SFT 对单回合指令合理；user-centric agent 需要通过多轮 clarification/action 适配隐含目标，训练环境必须生成可响应 user state。
- **Mechanism / Ownership / Flow / Implementation:** simulator 产生 user observations，agent action 改变 dialogue/environment，trajectory 由 turn/goal reward 评分；SFT cold-start 建立最小 interactive policy 后再 RL。
- **Evaluation Contract:** Qwen3 4B/8B、多个 interactive gym setting，比较 reward strategy、不同 simulated users 及有无 SFT cold-start；作者显示 simulator identity 显著影响结果。production latency/SLO 未披露。
- **Proof Boundary / Threats:** 证明所测 simulated-user gym 可训练 interaction behavior；不证明对真人 generalize，simulator 偏差可能被 policy exploit。
- **Trade-off / Evolution / Previous Boundary:** 可规模化 interaction 换来 environment modeling 与 reward hacking；真实 user evaluation 仍必要。`Layering / Dependency`：SFT policy → simulated interaction → RL → human validation。
- **ROADMAP / Decision / Questions:** owner `AGENT-WORKFLOW` Ch81；handoff `TRAIN-GRPO` Ch33、`PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: simulator drift、privacy 与 counterfactual user coverage？

### 13. When Judgment Becomes Noise

- **Candidate / Week / Score / Source Family / Type:** Judgment Noise / 2025-W39 / 29/30 / `ARXIV-2509.20293` / arXiv evaluation-method research。
- **Event / Sources / Access / Full-read:** v1 2025-09-24，v3 2025-10-08；rubric/overall-score decomposition、psychometrics、Arena-Hard-Auto analysis、Elo effect、limitations 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** single judge score 与 Elo 易排序；多 factor rubric 若 overall verdict 不由 factors 解释，aggregation 会隐藏真实 uncertainty。
- **Mechanism / Ownership / Flow / Implementation:** 保存 criterion scores 与 overall judgment，做 linear/polynomial variance decomposition 和 psychometric validity；Elo transformation 被作为可能压平 non-transitive uncertainty 的下游步骤。
- **Evaluation Contract:** 四个 judges、两个 cohorts、Arena-Hard-Auto rubric；作者报告约 55% 平均 unexplained variance。该数字不外推到所有 judge/tasks。
- **Proof Boundary / Threats:** 证明所测 benchmark 的 schema adherence 有严重 gap；不证明某个 judge 本身错误，也不提供真实 gold preference。prompt、cohort 与 factor specification 影响结论。
- **Trade-off / Evolution / Previous Boundary:** richer evidence 提高诊断性但增加 evaluation cost 与 model dependence；简单 score 仍适合低风险粗筛。`Direct Evolution`：verdict → factor evidence → uncertainty-aware aggregation。
- **ROADMAP / Decision / Questions:** owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `PLATFORM-TRACE` Ch69。`Books Pending — Integration Deferred`。Open: rubric coverage 与 human outcome 如何校准？

### 14. ReflectDrive

- **Candidate / Week / Score / Source Family / Type:** ReflectDrive / 2025-W39 / 25/30 / `ARXIV-2509.20109` / arXiv autonomous-driving VLA research。
- **Event / Sources / Access / Full-read:** v1 2025-09-24；action-codebook、discrete diffusion、reflection loop、driving evaluation、ablation 与 limitations 已核验。
- **Problem / Previous / Changed Constraint:** autoregressive trajectory decoding 简单但逐步误差与 latency 累积；continuous diffusion 可全局 refine 却难直接复用 language-model infrastructure。
- **Mechanism / Ownership / Flow / Implementation:** 2D trajectory 离散为 action codebook；diffusion LM 并行 denoise candidate actions，并以 safety-aware reflection 迭代修正。planner 持有 proposal state，verifier 持有 risk feedback，controller/environment 持有真实 transition。
- **Evaluation Contract:** 作者在 autonomous-driving datasets/simulated metrics 比较 AR 与 diffusion branches；真实车辆 control frequency、hardware、end-to-end latency 与 safety SLO 不完整。
- **Proof Boundary / Threats:** 证明离散 action + diffusion 在所测 planner 任务可行；不证明 physical closed-loop safety。codebook quantization、reflection latency 与 distribution shift 是风险。
- **Trade-off / Evolution / Previous Boundary:** parallel correction 换来 iterative compute 和 non-causal commit；real-time low-level control 仍需 bounded controller。`Alternative Branch`。
- **ROADMAP / Decision / Questions:** owner `MULTIMODAL-EMBODIED-VLA` Ch26；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。`Emerging / Experimental`。Open: commit/rollback 与 controller deadline？

### 15. Mixture of Thoughts

- **Candidate / Week / Score / Source Family / Type:** Mixture of Thoughts / 2025-W39 / 25/30 / `ARXIV-2509.21164` / arXiv multi-model execution research。
- **Event / Sources / Access / Full-read:** v1 2025-09-25；router、primary/expert interaction layers、training objective、ID/OOD evaluation、cost comparison、ablations 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** single-model routing 省 compute 但不协作；output ensemble 可协作却多次 decode 昂贵；weight fusion 要求 architecture 同构并固化 specialization。
- **Mechanism / Ownership / Flow / Implementation:** global router 选 top-K heterogeneous frozen experts 和 primary；projectors/cross-attention 把 peer hidden states 写入 primary latent flow，一次 forward 后由 primary decode。
- **Evaluation Contract:** language/code/math ID/OOD tasks，比较 routing、output collaboration 与 fusion；作者报告 wall-clock 接近 routing baseline。hardware、memory footprint、batch/concurrency/SLO 不完整。
- **Proof Boundary / Threats:** 证明所测 open experts 可 latent collaborate；不证明任意 architecture/tokenizer/state 可兼容，hidden interface 也是强 coupling。
- **Trade-off / Evolution / Previous Boundary:** single-pass 协作降低 multi-turn decode，但增加多模型驻留、projection schema、failure correlation 与版本耦合；routing-only 在资源紧张时仍合理。`Alternative Branch`。
- **ROADMAP / Decision / Questions:** owner `INFER-SCHEDULING` Ch56；handoff `MODEL-MOE` Ch21、`AGENT-MULTI-AGENT` Ch82。`Emerging / Experimental`。Open: expert version、hidden schema 与 partial failure？

### 16. MMR1

- **Candidate / Week / Score / Source Family / Type:** MMR1 / 2025-W39 / 27/30 / `ARXIV-2509.21268` / arXiv multimodal-RL research + open resources。
- **Event / Sources / Access / Full-read:** v1 2025-09-25；variance-progress theory、VPS/OVS/TDS、data construction、1.6M CoT + 15K RL set、training/evaluation/ablation 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** uniform prompt sampling 在 GRPO 中常产生 all-correct/all-wrong groups，multimodal reasoning 又使 trajectory diversity 难由 outcome alone 表达。
- **Mechanism / Ownership / Flow / Implementation:** variance promotion score 组合 outcome variance 与 trajectory diversity；batch 一部分按 VPS 采样、一部分 uniform 保 coverage。sampler 拥有 curriculum，verifier 拥有 outcome，embedding/trace metric 拥有 diversity。
- **Evaluation Contract:** 作者在 multimodal math/reasoning models 和 benchmarks 比较 sampling baselines，并提供 theory/ablation；硬件与 fleet SLO 不构成通用结论。
- **Proof Boundary / Threats:** 理论给 reward variance 与 expected gradient magnitude 下界关系；不证明高 variance 总产生正确方向，trajectory metric 可能奖励表面差异。
- **Trade-off / Evolution / Previous Boundary:** informative gradients 换来额外 rollout/scoring 与 sampling bias；uniform branch 仍保留。`Layering / Dependency`。
- **ROADMAP / Decision / Questions:** owner `TRAIN-GRPO` Ch33；handoff `MULTIMODAL-REPRESENTATION` Ch23。`Books Pending — Integration Deferred`。Open: verifier noise 如何传播到 VPS？

### 17. Tree Search for LLM Agent RL

- **Candidate / Week / Score / Source Family / Type:** Tree-GRPO / 2025-W39 / 29/30 / `ARXIV-2509.21240` / arXiv agent-RL research + code。
- **Event / Sources / Access / Full-read:** v1 2025-09-25，later revisions 至 v3 2026-03-18；v1 MDP、tree rollout、advantage derivation、11-dataset setup、tree-structure sensitivity、algorithm 与 appendices 已读。
- **Problem / Previous / Changed Constraint:** independent chain rollout 对短任务合理；long multi-turn agent 重复 prefix 并只收 outcome reward，token/tool cost 和 credit sparsity 同时恶化。
- **Mechanism / Ownership / Flow / Implementation:** Thought-Action-Observation 作为 node；initialize-then-expand 构造 shared-prefix trees；leaf rewards 回传形成 intra/inter-tree advantage 和 implicit step preference。orchestrator 必须 snapshot context/environment side effects。
- **Evaluation Contract:** 11 个 single-hop/multi-hop/web-agent QA datasets，多 model/scale；固定 token/tool budget 比较 chain/tree 并分析 tree levels/structures。真实收费 API、并发 scheduler 与 side-effect rollback 未完整覆盖。
- **Proof Boundary / Threats:** 证明所测 harness 中共享 prefix 提高 sample efficiency；理论等价依赖 binary preference 等假设。prefix correlation、exploration narrowing 与 baseline variance 限制外推。
- **Trade-off / Evolution / Previous Boundary:** rollout 复用和 process signal 换来 tree state、snapshot 与 complex scheduling；不可回放环境仍适合 independent trajectory。`Direct Evolution`。
- **ROADMAP / Decision / Questions:** owner `TRAIN-GRPO` Ch33；handoff `AGENT-WORKFLOW` Ch81、`AGENT-PLATFORM` Ch84。`Books Pending — Integration Deferred`。Open: tool side effects 怎样 fork/rollback？

### 18. TrustJudge

- **Candidate / Week / Score / Source Family / Type:** TrustJudge / 2025-W39 / 30/30 / `ARXIV-2509.21117` / arXiv evaluation research。
- **Event / Sources / Access / Full-read:** v1 2025-09-25，v2 2025-09-26；score granularity、probabilistic judgment、pairwise cycles、likelihood aggregation、experiments、ablation 与 appendix 已核验。
- **Problem / Previous / Changed Constraint:** deterministic score/pairwise vote 易部署；judge 本身有 distribution，rounding/tie 会制造 score-comparison conflict 和 transitivity violation。
- **Mechanism / Ownership / Flow / Implementation:** 提高 score granularity 或保留 token likelihood distribution；pairwise aggregation 用 likelihood 而非 hard tie。judge 产生 evidence distribution，aggregator 形成 decision，release gate 持有 operating point。
- **Evaluation Contract:** Llama-3.1-70B 等 judge、1,200 instructions、multiple rounds 与 pairwise tests；比较 5/10/100-point 和 probabilistic variants。API logprob availability 与 model family 影响可用性。
- **Proof Boundary / Threats:** 证明 hard verdict 丢失可测 uncertainty；不证明 likelihood 已校准为 truth probability，也不解决 rubric validity。
- **Trade-off / Evolution / Previous Boundary:** consistency 提高但需 logprobs、更多 storage/compute 和 calibration；hard score 仍可作 cheap filter。`Direct Evolution`：hard judge → distribution-aware evidence → gated decision。
- **ROADMAP / Decision / Questions:** owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `PLATFORM-TRACE` Ch69。`Books Pending — Integration Deferred`。Open: likelihood calibration、judge correlation 与 human anchor？

### 19. CE-GPPO

- **Candidate / Week / Score / Source Family / Type:** CE-GPPO / 2025-W39 / 26/30 / `ARXIV-2509.20712` / arXiv RL optimization research。
- **Event / Sources / Access / Full-read:** v1 2025-09-25，later revisions 至 v5 2026-04-23；clipped-token gradient analysis、objective、entropy dynamics、benchmarks、ablation 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** PPO/GRPO clipping 限制 policy drift 合理；被 clip tokens 梯度归零会系统性改变 entropy dynamics，长 reasoning 训练可能 collapse。
- **Mechanism / Ownership / Flow / Implementation:** 对 clipped tokens 保留 bounded gradient component 并控制 entropy，而非简单取消 clip。optimizer 持有 ratio/clip state，monitor 持有 entropy/gradient telemetry，policy trainer 持有 rollback。
- **Evaluation Contract:** 作者在所测 reasoning models/benchmarks 比较 GRPO variants 并跟踪 entropy、performance 和 clipped ratios；跨 scale/hardware 稳定性仍有限。
- **Proof Boundary / Threats:** 证明作者设置中 clipped gradients 与 entropy 相关且保留梯度可改善训练；不证明 entropy 越高越好。额外 coefficient、gradient bias 和 reward interaction 是风险。
- **Trade-off / Evolution / Previous Boundary:** 减少 zero-gradient region 却弱化 trust-region 直观；稳定任务仍可用 standard clipping。`Direct Evolution`：hard clip → gradient-preserving clip + entropy control。
- **ROADMAP / Decision / Questions:** owner `TRAIN-PPO` Ch32；handoff `TRAIN-GRPO` Ch33、`PLATFORM-MONITORING` Ch67。`Books Pending — Integration Deferred`。Open: gradient/entropy release gate 如何定义？

### 20. LongLive

- **Candidate / Week / Score / Source Family / Type:** LongLive / 2025-W39 / 29/30 / `ARXIV-2509.22622` / arXiv generative-systems research + code/model。
- **Event / Sources / Access / Full-read:** v1 2025-09-26；architecture、KV-recache、streaming-long tuning、window/sink attention、VBench、INT8、latency/quality analyses 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** diffusion/bidirectional attention 质量高但低效；causal video 支持 KV cache，却在长时一致性与 mid-stream prompt change 时产生 stale state。
- **Mechanism / Ownership / Flow / Implementation:** frame-level AR、short-window attention + frame sink 控制 history；prompt 改变触发 KV-recache；streaming-long tuning 对齐 train/test。prompt version 拥有 control identity，KV state 拥有 derived history，renderer 负责 frame commit。
- **Evaluation Contract:** 1.3B model、32 GPU-days fine-tuning、single H100、20.7 FPS、最长 240s、INT8 2.7GB→1.4GB，VBench 比较。作者结果不等于任意 resolution/quality/SLO。
- **Proof Boundary / Threats:** 证明该特定 model 可 real-time interactive long generation；不证明 world consistency 或 physical causality。recache cost、prompt race、sink bias 与 long drift 是风险。
- **Trade-off / Evolution / Previous Boundary:** causal streaming 与 cache 换来 window truncation 和 state invalidation；offline high-quality generation 仍可用 bidirectional diffusion。`Direct Evolution`。
- **ROADMAP / Decision / Questions:** owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；handoff `MULTIMODAL-WORLD-MODELS` Ch25、`INFER-KV-CACHE` Ch45。`Books Pending — Integration Deferred`。Open: prompt version 与 KV recache atomicity？

### 21. MinerU2.5

- **Candidate / Week / Score / Source Family / Type:** MinerU2.5 / 2025-W39 / 25/30 / `ARXIV-2509.22186` / arXiv VLM systems research + code/model。
- **Event / Sources / Access / Full-read:** v1 2025-09-26；model architecture、two-stage parsing、three-stage training、data engine、offline vLLM pipeline、benchmarks、ablations、prompts 与 appendices 已读。
- **Problem / Previous / Changed Constraint:** full-resolution end-to-end VLM 保 detail 但 blank regions 浪费 tokens；cropping 省 compute 却丢 global layout。
- **Mechanism / Ownership / Flow / Implementation:** downsampled page 先做 global layout，按 region 回到 native-resolution crops 识别；async backend 批量 page requests 并重叠 CPU/GPU。layout stage 拥有 region identity，crop stage 拥有 content，assembler 持有 reading order。
- **Evaluation Contract:** 1.2B model，多 document parsing/OCR benchmark，与 general/domain systems 比较；offline pipeline 基于 vLLM。完整 hardware、precision、concurrency 和 online SLO 未统一披露。
- **Proof Boundary / Threats:** 证明 coarse-to-fine 在所测 documents 节省冗余并保持 accuracy；不证明任意 layout/language 成立。region miss 会不可恢复地丢内容，assembler 错误传播。
- **Trade-off / Evolution / Previous Boundary:** token 效率换来两阶段 latency、crop scheduling 与 identity；简单低分辨率页面可 end-to-end。`Direct Evolution`：global parse → targeted recognition。
- **ROADMAP / Decision / Questions:** owner `MULTIMODAL-REPRESENTATION` Ch23；handoff `INFER-SCHEDULING` Ch56。`Emerging / Experimental`。Open: region recall 与 end-to-end evidence provenance？

### 22. Language Models Can Learn from Verbal Feedback Without Scalar Rewards

- **Candidate / Week / Score / Source Family / Type:** Feedback-Conditioned Policy / 2025-W39 / 26/30 / `ARXIV-2509.22638` / arXiv post-training research。
- **Event / Sources / Access / Full-read:** v1 2025-09-26；feedback-conditioned objective、offline/online bootstrap、shared feedback source、RFT/GRPO baselines、five math benchmarks、analysis 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** scalar reward 压缩 review nuance 且依赖 stable verifier；自然语言 feedback 更丰富但难直接变成 policy gradient。
- **Mechanism / Ownership / Flow / Implementation:** reviewer 生成 verbal condition，policy 在 prompt/response/feedback 上做 cross-entropy 更新；bootstrap 反复生成新 responses 和 fresh feedback。feedback artifact 拥有 text/provenance，trainer 拥有 conditioning，judge 同时提供 scalar baseline 以做公平比较。
- **Evaluation Contract:** base model 每 prompt 8 candidates，GPT-5-nano 反馈，比较 RFT/GRPO 与 FCP+bootstrap，五个 math benchmarks/中间 checkpoints；结果依赖 reviewer 且非 human feedback 通用结论。
- **Proof Boundary / Threats:** 证明所测 setting 无需直接优化 scalar 也可接近 baselines；不证明 verbal feedback 更 truthful，reviewer 可产生 style shortcut 或 self-confirmation。
- **Trade-off / Evolution / Previous Boundary:** 保留信息密度却增加 feedback tokens、teacher cost 和 prompt injection surface；verifiable scalar 在数学/代码仍高效。`Alternative Branch`。
- **ROADMAP / Decision / Questions:** owner `TRAIN-RLHF` Ch31；handoff `TRAIN-SFT` Ch29、`PLATFORM-EVALUATION-SYSTEM` Ch66。`Books Pending — Integration Deferred`。Open: feedback provenance 与 anti-reward-hacking verifier？

### 23. SPEAR

- **Candidate / Week / Score / Source Family / Type:** SPEAR / 2025-W39 / 26/30 / `ARXIV-2509.22601` / arXiv agent-RL research + code/checkpoints。
- **Event / Sources / Access / Full-read:** v1 2025-09-26；curriculum、intrinsic reward、self-imitation buffer、advantage recalibration、covariance clipping、benchmarks、hyperparameter sensitivity、cost analysis 与 algorithm appendix 已读。
- **Problem / Previous / Changed Constraint:** entropy bonus 鼓励探索但 long-horizon、multi-turn feedback distribution shift 会造成 runaway entropy；直接 exploitation 又会早熟收敛。
- **Mechanism / Ownership / Flow / Implementation:** early intrinsic tool-use reward 扩展 skill exposure，随后衰减；promising trajectories 进入 replay buffer 做 off-policy self-imitation；advantage recalibration 与 covariance clipping 抑制 policy drift/overconfidence。
- **Evaluation Contract:** WebShop、search/agent tasks、Qwen2.5 等 settings，对比 GRPO-like baselines；报告 buffer size、warm-up/decay、clipping 等 sensitivity。环境和 judge 限制跨域外推。
- **Proof Boundary / Threats:** 证明所测 harness 中 progressive exploration 优于固定 entropy；不证明 buffer trajectory 持续正确。stale experience、reward hacking 和 coverage collapse 是风险。
- **Trade-off / Evolution / Previous Boundary:** experience reuse 降低探索浪费却增加 off-policy bias、buffer governance 和 reset policy；短任务仍可 on-policy。`Direct Evolution`：entropy exploration → staged exploration → governed replay。
- **ROADMAP / Decision / Questions:** owner `TRAIN-GRPO` Ch33；handoff `AGENT-MEMORY` Ch77、`AGENT-WORKFLOW` Ch81。`Books Pending — Integration Deferred`。Open: replay provenance/supersession 和 environment version？

### 24. UltraHorizon

- **Candidate / Week / Score / Source Family / Type:** UltraHorizon / 2025-W39 / 26/30 / `ARXIV-2509.21766` / arXiv agent-evaluation benchmark + harness。
- **Event / Sources / Access / Full-read:** v1 2025-09-25；scenario construction、long-horizon harness、capability dimensions、models、metrics、failure analysis 与 appendix 已读。
- **Problem / Previous / Changed Constraint:** short-turn benchmark 低成本且可复现；ultra-long tasks 暴露 context growth、error accumulation、recovery 和 goal drift，单一 final score 无法定位失败。
- **Mechanism / Ownership / Flow / Implementation:** harness 维护 environment/task state 和 long action trace，按阶段 milestones 与 final outcome 评估；agent 只拥有 policy/context，不能把 environment opportunity 记作 model capability。
- **Evaluation Contract:** 多类 long-horizon scenarios 和 frontier/open agents；作者报告完成率与过程行为。tool reliability、time budget、retry policy 与 judge 共同影响结果，不能跨 harness 比较。
- **Proof Boundary / Threats:** 证明短评测会遗漏长时 failure；不证明 benchmark 即 deployment autonomy。environment leakage、nondeterminism、cost censoring 与 survivorship bias 存在。
- **Trade-off / Evolution / Previous Boundary:** 真实性提高但成本、variance、replay 难度上升；short benchmark 仍适合 unit regression。`Layering / Dependency`：unit eval → workflow eval → long-horizon reliability。
- **ROADMAP / Decision / Questions:** owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `AGENT-PLATFORM` Ch84。`Books Pending — Integration Deferred`。Open: time/cost censoring 与 checkpoint recovery 如何标准化？

### 25. WoW

- **Candidate / Week / Score / Source Family / Type:** WoW / 2025-W39 / 24/30 / `ARXIV-2509.22642` / arXiv embodied world-model research。
- **Event / Sources / Access / Full-read:** v1 2025-09-26；embodied-interaction data、model architecture、training stages、world/agent evaluations、ablations 与 appendices 已读。
- **Problem / Previous / Changed Constraint:** passive video pretraining 提供 appearance/dynamics prior，却缺 action-conditioned intervention 与 embodiment-specific feedback。
- **Mechanism / Ownership / Flow / Implementation:** embodied agent 执行 action，environment 返回 observation，model 从 interaction trajectories 学习 transition/scene representation；dataset 拥有 sensor/action schema，world model 拥有 latent dynamics，policy/controller 拥有 action authority。
- **Evaluation Contract:** 作者在所建 embodied tasks 和 world-model metrics 比较 baselines；simulator/real-world mix、hardware、control frequency 与 safety envelope 限制通用结论。
- **Proof Boundary / Threats:** 证明 interaction data 在所测任务提升 world representation；不证明“omniscient”或真实因果完备。coverage、sim bias 和 policy-induced data bias 是风险。
- **Trade-off / Evolution / Previous Boundary:** active data 提高 controllability 却昂贵且带 safety/selection bias；passive video 仍适合 breadth。`Direct Evolution`：observation prediction → action-conditioned interaction。
- **ROADMAP / Decision / Questions:** owner `MULTIMODAL-WORLD-MODELS` Ch25；handoff `MULTIMODAL-EMBODIED-VLA` Ch26。`Emerging / Experimental`。Open: persistent state revision 与 sim-to-real evidence？

### 26. PromptCoT 2.0

- **Candidate / Week / Score / Source Family / Type:** PromptCoT 2.0 / 2025-W39 / 29/30 / `ARXIV-2509.19894` / arXiv data/training research + code/data/models。
- **Event / Sources / Access / Full-read:** v1 2025-09-24；variational formulation、cold start、EM loop、self-play/SFT branches、six benchmarks、baselines、ablations、scaling/distribution/difficulty analyses 与 proof appendix 已读。
- **Problem / Previous / Changed Constraint:** human prompts 质量高但稀缺；one-shot synthetic prompts 依赖 hand-crafted heuristic 且容易太简单。强 reasoner 又可能没有更强 teacher 可蒸馏。
- **Mechanism / Ownership / Flow / Implementation:** concept-rationale-problem triples 初始化 rationale/prompt models；E-step 从 8 个 rationales 选高 joint-likelihood 项，M-step 更新 prompt generator；强 model 用 verifiable self-play，弱 model 走 teacher SFT。
- **Evaluation Contract:** Qwen3-4B/30B-A3B self-play、Qwen2.5-7B SFT；AIME/HMMT/LiveCodeBench/Codeforces，math avg@16、code pass@1，公开 4.8M prompts 与 artifacts。teacher/data-generation compute 未完整计入。
- **Proof Boundary / Threats:** 证明所测 math/code pipeline 产生更难分布并提升作者 models；不证明 domain-agnostic，也不能排除 benchmark-specific synthesis/contamination。
- **Trade-off / Evolution / Previous Boundary:** scalable task generation 换来 generator feedback loop、verification scope 和 provenance 成本；human-curated anchor 仍需保留。`Direct Evolution`：heuristic synthesis → rationale-mediated synthesis → EM self-improvement。
- **ROADMAP / Decision / Questions:** owner `TRAIN-DATA` Ch27；handoff `TRAIN-SFT` Ch29、`TRAIN-GRPO` Ch33。`Books Pending — Integration Deferred`。Open: generator collapse、contamination 与 task lineage？

### 27. StableToken

- **Identity / Event / Coverage:** 25/30，`ARXIV-2509.22220`；v1 2025-09-26。v1 architecture、Voting-LFQ、noise-aware consensus objective、ASR/SER/TTS setup、voter/perturbation ablation、efficiency、long-audio boundary 与 appendix 已读；v2 只补 revision lineage。
- **Problem → Mechanism / Ownership:** 单路径 speech quantizer 在量化边界会把轻微噪声放大为 token jump；多分支 LFQ 以 bit-wise vote 形成稳定 code，clean-majority/noisy-minority views 和 consensus loss 把 invariance 监督推到中间表示。tokenizer/version 持有 speech-token identity，downstream SpeechLLM 只消费 codes。
- **Evaluation / Boundary:** Whisper-large-v3 backbone、150k-hour corpus、25 Hz/8192-code vocabulary、FLEURS/LibriSpeech/CHiME-4/ESD/SEED-TTS，并与 SSL/distilled/supervised tokenizer 比较；作者结果不证明真实噪声与所有语言都稳定，也不证明 multi-branch 在任意 accelerator 上零成本。
- **Trade-off / Failure / Previous Boundary:** robustness 换来分支投影、consensus training 和 codebook/version migration；短、干净、离线 speech 仍可用单路径 tokenizer。新增 voter correlation、boundary drift 与 downstream code incompatibility。
- **ROADMAP / Decision:** owner `MULTIMODAL-REPRESENTATION` Ch23；handoff `INFER-PREFILL` Ch43。`Books Pending — Integration Deferred`。

### 28. Multiplayer Nash Preference Optimization

- **Identity / Event / Coverage:** 20/30，`ARXIV-2509.23102`；v1 2025-09-27。v1 n-player game、mirror-descent objective、equilibrium proof、instruction-following experiments、heterogeneous-annotator analysis 与 limitations 已读；2026 revisions 不倒灌。
- **Problem → Mechanism / Ownership:** scalar/Bradley–Terry preference 与 two-player Nash 对异质、非传递偏好只建一个对手；MNPO 让 policy 面向 opponent population，同时由 reference regularization 约束。trainer 持有 player population/reference snapshot，annotator model 持有 comparison distribution。
- **Evaluation / Boundary:** 论文在所测 instruction-following datasets 与 mixed-policy/heterogeneous settings 比较 NLHF baselines；hardware、precision、batch 与 wall-clock `Not Disclosed`。结果不证明真实用户偏好天然是稳定 n-player game。
- **Trade-off / Failure / Previous Boundary:** coverage 增强换来多策略采样、equilibrium approximation 与 population staleness；偏好近似传递时 DPO/two-player branch 更简单。
- **ROADMAP / Decision:** owner `TRAIN-RLHF` Ch31；handoff `AGENT-MULTI-AGENT` Ch82。`Emerging / Experimental`。

### 29. Sequential Diffusion Language Models

- **Identity / Event / Coverage:** 28/30，`ARXIV-2509.24007`；v1 2025-09-28。NSP factorization、parallel block training、dynamic selection/self-speculation、speed-quality curve、block-size ablation 与 training appendix 已读。
- **Problem → Mechanism / Ownership:** AR 每步一 token 串行但 KV 可复用；full/block diffusion 并行却固定长度且训练昂贵。NSP 把 next-token 与 next-block 统一为可变长 next-sequence，block 内 diffusion，confidence/verification 决定 commit 长度，从 pretrained AR retrofit 并保留 prefix KV。
- **Evaluation / Boundary:** SDLM-3B/32B、Qwen-2.5 retrofit、3.5M samples，比较 AR/DLM/block-diffusion，报告吞吐与多 benchmark；作者 2.1× 只属于其 model/hardware/decoding contract，完整 concurrency/SLO 未披露。
- **Trade-off / Failure / Previous Boundary:** 并行 commit 换来 confidence calibration、block rollback 与 approximate generation；不确定性高或 exact-token contract 下 length=1 退化为 AR 仍合理。
- **ROADMAP / Decision:** owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；handoff `INFER-SPECULATIVE-DECODING` Ch48、`INFER-KV-CACHE` Ch45。`Books Pending — Integration Deferred`。

### 30. Semantic-Space Exploration and Exploitation in RLVR

- **Identity / Event / Coverage:** 20/30，`ARXIV-2509.23808`；v1 2025-09-28。ER/ERV/ERA 定义、advantage shaping、meta-control、跨 model/RL algorithm experiments、ablation 与 limitations 已读。
- **Problem → Mechanism / Ownership:** token entropy 把下一 token uncertainty 错当 trajectory-level exploration；论文在 hidden-state trajectory 上以 effective rank 测 semantic coverage、velocity 测 refinement、acceleration 调节两者，再把信号注入 RLVR advantage。trainer 需要 privileged activations。
- **Evaluation / Boundary:** 多 base models、RLVR algorithms 与 reasoning benchmarks；结果含 Gaokao 等作者实验，但 effective rank 不是可解释 reasoning truth，closed API 无法取得同等 telemetry。
- **Trade-off / Failure / Previous Boundary:** richer signal 换来 activation storage、rank estimation 与 representation drift；仅能访问 tokens/rewards 时 entropy proxy 仍可用。跨 checkpoint 比较 hidden basis 是新 failure mode。
- **ROADMAP / Decision:** owner `TRAIN-GRPO` Ch33；handoff `PLATFORM-TRACE` Ch69。`Emerging / Experimental`。

### 31. ToolUniverse

- **Identity / Event / Coverage:** 29/30，`ARXIV-2509.23426`；v1 2025-09-27。protocol/schema、2,700+ tools、130+ skills、interface refinement/discovery、versioning/audit/governance、case studies 与 supplementary evaluation 已读；artifact v1.3.1 可追踪。
- **Problem → Mechanism / Ownership:** bespoke AI-scientist workflow 把 tool semantics、backend 与 domain glue 写死；统一 natural-language purpose、typed I/O schema、backend-neutral invocation、tests 和 versioned registry，再由 skills 编排。registry 持有 tool identity/schema/version，workflow 持有 state，human reviewer 持有 consequential approval。
- **Evaluation / Boundary:** scientific case studies、live services、tool conformance/trace review；不是随机对照的 autonomous discovery proof，也不证明 2,700 个 tool 质量同等。外部 API freshness、data license 与 hidden side effects 仍限制复现。
- **Trade-off / Failure / Previous Boundary:** extensibility 换来 schema drift、dependency supply chain、credential/governance 与 live-data nondeterminism；小而稳定的单领域 pipeline 仍可能优于开放 registry。
- **ROADMAP / Decision:** owner `AGENT-TOOL-CALLING` Ch78；handoff `AGENT-MCP` Ch83、`AGENT-WORKFLOW` Ch81、`PLATFORM-SECURITY` Ch72。`Books Pending — Integration Deferred`。

### 32. SparseD

- **Identity / Event / Coverage:** 28/30，`ARXIV-2509.24014`；v1 2025-09-28。head/time attention analysis、isolated selection、pattern reuse/skipping、Dream/LLaDA setup、latency、quality、ratio ablations 与 limitations 已读。
- **Problem → Mechanism / Ownership:** AR sparse pattern 不能直接移植到 iterative dLLM；SparseD 在 early steps 用 full attention 建 head-specific pattern，后续 denoising 复用，并对 prefill/generation tokens 分开选择，避免重要 generation state 被淹没。
- **Evaluation / Boundary:** Dream-7B-Instruct、LLaDA-1.5、最长 64K/1,024 steps，与 FlashAttention/稀疏 baselines 比较；1.50× 是论文限定 contract，不是所有 dLLM/length 的通用速度。
- **Trade-off / Failure / Previous Boundary:** 省 attention FLOPs 换来 early-step overhead、pattern staleness 与 quality threshold；短 context、少 step 时 full attention 更合理。
- **ROADMAP / Decision:** owner `INFER-VLLM` Ch50；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。`Books Pending — Integration Deferred`。

### 33. HunyuanImage 3.0 Technical Report

- **Identity / Event / Coverage:** 23/30，`ARXIV-2509.23951`；v1 2025-09-28。data filtering/captioning、native AR multimodal architecture、80B/13B-active MoE、progressive training/post-training、inference 与 human/automatic evaluation 已读。
- **Problem → Mechanism / Ownership:** separated understanding/generation pipelines 对专用任务合理，却难共享 semantic state；该模型把 text/image token 与 reasoning schema置于 AR MoE 中，并以 staged data/training 支持 image generation。model artifact 持有 representation/router contract，runtime 持有 active-expert execution。
- **Evaluation / Boundary:** 近 5B filtered images、作者 automatic/human comparison 与 open weights；vendor benchmark 不证明通用优越，训练 hardware、完整 precision/cost/concurrency 未全部公开。
- **Trade-off / Failure / Previous Boundary:** unified state 换来 MoE placement、巨大 data governance 和 autoregressive image latency；专用 diffusion pipeline 仍是 alternative branch。
- **ROADMAP / Decision:** owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；handoff `MODEL-MOE` Ch21。`Emerging / Experimental`。

### 34. VideoScore2

- **Identity / Event / Coverage:** 23/30，`ARXIV-2509.22799`；v1 2025-09-26。VideoFeedback2 construction、three-dimensional rubric、SFT→GRPO、in/out-domain suites、Best-of-N、fps/LR/step/inference ablations 与 appendix 已读。
- **Problem → Mechanism / Ownership:** single opaque video reward 混合 visual quality、alignment 与 physical consistency；模型先生成 rationale 再分维度打分，27,168 human-annotated videos 提供 score/reasoning traces。dataset/rubric version 持有 label identity，evaluator 持有 uncertain judgment。
- **Evaluation / Boundary:** 22 T2V sources、in-domain VideoScore-Bench-v2 与四个 OOD suites；作者 accuracy 不等于 calibrated correctness，CoT 不保证 faithful，reward 用于 Best-of-N 可能放大 evaluator bias。
- **Trade-off / Failure / Previous Boundary:** interpretability/coverage 换来高标注成本、rationale leakage 与 reward hacking；简单可测 artifact 仍应使用 executable metric。
- **ROADMAP / Decision:** owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `MULTIMODAL-WORLD-MODELS` Ch25。`Emerging / Experimental`。

### 35. MCPMark

- **Identity / Event / Coverage:** 29/30，`ARXIV-2509.24002`；v1 2025-09-28。127-task construction、initial-state fixtures、programmatic verifier、minimal agent loop、CRUD environments、pass@1/pass^4 与 failure analysis 已读。
- **Problem → Mechanism / Ownership:** read-heavy/LLM-judge MCP benchmarks 无法代表长 CRUD workflow；MCPMark 为每项任务固定 initial state 和 executable verifier，让 harness 分离 model decision、tool opportunity 与 artifact correctness。
- **Evaluation / Boundary:** Filesystem/GitHub/Notion/PostgreSQL/Playwright 等 environments，平均 16.2 turns/17.4 tool calls；closed-model scores 只属于当时 provider/harness，不等于 deployment autonomy。remote service simulation fidelity 是显式限制。
- **Trade-off / Failure / Previous Boundary:** executable verification 提高可信度，却增加 fixture maintenance、credential/sandbox、environment freshness 与 verifier blind spot；开放式质量仍需 human/semantic judge。
- **ROADMAP / Decision:** owner `AGENT-MCP` Ch83；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66、`AGENT-WORKFLOW` Ch81。`Books Pending — Integration Deferred`。

### 36. Winning the Pruning Gamble / Q-Tuning

- **Identity / Event / Coverage:** 24/30，`ARXIV-2509.23873`；v1 2025-09-28。EU-plane diagnostic、sample triage、asymmetric token pruning、five-benchmark setup、full-data/pruning baselines、ablation 与 appendix/PDF 已读；HTML过大但不阻断全文身份与方法核验。
- **Problem → Mechanism / Ownership:** sample-only pruning 保留冗余 tokens，token-only pruning 可能删掉 instructional/corrective signal；Q-Tuning 先用 error/uncertainty 将 samples 分象限，再只对 misconception samples 做 context-aware token pruning，calibration samples 保留完整。
- **Evaluation / Boundary:** SmolLM2-1.7B 等所测 models、五 benchmarks、data-budget comparison；12.5% data/+38% 是作者特定设置，不证明所有 SFT corpus 越少越好，数据打分成本与 leakage 需计入。
- **Trade-off / Failure / Previous Boundary:** compute 下降换来 teacher/scorer bias、token boundary 与 provenance 复杂度；small/clean corpus 或 rare-domain coverage 下 full data 仍合理。
- **ROADMAP / Decision:** owner `TRAIN-DATA` Ch27；handoff `TRAIN-SFT` Ch29。`Emerging / Experimental`。

### 37. d2Cache

- **Identity / Event / Coverage:** 29/30，`ARXIV-2509.23094`；v1 2025-09-27。KV three-phase dynamics、certainty-prior/attention-aware selection、LLaDA/Dream experiments、cache/parallel/long-context ablation、memory overhead 与 limitations 已读。
- **Problem → Mechanism / Ownership:** bidirectional dLLM 任一 token 更新都会改变全序列 KV，标准 append-only cache 无效；d2Cache 对 masked tokens 用 local known-token density × confidence 选 active update，对 prompt/decoded tokens 用 attention rollout，其他 KV 近似复用。
- **Evaluation / Boundary:** LLaDA 与 Dream、base/instruct、parallel/long-context settings；作者 speed/quality 结果不证明 token-local dynamics 对所有 scheduler 稳定，production batch/concurrency/SLO 未披露。
- **Trade-off / Failure / Previous Boundary:** 避免重算换来 stale KV、certainty calibration 与 rollout overhead；短序列/full-quality contract 仍应全量更新。
- **ROADMAP / Decision:** owner `INFER-KV-CACHE` Ch45；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。`Books Pending — Integration Deferred`。

### 38. SINQ

- **Identity / Event / Coverage:** 28/30，`ARXIV-2509.22944`；v1 2025-09-26。dual-axis parameterization、Sinkhorn normalization、pseudo-activation derivation、uniform/non-uniform/calibrated comparisons、timing、large/MoE model appendix 与 ablations 已读。
- **Problem → Mechanism / Ownership:** one-axis shared scale 让 weight outlier 污染同组精度；SINQ 以 row/column dual scales 和 fast Sinkhorn-Knopp normalization 从 weight structure 近似历史 activation magnitude，可叠加既有 PTQ，且 layer-local。
- **Evaluation / Boundary:** Qwen3/Llama/DeepSeek-V3/MoE 等、WikiText2/C4/reasoning、低至 ≤4-bit，含 quantization/inference timing；perplexity gap 与 overhead 属于作者 kernels/layout，真实 serving latency 仍依赖 packing/backend。
- **Trade-off / Failure / Previous Boundary:** calibration-free portability 换来额外 scales、tile/layout contract 与 kernel support；有代表性 calibration data 时 activation-aware branch 仍可能更强。
- **ROADMAP / Decision:** owner `INFER-TENSORRT-LLM` Ch49；handoff `INFER-VLLM` Ch50。`Books Pending — Integration Deferred`。

### 39. The Rogue Scalpel

- **Identity / Event / Coverage:** 28/30，`ARXIV-2509.22067`；v1 2025-09-26。random/SAE steering、cross-model generalization、universal-vector construction、JailbreakBench/judge protocol 与 appendices 已读。
- **Problem → Mechanism / Ownership:** activation steering 被视为精确、可解释控制，但 hidden-state perturbation 可跨越 alignment boundary；论文显示随机方向、benign SAE feature 乃至组合向量都能提升 harmful compliance。任何 inference-time steering 因此是 privileged mutation，不是纯配置。
- **Evaluation / Boundary:** 多开放模型、JailbreakBench 与 unseen prompts；0→1–13% 等为作者 attack setting，不证明所有 steering 有害，也不等于 closed-model deployment attack rate。
- **Trade-off / Failure / Previous Boundary:** controllability/experimentation 换来 safety regression、vector provenance 与 composition attack；没有 steering interface 的 immutable artifact 缩小攻击面。
- **ROADMAP / Decision:** owner `PLATFORM-SECURITY` Ch72；handoff `PLATFORM-MODEL-REGISTRY` Ch59、`WORLDVIEW-REPRESENTATION` Ch5。`Books Pending — Integration Deferred`。

### 40. SLA: Sparse-Linear Attention

- **Identity / Event / Coverage:** 28/30，`ARXIV-2509.24006`；v1 2025-09-28。weight decomposition、sparse/linear branches、fine-tuning forward/backward、fused kernel、Wan/HunyuanVideo experiments、quality/efficiency ablation 与 appendix 已读。
- **Problem → Mechanism / Ownership:** DiT full attention 对 video sequence 二次复杂；纯 sparsity 会丢掉大量低幅但低秩贡献。SLA 将 critical weights 走 quadratic sparse attention、marginal weights 走 linear attention、negligible 跳过，并以单 kernel 同时支持 train/infer。
- **Evaluation / Boundary:** Wan2.1-1.3B 等、作者 GPU/kernel，报告 attention 与 end-to-end speed；13.7×/2.2× 不可脱离 model、sequence、kernel、precision 外推，fine-tuning 后 quality contract 需逐模型重验。
- **Trade-off / Failure / Previous Boundary:** 更低 FLOPs 换来 retraining、threshold/rank drift 和 custom-kernel maintenance；短 sequence/full attention 仍更稳健。
- **ROADMAP / Decision:** owner `INFER-VLLM` Ch50；handoff `TRAIN-DISTRIBUTED-TRAINING` Ch36、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。`Books Pending — Integration Deferred`。

### 41. Tool-Light

- **Identity / Event / Coverage:** 22/30，`ARXIV-2509.23285`；v1 2025-09-27。entropy diagnosis、self-evolved sampling、positive/negative pair criteria、SFT→DPO、10-dataset setup、loop/sampling/data-ratio ablations 已读。
- **Problem → Mechanism / Ownership:** tool-integrated reasoning 会 under-use、over-use 或在 tool result 后过度思考；Tool-Light 以 vanilla + entropy-guided self-sampling 产生偏好对，再经 SFT 和 iterative DPO 校正 tool-call policy。
- **Evaluation / Boundary:** 10 math/reasoning datasets；entropy change 是 proxy，不证明 tool call causal usefulness，external side effects/latency/cost 未进入训练 contract。
- **Trade-off / Failure / Previous Boundary:** 自动偏好减少标注却放大 self-sampling bias 与 tool-result leakage；明确 rule/cheap deterministic tool 下 hand-designed policy 仍更可审计。
- **ROADMAP / Decision:** owner `AGENT-TOOL-CALLING` Ch78；handoff `TRAIN-DPO` Ch34。`Emerging / Experimental`。

### 42. Constrained-MDP LLM Distillation

- **Identity / Event / Coverage:** 22/30，`ARXIV-2509.22921`；v1 2025-09-26。CMDP formulation、modified reward/policy gradient、constraint guarantee、math-reasoning baselines、KL/reward/time appendix 与 additional results 已读。
- **Problem → Mechanism / Ownership:** 将 teacher imitation 与 task reward 作固定加权无法表达“性能最大化但偏离教师不得超过阈值”；论文把 divergence 设为显式 constraint，以 state-augmented RL 推导的 modified reward 避免部署时 teacher 和 dual-loop overhead。
- **Evaluation / Boundary:** 数学 reasoning tasks、soft-Lagrangian/distillation baselines；保证依赖 formulation/estimator 假设，不证明任何 KL threshold 都对应语义 safety，domain 与 scale 有限。
- **Trade-off / Failure / Previous Boundary:** 可控偏离换来 constraint calibration、reward hacking 与 policy-gradient variance；普通 KD 在任务 reward 不可信或 latency敏感时更简单。
- **ROADMAP / Decision:** owner `TRAIN-SFT` Ch29；handoff `TRAIN-RLHF` Ch31。`Emerging / Experimental`。

### 43. ChatInject

- **Identity / Event / Coverage:** 29/30，`ARXIV-2509.22830`；v1 2025-09-26。template-mimic/multi-turn attacks、cross-model transfer、template similarity、defense/bypass、AgentDojo/InjecAgent setup、confidence intervals 与 limitations 已读。
- **Problem → Mechanism / Ownership:** plain-text indirect injection defenses 假设 malicious content 与 privileged system syntax 可区分；ChatInject 把 payload 格式化为 native chat template，并用多轮 persuasion 让 environment content 获得伪 authority。parser/template owner 因而是 security boundary。
- **Evaluation / Boundary:** frontier/open models、AgentDojo/InjecAgent、prompt defenses 与 template mixing；ASR 只属于所测 templates/agents，不证明所有 closed models 同样受影响，也不等于 production incident rate。
- **Trade-off / Failure / Previous Boundary:** flexible templating 与 cross-provider compatibility 扩大 syntax-confusion 面；strip/delimiter 仍是 defense layer，但不能独立承担 trust decision。需 typed provenance、role separation 和 tool authorization。
- **ROADMAP / Decision:** owner `PLATFORM-SECURITY` Ch72；handoff `AGENT-CONTEXT` Ch75、`AGENT-TOOL-CALLING` Ch78。`Books Pending — Integration Deferred`。

### 44. RLP: Reinforcement as a Pretraining Objective

- **Identity / Event / Coverage:** 28/30，`ARXIV-2510.01265`；v1 **2025-09-26**，虽编号为 2510；v1 information-gain reward、EMA teacher、group-relative objective、proofs、compute-matched CPT/RPT comparisons、rollout/KL/length ablations 与 cost appendix 已读。
- **Problem → Mechanism / Ownership:** next-token pretraining 只奖励局部 likelihood，RL reasoning 往往延迟到 post-training；RLP 把 sampled thought 当 action，以“加入 thought 后 future-token log-likelihood 改善”给 dense verifier-free reward，并由 EMA teacher 提供稳定 comparison。
- **Evaluation / Boundary:** Qwen3-1.7B-Base、普通文档流、八个 math/science benchmarks，含 FLOP-matched/long-context/scale ablation；19% 是作者设置，不证明 hidden thought truthful，也不能排除额外 rollout compute 与 data mixture 贡献。
- **Trade-off / Failure / Previous Boundary:** 更早学习 exploratory reasoning 换来多 rollout、EMA state、self-referential reward 与 training instability；standard next-token objective 仍是低成本、可预测 base。
- **ROADMAP / Decision:** owner `TRAIN-PRETRAINING` Ch28；handoff `TRAIN-GRPO` Ch33。`Books Pending — Integration Deferred`。

## Low-Score Source, Date, Score, and Rejection Closure

以下 20 项均已建立唯一 primary identity、核验 v1/official first-public date、复算六维评分并阅读足以支持拒绝的正文范围；`Review Pending = 0`。

| Candidate | Primary Identity / First Public | Score | Verification | Rejection Closure | ROADMAP Owner |
| --- | --- | ---: | --- | --- | --- |
| DeepSeek-V3.1-Terminus | [official release](https://api-docs.deepseek.com/news/news250922/), 2025-09-22 | 19/30 | Official announcement/changelog verified | 只证明 corrective version 和语言/agent体验修正；training、root cause、regression set 与 runtime delta 未披露，固定为 `Version Fact / Mechanism Not Disclosed`。 | `PLATFORM-MODEL-REGISTRY` |
| Better Late Than Never | [arXiv:2509.17349](https://arxiv.org/abs/2509.17349), v1 2025-09-22 | 18/30 | Full text verified | latency meta-evaluation 揭示 metric segmentation bias，但主要是测量协议修正，尚未形成新的 serving mechanism。 | `PLATFORM-EVALUATION-SYSTEM` |
| Effective Reasoning Requires Good Demonstrations | [arXiv:2509.19284](https://arxiv.org/abs/2509.19284), v1 2025-09-23 | 18/30 | Full text verified | 展示 demonstration quality 对 reasoning 的重要性，但与已有 data quality/ICL contract 高度重合，缺新的 state/control owner。 | `AGENT-CONTEXT` |
| Hyper-Bagel | [arXiv:2509.18824](https://arxiv.org/abs/2509.18824), v1 2025-09-23 | 19/30 | PDF/abstract/artifact identity verified | multimodal understanding/generation 加速是特定模型组合；HTML不可用且公开证据不足以抽象成长期系统机制。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| Soft Tokens, Hard Truths | [arXiv:2509.19170](https://arxiv.org/abs/2509.19170), v1 2025-09-23 | 18/30 | Full text verified | 对 continuous-token expressivity 给出重要反例/警告，但系统实现与可重复 runtime contract 不足，作为理论边界保留。 | `MODEL-EMBEDDING` |
| Lavida-O | [arXiv:2509.19244](https://arxiv.org/abs/2509.19244), v1 2025-09-23 | 18/30 | Full text verified | unified multimodal generation 是 model-specific branch，未提供足以改变 AR/diffusion 主线的独立系统结论。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| SimpleFold | [arXiv:2509.18480](https://arxiv.org/abs/2509.18480), v1 2025-09-23 | 19/30 | Full text verified | generic transformer/diffusion 对 protein folding 有领域价值，但不改变通用 AI System owner 或跨领域 execution contract。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| Blueprints of Trust | [arXiv:2509.20394](https://arxiv.org/abs/2509.20394), v1 2025-09-23 | 18/30 | Full text verified | Hazard-Aware System Card/ASH ID 是治理 proposal，缺部署 artifact、operating point 与实证 release gate。 | `PLATFORM-SECURITY` |
| EmbeddingGemma | [arXiv:2509.20354](https://arxiv.org/abs/2509.20354), v1 2025-09-24 | 19/30 | Official model card + PDF identity verified | 高质量小 embedding model 是版本/产品事实；HTML v1 不可取且没有超越既有 embedding lifecycle 的新机制。 | `MODEL-EMBEDDING` |
| Seedream 4.0 | [arXiv:2509.20427](https://arxiv.org/abs/2509.20427), v1 2025-09-24 | 18/30 | Full text verified | VAE token reduction 与统一 editing/composition 属于特定生成模型，证据不足以提升为通用架构结论。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| SciReasoner | [arXiv:2509.21320](https://arxiv.org/abs/2509.21320), v1 2025-09-25 | 19/30 | PDF/metadata/artifact identity verified | scientific reasoning 训练有领域价值；HTML不可用且无法闭合通用 evaluation/verifier contract，拒绝升级。 | `PLATFORM-EVALUATION-SYSTEM` |
| Hunyuan3D-Omni | [arXiv:2509.21245](https://arxiv.org/abs/2509.21245), v1 2025-09-25 | 18/30 | Full text verified | unified 3D controls 与 difficulty-aware sampling 是领域模型设计，缺通用 world-state/control-loop 证据。 | `MULTIMODAL-GENERATIVE-PARADIGMS` |
| Recon-Act | [arXiv:2509.21072](https://arxiv.org/abs/2509.21072), v1 2025-09-25 | 19/30 | Full text verified | reconnaissance/action team 与 derived tools 有启发，但 Level-3/HITL 评测和 tool derivation 边界不足，未超越现有 workflow 原则。 | `AGENT-WORKFLOW` |
| LayerNorm Induces Recency Bias | [arXiv:2509.21042](https://arxiv.org/abs/2509.21042), v1 2025-09-25 | 19/30 | Full text + title/revision drift verified | v1 以“Behind RoPE”传播，后续标题变化；recency解释是受限分析，尚不足以重写 position/normalization 主线。 | `MODEL-POSITION-ENCODING` |
| EPO | [arXiv:2509.22576](https://arxiv.org/abs/2509.22576), v1 2025-09-26 | 19/30 | Full text verified | entropy-regularized agent RL 是众多 optimization variants 之一；与 CE-GPPO/SPEAR 相比缺更强的独立 state/evidence contract。 | `TRAIN-GRPO` |
| Quantile Advantage Estimation | [arXiv:2509.22611](https://arxiv.org/abs/2509.22611), v1 2025-09-26 | 18/30 | Full text verified | quantile baseline 缓解 entropy collapse，但适用域与长期稳定性证据有限，暂不提升。 | `TRAIN-GRPO` |
| Variational Reasoning for Language Models | [arXiv:2509.22637](https://arxiv.org/abs/2509.22637), v1 2025-09-26 | 19/30 | Full text verified | variational latent reasoning 是有趣分支，但未形成跨模型、可审计、runtime-visible 的稳定机制。 | `MODEL-DECODER-ONLY` |
| VoiceAssistant-Eval | [arXiv:2509.22651](https://arxiv.org/abs/2509.22651), v1 2025-09-26 | 19/30 | Full text verified | listening/speaking/viewing benchmark 补 coverage，但不改变 evaluation evidence/uncertainty/release-gate 主线。 | `PLATFORM-EVALUATION-SYSTEM` |
| StateX | [arXiv:2509.22630](https://arxiv.org/abs/2509.22630), v1 2025-09-26 | 18/30 | Full text verified | post-training state expansion 改善 RNN recall 是 architecture-specific 机制，缺长周期 memory identity 和 serving 证据。 | `MODEL-LONG-CONTEXT` |
| WebGen-Agent | [arXiv:2509.22644](https://arxiv.org/abs/2509.22644), v1 2025-09-26 | 19/30 | Full text verified | multi-level feedback + step RL 用于 website generation，主要是领域 workflow case，未补充新的 artifact verifier contract。 | `AGENT-WORKFLOW` |

## Evidence Level

- **Level A — Official version/interface:** Qwen3-Omni official report/artifacts、DeepSeek-V3.1-Terminus announcement。只证明公开内容；未披露机制不推断。
- **Level B — Full-text primary research:** 43 retained research families，均完成 v1 method、evaluation、ablation/sensitivity、limitations 与 relevant appendix 覆盖；performance 仍是作者实验。
- **Level C — Verified low-score:** 20 low-score families，均完成 identity/date/score/rejection closure；其中 Hyper-Bagel、EmbeddingGemma、SciReasoner 的 HTML 不可用，但 PDF/official artifact identity 足以支持低分拒绝，不伪装为 full retained audit。
- **Project inference:** evolution relation、Stable Node owner、跨周 spillback 与 Books disposition 是本项目推断，不冒充论文结论。

## Cross-Week Deduplication and Spillback Ledger

### Earlier Owners — Not Scored in W39

| Source Family | Primary Identifier | First Public | Correct Owner | W39 Handling |
| --- | --- | --- | --- | --- |
| RPG | arXiv:2509.16198v1 | 2025-09-19 | 2025-W38 | W38 当前 README 无该 family，必须 reopen；W39 只记录 spillback，不计分。 |
| MANZANO | arXiv:2509.16197v1 | 2025-09-19 | 2025-W38 | W38 当前 README 无该 family，必须 reopen；W39 不倒灌。 |
| BaseReward | arXiv:2509.16127v1 | 2025-09-19 | 2025-W38 | W38 当前 README 无该 family，必须 reopen；W39 不倒灌。 |
| VLAC | arXiv:2509.15937v1 | 2025-09-19 | 2025-W38 | recommendation 落在 W39，owner 仍是 W38。 |
| Ask-to-Clarify | arXiv:2509.15061v1 | 2025-09-18 | 2025-W38 | 回拨 W38。 |
| Audio Diffusion Language Model | arXiv:2509.16622v1 | 2025-09-20 | 2025-W38 | 回拨 W38。 |
| ARE | arXiv:2509.17158v1 | 2025-09-21 | 2025-W38 | 回拨 W38。 |
| SWE-Bench Pro | arXiv:2509.16941v1 | 2025-09-21 | 2025-W38 | 回拨 W38。 |
| HAPO | arXiv:2509.16591v1 | 2025-09-20 | 2025-W38 | 回拨 W38。 |
| Synthetic Bootstrapped Pretraining | arXiv:2509.15248v1 | 2025-09-17 | 2025-W38 | W38 已收录，不重复计分。 |
| MiniCPM-V 4.5 | arXiv:2509.18154v1 | 2025-09-16 | 2025-W38 | discovery 晚于 v1；回拨 W38 核对。 |
| Speech GRPO | arXiv:2509.16990v1 | 2025-09-21 | 2025-W38 | 回拨 W38。 |

### W39-Owned Late Discovery and Revisions

- W40 look-ahead ledger 的 22 个 W39 owner 已逐项回收，不再只存在于相邻周路由：LongLive `2509.22622`、MinerU2.5 `2509.22186`、EPO `2509.22576`、Quantile Advantage `2509.22611`、StableToken `2509.22220`、MNPO `2509.23102`、Sequential DLM `2509.24007`、semantic-space RLVR `2509.23808`、ToolUniverse `2509.23426`、SparseD `2509.24014`、HunyuanImage 3.0 `2509.23951`、VideoScore2 `2509.22799`、MCPMark `2509.24002`、Q-Tuning `2509.23873`、d2Cache `2509.23094`、SINQ `2509.22944`、Rogue Scalpel `2509.22067`、SLA `2509.24006`、Tool-Light `2509.23285`、constrained-MDP distillation `2509.22921`、ChatInject `2509.22830`、RLP `2510.01265`。
- 其中 StableToken、VideoScore2、SINQ、Rogue Scalpel、distillation、ChatInject 与 RLP 的 v1 为 09-26；MNPO、ToolUniverse、d2Cache、Tool-Light 为 09-27；Sequential DLM、semantic-space RLVR、SparseD、HunyuanImage 3.0、MCPMark、Q-Tuning 与 SLA 为 09-28。arXiv 编号不能替代 submission history；RLP 虽为 `2510.*`，v1 明确是 09-26。
- LongLive、MinerU2.5、EPO、Quantile Advantage、verbal-feedback learning、SPEAR、VoiceAssistant-Eval、Variational Reasoning、WoW、StateX 与 WebGen-Agent 的 v1 均为 2025-09-26；它们在 09-29 Hugging Face feed 才集中出现，已通过 look-ahead 回拨 W39。
- PromptCoT 2.0 的 Hugging Face 提交日期为 09-29，但 arXiv v1 是 09-24，owner 固定 W39。
- Video Models v2 为 09-29；仍由 v1 09-24 的 W39 owner 持有，不在 W40 重复评分。
- W40 现有 DeepSeek-V3.2-Exp v1/official release 为 09-29，正确留在 W40；未发现应从当前 W40 旧档回拨 W39 的其它已评分 family。

## Knowledge Tree Position

| Route | Canonical Owner | W39 Evidence |
| --- | --- | --- |
| Multimodal representation and streaming | `MULTIMODAL-REPRESENTATION` Ch23 | Qwen3-Omni、MinerU2.5、StableToken |
| Generative/world/embodied state | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 → `MULTIMODAL-WORLD-MODELS` Ch25 → `MULTIMODAL-EMBODIED-VLA` Ch26 | LongLive、Sequential DLM、HunyuanImage 3.0、Video reasoning、WoW、ReflectDrive |
| Data and pretraining | `TRAIN-DATA` Ch27 → `TRAIN-PRETRAINING` Ch28 | PromptCoT 2.0、RLPT、RLP、Thinking Augmented Pre-training、Q-Tuning |
| Post-training control | `TRAIN-RLHF` Ch31 → `TRAIN-PPO` Ch32 → `TRAIN-GRPO` Ch33 | verbal feedback、CE-GPPO、MAPO、VCRL、MMR1、MNPO、semantic-space RLVR、Tree-GRPO、SPEAR、CMDP distillation |
| Context, KV and execution state | `INFER-KV-CACHE` Ch45 → `INFER-TENSORRT-LLM` Ch49 → `INFER-VLLM` Ch50 → `INFER-GPU-MEMORY` Ch54 | EpiCache、d2Cache、SINQ、SparseD、SLA；CompLLM handoff 至 `AGENT-CONTEXT` |
| Evaluation and security evidence | `PLATFORM-EVALUATION-SYSTEM` Ch66 → `PLATFORM-TRACE` Ch69 → `PLATFORM-SECURITY` Ch72 | TrustJudge、Judgment Noise、VideoScore2、Strategic Dishonesty、Rogue Scalpel、ChatInject、UltraHorizon |
| Agent information/action workflow | `AGENT-CONTEXT` Ch75 → `AGENT-TOOL-CALLING` Ch78 → `AGENT-WORKFLOW` Ch81 → `AGENT-MCP` Ch83 → `AGENT-PLATFORM` Ch84 | LIMI、UserRL、Tree-GRPO、SPEAR、ToolUniverse、Tool-Light、MCPMark、UltraHorizon |
| Multi-model execution | `INFER-SCHEDULING` Ch56 | Mixture of Thoughts；`MODEL-MOE`/`AGENT-MULTI-AGENT` 仅 handoff |

## Independent Review and Weekly Evidence Gate

### Mechanical Review

- **ISO window:** 2025-09-22～2025-09-28 = Monday～Sunday，passed。
- **Candidate count:** 64 scoring rows，编号 1～64 连续。
- **Score arithmetic:** 六维之和与 Total 对齐；25～30 = 34，20～24 = 10，低于 20 = 20。
- **Review coverage:** 44/44 retained rows 有 non-template Full Source Review；20/20 low-score rows 有 primary ID、v1/first-public date、score、status 与 rejection closure。
- **Pending state:** `Review Pending = 0`；`Unverified / Blocked = 0`；`Disputed = 0`。
- **Source families:** 64 评分行 = 64 unique family IDs；announcement、paper、artifact 和 later revision 不重复计分。
- **Look-ahead:** W40 ledger 的 22 个 W39 owner 已逐项进入 scoring/Full Source Review；其中 09-29 feed 的 11 个 09-26 owner families 也已回收；recommendation date 与 arXiv 编号未误当 event date。
- **Spillback:** 12 个 earlier-owner families 不计入 W39 denominator；其中 RPG、MANZANO、BaseReward 已确认 W38 当前档案缺失，W38 必须 reopen。
- **Evidence boundary:** vendor/author 数字均绑定公开 workload；缺失 hardware/model/precision/length/batch/concurrency/SLO 时明确 `Not Disclosed`。
- **ROADMAP:** 44 retained 与 20 low-score 均映射 Stable Node；当前章节号与 legacy 关系按 ROADMAP 复核。
- **Markdown:** 标题层级、表格、URL、代码围栏和 trailing whitespace 进入最终机械检查。

### Gate Result

`2025-W39 Weekly Evidence Gate: Passed`。

该结论只表示 W39 本周 discovery、source review、低分拒绝、revision、spillback 与 evidence boundary 闭合。它不表示 2025 archive 完成，也不表示 Historical Books Gate 开启。W38 因新发现的 owner-date spillback 需要独立 reopen，但不会阻止 W39 本周 owner 集合闭合。

## Recommended Action

- **Historical Books Gate 后优先比较:** Qwen3-Omni 的 time-aligned multimodal/runtime contract；EpiCache 的 episode-owned bounded KV；Tree-GRPO 的 shared-prefix credit；TrustJudge/Judgment Noise 的 distribution-aware evidence；Strategic Dishonesty 的 internal-vs-output audit boundary。
- **Training evolution packet:** RLPT、Thinking Augmented Pre-training、PromptCoT 2.0 分别代表 objective、derived data 与 task synthesis；MAPO/VCRL/MMR1/CE-GPPO/SPEAR/Tree-GRPO 必须作为条件分支比较，不能罗列成“更好的 GRPO”。
- **Experimental hold:** LIMI、Video reasoning、ReflectDrive、Mixture of Thoughts、WoW、MinerU2.5 保留机制证据，等待跨 workload 复现或更完整 runtime/safety contract。
- **Low-score closure:** 20 项不进入 Full Source Review；若产生新的 primary evidence，回到首次 owner 周升级，不在 later week 重复建立 family。

## Event-Date Daily Decision

Historical Backfill 不创建 2025 Daily。所有 W39 owner evidence 直接保存在本 Weekly。

## Books Integration Decision

`Historical Books Gate: Closed`。本轮未修改 Books，未把 Weekly 摘要直接写入长期知识库。

- `Books Pending — Integration Deferred`：source review 已闭合，等待年度 Historical Evidence Gate 后逐 family 比较 owner 与相邻章节。
- `Emerging / Experimental`：机制值得保留，但证据不足以稳定改变书稿。
- `Weekly Only — Version/Product Fact`：只能记录版本事实，不反推内部机制。
- `Reject`：关闭本周候选，不否认后续 source family 可能形成新证据。

## Ignored Noise

- 转载、榜单、social-media claims、无 primary identifier 项目、旧内容重发和未绑定 workload 的 benchmark 宣传未进入评分。
- Hugging Face upvote/rank 只用于发现，不作为 reliability、novelty 或 impact 证据。
- 常规 release note 若不改变 state、control/data flow、failure model 或系统 contract，不为增加候选数而计分。
- later revision、conference publication、model-card 更新与 artifact 镜像均合并到原 source family。

## Repository Changes

- 仅重建 `papers/2025/weekly/2025-W39/README.md`。
- 将旧 1 行 seed 扩展为 64 个评分候选、44 个 Full Source Review、20 个低分 closure、12 个 earlier-owner spillback、22 个 W40 look-ahead recovery 与独立 Weekly Gate。
- 未修改年度索引、Learning State、Books、W38/W40 或任何其他文件；未 stage、commit、push、reset、checkout 或 clean。

## Open Questions

- multimodal absolute-time identity 怎样与 KV chunk、prompt version、codec frame 和 partial rollback 统一？
- lossy context state 应如何同时保存 source provenance、compression version、invalidation 与 fallback？
- variance-aware curriculum 怎样避免把“持续全错但重要”的 rare-hard samples 永久排除？
- tree rollout 面对有外部 side effect 的 tools 时，environment snapshot、fork 与 compensation 由谁拥有？
- judge likelihood、rubric adherence、transitivity 与 human outcome 如何形成 calibrated release decision，而不是另一个未经校准的分数？
- strategic dishonesty 检测如何在 closed model、隐私限制和 activation drift 下提供 auditable evidence？

## Missing Materials Request Ledger

None。W39 没有仍需用户补充的 P0 Identity、P1 Full Text、P2 Artifact 或 P3 Revision blocker。Hyper-Bagel、EmbeddingGemma 与 SciReasoner 的 HTML 不可用只影响其提升资格；PDF/official artifact identity 足以完成低分拒绝，不存在 `Review Pending`。

## Sources

### 模型与研究机构

- Qwen3-Omni Technical Report — https://arxiv.org/abs/2509.17765（v1: 2025-09-22；Accessed: 2026-08-24）
- Qwen3-Omni repository — https://github.com/QwenLM/Qwen3-Omni（Accessed: 2026-08-24）
- DeepSeek-V3.1-Terminus — https://api-docs.deepseek.com/news/news250922/（First Public: 2025-09-22；Accessed: 2026-08-24）
- DeepSeek API changelog — https://api-docs.deepseek.com/updates（Accessed: 2026-08-24）

### 论文与学术来源

- LIMI — https://arxiv.org/abs/2509.17567（v1: 2025-09-22；Accessed: 2026-08-24）
- EpiCache — https://arxiv.org/abs/2509.17396（v1: 2025-09-22；Accessed: 2026-08-24）
- Strategic Dishonesty — https://arxiv.org/abs/2509.18058（v1: 2025-09-22；Accessed: 2026-08-24）
- Better Late Than Never — https://arxiv.org/abs/2509.17349（v1: 2025-09-22；Accessed: 2026-08-24）
- RLPT — https://arxiv.org/abs/2509.19249（v1: 2025-09-23；Accessed: 2026-08-24）
- MAPO — https://arxiv.org/abs/2509.18849（v1: 2025-09-23；Accessed: 2026-08-24）
- Effective Reasoning Requires Good Demonstrations — https://arxiv.org/abs/2509.19284（v1: 2025-09-23；Accessed: 2026-08-24）
- Hyper-Bagel — https://arxiv.org/abs/2509.18824（v1: 2025-09-23；Accessed: 2026-08-24）
- Soft Tokens, Hard Truths — https://arxiv.org/abs/2509.19170（v1: 2025-09-23；Accessed: 2026-08-24）
- Lavida-O — https://arxiv.org/abs/2509.19244（v1: 2025-09-23；Accessed: 2026-08-24）
- SimpleFold — https://arxiv.org/abs/2509.18480（v1: 2025-09-23；Accessed: 2026-08-24）
- CompLLM — https://arxiv.org/abs/2509.19228（v1: 2025-09-23；Accessed: 2026-08-24）
- Blueprints of Trust — https://arxiv.org/abs/2509.20394（v1: 2025-09-23；Accessed: 2026-08-24）
- Video Models Are Zero-Shot Learners and Reasoners — https://arxiv.org/abs/2509.20328（v1: 2025-09-24；Accessed: 2026-08-24）
- EmbeddingGemma — https://arxiv.org/abs/2509.20354（v1: 2025-09-24；Accessed: 2026-08-24）
- SIM-CoT — https://arxiv.org/abs/2509.20317（v1: 2025-09-24；Accessed: 2026-08-24）
- VCRL — https://arxiv.org/abs/2509.19803（v1: 2025-09-24；Accessed: 2026-08-24）
- Seedream 4.0 — https://arxiv.org/abs/2509.20427（v1: 2025-09-24；Accessed: 2026-08-24）
- Thinking Augmented Pre-training — https://arxiv.org/abs/2509.20186（v1: 2025-09-24；Accessed: 2026-08-24）
- UserRL — https://arxiv.org/abs/2509.19736（v1: 2025-09-24；Accessed: 2026-08-24）
- When Judgment Becomes Noise — https://arxiv.org/abs/2509.20293（v1: 2025-09-24；Accessed: 2026-08-24）
- ReflectDrive — https://arxiv.org/abs/2509.20109（v1: 2025-09-24；Accessed: 2026-08-24）
- PromptCoT 2.0 — https://arxiv.org/abs/2509.19894（v1: 2025-09-24；Accessed: 2026-08-24）
- Mixture of Thoughts — https://arxiv.org/abs/2509.21164（v1: 2025-09-25；Accessed: 2026-08-24）
- MMR1 — https://arxiv.org/abs/2509.21268（v1: 2025-09-25；Accessed: 2026-08-24）
- SciReasoner — https://arxiv.org/abs/2509.21320（v1: 2025-09-25；Accessed: 2026-08-24）
- Tree Search for LLM Agent RL — https://arxiv.org/abs/2509.21240（v1: 2025-09-25；Accessed: 2026-08-24）
- Hunyuan3D-Omni — https://arxiv.org/abs/2509.21245（v1: 2025-09-25；Accessed: 2026-08-24）
- TrustJudge — https://arxiv.org/abs/2509.21117（v1: 2025-09-25；Accessed: 2026-08-24）
- CE-GPPO — https://arxiv.org/abs/2509.20712（v1: 2025-09-25；Accessed: 2026-08-24）
- Recon-Act — https://arxiv.org/abs/2509.21072（v1: 2025-09-25；Accessed: 2026-08-24）
- LayerNorm Induces Recency Bias — https://arxiv.org/abs/2509.21042（v1: 2025-09-25；Accessed: 2026-08-24）
- UltraHorizon — https://arxiv.org/abs/2509.21766（v1: 2025-09-25；Accessed: 2026-08-24）
- LongLive — https://arxiv.org/abs/2509.22622（v1: 2025-09-26；Accessed: 2026-08-24）
- MinerU2.5 — https://arxiv.org/abs/2509.22186（v1: 2025-09-26；Accessed: 2026-08-24）
- EPO — https://arxiv.org/abs/2509.22576（v1: 2025-09-26；Accessed: 2026-08-24）
- Quantile Advantage Estimation — https://arxiv.org/abs/2509.22611（v1: 2025-09-26；Accessed: 2026-08-24）
- Language Models Can Learn from Verbal Feedback Without Scalar Rewards — https://arxiv.org/abs/2509.22638（v1: 2025-09-26；Accessed: 2026-08-24）
- Variational Reasoning for Language Models — https://arxiv.org/abs/2509.22637（v1: 2025-09-26；Accessed: 2026-08-24）
- SPEAR — https://arxiv.org/abs/2509.22601（v1: 2025-09-26；Accessed: 2026-08-24）
- VoiceAssistant-Eval — https://arxiv.org/abs/2509.22651（v1: 2025-09-26；Accessed: 2026-08-24）
- WoW — https://arxiv.org/abs/2509.22642（v1: 2025-09-26；Accessed: 2026-08-24）
- StateX — https://arxiv.org/abs/2509.22630（v1: 2025-09-26；Accessed: 2026-08-24）
- WebGen-Agent — https://arxiv.org/abs/2509.22644（v1: 2025-09-26；Accessed: 2026-08-24）
- StableToken — https://arxiv.org/abs/2509.22220（v1: 2025-09-26；Accessed: 2026-08-24）
- Multiplayer Nash Preference Optimization — https://arxiv.org/abs/2509.23102（v1: 2025-09-27；Accessed: 2026-08-24）
- Sequential Diffusion Language Models — https://arxiv.org/abs/2509.24007（v1: 2025-09-28；Accessed: 2026-08-24）
- Semantic-Space Exploration and Exploitation in RLVR — https://arxiv.org/abs/2509.23808（v1: 2025-09-28；Accessed: 2026-08-24）
- ToolUniverse — https://arxiv.org/abs/2509.23426（v1: 2025-09-27；Accessed: 2026-08-24）
- SparseD — https://arxiv.org/abs/2509.24014（v1: 2025-09-28；Accessed: 2026-08-24）
- HunyuanImage 3.0 — https://arxiv.org/abs/2509.23951（v1: 2025-09-28；Accessed: 2026-08-24）
- VideoScore2 — https://arxiv.org/abs/2509.22799（v1: 2025-09-26；Accessed: 2026-08-24）
- MCPMark — https://arxiv.org/abs/2509.24002（v1: 2025-09-28；Accessed: 2026-08-24）
- Winning the Pruning Gamble / Q-Tuning — https://arxiv.org/abs/2509.23873（v1: 2025-09-28；Accessed: 2026-08-24）
- d2Cache — https://arxiv.org/abs/2509.23094（v1: 2025-09-27；Accessed: 2026-08-24）
- SINQ — https://arxiv.org/abs/2509.22944（v1: 2025-09-26；Accessed: 2026-08-24）
- The Rogue Scalpel — https://arxiv.org/abs/2509.22067（v1: 2025-09-26；Accessed: 2026-08-24）
- SLA — https://arxiv.org/abs/2509.24006（v1: 2025-09-28；Accessed: 2026-08-24）
- Tool-Light — https://arxiv.org/abs/2509.23285（v1: 2025-09-27；Accessed: 2026-08-24）
- Constrained-MDP LLM Distillation — https://arxiv.org/abs/2509.22921（v1: 2025-09-26；Accessed: 2026-08-24）
- ChatInject — https://arxiv.org/abs/2509.22830（v1: 2025-09-26；Accessed: 2026-08-24）
- RLP — https://arxiv.org/abs/2510.01265（v1: 2025-09-26；Accessed: 2026-08-24）
- Hugging Face Daily Papers 2025-09-22～09-29 — https://huggingface.co/papers/date/2025-09-29（Discovery only；Accessed: 2026-08-24）

### AI Infra 与工程项目

- PyTorch releases — https://github.com/pytorch/pytorch/releases（Accessed: 2026-08-24）
- vLLM releases — https://github.com/vllm-project/vllm/releases（Accessed: 2026-08-24）
- SGLang releases — https://github.com/sgl-project/sglang/releases（Accessed: 2026-08-24）
- NVIDIA Dynamo releases — https://github.com/ai-dynamo/dynamo/releases（Accessed: 2026-08-24）
- TensorRT-LLM releases — https://github.com/NVIDIA/TensorRT-LLM/releases（Accessed: 2026-08-24）
- Kubernetes releases — https://github.com/kubernetes/kubernetes/releases（Accessed: 2026-08-24）
