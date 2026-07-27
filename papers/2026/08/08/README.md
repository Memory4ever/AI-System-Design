# Daily Research — 2026-08-08

**Coverage Window:** 2026-08-06 09:02 ～ 2026-08-08 09:02（Asia/Shanghai）
**Access Date:** 2026-08-08
**Archive Clock:** Saturday；仅生成 Daily，不生成 provisional `2026-W32`
**Status:** Primary-source review complete；3 项完成全文复核，2 个既有章节被 refine

## Executive Summary

过去 48 小时未发现模型公司官方 Research 中同时满足首次公开日期、公开机制和长期 AI System
增量的新发布。主要证据来自 2026-08-05 首次公开、在 8 月 7 日 arXiv new listing 中进入检索窗口
的论文，以及上一日 Watch candidate 的全文复核：

1. **Architectural Implications of Agentic AI Workflows** 把 Agent workload 从“更多模型调用”展开
   为跨 CPU、GPU、tool 与 orchestration 的 bursty execution graph。长期增量是 workflow shape 应
   成为资源 contract；CPU harvesting、GPU residency consolidation 与 role affinity 只在存在真实
   stranded capacity、swap/prefetch 可隐藏且 tail SLO 有 headroom 时成立。
2. **SearchAuditor** 把 Reflection 从“知道失败”推进到 `localize → attribute → repair`。它也明确
   暴露证据边界：offline auditor 已知 run 失败，只看到 frozen trace，单一原因 schema 不能表达
   co-causal failure，作者最佳端到端通过率仍不足三分之一。
3. **SkillTrace** 把可复用 Agent Skill 视为 metadata、instructions、code、tools、references 与
   workflow 组成的混合模态资产。Expression、Implementation 与 Operational traces 可以形成带
   证据指针的 provenance review queue，但不能自动判定抄袭、许可违规或供应链恶意。
4. 工程项目在本窗口没有新的正式 Release 改变长期机制。Dynamo v1.3.1、KServe v0.20.0、
   SGLang v0.5.16、PyTorch v2.13.0 等仍是此前版本事实，不重复计为新事件。

三项 Deep Analysis 均为单篇 v1 preprint，Evidence Level 为 `Experimental`。Books 只吸收机制、
owner 边界、反例与 failure modes，不吸收作者 headline benchmark，也没有新增 Part、章节或
ROADMAP node。

## 1. 模型与研究机构

### Source Coverage

按 `CODEX_DAILY_RESEARCH_PROMPT.md` 的固定顺序检查：

- **OpenAI — No Material Update**
- **Anthropic — No Material Update**
- **Apple Machine Learning Research — No Material Update**
- **Google DeepMind — No Material Update**
- **Google Research — No Material Update**
- **Meta AI / FAIR — No Material Update**
- **Microsoft Research — No Material Update**
- **NVIDIA Research — No Material Update**
- **xAI News / Model Cards — No Material Update**
- **Amazon Science / AGI — No Material Update**
- **Cohere Labs — No Material Update**
- **Ai2 — No Material Update**
- **Mistral AI — Access Limited；官方 Research 页面本次返回错误，未发现可核验新事件**
- **Alibaba Qwen — No Material Update**
- **DeepSeek — Access Limited；官方 News 页面本次无法打开，未发现可核验新事件**
- **Moonshot AI / Kimi — No Material Update**
- **Zhipu AI — No Material Update**
- **MiniMax — No Material Update**
- **ByteDance Seed / Research — Access Limited；入口可达但未返回可检查列表**
- **Baidu ERNIE — No Material Update**
- **Tencent Hunyuan — No Material Update**
- **Huawei Noah's Ark Lab / Pangu — No Material Update**
- **Shanghai AI Laboratory / InternLM — No Material Update**
- **StepFun — Access Limited；官方 Research 页面本次返回错误，未发现可核验新事件**
- **Xiaomi MiMo — No Material Update**
- **InclusionAI / Ant Group — No Material Update**
- **Hugging Face Blog — No Material Update**

搜索结果中的旧文章重收录、产品更新、模型榜单、partner marketing，以及没有 technical report、
model card、system card 或论文支撑的功能 headline 均未进入候选。

