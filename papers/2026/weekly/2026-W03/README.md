# AI Research Weekly — 2026-W03

> Coverage Window: 2026-01-12～2026-01-18
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Discovery Recall Re-audit: 2026-08-07
> Books Integration Review: 2026-08-13 — 7/7 dispositions complete; Discovery Recall remains open

## Executive Summary

原周报只覆盖机构发布，遗漏了四篇与本书主线更直接的论文。恢复后的长期信号分成四层：
MoE design 不能只由 total / active parameters 两个数字决定；KVzap 把昂贵的 token-importance
oracle 蒸馏为 hidden-state surrogate，却尚未证明真实 wall-clock / memory savings；TableCache
利用可显式验证的 schema dependency，把 offline KV blocks、CPU/GPU residency、batch reranking 与
prefetch pipeline 连成一个 domain-aware cache system；RAPID 则把节点功率预算从静态基础设施参数
提升为与 prefill/decode 角色共同调度的资源。四者共同说明“减少在线计算或资源”通常意味着引入
新的 learned policy、结构化 identity、离线状态或控制回路，而不是免费删除工作。

## Coverage and Source Coverage

- 模型与研究机构：按固定顺序保留 Google Research 1 月 12、13 日和 Anthropic 1 月 15 日
  官方条目。
- 论文与学术来源：除官方页面关联论文外，重新检查 arXiv 2026-01 `cs.CL` / `cs.DC` 与
  `cs.LG/cs.AI` cross-list，恢复 KVzap、MoE design under constraints、TableCache 与 RAPID；均已阅读
  metadata、HTML 正文、实验、ablation、limitations/discussion 和关键 appendix。
- AI Infra：TableCache 对 vLLM/SGLang 的描述属于作者 baseline / interoperability claim，不是两项
  framework 的官方 release；KVzap 论文也明确说明尚未完成 engine integration 和 wall-clock 验证。

## Discovery Recall Reconciliation

- **Original scored rows:** 3（其中 2 个 `>=20`，1 个 19 分边界项）。
- **Newly recovered at `>=20/30`:** 4（KVzap、MoE design under constraints、TableCache、RAPID）。
- **Cross-list / revision deduplication:** 按 arXiv ID 去重；KVzap 2026-02-03 v2 只用于 W03 事件的
  revision 核验，不在 W06 重复创建候选。
- **Source Review ledger:** 7/7 scored rows 有候选级 review；6/6 retained candidates 有完整 packet，
  NeuralGCM 维持 19 分低分核验。
- **Unresolved:** 当前环境仍不能形成所有 arXiv categories 的机器可复算 hit census，W03 Gate 为
  `Open — Partial Recall Repair`；已恢复候选的全文与日期核验已通过。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Anthropic Economic Index: economic primitives | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Worth Watching |
| MedGemma 1.5 / MedASR | 3 | 3 | 3 | 4 | 3 | 4 | 20/30 | Vertical evidence |
| NeuralGCM precipitation work | 3 | 3 | 3 | 4 | 2 | 4 | 19/30 | Record Only |
| KVzap | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine Ch45；Experimental |
| MoE design under memory/inference constraints | 4 | 4 | 3 | 4 | 5 | 5 | 25/30 | Refine Ch21 |
| TableCache | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Integrate Ch51；bounded domain |
| RAPID: power-aware prefill/decode reallocation | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Integrate Ch55；Experimental |

## Full Source Review

### Anthropic Economic Index: economic primitives

- **Candidate / Week / Score:** Economic primitives / 2026-W03 / 22/30；
  `Source Family ID: anthropic-economic-index-primitives`。
- **Source Type / Dates / Sources:** Anthropic 官方完整研究报告、method appendix 与公开 dataset；
  2026-01-15 发布，数据窗口为 2025-11-13～20。报告明确样本主要来自 Claude.ai 与 1P API。
- **Access and Full-read Coverage:** Verified；已检查 primitives 定义、classifier prompts/validation、
  sample/privacy thresholds、O*NET mapping、regression、limitations 与结论。不是宏观因果论文。
- **Problem / Previous Design / Changed Constraint:** 只统计 occupation 或 automation/augmentation
  无法区分 task complexity、human/AI skill、purpose、autonomy 与 success；真实使用需要多个有噪声、
  可版本化的 measurement primitives，而不是一个“AI impact”总分。
