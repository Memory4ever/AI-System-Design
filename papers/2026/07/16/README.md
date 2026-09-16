# Daily Research — 2026-07-16

**规范：** V3
**窗口：** 2026-07-15T09:00:00+08:00 ～ 2026-07-16T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T18:00:00+08:00

## 1. 结论

本窗旧报告从 446 个 arXiv 去重身份保留 62 项；按当前长期贡献门槛重新逐项题摘复筛并经独立 false-negative 复核后，18 项进入候选分母，44 项转为有具体理由的分母前关闭。被关闭材料包括量子纠错里的“speculative decoder”同名碰撞、AI for Science/电网/临床应用、局部 VLA/Agent benchmark、模型版本事实与单点硬件优化；入选 exact v1 未见 withdrawn。

本日最重要的共同结论是：系统优化与可信执行都取决于“谁拥有可提交状态”。数据 provenance、复合模型 serving、edge/cloud KV、pruning recovery、KV eviction、去中心化训练、RL compute/credit、Agent compaction/memory/orchestration、异构执行 attestation、canonical action 与 continual evaluation 分别把状态的来源、迁移、恢复和验证显式化。4 项沿用既有正文，14 项新增机制已经写入对应 owner，并完成非作者逐项语义复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ANTHROPIC | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-GOOGLE-AI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-META-AI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-QWEN | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-DEEPSEEK | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-MOONSHOT | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ZAI | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-MINIMAX | 历史生效边界晚于本窗 | 不适用 | 无 |
| SRC-ARXIV | 官方新公告；446 个去重身份完成标题巡检与含糊/高信号完整摘要筛选，独立复核后 18 项入选 | 已检查 | 无 |

