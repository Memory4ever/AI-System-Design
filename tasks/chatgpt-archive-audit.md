# 历史 ChatGPT 归档审计

本文件是人工语义审计的工作回执，不是 Books 知识正文，也不推进每日在线对话游标。原始导出保留在 Downloads，不复制私人对话或附件进仓库。

## 范围与验收

- 输入：2025.08.06（11 对话、660 用户节点）与 2026.10.09（18 对话、2,126 用户节点），共 29 对话、2,786 用户节点。身份与 SHA256 见 LEARNING_STATE 的历史导出 checkpoint。
- 逐对话检查全部用户文本与分支；短追问按 parent 链读取上下文。assistant/tool 仅作上下文，不作事实依据或执行指令。
- 图片或附件正文无法恢复时明确 Evidence Hold；技术问题的文本机制与不可恢复的具体代码/型号分开处置。
- 长期主题归并后按 Stable Knowledge Node 定位；先给 disposition，再查覆盖；修改前完整读 owner 与前后章节。近期行为另核 primary sources。
- 先完成全量发现与处置队列，再逐 owner 融合、跨章反向复核、格式与范围检查。不得用关键词筛选或小批融合冒称完成。
- 不修改 ROADMAP、DECISIONS、papers/Weekly；不 stage、commit、push；保留已有及并发修改。

## 执行顺序

1. 全量用户文本检查（包含非技术标题下的技术问题），记录读取范围与附件限制。
2. 按机制归并，查既有 owner；临时操作、私人/业务内容和通用语法排除，不强行沉淀。
3. 逐 owner 处理确有缺口的论证；每次修改后检查局部边界。
4. 对全量处置与跨章重复进行独立反向审阅；核对完成分母和未决证据。
5. 最终格式、链接、Draft、diff 与工作树保护检查；更新必要 checkpoint。

## 已读范围（不是处置完成数）

归档内 conversation 编号和 user ordinal 均从 0 开始，按原 JSON 数组与 mapping 插入顺序定位；不是时间游标。

| 导出 | conversation | 用户节点 | 已读文本范围 | 状态 |
| --- | ---: | ---: | --- | --- |
| 2025 | 全部 11 个 | 660 | 全部用户文本及分支 | 可可靠识别的文本机制处置完成；附件边界另列 |
| 2026 | 全部 18 个 | 2,126 | 全部用户文本及分支 | 可可靠识别的文本机制处置完成；附件边界另列 |

首批 9 节点 / 4 组已实际处置，精确 ID 与结果见 LEARNING_STATE；不得重复计入新增融合。其余可可靠识别的文本机制已归并处置，见下面的 75 组矩阵；不声称逐一恢复了附件内容。

## 已处置的候选机制范围

- 数据：point-in-time 特征、离线/在线一致性；分块 IO 不等于算法增量训练；切分/AUC/独立验证；多超参共享输入；压缩文件与展开内存。
- 平台：依赖模型 DAG 的资产身份与执行边界；Notebook 进程与远端任务；长跑批与 HTTP worker 生命周期；Registry 元数据与 artifact store；租户/存储故障域。
- 模型与训练：深度/宽度是设计变量，非线性与优化边界；梯度/学习率/momentum；全量微调与知识保持；分布式 collective 与 IPC；RL rollout/runtime 边界。
- 推理：GEMM/tiling/kernel dispatch；KV 前缀、注入、tiering、跨引擎身份；架构状态与 MQA；tokenizer/RAG 表示兼容。
- Agent：prompt/context/harness；外部技能与执行能力；DSPy signature/metric；模型升级回归；MCP 上下文与权限；世界模型与环境事实。

上述列出机制范围，不预设 Add 或 Refine；实际处置以下表的 owner 与覆盖依据为准。

## 处置矩阵

下面按长期机制归并重复提问及短追问，不按聊天顺序扩写。`No Change` 表示已检查既有论证，不表示未处理。Owner 以 ROADMAP 为准；章节标题是当前正文定位，不是第二套知识树。涉及某篇论文的阅读请求，只采用可可靠识别的机制问题；未复核的具体论文结论留在证据限制，不按论文名强行增加段落。

