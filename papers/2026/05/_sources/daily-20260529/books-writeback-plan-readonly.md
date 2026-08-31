# 2026-05-29 Books 串行写回计划（只读挑战）

> Status: `Ready for root reconciliation; no Books or Gate mutation performed`
>
> Input denominator: `BOOKS_WRITEBACK_QUEUE.json` 的 21 个 Source Family。
>
> Review basis: 21/21 exact-v1 packet、当前 owner 与相邻章节、ROADMAP Stable Node、现有正文主线。

## 审计结论

原 queue 的 21 个 `Integrate` 不能原样写入。当前 Books 已经吸收了一部分相同机制，另有两个 family 不构成 AI System Books 的长期增量，三个 family 的 canonical owner 错位。只读挑战后的建议真值为：

- `Integrate`: 13
- `No Change — Existing Coverage`: 6
- `Weekly Only — Context`: 2
- `Blocked / Unverified`: 0

本文件只给串行 writer 提供计划，不修改 canonical queue、Daily README 或 Books Gate；root 应先把下表的 disposition / owner 修正同步到 canonical date-local artifacts，再开始共享 Books 写回。

## Queue 修正清单

| Source Family | 建议处置 | 修正理由 |
| --- | --- | --- |
| `arXiv:2605.29253v1` / `SF-2026-ARXIV-2605-29253` | No Change | Ch66 已明确把 Agent final outcome、trajectory、process、recoverability 与 cross-layer attribution 分开；OpenClawBench 的 taxonomy 和作者数值是受限实例，不再改变长期 contract。 |
| `arXiv:2605.29313v1` / `SF-2026-ARXIV-2605-29313` | No Change | Ch82 的 `Message 不是 State` 与 `Coordination State 必须有显式 Owner 与 Commit Transition` 已覆盖 schema validation、role write contract、transactional commit 与 audit；PatchBoard 是实现实例。 |
| `arXiv:2605.29341v1` / `SF-2026-ARXIV-2605-29341` | No Change | Ch77 已分别拥有 write、maintenance/consolidation、retrieval、use/evaluation，并已有 intervention matrix；四阶段 benchmark 不产生新的 owner 或控制权。 |
| `arXiv:2605.29640v1` / `SF-2026-ARXIV-2605-29640` | No Change | Ch77 已覆盖 event/entity、bitemporal state、summary/derived view、temporal index、correction/delete/rebuild；VikingMem 的产品化组合不应重复进入正文。 |
| `arXiv:2605.30102v1` / `SF-2026-ARXIV-2605-30102` | No Change | Ch82 已有 `Device–Cloud 协同是逐步路由，而不是静态部署选择`，包括状态、成本、隐私、网络、Pareto 与固定端侧 fallback；论文的 PEVR/EVA 是受限架构实例。若保留 evidence trace，owner 应是 `AGENT-MULTI-AGENT`，不是 `AGENT-PLATFORM`。 |
| `arXiv:2605.30294v1` / `SF-2026-ARXIV-2605-30294` | Weekly Only | RaFI 是 CUDA/MPI 的一般 ray/work forwarding library，支持 rendering、particle advection 等数据并行程序；它不改变 neural-network Pipeline Parallel 的 layer partition、micro-batch、weight-version 或 optimizer contract，`TRAIN-PIPELINE-PARALLEL` 为误路由。 |
| `arXiv:2605.30406v1` / `SF-2026-ARXIV-2605-30406` | Weekly Only | exact-v1 给出 catastrophic LOC 的政策 taxonomy 与处置类别，但 Detection/Verification 明确 out of scope，且没有实验或可执行 implementation；不足以改变 Ch72 当前 security control contract。 |
| `arXiv:2605.30571v1` / `SF-2026-ARXIV-2605-30571` | No Change | 论文的 durable delta 是 batch-1 Decode 中 kernel-launch/runtime overhead 会使峰值 HBM bandwidth 失去预测力；canonical owner 应是 `INFER-DECODE` / `INFER-TENSORRT-LLM`，不是 Embodied VLA。Ch44 已解释 batch-1 launch overhead 与 CUDA Graph，Ch49 已拥有 fusion/kernel/runtime realization，因此不再追加。 |

Owner 必须修正但仍保留 `Integrate` 的两项：

