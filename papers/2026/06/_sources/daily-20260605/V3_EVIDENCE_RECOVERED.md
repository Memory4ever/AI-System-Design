# 2026-06-05 V3 recovered-candidate evidence

本包覆盖独立复核后存续的 23 个 closure-recovered Candidate。每项使用 official exact-v1 HTML 的真实章节标题；未发现独立 limitations 标题时明确以 Discussion/Conclusion 为边界，不推断作者未披露的设置。

## The Evaluation Blind Spot: A Stereological Theory of Benchmark Coverage for Large Language Models

- **Identity / Method：** `arXiv:2606.05169v1`；正文定位：The curse of benchmark dimensionality.；Corollary: benchmark domination ⇏ \not\Rightarrow capability domination.。用有效维度、不可见 capability profile 与稳定 benchmark core 修正“排行榜分数等于覆盖”的评测结论。
- **Evaluation：** Counterfactual validation.；Evaluation monoculture.。
- **Limitations：** 8 Discussion；Takeaways and limitations.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；正文锚点“从‘已见切片均值’到 Blind-spot Mass”与“平均值、切片与不确定性”已经承载未见 capability/state mass、slice coverage 与 release authority。该论文只增加 stereological 解释框架，不改变现有长期合同。

## ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open-Weight Large Language Models

- **Identity / Method：** `arXiv:2606.05170v1`；正文定位：2 Method；Query benchmark.。证明 accuracy 与 error-severity distribution 不可约，要求发布时同时报告尾部严重度。
- **Evaluation：** Human validation.；Severity-aware evaluation.。
- **Limitations：** 7 Discussion；8 Limitations and misuse；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## AppAgent-Claw: CLI Is All You Need for GUI Automation

- **Identity / Method：** `arXiv:2606.05171v1`；正文定位：3 Method；3.1 System Overview。把 GUI workflow 固化为 record-once/replay-many skill，并用分层定位与 validation-coupled execution 取代运行时推理。
- **Evaluation：** 3.8 Execution, Validation, and Observability。
- **Limitations：** 5 Discussion；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-TOOL-CALLING`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## LANTERN: Layered Archival and Temporal Episodic Retrieval Network for Long-Context LLM Conversations

- **Identity / Method：** `arXiv:2606.05182v1`；正文定位：3 Method。在 compaction 前归档每轮，并以零 LLM-call hybrid retrieval 恢复状态；明确延迟与跨模型边界。
- **Evaluation：** 4.4 Evaluation Metrics；Human validation of LLM judge.。
- **Limitations：** 7 Discussion；8 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## State commitment learning: training language models to distinguish computation from memory

- **Identity / Method：** `arXiv:2606.05201v1`；正文定位：1.3 Method overview；3 Method。显式区分临时 computation 与 persistent committed state，以 counterfactual erasure 定义可训练、可验收的状态合同。
- **Evaluation：** 4.3 Experiment 1: main results；4.4 Experiment 2: training-objective ablation。
- **Limitations：** 6 Discussion；8 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming

- **Identity / Method：** `arXiv:2606.05233v1`；正文定位：2 The CUA-HandCrafted Benchmark；Appendix A Benchmark Detail: Sites, Channels, Canary, Release。跨 browser/coding surface 复现 prompt injection，直接推翻把旧 ASR 外推到 frontier CUA 的安全结论。
- **Evaluation：** 3 Results；Results.。
- **Limitations：** 6 Discussion: RL Optimization Is the Gap；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## DeployBench: Benchmarking LLM Agents for Research Artifact Deployment

- **Identity / Method：** `arXiv:2606.05238v1`；正文定位：3.1 Task Formulation；3.2 Benchmark Construction。用从 fresh machine 到隐藏实验验证的完整 pipeline 定义 research artifact deployment release gate，并定位 self-stop 错误。
- **Evaluation：** 3.3 Evaluation；4 Experiment。
- **Limitations：** 6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## SentinelBench: A Benchmark for Long-Running Monitoring Agents

- **Identity / Method：** `arXiv:2606.05342v1`；正文定位：2.3 Benchmark Tasks；3 Evaluation Protocol and Metrics。把长期 Agent 的持续轮询改写为 event monitoring；同时量化 completion、reaction time 与 resource use。
- **Evaluation：** 2.3.3 Task Validation；3 Evaluation Protocol and Metrics。
- **Limitations：** 5 Discussion and Limitations；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Ahoy: LLMs Enacting Multiagent Interaction Protocols

- **Identity / Method：** `arXiv:2606.05390v1`；正文定位：2.2 Implementing Protocol-Based Agents；3 Architecture。让 Agent 动态选择并并发 enact declarative interaction protocol，改变多 Agent 控制协议 ownership。
- **Evaluation：** 5 Evaluation。
- **Limitations：** 未设独立 Limitations 标题；以 exact-v1 的 Conclusion 和实验设置为 claim 边界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MULTI-AGENT`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Agents' Last Exam

