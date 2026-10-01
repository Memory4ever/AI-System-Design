# 2026-04-24 V3 贡献初筛

**最新恢复对账（2026-09-30）：** [Ramen 与 PrismaDV](V3_ROOT_REVERSE_ADMISSION_RAMEN_PRISMADV.md)、[HAT-VTR](V3_ROOT_HAT_VTR_REVERSE_ADMISSION.md)和[两项局部理论/诊断探针](V3_ROOT_TWO_THEORY_PROBE_REVERSE_ADMISSION.md)的当前处置均为具名贡献前关闭；[SPIRE先行公开反证](V3_ROOT_SPIRE_FIRST_PUBLIC_CORRECTION.md)另将20849移出本窗。下文旧“潜在”与 `5分仅报告` 为当时工作快照，不作为正式候选/评分。当前报表为85个未冻结工作家族，其余证据原样留存。逐族调整不把同类材料整体关掉。

作者 apr01；窗口 `[2026-04-23T09:00:00+08:00,2026-04-24T09:00:00+08:00)`。原始496身份标题浏览仅为有界查漏，不是逐项全文队列或候选分母。完整题摘来自本日 `arxiv-owner-replay-20260903/20260424/arxiv-owner-receipt.json` 对应身份；拟入选仍核exact-v1、撤回/纠错标记及本窗公开可用组合。以下是贡献判断，不把Updated改名为首发，也不提前冻结分母。

## 2026-09-28 收口校准快照（已由上方最新裁决覆盖）

原始 496 唯一标题、162 相关/含糊完整题摘的筛选范围不变。原 100 工作项经非作者贡献准入反查，20897、21203、21416 及下列六项已转具名前分母关闭；**当时**正式日报为 91 未冻结工作候选 = 90 arXiv 家族 + 1 GPT 模型/card 家族，其中 30 实际 Books 整合、10 拟已有覆盖、36 仅报告、15 中心争议，0 普通 Books 待办。此处及下文各阶段数字是过程快照，不覆盖上方最新数，也不代表日级 Gate 通过。

- `2604.21416v1`：CSC 实际对象是通用图像分类器的投毒防护；ResNet18/CIFAR10 的聚类与分类头再训练未建立对大模型训练、模型生命周期或 AI Infra 的直接设计增量。安全类比不足以准入；原 exact-v1 必要审阅留在 `V3_EVIDENCE_NOTES.md`，但当前不计候选、评分、仅报告或 Books。该纠正不改变当时 162 条完整题摘已读的历史筛选事实。

- `2604.21265v1`：音乐→诗歌→散文预训的容量/数据量取舍是受限任务 operating point；attention/FFN/norm 与 embedding/head 的迁移/重置、诗歌→散文共同更新未隔离所谓组件“orthogonal”贡献，也没有支持改动 Ch28 的现代预训练数据选择。原 §3–6 审阅与预算/seed 反证保留在 `V3_EVIDENCE_NOTES.md`，不以参数量小本身关闭。
- `2604.21592v1`：首帧全局读权与时间距同余稀疏连接服务特定 4D 形状生成，未证明一条超出 Ch24 局部/远期稀疏分账的可迁移选择边界；Table 2 只给该设置质量—FLOPs 取舍。无 anchor 的三项质量指标比 Ours 差，conservative/full attention 质量更好但计算更多；原精确数值保留，不用错误反证关闭。
- `2604.21677v1`：有理 activation 的接合光滑阶数、scale 与负半轴变体是局部算子选择；高阶 CNN 退步、GPT/BERT 参数排序反向，单独 elementwise CUDA 受带宽约束，未改变 Ch16/17 的大模型梯度/执行取舍。官方 PDF-v1 必要证据保留，不因小 GPT 硬拒。
- `2604.21776v1`：双 crop、2D warp anchor 与双流 token 训练改善单视频重拍，但没有 action-conditioned world transition 或真实 4D/物理状态的独立验收；对 Ch24/25 的主线仅能类比，未形成新长期生成/状态机制。原官方 v1 方法与限制保留。
- `2604.21772v1`：DOCO 在图像 open-set 分类中以 test-time prompt 补偿 frozen classifier 的已知/未知类别边界；现有必要证据未给出可迁移到大模型表示、推理服务或平台校准的独立机制/失效条件。不是因为视觉任务而排除，原受限结果与 Ch66 对照保留在 `V3_EVIDENCE_NOTES.md`。
- `2604.21461v1`：EgoPoint 的自我视角 pointing 基准分开 perception 与 reasoning，但 Ch66 已明确保留模态/时间必要性、视觉状态与规则解释等分账；本篇未进一步控制因果视觉线索或增加新的评价授权边界。不是因为具身领域而排除，原 benchmark 和诊断证据仍保留。

同一理由仍用于反查其它“受限可报告”行：先核是否真的改变现有判断或其适用条件；仅有领域应用、局部参数/算子 operating point 或跨主线类比，不因已完成全文或给出 5–6 分就保留。不能机械删光 Only，安全/纠错和真实设计反证仍须按原文定点保留。

## 独立准入纠正（覆盖下方旧工作标签）

root 复核已读 exact-v1 必要正文及 apr01 的贡献桥，apr01 再独立确认：`2604.20897v1` 的 matched-task irreversible-operation、affine-SAT 计数与 Kolmogorov 上界是抽象计算理论，未给本书 LLM/Infra 可执行的能耗、缓存或调度设计条件；`2604.21203v1` 的在线 SGD covariance 去偏限强凸、衰减步长及最优点 Hessian 等假设，未给 Transformer/Adam 训练或平台 uncertainty 的可迁移边界。两者都不因能映射 Ch70/Ch28 就准入。**终态均为具体前分母关闭**，不计候选、不评分、不进入 Books；以下旧“潜在/标准仅报告”只是保存的审阅过程，不是当前处置。必要证据保留在 `V3_EVIDENCE_NOTES.md`；若后续有真实大模型系统 workload/机制桥才定点重开。

## 最小消歧收口一：六项的必要正文裁决

本节是对下方旧工作标签的实际更新，不另扩标题/全文队列。作者实际打开对应官方 v1 HTML 的必要方法、评价和直接反证；日期与独立复核尚未通过，不据此计入确定的本窗候选。

