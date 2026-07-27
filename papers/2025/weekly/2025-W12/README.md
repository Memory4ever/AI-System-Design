# AI Research Weekly — 2025-W12

> Coverage Window: 2025-03-17～2025-03-23
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 3 项与长期 AI System 认知相关的证据：Differentially private LLM inference for synthetic data、NVIDIA Dynamo、SGLang joins PyTorch ecosystem。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Differentially private LLM inference for synthetic data（2025-03-18）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：NVIDIA Dynamo（2025-03-18）。
- 保留：SGLang joins PyTorch ecosystem（2025-03-19）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Differentially private LLM inference for synthetic data | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Must Read；全文复核后判断是否 refine Security |
| NVIDIA Dynamo | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；作为第 48 章演进起点 |
| SGLang joins PyTorch ecosystem | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Record Only；不写入正文 |

### Deep Analysis 1 — Differentially private LLM inference for synthetic data

- First Public: 2025-03-18
- Status: Google Research official blog + paper
- Primary Source: https://research.google/blog/generating-synthetic-data-with-differentially-private-llm-inference/
- Evolution Relationship: Principle Reuse

#### Why

用敏感数据生成合成数据时，prompt/query 本身可能泄露个体信息；只保护训练阶段不覆盖 inference-time generation。

#### Principle and Mechanism

研究在 LLM inference 的 sampling/aggregation 中加入 differential privacy accounting，试图控制单个记录对合成输出的影响。

#### Trade-off and Evidence Boundary

隐私预算提供形式化边界，却牺牲 utility 并增加 sampling 成本；边界取决于 threat model、epsilon/delta 和生成流程。

#### Connection and Evolution

知识树位置：第 23、62、68 章。Must Read；全文复核后判断是否 refine Security。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — NVIDIA Dynamo

- First Public: 2025-03-18
- Status: Official open-source announcement
- Primary Source: https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/
- Evolution Relationship: Direct Evolution

#### Why

reasoning workload 的长输入、长输出和变化中的 KV state 使单机 serving engine 难以独立完成集群级路由、PD placement 与内存协调。

#### Principle and Mechanism

初始 Dynamo 把 planner、smart router、distributed runtime、KV transfer/store 与 telemetry 组织为分布式推理层；版本实现需以代码和后续 releases 为准。

#### Trade-off and Evidence Boundary

解耦可分别扩展阶段和资源，却新增 state transfer、控制面一致性、故障恢复与跨节点 tail latency。厂商性能数字不脱离 workload contract 使用。

#### Connection and Evolution

知识树位置：第 48、50～52、58 章。Must Read；作为第 48 章演进起点。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 3 — SGLang joins PyTorch ecosystem

- First Public: 2025-03-19
- Status: Official governance announcement
- Primary Source: https://pytorch.org/blog/sglang-joins-pytorch/
- Evolution Relationship: Layering / Dependency

#### Why

成熟 inference runtime 的长期可持续性还取决于治理、生态接口和多厂商协作。

#### Principle and Mechanism

这是项目归属与社区治理事实，不是新 runtime 机制。

#### Trade-off and Evidence Boundary

基金会托管可扩大协作，也不自动保证技术路线、兼容性或性能。

#### Connection and Evolution

知识树位置：第 47 章。Record Only；不写入正文。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Private prediction for large-scale synthetic text generation

