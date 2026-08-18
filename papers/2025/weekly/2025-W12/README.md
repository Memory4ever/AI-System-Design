# AI Research Weekly — 2025-W12

> Coverage Window: 2025-03-17～2025-03-23
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Conditional Pass — 110 Owner Identities / 5 Exact Source Blockers
> Discovery Gate: Conditional Pass — Fixed-Organization Replay Closed / Cross-Index Recall Limitation Disclosed
> Historical Books Gate: Closed

## Executive Summary

旧文件的 43-owner 账本只是初始下界。重放 W12 周榜、逐日 HF/arXiv discovery、W13 spillback 与固定组织 release 后，当前可复算为 **110 个 W12 owner identities：98 个 strict Full Source Review、7 个低分 closure、5 个 Unverified / Blocked**，ordinary Review Pending 为 0。STEVE、MagicID、LLM-Mediated Guidance 与 CURIE 共 4 项按 arXiv v1 日期回拨 W11，不计入 W12 分母。

ETVA v1 PDF 已恢复并完成全文审计；固定组织 replay 又恢复 vLLM v0.8.1、Transformers v4.50.0 与 JAX v0.5.3 三个 owner events。剩余五个 source families 缺 event-time full text：TokenBridge、Judge Anything、TULIP、One-Step Residual Shifting Diffusion、VideoRFSplat。按用户授权执行 precise blocked-skip 后，W12 candidate evidence ledger 可条件闭合，但 archive source-complete gate 仍受这五项材料请求限制。

这次修复只写 Weekly evidence；Historical Books Gate 保持关闭，不把摘要写入 Books。

## Coverage Window and Limitations

- ISO window 为 Monday 2025-03-17 至 Sunday 2025-03-23。
- arXiv v1 / official release first-public date 决定 owner week；HF 推荐日、manuscript date 与 later revision 不替代事件日期。
- HF、Scholar、OpenAlex、DBLP、Crossref 只用于 discovery/identity/dedup；机制回到 primary source。
- 只有摘要或 later revision 可读时，不把 candidate 升级为 strict complete。
- 作者 benchmark 只在披露的 model、hardware、precision、length、batch/concurrency 与 evaluator contract 内成立。
- 固定组织的官方 release/tag 已逐项核对；Scholar/OpenAlex/DBLP/Crossref 没有可冻结的全量查询导出，因此仍披露 cross-index recall limitation，但不存在未路由的已知 candidate identity。

## 1. 方法与去重

- owner week 使用 arXiv v1 / 官方 release first-public date，不使用 HF 推荐日。
- 同一 `arXiv ID + Source Family` 只评分一次；revision/repository 只作 lineage。
- HF 只用于 discovery；机制、实验、limitations 回到 v1/official artifact。
- 只有摘要、v1 无法取得或 HTML 指向后续 revision 时，不给 final score。
- Books disposition 仅记 `Books Pending` / `Weekly Only` / `Blocked`；不写 Books。

## 2. 旧文件 22 项复核

以下 22 项继续有效；需要把 Gate 统计改成“22 strict packets among a larger reopened census”。

| Candidate | Score | Owner | 复核 |
| --- | ---: | --- | --- |
| Private Prediction | 23 | `PLATFORM-SECURITY` | 保留；2025 是 Blog amplification，论文首发 2024 |
| NVIDIA Dynamo | 27 | `INFER-DYNAMO` | 保留；launch 与 later APIs 分开 |
| SGLang joins PyTorch | 20 | `INFER-SGLANG` | 保留为 ecosystem/version fact |
| RWKV-7 | 29 | `MODEL-TRANSFORMER-LAYER` | 保留 |
| DAPO | 29 | `TRAIN-GRPO` | 保留 |
| R1-VL | 27 | `TRAIN-GRPO` | 保留 |
| VideoMind | 28 | `AGENT-WORKFLOW` | 保留 |
| MicroVQA | 26 | `PLATFORM-EVALUATION-SYSTEM` | 保留 |
| R0 | 28 | `MULTIMODAL-GENERATIVE-PARADIGMS` | 保留 v1 |
| Edit Transfer | 23 | `MULTIMODAL-REPRESENTATION` | 保留 |
| BlobCtrl | 27 | `MULTIMODAL-REPRESENTATION` | 保留 |
| WideRange4D | 22 | `MULTIMODAL-WORLD-MODELS` | 保留 |
| Impossible Videos | 26 | `PLATFORM-EVALUATION-SYSTEM` | 保留 |
| Creation-MMBench | 25 | `PLATFORM-EVALUATION-SYSTEM` | 保留 |
| DeepPerception v1 | 28 | `TRAIN-GRPO` | 保留；不倒写 KARL v3 |
| Infinite Mobility | 25 | `MULTIMODAL-EMBODIED-VLA` | 保留 |
| Multimodal Preference Survey | 24 | `TRAIN-DPO` | 保留为 survey/source map |
| Frac-Connections | 27 | `MODEL-TRANSFORMER-LAYER` | 保留 |
| Cosmos-Transfer1 | 29 | `MULTIMODAL-WORLD-MODELS` | 保留 |
| Measuring AI Long Tasks | 29 | `PLATFORM-EVALUATION-SYSTEM` | 保留 |
| FlexWorld | 24 | `MULTIMODAL-WORLD-MODELS` | 保留 |
| DreamRenderer | 27 | `MULTIMODAL-REPRESENTATION` | 保留；v1 recovered |

### 2.1 原有 retained 候选 Full Source Review（22）

Score order is fixed as `Technical Novelty / System Impact / Practical Value / Source Reliability / Project Relevance / Longevity`.

#### Private prediction for large-scale synthetic text generation

- **Candidate / Week / Score:** Differentially private LLM inference for synthetic data / 2025-W12 / 23/30。
- **Primary Source URLs:** https://arxiv.org/abs/2407.12108；https://research.google/blog/generating-synthetic-data-with-differentially-private-llm-inference/。
- **Six-dimensional Score:** Technical Novelty 4 / System Impact 4 / Practical Value 4 / Source Reliability 4 / Project Relevance 4 / Longevity 3 = **23/30**。
- **Source Family ID:** `google-private-prediction-synthetic-text-2024-2025`。
- **Source Type:** 2025 Google Research Blog + 2024 peer-reviewed paper / arXiv。
- **First-public Date / Revision History:** 论文 arXiv v1 为 2024-07-16，v2 为 2024-10-09（EMNLP 2024 Findings camera-ready）；Google Research Blog 发布于 2025-03-18。故本条是 2025 官方再传播事件，不是 2025 首发论文，年度元数据需在 Evidence Gate 时纠正。
- **Direct Primary Sources:** 论文 arXiv v2 全文；Google Research Blog。
- **Related Primary Sources:** 论文引用的 private prediction、exponential mechanism 与 sparse vector 文献用于定理和机制背景；不以 Blog 摘要替代正文。
- **Access and Verification Status:** Verified；20 页正文与 appendix 已读取。
- **Full-read Coverage:** metadata/revisions、problem、privacy definitions/theorems、algorithm、fixed-batch implementation、public drafter、experiments、compute、limitations 与 appendix 已覆盖。
- **Original Problem:** 私有 records 被放入 LLM prompts 生成 synthetic text 时，每个 next-token distribution 都可能暴露单个 record；仅保护下游模型训练或控制 API access 不给已发布合成数据形式化边界。
- **Why the Previous Design Was Reasonable:** 直接用 pretrained LLM 做 in-context generation 无需训练私有模型，易部署且质量高；若数据不敏感、只在可信边界内使用，普通 sampling 仍是更低成本方案。
- **Changed Constraint:** 需要公开数千条可复用 synthetic outputs，同时限制任一 private example 对整个输出分布的影响；逐 token 朴素 private aggregation 会快速消耗 privacy budget。
- **Mechanism:** 每个 private prompt 给出 next-token log-probabilities，先 recenter/clip，再跨 disjoint batches 聚合；softmax sampling 被解释为 exponential mechanism。固定 batch 跨 tokens 复用 KV Cache，并利用 parallel composition。public drafter 仅依赖已生成 synthetic prefix；sparse-vector/AboveThreshold 判断 public prediction 是否足够，public token 不消费 private query budget，分歧位置才调用 private aggregation。
- **State Ownership:** privacy accountant 拥有整次 release 的预算；batch assignment 必须仅依赖 record 本身（论文给出 hash 示例）；public drafter 不能读取 private records；target LLM 仍是 non-private pretrained model；输出数据是 DP release，模型本身不是 DP artifact。
- **Control Flow / Data Flow:** private examples → deterministic disjoint batch assignment → parallel LLM logits → recenter/clip/aggregate → private token sampling；或 synthetic prefix → public drafter → sparse-vector gate → public token / fallback private token。每个 release 必须把 token-level calls composition 到同一 ledger。
- **Implementation Details:** 固定 batch 避免每 token 重新分组并允许 KV reuse；作者还给出 public-data-assisted drafting 和 structured generation 的高收益路径。该机制保护 output distribution，不修改 base model weights。
- **Evaluation Setup:** Gemma 1.1 2B 用于 generation，另含已废弃 GPT-3 babbage ICL baseline 和 BERT-110M downstream fine-tuning；AGNews、TREC、DBPedia、MIT、IMDB、Yelp、WikiMoviesJSON 等数据；生成规模和 downstream utility 分别评测。
- **Baselines / Ablations / Sensitivity:** 对比 prior private prediction、private fine-tuning、public/private token paths；分析 batch size、privacy budget、public drafter、structured data 与 downstream data scale。作者明确 private fine-tuning 在部分设置仍更优。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** ICL 约 90～1,500 private examples，fine-tuning 约 2.5K～200K；private aggregation batch size 127～2,047；每 run 约 8～48 accelerator-hours，研究总量约 14K accelerator-hours。accelerator 型号、precision、online concurrency 与 serving SLO 未披露。
- **What the Evidence Actually Proves:** 在作者数据集和模型下，改进的 accounting、exponential-mechanism view、固定 batch 与 public drafting 能把 private prediction 从少量样本扩展到数千 synthetic examples，并形成可计算 DP guarantee。
- **What It Does Not Prove:** 不证明生成文本事实正确、公平或无 public-data leakage；不保护 base model；不证明任意 free-form corpus、重复 release 或交互式查询都保持同等 utility；不证明比 private fine-tuning 普遍更便宜。
- **Limitations / Threats to Validity:** 多为分类/结构化任务；private token 数决定预算；GPT-3 baseline 因 API/top-logprob 变化难复现；hardware 与端到端 latency 未披露；下游再发布虽受 post-processing 保护，错误解释和 utility 仍需独立评测。
- **Trade-offs / New Failure Modes:** 更大 batch 降 noise/改 utility却增加每 token LLM calls；public drafter 节省 budget却可能频繁 fallback；错误 batch identity、跨 release composition、accountant/version drift 会让形式保证失真。
- **Where the Previous Design Still Applies:** 数据可公开、只在可信域内生成、release 很少，或需要无限交互且可接受训练私有模型的场景，non-private generation / private fine-tuning 仍可能更合理。
- **Evolution Relationship:** `Layering / Dependency`：non-private LLM inference → private aggregation → public-drafter sparse-vector optimization；并非 2025 新工作替代 2024 论文。
- **ROADMAP Node:** 主 owner `PLATFORM-SECURITY`（current Ch72 / legacy Ch68）；`TRAIN-DATA` 与 `PLATFORM-EVALUATION-SYSTEM` 提供 data/evaluation handoff。
- **Target and Adjacent Chapters Read:** 已读 current Ch71 Multi Tenant、Ch72 Security、Ch73 Production Best Practice，并核验 ROADMAP stable/legacy mapping。
- **Existing Coverage:** Ch72 已写明 synthetic output、privacy unit、composition、accountant 与 inference-time / fine-tuning 适用边界，且已引用该论文；Source Review 证实该论点方向正确，但发现年度 first-public 归档错误。
- **Integration Decision:** `Books Pending — Refine Existing Argument`；Historical Books Gate 关闭；后续只在 Books Gate 打开后复核 privacy unit、composition 与 2024 first-public 边界。
- **Changed Files or Rejection Reason:** 本轮不改 Books；不把 2025 Blog 当作新论文机制。
- **Open Questions:** 年度索引如何标记“2025 official amplification of 2024 research”；真实产品的 release-level budget ledger、重复 query 与 user-level adjacency 如何实现。

#### NVIDIA Dynamo

- **Candidate / Week / Score:** NVIDIA Dynamo / 2025-W12 / 27/30。
- **Primary Source URLs:** https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/；https://github.com/ai-dynamo/dynamo。
- **Six-dimensional Score:** 5 / 4 / 4 / 5 / 5 / 4 = **27/30**。
- **Source Family ID:** `nvidia-dynamo-distributed-inference-runtime`。
- **Source Type:** 官方 announcement、开源 repository、后续 architecture/design docs 与 releases。
- **First-public Date / Revision History:** 2025-03-18 首次公开；后续 architecture、API 和 release line 持续演进。当前文档只能作为 evolution evidence，不得回写成 2025-03-18 已具备的精确接口。
- **Direct Primary Sources:** NVIDIA launch Blog；ai-dynamo/dynamo repository；当前官方 architecture/disaggregated-serving/planner docs（标记为后续状态）。
- **Related Primary Sources:** NIXL、TensorRT-LLM、vLLM integrations 与后续 Dynamo releases；用于验证 layering，不替代初始发布事实。
- **Access and Verification Status:** Verified for announcement and disclosed benchmark contracts；2025 初始 commit/tag 的完整稳定 API 未形成单独 archived design spec，精确 early semantics 标记 `Not Disclosed / Evolving`。
- **Full-read Coverage:** 初始组件、request routing、planner、KVBM、NIXL、PD disaggregation、benchmark setup/footnotes 与当前 architecture/control/request/state paths 已覆盖。
- **Original Problem:** 单 engine 能调度本地 token 和 KV blocks，却无法独立在数据中心尺度协调多 worker 的 KV locality、Prefill/Decode phase capacity、跨节点 state transfer 与变化负载。
- **Why the Previous Design Was Reasonable:** 聚合式 engine 减少网络 handoff 和控制面状态，单机或均衡短请求下更简单、failure domain 更小；round-robin 在 state locality 不重要时成本低。
- **Changed Constraint:** reasoning 模型出现 32K input / 8K output 等长而不对称阶段，KV 重用和跨 worker placement 影响 TTFT/ITL；Prefill 与 Decode 的 GPU shape、queue 与扩缩容需求分离。
- **Mechanism:** 初始发布将 smart router、planner、distributed KV cache manager、PD disaggregation 与 NIXL 组合。router 用 KV overlap 与 worker load 选 endpoint；planner比较 queue wait、KV transfer 和 processing estimates，决定 aggregated/disaggregated placement 并移动 capacity；KVBM 提供 GPU/host/SSD/network tiers；NIXL 承担跨内存/节点的数据移动。
- **State Ownership:** engine worker 拥有实际 request execution/KV buffers；router/index 持有 locality metadata；planner拥有 capacity decision；KVBM/NIXL 管理 placement/transfer。后续文档又明确 request plane、control plane、event/state paths，但这是后续演进，而非 launch day API guarantee。
- **Control Flow / Data Flow:** request → smart router（prefix overlap + load）→ aggregated worker 或 Prefill pool → KV transfer via NIXL/KVBM → Decode pool → stream；telemetry → planner → capacity reconfiguration。KV event 可见不等于 bytes 已 ready，必须有 transfer completion/error contract。
- **Implementation Details:** 初始项目定位为可与 TensorRT-LLM、vLLM 等 engines 组合的 distributed layer；框架/接口在开源后快速变化。不能用 2026 docs 中的 class、CRD、metadata schema解释 2025 实现。
- **Evaluation Setup:** launch Blog 含 DeepSeek-R1 与 Llama-70B 两类实验及 KV-aware routing trace replay。DeepSeek-R1：671B、GB200 NVL72、TensorRT-LLM FP4、ISL/OSL 32K/8K；baseline inflight TEP16/PP4/DP4，对比 disaggregated context EP4/DP16 + generation EP64/DP3，`up to 30x` 为厂商条件/部分 projected。Llama-70B：Hopper、vLLM FP8、3K/50。router：2×HGX-H100 nodes、8 个 DeepSeek-R1-Distill-Llama-70B instances、vLLM FP8 TP2、约 100K production requests，平均 4K/800。
- **Baselines / Ablations / Sensitivity:** aggregated/inflight batching、static/round-robin routing 与 KV-aware/disaggregated designs；初始公开材料不足以提供完整 planner ablation、failure injection 或 sensitivity surface。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 如上；并发、完整 arrival distribution、P99 SLO、power/cost 与部分 software versions 未完整披露，故不把倍数外推。
- **What the Evidence Actually Proves:** NVIDIA 在 2025-03 公开了以 KV state、phase-aware routing 和跨层 memory transfer 为中心的 distributed inference architecture，并在特定硬件/模型/workload 下报告收益。
- **What It Does Not Prove:** 不证明 PD 对所有 workload 更优，不证明 launch-day implementation 已有后续文档的 fault semantics，也不证明单个 benchmark 倍数可跨 GPU、engine、length 或 SLO复现。
- **Limitations / Threats to Validity:** vendor benchmark、部分 projected numbers、early project APIs、未充分披露 failure/recovery 与 tail latency；KV-aware routing 可能造成热点。
- **Trade-offs / New Failure Modes:** state/index staleness、transfer timeout、partial pool failure、planner oscillation、KV hot spots、跨版本 layout incompatibility、network tail 放进 token path；同时获得 phase 独立扩缩容与复用机会。
- **Where the Previous Design Still Applies:** 单节点、短 prompt、高互联成本、低 prefix reuse、严格简化 failure domain 或阶段负载相近时，aggregated engine 仍合理。
- **Evolution Relationship:** `Direct Evolution`：single-engine scheduling → KV-aware distributed routing → phase/state-aware runtime；后续 docs 是同一 family 的演进证据，不是对旧方案的否定。
- **ROADMAP Node:** 主 owner `INFER-DYNAMO`（current Ch52 / legacy Ch48）；`INFER-SGLANG`、`INFER-KSERVE-LLM` 与 distributed scheduling/state chapters 为 handoff。
- **Target and Adjacent Chapters Read:** 已读 current Ch51 SGLang、Ch52 Dynamo、Ch53 KServe LLM，并核对 Ch50、Ch54～56 的 owner 边界。
- **Existing Coverage:** Ch52 已经以 request/state/control paths、KV-aware routing、KVBM/NIXL、planner 与 failure semantics 组织长期框架；但当前正文主要基于后续 docs，需要在最终 integration 时补回 2025 launch → later architecture 的演进边界。
- **Integration Decision:** `Books Pending — Refine Existing Argument`；Historical Books Gate 关闭；后续补回 2025 launch→后续三路径架构的版本边界。
- **Changed Files or Rejection Reason:** 本轮不改 Books。
- **Open Questions:** 是否能定位 2025-03 archived commit 的组件 readiness；planner 的稳定性、recovery、versioned KV layout 与跨 engine compatibility。

#### SGLang joins PyTorch ecosystem

- **Candidate / Week / Score:** SGLang joins PyTorch ecosystem / 2025-W12 / 20/30。
- **Primary Source URLs:** https://pytorch.org/blog/sglang-joins-pytorch/；https://arxiv.org/abs/2312.07104；https://github.com/sgl-project/sglang。
- **Six-dimensional Score:** 3 / 3 / 3 / 4 / 4 / 3 = **20/30**。
- **Source Family ID:** `sglang-runtime-and-pytorch-governance`。
- **Source Type:** PyTorch governance announcement + SGLang paper/repository（机制背景）。
- **First-public Date / Revision History:** 生态加入公告为 2025-03-19；核心 SGLang 论文 arXiv v1 为 2023-12-12。2025 事件没有首次提出 RadixAttention、compressed FSM 或 language-model program runtime。
- **Direct Primary Sources:** PyTorch Blog；PyTorch Ecosystem Working Group说明。
- **Related Primary Sources:** 《SGLang: Efficient Execution of Structured Language Model Programs》及 official repository，用于区分既有技术与治理事件。
- **Access and Verification Status:** Verified；公告全文与论文 architecture、program model、RadixAttention、compressed FSM、API speculative execution、evaluation、appendices 已读取。
- **Full-read Coverage:** 公告全篇；论文 introduction/related work、frontend/runtime、algorithms、evaluation/ablations/hardware、limitations 与 appendix/compiler mode。
- **Original Problem:** 本候选真正处理的是成熟开源 serving 项目的可持续治理与生态可见性，不是新的 inference bottleneck。
- **Why the Previous Design Was Reasonable:** 独立项目能快速迭代并保有技术自治；加入 ecosystem 前已可通过 repository、releases 与社区协作演进。
- **Changed Constraint:** 项目被更广泛生产采用后，需要 licensing、CI、repo health、contributors 与公开 lifecycle 等成熟性信号。
- **Mechanism:** 2025 公告没有改变 runtime mechanism。论文中的 RadixAttention 以 CPU radix tree 管理 token-prefix identity、LRU eviction 与 longest-prefix-first scheduling；compressed FSM 合并 deterministic token transitions；这些均早于公告。
- **State Ownership:** PyTorch ecosystem 拥有项目收录/治理流程；SGLang maintainers 仍拥有 runtime roadmap。runtime 内部 prefix tree、KV blocks、request/grammar state 与 scheduler ownership 不因公告自动改变。
- **Control Flow / Data Flow:** governance event 不进入 request data path；技术背景中 frontend program → runtime prefix match/schedule → KV reuse / constrained decoding → model execution。
- **Implementation Details:** 论文 runtime 以 interpreter mode 为主，另有 compiler IR；Radix tree 在 CPU，KV payload 在 device；cache-aware schedule 可能 starvation。公告列举的 2025 feature set 是项目能力快照，不是加入 PyTorch 后才产生。
- **Evaluation Setup:** 原论文覆盖 Llama-7B/A10G、Mixtral-8x7B/8×A10G、Llama-70B/4×A100-80GB、LLaVA variants 等；作者报告受 workload 与 cache hit 条件约束的 throughput improvements。公告自身无新 controlled experiment。
- **Baselines / Ablations / Sensitivity:** 原论文比较 LMQL/Guidance/vLLM 等并做 no-cache、no-tree、FCFS/random schedule、frontend hints 等 ablation；公告无新增 ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 仅原论文的模型/GPU 条件可核验；公告关于 production scale 未给完整 precision、length、arrival、concurrency、SLO，不能用于性能结论。
- **What the Evidence Actually Proves:** 2025-03 SGLang 被列入 PyTorch ecosystem；早期论文已证明在其受控 workload 下程序结构和 prefix reuse 可被 runtime 利用。
- **What It Does Not Prove:** 不证明 governance affiliation 改善 correctness、compatibility 或性能，也不证明当前 SGLang 行为等同 2023 paper implementation。
- **Limitations / Threats to Validity:** 生态标准是 maturity signal 而非技术认证；paper benchmark 已随版本和竞争系统过时；cache-aware scheduling 有 starvation，compressed FSM 可扭曲 token probability。
- **Trade-offs / New Failure Modes:** 更强治理可能扩大协作与稳定预期，但增加 process cost；技术侧 prefix reuse 增加 identity/eviction/fairness state，structured decoding 增加 tokenizer/FSM correctness。
- **Where the Previous Design Still Applies:** 独立治理仍适合早期实验项目；低共享 prefix 或无需 structured programs 时，普通 serving abstraction 仍合理。
- **Evolution Relationship:** governance 对 runtime 是 `Layering / Dependency`；SGLang paper → later releases 才是技术 evolution。
- **ROADMAP Node:** 主 owner `INFER-SGLANG`（current Ch51 / legacy Ch47）。
- **Target and Adjacent Chapters Read:** 已读 current Ch50 vLLM、Ch51 SGLang、Ch52 Dynamo。
- **Existing Coverage:** Ch51 已准确区分历史 paper abstraction 与当前通用 serving framework，并包含 identity、fairness、state adapter 边界；治理公告没有新增长期机制。
- **Integration Decision:** `Weekly Only — Governance Fact`；基金会归属不等于 runtime mechanism。
- **Changed Files or Rejection Reason:** 不改 Books；`INFER-SGLANG`（current Ch51 / legacy Ch47）保留技术 owner，治理公告仅留 Weekly。
- **Open Questions:** PyTorch ecosystem 的生命周期/退出机制怎样影响依赖风险；技术兼容仍须按具体 release 验证。

#### RWKV-7 / Goose

- **Candidate / Week / Score:** RWKV-7 “Goose” / 2025-W12 / 29/30。
- **Primary Source URLs:** https://arxiv.org/html/2503.14456v1；https://github.com/RWKV/RWKV-LM。
- **Six-dimensional Score:** 5 / 5 / 5 / 5 / 5 / 4 = **29/30**。
- **Source Family ID / Source Type:** `rwkv7-generalized-delta-state-evolution`；arXiv v1论文、官方weights/dataset listing与training/inference repository。HF推荐页只用于发现。
- **Event Date / Revision History:** arXiv:2503.14456 v1为2025-03-18；作者社区称architecture code更早公开，但论文mechanism/evaluation contract首次完整公开仍归W12。后续weights与artifact只作lineage。
- **Access / Full-read Coverage:** 已读v1 architecture、generalized delta rule与WKV kernel、World v3 dataset、pretraining/upgrade path、LM/recent-data/MQAR/MAD/long-context/state-tracking/speed-memory/multimodal experiments、theory/stability/training/kernel/ablation appendices与limitations；官方artifact用于身份与可复现边界。
- **Original Problem / Previous Design / Changed Constraint:** softmax attention保留显式KV history，检索能力强且训练kernel成熟，但decode memory随context增长；早期linear attention/RNN用固定state换取constant-memory，却以无选择累积或scalar decay混合旧信息，难以按key覆盖。长context与state tracking要求在固定state中选择性删除、写入和保留，同时不能失去parallel training。
- **Mechanism / State Ownership:** 每个head拥有matrix state。RWKV-7把delta rule扩成`diag(decay) - rank-one removal` transition：vector-valued decay与in-context learning rate按channel控制更新，removal key与replacement key解耦，value residual跨layer回接layer-0 value，current-token bonus避免必须写入state后才能读取。state update仍是diagonal-plus-rank-one，允许parallel scan；optimized CUDA kernel、precision与checkpoint conversion共同属于机制contract。
- **Control / Data Flow / Implementation:** token-shifted input产生key/value/decay/removal/learning-rate/receptance/gates → recurrent WKV state更新 → receptance读取并叠加current-token bonus → MLP。head size固定64；World models从RWKV-5/6 checkpoints映射并扩宽，新参数小初始化；3.119T-token mmap corpus以cubic finite-field mapping遍历，context4096，AdamW分组含base-decay 2× LR。
- **Evaluation Contract:** 0.1B～2.9B World/Pile models；World 1.5B/2.9B训练5.6T tokens、最多12×8 H800，bfloat16训练但World使用内部fp32 WKV kernel。LM Harness、多语/近期互联网compression、MQAR、MAD、PG19/pass-key、group multiplication、VisualRWKV与kernel benchmarks。H100 SXM kernel test固定batch8、D4096、64 heads、head64；16K forward 7.9ms是不存state的单kernel measurement，不是端到端serving SLO。
- **Baselines / Ablations / Evidence:** matched earlier-RWKV checkpoints与small-model architecture ablation支持vector decay、vector learning rate、split keys和bonus均降低loss；main LM comparisons仍混有不同tokens/datasets/distillation。2.9B pass-key约35K后下降，128K finetuning也在约50K退化；所以constant compute/state不等于infinite memory。理论证明存在常数层RWKV-7可识别regular languages，不证明训练出的2.9B LM在任意长输入保持信息。
- **Trade-offs / Failure Modes / Old Design Boundary:** 固定state降低decode memory，却产生不可寻址的compression、precision-sensitive recurrent drift、prompt/EOT sensitivity、head-dimension-specific kernels和state version/serialization问题；作者观察单step NaN需checkpoint rewind。Transformer KV在exact retrieval、prefix reuse、random access和成熟FlashAttention生态仍更合适；classical RNN理论表达更强但优化/梯度问题仍在。
- **Evolution / Owner / Disposition:** `Direct Evolution / Alternative Branch`：scalar decay linear state → delta replacement → vector gated generalized delta state。owner `MODEL-TRANSFORMER-LAYER`（Ch17），handoff `MODEL-LONG-CONTEXT`（Ch22）、`MODEL-SELF-ATTENTION`（Ch14）、`INFER-DECODE`（Ch44）与 `INFER-GPU-MEMORY`（Ch54）；读Ch16/18及Ch21/23。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。
- **What Evidence Does Not Prove / Open Questions:** 不证明RWKV替代Transformer、无限context、跨kernel numerical equivalence或生产tail latency；需验证state checkpoint/rollback、continuous batching isolation、quantization drift与larger-scale from-scratch training。

#### DAPO

- **Candidate / Week / Score:** DAPO / 2025-W12 / 29/30。
- **Primary Source URLs:** https://arxiv.org/html/2503.14476v1；https://github.com/volcengine/verl。
- **Six-dimensional Score:** 5 / 5 / 5 / 5 / 5 / 4 = **29/30**。
- **Source Family ID / Source Type:** `dapo-reasoning-rl-optimization-system`；arXiv v1、官方verl-based repository、DAPO-Math-17K artifact。HF页面只用于发现。
- **Event Date / Revision History:** 论文正文标注2025-03-17，arXiv:2503.14476 v1实际提交/first public为2025-03-18，owner W12；后续code/dataset changes为same-family evolution，不倒写event-time结果。
- **Access / Full-read Coverage:** 已读v1 PPO/GRPO/KL-removal/rule-reward背景、四项DAPO机制、dataset transformation、algorithm、training/evaluation、progressive ablation、training dynamics、case studies与appendices；论文无独立limitations/hardware section，未披露GPU类型/数量、precision、wall-clock与完整system throughput。
- **Original Problem / Previous Design / Changed Constraint:** naive GRPO以group-relative reward省去critic，结构简单；但long-CoT rollout把若干隐含系统效应放大：symmetric clipping限制low-probability token上升、全对/全错prompt产生zero advantage、sample-level averaging稀释长response token、hard truncation把正确但过长样本误罚并诱发entropy collapse。
- **Mechanism / State Ownership:** Clip-Higher把upper/lower ratio clip解耦（0.28/0.2）以保留低概率探索；Dynamic Sampling持续oversample并过滤accuracy为0或1的groups，直到batch填满有效梯度prompt；Token-level Policy Gradient按整批token而非每response先平均，使每token贡献一致；Soft Overlong Punishment在16,384～20,480 token区间连续降reward。dataset pipeline把复杂数学答案转换为integer-verifiable prompts，verifier拥有reward truth。
- **Control / Data Flow / Implementation:** 17K prompt pool → behavior policy每prompt采16条 → rule verifier与length shaping → 丢弃zero-variance groups并补采 → group-normalized advantage → token-level clipped update。Qwen2.5-32B base、verl、AdamW constant LR 1e-6、20-rollout warmup、prompt batch512、mini-batch512/16 updates；evaluation temperature1.0/top-p0.7，AIME24重复32次报告avg@32。
- **Evaluation / Ablation Contract:** 单一math domain与AIME24；progressive table从naive GRPO 30，经overlong filtering36、clip-higher38、soft punishment41、token-level42、dynamic sampling50。该顺序证明特定组合的增量，不是完整factorial ablation；DeepSeek-R1-Zero-Qwen-32B 47来自不同训练实现，不能把50直接解释成算法普遍优越。Dynamic Sampling增加rollouts但减少steps，论文只称wall time未显著增加，未给出硬件/利用率/总sample cost。
- **What Evidence Proves / Does Not Prove:** 证明在作者Qwen32B/math/verifier设置下，rollout admission、loss normalization、clip范围与length reward必须联合设计，且train reward与validation accuracy可能脱钩。未证明四技巧跨模型、domain、noisy reward、process reward或human preference同样有效；“reflection emergence”只是qualitative trajectory，不证明faithful reasoning机制。
- **Trade-offs / Failure Modes / Old Design Boundary:** filtering zero-variance groups提高有效梯度，却改变prompt distribution并可能长期排除过难/过易能力；token-level loss让长response拥有更多总权重；soft length reward把latency budget写进objective；integer transformation可能改变原题语义。naive GRPO在短输出、均衡difficulty或rollout预算紧张时仍更简单，PPO/critic在dense temporal credit时仍有价值。
- **Evolution / Owner / Disposition:** `Direct Evolution / System Refinement`：GRPO sample-group objective → rollout admission control → asymmetric exploration clip → token-weighted loss → soft length contract。owner `TRAIN-GRPO`（Ch33），handoff `TRAIN-PPO`（Ch32）、`TRAIN-DISTRIBUTED-TRAINING`（Ch36）与 `PLATFORM-MONITORING`（Ch67）；读Ch32/34。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。
- **Open Questions:** 需要event-time artifact commit、GPU/precision/wall-clock、rollout duplication与prompt-selection bias；需要将entropy/length/effective-prompt ratio纳入可复现实验和production policy ledger。

#### R1-VL / StepGRPO

- **Primary Source URLs:** https://arxiv.org/html/2503.12937v1。
- **Six-dimensional Score:** 4 / 5 / 5 / 5 / 5 / 3 = **27/30**。
- **Identity / access:** arXiv:2503.12937唯一v1为2025-03-17，HF于3月18日推荐；2025-W12，27/30，`r1-vl-stepgrpo-multimodal-process-reward`。已读v1的SFT/GRPO背景、warm-up、StepRAR/StepRVR、optimization、8-benchmark evaluation、reward/rollout ablations与discussion；论文无独立limitations或artifact appendix，code在v1只承诺future availability。
- **Problem / mechanism:** outcome-only GRPO在弱MLLM上只有少量正确rollouts，group reward稀疏且方差大。StepGRPO先用Mulberry-260K做CoT warm-up，再从其中10K做online RL；GPT-4从reference CoT抽取/扩写key equations/variables，StepRAR按soft match比例加到answer reward，StepRVR只在response包含image/background analysis→reasoning steps→final answer的固定顺序时给1。每prompt M=4 rollouts，用group-normalized reward和KL-to-reference更新Qwen2-VL。
- **State / Control Flow / Implementation:** reference CoT与key-step list是teacher-owned evidence，rule verifier拥有格式/step-match reward，policy rollout拥有mutable reasoning trajectory，GRPO optimizer只消费group-normalized advantage。data flow为Mulberry warm-up → 10K prompt online sampling → StepRAR/StepRVR + answer reward → group normalization/KL update；因此实现依赖teacher extraction、string matcher、rollout admission与reference-policy version，而非单一loss公式。
- **Evidence contract:** Qwen2-VL 2B/7B，4×H100-80GB；warm-up batch128，RL batch4、LR1e-6、KL beta0.04。MathVista、MMStar、Math-V、ChartQA、DynaMath、HallusionBench、MathVerse、MME八项；7B平均53.3→GRPO51.4→StepGRPO57.1。MathVista ablation为warm-up58.2→61.2，分别加StepRAR/StepRVR为62.4/61.9，两者63.5；M增大可稳定baseline但提高rollout成本。未披露precision、rollout length、wall-clock、verifier false match和跨dataset contamination。
- **Boundary / Trade-off / Owner / Disposition:** 它把dense process signal换成便宜的可执行字符串/格式规则，却依赖teacher-derived key steps、reference CoT completeness和结构模板；匹配到equation不等于因果正确，固定“先分析后答案”还可能奖励格式服从而非faithful reasoning。PRM在开放语言、非符号步骤下仍更灵活，outcome reward在verifier强且base exploration足够时更便宜。`Alternative Branch`；owner `TRAIN-GRPO`（Ch33），handoff `MULTIMODAL-REPRESENTATION`（Ch23）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch32/34。`Books Pending — Experimental`，Historical Books Gate关闭。

#### VideoMind / Chain-of-LoRA

