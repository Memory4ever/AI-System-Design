# AI Research Weekly — 2025-W40

> Coverage Window: 2025-09-29～2025-10-05
> Research Mode: Retrospective Backfill / Full Discovery Replay
> First-public Ownership Cutoff: 2025-10-05 23:59:59 UTC
> Accessed: 2026-08-24
> Rebuilt: 2026-08-24
> Weekly Evidence Gate: Passed — 44/44 owners closed; 20/20 retained reviewed; 24/24 low rows closed
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留 DeepSeek-V3.2-Exp / DSA 一项，不能代表本周研究密度。重新执行固定机构、逐日 arXiv / Hugging Face、学术 metadata 与工程 release 扫描后，W40 最终闭合为 **44 个唯一 owner-date Source Families**：20 项达到 20/30 并完成非模板化 Full Source Review，24 项低于 20 分并完成身份、日期、六维评分与拒绝理由核验；普通 `Review Pending = 0`。

本周形成四条长期系统路线：

1. **长序列生成从保存全部历史推进到保存可递推状态。** DSA 以 learned selection 缩小主注意力访问集合；SANA-Video 把 causal linear attention 累积量变成 constant-memory block state。二者分别引入 selector miss 与有损压缩状态。
2. **RL 从“多采样再平均”推进到管理轨迹结构、环境状态和经验价值。** compositional RL、GRPO-MA、DeepSearch、ExGRPO 与 GEM 分别暴露 skill composition、thought/answer branching、tree frontier、experience replay 与 multi-turn transition 的不同 owner。
3. **Agent 可靠性从最终答案推进到过程 state。** AgentDebug 把 root cause 定位到 memory、reflection、planning、action 与 system；computer-use scaling 证明多 rollout 的收益取决于 selector 读取的 trajectory evidence，而不是单纯增加 Agent 数。
4. **多模态生成与行动必须保留 modality / environment contract。** Ovi 的 twin-backbone fusion、Vision-Zero 的 self-play 与 VLA-RFT 的 simulator-verified reward 都依赖特定 observation、action、reward 与同步假设。

本轮只闭合 Weekly 证据，不修改 Books。Self-Forcing++ 的身份、v1 日期与摘要可核，但 event-time v1 正文在当前访问路径不可抽取，已作为低分 `Unverified / Blocked` 给出精确材料请求，不留普通 pending。

## Coverage Window and Limitations

- ISO 周窗口为 Monday 2025-09-29 至 Sunday 2025-10-05；论文按 arXiv v1 UTC 日期、官方事件按首次公开日期归档。
- 固定来源顺序已重放：OpenAI、Anthropic、Google DeepMind、Meta AI、Microsoft Research、NVIDIA、Mistral、Cohere、DeepSeek、Qwen、Moonshot、ByteDance、Baidu、Tencent、Huawei、Hugging Face；随后逐日 arXiv / HF、OpenAlex / DBLP / Crossref metadata，以及 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime、OpenXLA。
- Scholar、OpenAlex、DBLP、Semantic Scholar、Crossref 与 HF 只用于 discovery、身份、日期与去重；机制结论回到官方页面、arXiv HTML/PDF、repository / artifact。
- 阅读覆盖 metadata / revision、Introduction、Related Work、Method / 公式、Implementation、Evaluation、baseline / ablation、limitations 与关键 Appendix；未披露的 hardware、precision、length、batch、concurrency 或 SLO 均记为 `Not Disclosed`。
- 2025-10-04～10-05 为周末，无新的 arXiv v1 批次；仍检查官方 release / changelog，未发现新增独立机制 owner。
- Historical Backfill 不补造 Daily；later revision 只用于限制与机制澄清，不改变 owner week。

## 1. 模型与研究机构

### Source Coverage

- **DeepSeek:** DeepSeek-V3.2-Exp / DeepSeek Sparse Attention（2025-09-29）是本周唯一达到候选门槛的官方模型事件；release、artifact、kernel 与 later same-architecture report 分离使用。
- **NVIDIA:** SANA-Video 是作者研究与 artifact，而非产品 SLO；RLP `2510.01265` 的 v1 实际为 2025-09-26，回拨 W39。
- 其余固定机构官方源已按顺序检查；没有把 API alias、价格、availability、无机制 benchmark 或旧内容重发提升为 W40 owner。

## 2. 论文与学术来源

### Source Coverage

- **2025-09-29:** SANA-Video、compositional RL、DataMind、Socratic-Zero、AgentDebug、GRPO-MA、Vision-Zero，以及 activation steering、policy valuation、scientific verifier 与 test-time specialization。
- **2025-09-30:** Dragon Hatchling / BDH、dParallel、Ovi、DeepSearch、optimizer tail-memory，以及 VLM overreasoning、scientific workflow、process-supervised exploration 与 code regression objectives。
- **2025-10-01:** GEM、VLA-RFT、RL dynamics predictability、LongCodeZip、TOUCAN，以及 SFT objectives、pretraining data、visual document retrieval、hidden-state verification、VOGUE 与 theorem proving。
- **2025-10-02:** ExGRPO、computer-use scaling、hallucination span detection，以及 StockBench、F2LLM、interactive training、red-team RPO、RewardMap、SQA、DrBench 与 Self-Forcing++。
- feed 中 v1 属于 2025-09-26～09-28 的项目全部作为 W39 spillback，不在本周重复计分。

## 3. AI Infra 与工程项目

### Source Coverage

- 固定工程项目 release、RFC、design document、PR 与 code path 已按顺序复核；本周没有形成独立 20+ owner 的 release。
- 常规 patch、模型适配列表与未给出 workload contract 的性能声明保留为 discovery noise；不把后来 release notes 倒灌为 W40 事件。
- DSA 的 DeepGEMM / FlashMLA / TileLang 只作为 DeepSeek Source Family 的 implementation evidence，不重复建立工程候选。

## Candidate Scoring

评分顺序为 Technical Novelty / System Impact / Practical Value / Source Reliability / Project Relevance / Longevity。

