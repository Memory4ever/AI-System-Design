# 2026-06-03 V3 semantic screening ledger

本 ledger 以 719-row canonical title+abstract packet 为唯一分母。先逐项读 title；边界不清或拟从旧 generic closure 恢复时读取完整 abstract。只有明确改变大模型/Infra 的 state/data/control ownership、execution/evaluation/release contract 或修正现有长期结论者进入 Candidate。

## 冻结结果

- Raw identities：719。
- Candidate：87；旧 44 项重审后保留 39 项，675 条旧 closure 中恢复 48 项。
- Pre-denominator Close：632；旧候选降级 5 项，旧 closure 维持关闭 627 项。
- 旧 Integrate：14 项均在严格分母中存续；fresh-context Books 复判后 7 项形成正文写回、7 项由现有命题级正文覆盖。两条 trace 日期错配中，Inference / Platform 所属项已修正，TRAIN 所属项交由对应 owner 处理。

## 旧候选前沿重审（44）

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.02643 | RAG inference cost attacks | Candidate | 外部知识库 poisoning 可放大检索与生成成本，改变 RAG 资源滥用威胁模型。 |
| 2606.02646 | MAS Ringelmann scaling | Candidate | 用 effective evidence 而非 nominal agent count 定义多 Agent 扩展合同。 |
| 2606.02668 | Consent Integrity | Candidate | approval 必须由 trusted mediator 从真实 action 渲染，改变人审执行边界。 |
| 2606.02800 | Cosmos 3 | Close | omnimodal world-model family 与任务结果是新模型架构/性能，题摘未给系统 ownership 或 release contract。 |
| 2606.02958 | Echelon | Candidate | device-level state non-export 是 boundary-first adaptation 的系统 invariant。 |
| 2606.02959 | Gate AI | Candidate | 固定阈值、group split 与 operating point disclosure 改变安全 benchmark 发布合同。 |
| 2606.02963 | KForge | Candidate | 跨 accelerator kernel generation 的验证与 backend ownership 属于推理基础设施。 |
| 2606.02964 | Multi-Segment Attention | Candidate | 用 kernel execution cost 决定 lossless KV eviction/reconstruction。 |
| 2606.02982 | DriftSched | Candidate | admission estimate 与 runtime token drift 持续 reconciliation。 |
| 2606.03001 | FOLD | Candidate | 对持续摄入训练语料建立 online fuzzy-dedup state 与 admission contract。 |
| 2606.03002 | SAE feature damage under quantization | Candidate | perplexity parity 不保证 feature fidelity，修正压缩 release gate。 |
| 2606.03005 | MUSE | Candidate | frozen MLLM 外围 harness 的 tool、parser 与 deterministic verification 分权。 |
| 2606.03014 | MOSAIC MoA scheduling | Candidate | routing skew、generation variance 与 inference concurrency 联合调度。 |
| 2606.03024 | SkillGuard | Candidate | skill 成为独立 security principal，并连接 intent、permission 与 runtime action。 |
| 2606.03026 | Spiking LM CPU runtime | Close | 绑定特定 spiking LM 与 commodity CPU 的局部 runtime，未给跨大模型 workload 合同。 |
| 2606.03032 | Deliberative Illusion | Candidate | factual attrition 与 stance homogenization 修正“共识即可靠”的多 Agent 评测结论。 |
| 2606.03034 | Capability advertisement trust | Candidate | 对 Agent registry 的 identity、drift、evidence 与 freshness 建立 trust layer。 |
| 2606.03043 | Judge subspace alignment | Candidate | inter-judge consensus 不取得 human-alignment authority，修正 judge evidence 边界。 |
| 2606.03054 | ToolGate | Candidate | perceptual tool issue 前的 execute/skip gate 改变 VLM Agent control flow。 |
| 2606.03056 | SkillDAG | Candidate | typed dependency/conflict graph 取代 skill 文档相似度，改变 skill routing state。 |
| 2606.03070 | ASymPO | Candidate | asynchronous post-training 在无 behavior logprob 时重定义 stale-policy 更新边界。 |
| 2606.03077 | Libra | Candidate | rollout/learner 的异构资源与 long-tail makespan 形成 Agentic RL 控制面。 |
| 2606.03108 | EvoTrainer | Candidate | policy 与 training harness 共同版本化、诊断与 backtest。 |
| 2606.03115 | SPOQ | Candidate | dependency waves、pre/post validation 与 Human-as-Agent 改变 coding workflow。 |
| 2606.03152 | Agentic query execution | Candidate | LLM operator 的 dollar cost/quality 使 planning 与 execution 在线交织。 |
| 2606.03159 | OmniDreams | Close | 自动驾驶 closed-loop world model 绑定单一物理仿真垂直任务。 |
| 2606.03161 | OAN trust layer | Candidate | Agent interconnection 前的 identity、governance、freshness 与 discovery authorization。 |
| 2606.03209 | DECA | Candidate | decentralized LLM FPFT 的 optimizer state、通信与 non-IID convergence contract。 |
| 2606.03305 | Contamination audit reliability | Candidate | distribution shift 与 scale 改变 contamination detector 的 release authority。 |
| 2606.03308 | Code-LLM hardening bound | Candidate | pass-only prompt filter 的不可消除 floor 修正安全验收结论。 |
| 2606.03323 | Pod-level attestation | Candidate | LLMaaS confidential workload 需要 Pod identity 而非只 attest Guest OS。 |
| 2606.03381 | Model extraction multi-client | Candidate | 跨身份 aggregation 击穿 per-client 防护，改变全局 security budget。 |
| 2606.03498 | PipeDream theory | Candidate | 对 pipeline parallel stale block-SGD 给出可核验训练边界。 |
| 2606.03518 | Compositional authorization | Candidate | delegation graph、time-limited scope 与 revoke 改变 Agent IAM。 |
| 2606.03519 | SIGMA GNN partition | Close | 通用 GNN graph partitioner，不属于大模型/Infra 当前主线。 |
| 2606.03650 | CoEval | Candidate | 无标签/不可信 benchmark 时的 model-selection authority 与交叉角色评测。 |
| 2606.03724 | Same Weights, Different Robot | Candidate | checkpoint 不等于 executable policy，要求 unnormalization/controller 一并发布。 |
| 2606.03755 | LAP | Close | Agent-to-instrument protocol 仍绑定 autonomous-science 垂直主线，本期不纳入。 |
| 2606.03770 | E2LLM | Candidate | heterogeneous edge/fog 的模型切分、placement 与资源控制属于 LLM serving。 |
| 2606.03811 | Adaptive worms | Candidate | LLM Agent 使 worm 从固定 exploit 变为按目标生成策略，扩展平台威胁模型。 |
| 2606.03819 | TreeFlash | Candidate | tree draft 的 AR approximation 与 target verification 改变 speculative runtime。 |
| 2606.03889 | RealClawBench | Candidate | 真实 session 的 environment reconstruction 与 verification 改变 Agent benchmark contract。 |
| 2606.03895 | Agent libOS | Candidate | operation admission、typed capability、budget 与 information-flow 三平面分权。 |
| 2606.03910 | NetKV | Candidate | network cost oracle 进入 disaggregated prefill/decode routing 与 TTFT SLO。 |