- **Primary Source URLs:** https://arxiv.org/html/2503.13444v1；https://videomind.github.io/。
- **Six-dimensional Score:** 4 / 5 / 5 / 5 / 5 / 4 = **28/30**。
- **Identity / access:** arXiv:2503.13444唯一v1为2025-03-17，HF于3月18日推荐；2025-W12，28/30，`videomind-chain-of-lora-temporal-workflow`。已读v1 role workflow、timestamp decoder、moment MCTS/verifier、Chain-of-LoRA、datasets/training、14-benchmark evaluation、role/memory/search ablations、prompts与limitations；official project/repository用于artifact identity。
- **Problem / mechanism:**把整段长视频一次压入QA模型，会让相关moment被大量无关frames淹没；部署四个专用模型又复制weights。Planner按query选择direct answer、grounding或ground+verify计划；Grounder用每frame pooled visual tokens、`<REG>` query和temporal pyramid预测top-5 intervals；Verifier逐个zoom-in并输出boolean/special-token score，Answerer只读选中segment。Planner/Grounder/Verifier各用rank64 LoRA挂在同一Qwen2-VL base上，role切换只替换adapter，形成Chain-of-LoRA。
- **State / Control Flow / Implementation:** shared base checkpoint拥有通用视觉语言state，各rank-64 LoRA拥有role-specific delta；orchestrator持有plan、top-5 interval candidates、verification scores和selected segment，video frames本身保持immutable evidence。请求流为query→Planner→Grounder temporal proposals→Verifier逐段zoom/reject→Answerer；每次role切换都要锁定adapter revision、frame sampling与segment identity，不能把多个角色输出视为同一模型一次forward。
- **Evidence contract:**2B/7B base；Planner39K、Grounder210K、Verifier232K SFT samples，后两者含由Grounder predictions生成的verify data；角色分别限制100/150/64/32 frames和64/64/64/256 tokens-per-frame，Grounder 1FPS、其余2FPS。14 benchmarks跨grounded QA、temporal grounding和general QA；role ablation与Chain-of-LoRA/All-in-One/4-copy Distributed比较。2B memory 4.2GB vs distributed16.6GB且表中accuracy相同，但没有端到端latency、adapter-switch、MCTS branch count、energy或P99 SLO。
- **Evidence boundary / trade-off:** Grounder+Verifier显著改善temporal localization，Chain-of-LoRA证明共享base可复用不同role deltas；但workflow会多次decode/re-encode video，top-5 grounder recall限制verifier上限，同源synthetic verifier data会继承grounder bias。special-token verifier优于textual/direct是一项受限ablation，不是通用verification结论；TACoS等数据已进入pretraining，不能称纯zero-shot。短视频/direct QA或严格latency场景下单pass/all-in-one仍合理。
- **Owner / disposition:** `Layering / Workflow Evolution`：single-pass QA → temporal proposal → verify/zoom → answer，参数侧single multi-task model → distributed copies → shared base + role LoRAs。owner `AGENT-WORKFLOW`（Ch81），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-LORA`（Ch30）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch80/82。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。

#### MicroVQA

- **Primary Source URLs:** https://arxiv.org/html/2503.13399v1。
- **Six-dimensional Score:** 4 / 4 / 4 / 5 / 5 / 4 = **26/30**。
- **Identity / access:** 2025-W12，26/30，`microvqa-expert-microscopy-reasoning-evaluation`；arXiv:2503.13399唯一v1为2025-03-17，HF于3月18日推荐。已读v1的task taxonomy、expert VQA collection/QC、two-stage MCQ/RefineBot、15-model evaluation、attribute/error analyses、ethics/limitations、data/contamination/prompt/model/human-trace appendices与artifact schema。
- **Problem / mechanism:**通用science exams偏语言知识，classification-derived microscopy benchmarks又不测hypothesis/experiment design。12名biology experts用30～40分钟/题创建1,042 raw VQA，覆盖expert visual understanding、hypothesis generation、experiment proposal；60%+为multi-image。Stage1以50个physician-reviewed gold MCQs优化prompt；Stage2 RefineBot让GPT-4o在无图条件下尝试答题、反思language shortcut、重写distractors，再由Claude/GPT检查meaning preservation，最多5轮。
- **State / Control Flow / Implementation:** source images与expert question/answer是authoritative evidence，RefineBot只拥有candidate distractors和shortcut diagnosis，Claude/GPT checker拥有meaning-preservation gate，dataset registry在最多5轮后commit accepted MCQ。流程明确把“题目是否需要视觉证据”和“模型是否答对”分开；canary、publication date与image provenance属于artifact identity，不能由模型评分替代。
- **Evidence contract:**1,042 questions、255 image sets、31 organisms、33 areas、3 microscopy modalities；数据为原创或2024-01后open-access并嵌canary。15个event-time model versions，fixed CoT prefix/regex parsing；o1最高52.8，human baseline50.3但human protocol并非expert ceiling。Stage2使models相对降35～42%，用于RefineBot的GPT/Claude families多降不到10 points，说明adversarial constructor bias。三位专家只审Claude Sonnet 30 samples：50% perception、30% knowledge、13% overgeneralization、7%其他；样本小，不能外推所有models。
- **Boundary / Trade-off / Owner / Disposition:** expert curation提高task authenticity，却仍是MCQ；RefineBot只消除当前models能发现的shortcut，未来models可重开。MCQ creator/model-family coupling、open-vs-closed gap、dataset scale和microscopy scope限制外推；specialist LLaVA-Med较base高4.5只说明重叠scientific corpus相关，不证明domain finetune普遍有效。专家制作与反shortcut迭代提高证据质量，也显著增加成本并把judge-family bias写入benchmark。AI for Science应将perception、knowledge、hypothesis和experiment proposal分别验收，不能用总accuracy授权autonomous experimentation。`Evaluation Refinement / Domain Composition`；owner `PLATFORM-EVALUATION-SYSTEM`（Ch66），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`AGENT-WORKFLOW`（Ch81）与 `PLATFORM-SECURITY`（Ch72）；读Ch65/67。`Books Pending — Refine Existing Argument Candidate`，Historical Books Gate关闭。

#### R0 / Rewards Are Enough

- **Candidate / Week / Score:** R0（v1标题“Rewards Are Enough for Fast Photo-Realistic Text-to-image Generation”）/ 2025-W12 / 28/30。
- **Primary Source URLs:** https://arxiv.org/html/2503.13070v1。
- **Six-dimensional Score:** 5 / 5 / 5 / 4 / 5 / 4 = **28/30**。
- **Source Family ID / Source Type:** `r0-reward-centric-few-step-generation`；arXiv v1论文与作者repository。2025-06-09 v2改名为“Reward-Instruct”，属于同一family的later revision，不改变W12 owner。
- **Event Date / Revision History:** arXiv:2503.13070 v1于2025-03-17 first-public；v2为2025-06-09。本文锁定v1机制与实验；当前repository只验证lineage并明确code仍为“coming soon”，不能作为event-time executable artifact。
- **Access / Full-read Coverage:** 已读v1 Abstract、Introduction、diffusion/reward-distillation背景、problem reformulation、generator parameterization、weight/LoRA/random-eta/multi-reward regularization、R0/R0+算法、SD1.5/SD3实验、metrics、high-resolution classifier、discussion与references。v1没有独立limitations/appendix，也未披露训练硬件、precision、batch、wall-clock、reward-query cost或端到端latency。
- **Original Problem / Previous Design / Changed Constraint:** diffusion distillation以trajectory/distribution matching保留pretrained data prior，在少步生成中是合理的稳定器；但强text condition与preference reward使reward gradient在作者复现中压过distillation gradient，同时online score/distillation增加memory与compute。约束从“逼近完整conditional density”转向“在少步预算内满足复杂条件”，作者因而把目标重写为regularized reward maximization。
- **Mechanism / State Ownership:** K-step generator由pretrained diffusion score network初始化；terminal image经HPS v2.1、ImageReward与CLIP/implicit-CFG等多个reward反向传播。pretrained weights拥有image-manifold prior，L2-to-initial-weights或LoRA限制参数漂移；每步随机eta扩展生成路径；各reward按image-gradient norm动态归一化。R0在最终样本给reward，R0+随机选择intermediate step、stop-gradient截断此前路径，并从该步预测clean image接受监督，以缩短反向图。
- **Control / Data Flow / Implementation:** JourneyDB只提供prompts；noise经过四个parameterized denoising transformations生成image → 多reward与CFG计算normalized gradients → 加权weight regularization → 更新generator。所谓“image-free”只表示post-training不读取真实images；generator initialization、CFG与high-resolution guidance仍继承预训练diffusion从images学到的prior，因此不能解释为rewards独立创造图像分布。
- **Evaluation Contract:** SD-v1.5/Realistic-Vision与SD3-Medium，4-step生成；Hyper-SD public checkpoint，RG-LCM/DI++由作者复现。HPS v2.1、Aesthetic、CLIP、ImageReward及COCO-5K zero-shot FID。SD1.5 R0/R0+的HPS为33.70/34.37，高于base 30.19；但FID为33.79/37.53，差于base 29.11。SD3 R0 HPS 34.04、FID 31.97，相对base为31.37/28.72。结果说明reward-aligned metrics与distribution metric发生分叉，不支持“全面质量提升”。
- **Baselines / Ablations / Sensitivity / Overhead:** ablations显示去掉weight regularization会collapse，单reward会过饱和，多reward与gradient normalization改善作者指标；R0+在1K HPS prompts上收敛更快。没有matched training compute、seed/CI、human evaluation、reward holdout、independent evaluator、reward-correlation test或完整memory/throughput数字；训练指标直接复用优化reward families，存在evaluation circularity。
- **What Evidence Proves / Does Not Prove:** 论文支持在作者两个pretrained backbones、few-step和所选reward条件下，expensive distillation loss可以被更直接的prior-preserving regularization替代。它不证明rewards足以学习unconditional image manifold，也不证明多个reward的bad modes独立；共同dataset/model bias可能形成shared exploit。更高HPS/ImageReward不等于更真实、多样或更接近data distribution，FID退化正是反例。
- **Trade-offs / Failure Modes / Old Design Boundary:** 删除distillation简化post-training，却把correctness交给reward coverage、gradient conflict和pretrained prior；新增reward hacking、mode collapse、metric overfitting、reward-version drift与多reward权重治理。weight anchoring提高稳定性但限制新分布适应；R0+减少backprop路径却用局部clean prediction替代全trajectory credit。reward弱、条件宽、diversity/coverage重要或缺可信evaluator时，distribution/trajectory distillation仍更合理。
- **Evolution / Owner / Disposition:** `Alternative Branch / Principle Reuse`：diffusion modeling → reward-enhanced distillation → pretrained-prior-constrained reward maximization → intermediate-step reward supervision。owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `TRAIN-RLHF`（Ch31）、`TRAIN-GRPO`（Ch33）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/25与Ch30/32/65/67。`Books Pending — Experimental / Reward-model Circularity`；Historical Books Gate关闭。
- **Open Questions:** 需要event-time code、GPU/precision/batch/wall-clock、reward-query cost、matched-compute baseline、independent human/holdout evaluation、diversity/recall指标与shared reward-bias stress test；还需解释v2是否改变了核心mechanism或只重命名/补实验。

#### Edit Transfer

- **Candidate / Week / Score:** Edit Transfer / 2025-W12 / 23/30。
- **Primary Source URLs:** https://arxiv.org/html/2503.13327v1；https://cuc-mipg.github.io/EditTransfer.github.io/；https://github.com/CUC-MIPG/Edit-Transfer。
- **Six-dimensional Score:** 4 / 4 / 3 / 4 / 4 / 4 = **23/30**。
- **Source Family ID / Source Type:** `edit-transfer-visual-relation-in-context`；arXiv v1论文、作者project page与later public repository。聚合推荐页只用于发现。
- **Event Date / Revision History:** arXiv:2503.13327 v1于2025-03-17 first-public；v2为2025-07-01。W12 review锁定v1正文；当前repository提供training data/config/checkpoint与代码，但不能倒写成2025-03-17同步artifact。
- **Access / Full-read Coverage:** 已读v1 Introduction、TIE/RIE/visual-ICL related work、DiT/MMA与four-panel method、CFM objective、training/evaluation、dataset/finetuning/inference/baseline/VLM/user-study appendices、discussion与limitations；联读project page和current repository以核验artifact lineage。
- **Original Problem / Previous Design / Changed Constraint:** text instruction适合语义编辑，却难精确表达姿态、视角等non-rigid geometry；single reference适合style/appearance，却没有显式source→target relation。约束从“描述目标结果”转为“从一个input-output demonstration抽取变换并迁移到新input”，需要同时表示example relation、query identity与待生成slot。
- **Mechanism / State Ownership:** source、edited target、query source和query target被排成2×2 composite并编码到统一visual-token sequence；前三格作为clean conditional tokens，右下target tokens加noise。FLUX DiT的bidirectional multimodal attention让四格共享关系上下文，rank-16 LoRA只在task-specific路径更新；conditional flow matching训练模型从noisy target恢复query edit。关系不是显式symbolic operator，而是由composite layout、attention与LoRA共同承载的implicit transformation state。
- **Control / Data Flow / Implementation:** FLUX.1-dev合成two-panel pairs → 人工按identity、front view、单一变换与alignment筛选 → 两个同type pairs组成一张four-panel training image → 21 edit types、每类2例 → 6,000 iterations。测试时example source/target与query source保持clean，query target从noise经35 denoising steps生成。single A100-40GB、Adam、LR 1e-4、batch4、约16小时；v1未披露precision、seed、inference latency或memory。
- **Evaluation Contract:** P2P、RF-Solver-Edit与MimicBrush三类不完全同接口baseline；TIE prompt由GPT-4o生成再人工修订，RIE只接收target reference。CLIP-T/CLIP-I/PickScore、GPT-4o LMM Score与198 pairwise tasks；论文报告各维度对baseline偏好率超过80%，但未披露participant count、per-type denominator、confidence interval、inter-rater agreement或held-out benchmark construction。
- **Ablations / Sensitivity / Evidence:** 10 edit types ×1 example失败、×2成功，扩展到21 types改善作者qualitative cases；no-finetune FLUX只捕捉部分pose，说明LoRA承担task learning而非纯test-time in-context induction。text与visual example冲突时输出会混合或随机服从一方；低层color transfer失败，说明relation representation偏向训练集中human-centric spatial transformations。
- **What Evidence Proves / Does Not Prove:** 支持“把多个视觉角色编码为一个有位置语义的token canvas，可让生成模型学习source-target relation”这一受限机制；不证明从任意single pair即时学习新operator，因为模型先在21种手工编辑type上finetune。跨species与composition主要是selected qualitative evidence；CLIP/GPT-4o metrics也不等于精确geometry或identity preservation。
- **Trade-offs / Failure Modes / Old Design Boundary:** composite canvas避免新增relation encoder，换来quadratic token interaction、固定panel convention、resolution dilution与layout shortcut；人工对齐样本提高sample efficiency，却缩窄distribution。text/visual control缺priority或conflict resolver，生成结果不可预测。text editing在目标可语言化、成本敏感时仍简单；reference appearance methods在color/texture/local identity transfer上仍更合适；显式pose/keypoint/flow control在需要可验证geometry时更可靠。
- **Evolution / Owner / Disposition:** `Principle Reuse / Alternative Branch`：text instruction → appearance reference → source-target visual demonstration → unified token canvas + task LoRA。owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `TRAIN-LORA`（Ch30）；读Ch22/24与Ch29/31。`Books Pending — Experimental Representation Case`；Historical Books Gate关闭。
- **Open Questions:** 需要event-time artifact commit、participant/sample accounting、unseen transformation split、explicit geometry metric、identity/background preservation、panel-order/layout ablation、precision/latency/memory与cross-backbone reproduction；还需区分v2和current code对v1 result的真实补强范围。

#### BlobCtrl

- **Candidate / Week / Score:** BlobCtrl / 2025-W12 / 27/30。
- **Primary Source URLs:** https://arxiv.org/html/2503.13434v1；https://liyaowei-stu.github.io/project/BlobCtrl/；https://github.com/TencentARC/BlobCtrl。
- **Six-dimensional Score:** 5 / 4 / 4 / 4 / 5 / 5 = **27/30**。
- **Source Family ID / Source Type:** `blobctrl-probabilistic-element-representation`；arXiv v1、project page、2025-03-20 inference-code release与later SIGGRAPH Asia v2/repository lineage。
- **Event Date / Revision History:** arXiv:2503.13434 v1于2025-03-17 first-public，原题为统一element-level generation/editing；official repository记录2025-03-20 release inference code，同属W12。v2于2025-10-01 major rewrite并改题为“Taming Controllable Blob for Element-level Image Editing”，不得倒写v1 claim/evaluation。
- **Access / Full-read Coverage:** 已读v1 blob/ellipse/Gaussian公式、opacity/composition/splatting、dual-branch architecture、self-supervised construction、identity loss/dropout、dataset/benchmark/training/baseline/human evaluation、ablations、limitations与全部appendices；project/current repository用于核对release timeline、environment与artifact lineage。
- **Original Problem / Previous Design / Changed Constraint:** bounding box/ellipse grounding保留layout但压缩identity，reference token保留appearance却缺continuous spatial control，mask/drag editing又依赖paired/video data并容易破坏background harmony。创作工作负载要求同一element在move/resize/replace/remove/compose间保持identity，同时layout可连续调整并支持多轮操作，必须把where、what与appearance分成可组合state。
- **Mechanism / State Ownership:** blob以2D Gaussian/ellipse的mean、covariance/axes与rotation拥有layout state；Mahalanobis-derived opacity和depth-aware alpha composition处理soft boundary/occlusion，DINO features经blob splatting承载spatial semantics，VAE latent承载appearance。foreground branch移除cross-attention并处理opacity+DINO+VAE，background branch保留text cross-attention与scene context；zero-initialized hierarchical fusion拥有两branch的commit point。
- **Control / Data Flow / Implementation:** BrushData mask经resolution/area/boundary过滤 → ellipse fit与Gaussian conversion → InternVL-2.5 caption形成1.86M BlobData。训练把真实target位置视为结果，随机生成source blob模拟移动；augmentation阻止copy-paste，foreground-region noise loss强化identity，lambda从1.0降至0.6把后期权重转向harmonization。branch/semantic/VAE dropout在训练中暴露控制路径，inference用fusion strength与control timestep在fidelity/diversity间调节。
- **Evaluation Contract:** SD1.5，512×512；foreground full finetune、background LoRA rank64，24×V100训练7天，batch192、Adam LR1e-5、weight decay0.01。BlobBench仅100 images、五类operation；CLIP-I/DINO、SAM-fit layout MSE、PSNR/SSIM/LPIPS/FID以及30人×20 sets的1–5评分。v1未披露precision、seed/CI、inference latency、multi-round accumulated error或per-operation human uncertainty。
- **Baselines / Ablations / Evidence:** GliGen、AnyDoor、Magic Fixup需被适配为五种workflow；尤其GliGen clean background由BlobCtrl removal生成，比较不是完全independent。作者表中BlobCtrl平均identity/layout指标较强，但benchmark和method由同一团队构建；FID为102.8虽优于adapted baselines，绝对值不能解释为普遍高保真。feature组合与identity loss ablation主要为qualitative/loss evidence；缺full factorial、matched parameter/compute与external benchmark。
- **What Evidence Proves / Does Not Prove:** 支持“用typed intermediate representation显式拆分layout、semantics、appearance，再由dual-branch fusion重新commit”这一长期机制；不证明Gaussian blob优于mask/keypoint/flow的所有任务，也不证明训练中feature separation形成因果disentanglement。single forward只支持iterative single-element operation，论文没有证明真正joint multi-element editing或长链一致性。
- **Trade-offs / Failure Modes / Old Design Boundary:** blob把位置控制变为低维连续参数，代价是复杂shape压缩、mask-to-ellipse information loss、depth ordering和overlap ambiguity；DINO/VAE/opacity三套state带来identity/version compatibility，dual backbone增加memory/compute。soft blob利于harmonization，却不适合pixel-exact boundary。boxes在粗layout、masks在exact silhouette、keypoints/flow在articulated geometry、直接text editing在无需identity锁定时仍更合适。
- **Evolution / Owner / Disposition:** `Direct Evolution / Layering`：discrete grounding token → identity reference → typed blob layout/semantic/appearance state → foreground/background staged fusion。owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、`TRAIN-DATA`（Ch27）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch22/24、Ch26/28与Ch65/67。`Books Pending — Refine Existing Argument Candidate`；Historical Books Gate关闭。
- **Open Questions:** 需要event-time commit、v1 BlobData/BlobBench availability、license/provenance、multi-object joint operation、multi-round drift、exact mask/flow baselines、matched compute、precision/latency/memory、external benchmark与state serialization contract；v2 major rewrite须作为same-family evolution另行核对。

#### WideRange4D / Progress4D

- **Candidate / Week / Score:** WideRange4D / Progress4D / 2025-W12 / 22/30。
- **Primary Source URLs:** https://arxiv.org/html/2503.13435v1；https://github.com/Gen-Verse/WideRange4D。
- **Six-dimensional Score:** 4 / 3 / 3 / 4 / 4 / 4 = **22/30**。
- **Source Family ID / Source Type:** `widerange4d-progressive-dynamic-reconstruction`；arXiv v1论文、作者repository与later dataset page。benchmark与baseline method属于同一family但保留不同evidence role。
- **Event Date / Revision History:** arXiv:2503.13435 v1于2025-03-17 first-public；v2为2025-04-29。W12锁定v1 method/benchmark；current repository的47-commit implementation和dataset link只作artifact lineage，不能证明event-time availability。
- **Access / Full-read Coverage:** 已读v1 4D dataset/reconstruction related work、WideRange4D categories/statistics/acquisition、3DGS/deformation formulation、Progress4D algorithm、training/baselines/results/ablation、UE construction与algorithm appendices；联读current repository的environment、data schema、training/render/evaluation入口。
- **Original Problem / Previous Design / Changed Constraint:** deformation-field 4DGS在人物原地动作上合理：canonical 3D state与小位移可由MLP平滑变形。但对象跨大范围移动时，单次随机初始化既难得到完整3D foreground，也让远时刻deformation远离anchor并累积blur。约束从局部连续形变变成大位移、长路径、天气与遮挡共同变化，需要先稳定scene state，再逐步扩大temporal fitting frontier。
- **Mechanism / State Ownership:** Stage 1以multi-view supervision优化3D Gaussian位置、covariance、opacity与color，随后freeze为stable scene owner。Stage 2把timesteps分为已对齐T0、当前T1与未来T2；deformation MLP只拟合T1，完成后commit到T0，再从T2引入邻近timesteps。alignment loss按temporal distance与deformation magnitude加权，让新state靠近最近stable anchor；这是curriculum/continuation method，不是新的causal transition model。
- **Control / Data Flow / Implementation:** UE assets、rig/IK与spline trajectories组成synthetic scenes；40 camera viewpoints、每视角60–150 frames（supplement另称60 synchronized sequences），SfM/3DGS初始化 → freeze → progressive timestep admission → L1+TV+alignment optimization。每1,000 iterations更新T0/T1/T2；每task单RTX4090，实验使用8×4090，Adam LR1.6e-4。v1未披露总scene/case数、total iterations、wall-clock、precision、memory或完整user-study protocol。
- **Evaluation Contract:** 作者自建WideRange4D同时评价作者Progress4D；每case 40 views，metrics为L1/PSNR/SSIM/LPIPS。4DGS/ST-4DGS使用multi-view contract，DreamScene4D/SC4D是monocular input，只在其输入view比较并加background mask，因此Table 1不是统一input-resource comparison。Progress4D报告PSNR 28.86，baseline最高26.35；无seed/CI、per-scene分布、training cost或external benchmark。
- **Ablations / Sensitivity / Evidence:** 唯一明确ablation是去掉alignment loss的qualitative deterioration；high-quality initialization没有独立matched quantitative ablation，progressive admission、freeze、loss weighting与threshold未做factorial/sensitivity。benchmark scene/motion realism经user study过滤，但参与者、问题、阈值与拒绝率未披露；synthetic UE 资产、相机与轨迹降低真实capture noise，也可能让方法适配其生成结构。
- **What Evidence Proves / Does Not Prove:** 支持“当optimization跨度过大时，先冻结高质量anchor，再按难度/距离推进mutable frontier”这一通用curriculum principle，也证明local-motion benchmark会隐藏大位移failure。它不证明模型学得action-conditioned world dynamics、counterfactual或uncertainty；这是observed multi-view sequence reconstruction，不是可控World Model。较高render metrics也不证明物理因果或真实部署generalization。
- **Trade-offs / Failure Modes / Old Design Boundary:** progressive fitting降低一次性优化难度，却引入order dependence、anchor bias、错误commit后向后传播与更长training；freeze 3D state保护quality，也可能阻止纠正初始geometry。deformation field在short/local motion、数据充分且需并行训练时仍更简单；tracking/segmentation路线在monocular输入下承担不同information contract，不能因较低分数被直接否定。
- **Evolution / Owner / Disposition:** `Principle Reuse / Experimental Reconstruction Branch`：single canonical deformation → high-fidelity frozen anchor → progressive mutable temporal frontier。owner `MULTIMODAL-WORLD-MODELS`（Ch25），handoff `MULTIMODAL-REPRESENTATION`（Ch23）、`TRAIN-PRETRAINING`（Ch28）与 `PLATFORM-EVALUATION-SYSTEM`（Ch66）；读Ch23/24/26、Ch27/29与Ch65/67。`Books Pending — Experimental State-reconstruction Case`；Historical Books Gate关闭。
- **Open Questions:** 需要event-time code/data commit、scene/case denominator、asset licenses、real-capture split、participant/protocol、full curriculum ablation、threshold/order sensitivity、seed/CI、precision/memory/wall-clock以及matched-input baseline；还需解释v2与current repository是否修正v1算法/数据矛盾。

#### Impossible Videos / IPV-Bench

- **Primary Source URLs:** https://arxiv.org/html/2503.14378v1；https://showlab.github.io/Impossible-Videos/。
- **Candidate / Week / Score:** Impossible Videos / 2025-W12 / 4/4/4/5/5/4 = **26/30**。
- **Source / Date / Revision:** Source Family `impossible-videos-ipv-bench`；arXiv:2503.14378 v1，first-public 2025-03-18；project page `https://showlab.github.io/Impossible-Videos/`。本包锁定 v1；后续数据或模型版本只能作 lineage，不能倒写 W12。
- **Problem / Previous Design / Changed Constraint:** 传统 video benchmark 主要检查真实世界动作、视觉质量或物理一致性；这对普通视频理解合理，却无法区分模型是在复现训练分布，还是能按指令生成并解释违反物理、生物、地理或社会规律的 counterfactual sequence。约束转为同时检验“打破规律”和“忠实遵循指定异常”。
- **Mechanism / State / Flow:** IPV taxonomy 有 4 domains、14 categories；IPV-Txt 保存 260 个 impossible prompts，IPV-Vid 保存 902 个筛选并标注的视频。数据流为 taxonomy/LLM/crowd prompts → 人工清晰度、相关性、可视化过滤 → 10 个 T2V 模型生成 2,600 videos + web collection + matched real videos → human annotation → generation/understanding tasks。benchmark owner 是 typed prompt、video provenance、taxonomy label 与 explanation，不是模型内部 world state。
- **Implementation / Evaluation Contract:** generation 同时测 visual quality 与 GPT-4o impossible-prompt following，IPV score 为两者组合；理解侧含 real/synthetic judgment、MCQA 与 explanation，强调 temporal anomaly。GPT-4o 三步 judge（抽取异常、ground、确认关键元素）在作者样本 human alignment 0.80，对 basic prompt 为 0.72；10 个 generation models 与多种 Video-LLM 参与，部分模型只以 1 FPS 取帧。
- **Evidence / Boundary:** 证据显示受测模型常生成视觉可接受但未实现指定反事实的视频，Video-LLM 对 temporal impossible event 也弱；它不证明“impossible video performance”等于 general reasoning/world-model quality。benchmark、prompt taxonomy、judge 与模型可能共享语言先验；生成视频来自模型与网络筛选，hardware、precision、latency、cost、confidence intervals 及真实开放分布未完整披露。
- **Trade-offs / Failure Modes / Old Design Boundary:** 反事实 prompt 扩大测试空间，却引入 judge policy、异常定义文化依赖、synthetic artifact shortcut 与 visual-quality/prompt-following乘积的可解释性问题。真实世界 benchmark 在安全、物理一致性和普通分布仍不可替代；IPV 是 alternative stress branch，而非 successor。
- **Owner / Disposition / Open Questions:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `MULTIMODAL-WORLD-MODELS`；`Books Pending — Refine Existing Argument`。需外部 benchmark reproduction、固定 model versions、per-category uncertainty、human protocol与是否能隔离 low-level artifact shortcut。

#### Creation-MMBench

- **Primary Source URLs:** https://arxiv.org/html/2503.14478v1。
- **Candidate / Week / Score:** Creation-MMBench / 2025-W12 / 4/4/4/5/4/4 = **25/30**。
- **Source / Date / Revision:** Source Family `creation-mmbench-context-aware-creativity`；arXiv:2503.14478 v1，first-public 2025-03-18；v1 HTML全文为直接证据。后续 leaderboard/model updates 不回写 event-time table。
- **Problem / Previous Design / Changed Constraint:** 传统 MLLM benchmark偏 closed-form factual QA，creative-writing benchmark又常是 text-only；两者都无法同时要求模型读取视觉事实、保持 role/background/requirements，并产出可评价的开放创意回答。约束从单一 correctness 变为 creative quality 与 visual factuality 的双重合同。
- **Mechanism / State / Flow:** 51 tasks 分为 literary writing、common/professional functional writing、creative multimodal understanding，每 task 15 cases，共 765。每 case 的 state 包括 images、Role、Background、Instruction、Requirement，以及 instance-specific general subjective criteria 与 visual factuality criteria；annotator cross-verification + expert review后 commit benchmark。text-only variant 用图像描述替换视觉输入，用于分离 base LLM 与 visual instruction tuning 影响。
- **Implementation / Evaluation Contract:** VLMEvalKit、greedy decoding、max output 4096；评 20 个 MLLM。GPT-4o judge 给 visual factuality 1–10，并与 GPT-4o-1120 baseline 做五档 pairwise comparison；交换 A/B 位置的 Dual Evaluation 减少 position bias。GPT-4o judge在人类对齐比较中 MAE/consistency较优；Qwen2.5-VL-7B从 text LLM 的 VFS/Reward `8.18/-19.18` 到 vision+text `7.55/-29.80`，作者据此提出 multimodal adaptation trade-off。
- **Evidence / Boundary:** 证明开放创意任务需要把 subjective quality 与 visual evidence 分开，并在该 judge policy 下多种 MLLM 落后闭源模型；不证明 visual tuning 必然降低创造力，因为 VLM/base LLM 的训练、prompt和架构不是严格 matched，且 image descriptions由GPT-4o生成。judge与reference baseline同源、765 cases和人工 criteria 选择限制外推；无硬件、吞吐、P99、成本。
- **Trade-offs / Failure Modes / Old Design Boundary:** instance-specific rubrics提高可解释性却增加维护成本与 evaluator coupling；pairwise reward依赖参考模型，reference升级会产生 version drift。closed-form benchmark仍适合 reproducible correctness，text-only creativity仍适合隔离语言能力；本工作是 evidence-layer extension。
- **Owner / Disposition / Open Questions:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-SFT`；`Books Pending — Refine Existing Argument`。需 independent judges、人类一致性、matched visual-tuning ablation、criteria provenance与版本锁定。

#### DeepPerception v1 / later KARL family

- **Primary Source URLs:** https://arxiv.org/abs/2503.12797；https://arxiv.org/pdf/2503.12797v1。
- **Candidate / Week / Score:** DeepPerception / 2025-W12 / 5/5/5/5/5/3 = **28/30**。
- **Source / Date / Revision:** Source Family `deepperception-kvg-cognitive-visual-grounding`；arXiv:2503.12797 v1，first-public 2025-03-17，16-page v1 PDF为直接证据；later KARL/v3 属同 family evolution，不得把后续重命名或实验倒写 v1。
- **Problem / Previous Design / Changed Constraint:** ordinary grounding用通用类别或 referring expression定位目标，直接 SFT在类别视觉差异明显时合理；KVG要求先调用 domain knowledge 区分同类细粒度实体，再输出 bounding box，zero-shot CoT甚至会退化。约束变为 knowledge retrieval、视觉比较和空间 commit 必须在一条可执行轨迹中协同。
- **Mechanism / State / Flow:** data engine把FGVR数据组成含至少2个同类实体的 composite image，Qwen2-VL-72B依据 GT entity/bbox生成 knowledge-integrated CoT。Stage 1用25K samples做Qwen2-VL-7B CoT-SFT；Stage 2从4K filtered instances采 group outputs，以 GRPO 的 group-relative advantage训练，reward为 IoU thresholded continuous reward + format regex；过易/全错样本过滤后进入RL。reasoning state与最终 bbox state分离，GT/evaluator拥有最终 grounding authority。
- **Implementation / Evaluation Contract:** KVG-Bench有1,336 cases、531 images、882 entities、10 domains，seen/unseen各5类；5 annotators加独立复核。11名非专家 closed/open-book为56.41%/78.83%。DeepPerception overall 62.20%，其中 seen 63.13%、unseen 60.85%；stage ablation SFT 54.12、CoT-SFT 56.81/56.96、GRPO 62.20。论文未完整披露硬件、precision、batch、wall-clock、online SLO。
- **Evidence / Boundary:** 证明在作者KVG合同中 teacher-CoT scaffolding + rule-based grounding reward优于direct SFT并改善 unseen categories；不证明生成CoT是真实因果解释或模型“内生认知”。teacher可读GT box，composite images和FGVR taxonomy可能造成 shortcut；作者benchmark、reward和method同源，IoU/format不验证知识陈述正确。
- **Trade-offs / Failure Modes / Old Design Boundary:** 两阶段训练提高可学习性，却引入teacher bias、reasoning imitation、reward hacking、filter selection bias与长输出成本。direct grounding在通用类别、严格latency或可靠detector可用时仍更合适；retrieval/open-book在知识更新快时可能比weight内化稳健。
- **Owner / Disposition / Open Questions:** owner `TRAIN-GRPO`，handoff `MULTIMODAL-REPRESENTATION` / `PLATFORM-EVALUATION-SYSTEM`；`Books Pending — Experimental`。需独立KVG集、真实图像、knowledge correctness verifier、matched-compute SFT、seed/CI及v1→KARL revision diff。

#### Infinite Mobility

- **Primary Source URLs:** https://arxiv.org/html/2503.13424v1。
- **Candidate / Week / Score:** Infinite Mobility / 2025-W12 / 4/4/4/5/4/4 = **25/30**。
- **Source / Date / Revision:** Source Family `infinite-mobility-procedural-articulated-assets`；arXiv:2503.13424 v1，first-public 2025-03-17；v1 HTML、URDF pipeline 与实验全文为直接证据，后续 dataset/artifact只作 lineage。
- **Problem / Previous Design / Changed Constraint:** 扫描/重建真实articulated objects可获得外观，却经常缺joint axis/range、碰撞间隙与compound joint，数据量也限制生成模型；纯 learned generation又继承小数据偏差。目标改为生成可执行、结构多样、能进入simulation的 typed asset，而非只生成看起来合理的mesh。
- **Mechanism / State / Flow:** 先生成articulation tree与6类simple/compound joints，再为每个 URDF link填充textured mesh并写 joint origin/type/axis/limit；程序规则修正ground collision、motion range与part gap（约原scale 2%）。asset commit为 URDF + meshes，可导入 SAPIEN、Isaac Sim、Genesis并标waypoints；CAGE再用每类1,000 procedurally generated samples训练。
- **Implementation / Evaluation Contract:** 人类评估由10 participants检查每category随机50 pairs的joint movement；GPT-4V依据RGB/normal maps评mesh quality。生成对象平均joint数12.32（PartNet-Mobility 5.91），tree edit diversity 78.62 vs 3.88；生成约0.46 s/object，NAP 2.04、CAGE 1.96。paper未给完整类别总数、random seeds、硬件/precision或sim-to-real success。
- **Evidence / Boundary:** 证明human-authored procedural grammar可生成更多结构分支并避免若干simulation collision，在author metrics上作为articulated-data source；不证明机器人策略迁移到真实世界或生成分布覆盖真实产品。GPT-4V不是physical verifier，human protocol小，joint friction/damping/motor strength明确缺失。
- **Trade-offs / Failure Modes / Old Design Boundary:** rules带来determinism与可执行性，却使category扩展依赖人工工程，错误joint/mesh ownership会在simulator中放大。扫描/real-to-sim在高保真单体资产仍合理；learned generator在规则难写、分布更广时仍是另一分支。
- **Owner / Disposition / Open Questions:** owner `MULTIMODAL-EMBODIED-VLA`，handoff `TRAIN-DATA` / `PLATFORM-EVALUATION-SYSTEM`；`Books Pending — Refine Existing Argument`。需asset license、physics properties、sim failure tests、real-object transfer、类别coverage及rule provenance/versioning。

#### Aligning Multimodal LLM with Human Preference: A Survey

- **Primary Source URLs:** https://arxiv.org/html/2503.14504v1。
- **Candidate / Week / Score:** Multimodal Preference Alignment Survey / 2025-W12 / 3/4/4/5/4/4 = **24/30**。
- **Source / Date / Revision:** Source Family `survey-mllm-human-preference-alignment`；arXiv:2503.14504 v1，first-public 2025-03-18；survey全文与官方 curated repository为直接 source map。它不是单一primary mechanism，后续repository更新不能倒写v1 taxonomy。
- **Problem / Previous Design / Changed Constraint:** MLLM常停在pretraining+SFT，能follow instruction但truthfulness、hallucination、safety、reasoning与跨模态preference未由统一目标约束。文本RLHF/DPO概念可复用，但visual/audio evidence、annotation与reward failure使同一偏好pair不再同质。
- **Mechanism / State / Flow:** survey按 application scenario、dataset construction、evaluation与future work组织；preference data拆成source、model responses、annotation owner，alignment方法再连接 human/closed-model/open-model/self-annotation，覆盖DPO/RLHF及多模态扩展。其价值是 provenance/evaluator taxonomy，而非可执行新算法。
- **Implementation / Evaluation Contract:** 汇总 general knowledge、hallucination、safety、conversation、reward model与alignment benchmarks，并覆盖image、multi-image、video、audio、medicine、math、embodied和agent；没有统一model/hardware/precision/batch/length/concurrency/SLO或matched experiment。
- **Evidence / Boundary:** 证明研究版图已从“提升单一VQA分数”扩展到 multimodal preference data、reward/evaluation与安全场景；不证明任一方法普遍有效，也不能跨论文直接比较作者benchmark。survey selection、快速版本漂移、缺独立复现和大量闭源judge结论限制证据强度。
- **Trade-offs / Failure Modes / Old Design Boundary:** taxonomy降低检索成本但可能把不同threat model与reward contract合并；偏好alignment可减少某些行为，却引入reward hacking、modality neglect、judge bias和capability regressions。SFT在明确、低歧义任务仍合理。
- **Owner / Disposition / Open Questions:** owner `TRAIN-DPO`，handoff `TRAIN-RLHF` / `PLATFORM-EVALUATION-SYSTEM`；`Weekly Only — Source Map`。需把survey引用回到各primary family，不能作为Books机制证据。

#### Frac-Connections

- **Primary Source URLs:** https://arxiv.org/html/2503.14125v1。
- **Candidate / Week / Score:** Frac-Connections / 2025-W12 / 5/5/4/5/5/3 = **27/30**。
- **Source / Date / Revision:** Source Family `frac-connections-fractional-hyper-connections`；arXiv:2503.14125 v1，first-public 2025-03-18；v1全文与附录PyTorch pseudocode为证据。后续实现/revision需单独标记。
- **Problem / Previous Design / Changed Constraint:** residual connection让深层Transformer梯度可传播，但极深网络仍有gradient vanishing与representation collapse折中；Hyper-Connections用多条full-width streams缓解，却增加hidden-state width和memory access。约束变为在固定总hidden width下保留多stream mixing。
- **Mechanism / State / Flow:** 将 `h∈R^d` reshape为 `m` 个 `d/m` partitions，以B/Y/A connection matrices选择block输入、回写block输出并跨partitions混合；static weights在测试固定，dynamic variant从当前hidden state经norm/linear/tanh和小scale产生。初始化为Pre-Norm residual等价、dynamic weights为0，使新模型从稳定旧路径开始。
- **Implementation / Evaluation Contract:** extra static parameter按 `m(2m+1)×2L`，OLMo-1B/7B SFC×4仅约1,152 extra params；实验含dense OLMo2-1B2与OLMoE-7B、最高3T tokens。OLMoE-7B DFC×4 training loss低0.012，7个downstream平均68.65 vs baseline68.30；DHC收敛更快，作者明确表现与memory折中。
- **Evidence / Boundary:** 证明在作者OLMo/OLMoE训练合同中，partitioned connections可在不扩总hidden width时改善loss/若干benchmarks；不证明端到端runtime或峰值memory等于普通residual，因为matrix mixing、reshape、kernel和communication未完整测量。平均提升小、部分任务收敛后趋同，缺多seed/CI与等wall-clock控制。
- **Trade-offs / Failure Modes / Old Design Boundary:** 固定width降低activation footprint，却增加connection state、mixing compute、kernel fragmentation与dynamic input-dependent路径；错误初始化可能破坏identity path。普通residual在中等深度、compiler成熟和收益微小时仍最简单；Hyper-Connections在memory充足且质量优先时可能更强。
- **Owner / Disposition / Open Questions:** owner `MODEL-TRANSFORMER-LAYER`，handoff `TRAIN-PRETRAINING` / `TRAIN-DISTRIBUTED-TRAINING`；`Books Pending — Refine Existing Argument`。需real wall-clock/HBM/bandwidth、kernel fusion、TP/PP交互、seed/CI与scale sensitivity。

#### Cosmos-Transfer1

- **Primary Source URLs:** https://arxiv.org/html/2503.14492v1；https://github.com/nvidia-cosmos/cosmos-transfer1。
- **Candidate / Week / Score:** Cosmos-Transfer1 / 2025-W12 / 5/5/5/5/5/4 = **29/30**。
- **Source / Date / Revision:** Source Family `nvidia-cosmos-transfer1-multimodal-control`；arXiv:2503.14492 v1，first-public 2025-03-18；official `nvidia-cosmos/cosmos-transfer1` repository为artifact lineage。v1机制和runtime table锁定W12，后续 release APIs 不倒写。
- **Problem / Previous Design / Changed Constraint:** single ControlNet/condition可保持一种geometry或appearance，但Physical AI同时拥有RGB、edge、depth、segmentation、LiDAR、HDMap，且不同空间区域需要不同约束强度。目标从全局单一condition转为 typed multimodal control maps和region-specific arbitration。
- **Mechanism / State / Flow:** 每种modality有独立ControlNet-style branch并注入7B world-generation backbone；spatiotemporal weight maps在每pixel/frame调节各branch，支持foreground用Vis/Edge锁外观、background用Depth/Seg保结构并增加多样性。AV branch把10Hz LiDAR densify到30FPS frames并与HDMap/3D boxes组合；control map、caption、camera/sensor calibration与branch revision构成生成state。
- **Implementation / Evaluation Contract:** RDS-HQ 65K个20s surround-view clips、约360h，含10Hz LiDAR与dense captions。作者测Blur-SSIM、Edge-F1、depth si-RMSE、mask mIoU、LPIPS diversity、quality score，以及AV 3D-bbox mAP/lane mIoU/reprojection。HDMap+LiDAR为44.66/51.55/8.67；LiDAR单branch mAP46.50但lane mIoU48.19，显示typed signals互补。
- **Runtime Contract / Boundary:** 5s 720p约56K tokens；GB200 NVL72上non-attention data parallel、attention head parallel，positive/negative CFG分两组，64 B200 all-to-all。1→64 GPUs end-to-end `141.7s→4.2s`。这是单rack、特定7B/sequence/parallelism厂商结果，未披露batch、precision、功耗、P99与多租户；不能外推任意video model。
- **Trade-offs / Failure Modes / Old Design Boundary:** multimodal control提高局部可控性却增加校准、时间同步、branch冲突、missing modality、weight-map policy与all-to-all failure；单modality在传感器稳定、成本受限时更简单。生成视频不是causal simulator或真实传感器，Sim2Real收益只由受限case study支持。
- **Owner / Disposition / Open Questions:** owner `MULTIMODAL-WORLD-MODELS`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `MULTIMODAL-EMBODIED-VLA` / `INFER-EXECUTION`；`Books Pending — Integrate New Mechanism Candidate`。需安全critical downstream、control conflict policy、sensor provenance、energy/P99和跨rack scaling。

#### Measuring AI Ability to Complete Long Tasks

- **Primary Source URLs:** https://arxiv.org/html/2503.14499v1；https://github.com/METR/task-standard。
- **Candidate / Week / Score:** Measuring AI Ability to Complete Long Tasks / 2025-W12 / 5/5/5/5/5/4 = **29/30**。
- **Source / Date / Revision:** Source Family `metr-long-task-time-horizon`；arXiv:2503.14499 v1，first-public 2025-03-18；v1全文、METR public tasks与method appendix为直接证据。后续 model releases/trend updates是同family observations，不回写v1。
- **Problem / Previous Design / Changed Constraint:** benchmark accuracy不告诉工程师模型可可靠承担多长的真实工作；task count也混合几十秒和数小时任务。新合同把difficulty锚定到domain-skilled human成功完成所需时间，再测agent在该时长的成功概率。
- **Mechanism / State / Flow:** 任务来自97个HCAST（46 families）、7个约8小时RE-Bench和66个<1分钟SWAA，共170；human baseliner成功时间取geometric mean。model+scaffold执行任务，executable scorer给0–1/成功标签；logistic model `p=σ((log h_model-log t_task)β_model)`估计50% horizon，hierarchical bootstrap跨family/task/attempt给不确定性。model能力、scaffold、tool/environment opportunity与human-time label是不同owner。
- **Implementation / Evaluation Contract:** 评13个2019–2025 frontier models。Claude 3.7 Sonnet 50% horizon约59分钟，80% horizon约15分钟；2019–2025估计doubling约212天，80%趋势213天。失败分析显示新模型少重复失败动作，却更常premature abandonment；messy、反馈弱且需主动找信息的环境仍困难。
- **Evidence / Boundary:** 证明在这套软件/ML/cyber task distribution与scaffold下，human-time与success负相关，趋势斜率比单点horizon更稳定；不证明现实组织任务自动化时间，也不等于deployment autonomy。任务缺组织context，多数通过bash文本操作，elicitation投入不均；human time仅成功attempt且样本小，长任务和95%可靠性需要远更多数据。
- **Trade-offs / Failure Modes / Old Design Boundary:** human-time带来可解释单位，却把技能、context、task family与baseliner selection折进同一数字；50%可展示frontier但对生产过低。短benchmark仍适合回归，domain-specific executable eval仍需保留；time horizon是aggregate capability lens。
- **Owner / Disposition / Open Questions:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW` / `AGENT-PLATFORM`；`Books Pending — Integrate New Mechanism Candidate`。需95/99% horizon、scaffold/version lock、non-software domains、组织context与real deployment replication。

