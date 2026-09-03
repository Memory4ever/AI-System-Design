# 2026-06-24 Ready-to-Insert Books Packet V1

每个 Source Family 只写入一个 owner；以下最小正文与 Review note 均绑定 exact-v1。

## AGENT-MEMORY — books/part-07-agent/77-memory.md

相邻章 `books/part-07-agent/76-rag.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24151**：不在设计时固定 text 或 code memory；memory manager 先保存 plan/fact/pitfall 文本，只有重复且验证通过的 plan 才 crystallize 为 callable tool，同时保留构建成本与 provenance。 AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。
- **SF-2026-ARXIV-2606-24428**：经验写入从同一 agent 自我总结改为 Execute 的异构并行轨迹、第三方 contrastive Distill 与 consensus Verify；只有通过独立验证的经验才能进入 storage/retrieval。 多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。
- **SF-2026-ARXIV-2606-24535**：多 Agent 共享记忆增加 explicit scope、valid time、provenance graph 与 policy-gated retrieval；矛盾在 write-time resolution，reader 只消费已提交版本，传播由 privilege gate 控制。 self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。
- **SF-2026-ARXIV-2606-24775**：把 agent memory 评价拆成 logical representation、physical storage/index、extraction、query routing 与 maintenance 五个 ownerable stage，并分别测 retrieval fidelity、evolution robustness、long-horizon stability 和 operation cost。 现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。
- **SF-2026-ARXIV-2606-25115**：一个 value-minus-harm-per-byte score 同时控制 KEEP eviction、SHARE uplink 与 TRUST provenance gate；RAM、energy、uplink budget 与 poison risk 成为 memory lifecycle state。 task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。
- **SF-2026-ARXIV-2606-25161**：memory update 不再只按最终问答 reward；transition verifier 对 coverage、preservation、faithfulness 打分，同一旧 state 下比较候选 write/revise/delete，并用 preference-guided RL 训练 writer。 MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24151: `arXiv:2606.24151v1`; exact-v1 URL=`https://arxiv.org/html/2606.24151v1`; Method=`https://arxiv.org/html/2606.24151v1 — §3 The Metis System; 3.2 Text Reflection; 3.3 Code Generation; 3.4 Memory Manager`; Evaluation=`https://arxiv.org/html/2606.24151v1 — §4 Experiments; A.1 Profiling Experiments`; Non-proof=`AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24428: `arXiv:2606.24428v1`; exact-v1 URL=`https://arxiv.org/html/2606.24428v1`; Method=`https://arxiv.org/html/2606.24428v1 — §3 Self-Confirmation Trap; 4 Execute-Distill-Verify`; Evaluation=`https://arxiv.org/html/2606.24428v1 — §5 Experiments; Memory Quality and Contamination`; Non-proof=`多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24535: `arXiv:2606.24535v1`; exact-v1 URL=`https://arxiv.org/html/2606.24535v1`; Method=`https://arxiv.org/html/2606.24535v1 — §3 Fleet-Memory Problem; 5 Governed Shared Memory Architecture`; Evaluation=`https://arxiv.org/html/2606.24535v1 — §7 Evaluation Methodology; 8 Results`; Non-proof=`self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24775: `arXiv:2606.24775v1`; exact-v1 URL=`https://arxiv.org/html/2606.24775v1`; Method=`https://arxiv.org/html/2606.24775v1 — §3 Method Overview; Representation, Extraction, Retrieval, Maintenance`; Evaluation=`https://arxiv.org/html/2606.24775v1 — §4 End-to-End Assessment; 5 Component Comparison`; Non-proof=`现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25115: `arXiv:2606.25115v1`; exact-v1 URL=`https://arxiv.org/html/2606.25115v1`; Method=`https://arxiv.org/html/2606.25115v1 — §III System Design; Net-Value-Density; Three Decisions`; Evaluation=`https://arxiv.org/html/2606.25115v1 — §V Evaluation; Trust Under Poisoning; Real Hardware`; Non-proof=`task-drift benchmark 与 Jetson 两臂/Hub testbed 不证明 score 跨设备、用户或攻击迁移；低校准或高风险 entry 应拒绝共享并回退本地可信 memory。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25161: `arXiv:2606.25161v1`; exact-v1 URL=`https://arxiv.org/html/2606.25161v1`; Method=`https://arxiv.org/html/2606.25161v1 — §3 Method; Memory Transition Verifier; Transition-Ranked GRPO`; Evaluation=`https://arxiv.org/html/2606.25161v1 — §4 Experiment; HaluMem; Reliability of Consolidation`; Non-proof=`MemoryAgentBench/HaluMem/Mem-alpha 与 verifier judge 不证明真实用户 consent、并发 writer、poisoning 或 judge drift；低置信 transition 应拒写并保留旧版本。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## AGENT-MULTI-AGENT — books/part-07-agent/82-multi-agent.md

