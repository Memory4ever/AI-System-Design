# Daily Research — 2026-07-01

**规范：** V3
**窗口：** 2026-06-30T09:00:00+08:00 ～ 2026-07-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T15:20:00+08:00

## 1. 结论

本窗复用并核实 609 个去重 arXiv v1 身份；逐条先读标题、含糊项再读完整摘要后，14 个材料家族通过当前贡献门槛。旧恢复队列共有 41 项，其中 27 项因规范/可访问性应用、通用工作流、社交平台审计、普通领域路由或仅重复已有 Agent 组织方式而转为 pre-denominator closure；不是因审阅成本删候选。

真正的主线集中在五类约束变化：安全不能只看 attack success，还要计量 fidelity；训练和 Agent 状态需要可撤销或可归因的 owner；长上下文 KV 由固定预算转向可恢复的分层表示与估计误差；speculation 必须保留 target/commit authority；多模态 workflow 需要同时管理控制流、数据流与执行流。14 项均已完成与其评分相称的原始版本审阅。5 项历史 `Integrate` 已在 Books 正文找到真实承载位置，其余为已有覆盖，不新增重复文字。

Anthropic 6 月 30 日的 Sonnet 5 发布与 Fable 5 redeploy 也落在本窗，但前者只披露版本、tokenizer 与厂商评价，后者主要是访问恢复和 safeguard policy；二者没有公开足以改变当前 Books 机制结论的新实现证据，均在贡献筛选前关闭。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 与 News 按 6 月 30 日事件检查；Sonnet 5、Fable 5 已做贡献关闭；因不进入候选，不再为其追查分钟级发布时间 | 已检查 | 无 |
| SRC-GOOGLE-AI | 该源在目标历史窗口后才成为每日固定源；本次不作追溯性覆盖断言 | 不适用 | 无 |
| SRC-META-AI | 同上 | 不适用 | 无 |
| SRC-QWEN | 同上 | 不适用 | 无 |
| SRC-DEEPSEEK | 同上 | 不适用 | 无 |
| SRC-MOONSHOT | 同上 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 同上 | 不适用 | 无 |
| SRC-ZAI | 同上 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 同上 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 同上 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 同上 | 不适用 | 无 |
| SRC-MINIMAX | 同上 | 不适用 | 无 |
| SRC-ARXIV | 复核本窗公告 owner、609 个去重 v1 身份与 41 项旧恢复队列；标题全量语义筛选，边界项读取完整摘要，14 项入选 | 已检查 | 无 |

