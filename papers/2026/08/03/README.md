# Daily Research — 2026-08-03

**规范：** V3
**窗口：** 2026-08-02T09:00:00+08:00 ～ 2026-08-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:30:00+08:00

## 1. 结论

本窗的 arXiv Monday 公告包含 430 个跨分类身份；它们只是发现索引，不是 430 个候选。独立复核重新逐题摘检查后，候选分母由 10 项纠正为 18 项：原筛选漏掉了 8 项明确改变大模型推理数据移动、Kernel locality、KV 生命周期、Agent 评测或 Diffusion cache control 的材料。其余条目主要是传统任务应用、局部指标优化、综述或 AI for Science，没有因能映射 ROADMAP 就进入候选。

18 项均取得当前可访问的 v1 原始正文（Memory Provenance 使用官方 PDF，其余使用 arXiv HTML），没有发现 withdrawal 标记；深入审阅完成。8 项长期机制已在 Books 存在，10 项完成正文整合；报告经写后语义复核闭环。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 按本窗与相邻发布日期检查，无符合当前范围的新机制正文 | 已检查 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 相邻公开记录为 Jul28 与 Aug10 | 已检查 | 无 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/) 相邻记录为 Jul28 与 Aug05 | 已检查 | 无 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 检查本窗首次公开条目；WaiT 的频率感知 flow-matching 属局部生成方法，题摘未改变本项目生成范式判断，初筛关闭 | 已检查 | 无 |
| SRC-QWEN | [Qwen](https://qwenlm.github.io/) 逐项检查日期，本窗无相关正文 | 已检查 | 无 |
| SRC-DEEPSEEK | [Research](https://www.deepseek.com/) 与公开更新按日期检查，本窗无新机制正文 | 已检查 | 无 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 与 [GitHub](https://github.com/MoonshotAI) 按发布时间检查，本窗无相关研究事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | [Research“全部”列表](https://hunyuan.tencent.com/research) 中 Jul21 后下一条为 Aug11 | 已检查 | 无 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 中 Jun16 后下一条为 Aug14 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research) 与论文目录按日期检查，本窗无条目 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) 按日期检查，最近记录早于本窗 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) 论文与博客按日期检查，本窗无条目 | 已检查 | 无 |
| SRC-MINIMAX | [Research / Blog](https://www.minimax.io/blog) 中 H3 为 Jul31 08:00 北京时间，明确窗外 | 已检查 | 无 |
| SRC-ARXIV | Monday 08:00 北京时间官方公告；430 个跨分类身份去重后完成题摘语义筛选，独立复核纠正漏项后 18 项通过贡献门槛；保留项均重新打开当前 v1 原文 | 已检查 | 无 |

本窗没有需要加载按需来源的具体触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Topology-Aware Data Movement](https://arxiv.org/html/2607.28633v1) | 2026-08-03T08:00:00+08:00 | 将 PD 架构中的 KV transfer 从统一 RDMA 改为 topology-aware transport、layer pipeline 与 placement 联合计划；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Safety, or Just Capability?](https://arxiv.org/html/2607.28685v1) | 2026-08-03T08:00:00+08:00 | 证明 Agent safety 分数必须绑定 metric、target behavior 与 model panel，不能把 capability proxy 当安全结论；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Model or Harness?](https://arxiv.org/html/2607.28802v1) | 2026-08-03T08:00:00+08:00 | 把 Agent failure 从 outcome label 推进为 model、harness、tool、environment 与 grader 的 repair assignment；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LLM Kernel Access on NUMA GPUs](https://arxiv.org/html/2607.28824v1) | 2026-08-03T08:00:00+08:00 | 按 global/partial/private operand sharing 区分多 partition GPU 的 pinning 与 co-scheduling，改变 Kernel placement contract；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Validation Evidence in LLM Repair Agents](https://arxiv.org/html/2607.28871v1) | 2026-08-03T08:00:00+08:00 | 用 buggy/candidate/gold 三状态重放区分 pass 与 bug-discriminating evidence，修正 Agent 以绿灯自证修复的做法；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Selective KV Cache Protection](https://arxiv.org/html/2607.29076v1) | 2026-08-03T08:00:00+08:00 | 将 analog-CIM 动态 KV 的噪声风险按 sink/recent/bulk token 分层，并保留数字高精度路径；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [OnlineCache](https://arxiv.org/html/2607.29398v1) | 2026-08-03T08:00:00+08:00 | 将 Diffusion feature cache 由静态 schedule 改为 sample/timestep 条件策略并显式修正缓存误差；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ResKV](https://arxiv.org/html/2607.29591v1) | 2026-08-03T08:00:00+08:00 | 将 eviction 丢失的 attention numerator/denominator mass 保存在 residual cache，并与 exact main cache 联合归一化；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [WitCert](https://arxiv.org/html/2607.28699v1) | 2026-08-03T08:00:00+08:00 | 把 KV 量化从离线平均分推进为请求级 sound risk meter 与 fail-open/fallback 决策；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DeltaServe](https://arxiv.org/html/2607.28848v1) | 2026-08-03T08:00:00+08:00 | 把推理空闲算力转成受 SLO 约束的 LoRA 训练配额，改变训练与服务共置的准入边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Hollow-LLM Attack](https://arxiv.org/html/2607.28884v1) | 2026-08-03T08:00:00+08:00 | 证明 ZK 等式正确性不自动绑定实际计算投入，纠正“架构与权重承诺等于执行真实性”的安全判断；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Aries](https://arxiv.org/html/2607.29069v1) | 2026-08-03T08:00:00+08:00 | 将 Agent serving 的观测单位从 token/request 改成跨模型、harness、tool 与 sandbox 的 trajectory；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MONITORING [Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Faster but Different](https://arxiv.org/html/2607.29079v1) | 2026-08-03T08:00:00+08:00 | 以干预实验把多模态 diffusion 加速的内容漂移定位到 stale visual/text state，并给出 refresh-speed-agreement 边界；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Reproducing LightMem](https://arxiv.org/html/2607.29104v1) | 2026-08-03T08:00:00+08:00 | 受控复现显示 memory construction 的收益可能由 retriever 选择主导，并在宽 token budget 下丢失原始证据；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Memory Provenance Laundering](https://arxiv.org/pdf/2607.29167v1) | 2026-08-03T08:00:00+08:00 | 揭示 memory consolidation 会洗掉低信任来源但保留 action trigger，并提出 authority non-amplification；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [ActFovea](https://arxiv.org/html/2607.29169v1) | 2026-08-03T08:00:00+08:00 | 用 action-conditioned visual corridor 与 freshness consistency 检测 VLA 闭环扰动，补足动作级 detector 的盲区；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [SLIM](https://arxiv.org/html/2607.29575v1) | 2026-08-03T08:00:00+08:00 | 用硬件 profiling 将 batch 饱和定位到 decode attention 的 DRAM 带宽，而非笼统的“大 batch 更快”；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [TokTier](https://arxiv.org/html/2607.29678v1) | 2026-08-03T08:00:00+08:00 | 为增量 tokenization 建立与全量 tokenizer 完全一致的 splice-check-fallback 合同，并区分 session 与 KV 生命周期；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md) |

## 4. 证据与知识整合

### [Topology-Aware Data Movement](https://arxiv.org/html/2607.28633v1)

v1 的 System Architecture 将 prefill→transfer→decode 建成显式异步生命周期，并按 NVLink/NVSwitch、PCIe、RDMA、TCP 择路；analytical model 与 component implementation 支持该设计方向，但作者明确没有可用于完整验证的异构多机+CXL testbed。Books 因而只吸收“KV transfer plan 必须绑定 topology epoch、placement、retry 与 completion”，不采用 3～18× projected headline 作为生产结论；统一 RDMA 在拓扑同构或转移不在 critical path 时继续成立。

### [Safety, or Just Capability?](https://arxiv.org/html/2607.28685v1)

论文在官方实现和作者 scorer 下比较四个 Agent-safety benchmark，并展示小 model panel、类别不平衡及 target behavior 差异会改变相关性；这证明的是 measurement validity，而不是某个模型“总体安全”。Ch66 已要求 score 绑定 dataset slice、metric、evaluator、model population 与 intended claim，且 capability 不能代理 safety，无需重复新增。

### [Model or Harness?](https://arxiv.org/html/2607.28802v1)

方法把 41 类 failure 放在 model、harness、user、tool、memory、environment 之间的 interaction edge，并用 fault side 指向 repair owner；跨四个 judge 的一致性只支持 taxonomy 可复现，不保证对所有开放轨迹因果正确。Ch66 已把 `model × benchmark × harness × environment × scorer` 作为评测身份，并要求保存 trajectory 后定位 model/harness/tool/grader failure，现有正文已承载该增量。

### [LLM Kernel Access on NUMA GPUs](https://arxiv.org/html/2607.28824v1)

论文先以 memory trace 提取 workgroup-level sharing，再在 cycle-level simulator 中区分 global、partial 与 private operands；不同 sharing class 对应 replication、subgroup co-scheduling 或 per-workgroup pinning。证据是 characterization 与 simulation，不是现成硬件上的通用加速。Ch49 吸收 operand-sharing class 进入 execution-plan identity，并保留单 partition 或 locality 不敏感时的普通 kernel fallback。

### [Validation Evidence in LLM Repair Agents](https://arxiv.org/html/2607.28871v1)

BSG-VA 在 exact working-tree state 捕获 validation command，并分别在 buggy、candidate 与 gold-fix state 重放，由反事实差异判定 positive event 是否真的区分目标 bug。643 个 rollout 的结果支持“pass 不是天然 bug evidence”；反馈实验的增益低于作者预设 practical-effect threshold，且 scaffold/model replication 不一致。Ch66 因而吸收的是 baseline replay 与 evidence-role contract，不把其百分比外推为所有 repair Agent 的失效率。

### [Selective KV Cache Protection](https://arxiv.org/html/2607.29076v1)

v1 将静态 projection weights 与动态 KV 写入分开，按 attention sink、recent window 与 bulk cache 的噪声敏感性选择 digital/analog 路径；模型结果来自 measured-noise-calibrated simulation，而非完整 LLM 在 fabricated chip 上端到端运行。Ch45 已有 sink/recent 高精度窗口、mixed precision、硬件/布局共同身份和 FullKV fallback，现有覆盖充分。

### [OnlineCache](https://arxiv.org/html/2607.29398v1)

方法把每个 sample、每个 denoising timestep 的 cache/recompute 选择建成 sequential policy，并可与 error corrector 双层优化。作者在 FLUX.1-dev、DiT 与 CogVideoX 上的结果只支持其训练和质量指标。Ch24 吸收“cache schedule 是轨迹状态控制、refresh 与 correction 是两种不同成本”，并要求未通过 freshness/agreement gate 时回退全量重算。

### [ResKV](https://arxiv.org/html/2607.29591v1)

ResKV 将固定预算拆成 exact main 与 approximate residual，residual entry 以 population count 恢复 softmax denominator，并用 query-dependent gate 调节贡献；LongBench/RULER 与单 A100 条件不能证明 production SLO。Ch45 已以完整演进链说明 hard eviction、merge、exact-main/approximate-residual 与 FullKV 共存，无需再写。

### [WitCert](https://arxiv.org/html/2607.28699v1)

v1 的 §3 先给出看似合理但不 sound 的 certificate，再由 §4 建立 deterministic witness bound 与受显式 request-level failure budget 约束的 probabilistic tier；§5 只在作者给定 quantizer、模型与工作负载上验证开销和修复效果。它支持“近似状态应带运行时风险预算与 fallback”，不证明 bound tight、最终语义正确或任意量化器都能获得同等性能。Ch45 已完整承载这个判断，无需重复写回。

### [DeltaServe](https://arxiv.org/html/2607.28848v1)

§3 的 host hook、multi-LoRA batching 与 SLO-aware admission 把 fine-tuning forward 视作可利用的服务 headroom；CUDA-graph-aware latency model 离线校准并在线更新，backward 仍被隔离。生产 trace 与三种 host 集成支持该分支可行，但不证明跨硬件、任意训练负载或预测误差下仍守住 SLO。Ch56 已保留“预测不确定时停止训练并回退纯推理”的边界。

### [Hollow-LLM Attack](https://arxiv.org/html/2607.28884v1)

§III 明确 threat model：攻击者保持公开 architecture/parameter shape，却以代数结构化 ghost weights 降低有效工作；后续电路验证只证明承诺方程成立。该结果否定的是“equational correctness 自动证明 advertised effort”，不是否定 ZK 对输入、权重与算术关系的保证。Ch72 已区分 correctness、model identity 与 work binding。

### [Aries](https://arxiv.org/html/2607.29069v1)

§3 把 task semantics 与 execution configuration 分离，并以 correlated telemetry 重建跨模型、tool 与 sandbox 的 trajectory；§4 的开源实验和商业 trace 显示 token 指标会漏掉 tool/harness bottleneck，sandbox 又呈 burst-idle 负载。证据不证明所测 harness 代表所有 Agent。拟在 Ch67 “从 request trace 到 Agent trajectory”段之后加入：trajectory ID 应贯穿 model call、tool effect、sandbox lease 与环境观测，且容量规划不能用 token throughput 替代工具等待与 burst resource。

### [Faster but Different](https://arxiv.org/html/2607.29079v1)

§5～§7 的 threshold、state-refresh 与 image-swap 干预把漂移收窄为 stale visual/generated-text state 的贡献；更短 refresh interval 在被测实现上形成 speed-agreement frontier。它没有证明加速输出的语义等价，也不能外推到 causal AR。拟在 Ch24 cache acceleration 分支中补入：并行/缓存加速除了 acceptance 或质量分数，还要显式审计 state freshness 与同模型未加速输出的一致性；refresh 是代价明确的 correctness knob。

### [Reproducing LightMem](https://arxiv.org/html/2607.29104v1)

§3 重建 LightMem，§4～§5 交叉比较 constructed memory 与 raw-turn RAG 以及不同 retriever。结果只支持指定对话数据、budget 与 retriever 下“构造摘要未必优于保留原始 turn”，不证明所有 memory abstraction 无用。拟在 Ch77 retrieval-memory 演进段加入：先冻结 retriever 与 token budget，再归因 memory construction；预算宽时保留 provenance-linked raw evidence，预算紧时才用压缩表示换 token 成本。

### [Memory Provenance Laundering](https://arxiv.org/pdf/2607.29167v1)

v1 PDF 的 threat model、PPMF schema、consolidation/evaluation 与 limitations 说明：由模型改写的 memory 不能拥有高于源 observation 的 action authority；platform-maintained provenance 不能交给同一生成模型自报。作者固定 risk policy 下的结果支持 non-amplification firewall，但不证明内容真假或覆盖未知攻击。拟在 Ch77 “derived memory”之后加入 authority lattice、source-preserving rewrite 与 tool authorization 的 handoff，并短链 Ch72。

### [ActFovea](https://arxiv.org/html/2607.29169v1)

方法以 kinematics、proprioception 和近期 action 构建 action-conditioned foveated regions，再检查 motion/freshness consistency；恢复候选只有经一致性验证才可提交。仿真和实机实验支持该 monitor 发现部分闭环错位，不证明任意扰动或 safety invariant。拟在 Ch26 runtime monitor 段补入“检测器也必须读取 control state；只看 action output 会漏掉 stale observation”，最终 veto 仍归 controller/safety envelope。

### [SLIM](https://arxiv.org/html/2607.29575v1)

GPU profiler 将饱和归因到 decode attention 在 active-context 增长时近恒定 arithmetic intensity 导致的 DRAM bandwidth pressure；轻量模型据此定位收益平台。证据限作者硬件与被测模型，不提供普遍 batch optimum。**已整合：** Ch56 将 admission 与 capacity planning 绑定 active KV length、bandwidth headroom 和校准域；一旦边际 throughput 进入平台，应停止扩 batch，把 latency/HBM 作为成本。

### [TokTier](https://arxiv.org/html/2607.29678v1)

§2 的 trace 划分出“小 append + 巨大既有 transcript”和少量 rebuild；§3 只有在 stable pre-tokenization boundary 检查通过时 splice，否则扩大窗口或 full fallback，并用 differential testing 守住 exact token IDs。其性能数字受 fleet trace、tokenizer 与 GPU 配置约束。Ch11 已写入 exactness contract，推理侧只需 handoff，不再复制机制。

## 5. 缺口与下一步

无

本窗没有可执行未决或用户材料请求。18 项候选均已完成证据判断与 Books 决定。

## 6. 复核

复核者：独立复核智能体（2026-09-07）
结论：通过

复核纠正 8 项 false negative。以 430 个 official-announcement identity 为分母，逐题摘重筛并对新增 8 项重开 exact-v1；withdrawal、Source Family、评分深度、证据边界与 owner 均已检查。新增 4 项 Books 机制位于 canonical owner 的正文区，另 4 项确有既有覆盖；旧日报候选池及旧处置未被继承。
