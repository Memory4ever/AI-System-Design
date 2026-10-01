# 2026-09-18 exact-version Source Review notes

本文件是当日 56 个冻结候选与 1 个重要修订的逐项证据索引。`采用命题` 是进入 Daily/Books 判断的最窄结论；`未证明` 用于阻止把作者实验外推为通用机制。所有 arXiv 条目均审阅所列 exact version。

## 模型、训练与评价

- **2609.17542v1 — Register Bias in Complexity-Based Large Language Model Routing**
  - 采用命题：complexity router 需要把 language register 当作 fairness/cost slice，而不能只校准平均难度。
  - Method：§III-A～III-E；Evaluation：§IV、§V；未证明：§VII 不证明所有 router、语言或模型有同等偏差。
  - 处置：已有覆盖 `INFER-SCHEDULING`。
- **2609.17560v1 — Pay Only for Disagreement**
  - 采用命题：模型更新可先定位新旧模型的 disagreement support，再用 anytime-valid confidence sequence 给 no-regression verdict。
  - Method：§3、§4.1～4.2、§5.1；Evaluation：§6.1～6.6；未证明：§8，依赖有界 loss、可观测配对预测、slice 与 routing identity。
  - 处置：整合 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.17848v1 — SFT or RL for Tool-Calling Agents?**
  - 采用命题：SFT/GRPO 的选择受 backbone、数据与 tool task 约束，不存在脱离 evaluation contract 的固定排名。
  - Method：§3.1～3.3；Evaluation：§4.1～4.2；未证明：Limitations 与 Appendix A，不覆盖任意工具空间和线上行为。
  - 处置：已有覆盖 `TRAIN-GRPO`。
- **2609.17857v1 — Who Judges Matters**
  - 采用命题：judge family-conditioned preference 不会因增加同源 judge 数量自动消失。
  - Method：§3、§4.1～4.2；Evaluation：§5～§9；未证明：Limitations，不证明 human truth 或任意模型族的偏差方向。
  - 处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.17930v1 — Locating Hidden Failures Makes Long-Horizon Agents More Reliable**
  - 采用命题：long-horizon evaluation 应把 failure localization 与最终 success 分开。
  - Method：§2.1～2.5；Evaluation：§3.1～3.3；未证明：§4，所采 trajectories 与 verifier 不能覆盖全部 agent failure。
  - 处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18005v1 — A Calibrated Instrument for Measuring How Inference Optimizations Affect Output Quality**
  - 采用命题：推理优化质量比较需要 dual reference、exchangeability/implementation null、positive control、等价界与功效预算。
  - Method：PDF §3.1～3.9；Evaluation：§5.1～5.4、Appendix C～E；未证明：§3.9 与披露的 220 prompts/两模型/特定优化 arms，不构成通用质量无损保证。
  - 处置：整合 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18080v1 — Decodability is Not Causality**
  - 采用命题：probe decodability 不能替代干预证据；SAE attribution 仍需 causal intervention 与 coherence gate。
  - Method：§3.1～3.7；Evaluation：§4、§5.1～5.4；未证明：§7，不证明所有 SAE feature 或 probe 都有相同因果结构。
  - 处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18123v1 — AutoTuneBench**
  - 采用命题：自动调参必须冻结机器、baseline、饱和度、provenance、预注册比较与 validator。
  - Method：§4.1～4.4、§5；Evaluation：§6.1～6.7；未证明：§8，只验证披露 engines/devices/tasks，不证明 agent tuner 的普遍最优性。
  - 处置：整合 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18204v1 — Beyond Accuracy**
  - 采用命题：procedural trace 会改变 overseer 的 decision criterion，process evidence 与 outcome accuracy 需要分别报告。
  - Method：§3、§4.1～4.4；Evaluation：§5.1～5.7；未证明：§6.3，不证明 trace 总能提高真实判定质量。
  - 处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18314v1 — Beyond Quadratic Loss**
  - 采用命题：Adam 稳定边界由 loss landscape 与 `β1/β2` 共同决定，不能把单一 momentum recipe 当常数。
  - Method：§2～§4；Evaluation：Appendix B～D；未证明：§5 与有限模型/尺度，不给出跨 objective 的普适最优超参。
  - 处置：整合 `TRAIN-PRETRAINING`。
- **2609.18453v1 — The Mirage of Calibrated Confidence**
  - 采用命题：verbal confidence 可与真实 reasoning trajectory 脱钩，不能单独拥有 abstention/truth 决策。
  - Method：§3.1～3.4、§4.1～4.2；Evaluation：§5～§6；未证明：Limitations，不证明所有模型或所有 confidence elicitation 都失效。
  - 处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18471v1 — First Token Matters**
  - 采用命题：reasoning model 的 safety collapse 可能在 onset/first token 已形成，最终文本检查不足以覆盖过程风险。
  - Method：§3.1～3.3、§4.1；Evaluation：§4.2、Appendix A～F；未证明：§7，不证明 onset intervention 在所有模型/攻击上成立。
  - 处置：整合 `PLATFORM-SECURITY`。
