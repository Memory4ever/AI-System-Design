# 2026-04-27 V3 贡献准入反向校准（作者侧，待独立核）

窗口仍为 `[2026-04-26T09:00:00+08:00, 2026-04-27T09:00:00+08:00)`。本次只复用本日日内 [必要证据表](V3_EVIDENCE_REVIEW.md) 已读的 exact-v1 决定性段落与所列实际 Books 论点，不把 408 个原始题名变成候选或全文队列。下表重新判断“对本项目有何具体长期机制、边界或纠错贡献”，不把已有章节、论文规模、小模型/单领域、访问难度或写 Books 的便利度当独立准入规则。这里是作者侧校准提案，非独立日 Gate；原证据和反例不删除。

| 家族 | 本轮贡献准入复判 | 具体理由或独立待核问题 |
| --- | --- | --- |
| OpenAI Symphony | 继续 | issue 当前状态拥有持续 eligibility，run/session/PR 只拥有执行产物，Human Review 不等 Done；不同于一般 workflow 状态图，Ch84 已实际吸收且写后通过。 |
| 2604.22750 | 继续 | Agent 预运行 token 自估和 runtime meter/hard cap 的授权与成本分账，负例为自估低相关且估算本身有费；不是只因 OpenHands 名称。 |
| 2604.22136 | 继续、中心争议隔离 | 匿名输入经私有映射恢复真实执行对象，Eq16 的执行身份零信息保证遭二元反例；effect-time gate 有用不等强定理成立。 |
| 2604.22152 | 继续、版本证据隔离 | action/vision/language token 与 progress proxy 可影响真实机器人 policy 评价权限，但 exact-v1 PDF 未可读，不能用污染 HTML 数值正面采用。 |
| 2604.22180 | 继续 | 同一 encoder 的 first-stage retrieval 与 rerank 双目标可反向变化，单看 rerank 指标会漏检 first-stage 退化。 |
| 2604.22266 | 继续，独立复核是否过宽 | forced-readout 的离线最后一次答案切换和在线可观测停止分离，作者完整轨迹 oracle 不等 runtime 信号；虽 Ch66 已承载，仍是受限具体评价反证。若独立复核认定只重复现有例证，可转前分母关闭。 |
| 2604.22271 | 继续，独立复核是否过宽 | PANL/LAT 的受控恢复和单独消融不一致，具体反证“线性可读即可授权自动修正”；实验不证明 PANL 必要或通用 correctness sensor。 |
| 2604.22407 | 继续 | 保护性 gradient 改写同时降低 Adam 二阶幅度会反向放大有效步长，和原 optimizer/replay 原则之间有新组合失效。 |
| 2604.22436 | **建议转前分母关闭** | 目录 Agent 的 task query、description、top-20 执行与 LLM-judge relevance 是成熟检索+运行验证组合；Ch84 已把描述/分类与 task-slice 真实执行/结果 witness 分权。现有 §4/6 只提供此目录上的规模和标签局限，没有独立改变 Agent 选择、权限或能力验收的规则；不是因“已有章节”或 benchmark 身份自动排除。保留 9,759/3,211/66,740 三种不同分母及 top-20/标签偏差原证据。 |
| 2604.22520 | 继续，独立复核负面切片价值 | 固定大模型调用比例下的条件 gain 预测有 severe-loss 8.19% 高于 random 7.10% 的反例，后置译文质量 guard 降至 5.69% 却增一次解码；这是 gain-only 路由不足以承担尾部质量的具体成本/保护边界，不把翻译任务外推所有路由。 |
| 2604.22575 | 继续 | 逐层 sparse-exact/linear/full 混合迁移及蒸馏与不同服务路径 TTFT/TPOT 反向，属模型状态/执行身份的受限可迁移取舍，非只因长上下文 headline。 |
| 2604.22238 | 继续 | 在线图状态经 chunk 后进展谓词控制 VLA 语言/视觉双输入，区分 planner 的可修订状态与控制器物理提交。 |
| 2604.22591 | 继续 | task-feasible benign 场景中物理风险因子放置及即时/累计/顺序违约分母，比单一离线动作标签更明确。 |
| 2604.22678 | 继续、Books 待独立采用 | 每份文档独立生成分支、token 后验加权与分支剪枝是 RAG 执行状态，不只是新 QA 数据集；后验非事实权威，成本反例保留。 |
| 2604.22709 | 继续、Books 待独立采用 | 离散隐式推理码需 bottleneck SFT→warm-up→受约束 RL；cold RL 失败与训练/输出成本分账是具体目标/资产生命周期。 |
| 2604.22722 | 继续、Books 待独立采用 | 离线 reader utility teacher 蒸馏到双塔 retriever，把训练 supervision 和在线 ANN 分权；若现 Ch76 已充分覆盖而实验无独立反证，可只报告，不因单个 R@1 胜出写书。 |
| 2604.22074 | 继续 | outcome reward、forced-prefix 敏感 CIR、自足 verifier SR 是三种不同评估对象，不是同一个“解释可信度”指标。 |
| 2604.22167 | 继续 | 稀有 harmful-output 事件的 proposal/target 逐 token likelihood ratio、support 与 ESS 是尾风险估计的具体审计条件，不是 proposal 攻击成功率。 |
| 2604.22127 | 继续、Books 待独立采用 | hybrid recurrent/attention 的 adapter target-module 排序随串行/并行拓扑变化；单 seed/小模型不足普遍因果，但该比较正面改变 placement 需检的条件。 |
| 2604.22273 | 继续 | ECR/EIR 乘初始正确率给 self-correction 净值边界，verify-first 的成本/外部依据与“有错可修”不同。 |
| 2604.21999 | 继续 | ACT 初始浅停会让深路径缺训练信号，scratch 与 T 预算需联合校准；小 Sudoku/3 seed 限制外推但不是排除本机制的理由。 |
| 2604.22565 | 继续 | 原文保留但突出 span 的输入变换，与删除/压缩有不同 token-cap 与 attribution 责任；是独立操作分支，不因 Ch75 已写即前关闭。 |
| 2604.22509 | 继续、Books 待独立采用 | 租户/运营方互不共享效用与物理约束、却对运行中分配持续重议的薄合约不同于 launch-time spot/配额。价格不是权限、生产收益未证。 |
| 2604.21964 | 继续 | safety case 从证据对照扩到 supported decision、assured system/environment、validity duration 与 defeater re-open；受限外部材料审查不等安全结论。 |
| 2604.22032 | 继续 | kernel 名称或 smoke test 不定义跨硬件 shape、数值/确定性/异常语义，oracle/tolerance 需在部署合同显式化。 |
| 2604.22191 | 继续 | RLFT 间接 reward-mediated 私有文档参与不能由字串/MIA 单独排除，document-disjoint 和成对 log-prob shift 是受限独立审计对象。 |
| 2604.22050 | **建议转前分母关闭** | §3–4 逐层 attention 暂替 identity、按敏感度配 softmax/linear/attention-free 并蒸馏 healing；Ch22 已有 dense→hybrid 的层位敏感度、保留难替换层及迁移质量/执行联合 Gate。所测 Qwen3-4B/A10 的 10M PIQA 反向与高并发数字只限定该局部改造，尚未发现能改变现有 owner 选择的独立机制或反证；保留三档动作和失败切片，不因局部实现新意强保候选。 |
| 2604.22409 | 继续 | 同任务的即时感知、oracle 文本历史和原始视觉流阶梯及 stepwise/episodic 分母提供评价方法新边界；L2→L3 的模态/权威混杂须保留。 |
| 2604.22661 | 继续 | 同一信息需求的多 query 变体要在检索前选一，ranking-optimal 未必 answer-optimal；成本未配对，但控制对象新。 |
| 2604.22076 | 继续 | forget set 不完备时选代表性 core-set 与未选/未知集合分账，梯度近似不等删除/因果证明。 |
| 2604.22117 | 继续，保护纠错 | 论文威胁说分散网站进入预训练，却以固定触发 SFT 代理验证；准入价值是安全证据权限纠错，不能把 SFT 结果变成预训练潜伏事实。 |
| 2604.22193 | 继续，独立复核是否过宽 | 用户/文档/模型先验正误与次序成对 probe，加训练后正确信息利用下降的负面切片；此非真实 provenance，但可校准来源冲突评价。若只与 Ch76 现有断言一致而无新裁决，改前关闭。 |
| 2604.22708 | **建议转前分母关闭** | 380 条三 scaffold trace 的 input/metadata 消融说明观测完整度影响局部失败定位，但 Ch69 已要求 immutable input/config/environment/effect trace、可重跑与诊断不等因果。所测 attribution 的数量差异没有修正缺边、diagnoser 授权或上线 repair Gate；保留 .66/.30 等受限 benchmark 与“+76%为相对值”纠正于来源笔记，不再当独立长期贡献。 |
| 2604.22038 | 继续 | 图文冲突与 cue 干预区分自述来源/行为 selectivity/真实 lineage，已有真实 Ch66 正文待独立核。 |
| 2604.22082 | 继续 | sandbagging model organism 中观察到的 elicitation ceiling 不是隐藏能力/真实欺骗已被消除，已有真实 Ch66 正文待独立核。 |
| 2604.22228 | 继续 | GPU NVLink/PCIe multipath 与 CUDA Graph replay 的 payload 和 launch 收益分账，已有真实 Ch36 正文待独立核。 |
| 2604.22312 | 继续 | previous-step TopK hint 只是 proposal，当前 counting/refine 拥有 exact correctness，已有真实 Ch49 正文待独立核。 |
| 2604.22753 | 继续 | 有异质 run 成本的 scaling-law pilot 需面向目标区不确定性作顺序选择；旧快照后稿术语污染已校正，已有真实 Ch28 正文待独立核。 |

