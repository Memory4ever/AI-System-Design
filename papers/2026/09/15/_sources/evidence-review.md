# 2026-09-15 Evidence Review

本文补充 [`../README.md`](../README.md) 中 31 个经 false-negative audit 恢复的候选。所有论文均使用 `exact-v1`；定位、采用命题与不证明事项如下。原先 15 项的证据审阅仍保留在日报正文。

## Evaluation 与可靠性

### BudgetBench — `arXiv:2609.13149v1`

- **证据位置：** §2 Protocol、§4 Evaluation Protocol、§6 Setup、§7 Results、§9 Threats。
- **采用命题：** 比较 Agent memory strategy 时，per-call input-token budget 应作为独立变量；质量、利用率、延迟和 violation rate 必须共同记录，不能由一次 full-context 结果代表预算曲线。
- **边界：** local Qwen2.5-1.5B 各 89 项、hosted Qwen3-30B-A3B 50 项和 LongMemEval 500 项只证明 harness 能暴露非单调曲线与违规；早期 tokenizer approximation 低估 token，且论文没有给出 memory strategy 的最终排序。

### PEAT — `arXiv:2609.13544v1`

- **证据位置：** §IV Methodology、§V Characterization / Evaluation。
- **采用命题：** DNN training kernel 的 pseudo-error campaign 应绑定注入算子、错误 signature、传播位置和 task outcome，不能以最终 loss/accuracy 单独定位 kernel fault。
- **边界：** V100、MI250 及所测 vision/language workloads 只覆盖作者注入模型；不证明生产硬件 fault prevalence、任意 kernel 的检测阈值或跨架构通用性。

### Persistent AI Identity Benchmark — `arXiv:2609.13637v1`

- **证据位置：** §2 Contract、§3 Protocol、§4 Results、§6 Limitations。
- **采用命题：** deployed agent identity 的 evaluation object 应绑定 profile version、session lineage、更新与持久化路径，并把 recall、composition、enactment、resistance、persistence 分开测量。
- **边界：** 16 synthetic profiles、32 probes、3 initialized configurations、1,536 responses 受单次 target sample、post-hoc follow-up 和 judge sensitivity 限制；不证明真实用户身份长期稳定。

### Compliance Data as Evaluation — `arXiv:2609.13642v1`

- **证据位置：** §IV Failure Modes、§V Measurement Contract、§VI Infrastructure、§VII Limitations。
- **采用命题：** monitoring/compliance data 只有在 claim、exposure、domain、capture process 与 comparator 对齐时才能支持比较；“有日志”不能自动成为模型或系统效果证据。
- **边界：** 论文主要是测量合同与 automated-driving case，未给 foundation-model causal benchmark；正文只能采用 validity boundary，不能采用性能结论。

### Factuality Judge Perturbation — `arXiv:2609.15561v1`

- **证据位置：** §3 Controlled Perturbation Pipeline、§4 Validation、§5 Evaluation、§6 Limitations。
- **采用命题：** factuality metric 的 meta-evaluation 应以受控 answer corruption 构造已知退化序列，检查 metric 是否随事实损坏单调变化；judge 分数本身不能证明事实正确。
- **边界：** perturbation validity、数据集、模型与 pipeline components 仍受 learned judge 影响；不证明通过该测试的 metric 在开放事实空间可靠。

## Training、Kernel 与 Serving Runtime

### ForgeTrain — `arXiv:2609.13645v1`

- **证据位置：** §3.1～§3.4 Method、§4.1～§4.4 Experiments、Appendix A/F/G/J。
- **采用命题：** 用 AI 生成场景专用训练引擎时，correctness gate 不应从模糊“质量相近”开始；Harness 先冻结 golden reference 的 activation、gradient、optimizer、loss-scaling 与 collective anchors，建立 bit-for-bit 基线，再只在 Gate 后单调放宽到 trajectory/downstream parity。优化 agent 不拥有验收标准，失败探索不能进入下一 baseline。
- **边界：** 七个 H100/Ascend model-hardware 设置中作者报告相对参考 MFU 提升 4.7%～33.2%，长程检查只覆盖 MiniCPM4/5 的三个 engine；这不证明任意模型、硬件或 AI 生成代码都生产可用，也不证明 training-quality parity 等于数值等价。Harness 构建、oracle 冻结与长程重跑是额外成本；无法建立可信 reference 时应回退成熟通用框架。

