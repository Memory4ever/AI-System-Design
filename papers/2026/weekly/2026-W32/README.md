# AI Research Weekly — 2026-W32

> Coverage Window: 2026-08-03～2026-08-09（Monday～Sunday）
> Research Mode: Live Daily Aggregation + Coverage-Gap Recovery
> Recovered: 2026-08-11；coverage repair 2026-08-12；blocker recovery 2026-08-13（Asia/Shanghai）
> Validation Status: 2026-08-14 Books review passed；7/7 Daily present；44/44 final dispositions；36 Full Source Reviews complete；3 Unverified / Blocked Identity gaps；0 Review Pending；Source-Family Books Gate Complete under blocked-skip；Archive/Discovery Gate Open

## Executive Summary

本周没有出现足以单独改写全书结构的模型公司发布。长期增量集中在三个跨来源演进链：

1. **局部系统优化走向端到端 deployment accounting**：AFlex 与 HeteroPanacea 把 P/D 进一步
   拆为 Attention/FFN operator，AFD-Ledger 随后补上相同 workload、SLO、预算和 device catalog 下的
   best-vs-best provisioning。新切分不是天然演进终点；state/activation movement、queueing、
   request-bearing-capacity tax、controller recovery 与 near-tie 都可能抵消局部收益。
2. **隐式缓存走向 typed、versioned state**：TokTier 把 tokenizer 增量状态纳入 reference-equivalence
   contract；LiveMem 区分可检索历史与 lossy recurrent state；TARL 把 memory 写入从二元 Write/Hold
   提升为 typed transition。三者处在不同层，不能合并为同一种“长期记忆”。
3. **Agent Workflow 从一次运行走向可编译、可诊断、可复用 artifact**：AtumAI 先把自然语言目标
   编译为 typed task contract；SearchAuditor 把失败后反思拆成 localize→attribute→repair；SkillTrace
   则要求 Skill 具有多轨迹 provenance、确定性审计和人工 review boundary。Agora 的资源研究说明
   workflow shape 也必须进入 runtime resource contract。
4. **MoE routing 的单一 score 开始暴露多重职责**：Beyond Routing 在固定 Top-K dispatch 的受控
   条件下单独校准已执行 expert outputs 的 commitment，提示 selection、execution 与 aggregation
   应作为三个可独立验证的 contract；但短序列、窄 domain 与单一 source 阻止它成为新默认方案。
5. **Agent testing 必须从结果比较走向可定位的行为 contract**：Tangent 把 unit、module、integration、
   API 与 end-to-end 放到同一测试层次中，并暴露 simple input、heavy mocking、浅 assertion 与 NFR
   coverage 的缺口。长期结论不是某个百分比，而是 benchmark、evaluation 与 testing 必须共享 evidence
   identity、同时保留不同的 subject boundary 与 adequacy。

本周从七份 Daily 去重得到 44 个评分 source families：23 项高分、19 项中分、2 项低分。
36 项论文已完成全文阅读和章节联读；KServe v0.20.0 已恢复 official release 与 linked change-family
边界审计，保留为 Version Fact。仅 PrefixPlace、xPress、Resource-Fair Scheduling 三项仍缺可唯一
定位的 primary identifier，不能计为 Full Source Review。8 月 9 日新恢复的 6 项 `20+` candidates 已在 8 月 12 日完成全文审计，
不再保留 `Full Source Review Pending`；Dynamo 与 DeepSpeed 只保留版本边界，Kubernetes RC 与
deception RAG 为低分边界记录。

8 月 9 日 Daily 已从单一 Beyond Routing 扩展为 10 个 scored source families，并完成 9 个 `20+`
source families 的全文审计。8 月 11 日发现的 ElastiCo 与 OasisKV v1 属于 8 月 8 日，现已阅读全文、
评分并定位 Ch59 / Ch46；8 月 8 日 Daily 同步恢复节点。ResKV 与 SLIM 则因 v1 日期为 7 月 31 日，
回拨 W31，不在 W32 重复计分。W32 的 candidate checkpoint 只剩三个 identity gaps；全历史 Gate 仍因
其他周 blocker 与 discovery replay 保持 Open。Tangent 已由 Daily refine Ch62；Weekly 不重复
追加同一结论。

## Coverage Window and Limitations

- 8 月 3～9 日共 7/7 Daily。8 月 9 日先由 8 月 11 日 retrospective discovery 回写 Beyond Routing，
  再于 8 月 12 日补齐 submission-date candidate coverage；Recovery Date 与 access boundary 均显式记录。
- 8 月 3 日为真实 `No Material Update Daily`；其后 arXiv recent batch 才公开周末累积论文，不能
  用 8 月 4 日看到的结果反写 8 月 3 日记录。
- 44 个 unique families 来自 Daily score rows 与恢复候选的 source-family 去重：Architectural Implications of
  Agentic AI Workflows 在 8 月 7 日初筛、8 月 8 日全文复核，只计一次并使用复核后的 29/30；
  KServe 与 Dynamo 的跨日重复也只计一次；SGLang v0.5.16 按 first-public date 回归 W30。
- 36 个 completed paper reviews 的机制、实验与限制以对应 Daily 或本周 recovery packet 的 arXiv HTML
  阅读记录为证据；KServe 只按 official release / linked change boundary 记录，不反推未披露 runtime。
- Tangent、subjective reasoning / RLVR、Business Arena、PIRL、pre-pretraining stability、activation
  steering、carbon-aware fine-tuning 与 AquiLLM 均在 8 月 12 日完成全文；ElastiCo 与 OasisKV 已在
  8 月 13 日完成正文、评分、owner 与 trade-off 核验。
- 所有作者 benchmark 只在论文披露的 model、hardware、precision、workload、batch/concurrency、
  evaluator 与 SLO 条件内成立。Daily 未披露的字段记为 `Not Disclosed`，不由周报补猜。
- Google Scholar、OpenAlex、DBLP、Semantic Scholar 与 Hugging Face 只承担 discovery / metadata；
  技术结论仍回到 primary paper、官方 Release 或代码文档。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Daily coverage | 7 / 7 | 2026-08-09 retrospectively recovered；no missing calendar day |