- **Mechanism / Ownership / Flow:** anonymized conversation sample→privacy filter/aggregation→Claude
  classifiers→task/primitives→region/occupation aggregates。Classifier、taxonomy、sampling window 与
  privacy threshold 都属于 measurement pipeline state。
- **Implementation / Evaluation Contract:** 九个 classifier 主要验证 directional accuracy；报告自己
  声明单项估计并非精确真值。conversation 是 observation unit，可能同一 user 多次出现；最低 cell
  thresholds 也会改变长尾可见性。
- **Evidence Boundary:** 证明特定 Claude 流量窗口中这些指标可用于描述性分析；不证明 Claude 成功
  等于业务成功，不证明观察到的 usage 代表劳动力总体，更不证明 exposure 导致就业变化。
- **Trade-offs / Previous Design Still Applies:** 多 primitives 增加解释力，也引入 classifier drift、
  privacy filtering、selection bias 与跨期不可比；简单 usage count 在稳定 taxonomy 的运营监控中仍有用。
- **Evolution / ROADMAP:** `Direct Evolution` within Economic Index measurement program；主节点
  `PLATFORM-EVALUATION-SYSTEM`（当前 Ch66 / Legacy Ch62），相邻 `PLATFORM-MONITORING`
  （当前 Ch67 / Legacy Ch63）。已读当前 Ch66～69；现有 EvalSpec、measurement identity 与
  telemetry boundary 已覆盖稳定原则。
- **Integration Decision:** `No Change — Already Covered`；Ch66 已要求 subject/environment/scorer
  identity，Ch67 已要求 sampling window 与 metric semantics；不复制经济结论。
- **Open Questions:** classifier、product surface 和 sample frame 变化后，哪些指标可以校准成真正
  可比的 longitudinal series？

### MedGemma 1.5 / MedASR

- **Candidate / Week / Score:** MedGemma 1.5 / MedASR / 2026-W03 / 20/30；
  `Source Family ID: google-haidef-medgemma15-medasr`。
- **Source Type / Dates / Sources:** Google Research 官方发布及所链接 model cards / Hugging Face
  artifacts；2026-01-13。属于 domain foundation-model assets，不是临床部署批准。
- **Access and Full-read Coverage:** Verified as official model/artifact fact；已检查模型用途、开放入口、
  adaptation 提示与 evaluation scope。训练数据完整构成、production monitoring 和临床 SLO 未统一披露。
- **Problem / Mechanism / Flow:** 通用 multimodal/ASR model 对医学影像、报告和术语分布覆盖不足；
  domain model 作为可再适配起点，经 task data、validation 与应用 runtime 才能进入具体 workflow。
  Model card 拥有 intended use，部署方拥有 local data、threshold、human review 和 incident state。
- **Evaluation Boundary:** 官方 benchmark 只证明披露数据集/任务上的作者结果；不证明跨医院、设备、
  口音、人群或临床流程泛化，也不证明最终诊疗安全。
- **Trade-offs / Previous Design Still Applies:** domain adaptation 提高术语和 modality fit，却增加数据
  governance、shift、calibration 与责任边界；通用模型 + retrieval/human workflow 在低频或快速变化知识上
  仍可能更合适。
- **Evolution / ROADMAP:** `Layering / Dependency`；`WORLDVIEW-WHAT-MODELS-LEARN`（Ch5）、
  `MULTIMODAL-REPRESENTATION`（Ch23）、`PLATFORM-MODEL-REGISTRY`（当前 Ch59 / Legacy Ch55）与
  `PLATFORM-EVALUATION-SYSTEM`（当前 Ch66 / Legacy Ch62）。已读目标及相邻章节；正文已有
  representation、data provenance、model registry 与 domain evaluation 契约。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；没有新增跨领域 AI System 机制。
- **Open Questions:** model card 如何携带 site-specific calibration、data lineage、drift slice 与 human
  escalation evidence？

### NeuralGCM precipitation work — Low-score verification

- **Candidate / Week / Score:** NeuralGCM precipitation / 2026-W03 / 19/30；
  `Source Family ID: neuralgcm-precipitation-2026`。
