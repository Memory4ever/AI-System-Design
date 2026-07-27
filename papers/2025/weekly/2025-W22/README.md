# AI Research Weekly — 2025-W22

> Coverage Window: 2025-05-26～2025-06-01
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：KServe v0.15、DeepSeek-R1-0528。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：DeepSeek-R1-0528（2025-05-28）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：KServe v0.15（2025-05-27）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| KServe v0.15 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；检查第 49/57 章是否已有同义覆盖 |
| DeepSeek-R1-0528 | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Record Only；保留版本时间线 |

### Deep Analysis 1 — KServe v0.15

- First Public: 2025-05-27
- Status: Official stable release
- Primary Source: https://kserve.github.io/archive/0.15/blog/articles/2025-05-27-KServe-0.15-release/
- Evolution Relationship: Direct Evolution

#### Why

Kubernetes 上的 LLM serving 不再只是部署一个 predictor；multi-node execution、KV cache、autoscaling 与 gateway policy 需要进入声明式控制面。

#### Principle and Mechanism

v0.15 增加 Envoy AI Gateway、multi-node inference、KEDA LLM autoscaler、LMCache distributed KV 与 enhanced vLLM backend 等集成。

#### Trade-off and Evidence Boundary

声明式集成降低拼装成本，却增加 CRD/API lifecycle、跨组件 compatibility 和故障定位层级；版本 feature 不等于端到端 SLO 保证。

#### Connection and Evolution

知识树位置：第 49、51、52、57、58 章。Must Read；检查第 49/57 章是否已有同义覆盖。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — DeepSeek-R1-0528

- First Public: 2025-05-28
- Status: Official model update; vendor evaluation
- Primary Source: https://api-docs.deepseek.com/updates
- Evolution Relationship: Direct Evolution

#### Why

reasoning model 能通过后续 post-training 改善能力，但模型更新本身不自动形成新的长期机制。

#### Principle and Mechanism

官方 changelog 证明版本升级和 benchmark 变化，未披露足够新增训练机制。

#### Trade-off and Evidence Boundary

能力更新可能改变质量/成本前沿，也造成 version drift 与评测不可比；不把分数提升写入长期正文。

#### Connection and Evolution

知识树位置：第 29、62 章。Record Only；保留版本时间线。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### KServe v0.15

- **Candidate / Week / Score:** KServe v0.15 / 2025-W22 / 25/30。
- **Source Family ID:** `KSERVE-0.15-2025-05`。
- **Source Type:** 官方 archived release blog、v0.15 documentation、release notes/linked design。
- **First-public Date / Revision History:** 2025-05-27；按 archived `0.15` 文档核验，current KServe 的 `LLMInferenceService`/后续 GA 行为不回投到 v0.15。
- **Direct Primary Sources:** KServe v0.15 release article；archived v0.15 generative inference、multi-node、KEDA、LMCache、Gateway integration docs。
- **Related Primary Sources:** KServe distributed inference API work-in-progress PR、vLLM 0.8.5 与 LMCache docs；只用于依赖边界。
- **Access and Verification Status:** Verified。archived release/documentation可访问；部分 linked experimental API在后续版本演化，v0.15时未成为稳定端到端contract。
- **Full-read Coverage:** 已阅读发布全文、feature列表、示例CR、multi-node workerSpec、autoscaling metrics、LMCache transfer config、model cache与security/health-check changes，并检查其 linked roadmap 状态。
- **Original Problem:** predictive `InferenceService` 的单 predictor 抽象不足以表达超单节点模型、LLM queue signal、KV层级与token-aware gateway policy。
- **Why the Previous Design Was Reasonable:** 小模型/单节点predictor、请求成本近似稳定时，通用autoscaling与Service routing已经足够，API简单且生态成熟。
- **Changed Constraint:** 模型跨节点、输入输出长度变化、KV复用与token cost让pod count/CPU-style utilization失真，并需要额外gateway与cache component。
- **Mechanism:** v0.15在现有`InferenceService`上增加multi-node `workerSpec`、KEDA custom metrics、Envoy AI Gateway/Kubernetes Gateway integration、LMCache KV offload与model cache增强；它是多项integration的集合，不是一个统一scheduler算法。
- **State Ownership:** KServe controller拥有declarative desired/status；KEDA拥有replica scaling decision；gateway拥有ingress policy；model server拥有active execution；LMCache connector拥有外部KV tier。发布材料没有定义跨组件单一transaction owner。
- **Control Flow / Data Flow:** CRD reconcile出predictor/worker topology与gateway/autoscaler配置；request经gateway到model server；metrics回到KEDA；KV tensor经connector进入LMCache。model artifact cache与runtime KV cache是不同state family。
- **Implementation Details:** archived example使用`serving.kserve.io/v1beta1` `InferenceService`与`workerSpec.pipelineParallelSize`；autoscaling示例读取`vllm:num_requests_running`；LMCache通过`--kv-transfer-config`与chunked prefill启用。
- **Evaluation Setup:** release article没有统一端到端benchmark；示例与feature availability不能作为SLO证据。
- **Baselines / Ablations / Sensitivity:** Not Disclosed。未对gateway、multi-node、KEDA与LMCache逐项消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** multi-node动机举Llama 3.1 405B，示例含Llama 3 8B/70B；硬件、precision、length distribution、concurrency与SLO未形成完整contract。
- **What the Evidence Actually Proves:** 证明v0.15开始把generative-specific topology、metric、gateway与KV integration纳入KServe declarative surface。
- **What It Does Not Prove:** 不证明这些component默认形成正确的LLM control plane，不证明KEDA metric适合所有workload，也不证明distributed inference API在v0.15已经稳定。
- **Limitations / Threats to Validity:** release是feature inventory；各依赖版本和failure semantics分散；experimental roadmap与stable feature易混淆。
- **Trade-offs / New Failure Modes:** 声明式集成减少手工拼装，却增加CRD/version compatibility、metric lag、scale churn、partial readiness、cache invalidation与multi-controller debugging。
- **Where the Previous Design Still Applies:** 单节点、低流量或无KV共享需求的模型仍可使用传统InferenceService/Knative路径。
- **Evolution Relationship:** `Direct Evolution`：predictive serving CR → generative topology/integration surface；不等同后续`LLMInferenceService`。
- **ROADMAP Node:** Ch49、Ch51、Ch52、Ch57、Ch58。
- **Target and Adjacent Chapters Read:** 已阅读 Ch48～52 与 Ch56～59；Ch49拥有LLM topology，Ch57拥有通用declarative model serving。
- **Existing Coverage:** Ch49/57已经覆盖topology与control-plane ownership；Books Gate要核验是否需要用v0.15补出“integration bundle不等于统一correctness contract”，而非罗列版本features。
- **Integration Decision:** `No Change — Already Covered`；Ch49 已拥有 LLMInferenceService topology、lifecycle 与 failure semantics。
- **Changed Files or Rejection Reason:** 不改 Books；版本功能作为 Ch49 的实现证据，不重复清单。
- **Open Questions:** v0.15各integration的正式support level、status propagation与rollback sequence在archive中是否有更强规范。

