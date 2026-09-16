# 2026-06-04 V3 recovered-candidate evidence — batch 01

本批覆盖独立复核后存续的前 16 个新恢复 Candidate。身份统一为 `arXiv:<id>v1`；Method、Evaluation 与 Limitations locator 均来自 exact-v1 正文。除明确列出的公开仓库外，artifact 一律记为 `Not Disclosed`，不把后来版本或未绑定 commit 的链接当作事件时证据。Books 判断以当前正文机制为准，旧 trace 不参与授权。

## Novel Aspects of IEEE SA P3109 Arithmetic Formats for Machine Learning

- **Identity / Method：** `arXiv:2606.04028v1`，§III Datum Sets、§IV Operations、§V Formal Verification 与 §VIII Block Operations；贡献是数值格式语义、运算与验证边界，不是某个模型的新结构。
- **Evaluation：** §V 的形式验证与 §VI Approximate Implementations；证据只覆盖草案格式及所述实现近似。
- **Limitations：** §X Discussion and Limitations；标准仍为 draft，不能外推为所有 accelerator 已实现或取得端到端收益。
- **Books：** `Only report`；可路由至训练数值稳定性相邻 owner，但尚不足以改变书稿的通用精度机制链。

## Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification

- **Identity / Method：** `arXiv:2606.04037v1`，§2.2 Agent Operational Envelope、§2.3 Ontology-to-Scenario Generation、§2.4 Trust Certificate 与 §2.5 Implementation Architecture；把 ontology 约束、scenario coverage、certificate 与 deployment gate 连成发布合同。
- **Evaluation：** §3 Proposed Evaluation Framework，含 bounded model checking、runtime verification、empirical assurance 与 anti-circularity controls。
- **Limitations：** 这是 proposed framework；经验有效性依赖 ontology 完整度、judge 校准与 ground-truth controls，不能视作生产认证标准。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有评测/发布门已覆盖预声明边界、独立 ground truth 与阻断式 gate。

## Need to Know: Contextual-Integrity-Grounded Query Rewriting for Privacy-Conscious LLM Delegation

- **Identity / Method：** `arXiv:2606.04067v1`，§3 DelegateCI-Bench 与 §4 Method（framework、reward、policy training）；将 disclosure decision 放在 delegation 前的 query-rewrite boundary。
- **Evaluation：** §5 Experiments，1600 个 held-out samples、privacy/utility metrics、judge assessment 与 ablation。
- **Limitations：** 独立 Limitations；medical/general-domain slice、judge 与本地 reformulator 的边界不能外推为任意隐私域或密码学保密。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；最小披露、数据边界与外部模型调用前的 policy enforcement 已有机制 owner。

## Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents

- **Identity / Method：** `arXiv:2606.04141v1`，§3 Threat Model、§4.1 System Overview、§4.2 CIFT、§4.3 DP-HONEY 与 §4.4 NIMBUS；把 pre-output activation signal、honeytoken 与跨轮泄漏预算组合成 control plane。
- **Evaluation：** §5.1–§5.5，覆盖白盒模型、50-conversation synthetic suite、组件指标与 integrated prototype。
- **Limitations：** §6 明示小型 in-house benchmark、white-box requirement 与 preliminary prototype；不证明 API-only 黑盒或生产 FPR/SLO。
- **Books：** `已有覆盖`，owner=`PLATFORM-SECURITY`；credential least privilege、跨轮状态、独立 detector 与阻断边界已有正文机制。

## Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval

- **Identity / Method：** `arXiv:2606.04391v1`，§3 formalization 与 §4 skill extraction、state-grounded retrieval、injection/execution；skill state 由页面状态而非只由任务文本选择。
- **Evaluation：** §5 WebArena setup、main results、efficiency、online performance 与 ablation。
- **Limitations：** 独立 Limitations；只验证 WebArena/指定模型，retrieval state 与 skill quality 不代表跨 GUI/workload 泛化。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；现有 memory/skill owner 已覆盖写入、检索、版本与执行反馈循环。