- **Source / Date / Verification:** Google Research 官方论文入口、library 和 precipitation model；
  2026-01-12。已核对 physics-based core + learned component、NASA precipitation observations、长期
  precipitation / extreme / diurnal-cycle evaluation；来源可验证，原 19/30 不上调。
- **Boundary / Rejection:** domain climate evidence；作者结果不等同 operational forecast SLO，且与本书
  当前 Model→Training→Serving 主线缺少新的通用机制。`Weekly Only — Low-score domain evidence`。
- **Open Questions:** hybrid physics/ML artifact 如何共同版本化 conservation constraints、observation
  dataset、rollout stability 与 uncertainty？

### KVzap

- **Candidate / Week / Score:** KVzap / 2026-W03 / 25/30；
  `Source Family ID: kvzap-learned-kv-pruning-policy`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 首次公开 2026-01-12，v2 修订
  2026-02-03，本轮访问 2026-08-07。W03 按 v1 计入，v2 仅补充核验。
- **Full-read Coverage:** 已阅读 metadata、KVzip/KVzip+ lineage、surrogate method、training data、
  compute/memory accounting、RULER/LongBench/AIME25、adaptive-threshold/sliding-window ablation、
  discussion、implementation challenges 和 appendix results。
- **Original Problem / Previous Design / Changed Constraint:** full KV 保持最强 fidelity 和规则 cache
  shape，便于 Flash/PagedAttention；training-free eviction 更轻却易丢关键信息；KVzip 以 double
  forward 的 context reconstruction 得到较好 importance score，但太慢且不能用于 long decode。
- **Mechanism / State / Flow:** 先用 KVzip+ oracle 生成每层/每 KV head 的 token score，再以
  hidden state 为输入训练 linear/MLP surrogate；在线对每个 token/head 预测 score，低于 threshold
  才在 attention 后 eviction，并保留最近 128 tokens。新增状态是 per-layer surrogate parameters、
  threshold、score buffer 和 variable per-head cache length。
- **Training / Evaluation Contract:** 每个 KV head 使用约 1.2M hidden-state/score pairs，来自过滤后
  约 2.4k Nemotron sample prompts；评测模型为 Qwen3-8B、Llama-3.1-8B-Instruct、Qwen3-32B，任务为
  RULER 4k～128k、LongBench 与 AIME25。AIME25 仅 30 题、每题 4 rollouts、上限 32k decode；
  RULER/LongBench 用 greedy、关闭 reasoning。硬件与真实 kernel throughput 未披露。
- **Evidence Boundary:** 论文支持在三种模型与列明 benchmark 上，以选定 threshold 获得约 2～4×
  logical KV compression 且作者观察到较小 accuracy loss；linear projection FLOP estimate 不是
  wall-clock。作者明确承认没有验证 GPU memory saving、prefill/decode speedup 或 engine integration。
- **Trade-offs / Failure Modes / Previous Design Still Applies:** learned policy 增加 model-specific
  training、threshold calibration 与 distribution-shift risk；不等长 head cache 破坏规则 PagedAttention
  layout，需要新 kernel。surrogate 错误是不可逆 eviction，full KV 在高 fidelity、短上下文或缺少
  variable-block kernel 时仍合理；training-free policy 在无法维护 surrogate lifecycle 时更简单。
- **Evolution / ROADMAP:** `Direct Evolution`：heuristic eviction → expensive oracle scoring → learned
  post-hoc surrogate → future end-to-end pruning。主节点 `INFER-KV-CACHE`（当前 Ch45 / Legacy Ch41），
  邻接 Ch44 Decode、Ch47 PagedAttention 与 Ch54 GPU Memory；pruning 与 quantization 是正交关系。
- **Integration Decision:** `Refine — Existing Argument`；已在 Ch45 接在 workload-aware eviction 后补入
  oracle distillation、threshold/recent-window safeguard、variable-head layout 与 policy identity；明确
  logical compression、FLOP estimate 不等于 HBM、wall-clock 或 production goodput。
- **Open Questions:** score model 如何随 base model / adapter / RoPE / tokenizer 版本失效；eviction
  rollback、prefix-cache sharing 与 multi-tenant isolation 如何定义？

### MoE design under memory/inference constraints