| # | Candidate | First Public | Source Family ID | TN | SI | PV | SR | PR | L | Total | Final Disposition |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | DeepSeek-V3.2-Exp / DSA | 2025-09-29 | `DEEPSEEK-DSA-2025` | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 2 | SANA-Video | 2025-09-29 | `ARXIV-2509.24695` | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Integration Deferred |
| 3 | RL Skill Composition | 2025-09-29 | `ARXIV-2509.25123` | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Books Pending — Integration Deferred |
| 4 | DataMind | 2025-09-29 | `ARXIV-2509.25084` | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 5 | Socratic-Zero | 2025-09-29 | `ARXIV-2509.24726` | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| 6 | AgentDebug | 2025-09-29 | `ARXIV-2509.25370` | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Books Pending — Integration Deferred |
| 7 | GRPO-MA | 2025-09-29 | `ARXIV-2509.24494` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 8 | Dragon Hatchling / BDH | 2025-09-30 | `ARXIV-2509.26507` | 5 | 5 | 3 | 5 | 4 | 4 | 26/30 | Emerging / Experimental |
| 9 | Vision-Zero | 2025-09-29 | `ARXIV-2509.25541` | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Integration Deferred |
| 10 | dParallel | 2025-09-30 | `ARXIV-2509.26488` | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Emerging / Experimental |
| 11 | DeepSearch | 2025-09-29 | `ARXIV-2509.25454` | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Books Pending — Integration Deferred |
| 12 | GEM: A Gym for Agentic LLMs | 2025-10-01 | `ARXIV-2510.01051` | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Integration Deferred |
| 13 | VLA-RFT | 2025-10-01 | `ARXIV-2510.00406` | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 14 | Predictability of RL Dynamics | 2025-10-01 | `ARXIV-2510.00553` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| 15 | LongCodeZip | 2025-10-01 | `ARXIV-2510.00446` | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Books Pending — Integration Deferred |
| 16 | ExGRPO | 2025-10-02 | `ARXIV-2510.02245` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Emerging / Experimental |
| 17 | Ovi | 2025-09-30 | `ARXIV-2510.01284` | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| 18 | TOUCAN | 2025-10-01 | `ARXIV-2510.01179` | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 19 | Scaling Agents for Computer Use | 2025-10-02 | `ARXIV-2510.02250` | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Books Pending — Integration Deferred |
| 20 | Hallucination Span Detection | 2025-10-02 | `ARXIV-2510.02173` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 21 | EasySteer | 2025-09-29 | `ARXIV-2509.25175` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Framework Case |
| 22 | ROVER | 2025-09-29 | `ARXIV-2509.24981` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Stylized RL Evidence |
| 23 | SCI-Verifier | 2025-09-29 | `ARXIV-2509.24285` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Narrow Verifier Case |
| 24 | More Thought, Less Accuracy | 2025-09-30 | `ARXIV-2509.25848` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Diagnostic Study |
| 25 | Muon Tail-End Memory | 2025-09-30 | `ARXIV-2509.26030` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Narrow Optimizer Mechanism |
| 26 | DeepScientist | 2025-09-30 | `ARXIV-2509.26603` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Workflow |
| 27 | Attention as a Compass | 2025-09-30 | `ARXIV-2509.26628` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Early Process-RL Case |
| 28 | Regression LM for Code | 2025-09-30 | `ARXIV-2509.26476` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Code-Specific Objective |
| 29 | Specialization after Generalization | 2025-09-29 | `ARXIV-2509.24510` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — TTT Analysis |
| 30 | Knapsack RL | 2025-09-30 | `ARXIV-2509.25849` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Budget-Heuristic Case |
| 31 | Beyond Log Likelihood | 2025-10-01 | `ARXIV-2510.00526` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Objective Sensitivity |
| 32 | MixtureVitae | 2025-09-29 | `ARXIV-2509.25531` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Dataset Report |
| 33 | StockBench | 2025-10-02 | `ARXIV-2510.02209` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Domain Benchmark |
| 34 | F2LLM | 2025-10-02 | `ARXIV-2510.02294` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Embedding Recipe |
| 35 | Interactive Training | 2025-10-02 | `ARXIV-2510.02297` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Early Feedback Loop |
| 36 | ModernVBERT | 2025-10-01 | `ARXIV-2510.01149` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Narrow Retriever |
| 37 | Tree-based Dialogue RPO | 2025-10-02 | `ARXIV-2510.02286` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Attack-Generation Case |
| 38 | CLUE | 2025-10-02 | `ARXIV-2510.01591` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Hidden-State Verifier |
| 39 | RewardMap | 2025-10-02 | `ARXIV-2510.02240` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Visual-RL Case |
| 40 | Aristotle | 2025-10-01 | `ARXIV-2510.01346` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Theorem-Proving Case |
| 41 | Sparse Query Attention | 2025-10-02 | `ARXIV-2510.01817` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Architecture-Specific |
| 42 | VOGUE | 2025-10-01 | `ARXIV-2510.01444` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Visual Exploration Case |
| 43 | DrBench | 2025-10-02 | `ARXIV-2510.02190` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Benchmark |
| 44 | Self-Forcing++ | 2025-10-02 | `ARXIV-2510.02283` | 4 | 4 | 3 | 2 | 4 | 2 | 19/30 | Unverified / Blocked — Full Text Required |

## Deep Analysis

### 1. SANA-Video：保存全部 KV → 保存可递推充分状态

传统 block-autoregressive video diffusion 用 full/local attention 与随历史增长的 KV；当 720p video token 数进入数万量级，历史缓存与 attention 成本同时成为瓶颈。SANA-Video 将 causal linear attention 重写为累计状态，使每个新 block 只更新固定大小 state；RoPE、temporal convolution 与 self-forcing 再补偿 locality、时序和 exposure bias。

这不是“无限上下文免费”：固定状态压缩历史并丢失 token-level 可寻址性；linear kernel、RoPE denominator 与 block commit 都带来 failure mode。作者在 64×H100、12 天训练和 RTX 5090 NVFP4 上给出 720p/5s 延迟，但这些是特定模型与 50 denoising steps 的作者结果，不是通用 serving SLO。

### 2. GEM：单轮样本 → 可复现 multi-turn transition contract

把 multi-turn trajectory 扁平为单条字符串可复用单轮 GRPO，却丢失 observation、action、reward、termination 与 reset 边界。GEM 以统一 Gym 接口、vectorized asynchronous environments、wrapper 与 evaluation protocol，把环境转移 state 变成训练系统的一等对象，并比较 REINFORCE、PPO、GRPO 与 ReBN。

收益来自环境并行和统一 contract，不来自算法名称；代价是 environment determinism、reward shaping、rollout freshness、straggler、sandbox 与 replay provenance 都必须被平台拥有。

### 3. Scaling Agents for Computer Use：增加 rollout 数 → 增加可判别证据

best-of-N 只有 selector 能识别正确轨迹时才有效。该工作并行执行多条 computer-use rollout，将 screenshot/action trace 转为 behavior narrative，再由 BJudge 选择提交；作者用 narrative ablation 说明 selector input representation 会改变结果。

证据支持的是 `parallel proposals + evidence-bearing selector`，不是“Agent 越多越好”。新增成本包括 N 倍环境机会、共享状态冲突、selector error、narrative information loss 与 tail latency；不可分解任务仍可能由 single agent + stronger verifier 更合适。