### BigMoMo — `arXiv:2609.14643v1`

- **证据位置：** §3 Motivation、§4.1～§4.4 Methods、§5.1～§5.5 Evaluation。
- **采用命题：** speculative decoding 的 multi-token verification window 不只可减少 target forward 次数，还可成为 storage-backed MoE 的 bounded lookahead：runtime 依据 acceptance、routing impact 与 movement cost 筛选 expert staging proposal，按 co-load pattern 重排 flash layout，并在最终 router/verification authority 不变的前提下批量搬运与重用权重。
- **边界：** 四个 MoE、五个 benchmark、两个 mobile platform 下作者报告相对 on-demand autoregressive offloading 平均 4.83×、相对最佳 speculative MoE baseline 平均 1.82×；结果不证明任意 MoE、flash/NPU 或生产 thermal/SLO。错误预测会产生无效读取，动态布局增加 metadata 与重组成本；acceptance/locality 不足时回退 on-demand load 或较小常驻模型。

### DeepSeek-V4-Flash on AMD gfx90a — `arXiv:2609.15627v1`

- **证据位置：** §3～§5 System/Correctness Recovery、§8 Current TP8 Results、§9 Protocol Separation、§10 Measurement/Correctness、§11～§13 Rejected Directions/Risks。
- **采用命题：** shape-specific mixed-precision inference path 必须先通过 component oracle、bounded semantic check 与 service sentinel，再取得性能测试资格；无效 fast path 应从历史数字中剔除。不同 concurrency、prefill/decode、native-AR/speculation 与 HTTP/resident 协议不能相除或相加为统一 speedup，执行计划 identity 必须绑定 checkpoint、commit、shape、precision、kernel selector 与 measurement protocol。
- **边界：** MI250 TP8/EP1、SGLang 和作者 code workload 中 C1/C32/C64 resident decode 分别为 87.60/1044.32/1334.24 tok/s，8K prefill 为 4.68～5.27k input tok/s；3.60×、10.32% 与 1.54% 来自彼此独立的 ABBA/pilot，不能组合。component equality 不证明 universal numerical equivalence，dynamic batching、cold-shape compile 与 million-token occupancy 未验证；不满足 oracle 时回退已验证 kernel/precision path。

### BOOST — `arXiv:2609.13592v1`

- **证据位置：** §3 Design、§4 Implementation、§5 Evaluation、§6 Discussion。
- **采用命题：** coherent heterogeneous memory 中，weights 与 KV 可以并发从 HBM/host memory 读取；memory controller 应按访问并行性而非只按“冷热搬运”选择驻留。
- **边界：** Grace Hopper、vLLM 和所测静态 weights/KV 配置下，作者报告 iso-batch TPOT +4.3%、吞吐平均 +31%；不外推其他互连、模型、precision、batch、concurrency 或 SLO。

### AttnFuse — `arXiv:2609.13612v1`

- **证据位置：** §3 System、§4 Optimizations、§5 Cross-architecture Study、§6 Evaluation、§9.1 Limitations。
- **采用命题：** attention DSL 若要把 RoPE 等 pre-matmul transform 与 attention kernel 融合，必须让 transform semantics、layout、tile 与目标 GPU 共同进入 compilation plan；fusion crossover 随架构变化。
- **边界：** RTX 3090/H100、Llama3-8B training 与作者 patterns 只证明所测 operator family；2.10× 与 H100 上距 PyTorch backend 5% 的数字不代表端到端 serving 或任意 shape。

### OpWeave — `arXiv:2609.14237v1`

- **证据位置：** §3 Analysis、§4 Formulation、§5 Algorithm、§6 System、§7 Evaluation。
- **采用命题：** 异构 serving 的 disaggregation unit 可以从完整 model/stage 下沉到 operator；planner 提交 operator placement，runtime 持有当前 topology、state transfer 与 fallback。
- **边界：** vLLM、作者 homogeneous/heterogeneous GPU clusters 和 analytical cost model 支持所测成本结果（最高 1.78×/1.89×），不证明任意网络、故障或生产尾延迟。

### Flattening Every Memory Peak — `arXiv:2609.14306v1`

