# AI Research Weekly — 2025-W38

> Coverage Window: 2025-09-15～2025-09-21
> Research Mode: Retrospective Backfill / Full Discovery Replay
> First-public Ownership Cutoff: 2025-09-21 23:59:59 UTC
> Accessed: 2026-08-24
> Rebuilt: 2026-08-24
> Weekly Evidence Gate: Passed — 88-row Full Discovery Replay and W39 Look-ahead Reconciliation
> Historical Books Gate: Closed

## Executive Summary

本周按“模型与研究机构 → arXiv / 学术来源 → AI Infra 与工程项目”重放 discovery，并以 2025-09-18～2025-09-21 submission feeds、W39 look-ahead 与 owner-date 交叉检查推翻了原 50-row 快照。最终分母为 88 个唯一 Source Family：48 个 `20+` 候选均完成非模板化 Full Source Review，40 个低分候选均完成来源、v1 日期、评分与拒绝闭环；普通 `Review Pending`、`Unverified / Blocked` 与 `Disputed` 均为 0。

本周最重要的长期系统信号不是某个孤立 benchmark，而是四条相互关联的设计演进：

1. **训练与压缩必须匹配真实执行分布。** Reasoning-Aware Compression 把校准分布从 prompt 扩展到 on-policy reasoning trace；Synthetic Bootstrapped Pretraining 则把“复读旧数据”推进到显式生成跨文档关系的新训练对象。
2. **推理扩展从同步重复采样转向可中断的异步资源分配。** ATTS 以 conformal stopping 把 target-model verification 变成可提前终止的控制流；opportunistic GPU inference 把中间上下文变成跨磁盘、RAM 与 GPU 的可迁移状态。
3. **可靠性从最终答案评分推进到过程、图结构与权限边界。** Graph confidence、TDRM、FAMAS 和 participant-aware ACL 分别把 confidence、reward、failure attribution 与 authorization 绑定到明确状态对象。
4. **资源抽象开始承认运行期健康与可消费容量。** Kubernetes DRA health/capacity 证明 allocation contract 可以向 runtime observation 与多维 accounting 演进，但 request 仍不等于隔离和 enforcement。
5. **后半周补齐了三个此前被静默遗漏的 owner 链。** RPG、SWE-Bench Pro、ARE 与 AgentSeer 把 agent workflow、可执行评测和 action-graph security 连成一条证据链；MANZANO、Ask-to-Clarify、VLAC 与 RoE 分别补足 native multimodal、physical action loop 与 MoE inference scaling；BaseReward、HAPO、SMART 和 MCTS-EP 则显示 reward signal、uncertainty 与 exploration policy 必须联合审计。

所有论文性能数字均保持作者实验边界；框架、硬件、模型、精度、长度、batch、并发或 SLO 未披露时明确记录 `Not Disclosed`。本轮只闭合 Weekly 证据体系，不修改 Books。

## Coverage Window and Limitations

- ISO 周窗口复核为 Monday 2025-09-15 至 Sunday 2025-09-21；arXiv 以 v1 UTC timestamp 归档，官方发布以页面首次公开日期归档。
- 固定来源顺序已重放：模型公司与一线研究机构；arXiv 与学术 metadata；PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime、OpenXLA。
- Google Scholar、OpenAlex、DBLP、Semantic Scholar 与 Crossref 只用于 discovery、身份与重复关系交叉检查；技术结论均回到论文全文、官方 Blog、system card、repository documentation 或 API 文档。
- 所有 `20+` 论文阅读覆盖 metadata、revision history、Abstract、Introduction、Related Work、Method/公式、Implementation、Evaluation、baseline、ablation、limitations、关键 Appendix 与公开 artifact；低分候选至少核验 identity、v1 日期及支持拒绝判断的 method/evaluation scope。无公开字段不推断。
- 2025-09-18～2025-09-21 的 arXiv submission/recommendation feeds 已逐日重放，并以 W39 前瞻清单反查 owner；共恢复 38 个漏项，其中 21 个达到 `20+` 并全文审计，17 个以低分 closure 关闭。发现页只负责召回，所有技术结论均回到 arXiv 正文或公开 artifact。
- Historical Backfill 不补造 Daily；后续 revision 只用于理解机制和限制，不改变 first-public owner。
- DeepSeek-R1 的 Nature 正式发表、以及若干在本周被再次传播的旧论文，均保留为 revision/spillback，不在 W38 重复计分。

## 1. 模型与研究机构

### Source Coverage

- **OpenAI:** GPT-5-Codex release 与 system-card addendum（2025-09-15）形成“长时 agentic coding + sandbox/network control + evaluation boundary”的版本证据。
- **Alibaba / FunAudioLLM:** Fun-ASR v1（2025-09-15）形成“data/model scaling → LLM integration → RL → production ASR constraints”的系统案例；后续 v2～v4 不改变 W38 owner。
- Anthropic、Google DeepMind、Meta AI、Microsoft Research、NVIDIA、Mistral、Cohere、DeepSeek、Qwen、Moonshot、ByteDance、Baidu、Tencent、Huawei、Hugging Face 官方源按固定顺序检查；未发现另一个能在本周建立独立、可核验机制 owner 的高分事件。

## 2. 论文与学术来源

### Source Coverage

- 2025-09-15：核验 multimodal preference hijacking、reasoning-aware pruning、speech-language preservation、RAG-like role-play、MedicalOS 与 embodied pointing。
- 2025-09-16：核验 legal-critical agentic software、graph confidence、hierarchical reflection、opportunistic GPU inference，以及 reasoning cost、prompt-injection defense、reversible DEQ、black-box model merging、federated personalization、token-level DP、radiology scaling 与 HPIM。
- 2025-09-17：核验 synthetic bootstrapped pretraining、process-supervised tool-use RL、MAS failure attribution、industrial GUI agent、decode-time hallucination suppression，以及 prosociality、curriculum tuning、prompt stability、controlled generation、jailbreak、ternary edge inference、autonomous driving 与 VC benchmark。
- 2025-09-18：除原有 mixed-precision quantization、reward-distribution RL、XR security、TD reward modeling、infinite-compute pretraining、asynchronous test-time scaling、PIM-NoC inference、participant-aware ACL 与 near-free jailbreak detection 外，补核 Ask-to-Clarify、convolutional diffusion decoding、Robot Control Stack、multi-agent diagnostics、multimodal spurious-signal debiasing、SmolRGPT 与 explainable supervisory control。
- 2025-09-19：补核 RPG、MANZANO、BaseReward 与 VLAC，分别覆盖 repository planning graph、native multimodal token space、multimodal reward modeling 与 real-world VLA critic。
- 2025-09-20：补核 HAPO、audio-conditioned diffusion LM、FESTA、NUMINA、SMART、decoding uncertainty、Roundtable Policy、M-Spoiler、prompt-driven video editing 与 nursing-skills assessment。
- 2025-09-21：补核 ARE、SWE-Bench Pro、seqBench、audio-visual navigation、strategic-intelligence governance、MCTS-EP、wargame review、RoE、systematic-review agents、AgentSeer、combinatorial-optimization solvers、LaySPA、Quantum Abduction、KAHAN、landmark graph、RALLM-POI 与 hierarchical trajectory diffusion。

## 3. AI Infra 与工程项目

### Source Coverage

- **PyTorch / TorchAO:** PT2 compilation-time reduction（2025-09-18）、Intel CPU quantized LLM inference（2025-09-17）与 Hugging Face TorchAO quantization recipes（2025-09-19）。
- **Kubernetes:** DRA resource health（2025-09-17）与 consumable capacity（2025-09-18），并与 W35 core DRA GA、W36 API details 去重。
- 其余工程项目 release、RFC、PR 与文档已按固定顺序检查；没有把常规 patch、价格、兼容性列表或缺机制的功能公告提升为候选。

## Candidate Scoring

评分顺序为 Technical Novelty / System Impact / Practical Value / Source Reliability / Project Relevance / Longevity。

| # | Candidate | First Public | Source Family ID | TN | SI | PV | SR | PR | L | Total | Final Disposition |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | GPT-5-Codex | 2025-09-15 | `OPENAI-GPT5-CODEX-20250915` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Weekly Only — Version Fact / Mechanism Partially Disclosed |
| 2 | Fun-ASR Technical Report | 2025-09-15 | `ARXIV-2509.12508` | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Emerging / Experimental |
| 3 | Phi: Preference Hijacking | 2025-09-15 | `ARXIV-2509.12521` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 4 | Reasoning-Aware Compression | 2025-09-15 | `ARXIV-2509.12464` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 5 | C3T speech-language preservation benchmark | 2025-09-15 | `ARXIV-2509.12171` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Narrow Evaluation Evidence |
| 6 | RAGs to Riches | 2025-09-15 | `ARXIV-2509.12168` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Role-play Case Study |
| 7 | MedicalOS | 2025-09-15 | `ARXIV-2509.11507` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Workflow Evidence |
| 8 | Learning to Generate Pointing Gestures | 2025-09-15 | `ARXIV-2509.12507` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Narrow Embodied Case |
| 9 | Legal-Critical Software / Synedrion | 2025-09-16 | `ARXIV-2509.13471` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 10 | Graph-Based Confidence Estimation | 2025-09-16 | `ARXIV-2509.12908` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 11 | H2R: Hierarchical Hindsight Reflection | 2025-09-16 | `ARXIV-2509.12810` | 4 | 4 | 3 | 5 | 5 | 4 | 25/30 | Books Pending — Integration Deferred |
| 12 | Opportunistic GPU Inference with Pervasive Context Management | 2025-09-16 | `ARXIV-2509.13201` | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 13 | LLMs Imitate Logical Reasoning, but at what Cost? | 2025-09-16 | `ARXIV-2509.12645` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Diagnostic Study Only |
| 14 | Multi-Agent LLM Defense Pipeline Against Prompt Injection | 2025-09-16 | `ARXIV-2509.14285` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Defense Composition Case |
| 15 | Reversible Deep Equilibrium Models | 2025-09-16 | `ARXIV-2509.12917` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Architecture-Specific |
| 16 | Black-box Model Merging for LMaaS | 2025-09-16 | `ARXIV-2509.12951` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Early Repository Case |
| 17 | Bi-level Personalization for Federated Foundation Models | 2025-09-16 | `ARXIV-2509.12697` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Narrow Federated Case |
| 18 | Token-Level Differential Privacy in Memory Sculpting | 2025-09-16 | `ARXIV-2509.12958` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Continual-Learning Case |
| 19 | Data Scaling Laws for Radiology Foundation Models | 2025-09-16 | `ARXIV-2509.12818` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Domain-Specific Scaling |
| 20 | HPIM Accelerator | 2025-09-16 | `ARXIV-2509.12993` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Simulator-Only Accelerator Case |
| 21 | Synthetic Bootstrapped Pretraining | 2025-09-17 | `ARXIV-2509.15248` | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Books Pending — Integration Deferred |
| 22 | Process-Supervised RL for Tool-Use Agents | 2025-09-17 | `ARXIV-2509.14480` | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Integration Deferred |
| 23 | FAMAS Failure Attribution | 2025-09-17 | `ARXIV-2509.13782` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 24 | InfraMind | 2025-09-17 | `ARXIV-2509.13704` | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Emerging / Experimental |
| 25 | DSCC-HS | 2025-09-17 | `ARXIV-2509.13702` | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 | Emerging / Experimental |
| 26 | Prosocial Ability Profiles of Multi-Agent Populations | 2025-09-17 | `ARXIV-2509.14485` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Evaluation Case Only |
| 27 | CAMPUS Curriculum Instruction Tuning | 2025-09-17 | `ARXIV-2509.13790` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Training Schedule Case |
| 28 | PromptSE | 2025-09-17 | `ARXIV-2509.13680` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Narrow Robustness Metric |
| 29 | AgentCTG | 2025-09-17 | `ARXIV-2509.13677` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Multi-Agent Wrapper Case |
| 30 | Helpfulness-Exploiting Jailbreak | 2025-09-17 | `ARXIV-2509.14297` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Attack Variant |
| 31 | TENET Ternary Edge Inference | 2025-09-17 | `ARXIV-2509.13765` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Architecture-Specific |
| 32 | FlowDrive | 2025-09-17 | `ARXIV-2509.14303` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Model Case |
| 33 | VCBench | 2025-09-17 | `ARXIV-2509.14448` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Benchmark |
| 34 | CoopQ | 2025-09-18 | `ARXIV-2509.15455` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 35 | FlowRL | 2025-09-18 | `ARXIV-2509.15207` | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 36 | Evil Vizier | 2025-09-18 | `ARXIV-2509.15213` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 37 | TDRM | 2025-09-18 | `ARXIV-2509.15110` | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |
| 38 | Pre-training under Infinite Compute | 2025-09-18 | `ARXIV-2509.14786` | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | Emerging / Experimental |
| 39 | ATTS | 2025-09-18 | `ARXIV-2509.15148` | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Integration Deferred |
| 40 | LEAP PIM-NoC Inference | 2025-09-18 | `ARXIV-2509.14781` | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Books Pending — Integration Deferred |
| 41 | Participant-Aware Access Control | 2025-09-18 | `ARXIV-2509.14608` | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Books Pending — Integration Deferred |
| 42 | LLM Jailbreak Detection for (Almost) Free | 2025-09-18 | `ARXIV-2509.14558` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 43 | DeepRefusal | 2025-09-18 | `ARXIV-2509.15202` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Safety Fine-tuning Case |
| 44 | Generalizable Geometric Image Caption Synthesis | 2025-09-18 | `ARXIV-2509.15217` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Data Synthesis Case |
| 45 | Black-box Layers via Low-rank Surrogate Optimization | 2025-09-18 | `ARXIV-2509.15113` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Specialized Optimizer Case |
| 46 | Ask-to-Clarify: Vision-Language-Action Model with Clarification | 2025-09-18 | `ARXIV-2509.15061` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 47 | Fast and Fluent Diffusion LMs via Convolutional Decoding | 2025-09-18 | `ARXIV-2509.15188` | 5 | 4 | 4 | 5 | 4 | 4 | 26/30 | Books Pending — Integration Deferred |
| 48 | Robot Control Stack | 2025-09-18 | `ARXIV-2509.14932` | 4 | 4 | 5 | 5 | 3 | 3 | 24/30 | Emerging / Experimental |
| 49 | Cognitive-Failure Diagnostics for Multi-Agent Expert Systems | 2025-09-18 | `ARXIV-2509.15366` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Narrow Diagnostic Workflow |
| 50 | Beyond Spurious Signals in Multimodal Learning | 2025-09-18 | `ARXIV-2509.15361` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Task-Specific Debiasing Case |
| 51 | SmolRGPT | 2025-09-18 | `ARXIV-2509.15490` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Small Domain VLM Case |
| 52 | Explainable Supervisory Control | 2025-09-18 | `ARXIV-2509.15491` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Control Case |
| 53 | RPG: Repository Planning Graph | 2025-09-19 | `ARXIV-2509.16198` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 54 | MANZANO | 2025-09-19 | `ARXIV-2509.16197` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 55 | BaseReward | 2025-09-19 | `ARXIV-2509.16127` | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 56 | VLAC: Vision-Language-Action-Critic | 2025-09-19 | `ARXIV-2509.15937` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 57 | M-Spoiler | 2025-09-20 | `ARXIV-2509.16494` | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Emerging / Experimental |
| 58 | HAPO | 2025-09-20 | `ARXIV-2509.16591` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 59 | Audio-Conditioned Diffusion Language Models for ASR | 2025-09-20 | `ARXIV-2509.16622` | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Pending — Integration Deferred |
| 60 | FESTA | 2025-09-20 | `ARXIV-2509.16648` | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | Emerging / Experimental |
| 61 | NUMINA | 2025-09-20 | `ARXIV-2509.16656` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Benchmark |
| 62 | Decoding Uncertainty | 2025-09-20 | `ARXIV-2509.16696` | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | Emerging / Experimental |
| 63 | SMART: Sycophancy Mitigation via Adaptive RL | 2025-09-20 | `ARXIV-2509.16742` | 4 | 5 | 4 | 5 | 4 | 4 | 26/30 | Books Pending — Integration Deferred |
| 64 | Roundtable Policy | 2025-09-20 | `ARXIV-2509.16839` | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | Emerging / Experimental |
| 65 | End-to-End Combinatorial Optimization Solvers | 2025-09-21 | `ARXIV-2509.16865` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Optimization Case |
| 66 | seqBench | 2025-09-21 | `ARXIV-2509.16866` | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | Emerging / Experimental |
| 67 | Audio-Visual Navigation with Stereo Attention | 2025-09-21 | `ARXIV-2509.16924` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Navigation Case |
| 68 | SWE-Bench Pro | 2025-09-21 | `ARXIV-2509.16941` | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Books Pending — Integration Deferred |
| 69 | Governing Automated Strategic Intelligence | 2025-09-21 | `ARXIV-2509.17087` | 3 | 3 | 2 | 5 | 3 | 2 | 18/30 | Reject — Preliminary Governance Review |
| 70 | MCTS-EP | 2025-09-21 | `ARXIV-2509.17116` | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Books Pending — Integration Deferred |
| 71 | ARE: A Research Environment for Agentic Systems | 2025-09-21 | `ARXIV-2509.17158` | 5 | 5 | 5 | 5 | 4 | 4 | 28/30 | Books Pending — Integration Deferred |
| 72 | Shall We Play a Game? | 2025-09-21 | `ARXIV-2509.17192` | 3 | 3 | 2 | 5 | 3 | 2 | 18/30 | Reject — Revision-Sensitive Scoping Review |
| 73 | RoE: Routing of Experts for Hyper-Parallel MoE Inference | 2025-09-21 | `ARXIV-2509.17238` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 74 | Can Agents Judge Systematic Reviews Like Humans? | 2025-09-21 | `ARXIV-2509.17240` | 3 | 3 | 2 | 5 | 3 | 2 | 18/30 | Reject — Domain Evaluation Case |
| 75 | Mind the Gap / AgentSeer | 2025-09-21 | `ARXIV-2509.17259` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Books Pending — Integration Deferred |
| 76 | Prompt-Driven Agentic Video Editing | 2025-09-20 | `ARXIV-2509.16811` | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Emerging / Experimental |
| 77 | AI-assisted Nursing Skills Assessment | 2025-09-20 | `ARXIV-2509.16810` | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Reject — Synthesized Domain Workflow |
| 78 | LLMs as Layout Designers / LaySPA | 2025-09-21 | `ARXIV-2509.16891` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Layout Optimization |
| 79 | Quantum Abduction | 2025-09-21 | `ARXIV-2509.16958` | 3 | 2 | 2 | 5 | 3 | 2 | 17/30 | Reject — Conceptual Case Studies |
| 80 | KAHAN Financial Data Narration | 2025-09-21 | `ARXIV-2509.17037` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Narration Workflow |
| 81 | Domain-Landmark Graph Learning | 2025-09-21 | `ARXIV-2509.17062` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Classical Planning Case |
| 82 | RALLM-POI | 2025-09-21 | `ARXIV-2509.17066` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Retrieval Case |
| 83 | Intention-aware Hierarchical Diffusion for Trajectory Anomaly Detection | 2025-09-21 | `ARXIV-2509.17068` | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Reject — Domain Anomaly Case |
| 84 | Native PyTorch Quantized LLM Inference on Intel CPUs | 2025-09-17 | `PYTORCH-INTEL-CPU-QUANT-20250917` | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Books Pending — Integration Deferred |
| 85 | Reducing PT2 Compilation Time for Meta Workloads | 2025-09-18 | `PYTORCH-PT2-COMPILE-TIME-20250918` | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Books Pending — Integration Deferred |
| 86 | TorchAO Quantized Models and Recipes on Hugging Face | 2025-09-19 | `PYTORCH-TORCHAO-HF-20250919` | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 87 | DRA Resource Health in Pod Status | 2025-09-17 | `K8S-DRA-RESOURCE-HEALTH-20250917` | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Books Pending — Integration Deferred |
| 88 | DRA Consumable Capacity | 2025-09-18 | `K8S-DRA-CONSUMABLE-CAPACITY-20250918` | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Books Pending — Integration Deferred |

