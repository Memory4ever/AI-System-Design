# AI Research Daily — 2026-08-15

- **Research date:** 2026-08-15（Asia/Shanghai）
- **Coverage window:** 2026-08-13 00:00 ～ 2026-08-15 09:10（Asia/Shanghai）
- **Access date:** 2026-08-15
- **Status:** Daily primary-source review completed；3 个系统候选完成全文核验并 refine 3 个既有章节；W33 尚未结束

## Executive Summary

今天没有发现需要作为新模型事件重复归档的机构发布，也没有确认窗口内达到长期门槛的 AI Infra release/RFC。
高价值证据集中在 8 月 13 日首次公开的三篇系统论文，它们补齐了三条已经存在、但粒度转换仍不完整的演进链：

```text
block-level paging
→ token-level liveness
→ pressure-activated physical reclamation

token-count / activated-expert proxy
→ calibrated multi-regime cost
→ makespan-aware expert dispatch

model replica autoscaling
→ stage disaggregation
→ operator-DAG elasticity
```

三篇论文均完成 arXiv v1 HTML 全文审读，包括方法、控制/数据流、实现、实验、ablation/sensitivity、限制与
相关 Appendix。它们分别提供 single-H100 KV relocation、8/16-GPU MoE serving 与 40×A100/24×GB200
operator provisioning 的作者实验；这些证据支持特定 workload contract 下的机制，不证明跨 runtime、硬件、
模型或多租户环境的普遍收益。

完成目标与相邻章节去重后，本日 refine Ch47、Ch49、Ch56。三个修改都位于旧方案的边界与下一粒度之间，
没有新增孤立论文段落，也没有改变 Part、章节号、Stable Node ID 或 ROADMAP 结构。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple Machine Learning Research、Google DeepMind、Google Research、
Meta AI / FAIR、Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、
Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、
StepFun、Xiaomi MiMo、InclusionAI 与 Hugging Face Blog 的 official Research/News/Publications、model/system
card、organization repository 与 technical-report surface。

Intern-S2-Preview technical report 的 arXiv v1 在 2026-08-13 首次公开，但模型 Source Family 已在 2026 年 5 月
公开，官方 repository 也在本窗口前完成 model release。因此本次记录为 `Related Primary Source / Revision
Evidence`，不把 technical report upload 伪装成新的模型发布事件。报告包含 scientific multimodal pretraining、
multi-task/agentic RL、on-policy distillation、time-series module 与 separate Memory Decoder 等多个机制；Sunday
W33 已完成 family-level 全文审读，结论为 `No Change — Source-family Evidence`。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence Level |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Intern-S2-Preview technical report | 2026-08-13 | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | E2 — arXiv v1 全文 + official repository；architecture/pretrain/post-train/evaluation 联合审计 |

### Recommended Action

- `No Change — Source Family Update`。Sunday W33 已联读 official repository、完整报告及早期 family boundary。
- Ch33 已有 partial rollout lifecycle、online draft freshness、typed process credit 与 multi-task optimization 边界；
  Memory Decoder、time-series、pretraining 和 post-training 的联合 recipe 缺 matched ablation，因此不拆成通用结论，
  也不重复计为模型发布事件。

## 2. 论文与学术来源

### Source Coverage

按 `cs.AI → cs.CL → cs.LG → cs.DC → cs.IR → stat.ML` 检查 arXiv recent，并对 cs.SE、cs.PL、
cs.RO、cs.CV 与 cs.PF 交叉筛选。Google Scholar、OpenAlex、DBLP、Semantic Scholar 与 Hugging Face Daily
Papers 用于发现、身份和重复关系；Crossref 用于 metadata 交叉检验。方法、实验与限制均回到 arXiv v1
HTML/PDF 与作者 artifact。

