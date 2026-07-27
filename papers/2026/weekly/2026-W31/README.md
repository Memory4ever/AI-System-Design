# AI Research Weekly — 2026-W31

> Coverage Window: 2026-07-27～2026-08-02（Monday～Sunday）
> Research Mode: Live Daily Aggregation + Cross-Day Re-evaluation
> Accessed: 2026-08-02（Asia/Shanghai）
> Validation Status: 2026-08-14 Books review passed; 7/7 Daily present; 26/26 final dispositions；ResKV / SLIM Full Source Reviews complete；Source-Family Books Gate Complete；Archive/Discovery Gate Open

## Executive Summary

本周的稳定信号不是某个模型排名，而是三个系统对象同时从隐式状态走向可验证 contract：

1. **Inference state** 从 exact prefix KV 扩展到 tiered、position-independent 和 attention-state
   injection；复用不再只是地址命中，还需要 semantic identity、ownership、version 与 invalidation。
2. **Evaluation evidence** 从 run-level artifact 扩展到 claim-level provenance；能重放程序仍不
   等于报告中的每个数字、方法和结论都有证据支持。
3. **Agent runtime state** 从 connection-bound session 扩展到 explicit handle、durable workflow
   与 bounded topology repair；协议、workflow 和 authority 仍是不同层。

Daily 已分别吸收 Kimi K3、vLLM KV tiering、MCP stable、RARG、CodeNib、noisy reward、
MemSecBench、lossy verification、SemPIC、OSReward 与 MANTA 的长期机制。本周新增的 Books
refinement 仅有一项：ScientistOne / Chain-of-Evidence 补足第 62 章的 claim-level provenance。
其论文 v1 首次公开于 5 月 25 日，本周事件是 7 月 30 日 Google Research 官方解释，不能
被写成新论文。

2026-08-13 的全量归属复核又纠正两项 curation-lag：ResKV 与 SLIM 的 arXiv v1 均首次公开于
7 月 31 日，真实 owner 是 W31，而不是 8 月 4 日发现它们的 W32。两篇正文、Appendix、实验和限制
现已完成 Full Source Review；8 月 4 日 Daily 保留为“后续发现 / 审计节点”，但不拥有事件计分。

## Coverage Window and Limitations

- 七份 Live Daily 均存在：7 月 27～31 日与 8 月 1～2 日，无缺失自然日。
- 7 月 27 日 Daily 含 HiKV、Ground Truth First、SGLang v0.5.16 等 W30 事件；本周按
  first-public / release date 去重，不再次计分为 W31 新事件。
- Google Research 7 月 30 日 ScientistOne 官方文章和 Anthropic 7 月 28 日密码分析研究未在
  对应 Daily 保留。本周显式记录此 coverage gap；不静默省略，也不伪造历史 Daily。
- ResKV、SLIM 的 v1 timestamp 均为 2026-07-31；它们在 8 月 4 日 Daily 才被发现。Weekly 按
  first-public date 回拨 W31，使用 8 月 13 日可访问正文完成审计，不伪造 7 月 31 日 Daily。
- ScientistOne 论文、方法、实验、限制及关键 Appendix 已复核；作者的 75-paper benchmark
  只支持其具体任务与适配条件，不能外推为“自主科研已达到人类水平”。
- Anthropic 密码分析两项结果只依据官方研究说明和其公开 source family 定界；关联密码学
  论文尚未逐篇完成领域级复核，因此为 `Weekly Only / 尚未验证完整机制`。
- Google Scholar、OpenAlex、DBLP、Semantic Scholar 用于发现与去重；Crossref 用于 metadata
  交叉检查。机制结论回到论文、官方规范、Release 和代码文档。

六维均为 0～5：Technical Novelty、System Impact、Practical Value、Source Reliability、
Project Relevance、Longevity。