上述 `Access Limited` 不等于“确认没有更新”。本轮以同机构的可访问官方入口、arXiv 作者/机构
metadata 与搜索发现做交叉检查，但没有找到可由 primary source 复核的窗口内事件；这些入口应在
W32 Sunday 聚合时再次检查。

### Candidate Scoring

本组无达到候选门槛的窗口内新事件。

## 2. arXiv / 学术来源

### Source Coverage

按 primary-source 顺序检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`stat.ML` 的
2026-08-07 new listings，并按关键词扩展到 `cs.AR`、`cs.OS`、`cs.CR` 与 `cs.MA`。同时检查
OpenReview/TMLR 与 Hugging Face Daily Papers；Hugging Face 的日期页在本次访问中返回错误，因而
仅以 arXiv new listing 和正文完成主检索，不把该覆盖缺口写成“已无新增”。Google Scholar、
Semantic Scholar、OpenAlex 与 DBLP 只用于 metadata、identifier、作者和 first-public date 的
discovery/cross-check，不替代论文正文或 revision history。

三项 Deep Analysis 均读取 arXiv HTML 的 metadata、Introduction/Background、Related Work、
Method、系统结构、Implementation、Evaluation setup、baselines/ablation、limitations/threats、
Conclusion 及影响结论的 appendices。论文未设置独立 Limitations section 时，从 annotation protocol、
discard criteria、wild audit 与反例中恢复可见边界，并明确标为作者未集中披露的限制。

### Candidate Scoring

评分维度依次为 Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、Source
Reliability（SR）、Project Relevance（PR）、Longevity（L），每项 0～5。

| Candidate | TN | SI | PV | SR | PR | L | Total | Evidence / Action |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Agentic workflow architecture / Agora | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Experimental；Refine Ch80 |
| SearchAuditor | 5 | 4 | 5 | 4 | 5 | 5 | 28 | Experimental；Refine Ch76 |
| SkillTrace | 4 | 4 | 5 | 4 | 5 | 5 | 27 | Experimental；Refine Ch80 |
| SMRC-SD: state-matched agent distillation | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Must Read；W32 source family |
| Project2Task | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Must Read；W32 source family |
| Search2Skill | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Must Read；W32 source family |
| LUNAR personalization benchmark | 3 | 4 | 3 | 4 | 4 | 4 | 22 | Watch；benchmark contract |

`SR=4` 表示可以直接访问作者 preprint、HTML 与 metadata，但尚未 peer review；它不是对 production
readiness 或结论可复现性的满分背书。三项中只有 Agent workflow architecture 在昨日 Daily 已列为
Watch；今天完成全文 Source Packet，不把 first-public event 重写为 8 月 8 日。

### Deep Analysis 1 — Architectural Implications of Agentic AI Workflows

**Primary source:** arXiv:2608.04458v1，first public 2026-08-05。
**Evidence Level:** Experimental / 24-hour production trace + bounded controlled study。
**Knowledge Tree:** Ch80 Agent Platform（owner）→ Ch77 Workflow → Ch59 GPU Scheduler。

#### Why

把 Agent workload 当作普通 LLM request，会隐藏 host orchestration、tool execution、等待和多模型
切换。传统 server provisioning 倾向按平均 utilization 和同质 core/GPU 配置做容量规划；但 Agent
request 会展开成时变 workflow，平均空闲并不等于 burst 到来时仍有安全 headroom。

#### Principle

资源 demand 是 workflow structure 的函数，而不只是 model identity 的函数：

```text
orchestration owner × sequential/parallel execution × model composition
→ CPU critical path、tool burst、GPU residency 与 locality pattern
→ conditional harvesting / consolidation / affinity policy
```

因此资源控制器需要看到 workflow role、ready state、residency 与 tail-SLO signal；同时必须保留
旧方案的成立条件：稳定的单模型 serving、持续高负载或并行工作流可能根本没有可收割空闲。

#### Mechanism

论文先按 orchestration、execution 与 model composition 建立 taxonomy，再用 Microsoft Azure 的
24 小时 fleet trace 和四个开源框架进行 characterization。Agora 原型组合三类机制：

