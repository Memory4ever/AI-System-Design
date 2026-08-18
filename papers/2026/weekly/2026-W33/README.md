# Weekly Research — 2026-W33

**Coverage Window:** 2026-08-10～2026-08-16（Monday～Sunday, Asia/Shanghai）  
**Generated:** 2026-08-16  
**Status:** Discovery/Evidence Gate Reopened on 2026-08-17；25 Full Source Reviews Complete；32 Discovery Review Pending；Correction Books Gate Closed

## Executive Summary

W33 的重要变化不是某一个产品 release，而是三条跨日证据链同时变得清晰：

```text
粗粒度状态 / 资源 / 消息
→ 暴露真正的 decision boundary
→ 只移动、同步或更新下游需要的最小对象
→ 同时保留 authority、provenance、rollback 与旧方案成立条件
```

第一条是 Agent state lifecycle：Prompt/Skill 从追加走向可删除、可压缩；Memory 从孤立 record 走向 provenance
graph、selective repair 与 associative evidence set；Workflow 再把 candidate retention 与 authoritative activation
分开。第二条是 runtime granularity：TP 从完整 tensor materialization 下沉到 sufficient statistics，KV 从 block
paging 下沉到 token liveness/reclamation，MoE 从 token proxy 转向 regime-aware makespan，Autoscaling 从 model
replica 下沉到 operator DAG。第三条是 proposal 与 authority 的分离：diffusion tree、latent prefix、selective
distillation signal、Agent-generated implementation 都可以提出候选，但 target verifier、workflow commit、outcome
verifier 与 machine-checked artifact 仍拥有最终裁决。

七份 Daily 最初去重得到 21 个 W33 owner candidates，全部达到 20 分且完成 primary-source Full Source Review；
原有 16 Refine / 5 No Change 及其 Books 修改继续保留。2026-08-17 discovery replay 发现 Sunday 扫描遗漏了
arXiv 8 月 14 日展示批次。补充批次中 QuoteBench、OmniScientist、Beyond Final Scores 与 AlayaWorld 已完成
Full Source Review；另有 32 个 source family 只完成 identity 发现，等待日期、revision、去重、评分与全文审计。
因此原“Weekly Complete”结论撤回，correction Books Gate 关闭。8 月 9 日的 Beyond Routing 仍归 W32。

## Coverage Window and Limitations

- 7/7 Daily：[`08-10`](../../08/10/README.md)、[`08-11`](../../08/11/README.md)、
  [`08-12`](../../08/12/README.md)、[`08-13`](../../08/13/README.md)、
  [`08-14`](../../08/14/README.md)、[`08-15`](../../08/15/README.md)、
  [`08-16`](../../08/16/README.md)。
- 事件按 arXiv v1 / official release 的 first-public date 归属，不按 recent-page 展示日、Daily 发现日或后续
  technical-report upload 重写日期。
- 21 个 candidates 均有正文级审计；没有以 abstract、Scholar/HF 摘要或社区热度替代论文。
- 作者 benchmark 只属于各自 model、hardware、precision、length、batch/concurrency、evaluator 与 SLO contract；
  未披露字段保持 `Not Disclosed`。
- Intern-S2 是 8 月 13 日 related source update，不重复记为模型 release；其多组件联合结果不能拆成组件因果收益。
- Sunday 扫描没有取回 8 月 14 日展示批次；2026-08-17 已将其确认为 discovery gap，而非“没有更新”。
- 原 21 项审计与 disposition 保留；新增四项完成 E2 review，32 项保持 Discovery Review Pending，不能计为
  retained row、No Change 或 Full Source Review。

## Discovery Recall Ledger