三个 `29/30` 候选在当日完成全文审读。DARTree、Vero、StateBridge、RippleMem、CROP 与 Post-Norm
Curriculum 随后在 Sunday W33 完成全文、目标/相邻章节与最终 disposition；没有从摘要直接写入 Books。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence Level |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| vToken: Token-Level Virtualization for Reclaimable KV Caches | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、vLLM prototype、paired mechanism/ablation；single-GPU scope |
| TEMPO: Makespan-Aware Expert-Parallel Load Balancing | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、calibrated simulation + 8/16-GPU wall-clock；部分 headline 为 model-space |
| OpScale: Operator-level Provisioning and Autoscaling | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、nano-vLLM prototype、A100/GB200 trace replay；single-model scope |
| DARTree | 2026-08-13 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | E2 — arXiv v1 全文、算法/lemma、七 benchmark、ablation 与 limitations；作者 latency contract |
| Vero | 2026-08-13 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | E2 — arXiv v1 全文、43-repository harness、两 task modes、audit 与 limitations |
| RippleMem | 2026-08-13 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | E2 — arXiv v1 全文、memory schema/graph/recollection、component/cost ablation 与 limitations |
| StateBridge | 2026-08-13 | 4 | 3 | 4 | 4 | 4 | 5 | 24/30 | E2 — arXiv v1 全文、closed-form alignment、四模型/两 family、sensitivity 与 case study |
| CROP | 2026-08-13 | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | E2 — arXiv v1 全文、triplet construction、selector ablation、reproducibility 与 limitations |
| Post-Norm under Curriculum Depth Growing | 2026-08-13 | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | E2 — arXiv v1 全文、matched controls/diagnostics/appendices；9-layer distillation boundary |

### Deep Analysis 1 — vToken：Paging 后为什么还需要第二层虚拟化

#### Why

PagedAttention 用固定 blocks 消除连续大块预留与大部分 external fragmentation；只要完整保留 KV，除尾块外
很少出现内部空洞。Token eviction 改变了这个前提：live tokens 散落在多个 partially occupied blocks 时，逻辑
容量已经释放，物理 allocator 却仍无法回收 block。

#### Principle

把 semantic liveness 与 physical reclamation 分开。Eviction policy 只决定哪些 token 可以死亡；runtime 维护
logical token identity、physical slot mapping、搬迁时机与 attention 可见性。Reclamation 必须保持 retained KV
完全等价，不能把 eviction 的质量损失和 relocation 的正确性混为一谈。

#### Mechanism

vToken 在既有 vLLM block allocator 上增加 per-sequence TokenTable、ReclamationManager 与 asynchronous copy
engine。Planner 从 request-local block/liveness snapshot 选择低利用率 blocks，只有预计 block 数严格下降且有
bounded evacuation headroom 时才提交；worker 在独立 CUDA stream 搬迁 K/V，更新 slot mapping，并在下一次可能
读取新位置的 attention launch 前等待 CUDA event。Shared-prefix blocks 暂时保守排除，CUDA Graph 的 tensors 与
captured inputs 保持稳定，只修改 replay 前的 mutable slot map。

#### Trade-off / Evidence Boundary

- 单张 H100-80GB；Mistral-7B、Llama-3.1-8B，capacity check 增加 Qwen2.5-14B；ShareGPT/LongBench。
- paired comparison 固定 prompts、decoding、policy、memory budget，temperature 0，`gpu_mem_util=0.90`；capacity
  frontier 使用 0.35/0.50 与 8K/12K output contracts。
- retained blocks 减少 27.2%～72.3%、throughput/frontier headline 只属于所列 policy、concurrency 与 p95 SLA。
- indirection-only ablation <1% 不证明高压下 relocation 免费；copy 与 Decode 会争用 GPU，planner 仍有 CPU cost。
- 当前只实现 single-node/single-GPU fast path，shared prefix 使用 conservative skip；TP、多 cache groups 与
  cross-device relocation 是推导边界，不是已验证生产事实。
- Full retention 在可行时仍优先；更 aggressive eviction 的 task quality 由 policy 负责，vToken 没有证明其无损。

#### Connection / Evolution / Recommended Action

主 owner `INFER-PAGED-ATTENTION`（Current Ch47，Legacy Ch43）。关系为 `Direct Evolution`：block paging →
token liveness → pressure-activated physical reclamation。`Refine — Existing Argument / Experimental`。

### Deep Analysis 2 — TEMPO：负载代理必须随执行 regime 改变

#### Why