- 在保留 burst protection 的前提下把 idle CPU cores 借给 co-located throughput workload；
- 在 state prefetch/swap 可隐藏时增加 GPU 上的 agent/model residency；
- 按 scheduler/orchestrator/runner 等 role 建立 core pool 与 affinity，减少共享 core 的 locality loss。

受控研究运行在 96-core AMD EPYC 7V12 与 8×NVIDIA A100 server，覆盖 SWE-Agent、Trae、CORAL、
Owl，并为不同 Agent role 设置独立 vLLM instance；作者测试 concurrency 1～32。Production trace 的
fleet size、request count 与 raw trace 未披露，不能据此构造 fleet-wide capacity estimate。

#### Trade-off

- Owl 存在较多 stranded GPU capacity，作者可回收部分设备；CORAL 的 parallel workflow 已较充分
  使用 GPU，harvesting 几乎没有空间且可能伤害 throughput。这是机制的关键反例。
- Low-load CPU harvesting 与 high-load harvesting 的可保留背景吞吐差异很大；作者数字只属于其
  workload 与 slowdown guard，不形成通用百分比。
- 更高 residency 引入 state prefetch/swap、HBM oversubscription、cache identity 与 eviction failure；
  role-aware pools 又可能降低共享弹性。
- 论文没有独立 Limitations section，也没有证明机制跨 GPU generation、network topology、tool mix、
  failure recovery 和 multi-tenant isolation 保持相同效果。

#### Connection / Evolution

这是 Ch80 的 `Layering / Dependency`：第 59 章仍在 seconds-to-minutes 层做 Pod/gang/device placement，
Ch80 在 run/step 层表达 Agent workflow 的 burst、role、tool 和 waiting demand。演进不是把 GPU
Scheduler 替换成 Agent Scheduler，而是：

```text
request-level average provisioning
→ workflow-visible phase/role demand
→ conditional harvesting and residency control
→ tail-SLO、state movement、fairness 与 recovery evidence
```

### Deep Analysis 2 — SearchAuditor

**Primary source:** arXiv:2608.05212v1，first public 2026-08-05。
**Evidence Level:** Experimental / curated failed-trajectory benchmark + bounded resume study。
**Knowledge Tree:** Ch76 Reflection（owner）→ Ch62 Evaluation → Ch77 Workflow。

#### Why

Agent final failure 不能指出最早的因果偏离。长 search trajectory 中，错误发生后仍可能产生大量
看似合理的检索、推理与写作；只重写最终答案会保留病因，完整重跑又浪费已验证状态。

#### Principle

Failure audit 应把 outcome、diagnosis 与 repair 分离：

```text
known failed outcome
→ earliest direct critical step / tolerance span
→ bounded primary root cause
→ evidence-grounded repair directive
→ gated resume, replay or replan
```

定位的不是第一个次优动作，而是最早有证据支持、对最终失败有直接影响的步骤。多个 audit 视角
需要 evidence-grounded adjudication，而不是在相关错误之间简单投票。

#### Mechanism

SearchAuditBench 从 3,500 条 raw trajectories 经 gradability、incorrectness 与 expert discard 筛选到
1,243 条失败轨迹，平均 73.1 messages、65.1K tokens，来自 8 个 open-weight models、5 个 deep-
search benchmarks 和统一 search/visit scaffold。四位作者团队 annotators 对 case 分工，每条由一人
完成 final annotation；LLM pre-screen 只提供建议，没有报告 inter-annotator agreement。

SearchAuditor 并行执行 holistic、backward-constraint 与 forward-timeline audit，再由 evidence-
grounded adjudicator 选择 critical step、root cause 与 repair。它假定 auditor 已知 run 失败，只读取
冻结的 query、answer 和 trajectory，不使用 gold answer 或 live web/tool。LiveBrowseComp 的恢复实验
从 predicted critical step resume，但仍只覆盖作者选择的 model、harness 与 failure cohort。

#### Trade-off

- 只有能从 trace 定位的失败进入 benchmark；flawed/stale task、evaluator false negative、incomplete
  trace 与无法离线审计的 environment failure 被排除。
