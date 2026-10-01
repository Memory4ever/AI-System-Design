# 04/20 仅报告候选的反向准入复核（作者，待非作者 Gate）

复核前工作态：150 个唯一完整题摘中，127 个正式候选（24 整合／13 具体已有覆盖／72 仅报告／18 窄争议）、22 个贡献前关闭、15483 一项日期隔离。这个比例不是配额；本次按《研究合同》§3 逐家族反问“若源命题成立，究竟改变哪条可保留的模型/系统选择或重要既有判断”。保留已有必要原文与反证，只对准入层重新裁决，不能把局部、模型小或负面结果当硬拒，也不能拿 §4 的长证据笔记倒推项目贡献。本文件是作者侧逆向审计，不表示独立 Gate 或最终分母通过。

## 第一组：原 72 项中的前 24 项（原正式 §3 次序）

| ID | 逆向准入 | 具体判断（源位置沿用正式 §4 与 v3-reopen-notes） |
| --- | --- | --- |
| 15675 C-Mining | 前关闭 | 几何错位选 cultural synthesis seed 和模型评分虽有实现，但未识别一个会改变模型数据选择规则的条件；文化覆盖真值、合成规模与成本未独立控制，剩余是该数据域 seed recipe。不是因文化/小模型关闭。 |
| 15701 Mixture-of-Layers Distillation | 前关闭 | 相同文本/key 上的逐层 attention 蒸馏是可复用监督实现，但现有 teacher–student 对齐的容量/层选择合同不因该局部配方改变；未隔离 mixture-of-layers 对强基线的必要性。 |
| 16022 SocialGrid | 保留 | 动态机会集使“任务完成”与“完成后路径效用”分母分离，可能改变 embodied 多 agent benchmark 对规划成功的解释；仅取该受限负载，不把新任务目录或社交能力分数本身准入。 |
| 16027 output diversity collapse | 保留 | lineage 与正确子集的 diversity 对照给后训练质量之外的明确选择边界：最终正确率不保证有效输出支持未坍缩；保留混杂，不归因唯一教师或训练目标。 |
| 16146 proxy rejection | 保留 | 拒绝门槛的 proxy-confidence 与实际接受集合之间的条件可改变 test-time alignment 的控制选择；只保必要等价/反例条件，不将 proxy 当安全真值。 |
| 16171 JumpLoRA | 保留（作者自纠） | rehearsal-free、task-agnostic 连续任务下，相比固定稀疏率的 adapter mask，可学习逐层阈值控制低秩更新在原权重坐标中的支持集，且逐任务 merge 免推理 task ID；这是 Ch30 更新支持选择的受限分支。SC 的 ELLA BWT 反退、预算未匹配不支持普遍防遗忘，仍可 5 分标准仅报告。 |
| 16211 NVBench | 保留 | 非语言 vocalization 的 inventory coverage、事件正确性、放置时机与语音质量分账，能纠正仅用语音主观质量验收这一构念；不因新 benchmark 名称准入，准入仅限遗漏的事件切片。 |
| 15583 SAGE | 前关闭 | query contrast 与窗口抽取是局部文档索引 selector；上下文保真、prefill/cache 成本没有建立现有检索深度/证据责任以外的新可行性条件。 |
| 15609 Adapting in the Dark | 保留（作者自纠） | 仅当远端返回完整 probability vector，local white-box steering 加 prediction harmonization 可用一次 API 调用完成输入 prompt 适配，而多次 ZOO 查询有不同成本；这是模型访问权限与调用预算下的受限替代设计。不是 label-only/top-k、黑盒真梯度或生产 SLO 保证。 |
| 15618 Majority Voting for Code Generation | 保留 | 可执行 program medoid 与逐输入 mode 不是同一 aggregation；固定候选内的准确率/成本反向可能改变 code-agent 答案选择，保留“共识≠正确”与执行权限条件。 |
| 15622 AdaVFM | 前关闭 | 低频语义云支持、高频 edge 子网与 scene lookup 的结合仍是所测视觉任务的资源配方；没有独立证明部署边界、能力缓存/过期条件或未知场景选择改变，不能因“edge/LLM”两词准入。 |
| 15577 Reward Weighted CFG | 保留 | 条件 likelihood-ratio 与真实 policy-improvement 的先验/归一前提是生成采样控制的机制边界；负 z-score、truncation 等实践差异必须单列，不因分子应用恢复该领域任务。 |
| 15521 Frequency-Aware Flow Matching | 前关闭 | low/high-frequency 与 spatial velocity 同时变动，未分离哪个条件改变生成范式选择；ImageNet FID 是局部配方成绩，现有多模态生成 factorization 与修正链不因它改变。 |
| 15557 Predicting Where Steering Vectors Succeed | 保留 | output-alignment 可读与实际可干预性不等价，若按其有限层/目标对照保留，会改变把 probe 当 intervention oracle 的判断；不采三阶段内部定律。 |
| 15461 PersonaLedger | 保留 | 私有统计经 LLM simulator 后 distribution fidelity 可被 learned prior 覆盖，说明 DP 后处理合法性与 synthetic fidelity 是不同保证；保留该有限反例，不采唯一架构因果或统一预算。 |
| 15376 Zoom Consistency | 前关闭 | 双 zoom 第二预测偏移是该视觉定位任务的局部误差 sensor；未证明比已有条件置信/几何一致性验收多出稳定选择规则，跨模型 router 的成本与弱结果不改变 Ch26。 |
| 15400 Trajectory Commitment | 前关闭 | 单模型、按最佳层挑选的 patch 非对称与随机对照 p=.056 只给探索性 fork 后果；没有新的可用干预选择或既有“可读≠可纠”判断的可信度修正。 |
| 15709 Bilevel Skill Optimization | 前关闭 | validity budget 下的结构 edit/content refinement 分工是成熟受限搜索组合；一次 held-out、小样本和同时更换多参数未使结构选择形成可推广新边界。 |
| 15482 Harmonizing Multi-Objective LLM Unlearning | 前关闭 | QA anchor、邻域和 raw-logit 蒸馏组合没有独立证明与已知 forget/retain/over-refusal 取舍不同的新有效性条件；五轴表不能单凭新 recipe 改写 unlearning 合同。 |
| 15484 vstash | 前关闭 | dense/sparse 分歧线索与 post-RRF 负结果受 IDF、cutoff、预处理和 loss/LR 同变约束；未形成 RAG 检索/生成责任外的可保留新选择。 |
| 15490 Think Multilingual, Not Harder | 保留 | 空 reasoning 的 MT SFT 仍改变 trace 语言行为，给“trace 语言变化必来自显式推理监督”一个受限反例；matched token 但未匹配样本，故不采唯一因果。 |
| 15705 CPO | 前关闭 | 概念图文字替换、视觉近邻与逆匹配构造多模态偏好对是局部数据配方；latent D 未识别、两组件消融不支持严格正交，尚不能改变 Ch29/31 的支持与验收条件。 |
| 15706 NAG | 前关闭 | 跨层 Top-K activation 选择目标数据是单代理指标，附录 validation 与192 GPUh提取成本不使它成为可迁移功能骨架或改变预训练数据选择合同。 |
| 15648 HyperGVL | 前关闭 | 超图身份/图编码的局部 VLM 任务优势未形成新的模型表示条件；尤其有 ID 的 clique expansion 和 V–E 图并非必丢高阶信息，不能用“pairwise 全失效”作为准入反证。 |