- **2609.18708v1 — Rethinking Critic Learning in PPO**
  - 采用命题：dense correlated state supervision 会造成 value flattening；稀疏 anchor 是条件化替代而非通用 critic recipe。
  - Method：§3、§4.1～4.3；Evaluation：§5.1～5.3；未证明：§6、Appendix A，只覆盖披露 tasks/models 和 critic construction。
  - 处置：整合 `TRAIN-PPO`。
- **2609.18878v1 — Preventing Model Collapse**
  - 采用命题：synthetic-data feedback 的稳定阈值依赖 Fisher–Rao dynamics 与理论假设，不能脱离生成/真实数据 identity 当固定配比。
  - Method：§II～§IV；Evaluation：理论 main result 与 auxiliary lemmas；未证明：§V，没有生产模型、硬件或经验 scale 验证。
  - 处置：整合 `TRAIN-DATA`。
- **2609.19107v1 — How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents**
  - 采用命题：architecture、growth rule、recursion 与 boundary operator 会改变拟合 scaling exponent。
  - Method：§3、§4.1～4.4、§5～§6；Evaluation：Appendix A～C；未证明：§7 与 recipe-specific sweeps，不证明 exponent 是跨数据/硬件常数。
  - 处置：整合 `WORLDVIEW-SCALING-LAW`。
- **2609.19145v1 — Objective vs. Search**
  - 采用命题：tokenizer 设计要把 optimization objective 与 search procedure 做 2×2 分解，intrinsic/extrinsic 结果不能互换。
  - Method：§2～§5；Evaluation：§6、§7.1～7.2；未证明：Limitations，不证明单一 tokenizer 在所有语言、模型与任务上占优。
  - 处置：整合 `MODEL-TOKENIZER`。

## 推理、内存与调度

- **2609.17573v1 — GroupKV**
  - 采用命题：diffusion LLM 多步全序列 KV 可按 group 稳定性分层，预测 compact buffer 并 selective repair。
  - Method：§3.1～3.2、§4.1～4.5；Evaluation：§5.1～5.5；未证明：§6，收益不外推未披露模型、硬件、batch 或 staleness budget。
  - 处置：整合 `INFER-KV-CACHE`。
- **2609.17652v1 — Fathom**
  - 采用命题：host-offloaded KV 的 per-query bit-plane read depth 可把 I/O depth 变成 accuracy/bandwidth control。
  - Method：§3.1～3.6；Evaluation：§4、§5.1～5.6、§6；未证明：§8，不证明所有 attention query 或 host tier 可用相同 depth。
  - 处置：整合 `INFER-KV-CACHE`。
- **2609.17691v1 — Accelerating Diffusion Sampling via Speculative Draft Trees**
  - 采用命题：diffusion draft tree 可提供受限并行 proposal，但 verifier/coupling 仍拥有 exactness 与 correction。
  - Method：§2、§3.1～3.3、Appendix B；Evaluation：§5.1～5.3、Appendix C；未证明：§6，不证明任意 diffusion model 或高维 workload 都加速。
  - 处置：已有覆盖 `INFER-SPECULATIVE-DECODING`。
- **2609.17943v1 — ASPIRE**
  - 采用命题：mixed draft/verify 请求可统一 forward 与异步批处理，但每请求 confirmed frontier/rollback 必须独立。
  - Method：§3、§4.1～4.3；Evaluation：§5.1～5.3、Appendix B～C；未证明：§7，结果绑定披露任务、draft variability、TP 与 recalibration。
  - 处置：整合 `INFER-SPECULATIVE-DECODING`。
- **2609.17983v1 — Contiguity, Not Importance**
  - 采用命题：文档局部编辑后的 stale KV repair frontier 由连续 causal influence 区间决定，而非抽象 token importance。
  - Method：Cache Repair as Budgeted Recomputation；Evaluation：Experimental Setup、Results 与各 repair analyses；未证明：Discussion/Conclusion，不给出跨模型固定 repair window。
  - 处置：整合 `INFER-KV-CACHE`。
- **2609.17997v1 — The Attention Within**
  - 采用命题：selective SSM 的 consensus equilibrium extent 与 output-gate observability 要分开评价。
  - Method：§II～§V；Evaluation：§VI-A～VI-B；未证明：§VII，连续时间、PoE/正定条件不证明实际离散网络或任务质量必然趋同。
  - 处置：整合 `MODEL-LONG-CONTEXT`。