| Score rows / unique source families | 48 / 44 | 3 cross-day duplicates + 1 W30 spillback removed |
| High / medium / low | 23 / 19 / 2 | ResKV/SLIM moved to W31；ElastiCo/OasisKV added to W32 |
| Full Source Reviews | 36 | 24 Daily reviews + 12 recovered paper reviews |
| Unverified / Blocked Identity Gaps | 3 | PrefixPlace、xPress、Resource-Fair Scheduling lack unique primary identifiers |
| Full Source Review Pending | 0 | 8 月 9 日六项 pending 已完成全文审计 |
| Unscored discovery-only blocked gaps | 0 | ElastiCo + OasisKV recovered and scored |
| Version / low-score boundary records | 3 / 2 | KServe、Dynamo、DeepSpeed / Kubernetes RC、deception RAG |
| W32 Candidate Evidence Checkpoint | Passed with explicit identity gaps | all uniquely identified `20+` papers reviewed；3 identity gaps requested |
| W32 Forward Archive Checkpoint | Passed with explicit blocked ledger | 0 ordinary pending；latest completed ISO week reached；blocked backlog retained for later retry |
| Source-Family Books Gate | Complete under blocked-skip | 36 reviewed papers and prior Daily integrations dispositioned；3 identity gaps receive no mechanism owner |

## 1. 模型与研究机构

### Source Coverage

七份 Daily 按固定顺序覆盖 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google
Research、Meta AI / FAIR、Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、
Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Seed、Baidu ERNIE、Tencent Hunyuan、
Huawei Noah、Shanghai AI Lab、StepFun、Xiaomi MiMo、InclusionAI 与 Hugging Face Blog。

未发现同时满足窗口内首次公开、公开机制与长期 AI System 增量的一线模型机构发布。这是对固定
source list 与已访问 primary index 的覆盖结论，不是对完整互联网的负面证明。

## 2. 论文与学术来源

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TokTier | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Refine Ch11；Full Source Review complete |
| Aries | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | No Change Ch80；Full Source Review complete |
| CAGE | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Emerging / Experimental；Full Source Review complete |
| LiveMem | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine Ch22；Full Source Review complete |
| AtumAI | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine Ch77；Full Source Review complete |
| AFlex | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Emerging / Experimental；Full Source Review complete |
| PrefixPlace | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Unverified / Blocked Backlog |
| xPress | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Unverified / Blocked Backlog |
| Resource-Fair Scheduling | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Unverified / Blocked Backlog |
| TARL | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine Ch73；Full Source Review complete |
| ALiBi numerical underflow | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine Ch13；Full Source Review complete |
| HeteroPanacea | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine Ch51；Full Source Review complete |
| TAOT | 4 | 5 | 4 | 4 | 4 | 3 | 24/30 | Refine `MODEL-MOE`；Full Source Review complete；Experimental |
| Oilbird | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Refine `INFER-SPECULATIVE-DECODING`；Full Source Review complete；Experimental |
| Formal Verification of Agentic Systems | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Refine `PLATFORM-SECURITY`；Full Source Review complete；Experimental |
| AFD-Ledger | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine Ch51；Full Source Review complete |
| The Loss Does Not See the Basis, but Adam Does | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine Ch24；Full Source Review complete |
| Argus | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | No Change Ch77；Full Source Review complete |
| SafeCommit | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine `PLATFORM-SECURITY`；Full Source Review complete；Experimental |
| CommBench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | No Change Ch62；Full Source Review complete；bounded case |
| Architectural Implications of Agentic AI Workflows | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine Ch80；Full Source Review complete |
| Hierarchical Graph Memory | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine `AGENT-MEMORY`；Full Source Review complete；Experimental |
| SearchAuditor | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | Refine Ch76；Full Source Review complete |
| SkillTrace | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Refine Ch80；Full Source Review complete |
| SMRC-SD | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine `TRAIN-GRPO`；Full Source Review complete；Experimental |
| Project2Task | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine `AGENT-PLANNING`；Full Source Review complete；Experimental |
| Search2Skill | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine `AGENT-MEMORY`；Full Source Review complete；Experimental |
| LUNAR personalization benchmark | 3 | 4 | 3 | 4 | 4 | 4 | 22/30 | No Change Ch62；Full Source Review complete；bounded benchmark |
| ElastiCo | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine `PLATFORM-GPU-SCHEDULER`；Full Source Review complete；Experimental |
| OasisKV | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine `INFER-VLLM`；Full Source Review complete；Experimental |
| Beyond Routing / FDAA | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Emerging / Experimental；Full Source Review complete |
| Tangent | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Refine Ch62；Full Source Review complete |
| LLM Reasoning for Subjective Tasks | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | No Change Ch29；Full Source Review complete |
| Business Arena | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Refine `PLATFORM-EVALUATION-SYSTEM`；Full Source Review complete |
| Multimodal RLVR / PIRL | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Refine `TRAIN-GRPO`；Full Source Review complete；Experimental |
| Instability of LLM Pre-Pretraining | 4 | 3 | 4 | 4 | 4 | 5 | 24/30 | No Change Ch24；Full Source Review complete |
| Per-Instance Multi-Layer Activation Steering | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | Emerging Ch5；Full Source Review complete；Experimental |
| Performance–Carbon Break-Even Fine-Tuning | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Emerging Ch66；Full Source Review complete；Ongoing Work |
| AquiLLM | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | No Change Ch72；Full Source Review complete；case architecture |
| Theory-Guided Deception Detection with RAG | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | Low-score boundary；Ignored |

## 3. AI Infra 与工程项目

### Source Coverage

现存 Daily 按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM
→ Ray → KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed → Megatron-LM
→ Unsloth → MLX → llama.cpp → ONNX Runtime → OpenXLA 扫描。普通 patch、continuous build 与
无设计说明的 PR 不计为长期候选。

### Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| KServe v0.20.0 | 3 | 4 | 5 | 5 | 5 | 3 | 25/30 | Weekly Only — Version Fact；official release boundary review complete |
| Dynamo v1.3.1 | 2 | 4 | 4 | 5 | 5 | 3 | 23/30 | Weekly Only — Version Fact |
| DeepSpeed v0.19.4 | 2 | 3 | 4 | 5 | 4 | 2 | 20/30 | Weekly Only — Version Fact |
| Kubernetes v1.37.0-rc.0 | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Pre-release boundary；Ignored |

## Deep Analysis 1 — 从 P/D 拆分到条件化 Execution-Graph Factorization

### Why

Prefill 与 Decode 的计算密度、KV ownership 与 batching 需求不同，因此 P/D disaggregation 在资源
异构、负载稳定且传输可隐藏时合理。随着 Attention 与 FFN 的瓶颈继续分化，operator-level pool
看似能进一步提高利用率，但每新增一条 cut edge 都会增加 activation/state movement、queue、
controller、failure recovery 与 capacity fragmentation。

### Principle and Mechanism

AFlex 把 operator allocation、GPU frequency 与 SLO control 联动；HeteroPanacea 用 P/D/A/F 四池模型
探索更细 factorization；AFD-Ledger 则要求在同一 model、workload、SLO、预算、catalog 与 runtime
contract 下比较完整 provisioning，而不是拿新架构的全局规划对比旧架构的局部 baseline。

