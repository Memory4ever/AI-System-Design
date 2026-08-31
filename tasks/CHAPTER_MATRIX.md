# 84 章学习深度矩阵

本矩阵定义第一轮 24 周结束时的目标，不代表当前掌握度。当前状态只读取
[`progress.yaml`](./progress.yaml)。所有章节至少通过 L2；表中目标高于 L2 的章节还必须完成对应证据。

## Part I 世界观

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch1 `WORLDVIEW-WHY-AI-SYSTEM` | 模型部署、能力交付与完整 AI System 的边界 | L3 | 为一个优秀 Demo 写出 production gap、状态流和能力发布门禁 | 1 |
| Ch2 `WORLDVIEW-AI-HISTORY` | 能力范式如何随数据、算力和系统约束演化 | L2 | 闭卷重建设计演化时间线，并解释三处旧方案共存边界 | 1 |
| Ch3 `WORLDVIEW-KNOWLEDGE-TREE` | capability production、delivery、governance 与 Agent loop | L3 | 将五项陌生技术定位到 Stable Node，并解释 owner 冲突 | 1 |
| Ch4 `WORLDVIEW-WHY-MODELS-LEARN` | objective、gradient、optimization 与泛化的不同职责 | L5 | 完成 Lab 01，区分 optimization failure、overfit 与 shift | 2 |
| Ch5 `WORLDVIEW-REPRESENTATION` | 分布式表示、inductive bias 与可解释性边界 | L4 | 对小模型 activation/embedding 做 probe，并给出不能证明的结论 | 2 |
| Ch6 `WORLDVIEW-TRANSFORMER` | content-dependent routing、短依赖路径与并行训练 | L3 | 比较 RNN、Conv、Attention 的依赖路径、并行度和新瓶颈 | 2 |
| Ch7 `WORLDVIEW-SCALING-LAW` | 经验幂律、compute-optimal allocation 与外推边界 | L3 | 从小规模数据拟合 log-log 关系并展示一次错误外推 | 2 |
| Ch8 `WORLDVIEW-LLM-INTELLIGENCE` | operational capability、emergence、可靠性与意识边界 | L3 | 设计 capability/reliability 分层评估并解释 aggregate 失真 | 2 |
| Ch9 `WORLDVIEW-SYSTEM-EVOLUTION` | Pipeline、Serving、平台与 Agent runtime 的瓶颈迁移 | L3 | 从单机训练到 Agent 画出 artifact、state 和 control handoff | 3 |
| Ch10 `WORLDVIEW-FUTURE` | 约束驱动情景分析而非产品预测 | L2 | 为两个未来方向写驱动力、新瓶颈、不确定性和证伪信号 | 3 |

## Part II 模型基础

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch11 `MODEL-TOKENIZER` | 文本到 token ids 的离散接口与压缩权衡 | L4 | 手工完成一次 BPE merge，比较多语言长度与 byte fallback | 3 |
| Ch12 `MODEL-EMBEDDING` | lookup、连续表示、output projection 与 weight tying | L4 | 用 one-hot 等价验证 lookup，追踪 `[B,T]→[B,T,d]` | 3 |
| Ch13 `MODEL-POSITION-ENCODING` | 顺序注入、relative position 与 RoPE 旋转 | L4 | 数值验证 RoPE dot product 的相对位置性质和长度边界 | 3 |
| Ch14 `MODEL-SELF-ATTENTION` | Q/K/V routing、mask、softmax 与 shape | L5 | Lab 02 attention 与 reference 对齐，并注入 mask/scale 错误 | 4 |
| Ch15 `MODEL-MULTI-HEAD-ATTENTION` | head split、子空间与 MHA/GQA/MQA | L4 | 推导三种 KV shape、参数量和容量差异，验证 layout 转换 | 4 |
| Ch16 `MODEL-FFN` | token-wise nonlinear transform、SwiGLU 与 GEMM shape | L5 | 比较 MLP/GLU/SwiGLU correctness、参数/FLOPs 与执行 shape | 4, 19 |
| Ch17 `MODEL-TRANSFORMER-LAYER` | residual、normalization 与可堆叠梯度路径 | L5 | 比较 Pre/Post-Norm activation 和 gradient，保留失败配置 | 4, 19 |
| Ch18 `MODEL-DECODER-ONLY` | causal objective、shifted targets 与生成接口 | L4 | 从 `[B,T,V]` loss 推到逐 token loop，并完成 reference parity | 4 |
| Ch19 `MODEL-KV-CACHE` | 模型级 K/V state 来源和缓存前后计算 | L5 | Lab 03 cached/full-recompute logits 对齐并计算 cache bytes | 5 |
| Ch20 `MODEL-SAMPLING` | logits、temperature、top-k/top-p 与随机状态 | L4 | 固定 logits 比较采样策略，验证重新归一化和 RNG replay | 5 |
| Ch21 `MODEL-MOE` | router、conditional capacity、load balance 与 dispatch | L5 | Lab 04 复现热点 Expert、capacity failure 与 grouped execution | 5, 19, 20 |
| Ch22 `MODEL-LONG-CONTEXT` | accepted length、position、利用率与系统容量 | L5 | 构造有效信息位置实验并联合计算 attention/KV capacity | 5, 22 |