- **Candidate / Week / Score:** Towards Principled Design of MoE Language Models / 2026-W03 / 25/30；
  `Source Family ID: moe-design-constraint-scaling-law`。
- **Source Type / Dates:** arXiv primary paper v1，首次公开 2026-01-13，本轮访问 2026-08-07。
- **Full-read Coverage:** 已阅读 five-variable formulation、fixed-budget ablations、scaling-law fit、
  configuration comparison、Megatron/FineWeb-Edu setup、random-seed uncertainty、limitations 与
  architecture-optimization appendix。
- **Original Problem / Previous Design / Changed Constraint:** 用 total parameters 近似 memory、active
  parameters 近似 inference compute 是合理的 model-card contract，但多个 depth、width、expert count、
  Top-K、granularity 组合共享同一两个数字，无法回答在固定 memory / active budget 下怎样选 architecture。
- **Mechanism / State / Math:** 论文以 `l,d,n_exp,n_topk,g` 描述 architecture，近似
  `N_total≈ld²(4+3n_exp/g)`、`N_active≈ld²(4+3n_topk/g)`；先固定预算 ablate granularity 与 width/depth，
  再在 30M～3B 参数、固定 token budget 下拟合 log-log loss。作者的 disambiguated fit 使用
  `N_total,n_exp,n_topk`，强调相同 sparsity ratio 不代表相同性能。
- **Implementation / Evaluation Contract:** Qwen3-like architecture、4 attention heads、无 GQA、无
  shared experts；FineWeb-Edu、held-out loss、Megatron-LM、mixed precision、FlashAttention 与
  TransformerEngine。scaling-law 主实验组合 32～256 experts、Top-K 2～16、每模型 9B tokens；部分
  ablation 4B/46B tokens。GPU type/count、wall-clock、communication topology 与 inference SLO
  `Not Disclosed`。
- **Evidence Boundary:** 结果支持所搜索小/中规模空间内 total parameters、sparsity 与 expert count
  共同解释 loss；不证明给出的 exponent 或“少 experts / 多 active experts”能外推到 frontier scale、
  shared experts、GQA、different data 或真实 all-to-all / serving cost。作者承认 greedy search 与有限
  hyperparameter / dataset grid。
- **Trade-offs / Previous Design Still Applies:** 更多 active experts 可能改善 capacity utilization，却
  增加 compute、dispatch 和 communication；更多 total experts 扩大 parameter memory，并可能挤压
  dense core width/depth。total/active parameters 仍是有用的粗 contract，只是不足以充当 optimizer。
- **Evolution / ROADMAP:** `Refine — Existing Model Contract Candidate`；主节点 `MODEL-MOE`
  （Ch21 / Legacy Ch21），邻接 Ch7 Scaling Law、`TRAIN-DISTRIBUTED-TRAINING`（Ch36 / Legacy Ch32）、
  Ch40 Communication 与 Ch56 Scheduling。已读 Ch20～22、Ch7 与系统 handoff。
- **Integration Decision:** `Refine — Existing Argument`；已在 Ch21 明确 total/active parameters 是
  约束坐标而非 architecture optimizer，补入 `l/d/E/k/g` 的耦合与 system-cost 联合约束；作者
  exponent 只留在受限证据层，不进入正文定律。
- **Open Questions:** 加入 all-to-all、load imbalance、expert placement、HBM 与 SLO 后，architecture
  search 应怎样把 loss scaling 与 system cost model 联立？

### TableCache

- **Candidate / Week / Score:** TableCache / 2026-W03 / 25/30；
  `Source Family ID: tablecache-schema-aware-kv-reuse`。
- **Source Type / Dates:** arXiv primary systems paper v1，首次公开 2026-01-13，本轮访问
  2026-08-07。
- **Full-read Coverage:** 已阅读 related work、PFK representation、position handling、Table Trie、
  cache management、query reranking、compute/load pipeline、实验、ablation、complexity、limitations
  与 appendix 指针。
- **Original Problem / Previous Design / Changed Constraint:** prefix trie/cache 对字节/token 顺序稳定的
  shared prefix 有效；Text-to-SQL 请求虽反复引用同一批 schema，却会改变 table order，导致通用 prefix
  identity 失配。独立预计算 table block 又切断 causal cross-table dependency，造成 accuracy loss。