- **2609.18063v1 — The Other Half of the Memory Wall**
  - 采用命题：Edge0 的 prerouter 预测直接替代下一层 routing，Recovery LoRA 沿 student path 补偿且 serving 时不合并；不是 prefetch miss/fallback。
  - Method：§3.1、§3.2 “Prediction Is the Routing”、§3.3、§4；Evaluation：§5.1～5.4；未证明：§6，证据绑定 Qwen/Ling、Mac、OpenCompass 与高方差同-session A/B。
  - 处置：整合 `INFER-GPU-MEMORY`。
- **2609.18112v1 — Token Latency Fairness**
  - 采用命题：multi-tenant fairness 应以 token 相对 isolated execution 的 latency inflation 为单位，并拆 compute/cache delay。
  - Method：§3、§4.1～4.3、§5.1～5.7；Evaluation：§7.1～7.2；未证明：§9 与 simulation assumptions，不证明模型误差或任意 cache policy 下的严格 isolation。
  - 处置：整合 `INFER-SCHEDULING`。
- **2609.18178v1 — Zero-I/O Fault Recovery**
  - 采用命题：fail-stop 且 optimizer step 已 commit 时，可在 CPU control group 共识后重建 process group/handles 并重绑存活 shard；不替代 durable checkpoint。
  - Method：§III-A～III-D；Evaluation：§IV-A～IV-H。1.216B/4×RTX5880/local NVMe 是 checkpoint-I/O 测量；Mistral-7B/16×RTX5880/1Gbps、25 updates/10 faults 才是 repeated recovery。
  - 未证明：§VI 不覆盖 silent corruption、唯一 shard 丢失、control-group failure、未提交 step 或站点级故障；处置：整合 `TRAIN-DISTRIBUTED-TRAINING`。
- **2609.18519v1 — COMPASS-ABS**
  - 采用命题：GPU fragmentation 要区分 scheduler-induced 与 workload-inherent 部分，并把 migration/compaction cost 放入决策。
  - Method：§3.1～3.2、§4.1～4.4；Evaluation：§5、§6.1～6.6；未证明：实验 trace/cluster 不支持固定 compaction 周期或任意拓扑收益。
  - 处置：整合 `PLATFORM-GPU-SCHEDULER`。
- **2609.18675v1 — HBFlex**
  - 采用命题：细粒度 KV state 与 coarse HBF execution 之间需要 plane-level placement、writeback 与 reclamation。
  - Method：§3、§4、§5.1～5.4；Evaluation：§6.1～6.5；未证明：§7，模拟/特定 HBF design 不证明生产 fabric 或任意 KV workload 收益。
  - 处置：已有覆盖 `INFER-GPU-MEMORY`。
- **2609.18849v1 — Ask the Tool, Don’t Guess**
  - 采用命题：tool-reported progress 可作为返回后 KV reuse value 的调度信号，但必须有 silence/lies fallback。
  - Method：§2、§3.1～3.2；Evaluation：§4.1～4.3、§5.1～5.3；未证明：Limitations 与 reporter-lies experiment，不证明工具信号总是可信或覆盖所有工具。
  - 处置：整合 `INFER-SCHEDULING`。
- **2609.19024v1 — OAK**
  - 采用命题：preemption scheduling 应显式计算 job age、restart cost 与已消耗 work，而不是把重启当无状态。
  - Method：§III-A～III-D；Evaluation：§IV、§V-A～V-F；未证明：§VI，simulator/有限硬件验证不证明任意集群 trace 或 failure model。
  - 处置：整合 `PLATFORM-GPU-SCHEDULER`。

## 数据、Agent 与安全

- **2609.18128v1 — Symbolic Temporal Supervision of LLM Agents Using Contracts**
  - 采用命题：LTLf/assume-guarantee contract 可把跨步 workflow invariant 变成可检查 state，但 monitor 不拥有未观测环境真值。
  - Method：§3、§4、§5.1～5.2；Evaluation：§6.1～6.4、Appendix C～F；未证明：§7 与 predicate catalogue，不证明 instrumentation 未覆盖的环境状态。
  - 处置：已有覆盖 `AGENT-WORKFLOW`。
- **2609.18672v1 — Selection Is Retrieval, Abstention Is Not**
  - 采用命题：tool selection 与 abstention 需要不同信号/校准，top-1 similarity 不能同时拥有二者。
  - Method：§2～§6；Evaluation：§7～§8；未证明：Limitations，只覆盖 70 个韩英 actions、披露 rankers 和设备。
  - 处置：已有覆盖 `AGENT-TOOL-CALLING`。