### Scoring Ledger

- Total candidates: 88
- `25～30`: 38
- `20～24`: 10
- `<20`: 40
- Retained rows (`20+`): 48
- Unique retained source families: 48
- Full Source Reviews: 48/48
- Low-score closures: 40/40
- Review Pending: 0
- Unverified / Blocked: 0

## Deep Analysis

### 1. Synthetic Bootstrapped Pretraining：从重复语料到关系合成

**Why → Principle.** 当新增高质量文本逐渐稀缺，简单重复训练数据可以增加 optimization exposure，却不能增加文档之间原本没有显式写出的关系。论文把瓶颈重新定义为“训练对象是否创造了新的可学习关系”，而不只是 token 数量。

**Mechanism.** 系统从文档集合中抽取跨文档关系，以 synthesizer 生成显式连接这些关系的新文本，再把原始与 synthetic documents 混合预训练。状态 owner 从单篇文档扩展到“source-document set + relation specification + derived document provenance”。

**Trade-off / Evidence.** 作者在 compute-matched 3B 模型、最高 1T token 设置中报告收益，并用重复语料与 20× unique-data oracle 分离“更多 exposure”与“更多关系”的作用。但 synthesizer 偏差、污染、provenance 与额外生成成本仍是新 failure mode；作者实验不证明任意模型规模、语种或生产数据管线都能复现。

**Connection / Evolution.** 这是 `TRAIN-DATA → TRAIN-PRETRAINING` 的 direct evolution：raw corpus → dedup/mixture → repeated data → relationship-aware derived data。旧的去重和数据混合仍是基础，synthetic relation data 不能替代来源治理。

### 2. ATTS：从同步 Test-Time Scaling 到可提前停止的异步验证

**Why → Principle.** 同步 rejection sampling 让昂贵 target model 验证所有候选，吞吐被最慢路径和固定 sample budget 锁死。若 verifier 可以给出有覆盖保证的置信集合，就能把“是否继续算”变成显式 control-plane decision。

**Mechanism.** draft models 并行产生候选，target model 对候选执行分阶段 rejection sampling；conformal prediction 根据校准分数决定接受、继续验证或回退。核心状态不是一个最终答案，而是 candidate set、calibration state、accept/reject decision 与剩余 compute budget。

**Trade-off / Evidence.** 作者在数学推理任务上报告相对 target-only scaling 的最高 56.7× latency speedup 与 4.14× throughput，但结果依赖 draft/target 组合、校准分布、coverage level 与 workload；它不是通用 serving SLO。收益来自少做 target work，代价是校准失配、coverage 退化、并行资源占用和更复杂的 decision trace。

**Connection / Evolution.** 它与 speculative decoding 是 `Principle Reuse` 而非同一算法：都用便宜 proposal 减少昂贵 verification，但 ATTS 的 commit unit 是 solution candidate，验证语义是统计 coverage，而非 token exactness。

### 3. DRA Consumable Capacity：从设备所有权到可计量共享

**Why → Principle.** exclusive allocation 容易解释和隔离，却不能表达 time-slicing、bandwidth 或 memory/compute share；“允许多个 Pod 指向同一设备”又缺少可验证的容量约束。DRA 把共享推进为 driver-declared quantities 与 scheduler accounting。

**Mechanism.** driver 在 ResourceSlice 中声明可消费 capacity；ResourceClaim 按 default/min/step 等 policy 请求数量，scheduler 对 allocation 做累计约束，driver 再负责 prepare 与 runtime enforcement。由此明确分开 inventory、admission accounting 与实际隔离三个 owner。

**Trade-off / Evidence.** 官方 alpha API 证明表达与调度 contract 存在，不证明 GPU compute、memory、bandwidth 可以压成单一标量，也不证明 driver 能提供 QoS。灵活性换来 fragmentation、noisy neighbor、accounting drift 与 recovery reconciliation。

**Connection / Evolution.** `exclusive device → pre-partitioned slice → consumable capacity` 是 direct evolution；strict latency 或 hard isolation workload 仍应保留 exclusive/MIG/static partition 分支。

## Full Source Review

### 1. GPT-5-Codex

- **Candidate / Week / Score / Source Family / Type:** GPT-5-Codex / 2025-W38 / 26/30 / `OPENAI-GPT5-CODEX-20250915` / official release + system-card addendum。
- **Event Date / Revision / Sources / Access:** 2025-09-15 首次公开；direct sources 为 OpenAI product announcement 与 GPT-5-Codex system-card addendum；两份官方材料均可访问并全文核验。公开证据说明版本行为与安全控制，不披露完整训练配方、数据、内部 architecture 或 serving runtime。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 已读 release、evaluation、cyber/bio/safety、sandbox/network 与 limitations。短回合 code completion/聊天对交互式重构曾合理；repo-scale、长时 tool use、测试循环与 code review 把任务变成持续 stateful workflow。
- **Mechanism / State Ownership / Flow / Implementation:** 官方描述为针对真实 coding tasks 的 reinforcement learning 与动态调整 reasoning time；agent 读取 repository、修改文件、运行 tests 后迭代。模型持有当前 reasoning/context，Codex harness 持有 workspace、tool permissions、sandbox/network policy 与 action log；内部 optimizer、rollout pipeline 和 exact runtime 未公开。
- **Evaluation Contract / Workload:** 官方列出 SWE-bench Verified、code refactoring 与 cyber safety 等 evaluation；model=GPT-5-Codex，hardware、precision、batch、serving concurrency 与 latency SLO `Not Disclosed`。system card 证明特定评测/mitigation 结果，不证明任意 repository、组织流程或自治级别。
- **Proof Boundary / Limitations / Threats:** 可证明这是面向 agentic coding 的官方模型版本并带 sandbox/network control；不能由产品行为反推内部训练或推理机制。风险包括 prompt injection、错误修改、网络外传、长时 error accumulation 与 evaluator coverage gap。
- **Trade-offs / Previous Boundary / Evolution:** 更长 reasoning 与 tool loop 提高复杂任务覆盖，却增加 latency、cost、权限面和 recovery burden；小而确定的编辑仍适合普通 completion。Evolution 为 `Layering / Dependency`：coding model → tool-using coding agent → policy-bounded workflow。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `AGENT-PLATFORM` Ch84，Legacy Ch80；handoff `AGENT-TOOL-CALLING` Ch78 与 `PLATFORM-SECURITY` Ch72。现有书稿已覆盖 tool/runtime separation 与 least privilege；最终 disposition 为 `Weekly Only — Version Fact / Mechanism Partially Disclosed`，本轮不改 Books。Open: 长时任务如何量化 rollback、human review 与 sandbox escape risk？

### 2. Fun-ASR Technical Report

- **Candidate / Week / Score / Source Family / Type:** Fun-ASR Technical Report / 2025-W38 / 25/30 / `ARXIV-2509.12508` / arXiv technical report + public code/model links。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-15，v2 2025-09-17，v3 2025-10-05，v4 2025-12-19；owner 固定 W38。HTML/PDF、method、evaluation 与 artifact 索引已核验；使用 later revision 只补充限制，不改事件日期。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 已读 ASR scaling、LLM integration、RL、streaming/noise/code-switch/hotword、benchmarks 与 limitations。传统 encoder-decoder/CTC 在标准 ASR 与低延迟上合理；真实工业语音同时要求语言理解、鲁棒性、可定制与低幻觉。
- **Mechanism / State Ownership / Flow / Implementation:** speech encoder 将音频映射到语言模型条件表示，LLM 建模 transcript/semantics，训练组合大规模监督数据与 RL；streaming、noise robustness、code-switch 与 hotword 是部署层分支。audio frontend 拥有声学状态，LLM 拥有语言生成状态，runtime 拥有 chunk/cache 与 latency policy。
- **Evaluation Contract / Workload:** 作者在公开与内部工业 ASR sets 上比较多类系统，并报告 streaming/robustness；精确生产硬件、precision、batch、concurrency、端到端 SLO 和部分数据构成 `Not Disclosed`。公开结果是作者实验，不是跨语种/场景通用结论。
- **Proof Boundary / Limitations / Threats:** 证明“benchmark 强并不等于工业 ASR 强”，以及 LLM-ASR 需要把 hallucination/streaming/hotword 放入同一 contract；不证明规模、LLM 或 RL 各自是唯一因果来源。私有集、数据规模与组件耦合限制可复现性。
- **Trade-offs / Previous Boundary / Evolution:** language modeling 可改善语义与长尾词，却可能生成声学证据不支持的文本；streaming 降 latency 会减少右上下文。旧式 CTC/transducer 在严格实时、可解释对齐和有限域仍合理。Evolution 为 `Alternative Branch` 而非替代全部 ASR。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `MULTIMODAL-REPRESENTATION` Ch23，Legacy N/A；handoff `PLATFORM-EVALUATION-SYSTEM` Ch66 与 `INFER-DECODE` Ch44。现有章节已有 modality boundary，但缺 ASR evidence-bound generation 的完整比较；最终 `Emerging / Experimental`，本轮不改 Books。Open: 私有 industrial set、端到端 RTF、WER/semantic accuracy 与 hallucination policy 如何共同校准？

### 3. Phi: Preference Hijacking in Multi-modal Large Language Models at Inference Time

- **Candidate / Week / Score / Source Family / Type:** Phi / 2025-W38 / 26/30 / `ARXIV-2509.12521` / arXiv research paper + author code。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-15，无后续 revision；HTML、PDF、method、algorithm、experiments、appendix 与 repository link 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 已读 threat model、DPO-style objective、PGD optimization、universal patch/border、transfer 与 defenses。只检测 overtly harmful images/text 曾合理；但视觉条件可在不显眼改变语义的情况下操纵模型 response preference。
- **Mechanism / State Ownership / Flow / Implementation:** white-box adversary 对输入图像做 PGD，使 chosen/rejected response log-probability gap 朝攻击偏好移动；universal perturbation 可嵌入不同图像。attacker 拥有 pixel perturbation，model 拥有 multimodal representation/decoder preference，application policy 若只看文本会错过输入侧控制。
- **Evaluation Contract / Workload:** LLaVA-1.5-7B、Llama-3.2-11B、Qwen2.5-VL-7B；A6000/A100；10k iterations、batch 2、gradient accumulation 8、扰动上限 16/255，并以 GPT-4o judge 等评估。serving concurrency/SLO 不适用或未披露。
- **Proof Boundary / Limitations / Threats:** 证明所测 white-box MLLM 可被优化图像改变偏好且存在 universal component；不证明黑盒、所有模型或现实摄像链路同样脆弱，也不证明 judge 等价于人类影响。transfer、物理世界和 defense coverage 受限。
- **Trade-offs / Previous Boundary / Evolution:** 输入过滤与输出 moderation 仍必要，但不足以覆盖 latent preference manipulation；鲁棒检测增加 latency/false positive，重编码可能损失任务信息。Evolution 为 `Layering / Dependency`：content safety → multimodal integrity → preference-control provenance。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-SECURITY` Ch72，handoff `MULTIMODAL-REPRESENTATION` Ch23；Legacy Ch68。书稿已有 prompt injection 与 provenance，但视觉 perturbation 对 preference 的控制链尚需 later Gate 比较；最终 `Books Pending — Integration Deferred`。Open: black-box transfer、physical robustness 与 acceptable false-positive operating point？

### 4. Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction

- **Candidate / Week / Score / Source Family / Type:** Reasoning-Aware Compression / 2025-W38 / 26/30 / `ARXIV-2509.12464` / arXiv research paper + code。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-15，v2 2026-05-02；HTML/PDF、公式、SparseGPT/ALPS/WANDA integration、experiments、ablation、appendix 与 code link 已核验；owner 仍为 W38。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 传统 post-training pruning 用 prompt activations 校准，对 next-token LM 曾合理；reasoning workload 的大部分 compute 与 activation distribution 出现在模型自己生成的长 CoT，prompt-only calibration 产生 distribution mismatch。
- **Mechanism / State Ownership / Flow / Implementation:** RAC 先从原模型采样 on-policy CoT，再把 prompt 与 reasoning activations 一起用于 layer-wise reconstruction/pruning；可作为 SparseGPT 等流程的 drop-in calibration change。teacher model 拥有 trace generator，compression pipeline 拥有 calibration corpus/masks，serving runtime 只消费稀疏权重。
- **Evaluation Contract / Workload:** Qwen3 等 reasoning models、50% sparsity 等设置，覆盖 math/reasoning 与生成 token length；作者比较 prompt-only 与 CoT-aware calibration并做方法/trace ablation。GPU、precision、serving batch/concurrency/SLO 并非所有实验均披露，不把 accuracy 或 token 数外推为 fleet throughput。
- **Proof Boundary / Limitations / Threats:** 证明 calibration distribution 对 reasoning pruning 重要，且所测方法可减少 accuracy/length regression；不证明稀疏 kernel 在任意硬件获得 wall-clock speedup，也不证明 sampled CoT 覆盖生产分布。later v2 不可伪装成 v1 已有证据。
- **Trade-offs / Previous Boundary / Evolution:** 额外生成 CoT 增加压缩成本、数据与 privacy footprint；错误 teacher traces 会固化偏差。短回答或非-reasoning model 仍可用 prompt-only calibration。Evolution 为 `Direct Evolution`：weight-only reconstruction → workload-aware activation reconstruction。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-TENSORRT-LLM` Ch49，handoff `INFER-DECODE` Ch44 与 `PLATFORM-MODEL-REGISTRY` Ch59；Legacy Ch45/40/55。现有书稿已有 execution-plan/workload contract；最终 `Books Pending — Integration Deferred`。Open: accuracy、reasoning length、kernel sparsity 与端到端成本应如何联合验收？

### 5. An LLM Agentic Approach for Legal-Critical Software

- **Candidate / Week / Score / Source Family / Type:** Legal-Critical Software / Synedrion / 2025-W38 / 26/30 / `ARXIV-2509.13471` / arXiv software-engineering research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-16，v2 为后续 ICSE 2026 revision；HTML/PDF、workflow、higher-order metamorphic testing、six tax publications、experiments 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 手工把法律文本翻译为代码加单元测试在稳定规则和有限范围内合理；tax rules 交叉引用、版本变化且缺少普通 oracle，使单 agent code generation 的静默语义错误不可接受。
- **Mechanism / State Ownership / Flow / Implementation:** Synedrion 将 specification extraction、implementation、review 与 test roles 分离，并以 higher-order metamorphic relations 从法律约束生成可执行检查；legal source/version 拥有规范身份，code artifact 拥有实现，verifier 拥有关系与 verdict，human 拥有 release authority。
- **Evaluation Contract / Workload:** 六份 tax publications，使用 symbolic execution/ground truth 与多模型 agents；作者报告 GPT-4o-mini worst-case failure 约 45%，frontier models 约 9～15%。hardware、precision、serving SLO 不相关或 `Not Disclosed`；这些数字只适用于作者任务/harness。
- **Proof Boundary / Limitations / Threats:** 证明 role separation + executable metamorphic oracle 可暴露 final-output benchmark 漏掉的法律错误；不证明法规解释唯一、生成代码可直接生产使用，或多 agent 必然优于单 agent。法律 ground truth 与 model judge 均可能偏移。
- **Trade-offs / Previous Boundary / Evolution:** 多角色与 symbolic checks 增加 token、latency、orchestration 与 disagreement handling，却提升审计轨迹。稳定、可形式化的小规则仍适合传统 DSL/handwritten implementation。Evolution 为 `Layering / Dependency`：spec → code → executable relations → governed release。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `AGENT-WORKFLOW` Ch81，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66、`PLATFORM-SECURITY` Ch72；Legacy Ch77/62/68。书稿已有 artifact-producing workflow 和 verifier contract；最终 `Books Pending — Integration Deferred`。Open: 法律版本、解释冲突与 human sign-off 如何成为一等 provenance？

### 6. All Roads Lead to Rome: Graph-Based Confidence Estimation

- **Candidate / Week / Score / Source Family / Type:** Graph-Based Confidence Estimation / 2025-W38 / 26/30 / `ARXIV-2509.12908` / arXiv research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-16；HTML/PDF、graph construction、confidence metrics、cascade setup、ablations 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** token probability/self-consistency 对短独立答案曾合理；长 reasoning 的多条轨迹共享中间命题，简单多数票会重复计算相关错误并忽略结构性 convergence/divergence。
- **Mechanism / State Ownership / Flow / Implementation:** 系统采样多条 chains，把语义等价 reasoning steps 合并为 directed graph，并从 topology/paths 派生 confidence；低置信样本再 cascade 到更大模型。sampler 拥有 raw traces，normalizer 拥有 node identity，graph scorer 拥有 confidence，router 拥有 escalation decision。
- **Evaluation Contract / Workload:** MATH500、MMLU-Pro、FOLIO；small/large model cascade，将最不确定约 15% 样本升级到 70B 级模型。hardware、precision、batch、online concurrency 与 SLO `Not Disclosed`；作者结果受 step parser 与 equivalence model 影响。
- **Proof Boundary / Limitations / Threats:** 证明图结构可在所测任务提供有用排序并支持 selective escalation；不证明输出概率是 calibrated truth probability，也不证明 atomic claims 独立。语义合并错误、采样不足与 graph cost 是关键威胁。
- **Trade-offs / Previous Boundary / Evolution:** 更多 samples 与图归一化提高可观察性，却增加 token/latency/cost；单次低风险回答仍可用简单 entropy/self-consistency。Evolution 为 `Direct Evolution`：answer score → independent samples → dependency-aware reasoning graph → abstain/escalate。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `AGENT-REFLECTION` Ch80；Legacy Ch62/76。书稿已明确 atomic claim 不可简单相乘及 evidence graph；最终 `Books Pending — Integration Deferred`，需 later Gate 判定是否 `No Change`。Open: node equivalence error 如何进入 calibration interval，cascade SLO 如何定价？

### 7. H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents

- **Candidate / Week / Score / Source Family / Type:** H2R / 2025-W38 / 25/30 / `ARXIV-2509.12810` / arXiv agent-memory research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-16；HTML/PDF、task/skill reflection hierarchy、memory update、evaluation 与 ablations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 保存完整轨迹或单层 textual reflection 在单一重复任务上合理；多任务 agent 中，case-specific lesson 与可迁移 skill 混在一起会造成 retrieval noise、错误泛化和 memory growth。
- **Mechanism / State Ownership / Flow / Implementation:** H2R 从 episode outcome 生成 task-level hindsight，再聚合为更高层 skill reflection，并在新任务中按层检索；trajectory store 拥有 raw evidence，reflection module 拥有 derived memory，retriever/router 决定何时使用，base model weights 不被等同为 memory。
- **Evaluation Contract / Workload:** 多任务 agent benchmarks，对比 no-reflection、flat reflection 与 hierarchical variants，并报告任务成功与 transfer；hardware、precision、online concurrency、memory latency/SLO `Not Disclosed`。作者结果依赖 evaluator 与任务分布。
- **Proof Boundary / Limitations / Threats:** 证明层级抽象在所测任务优于 flat hindsight；不证明生成 reflection 必然正确、跨域可迁移或长期不漂移。缺少强 provenance/supersession/delete contract 会累积错误策略。
- **Trade-offs / Previous Boundary / Evolution:** abstraction 降低检索噪声，却引入 consolidation cost、over-generalization 与 source-trace disconnect；短任务/低重复环境中不保存或仅保存原轨迹更安全。Evolution 为 `Direct Evolution`：history → episode reflection → hierarchical derived memory。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `AGENT-MEMORY` Ch77，handoff `AGENT-REFLECTION` Ch80、`AGENT-WORKFLOW` Ch81；Legacy Ch73/76/77。书稿已有 derived memory/provenance/supersession；最终 `Books Pending — Integration Deferred`。Open: 如何用 counterevidence 触发反思降级、删除或 rollback？