```text
co-located serving
→ P/D split
→ conditional A/F split
→ full-fleet provisioning and accounting
→ physical validation under drift and failure
```

### Trade-off, Evidence Boundary and Evolution

三篇作者实验支持“拆分是否值得必须看端到端 break-even”，不证明四池必然优于 P/D 或 co-location。
FFN-only device 若不能直接承载 request，会产生 request-bearing-capacity tax；near-tie 还可能在 trace、
power cap 或 catalog 变化后反转。关系为 `Direct Evolution + Layering`：Ch51 拥有 execution split，
Ch52/59 分别接收 runtime planning 与 cluster-capacity handoff。下一阶段压力是 online calibration、
multi-tenant fairness、controller interaction 与 partial-transfer recovery。

## Deep Analysis 2 — State 的演进不是“保存更多”，而是明确语义和生命周期

### Why

无状态 full tokenization、完整 KV 与 append-only memory 在短请求、充足内存、简单会话中合理；
长会话和长期 Agent 让重复计算、状态淘汰与错误记忆成为一阶问题。直接“缓存更多”却会把
tokenizer revision、lossy compression、provenance、delete、migration 和 tenant isolation 混成一个对象。

### Principle and Mechanism

TokTier 只有在 stable boundary 可证明时复用增量 tokenizer state，并以 full tokenization fallback
维持 reference equivalence。LiveMem 区分 exact / retrievable history 与固定容量 recurrent state：前者
回答“过去发生了什么”，后者只维持计算连续性。TARL 再把 memory write 改为 typed transition，使
append、revise、reject、defer、noop 能够进入 versioned ledger，而不是由一个 boolean label猜测下一状态。

```text
stateless recomputation
→ verified session cache
→ bounded latent continuity + external exact history
→ typed, versioned memory transition
→ governed delete / supersession / rollback
```

### Trade-off, Evidence Boundary and Evolution

更显式的状态改善复用和恢复，却新增 state owner、TTL、revision compatibility、shadow verification、
reset/delete、migration 与 crash replay。LiveMem 的 recurrent state 是有损内部状态，不能越过
authorization boundary 充当事实来源；TARL 的 transaction taxonomy 也不等于数据库 ACID。关系主要为
`Principle Reuse`，主 owner 分别是 Ch11、Ch22、Ch73，不能把三种 state 合并进一个章节。

## Deep Analysis 3 — Agent Workflow 走向可编译、可诊断、可审计的运行对象

### Why

当 Agent 同时调度 CPU、GPU、tools 与外部服务，单个 prompt 或最终 pass/fail 已不能表达系统对象。
如果目标、执行、失败归因和可复用 Skill 都是隐式文本，系统无法判断哪个状态 authoritative、
哪个 repair 可安全 resume、哪个经验可以跨任务复用。

### Principle and Mechanism

AtumAI 在 candidate search 前先生成 typed task contract，分离 hard constraints、evaluation contract 与
deployment authority。SearchAuditor 从 frozen trace 定位 earliest critical step，再做 bounded attribution
和 repair directive；resume 前仍需 reconcile 外部副作用。SkillTrace 把 Skill 定义为带 code/config/
prompt 等 mixed modality、multi-trace provenance 和 deterministic audit 的 artifact。Agora 则把 role、
burst 与 resource-residency shape 暴露给 runtime，避免只按平均 token load 调度。Tangent 补上另一条
不能由 benchmark 代替的路径：test 必须显式拥有 subject boundary、fixture、state transition、oracle、
side effect 与 failure model，才能把失败定位到 workflow 或环境边界。

```text
natural-language goal
→ typed problem contract
→ governed workflow execution
→ localize / attribute / repair
→ audited skill artifact
→ layered unit / interaction / environment tests
→ workflow-visible resource contract
```

### Trade-off, Evidence Boundary and Evolution

更强结构化引入 schema drift、sim-to-real gap、auditor false accept/reject、co-causal failure、artifact
supersession 与 scheduler control-loop interference。论文只证明各自受限环境中的机制，不证明 manager /
planner / reviewer taxonomy 或资源 harvesting 在所有 workload 都成立。主 owner 是 Ch77、76、80；
Tangent 的公开 Python sample 与单机构访谈也不能外推为全部生产实践。测试路径的主 owner 是 Ch62，
Ch69 / Ch77 只接收 release-gate 与 workflow handoff；Ch59 只接收较慢时间尺度的 cluster placement，
不吸收 millisecond workflow state。

## Evidence Level

| Evidence | Boundary |
| --- | --- |
| 36 项 paper Full Source Reviews | 24 项来自原 Daily，12 项由 2026-08-13 recovery packet 完成；作者实验仍为条件性证据 |
| 3 项 blocked identities | PrefixPlace、xPress、Resource-Fair Scheduling 尚无唯一 title / author / identifier；名称不拥有机制结论 |
| KServe v0.20.0 | official signed release、commit 与 linked change list 已核验；只保留版本化工程事实，不外推 production behavior |
| 8 月 9 日 Full Source Review Pending | 0；六项候选已在 Daily 补全，不再以摘要作机制证据 |
| Tangent artifact | 论文已全文阅读；引用的 GitHub repository 在 2026-08-12 访问时为空，artifact 未复现 |
| ElastiCo / OasisKV | v1 first-public date 均归 W32；正文、评分、owner 与 limitations 已核验 |
| Dynamo / DeepSpeed release | 只证明版本事实，不沉淀版本功能表或通用设计结论 |
| Kubernetes RC / deception RAG | 预发布或低分边界记录，不作为稳定实现事实 |

## Full Source Review Recovery — 2026-08-13

### TAOT — 24/30

- **Problem / Mechanism**：routing auxiliary loss 追求统计平衡，却不能保证每个 micro-batch 的 EP rank
  load，也可能削弱 semantic routing。TAOT 不改 router：在冷 rank 的 spare slots 放 hot expert guest
  replicas，以 residual imbalance 与 topology-weighted communication cost 构造 optimal-transport placement，
  再用 topology-aware repair 满足离散容量。runtime owns replica placement；router 仍拥有 token choice。
- **Evidence / Limits**：Qwen3-30B-A3B、Pile-test、4×8 A800，比较 Megatron ECHO、LPLB、LLEP，含
  ablation、sensitivity、planner overhead。证据不覆盖 optimizer migration、故障恢复、多租户或不同
  NVLink/fabric。`router balance → token spill → replica placement with topology cost` 是 layering，不是替代。
- **Owner / Decision**：已读 Ch21、Ch32、Ch35～37；主 owner Ch21，Ch32/36 handoff；
  `Refine — Existing Argument / Experimental`，已写入 `MODEL-MOE`。

### Oilbird — 23/30