## Context-as-AI-Service: Surfacing Cross-File Dependency Chains for LLM-Generated Developer Documentation

- **Identity / Method：** `arXiv:2606.04397v1`，§3 Source Ingestion、Storage and Indexing、Retrieval Interface、Review Layer；把跨文件依赖作为可追溯 context service 返回。
- **Evaluation：** §4 Case-Study Protocol、§5 两个 production codebase case studies 与 §6 evidence trail/dependency taxonomy。
- **Limitations：** 独立 Limitations；两个匿名案例与文档任务不足以证明通用代码理解或自动合并安全。
- **Books：** `已有覆盖`，owner=`AGENT-RAG`；索引 owner、dependency-aware retrieval、citation/evidence trail 与人工 review handoff 已覆盖。

## Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers

- **Identity / Method：** `arXiv:2606.04421v1`，§3 Three-Regret Functional、drift-robust replan/dispatch coupling 与 Trivium algorithm；持久 causal log 显式记录 why/when，并影响后续 dispatch。
- **Evaluation：** §4 Experiments，含预注册 controlled validation 与 pilot real-LLM stream。
- **Limitations：** §5 Conclusion, Impact, and Limitations；受合成 SCM、probe assumptions 与 pilot deployment scope 限制。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；现有 episodic/semantic memory、provenance、失效与再规划链已覆盖该长期机制。

## Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation

- **Identity / Method：** `arXiv:2606.04435v1`，§III problem formalization、§IV CHARM 与 §V mitigation architectures；在每个 stage 维护跨阶段置信与 verifier，而非只验最终答案。
- **Evaluation：** §VI Evaluation，clean/injected trajectories、跨数据集 cascade detection 与 re-execution 开销。
- **Limitations：** §VII Discussion；作者验证的是指定注入轨迹与 datasets，不能证明 Bayesian calibration、judge 或所有 retrieval failure 在生产中稳定。
- **Books：** `已有覆盖`，owner=`AGENT-RAG`（相邻 `PLATFORM-EVALUATION-SYSTEM`）；分阶段 citation/verification、fallback 与 end-to-end evaluation 已覆盖。

## AgentJet: A Distributed Swarm Training Framework for Agentic Reinforcement Learning

- **Identity / Method：** `arXiv:2606.04484v1`，§3 Swarm Architecture、Swarm RL、episode batching 与 context tracking；client/server 解耦让异构 agent、environment 与 learner 各自拥有生命周期和故障边界。
- **Evaluation：** §5 覆盖 shared/non-shared parameter、多 Agent、多任务与常规 multi-turn training，§6 展示 automated research pipeline。
- **Limitations：** exact-v1 未定位独立 Limitations 章节；边界由作者披露的 Werewolves/translation/AppWorld 等 workloads 推得，未建立任意环境、网络分区或生产多租户公平性结论。
- **Books：** `已有覆盖`，owner=`TRAIN-DISTRIBUTED-TRAINING`；现有 actor/rollout/learner 解耦、trajectory ownership 与 backpressure/failure recovery 已覆盖。

## Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents

- **Identity / Method：** `arXiv:2606.04555v1`，§4.1 Conversation Segment Tree、§4.2 online construction 与 §4.3 structure-aware retrieval；显式保留 temporal order 与 hierarchical segment owner。
- **Evaluation：** §5 LoCoMo、LongMemEval-MAB、RealMem，含 ablation 与 efficiency。
- **Limitations：** §6 Limitation and future work；指定 benchmark/backbone 与 online implementation 不能证明所有长期历史或事实更新模式。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；时间索引、层级摘要、检索传播与陈旧/冲突处理已有正文。

## Selectivity Estimation for Semantic Filters on Image Data