### 8. Scaling Up Throughput-oriented LLM Inference on Opportunistic GPU Clusters

- **Candidate / Week / Score / Source Family / Type:** Opportunistic GPU Inference / 2025-W38 / 28/30 / `ARXIV-2509.13201` / arXiv systems paper + software integration。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-16；HTML/PDF、Parsl/TaskVine integration、context hierarchy、experiments、failure handling 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 固定 GPU pool 与 task-local model load 对稳定 low-latency serving 合理；吞吐导向 scientific workloads 面临异构、可抢占、短生命周期 workers，重复装载模型/上下文会吞噬有效计算。
- **Mechanism / State Ownership / Flow / Implementation:** pervasive context management 为模型/数据/derived state 建立可重用 identity，并在 disk、host RAM、GPU memory 间分层缓存；scheduler 把 task 派给已有 context 的 opportunistic worker，worker 可被动态创建、回收或驱逐。control plane 持有 context metadata，worker 持有 materialized replica。
- **Evaluation Contract / Workload:** 异构 opportunistic GPU cluster、throughput-oriented inference；作者报告 execution time 由 11.4h 降至 13.1m（98.1%），naive opportunistic solution 比 context-aware 方案差 245.3%。模型/precision/请求长度等依具体实验，非 online latency SLO。
- **Proof Boundary / Limitations / Threats:** 证明复用/迁移 context 能在作者批处理 workload 显著降低重复初始化；不证明 interactive serving tail latency、任意模型或 cloud preemption 条件同样获益。metadata stale、eviction storm、replica corruption 与 locality starvation 是风险。
- **Trade-offs / Previous Boundary / Evolution:** context persistence 换吞吐，但增加 storage、coherence、placement 与 cleanup；稳定低延迟服务仍更适合固定 warm replicas。Evolution 为 `Direct Evolution`：task-local load → worker cache → fleet-visible typed context → state-aware scheduling。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-SCHEDULING` Ch56，handoff `INFER-GPU-MEMORY` Ch54、`PLATFORM-VOLCANO` Ch64；Legacy Ch52/50/60。现有书稿已有 typed state/locality，但需与 online SLO 边界比较；最终 `Books Pending — Integration Deferred`。Open: context identity、invalidations、replication budget 与 preemption recovery 如何统一？

### 9. Synthetic Bootstrapped Pretraining

- **Candidate / Week / Score / Source Family / Type:** Synthetic Bootstrapped Pretraining / 2025-W38 / 29/30 / `ARXIV-2509.15248` / arXiv research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-17；HTML/PDF、relation synthesis pipeline、compute-matched experiments、ablations、appendix 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** data repetition 在 unique data 稀缺时提高 exposure，曾是合理 baseline；但重复不创造跨文档关系，模型在固定 token budget 下仍缺少可组合结构。
- **Mechanism / State Ownership / Flow / Implementation:** 从 source document groups 识别 relationship，生成连接多个来源的 synthetic documents，与原始 corpus 联合预训练；data pipeline 必须保存 source set、synthesis prompt/model、derived artifact 与 filtering provenance，而非把 synthetic token 当无来源新事实。
- **Evaluation Contract / Workload:** compute-matched 3B models、最高 1T training tokens；比较 standard repetition、synthetic bootstrapping 与 20× unique-data oracle，并做 synthesis/mixture ablation。训练硬件、precision、batch 等仅以论文披露为准；不外推到更大模型。
- **Proof Boundary / Limitations / Threats:** 证明在作者设置下，显式合成关系比等量重复数据提供额外收益；不证明 synthetic knowledge 正确、无污染或可替代真实 unique data。synthesizer bias、memorization、feedback loop 与 provenance loss 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** 获得组合关系，付出生成/过滤 compute 与更复杂的数据血缘；高质量真实数据充足时直接训练仍更简单。Evolution 为 `Direct Evolution`：raw documents → curated mixture → repeated exposure → relationship-aware derived corpus。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `TRAIN-DATA` Ch27，handoff `TRAIN-PRETRAINING` Ch28；Legacy Ch23/24。现有书稿覆盖 synthetic data 与 provenance，但需 later Gate 检查跨文档 relation owner；最终 `Books Pending — Integration Deferred`。Open: 如何检测 derived corpus 的 unsupported relation、循环污染与 memorization？

### 10. Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents

- **Candidate / Week / Score / Source Family / Type:** TARL / 2025-W38 / 27/30 / `ARXIV-2509.14480` / arXiv agent-RL research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-17；PDF、method、turn-level adjudication、mixed-task curriculum、text/speech rollouts、experiments 与 limitations 已核验；无 HTML 不构成 blocker。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** episode-level success reward 对短单步 tool call 合理；多轮交互中最终失败无法说明哪一轮 planning/tool action 出错，稀疏 credit 也压缩 exploration。
- **Mechanism / State Ownership / Flow / Implementation:** TARL 用 LLM judge 对每轮 action/state 做 adjudication，再将 turn rewards 送入 RL；混入数学 reasoning tasks 保持 exploration，sandbox 支持 speech-text interleaving。environment 拥有 executable state，judge 拥有 process label，trainer 拥有 advantage/update，policy 只拥有 action proposal。
- **Evaluation Contract / Workload:** Qwen3-8B、约 3,000 retail examples、32K context；text τ-bench retail/airline 与 interleaved speech-text；作者报告相对强 RL baseline 超过 6% pass-rate improvement。训练硬件/precision、deployment batch/concurrency/SLO `Not Disclosed`。
- **Proof Boundary / Limitations / Threats:** 证明 turn-level judge signal 在作者 harness 改善 in-domain tool use；不证明 judge label 正确、voice agent 生产可靠或 OOD/generalization 已解决。论文自己显示跨域与 pass@k 仍弱。
- **Trade-offs / Previous Boundary / Evolution:** 密集 process reward 改善 credit assignment，却增加 judge cost、reward hacking 与 state-label coupling；终局可执行 verifier 强且 horizon 短时 outcome reward 仍更可信。Evolution 为 `Direct Evolution`：terminal reward → turn-level adjudication → mixed-task interactive RL。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `TRAIN-RLHF` Ch31，handoff `AGENT-TOOL-CALLING` Ch78、`AGENT-WORKFLOW` Ch81；Legacy Ch27/74/77。现有书稿已区分 process/outcome verifier；最终 `Books Pending — Integration Deferred`。Open: judge drift、speech ASR error 与 tool-state mismatch 怎样进入 reward confidence？

### 11. FAMAS: Automatically Attributing Failures of Multi-Agent Systems

- **Candidate / Week / Score / Source Family / Type:** FAMAS / 2025-W38 / 26/30 / `ARXIV-2509.13782` / arXiv software-engineering research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-17；HTML/PDF、trajectory replay/abstraction、spectrum formula、Who&When benchmark、12 baselines 与 threats 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** final success rate 与人工读 log 对少量 deterministic agents 合理；多 agent 的相同角色会跨 execution 产生不同 action，失败责任不能从单次 narrative 可靠归因。
- **Mechanism / State Ownership / Flow / Implementation:** FAMAS 把执行抽象成 agent-action-state elements，通过重复 runs 的 passing/failing spectra 计算 suspiciousness，并融合 agent activation 与 action activation。runtime 拥有 raw trace，normalizer 拥有 element identity，analyzer 拥有 spectrum/counts，human/operator 决定 remediation。
- **Evaluation Contract / Workload:** Who&When 含 184 failure logs、127 MAS（126 AG2、1 Magnetic-One），比较 12 baselines；指标聚焦 culprit agent/action 排名。模型、hardware、precision、online concurrency/SLO 不是核心或 `Not Disclosed`。
- **Proof Boundary / Limitations / Threats:** 证明 spectrum-based statistical contrast 在作者 benchmark 改善 failure localization；不证明 suspicious action 是因果 root cause，也不证明对所有 frameworks/long logs 泛化。replay nondeterminism、abstraction collision 与 simple/short-log bias 限制结论。
- **Trade-offs / Previous Boundary / Evolution:** 多次 replay 增加 token/cost，但把 debugging 从 prose inspection 变成可排序证据；确定性 workflow 或已有 tracing invariant 时传统 trace debugging 更直接。Evolution 为 `Principle Reuse`：program spectrum fault localization → agent/action spectra。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-TRACE` Ch69，handoff `AGENT-MULTI-AGENT` Ch82、`PLATFORM-EVALUATION-SYSTEM` Ch66；Legacy Ch65/78/62。书稿已有 decision trace 与 error amplification；最终 `Books Pending — Integration Deferred`。Open: 如何从 suspicious correlation 进入可执行 counterfactual/root-cause 验证？

### 12. InfraMind

- **Candidate / Week / Score / Source Family / Type:** InfraMind / 2025-W38 / 24/30 / `ARXIV-2509.13704` / arXiv agent-systems research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-17；HTML/PDF、five-module design、open/commercial DCIM evaluation 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** RPA scripts 对固定 GUI 稳定、可审计，但面对多 vendor、层级界面与版本漂移维护成本高；general GUI agent 又缺少工业状态定位、部署约束与高风险 action safety。
- **Mechanism / State Ownership / Flow / Implementation:** framework 用 VM snapshot 支持 search-based exploration，形成结构化 GUI knowledge；memory-driven planner 复用 task knowledge，state identification 定位层级界面，distillation 生成轻量执行模型，多层 guardrail 限制敏感操作。snapshot/environment 拥有可回滚 state，planner 拥有 intent，executor 拥有 action proposal，policy/human 拥有 commit。
- **Evaluation Contract / Workload:** open-source 与 commercial DCIM platforms，比较 task success/efficiency；vendor UI、任务分布、部分 model/hardware/precision/concurrency/SLO `Not Disclosed`，结果为作者实验。
- **Proof Boundary / Limitations / Threats:** 证明“explore → snapshot → structured memory → bounded execution”在所测 DCIM tasks 可行；不证明对真实生产 outage、权限边界或未见 UI change 安全。commercial environment 难独立复现。
- **Trade-offs / Previous Boundary / Evolution:** exploration 提高覆盖却可能触发危险副作用，snapshot/approval 增加成本；稳定高风险操作仍应使用 API/DSL/RPA。Evolution 为 `Alternative Branch`：deterministic automation ↔ exploratory GUI agent with rollback。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `AGENT-PLATFORM` Ch84，handoff `AGENT-WORKFLOW` Ch81、`PLATFORM-SECURITY` Ch72；Legacy Ch80/77/68。书稿已强调 tool permission 与 workflow durability；最终 `Emerging / Experimental`。Open: production DCIM 的 side-effect-free exploration、human override 与 recovery SLO 如何验证？

### 13. DSCC-HS: Dynamic Self-Reinforcing Hallucination Suppression

- **Candidate / Week / Score / Source Family / Type:** DSCC-HS / 2025-W38 / 23/30 / `ARXIV-2509.13702` / arXiv research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-17；HTML/PDF、proxy training、contrastive logits、decode loop、TruthfulQA/BioGEN evaluation 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** post-generation fact checking/RAG 可以修正文档型回答，但不能在每个 decode step 提前约束“事实风险”和“无依据细节”；单一 self-evaluation score 也可能与生成模型同源失败。
- **Mechanism / State Ownership / Flow / Implementation:** 以 Llama-3.2-1B 通过 LoRA（rank 8、alpha 16）训练两个 proxy，分别估计 factual alignment 与 hallucination tendency；每个 token step 用两者 contrastive logits steering Qwen3-8B。base model 持有 next-token logits，proxies 持有方向信号，decoder 持有融合强度与 commit。
- **Evaluation Contract / Workload:** TruthfulQA、BioGEN 与作者 augmentation；主模型 Qwen3-8B，两个 1B proxy 每 token 额外 forward。hardware、precision、batch/concurrency、latency/SLO `Not Disclosed`；FCR 等作者 metric 不等价于真实 calibrated confidence。
- **Proof Boundary / Limitations / Threats:** 证明在所测数据上 contrastive proxy steering 可改变 factuality metrics；不证明事实正确性可由同源模型可靠判定，也不证明部署成本可接受。synthetic labels、domain shift 与 proxy/base correlation 可能放大错误。
- **Trade-offs / Previous Boundary / Evolution:** 主动 decode control 比事后过滤更早，但至少增加两次小模型 forward/token、调参和 false refusal；可检索证据充分时 RAG+verifier 仍更直接。Evolution 为 `Experimental Alternative Branch`，不是“已解决 hallucination”。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-DECODE` Ch44，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66；Legacy Ch40/62。现有书稿已区分 likelihood、confidence、evidence；最终 `Emerging / Experimental`。Open: proxy confidence 如何做 out-of-domain calibration，额外 FLOPs 与 factual gain 如何联合定价？

### 14. CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization

- **Candidate / Week / Score / Source Family / Type:** CoopQ / 2025-W38 / 26/30 / `ARXIV-2509.15455` / arXiv quantization research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18，v2 2025-12；HTML/PDF、Shapley approximation、interaction modeling、MILP、experiments、ablations 与 appendix 已核验；owner W38。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** uniform bit-width 或 independent layer sensitivity 在简单模型/预算下合理；层间误差相互作用意味着逐层贪心选择不能可靠满足全局 memory/accuracy constraint。
- **Mechanism / State Ownership / Flow / Implementation:** progressive Shapley-style sampling估计 layer sensitivity 与 pair interactions，再以 MILP 在 2/4-bit choices 下优化总预算；calibration pipeline 拥有 quality estimates，solver 拥有 assignment，quant runtime/kernel 必须能兑现 chosen formats。
- **Evaluation Contract / Workload:** Llama-3、Gemma-2、Qwen3；Quanto/HQQ/GPTQ；perplexity/task accuracy 与 sensitivity/interaction ablations。hardware、precision kernel、batch/concurrency、latency/SLO 并非所有设置披露，因此量化质量不等于服务加速。
- **Proof Boundary / Limitations / Threats:** 证明考虑 pair interaction 在作者模型/bit set 改善质量-预算选择；不证明 Shapley approximation 精确、MILP 可扩展到任意格式，或部署 kernel 支持无开销混合精度。calibration overfit 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 更好全局配置换取 profiling/solver cost、layout fragmentation 与 kernel dispatch 复杂度；硬件只支持单一 fast path 时 uniform quant 仍优。Evolution 为 `Direct Evolution`：uniform bits → per-layer sensitivity → interaction-aware global assignment。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-TENSORRT-LLM` Ch49，handoff `PLATFORM-MODEL-REGISTRY` Ch59；Legacy Ch45/55。现有 execution-plan 章节已要求 format/kernel coupling；最终 `Books Pending — Integration Deferred`。Open: assignment 如何绑定真实 kernel availability、conversion cost 与 latency SLO？

### 15. FlowRL: Matching Reward Distributions for LLM Reasoning

- **Candidate / Week / Score / Source Family / Type:** FlowRL / 2025-W38 / 28/30 / `ARXIV-2509.15207` / arXiv RL research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、flow-matching objective、trajectory balance derivation、importance sampling/clipping、experiments、ablations 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** PPO/GRPO/REINFORCE-style expected-reward maximization 对稳定 dense reward 合理；长 reasoning 的 sparse/verifiable reward 造成 mode collapse、长度偏置与少数高奖励轨迹过度集中。
- **Mechanism / State Ownership / Flow / Implementation:** FlowRL 不直接最大化单点 reward，而让 policy trajectory distribution 匹配 reward-induced target distribution；length normalization 控制 token-count bias，off-policy samples 通过 importance weighting/clipping 校正。reward/verifier 拥有 target density，rollout store 拥有 trajectories，trainer 拥有 flow objective。
- **Evaluation Contract / Workload:** 7B/32B reasoning models，math/code tasks，对比 PPO、GRPO、REINFORCE++ 等并做 normalization/importance ablations。作者结果绑定其 verifier、sampling budget、模型与 task；完整 hardware/precision/global batch/concurrency/SLO 仅按论文披露。
- **Proof Boundary / Limitations / Threats:** 证明 distribution-matching objective 在所测 RL reasoning setting 改善 performance/diversity；不证明 reward distribution 等价于真实 utility，也不证明更大规模稳定。importance variance、reward misspecification 与 mode coverage 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** 保持多个高质量 reasoning modes，但估计/采样更复杂且依赖 reward temperature；reward 平滑、任务短时经典 objective 更简单。Evolution 为 `Alternative Branch`：expected reward optimization ↔ reward-distribution matching。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `TRAIN-GRPO` Ch33，handoff `TRAIN-RLHF` Ch31；Legacy Ch29/27。书稿已把 post-training 写成条件分支；最终 `Books Pending — Integration Deferred`。Open: reward calibration、distribution temperature 与 policy entropy 如何共同设定？

### 16. Evil Vizier: Vulnerabilities of LLM-Integrated XR Systems