- **Identity / Method：** `arXiv:2606.05405v1`；正文定位：2 Benchmark Design and Dataset Construction；2.1 Benchmark Design Principles: What Tasks are We Looking for?。用可验证、长期、经济真实 workflow 与 living task pool 替代静态短 benchmark 的发布评测合同。
- **Evaluation：** 3 Evaluation Pipeline；3.3 Evaluation Modes。
- **Limitations：** 6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## The Granularity Gap: A Multi-Dimensional Cross-Generational Audit of Sycophancy in Gemini Models

- **Identity / Method：** `arXiv:2606.05183v1`；正文定位：2.1. Framework Implementation；2.3. Experimental Design。证明 refuse/comply 不能代理 sycophancy severity，给 safety evaluation 的粒度与 judge 边界。
- **Evaluation：** 2.5. Evaluation Instruments；2.6. Human-Centered Validation。
- **Limitations：** 8. Discussion；9. Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `Only report`；该项保留为当前窗口的评测/方法论上下文，不形成新的长期知识 owner。

## Learned Subspace Compression for Communication-Efficient Pipeline Parallelism

- **Identity / Method：** `arXiv:2606.05484v1`；正文定位：1 Introduction；2 Related works。对 pipeline stage activation 建立可学习正交压缩、token anchor 与 streaming codebook sync 的通信合同。
- **Evaluation：** 3.4 Empirical Validation；4.2 Main Results。
- **Limitations：** 5 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`TRAIN-DISTRIBUTED-TRAINING`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints

- **Identity / Method：** `arXiv:2606.05622v1`；正文定位：E.1 Benchmark Traits Elaboration。用逐步揭示 world/user constraint 的多轮 protocol 测试状态累积与 replanning，而不是完整 prompt 的一次性规划。
- **Evaluation：** 3 Experiment；3.1 Experiment Setup。
- **Limitations：** 5 Conclusion；6 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows

- **Identity / Method：** `arXiv:2606.05670v1`；正文定位：2.1 Agent Workflow Design；3 Evaluation Protocol。将 single/fixed/evolving MAS 置于统一 loader、tool、answer、usage 与 trajectory logging substrate，修正“更多 Agent 更好”的比较。
- **Evaluation：** 2.2 Agent Evaluation Frameworks；3 Evaluation Protocol。
- **Limitations：** 5 Discussion；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## AdaMEM: Test-Time Adaptive Memory for Language Agents

- **Identity / Method：** `arXiv:2606.05684v1`；正文定位：1 Introduction；2 Related Work。分离 offline long-term trajectory 与在线 short-term strategy memory，明确 post-deployment adaptation 的状态更新边界。
- **Evaluation：** 4.2 Main Results；Appendix D Efficiency Analysis。
- **Limitations：** 5 Conclusion；Appendix E Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents

- **Identity / Method：** `arXiv:2606.05761v1`；正文定位：1 Introduction；2 Methodology。将长期 memory 分成 preservation、retrieval、downstream reasoning，并显式测试 complementary/nuanced/contradictory 关系。
- **Evaluation：** 2.2 Evaluation Overview and Taxonomy；3.3 Main Results。
- **Limitations：** 4 Discussion；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents

- **Identity / Method：** `arXiv:2606.05806v1`；正文定位：3 The ToolMaze Framework；3.5 Evaluation Framework and Metrics。用 DAG topology 与显式/隐式、瞬时/永久 tool failure 定义 fault-recovery contract 和 PRR。
- **Evaluation：** 2.2 Robustness and Risk Evaluation；3.2 The 𝒞 × 𝒫 \mathcal{C}\times\mathcal{P} Evaluation Matrix。
- **Limitations：** 5 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-TOOL-CALLING`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement

- **Identity / Method：** `arXiv:2606.05920v1`；正文定位：3.1 Evaluation Framework；DAG-Based Evaluation Protocol。把 underspecified intent、deployed browser test 与用户反馈纳入多轮代码 Agent 验收，而不是一次性完整规格。
- **Evaluation：** 3.1 Evaluation Framework；Automated Evaluation。
- **Limitations：** 6 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference

- **Identity / Method：** `arXiv:2606.05922v1`；正文定位：G.2 Per-Method Decomposition。以历史轨迹、coreset、self-validation 与 pairwise preference 更新 harness，明确无外部标签下的控制状态演化。
- **Evaluation：** 5 Experiments and Results；5.3 Comparison with Validation-Feedback Optimization。
- **Limitations：** 6 Discussion；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Epistemic Injustice in Language Models: An Audit of Pretraining Filters and Guardrails

- **Identity / Method：** `arXiv:2606.05936v1`；正文定位：1 Introduction；F1. Disagreement of filters and guardrails.。联合审计 pretraining filter 与 inference guardrail，证明词表控制点产生双阶段 epistemic erasure，修正数据/发布边界。
- **Evaluation：** 3.6 Evaluation Setting；Appendix A Detailed results on study of epistemic erasure of marginalised identities。
- **Limitations：** Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context in LLMs

- **Identity / Method：** `arXiv:2606.06203v1`；正文定位：Appendix A Benchmark details: evaluation prompts and dataset construction；MK-NIAH System Prompt.。在固定长度与位置下证明 lexical density 缩小 effective context，修正只按 token length/position 判断长上下文容量的结论。
- **Evaluation：** 4 Results；4.1 Experiment Settings。
- **Limitations：** 5 Discussion and Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已整合`，canonical owner=`MODEL-LONG-CONTEXT`；Ch22 “相同 Token Length 仍可能承载不同 Information Load”已在 Review notes 前绑定 token length、position、task 与 lexical density，区分资源容量与 effective-context quality，并写明度量混杂、切片成本、人工内容结构 fallback 与 exact-v1 外推边界。

## LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs

- **Identity / Method：** `arXiv:2606.06286v1`；正文定位：3 Proposed Method: Propensity-Aware Memorization Evaluation。分离 worst-case extractability 与 ordinary-use propensity，并给 deterministic corpus tracing，修正 memorization 安全评测合同。
- **Evaluation：** 3 Proposed Method: Propensity-Aware Memorization Evaluation；3.1 Propensity-Capability Evaluation Settings。
- **Limitations：** 6 Discussion；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；当前正文已覆盖相应 state/control/evaluation contract，new Integrate=0。

## CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence of LLM Agents through Controlled Multi-Agent Experiments

- **Identity / Method：** `arXiv:2606.06399v1`；正文定位：3.1 System Architecture；4 Benchmark Experiments。以可控 interaction condition 和 action-level internal-state probe 将多 Agent collaborative competence 与任务总分分开。
- **Evaluation：** 4.1 Experiment Setup；4.2 Evaluation。
- **Limitations：** 6 Conclusion；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `Only report`；该项保留为当前窗口的评测/方法论上下文，不形成新的长期知识 owner。