第一组最初裁决保留9、前关闭15；后续对 JumpLoRA 与 BETA 定点自纠后为保留11、前关闭13。其他48项也已逐家族审计，不按第一组比例预裁；较早“待完成”只描述当时过程。

## 第二组：原第 25–48 项

| ID | 逆向准入 | 具体判断 |
| --- | --- | --- |
| 15657 hardware verification token allocation | 前关闭 | RTL coverage ceiling/人工 waiver 与模型任务可解性分账是该验证场景的既有工程原则；变更多个组件且无可比较的模型资源选择条件，不能只因 agentic hardware 名称准入。 |
| 15794 Self-Distillation Recovery | 前关闭 | 受损 checkpoint 自蒸馏恢复是局部 repair recipe；teacher 相似度、损伤程度和成本未隔离可迁移“何时先恢复再训练”的边界。 |
| 15802 CHOP | 前关闭 | 相邻块 continuity 决定继承 prefix/重抽是具体 chunking 实现，检索数字未传到答案质量；没有改变 Ch76 的证据充分性或索引设计合同。 |
| 15871 UniEditBench | 前关闭 | image/video 编辑 triplet 与多维 judge 扩大任务覆盖，但评分器训练来源、五组可能重叠及质量目标未解决既有 judge 可靠性分歧；现阶段新榜单不等贡献。 |
| 15972 WORC | 前关闭 | swarm 标签映角色 quota 是局部预算分配 heuristic，权重非因果弱链、额外计算与 token 未配；尚不改变多 agent 决策中的 bottleneck/资源配置责任。 |
| 15842 mathematical reasoning mechanisms | 保留 | 同一算术题的 logit-lens 可读性与 activation swap 局部干预方向不同，反驳“探针没读出即表示不存在”的解释；只限测过模型/位置，不采普遍内部电路。 |
| 15851 DPrivBench | 保留 | 相邻关系与 argmin sensitivity 的具体错配表明 LLM 对保护保证的二元作答不等协议证明；Q26/Q57 窄反例使安全评价选择更明确，不把标签库当形式验证。 |
| 15859 QuantSightBench | 前关闭 | 金融预测区间/MLIS 扩任务与分数，但时间污染、区间覆盖的源定义没有纠正本书已有 calibration/时序 split 原则；领域表现不能自动入模型系统候选。 |
| 15719 Harness Evolution | 保留 | unresolved 问题的 checkpoint note 可作临时 procedure，而 resolution truth 才能跨问题提升，这是 agent 长时反馈 authority 的可检查条件；Table3 缺 N 阻止因果胜出，但不抹这条状态边界。 |
| 15741 Sequential Internal Dispersion | 前关闭 | all-token/cross-layer covariance sensor 是监督分类配方；在 MATH/OOD 组合反退且全状态成本未消歧下，未改变现有“传感器不是真值/需校准”合同。 |
| 15756 TTL | 前关闭 | CLIP OOD 前缀、伪标签bank和阈值组合未给比现有在线适配/污染控制更一般的新条件；单3090延迟和 FPR 取舍只是局部工作点。 |
| 15760 KWBench | 前关闭 | unprompted problem recognition 任务有意义，但原文承认无 recognition ablation、无同题 cue 干预和 single judge；不能由 gated score 修正重要“识别≠执行”因果判断，当前仅新基准。 |
| 16056 AST | 前关闭 | latent-copy/mel guidance 的语音编辑分支属于单任务局部生成 recipe，WER/DNSMOS 反退且没有改变 codec 边界/提交时序或保真保证。 |
| 16060 visual CoT | 保留 | 同 checkpoint prompt 组及 NoImage++ 条件给视觉证据缺失时仍具体作答的受限反证，足以警惕按统一 CoT 增益验收；不采训练史归因或普遍 CoT 有害。 |
| 16079 Flow Matching Stability | 前关闭 | 同 seed 输出近似而 vector field 不同是局部现象，数据与优化变化有反退；未形成可迁移剪枝/蒸馏或生成质量合同的新可行条件。 |
| 16135 Motion-Adapter | 前关闭 | 结构 mask/晚期融合在 text-to-motion 组合动作上可用，但任务与训练集可能重叠、缺物理 action 闭环；现阶段是领域生成 recipe，非 Ch24/26 新一般分支。 |
| 16054 Mind’s Eye | 保留 | 同任务的 prompt-arm×视觉操作方向反转是实际 EvalSpec 切片反例，root 已有限重开；B.8 人类 distractor p 值矛盾只隔离该结论，不抹提示分层。 |
| 16198 REA-Coder | 保留 | 生成前需求 QA 和失败后代码→遮蔽需求检查是两个独立位置的验证选择，首轮及消融给局部支持；模型 reference 不等用户意图，保此边界。 |
| 15663 CodeMMR | 保留 | 同检索器 image→code 与 code→image、长 SVG、未见任务方向大幅失配，直接修正统一检索分数的 workload 验收；root 已独立恢复。 |
| 15549 directed SGP | 保留 | 有向 mixing 图与半双工广播冲突时隙共同改变去中心训练的通信—收敛选择；root 已独立纠正“非 LLM 即拒”的硬门槛，不外推 GPU fabric。 |
| 16004 AgentV-RL | 保留 | 固定候选池的前向/后向工具交叉核能改变有限 verifier 调用选择，同时额外 token/时间和同模型非独立 truth 是必须保留的边界；root 已有限核。 |
| 15351 Aletheia | 前关闭 | 梯度探测 LoRA 选层属于可执行局部搜索，但缺同层数 random/depth 对照，未识别它改变容量/更新支持取舍的稳定条件；不因 rank16 实验本身准入。 |
| 15414 policy archive | 保留 | source-best 不等 transfer-best 且可用 probe+latent reembedding 保持 archive 坐标，是持续策略重访的不同选择条件；五 MiniGrid/20run只证明受限分支，不能扩为 LLM PPO 普遍 plasticity。 |
| 15451 weak-to-strong visual KD | 前关闭 | teacher warmup/hold/decay 和两次越过阈值即停是受限视觉蒸馏 schedule，first-at-target 不是总成本，强/弱 teacher 与已有容量差判断未形成新长期边界。 |

