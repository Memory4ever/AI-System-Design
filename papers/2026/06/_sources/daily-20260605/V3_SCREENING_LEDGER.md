# 2026-06-05 V3 strict screening ledger

> **Authority override（2026-09-11）：** 本文件下方 `76 / 630` 是作者侧 checkpoint。非作者 fresh audit 又关闭 2606.05402、2606.05711、2606.05868、2606.05946、2606.06036、2606.06079、2606.06087、2606.06438，并从 Close 恢复 2606.05558、2606.05559、2606.05828；最终 authority 为 **706 = 71 Candidate + 635 Close**。完整理由见 [`../JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md`](../JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md)。旧 8 个 `Integrate` 全部重判 `已有覆盖`；恢复候选的反例审计另把 2606.05169 从 Only report 改为 Existing Coverage，并识别 2606.06203 为真实正文增量。该增量已写入 Ch22 并通过 post-write audit；最终为 Existing 66 / Only report 4 / Integrate 1，正文缺口 0。legacy trace 与 post-Review note 不授权当前候选或 Books body。

## Authority and baseline

本记录只冻结当前 V3 题摘分母，不继承 V2.1 的 `Complete`、Candidate disposition 或 Books 决定。可读 canonical packet 包含 706 个去重 identity：68 项 old prior 与 638 项 closure proposal。逐项 title 与完整 abstract 位于 `canonical-raw-identity-inventory-v2.1.json.gz`；旧逐项 closure proposal 位于 `canonical-semantic-screening-checkpoint-v2.1.json.gz`。

严格准入要求摘要能指出可迁移的长期 design delta：明确改变 state/data/control ownership、execution/evaluation/release contract、系统级机制取舍，或修正 Books 既有结论。对象是 LLM/VLM/VLA/Agent、可映射章节、局部 benchmark、单一任务性能或新架构/adapter 名称均不够。

## Prior frontier reaudit — 52 retain / 16 close

旧 68 项逐题复审；边界项使用归档 exact-v1 的 Method/Evaluation/Limitations 复核摘要命题。以下 52 项满足严格门槛，但不继承旧 Books disposition：

| 机制族 | IDs | 严格准入依据 |
| --- | --- | --- |
| 评测、可信与安全合同 | 2606.05241、2606.05308、2606.05339、2606.05384、2606.05395、2606.05403、2606.05414、2606.05433、2606.05548、2606.05725、2606.05743、2606.05787、2606.05805、2606.05946、2606.05958、2606.05976、2606.06055、2606.06223、2606.06324、2606.06387、2606.06460 | search contamination、prediction-powered ranking、MCP fault、judge interaction、verifiable skills、source-evaluation blind spot、early failure alert、ZK training proof、ADK execution、API extraction、safety memory、RAG copyright、remediation、ML supply-chain、steering attack、self-correction、sensitive memory、risk-state monitoring、harness repair、tool poisoning 与 in-band governance 都给出可执行的评测/发布或安全控制点。 |
| 训练、推理与数据平面 | 2606.05271、2606.05495、2606.05568、2606.05597、2606.05742、2606.05868、2606.05875、2606.05933、2606.05951、2606.06178、2606.06256、2606.06302、2606.06438、2606.06453、2606.06467 | operator mapping、CUDA Graph event scheduling、ANN/PQ、异步 Agent RL、speculative reuse、GQA-to-MLA、RAG cache fusion、SLO scheduler、NVSHMEM、cost-performance routing、head-aware KV reuse、non-uniform KV compression、carbon lifecycle、programmable sparse attention 与 shared routing 明确改变系统资源/通信/执行合同。 |
| Agent communication、memory 与 control state | 2606.05304、2606.05415、2606.05679、2606.05711、2606.05872、2606.05894、2606.06036、2606.06044、2606.06054、2606.06079、2606.06087、2606.06090、2606.06240、2606.06284、2606.06337、2606.06448 | action-state message、executable schema、data-flow policy、latent communication、行为 observability、budgeted evidence、graph/temporal/trust memory、skill state、memory-as-execution-state、bitemporal contradiction、tool filtering、session graph 与 stateful workload 明确分配持久状态、控制或恢复责任。 |

以下 16 项严格关闭：2606.05378、2606.05391、2606.05396、2606.05523、2606.05551、2606.05558、2606.05559、2606.05606、2606.05610、2606.05646、2606.05662、2606.05688、2606.05800、2606.05828、2606.06032、2606.06063。它们分别停留在局部 circuit/refusal/安全 RL、通用 conformal/continual service、单一 OPE world model、rollout/hyperparameter/quant 方法、垂直 SWE/analytics、GRPO/skill-selection、描述性 forgetting 框架或 CUDA porting 任务；摘要没有形成跨 workload 的系统 owner、执行/评测或发布合同。

## Closure proposal reaudit — 24 recover / 614 close

638 项 closure proposal 逐项先看 title，边界不清时读取 canonical inventory 的完整 abstract。只恢复以下 24 项：

