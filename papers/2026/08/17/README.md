# Daily Research — 2026-08-17

**规范：** V3
**窗口：** 2026-08-16T09:00:00+08:00 ～ 2026-08-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T22:40:00+08:00

## 1. 结论

本窗重新检查 14 个每日来源。arXiv 以官方 `new` 公告而非 `submittedDate` 归属，共得到 419 个去重身份；从第一项 `2608.13562` 到最后一项 `2608.14546` 完整阅读标题，并对含义不明确或可能进入大模型/大模型 Infra 主线的条目阅读完整摘要，最终保留 16 个材料家族。旧报告从 `2608.15473` 开始的 6 项实际属于 8 月 18 日，已全部移出本窗。未发现入选版本带有 withdrawn 标记。

本窗最重要的三条变化是：生产负载证据要求调度器同时对非平稳需求、prefix locality 与负载均衡负责；有限状态模型、KV Cache 与 MoE 的“内存优化”逐渐从统一压缩演进为按信息价值、访问阶段和物理路径分配资源；确定性、Agent 恢复与跨 session handover 都要求显式记录可提交状态，而不是依赖生成文本看起来一致。

16 项均完成与其分数相称的证据审阅和 Books 比较：6 项形成写回提案，9 项确认由现有正文实质承载，1 项因仅有模拟架构证据保留在日报。共享 Books 尚待主任务按日期统一写回，因此本报告保持进行中。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 归档按日期读过本窗及相邻记录 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 列表按发布日期检查，本窗无正文事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind Blog / Publications 与 Google Research publication 入口按日期检查 | 已检查 | 无 |
| SRC-META-AI | FAIR publication 列表按日期越过本窗起点 | 已检查 | 无 |
| SRC-QWEN | 官方中英文文章目录按日期检查并按家族去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究与更新目录按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog、Research 与 release 入口按事件日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”目录在 Aug11 后直接到 Aug28，本窗无条目 | 已检查 | 无 |
| SRC-ZAI | Research 列表在 Aug14 后直接到 Aug26 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog、Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与官方仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper、Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | Research / Blog 日期序列按窗口检查 | 已检查 | 无 |
| SRC-ARXIV | 官方 `new` 公告 owner 清单，四个主类及主题过滤类；419 个去重身份从批次首项到末项完成题摘语义筛选，保留 16 项 | 已检查 | 无 |

没有按需来源被触发。

## 3. 候选与判断