结果：39 Candidate，5 Close。

## 从旧 generic closure 恢复（48）

| ID | 标题（缩写） | 题摘支持的长期 design delta |
| --- | --- | --- |
| 2606.02581 | Cost-Aware RAG | 逐 query 选择 retrieval strategy bundle，将 token/latency/grounding 联合纳入控制。 |
| 2606.02606 | ReLoRA | base-model 更新后 adapter compatibility 与 rollout delay 成为版本迁移合同。 |
| 2606.02755 | Acceptance-test LLM evaluation | 把 stakeholder requirement 编译为可执行验收与业务 release gate。 |
| 2606.02822 | OWASP defense attribution | 从总覆盖率改为 defense-family/threat/operating-point 可归因报告。 |
| 2606.02835 | Harmful overthinking | 以 prefix trajectory 判断达到正确答案后的额外 reasoning 是否反向退化。 |
| 2606.02875 | Handoff Debt | repository partial state、handoff view 与 successor rediscovery cost 进入 coding-Agent 评测。 |
| 2606.02907 | Probe format confound | 线性 probe 分离可能来自 task format，修正 reasoning representation 证据边界。 |
| 2606.02955 | Fast-dLLM++ | 按 heterogeneous confidence profile 决定 diffusion LM token commit。 |
| 2606.02981 | Inference-scaling predictor | 用廉价 validation statistics 预估 Best-of-N 收益，改变预算 admission。 |
| 2606.03075 | TGV-KV | VLM KV eviction 按 text-grounded cross-modal relevance 而非通用语言启发式。 |
| 2606.03083 | DeltaMem | residual-tree 维护增量经验，显式处理冗余与冲突。 |
| 2606.03087 | Correct-set turnover | RLVR 同时跟踪 acquisition 与 retention，修正只看 headline accuracy 的训练门禁。 |
| 2606.03092 | Shadow-price reasoning | 以全局资源影子价格分配 per-query inference budget。 |
| 2606.03113 | Dynamic exits | 按 local context 在线选择 exit layer 与 speculation length。 |
| 2606.03135 | Clarification information gain | 在 tool action 前用 intent belief update 决定是否向用户澄清。 |
| 2606.03136 | PsychoPass | guardrail state 从单 turn 扩为整段 adversarial trajectory。 |
| 2606.03143 | FederatedSkill | 跨用户 skill 演进分离本地隐私状态与共享更新。 |
| 2606.03220 | WebRISE | 将 requirement 编译为 observable state/transition/DOM-visual assertion。 |
| 2606.03239 | ARBOR | reusable rubric buffer 为 search-Agent process reward 保存 provenance 与复用状态。 |
| 2606.03291 | Multilingual unlearning | language transfer 与 reversibility 成为 unlearning release/rollback 条件。 |
| 2606.03318 | Realistic-interaction eval | 用户 ambiguity、uncooperative behavior 与 shifting intent 进入 tool-use 验收。 |
| 2606.03328 | Pruning calibration tradeoffs | averaged score 掩盖 capability retention，修正高稀疏 release gate。 |
| 2606.03330 | FLIPS | model identity 扩为 weights+prompt+sampling+quantization 的 instance identity。 |
| 2606.03344 | RogueMerge | 第三方 task vector 是对模型权重的 supply-chain write access。 |
| 2606.03354 | ImageAuditor | image-RAG datastore membership 扩展检索数据的版权/隐私审计边界。 |
| 2606.03391 | MoE merge routing breakdown | model merge 发布必须单独校准 router，而不能只验证权重聚合结果。 |
| 2606.03458 | KVarN | autoregressive KV quantization error 随 timestep 累积，改变 long-reasoning 压缩验收。 |
| 2606.03461 | Terminal-Agent trajectories | teacher 独立能力不等于 trajectory 教学价值，训练数据需 environment verification。 |
| 2606.03463 | DMF | deterministic CPU-first memory write/prune 取代不可审计的生成式摘要。 |
| 2606.03467 | StepFinder | temporal dependency 定位多 Agent cascade 的 root-cause step。 |
| 2606.03544 | SAGE | compute-matched social/self evolution 区分共享经验的真实增益。 |
| 2606.03565 | R3-Skill | skill retrieval 必须输出彼此兼容的 executable set，而非独立相关文档。 |
| 2606.03601 | DDOR | black-box delta debugging 将 overrefusal 定位、解释与 repair 串成闭环。 |
| 2606.03647 | LLM attack baseline | 要求 adaptive/transferable/applicable attack，修正虚高 robustness 结论。 |
| 2606.03648 | Capability-grounded safety | fine-tune 安全比较必须绑定相同 capability goal。 |
| 2606.03657 | NovelAPIBench | 动态发现 API、重建 environment 并验证 executable usage contract。 |
| 2606.03692 | SkillPyramid | skill construction、consolidation、transfer 与版本复用形成持久资产层级。 |
| 2606.03739 | Entropy Gate | LLM pipeline 的 token compression 需要语义 fidelity 与低信息预算门禁。 |
| 2606.03762 | Tool-aware agentic RL | tool trajectory filtering 与 exploration entropy 共同约束 rollout 数据。 |
| 2606.03785 | Backdoor unlearning | unknown-trigger generalization 将安全修复从已知 trigger 扩到 release 风险域。 |
| 2606.03800 | RLVR task supply | sandbox、prompt、reward function 与 human/synthetic substitution 构成训练数据合同。 |
| 2606.03810 | Consistency training misalignment | self-bootstrapping 可能固化不良行为，修正“label-free 一定安全”的训练假设。 |
| 2606.03892 | PROVE | stateful MCP server、state-grounded query 与 programmatic reward 共同定义 live tool-use RL。 |
| 2606.03928 | Value-aware KV eviction | reasoning decode 中 value outlier 与 stochastic eviction 决定可恢复缓存路径。 |
| 2606.03938 | Hyper-epoch pretraining | 从单模型重复 epoch 转向 model population 与 aggregation，改变训练状态 ownership。 |
| 2606.03969 | Faithful confidence | 区分 intrinsic 与 expressed confidence，修正 reasoning model 不确定性报告。 |
| 2606.03979 | Sleep memory consolidation | context knowledge 向长期参数迁移要求显式 self-modification/consolidation phase。 |
| 2606.03980 | Skill-RM | 将 rule、reference、checklist、rubric 统一为可版本化 reward-evaluation skill。 |