## Full Source Review

### 1. DeepSeek-V3.2-Exp / DeepSeek Sparse Attention

- **Identity / Sources / Read:** 2025-W40 / 28/30 / `DEEPSEEK-DSA-2025`；official release、repository、brief report、model/config、TileLang / DeepGEMM / FlashMLA kernels与 later same-architecture arXiv:2512.02556 已核。First public 2025-09-29；later report只补机制，不倒灌后续 RL 能力。
- **Problem → Mechanism / State / Flow:** dense MLA 在 128K 主 attention 仍近二次；DSA 以 lightning indexer 计算 relevance、top-k 2048，再让主 MLA 只访问选中 latent KV。indexer、latent KV、page index、kernel layout 与 fallback 分属 model/runtime operator；dense warm-up → sparse continuation → serving top-k gather。
- **Implementation / Evaluation Contract:** same-checkpoint migration、indexer KL warm-up、128K sequence、top-k 2048及 kernels 可核；later report给出 H800 cost estimate。训练 cluster、完整 precision、batch/concurrency、TTFT/TPOT/SLO不完整；vendor benchmark不外推。
- **Proof Boundary / Trade-off / Evolution:** 证明 learned selection 可把 main attention 降为 $O(Lk)$，不证明总复杂度完全线性、所有硬件更快或 selector 不丢关键 KV。新增 indexer compute、miss、sparse gather、layout/RoPE compatibility；短 context 或无 sparse kernel 时 dense MLA 仍合理。Direct Evolution：NSA → DSA productization。
- **ROADMAP / Decision / Questions:** Owner `MODEL-LONG-CONTEXT` Ch22；handoff `INFER-KV-CACHE` Ch45、`INFER-TENSORRT-LLM` Ch49；目标及相邻章已读，现有coverage只部分覆盖migration/fallback。最终 `Books Pending — Integration Deferred`；本轮不改Books。Open: selector recall、top-k sensitivity、layout conformance与独立SLO。

### 2. SANA-Video

- **Identity / Sources / Read:** 29/30 / `ARXIV-2509.24695`；v1 2025-09-29、v2 2025-10-13。arXiv HTML、project、method/equations、training stages、experiments、ablations、deployment与 appendices已核。
- **Problem → Mechanism / State / Flow:** full attention/KV 随video tokens增长；Linear DiT + block causal linear attention保存累计key/value state，配合3D RoPE、temporal Conv、autoregressive block training与self-forcing。generator拥有block state，runtime拥有commit，data pipeline拥有caption/filter provenance。
- **Implementation / Evaluation Contract:** 1.6B级模型从T2I继续训练，64×H100、12天；720p、5s、50 denoising steps，RTX5090 NVFP4 71s→29s为作者结果；比较Wan/SkyReel并做RoPE/temporal/latency ablation。并发/SLO未披露。
- **Proof Boundary / Trade-off / Evolution:** 证明递推linear state可使历史内存不随block数增长，不证明无限长度质量、exact recall或通用16×。固定状态压缩、denominator稳定、exposure bias与错误累积是新风险；短视频/高精细全局交互仍可用full attention。Direct Evolution：full history → local window → recurrent global summary。
- **ROADMAP / Decision / Questions:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；handoff `MODEL-LONG-CONTEXT` Ch22、`INFER-KV-CACHE` Ch45；相邻章已读，existing coverage缺mutable state边界。最终 `Books Pending — Integration Deferred`。Open: state invalidation、scene cut与interactive SLO。

### 3. RL Skill Composition

- **Identity / Sources / Read:** 29/30 / `ARXIV-2509.25123`，v1 2025-09-29；controlled tasks、training、representations、interventions、ablations与limitations已核。
- **Problem → Mechanism / State / Flow:** next-token pretraining可分别学会 $f$ 与 $g$，却未保证执行 $g(f(x))$；RL reward在组合任务上选择已有技能路径并更新policy。weights持有可复用技能，rollout持有组合轨迹，verifier持有终局reward。
- **Evaluation Contract:** 合成可控函数组合与多模型/训练阶段比较，以pretraining/NTP与RL分离“学新原语”和“重组旧技能”；hardware、production batch/concurrency/SLO不构成结论。结果是机制诊断，不是开放域通用能力证明。
- **Proof Boundary / Trade-off / Evolution:** 支持“RL可重组已存在但未被调用的技能”，不证明RL从无到有创造任意知识。奖励可验证性换来探索成本、spurious composition与reward hacking；有高质量组合轨迹时SFT仍合理。Alternative Branch：imitation composition vs outcome-driven search。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-RLHF` Ch31；handoff `TRAIN-GRPO` Ch33、`AGENT-PLANNING` Ch79；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: 如何检测primitive已存在、何时只是memorization、组合深度如何扩展？

### 4. Scaling Generalist Data-Analytic Agents / DataMind

- **Identity / Sources / Read:** 28/30 / `ARXIV-2509.25084`，v1 2025-09-29；taxonomy、data synthesis、SFT/RL、tool environment、benchmarks、ablations、limitations与artifact已核。
- **Problem → Mechanism / State / Flow:** 单一表格/SQL benchmark只覆盖局部工具链；DataMind从task taxonomy合成多轮code/tool trajectories，以SFT建行为先验，再用dynamic-objective RL改善执行。workspace/files、interpreter state、trajectory与verdict由environment而非weights拥有。
- **Evaluation Contract:** 多类data-analysis tasks与agent baselines，组件/training strategy ablation；作者数据/模型/harness结果不等于生产分析正确性。部分hardware、precision、online concurrency与SLO未完整披露。
- **Proof Boundary / Trade-off / Evolution:** 证明task diversity + executable environment可提升所测agent，不证明生成数据无偏或artifact可信。工具覆盖扩大带来sandbox、leakage、silent code error与judge gap；高风险任务仍应使用typed workflow。Direct Evolution：answer data → executable trajectory → environment-grounded RL。
- **ROADMAP / Decision / Questions:** Owner `AGENT-WORKFLOW` Ch81；handoff `TRAIN-DATA` Ch27、`PLATFORM-EVALUATION-SYSTEM` Ch66；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: artifact correctness、data lineage和execution isolation如何进入reward？

### 5. Socratic-Zero

- **Identity / Sources / Read:** 27/30 / `ARXIV-2509.24726`，v1 2025-09-29；teacher/solver/generator loop、prompts、reward ablation、curriculum、8×H20 implementation与appendices已核。
- **Problem → Mechanism / State / Flow:** 静态外部题库限制coverage；teacher评估solver能力区间，generator产生近发展区问题，solver训练后循环更新。curriculum与generated problems是derived training state，不能与ground truth混同。
- **Evaluation Contract:** 从100 seed questions启动，在数学reasoning benchmarks上比较静态augmentation等；8×H20/96GB、NVLink/InfiniBand披露。作者结果依赖teacher/model family与verifier；production SLO不适用。
- **Proof Boundary / Trade-off / Evolution:** 证明受控设置下co-evolution可扩展训练题，不证明“data-free”没有先验数据，也不证明问题/答案始终正确。新增self-confirmation、curriculum collapse、teacher bias与cost；人工数据仍是可靠锚点。Direct Evolution：static dataset → generated curriculum → co-evolving curriculum。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-DATA` Ch27；handoff `AGENT-MULTI-AGENT` Ch82；相邻章已读。最终 `Emerging / Experimental`。Open: provenance、duplicate control、counterexample review与rollback。