- `SF-2026-ARXIV-2605-30218`: `INFER-TENSORRT-LLM` → `INFER-CONTINUOUS-BATCHING`（Ch46）；核心是 dynamic batch 改变 reduction path 后的 selective determinism、verifier work 与 KV commit，不是通用 kernel compilation。
- `SF-2026-ARXIV-2605-30613`: `INFER-KV-CACHE` → `PLATFORM-MULTI-TENANT`（Ch71）；核心是 gateway credential / tenant domain 折叠后 prompt-cache isolation 失效，Ch45 只提供 cache state handoff，Ch72 提供安全边界。

## 串行写回分组

建议按 owner 合并为 10 个正文小组，而不是生成 13 个论文段落：

1. Ch77: `2605.29324`、`2605.29463`、`2605.30690`
2. Ch72: `2605.29359`、`2605.30521`
3. Ch78: `2605.29561`
4. Ch38: `2605.29664`
5. Ch66: `2605.29786`
6. Ch70: `2605.30040`
7. Ch46: `2605.30218`
8. Ch25: `2605.30263`
9. Ch82: `2605.30335`
10. Ch71: `2605.30613`

每个 Source Family 保留唯一 marker，但同一 owner 内应先写连贯演进，再把多个 marker 放进同一语义单元；所有正文必须位于 `## 小结`、`## Review notes` 之前。

## 逐项写回计划

### `SF-2026-ARXIV-2605-29324` — STAMP

- **Canonical owner / adjacent**: `AGENT-MEMORY`，`books/part-07-agent/77-memory.md`；相邻 Ch76 RAG、Ch78 Tool Calling。
- **Target H2 / anchor**: `## 评估 Memory`，放在 `### 用干预矩阵定位写入、检索与阅读失败` 之前；marker `<!-- source-family:SF-2026-ARXIV-2605-29324 -->`。
- **演进主线**: 静态 action trajectory 只教“做什么”且无法验证“何时记住什么” → 在可控虚拟环境中把 memory variable、写入时点和回读时点变成 environment-owned ground truth → 生成可验证 SFT trajectory，并允许 RL reward 读取真实环境状态。
- **State / control owner**: environment generator 拥有 hidden memory variable 与验证时钟；memory policy 只提出 encode/retrieve；training loop 消费 verifier reward，不能把模型自述升级为真值。
- **收益、代价与 failure**: 获得可定位、可扩展的 memory supervision；代价是 simulator/task synthesis、状态泄漏与 synthetic-to-real gap。模型可能学习模板或 hidden-variable shortcut。
- **Fallback / coexistence**: 真实交互日志、人工标注与 static benchmark 在环境无法忠实模拟时继续成立；高风险事实仍需 authoritative source。
- **Exact-v1 boundary**: 仅接受 `arXiv:2605.29324v1` §3.3–3.5、§4 和 §6 所披露的 mobile-GUI / Memory-World、SFT/RL 设置；不外推真实手机、开放任务或长期生产可靠性。

### `SF-2026-ARXIV-2605-29359` — Distributed Training Compute Governance

- **Canonical owner / adjacent**: `PLATFORM-SECURITY`，`books/part-06-ai-infrastructure/72-security.md`；相邻 Ch71 Multi Tenant、Ch73 Production。
- **Target H2 / anchor**: H2 `## Prompt Injection 与 Tool Boundary` 内，在 `### 从 Host-local Sensor 到独立基础设施安全面` 之后、`#### 缺失证据必须传播为 Unknown` 之前。
- **演进主线**: 以单一大型 cluster / site 作为 compute-governance observation unit 在集中训练时代合理 → 低频同步和 pipeline-parallel DiLoCo 使训练可以跨许多阈值以下节点聚合 → detection contract 必须从 host/cluster 扩展为跨节点、跨时间、跨供应链的 aggregate training lineage。
- **State / control owner**: governance evidence plane 拥有 chip/cluster identity、memory/compute threshold、registration 与 correlated activity ledger；网络或单 host sensor 只能提供 signal，不能独自判定违规。
- **收益、代价与 failure**: 缩小拆分集群规避的盲区；代价是跨域身份关联、隐私、误报、长期 retention 与执法依赖。Bandwidth monitoring 单点会被规避，模型外推也可能夸大可行性。
- **Fallback / coexistence**: 集中训练仍可用 cluster registration、site inspection 与传统 accounting；证据不足时输出 unknown / escalation，而不是虚假 all-clear。
- **Exact-v1 boundary**: 仅接受 `arXiv:2605.29359v1` §3 threat model/efficiency model、§4 simulated results、§5.1 assumptions 与 §5.3 countermeasures；不把 Llama-405B 规模外推、成本估计或政策建议当作生产检测证明。