| Ledger Item | Count | Review Result |
| --- | ---: | --- |
| Daily coverage | 7 / 7 | complete Monday～Sunday window |
| Scored W33 owner candidates | 25 | original 21 + 4 correction Full Reviews |
| High `25–30` / Medium `20–24` | 22 / 3 | correction queue not yet scored |
| Full Source Reviews | 25 | original 21 + QuoteBench / OmniScientist / Beyond Final Scores / AlayaWorld |
| Discovery Review Pending | 32 | identity found；date/revision/dedup/score/full read pending |
| Review Pending | 0 among scored rows | discovery queue remains outside scored ledger |
| Blocked / Unverified | 0 | no material request required |
| Cross-week spillback | 1 | Beyond Routing / FDAA belongs to W32 (2026-08-09) |
| Version-only Engineering events | 0 | no in-window release retained |
| Books refinements / No Change | 16 / 8 + 1 Books Pending | original 21 retained；three correction No Change；QuoteBench pending |
| W33 Evidence Gate | Reopened | discovery queue prevents closure |
| W33 Books Gate | Closed for correction | no new Books write until evidence gate closes |

## 1. 模型与研究机构

### Source Coverage

七份 Daily 按固定顺序覆盖 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google Research、Meta AI /
FAIR、Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、Qwen、DeepSeek、
Kimi、Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、StepFun、Xiaomi MiMo、
InclusionAI 与 Hugging Face Blog。

未发现同时满足 in-window first-public、公开机制与长期门槛的新模型发布。Intern-S2 technical report 作为
Source Family update 完成联合审计，保留一条评分行，但不制造第二个 release event。

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Intern-S2-Preview technical report | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | No Change Ch33；Source-family synthesis |

## 2. arXiv / 学术来源

### Candidate Scoring and Books Disposition

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SwiftQK | 2026-08-10 | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Refine `TRAIN-TENSOR-PARALLEL` Ch37 |
| QueryProof / WarehouseReliabilityBench | 2026-08-10 | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | No Change `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Recovering Wasted Compute in Autoresearch Agents | 2026-08-11 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `AGENT-WORKFLOW` Ch81 |
| Catastrophic Remembering | 2026-08-11 | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | Refine `AGENT-PROMPT` Ch74 |
| Dependency-Guided Rollback Repair | 2026-08-11 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `AGENT-MEMORY` Ch77 |
| MAP-Graph | 2026-08-11 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `AGENT-MEMORY` Ch77 |
| SkillZip | 2026-08-11 | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | Refine `AGENT-PROMPT` Ch74 |
| Agent Skills Can Be Harmful | 2026-08-12 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `AGENT-PLATFORM` Ch84 |
| Beyond Memory: Transactional Continuity Kernel | 2026-08-12 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `AGENT-WORKFLOW` Ch81 |
| ForeWAM | 2026-08-12 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine `MULTIMODAL-EMBODIED-VLA` Ch26 |
| The Sleeping Agent | 2026-08-12 | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Refine `AGENT-CONTEXT` Ch75 |
| vToken | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `INFER-PAGED-ATTENTION` Ch47 |
| TEMPO | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `INFER-TENSORRT-LLM` Ch49 |
| OpScale | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine `INFER-SCHEDULING` Ch56 |
| DARTree | 2026-08-13 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | No Change `INFER-SPECULATIVE-DECODING` Ch48 |
| Vero | 2026-08-13 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | No Change `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| RippleMem | 2026-08-13 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine `AGENT-MEMORY` Ch77 |
| StateBridge | 2026-08-13 | 4 | 3 | 4 | 4 | 4 | 5 | 24/30 | Refine `AGENT-MULTI-AGENT` Ch82 |
| CROP | 2026-08-13 | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Refine `TRAIN-GRPO` Ch33 |
| Post-Norm under Curriculum Depth Growing | 2026-08-13 | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | No Change `MODEL-TRANSFORMER-LAYER` Ch17 |

## 3. AI Infra 与工程项目

### Source Coverage

七份 Daily 检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、
Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、MLX、llama.cpp、ONNX Runtime 与
OpenXLA official release / RFC / PR surfaces。没有确认到 first-public date 位于 W33 且形成长期机制增量的新事件。
搜索中出现的 vLLM v0.21.0 实际发布于 5 月 15 日，不迁移到 W33。

### Candidate Scoring

本组没有 retained candidate。

## Deep Analysis 1 — Agent State：从“保存更多”到可授权、可恢复的生命周期

### Why and Principle

Append-only Prompt、完整 transcript 与 isolated branch 在短任务中合理：实现简单、证据直接、故障隔离清楚。
长期运行后，它们分别暴露 instruction bloat、错误记忆传播、Context 成本和重复搜索。演进的关键不是保存更多，
而是把 candidate、derived state、authoritative state 与 immutable evidence 分开。