#### FlexWorld

- **Primary Source URLs:** https://arxiv.org/html/2503.13265v1。
- **Candidate / Week / Score:** FlexWorld / 2025-W12 / 4/4/4/5/4/3 = **24/30**。
- **Source / Date / Revision:** Source Family `flexworld-progressive-3d-scene-expansion`；arXiv:2503.13265 v1，first-public 2025-03-17；v1全文与project page为直接证据。later artifacts只作 lineage。
- **Problem / Previous Design / Changed Constraint:** single-image 3D reconstruction只拥有可见surface，直接一次性生成360° scene会在大视角产生holes、geometry drift和不一致；image diffusion逐view补全又会累积错误。约束变为每轮只对当前粗scene不可见区域生成new observation，并把它commit回可渲染3D state。
- **Mechanism / State / Flow:** MASt3R/point cloud形成rough scene，沿zoom-out/rotation trajectory渲染incomplete video；fine-tuned CogVideoX-5B V2V以conditional video latents生成consistent views。每轮做depth scale alignment、guided filtering，把新point clouds转换/融合到3DGS并优化；FLUX SDEdit再refine固定views。immutable input evidence、mutable 3DGS与generated observations必须区分，progressive commit错误会向后累积。
- **Implementation / Evaluation Contract:** V2V在DL3DV-10K训练，480×720、lr5e-5、batch32、5K steps、16×A800-80G。RE10K随机300 clips、Tanks-and-Temples 14 scenes/100 clips，49 frames；对MotionCtrl/CameraCtrl/DimensionX/See3D/ViewCrafter测FID/FVD/PSNR/SSIM/LPIPS与camera error。RE10K FVD100.41 vs下一ViewCrafter143.89；ablation移除V2V、zoom-out或refine均有退化。
- **Evidence / Boundary:** 证明progressive novel-view generation + geometry-aware fusion在作者datasets上改善visual metrics与view coverage；不证明其生成不可见内容是真实world state或适合planning。无独立limitations节，generated evidence可自洽但错误；MASt3R camera labels、author pipeline、selected static scenes、未披露inference time/memory/seed/CI限制外推。
- **Trade-offs / Failure Modes / Old Design Boundary:** progressive expansion提高view flexibility，却引入 hallucinated geometry、order dependence、loop closure failure和迭代成本；一次性reconstruction在多视图充足或真实性优先时更可靠。该工作是scene-generation branch，不是 action-conditioned world model。
- **Owner / Disposition / Open Questions:** owner `MULTIMODAL-WORLD-MODELS`，handoff `MULTIMODAL-REPRESENTATION` / `MULTIMODAL-GENERATIVE-PARADIGMS`；`Books Pending — Experimental`。需uncertainty/provenance、loop closure、real multi-view verification、runtime与rollback policy。

#### DreamRenderer

- **Primary Source URLs:** https://arxiv.org/abs/2503.12885；https://limuloo.github.io/DreamRenderer/；https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_DreamRenderer_Taming_Multi-Instance_Attribute_Control_in_Large-Scale_Text-to-Image_Models_ICCV_2025_paper.html。
- **Candidate / Week / Score:** DreamRenderer / 2025-W12 / 5/4/4/5/5/4 = **27/30**。
- **Source / Date / Revision:** Source Family `dreamrenderer-multi-instance-attribute-binding`；arXiv:2503.12885 v1，first-public 2025-03-17；event-time metadata/project与later ICCV open-access paper用于核对lineage。由于arXiv HTML误渲染，后续正式版细节仅在与v1公开claim一致处作为related evidence，不把July supplement新增内容倒写W12。
- **Problem / Previous Design / Changed Constraint:** depth/canny/layout control可锁定geometry，但FLUX joint attention会让多个实例的color、number、identity等属性泄漏；全局hard isolation能防串扰却破坏scene harmony。约束变为按instance绑定text/image attribute，同时保留跨instance/background的global composition。
- **Mechanism / State / Flow:** Bridge Image Tokens复制/承接region image tokens，使仅由text预训练的T5 embeddings在joint attention中绑定正确实例；Hard Text/Image Attribute Binding限制instance token只访问对应属性，Soft Binding允许全局交互。layer analysis把hard image binding仅施加在负责instance rendering的中层，输入/输出层保持soft/global flow。region/mask、instance identity、attribute tokens与layer policy共同构成control state；方法training-free。
- **Implementation / Evaluation Contract:** 基于FLUX并兼容depth/canny，评COCO-POS/COCO-MIG，指标含Instance Success Ratio、mIoU、Image Success Ratio及image quality；与FLUX、3DIS及layout-to-image GLIGEN/InstanceDiffusion/MIGC等比较。正式版报告depth guidance SR62.50%、ISR94.51%、mIoU84.36；full hard-text ablation平均ISR71.9、image success37.1；mid-layer hard binding相对提升ISR约15.7%。event-time硬件、precision、wall-clock、memory与P99未披露。
- **Evidence / Boundary:** 证据支持multi-instance失败既是representation binding也是layer-placement问题，且 selective hard/soft control可改善作者benchmarks；不证明attention mask等于因果disentanglement或跨所有foundation models通用。later ICCV numbers、项目代码与W12 arXiv v1的revision边界必须保留；benchmark检测器/attribute parser可能偏置。
- **Trade-offs / Failure Modes / Old Design Boundary:** hard binding降低attribute leakage却可能切断必要cross-object relation，soft binding保持coherence却重新引入串扰；bridge tokens增加token/attention成本，mask错误会绑定错实例。单实例或属性简单时普通depth/canny足够；显式layout methods在严格geometry contract仍合理。
- **Owner / Disposition / Open Questions:** owner `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `INFER-EXECUTION`；`Books Pending — Refine Existing Argument Candidate`。需event-time PDF diff、token/runtime overhead、复杂overlap、跨backbone复现与binding failure detector。

## 3. W13 spillback 与 reopened candidate 审计包

### 3.1 W13 spillback strict Full Source Review Complete（17 / 21）

| Candidate / source | Score | 机制、实验与证据边界 | Owner / disposition |
| --- | ---: | --- | --- |
| When Less is Enough — https://arxiv.org/html/2503.16660v1 | 4/4/4/5/5/3 = **25** | 3-layer selector 用 Gumbel-Softmax mask，3-layer reconstructor 用 L2 feature reconstruction；约 100K COCO features，LLaVA-NeXT/OneVision，OCR/non-OCR 分开。证明 token redundancy 依 task；不证明 e2e latency/energy/P99，selector 可能不可逆删掉小字局部证据。 | `MULTIMODAL-REPRESENTATION`；handoff request/KV；Experimental |
| MAPS — https://arxiv.org/html/2503.16905v1 | 4/4/4/4/5/4 = **25** | Manager/UserProxy；Interpreter、Aligner、Scholar、Solver、Critic 五阶段并从最低分阶段 backtrack。GPT-4o，MathVista/OlympiadBench/EMMA；角色 ablation 显著退化。shared-base self-judge 有 correlated failure，缺 P99/cost/retry SLO。 | `AGENT-MULTI-AGENT`；handoff workflow/eval；Refine |
| MARS — https://arxiv.org/html/2503.16874v1 | 4/4/4/4/5/4 = **25** | Planner/Teacher/Critic/Student/Target 迭代 prompt，状态是 prompt+critique ledger。DeepSeek-V2.5/GPT-4o，12 general+5 domain，对比 APE/ProTeGi/OPRO/PE2。无 universal prompt representation/真实 deployment feedback，搜索成本与 judge bias 未闭合。 | `AGENT-PROMPT`；handoff multi-agent/eval；Refine |
| RoboFactory — https://arxiv.org/html/2503.16408v1 | 5/5/4/5/5/4 = **28** | GPT-4o RoboBrain 分解；logical/spatial/temporal constraints 进入 RoboChecker，每 timestep 校验/失败 halt-replan，5cm voxel shared state。ManiSkill 11 tasks，150 demos/task，Diffusion Policy，320×240，RTX4090 5h，batch128，300 epochs，100 configs；success single 49%→4-agent 10%，long pipeline 0%。 | `MULTIMODAL-EMBODIED-VLA`；handoff multi-agent/workflow/security；New Mechanism candidate |
| Creative Writing post-training — https://arxiv.org/html/2503.17126v1 | 4/4/4/5/5/5 = **27** | DDPO/DORPO 按 winning-response deviation 加权 DPO/ORPO。r/WritingPrompts；Gemma2-2B RM LoRA r16/a32，batch4，lr3e-5，3 epochs，MAE .39/Spearman .51；5 author raters，3/item，alpha .31/.45。未披露 hardware，judge/rater reliability 较弱。 | `TRAIN-DPO`；handoff eval；Experimental |
| OpenVLThinker — https://arxiv.org/html/2503.17352v1 | 4/5/5/5/5/3 = **27** | Qwen2.5-VL-7B 迭代 SFT/GRPO；RL model 产 verified demos 后从 base 重启 SFT。25K SFT/5K GRPO，后续 5K/5K；MathVista 初始 SFT 68.5→62.5，迭代后 70.2。self-data verifier bias 与 distribution narrowing 未消除。 | `TRAIN-GRPO`；handoff multimodal/eval；Refine |
| VCtrl — https://arxiv.org/html/2503.16983v1 | 5/4/4/5/5/4 = **27** | 冻结 CogVideoX-5B；control/video 同 VAE；task mask；约 1/5 blocks 的 control branch，residual injection + adaptive pooling + DistAlign。800K clips，49 frames/720×480，Adam 1e-5，clipnorm1。无 deployment VRAM/latency/P99，不能外推所有 control modality。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；handoff representation/data；Experimental |
| MathFlow — https://arxiv.org/html/2503.16549v1 | 4/4/4/4/5/5 = **26** | FlowVerse 2K bilingual visual math；separate perceptual/inference models，显式 evidence handoff。A100/ZeRO2/AdamW，pretrain 1e-5、SFT 5e-6；MathFlow-P+GPT4V 58.9、DeepSeek-R1 75.6。custom benchmark+closed inferencer confound。 | `MULTIMODAL-REPRESENTATION`；handoff workflow/eval；Refine |
| FastCuRL — https://arxiv.org/html/2503.17287v1 | 4/5/5/5/5/3 = **27** | prompt-length Short/Mix/Long，Short→Mix→Long→Mix context curriculum。40,315 Q/A，DeepSeek-R1-Distill-Qwen1.5B，8 GPUs 单节点，normalized batch128；860 vs1750 steps，avg57.5 vs57.0。无 equal-token/equal-compute clean control，stage 手工选择。 | `TRAIN-GRPO`；handoff long-context；Experimental |
| AgentRxiv — https://arxiv.org/html/2503.18102v1 | 5/5/4/5/5/4 = **28** | Agent Laboratory 共享 local paper repository/API，SentenceTransformer/cosine retrieval；N=40 generations，N=5 previous+5 arXiv。o3-mini medium / gpt4o-mini target；MATH500 70.2→78.2，3 labs 约+6%。compute 与 self-generated evidence bias 增加。 | `AGENT-WORKFLOW`；handoff memory/multi-agent/eval；Refine |
| Vision-R1 — https://arxiv.org/html/2503.18013v1 | 4/5/5/5/5/3 = **27** | GRPO localization rewards：format+recall+precision/IoU，threshold .5/.5/.75→.75/.75/.9。Qwen2.5-VL-7B/Griffon-G-7B，COCO/ODINW；progressive schedule 帮强 Griffon，弱 Qwen STEP=1 更好，故不是普适单调 curriculum。 | `TRAIN-GRPO`；handoff multimodal/eval；Experimental |
| LEMMA — https://arxiv.org/html/2503.17439v1 | 4/5/5/5/5/3 = **27** | first wrong step+error taxonomy；teacher 制造错误，Fix&Continue/Fresh&Restart 构造 revision trajectories。Llama3-8B/DeepSeekMath-7B，GPT-4o teacher+Nemotron70B check，约88.9K，MATH/GSM8K+OOD。math-only/teacher provenance 集中。 | `TRAIN-DATA`；handoff SFT/reflection；Refine |
| V-Seek — https://arxiv.org/html/2503.17422v1 | 4/5/5/5/5/3 = **27** | MILK-V 64-core SG2042/128GB，llama.cpp；Q4_0 fp32→int8 GEMV，NUMA-aware。Llama7B、R1-distill 8B/14B，prompt22/gen256；>32 threads NUMA 反噬。无 quality regression，energy unit 可疑，不能外推 GPU。 | `INFER-TENSORRT-LLM` generic execution owner；handoff prefill/decode/memory；Experimental |
| CODA — https://arxiv.org/html/2503.17760v1 | 5/5/4/5/5/4 = **28** | continuous VAE→residual quantization + unit-sphere attention quantization。ImageNet256/MaskGIT；ablation direct VQ rFID41.52/49% use→residual14.23→attention7.06/100%→adapt1.34。作者 budget 不能外推跨模型 runtime。 | `MULTIMODAL-REPRESENTATION`；handoff generative；New Mechanism candidate |
| PhysTwin — https://arxiv.org/html/2503.17973v1 | 5/5/4/5/5/4 = **28** | 3 RGB-D videos→state X_t；spring-mass explicit Euler action dynamics；先 physics/topology/geometry 后 Gaussian appearance。22 scenarios，RealSense D455，1–10s，9 points，unseen action pairs22。小 hand-built dataset、3 views、成功 case selection，不证明开放世界 causality。 | `MULTIMODAL-WORLD-MODELS`；handoff embodied；Experimental |
| MDocAgent — https://arxiv.org/html/2503.13964v1 | 4/5/5/5/5/3 = **27** | OCR/PDF text 与 page images 并行 ColBERT/ColPali；general/critical/text/image/summarizer agents。5 benchmarks，Llama3.1-8B+Qwen2-VL7B，top1/top4，4×H100；.407 vs .363、.465 vs .419。无 P99/cost/cross-doc provenance。 | `AGENT-RAG`；handoff representation/workflow/eval；Refine |
| ETVA — https://arxiv.org/pdf/2503.16867v1 | 5/4/4/5/5/4 = **27** | scene graph 生成 atomic yes/no questions；commonsense augmentation 与 video understanding/reflection/conclusion 分阶段判定。2K prompts/12K questions、105-prompt human subset、15 T2V models；ablation 支持 knowledge augmentation 与 multi-stage reasoning，但 judge correlation、非统一视频生成设置、二元等权聚合及未披露成本限制外推。 | `PLATFORM-EVALUATION-SYSTEM`；handoff multimodal generation/multi-agent；Refine |

#### ETVA — 2503.16867 v1，03-21

- **Candidate / Week / Score:** Evaluating Text-to-Video Alignment / 2025-W12 / 5/4/4/5/5/4 = **27/30**。
- **Source Family ID / type / date:** `etva-atomic-video-text-alignment-evaluation`；arXiv paper；v1 first-public 2025-03-21，v2 2025-08-17 是同 family later revision，不重复计分。
- **Direct / related primary sources and access:** event-time v1 PDF 22 页已恢复并全文读取；v2 metadata 只核验 revision lineage。覆盖 metadata、Introduction、Related Work、Method/公式、implementation prompts、evaluation/baselines/ablation、model settings、appendix 与 conclusion。论文没有独立 limitations section，因此 threats 由实验合同推导并明确标为审计判断。
- **Original problem / previous design / changed constraint:** CLIP similarity、caption overlap 与单次 MLLM 打分便宜，适合粗粒度筛查，却会把 object、attribute、relation、count 与 implicit commonsense 压成单分；当 T2V 输出需要定位具体 alignment failure 时，评估必须从 holistic impression 变成可追踪 atomic claims。
- **Mechanism / state ownership / control and data flow:** Element Extractor 从 prompt 抽 entity/attribute/relation，Graph Builder 建 scene graph，Graph Traverser 生成 atomic yes/no questions；Qwen2.5-72B 增强常识，Qwen2-VL-72B 依次执行 video understanding、critical reflection 与 conclusion。prompt graph/question set 是 evaluation-spec state，video/judge revision 是 evidence identity，最终分数是 binary atomic answers 的平均；不得把 judge 自信度当生成模型内部置信度。
- **Implementation / evaluation contract:** 数据包含 2K prompts、约 12K questions 与 10 类挑战；人工相关性使用 105 prompts × 15 T2V outputs，5 位 annotators 以 0～5、步长 0.5 的 Likert 分和 atomic majority vote 标注。模型覆盖 10 个 open 与 5 个 closed T2V systems，生成 duration/resolution 不完全一致。
- **Baselines / ablations / sensitivity / overhead:** baseline 包括 BLEU/ROUGE、CLIPScore ViT-B/32、ViCLIPScore、UMTScore 与 VideoScore-Qwen2-VL。ETVA 报告 atomic accuracy 89.27%、Kendall τ 47.16、Spearman 58.47；移除 knowledge augmentation 后为 67.34/27.34/35.54，移除 video-understanding stage 后为 82.73/37.56/44.81，direct-answer 为 63.07/18.18/23.84。作者还报告 multi-agent question generation 相对 vanilla ICL 的 rank-correlation 增益；这只在其 judge/prompt contract 内成立。
- **Hardware / model / precision / length / batch / concurrency / SLO:** judge models 如上；T2V outputs 覆盖不同分辨率与时长。judge hardware、precision、batch、concurrency、latency、token/cost、P99 与 production SLO 均 `Not Disclosed`，所以不形成 serving efficiency 结论。
- **What evidence proves / does not prove:** 证据支持“结构化 atomic question + knowledge augmentation + staged reasoning”在作者样本上比 coarse metrics 更贴近人工 alignment 判断；不证明 binary atoms 独立或等权，不证明 judge 无 hallucination/correlated error，也不证明该 evaluator 能测 realism、safety、causal world consistency 或任意 T2V distribution。
- **Trade-offs / failure modes / old design boundary:** 可解释性提高但 question generation、judge calls 与人工校准成本上升；scene-graph omission、commonsense injection error、question dependency、judge version drift 和 majority-vote bias 会改变分数。低风险粗筛、统一工作负载或极低评估预算下，CLIP/caption metrics 仍是合理第一层，而 ETVA 更适合作为后续 claim-level layer。
- **Evolution / ROADMAP / chapters / existing coverage:** `Layering / Dependency`：holistic similarity → structured prompt graph → atomic questions → staged evidence judgment。owner `PLATFORM-EVALUATION-SYSTEM`（current Ch66 / legacy Ch62），handoff `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）与 `AGENT-MULTI-AGENT`（current Ch82 / legacy Ch78）；已同读 Ch66 的 evaluation contract 与 Ch24、Ch82 的相邻责任，现有 Books 已覆盖 claim decomposition/evaluator identity 的一般框架，但没有必要在 Historical Books Gate 关闭时追加本案例。
- **Integration decision / changed files / open questions:** `Books Pending — Refine Existing Argument Candidate`；本轮仅解除 Weekly blocker。后续需验证 atomic dependency/weighting、跨 judge calibration、真实成本与 uniform generation-condition replication。

### 3.2 Low-score closure（7：W13 lane 2 + academic replay 4 + engineering replay 1）

| Candidate | Identity / date | Score | Owner | Rejection |
| --- | --- | ---: | --- | --- |
| Long Context Survey | 2503.17407 v1, 03-20 | 3/3/3/4/4/2 = **19** | `MODEL-LONG-CONTEXT` | secondary source map；无统一实验/hardware/SLO |
| Mind with Eyes | 2503.18071 v1, 03-23 | 3/3/3/4/4/2 = **19** | `MULTIMODAL-WORLD-MODELS` | survey taxonomy；无独立 causal evidence |
| AIMI sparse-event forecasting | 2503.16091 v1, 03-20 | 3/3/3/5/2/2 = **18** | `TRAIN-DATA` | 22-participant medication-adherence domain study；future prescribed-time features与personalization有实验，但balanced test、tiny cohort、sequential chunk forgetting及未部署app使其不足以改变通用AI System结论 |
| Deceptive Humor benchmark | 2503.16031 v1, 03-20 | 3/2/3/4/3/3 = **18** | `PLATFORM-EVALUATION-SYSTEM` | 9,000-item GPT-4o synthetic benchmark across English/4 Indic/code-mixed variants；只人工复核450条且native-language quality明显较弱，无真实分布/claim evidence retrieval contract，保留为domain benchmark |
| Survey on Evaluation of LLM-based Agents | 2503.16416 v1, 03-20 | 3/3/3/4/4/2 = **19** | `PLATFORM-EVALUATION-SYSTEM` | 系统整理 capability、domain、generalist 与 evaluation-framework 版图，并指出 dynamic environment、cost/safety/robustness/fine-grained evidence 缺口；但无统一 executable harness、同环境 model comparison、hardware/SLO 或独立 causal result，作为 source map 保留而不升级机制结论 |
| Stop Overthinking survey | 2503.16419 v1, 03-20 | 3/3/3/4/4/2 = **19** | `MODEL-SAMPLING` | taxonomy 覆盖 length-reward RL、variable-length SFT、latent compression、dynamic routing、prompt/routing 与 compute-optimal TTS，并明确 safety–efficiency trade-off；但为 secondary survey，且 o1 训练细节明确标为 speculation，无统一 accuracy/latency/cost contract，不能把跨论文结果写成通用机制收益 |
| JAX v0.5.3 | official tag `jax-v0.5.3`, 2025-03-19, commit `c8032a9` | 2/3/3/5/2/2 = **17** | `INFER-TENSORRT-LLM` generic execution owner | 官方 release 只新增 `dynamic_slice/update` 的 negative-index control 与 `random.categorical(replace=False)`；有精确版本/代码身份，但无 AI workload benchmark、hardware、end-to-end runtime 或长期 architecture shift，保留为 version-scoped implementation fact |

### 3.3 Unverified / Blocked（5：W13 lane 2 + academic replay 3）

| Priority | Candidate | Identity | 缺少材料 / reason | 建议文件名 |
| --- | --- | --- | --- | --- |
| P1 | TokenBridge | 2503.16430；v1 03-20 | v1/v2 HTML 错渲染；abstract 只够确认 continuous VAE→dimension-wise quantization→AR categorical loss | `2025-W12-tokenbridge-v1.pdf` |
| P1 | Judge Anything | 2503.17489 v1, 03-21 | project/repo 只确认 TaskAnything 1500 queries/15 categories/5 MLLMs 与 scripts；缺 v1 正文 | `2025-W12-judge-anything-v1.pdf` |
| P3 | TULIP | 2503.15485；v1 03-19，v2 04-07 | v2 可读且说明仅“clarified fine-tuning process, updated appendix”，但 event-time v1 PDF 约 9.3 MB，当前 parser 因文件过大无法读取；不能用 v2 的 fine-tuning/appendix 细节倒写 v1 | `2025-W12-tulip-v1.pdf` |
| P3 | One-Step Residual Shifting Diffusion (RSD) | 2503.13358；v1 03-17，v2 05-27，v5 2026-06-09 | v1 PDF 约 48 MB，event-time HTML cache miss；当前 official repository 仅 2 commits，README 已指向 ICML 2026 paper，不能用 later artifact/table 与 v5 mechanism 倒写 v1。摘要只够确认 one-step ResShift distillation 与 restoration/perception trade-off，不足以完成 Method、ablation、hardware 与 limitations 审计 | `2025-W12-rsd-v1.pdf` |
| P3 | VideoRFSplat | 2503.15855；v1 03-20，ICCV final 2025-10 | v1 arXiv HTML 错渲染为author-response模板，PDF fetch失败；abstract只确认dual image/pose streams、communication blocks与asynchronous denoising，official repo目前仍只有README/TODO且未发布training/inference code。CVF final是后续正式版，不能用其表格倒写event-time v1 | `2025-W12-videorfsplat-v1.pdf` |

### 3.4 本 lane 新完成 Strict Full Source Review（57）

#### Why Do Multi-Agent LLM Systems Fail? — 2503.13657 v1，03-18

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** Multi-Agent System 通常把失败归因于单个模型能力不足，并通过增加角色、消息轮次或拓扑复杂度来补偿；在任务可分解且局部错误互相独立时，这一设计合理。
- **Changed constraint / mechanism:** 当错误会通过 inter-agent communication 放大时，团队失败不再等于成员失败之和。论文从超过 150 条执行轨迹，通过 grounded-theory procedure 建立 14 个 failure modes，归为 system-design、inter-agent misalignment 与 task-verification 三类，再用自动 judge 定位 failure span。
- **State ownership / control flow:** task state 分散在各 agent 的 private context、message history 和 orchestrator；没有 authoritative shared state 时，过期假设、role drift 与错误 consensus 会跨轮传播。改进分别作用于 prompt、communication topology 和 verification contract，而不是简单增加 agent 数。
- **Implementation / evaluation contract:** 五种 MAS、人工三轮 annotation（Cohen's κ 约 0.24→0.92→0.84）；o1 few-shot judge accuracy .94、precision .833、recall .77、F1 .80、κ .77。干预在 AG2/ChatDev、GPT-4/GPT-4o 上各重复六次；收益随系统和 failure mode 变化，约十几个百分点而非普适消除失败。
- **Evidence boundary / trade-off:** 证明 failure taxonomy 能指导 targeted intervention；不证明 taxonomy 覆盖开放世界 Agent，也不证明更复杂 topology 必然更强。额外 critic、messages 与 recovery 增加 token cost、latency、coordination tax 和 correlated judge failure。
- **Coexistence / evolution:** single-agent 在 headroom 足、任务不可分或 communication tax 高时仍更合适；演进是 `task decomposition → explicit shared state → verifier/recovery → bounded topology`。Owner `AGENT-MULTI-AGENT`，handoff `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### Cosmos-Reason1 — 2503.15558 v1，03-19

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** video-language pretraining 擅长描述 observation，却未必把 physical commonsense 与 action-conditioned consequence 组织成可验证推理；扩大静态 caption 数据在 perception-first 工作负载中合理，但不能直接保证 embodied reasoning。
- **Changed constraint / mechanism:** 四阶段训练把通用视觉语料、physical/embodied curated data、SFT chain-of-thought 与 RL verifier 串联；8B/56B 模型采用 hybrid Mamba-MLP-Transformer，视觉输入最多 32 frames、最高 2 FPS、448×448，并以 300M ViT 编码。
- **State ownership / control flow:** 视频 observation 由 vision encoder 写入 token state，reasoner 生成 reasoning trace 与 final answer，RL verifier 只对可判定 final answer 回传 reward；因此“思考过程可信度”并未成为独立受控状态。
- **Implementation / evaluation contract:** 约 120M vision/general pretraining samples、8M SFT samples、24,079 RL samples。8B 用 TP4，56B 用 TP8/PP2；global batch 32、fused Adam β=(.9,.95)、weight decay .1。physical benchmark 为 604 questions/426 videos，embodied benchmark 为 612 questions/600 videos；五次推理平均，temperature .6、top-p .95。8B physical 45.4→52.3，56B 58.2→60.2；embodied 8B 47.2→60.0，56B 53.5→63.7；RL 8B average 58.9→67.1。
- **Evidence boundary / trade-off:** 证明 staged data/objective 与 final-answer RL 在作者 benchmark 上有效；不证明 reasoning trace faithful、真实机器人 closed-loop safety 或跨 embodiment 泛化。自建 benchmark 与训练数据 proximity、MCQ/final-answer verifier、硬件未披露限制外推。
- **Coexistence / evolution:** 通用 VLM 在无需 action consequence 的识别与描述任务仍更经济；演进是 `video description → physical commonsense supervision → embodied question contract → verifier-bounded RL`。Owner `MULTIMODAL-EMBODIED-VLA`，handoff `MULTIMODAL-WORLD-MODELS` / `TRAIN-GRPO` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Integrate — New Mechanism` candidate。

#### VidKV — 2503.16257 v1，03-20

- **Score:** 5/5/5/5/5/3 = **28**。
- **Original problem / old design:** uniform low-bit KV quantization 简单、kernel 规则，适合 text-like token distributions；video LLM 的长视觉序列使 KV memory 成为主约束，但 channel/token importance 高度异质。
- **Changed constraint / mechanism:** key 的 anomalous channels 保留 2-bit，其余 channel 用 1-bit 并通过 FFT-domain transform 降低量化误差；value 侧保留 salient tokens，其余压缩到平均约 1.58 bit。identity 不再只是 layer/token，而扩展为 key/value、channel class 与 token salience。
- **State ownership / control flow:** prefill 统计异常 channel 和 salient token，quantizer 写入异构 packed KV；decode 按 metadata 选择解码路径。压缩 metadata、threshold 与 layout 成为 cache identity 的一部分，必须随模型/layer/quantization revision 失效。
- **Implementation / evaluation contract:** v1 覆盖 video-LLM quality 与 memory-compression ablation；低于约 1.2-bit key 时质量明显下降，1-bit 结果仍落后 16-bit，说明不是无损替代。作者比较多种 key/value 分配而非只报告单点。
- **Evidence boundary / trade-off:** 证明 workload-aware asymmetric allocation 优于同预算 uniform quantization；尚未证明跨模型、长文本、production P99 或 end-to-end throughput。v1 未形成独立 limitations section，hardware、kernel fusion、metadata lookup 与动态 salience overhead 未完整披露。
- **Coexistence / evolution:** uniform quantization 在短上下文、规则 kernel 与可接受质量损失时仍合适；演进是 `uniform precision → K/V asymmetry → channel/token-aware precision → cache identity-aware runtime`。Owner `INFER-KV-CACHE`，handoff `INFER-MEMORY-MANAGEMENT` / `INFER-EXECUTION`；disposition `Emerging / Experimental`。

#### XAttention — 2503.16428 v1，03-20

- **Score:** 5/5/5/5/4/4 = **28**。
- **Original problem / old design:** dense attention 保证任意 query-key interaction，适合中短序列；长视频/长文本 prefill 中二次复杂度使 memory traffic 与 latency 失控，而固定 local/sink sparse pattern 又可能删除任务相关的远距离证据。
- **Changed constraint / mechanism:** attention map 中沿 anti-diagonal 的 block regularity 允许用少量 sampled blocks 估计整条 anti-diagonal score，再按 threshold 选择 blocks；无需训练，并允许动态 sparsity。
- **State ownership / control flow:** prefill 先执行 pattern estimation，生成 block mask；sparse attention kernel 只读取选中 QK blocks，decode path 不在本文主结论内。threshold 与 mask 是 request/sequence-dependent execution state，而不是模型权重。
- **Implementation / evaluation contract:** text/video understanding 与 generation，8K–256K context；在 256K、约 7% density 条件，作者报告 attention-kernel 相对 FlashInfer FlashAttention 最多约 13.5×。包含 pattern-selection overhead，但不是完整 serving stack。
- **Evidence boundary / trade-off:** 证明 anti-diagonal prior 可在作者 workloads 保留质量并降低 prefill attention kernel 成本；不证明 end-to-end TTFT/P99、decode、所有 attention heads 或任意 modality。硬件与各模型的完整 batch/concurrency/SLO 需在最终写回逐表绑定。
- **Coexistence / evolution:** dense attention 仍是短序列、精确性优先与无稳定结构先验时的基线；演进是 `dense exact → static sparse → data-dependent block selection → request-specific execution plan`。Canonical owner `MODEL-SELF-ATTENTION`，handoff `INFER-PREFILL` / `INFER-EXECUTION`；disposition `Emerging / Experimental`。

#### Expert Race — 2503.16057 v1，03-20