- **Problem / Mechanism**：trained drafter 有训练、部署与 compatibility 成本；lexical suffix drafter 无训练，
  但覆盖不了语义相近而 token suffix 不同的历史。Oilbird 复用 verifier 每个 position 已产生的 hidden key，
  从跨请求 store 检索 semantic draft，和 suffix/rejected-branch candidates 合并为同一 verification tree；
  verifier 仍逐 token 决定 commit，保证 greedy equivalence。
- **Evidence / Limits**：Llama-3.1-8B、Qwen3 8/14/32B、BF16、greedy、8 datasets；batch=1 收益明显，
  batch=32 接近或低于 1×。hidden vector 约 8KB/token，最长测试 store 约 2.6GB，retrieval 占 4.8～5.8%
  verification cycle；semantic key 在多数 per-node slice 增量很小。新增 tenant privacy、eviction/index、
  store drift 与 retrieval overhead。
- **Owner / Decision**：已读 Ch41、Ch44、Ch52；主 owner `INFER-SPECULATIVE-DECODING`；
  `Refine — Existing Argument / Experimental`。

### Formal Verification of Agentic Systems — 22/30

- **Problem / Mechanism**：tool-enabled Agent 持续修改 relational operational state，单次 trace test 无法证明
  temporal safety。论文把 deployment 建模为数据库 state-transition system，以 FO-CTL 表达性质；在
  bounded active domain 与 identifier-renaming equivariance 下 quotient 为有限状态并精确 model-check，
  同时给出 PSPACE-complete 与 canonical wrapper / graph-isomorphism complexity 边界。
- **Evidence / Limits**：证明和 case-management example 支持受限形式系统，不证明任意 LLM Agent 可验证。
  假设包括 finite tool semantics、boundedness、equivariance 与可枚举 transition；canonicalization、schema
  evolution、external side effect 和 probabilistic policy 仍是缺口。
- **Owner / Decision**：已读 Ch62、Ch68、Ch77；主 owner `PLATFORM-SECURITY`；
  `Refine — Existing Argument / Experimental`。

### SafeCommit — 24/30

- **Problem / Mechanism**：scalar confidence 不能回答“所有仍可能的 world 中 action 是否都安全”。
  controller 从 memory/observation/tool evidence 构造 conformal plausible-world support；仅当 action 在全部
  retained worlds 中安全才颁发 certificate。无 certified action 时选择低副作用 probe 缩小 support，预算
  用尽后 defer/escalate/abstain；irreversible action 必须先认证。
- **Evidence / Limits**：可复现实验是小型 controlled simulator，含 stale/conflict/poison/auth-drift 四类，
  明确不代表生产量级。需要准确 safety map、可交换 calibration、确定 probe outcome；certificate evaluation
  和 probe scoring 随 world/action/outcome 增长，也不能替代 sandbox、authorization 或 human approval。
- **Owner / Decision**：已读 Ch68、Ch73、Ch77；主 owner `PLATFORM-SECURITY`；
  `Refine — Existing Argument / Experimental`。

### CommBench — 24/30

- **Problem / Mechanism**：能写 CUDA 语法不等于能生成正确且高效的 distributed communication code。
  benchmark 把 100+ tasks 分为 P2P、collective、expert-parallel、comm-compute fusion 与 utility，使用
  compile/correctness/performance harness 在真实 NVLink、RDMA、NVIDIA/AMD 平台验证。
- **Evidence / Limits**：测试覆盖 B300、GH200、MI325X 与 400G fabric；结果说明 library API knowledge、
  algorithmic correctness 与 speed 是不同维度。model ranking 绑定当时模型、prompt、reference、hardware
  和 cheat-resistant harness；不能外推通用 coding capability，也不能把失败全归模型而忽略 library churn。
- **Owner / Decision**：已读 Ch32、Ch62、Ch69；Ch62 已有 executable artifact / workload contract，故
  `No Change — Already Covered`，作为 bounded communication case 保留。

### Hierarchical Graph Memory / HiGram — 23/30

- **Problem / Mechanism**：flat memory accumulation 增加 irrelevant context，局部事实更新又会留下依赖旧
  evidence 的 derived conclusion。HiGram 以 coarse-to-fine graph 连接 MemoryUnits；query/update 构建
  MicroGraph support subgraph，定位 affected evidence path，再联合重写 unit state 与 dependency edge，
  只有仍受有效 evidence 支持的依赖才保留。
- **Evidence / Limits**：LoCoMo 与 MemConflict，F1/BLEU/LLM judge、token length、organization/localization/
  update ablation。offline memory construction 不计 final token cost；没有 production concurrency、source
  provenance、delete、rollback、malicious update 或 human review contract。
- **Owner / Decision**：已读 Ch72～74；主 owner `AGENT-MEMORY`；
  `Refine — Existing Argument / Experimental`。

### SMRC-SD — 24/30

- **Problem / Mechanism**：privileged reference trajectory 即使最终成功，也可能与 student 当前 on-policy
  state 不一致，逐 turn 强蒸馏会教出不可执行 action。SMRC-SD 抽取 structured state signature，把当前
  history 路由到兼容 reference turn，匹配时用 contextual teacher + self-distillation，不匹配时回到 GRPO；
  privileged references 在 inference 移除。
- **Evidence / Limits**：ALFWorld/WebShop，Qwen2.5-3B 与 Qwen3-1.7B，含 routing controls、matcher audit、
  replay、overhead、seed 和 interpretive limits。state adapter/matcher 可能引入 shortcut 或 reference leakage，
  两个 text environment 不证明 browser/robot state 可安全抽象。
- **Owner / Decision**：已读 Ch27～30、Ch77；主 owner `TRAIN-GRPO`；
  `Refine — Existing Argument / Experimental`。

### Project2Task — 24/30

- **Problem / Mechanism**：把 project brief 直接丢给多个 executor 会产生重复、遗漏、依赖冲突和贡献归属
  模糊。planner 抽取 innovation atoms 与 lineage graph，比较 decomposition strategy，生成带 objective、
  boundary、owner、shared asset、dependency、order 的 task contracts，并在 execution feedback 后 repair plan。
- **Evidence / Limits**：10 个 research briefs，以 manuscript portfolio 的 coherence/coverage/overlap/
  consistency/task division 和 AutoResearchClaw downstream task accuracy 评测，五次 judge runs。小样本、
  LLM judge 与 heterogeneous accuracy average 不能证明一般科研质量；planner 也会过约束 executor。
- **Owner / Decision**：已读 Ch75、Ch77、Ch80；主 owner `AGENT-PLANNING`；
  `Refine — Existing Argument / Experimental`。

### Search2Skill — 24/30

- **Problem / Mechanism**：只从自身 trajectory 蒸馏 skill 会受模型知识边界限制；永远 search 又增加成本。
  policy 学习何时 search、query/evidence quality 与何时写 skill，用 rubric rewards 分离 search trigger、search
  quality、skill correctness；训练时外部 search，held-out evaluation 关闭 search、只让 library skill 执行。