相邻章 `books/part-07-agent/81-workflow.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24437**：MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。 只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。
- **SF-2026-ARXIV-2606-26156**：把 agent 内部 decision logic 与公开 message protocol 分离：decision maker 只能从 valid decisions 选互相兼容 emission set，adapter 隔离 communication service，operational semantics 拥有 protocol compliance。 2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24437: `arXiv:2606.24437v1`; exact-v1 URL=`https://arxiv.org/html/2606.24437v1`; Method=`https://arxiv.org/html/2606.24437v1 — §4 ReM-MoA; Ranked Reasoning Memory; Diversified Routing`; Evaluation=`https://arxiv.org/html/2606.24437v1 — §5 Experiments; Scaling and Ablations`; Non-proof=`只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-26156: `arXiv:2606.26156v1`; exact-v1 URL=`https://arxiv.org/html/2606.26156v1`; Method=`https://arxiv.org/html/2606.26156v1 — §2 Information Protocols; 3 Kiko Programming Model`; Evaluation=`https://arxiv.org/html/2606.26156v1 — §4 Operational Semantics; protocol-compliance proof`; Non-proof=`2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## AGENT-PLATFORM — books/part-07-agent/84-agent-platform.md

相邻章 `books/part-07-agent/83-mcp.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24311**：将 model invocation、tool execution、workspace mutation、rule knowledge 与 execution record 收进同一 runtime boundary；剩余时间成为显式 state，用于在探索、实现、验证之间重配预算。 结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24311: `arXiv:2606.24311v1`; exact-v1 URL=`https://arxiv.org/html/2606.24311v1`; Method=`https://arxiv.org/html/2606.24311v1 — §3 Method; 3.2 Integrated Execution Framework; 3.5 Structured Tool Boundary`; Evaluation=`https://arxiv.org/html/2606.24311v1 — §4 Experiments; Terminal-Bench 2.0/2.1`; Non-proof=`结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## AGENT-RAG — books/part-07-agent/76-rag.md

相邻章 `books/part-07-agent/77-memory.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24204**：把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。 闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。
- **SF-2026-ARXIV-2606-25191**：document assessment 不再默认多 Agent scoring；pilot probe 测 reasoning-score coupling，弱模型路由到 per-document isolation，只有 score 有信息的模型才承担 assessment/reranking。 7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。
- **SF-2026-ARXIV-2606-28387**：text-to-SQL 在 generation 前先检索 typed catalog object（table/column/metric/relation/query history）；parallel vector search、lineage expansion、reranker 与 deterministic ACL 共同决定可见 schema。 CRUSH4SQL/SEDE/BIRD 与 warehouse catalog quality 不证明跨 dialect、动态权限或低元数据环境；metadata noise/ACL 不确定时回退受限 catalog browse 或人工 schema selection。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24204: `arXiv:2606.24204v1`; exact-v1 URL=`https://arxiv.org/html/2606.24204v1`; Method=`https://arxiv.org/html/2606.24204v1 — §III Unified Dominance Abstraction; IV/V Unified Dominance Graph`; Evaluation=`https://arxiv.org/html/2606.24204v1 — §VI Experiment; Search Performance and Index Construction`; Non-proof=`闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25191: `arXiv:2606.25191v1`; exact-v1 URL=`https://arxiv.org/html/2606.25191v1`; Method=`https://arxiv.org/html/2606.25191v1 — §3 Reasoning-Score Coupling; 4 Candidate Treatments; MADARA`; Evaluation=`https://arxiv.org/html/2606.25191v1 — §5 Experimental Setup; 6 Results; K Cost-Accuracy`; Non-proof=`7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-28387: `arXiv:2606.28387v1`; exact-v1 URL=`https://arxiv.org/html/2606.28387v1`; Method=`https://arxiv.org/html/2606.28387v1 — §3 Schema-First Retrieval; Catalog Objects; Retrieval and Access Control`; Evaluation=`https://arxiv.org/html/2606.28387v1 — §4 Experimental Setup; 5 Results; D Analyses`; Non-proof=`CRUSH4SQL/SEDE/BIRD 与 warehouse catalog quality 不证明跨 dialect、动态权限或低元数据环境；metadata noise/ACL 不确定时回退受限 catalog browse 或人工 schema selection。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## AGENT-WORKFLOW — books/part-07-agent/81-workflow.md