- **Score:** 5/5/5/5/4/4 = **28**。
- **Original problem / old design:** token-wise top-k MoE 保持固定 active experts，便于计算预算与 capacity planning；在 diffusion timestep/batch 的 token difficulty 不均时，固定 k 可能对简单 token 过算、对困难 token 欠算。
- **Changed constraint / mechanism:** 将竞争域从“每 token 内选 k 个 experts”改为 batch/token/expert 的 global top-K；identity gating 提供 residual path，EMA threshold 稳定选择，layer-wise regularization 与 router-similarity constraint 抑制 collapse。
- **State ownership / control flow:** router 产生所有 token-expert scores，global selector 在总预算下分配激活；capacity owner 从 token-local policy 上移为 layer/global budget controller，并引入跨 token coupling。
- **Implementation / evaluation contract:** ImageNet 256×256 diffusion Transformer；通过把 expert hidden dimension 缩为 1/k 控制 activated-parameter budget，训练约 1.75M steps、batch 1024、learning rate 1e-4；500K-step ablations。论文报告 FID/compute，并显示 load-balance maximum violation .850 vs 2.052 的改善。
- **Evidence boundary / trade-off:** 证明动态 active experts 能在作者 DiT/ImageNet contract 下更好分配条件计算；不证明 LLM token serving、跨设备 all-to-all 或 production routing latency。global selection 引入同步、batch-shape sensitivity 与 hard-token starvation/collapse failure mode。
- **Coexistence / evolution:** per-token fixed top-k 在在线小 batch、可预测 latency 与 distributed placement 受限时仍合理；演进是 `dense → fixed token-local top-k → global budgeted dynamic routing`。Owner `MODEL-MOE`，handoff `TRAIN-DISTRIBUTED-TRAINING` / `INFER-DISTRIBUTED`；disposition `Emerging / Experimental`。

#### SWEET-RL — 2503.15478 v1，03-19

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** outcome-only RL 适合有终局 verifier 的短任务；长协作对话的稀疏终局 reward 无法定位哪一步破坏状态，直接 imitation 又会复制次优 trajectory。
- **Changed constraint / mechanism:** critic 在训练期读取当前 dialogue state 与 reference solution，用 mean log-prob 构造 dense step reward；actor 以此优化 backend/frontend collaborative trajectory。reference 是 privileged training signal，不是部署时可观测 confidence。
- **State ownership / control flow:** simulator/environment 持有 task state，actor 提议下一轮 action，critic 训练期读取 privileged target 评估 step，optimizer 更新 actor；部署只运行 actor，因此不得把 critic reward 写成 online correctness guarantee。
- **Implementation / evaluation contract:** ColBench 含 backend coding 与 frontend design；10K train/1K test tasks 由 Llama-70B 生成，test 经过人工检查；15K offline trajectories 由 Llama-8B actor 与 70B simulator 产生。backend 以 tests passed/task success；Llama-8B SWEET-RL 56.8/40.4 vs multi-turn DPO 48.0/34.4，70B SWEET-RL 60.2/45.6。frontend 用 cosine similarity 与对 GPT-4o win rate，最长 16K tokens。去除 reward normalization 会偏向短响应。
- **Evidence boundary / trade-off:** 证明 privileged critic 能改善该合成协作任务；不证明无 reference 的真实 deployment、开放式协作或安全关键 correctness。新增 critic compute、simulator bias、reference leakage、length bias 与 reward hacking。
- **Coexistence / evolution:** outcome reward 在强终局 verifier、短 horizon 时更简洁；演进是 `terminal reward → trajectory-aware dense critic → privileged training supervision → deployment actor`。Owner `TRAIN-RLHF`，handoff `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### SkyLadder — 2503.15450 v1，03-19

- **Score:** 5/5/5/5/4/4 = **28**。
- **Original problem / old design:** 从训练开始固定最大 context length，优化和数据管线简单，适合短序列为主的训练；大量 early tokens 尚未需要长上下文，却承担高 attention cost。
- **Changed constraint / mechanism:** 以 short-to-long schedule 逐步扩展 context，末段再回混长度；把 context length 从静态模型配置改成训练 curriculum state。论文同时测试 reverse schedule 与 expansion speed，显示“越快变长”并非单调更好。
- **State ownership / control flow:** data scheduler 决定每阶段 sequence-length distribution，optimizer 延续同一 parameter state，evaluation 分别测短/长能力；比较必须控制 token/FLOP budget 并追踪 optimizer-state continuity。
- **Implementation / evaluation contract:** 120M ablation 与 1B/3B models；1B 约 100B tokens、最高 32K，3B 最高 8K；code setting 用 HumanEval/BigCode。initial length 8，过慢扩展会伤害 long-context，reverse schedule 作为方向性 ablation。
- **Evidence boundary / trade-off:** 证明 curriculum length distribution 在作者 token budget 下改善 training efficiency/long-context acquisition；不证明任意 tokenizer、RoPE scaling、architecture 或 equal-wall-clock production training。hardware 未披露，token-equal 不等于 FLOP/energy-equal。
- **Coexistence / evolution:** fixed length 在长度分布稳定、data packing 简单或 optimizer transients 风险高时仍合理；演进是 `fixed max length → staged length curriculum → workload-aware mixed-length schedule`。Owner `TRAIN-PRETRAINING`，handoff `MODEL-LONG-CONTEXT` / `TRAIN-DATA`；disposition `Emerging / Experimental`。

#### φ-Decoding — 2503.13288 v1，03-17

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** autoregressive CoT 每一步只按当前 prefix 选择下一步，计算便宜但 myopic；ToT/MCTS 用 branching/backtracking 补全 future awareness，却在大搜索空间中支付大量无效 exploration。
- **Changed constraint / mechanism:** φ-Decoding 对每个 step beam 先生成候选，再 rollout future steps。它用相邻时间的平均 log-prob 差构造 dynamic advantage，用 foresight paths 的 cluster size 构造 alignment，合并两个分布后采样；不依赖 external PRM。width pruning 删除低于 `μ−σ` 的候选，depth pruning 在最大 cluster 占比达到 δ=.7 后切回普通 autoregressive completion。
- **State ownership / control flow:** decoder/orchestrator 持有 beam、candidate confidence、foresight paths、cluster assignment 与 stopping threshold。M=4、每 beam N=4 rollouts，K=3；不同模型/任务用不同 `(Tmin,Tmax)`（普通任务约 1–8，AIME 16–32），说明 search budget 是请求级 policy state，而不是模型固有能力。
- **Implementation / evaluation contract:** GSM8K、MATH-500、GPQA、ReClor、LogiQA、ARC-Challenge 和 AIME；Llama-3.1-8B/Mistral-7B 为主，并测试 Qwen2.5-3B、Llama-3.1-70B、R1-Distill-Llama-8B。A100 80GB、vLLM，Pass@1 与估算 FLOPs；对比 CoT、ToT-BFS、RaP-MCTS、Guided Decoding、Predictive Decoding。Llama-3.1-8B 平均相对 CoT 提升超过 14%；Qwen2.5-3B 六任务平均 53.66→57.46；作者称在一个 compute-matched point 可约 6× 更省。
- **Evidence boundary / trade-off:** 证明 self-foresight + adaptive pruning 在上述 reasoning workloads 的 accuracy/FLOPs frontier 有效；不证明 wall-clock/P99、并发 serving、token-cache reuse 或事实任务。TF-IDF cluster 与等权 `τ1=τ2=.6` 是手工选择；self-confidence/majority 仍可能 correlated wrong，cluster 与 rollout cost 随 beam/depth 放大。
- **Coexistence / evolution:** greedy/CoT 在低风险、短 horizon 与严格 latency 下仍合理；tree search 在强 verifier、探索覆盖优先时仍可取。演进是 `greedy local choice → exhaustive search → sampled foresight → adaptive width/depth budget`。Owner 应为 `MODEL-SAMPLING`（不是 `AGENT-PLANNING`），handoff `INFER-DECODING` / `AGENT-PLANNING`；disposition `Integrate — New Mechanism` candidate。

#### Inside-Out: Hidden Factual Knowledge in LLMs — 2503.15299 v1，03-19

- **Score:** 5/5/4/5/5/5 = **29**。
- **Original problem / old design:** 用单次 greedy answer 或 token likelihood 判定“模型知道什么”可部署且直观；但 generation path、prompt wording 与 length bias 会把 representation 中可区分的事实和可生成答案混为一谈。
- **Changed constraint / mechanism:** 论文把 knowledge 定义为 scoring method 在同一问题内，把 correct answer 排在 plausible incorrect answer 之前的 pairwise fraction。external scorer 只用 observable token probabilities（raw、length-normalized、P(True)）；internal scorer 用 question-answer hidden state 上的 linear probe。只有 internal knowledge 显著超过所测试 external functions 才称 hidden knowledge。
- **State ownership / control flow:** base model weights/hidden state 持有 representation；decoder 决定 candidate reachability；probe 只负责 ranking，不生成 candidate。因此“模型能识别正确候选”与“模型能把该候选采样出来”是两个 owner contract，repeated sampling 无法修复 support/decoding gap。
- **Implementation / evaluation contract:** Llama-3-8B-Instruct、Mistral-7B-Instruct、Gemma-2-9B-Instruct；EntityQuestions 四个 single-answer relations，约 1.7K test、约 200 dev、2K probe-training questions。每题 greedy + temperature 1 的 1,000 samples，并把缺失 gold 人工加入；LLM judge 标注；one probe per layer，以 dev 选层。internal vs best external 的平均相对 gap 约 40%，模型间约 14%–57%；56% 问题 1,000 次全错，9% 问题却把未生成 gold 评为 internal top-1。
- **Baselines / ablations / outcome:** external raw probability、length-normalized probability、P(True)；1,000 candidates 内 probe top-selection 相对 greedy 平均 +12.1%，但 oracle +108.8%；若把 gold 强行加入，probe 可 +52.7%。这证明 verifier/ranker 仍受 candidate recall 上限约束。
- **Evidence boundary / trade-off:** 只覆盖 closed-book、短 entity QA、四种 relation、7–9B open models；不证明 probe 表示因果“knowledge”、长答案或开放域事实。成本很高；K* 对 judge labeling error 敏感；未覆盖 related-fact consistency，hardware 未披露。probe 的训练与 layer selection 也引入 dataset-specific observer。
- **Coexistence / evolution:** output likelihood 仍适合低成本 online signal，retrieval/verifier 仍适合可提供候选的任务；该工作补充的是 `generation outcome → candidate ranking → internal representation score → candidate-recall boundary`。Owner `WORLDVIEW-REPRESENTATION`，handoff `MODEL-SAMPLING` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### Reinforcement Learning for Reasoning in Small LLMs — 2503.16219 v1，03-20

- **Score:** 4/5/5/5/5/4 = **28**。
- **Original problem / old design:** reasoning RL 常用大模型、大数据、多阶段 SFT/RL；稳定但昂贵。小模型直接 GRPO 可省 critic 与资源，但容量、sequence length 和 reward misspecification 使稳定区间更窄。
- **Changed constraint / mechanism:** DeepSeek-R1-Distill-Qwen-1.5B 跳过 SFT，直接用 GRPO group-normalized outcome reward；accuracy reward 检查 boxed answer，format reward 约束 `<think>`，第三实验用 cosine length reward。data curriculum 从 hard-only 改成 3K open-s1 + 3K open-deepscaler + 1K easier problems。
- **State ownership / control flow:** rollout group（6 samples/prompt）产生相对 advantage；rule verifier 持有 correctness/format，cosine scheduler 把 length 纳入 reward；policy optimizer 持有 KL 与 checkpoint。超过最优早期 checkpoint 后，policy 会 length rebound、KL unstable、mixed-language drift，说明 checkpoint selection/release gate 是机制的一部分。
- **Implementation / evaluation contract:** 4×NVIDIA A40 48GB、24h、bf16、vLLM eager、GPU memory utilization .7、gradient checkpointing；lr 1e-6、cosine min-rate .1、warmup .1、per-device batch 6、grad accumulation 4、6 generations、temperature .7、seed 42、max prompt 512、completion 3584/4096。原始 curated pool 39,659；主要实验 7,000 samples。
- **Evaluation / ablation:** AIME24 30、MATH-500 500、AMC23 40、Minerva 272、OlympiadBench 675，zero-shot Pass@1/lighteval。hard-only 在 50–100 steps 先升后于 200 steps 崩；mix curriculum 在 50–100 steps 得 AMC23 63→80、MATH-500 83→85，150–200 后退化；cosine reward 稳定 length 但峰值降为 AMC23 72.5。best checkpoints 平均 53.0–56.3，仍低于 DeepScaleR-1.5B 的 57.0；AIME 单项 46.7 高但只有 30 题。
- **Evidence boundary / trade-off:** 证明在单一 1.5B distilled base、math verifier 与严格资源合同中，RL 快速 elicitation 有效且存在 narrow early-stopping window；不证明能力“新生”、跨领域 generalization 或与所有 baseline 的成本严格可比。$42 来自 RunPod price estimate；closed/proprietary baseline numbers 不是同环境复现。
- **Coexistence / evolution:** SFT/大规模 multi-stage RL 在稳定性、格式 bootstrapping 与跨域时仍合理；演进是 `large-scale RL → critic-free GRPO → compact curriculum → length-aware reward → checkpoint/release control`。Owner `TRAIN-GRPO`，handoff `TRAIN-CHECKPOINT` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### DeepMesh — 2503.15265 v1，03-19

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** Marching Cubes 从 implicit field 提取 dense mesh，几何覆盖可靠但 topology 稠密、难编辑；早期 autoregressive mesh tokenization 直接序列化 faces，能学习 artist-like topology，却因重复 vertex、长序列和低质 3D data 在高 face count 时训练昂贵且 loss spike。
- **Changed constraint / mechanism:** DeepMesh 先按 connectivity 做 local face traversal，再以三级 block 的 offset index 编码并合并相同 index；在 512-resolution mesh 上把序列压到 vanilla 的约 28%，同时把 vocabulary 控制在 4,736。训练侧用 face-count bucket、fixed-window truncated/sliding training 和 Hourglass Transformer；post-training 以 Chamfer threshold 先过滤 geometry-invalid pair，再由人工比较 aesthetic，形成 5,000 对 DPO preference。
- **State ownership / control flow:** tokenizer 持有 vertex/face traversal 与 block-offset identity；data pipeline 持有 geometry-quality filter、face-count bucket 和 window boundary；autoregressive transformer 在 self-attention/cross-attention 下生成 mesh token；preference pipeline 用 Chamfer 与 volunteer judgement 决定 chosen/rejected；DPO policy/reference 更新生成分布。截断窗口与 topology continuation 是训练状态，不能被当作无条件完整 mesh guarantee。
- **Implementation / evaluation contract:** 约 500K meshes、平均约 8K faces，混合 ShapeNetV2/ABO/HSSD/Objaverse/Objaverse-XL 与 licensed data；point-cloud condition 从每 mesh 20K samples 选 16,384 points。500M/1.1B models；128×A800、4 days，cosine lr 1e-4→1e-5，context 9K；DPO lr 1e-5、10 epochs；temperature .5。100-mesh test、每 surface 1,024 points；对比 MeshAnythingv2/BPT。w/o DPO→DPO 的 Chamfer .1001→.0884、Hausdorff .1861→.1708、user preference 34%→37%；tokenization ablation 在 80 meshes/20K faces 上为 480s，优于 AMT 816s/BPT 540s。
- **Evidence boundary / trade-off:** 证明 representation、data curation 与 preference post-training 的组合能在作者 point-cloud-conditioned contract 改善 topology/geometry；无法把最终提升完全归因于单一机制。user-study 人数与 inter-rater agreement 未披露，image conditioning 实际先经 TRELLIS 转 3D 再采 point cloud；无 inference latency/P99/energy，artifact 当时未给完整 pretrain/DPO reproducibility。作者明确承认 point-cloud low-level feature 丢细节、3D data 有限、只测到 1B。
- **Coexistence / evolution:** implicit field + extraction 在 watertight geometry、任意 topology 与编辑性次要时仍合理；短序列 mesh AR 在低-poly 资产更简单。演进是 `dense extraction → explicit mesh tokens → topology-aware compression → length-aware training → geometry-gated human preference alignment`。Canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-DATA` / `TRAIN-DPO`；disposition `Emerging / Experimental`。

#### DiffMoE — 2503.14487 v1，03-18

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** dense DiT 对各 noise level、condition 和 sample 一视同仁，计算规则但忽略 diffusion token heterogeneity；token-choice 或 per-sample expert-choice MoE 固定 top-k/capacity，便于 budget，却让 expert 只见 isolated/local token distribution，难形成跨 noise/sample specialization。
- **Changed constraint / mechanism:** 训练时把 batch 的 `B×S` tokens 合并成 global pool，让每个 expert 在全局 affinity 上选 token；以 `C = (1/LN)Σ C_E` 明确 normalized capacity，令所有模型 training capacity=1。推理时 capacity predictor 从 training routing patterns 产生 token-expert score，并用 per-layer/per-expert threshold 选择可变 token 数；EMA quantile（α=.95）学习 dynamic threshold，使 average inference capacity 约为 1，而不是每 token 固定激活。
- **State ownership / control flow:** router/capacity predictor 写 affinity；global selector 跨 sample 决定 expert token set；threshold ledger 按 layer/expert 持有 EMA quantile；experts 处理选中 token 后 scatter 回原 sample。capacity budget 从 token-local owner 上移到 batch/layer global owner，因此 distributed implementation 会新增 cross-sample coupling、all-to-all/placement 与 batch-shape dependency，论文未把这些 deployment contract 闭合。
- **Implementation / evaluation contract:** ImageNet 256×256、1,281,167 train images，horizontal flip，AdamW lr 1e-4、weight decay 0、global batch 256、EMA .9999；多数实验 4×H800，SOTA run 8×H800。T2I pretraining 用 32×H800 internal data，再用 JourneyDB SFT。对比 dense DiT、TC-DiT、EC-DiT；700K interaction ablation 中 global dynamic 454M active parameters FID50K 14.41，优于 dense 675M 的 14.77；7M-step E8 在 CFG1.5 的 DDPM/Flow FID 2.30/2.13。T2I GenEval without/with SFT .44/.51 vs dense .38/.49。
- **Baselines / ablations / sensitivity:** L1 isolated、L2 intra-sample、L3 cross-sample 分离 token accessibility；interval threshold γ≈.4 与 dynamic threshold 均落入最佳 capacity region，FID 对过激活/欠激活呈 U-shape。batch size、CFG、Euler/Heun/Dopri5、VAE ft-MSE/ft-EMA 都显著改变 FID，作者也明确指出 FID 对 sampler、hardware、seed、sample count 敏感；因此“1× active beats 3×”只能绑定同一作者 protocol/训练步数。
- **Evidence boundary / trade-off:** 证明 diffusion workload 中 global token accessibility 与 dynamic capacity allocation 在作者 ImageNet/T2I contract 有效；不证明 LLM MoE、online small-batch、end-to-end latency/throughput、跨节点通信或 text-to-video。T2I 训练数据私有，缺 placement/communication overhead；dynamic threshold 新增 batch-dependent variance、starvation、capacity drift 与 reproducibility failure mode。
- **Coexistence / evolution:** dense DiT 在小模型、小 batch、deterministic latency 与通信受限时仍合理；fixed top-k 在 serving budget 严格时更可控。演进是 `uniform dense → token-local fixed MoE → sample-local expert choice → batch-global specialization → learned inference capacity`。Owner `MODEL-MOE`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `TRAIN-DISTRIBUTED-TRAINING` / `INFER-DISTRIBUTED`；与 Expert Race 是同周 alternative branch，不是重复 family。disposition `Integrate — New Mechanism` candidate。

#### JARVIS-VLA / ActVLP — 2503.16365 v1，03-20

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** VLA 常直接对 trajectory 做 imitation learning；当 foundation VLM 已具备足够 perception/grounding 时这最短路径合理，但 open-world partially observable task 会把 world knowledge、visual recognition、spatial grounding 的缺口全部压给有限 trajectory，action imitation 无法识别上游 representation failure。
- **Changed constraint / mechanism:** ActVLP 在 action imitation 前加入两段 non-trajectory post-training：先做 Minecraft world-knowledge text SFT，再做 caption/VQA 与 grounding visual-language SFT，最后才在 trajectory 上全参数微调 language transformer。vision modules 在 action stage 冻结；action decoder 把 keyboard 与 mouse bins 扩展为 51 tokens，并以 action chunk `a[t:t+τ]` 学习未来控制。
- **State ownership / control flow:** observation history 进入 prompt，VLM 持有 non-Markov temporal context；visual encoder/projector 写 multimodal state，language transformer 预测 action tokens；推理按 keybutton→camera Y→camera X 顺序 token-by-token commit。world/visual/grounding datasets 改 representation，trajectory owner 改 policy；环境 success verifier 才拥有 outcome truth，模型 token probability 不是 physical correctness。
- **Implementation / evaluation contract:** Qwen2-VL-7B 与 Llava-Next-8B；277K world-knowledge、35K caption/QA、404K grounding、7.4M gameplay frames。AdamW β=(.9,.95)、lr 5e-6、bf16、seed42、32×A800-80GB、ZeRO-1；visual-language stage max length 3584、per-device batch2、grad-accum4、128 GPU-hours；action stage length512、batch8、512 GPU-hours，总 batch256。inference 单 RTX3090/vLLM。MCU atomic tasks 每项至少 30 runs，对比 VPT-BC/RL、STEVE-1、GROOT、MineDreamer；JARVIS-Qwen category success 大幅高于 Qwen2-VL IL，尤其 smelt .70 vs .29。spatial-grounding-only ablation 对 downstream 帮助最大，且 trajectory scaling 只有在 eval loss 降到约 .30 以下才出现非零 success。
- **Evidence boundary / trade-off:** 证明 off-trajectory capability supervision 能在 Minecraft 1K+ atomic-task family 改善后续 imitation；不证明 physical robot/sim-to-real、open-world causal planning、long-horizon safety 或“40%”是所有 task 的 absolute gain。vision-language benchmark 部分由作者编写且用 LLM-as-judge；history prompt 增加 context/latency，action autoregression 缺实时 guarantee。作者明确指出 VLM 规模限制 throughput、目标 >40Hz 尚未达到，且仍低于 >90% human success。
- **Coexistence / evolution:** 纯 imitation 在 observation/action schema 稳定、trajectory coverage 高且低 latency 时更直接；modular planner/controller 在可解释 recovery 与 hard safety boundary 下仍必要。演进是 `trajectory imitation → capability-targeted VLM post-training → unified action tokens → history-conditioned action chunks → environment feedback`。Owner `MULTIMODAL-EMBODIED-VLA`，handoff `TRAIN-SFT` / `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Integrate — New Mechanism` candidate。

#### FlashVDM / Unleashing Vecset Diffusion — 2503.16302 v1，03-20

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** Vecset Diffusion 用 cross-attention 把 surface point cloud 压成 unordered latent set，并可在任意 volume resolution 查询 SDF；灵活且可扩展，但 384³ 已有逾 56M queries，Hunyuan3D-2 的 volume decoding 占 75.8%、diffusion sampling 占 23.9%，单纯减少 denoising steps 不会解决端到端瓶颈。
- **Changed constraint / mechanism:** runtime 同时改两条链。decoder 先低分辨率查询，只在 surface sign/tSDF boundary 周围递归升分辨率并 dilation；再按 subvolume sampled-query attention 选择 local KV，并跨 subvolume pack queries；最后缩窄 CA/MLP。sampling 侧以 guidance distillation warmup、EMA target、Huber、五阶段 consistency flow distillation 和 latent adversarial finetuning，把 teacher 压到 5 NFE。
- **State ownership / control flow:** image encoder→DiT latent→hierarchical query frontier→subvolume KV mask→SDF→Marching Cubes；frontier、tSDF threshold、dilation、packed query offsets 与 adaptive KV set 都成为 request/execution-plan state。distillation trainer持有 student/EMA target/teacher/discriminator 四类参数状态，多阶段 checkpoint 之间存在 cascade dependency。
- **Implementation / evaluation contract:** Hunyuan3D-2 1024/3072 vecsets，target resolution 380；baseline 用 FP8 SageAttention2 与 `torch.compile`。decoder frozen encoder、lr1e-4、batch256、300K/800K；distillation batch256，guidance w∼U[2,8]、20K，五 phase 20K+8K finetune，EMA .999；adversarial 5K、λ=.1。VAE 22.33s→.491s，V/S-IoU 96.11/93.27→95.55/93.10；generation 34.85s→1.041s，ULIP-I .1303→.1260、Uni3D-I .3151→.3095，并与 TripoSR/SF3D/SPAR3D/Trellis 比较。
- **Evidence boundary / trade-off:** 证明“优化 dominant stage + sparse state-aware execution + few-step distillation”在单一 Hunyuan3D-2 pipeline 可取得 32× overall；不证明通用 3D model、并发/P99、显存/energy 或 production scheduler。硬件只称 consumer GPU，未给精确型号；PyTorch indexing 尚未 fusion；tSDF/dilation 防洞但增加 query；多阶段 distillation 明示会积累 cascade errors。
- **Coexistence / evolution:** dense volume query 在低 resolution、拓扑完整性优先与 locality prior 不稳时仍最安全；feed-forward 3D 在质量预算较松时更快。演进是 `dense arbitrary-resolution decode → surface-aware hierarchical queries → local adaptive KV → packed sparse execution → progressive few-step sampling`。Canonical owner `INFER-EXECUTION`（census proposed generative owner 应修正），handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `INFER-KV-CACHE`；disposition `Integrate — New Mechanism` candidate。

#### Scale-wise Distillation of Diffusion Models (SwD) — 2503.16397 v1，03-20

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** full-resolution few-step diffusion 每一步处理 1024² latent，控制简单且不引入 scale mismatch；但早期高噪声阶段主要建立低频结构，高频计算尚无价值。直接放大 noisy latent 又产生严重 OOD（64→128 的 FID 可到 129.7–340.2）。
- **Changed constraint / mechanism:** SwD 为每个 denoising timestep 绑定 resolution schedule；先将当前 clean prediction `x0_hat` bicubic upscale，再重新注入对应 timestep noise，而不是 upscale noisy state。它在 DMD2 的 student/fake-DM/discriminator 框架上用 LoRA rank64，并以 feature-token distribution matching 的 patch loss补局部细节；teacher synthetic samples 保持训练分布。
- **State ownership / control flow:** sampler 持有 `(t_i,s_i)` pair、clean prediction、noise re-injection 与 resolution transition；student/teacher/fake model 分持 real/fake score，discriminator在 fake model layer11 features 上判断 distribution。scale schedule 是 model-training/inference contract，不能在未 scale-wise distilled 的 full-scale model 上随意启用。
- **Implementation / evaluation contract:** SD3.5 Medium/Large，synthetic teacher 40/28 steps、CFG4.5；8×A100 单节点，LoRA attention+MLP，lr4e-6、batch80、3–5K iterations。6-step scale `[256,384,512,640,768,1024]`、4-step `[256,512,768,1024]`；单 A100 FP16、`torch.compile`、batch8、100 runs。Medium 4-step .14s vs full-scale .26s，Large .32 vs .63；训练 21 vs41 s/iter、18 vs27。30K COCO/MJHQ 用 PickScore/CLIP/ImageReward/FID/GenEval，并有人评。
- **Ablations / evidence boundary:** 去 time shift、constant scale、用 full-scale-trained model 或 real data 均退化；去 PDM 的 MJHQ FID 13.6→19.3，naive token-wise loss更差。证明频率/scale-aware compute allocation可改善 few-step quality-latency frontier；不证明任意 diffusion latent、video temporal coherence、dynamic request schedule 或 SLO。human eval仍见轻微 complexity/aesthetics loss，论文无独立 limitations，schedule 手工且 synthetic teacher data 可能继承 bias。
- **Coexistence / evolution:** full-scale sampling 在 exact teacher fidelity、低分辨率或 schedule 管理成本不值得时仍合理；演进是 `all-step full scale → implicit spectral ordering → timestep-bound scale schedule → clean-state upscale + renoise → adaptive scale candidate`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `INFER-EXECUTION` / `TRAIN-LORA`；disposition `Integrate — New Mechanism` candidate。

#### InfiniteYou / InfuseNet — 2503.16418 v1，03-20

- **Score:** 4/4/4/5/5/4 = **26**。
- **Original problem / old design:** IP-Adapter 在 attention layer 把 identity 与 text 同位注入，部署方便；但在 FLUX/DiT 上会把 identity-copy pressure 与 prompt semantics 纠缠，出现 text alignment、hands/background/aesthetics 退化和 face copy-paste。
- **Changed constraint / mechanism:** 冻结 FLUX.1-dev MMDiT 主干，将 identity encoder 的 8 projected tokens交给较浅 InfuseNet control branch（base block 数是 branch 的4倍），通过 residual/control feature 注入而非修改 base attention owner。训练先用 real identity data学习相似性，再以 single-person-multiple-sample synthetic pairs做 stage-2 SFT，主动交换 identity fidelity 与 prompt/editability。
- **State ownership / control flow:** frozen text encoder/base DiT持有通用生成能力；identity encoder/projection 持有 subject identity；InfuseNet持有 control residual；SPMS pairing 持有 reference→synthetic target provenance。主干冻结保护通用分布，但 branch 仍可过强导致 identity dominance，因此 identity/text 权重是显式 trade-off，不是单一“越像越好”指标。
- **Implementation / evaluation contract:** PyTorch/Diffusers/FSDP，128×H100-80GB stage1、lr2e-5、batch512、300K；stage2 64×H100、lr1e-5、batch256；AdamW β(.9,.999)、wd.01、conditional flow matching。70 sets/16 participants user study；对比 FLUX IPA、PuLID-FLUX。ID Loss/CLIP/Pick 为 InfU .209/.318/.221，PuLID .225/.286/.212；overall human preference 72.8% vs27.2%。ablation显示去 stage2 identity loss更低(.172)但 CLIP/Pick 更差，说明是多目标 Pareto 而非单调提升。
- **Evidence boundary / trade-off:** 证明 control-branch ownership 与 SPMS multi-stage training在该 face-personalization workload比同位 attention injection更平衡；不证明任意 identity、multi-subject、视频或 abuse prevention。训练数据规模/来源与完整 test-set identity/pose distribution未披露；metric 对 face encoder/CLIP/Pick bias敏感，128 H100成本大。作者承认 identity/quality仍可提升且 deepfake misuse存在。
- **Coexistence / evolution:** IPA 在轻量 plugin、style transfer与资源受限场景仍合适，甚至论文保留其 style handoff；演进是 `attention-level identity plugin → modality conflict → frozen base + dedicated control branch → real-identity pretrain → SPMS SFT trade-off`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-SFT` / `PLATFORM-SECURITY`；disposition `Emerging / Experimental`。

#### Fin-R1 — 2503.16252 v1，03-20

- **Score:** 4/4/4/4/5/3 = **24**。
- **Original problem / old design:** general Qwen2.5-7B 能遵循金融问答格式，却缺 domain numeric reasoning；直接 SFT 最稳且成本较低，但会把 teacher CoT、格式和答案一起 imitation，无法按可验证 outcome继续优化。
- **Changed constraint / mechanism:** DeepSeek-R1先生成 CoT；reference exact-answer filter剔除错误结果，Qwen2.5-72B judge再选择 reasoning trajectory。Qwen2.5-7B-Instruct先在 FinQA/ConvFinQA SFT，再用 GRPO group-relative advantage；format reward强制 `<think>/<answer>`，accuracy reward由 Qwen2.5-Max judge判 semantic-equivalent final answer。
- **State ownership / control flow:** source dataset/reference持有 expected answer；teacher生成 reasoning；filter/judge决定 SFT provenance；GRPO rollout group决定相对 advantage；external judge持有 reward。模型无法自行拥有 correctness，且 judge同时进入 data selection、reward与evaluation，会形成 correlated evaluation loop。
- **Implementation / evaluation contract:** data mixture列出 Finance-Instruct-500K、FinanceIQ、FinPEE、Ant-Finance、FinCorpus、FinQA、ConvFinQA、TFNS、FinCUGE；但 SFT/RL重点仅 FinQA/ConvFinQA。对比 DeepSeek-R1及Qwen/Distill 7B–70B；Fin-R1 overall 75.2、FinQA76、ConvFinQA85；SFT-only overall71.9。论文未披露 GPU、precision、batch、GRPO group size、learning rate、训练步数或显著性。
- **Evidence boundary / trade-off:** 证明在作者 benchmark/judge contract中，SFT→GRPO对7B finance QA有增益；不证明开放域金融、真实合规/风险管理或训练题外 generalization。FinQA/ConvFinQA既训练又报告领先，Qwen2.5-Max semantic judge可引入 family bias；closed-answer、单模态、dataset coverage窄为作者明确 limitations。因此不把 headline“接近R1”写成通用效率结论。
- **Coexistence / evolution:** 单纯 SFT 在 judge不可靠、答案开放或 reward成本高时更可审计；rule verifier在规范化数值任务可能比 LLM judge更稳。演进是 `domain SFT → teacher-CoT filtering → judge-selected traces → group-relative outcome optimization → verifier/judge governance`。Owner `TRAIN-GRPO`，handoff `TRAIN-DATA` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Emerging / Experimental`。

#### Cube: A Roblox View of 3D Intelligence — 2503.15475 v1，03-19

- **Score:** 5/4/4/5/5/4 = **27**。
- **Original problem / old design:** continuous 3D latent 能保留几何细节，且对 reconstruction 友好；但无法像 text token 一样直接进入统一 autoregressive sequence，而普通 sinusoidal encoding 在 dot-product attention 下会让空间上远离的点产生相似 embedding。3D data 同时稀缺、多模态且输出规模不定，单一 object encoder 不能承担跨模态输入/输出 contract。
- **Changed constraint / mechanism:** pipeline 从 mesh surface 采样 8,192 points，用 phase-modulated positional encoding 同时保留高频细节和远点可分性；13-layer Perceiver encoder 将点云压成 512 continuous latents，OptVQ 映射到 16,384 codebook。为处理 VQ 不可微与 loss spike，训练以 50% 概率走一个可学习 linear shortcut 绕过 quantizer，并用 EMA teacher/full-query 对 student/masked-query 的 prototype cross-entropy 约束 latent geometry。
- **State ownership / control flow:** mesh/point coordinate 持有几何事实；encoder latent 持有连续形状状态；codebook index 持有离散 token identity；occupancy decoder 再把 token 恢复成 implicit field。linear shortcut 只在训练中持有可微 teacher-like path，推理不能把它误当作 bypass VQ 的无损路径。下游 text-to-shape 由 CLIP text、dual-stream attention 和 AR shape-token decoder拥有生成控制；shape-to-text 则冻结 tokenizer，通过 projection 对齐 InternVL2.5-2B。
- **Implementation / evaluation contract:** encoder/decoder 为 13/24 layers、width768、12 heads、总计273M；code embedding 32-D，PMPE β=.125，SSL λ=.0005。约1.5M licensed/public/Roblox opt-in assets；每 asset 另采 8,192 occupancy points。Toys4K OOD reconstruction 中 CraftsMan S/V-IoU 68.8/83.6，Cube-VQ 91.7/94.5，same-architecture continuous-KL 94.8/95.4；这直接暴露离散化 fidelity 税。text-to-shape captions 来自 GPT-4o，训练中10% text dropout做 CFG；scene JSON 仅 flat objects，orientation 只支持 Y-axis rotation。
- **Evidence boundary / trade-off:** 证明 PMPE、linear shortcut、self-supervised latent regularization 与 OptVQ 能形成可用于多模态 AR 的高质量 3D token；不证明统一 foundation model、生产级 scene reasoning 或 text/shape applications 的相对质量。论文未披露 tokenizer 训练 hardware、batch、optimizer、latency、throughput、显存和 SLO；三类 application 主要是 qualitative，cycle consistency仍丢高频细节，continuous variant依然更准。
- **Coexistence / evolution:** continuous latent 在重建 fidelity、无需 discrete AR interleave 或固定 3D pipeline 中仍更合适；演进是 `continuous geometry latent → attention-compatible spatial encoding → discrete shape identity → gradient-stabilized quantization → shared multimodal token contract`。Owner `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `AGENT-WORKFLOW`；disposition `Integrate — New Mechanism` candidate。

#### SynCity: Training-Free Generation of 3D Worlds — 2503.16420 v1，03-20

- **Score:** 4/4/4/5/5/3 = **25**。
- **Original problem / old design:** image/depth outpainting 可借强 2D prior 扩展可视区域，但大场景 3D coherence 很快漂移；直接 3D generation 几何规整，却大多 object-centric 或受 domain-specific 3D data 约束。直接让 Flux 生成一张“大世界图”再交给 TRELLIS，layout prompt 不能稳定控制对象位置和尺度。
- **Changed constraint / mechanism:** SynCity 不训练新模型，而把 world 拆成按固定顺序生成的 square tile grid。o3-mini-high 产出 world-level 与 tile-specific JSON；Flux ControlNet 在已生成邻居 context、fixed isometric base image 与 mask 上 inpaint；rembg/alpha matting隔离 tile，再添加稍大的灰色 base 让 TRELLIS 重建可检测边界。若 square area/base heuristic失败则换 seed重试，最后在 2D/3D latent/3DGS space裁剪、对齐、blend 与 upsample。
- **State ownership / control flow:** grid coordinate、generation order 和 tile prompt 是 authoritative orchestration state；neighbor render 是局部 continuity context；Flux 只拥有 2D proposal，TRELLIS拥有 per-tile occupancy/latent/3DGS，validator拥有 accept/retry control。这里生成的是静态 scene asset，不拥有 action-conditioned transition、causal dynamics 或可修订 world belief，因此不能归入 `MULTIMODAL-WORLD-MODELS`。
- **Implementation / evaluation contract:** off-the-shelf o3-mini-high、Flux ControlNet、TRELLIS，无训练/optimization。22名参与者对一个 city scene及近景比较 BlockFusion，SynCity overall/geometry/exploration/diversity/realism win rate 为90.9/81.8/90.9/90.9/86.4。ablation显示移除 neighbor context会导致跨 tile scale不一致；rebasing 使 base area 2271→4096、squareness .92→1.00、completeness .73→1.00。论文未披露 GPU、per-tile latency、retry rate、world-size scaling、memory或完整 cost。
- **Evidence boundary / trade-off:** 证明“结构化分解 + context-conditioned proposal + geometry validation/retry + typed blending”可以复用现有 generators生成可导航大场景；不证明 dynamic world model、物理一致性、无限扩展或对比训练式方法的同预算优势。human study规模小且只有单一 scene pair；atomic tiles依旧可见，heuristics/fallback不保证成功，TRELLIS对 Flux颜色有时只模糊遵循。
- **Coexistence / evolution:** 单对象 generator、procedural domain generator和训练式 scene model在一致性、吞吐或确定性更重要时仍成立；演进是 `single-object generation → one-shot scene prompt failure → tile decomposition → neighbor-conditioned proposals → validator/retry → latent/geometry blending`。Canonical owner 修正为 `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `AGENT-WORKFLOW` / `MULTIMODAL-WORLD-MODELS`（用于明确静态生成边界）；disposition `Emerging / Experimental`。

