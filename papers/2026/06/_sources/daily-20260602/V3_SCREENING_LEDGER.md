# 2026-06-02 V3 semantic screening ledger

本 ledger 以可读的 1,449-row canonical title+abstract packet 为唯一分母。判断顺序是先逐项读 title，只在边界不清或要从旧 generic closure 恢复时读完整 abstract。`Candidate` 只表示题摘已明确给出可迁移的长期 design delta；不继承旧 `Complete/Open`、评分或 Books disposition。

## 冻结结果

- Raw identities：1,449。
- Candidate：110；其中旧 51 项重审后保留 44 项，1,398 条旧 closure 中恢复 66 项。
- Pre-denominator Close：1,339；其中旧候选降级 7 项，旧 closure 维持关闭 1,332 项。
- 旧 `Integrate`：17 项中 16 项仍在 Candidate；`2606.00997` 撤回。存续项为 15 项 trace-only 正文补写队列与 1 项 body-existing 核验。

## 旧候选前沿重审（51）

| ID | 标题（缩写） | 当前判断 | 题摘语义理由 |
| --- | --- | --- | --- |
| 2606.00942 | Metastable Faults | Close | 通用计算系统故障分类，未落到大模型执行状态或发布合同。 |
| 2606.00944 | PRISM DP-LoRA | Close | 单一 DP-LoRA 几何方法；题摘未改变训练平台的数据/控制 ownership。 |
| 2606.00946 | Lodestar router | Candidate | 在线路由在质量、价格与延迟反馈间更新，改变多模型推理控制面。 |
| 2606.00947 | Federated personalization silent failures | Candidate | 明确指出隐私约束下 client-local 行为不可见，改变 foundation-model 评测可观测性。 |
| 2606.00953 | Cohesion-aware coding-agent partition | Candidate | 把依赖内聚性作为并行 Agent 分工与合并失败的控制条件。 |
| 2606.00981 | Async auto-formal planning | Close | 通用规划/形式化算法，未给出大模型或 Agent 平台可迁移执行合同。 |
| 2606.00997 | Order-agnostic LM chain rule | Close | 局部生成模型概率一致性分析，不改变当前大模型系统的状态、执行或发布合同；撤回旧采用链。 |
| 2606.01007 | Task-aware MoE grouping | Candidate | 将 workload identity 纳入 MoE 通信分组，改变 serving collective 与路由协同。 |
| 2606.01019 | Hybrid verified decoding | Candidate | 在 speculative decoding 中动态分配验证，直接改变正确性/吞吐执行合同。 |
| 2606.01034 | LLM judge panel regime map | Candidate | 明确有限 calibration 下 judge panel 的适用区间与报告要求。 |
| 2606.01065 | Leyline KV directives | Candidate | 将 Agent 生命周期意图显式下沉为 KV cache directive，改变缓存 ownership。 |
| 2606.01066 | Fuzzing RLVR verifiers | Candidate | 在训练前发现 verifier reward 漏洞，改变 RLVR 数据/奖励发布门禁。 |
| 2606.01091 | Deep Research rubric RL | Candidate | evidence-derived atomic rubric 改变 RL reward provenance 与 bootstrap 合同。 |
| 2606.01128 | Local MixVR | Close | 通用分布式学习通信算法，题摘没有大模型规模或训练系统边界。 |
| 2606.01138 | memorywire | Candidate | vendor-neutral Agent memory wire format 明确读写、版本与互操作 ownership。 |
| 2606.01139 | SkillRevise | Candidate | trace-conditioned skill revision 将失败轨迹接入持久 skill 变更闭环。 |
| 2606.01143 | Shared-prefix reuse for LLM RL | Candidate | schedule-level prefix reuse 改变 rollout/training 的 KV 生命周期。 |
| 2606.01155 | Sparse LM repeated training | Candidate | 联合 token repetition、稀疏度与有效参数量，修正预训练 scaling 边界。 |
| 2606.01185 | Lakehouse agents | Close | 数据湖仓单一垂直应用优化，没有跨 workload 的 Agent 系统合同。 |
| 2606.01196 | Low-resource safety failures | Candidate | 证据把安全退化定位到 action 而非 representation，修正安全评测结论。 |
| 2606.01212 | DiscourseFlip | Candidate | 跨检索与生成链的 discourse manipulation 改变 RAG 威胁模型。 |
| 2606.01311 | SkillAdaptor | Candidate | first actionable fault 与 acceptance check 把 skill 更新限定为可回退的局部变更。 |
| 2606.01314 | SkillSmith | Candidate | skill 与 tool 联合演进，改变 Agent 能力包的状态与验证闭环。 |
| 2606.01317 | SABER | Candidate | stateful workspace 中 coding Agent 的操作安全门禁与评测合同。 |
| 2606.01365 | Failure-aware MAS observability | Candidate | 将浪费计算追到 Agent/step 级因果链，改变多 Agent 可观测性。 |
| 2606.01387 | Resident KV claims | Candidate | claim identity、materialization predicate 与 fail-closed lowering 构成 KV 控制面合同。 |
| 2606.01413 | DP RAG datastore | Candidate | 将隐私预算放到检索 datastore 生成边界而非只看输出。 |
| 2606.01416 | Self-healing orchestrators | Candidate | 明确检测、隔离、恢复与 fallback 的 Agent orchestration 生命周期。 |
| 2606.01435 | Memory evidence/policy split | Candidate | 分离 evidence extraction 与 policy execution，改变 Agent memory ownership。 |
| 2606.01462 | Reasoning production-eval gap | Candidate | 揭示离线评测与生产行为错位，修正 reasoning model release gate。 |
| 2606.01494 | ClawHub security-signal disagreement | Candidate | 多安全信号冲突要求显式 adjudication，改变 skill 发布门禁。 |
| 2606.01502 | Cross-instance latent redistribution | Candidate | 将 query 移动与 cache/fabric 代价共同纳入跨实例推理控制。 |
| 2606.01508 | Agent OS | Candidate | Agent control plane 与传统 OS resource boundary 的结构候选。 |
| 2606.01567 | Terminal Agent skill injection | Candidate | skill 来源、执行权限与注入防护改变终端 Agent 安全边界。 |
| 2606.01600 | RoboTrustBench | Close | 机器人 video world model 单一垂直 benchmark，未形成通用大模型系统增量。 |
| 2606.01680 | AllReduce network failures | Candidate | degraded-link 在线 collective 调度直接改变分布式训练控制面。 |
| 2606.01725 | Trace-driven agentic simulation | Candidate | 用 workload trace 模拟多模型 Agent 系统，形成容量规划与评测合同。 |
| 2606.01751 | SparseX segment KV | Candidate | position-aligned segment identity 与 selective correction 改变 KV reuse 边界。 |
| 2606.01770 | Adaptive Auto-Harness | Candidate | open-ended task stream 中 harness routing/evolution 构成持续部署控制面。 |
| 2606.01839 | Conversation scheduling | Candidate | conversation-lifetime placement 与 KV transfer 改变 Agent serving 调度粒度。 |
| 2606.01850 | Compression uncertainty | Candidate | 压缩发布同时约束 accuracy 与 calibrated uncertainty，修正 release gate。 |
| 2606.01927 | Async inference overheads | Candidate | scheduling/I/O overlap 与 Amdahl 边界改变推理并行度选择。 |
| 2606.02060 | Deep-research span error | Candidate | outcome 到 first harmful commitment 的 span 追踪改变 Agent 评测粒度。 |
| 2606.02091 | DFlare | Candidate | diffusion speculative decoding 的 draft capacity 与 target verification 共同决定执行成本。 |
| 2606.02218 | Straggler-aware RL groups | Candidate | 同步 on-policy RL 根据 straggler risk 调 group size，改变 rollout barrier。 |
| 2606.02302 | SeClaw | Candidate | 从安全 spec 生成任务并保留验收边界，改变 Agent security evaluation contract。 |
| 2606.02373 | Harness-1 | Candidate | 将搜索状态外置到 harness，改变 Agent 与 environment 的状态 ownership。 |
| 2606.02430 | LLM inference error propagation | Candidate | layer/operation/token/task propagation chain 改变故障注入与缓解评测。 |
| 2606.02437 | PEFT scaling | Candidate | million-personal-model deployment 改变 adapter state、存储与服务 ownership。 |
| 2606.02483 | Ghost Tool Calls | Candidate | proposal/issue/execution 分权揭示 issue-time privacy 不可撤回边界。 |
| 2606.02540 | SkillHarm | Candidate | persistent skill 的 revision、reuse、revoke 与 sandbox 构成生命周期安全合同。 |