- **证据位置：** §2 Memory Axes、§3 Four Operators、§4 Integration、§7 Limitations 及相关 Appendix。
- **采用命题：** 长上下文 MoE training 的 memory contract 必须分别约束 expert dispatch、vocabulary projection、checkpoint boundary 与 optimizer state 的峰值，再用 streaming/bounded schedules 组合；只看 steady-state activation 或 optimizer 占用会漏掉 OOM owner。
- **边界：** 机制依赖模型、并行布局和 hardware；组合会增加 host traffic、recompute、ordering 与实现复杂度，不能把单项 peak reduction 相加为端到端收益。

### InplaceKVCache — `arXiv:2609.14507v1`

- **证据位置：** §3 Monolithic Failure、§4 Format、§5 Theory、§6 Implementation、§7 Evaluation、§9 Limitations。
- **采用命题：** KV 的 CPU/GPU residency 可以在写入时编码成稳定的 four-region physical layout，以 scheduling 选择消费位置而非事后搬迁；logical identity 与 physical region map 必须共同版本化。
- **边界：** 3 个 MoE 模型、A100/V100、32 GB 与最高 1M aggregate context 仅支持作者 kernel/framework；不证明通用 portability 或所有负载都优于迁移。

### Hybrid-state Cache Recovery — `arXiv:2609.15030v1`

- **证据位置：** §2 Design、§3 Recovery、§4 Numerical Control、§5 Evaluation、§6 Limitations。
- **采用命题：** hybrid state cache 恢复必须同时校验 scheduler token credit、strict-prefix lookup、transfer/save completion 与 numerical path；命中缓存不等于恢复到同一可继续状态。
- **边界：** GLM-5.3-Flash NVFP4、vLLM+LMCache、TP4、36/36 与 72 paired tests、120 serial runs 未覆盖并发 serving、普遍 determinism 或容量极限。

### ETCInfer — `arXiv:2609.15230v1`

- **证据位置：** §III Scheduler、§IV Models、§V Solution、§VI Implementation、§VII Evaluation。
- **采用命题：** inference scheduling 可把 cooling setpoint、GPU frequency 与 microbatch 联合为带 thermal dynamics 的计划，但 thermal model revision 与 SLO slack 必须归 scheduler，而不是让局部 DVFS/cooling controller独立优化。
- **边界：** simulation 与有限 validation 中作者报告最高 33.1% energy reduction、92.9% throttle reduction、SLO violation <0.7%；依赖 facility/GPU calibration，不证明生产集群通用收益。

### MAPS — `arXiv:2609.15359v1`

- **证据位置：** §3 Design、§4 Experiments、§5 Limitations。
- **采用命题：** output-length prediction 可与 prefill overlap，并以 calibrated upper bound 驱动 global/local scheduling；prediction 只提供 future-state estimate，实际 token progress 仍要持续对账。
- **边界：** 两类 workload、两个 LLM 的作者结果不证明 predictor 在分布漂移、不同 batch/concurrency 或生产 SLO 下稳定；已有 scheduling contract 已覆盖该责任边界。

### Trillion-Parameter MoE in a Box — `arXiv:2609.15636v1`

- **证据位置：** §II Workload/Design、§III Evaluation、§IV Conclusion。
- **采用命题：** 超大 MoE memory provisioning 不能把 HBM、DRAM 与 high-bandwidth flash 简化为单一容量轴；internal bandwidth 与 host-link bandwidth 的独立 knee 决定 expert staging 是否可行。
- **边界：** 两个 trillion-parameter MoE 的 operator analysis、一个 routing trace 与 agent traces 主要是 modeled design-space evidence，不是完整 production appliance、真实故障或普遍 SLO 证明。

## Agent State、Tool 与 Security

### IntentCap — `arXiv:2609.14631v1`

- **证据位置：** §1 Background/Motivation、§2 Design、§3 Preliminary Evaluation。
- **采用命题：** Agent capability 应是 task-scoped、短时且多来源合成的 typed lease：user intent、workflow、tool schema 与 runtime environment 各自拥有字段，任何来源都不能替另一个填权或扩大权限；LLM 只提出 lease，副作用前由 deterministic checker 验证 monotonic narrowing，并由 tool/OS policy 执行。
- **边界：** 初步实验只支持论文测试的 tool、execution、placement 与 delegation violation/benign cases；没有开放世界攻击率、长期运维或复杂撤销证明。字段 owner 配置错误会产生误拒/漏权，checker 与 policy runtime 成为新增可信组件；无法可靠合成时回退静态最小权限、显式审批与短会话隔离。