- **Evidence / Limits**：Qwen3-4B/8B、五域、8K SFT + 2K GRPO，比较 direct/search agent、ReasoningBank、
  Memp、EvolveR，含 failure taxonomy 和 run variance。仍可能 missed trigger、poor query、format error、
  insufficient coverage、hallucinated skill；没有来源许可、supersession、delete 或 adversarial web 证明。
- **Owner / Decision**：已读 Ch29、Ch72、Ch73、Ch80；主 owner `AGENT-MEMORY`；
  `Refine — Existing Argument / Experimental`。

### LUNAR — 22/30

- **Problem / Mechanism**：personalization benchmark 常只使用 profile 或短 preference，无法测量跨域长期
  behavior log。LUNAR 用 reality-anchored synthetic logs 和 retroductive rubrics，比较 full context、oracle
  curated context、raw-log RAG 与 Mem0 consolidated facts，并从 coverage/depth/privacy 评估 19 个模型。
- **Evidence / Limits**：含 automatic checks、40-sample human validation、position-shuffled pairwise judge；
  synthetic-but-anchored log 不等于真实用户，oracle curated context 不可部署，privacy agreement 也受小样本
  和 judge 限制。它测的是 context/memory harness + model，不是基础模型人格。
- **Owner / Decision**：已读 Ch62、Ch67、Ch73；Ch62 已覆盖 subject/harness/evaluator contract，故
  `No Change — Already Covered`，作为 personalization case。

### ElastiCo — 28/30

- **Problem / Mechanism**：训练/推理各自固定 GPU configuration、再由通用 scheduler placement，无法联合
  利用 elastic mode 与 co-location interference。Resource Specification Template 暴露可选 configuration；
  optimizer 以 shadow price 选择每 job config、bin-pack 并用 predictor 过滤 unsafe colocation，runtime
  把 memory budget 映射到 vLLM/PyTorch/MPS，必要时 drain/checkpoint/migrate。
- **Evidence / Limits**：64×A100-40GB、HDR200/NVSwitch、PyTorch 2.8、vLLM 0.11，8 training + 4 offline
  inference，trace simulation 到 512 GPUs，interference predictor 1,088 samples。只覆盖 single-GPU config
  scope；multi-GPU parallelism/collective、predictor drift、migration failure 与 online SLO 尚未解决。
- **Owner / Decision**：已读 Ch52、Ch59、Ch66；主 owner `PLATFORM-GPU-SCHEDULER`；
  `Refine — Existing Argument / Experimental`。

### OasisKV — 28/30

- **Problem / Mechanism**：long agent decode 的 KV 超出 HBM；把全 cache 每层搬入 GPU 会受 PCIe/network
  bandwidth 限制。OasisKV 把完整 KV 放 pinned CPU 或 remote prefill-side memory，用 sparse attention
  lookahead 预测下一层 block-head，四 stream prefetch/gather/execute/cleanup overlap，只让 working set 常驻
  HBM；P/D 模式用 NIXL/UCX 远端按需抓取并复用 staging state。
- **Evidence / Limits**：vLLM prototype；1/8 H100 80GB、双节点 400GbE RoCE，Qwen3-8B、
  Qwen3-235B-A22B、Llama-3.1-8B，40,960/65,536 context，含 dense/MoE、TP、PD、ablation。结果只在作者
  sparse selector/fetch cap/PCIe/NIC 条件成立；新增 prefetch miss、selection drift、host/remote capacity、
  NUMA、freshness、retry 与 failure-recovery state。
- **Owner / Decision**：已读 Ch41、Ch46、Ch50、Ch51；主 owner `INFER-VLLM`；
  `Refine — Existing Argument / Experimental`。

### KServe v0.20.0 — Version Boundary Review

official signed release 于 2026-08-06，tag commit `1fb7810`。release/linked changes 证明 model-based routing
gates/status、transformer→predictor auth header、multiple OCI sources、EPP shutdown/readiness、GIE v1.5 shim、
Managed DRA、distributed tracing、confidential model serving、RawDeployment canary、llm-d 0.8 等进入该版本；
它们是多个独立 source families 的集合，不证明默认启用、端到端收益或 rollback correctness。最终
`Weekly Only — Version Fact`，Ch57/58 handoff；不是 Books mechanism。

## Cross-Week Deduplication

- TokTier、Aries、CAGE 的 recent-batch visibility 与 event-time handling 保留原记录；ResKV、SLIM 的
  arXiv v1 明确为 7 月 31 日，因此回拨 W31，8 月 4 日只记录 delayed discovery。
- Architectural Implications of Agentic AI Workflows 的 8 月 7 日 metadata watch 与 8 月 8 日 Full Source
  Review 是同一 family；使用 29/30 final score，不重复计数。
- KServe v0.20.0 与 Dynamo v1.3.1 的 8 月 7/8 日记录各合并为一个 release family。
- SGLang v0.5.16 first-public date 为 7 月 25 日，回归 W30；W32 不重复计分。
- Beyond Routing 在 8 月 11 日被发现，但 first-public date 为 8 月 9 日，回写 W32；SwiftQK 与
  QueryProof first-public date 为 8 月 10 日，继续归 W33。
- Tangent、subjective reasoning / RLVR 与其余 8 月 9 日 candidates 均以 arXiv `Submitted on 9 Aug
  2026` 归 W32；8 月 12 日是访问 / recovery date，不是 event date。
- ElastiCo 与 OasisKV first-public date 为 8 月 8 日；已恢复为 W32 scored Full Source Reviews。
- HeteroPanacea、AFlex 与 AFD-Ledger 形成同周演进证据，但不是同一 source family，分别保留。

## Knowledge Tree Position

| Route | Primary owner | Handoff |
| --- | --- | --- |
| verified incremental tokenization | Ch11 | Ch41 / serving session state |
| position and finite-precision contract | Ch13 | Ch45 kernel validation |
| recurrent context continuity | Ch22 | Ch41 / Ch73 |
| optimizer × parameterization symmetry | Ch24 | Ch32 / Ch37 |
| conditional P/D/A/F factorization | Ch51 | Ch52 / Ch59 |
| workflow compilation and authority | Ch77 | Ch62 / Ch80 |
| causal reflection and safe resume | Ch76 | Ch63 / Ch77 |
| typed memory transitions | Ch73 | Ch68 / Ch77 |
| skill and workflow resource contract | Ch80 | Ch59 / Ch77 |
| Agent testing boundary and adequacy | Ch62 | Ch69 / Ch77 |
| subjective reward / reasoning policy | Ch29 | Ch27 / Ch62 |
| MoE dispatch / commitment split | Ch21 | Ch29 / Ch36 / Ch40 |
| long-horizon stateful/counterfactual evaluation | Ch62 | Ch75 / Ch77 / Ch69 |
| prompt-invariant multimodal RLVR | Ch29 | Ch62 / Ch27 |
| pre-pretraining stability | Ch24 | Ch23 / Ch62 |
| per-instance activation steering | Ch5 | Ch25 / Ch62 |
| carbon-aware lifecycle accounting | Ch66 | Ch24 / Ch45 / Ch69 |
| local research RAG / memory workspace | Ch72 | Ch73 / Ch80 |