MoE 的 EP group 在 dispatch、expert GEMM 与 combine 上同步，layer time 由最慢 GPU 决定。按 token 数均衡隐含
expert cost 随 token 线性增长；但 Decode 小 batch 可能主要支付每个 activated expert 的 weight-read floor，tile
边界与 All-to-All 又引入非线性。一个固定 proxy 在一个 regime 正确，在另一个 regime 可能主动制造碎片。

#### Principle

优化 wall-clock makespan，而不是把 token count、activation count 或 locality 当成跨 workload 的统一目标。
Cost model 必须对 `(kernel, dtype, hardware, expert shape)` 校准，并把 placement、dispatch 与 communication 的
控制层分开：dispatch 只能在现有 replicas 间移动 token，不能修复缺失的 hot-expert placement。

#### Mechanism

论文以 `max(activation/weight floor, token compute, communication)` 描述每 GPU 的 expert block cost，并在大
Prefill 下增加 tile staircase。`tempo_fast` 组合 whole-expert seeding、activation augmenting chains、partial token
migrations 与 token-LP/round-robin ensemble；graph 内只消费 persistent dispatch table 和计数，solver 在独立进程
异步计算并发布下一版。多节点先求 per-GPU shares，再以 same-node-first 规则选择 source→replica pairing。

#### Trade-off / Evidence Boundary

- 核心模型在 FP8 DeepGEMM、Qwen3/DeepSeek expert shapes 上约 10 分钟校准；kernel/driver/dtype 改变需重校准。
- 大量 headline 来自 calibrated simulator；8-GPU 与 2×8-GPU testbeds 提供 wall-clock anchor，full DSv3 EP32+
  仍含 extrapolation。
- Qwen3-235B FP8 的 shipped-LPLB 对比达到 1.4～1.7×，但 like-for-like 分析显示多数差异来自 data-path
  architecture；真实端到端收益只在特定 staleness/batch/compute-share band 出现。
- 小 expert、fresh placement、过小/过大 drift、All-to-All 已支配 step 或 expert compute share 低时，adaptive
  dispatch 为 parity 或 regression；论文明确报告负收益窗口。
- 异步 stale counts、model misspecification、table remap tax、restricted replication 与更深 topology 仍是开放问题。

#### Connection / Evolution / Recommended Action

主 owner `INFER-TENSORRT-LLM`（Current Ch49，Legacy Ch45），Ch21 只保留 Router/EP 语义。关系为
`Direct Evolution`：proxy balance → calibrated regime model → makespan dispatch。`Refine — Existing Argument /
Experimental`。

### Deep Analysis 3 — OpScale：资源粒度为什么会从副本下沉到 Operator

#### Why

完整模型副本是清晰的 failure/readiness unit，但 traffic burst 可能快于整模型 weight loading；不同 operator 对
batch、sequence length、QPS、memory 与 SM share 的 sensitivity 也不相同。统一复制全图会扩容非瓶颈部分，
而当前 critical path 仍可能没有得到最合适的 capacity。

#### Principle

Autoscaling unit 应与可独立测量、放置、路由和恢复的 bottleneck state 对齐。更细粒度只有在 end-to-end SLO、
operator dependency、communication 与 colocation interference 被共同建模时才有效；logical capacity plan 不能替代
physical placement validation。

#### Mechanism

OpScale 保留最小完整 base instances，并为额外 operator replicas 建立 data/control/execution planes：profiler 记录
workload-sensitive compute/memory/communication；control plane 选择 batch、replica、parallelism，并由 placement
module 以 memory/SM slack、interference model 与 locality 映射 GPUs；execution plane 维护 replica registry 与
capacity-weighted shortest queue。在线 greedy 结果与离线 exhaustive oracle 的差距在作者模型中不超过 8%。

#### Trade-off / Evidence Boundary

- prototype 基于约 17K Python LOC 的 nano-vLLM；模型包括 Qwen2-7B、Qwen2-57B-A14B 与其他 text/vision、
  dense/MoE workloads。
- 集群为最多 40×A100-80GB（5 VMs）与 24×GB200 NVLink domain；production traces 含 929K requests、
  1.5B tokens。precision、部分 concurrency 与完整 SLO matrix 并非所有图都披露。