| ID | 严格恢复理由 |
| --- | --- |
| 2606.05169 | 用有效维度、不可见 capability profile 与稳定 benchmark core 修正“排行榜分数等于覆盖”的评测结论。 |
| 2606.05170 | 证明 accuracy 与 error-severity distribution 不可约，要求发布时同时报告尾部严重度。 |
| 2606.05171 | 把 GUI workflow 固化为 record-once/replay-many skill，并用分层定位与 validation-coupled execution 取代运行时推理。 |
| 2606.05182 | 在 compaction 前归档每轮，并以零 LLM-call hybrid retrieval 恢复状态；明确延迟与跨模型边界。 |
| 2606.05201 | 显式区分临时 computation 与 persistent committed state，以 counterfactual erasure 定义可训练、可验收的状态合同。 |
| 2606.05233 | 跨 browser/coding surface 复现 prompt injection，直接推翻把旧 ASR 外推到 frontier CUA 的安全结论。 |
| 2606.05238 | 用从 fresh machine 到隐藏实验验证的完整 pipeline 定义 research artifact deployment release gate，并定位 self-stop 错误。 |
| 2606.05342 | 把长期 Agent 的持续轮询改写为 event monitoring；同时量化 completion、reaction time 与 resource use。 |
| 2606.05390 | 让 Agent 动态选择并并发 enact declarative interaction protocol，改变多 Agent 控制协议 ownership。 |
| 2606.05402 | 用细粒度 DAG 把非线性 reasoning trace 变成可观测数据模型，并区分 discourse 与 causal dependency。 |
| 2606.05405 | 用可验证、长期、经济真实 workflow 与 living task pool 替代静态短 benchmark 的发布评测合同。 |
| 2606.05183 | 证明 refuse/comply 不能代理 sycophancy severity，给 safety evaluation 的粒度与 judge 边界。 |
| 2606.05484 | 对 pipeline stage activation 建立可学习正交压缩、token anchor 与 streaming codebook sync 的通信合同。 |
| 2606.05622 | 用逐步揭示 world/user constraint 的多轮 protocol 测试状态累积与 replanning，而不是完整 prompt 的一次性规划。 |
| 2606.05670 | 将 single/fixed/evolving MAS 置于统一 loader、tool、answer、usage 与 trajectory logging substrate，修正“更多 Agent 更好”的比较。 |
| 2606.05684 | 分离 offline long-term trajectory 与在线 short-term strategy memory，明确 post-deployment adaptation 的状态更新边界。 |
| 2606.05761 | 将长期 memory 分成 preservation、retrieval、downstream reasoning，并显式测试 complementary/nuanced/contradictory 关系。 |
| 2606.05806 | 用 DAG topology 与显式/隐式、瞬时/永久 tool failure 定义 fault-recovery contract 和 PRR。 |
| 2606.05920 | 把 underspecified intent、deployed browser test 与用户反馈纳入多轮代码 Agent 验收，而不是一次性完整规格。 |
| 2606.05922 | 以历史轨迹、coreset、self-validation 与 pairwise preference 更新 harness，明确无外部标签下的控制状态演化。 |
| 2606.05936 | 联合审计 pretraining filter 与 inference guardrail，证明词表控制点产生双阶段 epistemic erasure，修正数据/发布边界。 |
| 2606.06203 | 在固定长度与位置下证明 lexical density 缩小 effective context，修正只按 token length/position 判断长上下文容量的结论。 |
| 2606.06286 | 分离 worst-case extractability 与 ordinary-use propensity，并给 deterministic corpus tracing，修正 memorization 安全评测合同。 |
| 2606.06399 | 以可控 interaction condition 和 action-level internal-state probe 将多 Agent collaborative competence 与任务总分分开。 |

其余 614 项维持 pre-denominator Close。canonical checkpoint 已为每项保存题目、摘要证据与 family-local reason；本轮没有把其通用模板当结论，而是逐项确认后归入以下实际缺口：

- 非大模型系统对象、AI-for-Science、传统 ML/HPC 或垂直业务应用，没有当前知识树 owner；
- 仅新增模型 block、adapter、量化、prompt、reward、单一 decoding/generation/robot/VLA 方法，未改变跨 workload contract；
- 仅新增局部 benchmark 或数据集，没有新的 execution/evaluation/release contract，也未修正 Books 结论；
- 仅描述风险、能力或 taxonomy，没有落到持久状态、控制点、系统接口或可复验验收协议。

## Fresh-context FP/FN sample

遮蔽旧标签后抽查 10 retain：2606.05171、2606.05201、2606.05238、2606.05304、2606.05484、2606.05670、2606.05806、2606.05933、2606.06240、2606.06453。完整摘要均能定位到 state/control、通信、调度、评测或发布合同。

另抽查 10 close：2606.05186、2606.05253、2606.05429、2606.05538、2606.05624、2606.05703、2606.05817、2606.06060、2606.06309、2606.06492。它们分别只给 micro-pretraining 试验、RTL/量化、K/V injection、图像/video decoding、局部 consistency/cache/LoRA 方法，未出现跨 workload 系统契约。本轮样本未发现新的 FP/FN；该自检不替代主任务的非作者复核。

## Author-side frozen checkpoint（已被独立复核覆盖）

- raw identities：706
- Candidate：76 = prior 52 + closure 恢复 24
- Close：630 = prior 严格关闭 16 + closure 维持 614
- 旧 638 closure proposals 的 false-negative：24/638（3.8%）
- 旧 68 prior 的 false-positive：16/68（23.5%）

这组 `76 / 630` 只保留为作者侧 checkpoint。最终独立 authority 是 `71 / 635`；旧 exact-v1 仅在 identity/claim 不变时复用。

## Final independent denominator and Books disposition

- raw identities：706。
- Candidate：71。
- Close：635。
- 相对作者侧 checkpoint：8 项 de-admit，3 项 restore。
- 旧 8 项 Integrate：8 项已有覆盖，0 项整合，0 项正文缺口。