结果：44 Candidate，7 Close。

## 从旧 generic closure 恢复（66）

以下条目均在完整 abstract 中给出了可迁移的控制、状态、执行、评测或发布变化；仅有模型名、局部性能或垂直任务的条目没有恢复。

| ID | 标题（缩写） | 题摘支持的长期 design delta |
| --- | --- | --- |
| 2606.00005 | Consilium Protocol | 多模型 disagreement、persona 与 out-of-sample evidence 的分权 deliberation 协议。 |
| 2606.00007 | Deliberative Curation | knowledge artifact lifecycle、commit-reveal voting 与 stateless-agent sanction。 |
| 2606.00021 | SENSE | retrieval speculative decoding 的语义导航、soft gate 与 target verification 边界。 |
| 2606.00024 | ART | KV 访问受限时以 attention runtime termination 控制 decode 工作量。 |
| 2606.00093 | LLM judge agreement metrics | scale、abstention、invalid output 与 pooling 的统一报告合同。 |
| 2606.00144 | BudgetDraft | verifier full KV 与 drafter sparse KV 的预算分权和 acceptance-aware training。 |
| 2606.00145 | CaB | 把任务完成判断变成 closed-loop switching interface，并显式校准。 |
| 2606.00150 | Persona Attack | 跨轮 memory injection 将安全边界从单 prompt 扩到会话状态。 |
| 2606.00152 | PrivacyPeek | 隐私审计从输出泄露前移到数据 acquisition 时刻。 |
| 2606.00160 | DataShield | benign fine-tuning 数据也进入 safety-degrading release gate。 |
| 2606.00198 | BAGEN | 将内部/外部 budget 从事后指标提升为 Agent 执行控制信号。 |
| 2606.00206 | Quantized reasoning | 量化导致 token inflation 而非仅 accuracy loss，修正部署评测合同。 |
| 2606.00279 | Bit-Exact inference verification | 用可复验执行消除 approximate-output 给对手留下的自由度。 |
| 2606.00376 | Deterministic Horizon | 给出 extended reasoning 到 tool delegation 的容量边界。 |
| 2606.00395 | PR2 | 以 routing replay 对齐 disaggregated rollout 与 training 的 MoE 状态。 |
| 2606.00448 | SkillReact | 单个安全 skill 的组合仍可能越权，要求安装集合级安全门禁。 |
| 2606.00485 | Cross-app context poisoning | first-party API 共享上下文改变 app 间数据与信任 ownership。 |
| 2606.00487 | TAPS | diffusion draft tree 以 target latency/acceptance 联合选择验证预算。 |
| 2606.00497 | Web-agent PII leakage | 将 deceptive content、敏感数据提交与防护缺失纳入部署安全门禁。 |
| 2606.00516 | Exclusive batching | prefill/decode interference 触发 mixed/exclusive batching 切换。 |
| 2606.00539 | GNMR | 低精度训练在 operator 级监控并切换 recoverable path。 |
| 2606.00566 | Tool-channel trust asymmetry | 相同 payload 因来源通道产生不同风险，要求 provenance-aware guardrail。 |
| 2606.00579 | Sandboxed coding agents | sandbox tool interface 可替代部分 native modality，修正执行 substrate 假设。 |
| 2606.00611 | TRACE | 长轨迹安全证据压缩改变 monitor state 与迟发风险聚合。 |
| 2606.00619 | MemPro | memory construction/retrieval pipeline 作为可演进程序而非固定组件。 |
| 2606.00642 | Reasoning trace exposure | 隐藏 raw trace 不等于保密，改变 reasoning API release boundary。 |
| 2606.00654 | Proactive availability backdoor | 攻击从被动 trigger 变为模型主动诱导，扩展上线威胁模型。 |
| 2606.00655 | MAS scaling behavior | 固定模型后隔离 agent count，给协作规模的评测边界。 |
| 2606.00669 | NeuroLog | LLM 只抽取 typed facts，Datalog/SMT 持有可审计验证 ownership。 |
| 2606.00674 | Outcome optimization shortcut bound | 对 outcome-only RL 的 shortcut 风险给出因果边界，修正 reward gate。 |
| 2606.00724 | WaveFilter | diffusion LLM long-context KV filtering 的误差/延迟 fallback 边界。 |
| 2606.00735 | ViBE | workload skew 与 GPU variability 联合进入 MoE placement/scheduling。 |
| 2606.00756 | CoMIC | cloud-edge Agent memory 的本地状态、共享 insight 与异构节点边界。 |
| 2606.00765 | FALAT | dependency-guided trajectory search 定位 first causal Agent/step。 |
| 2606.00801 | Quality-diversity red teaming | 以语义 attack archive 约束 coverage 与 mode collapse。 |
| 2606.00804 | Dynamic coordination selection | 按 problem class 选择 consensus/debate/synthesis/single-agent 控制路径。 |
| 2606.00813 | Cross-generational attacks | safety alignment 非单调，纠正“新版本默认更安全”的发布假设。 |
| 2606.00822 | SkillPager | 将 skill 文档解析为 typed nodes，按 execution-sufficient context 调页。 |
| 2606.00832 | Momento | multi-session memory benchmark 要求整合历史 action/preference/decision。 |
| 2606.00866 | MORI | 用 tool-call idle window 决定 KV offload/prefetch ownership。 |
| 2606.01801 | MetaForge | tool retrieval/adaptation/forging 构成受控工具生命周期。 |
| 2606.01813 | Cost-aware draft trees | 以 target verification cost 而非仅 acceptance length 选择 draft tree。 |
| 2606.01815 | CRAB-Bench | constraint graph、realistic user simulation 与多解验收改变 Agent eval。 |
| 2606.01828 | Trust-aware sparse topology | 信任与通信成本共同决定多 Agent 动态拓扑。 |
| 2606.01837 | Cross-modal jailbreak | 分散到多模态的 benign fragments 可重组为 harmful intent，扩展 guardrail 边界。 |
| 2606.01969 | Trust-calibrated code review | LLM 多文件变更需要 end-to-end 人审与工具 release workflow。 |
| 2606.01991 | SafeMCP | environment-grounded look-ahead 在 tool issue 前限制 Agent power。 |
| 2606.01993 | MMG2Skill | human guide 到 executable skill 的抽取、验证与演进边界。 |
| 2606.02011 | Extreme low-bit reasoning | 2-bit 量化的 trace inflation 使 per-token 加速不等于端到端加速。 |
| 2606.02031 | OpenWebRL | online multi-turn web-Agent RL 的 rollout/environment/training 基础设施。 |
| 2606.02041 | SentGuard | sentence-level streaming moderation 平衡语义完整性与干预延迟。 |
| 2606.02109 | BADGER | deterministic execution 与 generative judge 分层，形成 enterprise-agent eval contract。 |
| 2606.02240 | AgentRedBench | integration-specific dynamic attacks 与 defense placement 构成 SaaS Agent 门禁。 |
| 2606.02245 | Cost-aware RAG | evidence access tier 与预算成为检索决策的一等约束。 |
| 2606.02282 | POIROT | 通过 interrogation 分散多 Agent failure judgment，避免中心单点。 |
| 2606.02304 | Unified Context Evolution | 对经验分型、质量跟踪与跨 episode context 更新建立统一状态合同。 |
| 2606.02357 | Tool-use gain attribution | tool-call trace 不证明工具贡献，要求 answer-critical attribution。 |
| 2606.02359 | Multi-order communication | 从邻居响应拼接转为多阶消息传递，改变多 Agent communication state。 |
| 2606.02380 | SPADE-Bench | 以 plan-action divergence 检测 Agent 自述与执行分离的 deception。 |
| 2606.02423 | Harm amplification | 安全评测从单响应扩到多轮能力放大与规模化操作。 |
| 2606.02449 | HLL | CAPTCHA 作为外部验证 ownership，界定 Agent 不得自行跨越的上线边界。 |
| 2606.02461 | AgentCL | task stream、experience reuse 与 interference 构成 continual-Agent eval。 |
| 2606.02470 | MCP-Persona | personal-app environment simulation 纳入隐私状态与工具副作用。 |
| 2606.02494 | Pre-reliability monitoring | 先检查结构 wiring 再看 task error，改变早期 Agent 上线监控顺序。 |
| 2606.02536 | Behavioral trajectories | skill/memory/config file 版本变化与 Agent 行为轨迹建立可审计绑定。 |
| 2606.02544 | SimSD | 为 diffusion LM 定义与 mask semantics 一致的 speculative verification。 |