- **Mechanism / State Ownership / Flow:** offline 从 primary/foreign-key graph 拓扑排序，生成保留
  inter-table dependency 的 table KV blocks 并存 CPU；Table Trie 保存 table identity → cache path；
  online 匹配并按全局位置重施 positional encoding，GPU cache manager 做 residency/eviction。batch
  scheduler 根据 table-set similarity 重排请求，同时 compute current micro-batch、prefetch next caches。
- **Evaluation Contract:** Spider/BIRD，OmniSQL-7B 与 Qwen2.5-7B-coder；baseline 为 Transformers、
  vLLM/SGLang RadixCache、PromptCache、TurboRAG。单张 NVIDIA A800，`b_c=100,b_m=10`；backbones
  在 BIRD train complex tables 上 fine-tune 3 epochs。主要指标是整个 test set 的 total TTFT 与 SQL
  execution accuracy，不是单请求 percentile SLO；precision、concurrency、cache capacity 未披露。
- **Evidence Boundary:** 作者结果与 ablation 支持在显式 schema graph、可重排 batch、稳定 tables 和
  单卡实验中减少累计 TTFT；不证明通用 RAG/unstructured documents 可复用，也不证明线上 arrival
  order、fairness、tenant permissions、schema update 或 tail latency 下仍有同等收益。
- **Trade-offs / Failure Modes / Previous Design Still Applies:** 计算被转移为 CPU storage、GPU
  residency、identity/version、invalidations 与 PCIe loading；reranking 改变请求顺序并可能伤害 fairness /
  deadlines，论文复杂度含 `O(N²m/64)`。schema 高频变化或低 reuse 时在线 prefill / standard prefix
  cache 更合理；无法显式恢复 block dependency 时 selective recompute 比直接拼接更安全。
- **Evolution / ROADMAP:** `Direct Evolution`：exact prefix reuse → independent block precompute →
  dependency-aware reusable blocks → residency-aware reranking/prefetch。主节点 `INFER-SGLANG`
  （当前 Ch51 / Legacy Ch47），邻接 Ch45 KV lifecycle、Ch56 Scheduling 与 `AGENT-RAG`
  （当前 Ch76 / Legacy Ch72）。已读 Ch50～52、Ch75～76，确认 runtime 与 retrieval owner 边界。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch51 将 exact prefix 演进为带 dependency、
  position、permission 与 invalidation 的 reusable blocks，并保留 selective recompute、online Prefill
  与 arrival-order SLO 的共存边界；Text-to-SQL 只作为结构化领域案例。
- **Open Questions:** cache identity 是否应包含 model/tokenizer/adapter/RoPE/schema/permission 版本；
  如何在不破坏 arrival-order SLO 的情况下决定可重排窗口？

### RAPID: Power-Aware Dynamic Reallocation for Inference

- **Candidate / Week / Score:** RAPID / 2026-W03 / 27/30；
  `Source Family ID: rapid-power-aware-pd-reallocation`。
- **Source Type / Dates / Revision:** arXiv primary systems paper v1，真实 identifier 为
  `arXiv:2601.12241`，首次公开 2026-01-18，本轮于 2026-08-13 重新核验。此前记录的
  `2601.12727` 实际属于无关的人格影响论文，已纠正；事件仍归入 W03。
- **Full-read Coverage:** 已阅读 metadata、problem formulation、PD architecture、power sensitivity、
  power/GPU reallocation algorithm、implementation、LongBench 与 synthetic evaluation、sensitivity、
  related work、conclusion 和 future-work boundary；论文没有独立 Limitations 章节。
- **Original Problem / Previous Design / Changed Constraint:** 静态 colocated 或 disaggregated PD 在负载
  稳定、功率充足时容易部署；但 prefill 更接近 compute/power sensitive，decode 更接近 memory-bound，
  同一节点 uniform power cap 会让两个阶段承受不对称损失。约束从“GPU 数量固定”扩展成“节点总功率、
  GPU 角色与 TTFT/TPOT SLO 共同受限”。
