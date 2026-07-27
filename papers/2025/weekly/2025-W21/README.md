# AI Research Weekly — 2025-W21

> Coverage Window: 2025-05-19～2025-05-25
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 3 项长期证据：llm-d community launch、Claude 4、User-level differential privacy for LLM fine-tuning。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Claude 4（2025-05-22）。
- 保留：User-level differential privacy for LLM fine-tuning（2025-05-23）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 保留：llm-d community launch（2025-05-20）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| llm-d community launch | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；与 KServe/Gateway/Dynamo 建立边界 |
| Claude 4 | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；与 Memory/Tool章节交叉审查 |
| User-level differential privacy for LLM fine-tuning | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Must Read；与 W12 inference-time DP 形成层次关系 |

### Deep Analysis 1 — llm-d community launch

- First Public: 2025-05-20
- Status: Official open-source project launch
- Primary Source: https://developers.redhat.com/articles/2025/05/20/llm-d-kubernetes-native-distributed-inferencing
- Evolution Relationship: Direct Evolution

#### Why

传统 Service/round-robin 不理解 KV locality、prefill/decode 阶段、adapter 与 SLO，单 engine 也不拥有 Kubernetes fleet 的全局状态。

#### Principle and Mechanism

llm-d 以 vLLM 为 data plane，结合 Inference Gateway、KV-aware routing、PD disaggregation 与 Kubernetes-native lifecycle，形成可替换组件的 distributed inference stack。

#### Trade-off and Evidence Boundary

模块化避免单体锁定，却新增组件版本矩阵、跨层观测、状态一致性和责任边界；项目发布不等于所有路径已生产成熟。

#### Connection and Evolution

知识树位置：第 48、49、51、52、57、58 章。Must Read；与 KServe/Gateway/Dynamo 建立边界。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 2 — Claude 4

- First Public: 2025-05-22
- Status: Official release + system card; vendor evaluation
- Primary Source: https://www.anthropic.com/news/claude-4
- Evolution Relationship: Direct Evolution

#### Why

长时 coding/agent workload 需要在 reasoning 中调用工具，并把跨轮次状态外化到文件或 memory。

#### Principle and Mechanism

官方发布披露 extended thinking with tool use、parallel tools 与通过文件保存事实的产品行为；内部实现未知。

#### Trade-off and Evidence Boundary

外化 memory 提高 continuity，也带来 provenance、staleness、权限和 prompt injection 风险；benchmark 无法分离模型与 harness。

#### Connection and Evolution

知识树位置：第 52、62、73～77 章。Worth Watching；与 Memory/Tool章节交叉审查。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

### Deep Analysis 3 — User-level differential privacy for LLM fine-tuning

- First Public: 2025-05-23
- Status: Google Research official blog + paper
- Primary Source: https://research.google/blog/fine-tuning-llms-with-user-level-differential-privacy/
- Evolution Relationship: Direct Evolution

#### Why

record-level DP 不能限制同一用户多条记录的累计影响；真实对话和个性化数据的隐私单元通常是 user。

#### Principle and Mechanism

研究把 user-level clipping/sampling/accounting 用于 LLM fine-tuning，并分析 user contribution 不均衡的优化问题。

#### Trade-off and Evidence Boundary

更强隐私单元提高保护语义，却降低有效样本量、增加噪声与训练复杂度；utility 结论取决于用户分布和 privacy budget。

#### Connection and Evolution

知识树位置：第 25、62、68 章。Must Read；与 W12 inference-time DP 形成层次关系。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### llm-d community launch