### `SF-2026-ARXIV-2605-29463` — Memory Confabulation

- **Canonical owner / adjacent**: `AGENT-MEMORY` Ch77；相邻 Ch76、Ch78。
- **Target H2 / anchor**: `## Memory Write 是高风险决策`，接在现有 write pipeline 与 typed transition 之后。
- **演进主线**: Reflexion 把模型自诊断直接写成 procedural memory，在简单 trial reuse 中低成本 → 错误 diagnosis 会跨 trial 冻结并自我强化 → write admission 应优先消费 trajectory-level programmatic failure receipt，reflection 只能成为待验证 candidate。
- **State / control owner**: environment/tool trace 拥有 observed failure；extractor 生成 structured signal；memory writer 决定 pending/accept；模型 reflection 不拥有事实 commit。
- **收益、代价与 failure**: 减少 confident-but-wrong memory 的循环放大；代价是 domain-specific extractor、漏检和额外 trace storage。RRR 只能发现重复依赖，不证明每次反思都错误。
- **Fallback / coexistence**: 低风险、无 executable verifier 的开放任务仍可保留反思，但必须带 provenance/expiry，并允许 raw trajectory 回读与人工纠正。
- **Exact-v1 boundary**: `arXiv:2605.29463v1` §3.1–3.3、§4、§5 与 §6.4；结果只属于 ALFWorld/HumanEval 与论文 extractor，不证明通用 Reflexion failure rate。

### `SF-2026-ARXIV-2605-29561` — ParaTool

- **Canonical owner / adjacent**: `AGENT-TOOL-CALLING` Ch78；相邻 Ch77 Memory、Ch79 Planning。
- **Target H2 / anchor**: `## Tool Discovery 与选择`，在 `### Interface Granularity` 前增加“Tool representation 从 Context 移到可加载参数”的分支。
- **演进主线**: 完整 tool schema/examples 放入 Context 可审计且容易更新，但 tool 数增长后 token、混淆与 hallucination pressure 上升 → 每个 tool 编译为独立参数模块，由 gate 软选择与组合 → runtime Context 成本下降，但 tool identity 从可见文档转为 parameter artifact。
- **State / control owner**: registry/model loader 拥有 module identity/version；gating network 只提出组合；executor 仍拥有 schema validation、authorization 与 effect commit。
- **收益、代价与 failure**: 减少长 catalog Context 和重复 encoding；代价是预训练/存储/加载、gate routing error、参数冲突、更新和撤销不透明。参数模块不能替代最新 schema 或权限。
- **Fallback / coexistence**: 高频稳定工具可参数化；低频、快速变化、高风险工具继续使用显式 schema retrieval 与 typed runtime validation。
- **Exact-v1 boundary**: `arXiv:2605.29561v1` §3.3–3.7、§4 与 Limitations；Stable ToolBench/BFCL 结果不证明开放工具、动态版本或生产副作用安全。

### `SF-2026-ARXIV-2605-29664` — AMDP

- **Canonical owner / adjacent**: `TRAIN-PIPELINE-PARALLEL` Ch38；相邻 Ch37 TP、Ch39 ZeRO。
- **Target H2 / anchor**: `## 异步 Pipeline：去掉 Bubble 会把成本移到参数版本`，接在既有 fixed-delay / correction 分支之后。
- **演进主线**: 同步 1F1B 以 bubble 换参数版本清晰 → 完全异步提高利用率却放大 forward/backward mismatch → AMDP 限制首 stage 在 backward 前最多推进两个 minibatch，并以多条反向 pipeline 填补 bubble、gradient accumulation 在单次 update 提交。
- **State / control owner**: scheduler 拥有 multi-directional pipeline 与 minibatch readiness；optimizer owner 定义 update boundary；每个 microbatch receipt 记录 forward/backward weight version。
- **收益、代价与 failure**: 在论文模型/集群中提高利用率并保持收敛；代价是多 pipeline state、activation/queue memory、schedule complexity 与 mismatch assumptions。深度、模型或网络变化可能破坏上界。
- **Fallback / coexistence**: 版本一致性、恢复或内存优先时继续使用同步 1F1B；收敛或 mismatch receipt 异常时回退同步 schedule。
- **Exact-v1 boundary**: `arXiv:2605.29664v1` §3.1–3.4、§4、Appendix B；只支持论文 GPT/BERT、硬件与训练预算，不把模拟/局部吞吐外推任意集群。

