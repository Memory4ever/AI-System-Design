"""Curated exact-v1 evidence for the frozen 2026-06-19 denominator.

Every locator names a non-abstract section or appendix in the exact arXiv v1.
Benchmark fields contain only conditions disclosed by that version; absence is
represented by the literal contract value ``Not Disclosed``.
"""

ND = "Not Disclosed"


def loc(aid: str, anchor: str, heading: str) -> str:
    return f"https://arxiv.org/html/{aid}v1#{anchor} — §{heading}"


# aid: method anchor/heading, evaluation anchor/heading, limitation anchor/heading
SECTIONS = {
    "2606.19692": ("S5", "5 Incremental Systems Architecture", "S9", "9 Systems Evaluation", "S13", "13 Limitations and Discussion"),
    "2606.19704": ("S4", "4 Predictive Validity as the Ranking Criterion", "S6", "6 Implications for Benchmark Design", "S8", "Limitations"),
    "2606.19714": ("S4", "4 Methodology", "S6", "6 Experiments", "A5", "Appendix E Experimental Details"),
    "2606.19719": ("S3", "3 Cache-Aware Metrics", "S4", "4 Experimental Setup and §5 Results", "A2.SS4", "Appendix B.4 Quality Considerations and Limitations"),
    "2606.19746": ("S4", "4 System Design", "S5", "5 Evaluation", "S6", "6 Discussion"),
    "2606.19753": ("S2", "2 Grounded Inference Primitives", "S5", "5 Reference Architecture", "S7", "7 Generative Model Risks"),
    "2606.19755": ("S3", "3 Methodology", "S4", "4 Experiments and §5 Ablation", "A1", "Appendix A Experimental Setup and Safety Head"),
    "2606.19758": ("S4", "4 Methodology", "S5", "5 Experiments", "A3", "Appendix C Fallback Routing"),
    "2606.19769": ("S5", "V Data Standards as Infrastructure", "S6", "VI Implementation Priorities", "S4", "IV Why More Data Is Not Enough"),
    "2606.19795": ("S3", "3 Handoff Contracts, Objects, and Coordination", "S6", "6 Unified Handoff Protocol", "S1.SS2", "1.2 Limitations of Existing Surveys and §1.3 Scope"),
    "2606.19803": ("S2", "2 FGAC Policy Model", "S4", "4 Preliminary Experiments", "S5", "5 Discussion and §6 Future Work"),
    "2606.19808": ("S4", "4 Selective Verification Method", "S5", "5 Experimental Setup and §6 Results", "A10", "Appendix J Limitations and Deployment Considerations"),
    "2606.19847": ("S3", "3 AtomMem Methods", "S4", "4 Experiments", "S5", "5 Conclusion and Limitations"),
    "2606.19849": ("S3", "3 Stage-Wise Coordinated Streaming", "S4", "4 Experiments", "S5", "5 Accuracy-Latency and Resource-Constrained Parallelism"),
    "2606.19868": ("S3", "III Uncertainty-Estimation Taxonomy", "S4", "IV Experimental Setup", "S6", "VI Conclusion and Future Work"),
    "2606.19887": ("S3", "III FinRED Framework", "S4", "IV Experiments and §V Expert Validation", "S6", "VI Reliability and Limitations"),
    "2606.19898": ("S3", "3 Rule-Based Router and §4 ML Router", "S6", "6 Experiments", "S7", "7 Conclusion and Limitations"),
    "2606.19899": ("page=9", "PDF pp.9–15 Capability-Evaluation Methods", "page=16", "PDF pp.16–26 Evaluation Results", "page=28", "PDF pp.28–30 Limitations and Risk Interpretation"),
    "2606.19911": ("S3", "3 Multi-Agent Transactive Memory", "S4", "4 Experimental Setup and §5 Results", "S6", "6 Discussion"),
    "2606.19989": ("S2", "2 Online Dynamic Batching System Design", "S4", "4 Experimental Evaluation", "S5", "5 Scope and Limitations"),
    "2606.19992": ("S3", "3 ToolPro Design", "S4", "4 Experiments", "S5", "5 Limitations and Discussion"),
    "2606.19998": ("S3", "3 Tri-Info Method", "S4", "4 Experimental Setup and §5 Results", "S5.SS4", "5.4 Conclusion and Limitations"),
    "2606.20002": ("S2", "2 Connect-the-Dots Framework", "S3", "3 Implementations and Experiments", "S4", "4 Analysis and Limitations"),
    "2606.20005": ("S3", "3 StreamKL Forward/Backward Pass", "S5", "5 Experiments", "S6", "6 Limitations and Discussion"),
    "2606.20023": ("S2", "2 Privilege Model and Selection Analysis", "S3", "3 Evaluation Setup and §4 Empirical Analysis", "S5", "5 Mitigation and Limitations"),
    "2606.20047": ("S3", "3 PACMS System Design", "S5", "5 Evaluation", "S5.SS2", "5.2 Scope and Limitations"),
    "2606.20113": ("S3", "3 Problem Formalization and Stabilization Controller", "S5", "5 Experiments", "S6", "6 Limitations"),
    "2606.20122": ("S4", "4 Utility-Guided Dynamic Outline Optimization", "S5", "5 Experiments", "S6", "6 Limitations and Discussion"),
    "2606.20128": ("S3", "3 Differential Correctness Method", "S4", "4 Evaluation", "S6", "6 Limitations"),
    "2606.20158": ("S2", "II N-Version Coding-Agent Architecture", "S3", "III Experimental Methodology and §IV Results", "S5", "V Threats to Validity"),
    "2606.20235": ("S3", "3 ScholarQuest Construction", "S5", "5 Evaluation", "S6", "6 Limitations"),
    "2606.20243": ("S3", "III Phoenix System Architecture", "S4", "IV Evaluation", "S5", "V Discussion and Limitations"),
    "2606.20245": ("S3", "III Explicit Knowledge-Conflict Methodology", "S4", "IV Experiments", "S5", "V Limitations"),
    "2606.20254": ("S4", "4 Threat Model and §5 Task-Arithmetic Removal", "S6", "6 Evaluation", "S7", "7 Limitations"),
    "2606.20318": ("S4", "4 AgenticDB Design", "S5", "5 Evaluation Methodology and §6 Results", "S7", "7 Limitations and Discussion"),
    "2606.20363": ("S4", "4 Automated SKILL.md Generation", "S5", "5 Experiments", "S6", "6 Limitations"),
    "2606.20374": ("S3", "3 ARGUS System Overview", "S4", "4 Runtime Monitoring and Diagnosis Evaluation", "S6", "6 Limitations"),
    "2606.20381": ("S4", "4 UFP4 Recipe", "S5", "5 Experiments", "S6", "6 Limitations and Discussion"),
    "2606.20408": ("S3", "3 NRT-Bench Design", "S4", "4 Experimental Setup and Evaluation", "S6", "6 Limitations"),
    "2606.20470": ("S3", "III Defense and §IV Misdirection", "S5", "V Simulation Evaluation", "S6", "VI Limitations"),
    "2606.20474": ("S4", "4 Ultra-TurboQuant and §5 UltraQuant", "S6", "6 Accuracy and §7 Systems Evaluation", "S8", "8 Limitations"),
    "2606.20475": ("S3", "3 Marginal-Advantage Accumulation", "S4", "4 Experiments", "S5", "5 Limitations"),
    "2606.20487": ("S3", "3 Hierarchical Recovery Methodology", "S4", "4 Experiments", "S5", "5 Failure Analysis and Limitations"),
    "2606.20493": ("S3", "3 Contagion Network Model", "S4", "4 Experiments", "S5", "5 Limitations"),
    "2606.20502": ("S3", "III Methodological Framework", "S4", "IV Results", "S6", "VI Limitations"),
    "2606.20510": ("S3", "3 Verification Optimization and §4 Relaxation", "S5", "5 Evaluation", "S6", "6 Limitations"),
    "2606.20512": ("S3", "3 Probe-and-Refine Design", "S4", "4 Evaluation through §7 Cross-Model Analysis", "S9", "9 Limitations"),
    "2606.20520": ("S4", "4 Broker Execution and §5 Scoped Identity", "S8", "8 Evaluation and §9 Security Analysis", "S10", "10 Discussion and Limitations"),
    "2606.20529": ("S3", "3 LedgerAgent Method", "S4", "4 Experiments", "S5", "5 Limitations"),
    "2606.20536": ("S3", "3 Experimental Setup", "S4", "4 Experiments", "S5", "5 Limitations and Recommendations"),
    "2606.20537": ("S2", "2 FlashRT Runtime Substrate and Execution-State Capsules", "S4", "4 Evaluation", "S5", "5 Limitations"),
    "2606.20545": ("S3", "3 WRBench Suite and Persistent-State Diagnostics", "S4", "4 Evaluation", "S5", "5 Limitations"),
    "2606.20553": ("S3", "3 Threat Model and §4 Privacy-Backdoor Attack", "S5", "5 Evaluation", "S6", "6 Limitations"),
    "2606.20562": ("S3", "3 MemoryWAM Method", "S4", "4 Experiments", "A1", "Appendix A Additional Results and Limitations"),
    "2606.20754": ("S3", "III Perturbation-Based Uncertainty Methodology", "S4", "IV Experiments", "S5", "V Limitations"),
    "2606.20758": ("S3", "3 Four-Tier Memory and §4 Derive-Then-Explain", "S5", "5 Evaluation", "S6", "6 Limitations"),
    "2606.20785": ("S2", "2 Scalable Environments, Solvers, and Verifiers", "S4", "4 Experiments", "S6", "6 Discussion and Limitations"),
    "2606.20814": ("S2", "2 Overall Setup and Training Dynamics", "S4", "4 Model and Data Comparisons", "S5", "5 Limitations"),
    "2606.20820": ("S2", "2 Certifiable and Efficient Evaluation: Setup and Overview", "S5", "5 Empirical Evaluation", "A5", "Appendix A.5 Limitations"),
    "2606.20839": ("S2", "2 Process-Reward Tactic Evolution", "S3", "3 Experiments and §4 Main Results", "S5", "5 Limitations"),
    "2606.20873": ("S2", "2 SciLens Framework", "S3", "3 Experiments", "S4", "4 Limitations"),
    "2606.20898": ("S3", "3 Methodology", "S4", "4 Results", "S5", "5 Discussion and Limitations"),
    "2606.20910": ("S3", "III MARK Multi-Layer Fingerprinting", "S4", "IV Measurement Setup and Results", "S5", "V Limitations"),
    "2606.20922": ("S4", "4 Isolated Planning Defense", "S5", "5 Implementation, Performance, and Overhead", "S6", "6 Limitations"),
    "2606.20954": ("S3", "3 Long-Horizon Memory Methodology", "S4", "4 Experimental Setup and §5 Results", "S6", "6 Limitations"),
    "2606.20969": ("S4", "4 AutoACSL and §5–6 Static-Analysis Integration", "S7", "7 Experiments", "S8", "8 Limitations"),
    "2606.20978": ("S3", "3 Hierarchical Demonstration Format", "S4", "4 Experiments", "S5", "5 Limitations"),
    "2606.21005": ("S3", "3 Agent-Harness Method", "S4", "4 Experimental Setup and §5 Results", "S6", "6 Analysis and Failure Modes"),
}


