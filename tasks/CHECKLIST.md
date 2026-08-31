# AI System 24 周执行 Checklist

本文件记录行动；章节当前 Level 只以 [`progress.yaml`](./progress.yaml) 为准。勾选“读完”不等于通过 Level。

## 每周固定项

- [ ] 写下本周中心问题和成功标准。
- [ ] 在学习前完成闭卷基线，不用 Books 修饰已有认知。
- [ ] 为所有实验先写 Hypothesis、Prediction、variables 和 control group。
- [ ] 先验证 correctness，再测性能或质量。
- [ ] 至少主动寻找一个 failure boundary 或反例。
- [ ] 完成一次中文闭卷讲解和一次英文摘要。
- [ ] 把 evidence、blocker 和 knowledge debt 写入 `progress.yaml`。
- [ ] 使用模板完成周复盘；未通过项不得勾成完成。

## Week 1：学习合同与知识树

- [ ] 在 `progress.yaml` 填写 `start_date`、`current_week: 1` 和 `status: in_progress`。
- [ ] 按 L1～L6 审计已有 LoRA、Labs、工作经验，不符合 Gate 的保持 `unassessed`。
- [ ] 完成 Ch1～3 闭卷解释与 Stable Node 定位测试。
- [ ] 完成 Lab 00 的可证伪实验合同和平均值误导反例。
- [ ] 输出个人 Top 10 knowledge debt，不按 Books 篇幅排序。
- [ ] **Gate：**Ch1～3 达到本周目标，实验身份和证据格式可复用。

## Week 2：学习、表示与 Scaling

- [ ] 推导 empirical risk、gradient update 和 train/test distinction。
- [ ] 完成 Lab 01 最小训练循环与 autograd parity。
- [ ] 复现 underfit、overfit、optimization failure、distribution shift 中至少三类。
- [ ] 用小规模数据拟合一次 scaling 关系并故意错误外推。
- [ ] 设计 capability/reliability slice，解释 average metric 的局限。
- [ ] **Gate：**Ch4～8 达标；至少一项训练指标改善但测试能力下降。

## Week 3：系统演化与输入表示

- [ ] 完成 Ch9～13 闭卷解释。
- [ ] 手工完成 BPE merge、embedding lookup 和 RoPE 数值例子。
- [ ] 追踪 `[B,T]→[B,T,d_model]`，标明 token/position identity。
- [ ] 将三项近期技术映射到系统演化路线和 Stable Node。
- [ ] **Gate：**输入表示链 shape 连续，位置性质不是靠记忆结论。

## Week 4：Transformer 主体

- [ ] 实现 Lab 02 的 attention、MHA、MLP、norm/residual 和 decoder path。
- [ ] 对齐 reference output、activation 与 gradient。
- [ ] 注入 causal mask、scale、head layout 和 normalization 错误。
- [ ] 计算 FFN/MHA 参数量、FLOPs 和关键 GEMM shape。
- [ ] **Gate：**Ch14～18 达标；输出可被 Lab 03 加载的 deterministic checkpoint。

## Week 5：Autoregressive、MoE 与 Long Context

- [ ] Cached Decode 与 full recompute logits/token 对齐。
- [ ] 固定 RNG 重放 temperature、top-k 和 top-p。
- [ ] 计算 MHA/GQA/MQA KV bytes 和 context capacity。
- [ ] 复现 MoE load imbalance、capacity overflow 和 execution imbalance。
- [ ] 构造 accepted context 很长但 effective utilization 失败的任务。
- [ ] **Gate：**Ch19～22 达标；cache/router 的 state owner 和失败边界可定位。

## Week 6：多模态、World Model 与 VLA

- [ ] 完成 Ch23～26 闭卷解释。
- [ ] 比较至少两种 fusion 或 generation branch。
- [ ] 注入 modality/time/provenance identity 错误。
- [ ] 区分 observed、predicted、revised、committed state。
- [ ] 注入 environment drift 或 sensor failure 并触发安全降级。
- [ ] **Gate：**Ch1～26 全部至少 L2；完成第一次六周 Compression Pass。

## Week 7：Data、Pretraining、SFT 与 LoRA

- [ ] 建立 dataset identity、split、distribution 和 lineage receipt。
- [ ] 对齐 next-token objective、chat template 和 loss mask。
- [ ] 审计现有 Qwen LoRA run，不合格证据不计分。
- [ ] 增加 rank/target-module 或 base/adapter identity 的受控对照。
- [ ] 验证 weights-only、adapter load 和 exact continuation 的不同语义。
- [ ] **Gate：**Ch27～30 达标；训练产物可追溯到 data/objective/code。