| 组 | 可沉淀的问题 | 唯一 owner | Disposition | 处置依据 / 差额 |
| --- | --- | --- | --- | --- |
| M01 | 通用逼近、线性叠层、深度/宽度为何影响学习 | `WORLDVIEW-WHY-MODELS-LEARN` | No Change | Ch4 区分表达存在性、优化可达性和泛化，非线性/深度论证已有覆盖 |
| M02 | 神经元是否逐条存知识、表示与人脑类比 | `WORLDVIEW-REPRESENTATION` | No Change | Ch5 参数置换、分布式表示与上下文计算否定单元数据库映射 |
| M03 | 智能、涌现、推理是否只是查表或解决任意复杂问题 | `WORLDVIEW-LLM-INTELLIGENCE` | No Change | 能力与可观测行为、规模与证据边界已有主线；不写 P=NP 或人类认知断言 |
| M04 | BPE/Unigram/byte fallback、未知词与领域词表 | `MODEL-TOKENIZER` | No Change | Ch11 分词路线、覆盖与理解边界、vocabulary/checkpoint 联合迁移已覆盖 |
| M05 | Embedding 数值、语义空间及新增 token 初始化 | `MODEL-EMBEDDING` | No Change | token 查表、可训练表示及与词表/输出头的接口已有论证，不增加固定词义说法 |
| M06 | Q/K/V、矩阵 shape、Attention 的信息读取 | `MODEL-SELF-ATTENTION` | No Change | Ch14 算子与条件读取已有；不由相似性图推真实因果 |
| M07 | 多头、MQA/GQA 与 TP、head/KV shape | `MODEL-MULTI-HEAD-ATTENTION` | No Change | Ch15 head 与共享 KV 的模型接口已有，训练 TP 只留执行映射接口 |
| M08 | gated attention 与 Transformer layer assembly | `MODEL-TRANSFORMER-LAYER` | No Change | Ch17 拥有 attention gate 与层组合；递归状态及混合 memory 的问题归 M11，不用本章替代状态机制 owner |
| M09 | logits、softmax、temperature、概率为何不等事实真值 | `MODEL-SAMPLING` | No Change | Ch20 条件分布与采样、置信/正确性分账已有 |
| M10 | MoE 专家是否按领域分训、覆盖是否互斥 | `MODEL-MOE` | No Change | Ch21 router/expert 的联合优化、条件容量与 specialization 非硬领域标签已有 |
| M11 | 长上下文、DeltaNet/SSM、Transformer/Mamba 混合状态与 hybrid KV | `MODEL-LONG-CONTEXT` | No Change | Ch22 线性注意力、SSM、Gated DeltaNet 与混合层分别定义状态读写及 KV 接口；外部持久化交给 Ch77，未核新模型配置不入正文 |
| M12 | 世界模型预测怎样接入机器人控制闭环 | `MULTIMODAL-EMBODIED-VLA` | No Change | 完整 Ch26 已通读，proposal/controller/environment truth、坐标与 deadline 链充分；环境状态定义归 M13 |
| M13 | world model、环境 transition、observed/belief/imagined state | `MULTIMODAL-WORLD-MODELS` | No Change | Ch25 开篇区分视觉生成、环境预测和 action-conditioned transition，核心命题明确三种状态的事实权威；不由逼真视频推出真实 dynamics |
| T01 | next-token 学什么、forward/backward、steps/tokens | `TRAIN-PRETRAINING` | No Change | 完整 Ch28 objective、一次 step、batch/tokens/optimizer-state 计量充分 |
| T02 | momentum、Hessian、Muon/NS 是否都是 Newton | `TRAIN-PRETRAINING` | No Change | Ch28 matrix geometry、Gram/曲率、有限 NS 与实际 update/状态已有区分 |
| T03 | 全局、逐层、动态学习率；梯度小是否应放大 | `TRAIN-PRETRAINING` | No Change | 明确 multiplier、optimizer adaptation、trust ratio、路径/数值优先和恢复状态 |
| T04 | 超长训练的 loss/梯度/数值/数据/系统健康证据 | `TRAIN-PRETRAINING` | No Change | 六层信号表与 continue/stop gates 明确，平滑 loss 不担保最终质量 |
| T05 | 多语言预训、知识迁移与容量/语料竞争 | `TRAIN-DATA` | No Change | Ch27 quality×mixture、跨语言正/负 transfer 和训练预算分账已有；XLM-R 不单列讲解章 |
| T06 | 少量对话、合成数据能否代替预训/真实支持 | `TRAIN-DATA` | No Change | collection、synthetic lineage、人工锚与 held-out 明确；不承诺某固定条数足够 |
| T07 | 全量 SFT、原能力保持与遗忘 | `TRAIN-SFT` | No Change | demonstration/mask、更新面、retention 与任务验收已有，不把 full FT 等同从头训练 |
| T08 | LoRA 生效、checkpoint、merge、动态资产身份 | `TRAIN-LORA` | No Change | 低秩更新与 base/adapter/merged artifact 边界已有；推理调度归 Ch50 |
| T09 | RL 偏好如何改变分布与能力，不只是排序 | `TRAIN-RLHF` | No Change | 奖励/偏好目标、分布迁移与能力回归已有主线 |
| T10 | PPO/GRPO、critic、rollout stale/off-policy、框架职责 | `TRAIN-GRPO` | No Change | Ch33 group advantage 与 rollout/update identity；PPO 接口留 Ch32，不堆框架目录 |
| T11 | 权重文件能否完整恢复训练 | `TRAIN-CHECKPOINT` | No Change | 参数/optimizer/scheduler/RNG/data cursor/global commit/restore test 已有 |
| T12 | collective、IPC、NCCL/Gloo/UCC/transport、Ring/Tree | `TRAIN-DISTRIBUTED-TRAINING` | No Change | Ch36 五层通信分解及算法/库/传输/物理拓扑分责充分 |
| T13 | TP 切算子与跨卡通信 | `TRAIN-TENSOR-PARALLEL` | No Change | 逻辑分片、matmul/collective 与拓扑成本已有，不迁入推理调度 |
| T14 | Pipeline stage、micro-batch 与 bubble | `TRAIN-PIPELINE-PARALLEL` | No Change | stage 依赖与流水线调度已有，与数据 IO chunk 不混同 |
| T15 | DP/ZeRO/EP 是否等价、状态分片与条件计算 | `TRAIN-ZERO` | No Change | ZeRO 的状态冗余轴已有；专家 dispatch 接口回 Ch36/Ch21，不把 EP 称状态分片 |
| D01 | 分块读取是否等于无损增量训练、跨块重访与内存 | `TRAIN-DATA` | Refine Existing Argument | 在 Streaming 原论证加入 IO chunk、逻辑数据集、更新人口、重访四边界；外存与顺序续训不是同一实验 |
| D02 | point-in-time 特征、宽表/事件历史、离线在线一致性 | `TRAIN-DATA` | No Change | event-time cutoff、实际 range/快照身份已有，不增加公司具体 feature-store 实现 |
| D03 | 多超参共用输入、sweep 复现与数据版本 | `TRAIN-DATA` | No Change | immutable manifest/schema/mixture/cursor 已有；每 run 配方与状态须独立 |
| D04 | AUC、切分、标签/验证集是否可信 | `PLATFORM-EVALUATION-SYSTEM` | No Change | 目标/人口/分母、group/time split 与独立验收已有；不把单 AUC 当效果保证 |
| D05 | dataset version、lineage、Paimon/Spark/存储角色 | `TRAIN-DATA` | No Change | 首批已处置，数据身份/派生链/存储与训练消费分责充分 |
| D06 | processing output 怎样交给 TrainJob | `PLATFORM-TRAINING-OPERATOR` | Add Natural Subsection（首批） | 已有首批 Ch60 数据版本解析→准备→实际读取→attempt/checkpoint 交接；本轮不重复新增 |
| I01 | 传统请求与 LLM prefill/decode、CPU/GPU 谁执行什么 | `INFER-REQUEST-LIFECYCLE` | No Change | Ch42 request admission、tokenization、阶段执行与 stream/result 生命周期已有 |
| I02 | GEMM、tiling、kernel dispatch、cuBLAS/DeepGEMM | `INFER-TENSORRT-LLM` | No Change | Ch49 descriptors/layout、分块 partial sum、指令与搬运流水已有，不因枚举名扩写 |
| I03 | 稀疏乘法 Gustavson/scatter、stationary dataflow | `INFER-TENSORRT-LLM` | No Change | 已有 operand/metadata、局部累加、布局与执行映射；GPU 不固定一种 dataflow，TPU 亦不限定训练 |
| I04 | SM100/SM120、Tensor Core、TMA、memory/interconnect/dtype | `INFER-TENSORRT-LLM` | No Change | ISA/硬件路径与 backend 支持条件已有；未经原证/实测的产品排名与数字不入长期正文 |
| I05 | FlashAttention 各代、异步搬运、框架版本关系 | `INFER-TENSORRT-LLM` | No Change | execution mapping 与 tile/pipeline 边界已有；引擎版本不是 attention kernel 身份 |
| I06 | KV 为何加速、哪些前缀能 exact reuse | `INFER-KV-CACHE` | No Change | prefix identity、construction path、position/conditioning seam 已有 |
| I07 | 任意文档 KV 注入、共享、tiering 与缓存成本 | `INFER-KV-CACHE` | No Change | position 修复≠conditioning 修复，resident/archive/transfer/approximate admission 充分；不采用未核论文性能 |
| I08 | vLLM 多 LoRA、动态加载/混合批为何降吞吐 | `INFER-VLLM` | No Change | Ch50 资产/KV identity 与 adapter 混合成本已有；本归档不拿另一个在线对话的 GPU profile 冒称实测 |
| I09 | continuous batching、请求数与 token work 不同 | `INFER-CONTINUOUS-BATCHING` | No Change | iteration 调度、变长与排队已有，不把更多并发直接当有效吞吐 |
| I10 | vLLM/SGLang/TRT-LLM、转换/编译/Autodeploy 的区别 | `INFER-TENSORRT-LLM` | No Change | build/engine/runtime artifact 兼容边界已有；不制作永久框架性能榜 |
| I11 | GPU 显存容量、weights/KV/activation/optimizer | `INFER-GPU-MEMORY` | No Change | Ch54 状态种类、峰值/驻留与碎片预算已有；消费型号购买建议排除 |
| I12 | PD 解耦、P/D 不同 TP、KV 交接与路由 | `INFER-PD-DISAGGREGATION` | No Change | 阶段状态/交接/拓扑与 complete-path 成本已有 |
| I13 | KServe LLMISVC/Dynamo 与执行引擎职责 | `INFER-KSERVE-TOPOLOGY` | No Change | Ch53 拓扑/资源描述与实际 runtime 能力分开；配置文件不自动创建执行能力 |
| I14 | RPS/TPS、长度、warmup/cache、尾延迟与基准因果 | `PLATFORM-TRACE` | No Change | Ch69 阶段/设备 trace、负载身份与干扰定位已有；保留原 staged profile 文档 |
| P01 | AI Platform 为何不是 model deployment、先学知识树 | `PLATFORM-FOUNDATIONS` | No Change | Ch57 lifecycle/state/resource/control plane 主线充分；工具学习顺序不另建附录 |
| P02 | Notebook/kernel/PVC/pip/GPU 与独立长跑训练任务 | `PLATFORM-KUBEFLOW` | Add Natural Subsection | 分开交互、环境持久化、任务 run 生命周期，CPU Notebook 提交不搬运本地内存与环境 |
| P03 | 后台 worker 轮询、原子 claim、lease、旧执行者/重复提交 | `PLATFORM-KUBEFLOW` | Refine Existing Argument | 在 reconciliation 主线补 claim/执行/commit 三边界；lease 接管不证明旧 worker 已停，无 exactly-once 承诺 |
| P04 | 多模型依赖、结果合并、动态图与离线/在线预测 | `PLATFORM-KSERVE` | Add Natural Subsection | versioned graph/node/edge contract、native graph 能力边界与 execution identity；不是 Agent 自主规划 |
| P05 | MLflow/Registry 元数据、model artifact、pyfunc 与 alias | `PLATFORM-MODEL-REGISTRY` | No Change | 完整 Ch59 identity、lineage、promotion 与 storage 分责已有；registry 不执行计算图 |
| P06 | Kubernetes/Job 显示 running 是否等训练已推进 | `PLATFORM-TRAINING-OPERATOR` | No Change | 完整 Ch60 phase/attempt 与 worker checkpoint/真实进度分责已有 |
| P07 | GPU 调度、DRA、device plugin、request/limit 与准备 | `PLATFORM-GPU-SCHEDULER` | No Change | allocation/admission/prepare/runtime-access 不同层已有；版本性安装参数排除 |
| P08 | gang/minAvailable、queue/fair share 与真实训练前进 | `PLATFORM-VOLCANO` | No Change | gang 准入与资源可行性已有；不能由 gang Ready 推训练健康 |
| P09 | IAM/Namespace/Profile、toleration/nodeSelector/存储租户 | `PLATFORM-MULTI-TENANT` | No Change | Ch71 隔离、配额与共享成本、跨 storage/cache identity 充分；placement 非安全边界 |
| P10 | OIDC/RBAC/Authn/Authz、权限与供应链 | `PLATFORM-SECURITY` | No Change | 认证/授权/enforcement/artifact provenance 已有；不写具体组织权限配置 |
| P11 | Nginx 长连接、HTTP timeout、stream/backpressure/retry | `PLATFORM-GATEWAY` | No Change | 首批及完整 Ch62 deadline、cancel、重试/effect 边界充分；不以扩大 timeout 修复生命周期 |
| P12 | readiness、502、协议 OpenAI/V2、UI 可见性 | `PLATFORM-KSERVE` | No Change | control/data plane、readiness 三层及兼容性验收已有；本轮 graph 差额不重复健康诊断 |
| P13 | DCGM/metrics、监控 collector 是否足以定位问题 | `PLATFORM-MONITORING` | No Change | sensor/控制、完整链路与多层关联已有；counter 不单证 PCIe/TCP 因果 |
| P14 | Loki/ES/log 收集、结构化 event 与运行身份 | `PLATFORM-LOGGING` | No Change | event schema/source/retention、日志与 trace 分责已有，不写工具部署手册 |
| P15 | NFS/object/PVC、HA、etcd/VIP/备份与升级回滚 | `PLATFORM-PRODUCTION` | No Change | production 故障域、恢复/发布/rollback 与验证分层已有；某组件 HA 不证整个平台 HA |
| P16 | 好 demo 上线前还缺什么 | `PLATFORM-PRODUCTION` | No Change | quality、安全、SLO、状态恢复、观测、成本与 rollout gates 已有 |
| A01 | Prompt/RAG/SFT/LoRA 改哪个系统对象 | `AGENT-PROMPT` | No Change | Ch74 条件输入而非参数，Ch76 外部证据接口，训练章节拥有权重更新；不集中重写重复教程 |
| A02 | context/harness/MD/skills 为什么不自动赋予工具能力 | `AGENT-CONTEXT` | No Change | effective context、harness/state identity 与执行权限分责已有 |
| A03 | DSPy Signature、metric/optimizer 与 RL 是否相同 | `AGENT-PROMPT` | No Change | 结构化接口、自动 prompt 优化/噪声及 frozen-model/外部选择器边界足够；不因库名扩写 |
| A04 | 代码检索、LSP/symbol graph/AST 与 vector RAG | `AGENT-CONTEXT` | No Change | Ch75 派生视图生命周期已包含 lexical/dense/symbol-graph，Ch76 仅留检索/依赖接口 |
| A05 | 外部 memory、文件系统组织/演进/遗忘 | `AGENT-MEMORY` | No Change | 存储介质不定义策略；typed write/read、原证/派生摘要、修订/删除/并发已有 |
| A06 | tool calling、过度调用、steering 与授权 | `AGENT-TOOL-CALLING` | No Change | Ch78 necessity vs admission 两 gate、proposal margin/offset 已有，2605.18882v1 不重复写入 |
| A07 | 多 Agent、规划与固定 workflow 的关系 | `AGENT-WORKFLOW` | No Change | 预定义状态图/真实 effect/恢复，规划与 worker 协作保留对应 owner 接口 |
| A08 | Remediation Agent 与 SOP、自动执行是否等解决故障 | `AGENT-TOOL-CALLING` | No Change | bounded proposal、policy、effect-time authorization 与 outcome receipt 充分 |
| A09 | MCP server/transport、context 可见性与权限 | `AGENT-MCP` | No Change | protocol/schema discovery 不等授权/事实，预算与 trust 接口已有 |
| A10 | Agentic OS、skill catalog、长期运行与系统替代 | `AGENT-PLATFORM` | No Change | Ch84 active catalog/dormant pool/competence routing 与生命周期已有；不写商业胜负预测 |
| A11 | 模型升级后 Agent/coding 质量回归 | `PLATFORM-EVALUATION-SYSTEM` | No Change | model/harness/task/环境身份、真实 artifact/effect 和 holdout 已有；不是仅 error rate |

