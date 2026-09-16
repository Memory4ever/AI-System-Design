# 2026-06-02 V3 Evidence Batch 03

本批处理十项当前 V3 存续候选。公开时间使用 2026-06-02 官方 arXiv announcement batch 的北京时间范围；Method、Evaluation 与 non-proof 只绑定 exact v1。Books 处置以本轮读取的 Review notes 前正文为准，trace 与旧 Daily 标签不参与授权。

## Candidate evidence

### 2606.00669 — NeuroLog: Reasoning You Can Audit — Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT

- Primary / exact-v1: <https://arxiv.org/html/2606.00669v1>。
- Method: §4–§5 将 LLM 限制为逐函数 typed fact extractor，机械 parser 提供结构事实，Datalog rule mesh 组合跨函数 dataflow，Z3 post-pass 只验证候选路径并输出 SAT witness；第二个 LLM 只能据 witness 提议 crash input，由 ASan harness 决定是否成立。
- Evaluation: §7 在 stb、cJSON、libxml2、FFmpeg、curl 与 libarchive 上报告 CVE rediscovery、new finding、smell-pass cost、symbolic filters 和 crash synthesis，同时保留 honest negatives 与未 triage backlog。
- Non-proof: §8.1 明示 LLM 可能静默漏 fact、compile-free 路径看不到 preprocessor/type information、rule mesh coverage 有限，只测一个 provider 且没有与 CodeQL/Joern 做同目标 head-to-head；ASan 只验证可触发的特定 failure。
- Books comparison: `PLATFORM-SECURITY` 当前正文已将 vulnerability hypothesis、deterministic reproduction、sanitizer gate 与 disclosure 分层，也已有 typed fact base + Datalog/deterministic policy 路径；模型不能拥有 finding truth 或 release authority。判 `已有覆盖`。

### 2606.00674 — The Paradox of Outcome Optimization: A Causal Information-Theoretic Bound on Reasoning Shortcuts in LLMs

- Primary / exact-v1: <https://arxiv.org/html/2606.00674v1>。
- Method: §2–§4 用 Information Bottleneck、结构因果图与 algorithmic complexity 描述 outcome objective 对 reward-sufficient low-complexity shortcut 的偏好，并把 process verifier 解释为阻断 shortcut trajectory 的 topological filter。
- Evaluation: §5 在 Qwen2.5-3B/7B、Llama-3-8B 与 rule-reversal counterfactual tasks 上比较 outcome/process supervision 的 ID/OOD behavior，检验 shortcut/causal feature 的预测，而非只报告训练 loss。
- Non-proof: Limitations 限定小模型和人工 counterfactual task；真实 shortcut 未必二元，理论依赖可验证 intermediate step，构建高保真 process signal 昂贵且在开放任务中可能不可定义。
- Books comparison: `TRAIN-GRPO` 当前正文已明确 outcome-only verifier 可能奖励 shortcut、process reward 只能提供局部信号且引入 evaluator exploit，终局 outcome 与 fallback 仍保留；该理论为既有 trade-off 提供解释，不改变 owner contract。判 `已有覆盖`。

### 2606.00724 — WaveFilter: Enhancing the Long-Context Capability of Diffusion LLMs via Wavelet-Guided KV Cache Filtering

- Primary / exact-v1: <https://arxiv.org/html/2606.00724v1>。
- Method: §3 对 KV/cache-derived token signal 做多尺度 wavelet decomposition，在低维空间递归筛选高相关 token，再把保留集合交给既有 diffusion-cache path；它是 training-free selector，不拥有最终质量 admission。
- Evaluation: §4 在 LongBench、RULER、不同 compression scale/proportion 和 diffusion LLM/cache baseline 上同时测 quality、throughput 与 total runtime，并做 selector/budget ablation。
- Non-proof: §6 说明 perceptual-weight attention 计算有额外开销，throughput 会与 total runtime/quality 给出不同结论；只覆盖作者 diffusion model、task 与配置，不能外推连续 batching、其他 kernel 或 production tail。
- Books comparison: `INFER-KV-CACHE` 当前正文已要求 token-utility selector、layer/head budget、model/workload revision、quality regression、diffusion loop cache-drift bound 与 FullKV/recompute fallback。Wavelet 是局部 proxy 实例，判 `已有覆盖`。