## 否定侧有限反查与口径边界

已按不同风险反看既有 [筛选笔记](V3_SCREENING_NOTES.md) 中 `21999`（原小 Sudoku 排除被恢复）、`22565`（原文强调而不删 Context 被保留）、`22085`（Agent memory，但同后端多处同时改变，未隔离 typed schema）、`22128`（可解码 vs 因果使用，Ch66 已具体承载）、`22452`（多 Agent 大平台浅交互，不控制协作机会）、`22583`（分类 head budget 不证明 LLM decode 真实执行）、`22149`（车辆安全 posterior 不直接改变 VLA control interface）、`22384`（CPS monitor 若无新的模型负载/控制接口则关闭）。这不是对全部 408 身份或全部关闭项的独立验证；非作者应按来源/主题/共享理由补抽纠错、保护和系统设计反证信号。若发现“现有章节已有”被当成准入硬拒，定点重开受影响 family，而非机械扩大 raw 全文队列。

本次建议仅移出 `22436`、`22050`、`22708` 三家族：当前 38 工作项若独立复核同意，改为 35；其余 35 包括两个具名争议/版本隔离，仍非冻结终态。需保留原 exact-v1 证据，正式 README 与其他账目在独立口径确认后同步；不能因本轮剪枝收缩已证真增量或预支 Books/日 Gate。