## 维持关闭（1,332）与旧候选降级（7）

全量 title sweep 后，边界项读取完整 abstract；排除理由不再使用“看起来没有系统增量”的统一模板。关闭项按互斥 family 计数如下：

| Closure family | 数量 | 可判定理由与反例抽检 |
| --- | ---: | --- |
| Embodied/local task method | 78 | 机器人、自动驾驶、具体控制器或单一 VLA/VLM 任务内改进；没有跨 workload 的状态/执行合同。抽检 `2606.00008` 的分子优化 multi-agent 与 `2606.02562` 的机器人 safety filter 均绑定垂直环境。 |
| Incremental model/method without durable contract | 1,046 | 局部表示、adapter、单一生成/训练技巧或架构名；没有 owner/control/release 变化。该组含降级的 00942/00944/00981/00997/01128；也包括经 abstract 复核后关闭的 Loopzero、MOSAIC data-science、generic multi-agent conformal prediction、AI-MCU 与 replication-package agent。 |
| Local benchmark without transferable release delta | 50 | 单一任务或模态 benchmark 只增加分数/数据集，未改变通用验收合同；含降级的 RoboTrustBench。 |
| Theory without AI-system contract | 24 | 优化、统计、控制或小网络理论，没有大模型系统对象或可迁移系统结论。 |
| Vertical application without system delta | 141 | 医疗、金融、科学、工业、湖仓等单一领域应用；含降级的 Lakehouse Agents。 |

