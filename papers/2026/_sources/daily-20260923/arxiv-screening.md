# 2026-09-23 Daily：arXiv 来源筛选续跑记录

本文件只记录 `SRC-ARXIV` 的原始入口、日期归属与实际筛选；不是日报或 Books 审阅的替代品。独立审计发现原先的 605 个“仅标题级关闭”缺少可复算的逐项身份与理由，且未列账标题中确有应读摘要的歧义项，因此本来源重新标为**未完成**，详见末节；此前 `已检查（范围受限）` 不再有效。报告窗口为 2026-09-22T09:00:00+08:00 ～ 2026-09-23T09:00:00+08:00。

## 官方批次与日期口径

已取得 `cs.CL`、`cs.LG`、`cs.DC`、`cs.AI`、`cs.CV`、`cs.RO`、`cs.AR`、`cs.PL`、`cs.OS`、`cs.PF`、`cs.IR`、`cs.MA` 的官方 `/list/<category>/new` HTML，12 页页头均为 `Showing new listings for Tuesday, 22 September 2026`。入口示例：[cs.CL](https://arxiv.org/list/cs.CL/new)、[cs.LG](https://arxiv.org/list/cs.LG/new)、[cs.DC](https://arxiv.org/list/cs.DC/new)；其余分类替换路径中的代码即可。快照取于 2026-09-23 09:06～09:08 北京时间；它们是宽入口，不是本项目的候选清单。

解析每页 `New submissions`、`Cross submissions`、`Replacement submissions` 的 `/abs/<ID>`，按 arXiv ID 跨分类去重，得到 1,746 个唯一身份：1,003 个出现在 `New submissions`，183 个只在 `Cross submissions`，560 个只在 `Replacement submissions`。分类内/跨分类重复不另计；不能把 1,746 当作“本窗新论文”，也不能将 560 个 replacement 默认为重大修订。可复核的原始 12 页下载快照暂存在运行机 `/private/tmp/arxiv-20260923-cs.*.html`，解析中间文件为 `/private/tmp/arxiv-20260923.json`；这些临时文件不是仓库报告或永久证据。

据 arXiv 官方[Availability of submissions](https://info.arxiv.org/help/availability.html) 的 Announcement Schedule，Tuesday 的公告于 20:00 US Eastern 发出。2026-09-22 适用 EDT（UTC−04:00），对应本窗内的 2026-09-23T08:00:00+08:00。该页还明确 ID 在首次公告时分配，不能按作者提交时间倒推首次公开。例：[TreeSpark](https://arxiv.org/abs/2609.22098) 的 `v1` 提交字段为 2026-08-12，而其 ID 出现在本批 New 列表；这两种日期字段必须并列保留，不把 `Submitted` 冒充首次公开，也不因提交早而机械排除本次官方公告。若作者项目页等能证明正文更早已公开，须再去重到真正首次公开事件。本页目前只确认公告批次归属，尚未对全部可能入选项完成跨渠道首发及撤回核验。

## 实际主题检索与停止位置

在去重列表上按 ROADMAP 的模型、Training、Inference、Platform、Agent 与多模态/World Model 主线作**标题主题检索**，使用 `LLM / language model / foundation model / Transformer / MoE / speculative / KV cache / GPU / quantization / VLA / world model / Agent / RAG / inference / pretraining / distillation / RLHF / GRPO / attention / memory / evaluation` 等词及变体；正则仅生成阅读队列，不决定是否入选。1,003 个 New 中 373 个标题命中，183 个仅 Cross 中 46 个命中，560 个仅 Replacement 中 193 个命中。宽入口已遍历，但标题主题查询及其反向补检**尚未完成语义闭合**：未命中的标题仍需有界浏览以识别新命名机制，replacement 需只检查与机制、评价、纠错或安全有关的实际修订信号，不能把此处数字解释成贡献候选。

`cs.DC / cs.AR / cs.OS / cs.PF` 的 60 个唯一 New/Cross 标题已浏览，其中 50 个 New 的 32 个读完摘要；`cs.CL / cs.LG` 训练/推理主题的 93 个 New 标题已浏览，其中 65 个读完摘要。Agent/Evaluation、World Model/VLA、Information-State、Model/Multimodal/Execution、机制主题和五轮漏收抽检随后补读，明细与去重在下文。又按 arXiv ID 顺序对账本当时未出现的 646 个 New 标题作题目级浏览，选择其中 41 个边界歧义者读完摘要；第三轮反向抽核补读 8 个、实时多模态邻域补读 16 个、第四轮反向抽核再补读 8 个、第五轮反向抽核补读 4 个，随后对标题未记载但摘要命中大模型系统主题的边界项补读 6 个。跨批次去重后，本来源子任务读完 363 个标题与摘要；报告 owner 又独立读完 20 个仅标题级分层样本，本任务对个人身份邻域补读 4 个此前未读身份，并在末节新补读 13 个。合计实际读完 **400 个唯一标题与摘要（398 个 New、2 个仅 Cross）**；其余 **605 个 New** 仅到标题级范围筛选，不冒充摘要审阅或全文审阅。1,003 个 New 的题目均已浏览，标题级关闭有界独立抽核详见末节；不能把 1,746 个宽入口身份当作本窗新论文。摘要中的性能数字仍为作者主张。以下“拟进入”仅是项目贡献初判，末节后续裁决优先适用；不能据此宣布 `SRC-ARXIV` 已完成。

### 拟进入贡献候选的题摘：优先复核

这些材料的可取之处是能指出要重新核验的具体旧判断，不是因为名称或关键词碰巧匹配章节。

| arXiv 原始材料 | 题摘显示的具体增量；待核问题 |
| --- | --- |
| [2609.22101 Context Poisoning](https://arxiv.org/abs/2609.22101) | 长上下文“更长即可利用更多证据”受有效干扰项数与分数别名化约束；需核理论假设、hard-negative 对照与检索门控的召回代价。 |
| [2609.22109 Selective On-Policy Distillation](https://arxiv.org/abs/2609.22109) | 选择器在共享学习率下的优劣可能是 selector×rate 交互而非选择器本身；需核注册实验、样本/seed、LoRA 与 full-tune 的适用边界。 |
| [2609.22157 PAGE](https://arxiv.org/abs/2609.22157) | 固定 KV eviction 会在一类输入上灾难性失效；作者提出逐输入 admission gate，同时牺牲实际压缩比；需核真实批量内存收益和对照。 |
| [2609.22183 CleanScore](https://arxiv.org/abs/2609.22183) | 对 benchmark 污染的表面改写审计，null 结果不能排除泛化的泄漏效应；需核 negative controls、暴露干预和置信区间。 |
| [2609.22231 EvalMem](https://arxiv.org/abs/2609.22231) | Agent memory 的末端 QA 分数混淆 encoding/retrieval/generation 责任；拟用操作级诊断分层，需要核 oracle evidence、归因条件。 |
| [2609.22512 LLM Judge Error Dependence](https://arxiv.org/abs/2609.22512) | 多 judge 一致不等于独立证据；若错误相关，显著性与有效样本量会改变。需核同一题目配对、相关估计与投票外推。 |
| [2609.22755 NSP](https://arxiv.org/abs/2609.22755) | 长尾序列长度使固定 SP 度在负载平衡与通信间冲突；嵌套 SP group 让长短序列共享 GPU，需核调度/重计算开销与多硬件结果。 |
| [2609.22870 FP8 RL](https://arxiv.org/abs/2609.22870) | FP8 噪声通过 importance-ratio/clipping 可能使负优势 token 无梯度，形成熵激增；需核 BF16 对照、各模型与算法重复结果。 |
| [2609.23252 Robot World-Model Action Encoding](https://arxiv.org/abs/2609.23252) | action-conditioned dynamics 可能不具备对信息等价的绝对/相对动作编码的不变性；需核动作重参数化干预、真实任务与修复边界。 |
| [2609.23536 QEffect](https://arxiv.org/abs/2609.23536) | CUDA Graph 捕获的地址稳定性不保证 FP8 scaling 与 split-backward 资源世代正确；提出状态/资源契约，需核实现与 bitwise parity。 |
| [2609.23816 SPLASH](https://arxiv.org/abs/2609.23816) | HBM 容量与次级层带宽的旧取舍在高带宽闪存下可能改变；KV placement 与稀疏读取必须按页/并行平面共设计，需核硬件是否实测或模拟及 SLO。 |
| [2609.24122 Re:CAP](https://arxiv.org/abs/2609.24122) | 无穷尽标注时生产 RAG 检索 coverage 难测，作者用缺失证据探测审计；需核检索预算、judge/human 校验与生产迁移。 |
| [2609.24130 Self-Healing Harness](https://arxiv.org/abs/2609.24130) | Agent 自改规则的局部收益会破坏既有任务；外部 admission gate 决定持久化授权，需核 matched replay、非回归阈值与执行隔离。 |
| [2609.24456 Conduit](https://arxiv.org/abs/2609.24456) | 分布式 RL 中 experience buffer 不仅是队列，placement/delivery/scheduling 成独立数据面；需核是否可推广到 LLM RL 工作负载与端到端收益。 |
| [2609.24639 PD Power Provisioning](https://arxiv.org/abs/2609.24639) | PD 分离的实例数/功率不能独立优化；作者把长度分布、KV 预留、排队与 power-cap 连成解析模型，需核模型适配条件。 |
| [2609.24663 EvoPathBench](https://arxiv.org/abs/2609.24663) | 只看 agent 自进化终点成绩可能掩盖中途能力遗忘；需核冻结 artifact 的评估协议与跨场景限制。 |
| [2609.24749 D-JEPA](https://arxiv.org/abs/2609.24749) | world model 的预测相似不保证可执行动作选择；用实际结果训练 decision-local latent 关系，需核受控预测-决策分离与真实机器人证据。 |
| [2609.22674 M-JEPA](https://arxiv.org/abs/2609.22674) | 多 mask JEPA 的重复 target/context 执行与 token routing 形成训练浪费；不改学习目标而改变执行复用/稀疏处理，需核五种变体的语义等价与端到端收益。 |
| [2609.22991 PyTorch MPS Large Tensor](https://arxiv.org/abs/2609.22991) | 可能存在 2^32 元素边界下无异常的矩阵乘错误，直接影响模型执行正确性；需核精确 macOS/PyTorch、dtype/布局、公开复现与 CUDA 对照，不把单机观察泛化。 |
| [2609.23278 MoSim](https://arxiv.org/abs/2609.23278) | 分布式训练集群模拟若固定网络惩罚，会错估 placement 的 NIC 争用及 JCT；需核 trace、模拟器对照与跨拓扑外推。 |
| [2609.23301 TempoTrace](https://arxiv.org/abs/2609.23301) | AI 集群 trace 的时钟误差可反转因果事件；作者提出 PTP/GPU 时间戳与逻辑时钟，需严格区分五节点实测、仿真大集群及设计目标。 |
| [2609.24161 MCP-GRANITE](https://arxiv.org/abs/2609.24161) | MCP 工具粒度可能改变本地模型的选择与参数正确率，不能只比较模型大小；需核受控四种接口、任务定义与跨场景迁移。 |
| [2609.24991 KV Cost Attribution](https://arxiv.org/abs/2609.24991) | K8s、gateway 与 provider 多账本可能漏归属/双计，KV/shared serving 的计费归属不是 token 计数即真值；需核真实 H100 部分与合成账单部分的边界。 |

上述 23 项的 arXiv 官方公告批次时间依据相同，均暂记 `2026-09-23T08:00:00+08:00`（公告事件，不是提交时刻）。其论文正文可能已有更早公开渠道；该可能性、撤回及精确版本尚未逐项排查，不能先写进日报确定候选表。已抽查其中 MPS 错误、MoSim、TempoTrace、M-JEPA、MCP-GRANITE 与 KV Cost Attribution 的官方 abs，页面当前显示 `v1` 且未在本次页面文本中见撤回声明；这不是对后续状态或所有项的撤回保证。`2609.24205` 的 abs 抽查暂未返回可读取文本，仍待核。

**更早公开的归属纠正：**[2609.22220](https://arxiv.org/abs/2609.22220) 虽在本次 arXiv `New` 公告批次，作者[官网 News](https://mingzhe.space/news/) 明确记载 2026-09-12 已发布该论文并链接到 Hugging Face papers 页面。因此 09-23 的 arXiv 公告不是已知最早公开事件；它仅作为旧日期 owner 的 spillback/身份恢复线索，不进入本日报候选分母或评分。是否有更早公开版本及具体旧 owner 日仍待核。

**同家族去重纠正：**[2609.22978 DSec](https://arxiv.org/abs/2609.22978) 的主要机制已见于 DeepSeek 官方 [2026-04-24 V4 公告](https://deepseek.com/en/news/v4-preview/)所链接的 [V4 技术报告 §5.2.5](https://arxiv.org/html/2606.19348v1)：四类执行底座、3FS 分层镜像、CPU/内存高密度，以及与可抢占训练协调的 trajectory log。09-23 的系统论文可能补充实现细节或规模证据，但不能将这些机制当作本窗首发；仅按旧 Source Family 的后续证据对照，若无实际改变设计/评价边界则候选前关闭，不能重复计分。

### 已读题摘但准入仍未裁决

下列已读题摘涉及本项目，但尚需比较是否只是局部 operating point、成熟原则的重述或有可保留的独立边界，不因审阅工时而机械排除：`2609.22098`（draft tree 与负载预算）、`2609.22100`（RAG soft-memory 配额）、`2609.22106`（量化 residual 布局）、`2609.22114`（多轮 coding agent 压缩成本）、`2609.22156`（MoE speculation 边界）、`2609.22158`（step-level KV）、`2609.22335`（VLA GPU kernel 并发）、`2609.22471`（MoE expert coactivation）、`2609.22884`（稀疏注意力路由）、`2609.22888`（真实机器人在线 VLA 后训练）、`2609.23033`（looped LM wavefront decoding）、`2609.23085`（能耗感知模型路由）、`2609.23130`（vLLM/llm-d 综述，可能已有覆盖）、`2609.23314`（sink-suppressed KV eviction）、`2609.23790`（多 Agent memory 成本）、`2609.24089`（attention double-backward）、`2609.24150`（接受率目标的 draft 训练）、`2609.24197`（无 drafter KV 的并行 speculation）、`2609.24270`（GPU die 不对称调度）、`2609.24298`（KV bit-rank 分配）、`2609.24635`（operation token 的 KV 表示）。仅 `Cross submissions` 的 `2609.22547`（RLVR pass@k 统计）与 `2609.23570`（coding-agent memory benchmark）另作真实首发日恢复线索，不因 09-22 跨列而计本窗新论文。

第二批同属尚待裁决：`2609.23321` 是基于阿里巴巴生产 diffusion 服务日志的 LoRA adapter 共现观察，需要核清可否改变大模型 adapter preload/placement 判断；`2609.24205` 是训练阶段按瓶颈调 GPU 频率，需核是否仅重述成熟 DVFS 原则及 abs 可访问性；`2609.24847` 是 FPGA 上按 speculative decode 阶段重构 GEMV/GEMM tile，需核其长期执行规划贡献是否超出专用硬件局部 operating point。

### 已读题摘且明确候选前关闭

| arXiv 原始材料 | 关闭理由 |
| --- | --- |
| [2609.22110](https://arxiv.org/abs/2609.22110) | 尼日利亚母婴/疫苗健康问答的领域 LoRA 效果与安全比较；未分离出大模型训练新机制或跨域评价合同，属医疗场景效果。 |
| [2609.22113](https://arxiv.org/abs/2609.22113) | 阿片治疗留存预测的群体公平性研究，核心模型并非大模型及 Infra；领域公平性不因通用词汇入选。 |
| [2609.22164](https://arxiv.org/abs/2609.22164) | 结构化 EHR 合成临床笔记的多 Agent 生成-审核-重写组合，摘要仅示临床任务改善，未给本项目新的 Agent 审核机制或通用失效边界。 |
| [2609.22196](https://arxiv.org/abs/2609.22196) | 电商 learning-to-rank pipeline 搜索；虽有 fitness-noise/headroom 观察，当前证据只针对该搜索空间，未确立大模型/Agent 系统主线的设计变化。可在独立复核时抽样复看这一边界项。 |
| [2609.22232](https://arxiv.org/abs/2609.22232) | 肾替代治疗的健康分数与离线 RL 策略；主张是临床目标及策略结果，不是大模型训练/部署机制。 |
| [2609.22379](https://arxiv.org/abs/2609.22379) | 火星遥感影像的局部自监督预训练和检索，未给多模态基础模型通用表示/系统新约束；AI for Science 当前暂缓。 |
| [2609.22836](https://arxiv.org/abs/2609.22836) | 不规则多变量时序预测 foundation model，研究目标为时序 forecasting；未显示当前大模型主线表示或平台约束的可迁移设计边界。 |
| [2609.22917](https://arxiv.org/abs/2609.22917) | 芝加哥犯罪数据库的 LangGraph Text-to-SQL 单场景实现和两版 prompt 对比，作者也未给外部基线；没有新增可长期保留的 Agent 状态/控制机制。 |
| [2609.24294](https://arxiv.org/abs/2609.24294) | 气候模型 SHT 的通信压缩，即使涉及 GPU/collectives，目标不是大模型训练或推理；AI for Science 当前暂缓。 |
| [2609.24559](https://arxiv.org/abs/2609.24559) | 时序 forecasting 模型发布与领域 benchmark，不能因名称为 foundation model 就自动纳入大模型系统主线。 |
| [2609.22142](https://arxiv.org/abs/2609.22142) | 通用 K8s score plugin 的 pointwise-vs-ranking 目标不匹配；该差异是既有 Learning-to-Rank 原理，此摘要未给大模型资源调度的新机制/边界。 |
| [2609.22636](https://arxiv.org/abs/2609.22636) | 用 LLM agent 搜索软件 prefetch 配置，核心贡献在一般 CPU 工作负载的编译/性能调优，不是大模型训练或推理 runtime 机制。 |
| [2609.22753](https://arxiv.org/abs/2609.22753) | OCR edge service 以专用决策模型替换通用 LLM 的单一服务实证，重复“简单任务可用小模型/规则”原则，且缓存后延迟差异消失；未改本项目平台判断。 |
| [2609.22590](https://arxiv.org/abs/2609.22590) | 一般 DNN 的 16-bit 格式与选择性 ECC，实验在通用网络而非大模型训练/推理；未给本项目新系统约束。 |
| [2609.22743](https://arxiv.org/abs/2609.22743) | CPU 弱内存排序实现，虽有通用硬件意义，但摘要未联系模型计算/通信主线，不能以“AI 也用 CPU”入选。 |
| [2609.22443](https://arxiv.org/abs/2609.22443) | 物理神经网络输出的 edge/fog trust fusion，不是本项目大模型 Agent/Serving 可靠性机制。 |
| [2609.22765](https://arxiv.org/abs/2609.22765) | Verilog 代码生成数据选择使用模拟验证、IFD 与聚类，设计特征与收益都绑定 HDL 场景；未分离新的通用训练数据/评价边界。 |
| [2609.23444](https://arxiv.org/abs/2609.23444) | 芯片 ECO 领域的 agent+本地 9B 模型闭环应用与成本对比，未证明新的通用 Agent 控制/训练机制。 |
| [2609.24288](https://arxiv.org/abs/2609.24288) | 55nm 模拟 CIM 的 SA/SAR 设计与小型视觉网络评估，未触及本项目当前大模型计算路径。 |
| [2609.24904](https://arxiv.org/abs/2609.24904) | 3D chiplet 多 kW 供电方法综述，AI 只是需求背景；不直接改变大模型架构/运行时设计。 |

上述候选前关闭只基于题摘所能支持的项目范围/贡献判断；未为不影响处置的项目追查完整发表史或正文，不声称论文价值为零。`2609.22196` 属漏收敏感样本，应纳入独立准入抽检。

### 独立主题批次：`cs.DC / cs.AR / cs.OS / cs.PF`

本批 60 个 New/Cross 唯一标题已全部浏览：50 个 New 的首轮项目范围/贡献筛选得到 12 个上述“优先复核”、9 个“尚待裁决”、29 个候选前关闭；这只是本批准入初判，**不是**全 arXiv 候选分母，也尚未经独立复核。50 个 New 中 32 个读取了完整摘要（上述已有 12 项、此次新增 20 项）；其余 18 个标题明确是下列范围外任务，按研究合同的标题范围停止。与早先分组重叠的项目不重复计数。

| 仅标题即可关闭的 New 家族 | 标题已明确限定的非本项目主线 |
| --- | --- |
| [2609.22343](https://arxiv.org/abs/2609.22343) | 后量子密码在 RISC-V GPGPU 上加速，而非模型算子/LLM 运行时。 |
| [2609.22347](https://arxiv.org/abs/2609.22347) | 芯片设计验证任务的 reward model，未表明一般大模型 RL 训练机制。 |
| [2609.22358](https://arxiv.org/abs/2609.22358) | 智能水表时序数据集及清洗 pipeline。 |
| [2609.22775](https://arxiv.org/abs/2609.22775) | Spiking LIF 神经元的硬件设计/验证。 |
| [2609.22814](https://arxiv.org/abs/2609.22814) | 地震估计 HPC 工作流的闲置资源利用。 |
| [2609.22897](https://arxiv.org/abs/2609.22897) | 边缘设备上的物种识别任务。 |
| [2609.23116](https://arxiv.org/abs/2609.23116) | StreamNTT 的 Verilog-to-routing 工具链评测。 |
| [2609.23438](https://arxiv.org/abs/2609.23438) | 一般大数据共享系统 i-Cloud。 |
| [2609.23454](https://arxiv.org/abs/2609.23454) | 匿名机器人队形形成的控制/分布式算法，而非 VLA/World Model。 |
| [2609.23773](https://arxiv.org/abs/2609.23773) | 去中心化联邦学习的 peer selection，没有大模型训练系统限定。 |
| [2609.23843](https://arxiv.org/abs/2609.23843) | 联邦学习客户端调度，没有大模型训练系统限定。 |
| [2609.24018](https://arxiv.org/abs/2609.24018) | 通用拜占庭可靠广播算法。 |
| [2609.24436](https://arxiv.org/abs/2609.24436) | 范畴消息传递语言语义，不是模型/Agent 通信协议。 |
| [2609.24497](https://arxiv.org/abs/2609.24497) | 经典机器人 RRT* 路径规划加速。 |
| [2609.24628](https://arxiv.org/abs/2609.24628) | HL-LHC 科学分析数组在 AMD ROCm 的移植；AI for Science 暂缓。 |
| [2609.24713](https://arxiv.org/abs/2609.24713) | 区块链交易传播的抢跑攻击缓解。 |
| [2609.24757](https://arxiv.org/abs/2609.24757) | PYNQ-Z1 上特定车辆检测模型的量化 NPU 实现。 |
| [2609.24802](https://arxiv.org/abs/2609.24802) | 一般图消息传递编译，不等同大模型计算图或训练 runtime。 |

10 个仅 Cross 的 ID 为 `2609.22087`（可用性约束训练）、`2609.22601`（Agent 检索）、`2609.22645`（Ising）、`2609.22781`（数据库 io_uring）、`2609.23218`（内核 bug）、`2609.23517`（RISC-V 验证）、`2609.23700`（AI-native OS 安全综述）、`2609.23766`（K8s RCA）、`2609.24404`（EVM 编译）、`2609.24519`（FP4 tensor core 编码）。Cross-list 本身只改变分类，不构成首次公开或重要修订；前两项以及 AI-native OS、K8s RCA、FP4 题目可作真实首次公开日期的定点恢复线索，其余标题已明显在本项目范围外。本批没有把 Cross 当 New 计分。

### 独立主题批次：`cs.CL / cs.LG` 的训练与推理

按标题中的 training、pretraining、distillation、gradient、RLHF/GRPO、quantization、speculation、KV、decoding、inference 等词建立**阅读队列**，对 `New` 跨分类去重得 93 项。词命中本身不构成准入；其中 65 项读完完整摘要（早前已读 21、此批新增 44），28 项仅由标题已明确限定为医疗、材料、金融、工业控制、气候、EEG 等非大模型主线，按下文逐项关闭。以下 44 项新增摘要审阅的判断仍是**第一轮贡献筛选**，不是全文证据或最终分母。

| 追加高优先级，需独立准入及来源审阅 | 项目贡献假设与边界 |
| --- | --- |
| [2609.22254](https://arxiv.org/abs/2609.22254) | On-policy distillation 的 teacher continuation 长度同时改变监督方差与轨迹偏差；需核与 2609.22109 等同日 OPD 家族的独立增量。官方 abs 的 `v1 Submitted` 为 09-06，但出现在本次 New 公告，需特别排查其他更早公开渠道。 |
| [2609.22867](https://arxiv.org/abs/2609.22867) | 扩散生成的有限推理预算不能均匀分配给每一 denoising 步；需核误差/延迟预算模型和图像以外适用范围。 |
| [2609.23457](https://arxiv.org/abs/2609.23457) | RLVR 多维 rubric 若直接线性合并，会暗含跨准则可补偿、可比较的基数效用假设；组内序关系改训练信号，需核控制变量及 credit assignment。 |
| [2609.23585](https://arxiv.org/abs/2609.23585) | 4-bit 权重量化后，sink head 全局排序可能稳定而具体 top-k/head 与层级策略不稳定；需核 KV 选择策略的跨域校准边界，不把三个小模型外推。 |
| [2609.23916](https://arxiv.org/abs/2609.23916) | 时间增量继续预训练的 web crawl 存在 URL 重叠，不能照搬无交集 continual-learning 评价；需核 cutoff、数据泄漏、全量遗忘指标及 LoRA/full CPT 比较。 |
| [2609.24141](https://arxiv.org/abs/2609.24141) | OPD 的 teacher-scored token 与 student 更新可拆成两个预算；冻结信号多次 actor pass 是否真的降低 teacher 成本而不放大 off-policy 偏差，需核 8-H20 受限实验。 |
| [2609.24322](https://arxiv.org/abs/2609.24322) | 分类 accuracy 保持不代表量化检索 top-1 身份保持；候选 margin 与舍入误差之间给出可检查的精度升级边界，需核模型/索引/查询分布。 |
| [2609.24432](https://arxiv.org/abs/2609.24432) | OPD 的 token-level 训练信号可按梯度估计贡献而非均匀消费；需核 1% token 主张的 teacher/student、预算及泛化限制。 |
| [2609.24646](https://arxiv.org/abs/2609.24646) | 示范条件 teacher 的信息注入量逐 token 可控，和冻结 base-policy 锚点共同决定专门化/遗忘取舍；需核 SDFT 既有覆盖与比较公平性。 |
| [2609.24698](https://arxiv.org/abs/2609.24698) | Tree speculation 在压缩注意力下引入分支专有状态，verify/commit 后需刷新被接受路径；需核所谓 DeepSeek-V4-Flash 的公开 artifact、state 正确性与对照，不能凭论文名称视作厂商实现。 |
| [2609.24974](https://arxiv.org/abs/2609.24974) | 专用 Agent harness 的控制收益如何经训练迁到固定部署 harness，涉及 action-space/可见信息不一致；需核任务对照和哪些能力不能蒸馏。 |

这 11 项与上文 23 项合计 34 项**待复核高优先级线索**，绝非 34 个已冻结候选。它们均在上述官方 Tuesday New 公告批次，公告时间暂按 09-23 08:00 北京时间；arXiv 的 `Submitted` 字段不是公告或其他渠道首发证明。[2609.22870](https://arxiv.org/abs/2609.22870)、[2609.22254](https://arxiv.org/abs/2609.22254)、[2609.23457](https://arxiv.org/abs/2609.23457)、[2609.24698](https://arxiv.org/abs/2609.24698)、[2609.23916](https://arxiv.org/abs/2609.23916)、[2609.24322](https://arxiv.org/abs/2609.24322) 已重新打开官方 abs，均见 `v1`、未见撤回声明；其他项尚未逐一完成该检查。

新增已读摘要但**准入待裁决**：`2609.22091`（prospective memory）、`2609.22145`（diffusion LM 数据检测）、`2609.22146`（post-train SVD 几何）、`2609.22178`（CUA safety/capability）、`2609.22194`（广告 Agent SFT/RL 阶段）、`2609.22206`（多模态不确定性评估）、`2609.22452`（语音长上下文 benchmark）、`2609.22566`（OOD 蒸馏）、`2609.22603`（摘要事实脚手架评价）、`2609.22684`（VLA 单状态 token）、`2609.23055`（扩散优化器受控比较）、`2609.23205`（数学 sycophancy）、`2609.23215`（Agent 解释器错误）、`2609.23449`（Agent 记忆蒸馏）、`2609.23697`（多 teacher OPD）、`2609.23716`（prompt 自修订的非回归门控）、`2609.23742`（schema 强约束 vs 语义正确）、`2609.24196`（looped LM decoding）、`2609.24202`（稀疏注意力 token 群聚解释）、`2609.24303`（post-train 无标签校准）、`2609.24379`（topographic circuit）、`2609.24799`（医疗量化与解释证据）、`2609.24942`（OOD exactness 理论）。这里只能证明它们已读题摘，不能用“待裁决”自动保留；特别是 `2609.24942` 的广泛理论主张必须全文核定假设，`2609.24799` 必须判定是否只是医疗场景结果。

新增**读完摘要后的候选前关闭**：

| arXiv 原始材料 | 此项目的具体关闭理由 |
| --- | --- |
| [2609.22149](https://arxiv.org/abs/2609.22149) | 表格加文本的合成数据依赖测试；未涉及本项目多模态基础模型表示或训练数据生命周期的独立约束。 |
| [2609.22805](https://arxiv.org/abs/2609.22805) | 多参考同行评审生成任务的训练集与质量比较，未分离出可迁移的模型训练机制。 |
| [2609.23463](https://arxiv.org/abs/2609.23463) | 三种文本分类 backbone 的联邦 LoRA 最弱客户端实验，不是当前大模型分布式训练主线的模型/通信设计结论。 |
| [2609.23966](https://arxiv.org/abs/2609.23966) | Table-to-text 数量陈述的 task-local checker，未扩展为本项目通用 evidence/release contract。 |
| [2609.24401](https://arxiv.org/abs/2609.24401) | 通用小型神经网络结构剪枝实验，没有 LLM 或大模型推理执行路径证据。 |
| [2609.22216](https://arxiv.org/abs/2609.22216) | 五个 7–8B 模型在临床 benchmark 上的 GPTQ 精度/安全比较；其“INT8 universally safe”仅在这些测试条件内成立，未形成超出现有“按任务和安全风险验收量化”原则的新系统设计。 |
| [2609.22221](https://arxiv.org/abs/2609.22221) | 单 surrogate 检测器上的 GRPO 对抗改写，官方评测转移有限；结论局限于 AI 文本检测任务。 |
| [2609.22607](https://arxiv.org/abs/2609.22607) | 用 base LM 模拟人类对话的多样性/准确率，目标是 human simulation，不是本项目模型系统或 Agent 工作流设计。 |
| [2609.24103](https://arxiv.org/abs/2609.24103) | POMDP 分布式 RL 的 Bellman 收敛与 point-based planning 理论，不指向 LLM RL/Agent runtime 的新控制边界。 |
| [2609.24651](https://arxiv.org/abs/2609.24651) | 语音增强 diffusion/flow 的 rollout-state mismatch 修正，实证只在专用语音重建；尚不足以改变 Part III 通用生成范式判断。 |

其余 28 个题目已明确限定项目范围外，按标题停止，不声称已读其摘要：`2609.22171`（医用钠摄入推断）、`2609.22184`（药物靶点预测）、`2609.22233`（能源材料发现）、`2609.22240`（一般对抗训练统计定理）、`2609.22584`（工业 PID 控制）、`2609.22785`（金融做市）、`2609.22833`（联邦 RL 理论）、`2609.22919`（一般 safe RL exploration）、`2609.23127`（连续时间 MDP 理论）、`2609.23219`（潜在混杂因果推断）、`2609.23374`（临床 RL 证据）、`2609.23435`（组学任务领域蒸馏）、`2609.23547`（图 prompt 的最优传输）、`2609.23549`（电解催化剂预测）、`2609.23590`（电池能源调度）、`2609.23775`（鲁棒 RL 的 Transformer encoder 统计理论）、`2609.23875`（空间态势传感器指派）、`2609.24042`（时序 forecasting 深度平衡模型）、`2609.24083`（STEM 教学视频生成）、`2609.24177`（孟加拉法律场景的手机 RAG）、`2609.24219`（新闻来源可信度分类）、`2609.24233`（EEG 解码）、`2609.24249`（一般计算机视觉对抗攻击）、`2609.24422`（混合效应模型统计推断）、`2609.24489`（一般 offline RL 线性规划）、`2609.24679`（低秩张量恢复定理）、`2609.24754`（气候动力系统预测）、`2609.24882`（对流参数化模型）。这些题目中的 RL、Transformer、Inference 等通用词不能单独让其进入本项目候选。

### Agent / Evaluation 专题增量题摘

在宽入口的 Agent、Tool、Memory、Benchmark、Evaluation、World Model 标题主题队列中，定点完整阅读了以下 15 个此前未读 `New` 摘要。这只是**局部补检**，其余标题尚未封口。较可能改变本项目长期设计判断、值得下一步独立准入复核的是：`2609.22218`（万级能力目录先检索压缩再由 LLM 选择；核召回/缓存/SLO）、`2609.22223`（长文 factuality 的关联 claim 分组与证据复用；核相关错误和搜索预算）、`2609.22592`（Agent RL gym 先定义解空间与可执行 verifier 再生成环境；核是否真能降低后验 judge 漏误）、`2609.23058`（Agent 程序按目标需求集合惰性 materialize；核正确性及跨步副作用）、`2609.23806`（任务确定前固定组织可见状态，避免 benchmark 以任务选择 context 造成评价捷径；核合成公司外推）、`2609.24985`（多轮工具 RL 区分行动敏感 reward variation 与后续随机噪声，再选择可训练调用点；核 BFCL-v4 诊断/训练对照）。这六项只作为可复核增量假设，不并入上述 34 项初批线索计数，更不能视为已入选。

另九项读完摘要但先比较既有 owner/证据强度：`2609.22111`（Agent 论文-代码-实验 artifact 一致性审计，可能已由 Evaluation 承载）、`2609.22247`（search agent 对 harness 更新的泛化，需与 2609.24974 同 family 概念去重）、`2609.22259`（Text-to-SQL context layer 内容与检索 scaffolding 四臂消融，领域外推有限）、`2609.22587`（VLA 按事件触发异步推理，需核真实频率/时延合同）、`2609.22599`（LLM judge 四表面扰动测试，需核成熟 robustness 测试是否已覆盖）、`2609.23465`（多参与者对话记忆的 evidence→active-state 提交，与现有 AGENT-MEMORY 可能重合）、`2609.24264`（工具 trace 的可审计 action 注释协议，作者自己指出重复率不等于语义准确）、`2609.24890`（CUA 过程子目标评价，需核 human annotation/judge 错误）、`2609.24972`（Harness 自演化的候选约束和 OOD 对照，需与 2609.24130 区分）。这些都不能只凭摘要直接写入日报结论。

### World Model / VLA 专题：57 个 `New` 全部题摘审阅

在 1,003 个 New 的标题上以 `world model / VLA / vision-language-action / embodied / robot policy / robotic foundation / robotic manipulation` 作主题阅读队列，跨分类得 57 个唯一身份。57 份摘要均实际读完，其中 6 项已在之前批次记录（`2609.22335`、`2609.22587`、`2609.22684`、`2609.22888`、`2609.23252`、`2609.24749`），本次新增 51，避免重复累计。这只闭合**该标题主题队列**，不是所有机器人/多模态论文或 arXiv 的来源 Gate。

| 10 项需优先独立准入复核的新增题摘 | 具体增量假设及所需证据边界 |
| --- | --- |
| [2609.22293](https://arxiv.org/abs/2609.22293) | VLA 的图像扰动评价从随机采样转为对连续扰动区域的 sound validation；需核 H²V-M 证明的假设、覆盖区域与真实传感器噪声边界。 |
| [2609.22582](https://arxiv.org/abs/2609.22582) | 驾驶 VLA 排名不能解释行人避让机制；成对编辑场景检验 exposure/响应的因果敏感性，需核编辑真实性、预注册与 open-loop→闭环边界。 |
| [2609.22641](https://arxiv.org/abs/2609.22641) | 多 Agent world model 的共享历史与同时生成 peer view 需按可见性路由，提出跨视角状态 owner；需核静态场景、固定 Agent 数与世界状态一致性。 |
| [2609.22858](https://arxiv.org/abs/2609.22858) | 物理环境被行动改写后，已提交的观测信念与候选行动的 imagined state 不能混写；需核 excavation 场景之外的推广条件。 |
| [2609.23910](https://arxiv.org/abs/2609.23910) | Real-to-sim 的视觉/几何重建质量影响 VLA 策略排序能否外推真实世界；需核 matched policy trial 与场景覆盖。 |
| [2609.24274](https://arxiv.org/abs/2609.24274) | CPU VLA 推理的关键不是单次 latency，而是 action chunk 对控制周期的供给与反馈频率；需核 4 CPU、6 policy、fp32/int8、热稳定与实机 SLO。 |
| [2609.24350](https://arxiv.org/abs/2609.24350) | VLA visual robustness 不只遮挡，还包括 camera staleness、来源一致性与任务前提变化；需核仿真/真实机器人协议与模型族外推。 |
| [2609.24433](https://arxiv.org/abs/2609.24433) | VLA W4A4 校准—执行表示一致性与关键层 W8A8 回退形成精度/闭环行为取舍；需核 TensorRT 插件、Jetson/Ada、任务与 trial。 |
| [2609.24682](https://arxiv.org/abs/2609.24682) | World model 的状态表征可离线蒸馏给低时延 VLA，而非在线滚动生成；需核冻结 teacher、训练数据泄漏及真实控制收益。 |
| [2609.24984](https://arxiv.org/abs/2609.24984) | Video world model 用目标视角查询的隐式 3D memory 在固定 token 预算中维护跨视角历史；需核静态/动态场景与分钟级持续一致性。 |

上述 10 项同样只是**题摘层的复核队列**，不能与已冻结候选相加；同日大量 VLA 系统论文之间需比较是否重复描述“分层控制、闭环修正、状态持久化、低比特部署”已有路线。

另 16 项题摘尚需与既有 owner/近邻候选比较，暂不准入：`2609.22285`（虚构物理规则下的 continual pretraining 与执行解耦）、`2609.22840`（人工介入边界上的 residual TD 信用归属）、`2609.22879`（世界模型 rollout 的不确定性加权采样）、`2609.22973`（多站点 VLA federated fine-tuning 的真实异质性）、`2609.23578`（Agent→机器人原子技能的语言之外接口）、`2609.23614` 与 `2609.23968`（接触力/刚度交给 VLA 与底层控制器的不同合同）、`2609.23650`（外观不变与语义改变的动作响应区分）、`2609.23753`（active simulator query 与同状态不同动作反事实）、`2609.24033`（世界模型未来预测残差作为行动价值置信度）、`2609.24124`（主动感知的记忆写入/容量受控评价）、`2609.24170`（通用 LLM 当机器人 policy 的受限评测，只可作能力事实）、`2609.24271`（部署后经验演化系统，需核组件分别贡献）、`2609.24313`（动力学 operator 的跨场景表征）、`2609.24547`（全双工机器人动作用 predict-more-than-commit 限制物理提交）、`2609.24815`（robot 仿真的 streaming action-conditioned video，需核物理一致性与实时合同）。

其余 24 项读完摘要后按项目贡献门槛候选前关闭；不表示论文无学术价值：`2609.22175`（对视觉 distractor 用 contrastive 表征取代像素重建，是已知 world-model 目标取舍，本篇小规模实验未改变设计边界）、`2609.22289`（施工规格-演示采集接口，仅单场景验证）、`2609.22317`（驾驶预测的事件残差 gate，局部模型性能）、`2609.22385`（具身导航空间检查，局部任务规划）、`2609.22538`（人形机器人失效监控只独立测 monitor，恢复闭环未评）、`2609.22691`（人类行为模拟目标而非本项目物理行动合同）、`2609.22854`（LSTM episode state 用于 VLA 已属持久状态原则的实现变体）、`2609.22895`（high-level key action→low-level motion 已在 Part III 分层控制主线）、`2609.22926`（软体机械臂弹性释放特定机理）、`2609.23118`（越野车辆地形物理 world model 场景特化）、`2609.23133`（水下 code-as-policy 单场景应用）、`2609.23184`（显式 CoT 的 embodied 视频预测性能声明，未分离新的状态/control ownership）、`2609.23275`（staged VLA 控制表征的局部训练方案）、`2609.23333`（患者营销转化预测，领域外且说明因果反事实不成立）、`2609.23565`（VLA 视觉遮挡常规 regularization）、`2609.23566`（无学习 RGB-D 位姿求解器，非大模型机制）、`2609.23656`（LiDAR UAV 探索特定几何任务）、`2609.23755`（人类手操作到机器人数据/模型发布，尚未改变一般 VLA 系统合同）、`2609.23944`（拓扑视觉提示在少量特定双手任务中验证）、`2609.24118`（VLA 失败状态纠正流水线，既有闭环恢复原则且收益为局部任务）、`2609.24187`（肠道内镜专用 VLA）、`2609.24525`（3D 视觉特征与 action diffusion 条件的局部结合）、`2609.24526`（ME-VLM 型号/训练与压缩发布，题摘不足以证明一般新机制）、`2609.24626`（驾驶场景关系图监督的局部表征增益）。其中技术看似重要但早已有独立知识 owner 的项，若后续 source review 给出反证可重开，不直接删去筛选记录。

另有 [2609.23048](https://arxiv.org/abs/2609.23048) 从原优先复核队列经独立复核转为候选前关闭：其离线通过/闭环失败仅为受限案例；成功 rollout 数据包同时改变成功筛选、teacher label、视觉域与 OXE 占比，训练脚本只控制混入比例 `ρ_R=0.5` 对 `0`，不能声称单因素归因或新通用机制。故本专题为 10 项优先、16 项待比较、25 项候选前关闭。

### Agent / Information-State 续批：33 个新增 `New` 摘要

以 `agent / tool / harness / memory / context / retrieval / RAG` 在 1,003 个 `New` 标题中形成 166 个唯一身份的宽阅读队列；已浏览这 166 个标题，并对其中 34 个读完摘要。`2609.24663` 与前批重复，故本批只有 **33 个新增已读身份**。其余标题虽经首眼范围判断，但尚未逐项留下标题关闭理由，**本主题不能称已闭合**。以下仍是题摘级贡献筛选，不是 Full Source Review 或最终分母。

| 9 项优先独立准入复核 | 题摘显示的潜在长期设计增量与核验点 |
| --- | --- |
| [2609.22120](https://arxiv.org/abs/2609.22120) | Agent memory 不只保存轨迹摘要，而可保存以执行状态为条件的 walkthrough 并在调用时做依赖切片；需核状态正确性、缓存失效与长任务对照。 |
| [2609.22200](https://arxiv.org/abs/2609.22200) | 多轮对话隐私不能只按单响应泄漏率评估；同一 PII entity 在跨轮覆盖与组合攻击中的评价合同需要核对。 |
| [2609.22222](https://arxiv.org/abs/2609.22222) | Agent 能成功调用代码/工具不等于从官方统计中得出语义正确结论；需核 verifier 是否能区分执行正确性和来源/数值正确性。 |
| [2609.22819](https://arxiv.org/abs/2609.22819) | 工具选择由历史日志学习时受 support/privilege 边界约束，未覆盖动作需取消而非给反事实高分；需核 direct/DR estimator、反事实假设与真实工作流。 |
| [2609.23053](https://arxiv.org/abs/2609.23053) | RAG 答案正确不保证引用的证据真的参与生成；answer reward 与 citation faithfulness 应独立评估，需核干预式 attribution。 |
| [2609.23121](https://arxiv.org/abs/2609.23121) | 多模态 Agent 的图像上下文可作为一次性分支，文本主线持久；需核状态所有权、跨步记忆和重复视觉编码代价。 |
| [2609.24144](https://arxiv.org/abs/2609.24144) | 成对 rollout 的 reward-contrast 方差、策略梯度方差和最终学习收益并非同一量；需核预注册实验、配对设置与具体 estimator。 |
| [2609.24259](https://arxiv.org/abs/2609.24259) | Agent memory 既可能过度使用也可能未使用；以命题/token 反事实 credit 追踪记忆读写，需要核反事实构造及对最终任务结果的证明范围。 |
| [2609.24971](https://arxiv.org/abs/2609.24971) | Memory benchmark 在固定长历史、任务相关证据与 cost/latency 下测系统选择，不只测末端回答；需核任务隔离、oracle 和评价成本。 |

15 项**已读而准入待比较**：`2609.22162`（FedRepRAG 的跨客户端 latent 交换与隐私保证）、`2609.22682`（多 Agent 自组织，不确定是否超出现有协调原则）、`2609.22880`（per-query reranker gate 的有害跳过率校准）、`2609.22943`（selection-conditioned prompt/response token 数据选择）、`2609.22951`（step-level Agent model router）、`2609.23466`（跨会话 parametric memory 与 LoRA 生成链）、`2609.23512`（可验证的自适应 Agent 配置）、`2609.23808`（coding Agent dense reward 的训练生命周期）、`2609.23986`（双控制/记忆平面的 Jev-Mem）、`2609.23989`（Agent 持续学习）、`2609.24115`（合成的 grounded 边界工具场景）、`2609.24238`（模型记忆与上下文事实分离重复实验）、`2609.24290`（澄清式提问的反事实信息增益）、`2609.24662`（双控制 Agent 安全评估）、`2609.24983`（保留 on-policy 性质的 token-level 修正标注）。其比较问题是：这些工作究竟改变了本项目状态/控制/evaluation contract，还是已有机制的新数据集、实现和 operating point。

9 项**读完摘要后候选前关闭**：`2609.22119`（200 个提示上的 evaluation-awareness/activation steering，未见可迁移的发布/评估边界）、`2609.22562`（视觉文档 patch 压缩的局部检索优化）、`2609.22939`（问答图路线探索，主要对照经多重检验后无显著改善）、`2609.23142`（Unreal 场景的特定 Agent benchmark）、`2609.23354`（AI 搜索语境概念框架，未提供新系统机制）、`2609.23939`（XY-problem benchmark，重复已有澄清意图原则）、`2609.24220`（单一企业文档 PDF 标准化/分块管线，未分离超出既有 RAG 数据质量原则的新合同）、`2609.24277`（GUI 坐标 digit entropy，局部任务置信度代理）、`2609.24831`（ReAct 不确定性图度量，局部计算方式而非通用控制边界）。这些关闭不声称论文无价值；若独立漏收抽检发现未读机制可重开。

### Model / Multimodal / Execution 续批：17 个新增 `New` 摘要

从 New 中标题涉及通用模型、跨模态生成、扩散执行和推理状态的未读身份定点选 17 项，均读完完整摘要；本批与前面 214 个身份无重复。此处的“优先”只表示有**具体待证设计增量**，不等于准入，更不把摘要里的速度、质量或安全数值外推。

| 6 项优先独立准入复核 | 具体问题与证据边界 |
| --- | --- |
| [2609.22234](https://arxiv.org/abs/2609.22234) | VLM 的指令层级冲突跨越 text/image，文本对齐训练未必迁移到图像中的可执行指令；核图像攻击构造、真实网页 Agent 安全对照与能力保留。 |
| [2609.22283](https://arxiv.org/abs/2609.22283) | 流式 video diffusion 不一定要等历史帧完全去噪才可消费；历史状态选择改变 denoising 依赖图、流水执行与训练-推理匹配，核调度收益是否是端到端而非仅 DiT steady state。 |
| [2609.22361](https://arxiv.org/abs/2609.22361) | 音视频共因 latent 不保证去除外观 shortcut；需核结构因果假设、反事实扰动可识别性与真实 pretrained generator 的干预边界。 |
| [2609.23153](https://arxiv.org/abs/2609.23153) | 稀疏视频扩散的 step-local loss 下降不等于最终样本质量改善；作者以终端分布对齐训练纠偏，需将 sparse warm-up、蒸馏、FP8/融合核的收益分离，不能引用 `265×` 为通用速度。 |
| [2609.23900](https://arxiv.org/abs/2609.23900) | GDN/Attention 混合模型的 tree verification 除祖先 attention mask 外还须维护 branch-local recurrent state 和 accepted-chain commit；核 vLLM 代码、概率重评分等价范围及 batch/端到端代价。 |
| [2609.24881](https://arxiv.org/abs/2609.24881) | 黑盒 API 无 logits/权重时可用外部校准器估正确概率，但 AUROC 不等于 claim-level evidence confidence；需核跨模型和分布偏移校准、选择性回答风险。 |

8 项**已读而准入待比较**：`2609.22107`（合成因果结构上训练任意模态融合，需核“任意”在 12 模态/11 任务之外的可证范围）、`2609.22135`（omni-modal probe-best 与 steer-best 层的分离，需核是否改变本项目干预层选择判断）、`2609.22199`（跨层共享专家池，需与现有 MoE/共享参数对比真正新约束）、`2609.22243`（冻结小模型的状态索引 replay 授权，需核只是既有 action authorization 的形式实例还是新增机制）、`2609.22916`（AR layout 与 diffusion renderer 的联合训练，需核视觉文字 workload 的分工是否可迁移）、`2609.23658`（视频生成物理违例归因 RoPE 空间衰减，需核因果头干预与跨架构稳健性）、`2609.23715`（视觉 token pruning 后位置编码按 grounding 敏感层切换，需核既有位置保持主线的独立增量）、`2609.24346`（diffusion GraphRAG 在部分去噪实体稳定时事件触发检索，需核检索/rollback 正确性与真实端到端延迟）。

3 项**候选前关闭**：`2609.22151`（单一 recipe 禁用原料任务上 compliance 与自述分离；其 GRPO/SFT 对比尚未证明一般 model self-knowledge 或系统控制结论）、`2609.24440`（Mamba-130m/Pythia-70m SAE 对齐度被用来提出广泛表示普遍性主张，题摘的模型规模与 feature-matching 范围不足以改变本项目架构判断）、`2609.24919`（pixel diffusion 的 frozen vision 表征引导在 ImageNet FID 改善，未给跨工作负载的生成执行/状态新合同）。

### 剩余机制主题续批：23 个新增 `New` 摘要

从未读 New 中与硬件评价、Hosted LLM、Agent Evaluation、记忆/视觉状态、VLA 和训练/推理执行有关的标题定点选 23 项，全部读完摘要；它们此前未计入 231。标题中含 Agent、Benchmark 或 Robot 只是阅读入口，以下处置以摘要是否给出本项目具体设计/评价增量为准。

| 7 项优先独立准入复核 | 具体增量与证据边界 |
| --- | --- |
| [2609.22122](https://arxiv.org/abs/2609.22122) | 跨设备模型 ranking 可迁移不代表目标设备 latency+energy 可行集合可迁移；需核 HW-GPT-Bench 的 13 个设备、阈值设定和 RTX3080 proxy 的适用性，避免把排序相关性冒充部署可行性。 |
| [2609.22478](https://arxiv.org/abs/2609.22478) | Hosted LLM 评价要分清历史复现、相同标识下测量配置敏感性和跨标识持久性；摘要明确六个配置同时变化，不能归因某一项，还需核日期/serving period。 |
| [2609.23490](https://arxiv.org/abs/2609.23490) | 多语言 Agent benchmark 的翻译须保持 tool/control-flow 语义，任务成功、调用错误、token 成本和语言切换应分开；需核人工核验和 23 种语言的任务等价性。 |
| [2609.24165](https://arxiv.org/abs/2609.24165) | Agent 不能仅靠回答声称工具执行成功；外部 deterministic guard 将无执行凭证的产物变为明确 non-result，需核模拟 motor-control 与真实 beamline 证据边界。 |
| [2609.24362](https://arxiv.org/abs/2609.24362) | VLM sandbox 的图像证据应有独立 artifact ledger 和有限 active context，由模型显式提升可见性；需核 `2×2` 对照、302 rescue/142 regression 与本地 vLLM 测量条件。 |
| [2609.24797](https://arxiv.org/abs/2609.24797) | Kimi Delta Attention 在 gate/range 扩展下的状态转移表达力与稳定性兼容性是模型记忆机制问题；需核定理前提、真实 LM scaling 与已有 recurrent owner 的边界。 |
| [2609.24967](https://arxiv.org/abs/2609.24967) | 多 Agent 长期共享日志与互相验证可能让 reward 最优化产生串谋，需核协议冲突的构造、peer intervention、历史截断对照和外推边界。 |

9 项**准入待比较**：`2609.23363`（RTL coding Agent 的 post-PnR timing closure evaluator，领域特化）、`2609.23580`（VLA 以标量任务阶段减轻 observation aliasing，可能已由 Part III 持久状态承载）、`2609.23601`（256 KiB 写一次读多次的长视频 memory，需核冻结 VLM 与 KV 前缀修改代价）、`2609.23841`（机器人搜索持久 world-state graph 与证据请求，需核 CityNav/实机的推广范围）、`2609.23888`（触觉 teacher 的未来接触包蒸馏到无触觉 student，需核接触状态与行动的因果分工）、`2609.24071`（图表 Agent 将 structure/evidence/derivation 变成可审计 reward，需核 human/oracle 对照）、`2609.24417`（可微分的固定大小 routed KV memory，需核与已有 recurrent/cache 架构的真实差异）、`2609.24563`（task-specific Real2Sim2Real Agent 数据工厂，需核自动化阶段各自贡献）、`2609.24875`（VLM 极低比特权重量化与 GEMV 查表内核，需核单 RTX A6000 decoder operating point 是否有长期机制增量）。

7 项**候选前关闭**：`2609.22600`（GovSim 社会制度自撰规则，核心问题是伦理/共同资源困境而非本项目系统设计）、`2609.22712`（Agent 信任综述及未实证验证 lifecycle 框架，没有新的可核实机制）、`2609.23201`（通用排行榜不足以选应用模型的观点，已由本项目 Evaluation workload contract 承载）、`2609.24370`（FashionMNIST/CIFAR/Food 小型视觉网络的谱 attention 诊断，不支撑 LLM 推理架构判断）、`2609.24485`（单 FastVLM 上的视觉 token 预剪组合，尚未超出现有 token pruning/位置保留原则）、`2609.24755`（epistemic runtime 的概念框架与八个待测假设，明确无实证结论）、`2609.24997`（视频生成工具 Agent 的受限任务训练/benchmark，未建立超出一般 Agent tool-use 的控制机制）。

### 未命中宽关键词标题的反向漏收抽检

为检验标题词门槛是否漏掉新命名机制，对 `New` 标题中**未命中** `LLM / language model / transformer / agent / diffusion / foundation / GPU / KV / inference / train / memory / retrieval / robot / multimodal / world model / attention / expert / quantization / policy / benchmark / evaluation / serving / pretraining / distillation / vision-language`（含词形变体）的列表按 ID 排序，以 `NR % 13 == 7` 作可复现的 34 项系统抽样。34 个标题均人工浏览：既有账本 4 个身份（`2609.22289`、`2609.22443`、`2609.23127`、`2609.24847`）不重复计；8 个题意有歧义者及 5 个具身表征边界项读完摘要，共 **13 个新增已读身份**。这证明广泛关键词会漏命名新颖的 Agent 工作，不支持“未命中者都可标题关闭”。

仅 `2609.24289` 暂列**优先独立准入复核**：其 FACT（环境事实）与 TIP（执行步骤）两轨更新声称分离环境表征误差与条件执行误差；需核理论假设、跨多环境任务消融与既有 `AGENT-MEMORY` / `AGENT-SKILL` 分工的独立增量。其余 12 个读完摘要后关闭：`2609.22208`（Gemma-2-27B 对情绪表示几何的复制，明确不含原工作因果干预）、`2609.22241`（电信领域微调及自家 benchmark 排名，没有新训练/Agent 合同）、`2609.22554`（functional parameter identifiability 的概念与 VN 单实现，题摘尚不足以改变 MoE/训练判断）、`2609.22866`（表格 foundation model 的局部架构与 Elo/延迟）、`2609.23971`（跨领域 RAG 平台以多索引融合与供应商自述 benchmark 组合成熟功能，未分离独立新机制）、`2609.24066`（推理时 latent steering 的局部采样方案，未建立可持续控制状态或通用预算结论）、`2609.24554`（概念数学形式比较，非本项目大模型系统链）、`2609.23352`（双手触觉补全的专用自监督表征）、`2609.23488`（驾驶轨迹可行场联动的专用生成器）、`2609.23666`（LiDAR/depth humanoid 地形传感器融合）、`2609.23856`（手术视频三维力估计）、`2609.24155`（visuomotor flow 的对象条件化，局部任务增益）。抽样余下 17 个新身份按标题范围停止，未读摘要：`2609.22117`（人类移动位置 embedding）、`2609.22167`（化学反应收率）、`2609.22647`（小学数学可视化教具）、`2609.22734`（临床转录分类）、`2609.22796`（阿拉伯方言翻译共享任务）、`2609.22956`（帕金森足底压力分类）、`2609.23061`（UAV 小目标检测）、`2609.23249`（Fresnel-Kummer 曲面数学）、`2609.23408`（帧插值运动估计）、`2609.23573`（作文评分）、`2609.23789`（分布回归统计）、`2609.24218`（无人机音频定位）、`2609.24386`（孟加拉儿童生长迟缓预测）、`2609.24468`（MRI Gaussian 重建）、`2609.24668`（对象检测）、`2609.24768`（区域图片编辑）、`2609.24947`（特定物理学习）；这些标题未显示本项目大模型/Infra 的独立系统约束，不声称全文筛查。

同一未命中宽关键词的 `New` 列表再按 `NR % 13 == 2` 独立抽 34 个标题，避免只用一条抽样序列作漏收结论。5 个已在账本（`2609.22098`、`2609.22142`、`2609.22840`、`2609.22926`、`2609.24436`）不重计；对其余中 13 个可能含机制的题目读完摘要。该批揭示原宽主题词还漏了**偏好训练可靠性、World Action Model 设计比较、评估指标调整副作用**三类高贡献线索，因此需要把这些概念加入语义抽检的阅读，而不是简单扩写无限关键词表。

新增题摘中 3 个**优先独立准入复核**：`2609.22359`（抗迎合的“坚持/更新/拒绝”三路可靠性合同，原偏好标签不含证人可靠度会产生不可辨识的 deference dial；需核给定可靠度和真实已审可靠度之间的边界）、`2609.24048`（World Action Model 将六种 world→action 因果结构、八种 latent、四类目标作受控比较；需核真实机器人 DROID 的证据范围与既有 Ch25/26 结论差异）、`2609.24194`（Reward/judge 分数消除表面格式效应可能同时损害目标 construct 对齐，需核预声明 slice、独立标注与全体负收益，不能把残差化当“修好 evaluator”）。

4 个**待与既有知识 owner 比较**：`2609.22782`（SAE 几何仅部分预测 steering 代价，Qwen BatchTopK 还有适用边界）、`2609.23935`（post-training 的 harmlessness 偏好会渗入用户回合预测，需核跨模型与基础模型对照是否改变对齐目标理解）、`2609.24821`（answer-basin 表示是假设及相关实验，不等于证明概念方向不存在）、`2609.22274`（humanoid 技能转成接触/语义/边界条件齐备的可执行轨迹接口，但目前仅 MuJoCo 序列实证）。

6 个**读完摘要后关闭**：`2609.22230`（列表计数失误模式的模型间差别，局部 probing/steering 结论尚不改变系统设计）、`2609.23381`（物理表示语言识别，AI for Science 当前不在项目范围）、`2609.23726`（加拿大法律问答专用数据和微调）、`2609.24111`（CIFAR/ImageNet-C 上测试时视觉表征适配，未涉及基础模型/LLM serving）、`2609.22701`（汽车制造数字孪生与 RL 控制生命周期，不是本项目大模型平台主线）、`2609.24511`（精准插装的仿真到实机 RL policy，未提出一般 VLA 状态/控制新机制）。另 16 个按题目明确限定非本项目任务或一般数学/工程问题标题停止：`2609.22192`（异构时序模拟）、`2609.22508`（GAN 表征）、`2609.22614`（过程预测）、`2609.23026`（脑 MRI 分割）、`2609.23111`（推荐模型继承）、`2609.23191`（低资源语音表示）、`2609.23293`（A* tie-breaking）、`2609.23456`（卫星定位）、`2609.23535`（一般因果发现）、`2609.23606`（网格纹理压缩）、`2609.23836`（K-12 教育观察数据）、`2609.24250`（船舶维护）、`2609.24358`（海事决策）、`2609.24619`（手术技能视频评分）、`2609.24737`（torus attractor 网络）、`2609.24903`（音节声调分类）。本批抽检的 34 个标题并非 34 篇全文审阅。

### 剩余 `New` 的全量标题浏览与 41 篇边界题摘

对此前未在账本出现的 646 个 `New` 按 ID 顺序浏览全部标题；不是 646 篇正文或摘要审读。显然仅为气象、医疗、遥感、小型分类器、通用数学/控制/网络、芯片电路等单领域任务，且题目没有模型系统机制或评价合同问题者，在题目级关闭；题意可能藏有新机制的 41 篇读完摘要。下列 16 篇是**待独立准入复核**的高敏感线索，不等于进入候选分母：

| ID | 题摘显示的可能系统增量与核验边界 |
| --- | --- |
| [2609.22197](https://arxiv.org/abs/2609.22197) | 对层级递归推理模型作 recurrent-state 因果干预与 Transformer 对照；需核 Sudoku/Maze/ARC 之外能否形成一般状态机制。 |
| [2609.22224](https://arxiv.org/abs/2609.22224) | steering 向量能改变拒绝/迎合，不代表原模型天然沿同一 circuit 决策；需核 reconstruction/ablation 识别性。 |
| [2609.22226](https://arxiv.org/abs/2609.22226) | 多目标 decode-time alignment 将 scoring/normalization/aggregation/selection 外置成可换控制契约；需核选项空间和成本/SLO。 |
| [2609.22246](https://arxiv.org/abs/2609.22246) | 仅能发布新闻内容的对手可能操纵检索式 LLM 概率预测；需核语料污染剂量、证据独立性及安全边界。 |
| [2609.23125](https://arxiv.org/abs/2609.23125) | 激活量化的 perplexity 总均值可能掩盖特定检索/归纳能力损伤；需核 12 模型配对对照及阈值。 |
| [2609.23260](https://arxiv.org/abs/2609.23260) | 跨任务 teacher ghost outputs 的 subliminal learning 提出 kernel/优化解释；需核假设能否转成训练数据污染判断。 |
| [2609.23366](https://arxiv.org/abs/2609.23366) | recurrent state 稳定收缩与保留可区分未来的信息有冲突；需核 predictive quotient 定理条件和模型实现边界。 |
| [2609.23478](https://arxiv.org/abs/2609.23478) | latent action 的加法合成/逆向代数一致性即使破坏时序配对也可成立，不能单独证明可控动态；需核破坏性负对照。 |
| [2609.23587](https://arxiv.org/abs/2609.23587) | 压缩 reasoning model 看似降低 jailbreak 率可能只是能力坍塌；需核 matched capability 下安全比较。 |
| [2609.23594](https://arxiv.org/abs/2609.23594) | LoRA 因子正交不保证最终 composed update 对旧任务保护；需核优化轨迹及持续学习适用条件。 |
| [2609.24243](https://arxiv.org/abs/2609.24243) | VLM RL 后 CoT 可监控性下降，activation intervention 声称可保持 ground 线索；需核指标与外部监控证据。 |
| [2609.24380](https://arxiv.org/abs/2609.24380) | 将 PPO 的时间进度从 token 改为信息密度；需核优势估计、非均匀序列及与 GRPO/现有 RL 的真正差异。 |
| [2609.24504](https://arxiv.org/abs/2609.24504) | 权重 merge 可能组合或抹去未显式训练的能力；需核两 testbed、模型家族及是否改 artifact merge contract。 |
| [2609.24678](https://arxiv.org/abs/2609.24678) | Muon 正交更新在 LoRA continual learning 的对照中可能替代部分专用保护；需核预算、旧任务遗忘与优化器选择。 |
| [2609.24745](https://arxiv.org/abs/2609.24745) | World Action Model 的视觉未来质量未必代表行动选择效用；需核 imagined rollout oracle 与实际决策差距。 |
| [2609.24885](https://arxiv.org/abs/2609.24885) | RAG 评价需区分上下文直接暴露答案与真正图结构推理，提出 copy-ceiling exposure control；需核 oracle、检索输入及跨任务迁移。 |

另 18 篇题摘**尚待与现有章节比较后裁决**：`2609.22144`（多语言安全敏感层）、`2609.22219`（潜知识与口头表达）、`2609.22228`（latent reasoning robustness）、`2609.22253`（merge-aware finetuning）、`2609.22332`（共享 human/robot affordance 表示）、`2609.22700`（双向 step PRM）、`2609.23369`（行动相关预测状态）、`2609.23371`（编译文档状态协议）、`2609.23731`（模块式机器人边际校准不可合成）、`2609.24174`（rubric replay credit 的形式化但经验边界有限）、`2609.24209`（表示迁移主张需排除替代解释）、`2609.24287`（CFG flow 局部几何）、`2609.24352`（少样本 world representation）、`2609.24868`（异步 world action model）、`2609.24895`（人机交互式证明的前提）、`2609.24976`（视觉触觉 world model）、`2609.24979`（端侧 LoRA hypernetwork）、`2609.24981`（几何 latent world generation）。这些均不能因映射到 Part III/Training/Agent 就自动保留。

另外 7 篇读完摘要后在候选分母前关闭：`2609.22131`（相关结构剪枝是局部模型压缩，未改已有稀疏/校准原则）、`2609.22153`（SafeTune 将已知安全微调办法打包，未分离新机制）、`2609.22248`（63 人问卷的 human checkpoint 信任校准，尚无可迁移系统实现）、`2609.22537`（EvidenT 的 lexical RAG grounding 组合已有证据原则）、`2609.22655`（GEO 搜索排名问题域不属于大模型系统）、`2609.23254`（一般量化监控数学没有大模型特定状态/评价边界）、`2609.23892`（circuit diff 是局部解释工具，未证明新的训练/服务设计结论）。41 篇题摘的处置是 `16+18+7`，并非 41 个入选。其余未读摘要的 New 均只作题目级范围关闭，独立漏收抽核前不可把该范围判断升级为确定的全源贡献闭合。

### 标题级关闭的独立漏收抽核

从当时未在账本出现的 `New` 标题队列按 arXiv ID 顺序取 `NR % 17 == 5` 的 36 个，检查题目级关闭是否把新命名机制漏掉。28 个题目明确为食品营养、泵维护、临床/教育/社会科学、视觉小任务、一般流体或无人机传感等领域任务；8 个有歧义的标题实际读完摘要。`2609.22237`（LoRA rank 按任务/层预算分配）目前只是已有 adapter 合并方案的局部预算搜索，待与 TRAIN-LORA 既有资源权衡比较；`2609.22913`（实时虚拟形象需协调外部 voice agent、帧调度和中断，另有 paired-audio 评价）有特定多模态实时控制边界，保留为**标准审阅待准入核验**，不把视觉质量数字外推；`2609.23886`（冻结 2B 模型作 typed choice，不生成文本）是一种受限分类决策分支，摘要中几组硬件/API 速度成本不可直接比较，尚不证明新通用 Agent 设计；`2609.24036`（自然语言权限策略拆解后编译、lint、正反测试）与已有外部 deterministic validation 原则重合，当前仅领域化对照；`2609.24411`（人类 egocentric 视频训练 VLA 加部署时 action-effect feedback）有具身适配信号，但 10K 小时与 2K 小时并非受控数据等价，需与 Ch26 已有路线比较；`2609.24778` 的四任务 Real2Sim H2R benchmark 结果只支持该协议，不证明一般 sim-to-real 可预测。`2609.23242` 是电商库存优化的双时标凸规划，`2609.23600` 是 CLIP seen/unseen prompt routing 的局部方法，均在候选前关闭。抽核发现至少 `2609.22913` 的系统设计线索，故原题目级关闭不能直接全部确认为无遗漏；需对同类实时多模态/跨组件调度题目扩查。累计实际读完摘要变为 329 个（327 个 `New`、2 个仅 `Cross`），其余 676 个 `New` 仅标题级处理。

### 第三轮漏收触发的实时多模态邻域扩查

因抽核发现 `2609.22913`，重新查询全 `New` 中含 streaming/real-time/synchronization/avatar/speech/audio/video/multimodal/interactive 等概念但此前未入账本的 67 个标题；对 16 个可能涉及模型系统状态、反馈或评价边界者读完摘要，其余标题仍限定为领域任务或图像生成局部改进。**可能值得独立准入复核**：`2609.22094` 将多模态内容理解与政策判断以可审文本接口拆开，但需证明超出既有 safety classifier + rule contract；`2609.22628` 固定 prompt/judge 对照 document QA 的 text/image/both 输入，可能改变 modality 成本/准确性路由边界，但要核 gold-page/full-doc 两条件与四端点；`2609.22788` 相同视频物理准确度不意味着模型与人类使用相同 forward-simulation 策略，需核人群/模型种子与分布比较；`2609.23144` 给机器人 scene graph 的节点、边和几何显式 belief 更新，需核实时状态维护及 Ch25/26 owner；`2609.23533` 弱模态不只优化不足，可能出现表示流形坍缩，需核几何诊断、干预与大模型迁移；`2609.24995` 将视觉/手势定位不确定度保留到规划的 proceed/clarify 控制，需核真实闭环证据。这些是贡献假设，不按标题自动纳入。

**待与既有 owner 比较或仅作受限案例**：`2609.22214` 的语音证据路由绑定 MLC-SLM 竞赛输入，`2609.22829` 的人形机器人末端/全身控制分层，`2609.23286` 的长视频三维重建 token memory，`2609.23997` 的小 VLM 多机器人通信/工具协作，`2609.24391` 的神经形态边缘 AVSR 执行限制；它们均需问能否改变当前多模态/具身/边缘章节的具体选择。**候选前关闭**：`2609.22697` 是 TTS 情绪风格/数据集，`2609.23267` 是知识图谱 entity alignment 的局部视觉可靠度，`2609.23486` 是主动机器人任务数据集，`2609.23825` 是联邦多语 ASR 架构比较，`2609.24031` 是活动识别的视频 layout 对齐预训练；题摘没有分离本项目长期机制或跨任务设计边界。该批共 16 篇，累计摘要变为 345（343 个 `New`、2 个仅 `Cross`），仍有 660 个 `New` 仅题目级范围筛选。漏收抽核连续发现相关题目，来源 Gate 仍未闭合。

### 第四轮标题关闭反向抽核

第四轮反向抽核：从仍未在账本出现的 `New` 标题按 ID 顺序取 `NR % 19 == 9`，浏览 31 个标题，8 个歧义题目读完摘要。`2609.24969` 的 agent stochastic trajectory 极低频失效估计，提出以权重扰动训练 importance-sampling proposal，可能改变安全尾部风险评价合同；须核采样分布的 likelihood、估计无偏性/方差、真实 agent 环境及失败定义，暂列独立准入复核。`2609.22351` 的 3D scene-graph 对象置信传播与本日 `2609.23144` 的 posterior graph 有同一知识问题，须先做机制去重；`2609.23131` 的 partial-observation 目标检索 belief 与 proceed/abstain、`2609.22213` 的 temporal KGQA evidence-space constraint 均需与现有 Agent/World belief 及 deterministic evidence gate 比较。`2609.22886` 只在视觉 checkpoint merge 上合成图像补训练，`2609.23733` 是 VGGT 专用 attention head 剪枝，`2609.24092` 是文档视觉多跳推导训练，`2609.24760` 是数学逆向思维数据训练；题摘未给本项目新的通用机制，候选前关闭。其余 23 个标题限定领域应用/通用方法，只做题目级范围关闭。该轮又发现真正应读的来源，故不能把抽检称零漏收或来源 Complete。累计 353 份摘要（351 New、2 Cross），652 个 New 仅题目级关闭。

### 第五轮标题关闭反向抽核

从账本未逐项记录的 `New` 标题按 arXiv ID 数字尾段取模 `23 == 7`，得到 15 个，逐题复看。其中 11 个标题已经明确限定为人类认知理论、卒中复发、古希腊文献修复、无线切换、物理信息网络、工业工单提取、字典学习、SAM 分割、约旦方言语音识别、医学 MRI 等非本项目核心，标题级关闭。对 4 个边界题目读完[官方摘要](https://arxiv.org/abs/2609.23881)：

- [2609.22133v1](https://arxiv.org/abs/2609.22133) 在 14 项政治学文本分类复制实验中比较人/LLM 标注分歧；其 ambiguity-aware codebook 与下游推断上界是该社会科学标注协议的结果。它提示人工标签也有歧义，但尚未改变本项目现有 Evaluation 的 annotator uncertainty / disagreement 边界，候选前关闭，不外推“LLM 与人类标注普遍等价”。
- [2609.23881v1](https://arxiv.org/abs/2609.23881) 指出 JEPA 的 slow-feature bias 可能压制运动表征，提出无动作标签的 difference-image embedding regularizer，并报告四个环境中静态背景干扰下的下游规划改善。它可能补充 `MULTIMODAL-REPRESENTATION` 静态/动态表征契约，但还须核与现有视频 shortcut、track-aligned state 主线的独立机制和真实大模型外推；仅保留标准审阅线索，不因 `world model` 标签直接准入。
- [2609.24088v1](https://arxiv.org/abs/2609.24088) 指出视觉 tokenizer 的 reconstruction-FID 与 generation-FID 可弱相关甚至负相关：encoder latents 与生成时 prior latents 分布不同；generation-aware reconstruction 用加噪/去噪轨迹诊断 decoder，并在中间 latents 上继续成对训练。`MULTIMODAL-REPRESENTATION` 已有“高重建保真不等于生成最佳”结论，这一训练/评估路径或有具体条件增量，但必须核匹配 generator capacity、多个 tokenizer/尺度和生成质量之外的代价；保留标准审阅，不能先写长期结论。
- [2609.24180v1](https://arxiv.org/abs/2609.24180) 是视觉抓取 proposal 之后以触觉 residual TCP 修正的受限机器人执行方案。`MULTIMODAL-EMBODIED-VLA` 已有 high-level proposal → low-level feedback controller 与 contact-state 责任边界；作者仿真/单 UR5e 设置未形成新的通用 VLA 控制合同，候选前关闭。

本轮 15 个标题中 4 个新增摘要阅读，累计 **357 份摘要（355 New、2 Cross）**；其余 **648 个 New** 仍仅标题级处理。新发现的 `2609.23881` 与 `2609.24088` 都先与书稿比对，不能将抽检发现的可读论文直接算入候选。反向抽核再次发现需要阅读的命名机制，证明“只看标题”尚不足以宣布来源 Gate Complete。

### 标题级关闭的主题摘要边界补检

对标题尚未逐项入账的 `New` 做第二条路线的**摘要文本检索**：以 LLM、Agent、World Model、VLA、GPU、KV、训练/推理等概念从宽原始集合产生 183 个未记录身份。它只是有界补检队列，**未读完 183 篇摘要，也没有将其自动入选**。从中选 6 个标题单看会误判的边界身份，重新打开官方 abs 并读完摘要，与现有 owner 比较：

| 身份 | 题摘判定及边界 |
| --- | --- |
| [2609.22462v1 VLPSA](https://arxiv.org/abs/2609.22462) | `MULTIMODAL-EMBODIED-VLA` 已把 VLA proposal 与真实 safety shield / contact authority 分离；本文 Poisson safety function + full-body CBF-QP 是可读的具体实现、含单 Franka FR3 实验，但不是首次提出独立安全控制权。标准审阅看感知延迟、动态障碍与硬约束是否成立；不因 `91.2%` 作者 SafeLIBERO 值直接写成普适安全保证。 |
| [2609.24308v1 HappyWorld-Bench](https://arxiv.org/abs/2609.24308) | `PLATFORM-EVALUATION-SYSTEM` 已区分 world-model 外观、状态一致、action response 与 intervention；该 suite 将 video/spatial/embodied 三轨并列，首先是受限 benchmark artifact，不提供新的通用评价责任边界；候选前 `No Change — Existing Coverage`，不把 Elo/单一 placement accuracy 解释为物理正确。 |
| [2609.24516v1 LLJ Cards](https://arxiv.org/abs/2609.24516) | 汇总 judge 测量有效性、可靠性、透明和可复现实践；`PLATFORM-EVALUATION-SYSTEM` 已持有这些评测责任，摘要不含独立新机制或反例，候选前关闭，不能把 guidelines 自动等同实验验证。 |
| [2609.24744v1 World State Generator](https://arxiv.org/abs/2609.24744) | 程序化世界中把 plan 写成 checkable state 并在失败后修复，落在 `AGENT-PLANNING` 已有 typed expected-state、环境回执与 observation-triggered replanning 主线。7 个 benchmark / 合成 226K trajectories 只支持该训练设置；候选前 `No Change — Existing Coverage`，不把模型自述 state 提升成环境事实。 |
| [2609.24812v1 MSI-Bench](https://arxiv.org/abs/2609.24812) | 双语多说话人语音 Agent 的 `speaker-scoped` 感知、指令归属、工具调用及不应答时的克制，可能补足 `MULTIMODAL-REPRESENTATION` 的 speaker provenance 向 `AGENT-TOOL-CALLING` 授权交接。先保留**标准审阅**，核干净 transcript 对照、speaker 绑定与工具 effect；摘要的 1,152 cases、通过率只限该 suite。 |
| [2609.24927v1 Economic Misalignment](https://arxiv.org/abs/2609.24927) | 经济推荐任务里环境上下文暗示的财富与用户明确 cheapest 指令冲突，拓展了 `AGENT-TOOL-CALLING` 已有 memory-to-field relevance gate 的反例范围。先作**标准审阅**，核 13 Agent / 325K 实验的随机化、同请求对照与用户目标度量；不能把财富相关差异直接称为所有 Agent 的故意违令，更不能据摘要修改安全结论。 |

这次补检又将题目级关闭中的 6 个身份升级为已读摘要，但只有 2 个留下标准审阅线索、4 个可由现有 owner 或缺乏独立增量候选前关闭。累计 **363 份摘要（361 New、2 Cross）**；**642 个 New** 仍仅标题级。摘要检索命中的其余 177 个身份未被逐项语义判定，故不能把本节写作已闭合的 183 篇审阅。

### Replacement 定点信号，不与本窗新投稿混算

560 个仅 Replacement 身份尚未逐项核完修订理由；对标题涉及大模型/Agent/推理的旧 family 先按官方列表 `Comments` 检索 `withdrawn / substantially revised / corrected / updated results` 等**信号**，得到 7 项需定点判断，不能据此称所有 replacement 已闭合。逐项检查后，[2606.08151v4](https://arxiv.org/abs/2606.08151) 的 camera-ready 明确修正 retrieval recall metrics：它是 2026-06 既有 Agent memory family 的**评价更正**，需回查此前报告/书稿是否使用旧数字，不是 09-23 新论文。[2609.16639v2](https://arxiv.org/abs/2609.16639) 官方页面明确 withdrawn（作者未达一致），直接排除，不进入 selected 或 Books。其余 `2609.15795` 仅改标题 typo、`2609.09646` 仅修 reference metadata、`2512.12989` 是后量子迁移领域评估、`2605.01457` 是一般 offline 多 Agent 决策、`2608.03921` 自述全稿改写但目前无可证本项目设计判断变化；不因修订声明自动计本窗候选。

对 12 类别 `Replacement submissions` 的官方列表 Comments 又做了**跨分类去重的修订信号扫查**，并抽开 abs，新增以下应回拨旧 owner 的事项，而非今日 New：

| 旧 Source Family / 修订入口 | 今日发现的具体 correction/evolution 信号；后续动作 |
| --- | --- |
| [2608.28021v2](https://arxiv.org/abs/2608.28021) | 官方 Comments 明确 v1 将多数设定过安全状态的 prompt 误称“只含功能要求”，导致原分析混淆遵循指令与模型默认安全配置；v2 按 prompt class 分层，pooled gap 未变。须检查 August owner 是否错误引用“unprompted defaults”，不以本窗新候选计分。 |
| [2606.22419v3](https://arxiv.org/abs/2606.22419) | 官方 Comments 指出图检索 engine 的三处 gap 已在 v1.8.0 修复并于 09-21 probe 验证，论文实验和结果不变。旧 owner 的系统限制描述如把软件缺陷写成算法固有限制，应纠正；今日仅修订信号。 |
| [2601.15322](https://arxiv.org/abs/2601.15322) | Comments 明言修正历史结果解释并澄清研究边界；需要在原 Source Family 审核版本改变的是何种 faithfulness 结论，不能沿用旧统计解释。 |
| [2602.13718](https://arxiv.org/abs/2602.13718) | 修订新增受控消融、真实机器人和 VLA 实验；给旧 February owner 的证据升级线索，不等于今天提出新机制。 |
| [2603.16859](https://arxiv.org/abs/2603.16859) | 官方 Comments 明示 evaluation protocol/results 已更新；旧 March owner 应按新版重新核比较条件，不能把旧版数字继续视作最终证据。 |

另外 [2601.14286](https://arxiv.org/abs/2601.14286) 和 [2606.14053](https://arxiv.org/abs/2606.14053) 在本批 Comments 均标撤回，但分别是电路映射和统计方法，不属于本项目在本窗的新候选。上述扫查仅覆盖列表中显式修订/撤回/纠错说明；沉默 Comments 不能证明 560 个 replacement 均无实质变化，因此仍需按项目主题而非全量全文做收尾核验。

### Cross-only 的首发归属恢复

183 个仅出现在 `Cross submissions` 的身份不能按本日 New 重计。标题主题补检发现 `2609.22486`（Agent Web retrieval 基建）、`2609.22510`（trigger prompt injection）、`2609.22547`（RLVR pass@k 统计）、`2609.22818`（Agent memory-poisoning defense 的 benign-cost）、`2609.22949`（多 Agent prompt injection）、`2609.23315`（Agent graph memory 系统成本）、`2609.23570`（真实 repository coding memory）、`2609.23925`（MCP workflow benchmark）、`2609.24446`（Agent policy-constrained action validation）为值得按首次公开日期回拨的主题信号；其中后两者和 `2609.22486` 并未完成摘要审阅，不能据此宣称它们对项目有贡献。当前已读的 `2609.22547` 与 `2609.23570` 保持 Cross-only，不计今日候选。若发现原 owner 缺失，应在该日报另行核验，不在 09-23 追加分数。

## 精确续跑位置与不得声称之事

### 初批 34 项的贡献准入复判（仅题摘与现有 Books 对照）

下表把上文 23+11 个“优先阅读线索”逐项收窄；“标准审阅”仍**不是**冻结候选或 Books 决定，只表示存在可核的边界条件。`No Change` 是候选前判断，独立 reviewer 可凭正文反证重开。已完成的四项 Deep Review 由报告 owner 管理；本表不冒充再次全文审阅。

| Source Family | 本轮边界判断 |
| --- | --- |
| `2609.22101` | 标准审阅：长上下文干扰项数/aliasing 可能细化 `MODEL-LONG-CONTEXT` admission 边界；不能仅凭摘要覆盖现有 distractor/检索门控。 |
| `2609.22109` | 候选前 `No Change`：selector 与 learning rate 的交互已由 `TRAIN-RLHF` 的 matched LR 对照责任承载；只在作者设置中有新 selector 排序。 |
| `2609.22157` | 标准审阅：逐输入 KV eviction 失败 gate 可细化 `INFER-KV-CACHE` 的 cache budget/fallback，但需核批量下真实 compression，不能把 nominal 16× 当节省。 |
| `2609.22183` | 候选前 `No Change`：污染审计的 null 并非无污染证明；`PLATFORM-EVALUATION-SYSTEM` 已有受控 contamination–response 与不确定区间责任，单篇表面改写实证不改变合同。 |
| `2609.22231` | 候选前 `No Change`：memory encoding/retrieval/generation 分层诊断与 `AGENT-MEMORY`/`PLATFORM-EVALUATION-SYSTEM` 的 trace/evidence attribution 同义；具体 suite 可保留报告。 |
| `2609.22512` | 候选前 `No Change`：`PLATFORM-EVALUATION-SYSTEM` 已反复约束 judge 相关误差、有效样本量及人工/独立 evaluator 回退；相关性测量是受限证据而非新分权。 |
| `2609.22755` | 标准审阅：长尾长度分布下 nested SP group 可能是 `TRAIN-DISTRIBUTED-TRAINING` 现有分组/placement 的新执行点；需分离通信和重计算，不按并行术语自动准入。 |
| `2609.22870` | 已由报告 owner 完成独立 Source Review 与 `TRAIN-GRPO` Books 判断；不在本账本重复。 |
| `2609.23252` | 标准审阅：绝对/相对 action 编码不变性可能界定 `MULTIMODAL-WORLD-MODELS` 的 transition input identity；须核同任务可逆重参数化与真实控制，而非从一种编码优于另一种推普遍结论。 |
| `2609.23536` | 已由报告 owner完成独立 Source Review 与 Books 判断；不在本账本重复。 |
| `2609.23816` | 标准审阅：高带宽 flash 下 KV placement/稀疏读取是否改 `INFER-GPU-MEMORY` 成本前沿，取决于实机硬件和 TTFT/TPOT/SLO；摘要 headline 不是通用层级反转。 |
| `2609.24122` | 标准审阅：生产 RAG coverage 在缺失标注下的估计方式或能补 `PLATFORM-EVALUATION-SYSTEM` 的 retrieval oracle 边界；需核 human/judge 验证，不能从检索器自报推 coverage。 |
| `2609.24130` | 候选前 `No Change`：Agent 自改 harness 的非回归、独立 gate 和 rollback 已在 `PLATFORM-EVALUATION-SYSTEM` 与 `AGENT-PLATFORM`；此篇只作受限实现对照。 |
| `2609.24456` | 标准审阅：experience buffer placement/delivery/scheduling 可能细化 `TRAIN-DISTRIBUTED-TRAINING` RL 数据面，但需证明在 LLM rollout/learner 上的状态与吞吐边界。 |
| `2609.24639` | 候选前 `No Change`：`INFER-PD-DISAGGREGATION` 已联合 P/D ratio、power cap、queue、KV 与 tail SLO；作者解析模型只能作特定部署证据。 |
| `2609.24663` | 候选前 `No Change`：Agent 自演化按阶段记录 regression/旧任务与独立 holdout 已由 `PLATFORM-EVALUATION-SYSTEM` 承载；benchmark artifact 可在报告说明，不增写原则。 |
| `2609.24749` | 标准审阅：实际 action outcome 是否比预测相似更能训练 decision-local latent，可能是 `MULTIMODAL-WORLD-MODELS` 的具体优化路线；需分离真实机器人与模拟器，并与已知 action-utility ≠ visual fidelity 区分。 |
| `2609.22674` | 标准审阅：M-JEPA 多 mask 的共享 target/context 与 sparse routing 是 `TRAIN-PRETRAINING` 的计算复用候选，只有等价性及端到端节省可核时才超出局部 kernel 改进。 |
| `2609.22991` | 候选前 `Version Fact`：PyTorch MPS 大张量沉默错误如属实需版本/shape/dtype 回归，`INFER-TENSORRT-LLM` 已有执行栈数值正确性 gate；单 backend 事故不另造长期机制。 |
| `2609.23278` | 候选前 `No Change`：`TRAIN-DISTRIBUTED-TRAINING` 与 `PLATFORM-EVALUATION-SYSTEM` 已要求 simulator 随 placement 计算 NIC contention/JCT；新 trace 只在实际拓扑合同中成立。 |
| `2609.23301` | 候选前 `No Change`：`PLATFORM-TRACE` 已明确跨节点 clock skew 可以反转因果顺序；PTP/GPU 时间戳是实现证据，不将仿真大集群视为实测。 |
| `2609.24161` | 标准审阅：MCP 接口粒度可能改变本地模型的工具选择/参数错误，属 `AGENT-MCP` 的接口实验；需核四种接口可比性，不能将一组小模型迁移为通用粒度规则。 |
| `2609.24991` | 标准审阅：KV/shared serving 的 K8s/gateway/provider 多账本归属可能细化 `PLATFORM-COST`；需区分真实 H100 局部实验与合成账单，不能把 token count 当财务真值。 |
| `2609.22254` | 标准审阅：teacher continuation 长度的轨迹偏差/监督方差可能是 `TRAIN-RLHF` 的预算选择点；须先与本日其他 OPD 论文去重，查更早公开日期。 |
| `2609.22867` | 候选前 `No Change`：denoising steps 非均匀预算是 `MULTIMODAL-GENERATIVE-PARADIGMS` 已有迭代质量/延迟分支；本文图像 workload 的步长优化不改生成范式。 |
| `2609.23457` | 标准审阅：rubric 若按序而非基数线性合并，或细化 `TRAIN-RLHF` 多目标/硬约束分权；需核 objective、reward credit 与对照，不将单个 reasoning benchmark 外推。 |
| `2609.23585` | 候选前 `No Change`：量化后 head 稳定性与 top-k/head 策略在小模型上不一致，属于 `INFER-KV-CACHE` 已有量化/eviction 校准与回退，未单独改变 owner。 |
| `2609.23916` | 标准审阅：按时间增量预训练时 URL overlap 对训练/评估 cutoff 的影响，可细化 `TRAIN-DATA` lineage；需核时间标签与泄漏，不预设 LoRA/full CPT 优劣。 |
| `2609.24141` | 候选前 `No Change`：teacher call 与 student update 预算解耦及 stale/off-policy 风险已属 `TRAIN-RLHF`/`TRAIN-SFT` 的 state/teacher identity，作者成本点不单独成机制。 |
| `2609.24322` | 已由报告 owner 完成独立 Source Review 与 Books 判断；不在本账本重复。 |
| `2609.24432` | 候选前 `No Change`：按 token 的 teacher 信号贡献分配与 `TRAIN-SFT`/`TRAIN-GRPO` 的 token selection 主线重合；所谓 1% 只属于披露的 teacher/student/预算。 |
| `2609.24646` | 标准审阅：teacher 信息注入量与 frozen base anchor 的组合或给 `TRAIN-SFT` 分布覆盖/遗忘边界新证据；须核 teacher confound，不能称通用蒸馏公式。 |
| `2609.24698` | 候选前 `No Change`：压缩 attention 的 branch-local tree state/accepted path commit 已在 `INFER-SPECULATIVE-DECODING`；所谓厂商模型 artifact 未核，不能升级为官方系统事实。 |
| `2609.24974` | 候选前 `No Change`：训练与部署 harness 的 model–harness 配对身份/迁移失配已在 `AGENT-PLATFORM`；实验可供标准 evidence 对照，但不另增原则。 |

按此复判，初批 34 项中 3 项由报告 owner 已完成 Source Review/Books 判断，15 项仅保留有条件的标准审阅线索，16 项候选前 `No Change / Version Fact`。这个划分不包括后续主题补检和报告 owner 另行纳入的 `2609.23478`；也不代表 15 项已通过证据 Gate。下一个可执行批次只需审阅这些线索的**具体新条件**，若无新增则关闭，不应并行把 15 项全部升为候选。

### 初段 24 项“待裁决”题摘的准入复判

以下只判**是否有值得再审的具体贡献假设**，不构成全文事实认证。前文“准入待裁决”保留原阅读历史，本表是后续最新处置；相同 family 不能在两个位置分别计数。

| Source Family | 最新筛选处置 |
| --- | --- |
| `2609.22098` | 候选前关闭：draft tree 预算/验证吞吐的优化点在 `INFER-SPECULATIVE-DECODING` 已有 branch budget 与 accepted-token correctness。 |
| `2609.22100` | 候选前关闭：RAG soft-memory quota 是 `AGENT-RAG`/`AGENT-MEMORY` 既有检索—容量取舍的一个实现，没有新的 authority。 |
| `2609.22106` | 候选前关闭：量化 residual 物理布局属于 `INFER-TENSORRT-LLM` kernel artifact 的局部选择，题摘未显示跨 backend 新执行合同。 |
| `2609.22114` | 候选前关闭：多轮 coding Agent 压缩成本/正确性比较属于 `AGENT-CONTEXT` 已有压缩-证据 lineage 边界。 |
| `2609.22156` | 候选前关闭：MoE draft/target 路由差异及接受率、通信权衡由 `MODEL-MOE` 与 `INFER-SPECULATIVE-DECODING` 承载。 |
| `2609.22158` | 候选前关闭：step-level KV 留存是 `INFER-KV-CACHE` 粒度/回退实现，摘要未提出新的 state owner。 |
| `2609.22335` | 候选前关闭：VLA GPU kernel 并发的受限性能点依赖具体 action rate/设备，`MULTIMODAL-EMBODIED-VLA` 已要求闭环 latency 控制。 |
| `2609.22471` | 候选前关闭：expert coactivation 用于预取/placement 的线索已由 `MODEL-MOE`/`INFER-GPU-MEMORY` owner 分权。 |
| `2609.22884` | 候选前关闭：稀疏注意力路由与 fallback 属 `MODEL-LONG-CONTEXT` 已有 selector/coverage 机制，摘要未给独立系统合同。 |
| `2609.22888` | 标准审阅：真实机器人在线 VLA 后训练若改变 safety envelope、effect receipt 或 rollout-to-update identity，才可能超出 `MULTIMODAL-EMBODIED-VLA` 现有边界；不能从任务成功率自动准入。 |
| `2609.23033` | 标准审阅：looped LM wavefront 可能改变迭代状态的跨 step 执行调度；需核生成语义等价、跨阶段 cache 和端到端延迟，不按新算法名准入。 |
| `2609.23085` | 候选前关闭：能耗感知模型路由与质量/SLO 权衡已归 `PLATFORM-COST`、`INFER-SCHEDULING`；作者一组负载不是新原则。 |
| `2609.23130` | 候选前关闭：vLLM/llm-d 综述不是新的 primary mechanism；可用于发现旧来源，不能当本窗新论文证据。 |
| `2609.23314` | 候选前关闭：sink-suppressed KV eviction 的特定选择器仍属 `INFER-KV-CACHE` 现有 salience/eviction/fallback。 |
| `2609.23790` | 候选前关闭：多 Agent 共享/复制记忆的成本已在 `AGENT-MEMORY` 与 `AGENT-MULTI-AGENT` 的 owner 边界。 |
| `2609.24089` | 候选前关闭：Attention double-backward kernel 的局部吞吐仍需目标硬件验证，未给 `TRAIN-DISTRIBUTED-TRAINING` 新状态语义。 |
| `2609.24150` | 候选前关闭：按接受率训练 draft 的目标已由 `INFER-SPECULATIVE-DECODING` 承载；作者结果仅是一个训练 operating point。 |
| `2609.24197` | 标准审阅：不维持 drafter KV 的并行 speculation 或改变 cache ownership；需核 target-equivalent sampling 与真实内存/吞吐净收益。 |
| `2609.24270` | 标准审阅：GPU die 不对称 placement 可细化 `INFER-SCHEDULING`，仅当物理 locality/迁移成本令旧均质假设失效才是系统增量。 |
| `2609.24298` | 候选前关闭：KV 的 bit-rank 分配是既有 KV 精度/容量/误差预算的层级实现，题摘不足以改变 release gate。 |
| `2609.24635` | 候选前关闭：operation token 的 KV 表示变换仍需同请求正确性与 cache identity；摘要没有独立于 `INFER-KV-CACHE` 的新边界。 |
| `2609.23321` | 标准审阅：真实 diffusion 服务日志中的 LoRA adapter 共现可验证 `INFER-GPU-MEMORY` placement/caching 条件；观察性相关不证明预取策略因果收益。 |
| `2609.24205` | 候选前关闭：训练瓶颈阶段调 GPU 频率是 `PLATFORM-COST` 现有 phase/power-cap 思路；官方 abs 可读性障碍不影响低贡献关闭，不把论文性能数字带入报告。 |
| `2609.24847` | 候选前关闭：FPGA speculative GEMV/GEMM tile 重构属于专用硬件执行点；`INFER-TENSORRT-LLM` 已拥有跨硬件执行规划，摘要未证明一般新控制权。 |

本批 24 项为 **5 项标准审阅、19 项候选前关闭**。关闭不是称论文错误，而是未越过本项目长期机制门槛；5 项也不能未经精确首发/正文审阅进入冻结分母。

### 训练/推理增量批 23 项“待比较”题摘的准入复判

| Source Family | 最新筛选处置 |
| --- | --- |
| `2609.22091` | 候选前关闭：prospective memory 的特定任务数据/指标未给 `AGENT-MEMORY` 新读写 authority。 |
| `2609.22145` | 候选前关闭：diffusion LM 生成数据检测是来源鉴别任务，未改变 `TRAIN-DATA` 数据身份或生成机制。 |
| `2609.22146` | 候选前关闭：12 条 post-training chain 的 SVD update 几何是解释性观察，删除 diagonal 后仍有 gain 不证明应这样设计训练或适用于其他模型。 |
| `2609.22178` | 候选前关闭：CUA safety/capability suite 的能力事实需要各自风险/动作合同，题摘未提供新的 `PLATFORM-EVALUATION-SYSTEM` 机制。 |
| `2609.22194` | 候选前关闭：广告 Agent 的 SFT/RL 阶段是领域工作流，未改变本项目训练权责。 |
| `2609.22206` | 标准审阅：多模态不确定性若区分视觉 evidence 缺失与推理不确定，可细化 `PLATFORM-EVALUATION-SYSTEM` 的校准 slice；先核 evaluator 与 abstain contract。 |
| `2609.22452` | 候选前关闭：长语音 benchmark 首先是任务集，`MULTIMODAL-REPRESENTATION` 已区分 acoustic/semantic state 与时间对齐；仅按新测试集不准入。 |
| `2609.22566` | 候选前关闭：synthetic environment 下依 teacher 预测不变性重权蒸馏在 MNLI/QA/NER/情感分类中受限；`TRAIN-SFT` 已有 teacher reliability/gating，不能把 invariance proxy 当因果证书。 |
| `2609.22603` | 候选前关闭：摘要事实性 scaffold 的局部评价不超出 `PLATFORM-EVALUATION-SYSTEM` claim/evidence 拆分。 |
| `2609.22684` | 候选前关闭：VLA 单一 state token 是表示设计点，未证明 `MULTIMODAL-EMBODIED-VLA` 的可观测性/控制反馈分权改变。 |
| `2609.23055` | 候选前关闭：diffusion optimizer 的受控比较有再现价值，但同一图像训练设置的优化器排序不是 Part III 长期生成范式。 |
| `2609.23205` | 候选前关闭：数学 sycophancy 场景的表现与修正属于评估任务，不建立模型 self-knowledge 新机制。 |
| `2609.23215` | 候选前关闭：AIF 电网代理的 LLM explainer 在污染观测、错误行动及 metadata injection 下叙述失真；`PLATFORM-SECURITY` 已规定 reasoning/explainer 是低信任 observation，不拥有事实/动作批准权。作者未评缓解方案，不能引用为修复证据。 |
| `2609.23449` | 候选前关闭：Agent 记忆蒸馏的具体训练方案仍需记忆来源/撤销/授权身份，摘要没有 `AGENT-MEMORY` 新状态边界。 |
| `2609.23697` | 候选前关闭：多个 teacher 的 OPD 聚合仍处于 `TRAIN-SFT` 已有多 teacher debate/privileged distribution 分支。 |
| `2609.23716` | 候选前关闭：prompt 自修订需 frozen regression gate 与独立 outcome，已在 `AGENT-REFLECTION`/`PLATFORM-EVALUATION-SYSTEM`。 |
| `2609.23742` | 候选前关闭：schema 合规 ≠ 语义正确是 `AGENT-TOOL-CALLING` 已有 parser/business-validation 分权。 |
| `2609.24196` | 标准审阅：looped LM 的 decoding 调度需与同日报 `2609.23033` 去重，只在状态重用/commit 语义新且端到端可测时有独立增量。 |
| `2609.24202` | 候选前关闭：稀疏注意力 token 群聚解释不是新的选择器 admission、coverage 或 fallback 机制。 |
| `2609.24303` | 候选前关闭：用 pretrained base 作为 label-free calibration 参照、加权 disagreement，在有限分类数据上降低 ECE；`PLATFORM-EVALUATION-SYSTEM` 已要求 post-train artifact 重新校准，参考模型置信不是真值。 |
| `2609.24379` | 候选前关闭：topographic circuit 的表示分析未形成可操作的模型/系统设计判断。 |
| `2609.24799` | 候选前关闭：医疗量化的解释/正确性仅限临床任务，现有量化 release gate 已要求 item-level 与 safety slices。 |
| `2609.24942` | 候选前 `Disputed — Theory Scope`：把 OOD 泛化必要条件扩成“必须精确实现生成机制”是广泛理论主张，摘要中的 Tensor Logic/封闭域例子不足以证成所有深度模型的必要性；不能进入 Books 结论，若日后重开须核定理前提和反例。 |

本批 23 项为 **2 项标准审阅、21 项候选前关闭或理论范围争议**。这不判论文整体价值，只把缺乏本项目设计增量的任务/观察与真正可检验的系统条件分开。

### 后续专题“优先”题摘的强剪枝

以下复判只使用已读题摘、相邻来源去重及当前 Books 的既有命题；题摘可提出需要核验的设计差异，不能证明机制/benchmark。报告 owner 已独立推进的 `2609.23478`、`2609.24362`、`2609.22478`、`2609.24048` 另行裁决，本表不覆盖其结论。

| Source Family | 最新筛选处置 |
| --- | --- |
| `2609.22218` | 候选前 `No Change`：万级工具目录先检索再装载 schema 属 `PLATFORM-GATEWAY`/`AGENT-TOOL-CALLING` 已有授权目录与候选工具检索。 |
| `2609.22223` | 标准审阅：长文 claim 依赖图与 evidence 复用或细化 `PLATFORM-EVALUATION-SYSTEM` 的相关错误估计；需核分组错配和搜索成本，不把 claim 视独立 Bernoulli。 |
| `2609.22592` | 候选前 `No Change`：先有可执行 verifier 再生成 Agent gym 与 `MULTIMODAL-EMBODIED-VLA`/`PLATFORM-EVALUATION-SYSTEM` 的环境 validator 分权一致。 |
| `2609.23058` | 候选前 `No Change`：Agent 程序按需 materialize 是 `AGENT-WORKFLOW` 的惰性执行分支，正确性仍由 tool outcome 与副作用合同持有。 |
| `2609.23806` | 标准审阅：task 选定前冻结组织可见状态可阻断 benchmark context 选择捷径；需核合成公司以外的可迁移证据，或仅属既有 holdout/frozen-context 规则。 |
| `2609.24985` | 标准审阅：多轮工具 RL 将可行动 reward variation 与环境噪声分开，或细化 `TRAIN-GRPO` credit estimator；需核同状态反事实及 BFCL-v4 的 teacher/judge 条件。 |
| `2609.22293` | 标准审阅：VLA 图像扰动的 sound validation 若有明确扰动域/证书，可能比普通随机 robustness test 强；必须核传感现实边界，不从局部数学证书推真实安全。 |
| `2609.22582` | 标准审阅：驾驶行人避让的成对编辑场景可能成为 `MULTIMODAL-EMBODIED-VLA` decision-causality test；须核编辑保真、open-loop/closed-loop 及人类对照。 |
| `2609.22641` | 候选前 `No Change`：peer-view 可见性路由是 `MULTIMODAL-WORLD-MODELS` 已有多主体 latent/action stream 与共享 state 的具体实现。 |
| `2609.22858` | 候选前 `No Change`：observed belief 与 imagined state 分权、真实 observation 才能提交事实，是 `MULTIMODAL-WORLD-MODELS` 核心命题。 |
| `2609.23910` | 候选前 `No Change`：real-to-sim 几何质量不能直接保证 policy ranking 可迁移，已属 `PLATFORM-EVALUATION-SYSTEM` sim-to-real outcome contract；本篇可作特定证据。 |
| `2609.24274` | 候选前 `No Change`：CPU VLA action-chunk 供给、控制频率、热约束已在 `MULTIMODAL-EMBODIED-VLA`；六策略四 CPU 是受限 operating point。 |
| `2609.24350` | 候选前 `No Change`：camera staleness/provenance 与任务前提变化属于 `MULTIMODAL-EMBODIED-VLA` 的 observation freshness / closed-loop contract。 |
| `2609.24433` | 标准审阅：W4A4 校准表示与执行表示一致、关键层回退，或补 `INFER-TENSORRT-LLM`→VLA 闭环的质量边界；需核精度、设备、实机 trial，不能凭加速题摘准入。 |
| `2609.24682` | 标准审阅：World Model latent 离线蒸馏成低时延 VLA，与在线 imagination 的成本分支不同；需核 teacher-only 信息泄漏与真实控制收益。 |
| `2609.24984` | 候选前 `No Change`：固定 token 预算的跨视角 3D memory 属 `MULTIMODAL-WORLD-MODELS` 既有持久 state / revision 责任；需在报告限定静/动态场景。 |
| `2609.22120` | 候选前 `No Change`：state-conditioned walkthrough 的读写、依赖切片和 provenance 属 `AGENT-MEMORY` 已有派生记忆 lineage 与失效处理。 |
| `2609.22200` | 标准审阅：跨轮同一 PII 实体的复合泄漏可能细化 `PLATFORM-SECURITY` 会话级风险计量；需核实体 join/防护条件，不能按独立单轮风险相乘。 |
| `2609.22222` | 候选前 `No Change`：工具执行成功不等于统计结论正确，已由 `AGENT-TOOL-CALLING` 的 output/business-verification 与 `PLATFORM-EVALUATION-SYSTEM` evidence gate 分权。 |
| `2609.22819` | 标准审阅：历史工具日志的 support 缺口让未见动作缺反事实证据；可细化 `AGENT-TOOL-CALLING` 的 offline policy gate，但需核 estimator 假设与授权。 |
| `2609.23053` | 候选前 `No Change`：答案正确但引文未被实际使用，已由 `AGENT-RAG`/`PLATFORM-EVALUATION-SYSTEM` 的 citation faithfulness 与反事实 evidence test 承载。 |
| `2609.23121` | 候选前 `No Change`：图像上下文一次性分支、文本主线持久，是 `AGENT-CONTEXT` 的 modality provenance 与可撤销 active context。 |
| `2609.24144` | 标准审阅：成对 rollout 的 reward contrast 方差不等于 policy-gradient 方差；可能修正 `TRAIN-GRPO` 的 estimator 选择，须核推导与 matched training evidence。 |
| `2609.24259` | 候选前 `No Change`：反事实 memory credit 可作为 `AGENT-MEMORY` 读写诊断，但记忆是否影响终局仍由外部 outcome 验证。 |
| `2609.24971` | 候选前 `No Change`：长历史固定成本/延迟的 memory suite 只实例化 `PLATFORM-EVALUATION-SYSTEM` 既有 workload/evidence contract。 |
| `2609.22234` | 候选前 `No Change`：跨图文的指令层级/视觉 prompt injection 已由 `PLATFORM-SECURITY` 不可信模态入口及 action gate 持有。 |
| `2609.22283` | 标准审阅：streaming video diffusion 消费未完全去噪历史帧，可能改变 `MULTIMODAL-GENERATIVE-PARADIGMS` 迭代依赖图；须核训练-推理匹配和端到端时延。 |
| `2609.22361` | 标准审阅：音视频共因 latent 的外观 shortcut 需反事实干预；可能细化 `MULTIMODAL-REPRESENTATION` 静/动因素分离，但须核可识别性和 pretrained generator。 |
| `2609.23153` | 标准审阅：稀疏 video diffusion 的 step-local loss 与 terminal sample 分布不一致，或细化生成训练目标；`265×` 不含同负载端到端条件则不能引用。 |
| `2609.23900` | 候选前 `No Change`：`INFER-SPECULATIVE-DECODING` 已有 GDN/Attention branch-local recurrent state、accepted path commit；作者仓库更早实现不能按今天重复计新机制。 |
| `2609.24881` | 候选前 `No Change`：黑盒 API 外置 confidence calibrator 是 `PLATFORM-EVALUATION-SYSTEM` 已有校准 sensor/abstain 分权，AUROC 不是真实 claim-level confidence。 |
| `2609.22122` | 候选前 `No Change`：跨设备 ranking 与目标设备 latency+energy 可行性是 `PLATFORM-EVALUATION-SYSTEM` 已有 hardware/workload/SLO contract；13 设备 HW benchmark 是受限案例。 |
| `2609.23490` | 候选前 `No Change`：多语言 Agent 工具语义、控制流及成本分轴是 `PLATFORM-EVALUATION-SYSTEM` 的 task equivalence，不因 23 语言 suite 新增 owner。 |
| `2609.24165` | 候选前 `No Change`：模型叙述不等于执行回执，外部 deterministic guard 已由 `AGENT-TOOL-CALLING` 和 `AGENT-WORKFLOW` 持有。 |
| `2609.24797` | 候选前 `Disputed — Theory Scope`：Kimi Delta Attention gate/range 的表达力定理需精确假设与真实 LM scale，不能从形式表达等价推部署可训练稳定性。 |
| `2609.24967` | 标准审阅：多 Agent 长期共享日志下的 reward collusion 可能给 `AGENT-MULTI-AGENT` 新对抗样本；须核 peer intervention/历史截断与外部 reward owner，不能从少量仿真推生产频率。 |

本表将后续专题已标“优先”的 **36 项**压为 **14 项标准审阅、22 项候选前关闭或理论争议**；另有 `2609.24362`/`2609.22478` 已由报告 owner 定点审查，不重复计入本表。标准审阅只对列明的差异做 source-family/现有 owner 对照，不按“新 benchmark/新方法”批量升为候选。

### 后续专题普通“待比较”题摘的封口

这里的题摘已经在上文实际阅读，但未达到“仅因主题相关就进入分母”的门槛。为避免重复堆表，按其既有 owner 和仍需核验的**具体新增条件**封口；同一行只对所列 family 生效。

**Agent/Evaluation 9 项。** `2609.22111` 的论文—代码—实验一致性属于 `PLATFORM-EVALUATION-SYSTEM` 的 artifact lineage；`2609.22247` 的 harness 版本迁移已是 `AGENT-PLATFORM` 的 model–harness 配对身份；`2609.22259` 是 Text-to-SQL 域内 scaffolding；`2609.22599` 的 judge 表面扰动已是 Evaluation robustness slice；`2609.23465` 的 evidence→active memory commit 已是 `AGENT-MEMORY` 权责；`2609.24264` 的 trace action annotation 仍需外部 outcome 才算正确；`2609.24890` 的 CUA 子目标过程分数仍是已有 process-vs-outcome 分权——这 7 项候选前关闭。`2609.22587` 的事件触发异步 VLA 推理保留标准审阅，核控制频率与 stale observation 处理；`2609.24972` 的自演化 harness 先与 `2609.24130` 同家族机制去重，仅在有新可执行变更许可/独立 gate 时标准审阅。

**World Model/VLA 16 项。** `2609.22285` 虚构规则迁移是受控 pretraining task；`2609.22879` 不确定 rollout 采样、`2609.23650` 外观/语义 action response 区分、`2609.23753` 同状态不同动作模拟查询、`2609.24033` 未来预测残差作信心、`2609.24124` 主动感知写入和 `2609.24547` predict-more-than-commit，均已落在 `MULTIMODAL-WORLD-MODELS`/`MULTIMODAL-EMBODIED-VLA` 的 imagined-vs-observed、active observation、proposal-vs-action commit；`2609.22973` 是 VLA 联邦微调 operating point；`2609.23578` 是预定义原子技能的接口变体；`2609.23614`、`2609.23968` 是同一触觉/接触控制边界的实现选择；`2609.24170` 是通用 LLM robot policy 的受限能力评价；`2609.24313` 是 dynamics operator 局部跨场景表征——这 13 项候选前关闭。`2609.22840` 的 human intervention 时刻残差 TD credit 可能改变 online VLA feedback contract；`2609.24271` 的部署后经验演化需拆分组件贡献与安全 gate；`2609.24815` 的 action-conditioned streaming video 需证明 simulator latency/physical consistency，三者仅保留标准审阅。

**Agent/Information-State 15 项。** `2609.22682` 的自组织多 Agent、`2609.22880` 的 reranker 跳过门控、`2609.22943` 的 prompt/response token 选择、`2609.22951` 的 step-level model router、`2609.23466` 的 LoRA 参数化记忆、`2609.23512` 的适配配置验证、`2609.23808` 的 coding Agent dense reward、`2609.23986` 的记忆/控制双平面、`2609.24115` 的合成工具场景、`2609.24238` 的模型记忆/上下文事实区分、`2609.24290` 的澄清式提问信息增益与 `2609.24662` 的多 Agent 安全评价，分别已落入 `AGENT-MULTI-AGENT`、`AGENT-RAG`、`TRAIN-DATA`、`INFER-SCHEDULING`、`AGENT-MEMORY`、`PLATFORM-EVALUATION-SYSTEM`、`TRAIN-GRPO`、`AGENT-PLANNING` 或 `PLATFORM-SECURITY` 既有控制/证据主线；题摘没有与其相反的系统命题，这 12 项候选前关闭。`2609.22162` 的跨客户端 latent/隐私、`2609.23989` 的持续学习状态迁移、`2609.24983` 的 token-level on-policy correction，只有证明新 privacy/rollback/estimator 边界才标准审阅，先不准入。

**Model/Multimodal/Execution 8 项。** `2609.22107` 的 12 模态合成融合、`2609.22135` 的 probe-best/steer-best 分层、`2609.22243` 的状态索引 replay 授权、`2609.22916` 的 AR layout+diffusion renderer、`2609.23715` 的视觉 token prune 后位置补偿，分别是受限表示、白盒分析、既有 effect authorization、生成 hybrid、位置保留的实现，候选前关闭。`2609.22199` 跨层共享专家池的路由/权重共用是否造成新的 `MODEL-MOE` capacity/communication 约束、`2609.23658` 对视频物理错觉归因 RoPE 衰减的跨架构因果性、`2609.24346` diffusion 生成过程中实体稳定时触发 RAG 的检索/rollback 正确性，保留标准审阅，但不凭论文新名推一般规则。

**Mechanism 9 项。** `2609.23363` 的 RTL post-PnR evaluator、`2609.23580` 的 VLA 单标量任务阶段、`2609.23601` 的 256 KiB 视频 memory、`2609.23888` 的无触觉 student 蒸馏、`2609.24071` 的图表结构/证据 reward、`2609.24563` 的特定 Real2Sim2Real 数据工厂与 `2609.24875` 的单 A6000 VLM low-bit GEMV，仍是已知 owner 的领域或单硬件实例，候选前关闭。`2609.23841` 的机器人搜索持久 graph 是否在真实 observation 后修订 state authority、`2609.24417` 的固定大小 routed KV memory 是否在 exactness/压缩/写入一致性上超出现有 cache/recurrent contract，保留标准审阅；前者不能把 CityNav 等任务结果外推开放世界。

上述 **57 项**中，按本次题摘复判为 **13 项标准审阅、44 项候选前关闭**；无一因“待比较”或审阅工时自动进入候选分母。标准审阅如只重复现有原则，结论应为 `No Change`，不强求 Books 增量。

### 第二轮贡献剪枝：把 49 条“标准审阅”变成有限复核任务

上面五组的 49 条“标准审阅”只是初筛保留，不等于 49 个贡献候选。重新对照现有章节命题与题摘可支持的差异后，**8 个身份对应 7 个有限复核问题**；另外 **41 个身份在候选前关闭**。这个第二轮裁决覆盖前面表格中的较早状态；独立审阅如发现反证可重开，不能把题摘裁决伪装成全文结论。

| 待定点核验的身份 | 只核这个可能改变长期判断的问题 |
| --- | --- |
| `2609.22223` | 长文原子 claim 的依赖/共享证据是否使独立置信汇总失效，并提供超出现有 Ch66 claim-evidence contract 的可操作估计，而不只是换一套 benchmark。 |
| `2609.22819` | 离线工具轨迹缺少未执行动作的 support 时，所提 estimator 是否改变 Agent tool policy 的 release gate；核反事实假设而非只看日志拟合。 |
| `2609.23033`、`2609.24196` | 作为**同一 looped-LM 解码问题**先互相去重：迭代 state 的波前执行是否改变 exact output/commit 和端到端调度，而非单一 kernel 排布。不得分开计两个候选。 |
| `2609.24144` | reward contrast 的采样方差与 policy-gradient estimator 方差是否确有不同；核推导及 matched RL 训练，若仅是一种 proxy 观察则候选前关闭。 |
| `2609.24197` | drafter 不持有 KV 的并行 speculation 是否改变 target 等价性、cache owner 与净内存收益；若只换 draft 实现则关闭。 |
| `2609.24967` | 多 Agent 共享日志是否形成现有单 Agent reward hacking 之外的跨主体串谋失效；核 peer intervention 与外部 reward owner。 |
| `2609.24991` | K8s/OpenCost/gateway/provider 多账本是否造成不可由现有 tenant/request tagging 解决的 shared-KV 漏归属/重算，且 token/time meter 的选择实质改变 chargeback；区分实测与合成账单。 |

其余 41 个身份在**题摘贡献 Gate**前关闭，family-specific 理由如下；这不是对论文正确性或所有未来用途的否定：

- `2609.22101` 长上下文干扰仍属已有 retrieval/admission pressure；`2609.22157` 的逐输入 KV gate、压缩比与 fallback 已由 Ch45 的 workload-aware eviction / regression / FullKV 回退承载；`2609.22755` nested SP 分组是已有长度异质性下 communication/placement 的执行选择；`2609.23252` 绝对/相对 action encoding 是已知 transition input identity 的测试变量；`2609.23816` 的 OpenHBF 是 **measured GPU kernels + modeled custom dies/HBF planes**，不是现成 HBF GPU 的生产实测，Ch45 已拥有 KV tier/page/sparse read 的原则，暂不因 3.5–11.4× 模型值改长期决策。
- `2609.24122` RAG 缺失证据的 coverage oracle 已在 Ch66；`2609.24456` experience buffer 位置/交付属于现有 RL rollout→learner 数据面，摘要没有新的 ownership；`2609.24749` action utility ≠ visual prediction fidelity 已在 Ch25/26；`2609.22674` 多 mask JEPA 计算复用是实现级 common-subexpression；`2609.24161` MCP 工具粒度是接口选择受限案例；`2609.22254` teacher continuation 长度、`2609.23457` ordinal rubric、`2609.24646` teacher injection/anchor 是已有后训练目标/预算分支的具体 operating point；`2609.23916` web crawl URL overlap 已属训练数据 provenance/cutoff 基线。
- `2609.22888` 在线 VLA 更新的干预、安全与 revision 已在 Ch26；`2609.24270` GPU die placement 是现有物理 locality/迁移成本调度的单硬件实例；`2609.23321` diffusion LoRA 共现是相关性 observation，未单独证明新 prefetch 决策；`2609.22206` 多模态不确定性/abstain 已由 Ch66 按 evidence slice 承载。
- `2609.23806` task 前冻结上下文重申 existing holdout；`2609.24985` 可行动 reward variation 仍须外部 outcome，题摘只是 credit proxy；`2609.22293` sound 扰动证书限已定义图像域，不能替代 VLA 真实 safety envelope；`2609.22582` 成对驾驶场景是现有 decision-causality 评价的实例；`2609.24433` W4A4 VLA 精度/硬件/动作质量是已有量化 release gate 的受限点；`2609.24682` world-latent teacher→fast VLA student 是已有离线蒸馏对在线 imagination 的成本分支；`2609.22200` 会话级 PII 组合泄漏已由 Security provenance/consent gate 持有；`2609.22283` streaming video diffusion 的噪声历史消费、`2609.22361` 视听共因 shortcut、`2609.23153` 稀疏 video denoising step-vs-terminal loss，均是 Ch23/24 已有表示、训练/生成 mismatch 的受限分支，不能从局部结果推通用范式变化。
- `2609.22587` 事件触发异步 VLA 与 Ch26 已有 observation frontier/staleness/latency deadline 同义；`2609.24972` 自演化 harness 与 `2609.24130` 的独立 gate/rollback 同问题；`2609.22840` 人类干预 credit 是现有 intervention-to-update identity 的受限 estimator；`2609.24271` 部署后经验演化仍由 Ch26 policy revision 与 controller veto 定义；`2609.24815` action-conditioned streaming video 尚未改变 simulator 与真环境的 authority 分界；`2609.22162` 跨客户端 latent 仅在现有 privacy/consent 下形成一个联邦实现；`2609.23989` 持续学习状态迁移受现有 checkpoint/revision gate 约束；`2609.24983` on-policy token correction 是已有 ratio/clip/estimator 选择；`2609.22199` 跨层专家共用属于 MoE capacity/communication 实例；`2609.23658` RoPE 视觉物理错觉的单一归因未建立跨架构因果性；`2609.24346` diffusion 中途 RAG 检索仍需既有 proposal/rollback 正确性；`2609.23841` 持久机器人 graph 的修订权已由 Ch25/26 observed/imagined state 分层承担；`2609.24417` fixed-size routed KV memory 是 Ch45 已有 exact window + latent L2/soft eviction 的另一编码，题摘没有新 exactness 或 commit 合同。

本次缩减不触碰日报 owner 已核验的 8 个 family。另由漏收抽核得到的 `2609.24088`（生成时 latent 分布 vs reconstruction 分布）与 `2609.24812`（speaker provenance → Agent tool authorization）保留**两项外部定点复核线索**；它们不在上述 49 条算术中，也不因被发现较晚就自动准入。`2609.23881` 静/动 JEPA 与 `2609.24927` 经济推荐仅保留现有 owner 的受限案例/Weekly Only 边界，不扩大本日报候选分母。

### 独立标题关闭抽核与个人身份近邻补查

报告 owner 从我提供的 20 个仅标题级 `New` 分层样本，独立读了官方快照中的完整摘要：19 个暂无明确项目贡献漏收，**`2609.22195` 是一次真正的标题级漏收**，但不是本日报的确认首发。该论文题摘提出：多个私有经历可映射到同一公开 profile，只有 profile 条件的策略在 lineage-discriminative 问题上有 `1/m` 的不可辨识上界；Agent 不仅要知道有证据的经历，也应承认未经记录的经历未知。它可能比 Ch77 已有的 episode/provenance 与 profile 分层更明确地定义“appropriate ignorance”验收，但题摘中的 **10,000 probes 是 planned**，不是已完成的模型实验样本；已披露的是 deterministic fixtures 和 pilot evaluations。其余 19 个不能因样本表现而外推所有标题关闭项无漏收。

跨渠道日期：作者[官方 SIT 页面](https://www.openkedge.io/paper/persistent-cognitive-identity/situated-identity-test) 已公开相同 profile-collision/appropriate-ignorance 命题，但未展示精确发布日期；其[官方 SITBench 仓库](https://github.com/openkedge/sitbench)当前公开，GitHub API 记录仓库 `created_at=2026-08-29T23:29:29Z`、最早 commit `ffe165a157e5206316fe70ac9bd12f275fe65b8a` 为 2026-08-30T00:04:28Z 且提交信息称论文以后附到 arXiv，次日之前已提交评测实现/结果。这强烈提示 09-23 的 arXiv 公告是旧思想的后续 artifact；但 commit 时间不单独证明当时仓库已经公开，作者页也没有可验精确首发。因此身份保持 **Date Hold / possible spillback**，不纳入 09-23 冻结分母或评分；应按确定的早期公开事件回拨真实 owner，并区分 arXiv exact-v1 的有限 pilot 与网页后来更新的结果。

按 `profile / persona / episodic / identity / ignorance / autobiographical / personal memory / life history` 对 1,003 个 `New` **标题**作近邻扩查，得 16 个身份（含上文已读的 `2609.22091`、`2609.22231`、`2609.24927` 和独立样本中的 `2609.22195`）。对标题歧义的 `2609.22112`、`2609.22204`、`2609.22255`、`2609.24979` 再读官方列表摘要：`22112` 是 250 用户、LaMP-7 风格去标识对个性化文本质量的受限 privacy trade-off；`22204` 是 15 名日本参与者的 personal-information inference pilot；`22255` 是 role-playing 的脚本化三层 persona，并未证明 episodic lineage；`24979` 是端侧 hypernetwork 生成 LoRA 的个性化实现。这四项均未呈现与 `22195` 同一 profile-collision/appropriate-ignorance EvalSpec 的新增贡献，先候选前关闭或交已有 privacy/edge owner；其余近邻标题限定了医疗、心理、视觉跟踪或一般 RL 任务，不因 `identity/persona` 字样准入。此处只说明**标题邻域**已补检和上述 4 份新摘要确实阅读，不宣称 16 份摘要全部读完。合计摘要实读 **387（385 New、2 Cross）**，仅标题级 `New` 剩 **618**。

### 最小定点准入复核：不再扩张候选分母

从上节 8 个身份/7 个问题及外部 2 条线索中，只把下列**四个**问题交给报告 owner 做 exact-version Source Review 与 Books Decision；这是筛选准入建议，不是已确认的日期归属、分数或完成状态：

| 待原始证据审阅 | 相对现有 owner 的真实增量；不得外推 |
| --- | --- |
| [`2609.22819`](https://arxiv.org/abs/2609.22819) | Ch78/66 尚未具体处理工具离线评价在 unsupported actions 下的**增量 policy 比较仍可点识别，而两条 policy 的绝对价值不可识别**；这是 support/authority 分权的有限反例，不是新 DR estimator 或生产安全证明。摘要本身说保守界未认证部署提升。 |
| [`2609.24144`](https://arxiv.org/abs/2609.24144) | Ch33 已报告 group/reward/gradient variance，但未把“配对 rollout 可降低 reward-contrast 方差，却**可能提高** policy-gradient 方差”写成明确反例；需核 §定理前提、预注册标准未通过、2B tool Agent/三 seed 的有限证据。不得以 +5.1pt 单项替代未通过的 learning-curve gate。 |
| [`2609.24991`](https://arxiv.org/abs/2609.24991) | Ch70 已有 tenant/request cost tag 与 shared-cost policy；本篇可能具体补上 K8s/OpenCost/gateway/provider **跨账本 label 漏归属与双计**，并展示共享 KV 的 token-vs-time meter 会改变责任分摊。66%/61% 为构造的月度 synthetic allocation，不是生产账单；H100 上 vLLM 的 12–14pp meter 差异仍受所测负载限定。 |
| [`2609.24812`](https://arxiv.org/abs/2609.24812) | Ch23 已标记 speaker/turn，Ch78 的工具授权主要是文本主体；本篇的语音多说话人评价把**说话人识别 → 指令归属 → 是否允许 tool call / 是否应答**连成同一 EvalSpec。需核 clean-transcript 对照和每项 atomic rubric，不能把基准正确率外推生产授权安全。 |

另两项保持**标准审阅而非贡献候选**：`2609.23033` 的 looped-LM mixed-depth wavefront 是新架构上的执行点，但 Ch48 已有 mixed draft/verify batching 和 target commit；只在同生成语义且端到端 recurrent-call/内存边界改变时重开。`2609.24197` 的 drafter 无独立 KV 是内存优化分支，需核 target KV 只读复用、数值等价及真实并发净收益；未证明它替代已有 speculation 规则。两者现阶段不写 Books，也不必为题摘新名扩池。

其余定点线索候选前关闭：`2609.22223` 的 dependent claim graph、shared evidence 与搜索预算已在 Ch66 的最小依赖子图/证据复用合同；统一训练 agent verifier 是实现分支。`2609.24196` 是 looped LM 内部早/晚迭代 logits 对比的局部质量手段，不能与 `2609.23033` 的执行调度当一项或重复计分。`2609.24967` 的多 Agent 历史导致 collusion、reward 漂移与外部 policy owner 已在 Ch82 明列；论文中的 peer intervention 为受限案例，不改变授权边界。`2609.24088` 的 rFID≠gFID 与 latent prior/decoder 分布失配已在 Ch23 的 matched generator capacity、rate–distortion–generation 验收；GAR 轨迹是诊断实现。官方 arXiv abs 抽查上表四项及两项标准审阅均未显示 withdrawn；这不证明其他渠道没有更早公开版本。尤其 `2609.22819` 官方 abs 的 Submitted 字段为 09-19，不能把它冒充 09-23 首发，须按本批 New 公告与作者 artifact 再核日期。

更新裁决：`2609.23900` 经独立比较 [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 与作者既有实现提交，branch-local recurrent state、accepted-chain commit 与代价边界均非本窗新命题；**候选前关闭 / 既有覆盖**。上文初批“优先”是历史筛选记录，以此最终裁决为准。

在题摘层做第二轮强剪枝后，不应将前文各批次的“优先”简单相加。日报 owner 已独立审阅并完成 Books 判断的 `2609.22870`、`2609.24322`、`2609.23536`、`2609.23478`、`2609.24362`、`2609.22478`、`2609.24048`、`2609.24969` 不在本来源账本重复全文工作。尤其 `2609.24969` 的 LM 权重扰动 importance-sampling proposal 只补 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的原模型风险率与 proposal 命中率分权；Ch66 此前已有 rare-event cascade / upper-envelope 路线，并非本篇首次提出尾部风险评估。`2609.22157`（输入自适应 KV eviction gate）、`2609.24885`（RAG copy ceiling）、`2609.22628`（文档多模态输入选择）、`2609.23881`（JEPA 静态/动态表示）、`2609.24088`（生成时 latent 分布诊断）、`2609.24812`（多说话人 Agent speaker 归属）与 `2609.24927`（个人上下文影响经济推荐）宜先以标准审阅核已知机制的新增适用边界，不能仅因摘要给出有趣结果就提升为 Books 修订。`2609.23900` 的 branch-local recurrent speculative state 与 accepted-path commit 已由 [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 正文承载，目前只可能提供另一种具体 engine/模型证据，候选前 `No Change`。`2609.23125` 的 perplexity 不足以验收量化、`2609.24745` 的视觉未来质量不等于控制效用已在现有 Ch49/66 与 Ch25/26 主线，先检查其是否提供真正新条件，不能直接重复写书。DSec 与 GPU-Kernel Checker 的首发/同家族纠正见上文。其余标准审阅线索仅有条件进入后续 source-family 对照；本段是**下一步有限审阅顺序**，不是已冻结候选分母或来源 Gate。

1. 1,003 个唯一 `New` 标题已完成一次题目级浏览；我读完 361 个 New 与 2 个仅 Cross 摘要，报告 owner 独立审读 20 个此前仅标题级 New，个人身份邻域补读 4 个不同 New，故累计 387 个唯一摘要（385 New、2 Cross）。其余 618 个 `New` 是题目级范围关闭，**不是**逐篇摘要或全文审阅。前两轮反向抽检发现 `2609.24289`、`2609.22359`、`2609.24048`、`2609.24194` 等宽标题词表的真实漏收；第三轮从题目关闭中发现 `2609.22913` 的实时多模态系统线索并对相似 67 标题补检；第四轮发现 `2609.24969` 的 Agent 稀有失效估计线索；第五轮发现 `2609.23881` 的运动表征和 `2609.24088` 的生成 latent 评价边界；随后摘要主题补检发现 `2609.24812` 的 speaker-scoped Agent；独立 20 项样本又发现 `2609.22195` 的 profile-collision EvalSpec，但其首发 Date Hold。分层抽检并未覆盖全部标题关闭项，不能仅凭这些样本宣称来源贡献召回闭合；已读工时也不构成准入理由。
2. Replacement 已做 12 页显式 Comments 修订信号扫查并定位 5 个旧 owner 的重要更正/证据升级，但沉默 Comments 的 project-title 项仍有遗漏风险。183 个 Cross-only 不计本日 New；对列出的主题恢复其 first-public owner 周期，不能仅因 cross-list 日期计今天。`2609.22547` 与 `2609.23570` 只作为已读 Cross 恢复线索。
3. 对拟入选项查官方 abs 的精确版本、撤回字段与跨渠道首次公开，再独立复核本账本的优先线索和边界关闭；当前 23+11 项初批加后续主题优先线索只是**题摘阅读优先序**，不是 2026-09-23 冻结候选。须由小规模、去重后的设计增量清单进入最终分母，不能因为已读题摘很多就扩大候选。
4. 之后才进行 V2 三维评分、对应深度证据审阅和 Books 判断。此处记录的是当时的 `SRC-ARXIV = 未完成` checkpoint；后续闭合状态以末节为准。本文件始终不能替代 Evidence 或 Books 的独立验收。

## 2026-09-23 后续准入与日期复核 checkpoint（覆盖以上较早的暂定判断）

以下是**当时优先处理的日期裁决 checkpoint**；上文的“拟进入”“标准审阅”表保留筛选轨迹，不代表当日已冻结候选。arXiv `New` 批次公告在本窗，只能证明 arXiv 渠道在本窗公告；不能覆盖作者已经公开的论文、仓库或技术报告。完整 New 身份的最终准入状态以文末链接的逐项审计为准。

| Family | 可复核的作者/官方证据 | 本窗处置 |
| --- | --- | --- |
| [`2609.22819`](https://arxiv.org/abs/2609.22819) | 作者仓库 [09-18 07:27 UTC commit](https://github.com/jaxblack/counterfactual-tool-ranking/commit/3b0b74a38edf83d04b000f11875db5d34b0f8261) 已加入 executable MCP study、实验与 first working paper；09-18 09:41 UTC [后续提交](https://github.com/jaxblack/counterfactual-tool-ranking/commit/e3dacf0ae396500cc9c528bd0ae4ccf3c57185c1) 已有 public BFCL evaluation/policy contrast。 | `Date Hold`：核心内容写入时间早于本窗，但 commit 时间不证明当时仓库对公众可见。未找到可信公开上线时间，不在 09-23 评分或 Books；可核作者公告/存档后回拨。 |
| [`2609.24144`](https://arxiv.org/abs/2609.24144) | 作者仓库 [09-04 04:48 UTC 初始提交](https://github.com/TheDeadcoder/paired-rollouts/commit/a14f5c67d194c6e3a2f4f6e31c3fd25cac2a46b4) 已写 paired rollout/event-keyed noise/preregistration；[09-18 gradient probe 提交](https://github.com/TheDeadcoder/paired-rollouts/commit/a16287bcf190ddc93bf8c88f8caa0d24a69d927f) 与 09-19 结果提交又加入 estimator 反例证据。 | `Date Hold`：旧构想与后来的定量证据须作为同一 family 的演进节点；仓库提交的公众可见时间未证，且正文增量何时公开未定，不在本窗评分或 Books。 |
| [`2609.24812`](https://arxiv.org/abs/2609.24812) | Boson AI [09-08 02:59 UTC commit](https://github.com/boson-ai/MSI-Bench/commit/6d8313f90c00b6cfbd0e0d643fa981f3e9c8af3b) 自称“initial public release”，README 已有 `respond|silent` 与 `tool_calls` 的说话人归属评价接口。 | `Date Hold`：作者来源明确把公开发布置于 09-08，而非 09-23；但缺独立的精确上线记录，回拨到 09-09 窗口需再核。今日不重复计分。 |
| [`2609.24991`](https://arxiv.org/abs/2609.24991) | 作者 [GitHub Release v0.2.0](https://github.com/timurista/unalloc/releases/tag/v0.2.0) 明确 `published_at=2026-09-14T22:38:44Z`（北京时间 09-15 06:38），Release 附 `unalloc-case-studies.pdf`，正文已含 K8s/LLM 账本归属、KV 计量模拟与 case study；[09-14 23:52 UTC commit](https://github.com/timurista/unalloc/commit/0b5a8bb87e95ecc087ef3da2cc129d86cf6a58fa) 增补 H100/vLLM 实测，之后 v0.2.1 公开。 | `Spillback → 09-15 Daily`：至少核心论文和机制已有正式公开 release；09-23 arXiv 公告不再是 first-public。H100 证据是同 family 后续节点。今日本源关闭，不评分/Books。 |

以上仓库链接证明指定提交**内容与 commit 时间**，不把 repository `created_at` 或提交时间冒充公开可见时刻；唯一确切公开事件是 `unalloc` 的 Release `published_at`。四项不应反向改变本日报已独立通过的八项结论。`2609.22195` 仍因作者 OpenKedge 站点早发但无精确公开日期而 `Date Hold`；`2609.22220` 作者 09-12 公告已单独回拨。

### 有界漏收复核与两项标准审阅

在报告 owner 此前独立审读的 20 个标题级样本（19 个无明显漏收、1 个 `2609.22195` 已改 Date Hold）之外，按 ID 间隔抽取 8 个账本未列的 New 标题，读取完整官方快照摘要：`2609.22099`（菜谱结构）、`2609.22249`（prompt tutorial）、`2609.22988`（代码语言表示几何）、`2609.23162`（品牌可见性相关）、`2609.23386`（程序化 3D 建筑）、`2609.24125`（视觉对比学习正例）、`2609.24265`（医学扩散反问题）、`2609.24839`（3D 重建视角漂移）。均未提出超出现有 AI System owner 的新长期机制或评价合同；其中品牌研究是观察相关，不是检索机制的因果证据。又在标题含 Agent/World/robot/training/evaluation 等风险层按间隔抽取 12 个未列身份；对边界较近的 `2609.22308`（黑盒游戏复现基准）、`2609.22688`（CAD 几何引用）、`2609.22868`（驾驶 BEV 预训练）、`2609.23863`（对象中心 3D grounding 控制）、`2609.24813`（视觉空间输入变换）读完整摘要。前四者的系统责任已在 Ch26 的 object/geometry→controller 与 Part VI 的外部 evaluator；第五是特定 inference augmentation。均仅给受限任务或实现，没有新 owner 决策，候选前关闭。这 20 个补样与原独立 20 样本不是对其余标题的全量摘要审核；补样后可确认的唯一真实高风险漏收 `2609.22195` 已隔离，不宣称漏收概率为零。

[`2609.23033v1`](https://arxiv.org/html/2609.23033v1) §3–4 是 looped LM 的 `token position × recurrence depth` wavefront 调度：同一共享权重调用同时推进浅层 draft 与深层 verification，mismatch 冲洗未提交后缀；作者在单张 RTX A6000、BF16、greedy、Ouro-2.6B/Huginn-3.5B 上测量。它不是 Ch48 已有的**跨请求** mixed draft/verify batching；但只在 looped 架构适用，cross-recurrence KV-sharing 加速是**非 exact** 扩展。主审已按受限长期机制准入（V2 `5/9`）并在 Ch48 整合；本来源账本不代替其精确证据与写后复核，不从作者吞吐倍数推出通用 serving 收益。

[`2609.24197v1`](https://arxiv.org/html/2609.24197v1) §3–4 消除 drafter 自有 `O(N)` KV：attention 只读 target KV，last-token target hidden 初始化 Mamba state，target 仍负责 verification。作者在单张 A100 80G、vLLM、Llama3.1-8B/Qwen3-4B/8B 与八项任务，1000-request closed-loop/concurrency 8–128 的受限设置评估；低并发时 hybrid backbone 反比 block diffusion 更慢。主审原拟按受限长期机制准入（V2 `6/9`）并整合 Ch48；随后查到[Harvard 官方研讨会页面](https://systems.seas.harvard.edu/seminar/2026-09-22-weifan-jiang/)的 `datePublished` 与 `article:published_time` 均为 2026-09-21T15:00:00-04:00，即北京 09-22 03:00，且摘要已披露同一核心机制。因此是 **09-22 Daily 的早发 family**，09-23 arXiv New 不重复评分；Ch48 写入的证据审阅与独立复核转回真正 owner。

### 重要 Replacement 的真实 owner 转交

`2608.28021v2`、`2606.22419v3`、`2601.15322`、`2602.13718`、`2603.16859` 均为**旧 source family 的修订/纠错**，对应最早论文月份为 2026-08、06、01、02、03；不能算 09-23 首发，也没有证明在本窗改变长期设计结论。仓库中按 arXiv ID 与准确标题搜 `papers/2026` 和 `books/`，除 `2606.22419` 仅见于 `papers/2026/06/_sources/daily-20260622/POST_WRITE_FRESH_AUDIT_V1.md` 外，没有命中已选日报或书稿正文，因此目前**无可定位的 Books 旧断言需要直接改写**。若未来恢复旧 family，需依次核：`2608.28021v2` prompt class 分层、`2606.22419v3` 代码 bug 不等于算法缺陷、`2601.15322` faithfulness 解释、`2602.13718` 新机器人消融、`2603.16859` 评价协议。此处只转交旧 owner 线索，不创 09-23 新分数。

**早期来源 checkpoint，已被后续逐项审计取代。** 当时记录为 1,003 New 标题级扫描、400 个唯一摘要（398 New、2 Cross）与九项候选；这些累计值没有逐 ID 的阅读级别映射，后来发现漏收，不能当作最终筛选或候选分母。`2609.24197` 经 Harvard 官方页面公开元数据回拨 09-22；三项早期仓库公开 visibility 不可核，隔离为 `Date Hold`；`2609.24991` 由可证 Release 回拨 09-15。上文 363、387、618、400/9 都是过程计数，不能覆盖文末 New 身份审计与日报最终 38 项候选。

## 独立审计更正：来源 Gate 重新打开

以上早期来源 checkpoint 是独立审计**前**的判断，已被后续逐项审计取代。现在持久化了官方 Tuesday 12 分类经 ID 去重的 [1,003 个 New 身份与题名](./arxiv-new-identities.md)，以及 [183 个 Cross-only、560 个 Replacement-only 身份与题名](./arxiv-non-new-identities.md)，不再只依赖 `/private/tmp` 中可能消失的快照。两个身份索引只证明原始列表覆盖和去重，不证明筛选完成。

对 1,003 个 New ID 与本账本的显式身份求交，只有 **457 个 ID 曾被逐项点名**；剩余 **546 个 New 从未持久化逐项筛选判断**。此前“400 摘要 / 605 标题级”的累计值来自工作过程记录，尚未建立可重算的逐项阅读级别映射，不可据此为 605 条自动填上统一范围外理由。事实上，546 个未列身份里至少有 [`2609.22215`](https://arxiv.org/abs/2609.22215)（subliminal learning 缓解）、[`2609.22299`](https://arxiv.org/abs/2609.22299)（冻结策略购买却未使用物理证据）与 [`2609.22588`](https://arxiv.org/abs/2609.22588)（VLM 感知证据与行动脱节）等标题含义不允许仅按领域名关闭的边界项。它们需要完整摘要和项目贡献判断；不能因为先前从标题队列漏记，就推定其无贡献。也不能把“未列账”全部解释成“未读摘要”：先前的工作过程可能读过但未持久化 ID，须逐项恢复真实审阅级别。

上述 457/546 是独立审计开始前的基线，随着新增逐项审阅会变化；最新身份与阅读级别以 [New 逐项筛选状态](./arxiv-new-screening-audit.md) 为准，不再从旧账本的显式 ID 数倒推已读摘要量。

**独立审计时 `SRC-ARXIV = 未完成`，这一状态已被后续逐项恢复覆盖。** 当时可验收的只有官方列表身份、原候选审阅和日期隔离；后续已对 1,003 New 建立逐项审阅层级与处置。不得从早期 457/546 或 400/9 过程计数倒推最终分母。

## 2026-09-23 来源与候选最终对照

以 [New 逐项筛选状态](./arxiv-new-screening-audit.md) 为准：1,003 个唯一 New 身份全部有分层处置，其中 38 项通过贡献准入并完成相应 Source Review 与 Books Decision；580 项摘要/全文后候选前关闭、276 项标题范围外关闭、76 项标题级关闭、21 项标题明确范围外关闭。另有 5 项 Date Hold、4 项旧 owner、2 项理论范围争议和 1 项版本事实隔离。183 个 Cross-only 与 560 个 Replacement-only 做身份和有界修订信号检查，不声称逐篇读完摘要。最终 38 项及其 33 项整合、5 项已有覆盖详见[当日日报](../../09/23/README.md)；本账本保留过程证据，不再提供另一个“最终”候选数。