## Recommended Action

- 保留 8 月 3～9 日七份 Daily，W32 只承担跨日去重与演进重建，不替代 source-level detail。
- 已由 Daily 写入的 Ch11、13、22、24、51、73、76、77、80 结论通过周级联读；Weekly 不重复追加。
- Aries、Argus 判定 `No Change — Already Covered`；CAGE、AFlex 保持 `Emerging / Experimental`。
- Beyond Routing 保持 `Emerging / Experimental`；selection / execution / commitment 分层是潜在 Ch21
  机制缺口，但单一论文与跨域失败不足以改写主线。
- Tangent 的长期测试分层已 refine Ch62；subjective reasoning / RLVR 作为受限案例由 Ch29 既有
  reward-contract 论点覆盖，不重复追加。
- Business Arena 与 PIRL 已分别 refine `PLATFORM-EVALUATION-SYSTEM`、`TRAIN-GRPO`；pre-pretraining
  stability、activation steering、carbon-aware fine-tuning 与 AquiLLM 维持 `No Change` 或 `Emerging`。
- TAOT、Oilbird、Formal Verification、SafeCommit、CommBench、HiGram、SMRC-SD、Project2Task、
  Search2Skill、LUNAR、ElastiCo、OasisKV 已完成全文和章节联读；除已有明确 coverage 的 CommBench/LUNAR，
  其余机制已写入对应 Stable Node，并保留 Experimental 边界。
- PrefixPlace、xPress、Resource-Fair Scheduling 保留为 `Unverified / Blocked Identity`；需要准确标题、
  作者和 arXiv/DOI/official URL 后从零审计，不能沿用简称推断机制。
- KServe v0.20.0 已完成 official release boundary review；保留 Version Fact，不把功能表写入 Books。

## Event-Date Daily Decision

| Date | Daily | Weekly Treatment |
| --- | --- | --- |
| 2026-08-03 | [Daily](../../08/03/README.md) | No Material Update；保留凌晨真实覆盖边界 |
| 2026-08-04 | [Daily](../../08/04/README.md) | TokTier / Aries / CAGE；ResKV / SLIM 后续发现，owner 回拨 W31 |
| 2026-08-05 | [Daily](../../08/05/README.md) | LiveMem / AtumAI / AFlex；3 identity gaps retained |
| 2026-08-06 | [Daily](../../08/06/README.md) | HeteroPanacea / TARL / ALiBi；TAOT / Oilbird / Formal Verification recovered 08-13 |
| 2026-08-07 | [Daily](../../08/07/README.md) | AFD-Ledger / Adam / Argus；SafeCommit / CommBench / HiGram / KServe recovered 08-13 |
| 2026-08-08 | [Daily](../../08/08/README.md) | Agora / SearchAuditor / SkillTrace；SMRC-SD / Project2Task / Search2Skill / LUNAR / ElastiCo / OasisKV recovered 08-13 |
| 2026-08-09 | [Daily](../../08/09/README.md) | 10 scored families；9 `20+` Full Source Reviews；Tangent refine Ch62；0 full reads pending |

## Books Integration Decision

| Candidate Family | Existing / New Coverage | Final Decision | Changed by Daily |
| --- | --- | --- | --- |
| TokTier | Ch11 缺 verified incremental session state | Refine — Existing Argument | `books/part-02-model/11-tokenizer.md` |
| LiveMem | Ch22 缺 context turnover 下的 state continuity | Refine — Existing Argument | `books/part-02-model/22-long-context.md` |
| AtumAI | Ch77 缺 problem compilation / deployment authority split | Refine — Existing Argument | `books/part-07-agent/81-workflow.md` |
| ALiBi numerical underflow | Ch13 缺 formal / finite-precision gap | Refine — Existing Argument | `books/part-02-model/13-position-encoding.md` |
| HeteroPanacea + AFD-Ledger | Ch51 缺 conditional graph split 与 full-provisioning accounting | Refine — Existing Argument | `books/part-05-inference-system/55-pd-disaggregation.md` |
| TARL | Ch73 缺 typed memory transition | Refine — Existing Argument | `books/part-07-agent/77-memory.md` |
| Adam basis dependence | Ch24 缺 optimizer / parameterization joint contract | Refine — Existing Argument | `books/part-04-training-system/28-pretraining.md` |
| SearchAuditor | Ch76 缺 causal localization 与 gated resume | Refine — Existing Argument | `books/part-07-agent/80-reflection.md` |
| Agora + SkillTrace | Ch80 缺 workflow resource shape 与 versioned skill artifact | Refine — Existing Argument | `books/part-07-agent/84-agent-platform.md` |
| Aries / Argus | owner chapter 已具体覆盖 trajectory runtime 与 governed workflow | No Change — Already Covered | — |
| CAGE / AFlex | 单篇受限证据，尚不足以扩大正文 | Emerging / Experimental | — |
| Beyond Routing | Ch21 尚未显式拆 selection / execution / commitment；证据仍窄 | Emerging / Experimental | — |
| Tangent | Ch62 缺 Benchmark / Evaluation / Testing 层次与 Agent test adequacy | Refine — Existing Argument | `books/part-06-ai-infrastructure/66-evaluation-system.md` |
| Subjective reasoning / RLVR | Ch29 已覆盖 outcome reward、credit assignment 与 reward exploitation | No Change — Already Covered / Experimental | — |
| Business Arena / PIRL | stateful counterfactual evaluation / prompt-robustness evidence | Refine — Existing Argument / Experimental | `books/part-06-ai-infrastructure/66-evaluation-system.md`；`books/part-04-training-system/33-grpo.md` |
| Pre-pretraining / activation steering / carbon / AquiLLM | 受限 replication、experimental 或 case evidence | No Change / Emerging | — |
| TAOT / Oilbird | topology placement 与 training-free draft branch 已核验 | Refine — Existing Argument / Experimental | `books/part-02-model/21-moe.md`；`books/part-05-inference-system/48-speculative-decoding.md` |
| Formal Verification / SafeCommit | formal state verification 与 safe commitment certificate 已核验 | Refine — Existing Argument / Experimental | `books/part-06-ai-infrastructure/72-security.md` |
| CommBench / LUNAR | Ch62 已覆盖 executable harness 与 subject/evaluator boundary | No Change — Already Covered | — |
| HiGram / Search2Skill | graph rewrite 与 search-derived skill 已核验 | Refine — Existing Argument / Experimental | `books/part-07-agent/77-memory.md` |
| SMRC-SD / Project2Task | state-matched distillation 与 project-task contract 已核验 | Refine — Existing Argument / Experimental | `books/part-04-training-system/33-grpo.md`；`books/part-07-agent/79-planning.md` |
| ElastiCo / OasisKV | elastic configuration 与 off-HBM KV mechanisms 已核验 | Refine — Existing Argument / Experimental | `books/part-06-ai-infrastructure/63-gpu-scheduler.md`；`books/part-05-inference-system/50-vllm.md` |
| PrefixPlace / xPress / Resource-Fair Scheduling | unique primary identity 未建立 | Unverified / Blocked Identity | — |
| Dynamo / DeepSpeed / Kubernetes | 版本或预发布事实 | Weekly Only / Ignored | — |