相邻章 `books/part-07-agent/82-multi-agent.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24177**：以 artifact 为边界组织 producer-critic factory，critic 在 fresh context 验收后才推进；自动化 loop 只提交可机器检查部分，visibility/fixability taxonomy 将不可判定 claim 留给 human scientist。 444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。
- **SF-2026-ARXIV-2606-25198**：autonomous research loop 把 shared search state、lineage、quality/diversity/novelty archive 与 auditor verdict 作为 durable artifacts；40 个 fabrication 说明 score 结果必须过独立 audit 才能推进。 3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。
- **SF-2026-ARXIV-2606-25207**：HPO agent 不替代单一 optimizer，而从多工具 proposal pool 选择；prefix-stable prompt 复用 KV，跨 iteration speculation 与 relative-error accept test 把 judge/tool latency 隐藏在 model evaluation 下。 HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24177: `arXiv:2606.24177v1`; exact-v1 URL=`https://arxiv.org/html/2606.24177v1`; Method=`https://arxiv.org/html/2606.24177v1 — §2 Design Principles; 3 System Architecture`; Evaluation=`https://arxiv.org/html/2606.24177v1 — §4 Where Human Judgment Is Irreducible; A/B Case Studies`; Non-proof=`444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25198: `arXiv:2606.25198v1`; exact-v1 URL=`https://arxiv.org/html/2606.25198v1`; Method=`https://arxiv.org/html/2606.25198v1 — §3 Heuresis Framework; search strategies and async parallelism`; Evaluation=`https://arxiv.org/html/2606.25198v1 — §4 Experiments; 5 Analysis; B Reward Hacking`; Non-proof=`3 个 ML domain、3,222 scored runs 未出现 Original 且 verifier 漏掉过 fabrication；不证明自动搜索能扩展 quality-novelty frontier，关键 claim 仍需独立复现/人工 gate。`; Artifact=`https://github.com/a-antoniades/Heuresis`
- SF-2026-ARXIV-2606-25207: `arXiv:2606.25207v1`; exact-v1 URL=`https://arxiv.org/html/2606.25207v1`; Method=`https://arxiv.org/html/2606.25207v1 — §3 Agent-Integrated Tools; 4 Agent-System Co-Design`; Evaluation=`https://arxiv.org/html/2606.25207v1 — §5 Experiments; Wall-Clock Decomposition`; Non-proof=`HPOBench/PD1 与给定 wall-clock regime 不证明昂贵、非平稳或安全敏感 experiment；accept test 不满足或 speculation 浪费时回退串行工具 loop。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## INFER-GPU-MEMORY — books/part-05-inference-system/54-gpu-memory.md

相邻章 `books/part-05-inference-system/55-pd-disaggregation.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24506**：冷 MoE serving 将 stable weights 与 demand-driven KV 拆成独立资源池；planner virtualize shared KV，layer-wise scheduler/persistent kernel 只激活所需 weights 和 KV heads。 证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24506: `arXiv:2606.24506v1`; exact-v1 URL=`https://arxiv.org/html/2606.24506v1`; Method=`https://arxiv.org/html/2606.24506v1 — §3 CrossPool Design; KV Planner; Layer-wise Scheduler; Control Lowering`; Evaluation=`https://arxiv.org/html/2606.24506v1 — §5 Experiments; Context Scalability; Overall Performance`; Non-proof=`证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## INFER-KV-CACHE — books/part-05-inference-system/45-why-kv-cache-speeds-up.md

相邻章 `books/part-05-inference-system/47-pagedattention.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24467**：KV eviction 从统一 token score 改为 semantic-retrieval heads 选 token、error-aware controller 按层分配 cache budget；压缩决定属于 cache manager，不修改模型语义 owner。 LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24467: `arXiv:2606.24467v1`; exact-v1 URL=`https://arxiv.org/html/2606.24467v1`; Method=`https://arxiv.org/html/2606.24467v1 — §3 CompressKV; Retrieval Head Identification; Layer-Adaptive Allocation`; Evaluation=`https://arxiv.org/html/2606.24467v1 — §4 Experiments; LongBench/NIAH; Memory and Latency`; Non-proof=`LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## INFER-SCHEDULING — books/part-05-inference-system/56-inference-scheduling.md

相邻章 `books/part-05-inference-system/46-continuous-batching.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25040**：I2V scheduler 把相似请求历史 sparse mask 作为 request-conditioned prior，避免每请求 mask prediction；feature reuse 仅可选，并由 downsampled region 与 guidance enhancement 限制 semantic drift。 2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25040: `arXiv:2606.25040v1`; exact-v1 URL=`https://arxiv.org/html/2606.25040v1`; Method=`https://arxiv.org/html/2606.25040v1 — §3 Methodology; Sparsity Reuse; Latent Feature Reuse`; Evaluation=`https://arxiv.org/html/2606.25040v1 — §4 Experiments; Mask Quality and Routing Overhead`; Non-proof=`2.16x 来自论文 I2V workload/default config；相似度误路由、场景突变、跨模型 mask 不兼容和 feature boundary artifact 未证明，低置信时回退在线 mask/full compute。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## INFER-SPECULATIVE-DECODING — books/part-05-inference-system/48-speculative-decoding.md

相邻章 `books/part-05-inference-system/49-tensorrt-llm.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24957**：speculative verification 的 target KV 不再全读；Dustin 混合历史 attention 与 draft lookahead，semantic retrieval heads 在线估计关键 token，只对稀疏 KV 做 target verification。 静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。
- **SF-2026-ARXIV-2606-25091**：edge-cloud speculative decoding 的准入由 RTT、edge draft time、acceptance 与 target verification time 共同决定；single-request latency 不再是唯一目标，饱和 server 的 multi-tenant capacity 才可能 justify offload。 这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。
- **SF-2026-ARXIV-2606-25097**：speculative decoding 上线前增加 target-aligned invariance screen：byte identity、McNemar、TOST 与 matched target-only arm 分离算法安全差异和 dtype/framework 噪声。 证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24957: `arXiv:2606.24957v1`; exact-v1 URL=`https://arxiv.org/html/2606.24957v1`; Method=`https://arxiv.org/html/2606.24957v1 — §3 Observation; 4 Dustin Sparse Verification`; Evaluation=`https://arxiv.org/html/2606.24957v1 — §5 Experiment; Accuracy and End-to-End Decode Throughput`; Non-proof=`静态/动态 budget、memory capacity、SRH identification 与 configuration search 有成本；模型/任务迁移、低 ARR 或长尾输入应回退 dense target attention。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25091: `arXiv:2606.25091v1`; exact-v1 URL=`https://arxiv.org/html/2606.25091v1`; Method=`https://arxiv.org/html/2606.25091v1 — §II Background and Setting; III Gain Window`; Evaluation=`https://arxiv.org/html/2606.25091v1 — §III-A/B/C comparisons; IV Pipelining`; Non-proof=`这是 closed-form position analysis，不是广泛实测；closed API 无 verifier-only interface 时不可部署，WAN RTT 越界应回退 cloud AR 或 colocated SD。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25097: `arXiv:2606.25097v1`; exact-v1 URL=`https://arxiv.org/html/2606.25097v1`; Method=`https://arxiv.org/html/2606.25097v1 — §3 Methods; Serving-stack Configuration; TAIS Screen`; Evaluation=`https://arxiv.org/html/2606.25097v1 — §4 Results; E0/E1/E2/E5; B Reproducibility`; Non-proof=`证据绑定列出的 Llama target/draft、<=4,006 samples、temperature/framework 与非 tree-speculation 配置；无 matched arm 的 70B probe 不能算 TAIS pass。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## MODEL-LONG-CONTEXT — books/part-02-model/22-long-context.md