- **Mechanism / State Ownership / Control Flow:** central scheduler 维护 prefill/decode queues、worker role、
  per-GPU power cap 与 cooldown；先根据 TTFT/TPOT 和 queue pressure 调功率，仍无法满足时才改变 GPU
  角色。vLLM 0.8.4 worker 间以 HIP IPC / XGMI 直接传 KV，persistent ring buffer 与 atomic ready flag
  构成 handoff；decode 侧 pull，避免 host staging。新增的是有滞回的 closed-loop controller，而不是
  单次离线配置。
- **Implementation / Evaluation Contract:** 单节点 8× AMD MI300X，论文报告每卡约 192/196 GB HBM、
  750 W 上限；节点 full-power 约 6000 W，受限实验为 4800 W。Llama-3.1-8B、TP=1；LongBench 最长
  8K，以及 8K/128、512/512 synthetic prompts，Poisson arrivals。指标为 TTFT、TPOT、goodput、QPS/W；
  role shift 约 2～5 秒，power-cap 调整为数百毫秒，cooldown 约 2～6 秒，均是作者实现条件。
- **Evidence Boundary:** 论文支持在上述单节点、小模型、指定 trace 下，non-uniform power allocation
  能在较低总功率保持接近 full-power disaggregated 的表现，动态 power + role reallocation 对 phase mix
  变化优于只调功率；摘要的“up to 2×”必须绑定 workload、baseline 与 SLO，不能外推为任意 serving
  cluster 的通用吞吐提升。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** controller 引入 sensing delay、
  hysteresis、oscillation 与 role-transfer downtime；KV handoff ring buffer 带来容量、backpressure、
  consistency 和 recovery 问题。稳定 workload、宽松 SLO 或 power 不受限时，静态 uniform cap 与固定
  PD ratio 更简单；跨节点、TP>1、大模型和机架级 power coordination 尚未由论文证明。
- **Evolution / ROADMAP:** `Layering / Dependency`：固定 colocated serving → 固定 PD → static non-uniform
  power → feedback-driven power reallocation → power + GPU-role reallocation。主节点
  `INFER-PD-DISAGGREGATION`（当前 Ch55 / Legacy Ch51），邻接 Ch54 GPU Memory、Ch56 Scheduling 与
  Ch63 GPU Scheduler。已读 Ch54～56、Ch63，明确 facility/node power 与 request-state ownership 的接口。
- **Integration Decision:** `Integrate — New Mechanism`；已在 Ch55 将 power cap 纳入 P/D closed-loop，
  补齐 telemetry、actuation、cooldown、role epoch、rollback 与跨层 ownership；单节点 MI300X、TP=1
  的结果不外推到 rack、多模型或多 GPU model serving。
- **Open Questions:** power controller 的 telemetry freshness、safe actuation、failure recovery 与跨节点
  ownership 应由 serving scheduler、cluster scheduler 还是 facility power plane 负责？

## Evidence Level

机构页面说明发布事实；新增论文结论只在其 model/data/hardware/measurement contract 中成立。
KVzap 没有 wall-clock/kernel evidence，MoE scaling law 缺少 frontier/distributed cost 验证，TableCache
只验证 schema-rich Text-to-SQL，RAPID 只验证单节点 MI300X、TP=1、小模型与列明 trace；这些边界与
临床、经济 telemetry 的外推限制同等重要。

## Cross-Week Deduplication

后续 Economic Index 报告属于同一 measurement program；KVzap v2 归入 W03 source family；后续
KV compression 需区分 pruning、quantization、sparse attention 与 block reuse；后续 TableCache-like
方法需比较 dependency reconstruction 与 cache identity，而不只比较 hit rate。
RAPID 必须按 2026-01-18 v1 归入 W03；后续 power-aware scheduling 若扩展到 rack/facility 层，应作为
同一 source family 的演进核验，而非证明当前单节点结果已外推成立。

## Knowledge Tree Position

新增主节点为 `MODEL-MOE`（Ch21）、`INFER-KV-CACHE`（Ch45 / Legacy Ch41）、`INFER-SGLANG`
（Ch51 / Legacy Ch47）与 `INFER-PD-DISAGGREGATION`（Ch55 / Legacy Ch51）。MedGemma/NeuralGCM
保持领域/版本证据，Economic Index 由 Ch66/67 去重。共同原则是 state identity、evidence contract
与 changed constraint，但不同候选不构成直接替代。