## Part III 多模态、生成与世界模型

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch23 `MULTIMODAL-REPRESENTATION` | modality、time、alignment 与 provenance identity | L3 | 注入模态/时间错配并解释 fusion 输出为何仍可能看似合理 | 6 |
| Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS` | AR、Diffusion、masked generation 的 commit contract | L4 | Lab 05 对比两种生成 trace、可修正状态与执行成本 | 6 |
| Ch25 `MULTIMODAL-WORLD-MODELS` | action-conditioned transition、latent rollout 与事实状态 | L3 | 用 toy environment 区分 observed、predicted 和 committed state | 6 |
| Ch26 `MULTIMODAL-EMBODIED-VLA` | perception、action chunk、controller 与环境反馈 | L3 | Lab 06 注入 environment drift，验证 safety fallback | 6 |

## Part IV Training System

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch27 `TRAIN-DATA` | 数据身份、分布、质量、synthetic data 与 lineage | L5 | 设计分布 shift/contamination 对照，保留 dataset receipt | 7, 21 |
| Ch28 `TRAIN-PRETRAINING` | next-token objective、batch、信号与能力 prior | L4 | 实现最小 objective，区分 loss、gradient、数据和系统信号 | 7 |
| Ch29 `TRAIN-SFT` | chat template、loss mask 与 demonstration distribution | L5 | 对同一数据比较 mask/template 变化和 held-out 行为 | 7, 21 |
| Ch30 `TRAIN-LORA` | low-rank update、adapter identity、merge 与部署 | L5 | 审计现有 LoRA run，补 rank/target-module/base-adapter 回归 | 7, 21 |
| Ch31 `TRAIN-RLHF` | 偏好信号、能力/行为分布变化与评估切片 | L5 | 构造平均 KL 相近但 slice regression 不同的反例 | 8, 21 |
| Ch32 `TRAIN-PPO` | rollout、reward、advantage、clip/KL 与多状态训练 | L5 | toy PPO 追踪 policy/reference/value/optimizer state 和 instability | 8, 21 |
| Ch33 `TRAIN-GRPO` | group-relative estimator、DAPO 分支与 RL runtime | L6 | 复现 zero-gradient/length bias，完成 VERL 风格 rollout 诊断挑战 | 8, 21 |
| Ch34 `TRAIN-DPO` | offline preference objective、reference 与 beta | L5 | 同一 preference set 比较 DPO/SFT，并检查 rejected slice | 8, 21 |
| Ch35 `TRAIN-CHECKPOINT` | 可恢复、可转换、可部署的完整模型资产 | L5 | Lab 07 中断恢复、corruption rejection 与 lineage 对齐 | 9, 20 |
| Ch36 `TRAIN-DISTRIBUTED-TRAINING` | process group、collective、global batch 与 failure | L6 | 完成多进程 trace、slow/failing rank 诊断和并行方案预算 | 9, 20 |
| Ch37 `TRAIN-TENSOR-PARALLEL` | 单层 operator shard、collective 与 GEMM shape | L5 | TP/reference 数学对齐，扫描 shard shape 与通信 break-even | 9, 19, 20 |
| Ch38 `TRAIN-PIPELINE-PARALLEL` | stage partition、microbatch、bubble 与 schedule | L5 | 模拟 GPipe/1F1B timeline，测 bubble、activation 和 failure | 10, 20 |
| Ch39 `TRAIN-ZERO` | model-state redundancy、shard 与通信/恢复成本 | L5 | 计算并验证 stage 1/2/3 memory ledger 和 collective 差异 | 10, 20 |
| Ch40 `TRAIN-MEGATRON` | 多维并行组合与 Megatron runtime owner | L4 | 绑定版本追踪 TP/PP/EP/CP 配置到核心源码和 checkpoint | 10, 20 |
| Ch41 `TRAIN-DEEPSPEED` | ZeRO/runtime 组合、offload 与生命周期 | L4 | 追踪配置到 state partition/communication 路径，比较 Megatron 边界 | 10, 20 |

## Part V Inference System

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch42 `INFER-REQUEST-LIFECYCLE` | admission、Prefill、Decode、stream 与完成状态 | L4 | 为一次请求生成可回放状态 trace 和 TTFT/TPOT 边界 | 11, 22 |
| Ch43 `INFER-PREFILL` | prompt parallel compute、初始 KV 与 TTFT 干扰 | L5 | 扫描 prompt length/chunk size/concurrency，测 TTFT 和 goodput | 11, 19, 22 |
| Ch44 `INFER-DECODE` | 严格时间依赖、访存、batch shape 与 TPOT | L5 | Profile Decode，区分 weight/KV bandwidth、launch 和 compute | 11, 19, 22 |
| Ch45 `INFER-KV-CACHE` | runtime cache 生命周期、reuse、eviction 与一致性 | L5 | Lab 03/10 验证容量、prefix reuse、corruption 和 eviction | 11, 22 |
| Ch46 `INFER-CONTINUOUS-BATCHING` | iteration membership、admission、fairness 与 preemption | L5 | static/continuous 对照并找到 throughput 与 tail/fairness 冲突 | 12, 22 |
| Ch47 `INFER-PAGED-ATTENTION` | logical blocks、physical placement、sharing 与 CoW | L5 | 测 block size、fragmentation、refcount/CoW 和 KV exhaustion | 12, 22 |
| Ch48 `INFER-SPECULATIVE-DECODING` | draft、target verification、commit 与 exactness | L5 | acceptance/rejection 均与 target-only 分布/状态对齐 | 12, 22 |
| Ch49 `INFER-TENSORRT-LLM` | kernel/fusion/quantization 到 execution plan | L6 | 追踪一个 engine build/hot path，完成 kernel/shape 性能诊断挑战 | 12, 19 |
| Ch50 `INFER-VLLM` | scheduler、KV manager、workers 与 engine state | L6 | 从 API 追踪请求并诊断未知 tail-latency/KV 场景 | 12, 22 |
| Ch51 `INFER-SGLANG` | prefix reuse、structured generation 与 program runtime | L5 | 对同一 workload 比较 prefix/structured path 与 plain generation | 13, 22 |
| Ch52 `INFER-DYNAMO` | 分布式 request/control/KV paths 与 placement | L5 | Lab 11 验证 state-aware routing、remote KV identity 和故障 | 13, 20, 22 |
| Ch53 `INFER-KSERVE-TOPOLOGY` | 声明式 LLM topology、EPP 与 worker groups | L4 | 追踪 CRD 到 Gateway/EPP/worker desired-state handoff | 13, 20 |
| Ch54 `INFER-GPU-MEMORY` | weights、KV、workspace、communication 与 reserve | L5 | 建立容量计算器并用实测峰值解释预算误差 | 13, 19, 22 |
| Ch55 `INFER-PD-DISAGGREGATION` | phase split、KV transfer、独立扩缩容与 break-even | L5 | 双进程模拟并推导 transfer/queue/SLO break-even | 13, 20, 22 |
| Ch56 `INFER-SCHEDULING` | phase、token progress、KV ownership 与 SLO 调度 | L5 | 比较 load/state/SLO-aware policy，注入 starvation 与 stale state | 13, 20, 22 |

## Part VI AI Infrastructure

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch57 `PLATFORM-FOUNDATIONS` | capability lifecycle、control/data/evidence planes | L3 | 为一个 Demo 写出平台化对象、owner、Gate 和 rollback | 14 |
| Ch58 `PLATFORM-KUBEFLOW` | 组合式 ML platform 与组件边界 | L3 | 画出当前本地 Kubeflow desired/observed state 和最小保留路径 | 14 |
| Ch59 `PLATFORM-MODEL-REGISTRY` | artifact identity、lineage、stage 与 release evidence | L4 | 从 dataset/checkpoint 追踪到 deployable revision 和 rollback | 14 |
| Ch60 `PLATFORM-TRAINING-OPERATOR` | 声明式训练 workload、rank lifecycle 与恢复 | L4 | 追踪 CRD reconcile、Pod/rank identity、failure 和 status | 14 |
| Ch61 `PLATFORM-KSERVE` | model service desired state、revision 与 rollout | L4 | 部署小模型并追踪 controller 到 endpoint/canary/rollback | 14 |
| Ch62 `PLATFORM-GATEWAY` | traffic policy、model routing、auth 与 data path | L4 | 验证 route、timeout/retry、identity 和 failure attribution | 14 |
| Ch63 `PLATFORM-GPU-SCHEDULER` | useful capacity、topology、queue、fairness 与 gang | L5 | Lab 12 测 starvation/preemption/locality，解释 GPU 利用率误导 | 15, 20 |
| Ch64 `PLATFORM-VOLCANO` | queue/gang/priority 的具体实现映射 | L4 | 绑定版本追踪一次调度 decision 和 unschedulable reason | 15, 20 |
| Ch65 `PLATFORM-KAI-SCHEDULER` | topology-aware scheduling 与实现边界 | L4 | 与 Volcano 在同一 workload/constraint 下做机制对照 | 15, 20 |
| Ch66 `PLATFORM-EVALUATION-SYSTEM` | EvalSpec、slice、judge、release Gate 与证据 | L5 | Lab 13 复现 aggregate 通过但 slice/security 不应发布 | 15, 21 |
| Ch67 `PLATFORM-MONITORING` | metrics、SLO、aggregation 与 detection boundary | L4 | 为训练/推理各定义信号、分位数、标签和不能证明的结论 | 15 |
| Ch68 `PLATFORM-LOGGING` | event identity、diagnostic context 与审计边界 | L4 | 设计结构化事件并从失败恢复链验证完整性 | 15 |
| Ch69 `PLATFORM-TRACE` | 跨 gateway/runtime/GPU/tool 的 causal path | L4 | 串联一次端到端 trace，定位缺失 span 和错误归因 | 16 |
| Ch70 `PLATFORM-COST` | workload、capacity、goodput 与单位经济性 | L4 | 用实测 workload 建立容量/成本模型和 sensitivity | 16 |
| Ch71 `PLATFORM-MULTI-TENANT` | identity、quota、isolation、fairness 与 noisy neighbor | L4 | 注入资源竞争并验证 quota、隔离和归因 | 16 |
| Ch72 `PLATFORM-SECURITY` | data/model/tool/supply-chain threat 与 authority | L5 | 完成 threat model，注入一条越权或污染路径并 fail closed | 16 |
| Ch73 `PLATFORM-PRODUCTION` | readiness、canary、rollback、incident 与 evidence loop | L5 | Lab 13 完成一次可追溯发布和故障回滚演练 | 16 |

## Part VII Agent

| Ch / Stable Node | 核心学习内容 | Target | 最低验收证据 | Week |
| --- | --- | ---: | --- | ---: |
| Ch74 `AGENT-PROMPT` | soft instruction、interface 与不可执行保证 | L3 | 构造 prompt variation，区分行为引导和 authority contract | 17 |
| Ch75 `AGENT-CONTEXT` | per-call working set、assembly、budget 与 provenance | L4 | 对相同任务比较 full/bounded context 和 evidence loss | 17 |
| Ch76 `AGENT-RAG` | retrieval、evidence identity、ranking 与生成边界 | L4 | 构造 stale/conflicting corpus，测 retrieval 和 answer attribution | 17 |
| Ch77 `AGENT-MEMORY` | persisted derived state、retention、supersession 与删除 | L4 | Lab 14 验证 stale/poisoned memory、delete 和 tenant scope | 17 |
| Ch78 `AGENT-TOOL-CALLING` | typed proposal、authorization、effect 与 receipt | L5 | 注入 timeout/duplicate response，证明 side effect 不重复提交 | 17 |
| Ch79 `AGENT-PLANNING` | proposal decomposition、search 与环境事实边界 | L4 | 比较静态/动态 plan，在 tool failure 下追踪 replan | 18 |
| Ch80 `AGENT-REFLECTION` | diagnosis、bounded retry 与 verifier 失效 | L4 | 复现 self-critique 改写正确答案或放大错误的反例 | 18 |
| Ch81 `AGENT-WORKFLOW` | durable transition、idempotency、commit 与 recovery | L5 | Lab 15 注入 lost response/retry，验证 workflow state | 18 |
| Ch82 `AGENT-MULTI-AGENT` | delegation、typed handoff、shared truth 与 coordination tax | L5 | 同一任务比较 single/multi-agent 的质量、成本和错误传播 | 18 |
| Ch83 `AGENT-MCP` | protocol、capability discovery、transport 与 security | L4 | 追踪一次 MCP request/response/error 和 trust boundary | 18 |
| Ch84 `AGENT-PLATFORM` | identity、policy、resource、evidence 与运行时编排 | L5 | 将 Lab 15 接入平台 Gate，完成 governed action design | 18, 23 |

## 四个 L6 Anchor

第一轮只要求四个主题达到 L6，避免“所有内容都深入”等于没有重点：

| Track | L6 Anchor | 必须串联的邻接节点 |
| --- | --- | --- |
| GPU / CUDA | Ch49 `INFER-TENSORRT-LLM` | Ch14、16～17、21、37、43～44、54 |
| Distributed AI | Ch36 `TRAIN-DISTRIBUTED-TRAINING` | Ch35、37～41、52、55～56、63～65 |
| RL Infrastructure | Ch33 `TRAIN-GRPO` | Ch27～32、34～35、66 |
| Inference Runtime | Ch50 `INFER-VLLM` | Ch19～22、42～49、51～56 |

L6 Challenge 不复述已做实验。Reviewer 必须给出一个未见过的 workload、故障或约束变化，要求在有限时间内完成：

```text
quantitative budget
→ competing hypotheses
→ signals and experiment
→ decision / fallback
→ residual risk
```