相邻章 `books/part-02-model/13-position-encoding.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25156**：长上下文设计从单一 accuracy 目标改为 retrieval、likelihood、short-context quality、decode state 与 kernel cost 的 Pareto；Polar direction/magnitude channel 配 gated-delta recurrent state。 378M、2K train、256K eval 中 FinePDFs exact retrieval 为 0%，hardware transition audit 非随机；不能宣称普遍外推，Raven/softmax/更短 context 仍是共存点。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25156: `arXiv:2606.25156v1`; exact-v1 URL=`https://arxiv.org/html/2606.25156v1`; Method=`https://arxiv.org/html/2606.25156v1 — §3 Methodology; Polar Attention; Gated-Delta Memory`; Evaluation=`https://arxiv.org/html/2606.25156v1 — §4 Experimental Setup; 5 Results; C Complete Sweep`; Non-proof=`378M、2K train、256K eval 中 FinePDFs exact retrieval 为 0%，hardware transition audit 非随机；不能宣称普遍外推，Raven/softmax/更短 context 仍是共存点。`; Artifact=`https://github.com/kreasof-ai/atma`

## MULTIMODAL-EMBODIED-VLA — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25215**：VLA state 从当前 observation 扩成 observation-action-consequence triplet buffer；shared attention 读历史后果，block-causal mask 防训练泄漏，KV cache 支撑实时滚动。 LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25215: `arXiv:2606.25215v1`; exact-v1 URL=`https://arxiv.org/html/2606.25215v1`; Method=`https://arxiv.org/html/2606.25215v1 — §3 Method; Observation-Action-Consequence Context; Block-Causal Training`; Evaluation=`https://arxiv.org/html/2606.25215v1 — §4 Experiments; C/D Evaluation Protocols`; Non-proof=`LIBERO/SimplerEnv 与有限 real robot/camera placement 不证明长 horizon、强接触或 unseen embodiment；context/latency 失控时回退 reactive VLA。`; Artifact=`https://lianqing11.github.io/reflective-vla-page/`