### 6. Where LLM Agents Fail / AgentDebug

- **Identity / Sources / Read:** 29/30 / `ARXIV-2509.25370`，v1 2025-09-29；taxonomy、AgentErrorBench、root-cause algorithm、ALFWorld/GAIA/WebShop evaluation、ablation、limitations与repository已核。
- **Problem → Mechanism / State / Flow:** final failure无法定位cascading cause；taxonomy把memory、reflection、planning、action与system error分开，AgentDebug定位最早root cause并生成targeted feedback。raw trajectory、module attribution、feedback与retry generation必须有独立provenance。
- **Evaluation Contract:** 三类agent benchmarks与真实failure trajectories；作者报告all-correct +24%、step accuracy +17%、task success相对提升最高26%，仅适用于其annotator/models/harness。hardware、debug latency/SLO未披露。
- **Proof Boundary / Trade-off / Evolution:** 证明模块化trajectory diagnosis优于所测baseline，不证明taxonomy完备、feedback正确或retry安全。更细trace增加storage、privacy、attribution error与循环修复成本；简单流程可使用typed error code。Direct Evolution：outcome label → step trace → root-cause attribution → bounded retry。
- **ROADMAP / Decision / Questions:** Owner `AGENT-REFLECTION` Ch80；handoff `AGENT-WORKFLOW` Ch81、`PLATFORM-OBSERVABILITY` Ch67；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: attribution uncertainty、cross-module cause与human escalation。

### 7. GRPO-MA

- **Identity / Sources / Read:** 26/30 / `ARXIV-2509.24494`，v1 2025-09-29；tree-style theory、thought/answer sampling、variance derivation、math/code/multimodal experiments、temperature ablation与appendix已核。
- **Problem → Mechanism / State / Flow:** 一条thought只采一个answer会把thought quality与answer noise耦合；每个thought分支多个answers，以组内returns估计thought advantage。tree parent/child identity和sample budget成为训练state。
- **Evaluation Contract:** math、code、vision tasks与GRPO baselines，考察answers-per-thought与temperature；完整training cost与跨模型稳定性有限，serving SLO不适用。作者结果不是所有branching policy的通用定律。
- **Proof Boundary / Trade-off / Evolution:** 支持branching降低thought advantage variance，不证明更多answers单调最优。额外rollout、correlated children、credit leakage与memory增大；dense reward任务仍可用flat GRPO。Direct Evolution：flat group → hierarchical group → structured credit assignment。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-GRPO` Ch33；handoff `TRAIN-RLHF` Ch31；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: budget allocation、off-policy reuse与tree truncation bias。

### 8. Dragon Hatchling / BDH

- **Identity / Sources / Read:** 26/30 / `ARXIV-2509.26507`，v1 2025-09-30；mathematical particle formulation、GPU implementation、scale experiments、associative-memory analyses与appendices已核。
- **Problem → Mechanism / State / Flow:** Transformer依赖全局attention与固定层栈；BDH以局部相互作用粒子、Hebbian fast-weight-like state和反复更新替代显式全局attention。particle state与interaction graph是mutable runtime/training state。
- **Evaluation Contract:** 约10M～1B参数、GPT-2-like language tasks及memory analyses；作者比较同规模baselines。部分hardware可核，但training data、precision、batch、latency/SLO不足以支持production claim。
- **Proof Boundary / Trade-off / Evolution:** 证明该架构在作者任务上可训练并呈现局部memory现象，不证明生物等价、规模律优于Transformer或serving更高效。局部更新带来迭代步数、stability、state reset与kernel不成熟；Transformer仍是默认。Alternative Branch / Experimental。
- **ROADMAP / Decision / Questions:** Owner `MODEL-TRANSFORMER-LAYER` Ch17；handoff `MODEL-MLP` Ch16、`MODEL-LONG-CONTEXT` Ch22；相邻章已读。最终 `Emerging / Experimental`。Open: scaling、state reproducibility、parallel efficiency与fair baseline。

### 9. Vision-Zero

- **Identity / Sources / Read:** 27/30 / `ARXIV-2509.25541`，v1 2025-09-29；multi-agent self-play game、Iterative-SPO、data construction、prompts、ablations、reproducibility与limitations已核。
- **Problem → Mechanism / State / Flow:** 固定视觉QA数据难覆盖组合难例；proposer/editor生成图像变化，solver回答，judge/verified signal驱动迭代。game state、pair identity、reward与model version需分离。
- **Evaluation Contract:** 单图、pairwise edits与多视觉benchmarks；作者给出self-play/algorithm ablation。尚不覆盖长视频、multi-image或interactive 3D，hardware与production SLO不构成通用结论。
- **Proof Boundary / Trade-off / Evolution:** 支持策略化self-play在所测VLM提高表现，不证明game difficulty等于真实分布。新增collusion、reward leakage、synthetic bias与环境成本；有人类监督时SFT仍合理。Direct Evolution：static visual data → adversarial pair generation → policy-coupled curriculum。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-RLHF` Ch31；handoff `MULTIMODAL-REPRESENTATION` Ch23、`AGENT-MULTI-AGENT` Ch82；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: judge independence与synthetic provenance。

### 10. dParallel

- **Identity / Sources / Read:** 27/30 / `ARXIV-2509.26488`，v1 2025-09-30；objective、parallel decoding、models/datasets、speed-quality evaluation、ablation、limitations与reproducibility已核。
- **Problem → Mechanism / State / Flow:** diffusion LM固定mask schedule需要多轮串行refinement；dParallel学习哪些tokens可并行commit，以减少steps。mask/confidence、parallel group与commit decision是decode state。
- **Evaluation Contract:** 多个dLLM与语言tasks，比较固定/heuristic schedules及step ablation；作者报告减少steps且质量近似。hardware、batch、concurrency、TTFT/TPOT/SLO不完整，不能把step reduction等同wall-clock speedup。
- **Proof Boundary / Trade-off / Evolution:** 证明learned schedule可改善所测step-quality trade-off，不证明exactness或跨模型泛化。错误并行commit会传播且rollback复杂；保守serial refinement在高风险任务仍合理。Direct Evolution：fixed schedule → confidence heuristic → learned parallel commit。
- **ROADMAP / Decision / Questions:** Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；handoff `INFER-SPECULATIVE-DECODING` Ch48；相邻章已读。最终 `Emerging / Experimental`。Open: calibration、rollback、batch interaction与kernel utilization。