### Loop-Back Authority — `arXiv:2609.14767v1`

- **证据位置：** §3 Paired System Design、§4.1～§4.6 Results、§5 Discussion/Conclusion。
- **采用命题：** hierarchical Multi-Agent topology 的 admission 不能以“多一层 supervisor”默认成立；manager 只有在拥有独立、可执行的 verifier 时才值得取得 reject/revision authority。若只能表达偏好，loop-back 会增加 revision pressure、hedging 与成本，flat topology 仍是更稳的旧路径。
- **边界：** 43 对 business-intelligence reports、86 runs、五模型 judge 与 deterministic spec 只覆盖单一开放式短上下文任务；flat 的 utility/clarity 优势和 hierarchy 的 51.5% token、40.5% generation cost、20.2% total cost、34.3% latency 增量不能外推所有团队。loop 数与清晰度关系含相关性，judge 仍有模型偏差；有强 verifier、合规审批或可检查答案时 hierarchy 仍可能合理。

## RAG 检索与部署评价

### QCAR — `arXiv:2609.13489v1`

- **证据位置：** §3.1～§3.5 Framework/Assumptions、§4 Methodology、§5.1～§5.4 Experiments。
- **采用命题：** fixed top-k 之外，可以把 retrieval depth 作为 query-conditioned typed control：离线以默认 retriever 的 NDCG-k saturation 得到 per-query `k*`，再聚类为 cluster-level depth；在线只分配 cluster 和预算。它改变的是 retrieval controller 的 proposal，不改变 relevance、authorization 或 evidence sufficiency authority。
- **边界：** 约 20k raw/6,820 clean legal queries、domain-specific embedding/clustering 与 relevance labels 构成有界条件；摘要所称 F1/token 收益不能外推医疗、金融或任意 corpus。需要历史 query、可靠 labels 与 cluster drift 监控；数据不足、query 越界或 cluster 置信低时回退已校准 fixed top-k/保守上限。

### Synthetic–Authentic RAG Evaluation — `arXiv:2609.14579v1`

- **证据位置：** §3 Synthetic–Authentic Gap、§4.1～§4.4 Case Study、§5 Discussion/Limitations。
- **采用命题：** RAG release workload 不能只由 corpus-conditioned synthetic questions 定义；evaluation identity 应同时保存 authentic traffic 的长度、intent/source concentration、unanswerable/off-corpus 比例与 latency budget。Synthetic set 测 idealized coverage，authentic set 测真实输入鲁棒性，两者不能互相替代或合并成单一平均分。
- **边界：** 1,851 个 Gemini Notebook synthetic queries 与 322 个学生 survey queries 来自一个大学 faculty information system；authentic 平均 6.8 words、synthetic 15.7，source coverage 53 vs 165，hybrid retriever 在该场景最高约 8× latency。survey 不是生产流量，结果不证明 sparse/hybrid retrieval 普遍无益；上线前应持续以真实流量重估，并在真实样本不足时同时保留 synthetic coverage baseline。

### Residual Completion — `arXiv:2609.13800v1`

- **证据位置：** §3 Methodology、§4 Experiments。
- **采用命题：** stateful handoff 应保存 accepted choices、已发生 effects、未完成 obligations 与受限 action set；接手者只补 residual work，并由 checker 验证结果。
- **边界：** 五个环境、两个同 provider pairs 与 22–34.6% cost overhead 不覆盖开放网络和并发外部副作用；保证依赖完整 contract construction。Ch81 已承载该长期命题。

### Persistent Memory Poisoning — `arXiv:2609.13889v1`

- **证据位置：** §3 Methods / Threat Model、§4 Experiments / Defenses。
- **采用命题：** 恶意内容写入长期 memory/skill 后可延迟触发；prompt-only defense 在写入完成后不拥有可信清除能力，必须在 write/read/effect 三个边界保留 provenance、taint 与 quarantine。
- **边界：** OpenClaw、Claude Code 与所测 backbones/modalities/triggers 不给出开放世界攻击率；Ch72 已明确持久状态双时点检查。

### FlowSeal — `arXiv:2609.14003v1`