#### MathFusion — 2503.16212 v1，03-20

- **Score:** 4/4/5/5/5/4 = **27**。
- **Original problem / old design:** rephrase、难度改写、多解答与单题反思能扩大 instruction data，且 provenance简单；但它们围绕单一问题变体，未显式训练不同数学问题之间的依赖、并行组合和条件选择。随机拼接又容易制造不连贯或不可解样本。
- **Changed constraint / mechanism:** 先以 embedding similarity 为每题检索相似题对，再由 GPT-4o-mini-2024-07-18（temperature .7、max4096）构造三类合成：sequential 把A答案作为B输入，parallel把两个子问题合成共同目标，conditional依据 context比较/选择两者结果。GSM8K 与 MATH 原始15K加三路 fusion形成60K MathFusionQA；同一 teacher生成问题与答案，并另用 rejection-like verification识别不合理样本。
- **State ownership / control flow:** source pair与embedding neighbor持有组合 provenance；fusion strategy决定 dependency graph；teacher持有生成与初步验证；dataset manifest必须保存原题ID、strategy、teacher version和过滤状态，否则无法区分真实 compositional benefit与teacher imitation。约5.6% fused problems被 judge判不合理，五次 temperature1.0 regeneration仍失败才丢弃。
- **Implementation / evaluation contract:** DeepSeekMath-7B、Mistral-7B、Llama3-8B用 LLaMA-Factory，3 epochs、global batch128、8×A100、peak lr5e-6、3% linear warmup+cosine、length4096。六个 benchmark 为 GSM8K/MATH/CollegeMath2818/DeepMind1000/OlympiadBench text-English675/TheoremQA800。DeepSeekMath standard15K avg27.5，三路30K为45.7/45.3/42.3，full60K为47.5、近似60K DART 47.4；Llama3三随机 run standard avg21.7±.5，MathFusion39.0±.1。逐 strategy ablation、data-size sensitivity、teacher-rewrite control均存在。
- **Evidence boundary / trade-off:** 证明 pairwise structured synthesis在三种7–8B base和这些 math datasets上比同量简单 rewrite/若干 downsample baseline更高效；不证明“数据更分散”导致 generalization，t-SNE只是描述。teacher同时生成/验证会相关失效，训练/测试都来自有限 benchmark family，融合后的题仍会错误或含糊；三题以上 fusion、不同 retrieval和污染检查未闭合。
- **Coexistence / evolution:** 高质量人工题、单题 hard-example mining与多解答在 teacher bias不可接受、pair关系弱或 verifier严格时仍更可靠；演进是 `single-instance augmentation → relation-aware pairing → typed dependency fusion → provenance/verification → multi-source curriculum candidate`。Owner `TRAIN-DATA`，handoff `TRAIN-SFT` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### FluxFlow / Temporal Regularization — 2503.15417 v1，03-19

- **Score:** 4/4/4/5/5/3 = **25**。
- **Original problem / old design:** video generator按原始时间顺序训练，最大限度保留自然运动监督且无需额外 hyperparameter；但固定顺序让模型缺乏对 temporal perturbation 的辨别压力，长于训练 horizon时 motion/identity consistency显著退化。修改时空 attention或加入显式 flow/physics module有效但需要 architecture-specific成本。
- **Changed constraint / mechanism:** FluxFlow只改训练样本。frame mode随机选 `floor(αN)` 帧并重排；block mode把序列切成 non-overlap size-k blocks，再重排 `floor(βM)` 个 blocks，保留 block内部 motion。它把 order disturbance作为 regularization，不改变 diffusion noise objective或 AR next-token objective；不同 frame length须独立选择 perturbation，超过半数帧会因正确 temporal context不足而退化。
- **State ownership / control flow:** data loader/augmenter持有原序列、shuffle mask、block boundary和 perturbed order；model权重只看到被扰动条件，不拥有显式 optical-flow state。augmentation seed、α/β/k与base frame length因此是训练 provenance，不能在 deployment临时开启；extra-term generation收益来自 learned representation而非新的 runtime controller。
- **Implementation / evaluation contract:** VideoCrafter2（U-Net，16×320×512）、NOVA-0.6B（AR，33 frames）和 CogVideoX-2B（DiT，49×480×720）在 OpenVidHD-0.4M上按默认 config追加1 epoch；对照使用同设置但无 augmentation。UCF-101 13,320 videos/101 classes报告 FVD/IS，VBench报告5项 temporal、2项 frame-wise和总分。CogVideoX original total80.34，2-frame shuffle81.36；不同模型最优 strength不同。20 video pairs、10参与者以0–5评价 motion diversity/realism/smoothness/coherence/flow consistency；另测16-frame VC2外推128 frames和 interval/perturbation sensitivity。
- **Evidence boundary / trade-off:** 证明简单 temporal shuffle可跨 U-Net/DiT/AR三种作者配置改善若干 temporal指标，且无须改架构；不证明真正学到 physics/causal dynamics，也不保证所有 spatial metric不降——部分 setting 的 background/aesthetic/semantic会退化。论文未披露 GPU、batch、precision、learning rate、训练成本或显著性；10人主观研究较小，只有 frame/block shuffle，context-aware与motion-aware augmentation仍未验证。
- **Coexistence / evolution:** 原始顺序训练在数据少、细粒度顺序不可破坏、短 horizon或模型对 perturbation敏感时更安全；演进是 `fixed temporal supervision → controlled order perturbation → model-specific strength → motion/context-aware augmentation candidate`。Canonical owner修正为 `TRAIN-DATA`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Emerging / Experimental`。

#### MetaLadder — 2503.14891 v1，03-19

- **Score:** 4/4/5/5/5/4 = **27**。
- **Original problem / old design:** 普通 math SFT 把问题直接映射到 CoT 与答案，数据契约简单、推理路径短；但它不显式训练模型识别“当前题与哪类已知题共享结构”，因此 relation/analogy 只能隐含地从样本统计中出现。检索一个相似例题可显式提供类比，却增加 inference context、retrieval provenance 与错误示例污染。
- **Changed constraint / mechanism:** GPT-4o-mini-2024-07-18 先为原题 `Q,C` 生成 problem type / solution method `S`，再生成 analogous `Q',C'`，训练序列为 `Q S Q' C' Q C`。Self-evolution 让已训练模型继续生成 related problems，只保留 final answer 正确的样本，并可反转 Q/Q'；cut/shortcut 推理改为 `Q S Q C`，不再显式生成 analog problem，测试训练后是否已把 analogy 压入权重。
- **State ownership / control flow:** source Q/C 持有可验证答案；teacher 持有 S 与 Q'/C' synthesis；answer filter 只验证终局，不验证 analogy relation 或 reasoning faithfulness；training manifest 必须保存 source pair、teacher version、evolution round 与 reverse/cut 标记。推理时模型生成的 S 是 latent strategy proposal，而不是外部 evidence 或 correctness certificate。
- **Implementation / evaluation contract:** GSM8K/MATH 训练，OOD 为 ASDiv、College Math、GaoKao English 2023、DeepMind Math；Llama3-8B 与 DeepSeekMath-7B，LLaMA-Factory，1 epoch、global batch128、AdamW、peak lr5e-6 cosine、8×A100。zero-shot greedy、max generation 2048、Pass@1。Llama CoT 六集 avg 36.1，MetaLadder+SE-cut 42.8；DeepSeek CoT 47.3，reverse+SE-cut 57.6。DeepSeek shortcut 示例总推理时间约 2181.13s→1343.74s，接近 CoT 1253.26s；多轮 self-evolution 呈递减收益/平台。
- **Evidence boundary / trade-off:** 证明 typed analogy synthesis 与正确答案过滤在作者 math contract 上提高 Pass@1，且显式 Q'/C' 可在 inference 被裁掉；不证明模型内部忠实执行 analogy，也不证明 teacher 生成的 S/Q' 正确或适用于开放域。correct-answer filter 会保留碰巧正确、错误类比的轨迹，自演化还会收窄到模型已会解的分布；额外 teacher、样本长度与 evolution round 增加生成/训练成本。
- **Coexistence / evolution:** direct SFT 在题目关系弱、teacher provenance 不可信或 latency/数据成本优先时仍更简单；retrieval-grounded analogy 在必须展示外部证据时仍更可审计。演进是 `direct problem→answer imitation → typed analogy synthesis → verified self-evolution → internalized shortcut`。Canonical owner 修正为 `TRAIN-DATA`，handoff `TRAIN-SFT` / `AGENT-REFLECTION` / `AGENT-RAG`；disposition `Refine — Existing Argument`。

#### LEGION — 2503.15264 v1，03-19

- **Score:** 5/5/4/5/5/4 = **28**。
- **Access correction:** arXiv HTML 错渲染为 author-response LaTeX guideline，但 event-time official PDF `https://arxiv.org/pdf/2503.15264v1` 可完整读取；因此不是 blocker，审计以 15-page v1 PDF 为准。
- **Original problem / old design:** synthetic-image detector 通常输出 binary real/fake 或单一 tamper mask；这对 screening 合理，却不能告诉 generator/controller “哪里违反物理、结构或视觉一致性、怎样修复”。只用 GAN-era 二分类数据也会过拟合低层 generator fingerprints，而不是 human-visible artifact contract。
- **Changed constraint / mechanism:** SynthScars 收集 12,236 fully synthetic images、26,566 artifact instances，12 名专家用 polygon mask + natural-language explanation 标注 physics/distortion/structure 三类缺陷。LEGION 在 GLaMM 上并联 global authenticity classifier、LLM explanation 与 SAM-like pixel grounding；LLM 每个 artifact description 后生成 `<SEG>`，language-to-prompt projection 把该 token 变为 segmentation prompt。Defender 输出 explanation/mask，Controller 以 revision memory 重写 prompt 或逐区域 inpaint，形成检测→定位→修复闭环。
- **State ownership / control flow:** CLIP ViT-H/14 global CLS 持有 whole-image real/fake evidence；256 visual tokens 进入 Vicuna-based LLM 持有 artifact text proposal；SAM encoder/pixel decoder 持有 mask；Controller 持有 prompt/revision memory 与 accept-next-round control。mask、explanation、image revision 必须共享 version identity，否则 controller 可能用 stale localization 修复新图。
- **Implementation / evaluation contract:** SynthScars 11,236 train/1,000 test，human/object/animal/scene 四类，artifact label 约 6% physics、5% distortion、89% structure；12 annotators 合计 240h。Stage1 GLaMM LoRA，8×A100、alpha8、batch2/device、lr1e-4，CE/Dice/BCE loss weights 1/.2/.4；stage2 classifier 在 ProGAN 上，8×A100、lr1e-3、batch64/device。定位测 SynthScars/LOKI/RichHF，对比 HiFi-Net、TruFor、PAL4VST、Ferret、Griffon、LISA、InternVL2、Qwen2-VL、DeepSeek-VL2；explanation 用 ROUGE-L/CSS，LEGION-8B 在 SynthScars 39.50/72.60、LOKI 18.55/45.96。200 样本 refinement 中，2-round SD3.5 regeneration 的 HPS 31.24→33.36，3-round SDXL inpainting 29.57→30.20；另有 JPEG/noise/blur robustness 与 cross-generator detection。
- **Evidence boundary / trade-off:** 证明 typed artifact、text explanation 与 mask 可以组成可执行 refinement contract；不证明通用 deepfake/forensics、修复后事实正确或 HPS 增益等价于 artifact 消失。dataset 89% structure、human-visible defects 与 quality prefilter 带来 selection bias；detector/controller 相关失败、额外 LLM/SAM/多轮 generation 的 latency/cost、复杂场景 subtle artifact miss 是新 failure modes。
- **Coexistence / evolution:** binary detector 在高吞吐 screening、无需修复建议时仍合适；tamper-localization 在局部编辑威胁模型下也不应被 full-synthesis taxonomy 替代。演进是 `binary authenticity → artifact taxonomy → explanation+grounding → versioned repair controller`。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `PLATFORM-SECURITY` / `AGENT-WORKFLOW` / `MULTIMODAL-GENERATIVE-PARADIGMS`；disposition `Integrate — New Mechanism` candidate。

#### ZOODiP: Efficient Personalization of Quantized Diffusion Models without Backpropagation — 2503.14868 v1，03-19

- **Score:** 5/5/4/5/5/3 = **27**。
- **Original problem / old design:** Textual Inversion/LoRA/DreamBooth 依赖 backpropagation，需保存 activations/gradients，且量化后权重/算子往往不可微；在 datacenter GPU 上它们训练快且优化稳定，但个人图像需要 local personalization、显存仅数 GB 时，隐私与 memory 成为主约束。
- **Changed constraint / mechanism:** U-Net、VAE、text encoder 的 Linear/Conv2D 用 optimum-quanto symmetric INT8，embedding/norm 不量化；只学习 pseudo-token。ZO 用随机方向估计 `(L(theta+mu e)-L(theta))/mu * e`，n 次 forward 近似 gradient。Subspace Gradient 从 τ=128 token trajectory 做 PCA，投影掉 noisy/low-variance directions；Partial Uniform Timestep Sampling 只采高噪声区间，利用 text conditioning 在该阶段更强的经验结构。
- **State ownership / control flow:** quantized base artifact 持有 frozen model identity；personal token 持有 user-specific adaptation；ZO optimizer 持有 random direction/seed、finite-difference μ 与 trajectory；PCA subspace、timestep interval、quantization scheme 均属于 training provenance。forward-only 不等于没有隐私风险，personal token/checkpoint 仍可能泄露用户特征。
- **Implementation / evaluation contract:** SD1.5 主实验，DreamBooth 30 subjects、25 prompts、每 prompt 5 images（3,750 outputs），指标 CLIP-T/CLIP-I/DINO。ZOODiP 2.37GB，DreamBooth 19.4GB、QLoRA 7.56GB、PEQA 6.31GB、TuneQDM 8.96GB；ZOODiP .287/.772/.558，TI .285/.778/.559。n=1/2 约 20.7/16.1 iterations/s，n=2 质量更好，但总训练约31min，TuneQDM 1.4min、TI 8.8min；显存换时间。INT4 U-Net 约1.9GB但质量下降，activations仍 BF16；SDXL 约5GB vs FP32 TI 17GB。PUTS ablation 显示 U(500,1000) 有效而 U(0,500) 失败，故区间不是普适常数。
- **Evidence boundary / trade-off:** 证明 forward-only ZO + quantized diffusion 可把 personalization 显存压入 consumer-GPU 范围，同时接近 TI 的作者指标；不证明 mobile/NPU on-device、同 wall-clock 质量或跨 base model/timestep 泛化。训练迭代显著增加，随机估计 variance、PCA trajectory memory、INT4 quality loss 和 base-model/subject limitation都保留；论文未提供真实手机能耗/热约束。
- **Coexistence / evolution:** gradient-based TI/LoRA 在显存充足、训练时延优先与 quantizer 可微时仍更合适；ZO branch 适合 memory/privacy/forward-only contract。Owner `TRAIN-LORA`（当前知识树的通用 parameter-efficient adaptation owner，不表示其机制是 LoRA），handoff `INFER-EXECUTION` / `PLATFORM-SECURITY`；disposition `Emerging / Experimental`。

#### DyDecomp: Optimizing Decomposition for Optimal Claim Verification — 2503.15354 v1，03-19

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** claim verification 常把长 claim 静态拆成尽可能 atomic 的 subclaims；在 verifier context/lookup 弱时这能减小单步复杂度，但过拆会丢上下文、制造 tautology，且 retrieval、in-context、no-context verifier 的最佳 atomicity 不同。固定 decomposition prompt 因而把 verifier-specific operating point 误写成普适原则。
- **Changed constraint / mechanism:** 论文把 decomposition 建模成 MDP：768-D BERT state embedding，GRU state transition 按 CPMI information-loss change 加权；policy 对当前 claim 二选一 decompose/stop，以 breadth-first 选择下一 target。reward 是 verifier positive/negative label probability 的 absolute difference；PPO 学习每种 verification policy 下何时停止。`atomicity=log2(number of atomic information units)`，既可向上 merge，也可继续向 -1 拆分。
- **State ownership / control flow:** decomposer Llama3-Instruct-70B 生成 candidate subclaims；policy/GRU 持有 decomposition history 与 information-loss state；verifier持有 reward operating point；claim label以 all-subclaims-true 聚合。confidence 是 verifier score margin 的优化 proxy，不是 calibrated probability，更不是 end-to-end truth probability。
- **Implementation / evaluation contract:** FActScore 的 ChatGPT/PerplexityAI biography claims，60/20/20 split；retrieval、in-context-example、no-context 三种 verifier。decomposer train temperature .2/eval0，verifier temperature0。PPO epsilon .2、gamma .99、GAE lambda .95、replay512、rollout batch32、max trajectory20、lr3e-5 cosine、100 steps；约4.73M trainable parameters，2×RTX A6000、约80 GPUh。DyDecomp 在两个 dataset/三 verifier、atomicity1/2 平均 verification confidence 约+0.07，并在 PerplexityAI accuracy 约+0.12；one-layer/triple-decompose/no-entropy/cross-atomicity ablations均退化，DeepSeek-V3 check方向一致。
- **Evidence boundary / trade-off:** 证明 decomposition depth 应由 downstream verifier contract 动态选择，而不是“越原子越好”；不证明 reward margin 校准、开放域事实正确或 policy 不会 game verifier。70B decomposer+80 GPUh 对小 policy 成本高，retrieval quality、UNLI/CPMI model 与 biography-domain distribution 都是 confound；all-subclaims rule 还会放大单个 false negative。
- **Coexistence / evolution:** static decomposition 在 schema稳定、verifier固定和成本敏感时仍可复现；dynamic policy适合 verifier/workload异质且有可靠 validation label 的场景。演进是 `fixed atomic split → information-loss-aware state → verifier-conditioned stop policy → calibrated evidence aggregation as next pressure`。Canonical owner 修正为 `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW` / `AGENT-RAG`；disposition `Refine — Existing Argument`。

#### MotionStreamer — 2503.15451 v1，03-19

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** fixed-length diffusion 一次生成整段 motion，适合 offline animation，但不能响应逐轮到达的 text；VQ+GPT 能 autoregressive，却因 non-causal whole-sequence codec 无法即时 decode，离散误差还会沿长序列累积。fixed-window motion primitive 对实时控制有效，但无法利用 variable-length history。
- **Changed constraint / mechanism:** Causal TAE 以 1D causal convolution 把 272-D SMPL pose 压成 continuous latent，每个 latent 只依赖过去；LLaMA-like causal Transformer 结合 T5-XXL text/history 产生 condition，再由 9-layer diffusion MLP head 生成下一 latent。all-zero impossible pose 经 TAE 编成 reference end latent，距离低于 threshold 即停止。Two-Forward 以 cosine schedule 将 first-pass predicted latent 逐步替换 teacher-forced history；Mixed training 同时学习 atomic text-motion 与 contextual triplet，降低 exposure bias 并支持多轮组合。
- **State ownership / control flow:** current text、retained motion history、continuous latent 与 end threshold 组成 streaming state；AR model 负责 next-latent proposal，diffusion head负责局部 stochastic refinement，causal decoder拥有 first-frame commit。论文每一轮只保留最近一段 history 而移除更早段，故不是无界 memory；stop latent 也可能被分布外 pose误触发。
- **Implementation / evaluation contract:** HumanML3D/BABEL original splits，272-D pose、60 FPS；Causal TAE downsample4、train crop64，latent16/hidden1024，2M iterations（1.9M lr5e-5 +100K lr2.5e-6）、batch128。AR 12 layers/12 heads/768，block78，diffusion head1768×9、50 DDPM steps；motion length40–300，10K warmup+90K cosine、batch256，NVIDIA A800（count/precision未披露）。HumanML3D FID10.724/R@3 .851；BABEL subsequence FID15.743 vs FlowMDM18.736、transition FID32.888 vs34.721。VQ-VAE ablation reconstruction/generation FID5.173/11.024，causal continuous .737/10.724；first-frame latency只以图示呈现，未披露并发/SLO。
- **Evidence boundary / trade-off:** 证明 causal continuous codec + two-forward training 可在作者 motion benchmark改善在线 decode与长时一致性；不证明机器人 closed-loop control、physical safety或开放文本组合。50-step diffusion head仍带 per-latent latency，continuous latent失去离散 token 的 compact identity/easy caching，end threshold、history truncation与self-generated exposure都引入 drift/failure mode。
- **Coexistence / evolution:** fixed-length diffusion在整段质量优先、无需交互时仍合理；discrete tokens在检索、压缩、exact identity更重要时仍有优势。演进是 `offline fixed sequence → discrete AR but noncausal codec → causal continuous latent → diffusion-refined next state → exposure-aware streaming`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-EMBODIED-VLA` / `INFER-EXECUTION`；disposition `Integrate — New Mechanism` candidate。

#### Tokenize Image as a Set / TokenSet — 2503.16425 v1，03-20

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** grid/sequence tokenizer把每个 code绑定固定位置，decode和AR建模简单，但对低信息背景与高语义区域分配相同 capacity，且局部 noise 会直接改变对应 token。去掉位置得到 unordered set 后，又出现 factorial permutation、unstable matching和缺 per-element supervision。
- **Changed constraint / mechanism:** ViT encoder输出 M 个 VQ codes，training 时随机 permutation 后仍重建同一图，迫使 decoder学习 multiset identity。Dual transformation 将 token multiset无损转成 codebook-frequency count vector `X∈N^C`，满足 fixed length、discrete value与 `sum X=M`。FSDD从固定和 multinomial noise出发，在每个 diffusion step用 likelihood-preserving greedy adjustment修正 sum，再以 cross-entropy预测 clean count；inference同样逐步维护 conservation invariant。
- **State ownership / control flow:** tokenizer codebook version与 M 决定 set identity；count vector放弃 token顺序/位置但保留 multiplicity；greedy adjuster拥有 hard invariant enforcement，denoiser只负责概率 proposal。任何 codebook revision 都使 count-space model失效；生成后 decoder重新分配空间语义，因此不能要求 token级位置 provenance。
- **Implementation / evaluation contract:** ImageNet 256² / 50K validation，tokenizer AdamW lr1e-4、wd1e-4、batch256、1M steps（文中同时称约200 epochs），warmup+cosine、clip1、EMA .999，后500K仅训练 decoder并加 discriminator；DiT-like generator constant lr1e-4、batch256、200 epochs、EMA .9999，25 sampling steps+CFG。128-token/4096-code TokenSet rFID2.74、FSDD gFID5.56；AR fixed orders 6.55/6.62，AR-random8.99，SetAR6.92，ordinary discrete diffusion6.23，continuous diffusion75.45。token/codebook sweep显示容量非单调：4096 gFID5.56，8192退化8.76；128 tokens最好，256/512退化7.07/9.37。hardware、precision、latency与throughput未披露。
- **Evidence boundary / trade-off:** 证明“representation invariant必须进入 generative transition”——仅随机排序或普通 diffusion不足，fixed-sum discrete invariant显著改善作者 ImageNet contract；不证明 spatial grounding、多模态 alignment或高分辨率泛化。count vector长度等于 codebook C，稀疏高维计算与 greedy adjustment带来额外开销；位置 provenance丢失、decoder重建歧义和单数据集限制外推。
- **Coexistence / evolution:** grid token在局部编辑、spatial correspondence、streaming patch decode中仍更适合；set token在 global semantic allocation与扰动鲁棒性优先时形成 alternative branch。演进是 `fixed-position sequence → permutation-invariant multiset → lossless count dual → invariant-preserving discrete diffusion`。Owner `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS`；disposition `Integrate — New Mechanism` candidate。

#### 4DGS-1K: 1000+ FPS 4D Gaussian Splatting — 2503.16422 v1，03-20

- **Score:** 4/5/5/5/4/3 = **26**。
- **Original problem / old design:** vanilla 4DGS让大量 transient Gaussian表示动态边缘，并在每帧 rasterization处理所有 Gaussian；统一 representation简单、质量高，但 storage与inactive work随时间增长。只做静态 spatial pruning会误删生命周期短但关键的 motion state。
- **Changed constraint / mechanism:** spatial-temporal variation score把每个 Gaussian的 alpha ray contribution与 temporal opacity二阶变化/lifespan结合，优先删 spatial contribution低且 temporal lifespan短的元素。Temporal filter利用相邻帧 active Gaussian集合高 overlap，在 sparse keyframes重算 active mask，中间帧复用/filter；fine-tuning补偿长 keyframe interval漏掉的信息。post-processing再量化 spherical harmonics并bit-pack filter mask。
- **State ownership / control flow:** base 4DGS持有 Gaussian identity与temporal opacity；pruner产生 compact canonical set；keyframe mask是随 scene/time变化的 execution state，rasterizer只读取 active subset。pruning ratio、keyframe interval、environment-map开关和 mask/codebook version必须绑定 scene artifact，不能作为通用 runtime常数。
- **Implementation / evaluation contract:** N3V six real scenes（2704×2028，half-resolution 300 frames）与 D-NeRF eight synthetic videos；single RTX3090。先按4DGS训练，再按 N3V80%/D-NeRF85% pruning，disable clone/split并 fine-tune 5K iterations；N3V interval20，D-NeRF 6 keyframes。N3V 4DGS 31.91dB/2085MB/90 FPS/118 raster FPS，ours31.88/418MB/805/1092，PP50MB；D-NeRF ours 1462 FPS/2482 raster FPS/42MB，PP7MB。N3V fine-tune约30min/10.54GB，render1.62GB，mask+codebook约1MB/scene；TITAN X仍200+ FPS vs vanilla20。
- **Evidence boundary / trade-off:** 证明 workload-specific temporal redundancy可通过 typed pruning+active-set reuse显著减少 raster work/storage；headline“1000+ FPS”只适用于 D-NeRF/RTX3090 raster contract，完整 FPS与 raster FPS须分开，且 N3V完整 FPS805。不同 baseline 的 environment map不完全一致；固定 pruning ratio/interval scene-sensitive，过高 pruning或过长 interval会骤降质量，preparation stage成为新瓶颈。
- **Coexistence / evolution:** vanilla 4DGS在离线质量、未知scene dynamics与无需压缩时更稳；低 pruning/短 interval在高动态scene更安全。演进是 `dense temporal representation → contribution/lifespan-aware pruning → keyframe active-set reuse → post-training artifact compaction`。Canonical owner修正为 `INFER-EXECUTION`（generic workload execution-plan owner），handoff `INFER-MEMORY-MANAGEMENT` / `MULTIMODAL-WORLD-MODELS`；disposition `Emerging / Experimental`。

#### M3: 3D-Spatial Multimodal Memory — 2503.16413 v1，03-20

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** feature splatting把每个 foundation-model 1024-D 级 feature压到每个 Gaussian 的16–64维，storage/rendering简单且天然3D一致，却损失原 feature manifold；强行把本来 view-dependent 的2D embedding做3D consistency还会产生misalignment。逐帧保留原feature fidelity高，但视频冗余、无显式空间query。
- **Changed constraint / mechanism:** M3把 scene structure与knowledge分权：3DGS Gaussian只新增低维 principal query，原始高维feature经cosine-similarity greedy reduction成为 Principal Scene Components memory bank；rasterized query通过 Gaussian Memory Attention读取 PSC，重建 CLIP/SigLIP/DINOv2/SEEM/LLaMA3/LLaMAv 对应feature space。point-based loss每视图采2,000 points，避免全patch distillation memory。
- **State ownership / control flow:** Gaussian geometry持有空间coordinate与visibility，PSC持有高维knowledge payload，per-model query/projection持有索引；rendered feature只是一时view，需连回各foundation-model decoder/head。scene、foundation-model version、PSC threshold、query dimension与COLMAP pose共同构成memory identity；任一encoder revision都要求重建bank/projection。
- **Implementation / evaluation contract:** Garden/Train/PlayRoom/DrJohnson及自建M3-Robot（Unitree B1+Z1+RealSense405D、DJI Mini4-Pro），COLMAP pose；六种foundation models。与F-Splat/F-3DGS统一约30K scene-specific iterations、同reference features，每scene从头训练memory/decoder；M3 35M vs baselines61M。feature cosine/L2、PSNR/SSIM/LPIPS及grounding/retrieval mIoU/cIoU/AP/IR@1/TR@1；grounding labels由Semantic-SAM+GPT-4o生成。query degree16为报告点，7K iterations约1/4 budget已可用。机器人仅展示先tele-op scan、已知LiDAR pose、CLIP text query定位再grasp，未给成功率/latency/safety envelope；GPU、precision、bank storage与query P99未披露。
- **Evidence boundary / trade-off:** 证明把“高维payload”与“低维空间index”分离能比直接feature distillation更好保存若干foundation-model空间并支持scene query；不证明开放世界长期memory、动态scene update或foundation knowledge本身正确。PSC是启发式近重复删除，可能消除稀有细节；scene-specific训练、pose calibration、foundation-version coupling与attention lookup是新成本。表格中并非所有low-level metric都全面优于F-3DGS，不能写成普适dominance。
- **Coexistence / evolution:** scene graph在对象关系/可编辑schema优先时更可审计，direct feature splat在模型少、memory受限时更简单，frame retrieval在无需metric geometry时更便宜。演进是 `frame archive → low-dimensional feature splat → high-dimensional bank + spatial query → multimodal scene memory`。Owner `AGENT-MEMORY`，handoff `MULTIMODAL-WORLD-MODELS` / `MULTIMODAL-EMBODIED-VLA` / `AGENT-RAG`；disposition `Integrate — New Mechanism` candidate。

#### CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners — 2503.16356 v1，03-20

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** ROME/MEMIT等把新fact写入某些MLP层，在direct recall上有效；RAG/MeLLo将事实保留外部，provenance与rollback更好。但parametric edit可能只更新surface association，无法让bridge entity跨层路由到后续relation；外部prompt也可能不遵守分解协议。单hop成功不等于多hop可用。
- **Changed constraint / mechanism:** patch/circuit analysis把two-hop分成 early layer提取first-hop bridge、middle layer把bridge+second relation路由到last token、late layer完成target。CaKE不直接解weight delta，而由GLM-4-plus按knowledge type生成两类circuit-aware训练题：late-layer knowledge integration与reasoning-circuit enhancement；然后对所有layer FFN加LoRA，用cross-entropy同时训练updated fact被召回和继续推理。
- **State ownership / control flow:** edit fact与template provenance持有desired revision；generator持有synthetic circuit tasks；LoRA adapter持有parametric delta，base保持原knowledge。runtime没有显式router区分旧/新fact，冲突与supersession依赖adapter/version管理；patch analysis是diagnostic evidence，不是生产时可观测circuit guarantee。
- **Implementation / evaluation contract:** HoppingTooLate 82,021 two-hop queries用于mechanism analysis；editing用MQuAKE-CF-3k/CF-3k-v2/T（2–4 hops），LLaMA3-8B/70B-Instruct、Qwen2.5-7B。比较IFMET/AlphaEdit/ROME/MEMIT/WISE/MeLLo/LoRA；MAcc/H-Acc与CSQA/BBH/MMLU/GSM8K locality。LLaMA3-8B CaKE MQuAKE 三集57.3/57.2/81.5，而既有KE平均MAcc<20；general benchmarks大体保留，但LLaMA3 CSQA/BBH/MMLU从76.09/67.89/63.83到75.10/67.20/62.98。FFN LoRA rank8/alpha32、batch4、lr1e-4、epochs40/50/60；hardware、precision、edit count latency未披露，70B因compute只跑LoRA/MeLLo等有限baselines。
- **Evidence boundary / trade-off:** 证明“edit success contract必须包含下游composition”且typed reasoning data优于只喂raw fact；不证明作者定位到唯一真实circuit，也不证明大量连续edit稳定。GLM-generated templates与MQuAKE schema接近，可能学习template而非general circuit；all-layer adapter比localized edit增加参数影响面，locality小幅下降，conflict/delete/rollback仍需系统管理。
- **Coexistence / evolution:** RAG适合频繁更新、可引用与可删除事实；localized edit适合窄fact、direct recall；CaKE branch适合必须parametric且要multi-hop propagation的受控schema。演进是 `single-hop edit → circuit failure diagnosis → compositional edit data → all-layer adapter → versioned edit governance`。Canonical owner修正为 `TRAIN-LORA`，handoff `WORLDVIEW-REPRESENTATION` / `AGENT-RAG` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### Sonata: Self-Supervised Learning of Reliable Point Representations — 2503.16429 v1，03-20

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** point-cloud SSL通过两种augmentation对齐邻近point feature，能利用无标签数据；但mask后仍保留精确coordinate，模型可走geometric shortcut，用局部位置而非语义恢复目标。U-Net decoder提供multi-scale context，却也把浅层几何捷径送回高分辨率。
- **Changed constraint / mechanism:** student-teacher self-distillation去掉decoder，在coarser scales附SSL loss；对masked point额外Gaussian jitter（σ=.01 vs普通.005）破坏coordinate clue，再用parameter-free feature up-casting有限恢复multi-scale context（两次最佳）。训练前5%把mask size 10→40cm、ratio30→70%，teacher temperature/weight decay也progressive，使任务难度在模型形成语义表征后再提高。BN→LN牺牲初始精度换跨dataset normalization independence。
- **State ownership / control flow:** teacher EMA持有稳定target，student接收global/local/masked views；pooling index保留up-cast mapping，mask/jitter scheduler控制shortcut exposure。indoor/outdoor仍分开pretrain，domain identity没有被单一checkpoint统一；coordinate不是被删除，而是受控降可信度。
- **Implementation / evaluation contract:** 17,948 real +121,821 simulated =139,768 scene point clouds（PointContrast 86.7×），PTv3 108M（depth[3,3,3,12,3]、width[48,96,192,384,512]）。200 epochs、AdamW、batch96/32 GPUs、lr warmup10 epochs到.004后cosine、layer decay.9，weight decay .04→.2，EMA momentum .994→1；2 global（40–100% points）、4 local（5–40%）、2 masked views。ScanNet linear probe72.52 mIoU、Sonata+DINOv2 75.91；linear head<.2M/<.2%、decoder16.3M/13%。完整fine-tune覆盖indoor instance与nuScenes/Waymo/SemKITTI；hardware型号、precision、wall-clock未披露。
- **Evidence boundary / trade-off:** progressive ablation支持“shortcut removal→limited multiscale restore→curriculum→scale”链条，且linear probe显著改善；不证明语义来自真实causal structure或统一indoors/outdoors。ScanNet200/ScanNet++多类区分仍弱；synthetic占87%、dataset imbalance、32-GPU cost、LN初始退化与jitter可能损伤fine geometry都是边界。zero-shot PCA visualization不能当task correctness。
- **Coexistence / evolution:** supervised point pretraining在高质量label充足、domain固定时仍直接；几何feature在registration/metric reconstruction中本来就是目标，不应一概视为shortcut。演进是 `coordinate-aligned SSL → geometric shortcut diagnosis → controlled clue corruption → multi-scale recovery → curriculum/data scaling`。Owner `MULTIMODAL-REPRESENTATION`，handoff `TRAIN-PRETRAINING` / `MULTIMODAL-EMBODIED-VLA`；disposition `Integrate — New Mechanism` candidate。

#### URAE: Ultra-Resolution Adaptation with Ease — 2503.16322 v1，03-20

- **Score:** 4/4/5/5/5/4 = **27**。
- **Original problem / old design:** full high-resolution retraining成本高；普通LoRA优先更新weight的major singular components，在style/identity adaptation中有效。但从1K到2K/4K主要需学local texture/detail arrangement，信号可能位于small singular components；noisy real 4K data与guidance-distilled FLUX的train/inference CFG mismatch又会使少量data适配失败。
- **Changed constraint / mechanism:** URAE给出条件分支而非单一算法。2K有高质量teacher时用FLUX1.1 Pro Ultra合成3K varied-aspect samples，LoRA major components；4K无可靠synthetic teacher时用30K LAION≥4K real images，并对每个weight做SVD，只训练smallest-rank component `W_small`而冻结residual。guidance-distilled FLUX adaptation固定g=1，避免把已蒸馏的guided target再次以g>1训练；inference仍可使用g>1。
- **State ownership / control flow:** base model/positional scaling持有native resolution prior；dataset provenance决定synthetic-teacher bias或real-noise；adapter类型取决于detail signal所在subspace；training guidance scale与inference guidance是两个不同contract。SVD component identity随base checkpoint变化，不能跨revision复用。
- **Implementation / evaluation contract:** FLUX.1-dev；2K 3K synthetic、2K iterations、batch8、2×H100约1天；4K 30K LAION、2K iterations、8×H100约1天。比较PixArt-Sigma-XL/Sana/FLUX、Real-ESRGAN/SinSR及SDEdit/I-Max。2K HPD/DPG用FID/LPIPS/MAN-IQA/QualiCLIP/HPS/PickScore/DPG Bench，300 COCO prompts由GPT-4o评估；URAE FLUX DPG80.15→83.83。4K user study1,020 votes，minor adapter overall/prompt/aesthetic约53.24/54.12/52.94%；ablation中任何training CFG都大幅恶化（例如 synthetic-major FID29.44→76.07）。precision、rank r、optimizer/lr、inference latency/VRAM未在主设置完整披露。
- **Evidence boundary / trade-off:** 证明data source、weight subspace与guidance contract需联合选择，且作者FLUX/2K-4K setting有强ablation；不证明synthetic普遍优于real，也不证明minor singular components对所有domain/model最佳。closed teacher使2K comparison不独立，GPT-4o/preference metrics偏美学，4K缺公认benchmark；SVD cost、adapter merge/rollback与real-data licensing是新问题。
- **Coexistence / evolution:** ordinary LoRA在semantic/style shift、teacher可靠或major components承载目标时仍合理；full finetune在数据/compute充足时更自由。演进是 `full high-res retrain → generic LoRA → data-quality-conditioned branch → subspace-specific adaptation → train/inference guidance separation`。Owner `TRAIN-LORA`，handoff `TRAIN-DATA` / `MULTIMODAL-GENERATIVE-PARADIGMS`；disposition `Emerging / Experimental`。

#### CLS-RL: Image Classification with Rule-Based Reinforcement Learning — 2503.16188 v1，03-20

- **Score:** 4/5/5/5/5/4 = **28**。
- **Original problem / old design:** closed-form few-shot image classification 给出候选 class names，token-level SFT 直接、可复现，在标注覆盖稳定时合理；但少样本下容易把训练类记成局部映射，ImageNet/SUN397 等数据上甚至低于 zero-shot，暴露 catastrophic forgetting 与 base/new generalization 冲突。
- **Changed constraint / mechanism:** CLS-RL 用 GRPO 对同一问题采样 response group，以 frozen reference 的 KL、clipped policy ratio、format reward 与 exact class-name accuracy reward替代逐token teacher forcing。No-Thinking 分支移除 `<think>` 形式约束，直接以标签相等作为 reward；结果表明“让分类先生成长推理”不是普适前提，而是可选 control branch。
- **State ownership / control flow:** prompt 持有 candidate label set；policy group产生候选输出；rule verifier只拥有 final label/format truth；reference model和old policy约束更新幅度。reward 不验证 reasoning trace 的 faithful，也不保证候选label taxonomy与视觉证据一致，因此可验证状态仅是封闭答案，不是开放世界事实。
- **Implementation / evaluation contract:** Qwen2-VL-2B-Instruct 全参数微调，11 datasets（ImageNet、Caltech101、OxfordPets、StanfordCars、Flowers102、Food101、FGVCAircraft、SUN397、DTD、EuroSAT、UCF101），base-to-new 为4-shot；label list随机保留约40% labels，base-to-new约80%。8×A100，per-device batch1、gradient accumulation2，输入328×328；optimizer/lr、precision、wall-clock、rollout group size在主设置未充分披露。
- **Baselines / ablations / sensitivity:** 对比 zero-shot Qwen2VL、SFT、CLS-RL、No-Thinking。11数据平均H为64.12/69.03/80.15/82.64；open-set few-shot五数据平均52.63/73.0/74.40。但分支不是单调优胜：EuroSAT SFT H84.16高于No-Thinking70.07，Flowers SFT96.34高于82.29，FGVCAircraft CLS-RL63.69又略高于No-Thinking62.79。cross-dataset“free lunch”矩阵存在负迁移，不能写成普遍提升。
- **Evidence boundary / trade-off:** 证明在作者封闭标签、少样本、单一2B MLLM合同下，verifiable outcome RL可改善平均generalization，并且直接答案分支常优于显式thinking；不证明RL学到因果视觉概念、跨模型/开放类泛化，或training cost优于SFT。exact-match reward会奖励标签捷径，label-list采样、dataset ontology与平均数会掩盖domain-specific regression。
- **Coexistence / evolution:** SFT在label语义明确、充足数据及EuroSAT/Flowers这类受益域仍可能更好；显式thinking在需要可审计中间推导时仍有价值。演进是 `few-shot SFT → forgetting diagnosis → final-answer verifier → group-relative policy update → thinking/no-thinking conditional branch`。Owner `TRAIN-GRPO`，handoff `MULTIMODAL-REPRESENTATION` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### MusicInfuser: Making Video Diffusion Listen and Dance — 2503.14505 v1，03-18

- **Score:** 4/4/4/5/5/4 = **26**。
- **Original problem / old design:** pretrained text-to-video diffusion 已学到人体、舞蹈与场景先验，直接全量重训 joint audio-video model会丢掉这些知识并提高数据/compute成本；简单把audio feature加到frame feature虽便宜，却无法选择何时、在哪些层改变motion而保持visual manifold。
- **Changed constraint / mechanism:** 冻结/复用Mochi主干，通过zero-initialized audio cross-attention（ZICA）把Wav2Vec2 audio作为K/V写入video query，初始输出严格等于原video feature，随后渐进学习音乐条件；HR-LoRA只扩展对motion更敏感层的rank，Beta-Uniform scheduler从β=3指数衰减至1，协调早期structure与后期detail。设计把“新增modality”变成可回退residual，而非重写base model。
- **State ownership / control flow:** text prompt保留style/scene owner，audio encoder写时序conditioning，video diffusion latent持有appearance/motion，zero-init output projection控制audio influence从0开始；layer-selection与beta schedule是训练policy state。音乐节拍同步并不等于动作语义正确，seed变化产生不同choreography也不能单独证明未记忆。
- **Implementation / evaluation contract:** AIST 13,940 videos/60 music/10 genres/35 dancers，提取2,378 clips并按music track无重叠划分；另加15,799 YouTube dance clips，1:1混合，约2.5s片段。Mochi base、Wav2Vec2、HR-LoRA rank64；单A100、4,000 steps、lr1e-4、约20h；inference CFG6。precision、batch、resolution、concurrency、latency/SLO未完整披露。
- **Baselines / ablations / sensitivity:** 对比MM-Diffusion与Mochi；VideoLLaMA2 judge评dance/video/prompt metrics。video-quality average为MM-Diffusion7.94、Mochi8.78、MusicInfuser8.95；prompt alignment 8.86→8.96。layer adaptability贡献最大，HR-LoRA主要改善movement realism，Beta schedule改善body representation；naive feature addition多数指标更差。AIST GT仍在若干指标上界更高，且这些分数由同一Video-LLM evaluator产生。
- **Evidence boundary / trade-off:** 证明zero-init cross-modal residual + selected-layer adaptation在作者短舞蹈视频合同中能保留文本控制并加入music responsiveness；不证明真实beat alignment、长视频一致性、跨舞种泛化或production latency。YouTube provenance、evaluator bias、单模型/短clip、base model的人脸手指与快速运动失败、silhouette body merge限制外推。
- **Coexistence / evolution:** naive addition在低成本、弱conditioning时仍简单；joint audio-video model在大规模paired data和双向生成需求下可能更合适。演进是 `text-video prior → naive audio fusion → zero-init cross-attention → layer-selective LoRA → schedule-aware multimodal adaptation`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-LORA`；disposition `Emerging / Experimental`。