- **Candidate / Week / Score / Source Family / Type:** Evil Vizier / 2025-W38 / 26/30 / `ARXIV-2509.15213` / arXiv XR security research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、XR threat model、attack paths、prototype/evaluation、mitigations 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** text-only prompt injection defenses 假设输入与输出是离散消息；XR agent 把视觉/空间 context 直接映射到 overlay、navigation 或 action，使不可信 environment content 能影响物理决策。
- **Mechanism / State Ownership / Flow / Implementation:** 攻击者在 environment/visual channel 注入指令或误导性 context，perception/LLM 将其混入 trusted task context，XR renderer/action layer执行建议。sensor state、retrieved context、model proposal、rendered instruction 与 physical action 必须分层标记 provenance/authority。
- **Evaluation Contract / Workload:** 作者 XR prototypes、攻击场景与 success/defense observations；具体 headset、model、latency、用户研究规模等只按论文披露，precision/batch/concurrency 多数不适用或 `Not Disclosed`。
- **Proof Boundary / Limitations / Threats:** 证明 LLM-XR composition 新增跨模态 prompt injection/authority confusion；不证明所有 XR systems 同样易受攻击或 defenses 已生产可用。实验环境、参与者规模与物理场景有限。
- **Trade-offs / Previous Boundary / Evolution:** 更丰富 context 提升自然交互，却扩大 untrusted input 与 safety-critical output 的耦合；只读/低风险 XR assistant 仍可采用较轻策略。Evolution 为 `Layering / Dependency`：multimodal input integrity → tool authorization → physical safety envelope。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-SECURITY` Ch72，handoff `MULTIMODAL-EMBODIED-VLA` Ch26、`AGENT-TOOL-CALLING` Ch78；Legacy Ch68/74。书稿已有 physical action boundary；最终 `Books Pending — Integration Deferred`。Open: overlay provenance、human attention 与 emergency override 怎样可验证？

### 17. TDRM: Smooth Reward Models with Temporal Difference

- **Candidate / Week / Score / Source Family / Type:** TDRM / 2025-W38 / 28/30 / `ARXIV-2509.15110` / arXiv reward-model research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18，v2 2025-09-29；HTML/PDF、TD objective、online RL、Best-of-N/tree search、eight variants、ablation 与 limitations 已核验；owner W38。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** terminal scalar reward 对可验证短任务合理；长 reasoning 中同一 partial state 的 value 应与后续 outcome 一致，独立 step scoring 会抖动且难为 search/RL 提供稳定前缀信号。
- **Mechanism / State Ownership / Flow / Implementation:** 用 temporal-difference consistency 训练 process/value reward，使相邻 reasoning states 的预测通过 bootstrapped target 平滑；该 reward 可服务 online RL、Best-of-N 与 tree search。trajectory store 拥有 transitions，reward model 拥有 state value，search/trainer 分别消费而不能把 score 当 ground truth。
- **Evaluation Contract / Workload:** 八种 model variants、math reasoning tasks，比较 outcome/process reward baselines，并覆盖 online RL 与 inference-time search；hardware、precision、batch/concurrency、serving SLO 不完整披露，收益为作者实验。
- **Proof Boundary / Limitations / Threats:** 证明 TD consistency 在所测任务改善 reward smoothness 与 downstream selection/training；不证明 bootstrapped value 无偏或能识别事实错误。early error propagation、reward hacking 与 off-policy drift 是新风险。
- **Trade-offs / Previous Boundary / Evolution:** denser temporal signal改善 credit/search，却可能把错误 value 向前传播；有严格 terminal verifier 的短任务仍应以 outcome 为准。Evolution 为 `Direct Evolution`：terminal reward → per-step reward → temporally consistent process value。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `TRAIN-RLHF` Ch31，handoff `AGENT-REFLECTION` Ch80、`PLATFORM-EVALUATION-SYSTEM` Ch66；Legacy Ch27/76/62。书稿已有 verifier hierarchy；最终 `Books Pending — Integration Deferred`。Open: 如何用 executable terminal evidence 校准/截断 TD bootstrap error？

### 18. Pre-training under Infinite Compute

- **Candidate / Week / Score / Source Family / Type:** Pre-training under Infinite Compute / 2025-W38 / 24/30 / `ARXIV-2509.14786` / arXiv theoretical/empirical research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、theory/assumptions、scaling analysis、experiments、appendix 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** compute-optimal scaling 在有限预算下平衡 parameters 与 tokens；当研究问题把 compute 推到理论极限，data distribution、optimization floor 与 irreducible error 会取代简单 power law 成为主要边界。
- **Mechanism / State Ownership / Flow / Implementation:** 论文构造无限 compute 极限下的 pretraining 分析框架，分离有限 optimization、model capacity、data support 与 asymptotic loss；它是 analytical lens，不是新的生产 runtime。data distribution 拥有可学习 support，objective/architecture 决定 approximation，optimizer 决定到达程度。
- **Evaluation Contract / Workload:** 理论推导配合作者模型/数据 scaling experiments；具体模型、token、hardware、precision、batch 与拟合区间以论文为限，serving concurrency/SLO 不适用。
- **Proof Boundary / Limitations / Threats:** 证明在其假设和测量区间内，极限行为不能只由“更多 FLOPs”概括；不证明现实 frontier model 已到该极限，亦不证明外推曲线稳定。functional form、data quality 与 finite-range fit 是主要威胁。
- **Trade-offs / Previous Boundary / Evolution:** 提供长期 upper-bound 思维，但工程决策仍受有限预算、wall-clock、energy 和 data rights 约束；Chinchilla-like finite-budget planning 仍成立。Evolution 为 `Explanatory Analogy / Boundary Analysis`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `TRAIN-PRETRAINING` Ch28，handoff `WORLDVIEW-SCALING-LAW` Ch8；Legacy Ch24。书稿已有 scaling boundary；最终 `Emerging / Experimental`。Open: 如何把 data support/quality 与 finite-compute scaling law 统一到可操作 capacity plan？

### 19. ATTS: Asynchronous Test-Time Scaling via Conformal Prediction

- **Candidate / Week / Score / Source Family / Type:** ATTS / 2025-W38 / 27/30 / `ARXIV-2509.15148` / arXiv inference-systems research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、conformal formulation、three-stage rejection sampling、system schedule、experiments、ablations 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** target-only best-of-N 或同步 draft verification 在固定小 batch 下合理；多 candidate/异构 model 时昂贵 verifier 被固定 budget 和 slowest path 占满，不能把已足够可靠的请求提前释放。
- **Mechanism / State Ownership / Flow / Implementation:** 多 draft 产生 candidate solutions，target 分阶段验证；conformal calibration 给出 acceptance/coverage rule，scheduler 异步提交已满足条件的请求并对其余继续采样/回退。calibration set 拥有 coverage contract，request state 持有 candidates/scores，scheduler 拥有 compute allocation 与 commit。
- **Evaluation Contract / Workload:** 数学 reasoning benchmarks、draft/target model combinations；作者报告最高 56.7× latency speedup 与 4.14× throughput over target-only scaling。数字绑定其 hardware/model/sample budget/coverage 设置；precision、production concurrency 与 tail-SLO 不得自行补全。
- **Proof Boundary / Limitations / Threats:** 证明在校准分布与作者 workload 上异步 early stop 可减少 target work；不证明 distribution shift 下 coverage 恒定，也不是 token-level exact speculative decoding。calibration drift、candidate correlation、false accept 与 starvation 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 节省昂贵 verification，代价是 draft capacity、calibration state 与复杂调度；小 batch 或 target 很便宜时同步方法更简单。Evolution 为 `Principle Reuse`：proposal → verification → commit，但 commit unit/正确性语义不同于 speculative decoding。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-SCHEDULING` Ch56，handoff `INFER-SPECULATIVE-DECODING` Ch48、`PLATFORM-EVALUATION-SYSTEM` Ch66；Legacy Ch52/44/62。现有书稿已有 adaptive verification；最终 `Books Pending — Integration Deferred`。Open: coverage drift、tenant fairness 与 p99 deadline 如何联动？

### 20. LEAP: LLM Inference on Scalable PIM-NoC Architecture

- **Candidate / Week / Score / Source Family / Type:** LEAP / 2025-W38 / 27/30 / `ARXIV-2509.14781` / arXiv accelerator-architecture paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、PIM/NoC architecture、operator mapping heuristic、simulation methodology、baselines 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** GPU 将 dense linear algebra 与动态 attention 放在同一 memory hierarchy，对通用 batch workload 合理；decode 的 static-weight matrix multiplication 与 dynamic-dynamic attention 具有不同 data movement/reuse，统一映射产生带宽与 load imbalance。
- **Mechanism / State Ownership / Flow / Implementation:** static/dynamic-weight MM 映射到 PIM banks，dynamic-dynamic attention 利用 NoC compute；heuristic 根据 layer/operator shape 做 fine-grained parallel mapping。compiler/runtime 拥有 graph/placement，PIM tiles 拥有 weight/data shards，NoC 拥有 collective/reduction traffic。
- **Evaluation Contract / Workload:** Llama-family约 1B/8B/13B 级配置、simulator，与 A100-like baseline 比较；作者报告最高 2.55× throughput、71.94× energy efficiency。它是 simulation/architecture study，非 silicon 或 production serving；precision、sequence、batch 等须绑定论文设置。
- **Proof Boundary / Limitations / Threats:** 证明异质 operator mapping 在模拟器中可降低 data movement；不证明芯片可制造、软件栈成熟、模型 quality 不变或真实 SLO 达标。memory endurance、thermal、NoC contention 与 simulator fidelity 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** workload-specific co-design 提高 efficiency，却降低可编程性并新增 mapping/compiler burden；模型/shape 快速变化时通用 GPU 仍更稳健。Evolution 为 `Alternative Branch`：general accelerator ↔ heterogeneous PIM/NoC execution plan。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-TENSORRT-LLM` Ch49，handoff `INFER-GPU-MEMORY` Ch54；Legacy Ch45/50。现有 execution-plan owner 能承载 hardware/runtime contract；最终 `Books Pending — Integration Deferred`。Open: 真实 silicon、compiler portability、failure isolation 与模型演化 amortization？

### 21. Enterprise AI Must Enforce Participant-Aware Access Control

- **Candidate / Week / Score / Source Family / Type:** Participant-Aware ACL / 2025-W38 / 29/30 / `ARXIV-2509.14608` / arXiv security/design paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、formal policy, data-user bipartite/biclique model、fine-tuning/RAG application、XPIA examples 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** document ACL 在单用户 search 中合理；enterprise AI 会把多份文档组合进 shared training artifact、index、cache 或 answer，多参与者对不同 source 的权限交集决定结果是否可见。
- **Mechanism / State Ownership / Flow / Implementation:** 将 data objects 与 participants 建模为 authorization graph；只有当 output 所依赖的数据对所有 recipients 都授权时，组合/检索/回答才可提交。identity provider 拥有 principal，data plane 拥有 ACL/provenance，retriever/trainer 构造 candidate set，policy engine 在 commit 前做 deterministic intersection。
- **Evaluation Contract / Workload:** paper 给出 enterprise fine-tuning、RAG、Copilot Tuning deployment claim 与 cross-prompt-injection scenarios；主要是 design/formal contract，不提供通用 latency benchmark。model、hardware、precision、batch、concurrency/SLO `Not Disclosed`。
- **Proof Boundary / Limitations / Threats:** 证明 per-document ACL 不能自动保证 multi-source/multi-recipient result authorization，并给出确定性 policy formulation；不证明任意 enterprise stack 已完整实现，也不覆盖所有 inference leakage。provenance loss、group churn、derived artifact membership 与 stale cache 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** deterministic intersection 提升安全与审计，却可能降低 recall、复用与 cache hit，增加 policy latency；单主体私有 workflow 仍可用简单 ACL。Evolution 为 `Direct Evolution`：object ACL → retrieval-time filter → participant-aware derived-result authorization。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-SECURITY` Ch72，handoff `AGENT-RAG` Ch76、`PLATFORM-MULTI-TENANT` Ch71；Legacy Ch68/72/67。书稿已有 least privilege/provenance，later Gate 应补 derived result 的 recipient intersection；最终 `Books Pending — Integration Deferred`。Open: group revocation 如何触发 index/cache/model-derived artifact invalidation？

### 22. LLM Jailbreak Detection for (Almost) Free!

- **Candidate / Week / Score / Source Family / Type:** FJD / 2025-W38 / 26/30 / `ARXIV-2509.14558` / arXiv security research paper。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；HTML/PDF、affirmative-instruction construction、temperature-scaled first-token logits、virtual instruction variant、experiments、ablations 与 limitations 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** separate moderation model 在高风险场景可靠但增加每请求 latency/cost；surface keyword/refusal checks 又容易漏掉 jailbreak，因为模型内部的 comply/refuse preference 早于完整生成出现。
- **Mechanism / State Ownership / Flow / Implementation:** FJD 构造 affirmative instruction，读取 base model 的首 token logits并做 temperature scaling，以 comply/refuse preference 形成 detector；virtual instruction variant 降低额外 prompt/token cost。model forward 拥有 signal，detector 拥有 threshold，policy engine 决定 block/escalate。
- **Evaluation Contract / Workload:** 多个 open LLM、jailbreak/benign datasets，与 external detectors/ablation 比较；“almost free”表示复用生成模型/少量 logits，不等于零成本。hardware、precision、batch、online concurrency、p99/SLO 未完整披露。
- **Proof Boundary / Limitations / Threats:** 证明 first-token preference signal 在作者数据有分类价值；不证明它是 calibrated attack probability、能覆盖 adaptive attackers 或多语种。threshold/domain drift、base-model update 与 benign false positives 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** 低额外计算适合前置筛选，但同源 detector 与生成模型可能共错；高风险请求仍需独立 classifier、policy/verifier。Evolution 为 `Layering / Dependency`：cheap model-internal signal → escalation → independent safety gate。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-SECURITY` Ch72，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66；Legacy Ch68/62。现有书稿已有 operating point/defense-in-depth；最终 `Books Pending — Integration Deferred`。Open: 如何按模型版本、语言和 attack family 重校阈值并监控 drift？

### 23. Native PyTorch Quantized LLM Inference on Intel CPUs

- **Candidate / Week / Score / Source Family / Type:** Native PyTorch Quantized LLM Inference on Intel CPUs / 2025-W38 / 27/30 / `PYTORCH-INTEL-CPU-QUANT-20250917` / official engineering Blog + compiler/kernel documentation。
- **Event Date / Revision / Sources / Access:** official PyTorch Blog 2025-09-17；全文、quant formats、torch.compile lowering、AMX/AVX-512 kernels、benchmark tables 与 caveats 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** FP/BF16 或 GPU serving 对大批量/高算力合理；CPU deployment 受 memory bandwidth、weight footprint 与 instruction utilization 限制，需要 format、compiler 与 ISA 共同设计。
- **Mechanism / State Ownership / Flow / Implementation:** 支持 A16W8、DA8W8、A16W4、DA8W4 等 recipe；`torch.compile`/TorchInductor 将 quantized GEMM lower 到候选 templates 并 autotune，AMX/AVX-512 执行。model artifact 拥有 quant schema/scales，compiler 拥有 lowering/cache key，runtime 拥有 selected kernel。
- **Evaluation Contract / Workload:** Llama-3.1-8B、单节点双路 Intel Xeon 6980P、input 1K/output 128、vLLM 0.8.5 offline、July release candidate；hardware/length 明确，但 online concurrency、tail latency/SLO 未披露。不同 format 的质量与性能必须分开验收。
- **Proof Boundary / Limitations / Threats:** 证明 native PyTorch path 可在所测 Intel CPU/模型调用 quant kernels并达到作者 performance；不证明其他 CPU、模型、sequence、batch 或 online workload 同样获益。ISA availability、NUMA、packing 与 graph break 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 量化降低 bandwidth/footprint，却增加 calibration、accuracy risk、packing 与 kernel specialization；GPU 或低请求量不一定需要同样路径。Evolution 为 `Layering / Dependency`：quantized artifact → compiler lowering → ISA-specific execution。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-TENSORRT-LLM` Ch49，handoff `INFER-GPU-MEMORY` Ch54、`PLATFORM-MODEL-REGISTRY` Ch59；Legacy Ch45/50/55。现有书稿已将 execution plan 泛化到 CPU/accelerator；最终 `Books Pending — Integration Deferred`。Open: online batching、NUMA placement 与 quant-quality release gate？

### 24. Experience in Reducing PT2 Compilation Time for Meta Internal Workloads

- **Candidate / Week / Score / Source Family / Type:** PT2 Compilation Time / 2025-W38 / 29/30 / `PYTORCH-PT2-COMPILE-TIME-20250918` / official engineering Blog + implementation notes。
- **Event Date / Revision / Sources / Access:** official PyTorch Blog 2025-09-18；全文、profile decomposition、parallel Triton compile、dynamic-shape/cache-key changes、StaticCudaLauncher、MegaCache 与 measured before/after 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** runtime kernel specialization/autotune 能获得高执行性能，在重复稳定 shapes 下合理；大型 foundation model 的 graph 数、dynamic symbols 与 thousands of Triton kernels 使首次 compile 变成部署阻塞。
- **Mechanism / State Ownership / Flow / Implementation:** profiling 将 1825.58s baseline 中 TorchInductor 占 67.8%、`async_compile.wait` 843.95s 暴露出来；将 Triton compile 更早并行、用 `mark_dynamic` 稳定 shape、稳定 symbolic IDs/cache keys、StaticCudaLauncher 与 MegaCache 复用 artifacts。graph compiler 拥有 IR/symbol identity，artifact cache 拥有 binary provenance，runtime 只加载匹配 artifact。
- **Evaluation Contract / Workload:** Meta 一个大型内部 foundation model；官方称 compile 从约 3000s 降到 500s 以下（超过 80%），并给具体 profile slice。model details、GPU、precision、batch、serving concurrency/SLO 多数 `Not Disclosed`，不可当普遍 PT2 improvement。
- **Proof Boundary / Limitations / Threats:** 证明 compile latency 由等待、dynamic identity 与 cache miss 共同拥有，且这些优化在该内部 workload 有效；不证明所有 PT2 models 或 versions 达成同样比例。stale cache、wrong guard、artifact incompatibility 与 parallel memory pressure 是新风险。
- **Trade-offs / Previous Boundary / Evolution:** 更稳定/共享 cache 降低 cold-start，但扩大 invalidation、reproducibility 与 storage contract；小模型/少编译时简单 JIT 足够。Evolution 为 `Direct Evolution`：local JIT → parallel compilation → stable symbolic identity → fleet artifact cache。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `INFER-TENSORRT-LLM` Ch49，handoff `PLATFORM-MODEL-REGISTRY` Ch59、`PLATFORM-PRODUCTION` Ch73；Legacy Ch45/55/69。书稿已有 compilation cache identity；最终 `Books Pending — Integration Deferred`。Open: cache key 如何包含 compiler/driver/shape/precision 且支持安全回滚？

### 25. TorchAO Quantized Models and Recipes on Hugging Face Hub

- **Candidate / Week / Score / Source Family / Type:** TorchAO Quantized Models and Recipes / 2025-W38 / 26/30 / `PYTORCH-TORCHAO-HF-20250919` / official engineering Blog + model-card/recipe artifacts。
- **Event Date / Revision / Sources / Access:** official PyTorch Blog 2025-09-19；全文、INT4/AWQ、FP8、mobile INT8/INT4 recipes、model cards、A100/H100/mobile examples 与 repository links 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 手工量化脚本在单团队/单模型中可行；跨 hub 发布时若只有 weight 文件而无 recipe、backend 与 quality context，artifact 无法复现也不能安全选择。
- **Mechanism / State Ownership / Flow / Implementation:** TorchAO 将 quantized weights、recipe/config 与 model card 一起发布到 Hugging Face，加载端依据 backend/hardware 选择实现；artifact registry 拥有 format/schema/provenance，compiler/runtime 拥有 kernel compatibility，evaluation gate 拥有 quality acceptance。
- **Evaluation Contract / Workload:** INT4/AWQ、FP8 与 mobile recipes，A100/H100/mobile examples；每个 benchmark 只对其 model/hardware/precision/length/batch 有效，统一 concurrency/SLO `Not Disclosed`。官方 recipe availability 不等于任意 workload performance guarantee。
- **Proof Boundary / Limitations / Threats:** 证明 recipe/model-card 可让 quantization 从本地 transform 变成可分发 artifact contract；不证明所有 hub artifact 被独立验证或质量相同。backend skew、missing calibration provenance 与 silent fallback 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 可复用性提高，但 artifact identity 维度变多且需要 compatibility matrix；内部固定 stack 仍可保留简单私有包。Evolution 为 `Layering / Dependency`：quant transform → typed artifact → backend-compatible deployment。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-MODEL-REGISTRY` Ch59，handoff `INFER-TENSORRT-LLM` Ch49、`PLATFORM-EVALUATION-SYSTEM` Ch66；Legacy Ch55/45/62。现有书稿已覆盖 model/engine pair；最终 `Books Pending — Integration Deferred`。Open: recipe、calibration data、kernel version 与 quality evidence 如何进入 immutable manifest？

### 26. DRA Resource Health in Pod Status

- **Candidate / Week / Score / Source Family / Type:** DRA Resource Health / 2025-W38 / 26/30 / `K8S-DRA-RESOURCE-HEALTH-20250917` / official Kubernetes feature Blog + API documentation。
- **Event Date / Revision / Sources / Access:** official Kubernetes Blog 2025-09-17；`DRAResourceHealth` 为 Kubernetes v1.34 alpha；Blog、API/schema、driver/kubelet streaming、examples 与 limitations 已核验。它不是 W35 DRA core GA 的同一完成状态。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** allocation status 只证明设备曾被分配；out-of-band node monitoring 对短任务/独占设备合理，但长时 AI jobs 需要把运行期 device health 与具体 Pod/resource identity 关联。
- **Mechanism / State Ownership / Flow / Implementation:** driver 通过 `NodeWatchResources` stream 提供 health，kubelet 缓存并投影到 ContainerStatus 的 `allocatedResourcesStatus` / `resources.health`，取值 Healthy/Unhealthy/Unknown。driver 拥有判定，kubelet 拥有 cache/status projection，controller/human 拥有 remediation。
- **Evaluation Contract / Workload:** 官方 API/behavior example，无 GPU model workload、node-scale、freshness distribution、failure-recovery benchmark。device type、hardware、precision、batch、concurrency 与 SLO 不适用或 `Not Disclosed`。
- **Proof Boundary / Limitations / Threats:** 证明 driver→kubelet→Pod status 的 observation handoff 与 Unknown semantics；不证明自动 failover、driver accuracy、status freshness 或 vendor support。stream interruption、hard-coded timeout、terminated Pod no update 与 status write pressure 是限制。
- **Trade-offs / Previous Boundary / Evolution:** 提升诊断力，但 stale/Unknown signal 可能触发错误自动化；只需 node-level alert 或任务很短时旧 monitoring 仍合理。Evolution 为 `Layering / Dependency`：stable allocation → alpha runtime health observation。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-GPU-SCHEDULER` Ch63，handoff `PLATFORM-MONITORING` Ch67；Legacy Ch59/63。书稿已有 allocation/health owner split；最终 `Books Pending — Integration Deferred`，later Gate 可能 `No Change`。Open: freshness SLO、driver attestability 与 remediation hysteresis？