PDF_ONLY = {"2606.19899"}
MIRROR_FALLBACK = {"2606.20820"}


# Source-specific durable mechanism/control delta and exact-v1 non-proof boundary.
DETAILS = {
    "2606.19692": (
        "旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。",
        "结论限于单向量 cosine 检索、固定 encoder、两个 10 万文档语料和给定攻击；organic hubs 在冻结阈值下大量被标记，targeted single-query、late-interaction、multi-vector 与模型内部投毒未验证。",
    ),
    "2606.19704": (
        "它不再用单次 aggregate mean 排名决定发布，而要求 evaluation owner 保存 configuration identity，并以 in-sample/OOD rank correlation、judge-independent trajectory verifier 和持久 benchmark transport 判断配置能否外推；旧 leaderboard 可保留为观测列，不能继续拥有 release 决策。",
        "这是基于 AssetOpsBench 与 14 份未同行评审 implementation reports 的 position paper；作者未运行大规模 predictive-validity trial，也未证明十二层正交或排名与真实 incident/override 指标相关。",
    ),
    "2606.19714": (
        "AURA 把 judge trust 作为可更新隐状态：人类只验证 uncertainty 高的 pair，refinement 将已验证的一致性信号传播到其余比较，再更新下一轮采样；evaluation owner 而非 judge 独占抽样、停止和审计轨迹。其代价是传播错误会放大初始偏差，需保留随机抽检和预算耗尽时的原始 judge/human fallback。",
        "证据来自 5×640 合成比较与一组真实 pairwise judge 数据；未证明在开放域、judge 分布漂移、非 pairwise 评价或极低 human budget 下仍校准。",
    ),
    "2606.19719": (
        "语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。",
        "74,265 个英文 pair、45% 正例、9 个 bi-encoder/reranker 的结果受 ParaBank2 与合成数据占比、标签噪声及部署先验约束；固定 test mix 不证明低重复率生产流量。",
    ),
    "2606.19746": (
        "dense-attention 时代的 RDMA 全 prefix 搬运被改为 CXL cache-line top-k 按需读取：prefill 把 KV 写入共享池，scheduler 按设备分配请求，decode GPU 只取 sparse attention 选中的条目；KV owner 从单 GPU/整块传输变成 CXL pool 与调度器协同。失败时仍需本地 DRAM/RDMA 路径，代价是 CXL 拓扑、细粒度访问和设备争用。",
        "只验证 DeepSeek-V3.2 AWQ4、SGLang/HiSparse、8×H20、2TB CXL、16K–128K/1K 输出；RDMA 是本机 loopback 的理想化基线，不能证明跨机、dense attention 或其它 CXL 设备收益。",
    ),
    "2606.19753": (
        "该文把概率模型封装为受类型化输入、可验证输出、超时/失败状态和确定性 orchestration 约束的组件，主程序保留状态与最终 authority；但它是架构原则而非新的可复算实现，作为现有 grounded-inference 原则的补充而不追加 Books 机制。",
        "没有公开 workload、实现 artifact 或对照实验；四个 primitive 与两个 anti-pattern 未被量化验证，不能据此声称确定性、可靠性或生产风险已经闭合。",
    ),
    "2606.19755": (
        "SafeSpec 将安全 head 并入 target verification 的同一次前向：draft token 通过语义与风险联合门，风险触发 rollback 和 safety-guided multi-sampling，而非在 speculative path 外串联 guard。target verifier 持有 accept/rollback 控制；外部 guard 仍作为未知攻击与 head 故障 fallback。",
        "15% ASR 降幅与 2.06× benign speedup 绑定 Qwen3-32B、论文所列攻击集和 6×A800；latent head 不能证明新型 jailbreak、跨语言或 target/draft 变更后仍校准。",
    ),
    "2606.19758": (
        "SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。",
        "结果仅覆盖六个 reasoning/coding benchmark、三个 base LLM 和论文 skill libraries；0.96-point unseen-library drop 不证明开放技能供应链、权限隔离或长任务稳定性。",
    ),
    "2606.19769": (
        "它把 humanoid 数据 owner 从孤立样本仓库提升为 lifecycle contract：每条经验绑定 body/action/task/scene/trace/outcome，并保留时间、坐标系、标定、运动学、单位、版本和 provenance；capability-specific schema 在水平标准之上扩展，旧数据只能经显式兼容层进入训练。",
        "材料源于 ISO/WD 26264-1 制定经验而非完成标准或跨厂商 benchmark；未证明提议字段足以消除硬件差异、隐私/IP 限制和 sim-to-real 偏移。",
    ),
    "2606.19795": (
        "EDA agent handoff 从传文件/自然语言升级为 consumer-defined acceptance contract：artifact 连同 scope、evidence、provenance、authority 和 workflow state 传递，下一 stage 显式 accept/reject；EACP 分离 discovery、message、tool、workflow 与 security/IP 层。旧 stage-local check 共存，但不能替代跨边界交付证据。",
        "这是 82 个系统的 survey/protocol proposal，没有端到端 EACP 实现或 signoff benchmark；五层协议未证明能覆盖供应链 IP、工具副作用和组织级授权。",
    ),
    "2606.19803": (
        "向量检索不再先 ANN 后应用层过滤，而把 subject/object/policy 与 approximate candidate generation 共同求解；policy engine 拥有可见集合，ANN 只在授权候选内优化 recall/latency。pre/post-filter 可作为规模与索引能力不同的共存路径，但必须分别报告漏检和越权风险。",
        "论文仅给 formal model 与 preliminary experiments；未覆盖动态 policy、跨租户缓存、删除一致性或所有向量数据库实现，不能宣称 FGAC 与 ANN recall 已同时普适最优。",
    ),
    "2606.19808": (
        "SEVRA 把额外推理视为 serving allocation：冻结 solver 先产出 attempt，recoverability gate 决定保留、验证或 bounded retry；scheduler 拥有 token budget 和 harmful-flip 审计。较长 initial budget 在部分任务更优，因此 controller 必须与 no-verify/longer-solve 路径共存。",
        "76.3%/26.8% 与 transfer 数字限于 Qwen3-4B、MATH500/GSM8K/CommonsenseQA 和给定 token budgets；不证明 gate 在新模型、开放题或负载漂移下优于先增加初始预算。",
    ),
    "2606.19847": (
        "AtomMem 以 Fact Executor 将长对话压成高价值 atomic facts，按事件层次与 temporal profile 演化，并由 associative graph 在查询时联结；memory owner 控制 extract/update/retrieve，原始对话保留为冲突校验 fallback。代价是事实抽取错误、属性覆盖和图扩散会造成不可逆记忆漂移。",
        "只在 LoCoMo 的多类 reasoning 指标上比较；未证明真实多会话隐私、删除、冲突事实、跨语言或长期 profile 更新正确。",
    ),
    "2606.19849": (
        "ViCoStream 将 video preprocessing、encoder、token drop、prefill/decode 统一到 chunk scheduler，以 CUDA-stream overlap、bounded visual attention 和 query retrieval 控制每 chunk 计算/内存；调度器拥有 stage backpressure，降载时通过 token retention/attention scope 回退，而非让单模块各自最大化。",
        "134 FPS 与 <50 ms TTFT 仅对应 Qwen2.5-VL-3B/7B、单 A100 和论文 streaming benchmarks；精度接近 full-history 不证明长时依赖、并发请求或其它 GPU。",
    ),
    "2606.19868": (
        "统一框架把 black-box UE 的 verbalization、sampling、explanation、multi-agent 与 hybrid 信号放到同一 evaluator contract；但 24 方法无单一 winner，现有评测章已包含按 task/calibration 选择 UE 的原则，因此记为 No Change。",
        "24 方法×4 模型×4 数据设置不能证明跨 API 版本、开放生成或成本约束下的统一最优；answer-space/hybrid 优势是设置相关观察。",
    ),
    "2606.19887": (
        "FinRED 用专家 taxonomy 生成金融 red-team 样例并由专家复核标签/可靠性，属于现有 domain-specific evaluation pipeline 的实例；它未改变通用 release owner，故只作 No Change handoff。",
        "专家一致性和覆盖只适用于论文金融风险 taxonomy、模型与样本；未证明其它司法辖区、实时市场或非金融安全域。",
    ),
    "2606.19898": (
        "filtered ANN 从静态单索引选择变为 query-aware router：规则或 learned policy 依据 filter selectivity/shape 将查询送往不同索引路径；router 拥有 plan choice，监测失配时回落到精确过滤或保守规则。代价是训练分布漂移会把 latency 优化变成 recall 回归。",
        "实验绑定论文数据分布、filter 模式、索引实现和 recall/latency 指标；未证明动态更新、复杂布尔 policy 或跨 tenant workload。",
    ),
    "2606.19899": (
        "该工作把生物能力/风险拆为可操作 task suites、agent scaffold 与分级 risk interpretation，但仍属于垂直 benchmark；现有 evaluation 章节已要求 domain expert、capability 与 misuse 分离，故不新增机制。",
        "PDF 评测不能把受测 agent 的实验室能力直接外推为现实生物危害；任务覆盖、工具 access、专家评分和风险阈值均是特定设计。",
    ),
    "2606.19911": (
        "多 agent 记忆从各自 transcript 变为 transactive directory：agent 保存谁知道什么与证据位置，查询先路由到 memory owner 再取内容；目录过期时回落到广播/共享检索。其收益以额外索引维护、错误 expertise attribution 和隐私边界为代价。",
        "只在论文 multi-agent tasks、拓扑和模型上验证；未证明目录在 agent churn、对抗写入、跨组织权限或长期知识漂移下可靠。",
    ),
    "2606.19989": (
        "训练 batching 从离线固定 batch 改为 online queue policy，在到达、长度与资源状态变化时决定组合，同时以形式化界约束等待/效率；scheduler 拥有 batch formation，超出假设时退回静态 bucket。代价是在线估计误差与公平性。",
        "形式保证依赖论文到达与成本模型；未证明真实多租户数据 loader、straggler、网络/optimizer 状态或非平稳长度分布满足假设。",
    ),
    "2606.19992": (
        "Tool Programs 将静态 endpoint 列表变成可组合、带类型与执行语义的服务接口；服务端拥有 program validation/sandbox，agent 只提交受限程序，失败时回落到单步 endpoint。灵活性以验证复杂度、资源上界和更大的代码注入面为代价。",
        "实验只覆盖作者 web-service/tool tasks；未证明任意第三方 API、副作用事务、认证轮换或不可信程序可安全执行。",
    ),
    "2606.19998": (
        "Tri-Info 用 VLA 内部 information signals 预测 action failure，并把 abstain/fallback 交给执行控制器；旧做法只看 action likelihood 或单一 uncertainty。代价是 probe 与阈值需随 policy/environment 校准，未知 shift 时回落到人工/安全 controller。",
        "只在论文 VLA 模型、任务与 failure labels 上验证；离线 AUROC/检测率不证明真实机器人动作安全、因果故障或跨 embodiment 泛化。",
    ),
    "2606.20002": (
        "Connect-the-Dots 用跨 domain、跨 lifecycle 的 RL trajectory 把短任务 reward 改为长期 agent state transition 信号；trainer 拥有 curriculum、reward 与 checkpoint selection，旧单域 SFT/RL 作为稳定初始化。代价是跨域 reward leakage 和 credit assignment，失败时需回退到分域训练/验证。",
        "结果限于 exact-v1 domains、模型、reward verifier 和 rollout budget；未证明开放世界长期记忆、真实工具副作用或跨生命周期泛化。",
    ),
    "2606.20005": (
        "StreamKL 将 attention distillation 的 KL 计算分块流式执行，避免物化完整概率张量；kernel/trainer 共同拥有 block state 与数值归约，OOM 或不支持 shape 时回退到标准 KL。速度/显存换来额外 kernel、归约误差和硬件依赖。",
        "只验证论文 attention shapes、精度、模型与 GPU；未证明所有 vocab/sequence 规模、分布式并行或低精度下保持相同数值和收敛。",
    ),
    "2606.20023": (
        "工具选择不再只优化成功率，而先求满足任务的最小 capability set；planner 提议工具，policy layer 比较 privilege lattice 后降权/拒绝 over-privileged choice，并保留必要时显式 escalation。代价是 capability annotation 不全会误拒绝或低估组合权限。",
        "测量与 mitigation 绑定论文 agent/tool suites 和 privilege labels；未证明动态 OAuth scope、跨工具权限合成或恶意 metadata。",
    ),
    "2606.20047": (
        "PACMS 把 context assembly 表述为预算约束 submodular selection：独立 engine 根据 relevance、coverage 与 redundancy 选取片段，agent 消费带 provenance 的 context；不足时回落到更大窗口或检索重试。代价是 utility surrogate 可能遗漏依赖和顺序。",
        "评测限于论文任务、预算、retriever 与 utility 定义；submodular 近似不证明长依赖、冲突证据或对抗 context 下答案正确。",
    ),
    "2606.20113": (
        "streaming tool use 不应在第一个 token 触发；controller 追踪 tool-intent 随解码的稳定度，在置信轨迹达到阈值后才 dispatch，未稳定则继续生成或回落到完整 query。它用 latency 换误调用率，并要求 cancellation/duplicate suppression。",
        "稳定阈值与收益只在论文 retrieval tasks、模型、网络延迟和工具集上测得；未证明有副作用工具、长参数或分布漂移。",
    ),
    "2606.20122": (
        "ScaffoldAgent 将 deep-research outline 变成可迭代控制状态：每轮按预期 utility 增删/重排子目标，再据证据覆盖继续搜索；planner 拥有 outline version，budget 用尽则冻结当前结构并交给 verifier。代价是 utility 估计会偏向易检索证据。",
        "实验仅覆盖论文开放研究任务、搜索后端和 judge；未证明 factuality、source authority、长时间网页漂移或真实研究验收。",
    ),
    "2606.20128": (
        "GPU kernel 验收从单设备单输入通过改为 CPU oracle、跨 shape/dtype/GPU differential testing 与 clean controls；release owner 保存失败 witness，并在 verdict 不一致时拒绝上线或回退原 kernel。代价是 oracle/设备矩阵成本和未覆盖输入。",
        "24/26 ops 与 RTX3060/A10/L40S/A100/H100 的测试仍不穷尽未定义行为、驱动版本、并发或大模型端到端性能。",
    ),
    "2606.20158": (
        "N-version coding agents 并行产出独立实现，由测试/静态检查和 adjudicator 汇合，而非信任单次生成；workflow owner 管理 diversity、quorum 与 fallback 到人工。额外 token/latency 的收益依赖故障独立性，相关 hallucination 会击穿多数表决。",
        "结果只覆盖论文 coding tasks、agent versions 与 test suites；未证明安全漏洞、缺失 oracle、共享训练数据导致的相关错误。",
    ),
    "2606.20235": (
        "ScholarQuest 提供 taxonomy-guided academic-search benchmark，但没有改变 evaluation/release 控制权或现有 paper-search owner，因此不追加 Books。",
        "benchmark 覆盖开放文献环境与既定 taxonomy；分数不证明封闭数据库、未来索引、全文权限或科研结论正确。",
    ),
    "2606.20243": (
        "Phoenix 的 multi-agent issue-resolution safety pipeline 已被 workflow 章的隔离执行、review gate 与 rollback 原则覆盖；本日只保留实现 handoff，不重复 owner。",
        "GitHub issues、repositories、tests 与 agent 配置是特定实验；测试通过不证明 supply-chain、secret、部署或未测试行为安全。",
    ),
    "2606.20245": (
        "显式 parametric/context knowledge conflict resolution 属于现有 context provenance 与冲突裁决路径；该研究没有新增跨系统 state owner，故 No Change。",
        "实验只验证给定冲突构造、模型和问答集；显式选择不能证明来源真实性、时效性或隐式冲突被发现。",
    ),
    "2606.20254": (
        "量化不再被当作纯压缩步骤：security owner 将 quantization-conditioned backdoor 视作可分离 task vector，在发布前比较全精度/量化行为并用 task arithmetic 移除，再做 clean/attack 双验收。无法分离时回退到拒绝量化模型。",
        "移除效果限于论文 backdoor construction、模型、bit-width 与 calibration data；未证明未知触发器、其它量化器或 task-vector subtraction 不损害能力。",
    ),
    "2606.20318": (
        "AgenticDB 将数据库 reconfiguration 变成 telemetry→proposal→sandbox evaluation→guarded apply→rollback 的闭环；DB control plane 而非 LLM 持有变更权限和状态版本。代价是试验流量与错误 cost model，fallback 为上一配置和人工 approval。",
        "结果绑定论文 workloads、DBMS、动作空间和离线/沙箱指标；未证明生产突发流量、数据迁移、锁竞争或跨版本自动演进安全。",
    ),
    "2606.20363": (
        "SKILL.md 不再完全手写，而从 computer-use trajectory 中抽取可复用步骤、前置条件和 recovery，经过评测后发布；skill registry 拥有版本/验证，agent 只消费已批准 artifact。错误归纳时回退原 trajectory 或人工 skill。",
        "实验覆盖论文应用、轨迹质量和 computer-use agent；未证明 UI 漂移、敏感动作、跨 OS 或生成 skill 的供应链安全。",
    ),
    "2606.20374": (
        "ARGUS 将万卡训练诊断从节点日志提升为跨 rank/collective/network/storage 的统一 trace identity；collector 控制采样与时钟映射，diagnoser 只在证据图上定位瓶颈，超预算时降采样并保留关键 span。代价是 telemetry overhead 与相关性误判。",
        "生产观察来自特定 >10,000-GPU 集群、训练栈和故障集；trace 覆盖与诊断时延不证明因果根因、其它 fabric 或故障自动修复。",
    ),
    "2606.20381": (
        "UFP4 针对 FP4 pretraining 的 shrinkage bias 重新分配量化几何与 scaling，使 optimizer/quantizer 共同拥有低精度状态；异常 loss 时回退 BF16/更高精度。显存/吞吐收益以 recipe、kernel 和收敛敏感性为代价。",
        "只在 exact-v1 模型规模、token budget、FP4 hardware/simulation 与下游评测验证；未证明更长预训练、其它 optimizer 或最终能力无回归。",
    ),
    "2606.20408": (
        "NRT-Bench 将 operator-agent red teaming 组织成多轮控制室状态、攻击轨迹和 safety-critical acceptance，但作为垂直 benchmark 已被通用多轮安全评测契约覆盖，故 No Change。",
        "任务、模拟控制室、attackers 与 judges 不等同真实基础设施；benchmark 成功/失败不能外推为生产控制权限或事故风险。",
    ),
    "2606.20470": (
        "防御不只阻断 model-guided attacker，还可发布受控假信号改变攻击者 belief/update path；defender 拥有 decoy 状态与撤销，真实 agent state 不暴露。代价是误导污染 observability 与合法调试，故必须与直接拒绝、隔离和审计共存。",
        "结果来自论文 attack/defense simulation；未证明真实攻击者适应、法律/伦理约束、side channel 或 decoy 不伤害正常 agent。",
    ),
    "2606.20474": (
        "UltraQuant 将 agent 长上下文 KV 压到 4-bit，并分别控制 token/channel quantization 与 runtime dequant；cache manager 持有 format metadata，质量回归时按 layer/request 回退高精度。收益以 kernel 复杂度、误差累积和 workload sensitivity 为代价。",
        "质量与系统数字限于论文 models、context-heavy agent workloads、长度和 hardware；未证明极长上下文、不同 attention、并发 tail latency 或所有任务无损。",
    ),
    "2606.20475": (
        "memory self-evolution 不按单轮 reward 覆盖旧记忆，而累计候选记忆相对基线的 marginal advantage，再由 memory owner 决定 promote/retain/evict；低置信时保留旧版本。代价是 delayed credit 与 evaluator bias 会固化错误。",
        "实验仅覆盖论文 agents、tasks、judge 与 memory budget；未证明非平稳长期用户、对抗记忆或跨任务 advantage 可比较。",
    ),
    "2606.20487": (
        "跨设备 agent 从全局 replanning 改为层级 recovery：设备局部 controller 先修复可逆错误，跨设备依赖破坏才升级 workflow planner；handoff state 保存 checkpoint/compensation。代价是故障分类错误，fallback 为全局重规划或人工。",
        "只验证论文 devices、tasks、failure injection 与 latency；未证明真实设备副作用、网络 partition、并发用户或补偿完整。",
    ),
    "2606.20493": (
        "它把 evaluator preference 看作多-agent 图上的传播状态，要求 evaluation owner 跟踪 judge influence/依赖，而非把 agent votes 当独立样本；检测到 contagion 时使用隔离 judge 或独立 anchor。代价是图估计与额外评审成本。",
        "结果来自论文 contagion model、拓扑和 LLM judges；未证明真实组织评审、隐藏共享训练或动态 agent 网络中的因果传播。",
    ),
    "2606.20502": (
        "该研究表明 vulnerability detector 可校准却不理解漏洞，支持现有 evaluation 章分离 confidence calibration 与 semantic correctness 的原则；没有新的长期 owner，故 No Change。",
        "结果绑定 systems-software 数据集、fine-tuning recipe、模型与漏洞标签；校准曲线不能证明新代码、组合漏洞或真实 exploitability。",
    ),
    "2606.20510": (
        "概率 verification 将 agent policy 的不确定转移纳入可计算验收，通过 relaxation 在 sound bound 与成本间调节；verifier 拥有 accept/reject，超时或 bound 过松时回退 conservative rule/human review。代价是状态抽象与概率模型误设。",
        "soundness 只对论文形式假设、抽象与概率界成立；实验不证明开放工具环境、非平稳 policy 或未建模副作用。",
    ),
    "2606.20512": (
        "repository guidance 从静态 README/AGENTS 文本变为 probe-and-refine：运行 coding agent，定位失败 step，再在固定 step budget 内修改 guidance 并跨模型验证；repo owner 持有发布/回滚，过拟合时保留旧指导。代价是 probe 成本和 benchmark leakage。",
        "结果限于论文 repositories、tasks、agents 和 step budget；未证明未来代码变化、隐藏测试、安全规范或跨模型长期泛化。",
    ),
    "2606.20520": (
        "Sovereign Execution Broker 将 prompt 声明的权限替换为 certificate-bound authority：principal 提交带 scope/expiry 的证书，broker 在工具执行前验证、记录并可 revoke；agent 不持有最终执行权。证书/身份漂移时 fail closed，并与人工 break-glass 共存。",
        "evaluation 只覆盖论文 broker、capability 和 attack scenarios；未证明所有第三方工具、密钥轮换、跨域 trust root 或 broker compromise。",
    ),
    "2606.20529": (
        "LedgerAgent 将 policy-relevant state 记录为结构化 append-only ledger，planner 每次工具调用前读取约束并提交可审计 transition；ledger/policy engine 拥有状态，LLM 不能静默改写。解析冲突时拒绝或转人工。代价是 schema 覆盖与写放大。",
        "实验限于论文 tool tasks、policy set 与 ledger parser；未证明并发事务、隐式状态、恶意工具返回或长期 ledger 压缩。",
    ),
    "2606.20536": (
        "FID 验收从单次 seed 分数改为显式训练 seed×生成 seed 分布与置信区间；evaluation owner 保存随机性来源，release 依据分布而非最好一次。增加重复成本，预算不足时至少报告 seed sensitivity 而非隐藏。",
        "数百个 SiT 网络和 ImageNet-256 的方差结论不证明其它生成架构、数据、采样器或人类质量；FID 本身仍不是完整质量/安全指标。",
    ),
    "2606.20537": (
        "Execution-State Capsule 在 graph-boundary 捕获可恢复的静态 buffer/执行状态，使 on-device small-batch serving 可 checkpoint/restore，而非重建整个 runtime；FlashRT 拥有 capsule schema 与兼容性，失配时冷启动。代价是图绑定、静态内存和 backend 特化。",
        "只验证 NVIDIA CUDA backend、论文 graph/model/batch 和设备；未证明跨 driver/backend、故障一致性、并发恢复或生产 tail latency。",
    ),
    "2606.20545": (
        "WRBench 把 camera motion 当 observability intervention，依次验证相机执行、在视场内连续性、离开视场后的状态演化和重新观察一致性；world-model evaluator 拥有 persistent-state verdict，普通 fidelity 指标仅并列。失败时回到显式 state memory/受限 camera。",
        "benchmark 只诊断论文 world models、camera paths 与 human calibration；未证明真实物理状态、因果动力学、长期遮挡或安全控制。",
    ),
    "2606.20553": (
        "联邦微调的效率路径被证明可承载 privacy backdoor；release contract 因此要在 client update 聚合前后检测泄漏触发与 utility，并由 server 持有 quarantine/rollback。安全聚合与效率优化需和隐私 red-team 共存。",
        "攻击与防御只在论文 FL topology、语言模型、clients 和 triggers 上验证；未证明 secure aggregation、异构数据或未知 covert channel。",
    ),
    "2606.20562": (
        "MemoryWAM 将 world-action model 的历史压入 persistent memory，在新 observation/action 时选择性读取和更新，使状态不完全依赖当前窗口；memory controller 拥有写入/遗忘，漂移时清空或回退无记忆 model。代价是错误状态累积和额外带宽。",
        "实验限于论文 environments、horizons、models 和 memory sizes；未证明真实机器人、不可逆动作、长期漂移或 memory poisoning。",
    ),
    "2606.20754": (
        "VLA failure detector 对 observation/action 表征施加受控扰动，以 action prediction 的变化量估计 epistemic risk，再由安全 controller abstain；相比重复 sampling，它把 shift sensitivity 放到执行前。阈值失配时回退人工/保守 policy。",
        "只验证 LIBERO/LIBERO-PRO、给定 VLA 与 perturbations；检测改善不证明真实硬件、未知 distribution shift、校准概率或安全动作。",
    ),
    "2606.20758": (
        "OPS CORTEX 用四层 operational memory 保存拓扑、正常模式、事件与历史故障；deterministic graph/threshold engine 先派生 root-cause candidate，LLM 只解释、确认和建议，不拥有因果判定或修复权限。图证据不足时回退人工 investigation。",
        "原型只在 instrumented e-commerce benchmark 的 8 个注入故障验证；threshold ordering 不是普遍因果证明，也未覆盖 topology drift、并发故障或生产 SLO。",
    ),
    "2606.20785": (
        "FaraGen1.5 将 computer-use 数据生成拆为 environment、solver、verifier 三个 owner：live/synthetic 环境承载动作，solver 生成多轮轨迹，三类 verifier 分别判断 correctness/efficiency/critical points；通过的轨迹再按缺陷迭代混入 SFT。不可逆/auth 场景由 synthetic environment 隔离。",
        "Fara1.5 4B/9B/27B 在 Online-Mind2Web/WebVoyager 的结果不证明真实网站漂移、账号安全、不可逆副作用或 verifier 对所有任务正确。",
    ),
    "2606.20814": (
        "训练审计不只看 narrow fine-tune loss，还保存 pretrained prior activations、训练/评测 prompt subspace overlap 与 alignment score trajectories；release owner 用这些信号发现 emergent-misalignment 风险，但不能把相关性当控制。失败时停止/回滚 checkpoint 并做行为评测。",
        "多组相关与未找到更好 local minima 的负结果绑定论文模型、数据和 prompts；activation overlap 不证明因果、可迁移 detector 或未来 fine-tune 安全。",
    ),
    "2606.20820": (
        "Celeus 用 e-process 构造 anytime-valid CI：sampler 依据 uncertainty 选样，surrogate 估计未评样本，evaluation scheduler 可在任意时间按 CI width 停止而保持 coverage；surrogate 失配时回退均匀抽样/有限总体界。代价是 i.i.d./有限池假设与校准开销。",
        "54–62% 样本节省来自 7–8B surrogate、67–72B dense/8×7B MoE target 与论文任务；population guarantee 假设 i.i.d. pool，distribution shift 尚未解决。",
    ),
    "2606.20839": (
        "Galaxy agent 将成功/失败 workflow trace 经 process verifiers 转成 tactic library，inference executor 先检索 tactic 再构造 DAG、绑定数据、监控与生物验收；workflow owner 保存 typed artifact/provenance，失败时回到无记忆或 reflection。代价是 tactic 污染与 domain verifier 成本。",
        "只验证隔离 Galaxy、BioWorkflow/BioAgent tasks、论文模型和 process rewards；未证明其它科学平台、真实数据权限或 biological correctness。",
    ),
    "2606.20873": (
        "SciLens 将科学 claim 分成 empirical/background atoms，再按 table cell/arithmetic 或 figure panel/axis/legend 建 witness，只有全部核心 atom entail 才支持；verifier 拥有 evidence graph，VLM 不能直接二分类。无法定位 witness 时 abstain。",
        "79.2 macro-F1/63.1 pair accuracy 只在 SciClaimEval dev set；未证明新学科、复杂统计图、OCR 错误或科学结论真实性。",
    ),
    "2606.20898": (
        "RAG 与 long-context 的 token/accuracy frontier 是 manufacturing case study，现有 RAG 章已覆盖 evidence access 与成本权衡；它没有新的控制或状态 owner，故 No Change。",
        "972 answers、3 machines、2 small models 的 73.1% vs 65.4%/26× token cost 不能外推其它 corpus、models、retriever 或更新频率。",
    ),
    "2606.20910": (
        "MARK 将 web-agent attribution 从 robots.txt/单层 bot flag 改为 TLS/HTTP 与 browser-action 多层 fingerprint，site policy engine 根据 attribution 决定 throttle/challenge；classifier 漂移时回退行为限流而非永久身份结论。代价是隐私、误报和可规避性。",
        "97% 只来自六种 agent framework、instrumented domain、当时网络/browser stack 与 decision tree；未证明未知 agent、代理重放或长期 evasion resistance。",
    ),
    "2606.20922": (
        "Tool-Guard 将 planning 与 poisoned tool description 隔离：检测到可疑/misaligned 调用后把对应 tool 加入 influenced list，后续规划不再看到其描述，但执行层仍可在受控条件下调用以保留 utility。policy owner 持有 quarantine，误报时可审计恢复。",
        "AgentDojo/ASB 的 attack-success 与 utility 只覆盖给定描述投毒、模型、detector 和工具；未证明多工具串谋、隐藏 side effect 或 detector evasion。",
    ),
    "2606.20954": (
        "LRE 用几 KB CPU scorer 在未来 query 未知时预测 history unit 是否 load-bearing，按 matched budget 保留原文而非神经压缩；memory manager 拥有 eviction，低置信时 pin credential/path 或回退更大窗口。代价是 scorer drift 与 verbatim 隐私存储。",
        "agent/LoCoMo 数字限于论文 traces、budgets 与 supervision；95% self-supervised effectiveness 不证明新任务、敏感 token、对抗 history 或无限时长。",
    ),
    "2606.20969": (
        "AutoACSL 以 CPG 静态特征构造 prompt，LLM 生成候选 contract，Frama-C/WP 反复验证/反馈直至证明或停止；formal verifier 持有 accept 权，LLM 只提案。终止未证时回退人工 specification。该闭环已由现有 tool-verifier workflow 覆盖，故 No Change。",
        "604 个 C program、四模型和 Frama-C/WP 的 98%/96% 不证明未覆盖 C 特性、外部函数、并发、错误 specification completeness 或其它 prover。",
    ),
    "2606.20978": (
        "PbD pipeline 不把录制动作平铺给 agent，而先按命名 subgoal 建层级，再保持相同 action sequence 供 planner 消费；demonstration owner 保存 grouping，描述已精确时可回退无示例。代价是人工/自动分段错误。",
        "85 个 web tasks 中优势只出现在 43 个模糊描述任务；精确描述的 42 个任务无收益，且未证明跨网站漂移、长 workflow 或自动 subgoal 标注。",
    ),
    "2606.21005": (
        "Beaver 把 multimodal scientific curation 拆成 evidence tools、task scaffold 与 artifact-grounded autoresearch；每轮保存属性级 provenance 和 stage-local failure，再由 harness owner 修订工具/流程。缺 witness 时不填值或转人工，而非让 frontier agent自由生成。",
        "81.0 GRAS 与 >23-point 增益限于论文 curation tasks、gold records、frontier agent 与 artifacts；provenance 不证明 source 本身正确或跨学科 schema 泛化。",
    ),
}