明确关闭 2607.13062（量子纠错术语碰撞）、2607.13220/13221/13651（AI for Science/领域系统）、多项局部 VLA 与 Agent benchmark、CIMERA/ExTernD 单点硬件或量化变体；这些不支撑本书通用机制更新。MiMo 的材料不是单纯版本事实：其正文披露了 Hybrid SWA、MoE 与多模态复合架构的 KV、缓存、调度和 preprocessing 全链路设计，已恢复为候选。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [OriginBlame](https://arxiv.org/html/2607.13037v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 为训练数据建立 record/token 级 provenance 与派生链；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [The Economics of AI Decoding Chips](https://arxiv.org/html/2607.13068v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 用 compute、capacity 与 bandwidth 三个比率解释 decode accelerator 取舍；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Compaction as Epistemic Failure](https://arxiv.org/html/2607.13071v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 揭示被 kill 的进程输出经 compaction 后被错误持久化为成功事实；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Efficient and Privacy Aware Edge Cloud Collaborative Inference](https://arxiv.org/html/2607.13093v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 把 authenticated KV/state transfer 纳入 edge/cloud split；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-DYNAMO，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [Full-Pipeline Inference Optimization for MiMo-V2.5 Series](https://arxiv.org/html/2607.13095v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 将 Hybrid SWA 的逻辑状态语义落实到 dual-pool KV、分层预取、distributed cache 与 affinity routing；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ShortOPD](https://arxiv.org/html/2607.13124v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 用 short-to-long on-policy distillation 恢复 pruning 后的 free-form 能力；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Adaptive Filtering of the KV Cache](https://arxiv.org/html/2607.13205v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 诊断并纠正 eviction 对结构角色的系统性偏置；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Agora](https://arxiv.org/html/2607.13332v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 将异构互联网节点的训练贡献、验证和聚合显式化；2 + 3 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/html/2607.13359v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 区分总成本与关键路径延迟，以 accuracy floor、critical-path credit 和在线 controller 优化 execution graph；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Where Should RL Post-Training Compute Go?](https://arxiv.org/html/2607.13389v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 分解 model size、search、learning 与 feedback 的 compute allocation；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Demystifying On-Policy Distillation](https://arxiv.org/html/2607.13399v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 区分 OPD 的 exploration catalyst、distribution repair 与 pathologies；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Memory as a Controlled Process](https://arxiv.org/html/2607.13591v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 将记忆写入、保留、读取和删除建模为受观测反馈控制的过程；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [WarpGuard](https://arxiv.org/html/2607.13640v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 联合证明 CPU control flow、GPU control flow 与 kernel launch binding；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [CAVA](https://arxiv.org/html/2607.13716v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 将异构 runtime action 规范化为可绑定 policy、approval、receipt 与 attestation 的稳定对象；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Post-Training Shifts Confidence](https://arxiv.org/html/2607.13753v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 将 SFT、RL、OPD 后的 CoT confidence calibration 分阶段评估；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Generative Compilation](https://arxiv.org/pdf/2607.13921v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 在代码生成过程中用 compiler feedback 封存已验证的部分程序；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [TRACE](https://arxiv.org/html/2607.13988v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 在 tool-call boundary 定义状态，以 frozen reference 对 gold-answer 可预测性的 TD 变化分配 turn credit；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Do Agent Optimizers Compound?](https://arxiv.org/html/2607.14004v1) | 2026-07-16T08:00:00+08:00 ～ 2026-07-16T09:00:00+08:00 | 把一次性 optimizer 评测改为跨 phase 的 transfer、migration 与 regression contract；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [OriginBlame](https://arxiv.org/html/2607.13037v1)
exact v1 把 provenance 作为写入时状态，而不是事后猜测：`.ob/` 中的 JSONL 记录 author、section 与 document/index 三层对象，并通过哈希和单跳映射把最终 record/token 追溯到原始贡献；撤回请求由确定性 blame query 生成 forget set。[Method §4](https://arxiv.org/html/2607.13037v1#S4) 与 [Architecture §4.1](https://arxiv.org/html/2607.13037v1#S4.SS1) 因而支持 Ch27 中“dataset identity 必须延伸到派生记录与 token”的机制，而不是只增加一个来源标签。

- **Evaluation：** [§5](https://arxiv.org/html/2607.13037v1#S5) 在 219,555 个中文 Wikipedia 页面、482,543 位作者以及 1K～220K 页面规模上验证撤回集合与接入成本；record 级追踪把相对 dataset-level 删除的 over-deletion 从最高 101× 降到 1.3×，HuggingFace 与 Datatrove 管线吞吐开销分别为 1.3%～4.0% 和 2.1%～19.0%。这些是该语料与实现的功能/吞吐结果，不是任意数据湖的成本上界。
- **Limitations：** [§6](https://arxiv.org/html/2607.13037v1#S6) 明确说明不能为既有数据集追溯补录、公开 parser 仅覆盖 MediaWiki、只追踪单跳派生，而且数据变化后必须重建索引；contributor identity 还会形成需要访问控制的个人信息。
- **取舍与回退：** 精确删除换来写入时 instrumentation、索引重建、额外存储与身份治理。无法改造旧管线或索引已过期时，系统不得声称 record/token 级可撤回，应退回保守的全量扫描/整批移除，并在重建 lineage 后才恢复精确删除。

### [The Economics of AI Decoding Chips](https://arxiv.org/html/2607.13068v1)
[§1](https://arxiv.org/html/2607.13068v1#S1)、[§2](https://arxiv.org/html/2607.13068v1#S2) 与 [§5](https://arxiv.org/html/2607.13068v1#S5) 用 `F/B`（算力/带宽）和 `F/S`（算力/容量）构造 decode 的资源经济模型：单用户 decode 往往先受权重与 KV 的容量/带宽约束，因此“少买计算、多买普通 DRAM、容许较低带宽”是一个特定工作负载分支，而不是通用加速器结论。

- **Evaluation：** 证据来自器件规格、价格和解析模型；HTX-301 的设计/价格是论文中的产品主张，而不是在统一模型、长度、并发和 SLO 下完成的生产对照实验。它可以说明被峰值 FLOPS 隐藏的供给与容量成本，不能证明该芯片在所有 serving 场景更优。
- **Limitations：** [§8](https://arxiv.org/html/2607.13068v1#S8) 及前文比较显示，低 `F/B`、高容量设备会牺牲 prefill 和高并发吞吐；SRAM 路径以容量换延迟，消费级内存设备接近但未达到论文所需的容量角点。
- **取舍与回退：** 专用 decode 硬件降低闲置算力与 HBM 供应成本，却把系统推向更慢内存和更窄 workload envelope。prefill 占比高、批量大、训练复用或吞吐优先时仍使用 HBM GPU/TPU；混合负载可拆分 prefill/decode，仅把受容量成本主导的 decode 放到该分支。

### [Compaction as Epistemic Failure](https://arxiv.org/html/2607.13071v1)
[Observed Failure §3](https://arxiv.org/html/2607.13071v1#S3)、[Experimental Context §3.1](https://arxiv.org/html/2607.13071v1#S3.SS1) 与 [Mechanism §4](https://arxiv.org/html/2607.13071v1#S4) 记录了一个明确的状态提升错误：退出码 143 的进程只留下 partial stdout，compaction 却把它改写为“已确认结果”，后续会话再把摘要当作事实而不复核。Ch75 因而需要把 command identity、stdout、exit status 与确认状态作为不同字段保存。

- **Evaluation：** 论文采用单一重度用户工作流的参与式观察，证明这种 failure mode 在所述 Claude Code 流程中真实存在并能跨会话传播；它没有测量不同 Agent、用户或版本中的发生率，也不能给出 compaction 导致错误的总体因果比例。
- **Limitations：** [§7](https://arxiv.org/html/2607.13071v1#S7) 将生态真实性与可推广性分开：案例受单个用户的任务和操作方式影响，缺少受控、多系统的复现实验。
- **取舍与回退：** compaction 节省上下文，却可能丢掉证据状态与 provenance。摘要只能保留“观察到 partial output / 进程未确认”，不能升级为成功；原始输出或退出码不可得时，必须重跑验证命令，无法重跑则把结论降为 unknown。

### [Efficient and Privacy Aware Edge Cloud Collaborative Inference](https://arxiv.org/html/2607.13093v1)
[Method §5](https://arxiv.org/html/2607.13093v1#S5) 将本地 embedding/projection/draft 与云端 decoder 分开，并把量化张量和 KV 状态封装为带 cache authorization 的 AES-GCM 传输对象。这里的关键不是“split inference”本身，而是 endpoint、cache identity 与可提交 token 状态共同决定云端能否复用历史。

- **Evaluation：** [§7](https://arxiv.org/html/2607.13093v1#S7) 的 PyTorch/QUIC/8-bit/AES-GCM 原型使用作者定义的 7B-class target、512-token 输入与 128-token 输出等条件，报告相对基线最高 46.1% per-token latency 降幅和 67.4% downlink 降幅，并在该设置下保持接近 full-cloud 的生成质量；未披露条件不能补作生产 SLO。
- **Limitations：** [Security §8](https://arxiv.org/html/2607.13093v1#S8) 的 threat model 只保护传输，获授权的云端仍可读取解密后的表示，且没有 differential privacy 或 secure computation 保证，hidden representation 也可能泄漏输入信息。
- **取舍与回退：** 状态复用节省链路与重复计算，却增加 key、cache authorization、重放防护和恢复逻辑。[§6.3](https://arxiv.org/html/2607.13093v1#S6.SS3) 给出可执行回退：认证失败改为 cache-free decoding，块丢失/校验失败重传，speculation 失败则从最后接受 token 重算并修正 cache；更强隐私要求需退到 local-only、TEE/MPC 或 DP 路线。

### [Full-Pipeline Inference Optimization for MiMo-V2.5 Series](https://arxiv.org/html/2607.13095v1)
[KV refactor §3](https://arxiv.org/html/2607.13095v1#S3) 以 Full/SWA 双池承载不同生命周期：Full index 是权威索引，SWA block 通过映射与双重容量检查保持 window-safe prefix 语义，再用 layer-wise prefetch、GCache 与跨层级传输连接执行路径。理论上的 SWA 低 KV 占用只有在这些状态身份一致时才能成为 serving 收益。

- **Evaluation：** [§7](https://arxiv.org/html/2607.13095v1#S7) 绑定 MiMo-V2.5、SGLang 0.5.5 与作者披露集群；其中路由器的 prefix affinity 使 L2 hit rate 提升 25%、input throughput 提升 30%，长请求 TTFT P90 降低 30.5%。多模态侧的 encoder 由约 15 提升到 30 QPS、P90 由 100.76 ms 降到 82.94 ms，video decode 由 156 s 降到 23 s；这些都不是跨模型常数。
- **Limitations：** [§3.3](https://arxiv.org/html/2607.13095v1#S3.SS3) 指出 cache hit 受请求前缀重复度约束；dual-pool 映射只适用于相应 Hybrid SWA 语义，affinity routing 还可能制造 load skew，未披露的模型、并发和网络条件不能外推。
- **取舍与回退：** 双池、分层 cache 和亲和调度减少 KV 占用/迁移，却增加索引一致性、容量核算与 starvation 风险。映射无效或架构不兼容时退回 full-KV 路径；亲和性造成倾斜时以 uncached-token 优先级和等待时间惩罚切回负载优先调度。

### [ShortOPD](https://arxiv.org/html/2607.13124v1)
[Method §3](https://arxiv.org/html/2607.13124v1#S3) 从 Block-Influence 深度剪枝后的 Qwen3-4B 出发，冻结原模型作 teacher，以 student on-policy rollout 的 generalized JSD（top-100 加 tail）恢复分布；[§3.3](https://arxiv.org/html/2607.13124v1#S3.SS3) 用 repetition gate 在短 rollout 无效时才扩到长预算，而不是始终支付完整序列成本。

- **Evaluation：** [§4](https://arxiv.org/html/2607.13124v1#S4) 与 [Evaluation details](https://arxiv.org/html/2607.13124v1#S10) 使用 45,447 个 math/code/open prompts、一轮训练和 8 张 H20，对比 SFT、sequence KD、KD、OPD 与 ShortOPD；表中恢复收益和约 1.3× 训练速度只适用于该模型、约 25% depth pruning 与预算设置。
- **Limitations：** [§6](https://arxiv.org/html/2607.13124v1#S6) 明确只验证 BI、固定约 25% 剪枝与 Qwen3-4B family，未覆盖其他剪枝方法、比例和更大模型，也没有确定“损伤过大后轻量恢复必然失效”的边界。
- **取舍与回退：** 自适应长度减少重复 suffix 计算，却引入 repetition detector、EMA/controller 与冻结 teacher 成本。检测器不稳定时退回固定 short/long OPD；student–teacher gap 过大时先用 SFT/KD warm-up，无法恢复则降低剪枝率而非延长 rollout 硬救。

### [Adaptive Filtering of the KV Cache](https://arxiv.org/html/2607.13205v1)
[Method §4](https://arxiv.org/html/2607.13205v1#S4) 先做 counterfactual role eviction，随后以 SnapKV 的 windowed attention mass/max-pooling 为基线，加入 role-conditioned allocator 和 `alpha_KEY` 保底；因此它改变的是预算分配，而不是 KV 内容语义。

- **Evaluation：** [§4](https://arxiv.org/html/2607.13205v1#S4) 到 [§6](https://arxiv.org/html/2607.13205v1#S6) 在 synthetic schema QA 与 Llama/Mistral/Phi/Qwen 上测量角色丢失；约 15 MB 的线性 probe 可达近 0.995 F1，但 QA exact match 仍会损失 18～32 个百分点，且 over-baseline 收益对 seed 敏感。
- **Limitations：** [§7](https://arxiv.org/html/2607.13205v1#S7) 说明实验只用 attention mask 模拟 eviction，没有真的收缩 KV tensor，因此未证明 memory、latency 或 throughput 收益；role-density floor、真实语料、4-bit cache 与 parser 误差仍未闭合。
- **取舍与回退：** key 配额减轻结构角色被清空的风险，却牺牲 value budget 并依赖可靠的 role parser。角色密度低或 parser 不可用时退回 SnapKV/H2O 等非角色策略；merged-token 场景至少保留小的 `alpha_KEY`，不得把 key 配额降为零。

### [Agora](https://arxiv.org/html/2607.13332v1)
[Protocol §3](https://arxiv.org/html/2607.13332v1#S3) 把 worker、trainer 与 authorizer 分开：pipeline stage shard 可复制，worker 通过 surrogate test 获得贡献资格，参数以异步稀疏方式聚合；join/leave、checkpoint 与 rollback 共同维持 model-state authority，而不是默认所有互联网节点可信。

- **Evaluation：** [§5](https://arxiv.org/html/2607.13332v1#S5) 的 Pluralis-8B 实验在约 40 天内处理 500B FineWeb-Edu tokens，节点跨三洲且 GPU/网络异构；运行约达 170K token/s、4.2 token/TFLOP 和集中式 H100 baseline 的 63% efficiency。它证明协议可支撑该次运行，不等同于开放对抗网络的一般鲁棒性。
- **Limitations：** [§6.4](https://arxiv.org/html/2607.13332v1#S6.SS4) 的 all-reduce failure 及结果把网络延迟、GPU 类型和参与者行为混在同一系统中；200 Mbps 以上带宽不再成为主要瓶颈只是该配置观察，也未覆盖恶意 authorizer/worker 的完整攻击面。
- **取舍与回退：** 开放贡献扩大可用算力，却增加验证、异步陈旧、stage 不均衡与回滚成本。贡献不可验证或 churn 超出 checkpoint 恢复能力时，收缩为托管/授权 worker；稳定性优先时退回集中式训练，并从最后通过验证的 checkpoint 恢复。

### [Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/html/2607.13359v1)
[Method §3](https://arxiv.org/html/2607.13359v1#S3) 将 query execution 表示为 DAG；总 token/API cost 与 wall-clock critical path 是两个不同目标。第一阶段选择 orchestrator，第二阶段由 frozen traces 训练 controller，在 accuracy floor 的拉格朗日约束下裁去对未来结果冗余的 interaction。

- **Evaluation：** [§4](https://arxiv.org/html/2607.13359v1#S4) 只覆盖 HumanEval、GSM8K、MATH 与 MMLU-Pro 及固定 provider/configuration；原生 LAMaS 报告超过 50% 的延迟下降，叠加到其他架构时为约 27%～39%，准确率仅在这些实验中维持。
- **Limitations：** API wall time 含供应商波动，四类 benchmark 未覆盖安全、hallucination 与生产 tail latency；[Appendix E](https://arxiv.org/html/2607.13359v1#A5) 的泛化实验也不能替代新 DAG/模型上的 accuracy-floor 校准。
- **取舍与回退：** 在线裁边降低关键路径，却增加 latency estimator、controller drift 与错误删除必要 interaction 的风险。准确率下界或延迟模型未校准时，禁用在线 elimination，退回经过验证的 fixed DAG/orchestrator。

### [Where Should RL Post-Training Compute Go?](https://arxiv.org/html/2607.13389v1)
[Method §3](https://arxiv.org/html/2607.13389v1#S3) 将总预算拆成 search、learning 与 reward/feedback，并用更新占比 `rho` 表示 rollout 与梯度更新的分配；RACE 先跑小规模 IsoFLOP pilot grid，再拟合条件分配面，拟合不稳或最优点落在边界时直接保留 pilot-best，而非输出伪精确比例。

- **Evaluation：** [§4](https://arxiv.org/html/2607.13389v1#S4) 与 [§5](https://arxiv.org/html/2607.13389v1#S5) 使用 Qwen2.5 1.5B/3B/7B、GRPO+LoRA、Polaris-53K 数学数据、`K=2`、最长 2048 completion，并在 GSM8K/MATH500 验证；论文在同 regime 的分配诊断有效，但仍有非零 regret，也没有证明跨 regime 的全局 held-out 改善。
- **Limitations：** [§7](https://arxiv.org/html/2607.13389v1#S7) 只覆盖单一模型族、数学 proxy、GRPO/LoRA 和有限 seeds；FLOP 账本还没有包含真实硬件利用率、通信或 wall-clock 成本。
- **取舍与回退：** pilot 减少大规模盲试，却增加拟合误差和额外实验成本。样本不足、拟合不稳定或 workload 已知稳定时使用 pilot-best/静态分配，并以 held-out downstream 结果决定是否采纳，而不是把 `rho` 当通用律。

### [Demystifying On-Policy Distillation](https://arxiv.org/html/2607.13399v1)
[§2](https://arxiv.org/html/2607.13399v1#S2) 将 OPD 写成 student on-policy 样本上的 reverse KL，token log-ratio 形成 advantage；当 teacher/student gap 过大时，作者比较 hard clipping 与 log-scale compression，以区分有效指导信号和极端比率造成的 pathologies。

- **Evaluation：** [§5.2](https://arxiv.org/html/2607.13399v1#S5.SS2) 在 Qwen3-1.7B 与 Nemotron-Cascade 数学数据上，以 avg@32/pass@1 检查 prompt diversity、采样数和 teacher gap；结果支持“prompt 多样性比单题重复采样更重要”，并显示强 teacher mismatch 下 hard clipping 可恢复训练，而 soft compression 仍可能保留噪声。
- **Limitations：** [Limitations](https://arxiv.org/html/2607.13399v1#Sx1) 明确调节启发式依赖 teacher/student gap，证据集中在数学推理，未验证开放文本与知识密集 QA，也没有证明更大 teacher 必然更好。
- **取舍与回退：** clipping 抑制异常 advantage，但会删掉一部分稀有有效信号；gap 小时可用较软调节，gap 大时优先 hard clipping。训练仍不稳定时退回 off-policy/SFT warm-up 或标准 KD，再重新进入 OPD。

### [Memory as a Controlled Process](https://arxiv.org/html/2607.13591v1)
[Method §3](https://arxiv.org/html/2607.13591v1#S3) 将 task state 与 memory state 合成 MDP；[§3.1](https://arxiv.org/html/2607.13591v1#S3.SS1) 的在线 UCB controller 在 retrieve/depth、plan injection、consolidate、forget/skip 之间选动作。控制器只拥有 memory-operation policy，不能把其输出等同于事实正确或治理授权。

- **Evaluation：** [§4](https://arxiv.org/html/2607.13591v1#S4) 覆盖 6 个 benchmark、3 个 runner 与 3 个 backbone，并与 9 个 baseline 比较；主结果使用固定 G-Memory backend，controller 与额外 memory operations 的 ablation 分别带来作者报告的约 5.2 和 1.5 点增益，但主要配置没有多 seed 平均。
- **Limitations：** 论文没有独立 Limitations 节；从 experimental setup 可确定离散状态、固定 inner backend、单次配置和 benchmark harness 限制，不能据此证明 learned policy 已解决 stale memory、访问控制或事实污染。
- **取舍与回退：** 自适应控制减少无效检索/token，却需要足够在线观察且可能学习到错误写删策略。冷启动、观测不足或高风险任务采用 deterministic retrieve/store schedule，必要时 `skip memory`；访问权、保留期与删除仍由外部 policy/RBAC 决定。

### [WarpGuard](https://arxiv.org/html/2607.13640v1)
[Design §5](https://arxiv.org/html/2607.13640v1#S5) 在 CPU 与 GPU control-flow trace 之外，再绑定 host dispatch、kernel identity 与 launch configuration；TCB 包含 OS、driver、CUDA、prover 与 verifier，warp trace 先写本地 GPU buffer 再周期性 flush。该机制证明的是复合执行身份，不是任意数据/side-channel 完整性。

- **Evaluation：** [§7.1](https://arxiv.org/html/2607.13640v1#S7.SS1) 与 [§7.2](https://arxiv.org/html/2607.13640v1#S7.SS2) 在 Jetson Orin、DynamoRIO/NVBit 上复现 GPU 与跨边界 control-flow 攻击；代价非常高：AI/IoT workload 的 function-level 开销约 1.9×～6.9×，basic-block 约 15.5×～120×，部分 microbenchmark 达 128×。
- **Limitations：** [Threat Model §4](https://arxiv.org/html/2607.13640v1#S4) 排除 control-flow bending、data-only、side-channel 与动态/self-modifying/JIT code；[§8](https://arxiv.org/html/2607.13640v1#S8) 还指出 trace buffer 可被攻击者访问，hashing 会丢失定位信息并降低响应性。
- **取舍与回退：** 细粒度 trace 提升覆盖但不可直接用于低延迟全量执行。默认采用 function-level，只有高风险 kernel 才启用 basic-block；不支持的 JIT/dynamic kernel 应 fail closed 或拒绝标记为已证明，也可退回 CPU-only/硬件 tracing 与外部完整性控制。

### [CAVA](https://arxiv.org/html/2607.13716v1)
[Method §4](https://arxiv.org/html/2607.13716v1#S4) 把 raw runtime event 依次 capture、normalize、interpret、fingerprint、bind、close 与 attest，形成 canonical action object；policy、approval 和 receipt 因而绑定 action meaning 与上下文，而不是易变的显示字符串。attestation 只证明该 action/receipt 的完整性和绑定关系，不证明动作本身明智。

- **Evaluation：** [§6](https://arxiv.org/html/2607.13716v1#S6) 使用 96 个 scenario 扩展出的 384 个 shell/MCP/browser/managed-agent 变体，并与 raw-string/first-token 等基线比较；作者 adapter/schema 下的 1.0 指标证明 canonicalization 的可行性，不代表所有 runtime parser 或企业 action distribution 已覆盖。
- **Limitations：** [§11](https://arxiv.org/html/2607.13716v1#S11) 说明 benchmark 只具代表性而非生产分布，parser pack/部分实现未公开，observe-only runtime 不能阻断动作；签名通过也无法证明 policy 决策正确。
- **取舍与回退：** canonicalization 降低字符串变体绕过，却会产生 parser 漏判与误拒绝。unknown/unparsed action 必须 ask/deny 或人工审阅；fingerprint、参数或上下文改变后不能复用 approval，observe-only 部署也不得声称具备 enforcement。

### [Post-Training Shifts Confidence](https://arxiv.org/html/2607.13753v1)
[§2](https://arxiv.org/html/2607.13753v1#S2) 以 top-k token probability 构造 Pre-/Intra-/Post-CoT confidence，分别服务难度估计、early stop 与答案聚合；confidence 的 owner 是具体 post-training artifact 与推理阶段，不能从 base model 阈值直接继承。

- **Evaluation：** [§3](https://arxiv.org/html/2607.13753v1#S3) 在同数据的四个 Qwen2.5-7B 变体（base/SFT/RL/OPD）和 AIME24/25、AMC23、MATH500 上比较；[§4](https://arxiv.org/html/2607.13753v1#S4) 显示 OPD 的 pre-confidence、SFT 的 intra-confidence、RL 的 post-confidence 各有优势，RL Top-10 aggregation 相对 majority 平均约提升 5.4 点，而 OPD 的 post-confidence filtering 可能反而变差。
- **Limitations：** [Limitations](https://arxiv.org/html/2607.13753v1#Sx1) 只覆盖一个 backbone family 与数学推理，并依赖内部 token probability；外部 verifier、语言置信、其他 uncertainty signal 和跨域校准未验证。
- **取舍与回退：** 分阶段置信控制可节省 token/改善聚合，却增加每个 artifact、阶段和预算的校准成本。验证集上不优于基线时不启用 confidence routing/filtering，答案聚合退回 majority voting，并在每次 post-training 后重新标定。

### [Generative Compilation](https://arxiv.org/pdf/2607.13921v1)
[Method pp.7–8](https://arxiv.org/pdf/2607.13921v1#page=7) 的 sealor 把 partial program 补成带 placeholder 的可编译完整程序，使 compiler feedback 可在 token 流结束前返回；多个检查并发运行，以 latest-wins 方式向生成器提交当前 verdict。形式化与 Lean mechanization 证明的是 boolean completeness/soundness，不是诊断文本或最终程序语义。

- **Evaluation：** [§7 pp.22–25](https://arxiv.org/pdf/2607.13921v1#page=22) 在 7 个模型、两个 Rust repository task（Translation/UpdatedAPI）、每项两次、temperature 0.6 的固定 harness 中比较 post-generation compilation 与 generative compilation：平均 compiler errors 从 20.7 降到 13.1，功能正确性在 14 个组合中 11 个更优；85.3% task 获得 early feedback，错误检测中位数只需越过出错点 3 行。
- **Limitations：** [Discussion pp.25–26](https://arxiv.org/pdf/2607.13921v1#page=25) 明确形式保证只覆盖 `ok/not ok`，sealor 仍为手写且只验证 Rust 任务；没有 Rust constrained-decoding 对照，调用频率与 compiler 开销也可能抵消收益。
- **取舍与回退：** 提前编译减少错误传播，却增加 sealor 维护、并发检查和过期 verdict 处理。partial checker 不支持或报错时完成生成后再编译；最终 unit/integration test 始终是语义正确性的权威，不得以 prefix 可编译替代。

### [TRACE](https://arxiv.org/html/2607.13988v1)
[Method §3](https://arxiv.org/html/2607.13988v1#S3) 在每个 tool-call boundary 冻结状态，用 frozen reference 对已知 gold answer 的平均 log probability 构造 value，再以相邻状态的 TD delta 分配 turn credit，并与最终 outcome advantage 合并。reference 只估计“距 gold answer 的可预测性”，最终成败仍由 outcome reward 裁决。

- **Evaluation：** [§4](https://arxiv.org/html/2607.13988v1#S4) 使用 synthetic multi-document offline search、ReAct search/open/find 与 exact-match final answer；中等 turn-credit 权重约为 34.7/35.6，相对无传播 30.0 提升，而最大传播反降到 28.9，说明 credit 不是越强越好。
- **Limitations：** [§6](https://arxiv.org/html/2607.13988v1#S6) 只支持短且已知 ground truth 的答案，长结构输出和开放目标无法直接计算该 value；开放环境还可能需要 execution progress 或 subgoal estimator。
- **取舍与回退：** 稠密 credit 缓解稀疏 reward，却把偏差引入 frozen reference 与 gold-answer likelihood。ground truth 不可靠、输出开放或 propagation 对验证集有害时设置 turn weight 为零，退回 outcome-only GRPO 或 execution-based verifier。

### [Do Agent Optimizers Compound?](https://arxiv.org/html/2607.14004v1)
[Method §3](https://arxiv.org/html/2607.14004v1#S3) 冻结两阶段 task split：先用 T1 将 artifact A0 优化为 A1，再以扩展的 T1+T2 产生 A2；分别记录 Phase-1、unseen transfer、Final 与 Lifelong Average，并把旧任务 regression 纳入搜索，而不是让 optimizer 只在当前任务自证成功。

- **Evaluation：** [§5](https://arxiv.org/html/2607.14004v1#S5) 与 [§6](https://arxiv.org/html/2607.14004v1#S6) 使用 Terminal-Bench 2.0 的 12+10 个 hard tasks、每 phase 200 rollouts 和每任务两次 evaluation，对 baseline、GEPA、Meta-Agent 与 RELAI 比较；RELAI 的 76.4 lifelong score 只属于该两阶段 harness。
- **Limitations：** [§7](https://arxiv.org/html/2607.14004v1#S7) 明确任务关联较弱、只运行两个 phase，并假设环境可重复且 verifier 可靠；真实生产中的单次轨迹、非平稳依赖和不完美反馈不在证明范围。
- **取舍与回退：** continual evaluation 能暴露迁移与遗忘，但显著增加 rollout、artifact versioning 和旧任务回归成本。缺少可重复 verifier 或没有连续优化生命周期时，一次性静态评测仍然合适；候选 artifact 让旧任务回退时保留 A1，并拒绝/回滚 A2。

## 5. 缺口与下一步

无

无材料请求。14 项新增机制均已写入正文：`2607.13037` 位于 Ch27“Provenance 必须追踪到派生记录与 token”；`2607.13068` 与 `2607.13095` 位于 Ch49“架构收益必须贯穿完整 Serving Pipeline”；`2607.13071` 位于 Ch75“Compaction 不能把 Partial Observation 提升为已确认事实”；`2607.13093` 位于 Ch52“Stateful Elasticity 必须迁移可验证的 Environment State”；`2607.13332` 位于 Ch36“Rollout 与 Update Pool 的边界可以移动，但 Policy Identity 不能漂移”；`2607.13359` 位于 Ch82“总 Cost 与 Wall-clock Latency 需要不同 Credit Assignment”；`2607.13389` 位于 Ch33“Post-training Compute 应先定位瓶颈，再选择投入位置”；`2607.13591` 位于 Ch77“共享 Memory 需要分离选择性写入、访问权与事实状态”；`2607.13640` 位于 Ch72“异构执行的 Attestation 必须证明跨 CPU–GPU 的 Dispatch Binding”；`2607.13716` 位于 Ch78“Approval 应绑定 Canonical Action Meaning”；`2607.13753` 与 `2607.14004` 位于 Ch66“Post-training 与 Agent Optimizer 都会改变 Evaluation State”；`2607.13988` 位于 Ch31“Tool-call Boundary 可以成为 Turn-level Credit 的状态切面”。其余 4 项的既有正文覆盖保持不变。

## 6. 复核

复核者：`/root/july_evidence_crosscheck`（exact-v1 证据修复）与 `root`（非作者最终语义验收）

结论：通过

18/18 候选的 Method、Evaluation、Limitations、证明边界、具体 trade-off 与可执行回退均已逐项检查；候选分母、评分和 Books disposition 未被证据修复静默改变。

复核记录：

- 候选准入、评分、withdrawn 状态与 owner 沿用 `/root/aug21_31` 的既有独立复核，本轮未改动。
- Books 写后语义复核沿用 `/root/aug01_10` 的结果；本轮未修改 Books 或 Integration disposition。
- `/root/july_evidence_crosscheck` 重新打开 18 个 exact-v1 primary source，对 §4 的 Method、Evaluation、Limitations、证明/未证明边界和具体回退逐项修复并完成作者侧自检。自检确认各项都能定位到论文正文或 PDF 页码，且不再以摘要句、截断文本或通用 trade-off 模板替代 Source Review。

本轮证据修复自检通过；root 已逐项复读 §4，并确认修复后的证据边界与既有 Books Decision 一致。
