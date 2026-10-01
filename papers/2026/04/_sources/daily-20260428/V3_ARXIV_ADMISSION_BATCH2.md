# 04/28 arXiv 贡献准入：第二个有限旧线索批

本批只取旧 V2.1 `retained` 表中紧接首批的 30 个身份（`2604.23141`～`2604.23646`）。逐项阅读已存 `arxiv-owner-replay-20260903/20260428/arxiv-owner-receipt.json` 的完整标题和摘要，**不沿用旧分数、Books 标签或「111 项候选」**。缓存题摘可能受后发版本污染；“继续”只指明确的潜在长期机制/评价边界，尚须官方 exact-v1、日期例外、关键反证和实际章节差异；“关闭”是本阶段具体贡献不足，不称论文学术价值为零。本批不建立日期证据，日期规则及相邻 ID 批次推断见[检查点](./V3_REVIEW_CHECKPOINT.md)。

| ID | 题摘判断 | 当前具体理由或必要消歧 |
| --- | --- | --- |
| 2604.23141 | 前分母关闭 | AR 眼镜识别/社工攻击下组合 sensing ACL、F-RMU unlearning 与 Agent guardrail；题摘未隔离哪个控制跨设备/模型/执行边界创造了现有权限链不能表达的新不变量。60 人、360 段会话只属该攻击场景，不能代替跨栈组件的因果对照。 |
| 2604.23150 | 继续 | 多节点 MoE 的 100k+ expert 激活轨迹若能证明 prefill/decode 相关性与任务域漂移会改变微批分组和 replica placement，可能修正只按平均热度放置；核 trace 来源、通信/端到端、内存约束及和静态 placement 的受控比较，不采“20×”无配置表述。 |
| 2604.23172 | 前分母关闭 | cosine assignment、top-1 STE 与 layer-wise NAS 是 VQ-QAT 的局部组合；作者自己报告跨量化率不稳定，题摘未指出会改变大模型训练/推理量化的稳定机制或已有质量—压缩边界。不能因 `MODEL-FFN` 能映射就入选。 |
| 2604.23178 | 继续 | 五类 judge、四偏差与等协议比较若确立 style bias 超过 position 且“更大/更新的 judge 未必更稳定”，会改变评估器选型和 budgeted debias 的合同；核人类 gold、375-pair 自建集、Holm-Bonferroni 及 cost 计算，不能把最高 agreement 当通用准确率。 |
| 2604.23205 | 继续 | UMA 端侧 NPU 权重从 4KB page 加密转为 64B AXI burst 内联解密，明文仅在隔离 SRAM 的 tile 生命周期存在；可改变安全边界与带宽粒度共同设计。核真实芯片 vs projection、AES 与 DRAM overlap、物理攻击假设和不同模型/层几何，不照搬 98.4% 理论带宽声明。 |
| 2604.23210 | 继续核贡献 | 仅 1-bit danger 反馈而非 reward/reflection 对安全规则发现可能揭示独立安全通道必要性；但五个低维 gridworld 与五个文本 analog 未必足以改 Agent 长期控制结论。核可执行规则、错误警报和与既有 safety monitor/verification owner 的具体差异。 |
| 2604.23238 | 继续核贡献 | 针对模型输出轨迹被蒸馏，选择反事实影响大的 sparse thought anchor 并同时约束可检测性，可能改变“防护强度/输出可信”取舍；先核 Stackelberg 约束是否落实、student/teacher 双侧指标与黑盒成本，不能把论文自称安全防御直接写成平台保证。 |
| 2604.23272 | 继续核贡献 | VLA 的 tactile/torque 异质感知通过 decoupled stream 和未来物理信号预测接入动作；核两阶段冻结与预测辅助是否真的分离多传感器互补性，而非已有多模态融合在少数机器人任务的局部收益。 |
| 2604.23277 | 前分母关闭 | semantic k-NN/顺序边、topic cluster、bridge centrality、greedy 去冗余的 extractive context compression 组合；题摘未证明结构先验相对现有 query-aware 保真/压缩状态合同带来新的失败条件或选择，四数据集竞争力不足以单独准入。 |
| 2604.23280 | 前分母关闭 | Agent 身份在 substrate/persistence/verifiability/legal standing 四维的调查和五项 gap 是治理议程；没有新实现、评价反证或能改变现有 agent identity / authority 设计判断的可核证据，不因“跨组织”术语准入。 |
| 2604.23318 | 继续 | 正确/错误组的 hidden-state span Wasserstein 距离用于 token advantage reweight，不增加 step gold；若区分相关 representation signal 与真正局部 credit，会改 GRPO 反馈分配边界。核定理前提、hidden state 比较是否泄露答案、同预算 PRM/GRPO 对照及负例。 |
| 2604.23333 | 继续 | 在轨迹中用正确/错误步骤的 confidence margin 而非只以 outcome reward 训练，可能改变可信度与 test-time compute 控制分权；核中间步骤标签来源、校准定义、conformal 风险是否仍需独立 held-out，不把科学题分数当 AI-for-Science 准入。 |
| 2604.23338 | 前分母关闭 | 7 层 × 4 时间尺度 Agent 安全 taxonomy 对 116 文献做编码并提出空白区，题摘未给新攻击机理、受控风险比较或解决 Ch72 现有跨会话/委托/effect 权限疑点的独立证据；“暂无 benchmark”是研究议程，非本日报新增技术合同。 |
| 2604.23366 | 继续核贡献 | FEVER gold-evidence 下的 grounded/contradicted/complementary 四类与 proceed/regenerate/replan 三档门控可能改变 RAG 证据充分性到行动的 handoff；但这是静态 FEVER+LLM judge，不是实际多 Agent 执行。核 evidence type 权重、judge 依赖和与 Ch76 已有来源身份/行动授权分工是否新增可采用命题。 |
| 2604.23374 | 继续 | 传统字符串 taint 无法追到语义变换/跨会话记忆，离线重建 source→sink 轨迹与在线 effect guard 是不同责任；核 400 场景/20 framework 采样、ground truth、与 FIDES 同威胁假设及离线开销，不把检测当阻断。 |
| 2604.23455 | 继续 | 浏览器症状与后台观测成对、固定多模态 snapshot 的 87 个诊断场景若确证“工具更多反而因探索失焦”会改变 Agent 诊断评价分母；核 gold 故障归因、tool budget 等量对照及五 fault families，不把 19.7% 精度外推一般运维。 |
| 2604.23459 | 继续 | 13 种多 Agent 架构在浏览器/桌面/代码三环境中把拒绝、拦截、部分有害执行和最终成功分阶段测量，可能修正“多代理分责天然更安全”；核配置、攻击机会与良性成功可比性，3.8× 只属受测配置。 |
| 2604.23466 | 继续 | Hopper/Blackwell 的 CuTile 与 Triton/cuBLAS/FlashAttention 交叉结果若真实显示同一 attention kernel 在 B200 领先而 RTX PRO 6000 大幅落后，会改变“高级 tile 抽象自动可移植”的设计判断；核精度、形状、实现公平性和端到端 LLM 贡献，不把 kernel 1007TFLOPS 当服务收益。 |
| 2604.23467 | 继续核贡献（非作者查漏后重开） | v1 不只是静态 CUDA Graph+JIT：还含 1–50 token 长度预捕获、miss 时 JIT+异步捕获、rolling buffer。Ch49 现有 graph 主线未具体承载这一运行中捕获/缓存更新责任；需核缓存失效与形状覆盖、同精度同 SLO、额外显存和可迁移工作负载，再决定是否真有长期增量。单卡 batch1 Llama-2 7B 的 TTFT 不能推普遍 serving 收益。 |
| 2604.23478 | 前分母关闭 | 官方 v1 的 hand-validated 等价改写、极性反转与 always-A 退化揭示 judge 输入协议脆弱性；但 Ch66 已有语义等价模板、选项排列和人为金标的验收合同，本篇摘要与定点方法未给超出现有命题的独立新控制。保留该具体反例，不说完全没有反证。 |
| 2604.23483 | 前分母关闭 | 二 Agent/10-query 的黑盒改写攻击在 misinformation detector 上奏效，仍是特定分类流水线的语义改写与二元反馈搜索；题摘的不同 pipeline 逃逸率未给新的 Agent effect 权限或模型安全通用机制，不以 LLM 管线名称提升到主线。 |
| 2604.23488 | 继续 | 明示提示诱导的 reward hack 轨迹与训练中自然出现的 hack 轨迹若在相同 monitor 协议下不可互代，直接影响监测训练集/验收数据的外推；核 tracer 对真实 hack 的 false positive、训练组泄漏、budget 与未知 hack 类型，不把提示构造样本当自然发生率。 |
| 2604.23505 | 前分母关闭 | P1 模型内/P2 工作流/P3 社会技术不确定性传播 taxonomy 与五挑战是已有错误传递、状态有效性及人工审批原则的归纳；题摘无新量化传播模型、失效反证或可执行回退合同，不因“compound system”叙述准入。 |
| 2604.23543 | 前分母关闭 | Pref-CTRL 把 RE-Control 隐态梯度编辑的标量 value 换成偏好多目标 value；两 benchmark/ OOD 增益仅局部方法比较，题摘未隔离新控制状态或说明为何它改变在线 steer 与 preference reward 的现有设计边界。 |
| 2604.23553 | 继续核贡献 | 扩大 thread-block cluster 融合到完整 GPT-NeoX/Pythia decode block，可能改变 kernel fusion 与 launch/中间物化的边界；核 RTX5090、两模型、同 precision/质量与 persistent TMA graph 的独立收益，不能据 1.34× 单卡局部结果推普适端到端收益。 |
| 2604.23577 | 继续核贡献 | router/cascade 与针对升级失败的定向 distillation 构成闭环，可能把服务路由成本反馈写回便宜模型的训练选择；核 8 周 pilot、human eval、acceptance/SLO 分母、同预算反证及 Ch56 现有 cost-feedback 论点是否已承载。不能因为三模块齐全就入选。 |
| 2604.23581 | 继续 | 同 judge/rubric 下将 Agent 轨迹依赖 DAG 加入故障归因，若 +22pp/+34pp 真由 DAG 引起，可能改变 trace eval 中“错在何节点”的证据合同；核 450 cases、12% 非 DAG 对照、root cause gold 和协议回放。 |
| 2604.23584 | 继续核贡献 | 图像检索证据中的身份编码/属性编码分离，再替换身份且保持任务线索，涉及隐私与 groundedness 两目标冲突；核“保证不同身份”的 oracle 阈值、视觉证据是否仍有效、延迟和人脸以外局限，不能把生成视觉近似当隐私保证。 |
| 2604.23626 | 继续核贡献（非作者查漏后重开） | v1 有 w/o History/异构图及归纳/转导对照，不能说完全未隔离图历史贡献；需核其联动 role/backbone 路由是否真的改变 Ch81 Agent memory/selection owner。摘要以 GiB 称 GPU cost，但正文 Cost 按 token×价格定义，资源量纲冲突；不得采 `186.26→1.04 GiB` 作证据。 |
| 2604.23646 | 前分母关闭 | 官方 v1 §2.2/§4.4/§5 确有威胁模型、实现范围与形式条件，不能以“缺披露”拒绝；真正边界是 T1/T3/T6 尤其 A11 等强假设，intent/authorization/execution、capability token、lineage、goal drift/output gate 已由 Ch72 现有权限链承载。未见足以改变当前控制责任的独立新不变量，定点保留假设边界。 |

非作者双向校准见 [独立复核](./V3_APR01_ADMISSION_BATCH2_INDEPENDENT.md)。本批现在为 **11 条继续、9 条继续核贡献、10 条前分母关闭**；不是 20 项冻结候选。`.23366` 的 FEVER 行动选择只是静态 proxy，Table 8 contradiction catch-rate 弱于部分对照，须在后续证据中保持；只进一步审真正可能改变长期命题的项，不把本批 30 条都送全文。