### 27. DRA Consumable Capacity

- **Candidate / Week / Score / Source Family / Type:** DRA Consumable Capacity / 2025-W38 / 28/30 / `K8S-DRA-CONSUMABLE-CAPACITY-20250918` / official Kubernetes feature Blog + API documentation。
- **Event Date / Revision / Sources / Access:** official Kubernetes Blog 2025-09-18；`DRAConsumableCapacity` 为 v1.34 alpha；Blog、`allowMultipleAllocations`、capacity/request policy、ShareID/DistinctAttribute、scheduler accounting 与 driver responsibility 已核验。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** exclusive devices/MIG slices 隔离清晰但粒度固定；允许 multiple allocations 若没有 quantity/accounting 会造成声明式 overcommit，无法表达 bandwidth、memory 或 compute share。
- **Mechanism / State Ownership / Flow / Implementation:** device 在 ResourceSlice 声明 consumable capacity，请求按 default/min/step 指定数量，scheduler 跨 claims 累计并限制总 allocation；ShareID/DistinctAttribute 约束共享关系，driver 在 prepare/runtime 层负责兑现。inventory、admission accounting、enforcement 三者 owner 分离。
- **Evaluation Contract / Workload:** 官方 API examples 与 scheduler correctness contract；无真实 GPU compute/memory/bandwidth isolation、fragmentation、fairness 或 performance benchmark。hardware/model/precision/length/batch/concurrency/SLO 不适用或 `Not Disclosed`。
- **Proof Boundary / Limitations / Threats:** 证明 Kubernetes 能对 driver-declared additive capacity 做 allocation-time accounting；不证明多维 GPU resource 可安全合并、driver 有强隔离或 performance 可预测。nominal capacity、accounting drift、fragmentation、noisy neighbor 与 recovery reconciliation 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 提高利用率/表达力，却扩大 driver 与 policy responsibility；strict latency/hard isolation 或 driver 无法 enforce 时 exclusive/MIG/static partition 仍合理。Evolution 为 `Direct Evolution`：exclusive → discrete partition → consumable capacity。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** Owner `PLATFORM-GPU-SCHEDULER` Ch63，handoff `PLATFORM-VOLCANO` Ch64、`PLATFORM-MULTI-TENANT` Ch71；Legacy Ch59/60/67。书稿已有 request≠enforcement 与多维 capacity；最终 `Books Pending — Integration Deferred`。Open: driver 如何证明 enforceability，dominant-resource fairness 与 recovery accounting 如何组合？

### 28. Ask-to-Clarify: Vision-Language-Action Model with Clarification

- **Candidate / Week / Score / Source Family / Type:** Ask-to-Clarify / 2025-W38 / 26/30 / `ARXIV-2509.15061` / primary research + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18，v2 2025-09-19；论文与公开材料可访问，later revision 只作 lineage。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 覆盖 architecture、two-stage training、11-task real-robot evaluation 与 limitations。一次性指令在无歧义时合理；真实场景中的指代与用户意图歧义会把不确定性传入 physical action。
- **Mechanism / State Ownership / Flow / Implementation:** VLM planner 判断是否需 clarification，维护多轮语义状态，再经 semantic-visual adapter 条件化 diffusion motor executor；knowledge-insulation training 分离语言交互与动作学习。用户持有 intent，planner 持有 belief，executor 持有 trajectory，environment 提供纠错事实。
- **Evaluation Contract / Workload:** 11 个真实机器人任务；结果绑定 embodiment、camera/action schema 与作者模型，hardware、control frequency、并发和 production SLO 不构成通用结论。
- **Proof Boundary / Limitations / Threats:** 证明 clarification 可成为 VLA control-flow 分支；不证明能识别所有歧义或对话能替代低层 safety controller。task scope、phrasing 与 closed-set objects 限制外推。
- **Trade-offs / Previous Boundary / Evolution:** 减少误动作但增加 latency、用户负担与 deadlock；明确、低风险、可逆动作仍可直接执行。演进为 `direct action → ambiguity detection → clarification → bounded execution`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MULTIMODAL-EMBODIED-VLA` Ch26，handoff=`AGENT-PLANNING` Ch79；Decision=`Books Pending — Integration Deferred`。问题：何种 calibrated risk threshold 值得打断用户？

### 29. Fast and Fluent Diffusion Language Models

- **Candidate / Week / Score / Source Family / Type:** Fast and Fluent Diffusion LMs / 2025-W38 / 26/30 / `ARXIV-2509.15188` / primary research + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；正文、公式、decoding algorithm、training recipe、evaluation 与公开 artifact 可访问。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 全序列 refinement 保留全局依赖但昂贵；hard block decoding 提速却损失块边界流畅性。open-ended generation 要求并行度与连贯性同时成立。
- **Mechanism / State Ownership / Flow / Implementation:** normalized convolutional decoder 用重叠局部窗口收窄未决区域，不固定切断 block；rejective fine-tuning 强化远离已确认 context 的 token。decoder 持有 mask/confidence/window state，commit rule 决定固化 token。
- **Evaluation Contract / Workload:** open-ended generation 与 AlpacaEval 等作者实验，对比 diffusion baselines 并测 steps/quality；hardware、batch、serving concurrency 与 latency SLO 未充分披露。
- **Proof Boundary / Limitations / Threats:** 证明 block 不是 diffusion LM 加速的唯一分支，training/inference alignment 可改善远端 token；不证明 diffusion 在通用 serving 取代 causal AR。judge、scale 与 kernel 实现影响结论。
- **Trade-offs / Previous Boundary / Evolution:** 并行度换来动态 state、calibration 与 cache/rollback 复杂度；严格因果 streaming 仍适合 AR。演进为 `global denoising → hard block → overlapping window + rejective alignment`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff=`INFER-DECODE` Ch44；Decision=`Books Pending — Integration Deferred`。问题：动态窗口如何映射到 paged state 与 exact commit？

### 30. Robot Control Stack

- **Candidate / Week / Score / Source Family / Type:** Robot Control Stack / 2025-W38 / 24/30 / `ARXIV-2509.14932` / primary systems research + repository。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-18；论文、architecture、supported interfaces、sim/real experiments 与 repository docs 可访问。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** robot-specific script 对单次实验合理；policy、simulator、sensor 与 embodiment 同时变化时，重复 glue 阻碍复现和 sim-to-real 对照。
- **Mechanism / State Ownership / Flow / Implementation:** layered stack 分离 policy interface、observation/action schema、robot transport 与 sim/physical backend；stack 持有 normalized contract，driver 持有 timing/calibration。
- **Evaluation Contract / Workload:** 多 robot 和 sim/physical settings 运行 Octo、OpenVLA、Pi0 等公开 policies；验证 interface portability，不是 policy 能力排行榜。
- **Proof Boundary / Limitations / Threats:** 证明 modular stack 可减少 integration friction；不证明 abstraction 消除 embodiment gap 或 production safety。driver maturity 与 calibration drift 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** 统一接口提高复用但可能隐藏 timing、units、actuator semantics；强实时系统仍需定制路径。演进为 `robot-specific loop → normalized boundary → swappable backend`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MULTIMODAL-EMBODIED-VLA` Ch26，handoff=`PLATFORM-FOUNDATIONS` Ch57；Decision=`Emerging / Experimental`。问题：如何版本化 calibration、deadline 与 safety envelope？

### 31. RPG: A Repository Planning Graph

- **Candidate / Week / Score / Source Family / Type:** RPG / 2025-W38 / 27/30 / `ARXIV-2509.16198` / primary agent-systems research + repository。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-19，v2 2025-09-23；核验 v1、RepoCraft/ZeroRepo evaluation 与 Microsoft `RPG-ZeroRepo` artifact。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** file-by-file generation 对小项目可行；repository-scale 任务同时含 capability、file、function 和 data-flow dependency，线性 plan 难以保存约束或定位失败。
- **Mechanism / State Ownership / Flow / Implementation:** RPG 将需求解析为 typed graph；ZeroRepo 依次做 proposal、implementation construction，再按拓扑生成代码并运行 tests。graph 是 durable planning state，workspace/test runner 是 execution truth，diagnosis 只提供修复建议。
- **Evaluation Contract / Workload:** RepoCraft 6 个项目、1,052 tasks；作者报告 81.5% coverage、69.7% test accuracy，并做 graph/TDD ablation。结果绑定 tasks、models、test oracle 和 compute budget。
- **Proof Boundary / Limitations / Threats:** 证明显式 dependency graph 可改善组织与故障定位；不证明 graph 自动正确或 tests 完备。早期 graph error amplification、oracle gap 与 stale state 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 可追踪性与局部重试换来构图、同步和 invalidation 成本；小任务仍适合简单 plan。演进为 `prompt-to-files → linear plan → typed repository graph → graph-guided repair`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`AGENT-WORKFLOW` Ch81，handoff=`AGENT-PLANNING` Ch79、`PLATFORM-TRACE` Ch69；Decision=`Books Pending — Integration Deferred`。问题：用户修改和 partial rollback 后 graph identity 如何更新？

### 32. MANZANO

- **Candidate / Week / Score / Source Family / Type:** MANZANO / 2025-W38 / 27/30 / `ARXIV-2509.16197` / primary multimodal research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-19；完整论文、training stages、understanding/generation evaluation 与 ablations 可访问。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 分离 understanding encoder 与 generation model 可各自优化，但重复视觉表征且 token identity 不一致；简单共享又会 task interference。
- **Mechanism / State Ownership / Flow / Implementation:** shared vision encoder 经两个 adapters 输出理解用连续 embeddings 与生成用离散 tokens，共同进入 AR LLM；辅助 diffusion decoder 还原 pixels。encoder 持有共享语义，adapters 持有 task boundary，decoder 持有重建状态。
- **Evaluation Contract / Workload:** 图像理解/生成 benchmarks、不同 scales 和 training stages；hardware、precision、serving latency、并发不形成通用 contract。
- **Proof Boundary / Limitations / Threats:** 证明 shared backbone + typed adapters 是统一多模态的一条可行分支；不证明 task conflict 消失或单一 token space 最优。data mix、loss weights、decoder capacity 影响结论。
- **Trade-offs / Previous Boundary / Evolution:** 共享促进 transfer 却耦合训练、版本与 failure domain；强隔离时独立模型仍合理。演进为 `separate models → shared encoder → typed adapters → unified AR + pixel decoder`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MULTIMODAL-REPRESENTATION` Ch23，handoff=`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24；Decision=`Books Pending — Integration Deferred`。问题：representation identity 如何跨 tokenizer/decoder revision 追踪？

### 33. BaseReward

- **Candidate / Week / Score / Source Family / Type:** BaseReward / 2025-W38 / 27/30 / `ARXIV-2509.16127` / primary reward-model research + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-19；核验 RM taxonomy、data recipe、architecture、benchmarks、RL integration 与 code/model 信息。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 单 scalar head 对单模态 preference 可行；multimodal post-training 要同时判断文本、图像、事实与过程，异质数据放大 reward hacking。
- **Mechanism / State Ownership / Flow / Implementation:** 比较 Naive/Critic/Generative RM，再以 Qwen2.5-VL、两层 reward head 和 curated preference data 构建 BaseReward。RM 产生 ranking/scalar，RL learner 持有 policy update，dataset provenance/evaluator contract 独立版本化。
- **Evaluation Contract / Workload:** MM-RLHF-Reward、VL-Reward、Multimodal Reward Bench 与作者 RL pipeline；结果绑定 data mixture、prompt pairs、labels 和 model。
- **Proof Boundary / Limitations / Threats:** 证明 backbone、head、data 与 ensemble 是共同变量；不证明 benchmark 等于真实 alignment，也不排除 contamination/label bias。reward overoptimization 仍开放。
- **Trade-offs / Previous Boundary / Evolution:** 更强 critic 提高覆盖，代价是成本、opaque errors 与 policy-RM co-adaptation；可执行任务仍应优先 rule verifier。演进为 `single head → recipe audit → multimodal critic → RL loop`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`TRAIN-RLHF` Ch31，handoff=`PLATFORM-EVALUATION-SYSTEM` Ch66；Decision=`Books Pending — Integration Deferred`。问题：如何用 held-out domains 和 adversarial rollouts 约束 drift？

### 34. VLAC: Vision-Language-Action-Critic