- **Identity / Method：** `arXiv:2606.04610v1`，§2 offline embeddings/online estimation、§3 specificity model、compressed KV-cache batching 与 ensemble；把 semantic filter selectivity 变成 query optimizer 的 cost signal。
- **Evaluation：** §4 experiments、Q-error 与 end-to-end runtime，覆盖不同 filter counts 与 semantic-query chains。
- **Limitations：** §3.1 Limitations 与 §6；依赖 embedding/LLM specificity proxy，数据分布漂移和 estimator error 会破坏计划质量。
- **Books：** `已有覆盖`，owner=`AGENT-RAG`；现有检索/query-plan owner 已覆盖质量估计、缓存成本与执行期 fallback。

## Bridge the Last-Mile Gap to Semantic Analytics: Compiling Natural-Language Queries into Semantic Operator Pipelines

- **Identity / Method：** `arXiv:2606.04641v1`，§3 query-data linker、semantic planner、backend code generation 与 cost summary；分离 data-aware semantics 与 backend-specific execution。
- **Evaluation：** §4 在 Palimpzest、LOTUS、Nirvana 及五个 datasets 上比较 quality、runtime 与 phase ablations。
- **Limitations：** §5 Conclusion；对 reference docs、backend API 稳定性和五个 datasets 的依赖不证明开放世界自然语言可无歧义编译。
- **Books：** `已有覆盖`，owner=`AGENT-RAG`；query planning、operator contract、backend adapter 与可验证执行结果已有机制链。

## CYGNET: Cypher Gate for Neural Execution Triage and Cost Containment

- **Identity / Method：** `arXiv:2606.04645v1`，§2 architecture/schema sources、validator backends、mirror graph、equivalence verification、cost gate 与 corrector；在数据库执行前隔离结构错误和高成本计划。
- **Evaluation：** §3 validator quality、EXPLAIN calibration、latency、multi-error、corrector 与 CypherBench end-to-end。
- **Limitations：** §5 Conclusions；mirror graph/schema coverage、Neo4j planner 与 CypherBench 的结论不外推到任意 tool/database。
- **Books：** `已有覆盖`，owner=`AGENT-TOOL-CALLING`；现有 schema validation、dry-run/sandbox、cost budget 与执行前 authorization 已覆盖。

## Rethinking Continual Experience Internalization for Self-Evolving LLM Agents

- **Identity / Method：** `arXiv:2606.04703v1`，§3 formulation 与 §5 granularity、injection pattern、internalization regime、multi-iteration stability；区分 contextual experience 与 parametric capability 的 owner。
- **Evaluation：** §4 setup 与 §5 多轮/消融，报告 trajectory efficiency、rollout cost 与稳定性。
- **Limitations：** 独立 Limitations；指定任务、训练配方与多轮规模不能证明不会遗忘、污染或跨域退化。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；现有“外部记忆优先、参数化吸收需 release/eval gate”已覆盖。

## PersonaTree: Structured Lifecycle Memory for Person Understanding in LLM Agents

- **Identity / Method：** `arXiv:2606.04780v1`，§3 lifecycle state、online evidence insertion、confidence update、offline consolidation 与 path retrieval；把 persona 更新与证据路径显式化。
- **Evaluation：** §4 六个 datasets 的 main/efficiency results 与 §5 hierarchy/path-retrieval ablations。
- **Limitations：** exact-v1 未定位独立 Limitations 章节；边界由 benchmark 与 synthetic/curated persona evidence 推得，不能证明真实用户 consent、删除权、身份合并或长期漂移已解决。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；现有 provenance、confidence、consolidation、冲突与生命周期 policy 已覆盖。

## AIP: A Graph Representation for Learning and Governing Agent Skills

- **Identity / Method：** `arXiv:2606.04781v1`，§3 Agent Instruction Protocol；把 free-form skill 拆成 graph nodes/edges、preconditions 与 execution/governance metadata。
- **Evaluation：** §4 SkillsBench 94 tasks/8 domains，比较 pass rate、wall-clock 与任务级失败。
- **Limitations：** §4.5 Limitations；单一 benchmark、agent harness 与 graph authoring cost 不能证明所有 skill 可结构化或自动治理。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；capability registry、typed precondition、version/release 与 policy ownership 已覆盖。