## 1. 模型与研究机构

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ScientistOne official publication node | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine Ch62；paper v1 属于 W22 |
| Kimi K3 Technical Report | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine Ch21，Daily 已完成 |
| Anthropic cryptanalysis with Claude | 3 | 4 | 3 | 4 | 4 | 4 | 22/30 | Weekly Only；机制核验未闭合 |
| Qwen-UI-Agent | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Experimental；Daily only |
| OpenAI task-crossover study | 1 | 2 | 2 | 5 | 1 | 2 | 13/30 | Record Only |

## 2. 论文与学术来源

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SemPIC | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine Ch46，Daily 已完成 |
| OSReward | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine Ch62，Daily 已完成 |
| InferScale | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Experimental；Weekly only |
| RARG | 5 | 4 | 4 | 3 | 5 | 5 | 26/30 | Refine Ch72，Daily 已完成 |
| CodeNib | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Refine Ch71，Daily 已完成 |
| RL for Code Optimization | 4 | 5 | 4 | 3 | 5 | 5 | 26/30 | Refine Ch29，Daily 已完成 |
| MemSecBench | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine Ch73，Daily 已完成 |
| MANTA | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine Ch78，Daily 已完成 |
| Revisiting Lossy Verification | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine Ch44，Daily 已完成 |
| WIDE | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching；Daily only |
| Computer-use benchmark audit | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Related evidence；Daily only |
| Filesystem-Based Memory | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Worth Watching；Daily only |
| Shieldstral | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching；Daily only |
| SpecBox | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Worth Watching；Daily only |
| Local CUA inference-time scaling | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Worth Watching；Daily only |
| ResKV | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine `INFER-KV-CACHE`；Full Source Review complete；Experimental |
| SLIM | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine `INFER-SCHEDULING`；Full Source Review complete；Experimental |

## Full Source Review Recovery — 2026-08-13

### ResKV — 24/30

- **Source / Date / Coverage**：`RESKV-FIXED-BUDGET-RESIDUAL-CACHE`；arXiv:2607.29591 v1，
  2026-07-31。已读 theory、construction/decode algorithm、LongBench/RULER setup、baseline、ablation、
  memory/throughput、implementation 与 limitations。
- **Problem / Previous Design**：hard eviction 保留少量 exact KV，但连同被删 token 的 attention
  numerator 与 denominator mass 一并丢失；merge 能保留更多信息，却会污染本应 exact 的 retained
  entries。二者在 tight fixed budget 下分别偏向“丢失”和“篡改”。
- **Mechanism / State Flow**：总预算固定为 `b=m+r`。main cache 保存 exact token；每 layer / KV head
  对 omitted keys 做少量 Lloyd clustering，residual entry 保存 representative K/V 与 population count。
  decode 时 main/residual 进入同一个 softmax，`log count` 恢复聚合质量，dynamic gate 在主注意力尖锐时
  抑制 residual。压缩在 prefill 后构建一次；cache manager 拥有 main/residual layout 与 gate metadata。
- **Evaluation / Boundary**：LongBench、RULER 的 4K/32K，Llama-3.1-8B-Instruct 与
  Qwen2.5-7B-Instruct，compression ratio 0.6～0.9；实现基于 PyTorch/Transformers/FlashAttention-2，
  单 A100 40GB、seed 42。证据支持作者两种 backbone、单请求条件下相同 slot budget 的质量保留；
  不证明大 batch、多租户、continuous batching 或 production SLO 下仍有净收益。
- **Trade-off / Evolution**：`exact full cache → hard eviction → merge → exact main + approximate residual`。
  新增 clustering/gate 成本、query-distribution mismatch、generation 期间 residual stale、kernel complexity；
  论文也未实现长期生成中的 residual refresh。sharp retrieval 或极低 overhead 场景仍可使用 hard eviction。
- **ROADMAP / Disposition**：已读 Ch22、Ch41、Ch43、Ch46；主 owner Ch41，Ch22/46 只作长上下文与
  serving handoff。`Refine — Existing Argument / Status: Experimental`，已写入 `INFER-KV-CACHE`。

### SLIM — 24/30