- 最多 36.3% GPU、28% power、44% throughput 等数字绑定这些模型、trace、hardware 与 SLO，不是通用收益。
- operator profile、interference、queue model 分别仍有误差；physical placement 必须重新验证 SLO。
- ultra-low-latency megakernel、低 QPS、小模型或弱 operator heterogeneity 留给 model replica；online resharding 的
  weight redistribution 明显重于 replica scaling。
- 当前聚焦 single-model；multi-tenant fairness、cross-model interference 与 partial operator failure semantics 未闭合。

#### Connection / Evolution / Recommended Action

主 owner `INFER-SCHEDULING`（Current Ch56，Legacy Ch52），Ch55 提供 stage-disaggregation handoff，Ch63 继续拥有
cluster device placement。关系为 `Direct Evolution`：model replica → stage split → operator-DAG elasticity。
`Refine — Existing Argument / Experimental`。

## Full Source Review Addendum — Three `29/30` Candidates

### vToken — 29/30

- **Direct source / coverage:** arXiv:2608.13263v1；metadata、background、design、implementation、全部 evaluation、
  sensitivity、prefix compatibility、correctness、discussion、related work。
- **State ownership:** policy owns logical victims；TokenTable owns identity/mapping；allocator owns blocks；worker/CUDA
  event owns visibility barrier；scheduler owns headroom/backpressure。
- **Control/data flow:** policy event → liveness update → profitability plan → async K/V copy → slot-map publication →
  pre-attention event wait → old-block release。
- **Evidence proves:** 相同 eviction decisions 下，physical reclamation 可把 token holes 转成 reusable blocks，并在所列
  single-GPU workloads 改变 capacity/SLA frontier。
- **Does not prove:** token eviction quality、distributed correctness、shared-prefix relocation、任意 block size 的最优性。
- **Disposition:** `Refine — Existing Argument / Experimental` → Ch47。

### TEMPO — 29/30

- **Direct source / coverage:** arXiv:2608.13057v1；metadata、theory、cost model、solver、SGLang integration、完整
  simulation/wall-clock evaluation、ablation、multi-node experiments、limitations 与 relevant appendices。
- **State ownership:** Router owns expert choice；EPLB owns replica placement；dispatcher owns per-window token split；
  calibrated table owns estimated cost；runtime table revision owns graph-visible decision。
- **Control/data flow:** cumulative counters → background snapshot/aggregation → out-of-process solve → pinned table publish →
  fused graph-resident dispatch/count kernel。
- **Evidence proves:** expert execution存在至少 activation-floor、token/tile 与 communication regimes，固定 proxy 没有
  workload-independent dominance；time model 在作者 testbeds 的特定 band 能改善 makespan/tail。
- **Does not prove:** full-scale DSv3、4+ nodes、restricted-replica guarantee、任何 MoE Serving 默认应启用 adaptive dispatch。
- **Disposition:** `Refine — Existing Argument / Experimental` → Ch49。

### OpScale — 29/30

- **Direct source / coverage:** arXiv:2608.13499v1；metadata、characterization、optimization、three-plane implementation、
  baselines、trace evaluation、sensitivity、discussion 与 provisioning/placement appendices。
- **State ownership:** profiler owns versioned sensitivity；control plane owns logical plan；placement owns physical feasibility；
  replica manager owns lifecycle/registry；request path owns per-stage routing。
- **Control/data flow:** live workload + profiles → critical-path plan → interference/locality placement → replica lifecycle →
  weighted shortest queue → SLO observation/replan。
- **Evidence proves:** operator heterogeneity can make a finer elasticity unit useful in the disclosed single-model environment，
  and the prototype instantiates an end-to-end control loop。
- **Does not prove:** multi-tenant fairness、cross-model isolation、megakernel workloads、unreported hardware/runtime combinations。
- **Disposition:** `Refine — Existing Argument / Experimental` → Ch56。

## 3. AI Infra 与工程项目

### Source Coverage

检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、
Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、MLX、llama.cpp、ONNX Runtime 与 OpenXLA
的 official release surfaces。没有确认到 first-public date 位于本窗口、同时达到长期机制门槛的新 release/RFC。