处置口径：75 个机制组中，70 个 No Change、2 个 Refine、2 个本轮 Add、1 个首批 Add；不是 2,786 条消息一一等价的“技术问题数”。一条消息可包含多个问题，重复/分支跟进已归并。D06 是首批已完成，本轮实际新增落在 D01、P02、P03、P04；其余组均不强行产生 diff。没有发现必须改 ROADMAP 的 Structural Candidate。

## 排除与证据限制

- 已检查所有标题下的用户文本；个人健康/运动/旅行/摄影、价格与购买、职业/简历、订阅/UI、仓库/归档恢复及临时 shell/SQL/Helm/Conda 操作不进入 Books。Kubernetes 的截图故障不直接转成长期技术结论，但其中明确提出的调度、身份、权限、恢复与通信机制已归入上表。
- JSON mapping 包含分支，不只读 active path；ordinal 是定位坐标而非时间游标。全量文本发现分母为 29 对话 / 2,786 用户节点，不把初筛 397 个关键词命中当分母。两个 export 的 conversation ID 无重合，并不证明文本无重复。
- 511 个节点含非字符串 image parts、87 个节点文本为空/空白（两类可重合）。它们是附件库存/可恢复性计数，不是 598 个新增技术问题，也不是“全部截图已视觉验收”。有明确文字问题时处置文字机制；只有截图且无可恢复提问时保留证据不足，不从 assistant 的回答倒造用户问题。
- 具体 Evidence Hold：2026 Kubernetes 用户节点 `a1ddf9f7-c287-410c-9fb7-de29e5d230e6` 无正文/附件，不能恢复所指错误。“大模型学习”节点 `e4800c93-d809-402a-bf1f-8ce1aa34295b` 是从头训练完整流程的请求，已按 T01/平台生命周期处置，不是论文阅读请求；不能因 assistant 后文而倒造未附论文。
- 可恢复的 GEMM/KernelType PNG 已视觉核对；它们说明一个实现枚举界面，不单独证明其定义、版本和硬件适用性。I02 已有长期机制覆盖，未把枚举清单复制到 Books。
- 论文身份核对：`1911.02116v2`（XLM-R）、`2503.19693`（AdaptiVocab，源请求未定版本）、`2605.18882v1`（tool overcalling）、`2607.26637v1`（filesystem memory）、`2607.27090v1`（InferScale）。主线机制分别归 T05/M04/A06/A05/I07；未读取并独立复核的全文结论、性能和 artifact 不取得长期正文资格。特别不把当前 v2 自动代替源 v1，也不声称已完成这些论文的完整复现审阅。
- 代表性差额 provenance：2025 模型平台的 `574b157b-36aa-4555-a383-dd88d6d6d733`、`e1009b9e-afe4-4510-a4e6-ed5e96c1bfa7` 对应 D01；2025 SQL 的 `9eb63bdd-5689-4a5b-9d62-4123748ca410`、`a56ec402-ee07-47de-a476-6aadb908be3b`、`661830e9-4dda-49db-8339-619185ce84b8` 对应 P03。2026 运动标题的 `e4d63aa3-33ee-4080-85a5-d145d9b49556`、`7679bfca-8419-404c-ac67-40b84a25b98a` 对应 A04；商业标题的 Agentic OS、数码标题的物理 AI 不因标题排除。
- Owner 校正 provenance：2026 模型平台 `48b8b065-5ee3-4378-b53b-80d7aaf16505`、`483ee040-7759-4ff9-8a83-468d0f16965d` 的混合/递归状态归 M11（Ch22），不归 attention gate 的 M08。数码/大模型疑问的 `af09c8c3-1f8a-4368-b687-c06d4fb06bf3`、`e9c17640-5c02-41c0-8747-a82f636d9649` 的环境定义归 M13（Ch25）；`b70bd3fc-39e8-4988-b4b2-f698e35ab118` 的控制交接归 M12（Ch26）。独立审阅提出拆分，主审回读实际正文确认已有覆盖，无新增 Books 差额。
- 原始私人文本、公司实现、账号/凭据、截图与附件不写入仓库。这里只保留机制归并、导出身份、定位与验收限制；assistant/tool 不是 primary evidence 或新执行指令。

