# 2026-06-02 V3 Evidence Batch 07

本批处理最后八项从旧 closure 恢复的 V3 候选。公开时间使用 2026-06-02 官方 arXiv announcement batch 的北京时间范围；Method、Evaluation 与 non-proof 绑定 exact v1。`2606.00005v1` 无 arXiv HTML，故以官方 exact-v1 PDF 为正文证据；其余使用官方 exact-v1 HTML。Books 处置只由当前 owner 正文支持。

## Candidate evidence

### 2606.00005 — Emergent Collaborative Deliberation in Multi-Model AI Systems: A BFT-Derived Protocol for Epistemic Synthesis

- Primary / exact-v1: <https://arxiv.org/pdf/2606.00005v1>。
- Method: §3 将 PBFT 的 coordinator/round/view-change 结构改造成 Consilium deliberation，由 human moderator 保留 override，按 model×cognitive-persona 随机分配角色，并把 In-Sample deliberation 与 Out-of-Sample live-evidence validation 分成两条证据通道；输出保存被挑战的 claim chain，而非多数结论。
- Evaluation: §4–§6 比较 single frontier、single+search、multi-model panel 与 edge models+search，并在 1,478 sessions、32 topics、10 domains 上报告 challenge coverage、blind-spot discovery、cost 与随机 model×persona assignment 的 run-to-run variation。
- Non-proof: engineered persona 不等于统计独立，训练语料重叠、search source 共因与 moderator bias 仍会形成 correlated error；作者的 challenge/bias 指标和 239 条检索不证明 claim truth、BFT safety、开放领域覆盖率或自动 commit authority。
- Books comparison: `AGENT-MULTI-AGENT` 当前正文已明确 persona 不创造独立能力、deliberation 应保存初始 evidence/消息/终局保留率、共识不能替代独立 outcome evidence，且错误相关时回退异构 verifier/人工。Consilium 是该 contract 的具体 composition，判 `已有覆盖`。

### 2606.00007 — Deliberative Curation: A Protocol for Multi-Agent Knowledge Bases

- Primary / exact-v1: <https://arxiv.org/html/2606.00007v1>。
- Method: §2–§4 将知识 artifact 建模为 proposed→under_review→active→disputed→superseded/retracted 的 guarded LTS，由不参与投票的 orchestrator 提交 transition；review 依次使用 absence-of-objection、formal vote 与 arbitration，并把 reputation、timeout、dispute bound、commit-reveal 与 stateless-agent sanction 写成协议状态。
- Evaluation: §5 用 100 个、七种行为 archetype 的 simulated agents 比较 majority vote，并在两种 adversity 下测 precision、resilience、fairness、liveness 与组件 ablation；另以 Community Notes 作受限一致性回放。
- Non-proof: structured deliberation、graduated sanctions 与部分 broken-agent handling 未被完整实验；simulation archetype、Beta/EigenTrust 和 outcome labels 不代表真实 Agent population。Reputation 不能证明事实，model homogeneity、sycophancy 与 source hallucination 仍会击穿投票。
- Books comparison: `AGENT-MEMORY` 已有 pending/active/superseded/rejected、provenance、争议与撤销传播；`AGENT-PLATFORM` 已有 admit/supersede/reject/rollback 与独立 promotion gate；`AGENT-MULTI-AGENT` 已要求 reputation 按 skill 条件化、保存 zero-evidence，并禁止 consensus 自证。该协议组合没有新增 owner contract，判 `已有覆盖`。

### 2606.00145 — Completion at the Boundary (CaB): Deployable Switching with Completion-Aware Control under Limited Calibration

- Primary / exact-v1: <https://arxiv.org/html/2606.00145v1>。
- Method: §4–§5 预测 Before/Hit/After Boundary-Phase Token，CaB-When 用冻结的 global rule 决定是否把 composite instruction 前移一段，CaB-How 让 action 单向读取同一步 phase posterior，禁止 action 反向泄漏到 completion decision。
- Evaluation: §6 与附录在 Minecraft 的 32 single tasks、18 two-stage composites 上区分共享 rollout-bank 的 E1 与 closed-loop switching 的 E2；固定 PaliGemma-3B、dev-only calibration、single global rule，并报告 bootstrap interval 和 handoff/action ablation。
- Non-proof: 单一 Minecraft/VLA substrate、单 seed、有限 task group 与 frozen calibration 不证明开放 GUI、真实机器人、长 workflow 或跨 domain polarity；completion posterior 是 sensor，不是外部 state truth，错误切换会改变后续 observation。
- Books comparison: `AGENT-WORKFLOW` 当前正文已要求 bounded completion packet、只读 verifier、state revision/acceptance criteria 与 owner commit，并要求 handoff 保留 prerequisite、authority、fallback 和 execution consequence。CaB 的 BPT/readout 是受限 VLA implementation，判 `已有覆盖`。

### 2606.00150 — Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models

- Primary / exact-v1: <https://arxiv.org/html/2606.00150v1>。
- Method: §3 将 benign-seeming persona instructions 分步注入 manual transcript memory 或 state-based memory，让后续 harmful query 继承累计 context；攻击变量是 instruction combination、顺序与 memory implementation，而非单一 prompt。
- Evaluation: §4 与附录在多种开源/商用 LLM、60 个 harmful questions、不同 persona combinations 和 memory implementations 上报告 ASR/FAR，并给出真实聊天产品的受限测试。
- Non-proof: attack taxonomy、自动判定、模型版本和手工/state-based memory 实现限制结论；特定组合的高 ASR 不代表生产发生率，披露有害输出也不证明真实 side effect。模型更新、system policy 或 conversation truncation 会改变结果。
- Books comparison: `PLATFORM-SECURITY` 当前正文已要求跨 iteration 保留不可由 Agent 清零的 trajectory risk state，并把 prompt、memory write、action/effect 与独立 stop/authorization gate 串联；单轮 guard 不拥有最终 authority。判 `已有覆盖`。