搜索面仍会混入旧 release 页面或未来索引快照，因此版本事实必须回到 signed tag/release timestamp；本日没有把
重新抓取的 release notes 重复记为事件。

### Candidate Scoring

本组没有新增评分候选。

## Evidence Level and Claim Boundary

- **官方事实:** arXiv v1 metadata、official repository/model card 与 GitHub release/tag 时间。
- **论文实验结论:** 只在每篇披露的 model、hardware、precision、workload、batch/concurrency 与 SLO 范围内成立。
- **社区观点:** 未作为评分、机制或 Books Integration 依据。
- **本项目推断:** 三项共同说明“资源管理粒度必须与逻辑 state 粒度、物理 reclaim/placement 粒度和可观测 cost
  regime 对齐”；这是跨论文/章节联读的系统归纳，不是作者声明的统一架构。

## Knowledge Tree Position

| Candidate | Owner | Current Chapter | Legacy Chapter | Adjacent Chapters Read | Evolution Relationship |
| --- | --- | ---: | ---: | --- | --- |
| vToken | `INFER-PAGED-ATTENTION` | Ch47 | Ch43 | Ch45 / Ch46 / Ch47 | Direct Evolution |
| TEMPO | `INFER-TENSORRT-LLM` | Ch49 | Ch45 | Ch21 / Ch36 / Ch49 / Ch56 | Direct Evolution |
| OpScale | `INFER-SCHEDULING` | Ch56 | Ch52 | Ch49 / Ch52 / Ch55 / Ch56 / Ch63 | Direct Evolution |
| Intern-S2 report | `TRAIN-GRPO` | Ch33 | Ch29 | Ch23 / Ch29 / Ch33 / Ch48 / Ch81 | Layering / Dependency；No Change |
| DARTree | `INFER-SPECULATIVE-DECODING` | Ch48 | Ch44 | Ch46 / Ch48 / Ch49 | Alternative Branch；No Change |
| Vero | `PLATFORM-EVALUATION-SYSTEM` | Ch66 | Ch62 | Ch62 / Ch66 / Ch81 | Layering / Dependency；No Change |
| RippleMem | `AGENT-MEMORY` | Ch77 | Ch73 | Ch75 / Ch76 / Ch77 | Direct Evolution；Refine |
| StateBridge | `AGENT-MULTI-AGENT` | Ch82 | Ch78 | Ch81 / Ch82 / Ch83 | Alternative Branch；Refine |
| CROP | `TRAIN-GRPO` | Ch33 | Ch29 | Ch29 / Ch33 / Ch66 | Layering / Dependency；Refine |
| Post-Norm Curriculum | `MODEL-TRANSFORMER-LAYER` | Ch17 | Ch17 | Ch16 / Ch17 / Ch28 | Alternative Branch；No Change |

## Recommended Action

- vToken：`Refine — Existing Argument`，在 Ch47 从 block fragmentation 继续推导 token liveness 与 reclamation commit。
- TEMPO：`Refine — Existing Argument`，在 Ch49 将 MoE grouped execution 的 cost 从 token proxy 扩展为 conditional
  multi-regime makespan；不把算法写进 Ch21 的 Router owner。
- OpScale：`Refine — Existing Argument`，在 Ch56 补 model replica → stage split → operator DAG 的弹性粒度演进；
  Ch63 继续拥有物理 cluster placement。
- RippleMem：`Refine — Existing Argument / Experimental`，在 Ch77 将孤立 top-k 推进为 anchor recall → bounded
  associative expansion → provenance-preserving evidence assembly。
- StateBridge：`Refine — Existing Argument / Experimental`，在 Ch82 补 language hidden-state 的 training-free
  alignment 分支，同时保持 latent 只作 proposal channel。
- CROP：`Refine — Existing Argument / Experimental`，在 Ch33 区分 optimization need 与 task relevance，并把
  counterfactual sensitivity 明确限定为 proxy。
- DARTree、Vero、Post-Norm Curriculum 与 Intern-S2：`No Change — Already Covered / Source-family Evidence`；分别由
  Ch48 的并行 draft + causal correction + tree verification、Ch66 的 repository artifact/evidence contract、Ch17 的
  normalization×training-path 联合设计、Ch33 的 typed trajectory/partial rollout/online draft 现有主线覆盖。