- 每条 trajectory 只标一个 primary cause，会压缩多个共同致因；单 annotator per case 又让 label
  uncertainty 难以估计。
- 作者最佳配置的 exact localization、root-cause 与 fully-passed audit 仍有明显差距；auditor 不能
  作为自动 rollback/repair authority。
- 作者发现许多 token/tool calls 发生在决定性错误之后，这是该 corpus 的诊断证据，不代表所有
  Agent workload 都能通过 early stop 节省相同成本。

#### Connection / Evolution

这是 Ch76 的 `Direct Refinement`。原章节已有 constraint-wise audit 与 executable diagnostics；本次
补上 earliest causal step、tolerance span、repair boundary 与 resume gate。Ch62 仍负责 evaluator
是否可信，Ch77 负责实际 replay/resume 与 side-effect reconciliation。

### Deep Analysis 3 — SkillTrace

**Primary source:** arXiv:2608.05204v1，first public 2026-08-05。
**Evidence Level:** Experimental / constructed benchmark + unlabeled wild audit。
**Knowledge Tree:** Ch80 Agent Platform（owner）→ Ch55 Registry → Ch68 Security → Ch79 MCP。

#### Why

Agent Skill 不是纯代码包。复用可能只保留 instructions、实现片段或 activation/procedure/resource-flow
结构；代码 clone detection 和 whole-package similarity 都无法同时覆盖这些来源证据。

#### Principle

混合模态 artifact 的 provenance 必须保留多条互补 trace，同时把 detection 与 verdict 分开：

```text
versioned Skill package
→ Expression / Implementation / Operational evidence
→ per-trace calibrated similarity and evidence pointer
→ review queue
→ human/policy decision
```

Same-function similarity 不是 shared provenance。Operational structure 尤其容易因合理的通用流程而
碰撞，所以不能把单一高分变成法律、安全或许可结论。

#### Mechanism

SkillTrace 把 Operational Trace 表示为 typed Skill Operational Graph，拆成 Activation、Procedure、
Resource-Flow views。LLM 只在 ingestion 时辅助 operational extraction；prompt/version 固定并缓存，
audit-time pair comparison 保持 deterministic。各 trace threshold 用 same-function strict negatives
分别校准，并返回触发 trace 与 evidence pointer。

SkillTrace-Bench 包含 100 个 public anchors、820 个 positive transformations 和 751 个 negative
controls。36,446-Skill wild audit 没有完整 ground truth，因此只能展示 review queue，不能估计真实
侵权率或 prevalence。作者还在 global routing 中主动排除 Operational-only evidence，以避免 generic
same-function workflow collision。

#### Trade-off

- 许多 positives 是受控或 LLM-generated transformations，可能带有生成模型风格偏差。
- Operational extraction 即使 temperature 0、prompt versioned，仍可能生成粗糙或错误 graph；source
  revision 后还要 invalidation/re-extraction。
- Wild audit 只覆盖公开 registry，且没有完整 label；adversarial evasion 也不在 benchmark 内。
- 作者披露的 extraction time/cost 与 AUROC/F1 只属于其模型、prompt、dataset 和 hardware/service
  contract，不进入 Books。

#### Connection / Evolution

这是 Ch80 的 `New Mechanism`：把 Skill 纳入 Agent definition、registry、rollout 与 revocation graph。
Ch55 的 registry identity、Ch68 的 supply-chain enforcement 和 Ch79 的 MCP connection 仍各自成立；
多 trace provenance 只为这些控制面提供 review evidence，不替代它们。

### Evidence Level

- **官方事实**：title、authors、v1 time 与 revision history 来自 arXiv metadata；工程版本日期来自
  官方 GitHub Release。
- **论文实验结论**：taxonomy、mechanism、dataset、hardware、ablation、benchmark 与反例均按作者
  正文记录，并绑定披露的 workload contract。
- **自己的推断**：Ch76/Ch80 ownership、evolution relationship 与 Books disposition 是本仓库的
  integration judgment。