#### MagicMotion: Controllable Video Generation with Dense-to-Sparse Trajectory Guidance — 2503.16421 v1，03-20

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** dense segmentation mask trajectory提供精确shape和motion supervision，但标注昂贵；point/box control容易取得，却丢掉object boundary并在多目标场景产生identity drift。直接从sparse condition训练虽简单，却要求模型同时学object identity、shape和motion，收敛及控制精度较差。
- **Changed constraint / mechanism:** 在CogVideoX-5B image-to-video上增加Trajectory ControlNet：trajectory与first frame经同一3D VAE编码，control branch通过zero-initialized convolution residual注入video branch；多层DiT feature concat给segment head预测latent masks。训练严格按mask→box→少于10帧有box的sparse-box三阶段递进，first frame始终用segmentation mask绑定object identity，latent segment loss在稀疏阶段保留fine shape。
- **State ownership / control flow:** first-frame mask建立controlled-object identity；trajectory condition随阶段降密度；ControlNet持有motion constraint，video DiT持有appearance/generation，segment head恢复shape evidence。progressive checkpoint是下一阶段初始化，不可把stage3结果归因于单一sparse signal；SAM2只在评估侧传播first-frame ground-truth mask，不是生成时oracle。
- **Implementation / evaluation contract:** MagicData 51K text/video/trajectory triplets，平均346 frames、约999×1503；motion filtering用UniMatch optical-flow score。CogVideoX-5B生成49 frames/480×720；三阶段各1 epoch，4×A100-80G，AdamW lr1e-5，batch1/GPU；inference 50 steps、CFG6、ControlNet weight1。MagicBench按foreground object count分六类，并与DAVIS共同评估。
- **Baselines / ablations / sensitivity:** 比较Motion-I2V、ImageConductor、DragAnything、LeViTor、DragNUWA、SG-I2V、Tora。MagicBench stage1 FID/FVD/M-IoU/B-IoU为87.13/112.69/91.57/87.75，stage2为93.27/107.21/76.61/81.45；方法在两benchmark表中优于所列baseline，但不同方法支持frame数不同，作者对49帧uniform sample到各自N。去掉latent segment loss显著降低shape/trajectory precision；从dense stage继承优于scratch sparse训练。
- **Evidence boundary / trade-off:** 证明dense-to-sparse curriculum、identity anchor和auxiliary segmentation在作者trajectory-I2V合同中改善控制；不证明开放场景因果动作、长视频identity、真实交互或实时性。SAM2-based IoU、derived MagicData、不同baseline frame length、50-step sampling和无独立limitations节限制结论；extra ControlNet/segment head增加显存、训练阶段与checkpoint dependency。
- **Coexistence / evolution:** dense masks在高精控制、标注可得时仍最佳；points/boxes在交互编辑和低标注成本场景更实用。演进是 `dense trajectory supervision → identity-anchored ControlNet → progressive condition sparsification → latent shape reconstruction → multi-object benchmark`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-DATA`；disposition `Integrate — New Mechanism` candidate。

#### BigO(Bench): Controlled Time and Space Complexity Code Generation — 2503.15242 v1，03-19

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** pass/fail coding benchmarks验证functional correctness，却把algorithmic complexity当隐式副产物；固定unit tests无法回答模型是否理解指定time/space class，也无法区分“偶然生成常见optimal solution”与“能按要求生成次优/不同复杂度分支”。人工静态标注准确但无法扩展到百万solutions和dynamic language行为。
- **Changed constraint / mechanism:** BigO framework从problem-specific dataclass解析输入，独立/联动放大变量，在sandbox运行Python solution并测runtime/memory，再以多种curve-fitting、aggregation和ensemble拟合worst-case empirical class；优化目标同时包含accuracy、coverage和cross-run/cross-machine self-consistency。该工具给Code Contests正确solutions生成synthetic time/space labels，并形成prediction、constrained generation与coefficient percentile三类任务。
- **State ownership / control flow:** dataclass持有input schema；expansion policy持有scaling direction与worst-case search；sandbox持有execution evidence；curve fitter把noisy measurements转为complexity label；benchmark ledger保留problem/solution/target class。label是measurement-derived evidence，不等价于formal asymptotic proof；compiler/runtime/environment是evaluation identity的一部分。
- **Implementation / evaluation contract:** 从8,139 problems、1,485,888 correct Python solutions出发，过滤无working dataclass、少于50 solutions及异常types，得到3,105 problems、1,190,250 annotated solutions。测试涵盖Llama3.1/3.3、Codestral、GPT-4o、o1-mini、Qwen2.5-Coder、DeepSeekCoder/V3/R1等；多数context 32K，CodeLlama70B为16K。Pass@k按problem-class独立，Best@1只看optimal class，All@1要求同题所有classes同时正确。
- **Baselines / ablations / sensitivity:** time complexity generation中GPT-4o Pass@1/10为20.6/44.7、Best@1 30.2、All@1 4.3；o1-mini为19.8/65.2/27.6/4.5，说明采样可增加命中却无法闭合class coverage。模型在non-optimal class反而更差，支持“常见optimal snippet记忆”诊断。fine-tuning用2,000 problems/20K solutions、每problem-class 10 human examples、约18–22M tokens、10 epochs；但生成与标签共享dynamic framework，仍可能共同偏差。
- **Evidence boundary / trade-off:** 证明executable measurement contract能显式评估complexity-conditioned generation，并揭示普通functional benchmark看不到的failure；不证明拟合标签等于数学worst case。输入扩张可能漏edge-case、CPU timing noisy、statistical memory受runtime影响，Python-only/contest distribution、模型/API版本与未完整披露硬件/temperature限制外推；sandbox成本与多次测量显著高于unit tests。
- **Coexistence / evolution:** formal proof/static analysis在安全关键、upper-bound guarantee和可解析代码上仍是gold contract；unit tests在只关心功能时更便宜。演进是 `functional tests → profiled executions → input-scale expansion → fitted complexity label → multi-class executable evaluation`。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW` / `PLATFORM-OBSERVABILITY`；disposition `Integrate — New Mechanism` candidate。

#### Temporal Consistency for LLM Reasoning Process Error Identification — 2503.14495 v1，03-18

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** learned Process Reward Model能逐步定位数学推理错误，但需大量step annotation且OOD generalization弱；training-free majority vote把独立样本聚合，适合错误近独立的情形，debate则允许相互修正。可是在first-error localization中，少数正确判断会被多数覆盖，冗长错误解释又可能在debate中压过简短正确理由。
- **Changed constraint / mechanism:** K个verifier彼此隔离，各自在后续round看到自己的上一轮`(loc,res)`并反思；每轮聚合majority location与支持比例。只有连续q轮majority不变且支持比例不下降才early stop，否则到T轮返回final majority。控制权从一次性vote转为temporal stability gate，而不是让agents互读内容。
- **State ownership / control flow:** 每个verifier私有history持有自我修订轨迹，aggregator只持有location vote与support fraction，stopping controller持有q/T budget；solution ground truth只在benchmark拥有。稳定consensus只是代理置信度，不等于correctness，相关模型/同prompt可以稳定地共同犯错。
- **Implementation / evaluation contract:** ProcessBench 3,400 problems（GSM8K400、MATH1K、Olympiad1K、Omni-MATH1K），MathCheck 516并与correct GSM8K平衡，PRM800K随机300；F1为correct/incorrect sample accuracy harmonic mean。majority/debate/temporal均用5 agents；debate 2 rounds，temporal q=3、T=10。hardware、decoding temperature、concurrency与wall-clock未充分披露；cost仅按OpenRouter public price估算。
- **Baselines / ablations / sensitivity:** GPT-4o greedy/majority/debate/temporal在ProcessBench为62.5/65.9/66.8/69.1；R1-Distill-Llama-8B为29.3/48.9/57.6/67.2。q从0到3，后者F1 48.9→67.2；仅multi-agent self-checking、仅iterative generation分别从29.3提高24.2/25.8 points，组合67.2。不同模型增益跨度极大，不能外推“7B总胜70B”。
- **Evidence boundary / trade-off:** 证明isolated temporal refinement和stability-based early stop在数学first-error benchmark可改善F1；不证明生成的解释faithful、非数学任务有效或稳定即calibrated confidence。最多50次verification/题的成本、shared-model correlated errors、prompt sensitivity及同数据上调q/T是新failure modes；作者明确承认多轮compute与数学域边界。
- **Coexistence / evolution:** 单次verifier在低延迟/高能力模型仍合理；majority在独立采样且固定budget时简单；debate在可交换互补证据时有优势。演进是 `single process judge → parallel vote/debate → isolated self-revision → temporal consistency gate → budgeted verifier policy`。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-MULTI-AGENT` / `MODEL-SAMPLING`；disposition `Integrate — New Mechanism` candidate。

#### FreeGrasp: Free-form Language-based Robotic Reasoning and Grasping — 2503.13082 v1，03-17

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** geometric grasp pipeline在目标ID已知、场景稳定时可靠；直接让VLM选最终target可利用开放词汇，但clutter/occlusion下目标不可抓，必须先移除obstacle。end-to-end policy可学习这一顺序，却需大量trajectory且难把language、occlusion、segmentation、pose与motion failure分开。
- **Changed constraint / mechanism:** top-down RGB经Molmo open-vocabulary localization生成mark-based prompt，GPT-4o根据free-form instruction与spatial/occlusion relation选择“下一件可抓object”并返回ID/class/是否target；LangSAM重新segment，GraspNet估pose，MoveIt/ROS执行。每次抓取后重采RGB-D并循环，形成可观测的replan闭环而非一次性plan。
- **State ownership / control flow:** instruction持有semantic target；detector持有每帧object IDs，VLM持有temporary occlusion-order decision，segmenter/pose planner/robot分别持有mask、grasp pose与execution state。object removal会使“某物右侧”等instruction失效，但系统未维护可更新referent/provenance，所以环境状态变化没有回写language constraint。
- **Implementation / evaluation contract:** FreeGraspData从MetaGraspNetV2选择≥4 objects场景，利用occlusion graph构造GT grasp sequence、六级difficulty和human free-form instructions；900 scenarios，每object 3 instructions。静态侧报告RSR与IoU≥.5的SSR；real robot每difficulty10 scenarios，共60 episodes，用Segmentation/Pose/Motion分层failure。24GB RTX4500；mean pipeline 15.39s（Molmo9.12、GPT-4o5.46、LangSAM.71、GraspNet.10），VLM/pose在首步后可与manipulation并行。
- **Baselines / ablations / sensitivity:** 与同用GPT-4o的ThinkGrasp比较，并用GT-localization variant隔离detector error；FreeGrasp在多数difficulty/settings更好，但在最易无歧义场景并非总胜。最严格S/P/M下ThinkGrasp在Medium/Hard全失败，FreeGrasp仍有成功；错误segmentation若包含可抓物仍可能产生正确pose，说明module-level metrics非简单乘法。
- **Evidence boundary / trade-off:** 证明modular perception→reasoning→segmentation→pose→feedback能在该bin-picking contract处理free-form target与obstacle order；不证明开放世界VLA、动态human instruction、安全抓取或实时控制。GPT-4o visual-spatial/occlusion弱，closed API/version依赖、60 real episodes、15s级latency、static dataset和instruction invalidation限制外推。
- **Coexistence / evolution:** fixed geometry pipeline在known SKU、低歧义与严格cycle time仍更可靠；end-to-end policy在大量trajectory和高频control时可减少API latency。演进是 `target-known grasp → open-vocabulary target → obstacle-aware next-object reasoning → modular execution → observation/replan loop`。Owner `MULTIMODAL-EMBODIED-VLA`，handoff `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### NuiScene: Efficient Generation of Unbounded Outdoor Scenes — 2503.16375 v1，03-20

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** monolithic triplane/spatial grid保留明确坐标与local query，适合bounded scene；outdoor height variation迫使统一volume为最高建筑付费，高resolution triplane OOM。T2I+depth逐帧outpaint虽open-domain，却会累计depth error、seam与global inconsistency。
- **Changed constraint / mechanism:** 把场景拆成50×height×50 local chunks，VAE用16-token vector set压缩任意高度occupancy；same-chunk双point-cloud embedding consistency避免KL posterior collapse，并从latent预测height以剪枝query。diffusion一次生成2×2 chunk latent，训练四种mask/neighbor configurations，推理按raster order写入persistent scene latent grid，最后逐chunkdecode/marching cubes。
- **State ownership / control flow:** scene latent grid是authoritative spatial state；mask选择当前位置可见neighbors，diffusion生成新的quad state并commit，VAE decoder只负责occupancy。raster order带来方向性和error accumulation；chunk边界、height estimate、conditioning neighborhood属于generation identity，不能把“unbounded”理解为global coherent world state。
- **Implementation / evaluation contract:** NuiScene43含43 scenes（16 rural/medieval、19 low-poly city、4 Japanese、4 other），理论sampleable quad chunks约15.2M；主single-scene用100K quad chunks（95K/5K），multi-scene仅加3 scenes、300K samples。VAE 2×L40S、batch40：vecset 36.1h/36.6GB，64² triplane 58.5h/55.7GB，128² OOM；diffusion 1×A6000、batch192：vecset 11.1h/10.4GB vs triplane27.6h/24.4GB。
- **Baselines / ablations / sensitivity:** vecset reconstruction IoU .989、CD .055、F-score .864，优于best table triplane .940/.064/.831；generated quad FPD/KPD .571/.951 vs1.406/2.589。evaluation以10K generated vs10K source chunks、2048 points和PointNet++ feature；single-scene会过拟合相似sub-scenes，multi-scene仅qualitative/limited scale，不能据dataset总规模宣称43-scene训练。
- **Evidence boundary / trade-off:** 证明vector-set local representation与explicit neighbor-conditioned outpainting改善作者scene-chunk的memory/training frontier；不证明semantic controllability、global topology、infinite-horizon consistency或physical simulation。offline chunk storage高、训练scene少、bridge seam/discontinuity、无text/attribute condition与全局context是作者明确限制；raster seriality也限制parallel generation。
- **Coexistence / evolution:** triplane在bounded scene、regular query和明确global coordinate时仍简单；T2I prior在appearance/open-domain优先时更强。演进是 `global spatial grid → height-normalized chunks → vector-set latent → neighbor-conditioned outpainting → persistent raster scene state`。Owner `MULTIMODAL-WORLD-MODELS`（仅负责persistent spatial-state branch，不把它写成action-conditioned world model），handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `INFER-EXECUTION`；disposition `Integrate — New Mechanism` candidate。

#### Zero-1-to-A: One Image to Animatable Head Avatars Using Video Diffusion — 2503.15851 v1，03-20

- **Score:** 5/4/4/5/5/4 = **27**。
- **Original problem / old design:** static image-to-3D/SDS只需单图和frozen 2D prior，适合geometry/texture；但animatable avatar还需view consistency、expression dynamics与rig。一次性用video diffusion伪数据训练4D representation会形成“坏avatar生成坏guidance、坏guidance继续破坏avatar”的closed-loop collapse。
- **Changed constraint / mechanism:** SymGEN让FLAME-rigged Gaussian avatar和portrait video diffusion互相生成/refine data；先固定expression把camera从front逐渐扩展到side，学习spatial consistency，再固定camera把expression从relaxed扩展到hyperbolic，学习temporal consistency。progressive dataset每阶段只在已有avatar可提供较稳定rendering后增加难例，打破chicken-and-egg instability。
- **State ownership / control flow:** FLAME mesh持有pose/expression schema，每triangle初始化10 Gaussians持有appearance；video diffusion持有external spatiotemporal prior，synthetic dataset是可迭代中间state，reconstruction以L1/LPIPS/position/scale loss更新avatar。teacher与student互相依赖，错误可被self-reinforce；dataset revision和avatar checkpoint必须成对管理。
- **Implementation / evaluation contract:** default使用facial-landmark-conditioned portrait video diffusion、CFG3.5；训练10K iterations，初始spatial dataset20 samples、每1K更新，5K后加入10 synthetic expression temporal samples。loss weightsL1=10、LPIPS=10、position=.1、scale=10。hardware、optimizer/lr、precision、wall-clock在主设置未完整披露；rendering speed只在same-device figure中给出，缺production concurrency/SLO。
- **Baselines / ablations / sensitivity:** 静态头像与DreamFusion、LatentNeRF、Fantasia3D、ProlificDreamer、HeadSculpt/Artist/Studio比较；三种CLIP score中Ours .285/.320/.322，并非每列都最高。无temporal learning时side-view眼口改善但夸张表情mouth artifacts，无spatial learning时expression泛化改善但eye misalignment；两stage与progressive order共同必要，不能归因video diffusion单项。
- **Evidence boundary / trade-off:** 证明progressive spatial/temporal pseudo-data refinement能在单图head-avatar合同缓解teacher inconsistency；不证明任意人体4D、真实motion causality或zero-shot deployment。FLAME-constrained Gaussians不能表示afro等mesh外结构，edge blur/label ambiguity、closed base diffusion与缺硬件细节限制外推；额外10K-step per-avatar optimization不是即时生成。
- **Coexistence / evolution:** static avatar在无animation需求时更便宜；multi-view/video capture在高fidelity与真实动态监督可得时更可靠。演进是 `static SDS → video prior distillation → symbiotic pseudo-data loop → spatial-first curriculum → temporal refinement`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-WORLD-MODELS` / `TRAIN-DATA`；disposition `Emerging / Experimental`。

#### Concat-ID: Universal Identity-Preserving Video Synthesis — 2503.14151 v1，03-18

- **Score:** 5/5/4/5/5/3 = **27**。
- **Original problem / old design:** face encoder+adapter把identity feature注入video model，可隔离modality但增加参数/训练推理路径；把reference image沿channel与first-frame latent拼接更直接，却假设spatial alignment，容易在首帧产生artifact并复制reference expression。identity fidelity与facial editability不是同一目标。
- **Changed constraint / mechanism:** 复用video VAE把任意reference image编码进与video相同latent space，沿sequence而非channel拼到video tokens尾部，完全交给现有3D self-attention交互；扩展3D-RoPE区分video/reference及多reference次序。数据侧依次使用same-video pairs、跨video same-identity pairs、high-similarity trade-off pairs，训练按pretrain→cross-video→trade-off推进。
- **State ownership / control flow:** VAE持有shared latent contract，reference sequence position持有identity/subject slot，3D attention负责融合，text prompt持有motion/expression intent。reference顺序会决定multiple identities spatial placement，因此“identity slot”并非完全permutation-invariant；ArcFace/CLIP相似阈值与base checkpoint revision是dataset/condition identity的一部分。
- **Implementation / evaluation contract:** CogVideoX-5B全参数三阶段，lr分别1e-5/5e-6/5e-6、linear decay，49 frames/480×720，text/image condition各0.1 dropout。1.3M single-identity videos×5 refs，cross-video 0.8M pairs/0.5M refs（cos .7–.9），trade-off 160K后按quality/motion取top50K（cos .9–.99）。hardware、precision、batch、steps、wall-clock未在主设置完整披露。
- **Baselines / ablations / sensitivity:** ConsisID benchmark过滤训练overlap后97 images×9 prompts=873 pairs；single ID ArcSim/CurSim/ViCLIP/CLIPDist为.442/.466/.242/.325，对ConsisID .432/.451/.237/.303。multi-ID对Ingredients identity更高但ViCLIP .190低于.199。100 video groups、3 voters、900 pairwise answers的user study支持motion/identity；data-stage ablation显示cross-video提升editability却损fidelity，trade-off回调。multi-subject/three-ID主要qualitative且后者仅40K videos。
- **Evidence boundary / trade-off:** 证明shared VAE latent+sequence concat能在该CogVideoX合同避免额外adapter并扩展多个condition；不证明“universal”、任意subject、复杂多人物interaction或production memory。每增加reference使sequence/attention cost上升，slot order泄露spatial prior；training data私有、empirical thresholds、identity detector bias和缺hardware限制外推。
- **Coexistence / evolution:** adapter在需要冻结base、独立version/rollback和bounded condition cost时仍更可控；channel concat在aligned edit/inpainting仍合理。演进是 `special face adapter → channel-aligned reference → shared-latent sequence condition → cross-video disentanglement → multi-condition slots`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-DATA`；disposition `Emerging / Experimental`。

#### DP-Recon: Decompositional Neural Scene Reconstruction with Generative Diffusion Prior — 2503.14830 v1，03-19

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** sparse-view neural reconstruction必须忠实observed pixels，object-compositional SDF又可导出独立mesh/pose/scale；但heavy occlusion的unseen geometry/texture无数据约束。直接加SDS prior能补全，却可能改坏已观测区域，generative plausibility与reconstruction truth发生owner冲突。
- **Changed constraint / mechanism:** DP-Recon先以object/background decomposition重建显式SDF/mesh，再分别对normal render做geometry SDS、对color render做appearance SDS；visibility map对每pixel动态调prior weight：low visibility放大生成先验，high visibility衰减甚至关闭，使data evidence与prior按可见性仲裁。background也作为独立object，最终导出per-object geometry与UV。
- **State ownership / control flow:** camera-calibrated input与mask持有observed truth，per-object SDF/mesh持有scene state，visibility renderer决定哪个区域可让diffusion prior写入，text prompt只是unseen completion proposal。object逐个优化而无functional-group state，可能产生局部合理但关系不一致的场景。
- **Implementation / evaluation contract:** Replica 8 synthetic scenes、ScanNet++ 6 real scenes，默认10 views；YouTube case用15 views、COLMAP pose、SAM2 masks。PyTorch/Adam lr5e-4，compositional stage 1,024 rays/iter，geometry/appearance render128²，background panorama2048×1024。single A100，80K iterations/约10.45h per scene；geometry 35K、appearance75K开始，50K约4.52h已有主要收益。
- **Baselines / ablations / sensitivity:** 与MonoSDF、RICO、ObjectSDF++等比较；无prior scene CD8.51、NC86.13、PSNR24.31、object CD7.67/mIoU73.31，逐步加入geometry/appearance prior与visibility后全模型最好。visibility threshold geometry .5、appearance .3且piecewise weights手工设定。prior提升unseen completion，但错误prompt会生成不协调table/color。
- **Evidence boundary / trade-off:** 证明visibility可作为evidence/prior arbitration signal，在作者14-scene sparse-view合同改善geometry/appearance；不证明生成补全是真实hidden structure。GT/derived masks与camera pose依赖、text-prompt sensitivity、single-scene optimization cost、hair/grass/sky/fur loose geometry failure和independent-object relation缺失限制部署。
- **Coexistence / evolution:** pure reconstruction在测量可信、不可接受hallucinated geometry时仍应优先；image-to-3D在位置/scale无要求时更简单。演进是 `monolithic sparse reconstruction → object decomposition → diffusion completion → visibility-gated prior → editable per-object assets`。Owner `MULTIMODAL-WORLD-MODELS`（scene-state reconstruction branch），handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Integrate — New Mechanism` candidate。

#### PORTAL: Agents Play Thousands of 3D Video Games — 2503.13356 v1，03-17

- **Score:** 4/4/4/3/5/3 = **23**。
- **Original problem / old design:** online LLM每frame reasoning能快速适配game，却无法满足real-time latency；end-to-end RL/neural policy执行快，但训练/模拟昂贵且跨game迁移差。传统hand-authored behavior tree可解释、低延迟，却把每款game的规则工程成本留给developer。
- **Changed constraint / mechanism:** PORTAL把高层policy表示为`(Π,Θ,Φ)`：DAG/behavior tree控制流、neural task nodes和rule-based condition/task nodes；Qwen2.5-Coder-32B离线把自然语言目标编译成DSL，再转JSON给server实时执行。runtime不调用LLM；episode metrics与由environment state合成的bird-eye minimap/replay交给VLM做strategy reflection，再离线生成新tree。
- **State ownership / control flow:** DSL/JSON policy是versioned executable artifact，game server持有authoritative environment state，neural/rule nodes执行局部observation→action，高层LLM只在offline compile/revision阶段拥有proposal权。compiler/type/schema/verifier contract未严格定义，错误policy可能以低延迟持续执行；VLM replay评价不是environment success truth。
- **Implementation / evaluation contract:** 文中称platform有thousands of player-created FPS games、LLM为Qwen2.5-Coder-32B；实证正文只展示basic/team policy在9个games的截图/视频和qualitative coordination/reflection，没有统一task success、episode count、baseline、hardware、frame rate、P99、cost或statistical test。作者也未给独立ablation/limitations section。
- **Evidence boundary / trade-off:** 论文提供重要的offline plan compilation→online bounded executor设计样例，但不足以证明“thousands”上的quantitative generalization、minutes级开发SLO或优于RL。环境/engine/tool nodes可能共享game family，9-demo不能排除manual tuning；project artifact可供inspect但没有executable benchmark contract。因此score保守为23，不能把marketing-scale claim写成核心事实。
- **Coexistence / evolution:** authored behavior tree在policy需certify、game rules稳定时更安全；online LLM在turn-based/低频探索任务仍灵活；RL在dense simulator和连续control更合适。演进是 `online language action → offline DSL policy synthesis → hybrid behavior tree executor → replay-based revision`。Owner `AGENT-WORKFLOW`，handoff `AGENT-TOOL-CALLING` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Emerging / Experimental`，非核心integration evidence。

#### Coarse-to-Fine Token Prediction for Autoregressive Image Generation — 2503.16194 v1，03-20

- **Score:** 5/5/5/5/5/3 = **28**。
- **Original problem / old design:** 大VQ codebook降低image quantization error，但把AR next-token softmax扩大到16K/262K classes，fine-grained visually similar labels造成optimization redundancy与重复head compute。直接缩codebook省计算却回退representation fidelity；单级AR仍需256 sequential steps。
- **Changed constraint / mechanism:** 对16,384 VQ codewords按embedding做k-means得到默认512 coarse clusters；stage1 causal AR仅预测coarse token sequence，stage2 full-attention auxiliary model在完整coarse sequence+context上一次性恢复所有fine labels。把难题分成`global sequential structure`与`within-cluster refinement`，但第二步的条件独立/full-attention prediction不是原始exact AR factorization。
- **State ownership / control flow:** frozen tokenizer/codebook持有fine identity与cluster mapping，stage1持有coarse causal history，stage2并行commit fine labels，VQ decoder重建image。cluster assignment随tokenizer revision失效；stage1错误把true fine token排除出cluster时stage2无法rollback，形成hierarchical support bottleneck。
- **Implementation / evaluation contract:** ImageNet-1K、LlamaGen VQ-VAE、16×16 downsample/16,384 codebook；stage1/stage2沿用LlamaGen，stage2改full attention。single A100、batch64；例如343M baseline 256 steps 7.50 img/s、FID3.80，CTF 310M+343M、257 steps8.71 img/s、FID2.97；111M case反而13.75→12.83，说明small model overhead可占主导。训练100 epochs FID5.43近baseline300 epochs5.46。
- **Baselines / ablations / sensitivity:** 比较GAN/diffusion/masked/VAR/LlamaGen，核心clean comparison是同backbone。clusters128/512/1024 FID11.23/5.51/5.38；stage2 size111/343/775M FID5.51/5.33/5.27，边际收益递减；CFG、temperature、top-k显著改变precision/recall。过少clusters使stage2一跳内候选太多，过多则退化回标准AR。
- **Evidence boundary / trade-off:** 证明hierarchical label factorization在作者ImageNet/tokenizer/AR合同改善训练与多数large-model采样frontier；不证明text/image/video通用、perceptual exactness、distributed serving或端到端energy。额外model/checkpoint、cluster mapping、support loss、two-stage调参和small-model slowdown是新成本；无独立limitations节。
- **Coexistence / evolution:** 单级AR在小codebook、exact likelihood与简单artifact管理时仍合理；VAR/masked/diffusion是不同factorization branch。演进是 `large flat vocabulary → semantic codeword clustering → coarse causal plan → one-step fine refinement`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `INFER-DECODING`；disposition `Integrate — New Mechanism` candidate。

#### SALT: Singular Value Adaptation with Low-Rank Transformation — 2503.16055 v1，03-20

- **Score:** 5/4/4/5/5/4 = **27**。
- **Original problem / old design:** LoRA以低秩增量适配冻结权重，参数和artifact边界清楚，但当下游变化需要重标定原权重的主奇异方向时，单一低秩旁路可能欠拟合；对全部singular values统一scale/shift又会让adaptation缺少component-specific容量。
- **Changed constraint / mechanism:** 对冻结矩阵做SVD；前`r`个主奇异值各自学习scale `α`和shift `β`，并用ReLU保持非负；剩余子空间学习低秩`XYᵀ`变换。它把“重标定已有主方向”和“在尾部子空间添加新方向”分开，而不是把所有变化压进同一LoRA rank。
- **State ownership / control flow:** base SAM/SAM2权重冻结，SALT参数与normalization/text affine参数构成版本化adapter；SVD basis与base checkpoint强绑定，base revision变化必须使adapter失效。inference仍执行合并后的线性层，但训练需持有分解basis和两类参数。
- **Implementation / evaluation contract:** 五个medical vessel segmentation datasets：DIAS 20/10、ROSE 22/8、DRIVE 14/6、ARCADE 700/300、XRay-Angio 93/41；prompt-adapted SAM，512输入、text prompts、AdamW lr1e-4、wd1e-2、batch5、200 epochs、step decay、augmentations，RTX4090 24GB。rank256 SALT 3.9%/9.4M trainable、avg Dice .74、HD95 23.87；LoRA256 14.08%/33.9M、.70/25.94；S-SAM .40%/1M、.71/30.12。rank4 SALT .46%/1.1M、avg .72。
- **Baselines / sensitivity:** rank对component的最优值不同；LoRA rank4→256由Dice .72→.76，减少MHA/MLP SALT rank反而可改善。SAM2 extension中作者报告相近质量下SALT比LoRA少2.4×（rank256）或1.8×（rank4）参数，但这是同一family内结果，不是通用PEFT定律。
- **Evidence boundary / trade-off:** 证明在这些小规模vessel datasets和SAM family中，显式主奇异值适配可用更少trainable parameters达到有竞争力的Dice/HD95；不证明跨模型、跨任务或wall-clock更快。random split、无多seed/CI、无inference overhead、domain-specific prompts与预计算SVD限制外推。
- **Coexistence / evolution:** LoRA在无需SVD、跨base portability和tooling成熟度优先时仍更合理；full fine-tuning在大分布迁移且compute/data充分时仍是上界。演进是 `low-rank additive update → singular-direction rescaling → head/tail subspace split adaptation`。Owner `TRAIN-LORA`，handoff `TRAIN-SFT`；disposition `Emerging / Experimental`。

#### Where do Large Vision-Language Models Look? — 2503.13891 v1，03-18

- **Score:** 5/4/4/5/5/4 = **27**。
- **Original problem / old design:** attention map和token-level saliency容易被当作“模型看哪里”的解释，但多encoder、多resolution LVLM中内部attention不等价于output dependence；分别优化deletion与insertion mask更完整，却增加约2倍求解成本且产生两个不一致解释。
- **Changed constraint / mechanism:** 用原图与blurred baseline下答案log-likelihood ratio筛选真正依赖视觉的output tokens；再优化一个region mask，同时满足删除该区域显著降低score、只插入该区域恢复score。通过指数衰减L2的graduated non-convexity避免mask一开始陷入局部极值。
- **State ownership / control flow:** 固定LVLM拥有answer probability，perturbation pipeline拥有blur/mask基线，optimizer拥有sample-specific attribution mask；heatmap是外部解释artifact，不是模型内部causal state。token筛选与baseline选择共同定义解释identity，改变prompt或blur operator必须重新计算。
- **Implementation / evaluation contract:** LLaVA-1.5、LLaVA-OneVision、Cambrian；MMStar 1500、CV-Bench 2638、MMVP 300。先排除原图与blurred图答案score差异不足样本，最终只保留MMVP 35%、MMStar 47%、CV-Bench 34%。single mask约7.4s/sample，separate masks约19.1s；作者表中single-mask deletion/insertion约为MMVP .366/.811、MMStar .292/.953、CV-Bench .402/.965。
- **Baselines / sensitivity:** joint-probability与keyword-token selection整体较差；L2 λ=.1较稳，λ=1/10明显退化。扩大LLM、增加encoder/resolution并不单调改善focus；正确focus也不保证空间/科学问题答对，counting仍困难。
- **Evidence boundary / trade-off:** 证明perturbation-defined visual dependence可以比raw attention提供更接近output的region attribution并降低双mask求解成本；不证明heatmap忠实复现内部reasoning，也不证明被过滤掉的多数样本。强过滤造成selection bias，blur baseline与likelihood proxy可改变结论；hardware/concurrency未披露。
- **Coexistence / evolution:** raw attention在debug model internals时仍有价值；gradient/perturbation attribution回答的是不同问题。演进是 `internal attention inspection → output-token dependence test → deletion/insertion masks → shared mask with explicit cost trade-off`。Owner `MULTIMODAL-REPRESENTATION`，handoff `PLATFORM-EVALUATION-SYSTEM`；disposition `Refine — Existing Argument`。