## PLATFORM-EVALUATION-SYSTEM — books/part-06-ai-infrastructure/66-evaluation-system.md

相邻章 `books/part-06-ai-infrastructure/67-monitoring.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24074**：把一次性 benchmark 分数改成带双侧错误界、逐 token 成本和停止阈值的 SPRT certification；certifier 持有 query/score/log-likelihood state，跨阈值才发布 reliable/unreliable verdict。 只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。
- **SF-2026-ARXIV-2606-24081**：把 T2I jailbreak 的 prompt-only 比较升级为 paper-to-pipeline contract：attack module、victim、filter、multimodal judge、配置、日志与版本 artifact 共同成为可复现状态。 11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。
- **SF-2026-ARXIV-2606-24124**：将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。 逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。
- **SF-2026-ARXIV-2606-24996**：deployment-facing leaderboard claim 必须经过 interface lock、clean positive anchor、native negative control、power/false-promotion 与 first-failing-gate report card；任一 gate 失败即禁止发布 selection inversion。 证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24074: `arXiv:2606.24074v1`; exact-v1 URL=`https://arxiv.org/html/2606.24074v1`; Method=`https://arxiv.org/html/2606.24074v1 — §3 Reliability Certification Setup; 4 Constructing a Certification SOTM`; Evaluation=`https://arxiv.org/html/2606.24074v1 — §5 A Matching Reliability Certification Lower Bound`; Non-proof=`只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24081: `arXiv:2606.24081v1`; exact-v1 URL=`https://arxiv.org/html/2606.24081v1`; Method=`https://arxiv.org/html/2606.24081v1 — §3 PixJail Framework; 3.2 Attack Module; 3.3 Evaluation Pipeline; 3.4 Memory Updates`; Evaluation=`https://arxiv.org/html/2606.24081v1 — §4 Experiments; 4.1 Data, Models and Metrics; 4.3 Main Results`; Non-proof=`11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24124: `arXiv:2606.24124v1`; exact-v1 URL=`https://arxiv.org/html/2606.24124v1`; Method=`https://arxiv.org/html/2606.24124v1 — §3 DSL for Reasoning Trace Formalization; 4 Structured Verification`; Evaluation=`https://arxiv.org/html/2606.24124v1 — §5 Evaluation; E Standalone Verification on ProcessBench`; Non-proof=`逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24996: `arXiv:2606.24996v1`; exact-v1 URL=`https://arxiv.org/html/2606.24996v1`; Method=`https://arxiv.org/html/2606.24996v1 — §2 Results: Two Roles for the Certification Protocol`; Evaluation=`https://arxiv.org/html/2606.24996v1 — §A Report-Card and Gate Procedure; C/D Robustness Controls`; Non-proof=`证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## PLATFORM-GPU-SCHEDULER — books/part-06-ai-infrastructure/63-gpu-scheduler.md

