# 2026-06-09 V3 recovered-candidate evidence

本包覆盖最终 denominator 中 38 个 closure-recovered Candidate。37 项读取 official exact-v1 HTML；2606.09483 的主站 body/PDF 连续超时后，改由同属 arXiv 官方域的 `export.arxiv.org` exact-v1 PDF 恢复正文，不用旧 trace 补权。第二轮全表复核将 2606.07909、2606.08300 与 2606.08702 降回 pre-denominator closure；其中前两项曾进入本恢复包，以下不再保留其 Source Review。

## Enabling KV Caching of Shared Prefix for Diffusion Language Models

- **Identity / Method：** `arXiv:2606.07571v1`；§4 Observations、§5 BiCache。浅层 exact-prefix KV 在高相似度区域复用；共享前缀比例决定安全层深，深层按刷新间隔重算。
- **Evaluation：** §6；LLaDA、B200 180GB、batch=1、generation length=256、steps=128；相对无缓存报告 36.3%～82.8% 加速，组合路径最高 98.3%，准确率差异 0～1.8%。
- **Limitations：** §9；exact prefix、offline profiling、单一 LLaDA family/current DLM ecosystem，不外推其他 architecture、accelerator 或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-KV-CACHE`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs

- **Identity / Method：** `arXiv:2606.07577v1`；正文定位：1 Introduction；2 Related Work。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 5 Results；5.1 Main Results。
- **Limitations：** 6 Conclusion；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-KV-CACHE`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Training-Inference Kernel Contracts: Bounding Divergence in Post-Training and Deployment

- **Identity / Method：** `arXiv:2606.07581v1`；正文定位：8 Experimental protocol；Reproducibility and implementation matters in RL.。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 7.3 Observability and continuous re-evaluation。
- **Limitations：** 11 Limitations；12 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-TENSORRT-LLM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs

- **Identity / Method：** `arXiv:2606.07586v1`；正文定位：IV Skill System。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** V Evaluation。
- **Limitations：** VI Conclusion and Future Work；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## The Routing Plateau: Understanding and Breaking the Accuracy Limits of LLM Routers

- **Identity / Method：** `arXiv:2606.07587v1`；正文定位：Detailed method comparison: the top tier is nearly indistinguishable.。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Routing benchmarks and analysis.；4.1 Routers, Benchmarks, and Evaluation Methods。
- **Limitations：** 6.4 Discussion: Gap to the oracle；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-SCHEDULING`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference

- **Identity / Method：** `arXiv:2606.07665v1`；§2–§3。LLM 只给 metadata、ranking 与参数建议；compiler/runtime 构造 bounded candidates，负责模板、静态检查、验证、benchmark 与 fallback，不让 LLM 直接准入可执行 CUDA。
- **Evaluation：** §4；A800 SXM4 80GB、FP16，Llama3.2 1B/3B 与 Qwen3 1.7B/4B，输入 128～40960、输出 32～32768；full hybrid 相对 vLLM 约 1.06～1.07×，消融未独立隔离 LLM guidance。
- **Limitations：** §7；prototype、Transformer region、unsupported fallback，搜索不保证 optimal。
- **Books：** `已有覆盖`，owner=`INFER-TENSORRT-LLM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Fast LLM-Based Semantic Filtering: From a Unified Framework to an Adaptive Two-Phase Method

- **Identity / Method：** `arXiv:2606.08090v1`；正文定位：3. Semantic Filtering and a Unified Framework；3.3. A Unified Algorithmic Framework。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Headline empirical result.。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-SCHEDULING`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention

- **Identity / Method：** `arXiv:2606.09079v1`；正文定位：1 Introduction；2 Methodology。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 3.2 Primary Results: Breaking the Capacity Wall。
- **Limitations：** 3.3 Limitations and Diagnostics；4 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-KV-CACHE`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy

- **Identity / Method：** `arXiv:2606.09080v1`；正文定位：4 Inference Implementation；Appendix B Implementation Details。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Evaluation Settings.。
- **Limitations：** 6 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning

- **Identity / Method：** `arXiv:2606.09138v1`；正文定位：3.2. Design Principles；3.3. System Overview。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Not Disclosed in accessible exact-v1 material。
- **Limitations：** 5. Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`TRAIN-GRPO`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Resource-aware Computation-Communication Overlap for multi-GPU ML Workloads

