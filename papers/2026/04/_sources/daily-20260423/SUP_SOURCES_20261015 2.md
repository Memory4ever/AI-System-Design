# 2026-04-23 既有 Daily 来源遗漏补充（唯一记录）

## A1 范围、冻结与 ownership

作者：supp_apr23_author。只补北京时间 **2026-04-22 ～ 2026-04-22**；原52候选整行、日期、评分、小时窗口与连续原§4以[逐字baseline](./baseline-before-supplement-20261015.md)冻结。原52家族证据/实际Books写后/具名独核分层复用，原完成不等于本轮补查完成。

已完整重读实际AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、RESEARCH_SOURCES使用说明/每日14/arXiv主题、ROADMAP与State最新路由；using-agent-skills及daily-research-closure用于范围/证据分层和验收。只拥有本日README与本日_sources，不写LS/index；Books须root授窄锁和非作者实际POST。保护并发staged/unstaged，不stage、commit、push。

本日原机构证据覆盖Apr22 09点后，未变化的实际关闭及原文可复用；补查重点是自然日00–09差额和原目录外部隔离的可恢复部分。原arXiv51候选主要属于Apr23公告批，不能代替Apr22自然日检查。宽分类列表仅作标题导航，不变全文队列；主题查询若过宽立即收窄，不以召回/数量倒推准入。

当前执行：官方cs.CL有界月列表/相关主题查询；query原始返回分层保存。`SUP_TOPIC_MODEL`试探 submittedDate Apr19–22、250/938 结果过宽且主要落旧日，只作线索，不作完整覆盖或逐项AB队列；已收窄到Apr20 18Z–Apr21 18Z的title主题切片，待官方公开列表确认归属。不得将submittedDate直接写为首公开。

当前普通待办：有限集合必要Source/具体owner与实际Books POST、来源边界归并和六部分DAY/FINAL；发现入口已有限停止，不追加整库全文。逐项有效层以末节为准，无本轮完成声明。

## A2 第一有限题摘集与有效同事件层

原Apr22旧99只按baseline§3精确同事件去重，来自Apr22作者的具名路由已接纳；不继承其Apr21新补池。`V3_ARXIV_OFFICIAL_BOUNDED_DISCOVERY`与`V3_ROOT_DAILY_GATE_20260422`支持原99的Apr22公告有界组合，不更改原日期。

本次`SUP_TOPIC_FOCUS`title主题查询完整181/181（start0/max200，UTC submitted20日18:00–21日18:00），`SUP_TOPIC_MULTIMODAL`56/56、`SUP_TOPIC_SYSTEM`36/36、`SUP_TOPIC_RAG`35/35均完整单页。日期筛子仅导航，非首公开字段。完整题摘只读有限潜力/含糊身份；明确科学/医学/传统通信等范围外标题不扩原文。跨query去重；不将308槽位或试探MODEL250槽称全部AB/全文。月CL两次响应均超时不完整（分别1275981/3331384、808442/826978字节），只能有限已到标题导航，不作读完依据。

### 可复用关闭（不是本轮新增候选）

- `19087v1` OLLM：本次抓取v1并发现Apr22 `V3_APR01_PENDING_FIVE_INDEPENDENT`及`V3_EVIDENCE_REVIEW`§1133已有具名独核前关闭。特权gold-next-token encoder/oracle option不能证明部署policy同预算改善，RL部署成效留未来；精确机制和反证未变，复用关闭，不重新评分。
- `18975v1`：Apr22 `V3_EVIDENCE_REVIEW`§941及原日级否侧具名结果已核代价门、灰区/冷却和强历史惩罚漏升级；有限Minecraft阈值组合未改变现有具体长期判断。不是声称没有组件实验，复用具体关闭。
- `19321v1`：Apr22 `V3_APR20_FOUR_18943_19321_INDEPENDENT`及后续root§1105前关闭，几何选层与权重分配反向结果已保留；不因新命中再次评分。

### 实际完整exact-v1题摘后本批工作判断

| 身份 | 约束→原文实际增量→需改变选择，或具体关闭理由 |
| --- | --- |
| 19011 Sobolev diffusion | TO局部最优示范缺误差恢复→反馈gain作为逐denoise-step导数监督而非对整采样链匹配→核已知可微动力学/solver条件下数据效率与推理预算；拟5，必要§3/4/5实际已读。 |
| 19503 ReaLB | 视觉token使EP rank偏载→按rank在dispatch内FP4/高精度转换而非复制expert→核精度/调度/负载依赖；拟6。v1只有1.29×layer速度及1.2%损失，不采用currentv3的端到端1.10–1.32×。 |
| 19654 FEPLB | rebalancing与SM计算竞争→inter-node标准EP后intra-node NVLink Copy Engine重分配＋CPU并行调度→核共享链路及动态expert权重成本；拟6。 |
| 19657 GAAP | 单步IFC不能保跨任务敏感流→持久store/annotation绑定user permission并隔离模型可见数据→核deterministic保密的实际closure/信任边界；拟6保护深入。 |
| 19724 benign overfitting | ViT对抗训练的鲁棒泛化解释不足→简化ViT在SNR/扰动预算条件下良性过拟合界→核假设/训练模型和泛化对象；拟5。 |
| 19544 DT2IT-MRM | 风格/标签噪声混入reward→强度标签、T2I重构及迭代curation→只补决定准入的干预/对照，未把三榜第一当机制证据。 |
| 19572 TACO | terminal observation异质/长程冗余→从轨迹自发现可复用过滤规则→仅最小核规则执行/更新与同预算反证是否超成熟压缩配方，未评分。 |
| 18847 harm recovery | 人类rubric→reward→候选plan rerank是成熟反馈/搜索组合；50任务/偏好数据集及整体效果未在题摘建立新的恢复原子性、补偿可行性或保护条件，拟贡献前关闭；v1是1150 pairwise，不用currentv2的1130回填。 |
| 19034 ABot | VLM affordance→online hierarchical memory→探索优先级是成熟空间记忆闭环组合，整体coverage收益未区分新表示/更新有效条件，拟关闭，不因embodied应用硬排。 |
| 19064 SDB | hidden hypothesis扰动、soft权重与稳定正则为已有探索/稳健训练配方组合；三个VLN局部工作点没有新边界/保证或明确设计改判证据，拟关闭。 |
| 19231 noisy receiver | memoryless noisy primitives/no-bypass cut为一般通信/计算信息论，没有foundation model、模型并行或当前神经runtime的直接机制桥；不凭inference/cut词跨接，拟范围关闭。 |
| 19565 attention hallucination | 四个attention统计＋logistic detector、约100 heads的选择为成熟特征/正则组合；task-specific/model-dependent PR-AUC及选特征改善未给新检测保证或证据权威条件，拟关闭，不外推为无幻觉检测。 |
| 19656 GRIL | clarify/pause两阶段奖励与继续解题是成熟信息补齐交互RL组合，insufficient-math整体指标未分离新的可执行pause/恢复或置信度保证，拟关闭。 |
| 19716 logical subspace | paired-view CCA＋hidden steering为成熟多视图投影/干预组合，四逻辑任务accuracy并不证明独立逻辑因子或新的迁移保证，拟关闭。 |
| 19728 VLA Foundry | 统一LLM→VLM→VLA训练代码/开放simulator和checkpoint不独立构成新训练/表示机制；替换Qwen3-VL基座的整体差异未隔离新适用边界，拟关闭。 |
| 18779 Mango | 完整v1题摘在FOCUS原entry；URL bandit/Thompson/episodic memory已有组合，两个benchmark success增量没隔离新条件，拟EX供root首批抽核。 |
| 19193 CLVG | 完整v1题摘在FOCUS与MULTIMODAL原entry；taxonomy＋AVE/低logic互动成功率没有在AB控制judge/任务协议混杂并提出新失效条件，拟EX供root首批抽核。 |

`20329`当前官方DeepMind正文仍显示Apr22日级日期，身份/v1和旧具名必要Source反证吻合；其09点保留不再是本自然日资格要求，但最终准入/Books仍需本轮root核。`Seed3D2`官方paper Apr22且完整题摘已读，正确静态PDF为`Seed3D_v2.pdf`，旧21443v1实际是Halpern算法论文，不采用该错误身份；原报告存档行不静默改写。Seed模型的粗细分阶段、locality codec及直接PBR输出拟6必要核，不将物理ready当真实动力学验收。两项均待本轮校准。

OpenAI自然日RSS已实际完整1293项，5条落Apr22（其中4条与原日有效事件重复）；新`Privacy Filter`原pubDate为Apr22 00:00 GMT=北京08:00，原09点窗口漏了该项。官方核心已读：AR checkpoint转bidirectional token classifier、一次forward＋BIOES/Viterbi、runtime operating point与annotation-corrected benchmark；对误漏/过度redaction、static taxonomy、非匿名化保证的限定有必要模型card支持，拟5，待root准入。CLI原文Cloudflare，仅用web原官方恢复，不把challenge当正文。