- **Candidate / Week / Score:** llm-d community launch / 2025-W21 / 27/30。
- **Source Family ID:** `LLMD-2025-LAUNCH`。
- **Source Type:** 官方项目发布、创始 proposal、开源仓库。
- **First-public Date / Revision History:** 项目于 2025-05-20 公开；当前 proposal 页面后来随项目重组而更新，因此只把其中明确写作 initial goals/design choices 的内容用于 2025 机制重建，2026 component/release 事实不回投到首发版本。
- **Direct Primary Sources:** llm-d 首发公告；`llm-d` founding proposal；项目仓库与 launch-time architecture description。
- **Related Primary Sources:** vLLM、Gateway API Inference Extension 与 NIXL 各自文档；它们证明依赖层能力，不证明 llm-d 的端到端成熟度。
- **Access and Verification Status:** Verified。公告、proposal 与 repository documentation 均可访问；首发时各 component 的精确 commit matrix 未在公告完整冻结。
- **Full-read Coverage:** 已阅读 launch announcement、proposal 的 goals/non-goals、四项 primary techniques、三层 runtime、design choices、user stories 与 success criteria；同时检查当前仓库说明以识别术语演化，未把后续 release 能力写成 2025 已实现事实。
- **Original Problem:** 单一 engine 或 Kubernetes Service 只掌握局部执行/endpoint 状态，无法同时利用 prefix locality、prefill/decode 分工、硬件差异、queue pressure 与 fleet lifecycle。
- **Why the Previous Design Was Reasonable:** 单副本、共享无状态 replica 与 round-robin 在模型较小、请求短、cache reuse 弱且副本近似同质时简单、可恢复、易运维。
- **Changed Constraint:** 大模型、长 prompt、shared-prefix、PD 分离和多硬件 pool 使 request placement 影响 TTFT、tail latency、cache reuse 与 accelerator efficiency。
- **Mechanism:** founding proposal 把系统拆为 inference scheduler、vLLM data plane 与 remote prefix cache，并把 tiered prefix cache、disaggregated serving、LLM-aware load balancing、autoscaling 作为四条独立但可组合的 scale path；scheduler-directed RPC 在 latency/throughput 间选择，而非把所有逻辑塞进 engine。
- **State Ownership:** engine 拥有 token execution 与本地 KV；scheduler 拥有 routing/flow-control decision；remote cache 层拥有可跨 replica 扩展的 prefix state。proposal 特别区分 replica-local in-memory cache 与 durable/disaggregated cache，避免把 replica 无意变成唯一事实 owner。
- **Control Flow / Data Flow:** request 经 Inference Gateway/selector 进入 scheduler，scheduler 根据 workload 与 cache/queue signal 选择 replica 或 prefill/decode path；KV data 通过 engine/NIXL path 转移，metadata/routing signal 与 tensor data path 分离。
- **Implementation Details:** vLLM 提供 point-to-point disaggregated serving；NIXL 抽象 KV transfer；Kubernetes API 表达 pool/workload；upstream-first 与可替换 component 是设计选择。proposal 不是 production conformance specification。
- **Evaluation Setup:** 首发 proposal 只定义 scale、perf/$ at target latency 与 operational toil 等 success criteria；没有一个绑定 model、hardware、length、concurrency、precision 与 SLO 的统一结果集。
- **Baselines / Ablations / Sensitivity:** Not Disclosed at launch。首发材料没有给出完整 round-robin、monolithic runtime 与各组件消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Not Disclosed as a complete workload contract；因此不保留首发性能外推。
- **What the Evidence Actually Proves:** 证明 llm-d 的长期设计意图是模块化 distributed inference stack，并明确 ownership 分层与四类扩展机制。
- **What It Does Not Prove:** 不证明所有路径在 2025-05 已 production-ready，不证明任一组件组合对所有模型/硬件优于单体 runtime，也不证明 current repository 行为等同首发状态。
- **Limitations / Threats to Validity:** launch material 带项目愿景性质；component 快速演进会造成术语与 API drift；缺少首发 commit-pinned、端到端 workload contract。
- **Trade-offs / New Failure Modes:** 模块化换来替换性，却新增版本矩阵、metric freshness、cross-layer tracing、KV ownership/invalidation、partial failure、policy conflict 与升级顺序。
- **Where the Previous Design Still Applies:** 小模型、弱 prefix reuse、低并发或单 pool 场景仍可用单 engine/简单 load balancing，避免 control-plane tax。
- **Evolution Relationship:** `Direct Evolution`：single-engine optimization → fleet-aware routing/cache/PD composition；不是 vLLM、KServe 或 Gateway 的替代品。
- **ROADMAP Node:** Ch48、Ch49、Ch51、Ch52、Ch57、Ch58。
- **Target and Adjacent Chapters Read:** 已阅读 Ch47～52 与 Ch57～59；Ch48 拥有 distributed runtime，Ch58 拥有 gateway/EPP boundary，Ch49/57 拥有 KServe topology/control-plane boundary。
- **Existing Coverage:** 现有 Ch48 已解释 request/control/state path、KV-aware routing 与 disaggregation；Ch58 已解释 Gateway–EPP–engine scheduler 分工，但尚需在 Books Gate 与 KServe/Gateway 候选联审后确认是否缺少“local cache 与 durable cache ownership 分离”这一演进节点。
- **Integration Decision:** `No Change — Already Covered`；Ch48/49 已区分 engine data plane、distributed runtime 与 Kubernetes control plane。
- **Changed Files or Rejection Reason:** 不改 Books；source family 用于确认分层，不重复 release architecture。
- **Open Questions:** 能否找到 2025-05 精确 commit/tag 以冻结 component/API matrix；首发四条 path 分别在哪个 release 达到可重复 workload contract。

