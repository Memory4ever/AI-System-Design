# May04 非作者独立复核

复核者：Anscombe，非本日报作者。作者：Schrodinger（`01a129f4-0108-79e2-bb60-b48228c717f4`）。本文件只处理2025-05-04；不继承其他日期候选或证据。

## 1. 上下文、权限与当前层次

已重读AGENTS、Research/Report合同、Sources使用说明及Daily组、Prompt、ROADMAP、State本日路由和[当前日报](../../04/README.md)。开始前已向作者协调本日ownership。仅写本独核文件及必要本日复核原件，不改Report/Books/State/index/scripts，不stage/commit/push。原窗口、旧0候选、旧日期评分/有效审阅和连续旧§4冻结；新增仅2025-05-03完整BJT自然日，不要求小时、不catchup。

当前为FIRST准入校准，不是DAY。已读[首批提案](SUP_FIRST_20261011.md)的9份精确v1完整题摘及对应请求原件；另围绕三个代表EX的决定事实定点读必要方法/讨论，CHORUS追加精确v1 PDF必要段。尚未独核其他材料、14来源历史停止、完整最终六节、候选Evidence或具体Books处置。作者继续的可读题摘/历史切片是普通待办，不得一概改成外部受阻。

## 2. 实际读取及独立准入

以下每项实际从本日 `SUP_abs-<ID>v1_20261011.raw` 解析完整标题、Abstract、Comments/版本身份与Submission history，并核同名request的精确请求/最终URL和200响应；不是只照录作者理由。9份均明确引用对应v1，所读页未见撤回说明；版本数量不自动证明重要修订。Submitted不授首次公开日期，未遍历完整版本史。