下表的公开时间表示材料进入本窗的官方 `new` 公告时段；它不是作者提交时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [A Year in LLM Serving](https://arxiv.org/html/2608.13573v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 一年生产 trace 揭示 workload 非平稳及 cache locality / load balance 冲突；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [The Query Knows What to Forget](https://arxiv.org/html/2608.13668v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 为线性 Attention 增加 query-derived、与 key 正交的可编辑方向；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [The Integer Alibi](https://arxiv.org/html/2608.13756v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 将 INT8 kernel 分歧定位到 scale 与输出舍入而非整数累加；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [CForce](https://arxiv.org/html/2608.13925v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 用后期 denoising 预测监督早期 mask 预测，修正并行解码的训练—推理错位；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [MoE Expert Execution with ReRAM Near-Memory](https://arxiv.org/html/2608.13962v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 将 resident expert weight bandwidth 与路由偏斜下的 occupancy 联合设计；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [ForgeWM](https://arxiv.org/html/2608.14022v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 从双向视频生成器逐阶段得到 1/2/4-step causal world-model students；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [KV Cache Compression Through the Lens of Transform Coding](https://arxiv.org/html/2608.14191v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 将 bit allocation 目标从 cache 重构误差改为 attention-aware distortion；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [FreeBalance](https://arxiv.org/html/2608.14205v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 在路由发生前预测 residual workload，并把 expert 迁移隐藏在前序计算中；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Beyond Capacity](https://arxiv.org/html/2608.14333v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 用 direct / HBM-relay 双路径并发交付 HBF-resident experts；2 + 2 + 2 = 6 | 标准完成 | 仅报告：模拟的专用硬件分支 |
| [CoRun](https://arxiv.org/html/2608.14376v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 以 isolated prefill、fixed-shape decode 和 request-bound RNG 获得确定性；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-CONTINUOUS-BATCHING，[Ch46](../../../../books/part-05-inference-system/46-continuous-batching.md) |
| [AgentRewind](https://arxiv.org/html/2608.14380v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 对齐恢复模型 context 与受控环境 checkpoint；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [DeaMoE](https://arxiv.org/html/2608.14385v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 以 department-shared 与少量 private weights 减少 small-batch Decode 的 expert load；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [More Correct Mass, Worse Answers](https://arxiv.org/html/2608.14420v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 证明全局 power sharpening 可增加正确质量却破坏聚合所需路径覆盖；3 + 1 + 3 = 7 | 深入完成 | 整合：MODEL-SAMPLING，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Rollplex](https://arxiv.org/html/2608.14498v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 在同步 VLM RL 中跨 rollout / reference / train phase 重排 prefix 计算与 HBM residency；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Handover of In-Context Learning State](https://arxiv.org/html/2608.14528v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 用 predictive equivalence 定义跨 session handover 的最小充分状态；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Marionette](https://arxiv.org/html/2608.14530v1) | 2026-08-17T08:00:00+08:00 ～ 2026-08-17T09:00:00+08:00 | 将显式 3D state、零参数几何 renderer 与外观生成分开，使长期错误可在 state 层修正；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [A Year in LLM Serving](https://arxiv.org/html/2608.13573v1)

exact-v1 的 §§3–7 基于一年、61.2 亿请求、9,174 个模型的单平台 trace，分别检查需求非平稳性、token shape、prefix reuse 和 routing。证据支持“容量、cache 与 placement 不能由短窗口固定分布共同校准”；它不证明 CompanyX/Chutes 的用户结构代表其他平台，且论文所称 trace 仍是“approved and will be added”，不能写成 artifact 已取得。Ch56 已将 routing、KV locality、placement、autoscaling 和分布漂移放在同一 scheduler contract 中，本材料补的是受限实证而非新机制，因此不再追加正文。

### [The Query Knows What to Forget](https://arxiv.org/html/2608.13668v1)

exact-v1 从 fast-weight update 的可达子空间出发，指出 key-directed delta 无法修改 query 在 key-orthogonal 子空间读取到的干扰；QED 只在该正交方向增加一次 erase，同时保留 rank-one update 和稳定性条件。340M 模型、15B tokens 与合成 retrieval 只支持披露长度和模型，部分消融并不显著，不能把约两倍 usable context 外推为通用倍数。

**已整合位置：** Ch22 在线性/循环状态的“写入、遗忘与可读性”之间。现有命题关注固定容量与状态合并；新增机制是“写入方向决定可编辑子空间，读取 query 可能暴露不可擦除干扰”。静态 key-gating 在上下文较短或额外方向收益不足时仍更简单。

### [The Integer Alibi](https://arxiv.org/html/2608.13756v1)

exact-v1 固定 checkpoint、prompt、hardware、engine、decoding 与 quantization，只替换 CUTLASS / Triton INT8 GEMM；利用无溢出时 INT32 dot product 精确且与 reduction order 无关，把分歧定位到 scale application 与 BF16 rounding。power-of-two scale 恢复受测路径 bitwise agreement，但不证明真实 scale 可任意替换而无质量代价。Ch49 已明确把 reduction order、activation approximation、scale、kernel identity 与 engine artifact 一起冻结，并保留容差与逐位一致的条件分支，故已有覆盖。

### [CForce](https://arxiv.org/html/2608.13925v1)

exact-v1 用预收集 self-rollout trajectory，让较晚 denoising state 的预测监督较早 mask state，并用 confidence-adaptive KL 在 forward/reverse KL 之间调节；实验只覆盖所述 LLaDA 非编辑与可编辑分支。它支持“并行越激进，训练时未见过的早期联合预测越成为错误源”，不证明所有 diffusion LM 都优于 AR。Ch24 已将 mutable generation、trajectory-consistent correction、parallel proposal 与 commit boundary 串成同一演进链，CForce 是该现有命题的训练侧实例，不再重复写入。

### [MoE Expert Execution with ReRAM Near-Memory](https://arxiv.org/html/2608.13962v1)

exact-v1 把实际 MFU 分解为理想 MFU 与 occupancy，并以 core-local multicast、coactivation placement 和 load-aware fetch 处理 sparse expert union 与 routing skew。收益来自 measured + modeled ReRAM/H20 组合，模型为 Qwen3.5 与 GLM-5.2；未披露可部署芯片 artifact，延迟和能耗不能视为现货硬件保证。

**已整合位置：** Ch54 在“capacity tiering”之后补充 bandwidth density 与 occupancy 不同：权重驻留解决容量，不自动解决 routing skew。near-memory pool 只拥有 immutable expert weight delivery，router 仍拥有语义选择；通用 GPU/HBM 在负载小、路由集中或专用硬件不可得时继续成立。

### [ForgeWM](https://arxiv.org/html/2608.14022v1)

exact-v1 的四阶段路线为 domain adaptation → teacher-forced causal training → causal consistency distillation → on-policy distribution matching，并分别训练 1/2/4-step students；双路径部署把实时 draft 与 replay-time refinement 分开。Minecraft/FPS 结果不证明开放物理世界的 causal sufficiency。Ch25 已明确覆盖双向生成到 causal few-step transition、budget-specialized student、replay refinement 与 action-conditioned evaluation 的演进，因此判为已有覆盖。

### [KV Cache Compression Through the Lens of Transform Coding](https://arxiv.org/html/2608.14191v1)

exact-v1 在 white-noise quantization 假设下把 attention-aware distortion 分为 key/value、token/channel 可加项，再用 transform coding 与 reverse water-filling 在 calibration set 上分配 bits。Llama-3.1-8B 与 Qwen2.5-7B 的作者实验支持披露任务上的约 5.8× operating point；它不证明噪声独立、query 分布稳定或 runtime kernel 已高效实现。

**已整合位置：** Ch45 的 variable-rank / water-filling 之后，区分“最小化 cache reconstruction error”与“最小化 downstream attention distortion”。codec basis、calibration/query distribution、bit map、RoPE 和 packed layout 必须进入 cache identity；分布漂移或 kernel 不支持时回退均匀量化/原精度 KV。

### [FreeBalance](https://arxiv.org/html/2608.14205v1)

exact-v1 用 residual hidden representation 预测下一层 expert workload，在 router 给出真实结果前规划有限 swaps，并由 cost model 把迁移约束在可重叠窗口内。作者实验只覆盖两类 MoE、8×A800、EP=8、batch 16、8K prefill 与三次平均，不覆盖 Decode、跨节点或 tail SLO。Ch49 已把它写成 `offline placement → reactive migration → predictive pre-routing migration` 的条件分支，并保留预测失误与回退边界，已有覆盖。

### [Beyond Capacity](https://arxiv.org/html/2608.14333v1)

exact-v1 将 whole experts 分配给 direct GPU–HBF 或 HBF–HBM–GPU relay，两路并行交付，同时把 immutable expert weights 与 mutable KV traffic 分开管理；early determination 尝试把 flash read 藏在前序计算后。证据来自 event-driven continuous-batching simulator 与测得的 GPU compute latency，不是实际 HBF system。它说明双路径可能扩大供给带宽，但尚不足以改变 Books 的通用 memory hierarchy 结论，保留为硬件架构上下文。

### [CoRun](https://arxiv.org/html/2608.14376v1)

exact-v1 区分 batch invariance 与 position invariance：Prefill 隔离，Decode 填充到固定 shape，RNG 绑定 request，从而避免动态 batching 改变 tiling/reduction。Qwen/DeepSeek 的作者实验不证明所有 kernels 都 position-invariant，也未覆盖所有 speculative rollback 与稀疏流量。Ch46 已把固定形状 deterministic verifier 写成 ordinary fast path 之外的 request policy，并记录 padding、等待窗口与 throughput 的代价，故已有覆盖。

### [AgentRewind](https://arxiv.org/html/2608.14380v1)

exact-v1 同时 checkpoint Agent context 与受控 workspace，并在恢复时带回前次失败信息；MettleBench 的 82 个工程任务允许无限 rewind、没有 wall-clock 上限，主要覆盖 workspace，不能证明网络、付款或并发副作用可回滚。Ch81 已明确区分联合 checkpoint、Memory failure evidence、external-effect compensation 与 approval barrier，且保留这一实验边界，已有覆盖。

### [DeaMoE](https://arxiv.org/html/2608.14385v1)

exact-v1 将 experts 组成 departments，共享大部分参数并保留少量 private weights，再用两阶段 router 避免 small-batch Decode 反复装载重复权重。7B 预训练与 DeepSeek-V3 microbenchmark 支持特定模型/A40/H100 operating points，不证明语义专业化、训练稳定性或跨节点吞吐。

**已整合位置：** Ch21 在“稀疏激活不等于减少权重搬运”之后，增加从独立 experts 到 shared trunk + private delta 的结构分支。它用表示耦合和两级 routing 换更小 working set；任务需要高度独立 experts 或共享部分造成 interference 时，标准 MoE 仍合理。

### [More Correct Mass, Worse Answers](https://arxiv.org/html/2608.14420v1)

exact-v1 用 self-consistency 展示固定 exponent 会产生 dose mismatch，并以 pass@k 与 path support 的分离说明 coverage mismatch：正确轨迹总质量上升不保证 aggregation 后答案更好。作者在受测模型/推理 benchmark 上报告最高 18.5 个百分点下降，不能外推所有 verifier/search pipeline；但反例足以推翻“全局 sharpen 单调改善下游”的直觉。

**已整合位置：** Ch20 在 temperature / distribution shaping 与 self-consistency 之间，加入 trajectory-level mass、answer-level aggregation 和 support coverage 三个不同对象。新分支按问题校准 deformation 并保护中等概率路径；单样本低温或无需路径聚合时，简单 sampling 仍成立。

### [Rollplex](https://arxiv.org/html/2608.14498v1)

exact-v1 把 reference/train 的 prefix computation 移入 rollout decode 的 spatial slack，并以 phase-aware residency 与跨 TP layout 的物理 weight sharing 避免完整第二份 actor。32×H800、Qwen2.5-VL-32B 与指定 GRPO contract 只支持该同步 on-policy workload。Ch36 已完整写入 producer–consumer lifetime、layout compatibility、snapshot publication、恢复成本与 colocation/disaggregation 共存条件，已有覆盖。

### [Handover of In-Context Learning State](https://arxiv.org/html/2608.14528v1)

exact-v1 将 handover 定义为保持后续 target distribution，而不是逐字恢复历史；在 exogeneity 条件下，predictive equivalence 给出最粗 deterministic sufficient handover，并用 Gaussian/nonparametric regression 给出有限 memory 的上下界。理论模型不证明开放 Agent 能知道未来 query、自动抽取充分统计量或忠实保存决策。

**已整合位置：** Ch75 在 Context selection 与跨 session continuity 之间，加入 `exact decisions/constraints + task-justified sufficient statistics + unreduced observations` 的三层 record。压缩换空间但承担 writer bias 和 unknown-query risk；高风险、未知任务或证据不可约时保留原文/完整 transcript。

### [Marionette](https://arxiv.org/html/2608.14530v1)

exact-v1 先预测 276 维多实体 3D state，再由零参数 renderer 计算 geometry/occlusion，最后只让 diffusion model 生成 appearance；terrain collider 与 separation cap 可在不改 observation model 时修正长期状态。证据限于交互游戏、两个角色与披露控制，不证明真实环境动力学。Ch25 已把显式可修订 world state、geometry renderer、appearance generation、observation reconciliation 与纯视频生成的共存边界写成完整链路，故已有覆盖。

## 5. 缺口与下一步

无

6 项 Books 增量已写入相应机制正文；其他 10 项均已终态处置，没有剩余可执行工作。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立审查修正了原报告使用 `submittedDate` 造成的整批日期错位，并复核 419 个 official-announcement 身份的首尾覆盖、题摘准入、exact-v1/withdrawn、评分、证据边界与 Books 决定。6 项新增机制均位于对应章节的 `Review notes` 之前，并保留旧方案、代价与作者实验边界；机器校验与 diff 检查通过。