- **Source / Date / Coverage**：`SLIM-SATURATION-AWARE-SERVING-MODEL`；arXiv:2607.29575 v1，
  2026-07-31。已读 analytical model、calibration、batch-configuration algorithm、2/4-GPU validation、
  sensitivity、overhead 与 limitations。
- **Problem / Previous Design**：roofline/linear latency model 在未饱和区间有用，但 decode 的 active
  context memory traffic 会随 batch、input/output length 增长并进入 bandwidth saturation；继续线性外推
  会错误选择 batch、TP 与 replica 配置。profile-everything 更准确，却无法低成本覆盖大配置空间。
- **Mechanism / Ownership**：SLIM 把 prefill compute、decode dense compute 与 attention memory traffic
  分开建模，以 saturation-aware term 表示 active-context bandwidth ceiling，再由少量 calibration points
  拟合硬件/模型常数。SLIM-BCA 用模型枚举满足 memory/SLO 的 batch configuration；runtime profiler
  拥有 calibration，capacity planner 拥有配置决策，online scheduler 仍拥有 admission/queue。
- **Evaluation / Boundary**：Qwen 32B/72B、2/4 张 H100 的受控服务配置；论文报告对未见 batch/
  sequence/parallelism configuration 的 latency 和吞吐预测，并与经验 profiling baseline 比较。模型在部分
  setting 仍高估差距，TP communication 在作者范围内不是主瓶颈；这些结果不能外推到 MoE、异构 GPU、
  network-heavy P/D、量化 kernel 或 multi-tenant interference。
- **Trade-off / Evolution**：`single-point profile → linear/roofline estimate → saturation-aware model →
  online calibrated capacity control`。轻量模型减少 profile cost，却新增 calibration drift、model-form bias、
  near-boundary SLO error 和 planner/scheduler control-loop interaction。变化快或 tail-latency 主导时，旧的
  empirical profiling/canary 仍不可替代。
- **ROADMAP / Disposition**：已读 Ch45、Ch50、Ch52、Ch66；主 owner Ch52，Ch66 只接收 capacity/
  cost handoff。`Refine — Existing Argument / Status: Experimental`，已写入 `INFER-SCHEDULING`。

## 3. AI Infra 与工程项目

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MCP `2026-07-28` stable | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Refine Ch79，Daily 已完成 |
| vLLM `v0.26.0` KV tiering | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Refine Ch46，Daily 已完成 |
| Dynamo Kimi K3 dev snapshot | 2 | 3 | 2 | 5 | 4 | 2 | 18/30 | Record Only |
| llama.cpp daily builds | 2 | 2 | 3 | 5 | 3 | 2 | 17/30 | Record Only |

## Deep Analysis 1 — 从 Run Evidence 到 Claim-level Provenance

### Why

传统 Evaluation 保存 model、dataset、environment、log 和 score，回答“这次 run 发生了什么”。
长 Agent workflow 还需要回答“最终文本中的这条 claim 究竟由哪个 artifact 支持”。生成和验证
若在最后才相遇，错误会沿 literature → hypothesis → experiment → paper 被一致地放大。

### Principle

证据完整性必须是写作时的约束，而不是发布后的装饰：

```text
typed claim
→ declared source artifact
→ claim-specific verifier
→ supported / partial / unsupported
→ rewrite, reject or publish
```

### Mechanism

ScientistOne 先把检索材料、代码、实验日志、分数与 ablation 组织为带 evidence tag 的中间
表示，再执行 deterministic Ground、LLM Critic、Resolve、Compose 与 Claim Verifier。后验
CoE Audit 分别检查 score reproduction、specification violation、reference existence 与
method–code alignment。状态 owner 不是最终 prose，而是 versioned artifact graph 与 verdict。

### Trade-off

更细 provenance 增加 schema、storage、verification latency、source retention 与 supersession
成本。Reference 存在不等于支持 claim；model judge 仍有 false negative；结构完整也不证明
科学新颖性和正确性。论文 baseline 经过 ADRS 适配，开放科学领域没有同样确定的 evaluator。