相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25082**：MIG scheduler 同时拥有 configuration 内作业放置与 configuration 间 repartition；controller 以 power/performance state、partition action 与 reward 决定何时重分，而不是把 MIG 当静态 SKU。 主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。
- **SF-2026-ARXIV-2606-25098**：grid signal 成为 cluster scheduler 的外部 control input，power telemetry/model 回写可用 curtailment budget；priority job 保留服务级别，elastic job 承担降载或跨地域迁移。 130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25082: `arXiv:2606.25082v1`; exact-v1 URL=`https://arxiv.org/html/2606.25082v1`; Method=`https://arxiv.org/html/2606.25082v1 — §IV Proposed Solution; Scheduling Within Configuration; Dynamic Re-Partitioning`; Evaluation=`https://arxiv.org/html/2606.25082v1 — §V Experiments and Results`; Non-proof=`主要是 simulation 与测得的 MIG power characteristic；repartition downtime、state migration、真实混合作业 SLO 和多节点 GPU fabric 未闭合，收益不足时保留静态 partition。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25098: `arXiv:2606.25098v1`; exact-v1 URL=`https://arxiv.org/html/2606.25098v1`; Method=`https://arxiv.org/html/2606.25098v1 — §3 Architecture for Power-Flexible AI Infrastructure`; Evaluation=`https://arxiv.org/html/2606.25098v1 — §4 Experimental Demonstration; 5 Grid Services; 6 Geo-Load Shifting`; Non-proof=`130 kW GPU cluster 与展示的 dispatch/geo shift 不证明 hyperscale、所有训练 checkpoint 或数据主权条件；telemetry/model 失准时回退静态 power cap 和 locality policy。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## PLATFORM-MONITORING — books/part-06-ai-infrastructure/67-monitoring.md

相邻章 `books/part-06-ai-infrastructure/66-evaluation-system.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24119**：撤销把 denoising top-1 concentration 当 PEFT collapse alarm 的旧路径；monitor 改读 max LoRA gradient norm，并由每个 DLM family 的 held-out calibration 拥有告警阈值。 816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24119: `arXiv:2606.24119v1`; exact-v1 URL=`https://arxiv.org/html/2606.24119v1`; Method=`https://arxiv.org/html/2606.24119v1 — §3 Methodology; 3.2 Experimental Setup`; Evaluation=`https://arxiv.org/html/2606.24119v1 — §4 Experiments and Results; 4.1 Calibrated Triage`; Non-proof=`816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## PLATFORM-SECURITY — books/part-06-ai-infrastructure/72-security.md