### 11. DeepSearch

- **Identity / Sources / Read:** 29/30 / `ARXIV-2509.25454`，v1 2025-09-29；tree search、entropy-guided frontier、adaptive replay、solution cache、training、ablations与limitations已核。
- **Problem → Mechanism / State / Flow:** flat on-policy RLVR在难题上正reward稀疏；MCTS扩展partial reasoning，global frontier按value/entropy选节点，成功/失败经验进入replay/cache。frontier、tree provenance、verifier verdict与policy version必须绑定。
- **Evaluation Contract:** 1.5B reasoning model与数学tasks，对比RLVR/search baselines；作者报告62.95%及相对GPU-hour节省，受题库、verifier和cache命中影响。并发/SLO与跨规模外推不成立。
- **Proof Boundary / Trade-off / Evolution:** 支持tree-guided exploration缓解作者设置的稀疏reward，不证明MCTS总比sampling便宜。新增tree memory、stale replay、duplicate solutions与verifier exploitation；容易题仍适合flat rollout。Direct Evolution：flat rollout → structured frontier → replayable experience。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-RLHF` Ch31；handoff `AGENT-PLANNING` Ch79、`AGENT-MEMORY` Ch77；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: cache invalidation、policy drift与search/replay accounting。

### 12. GEM: A Gym for Agentic LLMs

- **Identity / Sources / Read:** 29/30 / `ARXIV-2510.01051`，v1 2025-10-01；environment API、async vectorization、wrappers、24 environments、training algorithms、evaluation与appendix已核。
- **Problem → Mechanism / State / Flow:** 单轮RL接口无法表达multi-turn observation/action/reward/termination；GEM提供统一Gym contract和异步vectorized execution，比较REINFORCE、PPO、GRPO、ReBN。environment拥有transition state，trainer拥有trajectory/version，sandbox拥有effects。
- **Evaluation Contract:** 24 environments及多算法/model experiments；作者指出REINFORCE是强baseline且reward shaping会改变convergence。hardware/precision、environment吞吐、straggler与SLO未形成跨平台保证。
- **Proof Boundary / Trade-off / Evolution:** 证明统一环境层可复现训练比较，不证明wrapper消除environment差异或更多env并行必然更好。新增nondeterminism、reset leak、reward inconsistency、sandbox风险；单轮verifiable tasks仍可用轻量GRPO。Layering：model RL → environment contract → platform runtime。
- **ROADMAP / Decision / Questions:** Owner `AGENT-PLATFORM` Ch84；handoff `TRAIN-RLHF` Ch31、`AGENT-WORKFLOW` Ch81；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: environment version、side-effect rollback、replay determinism与fleet accounting。

### 13. VLA-RFT

- **Identity / Sources / Read:** 28/30 / `ARXIV-2510.00406`，v1 2025-10-01；world simulator、verified reward、VLA fine-tuning、benchmarks、evaluation与appendix已核。
- **Problem → Mechanism / State / Flow:** imitation只复制demonstration，不能直接优化task success；world simulator执行proposed action/trajectory并返回可验证结果，RL更新VLA。observation/action schema、simulator state、reward与policy version是独立owner。
- **Evaluation Contract:** 作者robot/VLA tasks和simulator-based rewards；实际robot transfer、control frequency、hardware、latency/safety SLO未完整证明。simulator correctness是结论前提。
- **Proof Boundary / Trade-off / Evolution:** 支持simulator verifier可为VLA提供比纯imitation更直接的信号，不证明sim-to-real、物理安全或world model无偏。新增reward hacking、sim gap、action latency与unsafe exploration；真实demonstration仍是锚点。Direct Evolution：behavior cloning → simulated outcome reward → bounded real validation。
- **ROADMAP / Decision / Questions:** Owner `MULTIMODAL-EMBODIED-VLA` Ch26；handoff `TRAIN-RLHF` Ch31、`PLATFORM-EVALUATION-SYSTEM` Ch66；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: safety envelope、sim fidelity与human override。

### 14. Predictability of RL Dynamics

- **Identity / Sources / Read:** 26/30 / `ARXIV-2510.00553`，v1 2025-10-01；parameter-update analysis、rank-1 subspace、prediction/acceleration、ablations与limitations已核。
- **Problem → Mechanism / State / Flow:** RL昂贵且update trajectory难解释；作者观察更新集中于可预测低秩方向，使用早期dynamics估计后续更新。optimizer state、subspace estimate与checkpoint lineage必须绑定。
- **Evaluation Contract:** 多模型/reasoning tasks与subspace ablation；作者报告加速且性能保持，只适用于所测algorithm/model scale。hardware、precision、distributed optimizer与end-to-end cost未足以泛化。
- **Proof Boundary / Trade-off / Evolution:** 证明特定RL runs存在强低秩结构，不证明所有任务/阶段可预测或可安全跳步。新增forecast drift、missed directions与rollback需求；非平稳reward仍需完整更新。Principle Reuse：low-rank optimization state → predicted trajectory。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-RLHF` Ch31；handoff `TRAIN-CHECKPOINT` Ch35；相邻章已读。最终 `Emerging / Experimental`。Open: drift detector、distributed state一致性和错误预测恢复。

### 15. LongCodeZip

- **Identity / Sources / Read:** 27/30 / `ARXIV-2510.00446`，v1 2025-10-01；function selection、conditional-perplexity blocks、adaptive budget、baselines、implementation、ablation与limitations已核。
- **Problem → Mechanism / State / Flow:** uniform truncation破坏code dependencies；先按instruction选相关functions，再在函数内按perplexity检测blocks并分配token budget。repository structure、score、compressed context与source span需保留provenance。
- **Evaluation Contract:** 多code LLM/tasks与compression baselines，作者报告最高5.6× compression；hardware、retrieval latency、concurrency/SLO不完整。结果依赖parser、language和instruction。
- **Proof Boundary / Trade-off / Evolution:** 证明结构感知两阶段压缩优于作者baselines，不证明被删代码无跨文件隐式依赖。新增parser failure、dependency loss、stale index与budget tuning；短repository应保留原文。Direct Evolution：tail truncation → semantic chunks → structure-aware adaptive compression。
- **ROADMAP / Decision / Questions:** Owner `AGENT-CONTEXT` Ch75；handoff `AGENT-RAG` Ch76、`MODEL-LONG-CONTEXT` Ch22；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: span provenance、dependency graph和incremental invalidation。