### Mechanism and Evolution

```text
append-only instruction / raw episode
→ rationale-aware delete and typed consolidation
→ provenance-aware derived graph
→ selective state + execution repair
→ transactional candidate activation
→ anchor recall + bounded evidence expansion
→ independently tested Skill admission
```

Prompt/Skill writer 只能提出或压缩候选；Memory graph 维护 source/dependency/supersession；Workflow controller 提交
activation、rollback 或 compensation；Evaluation/Agent Platform 决定 Skill 的 marginal utility 是否覆盖新 failure
surface。RippleMem 补的是 read path 的 evidence set，不替代 MAP-Graph/rollback 的 update path。

### Trade-off and Boundary

结构化 state 增加 schema drift、writer/judge bias、dependency maintenance、delete propagation、commit/replay 与
authorization cost。Raw history 在取证、短任务、低更新率时仍成立；isolated branch 在 side effect 难协调时继续
安全；自动 compression 不得覆盖 immutable evidence。五篇 8 月 11 日与四篇 8 月 12 日论文、RippleMem 的作者
实验只提供受限 mechanism evidence，不证明生产 autonomy 或固定 taxonomy。

## Deep Analysis 2 — Runtime Granularity：最小对象必须由下游语义决定

### Why and Principle

完整 tensor、KV block、token count 与 model replica 都是早期合理控制单元：容易实现、易于恢复、测量稳定。
当 workload、memory pressure、MoE regime 与 burst speed 改变时，粗粒度会让系统移动不需要的数据、无法回收
已死亡状态、误价最慢 rank 或扩容非瓶颈 operator。新粒度只有在可测量、可提交、可恢复时才是演进。

### Mechanism and Evolution

```text
TP full-tensor materialization → sufficient-statistic reduction
block paging → token liveness → pressure-activated physical reclamation
token/expert proxy → calibrated activation/compute/communication regimes → makespan dispatch
model replica → stage split → operator-DAG elasticity
```

SwiftQK 从 QK-Norm 语义推导 scalar平方和；vToken 分开 logical victim 与 physical slot/block reclaim；TEMPO 分开
router choice、placement 与 dispatch cost；OpScale 分开 logical provisioning 与 physical placement/SLO validation。
四者共同支持“最小对象由 consumer/decision semantics 决定”，并不构成一个共享实现。

### Trade-off and Boundary

更细粒度新增 synchronization、indirection、copy、calibration、profile drift、interference 与 partial-failure semantics。
AllGather 在 consumer 需要完整 tensor 时成立；full KV retention 在 capacity 足够时优先；静态 MoE balance 在
regime 稳定时更简单；model replica 在低 QPS、megakernel 或 failure unit 必须完整时继续成立。论文硬件从
RTX/A100/H100 到 GB200，不能把任一 headline 拼接成通用 fleet gain。

## Deep Analysis 3 — Proposal Channel 扩张后，Authority 反而必须更清楚

### Why and Principle

Diffusion drafter、latent message、teacher token signal 与 coding Agent 都能提高候选覆盖或压缩信息，但它们各自
携带 approximation、compatibility、bias 或 specification risk。演进不是让 proposal 直接获得控制权，而是扩张
候选通道的同时，把 commit/verdict 绑定到更强、可复算的 authority。

### Mechanism and Evolution

```text
parallel diffusion proposal → causal correction / tree pruning → target exact verification
text message → aligned continuous prefix → typed artifact / Workflow commit
uniform teacher supervision → counterfactual relevance selector → outcome-verifier direction
function-level code check → repository implementation + proof artifact → machine-checked build
```

DARTree 的 depth-wise correction 和 deferred pruning 已由 Ch48 的并行 proposal/tree verification 主线覆盖；
StateBridge 增加 cross-model alignment，却不能替代 message/state boundary；CROP 只改变有限 teacher budget 的落点；
Vero 说明高 per-spec pass rate 不等于 repository completion，proof closure 也不保证 specification 完整。

### Trade-off and Boundary

