# 2026-06-02 V3 Books Post-write Audit Scope

## 审计边界

本记录登记 2026-06-02 全部 32 项 Books 正文写入，以及 proposal 消费过程中改判 Existing 的命题级锚点。正文存在、锚点位于顶层 `Review notes` 之前、owner 边界与证据 non-proof 均通过独立复核；它不以 Daily trace 或 proposal 状态替代正文。

## 已写入 Review notes 前正文（32）

| arXiv exact-v1 | Owner | 正文锚点 | 作者侧检查 |
| --- | --- | --- | --- |
| `2606.00395v1` | `TRAIN-GRPO` | “MoE Route Replay 也属于 Behavior-policy Identity” | 通过：旧方案、route state/control owner、staleness、trade-off 与 fallback 可定位 |
| `2606.00756v1` | `AGENT-MEMORY` | “Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权” | 通过：local/cloud owner、dispatch/expiry、断连 fallback 与证据边界可定位 |
| `2606.01091v1` | `TRAIN-GRPO` | “Evidence-derived Rubric 是版本化 Reward State” | 通过：rubric provenance/bootstrap/polarization 与 static fallback 可定位 |
| `2606.01155v1` | `TRAIN-PRETRAINING` | “数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账” | 通过：联合 scaling identity、data saturation、硬件 non-proof 与 dense fallback 可定位 |
| `2606.01680v1` | `TRAIN-DISTRIBUTED-TRAINING` | “退化链路仍在线时，Collective 需要 Bandwidth-state Schedule” | 通过：collective semantics、planner authority、lower-bound scope 与普通 collective fallback 可定位 |
| `2606.02218v1` | `TRAIN-GRPO` | “同步 Group Size 也可以由 Straggler Risk 有界调节” | 通过：同步/on-policy invariant、posterior risk、measurement 与静态 group fallback 可定位 |
| `2606.02245v1` | `AGENT-RAG` | “Evidence Access Right、Cost 与 Sufficiency 是联合检索状态” | 通过：authorization/source authority 优先级、budget receipt、abstain 与免费 corpus fallback 可定位 |
| `2606.02357v1` | `AGENT-TOOL-CALLING` | “Tool 出现不等于 Tool 对答案有贡献” | 通过：三条反事实、attribution/outcome 分权、不可逆环境 fallback 与 non-proof 可定位 |
| `2606.02359v1` | `AGENT-MULTI-AGENT` | “多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要” | 通过：per-hop lineage、merge/transport/workflow 分权、consolidation-loss receipt 与 raw-message fallback 可定位 |
| `2606.00024v1` | `INFER-KV-CACHE` | “Value-aware Termination 只能提前结束读取，不能接管正确性” | 通过：traversal state、threshold 风险与 full traversal fallback 可定位 |
| `2606.00093v1` | `PLATFORM-EVALUATION-SYSTEM` | “Judge Agreement 不是单一数字” | 通过：measurement identity、exclusion/abstention 与 truth authority 分离可定位 |
| `2606.00152v1` | `PLATFORM-SECURITY` | “Tool Response 在进入 Context 时就要执行 Data-minimization Gate” | 通过：acquisition-time admission、field receipt 与 narrow-scope fallback 可定位 |
| `2606.00485v1` | `PLATFORM-SECURITY` | “App-local Context Namespace 阻止普通 Writer 获得跨 App Authority” | 通过：namespace/provenance/mediator 与 fail-closed composition 可定位 |
| `2606.00611v1` | `PLATFORM-MONITORING` | “Risk-aware Latent 只能压缩 Evidence，不能压缩 Authority” | 通过：compressor/reader identity、raw evidence fallback 与 authority 边界可定位 |
| `2606.00654v1` | `PLATFORM-SECURITY` | “模型建议也可能塑造未来 Trigger” | 通过：跨轮 lineage、independent confirmation 与自证自批禁界可定位 |
| `2606.00801v1` | `PLATFORM-SECURITY` | “Semantic Archive 暴露 Mode Collapse，但不拥有 Release Verdict” | 通过：coverage state、mutation lineage 与 independent verdict 可定位 |
| `2606.00866v1` | `INFER-KV-CACHE` | “Agent Idle Window 要按 Program Horizon 决定 Tier，而不是二元搬空” | 通过：tier state、transfer fence、admission 与 no-move/LRU fallback 可定位 |
| `2606.00947v1` | `PLATFORM-EVALUATION-SYSTEM` | “Federated Personalization 的盲区是可见性合同” | 通过：client-local evidence visibility、taxonomy non-proof 与 unknown state 可定位 |
| `2606.01725v1` | `INFER-SCHEDULING` | “Task-DAG Simulator 只能校准 Capacity Plan，不能承诺线上 SLO” | 通过：DAG workload identity、capacity owner 与 simulation non-proof 可定位 |
| `2606.01751v1` | `INFER-KV-CACHE` | “非 Prefix 复用必须绑定 Position-aligned Segment 与 Correction State” | 通过：segment identity、correction owner 与 dense/full-attention fallback 可定位 |
| `2606.01815v1` | `PLATFORM-EVALUATION-SYSTEM` | “Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境” | 通过：generator/verifier identity、side-effect sandbox 与外部有效性边界可定位 |
| `2606.01839v1` | `INFER-SCHEDULING` | “Conversation Placement 用已观察状态替代逐 Turn 预测” | 通过：conversation owner、KV transfer/pinning 与 per-turn fallback 可定位 |
| `2606.01850v1` | `PLATFORM-EVALUATION-SYSTEM` | “Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty” | 通过：双门禁、regime identity 与统一 safe bit-width non-proof 可定位 |
| `2606.01927v1` | `INFER-REQUEST-LIFECYCLE` | “并行扩展必须先移出不可扩展的 Host Critical Path” | 通过：host/runtime control flow、Amdahl 边界与低 TP coexistence 可定位 |
| `2606.02011v1` | `INFER-TENSORRT-LLM` | “Reasoning Quantization 要验收 Commitment，而不只是 Token Cost” | 通过：precision/budget/termination identity、loop failure 与 FP16 fallback 可定位 |
| `2606.02041v1` | `PLATFORM-SECURITY` | “Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence” | 通过：buffer/segmenter/released bytes 与 abort fallback 可定位 |
| `2606.02060v1` | `PLATFORM-EVALUATION-SYSTEM` | “Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标” | 通过：first harmful commitment、annotation/judge boundary 与 raw-trace fallback 可定位 |
| `2606.02091v1` | `INFER-SPECULATIVE-DECODING` | “Draft Capacity 可以借用 Target Feature，但不能借走 Commit Authority” | 通过：draft/target ownership、verification cost 与 serial fallback 可定位 |
| `2606.02240v1` | `PLATFORM-SECURITY` | “Integration-aware Campaign 必须把 Connector 与 Effect Identity 编进 Case” | 通过：connector/effect identity、cleanup receipt 与 issue authority 可定位 |
| `2606.02430v1` | `PLATFORM-EVALUATION-SYSTEM` | “数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播” | 通过：fault model、propagation coordinates 与 mitigation non-proof 可定位 |
| `2606.02494v1` | `PLATFORM-MONITORING` | “Pre-reliability Monitoring 先验证 Wiring，再解释 Quality” | 通过：scope/maturity/FMEA routing 与 unknown/human fallback 可定位 |
| `2606.02544v1` | `INFER-SPECULATIVE-DECODING` | “双向 Mask Context 必须先改写成 Temporal-causal Verification Layout” | 通过：position alignment、target commit 与 blockwise fallback 可定位 |