- **Candidate / Week / Score:** Differentially private LLM inference for synthetic data / 2025-W12 / 23/30。
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
- **ROADMAP Node:** 主 owner 第 68 章；第 23、62 章提供 data/evaluation handoff。
- **Target and Adjacent Chapters Read:** 已读第 67 章 Multi Tenant、第 68 章 Security、第 69 章 Production Best Practice。
- **Existing Coverage:** 第 68 章已写明 synthetic output、privacy unit、composition、accountant 与 inference-time / fine-tuning 适用边界，且已引用该论文；Source Review 证实该论点方向正确，但发现年度 first-public 归档错误。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，复核 privacy unit、composition 与 2024 first-public 边界。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/68-security.md`；不把 2025 Blog 当作新论文机制。
- **Open Questions:** 年度索引如何标记“2025 official amplification of 2024 research”；真实产品的 release-level budget ledger、重复 query 与 user-level adjacency 如何实现。

### NVIDIA Dynamo

- **Candidate / Week / Score:** NVIDIA Dynamo / 2025-W12 / 27/30。
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
- **ROADMAP Node:** 主 owner 第 48 章；第 47、49、50～52、58 章为 handoff。
- **Target and Adjacent Chapters Read:** 已读第 47 章 SGLang、第 48 章 Dynamo、第 49 章 KServe LLM；核对第 46、50～52 章边界。
- **Existing Coverage:** 第 48 章已经以 request/state/control paths、KV-aware routing、KVBM/NIXL、planner 与 failure semantics 组织长期框架；但当前正文主要基于 2026 docs，需要在最终 integration 时补回 2025 launch → later architecture 的演进边界。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch48，补回 2025 launch→后续三路径架构的版本边界。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/48-dynamo.md`。
- **Open Questions:** 是否能定位 2025-03 archived commit 的组件 readiness；planner 的稳定性、recovery、versioned KV layout 与跨 engine compatibility。

### SGLang joins PyTorch ecosystem

- **Candidate / Week / Score:** SGLang joins PyTorch ecosystem / 2025-W12 / 20/30。
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
- **ROADMAP Node:** 主 owner 第 47 章。
- **Target and Adjacent Chapters Read:** 已读第 46 章 vLLM、第 47 章 SGLang、第 48 章 Dynamo。
- **Existing Coverage:** 第 47 章已准确区分历史 paper abstraction 与当前通用 serving framework，并包含 identity、fairness、state adapter 边界；治理公告没有新增长期机制。
- **Integration Decision:** `Weekly Only — Governance Fact`；基金会归属不等于 runtime mechanism。
- **Changed Files or Rejection Reason:** 不改 Books；Ch47 保留技术 owner，治理公告仅留 Weekly。
- **Open Questions:** PyTorch ecosystem 的生命周期/退出机制怎样影响依赖风险；技术兼容仍须按具体 release 验证。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Differentially private LLM inference for synthetic data → 第 23、62、68 章（Principle Reuse）
- NVIDIA Dynamo → 第 48、50～52、58 章（Direct Evolution）
- SGLang joins PyTorch ecosystem → 第 47 章（Layering / Dependency）

## Recommended Action

- Differentially private LLM inference for synthetic data：Must Read；全文复核后判断是否 refine Security
- NVIDIA Dynamo：Must Read；作为第 48 章演进起点
- SGLang joins PyTorch ecosystem：Record Only；不写入正文

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W12/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- inference-time DP 的 privacy unit 与重复 query composition 仍需按部署 contract 明确。
- Dynamo 的跨节点 state freshness、failure recovery 与版本兼容性继续由后续实现证据约束。
- 项目治理归属本身不证明 runtime correctness 或性能。
- 年度索引需把 private prediction 论文 first-public 改为 2024，并把 2025-03-18 记为 Google Research Blog 传播事件。

## Sources

- Differentially private LLM inference for synthetic data — https://research.google/blog/generating-synthetic-data-with-differentially-private-llm-inference/（First Public: 2025-03-18；Accessed: 2026-07-31）
- Private prediction for large-scale synthetic text generation — https://arxiv.org/abs/2407.12108（v1: 2024-07-16；v2: 2024-10-09；Accessed: 2026-07-31）
- NVIDIA Dynamo — https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/（First Public: 2025-03-18；Accessed: 2026-07-31）
- NVIDIA Dynamo repository — https://github.com/ai-dynamo/dynamo（Accessed: 2026-07-31；current repository, not launch-day API evidence）
- NVIDIA Dynamo architecture — https://github.com/ai-dynamo/dynamo/blob/main/docs/design-docs/architecture.md（Accessed: 2026-07-31；later evolution evidence）
- SGLang joins PyTorch ecosystem — https://pytorch.org/blog/sglang-joins-pytorch/（First Public: 2025-03-19；Accessed: 2026-07-31）
- SGLang paper — https://arxiv.org/abs/2312.07104（v1: 2023-12-12；Accessed: 2026-07-31）
- PyTorch Ecosystem Working Group — https://pytorch.org/blog/introducing-the-pytorch-ecosystem-working-group-and-project-spotlights/（First Public: 2025-06-05；Accessed: 2026-07-31）
