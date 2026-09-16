# 2026-05-07 非作者独立复核 — 未通过

> 角色封存：本 reviewer 随后受主任务委派转为 May07 作者整改。本文件保留发现时的独立问题清单，不再作为修后稿的最终非作者验收；新稿必须由另一名非作者复核。

Reviewer：`/root/may06_independent_review`，本轮未参与 May07 作者侧修复；以下是复核意见，不是作者补写或新候选冻结。状态维持 **进行中**。主任务可执行 Books 修复，但修复后仍须回读验收。

## 真实范围与边界

- 完整读当前 78 项候选的题目、已存完整摘要、准入理由、三维评分与全部 78 组 Method/Evaluation/Limitation locator/snippet；每项判断见下表。评分是针对本次拟采用命题的复核建议，不能机械批量替换，更不能据分数倒推准入。
- 469 个 closures 的标题全量扫描；按来源类别、方法/理论/benchmark/领域应用/观点等关闭理由，以及安全、纠错、长期系统机制扩查 36 个完整摘要。不是 469/469 全量语义复核。样本结果否定当前关闭族的可靠性，应作者重开受影响族，而非只补列出的几篇。
- 独立在线回读的 exact-v1 主来源包括 04209、04468、04478、04563、04624、04811、04960、05023、05049、05097、05112；其余是题摘及作者 packet 的逐项语义检查，**不声称 78/78 全文独立复读**。多项字段已证实角色错误，足以拒绝整体通过。
- 已回读 44 个当前 Integrate identity 对应 Books 的实际段落/邻接内容（其中多项只剩泛化段落，不能验收）；当前 ledger 实为 **51 项整合**，非 §5 的“33旧+5新”。04061、04261、04700、04874、04893、05029、05116 未在目标 Books 找到其 identity 绑定，仍需作者给真实正文锚点，不能自动将 marker 缺失等同没有任何语义覆盖。
- 未修改共享 Books、raw receipt 或作者 screening ledger；未 stage/commit/push。未对机构来源每项查询历史做重新获取，机构覆盖仍不在本次通过范围。

## 分母、日期与撤回

548 identity 唯一；与 raw owner receipt 的 identity 集合双向差集为空；与 May06 active canonical ledger 无重叠。当前状态计数 **548=78+469+1**。这些是身份/一致性检查，不能证明准入或关闭正确。