- **Identity / Method：** `arXiv:2606.09200v1`；正文定位：1 Introduction；2 Background。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4 Experimental Results。
- **Limitations：** 6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`TRAIN-DISTRIBUTED-TRAINING`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs

- **Identity / Method：** `arXiv:2606.09508v1`；正文定位：1 Introduction；2 Related Work。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4.4 Complexity Analysis；5 Experiment。
- **Limitations：** 6 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-KV-CACHE`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference

- **Identity / Method：** `arXiv:2606.09514v1`；正文定位：4 Method；4.1 Framework Overview。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 5.2 Analysis；5.2.1 Speed Analysis。
- **Limitations：** 6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-TENSORRT-LLM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing

- **Identity / Method：** `arXiv:2606.09551v1`；正文定位：Our Approach.；Appendix F Full Compilation Protocol。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Results.；4.5 Two-Call Evaluation Theorem。
- **Limitations：** 7 Conclusion；Discussion.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Rosetta Memory: Adaptive Memory for Cross-LLM Agents

- **Identity / Method：** `arXiv:2606.07711v1`；正文定位：4.1 Implementation of f read f_{\mathrm{read}} and f write f_{\mathrm{write}}；Implementation Details.。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Not Disclosed in accessible exact-v1 material。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents

- **Identity / Method：** `arXiv:2606.08151v1`；正文定位：1 Introduction。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Not Disclosed in accessible exact-v1 material。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures

- **Identity / Method：** `arXiv:2606.08275v1`；正文定位：1 Introduction；Contributions.。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 5 Validation against ground truth。
- **Limitations：** 7 Limitations；8 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-TRACE`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Autonomous Incident Resolution at Hyperscale: An Agentic AI Architecture for Network Operations

- **Identity / Method：** `arXiv:2606.09122v1`；正文定位：III Architecture；III-A System Overview。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** VI Evaluation。
- **Limitations：** VIII Discussion；VIII-B Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents

- **Identity / Method：** `arXiv:2606.09316v1`；正文定位：3 Method。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4.2 Experimental Analysis。
- **Limitations：** 5 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## What Should a Skill Remember? Quality--Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents

- **Identity / Method：** `arXiv:2606.09421v1`；§3。profile task/skill 后选择 source-native、workflow、API/code、rule/formula preservation anchor，并审计缺失 anchor；目标是受约束的 quality–cost utility，而非最短 rewrite。
- **Evaluation：** §4；SkillsBench 88 skills、86 runnable，固定 task/environment/verifier，覆盖 Gemini 3 Flash/Pro、GPT-5.4 Codex 与 Claude Opus 4.6；held-out total cost -7%、downstream token -6%，cross-model 均值约 -14.7%/-13.7%。
- **Limitations：** 受控 textual skills；不覆盖动态资源、持续更新 skill、生产 latency/pricing/caching/hardware 或人工复核，lightweight audit 不能替代人工安全审阅。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning

- **Identity / Method：** `arXiv:2606.09447v1`；正文定位：3.2. WebAgent Framework。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 6. Evaluation；6.1. Single-Step Evaluation。
- **Limitations：** 7.4. Discussion；8. Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`TRAIN-GRPO`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents

- **Identity / Method：** `arXiv:2606.09483v1`；official export PDF §2 Method、§2.1 Cognitive Capability Hierarchy、§2.2 Synchronous Daytime Writer、§2.3 Asynchronous Nighttime Sweeper、§2.4 Read Path and Latency。
- **Evaluation：** §3 Experiments，含 §3.1 Setup、§3.2 Main Results、§3.3 Ablation 与 §3.4 Analysis。
- **Limitations：** 独立 Limitations；只覆盖披露的 vector store、benchmarks 与双进程 memory implementation，不外推到未列模型、真实用户隐私、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文的 episodic/semantic consolidation、在线写入/离线归并、visibility/commit 与读路径已覆盖。

## SecureClaw: Clawing Back Control of LLM Agents

- **Identity / Method：** `arXiv:2606.09549v1`；正文定位：3 SecureClaw Design；3.1 Design overview and component roles。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4.1 Main cross-benchmark results；A.2 Evaluation methodology。
- **Limitations：** 6 Limitations and broader impact；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Collaborative Human-Agent Protocol (CHAP)