### 16. ExGRPO

- **Identity / Sources / Read:** 26/30 / `ARXIV-2510.02245`，v1 2025-10-02；experience value、mixed-policy objective、Qwen2.5-Math-7B/OpenR1 setup、ablations、limitations与appendices已核。
- **Problem → Mechanism / State / Flow:** uniform replay忽略哪些经验最有学习价值；ExGRPO用correctness与entropy估计experience value，优先选择经验并混合新旧policy data。experience、policy version、priority与importance correction是state。
- **Evaluation Contract:** 1.5B～8B级模型/数学任务，核心实验用Qwen2.5-Math-7B与Dr.GRPO/OpenR1；作者报告若干平均提升。hardware、wall-clock、concurrency/SLO未证明普适性。
- **Proof Boundary / Trade-off / Evolution:** 支持有条件经验选择提高作者设置sample efficiency，不证明高entropy总有价值或off-policy bias已消除。新增priority collapse、staleness与duplicate replay；rapid drift时纯on-policy更稳。Direct Evolution：uniform rollout → valued experience → version-aware replay。
- **ROADMAP / Decision / Questions:** Owner `TRAIN-GRPO` Ch33；handoff `AGENT-MEMORY` Ch77；相邻章已读。最终 `Emerging / Experimental`。Open: replay TTL、importance correction、failure diversity。

### 17. Ovi

