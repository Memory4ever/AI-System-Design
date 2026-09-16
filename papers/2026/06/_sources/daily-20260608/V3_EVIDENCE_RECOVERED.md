# 2026-06-08 V3 recovered-candidate evidence

本包覆盖独立复核后存续的 15 个 closure-recovered Candidate。章节 locator 取自 official exact-v1 HTML；没有独立 limitations 标题时，以 Discussion/Conclusion 和披露 workload 为 claim 边界。

## Final owner corrections for restored candidates

- `2606.06915`：`已有覆盖`，canonical owner=`INFER-SCHEDULING`；Ch56 “Reasoning Budget 必须进入调度与评估身份”与“Model Routing 与 Test-time Scaling 必须结算同一个 Budget”。OpenAI-compatible proxy/library 只是受限实现。
- `2606.06991`：`已有覆盖`，canonical owner=`MULTIMODAL-REPRESENTATION`；Ch23 “Streaming Multimodal Identity 不止是 Token Type”与“实时多模态表示还必须拥有可中断的时间状态”。Ch42 只接手 runtime continue/cancel/commit。
- `2606.07054`：`已有覆盖`，canonical owner=`PLATFORM-EVALUATION-SYSTEM`；Ch66 “Trajectory Judge 必须区分叙述、动作与完成证据”。Ch67 只采集 observation，不拥有 verdict。

## Subtle Injection for Ground-truth Inference of LLM Training Data

- **Identity / Method：** `arXiv:2606.06502v1`；正文定位：3 Formal Framework；6.1 Simulation Design。用 canary 与 Neyman-Pearson FPR control 把训练数据 ownership 变成可取证、可验收的合同。
- **Evaluation：** 7 Results；7.4 Per-Strategy Analysis。
- **Limitations：** 8 Discussion；8.4 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，canonical owner=`PLATFORM-SECURITY`；Ch72 已覆盖 memorization/adaptive-extraction 分离、membership protocol 与 canary/FPR 审计；Ch27 仅提供 provenance/canary 数据 handoff。

## MacArena: Benchmarking Computer Use Agents on an Online macOS Environment

- **Identity / Method：** `arXiv:2606.06560v1`；正文定位：3.2 Benchmark Structure；Evaluation Framework.。原生虚拟化和跨平台任务使 GUI Agent 的环境差异可复验，并直接修正从 Linux benchmark 外推 macOS competence 的结论。
- **Evaluation：** Evaluation Framework.；4.2 Analysis。
- **Limitations：** 5 Limitations and Future Work；6 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `Only report`；保留为当前窗口上下文，不形成新的长期知识 owner。

## RECAP: Regression Evaluation for Continual Adaptation of Prompts

- **Identity / Method：** `arXiv:2606.06698v1`；正文定位：Appendix A Protocol Pseudocode；Appendix H Per-Method Behavioral Profiles。用 proactive adapt-then-test、constraint-level regression/forgetting 定义生产 constraint 更新后的 release gate。
- **Evaluation：** 4 Results；Appendix E Per-Backbone Results。
- **Limitations：** 5 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## Pomona: Continuous Code Quality Improvement via Small, Agentic Pull Requests at Bloomberg

- **Identity / Method：** `arXiv:2606.06752v1`；正文定位：1. Introduction；2. Pomona Overview。工业部署中用扫描 backlog、小 PR、review/merge 证据构成低风险连续 Agent 发布循环。
- **Evaluation：** 3. Early Insights and Evaluation；3.1.1. Results。
- **Limitations：** 4. Discussion；6. Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-WORKFLOW`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## AdMem: Advanced Memory for Task-solving Agents

- **Identity / Method：** `arXiv:2606.06787v1`；正文定位：2.2 Framework。以 actor/memory/critic 分离 semantic/episodic/procedural、短期/长期状态，并定义 merge/prune owner。
- **Evaluation：** 正文未设独立 Evaluation 标题；只使用 exact-v1 中可识别的结果/案例。
- **Limitations：** 4 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use Workflows

- **Identity / Method：** `arXiv:2606.06923v1`；正文定位：9.3 DeclarativeAgent system prompt。在统一 POMDP 中比较 declarative skill 与 imperative state machine，揭示 retrieval quality 对 orchestration 的控制边界。
- **Evaluation：** 6 Theoretical Analysis；7 Experimental Results。
- **Limitations：** 9 Discussion and Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-WORKFLOW`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## Auditing Training Data in Domain-adapted LLMs: LoRA-MINT