- **不得推断**：不能从 Agent workflow 论文外推统一 server topology，不能把 auditor 当 repair
  oracle，不能把 Skill similarity 当 plagiarism、license 或 security verdict。

## 3. AI Infra 与工程项目

### Source Coverage

按固定顺序检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、
Ray、KServe、Kubeflow、Kubernetes、Hugging Face Transformers、Hugging Face Accelerate、
DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

| Candidate | TN | SI | PV | SR | PR | L | Total | Evidence / Action |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Dynamo v1.3.1 | 2 | 4 | 4 | 5 | 5 | 3 | 23 | 2026-08-06 Version Fact；cross-day dedup |
| KServe v0.20.0 | 3 | 4 | 5 | 5 | 5 | 3 | 25 | 2026-08-06 Version Fact；W32 source family |
| SGLang v0.5.16 | 4 | 5 | 5 | 5 | 5 | 4 | 28 | 2026-07-25；W30 historical event，不重记 |

- **无窗口内新正式 Release**：官方 Releases 页面截至访问时，Dynamo 最新稳定 patch 仍为
  v1.3.1（8 月 6 日）；KServe 的相关 v0.20.0 event 已在前两日 Daily 记录；SGLang v0.5.16、
  PyTorch v2.13.0、Triton v3.7.1 等均早于窗口。
- GitHub 页面中的 nightly、rolling tag、dependency bump、未合并 PR、未来 roadmap 和搜索引擎
  重收录不作为 release event。
- 本日没有把工程版本功能表写入 Books。KServe v0.20.0 仍待 W32 对 routing、KV tiering、traffic
  splitting、DRA、tracing 与 rollout source families 做跨日联合复核。

## Knowledge Tree Position

| Candidate | Primary Owner | Target and adjacent chapters read | Books decision |
| --- | --- | --- | --- |
| Agent workflow architecture / Agora | Ch80 Agent Platform | Ch79～80；核对 Ch58～61、Ch77 | Refine — Existing Argument |
| SearchAuditor | Ch76 Reflection | Ch75～77；核对 Ch62 | Refine — Existing Argument |
| SkillTrace | Ch80 Agent Platform | Ch79～80；核对 Ch55/Ch68 | Integrate — New Mechanism |
| SMRC-SD / Project2Task / Search2Skill | Full Source Reviews complete 2026-08-13 | Ch29 / Ch75 / Ch73 | Experimental refine candidates；Books Gate closed |
| Engineering release facts | 各 runtime owner | Ch45～61 | Weekly Only / cross-day dedup |

没有新增 ROADMAP node、Part 或章节。Ch59 保持 cluster placement owner，Ch55 保持通用 registry
owner，Ch68 保持 supply-chain enforcement owner，Ch79 保持协议 owner；Ch80 只吸收 Agent-specific
asset 与 run resource semantics。

## Recommended Action

- 已 refine Ch76：加入 earliest critical-step localization、root-cause attribution、repair directive、
  resume gate，以及 frozen-trace / single-cause / human-review boundary。
- 已 refine Ch80：加入 Skill 的 mixed-modality identity、multi-trace provenance、deterministic audit 与
  review-only verdict；加入 workflow-visible resource demand、conditional harvesting/consolidation 与
  Ch59 的时间尺度边界。
- SMRC-SD、Project2Task、Search2Skill 与 LUNAR 已在 2026-08-13 完成全文、相互去重与章节联读；
  ElastiCo、OasisKV 两项同日恢复并评分，均保留为 W32 source families。
- Sunday 2026-08-09 完成当日 Daily 后，再汇总 2026-W32（2026-08-03～2026-08-09）；不提前生成。

## Books Integration

### Absorbed

- `books/part-06-agent/76-reflection.md`：把 final failure 拆成 earliest causal localization、bounded
  attribution、evidence-grounded repair 与 gated resume，并保留 offline audit 的不可见状态边界。
- `books/part-06-agent/80-agent-platform.md`：增加可复用 Skill 的版本化 mixed-modality contract、
  三类 provenance traces 与 human-review boundary；把 workflow shape 纳入 Agent runtime resource
  scheduling，同时保留 Ch59 的 cluster placement ownership。
