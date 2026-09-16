# 2026-06-04 V3 recovered-candidate evidence — batch 02

本批覆盖其余 15 个新恢复 Candidate。所有技术 claim 都限制在 `arXiv:<id>v1` 的正文 locator、实验设置与作者明示边界；没有用旧 Books trace 代替正文判断。

## Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents

- **Identity / Method：** `arXiv:2606.04815v1`，§3.1 online lifelong formulation、§3.3 verifier-guided skill learning 与 §3.4 online skill internalization；把 action feedback、skill store 与 test-time policy 更新连成闭环。
- **Evaluation：** §4 setup、main results、ablations、hyperparameter 与 qualitative analysis。
- **Limitations：** §5 Conclusions and Further Work；指定 environments/verifier 的改善不证明开放世界长期安全，也未消除 skill poisoning、遗忘和回滚成本。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；skill write/read、verifier、online update 与 release/fallback 边界已有正文。

## Channel Fracture: Three Instances of Cross-Boundary Silent Delivery Reliability Failures in Multi-Agent Systems

- **Identity / Method：** `arXiv:2606.04896v1`，§3 三种 injection channels/root-cause/fracture pattern 与 §4 CADVP v1.1；关键机制是 receiver-visible confirmation，而不是 writer-side success。
- **Evaluation：** §3.2–§3.4 对 direct DB、target self-write、cron-delegated write 的可重复实验，§4.4 应用 13 维协议。
- **Limitations：** §5 Discussion；只有一个 Hermes/Holographic-memory 实现族和三种通道，不能推为所有多 Agent runtime 的发生率或完整协议。
- **Books：** `已有覆盖`，owner=`AGENT-MULTI-AGENT`；现有跨 Agent handoff、delivery acknowledgement、receiver verification 与 fallback 已覆盖。

## Audio Interaction Model

- **Identity / Method：** `arXiv:2606.05121v1`，§3 always-on perceive–decide–respond、streaming construction/training 与 asynchronous FIFO inference；把 continuous audio 的 state 与 scheduling contract 显式化。
- **Evaluation：** §5 benchmarks、main results、ablation/case study，Appendix A real-world validation 与 Appendix G error analyses。
- **Limitations：** exact-v1 未定位独立 Limitations 章节；边界由作者披露的 audio models/dataset/benchmarks 推得，FIFO 稳定性不等于任意设备、噪声、延迟和 barge-in SLO 已满足。
- **Books：** `已有覆盖`，owner=`MULTIMODAL-REPRESENTATION`（系统调度 handoff 至 inference owner）；流式 chunk/state、异步调度与端到端验收边界已有正文链。

## Streaming Communication in Multi-Agent Reasoning

- **Identity / Method：** `arXiv:2606.05158v1`，§3 step streaming algorithm、effectiveness/efficiency characterization；下游 Agent 在上游完整结束前消费经验证的 reasoning step。
- **Evaluation：** §4 setup、quantitative/case/perturbation、step-level scaling 与 cost analysis。
- **Limitations：** §6 Limitation；数学推理 benchmarks、commercial backbones 与固定 topology 不证明任意异步依赖或 tool workflow 保持正确。
- **Books：** `已有覆盖`，owner=`AGENT-MULTI-AGENT`；streaming handoff、partial-state provenance、backpressure 与 correction authority 已覆盖。

## Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models

- **Identity / Method：** `arXiv:2606.04109v1`，§3 framework/methodology；content-fixed paired variants 隔离 Reference/Evidence/Instruction/Example 标签对 context adoption 的影响。
- **Evaluation：** §4 adoption gradient、global-instruction/nested-label interaction、task-affordance 与 reader-setting probes，§5 给 benchmark methodology。
- **Limitations：** §7；模型、语言、短答案 probe 与 presentation setting 的边界不等于完整 RAG pipeline 效果。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有 prompt/template versioning、paired control 与 context-conflict evaluation 已覆盖。

## The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?

- **Identity / Method：** `arXiv:2606.04455v1`，§3 formulation、protocol、sandboxed evaluation architecture 与 integrity；将 agent-building artifact、开发预算和 unseen test 分离。
- **Evaluation：** §4 models/resources 与 §5 integrity validation、meta-agent performance。
- **Limitations：** 结果受 task suite、API/time budgets、Harbor sandbox 与 evaluator 实现限制，不能证明自主 agent development 的开放世界能力。
- **Books：** `Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；它是有用的 benchmark contract，但未改变当前通用评测 owner。

## QO-Bench: Diagnosing Query-Operator-Preserving Retrieval over Typed Event Tuples

- **Identity / Method：** `arXiv:2606.04646v1`，§3 denotational retrieval、operator preservation/execution 与 tractable subclass；把 filter/intersection/join preservation 与回答分离验收。
- **Evaluation：** §4 22,984 articles、614 events、18 templates 与 judge consensus，§5 定位 retrieval versus execution failure。
- **Limitations：** 独立 Limitations；financial-event tuple schema、derived gold 与模板集合不代表所有开放文本 query。
- **Books：** `已有覆盖`，owner=`AGENT-RAG`；retrieval recall、operator semantics、structured execution 与 answer verification 已覆盖。

## Revisiting Vul-RAG: Reproducibility and Replicability of RAG-based Vulnerability Detection with Open-Weight Models

- **Identity / Method：** `arXiv:2606.04739v1`，§3 Vul-RAG reconstruction 与 §4 dataset/models/metrics/implementation；贡献是对既有结果的复验边界。
- **Evaluation：** §5 reproduction、newer models、code specialization、reasoning 与 scale；§6 Threats to Validity。
- **Limitations：** 垂直 vulnerability dataset/model slice 不能外推为一般 RAG，且复现失败只约束原 claim 所列设置。
- **Books：** `Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；用于提醒复现与开放权重基线，不形成独立长期机制增量。

## AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?

- **Identity / Method：** `arXiv:2606.05080v1`，§2 task formulation/construction/composition 与 Appendix A scoring anchors/gates；以可执行 artifact 和长时迭代状态验收，而非单轮答案。
- **Evaluation：** §3 benchmark results 与 §4 cost、failure、harness ablation。
- **Limitations：** 独立 Limitations and Broader Impact；32 个系统/CUDA/model tasks 与 harness 资源限制不代表真实科研自主性或安全部署。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；现有长程 task、artifact gate、cost/failure taxonomy 与 harness ablation 已覆盖。

## Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)

- **Identity / Method：** `arXiv:2606.05145v1`，§2 operator-class setup/features/recoverability regimes，§3 routing test-time compute，§4 prospective routing policy；用可操作性而非语言解释分配重试。
- **Evaluation：** §4 prospective validation、§5 regime features、§6 post-training audit channel；Appendix A 给 junction/trajectory metrics。
- **Limitations：** §9；problem-unit、operator class、temperature 与 backbone 的边界不证明任意 reasoning failure 可被观测或修复。
- **Books：** `已有覆盖`，owner=`INFER-SCHEDULING`（相邻 Evaluation）；failure-aware compute routing、budget 与 fallback 已覆盖。

## Beyond Single-Policy: Evaluating Composed Organization-Specific Policy Alignment in LLM Chatbots

- **Identity / Method：** `arXiv:2606.04394v1`，§3 grounding、composition、query generation 与 policy-handling evaluation；将多条组织 policy 的冲突/组合变成测试对象。
- **Evaluation：** §4 testbed/target models/construction comparisons 与 §5 composed-vs-single、pattern/facet error、validity。
- **Limitations：** 独立 Limitations；30 worlds、synthetic compositions 与 judge 不能代表全部真实制度冲突或法律正确性。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`（相邻 Security）；policy composition、冲突矩阵与多层验收已有机制。

## MemoryDocDataSet: A Benchmark for Joint Conversational Memory and Long Document Reasoning

- **Identity / Method：** `arXiv:2606.04442v1`，§3 micro-world/source-dimension benchmark 与 §4 six-stage collection/verification pipeline；显式区分 conversation-only、document-only 与 hybrid evidence。
- **Evaluation：** §5 six retrieval/memory baselines、metrics/results 与 §6 joint-retrieval gap analysis。
- **Limitations：** synthetic micro-worlds、50 worlds/1000 QA 和自动生成 pipeline 不能证明真实长期会话的隐私、更新与噪声边界。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`（相邻 `AGENT-MEMORY`）；source-dimension、hybrid evidence 与检索分层验收已有正文。

## Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms

- **Identity / Method：** `arXiv:2606.04701v1`，§3 continuous evolving state、agent-initiated observation、task construction 与 accuracy/efficiency metrics。
- **Evaluation：** §4 model/agent setup、main results/design ablation 与 §5 over/under-observation、awareness-vs-capability diagnostics。
- **Limitations：** 独立 Limitations；short-video platform replica、语言/文化与 annotation scale 使结果不能外推至全部 GUI environments。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；Ch66“Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy”与 Living-world Evaluation/Run Identity 已覆盖动态观察预算、环境推进与运行身份。

## Auditing CoT Answer-Hijack Patches: Source-Control Certificates with Type-I Guarantees

- **Identity / Method：** `arXiv:2606.04717v1`，§3 K-shot layer disruption、recovery/spread metrics、pre-specified diagnostics；通过 paired source controls 区分 patch 来源与答案恢复。
- **Evaluation：** §4–§9 覆盖 GSM8K/MATH slice、cross-architecture spread、source controls、band metrics 与 reproducibility protocol。
- **Limitations：** §10 明示两个 model families、主要 benchmark 与 white-box operator；不构成生产 patch defense 或通用因果证明。
- **Books：** `Only report`，route=`PLATFORM-EVALUATION-SYSTEM`；作为 activation-patching 审计案例，不新增通用系统机制。

## Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents

- **Identity / Method：** `arXiv:2606.04874v1`，§3 task/data/metrics，把 decomposition、tool selection、constraints、broken tools 与 unsolvable tasks 分轴验收。
- **Evaluation：** §4 overall/extraneous/broken/unsolvable，§5 executable validation、horizon profiles、refinement 与 efficiency。
- **Limitations：** 独立 Limitations；合成 robustness scenarios、tool catalog 与 judge 不能证明真实 workflow 的全部 side effects。
- **Books：** `已有覆盖`，owner=`PLATFORM-EVALUATION-SYSTEM`；规划分轴、失败注入、不可解判定与 executable validation 已覆盖。