更丰富 proposal 会增加 verify shape、continuous-prefix security、triplet construction、lemma/library maintenance 与
specification audit cost。Classic AR drafter、文本消息、full-token OPD、普通 tests 在耦合成本高或权威证据不足时
仍成立。DARTree、StateBridge、CROP 与 Vero 因此不是相互替代，而是 `Principle Reuse`：**proposal 越自由，
authority、identity、fallback 与 replay contract 越不能隐含。**

## Cross-Week Deduplication

- Beyond Routing / FDAA 的 v1 first-public date 为 2026-08-09，owner 是 W32；8 月 11 日只完成发现/分析，不在
  W33 重复评分。其跨域失败与窄 intervention 使其继续 `Emerging / Experimental`。
- Intern-S2 technical report 是已有 model family 的 related source，不重复计为 release；其 source-family mechanisms
  只对 Ch33 提供 `No Change` 联合证据。
- DARTree 与此前 Domino/DFlash/DDTree/DSpark 属同一 speculative source family 演进；W33 记录新 pruning/correction
  evidence，正文不重复建立算法清单。
- RippleMem 与 W32 HiGram、MAP-Graph 不合并成同一事件：前者主要拥有 read-time anchor expansion，后两者主要
  拥有 derived-state update/provenance；关系是 layering，不是 revision。
- StateBridge 与早期 Vision Wormhole 都是 latent communication 分支，但传递对象和 alignment contract 不同，
  分别保留 source identity，共享 Ch82 owner。

## Event-Date Daily Decision

| Event Date | Daily Owner | Weekly Action |
| --- | --- | --- |
| 2026-08-10 | 08-11 Daily | SwiftQK / QueryProof 保留；旧索引项排除 |
| 2026-08-11 | 08-13 Daily | 五项 Agent state/workflow papers 保留 |
| 2026-08-12 | 08-14 Daily | 四项 Skill/Workflow/Embodied/Context papers 保留 |
| 2026-08-13 | 08-15 Daily + 08-16 review | 十项 paper/report candidates 保留并闭合 E2 review |
| 2026-08-09 | 08-09 Daily / W32 | Beyond Routing spillback，不计入 W33 |

## 2026-08-17 Discovery Correction

### Completed Source Reviews

| Candidate | Source Family | Score | Full-read Boundary | Provisional Disposition |
| --- | --- | ---: | --- | --- |
| QuoteBench | `arxiv:2608.13547` | 29/30 | metadata、method、fixed-output replay、SSH/JSON validation、statistics、validator audit、limitations/appendix | Books Pending；Ch66 owner / Ch80 handoff |
| Beyond Final Scores | `arxiv:2608.13417` | 28/30 | process metrics、resource/cost、experience reuse、harness comparison、limitations/appendix | No Change Ch66/Ch81 |
| OmniScientist | `arxiv:2608.13558` | 27/30 | multimodal evidence taxonomy、three-Agent pipeline、deterministic gates、evaluation/ablation、bias checks、limitations | No Change Ch23/Ch66/Ch81 |
| AlayaWorld | `arxiv:2608.13492` | 26/30 | motion-aware conditioning、3D point-cache memory、protocol alignment、WBench evaluation、limitations | No Change Ch25；Experimental update |

四项均以 2026-08-13 v1 first-public date 归入 W33。QuoteBench 证明生成正确性与 transport 正确性必须分层
测量，但其长期正文位置要等 correction batch 结束后再判断；后三项的机制已由现有 owner 章节覆盖，不复制论文
方案。完整 Why→Mechanism→Trade-off→Evidence boundary 位于 08-17 Daily。

### Discovery Review Queue

下列 32 项只完成 identity 发现，尚未完成日期/revision、跨分类/跨周去重、评分与 Full Source Review：