- `docs/LEARNING_STATE.md`：同步两项稳定认知与三篇 Experimental evidence 的边界。

### Not Absorbed

- **SMRC-SD / Project2Task / Search2Skill / LUNAR**：全文已核验；前三项分别为 Ch29、Ch75、Ch73
  Experimental refine candidates，LUNAR 由 Ch62 既有 subject/harness/evaluator contract 覆盖。
- **ElastiCo / OasisKV**：从 discovery gaps 恢复为 28/30 Full Source Reviews；分别定位 Ch59、Ch46，
  仍受 single-GPU config scope 与特定 H100/PCIe/RoCE testbed 限制。
- **工程 Release**：没有新的窗口内 event；旧版本事实不重复进入 Books。

## Ignored Noise

- 模型榜单、community challenge、partner marketing 与缺少 primary technical evidence 的 headline。
- arXiv new listing 中仅增加 benchmark、缺少机制，或与 AI System Design 关联弱的条目。
- 没有 hardware、model、precision、length、batch、concurrency 与 SLO contract 的性能宣传。
- GitHub nightly、dependency bump、rolling build、未合并 PR、future roadmap 与搜索引擎重收录。
- 将相似性得分直接称为抄袭/攻击，或把 offline auditor 称为 autonomous repair system 的二次解读。

## Repository Changes

- 新增 `papers/2026/08/08/README.md`。
- Refine Ch76、Ch80，并同步 `docs/LEARNING_STATE.md`。
- 未修改 ROADMAP 或 `docs/DECISIONS.md`；未生成 provisional `2026-W32`。
- 运行前已有 staged/unstaged Books、Learning State、ADR、interview、历史 Weekly 与 8 月 Daily 修改
  均保留；未执行 stage、unstage、commit、push、reset、checkout 或 clean。

## Recovery Addendum — 2026-08-13

- SMRC-SD：state matcher、contextual teacher、GRPO fallback、ALFWorld/WebShop 与 leakage/shortcut 边界已核验。
- Project2Task：innovation lineage、decomposition strategy、task contracts、10-brief/judge evaluation 已核验。
- Search2Skill：search trigger/query/skill rubric、held-out no-search evaluation 与 failure taxonomy 已核验。
- LUNAR：behavior-log synthesis、19 models、full/curated/RAG/Mem0 与小样本 human/privacy 边界已核验。
- ElastiCo（28/30）：elastic configuration、interference-aware placement、64×A100 testbed 与 multi-GPU
  限制已核验；主 owner Ch59。
- OasisKV（28/30）：CPU/remote KV、lookahead sparse prefetch、vLLM/NIXL、H100/RoCE testbed 与
  miss/freshness/recovery 边界已核验；主 owner Ch46。
- Historical Books Gate 保持关闭，本次没有 Books 修改。

## Open Questions

1. Agent workflow shape 怎样在不把 millisecond runtime state 塞进 kube-scheduler 的前提下，形成
   admission、autoscaling 与 node-level controller 可消费的稳定 contract？
2. CPU burst protection、GPU residency swap 与 role affinity 的控制环如何避免相互振荡，并在
   multi-tenant tail SLO 下建立 fairness？
3. SearchAuditor 的 critical-step label 若存在多个共同原因，应使用 causal graph、set-valued label
   还是 staged diagnosis？怎样测量 annotator disagreement？
4. Offline trace 缺少 environment state 时，resume gate 怎样先 reconcile 外部副作用而不重复执行？
5. Skill Operational Graph 的 extractor revision 如何触发 invalidation、重抽取与历史 verdict
   supersession？
6. Same-function strict negatives 在通用 workflow 与 domain-specific procedure 中应怎样分别校准？
7. SMRC-SD 的 state matcher 是否会把环境 shortcut 或 reference leakage 当作“兼容状态”？

## Sources

