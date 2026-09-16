# 2026-06-02 V3 Evidence Batch 02

本批只处理当前 V3 题摘准入后从旧 closure 恢复的十项候选。公开时间沿用 2026-06-02 官方 arXiv announcement batch 的北京时间范围；下列 Method、Evaluation 与 non-proof 均绑定 exact v1。Books 处置只比较当前 Review notes 前正文，不继承旧 Daily 或 trace 标签。

## Candidate evidence

### 2606.00497 — “I Strongly Suspect This Website Is a Scam”: Benchmarking PII Leakage and Detection without Defense in Autonomous Web Agents

- Primary / exact-v1: <https://arxiv.org/html/2606.00497v1>。
- Method: §3 冻结攻击者可控 web origin、四级 PII profile、91 个攻击环境与 10 个 benign twins；primary outcome 不是“是否点击”，而是 critical-tier field 是否实际到达 attacker-controlled POST endpoint。§3.4 另把 reasoning 中是否表达怀疑作为 observation，而不把它当作 action gate。
- Evaluation: §4 在四个模型家族、四种 prompt mitigation、每个 environment/model/condition 五个 seed 上比较 field-level leakage，并用 paired siblings 隔离 attack factor；detection–action gap 直接检验“识别风险”是否阻止提交。
- Non-proof: §7 与附录把结论限制在 synthetic/self-hosted English 环境、固定 PII profile、四个当时模型和 consumer-default no-confirmation harness；LLM judge 只测 verbalized suspicion，不能推断内部 knowledge，benchmark 也没有实现 production output interceptor。
- Books comparison: `PLATFORM-SECURITY` 当前正文已把 proposal、authorization、issue、execution 与 observation 分 owner，并明确 external call 在 issue-time 已可造成不可逆泄漏；这已经覆盖 field-level endpoint outcome 与“reasoning monitor 不能授予提交权限”的长期合同。该文提供更强评测实例，不新增正文，判 `已有覆盖`。

### 2606.00516 — Threshold-Based Exclusive Batching for LLM Inference

- Primary / exact-v1: <https://arxiv.org/html/2606.00516v1>。
- Method: §3–§5 建模 prefill/decode 在 mixed batching 与 exclusive batching 下的 compute、bandwidth 和 slot occupancy，推导硬件/模型/workload 相关 crossover，并以在线 threshold 在两种 phase policy 间切换，同时约束 memory-safe batch size。
- Evaluation: §6–§7 在不同 GPU bandwidth、模型规模、请求分布与并发变化下比较 EB、MB 与 hybrid EB+ 的 throughput/latency；证据支持 workload-dependent phase switch，而不是普遍优于 mixed batching。
- Non-proof: 分析依赖论文中的 kernel/runtime cost model、饱和条件与请求分布；高带宽硬件和更大模型仍可使 MB 占优，离线 threshold 也不能证明生产 tail/SLO 或任意 engine 集成。
- Books comparison: `INFER-SCHEDULING` 当前正文已有“Exclusive Batching 的 Phase Switch 是 Workload-dependent State”，包含 crossover、hardware/workload identity、memory boundary 与回退 mixed scheduling。判 `已有覆盖`。

### 2606.00539 — GNMR: Runtime Stability Control for Low-Precision Large Language Model Training

- Primary / exact-v1: <https://arxiv.org/html/2606.00539v1>。
- Method: §2–§4 将 transformer 分解为可监控 operator/block unit，用 operator-normalized risk、long/short-window signal 与有限 recovery budget 检测数值异常，并只把可恢复 unit 切到更稳健路径，而非全局永久提精度。
- Evaluation: §5 分开测 trigger quality、budget behavior、quality preservation 与工程开销，并跨训练 recipe/backend 配置验证 controller；这支持控制面机制，不证明任意低精度格式天然稳定。
- Non-proof: §6 依赖 backend 暴露足够 observability、unit 可恢复且存在兼容 recovery implementation；阈值和预算会随模型、recipe 与并行拓扑漂移，monitor overhead 也必须计入。
- Books comparison: `TRAIN-PRETRAINING` 当前正文已拥有 operator-normalized risk、长短窗口信号、limited recovery budget、recoverable-unit fallback 与 identity 失配拒绝。判 `已有覆盖`。

### 2606.00566 — Same Payload, Different Channel: Measuring Trust Asymmetry in Tool-Using Language Models