### `SF-2026-ARXIV-2605-29786` — Croissant Tasks

- **Canonical owner / adjacent**: `PLATFORM-EVALUATION-SYSTEM` Ch66；相邻 Ch65 Scheduler、Ch67 Monitoring。
- **Target H2 / anchor**: H2 `## 工程实践：从最小可信闭环开始` 内的 `### Evaluation Object 必须携带依赖图、时间与可复现条件`，在现有 artifact/reproduction 论证中加入 declarative Task Contract。
- **演进主线**: 保存 source code/environment 能重跑同一实现，但依赖脆弱且把 problem 与 solution 混合 → machine-actionable metadata 分开 task problem、resources、metrics、execution contract 与 candidate solution → 独立实现可以验证概念性可复现，而不是只重放旧代码。
- **State / control owner**: benchmark owner 版本化 task specification；implementation agent 只生成 candidate；harness/verifier 拥有执行与结果 acceptance。
- **收益、代价与 failure**: 提高跨实现、跨时间复现性；代价是 schema expressiveness、自动抽取错误、环境细节遗漏与 verifier 同源偏差。
- **Fallback / coexistence**: reference code/container 继续作为 regression baseline；无法完整声明的任务保留原 artifact 和人工复核。
- **Exact-v1 boundary**: `arXiv:2605.29786v1` §3 vocabulary、§4 empirical validation、§5.2 limitations；agent-generated reproduction 成功不证明语义等价、schema 完备或任意 benchmark 可自动迁移。

### `SF-2026-ARXIV-2605-30040` — Token Inflation Billing Audit

- **Canonical owner / adjacent**: `PLATFORM-COST` Ch70；相邻 Ch69 Trace、Ch71 Multi Tenant。
- **Target H2 / anchor**: `## Showback、Chargeback 与公平`，在共享资源归因后加入“meter evidence 不能由被计费方单独拥有”。
- **演进主线**: provider-reported token count 在透明 tokenizer/执行路径中足够便宜 → hosted reasoning 隐藏 model、tokenizer 与 reasoning trace 后，audit 退化为检查 provider 自己生成的 evidence → billing meter 必须绑定 provider 不能单独操纵的 execution evidence。
- **State / control owner**: usage meter 生成 token/work receipt；billing service 聚合；tenant/auditor 验证 attestation/proof/third-party replay；provider 不能同时拥有计量、证据与最终结算。
- **收益、代价与 failure**: 降低 token inflation 与 disputed billing；代价是 TEE/cryptographic proof/re-execution 成本、隐私、tokenizer disclosure 和 streaming proof lifecycle。Attestation 证明执行身份，不证明模型质量或价格公平。
- **Fallback / coexistence**: 低风险内部服务可用透明 tokenizer + sampled replay；无法独立验证时将账单标为 provider-asserted 并保留争议/上限机制。
- **Exact-v1 boundary**: `arXiv:2605.30040v1` §2、§3–5 与 Appendix A；攻击幅度只属于三类审计框架及其模型/数据，不外推所有 provider 或账单。

### `SF-2026-ARXIV-2605-30218` — MarginGate

- **Canonical owner / adjacent**: **修正为** `INFER-CONTINUOUS-BATCHING` Ch46；相邻 Ch45 KV Cache、Ch47 PagedAttention。
- **Target H2 / anchor**: `## Selective Determinism：把 Verify 变成第三类 Iteration Work`，作为现有 window verifier 的 margin-triggered policy 分支，而非另建论文段。
- **演进主线**: 固定 batch / batch-invariant kernel 保证确定性但对全部 token 征税 → always-on per-token verifier 仍昂贵 → 用 top-1/top-2 margin 触发低 margin step 的 reference verification，确认 mismatch 后连同当前 KV column 一起修复。
- **State / control owner**: fast path 只产生 private candidate token/KV；calibrated trigger 提出 verify；reference verifier 拥有 commit token 与 KV；scheduler 计入 verifier work 和 tail SLO。
- **收益、代价与 failure**: 在论文 flip-sparse 条件下降低 verifier 触发；代价是校准 drift、near-tie recall、额外 reference path 与 mismatch tail。高 margin 不等于数值正确。
- **Fallback / coexistence**: 审计/CI、flip 稠密、quantized/MoE 或 calibration OOD 时回退 always-on verification、batch-invariant kernel 或固定 batch。
- **Exact-v1 boundary**: `arXiv:2605.30218v1` §2、§3.1–3.3、§4、§5 与 Limitations；只支持所测五模型、数据、BF16 与 batching 实现，不证明跨 kernel/hardware bitwise determinism。

