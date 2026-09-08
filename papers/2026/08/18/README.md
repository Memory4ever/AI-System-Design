# Daily Research — 2026-08-18

**规范：** V3
**窗口：** 2026-08-17T09:00:00+08:00 ～ 2026-08-18T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T23:30:00+08:00

## 1. 结论

本窗重新检查 14 个每日来源。arXiv 按官方 `new` 公告归属得到 1,151 个去重身份；已从批次首项 `2608.14550` 到末项 `2608.16889` 完整阅读标题，并对可能改变大模型或大模型 Infra 长期判断的条目阅读摘要，最终保留 24 个材料家族。旧报告只有 3 项且把提交时刻当公开时刻，既漏掉整批材料，又把实际属于 8 月 19 日的 SkillEffect 放进本窗；本版已纠正。

本窗形成三条演进：Serving 从静态指标和统一分页转向 workload、硬件、Agent 拓扑与 state identity 联合决策；训练与 Agent runtime 从只恢复进程演进为同时恢复模型可见上下文、KV 与环境副作用；kernel、量化和并行优化都要求 correctness gate 与 artifact identity，而不能只比较吞吐数字。24 项均完成与分数相称的证据审阅，未发现候选版本被 withdrawn。9 项长期机制已经写入 Books，14 项由现有章节实质承载，1 项仅保留日报。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 Research 索引按本窗日期检查 | 已检查 | 无 |
| SRC-ANTHROPIC | 官方 Research 日期列表检查 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind Blog / Publications 与 Google Research 入口按日期检查 | 已检查 | 无 |
| SRC-META-AI | 官方 publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方中英文文章目录按日期过滤并去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Updates / Research 按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog / Research 与 release 入口按日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”日期列表从 Aug11 跳到 Aug28 | 已检查 | 无 |
| SRC-ZAI | 官方 Research 列表从 Aug14 跳到 Aug26 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research / Blog / Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方 Paper / Blog 日期序列检查 | 已检查 | 无 |
| SRC-MINIMAX | 官方 Blog / Research 日期序列检查 | 已检查 | 无 |
| SRC-ARXIV | 官方 `new` owner 清单；1,151 个身份从首项到末项完成题摘语义筛选，保留 24 项 | 已检查 | 无 |

没有按需来源被触发。

## 3. 候选与判断