## Ignored Noise

- Intern-S2-Preview model family 的技术报告 upload：作为 source-family mechanism synthesis，不重复制造新模型事件。
- arXiv recent 中与 AI System 知识树无关的 domain application、纯 survey/position paper、重复 revision。
- GitHub 搜索结果中的旧 release page、未来 crawl snapshot 与无 signed timestamp 的版本摘要。
- 缺 model、hardware、precision、input/output length、batch/concurrency 或 SLO 的 benchmark headline。

## Repository Changes

- 新增 `papers/2026/08/15/README.md`。
- Refine Ch47：补 block paging → token liveness → asynchronous reclamation 的演进、正确性与共存边界。
- Refine Ch49：补 MoE proxy balance → calibrated multi-regime makespan dispatch 的演进与 placement 边界。
- Refine Ch56：补 model-level → stage-level → operator-level elasticity 的演进与 ownership/failure boundary。
- Sunday follow-up Refine Ch33、Ch77、Ch82，并向 Ch17、Ch48、Ch66 的 Review notes 补入章节级 No Change 证据。
- 同步 `docs/LEARNING_STATE.md`；ROADMAP 与 DECISIONS 不变。
- 今天是 Saturday，未生成 W33 Weekly；未执行 stage、commit、push 或破坏性 Git 操作。

## Open Questions

1. vToken 如何为 TP shards、multiple KV groups 与 shared-prefix relocation 定义跨 shard atomic visibility？
2. TEMPO 的 calibrated cost surface 在 kernel revision、expert quantization 与 4+ node topology 下多久失效一次？
3. Operator-level runtime 如何把 partial operator failure、backpressure、request replay 与 multi-tenant fairness 纳入同一
   plan revision？
4. Intern-S2 的多组件联合报告缺少哪些 matched ablation，才能把 Memory Decoder、online draft 或 trace-aware
   experience 的收益从整体 recipe 中分离？
5. DARTree 在相同 target/draft、temperature、tree budget、GPU 与 concurrency 下，depth-wise materialization 是否仍
   优于 heap-based tree construction？
6. RippleMem 的 anchor expansion 在 concurrent update、delete、tool state 与独立 judge 下如何保持 graph/version identity？
7. StateBridge 连续 prefix 如何经过 security inspection、cross-version compatibility 和 deterministic replay？
8. CROP 的 counterfactual difficulty、triplet generation cost 与跨领域 transfer 应如何进入 selector EvalSpec？

## Sources

### 模型与研究机构

- Shanghai AI Lab / InternLM, Intern-S2-Preview official repository（模型 Source Family；首次发布早于本窗口；访问
  2026-08-15）: https://github.com/InternLM/Intern-S1
- Intern-S2-Preview technical report, arXiv:2608.13505v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13505

### 论文与学术来源

- vToken, arXiv:2608.13263v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/html/2608.13263v1
- TEMPO, arXiv:2608.13057v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/html/2608.13057v1
- OpScale, arXiv:2608.13499v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/html/2608.13499v1
- DARTree, arXiv:2608.13524v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13524
- Vero, arXiv:2608.13522v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13522
- StateBridge, arXiv:2608.13317v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13317
- RippleMem, arXiv:2608.13334v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13334
- CROP, arXiv:2608.13387v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13387
- Post-Norm under Curriculum Depth Growing, arXiv:2608.13156v1（提交 2026-08-13；访问 2026-08-15）:
  https://arxiv.org/abs/2608.13156
- arXiv cs.AI recent（访问 2026-08-15）: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent（访问 2026-08-15）: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent（访问 2026-08-15）: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent（访问 2026-08-15）: https://arxiv.org/list/cs.DC/recent

### AI Infra 与工程项目

- vLLM releases（访问 2026-08-15）: https://github.com/vllm-project/vllm/releases
- SGLang releases（访问 2026-08-15）: https://github.com/sgl-project/sglang/releases
- KServe releases（访问 2026-08-15）: https://github.com/kserve/kserve/releases