```text
2608.13517 DFM Mimir v1
2608.13515 Measuring Task-Agnostic Training Data Influence
2608.13520 Data Geometry of Masking Diffusion
2608.13545 LittleLearner
2608.13538 SAEVerbalizer
2608.12888 When Your Agent Opens the Chat App
2608.12851 Practice Makes Unsafe
2608.12847 Query-Conditioned Reuse of Long-Horizon Agent Trajectories
2608.12932 FlashDrive
2608.12788 ARAC
2608.12585 Reasoning Jury
2608.12720 ERSkill
2608.12627 EgoCITE
2608.12915 InFactPlanner
2608.13076 SPADE
2608.13179 Verifier-Bounded Credit Assignment
2608.13173 SkillShapley
2608.13120 SkillEvo
2608.13060 VALG
2608.13046 BoardroomAI
2608.13043 Local Mismatch to Global Impact
2608.12895 Agent Behavioral Contracts II
2608.12892 Predictive Memory Localization
2608.13456 Causal World Models survey
2608.13267 Scientific-Figure Behavioral Evaluation
2608.13160 TRAPSBench
2608.12440 Specification-First Convergence
2608.13410 Who Speaks Matters
2608.13389 TopoIntent
2608.13459 CAPRI
2608.12322 What Drives LLM Self-Reflection
2608.12321 LLMs Know the Constraint But Do Not Use It
```

这些条目不计入 retained-row denominator。只有完成 source-family identity、event ownership 和六维评分后，
`20+` 候选才进入非模板化 Full Source Review；低分候选也必须保留来源、日期与拒绝理由。

## Books Integration Decision

### Correction Gate

- 原 21 项 Books disposition 与正文修改保留，不因 discovery gap 回滚。
- OmniScientist、Beyond Final Scores、AlayaWorld 为章节级 No Change；只增加 source-family evidence。
- QuoteBench 保持 `Books Pending`；32 项 discovery queue 不进入 Books。
- W33 correction Evidence Gate 通过前，不新增 Books 修改，也不宣称 W33 全周 Integration Complete。

### Integrated / Refined

- Ch26 `MULTIMODAL-EMBODIED-VLA`：ForeWAM 的 explicit future → joint WAM → direct-policy latent interface。
- Ch33 `TRAIN-GRPO`：CROP 的 task relevance vs optimization need；既有 Intern-S2 partial-rollout/online-draft 主线不重复。
- Ch37 `TRAIN-TENSOR-PARALLEL`：SwiftQK 的 algebra-first sufficient-statistic communication。
- Ch47 `INFER-PAGED-ATTENTION`：vToken 的 block paging → token liveness → asynchronous physical reclamation。
- Ch49 `INFER-TENSORRT-LLM`：TEMPO 的 proxy balance → regime-calibrated makespan dispatch。
- Ch56 `INFER-SCHEDULING`：OpScale 的 model/stage → operator-DAG elasticity。
- Ch74 `AGENT-PROMPT`：instruction rationale、deletion contract 与 typed Skill consolidation。
- Ch75 `AGENT-CONTEXT`：The Sleeping Agent 的 typed preservation/compression contract。
- Ch77 `AGENT-MEMORY`：MAP-Graph / rollback 的 provenance repair，加 RippleMem associative evidence read path。
- Ch81 `AGENT-WORKFLOW`：shared constraint registry 与 candidate→authoritative activation transaction。
- Ch82 `AGENT-MULTI-AGENT`：StateBridge training-free latent alignment，保留 proposal-only authority。
- Ch84 `AGENT-PLATFORM`：Skill paired execution、failure surface 与 marginal-cost admission。

### No Change / Weekly Evidence Only

- QueryProof：Ch66 已有 behavior contract、executable verifier、abstain/refuse 与 false-success boundary。
- DARTree：Ch48 已有 parallel diffusion proposal、causal correction、dynamic tree、exact target commit；只补 source note。
- Vero：Ch66 已有 repository artifact、process/build evidence 与 specification/evaluator boundary；只补 source note。
- Post-Norm Curriculum：Ch17 已将 normalization placement 与 residual/training path 联合设计；受限九层实验不改写主线。
- Intern-S2 report：Ch33 已有 partial rollout lifecycle、staleness correction、online draft、typed credit 与 multi-task边界；
  组件缺 matched ablation，不从联合 recipe 外推。

## Repository Changes

- 新增本 W33 Weekly，并同步年度 Weekly 索引。
- 保留 8 月 13～15 日已经完成的 Books 修改；8 月 16 日新增 Ch33、Ch37、Ch77、Ch82 refine。
- Ch17、Ch48、Ch66 仅补 No Change primary-evidence notes；同步 8 月 11、15、16 日 Daily 状态。
- 2026-08-17 新增 discovery correction：补四份 Full Source Review、32 项发现队列，并重开 W33 gate；
  correction batch 暂未修改 Books。