### 2606.00160 — DataShield: Safety-degrading Data Filtering for LLM Benign Instruction Fine-Tuning

- Primary / exact-v1: <https://arxiv.org/html/2606.00160v1>。
- Method: §IV 从 checkpoint 抽取 compliance direction，用 CAS 选择 safety-critical layer，并按每个 benign sample 在该方向上的 projection shift 过滤可能导致 safety degradation 的训练数据。
- Evaluation: §V 在 Llama3/Llama3.1/Qwen2.5、Alpaca/Dolly、三种 safety benchmark 上比较过滤器，评估 sample selection、过滤后安全、layer selection、projection 与排序成本。
- Non-proof: compliance direction、critical layer 与 threshold 会随 checkpoint、adapter、数据顺序和 policy 漂移；投影相关性不是因果证明，过滤会误伤 benign diversity，不能替代训练后 held-out safety regression。
- Books comparison: `TRAIN-DATA` 当前正文已以本篇 exact-v1 明确写入“内容无害不等于更新无害”的 training-effect filter，保存 checkpoint、layer、projection、threshold、admission lineage 与 canary/回归 fallback。判 `已有覆盖`。

### 2606.00198 — BAGEN: Are LLM Agents Budget-Aware?

- Primary / exact-v1: <https://arxiv.org/html/2606.00198v1>。
- Method: §3 先生成不受预算约束的完整 trajectory 与 per-turn cost，再逐 prefix 回放并让同一 Agent 预测剩余 budget interval 和是否仍可完成；将能力拆成 feasibility、early failure detection 与 interval calibration，并用估计驱动受 hard cap 约束的 early-stop policy。
- Evaluation: §4–§6 在五个 frontier models、四种环境上覆盖 token、money、time、warehouse space，并在 Qwen-7B 上用 SFT/RL 训练 estimator；报告 coverage/tightness/error、cross-task retention、token savings、success loss 与 false abort。
- Non-proof: offline prefix replay 避开了在线自评成本与干预效应；训练后的 interval 仍频繁漏真值，cross-task 只保留有限收益。Agent 自报不是真实 resource meter，错误 early stop 会牺牲困难任务，不能绕过 hard budget、verification reserve 或 outcome gate。
- Books comparison: `AGENT-PLANNING` 已把 remaining time/token/tool/cost、uncertainty、feasibility 与 stop/fallback 组成 belief state，并要求 hard cap、verification reserve 和 slice calibration；`AGENT-PLATFORM` 已要求 stop controller 保存 terminal reason/evidence，禁止 self-report 直接提交。判 `已有覆盖`。

### 2606.00206 — Quantized Reasoning Models Think They Need to Think Longer, but They Do Not

- Primary / exact-v1: <https://arxiv.org/html/2606.00206v1>。
- Method: §3–§5 比较 full-precision 与多种 PTQ 的 token-level KL/entropy，定位量化模型在已出现中间正确答案后采样“wait/but/alternatively”等 overthinking markers 的 failure；以 training-free logit penalty 抑制这些 markers。
- Evaluation: 五个 1.5B–32B models、三种 quantization methods、五个 math/coding/science benchmarks 上联合报告 accuracy、CoT length、intermediate-correct/final-wrong slice 与 marker/high-KL/random-token penalty ablation。
- Non-proof: curated marker list、temperature、reasoning format、model family 与 benchmark 限制外推；logit penalty 会改变输出分布，不能证明所有 extra reasoning 都无益，也未验证 production batching、tail latency、termination safety 或高风险答案正确性。
- Books comparison: `INFER-GPU-MEMORY` 当前正文已明确低比特可能用更多 reasoning tokens 抬高总成本，要求以完成任务的 memory/latency/energy/quality 而非压缩比验收；`INFER-DECODE` 已有 request-local overthinking detector 与 exit/logit/jump intervention。Marker penalty 是局部实现，判 `已有覆盖`。

### 2606.00376 — The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary

- Primary / exact-v1: <https://arxiv.org/html/2606.00376v1>。
- Method: §3–§4 以 state-space depth、context-dependent error 与 attention entropy 建立所谓 deterministic horizon，再比较 unrestricted/depth-limited CoT、deterministic solver tool、length encouragement 与 trace fine-tuning；系统结论是超过可可靠跟踪深度后把可形式化 state transition 委派给外部工具。
- Evaluation: §5–§6 在 12 models、五种 conditions、八类 synthetic/real tasks 上比较 accuracy decay、tool delegation、fine-tuning、attention entropy 与 failure taxonomy，包含 SWE-Bench-State、WebArena-Nav、SQL-Multi 和多次运行。
- Non-proof: theorem 依赖作者的 context-error/independence/attention assumptions，BFS solver 还是带答案结构的强 oracle；任务深度、模型版本与 tool interface 限制所谓 horizon，不能证明 transformer 的普适架构上界或任意现实任务都应调用工具。
- Books comparison: `AGENT-PLANNING` 当前正文已分离 semantic plan、deterministic feasibility/solver、execution evidence 与 replanning；`AGENT-TOOL-CALLING` 已明确内部 recurrent reasoning 不能替代带 observation、authorization 和 effect receipt 的外部 tool protocol。论文的强理论外推不改变这条长期边界，判 `已有覆盖`。

## Batch result

- Evidence closed: 8 / 8。
- Books: 8 `已有覆盖`，0 `整合 proposal`，0 `仅报告`，0 `暂缓`。
- 66 个从旧 closure 恢复的候选至此全部完成当前 candidate-level Evidence 与 Books comparison；本批没有新增 Books 写入队列。