- **2609.18703v1 — RayOrch**
  - 采用命题：foundation-model dataflow 需要跨 grain lineage、ready-state scheduling、commit 与 recovery，而不仅是 task queue。
  - Method：§3.1～3.2、§4.1～4.5、§5；Evaluation：§6.1～6.5；未证明：§7，结果绑定作者 pipelines/cluster 与 failure injection。
  - 处置：已有覆盖 `TRAIN-DATA`。
- **2609.18769v1 — Version- and Scope-Aware Question Answering over Normative Documents**
  - 采用命题：normative answer identity 必须包含 document version、effective interval 与 scope。
  - Method：AI Approach and Design Rationale、Systems/Corpus/Controls、Question Set；Evaluation：Evaluation Methodology、Results；未证明：Lessons Learned，只是特定部署案例，不证明通用 QA correctness。
  - 处置：已有覆盖 `AGENT-RAG`。
- **2609.18820v1 — Compositional Policy Violations**
  - 采用命题：逐步合规不能推出组合 workflow 合规，monitor 必须重建跨步 joint state 与 provenance。
  - Method：§3、§4、§5.1～5.6；Evaluation：仅 taxonomy/architecture examples；未证明：§6～§7，没有端到端生产 detection benchmark 或完备性保证。
  - 处置：已有覆盖 `PLATFORM-SECURITY`。
- **2609.18998v1 — One Axis, No Brake**
  - 采用命题：self-knowledge signal 不能可靠阻止 harmful peer conformity；minority evidence 与 consensus state 要分开。
  - Method：§2、§3.1～3.4、§4.1～4.2、§5；Evaluation：Appendix B～F；未证明：§8 与 preliminary warrant arm，不证明任意开放式多 Agent 系统都同样坍塌。
  - 处置：已有覆盖 `AGENT-MULTI-AGENT`。
- **2609.19101v1 — Monitoring and Discovering Reward Hacking with Internal Representations**
  - 采用命题：internal representation probe 可作 reward-hacking sensor，但不拥有 intent/truth，必须结合 independent outcome evidence。
  - Method：§2.1～2.3、§3.1～3.2、§4.1～4.4；Evaluation：§5 与 Appendix B～C；未证明：§8，probe false positive 与环境 transfer 不支持通用 intent detector。
  - 处置：整合 `PLATFORM-SECURITY`。
- **UnStep repository snapshot**
  - 采用命题：官方 artifact 披露把少步 denoising、较小 KV window、cache refinement 与 DiT/VAE runtime 优化组合；只作 artifact claim。
  - Method/Evaluation locator：官方仓库初始 commit `e7525751dc00582571cb3eea6e357cfa57db0843` 的 README、inference commands 与 reported performance；identity locator：本地 `unstep-repo.json` 的 `created_at=2026-09-17T11:52:19Z` 与 `audit_binding`。
  - 未证明：当窗无已审论文正文或独立 evaluation，README 数值不支持新普遍机制；处置：已有覆盖 `MULTIMODAL-GENERATIVE-PARADIGMS`。

## Fresh-context false-negative 恢复项

- **2609.17745v1 — REVERSAL-BENCH**
  - 采用命题：reset-free embodied learning 必须显式建模 irreversibility、recoverability oracle 与吸收态；恢复不可达时不能继续把 online learning 当作安全默认值。
  - Method：§III-A～III-F、§V；Evaluation：§IV、§VI；未证明：§VII，只覆盖论文的 physics engines、任务和 oracle，不证明开放世界状态可逆或 recovery policy 普遍有效。
  - 处置：整合 `MULTIMODAL-EMBODIED-VLA`。
- **2609.17940v1 — Beyond the Previous Layer**
  - 采用命题：较早层的 expert selections 在控制最近层选择后仍含增量预测信息，可作为 residency hint，但不能替代实际 router。
  - Method：§2.1～2.2；Evaluation：§3.1～3.3；未证明：§4，只证明 frozen OLMoE/JetMoE 上的 predictive structure，不证明端到端 prefetch、吞吐或 SLO 改善。
  - 处置：整合 `INFER-GPU-MEMORY`。
- **2609.18016v1 — Causal-History Test-Time Scaling for Failure Recovery**
  - 采用命题：autoregressive world-action model 的恢复需区分 trigger、可靠 history prefix、causal KV reconstruction 与多假设 verification。
  - Method：§III-A～III-C；Evaluation：§IV-A～IV-E；未证明：有限仿真/实机 manipulation 不证明 prefix 永远可恢复、隐藏状态可观测或高风险动作适合在线试错。
  - 处置：整合 `MULTIMODAL-WORLD-MODELS`。