相邻章 `books/part-06-ai-infrastructure/73-production-best-practice.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24245**：把静态 expert rule 的维护改为 annotation-driven CEGIS：trace evaluator 产出 FP/FN counterexample，ILP 选 discriminating predicate，candidate verifier 决定是否发布 rule revision。 291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。
- **SF-2026-ARXIV-2606-24322**：memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。 保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。
- **SF-2026-ARXIV-2606-24402**：RAG 安全 gate 不再只问文档是否被检索，而按 local-artifact、model-knowledge、runtime-dependent 三层 verification boundary 决定 claim 能否进入行动；L3 需要动态探测或权威外部证据。 11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。
- **SF-2026-ARXIV-2606-24408**：利用训练数据自然出现且稀有的 identifier 作为 post-hoc audit unit，避免必须预埋 canary；auditor 分离 DP leakage 检查与 dataset inference，并记录 identifier cardinality/生成机制。 NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。
- **SF-2026-ARXIV-2606-24774**：training-data audit 从 output entropy 转向 parameter-gradient signature；auditor 对跨模态 parameter slices 做稳定性/对齐特征，并用已知 train/non-train reference mask 掉不敏感维度。 需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。
- **SF-2026-ARXIV-2606-25189**：policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。 1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24245: `arXiv:2606.24245v1`; exact-v1 URL=`https://arxiv.org/html/2606.24245v1`; Method=`https://arxiv.org/html/2606.24245v1 — §3 Overview; 4 Approach; ILP-Guided Predicate Learning`; Evaluation=`https://arxiv.org/html/2606.24245v1 — §5 Experimental Setup; 6 Evaluation`; Non-proof=`291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24322: `arXiv:2606.24322v1`; exact-v1 URL=`https://arxiv.org/html/2606.24322v1`; Method=`https://arxiv.org/html/2606.24322v1 — §II Threat Model; III TMA-NM; IV Formal Model`; Evaluation=`https://arxiv.org/html/2606.24322v1 — §V MEM-INV-Bench; VI Evaluation`; Non-proof=`保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24402: `arXiv:2606.24402v1`; exact-v1 URL=`https://arxiv.org/html/2606.24402v1`; Method=`https://arxiv.org/html/2606.24402v1 — §3 Problem Setting and Study Design; 5 Verification Boundary`; Evaluation=`https://arxiv.org/html/2606.24402v1 — §4 Poisoning Outcomes; 6 Generalization; 7 Mitigations`; Non-proof=`11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24408: `arXiv:2606.24408v1`; exact-v1 URL=`https://arxiv.org/html/2606.24408v1`; Method=`https://arxiv.org/html/2606.24408v1 — §3 Natural Identifiers; 4 DP Auditing; 5 Dataset Inference`; Evaluation=`https://arxiv.org/html/2606.24408v1 — §H DP-SGD Auditing; I/J/K Additional Evaluation`; Non-proof=`NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24774: `arXiv:2606.24774v1`; exact-v1 URL=`https://arxiv.org/html/2606.24774v1`; Method=`https://arxiv.org/html/2606.24774v1 — §GradAudit gradient-slice and noise-masking methodology`; Evaluation=`https://arxiv.org/html/2606.24774v1 — §Seven pretraining/fine-tuning configurations; medical and general datasets`; Non-proof=`需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25189: `arXiv:2606.25189v1`; exact-v1 URL=`https://arxiv.org/html/2606.25189v1`; Method=`https://arxiv.org/html/2606.25189v1 — §3 Design; Policy DSL; Information-Flow Control`; Evaluation=`https://arxiv.org/html/2606.25189v1 — §5 Evaluation; Compliance; Macro/Micro Overhead`; Non-proof=`1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。`; Artifact=`https://github.com/eunomia-bpf/ActPlane`

## PLATFORM-TRACE — books/part-06-ai-infrastructure/69-trace.md

相邻章 `books/part-06-ai-infrastructure/67-monitoring.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24626**：故障诊断不再把全 trajectory 填入一个 context；investigator 用 segment search/read tools 主动取证，并用 persistent STM 保存跨轮 hypothesis/evidence，使 attribution 与原始 trace 长度解耦。 Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24626: `arXiv:2606.24626v1`; exact-v1 URL=`https://arxiv.org/html/2606.24626v1`; Method=`https://arxiv.org/html/2606.24626v1 — §2 Methodology: SAFARI`; Evaluation=`https://arxiv.org/html/2606.24626v1 — §3 Experimental Setup; 4 Results; A/B/C appendices`; Non-proof=`Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## TRAIN-DATA — books/part-04-training-system/27-data.md