- **证据位置：** §V Defense、§VI Evaluation、§VII Ablation、§VIII Real-world Study、§IX Discussion。
- **采用命题：** tool interceptor 可在模型下方传播 provenance/IFC labels，并只通过显式 declassification 释放数据；LLM 是 policy sensor，不拥有 flow authority。
- **边界：** 三个 benchmarks、五个 prompt baselines、八类 attacks 与 live MCP 只覆盖标注、provenance 和 interceptor 完整的路径；隐式通道、漏标、未知 side effect 仍未关闭。Ch72 已覆盖该机制。

### Unnecessary Tool Availability — `arXiv:2609.14157v1`

- **证据位置：** §3 Setup、§4 Benchmark、§5 Experimental Setup、§6 Results / Mitigation。
- **采用命题：** 即便没有实际 tool call，暴露无关工具也会改变回答策略和 closed-answer correctness；tool registry 应在 prompt 构造前做 scope-aware admission，而不是把全量 catalog 当中性上下文。
- **边界：** 500 query pairs、10 domains、6 LLMs 中 answer rate 从 98.2% 降至 63.5% 是作者条件；不证明任意模型、工具 schema 或任务都同幅下降。

### Carryover Drafting — `arXiv:2609.14717v1`

- **证据位置：** §2 Method、§3 Setup、§4 Results、§5 Mechanism、§6 Discussion。
- **采用命题：** speculative decoding 中被 target 拒绝的 verifier hidden states 可以转成仅供下一轮 proposal 的临时 drafter KV；拒绝分支不得越过 target commit frontier。
- **边界：** DFlash/DSpark-derived drafters、两个 targets 与 vLLM 中 acceptance +6.5–14.7%、speed +7.9–14.4% 受 proposal block、训练和 overhead 限制。

### Pull — `arXiv:2609.14773v1`

- **证据位置：** §3 Method、§4 Setup、§5 Experiments、§6 Discussion / Limitations。
- **采用命题：** working memory 可保存 deterministic metadata directory，按 query 懒惰 materialize 原始 evidence；失败时撤销读取视图，不用不可逆 summary 取代 source state。
- **边界：** LoCoEval 128 conversations/12,780 turns、routing 7,831×10 与 BEAM1M 14 conversations/263 queries 受 selector、missing evidence 与 judge 影响。

### AgentKV — `arXiv:2609.14872v1`

- **证据位置：** §3 Method、§4 Evaluation、Limitations。
- **采用命题：** agentic KV eviction 应区分 think/act/tool phases，并用受限 query buffer 表示未来 query mixture；phase classifier 只提交 eviction hint，exact KV owner 保留回退与跨轮 identity。
- **边界：** 两个模型、六个 domains、三个 budgets 不能证明 phase classifier 在分布漂移、工具长等待或任意模型中可靠。

### ActGuard — `arXiv:2609.14987v1`

- **证据位置：** §3 Method、§4 Experiments 及 Appendix。
- **采用命题：** pre-execution action audit 可把 local tool prior、evidence localization 与 verifier sanitization 组合，但仍必须位于 deterministic authorization 前，不能自己提交副作用。
- **边界：** AgentDyn/AgentDojo 和作者攻击只证明该组合在所测环境提高 detection；新增 trusted component、延迟与 adaptive attack surface。Ch72 已有相同 authority boundary。

### Overflip — `arXiv:2609.15013v1`

- **证据位置：** §3 Threat、§4 Setup、§5 Results、§6 Discussion / Limitations。
- **采用命题：** guardrail label 在长输入中可能因无害 repetition 发生方向翻转；release evaluation 必须扫描 length × repetition pattern，而不能把一次短输入 verdict 当稳定 classifier property。
- **边界：** 9 个 guardrails、100 prompts 中 5 个出现首次翻转（2.6k–9.4k tokens）；不是所有 guardrail 的普遍规律，attention dispersion 证据也不是完整因果证明。

### Agent-tool Effect Histories — `arXiv:2609.15397v1`

- **证据位置：** §2 Effect Histories、§3 Anomalies、§4 Transactional Contracts、§5 MCP Survey。
- **采用命题：** tool call success 只证明 observation 返回，不证明 world effect 已提交；workflow 应记录 effect history、幂等身份、rollback/compensation 与 observation reconciliation，处理八类 agent-tool boundary anomaly。
- **边界：** 形式模型和 98,291 个 MCP tools 的 survey 暴露 capability annotation 缺口，但不证明 black-box tools 已提供所需 transaction semantics。