- **2609.18066v2 — Towards Training Private LLMs on Apple Silicon with RDMA over Thunderbolt**
  - 采用命题：在大统一内存但低互联带宽的训练拓扑中，多 trunk、持久 worker 与 CPU-side overlap 可以换取更高吞吐；硬件容量、互联与 acquisition cost 必须共同评价。
  - Method：§3；Evaluation：§4.1～§4.4；未证明：四节点 Mac Studio、Qwen3-9B 与所测 sequence length 不支持外推任意模型、规模、可靠性或数据隐私保证。
  - 处置：已有覆盖 `TRAIN-DISTRIBUTED-TRAINING`。
- **2609.18099v1 — When Is Graph Structure Worth Its Cost?**
  - 采用命题：GraphRAG 的结构收益必须与 ingestion/query 的模型调用成本和原文 evidence 保真共同评价。
  - Method：§3；Evaluation：§4.1～§4.6；未证明：§5 的 threats to validity，120 个问题、四个领域与单一主要 baseline 不证明普遍质量或成本优势。
  - 处置：已有覆盖 `AGENT-RAG`。
- **2609.18110v1 — SSD-LLaMA**
  - 采用命题：超大 MoE 的本地执行必须统一 SSD expert-pack、异步读取、DRAM/VRAM cache 与 CPU-GPU work split；“SSD 容得下”不等于 token latency 可接受。
  - Method：§3～§4；Evaluation：§5.1～§5.4；未证明：§7，作者模型、量化、RTX 5090、RAM/SSD 与 benchmark 不支持外推任意硬件、模型质量、tail latency 或耐久性。
  - 处置：已有覆盖 `INFER-GPU-MEMORY`。
- **2609.18145v1 — Reaching Every Position Without Searching**
  - 采用命题：跨层旋转的 fixed sparse wiring 可在对数深度形成全局可达性，但 global reachability 与内容自适应选择是不同能力。
  - Method：§3.1～§3.4；Evaluation：§4～§9；未证明：§10，小型字符模型、短窗口与固定 step budget 不证明可替代通用 LLM Attention。
  - 处置：整合 `MODEL-SELF-ATTENTION`。
- **2609.18346v1 — Faithful yet Collusive**
  - 采用命题：CoT 的 structural/intent faithfulness 与行为 effect 不同，trace monitor 不能单独判定多 Agent 联合策略安全。
  - Method：§3.1～§3.8；Evaluation：§4～§5；未证明：Limitations，只覆盖有限模型与 Bertrand pricing simulation，不证明真实市场共谋率。
  - 处置：整合 `PLATFORM-SECURITY`。
- **2609.18388v1 — GeoMesh**
  - 采用命题：geo-distributed synchronous training 可用 per-worker batch/inner-step plan 与 sign-compressed pseudo-gradient 减少异构等待，但 step owner 必须版本化聚合权重、local work 与 compression state。
  - Method：§3.1～§3.2；Evaluation：§4.1～§4.4、Appendix A～B；未证明：§7，只覆盖 150M～500M 模型、作者异构 GPU/WAN 设置，不证明大规模收敛、非 IID 数据或故障恢复。
  - 处置：整合 `TRAIN-DISTRIBUTED-TRAINING`。
- **2609.18460v1 — Collective Loss of Control in LLM Agent Systems**
  - 采用命题：隐式通信路径可使局部异常形成条件性 contagion；隔离、message admission、recovery 与最终 effect authority 必须分别拥有状态。
  - Method：§3～§5；Evaluation：§6～§8；未证明：论文明确未测自然 rare-event rate，也未证明 autonomous cascade，只证明特定 pending-call transport 下的 susceptibility。
  - 处置：整合 `PLATFORM-SECURITY`。
- **2609.18842v1 — Infinite-Parameter LLMs**
  - 采用命题：hypernetwork 可把 live data 编译为低秩 FFN 调制并在线更新 latent belief，但生成权重必须绑定 base、session、provenance、validity 与 rollback。
  - Method：§3.1～§3.5；Evaluation：§4.1～§4.4；未证明：§5，小规模受控实验不证明无限容量、生产持续学习稳定性、隐私或跨租户隔离。
  - 处置：整合 `MODEL-FEED-FORWARD-MLP`。
- **2609.19000v1 — Capability Emergence Can Be Forecast**
  - 采用命题：能力出现的 early warning 要报告 per-seed lead time、calibrated interval、manufactured negatives、false-alarm bound 与 blind gate；precursor 不拥有 release authority。
  - Method/Evaluation：论文的 precursor construction、split-conformal calibration、trap-language negative controls、blind gates 与 public-checkpoint study；未证明：合成/小模型和有限公开 families 不证明任意新能力均可预测或 anchor 具有因果充分性。
  - 处置：整合 `WORLDVIEW-LLM-INTELLIGENCE`。
