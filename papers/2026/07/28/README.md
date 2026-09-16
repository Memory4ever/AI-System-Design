# Daily Research — 2026-07-28

**规范：** V3
**窗口：** 2026-07-27T09:00:00+08:00 ～ 2026-07-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:18:00+08:00

## 1. 结论

本窗从已保存的 arXiv 原始身份表恢复 **1022** 个唯一 identity。逐条检查标题；只有明显属于领域应用、传统算法或与大模型无关的条目才在标题层关闭，其余均读取完整摘要后判断范围与贡献。最终冻结 **30** 个候选，准入率 **2.94%**；其余 **992** 个材料家族在 Candidate Denominator 之前关闭。旧稿把 199 个条目全部视为候选，混入了“能映射 ROADMAP”“属于 AI/ML”或“有局部 benchmark 改进”但没有长期系统设计增量的条目；本次有 **169** 个旧候选被降回准入前关闭。

30 个候选均已取得 exact-v1 HTML，完成了方法、实验和限制边界审阅；未发现入选论文被整篇 withdrawn。Books 对读结果为：**20 项完成实体正文整合，8 项由既有实体正文承载，2 项仅保留在报告**。20 项新增正文已经逐项完成 source-family 绑定、owner 与相邻语义核对，并由非作者独立执行 post-write 复核；本日报据此闭环。

从 07-26 移交的两个 first-public owner 事件已在本窗处理：`arXiv:2607.23250v1`（Libra）进入候选；`arXiv:2607.22997v1`（Real2Sim2Real for VLA Manipulation: AMD ROCm Pipeline）只证明特定 VLA 在 AMD/ROCm 上的移植与实验流水线，不改变可复用的模型或系统责任边界，故作为 family-specific pre-denominator closure 关闭，不评分、不进入 Books。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 当前注册入口在本历史窗口的生效边界之后，不反向扩扫历年目录 | 不适用 | 无 |
| SRC-ANTHROPIC | 同上 | 不适用 | 无 |
| SRC-GOOGLE-AI | 同上 | 不适用 | 无 |
| SRC-META-AI | 同上 | 不适用 | 无 |
| SRC-QWEN | 同上 | 不适用 | 无 |
| SRC-DEEPSEEK | 同上 | 不适用 | 无 |
| SRC-MOONSHOT | 同上；Kimi K3 由本窗 arXiv 原始事件发现，不把机构入口记作已扫描 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 当前注册入口在本历史窗口的生效边界之后，不反向扩扫历年目录 | 不适用 | 无 |
| SRC-ZAI | 同上 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 同上 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 同上 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 同上 | 不适用 | 无 |
| SRC-MINIMAX | 同上 | 不适用 | 无 |
| SRC-ARXIV | 复用 `canonical-raw-identity-inventory-v2.1.json.gz` 中 1022 个去重身份及标题、完整摘要；按 official first-public owner receipt 归属本窗，不使用旧 Weekly 发现候选 | 已检查 | 无 |

原始 1022 个身份的准入前关闭不进入正文候选。主要类型是：非大模型/大模型基础设施的领域应用；传统 CV、机器人、图算法、优化或预测任务；仅局部方法/指标改进而不改变状态、数据流、控制权或 evaluation contract；以及只因通用名词可映射 ROADMAP、但没有新增长期命题的材料。所有关闭均以 family 为单位；ROADMAP 只辅助判断贡献，不作为自动准入白名单。

## 3. 候选与判断