相邻章 `books/part-04-training-system/28-pretraining.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24133**：把固定或单目标 data mixture 改为 SAC controller：state 汇聚 domain loss/lexical diversity/weight-norm，action 写回下一训练阶段的 domain weights，多目标 reward 决定调度。 The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。
- **SF-2026-ARXIV-2606-24998**：数据去重从 hygiene 建议升级为 compute allocation contract：相同样本的 internal repetition 先改善后破坏 eval loss，data owner 应记录 repeat count、unique pool 与 model-size-dependent peak。 结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24133: `arXiv:2606.24133v1`; exact-v1 URL=`https://arxiv.org/html/2606.24133v1`; Method=`https://arxiv.org/html/2606.24133v1 — §2 Methodology: The Holistic Data Scheduler; 2.2 Online Data Mixing`; Evaluation=`https://arxiv.org/html/2606.24133v1 — §3 Experiments and Analysis; 3.1 Experimental Setup`; Non-proof=`The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24998: `arXiv:2606.24998v1`; exact-v1 URL=`https://arxiv.org/html/2606.24998v1`; Method=`https://arxiv.org/html/2606.24998v1 — §3 Methods; Repeated-pool construction`; Evaluation=`https://arxiv.org/html/2606.24998v1 — §4 Results; F Training and Evaluation Details`; Non-proof=`结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## TRAIN-DISTRIBUTED-TRAINING — books/part-04-training-system/36-distributed-training.md

相邻章 `books/part-04-training-system/38-pipeline-parallel.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24143**：将 rollout、teacher scoring、student update 解耦为 queue stages；learner 用 current-student recomputation 修正 reverse-KL stale signal，并以 multi-sample MC 避免 cached top-k support bias。 实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。
- **SF-2026-ARXIV-2606-24722**：把 end-to-end backprop 的全局 hidden-target ownership拆成 block-local diffusion objective；edge worker 独立更新 block，coordinator 只按版本/acceptance rule 接收异步 update，同一 block protocol 也支撑分布式 inference。 real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。

### Source-specific Review notes

- SF-2026-ARXIV-2606-24143: `arXiv:2606.24143v1`; exact-v1 URL=`https://arxiv.org/html/2606.24143v1`; Method=`https://arxiv.org/html/2606.24143v1 — §4 Forward- and Reverse-KL OPD Under Staleness; 7 AsyncOPD`; Evaluation=`https://arxiv.org/html/2606.24143v1 — §7 AsyncOPD Experimental Results; G Scheduler Details`; Non-proof=`实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。`; Artifact=`https://github.com/furiosa-ai/async-opd`
- SF-2026-ARXIV-2606-24722: `arXiv:2606.24722v1`; exact-v1 URL=`https://arxiv.org/html/2606.24722v1`; Method=`https://arxiv.org/html/2606.24722v1 — §2 Protocol; Block-Local Diffusion Objective; Decentralized Execution`; Evaluation=`https://arxiv.org/html/2606.24722v1 — §3 Real-Text Experiments; 4 Decentralization and Asynchrony`; Non-proof=`real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

## TRAIN-GRPO — books/part-04-training-system/33-grpo.md

相邻章 `books/part-04-training-system/31-rlhf.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-25178**：多域 RLVR curriculum 不再只追当前 domain learnability；controller 从正在计算的 GRPO projected gradients 估计跨域 transfer，对 bandit arm value 做平滑后决定下一 domain。 六域、Qwen3-1.7B/Llama3.2-3B 与 <1% overhead 不证明更大模型、non-verifiable reward 或 adversarial domain；gradient conflict 不稳定时回退 proportional/hand-designed mix。

### Source-specific Review notes

- SF-2026-ARXIV-2606-25178: `arXiv:2606.25178v1`; exact-v1 URL=`https://arxiv.org/html/2606.25178v1`; Method=`https://arxiv.org/html/2606.25178v1 — §3 Method; Gradient-Based Transferability; Curriculum Algorithm`; Evaluation=`https://arxiv.org/html/2606.25178v1 — §4 Experiments; B Implementation/Evaluation Details`; Non-proof=`六域、Qwen3-1.7B/Llama3.2-3B 与 <1% overhead 不证明更大模型、non-verifiable reward 或 adversarial domain；gradient conflict 不稳定时回退 proportional/hand-designed mix。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

