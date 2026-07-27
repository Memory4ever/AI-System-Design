# AI Research Weekly — 2025-W23

> Coverage Window: 2025-06-02～2025-06-08
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Gateway API Inference Extension。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 本组无达到保留门槛的候选。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- Source-family chronology pointer：Urania（arXiv:2506.04681）v1 于 2025-06-05 首次公开；
  其候选评分与完整 Source Review 保留在 W50 的 2025-12-10 Google Research follow-up 下，
  此处不重复计分或生成第二套机制结论。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：Gateway API Inference Extension（2025-06-05）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gateway API Inference Extension | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Must Read；与 llm-d/KServe 共同重建第 58 章 |

### Deep Analysis 1 — Gateway API Inference Extension

- First Public: 2025-06-05
- Status: Official Kubernetes project design
- Primary Source: https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/
- Evolution Relationship: Direct Evolution

#### Why

HTTP path/round-robin 看不到模型 identity、queue、KV cache、adapter 与请求 criticality，因此会把部分有状态的 inference 当成普通无状态流量。

#### Principle and Mechanism

设计以 InferencePool 表达平台管理的 serving endpoints，以 InferenceModel 表达模型所有者的逻辑 endpoint/policy，并通过 Endpoint Selection Extension 使用实时指标选择后端。

#### Trade-off and Evidence Boundary

模型感知路由改善决策输入，却新增 selector 可用性、metric freshness、stale routing、policy conflict 与安全边界；roadmap 项不能写成已实现事实。

#### Connection and Evolution

知识树位置：第 49、52、57、58 章。Must Read；与 llm-d/KServe 共同重建第 58 章。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Gateway API Inference Extension

- **Candidate / Week / Score:** Gateway API Inference Extension / 2025-W23 / 28/30。
- **Source Family ID:** `GAIE-2025-06`。
- **Source Type:** Kubernetes official design announcement、project API/docs/repository。
- **First-public Date / Revision History:** 本周证据日期为2025-06-05的official Kubernetes article；项目在此前已有alpha design，且2026 repository发生EPP/API迁移。当前docs只用于识别演进，不回投到2025 architecture。
- **Direct Primary Sources:** Kubernetes 2025-06-05 article；InferencePool/InferenceModel API docs；Endpoint Selection Extension design与project repository。
- **Related Primary Sources:** Gateway API、Envoy ext-proc、llm-d integration docs。
- **Access and Verification Status:** Verified for 2025 published design；roadmap与后续GA/migration能力严格分开。
- **Full-read Coverage:** 已阅读问题定义、persona/API model、request flow、ESE scheduling、benchmark setup/results与roadmap；同时检查API ownership discussion、repository当前migration note以识别后续变化。
- **Original Problem:** HTTPRoute/round-robin看不到model identity、adapter、request criticality、queue与KV locality，长且部分有状态的LLM request会形成hotspot。
- **Why the Previous Design Was Reasonable:** 对短、同质、无cache affinity的HTTP请求，Service/Gateway的简单endpoint balancing稳定、通用且failover语义清晰。
- **Changed Constraint:** request cost由input/output token和active sequence决定，replica状态由queue、loaded adapter与KV cache决定，且模型owner和platform owner需要不同API。
- **Mechanism:** `InferencePool`由platform表达共享serving endpoints/policy，`InferenceModel`由model owner表达public model identity、fine-tune与traffic policy；Gateway匹配pool后调用Endpoint Selection Extension，根据live metrics/capabilities返回具体endpoint。
- **State Ownership:** Gateway拥有route与forwarding；ESE/EPP拥有一次endpoint decision；model server拥有queue/KV/adapter事实；InferencePool与InferenceModel分别由platform/model personas管理。selector不是engine scheduler的唯一事实源。
- **Control Flow / Data Flow:** client → Gateway/HTTPRoute → InferencePool → ext-proc/ESE读取endpoint metrics/capabilities → 选定pod → Gateway转发。metric/control path与token/KV data path分离。
- **Implementation Details:** 2025设计基于Gateway API CRDs与extension point；InferenceModel映射public name到pool内model/fine-tune；roadmap中的remote prefix、fairness、HPA、heterogeneous accelerator与PD不能写成已实现。
- **Evaluation Setup:** 10个Llama2 replicas、vLLM V1、H100 80GB pods、ShareGPT workload、100–1000 QPS，比较ESE与standard Kubernetes Service；报告高负载下p90 latency趋势及近似throughput。
- **Baselines / Ablations / Sensitivity:** baseline只有standard Service；未披露model size、precision、input/output分布、exact pod/GPU count、warmup、run variance、SLO，也没有queue/KV/criticality scorer消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H100 80GB、Llama2、10 replicas与QPS范围披露；其余关键contract不完整，故不保留泛化性能数字。
- **What the Evidence Actually Proves:** 证明Kubernetes社区提出persona-separated inference routing API，并在一个受限setup下观察到高负载tail-latency改善。
- **What It Does Not Prove:** 不证明所有model-aware scorer优于round-robin，不证明roadmap能力已实现，不证明stale metric或EPP failure下仍满足SLO。
- **Limitations / Threats to Validity:** 单一作者benchmark、workload contract不全、project alpha演化快、ESE/EPP术语迁移。
- **Trade-offs / New Failure Modes:** richer signal改善placement，却新增metric freshness、selector availability、fail-open/close、policy conflict、tenant leakage、route/engine double-scheduling与observability join。
- **Where the Previous Design Still Applies:** 同质replica、低负载、低state affinity时Service/least-connections仍更简单；engine内token scheduler仍不可被gateway替代。
- **Evolution Relationship:** `Direct Evolution`：network endpoint routing → model/state-aware endpoint selection；与engine scheduling是`Layering / Dependency`。
- **ROADMAP Node:** Ch49、Ch52、Ch57、Ch58。
- **Target and Adjacent Chapters Read:** 已阅读 Ch48～52、Ch57～59；Ch58已经拥有Gateway–EPP–engine scheduler边界。
- **Existing Coverage:** Ch58覆盖persona/ownership与freshness/failure原则，但Books Gate需要与llm-d、KServe验证是否补一段“2025 API model如何把what与where分权”的演进，而不是重复CRD名。
- **Integration Decision:** `No Change — Already Covered`；Ch58 已区分 Gateway、EPP 与 engine scheduler，Ch49 拥有 topology。
- **Changed Files or Rejection Reason:** 不改 Books；API 版本事实留 Weekly。
- **Open Questions:** 能否冻结2025-06对应API commit/schema；当EPP失联、metric过期或model identity冲突时，各provider的normative behavior是什么。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- Gateway API Inference Extension → 第 49、52、57、58 章（Direct Evolution）

## Recommended Action

- Gateway API Inference Extension：Must Read；与 llm-d/KServe 共同重建第 58 章

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W23/README.md。
- 本周候选已完成 Source Review；Books Integration 仍受年度 Evidence Gate 约束。

## Open Questions

- 已完成 Gateway API Inference Extension 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。

## Sources

- Gateway API Inference Extension — https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/（First Public: 2025-06-05；Accessed: 2026-07-31）