所有 arXiv 公开时间均由 official owner reconciliation 确认落在本窗；原始提交字段与可公开时间不一致的 family 以首次可公开 owner event 为准，不伪造分钟级时刻。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Execution-Grounded Security Testing](https://arxiv.org/html/2607.22569v1) | 2026-07-28T08:00:00+08:00 | 把安全评估从输出文本推进到 tool trace、runtime trace 与文件系统效果；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [HeraSys](https://arxiv.org/html/2607.22578v1) | 2026-07-28T08:00:00+08:00 | 跨并发 workflow 做结构节点复用和联合优先级调度；3+3+2=8 | 深入完成 | 整合：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [The Scaffold Effect](https://arxiv.org/html/2607.22585v1) | 2026-07-28T08:00:00+08:00 | 证明 harness 是评估对象身份和成本的一部分；3+2+2=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MM-ShiftKV](https://arxiv.org/html/2607.22586v1) | 2026-07-28T08:00:00+08:00 | 暴露 multimodal prefill 统计不能代表 decode query 的选择偏差；3+2+2=7 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DynaResize](https://arxiv.org/html/2607.22614v1) | 2026-07-28T08:00:00+08:00 | 把 post-training Rollout/Training GPU 分区变成有语义约束的运行时角色切换；3+3+2=8 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [PRESTO](https://arxiv.org/html/2607.22634v1) | 2026-07-28T08:00:00+08:00 | 对齐 diffusion marginal 与 AR prefix verifier 的候选排序语义；3+2+2=7 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [PTStore](https://arxiv.org/html/2607.22648v1) | 2026-07-28T08:00:00+08:00 | 将 prefix KV 从单机缓存提升为分布式复制和热点均衡状态；3+3+2=8 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Multi-Block Editing](https://arxiv.org/html/2607.22663v1) | 2026-07-28T08:00:00+08:00 | 为已 finalize 的 diffusion block 增加可重开、修订和再次提交的状态；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Co-Harness](https://arxiv.org/html/2607.22688v1) | 2026-07-28T08:00:00+08:00 | 把 model weights 与 data-generating harness 作为共同演进的配对 artifact；3+3+2=8 | 深入完成 | 整合：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [LazyMem](https://arxiv.org/html/2607.22690v1) | 2026-07-28T08:00:00+08:00 | 将 memory 构造从写入时压缩推迟到 query-time selective construction；3+2+2=7 | 深入完成 | 整合：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Mass-Aware Attention](https://arxiv.org/html/2607.22781v1) | 2026-07-28T08:00:00+08:00 | 揭示 softmax 归一化可能抹去重复证据量；2+2+2=6 | 标准完成 | 仅报告：主要证据来自 temporal graph，RAG 增量未改善诊断 head，尚不足以修改 LLM attention 设计结论 |
| [StateAct](https://arxiv.org/html/2607.22798v1) | 2026-07-28T08:00:00+08:00 | 将 computer-use 的行动与完成验证从 pixels 移到程序真实状态；3+3+2=8 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [What Can Be Enforced?](https://arxiv.org/html/2607.22868v1) | 2026-07-28T08:00:00+08:00 | 区分可表示策略、静态判别边界与 intervention 后闭环安全前沿；3+3+2=8 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Libra](https://arxiv.org/html/2607.23250v1) | 2026-07-28T08:00:00+08:00 | 用 attention 的平方成本而非 token 数定义长上下文训练负载；3+3+2=8 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Sparse Event-KV](https://arxiv.org/html/2607.23693v1) | 2026-07-28T08:00:00+08:00 | 把 KV 稀疏化解释为派生状态 materialization，而非简单 token 抽样；3+3+2=8 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Training Language Models to Cooperate with Inference-Time Controllers](https://arxiv.org/html/2607.23771v1) | 2026-07-28T08:00:00+08:00 | 训练分布显式包含部署时 inference controller；3+3+2=8 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [RLSVR](https://arxiv.org/html/2607.23802v1) | 2026-07-28T08:00:00+08:00 | 用 task transformation 构造可自验证 reward，而非强行给开放任务打标；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Agentic Context Management](https://arxiv.org/html/2607.23809v1) | 2026-07-28T08:00:00+08:00 | 将 context 选择、压缩、恢复建模为 agent 可执行但受预算约束的动作；3+2+2=7 | 深入完成 | 整合：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Kalypso](https://arxiv.org/html/2607.23815v1) | 2026-07-28T08:00:00+08:00 | 将 semantic query plan 变成 operator DAG、KV pinning 与 memory-aware admission；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING`，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [WorldDiT](https://arxiv.org/html/2607.23909v1) | 2026-07-28T08:00:00+08:00 | 在单个 diffusion transformer 中联合 world observation 与 action chunk；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SpecBox](https://arxiv.org/html/2607.23933v1) | 2026-07-28T08:00:00+08:00 | 将 sandbox 生命周期与模型生成中的 tool intent 预测联合调度；3+3+2=8 | 深入完成 | 整合：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [ContainmentBench](https://arxiv.org/html/2607.23999v1) | 2026-07-28T08:00:00+08:00 | 把 exposure→propagation→proposal→authorization→commit 拆成阶段证据；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [KAP](https://arxiv.org/html/2607.24260v1) | 2026-07-28T08:00:00+08:00 | 将结构化 knowledge prior 编译成 versioned physical KV access plan；3+3+3=9 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DraftExpert](https://arxiv.org/html/2607.24434v1) | 2026-07-28T08:00:00+08:00 | 在 speculative cost 中加入 target expert expansion、residency 与预取；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Looping Is Not Reliability](https://arxiv.org/html/2607.24604v1) | 2026-07-28T08:00:00+08:00 | 将 verifier evidence 绑定 exact code state，并保留 verified checkpoint；3+3+2=8 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [APPA](https://arxiv.org/html/2607.24625v1) | 2026-07-28T08:00:00+08:00 | 将 monotone taint 的 abort-only 路径扩展为可隔离、可验证返回的恢复路径；3+3+2=8 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Sparse Autoencoders Encode Both Concepts and Functions](https://arxiv.org/html/2607.24645v1) | 2026-07-28T08:00:00+08:00 | 区分 feature activation 可解释性与干预后的 logit-effect geometry；2+2+2=6 | 标准完成 | 仅报告：局部 SAE 干预研究不足以形成平台级 steering/release contract |
| [Kimi K3](https://arxiv.org/html/2607.24653v1) | 2026-07-28T08:00:00+08:00 | 以极稀疏 routing 与固定 expert-parallel shape 展示模型/系统协同；3+3+2=8 | 深入完成 | 已有覆盖：`MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Eviction as Estimation](https://arxiv.org/html/2607.24667v1) | 2026-07-28T08:00:00+08:00 | 将 KV eviction 的决策时机建模为 commit lag，并给出负面适用边界；3+2+2=7 | 深入完成 | 整合：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [The Physics of Multi-Turn Long-Horizon Planning](https://arxiv.org/html/2607.24720v1) | 2026-07-28T08:00:00+08:00 | 用受控环境分离 planning acquisition、shaping 与跨教师 integration；2+2+2=6 | 深入完成 | 整合：`AGENT-PLANNING`，[Ch79](../../../../books/part-07-agent/79-planning.md) |

## 4. 证据与知识整合

### [Execution-Grounded Security Testing](https://arxiv.org/html/2607.22569v1)

采用 exact-v1 §4 的执行证据框架、§5 的多 agent/model workload 和 §6–§7 的边界。论文真正改变的是安全观测单元：模型文本只能描述意图，tool invocation、runtime trace、文件 diff 与 sandbox outcome 才能证明外部效果；execution oracle 只引导 red-team probe，不拥有生产授权。实验支持“常规工程任务可掩护危险操作并触发可验证副作用”，不证明比例能外推到其他权限、工具、模型或真实生产环境。该路径增加高风险样本执行、sandbox 隔离、oracle 假阳性和 trace retention 成本。Ch72“Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate”已完整承载这一命题，故不重复写入。

### [HeraSys](https://arxiv.org/html/2607.22578v1)

采用 exact-v1 §3 的 node merging、load-aware joint scheduling、resource skewing 与 pipeline decomposition，以及 Appendix 的 workload。单 workflow scheduler 只看到局部请求；HeraSys 把多个 workflow 的同构节点和跨工作流优先级放入共同调度状态，使中间结果复用、batching 与关键路径可以联合决策。实验只证明作者 workflow、模型与资源配置下的 P99/throughput 改善，不证明任意语义节点可安全合并，也未给出生产多租户公平和 stale reuse 的普适保证。代价是 DAG identity、等价性检查、租户隔离、优先级反转和全局状态陈旧。该机制现已进入 Ch56“跨 Workflow 复用必须建立 semantic node identity”，并保留独立执行回退。

### [The Scaffold Effect](https://arxiv.org/html/2607.22585v1)

采用 exact-v1 §3–§4 及附录 failure classification。对相同模型、相同任务更换 harness，会改变工具序列、停止规则、等待开销与 tokens-per-solved；因此 leaderboard 的 subject identity 必须是 model×harness×environment×scorer，而非模型名。50 个 Terminal-Bench Pro 任务和三个开源 harness 只支持该局部比较，pass-rate 置信区间并不证明某 harness 普遍更优。完整 trace 与配置提高可复算性，却增加运行成本和 adapter drift。Ch66“Evaluation Identity 必须包含 Harness 与 Environment”已经精确承载，不再新增正文。

### [MM-ShiftKV](https://arxiv.org/html/2607.22586v1)

采用 exact-v1 §3、Appendix A–C 与 §8。传统 prefill-only selection 假定 prefill query 可代表 decode query；多模态 visual tokens 多、decode query variance 更大时，小的排序误差会不可逆地丢掉关键 grounding state。MM-ShiftKV 在 prefill 构造 variance-expanded proxy 并按聚合 attention mass 选择 KV，改变的是 importance sensor，不是 KV 正确性 owner。实验只覆盖所列多模态模型和 benchmark、严格预算下的质量比较，不证明 proxy 是 decode 分布的校准概率或生产 tail-SLO 最优。代价是额外 prefill 估计、proxy 失配与视觉 token 误删。该边界现已进入 Ch45“Multimodal KV 选择必须区分 Prefill key 统计与 Decode query 需求”。

### [DynaResize](https://arxiv.org/html/2607.22614v1)

采用 exact-v1 §3–§5。静态 Rollout/Training GPU 分区在长尾 rollout 下形成 pipeline bubble；DynaResize 将 GPU role、communicator、staged state 与 resize generation 变成运行时状态，在 barrier 边界切换资源，同时声称不改变 RL trajectory/optimizer 语义。作者 workload 支持其吞吐与切换开销结果，不证明对任意 optimizer state、并行拓扑、故障恢复或 asynchronous policy lag 都语义等价。收益以额外 communicator 生命周期、状态搬运、hysteresis 校准与 resize 失败回滚为代价。该状态迁移合同现已进入 Ch36“Rollout 与 Training GPU 角色切换必须是有语义的状态迁移”。

### [PRESTO](https://arxiv.org/html/2607.22634v1)

采用 exact-v1 §1–§2、§5 与讨论/消融。Diffusion drafter 的位置边缘分布不以已选 prefix 为条件，直接用其分数构树会和 AR verifier 的 prefix-conditioned acceptance 错位；PRESTO 用 prefix-aligned score 与 priority search 重排 proposal tree。Draft 仍只拥有 proposal，AR target 拥有逐前缀验证与 output/KV commit。实验只支持所测 diffusion drafter/target/benchmark 的吞吐，不证明所有边缘分布校准，也不保证 self-speculative 模式获得同等收益。代价是树搜索、额外打分、mask/branch state 和低接受率时的浪费。该 mismatch 现已进入 Ch48“Diffusion proposal 与 AR verifier 必须对齐同一个 Prefix 条件分布”。

### [PTStore](https://arxiv.org/html/2607.22648v1)

采用 exact-v1 §4.1、§6–§7。单 engine prefix cache 遇到热点和容量边界后，PTStore 将 prefix tensor 按内容身份分布、复制并从远端复用，cache owner 需要同时持有 digest、replica placement、freshness 与 transfer completion；scheduler 不能把“远端存在”误当成“本地已可读”。作者长文本 QA workload 支持其相对 throughput，不证明跨 model/tokenizer/position layout 的兼容，也未给出生产一致性、租户隔离和故障恢复保证。复制扩大容量并缓解热点，但增加网络、catalog、失效与副本放大。该 replica lifecycle 现已进入 Ch45“分布式 Prefix KV 是带复制与新鲜度的 materialized state”。

### [Multi-Block Editing](https://arxiv.org/html/2607.22663v1)

采用 exact-v1 §2–§4。Block diffusion 提交边界令早期 block 无法利用后来上下文，错误一旦 finalize 就会成为后续条件；MBE 重新打开选定 block、建立 full-attention edit window，并以 multi-shape graph/KV control 支持变量长度重算。旧 block decode 仍适合吞吐优先且错误可接受的工作负载；editing 增加 revision lineage、重新验证、KV invalidation 与 graph pool 内存。论文只在 LLaDA2.1-Mini 和 12 个 benchmark 上证明质量/吞吐取舍，不证明任意 dLLM 或生产 SLO 普遍受益。该演进现已进入 Ch24“已 Finalize 的 diffusion block 也可能需要可控重开”。

### [Co-Harness](https://arxiv.org/html/2607.22688v1)

采用 exact-v1 §3、Appendix F–G。固定 harness 让训练数据生成过程保持在 optimizer 之外；Co-Harness 交替让 HarnessCritic 从失败轨迹提出局部 harness 更新，再用新轨迹更新 weights，从而把 model、prompt、tools、skills、memory 与 verifier 变成配对 artifact。200+ 小时案例支持这一闭环可以发现改进和从部分 crash 恢复，不证明自治 critic 不会 reward-hack、回归或把过拟合写入 harness，也没有生产安全/可复现性保证。代价是双重非平稳、版本组合爆炸、rollback 和独立验证。该交替优化与双向回归 gate 现已进入 Ch84“Model 与 data-generating harness 是共同演进的配对 artifact”。

### [LazyMem](https://arxiv.org/html/2607.22690v1)

采用 exact-v1 §3、Appendix B/C/F。Write-time compression 便宜但在未知未来 query 下不可逆；LazyMem 先宽召回，随后在 query-time 并行窗口内保留并压缩相关证据，把构造结果定义为带 query identity 的 derived memory，而非永久事实。LongMemEval/LoCoMo 结果支持作者模型、retriever、judge 和 token budget 下的质量/压缩取舍，不证明摘要 faithful、跨域长期稳定或能替代源记录。代价是每次查询构造、judge/reward 偏差、宽召回噪声和 derived-state invalidation。该分支现已进入 Ch77“写入时保留 lossless source，读取时再构造 derived memory”。

### [Mass-Aware Attention](https://arxiv.org/html/2607.22781v1)

采用 exact-v1 §III-C、§IV 与 §VII-E。标准 softmax 的 L1 归一化使重复相同 evidence 时分子、分母同比增长，aggregate 可能丢掉 evidence count；Lp family 让 representation magnitude 保留部分 mass。实验主要来自 temporal graph，补充 RAG 诊断没有转化为 downstream 改善，LayerNorm 还可能擦除信号。因此它证明一条 normalization 反例和局部可恢复性，不证明 LLM 应替换 softmax、语言建模会增益或现有 kernel/SLO 可接受。先保留报告，不修改 Ch14。

### [StateAct](https://arxiv.org/html/2607.22798v1)

采用 exact-v1 §5–§6。Screenshot 是 program state 的有损 render；StateAct 让主 agent 用 code 读写文件、DOM/backend 等真实状态，只把确需视觉操作的子目标交 GUI agent，并由独立 finish gate 检查已保存结果。OSWorld 结果支持该 harness 在所测任务中改善成功率/成本，不证明任意应用暴露可靠 program state，也不证明 code path 比 GUI path 更安全。代价是更高权限、schema drift、直接 state mutation 和 finish predicate 漏检；无可读状态时必须回退 GUI observation。该边界现已进入 Ch78“Computer-use Action 与完成判断应优先读取程序真实状态”。

### [What Can Be Enforced?](https://arxiv.org/html/2607.22868v1)

采用 exact-v1 §3、Appendix B 与 §8。论文把三类主张拆开：register 能表示哪些 good-prefix policy；固定外生分布下怎样校准 false-block/miss；阻断会改变后续 proposal 时，为什么静态分数和 ungated trajectory 不能识别 closed-loop frontier。形式结果和 controlled enumeration 支持这些条件化命题，不证明开放 Agent 的状态空间完备、judge 可观测或 conformal 假设持续成立。更强保证需要 policy state、occupancy model、干预后重跑和 robustness margin，代价是状态爆炸、保守 block-all 与模型误设。该边界现已进入 Ch72“可表示、可静态判别与可闭环执行是三层不同安全前沿”。

### [Libra](https://arxiv.org/html/2607.23250v1)

采用 exact-v1 §4–§6。固定 token packing 平衡线性算子和显存，却不平衡 attention 的 `sum(length²)`；Libra 用 bounded sequence pool 在有限 lookahead 内按估计 attention cost 分配，降低 DP straggler/pipeline bubble。实验支持作者数据、长度分布、并行布局与实现中的性能，不证明任意 attention kernel、packing policy 或动态数据流都获益。池越大越能平衡，也增加等待、重排、数据顺序偏差和 scheduler state。该机制现已进入 Ch36“长上下文训练负载不能只按 Token 数均衡”。

### [Sparse Event-KV](https://arxiv.org/html/2607.23693v1)

采用 exact-v1 §1–§2、Appendix C/E 与 §9。关键结论不是“少存 token”：下游 contextualized KV row 可能携带已省略上游 observation 的语义，因此 materialized unit 是派生事件状态；donor-swap/decoy 实验只在所测 model/payload 中支持这条 causal channel。它不证明任意 source 可省略、状态可无损恢复、跨模型可组合或生产 SLO。收益是稀疏物化，代价是事件检测、derived-state provenance、错误遗漏和无法逆推原输入。该机制现已进入 Ch45“Sparse Event-KV 是可重建的派生状态，而不是被抽样的原始 token”。

### [Training Language Models to Cooperate with Inference-Time Controllers](https://arxiv.org/html/2607.23771v1)

采用 exact-v1 的 controller 定义、§6 实验与附录。部署时若 controller 会投票、重采样、反思或选择最终答案，单 response reward 优化的模型可能与该组合规则错配；controller-aware GRPO 直接用 controller 产出的 ensemble outcome 定义训练回报，使 weights 学会产生互补而非孤立最优的轨迹。所测 Llama-3.2-3B、数学任务和 12 种 controller 只证明局部兼容性，不保证跨 protocol、任务或 controller revision 泛化。代价是训练/部署耦合、rollout 成本和 controller drift。该分支现已进入 Ch33“训练目标必须包含部署时 Inference Controller”。

### [RLSVR](https://arxiv.org/html/2607.23802v1)

采用 exact-v1 方法、Appendix C/D 与 §5。开放任务缺 deterministic verifier 时，RLSVR 不直接让 judge 给终局分，而是把任务变换为可生成、可校验的自验证子任务，再以验证信号训练原任务能力。作者实验支持其 task transformation 和所测 judge/任务下的提升，不证明生成的 verifier 无偏、不会缩窄能力或可替代真实 outcome；alternative judge 仍共享建模偏差。代价是 transformation leakage、reward hacking、额外 rollout 和验证覆盖不足。该条件分支现已进入 Ch33“开放任务只有在 Transformation 保留目标且能自验证时才适合 RLVR”。

### [Agentic Context Management](https://arxiv.org/html/2607.23809v1)

采用 exact-v1 §3、Appendix C 与 limitations。固定截断或静态摘要把 context policy 藏在 harness；该工作把 inspect/select/compress/recover 视为 agent 动作，使 context state、预算和任务进度共同驱动选择。实验只支持作者 long-horizon tasks、prompt、model 和 judge 下的 trajectory 改善，不证明 agent 自管 context 能保持安全约束、来源完整性或对所有任务优于 deterministic policy。代价是动作空间扩大、自删关键证据、预算消耗和不可复算性。该 authority 边界现已进入 Ch75“Context Mutation 是 Agent Proposal，State Owner 负责校验与提交”。

### [Kalypso](https://arxiv.org/html/2607.23815v1)

采用 exact-v1 §5.3、§7 与 §9。关系查询中的 semantic operators 构成 DAG，中间 tuple 的 KV 可以跨 operator pipeline 复用；scheduler 联合 operator admission、token-bound memory estimate、KV pinning 与 deadlock fallback。实验只证明所测 query plan/workload 的 completion-time 改善，不证明任意 UDF、模型、硬件或生产 tail-SLO。更细粒度调度换来计划身份、内存预测误差和跨 operator backpressure。Ch56 当前正文已包含 relational query plan/operator admission/KV pinning 机制，故无需重复。

### [WorldDiT](https://arxiv.org/html/2607.23909v1)

采用 exact-v1 §2–§4。单 diffusion transformer 同时生成 continuous action chunk 和 future RGB patch，把 world prediction 作为 action representation 的共同训练约束。LIBERO 四套模拟结果只说明一个 sub-billion parameter joint baseline 的 Pareto 位置，不证明视觉预测因果正确、真实机器人安全、开放动作支持或 world branch 对 planning 的必要性。联合模型减少独立 backbone，却增加 objective interference，且真实 observation 仍是 transition authority。Ch25 已经完整区分 visual generation、action-conditioned transition、imagined state 和 physical evidence，故本项作为受限案例已有覆盖。

### [SpecBox](https://arxiv.org/html/2607.23933v1)

采用 exact-v1 §3–§6。常驻 sandbox 浪费内存，按需启动增加 tail latency；SpecBox 在 token generation 中用 intent sensor 预热 sandbox，并沿 dependency graph 预取后续环境，结果 cache 和共享内存传输是相邻但独立优化。预测只拥有资源 proposal，tool policy/actual call 才能 commit sandbox 使用；误预测必须可回收。作者 agent trace 支持所测 P99/内存结果，不证明 keyword/embedding intent 在新工具、对抗 prompt 或多租户下可靠。代价是误预热、资源抢占、cache 身份和权限泄漏。该机制现已进入 Ch84“Sandbox 预热只能由 Tool Intent 生成 proposal”，并与 LLM engine 调度保持 owner 分离。

### [ContainmentBench](https://arxiv.org/html/2607.23999v1)

采用 exact-v1 §3–§6、§8。相同“最终未违规”可能对应不同 propagation、proposal 和 authorized utility；benchmark 因此保存 exposure→propagation→proposal→authorization→commit trace，而不是让 endpoint attack rate 独占 verdict。synthetic workflow 与所测模型只支持阶段指标的区分力，不证明零观察等于安全，也不证明 intent-ledger schema 在现实工具中完备。代价是 parser/policy/scenario 版本和敏感 trace 治理。Ch72“Containment 不能只看最终是否发生攻击”已逐项承载，故不新增。

### [KAP](https://arxiv.org/html/2607.24260v1)

采用 exact-v1 §2.2、§4–§7。结构化 evidence/graph prior 若只序列化为 prompt，runtime 仍会密集读取全部 KV；KAP 把 prior 编译成 versioned access plan，由 executor 在保持逻辑 prompt 的同时改变 physical KV consumption，并保留 exact fallback。实验只支持所测 4K–128K QA、模型和 GraphSpec，不证明计划选择无损、跨模型可移植或生产尾延迟。代价是 IR、compiler/runtime 版本耦合、错误 sparse access 与回退成本。Ch45“Structured knowledge 只有进入 physical access plan 才改变 KV 成本”已经承载。

### [DraftExpert](https://arxiv.org/html/2607.24434v1)

采用 exact-v1 方法与实验/消融。专家 offload 场景中，验证一个 draft block 会触发各位置 target-expert union；因此 acceptance 不能单独代表收益。固定驻留 draft expert、confidence–expansion truncation 与 target prefetch 将 expert residency/transfer 加入 speculation contract，最终 token/KV 仍由 target 精确验证提交。实验只覆盖 DeepSeek-V2-Lite、Moonlight-16B-A3B 与两类 offload，不证明模型全驻留或生产 batch 获益。Ch48“MoE verification 还要结算 target-expert expansion”已精确承载。

### [Looping Is Not Reliability](https://arxiv.org/html/2607.24604v1)

采用 exact-v1 §4–§8。重复 generate-test-revise 会让 stale trace 评价已经变化的 code state；论文将 verifier evidence 绑定 code digest/revision，保留 verified checkpoint，并分开 admission、preservation、certification、competence 与 liveness。实验支持 stale evidence 会伤害一部分已正确起点，也显示保护策略可能降低修复能力；它不证明 typed contract 能提高模型 competence 或 verifier 可靠。代价是 checkpoint/trace lineage、额外验证和保守停止。该机制现已进入 Ch81“Verifier Evidence 必须绑定生成它的 exact code state”。

### [APPA](https://arxiv.org/html/2607.24625v1)

采用 exact-v1 的双阶段 reference monitor、trajectory confinement、证明与实验。传统 monotone taint 在读入不可信数据后只能永久阻断；APPA 在 dispatch 前检查 composite labels，返回后再决定 output 是否进入主 context，并把不可信探索放到 disposable child branch，只允许 shape-bounded、保留 provenance 的结果返回。形式不变量和 6600 个受控 episode 支持该 threat model 内的 no-laundering/branch isolation，不证明自然语言标签完备、隐式信道关闭或现实生产零攻击。代价是 label/schema、branch transcript、cast resolution 和误拒绝。该恢复路径现已进入 Ch72“Taint 传播需要可隔离、可验证返回的恢复路径”。

### [Sparse Autoencoders Encode Both Concepts and Functions](https://arxiv.org/html/2607.24645v1)

采用 exact-v1 §3–§4、Appendix F 与 §7–§8。FEGA 在多 context 中移除同一 active SAE feature，比较 logit-effect cloud，从而区分“激活描述清楚”“因果影响存在”和“存在稳定 steering direction”。结果显示 value-like/pointer-like features 的 downstream geometry 不同，且一维可复用方向罕见；这只支持所测 SAE/model/intervention，不证明所有 feature 或生产 steering policy。它是重要的证据边界，但尚不足以形成平台 release 机制，故仅报告。

### [Kimi K3](https://arxiv.org/html/2607.24653v1)

采用 exact-v1 §2、§5.1、§6 与 §8。长期增量不是厂商榜单，而是 routing objective 与 executable shape 的耦合：quantile-based balancing、固定 expert-parallel shape 与关键路径无 host synchronization 共同决定极稀疏 MoE 是否可执行。作者模型报告只证明 Kimi K3 artifact 与披露训练/评测，不证明这些机制普遍最优，2.5× scaling efficiency 也不能脱离其口径外推。更静态的 shape 换来 controller state、分布漂移和稀有 expert 风险。Ch21 已经以版本化案例承载该机制。

### [Eviction as Estimation](https://arxiv.org/html/2607.24667v1)

采用 exact-v1 的 commit-lag framework、§7 controlled experiments 与 §10。现有 policy 在 item 到达时立即决定保留（H=0）；fixed-lag smoothing 延迟 commit，观察近未来的实际使用再驱逐，把不可观测 future guess 换成有界的 demonstrated utility。受控场景支持该机制，但第三方自然文本 benchmark 上优势大多消失甚至更差，明确说明 reuse 不尖锐或 correctness weighting 与 attention 重合时不值得等待。代价是 delayed eviction、暂存容量和 observation lag。该设计轴与负结果现已进入 Ch45“Eviction 还要选择何时提交，而不只是选择删谁”。

### [The Physics of Multi-Turn Long-Horizon Planning](https://arxiv.org/html/2607.24720v1)

采用 exact-v1 的受控 environment、pretraining acquisition、GRPO/OPD shaping、MOPD integration 与 §8 边界。论文区分：atomic skill 并不自动组合成长程计划，少量长程轨迹可提供 transition structure；错误轨迹会随 horizon 放大；post-training 是否有效取决于已有能力 support 和 teacher planning pattern 是否兼容。实验只支持该合成环境、模型与教师配置，不证明真实工具世界或开放知识迁移；多教师还会引入模式冲突和遗忘。该受限演进现已进入 Ch79“Planning 能力要区分 Acquisition、Shaping 与 Integration”，没有把 OPD/MOPD 写成普适优胜者。

## 5. 缺口与下一步

无

20 项新增机制已分别进入 Ch24、Ch33、Ch36、Ch45、Ch48、Ch56、Ch72、Ch75、Ch77～79、Ch81 与 Ch84 的实体正文；每项均有唯一 source-family 绑定，并保留证据边界、代价、失败回退和旧路径。8 项 `Existing Coverage` 经主文对读确认不是 trace-only，2 项 `Weekly Only` 没有越过长期知识门槛。

### 材料缺口

本窗候选没有阻塞材料请求：30/30 exact-v1 HTML 均可读，方法、实验与限制位置可定位。未固定的代码仓库 commit 不用于支持实现或性能主张，因此不构成当前 Books 机制写入的阻塞条件；若后续要声称实现可复现，再单独重开对应 artifact audit。

### 关闭项重开条件

992 个准入前关闭项不因“以后出现相似关键词”自动重开。只有出现新的原始证据，明确改变大模型/大模型基础设施的状态所有权、数据流、控制权、evaluation contract 或 Books 既有结论，才重开对应 family。`arXiv:2607.22997v1` 只有在作者给出超出 AMD/ROCm 移植案例、可复用且经比较验证的运行时机制时重开。

## 6. 复核

复核者：非作者独立智能体 `/root/aug21_31`

结论：通过

非作者复核重新检查了固定北京时间窗口、1022→30+992 算术、候选准入与 withdrawn 状态，并逐项对读 20 项新增正文与 8 项 `Existing Coverage`。20 项新增机制均位于对应 Stable Node 的主文、source-family 标记唯一，且包含论文证明/未证明、state/control/commit owner、trade-off、fallback 与相邻章节边界；没有发现重复段落或用 trace 冒充正文。8 项既有覆盖分别在 security effect evidence、evaluation harness identity、operator-DAG scheduling、world-state authority、containment stage evidence、physical KV access plan、MoE verification cost 与 routing-shape coupling 的实体论证中成立。复核中发现的 6 条旧 Daily owner 日期错绑已全部更正为 `2026-07-28`。机器校验只验证格式与一致性，不替代上述语义结论。