所有 548 项已存 DataCite initial-created 为 2026-05-07；400 为 direct OAI route，148 为 revision-route，其中 72 存在后续 OAI 日期，其余不应被虚构为都有后续 OAI。独立重取 DataCite 04050（01:43:45Z）及 05116（02:09:37Z）与收据一致。官方 [availability](https://info.arxiv.org/help/availability.html) 明确 ID 在公告时分配，Wednesday 20:00 EDT 对应 05-07 08:00 Asia/Shanghai；因此当前 public-batch-derived 口径合理，不应因较早 submitted 或后续 OAI 更新制造 gap。但这仍是批次推导，不是单篇公告时间直接披露。共享依据为 [announcement provenance](../ARXIV_ANNOUNCEMENT_PROVENANCE.md)。

[2605.04356](https://arxiv.org/abs/2605.04356) 当前历史标 v1 withdrawn。不得进入候选、评分或 Books。raw receipt 保持原 provenance；新 canonical screening ledger 却仍复制其完整研究摘要，超过最小排除用途，应改为 identity、withdrawn 状态、排除理由与官方链接，不继续保存可被误作研究证据的摘要。

## 候选逐项准入与评分复核

“可保留”表示题摘要中可辨识具体机制/反证，不表示证据或 Books Gate 已通过；“重审”须作者明确旧判断→新增机制→具体设计选择。

| arXiv suffix | 准入建议 | 建议 D+R+U | 问题/保留边界 |
| --- | --- | --- | --- |
| 04050 | 可保留 | 2+2+2=6; Books deep override | 8分将原文指针可回取与通用lossless语义基础混淆；limitation字段不是限制，需比较fallback/summary retrieval task与OOLONG narrow protocol。 |
| 04055 | 可保留 | 2+1+2=5 | meta-objective/HUW优先权为可检验机制；暂缓应有具体争议/必要证据，不仅等待Books。 |
| 04058 | 可保留 | 2+1+2=5 | frozen quantization内存转投side-MoE需精确NoChange正文；Conclusion首句不是direct limitation。 |
| 04061 | 可保留 | 3+1+2=6; counterevidence/Books deep | 四小模型受控transformation不能上升universal task template；Durability3偏高。 |
| 04069 | 可保留 | 2+2+2=6 | self-certification theorem可作理论证据而非实验；LAWS error/Lipschitz假设须核查，KV existing-coverage不能只泛称validity。 |
| 04075 | 可保留 | 2+1+2=5 | deferred importance与state revival具体机制准入；应核NoChange是否真实包含state compression/reactivation。 |
| 04077 | 可保留 | 3+1+2=6; correction/Books deep | aggregation单训练目标组件Reach2/Durability3夸大；Method locator Compared Methods未必本方法；Conclusion首句不是限制。 |
| 04084 | 可保留 | 2+2+2=6 | PQ布局与prefill/decode执行联合Reach可2；需保留prefill慢于cuBLAS的重要反证。 |
| 04107 | 可保留 | 2+2+2=6 | 表示编译有边界；Durability3无据，不继承validator/adapter保证。 |
| 04116 | 可保留 | 3+2+2=7 | 深审1shot greedy及paraphrase范围；新channel不是universal membership。 |
| 04135 | 可保留 | 3+1+2=6; correction deep | bibliometric survey是测量披露纠错而非跨生命周期设计基础；Reach3/Durability3膨胀。 |
| 04178 | 可保留 | 2+2+2=6 | architecture-specific model仅single-kernel/single-GPU/steady频率；不凭peak vsachieved常识升Durability3。 |
| 04209 | 可保留 | 3+2+2=7 | 报告称statistically hidden疑似误述，原文是Sparse-PCA计算难区分且参考是加dither权重，不是相对原权重统计不可区分。 |
| 04213 | 可保留 | 3+2+2=7 | gate-level stuck-at simulation不是生产GPU现场错误频率；9分与无direct limitation均过度，正文需区分故障注入分布与自然失效率。 |
| 04215 | 可保留 | 2+2+2=6;Books deep | admission是本书推论；需测underpredict/retry和actual latency不只FLOP；Conclusion首句不是限制。 |
| 04236 | 可保留 | 2+1+2=5 | heuristic adaptive stop不应叫calibrated commit guarantee；不同model/bench/seed边界实在，需NoChange精确read。 |
| 04261 | 可保留 | 3+2+2=7 | perceptual mismatch/authority laundering是有意义新攻击场景；effect-side boundary是工程推论，不是VLM alignment被攻破。 |
| 04263 | 可保留 | 2+2+2=6;Books deep | semantic判定最大前缀不保证target distribution exactness；generic token-level必须每token说法需限定；Method正确Evaluation只ablation不足。 |
| 04264 | 关闭或举证重审 | 1+1+2=4 | 摘要明确Viewpoint/design agenda及one running ecosystem traces；provenance/governance一般原则无新增因果/保证机制，现理由换state owner词不足准入。 |
| 04266 | 可保留 | 3+2+2=7 | Stackelberg/FPO假设与1B模型pipeline限定，不能写所有iterative RLHF均collapse。 |
| 04269 | 可保留 | 2+1+2=5;Books deep | 需要adaptive strong monotonicity或projected stationarity两regime，noise-vsdrift是受限理论非普遍Adam/SGD优劣。 |
| 04295 | 可保留 | 2+1+2=5 | semantic entropy+conformal accepted-risk guarantee需检查selective vs marginal guarantee而非复述exchangeability；NoChange具体命题。 |
| 04312 | 可保留 | 2+1+2=5 | 动态对手排名缓解saturation而非任务绝不会污染，Bayesian skill/modelcomposition有限；Reach2无跨system evidence。 |
| 04333 | 可保留 | 2+3+2=7 | 真实production跨transport/topology/routing足Reach3；Durability3应对具体trio而非通信一般基础，需实测failure范围。 |
| 04341 | 可保留 | 2+2+2=6;Books deep | train compression与infer结构桥接可reach2；compressed-module speedup不是端到端。 |
| 04357 | 可保留 | 2+2+2=6;Books deep | 6models20GPU config jointsolver mechanism，Reach3/Durability3过高；lossless两阶段只优化问题给定模板，不代表实际schedule全局最优。 |
| 04361 | 可保留 | 3+1+2=6 | 条件反证有价值；10软件设计任务/7注入条件不支持Durability3；不得外推通用单次诊断保证。 |
| 04396 | 可保留 | 2+1+2=5 | 控制组合任务中的正则时机机制；必须保留modular arithmetic负对照和调优常数无劣化边界。 |
| 04418 | 可保留 | 2+2+2=6 | 约束流形优化机制可准入，结论摘要不是direct limitations。 |
| 04431 | 可保留 | 3+2+2=7 | 训练故障表征闭环可准入；Compared Approaches不是自身方法，覆盖面/长期性高估。 |
| 04446 | 可保留 | 3+2+2=7 | 安全机制准入；白盒开源同族代理至对应API迁移，不是任意黑盒保证。 |
| 04454 | 可保留 | 3+1+2=6 | 有审计与受控反例；Four levels是概念分类而非两项研究Evaluation定位，9分膨胀。 |
| 04468 | 可保留 | 2+1+2=5 | moving-anchor与local trust-region具体；Standard SFT limitations是基线局限，非自身限制。 |
| 04477 | 可保留 | 2+1+2=5 | 历史数据驱动探索奖励机制准入；需保留regret假设，结论摘要不是局限。 |
| 04478 | 可保留 | 3+2+2=7 | 分布式rank故障实时诊断机制；Prior Diagnostic Works limitations非自身局限，补读是否支持remediation。 |
| 04496 | 可保留 | 2+1+2=5 | 外部文档探索中的gap-state机制可准入；limit只有引言句无实际限制。 |
| 04543 | 可保留 | 2+1+2=5 | 实际增量conditional-OT prefix acceptance，而非泛化proposal-verification状态机；重写delta。 |
| 04563 | 可保留 | 2+2+2=6 | range-level保护具体；有界近似不等于bit-exact，核实故障模型与硬件成本。 |
| 04568 | 可保留 | 2+1+2=5 | world-model梯度MPC与gradient-free比较可准入；report必须避免uncertainty必要性断言。 |
| 04572 | 可保留 | 2+2+2=6 | 样本更新方向投影安全风险具体；不可把相关风险分数当因果或安全保证。 |
| 04595 | 可保留 | 2+2+2=6 | compute+KV联合队列稳定性准入；Dur3需理论适用范围支撑，非普适production sizing。 |
| 04624 | 可保留 | 3+2+2=7 | evaluator-channel阻断排名反证具体；96k执行不能写成576k全执行。 |
| 04638 | 可保留 | 2+1+2=5 | 语义embedding梯度替代采样UQ具体；不是事实正确性概率。 |
| 04665 | 可保留 | 3+1+2=6 | 输出模式稳定性反证可准入；150查询五小模型，不足Reach2，method定位为背景。 |
| 04678 | 可保留 | 2+1+2=5 | 统一基线下latent-action表征任务对应可准入；不可写通用表征桥优越性。 |
| 04698 | 关闭或举证重审 | 1+1+2=4 | 摘要是LightGBM恶意软件摄取的IAT poisoning案例，未提供LLM pipeline新机制，也未支持作者添加的延迟/lineage/撤销责任；需作者指出新的长期机制而非安全标签。 |
| 04700 | 可保留 | 3+1+2=6 | 音频token梯度稀疏攻击反证保留；3ALM及白盒访问条件，Dur3缺依据。 |
| 04709 | 可保留 | 2+1+2=5 | GMM计划与uncertainty-return共享具体；14控制任务不支撑必要性断言。 |
| 04711 | 可保留 | 2+2+2=6 | block梯度统计风险+budget配置分配具体；不是已证明反转统一optimizer所有情况。 |
| 04719 | 可保留 | 2+1+2=5 | 工具步骤credit具体，可有限候选；BIRD单任务需清楚算法不同于通用dense reward。 |
| 04785 | 可保留 | 2+2+2=6 | 规范化+多步链+pre-exec机制准入；630样本patched非zero-shot必须保留，局限引言空泛。 |
| 04808 | 可保留 | 2+2+2=6 | 可控模拟工具环境+effect judge具体；模拟有效性不能外推真实部署攻击率。 |
| 04811 | 可保留 | 2+1+2=5 | 树分支MC平均拆agent credit具体；成本/树分支依赖必读。 |
| 04874 | 可保留 | 2+1+2=5 | 视觉不确定token加权具体；自估signal失准边界需真实来源。 |
| 04893 | 可保留 | 3+1+3=7 | 谱诊断transpose-invariance不可辨识结构定理可Dur3；注意只orientation-blind而非所有hallucination信息无效。 |
| 04897 | 可保留 | 2+1+2=5 | 完整原始event+检索中心能准入但须比较已有lossless-memory命题；不能换成admission/update ownership作为论文机制。 |
| 04901 | 可保留 | 3+2+2=7 | 中间activation shuffling权重保护攻击实质反证；两小模型查询访问，不能破密全方案。 |
| 04913 | 可保留 | 2+2+2=6 | midpoint task梯度边界+前部feature reconstruction具体，保留interface兼容约束。 |
| 04932 | 可保留 | 2+1+2=5 | 定理低rank drift方向切线能量，非一般LLM部署风险；论文frozen传统预测器需写适用边界。 |
| 04956 | 可保留 | 3+2+2=7 | kernel correctness≠efficiency且迭代救正确性降性能的反例有deep价值。 |
| 04960 | 可保留 | 2+1+2=5 | entropy/progress token credit具体；无verifier之外的事实监督保证。 |
| 04984 | 可保留 | 2+1+2=5 | cluster future outcome potential无需gold verifier具体；可靠性自信号偏差不能省略。 |
| 04992 | 可保留 | 3+2+2=7 | 预训练weight translator恢复适配器安全具体；非无需前置安全数据，translator训练要unsafe-safe pairs。 |
| 05003 | 可保留 | 3+1+2=6 | RM socially undesirable preference反证保留，domain-bound，不能把社会标签看普适gold。 |
| 05007 | 可保留 | 2+2+2=6 | 联合分解深度与worker选择具体；单orchestration层不支持Reach3。 |
| 05023 | 可保留 | 2+2+2=6 | executable IR lift-transfer-lower具体，GPU Architecture定位背景非own method。 |
| 05029 | 可保留 | 3+1+3=7 | 明确线性高斯population objective结构反证可Dur3，但不能泛化无边界所有学习/scaling。 |
| 05049 | 可保留 | 2+3+2=7 | memory compute comm与hybrid并行跨训练组件Reach3合理；平台/模型条件限定Dur2。 |
| 05058 | 可保留 | 2+1+2=5 | 多维security cube加13attack5defense实验可准入；已有威胁合同对比需精确。 |
| 05066 | 可保留 | 3+2+3=8 | 有限精度state信息容量结构下界Dur3合理；需精确OSP假设，不能architecture枚举替代proof。 |
| 05090 | 可保留 | 3+2+2=7 | contrastive intervention audit+验证集假设检验具体；promptbank未覆盖差异不能发现。 |
| 05092 | 关闭或举证重审 | 1+1+2=4 | 驾驶舱单数据集双流gate应用，摘要未显示新的可迁移world-model系统约束/反证；一般causal temporal gate不足准入，7分不支持。 |
| 05097 | 重审 | 2+1+2=5 if retained | 题摘称无实验；独立exact-v1 HTML却有Appendix A的13文档动力学小实验，需对齐摘要/全文版本并重写采用命题为每edge fast/slow耦合而非weights/retrieval/episodic分层。无retrieval指标或competitivebaseline，不能深读结论充当系统效果。 |
| 05112 | 可保留 | 2+2+2=6 | prefix replay双向pass-rate control具体，mask replay tokens区分更新主体；Appendix diagnostic不是主方法。 |
| 05116 | 可保留 | 3+1+2=6 | 无语义junk诱导有害prefix攻击反证；proof-of-concept发现token不证明训练自然backdoor成因。 |
| 05170 | 可保留 | 2+2+2=6 | harness任务扩展与验证机制需全文支撑；准入reason的人类release authority未由摘要支持，不可凭工程建议冒论文结论。 |
| 05185 | 可保留 | 2+2+2=6 | fatal-aware RL token mask与one-sided clamp具体；训练失败语义新机制清楚。 |
| 05191 | 可保留 | 2+2+2=6 | context atomic ops与compress表达完备主张具体；表达完备不是事实正确保证，结论摘要不是限制。 |

## 36 项关闭样本与扩查

原关闭理由大量复用“没有跨 workload owner / release contract”，但合同允许单组件的新机制、理论边界与重要反证；没有跨系统关系应影响 Reach，不是统一准入否决。也存在把算法论文错误归入 dataset/benchmark、把理论当综述，以及 04100 理由为 `None`、04373 正向准入理由配 closure 状态。需要重开这些理由族，先题摘重新冻结，不要求 469 项全文化。

| suffix | 复核结果 | 依据 |
| --- | --- | --- |
| 04054 | 保持关闭 | 最小动力学范例；未建立与现有模型训练设计的新增可验证联系。 |
| 04059 | 重开 | 无历史teacher访问的连续蒸馏：外部数据logit保留针对UKF；不是dataset贡献。 |
| 04065 | 重开准入核对 | FER与AAS实际改变无监督RL信号分配；按dataset族拒绝错误，仍需判断相对已有机制增量。 |
| 04078 | 重开 | 同prefix比较student/teacher局部validity分配distillation强度，区别于固定路径模仿。 |
| 04091 | 重开准入核对 | discounted reputation联合选择/聚合/BFT且去trusted-root假设；不能以单域自动拒绝。 |
| 04100 | 重开 | naive centered ETD破坏正定性反证+auxiliary regularization；理由为字符串None。 |
| 04180 | 重开 | 同作者风格控制与gold/wrong/no evidence反证直接改变hallucination evaluation和retrieval gating。 |
| 04243 | 重开 | 表示提取与symbolic reasoning分离的受控反证；不能要求跨workload才准入。 |
| 04251 | 重开 | root-cause fix与oracle-passing的区分及双层评价；直接改变repair验收判断。 |
| 04305 | 重开准入核对 | watermark由token改AMR结构、parser检测，具有可执行provenance机制；不得只归局部benchmark。 |
| 04373 | 重开 | bilevel regret找反例→counterfactual编译runtime rule；状态closure与其正向理由矛盾。 |
| 04410 | 保持关闭 | documentation template立场，无新的验证机制或关键反证。 |
| 04051 | 保持关闭 | 一般多模型set-based optimization，与AI System知识增量未连通。 |
| 04056 | 保持关闭 | 代数组分解表征局部机制，现有摘要未指出本项目需修改的设计选择。 |
| 04063 | 保持关闭 | AD survival应用及领域fairness指标；不能仅有trustworthiness字样即入选。 |
| 04098 | 保持关闭但重写理由 | 真实临床域能力下降是限定场景外部验证，非自动跨域核心增量；原理由不能说无反证。 |
| 04115 | 重开准入核对 | functionally-equivalent RNN的loss-invisible状态仍改变学习动力学，属于理论边界而非需跨层owner。 |
| 04222 | 保持关闭 | 传统控制HESS assume-guarantee，无直接AI模型/系统新贡献。 |
| 04330 | 重开 | implicit reasoning在宽度/图变化与depth extrapolation上的不同边界，影响CoT选择。 |
| 04421 | 重开准入核对 | attention-logit ODE与SDPA/CT-RNN极限关系+sink gate，非领域数据贡献。 |
| 04542 | 重开 | sequence-level power与local approximation不等价；true reward收益受covariance限制，非综述。 |
| 04651 | 重开 | labeled examples单pass编译fast weights，明确backprop/context成本替代；不是benchmark。 |
| 04738 | 重开 | Hessian稳定null-space additive suppression可离线吸收，无inference transform；明确量化替代机制。 |
| 04754 | 重开准入核对 | dense/MoE在approx multiplier下robustness反转，需限定CNN/ViT证据但不能自动拒绝。 |
| 04763 | 重开 | function chunking在864设置非Pareto，直接纠正code RAG chunk选择直觉。 |
| 04842 | 保持关闭但重写理由 | 通用DPU通信研究，未有AI workload直接依据；不能说无机制。 |
| 04952 | 重开 | VQ shortlist+exact restricted routing降低granular MoE路由成本，明确执行机制。 |
| 04957 | 重开准入核对 | graph coupling破exchangeability，conditional spectral分解改变CP假设，不是dataset。 |
| 04970 | 重开 | 冻结模型的soft vocabulary skill tokens独立训练后zero-shot组合，对比weight/context替代。 |
| 05009 | 重开准入核对 | 同trust gate贯通training distillation与deployment ensemble；原无跨workload语句与摘要矛盾。 |
| 05025 | 重开准入核对 | 单pass attention-KL probe替代sampling，需与04638/05166同标准比较。 |
| 05040 | 重开 | reward-reweighted self-teacher目标与何时优于external teacher理论边界，非benchmark。 |
| 05045 | 重开准入核对 | perceptual robustness与relation correctness分離反证；需精确匹配VLM评估旧判断。 |
| 05113 | 重开 | finite-width recurrence t≈sqrt(n)失效尺度改变long-context初始化适用边界。 |
| 05166 | 重开 | first-content-token confidence匹配multi-sample agreement的低成本反证，改变UQ baseline。 |
| 05206 | 重开准入核对 | mask高norm无效→局部语义损伤及encoder/denoiser register分治，需核相对旧设计。 |

## Evidence 的实质错误

1. [04468 §3](https://arxiv.org/html/2605.04468v1#S3) 的“Limitations of Standard SFT”评价旧基线；不能充当 Anchored Learning 自身 limitation。应读 §4、§5 的支持/投影假设和 §6 设置。其 moving anchor 插值的是当前模型与**冻结 SFT reference**，不要误写为任意阶段更新 reference。
2. [04478 §2.3](https://arxiv.org/html/2605.04478v1#S2.SS3) 是 prior diagnostic works 的局限；不是 CCL-D limitation。当前字段没有证明新方法的覆盖/失效边界。
3. [05023 §2.1](https://arxiv.org/html/2605.05023v1#S2.SS1) 是 GPU 背景；真实 CuBridge 在 §3 的 CuIR/lifting/transformation/reconstruction。04077 Compared Methods、04116 Baseline Methods、04431 Compared Approaches、04665 Method=Evaluation Methodologies 同属错误角色，需回原文换字段。
4. 04454 Evaluation 指向“四层级”概念分类；04785 Evaluation 指向 core-rule latency property，均不等于本论文核心结果的评价合同。04263 仅用 ablation、04418/04543 仅附录实验，需补主比较设置与采用命题关联。
5. 04050、04058、04077、04213、04215、04266、04295、04333、04357、04418、04431、04454、04477、04572、04595、04700、04709、04808、04960、05049、05112、05191 的 limitation 多为 conclusion 首句；04496/04785 只留“有若干局限”的空前缀；05092 留投稿说明。必须写实际直接限制，不能在结尾套“限论文条件”代替。
6. [04209 §6](https://arxiv.org/html/2605.04209v1#S6) 是 Sparse-PCA 硬度假设下的 **computational** indistinguishability，参考是 Gaussian-dithered clean distribution；report 中 statistically hidden 的措辞错误。
7. [05097 v1 HTML](https://arxiv.org/html/2605.05097v1) 有 13-document Appendix 动力学实验，而 stored abstract 称无实验，需核对版本/摘要内容边界。该实验未报告 retrieval metric/competitive baseline；采用命题应是每 edge fast/slow 耦合，不是 weights/retrieval/episodic 三层。

## Books：可执行修复与已解决项

下表保留发现时的问题快照；本轮随后完成的修改，以后面的“最终正文回读”状态为准，不应继续把已修正项当作待写回。

| 范围 | 现状 / 要求 |
| --- | --- |
| Ch54 / 04450 | **已解决**：独立回读确认 EMB/KV hot-cache 专属段及 source marker 已由 root 删除；memory breakdown→physical layout衔接成立。旧 queue/comparison 仍声称35/35且含04450，需标 superseded，不能作为active验收。 |
| Ch49 / 04563，原1399–1405 | RangeGuard真实机制是 HBM bit-error→RID range metadata ECC→代表值有界替换；旧正文变成approximate kernel超界重算/提高精度，不成立。root正在协调修复，回读前未验收。[exact-v1](https://arxiv.org/html/2605.04563v1#S5) |
| Ch77 / 04811，原1205–1211 | TreeMem是builder/summarizer/retriever策略的树分支Monte Carlo downstream reward credit，不是memory节点写入审批/lineage责任树。root正在协调修复。[exact-v1](https://arxiv.org/html/2605.04811v1#S3) |
| Ch33 / 04960、05112，原1528–1532 | 只有泛化entropy/pass-rate原则，缺真正信号和state flow。EP-GRPO：entropy sigmoid门控outcome幅度；frozen-ref log-ratio按outcome或raw reward符号定向；累计entropy分桶归一化后合并。PS：成功/失败prefix分别帮助hard/阻碍easy bucket→重放原executor重建state→current-policy continuation→旧prefix loss mask=0。二者不证明逐步正确性或通用最优curriculum。[04960 §V](https://arxiv.org/html/2605.04960v1#S5)，[05112 §2/Appendix A](https://arxiv.org/html/2605.05112v1#S2) |
| Ch66 / 04624，原2445 | 不是execution trace与judge意见冲突，而是selector使用evaluator signal改变修复选择，channel blocking对照导致排名改变。需写真正测量对象，不要借paper支持一般冻结identity原则。[exact-v1](https://arxiv.org/html/2605.04624v1#S1) |
| Ch31 / 04913、04984，原640 | LoPT缺midpoint task-gradient边界与前半feature reconstruction；SIOP缺future-answer semantic clusters及可靠性分布；一句local objective/weak credit不足承载整合。 |
| Ch36 / 05049，原1184 | 已查 §VI-A确有按token imbalance触发intra-group expert migration，不能一概删除动态机制；但按链路状态在线调整pipeline未找到支持，须删/标独立工程推论。CCL-D恢复动作也应与诊断证据分开。[Piper](https://arxiv.org/html/2605.05049v1#S6) |
| Ch72 / 04446、04698，原1595–1599 | Misrouter是弱对齐expert安全路由攻击，capacity contention/isolation另需来源；04698没有建立LLM supply-chain delayed lineage/revocation机制。限定原证据或移除归因，不以工程常识代论文增量。 |
| Ch25 / 04709、05092；Ch26 / 04678 | ELVIS的GMM多模态计划+shared uncertainty-return、latent-action的formulation-task对照未被具体承载；Driver-WM被放大成通用world-state治理。重评准入后限定写回。 |
| Ch28 / 04711；Ch84 / 05170 | BAOC逐block optimizer-state预算机制已实际写入；Design Conductor明确区分论文案例与工程commit协议，回读方向正确。不能由这两项代表其它Books通过。 |
| 当前51项mapping | §5、old queue、comparison的分母不一致。给每项真实body anchor+支持命题+直接边界；04061/04261/04700/04874/04893/05029/05116尚无identity绑定。No Change也须具体比较，不得用“owner已有相关原则”替代。 |

### 本轮最终正文回读

主任务修复后，本 reviewer 再次实际读取正文与邻接段，确认以下主要错配已解决：

- Ch54/04450：专属段与marker已删除，未继续用generative recommender类比充当LLM证据。
- Ch49/04563：已写出RID→保存ECC冗余→丢弃显式RID→读时重建/解码→范围代表值，不再冒充kernel误差重算路径。
- Ch77/04811：已定位memory-construction policy的树分支Monte Carlo credit，明确不提供线上memory写入authority或lineage。
- Ch33/04960：已补entropy-gated幅度、frozen-reference divergence、累计entropy桶内标准化，以及零reward方差时threshold符号分支；自监督proxy与逐步正确性分开。
- Ch33/05112：已补0/8、8/8过滤，3–5/8普通训练，1–2/8成功prefix与6–7/8失败prefix；原executor重放与current-policy continuation、prefix mask分开。
- Ch66/04624：已改为repair selector使用evaluator signal造成coupling、channel-blocking对照，不再用一般trace/judge意见冲突替代研究对象。
- Ch31/04913、04984：已补midpoint任务梯度/前段feature reconstruction与future-answer cluster/potential机制；这是核心缺失已补的正文确认，不能代替尚待作者整理的完整exact-v1证据与disposition。
- Ch36/04478、05049：已将诊断与remediation authority分开；Piper收窄到token imbalance触发intra-group expert迁移，不再声称按链路任意改pipeline。
- Ch72/04446、04698：已删除capacity contention的论文事实归因，另列工程控制；04698未支撑的delayed-ingestion/lineage段及其marker已删除。因此当前ledger的04698“整合”必须同步反转，不能沿用旧queue。

这些局部修正不解决候选分母、78项证据字段、全部分数和其余Books映射；总体仍未通过。Markdown本地链接存在性检查、V3 validator与全工作树diff-check均通过；远端论文链接在上述定点原文访问中核验，不声称所有远端链接均重新访问。

## 当前51项 Integrate 的统一复核映射

此表只对当前 ledger 51项逐一映射，不继承旧35项queue；行号为复核当时的导航线索，共享Books后续修改可能移动，不能用行号或marker替代正文再读。

| suffix | owner | 当前目标/已读位置 | 复核状态 |
| --- | --- | --- | --- |
| 04050 | AGENT-CONTEXT | [75-context.md](../../../../../books/part-07-agent/75-context.md)，复核时约 L258 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04061 | MODEL-SELF-ATTENTION | [14-self-attention.md](../../../../../books/part-02-model/14-self-attention.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 04077 | TRAIN-GRPO | [33-grpo.md](../../../../../books/part-04-training-system/33-grpo.md)，复核时约 L1710 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04116 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，复核时约 L1587 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04135 | PLATFORM-EVALUATION-SYSTEM | [66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，复核时约 L2416 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04209 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，复核时约 L1583 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04213 | PLATFORM-MONITORING | [67-monitoring.md](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)，复核时约 L387 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04215 | MULTIMODAL-GENERATIVE-PARADIGMS | [24-multimodal-generative-paradigms.md](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，复核时约 L544 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04261 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 04263 | INFER-SPECULATIVE-DECODING | [48-speculative-decoding.md](../../../../../books/part-05-inference-system/48-speculative-decoding.md)，复核时约 L711 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04266 | TRAIN-RLHF | [31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)，复核时约 L624 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04269 | TRAIN-PRETRAINING | [28-pretraining.md](../../../../../books/part-04-training-system/28-pretraining.md)，复核时约 L945 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04333 | TRAIN-DISTRIBUTED-TRAINING | [36-distributed-training.md](../../../../../books/part-04-training-system/36-distributed-training.md)，复核时约 L1158 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04341 | TRAIN-LORA | [30-lora.md](../../../../../books/part-04-training-system/30-lora.md)，复核时约 L473 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04357 | INFER-SCHEDULING | [56-inference-scheduling.md](../../../../../books/part-05-inference-system/56-inference-scheduling.md)，复核时约 L983 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04361 | AGENT-CONTEXT | [75-context.md](../../../../../books/part-07-agent/75-context.md)，复核时约 L429 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04418 | TRAIN-PRETRAINING | [28-pretraining.md](../../../../../books/part-04-training-system/28-pretraining.md)，复核时约 L949 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04431 | TRAIN-RLHF | [31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)，复核时约 L630 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04446 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，复核时约 L1593 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04468 | TRAIN-SFT | [29-sft.md](../../../../../books/part-04-training-system/29-sft.md)，复核时约 L582 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04477 | TRAIN-RLHF | [31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)，复核时约 L636 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04478 | TRAIN-DISTRIBUTED-TRAINING | [36-distributed-training.md](../../../../../books/part-04-training-system/36-distributed-training.md)，复核时约 L1180 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04496 | AGENT-CONTEXT | [75-context.md](../../../../../books/part-07-agent/75-context.md)，复核时约 L441 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04563 | INFER-TENSORRT-LLM | [49-tensorrt-llm.md](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，复核时约 L1399 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04572 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，复核时约 L1597 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04624 | PLATFORM-EVALUATION-SYSTEM | [66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，复核时约 L2443 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04665 | PLATFORM-EVALUATION-SYSTEM | [66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，复核时约 L2445 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04678 | MULTIMODAL-EMBODIED-VLA | [26-multimodal-embodied-vla.md](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，复核时约 L707 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04698 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，原约 L1597 | root已删除不当段与marker；作者须将整合反转，不能视为仍有正文承载 |
| 04700 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 04709 | MULTIMODAL-WORLD-MODELS | [25-multimodal-world-models.md](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，复核时约 L945 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04711 | TRAIN-PRETRAINING | [28-pretraining.md](../../../../../books/part-04-training-system/28-pretraining.md)，复核时约 L953 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04719 | TRAIN-RLHF | [31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)，复核时约 L640 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04811 | AGENT-MEMORY | [77-memory.md](../../../../../books/part-07-agent/77-memory.md)，复核时约 L1205 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04874 | TRAIN-DPO | [34-dpo.md](../../../../../books/part-04-training-system/34-dpo.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 04893 | PLATFORM-EVALUATION-SYSTEM | [66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 04901 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，复核时约 L1535 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04913 | TRAIN-RLHF | [31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)，复核时约 L640 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04932 | PLATFORM-EVALUATION-SYSTEM | [66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，复核时约 L2447 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04960 | TRAIN-GRPO | [33-grpo.md](../../../../../books/part-04-training-system/33-grpo.md)，复核时约 L1528 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04984 | TRAIN-RLHF | [31-rlhf.md](../../../../../books/part-04-training-system/31-rlhf.md)，复核时约 L640 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 04992 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md)，复核时约 L1599 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05007 | AGENT-MULTI-AGENT | [82-multi-agent.md](../../../../../books/part-07-agent/82-multi-agent.md)，复核时约 L684 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05023 | INFER-TENSORRT-LLM | [49-tensorrt-llm.md](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)，复核时约 L1557 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05029 | MULTIMODAL-WORLD-MODELS | [25-multimodal-world-models.md](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 05049 | TRAIN-DISTRIBUTED-TRAINING | [36-distributed-training.md](../../../../../books/part-04-training-system/36-distributed-training.md)，复核时约 L1184 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05090 | PLATFORM-EVALUATION-SYSTEM | [66-evaluation-system.md](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，复核时约 L2447 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05092 | MULTIMODAL-WORLD-MODELS | [25-multimodal-world-models.md](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，复核时约 L955 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05112 | TRAIN-GRPO | [33-grpo.md](../../../../../books/part-04-training-system/33-grpo.md)，复核时约 L1552 | 已读正文；具体通过/缺陷按上表，非全项验收 |
| 05116 | PLATFORM-SECURITY | [72-security.md](../../../../../books/part-06-ai-infrastructure/72-security.md) | 未找到identity绑定；作者补具体锚点或改disposition |
| 05170 | AGENT-PLATFORM | [84-agent-platform.md](../../../../../books/part-07-agent/84-agent-platform.md)，复核时约 L391 | 已读正文；具体通过/缺陷按上表，非全项验收 |

## 作者必须重开的主题簇

- 蒸馏/训练信号：04059、04065、04078、04542、05040。
- 评价纠错与低成本sensor：04180、04243、04251、04763、05025、05045、05166。
- 安全/信任与runtime保护：04091、04305、04373。
- 模型理论与状态边界：04100、04115、04330、04421、05113。
- 执行/适配/量化与条件机制：04651、04738、04754、04952、04957、04970、05009、05206。

上述共28项，其中17项明确应重开、11项需重新准入核对；作者还应扩查相同错误理由族，不仅修样本。正向池须重审04264、04698、05092；05097先解决摘要/全文边界与采用命题，不以无实验作为一刀切排除理由。最终候选分母由修后的作者筛选冻结，reviewer不以抽样外推新总数。

## 结论

**未通过。** 身份算术与日期口径可以保留，但筛选、Source Review、评分及 Books 仍有实质缺陷。作者先重开错误关闭族，校准候选采用命题与字段，再由非作者按修后集合重新验收。不得把本文件、78张表或 validator 通过称为完整研究完成证明。