## 经正文重读改判 Existing（3）

| arXiv exact-v1 | Owner | 命题级锚点 | 不新增正文的理由 |
| --- | --- | --- | --- |
| `2606.00619v1` | `AGENT-MEMORY` | “Memory policy 本身也可能成为可学习、可版本化的 procedural asset”及其 held-out tournament/release 段 | 已覆盖 executable extraction/update procedure、source episode、独立验证、versioned bank、provenance、rollback 与 proposer/release 分权；tree evolution 是受限实现 |
| `2606.01770v1` | `AGENT-PLATFORM` | “Harness Controller 是版本化策略，不是模型的隐式习惯”“自适应 Harness 只能提交保持成功约束的干预”及章节小结 | 已覆盖 open-ended stream、harness history、routing/specialization、bounded intervention、release authority、rollback 与静态 harness fallback |
| `2606.02540v1` | `PLATFORM-SECURITY` | “Harness Backdoor 把单次写入变成跨 Run 控制状态” | 已覆盖 persistent skill 的跨 session reuse、revision/provenance/revoke、sandbox、rollback 与 independent release owner |

## Adoption residue

- `SF-ORDER-AGNOSTIC-CHAIN-RULE / arXiv:2606.00997v1` 未通过当前 Candidate Denominator；Ch24 的 Daily trace 已删除，未发现其他 source-specific 正文。
- `SF-DEEP-RESEARCH-RUBRIC-RL` 与 `SF-SPARSE-REPEATED-TRAINING` 的 Daily 日期已由 `2026-06-01` 修正为 `2026-06-02`。
- `SF-OPTCC-ASYMMETRIC-ALLREDUCE` 与 `SF-STRAGGLER-AWARE-RL-GROUP` 的 trace 已绑定本批正文锚点。

## 独立 post-write 复核

独立复核已重新读取 32 段正文、3 处 proposal-to-Existing 锚点和对应 exact-v1 evidence，并尝试证伪：

1. 正文是否只复述论文，而没有形成 owner-level 长期机制；
2. 状态、数据流或控制 authority 是否越过相邻 owner；
3. 证据边界是否把作者 benchmark 外推为生产或普遍结论；
4. trade-off、failure mode、旧方案共存与 fallback 是否真实可定位；
5. README、Evidence Batch、Books 与队列计数是否一致。

复核结果：上述五项均通过；未发现 source-specific 列表式追加、owner 越界、benchmark 外推、缺失 fallback 或计数漂移。

当前 Gate：**Books 写回与独立 post-write 复核完成；未决 proposal 为 0，日报可标记完成。**