本窗由 RaBitQCache 触发其作者仓库定点核查；代码只支持公开 artifact 身份，不冒充性能复现。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Security–Fidelity Tradeoffs](https://arxiv.org/html/2606.30783v1) | 2026-07-01T08:00:00+08:00 | 防注入评价必须同时度量 security 与 fidelity；`3+3+3=9` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Revocable Learned State via Process Sidecars](https://arxiv.org/html/2606.30788v1) | 2026-07-01T08:00:00+08:00 | 把可撤销私有学习状态从公共权重隔离；`3+2+3=8` | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Predictable GRPO](https://arxiv.org/html/2606.30789v1) | 2026-07-01T08:00:00+08:00 | 用受限闭式动力学解释 group size 与训练轨迹边界；`2+2+2=6` | 标准完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [When Calibration Rankings Reverse](https://arxiv.org/html/2606.30814v1) | 2026-07-01T08:00:00+08:00 | 校准比较需控制 accuracy，否则模型排序可翻转；`3+2+3=8` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Does Learning to Stop Help?](https://arxiv.org/html/2606.30852v1) | 2026-07-01T08:00:00+08:00 | early-exit 收益取决于轨迹结构、错误容忍度与 probe/re-prefill 成本；`2+2+3=7` | 深入完成 | 已有覆盖：`INFER-DECODE`，[Ch44](../../../../books/part-05-inference-system/44-decode.md) |
| [RoPoLL](https://arxiv.org/html/2606.30931v1) | 2026-07-01T08:00:00+08:00 | judge 聚合需要显式污染模型与鲁棒边界；`2+2+2=6` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Omni-Flow](https://arxiv.org/html/2606.31093v1) | 2026-07-01T08:00:00+08:00 | 多模态推理把 workflow、tensor/KV identity 与执行计划统一成三层 owner；`3+3+3=9` | 深入完成 | 已有覆盖：`INFER-SGLANG`，[Ch51](../../../../books/part-05-inference-system/51-sglang.md) |
| [SeKV](https://arxiv.org/html/2606.31145v1) | 2026-07-01T08:00:00+08:00 | KV 从二元保留/驱逐扩展为 query-adaptive resolution 与可恢复层级；`2+2+2=6` | 标准完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [BlockPilot](https://arxiv.org/html/2606.31315v1) | 2026-07-01T08:00:00+08:00 | input-aware block policy 调整 speculative depth，但 target 保持验证权；`2+2+2=6` | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [RaBitQCache](https://arxiv.org/html/2606.31519v1) | 2026-07-01T08:00:00+08:00 | 低比特无偏 proxy 支持 attention-mass Top-p，并暴露索引扫描与不规则执行成本；`3+2+3=8` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [MemLearner](https://arxiv.org/html/2606.31734v1) | 2026-07-01T08:00:00+08:00 | 视频世界模型的读取策略随帧与 denoising timestep 变化；`2+2+2=6` | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [TRIAGE](https://arxiv.org/html/2606.32017v1) | 2026-07-01T08:00:00+08:00 | heterogeneous agent trajectory 需要 role-typed credit，而非广播单一 outcome advantage；`2+2+3=7` | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Reinforcement Learning with Metacognitive Feedback](https://arxiv.org/html/2606.32032v1) | 2026-07-01T08:00:00+08:00 | 自报置信度必须绑定外部正确性校准，不能直接当真值概率；`2+2+3=7` | 深入完成 | 已有覆盖：`TRAIN-RLHF`，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [QVal](https://arxiv.org/html/2606.32034v1) | 2026-07-01T08:00:00+08:00 | 在完整训练前以 reference-Q 筛选 dense supervision signal；`2+2+2=6` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Security–Fidelity Tradeoffs](https://arxiv.org/html/2606.30783v1)

精确版本为 v1。1,168 个样本、48 个配置只支持其 security–fidelity frontier，不能外推到未测防御或生产攻击分布；Ch72 已把 fidelity 写成 security 之外的独立 release 约束。

**Evidence Review 细节。**
- **拟采用命题：** prompt-injection defense 若通过统一压低不可信文本影响力获得安全，会同时破坏必须原样处理的数据；security 与 fidelity 是两个独立 release constraint，不能由单一 attack-success 指标代替。
- **证据与未证明：** exact v1 的 1,168 样本、48 配置支持论文 threat model 内存在可测的 security–fidelity frontier；不证明未测 defense、适应性攻击或生产流量仍落在同一 frontier，也不证明模型内抑制可替代模型外 effect gate。
- **证据定位：** Method 为 §3.2、Appendix A.2、E.1；Evaluation 为 §3/§3.4、§4；Limitations/边界为 §2 threat model 与 §7。
- **取舍与回退：** 更强的指令抑制能降低已测注入成功率，却会损坏必须原样保留的不可信文本；当 fidelity slice 越界时，应把数据与指令通道隔离并交给模型外 effect gate，而不是继续提高统一抑制强度。

### [Revocable Learned State via Process Sidecars](https://arxiv.org/html/2606.30788v1)

精确版本为 v1。Qwen-2.5 0.5B/1.5B 与 Llama-3.2-1B 的实验支持 sidecar 撤销分支，不证明任意架构完全遗忘；Ch77“可撤销状态与 process sidecar”已承载机制、provenance 代价与重训 fallback。

**Evidence Review 细节。**
- **拟采用命题：** 需要撤销的 learned state 应从公共参数基底分离到带 provenance 的 process sidecar，使删除操作只撤销私有增量而不默认破坏公共技能。
- **证据与未证明：** Qwen-2.5 0.5B/1.5B 与 Llama-3.2-1B 的作者实验支持受测 sidecar 撤销分支；不证明任意架构完全遗忘，也不证明 sidecar 组合后不存在表征残留或旁路泄漏。
- **证据定位：** Method 为 §3 与 safety-post-training/sensitivity 描述；Evaluation 为 §2、§5/§5.1；Limitations 为 §6、§7、Appendix B.7。
- **取舍与回退：** sidecar 提高可撤销性，却新增基底/私有状态的版本绑定、组合推理与泄漏面；若撤销后行为或表示审计仍残留目标信息，应停用 sidecar 并回到隔离数据后的重训/恢复路径。

### [Predictable GRPO](https://arxiv.org/html/2606.30789v1)

精确版本为 v1。闭式模型在三个模型、两个 group size 的作者设置中拟合良好，但 residual group dependence 与 OOD transfer 限制其普适性；Ch33 仅把它作为诊断模型。

**Evidence Review 细节。**
- **拟采用命题：** GRPO 的 reward rate、group size 与噪声可在局部线性化域内形成闭式诊断模型，用于预测更新趋势而不是取代真实训练曲线。
- **证据与未证明：** 三个模型、两个 group size 的作者设置支持局部拟合；residual group dependence 与 OOD transfer 表明它不是普适动力学定律，也不能据此承诺大规模训练稳定性。
- **证据定位：** Method/假设为 §3.1 与训练算法描述；Evaluation 为 §4/§4.2、Figure 7 的线性化边界；Limitations 为 §6。
- **取舍与回退：** 闭式模型降低试参成本，却依赖线性化区间、group-size 与数据分布；residual 或 OOD 误差超出校准范围时，只能把它当诊断先验并回退真实训练曲线与保守超参搜索。

### [When Calibration Rankings Reverse](https://arxiv.org/html/2606.30814v1)

精确版本为 v1。结果说明不控制 accuracy 时 calibration ranking 会翻转；Ch66 已把 accuracy、calibration 与 scorer contract 分离。

**Evidence Review 细节。**
- **拟采用命题：** calibration ranking 必须控制 accuracy 与 confidence-elicitation method；否则能力差异会把“更准确”伪装成“更校准”，甚至反转排序。
- **证据与未证明：** exact v1 支持受测模型/任务中 accuracy conditioning 会改变 calibration ranking；不证明某个 calibration metric 或 elicitation 方法对所有模型族公平，也不能从条件排序推出部署可靠性。
- **证据定位：** Method 为 calibration metrics/methods、confidence elicitation 与 §4 ACE；Evaluation 为 §4 setup；Limitations 为 Limitation 与 §7。
- **取舍与回退：** accuracy-controlled 比较减少能力差异造成的混杂，却会引入匹配/重采样方差并改变评价分布；因此必须同时报告原始 accuracy、条件化 calibration 与置信区间，不能用单一排序替代。

### [When Does Learning to Stop Help?](https://arxiv.org/html/2606.30852v1)

精确版本为 v1。同一 stopper 在 KV fork 与黑盒重复 prefill 下成本方向可反转；Ch44 已把退出策略绑定 lost-correct risk、probe overhead 与执行路径。

**Evidence Review 细节。**
- **拟采用命题：** reasoning early exit 必须把 lost-correct risk、stopper calibration、probe overhead 与真实执行路径放入同一停止合同；不能只用少生成 token 证明省成本。
- **证据与未证明：** 作者实验支持同一 stopper 在可复用 KV fork 与黑盒重复 Prefill 下成本方向可反转；不证明跨模型/任务稳定，也不证明 stop score 等同答案正确概率。
- **证据定位：** Method 为 training-free exit、§3/§3.3；Evaluation 为 §4/§4.1；Limitations 为 §5、§7。
- **取舍与回退：** 提前停止节省 decode work，却承担 lost-correct risk 与 probe 开销；没有 KV fork、probe 未校准或答案仍不稳定时，应继续完整推理而不是复用黑盒重跑成本来宣称收益。

### [RoPoLL](https://arxiv.org/html/2606.30931v1)

精确版本为 v1。结论依赖论文定义的 judge 污染模型与聚合器；Ch66 已承载污染假设、鲁棒聚合与 evaluator version 边界。

**Evidence Review 细节。**
- **拟采用命题：** LLM judge panel 的误差可能相关且呈 Byzantine/systematic bias，聚合合同必须显式声明污染比例、相关性与不确定性，不能假设独立高斯噪声。
- **证据与未证明：** exact v1 支持其定义污染模型下鲁棒聚合优于简单平均；不证明现实 judge 满足污染上界或独立性，也不证明 panel consensus 是事实 ground truth。
- **证据定位：** Method 为 §3/§3.1；Evaluation 为 §6/§6.1、§6.7 noisy-GT control；Limitations 为 scope/limitations 与 §7。
- **取舍与回退：** 鲁棒聚合可降低有界污染的影响，却可能压掉有效少数意见，并依赖污染比例与 judge 独立性假设；假设不可验证时回退独立 evaluator、人工抽检和分歧保留。

### [Omni-Flow](https://arxiv.org/html/2606.31093v1)

精确版本为 v1。论文给出 Control/Data/Compute Flow 三层抽象与跨角色 KV sharing，但没有受控端到端 benchmark；Ch51 已写入三类 owner、layout compatibility、atomic eviction 与恢复责任。

**Evidence Review 细节。**
- **旧方案与约束变化：** `本章的核心判断是：**SGLang 将 language-model program 的结构暴露给 runtime，使 prefix reuse、structured generation 与并行分支不再只是应用层偶然模式，而能成为 KV management 和 scheduling 的输入。**`（`books/part-05-inference-system/51-sglang.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** 多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。 它改变 `INFER-SGLANG` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.31093v1#S3 :: declarative cyclic graph, streaming frames, OR-AND activation and static plan; https://arxiv.org/html/2606.31093v1#S4 :: framework-owned global KV/tensor pools, tiered storage and distributed metadata; https://arxiv.org/html/2606.31093v1#S5 :: SGLang interface takeover and common LLM/DiT execution path`；Evaluation：`https://arxiv.org/html/2606.31093v1#S7 :: three supported deployment scenarios are described; the v1 paper does not publish a controlled benchmark or independent comparison`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31093v1#S7 :: framework is early-stage; performance, attention variants, TP/CP transfer, cache-aware scheduling and broader model coverage remain future work`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** 框架级 KV/tensor 共享减少重复计算，却把全局 metadata、layout compatibility、原子驱逐和恢复责任引入统一 runtime；身份或布局不能证明兼容时，回退角色内独立执行和重算。

### [SeKV](https://arxiv.org/html/2606.31145v1)

精确版本为 v1。方法把 KV 从保留/驱逐推进到 query-adaptive resolution，同时新增 CPU 回取和 segmentation 风险；Ch45 已承载分层表示与恢复边界。

**Evidence Review 细节。**
- **旧方案与约束变化：** `Offload/recall can keep a recoverable cold tier and use query-dependent selection to fetch only the needed KV, but selector calibration, host transfer, prefetch misses and pinned-memory capacity enter the Decode critical path.`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L350-L390`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** KV capacity can be managed as query-adaptive resolution rather than a binary keep/evict decision: compact GPU summaries choose spans, coarse contributions remain resident, and selected CPU bases are reconstructed on demand. This preserves recoverability but moves routing calibration, segmentation quality and host bandwidth into Decode correctness and latency. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.31145v1#S3 :: entropy-guided spans, GPU routing summaries, query-adaptive zoom and CPU-resident low-rank bases`；Evaluation：`https://arxiv.org/html/2606.31145v1#S4 :: author evaluation covers long-context retrieval/reasoning workloads and several open-weight backbones; performance figures are not promoted outside that contract`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31145v1#S6 :: sensitivity to span quality and thresholds, host-device bandwidth, adversarial repeated activation and untested broader modalities`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** query-adaptive resolution 减少常驻 KV，却增加分段误判、CPU 回取和不规则读取；query shift、miss 或质量预算越界时恢复高分辨率热 KV 或完整重算。

### [BlockPilot](https://arxiv.org/html/2606.31315v1)

精确版本为 v1。controller 只选择候选 block，target 仍保留 exact verification；Ch48 已承载 label search、predictor drift、batch opportunity cost 与串行 fallback。

**Evidence Review 细节。**
- **旧方案与约束变化：** `本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**`（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** 固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.31315v1#S2.SS3 :: local candidate interval and hidden-state classifier for per-instance block size; https://arxiv.org/html/2606.31315v1#S2.SS4 :: label construction and model integration`；Evaluation：`https://arxiv.org/html/2606.31315v1#S3 :: author evaluation spans math, code and chat workloads with autoregressive and diffusion speculation baselines; no result is externalized as a production constant`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31315v1#A3 :: offline label search scales with model and candidate count; broader policy generalization and cheaper search remain open`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L641-L656`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** 自适应 block 深度减少无效 draft work，却新增 controller 预测、label 搜索与 batch 碎片；target 必须保留 exact verification，预测漂移或机会成本过高时回退固定深度/串行解码。

### [RaBitQCache](https://arxiv.org/html/2606.31519v1)

精确版本为 v1。旋转后 1-bit proxy 支持 attention-mass Top-p，但引入索引空间、扫描和不规则执行成本；Ch45 已承载 estimator-to-quality gap 与 exact mode 边界。

**Evidence Review 细节。**
- **旧方案与约束变化：** `KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算。`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** 固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.31519v1#S3.SS2 :: randomized rotation, 1-bit Key index, correction factor and unbiased estimator; https://arxiv.org/html/2606.31519v1#S3.SS3 :: INT4 Query scan, adaptive Top-p selection, exact selected KV plus local window; https://arxiv.org/html/2606.31519v1#S3.SS4 :: asynchronous Prefill index construction and lazy Decode updates; https://arxiv.org/html/2606.31519v1#A1.SS3 :: unbiased estimator, high-probability error bound and an explicit Top-p application remark; the remark is rationale, not a Top-p mass or retrieval-quality theorem; https://arxiv.org/html/2606.31519v1#A1.SS4 :: proofs of estimator unbiasedness/error bound and query-quantization error`；Evaluation：`https://arxiv.org/html/2606.31519v1#S4.SS1 :: vLLM 0.10.2, FlashInfer 0.5.3, LMCache, Triton/custom CUDA and NVIDIA Hopper architecture (exact GPU SKU not disclosed); https://arxiv.org/html/2606.31519v1#S4.SS2 :: LongBench, RULER 8K-64K and GSM8K on LongChat-7B and LLaMA-3.1 8B/70B with baseline configurations and p thresholds; https://arxiv.org/html/2606.31519v1#S4.SS3 :: TTFT, TBT and end-to-end latency for 10K-32K contexts; author maximums are 3.88x TBT and 2.16x end-to-end, not production constants`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31519v1#S4.SS4 :: p-sensitivity and centroid re-centering ablation; removing re-centering changes LongBench average 50.63 to 50.25; the uniform-hypersphere assumption may fail for clustered Q/K and under Decode drift; https://arxiv.org/html/2606.31519v1#A3.SS1 :: index-space derivation; https://arxiv.org/html/2606.31519v1#A3.SS2 :: complexity derivation; exact GPU SKU, serving concurrency, arrival process, precision outside the selector, tail-SLO and independent replication are not disclosed`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** 1-bit proxy 降低候选扫描成本，却占用索引空间并产生 proxy miss 与不规则 kernel；attention-mass 估计未满足质量预算时回退 exact score 或完整 KV attention。

### [MemLearner](https://arxiv.org/html/2606.31734v1)

精确版本为 v1。learned query 只在作者视频模型中证明长上下文读取收益，不提供 action-conditioned causal world state；Ch25 已把它放在 persistent-but-revisable context 分支。

**Evidence Review 细节。**
- **旧方案与约束变化：** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep. It improves selective reuse without granting causal world-state semantics, and introduces full-context growth, entity-binding error, query-policy drift and a separate need for compression, update and forgetting. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.31734v1#S3.SS2 :: learned query tokens extract timestep- and frame-dependent information from context under diffusion loss; https://arxiv.org/html/2606.31734v1#S4 :: mixed rendered/real data strategy`；Evaluation：`https://arxiv.org/html/2606.31734v1#S5 :: author evaluation and ablations cover long-video persistence on an internal 1B model and an open video backbone; no causal-control claim is retained`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31734v1#S6 :: failures with many interacting characters, linear full-context growth, and open compression/update/forgetting problems`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L747-L761`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** learned query 压缩长视频读取成本，却可能不可逆丢失未来问题所需帧，而且不产生 action-conditioned causal state；不确定或分布外请求应保留/重读源帧而不是把压缩记忆当世界真值。

### [TRIAGE](https://arxiv.org/html/2606.32017v1)

精确版本为 v1。role taxonomy 与 judge 不是 causal credit ground truth；Ch33 已承载 typed credit、taxonomy/version ownership 与 reward hacking 风险。

**Evidence Review 细节。**
- **旧方案与约束变化：** `Typed Credit first aligns sample identity with role, block, subgoal and receiver-tested decision boundaries; local process signals remain subordinate to a hard outcome gate and do not establish causal credit by themselves.`（`books/part-04-training-system/33-grpo.md#L865-L890`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** Broadcasting one outcome advantage across a heterogeneous trajectory confuses exploration, infrastructure, decisive action and regression. Role-typed segment correction can reduce that dilution, but the role judge is not ground truth and cannot establish causal credit; its taxonomy, estimator and policy/verifier versions become training state. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.32017v1#S2 :: segment roles and role-conditioned correction over GRPO advantage; https://arxiv.org/html/2606.32017v1#S4 :: MSE/variance rationale and failure conditions`；Evaluation：`https://arxiv.org/html/2606.32017v1#S5 :: author experiments cover three agent environments and two student policies; one search setting has only a single run`；Limitations/Counterevidence：`https://arxiv.org/html/2606.32017v1#S6 :: role labels are semantic estimates, context dependent and not causal identification`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L888-L902`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** role-typed credit 减少广播式 reward 的误归因，却依赖 taxonomy、judge 版本与局部可观测性，并可能被角色策略利用；分层证据不足时保留终局 outcome 与轨迹复核，不自动提交局部更新。

### [Reinforcement Learning with Metacognitive Feedback](https://arxiv.org/html/2606.32032v1)

精确版本为 v1。faithful calibration 依赖任务、模型、自信号提取与外部 correctness；Ch31 已把 metacognitive feedback 限定为训练信号，而非“模型知道自己不知道”的证明。

**Evidence Review 细节。**
- **旧方案与约束变化：** `Reward uncertainty can prioritize trusted human or oracle feedback, but the learned reward remains a proxy whose calibration, distribution coverage and exploitability must be validated independently of policy optimization.`（`books/part-04-training-system/31-rlhf.md#L258-L303`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** Self-reported uncertainty can become a training signal only after binding intrinsic-confidence extraction to externally judged correctness. Metacognitive feedback may align expression with that internal signal, but does not make language confidence a calibrated probability and introduces self-signal collapse, metric dependence and reward-hacking risk. 它改变 `TRAIN-RLHF` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.32032v1#S2 :: intrinsic-confidence extraction, metacognitive data selection and metacognitive advantage scaling; https://arxiv.org/html/2606.32032v1#A2 :: training details`；Evaluation：`https://arxiv.org/html/2606.32032v1#S4 :: author numerical/factual evaluations and ablations are task- and model-scoped; expressed confidence is not promoted as a universal probability`；Limitations/Counterevidence：`https://arxiv.org/html/2606.32032v1#A3.SS3 :: equal-width cMFG has empty-bin and restricted-support failure modes; self-signal still requires external correctness calibration`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L732-L746`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** metacognitive feedback 能把自信号变成训练特征，却会继承不忠实自报、校准漂移与 reward hacking；它必须由外部 correctness 校准，失配时撤销该信号，不能取得回答或执行的事实权威。

### [QVal](https://arxiv.org/html/2606.32034v1)

精确版本为 v1。reference-Q 是 dense supervision 的早期筛选 proxy，不等于最终策略质量；Ch66 已区分 proxy、训练和最终 evaluator contract。

所有性能数字继续绑定作者披露的 model、workload、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 `Not Disclosed`，本次未复现实验。

**Evidence Review 细节。**
- **旧方案与约束变化：** `A dense process score is only a training proxy and must be checked against future return, terminal verifier evidence and critical slices; correlation does not make it causal credit or a deployment correctness gate.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L749-L752`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。
- **机制、状态与代价：** A dense supervision signal should be screened against future return or reference Q before paying for full policy training. This is a proxy-quality gate, not a deployment verifier: reference-policy coverage, horizon truncation and offline correlation still limit what the score proves. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。
- **证据定位：** Method：`https://arxiv.org/html/2606.32034v1#S2 :: reference-policy Q alignment as an offline contract for dense signals; https://arxiv.org/html/2606.32034v1#S3 :: controlled dataset construction`；Evaluation：`https://arxiv.org/html/2606.32034v1#S4 :: author comparison covers multiple signal families, environments, modalities and open-weight backbones; correlation is not causal credit or final policy quality`；Limitations/Counterevidence：`https://arxiv.org/html/2606.32034v1#S6 :: training-free Q alignment remains bound to reference-policy quality, trajectory coverage and controlled environment labels`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L875-L887`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。
- **取舍与回退：** reference-Q 可在完整训练前淘汰明显弱信号，却可能因 proxy 偏差、初始策略与任务分布而误排序；边界不稳时回退小规模训练试验和最终 evaluator，而非用 proxy 直接发布策略。
## 5. 缺口与下一步

无

本窗没有外部材料请求。需要写回的五项历史语义增量均已在现有 Books 正文找到可核查 anchor；非作者独立复核已确认这些段落仍准确承载，不需再次追加。

## 6. 复核

复核者：主任务独立复核（非本报告作者）

结论：通过

独立复核逐项检查 14 个候选的窗口归属、exact-v1 locator、评分与 Books 处置，并重读对应章节正文；五项旧 `Integrate` 的机制命题均已有正文 anchor，不是只有 trace。另对旧队列中的 VLA 可识别性、belief trajectory、RAG hallucination probe、多模态 uncertainty 等高风险排除项，以及应用型 Agent/VLA 项分层抽检；未发现需要恢复的系统性漏项。格式校验与 `git diff --check` 通过。