第二组保留10、前关闭14；计入第一组后续自纠，累计前48项保留21、前关闭27。此前独立有限核确认过必要源者仍保留其证据范围，本次只修正是否值得占本日报候选分母，不把前关闭等同论文无价值。

## 第三组：原第 49–72 项

| ID | 逆向准入 | 具体判断 |
| --- | --- | --- |
| 15614 Extended Best-of-N | 前关闭 | 固定 N 内 entmax/empowerment 调参是一般 RL 任务局部采样 recipe，CartPole/PointMass与 locomotion 反退未表明 LLM 候选覆盖、选择和预算合同的新条件；不因负例关闭，而因没有直接主线增量。 |
| 16076 PGCM | 前关闭 | segmenter→prototype→concept-only 的可显示概念接口具体，但 segmenter 已先看整图、缺独立人类语义测试；当前任务配方不足以改变 Ch23 表示身份/因果解释责任。 |
| 16090 AW-PSP | 保留 | availability 与 label support 相关会把常在线设备过采，改变同步参与者选择；即使 covered-label 指标不等全类质量，相关缺失机制本身是训练分布边界，不能因小实验拒绝。 |
| 15621 AdaRankLLM | 前关闭 | 有序 passage 子集和丢检索选项是已知 retrieval-depth 控制的局部 selector，强模型/重排反退、selector+生成成本未 matched；没有新可迁移的“何时 k=0”的可行边界。 |
| 15702 Metacognitive Monitoring Battery | 保留 | 行为 profile 对操作阈值±5pp可变9–10/20模型、retro/pro 相关 CI 很宽，直接改变把多任务“自我监测”总分当构念的判断；不采内部实体或自然类型。 |
| 15715 GTA-2 | 保留 | ToolSR89.85 与 root8.33 和框架成本对照使工具有效/最终成果/效用三分母不能合并；这比增添任务目录更具体，值得有限评价候选。 |
| 15732 LAAR | 保留 | 重试到首次正确的 TTCA 与首答准确率方向可能相反，改变请求路由成本目标；exact-match oracle及未计 router 开销限其生产外推。 |
| 15710 VoxMind | 保留 | 语音发声关键路径外先并行辅助工具候选、显式 retrieve 后才入本地工具集，是对口语 agent 时延与工具 authority 的实际分支；不采任意规模 O(1)。 |
| 15717 Into the Gray Zone | 保留 | 对齐领域上下文与目标互动、预算选择后的安全响应切片形成有限保护反证；不将 selected ASR 当事故概率或上下文当授权。 |
| 16009 MEDLEY-BENCH | 保留 | private/social 各隔离条件与 rubric 的相对最低/绝对 deficit 区别会影响 evaluator 如何读自监测能力；pseudo-GT/规模未配仍制约机制归因。 |
| 16145 Training Time Prediction | 前关闭 | 精度 profile 预测 single iteration 是 Ch36 既有 critical-path 方法的实现例，8×H100 表未给超出“目标硬件、dtype、通信都须测”的新选择边界；不能因 MAPE 数字准入。 |
| 15771 Skill-RAG | 前关闭 | hidden-state probe + rewrite/decompose/focus 是受限 RAG repair recipe，探针标签依 gold 且未识别失败因果；无超出现有 relevance→sufficiency→requery 的可保留责任。 |
| 15805 Digital Cousins | 保留 | panorama 静态场景→几何 cousin→示教/导航的 real-to-sim 数据替代路线直接触及 Ch26 真实回授，Table III 同总量反退界定何时不能把合成场景当等价训练数据；不采物理可靠性。 |
| 15809 Adaptive Information Flow | 保留（作者自纠） | white-box VLM 可先用一次额外解码读跨层视觉 attention 熵，再仅遮文本 query→高熵视觉 key 的读取而保留视觉 state；同 mask ratio 随机/低熵遮挡反向是受限替代接口。oracle 上界非部署法、弱 indirect prompts 和无端到端 SLO 限其仅报告，不要求它先产生新授权边界。 |
| 15827 UsefulBench | 保留 | 同 query-doc 下高 relevance 不必高 decision usefulness，独立标注与21.9%交集是检索目标选择的具体反证；行业专家/heuristic score 限真值，不恢复领域任务本身。 |
| 15829 Text–Image Erasure | 保留 | 文本概念 hull 与视觉 latent 共同编辑并分别测相邻概念保留，对 text-only erasure 的保护/效用选择有有限替代；温度叙述冲突和部分反向表保留，不采零残余。 |
| 15830 Puzzle Pieces | 前关闭 | 难题 hint 分层/撤架是已有 curriculum 与 teacher scaffolding 的局部配方；pass@m 误称成功概率、成本未等价、跨模型 headline 失配，使其没有新稳定训练选择边界。 |
| 15873 Listener–Speaker | 前关闭 | speaker/listener 信息集、提示和解析成功率均不匹配，不能用分数差纠正“judge 不等 generator”的已有判断或识别新机制；不是因语用小任务拒绝。 |
| 15917 Adaptive Image Editing | 前关闭 | rewrite/SAM/crop 路由可改善所选低分子集，但 40% pilot 选择和额外规划成本未完整对齐，所述 operating regime 仍是局部 editor 编排而非长期新责任。 |
| 15923 Hierarchical Codec Diffusion | 保留 | 低/高 RVQ 层按 lip/identity 与 expression 条件分责是生成表示的具体替代选择，训练音频条件与推理视觉条件的断裂也直接限定机制；只保受限语音控制，不采完全解耦。 |
| 15944 CIMple | 保留 | 近存 MAC 与 LUT softmax 的双bank流水给 attention 非线性与片上容量的实际协同设计分支；合成/布局点和整模型外存反证限制它，但不因没芯片流片关闭。 |
| 15945 RAGognizer | 前关闭 | LoRA 加 detection head 的联合 CE/BCE 是成熟多任务监督分支，标签真值、质量反退及不配对 answer 数据没改变 hallucination sensor 的可靠性/提交合同。 |
| 15958 RAG Anonymization | 保留 | PRE/POST 放置点改变原文何时暴露给 embedding/API，即使最终答案 PII 更少亦不等上游保护；这是明确安全设计责任边界，保不同 ε 不可横比。 |
| 15967 TwoHamsters | 保留 | 原子策略安全并不推出组合安全，所构造的概念对及有限过滤/擦除对照给安全验收粒度反例；不采数据集事故率或所有 defense 失效。 |