- Primary / exact-v1: <https://arxiv.org/html/2606.00566v1>。
- Method: §3–§4 构造 byte-for-byte 相同的 malicious payload pair，只改变 user-message 与 tool-description/tool-output wrapper，以 Source Attribution Score 隔离 channel 变量；另以 probe 与 causal activation patching 分析 channel-conditioned representation。
- Evaluation: §5 在六个 production LLM、98 个 matched cases 和三类攻击 family 上比较 asymmetry，并与外部 tool-poisoning benchmark 做 ranking replication；mechanistic 部分仅覆盖一个可访问权重模型。
- Non-proof: §6 的六模型样本不足以分离 agent-native training、model size 与 provider policy，tool description 和 tool output 的风险方向也不同；单模型 activation patch 不能外推其他架构或证明生产 guardrail 有效。
- Books comparison: `PLATFORM-SECURITY` 当前正文已要求 authenticated origin/principal/trust metadata、typed channel boundary、tool result 低信任与 effect-time reference monitor；相同 payload 不因 wrapper 获得 authority 已是正文 contract。判 `已有覆盖`。

### 2606.00579 — Sandboxed Coding Agents are Competitive Omni-modal Task Solvers

- Primary / exact-v1: <https://arxiv.org/html/2606.00579v1>。
- Method: §2–§3 让 text+image coding agent 在 sandbox 中把 audio/video 先落为 workspace state，再编排 ffmpeg、ASR、OCR 与自写代码提取证据；Code-X 用可验证 reward 与 OmniCoding trajectories 训练这种 tool orchestration。
- Evaluation: §4–§5 在多个 audio/video benchmark 比较 coding agents、native omni-modal model 和预定义 scaffold，并通过 process trace/failure taxonomy 分析收益来源；TerminalBench-O 仍是作者构建的 process benchmark。
- Non-proof: §6 只训练 9B/27B 开源模型，部分 frontier 对照不可完整复现；任务是 offline staged media，不覆盖 streaming、实时交互或真实 side effect，isolated sandbox 也不代表 production permission boundary。
- Books comparison: 论文说明 sandboxed tool transformation 能替代部分 native modality input，但长期设计仍落在现有 tool contract、workspace isolation 与 evidence provenance；在离线 benchmark 范围外没有形成新的跨 workload owner 机制。判 `仅报告`。

### 2606.00611 — TRACE: Trajectory Risk-Aware Compression for Long-Horizon Agent Safety

- Primary / exact-v1: <https://arxiv.org/html/2606.00611v1>。
- Method: §3 采用 Compressor–Reader 分工，把完整 long-horizon trajectory 编码为 bounded latent evidence state，再由独立 reader 判断 sparse、delayed 与 compositional risk；压缩对象是风险证据而非普通文本摘要。
- Evaluation: §4–§5 在 R-Judge、ASSEBench、Pre-Ex-Bench 等 trajectory-safety 数据与多个 backbone 上比较 full-context、SFT/summary 与 TRACE，并报告不同 latent budget、证据 regime、false-positive/false-negative case。
- Non-proof: §6/附录没有覆盖 production auth、rate limit、多用户 permission hierarchy 或不可逆 side effect；风险 taxonomy 与 label/judge 会漂移，latent state 不可直接人工审计，压缩遗漏时必须回到原轨迹。
- Books comparison / final: 差额已写入 `PLATFORM-MONITORING` 正文锚点“Risk-aware Latent 只能压缩 Evidence，不能压缩 Authority”；compressor/reader revision、source span、abstain 与 raw-trajectory fallback 均可定位。

### 2606.00619 — MemPro: Agentic Memory Systems as Evolvable Programs

- Primary / exact-v1: <https://arxiv.org/html/2606.00619v1>。
- Method: §3–§4 把 extraction、storage、retrieval 与 injection 组成的 MCR pipeline 作为可执行 program，由 evolver 基于 failure feedback 生成 edit/debug candidate，并以 version tree 保存可运行实现；held-out evaluator 决定是否提升新 revision。
- Evaluation: §5 在 long-memory 与 QA benchmarks 上比较固定 pipeline、局部组件优化和 system-level/tree evolution，并以 ablation 分离 inner/outer evolution 与 chain/tree search 的作用。
- Non-proof: §7 明示离线 evolution 成本高、依赖强 evolver 与 evaluator，当前只实现 tree topology；privacy/governance、sandbox、日志和 executable edit review 尚未闭合，judge/gold/eval contract 也被冻结而没有共同演化。
- Books comparison / final: 重读当前 `AGENT-MEMORY` 正文后改判 `已有覆盖`。命题“Memory policy 本身也可能成为可学习、可版本化的 procedural asset”已覆盖 executable extraction/update procedure、source episodes、held-out validation、versioned bank、provenance 与 rollback；其后 cluster-local tournament 又分离 proposer 与 release evidence。MemPro 的 tree evolution 是受限实现，不改变现有 owner contract。