- **Identity / Method：** `arXiv:2606.06946v1`；正文定位：III Proposed Method: LoRA-MINT；IV Experimental Framework。用 membership inference 审计 LoRA/domain-adapted model 的训练数据暴露，进入 data provenance contract。
- **Evaluation：** V Experiments and Results。
- **Limitations：** 未设独立 Limitations；以 Conclusion 与披露 workload 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`TRAIN-DATA`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## FinEvolveBench: A Benchmark for Self-Evolving Agents on Low-Repetition Tasks with Implicit Rewards

- **Identity / Method：** `arXiv:2606.06960v1`；正文定位：4.2 Tree-of-Experience Self-Evolution Framework。将低重复任务、延迟 noisy outcome 与 experience update 对齐，给自演化 Agent 的在线反馈/评测合同及负结果。
- **Evaluation：** 正文未设独立 Evaluation 标题；只使用 exact-v1 中可识别的结果/案例。
- **Limitations：** 6 Conclusion；7 Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## MADE: Beyond Scoring via a Multilingual Agentic Diagnosing Engine for Fine-Grained Evaluation Insights

- **Identity / Method：** `arXiv:2606.07020v1`；正文定位：(Meta) MADE turns benchmark landscapes into action maps.。把 8.66M evaluation records 分解为 plan、aggregate、instance、culture 与 grounded report，形成可复用诊断流水线。
- **Evaluation：** Multilingual and multicultural evaluation.；Post-evaluation diagnosis and error analysis.。
- **Limitations：** 6 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `Only report`；保留为当前窗口上下文，不形成新的长期知识 owner。

## Beyond Rubrics: Exploration-Guided Evaluation Skills for Reward Modeling

- **Identity / Method：** `arXiv:2606.07040v1`；正文定位：2.1 Task Formulation and Online Rubric-Based Reward Modeling；2.3 A Naive Skill-Based Method。将 per-query rubric 改成可演化、可复用并直接注入 judge context 的 evaluation skill state。
- **Evaluation：** 4.1 Datasets and Experiment Settings；4.2 Main Experiment Results。
- **Limitations：** 5 Analyses and Discussion；7 Conclusion；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## SWE-Explore: Benchmarking How Coding Agents Explore Repositories

- **Identity / Method：** `arXiv:2606.07297v1`；正文定位：3 SWE-Explore Benchmark；3.1 Task Formulation。在固定 line budget 下把 repository exploration 分成 coverage、ranking、context efficiency，并与 downstream repair 对齐。
- **Evaluation：** Validation by downstream repair.；4.2 Downstream validation.。
- **Limitations：** 5 Conclusion；Discussion.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `Only report`；保留为当前窗口上下文，不形成新的长期知识 owner。

## DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning

- **Identity / Method：** `arXiv:2606.07299v1`；正文定位：2 DuMate-DeepResearch Framework。解耦 Agent Core/Tool Ecosystem、外层规划/内层搜索，并使中间决策和工具调用显式可审计。
- **Evaluation：** 3 Experiments and Evaluation；3.2 Detailed Analysis。
- **Limitations：** 未设独立 Limitations；以 Conclusion 与披露 workload 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## Certifiable Semantic Agreement Among LLM Agents: What the Admissibility Instrument Decides

- **Identity / Method：** `arXiv:2606.07316v1`；正文定位：Approach.；3. System Model and Problem Formulation。用 typed commit/verdict/abort certificate 明确多 Agent 语义共识，并给出 coverage 无优势与 tie-break 漏洞的负结果。
- **Evaluation：** Evaluation.；5. Correctness Analysis。
- **Limitations：** Scope and limitations.；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MULTI-AGENT`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions

- **Identity / Method：** `arXiv:2606.07402v1`；正文定位：2 M 3 Exam : Agent Benchmark；2.1 Task Formulation。将多模态 memory 拆成 grounding、cross-session reasoning 与 index/token cost，并按需读取 raw visual source。
- **Evaluation：** 4 Benchmarking Analysis；Evaluation Metrics.。
- **Limitations：** 7 Conclusion；Limitations；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文已覆盖对应 state/control/evaluation contract，new Integrate=0。

## Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling

- **Identity / Method：** `arXiv:2606.07404v1`；正文定位：3 The LightningLM System。120B MoE 单节点训练以 reversible activation、state-preserving growth 与 quantized-expert/adapter optimizer state 形成端到端系统合同。
- **Evaluation：** 8.4 The difficulty curriculum, and the role of held-out evaluation。
- **Limitations：** 未设独立 Limitations；以 Conclusion 与披露 workload 为界；不外推到未列出的模型、任务、硬件、并发或生产 SLO。
- **Books：** `已有覆盖`，canonical owner=`TRAIN-PRETRAINING`；Ch28 已覆盖 shape-aware parameter mapping、activation-scale preservation、optimizer-state reset、asymmetric rewarm 与 loss-shock canary/rollback；Ch36 仅接手并行布局与分布式状态迁移。