### 2606.00735 — ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving

- Primary / exact-v1: <https://arxiv.org/html/2606.00735v1>。
- Method: §3–§4 用 per-GPU measured performance function 将 expert token magnitude 与 device effective throughput 映射为 latency，再联合优化 expert placement；drift detector 根据 routing/load vector 触发局部 recalibration，而不是固定周期全量搬迁。
- Evaluation: §5 在 MoE serving、异构/扰动 GPU performance、不同 batch/token distribution 与 execution phase 上比较 token-balanced 与 latency-balanced placement，并报告 imbalance、SLO attainment、P90 TTFT 和 recalibration overhead。
- Non-proof: 性能函数、routing profile 与 drift threshold 绑定披露硬件/模型/runtime；预测误差、迁移成本和控制震荡可能抵消收益，论文结果不证明任意故障/跨节点网络或生产 workload 都能补偿。
- Books comparison: `INFER-SCHEDULING` 当前正文已要求 expert placement 同时消费 routing skew、measured service rate、device variability、迁移频率与 execution epoch，并在 drift/solver 失效时回退静态 placement。判 `已有覆盖`。

### 2606.00756 — CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents in Cloud-Edge Systems

- Primary / exact-v1: <https://arxiv.org/html/2606.00756v1>。
- Method: §3 采用 Centralized Reflection / Decentralized Execution：edge agent 保留 subgoal-oriented local history 并按需 re-expand，cloud critic 异步评估 completed trajectories、过滤可复用 experience，再以 semantic subgoal ID 聚合跨 edge guidance；参数不在线更新。
- Evaluation: §4 在两类 long-horizon 场景、不同 edge/cloud 配置上比较 local memory、cloud reflection 与 full CoMIC，并分别测 progress、grounding、success、context saving 和组件消融。
- Non-proof: §5 明示弱 edge model 仍可能无法产生 viable subgoal 或理解 guidance；收益依赖 critic admission、dispatch precision 与 normalization，部分 task 保持零成功，未覆盖多租户隐私、staleness、断连或 production bandwidth/SLO。
- Books comparison / final: 已写入 `AGENT-MEMORY` 正文“Edge-local Episode 与 Cloud-derived Guidance 必须分离所有权”，明确 local episode authority、cloud-derived guidance revision、subgoal key、dispatch receipt、tenant/expiry boundary 与断连时 local-only fallback；派生 guidance 不取得事实或 action authority。

### 2606.00765 — FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search

- Primary / exact-v1: <https://arxiv.org/html/2606.00765v1>。
- Method: §2 先构造 expected solution/search space，再把 decision、tool output 与 agent message 组织为 typed dependency graph；候选 narrowing 后通过“纠正该步是否足以恢复 outcome”的 counterfactual objective 区分 first causal error 与后继传播，并做 local adversarial re-search。
- Evaluation: §3–§4 在 Who&When 的 algorithm-generated 与 hand-crafted multi-agent failure trajectories 上比较 responsible-agent/decisive-step accuracy，并消融 hierarchy、transition typing 与 local re-search。
- Non-proof: §5 依赖多处 LLM judgment，window processing 可能漏 long-range dependency，并假设 failure 可局部化；多个相互作用错误时单步修正不构成因果证明，受控 benchmark accuracy 也不代表生产 prevalence。
- Books comparison: `PLATFORM-TRACE` 当前正文已要求从阶段异常升级到可证伪因果候选，以 dependency、replay/intervention/counterfactual 验证 first harmful commitment，证据不足保留 multiple candidates。判 `已有覆盖`。

### 2606.00801 — Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety

- Primary / exact-v1: <https://arxiv.org/html/2606.00801v1>。
- Method: §2 用 semantic genome 表示 strategy、encoding、length 等可解释攻击维度，以 MAP-Elites 同时优化 fitness 与 archive coverage，避免单一 LLM attacker 在少数 prompt mode 中收敛。
- Evaluation: §3 在四个模型上固定 population/generation budget，比较各 archive cell 的 coverage、best attack 与 model-specific vulnerability profile；输出是可重放策略 archive，而不是只有最高 ASR。
- Non-proof: §4 的拒绝短语 judge 约有 12% 误判且不区分 harm severity，演化预算仅 30×30、seed payload 单一，所谓 multi-turn 仍是单次结构包装；未覆盖真实 Agent tool/state 或 adaptive production adversary。
- Books comparison / final: 差额已写入 `PLATFORM-SECURITY` 正文锚点“Semantic Archive 暴露 Mode Collapse，但不拥有 Release Verdict”；archive coverage、mutation lineage 与独立 scorer/human gate 均可定位。