### 第二有限题摘集（各精确v1在SUP_AB_IDv1 raw）

| 身份 | 实际题摘工作判断 |
| --- | --- |
| 19679 MMControl | joint audio/video单尺度控制耦合→dual-stream bypass与逐modality guidance独立调整→核控制独立性与joint一致性/预算的边界，拟5。 |
| 19683 Mask World Model | RGB外观噪声干扰policy→预测semantic-mask dynamics作为信息瓶颈再接diffusion action→核丢外观信息后动作充分性/接触与背景鲁棒性的控制，拟5，不接受“强制捕获真实物理”。 |
| 19734 UniT | 本体动作不兼容→动作/视觉双向cross-reconstruction＋fusion离散token→核视觉后果锚与动作支持集/encoder消费条件，拟6，t-SNE不是物理等价证明。 |
| 19741 CityRAG | 生成先验无地理实例身份→geo-registered且temporally-unaligned context训练分开稳定scene/短时属性→核新视角/loop/retrieval的地理锚和动态一致性，拟6，不由长视频认定物理模拟正确。 |
| 19747 AnyRecon | 固定一两view限制稀疏重建→capture-view cache去temporal compression＋显式geometry memory检索→核任意view支持域、frame correspondence和重建-生成交接条件，拟6。 |
| 19536 LiveVLN | 多步continuation/感知执行overlap与prefix耗尽前handoff为成熟async控制配方；题摘平均等待时间不新增状态对齐/截止期或动作可执行条件，拟EX；不是因runtime或小实验排除。 |
| 19710 SpanVLA | AR reasoning＋flow action/history init、GRPO负例恢复与新驾驶数据为成熟已知组合；题摘NAVSIM整体指标不隔离新的bridge状态或恢复支持集保证，拟EX。 |
| 19720 ReImagine | image-first appearance＋SMPL-X motion＋video temporal refine为成熟解耦pipeline，题摘不给新的时序成立条件/取舍反证，仅质量改善，拟EX。 |
| 19522 GenerativeMPC | VLM-RAG输出MPC velocity/safety及impedance参数是成熟语义/控制分层，但有保护“safe/predictable”信号，仅最小核是否hard envelope独立控制及证据边界，不把60%减速自认证安全；未评分。 |
| 19564 EgoSelf | interaction graph→profile→future interaction预测为成熟长期memory/用户建模组合，任务表现不提供新更新有效性/隐私条件，拟EX。 |
| 19566 Diagnosable ColBERT | clinical concept-latent对齐/专家相似约束的position paper，当前是暂缓生医应用且未给一般retrieval机制的新验证，不由diagnosable/latent词重引范围；EX。 |
| 19004 Ocean | exact symbolic SpGEMM内存分配→HyperLogLog cardinality estimator＋shared/global hash accumulator的有界执行分支→核低估/overflow回退和稀疏形状下可执行性，拟5，非把一般GPU加速数直接外推LLM。 |

新增准入至此仍是工作提案，需root有限校准/必要证据；不由抓取HTML数认定已读全文或固定候选分母。

### 有界标题补检与共同有效层复用

为弥补提交时段query会漏早提交/延后公告，本次只查看原Apr22 `arxiv-owner-receipt.json`中18585–18700这段非原99的27个具名标题（不继承其generic labels、全月分母或Apr21本轮补池）。相关5完整题摘为18585/18603/18623/18639/18648；其中18585 recurrence研究正交多项式/分子积分无直接模型执行桥，18639 warmup/consistency/reflection/curriculum和18648舞蹈语法/normalization/loss已有具体关闭，18623已具名v1负侧反查；分别复用Apr22 `V3_REVIEW_CHECKPOINT`§216/136/219和`V3_EVIDENCE_REVIEW`§1034/1043，不将理论、小模型或人体运动一概排除。

`18603 Dual Triangle Attention`完整题摘新增线索：双向attention失去因果mask的顺序偏置→每head QK子空间分两组past/self与future/self三角mask→核无需位置embedding的顺序信号、RoPE可并存和单kernel可行条件；拟5必要Source，不因protein实验纳AIforScience，只审自然语言MLM及机制。该项不在原99/170具名集合，不能用旧generic关闭覆盖。

## A3 已实际必要Source（作者准备，不计独核通过）

### 19011v1 — Sobolev diffusion（2+1+2=5）

本日exact-v1 HTML实际§2.2/3.1 Eqs7–11、§3.2、§4.1–4.5及§5。iLQR/ProxDDP给局部feedback gain，链式动力学导数构成trajectory chunk对state-history的Jacobian目标；完整diffusion链末端导数匹配Eq10在实验失败，实际Eq11用逐denoising-step的x0估计匹配该目标，两者不等价。Stochastic Sobolev单随机projection减少完整Jacobian/Hessian负担，仍每epoch约2倍Diff费用；交替loop同时从warm和unwarm初值解TO、拒未收敛解、重建dataset，不能把全部收益只归导数loss。

§4实际300k U-Net、K5、默认Th32/To1/Ta31，固定dataset5seeds、每seed50个随机实例；单笔记本i9-13950HX/RTX2000ADA、仿真pendulum/UR5/quadrotor。部分固定dataset对照支持更少轨迹可达到该solver局部解质量，不证明5–10倍普遍样本律。长action length虽省rollout却增TO迭代，Table2存在Ta15总5.1s慢于TO-alone4.1s；不能只报求解器时间而漏policy rollout。§4.5没有显式constraint项、碰撞failure仍须另外验；已知可微动力学、solver feedback gain与低层控制是条件，contact-rich仅未来工作，不写真实安全/通用VLA部署。

### 19654v1 — FEPLB（2+2+2=6）

实际§2.1–2.3/§3.1–3.5/§5：标准EP先跨节点dispatch，static expert计算期间，CPU按当前token histogram做确定性whole-expert贪心迁移，机内NVLink Copy Engine并行搬weights+tokens；dynamic专家后算，再combine。Token仍给同一logical expert；native weight/optimizer/gradient owner不能因临时copy改变。只迁whole expert保grouped GEMM粒度，小token threshold与dyn控制适用范围；约50us CPU及max_num_dyn8×72MiB=576MiB buffer均是实际费用，不是没有开销。

作者H100SXM5/80GB、机内NVLink4、节点间400GbIB；18而非78层GLM5 variant、128 experts，PP4/EP2、PP4/EP4、PP2/EP8，Megatron+DeepEP/TransformerEngine/cuBLAS。指标是max-minus-mean token/GEMM straggler及perMoElayer，不是完整step或收敛；EP2 backward14.4ms仍慢于CE重实现FasterMoE14.0ms，动态专家数收益递减。共享NVLink/HBM仍可能争用，SM-free不推出无带宽竞争，bulktransfer兼容与static-compute隐藏窗口有条件；不采用作者“true orthogonal/消除overhead/免费”普遍称。质量、seed/不确定性、全step与恢复未披露/未核，不授长期训练精确等价或跨拓扑总收益。

### 19503v1 — ReaLB（2+2+2=6）

实际§4.2–4.4、§5.1–5.5、§6，采用原精确v1而非currentv3。对当前EP rank的token load与vision fraction双threshold发precision plan，**整rank的专家都可W4A4，包括混在其中的text**，不是只量化视觉token。原BF16 weights+precomputed scale保留，临时FP4转换与metadata allgather在dispatch期间重叠，received activation的量化在GEMM融合；不能由“没有常驻多精度副本”声称零临时buffer或无需scale。global batch threshold2048=256×8、modality threshold.7、capacityC1为受测设置，小batch全rank同时关闭保持同步；常量不授跨设备通用阈值。

v0.13 vLLM、FlashInferNVFP4/LLMCompressor、8RTX5090；Kimi-VL-A3B/Qwen3-VL30B-A3B/ERNIE4.5-VL27B-A3B、BF16 vs FP4-All/EPLB/async/seq对照。§5.2 layer计时明确排除dispatch/combine；§5.3 5k请求、两图、output8，但通信另借H20/NVLink profile以代5090弱互联，因此不能报为单一实机完整服务/SLO。**更正A2简写：v1摘要只有1.29×layer，v1Intro/§5.3确有E2E1.06–1.53×宣称；不得说v1无E2E。** 模态比例是经验敏感度代理，RealWorldQA约3point下降，.9阈值的MMMU反较.7差；不能采“保护text无损”、免费调度、PD生产更快或跨模态扩展保证。

### Privacy Filter — 官方Apr22 model card

准确官方PDF已存`SUP_OPENAI_PRIVACY_CARD`；实际pp5–7/11–18。AR checkpoint将mask改bidirectional band128（单层有效257）并替换33classBIOES head；一次forward并不等任意128k输入内信息全局可达/可用。8blocks/14Q2KV/top4of128MoE，Viterbi合法transition与6bias选路径；runtime阈值/transition改precision-recall，不改训练privacy taxonomy，后者须finetune。漏标与过度redaction、非匿名化/非合规保证明确，不执行模型/代码或宣称production测过。