| 精确身份 | 独立判断：原约束 → 原文增量 → 需要核验的选择 |
| --- | --- |
| 2505.01382v1 Diffusion Guidance | 保留P。特例理论不能说明一般guidance收益 → 一般分布的平均classifier概率倒数命题且uniform改善不成立 → `MULTIMODAL-GENERATIVE-PARADIGMS`应区分被保证的统计量与逐样本质量。AB已足准入，不机械全文；假设/证明和任何采用仍待相应Evidence，不能把sample quality换成通用视觉质量。 |
| 2505.01386v1 CATransformers | 保留P。只优化运行能耗/延迟忽略制造碳 → 联合模型/硬件搜索加入embodied与operational碳后设计选择不同 → 核生命周期成本目标如何改变设计。owner优先`PLATFORM-COST`，硬件协同为交接，不把scheduler当唯一owner；不采17%通用结论，质量/寿命/利用率/估算边界仍待Evidence。 |
| 2505.01406v1 VIDSTAMP | 保留P，包括安全反侧。图像水印不能直接处理视频时序篡改 → decoder静态图像/视频两阶段训练，空间消息与时序一致性取舍 → 核生成过程内的provenance容量/质量/攻击边界。owner `MULTIMODAL-GENERATIVE-PARADIGMS`，安全交接；摘要的no-extra-cost及robustness不是独立验证或任意篡改/安全保证。 |
| 2505.01524v1 DCR Delusion | 保留P，必须保留设计反证。距离/holdout proxy常被当隐私检验 → 多数据/模型下通过proxy仍被MIA攻击 → 核训练数据隐私评估是否必须与攻击风险分开。owner `TRAIN-DATA`，安全交接；不采用法律匿名性建议，不说任意MIA足以完整证明隐私。AB足准入，实际攻击/对照待Evidence。 |
| 2505.01572v1 PipeSpec | 保留P。多模型draft/verify串行依赖 → 分层异步执行与验证/回滚及steady-state分析 → 核并行阶段提交协议和资源收益条件。owner `INFER-SPECULATIVE-DECODING`；非零接受率保证只按论文分析假设，未授真实通信/质量/端到端性能。 |
| 2505.01637v1 Morello | 保留P。程序搜索组合爆炸、启发式采样 → rewrite递归分解+affine-cost DP+相邻同解memo压缩 → 核搜索覆盖与内存/成本模型取舍。owner `INFER-TENSORRT-LLM`的execution-plan边界，不声称TensorRT实现；原文x86、小XLA图/Zen1实例不能外推GPU或完整LLM最优。 |
| 2505.01415v1 Hydrology | 保持EX，但理由限实际原文。除AB外定点读[精确v1 §6 Discussion](https://arxiv.org/html/2505.01415v1#S6)：表现差异与训练域相关性/极值失败的解释仍是可能原因，未给隔离训练组成或架构因果的可复用新条件。不是因水文标题或负面结果关闭，不采这些推测为主线定律；日级日期未确认不影响此贡献关闭。 |
| 2505.01485v1 CHORUS | **EX改窄P**。AB提示的消融经必要段实核确有设计反侧：专家提示对Llama3.1反降，普通RAG在多个模型上低于baseline，有/无reasoning字段也改变结果。已有模块并不消除这类有效性检验价值，应核模型/提示/上下文/schema组合的失效边界，owner `AGENT-PROMPT`，RAG/context交接；不是solver领域新纪录准入。公开日/必要先稿身份仍待核，不先评分。 |
| 2505.01571v1 PainFormer | 保持EX。定点读[精确v1 III-A/III-C及VII](https://arxiv.org/html/2505.01571v1)：层次FFT/attention、现成latent cross-attention及生理信号图像化服务本任务，结果未隔离出新的通用表示成立条件；不以医学体裁关闭，也不把synthetic thermal/depth宣传的privacy当保证。abs AB比较73项，而v1 HTML与PDF首页写74项，这是摘要/正文差异，非自动证明版本污染，不将任何一数字用于本日采用。 |

实际首批处置为7P（含CHORUS重开）/2EX，不是7项确定本窗候选。P只授继续核验价值；未知公开日期/必要家族身份不得进入候选表，题摘准入不算Evidence完成或Books已有覆盖。

## 3. CHORUS决定性窄读与版本界限

实际打开[2505.01485v1 HTML](https://arxiv.org/html/2505.01485v1)的§2.4、§3.2、§3.5/Table2与相关结论限制；web PDF入口报400/content-too-large，不能写成成功读取。随后直接请求[精确v1 PDF](https://arxiv.org/pdf/2505.01485v1)，实际200、最终URL不变、13,064,188 bytes、18页；内存提取首页身份及必要pp8-10、12-14，未通读正文/附件。首页明确`arXiv:2505.01485v1`，Table2反侧与HTML一致。

准入只据局部配置结果重新考虑提示/检索/schema组合，未把跨模型差异归因为参数规模定律或证明上下文容量过载；论文objective-value相等的指标也不能证明完整约束语义相等（此为独核限制）。尚未做完整Evidence预算/统计校验，不采用GPT4成本优势宣传。已向作者发送精确重开点，作者确认接受。

PainFormer另实际直接请求v1 PDF，200、最终URL不变、28,092,385 bytes、18页，仅提取首页确认正文AB为74；不把abs的73/正文74差异误写为当前版污染或需要全篇diff。该差异不改变当前贡献关闭，不授机制或临床结论。

## 4. 当前普通待办与复用界限

作者现称新增39份proper-ID原件已抓取，但抓取不等阅读，也不在本首批独核数量内。后续独核全部新增P、纠错/安全/反证/重要修订关闭项及分层EX；如发现同类错误，仅扩查受影响集合。FIRST已核内容不重复全篇阅读，变化命题才定点重开。

14来源入口/真实分页/目标切片尚未最终交付，132appearances/75unique目前仅作者提交字段发现计数，未在此授来源覆盖。待实际scope/stops原件与最终六节到达再核；窗口未知的P要明确日期/必要身份原入口、不能采用的命题和重开位置。旧Books叙述及空候选不能代替本轮具体Books裁决。

当前结论：FIRST校准完成并发现1项应重开；DAY未审、未通过，仍有普通可执行工作。没有把未读准入转成日期保留，也不授正面Coverage/Evidence、Books整合或无遗漏。

## 5. 后续39精确v1题摘实读与窄准入

July21行政差额另在其独立文件完成后，已重新读本日AGENTS指定上下文和May04 README，以下只用May04材料。新增39份同日`SUP_abs-<ID>v1_20261011.raw`完整AB、Comments/版本史均已实际读，逐项request为200、精确最终URL与请求相同、可见Cite-as版本身份匹配；两份初次输出被截断的TutorGym/MICA另单独重读完整AB，不把截断算读完。无全池/新页发现扫描。

下表是独立狭义准入，不替代作者后续筛选表或公开身份/Evidence。`P`表示具体增量可继续核验，不给分、不是确定本窗候选；`EX`限所读内容。日期入口/先稿/来源历史仍由作者继续处理，当前不能把全部39直接转外部终态。

| v1身份 | 独立最小准入句与不采用边界 |
| --- | --- |
| 2505.01399 iTUP | P：准静态选工具未决定任务合适抓握 → 接触grounding/位置速度轨迹/物理抓握联合 → 核动态工具执行的接口与抓握条件，`MULTIMODAL-EMBODIED-VLA`；不采稳定/安全通用保证。 |
| 2505.01482 GPQA prompting | P：答对率常代理推理可靠性 → self-consistency答对排序与解释评价错序且部分prompt低于直接回答 → 核`PLATFORM-EVALUATION-SYSTEM`的答案/解释协议分离；不能证明“仅模式识别”或真实内在逻辑缺失。 |
| 2505.01484 LLM watermark | P：closed/open对手访问条件不同 → 每token扰动与Gaussian-mixture计算困难性联系 → 核`PLATFORM-SECURITY`威胁模型和检测/不可移除条件；必要§1.2/§2窄读见§6，绝非任意开源模型不可移除保证。 |
| 2505.01490 WorldGenBench | P：T2I外观质量不覆盖隐含知识语义 → Knowledge Checklist分解语义期望及模型失效切片 → 核`MULTIMODAL-GENERATIVE-PARADIGMS`评价覆盖；排行榜不证明AR范式普遍优于diffusion。 |
| 2505.01523 Subset Selection | P限局部比较：混合utility/diversity常被期待节省数据不损质量 → 不同预算下与DPP/random排序不一致 → 核`TRAIN-DATA`选样策略的预算依赖；必要§4/5/6.4已读，不采统一优势、近全量/成本节省或greedy理论保证。 |
| 2505.01539 Argumentation tasks | P：固定问答难隔离推理复杂度 → 可控攻击图/形式明确答案生成任务 → 核`PLATFORM-EVALUATION-SYSTEM`复杂度与错误类型，不采法律可靠性保证。 |
| 2505.01557 Contextures | P但**先稿身份未闭合**：表示理论分散 → context-induced expectation operator/singular functions与兼容任务 → 核`WORLDVIEW-REPRESENTATION`的有效context与scale边界；admin overlap具名旧稿见§6，不将新ID或longer-version当新贡献。 |
| 2505.01558 Sensor Agnostic | P：源传感器表示难迁目标通道 → source-target MAE联合pseudo-label/适配器及置信权重作用 → 核`MULTIMODAL-REPRESENTATION`跨传感器训练条件；必要§3/§3.4及Appendix E反侧实读，不以遥感排除、不采域不变普遍定理。 |
| 2505.01560 Translation agents | P：多agent提升可被自动指标/账面费用误解 → 人工/自动排序不一致及流程token成本 → 核`AGENT-WORKFLOW`质量协议与完整协调预算；不外推所有agent，也不拿April价格代当前成本。 |
| 2505.01563 TutorGym | P：最终题解成绩代理辅导能力 → 交互step正确反馈/动作与学习轨迹诊断 → 核`PLATFORM-EVALUATION-SYSTEM`最终结果之外的错误识别；不由human-like曲线证明真实人类认知。 |
| 2505.01578 MICA | P：仅RGB frame遗漏意图线索 → gaze/speech grounding及不同任务cue有效性 → 核`MULTIMODAL-REPRESENTATION`信息可观测边界；不采93%普遍等效或安全保证。 |
| 2505.01583 TEMPURA | P：视频压缩/不分段遮蔽event边界 → masked-event预测再分段caption训练 → 核`MULTIMODAL-REPRESENTATION`时序粒度与objective，不由causal explanations证明因果识别。 |
| 2505.01592 PIPA | P：完成率代理交互满意度 → pipeline原子行为评价显示中间行为/结果均影响满意度 → 核`PLATFORM-EVALUATION-SYSTEM`阶段诊断及用户模拟器界限；POMDP改写本身不算贡献。 |
| 2505.01595 Odds | P：离散口述概率与真实条件估计混淆 → decoder期望label scoring、合成/配对排序监督及非单峰限制 → 核`PLATFORM-EVALUATION-SYSTEM`概率/排名/greedy输出关系；必要§3.3已读，不采概率真实校准保证。 |
| 2505.01616 Phantora | P：静态trace/model估计适配耗费人力 → live interception与event网络模拟结合 → 核`TRAIN-DISTRIBUTED-TRAINING`性能模拟同步/代表性，不等复现或真实生产预测保证。 |
| 2505.01618 CompleteP | P：depth HP transfer未必脱离lazy regime → 同时满足逐层non-lazy与depth参数迁移 → 核`TRAIN-PRETRAINING`宽深配比/训练预算条件；不采12-34%普遍节省。 |
| 2505.01619 SSkP | P含安全反侧：offline安全标签不全 → PU skill-risk预测加在线risk planning/适配 → 核`MULTIMODAL-EMBODIED-VLA`风险估计与skill执行门；仿真结果不证明真实安全。 |
| 2505.01652 Causal fairness | P：IID干预假设忽略图依赖 → NSCM下decomposability/graph independence及interventional估计 → 核`PLATFORM-EVALUATION-SYSTEM`因果公平性评价条件；不是通用公平/安全保证。 |
| 2505.01657 RAGAR | P：历史均权与reference一致性可压制偏好 → similarity检索权重与ranking目标 → 核`MULTIMODAL-GENERATIVE-PARADIGMS`语义一致性/偏好优化区别，不因推荐应用关闭。 |
| 2505.01660 Focal-SAM | P：head排除粗粒度、多次backprop昂贵 → class-wise sharpness惩罚不额外backprop → 核`TRAIN-PRETRAINING`尾类控制/计算取舍，不采未读generalization证明。 |
| 2505.01694 RTD-TR | P限配对拓扑目标：CE未显式保留多尺度拓扑 → RTD约束Task Residual及每类一例的paired-cloud batching → 核`MULTIMODAL-REPRESENTATION`轻量适配与结构一致性；必要Method/Experimental Settings实读，RTD/其subgradient来自旧工作，不称发明。 |
| 2505.01706 Robust 2D-DPO | P：response/segment分数受label noise → segment-level稳健2D-DPO → 核`TRAIN-DPO`噪声与偏好粒度；Comments称updated abstract/algorithm/results，不能仅因v1标签忽略修订说明，也不据此臆造撤回。 |
| 2505.01709 RoBridge | P限实际表征/控制：symbolic planning未给可执行交接 → action/mask/masked-depth/constraint接口、不同频率闭环及视角消融 → 核`MULTIMODAL-EMBODIED-VLA`表征不变性/丢mask失败条件；必要§3.1/4.5/4.6已读，不采75/83%跨环境普遍值。 |
| 2505.01713 ICVL | P限局部对照：纯文本action labels丢visual信息 → VLM-intention跨注意融合及example选择有具体替代比较 → 核`MULTIMODAL-REPRESENTATION`intent表征与fusion选择；必要§4.4 Tables3-5实读，不把意图称真实因果或模块名自动准入。 |
| 2505.01729 PosePilot | P：camera-control生成未保持几何 → depth/pose readout与forward/reverse warping loss → 核`MULTIMODAL-WORLD-MODELS`视角条件和几何一致性；不把视频几何保真当动作动力学或真实控制可靠性。 |
| 2505.01731 SV pruning | P：均匀剪枝忽略layer不同贡献 → sliding-window Shapley approximation分配非均匀预算 → 核`INFER-TENSORRT-LLM`质量/搜索代价，不采PPL数字为实际加速。 |
| 2505.01742 Easz | P：edge神经编码/切换负担 → patch erasure+server learned reconstruction改变compute归属 → 核`MULTIMODAL-REPRESENTATION`codec质量/通信/接收端计算边界；不是“端到端无计算”或只因IoT类比准入。 |
| 2505.01743 Llambda | P：高分辨率VLM难直接解释低分辨率序列 → contrastive pseudo-label与时空物理一致性caption筛选 → 核`MULTIMODAL-REPRESENTATION`输入域/伪标签约束；LoRA不单独准入，BERTScore不证明真实理解或端侧可用。 |
| 2505.01761 Same evaluation | P：评价应随granularity一致 → 长文本漏error spans/ranking下降及FSP/FT补救 → 核`PLATFORM-EVALUATION-SYSTEM`输入长度偏差；不因翻译任务关闭，也不称普遍修复。 |
| 2505.01812 New News | P：ICL可用新知识不等于FT进入weights → FT-ICL差额、自QA协议及contextual-shadowing反侧 → 核`TRAIN-SFT`知识内化与上下文遮蔽；不采初步scaling为定律。 |
| 2505.01822 AEPO | P：diffusion policy中间energy的log-expectation难算 → conditional-Gaussian解析与学习目标估计 → 核`MULTIMODAL-GENERATIVE-PARADIGMS`guidance可解条件；offline RL成绩不自动外推LLM RLHF。 |
| 2505.02862 ICRT | P含安全/评价反侧：binary attack率遮蔽输出严重度 → 认知decomposition/relevance攻击切片与ranking评估 → 核`PLATFORM-SECURITY`威胁/评估定义；未读payload、不复述可执行攻击、不采普遍绕过。 |
| 2505.02865 SpecSearch | P：tree thoughts生成延迟 → draft thought/token协同与quality拒绝门 → 核`AGENT-PLANNING`搜索质量/推理预算，speculative交接；不混tokens无损采样与reasoning-quality经验保证。 |
| 2505.03814 Cer-Eval | P：固定大测试集缺精度/预算停止依据 → sample-complexity/partition适应抽样及CI → 核`PLATFORM-EVALUATION-SYSTEM`抽样预算/置信条件；95%未按未读假设采用。 |
| 2505.03818 SInQ | P：合成代码题未检语义差异 → generator/evaluator找divergent输入的半对抗训练 → 核`TRAIN-DATA`可执行语义oracle及跨语言迁移；infinite-compute极限不证明有限自玩持续提升。 |
| 2505.03819 Focus on Likely | P：不确定分类直接argmax → test-instance单步梯度集中likely classes → 核`MODEL-SAMPLING`decision/适配交接或`TRAIN-PRETRAINING`test-time objective；不将降低entropy等同真实校准，owner待作者具体命题固定，不据标题自动纳入LLM生成。 |
| 2505.03821 Perspective Taking | P：识别成功代理空间理解 → 控制物体/人物姿态/视角的诊断题分层失败 → 核`MULTIMODAL-REPRESENTATION`observer/viewpoint identity；不能由实验推荐证明geometry模块必然有效。 |
| 2505.04637 Adaptive Token Boundaries | P限实际提出的differentiable boundary/层次cross-modal结构，必要PDF见§6；先稿DOI与模型/预算/实施可信度尚未解决，不采认知同构、显著性或数值收益。 |
| 2505.04638 ARIEL | EX：AB具体任务是生物医学研究文本摘要、图解释及科研hypothesis辅助，暂缓AI for Science应用路线；未给领域外的新执行机制或具体可复用评价混杂。不是因含医学词关闭，也不把专家评价/test-time scaling术语借通用owner重引本暂缓任务。 |

本批独立判断38P/1EX，连首批为45P/3EX、48个精确v1家族。数量只对应已读本地48，不是75发现家族全部筛完或日级公开分母；其余发现材料及来源目录仍未验，不预签DAY。

## 6. 必要局部与具名版本/先稿问题

以下为实际在线原件窄读，未自动归档新增raw、未假装浏览器复现；本地精确AB/request与在线必要URL分开。没有通读39篇。

- [Watermark 01484v1](https://arxiv.org/html/2505.01484v1) §1.2/§2：closed每token partition扰动、open非中心Gaussian mixture与robust-statistics困难性连接，强度依secret-key/对手/分布假设，不以不可移除宣传采安全保证。未核Theorem3.2/4.3完整证明。
- [Subset 01523v1](https://arxiv.org/html/2505.01523v1) §4/5/6.4 Table1：方法借DELIFT/submodular等既有思路，本文budget配置与DPP/random排序变化是所保留比较命题。实际表未证明全量等质或端到端省费；不把通用greedy近似结论自动授给本文pairwise-diversity目标。不是完整理论/实验验收。
- [RTD 01694v1](https://arxiv.org/html/2505.01694v1) Method/Experimental Settings：配对cloud要求每类一例、batch=classes，按dataset/shot搜索lambda；性能图不控制该搜索预算差别，不授普遍净收益。只限定适配目标与batch条件。
- [Odds 01595v1](https://arxiv.org/html/2505.01595v1) §3.3：expected-label scoring加synthetic-mixture/pairwise loss，既有单峰理论不总成立，原文指出margin/regression单独不足以保证greedy正确；这个决定性限制已读，不仅因scale变大准入。
- [RoBridge 01709v1](https://arxiv.org/html/2505.01709v1) §3.1/4.5/4.6：IOR具名接口、masked-depth与raw-depth的viewpoint变化对照及occlusion/mask-loss失败已读。不是把成熟三层planning重新命名当贡献。
- [ICVL 01713v1](https://arxiv.org/html/2505.01713v1) §4.4 Tables3-5：intention来源与concat/cross-attention方向有具体局部替代比较，足以继续核，不借这些差异宣称通用机制更优。
- [Sensor 01558v1](https://arxiv.org/html/2505.01558v1) §3/3.4及Appendix E/Table4：source-target序列重建接口与confidence相关推导；Appendix明确MAE单独会退化/可能错置信，联合DA才局部较好。反侧使其不只是遥感指标；未核完整推导或普遍域不变证明。
- Adaptive 04637v1 HTML入口未返回可读正文；实际直接[PDF](https://arxiv.org/pdf/2505.04637v1)200、最终URL不变、1,142,456 bytes、13页，内存仅读首页/pp4-6的§3.2.2及必要配置。boundary sigmoid/层次表示/contrastive alignment确实提出；GPT-4V“publicly available implementations”的口径、完整训练预算及boundary如何形成实际token序列未证，不能把图示/公式当实现复现。首页出版DOI与abs一致；[DOI](https://doi.org/10.5121/csit.2025.150807)实际web不可访问，先稿公开日仍需作者定点恢复出版正文/metadata，不能从pp89-101/2025推本窗或先行全版diff。
- Contextures01557 Comments的admin overlap不是撤回、也不是“论文无价值”。实际定点打开[2504.19792v1家族页](https://arxiv.org/abs/2504.19792)：Runtian Zhai博士论文、完整AB已经包含contexture、兼容任务、scale递减与context改良。当前只有v1，未读完整博士正文；submitted Apr28不自动证明first-public。应定点核必要正文与01557拟新增命题差额及原公开日期，不得仅因为博士体裁关P或因May新ID重计首次贡献。

上述已向作者交精确身份/反侧问题，等待实际题摘筛选/日期与来源包；不把等待作者落稿叫无法执行的外部阻塞。后续采用命题变更只核相应差额，已读窄段有效复用。

## 7. 余27题摘、共同误关修正与OLD窄核

继续本日，未重开July21。余27份精确v1完整AB、Comments、Cite-as与可见Submission history实际读完，同名request均200、请求/最终URL精确v1相同；连§2/5共75家族题摘层已读。这里选择把所有余项AB读完以检查作者的共同关闭理由，不意味着75篇全文或候选Evidence完成。可见后版数量不等于重要修订；未扫描版本全集。安全/负面/身份信号的必要局部另列，未用日期未知关闭未读准入。

### 7.1 六项EX改窄P

| 精确v1 | 实际必要位置、准入句与界限 |
| --- | --- |
| [2505.01603 Dandelion](https://arxiv.org/html/2505.01603v1) | §1/3/4.3：POSIX sandbox初始化牵连通信环境 → 不可信pure compute与trusted通信函数拆分，且实际包含Text2SQL Agent工作流 → 核`AGENT-PLATFORM`接口/隔离/弹性取舍。不是仅AI inference类比；禁syscall/用户不能修改通信实现是实际边界。不采用96%通用省内存、任意安全或训练适用，large/frequent state sync与AI training是原文non-goals。 |
| [2505.01695 SimAug](https://arxiv.org/html/2505.01695v1) | §3.2/4.4-4.7：稀疏/失衡交互不能只增加任意合成量 → inactive用户/unpopular项定向补边与user/item、feature/interaction替代比较，过多augmentation退化、较大PLM未必较好 → 核`TRAIN-DATA`表征来源与补样量的局部有效性。成熟similarity方法不消除比较价值；不采普遍fairness或作者关于噪声/用户复杂度的因果猜测。 |
| [2505.01785 TV-SurvCaus](https://arxiv.org/pdf/2505.01785v1) | 完整AB及必要PDF首页/pp5-6：静态表征平衡未直接解决time-varying treatment-confounder feedback/censoring → 表征平衡与sequential权重的估计边界 → 核`WORLDVIEW-REPRESENTATION`学习表征/反事实估计条件，评价交接。不因medicine/survival名关闭，不采完整定理、临床或泛化保证。精确PDF200、最终URL不变、409543 bytes、22页，首页内部date May6 2025且标v1；同v1 HTML内部date Aug24 2026，是必要载体口径差异，不用任一内部date作为first-public，不假装已比较完整方法。 |
| [2505.01790 Educational Video QG](https://arxiv.org/html/2505.01790v1) | §4.3/Table5及人工评价Table8：自动文字重合分代理内容质量 → 去模态后某些自动分变好而内容specificity/answerability变差，且模型依赖 → 核`PLATFORM-EVALUATION-SYSTEM`多模态输入缺失的测量盲区。不是教育题库应用准入；短问句偏置是作者解释，未证明普遍因果或最优模态。 |
| [2505.03824 MAP](https://arxiv.org/html/2505.03824v1) | §4.3-4.4/5.1-5.4：flat历史扩展不必变好 → 固定GPT3.5下检索组织与逐轮flat/fragmented历史在单域/跨域的长度依赖差额 → 核`AGENT-MEMORY`检索/上下文组织的局部条件。不是发明RAG或证明timely-update一致性；baseline与完整prompt同时改变，不能归因纯检索；不采报价/普遍省费。 |
| [2505.02858 Synthetic Multi-platform Data](https://arxiv.org/html/2505.02858v1) | §5.5/Table9/Fig8及§6：单篇lexical/semantic相似不保证集合结构 → 跨来源共同named-entity频次/degree-vector诊断及top/bottom实体差额 → 核`TRAIN-DATA`合成集合联合结构评价。不是政治/social-topic成效准入，不采用privacy/下游utility。admin overlap具名旧稿[2407.08323v1](https://arxiv.org/abs/2407.08323v1)完整AB及[旧§1/5.1](https://arxiv.org/html/2407.08323v1)实际读，旧稿已有单篇与集合tag复用区别；新MPTM/NER诊断须按实际差额处理，不能全称首次或因overlap全关。必要家族事件/公开日期仍待核。 |

上述已逐项发作者，不等待整包才通知。六项只改变准入与后续需要核的命题；未知公开日期仍不能确定入本窗候选、先评分或进Books。作者原44P/30EX/1OLD提案据此应为50P/24EX/1OLD，待作者落稿读回；不是75公开家族分母。

### 7.2 其余代表关闭的必要消歧

- [01559 Mechanical Design](https://arxiv.org/html/2505.01559v1) §4.1/4.2 qualitative及§4.3：无语义part IDs/untitled names/相似part集合造成任务歧义，LR/dropout的机制解释仍为猜测，未隔离数据组成/参数的通用新条件。保持EX，不因mechanical名字关闭，也不采用多head自动降低overfit的解释。
- [01658 Inference Engine Survey](https://arxiv.org/html/2505.01658v1) 必要engine/优化支持表、structured-output benchmark段及§7：主要为支持特征/生态分类与既有benchmark介绍，所读比较没有新受控测量反侧。保持EX，未通读65页或审每个引用，不采表中兼容性为当前产品保证；不是因为survey体裁关闭。
- [01693 DeBERTa-RAD](https://arxiv.org/html/2505.01693v1) III-A/C、IV-H/I：teacher输出硬标签，所谓distill loss仍对one-hot target、只改student温度；uncertainty三类与MIMIC任务比较没有隔离出新的teacher概率信息/学习成立条件。保持EX，不能从硬标签宣称已转移teacher soft confidence，也不采领域指标为通用蒸馏机制验证。
- [01711 CXR-TextInter](https://arxiv.org/html/2505.01711v1) §3.1/3.2、4.4及结论限制：image-to-text upstream明确未详述，概念embedding平均后加到token的成熟融合；ablation只比较有/无KG，未识别结构文本替代视觉的独立信息条件。保持EX，不以medical名关闭，亦不将upstream不可详读作为拒绝贡献的唯一理由。
- [01636 STROT](https://arxiv.org/html/2505.01636v1) §3.3-3.6及§4必要case：计划/字段schema、error trace再生成和有界retry属于所示执行组合，病例演示未形成新的失败恢复语义或有效性条件。保持EX，不采用低temperature即确定性、structured成功即语义正确的宣传。
- [02861 MetaOrch](https://arxiv.org/html/2505.02861v1) §2.3-2.5/3.1/4.3：任务/agent实际是合成向量、启发式score/fuzzy label监督，LLM integration为未来工作；未形成主线新的执行契约。保持EX；Static-Best质量高于MetaOrch而selection accuracy低，不能把selection分当最终质量保证，但此toy例本身未建立LLM主线的新测量规律。
- [01542 Emotions Survey](https://arxiv.org/html/2505.01542v1) V-D/E、VIII限制/IX伦理：已有研究风险/偏差与数据局限的归纳，不是本稿新的安全测量或纠错证据。保持EX，不采用therapy/隐私/安全保证，未重扫其参考文献。
- [17024 Affective-Taxis](https://arxiv.org/html/2505.17024v1) §4/5及limitations：实际建模简单生物taxis，作者承认无跨时间associative learning；对人类/AI affect的必要性为推论，未给可改变当前模型优化/解释/安全门的已指定机制。保持EX，非因安全题目略过，也不采“必须显式表征affect”作已证结论。
- [2506.06286 Alignment Taxonomy](https://arxiv.org/html/2506.06286v1) §3及§4：aim/scope/constituency规范分类与explicit moral deliberation论证，具体技术架构与实施仍留future operationalization；未给本主线新目标/测量机制或反证。保持EX，不采RL伦理普遍必要/不可能性保证，不用June ID推公开日。

另12项完整v1AB的具体关闭层如下，未机械读全文：01385 building-mask polygon几何后处理未形成通用模型/系统条件；01627领域组件GPT3.5标注为已有DA应用；01639既有neural Bayes估计用于Levy金融参数；01651authority/autonomy/accountability治理分类而非执行门；01754领域media-bias分析而非模型评价；01804空管Markov/utility运营模型非LLM Agent；01810 CP/CRC用于定位为既有保证应用；01821edge-cloud技术/方向综述未指出独立新测量反侧；02859battery XAI chatbot的人类理解成效非新模型解释机制；03817audit-log IRL攻击归因为安全领域应用而非LLM安全机制；07835Web3产品愿景未给实际委派协议变化；2506.11015人脑记忆/教育论述与grokking类比未给模型学习/记忆机制。这里的安全/治理词不自动授主线贡献，也不自动略过可见信号。连FIRST已核01415/01571及§5已核04638，共24EX按实际理由关闭；不是外部页面无遗漏保证。

### 7.3 Contextures窗前共同命题

实际读本地`SUP_arxiv-ID-old-correct_20261011.raw`完整唯一结果及request：正确`paper_id=2504.19792`、`announced_date_first`、200、唯一命中明确originally announced April2025。仅月级已足界定早于May03（即使BJT月末跨至May01仍窗前），不追小时、不从submitted认定公开。不是错误field查询的空响应。

实际窄读旧`SUP_html-contexture-old` §14 Quantitative metric/Eq18、Table3及无universal metric说明，与新`SUP_html-contexture` §5.2/Eq4、Table1对照：谱指标形式、beta=1/d0=512与credit-approval/breast-w/diabetes等数值相同；旧完整AB已含contexture、compatible tasks和scale递减。上述本次拟采用的共同命题可按窗前OLD去重，不是论文无价值/博士体裁EX；未宣称每个lemma、方法和全文完全相同，不审无关学位论文附件。后续若指定实质不同新命题，只重开该命题及事件身份。

当前准入校准可复用到75题摘层，source范围/日期停止、01706实际修订影响、04637具名出版身份冲突及最终六节仍按作者正在准备的实际包继续。DAY尚未通过，不把这些普通可读差额写成日级无法继续。

## 8. 修订、出版身份与来源原件差额

本节只继续May04，已重新读AGENTS、Research/Report合同、Sources使用说明与Daily组、Prompt、ROADMAP、本日README及本日停点。State仅读最新路由，不继承July21研究。作者现已同步50P/24EX/1OLD；§2～7未变化准入与必要局部复用，不重复75全文。

### 8.1 01706修订说明的实际关闭层

实际读完整v1 AB页面的Comments `Updated abstract, algorithm and experimental results`、版本史仅v1；本地当前/v1 HTML的SHA-256同为`784f24e18e265414fea74b5449c0d2ecd349e26fd773636d173f725cb72489a9`。进一步实读§4.2/4.3、§5.5 Table2、§6、Appendix D Algorithm1，不以版本标签略过说明，也不臆造另一个修订版。精确[v1 PDF](https://arxiv.org/pdf/2505.01706v1)实际200、1794418 bytes、15页；定点读p5与p14确认不是HTML转换独有问题。

保留窄P：分段偏好分数的定向扰动训练是待核验配方，不授无偏/通用稳健保证。Eq11两个相同loss相减，Algorithm1 line12累计正log-sigmoid却line17做梯度下降，与正文负log目标有符号冲突；Table2的稳健版本仍低于vanilla DPO，不可宣传普遍优于DPO。以上是具体必要限制，不因有错误线索抹掉潜在贡献；若未来采用理论/正确实现命题，须定点取得更正公式、对应实现及评价协议。当前不要求无关全篇diff，也不把未核公开日改成Evidence完成。

### 8.2 04637出版身份冲突

本次通过web实际打开出版方[csit150807.pdf](https://aircconline.com/csit/papers/vol15/csit150807.pdf)，可见11页、pp91–101，标题为`A Creative System To Generate And Play Music And Lyrics Using Flutter And Ai Technologies`，作者Yuting Gao/Ang Li，DOI为`10.5121/csit.2025.150807`。这不是继承作者浏览器观察，也不是用其CLI403宣布原文不可达。与此前实际读的arXiv 2505.04637v1 Adaptive Token Boundaries、Dongxing Yu、13页/pp89–101身份不一致；出版方PDF不能自动作为Adaptive先稿或支持其实验。只隔离该DOI/发表与first-family关系，不推断撤回、伪造或两篇同家族。arXiv窄机制P仍可保留，必要公开身份及可信度限制须精确写明。

### 8.3 已实核的来源停止与限制

以下为本地本日原始响应/request的独立核查，不是新发现扫描，也不授14源最终DAY：

- arXiv四Atom的total=returned为38/25/47/22，start0，132appearances去重75家族，只是四限定主题提交字段发现。`/list/cs.CL/2025-05?skip=0&show=25`确实200，显示月2833项及first25标题，无精确公开日；不扩成2833待审队列，也不沿用短日期404宣布整个历史入口失败。原Advanced day和错误field ID响应为错误表单，非nohit；正确paper_id的CHORUS唯一命中只给originally announced May2025，未闭合May03。
- Seed文件名与实际类型相反：`seed-blog0`为article_type1/ContentType0论文，`seed-papers0`为type2/ContentType1博客。论文tokens0/20/40实际数组18/20/19、total94、next60/has_more=true；目标邻接May05到May02。博客0/20实际18/18、total45、next40/has_more=true；邻接May12到Apr23。已核所返PublishDate无May03，但稀疏返回及locale未记录不能证明完整94/45或全站无遗漏；此具体限制已送作者，不假装US locale复现。
- Hunyuan publicList POST pageNum1/pageSize1000/renderType0为200/code0，totalNum=实际list=11，displayPublishTime皆2026。仅当前目录返回不足May历史，不沿用其他日期的9条数量，不由此写May零命中；动态首查/必要替代停止尚待作者最终包。
- Google Research May月Blog实际9项，May01/02到May06/07/12/13/14/22/23，无May03；Amplify只有May02官方日，不猜小时把它catchup到May03。DeepMind page6触发9个May链接，最终正文metadata为May06/14/20，部分308经尾斜杠200恢复；不写全9失败。Publications历史主题query仍等待作者实际差额。
- Meta page2/3/4内容实际变化，page4可见May21/14/13→May01/Apr29，但列表混入乱序旧项，不能单凭页面最早日期当完整单调时间游标。Z.ai page2/3文本相同、最早Dec07且显示没有更多，只授当前返回停止，不授May历史。ERNIE page2实际1/2末页到Jun30，未到May历史；不将缺少May内容写来源当时不存在。
- MiMo 6159本地JS实际Paper数组含May12、Jun04等2025日期，不是全2026；8557首页组件与6159内容列表须分开。Blog内容JS也含Dec2025日期；直达Flash页面为Dec16发布，不是完整Blog列表。MiniMax EN/CN/Agent三个入口已实际读返回日期切片，CN还含Jan15/2025，EN首页停到Oct27/2025，Agent三项皆2026；不从首页成功授全部历史或把所有内容误记2026。

当前仍有可执行的sourcefinal、必要身份/公开日期停止与六节同步。尚未签DAY；来源当前列表/AB或必要局部不等Evidence完成，不授Books已有覆盖、整合或无遗漏。单篇准备继续推进，作者未交最终包的层保持普通待办而非假称执行受阻。

### 8.4 三项包、US locale与50项日期查询读回

随后实际读作者`SUP_NARROW_EVIDENCE_20261011.md`全部三项处置。01706、04637与02858的原件身份、最小P及不采用边界与§7/8实际独核一致，可复用；不是三项确定候选或Evidence通过。04637出版对应仍不得采用，未来若有独立可靠的精确arXiv事件公开日/正文身份，可只评其可支持命题，不机械要求澄清出版DOI才允许读arXiv正文。02858共同tag反侧不重计，新NER集合结构诊断潜力不因旧共同段落被全关。

作者补取的Seed US locale五组request真实含`x-tt-locale: US`且status200；独立比对每组响应ArticleID顺序与旧数组全部一致。type1 tokens0/20/40仍18/20/19、total94、next60/has_more=true，type2 tokens0/20仍18/18、total45、next40/has_more=true。原未记录locale的普通事项已实际关闭，不能误记为仍未请求US；稀疏目录/全站召回限制保留，不为填满94/45遍历其他日期。

四批精确`paper_id` OR请求及实际`li.arxiv-result`逐项独核：13/13/13/11、status200、size50，每批请求ID集合与实际结果身份完全相同，合计50唯一P；每项只给originally announced May2025。第四批摘要中的旧2407.08323链接不是第12条命中，不能用全文ID regex把它误增分母。请求不足一页且所求50全返回，可在此限定身份查询停止；月级公告不足证明May03，submitted、内部日期与HTML citation字段仍不得代替日级公开门。

当前进行中README的V3实际退出0；这仅接口一致，不授DAY。baseline SHA与原连续Benchmark正文实际匹配；本时点README3个本地引用、独核2个本地引用全部可达，限定diff whitespace检查通过。以上检查需在最终六节更新后只核差额，不把本时点结果冒称最终完成态结果。

### 8.5 来源终态包与一次性请求

实际读`SUP_SOURCES_20261011.md`及`SUP_DATE_REQUEST_20261011.md`，并核新增Google Publications七份raw/request：model page1/2为1–15/16–19，systems1–11，multimodal1–14，agent page1/2/3为1–15/16–30/31–37，均200且终页到total。只核所返标题/年份/分页及入口能力，不称81唯一、当日队列或全部AB已筛；其中同题名/跨主题重复和非模型领域条目可见，不扩大成年度待关闭集合。官方公开日缺段H1保留，不授Coverage。其他来源原件核查复用§8.3/8.4。

OpenAI实际XML item1287，按现有pubDate转BJT目标日无项，邻接May02 sycophancy/May05；Anthropic实际177个publishedOn出现含重复，邻接Apr28/May29；Qwen page2实际Jun05到Apr29、DeepSeek完整changelog Mar24到May28、Kimi所返Blog Apr07到May06。上述只授各自实际目录返回切片，不授删除内容/全机构历史。MiniMax中英文及Agent当前目录同样只授已返目标元数据边界，不由单次首页成功承诺召回。

Hunyuan的浏览器必要尝试超时仅继承作者实际tool observation，本复核没有重放浏览器，不能写自己已从网页读取“全部”。独立可验证的是shell、实际JS/API参数及11条2026 payload；因此May历史段隔离而非零命中。作者Meta/具名日期辅助search空也仅作工具观察，不代替原始日期/正文；Research缺段不因辅助为空被关闭。Z.ai累计18/noMore、ERNIE末页Jun30、MiMo当前Paper/Blog没有May历史事件恢复均按请求具体H项停止，不证明当时源不存在。

MiMo有一项普通文字修正已明确送作者：8557/6159的Paper/Blog身份与切片（本地文件为home8557/home6159）必须按实件；8557包含15 Blog身份、initialVisibleCount8，隐藏7不是新队列。6159 Paper8最早May12；content-js Safety有Dec18 frontmatter、HSS为Dec19，而已保存Flash直达正文header为Dec16,2025，故不能写Blog最早Dec19。部分custom route没有日期字段，不能把仅取15标题说成15官方发布日期全核；无需读未来正文，保留May历史缺口足够。此修正尚待作者写回，不因校验PASS略过。

D1实际列50唯一P、与四批请求及准入表一致，24EX无多余日请求，Contextures共同OLD不计第51P；D1内01706/02858/04637不是三份重复日期请求。H1～H7分别对应真实日期能力不足的历史源slice，替代原件与定点重开位置明确，不请求小时/全历史或证明替代不存在。必要内容达到此限定层可安全隔离，不进入正面Evidence/Books/无遗漏。当前剩余普通项为MiMo文字校正及正式六节包/最终机械与DAY复核，未预签。

## 9. 最终DAY裁决

复核者：Anscombe（`01a1289f-7cae-7253-bef5-9228c04195d8`），非本日报作者。
结论：通过

验收范围：May04仅补May03完整BJT自然日，14每日来源的实际有限入口/主题/分页停止、75精确v1题摘的准入处置、具名安全/修订/反证与必要先稿身份、候选及Books采用权限、当前完整六部分。此结论为**安全终态DAY**，不是所有历史来源Coverage或50项候选Evidence正面通过；不授无遗漏、性能、安全、通用理论或Books完整覆盖。

### 实际闭合差额

- 全75精确v1完整AB及Comments/可见history已分批实际独核，50P/24EX/1OLD与当前筛选一致。全部P的准入门有具体最小命题；24EX均到完整AB层，其中含糊/安全/反侧按§3/6/7/8必要局部处理，未无差别读75全文或全部附件。CHORUS和六项后续EX重开得到实际局部支持，未以成熟组合、应用标题或审阅费用关闭。未变化单篇按层复用，不重新发现。
- Contextures只去重旧April公告及实际共同公式/表格/题摘命题，未宣称新旧全文相同。01706修订说明已读到方法与精确PDF算法符号，保留噪声配方窄P及争议，不虚构版本差异；02858旧共同反侧与新NER诊断分开；04637两份实际原PDF不同身份已确认，不假装出版方不可读取，不推断撤回或造假。这些单篇必要差额闭合不等Evidence通过。
- Seed US五次实际header/request与ID次序核对闭合。MiMo R1已读回来源/README及九个200原页元数据，准确区分15身份、五列表frontmatter、Flash Dec16与额外Safety Dec18；九日期未得不推全部晚期。R2请求表H6旧“均晚期”已经实际改成相同精确边界，本复核最后刷新行38确认，普通修正闭合，不再把它保留为待办。
- Meta新可访问Publications入口没有被外部停：page1～7 raw/request及真实Next已实际独核，每页24日期块；前12当前段共84元数据依次到page7 May14/13→Apr28/25/17，后12各页为2016～2021乱序旧项，不提前停止，也不变成84旧全文队列。page5末项实际Sep15。目标切片无May03目录日，第8页未开，H2请求已从实际最终请求表撤销。仅授该Blog/Publications返回切片，不把目录日当全部首次公开，也不据CATransformers Nov11目录日改其v1归属。

### 六部分与采用边界

当前README六部分已完整实读：§1准确分开132提交发现出现/75家族、50潜力/24关闭/1共同旧事件与正式新增0；§2含14源与实际AIRC身份触发，停止和限制自包含；§3旧0及新增确定候选0，不因缺公开日先评分；§4连续旧Benchmark正文保持，增量只到实际读层；§5列一次性D1与六个H来源缺段，替代原件/不能采用/定点重开明确；§6正确记录非作者角色与机器权限。作者仍进行中/待独核的文字是交包时状态，不作为新的外部未读队列，也不由作者自行签署完成。

D1全部50精确v1只证May公告月，不证May03；H1/H3/H4/H5/H6/H7六个源历史切片继续隔离。正式新增、候选Evidence完成、Books新写均0，**不是零命中**。无确定当窗材料可用于长期采用，Books处置为不采用/暂缓；未声称具体已有覆盖或整合，因此不借主题相似重读或改共享Books。日期/身份原件以后到达，只恢复具名项及拟采用命题；source原件到达只补May03相关主题slice，不catchup、不扩年度/月库存或其他日报。未读证据不转成受阻，本日研究可执行普通事项现为0。

### 实际验证与交接

最终正文时点V3再次实际退出0；README8个本地引用均可达，同日全部SUP Markdown的本地引用亦无缺失。205个本日SUP JSON实际可解析；P表50/EX表24、D1精确v1链接50及四批实际结果身份集合已核。baseline SHA为`27593563cf12764f81fb638fe25f8714fbc2b20c1ab057eebd05e77559920384`且逐字节等于HEAD旧报告；旧空候选、原窗口文本与完整连续旧§4逐字保持。限定README/SUP路径的unstaged/cached whitespace检查通过，限定cached无文件；实际读README限定diff未发现扩大采用权限。未以机器PASS代替以上语义核验。

本复核只写本日`SUP_INDEPENDENT_20261011.md`，未改README/State/Books/index/scripts或其他2026，未stage/commit/push。可由root依据本节同步行政完成态与计数；不预签其后State/Books写回。仅完成header/§1/5/6同步而不改变上述身份、数量、保留项及采用权限时，可复用本次DAY；若出现新普通事项、具体主张变化或采用权限扩大，只回到对应差额独核，不重读全部75。

## 10. FINAL完成态窄核

复核者：Anscombe（`01a1289f-7cae-7253-bef5-9228c04195d8`），非本日报作者。
结论：通过

本轮仅实读May04行政完成态及随后§5/6两处格式修正，复用§9已成立的完整六节安全终态DAY。已重读AGENTS及必要Report合同；不重开75题摘/全文、机构发现或July21，不虚构复跑来源。header现在为完成，检查时间为root写入的`2026-10-11T18:49:33+08:00`；该时间不是本独核执行时间。§1/5/6的完成叙述没有扩大既有准入、证据或Books权限。

实际首次完成态V3退出1：§5未满足终态保留项明确标记及用途限制的识别，§6把通过结论和括号范围写在同一行。此首次失败不记为通过，也不撤销§9研究裁决。root仅窄修后，本复核实际读回：§5明确“终态保留项”、不用于正面证据/Books/无遗漏断言及定点重开条件；§6独立一行“结论：通过”，另段保留安全终态而非50日期项/六源缺段正面Coverage/Evidence的限定。与修前完成态的只读文本快照相比，header和§1～4逐字未变，变化仅在§5/6。修后独立运行`python3 -B scripts/validate_research.py --report papers/2025/05/04/README.md`实际退出0，检查1份V3、候选0；仅授接口一致性，不以此代替语义。

冻结及引用实核：baseline SHA-256仍为`27593563cf12764f81fb638fe25f8714fbc2b20c1ab057eebd05e77559920384`，逐字节等于HEAD旧报告；原hour窗口文本、连续旧§4 Benchmark正文与旧空候选保留。当前README有14个唯一Daily来源编号，表外AIRC只沿用具名身份触发；9个本地引用全部存在，所指本独核§9存在。50P/24EX/1OLD合计75、发现132次出现的分母层未变，D1仍50个精确v1，H1/H3/H4/H5/H6/H7仍六项，不恢复已撤销H2。准入、原件停止及单篇核心均复用§9，不声称重新读取来源或205个JSON。

FINAL确认：本日研究普通事项0，两处完成格式差额已闭合，可沿用§9完成本日安全终态DAY。正式新增、候选Evidence完成、Books新写仍均0，非零命中；50项公开日及六源历史缺段继续隔离，不授正面Coverage/Evidence、Books已有覆盖/整合或完整无遗漏。以后只有具名公开日/身份原件或May03相关历史切片到达才定点重开，不catchup、不扩库存或其他日期。本节不预签State、全2025计数或后续Books写回。

本次仅追加本文件；限定README/本独核文件的unstaged与cached `diff --check`实际通过，限定cached无文件。未改README/State/Books/index/scripts或其他2026，未stage/commit/push。