- **Candidate / Week / Score / Source Family / Type:** VLAC / 2025-W38 / 27/30 / `ARXIV-2509.15937` / primary embodied-RL research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-19；核验 InternVL critic、training data、async real-world RL、four-task evaluation 与 human protocol。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** sparse terminal reward 对短 simulation 合理；真实 robot episode 贵且安全约束强，需要 dense progress signal，纯 human correction 又不可扩展。
- **Mechanism / State Ownership / Flow / Implementation:** VLAC 输出 progress delta 与 done，可交替生成 reward/action tokens；async learner 组合 demo replay、return/explore 和 guided exploration。critic 持有 process assessment，policy 持有 action，human 持有 intervention，environment 持有 physical truth。
- **Evaluation Contract / Workload:** 4 个 manipulation tasks；作者报告部分任务约 30%→90% success、200 episodes 内学习及 human intervention 的 sample-efficiency 收益，均绑定具体 robot/task/model/protocol。
- **Proof Boundary / Limitations / Threats:** 证明 VLM process critic 可提供 dense signal；不证明不会 reward hack 或迁移到新 embodiment。critic-policy coupling 与 human selection bias 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** dense critic 降低 sparse-reward burden，却引入 bias、成本与 loop instability；明确定义成功的任务仍可用 terminal verifier。演进为 `terminal reward → learned progress critic → human-bounded async RL`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MULTIMODAL-EMBODIED-VLA` Ch26，handoff=`TRAIN-RLHF` Ch31；Decision=`Books Pending — Integration Deferred`。问题：critic uncertainty 何时触发 human takeover？

### 35. M-Spoiler

- **Candidate / Week / Score / Source Family / Type:** M-Spoiler / 2025-W38 / 24/30 / `ARXIV-2509.16494` / primary multi-agent security research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20；核验 threat model、stubborn-agent construction、tasks、attacks 与 defenses。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 多 agent defense 常假设 attacker 观察全部状态；现实 attacker 可能只知道一个 agent，却可反复交互推断群体行为。
- **Mechanism / State Ownership / Flow / Implementation:** stubborn agent 模拟与已知 agent/环境交互来生成 adversarial samples，再注入协作。attacker 持有 partial observation/surrogate state，orchestrator 持有 transcript，defense 应在 participant/action boundary 执行。
- **Evaluation Contract / Workload:** 多 tasks/settings/defenses；结果绑定模型、prompt topology、query budget 和 judge，未证明生产 agent mesh 的真实攻击率。
- **Proof Boundary / Limitations / Threats:** 证明 incomplete information 不会消除 MAS attack surface；不覆盖 tool permissions、persistent memory 或 network policy。simulation fidelity 是限制。
- **Trade-offs / Previous Boundary / Evolution:** 过滤/consensus 降低注入但增加 communication tax 与 false positive；isolated workflow 仍减小攻击面。演进为 `full-observation adversary → partial-observation simulation → participant-aware defense`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`PLATFORM-SECURITY` Ch72，handoff=`AGENT-MULTI-AGENT` Ch82；Decision=`Emerging / Experimental`。问题：如何写成 executable policy test？

### 36. HAPO

- **Candidate / Week / Score / Source Family / Type:** HAPO / 2025-W38 / 27/30 / `ARXIV-2509.16591` / primary RL research + code。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20，v2 2026-04；核验 v1 algorithm、公式、settings、ablations 与 artifact，later revision 只作 lineage。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** fixed temperature、group advantage 与 symmetric clipping 对稳定 reward 合理；reasoning rollout 的 token entropy、difficulty 与 gradient contribution 高度异质。
- **Mechanism / State Ownership / Flow / Implementation:** token entropy 调节 temperature，以 token-level group average advantage 分配 credit，再做 differential redistribution 与 asymmetric adaptive clipping。sampler 持有 entropy/temperature，learner 持有 advantages/clip bounds。
- **Evaluation Contract / Workload:** 多 scales、数学/代码/逻辑 tasks，与 DAPO 等比较并做 ablation；结果绑定 rollout budget、reward/verifier、prompts、hardware/precision。
- **Proof Boundary / Limitations / Threats:** 证明 sampling、credit assignment 与 clipping 可联合适配 token uncertainty；不证明 entropy 等于 epistemic uncertainty或避免 reward hacking。
- **Trade-offs / Previous Boundary / Evolution:** 提高 exploration/credit granularity，却增加超参数与 non-stationary feedback；短、同质输出仍适合简单 group objective。演进为 `fixed group update → token advantage → entropy-conditioned sampling + asymmetric trust region`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`TRAIN-GRPO` Ch33，adjacent Ch31/32；Decision=`Books Pending — Integration Deferred`。问题：entropy 与 verifier uncertainty 如何解耦？

### 37. Audio-Conditioned Diffusion Language Models for ASR

- **Candidate / Week / Score / Source Family / Type:** Audio-conditioned DLM / 2025-W38 / 25/30 / `ARXIV-2509.16622` / primary multimodal research + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20；核验 conditioning、masking/decoding、ASR evaluation、speed-quality comparison 与 code/model。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** causal ASR decoder稳定 streaming 但 token latency 受限；纯文本 DLM 缺 acoustic grounding，不能只靠 rescoring 修复识别。
- **Mechanism / State Ownership / Flow / Implementation:** audio evidence 注入 LLaDA，比较 random/low-confidence masking 与 semi-AR；cascade 用 Whisper proposal 后 deliberation。encoder 持有 observation，DLM 持有 masked transcript/confidence，commit policy 决定修正范围。
- **Evaluation Contract / Workload:** 作者 ASR setting 中 cascade 报告 2.25/4.94 WER、test-other 相对改善 12.3%；standalone 更快但略降准确率。数字绑定 data/model/steps，hardware/batch/concurrency/SLO 未完整披露。
- **Proof Boundary / Limitations / Threats:** 证明 audio conditioning 是 DLM ASR deliberation 的关键输入；不证明适用于 streaming、噪声多语种或 production ASR。
- **Trade-offs / Previous Boundary / Evolution:** iterative correction 增加纠错空间，也增加 mask state 与 latency variance；严格实时仍适合 causal decoder。演进为 `AR transcript → text-only deliberation failure → audio-conditioned refinement`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch23/44；Decision=`Books Pending — Integration Deferred`。问题：streaming deadline 内如何定义可中断 commit？

### 38. FESTA

- **Candidate / Week / Score / Source Family / Type:** FESTA / 2025-W38 / 24/30 / `ARXIV-2509.16648` / primary uncertainty-evaluation research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20；论文、functionally equivalent/complementary transformations、vision/audio evaluation 与 ablations 可访问。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** softmax/token confidence 对 closed classifier 可用，但 multimodal black-box model 常无 calibrated probability，且单输入无法区分 shortcut 与 task-relevant evidence。
- **Mechanism / State Ownership / Flow / Implementation:** 生成保持任务语义、功能等价或互补的 input variants，比较黑盒输出一致性并形成 uncertainty score；transformation contract 持有 invariance assumption，evaluator 持有 paired outputs，model 不被当作自证者。
- **Evaluation Contract / Workload:** vision/audio tasks；作者报告 misprediction detection AUROC 相对提升 33.3%/29.6%，绑定 transformations、datasets、models 与 baselines，不是通用 calibration guarantee。
- **Proof Boundary / Limitations / Threats:** 证明 counterfactual consistency 可构造 ground-truth-free uncertainty signal；不证明 transformations 真正保持语义或覆盖 OOD。generator bias 与 correlated errors 是主要威胁。
- **Trade-offs / Previous Boundary / Evolution:** 减少对内部 logits 依赖，但增加多次 inference 与 transformation validation；有可靠 calibrated head 时简单 confidence 更便宜。演进为 `single-output confidence → semantic-preserving probes → consistency-derived uncertainty`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`PLATFORM-EVALUATION-SYSTEM` Ch66，handoff=`PLATFORM-TRACE` Ch69；Decision=`Emerging / Experimental`。问题：如何审计 equivalence contract，避免一致地错？

### 39. Decoding Uncertainty

- **Candidate / Week / Score / Source Family / Type:** Decoding Uncertainty / 2025-W38 / 24/30 / `ARXIV-2509.16696` / primary evaluation research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20；核验 decoding strategies、uncertainty metrics、preference-aligned/SFT model comparison 与 limitations。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 把 uncertainty 当作模型固有属性在固定 greedy decoding 下尚可；temperature、top-p、beam/contrastive search 改变输出分布和可观察 confidence，model 与 decoder 不可分离。
- **Mechanism / State Ownership / Flow / Implementation:** 在多 decoding policies 下测 uncertainty-quality relation，并区分 preference-aligned 与 SFT-only models；model 持有 conditional distribution，decoder 持有 search/truncation state，evaluator 持有 calibration/quality labels。
- **Evaluation Contract / Workload:** 作者任务和模型中 contrastive search 常改善 preference-aligned uncertainty，但 SFT-only 结论不同；未披露/不适用的 serving hardware、batch、concurrency、SLO 不可补推。
- **Proof Boundary / Limitations / Threats:** 证明 uncertainty 结果依赖 decode policy 与 training regime；不证明某策略普遍最 calibrated。metric choice、judge 与 task shift 会改变排序。
- **Trade-offs / Previous Boundary / Evolution:** 更复杂 search 可改善 quality/calibration，却增加 compute、latency 与 state；低延迟场景仍可 greedy + external verifier。演进为 `model confidence → model+decoder contract → workload-specific calibration`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`PLATFORM-EVALUATION-SYSTEM` Ch66，handoff=`MODEL-SAMPLING` Ch20；Decision=`Emerging / Experimental`。问题：release gate 应按 model 还是 model-decoder pair 校准？

### 40. SMART: Sycophancy Mitigation via Adaptive Reinforcement Learning

- **Candidate / Week / Score / Source Family / Type:** SMART / 2025-W38 / 26/30 / `ARXIV-2509.16742` / primary post-training research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20；核验 UA-MCTS、trajectory labels、progress/outcome rewards、RL objective、sycophancy/OOD evaluation 与 ablations。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** fixed exploration MCTS 与 final-outcome reward 在均匀任务上合理；sycophancy failure 常在中间推理步骤发生，state uncertainty 和 useful exploration depth 不同。
- **Mechanism / State Ownership / Flow / Implementation:** UA-MCTS 根据 state uncertainty 动态调 exploration，收集 step progress 与 outcome signal，再用 progress-aware RL 更新 policy。tree 持有 branching/visit state，judge 持有 step/outcome labels，learner 持有 policy update。
- **Evaluation Contract / Workload:** sycophancy、OOD 与 general-capability tasks，作者模型与 search budgets；结果依赖 uncertainty proxy、judge、rollout compute，不证明所有对齐失败可由搜索缓解。
- **Proof Boundary / Limitations / Threats:** 证明 uncertainty-aware search 可改善 training data allocation，并把反谄媚信号落到过程；不证明自评 uncertainty calibrated。judge bias、search-policy feedback 与 compute mismatch 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** 更有针对性的 exploration 换来昂贵 tree search 与更复杂 credit；有 executable outcome verifier 时简单 outcome RL 仍可靠。演进为 `uniform search + terminal reward → uncertainty-aware search → progress-aware RL`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`TRAIN-RLHF` Ch31，handoff=`TRAIN-GRPO` Ch33；Decision=`Books Pending — Integration Deferred`。问题：进度标签怎样避免被 policy gaming？

### 41. Roundtable Policy

- **Candidate / Week / Score / Source Family / Type:** Roundtable Policy / 2025-W38 / 24/30 / `ARXIV-2509.16839` / primary ensemble research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20；核验 weighted-consensus mechanism、black-box assumptions、science tasks、baselines 与 limitations。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** majority vote 在独立同质量模型下合理；heterogeneous LLMs 的专长与错误相关性不同，固定等权会放大共错或压制 specialist。
- **Mechanism / State Ownership / Flow / Implementation:** 多个 black-box models 产生候选和 confidence/evidence，roundtable 按 estimated reliability 加权聚合；成员持有 local answer，aggregator 持有 weights/consensus state，final verifier 决定是否接受。
- **Evaluation Contract / Workload:** heterogeneous science tasks 与作者模型组合；model calls、prompting、weight calibration 和 judge 绑定结果，缺 production latency/cost/SLO 证据。
- **Proof Boundary / Limitations / Threats:** 证明 weighted consensus 可作为 heterogeneous ensemble 分支；不证明模型错误独立或 self-confidence 可直接作权重。correlated hallucination 与 weight drift 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 增加 diversity 与解释 trace，但 communication/call cost 上升；单模型有 headroom 或低延迟时不应强行 ensemble。演进为 `single model → equal vote → reliability-weighted consensus`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`AGENT-MULTI-AGENT` Ch82，handoff=`PLATFORM-EVALUATION-SYSTEM` Ch66；Decision=`Emerging / Experimental`。问题：如何在 held-out workload 校准成员可靠性并控制共错？

### 42. seqBench

- **Candidate / Week / Score / Source Family / Type:** seqBench / 2025-W38 / 24/30 / `ARXIV-2509.16866` / primary benchmark research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-21；核验 generator、controlled depth/backtracking/noise factors、models、metrics 与 analysis。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 静态 reasoning benchmark 容易混合知识、memorization 与逻辑长度；需要可参数化 workload 才能定位何时出现 sequential failure。
- **Mechanism / State Ownership / Flow / Implementation:** generator 控制 logical depth、backtracking 与 distractor noise，保留可执行 ground truth；benchmark 持有 problem parameters/solution trace，model 只产生 candidate reasoning，verifier 计算 correctness。
- **Evaluation Contract / Workload:** 多模型按 controlled parameters 测试，作者观察超过 model-specific depth 后近指数式崩溃；这不是自然任务的普遍 scaling law。
- **Proof Boundary / Limitations / Threats:** 证明 task difficulty 可拆成 sequential dimensions；不证明 synthetic generator 覆盖真实 reasoning 或 CoT 等于内部机制。format sensitivity 与 contamination 仍需控制。
- **Trade-offs / Previous Boundary / Evolution:** 可诊断性提高但生态真实性下降；自然 benchmark 仍用于 external validity。演进为 `aggregate accuracy → parameterized trace workload → failure-surface measurement`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`PLATFORM-EVALUATION-SYSTEM` Ch66；Decision=`Emerging / Experimental`。问题：怎样把 depth/backtracking 映射到 agent tool/workflow state？

### 43. SWE-Bench Pro

- **Candidate / Week / Score / Source Family / Type:** SWE-Bench Pro / 2025-W38 / 28/30 / `ARXIV-2509.16941` / primary executable benchmark + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-21，v2 2025-11；核验 v1 dataset construction、1,865 problems、41 repositories、partitions、human verification 与 agent trajectory analysis。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 短、单文件、广泛公开的 coding tasks 适合早期比较；modern coding agents 要处理 hours-to-days、multi-file、active-repo tasks，且污染与 harness correctness 成为主要约束。
- **Mechanism / State Ownership / Flow / Implementation:** public/held-out/commercial partitions 分离 exposure；repository commit、issue、tests 与 environment 构成 executable task identity；trajectory logs支持 failure clustering。benchmark owner 持有 immutable task/environment，agent 持有 action trace，tests 提供 acceptance oracle。
- **Evaluation Contract / Workload:** 1,865 problems、41 active repos，human verification 与 multi-agent/model comparisons；score 只对固定 container、tests、budget 和 policy 有效，不能等同一般软件工程生产力。
- **Proof Boundary / Limitations / Threats:** 证明长时、多文件、污染受控评测揭示不同于简化 benchmark 的 failure surface；不证明 tests 完备或商业 partition 永不泄漏。environment drift 与 flakiness 是风险。
- **Trade-offs / Previous Boundary / Evolution:** realism/contamination resistance 提升，却增加成本、复现与版本维护；小 benchmark 仍适合快速 regression。演进为 `unit patch benchmark → multi-file executable task → held-out long-horizon evidence`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`PLATFORM-EVALUATION-SYSTEM` Ch66，handoff=`AGENT-WORKFLOW` Ch81；Decision=`Books Pending — Integration Deferred`。问题：如何把 harness health、budget、trajectory 与 test coverage 放进同一 evidence manifest？

### 44. MCTS-EP

- **Candidate / Week / Score / Source Family / Type:** MCTS-EP / 2025-W38 / 25/30 / `ARXIV-2509.17116` / primary preference-learning research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-21；核验 MCTS exploration、preference-pair construction、iterative optimization、theory 与 ALFWorld/WebShop evaluation。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 随机 rollout 生成 preference pairs 简单，但长时 agent task 的有信息失败稀疏，容易浪费 compute 或只比较相近轨迹。
- **Mechanism / State Ownership / Flow / Implementation:** MCTS 用 feasibility/quality signal探索 trajectory tree，选择正负路径构造 preference data，再迭代优化 policy；tree 持有 state/action visits，verifier 持有 outcome，trainer 持有 pair/provenance。
- **Evaluation Contract / Workload:** multimodal reasoning 及 ALFWorld/WebShop；包含 strongly-convex loss 条件下的理论界与作者实验，不能外推非凸大模型全局收敛。
- **Proof Boundary / Limitations / Threats:** 证明 search policy 会改变 preference-data 信息量；不证明 MCTS 计算成本总能回收或 simulator matches deployment。search bias 与 stale policy data 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 提高 hard-negative/positive pair 质量，代价是 tree compute 与复杂 provenance；短任务仍可随机采样。演进为 `random rollout pairs → search-guided trajectory pairs → iterative preference optimization`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`AGENT-PLANNING` Ch79，handoff=`TRAIN-DPO` Ch34；Decision=`Books Pending — Integration Deferred`。问题：如何避免 search policy 把 preference data 锁进窄分布？

### 45. ARE: A Research Environment for Agentic Systems

- **Candidate / Week / Score / Source Family / Type:** ARE / 2025-W38 / 28/30 / `ARXIV-2509.17158` / primary agent-platform research + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-21，v2 2025-12；核验 v1 platform abstractions、Gaia2 environments、orchestration、evaluation 与 scaling analyses。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 静态 QA/harness 对单轮 agent 合理；真实 workflow 有 ambiguity、noise、dynamic state、collaboration 和 temporal constraints，需要可执行 environment 与 async orchestration。
- **Mechanism / State Ownership / Flow / Implementation:** ARE 抽象 rules、tools、content、verifiers 与 async agent orchestrations；Gaia2 组合动态 environments。environment 持有 world state，orchestrator 持有 agent/task lifecycle，tools 持有 effects，verifier 持有 acceptance evidence。
- **Evaluation Contract / Workload:** Gaia2 与多个 agent systems；作者观察无单系统统治、reasoning-efficiency trade-off 和 budget scaling plateau。结果绑定 environments、tools、budgets 与 verifiers。
- **Proof Boundary / Limitations / Threats:** 证明 agent evaluation 需要 stateful environment 和 explicit verifier；不证明 Gaia2 等同生产 autonomy 或更多 budget 必然无效。environment fidelity 与 verifier coverage 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** realism/diagnosis 增强但复现成本、flakiness 与 orchestration complexity 上升；静态 tasks 仍适合组件 regression。演进为 `static benchmark → tool harness → dynamic environment + async orchestration + verifier`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`AGENT-PLATFORM` Ch84，handoff=`PLATFORM-EVALUATION-SYSTEM` Ch66；Decision=`Books Pending — Integration Deferred`。问题：如何版本化 environment dynamics 与 verifier semantics？

### 46. RoE: Routing of Experts for Hyper-Parallel MoE Inference

- **Candidate / Week / Score / Source Family / Type:** RoE / 2025-W38 / 27/30 / `ARXIV-2509.17238` / primary MoE inference research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-21；核验 controlled stochastic routing、parallel sampling/aggregation、batching、KV design、models 与 ablations。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** deterministic top-k routing 高效且可训练，但 test-time compute scaling 通常复制整模型/sequence；MoE 已有 dormant expert diversity，可在 token level 暴露更多候选。
- **Mechanism / State Ownership / Flow / Implementation:** controlled stochastic routing 为同一 token 采样不同 expert paths，再聚合候选；hyper-parallel batching 与 specialized KV cache 复用共享 prefix/state。router 持有 expert distribution，runtime 持有 branch/KV identity，aggregator 决定 commit。
- **Evaluation Contract / Workload:** 作者 MoE models/tasks；报告 7B MoE 可接近 10.5B MoE、约少 30% compute，绑定 routing samples、aggregation、hardware/implementation，不是通用 MoE 性能事实。
- **Proof Boundary / Limitations / Threats:** 证明 test-time scaling 可复用 expert diversity 而不只复制模型；不证明随机路由保持 calibration 或 routing branches 独立。KV amplification、tail latency 与 correlated experts 是风险。
- **Trade-offs / Previous Boundary / Evolution:** 增加 quality/parallelism 但扩大 active compute、KV 与 aggregation；吞吐优先仍适合 deterministic top-k。演进为 `trained sparse routing → deterministic inference → stochastic expert branches + shared-state aggregation`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`MODEL-MOE` Ch21，handoff=`INFER-SCHEDULING` Ch56 与 `INFER-GPU-MEMORY` Ch54；Decision=`Books Pending — Integration Deferred`。问题：如何做 branch-aware admission、fairness 和 rollback？

### 47. Mind the Gap / AgentSeer

- **Candidate / Week / Score / Source Family / Type:** Mind the Gap / AgentSeer / 2025-W38 / 27/30 / `ARXIV-2509.17259` / primary agent-security evaluation research + artifact。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-21；核验 GPT-OSS-20B model-vs-agent red teaming、HarmBench objectives、action graph、tool settings 与 vulnerability analysis。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** 只测模型文本输出可评估 content safety；部署为 tool-using agent 后，环境机会、multi-step actions 与 state transitions 产生模型层看不到的新攻击面。
- **Mechanism / State Ownership / Flow / Implementation:** AgentSeer 将 observation、tool call、effect 和 subsequent state 建成 action graph，比较同模型 model-only 与 agentic harness。model 持有 proposal，harness 持有 tools/permissions，environment 持有 effects，monitor 持有 action trace。
- **Evaluation Contract / Workload:** GPT-OSS-20B、HarmBench-derived objectives 与作者 tools/environments；作者报告 agent-only vulnerabilities 和 tools setting 更高 vulnerability，数字只对该 harness/attack budget 有效。
- **Proof Boundary / Limitations / Threats:** 证明 model safety score 不等于 deployment safety，action graph 可定位 agent-only path；不证明监控可阻止攻击或覆盖隐蔽 side effects。harness opportunity 与 evaluator completeness 是限制。
- **Trade-offs / Previous Boundary / Evolution:** action-level observability 增强 attribution，却增加 trace volume、privacy 与 policy complexity；无 tools 的 model test 仍是必要组件 gate。演进为 `output red team → harness red team → action-graph deployment evidence`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`PLATFORM-SECURITY` Ch72，handoff=`PLATFORM-TRACE` Ch69 与 `AGENT-TOOL-CALLING` Ch78；Decision=`Books Pending — Integration Deferred`。问题：如何把 graph policy violation 变成 pre-action deny 与 post-action rollback？

### 48. Prompt-Driven Agentic Video Editing

- **Candidate / Week / Score / Source Family / Type:** Prompt-Driven Agentic Video Editing / 2025-W38 / 24/30 / `ARXIV-2509.16811` / primary systems/HCI research。
- **Event Date / Revision / Sources / Access:** arXiv v1 2025-09-20，v2 2025-09-28；v1 identity/PDF 与 v2 HTML 全文可访问。architecture、four-study evaluation 通过全文核验；v2 只辅助机制阅读，未把未确认的 revision delta 写成 v1-specific fact。
- **Full-read Coverage / Problem / Previous Design / Changed Constraint:** transcript/vector search 对短 clip 和定位合理；multi-hour narrative editing 需要跨片段保存 character、causality、timestamp 与 creator intent，反复把原视频塞回长上下文既贵又不稳定。
- **Mechanism / State Ownership / Flow / Implementation:** pipeline 用重叠 temporal segmentation、guided memory compression 与 coarse/fine fusion 生成 timestamped semantic index；planning、retrieval、narration、rendering agents 在 Temporal.io workflow 中消费可审计的 storyboard/edit-plan artifacts，GCS 持有 media/index，FFmpeg/MoviePy 执行确定性 rendering。index 是 derived state，source video 是 evidence truth，user 可审查中间 artifacts。
- **Evaluation Contract / Workload:** 400+ videos 总体覆盖；具体研究含 21 movies、9 TV episodes、8 expert raters，并有 QA、ablation、edited-video 与 user studies。pipeline 使用 Gemini 2.0 Flash；结果绑定 segmentation、prompts、raters、tools 与 cloud setup，不能外推为所有 long-video agent workflow。
- **Proof Boundary / Limitations / Threats:** 证明 persistent time-aligned index + durable workflow 可降低长视频反复理解成本并提高可审查性；不证明 narrative inference 无幻觉或多 agent 数量本身带来收益。小 rater sample、proprietary model、timestamp error、derived-index staleness 与 copyright/privacy 是威胁。
- **Trade-offs / Previous Boundary / Evolution:** 结构化 index 支持复用、局部修订和 provenance，代价是多 pass compute、storage、invalidation 与跨 agent error amplification；短视频/单次编辑仍可直接 prompt。演进为 `timeline/transcript search → vector retrieval → persistent narrative index → artifact-driven editing workflow`。
- **ROADMAP / Adjacent / Existing Coverage / Decision / Changes / Questions:** owner=`AGENT-WORKFLOW` Ch81，handoff=`MULTIMODAL-REPRESENTATION` Ch23、`AGENT-MEMORY` Ch77；Decision=`Emerging / Experimental`。问题：source clip、derived index、storyboard 与 final render 如何共享 immutable lineage、supersession 与 delete contract？

## Low-Score Source, Date, Score, and Rejection Closure

以下 40 项均已定位唯一 primary identifier、复核 v1 日期并阅读摘要/正文中与评分相关的 method、evaluation 与 limitation；它们不处于 Review Pending。拒绝意味着本周不进入完整机制账本，不意味着论文无价值。

| Candidate | Primary Source / v1 Date | Score | Source Verification | Rejection Closure | ROADMAP Owner |
| --- | --- | ---: | --- | --- | --- |
| C3T speech-language preservation | [arXiv:2509.12171](https://arxiv.org/abs/2509.12171), 2025-09-15；v2 2025-10-16 | 19/30 | Full text + benchmark code identity verified | 将 text tasks 经 voice-cloned TTS 转为 speech，能测 modality preservation/fairness，但 5-page benchmark、synthetic speech 与有限模型不足以改变通用 multimodal evaluation contract。 | `PLATFORM-EVALUATION-SYSTEM` |
| RAGs to Riches | [arXiv:2509.12168](https://arxiv.org/abs/2509.12168), 2025-09-15 | 19/30 | Full text verified | 453 次 role-play interactions、LLM judge 与 ROUGE-like utilization metrics 证明 curated demonstrations 可影响角色一致性；证据过于 task-specific，未形成新的 RAG state/identity 机制。 | `AGENT-RAG` |
| MedicalOS | [arXiv:2509.11507](https://arxiv.org/abs/2509.11507), 2025-09-15 | 19/30 | Full text verified | 214 cases/22 specialties 展示 domain command abstraction，但临床 ground truth、real deployment safety、权限与 prospective validation 不足；“OS”主要是 workflow wrapper，暂不形成通用 owner。 | `AGENT-PLATFORM` |
| Pointing Gestures in Embodied Agents | [arXiv:2509.12507](https://arxiv.org/abs/2509.12507), 2025-09-15 | 18/30 | Full text verified | imitation+RL 在小型 motion-capture/VR referential game 的结果是窄域 physical-action case，尚不足以改变 VLA control/safety 主线。 | `MULTIMODAL-EMBODIED-VLA` |
| LLMs Imitate Logical Reasoning, but at what Cost? | [arXiv:2509.12645](https://arxiv.org/abs/2509.12645), 2025-09-16 | 19/30 | Full text and evaluation identity verified | 提供 reasoning behavior/cost 诊断，但没有足够稳定的新 training/runtime mechanism；保留为 evaluation case，不把 task performance 推成推理本质。 | `PLATFORM-EVALUATION-SYSTEM` |
| Multi-Agent LLM Defense Pipeline | [arXiv:2509.14285](https://arxiv.org/abs/2509.14285), 2025-09-16 | 19/30 | Full text verified | 多 agent defense composition 可作为 defense-in-depth 案例，但额外 agents 不是独立 security guarantee，攻击覆盖、通信税与同源共错不足以支撑长期机制更新。 | `PLATFORM-SECURITY` |
| Reversible Deep Equilibrium Models | [arXiv:2509.12917](https://arxiv.org/abs/2509.12917), 2025-09-16 | 19/30 | Full text and revisions verified | reversible DEQ 的 memory/implicit-depth 机制有研究价值，但与本书当前 Transformer/training system 主线连接弱，且实验未形成通用 distributed/runtime contract。 | `MODEL-TRANSFORMER-LAYER` |
| Black-box Model Merging for LMaaS | [arXiv:2509.12951](https://arxiv.org/abs/2509.12951), 2025-09-16 | 19/30 | Full text verified | 针对 massive model repositories 的 black-box merge 是早期 selection/combination case；quality、cost、artifact compatibility 与 production reproducibility 尚不足。 | `PLATFORM-MODEL-REGISTRY` |
| Bi-level Personalization for Federated Foundation Models | [arXiv:2509.12697](https://arxiv.org/abs/2509.12697), 2025-09-16 | 19/30 | Full text and v2 metadata verified | task-vector aggregation 说明 personalization/aggregation tension，但任务与 threat model 窄，未改变本书 distributed training 的 state/communication 主线。 | `TRAIN-DISTRIBUTED-TRAINING` |
| Token-Level DP in Memory Sculpting | [arXiv:2509.12958](https://arxiv.org/abs/2509.12958), 2025-09-16 | 19/30 | Full text verified | token-level differential privacy 与 continual-memory selection 是有界案例；privacy accountant、utility generalization 与 agent-memory provenance 仍不足以形成通用方案。 | `TRAIN-DATA` |
| Data Scaling Laws for Radiology Foundation Models | [arXiv:2509.12818](https://arxiv.org/abs/2509.12818), 2025-09-16 | 18/30 | Full text verified | radiology-specific data/label distribution 提供领域 scaling evidence，但不能把拟合曲线外推为通用 foundation-model law。 | `TRAIN-DATA` |
| HPIM Accelerator | [arXiv:2509.12993](https://arxiv.org/abs/2509.12993), 2025-09-16 | 19/30 | Full text verified | heterogeneous PIM 映射仅提供 simulator/architecture-specific 结果，缺真实 silicon、compiler/runtime 与 workload portability；由更完整的 LEAP evidence 承担本周 PIM 路线。 | `INFER-TENSORRT-LLM` |
| Prosocial Ability Profiles | [arXiv:2509.14485](https://arxiv.org/abs/2509.14485), 2025-09-17 | 18/30 | Full text verified | Measurement Layouts 揭示 Melting Pot 高分不等于 prosociality，适合作为 benchmark caveat；仍是单 suite reanalysis，未形成新的 MAS architecture。 | `PLATFORM-EVALUATION-SYSTEM` |
| CAMPUS Curriculum Instruction Tuning | [arXiv:2509.13790](https://arxiv.org/abs/2509.13790), 2025-09-17；v2 2025-11-03 | 19/30 | Full text and revision verified | dynamic competence-aware curriculum 是训练 schedule case，但数据、模型与 benchmark 范围不足以改变通用 SFT data/objective contract。 | `TRAIN-SFT` |
| PromptSE | [arXiv:2509.13680](https://arxiv.org/abs/2509.13680), 2025-09-17 | 18/30 | Full text verified | emotion/personality prompt variants 与 AUC-E 揭示 performance/stability 解耦，但只覆盖 code LLM prompts，metric 尚未形成通用 robustness gate。 | `PLATFORM-EVALUATION-SYSTEM` |
| AgentCTG | [arXiv:2509.13677](https://arxiv.org/abs/2509.13677), 2025-09-17 | 19/30 | Full text verified | 用多 agent wrapper 做 controllable text generation，主要收益仍可能来自额外 sampling/prompting；缺少单 agent compute-matched headroom 与 error-amplification contract。 | `AGENT-MULTI-AGENT` |
| Helpfulness-Exploiting Jailbreak | [arXiv:2509.14297](https://arxiv.org/abs/2509.14297), 2025-09-17 | 19/30 | Full text verified | 展示一个利用 helpfulness 的 attack variant，但未形成超越已有 jailbreak taxonomy/defense operating point 的长期机制。 | `PLATFORM-SECURITY` |
| TENET Ternary Edge Inference | [arXiv:2509.13765](https://arxiv.org/abs/2509.13765), 2025-09-17 | 19/30 | Full text verified | LUT/sparsity-aware ternary architecture 是特定 edge accelerator 设计，依赖 model/ISA/layout；缺 silicon 与软件栈证据，暂不提升。 | `INFER-TENSORRT-LLM` |
| FlowDrive | [arXiv:2509.14303](https://arxiv.org/abs/2509.14303), 2025-09-17 | 19/30 | Full text verified | energy-flow field 对 autonomous driving 是领域表示分支，未补足通用 world-state identity、control frequency 与 physical safety contract。 | `MULTIMODAL-EMBODIED-VLA` |
| VCBench | [arXiv:2509.14448](https://arxiv.org/abs/2509.14448), 2025-09-17 | 19/30 | Full text verified | VC domain benchmark 有领域价值，但不改变平台 evaluation 的可执行性、uncertainty 或 evidence contract。 | `PLATFORM-EVALUATION-SYSTEM` |
| DeepRefusal | [arXiv:2509.15202](https://arxiv.org/abs/2509.15202), 2025-09-18 | 19/30 | Full text verified | probabilistic refusal-direction ablation 是 safety fine-tuning case；对 generalization/adaptive attack 与 utility trade-off 的证据不足，暂不改变 defense-in-depth 结论。 | `PLATFORM-SECURITY` |
| Geometric Image Caption Synthesis | [arXiv:2509.15217](https://arxiv.org/abs/2509.15217), 2025-09-18 | 18/30 | Full text verified | 几何 caption synthesis 是窄域 multimodal data recipe，尚不足以改变通用 representation/data provenance 主线。 | `MULTIMODAL-REPRESENTATION` |
| Black-box Layers via Low-rank Surrogate Optimization | [arXiv:2509.15113](https://arxiv.org/abs/2509.15113), 2025-09-18 | 19/30 | Full text verified | low-rank surrogate + zero-order optimization 解决不可微 black-box layer，但适用面与规模证据有限，未改变主流 backprop/training-system contract。 | `TRAIN-PRETRAINING` |
| Cognitive-Failure Diagnostics for Multi-Agent Expert Systems | [arXiv:2509.15366](https://arxiv.org/abs/2509.15366), 2025-09-18 | 19/30 | Full text verified | expert-gold、controlled mutation、LLM judge 与 vectorized recommendation map 有诊断价值，但只在 recruiting assistant 展示，未建立可迁移的 MAS failure taxonomy 或 executable verifier。 | `PLATFORM-EVALUATION-SYSTEM` |
| Beyond Spurious Signals in Multimodal Learning | [arXiv:2509.15361](https://arxiv.org/abs/2509.15361), 2025-09-18 | 19/30 | Full text verified | counterfactual mediation 与 modality-expert routing 是 sarcasm/sentiment 的 task-specific debiasing case，未形成可跨 workload 验证的 representation/provenance contract。 | `MULTIMODAL-REPRESENTATION` |
| SmolRGPT | [arXiv:2509.15490](https://arxiv.org/abs/2509.15490), 2025-09-18 | 19/30 | Full text verified | 600M RGB/depth VLM 与三阶段 curriculum 展示 warehouse spatial reasoning，但 model/domain/benchmark 过窄，缺 physical control 与 safety evidence。 | `MULTIMODAL-EMBODIED-VLA` |
| Explainable Supervisory Control | [arXiv:2509.15491](https://arxiv.org/abs/2509.15491), 2025-09-18 | 19/30 | Full text verified | timed-automata supervisor、Lyapunov/SMC 与解释 predictor 是 spacecraft/AUV control case；不改变通用 AI-system agent/control owner，且 domain assumptions 很强。 | `MULTIMODAL-EMBODIED-VLA` |
| NUMINA | [arXiv:2509.16656](https://arxiv.org/abs/2509.16656), 2025-09-20 | 19/30 | Full text verified | 3D numerical/spatial benchmark 与 NUMINA-Flow 的 rewrite/self-check pipeline 有数据治理意义，但仍是 domain benchmark，未改变平台级 executable evaluation contract。 | `PLATFORM-EVALUATION-SYSTEM` |
| End-to-End Combinatorial Optimization Solvers | [arXiv:2509.16865](https://arxiv.org/abs/2509.16865), 2025-09-21 | 19/30 | Full text verified | SFT + feasibility/optimality-aware RL 覆盖 7 类 NP-hard problems，但结论高度绑定 solver domain、instance generator 与 verifier，不能提升为通用 agent planning 机制。 | `AGENT-PLANNING` |
| Audio-Visual Navigation with Stereo Attention | [arXiv:2509.16924](https://arxiv.org/abs/2509.16924), 2025-09-21 | 19/30 | Full text verified | stereo attention 与 audio-guided fusion 在 Replica/Matterport3D 是 narrow navigation case，缺 sim-to-real、control deadline 与 safety envelope。 | `MULTIMODAL-EMBODIED-VLA` |
| Governing Automated Strategic Intelligence | [arXiv:2509.17087](https://arxiv.org/abs/2509.17087), 2025-09-21 | 18/30 | Full text verified | preliminary uplift/governance taxonomy 主要是 scoping argument，缺可执行 threat model、operating point 与 system mechanism，暂不进入长期治理主线。 | `PLATFORM-SECURITY` |
| Shall We Play a Game? | [arXiv:2509.17192](https://arxiv.org/abs/2509.17192), 2025-09-21 | 18/30 | v1 identity and revision history verified | 当前后续版本的 scoping scope 已纳入 2026 文献，不能倒灌为 v1 证据；v1 本身未形成足够系统机制，按 revision-sensitive review 关闭。 | `PLATFORM-SECURITY` |
| Can Agents Judge Systematic Reviews Like Humans? | [arXiv:2509.17240](https://arxiv.org/abs/2509.17240), 2025-09-21 | 18/30 | Full text verified | 比较 agents 与 humans 做 systematic-review judgments 是领域 evaluation case；judge reliability、domain scope 与 workflow external validity 不足以改变通用 evidence contract。 | `PLATFORM-EVALUATION-SYSTEM` |
| AI-assisted Nursing Skills Assessment | [arXiv:2509.16810](https://arxiv.org/abs/2509.16810), 2025-09-20 | 18/30 | Identity/date and relevant method/evaluation scope verified | 从 action recognition 到 subaction/procedural reasoning 的 curriculum 只在 synthesized nursing videos 验证；真实临床 variability、safety 与 instructor ground truth 不足。 | `PLATFORM-EVALUATION-SYSTEM` |
| LLMs as Layout Designers / LaySPA | [arXiv:2509.16891](https://arxiv.org/abs/2509.16891), 2025-09-21 | 19/30 | v1 identity, revision history, and relevant scope verified | hybrid geometric/structural/visual rewards 与 GRPO 是 graphic-layout domain case；v2-v4 扩展不倒灌 v1，且不改变通用 post-training contract。 | `TRAIN-GRPO` |
| Quantum Abduction | [arXiv:2509.16958](https://arxiv.org/abs/2509.16958), 2025-09-21 | 17/30 | Identity/date, revision history, and evidence scope verified | superposition/interference/collapse 主要是 conceptual analogy 与 case studies，缺可反驳的 system implementation、baseline 和 executable evaluation，不提升为 uncertainty mechanism。 | `WORLDVIEW-LLM-INTELLIGENCE` |
| KAHAN Financial Data Narration | [arXiv:2509.17037](https://arxiv.org/abs/2509.17037), 2025-09-21 | 19/30 | Identity/date, artifact, and relevant evaluation scope verified | entity/pair/group/system hierarchical narration 在 DataTales 和 healthcare transfer 有价值，但 factuality 依赖 domain knowledge、GPT-4o judge 与 task construction，未形成通用 RAG/evidence contract。 | `AGENT-RAG` |
| Domain-Landmark Graph Learning | [arXiv:2509.17062](https://arxiv.org/abs/2509.17062), 2025-09-21 | 19/30 | Identity/date and relevant method/evaluation scope verified | probabilistic lifted landmark ordering graph 改善 classical planning domain reuse，但 precision/recall evaluation 与 symbolic assumptions 不足以改变 LLM-agent planning owner。 | `AGENT-PLANNING` |
| RALLM-POI | [arXiv:2509.17066](https://arxiv.org/abs/2509.17066), 2025-09-21 | 19/30 | Identity/date, code, and relevant evaluation scope verified | trajectory retrieval、geographic reranking 与 self-rectification 是 Foursquare POI domain recipe；没有形成超越已有 retrieval/rerank/verify 主线的新 state contract。 | `AGENT-RAG` |
| Intention-aware Hierarchical Diffusion for Trajectory Anomaly Detection | [arXiv:2509.17068](https://arxiv.org/abs/2509.17068), 2025-09-21 | 19/30 | Identity/date and relevant method/evaluation scope verified | inverse-Q high-level intent + diffusion sub-trajectory reconstruction 是 anomaly-detection domain composition；作者最高 30.2% F1 改善绑定数据与 baselines，不能提升为通用 world model。 | `MULTIMODAL-WORLD-MODELS` |

## Evidence Level

- **Level A — Official interface/version evidence:** GPT-5-Codex、PyTorch/TorchAO 与 Kubernetes DRA。只证明公开版本、API、workflow 或官方 workload 中的行为；机制未披露处固定为 `Version Fact / Mechanism Not Disclosed` 或 `Partially Disclosed`。
- **Level B — Primary research with full-text review:** 42 个 retained arXiv families。结论均为作者实验/分析；performance、safety、accuracy、energy、latency 与 throughput 不提升为普遍事实。
- **Level C — Verified low-score research:** 40 个 low-score families。身份与日期已闭合，但因 novelty、scope、evaluation contract 或 project relevance 不到门槛而拒绝。
- **Project inference:** source-family evolution、canonical owner 与跨章 handoff 是本项目分析，已与 source fact 分开。

## Cross-Week Deduplication and Spillback Ledger

### Earlier Owners — Not Scored in W38

| Source Family | Primary Identifier | First Public | Correct Owner | W38 Handling |
| --- | --- | --- | --- | --- |
| Small Language Models are the Future of Agentic AI | arXiv:2506.02153v1 | 2025-06-02 | 2025-W23 | 本周发现/传播，回拨 W23；W38 不重复评分。 |
| Medha | arXiv:2409.17264v1 | 2024-09-25 | 2024-W39 | 旧论文，不属于 2025 owner window。 |
| ActLCD | arXiv:2505.23657v1 | 2025-05-29 | 2025-W22 | 后续讨论仅作 revision relation。 |
| StreamBridge | arXiv:2505.05467v1 | 2025-05-08 | 2025-W19 | W38 不重复计分。 |
| SEAL | arXiv:2506.10943v1 | 2025-06-12 | 2025-W24 | W38 不重复计分。 |
| Pimba | arXiv:2507.10178v1 | 2025-07-14 | 2025-W29 | W38 不重复计分。 |
| JoPA | arXiv:2405.20404v1 | 2024-05-31 | 2024-W22 | 旧论文，不属于 2025 owner window。 |
| DeepSeek-R1 | arXiv:2501.12948v1 | 2025-01-22 | 2025-W04 | 本周 Nature formal publication 是同一 family 的后续 publication node，不重计机制分。 |

### W38-Owned Revisions

- Fun-ASR v2（2025-09-17）仍在同周且与 v1 合并；v3/v4 仅记录 revision。
- Reasoning-Aware Compression v2（2026-05-02）、Legal-Critical Software v2、CoopQ v2、TDRM v2、RPG v2、HAPO v2 与 SWE-Bench Pro v2 等后续版本均保留 W38 owner；later text 不能伪装成 v1 已公开事实。
- W39 look-ahead 先回拨 9 个明确 W38 owner，随后完整 feed replay 又恢复 29 个同周漏项；38 项均已进入本周评分、Full Source Review 或低分 closure，不留 spillback pending。
- W39 边界反查确认 `2509.17318` CogAtom、`2509.17393` Program Synthesis 与 `2509.17567` LIMI 的 v1 均为 2025-09-22，owner=2025-W39，W38 不重复评分。
- 与 W37/W39 的 88 个 Source Family ID 交叉检查无重复；DRA 与 W35/W36 通过 feature-specific IDs 保持 core GA、health alpha、capacity alpha 的演进关系。

## Knowledge Tree Position

| Route | Canonical Owner | W38 Evidence |
| --- | --- | --- |
| Multimodal representation / integrity | `MULTIMODAL-REPRESENTATION` Ch23 | Fun-ASR、Phi handoff |
| Multimodal generation / embodied loop | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 → `MULTIMODAL-EMBODIED-VLA` Ch26 | MANZANO、audio DLM、Ask-to-Clarify、VLAC、Robot Control Stack |
| Conditional capacity | `MODEL-MOE` Ch21 → `INFER-SCHEDULING` Ch56 | RoE stochastic expert branches |
| Data and pretraining | `TRAIN-DATA` Ch27 → `TRAIN-PRETRAINING` Ch28 | Synthetic Bootstrapped Pretraining、Infinite Compute |
| Post-training reward / process supervision | `TRAIN-RLHF` Ch31 → `TRAIN-GRPO` Ch33 | TARL、TDRM、FlowRL、BaseReward、HAPO、SMART |
| Decode / execution plan / quantization | `INFER-DECODE` Ch44 → `INFER-TENSORRT-LLM` Ch49 | DSCC-HS、RAC、CoopQ、LEAP、Intel quant |
| Typed state and scheduling | `INFER-GPU-MEMORY` Ch54 → `INFER-SCHEDULING` Ch56 | Opportunistic context management、ATTS |
| Artifact identity | `PLATFORM-MODEL-REGISTRY` Ch59 | TorchAO recipes、PT2 compile cache handoff |
| Resource contract | `PLATFORM-GPU-SCHEDULER` Ch63 | DRA health/capacity |
| Evidence / trace | `PLATFORM-EVALUATION-SYSTEM` Ch66 → `PLATFORM-TRACE` Ch69 | Graph confidence、FAMAS、FESTA、seqBench、SWE-Bench Pro、AgentSeer handoff |
| Multi-tenancy / security | `PLATFORM-MULTI-TENANT` Ch71 → `PLATFORM-SECURITY` Ch72 | Participant-aware ACL、Phi、Evil Vizier、FJD、M-Spoiler、AgentSeer |
| Planning / workflow / platform | `AGENT-PLANNING` Ch79 → `AGENT-WORKFLOW` Ch81 → `AGENT-PLATFORM` Ch84 | H2R、RPG、MCTS-EP、ARE、prompt-driven video editing、Legal-Critical Software、InfraMind、GPT-5-Codex |

## Independent Review and Weekly Evidence Gate

### Mechanical Review

- **ISO window:** 2025-09-15～2025-09-21 = Monday～Sunday，passed。
- **Candidate count:** 88 scoring rows，编号 1～88 连续，无 duplicate row。
- **Score arithmetic:** 六维之和与 `Total` 对齐；25～30 = 38，20～24 = 10，低于 20 = 40。
- **Review coverage:** 48/48 retained rows 有 Full Source Review；40/40 low-score rows 有 primary ID、v1 date、score 与 rejection closure。
- **Pending state:** `Review Pending = 0`；`Unverified / Blocked = 0`；`Disputed = 0`。
- **Source family:** 88 个评分行对应 88 个唯一 family；revision 不重复计分；DRA feature families 与 core DRA family 不混写。
- **Dates and revisions:** 所有 arXiv owner 使用 v1；official events 使用页面发布日期；later revisions 只作 lineage。
- **Evidence boundary:** 作者/厂商数字均绑定已披露 workload；未披露 hardware/model/precision/length/batch/concurrency/SLO 明示 `Not Disclosed`。
- **ROADMAP mapping:** retained 与 low-score candidates 均有 Stable Node owner；当前章节号与 legacy mapping 对 48 个 retained reviews 已核对。
- **Markdown:** 标题层级、表格、代码围栏、URL 与 trailing whitespace 进入最终机械检查。

### Gate Result

`2025-W38 Weekly Evidence Gate: Passed`。

该状态只表示 W38 discovery、source review、评分、去重与 evidence boundary 闭合；不表示 2025 年度 archive 完成，也不表示 Books Integration 完成。Historical Books Gate 继续关闭。

## Recommended Action

- **Must Read / later Books Gate重点比较:** Synthetic Bootstrapped Pretraining、ATTS、participant-aware ACL、PT2 compilation cache identity、DRA consumable capacity、RPG、SWE-Bench Pro、ARE、AgentSeer 与 RoE。
- **Mechanism candidates:** RAC 的 workload-aware calibration、FAMAS/AgentSeer 的 action-level attribution、BaseReward/HAPO/SMART 的 reward-policy coupling、MANZANO 的 typed multimodal identity、VLAC 的 process critic、opportunistic inference 与 RoE 的 shared-state branching。
- **Security candidates:** Phi、Evil Vizier、FJD、M-Spoiler 与 AgentSeer 必须绑定 threat model、harness opportunity、tool permissions 与 operating point，不能写成单一 detector/guardrail 即可解决。
- **Experimental hold:** Fun-ASR、InfraMind、DSCC-HS、Infinite Compute、Robot Control Stack、FESTA、Decoding Uncertainty、Roundtable、M-Spoiler、seqBench 与 prompt-driven video editing 保留研究证据；更强独立复现或系统 contract 前不进入核心结论。
- **Low-score closure:** 40 项不进入 Full Source Review；若未来 family 产生新的 primary evidence，应回到首次 owner 周升级，而不是在新周重复建立事件。

## Event-Date Daily Decision

Historical Backfill 不创建 2025 Daily。所有 W38 owner evidence 直接保存在本 Weekly；W31/W32 live Daily 同步规则不适用于本历史周。

## Books Integration Decision

`Historical Books Gate: Closed`。本轮没有修改 Books，也没有把 Weekly 摘要直接写进长期知识库。

- `Books Pending — Integration Deferred` 表示 source review 已闭合但等待年度 Historical Evidence Gate 后逐 family 比较目标与相邻章节。
- `Weekly Only — Version Fact / Mechanism Partially Disclosed` 表示只能沉淀版本事实，不能反推内部实现。
- `Emerging / Experimental` 表示机制值得保留但证据不足以稳定改变书稿。
- `Reject` 只关闭本周候选，不否认后续版本可能形成新证据。

## Ignored Noise

- 转载、新闻摘要、榜单、social-media claims、无 primary identifier 的项目与未绑定 workload 的 benchmark 宣传未进入评分。
- 常规 patch/release-note 功能列表若不改变 state、data/control flow、failure model 或系统 contract，不为增加候选数量而计分。
- 已有 source family 的正式发表、媒体重发和 later revision 不作为新事件；必要信息进入 spillback/revision ledger。

## Repository Changes

- 仅重建 `papers/2025/weekly/2025-W38/README.md`。
- 将原 2 个评分行扩展为 88 个经核验候选；完成 48 个 Full Source Review、40 个低分 closure、8 个 earlier-owner spillback、38 个 W38 owner omission recovery 与 W39 look-ahead boundary closure。
- 未修改年度索引、Books、`docs/LEARNING_STATE.md` 或相邻 Weekly；未 stage、commit、push、reset、checkout 或 clean。

## Open Questions

- workload-aware calibration 是否能用统一 contract 同时约束 accuracy、reasoning length、kernel speedup 与 deployment cost？
- graph/process reward 的 confidence 如何把 dependency、judge error 与 calibration drift纳入，而不是把多个 90% 分数简单相乘？
- derived training data、derived agent memory 与 compiled artifact 能否共享 provenance、supersession、invalidation 和 rollback 模型？
- asynchronous verification 与 context-local scheduling 如何同时满足 tenant fairness、deadline 与 failure recovery？
- participant-aware authorization 如何扩展到 fine-tuned weights、embedding/index、shared KV/cache 与 generated artifacts？
- DRA 的 nominal capacity、runtime health 与真实 QoS enforcement 如何在 controller 中闭环而不 oscillate？
- repository planning graph、agent action graph 与 executable benchmark environment 能否共享 version、provenance、supersession 与 rollback contract？

## Missing Materials Request Ledger

None。W38 没有仍需用户补充的 P0 Identity、P1 Full Text、P2 Artifact 或 P3 Revision blocker。

## Sources

### 模型与研究机构

- GPT-5-Codex release — https://openai.com/index/introducing-upgrades-to-codex/（First Public: 2025-09-15；Accessed: 2026-08-24）
- GPT-5-Codex system-card addendum — https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/（First Public: 2025-09-15；Accessed: 2026-08-24）
- Fun-ASR Technical Report — https://arxiv.org/abs/2509.12508（v1: 2025-09-15；Accessed: 2026-08-24）

### 论文与学术来源

- Phi — https://arxiv.org/abs/2509.12521（v1: 2025-09-15；Accessed: 2026-08-24）
- Reasoning-Aware Compression — https://arxiv.org/abs/2509.12464（v1: 2025-09-15；Accessed: 2026-08-24）
- C3T — https://arxiv.org/abs/2509.12171（v1: 2025-09-15；Accessed: 2026-08-24）
- RAGs to Riches — https://arxiv.org/abs/2509.12168（v1: 2025-09-15；Accessed: 2026-08-24）
- MedicalOS — https://arxiv.org/abs/2509.11507（v1: 2025-09-15；Accessed: 2026-08-24）
- Pointing Gestures — https://arxiv.org/abs/2509.12507（v1: 2025-09-15；Accessed: 2026-08-24）
- Legal-Critical Software — https://arxiv.org/abs/2509.13471（v1: 2025-09-16；Accessed: 2026-08-24）
- Graph-Based Confidence — https://arxiv.org/abs/2509.12908（v1: 2025-09-16；Accessed: 2026-08-24）
- H2R — https://arxiv.org/abs/2509.12810（v1: 2025-09-16；Accessed: 2026-08-24）
- Opportunistic GPU Inference — https://arxiv.org/abs/2509.13201（v1: 2025-09-16；Accessed: 2026-08-24）
- Logical Reasoning Cost — https://arxiv.org/abs/2509.12645（v1: 2025-09-16；Accessed: 2026-08-24）
- Multi-Agent Prompt-Injection Defense — https://arxiv.org/abs/2509.14285（v1: 2025-09-16；Accessed: 2026-08-24）
- Reversible Deep Equilibrium Models — https://arxiv.org/abs/2509.12917（v1: 2025-09-16；Accessed: 2026-08-24）
- Black-box Model Merging — https://arxiv.org/abs/2509.12951（v1: 2025-09-16；Accessed: 2026-08-24）
- Bi-level Federated Personalization — https://arxiv.org/abs/2509.12697（v1: 2025-09-16；Accessed: 2026-08-24）
- Token-Level Differential Privacy — https://arxiv.org/abs/2509.12958（v1: 2025-09-16；Accessed: 2026-08-24）
- Radiology Data Scaling — https://arxiv.org/abs/2509.12818（v1: 2025-09-16；Accessed: 2026-08-24）
- HPIM — https://arxiv.org/abs/2509.12993（v1: 2025-09-16；Accessed: 2026-08-24）
- Synthetic Bootstrapped Pretraining — https://arxiv.org/abs/2509.15248（v1: 2025-09-17；Accessed: 2026-08-24）
- Process-Supervised Tool-Use RL — https://arxiv.org/abs/2509.14480（v1: 2025-09-17；Accessed: 2026-08-24）
- FAMAS — https://arxiv.org/abs/2509.13782（v1: 2025-09-17；Accessed: 2026-08-24）
- InfraMind — https://arxiv.org/abs/2509.13704（v1: 2025-09-17；Accessed: 2026-08-24）
- DSCC-HS — https://arxiv.org/abs/2509.13702（v1: 2025-09-17；Accessed: 2026-08-24）
- Prosocial Ability Profiles — https://arxiv.org/abs/2509.14485（v1: 2025-09-17；Accessed: 2026-08-24）
- CAMPUS — https://arxiv.org/abs/2509.13790（v1: 2025-09-17；Accessed: 2026-08-24）
- PromptSE — https://arxiv.org/abs/2509.13680（v1: 2025-09-17；Accessed: 2026-08-24）
- AgentCTG — https://arxiv.org/abs/2509.13677（v1: 2025-09-17；Accessed: 2026-08-24）
- Helpfulness-Exploiting Jailbreak — https://arxiv.org/abs/2509.14297（v1: 2025-09-17；Accessed: 2026-08-24）
- TENET — https://arxiv.org/abs/2509.13765（v1: 2025-09-17；Accessed: 2026-08-24）
- FlowDrive — https://arxiv.org/abs/2509.14303（v1: 2025-09-17；Accessed: 2026-08-24）
- VCBench — https://arxiv.org/abs/2509.14448（v1: 2025-09-17；Accessed: 2026-08-24）
- CoopQ — https://arxiv.org/abs/2509.15455（v1: 2025-09-18；Accessed: 2026-08-24）
- FlowRL — https://arxiv.org/abs/2509.15207（v1: 2025-09-18；Accessed: 2026-08-24）
- Evil Vizier — https://arxiv.org/abs/2509.15213（v1: 2025-09-18；Accessed: 2026-08-24）
- TDRM — https://arxiv.org/abs/2509.15110（v1: 2025-09-18；Accessed: 2026-08-24）
- Pre-training under Infinite Compute — https://arxiv.org/abs/2509.14786（v1: 2025-09-18；Accessed: 2026-08-24）
- ATTS — https://arxiv.org/abs/2509.15148（v1: 2025-09-18；Accessed: 2026-08-24）
- LEAP — https://arxiv.org/abs/2509.14781（v1: 2025-09-18；Accessed: 2026-08-24）
- Participant-Aware Access Control — https://arxiv.org/abs/2509.14608（v1: 2025-09-18；Accessed: 2026-08-24）
- LLM Jailbreak Detection for (Almost) Free — https://arxiv.org/abs/2509.14558（v1: 2025-09-18；Accessed: 2026-08-24）
- DeepRefusal — https://arxiv.org/abs/2509.15202（v1: 2025-09-18；Accessed: 2026-08-24）
- Geometric Image Caption Synthesis — https://arxiv.org/abs/2509.15217（v1: 2025-09-18；Accessed: 2026-08-24）
- Black-box Layers via Low-rank Surrogate Optimization — https://arxiv.org/abs/2509.15113（v1: 2025-09-18；Accessed: 2026-08-24）
- Ask-to-Clarify — https://arxiv.org/abs/2509.15061（v1: 2025-09-18；Accessed: 2026-08-24）
- Fast and Fluent Diffusion Language Models — https://arxiv.org/abs/2509.15188（v1: 2025-09-18；Accessed: 2026-08-24）
- Robot Control Stack — https://arxiv.org/abs/2509.14932（v1: 2025-09-18；Accessed: 2026-08-24）
- Cognitive-Failure Diagnostics for Multi-Agent Expert Systems — https://arxiv.org/abs/2509.15366（v1: 2025-09-18；Accessed: 2026-08-24）
- Beyond Spurious Signals — https://arxiv.org/abs/2509.15361（v1: 2025-09-18；Accessed: 2026-08-24）
- SmolRGPT — https://arxiv.org/abs/2509.15490（v1: 2025-09-18；Accessed: 2026-08-24）
- Explainable Supervisory Control — https://arxiv.org/abs/2509.15491（v1: 2025-09-18；Accessed: 2026-08-24）
- RPG — https://arxiv.org/abs/2509.16198（v1: 2025-09-19；Accessed: 2026-08-24）
- RPG-ZeroRepo artifact — https://github.com/microsoft/RPG-ZeroRepo（Accessed: 2026-08-24）
- MANZANO — https://arxiv.org/abs/2509.16197（v1: 2025-09-19；Accessed: 2026-08-24）
- BaseReward — https://arxiv.org/abs/2509.16127（v1: 2025-09-19；Accessed: 2026-08-24）
- VLAC — https://arxiv.org/abs/2509.15937（v1: 2025-09-19；Accessed: 2026-08-24）
- M-Spoiler — https://arxiv.org/abs/2509.16494（v1: 2025-09-20；Accessed: 2026-08-24）
- HAPO — https://arxiv.org/abs/2509.16591（v1: 2025-09-20；Accessed: 2026-08-24）
- Audio-Conditioned Diffusion Language Models — https://arxiv.org/abs/2509.16622（v1: 2025-09-20；Accessed: 2026-08-24）
- FESTA — https://arxiv.org/abs/2509.16648（v1: 2025-09-20；Accessed: 2026-08-24）
- NUMINA — https://arxiv.org/abs/2509.16656（v1: 2025-09-20；Accessed: 2026-08-24）
- Decoding Uncertainty — https://arxiv.org/abs/2509.16696（v1: 2025-09-20；Accessed: 2026-08-24）
- SMART — https://arxiv.org/abs/2509.16742（v1: 2025-09-20；Accessed: 2026-08-24）
- Roundtable Policy — https://arxiv.org/abs/2509.16839（v1: 2025-09-20；Accessed: 2026-08-24）
- End-to-End Combinatorial Optimization Solvers — https://arxiv.org/abs/2509.16865（v1: 2025-09-21；Accessed: 2026-08-24）
- seqBench — https://arxiv.org/abs/2509.16866（v1: 2025-09-21；Accessed: 2026-08-24）
- Audio-Visual Navigation — https://arxiv.org/abs/2509.16924（v1: 2025-09-21；Accessed: 2026-08-24）
- SWE-Bench Pro — https://arxiv.org/abs/2509.16941（v1: 2025-09-21；Accessed: 2026-08-24）
- Governing Automated Strategic Intelligence — https://arxiv.org/abs/2509.17087（v1: 2025-09-21；Accessed: 2026-08-24）
- MCTS-EP — https://arxiv.org/abs/2509.17116（v1: 2025-09-21；Accessed: 2026-08-24）
- ARE — https://arxiv.org/abs/2509.17158（v1: 2025-09-21；Accessed: 2026-08-24）
- Shall We Play a Game? — https://arxiv.org/abs/2509.17192（v1: 2025-09-21；Accessed: 2026-08-24）
- RoE — https://arxiv.org/abs/2509.17238（v1: 2025-09-21；Accessed: 2026-08-24）
- Can Agents Judge Systematic Reviews Like Humans? — https://arxiv.org/abs/2509.17240（v1: 2025-09-21；Accessed: 2026-08-24）
- Mind the Gap / AgentSeer — https://arxiv.org/abs/2509.17259（v1: 2025-09-21；Accessed: 2026-08-24）
- Prompt-Driven Agentic Video Editing — https://arxiv.org/abs/2509.16811（v1: 2025-09-20；Accessed: 2026-08-24）
- AI-assisted Nursing Skills Assessment — https://arxiv.org/abs/2509.16810（v1: 2025-09-20；Accessed: 2026-08-24）
- LLMs as Layout Designers / LaySPA — https://arxiv.org/abs/2509.16891（v1: 2025-09-21；Accessed: 2026-08-24）
- Quantum Abduction — https://arxiv.org/abs/2509.16958（v1: 2025-09-21；Accessed: 2026-08-24）
- KAHAN — https://arxiv.org/abs/2509.17037（v1: 2025-09-21；Accessed: 2026-08-24）
- Domain-Landmark Graph Learning — https://arxiv.org/abs/2509.17062（v1: 2025-09-21；Accessed: 2026-08-24）
- RALLM-POI — https://arxiv.org/abs/2509.17066（v1: 2025-09-21；Accessed: 2026-08-24）
- Intention-aware Hierarchical Diffusion — https://arxiv.org/abs/2509.17068（v1: 2025-09-21；Accessed: 2026-08-24）

### AI Infra 与工程项目

- Intel CPU Quantized LLM Inference — https://pytorch.org/blog/high-performance-quantized-llm-inference-on-intel-cpus-with-native-pytorch/（First Public: 2025-09-17；Accessed: 2026-08-24）
- PT2 Compilation Time — https://pytorch.org/blog/experience-in-reducing-pt2-compilation-time-for-meta-internal-workloads/（First Public: 2025-09-18；Accessed: 2026-08-24）
- TorchAO Quantization Recipes — https://pytorch.org/blog/torchao-quantized-models-and-quantization-recipes-now-available-on-huggingface-hub/（First Public: 2025-09-19；Accessed: 2026-08-24）
- DRA Resource Health — https://kubernetes.io/blog/2025/09/17/kubernetes-v1-34-pods-report-dra-resource-health/（First Public: 2025-09-17；Accessed: 2026-08-24）
- DRA Consumable Capacity — https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/（First Public: 2025-09-18；Accessed: 2026-08-24）