- **Identity / Method：** `arXiv:2606.09751v1`；正文定位：1.1 The protocol gap；4 Protocol Architecture。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Not Disclosed in accessible exact-v1 material。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-WORKFLOW`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents

- **Identity / Method：** `arXiv:2606.07595v1`；正文定位：1 Introduction；Contributions.。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 3 Evaluation Setting；4 Tool Propagation Results。
- **Limitations：** 8 Limitations；10 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Finite Certificates for In-Context Determinacy and a Threshold Theory of Emergence in Language Models

- **Identity / Method：** `arXiv:2606.07623v1`；正文定位：1 Introduction；Contributions.。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Not Disclosed in accessible exact-v1 material。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?

- **Identity / Method：** `arXiv:2606.07682v1`；正文定位：3.3 Verification Design；4.3 Evaluation Protocol。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4.3 Evaluation Protocol；5 Experimental Results。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## When Behavioral Safety Evaluation Fails: A Representation-Level Perspective

- **Identity / Method：** `arXiv:2606.08044v1`；正文定位：KL implementation note.；C.1 Implementation details。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Behavioral evaluation does not detect dissociation.；4 Interventions for Safety Evaluation。
- **Limitations：** 7 Discussion；Limitations and Future Work.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Decoy-Calibrated Failure Audits for Language Models

- **Identity / Method：** `arXiv:2606.09046v1`；正文定位：Model and benchmark scope.；Appendix C Implementation notes。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Not Disclosed in accessible exact-v1 material。
- **Limitations：** 5 Limitations；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces

- **Identity / Method：** `arXiv:2606.09071v1`；§3。诊断 candidate 后执行 prefix-preserving targeted replay；diagnosis-specific faithfulness gate 阻止无关恢复，失败时 verified rollback，并以 contrastive explanation 更新诊断。
- **Evaluation：** §4；WTQ 137/119、GAIA 117/83、BBM 150/150、SWE 31/30，gpt-5.2 auditor/agent、temperature=0；主实验使用 oracle expected answer 与 exact-match localization。
- **Limitations：** Appendix R；结构化环境、oracle 依赖、不可逆副作用与缺失环境会阻止 replay；只处理 single earliest decisive error。Outcome flip 支持 intervention 的充分性，不证明归因唯一或最小。
- **Books：** `待整合`，owner=`PLATFORM-TRACE`；写入 prefix preservation、diagnosis-specific faithfulness gate 与 sufficiency/non-uniqueness 边界；`AGENT-REFLECTION` 只保留短 handoff。

## Precision Is Not Faithfulness: Coverage-Aware Evaluation of Grounded Generation with a Complete Oracle

- **Identity / Method：** `arXiv:2606.09376v1`；正文定位：6 Method: Verifier-Guided Generation；Small fine-tuned model and verifier-guided method (RQ3).。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Metric validation (offline).。
- **Limitations：** 11 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces

- **Identity / Method：** `arXiv:2606.09426v1`；正文定位：WeaveBench Benchmark；Appendix A Benchmark Construction。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Main Results；Failure Mechanism Analysis。
- **Limitations：** Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions

- **Identity / Method：** `arXiv:2606.09461v1`；正文定位：3.3 Task Design；A.4 Human Annotation Protocol。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4 Experiment；4.2 Experimental Results。
- **Limitations：** 5 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback

- **Identity / Method：** `arXiv:2606.09748v1`；正文定位：3 Experimental Framework。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 4.3 Main Results；4.4 Analysis。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## iOSWorld: A Benchmark for Personally Intelligent Phone Agents

- **Identity / Method：** `arXiv:2606.09764v1`；正文定位：3.3 Task Design。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** Evaluation.；4.2 Results。
- **Limitations：** 5 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## MC-PDD: Masked Corpus-Level Pretraining Data Detection for Black-Box Large Language Models

- **Identity / Method：** `arXiv:2606.07996v1`；正文定位：I Introduction；II Related Work。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** VI Results；VI-A Result on SteamMIA。
- **Limitations：** VIII Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`TRAIN-DATA`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models

- **Identity / Method：** `arXiv:2606.09401v1`；正文定位：4 Benchmark design and experiments；4.2 RQ2: Which DP adaptation method is the most protective?。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 5 Discussion of our Results。
- **Limitations：** 5 Discussion of our Results；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs

- **Identity / Method：** `arXiv:2606.09411v1`；正文定位：3.1 Method；4.2 Method。题摘准入依据见 V3_SCREENING_LEDGER.md；owner 以执行/状态/评测合同而非论文名称确定。
- **Evaluation：** 3.2 Evaluation。
- **Limitations：** 未定位独立 Limitations；仅以可访问题摘和披露 scope 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。