## Recommended Action

七个候选已完成逐项 disposition 与周级反向检查。四篇系统/模型机制论文已按唯一 owner 融入现有
演进链；Economic Index 为章节级 No Change，MedGemma 与 NeuralGCM 仅保留 Weekly。W03 Discovery
Recall 仍为 Open；未来恢复的新候选必须重新打开本周 Books Review。

## Event-Date Daily Decision

2026-01-12、01-13、01-15、01-18：直接记入 Weekly；历史回填不创建 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete — 7/7 dispositions；Archive Discovery Gate Open`。

- Economic primitives：`No Change — Already Covered` → Ch66/67；
- MedGemma 1.5 / MedASR：`Weekly Only — Version/Product Fact`；
- NeuralGCM：`Weekly Only — Low-score domain evidence`；
- KVzap：`Refine — Existing Argument` → `INFER-KV-CACHE` / Ch45；
- MoE design：`Refine — Existing Argument` → `MODEL-MOE` / Ch21；
- TableCache：`Integrate — New Mechanism` → `INFER-SGLANG` / Ch51；
- RAPID：`Integrate — New Mechanism` → `INFER-PD-DISAGGREGATION` / Ch55。

周级 Review 重新打开四篇 primary source，发现并修正 RAPID 的错误 arXiv identifier；同时确认 KVzap
没有 engine wall-clock 证据、MoE fit 不能跨规模外推、TableCache 的 dependency oracle 不能泛化到
unstructured RAG，RAPID 的 power response 不能泛化到机架级系统。

## Ignored Noise

把领域 benchmark 写成通用部署能力、把 logical KV compression 当作 wall-clock speedup、把小规模
loss fit 当作 frontier law、把 batch total TTFT 当作单请求 tail SLO，以及只在标题层命中但未完成
全文/评分的论文。

## Repository Changes

- 2026-08-07：恢复四篇遗漏论文，补充评分、Full Source Review、revision 去重和 recall limitation；
  无历史 Daily 或 Books 修改。
- 2026-08-13：完成 W03 独立 Books Gate，更新 Ch21、Ch45、Ch51、Ch55；纠正 RAPID primary
  identifier `2601.12727 → 2601.12241`，同步 owner、disposition 与证据边界。

## Open Questions

1. usage telemetry 的 taxonomy 更新后，怎样保持跨期可比性？
2. learned KV pruning 怎样与 variable-block kernel、cache rollback 和 prefix reuse 组合？
3. MoE quality scaling 与 all-to-all / HBM / SLO cost model 怎样联立？
4. dependency-aware KV block 的 identity、permission、invalidations 与 fairness 由哪个层拥有？
5. PD scheduler 与 cluster/facility power controller 之间怎样分配 actuation、rollback 与 safety ownership？

## Sources

- Google Research January 2026 archive, accessed 2026-07-31:
  https://research.google/blog/2026/01/
- Anthropic Economic Research index, accessed 2026-07-31:
  https://www.anthropic.com/research/team/economic-research
- KVzap, arXiv v1 published 2026-01-12, v2 revised 2026-02-03; accessed
  2026-08-07: https://arxiv.org/abs/2601.07891 ;
  HTML reviewed: https://arxiv.org/html/2601.07891v2
- Towards Principled Design of MoE Language Models under Memory and Inference Constraints,
  arXiv v1 published 2026-01-13; accessed 2026-08-07:
  https://arxiv.org/abs/2601.08215 ; HTML reviewed: https://arxiv.org/html/2601.08215v1
- TableCache, arXiv v1 published 2026-01-13; accessed 2026-08-07:
  https://arxiv.org/abs/2601.08743 ; HTML reviewed: https://arxiv.org/html/2601.08743v1
- RAPID: Power Aware Dynamic Reallocation For Inference, arXiv v1 published
  2026-01-18; identifier corrected and accessed 2026-08-13:
  https://arxiv.org/abs/2601.12241 ; HTML reviewed: https://arxiv.org/html/2601.12241v1
- arXiv January 2026 `cs.CL` / `cs.DC` monthly listings, accessed 2026-08-07:
  https://arxiv.org/list/cs.CL/2026-01 and https://arxiv.org/list/cs.DC/2026-01