- **Identity / Sources / Read:** 25/30 / `ARXIV-2510.01284`，v1 2025-09-30；twin-DiT、blockwise cross-modal fusion、training stages、implementation、metrics、ablation与limitations已核。
- **Problem → Mechanism / State / Flow:** 独立生成audio/video再后处理同步会丢失细粒度一致性；Ovi保持独立audio/video backbone，在block间交换cross-modal state并联合训练。timestamp、modality tokens、fusion state与decoder由不同模块拥有。
- **Evaluation Contract:** 作者audio-video datasets、compared methods与同步/质量metrics，做fusion ablation；hardware、precision、batch、serving latency/concurrency/SLO不完整。主观metric与数据构成限制外推。
- **Proof Boundary / Trade-off / Evolution:** 证明twin backbone + repeated fusion在作者设置改善同步，不证明shared latent或单backbone劣于所有场景。双backbone增加compute、alignment drift与timestamp mismatch；低耦合内容仍可用独立pipeline。Alternative Branch：late composition vs iterative fusion。
- **ROADMAP / Decision / Questions:** Owner `MULTIMODAL-REPRESENTATION` Ch23；handoff `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；相邻章已读。最终 `Emerging / Experimental`。Open: sync calibration、streaming与modality rollback。

### 18. TOUCAN

- **Identity / Sources / Read:** 28/30 / `ARXIV-2510.01179`，v1 2025-10-01；MCP environment collection、1.5M synthesis pipeline、tool-schema extensions、SFT evaluation、BFCL ablation、limitations、code/data instructions已核。
- **Problem → Mechanism / State / Flow:** synthetic tool calls常缺真实schema与execution feedback；TOUCAN从real MCP environments枚举tools、生成/执行/过滤trajectories并扩展为training data。server/tool version、schema、arguments、result、verdict与license需共同形成provenance。
- **Evaluation Contract:** 1.5M trajectories与BFCL V3等function-calling benchmarks；extension ablation显示各环节贡献。server availability、side effects、hardware、online concurrency与SLO未形成生产保证。
- **Proof Boundary / Trade-off / Evolution:** 证明真实MCP schema可规模化构造tool-agentic data，不证明数据安全、live behavior稳定或benchmark等价workflow success。新增secret/PII、license、schema drift与unsafe effects；高风险域仍需人工curation。Direct Evolution：static schema examples → executed traces → provenance-bearing MCP data。
- **ROADMAP / Decision / Questions:** Owner `AGENT-MCP` Ch83；handoff `TRAIN-DATA` Ch27、`AGENT-TOOL-CALLING` Ch78；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: consent、redaction、schema revision和sandbox。

### 19. Scaling Agents for Computer Use

- **Identity / Sources / Read:** 29/30 / `ARXIV-2510.02250`，v1 2025-10-02；bBoN rollout、behavior narrative、BJudge selector、OSWorld/Windows/Android evaluation、implementation、ablation与limitations已核。
- **Problem → Mechanism / State / Flow:** 单agent受随机误操作限制；并行N条rollout后，将screenshots/actions转成behavior narratives，selector比较并commit一条。environment snapshot、trajectory、narrative、verdict与effect需隔离。
- **Evaluation Contract:** 多computer-use environments；作者报告OSWorld最高69.9%，10-rollout narrative ablation约60.2%对55～56.8% alternatives。模型、rollout数与harness绑定；hardware、tail latency、并发/SLO未完整披露。
- **Proof Boundary / Trade-off / Evolution:** 支持selector evidence质量决定parallel scaling，不证明Agent数量单调改善或外部系统可安全并行。N倍cost、state conflict、selector bias、narrative loss与rollback是新风险；不可复制环境仍适合single agent。Direct Evolution：single rollout → best-of-N → evidence-aware selection。
- **ROADMAP / Decision / Questions:** Owner `AGENT-MULTI-AGENT` Ch82；handoff `AGENT-WORKFLOW` Ch81、`PLATFORM-EVALUATION-SYSTEM` Ch66；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: shared-state isolation、selector calibration与cost-normalized gain。

### 20. Learning to Reason for Hallucination Span Detection

- **Identity / Sources / Read:** 26/30 / `ARXIV-2510.02173`，v1 2025-10-02；span annotation、reasoning detector、training/evaluation、baselines、error analyses与available appendices已核。
- **Problem → Mechanism / State / Flow:** answer-level factuality label不能定位修复位置；模型生成claim-level reasoning并标注unsupported spans。source context、atomic claim、evidence link、span verdict与detector confidence必须分别保存。
- **Evaluation Contract:** 多hallucination detection datasets/baselines与span metrics；作者实验不等于truth probability calibration。hardware、precision、online latency/concurrency与abstention operating point未完整披露。
- **Proof Boundary / Trade-off / Evolution:** 证明reasoning supervision可改善所测span detection，不证明detector reasoning真实或claims可独立相乘。新增verification tokens、false confidence、correlated errors与retrieval gap；低风险文本可用轻量filter。Direct Evolution：answer label → claim/span label → evidence-linked correction。
- **ROADMAP / Decision / Questions:** Owner `PLATFORM-EVALUATION-SYSTEM` Ch66；handoff `AGENT-REFLECTION` Ch80；相邻章已读。最终 `Books Pending — Integration Deferred`。Open: calibrated operating point、dependency-aware aggregation与human review。

## Low-Score and Blocked Closure

以下24个owner均已核身份、v1日期与六维评分；拒绝不是泛化的“分数低”。

| Candidate | Evidence Boundary | Rejection / Blocked Closure |
| --- | --- | --- |
| EasySteer | activation-steering framework与作者case可读 | framework便利性未形成跨模型稳定控制contract |
| ROVER | random-policy Q-value在作者RL设置可读 | stylized valuation不足以替代PPO/GRPO critic结论 |
| SCI-Verifier | scientific QA verifier benchmark/model可读 | domain equivalence与judge边界强，未形成通用release gate |
| More Thought, Less Accuracy | VLM overthinking诊断可读 | 相关性研究不提供可执行router/stop mechanism |
| Muon Tail-End Memory | heavy-tail associative memory分析可读 | 特定optimizer/数据分布，缺distributed/end-to-end证据 |
| DeepScientist | progressive science workflow可读 | domain artifact correctness与独立replication不足 |
| Attention as a Compass | attention-guided process RL可读 | 早期单机制case，缺跨task credit-assignment边界 |
| Regression LM for Code | continuous code objective可读 | code-specific metric尚未改变通用generation factorization |
| Specialization after Generalization | test-time training分析可读 | 诊断价值高但缺可复用runtime contract |
| Knapsack RL | rollout budget allocation可读 | 作者设置有效，不证明通用exploration allocator |
| Beyond Log Likelihood | capability-dependent SFT objectives可读 | objective ranking敏感，尚无稳定选择规则 |
| MixtureVitae | permissive-first dataset pipeline可读 | dataset/license report，缺独立training因果分解 |
| StockBench | real-market agent benchmark可读 | domain opportunity、harness与market period耦合 |
| F2LLM | 6M open-data embedding recipe可读 | author report未形成通用embedding data law |
| Interactive Training | feedback-driven optimization可读 | identity、feedback owner与stability证据早期 |
| ModernVBERT | smaller visual-document retriever可读 | narrow architecture/benchmark，不改变RAG owner结论 |
| Tree-based Dialogue RPO | red-team attack generation可读 | attack success依赖target/policy，缺defense operating point |
| CLUE | hidden-state clustering verifier可读 | representation drift与cross-model transfer不足 |
| RewardMap | multi-stage visual reward shaping可读 | visual task-specific，不形成通用reward ownership原则 |
| Aristotle | theorem-proving system facts可读 | product/harness能力不能反推通用agent correctness |
| Sparse Query Attention | query-head reduction与作者实验可读 | architecture-specific，缺跨backend/long-context evidence |
| VOGUE | visual uncertainty引导探索可读 | perturbation proxy与epistemic uncertainty未对齐 |
| DrBench | evidence-bundle research benchmark可读 | domain benchmark，不改变evaluation owner |
| Self-Forcing++ | identity `2510.02283`、v1 2025-10-02与摘要可核；HTML返回内部错误，18.3 MB PDF在当前web extractor触发size limit | `Unverified / Blocked`。需 `2510.02283v1` event-time PDF或source bundle，含Method、training algorithm、evaluation、ablations、limitations、appendix；建议文件名 `2510.02283v1.pdf` 或 `2510.02283v1-source.tar.gz`。恢复前不采用其minute-scale质量/长度结论 |

## Evidence Level

- Official Fact只覆盖release、artifact、version与公开接口；产品行为不用于反推内部训练/runtime。
- arXiv / report为作者实验；性能数字绑定已披露model、hardware、precision、length、steps、batch/concurrency与evaluator，缺失项写`Not Disclosed`。
- `Books Pending`表示Weekly证据闭合但Historical Books Gate关闭，不是Weekly缺失。
- `Emerging / Experimental`表示全文可读但独立复现、规模或production contract不足；`Unverified / Blocked`不进入长期机制结论。

## Cross-Week Deduplication and Spillback Ledger

以下 **22 个 Source Families** 在W40 feed出现，但arXiv v1属于W39（2025-09-22～09-28）；22/22全部排除于W40 Candidate Scoring与44-row owner分母之外，由W39 owner week承接：

- LongLive `2509.22622`、MinerU2.5 `2509.22186`、EPO `2509.22576`、Quantile Advantage `2509.22611`、StableToken `2509.22220`、Multiplayer Nash Preference Optimization `2509.23102`。
- Sequential Diffusion LMs `2509.24007`、Hidden-State RLVR `2509.23808`、ToolUniverse `2509.23426`、SparseD `2509.24014`、HunyuanImage 3.0 `2509.23951`、VideoScore2 `2509.22799`。
- MCPMark `2509.24002`、joint sample/token pruning `2509.23873`、d2Cache `2509.23094`、SINQ `2509.22944`、Rogue Scalpel `2509.22067`、SLA `2509.24006`。
- Tool-integrated reasoning `2509.23285`、distillation CMDP `2509.22921`、ChatInject `2509.22830`、RLP `2510.01265`（v1 2025-09-26）。
- DeepSeek DSA在W08 NSA、W40 V3.2-Exp与W49完整V3.2 report之间按同family演进，不重复形成三套机制结论。

## Knowledge Tree Position

- **Model / Multimodal:** `MODEL-TRANSFORMER-LAYER` Ch17、`MODEL-LONG-CONTEXT` Ch22、`MULTIMODAL-REPRESENTATION` Ch23、`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24、`MULTIMODAL-EMBODIED-VLA` Ch26。
- **Training:** `TRAIN-DATA` Ch27、`TRAIN-RLHF` Ch31、`TRAIN-GRPO` Ch33、`TRAIN-CHECKPOINT` Ch35。
- **Inference / Platform:** `INFER-KV-CACHE` Ch45、`INFER-SPECULATIVE-DECODING` Ch48、`INFER-TENSORRT-LLM` Ch49、`PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-OBSERVABILITY` Ch67。
- **Agent:** `AGENT-CONTEXT` Ch75、`AGENT-MEMORY` Ch77、`AGENT-PLANNING` Ch79、`AGENT-REFLECTION` Ch80、`AGENT-WORKFLOW` Ch81、`AGENT-MULTI-AGENT` Ch82、`AGENT-MCP` Ch83、`AGENT-PLATFORM` Ch84。

## Recommended Action