### `SF-2026-ARXIV-2605-30263` — minWM

- **Canonical owner / adjacent**: `MULTIMODAL-WORLD-MODELS` Ch25；相邻 Ch24 Generative Paradigms、Ch26 Embodied VLA。
- **Target H2 / anchor**: H2 `## Memory 架构为何从静态 cache 演进` 内，在 `### 从全历史条件到有界 History Bank 与 Self-rollout Distillation` 前补“从 bidirectional video generator 到 causal interactive rollout”的转换链。
- **演进主线**: bidirectional diffusion 适合离线整段视频质量，却不能直接承担 causal、camera-conditioned、low-latency transition → camera-control fine-tuning → AR diffusion training → causal ODE/consistency distillation 与 asymmetric DMD → few-step streaming rollout。
- **State / control owner**: action/camera schema 与 causal history 由 world-model runtime 版本化；diffusion backbone 只生成 transition proposal；真实 observation/controller verifier 仍拥有环境事实与 action commit。
- **收益、代价与 failure**: 复用开放 video backbone 并缩短 rollout；代价是 teacher/student mismatch、few-step quality、self-rollout drift、camera-control coverage 与 architecture-specific recipe。
- **Fallback / coexistence**: 非交互视频继续使用 bidirectional generator；安全关键 planning 回退 domain simulator/short-horizon closed-loop correction。
- **Exact-v1 boundary**: `arXiv:2605.30263v1` §2.1–2.2、§3、§4；只支持 Wan2.1/HY1.5 等披露 backbone、camera data 与 latency recipe，不证明物理因果、planner utility 或 real-world safety。

### `SF-2026-ARXIV-2605-30335` — Compositional Incoherence

- **Canonical owner / adjacent**: `AGENT-MULTI-AGENT` Ch82；相邻 Ch81 Workflow、Ch83 MCP。
- **Target H2 / anchor**: `## Verification 与 Aggregation`，在 aggregation 不能由局部正确推出整体正确的主线中加入 runtime coherence gate。
- **演进主线**: 每个 component 单独校准在独立问题中合理 → partial evidence 与 coupling constraints 组合后，局部 coherent quote 仍可能没有任何 joint distribution → 计算 compositional residual，超阈值时以 hierarchical projection 修复或拒绝 commit，并用 sequential monitor 跟踪 drift。
- **State / control owner**: components 拥有局部 proposal；aggregator 保存 cross-component constraint graph；deterministic projector/verifier 拥有 coherent composition；decision owner 再消费修复后结果。
- **收益、代价与 failure**: 获得可计算的 group-level invariant；代价是必须显式声明 coupling、projection cost 与过度修复。约束图错误时残差和 repair 同样错误。
- **Fallback / coexistence**: product-structure / independent tasks 可继续局部 aggregation；无法定义 joint constraint 时保留 dissent、人工审查或单 Agent baseline。
- **Exact-v1 boundary**: `arXiv:2605.30335v1` §3、§4–5、§6 与 Appendix M；实验只覆盖论文 forecasting panels/relations，不证明开放 Agent workflow 的通用发生率或收益。

### `SF-2026-ARXIV-2605-30521` — Mock Tool-call Quarantine Counterevidence

- **Canonical owner / adjacent**: `PLATFORM-SECURITY` Ch72；相邻 Ch71 Multi Tenant、Ch73 Production。
- **Target H2 / anchor**: H2 `## 风险管理而不是一次性认证` 内的 `### Instruction Hierarchy 必须携带 Authenticated Provenance`，紧接固定 role priority 不构成安全边界的论证。
- **演进主线**: 把 untrusted text 放进较低优先级的 mock Tool Result 看似利用 instruction hierarchy 隔离输入 → role wrapper 仍是同一模型语言通道，部分任务甚至出现 hierarchy inversion → untrusted-input isolation 必须依赖 authenticated provenance、typed data boundary 与独立 policy/reference monitor。
- **State / control owner**: wrapper 只能标注 channel；policy engine 认证 origin/trust；judge/model 输出仍是 sensor；高风险 action 由 executor commit。
- **收益、代价与 failure**: 避免把 prompt formatting 误当隔离；更强 primitive 增加 parsing、schema、false reject 和模型训练成本。Red-team 未命中不等于安全。
- **Fallback / coexistence**: mock tool wrapping 可保留为 defense-in-depth / prompt hygiene，但不能获得授权或 release Gate；失败时 sandbox、拒绝或人工升级。
- **Exact-v1 boundary**: `arXiv:2605.30521v1` §2、§3、§4 与 §6；七模型、三 judge tasks、static attacks 不证明任意模型/动态攻击必然 inversion。