### 2606.00642 — Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs

- Primary / exact-v1: <https://arxiv.org/html/2606.00642v1>。
- Method: §3–§5 用 Reasoning Exposure Prompting 将表面工具/代码任务包装为 trace extraction prompt，并以多轮 continuation 和 wrapper variants 提高暴露；安全问题是行为可被 prompt 重建，而不是只看 API 是否直接返回 raw trace。
- Evaluation: §5–§7 在作者可访问的 open-weight reasoning models 上比较 exposure、lexical/semantic similarity 与 distillation utility，并做 wrapper/degradation ablation。
- Non-proof: §9 只覆盖 open-weight/特定 prompt interface；相似输出和学生性能不证明 causal fidelity，closed system、不同 decoding 或未公开 trace policy 可能不同，隐藏接口本身也从未构成 secrecy proof。
- Books comparison: `PLATFORM-SECURITY` 当前正文已有“Hidden Reasoning Trace 不是 Secrecy Boundary”，明确 reasoning surface 只能是低信任 observation、secret 不得进入模型可读 context、输出仍需独立 DLP/authorization。判 `已有覆盖`。

### 2606.00654 — The Invitation Trap: Proactive Availability Backdoor in LLMs via Conversational Induction

- Primary / exact-v1: <https://arxiv.org/html/2606.00654v1>。
- Method: §3 将传统等待外部 trigger 的 backdoor 改为模型先利用 helpful suggestion 诱导用户在后续轮次输入 trigger，再执行 availability payload；dual-agent ecological simulation 显式建模 attacker-model 与 user interaction。
- Evaluation: §4 在多个模型、主题和三类 persona profile 上联合计算 attack incidence 与 trigger 后 success，并比较 few-shot deployment 与 Anti-PAB；人评只用于校验部分模拟判断。
- Non-proof: §6 只用粗粒度 persona、有限 domain，主要部署证据集中在一个闭源模型；模拟 user 不等于真实人类，73.1% 联合率不能外推 production incidence，防御也未经过长期 adaptive attack。
- Books comparison / final: 差额已写入 `PLATFORM-SECURITY` 正文锚点“模型建议也可能塑造未来 Trigger”；跨轮 lineage、independent confirmation 与同一模型不得自证自批均可定位。

### 2606.00655 — Scaling Behavior of Single LLM-Driven Multi-Agent Systems

- Primary / exact-v1: <https://arxiv.org/html/2606.00655v1>。
- Method: §3 以同一 base LLM 驱动 homogeneous agents，在 minimalist sequential communication 中只改变 agent count，并比较不同 task/model scale；附加 topology 对照检查结论是否只是某一通信形态造成。
- Evaluation: §4 在 agent count 1–8、若干 closed-book QA/reasoning task 与不同模型规模上观察 inverted-U/diminishing-return，并将 degradation 分解到 coordination overhead 而非仅 long-context failure。
- Non-proof: §5 只覆盖 homogeneous team、有限 agent 数、简化 coordination 和 output accuracy；没有 heterogeneous role、tool side effect、production latency/cost 或开放环境，最优 K 不能跨 task/model revision 继承。
- Books comparison: `AGENT-MULTI-AGENT` 当前正文已明确 agent 数量不单调改善，并用 single-agent headroom、branch diversity、sequential repair、aggregation/verification cost 与 coordination tax 决定是否扩 K，且要求 single-agent fallback。判 `已有覆盖`。

## Batch result

- Evidence closed: 10 / 10。
- Books: 7 `已有覆盖`，2 `整合已写入`，1 `仅报告`，0 `整合 proposal`，0 `暂缓`。
- Proposal queue: 空。2606.00611、2606.00654 已完成正文绑定；2606.00619 经正文重读改判 `已有覆盖`。
- 写入后按当前 owner 正文复核；未发现重复合并或 trace 代替正文。