本次 Weekly 同步 8 月 9 日 Daily 对 Ch62 的 refine，不重复增加第二份正文。它验证并串联本周 Daily
已完成的章节修改；未改变章节 ownership、84 章结构或旧技术仍成立的边界。

## Final Books Integration Ledger

| Candidate family | Final disposition | Stable owner / concrete reason |
| --- | --- | --- |
| TokTier | Refine — Existing Argument | `MODEL-TOKENIZER`：verified incremental tokenizer state |
| Aries | No Change — Already Covered | `AGENT-PLATFORM` 已有 trajectory runtime ownership |
| CAGE | Emerging / Experimental | recent-batch/event-time 证据窄，不扩大 owner 结论 |
| LiveMem | Refine — Existing Argument | `MODEL-LONG-CONTEXT`：bounded recurrent continuity 与 exact history 分层 |
| AtumAI | Refine — Existing Argument | `AGENT-WORKFLOW`：problem compilation 与 deployment authority 分离 |
| AFlex | Emerging / Experimental | operator/frequency joint control 尚缺跨硬件与故障证据 |
| PrefixPlace | Unverified / Blocked Identity | 缺唯一 primary identifier，不分配机制 owner |
| xPress | Unverified / Blocked Identity | 缺唯一 primary identifier，不分配机制 owner |
| Resource-Fair Scheduling | Unverified / Blocked Identity | 缺唯一 primary identifier，不分配机制 owner |
| TARL | Refine — Existing Argument | `AGENT-MEMORY`：typed memory transition ledger |
| ALiBi numerical underflow | Refine — Existing Argument | `MODEL-POSITION-ENCODING`：formal semantics 与 finite precision 分层 |
| HeteroPanacea | Refine — Existing Argument | `INFER-PD-DISAGGREGATION`：conditional P/D/A/F execution graph |
| TAOT | Refine — Existing Argument / Experimental | `MODEL-MOE`：router choice 与 topology-aware replica placement 分责 |
| Oilbird | Refine — Existing Argument / Experimental | `INFER-SPECULATIVE-DECODING`：verifier-state semantic draft retrieval |
| Formal Verification of Agentic Systems | Refine — Existing Argument / Experimental | `PLATFORM-SECURITY`：bounded transition-system verification |
| AFD-Ledger | Refine — Existing Argument | `INFER-PD-DISAGGREGATION`：full-provisioning accounting contract |
| The Loss Does Not See the Basis, but Adam Does | Refine — Existing Argument | `TRAIN-PRETRAINING`：optimizer 与 parameterization joint identity |
| Argus | No Change — Already Covered | `AGENT-WORKFLOW` 已有 governed durable execution |
| SafeCommit | Refine — Existing Argument / Experimental | `PLATFORM-SECURITY`：plausible-world commit certificate |
| CommBench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` 已有 executable artifact/workload contract |
| Architectural Implications of Agentic AI Workflows | Refine — Existing Argument | `AGENT-PLATFORM`：workflow resource shape 与 lifecycle |
| Hierarchical Graph Memory | Refine — Existing Argument / Experimental | `AGENT-MEMORY`：dependency-localized derived-state update |
| SearchAuditor | Refine — Existing Argument | `AGENT-REFLECTION`：causal localization 与 gated resume |
| SkillTrace | Refine — Existing Argument | `AGENT-PLATFORM`：versioned Skill artifact 与 resource shape |
| SMRC-SD | Refine — Existing Argument / Experimental | `TRAIN-GRPO`：state-matched privileged distillation |
| Project2Task | Refine — Existing Argument / Experimental | `AGENT-PLANNING`：brief-to-task-contract compilation |
| Search2Skill | Refine — Existing Argument / Experimental | `AGENT-MEMORY`：search-derived Skill 的 held-out publish Gate |
| LUNAR personalization benchmark | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` 已有 subject/harness/evaluator identity |
| ElastiCo | Refine — Existing Argument / Experimental | `PLATFORM-GPU-SCHEDULER`：elastic configuration portfolio |
| OasisKV | Refine — Existing Argument / Experimental | `INFER-VLLM`：sparse off-HBM working-set prefetch |
| Beyond Routing / FDAA | Emerging / Experimental | selection/execution/commitment 证据不足以改写 MoE 主线 |
| Tangent | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM`：Benchmark/Evaluation/Testing 分层 |
| LLM Reasoning for Subjective Tasks | No Change — Already Covered | `TRAIN-GRPO` 已有 reward、credit 与 evaluator boundary |
| Business Arena | Refine — Existing Argument / Experimental | `PLATFORM-EVALUATION-SYSTEM`：versioned stateful counterfactual fork |
| Multimodal RLVR / PIRL | Refine — Existing Argument / Experimental | `TRAIN-GRPO`：prompt-mutation robustness 与 hard outcome Gate |
| Instability of LLM Pre-Pretraining | No Change — Already Covered | `TRAIN-PRETRAINING` 已有 optimizer/data/parameterization stability contract |
| Per-Instance Multi-Layer Activation Steering | Emerging / Experimental | 单篇受限干预，不扩展 `WORLDVIEW-WHAT-NN-LEARN` |
| Performance–Carbon Break-Even Fine-Tuning | Emerging / Experimental | 案例依赖 hardware/accounting assumptions，不改成本主线 |
| AquiLLM | No Change — Already Covered | `PLATFORM-SECURITY` 已有 policy sensor/authority/reconciliation 分层 |
| Theory-Guided Deception Detection with RAG | Weekly Only / Low-score Boundary | 18/30，不形成长期机制 |
| KServe v0.20.0 | Weekly Only — Version Fact | release family，不把功能表推断为统一机制 |
| Dynamo v1.3.1 | Weekly Only — Version Fact | patch release 事实 |
| DeepSpeed v0.19.4 | Weekly Only — Version Fact | release 事实 |
| Kubernetes v1.37.0-rc.0 | Weekly Only / Pre-release Boundary | 18/30 RC，不进入长期正文 |

Ledger check：44/44；24 Refine、7 No Change、5 Emerging、3 Unverified / Blocked Identity、
3 Weekly Only Version Facts、2 low-score / pre-release boundary records；0 Review Pending。

## Ignored Noise

- 把 SGLang v0.5.16 或其他旧 release 在本周的重复索引当成新事件。
- 把 arXiv list / Hugging Face 排名、upvote 或搜索摘要当作 paper mechanism evidence。
- 缺少完整 workload contract 的 speedup、cost、tokens/s 或 energy headline。
- 从 KServe release name 推断未公开 controller、routing 或 rollback 实现。
- 把回填前的 6/7 Daily 状态继续当作当前事实，或把 retrospective recovery 伪装成当日实时抓取。

## Repository Changes

- 新增 `papers/2026/weekly/2026-W32/README.md`，恢复完整 ISO window 的 Weekly archive。
- 2026-08-13 明确记录 7/7 Daily、44 个 unique scored families、36 个 paper Full Source Reviews、3 个
  blocked identity gaps、0 个 Full Source Review Pending、0 个 unscored discovery gaps、3 个 version-boundary records
  与 2 个 low-score boundary records。
- 2026-08-14 完成 44/44 final ledger；将 TAOT、Oilbird、Formal Verification、SafeCommit、HiGram、
  Search2Skill、SMRC-SD、PIRL、Project2Task、ElastiCo、OasisKV、Business Arena 的长期机制写入九个现有
  Stable Node；未新增或重编号章节。
- 同步年度 Weekly index 与 Learning State；ROADMAP 与 DECISIONS 不变。未执行 stage、commit、push 或破坏性 Git。

## Open Questions

1. PrefixPlace、xPress、Resource-Fair Scheduling 的准确标题、作者、arXiv/DOI 或 official URL 是什么？
2. P/D/A/F planner 在 workload drift、failure recovery、multi-tenant fairness 与 controller interaction 下的
   break-even 是否可由公开 artifact 复现？
3. Tokenizer、recurrent state 与 durable memory 的 revision / delete / migration contract 应如何在
   serving session 与 Agent identity 之间传递而不混淆 authority？
4. SearchAuditor 的 frozen-trace、single-cause assumption 如何扩展到外部副作用与 co-causal failures？
5. KServe v0.20.0 的多个 versioned changes 在 rollback / multi-controller failure 中分别由谁拥有，
   哪些已有独立设计文档和故障注入证据？
6. 三个 identity gaps 建立唯一来源后，是重复证据还是新的 locality/speculation/fairness 演进分支？
7. Business Arena 的 fork identity 与 PIRL 的 prompt mutation 在跨 runtime、跨 domain 复现后，是否仍支持
   当前 Experimental owner boundary？
8. Tangent 的 artifact repository 何时补齐，当前 taxonomy 与统计能否独立重建？

## Sources

完整 source-level 阅读范围、实验条件和限制见对应 Daily；下列均为 primary source 或官方 release。

### Papers — Full Source Reviews Completed

- TokTier: https://arxiv.org/abs/2607.29678
- Aries: https://arxiv.org/abs/2607.29069
- CAGE: https://arxiv.org/abs/2607.29190
- LiveMem: https://arxiv.org/abs/2608.02515
- AtumAI: https://arxiv.org/abs/2608.02569
- AFlex: https://arxiv.org/abs/2608.01891
- HeteroPanacea: https://arxiv.org/abs/2608.03741
- TARL: https://arxiv.org/abs/2608.03699
- When Attention Goes Blind / ALiBi numerical failure: https://arxiv.org/abs/2608.03994
- AFD-Ledger: https://arxiv.org/abs/2608.04502
- The Loss Does Not See the Basis, but Adam Does: https://arxiv.org/abs/2608.05136
- Argus: https://arxiv.org/abs/2608.05144
- Architectural Implications of Agentic AI Workflows: https://arxiv.org/abs/2608.04458
- SearchAuditor: https://arxiv.org/abs/2608.05212
- SkillTrace: https://arxiv.org/abs/2608.05204
- Beyond Routing / FDAA: https://arxiv.org/abs/2608.08853
- Tangent: https://arxiv.org/abs/2608.08413
- LLM Reasoning for Subjective Tasks: https://arxiv.org/abs/2608.08889
- TAOT: https://arxiv.org/abs/2608.03676
- Oilbird: https://arxiv.org/abs/2608.03839
- Formal Verification of Agentic Systems: https://arxiv.org/abs/2608.03609
- SafeCommit: https://arxiv.org/abs/2608.04289
- CommBench: https://arxiv.org/abs/2608.04450
- Hierarchical Graph Memory: https://arxiv.org/abs/2608.05095
- SMRC-SD: https://arxiv.org/abs/2608.05219
- Project2Task: https://arxiv.org/abs/2608.05225
- Search2Skill: https://arxiv.org/abs/2608.05245
- LUNAR: https://arxiv.org/abs/2608.05246
- ElastiCo: https://arxiv.org/abs/2608.07971
- OasisKV: https://arxiv.org/abs/2608.08097

Tangent 正文引用的 artifact repository 在 2026-08-12 访问时为空：
https://github.com/aster-test-generation/tangent-ase-2026

### Papers — Unverified / Blocked Backlog

- PrefixPlace、xPress、Resource-Fair Scheduling：2026-08-05 Daily 未保留可追溯 primary URL；
  存在 provenance / identity gap，因此维持 `Unverified / Blocked Identity`。

### Papers — Full Source Reviews Completed on 2026-08-12

- Business Arena: https://arxiv.org/abs/2608.08621
- Improving Generalization Robustness of Multimodal RLVR: https://arxiv.org/abs/2608.08802
- Instability of LLM Pre-Pretraining: https://arxiv.org/abs/2608.08800
- Deployable Per-Instance Multi-Layer Activation Steering: https://arxiv.org/abs/2608.08829
- Performance–Carbon Break-Even Fine-Tuning: https://arxiv.org/abs/2608.08744
- AquiLLM: https://arxiv.org/abs/2608.08883

### Low-score Boundary

- Theory-Guided Deception Detection with RAG: https://arxiv.org/abs/2608.08881

### Engineering

- KServe v0.20.0: https://github.com/kserve/kserve/releases/tag/v0.20.0
- NVIDIA Dynamo v1.3.1: https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.1
- DeepSpeed releases: https://github.com/deepspeedai/DeepSpeed/releases
- Kubernetes releases: https://github.com/kubernetes/kubernetes/releases