### Claude 4

- **Candidate / Week / Score:** Claude 4 / 2025-W21 / 22/30。
- **Source Family ID:** `ANTHROPIC-CLAUDE4-2025-05`。
- **Source Type:** 官方 announcement + 124 页 system card。
- **First-public Date / Revision History:** 2025-05-22；system card 后于 2025-07-16 做脚注/格式修订，并于 2025-09-02 修正 Claude Code Impossible Tasks 数字，故当前 PDF 的被修正数字不冒充发布日原值。
- **Direct Primary Sources:** Claude 4 announcement；Claude Opus 4 & Sonnet 4 System Card（May 2025，含 changelog）。
- **Related Primary Sources:** Anthropic extended-thinking/tool-use API 文档仅用于产品 contract；第三方 customer quotes 不作为机制证据。
- **Access and Verification Status:** Verified。announcement 与完整 system card 可访问；model architecture、post-training objective、tool-policy training 与 memory implementation 未披露。
- **Full-read Coverage:** 已覆盖 system card 的 model/training characteristics、release process、safeguards、agentic safety、alignment assessment、model welfare、RSP capability assessments、cyber/CBRN 与附录；announcement 的 benchmark methodology、extended thinking with tools、parallel tools、file-backed memory 与 API contract 已联读。
- **Original Problem:** 长时 coding/agent task 需要在多步 reasoning 中获取外部 observation，并在 context 之外保存可恢复状态；仅靠一次 completion 或不可审计 hidden reasoning 无法提供 durable continuity。
- **Why the Previous Design Was Reasonable:** 对短任务，单次 context 内 reasoning 与串行 tool call 更简单，也减少文件写入、权限和 stale state 风险。
- **Changed Constraint:** task horizon 延长到多工具、多文件与多小时执行，单 context 的容量、恢复和 provenance 边界暴露。
- **Mechanism:** 官方只公开产品行为：extended thinking 可与 tool use 交替、tools 可并行、developer 提供本地文件访问时模型可创建/维护 memory files；thinking summary 由较小模型压缩。内部 routing、training 与 write policy 未披露。
- **State Ownership:** 模型生成 tool/file proposals；host application/Claude Code 与文件系统拥有执行和持久状态。system card 没有证明模型本身拥有 durable memory subsystem。
- **Control Flow / Data Flow:** model reasoning → tool proposal → host execution → observation 返回 reasoning；file-backed memory 是显式 artifact path，不是参数更新。并行 tool 的 join、conflict 与 retry contract 未在 release 中完整公开。
- **Implementation Details:** 两个模型均为 hybrid reasoning modes；官方披露训练数据类别、截止时间、过滤与 release safety levels，但架构、参数量、optimizer、tool-training recipe 为 Not Disclosed。
- **Evaluation Setup:** announcement 的 SWE-bench 使用 bash/file-edit scaffold；high-compute variant 包含 parallel attempts、visible-test rejection 与 internal scorer；TAU-bench 将 step cap 从 30 提至 100。system card 评估覆盖 computer use、agentic coding、prompt injection、reward hacking 与 capability thresholds。
- **Baselines / Ablations / Sensitivity:** 有 model/snapshot 与 scaffold comparison，但没有把 model、harness、tool access、parallel sampling 各自贡献完整消融；后续 system-card 数字还发生修订。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** API context/pricing 与部分 reasoning budget有披露；训练硬件、precision、batch、production concurrency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明公开 product contract 支持 reasoning–tool interleave、parallel tool proposals 与 host-provided file state；也证明 agent benchmark 结论强依赖 scaffold、step budget 与 selection method。
- **What It Does Not Prove:** 不证明“模型具有长期记忆”这一内部机制，不证明数小时 autonomous claim 可脱离 harness/权限成立，不证明 benchmark gain 来自某个已公开 training mechanism。
- **Limitations / Threats to Validity:** vendor-run evaluations、snapshot drift、system-card number corrections、rare-scenario elicitation 与 classifier-based analysis限制外推；system card 自身多次强调评估集不能覆盖所有 attacks。
- **Trade-offs / New Failure Modes:** tool/reasoning interleave提高适应性，却增加 prompt injection、observation poisoning、parallel side-effect conflict、budget exhaustion 与 audit burden；file memory增加 continuity，也新增 provenance、staleness、authorization、deletion 与 poisoning。
- **Where the Previous Design Still Applies:** 短、低风险、可一次验证的任务仍应优先无持久 memory、少工具与 deterministic workflow。
- **Evolution Relationship:** `Layering / Dependency`：model capability 只能在 host tool/workflow/memory contracts 上交付，不是 Workflow runtime 的替代。
- **ROADMAP Node:** Ch52、Ch62、Ch73～77。
- **Target and Adjacent Chapters Read:** 已阅读 Ch52、Ch62、Ch72～77；Memory、Tool Calling 与 Workflow 已明确 host/runtime ownership。
- **Existing Coverage:** Ch73 已区分 context 与 durable memory，Ch74 已写“模型输出只是 proposal”，Ch77 已写 deterministic spine。公开材料主要是 product/version evidence，暂未发现可独立沉淀的新内部机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；model、harness 与 platform attribution 已由 Ch62/74～77 覆盖。
- **Open Questions:** Anthropic 是否公开过 file-memory write/retention policy、parallel tool conflict contract 与可复现 agent harness artifact。