#### Training Video Foundation Models with NVIDIA NeMo — 2503.12964 v1，03-17

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** 把image/text训练栈直接扩展到video会同时放大解码、tokenization、长序列attention、cloud-shard重复下载与distributed collective成本；单一parallelism recipe在小模型短序列上合理，却无法同时覆盖28B模型和73K-token video workload。
- **Changed constraint / mechanism:** end-to-end stack连接NeMo Curator、multimodal loader、causal temporal 3D tokenizer、3D patchification、Megatron Core与inference；每rank读取unique shard后all-gather，避免所有rank从cloud重复下载。训练按model size/context选择TP/SP、CP ring attention、PP、FSDP，并用AdaLN-LoRA压缩巨大conditioning projection；ST-DiT的spatial/temporal/full attention shape切换使用optimized all-to-all减少重排collectives。
- **State ownership / control flow:** curator持有clip/filter lineage，shard manifest和rank assignment持有data ownership，tokenizer revision定义spatiotemporal token identity，parallel planner把sequence/model/layer/optimizer state映射到rank mesh。shape transition与all-to-all layout成为execution-plan state，不能只记录“用了CP”。
- **Implementation / evaluation contract:** 7B/28B，context 8,192或73,728；多数实验8 nodes×8 H100，28B Stage3用32×8 H100。作者报告最高48.2% MFU、8→32 nodes超过95% strong-scaling efficiency、7B相对Fast-DiT最高1.85×，而Fast-DiT 28B OOM。ST-DiT 74K context：7B CP 3371.4 token/s/GPU→all-to-all 8113.6（2.407×）；12B 2342.8→5288.5（2.257×），最高约40% MFU。
- **Baselines / sensitivity:** 小模型短context偏FSDP，长sequence优先CP，模型尺寸优先TP/FSDP，二者都大则TP+PP+CP；TP/SP放intra-node、CP/PP放inter-node。7B AdaLN projection约2.7B参数，AdaLN-LoRA作者报告最高约1.2×compute改善。该结论是workload-specific配置frontier，不是某种parallelism绝对优越。
- **Evidence boundary / trade-off:** 证明video workload需要把data decode、tokenization、attention形状和rank topology共同设计，并在作者H100集群合同下获得较高MFU/扩展效率；不证明任意cluster、network、codec或model结构。vendor author benchmark、软件commit/precision/部分batch和production SLO披露不完整，100PB+与3×curation claim不能脱离原条件外推。
- **Coexistence / evolution:** 简单FSDP在小模型和运维成本优先时仍更合适；标准ring CP在shape稳定时更易验证。演进是 `single recipe → workload-typed parallel mesh → data-ownership-aware loader → attention-shape-aware collective plan`。Owner `TRAIN-DISTRIBUTED-TRAINING`，handoff `TRAIN-DATA` / `INFER-DISTRIBUTED`；disposition `Integrate — New Mechanism` candidate。

#### GASP: Unifying Geometry, Semantics, and Motion for Self-Supervised 3D Representation Learning — 2503.15672 v1，03-19

- **Score:** 5/5/4/5/5/5 = **29**。
- **Original problem / old design:** 仅以continuous 4D occupancy训练的geometry-first encoder能预测空间占用，却缺semantic feature和可行路径；为每个downstream task单独标注/预训练能建立明确objective，但label成本高且共享state弱。静止车辆trajectory又使future-path supervision退化为单点。
- **Changed constraint / mechanism:** 将过去K=3个、间隔0.5s的lidar scans做ego-motion compensation并voxelize，经ResNet/deformable attention/FPN得到BEV latent；任意query `(x,y,z,t)`由三个decoder同时预测occupancy、DINOv2 feature与ego path。DINO feature做position denoise与PCA16；ego path被定义为与time无关的可通行region，避免stationary trajectory ambiguity。
- **State ownership / control flow:** sensor alignment拥有observation-time frame，BEV latent持有共享scene estimate，query decoder分别拥有geometry/semantic/traversability readout。ego path是observed behavior-derived affordance，不是对alternative action conditioned dynamics；因此world-state owner不能被误写成causal planner。
- **Implementation / evaluation contract:** Argoverse2，x/y ±70m、z[-2,6]、pillar .16m；100K steps，Adam cosine max4e-4，warmup2K，effective batch8。每sample约0.9M positive+0.9M negative occupancy queries、100K DINO feature queries、10K positive+10K negative ego queries，loss权重1/.5/.1。下游含semantic BEV forecasting、map segmentation、semantic 4D occupancy、ego trajectory；低标签规模n=1…1e5，n≤100用10 seeds。
- **Baselines / sensitivity:** 4D vehicle occupancy t=0…3s、0.5s间隔、80×80m/.4m。frozen GASP ego min6 ADE/FDE .617/1.06，对UnO .834/1.43；min1 1.39/2.87，对1.84/3.70。fine-tuned GASP .706/1.27，对UnO .902/1.51。逐项objective、DINO PCA8/16/32与missing-ray ablation；missing rays对aggregate metric不显著但减少qualitative halos。
- **Evidence boundary / trade-off:** 证明geometry+semantic+path多目标pretraining在该lidar/Argoverse2合同提升若干low-label downstream tasks；不证明真正action-conditioned world dynamics、closed-loop driving或跨sensor/城市泛化。实验虽称architecture sensor-agnostic但只验证lidar，且hardware/precision/wall-clock未披露。
- **Coexistence / evolution:** 纯occupancy在semantic/privacy/cost受限且任务只需几何时仍更简洁；task-specific supervised model在labels充分时更直接。演进是 `occupancy geometry → semantic feature target → behavior-derived affordance → shared queryable world state`。Owner `MULTIMODAL-WORLD-MODELS`，handoff `MULTIMODAL-REPRESENTATION` / `MULTIMODAL-EMBODIED-VLA`；disposition `Integrate — New Mechanism` candidate。

#### Make Your Training Flexible / FluxViT — 2503.14237 v1，03-18

- **Score:** 5/5/5/5/5/3 = **28**。
- **Original problem / old design:** 固定frame count、spatial resolution与完整token grid让video encoder容易训练和部署，但不同device/latency budget需要不同token数；分别训练多个模型会复制artifact和training cost，inference时临时drop tokens又因训练分布不匹配而损失质量。
- **Changed constraint / mechanism:** Flux-Pretraining从更大的flexible spatiotemporal sampling grid中选择固定预算的group-dynamic tokens，用full teacher features做masked alignment；tuning阶段延续flexi-sampling，并在train subset上按下游任务搜索token allocation。FluxViT以Global-Local Positional Embedding编码selected token的global/source位置，以Dual Patch Normalization稳定不同resolution/token distribution；同batch把2048/1024/512 token student分别forward并用teacher/self-distillation对齐。
- **State ownership / control flow:** token budget和sampling grid成为deployment input contract，selector生成request/config-specific token set，GLPE保留token provenance，shared checkpoint支持多个budget。下游heuristic search产生的allocation是task-specific deployment artifact；改变dataset/task/latency budget必须重新验证，不能把它当模型内生最优调度。
- **Implementation / evaluation contract:** K-MASH约1.1M samples，FluxViT 100 epochs、global batch2048；single-modality ablation Flux-Single-UMT用32×A100训练15.5h、per-GPU batch32/44GB，Multi 20.3h/70GB。K400、SSv2、COIN及retrieval datasets上测试多个GFLOP/token budgets；FluxViT-S在K400 154×12 GFLOPs约88.0 top-1，而13×12约84.0，展示的是budget-quality frontier而非免费等价。
- **Baselines / ablations / sensitivity:** 与InternVideo2、UMT、VideoMAE等比较；GLPE+DPN在K400/SSv2 Token Optimization上约+3.3/+3.9 points。sampling超参多数影响小但`T_thres`敏感；更复杂Vid-TLDR reduction sequence反而不稳定且需大量parameter search，作者最终保留近零成本heuristic。Multi co-training增加约31% wall-clock并显著增加memory。
- **Evidence boundary / trade-off:** 证明共享video encoder可通过多预算co-training与位置/归一化修正，在作者datasets上形成更好的compute-quality frontier；不证明任意video workload、online request-level adaptive scheduling或真实P99/energy。token allocation使用train subset搜索，有task leakage/overfitting风险；多forward teacher训练成本与私有/大规模data合同限制外推。
- **Coexistence / evolution:** 固定resolution checkpoint在单一硬件/SLO下更简单且可预测；独立specialized model在极端budget可能仍优于shared weights。演进是 `one model per grid → inference token drop → flexible sampling augmentation → multi-budget co-training → task-specific token allocation`。Owner `TRAIN-PRETRAINING`，handoff `MULTIMODAL-REPRESENTATION` / `INFER-EXECUTION`；disposition `Integrate — New Mechanism` candidate。

#### See-Saw Modality Balance / BalGrad — 2503.13834 v1，03-18

- **Score:** 5/4/4/5/5/4 = **27**。
- **Original problem / old design:** joint multimodal training假设各modality的gradient会共同降低task loss；当一侧更容易学习或有spurious correlation时，较大gradient会主导更新，弱modality被忽略。仅做loss/gradient magnitude reweighting可以拉平贡献，却可能让balance objective与task objective方向冲突，产生negative transfer。
- **Changed constraint / mechanism:** BalGrad先用两个unimodal predictions的双向KL产生balance gradient，做inter-modality gradient reweighting；再检测target-task gradient `g_T` 与KL gradient `g_kl` 的dot product。若冲突为负，将`g_T`投影到`g_kl`正交方向，否则保留原gradient，把“梯度大小平衡”和“目标方向不冲突”分成两步。
- **State ownership / control flow:** visual/text encoder分别拥有unimodal predictions，KL loss定义balance target，optimizer在每step读取多组gradient并决定projection。balance不是static per-layer learning rate，而是batch-dependent direction contract；额外forward/backward与gradient buffers成为training runtime成本。
- **Implementation / evaluation contract:** UPMC Food-101、Hateful Memes、MM-IMDb；ViT+BERT late concatenation，encoder冻结、只训练embedding/classifier linear probe。训练只看完整modality；测试missing用empty text/zero pixels，noisy用image 30% salt-and-pepper、text随机删15% tokens，并测missing ratio .2/.4/.6/.8。BalGrad在UPMC full 80.32、missing average45.26/gap39.54；Hateful Memes full67.35、average61.67/gap8.38；MM-IMDb full43.19略低于baseline44.09但gap更小。
- **Baselines / ablations / sensitivity:** 比较MSLR、OGM-GE、AGM。只reweight在Hateful Memes出现negative transfer，projection加入后缓解；无projection/有projection gradient-conflict fraction为UPMC .66→.36、Hateful .78→.32、MM-IMDb .28→.26。结果说明balance与aggregate task accuracy有时是trade-off，不是可同时单调优化。
- **Evidence boundary / trade-off:** 证明在三个late-fusion linear-probe datasets和人工missing/noise合同中，gradient magnitude+direction控制能减少modality gap；不证明full fine-tuning、LLM-scale native multimodal pretraining或现实sensor dropout。无独立limitations节，hardware/precision/batch/wall-clock未披露；zero/empty和salt-pepper不代表真实故障，gap metric也可能用降低强modality换平衡。
- **Coexistence / evolution:** 标准joint training在modalities同等可靠且无显著gradient conflict时仍更便宜；简单reweight在direction aligned时足够。演进是 `joint loss → modality-wise gradient diagnosis → magnitude reweighting → conflict-aware projection`。Owner `TRAIN-PRETRAINING`，handoff `MULTIMODAL-REPRESENTATION` / `TRAIN-DATA`；disposition `Refine — Existing Argument`。

#### Why Personalizing Deep Learning-Based Code Completion Tools Matters — 2503.14201 v1，03-18

- **Score:** 4/4/5/5/4/4 = **26**。
- **Original problem / old design:** 一个跨repository训练的generic code model能学习通用syntax/API pattern，artifact和serving成本最低；但organization/developer vocabulary、method signatures与coding conventions形成局部分布。单纯扩大generic dataset可能增加覆盖，却不保证训练样本与实际completion高度相关。
- **Changed constraint / mechanism:** 论文把personalization拆为organization-specific和developer-specific fine-tuning，并控制额外training size：同量generic `Baseline+`、organization subset与developer data比较。它不是新optimizer，而是把data ownership/specificity作为可测设计变量；较小personalized model再与10× larger generic model做cost/performance对照。
- **State ownership / control flow:** commit author disambiguation、repository snapshot与chronological completion split定义provenance；organization model是共享versioned artifact，developer model把model state按个人分叉。前者data更多、deploy/maintain一次；后者更specific但导致N-model lifecycle、privacy、freshness与delete/supersession问题。
- **Implementation / evaluation contract:** Apache 1,161 projects、Spring 68 projects，136 developers；T5 60M/750M与Code Llama 7B。generic T5 pretrain约1.14M/1.09M methods，再fine-tune约1.43M/1.36M completion instances；personalization sets约1K–908.1K。metrics是Exact Match、CrystalBLEU，McNemar/odds ratio与Wilcoxon/Cliff's delta；共训练396 models，实验在HPC cluster，但GPU型号、precision、batch/concurrency未完整披露。
- **Baselines / ablations / sensitivity:** organization-specific Code Llama在20 developers中11个EM显著提升，平均+5.84 points；developer-specific效果受data size限制并非普遍更好。同量generic data不产生相同收益，支持specificity而非纯sample count解释。organization-specific T5-small 60M与generic T5-large 750M在top-20上总体相近，但某些Apache developers差异可正可负；作者租GPU模型估算breakeven约44,948–272,824 inferences，依赖外部Copilot usage假设。
- **Evidence boundary / trade-off:** 证明在Java/Apache/Spring和离线line/block completion合同中，organization data常能提高EM/CrystalBLEU，并可改变small-vs-large成本frontier；不证明真实developer productivity、安全性、其他语言或online drift。EM不等价semantic correctness，CrystalBLEU仍是surface proxy；Code Llama可能已见target code，身份消歧和public OSS行为不代表企业private repo。
- **Coexistence / evolution:** generic model在小组织、data governance成本高或跨域请求多时仍合理；RAG/context可在不分叉weights时提供新鲜repository knowledge。演进是 `generic pretraining → relevant-data fine-tuning → organization shared model → developer-specific branch`，并留下model fleet与forget/delete压力。Owner `TRAIN-DATA`，handoff `TRAIN-SFT` / `AGENT-CONTEXT` / `PLATFORM-TENANCY`；disposition `Refine — Existing Argument`。

#### Towards Unified Latent Space for 3D Molecular Latent Diffusion Modeling — 2503.15567 v1，03-19

- **Score:** 4/4/4/5/3/4 = **24**。
- **Original problem / old design:** 3D molecule包含atom type、bond graph与coordinates；分离invariant/equivariant latent spaces可显式保护SE(3)结构，物理先验清楚，但多套diffusion/state和跨modality一致性增加实现与sampling成本。通用Transformer/DiT更简单，却通常不天然equivariant。
- **Changed constraint / mechanism:** UAE-3D用Relational Transformer把atom/bond/coordinate压到单一latent sequence，以standard Transformer同时解码三类输出；atom/bond CE、coordinate/distance MSE约束near-lossless reconstruction。SE(3) equivariance不再固化进diffusion architecture，而通过rotation/translation data augmentation写入unified latent；UDM-3D随后用无molecular inductive bias的DiT做latent diffusion。
- **State ownership / control flow:** encoder持有molecule→latent identity，single latent同时承载discrete chemistry与continuous geometry，decoder恢复atom/bond/coordinate；VAE revision决定diffusion latent contract。统一状态减少cross-stream synchronization，但若compression产生微小化学错误，会把invalidity一起传给generative stage。
- **Implementation / evaluation contract:** GEOM-Drugs与QM9，de novo和六种quantum-property conditional generation；QM9 split中property predictor只在独立50K subset训练。UAE reconstruction对GeoLDM VAE：atom/bond accuracy100/100、coordinate RMSD .0002Å vs98.6/96.2/.1830。单A100上two-stage 14h VAE+38h LDM=52h，作者对GeoLDM 449h、JODO139h；sampling .081s/sample vs .59/.79s，但batch/precision未披露。
- **Baselines / ablations / sensitivity:** GEOM-Drugs UDM-3D V&U&N .958、3D FCD17.36；QM9 .948/.881，并非所有2D metrics都绝对最好。conditional MAE六项多数优于列出baselines。相同depth/hidden下DiT优于vanilla Transformer，作者归因adaptive LayerNorm；但缺“unified vs separated latent在同一backbone/compute”完全控制，难把所有收益唯一归因unification。
- **Evidence boundary / trade-off:** 证明该molecular workload可把heterogeneous state压成统一latent并获得良好reconstruction/author-benchmark efficiency；不证明通用multimodal latent原则或真实drug discovery效用。无独立limitations节，chemical validity metrics不等价synthesizability、toxicity、docking或wet-lab success；两datasets与作者复现条件限制外推。
- **Coexistence / evolution:** separate equivariant/invariant state在可解释symmetry guarantee与高风险science场景仍更稳健；统一latent适合复杂度/throughput优先且reconstruction可严格验证时。演进是 `separate modality dynamics → unified near-lossless codec → generic latent DiT`。Owner `MULTIMODAL-REPRESENTATION`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Emerging / Experimental`，AI-for-Science limited case。

#### ViSpeak — 2503.12769 v1，03-17

- **Score:** 5/5/5/5/5/4 = **29**。
- **Original problem / old design:** offline video QA 等完整视频到齐后统一理解，turn-taking chat 也假定用户输入和模型输出互斥；对离线问答，这能简化 context、decoder ownership 与评测。但真实 streaming assistant 必须在没有显式文字指令时从视觉动作判断何时开始、打断、回应或终止，并且未来音视频在输出期间仍继续到达。
- **Changed constraint / mechanism:** ViSpeak 把 visual feedback 定义为七个有时间窗的任务：wake-up、anomaly warning、gesture、reference、interruption、humor reaction、termination。双流 chat template 同时保留 user input 与 agent output，并在进入 LLM 前融合；音视频按 1 秒片段、1 fps 排序，每段追加 `<seg>`。text/audio/visual response 用不同 marker，visual interruption 可在 segment boundary 输出 `Stop`。独立 informative binary head 根据最后一个 visual token 决定是否主动发言，阈值把“是否说”从 token generation 中拆出。
- **State ownership / control flow:** 输入流持续写入 timestamped segment state，agent output 是并行第二条流；融合层生成统一 decoder context，informative head 持有 speak/no-speak gating，LM head 只负责内容。event interval `[t1,t2]`、允许延迟 `T`、response time、conversation history 与 interruption status 都属于 streaming workflow state，而非静态模型能力。音频 turn-taking 被明确排除，故不能写成完整 omni-modal duplex agent。
- **Implementation / training:** VITA-1.5 base（Qwen2.5-7B、InternViT-300M-448px、341M audio encoder）。三阶段为 template alignment、streaming/proactive tuning、ViSpeak-Instruct；adapter pretrain lr `5e-4`/batch 256，LLM LoRA lr `1e-4`/batch 128，后两阶段沿用 finetune 配置。stage 1 为 256 image tokens、最多 16 images；streaming stage 降到 64 tokens/image、最多 64 images、1 fps。训练 context 只有 6K，hardware/precision/并发/P99 未披露。
- **Evaluation contract / ablations:** ViSpeak-Bench 为 1,000 videos/1,000 QA；ViSpeak-Instruct 34K。动作出现于 `[t1,t2]`，响应必须落在 `[t1,t2+T]`；open-ended text 由 GPT-4o 评 0–5，overall 是 timing accuracy × text score，visual reference 为 MCQ 且 time accuracy 固定 1。StreamingBench s2 62.00、OVO-Bench 61.08；ViSpeak-Bench 另有人类抽样 20%。stream fusion 的 Adaptive Sum/Linear/Add 结果接近；proactive ablation 显示 LM head 30.00、冻结 LLM 的 informative head 34.80/36.00、joint training + visual token 38.80，并提升 StreamingBench overall 到 62.00。
- **Evidence boundary / trade-off:** 证明把 streaming input/output、timing window 和 proactive gate 作为显式 state 可提升作者 benchmarks；不证明真实 wall-clock latency、P99、false-interrupt cost、open-world safety、audio duplex 或长期记忆。GPT-4o judge、脚本化收集、1 fps、固定阈值与 reference task 的特殊计分限制外推；数据规模/多样性有限，6K context，分段音频使 LibriSpeech WER 恶化到 18.4。
- **Coexistence / evolution:** offline full-context QA 和 turn-taking chat 在低实时性、用户明确提问与误触发成本高时仍合理；演进是 `offline complete context → streaming timestamped input → parallel user/agent streams → explicit speak/interruption control → memory-aware duplex interaction`。Owner `AGENT-WORKFLOW`，handoff `MULTIMODAL-REPRESENTATION` / `AGENT-PLATFORM` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Integrate — New Mechanism` candidate。

#### LLM-FE — 2503.14434 v1，03-18

- **Score:** 4/3/4/5/4/4 = **24**。
- **Original problem / old design:** conventional automated feature engineering 在预定义算子空间内 beam/search，容易复现、执行边界清晰，但不能利用字段语义和领域知识；早期 LLM feature engineering 直接一次性 prompt 或只用 validation score 选结果，未把前序失败和成功沉淀为可复用 search state。
- **Changed constraint / mechanism:** LLM-FE 把 feature engineering 写成 executable program search。prompt 注入 task metadata、feature descriptions 与 data examples，LLM 对历史高分 transformation programs 做 mutation；程序在 train split 上转换数据并训练 predictor，在 validation 上得到 accuracy 或 regression error，再把 `(program, score)` 写入 multi-population island memory。各 island 独立演化，top-performing samples 组成下一轮 in-context demonstrations，以 evaluator feedback 而非语言自评推进搜索。
- **State ownership / control flow:** LLM 只提出 transformation source，sandbox/executor 持有 code execution，tabular learner/evaluator 持有 empirical score，population database 持有 lineage 与 diversity。best validation program 是 workflow artifact，不是模型 weight；若 validation set 被反复搜索，selection overfitting、unsafe code 与 schema drift 必须由外部 policy/release gate 管理。
- **Implementation / evaluation contract:** 11 classification、10 regression 以及 8 high-dimensional/large-scale datasets，来源 OpenML/UCI/Kaggle；80/20 split、五个 random seeds/splits。统一 XGBoost 主比较，baseline 为 AutoFeat、OpenFE、CAAFE、FeatLLM；LLM baseline 默认 GPT-3.5-Turbo，限制总计 20 samples。另测 Llama-3.1-8B、MLP、TabPFN（TabPFN 大数据只取 10K）。总体表中 XGBoost base classification .820、LLM-FE GPT-3.5 .840；regression N-RMSE .324→.306；MLP .745→.784、.871→.631，但不是逐数据集都胜出。
- **Baselines / ablations / sensitivity:** 去掉 data examples、domain knowledge 或 evolutionary refinement 均削弱 aggregate result；无 evolutionary refinement 在 PC1/Balance-Scale 分别约 7/5 iterations 后 stagnate。论文还测 feature transfer、Gaussian noise `σ∈{0,.01,.05,.1}` 与 large/high-dimensional data；large dataset 会稀释 feature gain。hardware、token/cost、execution failure budget、parallel island wall time 和完整 security sandbox 未披露。
- **Evidence boundary / trade-off:** 证明 `proposal → executable evaluation → persistent population → mutation` 在所测 tabular contract 中比一次性 LLM proposal 更好；不证明 LLM 发现因果特征、跨 schema 自动迁移或 production-safe code。反复读 validation 会提高 adaptive overfitting 风险，LLM/API 与 model-training cost 较大，memory 中成功程序可造成 premature convergence，domain metadata 也可能泄露 target semantics。
- **Coexistence / evolution:** 固定 transformation library 在监管、低延迟、可解释算子与小搜索预算下仍更合适；演进是 `fixed operator search → domain-aware LLM proposal → executable validation feedback → island memory and evolutionary refinement`。Owner `AGENT-WORKFLOW`，handoff `AGENT-TOOL-CALLING` / `AGENT-MEMORY` / `PLATFORM-EVALUATION-SYSTEM`；disposition `Emerging / Experimental`。

#### Take-along Visual Conditioning / Visual Forgetting — 2503.13360 v1，03-17

- **Score:** 5/5/4/5/5/4 = **28**。
- **Original problem / old design:** multimodal decoder 把 image tokens 放在 prompt 前部，随后依赖 autoregressive text state；在短回答中这能避免重复视觉编码和 KV 成本。但长 CoT 会让已生成文本越来越支配下一步，早期视觉证据虽仍在 context 却逐渐失去有效控制。
- **Changed constraint / mechanism:** diagnostic 在 reasoning 中途移除 image，MathVista-hard 只下降约 2%，而早期移除约下降 20%，并观察约 20% tokens 后 visual attention contribution 变弱。TVC 在训练期用 Dynamic Visual Reaffirmation：在 self-reflection interval 重注 image embeddings 与 bridging prompt；推理期用 Periodic Visual Calibration：4×4 average-pool 压缩视觉 tokens，在反思点 prepend prompt 并 reset/rebuild visual KV state。机制不是“增大 context”，而是改变证据在 generation timeline 中的 placement 与 refresh policy。
- **State ownership / control flow:** visual encoder 产生 immutable evidence tokens，decoder KV 持有 text/visual cached state，PVC controller 决定何时压缩、重注和重置 visual KV；reasoning text 仍连续保留。因 reset/re-injection 改变 cache identity，position、modality、compression revision 与 reflection boundary 都必须进入 runtime state contract。
- **Implementation / data:** QVQ-72B-Preview 生成 long-CoT，Qwen2.5-72B-Instruct 以 answer match 作 yes/no judge；初次 temperature 0，55.8% invalid cases 以 temperature 1、最多 8 responses 重采并选最短 valid response，得到约 200K。数据由 MathV360K 221K、Geo170K 22K、LLaVA-OneVision 97K、Cambrian 1K 等过滤构造。Qwen2-VL 7B/72B；lr `2e-5`、batch 256、5 epochs、ZeRO-3、bf16、max text 8192，64×H20-96G；7B 10h、72B 约 4 days，仅训练 LLM+connector，冻结 visual encoder。
- **Evaluation contract / ablations:** MathVista、MathVision、MathVerse、Dynamath、OlympiadBench，以 GPT-4o-mini/VLMEvalKit 评测，MathVista/MathVerse 用 testmini 并排除指定 text-only/proof splits。7B 三项 average：base 33.9，direct SFT 38.3，TVC without PVC 41.4，without DVR 41.0，full 43.2。4×4 average pooling 对能力影响小并略提分；50K→200K 数据规模趋势向上。
- **Evidence boundary / trade-off:** 干预结果支持“长文本状态会压制视觉证据”及 re-injection 可改善作者 math benchmarks；attention weight 不是因果解释，约 2% removal gap 也不代表模型没有利用视觉。teacher/judge 共源、answer-only filtering、64-GPU 训练、KV reset/re-encode cost 与缺失 P99/concurrency 限制外推；周期性 visual injection 可能覆盖文本 working state、增加 TTFT/ITL、产生 position/cache invalidation bugs。
- **Coexistence / evolution:** 视觉 token 一次性置于 prompt 在短回答、cache 成本受限或视觉证据不需反复检查时仍合理；演进是 `single visual prefix → long-CoT visual decay diagnosis → training-time reaffirmation → inference-time compressed evidence refresh`。Owner `MULTIMODAL-REPRESENTATION`，handoff `MODEL-LONG-CONTEXT` / `INFER-KV-CACHE` / `AGENT-CONTEXT`；disposition `Integrate — New Mechanism` candidate。

#### KDTalker — 2503.12963 v1，03-17