### DeepSeek-R1-0528

- **Candidate / Week / Score:** DeepSeek-R1-0528 / 2025-W22 / 21/30。
- **Source Family ID:** `DEEPSEEK-R1-0528`。
- **Source Type:** 官方model update、API changelog/model card。
- **First-public Date / Revision History:** 2025-05-28；属于DeepSeek-R1 family的后续checkpoint，不改变R1 paper的first-public date。
- **Direct Primary Sources:** DeepSeek API update/changelog、official model repository/model card。
- **Related Primary Sources:** DeepSeek-R1 technical report用于base family机制，不把0528 benchmark反推成新训练算法。
- **Access and Verification Status:** Partially Verified。官方版本与能力/benchmark声明可核验；新增post-training recipe、data、hardware、optimizer与ablation未披露。
- **Full-read Coverage:** 已检查official update、model card/changelog与R1 report中可对应的mechanism；不存在可供全文复建的0528独立technical report。
- **Original Problem:** checkpoint refresh可改善reasoning/function calling，但如果只发布分数，系统无法判断能力变化来自data、training、decoding还是harness。
- **Why the Previous Design Was Reasonable:** 原R1 checkpoint在固定version、经过本地evaluation后仍是可治理基线；稳定性常比追逐新分数更重要。
- **Changed Constraint:** provider发布新checkpoint/API alias，造成model drift、benchmark comparability与production regression风险。
- **Mechanism:** `Mechanism Not Disclosed`。公开材料只证明model version更新及作者reported evaluations。
- **State Ownership:** provider/model registry拥有version identity；platform deployment/evaluation control plane必须pin version并决定promotion。
- **Control Flow / Data Flow:** new checkpoint → offline evaluation → shadow/canary → promotion/rollback；不是“changelog score上升→自动替换”。
- **Implementation Details:** Not Disclosed beyond model/API artifacts。
- **Evaluation Setup:** 作者公开若干benchmark变化，但完整hardware、serving stack、precision、concurrency/SLO与所有baseline harness并未作为统一contract披露。
- **Baselines / Ablations / Sensitivity:** 无新机制消融；version-to-version分数不能归因。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Disclosed as a complete contract。
- **What the Evidence Actually Proves:** 证明0528是新的official checkpoint/version fact。
- **What It Does Not Prove:** 不证明新的长期training/system principle，不证明普遍优于原R1，不证明production cost-quality frontier必然改善。
- **Limitations / Threats to Validity:** vendor benchmark、未披露recipe、alias drift与评测集污染风险。
- **Trade-offs / New Failure Modes:** 新version可能提升能力，也引入behavior drift、tool/schema regression、revalidation成本与rollback依赖。
- **Where the Previous Design Still Applies:** 已验证、可复现且满足SLO的旧checkpoint仍应保留，直到新version通过同一production contract。
- **Evolution Relationship:** `Direct Evolution` at artifact/version level；不是已公开mechanism evolution。
- **ROADMAP Node:** Ch29、Ch62、Ch69。
- **Target and Adjacent Chapters Read:** 已阅读 Ch28～30、Ch62、Ch69；这些章节已经区分training mechanism、evaluation object与release gate。
- **Existing Coverage:** Ch62/69已有version-bound evaluation与progressive delivery原则；当前证据没有新增机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact`。
- **Changed Files or Rejection Reason:** 不改 Books；无公开新训练机制。
- **Open Questions:** 是否存在同日可验证的official model card commit、weight hash与完整evaluation harness。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- KServe v0.15 → 第 49、51、52、57、58 章（Direct Evolution）
- DeepSeek-R1-0528 → 第 29、62 章（Direct Evolution）

## Recommended Action

- KServe v0.15：Must Read；检查第 49/57 章是否已有同义覆盖
- DeepSeek-R1-0528：Record Only；保留版本时间线

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W22/README.md。
- 本周候选已完成 Source Review；Books Integration 仍受年度 Evidence Gate 约束。

## Open Questions

- 已完成 KServe v0.15 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。
- 已完成 DeepSeek-R1-0528 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。

## Sources

- KServe v0.15 — https://kserve.github.io/archive/0.15/blog/articles/2025-05-27-KServe-0.15-release/（First Public: 2025-05-27；Accessed: 2026-07-31）
- DeepSeek-R1-0528 — https://api-docs.deepseek.com/updates（First Public: 2025-05-28；Accessed: 2026-07-31）