### Connection and Evolution

主 owner 为 Ch62，Ch77 只负责 Workflow 中证据的产生和 durable transition：

```text
run/artifact retention
→ reproducible execution
→ typed claim provenance
→ pre-publication integrity gate
→ domain expert review for non-automatable claims
```

关系为 `Layering / Dependency`，没有用 CoE 覆盖既有 evaluation run contract。

## Deep Analysis 2 — KV 复用从字节命中演化为语义兼容

### Why

Exact prefix reuse 适合相同 token 序列；长文档、多租户与 Agent memory 使可复用内容经常位于
不同 position，甚至以 attention state 而非原始 token 出现。单一 HBM allocator 无法表达
device、host、object store、semantic compilation 与 online repair 的不同生命周期。

### Principle and Mechanism

```text
token injection
→ exact-prefix KV reuse
→ tiered KV transfer
→ position-independent semantic linking
→ online attention-state repair / offline semantic compilation
```

vLLM `v0.26.0` 把 cache 越过 device boundary 后的 identity、replica ownership、credential
和 observability 变成数据面协议。SemPIC 预先生成 position-independent KV，并在 Reader 侧
通过 linking mechanism 组合；InferScale 则把离线记忆转成可注入 attention state，并在运行时
修复。三者不是线性替代，而是不同 latency、freshness 与 model-coupling 分支。

### Trade-off, Connection and Evolution

复用命中率提高的代价是 cache identity 必须包含 model/revision、tokenizer、position policy、
adapter、quantization 与 writer/reader compatibility；还新增 rebuild、invalidation、rollback、
tenant isolation 和 remote-transfer SLO。Ch46 已拥有 semantic composition contract；InferScale
仍为 `Experimental`，未因 Weekly 合并而扩大正文结论。

## Deep Analysis 3 — Agent 状态从 Session 走向显式 Handle 与受限修复

### Why and Principle

连接绑定 session 在单进程、长连接下合理；gateway、短连接、弹性扩缩和长任务使 transport
lifecycle 不再等于业务 lifecycle。稳定方向是让 identity 与 state ownership 显式化，同时
保持 authority 在 Workflow / policy 层。

### Mechanism

MCP stable 以 per-request version/capability negotiation、`server/discover` 与 explicit state
handle 取代协议隐含 session。MANTA 则在 multi-agent runtime 中以 trace signal 触发 bounded
topology repair。MemSecBench 从另一侧说明持久 memory 的 poisoning、propagation、detection、
repair 和 benign-state preservation 必须作为完整 lifecycle 测量。

### Trade-off, Connection and Evolution

显式 handle 改善负载均衡和恢复，却新增 handle TTL、authorization、revocation 与 orphan
cleanup；动态 topology 改善局部失效，却新增 mutation race、authority transfer、replay 与
side-effect ambiguity。Ch79、Ch78、Ch73 分别拥有协议、拓扑与 memory contract，Ch77 负责
durable business state；Weekly 不把这些状态合并为一个“Agent session”。

## Evidence Level

| Evidence | Boundary |
| --- | --- |
| Official stable specification / signed release | 可证明版本和公开 contract；不证明所有 SDK、server fleet 已迁移 |
| Official Research + full paper | 可证明作者方法、实验与限制；作者 benchmark 仍是条件性证据 |
| arXiv v1 + accessible full text | 可沉淀机制与开放问题；独立复现和 production integration 未成立 |
| Dev snapshot / continuous build | 只证明版本事实；不升级为稳定架构结论 |
| Discovery index / community signal | 只用于发现，不作为 claim evidence |

## Cross-Week Deduplication

- HiKV、Ground Truth First、Native Multimodal、SGLang v0.5.16 与 Nunchaku 的真实事件日期属于
  W30；7 月 27 日 Daily 是复核节点，不在 W31 重复计分。