### 2606.00804 — Dynamic Coordination Strategy Selection for Enterprise Multi-Agent Systems

- Primary / exact-v1: <https://arxiv.org/html/2606.00804v1>。
- Method: §3 冻结 problem-class × coordination-condition × model-arm matrix，在 consensus、debate、synthesis 与 single-agent 间进行 class-conditioned routing；论文把 predicted route 降格为 near-best heuristic，而非固定 winner law。
- Evaluation: §4 在六行业、五 problem classes、四执行条件、多个 model arms/replications 上比较 quality，并用 auxiliary judge arm 与预注册统计检验 exact-winner、near-best 和 language-stratum claim。
- Non-proof: §7 明示 fixed Sonnet judge bias、task corpus/strategy implementation 有限，second judge 相关性仅中等；30 个 enterprise tasks 不覆盖 latency、cost、tool side effect 或真实组织 workflow。
- Books comparison: `AGENT-MULTI-AGENT` 当前正文已按 decomposability、evidence independence、tool coupling、budget 与 coordination tax 选择 singleton/debate/selection/synthesis，并要求 equal-budget Pareto admission 和 single-agent fallback。判 `已有覆盖`。

### 2606.00813 — Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs

- Primary / exact-v1: <https://arxiv.org/html/2606.00813v1>。
- Method: §3 对每代模型独立生成 quality-diversity attack archive，再做 forward/backward cross-generational replay；release subject 同时绑定 target generation、attack archive revision、judge 与 seed。
- Evaluation: §4–§5 在四代 Gemma、三 seeds、统一 self-hosted judge 上比较 baseline ASR、cross-generation transfer 与 vulnerability fingerprints，并做 second-judge sensitivity。
- Non-proof: §6 仅一个模型家族、三 seeds，部分差异未达显著；copyright slice 对 judge 选择敏感，静态/自适应 archive 仍不能穷尽攻击面或证明某代绝对安全。
- Books comparison: `PLATFORM-EVALUATION-SYSTEM` 当前正文已要求 capability/safety result 绑定 model release、elicitation、scaffold、评测日期、artifact 与 evaluator，并禁止旧证据跨 revision 自动继承；Security 也要求每次 remediation 重跑受影响 regression。判 `已有覆盖`。

### 2606.00822 — SkillPager: Query-Adaptive Intra-Skill Navigation via Semantic Node Retrieval

- Primary / exact-v1: <https://arxiv.org/html/2606.00822v1>。
- Method: §3 离线把已知 Markdown skill 解析为 typed semantic nodes，在线用 MMR 做 query-conditioned global selection，再补齐 supporting/dependency nodes 并动态调整 context budget；目标是 minimal execution-sufficient context，而非整篇注入。
- Evaluation: §4–§5 在 395 skills、1,975 synthetic queries 上比较 full document、naive chunks 与 graph/node variants，并以 human subset 校验 LLM-judged context sufficiency、报告 token Pareto 与 parser ablation。
- Non-proof: §6 未测下游 execution success，只用 easy partition、单 embedding family 和 synthetic queries；预先假设已知正确 skill，不覆盖 routing/multi-skill composition，离线 parser 成本与错误 node 也会随文档 revision 失效。
- Books comparison: `AGENT-MEMORY` 当前正文已把 hierarchical Skill 视为 query decomposition/compositional retrieval plan，并要求 provenance、schema、applicability、tool identity 与 flat-skill fallback；`AGENT-CONTEXT` 也要求 dependency facts 与定点检索。SkillPager 是该 contract 的局部实现，判 `已有覆盖`。

## Batch result

- Evidence closed: 10 / 10。
- Books: 8 `已有覆盖`，2 `整合已写入`，0 `整合 proposal`，0 `仅报告`，0 `暂缓`。
- Proposal queue: 空。2606.00756、2606.00801 均已完成正文绑定。
- 写入后按当前 owner 正文复核；未发现重复合并或 trace 代替正文。