访问日期均为 2026-08-08；论文日期为 arXiv first-public date，Release 日期为官方页面日期。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Apple Machine Learning Research: https://machinelearning.apple.com/
- Google DeepMind: https://deepmind.google/blog/
- Google Research: https://research.google/blog/
- Meta AI: https://ai.meta.com/blog/
- Microsoft Research: https://www.microsoft.com/en-us/research/blog/
- NVIDIA Research: https://research.nvidia.com/
- xAI News: https://x.ai/news
- Amazon Science: https://www.amazon.science/
- Cohere Labs: https://cohere.com/research
- Ai2 Papers: https://allenai.org/papers
- Mistral AI Research: https://mistral.ai/research
- Alibaba Qwen: https://qwenlm.github.io/
- DeepSeek: https://api-docs.deepseek.com/news/
- Moonshot AI / Kimi: https://www.kimi.com/
- Zhipu AI: https://www.zhipuai.cn/
- MiniMax: https://www.minimaxi.com/news
- ByteDance Seed: https://seed.bytedance.com/
- Baidu ERNIE: https://ernie.baidu.com/blog/zh/publication/
- Tencent Hunyuan: https://github.com/Tencent-Hunyuan
- Huawei Noah's Ark Lab: https://noahlab.com.hk/
- Shanghai AI Laboratory: https://www.shlab.org.cn/
- StepFun Research: https://www.stepfun.com/research
- Xiaomi MiMo: https://mimo.xiaomi.com/
- InclusionAI: https://www.inclusion-ai.org/publication/
- Hugging Face Blog: https://huggingface.co/blog

### Academic Sources

- Agent workflow architecture metadata（2026-08-05）: https://arxiv.org/abs/2608.04458
- Agent workflow architecture full HTML: https://arxiv.org/html/2608.04458
- SearchAuditor metadata（2026-08-05）: https://arxiv.org/abs/2608.05212
- SearchAuditor full HTML: https://arxiv.org/html/2608.05212
- SkillTrace metadata（2026-08-05）: https://arxiv.org/abs/2608.05204
- SkillTrace full HTML: https://arxiv.org/html/2608.05204
- SMRC-SD metadata: https://arxiv.org/abs/2608.05219
- Project2Task metadata: https://arxiv.org/abs/2608.05225
- Search2Skill metadata: https://arxiv.org/abs/2608.05245
- LUNAR metadata: https://arxiv.org/abs/2608.05246
- arXiv cs.AI new: https://arxiv.org/list/cs.AI/new
- arXiv cs.CL new: https://arxiv.org/list/cs.CL/new
- arXiv cs.LG new: https://arxiv.org/list/cs.LG/new
- arXiv cs.DC new: https://arxiv.org/list/cs.DC/new
- arXiv cs.IR new: https://arxiv.org/list/cs.IR/new
- arXiv stat.ML new: https://arxiv.org/list/stat.ML/new
- OpenReview: https://openreview.net/
- TMLR submissions: https://openreview.net/submissions?venue=TMLR
- Hugging Face Daily Papers: https://huggingface.co/papers
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### Engineering Sources

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- JAX Releases: https://github.com/jax-ml/jax/releases
- CUDA Toolkit Release Notes: https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
- Triton Releases: https://github.com/triton-lang/triton/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases
- TensorRT-LLM Releases: https://github.com/NVIDIA/TensorRT-LLM/releases
- Ray Releases: https://github.com/ray-project/ray/releases
- KServe Releases: https://github.com/kserve/kserve/releases
- Kubeflow Releases: https://github.com/kubeflow/community-distribution/releases
- Kubernetes Releases: https://github.com/kubernetes/kubernetes/releases
- Hugging Face Transformers Releases: https://github.com/huggingface/transformers/releases
- Hugging Face Accelerate Releases: https://github.com/huggingface/accelerate/releases
- DeepSpeed Releases: https://github.com/deepspeedai/DeepSpeed/releases
- Megatron-LM Releases: https://github.com/NVIDIA/Megatron-LM/releases
- Unsloth Releases: https://github.com/unslothai/unsloth/releases
- MLX Releases: https://github.com/ml-explore/mlx/releases
- llama.cpp Releases: https://github.com/ggml-org/llama.cpp/releases
- ONNX Runtime Releases: https://github.com/microsoft/onnxruntime/releases
- OpenXLA Releases: https://github.com/openxla/xla/releases