模型card§7.2.1–7.4：baseline已经先做rule cleanup，不是未改原benchmark；corrected再只对model检出而dataset未标的span经GPT5.4审，约10kspans/8kexamples，人工仅100span100%agreement；反向漏检 adjudication只有85%未采用。corrected非全面独立重标gold，不能把两套token/span/F1直接混为公开原榜单。CredData tokenF1.842与exactspanF1.617不同；SPY因仅prompt-author且taxonomy不同先F1.545，10%finetune后.962属于适配证据，不纳生医领域研究。近线索位置/一跳alias距离使recall退化，128k可接受长度不认证远程alias解析；本次只采用固定taxonomy/decoder、评价版本与policy变更分责。

## A4 首三项逐字PRE提案（未授锁、不写Books）

### 19011 → MULTIMODAL-EMBODIED-VLA / Ch26

目标：`闭环主干`三时间尺度段之后、`Hierarchical Generative Planner`标题之前；上游Ch25预测状态不是真实状态、下游Ch27训练数据provenance的交接不改。现Ch26有learnedproposal/controller分权、连续轨迹的解析导数，但没有**solver反馈gain作为逐去噪监督**这条训练分支。拟插两段：

> 当动作生成器只为已知动力学的轨迹优化器提供初值时，监督还可以包含局部反馈，而不只模仿最优轨迹。局部最优示范往往没有小失误，policy稍偏离就可能落到示范未覆盖的状态；若iLQR类solver已经给出控制对状态的feedback gain，可沿可微动力学传播成action chunk对history的导数目标。一个受限diffusion分支让每个去噪步的干净轨迹估计匹配这一目标，以随机投影控制导数计算费用。这不是把整条采样链的最终Jacobian精确匹配，也不让policy接管约束求解；学习器提议warm start，原solver/controller仍检查并修正。
>
> [Sobolev diffusion的有限对照](https://arxiv.org/html/2604.19011v1#S3)支持这种监督接口，但每epoch约多一倍训练费用，交替收集又包含warm/unwarm双求解、失败过滤与dataset重建，不能把总改善唯一归于导数项。较长chunk省rollout却可能增TO迭代，需结算policy加solver的总时间；损失没有显式碰撞约束，已知可微动力学和可用feedback gain是前提。动力学失配、接触复杂、导数目标或净预算失效时，保留普通轨迹模仿、短chunk重观测与原TO/独立controller，不从仿真局部样本效率签发真实安全或通用VLA收益。<!-- source-family:SF-2026-ARXIV-2604-19011 -->

### 19654 → TRAIN-DISTRIBUTED-TRAINING / Ch36

目标：`Expert Parallel 从静态放置到动态 Token + Weight Spill`的reactive-spill成本段之后、MoonEP段之前。现文已经有spill/副本nativeowner，不重复它；只补**whole-expert、NVLink CE与staticcompute窗口**的具体边界。拟两段：

> 保持同一router图时，spill还能先按硬件资源拆成两阶段：标准EP完成跨域dispatch，机内把少量expert标为本轮可迁移，在固定expert计算期间由CPU按当前计数生成whole-expert搬运计划，再由NVLink Copy Engine复制相应权重和tokens。这样不必把GroupGEMM切成很小的每expert流水，临时执行位置改变而logicalexpert、nativeweight/optimizer及梯度归属不变；静态expert的计算时间同时成为隐藏planning与复制的窗口。
>
> 这份窗口不是免费资源：Copy Engine不占SM仍可能争用NVLink/HBM，whole-expert粒度在低EP或小热点时不够细，额外weightbuffer也占显存。[FEPLB的H100/截层GLM5对照](https://arxiv.org/html/2604.19654v1#S2)有低EP backward反退，仅报告所测per-layer/straggler而非全训练收敛；约50usCPU与576MiB示例buffer须进成本账。复制无法被staticcompute隐藏、拓扑/梯度owner不兼容或净step收益不成立时，保留静态EP、原spill/replication或较低频规划，不由SM-free批准完全无竞争或全程等价。<!-- source-family:SF-2026-ARXIV-2604-19654 -->

### 19503 → INFER-TENSORRT-LLM / Ch49

目标：`MoE Dispatch 应平衡时间，而不是固定代理量`的time-aware共存段之后、`Placement 从事后响应推进到预算内预测`之前。只补**不迁移、以rankprecision改服务时间**的替代分支，不重复costsurface/placement。拟两段：

> 若多模态prefill的热点变化太快、权重复制又难摊销，还可以不移动token或expert，而改变热点rank的执行精度：用当前routing计数和模态比例提议rank级precisionplan，在dispatch期间重叠metadata同步与权重量化，收到token后再融合activation量化。保留原高精度权重避免多份常驻副本，却仍有scale、转换和临时缓冲；视觉占比只是敏感度代理，整rank低精度会同时影响其混合的text，不能解释为只压缩视觉token。
>
> [ReaLB v1的受限对照](https://arxiv.org/html/2604.19503v1#S4)只在披露的FP4硬件、大batch与三种MoE-VL模型支持这条取舍；小batch需所有rank共同关闭以免同步失配，较高模态阈值也不保证每个任务更准。Layer计时排除dispatch/combine，文中端到端结果另借H20/NVLink的通信profile，不能合成单一5090集群的服务SLO；部分视觉问答仍有约3point回退。质量、precisionABI、可重叠窗口或总费用不合格时，保留BF16/既有dispatch与放置策略，不把动态精度当作无损负载均衡或免费生产加速。<!-- source-family:SF-2026-ARXIV-2604-19503 -->

## A5 后续作者实际必要Source与收窄

### MMControl 19679v1（2+1+2=5）

实际本日SUP_AB_19679v1 HTML §3.1–3.4、§4.1–4.3/§5。Reference image与结构帧沿时间拼接，以mask区分reference和generation；audio同样reference+silenceplaceholder、不是已支持任意pitch/energy控制。Visual/audio bypass不含它们之间额外cross-attention，在原jointDiT偶数层分别residual hints，γv/γa控制hint强度，jointbackbone仍耦合两模态。Zero-init只保护初始，不认证训练后旧生成无损或两控制因果独立。Stage2借LTX2冻结distilledLoRA/3step且CFGoff并重编码条件，不能把两阶段收益只归bypass。

LTX2-19B、30kHallo3、4H200/7200steps/约12h；两组各200sample，GTaudio驱动baseline与联合生成speech任务不同；SyncC/D、DINO/CLIP和depthMAE都是指定估计器proxy，不证明完美唇同步、真实结构或身份。γv/γa控制只有Fig7定性对照，未隔离所有joint交叉效应；multi-character/conversation/unseenstyles列未来。**拟仅报告**：分支与局部controls可报告，但现Ch24条件路径/历史分权已有一般解释，原文未建立新的独立控制保证或可复用定量winregion，不把整套recipe假称已有覆盖，也不制造Booksdiff。

### Mask World Model 19683v1（2+1+2=5）

实际§3.2–3.5、§4.1–4.3/§5及必要表：训练用offline语义mask，经固定palette复用同一videoVAE；memory四RGBframe固定clean、未来五masklatent作flow目标，部署只RGB无需在线segmentation。Stage2 VAE冻结，但backbone/actionhead共同只用actionloss更新；不再有maskloss，故不能说部署feature永久等于真实语义mask。Backbone feature给actionexpertKV，36stepchunk/10Euler却只执行第一个action再重规划；mask目标并未把真实physics/contact独立监督出来，也不是显式action-conditionedmask transition保证。

LIBERO500episode/suite、RLBench6tasks各20，Franka/D435i两视角、四实机任务每task50demo后各20trial；MWM多wristview与RGBbaseline的配置差额限制唯一归因。Appearance shift保持geometry、BG/light/color而非新任务动力学；OODSR42.1/ID67.5仍大量失败，BG27.5最差，nPAUC.648vs.629只是相对保留率。Masklabels、VAE/flowpretrain、finetune、双view/10step/actioncontroller全计费；未披露通用precision/完整deadline/seedCI不补。拟ownerCh25结构化预测→动作消费的训练接口差额，非模型获得真实物理状态。

### UniT 19734v1（2+2+2=6）

实际§3.2–3.4、§4.1–4.2、§5.1–5.4/§6。三branch以真实obs pair、state/action及fusion各编码，共享RQcodebook，每个分支都重建未来DINOfeature及nativeaction；动作先pad且embodiment-specificMLP/decoder，不是消除本体适配。**VLA用fusion离散code作辅助predictiontarget，实际flowactionhead消费共享VLMfeature，不是把预测code直接decode成动作。WM则只读state/action branch的continuous pre-quant features以避免未来图泄漏，不能把二者叫同一离散token协议。** 跨重建是训练对齐约束，不证明同code物理等价或tSNE是因果证据。

RoboCasa24tasks×50episode、full24k/few2.4k；EgoDex27,419额外human、联合再robotfinetune，不能把45.5v47.8表面匹配当10倍全部数据效率。IRON50d两实机任务每task120robot、另32kproprietary+30kEgoDex预训练；OOD有human覆盖补入，zero-shot只robot无该task且仍有humanstacking示范，不等零训练。WM10step/10s低分辨率、Gemini3Pro三维评分不是动作真值，FVD未全胜；λ/额外tokenizer/backbone/head/数据与control成本均在。拟Ch26现canonical/native接口与已有关节codec之外的**训练target/部署consumer双接口**差额，WM只交叉引用不重复owner。

### CityRAG 19741v1（2+2+2=6）

实际§3.1–3.4/§4.1–4.2/§5。同地不同时间StreetViewpair用metricECEF/相对pose，≤5m平均偏差、target73frame、context61–81frame，变长context阻止逐帧copy；firstimage持当前外观/动态先验，外部geo视频供稳定场景。Pose residual与全contextcrossattn分别训练，Wan2.1-14B原textcrossattn冻结且fixedprompt，**finetune后已不响应新caption**；不能采任意text条件或完全独立静态/动态因子。外部参照、首帧与自产AR末帧有不同provenance。

5.5Mraw/1.3Mtrainingpanoramas、8citytrain/2unseen、32A100一周/20kiters；正式定量每city10trajectory只preprocessedpairs，**不含用户任意trajectory/长autoregressive测试**。长minutes/loop闭合主要定性；20users×三问各10samples评分，地理faithfulness、firstframecontinuity、visualquality不可互替。Staticmetrics用Mask2Former除vehicle/person，PSNR低/可幻觉几何；数据无snow/rain/night而demo有snow，不授泛化保证。Map/pose/retrieval、训练/生成与重新锚定全费；拟Ch25 persistentstate旁补**外部稳定地理参照vs首帧瞬态**的训练/条件职责，不授真实simulator。

### AnyRecon 19747v1（2+2+2=6）

实际§3.1–3.4、§4.1–4.4/§5。Captureviewbank保原图，selectedviews前置成queryableKV，framewise2DVAE去temporalpooling保view对应；其“one-to-one latent/pixel”只表示时间对应，空间VAE仍有损，不采像素可逆。另π3/VGGT点图作geometrymemory，渲染visibility/sourceviewindex后按对target可见点贡献检索view；新生成views又经π3重建并**replace**geometrymemory。Sourceobserved原图与generated-derivedgeometry不能混成新增现实证据，loop可放大hallucination，文中“preventserroraccumulation”无普遍证明。

Wan2.1I2V14B/LoRAr32，dense100k→sparse10k→DMD2 30k、64A800；40frames512×896，DL3DV10scene/Tanks5scene，3viewinterpolation/4viewextrapolation。Temporalcompression/singleframevs3reference（geometry仍用3）的消融支持对应接口，而非任意数量、极小overlap都有效。Time脚注只singlepassdiffusion，另15s codec；90vs1820为DiT局部、105含codec，仍不含完整capture→geometry/retrieval/update全环，非实时20×。当前geometry初值结构失败仍生成错，增加view/无temporalcompression抬token/compute；拟Ch25生成-重建交接旁补**原capture cache与可修订geometry两份memory**。

### 18603v1 DTA（2+1+2=5，待root准入）

完整v1实际Abstract/Results/Discussion/Methods。Q、K、**V均按headwidth分半**，变2nsubhead，各独立softmax，downpast/self与upfuture/self且diagonal都留；RoPE在fullhead上先做再split。不是把同score做两个mask再相加的等价fullattention，也不能把双向attention称排列不变（应是无位置/mask理想算子的排列等变）。NaturalMLM12layers/768hidden/UNetextras、1Btokens、3seeds、256→1024；DTA+RoPE长窗仍最好、移除RoPE的DroPE明显退化，NoPE不能据此成普遍替代。probe标准head64/DTAlogicalhead128以各subhead64，不是所有底层shape完全相同；单flexattentioncall/理论乘加不授服务halfFLOPs加速。只纳自然语言与通用mask机制，不采用protein应用结论。

### GAAP 19657v1（2+2+2=6保护深入）

HTML只覆盖部分方法；完整18页PDFv1已resume取全，实际§3.2/4.1–4.5/5、§6.1–6.5/7（pp4–13）。Userprompt/keys视public、values只存privateDB，trustedpermissionDB按(data,externalparty)批准，IFC分析generatedPython；multishot/QLLM也作为sinks，继承披露给model的taints。Persistentdisclosurelog把以前给externalparty的数据重新taint其返回，annotations可细化party与哪些参数不会返回；annotation是**可信外部spec，不由开源可审就自动正确**。默认保守可减依赖，但不用本地未验证annotation授强保证。权限revoke不能撤回已给远端的值；prompt直接PII、metadata/timing及integrity不在承诺中，跨外部串联需closure，不采无条件防所有泄漏。

Prototype Python/Pyre/SQLite、10MCP/48tools，20task/三固定注入，GPT5API；AgentDojo只utility，非隐私攻防。0observedattack不证明所有adaptive/encoding/covertchannel防护；utility GAAP76vsNP81，AgentDojo64.6vsNP80.1/CaMeL10exec71有损，不能写无影响。permission85→55、真实交互58→39是reset对照，非长期UX保证；outputcode增tokens/IFC最多20s/平均13%latency、disclosurelog可无界。拟Ch72现trajectoryposteriorbudget之外补**持久permission与taintlog不是同状态、外部返回再污染**的机制；尚未核artifact/复现/形式soundness，不授deterministic全球保证。

### 19536 LiveVLN / 19522 GenerativeMPC最小门

LiveVLN实际III-A/B及IV-A–D达到必要Source：guard已承诺/执行、tail未释放可改，新refresh以committedguard条件化；wallclock最短prefix对EMA感知推理预算，不赶上仅已验证one-stepbackup否则STOP。固定StreamVLNguard2与native4、NaVIDAchunkadaptive不同；G1每backbone40run=8instruction×5，变化inferencefrequency/actionexposure非同trajectory严格因果。blockingmore-rounds使waiting30.5→52.2%，full10.3%；withouttail损task、withoutadaptation损continuity，直接改变handoff接口判断，转拟6候选。2mendpointsuccess不授collision，meanlatency不证deadline或有效τ/backup；拟Ch26快慢/streaming接口内补guard/tail与wallclockbudget，不重述async本身。

GenerativeMPC实际IV/V：VLM-RAG直接给vmax/dsafe/K/D，APF是softcost且goal.5m内衰减为0，无独立hard-envelope/certificate。五demoseed和固定人偶/handscene，60%仅.25→.10m/s，fullbimanualhardware未来。成熟RAG/MPC/admittance组合未建立新保护成立条件，拟具名EX；保上述具体反证，不采用safe/predictable或simreal误差全由Modbus的无控制归因，不因security词把它抬高分。

### 19004收窄与19544/19572状态

root第二批actualAB指出19004仅通用SpGEMM/HLL allocation、无foundationmodel/训练runtime直接bridge，已按此**贡献前关闭**，不再追附件，A2潜力原记录保时序。19544最小§3/4揭示fixedchosenfirst与parser重评信号，19572最小§4/6.2识别typedruleexecutor/complaint与benchmark多轮演化；两项待root准入校准，不将prepared算完成。各原对照/反证保留，不凭Books已有就删候选。

## A6 必要理论反侧与首三实际写入

### 19724v1 — Benign Overfitting（2+1+2=5，中心保证深入）

完整HTML恢复后实际读§3–6必要定义、Condition4.1、Theorem4.2–4.3和Lemma5.3–5.6，不遍历3MB附录。模型是固定readout、两层简化ViT，数据有一个类别signal与其正交子空间Gaussian噪声，其维数/宽度、N²量级和tiny initialization等条件不等真实预训练ViT。Small τ下signal attention增长、moderate τ下接近uniform而需更强N·SNR²是受限作者理论；大τ失败仍属于该特构分布。Synthetic d1024/M16/dh128、最多22train/100test；real images先统一L2 norm5再加Gaussian，full-batch GD/.1、PGD20step，实验不是任意自然数据SNR的可实施测量律，也不把augmentation当独立新增N。

两处具体打印桥需独立窄核：§4 `Discussion on Multi-Norm Attacks`把p≥2的norm equivalence写成`||x||2 ≤ ||x||p ≤ d^(1/2−1/p)||x||2`，x=(1,1)、p=∞已使第一不等式为√2≤1，因此不采用“all proofs transfer”。§5.3 Lemma5.6/S5.Ex19把`P(min margin≤0)`等同`P(clean margin +(clean margin−min margin)≤0)`；clean=1/min=−1时前真后假，正确代数应减gap。只反驳所打印多norm转移与证明等式，不宣称整个L2 theorem不可能。拟5中心保证暂缓、Books0；重开需该桥勘误/独立可核修正及匹配条件，不以降分/删候选逃避。已交root最小反核，尚未通过。

定点补读对应Appendix G.4.2 `Robust test error`而非全部附件：Eq102之后同一robust error推导重复`clean +(clean−min)`等式，未在这处必要证明修正。因而争议不是只看main typo就宣布全部证明错误；保打印桥反例，修正后的L2结论是否可成立仍不预判。当前official Atom已actual读16身份title/comment：19724另有admin text-overlap with2409.19345 byotherauthors信号，非withdrawal、不由此判抄袭；19533新v3只有leaderboard更新说明、UniT v2只ancillary citation/manuscript unchanged，其余可见comment无具名撤回/勘误。原件`SUP_CURRENT_SIGNAL_20261015.raw.xml`，不称完整版本史检查。

### 19011 / 19503 / 19654 有效层与实际落笔（actual POST通过）

root已actual必要Source和A4逐字PRE/当前target邻接：19011 §3/Eq7–11/Alg1–2、§4.1–4.5/Fig2c/§5；19654 §2–5/Tables1–4；19503 §4–6/Tables1–2。19011 Fig2c Ta1总9.4s比TO4.1s慢、Ta9总1.6s/solver.56，不能把solver局部20×写总费。FEPLB native gradient/version协议正文未披露，原PRE中既成事实措辞已按root要求收窄为规范性约束与另验；ReaLB mixed5090 compute/H20 communication profile的E2E边界保持。

日资格由本日`SUP_DATE_FIRST_20261015.raw.json`各doi.attributes.dates的v1 Updated分别Apr22T00:27:23Z/01:01:28Z/01:10:47Z，created/registered都Apr22、`SUP_DATE_FEPLB_20261015.raw.xml`header Apr22/仅v1，与已认可官方ID公告规则/旧Apr22 18585–19498邻界/Apr23 19749起次批组合。root已逐字段实际核并通过**Apr22自然日**，不把Submitted/Updated/OAI/DOI任一单证改名first-public，不追公开秒。旧09点hold不自动带入新自然日。

root授三独立窄lease后，作者已保存：19011 Ch26三时间尺度后/Hierarchical前两段（约194–196）＋本人Review note1800；19654 Ch36原reactive-spill成本后/MoonEP前两段（773–775）＋本人note1898；19503 Ch49time-aware共存后/Placement前两段（800–802）＋本人note2464。仅三本人正文及note，完整局部邻接作者已顺读，限定diff-check通过；root实际逐字正文、完整局部邻接与本人note POST通过，三窄lease全释放，作者已仅行政同步三本人note并实读回。本日3项真实整合，不授整日。

## A7 后续逐字PRE（准备，不授Source/写锁）

已复读ROADMAP、Books上下文、Ch71/73交接和Ch25/26/27交接。下列均需root实际必要Source/owner/PRE与日资格通过后另授窄lease，不因准备段落而计整合。

### Privacy Filter → PLATFORM-SECURITY / Ch72

位置：`Decoding Constraint`现两段后、`Agent Privacy 必须对整条Trajectory记账`标题前。现文有PII filter与跨步posterior预算，缺**token标签taxonomy、解码operating point与label adjudication版本**三分责；不接管Ch66通用评估，只保隐私释放条件。

> 单次文本脱敏也须分开“什么算敏感”和“在已定义类别内怎样取舍误漏”。一个受限模型分支将autoregressive checkpoint改为双向局部attention与BIOES token classifier，一次forward后用Viterbi合法转移和bias选择敏感span；运行时调整precision–recall不等于改隐私taxonomy，新的敏感类别仍可能需要重新标注与微调。窗口和可接受输入长度也不同：长文能送入模型，不保证相距很远的别名/间接线索已连通，更不使被保留文字自动匿名化。
>
> [官方Privacy Filter model card](https://cdn.openai.com/pdf/c66281ed-b638-456a-8ce1-97e9f5264a90/OpenAI-Privacy-Filter-Model-Card.pdf)的原benchmark、rule-cleaned与模型提示后复审的corrected标签必须分开版本；只审模型找出但原标签漏掉的span，会改变评价人口，少量人审一致不认证全面独立gold。固定taxonomy、decoder设置、域与标签版本共同构成脱敏资格，误漏与过度删除分别验收；推理、Viterbi、标注复审和适配都计费。新域、长距离线索或标签不可信时，保留规则/更保守的删改、人工复核或不释放，不能由一次高F1签发跨步隐私、法律合规或未知类别保护。<!-- source-family:SF-2026-OPENAI-PRIVACY-FILTER -->

### GAAP 19657 → PLATFORM-SECURITY / Ch72

位置：现AgentPrivacy两段/posterior marker之后、最小披露抽象语言段之前。现论点是量化披露风险预算；缺**跨task持久taint、外部返回值重新污染与permission/log双状态**的执行机制，不把IFC称从无到有。

> 跨任务还有一份不同于风险预算的状态：外部服务已经见过哪些秘密。一个受限IFC执行环境让模型只见公开key与代码结构，私有value留在受控store；读取和运算传播taint，向指定外部entity披露时再核用户permission。若同一entity以后返回数据，返回值须继承其历史披露log的taint，避免新任务把已知秘密洗成public。Permission表达当前允许什么，disclosure log记录已经发生什么；撤销权限不让外部收件人遗忘，两个状态不能合成一个可清零授权位。
>
> [GAAP的必要机制与评价](https://arxiv.org/html/2604.19657v1#S3)依赖所有相关model/tool通道被调停、可信store与annotation及准确entity身份；它不保护先被当作public送入prompt的秘密，也不能从有限固定注入的零观察泄漏推及所有covert channel或串谋。注释/权限维护、持久log、IFC与更多代码生成均付费，utility与latency仍有损失；log持续增长也有生命周期成本。无法追踪返回来源、权限或taint不完整时，停止该披露并保留隔离/人工审批，不让deterministic标签替代端到端信任边界验收。<!-- source-family:SF-2026-ARXIV-2604-19657 -->

### UniT 19734 → MULTIMODAL-EMBODIED-VLA / Ch26

位置：现多指手codec两段后、`Privileged 3D Teacher`标题前。旧文是部署latent→embodiment decoder；差额是**共享码训练目标不等实际action输出消费者**。

> 共享动作码还可以主要服务训练对齐，而不成为部署时的动作解码器。一个受限跨本体分支将当前/未来视觉特征和原生state/action分别编码，经共享量化形成fusion codes，再跨重构视觉后果与动作；本体专属输入输出接口仍保留。在VLA中，预测fusion token可作辅助目标，实际连续action head却消费共同backbone特征；在world-model消费者中，又可只读量化前的action branch以避开未来视觉泄漏。因而“统一token”必须随生产目标和实际消费路径解释，不能从token命名或t-SNE聚类批准跨本体动作等价。
>
> [UniT的受限对照](https://arxiv.org/html/2604.19734v1#S3)支持视觉后果锚定的表示分支，不证明隐藏因果状态或未知本体可直接执行；human-video增益仍需机器人适配，world-video分数也不是action成功。视觉teacher、共享codec、原生decoder、额外人类数据与VLA/action训练均付费，应分别验cross-reconstruction、目标任务闭环和实际部署consumer。码或本体接口失配时，保留原生action、已标定codec与显式retarget，不把辅助预测正确代替控制器、安全边界或真实动作提交。<!-- source-family:SF-2026-ARXIV-2604-19734 -->

### LiveVLN 19536 → MULTIMODAL-EMBODIED-VLA / Ch26

位置：本次19011两段后、Hierarchical标题前；与19011不重叠。旧三时间尺度未区分**已承诺prefix与可修订tail、wallclock覆盖/backup**，不是重述async。

> 感知与执行重叠时，还须把action buffer切成已经承诺的guard prefix和仍可修订的tail。慢层刷新以已承诺prefix为条件，不能在新观测回来后重写已经执行或即将执行的动作；下一次refresh也应在prefix耗尽之前启动。一个受限导航runtime用感知推理时延的EMA与margin选择足够覆盖wallclock预算的最短prefix，赶不上时只消费已验证的一步backup，否则STOP。这里控制的是handoff与动作承诺边界，平均生成更快不是deadline证书。
>
> [LiveVLN的受限对照](https://arxiv.org/html/2604.19536v1#S3)中，单纯让blocking系统更频繁刷新反而增加等待，去tail或去自适应分别伤害任务与连续执行；但guard/chunk与推理频率也改变，不能当完全相同trajectory预算的唯一因果。Prefix身份、时钟、时延估计、backup验证及buffer维护均付费；有限实机端点成功与小平均jitter不证明碰撞安全或最坏时限。估计失配、新观测推翻旧guard或没有有效backup时，应停机重观测、缩短chunk或回blocking controller，不以不断运动代替可信执行。<!-- source-family:SF-2026-ARXIV-2604-19536 -->

### CityRAG 19741 → MULTIMODAL-WORLD-MODELS / Ch25

位置：persistentstate的provenance/timestamp要求之后、pose-indexed generated-history段之前。旧文有generated-history检索，缺**独立观测的地理稳定参考与首帧瞬态**。

> 记忆也可以来自独立拍摄的地理参照，而不只来自自己生成的历史。把不同时刻、同一metric坐标附近的街景作为context，可训练生成器从参照读取稳定场景结构，同时从当前首帧读取天气、外观和短时对象；共同camera pose与专门的地理cross-attention承担对齐，参照时间不应伪装成当前observation。这里训练的是条件职责分工，不是对动态物理状态的完整恢复，也不意味着场景在两次拍摄之间没有改变。
>
> [CityRAG的正式定量](https://arxiv.org/html/2604.19741v1#S3)限于预配对短轨迹，不含任意用户路径和长autoregressive闭环；长分钟重访展示与静态mask指标不能认证动态对象或精确几何。地理配准、context检索、pose、额外训练与生成均付费，冻结原文字路径的适配还可能失去新caption响应。地理误配、场景改建或瞬态条件不可信时，保留当前真实观测、短段条件生成和可靠地图/simulator校正，不让外部参考把过去状态提交成现在的事实。<!-- source-family:SF-2026-ARXIV-2604-19741 -->

### AnyRecon 19747 → MULTIMODAL-WORLD-MODELS / Ch25

位置：generated-frame几何更新/2604.01001段之后、ObjectAddress标题前。现文有生成帧更新geometry，缺**不可混淆的原始capture viewbank与可替换derived geometrybank**。

> 稀疏重建与生成循环还可分开保存两种memory：原始capture views保留观测证据，可修订geometry只服务当前视角检索和条件化。先用几何投影的可见点贡献选择reference views，把这些view的latent KV前置给生成器；framewise codec去掉时间池化以保view对应，却不把有损空间VAE变成像素可逆。新生成view再次重建并替换geometry时，改变的是derived bank，不增加新的真实capture，也不能让几何自洽抹去观测provenance。
>
> [AnyRecon的有限消融](https://arxiv.org/html/2604.19747v1#S3)支持多reference与无时间压缩的接口取舍，不证明任意view数量或极弱overlap都稳定；生成错误仍可反馈到下一轮geometry。Capture编码、点图重建、检索、多view token、生成及geometry替换均付费，单pass DiT时间也不等完整loop，更非实时吞吐。结构初值、可见性或reference错配时，保留原capture、已可信geometry和短段重建/新观测刷新，不把迭代生成当作消除error accumulation的保证。<!-- source-family:SF-2026-ARXIV-2604-19747 -->

### Mask World Model 19683 → MULTIMODAL-WORLD-MODELS / Ch25

位置：`从重建Observation到预测可推进Representation`原一般四段之后、LeWAM共训段之前。原文已说目标representation和闭环消费者分账，但没有**固定语义palette经原视频codec预测，再转action-only loss**的具体压缩分支；拟两段而非泛重复语义state。

> 预测目标还可以先经过有损的语义分割，而不是选择另一层连续视觉feature。一个受限机器人分支把离线semantic masks按固定palette编码为RGB，复用视频VAE，从短RGB history预测未来mask latents；随后保留这条backbone，将动作作为另一扩散分支训练，第二阶段只对action计loss。Mask是训练pipeline给出的类别瓶颈，第二阶段冻结的是codec而不是所有预测权重；action head读取backbone特征，也不等于控制器直接消费已验证的未来mask或真实物理状态。
>
> [Mask World Model的有限外观扰动对照](https://arxiv.org/html/2604.19683v1#S3)支持减少背景/颜色干扰的分支，但mask丢失纹理、材质或细接触信息后未必仍足够，外观鲁棒也不等新任务动力学泛化。多view、预训练与动作适配的配置差额须保留，OOD绝对成功仍远低于ID，不能仅用相对保留率签发可靠控制。分割制备、VAE/预测训练、双view和完整动作采样均付费；类别错误、细节必要或闭环回归时，保留RGB/更丰富表示、真实观测刷新与独立controller，不由semantic标签自证物理充分性。<!-- source-family:SF-2026-ARXIV-2604-19683 -->

### DTA 18603 → MODEL-POSITION-ENCODING / Ch13

位置：`Causal mask不是PositionEncoding`两段后、局部混合标题前。Ch12初始embedding/Ch14内容routing的交接已读；差额是**双向可见性拆成两个方向softmax**，不等一般causalMask或新距离embedding。

> 双向读入也可以有意保留方向不对称，而不把整个模型改为causal。一个受限attention分支把每个head的Q/K/V通道拆成两组：一组只读past与self，另一组只读future与self，各自softmax后拼回输出。Self进入两边、两份归一化也不等于原full-attention的无损拆分；顺序信号来自两个可见集合，模型仍可同时使用RoPE，不能把mask名称解释为已拥有精确距离编码。
>
> [Dual Triangle Attention的自然语言MLM对照](https://arxiv.org/html/2604.18603v1#Sx4.SSx2)只支持受测结构的顺序偏置；RoPE组合更强而NoPE外推仍可退步，不批准取消所有位置编码。两组子head宽度、训练目标和kernel实现须共同核算，单kernel可实现也不自动等同更快的完整训练或推理。方向分组限制跨通道匹配的自由度；顺序/长距质量或净费用失配时，保留普通双向attention、显式RoPE与原head布局，不从局部结果推出任意长度泛化。<!-- source-family:SF-2026-ARXIV-2604-18603 -->

### Google Vision Banana 20329 → MULTIMODAL-REPRESENTATION / Ch23

复用未变的`V3_APR02_20329_INDEPENDENT`必要Source/owner反侧，实际重新读v1§2与Ch23统一Pixelspace全局部（约349–357）。插在该两段与marker之后、连续/离散表示总标题之前；差额是**RGB output artifact的任务解析协议**而非重写nativepixelarchitecture。

> 统一像素接口还可发生在输出端，而不要求先重建一套native pixel backbone：把分割mask、metric depth或surface normal按任务规则编码为RGB，经指令微调让原图像生成器输出，再由固定parser还原任务对象。RGB只是共享载体，颜色聚类、深度映射/尺度、坐标与任务类型仍属于可执行输出协议；看起来像depth heatmap不等可解析的metric depth，也不证明内部特征天然具有真实几何。
>
> [Vision Banana的受限评价](https://arxiv.org/html/2604.20329v1#S2)把生成质量与解析后的感知指标分开，原生成数据与内部2D/合成3D标签混训仍有不可独立复现部分；实例分割和部分法线结果也非全面胜出。Parser、色码误差、额外生成/解码、任务微调及原图像生成回归均付费，当前计算重于轻量专用head，不从同一RGB格式推普遍效率。输出不可解析、几何精度或原能力回归时，保留专用感知encoder/head、显式连续接口与独立验收，不由生成逼真批准感知真值或下游物理行动。<!-- source-family:SF-2026-ARXIV-2604-20329 -->

## A8 剩余必要Source与报告限定（作者准备）

Seed3D2正确官方18pp PDF已实际必要pp4–7/9–14：VecSet VAE双perceiver/locality aggregation与content-adaptive sparse SDF query，coarse latent→partialdiffusion refine；RGB→PBR cascade改直接multi-view albedo/metallic-roughness，材料语义VLM作为SFT条件。Lighting ill-posed、locality细节/单模块控制不充分，不能把仿真ready当物理正确。60raters/每对15票/200余prompts对五商业模型和旧版1.0的偏好比较，只支持整套有限输出；没有可匹配硬件precision/端到端runtime或子模块唯一归因。Ch23现meshcodec/几何state与Ch24生成分支仍承载表示/消费者分责，但本次不冒称具体PBR配方已经覆盖；该公开更适合**仅报告整套版本组合及限制**，未足以改变长期通用设计，不按Books已存在删候选。Articulation未采用故不扩p8附件，不采21443错误身份。

MMControl19679拟**仅报告**：dualstream提示与γv/γa独立调幅可作局部生成分支，实际仍共享AVbackbone耦合且guidance sweep主要定性，未给广泛解耦/因果独立保证；Ch24现外部参考parallel context与residual hints已承载其通用接口，未宣称覆盖完整AV算法。局部Stage2蒸馏/LoRA与运动/音画对齐工作点不改变本次长期结论，保设备/数据/GTaudio对照与全费。

19544 DT2IT-MRM最小门实际§3/4及§4.4：同model多style候选、修复坏样本含proprietary/goldstyle、listwise/pointwise一致，MRM迭代翻bottom50%再重标/重训；§4.4发现R1Reward chosen总在第一与parser-loop失败，BaseReward subset/overall不一致，修正评价口径有项目关系，不只新benchmark。拟5仅报告该具体对照纠偏；若准入需继续必要消融/尾部限制，不把929k vs2.8M当纯数据效率，未预记Source完成。

19572 TACO最小门实际§4/6.2：typed rule executor/trigger/keep/remove/minretention，关键错误保留；成功应用提高confidence，Agent看到完整输出后complaint可降权或全局delete。Complaint不是silent omission检测保证；多轮同benchmark演化与batchsize改变共享经验，RetentionTop30稳定不是heldout truth。拟5仅报告规则层可复用与bench multi-turn暴露差异；若准入仍需核必要对照/成本，未预记Source完成，不把no weights称没有训练/更新artifact。

19533 CyberDefense完整13pp exact-v1 PDF实际pp1–13必要§3/4/6–10及T5：groundtruth来自Sigma+LLM后果/enrichment，非独立真实攻击真值；50queries×10rowcap限制可见人口，但SQL aggregation可能另汇总，不宣称绝对只能看500条。26campaigns、模型N10或26、98runs每设一次，预算/覆盖与识别、是否flagged分开。Table5 caption写normalized “1=max flags anymodel”，正文却拿绝对50% tactic recall作运营bar，值最高.61而非1，内部口径未闭；5/13passing和unsupervisedready不采用。§10.2承认Sigma FP/LLMlabelerror，campaigngenerator proprietary/prebuilt JSON不等全生成链可复现。拟5，仅在root准入后以中心指标争议暂缓，保可读局部观察，不Books；重开要原分母/normalization及可信标注协议修正，不推所有LLM不能防守。

日资格增补`SUP_DATE_REST_20261015.raw.json`完整11条：除18603外v1 Updated集中Apr22T01:03–01:15Z/created02:19–02:24Z，与本日FEPLB OAI+公告邻界同向。18603 v1提交Apr9但四月ID18603/createdApr22T01:57:05Z、v1 UpdatedApr22T14:48:33Z；不能把提交日迁首发，也不将较晚修元数据当公告秒。只交root日级组合核，不对未准入项先评分冻结。

### 19544 / 19572 准入后必要差额实际读足

root完整v1AB/最小门准入：18603 5、19544 5、19572 5、19536 6；19522与19724仍定点反侧，19533准入待核。作者19544已进一步实际§4.1–4.6/Tables7–8/§5：pointwise步骤使数据355→405→337K，不能视纯单因素；同50K T2I reformulation支持局部转换。未curated942K vsfinal929K虽多数提升，但MMRLHF从92.9降至89.4，作者亦明确并非三榜全第一；64Ascend910B3/一epoch/bs512/lr grid/data制备全费，未核公开code或独立复现R1-Reward/parser批评。拟2+1+2=5标准完成、仅报告具体标签/测量纠偏，不把929K vs2.8M称纯效率证明，也不冒称其完整MRM组合已被Books覆盖。

19572实际§5、§6.1–6.7/Tables2–4/§7：小model因执行更久可使总tokens增加；globalpool来自同benchmark多轮演化，w/o intra消融还使用final globalpool，不能当完全相同历史曝光的factorial证明。每轮约4天、retrieval/规则提炼/更新、并行batch带来的经验滞后与运行成本均计费；TopK与N更大不单调更优。其typed observation-filter artifact是可复用局部机制，complaint不证明silent omission可见、Retention不认证heldout稳定；拟2+1+2=5标准完成，仅报告该受限工作点。实际Ch77读时构造/原始回读与Ch31强度proxy/噪声论点比较后，不以主题相似冒称完整覆盖或为少改书删除候选。

## A9 当前机械检查与可恢复边界

原52候选整行实际比对全部保留；原§4连续20179字符实际逐字存在。四主题查询总308槽/跨query263身份只是导航，非题摘全文分母。README已合并14行来源差额、20329自然日资格解释与Seed错身份纠正，原旧09点/§4不改。使用工具现有`冻结候选日期`字段指向本日baseline后，当前进行中V3接口检查通过（首次51旧时间范围告警系缺显式基线引用，未改旧日期），42窗口测试通过，限定README/SUP/三本人Books diff-check通过；这些不代语义/DAY/FINAL。

当前本日3真实整合/POST与本人注行政读回完成，root下一有限Source/PRE普通推进；尚无新lease。已有并发index A/AM保持，本人未stage/commit/push；新DATE_REST与CURRENT_SIGNAL未暂存。准备层不算actual审完，不将冻结原层或各单篇通过冒充日级完成。

后续差额：Privacy/GAAP必要PDF与Ch72实际owner/逐字PRE经root actual通过，Privacy维持2+1+2=5/GAAP维持6，保护相关深入不按安全标签加分。按两窄lease写四正文段及两本人notes后，root实际43–68完整机制/两侧grammar、trajectory、posterior、最小披露与本人3414/3416 POST通过，lease释放，作者只行政同步并actual读回。本日现5真实整合。

18603 root实际必要Methods/Results/Discussion及Ch13完整插位/Ch12、14交接，A7两PRE通过但未授写锁：改正确HTML锚`#Sx4.SSx2`。作者再定点官方OAI，`SUP_DATE_18603_20261015.raw.xml` header Apr22、仅v1、原submitted Apr9、ID18603，配合原公告/ID邻界与Apr22 DataCite层作日级旁证；等待root date/lease，不由DOI单证写书。报告已纳17准入工作候选（原52不变）及逐项必要证据，19533仍准入待核不计确定分母。新增7拟I仍普通待审/实际写入，故当前接口检查有对应7条“整合须深入完成”告警，非完成态通过；旧行冻结/日期兼容及42测试有效，不用改标签逃避。

root随后已actual完整11条v1日期投影与18603官方OAI，Apr22有限组合资格通过，非Updated/OAI单证。DTA已获Ch13指定lease，作者实际两段228/230及本人349保存、全局部邻接顺读与限定diffcheck通过，待root实际POST，尚不计第6真实整合。19544 root实际§3全、§4.1/4.3–4.6/T1–8，5分标准Source/Only通过：同GPT5.2 list/pointwise不是独立gold，修复引proprietary/refanswer、固定chosen/parser批评未独立复现、MMRLHF反退与全部制备/NPUs成本保留；无需Books写。报告只同步该行标准完成及受限Only，未授DAY。

### 最新有效层（覆盖上方阶段时点）

- DTA root实际Ch13 222–244完整原mask/新两段/原局部混合及本人349 POST通过；窄lease释放，作者已行政同步并actual读回。本日现**6真实整合**（19011/19503/19654/Privacy/GAAP/18603），不是7拟PRE。
- 19724 root已actual§3全/§4条件及跨norm句、§5.3 Lemma5.5–5.6/§6配置反侧/G.4.2 Eq102后推导，确认两打印桥错误，维持5深入、中心争议终态、Books0；不否定L2结果可修可能/其他实验，admin note仅说明。报告已同步该行争议与精确重开条件。
- 19522 root实际IV-A/B与V-A–D/TablesII–III，确认APF softcost/goal.5m fade0、.25→.10/profile/五示教/固定dummy，风险最小门后具体EX通过；未形成独立hard envelope或可信映射，不将局部硬件观察抹成全部模拟，不追无影响日期/附件。
- 18847安全负侧有限重核已交root。作者额外只读§4.1–4.2/T1、§6.1/7：20annotators/40formative、230人1150pairs/150double κ=.15，rubric评分与选择同人，moderation是偏好相关；50BackBench评价仍humanA/B/BT，无独立restoredstate/safety分母。撤回“没atomic guarantee因此EX”的过强门槛措辞，待root判断这组具体数据是否改长期恢复选择；不作新发现扩池或预记准入。

LiveVLN root已actual III–IV/Alg1/Eq4–9/TablesI–III/Discussion及Ch26完整插位/Ch25、27交接，确认已承诺g/可修订r、EMA guard与validated one-step backup否则STOP，保实机固定2actions、40runs/平均jitter和模拟反退/频率混杂；6分因长期接口缺口深入通过。A7两PRE获lease后作者已写Ch26 198/200+本人1804并顺读完整192–209邻接/本注，限定diffcheck通过，等待root actual POST，不预记第7实际整合。

仅恢复同一原有下载URL `https://arxiv.org/list/cs.CL/2026-04?skip=600&show=500`的尾18536B，`SUP_LIST_CL_TARGET`现826978B/完整HTML/500条，机械ID没有18585–19748目标带；月页非单调，不能从这页0推出全月0，不扩新AB/全文队列。另一3331384B整月页仍只收到1275981B，作为来源限制保持；前两partial是此前时点，不把target现完整冒充整个分类已覆盖。

MMControl19679 root已actual§3全MMCU/dualbypass/γ/两stage及§4必要配置/Tables1–2/定性sweep，5标准/Only通过。冻结backbone与zero-out init不授有限γ因果完全解耦/所有prior无损；shared main joint仍耦合。30K/4H200/7200step/lr1e-5/B2acc2/12h、200audio+200depth、GTaudio baselines任务不同、motion/syncD反退保留；完整runtime/CI/SLO未披露，不补造。通用control接口不新写、不冒称整套AV配方已有，报告已同步该行及必要段，非DAY。

TACO19572 root已actual§4–5全、§6.1–6.7/Tables2–4/预算反侧，5标准/Only通过。Typedrule/critical留原/complaint抑制replacement与confidenceusage写回属于受限artifact，不授权nocomplaint无silentomission、Retention为heldout truth或staticablation同曝光；small<40B总tokens可增、CompileBench75=75。N4一round4天/规则选择生成/重放与全费均保，未把no-weight叫无更新/无成本。日期前层有效，报告同步行及必要段，无Books写，不授DAY。

LiveVLN root actual新198/200与完整邻接/本人1804 POST通过、lease释放，作者已只行政同步并actual读回，本日**7真实I**。MWM root实际§3全/§4.1–4.3/T1–4/必要A1与Ch25完整插位/Ch24、26交接，5分长期gap深入通过；纠正A7与README原Stage2 flow措辞为Eq8 scorematching/noise扩散、codec冻结限定第二阶段，不借Stage1 FM回填。授指定lease后作者已写Ch25 323/325与本人1504、完整314–330邻接/本注顺读、限定diffcheck0；待root actual POST，不计第8真实I。

随后root actual MWM完整Ch25 314–330原表示预测/新323325/LeWAM与连续表示分支及本人1504 POST通过、限定diffcheck0，修正两词在正文，lease释放。作者仅行政同步本人note并actual读回，报告该行已同步实际POST；本日现**8真实I＋3Only＋1D＝12/17有效处置**。剩已准入普通5为UniT/CityRAG/AnyRecon/20329四拟I与Seed Only；另19533准入/18847风险最小门不偷计正式分母，未DAY。

Seed3D2 root实际正确官方PDF pp4–7/9–14的必要机制、训练推理、用户研究及限制，6标准/Only通过。VecSet locality/sparseSDF、coarse重编码/voxelprior两stage、directalbedoMR共享MoE/VLM SFT保有限披露，细粒度算法/模块控制未披露；60raters/每比较15票/200+prompts是组合偏好，CFG+step蒸馏/remesh15s不授完整E2E/SLO，simulation-ready/URDF/IsaacSim不授真实物理。无新Books，原21443错误身份不继续当有效材料；报告已同步标准完成/Only与反侧。本日现**8I＋4Only＋1D＝13/17**，剩四拟I普通及19533/18847最小门，不授DAY。

### A10 最新有限层：UniT/CityRAG与最终两门

压缩恢复重读实际AGENTS、当前研究/Report合同、Prompt、来源说明/每日组/arxiv主题、ROADMAP及LS最新111路由，仅接本日停点；不继承其他日队列。UniT19734 root实际§3–4/§5.1–5.2全及5.3–5.4/Conclusion必要反侧，6分长期gap深入通过，VLA fusioncode辅助target与实际flowhead读sharedVLM、WM continuousprequantbranch双consumer保留；24×50sim/24Kvs2.4K及27,419额外human/adapter/robot再训、FVD反退不授physicalequivalence或全零数据。Ch26指定两段148/150及本人1808按lease保存，作者全局部顺读/diffcheck0；root实际140–159旧codec→新两段→Privileged3D及本人注POST通过、lease释放，作者只行政同步并actual读回。本日现9真实I。

CityRAG19741 root实际§3全/§4.1–4.2正式人口/Table1/Discussion，6分必要Source及gap深入通过；ECEF/≤5m异时paired、context61–81/target73、firstimage瞬态与geo稳定context、32A100一周20K、固定prompt/新caption响应丢失与正式100短轨迹/20user/staticmask边界保留。Root实际Ch25 542–570 provenance/generatedhistory/LiveWorld与Ch24/26交接及A7逐字PRE通过，授provenance后/generatedhistory前两段+本人注。作者已写554/556、本人1508，实际549–571完整邻接与本注顺读、限定diffcheck0；待root actualPOST，不预计第10真实I。

19533 root实际完整v1AB及pp3–5/7/9–11必要任务/labels/协议/T5/限制，准入2+1+2=5；开放SQL evidence-discovery的observed/submitted分母有具体评价增量，不因security词硬收，也不因仅新benchmark硬排。Normalizedmax=1却表内最高.61与正文绝对50%bar/5of13不能互用，中心争议终态/Books0通过；50×10非绝对500events、Sigma+LLMenrichment非全真oracle、N10vs26/98一次run及generatorproprietary保留。须原normalization/labels/分母修正才定点重开，不用v3更新榜替v1勘误。日期已在root实际11条组合通过层，报告纳确定第18家族。

18847 root完整AB+§4.1–4.2/Table1/§6.1/7风险最小门实际通过具体EX：同人rubric与A/B topic偏好关联及同类RM rerank主要为偏好数据/成熟选择配方，未给改变当前恢复执行或证据选择的具体新成立条件/反证；不是因缺atomic guarantee、无objective safety或安全词决定EX。40formative/1150pairs230人/κ.15、50BackBench humanBT有限偏好增益留raw，不否其学术价值，不扩全附件/不追不影响处置日期。当前18候选＝9I＋4Only＋2D已有效15项，CityRAG待POST/AnyRecon与20329具体Books层普通；未授DAY。

### A11 最终待DAY态：18必要层与12真实POST有效

CityRAG root实际Ch25 549–566新554/556及完整provenance/generatedhistory/LiveWorld、本注1508 POST通过，lease释放，作者已只行政同步并actual读回。AnyRecon root实际§3–5/Eq2/T1–3/必要配置限制，6分Source与gap深入、Ch25 520–542原01001→ObjectAddress及A7逐字PRE通过；Google20329 root实际未变原V3_APR02_20329_INDEPENDENT必要独核与exactv1§2、Ch23 349–369原nativepixel→连续表示及A7两段PRE通过，6分Source/owner差额有效，仅按官方Apr22解除本补窗日级hold，不授旧小时资格或47.8%edit等效优势。

授最后两窄lease后作者已保存Any Ch25 528/530与本人1512、Google Ch23 361/363与本人1658，实际完整邻接/本人注读回、限定diffcheck0。Root actualPOST两项通过：完整Ch25 523–546/本人1512与Ch23 351–371/本人1658，PRE一致、限制近机制、旧段无删，lease全释放；作者只行政同步两本人注并actual读回。现**12真实I（7唯一owner/24正文段）＋4Only＋2D＝18新增**，合原52为70＝29I/5NC/24Only/12D。必要Source、具体Books与写入普通待办0，尚不授DAY/完成态FINAL。

Root否侧三普通样本19565/19656/19716完整v1AB actual：feature统计+logreg及任务依赖head、缺premise clarify/pause奖励、CCA+steering局部workpoint，没有可定位的新成立条件/设计反证；不以‘没普遍保证’作准入门槛。合首批2/第二批5/风险2/普通3＝本轮16具名EX中实际12，另19034/19064/19231/19728未冒称独立审；七旧具名负侧只复用有效层。README六部分已合最终待DAY态，来源局限/自然日合证/原冻结/当前普通0与独立实际范围自包含，状态仍进行中/复核未通过；待作者最终自检后交root实际DAY，不预写通过。

作者最终待DAY态自检：V3接口一致性通过，42窗口测试通过；70唯一候选/52原整行逐字保留、原小时窗口及连续原§4正文不变，135本地引用/48路径零missing。七Books family正文marker/独立POST与本人注已逐项绑定，未核代码/复现。README/SUP与七目标Books限定unstaged/cached检查0（对Ch25路径单独再次校正核），不检查或改动并发index。完整六部分已交root actualDAY，尚未保存完成态或宣告FINAL。

### A12 root实际完整六部分DAY通过，完成态保存

非报告/新增正文作者root实际DAY通过：原52及连续旧§4按未变有效层复用，新18逐条§3/§4全读；14源/主题查询停止/日级资格合证与中央争议隔离、12实际POST/4Only/2D、否侧12/16范围均与实际核验相符。Root独立复跑V3/42测试、52旧整行/窗口/连续原§4冻结、135refs48paths零missing及README/SUP限定cached/unstaged差异检查通过；原正文trim口径差异不影响连续逐字不变。允许作者仅行政同步完成字段/检查时间与§1/5/6，不另起Source/发现或第三审。

作者已保存22:51:26+08完成态及复核通过，其他研究/来源/Books正文不动；普通0、全部窄锁释放。当前只待root对已保存完成态做最小actualFINAL回读，不预记该层已发生；不stage/commit/push，不写LS/index。

随后root实际最小FINAL通过：保存态完成/22:51:26、§1/5/6与A12一致，V3及限定cached/unstaged检查再次通过，无新增研究差额；Apr23日级正式接纳，原52冻结保护有效，普通0、窄锁与作者ownership全释放。作者仅同步README三处待FINAL为已发生通过，并实际读回，不需第三审；本日结束，不接其他日/LS/index，不stage/commit/push。