- Kimi K3 launch 已在 W29；W31 保留 7 月 27 日 technical report 作为 source-family evidence
  update，不把它写成第二次模型发布。
- ScientistOne paper v1 属于 W22（2026-05-25）；W31 只记录 7 月 30 日 Google Research
  official publication node，并明确补齐此前未覆盖的 source family。
- MCP 7 月 28 日 RC 与同日 stable 是一个 source family；Weekly 以 stable 为最终事件，RC 只
  解释演进过程。
- ResKV 与 SLIM 的 v1 均为 7 月 31 日；8 月 4 日只是 delayed discovery。两项回拨 W31 并从 W32
  score ledger 删除，避免按发现日重复计分。

## Knowledge Tree Position

| Route | Primary owner | Handoff |
| --- | --- | --- |
| Router objective → executable dispatch | Ch21 | Ch32/48 |
| Reward as measurement interface | Ch29 | Ch62 |
| Speculative sampling contract | Ch44 | Ch20/52 |
| Tiered / semantic KV state | Ch46 | Ch41/50/51 |
| Claim-level evidence | Ch62 | Ch77/80 |
| Context derived views / interaction prior | Ch71/72 | Ch65/77 |
| Memory poisoning lifecycle | Ch73 | Ch68/77 |
| Runtime topology repair | Ch78 | Ch77 |
| Explicit protocol state | Ch79 | Ch77/80 |
| fixed-budget residual KV | Ch41 | Ch22/46 |
| saturation-aware performance model | Ch52 | Ch45/50/66 |

## Recommended Action

- 保留本周全部七份 Daily；Weekly 不替代 source-level detail。
- ScientistOne 作为 `Status: Experimental` 的 claim-evidence 案例进入 Ch62；继续观察 artifact、
  independent reproduction 与开放领域 verifier。
- InferScale、Qwen-UI-Agent、WIDE、SpecBox、Shieldstral 继续 Daily / Weekly only，等待代码、
  source-family 补全或独立复现。
- Anthropic cryptanalysis 在两篇技术论文完成领域级全文复核前不得升级为模型固有能力结论。
- ResKV、SLIM 已完成全文审计，分别 refine `INFER-KV-CACHE` 与 `INFER-SCHEDULING`；正文只吸收
  main/residual state split 与 saturation-aware calibration/control，不外推单 A100 或少量 H100 结果。

## Event-Date Daily Decision

| Date | Daily | Weekly treatment |
| --- | --- | --- |
| 2026-07-27 | [Daily](../../07/27/README.md) | W30 内容跨周去重；窗口内 source-family update 保留 |
| 2026-07-28 | [Daily](../../07/28/README.md) | MCP RC → stable 合并；Anthropic 漏项在 Weekly 标明 |
| 2026-07-29 | [Daily](../../07/29/README.md) | Kimi K3 report、vLLM、MCP stable 主记录 |
| 2026-07-30 | [Daily](../../07/30/README.md) | 三篇 paper 主记录；ScientistOne official 漏项在 Weekly 补齐 |
| 2026-07-31 | [Daily](../../07/31/README.md) | KV injection、memory security、lossy verification |
| 2026-08-01 | [Daily](../../08/01/README.md) | semantic KV、trajectory judge、topology repair |
| 2026-08-02 | [Daily](../../08/02/README.md) | No Material Update；完成 Sunday cross-day audit |

## Books Integration Decision