完整 72 项作者逆向结果经 16171/15609/15809 三项定点纠错：保留36，具体贡献前关闭36。原正式127、前关闭22、日期隔离1，经此层现为**正式91（24整合／13具体已有覆盖／36仅报告／18窄争议）、前关闭58、日期隔离1**，仍合150。36项已从正式§3/§4移出，原必要证据与反证保留在恢复笔记；三项报告条目已恢复。这个分母仍是作者拟冻结，待 root 正反样本与日级独立 Gate，不因单项纠错预支通过。

### 逆向后定点自纠：16171

[官方 exact-v1](https://arxiv.org/html/2604.16171v1) §2–3/Algorithm 1 与 Tables 1–2 给出的可保留选择不是“普遍不遗忘”，而是在无 replay、推理不知任务 ID 时，固定稀疏率/每任务 adapter 路线之外，把低秩 `AB` 先构造成原矩阵形状，再用可学习阈值筛选并逐任务合入基座。低秩训练参数与最终稀疏更新不是同一资产；零初始化造成的 20% warm start 也是方案成立条件。三 seed 的 SC/LS 顺序比较表明受限可行，但 ELLA 的 SC BWT 从 −0.5 降到 −1.9、两组 OA 增益大小不同，且缺完整 compute/state 与一般任务序列对照，不证明独立参数隔离或生产收益。原前关闭理由要求它先让 Ch30/35 原选择“失效”，门槛高于合同§3 的条件替代设计；现恢复为 2+1+2=5 标准仅报告，不自动增 Books。此为作者纠错，非 root 单项或整日 Gate。

### 逆向后定点自纠：15609 / 15809

[15609 exact-v1](https://arxiv.org/html/2604.15609v1) §3.1–3.4/Tables 2、6、8：远端仅一轮返回完整 probability vector 时，本地 22M ViT-Small 的可微路径与远端输出做 prediction harmonization，远端分支 stop-gradient 只是优化代理，不等于真实远端目标梯度为零；可靠样本过滤与 clean→prompted KL 抑制随机 prompt 坍缩。ImageNet-C ViT-B/16 的 BETA 62.6 优于黑盒 ZOO 等，但白盒 ETA 65.8、另一个模型 67.2 均高于 BETA；作者单 RTX3090 表的 45→48ms 是给定 API 配置，不能推所有远端推理。它改变的是完整概率 API 可用且查询收费时的输入适配选择，不是一般闭源语言 API 可得概率、无额外本地资源或全部模型优越。原前关闭用“未改变 Foundation 部署合同”代替贡献判断，现恢复 2+1+2=5 标准仅报告，不改 Books。

[15809 exact-v1](https://arxiv.org/html/2604.15809v1) §3.3/§4.1–4.3/Tables 7–8：oracle 手选 mask 的正确率只是上界，不是线上方案；实际方法需读取 VLM 跨层 attention，额外一次解码生成视觉 token 熵排序，只限制文本 query 对部分视觉 key 的读取，不从表示中删除视觉 token。Table 7 相同 mask ratio 的随机/低熵遮挡较差支持这个受限排序，但 Table 8 的 future-aware 全连通更差和作者承认的间接提示失败都阻止“attention 即唯一视觉因果”结论。当前 Ch23 已有视觉 token 的选择、位置及后续证据访问合同，未缺一个必须写入的长期责任；但这项条件化 mask 接口仍是可报告的局部设计替代，原前关闭要求新授权边界属错误必要条件。现恢复 2+1+2=5 标准仅报告，非整日 Gate。

### 同理由层风险复查：现仍前关闭的边界样本

本段只复查“有局部算法或新 benchmark，但是否改变可保留选择”这一共同理由层；它不是对净新36项的第二次逐篇深审，也不能充当非作者抽样。下列判断在原已读必要原文/反证上定点回看，未变化证据不重读无关附件：

| ID 与必要源 | 复查后的前关闭理由 | 与恢复项的区别 |
| --- | --- | --- |
| [15917 图像编辑](https://arxiv.org/html/2604.15917v1) §3/Table1、§4、§5/Tables2–5 | 低分40% pilot 的 rewrite/crop/spatial 分支及 feedback 有用，但类别由 MLLM 后验归因，agent、route、辅助工具和调用预算同时变化，未形成优于现有条件编辑/分解原则的稳定选择规则；Table2 多切片仍反退。继续前关闭，不是因图像编辑或 agent 名称。 | 15809 在同遮挡率有直接随机/反向 mask 比较，且读取边与删 token 是不同执行接口；15917 的多工具组合没有同等清楚的新接口边界。 |
| [16079 Flow Matching Stability](https://arxiv.org/html/2604.16079v1) §3/Table1/Fig1–2 | 同 seed 输出 ArcFace 接近与 FID 可分账；高-loss 50% FID33.92 差于低-loss23.49、balanced cluster22.80 是具体负例。但该受限 CelebHQ/共用 VQ-VAE 及作者前驱 diffusion 稳定性工作，不足以由此给新的跨数据/模型 prune 选择；Ch27 已要求 loss 代理与 held-out、覆盖/成本分账。继续前关闭，保这组反证，不写“FM 普遍稳定”。 | 16171 有固定稀疏率→可学习阈值的独立 update-support 选择，且 task-agnostic merge 接口明确；16079 还没有可复用的保留哪类样本条件。 |
| [15648 HyperGVL](https://arxiv.org/html/2604.15648v1) §2.4、§3.4–3.5、§4 | 84k问答源于2400问题×表示，WiseHyGR 的选择标签来自受测最优表示；裸V–V可丢超边身份，但有 ID 的 clique/V–E 不可概称 pairwise 必丢。它给超图任务的格式敏感度，不识别新的通用多模态表示边界或 model-independent 选择，继续前关闭。 | 15809 不是仅把同一图对象换编码/选最佳输入，而是在既有视觉表示下改变文本读取视觉状态的 attention edge。 |
| [16056 AST](https://arxiv.org/html/2604.16056v1) §3–4/Alg1/Tables1–2 | latent copy、词对齐和时长偏移为局部语音编辑路径；WDTW/SpkSim并非未编辑 waveform 逐样本恒等或身份真值，WER/DNSMOS 对基线反退，完整时延/NFE未给，尚不足改变 Ch24 的生成修正/commit 或 Ch23 表示身份选择。不是因为语音或单卡实验前关闭。 | 15609 的一次完整概率 API 与多次远端 ZOO 查询改变访问/预算组合；AST 只在一个编辑任务内叠加既有条件控制。 |
| [15760 KWBench](https://arxiv.org/html/2604.15760v1) §3–4/§7.5–8 | unprompted recognition 值得测，但223题中强制项由 single judge 判，作者明确无同题 cue intervention/recognition ablation；现只能确认新任务组织与 profile 相关，不能让“识别而非执行”成为已分离的新评价结论。Ch66/Agent 已把触发、执行与 outcome 分责，继续前关闭。 | 保留的16027/16146分别有可定位的正确子集分布或拒绝集合条件；KWBench缺支持其中心区分的对应干预。 |
| [15482 unlearning](https://arxiv.org/html/2604.15482v1) §3–4/评价 | QA anchor、邻域与 raw-logit 蒸馏组合能给所测质量点，却未隔离一个与现有 forget/retain/over-refusal 取舍不同的有效性条件；不能因五轴表或多目标名称独占新机制。继续前关闭，原反证保留。 | 本轮恢复项各有直接改变更新支持、访问调用或信息流执行的一条可指出的替代边，不仅是把成熟损失项并置。 |

这些关闭都是当前作者判断，root 如发现上述任何一项改变了真实选择条件，只重开受影响家族和同一错误理由层；尤其 16079 的单域负例不得在报告消失，也不等于已有跨域定律被反驳。

### 后续非作者纠错：八项作者前关闭已撤销

上文是当时的作者准入判断，不能继续当作当前终态。[root 八项逐篇独立重判](./V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)复用未变的必要原文/负对照后，恢复 15351、15451、15614、16076、15705、15706、16079、16135 为具条件的标准仅报告候选；其中上一表对 16079 的“继续前关闭”及首三组对应八行已被该裁决覆盖。弱对照、额外成本、单域实验、指标反退及未证普遍性仍保留，但它们限制可采结论，不抹去具体训练支持集、视觉表示、embodied 选择或评价反例。原72项先移出39、作者自纠三、非作者纠错八后，净28项前关闭；正式日20当前工作态为99候选／50前关闭／15483日期隔离，尚非日级 Gate。剩余共享关闭理由仍按来源、主题与理由层作非作者正反抽检，不把八项恢复机械扩至所有局部方法。

### 后续非作者纠错：15675／15583／15771 的前关闭已撤销

上段99／50／1是八项裁决后的历史工作态。[root 新三项独立核](./V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)发现：15675 的固定合成流水线中跨语错位筛种相对随机／单语种子有具体选择证据；15583 的本地分块 attention 前向与同文档多query缓存改变输入预算在selector和reader间的成本位置；15771 的失败探针与失败后恢复动作路由是有条件的控制分支。旧表“无新选择条件”“完全局部recipe”的关闭句因此失效，但原文中的文化真值、未匹配端到端成本、gold标签、反向指标与未隔离消融仍为限制。作者复用原必要证据、对照Ch27/76现有owner后，三项按5分标准Only进入正式§3/4；净新前关闭由28降25，本日工作态102候选／47前关闭／15483日期隔离。三项受限准入不代表其他前关闭也应恢复，更不签日期或日级 Gate。