下表公开时间表示材料进入本窗的官方 `new` 公告时段，不是作者提交时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [CacheCraft](https://arxiv.org/html/2608.14555v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | correctness-gated program search 寻找 KV eviction scorer；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Agentic Kernel Optimization](https://arxiv.org/html/2608.14560v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 将 kernel 生成约束为 correctness、anti-hacking、profiling 闭环；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [HW-Router](https://arxiv.org/html/2608.14575v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | queue、KV、TTFT/TPOT 与设备状态联合路由；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [CacheScout](https://arxiv.org/html/2608.14624v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | Agent 转移图预测固定前缀复用并联合 eviction/prefetch；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Belayer](https://arxiv.org/html/2608.14635v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 分离 GPU worker 与环境恢复并维护 prefix consistency；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-CHECKPOINT，[Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [AGENTCHAOSBENCH](https://arxiv.org/html/2608.14680v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 成对正常/故障 trace 定位跨组件 runtime fault；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [The Recall Trap](https://arxiv.org/html/2608.14838v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 固定 context budget 下 recall 上升可降低任务成功；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Wide-Area Distributed Inference Co-Design](https://arxiv.org/html/2608.14967v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | KV 迁移、重算、压缩、routing 与 WAN capacity crossover；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KSERVE-TOPOLOGY，[Ch53](../../../../books/part-05-inference-system/53-kserve-llm.md) |
| [P-PAS](https://arxiv.org/html/2608.15171v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | token budget 成为 prefill/decode pressure 的闭环变量；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [AgentR](https://arxiv.org/html/2608.15264v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | intent、query、assessment 变为可恢复 workflow artifacts；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [ExactMoE](https://arxiv.org/html/2608.15383v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 保持 top-k 语义，以 host W4 expert bank + GPU slot cache 管驻留；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Q-First](https://arxiv.org/html/2608.15473v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 调整依赖图以重叠 memory-side KV sweep 与 compute；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [FlashQuant](https://arxiv.org/html/2608.15531v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 融合 dense low-bit GEMM 与 sparse outlier path；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [DeltaLog](https://arxiv.org/html/2608.15533v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | dense base + bounded update log 延迟物化 recurrent state；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [GraniKV](https://arxiv.org/html/2608.15584v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | shared prefix 与 private suffix 使用不同分页粒度；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-PAGED-ATTENTION，[Ch47](../../../../books/part-05-inference-system/47-pagedattention.md) |
| [KV-Rescue](https://arxiv.org/html/2608.15797v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 用小模型 full-context steps 修补 eviction 信息缺口；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Bounded Agents](https://arxiv.org/html/2608.15888v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | delegation chain 累计收紧 scope、budget 和历史约束；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Aborted but Not Forgotten](https://arxiv.org/html/2608.15939v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | transcript rollback 不等于 model-visible KV rollback；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [KV-Pipe](https://arxiv.org/html/2608.15943v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | cross-layer KV sharing 成为 Pipeline balance 的结构旋钮；3 + 2 + 2 = 7 | 深入完成 | 整合：TRAIN-PIPELINE-PARALLEL，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [Pallas](https://arxiv.org/html/2608.16477v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | handover 前预测并拆分 prefix recompute/suffix migration；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [The Working Set of a Coding Agent](https://arxiv.org/html/2608.16630v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 将失败归因于耦合事实不在可用 working set；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [LM Head Gradient Bottleneck](https://arxiv.org/html/2608.16671v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | causal intervention 区分梯度几何压缩与有害瓶颈；3 + 1 + 3 = 7 | 深入完成 | 仅报告：受限负结果 |
| [ClawGym II](https://arxiv.org/html/2608.16798v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | opaque harness 调用重建为 trajectory tree；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Proteus](https://arxiv.org/html/2608.16844v1) | 2026-08-18T08:00:00+08:00 ～ 2026-08-18T09:00:00+08:00 | 随上下文推进逐步解锁 memory capacity；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |

## 4. 证据与知识整合

### [CacheCraft](https://arxiv.org/html/2608.14555v1)

v1 将 eviction 限定为可检查 scorer interface，再以 cascade evaluator、输出不变量和 reward-hacking 诊断演化程序。RULER 4K/8K、两种 8B 模型只证明该搜索空间可行。Ch45 已覆盖 attention-aware signal、预算和漂移；LLM 只产生 proposal，已有覆盖。

### [Agentic Kernel Optimization](https://arxiv.org/html/2608.14560v1)

B200 与 FlashInfer-Bench 的三类 workload 采用生成、编译、profile、修复和 correctness gate；相对 PyTorch 的倍数不能外推。Ch49 已冻结 kernel、shape、hardware、数值与 correctness contract，Agent 不拥有验收权。

### [HW-Router](https://arxiv.org/html/2608.14575v1)

predictor 合并模型/input shape 与 queue、KV occupancy、GPU utilization、近期 TTFT/TPOT；受测 workload 的改善不证明跨集群稳定。Ch56 已要求 router 读取实时资源与 tail state，并在漂移时回退。

### [CacheScout](https://arxiv.org/html/2608.14624v1)

系统在线学习 Agent transition，不要求预先给 workflow DAG；预测只拥有 prefetch/eviction hint，不能改变 prefix identity。**已整合：** Ch45 在 recency/attention-aware eviction 后加入 semantic transition 分支，预测错误只浪费容量，identity validation 仍是 reuse gate。

### [Belayer](https://arxiv.org/html/2608.14635v1)

worker failure 验证 owner/GPU health 后复用 weight/raw arena 并按 prefix 重建 KV；environment failure 则恢复 filesystem/runtime 并协调 LLM context。Ch35 已承载两类状态与外部不可逆副作用边界。

### [AGENTCHAOSBENCH](https://arxiv.org/html/2608.14680v1)

五个 A2A/MCP 应用、十类故障与 275 条 trace 说明最终分数不足以定位 tool/model/guardrail/delegation failure。Ch67 已有 typed trace、跨组件因果链与 fault injection，保留为受限评价实例。

### [The Recall Trap](https://arxiv.org/html/2608.14838v1)

论文固定 12-slot context、模型和环境，只切换 per-file dedup；更高 gold-file recall 却降低两个模型的 issue resolution。**已整合：** Ch76 在“召回率不是最终目标”后补充 budget-conditioned evidence composition：检索单元、冗余、文件深度与 executor 搜索权共同决定成功。

### [Wide-Area Distributed Inference Co-Design](https://arxiv.org/html/2608.14967v1)

材料把跨站 KV 迁移与重算、压缩、locality routing、packet/optical capacity 放进同一 workload model；阈值依 70B、MHA/GQA 和链路假设。Ch53 已以 state size、recompute、network tail 和 locality 做选择，不写死数值。

### [P-PAS](https://arxiv.org/html/2608.15171v1)

vLLM 的 MBT 在低 pressure 时宜大、高 pressure 时宜小；相同阈值不能跨模型/SLO 外推。Ch56 已将 token budget 写成负载反馈变量，并保留 oscillation/starvation guard。

### [AgentR](https://arxiv.org/html/2608.15264v1)

PostgreSQL 持久化 intent、queries、assessment、gap 与 usage，BullMQ 只推进显式状态和 retry；技术栈不是必要条件。Ch81 已覆盖 durable state、idempotency、resume 与审计。

### [ExactMoE](https://arxiv.org/html/2608.15383v1)

所有 routed expert 以 group-128 W4、MARLIN-native 形式驻留 host pinned memory，GPU slots 缓存热专家；“Exact”不指数值等价。Ch54 已有 immutable weight tiering、slot identity 与 miss 成本。

### [Q-First](https://arxiv.org/html/2608.15473v1)

KV sweep 只依赖 query，因此作者交换 attention/FFN 使 memory-side sweep 与 compute-side block 并行；相对误差不证明任意 checkpoint 可透明换序。**已整合：** Ch55 增加“改变依赖图而非增加 in-flight sequences”的分支，并绑定训练/模型兼容性。

### [FlashQuant](https://arxiv.org/html/2608.15531v1)

W4 dense GEMM 与 sparse outlier SpMM 在同一 tile 融合，收益主要针对 memory-bound Decode；准确率、outlier pattern 与 shape 均受合同限制。Ch49 已把 mixed-precision subpaths、fusion 与数值验证归于 execution plan。

### [DeltaLog](https://arxiv.org/html/2608.15533v1)

完整 recurrent state 改成 dense base + bounded compact-update log，并周期 merge。**已整合：** Ch45 分离逻辑状态、物理增量日志与 materialization epoch；cache identity 必须包含 base version 和 log prefix。

### [GraniKV](https://arxiv.org/html/2608.15584v1)

HOT pool 为 shared prefix 保留连续大粒度，COLD pool 为 suffix 使用 token-level allocation。**已整合：** Ch47 从 uniform page 演进到 region-specific granularity；代价是双 allocator、迁移和 fragmentation accounting。

### [KV-Rescue](https://arxiv.org/html/2608.15797v1)

小型 full-context helper 的步骤与被 eviction 的大模型 interleave，改变生成路径而非恢复被删 KV，收益依额外 compute。Ch45 已覆盖 lossy eviction 后的 recompute/helper/quality fallback。

### [Bounded Agents](https://arxiv.org/html/2608.15888v1)

APC 沿 principal chain 累积 scope、budget 与 prior actions，sub-agent 只能缩权；形式化 closure 不证明工具都 enforce。Ch72 已写明 delegation attenuation 与 action history authorization。

### [Aborted but Not Forgotten](https://arxiv.org/html/2608.15939v1)

same-token/different-cache audit 固定决策 tokens，仅改变 stale KV 是否重建。**已整合：** Ch45 加入 rollback consistency：commit cursor 同时约束 transcript、KV pages、prefix hash 和 speculative branch；无法证明时重建 committed prefix。

### [KV-Pipe](https://arxiv.org/html/2608.15943v1)

tail-first cross-layer KV sharing 改变每层 FLOPs 并迭代降低 pipeline imbalance；它是模型结构改动。**已整合：** Ch38 增加“先改 partition，再改 per-layer work”的分支；checkpoint 不可改时仍使用标准 PP。

### [Pallas](https://arxiv.org/html/2608.16477v1)

handover 前在目标重算 stable prefix 并迁移 evolving suffix；预测错误、竞争和重规划会制造负载。Ch45 已写入预测式迁移、residency hint 与 identity fallback。

### [The Working Set of a Coding Agent](https://arxiv.org/html/2608.16630v1)

七模型五 harness 的 supply/withhold 实验显示缺失依赖事实时 Agent 常编造，更多 token 无法修复，陈旧 convention 甚至更差。**已整合：** Ch75 把 dependency working set 作为 context selection 目标，并在写动作前校验耦合事实可用。

### [LM Head Gradient Bottleneck](https://arxiv.org/html/2608.16671v1)

backward-only intervention 保持 logits 与 LM-head update，只降低回传 rank；几何压缩有损，但 forward factorization 更有害，辅助反馈未超过 tuned backprop。规模限于 WikiText-2 小模型，只作为对强因果断言的反证。

### [ClawGym II](https://arxiv.org/html/2608.16798v1)

model-boundary proxy 捕获 opaque harness 调用，按 prefix tree 恢复轨迹并适配 PPO/GRPO；sandbox、retry、retokenization 与 shared terminal reward 限制已在 Ch33 写明。

### [Proteus](https://arxiv.org/html/2608.16844v1)

早期 bottleneck 强制压缩，随后随时间解锁 memory capacity，减少早期 token 占满状态。**已整合：** Ch22 在 fixed-capacity memory 后加入 capacity scheduling；短上下文或早期细节必须无损时静态容量仍合理。

## 5. 缺口与下一步

无

9 项 Books 增量已写入相应机制正文；其余候选均已终态处置，没有剩余可执行工作。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核检查了 1,151 个 official-announcement 身份的首尾覆盖、分层题摘筛选、24 项准入与漏项、exact-v1/withdrawn、§3/§4 对齐及 Books 实际落点。9 项新增机制均位于对应章节的 `Review notes` 之前，保留了适用条件、代价与实验边界；机器校验与 diff 检查通过。