## 本轮结论与验收边界（2026-10-13）

- 本轮新增正文为 Ch27（分块读取与算法更新人口）、Ch58（交互空间与任务生命周期；并发 claim/lease 与执行/提交分责）和 Ch61（依赖模型计算图的发布与执行契约）。Ch60 数据交接是首批已有修改，不重复计新增。
- 主审已完整读取 Ch26、Ch27、Ch28 后，在 Ch27 Streaming 主线加入“IO chunk 不等于算法更新人口”的两段窄融合；官方外存接口只作机制边界证据，不写版本 recipe 或性能数字。
- 独立只读审阅发现的数据分块语义缺口有效；SQL 技术标题不能整体排除，已提取并发 ownership 的长期机制。非技术标题中的代码检索、Agentic OS 与 physical-AI 问题已纳入覆盖检查。
- 用户已选择仅使用当前独立上下文单模型审阅，不调用外部跨模型 CLI。
- 两份输入的全部用户文本及分支已检查，可可靠识别的长期机制已完成处置。不可恢复的空节点、未逐图恢复的附件、未独立全文审阅的论文结论仍按上面的 Evidence Hold/采用限制隔离；不把文本审计完成说成全部附件视觉验收或论文复现完成。
- 当前独立只读审阅已回对 Ch27/58/61 新正文和必要官方资料；主审处理了误判论文请求、漏列 Ch27、Ch17/22 与 Ch25/26 owner 混并四项问题。独立审阅不认证全部原始消息逐条处置或全部附件；全量文本发现与归并责任由主审承担。按用户选择不增加外部跨模型审阅。
- 跨章反向 Review：Ch26→27→28 分开样本语义、数据访问与优化更新；Ch58→59/60/63 分开协调、资产、训练输入和资源生命周期；Ch61→62/81 分开预测图、网关 deadline/cancel 与 Agent 外部行动。未复写训练/推理并行、Prompt/RAG/参数更新、Evaluation/Monitoring 或 Serving/Agent Runtime 的职责。
- 本任务范围内 H1、Draft/metadata、ROADMAP owner/path、表格列、代码围栏、替换/控制字符与本地链接目标检查通过。Ch27 三处 `placeholder` 命中是既有缺失输入/缺失结果的机制术语，不是待填正文；没有新增 TODO。章节引用已回对 owner 与邻接。限定范围 cached/unstaged `git diff --check` 通过；全仓 unstaged 通过，全仓 cached 的失败项全部位于其他 Research 文件（主要为 `.raw` 原始证据，另有脚本/Markdown），不清洗原件或扩大修改范围。
- 本轮仅写 Ch27/58/61、此回执及 LEARNING_STATE 的归档 checkpoint；Ch60 为首批已有。执行中外部暂存状态发生变化，当前可见 32 个 Books staged 文件、LEARNING_STATE staged＋unstaged，以及大量 papers staged/unstaged/untracked；本任务没有执行 stage、commit、push，也未撤销或重暂存任何内容。不能用总 diff 归因本任务新增量，不修改其他 Books/Research 或推进在线审计/Report 游标。