## 关闭 family（632）

全量 title sweep 后，边界项读取完整 abstract。关闭项按互斥 family 计数：

| Closure family | 数量 | 具体边界 |
| --- | ---: | --- |
| Embodied/local task method | 52 | robot、driving、physical simulation 或单一 VLA 控制；包含 OmniDreams，未证明跨 workload 系统合同。 |
| Incremental model/method | 481 | 局部架构、adapter、训练技巧或表示分析；含降级的 Cosmos 3、spiking CPU runtime 与 SIGMA。 |
| Local benchmark | 22 | 单一模态/语言/任务数据集或 leaderboard，没有可迁移 release delta。 |
| Theory without AI-system contract | 5 | 通用优化、统计或学习理论，没有大模型系统 owner。 |
| Vertical application | 72 | 医疗、金融、科学、推荐、遥感等单一领域；包含 LAP autonomous-science protocol。 |

合计 632 Close，与 87 Candidate 覆盖全部 719 identities。旧 closure 内部对应 51/478/22/5/71 = 627；另加五个旧候选降级。

## Fresh-context FP/FN 抽检

| 方向 | 样本 | 结论 |
| --- | --- | --- |
| Candidate FP challenge | 02668、02958、02964、02982、03024、03070、03077、03323、03895、03910 | 10/10 有明确 trusted path、state non-export、KV、token drift、permission、async RL、resource、attestation、capability 或 network ownership。 |
| Recovered boundary challenge | 02755、02875、02907、03135、03220、03330、03461、03657、03800、03980 | 10/10 的准入依据是可迁移验收/状态/身份/训练数据/奖励合同，不是对象名或局部分数。 |
| Close FN challenge | 02614、02624、02800、02812、03159、03519、03755、03829、03841、03963 | 10/10 完整摘要仍绑定公共政策/蛋白/单模型架构/医疗/驾驶/GNN/科学/金融/数据科学/UAV 等局部或垂直对象。 |

抽检未发现新的共享错误 family，87-item denominator 冻结。其后的 exact-v1 Evidence、Books Decision 与独立 post-write review 均已闭合，最终状态见日报与 `POST_WRITE_AUDIT_SCOPE_V3.md`。