- 更新 `docs/LEARNING_STATE.md`；ROADMAP、DECISIONS、Part/章节结构保持不变。
- 未 stage、commit、push、reset、checkout 或 clean。

## Open Questions

1. SwiftQK 的 sufficient-statistic path 在 PCIe、跨节点或其他 accelerator collective 上何时仍优于 AllGather？
2. vToken 的 relocation 如何跨 TP、multi-KV-group 与 shared prefix 保持 atomic visibility？
3. TEMPO calibration 与 OpScale profiles 在 kernel/hardware revision 后如何检测 expiry 而不形成控制环振荡？
4. Associative Memory 的 graph expansion 如何与 delete、ACL、concurrent update 和 independent judge 联合验证？
5. Continuous latent prefix 如何获得 security scan、跨版本 compatibility、audit projection 与 deterministic replay？
6. Selective OPD 的 counterfactual difficulty 与 triplet construction cost 是否会抵消有限 token budget 的收益？
7. Vero 的 repository-scale proof benchmark 怎样扩展到 concurrency/temporal properties 与 maintenance patches？
8. 32 项 discovery queue 中哪些应回拨到更早 week，哪些是 cross-list/revision 或低分边界候选？
9. QuoteBench 的 generation/transport 二维合同是否需要 refine Ch66，还是现有 EvalSpec 已能完整表达？
10. Sunday scan 怎样保存分类页 count、last-seen arXiv identifier 与 replay evidence，避免“页面可访问但批次未召回”？

## Sources

### Live Dailies

- 2026-08-10: ../../08/10/README.md
- 2026-08-11: ../../08/11/README.md
- 2026-08-12: ../../08/12/README.md
- 2026-08-13: ../../08/13/README.md
- 2026-08-14: ../../08/14/README.md
- 2026-08-15: ../../08/15/README.md
- 2026-08-16: ../../08/16/README.md
- 2026-08-17 correction: ../../08/17/README.md

### Primary Papers and Reports

- SwiftQK: https://arxiv.org/html/2608.09160
- QueryProof / WarehouseReliabilityBench: https://arxiv.org/html/2608.09254
- Recovering Wasted Compute: https://arxiv.org/html/2608.10424
- Catastrophic Remembering: https://arxiv.org/html/2608.11095
- Dependency-Guided Rollback Repair: https://arxiv.org/html/2608.10502
- MAP-Graph: https://arxiv.org/html/2608.10509
- SkillZip: https://arxiv.org/html/2608.11079
- Agent Skills Can Be Harmful: https://arxiv.org/html/2608.11888
- Beyond Memory: https://arxiv.org/html/2608.11632
- ForeWAM: https://arxiv.org/html/2608.11605
- The Sleeping Agent: https://arxiv.org/html/2608.11775
- Intern-S2-Preview report: https://arxiv.org/html/2608.13505
- vToken: https://arxiv.org/html/2608.13263
- TEMPO: https://arxiv.org/html/2608.13057
- OpScale: https://arxiv.org/html/2608.13499
- DARTree: https://arxiv.org/html/2608.13524
- Vero: https://arxiv.org/html/2608.13522
- RippleMem: https://arxiv.org/html/2608.13334
- StateBridge: https://arxiv.org/html/2608.13317
- CROP: https://arxiv.org/html/2608.13387
- Post-Norm Curriculum: https://arxiv.org/html/2608.13156
- QuoteBench: https://arxiv.org/html/2608.13547
- OmniScientist: https://arxiv.org/html/2608.13558
- AlayaWorld: https://arxiv.org/html/2608.13492
- Beyond Final Scores: https://arxiv.org/html/2608.13417

### Official Discovery and Engineering Surfaces

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Google DeepMind: https://deepmind.google/research/publications/
- Hugging Face Papers: https://huggingface.co/papers
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- Google Scholar: https://scholar.google.com/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/
- vLLM releases: https://github.com/vllm-project/vllm/releases
- SGLang releases: https://github.com/sgl-project/sglang/releases
- KServe releases: https://github.com/kserve/kserve/releases