### `SF-2026-ARXIV-2605-30613` — CacheProbe

- **Canonical owner / adjacent**: **修正为** `PLATFORM-MULTI-TENANT` Ch71；相邻 Ch70 Cost、Ch72 Security；Ch45 KV Cache 只作状态机制 handoff。
- **Target H2 / anchor**: `## Serving 与 Cache 隔离`，在 cache key / tenant policy domain 之后加入 gateway identity collapse。
- **演进主线**: provider 以 account/org namespace 隔离 prompt cache 在直连调用中合理 → gateway 复用 provider credential、路由 metadata 或默认模式后，多个 gateway user 可能落入同一 provider cache domain → isolation identity 必须端到端绑定 external principal、gateway account、provider account、BYOK mode、model/revision 与 cache policy。
- **State / control owner**: gateway identity translator 和 provider cache owner共同定义 isolation key；tenant policy 决定共享；timing/metadata probe 只是审计 sensor，不拥有泄漏判决。
- **收益、代价与 failure**: 保留租户内复用并检测跨租户共享；代价是命名空间碎片、命中率下降、统计噪声、cache load/time drift 与 provider 不透明。
- **Fallback / coexistence**: 敏感租户禁用跨租户 prompt cache、使用独立 provider credential/pool 或 full recompute；普通单租户缓存继续成立。
- **Exact-v1 boundary**: `arXiv:2605.30613v1` §III–VI、§VII-C/D；仅覆盖三 provider、随机 prompts 与论文阈值，metadata/timing 差异不证明所有请求内容可恢复。

### `SF-2026-ARXIV-2605-30690` — ElasticMem

- **Canonical owner / adjacent**: `AGENT-MEMORY` Ch77；相邻 Ch76 RAG、Ch78 Tool Calling。
- **Target H2 / anchor**: `### 从固定记忆参数到可扩展 Expert Pool` 后，扩展为 query-conditioned elastic latent budget；不要把 latent state 写成事实库。
- **演进主线**: text retrieval 用 token Context 换可见性，fixed latent memory 减少 token 却固定容量 → hidden-state query 检索 latent bank → policy 为每条 memory 分配可变 latent budget → soft tokens 注入 generation，downstream reward 优化资源分配。
- **State / control owner**: external bank 保存 key/content/version；retriever 和 budget policy只分配读预算；reasoner 消费 soft state；事实 authority 仍由 provenance/evidence owner 持有。
- **收益、代价与 failure**: 按 query utility 分配容量并降低显式 token；代价是 latent 不可解释、budget collapse、reward hacking、retrieval/bank drift 与额外训练。相似度之外的 utility 也不等于 truth。
- **Fallback / coexistence**: 高风险事实、需要引用/删除/人工审计时回退 text memory/raw evidence；低风险重复任务可使用 latent fast path。
- **Exact-v1 boundary**: `arXiv:2605.30690v1` §3.2–3.6、§4、Appendix A/B；MemorySuite 与 Qwen2.5 结果不证明跨模型、长期更新、删除或安全审计能力。

## Writer 机器与语义验收

串行 writer 完成后应至少验证：

1. 13/13 confirmed Integrate family 各有一个且仅一个正文 marker；8 个降级 family 不新增 marker。
2. marker 位于目标 H2 内，并满足 `marker < ## 小结 < ## Review notes`。
3. `2605.30218` 只写 Ch46，`2605.30613` 只写 Ch71；Ch45/Ch72 仅通过正文 handoff，不复制 owner 机制。
4. 每个 family 的正文同时包含旧方案合理性、changed constraint、state/control owner、收益、trade-off、failure、fallback/coexistence 与 source-specific exact-v1 non-proof boundary。
5. 同一 owner 的 family 形成一条演进链；删除论文名后正文仍成立。
6. writer 不关闭 Books Gate；由不同 reviewer 完成 owner+adjacent post-write semantic audit 后再同步 05-29 Gate。