- **Score:** 4/3/3/5/4/3 = **22**。
- **Original problem / old design:** 3DMM/fixed-keypoint talking-head pipelines 可解释、控制简单，但固定 landmarks 难以适配不同身份的 facial information density，head pose 容易收缩；直接 pixel/latent diffusion 可获得多样性，却更昂贵且可能牺牲 lip synchronization 与 identity。
- **Changed constraint / mechanism:** KDTalker 复用预训练 LivePortrait，从 reference image 提取 adaptive unsupervised 3D canonical/deformation keypoints、scale/rotation/translation 与 appearance feature；audio encoder 给出 condition。reference-guided prior 把初始 motion state 与 noise 组合，42.93M spatiotemporal diffusion 预测 `(δ,s,R,t)`，再经 `x_d=s(x_cR+δ)+t` 生成 driving keypoints，由 LivePortrait warper/decoder 渲染。RoPE 与 spatiotemporal attention 对齐跨帧 audio-keypoint dependency。
- **State ownership / control flow:** reference branch 持有 identity/appearance 和 canonical geometry，diffusion branch 持有 stochastic motion trajectory，audio condition 驱动 temporal change，renderer 把 motion state commit 为 frames。把生成从 pixels 移到低维 motion state 降低计算，但 detector/renderer error 成为 shared upstream failure。
- **Implementation / evaluation contract:** VoxCeleb 原始超过 100K clips/1,251 subjects，但只选择 4,282 aligned video-audio pairs；256×256 crop，audio 16kHz mel。HDTF 349 videos，各取前 8 秒，首帧作 reference。单 RTX 4090；training 1,000 diffusion steps，AdamW warmup+cosine，peak lr `5.12e-4`，batch 256；inference DDIM 50 steps、64 audio frames/pass、输出 512×512。作者报告 21.678 FPS，但未披露 batch、warmup、I/O 与 latency SLO。
- **Baselines / ablations / sensitivity:** 对比 SadTalker、Real3DPortrait、AniTalker、AniPortrait；指标 LSE-C/D、pose diversity、FID、CPBD、ArcFace CSIM、FPS。KDTalker 为 LSE-C 7.326、LSE-D 7.548、diversity .760、FID 9.756、CSIM .949、21.678 FPS。去 reference/attention/RoPE 均有退化；VAE/GAN/VAE+GAN branch 显示 diversity、lip sync、temporal consistency 间折中。DDIM 1→5 steps 大幅改善，50 steps FID 最优，之后边际收益消失；8→64 frames 改善 lip sync/diversity。
- **Evidence boundary / trade-off:** 证明在 HDTF、单 4090 与选齐 4,282-pair 训练集上，低维 implicit-keypoint diffusion 是 pixel-heavy branch 的可行替代；不证明跨语言、遮挡、profile face、任意 identity、真实 end-to-end latency 或 misuse safety。依赖 keypoint detector 与 LivePortrait artifact，noise/complex faces 会 misalignment，occlusion 会产生 blurred edges 和 eyes/mouth/nose distortion。
- **Coexistence / evolution:** fixed 3DMM 在强可控、低随机性与安全审计场景仍更合适；pixel diffusion 在极细 texture/editability 优先时仍可取。演进是 `fixed geometric landmarks → adaptive implicit geometry → diffusion over motion state → pretrained renderer commit`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-REPRESENTATION` / `INFER-EXECUTION` / `PLATFORM-SECURITY`；disposition `Emerging / Experimental`。

#### ELTEX — 2503.15055 v1，03-19

- **Score:** 4/4/4/5/5/4 = **26**。
- **Original problem / old design:** 小领域模型依赖少量人工标注或 naive synthetic prompt；真实数据最可信但稀缺、过时且不平衡，直接 LLM generation 可扩展却容易重复、遗漏 domain signals、复制 provider bias。在低风险通用数据增强中简单 prompt 尚可，在 cyber early-warning 这种 false-negative/false-positive 都昂贵的任务中不够。
- **Changed constraint / mechanism:** ELTEX 先让多个 LLM 汇总 cyberattack indicators，经人工筛选压缩成 domain token list，再把 task constraints、indicator list 与匿名 real examples 组成 dynamic prompt。GPT-4o 生成 0–1 label 的 synthetic social posts；pipeline 先 exact-match，再用 BGE-base-en-v1.5 embedding/cosine threshold `.9` 去重。最终把 synthetic、real 或 hybrid data 用于 Gemma-2B LoRA，因而 provenance 不只记录“synthetic”，还需记录 seed corpus、generator/version、prompt/indicator revision、dedup threshold 与 label ownership。
- **State ownership / data flow:** real corpus 与 human-refined labels 是 authoritative seed；indicator compiler 与 prompt builder 持有 domain policy，Azure GPT-4o 生成候选，dedup service 持有 identity，dataset registry commit accepted rows，trainer 只消费 versioned artifact。GPT-4o 的 continuous score 由人类只验证 binary label，故该 score 不能直接当 calibrated ground truth。
- **Implementation / evaluation contract:** 1,603 real messages 按 80/20 train/validation；只用 train seed 生成 8,892 synthetic（5,530 attack、3,362 general），另有 398 real test messages，来自 distinct attack events。released synthetic collection 11,448。Gemma-2B、PEFT/LoRA rank 8、4-bit/bf16 compute、AdamW、单 A100-80GB；real-only batch1/accum16、lr `2e-4`、10 epochs，synthetic/hybrid batch4/accum8、lr `2e-4`、5 epochs。
- **Baselines / metrics / outcome:** 比较 base、real、synthetic、hybrid Gemma-2B、Granite-3.2-2B、Llama-Primus 与 GPT-4o；accuracy、Brier、recall、F1、ROC、false-positive/negative。base 为 accuracy .51/F1 .30/Brier .43；real .65/.61/.31；synthetic .77/.76/.16；hybrid .82/.81/.14；GPT-4o .84/.81/.10。hybrid 的 false-negative .10、false-positive .08。dedup 使 attack/general 分别减少 11.8%/5.2%；threshold sensitivity 提供 `.8` 对照，但没有跨领域/跨 provider replication。
- **Evidence boundary / trade-off:** 证明 domain-indicator-guided generation + hybrid data 在该 blockchain-social-media test contract 中优于 real-only，并改善作者报告的 Brier score；不证明 synthetic score 本身可信、适用于所有 cybersecurity、超过 GPT-4，或抵抗新攻击分布。测试集只有398，seed/annotation 仍依赖 GPT-4o，provider update 破坏复现；大于100K未验证，generation/API、embedding/dedup、human review 增加成本，synthetic data 可放大 blind spots 与隐私泄漏。
- **Coexistence / evolution:** 纯人工真实数据在高监管、可获得专家标签与 rare-tail correctness 优先时仍是基线；naive synthesis 在探索性低风险任务仍便宜。演进是 `real-only scarce corpus → naive synthetic expansion → domain-indicator prompt contract → dedup/provenance → real+synthetic hybrid evaluation`。Owner `TRAIN-DATA`，handoff `PLATFORM-ARTIFACT` / `PLATFORM-EVALUATION-SYSTEM` / `PLATFORM-SECURITY`；disposition `Refine — Existing Argument`。

### 3.5 Owner-week correction：4 个 v1 identity 回拨 W11（不计 W12 strict / owner）

#### STEVE: Step Verification for Computer-use Agent Training — 2503.12532 v1，03-16

- **Owner week:** 2025-W11（Sunday 03-16），不是 W12。W12 row 必须改为 `Spillback — W11`；以下 packet可供 W11 ledger串行写回。
- **Score:** 5/5/5/5/5/4 = **29**。
- **Mechanism:** 从 seed tasks用 GPT-o1生成可执行 desktop tasks，Qwen2-VL agent采 trajectory；GPT-4o verifier读取 action前后 screenshot、reasoning与action，输出 stepwise binary beneficial/harmful label；KTO使用 unpaired positive/negative action，multi-round重新采样以扩展negative distribution。UI grounding与agent policy共享base但有分布冲突，KTO+LoRA避免纯SFT对localization的明显遗忘。
- **State / evaluation:** environment screenshot transition是 step evidence，verifier不是环境真值；late-trajectory precision下降说明历史依赖超出两帧。grounding数据含 WebUI180K images/1M elements、SeeClick10K/150K、AITW15K、Allava50K、private Windows10K/80K；Qwen2-VL7B。grounding AdamW/cosine lr2e-5、batch32、1 epoch；KTO lr5e-5、batch16、2 epochs、LoRA r256/alpha16、beta.1，vision encoder frozen。WinAgentArena success SFT7.1、KTO14.2、GPT-4o planner+own grounding23.0；KTO R3 File Explorer/Web/VScode 46/26/18%，五 runs。agent 0.4s/frame、作者API price估算 $6/1K tasks，但hardware/concurrency未披露。
- **Boundary / evolution:** 证明 environment transition可把 sparse outcome转成 stepwise preference data，并在该Windows benchmark优于SFT；不证明 verifier判断等价于 task success、安全操作或跨OS泛化。GPT-4o judge相关偏差、late-step context缺失、private data、任务生成器与evaluation分布相近均限制外推。演进是 `behavior cloning → outcome reward → screen-transition step verification → unpaired KTO → iterative policy/data refresh`。Owner `AGENT-WORKFLOW`，handoff `TRAIN-DPO` / `PLATFORM-EVALUATION-SYSTEM` / `PLATFORM-SECURITY`；disposition `Integrate — New Mechanism` candidate for W11。

#### MagicID — 2503.12689 v1，03-16

- **Owner week:** 2025-W11（Sunday 03-16），不是W12。W12 census必须标记 `Spillback — W11`。
- **Score:** 5/4/4/5/5/4 = **27**。
- **Mechanism / state:** 静态reference self-reconstruction在video inference形成1-frame→multi-frame domain shift，训练越久motion越收缩。MagicID从initial/fine-tuned T2V outputs与reference-inflated static videos建立repository；ID encoder、RAFT optical flow、VLM分别产identity/dynamics/prompt rewards。第一阶段选大ID差且容忍motion的pairs；第二阶段用三目标non-dominated upper/lower Pareto front选top100 dynamic pairs。HPO以diffusion noise-prediction error相对frozen reference实现DPO-style preference loss。
- **Evaluation contract:** HunyuanVideo，AdamW lr2e-5、wd1e-4；先1000-step LoRA/customization，再5000-step HPO；20 prompts，100 fine-tuned+20 initial videos，single H100，DDIM50 steps、CFG7.5，61 frames/720×1280。40 characters×40 action prompts；MagicID FaceSim .600、dynamic14.42、temporal .9933、CLIP-T26.28、CLIP-I78.83、FVD1228.33；25 raters/40 sets。ID-only pairs face .605但dynamic7.382；加dynamic pairs14.42，验证目标trade-off。
- **Boundary / evolution:** 证明machine-scored hybrid preference pairs可缓解该single-person customization合同的identity/motion冲突；不证明scores等价human preference、多人identity、任意base video model或生产成本。只有100 Pareto pairs、40 identities、reward models correlated bias，且per-identity 6K-step optimization昂贵。演进是 `static self-reconstruction → reward-scored pair repository → identity-first stage → Pareto dynamic stage → reference-constrained diffusion preference optimization`。Owner `TRAIN-DPO`，handoff `MULTIMODAL-GENERATIVE-PARADIGMS`；disposition `Emerging / Experimental` for W11。

#### LLM-Mediated Guidance of Multi-Agent Reinforcement Learning Systems — 2503.13553 v1，03-16

- **Owner week:** 2025-W11（Sunday 03-16），不是 W12；W12 只保留 `Spillback — W11`。
- **Score:** 5/5/4/5/4/4 = **27**。
- **Problem / mechanism:** 已训练 MARL policy 在 reward misspecification 或用户目标变化后，重新训练成本高；直接让非专家写 reward 或 action policy 又不现实。论文让 LLM mediator 把自然语言策略翻译为 task list，在 300-step intervention window 内覆盖 learned-policy actions；rule-based mediator 是同构基线。共享 PPO policy 与 centralized training 保留原有学习路径，所有 intervention transitions 仍写入 shared replay/training buffer，因此指导不是旁路演示，而会改变后续 policy state。
- **Evaluation contract:** AWS Unity wildfire 环境，3 agents（扩展实验到 6），每 agent 输入 8-D vector 与 42×42 RGB，动作含左右移动和投水；环境含隐藏 wind、humidity、temperature、terrain。使用 Pharia-1-LLM-7B-control-aligned 与 Llama-3.1-8B-Instruct，PPO 训练 `3e5` timesteps、10 trials。reward 被大幅重塑：例如 extinguish reward `5→1000`、village penalty `-50→0`。无 intervention 的 episode reward `238.34±14.34`；Pharia rule-based / NL 为 `437.65 / 372.05`，Llama 为 `376.18 / 331.22`；agent 数增加时 coordination 下降。
- **Evidence boundary / trade-off:** 证明在该模拟器、强 reward reshape 与中央 mediator 合同中，自然语言可经 mediator 改写行动并提高指定目标表现；不证明真实 wildfire、安全人类接管或通用可扩展协作。中央 mediator 是 single point of failure，parser/prompt 可覆盖原本正确动作；NL 分支慢于且未胜过 rule-based branch，shared buffer 会把错误干预固化进 policy。演进是 `fixed learned policy → rule-based override → natural-language-to-task mediation → intervention data re-enters learning loop`。Owner `AGENT-MULTI-AGENT`，handoff `TRAIN-RLHF` / `AGENT-WORKFLOW` / `PLATFORM-SECURITY`；disposition `Emerging / Experimental` for W11。

#### CURIE: Evaluating LLMs on Multitask Scientific Long Context Understanding and Reasoning — 2503.13517 v1，03-14

- **Owner week:** 2025-W11（Friday 03-14），不是 W12；W12 只保留 `Spillback — W11`。
- **Score:** 4/5/4/5/4/3 = **25**。
- **Problem / mechanism:** 通用 long-context benchmark 多测 needle retrieval 或单一问答，不能揭示 scientific document 中结构化抽取、跨段约束与领域推理的不同 failure mode。CURIE 建立 10 个新任务、覆盖 6 个科学领域，以完整论文/材料为 context，由 PhD experts 标注；例如 GEO 要从 19 篇论文提取 dataset/site/variable/description/time/spatial range，BIOGR 还需从地图恢复 bounding box。它的贡献是 evaluation contract，不是新的模型或 serving mechanism。
- **Evaluation contract:** 模型 context 均至少 32K；比较 Mixtral、Command-R+、LongLLaMA、Gemini 1.0/1.5/2 Flash、GPT-4o、Claude 3 Opus。指标含 ROUGE-L、BERTScore-F1、dictionary matching precision/recall/F1；LMScore 使用 GPT-4o 对 bad/ok/good 的 top-5 log-probabilities并在部分任务与人工评分相关。Claude 3 Opus overall 最强；GPT-4o 在 GEO/BIOGR 强但在 PDB/HFD 出现 repetition/nontermination，Gemini 2 Flash 在 PDB 约半数输出 Python。专家 agreement 在 HFE/DFT-S >95%、MPV >80%、GEO >90%。
- **Evidence boundary / trade-off:** 证明模型排名会随 scientific task、output structure 与 metric 改变，并暴露 repetition/nontermination 等 harness-visible failure；不证明 closed-model 内部机制、科学结论正确或生产成本。任务规模与领域不均，automatic metric 会误排；GPT-4o judge 相关偏差、closed model version drift、无 hardware/cost/P99/SLO 都限制外推。演进是 `generic long-context QA → domain paper tasks → typed scientific outputs → expert/automatic metric triangulation`。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `MODEL-LONG-CONTEXT` / `AGENT-RAG` / `AGENT-WORKFLOW`；disposition `Refine — Existing Argument` for W11。

## 4. 新发现 census（68 条：64 W12 owner + 4 W11 spillback）

以下 68 个 identity 原先未进入 W12 scoring ledger，现已逐项路由：57 个 W12 strict review、4 个 W12 low-score closure、3 个 W12 blocked、4 个回拨 W11。日期统一按 arXiv v1 / official first-public；没有把 discovery priority 当 final score。

| # | Candidate | arXiv / first public | Priority | Proposed owner | Status |
| ---: | --- | --- | --- | --- | --- |
| 1 | Survey on Evaluation of LLM-based Agents | 2503.16416 / 03-20 | P-low | `PLATFORM-EVALUATION-SYSTEM` | Low-score closure 19；§3.2 |
| 2 | One-Step Residual Shifting Diffusion | 2503.13358 / 03-17 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Unverified / Blocked — event-time v1 full text |
| 3 | Stop Overthinking survey | 2503.16419 / 03-20 | P-low | `MODEL-SAMPLING` | Low-score closure 19；§3.2 |
| 4 | Inside-Out: Hidden Factual Knowledge | 2503.15299 / 03-19 | P-high | `WORLDVIEW-REPRESENTATION` | Strict Review Complete；§3.4 |
| 5 | RL for Reasoning in Small LLMs | 2503.16219 / 03-20 | P-high | `TRAIN-GRPO` | Strict Review Complete；§3.4 |
| 6 | Cosmos-Reason1 | 2503.15558 / 03-19 | P-high | `MULTIMODAL-EMBODIED-VLA` | Strict Review Complete；§3.4 |
| 7 | φ-Decoding | 2503.13288 / 03-17 | P-high | `MODEL-SAMPLING` | Strict Review Complete；owner corrected；§3.4 |
| 8 | TULIP | 2503.15485 / 03-19 | P-high | `MULTIMODAL-REPRESENTATION` | Unverified / Blocked — event-time v1 full text |
| 9 | Why Do Multi-Agent LLM Systems Fail? | 2503.13657 / 03-18 | P-high | `AGENT-MULTI-AGENT` | Strict Review Complete；§3.4 |
| 10 | DeepMesh | 2503.15265 / 03-19 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 11 | Vecset Diffusion / FlashVDM | 2503.16302 / 03-20 | P-high | `INFER-EXECUTION` | Strict Review Complete；owner corrected；§3.4 |
| 12 | Scale-wise Distillation | 2503.16397 / 03-20 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 13 | JARVIS-VLA | 2503.16365 / 03-20 | P-high | `MULTIMODAL-EMBODIED-VLA` | Strict Review Complete；§3.4 |
| 14 | InfiniteYou | 2503.16418 / 03-20 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 15 | Fin-R1 | 2503.16252 / 03-20 | P-high | `TRAIN-GRPO` | Strict Review Complete；domain boundary；§3.4 |
| 16 | VidKV | 2503.16257 / 03-20 | P-high | `INFER-KV-CACHE` | Strict Review Complete；§3.4 |
| 17 | DiffMoE | 2503.14487 / 03-18 | P-high | `MODEL-MOE` | Strict Review Complete；§3.4 |
| 18 | Cube: Roblox View of 3D Intelligence | 2503.15475 / 03-19 | P-high | `MULTIMODAL-REPRESENTATION` | Strict Review Complete；§3.4 |
| 19 | SynCity | 2503.16420 / 03-20 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；owner corrected；§3.4 |
| 20 | MathFusion | 2503.16212 / 03-20 | P-high | `TRAIN-DATA` | Strict Review Complete；§3.4 |
| 21 | Temporal Regularization for Video | 2503.15417 / 03-19 | P-high | `TRAIN-DATA` | Strict Review Complete；owner corrected；§3.4 |
| 22 | MetaLadder | 2503.14891 / 03-19 | P-high | `TRAIN-DATA` | Strict Review Complete；owner corrected；§3.4 |
| 23 | LEGION | 2503.15264 / 03-19 | P-high | `PLATFORM-EVALUATION-SYSTEM` | Strict Review Complete；official v1 PDF fallback；§3.4 |
| 24 | Efficient Personalization of Quantized Diffusion | 2503.14868 / 03-19 | P-high | `TRAIN-LORA` | Strict Review Complete；§3.4 |
| 25 | Optimizing Decomposition for Claim Verification | 2503.15354 / 03-19 | P-high | `PLATFORM-EVALUATION-SYSTEM` | Strict Review Complete；owner corrected；§3.4 |
| 26 | MotionStreamer | 2503.15451 / 03-19 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 27 | STEVE computer-use verifier | 2503.12532 / **03-16** | P-high | `AGENT-WORKFLOW` | **Spillback — W11**；strict packet §3.5；不计 W12 owner |
| 28 | Tokenize Image as a Set | 2503.16425 / 03-20 | P-high | `MULTIMODAL-REPRESENTATION` | Strict Review Complete；§3.4 |
| 29 | 1000+ FPS 4D Gaussian Splatting | 2503.16422 / 03-20 | P-high | `INFER-EXECUTION` | Strict Review Complete；owner corrected；§3.4 |
| 30 | XAttention | 2503.16428 / 03-20 | P-high | `MODEL-SELF-ATTENTION` | Strict Review Complete；§3.4 |
| 31 | M3: 3D-Spatial Multimodal Memory | 2503.16413 / 03-20 | P-high | `AGENT-MEMORY` | Strict Review Complete；§3.4 |
| 32 | CaKE circuit-aware editing | 2503.16356 / 03-20 | P-high | `TRAIN-LORA` | Strict Review Complete；owner corrected；§3.4 |
| 33 | Expert Race | 2503.16057 / 03-20 | P-high | `MODEL-MOE` | Strict Review Complete；§3.4 |
| 34 | SWEET-RL | 2503.15478 / 03-19 | P-high | `TRAIN-RLHF` | Strict Review Complete；§3.4 |
| 35 | Sonata | 2503.16429 / 03-20 | P-high | `MULTIMODAL-REPRESENTATION` | Strict Review Complete；§3.4 |
| 36 | Ultra-Resolution Adaptation | 2503.16322 / 03-20 | P-high | `TRAIN-LORA` | Strict Review Complete；§3.4 |
| 37 | CLS-RL | 2503.16188 / 03-20 | P-high | `TRAIN-GRPO` | Strict Review Complete；§3.4 |
| 38 | SkyLadder | 2503.15450 / 03-19 | P-high | `TRAIN-PRETRAINING` | Strict Review Complete；§3.4 |
| 39 | MusicInfuser | 2503.14505 / 03-18 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 40 | MagicMotion | 2503.16421 / 03-20 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 41 | BigO(Bench) | 2503.15242 / 03-19 | P-high | `PLATFORM-EVALUATION-SYSTEM` | Strict Review Complete；§3.4 |
| 42 | Temporal Consistency for Reasoning Error Identification | 2503.14495 / 03-18 | P-high | `PLATFORM-EVALUATION-SYSTEM` | Strict Review Complete；§3.4 |
| 43 | Free-form robotic reasoning and grasping | 2503.13082 / 03-17 | P-high | `MULTIMODAL-EMBODIED-VLA` | Strict Review Complete；§3.4 |
| 44 | NuiScene | 2503.16375 / 03-20 | P-high | `MULTIMODAL-WORLD-MODELS` | Strict Review Complete；world-state boundary；§3.4 |
| 45 | Zero-1-to-A | 2503.15851 / 03-20 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 46 | Concat-ID | 2503.14151 / 03-18 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 47 | Decompositional Scene Reconstruction | 2503.14830 / 03-19 | P-high | `MULTIMODAL-WORLD-MODELS` | Strict Review Complete；scene-state branch；§3.4 |
| 48 | Agents Play Thousands of 3D Video Games | 2503.13356 / 03-17 | P-high | `AGENT-WORKFLOW` | Strict Review Complete；score 23 / evidence downgrade；§3.4 |
| 49 | Coarse-to-Fine AR Image Generation | 2503.16194 / 03-20 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete；§3.4 |
| 50 | SALT | 2503.16055 / 03-20 | P-high | `TRAIN-LORA` | Strict Review Complete；§3.4 |
| 51 | Where do LVLMs Look? | 2503.13891 / 03-18 | P-high | `MULTIMODAL-REPRESENTATION` | Strict Review Complete；§3.4 |
| 52 | Training Video Foundation Models with NVIDIA NeMo | 2503.12964 / 03-17 | P-high | `TRAIN-DISTRIBUTED-TRAINING` | Strict Review Complete；§3.4 |
| 53 | GASP | 2503.15672 / 03-19 | P-high | `MULTIMODAL-WORLD-MODELS` | Strict Review Complete；§3.4 |
| 54 | AIMI sparse-event forecasting | 2503.16091 / 03-20 | P-low | `TRAIN-DATA` | Low-score closure 18；§3.2 |
| 55 | Deceptive Humor benchmark | 2503.16031 / 03-20 | P-low | `PLATFORM-EVALUATION-SYSTEM` | Low-score closure 18；§3.2 |
| 56 | Deployment-efficient video models / FluxViT | 2503.14237 / 03-18 | P-high | `TRAIN-PRETRAINING` | Strict Review Complete；§3.4 |
| 57 | See-Saw Modality Balance | 2503.13834 / 03-18 | P-high | `TRAIN-PRETRAINING` | Strict Review Complete；§3.4 |
| 58 | MagicID | 2503.12689 / **03-16** | P-high | `TRAIN-DPO` | **Spillback — W11**；strict packet §3.5；不计 W12 owner |
| 59 | Personalized code completion | 2503.14201 / 03-18 | P-high | `TRAIN-DATA` | Strict Review Complete；owner/priority corrected；§3.4 |
| 60 | Unified latent space for 3D molecules | 2503.15567 / 03-19 | P-high | `MULTIMODAL-REPRESENTATION` | Strict Review Complete；score 24 / priority corrected；§3.4 |
| 61 | VideoRFSplat | 2503.15855 / 03-20 | P-high | `MULTIMODAL-WORLD-MODELS` | Unverified / Blocked — malformed v1 HTML and unavailable v1 PDF；§3.3 |
| 62 | ViSpeak | 2503.12769 / 03-17 | P-high | `AGENT-WORKFLOW` | Strict Review Complete 29；§3.4 |
| 63 | LLM-FE | 2503.14434 / 03-18 | P-high | `AGENT-WORKFLOW` | Strict Review Complete 24；owner/priority corrected；§3.4 |
| 64 | Take-along Visual Conditioning / Visual Forgetting | 2503.13360 / 03-17 | P-high | `MULTIMODAL-REPRESENTATION` | Strict Review Complete 28；§3.4 |
| 65 | KDTalker | 2503.12963 / 03-17 | P-high | `MULTIMODAL-GENERATIVE-PARADIGMS` | Strict Review Complete 22；identity/priority corrected；§3.4 |
| 66 | LLM-Mediated Guidance of MARL Systems | 2503.13553 / **03-16** | P-high | `AGENT-MULTI-AGENT` | **Spillback — W11**；Strict Review Complete 27；§3.5 |
| 67 | CURIE scientific long-context evaluation | 2503.13517 / **03-14** | P-high | `PLATFORM-EVALUATION-SYSTEM` | **Spillback — W11**；Strict Review Complete 25；§3.5 |
| 68 | ELTEX | 2503.15055 / 03-19 | P-high | `TRAIN-DATA` | Strict Review Complete 26；identity recovered；§3.4 |

### 摘要级 priority facts（不能升级为 Full Source Review）

- GASP：query future spacetime 的 general occupancy、ego occupancy、distilled semantic features；需核验 action-conditioning、forecast horizon、sensor schema、downstream ablation。
- NeMo video training：必须锁定 2025 NeMo/Megatron version、parallel strategy、hardware/reproducibility，不能用 current docs 倒写。

## 5. Owner-week spillback / duplicates

### 回拨 W11 或更早（不计 W12 owner）

- DropletVideo 2503.06053 — 03-08 → W10。
- Being-0 2503.12533、SPIN-Bench 2503.12349、STEVE 2503.12532、MagicID 2503.12689、LLM-Mediated Guidance 2503.13553、Atlas 2503.12355 — 03-16 → W11；Federated-Learning GIA survey 2503.11514 — 03-13、CURIE 2503.13517 — 03-14 → W11。HF 推荐/展示日不覆盖 arXiv v1 owner date。
- SmolDocling、ReCamMaster、PLADIS、VGGT、Personalize Anything、API vs GUI Agents、MCoT Survey、Adversarial Data Collection、LHM、AudioX、CapArena、State Space Model Survey、GKG-LLM、VERIFY、Vamba、FlowTok、TxAgent、reWordBench、V-STaR、Large-scale Grounded Video Caption、Kolmogorov-Arnold Attention、MPBench、MTV-Inpaint、ETCH、Reflect-DiT、Long-Video Audio Multi-Agent、Florenz、Neighboring AR、ProJudge、TikZero、UVE、Painting with Words：owner 均在 W10/W11，W12 只保留 spillback，不重复评分。
- 精确早期 ID：GKG 2503.11227、VERIFY 2503.11557、LHM 2503.10625、UVE 2503.09949、Painting with Words 2503.07906、reWordBench 2503.11751、V-STaR 2503.11495。

### same-family / revision

- Multimodal Preference Survey v1 03-18、v2 03-23：同 family，一次评分。
- TokenBridge v1 03-20、v2 03-22、v3 08-29：同 family；事件时只以 v1 为机制证据。
- ETVA v1 03-21、v2 08-17：同 family；v2 只作 related revision。
- DeepPerception v1/v2 与 KARL v3、R0 later rename、BlobCtrl later rewrite、Cosmos-Transfer1 later revision：均不得倒写 event-time。

## 6. Engineering / fixed-organization sweep

旧 W12 已保留 Google Private Prediction、NVIDIA Dynamo、SGLang joins PyTorch。本轮逐仓库核验 event-time official release/tag，新增 vLLM v0.8.1、Transformers v4.50.0 两个 strict owner 与 JAX v0.5.3 一个低分 owner。负向路由也已闭合：SGLang v0.4.4 为 03-13（W11）、Ray 2.43 为 02-27、DeepSpeed 0.16.5 与 Transformers v4.50.1 为 03-27/03-25（W13）；OpenXLA 没有 W12 official GitHub release，Megatron-LM 未定位到 W12 first-public release identity。没有把 absence of release 当产品能力结论。

### 6.1 vLLM v0.8.1 — strict Full Source Review

- **Candidate / Week / Score:** vLLM v0.8.1 / 2025-W12 / 3/4/4/5/4/3 = **23/30**。
- **Source Family ID / type / date:** `vllm-v0-8-1-correctness-release`；official GitHub release；published 2025-03-19 17:40 UTC，tag `v0.8.1`，commit `61c7a1b`。v0.8.0 是 previous state；later tags 不倒写 W12。
- **Direct / related primary sources and coverage:** official release/tag 与 linked changelog/code changes 已核验；相关 vLLM repository docs 只用于理解 component ownership。覆盖 release metadata、breaking/correctness fixes、sampling/structured-output/processor-cache/TPU 与 model-support changes；release 没有独立 design paper、benchmark 或 limitations。
- **Original problem / previous design / changed constraint:** v0.8.0 的功能集合在普通路径可工作，但 sampling dtype、top-k、structured-output backend、processing cache、chunked-prefill padding 等边界暴露 correctness/compatibility 问题。patch release 的目标是锁定这些 execution contracts，而不是提出新的 serving architecture。
- **Mechanism / state ownership / control flow:** sampled-token IDs、sampling logits/dtype、structured-output backend selection、processor cache key/size 与 chunked-prefill padding 分别由 sampler、grammar/backend dispatcher、input processor cache 和 platform execution path 持有。v0.8.1 修复这些状态跨路径解释不一致，并增加 Triton rejection sampler、Gemma3 V1、embedding LoRA 等受版本约束能力。
- **Implementation / evaluation contract:** release note 可追踪具体 change/PR 与 commit identity，但未提供统一 workload、baseline、ablation 或 regression matrix；因此 correctness 结论限于被修复的代码路径，不能从 change list 推导端到端吞吐收益。
- **Hardware / model / precision / length / batch / concurrency / SLO:** release note 未披露统一 model、GPU/TPU、precision、sequence length、batch/concurrency、TTFT/ITL/P99 或 cost SLO；全部记 `Not Disclosed`。
- **Evidence / non-evidence / trade-offs:** 证据证明 2025-03-19 存在这些 version-scoped fixes/features；不证明 v0.8.1 普遍更快、更稳定或适用于所有 backends。增加 backend/model paths 扩大 test matrix，cache/padding/dtype identity 错配仍可能造成 silent correctness failure。
- **Old design boundary / evolution / owner:** v0.8.0 在未触发相关边界或已 downstream patch 的部署仍可运行；演进是 `feature expansion → edge-path inconsistency → patch-level contract repair`。owner `INFER-VLLM`（current Ch50 / legacy Ch46），handoff `INFER-SPECULATIVE-DECODING` 与 `INFER-REQUEST-LIFECYCLE`。
- **Integration decision / chapters / open questions:** `Weekly Only — Version/Correctness Fact`。已同读 Ch50 与 Ch48；Books 已以 engine state/exactness contract 承载一般机制，Historical Books Gate 关闭且本 release 不构成新长期机制。缺完整 regression matrix、backend compatibility table 与 production SLO。

### 6.2 Transformers v4.50.0 — strict Full Source Review

- **Candidate / Week / Score:** Transformers v4.50.0 / 2025-W12 / 4/4/4/5/4/3 = **24/30**。
- **Source Family ID / type / date:** `transformers-v4-50-0-tp-assisted-generation-release`；official GitHub release；published 2025-03-21 13:40 UTC，tag `v4.50.0`，commit `0b057e6`。v4.50.1 于 03-25 属 W13。
- **Direct / related primary sources and coverage:** official release/tag、linked documentation/PR summaries 已核验；覆盖 tensor-parallel initialization、assisted generation、model additions、deprecations 与 mutable model-release tag policy。没有用 current main-branch docs 倒写 event-time behavior。
- **Original problem / previous design / changed constraint:** 先完整 materialize model 再做 tensor-parallel shard 的加载路径实现简单，却在大模型初始化时制造峰值 host/device memory；assisted generation 若要求严格同 tokenizer/model family，又限制 proposal model 可替换性。model support 快速增长还使传统 package version 无法单独表达某个 model implementation 的更新节奏。
- **Mechanism / state ownership / control flow:** module-by-module TP initialization 在权重装载阶段直接按 parallel plan 创建/分发 shard，减少 full-model peak；assisted generation 放宽 assistant-model compatibility并支持 sampling，但 proposal/target tokenization、acceptance 与 RNG state 仍必须由 generation loop 统一控制。model-based release tags 被明确设计成 mutable 指针，复现 owner 必须记录 immutable commit，而不能只保存 tag 名。
- **Implementation / evaluation contract:** release 证明这些 API/code paths 在该版本进入 official package；没有统一模型、基线、ablation、peak-memory 数值或 generation exactness benchmark，故只形成 implementation/version evidence。
- **Hardware / model / precision / length / batch / concurrency / SLO:** release note 未提供统一 hardware、model size、precision、length、batch/concurrency、latency/P99 或 cost SLO，均为 `Not Disclosed`。
- **Evidence / non-evidence / trade-offs:** module-wise TP 可消除“必须先持有完整权重”的结构性峰值，但会把 sharding plan、device mesh、parameter naming 与 checkpoint revision 加入加载身份；more-general assistant sampling 提高兼容性，却扩大 tokenizer alignment、proposal quality 与 acceptance-state 测试空间。release 不证明任意模型都节省相同比例内存或获得 speedup。
- **Old design boundary / evolution / owner:** 小模型、内存充足或单设备加载时 full materialization 更简单；同-family deterministic assistant 在 exactness/debug 优先时仍更稳。演进是 `full materialization → shard-aware construction` 与 `restricted assistant → generalized proposal contract` 两条并行 implementation branch。
- **ROADMAP / chapters / disposition / open questions:** canonical owner `INFER-TENSORRT-LLM` 的 generic execution-plan responsibility（current Ch49 / legacy Ch45），handoff `INFER-SPECULATIVE-DECODING`（Ch48）与 `PLATFORM-MODEL-REGISTRY`（Ch59）。已同读 Ch49/48/59；`Weekly Only — Version/Implementation Fact`，不改 Books。缺 model-specific memory measurements、assistant exactness matrix 与 immutable artifact retention policy 的生产证据。

### 6.3 JAX v0.5.3 — low-score closure

- **Identity / source / date:** `jax-v0-5-3-dynamic-slice-categorical-release`；official GitHub release `jax-v0.5.3`，published 2025-03-19，commit `c8032a9`。
- **Score / rejection:** 2/3/3/5/2/2 = **17/30**。`allow_negative_indices` 为 `dynamic_slice/update` 提供显式 index contract，并可避免部分 code-size expansion；`random.categorical(replace=False)` 增加无放回采样。两者有长期 correctness 价值，但 release 没有 AI workload、hardware、benchmark、ablation 或系统级机制变化，故 `Weekly Only — Low-score Version Fact`，不升级 Full Source Review。
- **Owner / boundary:** `INFER-TENSORRT-LLM` generic execution owner，训练/采样章节只作 handoff；不能据 API addition 推导 compiler/runtime speedup。

## 7. 缺失材料清单

| Priority | Family / known identity | 现有材料为何不足 | 可接受材料 / 建议文件名 | 补回后的审计范围 |
| --- | --- | --- | --- | --- |
| P1 Full Text | TokenBridge / https://arxiv.org/abs/2503.16430，v1 03-20 | HTML 错渲染，摘要只能确认 continuous VAE→dimension-wise quantization→AR loss，无法核验公式、codebook identity、实验和limitations | v1 PDF、HTML、TXT或作者 manuscript；`2025-W12-tokenbridge-v1.pdf` | Method/公式、实现、baseline/ablation、hardware/runtime、limitations 与 owner/disposition |
| P1 Full Text | Judge Anything / https://arxiv.org/abs/2503.17489；https://github.com/URRealHero/JudgeAnything，v1 03-21 | repo/scripts 只确认 TaskAnything 规模与模型列表，不能证明 judge protocol、human agreement、ablation 和 failure analysis | v1 PDF、HTML、TXT或带 version 的 author manuscript；`2025-W12-judge-anything-v1.pdf` | evaluator contract、prompt/judge identity、human calibration、实验、limitations 与最终评分 |
| P3 Revision | TULIP / https://arxiv.org/abs/2503.15485v1，v1 03-19 | v2 明示澄清 fine-tuning 并更新 appendix；不能把这些 later details 当 event-time evidence | event-time v1 PDF/HTML/TXT；`2025-W12-tulip-v1.pdf` | v1/v2 diff、Method、训练合同、ablation、hardware、limitations 与 disposition |
| P3 Revision | One-Step Residual Shifting Diffusion / https://arxiv.org/abs/2503.13358v1；https://github.com/Daniil-Selikhanovych/RSD，v1 03-17 | v1 约 48 MB 且 HTML cache miss；repo/v5 已转向 later ICML 2026 state，摘要不足以锁定 distillation objective 与 restoration/perception trade-off | event-time v1 PDF/HTML/TXT或作者 manuscript；`2025-W12-rsd-v1.pdf` | v1 mechanism/公式、teacher/student flow、baseline/ablation、hardware、limitations、revision diff 与评分 |
| P3 Revision | VideoRFSplat / https://arxiv.org/abs/2503.15855v1；https://github.com/gohyojun15/VideoRFSplat，v1 03-20 | v1 HTML 错渲染、PDF fetch 失败；repo 仍为 README/TODO，ICCV final 是 later evidence | event-time v1 PDF/HTML/TXT或作者 manuscript；`2025-W12-videorfsplat-v1.pdf` | dual-stream/communication/asynchronous denoising 的 v1 实现、实验、hardware、limitations、later-final diff 与评分 |

## Evidence Level

- Strict Full Source Review：98。
- Low-score identity/date/score/rejection closure：7。
- Unverified / Blocked：5。
- Ordinary Review Pending：0。
- W11 spillback strict packets：4，不计 W12 owner 分母。

## Knowledge Tree Position

所有已审 owner 均映射到 ROADMAP 中现有 Stable Node；未创建新 owner。跨周重复按 Source Family 与 v1 first-public date 路由。

## Recommended Action

W12 candidate evidence ledger 按 **110 owner identities** 条件闭合；五个 blocker 依据精确材料请求暂时跳过，ordinary Review Pending 为 0。用户若提供缺失 PDF/TXT/HTML，可逐项解除 archive source-complete 限制，无需重做已完成 98 项。Historical Books Gate 继续关闭。

## Event-Date Daily Decision

Historical Backfill 不补造 Daily。四个 W11 spillback 只回写 W11/年度索引，不在 W12 重复计分。

## Books Integration Decision

**Books Frozen — Historical Gate Closed.**

## Ignored Noise

早周 owner、same-family later revision 与窗口外 engineering release 均不重复评分；HF recommendation day 不覆盖 first-public date。固定组织负向路由和 cross-index recall limitation 已显式保留，不把“没找到 W12 release”写成产品能力事实。

## Repository Changes

- W12 owner census 从旧 43-row 初始账本修正到 110。
- 恢复 ETVA v1 全文，并写回 vLLM v0.8.1、Transformers v4.50.0 与 JAX v0.5.3 三个固定组织 owner events。
- 最终账本为 98 strict、7 low closures、5 blocked 与 4 个 W11 spillback packets；五项 blocker 均有精确材料请求。
- 未修改 Books，未 stage、commit 或 push。

## Open Questions

- 能否取得五个 blocked families 的 event-time v1 PDF/TXT/HTML？
- 后续若取得 Scholar/OpenAlex/DBLP/Crossref 的 event-time immutable discovery export，是否出现尚未建立 identity 的新候选？当前不是 ordinary Review Pending，也不改变 110-owner 可复算分母。
- W11 接收四个 spillback 后的 denominator 与 strict count 是否需要再次重算？

## Sources

- `CODEX_HISTORICAL_RESEARCH_PROMPT.md`
- `papers/2025/weekly/2025-W11/README.md`
- `papers/2025/weekly/2025-W12/README.md`
- `papers/2025/weekly/2025-W13/README.md`
- `papers/2025/weekly/README.md`
- `ROADMAP.md`
- HF W12 weekly discovery: https://huggingface.co/papers/week/2025-W12
- HF 2025-03-20: https://huggingface.co/papers/date/2025-03-20
- HF 2025-03-21: https://huggingface.co/papers/date/2025-03-21
- ETVA event-time v1 PDF: https://arxiv.org/pdf/2503.16867v1
- vLLM v0.8.1 official release: https://github.com/vllm-project/vllm/releases/tag/v0.8.1
- Transformers v4.50.0 official release: https://github.com/huggingface/transformers/releases/tag/v4.50.0
- JAX v0.5.3 official release: https://github.com/jax-ml/jax/releases/tag/jax-v0.5.3
- DeepMesh v1: https://arxiv.org/html/2503.15265v1
- DiffMoE v1: https://arxiv.org/html/2503.14487v1
- JARVIS-VLA v1: https://arxiv.org/html/2503.16365v1
- RSD v1 metadata: https://arxiv.org/abs/2503.13358v1
- RSD later official artifact (not event-time proof): https://github.com/Daniil-Selikhanovych/RSD
- FlashVDM v1: https://arxiv.org/html/2503.16302v1
- SwD v1: https://arxiv.org/html/2503.16397v1
- InfiniteYou v1: https://arxiv.org/html/2503.16418v1
- Fin-R1 v1: https://arxiv.org/html/2503.16252v1
- Cube v1: https://arxiv.org/html/2503.15475v1
- SynCity v1: https://arxiv.org/html/2503.16420v1
- MathFusion v1: https://arxiv.org/html/2503.16212v1
- FluxFlow v1: https://arxiv.org/html/2503.15417v1
- MetaLadder v1: https://arxiv.org/html/2503.14891v1
- LEGION event-time v1 PDF: https://arxiv.org/pdf/2503.15264v1
- ZOODiP v1: https://arxiv.org/html/2503.14868v1
- DyDecomp v1: https://arxiv.org/html/2503.15354v1
- MotionStreamer v1: https://arxiv.org/html/2503.15451v1
- TokenSet v1: https://arxiv.org/html/2503.16425v1
- 4DGS-1K v1: https://arxiv.org/html/2503.16422v1
- STEVE v1 (W11 spillback): https://arxiv.org/html/2503.12532v1
- M3 v1: https://arxiv.org/html/2503.16413v1
- CaKE v1: https://arxiv.org/html/2503.16356v1
- Sonata v1: https://arxiv.org/html/2503.16429v1
- URAE v1: https://arxiv.org/html/2503.16322v1
- CLS-RL v1: https://arxiv.org/html/2503.16188v1
- MusicInfuser v1: https://arxiv.org/html/2503.14505v1
- MagicMotion v1: https://arxiv.org/html/2503.16421v1
- BigO(Bench) v1: https://arxiv.org/html/2503.15242v1
- Temporal Consistency v1: https://arxiv.org/html/2503.14495v1
- FreeGrasp v1: https://arxiv.org/html/2503.13082v1
- NuiScene v1: https://arxiv.org/html/2503.16375v1
- Zero-1-to-A v1: https://arxiv.org/html/2503.15851v1
- Concat-ID v1: https://arxiv.org/html/2503.14151v1
- DP-Recon v1: https://arxiv.org/html/2503.14830v1
- PORTAL v1: https://arxiv.org/html/2503.13356v1
- Coarse-to-Fine AR v1: https://arxiv.org/html/2503.16194v1
- SALT v1: https://arxiv.org/html/2503.16055v1
- Where do LVLMs Look v1: https://arxiv.org/html/2503.13891v1
- NeMo Video Foundation Models v1: https://arxiv.org/html/2503.12964v1
- GASP v1: https://arxiv.org/html/2503.15672v1
- AIMI v1: https://arxiv.org/html/2503.16091v1
- Deceptive Humor v1: https://arxiv.org/html/2503.16031v1
- FluxViT v1: https://arxiv.org/html/2503.14237v1
- BalGrad v1: https://arxiv.org/html/2503.13834v1
- MagicID v1 (W11 spillback): https://arxiv.org/html/2503.12689v1
- Personalized Code Completion v1: https://arxiv.org/html/2503.14201v1
- Unified 3D Molecular Latent v1: https://arxiv.org/html/2503.15567v1
- ViSpeak v1: https://arxiv.org/html/2503.12769v1
- LLM-FE v1: https://arxiv.org/html/2503.14434v1
- Take-along Visual Conditioning v1: https://arxiv.org/html/2503.13360v1
- KDTalker v1: https://arxiv.org/html/2503.12963v1
- ELTEX v1: https://arxiv.org/html/2503.15055v1
- LLM-Mediated Guidance v1 (W11 spillback): https://arxiv.org/html/2503.13553v1
- CURIE v1 (W11 spillback): https://arxiv.org/html/2503.13517v1
- Agent Evaluation Survey v1: https://arxiv.org/html/2503.16416v1
- Stop Overthinking Survey v1: https://arxiv.org/html/2503.16419v1
- VideoRFSplat v1 metadata: https://arxiv.org/abs/2503.15855v1
- VideoRFSplat later empty artifact (not event-time proof): https://github.com/gohyojun15/VideoRFSplat
- §3 embeds all reviewed arXiv v1 URLs；§4 embeds primary IDs, writeback should use `https://arxiv.org/abs/<id>` and reopen each before final scoring。

## Reviewer Check

- ISO / owner-week routing：Pass。
- HF weekly/daily replay 与 W13 spillback：Pass；ETVA 已恢复，Atlas 与 Federated-Learning GIA survey 按 v1 日期回拨 W11，未误用推荐日。
- Fixed-organization release replay：Pass；3 个 W12 owner 写回，5 个窗口外 release/identity 做负向路由，OpenXLA/Megatron 不因 absence 被制造为候选。
- Source Family / revision dedup：Pass；ETVA、TokenBridge、TULIP、RSD 与 VideoRFSplat 的 later revisions 均未重复计分或倒写 event-time mechanism。
- Denominator decomposition：旧 22 strict + W13 spillback lane（17 strict + 2 low + 2 blocked）+ W12 reopened academic lane（57 strict + 4 low + 3 blocked）+ fixed-organization additions（2 strict + 1 low）= **110**；另 4 个 W11 spillback 明确排除。
- 98 strict + 7 low + 5 blocked = 110 W12 owner identities；四个 W11 spillback 不计入分母。
- Review Pending = 0；五个 source blockers 均有精确材料请求，fixed-organization replay 已闭合。
- Candidate Evidence Gate `Conditional Pass`；cross-index recall limitation 与五项 archive source blockers 已披露；Historical Books Gate Closed。