- **20874 Root Theorem：恢复潜在贡献，纠错深入。** [v1](https://arxiv.org/html/2604.20874v1) §3–8把有限窗口、填充导致质量下降扩为无限任务必然累积历史、所有问题都归结为signal/token及唯一压缩架构。有限canonical state加有界read-time检索可以使context填充率不随任务次数增长；这并不违反有限窗口或给定填充下退化公理，却不满足“无限任务必增长历史”的中间桥。中心普遍结论需窄争议隔离，不否定作者受限session经验或所有context压缩价值。拟2+1+2=5，纠错Deep；日期/精确身份通过后才记候选与暂缓，不写Books。
- **20897 Watts-per-Intelligence II：潜在贡献已明确，标准仅报告提案。** [v1](https://arxiv.org/html/2604.20897v1) §3–5定义可恢复执行substrate、任务类描述的算法信息及universal-search成本，§7.1用共享affine解空间说明适配—恢复—部署horizon分账。其复杂度/操作成本模型不是GPU计时或任意cache命中率；无结构有限cache的渐近例不覆盖真实heavy-hitter分布。拟2+1+2=5；可报告该条件性理论对象，不将热力学界或joule示例作为现代LLM工程节能保证，暂不改Books。
- **20926 Parallel-Code World Models：具体前分母关闭。** [v1](https://arxiv.org/html/2604.20926v1) §2.1–2.3及Tables1–4的实际链是生成完整OpenMP代码、真实ThreadSanitizer/Caliper标注、teacher后验解释、预测器SFT，再作repair feedback。配对profiling减少环境噪声，但没有新partial-program可执行标签、拒绝/不确定性协议或改变代理可用边界的受控证据；主要收益为成熟执行反馈蒸馏在并行代码任务的应用。不是因已有章节或无LLM排除，也不否认受限race修复经验。贡献已关闭，不为它追完整首发史。
- **20938 HARBOR：恢复潜在贡献，构造/安全声明定点深入。** [v1](https://arxiv.org/html/2604.20938v1) §VI Eq2–6与§VII实现把warm flag、cold-start未知量和后验chance constraint接入配置选择，足以核验其保护边界。但Python评估替换了论文SAAS/NUTS、Matérn与acquisition实现；Boolean cube上Matérn5/2并非一般affine Hamming核。维度2、长度尺度1时，距离0/2/2√2的核值不满足k(2√2)=2k(2)−k(0)，不能称该替换仅rescaling。只隔离后验/实现等价及其保证，不否定全经验；拟2+2+2=6，纠错/保护Deep，Books采用待实际命题对照。
- **21026 MCAP：独立复核后恢复潜在贡献，5分标准审阅。** [v1](https://arxiv.org/html/2604.21026v1) 原先以“没有稳定性/error-bound合同”关闭不成立；apr20_resume 定点指出 §3.1.1，作者随后实际重开该节及 Appendix D，确认原文定义 prompt 分布下的 activation/FFN 信号期望，并给出独立采样、sub-Gaussian 与第k名边际差 Δk 条件下的 top-k recovery／方差—样本量关系。这使校准排序的可靠性条件成为可保留的受限贡献，拟2+1+2=5，不直接改Books。该稳定性对象不是 downstream loss、精度或任务正确性，12个purposeful prompts也不能冒充iid样本以获得公式保证。ConfigA保所有层并paging，B/C还跳层，不是相同质量策略；末层例外、低内存配置质量下降和profiling成本仍保留，不采用“50%容量即安全”。原组合性判断保留为实验归因限制，不再作为否认原文理论对象的关闭依据；日期与正式终态仍待本日核实。
- **20925 Group Homomorphism：具体前分母关闭，提请否定侧独立校准。** [v1](https://arxiv.org/html/2604.20925v1) III-A/B沿用homomorphism与variance loss，III-C加入分割/重建，III-D以g1逆乘g2和加法projection取相对运动。实际IV实验是受限Chaser/Evader模拟、PCA轴与趋近/远离解释，未新增group身份、非交换交互或物理transition验收的可迁移条件；作者也承认commutative结构不足以表示非对称agency。相对坐标组合与玩具演示尚未实质改变主线表示/WorldModel设计，不因参数小或无LLM拒。若独立复核指出具体新条件再定点重开，不全附件扩审。

六项把最小消歧36减少为30：三项潜在贡献、三项具体关闭。当前162条题摘工作标签更新为97潜在贡献、30最小消歧、34具体贡献关闭、1早家族关闭。该数仍不是冻结候选或审阅完成数；拟评分只说明必要审阅投入，日期未确认项不先在正式候选表评分。

## 最小消歧收口二：四项必要正文已读，日期与独立审阅仍分开

- **20987 COS-PLAY：恢复为潜在贡献。** [官方v1](https://arxiv.org/html/2604.20987v1) §3、§4.1–4.3、§5.2及Appendix F实际读取。它不仅把成功轨迹存成skill：决策侧action/retrieval与库侧segmentation/contract/curation由不同LoRA/奖励职责训练，滚动bank改变下一轮policy所见的状态分布；§5.2静态首版/终版bank与SFT/GRPO交叉对照显示policy-bank不匹配是受限失效分支。拟2+2+2=6；必要证据还不能把全部收益唯一归于共同训练，六游戏及训练后8B与未匹配训练成本的frontier比较不作普遍优越性。§4.3 episode-end检索reward与Appendix F skill-switch叙述有粒度差异，应保留而非补造精确credit。Ch84已实际读programmable skill contract及Feedback生命周期段，已有promotion/retirement并不等于已经承载双侧可训练选择与bank分布共适应；Books差异待独立采用核，不先宣称整合。
- **21018 Evolving ICL：恢复为潜在贡献。** [官方v1](https://arxiv.org/html/2604.21018v1) §4.2.1–4.2.2、Algorithm1及§5.1–5.2实际读取。warmup用测试答案oracle发现correct、移除已解题并从同一测试集建立demonstration pool；后续选择语义近邻，又把新解题加入pool。因此测量对象是依赖先前成功标签的跨问题适应过程，不是独立单题预算分配或可部署正确性selector。拟2+2+2=6，评价合同差异需深入核；output-token-matched不等同新增ICL prefill与oracle成本全匹配。四轮、warmup一轮、TopP=3及四次运行只限披露配置，GPT-5-Nano在ReasoningGym等例外保留。Ch66已有candidate coverage/selector与adaptive-stop分账，但是否明确承载测试集内跨题标签回流须读实际相邻命题后决定，不能仅同主题判Existing。
- **21251 CAP：恢复为纠错潜在贡献，不采用遗忘保证。** [官方v1](https://arxiv.org/html/2604.21251v1) §3.1–3.3、Eq1–4、Appendix B.1–B.2实际读取。冻结目标LLM、训练可撤销prefix生成器是行为抑制接口，不能证明参数信息被删除；Ch72的“Unlearning更要显式声明secret substrate与observer”正文已实际承载此边界，故这部分无需重复写。但中心条件互信息桥有独立问题：若每个benchmark query的reference answer是固定函数a(q)，则I(response;reference|q)=0；Appendix B把其他query的答案作为当前q的InfoNCE负例，未建立这些负例来自p(a|当前q)或与该条件互信息下界等价。这只隔离条件MI解释/理论保证及privacy-compliance外推，不否定其embedding surrogate可优化输出或所有经验。拟2+1+2=5，纠错Deep；需非作者核这个最小反例/条件分布桥，未核前不写Books或定整项争议已通过。
- **21308 CI-Work：恢复为评价/保护潜在贡献。** [官方v1](https://arxiv.org/html/2604.21308v1) §3–4.5、§5.1及Appendix E实际读取。相同enterprise observation混入essential与sensitive entries，分别测essential conveyance、按sensitive条目归一化leakage和任一泄漏的case violation，避免安全地不说任何内容被当任务成功。拟2+2+2=6，保护评价必要深入核。125个种子（25人工+100生成）、每例4+4entries、五flow方向，GPT-5.2生成/模拟/judge构成同源评价而非真实企业incident；人工一致性不等于perfect oracle。Appendix E相关统计单位是model–direction aggregate，不是仅九个model，因此不能用n=9直接判p值错误；同模型/同种子相关性仍限制独立性与因果trade-off。Ch72已实际读value→sink的purpose/authority边界，此处不同的是安全×任务完成的混合输入评价协议；最终Books owner优先核Ch66的具体已有安全分母，而非再写泛privacy原则。

这四项均从最小消歧转潜在贡献：162完整题摘当前101潜在、26最小消歧、34具体关闭、1早家族关闭。不是冻结分母或101篇已深审；拟分数仅表达必要投入，公开归属仍须单项日期证据，未确认者不进入正式确定候选表。没有实际Books写入或日级Gate。

## 最小消歧收口三：六项具体裁决

- **21155 Multi-Agent Empowerment：前分母关闭。** 完整题摘实际读出的对象是tendon耦合agent与Vicsek flock的intrinsic-control行为组织及empowerment计算，不是学习语言/基础模型表示、训练/推理执行或LLM协作的机制；将群体组织类比Ch82并不足以建立当前主线关系。不是因小模型、非LLM或无新runtime硬拒，本文的控制理论价值仍保留在原始身份。
- **21199 ARFBench：前分母关闭。** 完整题摘的生产telemetry题库、TSFM+VLM后训练和model-expert best-of-two oracle是具体应用评价；后者只显示候选互补上界，未给可执行selector或把oracle与实际incidence判断的新有效性条件分离。750题/内部真实telemetry不是独立准入理由，本次未看到改变Foundation/System主线设计的受控增量，不为“superhuman”宣传追全部附件。
- **21277 MMTR：前分母关闭。** [官方v1](https://arxiv.org/html/2604.21277v1) §3.1–3.2、§4.1–4.2的局部mask重构、多页输入、按长度组合lexical/semantic/judge，是已有masked-reconstruction任务与分层scorer的具体题库组合；人工筛unique答案及声称视觉必要并非无文本/无视觉受控证明。去掉显式QA不等于隔离instruction-following或消除语言prior，现有结果尚未形成新的因果辨别/发布条件。关闭不因文档领域窄或数据规模；保留其可复用任务资源身份，不采用“mask就防memorization”。
- **21555 CSC：前分母关闭。** [官方v1](https://arxiv.org/html/2604.21555v1) §3.1–3.4实际以随机位置插入articles与not/niet、比较归一化embedding-distance曲线。无下游classifier只去掉一个读出组件，并不将grammar扰动自动变成真值；articles插入不保证语义恒定、任意negation不保证唯一语义对照。该诊断尚未给足以改变主线表示选择的新增有效性条件或独立反证；不是因“已有embedding主题”拒收，也不把heuristic全部说成无效。
- **21505 Orchid：潜在评价贡献。** [官方v1](https://arxiv.org/html/2604.21505v1) §3各歧义定义、§4.1三阶段rewriting/人审、Fig7原/改写成对统计实际读取。它将同一函数requirement变成多可解释输入而仍沿用original tests，从而需要区分“模型功能失败”与“reference只接受原意”的评价责任，不是只新增更多代码题。拟2+1+2=5，标准审阅，尚须核§5具体协议及Ch66实际ambiguous-reference正文；不采用advanced模型必更差的普遍因果，也不把任意文案篡改变成有效ambiguity。
- **21765 PrismaDV：潜在方法/评价贡献。** [官方v1](https://arxiv.org/html/2604.21765v1) §4的data-code assumption graph、§5.1–5.3与§8.3实际读取。SIFTA按task–column失败unit及代码assumption回溯选择反馈，重凝缩观察后联合改耦合module prompts，而非只拿整体F1更新独立prompt；这改变稀疏执行反馈的诊断对象与选择性，不是纯框架命名。拟2+1+2=5，标准审阅/可能仅报告。15次完整evaluation预算、两seed、五数据集单表单文件，NewTasks只略胜manual及部分dataset反例限制transfer，不能称数据测试证明所有task正确或GEPA不能优化一般组合系统。原始下游应用不是唯一准入依据，本次保留的是反馈/中间artifact耦合机制。

六项最小消歧转2潜在+4具体关闭：162工作值为103潜在、20最小消歧、38具体关闭、1早家族。扣除下节21日期保留项后，普通工作为89潜在、13最小消歧；不是候选冻结/全文完成或Books产出。

## 最小消歧收口四：四项训练机制

- **21045 HPO：潜在贡献，公式/实现桥须深入核。** [v1](https://arxiv.org/html/2604.21045v1) §3.2–3.3、§4.1–4.3实际读取：句级hypothesis/reference对齐含null后，在quality低于阈值时令latency最差，再分别聚合并优化，改变低延迟可被空/错译投机的reward可用条件，不把旧InfiniSST KV架构当本篇新贡献。拟2+2+2=6。Eq4文本说latency独立标准化却用quality std；Eq7已外乘policy ratio而Eq8内部又ratio/clipped ratio，和通常一次ratio surrogate不同。以ratio=2、positive reward=1、clip上界1.2为例，Eq7/8非KL项为2.4而通常clipped项1.2，不能按印刷式同时采用“标准GRPO objective”声明。这可能是文稿/实现桥问题，不推代码必错或全部收益无效；需要精确公式勘误或对应loss实现。只对影响采用的桥深入核，不扩repo普通代码。
- **21160 GRCA：潜在贡献。** [v1](https://arxiv.org/html/2604.21160v1) §3.3–3.5/Eq6–10、§4.2/Table3实际读取：从JSON字符span回到token index，四geometry field各自group-standardize并只路由对应span，background单独advantage，再用reprojection全局reward。相比完整回答/集合候选/推理segment分账，是结构字段的reward-to-token接口，拟2+2+2=6。KPA是点在GT box内的containment，不是点坐标match或物理可执行；Qwen2.5-VL3B、ShapeNet/PointBERT、4×A80080GB、固定预算对照的IoU3D GRCA .683略低broadcast .684，不能只报KPA提升或宣称全面无alignment tax。Ch33既有集合span/segment和credit action-space正文已读，但具体字段parse错/背景credit责任是否需补仍待独立owner对照。
- **21203 SGD Covariance：潜在条件理论，拟仅报告。** [v1](https://arxiv.org/html/2604.21203v1) §3.1–3.3/Eq5–8、Assumptions4–6与Theorem7实际读取。利用当前迭代与窗口和的交叉项减自身outer product，双最近block递推处理相关SGD迭代的平均协方差，提供Hessian-free bias-reduction机制；不是单独又报optimizer收敛快。拟2+1+2=5，标准审阅。strong convexity、x*处Hessian、q≥8梯度矩、stochastic Lipschitz及衰减步长α∈(.5,1)等条件不适用于无条件Transformer/Adam训练，不写现代非凸训练uncertainty certificate。此阶段只核中心定义/实现/条件，不通读全部证明；Books若无可支持的主线迁移仅报告，而不把数学新意直接当工程保证。
- **21265 Ladder of Beauty：潜在受限训练证据。** [v1](https://arxiv.org/html/2604.21265v1) §2相关差异、§3.1–3.3、容量/transfer实验线索实际读取。同tokenization真实/合成music对照、music→poetry→prose分阶段和组件迁移，提供与容量交互的可核跨模态pretrain分支，不因33K～400K规模关闭，也不把既有music-transfer首创搬到本篇。拟2+1+2=5；必要审阅还须核组件reset/freeze与预算对照，摘要的“orthogonal”不是已证唯一因果。序列256、单头/8层小decoder、capacity-limited行为不推foundation-scale收益或普遍课程顺序。

四项均转潜在：162现107潜在、16最小消歧、38具体关闭、1早家族；扣除21日期保留项后普通工作为93潜在、9最小消歧。原有数据/反证不删，不把数学矛盾直接称实验被复现证伪，整日仍进行中。

## 最小消歧收口五：攻击搜索、纠错评价与训练保护

- **20945 Breaking Bad：具体前分母关闭，保护信号请求独立核。** [官方v1](https://arxiv.org/html/2604.20945v1) §3/Algorithm1及§4实际读取。先找refusal与gibberish系数边界，再在中间区间搜索最大compliance，是既有白盒steering的局部参数搜索；八模型的规模、family与量化并不构成匹配的单因素对照。此次没有分离新的可迁移保护有效性条件或攻击权限变化，不以排名直接准入，也不因安全题名全部深审。该关闭须非作者核真实威胁/反证，不宣称全部steering已被覆盖或不存在风险。
- **21159 Adaptive Instruction Composition：潜在方法贡献，5分标准提案。** [官方v1](https://arxiv.org/html/2604.21159v1) §4.1–4.3/Algorithm1、§8实际读取。组合的query/tactics先分别embedding、降维并拼接，再对每轮随机候选子池学习成功分布；成功组合去重迫使反馈在组合特征上泛化，与全部随机组合的搜索职责不同。拟2+1+2=5，可保留自适应搜索的具体预算/覆盖分支，而非HarmBench排名。三目标模型、同源judge与额外bandit GPU限定外推；embedding proxy不成为语义多样性真值或完整攻击空间覆盖，迁移与端到端成本仍需标准对照核后定Only/Existing，不先新写Books。
- **21232 ReCAPA：潜在贡献，5分纠错深入提案。** [官方v1](https://arxiv.org/html/2604.21232v1) §3.1–3.5及Appendix D.1–D.3实际读取。局部、subgoal、trajectory的不同对齐/重选职责可作为受限控制分支；EPR通过first-error及匹配的无前错trajectory比较后续风险，不能把observational matching叫因果干预。中心PAC定义不一致：主文Eq6是log后错概率的负斜率，D.3是q(k)/q(1)比值；q(1)=.5、q(2)=.25时前者为ln2、后者为.5，不是同一统计量。拟2+1+2=5，只隔离PAC实现/曲线解释及相应中心保证，不否定全部控制机制或经验；需对应统计实现/定义修正后定点重开，不无界读全附件。
- **21416 CSC：潜在训练保护贡献，6分安全深入提案。** [官方v1](https://arxiv.org/html/2604.21416v1) §3.2–3.3/§4实际读取。defender拥有完整训练管线，early latent clustering提议隔离样本，然后冻结feature extractor、将疑似poison改到virtual class并重训head；这不同于删样本或直接unlearning，但只是转移trigger→target关联，不证明trigger表示已消失。拟2+2+2=6，真实保护行为需核误隔离、clean accuracy及对适应性攻击的条件，近零ASR不当完全移除/LLM发布保证。尚需评价反证及Ch72实际分支对读，不能因图像分类或小规模直接关闭。

四项从最小消歧转3潜在+1具体关闭。当前162完整题摘为110潜在、12最小消歧、39具体关闭、1早家族；其中21日期保留项未变，普通工作96潜在、5最小消歧。它们不是冻结候选、110已证贡献或全文审阅完成。Books实际新增仍0；现有充分必要证据复用，只继续具体未决。

## 六项独立校准后的定点纠正

`V3_APR20_SIX_MINIMAL_ADMISSION_AUDIT.md`实际核六项，不是全162题摘校准。20874／20938窄争议、20897标准仅报告提案及20926／20925具体关闭在限定范围通过；21026按上文恢复。20897 §7.1的`nd+n`是给定表示下的编码上界，不是所有affine解空间的精确Kolmogorov复杂度；简单subspace仍可压缩，报告不采用等式或由此推实机能耗。最新工作值为**162=111潜在+12最小消歧+38具体关闭+1早家族**，21日期隔离未变；普通工作为97潜在与5最小消歧，仍未冻结、Books实际0。

## 最小消歧收口六：五项剩余边界已实际核

- **21461 EgoPoint：潜在受限评价贡献，拟2+1+2=5标准。** [官方v1](https://arxiv.org/html/2604.21461v1) §3.2、§4.1–4.5及Limitations实际读。模拟ray-cast给指向标签，真实指认另采；400个错误将近手干扰、忽略手势与定位正确后的推理失败分开，LoRA后的rescue只属于该错误子集。值得保留的是gesture-grounding与后续reasoning分账，而非11K题目本身；没有独立改变手势/距离/显著性的反事实控制，不能称已证明近手偏置唯一因果。真实域收益小于模拟域、问题短且单轮，拟仅报告或按Ch66实际诊断正文判已有，不先写Books。
- **21590 AgenticQwen：潜在数据机制贡献，拟2+2+2=6标准。** [官方v1](https://arxiv.org/html/2604.21590v1) §3.1–3.3、Algorithm1与§4实际读。线性轨迹先扩行为树，再反推使选定分支成为必需路径的environment/user/SOP三种输入职责；它不是仅增加随机难题。失败样本重写与同一Qwen3-235B三次一致不是真值oracle，mock tool/user及rubric奖励限制真实执行归因；未见独立剥离两flywheel的匹配消融，不采用模型总体优越性。后续与Ch27/Ch33的具体数据生成和反馈责任对读，不把旧retained/DeepComplete继承为本轮证据。
- **21592 Sculpt4D：潜在生成/执行分支，拟2+1+2=5标准。** [官方v1](https://arxiv.org/html/2604.21592v1) §3.2–3.3、§4.1–4.3、Table2与§7/8实际读。保留全部token但稀疏attention连接；全局首帧读权与按时间距改变block同余连接密度不同于删除远帧表示。该局部可行分支可报告，但block index同余不单独证明实际3D语义对应。经apr20_resume定点纠正：Table2无anchor的CD/IoU/F为.0986/.3442/.3375，Ours为.0972/.3451/.3383，无anchor三项均较差；真正应保留的取舍是conservative与full attention几何更好、计算更多。此受限消融不证明anchor普遍必要或全局最优。FLOPs非完整推理SLO，50对象、预训练3D模型和有限4D训练范围保留；不因4D应用硬排，也不以一个加速数字进入Books。
- **21677 GEM：潜在受限算子替代，拟2+1+2=5标准。** HTML失败后实际读[官方PDF v1](https://arxiv.org/pdf/2604.21677v1) §2.1–2.3、§3 CUDA说明与§3.2/3.3/4的关键反例。有理gate提供C^(2N)接合与scale调整的具体算术分支；光滑阶数并不保证较好学习，高N深CNN退步与GPT/BERT的epsilon排序反向保留。基型/EGEM负半轴仍零梯度，SE-GEM才改变该分支；独立elementwise kernel带宽受限，少运算不等端到端FFN加速或大模型胜出。可报告该受限替代，不先新增全局activation保证。
- **21766 AUDITA：具体前分母关闭。** [官方v1](https://arxiv.org/html/2604.21766v1) §3、§4.1/4.2、§5 Table4/§5.1–5.2及Appendix A实际读。已确有question-only/transcript/raw-audio消融，不能沿旧理由称没有；但测试对象是知识密集audio trivia，转录丢失非语言音频与IRT难度/区分度为成熟诊断组合。当前protocol未分离词汇知识、perception、时间必要性的新控制，也不能由低于chance证明“systematic miscalibration”唯一原因；尚未形成改变本项目模型/评估设计的独立新边界。关闭不因为音频领域或benchmark名称，不否定数据资源价值。

五项M转4潜在+1具体关闭；最新162为**115潜在+7最小消歧+39具体关闭+1早家族**。剩7M均在21日期隔离内，普通贡献消歧已收口；普通潜在101尚需必要证据与实际Books判断，非冻结101全文队列。`V3_APR02_COS_ICL_CAP_CI_INDEPENDENT.md`四项必要源→owner已实际读：三窄gap/一CAP窄D通过，不是写后或日Gate；CI seed的100扩充为Gemini-3-Pro，GPT-5.2在后续entries/episodes/trajectories与评价，避免把同源pipeline写错。来源机构仍以机构notes真实停点/限制为准，Books实际0。

## 日期例外清单

## 已独立采用核通过的三处 literal Books 提案与实际写后

root实际写后核：三家族正文已分别位于Ch84可更新Skill→admission、Ch66反馈成本→长期artifact、Ch66隐私成功→具身风险之间。逐段实际对读，未把已有一般lifecycle、oracle或权限原则声称为新缺口；相邻责任与共存分支保留。COSPLAY明确双侧policy/bank适配与有限预算；Evolving ICL明确跨测试标签池及未匹配prefill/oracle；CI-Work明确三个不同分母、25人工+100Gemini种子、GPT5.2后续链路和规范真值边界。独立apr02必要原文/实际owner结果已复用，无新增实现或性能断言；scoped diff检查通过，三处实际写后PASS。

日期复核仍明确证据种类：root重新打开arXiv官方availability的ID公告分配及常规slot，实际原字段和日内相邻簇共同支持本段的有限08–09范围推断；不是逐篇历史公告日志确证，Submitted/Updated/OAI/created不单独证明公开时刻。只对这三项采用，不扩及21具名例外，不宣称日级覆盖零遗漏；新的延期或早同家族反证将定点重开。此三项的采用/写后通过不是整日Gate。

### 三项写前日期联合依据（2026-09-27T21:21:58+08:00）

作者重新打开官方 [availability](https://info.arxiv.org/help/availability.html) 的 ID assignments 与 Announcement Schedule：永久 ID 在公告时分配，Wednesday14:00–Thursday14:00 的常规公告是 Thursday20:00 ET，即本日08:00 BJT；Submitted不是公开时刻。重新打开三项官方abs/v1核身份和原始提交字段，并实际对读原始库存：20987／21018／21308 的v1处理字段分别04/24T00:03:33Z、00:05:28Z、00:26:04Z，OAI当前datestamp均04/24；它们处在本日20844起的同一递增处理簇，首项处理00:00:05Z，均未跨09:00截点。按官方公告分配、常规slot、相邻批次处理簇及精确v1身份组合，有限推断这三项公开范围为 `[2026-04-24T08:00:00+08:00,2026-04-24T09:00:00+08:00)`，不是把Updated／OAI／DOI created改名为首发，也不是逐篇公告日志确证。当前官方月列表返回429，未用于支持日期；三项未发现更早同家族正文线索。对本日跨截点21身份仍按具名例外隔离，不将该组合无条件外推整批。后续若取得早公开或延期公告反证，只重开这些受影响家族和其采用链；本日独立日期Gate仍由root验收。

作者实际读 Ch84 的 Skill compilation、updater/adoption/outcome与model×harness cross-product，Ch66 Snapshot/feedback及Outcome Witness/MyPhone相邻正文，并读Ch83及Ch65/67交接。下列只是拟落笔文字；apr02源→owner有限通过不等写锁、实际整合或写后通过。三家族v1 processing字段分别为04/24T00:03:33Z／00:05:28Z／00:26:04Z，OAI本日与连续同批身份相容，拟按官方公告slot/ID分配/相邻批次联合推08–09；字段本身不叫公开时刻，例外与批次日级依据仍须复核。

**20987 → AGENT-PLATFORM / Ch84，拟插入“Skill的可更新性”fault-localized机制之后、Skill admission三层之前。** 拟正文：“库维护也可能由可训练策略承担：决策策略选择action与retrieval，维护策略则选择trajectory segmentation、skill contract与curation。决策产生维护数据，维护又改变决策所见的检索分布，因此应分开登记两侧目标、reward与bank状态，并以冻结的policy×bank交叉测试辨别consumer升级和库升级。仅记录catalog版本或一次任务成功不能说明两侧兼容。” 代价/边界：“双侧训练增加rollout、库更新与回归组合成本；六游戏的8B受限实验不能保证共同训练普遍更好，episode-end与skill-switch奖励粒度仍待对应实现解释。分布或credit不清时保留冻结库/人工维护，而不是自动发布新bank。” 唯一证据20987v1 §3/4.1–4.3/5.2与F，不重复已有一般lifecycle原则。

**21018 → PLATFORM-EVALUATION-SYSTEM / Ch66，拟插入feedback-channel成本段后、长期artifact evolution前。** 拟正文：“反馈还可跨测试问题流动：oracle确认一题成功后，把成功回答放入共享demonstration pool、移除已解题，再供后续问题使用。这时评估单位是有标签反馈的题序与池状态轨迹，不是相互独立的单题部署正确率；应保存pool初始化/更新、题序、标签访问与邻居选择，并与无此反馈的冻结pool基线分账。” 代价/边界：“匹配输出tokens没有匹配新增ICL prefill、oracle与池维护成本，利用正确答案筛pool也不证明线上selector可用。有限四轮与少数API模型只能支持受限适应流程；无法恢复反馈时退回独立问题snapshot比较，不补造与部署等价。” 证据21018v1 §4.2/Alg1/5；正文active set与Alg1全test pool定义差异保留，不能默认为同一实现。

**21308 → PLATFORM-EVALUATION-SYSTEM / Ch66，拟插入MyPhone隐私×成功两段后、具身危险动作前。** 拟正文：“同一observation可同时含任务必需信息和敏感信息；应分别测必需entry的conveyance、敏感entry的leakage和至少一次泄漏的case violation。三者分母不同，低leakage可能只是沉默，低entry平均也不能消除少数整例违规；成功交集仍要绑定预先定义的用途/recipient与必要性规则。” 代价/边界：“这需要带entry标签的受控输入和额外judging，生成/模拟/评分同源会限制外部有效性；125个有限seed与4+4entries不代表真实企业incident分布，也不赋予judge规范真值。没有可核标注时保留人工/安全审计，不用平均泄漏率替代过程证据。” 证据21308v1 §3–5.1/E；25人工+100Gemini-3-Pro扩充，GPT5.2后续链路已修，不重复Ch72purpose authority。

## 日期例外的有限隔离（不把处理字段当首发）

当前101潜在贡献和26最小消歧中，下列21身份不能与其余早于01Z的处理簇一起推定09:00截点前公开。实际读库存原字段，另重开20972、21843、21921的官方abs/v1；这些页面提供Submitted与版本身份，并未提供单篇Announced时刻。官方常规Thu20:00EDT→Fri08:00BJT仅给通常公告slot，不给处理跨01Z条目的可验证上界。此处不判“实际晚公开”或自动回拨归属，只隔离本窗正面准入/评分/Books；恢复条件是官方公告清单或与该精确v1同身份的可验证首次公开正文/批次上界。

| 身份 | v1 Updated原字段（UTC；非首发） | 当前贡献阶段 | 具体额外边界 |
| --- | --- | --- | --- |
| 2604.20972 | 2026-04-24T04:25:49Z | 潜在 | Submitted04/22T18:05:29Z不能给公开上界；不能只据低序号拉回08点。 |
| 2604.21191 | 2026-05-05T00:48:33Z | 潜在 | OAI当前也是05/05；早Submitted不是首发，需原v1公开批次。 |
| 2604.21843 | 2026-04-24T01:00:09Z | 潜在 | 官方abs身份/题摘一致，但Submitted04/23T16:32:49Z不是公告。 |
| 2604.21854 | 2026-04-24T01:01:11Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21860 | 2026-04-24T01:01:31Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21873 | 2026-04-24T01:02:16Z | 最小消歧 | 日期隔离后不扩全文；题摘判断保存。 |
| 2604.21879 | 2026-04-24T01:02:25Z | 最小消歧 | 日期隔离后不扩全文；题摘判断保存。 |
| 2604.21882 | 2026-04-24T01:02:32Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21901 | 2026-04-24T01:03:37Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21904 | 2026-04-24T01:03:41Z | 最小消歧 | 日期隔离后不扩全文；题摘判断保存。 |
| 2604.21909 | 2026-04-24T01:04:02Z | 潜在 | 当前OAI05/15不能恢复v1首发上界。 |
| 2604.21911 | 2026-04-24T01:04:10Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21914 | 2026-04-24T01:04:20Z | 最小消歧 | 日期隔离后不扩全文；题摘判断保存。 |
| 2604.21915 | 2026-04-24T01:04:21Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21916 | 2026-04-24T01:04:25Z | 潜在 | OAI空不是不存在，仍缺公开上界。 |
| 2604.21921 | 2026-04-24T01:04:33Z | 最小消歧 | Seed公开目录04/23T00+08可能是日期粒度，且早于本窗起点；不能将午夜当精确首发或硬放本日。 |
| 2604.21923 | 2026-04-24T01:04:37Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21924 | 2026-04-24T01:04:39Z | 最小消歧 | 日期隔离后不扩全文；题摘判断保存。 |
| 2604.21927 | 2026-04-24T01:04:44Z | 潜在 | OAI空不是不存在，仍缺公开上界。 |
| 2604.21930 | 2026-04-24T01:04:47Z | 潜在 | 截点前公开上界未恢复。 |
| 2604.21931 | 2026-04-24T01:04:48Z | 最小消歧 | 日期隔离后不扩全文；题摘判断保存。 |

21=14潜在+7含糊。其余87潜在与19最小消歧仍是普通可执行工作，不宣称都已贡献准入或审阅完成；此前34具体关闭与1早同家族不受影响。此隔离不能替代本日arXiv覆盖，也不以53原始晚处理条目全数创建材料队列。

## 第一批：20条完整题摘的语义判断

| 身份 | 当前准入判断 | 原有判断、题摘实际新增与需要核验的选择 |
| --- | --- | --- |
| [2604.20844 AtomicRAG](https://arxiv.org/abs/2604.20844v1) | 前分母关闭 | 原子事实替代chunk、移除关系标签、PPR加relevance过滤是成熟粒度与图检索组合；题摘未隔离关系抽取误差的有效性条件或新的恢复机制，五基准任务提升不能单独改变检索设计判断。不是因为已有Ch76而排除。 |
| [2604.20849 SPIRE](https://arxiv.org/abs/2604.20849v1) | 拟准入 | 扁平chunk把结构与正文共同复制；路径集合定义addressable subdocument，query-time聚合摊销共享scaffolding、local/global context职责分离，需要核结构保留与引用预算如何共同约束取证，而非仅换HTML任务。 |
| [2604.20850 Association Is Not Similarity](https://arxiv.org/abs/2604.20850v1) | 窗前同家族关闭 | 初筛看到 transductive/inductive 与相似负例反证，贡献线索成立；定点恢复其官方关联 Zenodo DOI 后，已公开的同作者 AAR preprint 在 2026-02-14 含相同中心机制/反证，不是 April24 首发。不因早 Submitted 自动回拨，也不把此次 arXiv 公告重计分；具体原字段见文末日期复核。 |
| [2604.20854 ERA](https://arxiv.org/abs/2604.20854v1) | 拟准入 | internal/external独立Dirichlet belief mass加DST冲突对abstention objective，可能改变scalar置信度不足时的表示/优化选择；独立性和epistemic/aleatoric分解保证需必要公式核验，题摘结论尚未证实。 |
| [2604.20860 RealRoute](https://arxiv.org/abs/2604.20860v1) | 前分母关闭 | 并行跨源retrieve后verify是既有“先取证再决定/验证”组合；未给 source-agnostic completeness 保证或控制budget与错误归因的新条件，演示及multi-hop gains本身不构成长久增量。 |
| [2604.20874 Root Theorem](https://arxiv.org/abs/2604.20874v1) | 最小必要消歧 | 两个有限context公理推出质量随token无条件单调、唯一永久架构等强保证，可能有中心推导缺桥；先查其数学对象与假设是否真形成可采用/纠错的命题，不因“信息论”标签入选。 |
| [2604.20897 Watts-per-Intelligence II](https://arxiv.org/abs/2604.20897v1) | 最小必要消歧 | reusable substrate、class-specific speedup、恢复成本和部署horizon构成具体代价分账，但题摘的algorithmic-information→speedup桥是否是适用于本项目计算设计的条件性约束仍不清；只核中心定义/证明，不扩SAT引用树。 |
| [2604.20911 Omission Constraints](https://arxiv.org/abs/2604.20911v1) | 拟准入，保护审阅 | 生产policy被当跨turn保持时，三臂及token-matched内容对照发现禁止与要求类约束不同衰减；需核行为监控盲区、per-model重新注入条件与因果范围，不把单模型百分数推广为所有模型。 |
| [2604.20913 FairyFuse](https://arxiv.org/abs/2604.20913v1) | 拟准入 | ternary压缩并未自动消除解量化乘法；八子GEMV融合到AVX-512单loop揭示压缩把CPU memory-bound转compute-bound而GPU未必获益的实际执行分支，需要核kernel与端到端成本及模型质量身份。 |
| [2604.20915 Absorber LLM](https://arxiv.org/abs/2604.20915v1) | 拟准入 | 参数记忆若仅拟合历史token未保留context未来影响；以更新后contextless模型对齐原模型full-context未来行为改变TTT训练目标与state责任，需核代理/teacher可见性及流式成本，不采用“确保泛化”。 |
| [2604.20920 Gist Sparse Attention](https://arxiv.org/abs/2604.20920v1) | 拟准入 | 训练mask让gist承担chunk summary，再以query-gist选择并unfold原token，打通训练责任、selector bandwidth与读回预算；不是仅部署时剪KV，需核原KV常驻/带宽、query条件误差及continued-pretrain代价。 |
| [2604.20926 Parallel-Code World Models](https://arxiv.org/abs/2604.20926v1) | 最小必要消歧 | 真实工具race/profile标签蒸馏到预测器是成熟代理评价路线；题摘强调partial code工具不可运行，需核是否新增可检查的partial-state标签/可信度边界，而非只用代码域提高反馈成功率。 |
| [2604.20930 SafeRedirect](https://arxiv.org/abs/2604.20930v1) | 拟准入，保护审阅 | 任务本身要求危险完成时，允许失败、hard-stop和保留placeholder的多模型消融可修正“抑制/普通systemprompt足够”的保护条件；需核授权失败与实际执行隔离不能混同。 |
| [2604.20932 Adaptive RAG Defense](https://arxiv.org/abs/2604.20932v1) | 拟准入，保护审阅 | 全开防御造成retrieval utility损失，query-conditioned选择与攻击多向量实测是安全-utility独立证据；不把“接近零攻击”当形式保证，核模型选择、同预算与具体失败切片。 |
| [2604.20933 IRIS](https://arxiv.org/abs/2604.20933v1) | 拟准入 | self-play两类数据tilted risk由Rényi order控制梯度集中，按分布gap改变order是具体objective分支，需核固定点/权重/支持假设及adaptive schedule，不以少样本胜SFT外推训练效率。 |
| [2604.20938 HARBOR](https://arxiv.org/abs/2604.20938v1) | 最小必要消歧 | mixed-variable noisy BO、冷启动修正和posterior chance safety是否新增可复用acceptance/失效合同尚不清，flag-gated case与“数bits即胜manual”不能独立准入；只核cold-start与chance constraint机制。 |
| [2604.20943 Sleep-Consolidated Memory](https://arxiv.org/abs/2604.20943v1) | 前分母关闭 | working-memory、importance、离线consolidation与value-forgetting组合，用十turn/数百concepts验证局部召回；未提供区别已有分层memory的新增恢复、遗忘效用或失败有效性条件，生物类比不构成机制证明。 |
| [2604.20994 MCP Function Hijacking](https://arxiv.org/abs/2604.20994v1) | 拟准入，保护审阅 | adversarial function跨query/函数集转移，威胁对象是tool selection而非只向userprompt注入；需核payload入站权限、function-body/name/schema身份及guardrail边界，ASR仅BFCL配置。 |
| [2604.21026 MCAP](https://arxiv.org/abs/2604.21026v1) | 最小必要消歧 | load-time layer signal联合precision/residency可能改变校准owner，但摘要仅报告importance dispatch与有利配置；需先查Monte-Carlo估计对象/稳定性和可行性前提，不能因三存储tier/两precision术语直接retain。 |
| [2604.21428 Decoupled DiLoCo](https://arxiv.org/abs/2604.21428v1) | 拟准入 | 同步DiLoCo仍受慢/故障learner锁步，独立learner+fragment/min-quorum/adaptive grace/token-weight merging改变训练同步和故障责任；需核延迟/失效更新身份、真实vs模拟评价与质量损失，不采用零停机普遍保证。 |

当前20条：12拟准入、5最小消歧、3前分母关闭。只说明当前贡献口径，尚未最终去重/日期确认、未评分/证据完成；不把3关闭追全发表史，不把5消歧默认为候选。来源未收口，分母未冻结。

## 第二批：20条完整题摘的语义判断

本批实际读本日原始库存中以下20身份的完整题名与摘要，旧screening标签不继承。日期、exact-v1污染和撤回轻量核仍独立完成；“拟准入”不是证据通过。

| 身份 | 当前准入判断 | 原文具体机制或关闭依据 |
| --- | --- | --- |
| [2604.20851 HAT-VTR](https://arxiv.org/abs/2604.20851v1) | 拟准入 | query shift增大gallery hubness，memory校正similarity与temporal-consistency loss是检索迁移的具体反证/适配分支；核hubness诊断与冻结gallery、更新责任，不仅“12扰动benchmark”。 |
| [2604.20855 Caesar](https://arxiv.org/abs/2604.20855v1) | 前分母关闭 | 动态图导航、coverage探索及adversarial refinement组成creative deep research；摘要没有隔离新的可靠性/预算或可验证新颖性条件，creative输出提升不足以改成熟探索—综合选择。不是因为存在Agent章节。 |
| [2604.20859 KGiRAG](https://arxiv.org/abs/2604.20859v1) | 前分母关闭 | response quality驱动循环GraphRAG对单次baseline是成熟retrieve–assess–refine组合；HotPotQA语义质量提高未给新停止、纠错或取证有效性边界。 |
| [2604.20902 Frequency-Forcing](https://arxiv.org/abs/2604.20902v1) | 拟准入 | hard频率变换改变flow坐标，earlier-maturing辅助频率流则保持原pixel interpolation；可学习wavelet scratchpad不用外部teacher，形成soft-order与hard-coordinate的生成替代分支，核耦合和训练成本。 |
| [2604.20903 SUA](https://arxiv.org/abs/2604.20903v1) | 拟准入，保护审阅 | distribution sensitivity减entropy的scalar用于perturbed risk/calibration界及abstention，可能改变“entropy即可表置信”的边界；需核敏感度对象、归一化、worst-case桥及ambiguity collapse假设，不先采用保证。 |
| [2604.20904 Normative Simulacra](https://arxiv.org/abs/2604.20904v1) | 拟准入，保护审阅 | same completion对正确/随机错误norm universe的contrastive reward与SFT保守却不提高judgment correctness的受控反证，可能补context-conditional privacy训练验收；小说norm及judge不是现实法律/授权truth。 |
| [2604.20917 DexBench](https://arxiv.org/abs/2604.20917v1) | 拟准入 | 固定输入预测执行行为与为目标行为反推输入变更的配对接口，能测试forward-answer-only评价未覆盖的执行条件；核mutant oracle、paired难度/泄漏，不能以双题都对证明因果理解。 |
| [2604.20923 ILDR](https://arxiv.org/abs/2604.20923v1) | 拟准入 | held-out表征inter/intra ratio先于验证准确率、阈值触发optimizer干预形成early-stop诊断边界；核同holdout重复使用、阈值选择、跨seed与干预替代解释，不把几何提前信号当上线certificate。 |
| [2604.20925 Group Homomorphism](https://arxiv.org/abs/2604.20925v1) | 最小必要消歧 | group homomorphism结构约束联合object slots与相对运动表征，可能是不同于statistical-independence的学习分支；只核约束/损失实际如何强制分解与所测对照，不因infant/toy标签硬拒，也不把解释性声明当物理law保证。 |
| [2604.20936 AttentionBender](https://arxiv.org/abs/2604.20936v1) | 前分母关闭 | 创作性2D attention-map变换观察到分布式扭曲，题摘没有受控分离attention归因或可迁移控制有效性；4500生成数量与glitch aesthetic未改变本项目已有“attention不等可定位因果”判断。 |
| [2604.20937 SToP](https://arxiv.org/abs/2604.20937v1) | 拟准入 | MCQA保留的粗粒度线索掩盖fine-grounding剪枝坍塌，sink-score对多selector校正是评价切片和selector身份共同变化；核sink定义/对照/成本，不推广90%剪枝无损。 |
| [2604.20940 Sema](https://arxiv.org/abs/2604.20940v1) | 拟准入 | 人类连续playout transport与event-driven模型消费不一致；离散audio、lossless结构文本+visual tokens、bursty delivery去jitter buffer改变传输/消费边界。emulated WAN只是受限证据，核前端/回读成本与丢时序风险。 |
| [2604.20945 Breaking Bad](https://arxiv.org/abs/2604.20945v1) | 最小必要消歧，保护信号 | adaptive coefficient grid+US/RepE本身成熟；模型/量化差异下attackability排序是否有独立的新适用边界尚不明，只核攻击权限、matched配置和报告反例。不能单凭八模型排名retain或因“已有steering”略过安全差异。 |
| [2604.20972 Agreement Trap](https://arxiv.org/abs/2604.20972v1) | 拟准入，日期待核 | rule-grounded可辩护多答案与historical-label agreement的分母不同，同决策改变规则粒度的对照可能补EvalSpec；token-logprob并非逻辑证明。原v1processing跨截点，不能按本日库存强定当窗。 |
| [2604.20985 DP Model Merging](https://arxiv.org/abs/2604.20985v1) | 拟准入，保护审阅 | 同数据集不同privacy/utility训练资产的random selection与linear mixture分别进行RDP/PLD accounting，允许deployment目标变化而不重训；核correlation/组成机制与privacy保证条件，不认为后处理自动给任意更强DP。 |
| [2604.20987 COSPLAY](https://arxiv.org/abs/2604.20987v1) | 最小必要消歧 | decision agent与无标签rollout skillbank共同更新可能改变producer/consumer训练责任；摘要只列发现/合约/检索等成熟模块，需最小核独立loss/update与反证，不因六游戏增益自动retain。 |
| [2604.20995 VLAF](https://arxiv.org/abs/2604.20995v1) | 拟准入，保护审阅 | 强毒性场景提前refusal使oversight-dependent选择不被观察，value-conflict配对改变安全diagnostic支持；核monitoring干预、行为/表示证据与mitigation限界，不把单方向差异叫内部真实偏好。 |
| [2604.21003 Last Harness](https://arxiv.org/abs/2604.21003v1) | 前分母关闭 | worker/evaluator/evolver外再做meta-loop及对应meta-learning，是已知嵌套搜索重组；摘要给算法声明而无新可检查选择偏差/停止/泛化条件，不能采用“任何新领域无需人类工程”。 |
| [2604.21016 Stochastic Sharpness Gap](https://arxiv.org/abs/2604.21016v1) | 拟准入 | top-Hessian方向噪声强化三阶self-stabilization、SGD equilibrium低于GD 2/η，提供batchsize影响稳定性的一条条件性机制；核coupling和局部近似假设，不当所有Transformer规律。 |
| [2604.21018 Evolving In-context Demos](https://arxiv.org/abs/2604.21018v1) | 最小必要消歧 | warmup solved测试query成为其他query示例，生成分布与compute allocation共同变化；核“successful”oracle及同budget/dataflow是否新增可复用选择条件，而非普通adaptive sampling加prompt bank。 |

本批20：12拟准入、4最小消歧、4前分母关闭。累计40完整题摘：24拟准入、9最小消歧、7具体关闭。是工作范围，不是冻结分母；相关摘要可疑或存在重大安全/纠错信号时继续必要原文核验。

## 第三批：20条完整题摘的语义判断

以下20实际完整题摘来自同一原始库存。普通领域应用与模型主线机制分开，安全信号不因主题已有而略过。

| 身份 | 当前准入判断 | 原文具体机制或关闭依据 |
| --- | --- | --- |
| [2604.21041 Projected Gradient Unlearning](https://arxiv.org/abs/2604.21041v1) | 拟准入，保护审阅 | 下游无关数据fine-tune使概念复活，retain激活CoreGradientSpace的正交更新硬化与concept类型差异改变unlearning生命周期验收；核哪些更新受约束，不能把投影保证推广任意攻击者/训练。 |
| [2604.21044 Active Data](https://arxiv.org/abs/2604.21044v1) | 前分母关闭 | atomic active对象分解及air-traffic implementation是一般复杂数据设计/领域应用；题摘没有模型学习、训练、生成或Infra的新机制桥，不因“data/AI”词强入范围。 |
| [2604.21045 HPO Speech](https://arxiv.org/abs/2604.21045v1) | 最小必要消歧 | dialogue KV复用是已有baseline，hierarchical reward与segmentation如何较质量/延迟成熟多目标形成新credit分工未明确；只核层级决策对象和消融，语言任务收益不自动retain。 |
| [2604.21046 JEPAMatch](https://arxiv.org/abs/2604.21046v1) | 前分母关闭 | FlexMatch loss叠加LeJEPA latent regularization是成熟伪标签+几何正则组合；题摘未分离新的class-imbalance条件、保证或负面设计证据，仅分类基准提高/收敛加速不足。不是因CIFAR小模型拒绝。 |
| [2604.21057 TRACES](https://arxiv.org/abs/2604.21057v1) | 拟准入 | reasoning-step角色实时标签与到正确答案后的行为迁移给early-stop sensor，困难题质量代价明显变陡；核标签/正确性oracle与在线额外成本，不把角色变更当内部已知正确或token节约等latency。 |
| [2604.21072 BloomBee](https://arxiv.org/abs/2604.21072v1) | 拟准入 | 互联网低带宽下layer assignment、microbatch、offload联立DP与lossless/speculation共同优化通信，改变只做单一分区选择；核全部负载、端到端/同步代价和旧已写Ch56是否真实承载。 |
| [2604.21079 Foveated Reasoner](https://arxiv.org/abs/2604.21079v1) | 拟准入 | 单一AR轨迹中按需触发crop并回注高分辨率证据，RL惩罚see-everything使训练职责与读入预算联合；核same-trajectory状态/KV兼容、低token质量与extra观察成本，不叫精确cache复用。 |
| [2604.21083 GateScope](https://arxiv.org/abs/2604.21083v1) | 拟准入，保护审阅 | 商用gateway所称model身份、truncation、billing与latency的black-box测量可修正“API标签等执行身份”；核行为测试能识别与不能证明的替换/缓存，费用配置和同query对照，不能凭输出差异确定内部路由。 |
| [2604.21098 Propensity Inference](https://arxiv.org/abs/2604.21098v1) | 拟准入，保护审阅 | strategic/non-strategic环境因素分离、Bayesian effect估计与避免circular analysis，提供对行为归因为战略性的受控反证；核因子支持、capability相关性与不确定性，不由等影响推模型无战略行为。 |
| [2604.21100 Preconditioned DeltaNet](https://arxiv.org/abs/2604.21100v1) | 拟准入 | online least-squares曲率从first-order delta到exact preconditioning等价再diagonal近似及chunkparallel，改变recurrence状态更新；核近似/稳定性和额外统计成本，340M/1B不外推所有长上下文。 |
| [2604.21106 Iso-Depth Loops](https://arxiv.org/abs/2604.21106v1) | 拟准入 | 精确v1在固定20个有效blocks、full BPTT及匹配FLOPs下比较权重共享/宽度/tokens，区分unique parameters与执行深度的容量与成本；原库存truncated-BPTT/hyperconnection实验来自后版口径，本轮删除该准入依据。v1仅将这些改动列为未来工作；核联合拟合/heldout/预算，φ不是普遍常数。 |
| [2604.21131 Cross-Session Threats](https://arxiv.org/abs/2604.21131v1) | 拟准入，保护审阅 | 多session共同payload与identity-anchor policy，FullLog在context足够仍低召回；coreset ranker重排破KVprefix与recall耦合是实际安全/serving边界。核人工rewrite与单correlator范围、CSR不等安全truth，禁止复合分数掩盖漏检。 |
| [2604.21134 IVG](https://arxiv.org/abs/2604.21134v1) | 前分母关闭 | chart specification查询+交互view消歧使用已有结构oracle与视觉证据路线，Plotly局部QA提升未分離新可检验权限/失效或truth合同；不因新增benchmark就retain。 |
| [2604.21139 Slot Machines](https://arxiv.org/abs/2604.21139v1) | 拟准入 | residual中current/prior entity可解码但factual retrieval只使用current，relational任务不同，具体反证揭示representation availability≠behavior use；核causal干预/slot分解，不将probe当所有模型机制。 |
| [2604.21155 Multi-Agent Empowerment](https://arxiv.org/abs/2604.21155v1) | 最小必要消歧 | intrinsic reward的multi-agent extension可能改变action-channel控制对象，但题摘只称principled/efficient和群体组织，未给具体extension；只核目标定义是否有直接学习/控制主线机制，不因tendon/Vicsek拒，也不凭group analogy保留。 |
| [2604.21159 Adaptive Instruction Composition](https://arxiv.org/abs/2604.21159v1) | 最小必要消歧，保护信号 | crowdsourced tactics组合contextual bandit+contrastive pretrain实现diversity/effectiveness，摘要可能只是成熟组合的新attack operating point；核budget/迁移反证和实际威胁变化，不自动把HarmBench排名当新保护条件。 |
| [2604.21160 Geometric Reward Credit](https://arxiv.org/abs/2604.21160v1) | 最小必要消歧 | field-specific reward只给对应geometry token spans、reprojection verifier可能是与global reward不同的credit分支；核真正loss责任及matched消融是否超出已知span assignment，不能把reprojection一致当物理几何真值。 |
| [2604.21164 MAGIC-TTS](https://arxiv.org/abs/2604.21164v1) | 拟准入 | local duration/pause条件输入、zero-value bias修正、missing-control支持改变生成条件训练边界；核未指定时回退与显式time目标/声学质量代价，不将首创声明当贡献证明。 |
| [2604.21189 Poisson CBF](https://arxiv.org/abs/2604.21189v1) | 拟准入，保护审阅 | sampled robot surface→resolution-dependent buffered free space→PSF/QP将有限采样约束连到连续body安全，是具体controller适用条件；核occupancy/动态估计/求解可行性假设，不把7DoF验证叫任意VLA安全。 |
| [2604.21190 SpatiO](https://arxiv.org/abs/2604.21190v1) | 前分母关闭 | 多种视觉prior specialists按观察reliability重加权是成熟heterogeneous ensemble/router组合；题摘没给可靠性标定/证据独立性的新条件，空间基准优于固定pipeline本身不改长期设计。 |

本批20：12拟准入、4最小消歧、4具体关闭；累计60完整题摘：36拟准入、13最小消歧、11关闭。仍未冻结；拟准入事件必须分别通过exact-version及本窗日期，未阅正文不称Evidence完成。

## 第四批：20条完整题摘的语义判断

本批原始库存完整题摘已实际读取；以下贡献判断与日期归属、exact-version及证据审阅分开。

| 身份 | 当前准入判断 | 原文具体机制或关闭依据 |
| --- | --- | --- |
| [2604.21191 Prefix Parsing](https://arxiv.org/abs/2604.21191v1) | 拟准入，日期待核 | 将prefix grammar变换到ordinary parser，再以algorithmic differentiation求全next-token weight，是约束生成可复用执行分支；需核加权空规则/循环和变换成本，不把语法合法性当语义或授权真。原processing跨截点。 |
| [2604.21192 VLA B1K](https://arxiv.org/abs/2604.21192v1) | 拟准入，保护审阅 | 终态progress score忽略到达路径，可能隐藏危险行为及不稳定重复；拟核实际trajectory-safety协议和reproducibility控制，而非因多一个机器人题库入选。 |
| [2604.21193 DAVinCI](https://arxiv.org/abs/2604.21193v1) | 前分母关闭 | internal/external attribution后接entailment与confidence calibration，是成熟两阶段测量组合；题摘列span/threshold/retrieval消融而无新因果或有效性条件，FEVER提升不足以改变这些责任的原判断，不以名称或high-stakes用途retain。 |
| [2604.21197 ProjRes](https://arxiv.org/abs/2604.21197v1) | 拟准入，保护审阅 | 以sample hidden vectors对共享gradient子空间的投影残差做被动membership，是具体泄漏接口；核rank/非正交梯度假设、攻击者可见性和DP accounting，不照录近100%或普遍抗DP。 |
| [2604.21199 ARFBench](https://arxiv.org/abs/2604.21199v1) | 最小必要消歧 | 软件incident时序QA和TSFM/VLM hybrid本身是任务组合；best-of-two expert/model oracle被称superhuman有评价信号，先核是否新增可迁移selector/oracle接口反证，或只明确局部oracle上界即可关闭，不因production数据直接retain。 |
| [2604.21203 SGD Covariance](https://arxiv.org/abs/2604.21203v1) | 最小必要消歧 | 全online去偏covariance且无Hessian有明确统计对象；需核用于训练不确定性判断的假设及具体偏差修正，不能因为纯理论而拒，也不把asymptotic rate直接赋给非凸Transformer。 |
| [2604.21215 Recurrent Transformer](https://arxiv.org/abs/2604.21215v1) | 拟准入 | 每层读取自身activation生成的KV，而非上一层状态；exact tiling声称减少prefill HBM量，形成temporal-depth与训练/执行依赖的新分支，核精确依赖与budget，不将parameter-matched当compute-matched。 |
| [2604.21221 Sparse Forcing](https://arxiv.org/abs/2604.21221v1) | 拟准入 | 训练中学习persistent visual block压缩/更新与局部稀疏，再由PBSA执行，是不同于部署剪KV的训练—kernel联合责任；核longrollout质量/刷新/成本，不推广无损或real-time SLO。 |
| [2604.21223 IRM Detection](https://arxiv.org/abs/2604.21223v1) | 前分母关闭 | 使用公开base/instruct模型的implicit reward作文本检测，题摘只给已知ratio信号的新检测operating point；没有新身份、失效或calibration保证，DetectRL胜排名不足以改本项目检测/概率边界，不因zero-shot自动保留。 |
| [2604.21229 EngramaBench](https://arxiv.org/abs/2604.21229v1) | 拟准入 | 同GPT4o条件下structured memory跨空间优而全局composite低，消融揭示specialization与aggregate相反代价；核30-query切片/成本/评分器和结构归因，不把同answerer当全部混杂已消除。 |
| [2604.21231 SparKV](https://arxiv.org/abs/2604.21231v2) | 撤回关闭，不入候选、不评分 | 当前官方v2明确withdrawn；Comments说明§4模型定义错误假设影响结论。已实际恢复处置说明，不是正文不可达。清除拟入选/采用链；原始v1阅读不支撑Books，不倒灌性能。保留本行必要撤回依据，不追版本史。 |
| [2604.21232 ReCAPA](https://arxiv.org/abs/2604.21232v1) | 最小必要消歧 | action/subgoal/trajectory三级Sinkhorn/scorefield对齐是否有新的预测纠错职责尚不明；先核实际loss与两个传播/恢复指标，不能用层级名词把成熟feedback组合扩成长久贡献。 |
| [2604.21241 CorridorVLA](https://arxiv.org/abs/2604.21241v1) | 拟准入 | Δposition稀疏anchor定义训练tolerance corridor，flowhead越界才纠正、界内另作一致性refinement，是显式空间监督支持分支；核anchor误差与真实动作/预算，训练约束不等执行安全。 |
| [2604.21251 CAP](https://arxiv.org/abs/2604.21251v1) | 最小必要消歧，保护信号 | RL训练promptgenerator却可撤prompt恢复知识，其“unlearning”与访问抑制契约需要区分；先核实际威胁和恢复对照是否新增独立反证，不因closed-source/prompt术语retain，也不直接采用合规删除声明。 |
| [2604.21253 PLOTTER](https://arxiv.org/abs/2604.21253v1) | 前分母关闭 | event/character graph上Evaluate–Plan–Revise后生成故事，是成熟结构计划与校验组合；题摘未分离新可验证causal constraint或全局coherence保证，局部叙事提升不改模型/Agent主线设计判断。 |
| [2604.21254 Hyperloop](https://arxiv.org/abs/2604.21254v1) | 拟准入 | middle-block复用与每loop后matrix residual结合，parameter memory与循环compute/latency分账有明确结构分支；核与depth/compute-matched及量化条件，不能称半参数等半运行成本。 |
| [2604.21255 AgentEcho](https://arxiv.org/abs/2604.21255v1) | 拟准入 | 任务mandatory与nonmandatory行为分开，再controlled distillation测action-graph convergence，可改变仅凭行为相似推教师来源的诊断；核task约束mask/causal支持，不由跨provider相似直接断言蒸馏。 |
| [2604.21265 Music Pretraining](https://arxiv.org/abs/2604.21265v1) | 最小必要消歧 | components分工与capacity-dependent data volume有受控负面/范围信号；先核全pipeline budget、拆component干预和plateau是否足以形成训练数据条件，而非仅音乐域成功。不能因400K模型硬拒或外推现代预训练。 |
| [2604.21268 GUI Proposer/Critic](https://arxiv.org/abs/2604.21268v1) | 拟准入 | 位置proposal渲染回图后由visualcritic选择、maturity-aware共同RL改变producer/selector目标分工；核成熟度定义及配对控制，pass@k可用性不等online selector已可靠。 |
| [2604.21275 Petastorm Pipeline](https://arxiv.org/abs/2604.21275v1) | 拟准入 | 共享worker queue race换专属round-robin队列/RNG和pushdown/cache，把吞吐与确定顺序责任分开；核exact order/worker failure/epoch种子及端到端profile，不以6倍数字代替严格determinism证明。 |

本批20：12拟准入、5最小消歧、3具体关闭；累计80完整题摘：48拟准入、18最小消歧、14关闭。只是主线标题导向的工作集合，不能将其比例外推到496 raw；未冻结、未最终确认日期或证据，不预支Books。

## 单项日期复核：20850 AAR

实际重新打开 [arXiv abs/v1](https://arxiv.org/abs/2604.20850v1)，其 Related DOI 指向 `10.5281/zenodo.18602385`；v1 Submitted 为 `2026-02-13T21:02:53Z`，仍不把提交当公开。网页工具无法读 Zenodo 页面后，定点读取官方 API `https://zenodo.org/api/records/18602385`，返回公开版本记录 [18636480](https://zenodo.org/records/18636480)：`status=published`、`access_right=open`、`publication_date=2026-02-14`、`created=2026-02-13T20:54:05.443399+00:00`、`modified=2026-02-13T20:54:05.821279+00:00`、`version=2.0`。这几种字段语义保持分开，不把记录创建时刻改为论文精确首公开。

官方题名 Association-Augmented Retrieval / Association≠Similarity、作者 Jason Dury、4.2M MLP/co-occurrence、transductive 增益而 inductive 无显著改善、相似非关联负例伤害检索均与 arXiv 家族中心一致。API 明确提供开放 preprint PDF，275061 bytes，并非仅搜索索引。足以确认本家族的必要正文早于 April 窗口已公开；不需展开所有版本史。此次 arXiv 项从拟准入改为窗前家族关闭，不删贡献线索，不在本日评分或新写 Books，也不声称已完整验收 February 原 owner。

80 条当前语义工作对账：**47 拟准入、18 最小消歧、14 具体贡献关闭、1 窗前同家族关闭**。此前48是初筛当时值；本表尚非最终当窗分母，拟准入仍分别核日期/版本/撤回及证据。

## 第五批：20条完整题摘

本批实际读取原始库存完整摘要，不把标题匹配或旧标签当贡献证据。

| 身份 | 判断 | 具体准入或关闭依据 |
| --- | --- | --- |
| [21276 ASR Priors](https://arxiv.org/abs/2604.21276v1) | 拟准入 | matched-prompt与噪声/静音/遮挡切片显示公平差距变小可只是全组WER恶化，压缩/重复插入与LLM尺度不等价；是ASR可靠性评价边界，不能从不同架构直接证明encoder唯一因果。 |
| [21277 MMTR-Bench](https://arxiv.org/abs/2604.21277v1) | 最小消歧 | 无prompt的masked-text恢复和level-aware协议可分instruction与视觉重构，但当前摘要仅声明隔离能力；需最小核输入支持/评价是否真的测到独立边界，不能以2771新任务准入。 |
| [21286 CE Load-Bearing](https://arxiv.org/abs/2604.21286v1) | 拟准入 | 预注册CE/MSE及bidirectional dynamics、失败的latent-movement manipulation与temperature后验消融分开，约束probe优越性的归因；只保留2.1M/CIFAR10/10seed范围，不推模型自知。 |
| [21308 CI-Work](https://arxiv.org/abs/2604.21308v1) | 最小消歧，保护信号 | 5信息流方向的essential-content/sensitive-context分账可能补泄漏评价合同；utility与泄漏相关和规模叙述尚不能证明新增机制，需要核授权对象、支持与切片，而非因enterprise benchmark保留。 |
| [21326 MiMIC](https://arxiv.org/abs/2604.21326v1) | 拟准入 | earlyfusion视觉collapse与latefusion语义misalignment呈不同压力，fusion-in-decoder加modality mixin/caption dropout承担缺caption训练责任；核控制因素，不把跨模型比较称完全因果。 |
| [21327 DDRL](https://arxiv.org/abs/2604.21327v1) | 拟准入 | pseudo-label中等consistency噪声被group-relative advantage放大，frequency选样/固定advantage/offpolicy共识更新是具体后训练信号分支，须核selection bias与固定信号不等真值。 |
| [21330 TGR-MoE](https://arxiv.org/abs/2604.21330v1) | 拟准入 | 稀疏router未选expert缺反馈，用dense teacher中间表示产生teacher-router监督是梯度支持分支；核teacher权限/构造和稀疏对照，vision有限任务不自动泛化语言MoE。 |
| [21335 Sub-Token Routing](https://arxiv.org/abs/2604.21335v1) | 拟准入 | retained token内分组V、保持Q/K不动且接在token reduction后，新增价值维度压缩与token删除的不同责任；核matchedbytes及执行成本，budget质量改善不等真实带宽已省。 |
| [21343 Latent Denoising](https://arxiv.org/abs/2604.21343v1) | 拟准入 | corruption在projected视觉token、目标在中层hidden重构teacher patch并保intra-image结构，改变语言loss对视觉的间接监督；推理关闭auxhead不退还训练成本，核分布移位消融与decoder预算。 |
| [21346 Symbolic Grounding](https://arxiv.org/abs/2604.21346v1) | 拟准入 | same-task rawimage与已知生成程序/结构输入作为diagnostic upperbound，控制format/conceptprompt/最小grounding后定位表示瓶颈；oracle符号输入非部署架构，也非所有视觉推理归因。 |
| [21361 Clock Skew](https://arxiv.org/abs/2604.21361v1) | 拟准入 | 注入单stage skew时功能/吞吐正常而negative span出现，运行中drift使违例非静态；是可观测因果证据与功能成功分开的受控反证，5ms不是通用阈值，Aeron未完成不计。 |
| [21375 VLAA-GUI](https://arxiv.org/abs/2604.21375v1) | 前分母关闭 | UI-success verifier、重复屏幕loopbreaker及按需search/coding/grounding组成成熟观察—校验—恢复；题摘消融给工具/预算实例收益，未新增可检查的停止有效性或恢复机制，排名/超人百分数不足以改该判断。 |
| [21391 ResVLA](https://arxiv.org/abs/2604.21391v1) | 拟准入 | spectral低频确定intent作为anchor、高频stochastic residual diffusion bridge，与纯噪声初始化不同的condition支持责任；核分解/动作质量和sim/real条件，不把频率等同意图真值。 |
| [21395 Geometric Blind Spot](https://arxiv.org/abs/2604.21395v1) | 拟准入 | task-loss cap下Gaussian isotropic encoder matching与Jacobian/clean class-layout反向结果，揭示减局部敏感不保clean geometry；线性Gaussian driftfloor和深网经验明确分开，不推普遍最优策略。 |
| [21396 VG-CoT](https://arxiv.org/abs/2604.21396v1) | 前分母关闭 | detection/OCR→GPT rationale→open-set refinement及rationale/answer/alignment三指标是成熟伪标签和评估组合；摘要没给grounding正确性/过程faithfulness新证据，自动与可扩展不等可信保证。 |
| [21406 HumDial](https://arxiv.org/abs/2604.21406v1) | 前分母关闭 | 双通道人录数据测interrupt/overlap/turn negotiation是已有duplex评价对象的新资源；题摘未提出新的ownership、uptake/时序判据或替代解释，不能仅新leaderboard准入。 |
| [21416 CSC](https://arxiv.org/abs/2604.21416v1) | 最小消歧，保护信号 | early latent DBSCAN辨毒后relabel虚拟class可能不同于unlearning，需最小核是不是新的可迁移保护行为及trigger访问边界，near-zeroASR不能自动保留或升形式保证。 |
| [21454 State-Tracking](https://arxiv.org/abs/2604.21454v1) | 拟准入 | matched transformer/hybrid和reasoning augmentation对照显示hybrid不是统一更准，sequential与flat-retrieval方向不同；需核预算/权重matched，不能把reasoningtoken有益推成state真实因果已证明。 |
| [21461 EgoPoint](https://arxiv.org/abs/2604.21461v1) | 最小消歧 | pointing被saliency/proximity替代有诊断信号，但11k规模/合成微调增益尚不独立揭示cue因果；需最小核视角/手势受控干预与真值支持，不因smartglasses主线自动retain。 |
| [21477 MCP Pitfall Lab](https://arxiv.org/abs/2604.21477v1) | 拟准入，保护审阅 | 静态本地metadata/schema/日志规则覆盖不了跨tool/image forwarding，实际trace+objectivevalidator区分静态finding、sink执行与attacker目标；核validator-completed分母，不把risk0当完整防御。必要正文已纠正原“semantic BOM”概括。 |

本批13拟准入、4最小消歧、3贡献关闭；累计**100完整题摘：60拟准入、22最小消歧、17贡献关闭、1窗前同家族关闭**。标题查漏来源仍496，非100篇确定当窗、非候选冻结、非证据完成；后续只读准入所需必要段，不能将496全体扩为全文队列。

## 第六批：20条完整题摘

| 身份 | 判断 | 实际摘要中的增量或待消歧点 |
| --- | --- | --- |
| [21480 DIVERT](https://arxiv.org/abs/2604.21480v1) | 拟准入 | full agent/environment snapshot恢复前缀后定向user-response分叉，将独立全rollout成本换覆盖引导；需核恢复身份与failure/token不等生产概率，无差别prefix复用不足替代实际环境state。 |
| [21505 Orchid](https://arxiv.org/abs/2604.21505v1) | 最小消歧 | 四类需求歧义和实现divergence是否有同题规范真值/多合法解支持尚需核；新1304任务及歧义伤性能常识不能独立改已有EvalSpec。 |
| [21511 SAE-SPLADE](https://arxiv.org/abs/2604.21511v1) | 拟准入 | token-indexed稀疏表示改成SAE concept索引，是lexical vocab身份与稀疏检索训练/部署的替代分支；核concept可迁移/训练成本，不把名称concept当语义真值。 |
| [21523 Evaluator Blind Spots](https://arxiv.org/abs/2604.21523v1) | 拟准入 | 40退化维度与单答/pairwise/reference三协议测试judge最低辨别力，局部好score不保发现图像反证；核可感知真值与任务支持，pairwise相对好不是可靠证书。 |
| [21549 Multicalibrated Prevalence](https://arxiv.org/abs/2604.21549v1) | 拟准入 | population shift下固定误差率纠偏失效，feature-conditional multicalibration给估计器条件保证；拟核覆盖/支持与统计假设，而非纳入公共卫生/政治领域应用本身。 |
| [21555 Separation Curves](https://arxiv.org/abs/2604.21555v1) | 最小消歧 | 去除下游classifier、对syntactic noise/semantic negation比较有具体诊断对象，但“客观概念捕获”可能只几何proxy；只核是否提供新受控边界，跨domain/length资源非充分准入。 |
| [21570 SpecSyn](https://arxiv.org/abs/2604.21570v1) | 拟准入 | semantic-non-equivalent程序mutants与variantdiscrimination检查spec强度，区别只让verifier接受当前实现；核变异真值和precision/recall对象，通关属性数不等真实NL需求完备。 |
| [21571 Separable Experts](https://arxiv.org/abs/2604.21571v1) | 拟准入，保护审阅 | userproxy删除称deterministicunlearning却baseline KL/verification仍有限，需核共享weights信息支持、cache/adapter效应与威胁；不接受“未进weights”自动抗所有membership/extraction。 |
| [21579 Metamorphic Repair](https://arxiv.org/abs/2604.21579v1) | 拟准入 | semantic-preserving变换和原NLL相关可诊断repair benchmark污染，但输入难度/分布移动与记忆仍可能混杂；是诊断authority边界，不把相关性当直接泄漏证明。 |
| [21590 AgenticQwen](https://arxiv.org/abs/2604.21590v1) | 最小消歧 | error难度flywheel与linear→branching行为树属于可执行curriculum线索，但摘要仍是synthetic/multiroundRL组合；仅核任务生成/更新协议是否新增独立设计条件，不因工业小模型成功retain。 |
| [21592 Sculpt4D](https://arxiv.org/abs/2604.21592v1) | 最小消歧 | initialframeanchor+time-decaying sparsemask是清楚表示分支，需核与普通reference/localattention的实际差异及4D依赖，而非56%计算数字或原3D模型迁移自动准入。 |
| [21593 polyGRPO](https://arxiv.org/abs/2604.21593v1) | 拟准入 | 语言受限/自由采样作为在线探索维度改变数据/偏好分布；核accuracy/reasoningstructure奖励、预算和英语迁移，不从prompt结果证明语言是内部latent路径。 |
| [21598 DryRUN](https://arxiv.org/abs/2604.21598v1) | 拟准入 | 去掉公开样例/真实执行信号后LLM自拟输入与模拟、hidden-test质量仍可比，可能限定public-test锚过拟合；核matched预算/外部teacher信号，不能推模拟等真实执行或保证正确。 |
| [21611 Verbal Process Supervision](https://arxiv.org/abs/2604.21611v1) | 拟准入 | matched-compute比较critiquegranularity且语言表达失败时收益下降，具体supervisor/actor gap条件；核预算和对照，不用r=.9当因果/第四轴普律。 |
| [21632 Unseen-token Collapse](https://arxiv.org/abs/2604.21632v1) | 拟准入 | 未训练unembedding趋同导致变量不可区分，copying/冻结/reset与数据diversity有受控对照，并有Gemma unusedtoken线索；核tied参数条件，不把symbolic小实验外推所有词义。 |
| [21677 GEM Activations](https://arxiv.org/abs/2604.21677v1) | 最小消歧 | rational算术/C2N平滑及CNN/Transformer参数反向偏好有具体函数条件；只核是否形成新的解释/执行取舍而非一组局部operatingpoints，不因理论或小GPT硬拒。 |
| [21681 Sapiens2](https://arxiv.org/abs/2604.21681v1) | 前分母关闭 | maskedreconstruction+selfdistilledcontrastive、窗口attention及人像数据扩展是成熟训练/表示组合；摘要多任务质量和规模未隔离目标相互作用或新稳定机制，不能仅更大基础模型/release准入。 |
| [21686 WorldMark](https://arxiv.org/abs/2604.21686v1) | 拟准入，已纠正库存后版摘要 | 原始v1 official abs/PDF为六模型共享WASD/LR adapter、同场景/动作与视觉/translation-rotation/consistency八指标；仅据此保留有限跨模型测量操作点，不采用库存十模型及direction purity/latency/stability扩展。adapter语义标定和VLM/SLAM proxy不等真实物理控制。必要原文已审，拟标准仅报告。 |
| [21700 BadStyle](https://arxiv.org/abs/2604.21700v1) | 拟准入，保护审阅 | 自然风格trigger加target在poison强化/benign抑制auxloss形成训练责任，prompt/PEFT注入权限与长生成payload分开；核输入/输出camouflage和真实可见性，不照录所有防御都失效。 |
| [21724 X-GRAM](https://arxiv.org/abs/2604.21724v1) | 拟准入 | 长尾undertraining/slotcollapse/layer需求不同由hybridhash/aliasmixing与depthgate注入value/residual回应，改变静态参数表的训练支持；核查询、表字节及执行成本，capacity-decoupled不等全部FLOPs零增。 |

本批14拟准入、5最小消歧、1贡献关闭；累计**120完整题摘：74拟准入、27最小消歧、18贡献关闭、1窗前家族关闭**。尚非冻结、当前也没有本日Books实际新增。此高比例是标题已收窄后定点读题摘的工作池，不代表496原始范围的大多数有长期贡献；必要段若显示只是成熟组合会据事实关闭并保留改判。

## 第七批：20条完整题摘

本批题摘已在上一执行段实际完整读取，本次恢复只保存未落盘裁决，不重复抓取或冒称完成证据审阅。

| 身份 | 判断 | 实际摘要中的增量或具体关闭依据 |
| --- | --- | --- |
| [21725 AEL](https://arxiv.org/abs/2604.21725v1) | 拟准入，已纠正库存后版摘要 | official abs/PDF/HTML v1题名为Agent Evolving Learning，fast Thompson retrieval与slow诊断/策略池扩展形成双时标操作点，有限portfolio反证复杂credit/扩池未必好；不采用库存后版support-ticket扩展及provably no-harm，不把金融指标/causal文字升级成保证。拟5标准仅报告。 |
| [21728 Ramen](https://arxiv.org/abs/2604.21728v1) | 拟准入 | mixed-domain TTA按域一致性/预测平衡选缓存，再复用embedding-gradient而非重新前后向；须核旧梯度对应参数状态与缓存有效性，不能把无额外forward等同无维护成本。 |
| [21741 HiWM](https://arxiv.org/abs/2604.21741v1) | 拟准入 | world-model闭环上以失败为目标的人类短纠正分支、缓存中间状态回滚，提供纠正经验的派生状态责任；predicted correction不是真实策略验收，三实机任务相关性不证明模拟真实等价。 |
| [21748 StructMem](https://arxiv.org/abs/2604.21748v1) | 前分母关闭 | 时间锚定事件、双视角、周期语义巩固及层级链接是成熟记忆组织组合；题摘未新增巩固有效性、状态恢复或受控独立反证，LoCoMo效率实例不足以改变这些判断。 |
| [21764 Reasoning Skills](https://arxiv.org/abs/2604.21764v1) | 前分母关闭 | 将推理摘要存成skill并检索复用是成熟程序记忆分支；仅代码/数学token减少，未新增迁移、freshness或验证支持，不把减少deliberation当新的可靠性机制。 |
| [21765 PrismaDV](https://arxiv.org/abs/2604.21765v1) | 最小消歧 | 下游代码/数据profile提取隐含假设和测试是成熟组合，SIFTA在稀缺outcome下的选择优化可能独立；只核决定准入的反馈选择机制，60任务/5数据集不是准入理由。 |
| [21766 AUDITA](https://arxiv.org/abs/2604.21766v1) | 最小消歧 | 长程音频题目声称不能靠单一文本/声音线索，需核audio necessity控制和IRT对象；更难题库及人模差距本身不证明新评价边界。 |
| [21769 User-defined Leaderboard](https://arxiv.org/abs/2604.21769v1) | 前分母关闭 | slice权重、偏好与用户自定义排名是既有评价聚合的交互实现；题摘未新增聚合保证或受控反证，dashboard和主题分组不独立贡献。 |
| [21771 TestGeneralizer](https://arxiv.org/abs/2604.21771v1) | 前分母关闭 | 由初始测试推需求、生成模板/实例及可执行测试，是成熟测试生成流水线；mutation与LLM评coverage未新增spec真值或充分性保证，不因可执行就retain。 |
| [21772 DOCO](https://arxiv.org/abs/2604.21772v1) | 拟准入 | adapt-conditioned ID/OOD分流与ID补偿prompt向同batch OOD传播结构约束，区分域修正和新类别支持；核split错误与反馈选择循环，不外推open-world可靠性。 |
| [21776 ReshootAnything](https://arxiv.org/abs/2604.21776v1) | 拟准入 | 单目随机平滑crop构造伪视角支持，warp轨迹anchor与独立crop遮挡迫使跨时/视角恢复；是训练支持的具体分支，不把伪点云或合成遮挡当真实4D几何证明。 |
| [21794 DiffMAS](https://arxiv.org/abs/2604.21794v1) | 拟准入 | 多Agent latent trajectory的联合编码/解释与PEFT训练承担producer–consumer兼容，不同于固定latent传输；核训练loss、trajectory权限及额外预算，通信紧凑不等决策保持。 |
| [21795 NEST](https://arxiv.org/abs/2604.21795v1) | 前分母关闭 | session-type监控器合成到P4处理一般microservice丢包/重排；摘要未研究大模型计算、模型状态或训练/推理接口的直接问题，不能仅用network/data-plane类比扩入当前主线。 |
| [21809 Quotient-space Diffusion](https://arxiv.org/abs/2604.21809v1) | 拟准入 | 对称冗余商空间允许类内运动并保持对称目标分布，是一般生成机制的条件分支；分子SE(3)只是实例，须核商测度/收敛条件，不收其科学应用本身。 |
| [21811 PAC Consensus](https://arxiv.org/abs/2604.21811v1) | 前分母关闭 | 一维意见区间/投影与平台审议的ERM一致度研究针对社会共识聚合，不研究当前模型学习或Agent执行机制；PAC命名与可映射Evaluation不足以建立主线关系。 |
| [21816 Tool Attention](https://arxiv.org/abs/2604.21816v1) | 前分母关闭 | intent–schema embedding、precondition/scope门控和lazy schema是成熟工具发现组合；120工具模拟与端到端projection没有新的可执行admission或失效证据，不把95%token削减当贡献合同。 |
| [21827 Fantasia](https://arxiv.org/abs/2604.21827v1) | 前分母关闭 | 人类目标到AI终稿的agency/cognitive-allocation议程未提供模型训练/执行的新机制或受控反证，属于交互研究动向而非本次系统知识候选。 |
| [21829 Black-box Skill Stealing](https://arxiv.org/abs/2604.21829v1) | 拟准入，保护审阅 | 公开Agent接口对内部skill模块的内容提取、攻击自动化与分层防护构成具体资产边界；核调用权限、实际泄露对象及成本，不将一次泄露直接推所有模块或法律结论。 |
| [21843 Causality-encoded Diffusion](https://arxiv.org/abs/2604.21843v1) | 拟准入，日期未决 | 已知DAG的条件生成与固定节点干预传播形成生成分解分支，须核结构噪声/因果假设；流式细胞实例不入Science应用。v1 processing跨01Z，先核日期或隔离，不直接当本窗确定候选。 |
| [21854 Statistical Certification](https://arxiv.org/abs/2604.21854v1) | 拟准入，保护/纠错及日期未决 | 黑盒风险界与规范权威δ/operational domain区分，强通用certification主张需核采样支持/分布外边界；不接受统计界自动合规。processing跨01Z先定点日期，不扩全附件。 |

本批10拟准入、2最小消歧、8具体关闭；累计**140完整题摘：84拟准入、29最小消歧、26贡献关闭、1窗前家族关闭**。这仍是标题主线导向工作集合，日期/版本/撤回、必要证据和Books尚未闭合；未冻结分母，不声称140或496全部有贡献。

## 末端标题补漏：22条完整题摘，均有跨截点 processing 线索

本轮实际读完22条原始完整摘要。以下拟准入/最小消歧仅表示贡献判断，**所有22身份的v1 processing均≥2026-04-24T01:00Z**；该字段不是公开时刻，不能据此确定晚首发，也不能按本批ID强推当窗。贡献关闭项不用为不影响处置的日期追加追查；其余先核有界公开组合或具名隔离，不在未定日期前扩成全文队列。

| 身份 | 判断 | 原始摘要中的具体依据 |
| --- | --- | --- |
| [21860 Transient Turn Injection](https://arxiv.org/abs/2604.21860v1) | 拟准入，保护/日期待核 | adversarial intent跨隔离交互但moderation无session聚合，是具体输入边界；须核实际state/access与商业端观察，不能仅称多轮攻击更强或升级全部alignment失效。 |
| [21871 Moral Dilemmas](https://arxiv.org/abs/2604.21871v1) | 前分母关闭 | morality声明、人类行为预测和决策三对象在relational任务分离，是已有readout≠actual decision方法的新社会情境；题摘未新增机制或改变该边界的独立反证，不因道德应用恢复议题。 |
| [21873 Physical Video Signals](https://arxiv.org/abs/2604.21873v1) | 最小消歧 | 共享event record跨prompt生成what/when/where目标，扰动收益集中弱original有评价信号；只核相同目标/semantic family支持与扰动是否新有效性控制，1560clips和physics标签不足准入。 |
| [21879 Image Authenticity](https://arxiv.org/abs/2604.21879v1) | 最小消歧 | image-specific decoder/encoder作为180KB metadata恢复生成式ISP前信号有明确派生恢复对象；须核何时取得原信号和实际可恢复性，不能把postcapture使用误写成无原始信息即可逆推真实像素。 |
| [21882 RedirectQA](https://arxiv.org/abs/2604.21882v1) | 拟准入/日期待核 | 同实体事实仅替换alias/abbreviation改变结果，canonical name单接口混合记忆与访问；13模型及frequency关联限定，不把alias失败直接推未记忆或实体frequency唯一因果。 |
| [21889 TingIS](https://arxiv.org/abs/2604.21889v1) | 前分母关闭 | 索引+LLM事件合并、cascade routing与多维降噪是成熟incident应用组合；生产流量/P90和发现率未隔离新的模型/状态/评价机制，不因真实上线指标自动retain。 |
| [21901 GiVA](https://arxiv.org/abs/2604.21901v1) | 拟准入/日期待核 | gradient-informed vector-adaptation bases改变固定basis下rank需求与训练成本，是初始化/参数化分支；核预算和basis维护，8倍rank减少不等8倍真实系统节约。 |
| [21904 UniGenDet](https://arxiv.org/abs/2604.21904v1) | 最小消歧 | symbiotic multimodal attention和detector-informed alignment可能形成生成/判别共同目标，但摘要未说明具体支持/更新职责；只核这一步，不凭co-evolution框架名保留。 |
| [21905 LoRA Redux](https://arxiv.org/abs/2604.21905v1) | 前分母关闭 | SP/SVD、rank、gauge和lifecycle的机制概览未宣称新综合证据解决具体争议，也不做受控比较；技术分类和未来议程不足以重开成熟PEFT知识。 |
| [21909 Directional Confusions](https://arxiv.org/abs/2604.21909v1) | 拟准入/日期待核 | matched accuracy下confusion方向组织与robust训练反向，scalar asymmetry也可能混两种error geometry；有受控12扰动评价反证，须核模拟归因，不能把人类结构当机器必需目标。 |
| [21911 HalluScope](https://arxiv.org/abs/2604.21911v1) | 拟准入/日期待核 | instruction引入的prior与视觉错误相对作用用专门控制区分，随后受限DPO响应；须核控制条件及同预算，不把prompt作用直接归语言/视觉组件唯一因果或全部hallucination修复。 |
| [21914 VistaBot](https://arxiv.org/abs/2604.21914v1) | 最小消歧 | geometry→view synthesis latent→action组合可能只是成熟视角增强；只核闭环latent接口/训练支持是否有独立机制，不因ACT/π0迁移、免calibration或VGS倍数retain。 |
| [21915 Vista4D](https://arxiv.org/abs/2604.21915v1) | 拟准入/日期待核 | static pixel分割、4D重建的explicit camera/content支持与带artifact的multiview训练回应depth误差，是条件表示分支；核分工与控制，不把pointcloud或一致度直接当物理真值。 |
| [21916 MathDuels](https://arxiv.org/abs/2604.21916v1) | 拟准入/日期待核 | author/solver双角色和Rasch共同估计揭示能力不可互代、参与者加入改变难度支持；核independent verifier和可比较性，不把动态题库自动免污染或排行榜稳定。 |
| [21917 CrossCommitVuln](https://arxiv.org/abs/2604.21917v1) | 前分母关闭 | 通用Python CVE跨commit SAST研究，没有研究大模型训练、Agent代码行为或模型计算的直接接口；一般软件安全的局部工具盲点不因可类比长轨迹而扩入当前范围。 |
| [21921 Context Unrolling](https://arxiv.org/abs/2604.21921v1) | 最小消歧/早公开线索 | 跨模态显式推理与shared manifold描述未说明机制支持；Seed公开目录另给04/23日历邻界，须先定点判其更早正文事件，不按April24 processing当首次公开。 |
| [21923 Multicalibration Complexity](https://arxiv.org/abs/2604.21923v1) | 拟准入/日期待核 | growing group家族与固定group在batch mean-ECE上样本阶不同，是有限条件下calibration预算分支；须核minimax假设/随机预测器与非LLM通用保证的区别。 |
| [21924 LoHo-Manip](https://arxiv.org/abs/2604.21924v1) | 最小消歧 | manager done/remaining语言记忆+rendered trace消费与replanning可能只是成熟分层控制组合；只核VLA接口适配及失败step如何有据保留，不把隐式closed-loop等于可靠恢复。 |
| [21927 CL Regimes](https://arxiv.org/abs/2604.21927v1) | 拟准入/日期待核 | 固定训练subspace/depth改变方法排序、update幅度与forgetting关系，是受控CL评价边界；小图像任务不硬拒，五regime/11order仍不能证明深度唯一因果或现代Transformer通律。 |
| [21928 ASR via Generative LLMs](https://arxiv.org/abs/2604.21928v1) | 前分母关闭 | WER不测语义、LLM候选选择/embedding/error解释都是成熟评价接口；HATS人类一致度新operating point未给新有效性、偏差或可迁移机制，不因更好百分数保留。 |
| [21930 Temporal Taskification](https://arxiv.org/abs/2604.21930v1) | 拟准入/日期待核 | 固定stream/model/budget只变任务时间切分，改变forgetting/backward transfer；任务边界是evaluation对象而非中性预处理，有controlled设计反证。网络forecast实例不升普遍CL排序或新模型机制。 |
| [21931 Fast and Slow](https://arxiv.org/abs/2604.21931v1) | 最小消歧 | 自监督speed估计→慢动作数据选择→speed-conditioned生成可能补时间支持，但需核相对speed识别与真实时间条件、训练/采样控制；dataset更大和下游应用不是准入依据。 |

末端22：10拟准入、7最小消歧、5具体关闭。累计**162完整题摘：94拟准入、36最小消歧、31贡献关闭、1窗前家族关闭**，仍非日期确认后的候选分母，非162篇已深审。标题范围的余项是明确领域/一般应用，只用于查漏不建立全体逐项closure队列。