### User-level differential privacy for LLM fine-tuning

- **Candidate / Week / Score:** User-level differential privacy for LLM fine-tuning / 2025-W21 / 23/30。
- **Source Family ID:** `GOOGLE-ULDP-2407.07737`。
- **Source Type:** 2024 primary research paper + 2025 Google Research follow-up。
- **First-public Date / Revision History:** 论文 arXiv v1 首发 2024-07-10；Google Research 于 2025-05-23 再解释该工作。此前将 2025 Blog 日期写成技术 first-public date 不准确，本次已纠正。
- **Direct Primary Sources:** arXiv:2407.07737 全文；Google Research 2025 follow-up；论文公开 accounting/software references。
- **Related Primary Sources:** 并行工作 arXiv:2406.14322 用于 related-work 边界，不混并实验结论。
- **Access and Verification Status:** Verified。论文 HTML、公式、appendices 与实验 setup 可访问；真实部署 attack audit 与非英语/多模态数据未覆盖。
- **Full-read Coverage:** 已阅读 metadata、Introduction、ELS/ULS algorithms、tight accounting、variance analysis、synthetic mean estimation、LM setup/results、related work、discussion、privacy-attack说明及 A–G appendices（accounting implementation、datasets、group-size heuristic、sensitivity/personalization）。
- **Original Problem:** record-level adjacency只限制一条 example 的影响；用户贡献多条高度相关记录时，不能表达“移除一个用户全部数据”的保护语义。
- **Why the Previous Design Was Reasonable:** example-level sampling/clipping易于向量化，且在用户贡献少、样本近似独立或 privacy target 本来就是 record 时，计算更直接。
- **Changed Constraint:** assistant/chat/email 等数据天然按 user 聚集、贡献数不均且存在 within-user correlation；同时 LLM fine-tuning 受固定 accelerator budget 限制。
- **Mechanism:** ELS 从每用户最多 `G_ELS` 条记录组成 pooled dataset，做 example sampling/clipping，再通过 tight accountant提升到 user-level guarantee；ULS 先采样用户，对每个用户最多 `G_ULS` 条 example gradient 求平均，再做 per-user clipping/noise。选择 `(G_ULS, cohort M)` 本身是 compute–noise trade-off。
- **State Ownership:** privacy ledger/accountant 属于 training control plane；user grouping与contribution bounds属于dataset governance；optimizer只消费已经裁剪/加噪的aggregate，不能自行推断用户身份。
- **Control Flow / Data Flow:** user-partitioned dataset → user/example sampling → bounded group contribution → per-example or per-user gradient → clipping → Gaussian noise → optimizer；privacy parameters与sampling schedule共同进入accounting。
- **Implementation Details:** model 用 Praxis，ELS 用 JAX/tf.data，ULS 用 Dataset Grouper + FAX并行化，实验运行于 PAX；论文给出 dp_accounting 实现与 Estimate-and-Double heuristic。
- **Evaluation Setup:** C4-minus 预训练 400k steps、batch 512；Stack Overflow fine-tune 10k steps、CC-News 2k steps；TPU v3 `4x4/8x8/16x16` slices；Stack Overflow 与按 base-domain 分组的 CC-News；`delta=n^-1.1`，多组 epsilon/compute budgets。
- **Baselines / Ablations / Sensitivity:** 比较 ELS、ULS 与 no fine-tuning；扫描 group/cohort size、epsilon、compute budget、用户数 accounting 假设，并有 personalization 与 heuristic validation。没有真实 production attack benchmark。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TPU topology、预训练 batch 与 steps披露；模型规模/precision/sequence length/online concurrency/SLO未完整披露，因此 utility 结论不外推到任意 LLM。
- **What the Evidence Actually Proves:** 在论文的两个 user-partitioned text dataset 与固定 compute budget 下，ULS在强 privacy、较大 compute 或 within-user gradient diversity较高时通常优于ELS；tight accountant让ELS/ULS可公平比较。
- **What It Does Not Prove:** 不证明ULS总优于ELS，不证明形式DP自动抵抗所有实现/side-channel攻击，也不证明domain-based CC-News grouping等于真实用户。
- **Limitations / Threats to Validity:** CC-News用domain代理user且accounting假设用户数可放大10倍；仅两个text datasets；模型/序列细节不全；shuffle实现与理论subsampling存在implementation boundary；hyperparameter tuning影响utility。
- **Trade-offs / New Failure Modes:** user-level语义更强，却要求可靠identity/grouping、贡献上限、per-user compute sharding与ledger composition；共享账号、设备迁移、跨产品identity会让adjacency错误。
- **Where the Previous Design Still Applies:** record-level threat model、单记录用户、用户边界不可信或compute极紧时，ELS仍可能更合适；论文也明确存在ELS胜出的设置。
- **Evolution Relationship:** `Direct Evolution`：record privacy unit → user privacy unit；与 inference-time privacy filter 是 `Layering / Dependency`，两者不替代。
- **ROADMAP Node:** Ch25、Ch62、Ch68。
- **Target and Adjacent Chapters Read:** 已阅读 Ch25、Ch62、Ch67～69；Ch68 当前已有 privacy unit、grouping、clipping/noise/accounting 与 composition 论证。
- **Existing Coverage:** Ch68 已准确吸收“先定义 privacy unit 再选机制”及 user grouping/ledger 边界；最终复核未把单篇实验中的 `G` 与 cohort `M` 写成通用配方。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch68，明确 user adjacency、clipping、accounting 与 utility。
- **Changed Files or Rejection Reason:** 已复核 `books/part-05-ai-infrastructure/68-security.md`。
- **Open Questions:** 项目平台怎样定义跨workspace/shared-account adjacency；privacy ledger如何与data deletion、retraining和跨run composition对齐。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- llm-d community launch → 第 48、49、51、52、57、58 章（Direct Evolution）
- Claude 4 → 第 52、62、73～77 章（Direct Evolution）
- User-level differential privacy for LLM fine-tuning → 第 25、62、68 章（Direct Evolution）

## Recommended Action

- llm-d community launch：Must Read；与 KServe/Gateway/Dynamo 建立边界
- Claude 4：Worth Watching；与 Memory/Tool章节交叉审查
- User-level differential privacy for LLM fine-tuning：Must Read；与 W12 inference-time DP 形成层次关系

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W21/README.md。
- 更新 books/part-05-ai-infrastructure/68-security.md。

## Open Questions

- llm-d 各控制面组件的 freshness、ownership 与故障语义继续由后续 release evidence 约束。
- Claude 4 未公开足以推导训练或 runtime 机制的材料。
- user-level adjacency 在共享账户、跨设备与长期贡献场景中的定义仍需业务 threat model。

## Sources

- llm-d community launch — https://developers.redhat.com/articles/2025/05/20/llm-d-kubernetes-native-distributed-inferencing（First Public: 2025-05-20；Accessed: 2026-07-31）
- Claude 4 — https://www.anthropic.com/news/claude-4（First Public: 2025-05-22；Accessed: 2026-07-31）
- User-level differential privacy for LLM fine-tuning — https://research.google/blog/fine-tuning-llms-with-user-level-differential-privacy/（First Public: 2025-05-23；Accessed: 2026-07-31）