def bench(**values):
    fields = ("workload", "model", "hardware", "precision", "input_length",
              "output_length", "batch", "concurrency", "slo", "evaluator")
    return {field: values.get(field, ND) for field in fields}


BENCHMARKS = {
    "2606.19692": bench(workload="Two 100,000-document BEIR-composed corpora; 5,571/8,000 sentinels; embedding-space and HotFlip hub attacks", model="BAAI/bge-large-en-v1.5 plus MiniLM, BGE-base, GTE-large, E5-large-v2 sweep", hardware="Apple-silicon arm64 with MPS", precision="float32 embeddings", input_length="max sequence length 256; HotFlip length 32", concurrency="1–8 ingestion threads", evaluator="attack recall/AUROC at frozen 1% benign FPR; HNSW decision flips; ingestion latency/scaling"),
    "2606.19704": bench(workload="AssetOpsBench synthesis across 14 implementation studies and seven prior agent benchmarks", evaluator="Proposed in-sample/OOD rank correlation under three pre-registered criteria; experiment not run"),
    "2606.19714": bench(workload="Synthetic pairwise data: 5 runs × 640 comparisons; real pairwise LLM-answer judge data", evaluator="human-consistency recovery, uncertainty-directed label efficiency, ranking agreement and ablations"),
    "2606.19719": bench(workload="74,265-pair English test set with 45% positive labels", model="Nine retriever/reranker variants including MiniLM, GTE, ColBERT-family and LangCache models", precision="BF16 for disclosed LangCache training", input_length="128 tokens for LangCache-Embed-v3", evaluator="PR-AUC, P-CHR AUC, CRR, deployment precision, calibration/structural-gap decomposition"),
    "2606.19746": bench(workload="512 ShareGPT requests; cache-populate and cache-hit rounds", model="DeepSeek-V3.2 AWQ 4-bit on SGLang/HiSparse", hardware="8×NVIDIA H20 96GB; 2×Xeon Platinum 8575C; 2TB DRAM; 2TB CXL pool", precision="AWQ 4-bit weights; BF16 SGLang runtime", input_length="16K–128K tokens", output_length="1K tokens", concurrency="8 cache-populate; 64 cache-hit", evaluator="output-token throughput, TTFT, TBT versus RDMA loopback, host-DRAM and GPU-only baselines"),
    "2606.19753": bench(),
    "2606.19755": bench(workload="Multiple adversarial/jailbreak and benign workloads listed in exact-v1", model="Qwen3-32B target; Qwen3Guard-Gen-0.6B guard baseline; latent safety head", hardware="6×NVIDIA A800 80GB", evaluator="attack success rate, over-refusal, capability and speculative-decoding speedup"),
    "2606.19758": bench(workload="Six reasoning and coding benchmarks; unseen-skill-library transfer", model="Three base LLMs", evaluator="task score versus CARD and topology baselines; unseen-library performance drop"),
    "2606.19769": bench(),
    "2606.19795": bench(workload="Survey of 82 agentic EDA systems", evaluator="handoff-contract taxonomy; no empirical EACP benchmark disclosed"),
    "2606.19803": bench(workload="Preliminary policy-aware vector-search experiments disclosed in §4", evaluator="policy correctness, ANN recall and query latency"),
    "2606.19808": bench(workload="MATH500, GSM8K and CommonsenseQA reasoning tasks", model="Frozen Qwen3-4B solver", input_length="Initial solve budgets include 8,192 tokens", evaluator="accuracy, verification/post-generation tokens, harmful flips and realized total tokens"),
    "2606.19847": bench(workload="LoCoMo multi-session memory benchmark", evaluator="reasoning-task accuracy, memory size/cost and ablations"),
    "2606.19849": bench(workload="Multiple streaming-video benchmarks listed in exact-v1", model="Qwen2.5-VL-3B/7B-Instruct", hardware="Single NVIDIA A100", slo="Reported TTFT below 50 ms in tested configuration", evaluator="video FPS, TTFT, accuracy and stage-wise bottleneck/ablation curves"),
    "2606.19868": bench(workload="Four dataset settings", model="Four black-box LLMs; 24 uncertainty-estimation methods", evaluator="unified uncertainty quality/calibration comparison across method categories"),
    "2606.19887": bench(workload="FinRED expert-guided financial red-team benchmark", evaluator="red-team coverage/performance, expert validation and inter-rater reliability"),
    "2606.19898": bench(workload="Filtered-ANN query workloads and filter-selectivity regimes in §6", evaluator="recall/latency and routing accuracy against fixed rule/index paths"),
    "2606.19899": bench(workload="Biological capability and risk task suites in exact-v1 PDF", evaluator="task capability scores and expert risk interpretation"),
    "2606.19911": bench(workload="Multi-agent tasks and memory ablations in §4", evaluator="task success, retrieval/communication cost and transactive-directory ablations"),
    "2606.19989": bench(workload="Online LLM-training arrival/length traces in §4", evaluator="batching efficiency, waiting time/utilization and formal competitive guarantees"),
    "2606.19992": bench(workload="Agentic web-service tasks in §4", evaluator="task completion, tool-program flexibility and execution overhead"),
    "2606.19998": bench(workload="VLA failure-prediction tasks in exact-v1", evaluator="failure-detection discrimination/calibration and cross-setting generalization"),
    "2606.20002": bench(workload="Cross-domain long-lifecycle agent rollouts in §3", evaluator="cross-domain task success/generalization and RL ablations"),
    "2606.20005": bench(workload="Attention-distillation KL workloads in §5", evaluator="peak memory, runtime/throughput, numerical error and downstream distillation quality"),
    "2606.20023": bench(workload="Agent tool-selection tasks with privilege annotations", evaluator="task success, selected privilege excess and mitigation utility"),
    "2606.20047": bench(workload="Context-selection tasks and budgets in §5", evaluator="answer/task quality versus context tokens, latency and selection ablations"),
    "2606.20113": bench(workload="Streaming retrieval/tool-intent tasks in §5", evaluator="task success, tool-call timing, false dispatch and latency"),
    "2606.20122": bench(workload="Open-ended deep-research tasks in §5", evaluator="research-task quality, evidence coverage, cost and outline-optimization ablations"),
    "2606.20128": bench(workload="24-kernel corpus extended to 26 operations including flash attention", hardware="RTX 3060, A10, L40S, A100 SXM4 and H100 NVL", precision="FP64 CPU oracle; FP32/FP16/BF16 target cases", input_length="Operation-schema shape domains", evaluator="bug recall, clean-control precision and cross-GPU verdict consistency"),
    "2606.20158": bench(workload="Coding-agent tasks under N-version configurations", evaluator="functional correctness, failure correlation, adjudication accuracy and agent cost"),
    "2606.20235": bench(workload="ScholarQuest taxonomy-guided open-literature search tasks", evaluator="academic-search task success and taxonomy-specific retrieval/reasoning metrics"),
    "2606.20243": bench(workload="GitHub issue-resolution repositories and injected failure/safety cases", evaluator="issue resolution, test outcomes, unsafe-action rate and multi-agent ablations"),
    "2606.20245": bench(workload="Parametric-versus-contextual knowledge-conflict tasks", evaluator="conflict detection/resolution accuracy across knowledge conditions"),
    "2606.20254": bench(workload="Quantization-conditioned backdoor clean/attack suites", evaluator="attack success, clean utility and post-removal quantized-model quality"),
    "2606.20318": bench(workload="Database workloads and reconfiguration action space in §5", evaluator="workload performance, adaptation speed, unsafe/regressive changes and rollback"),
    "2606.20363": bench(workload="Computer-use interaction trajectories and held-out skill tasks", evaluator="skill execution success, generation quality and trajectory-mining ablations"),
    "2606.20374": bench(workload="Production distributed-training workloads and diagnosed incidents", hardware=">10,000-GPU cluster", evaluator="trace coverage, diagnosis latency/accuracy and production overhead"),
    "2606.20381": bench(workload="LLM FP4 pretraining configurations in §5", precision="FP4/UFP4 with higher-precision comparisons", evaluator="pretraining loss, downstream quality and shrinkage-bias diagnostics"),
    "2606.20408": bench(workload="NRT-Bench multi-turn operator-agent red-team scenarios in simulated control rooms", evaluator="attack success, safe task utility and multi-turn recovery"),
    "2606.20470": bench(workload="Model-guided attack/defensive-misdirection simulations", evaluator="attacker success/time/cost under defense and decoy strategies"),
    "2606.20474": bench(workload="Context-heavy agent workloads and long-context KV-cache traces", precision="4-bit KV cache with higher-precision baselines", evaluator="task quality, KV footprint, throughput and latency"),
    "2606.20475": bench(workload="Memory-driven agent self-evolution tasks in §4", evaluator="task success, memory utility, marginal-advantage accuracy and ablations"),
    "2606.20487": bench(workload="Cross-device agent tasks with injected local/cross-device failures", evaluator="recovery success, latency/cost and unnecessary global replans"),
    "2606.20493": bench(workload="Multi-agent evaluator networks/topologies in §4", evaluator="preference propagation, independence loss and intervention effectiveness"),
    "2606.20502": bench(workload="Systems-software vulnerability-detection datasets in §III–IV", evaluator="detection quality, calibration and comprehension/semantic probes"),
    "2606.20510": bench(workload="Probabilistic agent-verification cases in §5", evaluator="soundness/coverage, verification cost and relaxation tightness"),
    "2606.20512": bench(workload="Repository coding tasks under probe-and-refine guidance", evaluator="task success, localization, step budget, cross-model transfer and guidance ablations"),
    "2606.20520": bench(workload="Agent-control-plane authority and attack scenarios in §8–9", evaluator="authorized task utility, unauthorized execution, revoke/drift behavior and broker overhead"),
    "2606.20529": bench(workload="Policy-constrained tool-calling tasks in §4", evaluator="task success, policy violations, state consistency and ledger overhead"),
    "2606.20536": bench(workload="Several hundred SiT networks on ImageNet 256×256", input_length="256×256 images", evaluator="FID distributions across training and generation seeds"),
    "2606.20537": bench(workload="Low-latency small-batch on-device Physical-AI serving graphs", hardware="NVIDIA CUDA backend", evaluator="checkpoint/restore latency, throughput, memory and correctness across graph boundaries"),
    "2606.20545": bench(workload="WRBench camera-motion interventions on generated-world models", evaluator="human-calibrated camera execution, in-view continuity, off-view evolution and re-observation consistency"),
    "2606.20553": bench(workload="Federated language-model fine-tuning with privacy-backdoor attacks", evaluator="leakage/attack success, clean utility and defense behavior"),
    "2606.20562": bench(workload="World-action-model environments and persistent-memory ablations", evaluator="action/world prediction, task success, memory/latency and horizon scaling"),
    "2606.20754": bench(workload="LIBERO and LIBERO-PRO under distribution shift", evaluator="failure-detection quality for perturbation versus sampling uncertainty"),
    "2606.20758": bench(workload="Instrumented e-commerce microservices with eight injectable failure scenarios", evaluator="root-cause derivation/explanation correctness, evidence path and diagnosis behavior"),
    "2606.20785": bench(workload="Online-Mind2Web, WebVoyager and FaraGen1.5 computer-use trajectories", model="Fara1.5 Qwen3.5-based 4B/9B/27B; solver harness supports multiple frontier models", evaluator="task success plus correctness, efficiency and critical-point trajectory verifiers"),
    "2606.20814": bench(workload="Narrow fine-tuning datasets and out-of-domain alignment prompts in §2–4", evaluator="training loss, alignment scores, activation-prediction accuracy and train/eval subspace overlap"),
    "2606.20820": bench(workload="LLM evaluation pools and target-precision stopping tasks in §5", model="7–8B surrogate models; 67–72B dense and 8×7B MoE target models", evaluator="evaluated-sample count, confidence-interval width and anytime-valid coverage"),
    "2606.20839": bench(workload="Held-out peer-reviewed Galaxy workflows converted to BioWorkflow Bench and BioAgent Bench tasks", evaluator="workflow completion, biological correctness, execution efficiency and tactic/process-reward ablations"),
    "2606.20873": bench(workload="SciClaimEval development set", evaluator="macro-F1, pair accuracy and atom/witness grounding diagnostics"),
    "2606.20898": bench(workload="972 manufacturing-safety answers across three machines and three grounding approaches", model="Two small language models", evaluator="expert-validated correctness and per-query input-token cost"),
    "2606.20910": bench(workload="Live instrumented-domain traffic from six agent frameworks, humans and legacy crawlers", model="Decision-tree classifier over TLS/HTTP/browser-action features", evaluator="agent-framework attribution accuracy and class separation"),
    "2606.20922": bench(workload="AgentDojo and ASB cross-tool description-poisoning tasks", evaluator="attack success, benign task utility and defense overhead"),
    "2606.20954": bench(workload="Long-running agent tasks and LoCoMo conversational-memory evaluation under matched budgets", hardware="CPU-only LRE scorer", evaluator="task/answer accuracy, context tokens, compressor calls and action-call count"),
    "2606.20969": bench(workload="604 C programs from multiple datasets", model="GPT-o4 Mini, GPT-5.2, Grok-4.1 and Gemini-3", evaluator="specification-generation success and Frama-C/WP full-proof ratio"),
    "2606.20978": bench(workload="85 web-automation tasks: 43 vague and 42 precise descriptions", evaluator="pass rate, paired permutation test and format ablations"),
    "2606.21005": bench(workload="Multimodal scientific-paper curation tasks with gold curated records", evaluator="Gold-Referenced Attribute Score, attribute-level errors and harness-component ablations"),
}


ARTIFACTS = {
    "2606.19758": "https://anonymous.4open.science/r/SIGMA-2338/ — code artifact disclosed by arXiv:2606.19758v1",
    "2606.19887": "https://github.com/selectstar-ai/FinRED-paper; https://huggingface.co/datasets/datumo/FinRED — code and dataset artifacts disclosed by arXiv:2606.19887v1",
    "2606.20002": "https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod — implementation disclosed by arXiv:2606.20002v1",
    "2606.20922": "https://github.com/shishishi123/Tool-Guard — code artifact disclosed by arXiv:2606.20922v1",
}