合计 1,339 Close，与 110 Candidate 共同覆盖 1,449 个身份。

## Fresh-context FP/FN 独立抽检

| 抽检方向 | 样本 | 结果 |
| --- | --- | --- |
| Candidate false-positive challenge | 00946、01019、01065、01138、01387、01502、01751、01839、01927、02483 | 10/10 的 abstract 均能指出明确的 routing、verification、KV、wire-format、scheduling 或 issue-time ownership；保留。 |
| Candidate boundary challenge | 00145、00376、00579、00674、01969、02109、02449、02470、02494、02536 | 10/10 不是因对象名纳入；分别依赖 closed-loop switch、delegation bound、sandbox substrate、reward bound、review workflow、分层验收、外部验证、环境副作用、监控顺序、配置版本绑定。 |
| Close false-negative challenge | 00008、00329、00708、00717、00750、01600、01886、02006、02358、02562 | 10/10 完整 abstract 仍绑定分子/递归告警/数据科学/通用 conformal/scientific web/机器人/金融/研究包/edge MCU/机器人 safety 等局部对象，未达到跨 workload 系统合同门槛。 |

独立抽检没有发现需要继续扩查的新共享错误 family。当前 110-item denominator 因此冻结；后续只重开候选级 evidence/Books，而不再用旧 28/51 总数改写分母。