## Week 8：Preference Optimization

- [ ] 为 RLHF、PPO、GRPO、DPO 分别画出 data/state/control flow。
- [ ] 统一比较 demonstration、preference、reward、trajectory 和 reference policy。
- [ ] 复现一个 proxy improvement 但真实 slice 不改善的反例。
- [ ] 复现 GRPO zero-gradient group、length bias 或 truncation noise。
- [ ] **Gate：**Ch31～34 达到第一阶段目标；算法选择是条件表而非排名。

## Week 9：Checkpoint、Collective 与 TP

- [ ] 保存并恢复 model、optimizer、scheduler、RNG 和 data cursor。
- [ ] 在 tolerance 内比较 resumed 与 uninterrupted trajectory。
- [ ] 完成 collective trace、global batch 和 TP reference parity。
- [ ] 扫描 tensor/message shape，记录通信与 GEMM 效率变化。
- [ ] 注入 slow/failing rank 和 checkpoint missing shard。
- [ ] **Gate：**Ch35～37 达标；失败不能表现为静默成功。

## Week 10：PP、ZeRO、Megatron 与 DeepSpeed

- [ ] 模拟 GPipe/1F1B bubble 与 activation timeline。
- [ ] 计算 ZeRO 1/2/3 memory/communication ledger。
- [ ] 追踪 Megatron 和 DeepSpeed 的配置到源码 state owner。
- [ ] 写出 DP/TP/PP/ZeRO/EP/CP 组合选择表。
- [ ] **Gate：**Ch27～41 全部至少 L2；完成训练系统 Compression Pass。

## Week 11：Inference Request State

- [ ] 完成 Ch42～45 闭卷解释和请求状态机。
- [ ] 扫描 prompt/output length、concurrency、TTFT、TPOT 和 goodput。
- [ ] Profile Prefill/Decode，区分 compute、weight/KV bandwidth 和 launch。
- [ ] 验证 KV lifecycle、reuse、eviction 和 corruption detection。
- [ ] **Gate：**单请求 token、KV、stream 和 finish state 同边界提交。

## Week 12：Serving Engine

- [ ] 比较 single/static/continuous batching。
- [ ] 测量 block size、fragmentation、sharing 和 preemption。
- [ ] 验证 speculative acceptance/rejection 与 target-only reference。
- [ ] 追踪 vLLM API→scheduler→KV manager→worker→stream。
- [ ] 追踪 TensorRT-LLM model→engine build→runtime hot path。
- [ ] **Gate：**Ch46～50 达到第一阶段目标；定位吞吐改善但 tail/fairness 变差区间。

## Week 13：Distributed Inference

- [ ] 比较 round-robin、load-aware、state-aware routing。
- [ ] 验证 remote KV identity、freshness、checksum 和 fallback。
- [ ] 推导 aggregated/PD 的 KV transfer 与 break-even。
- [ ] 注入 worker、transfer、selector 和 stale-state failure。
- [ ] **Gate：**Ch51～56 达标；部署建议绑定 workload、topology 和 SLO。

## Week 14：Platform Control Plane

- [ ] 完成 Ch57～62 闭卷解释。
- [ ] 连接 model identity、artifact、workload、service revision 和 route policy。
- [ ] 追踪 Training Operator/KServe reconcile 到实际 workload/endpoint。
- [ ] 验证 canary、rollback、timeout/retry 和 status ownership。
- [ ] **Gate：**control plane、data path 和 evidence plane 不共享模糊真相。

## Week 15：GPU Scheduling、Evaluation 与 Observability

- [ ] 定义 queue、quota、priority、fairness、locality 和 gang requirements。
- [ ] 比较 default、Volcano、KAI 的同一调度场景。
- [ ] 复现 aggregate 通过但 slice/tail/security Gate 拒绝。
- [ ] 为 metrics 和 logs 分别声明可证明与不可证明的结论。
- [ ] **Gate：**Ch63～68 达标；调度和发布决定可解释。

## Week 16：Production Governance

- [ ] 串联 gateway/runtime/GPU/tool 的端到端 trace。
- [ ] 使用实测 workload 建立容量与成本 sensitivity。
- [ ] 注入 noisy neighbor、越权或 artifact 污染。
- [ ] 执行 canary failure、rollback 和 evidence retention。
- [ ] **Gate：**Ch69～73 达标；Ch42～73 全部至少 L2。