- Historical Books Gate保持关闭；20个retained owners已具备未来逐Source Family审计输入，但本阶段不写Books。
- Self-Forcing++正文恢复后重新评分；当前blocked-skip不阻塞forward sweep，也不引用其性能结论。
- W39 spillbacks已明确列账；本文件不越权修改W39或年度索引。

## Event-Date Daily Decision

Historical Backfill不创建Daily；真实事件日期与证据边界直接记录在Weekly。

## Books Integration Decision

`Historical Books Gate: Closed`。本周没有执行Books Integration；`Books Pending — Integration Deferred`不能解释为已经吸收。

## Ignored Noise

- 忽略转载、排行榜、旧论文重发、HF推荐日与v1日期混淆、无primary evidence的营销性能结论。
- 常规patch、兼容性列表、价格/API alias变化若不形成新机制，只作为discovery记录。
- 不把作者benchmark、模拟器结果或judge分数写成跨模型、跨硬件、跨环境的通用事实。

## Repository Changes

- 仅重建 `papers/2025/weekly/2025-W40/README.md`。
- 旧1-row快照被44-owner discovery账本取代；未修改年度索引、Learning State、Books、相邻Weekly或Git暂存状态。

## Open Questions

- DSA selector recall、SANA recurrent state loss、dParallel commit calibration能否使用统一state-quality / fallback contract？
- Agent rollout scaling如何同时计量environment opportunity、selector accuracy、shared-state conflict与cost-normalized gain？
- RL experience、tree frontier与derived curriculum如何绑定policy version、TTL、supersession与rollback？
- Self-Forcing++ event-time v1全文何时可取得？

## Independent Review and Weekly Gate

- **Window / dates:** 2025-09-29～10-05 ISO Monday～Sunday通过；44个owner日期均在窗口。
- **Denominator:** 44 W40 owners = 20 retained + 24 low/blocked；spillbacks不进入分母。
- **Reviews:** 20/20 20+ owners拥有非模板化Full Source Review；24/24低分/blocked owners拥有身份、日期、六维分数与拒绝/材料closure；`Review Pending = 0`。
- **Dedup:** 44个W40 Source Family ID与primary identifier唯一；22/22 W39 spillbacks全部排除于W40评分；DeepSeek revision与later revisions未重复计分。
- **Evidence boundary:** vendor/author benchmark均绑定已披露workload；未披露项没有被推断；Self-Forcing++保持blocked。
- **Structure:** 3/3 Deep Analyses；Stable Node owner、handoff、Books Gate与Historical Daily policy一致。
- **Gate result:** `Weekly Evidence Gate Passed with 1 explicit blocked-skip material request`; `Historical Books Gate Closed`；因Self-Forcing++材料请求与W39 spillback reconciliation仍显式存在，本文件不宣称Archive Completion。

## Sources

- DeepSeek-V3.2-Exp — https://api-docs.deepseek.com/news/news250929/ ; https://github.com/deepseek-ai/DeepSeek-V3.2-Exp （First Public: 2025-09-29；Accessed: 2026-08-24）
- SANA-Video — https://arxiv.org/html/2509.24695 ; RL Skill Composition — https://arxiv.org/html/2509.25123 ; DataMind — https://arxiv.org/html/2509.25084 （Accessed: 2026-08-24）
- Socratic-Zero — https://arxiv.org/html/2509.24726 ; AgentDebug — https://arxiv.org/html/2509.25370 ; GRPO-MA — https://arxiv.org/html/2509.24494 （Accessed: 2026-08-24）
- Dragon Hatchling — https://arxiv.org/html/2509.26507 ; Vision-Zero — https://arxiv.org/html/2509.25541 ; dParallel — https://arxiv.org/html/2509.26488 （Accessed: 2026-08-24）
- DeepSearch — https://arxiv.org/html/2509.25454 ; GEM — https://arxiv.org/html/2510.01051 ; VLA-RFT — https://arxiv.org/html/2510.00406 （Accessed: 2026-08-24）
- RL Dynamics — https://arxiv.org/html/2510.00553 ; LongCodeZip — https://arxiv.org/html/2510.00446 ; ExGRPO — https://arxiv.org/html/2510.02245 （Accessed: 2026-08-24）
- Ovi — https://arxiv.org/html/2510.01284 ; TOUCAN — https://arxiv.org/html/2510.01179 ; Scaling Agents — https://arxiv.org/html/2510.02250 ; Hallucination Span — https://arxiv.org/html/2510.02173 （Accessed: 2026-08-24）
- EasySteer — https://arxiv.org/abs/2509.25175 ; ROVER — https://arxiv.org/abs/2509.24981 ; SCI-Verifier — https://arxiv.org/abs/2509.24285 （Accessed: 2026-08-24）
- More Thought — https://arxiv.org/abs/2509.25848 ; Muon — https://arxiv.org/abs/2509.26030 ; DeepScientist — https://arxiv.org/abs/2509.26603 （Accessed: 2026-08-24）
- Attention Compass — https://arxiv.org/abs/2509.26628 ; Regression LM — https://arxiv.org/abs/2509.26476 ; TTT — https://arxiv.org/abs/2509.24510 （Accessed: 2026-08-24）
- Knapsack RL — https://arxiv.org/abs/2509.25849 ; Beyond Log Likelihood — https://arxiv.org/abs/2510.00526 ; MixtureVitae — https://arxiv.org/abs/2509.25531 （Accessed: 2026-08-24）
- StockBench — https://arxiv.org/abs/2510.02209 ; F2LLM — https://arxiv.org/abs/2510.02294 ; Interactive Training — https://arxiv.org/abs/2510.02297 （Accessed: 2026-08-24）
- ModernVBERT — https://arxiv.org/abs/2510.01149 ; Red-Team RPO — https://arxiv.org/abs/2510.02286 ; CLUE — https://arxiv.org/abs/2510.01591 （Accessed: 2026-08-24）
- RewardMap — https://arxiv.org/abs/2510.02240 ; Aristotle — https://arxiv.org/abs/2510.01346 ; SQA — https://arxiv.org/abs/2510.01817 （Accessed: 2026-08-24）
- VOGUE — https://arxiv.org/abs/2510.01444 ; DrBench — https://arxiv.org/abs/2510.02190 ; Self-Forcing++ — https://arxiv.org/abs/2510.02283 （Accessed: 2026-08-24）
- RLP spillback — https://arxiv.org/abs/2510.01265 （v1: 2025-09-26；Accessed: 2026-08-24）
- HF discovery — https://huggingface.co/papers/date/2025-09-29 ; https://huggingface.co/papers/date/2025-09-30 ; https://huggingface.co/papers/date/2025-10-01 ; https://huggingface.co/papers/date/2025-10-02 ; https://huggingface.co/papers/date/2025-10-03 （Discovery only；Accessed: 2026-08-24）