| Candidate family | Existing coverage | Final decision | Changed file |
| --- | --- | --- | --- |
| ScientistOne / CoE | Ch62 已有 run evidence，缺 claim-to-artifact mapping | Refine — Existing Argument | `books/part-06-ai-infrastructure/66-evaluation-system.md` |
| Kimi K3 / vLLM / MCP | Daily 已完成 owner chapter 写入 | No duplicate Weekly prose | — |
| RARG / CodeNib / noisy reward | Daily 已完成 Ch72/71/29 | No duplicate Weekly prose | — |
| MemSecBench / lossy verification | Daily 已完成 Ch73/44 | No duplicate Weekly prose | — |
| SemPIC / OSReward / MANTA | Daily 已完成 Ch46/62/78 | No duplicate Weekly prose | — |
| InferScale / Qwen / WIDE / SpecBox / Shieldstral | 单篇或 source-family 尚不足 | Experimental / Weekly only | — |
| Anthropic cryptanalysis | 结果受限且领域级论文核验未闭合 | Unverified mechanism / Weekly only | — |
| ResKV | Ch45 已有 eviction/merge/quantization，缺 main-residual shared-softmax 分支 | Refine — Existing Argument / Experimental | `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` |
| SLIM | Ch56 已有 profiling/control，缺 saturation-aware lightweight modeling 分支 | Refine — Existing Argument / Experimental | `books/part-05-inference-system/56-inference-scheduling.md` |

本周新增内容补全了证据粒度，没有改变既有设计结论、章节 ownership 或 84 章结构。

## Final Books Integration Ledger

| Candidate family | Final disposition | Stable owner / concrete reason |
| --- | --- | --- |
| ScientistOne official publication node | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM`：claim-to-artifact provenance |
| Kimi K3 Technical Report | Refine — Existing Argument | `MODEL-MOE`：router objective 与 executable dispatch 已由 Daily 写入 |
| Anthropic cryptanalysis with Claude | Weekly Only | 领域论文核验未闭合，不推断模型固有机制 |
| Qwen-UI-Agent | No Change — Already Covered | `AGENT-PLATFORM` 已有 environment/action/workflow/authority contract |
| OpenAI task-crossover study | Weekly Only | 13/30 边界记录，不形成系统机制 |
| SemPIC | Refine — Existing Argument | `INFER-VLLM`：position-independent semantic KV composition |
| OSReward | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM`：可执行 outcome contract |
| InferScale | Weekly Only | attention-state injection 为受限实验，owner 机制证据不足 |
| RARG | Refine — Existing Argument | `AGENT-RAG`：retrieval 与生成控制联合状态 |
| CodeNib | Refine — Existing Argument | `AGENT-CONTEXT`：repository-derived Context state |
| RL for Code Optimization | Refine — Existing Argument | `TRAIN-GRPO`：reward/verification 与 update identity |
| MemSecBench | Refine — Existing Argument | `AGENT-MEMORY`：poisoning、传播、检测与修复 lifecycle |
| MANTA | Refine — Existing Argument | `AGENT-MULTI-AGENT`：bounded topology repair |
| Revisiting Lossy Verification | Refine — Existing Argument | `INFER-SPECULATIVE-DECODING`：lossy verifier 的 acceptance boundary |
| WIDE | No Change — Already Covered | `MODEL-MOE` / `INFER-EXECUTION` 已有 conditional compute 与 kernel/scheduling contract |
| Computer-use benchmark audit | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` 已区分 harness、environment 与 model subject |
| Filesystem-Based Memory | No Change — Already Covered | `AGENT-MEMORY` 已有 derived view、provenance 与 durable state 边界 |
| Shieldstral | No Change — Already Covered | `PLATFORM-SECURITY` / `PLATFORM-EVALUATION-SYSTEM` 已有 policy taxonomy 与 operating point |
| SpecBox | No Change — Already Covered | `AGENT-PLATFORM` 已有 sandbox pool、credential 与 isolation lifecycle |
| Local CUA inference-time scaling | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` / `AGENT-REFLECTION` 已有 bounded retry、verification 与 cost |
| ResKV | Refine — Existing Argument / Experimental | `INFER-KV-CACHE`：exact main + approximate residual |
| SLIM | Refine — Existing Argument / Experimental | `INFER-SCHEDULING`：saturation-aware calibrated capacity model |
| MCP `2026-07-28` stable | Refine — Existing Argument | `AGENT-MCP`：explicit handle 与 capability negotiation |
| vLLM `v0.26.0` KV tiering | Refine — Existing Argument | `INFER-VLLM`：typed tier identity 与 transfer ownership |
| Dynamo Kimi K3 dev snapshot | Weekly Only | development snapshot，只保留版本事实 |
| llama.cpp daily builds | Weekly Only | continuous build，不形成稳定设计结论 |