## Week 17：Agent Information State

- [ ] 比较 Prompt、Context、RAG、Memory 和 Tool authority。
- [ ] 构造 stale/conflicting/poisoned evidence。
- [ ] 验证 provenance、supersession、delete 和 tenant scope。
- [ ] 注入 tool timeout/duplicate response，防止重复 side effect。
- [ ] **Gate：**Ch74～78 达标；answer/action 可回到 evidence/authority。

## Week 18：Agent Action Workflow

- [ ] 比较 static/dynamic planning 和 bounded reflection。
- [ ] 注入 lost response、duplicate retry 和 partial commit。
- [ ] 比较 single/multi-agent 的质量、token、latency 和错误传播。
- [ ] 追踪 MCP request/response/error 与 trust boundary。
- [ ] **Gate：**84 章全部至少 L2；完成 Agent 与全书主干 Compression Pass。

## Week 19：GPU / CUDA L6 Track

- [ ] 选择一个 GEMM 和一个 Attention workload，冻结 tensor shape 与 correctness。
- [ ] 使用 profiler 区分 occupancy、HBM、Tensor Core、launch 和 transfer。
- [ ] 追踪至少一个 CUTLASS/Triton/TensorRT-LLM kernel path。
- [ ] 改变 head/FFN/expert/shard shape，验证性能预测。
- [ ] 完成 Ch49 未知场景 L6 challenge。
- [ ] **Gate：**形成 GPU bottleneck decision tree，而不是优化技巧列表。

## Week 20：Distributed AI L6 Track

- [ ] 为 TP/PP/EP/ZeRO/PD 建立统一 state/communication ledger。
- [ ] 扫描 collective size、topology、straggler 和 failure。
- [ ] 比较 training layout 与 serving layout，验证可重新切分。
- [ ] 连接 Expert 热点、All-to-All、placement 和 scheduler。
- [ ] 完成 Ch36 未知场景 L6 challenge。
- [ ] **Gate：**设计建议包含 quantitative budget、fallback 和 recovery。

## Week 21：RL Infrastructure L6 Track

- [ ] 串联 dataset→rollout→reward/verifier→advantage→update→checkpoint。
- [ ] 比较 PPO/GRPO/DPO 的 state、通信和 stale-policy 风险。
- [ ] 注入 reward hacking、zero-gradient、length bias 或 evaluator drift。
- [ ] 追踪一个 VERL/Miles 类 runtime 的 rollout 与 weight-sync hot path。
- [ ] 完成 Ch33 未知场景 L6 challenge。
- [ ] **Gate：**能区分算法目标、estimator 问题和 runtime failure。

## Week 22：Inference Runtime L6 Track

- [ ] 构造混合 prompt/output/concurrency/SLO workload。
- [ ] 追踪 request、token progress、KV ownership 和 worker placement。
- [ ] 形成至少三个 competing hypotheses 并用 signals 排除。
- [ ] 比较 batching、paging、speculation、reuse、PD 的正交性。
- [ ] 完成 Ch50 未知场景 L6 challenge。
- [ ] **Gate：**四个 L6 Anchor 全部通过 fresh-context Review。

## Week 23：End-to-End Capstone

- [ ] 从干净环境运行 Data→Training→Checkpoint→Registry→Serving→Evaluation。
- [ ] 接入一个受治理的 Agent action workflow。
- [ ] 注入至少五类 compute/process/state/control/security failure。
- [ ] 保留 raw evidence、trace、rollback 和未证明边界。
- [ ] 邀请 fresh-context Reviewer 按 README 复现或挑战。
- [ ] **Gate：**任一输出可追溯到组合 revision 和 release decision。

## Week 24：最终审计与下一轮

- [ ] 随机抽取 12 章完成闭卷讲解，四柱各至少两章。
- [ ] 完成一次中文和一次英文定量 System Design Mock。
- [ ] 审计 84 个 current/target Level 和所有 evidence links。
- [ ] 对未达标项区分 blocker、knowledge debt 和 target 过高。
- [ ] 输出 `5 principles + 10 trade-offs + 3 state/formulas + 1 system map`。
- [ ] 根据证据制定下一轮 12 周计划，不按未读章节数量规划。
- [ ] **Final Gate：**所有章节至少 L2，L5/L6 均有合格证据，Capstone 可复现。