- **2609.19135v1 — Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging**
  - 采用命题：当前状态/行为边际 coverage 不能替代 logger history identity；即使 latent state 很少，history dependence 也可使 OPE 样本需求随 horizon 指数增长。
  - Method：§2～§5；Evaluation：§6、Appendix F；未证明：§8 与构造性 POMDP 不表示所有 OPE 不可用，也不直接给出生产 estimator 的统一阈值。
  - 处置：整合 `PLATFORM-EVALUATION-SYSTEM`。

fresh audit 同时确认：`2609.17594v1` 的首次公开早于本窗，只作跨日去重。

## 定点终审重开的 exact-v1 候选

- **2609.18622v1 — How Many Labels Does Model Choice Need?**
  - 采用命题：模型选择的标注需求取决于目标指标，而不能由 prediction agreement 统一替代；同一 panel 上，disagreement labels 足以闭合 accuracy choice，却可能完全无法闭合 AUGRC choice。评价系统应按 selection objective、tolerance 与当前不可区分集合维护证书，并让证书而非预算耗尽决定停止。
  - Method：exact-v1 的 problem setup、adaptive label-query procedure、exact/approximate selection certificate 与 stopping rule；Evaluation：108 个 panel comparisons，以及 disagreement、uniform 与 proposed acquisition 的 accuracy/AUGRC label-budget 对照；未证明：固定未标注 pool、固定候选预测/排序、binary 或共享 multiclass predictions 与 `K<=8` 不覆盖 retraining、transfer、分布漂移或任意规模模型库，有限 panel 的预算比例也不能外推。
  - 评分：Design Delta 3 / System Reach 2 / Durability 3，Total 8；处置：整合 `PLATFORM-EVALUATION-SYSTEM`。Ch66 已有唯一 source-family marker 和实质正文，本次只核对绑定，不重复写入。
- **2609.17904v1 — Timely Activation of Safety Filters via One-Step Reachability Expansion**
  - 采用命题：连续时间 HJ safety filter 的不变性保证不能静默继承到 sampled-data controller；若一个控制周期可越过 unsafe BRT，filter 必须对最坏情况一步可达域提前扩张触发边界。reachability model、采样周期、扰动界与 actuator delay 应共同进入 physical safety identity。
  - Method：exact-v1 的 continuous-time HJ/BRT 定义、worst-case one-step reachable set、expanded BRT 与理想假设下的安全命题；Evaluation：Dubins-car simulation、多个采样周期各 100 次运行，并与未扩张 filter 比较。未证明：实验采用精确动力学与完美状态，扩张分支仍只有 67–86/100 safe outcomes；论文明确说明它没有完全消除 continuous-discrete mismatch，只在单一仿真系统验证，未覆盖真实机器人、高维动力学、模型误差或硬件时延。
  - 评分：Design Delta 3 / System Reach 2 / Durability 3，Total 8；处置：整合 `MULTIMODAL-EMBODIED-VLA`。Ch26 已有唯一 source-family marker 和实质正文，本次只核对绑定，不重复写入。

## 标题层 false-negative 恢复项

- **2609.17989v1 — Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders**
  - 采用命题：system prompt 指定的 principal 会改变 agent 对 sponsorship disclosure 的选择和质疑；角色、authority 与利益边界不能被当作中性文案。
  - Method/Evaluation：Study 1 的 principal assignment controlled-choice design、跨模型/推理深度 replication，以及 Study 2 对 disclosure attribution/wording 的分解；未证明：所测购物场景与角色措辞不证明任意 agent 都有固定 sponsorship bias，reasoning trace 也不等于真实因果机制。
  - 处置：已有覆盖 `AGENT-PROMPT`；Ch74 已将 role/authority context 与外部 policy/evidence 分开。
- **2609.18357v1 — Market Signal Injection: Adversarial Context Manipulation of LLM Pricing Agents**
  - 采用命题：数据数值不变时，format/order/sentiment presentation 仍可操纵 LLM agent；canonicalization、decision boundary 与最终 effect authorization 需要分层。
  - Method：§3～§4 的 Bertrand duopoly/triopoly、MSI attack 与 matched controls；Evaluation：§5.1～§5.6 的九个 open-weight/三个 proprietary models、held-out probes、canonicalization 与 adaptive-attack mitigation；未证明：activation separability 不识别有害决策，模拟市场也不证明现实价格影响或跨任务防御充分性。
  - 处置：已整合 `PLATFORM-SECURITY`；精确锚点、回退与写后核验见 `books-queue.md`。