Ledger check：26/26；14 Refine、7 No Change、5 Weekly Only；0 Pending、0 Blocked、0 Disputed。

## Ignored Noise

- 模型榜单、媒体转载、社交热度和没有 system/model card 的产品宣传。
- 把论文 revision、官方 Blog 解释或 Daily 复核日期误作首次公开日期。
- 缺少 workload contract 的 speedup、energy、tokens/s 与成本 headline。
- GitHub continuous build、普通 patch、dependency bump 与未合并 PR。
- 从密码分析结果反推未公开的模型训练、harness 或通用 autonomy 机制。

## Repository Changes

- 新增 `papers/2026/weekly/2026-W31/README.md`。
- Refine `books/part-06-ai-infrastructure/66-evaluation-system.md`，加入 claim-level provenance。
- 更新 `papers/2026/weekly/README.md` 与 `docs/LEARNING_STATE.md` 的 Live Weekly coverage。
- 2026-08-13 将 ResKV、SLIM 按 first-public date 从 W32 回拨 W31，新增两项 Full Source Review。
- 2026-08-14 将 ResKV 与 SLIM 的长期机制分别写入 Ch45、Ch56，并完成 26/26 final ledger。
- 今日 Daily 见 `papers/2026/08/02/README.md`。
- 未新增 Part / chapter，未修改 ROADMAP / DECISIONS，未执行 stage、commit、push 或破坏性 Git。

## Open Questions

1. Claim evidence 的 source revision、删除、代码重构与 supersession 应如何触发下游失效？
2. 没有 deterministic evaluator 的科研、政策和开放式任务，哪些 claim 只能由领域专家验证？
3. Semantic KV 的 writer/reader compatibility 应怎样进入 cache key、rebuild evidence 与 SLO？
4. Explicit handle 和 topology mutation 在 crash/replay、delegated credential 与外部副作用下如何
   保持可审计、近似 exactly-once 的业务语义？
5. Anthropic 密码分析结果中 model、multi-agent harness、token budget、人类验证和 executable
   pipeline 各自贡献多少？

## Sources

访问日期均为 2026-08-02；完整 source-level notes 位于七份 Daily。

### Model and Research Institutions

- Google Research, “Science One Framework”, published 2026-07-30:
  https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
- ScientistOne paper, arXiv v1 first public 2026-05-25: https://arxiv.org/abs/2605.26340
- Anthropic, “Discovering cryptographic weaknesses with Claude”, 2026-07-28:
  https://www.anthropic.com/research/discovering-cryptographic-weaknesses
- Kimi K3 Technical Report: https://arxiv.org/abs/2607.24653
- Qwen-UI-Agent: https://arxiv.org/abs/2607.28227

### Papers

- RARG: https://arxiv.org/abs/2607.24223
- CodeNib: https://arxiv.org/abs/2607.25431
- Reinforcement Learning for Code Optimization: https://arxiv.org/abs/2607.25970
- InferScale: https://arxiv.org/abs/2607.27090
- MemSecBench: https://arxiv.org/abs/2607.27080
- Revisiting Lossy Verification: https://arxiv.org/abs/2607.26627
- SemPIC: https://arxiv.org/abs/2607.28069
- OSReward: https://arxiv.org/abs/2607.28609
- MANTA: https://arxiv.org/abs/2607.28527
- ResKV: https://arxiv.org/abs/2607.29591
- SLIM: https://arxiv.org/abs/2607.29575

### Engineering

- MCP stable release: https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28
- vLLM v0.26.0: https://github.com/vllm-project/vllm/releases/tag/v0.26.0
- NVIDIA Dynamo releases: https://github.com/ai-dynamo/dynamo/releases
- SGLang releases: https://github.com/sgl-project/sglang/releases