- **2609.18440v1 — Planning or Improvisation? Stress-Testing the Poetry Planning Site on Open Models and Open Cross-Layer Transcoders**
  - 采用命题：复现 attribution 曲线形状不等于复现原机制；位置特异性、newline 位点身份和 causal plan 必须分别检验。
  - Method：claim decomposition 与四个开放模型/六个 CLT 的 feature census、steering、activation patching；Evaluation：247/444 detectable prompt-inject pairs、36 runs/8640 lines 与 1260-line residual-patching test；未证明：作者明确声明不是 faithful reproduction，开放小模型/CLT 不能否定其他模型存在提前规划。
  - 处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`；Ch66 已要求 shape、site、intervention 与 mechanism claim 分离。
- **2609.18516v1 — Align, Integrate, and Fire: Efficient Token-Level Alignment for Zero-Shot SpeechLLMs**
  - 采用命题：continuous speech frames 可经 DTW-aligned CIF 压缩到目标文本 token 长度，并以单层 distillation 降低 projector 训练成本。
  - Method：§3.1～§3.3 的 DTW alignment、ACIF 与 single-layer KD；Evaluation：§4.1～§4.4 的 ASR、speech translation 和 parameter-efficient baselines；未证明：作者模型、语言与任务不支持通用 SpeechLLM 质量/延迟结论，训练 alignment 也不等于线上已知目标文本。
  - 处置：已有覆盖 `MULTIMODAL-REPRESENTATION`；Ch23 已有 modality encoder、sequence compression、alignment 与 distillation 边界。
- **2609.18560v1 — The evolution of sex for artificial intelligence: a population-genetic framework for multigenerational model populations**
  - 采用命题：recursive training 的漂移受真实样本绝对注入量影响；多父模型的组合规则决定互补能否保留；冲突 convention 比普通参数漂移更能预测 merge incompatibility。
  - Method/Evaluation：Materials and Methods 与 Results 中的 exact inheritance model、RNN/FFN/VAE generators、LLM specialists/merging experiments；未证明：生物学对应不是跨架构普遍定律，有限模型、seeds 与 conventions 不给出生产固定配方。
  - 处置：已整合 `TRAIN-DATA`；精确锚点、回退与写后核验见 `books-queue.md`。
- **2609.18857v1 — Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN**
  - 采用命题：分别正确的 agents 对共享控制变量独立 commit 仍可产生振荡；proposal authority、feasibility invariant、dwell/deadband 与 commit owner 必须显式分离。
  - Method：§III～§V 的 O-RAN shared-state model、AURA arbiter 与 convergence proof（§IV-C）；Evaluation：§VI 的 live OAI/FlexRIC latency/throughput testbed；未证明：protected-slice latency compliance 未改善，结果绑定 O-RAN 与单变量 proposal schema，复合动作仍需 coordinator/人工 fallback。
  - 处置：已整合 `AGENT-MULTI-AGENT`；精确锚点、回退与写后核验见 `books-queue.md`。

日期复核另确认 `2609.17552v1` 的 first-public event 为 2026-07-16，不属于本窗；它只保留在 screening ledger 的 earlier-owner 去重集合，不评分、不做本窗 Books Decision。

## 重要修订（不重复评分）

- **2606.27409v2 — Delayed Verification Destabilizes Multi-Agent LLM Belief**
  - 采用命题：synthetic signed-belief recurrence 在其假设下支持 delay-induced oscillatory boundary；grounded factual study 未识别或证实同类振荡，必须保留 completion/abstention 不确定性。
  - Method：§3～§6；Evaluation：§7.1、§7.2（含 expanded 400-question complete logs）、§7.3；未证明：§8～§10，factual completion bounds 因大量 abstention 同时允许误差增加/降低，不能声称 truth 是 absorbing boundary。
  - 处置：整合修正 `AGENT-MULTI-AGENT`，revision 不重复评分。

## 终审定点返修恢复项

- **2609.18270v1 — BENCHCOMPASS**
  - 采用命题：评价同一模型时，应并列 closed、open 与 attacked-open 条件，才能分离 parametric knowledge、context-use gap/interference 与 harness brittleness；evidence pack 必须保留来源定位和扰动 provenance。
  - Method：§3 的三种评价条件、diagnostic signals 与 repair hypotheses；构建：§4 的 payment-domain corpus、answer-preserving perturbations、evidence packs 与 expert admission；Evaluation：§5 的主实验与 judge sensitivity。
  - 未证明：306 个专家接纳案例只覆盖 payment domain；repair hypotheses 不是因果修复验证；没有评价 retrieval、tools 或 multi-agent；judge 与 domain coverage 仍有限。
  - 评分：`3 + 2 + 3 = 8`，Deep；处置：待整合 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18306v1 — Bias Amplification in Multi-Agent Network**
  - 采用命题：多 Agent 评价不能把 numeric opinion convergence 与 rhetorical vocabulary alignment 当作同一状态；biased minority 可能同时通过行为与语言通道影响中立 agents。
  - Method：§3 的受控 Llama 3.2 network 与 Friedkin-Johnsen baseline；Evaluation：§4～§5 的 neutral-agent metrics、15 次重复与 95% confidence intervals。
  - 未证明：单一模型族、四个主题、理想化网络和结构化交互不证明生产系统发生率或开放网络中的普遍因果关系。
  - 评分：`2 + 2 + 2 = 6`，Standard；处置：已有覆盖 `AGENT-MULTI-AGENT`。
- **2609.18520v1 — AeroWeaver**
  - 采用命题：embodied multi-agent harness 应分离 role-conditioned semantic decision、governed skill invocation、body-local observation、coordination report、固定 executor 与 role-indexed state/action/reward memory；agent 只拥有局部行动，不自动拥有 joint-action authority。
  - Method：§III-A～III-C；Evaluation：§IV 的九个 MPE-inspired closed-loop tasks、54 个 task-condition pairs、十次 episode return 与组件消融。
  - 未证明：模拟 UAV/MPE 条件不证明真实硬件、physical safety、sim-to-real 或 reward adaptation；LLM coordination 的收益也不是跨环境通用结论。
  - 评分：`2 + 2 + 2 = 6`，Standard；处置：已有覆盖 `AGENT-MULTI-AGENT`，并向 `MULTIMODAL-EMBODIED-VLA` handoff。
- **2609.18649v1 — DyMT-ESB**
  - 采用命题：多轮安全/偏差评价必须让 user turn 依赖上一轮 response，并把 conversation history、turn frontier 与停止条件纳入 evaluation identity；固定脚本和固定轮数会漏掉 late-emerging、non-monotonic 与 re-emerging behavior。
  - Method：§2 的动态多轮协议；Evaluation：§3～§4 的 240 seed stereotypes、六类偏差、六个模型、5/10-turn 对照与 human judge validation。
  - 未证明：用户是合成的，generator/judge 主要来自 GPT-4o-mini，六类偏差和六个模型不能代表真实用户发生率或所有风险类型。
  - 评分：`3 + 2 + 3 = 8`，Deep；处置：待整合 `PLATFORM-EVALUATION-SYSTEM`。
- **2609.18860v1 — Decodable but Misrouted**
  - 采用命题：supervised accessibility 与 native output routing 是不同命题；只有 feature knockout、routed-feature patching 与受限 recovery 才能说明 silent discriminative features 是否进入模型决策路径。
  - Method：§2～§5 的 sparse probes、native head、feature knockout、routed-feature patching 与 calibration-only routing/LoRA；Evaluation：Gemma/Qwen 上六个 harmful-content 多模态任务及 locked split。
  - 未证明：harmful-meme 任务与模型范围有限；probe access 不等于 native rule；干预样本小、比例随尺度敏感，LoRA 还出现 negative transfer。
  - 评分：`3 + 2 + 3 = 8`，Deep；处置：已有覆盖 `PLATFORM-EVALUATION-SYSTEM`。

## 终审定点返修关闭项

- `2609.17555v1`：v1 首发早于本窗；REQAP 是 AlexNet/VGG/ResNet systolic-array 的 mixed-precision packing 与 selective MSB TMR，不作为 09-18 owner。
- `2609.17800v1`：牙科 X-ray VLM 的 tool-evidence 应用，未形成超出现有 tool/evidence grounding 的通用机制。
- `2609.17977v1`：把既有 confidence-gated cascade 迁移到对话情绪识别 CCaaS；贡献是领域 operating point，不改变路由/abstention contract。
- `2609.18045v1`：一般多智能体动力系统的隐藏轨迹与 interaction graph 联合推断，不是 LLM Agent 平台机制。
- `2609.18120v1`：十阶段渗透测试流程组合 deterministic exploit map、local/free-tier cascade、MCP tools 与测试协议；没有超出现有 workflow/MCP/security/evaluation owner 的长期机制。
- `2609.18416v1`：随机子空间梯度下降的一般优化理论，摘要与正文未给出 LLM training-system boundary 或可采用 operating point。
- `2609.18496v1`：网络安全领域的 mid-training/SFT synthetic-data 配方，未改变 continued pretraining、domain adaptation 或 data curation 的既有机制边界。
- `2609.18959v1`、`2609.19006v1`：v1 首发均早于本窗，分别归其真实 first-public owner，不在 09-18 评分。
