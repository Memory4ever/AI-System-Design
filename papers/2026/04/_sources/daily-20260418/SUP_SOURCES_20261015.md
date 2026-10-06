# 2026-04-18 唯一来源补查记录

## A1 范围与恢复

- 只补北京时间2026-04-17完整自然日；原09:00→09:00窗口、原0候选及连续原§4保留，运行前基线见[冻结稿](baseline-before-supplement-20261015.md)。不启动Live/Weekly/2025或其他日期。
- 旧V3_REVIEW_CHECKPOINT的原件身份/版本/采用命题未变部分按研究合同§7复用，但旧完成标签不替代本轮验收。原arXiv零常规公告判断不适用于新增自然日：Apr17北京时间含美国EDT Thu Apr16晚公告。
- 最新学习路由106/279；Apr18未验收。作者supp_apr18_author；独立准入、Source、owner、PRE/POST、DAY/FINAL由root。作者不自行计入完成、不写共享State/索引；Books改写前逐段申请窄lease。
- 首批完整题摘及代表排除项即发root校准；潜在贡献、必要Source prepared、独核通过、owner实际落实分开。不将宽月目录变为全量逐项队列。
- 本轮未stage/commit/push；保护运行前与并发全部修改。技能daily-research-closure用于窗口/证据复用/验收分层；当前合同优先。

## A2 来源差额待办

- 机构14源旧停点先核与Apr17自然日是否仍成立；没有受影响信号则复用有效具体层。五处历史目录缺口不作零命中或Coverage通过。
- arXiv对本窗公开日期的模型、系统、多模态、Agent主题查询与官方相关标题导航，逐项只读可能有贡献的完整题摘；必要公开日期核日不追秒，不用90天catchup。
- 尚无本轮候选或深审完成。普通研究工作尚待，不称blocked。

## A3 首批完整题摘校准请求（准入prepared，尚非Source完成）

原件：[model主题](SUP_theme_model_20261015.raw.xml)、[systems主题](SUP_theme_systems_20261015.raw.xml)、[multi主题](SUP_theme_multi_20261015.raw.xml)、[agents主题](SUP_theme_agents_20261015.raw.xml)。四查询都是 submittedDate `[202604151800 TO 202604161800]` 身份发现线索，返回240/21/40/96，均start0/max250且total与返回数相等；不把Submitted字段当公开日，当前版本题摘不可自动代入v1。本轮完整读以下14题摘，拟处理10、代表排除2、负面评价边界2待校准。其余命中只标题导航，不自动变逐项队列。

| 身份 | 原约束→实际增量→待核设计选择 | 初步处置 |
| --- | --- | --- |
| 2604.14825v1 Nautilus | 高层代数改写与tile优化交互难共同搜索→successive lowering及保留规则结构的auto-scheduler→自动发现attention fusion的表达/搜索条件 | 拟入选，2+2+3=7，Ch49潜在owner |
| 2604.14561v1 CoCoDiff | Ulysses DiT频繁all-to-all受依赖/跨节点带宽约束→V先算通信重叠与拓扑分相/步间冗余→不可将序列并行通信视为全同等可重叠 | 拟入选，2+2+3=7；API当前v2，必须读v1 |
| 2604.15379v1 Fleet | flat GPU任务层次不表达chiplet locality→Chiplet-task及per-chiplet persistent scheduler→decode权重复用需要对齐L2共享scope | 拟入选，2+2+3=7 |
| 2604.14993v1 chain jobs | 模型block放置与cache容量不能分开优化→链结构large-memory server-chain composition及保证算法→PP serving分配目标需纳入驻留容量 | 拟入选，2+2+3=7 |
| 2604.15186v1 Scepsy | 动态workflow端到端时长难预测→各LLM执行时间份额较稳构造aggregate pipeline→联合GPU share/TP/replicas优于逐模型独优 | 拟入选，2+2+3=7；API当前v3，必须读v1 |
| 2604.15272v1 Prism | tensor superoptimization枚举昂贵→sGraph符号族、语义等价与硬件界剪枝→搜索表示与实例auto-tune分层 | 拟入选，2+2+3=7 |
| 2604.14419v1 Equifinality | 更复杂MoE路由拓扑常被认作PPL来源→受控小模型多seed等价检验与容量对齐缩小router优势→路由复杂度与容量/收敛须分开归因 | 拟入选，3+1+3=7；不因小模型/负结果排除 |
| 2604.14434v1 Geometric Routing | 路由质量近似不代表expert不可解释→centroid/低秩expert可读与干预，linear routing也可steer→拓扑质量和expert因果控制分开 | 拟入选，2+1+2=5；与14419不同实际命题，不借成熟原则计分 |
| 2604.14433v1 Zero-Ablation | 寄存器置零损失常归因图像特定内容不可缺→mean/noise/cross-image替换保性能且多任务/规模复核→干预分布漂移不等于内容因果必需 | 拟入选，3+1+3=7；重要设计反证 |
| 2604.15409v1 FP16 KV | 数学cache等价被误作执行数值等价→cache on/off FP16 greedy全序列分歧与FP32反侧→采用命题只能是数值执行路径比较，摘要sole causal/fundamental需挑战 | 拟入选，3+2+3=8；不是直接接受全称保证 |
| 2604.14585v1 Prompt coin flip | compound prompt联合优化假定交互及headroom→多方法多repeat诊断提示词交互/输出结构→潜在负结果边界 | 待精确v1摘要校准；当前API v2的72run等不可直接算v1 |
| 2604.14437v1 Test shortcuts | 公开benchmark可能混淆记忆/推理→LevelDB与HANA mutation/反馈对比→只可作特定测试生成评价盲区，proprietary不自动证明未训练 | 待root准入校准，拟标准5，不采泛化缺乏真正推理 |
| 2604.14866v1 MetaDent | 牙科标注/benchmark与现有VLM领域迁移→数据及任务评测，完整摘要未提出改变基础模型/系统设计的独立机制 | 排除：临床应用数据与指标，不因VLM可映射Ch23/66准入 |
| 2604.15377v1 M3R | 气象雷达/PWS融合提升局部降水→领域cross-attention预测架构 | 排除：AI for Science暂缓，不从多模态/数据节点绕入 |

公开日期、轻量撤回/纠错标记、同版本跨日复用关系尚待本项精确abs核；没确认日期的不先计确定候选。未采用搜索索引结果作为性能证据。

## R1 root 首批实际准入校准（2026-10-15，作者串行记入）

root实际读完A3的12 exact-v1 abs＋2 EX原XML完整题摘。Fleet15379/Prism15272/FP16KV15409有具体机制/数值反侧潜力，Scepsy15186有聚合pipeline调度潜力但尚日门；不授Source或日期通过。14437只读决定准入的最小core：若只是非匹配领域对比和mutation指标应用则具体EX停止，不能仅因两数据库/proprietary标签声称无训练污染或LLM无推理。14866/15377两EX具体理由通过。

root逐项实际读Apr17同v1完整候选行与各自§4，14825/14561/14993/14419/14434/14433/14585七项有效Source/具体Books处置可复用去重；15186是日期hold，不是有效审阅。作者早先消息的“8有效”已纠正为七有效＋一datehold。A3对应七项初评分仅发现阶段prepared，撤销新增评分/候选意图，正式本日不重列、不重读有效core。

12 exact-v1 abs均真实取得，作者实际读回：14585 v1只是Claude Haiku，不倒灌v2 Haiku4.5/新增mechanistic account；Scepsy v1摘要声称up to2.4×/27×，而APIv3为2.5×/1.0–3.3×，后续不得混用。abs无显式withdrawn/erratum/corrigendum信号。首次公开日仍待必要原始依据，Submitted不是证明。

## A4 第二小批题摘准入prepared

作者完整读四XML下列22项摘要；当前API后版只用于潜力发现，拟入选仍精确v1核对，不倒灌。

| 身份 | 具体贡献门与初步处置 |
| --- | --- |
| 14629 Switch-KD | 分模态KD不直接对齐融合后概率→student visual输出切入teacher语言路径并双向logits差→跨模态teacher/student对齐方式；拟2+1+2=5 |
| 15280 emotion | DFER长尾与微表情时间尺度同时暴露VLM频率/稀采样约束，提出平衡采样与帧间文本摘要probe；拟负面证据边界5，必须v1确认，不采全部VLM无时间表示 |
| 15309 MM-WebAgent | 摘要只有hierarchical planning/iterative reflection整合AIGC以提高网页一致性，未指出区别于成熟规划反思的新执行机制/成立条件；EX，不以新网页benchmark准入 |
| 15188 VisPCO | 固定视觉pruning配置未必在Pareto边界→连续松弛/STE与augmented Lagrangian预算约束配置搜索→比较token压缩时须联合层间预算；拟2+1+2=5 |
| 14951 RaTA | 闭集toolID→多模态输入生成task表示并检索标准tool描述/DPO；拟5，核是否只成熟retrieval组合或有未见工具受控增量，尚非确定准入 |
| 14399 SpaceMind | Skill/MCP/reasoning三维解耦及失败经验写skill文件；摘要只有集成模块/场景成功率与6组恢复，未说明新执行机制或controlled成立条件；准入含糊只最小core，不默认入选 |
| 14779 AIM | VLM可训练组件规模不对称使global正则忽略小visual projector→按模态敏感度targetedmask→跨模态continual稳定性预算不能按全局平均；拟2+1+2=5 |
| 14902 ADAPT | 指令未显式affordance但环境状态变→显式可操纵前提检查及隐藏约束benchmark→任务成功不能只看指令跟随；拟负面/评价边界5，核是否成熟检查组合 |
| 14520 CoM | no single modality topology普适→动态拓扑重组/learned planner修复topology-sensitive failure→需要把输入组织与证据量分开；拟2+1+2=5，APIv2必须v1 |
| 14967 UniDoc | 静态visual检索忽略细粒度证据→coarse document/image/region分层action与dense reward→检索/裁剪的预算与评价耦合；拟2+2+2=6，APIv2必须v1 |
| 14580 TurboTalk | 极限one-step蒸馏不稳→DMD4step后对抗4→1、progressive timestep/selfcompare→路径/对抗参照与成本分账；拟2+1+2=5，APIv2必须v1 |
| 14605 GIST | 摘要只identity preserving compositor插入已有graphic设计pipeline及judge偏好，不具体新增基础生成机制/成立边界；EX，不以应用质量准入 |
| 15308 RAD2 | 高维trajectory直接稀疏reward不稳→generator/discriminator分工、temporally consistentGRPO/BEVwarp闭环→候选生成与闭环长程评分分离；拟2+2+2=6 |
| 15395 robotics survey | 完整摘要为阶段/分类/数据/挑战目录，未提出修正具体设计判断的独立新证据；EX，不因综述主题贴owner准入 |
| 14648 Seen-to-Scene | outpainting仅生成缺跨帧显式传播→flow completion与reference-guided latent propagation保已知/生未知→生成与观测区域时空一致性边界；拟2+1+2=5 |
| 14552 DEEP-GAP | ResNet18/50/101在T4/L4及精度/batch对比，只给已知硬件配置选择，无新的LLM执行机制/已辨设计反证；EX，不把单数字或GPU名当贡献 |
| 18616 Ave | dataflow tag+SMT可给kernel agent定位约束违反，有机制潜力；ID明显晚且APIv2不可归Apr17，先必要日门，不深审或确定候选 |
| 14411 hypergraph | 有bounded incidence专用GPUpartition算法，但完整摘要没有支撑模型训练/推理/compiler选择的具体关联，只算法类比不足；EX |
| 14700 CRONet | 领域topology optimization神经网片上hardware实现；当前AIforScience暂缓，不从GPU通用owner绕入；EX |
| 15128 SCENIC | 现有NIC高速兼容与programmability冲突→SCU datapath/ARM control与LinuxRDMA/GPU直接访问→collective/data partition卸载边界；拟2+2+2=6 |
| 15388 Verilog | multiagent生成testbench＋高质SFT的工作流，摘要没有可归因新机制或已证复现边界，只少数据匹配指标；EX，非因硬件应用硬排 |
| 14751 FL correlations | 压缩常假定structure/time/spatial相关存在→测量强度后切换压缩mode与deployment相关反侧→压缩收益依赖实测相关；拟2+1+2=5，核是否泛综述或可迁移有效性证据 |

## R2 root Prism/Scepsy 必要Source实际独核（作者串行记入）

root实际独立打开精确v1HTML：Prism §2/3.2–3.4/4 axioms及明确soundness无formalproof/不complete、§5随机tuning/§6实现、§7.1–7.5评价反侧，支持symbolic family→mapping→axiom verification→target profiling的有限机制；不采globally optimal/全数值sound。matmul关联axiom不是FP bitwise保证；部分search总费135>52、152>13，Mirage timeout与配置摊销分开。

Scepsy §3–6/Eq1–2、§7.1–7.5/§9：aggregatepipeline是统计代理不是实际DAG重排，n/p均值代理/吞吐min；跨不同LLM并行被串行化、bimodal与不可忽略tool时间是直接限制，分位latency相加不认证整体tail。16RTXA6000/100GbIB/两NVLink对、两workload/不同vLLM及prefixcache混杂、低load Ayo可更快和search128GPU70s不抹掉。两项必要Source有限机制通过；未读代码或复现，不授日期/owner/PRE。

Fleet15379/FP16KV15409自身v1Updated在Apr20，与SubmittedApr15/16冲突是具体归属警报；root同意不能继承同批推断。不单以Updated直接证明first-publicApr20，必要公开日不能支持Apr17则具名终态日期保留，未授Source深审完成。

## A5 第三批完整题摘，Agent与标题导航差额（准入prepared）

不依旧screening-ledger那种“单领域/局部不改变ownership”模板排除。作者完整读对应四XML摘要；下表精确v1已缓存的逐项身份为`SUP_AB_<编号>v1_20261015.raw.html`。不同后版摘要只作发现，AgentGA v1明确10/16 benchmark runs、74.52 vs54.15及1135 comparisons，不能倒灌v2全16/1680。

| 身份 | 完整题摘后的具体贡献门/处置 |
| --- | --- |
| 14972 SAGER | 用户semanticmemory不等决策策略适应→rich evolution/minimal runtime双表征skill、accepted/unchosen对比→策略与memory收益需分开；拟2+1+2=5，精确v1已读 |
| 14712 SGA-MCTS | 在线tree-search重开销→离线search转delexicalized state-goal-action原子再重绑定→可迁移hint与成功保证分开；拟2+1+2=5，v1已读 |
| 15034 Autogenesis | prompt/tool/env/memory跨资源更新无统一version/lifecycle→resource substrate与propose/assess/commit protocol分层→候选更新与运行态承诺边界；准入含糊仅最小core，不能把成熟version/rollback术语当增量；v1已读 |
| 14386 coalition | n-agent联盟稳定性未有显式偏好假设→hedonic game/epsilon rational条件与CoalT比较→理性/偏好一致性前提需验；拟2+1+2=5，v1已读，不采无条件Nash保证 |
| 14655 AgentGA | 直接改代码搜索vsagent seed/parentarchive重新开独立run→遗传初始化与artifact继承→外循环种子而非代码成为可搜索对象；拟2+1+2=5，v1已读 |
| 14403 unified RAG | 分别存retrieval embedding和reader压缩重复budget→共享检索/压缩latent表示→磁盘/上下文需联合设计；拟2+2+2=6，v1已读 |
| 15267 CoopEval | 同伙伴重复博弈合作不代表变化伙伴可用→合同/mediator/reputation/repetition可控对比与co-player反侧→合作机制边界；拟2+1+2=5，待读v1 |
| 14956 FedGUI | 移动平台FL结果外推跨GUI不可靠→四种异质性拆解，platform/OS主导→GUI联合训练不能仅按device区分；拟1+1+2=4，若v1有实质设计反证必要深入受影响层 |
| 14989 DrRTL | 退化小设计/弱EDA工具混淆优化→工业流程现实设计、group-relative skill提炼→可复用策略须绑目标工具/真实criticalpath；拟2+1+2=5，待v1 |
| 14550 VeriGraphi | 层级RTL代码跨module接口幻觉→spec-anchored graph先验证hierarchy/ports/wiring再渐进生成→代码前结构schema检查；拟2+1+2=5，待v1 |
| 14401 Credo | semantic状态与imperative/prompt规则纠缠→belief/policy declarative DB-backed控制面→是否新增实际一致性/变更语义待最小core，非仅术语即准入；v1已缓存待读 |
| 15306 ShortestPath | 泛化失败混训练data/RL/inference因素→受控spatial与length两轴区分、recursive instability→RL与TTC不能代替覆盖/长程稳定；拟3+1+3=7，待v1 |
| 15153 Kmerge | compression只文本token→连续K embedding聚合＋LoRA reader→检索压缩/编码成本与任务loss分账；拟2+1+2=5，待v1 |
| 14493 ondevice ASR | CPU streaming硬件资源与quality Pareto→受控多架构/mode/quantization+fusion→不可由batch WER代替stream/CPU可行性；拟5潜力，待v1及是否仅数字无机制的最小core |
| 15001 COEVO | strict correctness gate删掉局部错但PPA有用候选→连续correctness/annealedgate＋4D Pareto→中间搜索fitness和最终合法验收分开；拟2+1+2=5，待v1 |
| 14631 StoryCoder | 题干碎片化与reasoning链改写混杂→任务/constraints/examples结构化叙事，coherence/genre反侧→输入表示与推理预算分开；拟5潜力，待v1及最小归因core |
| 14785 MirrorBench | 对外物体评价漏self-centric镜像→tiered镜像关系任务→空间参照/识别能力边界，拟5评价潜力；不采自我意识或AGI结论，待v1 |

明确EX的完整题摘层：14896 Ukrainian仅现有BGE/rephrase/retry组合与检索瓶颈应用，15236 microphysics仅概念methodology无具体机制/证据，15121 VSA streaming未建立foundation学习/agent系统具体关系（不能借memory类比），14691 CAMO将LLM社会模拟用于因果发现属当前科学研究应用，不从Agent节点绕入；14687 checkers MCTS/minimax解释为LLM生成解释的成熟流程、无模型机制/LLM规划改变；14455 AIBuildAI只有manager/designer/coder/tuner角色组合及排行榜，14661 AIPC只有skills/helper/stagevalidation既有部署流程（不凭agent化即准入），14984 governance访谈/card建议，14317 reverseengineering综述挑战，无新可判定设计证据；15044 CoGrid/MUG社会/心理模拟实验工具不是foundation系统机制，15233 BlueDIL两交互demo只统一多源queryplan已有设计，没有新增执行/证据边界；14858 ATBench只是按新运行域定制风险taxonomy，不以增加覆盖标签作贡献；14518 MindDR三agent＋SFT/SearchRL/ReportRL/preference流程及指标未指新机制/具体有效性条件，14593 jealousy用现有RepE/心理构念作特定行为干预，未独立改变表示机制解释。以上不是领域词硬排；若root发现具体新机制或反证，只开对应集合。

额外高ID具名潜力（未准入/未深审）：16529 rolloutsummary TTC、15415 harmfulskills、16521累计PII、15384 LinuxArena、15408 dispatch raggedattention、15414 policyarchive。API Submitted落早日但ID晚，必须必要first-public日门，不把未知记零命中，不按Submitted放入本窗。

### 有界标题导航差额

本地四类官方月目录`arxiv-owner-replay-20260903/monthly-membership/{cs.CL,cs.AI,cs.LG,cs.DC}.html*`只浏览14300～15311一段标题补检，非全月逐项AB队列。直接查四query未命中标题发现下列精确v1摘要，作者已完整读：

| 身份 | 实际增量与初步门 |
| --- | --- |
| 14414 autocorrelation | pooled turn-level独立性假设→同对话依赖校正/holdout replicability反侧→对话统计有效样本单位；拟3+1+3=7，5用户/202对话局限不可丢 |
| 14790 diffusion crossover | 高维genotype crossover不保语义→noise序列逐步Slerp/指定step区间→扩散轨迹作为recombination空间；拟2+1+2=5，不采LPIPS即真实语义保证 |
| 14932 WavAlign | shared speech参数稀疏preference更新可能损acoustic→只semantic preference/explicit acoustic anchor按rollout调mix→声学/语义RLcredit边界；拟2+2+2=6 |
| 15224 evaluation faking | judge评语只受内容假定→同1520response固定，仅system后果句变化导致leniency且CoT不显式承认→CoT无信号不证judge无context bias；拟3+1+3=7，不推意图欺骗 |
| 15294 viewpoint | 探针能decode视角不等绑定对应observation→headwise干预/fine-tune暴露binding失败→表示可读与生成使用分开；拟2+1+2=5 |
| 15302 JudgeReliability | aggregatecycle率遮per-document坏样本→transitivity诊断＋splitconformal score集合→marginalcoverage不等individual保证；拟2+1+2=5，旧9点hold不适用当前整日 |
| 14930 IEcache | 摘要只query-driven IE/cache-aware reasoning架构和指标，需查同v1有效记录先；不把memory类比准入 |
| 14531 TRACER | 生产logs surrogate＋agreement paritygate→teacher一致性与groundtruth quality分开；先查同v1有效记录去重 |
| 15180 AdaSplash2 | entmax normalizer迭代贵→onchip histogram初始化τ到1–2iter及zero-block skip→sparsity生成成本与可兑现训练成本；拟2+2+2=6，旧hourhold不继承 |

作者最小core14437 §2/§3.2/§4确认有编译反馈后删assertion/空testbody的迭代局部失效路径，而非仅两个database换域指标；提请root有限2+1+2=5仅报告准入，不采proprietary无污染/LLM无推理。Prism OAI官方GetRecord实际single-v1 datestamp Apr17，结合精确身份/本地Apr17注册v1日值/正常公告批界只核日；Scepsy后版OAI本身不代表首次公开，但原Apr17 v1日值和同批界无新异常，不因01:xx跨旧小时窗重造障碍。

## R3 root 第二批校准与14437贡献门关闭

root已实际读A4全部22完整题摘，潜力/含糊/7EX具体边界通过；15388不是因HDL类别排，而是未有新机制/有效边界。root实读14437v1 §2/3.2/Discussion：全部experiment/figures引用同作者TechnicalReport1/2026，本篇为再阐释，未新增可区分反证或重分析。故A5作者暂拟5修正为具体pre-denom EX，不评分/候选，不称已读先稿/已审同事件重复。未核先稿本体、不再追主prior全文。该body抬头Aug24与AprSubmitted也不一致，但贡献门已关闭，不为不影响处置的日期再建请求。

作者定点查14932/14414/14531/14403四相同v1实际行与对应完整§4，可复用既有Source/Books处置：14932 semantic-channel preference/acousticanchor已整合Ch31；14414 conversation独立unit已有覆盖Ch66；14531 teacheragreement局部路由Only；14403 Eret→Ecomp共同持久化表示已整合Ch76。提请root只核此四身份复用，不继承月度完成标签、不新增评分/Source或Books写入。14930尚未找到有效本日候选行，只按含糊IEcache门继续。

## A6 首两项作者必要Source与owner差额prepared

作者已加载ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE与最新相关LEARNING_STATE，读Ch49开篇/typed equality、PersistentEgraph、FastFusiest/TCM、Nautilus相邻论证及Ch48/50交接，读Ch56多模型/Workflow/TaskDAG对应正文及Ch55/57交接；不将章末trace当owner正文。

15272 Prism作者已实际读v1 §2、§3.2–3.4、§4–6及§7.1–7.6必要层，与R2独核一致。具体差额不是再说typedstate/数值回归，而是graph结构→Boolean mapping→integer parallelization的分级提交；d=1 expressioncheck只是必要条件筛选，后续mapping/egraph及targetprofiling不能省。A100半精度5workload×2配置、1000次均值非服务SLO；70axiom人工核/随机test无formal soundness/complete，结构共享和实机配置成本分账。潜在唯一owner Ch49。

15186 Scepsy作者实际读本地同v1正文§3–6/Eq1–2、§7.1–7.5/§9，与R2一致。具体差额是trace-derived n/p将逐LLM load/performance profile转换workflow统计代理，联合fraction/TP/replica再placement，而不是DAG重排；同LLM fanout平均并行不处理跨LLM criticalpath、bimodal/tool成本。Ch56已有TaskDAG/prefix/逐setuptraffic profile，但尚无这条不解析任意控制流的aggregate分配分支；潜在唯一owner Ch56，非Ch81Agent执行语义。

### PRE请求：Prism Ch49两段逐字最小稿（尚未写Books）

位置：`books/part-05-inference-system/49-tensorrt-llm.md`约34行，TCM段末“并非同一条最优性证明。”之后、“在跨阶段的typed state之外”之前；只新增下列两段和本人Review note，不碰其他作者段。

> 当同一算子结构的候选只因并行映射和 tile 大小不同而被反复生成、验证时，可以先让一张分层图表示整个候选族：用布尔变量描述 tensor 维度如何映射到 grid/loop，用整数变量保留并行粒度，先搜索结构，再提交映射，最后在目标 GPU 上调参。一个便宜的必要条件是在所有并行维度都取1时检查表达式是否仍有可能成为输出子式；通过只表示尚未被排除，不代替后续映射约束与等价检查。这样把“验证哪一类计算”和“测量哪一个执行配置”分开，而不是让 profile 替代正确性证明。
>
> [Prism v1](https://arxiv.org/html/2604.15272v1)用这条分支减少重复搜索，但其约70条公理依靠人工审阅和随机等价测试，没有完整 soundness 或 completeness 证明，矩阵代数改写也不自动给出浮点 bitwise 等价。A100半精度、五种局部LLM负载的结果还需分别计入构图、映射验证、编译和实机 profiling；部分配置的总优化时间反而从13秒升至约152秒，不能把候选族复用写成所有配置更快或完整服务SLO收益。预算难以摊销、目标shape超出规则或数值回归时，保留既有固定图、已验证kernel与局部 autotune。<!-- source-family:SF-2026-ARXIV-2604-15272 -->

本人Review note逐字：`- SF-2026-ARXIV-2604-15272 — Daily2026-04-18补Apr17；[Prism exact-v1](https://arxiv.org/html/2604.15272v1) §2–7必要机制/约70axiom与无formal soundness/complete、A100 FP16五workload/两配置及总优化反侧。仅结构/mapping/parallelization分级提交与target profiling分账，不采全数值sound或全局最优；作者必要Source/owner已读，root必要Source R2通过，待逐字PRE/实际POST；未核代码或复现。`

### PRE请求：Scepsy Ch56两段逐字最小稿（尚未写Books）

位置：`books/part-05-inference-system/56-inference-scheduling.md`约1494行，`## Agent Serving 把调度单位从单次 Query 扩展为 Conversation 与 Task DAG`之后、`### Ready 只表示可释放`之前。加小标题“### 动态 Workflow 可以先按模型需求份额分配，但统计 Pipeline 不是执行图”，下列两段及本人末注。

> 为任意分支、循环和 fan-out 精确重建执行图，在控制流稳定时能保留 critical path；当框架多样、单次轨迹差异很大时，可先用实际 traces 估计每个模型的平均调用次数 n 和同模型平均并行度 p，再重放请求取得不同 TP/负载的性能曲线。工作流到达率 λ 给模型带来约 λn 的调用负载，其延迟贡献以 n/p 缩放，吞吐由各模型容量除以 n 后的最小值约束。这个 aggregate pipeline 只是分配预测器，不会把实际 DAG 改成串行图；控制器据此共同搜索 GPU fraction、TP 与 replica count，再由拓扑感知 placement 判断配置能否放置。
>
> 这种压缩换来更小的配置搜索，却丢失跨不同模型的并行 critical path；同一模型的双峰调用人口和不可忽略的 tool time 也会使代理失准，分位延迟直接相加更不是整体 tail 保证。[Scepsy v1](https://arxiv.org/html/2604.15186v1)的16张RTX A6000、100Gb InfiniBand及两类工作流只支持受测范围，baseline的prefix cache/engine版本差异、低负载Ayo略优与128GPU搜索约70秒均限制 headline 的解释。Tracing、逐TP profiling、搜索、放置与MPS共驻干扰需要另计，实际completion/queue/KV仍由runtime拥有；统计失配时保留逐阶段trace、显式tool预算和已测保守allocation，而不向任意Agent程序承诺吞吐或SLO。<!-- source-family:SF-2026-ARXIV-2604-15186 -->

本人Review note逐字：`- SF-2026-ARXIV-2604-15186 — Daily2026-04-18补Apr17；[Scepsy exact-v1](https://arxiv.org/html/2604.15186v1) §3–6/Eq1–2、§7.1–7.5/§9。仅trace-derived n/p统计需求→fraction/TP/replica共同分配与拓扑放置，不改实际DAG/不授tail保证；跨LLM并行、bimodal/tool限制、16RTXA6000/100GbIB、baselineengine/prefix差异与低load/search反侧保留。root必要Source R2通过，待逐字PRE/实际POST；未核代码或复现。`

## A7 第四批模型/评价完整v1题摘prepared及日期定点层

作者已完整读A5后12个缓存v1摘要，和前14个合并共26个v1摘要完成，不将其视为Source完成。另新增21个`SUP_AB_<ID>v1_20261015.raw.html`作者已逐项实读；与原API当前版本对照不倒灌后版。

| 身份 | 原约束→新增机制或边界→待核选择；初步贡献门 |
| --- | --- |
| 14973 perturbrobustness | embedding编辑操作变化未按任务影响解释→带五条数学性质的3metric＋六foundation9扰动与downstream对照→embedding稳定度和任务鲁棒非同一指标；拟2+1+2=5 |
| 14602 CausalDetox | correlation找toxichead不足→PNS选择/动态inputsteer＋微调两路径→干预选择目标与稳健生成分开；拟2+1+2=5，necessity/sufficiency与永久unlearn强称须直接挑战 |
| 14463 steering | activation强度无语义标尺且有fluency限制→semanticcalibration/fluencyconstrained sweep推翻prompt优于inject的受限对照→比较控制量与目标validity；拟2+1+2=5，不采真实人格 |
| 14314 DharmaOCR | quality平均遮循环生成对资源尾部影响→degenerate rejectDPO＋fidelity/结构/degeneration/unitcost联合评价→OCR结构与停止failure同验；拟2+2+2=6，不因领域OCR排 |
| 14641 ASCII | spatial答错可由构图或读图失败→可验证text→ASCII与QA分离训练，read/write不对称及无ASCII测试迁移→外显表示建构训练和推理使用分开；拟2+1+2=5 |
| 14477 ViCD | vision neuron概念读出不解释路由→edgegraph discovery与typographic干预→可读feature不等计算路径；拟2+1+2=5 |
| 15259 loopstable | 多迭代不自动外推→fixedpoint reachability/inputdependence/geometry及recall/outerNorm→loop架构稳定条件；拟3+1+3=7，countable/guarantee需核假设 |
| 15237 StreamCacheVGGT | singlelayer score噪声与binaryeviction丢几何→crosslayer salience＋moderatekeymerge/anchors三层压缩→cache budget不等geometry足够；拟2+2+2=6，不授常数全费保证 |
| 15244 SpecGuard | tokenexactSD不解决stepcorrectness→internalattention/logprob两信号step候选选择/target重算→有损verification合同vs经典targetdistribution分开；拟2+2+2=6，必须核因果/质量条件 |
| 14646 UEC | prompt难度不同但统一entropy探索易collapse→困难prompt更多explore＋独立stabilizer→entropy预算与优化更新分责；拟2+1+2=5 |
| 14870 curvatureprobe | isotropic检测被无关方向稀释→topHessianeigenspace测局部稳定、二次模型k^-2与HVP估计→观察方向/维度而非任意全局generalization；拟2+1+2=5，必要理论假设深入 |
| 14925 dynamicSAE | 固定TopK sparsity损失/解释性折中→dictionary crossattention＋sparsemax自选support→activecounts不是自证monosemantic；拟2+1+2=5 |
| 14302 sketchmultiview | 扭曲sketch不直接给3Dgeometry→cameraawareattentionadapter＋SfM sparsecorrespondenceloss→viewconsistent generation而非外推物理state；拟2+1+2=5 |
| 14525 crossquery | perquery准确不保证case全体可满足→commitment抽取/SAT/counterexample修复＋revisioncost→beliefglobalvalidity与每答truth分开；拟2+1+2=5 |
| 14768 CoTEvol | teacher蒸馏与独立search成本高→trajectoryglobalcrossover/uncertainstepmutation＋fitness→syntheticCoT搜索粒度/额外预算分账；拟2+1+2=5 |
| 14920 dualaxisRM | turntiming proxy和语义质量混同→RM同时输出semantic/timing分数→full-duplex RL评价不同质量轴；拟2+1+2=5，不把RM相关性当已RL改进 |
| 15281 R3D | 3Dpretrainencoder放大policy不稳→aug与BatchNorm缺陷受控诊断＋transformerencoder/diffdecoder→perception scaling与policy稳定数据/归一化分开；拟3+1+3=7 |
| 14724 HAMSA | 2DSSM靠scan映序列复杂→FFT complexkernel/inputfreqgate替代scan→全局频域mixing不等有界causalrecurrentstate；拟2+1+2=5 |
| 14762 OmniGCD | 每datasetGCDfinetune与encoder耦合→synthetictrained latenttransform可跨四模态zero-shot→categorydiscovery与pretrainedrepresentation分离；拟2+1+2=5，remote-sensing只是四模态之一不整体science硬排 |
| 15299 AnimationBench | 完整摘要主要将已有animationprinciples/IP保存变标签＋benchmark，有人类相关但未指具体counterfactual/evaluator失效修正证据；EX，不因新增风格benchmark即准入，提请root校准 |
| 14723 BoundedAutonomy | 已查Apr17实际samev1行及完整§4为Ch78确定性entitybinding/commit分权已有覆盖；复用去重，不新增分数。 |

尚未纳队的明确science/领域应用标题按范围关闭，不强制全AB。14459 filler-gap developmental linguistics完整AB为特定语言习得共享结构/人类样本效率，未新增foundation机制或设计反证，EX；14672 spatialgender taxonomy及特定偏见分布，未改变bias评价机制、所称pipeline trace仍是特定社会领域解释，EX；14668 DOMSteer是UI辅助的成熟DOM改写设计空间/用户实验，不改Agent执行机制或可靠性条件，EX。15114 amortizedOT与14486Tweedie是可能相关一般理论：完整AB尚需最小机制关联校准，不能因无章节名就排，也不能仅能讲到diffusion就自动收。

### 同公开日必要元数据定位（不单独当first-public证明）

对本轮具名60潜力身份只定点提取已有官方注册原件中的自身v1日期，不遍历原月库存作贡献队列。除18616为Apr22且无v1Updated字段外，另59条在Apr17原始文件中自身v1Updated同Apr17；含Prism/Scepsy/AdaSplash/Judge15302旧hourhold。配合官方目标身份、Apr17正常公告批界与无具体矛盾只核日，不追秒、不重造9点门。Fleet/FP16KV另有Apr20自身值警报，仍独立隔离，不与59项混用。当前指向`arxiv-owner-replay-20260903/datacite-created/2026-04-17-page-01.json`和page02；该定位本身不是DataCitecreated=firstpublic规则。

14930 IEcache按精确v1查Apr17 `v3-reopen-notes.md`第509行已有真实III-A/B、IV-C与TableI具体EX：query→schema→extract/LLMmergeprune/按需回读/可选selfcheck为成熟query-conditioned workingmemory组合，Qwen8B无差、Calendar无同类消融、未控额外调用预算。该实际贡献门可复用（非主题覆盖硬排）；不再购core，不评分。

## R4 root Prism/Scepsy date、owner与逐字PRE实际通过并授窄lease

root实际读取两项Apr17原注册精确record/endpoint、Prism单v1 OAI datestampApr17、Scepsy原v1身份和后版OAI边界，结合当前官方身份/正常公告批界，支持Apr17自然日有据归属；不单用created/Submitted/秒截点，不授历史逐篇membership。两项date与A6逐字PRE通过。

root实际读Ch49完整typed/egraph/compatible/TCM两侧，授Prism Ch49 TCM完整反侧后、typed-state有序端口前两段＋本人注窄lease；实际读Ch56 AgentServing/Ready完整邻接，授Scepsy在AgentServing标题下/Ready前小标题＋两段＋本人注。作者只写这两位置，不改并发index；写后仍待真实POST，未授日级完成。

## A8 最小core准入差额与首新Source prepared

作者已实际最小core：Credo14401 §2.1–2.3不是只有DB术语：typed value/confidence＋static/dynamic belief dependencies，policy显式INVALIDATE受影响contextkeys再重跑operator；拟5有限替代机制，demo没有一致性/质量证明。RaTA14951 §3.2–3.3用retrieved groundtruth tool rank选description preferencepair，§4.3 JSONzero41.5<NL43.9、ContrieverfewJSON24<NL25.5，与“始终优”文字冲突；拟5仅结果导向representationcredit，不授unseen工具调用正确。ADAPT14902 §3静态/动态设置固定instruction/goals只注入objectstate，§4暂停原action→恢复precondition→resume，§5.4 privilegedstatesymbolic46.15>ADAPT27.69>6.15；occlusion误判和72.6→210.8s不可省。拟5作为状态/计划正交评价边界，不采所有变化solecausal或0.2s等全费。

SpaceMind14399 §3.2/3.5、4.4最小core显示skillCRUD/LLMreflection＋blacklist/dedupe/scope/parentexistence成熟组合，六组优先选失败并报best-round，无新的执行机制或controlled成立边界；拟具体pre-denomEX，不把blacklist写为原文安全保证。AGP15034 §3.1–3.2为既有registry/version/immutablesnapshot/CRUD＋Reflect/Select/Improve/Evaluate/Commit类型签名重述；没有给可判定安全/monotonicacceptance新条件，不能由名字/typedalgebra证明safe-by-construction。拟pre-denomEX，尚待root准入差额确认，不是选后因深审费时缩池。

OT15114 §4.4直接将amortizedRA/OA transport用于mini-batchCFM，不是泛OT类比：2D三64unitSELU/20Ksteps/b512/sigma.1、50pretrainbatch/100projection、fixedRK4 101step，报告training/pretrain分账；W2略退与NPE变化保留。决定scope的关联已清楚，拟2+1+2=5，必要方法/理论假设未完成。Tweedie14486 §1完整原文是一般加噪posteriorfunctional存在/唯一/连续及Fourier构造，能关联Gaussian score→denoiser前提但原文未有diffusion训练/采样机制，准入关联待root；不因一般理论/经济来源排，也不因能联想到Ch24就自动收。

### Switch-KD14629 必要Source prepared（未独核）

作者actual §3.1–3.2/Eq1–15、§4.1/Table3–6/§4.3.1–4.3.5。teacher冻结、student全部trainable，额外训练path为Lteacher(Pteacher(Vstudent(image)),text)，输出logits与原teacher同vocab对齐；另student ownpath标准对齐。DBiLD不是直接每tokenKL，而按teacher/student各自Kneedle top-k的两两logitdifference再RKL，排序/成对数和额外teacherpath增加训练费，不能叫部署负担不变即训练免费。

局部对照采用SigLIP+2layerprojector/Qwen2.5，PT558K/DFT665K；0.5B←3B、1.5B←7B，两权重λ1=λ2=1/τ3；otherarchitectures比AlignKD时backbone及数据不同不可直接归因。Table3 w/oswitch58.8→switch60.1，但SciQA58.1→57.9、MMMU31.7→29.8反退。Table4 DBiLD0.5avgpoint是局部，top-k动态不是一切都better。Table5 PTDFT58.8 vsDPTDFT58.7，Table6 0.5B用更大7Bteacher59.8<3Bteacher60.1；正反侧均不消失。§4.3.5明确feature-space/vocab一致性要求，异构architecture尚待adapter，不能把interface兼容当已普适。必要hardware/precision/fulltrainingcost未在所读主实验披露（NotDisclosed）；不授能耗、streaming/concurrency/SLO或已复现。拟5标准Source支持条件机制，owner/Books尚待。

### AIM14779 必要Source prepared（中心因果解释待挑战，未独核）

作者actual §3–6/Table1–3及§6.4。VL-T5/FasterRCNN36region冻结vision，visualprojector/sharedencoder0–7/textencoder8–11+decoder划组；endtask500sample估diagonal empiricalFisher、以逐参数历史max保留importance、各subspace取分位冻结，ρvis.3/shared.1/text.5，再gradmask并配episodicreplay。VQAv2十task/COMP五fold、GQA六scene；M5000/500、3epoch/b80/AdamW1e-4，不能与no-memory正则直接视等预算。Table3 uniform/swapped/AP反侧支持受限mask分配选择；sumaggregationAF1.33优于max1.56但AP42.96<43.35，Group3Novel QUAD43.15>AIM42.22，不能称所有指标/组更好。

关键挑战：§4.3/Eq1从text参数总量使总penalty大，推出visual每参数必被“抢regularizationbudget”并非由式子成立；separable对角正则下visual坐标梯度2λIi(θi-θoldi)不因text参数数目直接变化，需另有globalcoupling或实证因果才能成立。Fisher/weightdrift相关不证明因果，Max非sum可减累加不证明任意task数uniformbound，分位ties也不授exactρfreeze。当前只拟采用modality-conditionedgradmask经验替代，不采这些普遍机制保证；是否中心争议隔离由root独核，不用小scope/noowner降分逃避。

## R5 root 首两项实际POST通过；作者本人注已同步读回

root实际POST读Ch49 24–48完整局部/两新增段与本人注3038、Ch56 1488–1522完整局部/小标题/两新增段与本人注2057，与A6逐字PRE/R2主源边界一致，继承/替代论证连贯，未移动原段。两项实际POST通过，非日级DAY。作者仅同步两本人注的R4PRE/R5POST事实并实际读回，精确窄位置未再改正文；待root保存后本人注final释放lease。

## A9 Looped stability15259必要深入prepared（中心强称反例待独核）

作者actual v1 §3.1–5.2/Prop1–5、AppA.4/A.5/A.6完整必要证明与B.1/B.5配置反侧。Smooth假设、g(x,θ)=fθ(x)-x全导数transversal是Prop1/2前提；结论是almostall参数的isolated/countable fixedpoints，compact时finite，不是任意autonomous架构完全无输入依赖。有限迭代、basin选择与真固定点输出不同。Recall分external/internal，只有internal让初始input只影响residualupdate；同参数近compute但internal每迭代多一次g。Brouwer存在不证明可达、更不证明正确解。

两处具体中心挑战：Prop4把attractingiffρ(M)<1说成必要充分，但smooth标量f(x)=x-x³在0的Jacobian1，足够小非零初值仍渐近收敛（边界非hyperbolic不能用严格线性稳定条件排除）。Prop5声称ρ<1后inputgradient必finite nonzero，而其自己式(I-Jx)^-1 Ju只有Ju非零/无抵消才能给非零；smooth recall f(x,u)=.5x+u²在u0固定点0收敛，导数0，直接不满足无条件nonzero。AppA.6证明到公式，没有补Ju非零假设。AppA.4由spectralradius→1推出I-J最小eig→0也不一般成立（接近-1的标量J可ρ→1而I-J→2），且原文承认boundary本身少信息；不采用全部rho1参数梯度爆炸保证。

可分离有效有限机制：需要区分固定点可达性、持续inputinjection和架构几何；条件收敛下IFT公式与g导数身份仍可作局部解释，但不向无条件Nash/全输入或泛化保证滑动。必要实验是hidden256/singlelayer、8head/MLP1024/GELU、3seed、AdamW100epoch/b500/maxloop30/progressiveα1；prefixsums32→512bit特例换slidingwindow5而非RoPE，chess/sudoku维度固定、难度轴不同。120B200GPUh/BF16compile单GPU不是端到端production或LLMscale证明；最佳norm/recall随任务/LR变，postnormtokenclustering与inputperturbation不足是直接反侧。当前拟7保持，不写Books强保证，需root独核中心争议/有限采用边界。

## A10 VisPCO/StreamCache必要Source prepared（未独核）

VisPCO15188作者actual §3/Eq1–17/Alg1、§4.1–4.4/Tables1–5。先将固定layerpruning与budget选择分开，outputKL是未压缩teacher-logits代理，不是任务truth；F(r)是decoderFLOPs模型。Gaussian rankthreshold interpolation＋STE有偏梯度，augmentedLagrangian/参数化single或multistep非全局Pareto证明，Theorem1是有二阶条件的局部解，不继承nonconvex离散任意初始化globalopt。Qwen2.5VL3B/30KLLaVA数据、8H20 96G、AdamWb16/4e-4，迁移Gemma3/LLaVA；50%附近budget配置差大，90%及极低budget益弱。Table2 Random160在三个任务44.0/48.1/82.4高于VisPCO43.6/47.5/81.3，但48h>1h，不抹掉质量—搜索成本反侧；Table4 H20 TTFT76vsFastV74ms/throughput20相同，不声称再带实际速度收益，fullservingconcurrency/length ND。模型配方/scoremethod不同及非均等搜索预算不汇成所有配置更快。

StreamCache15237作者actual §3.1–3.4/Eq1–15、§4.1–4.5/Tables1–7。CLCES用5层窗口rankvariance奖励稳定，HCC以score三层retain/merge/evict，moderate keys向retained/protected target余弦最近邻加权K/V；每层B200K、merge.15及DAP保护继承OVGGT。模型DINOv2/causalVGGT，单Ascend910B2；7Scenes/NRGBD/ETH3D/Bonn/KITTI，100–1000frame，预算/stride不同不直接比速度。Table2 NRGBD100Acc .0222劣于OVGGT.0220、300NC略退；Table3 400K多数值近似或更差，Table4 Bonn500 .072劣于.067，Table6 merge过多反退。作者声称constant是固定cache随T，不是sorting/rankhistory/nearestneighbor/输出map全部零成本；NlogN/WN费用不以“negligible”免验。

该源具体保证/接口冲突待root：Uniform(0,1)std=1/sqrt12不是有界rank分布“最大std”，rank跨层也未证iid；score∝inversevariance/unbiasedindependent同一几何量未验证，不能授MVUE。Eq12 target∈R∪P、Eq14更新targetKV，与§3.4“protected P exempt from both eviction and merging”存在保护定义含糊，不能直接发布exactrecipe/坐标anchor不变保证。Eq3 argminΣj·sπ(j)按rearrangement实际给降序而文字称升序；variance翻转可相同，不能仅此推全部经验无效。当前保6分，有限经验与中心保护/统计强称分开，未写Books。

### 来源最后查漏的有限停点

为弥补LLM简称/judge/reward术语漏项，仅加`submittedDate:[202604151800 TO 202604161800] AND ((cat:cs.CL OR cat:cs.AI OR cat:cs.LG) AND (all:LLM OR all:judge OR all:benchmark OR all:evaluation))`。单250请求传输不完整，不作成功或零命中；实际重取p1/p2/p3 start0/100/200、max100，total227、返回100/100/27，均完整XML。这是bounded主题补检，新增标题先跨四主题/同版有效记录去重，再只对真实相关潜力读AB，不将227全变候选/全文队列。

此前本轮cs.CL/cs.LG live month请求各仅14字节Rateexceeded，不作覆盖；标题导航实际可复用旧cs.CL/cs.AI各2000条当前ID段，但旧cs.LG693到08958、cs.DC45到06637未覆盖本窗，不称四类均有Apr17标题。systems/multi/agents主题入口实际有效；CV/RO/AR/PL/OS/PF/IR/MA标题补查仍待定点范围收口，不用关键词命中当全学科召回。

## R6 root 保存态本人注final通过，两个lease释放；新题摘/含糊门校准

root实际读回Ch49本人注3038/Ch56本人注2057，Prism/Scepsy全链通过，两个窄lease释放，日级未验。

root完整读A5的21＋A7的20条exactv1题摘（去重40含15299EX），明确机制/反证可按有限scope推进；不授Source或Books。决定门实际最小core：MirrorBench14785 III-B/C/IV固定同环境分层提示/镜像行动混淆是具体grounding评价边界，5可标准，非心理自觉/普遍自我缺失；OmniGCD14762 §3/4.1–4.3/5.1–5.2有synthetic低维跨模态settransform→clustering与frozenencoder分离的替代机制，5可入，不是统一语义空间，须保transductive全set/tSNE费用；CoTEvol14768 §3.4/Eq3–6/Table2–4有GT分型反馈＋最高entropy step保prefix重采样/fitness粒度消融与难度/GT依赖，5可标准，不授entropy=error/selfverify，整体setup/cost仍待必要Source。AnimationBench15299 §2/3.2–3.3/AppC只是现有VLMQA/人工偏好在新风格应用，没受控realism指标反排序/新评价机制，pre-denomEX通过，不泛称animation低价值。

root对原EX按理由分层实际抽检6项：14455/14661/14858/14518/14593/14984。14593另AB+最小core IV-A–E/V-C/VI：心理构念RepE/投影/回归/双向steering流程的新内容仅jealousy因子任务结果，safety为讨论前景，无实际toxicitybenchmark或新约束；没给通用FM表示/因果识别修正。双向加减不证necessary/sufficient，negativecontrol/筛选也未排全部confound；EX不是心理领域或已有RepE本身。其余具名明确EX未抽范围仍保身份和理由，不称全量复核，不为EX继续追日期/全文。

## R7 root 含糊贡献门实际最小core校准

root实际读Credo14401 §2.1–2.3/§3：dependency INVALIDATE/参数重写具体，5可标准，数据库明示不授一致性/安全/confidence校准证明；RaTA14951 §3.2–3.3/Eq4/§4.3 Table3为真实retrieval-rank preference，5可标准，JSON/fewshot反侧保留；ADAPT14902 §3.2–3.4/§4.1/Table5–6，固定goal/state变化与恢复precondition构成5分有限增量，须保privilegedheuristic及runtime分账。三项尚非必要Source最终通过。

SpaceMind14399 actual§3.5/4.4黑名单/去重/parentexistence与优选失败best-round未给新可验证安全条件，pre-denomEX通过（已核safe-guarantee信号，不授安全）；AGP15034 actual§3.1–3.2/Eq/Alg1仍为类型注册/版本/Reflect…Commit接口重述，没有可判定新acceptance/safety条件，EX通过。OT15114 actual§3.2/4.4明确CFM amortization机制，可5；W2三配置均弱于I-CFM，不改写为只有轻微差异，NPE和cost分别解释。Tweedie14486 intro/Table1支持非Gaussian posterior接口存在条件，可5必要标准理论；核standingassumptions/主要existence/uniqueness即可，不遍历全附录；Gaussian经典式不是本篇新贡献，不把读者denoiser连接当论文新sampler。

## R8 root 首六项自身v1日门实际校准；额外同版复用

root实际读Apr17 page01的15259/14779/14629/14401/15114/14486自身记录：各有v1Submitted（15日截后或16日截前）＋v1Updated Apr17（00–01Z）＋对应官方精确身份，与已核正常公告批界一致，支持各自有界Apr17归属；不是DataCitecreated单独作证，不借后版摘要/机制。18616不在这两页、保自身Apr22警报，不混59项。剩余拟选应给有限最终ID集合再独核自身元数据/异常，不重扫原月库存。

eval补检标题的四项同v1有效结果已由作者定点实读Apr17候选行及完整§4：15022 RouteRome §4 374–380（120blackboxqueries/surrogate→suffix、强route非truth/突破权限）；15149 GamingVerifiers 398–404（固定H原始/同构remap双验证、多个零观察shortcut反侧）；14345 482–486（biasL与variance不同，current v6/PAC-CF标题变化不是新事件）；14877 582–588（matched(k,T)、64次失败非概率零、T非nested不保证单调）。复用必要审阅与具体Books处置，不重评分、不移动原候选、不整体继承邻日池。

## A11 R3D/RaTA/Credo必要Source prepared（未独核）

R3D15281作者actual §3–5/Table1–10、AppB训练/点云输入、Cpretraining/D预处理/E各baseline配置。受测DP3默认下PointNet BN→LN avg1.0→59.6，Uni3D BN→LN0→64.7是具体归一化混杂反例；不是从所有大encoder推伸缩定律。PointSAM dense tokens→crossattention actiondenoise较globalconditioning62.5→77.5，pretrain相对scratch65.75，auxEE再79.75；但shoe92→87/hammer94→91反退，causalattention不等优化不干扰或免费。1024point tiny83.8>small76.8>base73，8192point small81.8>tiny68/base80.2；更多demonstrations不消除tiny优势。FPS重排/colorjitter/coordproprio噪声与dropout共同，未逐项证明各自唯一原因。

RoboTwin每task50demo、easy/hard各5、ManiSkill1000demo与5子任务；ours horizon16/1000epoch，DP3 horizon8/3000epoch，其他baselines训练/点数/pretrain预算不同，不把headline归给单机制。Hard stapler27<ManiFlow44、ManiSkillStack24<ACT35，未全任务胜。实机xArm6/双D435、每task50demo/50evaltrials三任务，discolight自身68.7→58.7；训练CDM增强、部署CDM关闭/8192均匀采样，不能照“exactsame”忽略Pi0输入适配与budget差异。预训练40epoch/8H20及ScanNet/ARKitScenes/PartNeXt额外监督需另计，真实eval训练seed/置信区间/总runtime ND。AppD去staticframes能影响freezing并与aug/norm混杂；有限结论只重开perceptioncapacity/normalization/pointdensity联合选择，不授通用机器人安全或任意规模。

RaTA14951作者actual §3.1–3.3/Eq1–4、§4.1–4.4/Table1–3。query→QwenOmni JSON taskdescription→Qwen3Embedding8B nearesttool，偏好正例是五种decoding候选里GTtoolrank最低的description，负例从其余均采样，同rank全弃。SFT4epoch/2L40S或A40、DPOLoRAr8alpha16/8epoch/1GPU；826traintool/94testtool，查询可相同文本配不同模态/GT，每querytoolpair独立exactmatch，指标不是tool实际执行正确性。DPO3B weighted69.7→70.4/7B70.6→70.8；7Bimage58.8→57.1、audio不变83.7，不能称每modality提升。Table3 NL/JSON与fewshot反侧和正文自称“consistently”冲突，采用rankcredit而非JSON普遍优、unseentoolgrounding保证。不同retriever尺寸/embedding费用不等，inferenceprecision/latency/seed ND；必要标准支持有限描述生成目标选择，未核code/production。

Credo14401作者actual §1–4全部短主文/Fig1–4。typed(value,confidence) static/dynamicbelief、dependency、policy INVALIDATE evidence/modelanswer/verified后改retrieve参数、按依赖重跑构成显式controlplane；不是DB就证明事务一致性、终止、安全或confidence校准。FinanceBench100query/18固定配置的Fig1仅说明retrieval/model/prompt取舍；12B同strategy BM25 45 vsdense72、27B BM2550<4Bdense65不是adaptivepolicy已控budget收益。Demo两示例和逐步UI展示，没有adaptive固定同budget对照/多seed，hardcodedconfidence threshold未经校准；operator可注册任意API不授权限控制/sideeffectexactlyonce。模型Gemma3 4/12/27B、topk6/12与inference+embeddingcost范围明确，硬件/precision/并发/总latency ND。有限采用belief依赖失效与物理参数重写接口，收益/一致性/安全不采用；owner比较尚未做。

## R9 root SwitchKD通过；AIM/Loop中心争议隔离

root实际读SwitchKD14629 §3.1–3.2/Eq1–15、§4.1–4.2/Table1–2/§4.3/Table3–6及限制，A8有限机制/反侧/成本通过，5标准可接owner，不授所有配置优/已实现。

root实际读AIM14779 §4.1–4.3/Eq1、§5/6.1/Table1–3/§6.4：separable正则确不因另一组参数数量直接减少本坐标梯度，Max/ties无普遍保证；经验与反侧保留，但中心“文本抢预算→视觉必欠正则”未闭。维持5标准，中心争议/暂缓终态隔离，不用Only代替。重开需显示实际全局耦合或受控消融能区分参数数量/λ/模态异质性的因果解释，不能只再给Fisher相关。

root实际读Loop15259 §3–5/Prop4–5、A4–6/B1/B5，两scalarcounter有效，rho→1也不等I−J奇异；支持局部条件式、不支持无条件nonzero/iff。维持7深入完成、中心Disputed暂缓，正面Books不写；120B200GPUh/single256/3seed和任务/Norm反侧保留。重开需正式修正边界稳定/持续输入非零导数的必要假设（含Ju/退化点与谱位置）并重验依赖主张，不能用有限FP迭代稳定代替外推。

## A12 SpecGuard15244必要深入prepared（中心正确性保证待独核）

作者actual v1 §3.1–3.5/Alg1–2/Lemma1–2/Theorem1、§4.1–4.5/Table1–2、§6与AppA2.1–2.3/Table4–9。保原6分，因correctness强称影响已知SD/验证边界深入受影响内容，不用改分配工作。草稿/target每step16sample、sentence-transformer相似度selector、minlogprob＋attentionrollout权重β.3/阈值τ.7；fallback再target16sample。不是经典精确target分布SD；内部信号也不等零额外模型，selector明确用外部sentence-transformer。

中心反证：§3.1说rollout行在inputtoken上归一后又以suminput定义G，该文字下总和恒1，具体归一域/headsparse后处理缺少可执行澄清；attention质量不自证faithfulness。weightedmean≥τ不强制两信号都≥τ，与“simultaneously”强称不同。Lemma1只能约束P(accept|correct)敏感性，不能推出P(correct|accept)；尚须τ≤α，unionbound也不需要independence。Theorem1把敏感性直接写成allacceptedcorrect乘积，缺错误先验/条件独立或逐history条件，随机C_T亦不能直接作确定指数。Lemma2 target调用次数与k个生成/attentionrollout/embedding全部计算不是一个费用，均不能授soundness或准确率不损保证。

评价A100/vLLM、QwenMath1.5B/7B/Qwen1.5B7B/Llama1B8B、Math500/GSM8K/Gaokao/Olympiad四EM任务，\n\n定义step、temp.7/topP.8/n16；Greedy n1另列。QwenMathGSM95.8、34min vsRSDmajority88.7/>41min是整套选择器局部对照，不是单token速度/生产SLO，SD7tokens与search预算/targetcapacity不同。QwenMathgreedyOlympiad40.7<targetmajority41.0、generalgreedyOlympiad37.8<target38.8，不能所有配置优。§6明确singleinstance、无batch/硬件优化/开放生成；precision/长度/并发及种子置信区间ND。有限经验与错误保证分离，拟中心争议暂缓，不写Books正面验证保证；重开需正确条件化定理与实际G归一/执行身份澄清，再核相应对照。

## R10 root A11三必要Source通过、56自身日门与SpecGuard争议

root实际读Credo §1–4/Fig1–4全部短主文、RaTA §3/4.1–4.3/Table1–3、R3D §3–5/Table1–10及必要AppB/C/D/E，A11有限采用边界通过，可接具体owner，非Books或复现通过。R3D §4.7说实机ViTsmall而§5.3写tiny，recipe身份未统一；CDM训练开/部署关、causalmask不阻所有梯度耦合保留，只支持normalization/密度/容量/数据/消费者成本共同选择。

root对作者给的有限56精确ID逐条提取并实际读Apr17 page01/02自身title、v1Submitted/Updated/Available：均匹配身份，Submitted Apr15 18:00:45Z～Apr16 17:59:44Z，各自身Updated Apr17 00:04～01:06Z，结合已核正常公告批界/官方精确身份支持Apr17日门（含15281）；不作created单证或historical逐篇列表证明。已通过的8身份不重审。

root实际核SpecGuard15244 §3.1–3.5/Alg1–2/Lemma1/Thm1、§4.1/Table1/§6–7，A12中心争议通过：correct条件recall不能反转PPV、joint乘积无history条件且右侧随机CT；weightedmean不保双阈值、G归一域需澄清。维持6及必要深入范围、Disputed暂缓隔离，不以Only隐藏、不写Books正确性保证；终态重开条件沿A12，不遍历无关图/附件。

15010轻量纠错：root实际读当前官方abs Comments，v2Jul17明确correction citation/CLT detection-only hook、position-specificity非siteidentity、弱化necessity/depth；Apr17有效v1行/完整§4仅有限steering/skip复现且明示prompt位置不同/非普遍16层/无永久不可纠错，Only未正面采用检测机制。本日仅同v1复用，Jul17修订作为真实归属事件恢复线索，不新增Apr17候选/重评分、不追全v2；后续仅当某实际采用claim依赖受损detection才定点重开，不改已验收昨天报告。

### 最后既具名决定门与发现停点

停止新的发现入口；四主题＋eval227分页及实际cs.CL/cs.AI相关标题范围收口，不扩新的泛化backstop队列。其他category标题未覆盖范围如实保留，不宣称全学科召回。只有已具名13条＋14709/15037/15184的决定门待关闭，不将各层统称“待全文”。14698/14980/15297原v1AB已另取并实际完整读：MFPO v1仅MuJoCo/DMC，不倒灌后版Humanoid；ConfGuide v1也是medicalmultilabel conformalset→VLMguidance；optimizer v1的数量宏未展开，结论仍tabularMLP的Muon/EMA及费用取舍，不借v2具体数量。

## A13 首四项具体owner比较与两最小逐字PRE（未授lease）

作者恢复后重读Books背景/理念/写作、ROADMAP及当前LS路由，实际读Ch23 stitching两侧与Ch22/24交接、Ch26 component-scaling两侧与Ch25/27交接，未写共享Books。

Credo14401拟已有覆盖：`AGENT-WORKFLOW` Ch81的StateMachine/persistedpolicy、label未变而evidence改变仍reactivate段、650依赖revisionjournal/未知依赖扩大失效段，实际承载显式controller和依赖局部重算；DBcatalog/demo没有受控证据改变这些长期成立边界，不冒充实际transaction实现覆盖。RaTA14951拟已有覆盖：`AGENT-TOOL-CALLING` Ch78的217–223 shortlistproposal/目录漂移、634–644集合/rank仅discovery非execution，配Ch34 303–317 pair排序依据/独立评价/shortcut。GTretrievalrank是本任务pairlabel owner，不改变DPO目标形式或执行权限；Table3是报告内有限格式/训练适用条件，不为任务配置堆一段。两NC均待root实际比较，不以主题映射代替。

### SwitchKD14629：申请Ch23窄位置

`books/part-03-multimodal-world-models/23-multimodal-representation.md`，VFM stitching第二段（以“有限VFM stitching对照”起）完整反侧后、fisheye段前，两段＋末尾本人note。新增差额不是feature接近，而是把studentvisual送入冻结teacherprojector/LLM，以最终teacherlogits反传训练studentvisual，与student自己语言路径区分。逐字稿：

> 适配还可以在训练时把学生的视觉表示送进冻结教师的完整消费者，而不只匹配切点 feature。若两侧视觉接口和输出词表兼容，保留学生自己的语言路径，同时将学生视觉 encoder 的输出交给教师 projector 与语言模型，再用教师原路径的输出约束这条交叉路径；教师参数冻结仍须向学生视觉分支传播梯度。它把“视觉表示是否能被较强消费者读懂”变成额外训练目标，不代表教师输出是真值，也不要求部署继续运行教师。<!-- source-family:SF-2026-ARXIV-2604-14629 -->
>
> [Switch-KD 的受限对照](https://arxiv.org/html/2604.14629v1)用双方选定的 top-k logit 成对差异对齐，增加排序、配对与额外教师前向/反向；部署结构不变不等训练免费。局部平均收益伴随 SciQA/MMMU 退步，更大教师和增加训练阶段也非单调更好；跨架构比较又混有骨干、数据差异。视觉空间或词表不兼容时仍需额外 adapter，不能批准任意异构替换。应连同监督、两条训练路径及消费者回归验收；质量或总预算失配时，保留普通输出蒸馏、原 feature 接口与独立学生训练，不让交叉路径的低 loss 自签全任务兼容。

本人note逐字：`- SF-2026-ARXIV-2604-14629 — Daily2026-04-18补Apr17；[Switch-KD exact-v1](https://arxiv.org/html/2604.14629v1) §3.1–3.2/Eq1–15、§4.1–4.3/Table1–6及异构限制。5标准，交叉teacher-consumer路径为具体owner差额而必要加深；仅兼容接口/词表下student视觉读出训练，不采全任务优、训练免费或任意异构迁移。root必要Source/date通过，逐字PRE/实际POST待验；未核artifact/复现。`

### R3D15281：申请Ch26窄位置

`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，LIBERO encoder/action-codec有限反侧完整段后、PAMDP混合离散连续段前，两段＋本人note。现有只承载actionbottleneck，缺normalization和pointdensity会改变同一consumer扩容判断的实控反例。逐字稿：

> 即使动作 head 不变，感知扩容也要先排除训练配方造成的假瓶颈。一个受限 3D policy 对照保持 DP3 设置，分别替换 PointNet 与较大视觉骨干中的 BatchNorm/LayerNorm，观察到原先几乎无法训练的配置在更换归一化后恢复；这足以挑战“大骨干本来就不适合 policy”的归因，却不能证明所有骨干只换归一化即可。点采样顺序、颜色与坐标扰动、静止帧过滤及预训练监督都可能改变过拟合，应与容量和闭环结果共同记录，而不是把感知预训练分数直接换算成动作成功率。<!-- source-family:SF-2026-ARXIV-2604-15281 -->
>
> [R3D 的有限证据](https://arxiv.org/html/2604.15281v1)还把 dense geometric tokens 交给 action queries，而非先池化成全局 feature；它保留可读位置，却增加 attention、点云制备和训练成本。1024 点下较小骨干更好、8192 点下中等骨干更好，辅助末端动作监督也有子任务退步，不能写成容量或联合目标单调获益。不同基线的 horizon/训练预算不等，实机骨干型号叙述未统一，训练开启的深度增强在部署关闭；三任务双相机实验不提供统一 recipe、控制 deadline 或物理安全证明。归一化、点密度或消费者质量失配时，保留较小骨干、原全局表示与已验证连续 policy，重新核真实观察和 controller，而非继续无条件扩容。

本人note逐字：`- SF-2026-ARXIV-2604-15281 — Daily2026-04-18补Apr17；[R3D exact-v1](https://arxiv.org/html/2604.15281v1) §3–5/Table1–10及必要AppB–E。7深入，BN/LN受控反例与pointdensity/capacity/consumer共同选择为差额；保dense/aux反退、预算/静止帧/pretrain与实机tiny-small/CDM差异，不授所有骨干修复、无梯度干扰或安全部署。root必要Source/date通过，逐字PRE/实际POST待验；未核artifact/复现。`

## R11 root 两NC/两逐字PRE通过并授窄lease；最后题摘边界

root实际读Ch81 state/policy/activation及label/evidence-reactivation、revision/readcertificate依赖完整局部，Credo有限NC通过；Ch78 shortlist/revisablefrontier/set/rank完整局部＋Ch34 pairlabel来源/独立评价/shortcut，RaTA有限NC通过，不冒充现有SQL/ranklabel实现。root actual Ch23 stitching完整两段→fisheye、Ch26 LIBERO两段→PAMDP完整两段，两gap与A13逐字稿/本人注PRE通过，授各指定两段＋本人注窄lease。作者已按稿写入，Ch23正文87/89及本人注2172、Ch26正文238/240及本人注2495，原邻段/index保持；限定diffcheck通过，尚待root实际POST。

最后16决定门root完整读15个exactv1题摘；15140原XML为v2尚不当v1已读，正定点取v1AB。14375/14338/14332/14698/15063/14709有明确机制/评价反证可有限评分；14332/15063因correctness/security变化仅深入受影响命题。14867/14519/15037/15184/14980 root接必要最小core，无作者重复全文。15297只是tabularMLP同协议Muon/EMA经验，无FM适用性边界/机制反证，EX通过（非所有小模型优化排）；14773taxonomy未给独立评价盲区受控证据、15115是CNNFL局部算法无可支持FM/平台责任变化、14487为SNN特有firing度量无本项目foundationbridge，三EX有限成立，不由领域名称硬排，不外推generalinference。

## A14 AdaSplash-2 15180必要Source prepared（未独核）

作者actual §2.3–2.4/§3.1–3.3/Eq3–11、§4.1–4.3/Table1–3，必要B1阈值证明/C5overflow/D训练评价。左binendpoint histogram在SRAM归纳scores，先maxpass再histogrampass，以histroot初始化后用按alpha选Halley/Newton/secant＋越界bisection回退refine，构建bitpacked nonzeroblockmask/fns跳过，并复用backward。它加速的是本来entmax稀疏算子，不是softmax的exactdropin；hist初始化/数轮refine和mask制备仍需多遍读key。w64/B8/Bc64 bin容量16320keys，长序列须periodicflush；morebins降低误差但减小容量，不能由O(B)抹掉overflow或HBM费用。

必要理论边界：Eq7把最大z=1夹到最后bin，B1却用z<b+h作全域严格不等，singleton/oneactive support可使tau*=0、tauh=-h，反驳主文strict error<h及两根都在[0,1]的普遍说法；较弱非严格0≤tau*−tauh≤h与保守support可单独讨论，不能以此断言完整kernel无误/误差零。B2关于f的smoothness只按alpha与support跨界条件，不能把有界二阶导数等同任意迭代全局收敛；本文采用机制不照抄强数值保证，具体recipe需澄清clamp/精确refine后。

microbenchmark单A6000/bf16/headdim64/4K–128K，GaussianQKV以variance调sparsity，长context用1B模型sparsity抽样；低sparsity/forward多遍可慢于FA2，backward收益与高sparsity才形成有利组合，非完整训练或serving加速。语言模型350M/1B、50B DCLM-Edu/4H100、b524Ktokens/100Ksteps/WSD，最后10B改ProLong32K；NAPE(NoPE/ALiBi各半heads)与RoPE分开。1B RoPE RULER32K entmax23.4<softmax27.3、shortavg51.2<52.5，NAPE53.1vs53.0亦近似；不能“allacrosstheboard”。HELMETICL是子集非全部benchmark，主inference采用fullymaterializedlogits简化路径，不能继承trainingkernelmemory优势。原6分必要Source支持有限hardware稀疏接口，数值边界独立隔离，未核artifact/复现，owner待比较。

## A15 两视频/Omni反证必要Source prepared（未独核）

15280作者actual §3.1–3.4/Table1–2、§4.1–4.2/Table3、§5。MAFW495(11×45)/DFEW700(7×100)平衡test使WAR=UAR；余样本train，不把balancedtest当原自然人口。GoogleNgram英中11词频与VLM每类F1相关（11个classes不是视频样本数），专有pretrain无法读，§5承认correlative，不能由correlation或非对称confusion唯一识别训练频率原因；“semanticconfusion必对称”没有证明。Shuffle同组frame对VLM小变、specialist约15–16%相对F1下降，支持这两个任务/受测sampling中的顺序利用差，不能推出架构普遍bagofframes或causalmask失效。Qwen2.5VL/EmotionQwen 1/5/10/15/20/25FPS曲线非单调，但不能单靠它定位attentiondilution唯一原因。

约1500balancedfinetune同时减少约6倍样本与改变分布，非相同人口/预算因果；MSCE在稀疏keyframe间各读m4frames生成motiontext、再交错frame/text分类，是增加观察＋摘要调用，不是从未看过的信息恢复真值。三个模型六个datasetF1局部提升，但EmotionQwen MAFW recall.2925→.3061、precision等各轴需分验，summary噪声承认，未给matched额外观察或同预算captionbaseline。硬件/precision/完整latency/concurrency/多seedCI未披露，支持有限ordering/density/proxy与消费通道边界，不采所有VLM/心理真值/新架构保证；拟5标准的反证范围，owner待比较。

CoM14520作者actual §3.1–3.3/Table2–3、§4.1/公式1–7、§5.1–5.4/Table4–8。query-onlyplanner选modality集合/顺序/parallel-sequential-interleaved和PD或PRD；parallel单独调用各模态再concatenate文本，PRDdecider只读rationales。Invalidtopology回Audio→Visual，并非planner已证找minimal sufficient/optimal；文本隔离原sensor只切断该阶段输入，不证明rationale真实或strictgrounding/因果链。fixedtopology/顺序翻转提供有限inputserialization选择差，而attention/Yesrate变化不独立证明唯一position因果。

QwenOmni3B/7B、Ola7B七benchmark，temp0/fixedseed；训练freePD与Gemini2.5Pro4745trajectory/LoRAr16/1epoch的PRD分开，Table5的PD/PRD都SFT，不能把总体优势归trainingfree拓扑。Table6固定parallel MusicAV64.8>CoM63.7、AHal83.7>78.2，interleavedDaily55.5>55.4；Table4 Ola/Music/world与3BAHal有反退，Table7另prompt音乐78.6→78.0，Table8Omni prefill.089→.098、generate.682→.763更慢。singlevGPU/100samples只局部TTFT与pertoken、未披露GPU型号/precision/总pipelineplanner计时口径，不是端到端免费；5framesvs15frames只是visualtokens非总compute。Ola不支持interleaved、3Bfallback暴露可用拓扑/指令能力条件。拟5标准有限替代serialization/两种consumer路径，不授统一模态融合或推理保证，owner待比较。

## R12 root Switch/R3D实际POST通过

root actual读Ch23 79–95完整局部含Switch正文87/89＋本人注2172、Ch26 232–252完整局部含R3D正文238/240＋本人注2495，内容与A13逐字PRE/必要Source边界一致，旧邻段保留，两实际POST通过。作者仅同步两本人注为实际层并实读回，尚待root保存态注final释放lease；日级未验。

## A16 ADAPT14902/StreamingASR14493必要Source prepared（未独核）

ADAPT作者actual §3.1–3.4/Table2–3、§4/§5.1–5.6/Table4–6及Limitations/Risks。state注入occ/used/dirty同时保持goal/instruction，FF重生成仅保可解任务；这是选择后可解人口，非任意变化或唯一cause证明。LLaVA1.5-7B LoRA与available/unavailable参考图＋当前观察判状态，暂挂原action、提恢复策略再resume；新增Waitcontroller，CAPEAM给oraclesubgoal/experttrajectory、SayCan给visibilityoracle，不能宣称全链仅模块变化。Table5 27.69>6.15但privilegedsymbolic46.15更高；各主结果与该dynamic子人口不混，single deterministic fulltest不等多seedCI。RTX3090总72.6→210.8s、init32.8s/每call.2s分开，step358→371不足单证全部差来自环境等待；occlusion误判/恢复错误保留。§Risk明确无真机uncertainty/safety/HRI，5标准仅固定目标下state/precondition与plan分责的评价边界，未核artifact/复现。拟owner `AGENT-PLANNING`，当前Ch79 conditionalpolicy与实际observation/precondition机制可能具体已有覆盖，待root比较而非自动写书。

StreamingASR14493作者actual §3–9/Table2–6及必要streaming/quantization边界。ESB八英文domain全utterance最终拼chunktranscript，avgWER非tail/partialrevision/stability；EPYC7V12 AVX2限32core/CPU batch1 vsH100PyTorch分开。Nemotron.6B cacheawareencoder/LSTMdecoder/joiner三graph，FP32 rollingcache与melringbuffer跨chunk维护，权重量化只encoder、decoder/joinerFP32；kquantblock32/20scale候选是weightonlyFP32activation MatMulNBits，不是全部int4计算。RTN与weightedfit/敏感QKVO和首尾int8的代价分开，不由模型磁盘尺寸证明总RAM。

同560mschunk/5.6shistory vs1.12shistory WER7.28→8.51支持historybudget；80/160/1120ms亦不同精度与吞吐。PyTorchCUDA7.28→CPUONNXFP32 8.03是runtime转换缝，文中只猜kernel差不证明export数值等价；在同CPUFP32基线下int4kquant8.20/RTFx7.20/.67GB，int4RTN8.46/7.30/.66GB，mixed8.12/7.15/.73GB，而ConvInteger10.14/8.0更快却更差。0.56*(1+1/RTFx)是平均吞吐推导非逐chunktail、未测consumer弱机/50ms外推不作实测，32servercores不授所有ondevice/实时SLO。初始Parakeetchunk搜索9.22与跨模型表12.83配置人口不同，不拼成同一值；无生产ITN/diarization/codeswitch词表评估。标准5只采streamingstate与分组件precision/评价身份边界，不采SDK发布状态或所有batch模型不适合streaming，artifact/复现未核；owner待比较。

## A17 SGA-MCTS14712/Sager14972必要Source prepared（未独核）

SGA作者actual §3.1–3.4/Eq1–5、§4.1–4.2/Table1–2、§5.1–5.3/Table3–4/§7。MCTS只离线expansion加Plan/Reflect，successful+shortreward→LLM抽去词汇的state-goal-action atom，online topK软提示/LLMinstantiate，不是rigidtemplate。Known-info tracker也是LLM；加权cosine＋slotoverlap的β混合分不是硬前置条件gate，语义分可补偿缺失slot，success轨迹不证明每个transition正确/因果或所有control literal已安全保留。MCTS树共享访问不自动实现跨路径state-goal transposition；无实现核验不采“inherentDAGdedup/收敛最优”。

Qwen3 8/14/32B nonthinking，GPT5thinking仅reference；StableTB G2offline→G3online，ToolHop50/50、BFCL25/75split。Table1提高但Table2 online630tokens仍多于ReAct260，只少于thinking2713，离线2388/10685/1290exploredactions及213/1560/226atom/embedding与state-tracker费用另计，未实测strictlatencybreak-even。Hybridβ0反退1.5point只局部support，familiarity cosine不是新工具identity或entropy/OOD真值，三个不同dataset关联不足唯一归因abstractlogic。报告mean±但主设置硬件/precision/总离线费/严格SLO/重复次数未披露，保seedquestioncoverage和verification质量上限限制。5标准有限采用离线atom与在线softretrieval分责，不采verifiedtransition/hallucination完全消除，owner待比较。

Sager作者actual §2.1–2.5/Eq1–5/Alg1、§3.1–3.5/Table1–5/长短与warmup反侧。factmemory与per-user自然语言policy分存，full约1500chars作更新substrate，每次extract约30token likes/style给listwise ranking，instruction>facets>skill只prompt优先级，不是hardauthorization。选择一个正例/其余未选不当disliked，new low、支持后medium/high、明确矛盾降一层的structureddiff；这些是heuristic tier不是校准probability，单次未选不负标注是有限反馈合同。Listwise消tie是输出形式性质，不证明真实偏好唯一全序或模型必然遵循softtie-breaker。

gpt4omini/MemRecgraph，Books/Goodreads/MovieTV/Yelp N10=1positive+9randomnegatives；warmup τ0–3后冻结技能再test，不能称testtime持续自进化或真实在线用户试验。相同memorybackbone但rank/objectives/skill一起变，不是仅policy-evolution唯一因果；leaveoneout与fullreplace对照支持受测增量，test全次p<.05声明未替代多seed置信区间。τ3在sparseBooks回退，10/30/80/150/200token sweep中30局部较好，不授通用100token“cognitive boundary”/attention唯一原因。统计初始化/graph/retrieval/summary/skill更新/排序调用全计费，ND硬件precision和端到端费用；四datasetdensity相关不是density唯一cause。5标准有限采用full/slim表示与保守diff/反馈标签分责，不采用户心理真值或一般Agent政策可自动授权，owner待比较。

## R13 root 最后16决定门冻结、两本人注final

root actual读最后必要5门：FCL14867 §3–5三反馈级控制与有限计数trace反例诊断，可5；CI-CBM14519 §3.2/Table5把concept保持与旧class读出保持分开，regularization-only近乎无变而pseudo有效，可5具体设计反例；ProVoice15037 §2/3.2–3.3/Eq1/Table1–2把FPR/Recall与trigger-gated回答分验、thinking非各声任务单调，可5；AAD15184 §3–4 solver表示/错误中间render/确定性诊断与faceidentity接口，可5，只prototype/无受控因果提升，不以CAD本身准入。ConfGuide14980 §2–3只是现有CRC＋正反argument医疗组合，无新校准法/有效性边界或具体因果反证，EX通过；CRC预测集期望风险不保证argument真实/完整，排除类无法review，不因此扩全医疗。DiscoTrace15140v1完整citationabstract已独立实读，具体修辞多样性描述EX通过，不称核全文。

最终有限候选/关闭层：原56＋新增10（14375/14338/14332/14698/15063/14709/14867/14519/15037/15184）＝66；最后六EX为14773/15140/15297/15115/14487/14980。新10自身日门root待核，不能先列确定当窗候选。没有新发现入口，所有普通待办只接这有限集合的必要层。FedGUI14956仍4分关闭层，不因好写或owner提高分；若其已具名设计反证触发，则只加深受影响命题。

root actual读回Ch23本人注2172/Ch26本人注2495保存态，Switch/R3D全链通过，两指定窄锁释放；无书稿锁占用。

## A18 UniDoc14967/TurboTalk14580必要Source prepared（未独核）

UniDoc作者actual §3.1–3.4/Eq1–9/Alg1、§4.1–4.4/Table1、§5–6/Table2–3及必要A2/A3/C/D。search→selectindices→bboxcrop/zoom分责；多次search按rank interleave算NDCG不是去重集合，不能从局部filter宣称同一候选集recall凭空提高。selection无gold时以retrievertop1作pseudo-positive，不能叫标注真值；IoU到teacher/Mineru候选box只空间代理，patterntag不证明可执行/事实正确。Qwen2.5VL3/7B、SFT12621/RL5537、8A10080GB/group5，SFT表冻结vision/projector而language更新，不照“fullparameter”推全模型trainable。RL oneepoch/TP4/maxprompt40K/maxresponse1024、λ=.1四项+.6answer；Qwen2.5-72B binaryRM、teacher235B与同teacherfilter产生共同偏差，finalanswer过关不证明每个中间step正确。

Table2 select带overall66.6→70/crop71；Table3加retrievalreward VDS76.7→76.2、selection MMLB36.8→36.6、crop VDS77.8→77.4，不能densefeedback全轴改善或唯一因果。训练和评价均涉及SlideVQA，本文未在所读层证源document严格去重，保split协议局限，不自行断泄漏。SFT/RL/过滤人口、额外retrieval/crop/encoder和RM全计费，未给matched整链latency/concurrency/seedCI；toolobservation放Userrole是输入协议选择，不升级tool为人类指令authority。6标准有限hierarchicalaction/各rewardtarget分责，owner待比较，未核code/复现。

TurboTalk作者actual §3.1–3.4/Eq1–11/Alg1、§4.1–4.3/Table1–4。InfiniteTalk DMD多步→4，再3→2→1对抗蒸馏，前steps stopgrad但共享参数继续更新，不等中间函数永久固定；warmup只扰动最后t，selfcompare由4step初始化discriminator的denoise分支产生，不称独立冻结teacher或groundtruth。R3GAN与R1/R2/R3扰动正则实际目标；Eq11的(1−λ)real+λself与Alg1 real+λself、设置λ.5与Table4 50尺度未统一，不发布精确recipe或全局稳定保证。

2000h单人video＋辅助200Kclips；DMD2000steps/64H800、adv3000/32H800/b1/ZeRO3、81frames/720p附近、50%iter含9contextframes；wav2vec2读相邻未来audio不授zero-lookaheadstreaming。三测试集各40video，其他4NFEtrainedbaselines直接跑1/2step，不等对应预算重训；120NFE→1只是调用数比，不是实测120×端到端速度/real-timeSLO。Table2 dynamicTS让SyncD8.43→8.65更差、全组件FID31.46稍劣selfcompare31.41；Table3GANFVD411.58好于R3GAN414.23，Table1自身1vs4step及teacher音画/质量各有反退，不采全指标无损。训练/critic/reference/wav2vec2/VAE全计费，precision/完整时延/并发/seedCI ND。5标准有限progressivebudget与intermediatereference稳定化分支，必要source边界足即停，owner待比较。

## R14 root 最后10自身v1日门通过

root actual逐身份读原DataCiteApr17p1/p2 title/ownv1Submitted/ownv1Updated/Available：14375/14338/14332/14698/15063/14709/14867/14519/15037/15184均自身v1Apr17 Updated00:05–01:01Z、SubmittedApr15晚～16正常批界，同已核公告批界合证日门通过。14698v2June2、14709v2Apr24/v3May6、15037v2Apr21/v3May5、15184v2Apr28分开，不借后版论证v1。66包含FedGUI4分关闭，不是66正面贡献；必要日期例外继续隔离，不先读core。

## A19 机构自然日差额与原始检查记录的复用位置

作者实际完整重读本日原`V3_REVIEW_CHECKPOINT.md`，按记录的入口/分页/日期邻界复用，而不是继承其完成标签。该文件10–27行保存初次各源实际检查，29–31行为实际收口，35–39行是五项必要目录再读；这些是原来源检查记录，不冒称本次重新访问所有网站。下面是Apr17自然日的差额判断，reader尚须实际核范围/停点；原小时arXiv结论明显失效，必须替换。

| 来源 | 原记录位置与实际停点 | Apr17自然日差额/限制 |
| --- | --- | --- |
| SRC-OPENAI | 原16行：完整RSS1230、Apr16 10Z→Apr20 00Z；Research403 | RSS日期邻界仍跨Apr17；Research历史缺口继续隔离，不授该目录Coverage |
| SRC-ANTHROPIC | 原15行：publishedOn Apr14 13:01Z→Apr22 14:12/14:27Z | 同目录日期仍不含Apr17，无需重读邻窗正文 |
| SRC-GOOGLE-AI | 原17/31/39行：Research四月9条Apr16→21；DeepMind实际page3七April原文30/27/23/22/15/14/2；Publications771页泛目录 | 两Blog日界不含Apr17可复用，Publications日级停点仍缺，不扩全年队列 |
| SRC-META-AI | 原18/31行：Research0抽取、Blog两页混April08/06/July等、Publication超时 | 无可靠历史停点，保留隔离，不把空提取当零命中 |
| SRC-QWEN | 原19/31/39行：dynamic40 extra.date Apr15 10+08→Apr18 10+08、static60最晚Dec23；org58止2023，release页跳Qwen3.8无release | Apr18仍自然日窗外，不只因旧截止后一小时；当前rename不替历史release，有限目录可复用 |
| SRC-DEEPSEEK | 原20行：news动态Apr24→Dec1、研究Jun24→Feb25；org39止2023 | 目录日界不含Apr17；只有限公开索引/仓库事件 |
| SRC-MOONSHOT | 原21/31行：Blog26最新2025Nov7；org43止2023、release页无项 | 组织/release可复用实际层，2026Blog历史缺口不获Coverage |
| SRC-TENCENT-HUNYUAN | 原22/39行：publicList page1/100 total9/list9 displayApr23→Feb13；org83止2024 | 无Apr17项；HY-SOAR createdApr16 06:34Z为Apr16自然日，不反推论文日 |
| SRC-ZAI | 原23/31行及冻结README：Research15 Apr29→Apr7→Apr1、releasenotes Jun16→Apr7→Feb12；org53止2021 | 可见三个目录不含Apr17，无普通PR扩扫 |
| SRC-BYTEDANCE-SEED | 原24/31/39行：type1 page20/20条May13→Apr9、PublishDate Apr20→16；type2 page0/20 total95、Apr23→9→1、page20为2025；org63止2024 | 日期桶可复用，不视精确首发；LeapAlign15311具体早目录异常不因整源目录无Apr17消失 |
| SRC-BAIDU-ERNIE | 原25行：第一页10条Apr30→Apr15→Feb6，尾2025Nov | Apr15整天窗外，只复用目录停点，不重审Image |
| SRC-XIAOMI-MIMO | 原26/31行：Paper8 Jun29→Mar13；Blog14无日期；org18止2025 | Paper/仓库有限层无Apr17；无日期Blog历史隔离 |
| SRC-MINIMAX | 原27行：en12 May26→Mar18、zh13 Apr27→Mar18；AgentTech一项May13；org35止2025 | 三当前Blog索引/组织日界无Apr17，不称历史删除项不存在 |
| SRC-ARXIV | 原14行小时窗不含批次，不可复用为自然日零；本SUP A3/A10四主题＋eval三页/CL-AI相关标题停点 | Apr17常规公告实际包含；有限66及同v1复用/日期例外逐身份处理，不授全分类/无遗漏 |

五机构外部缺口、arXiv未覆盖标题子范围与具名日期例外均不用于正面Coverage或“当天没有研究”。按root要求停止新增Source批次，当前只接已prepared必要Source的独核、具体owner比较及报告合并，不以尚未读完标blocked。

## A20 ADAPT具体owner已有覆盖提案（非Source通过声明）

作者actual读Ch79首节conditionalpolicy/真实observation与尚未查询事实区别、60–62段经验相关性不等statecompatible、161–183的precondition变/plan图不可行vs执行偏差→先修mismatch再决定废弃plan；并读Ch78 executor边界与Ch26反馈/safety交接。ADAPT14902采用的固定goal下stateprecondition检查、暂挂/恢复原action，并不比这些论证新增长期控制合同；单视图affordanceclassifier/Wait/参考图为任务实现、没有新确定性安全/效能保证。拟 `AGENT-PLANNING` Ch79已有覆盖，正面机制只限实际已有conditionalplan与executionrepair分责；报告保固定goal对照/有限模型反侧和2.9倍runtime，不称Books实现了ADAPT。尚待root A16必要Source与本NC实际比较，不自行转已关闭。

## R15 root StreamCache争议、六必要Source与ADAPT具体NC通过

StreamCache15237 root actual §3.1–3.4/Eq3–15、§4.1/Table1–3：排序方向/variance不必变、uniformstd非最大/MVUE假设未验、protected可当merge target与豁免矛盾均实存。6不变，中心统计/保护精确保证争议暂缓通过，有限经验保留不写正面recipe；重开需保护集合更新的可执行定义、统计条件及相应对照，不用一个排版错否定全经验。

root actual必要Source通过：VisPCO15188 §3/Eq1–17/4.1–4.4/Table2–4；Ada15180 §3/Eq6–11/B1、4.1–4.3/Table1、C5/D；ASR14493 §3/5–7.3/Table6；ADAPT14902 §3.2–4/5.5–5.6/Table5–6；SGA14712 §3.3–3.4/Eq3/§4/Table1–2/§5/Table3–4；Sager14972 §2.2–2.5/3.1/Table2–5/3.5。作者各A层的机制/配置/反侧边界通过，不授owner或日级。Ada严格<h/两根unitinterval的singleton反例独立隔离，弱≤h/保守support和refine可分离，不自动全稿争议；ASR平均RTFx非tail；SGA软score非hardgate/MCTS非自动DAG/逐transition认证；Sager tier非概率/无通用100token界均保留。

root actual A20 Ch79 50–68/155–190具体NC通过，不称oracle/Wait已通用安全。当前必要Source定案16（4实际整合/3具体NC/4中心争议/5待owner），FedGUI4只最低关闭另计，prepared及未读部分不虚计。

## A21 四具体已有覆盖提案与Ada局部gap（未授Books）

作者实际读下列当前正文/邻接后，拟NC并保留报告中的各自经验与适用条件，不声称原文算法已经实现：

- **SGA14712 → `AGENT-MEMORY` Ch77**：§“从原始轨迹到派生策略”实际从成功/失败抽procedurallessons→retrieval，并有“子问题—解题过程”局部单元的软提示、多个分支prior及总预算；其后“稳定意图与易变标识”段已有去源ID、保阶段前后条件、当前观测重ground，并由executor持权限。§skillretrieval(200–202)又明确语义分非前置合法。SGA新MCTS获取与softweightedslotranking没有更强verifiedtransition或硬gate证据，不改变这些具体长期选择；报告保离线采集/在线费用与verification上限。
- **Sager14972 → `AGENT-MEMORY` Ch77**：68/82–110的memory类型/readwritepolicy、typedrevise/noop/pending/lineage、derivedsummary非事实；306–329 FactState与Retrieval-policyState分开、workingContextbudget/fallback及独立utility/事实治理；同章proceduralconsolidation保存source/confidence/supersession而非整份覆盖。Full/slim是可派生消费view，置信tier更新不能认证事实或真实用户心理，30token/warmup局部不重写长期memory原则；拟已有覆盖，不冒称已有Sager某个tier算法。
- **ASR14493 → `INFER-TENSORRT-LLM` Ch49**：989–1013量化重构不是原值、group/metadata成本、1005按W/A/K/V与层段不同格式并保较高KV/weightonly、1011静态/动态及weightonly准备责任，配Ch23 437–439/511因果stream仍有边界/缓冲/消费身份与平均FPS非deadline。有限采用分组件精度、保跨chunkstate与协议评估；ASR具体3graph/RNNT是受测实现、未给新增长期cacheauthority。Report保32core与转换缝/ConvInteger反退，不将这些当已写ASRruntime。
- **VisPCO15188 → `MULTIMODAL-REPRESENTATION` Ch23**：721–731固定预算先决定layer/fusion/relevancecoverage配额与删除层，CLASP保FLOP预算/校准人口和完整cost；紧邻离线goldloss搜索mask→traincompressor→deployselector分阶段及费用；745–749跨层压缩位置早晚的节省/敏感度取舍。VisPCO有限新增是配置优化求解分支，localKL/FLOP代理、biasedSTE与jointretention向量未提供更强语义/全局Pareto/墙钟保证，拟已有覆盖该预算/位置/消费者分责，不冒称已有连续优化solver。若root认为具体连续联合预算是未承载长期替代，应仅补该gap，不为便于NC改准入或分数。

**Ada15180明确gap**：Ch49 960–975现有exactTopK与低比特score-histogram只解“选哪些token”，不承载entmax归一化threshold的histroot→原score refine→nonzeroblockmask/反向复用，不能以同名histogram判NC。拟在该完整近似selector反侧后、losslessweightstorage段前两段；先区分替换attentionnormalizer与近似selector，再解释SRAM初始化、refinement/overflow及forward/backward账和模型质量条件。不采用strict<h或两根unitinterval的强界，不声称已有精确safe实现；逐字稿待root gap裁定后提出，不自行写入。

## R16 root 四具体NC通过、Ada gap通过待逐字PRE

root actual读Ch77 675–710/194–205的procedural软prior/去ID重ground/独立执行，覆盖SGA有限采用；80–111/302–330 typedrevise/derivedview与fact-policy/consumerbudget覆盖Sager，不称已有tier算法。Ch49 985–1013 W/A/K/V/weightonly＋Ch23 causalstream有效层覆盖ASR保state/分组件精度，完整费用原已要求，3graphrecipe不另造diff。Ch23 721–749实际layerbudget/离线特权mask搜索/消费预算/位置成本覆盖VisPCO拟采用判断，continuoussolver仅可选实现，不强制加段、不改准入/评分。四具体NC通过。

Ada Ch49 960–984 actual exactTopK/近似selector与entmax归一化求根不是同一责任，gap通过，仅允许两段机制＋strict界隔离；尚未授lease，作者先提出逐字稿。

## A22 Ada15180逐字最小PRE申请

位置：`books/part-05-inference-system/49-tensorrt-llm.md`，现近似低比特Q/K histogramselector完整反侧与SF2604-24820标记后、以“权重存储也可以”起的losslessweight段前；两段＋末尾本人注。已实际读Ch49完整960–984与量化局部、Ch48/50交接及Ch14 Attention基本归一化责任，不把normalizer语义从Ch14重复铺开。

> 稀疏性也可以来自替换 Attention 的归一化算子，而非在 softmax 前近似选 Top-k。采用 entmax 的模型需要求一个使输出权重和为一的阈值；一个执行分支先流式求行最大值，再将有效 scores 的左端点分箱计数保存在 SRAM，用小直方图提出初始阈值，随后回到原 scores 做带区间回退的 refinement。最后产生非零 block mask，用于跳过输出乘法中的零块，并复用到反向梯度遍历。这里改变了模型算子及求根路径，不是原 softmax 的精确 drop-in，也不是只要选择集合内计算精确就保持原模型质量。<!-- source-family:SF-2026-ARXIV-2604-15180 -->
>
> [AdaSplash-2 的有限机制与对照](https://arxiv.org/html/2604.15180v1)仍支付多遍 key 读取、分箱、refinement 与 mask；64-bit、8-bin 的默认计数容量只有16,320个 keys，更长输入需要 flush。左端点近似的严格误差小于 bin width、两根都在单位区间的强称有单活跃项反例，不能据此发布完整数值安全保证；更弱非严格界也不免除实际归一化与质量验收。单 A6000、BF16 的高稀疏 forward/backward 优势不等于低稀疏 forward、更换位置编码后的模型质量或完整 serving 都更好；所测1B模型的 RoPE 配置仍有反退，推理又使用 materialized logits 路径。只有算子质量、计数容量、稀疏率与总费用都合格时才采用该分支，否则保留原 normalizer、常规求根与 dense kernel，不从训练算子加速批准服务 SLO。

本人note逐字：`- SF-2026-ARXIV-2604-15180 — Daily2026-04-18补Apr17；[AdaSplash-2 exact-v1](https://arxiv.org/html/2604.15180v1) §3/Eq6–11、4.1–4.3/T1–3及B1/C5/D必要层，2+2+2=6。entmax histroot/refine/mask与backward复用区别于TopK selector；strict<h/两根unitinterval强界的singleton反例独立隔离，保计数容量、多pass、forward低稀疏/RoPE反退与materialized inference，不授exactsoftmax/全数值安全或servingSLO。root必要Source/date/gap通过，逐字PRE/实际POST待验；未核artifact/复现。`

## R17 root A15通过、机构复用范围通过、Ada实际PRE/POST与分工

root actual通过A15两必要Source：15280 §3.3–3.4/Table1–2/§4.1–4.2/Table3，只11类Ngram相关/双任务shuffle/额外4gapframes，不授架构或attention唯一因果/真实情绪；14520 §4.1/Eq1–7/§5/Table4–8，planner/fallback、PD与PRD训练资格/文本隔离非truth、固定topology/模型prompt反侧和Omni更慢保留。两项可接owner，非Books通过。

root完整实读原V3_REVIEW_CHECKPOINT全部41行及A19自然日14行，身份/窗口未变的原来源检查范围可复用通过。MiniMaxAgentTech只May13当前恢复项不能支持Apr17历史，作者已在正式§1/源表/§5补明确子入口隔离，不压缩成只有五机构。尚非整日Coverage/无遗漏通过。

A22 Ada两段及本人注PRE通过、获唯一Ch49指定窄lease后保存正文976/978、本注3044。root actual POST读969–986完整旧selector→新两段→losslessweight两段＋本人注，逐字一致、限制近文/旧邻段保留，限定diffcheck通过；该lease释放。按root只做本人注POST行政同步，同时纠正本人Prism/Scepsy已R6释放的旧待释放文字，不改任何正文/他人note，不再新造注final循环。

fresh reader `supp_apr18_evidence`只接8既定ID：15306/15224/15302/14338/14375/14870/14525/14790，准入/date有效层复用，必要Source/owner不写SUP/README/Books，作者串录。作者保留互斥8：14648/15308/14314/14641/14463/14602/14477/14925。root接A18 14580/14967及已prepared owner；不追加发现、不重复下载已有效同版。

## R18 A18两必要Source与四定点同v1复用实际通过

root actual读TurboTalk14580v1 §3.1–3.4/Eq1–11/Alg1、4.1–4.3/Table1–4，确认共享参数/final-step stopgrad、当前discriminator denoise的selfcompare，Eq11/Alg1与λ.5对50未统一、futureaudio及NFE非实测速度/反侧完整；有限5可接owner，不授exactrecipe。UniDoc14967 actual §3.1–3.4/Eq1–9/Alg1、4.1–4.2/Table1、§5/Table2–3/6.1–6.2及A2/A3/C/D，search/select/crop、top1pseudo-positive、235B teacher生成并滤final非逐步验真、72B binaryRM、SFT freeze视觉/projector与GRPO费用确认；6标准有限机制通过。同集合filter不增加原召回，SlideVQA跨源去重未核只记限制，不宣称泄漏。均尚待具体owner，非Books通过。

额外四个相同v1实际复用通过：root读Apr17正式原表及连续§4的15022 L374–380、15149 L398–404、14345 L482–486、14877 L582–588。15022/14877最终Only已实际owner反向裁决，不沿历史拟补再写；15149固定H等构双验已Ch31真实POST；14345仅静态已知bias条件，动态var估bias反例隔离。Apr18仅去重，不新评分/候选/Books，不改Apr17冻结内容。

## A23 Seen-to-Scene与RAD-2必要Source prepared（非独核通过）

**14648 Seen-to-Scene，2+1+2=5。** 作者实际读[exact-v1](https://arxiv.org/html/2604.14648v1) §3–6/Eq3–6/Table1–3及B/Table5、C传播/refine/Alg1、D长序列采样；原件 `SUP_CORE_14648v1_20261015.raw.html`。有限增量是以m=4候选窗内灰度SSIM选reference chain，用最近前后参考RAFT/补全flow传播外观到当前latent，再做双向offset refinement；不是语义新信息oracle，也不是因果stream。25帧训练、100K YouTubeVOS样本、100K步/两RTXA6000，仅temporal UNet及flowcompletion等训练，zero-shot只指无逐测试场景FT。DAVIS2017的90段与YouTubeVOS60段、256²、mask .25/.66；Table2 FVD586→355→220.7→218.8支持该有限组合，不分别证明每个外推。Table3 12.109s/8.81GB对M3DDM43.127s/9.63GB与MOTIA373.19s/11.98GB，不是匹配所有训练/逐场景适配和quality成本；推理硬件/precision/steps/重复不确定性在必要层Not Disclosed。

反侧/停点：Table5 m2–7的PSNR/LPIPS/SSIM相同，FVD小差，不夸选链唯一因果；reference数R可随N增长，O(NR)不推出全长线性/常数状态。Eq6跨参考链合成与Alg1逐intermediateframe合成表述不完全相同，不能发布精确执行recipe或“完全不读非参考帧”成本保证。光流完成/生成未见区不是真实场景证据，latent传播会丢细节，输入保真非逐pixel immutable；D重叠窗每步平均预测后全局更新并依赖future，不是在线无限视频。支持与反侧足即停，未读代码/复现/附件视觉。尚待root必要Source及Ch24具体owner差额。

**15308 RAD-2，2+2+2=6。** 作者实际读[exact-v1](https://arxiv.org/html/2604.15308v1) §3.1–3.3/Eq1–18、§4.1–4.6/Table1–10与§5限制；原件 `SUP_CORE_15308v1_20261015.raw.html`。DiT候选生成＋独立discriminator rerank、Hreuse期间复用轨迹、按group rollout std过滤、FIFO8缓冲/每8轮改generator；generator对低回报样本做保空间路径的纵向加减速/重积分再MSE训练，不是直接学完整RL概率密度。BEV-Warp对日志未来BEV按ego SE2双线性warp，固定高度/无pitchroll，不生成他车action-conditioned反应，TTC又用GT futureoccupancy；3DGS亦另训1044/test256场景，不是零样本simtransfer或真实安全证明。50K小时预训、从50Kclips筛10Ksafety＋10Kefficiency、heldout512各类；GPU/precision/训练总时与逐M latency未披露，不能把环境步数曲线称总费用更省。

中心未决：§3.1 Eq8明确直接用各候选独立sigmoid分数（跨候选归一化仅optional），§3.3 Eq16却把新旧sigmoid比当importance ratio；未定义实际选择分布/其归一化常数，entropy亦称policyentropy。即使按p=s/Σs补解释，真实ratio还多Zold/Znew，不能从Eq16认定是已证明合法PPO/GRPO校正；必要主文已无进一步澄清，不继续盲找附件。拟保6、只隔离该correctness主张待root定中心/局部，不抹掉有限经验。Table1 BEV CR .533→.234但Table2 3DGS AF .078略劣Senna2 .077；Table4部分安全训练损efficiency、fullEP@.9 .984低于geneIL+discRL .986；Table5 H8非所有metric最优；Table6 Safety@1 .617→.615不能“无任何代价”；Table10 M64→128 EP .816→.814且Safety@1低于M32，不宣称候选越多全指标单调。未复现/核代码/真人道路安全。

## R19 root四必要Source补足完成层（不预授owner）

root实际读足14867 FCL v1§3–5.3：三反馈级、GPT5nano/10attempt/max10iteration，finite runcoverage不是formal全状态保证，硬件/费用缺不推SLO。14519 CI-CBM §3.2–3.3/Eq3–6、§4/Table5：frozenencoder/每类centroid把新类feature移到旧中心再过currentprojector，三次评估/seed1993；conceptreg-only不保旧class、pseudo依赖好feature/近似几何，非恢复完整旧分布。15037 ProVoice §2–3.4/Eq1/Table1–2：1182合成场景/Qwen3Max+CosyVoice3，trigger FPR/Recall与gated judge回答分验，thinking对ESS并非单调，合成context/LLMjudge不认证实时权限或人类效用。15184 AAD §3–5：JSONlinks/joints/solver/失败render/face-ID、Newton确定性，1动态+5静态demo/4–34iter、scissors4.14h/468calls，只prism/revolute、stuck可restart；无matched因果提升或fabrication验证。四项均5标准必要Source通过，可接owner，不把原mincore门倒记为此前已Source完成。

## A24 DharmaOCR / ASCII / psychological steering / CausalDetox 必要Source prepared

原件分别 `SUP_CORE_14314v1_20261015.raw.html`、`SUP_CORE_14641v1_20261015.raw.html`、`SUP_CORE_14463v1_20261015.raw.html`、`SUP_CORE_14602v1_20261015.raw.html`。ASCII原件下载在AppendixJ长prompt中断，但已含完整§3–6/限制及AppA–I；采用所需层完整，不冒充整HTML成功，也不为无关prompt继续抓。

**14314 DharmaOCR，2+2+2=6。** 实际§3–6.2/7.3/8.1、AppA1/A4：SFT→专门保repetition作为reject的49,170 DPOpairs→AWQ，主采用命题是退化既是质量失败也是共享decode预算风险，DPO为局部缓解而非通用算法创新。39,680页、23,726偏好实例/5response/10pairs；同一235Bjudge选分、原SFT eval并入DPO，benchmark496另列为独立；§4.4又按“benchmarkperformance”选config，保文字资格歧义不擅称泄漏或严隔离。SFT单H200、偏好生成8H200/DPO4H200，推理L40S48GB/vLLM、maxoutput8192。Table1 DPO olm .928→.927/退化1.01→.40，Nanonets .917→.921/1.61→.20，但Qwen3B质量.819→.793；不说所有quality无损。Table2 olm退化写.60与Table1 .40不一，59.4%平均不当可重复普遍值。

AppA1并发30、greedy、vLLM0.15/TP1/maxbatched32000/model65536，observedwalltime与把退化duration替平均值的模拟10.14/3.57/42.47%不能当真实重新调度实验或纯KV因果；活跃退化期间健康请求均值升高是重叠相关、负载/长度未干预隔离。API publicprices vs自托管摊租不是同成本边界，H200把整8GPU价除8假定其余资源可满用，不授普遍52倍降本/SLO。退化判定hitcap且重复，漏非hitcap退化；header/footer重复仍需postprocess，RLVR未来计划不是已实现。未核artifact/复现。

**14641 ASCII/Text2Space，2+1+2=5。** 实际§3–6/限制、AppA/B/C：同一spatialgraph生成text/ASCII/goldanswer，20K合成英文离散2–8节点/1–12relation，test1000；Qwen30B-A3B LoRA4000train/500val、4A40/BF16/r16/一epoch，不是大范围视觉或3D推理。先goldASCII再answer与先自画ASCII再answer的对比表明construction瓶颈：baseQwen30B text75.0、gold83.7、selfdraw-first66.6；read训练不等write训练，construction后text82.2、comprehension73.7，后者StepGame−6.1但SpartQA+44.2，不能概称comprehension无任何迁移。Table3一致子集更准是selection诊断，不证ASCII内部表示/无GT truthcertificate；同一模型两输出可一致地错、双turn提高一致性并非同比提准确。AppB用同Qwen格式对照选grid，预算/输出长度及seedCI未披露，不以训练样本相同声称token/compute matched。无代码/复现，支持与反侧够即停。

**14463 psychological steering，2+1+2=5。** 实际§4–6/Table2–4：centroidunits校准mean-difference向量及fluency终止αsweep，专比Yes/No probe与完整utterance MDS、stride和midlayer，再用GPT5.1 SJT评价。14个1–32B instruct/nonreasoning、>12BNF4，64token completion/greedy；500正500反syntheticstatement，sweepclassifier也训在这批statement embedding上且无SJTstem，存在stylemetric重用；完整utterance vsYes/No也混activationpopulation，不据perfectprobeaccuracy归因真实construct。Table2含ties且先筛有向有效steer再取α/layer极值，末表非未调参泛化保证；MDS没有所有模型胜P2，gemma1B仅一个valid后排，混合PM13/14亦不是普遍可用。§5.3“leakage”实际上平均绝对Pearson相关，不是其他trait每unit移动幅度；不采用该单位解释或从相关得humanpsych结构因果。小幅局部线性/fluency不证明语义任务质量/独立心理人格，其他任务及组合injection未量测；αsweep总硬件/费Not Disclosed。有限采用是控制vector尺度与开放任务评价口径会改变promptvssteer对比，不授普遍控制/安全。

**14602 CausalDetox，2+1+2=5。** 实际§3–5.8/Table1–5/限制、AppG/H/I/J/M，遇correctness信号深入受影响公式。多headactivation VAE32latent proxy、linearGaussian标签模型估PNS下界排名，再global或kNNweighted/shrink局部方向；两fold同budget对比、4种7/8B，ParaTox为Vicuna13B改写ToxiGen/ImplicitHate而非直接原dataset，ParaDetox人rewrite。Table1/T2明确多配置tox降低伴PPL/fluency反退，Mistral18headα5 PPL71.76/fluency.30；人评60样本两人有限。AppH zerohead输出干预有局部支持但无法认证必要/充分最小集或排尽confounder，VAE可重复编码不验证latent因果充分。Eq5文字为lowerbound但式写等号，二元Y套Gaussian回归不自动提供PNS识别。

两具体争议：Eq11最大化预测毒性PNS减KL，不推出无steering即永久unlearning；有限Table3 .2499→.2200不证明概念已删或一般安全。AppG2 Eq12为(1/k)Σ(h_non-toxic[π(i)]−h_toxic[i])，对同一邻域任意置换π完全不变，却Table14声称此置换令.1728→.2482；若实际用Eq8加权/变retrieval，必须另给执行定义，不能把未定义变更当semanticpair因果控制。AppM Table18 base1.3527s/global2.7174/local2.7345约翻倍，与Table17global<1%overhead冲突；27/6=4.5非文字7倍，offlineGPUhours不遗漏。拟保5，中心causalnecessity/permanentunlearning和shufflecontrol安全隔离待root裁定，不以Only隐藏；经验可单独保，不再遍历全部附件。

## A25 Vi-CD与Sparsemax SAE必要Source prepared

**14477 Vi-CD，2+1+2=5。** 作者实际[exact-v1](https://arxiv.org/html/2604.14477v1) §3–5/Eq1–3/Alg1/Table1–2及0.A/B/D/E/F/G必要设置；原件`SUP_CORE_14477v1_20261015.raw.html`。将每head receiver合为attention-input node降低搜索图规模，再用foreground segmentation/inpainting clean-corrupt pairs做逐edge activationpatching/logitdiff剪枝，accuracy另验faithfulness；不是从零构独立子网络，非保留edge仍消费corrupt activations。ForAug每类128个base已答对样本/max900node、perclass threshold按>80%retention选择，主体ViTB/OpenCLIPB32，0.B主类为Imagenette有限切片，不将主文“每ImageNet类”泛成1000类全面验证。0.A末句阈值above剪/below留与§3低lossdrop剪相反，保实现定义歧义、不发布exactrecipe。

有限对比支持较稀疏faithful circuits，但包含逐edge至少一次patch和阈值搜索，EAP/IG同图不等总预算匹配；未披露端到端GPU/precision/费用，不从10倍稀疏推出10倍加速。T1大字ASR39.1→2.8而clean57→55.8，bezel clean57.1→49.9不能“无性能伤害”；T2 revolver R@5/10及Rmean下降不能全recall优。0.D20runs同分布不同128样本，Jaccard/core稳定非跨分布保证；0.E先筛>80%faithfulness再union，只支持该有限两类任务，不证一般composition。0.G matchedrandom/noncircuit对照有机制相关性，但inpainting可能残留/改变OOD，正向faithfulness与directionablation不认证唯一必要机制、无关计算不受损或普遍安全。未读代码/复现，潜在ownerCh5解释/干预而非用Ch66混管。

**14925 Sparsemax SAE，2+1+2=5。** 实际[exact-v1](https://arxiv.org/html/2604.14925v1) §3–4.2/Eq3–7/Alg1/Table1–4及Prop1 KKT证明§6；原件`SUP_CORE_14925v1_20261015.raw.html`。Query为activation，共concept的K/V投影＋simplex sparsemax threshold支持每样本自适应support，不是自动恢复真实唯一concept数或证明monosemantic。排序求τ的Eq7/KKT成立，Alg1分母排版夹z不沿用。CLIPViTB16第二末层、ImageNet训练2,621,440patch/M49152，GPT2small第8层/OpenWebText1Btoken、128seq/M3072–24576；Adam3e−4，baselines用各论文建议K32/λ1e−3。没有匹配每样本/总L0或同参数量/算力Pareto搜索，不能把重构提升完全归dynamicK，更不能称无hyperparameter。

三seed图像11task；class top-n概念来自每个目标dataset训练集按activation频率选，不是无目标类信息的纯zero-shot。Table1 NMSE和Table3结构×激活对照支持有限替代；Table2 CE degradation有负/正值且未完整明确符号定义，TopK部分项比ours更接近零，不照录“所有CE均优”。Table4 K24在Food101部分topn较K32更差，平均support24不是普遍optimalK；allconcept在多task比top50差，概念数更多非单调。低重构/示例patch热图不证明因果语义、可控/安全；硬件、runtime、memory和完整seedCI未披露，不推serving或大模型扩展。当前支持/反侧足，未核artifact/复现，owner需对比Ch5 SAE诊断边界。

## A26 四项已Source通过的具体owner比较（两NC/两最小gap，未授写）

作者重读Books背景/理念/写作、ROADMAP及当前Ch23融合/shortcut/streaming、Ch24fewstep/DMD/sharedreference与Ch75/76相关交接，不按新论文名自动加段。

- **15280 emotion → `MULTIMODAL-REPRESENTATION` Ch23已有覆盖提案。** 实际1233–1247 connector shortcut已有静态cue不能签动态理解、变换应变/不变关系/paired验真、错误变换与额外budget；594完整latefusion已有文本perception不是独立原模态真值，1369顺序监督与当前真正需要历史分开。本文11类Ngram相关不能给预训练唯一因果，双任务shuffle及额外4gapframes/summary的MSCE仍是这些选择的局部验证，不新增长期“多帧必需/attention失效”合同。NC不改5分准入、不称已实现MSCE，报告保具体增量/配置/局限。
- **14967 UniDoc → `AGENT-RAG` Ch76已有覆盖提案。** 实际77–115已有document/query/answer三层分责、queryproposal/候选检索与support另验、结构导航/完整页回退；1276–1290视觉page+regionlocator逐claim链与粒度对齐；1333–1335跨页图/表/文本组合及误剪/回原页。相关consumer Ch23 841–853实际按未决claim提出crop、原图坐标尺度/编码成本、动作监督与answer条件分开。search→select同池只减噪→crop回原图的采用判断已具体承载，dense NDCG/IoU/pseudo-top1只是受测训练选择，没有新增truth/recall保证可填长期gap。拟NC唯一ownerCh76，Ch23仅交接，不冒称已有UniDoc算法或RLrecipe。
- **14520 CoM → Ch23最小gap。** 当前latefusion已有modality perception→文本decision与非独立真值；Ch75 159–169只讲派生state前后次序改变causal reread，Ch76 760–780只讲输入模态支配/独立source检查。都未承载query-only planner同时提出**模态subset、输入serialization topology和是否保留rawsignal给最终consumer**这一联合选择。建议在Ch23原latefusion受限情绪段后/crossattention标题前最多两段：parallel各模态独立调用、sequential有序原模态、interleaved按真实片段交错；PD直接rawinput，PRD最后只消费派生text，二者权限不同。保subset非已知充分、文本隔离非truth、拓扑/prompt/模型反侧/额外调用和fallback，不新增Agentworkflow章或runtime执行器。待root定gap，再给逐字稿。
- **14580 TurboTalk → Ch24最小gap。** 实际927–949 DMD段区分同noisystate的teacheranchor/real-fake-score和rewardtarget；808–811 sharedreference为真实flow适应自产history/stopgradient区间位移，并非GAN同状态的一步输出对当前discriminator少步denoise参考的相对打分；1509直接少steps与另训student区别亦未承载该对象。建议在K-DMD两段后/continuousschedule前最多两段：预训4step再逐级3→2→1、只沿finalstep回传；参考来自当前D的4stepdenoise而非独立frozenteacher，selfcompare与adv共训。保损失系数/Alg1歧义不抄exactrecipe、futureaudio非streaming、NFE非速度、分阶段训练费及质量反退；尚待root gap裁决/PRE，不自行写。

## R20 root五必要Source补足与两中心correctness争议实际闭合

root actual必要Source通过：14762 OmniGCD §3–4/5.1–5.3/Table1–4，frozen各modal encoder→2D/tSNE→synthetic-trained setGCDformer，8000epochs/batch16/max200clusters/3000points、test整组knowntrain+unknowntest transductive；5runs16datasets，old/new反例、tSNE/encoder费用保留，非共享语义空间。14768 CoTEvol §3.1–3.4/Eq3–6/4.1/Table1–4及10，pop4×3iter/k2/temp.6/2048cap，GT correctness+format/lengthfitness→crossover/最高熵step mutation→SFT；6.8%失败fallbackD-CoT，GTfree自评不是真值、LIMO个别输/GPT4.1存在lose，不授无教师。14785 MirrorBench III/IV/TableII，4level镜像body action grounding、IsaacSim1024²/temp0/最少Manhattan步+10，18模型+random/human，同obs/action未控制全部body/可观测性/scaffold；TSR/SIR/FCR/PCR分开，FCR可负、peak非final，不推意识或普遍闭源更强。15114 OT §3.2/Eq16–17/4.4/Table4及C/Table10，offlineOT/Gram拟合RA或dualOA→固定slicedpotentials摊销，Gram/训练人口条件保；2D三任务W2²都差于I-CFM，CIFAR10 OA607+12/RA618.1+16.4s比I-CFM481.9慢而vsOT744.2快，NPE好不能抵消W2/cost，NFE146–147非速度。四项均5标准可接owner，非Books通过。

14486 Tweedie root actual §2.1 A1–3/§3 Eq3.1/Cor1.1/§5Gaussian，5不变而深入受影响证明：A1仅φY=φXφV且明示弱于独立，边际PX可识别不识别jointposterior，Eq3.1却用fV(y−x)而非conditional kernel。reviewer自构反例非论文实验：A/B∈{0,1,2}基joint1/9加ε1/18乘生成函数q=(x−1)(y−1)(x−y)系数，行列和/反对角和均0而joint变；X=A、V=B+独立Gaussian，V有密度/φV离散零、Y卷积边际同而posterior不同。一般dependent posterior强结论中心争议暂缓，不采样器/稳定可实现估计器；Theorem1 pullbackTVnorm的latentfunctional存在及§5明确(X,Σ)⊥V的conditionalGaussian结果可分离保留，不否定经典Tweedie。重开需conditionalnoisekernel或独立等足够条件及相应证明。owner仅Ch24理论接口，无正面Books新写。

root actual RAD15308 §3/Eq8/16–18同意中心importance/policygradient合法性争议暂缓：若argmax无selectionlikelihood，若p=s/Z缺Zold/Znew，optional不补实现；6保，BEV/trajectoryreuse/structuredgenerator经验仅Report，不认证recipe，重开需实际选择分布/执行与正确ratio及相应受控比较。root actual CausalDetox14602 §3–4/Eq5–11、G2Eq12/Table13–14、M/Table17–18同意5中心causal/permanentunlearning争议暂缓，等权shuffle不变和weightedEq8不是同一个实现；重开需实际配对shuffle、因果识别假设验证与FT撤steering后的遗忘评价。两项必要Source独核争议闭合、不写Books正面保证，不称外部访问受阻。

## A27 fresh独立reader八项实际必要Source与owner交付（待root接纳层）

非作者`supp_apr18_evidence`只读指定8 IDs与Books、未写SUP/报告/Books、未占锁；原件各为本目录`SUP_CORE_<ID>v1_20261015.raw.html`。作者按其逐条真实交付串录，不把尚未root接纳标成日级通过。

- **15306 ShortestPath，7深入**：reader actual §2–7/Table1–2、A/D1–2，8层8head、randomwalk1.3Btoken/10Mtraj预训已见train+test地图；unseen仅shortestpath SFT未见。directanswer无CoT，条件两短段正确时长段成功.811→.589是受限递归不稳、MLPprobe不证机制。固定records非token/compute相等；DrGRPO4/8/16rollout最多20epoch/one-multipass未超受测bestSFT，majority/shortest10预算有限不推全部RL/TTC无效；约1%较长数据救30/32或34，length80反退，math7B非全RL/lengthscale复制。建议Ch8 279–285后的spatialtransfer vslengthscale/conditionalcomposition双轴最小gap，未授PRE。
- **15302 JudgeReliability，5标准**：actual §3.1–3.2/Eq1–3、§4、5.1–5.3/Table1–4、§6–7，SummEval30doc×8systems/四judge OpenRouter、pairk3、20随机50/50cal-test。perdoc cycle分布揭aggregate隐藏异质，MFAS三模型不优/GPT.714→.643。splitCP absresidual+全局q/1–5clip仅exchangeable边际coverage，固定q下width又随score离量表边界变化；重复1,918/20split非独立大样本，相关relevance−.01/LLaMAcoh−.03反侧，T1 Qwen/Mistral median1.8%与正文all0冲突。费用含28pairs×3×judge×criterion与calibration，不称免费truth。具体NC提案Ch66 833–864/997–1062 actual perexample切片/相关分母、marginal非conditional、selection与resplit非独立；非已实现cycle算法。
- **14338 PSIG，5标准**：actual §2–3.3/Thm3.2/Prop3.6/Thm3.8、§4/Table1。同直线随机baseline s→CDFG积分权重在可积梯度下Fubini成立，sum=F(x)−E F(b_s)而非固定x0；1/3variance仅零均值delta白噪声/uniform，signal亦改变，不证真实faithfulness/SNR。RiemannO(1/m)需加权函数光滑/有界变差；MC完整IG有内层梯度费。三toy/人工N01噪声/1000trial，非LLM实证；§2 completeness iff忽略积分抵消，准确采用residual=0。Ch5 277–315/337–365尚无该随机baseline/CDF与期望baseline责任，建议最小gap待作者actual/PRE。
- **14375 modularCL，5标准**：actual §4–8/Eq1–8/Table1–4。frozenF→plasticG、student/router参数分离stopgrad、teacherCE阈值warmup；tasklocalbuffer可多epoch，Kbatch稳定再commitfreeze/purge不等DP/无inversion/法规擦除。MNIST99.42是expertretain而mixed约95.54，4096维d12人工manifold非LLM实测；router96.1/203x/145x不是confidence/nocollisionproof，O(N)routers/容量增与forwardtransfer代价保留。softmix不同标签空间zero-padding不自证语义/概率校准，freeze仅参数保持，不保误route。Ch29 984–999/1033–1059尚无teacher-student-router当前session并行→commitfreeze与路由分验，建议gap。
- **14870 curvature，5标准**：actual §3–7/Eq5–15/Thm2、A2/Lemma5。新增1sample的lossfield变化非fittedmodel稳定/泛化，k−2需局部quadratic/顺序minimizer处loss-grad-Hess统一有界，Gaussianunbounded不自动全域成立；topD最优只A2 a=c=0/commonbasis/δ排序兼容，主文Prop3漏排序，不采普遍topcurvature最优。nanochat107M/d6/step3500/FP32/k8、σ≤1e−3局部，1e−2反退。5seed D45 I17.53s/II1.777/GMIII.000122 vsDirectIII2.197，18000x仅III，总19.307对19.727。Ch4 96–142无probinglaw/surrogate/阶段成本区分，建议最小gap或作者actual NC，不先授。
- **14790 crossover，5标准**：actual §3.1–3.3/Eq4/Alg1–2、4.1–4.6/5.1–5.5/Table1–2，genotype为xT和每reverse step独立z_t非预测ε；前tinterp slerp、余步新Gaussian mutation，保存整噪声序列另费。singleclassMNIST/sofa、无attentionUNet/DDPM1000step/4080Super/3000epoch、CMMD选checkpoint，5trials有不显著run，LPIPS/PCA非语义继承/几何truth，图择最高相关、userstudy仅作者；40–50s/10population，latent/DDIM只是future。norm保留需同norm条件；Table2 RefA的负号为hiddenphantom非真实负值，不误抄。Ch24 149–211DDPM无噪声轨迹recombine，建议gap。
- **14525 CrossQuery，5标准**：actual §3.1–3.5/Eq5–13、4.1–4.8/Table1–4、§6。canonical LLMextract→SAT/SMT/core→flip/soften当前或撤旧commit，lexicographic先少改past再label/size；Unknown不commit polarity、SAT只consistentbelief非labeltruth/抽取faithful，soften保label须保修订记录。390case/2450bundles/5–8query、case80/10/10、8breadth/5deep；SC20非同预算，OH1.26–1.58不是免费。T1 Acc.85<SC.86而SetCons.94>.63；§4allmachineverified与4.1仅50case(13%)solver检查其余340人κ.82矛盾，gold资格保留不称全验证；Unk17–19%相近不排abstention贡献。NC提案Ch79 188–211的formalpredicate/solver语义资格/ARGOSjointconsistency非truth，Ch81 106–116 evidence触发/预算/可撤旧为交接，非已有本benchmark实现。
- **15224 JudgeFaking，7深入中心争议提案**：actual §3–6/Table1–5、A/B/E/F/G6–9/I。pool1520/18240/全parse主称与G变n/R1MT少两类矛盾，pairedEq1/N与McNemar同item无法核；QwenHB+WG Retrain8cell均Δ−1.325pp非T5−2.5；V3 JailbrokenDecomm+2.7反everycelllenient；58/72含zero且共享baseline/cell相关，iidbinomial p.5/未校正top5p不自成立，peak−9.8亦非G全表最大。R1temp.6/API按条件batch/retry，缺重复随机化/漂移控制，CORRECTtier非humantruth。ERR0仅五词未命中可见think，不证所有monitor无信号/无意识或preCoT机制。同response同prompt多一句后果令judge敏感可有限报告，不能归有意faking/训练冲突回避。重开需统一逐item配对/漏样分母、重算mean/tests、独立检测敏感度及同条件重复；暂缓不写正面Books，不因费时降分/EX。

reader轻量当前官方abs检查：未见具名withdrawal/correction；14790currentv2Jun30无具体说明，仅14p/7fig/2table，不读取v2/倒灌；其余7所见v1。UnderReview/SubmittedNeurIPS/ICLRworkshop/journalref只发表元数据，不改已核Apr17日门。reader已释放本日只读ownership，root接纳/作者owner实读及PRE/POST另层。

## R21 A26两NC与两最小gap root实际通过

root actual Ch23 shortcut1236–1247/latefusion594与streaming1363–1373，15280具体NC通过。actual Ch76 77–115/1275–1291/1331–1338和Ch23 activecrop841–853，14967具体NC通过，不冒称已有GRPOrecipe。14520 query-only subset/topology/raw-vs-derived最终消费接口、14580 progressive4→1/finalstepgrad/current-D denoise-reference分别有最小gap；root通过gap，仍未授正文写权，作者先给下列逐字PRE。

## A28 CoM与TurboTalk逐字最小PRE申请

**14520**：`books/part-03-multimodal-world-models/23-multimodal-representation.md`原latefusion受限情绪完整段后、`### Cross-attention fusion`前，两段＋本人末注：

> 决策层融合还可以在读取信号之前，先由只看 query 的 planner 提出模态子集、序列组织和后续读取路径。并行分支分别读取每种模态，再汇总各自描述；顺序分支让后面的模态处于前面输入的条件下；交错分支则按实际片段组织音视频对应。这些是不同的输入与消费接口，而不是同一信息的无害换序。直接回答路径仍读取原始模态；另一条分析路径先产生 perception 文本，最终 decider 只消费这些派生描述。Planner 选择的“小集合”不等于已知充分证据，文本隔离也不会使感知描述自动成为真值。<!-- source-family:SF-2026-ARXIV-2604-14520 -->
>
> [CoM 的受限对照](https://arxiv.org/html/2604.14520v1)支持按问题比较这些分支，但部分固定拓扑、prompt 和模型仍更好；增加 reasoning 并非单调收益，Omni 配置的总推理时间还会上升。分角色提示可以复用同一 backbone，却不免 planner、各模态读取与汇总的多次调用；并行阅读只隔离本次输入，不证明跨模态语义独立。应分别保存原信号、片段对应、拓扑与派生描述，验收最终答案和总费用；模态选择漏证、对应失真或文本描述不可靠时，回读原始输入、采用已验证的固定融合或独立感知路径，而不把原文无效规划时的 Audio→Visual 默认次序当通用安全回退。

本人注：`- SF-2026-ARXIV-2604-14520 — Daily2026-04-18补Apr17；[CoM exact-v1](https://arxiv.org/html/2604.14520v1) §4.1/Eq1–7/§5/Table4–8，2+1+2=5。采用query-only subset/topology与PD原模态、PRD派生text消费分责；不授minimal sufficient/truth/全任务或SLO，保prompt/固定拓扑反侧与额外调用、原始输入回退。root必要Source/date/具体gap通过，逐字PRE待验，未获正文写权；未核artifact/复现。`

**14580**：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`K-DMD完整段后、`<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:start -->`前，两段＋本人末注：

> 少步训练也可以先建立四步生成路径，再逐级减少为三步、两步和一步，而不要求一个学生同时适配任意步数。一个对抗训练分支只沿最后一次生成更新回传梯度，前面中间状态停止梯度；这限制的是本次反传路径，不是冻结共享生成器参数。Discriminator 另以自己的少步去噪分支构造参考，并比较参考与当前生成结果；参考来自持续更新的内部模型，而非一份独立、冻结的教师真值。Self-comparison 因此增加的是相对训练信号，不能自动认证目标分布或最终质量。<!-- source-family:SF-2026-ARXIV-2604-14580 -->
>
> [TurboTalk 的必要机制与反侧](https://arxiv.org/html/2604.14580v1)支持这一渐进压步分支，但损失式、算法与所列系数尚有不一致，这里不发布完整可执行配方。初始化蒸馏、分阶段对抗训练、内部参考与音视频条件都计费；比较四步模型直接减少采样次数，也不等于同预算重训的一步基线。部分质量与同步指标会反退，使用未来音频的离线片段不认证 streaming，较少 NFE 也不是实测端到端速度。内部参考漂移、口型或画面质量失配、总成本不合算时，保留已验多步生成、独立教师蒸馏或更多采样步骤，分别验收质量、条件可见性和实际延迟。

本人注：`- SF-2026-ARXIV-2604-14580 — Daily2026-04-18补Apr17；[TurboTalk exact-v1](https://arxiv.org/html/2604.14580v1) §3.1–3.4/Eq1–11/Alg1、4.1–4.3/Table1–4，2+1+2=5。渐进4→1/finalstep梯度/current-D denoise-reference区别于固定teacher anchor；系数/算法歧义不抄recipe，futureaudio/质量反退/阶段训练与NFE非速度近文。root必要Source/date/具体gap通过，逐字PRE待验，未获正文写权；未核artifact/复现。`

## R22 reader八项独核交付root接纳、A28两逐字PRE/保存

root实际读回A27独立reader八项真实范围/反侧/owner提案并接纳必要Source层：15302/14525具体NC通过，15224中心争议终态通过，不授其正面主张；另五gap仍需作者actual owner/PRE。A28两个逐字稿与本人注PRE通过，授Ch23/24指定窄lease，作者仅保存四段与两本人注，实际顺读590–607/923–940及注2182/2842、限定diffcheck零。此刻尚待root实际POST，不把PRE或保存当POST；其余正文/notes与index保留。

## A29 四具体已有覆盖提案（Source层已有效，owner待独核）

- **14867 FCL → `AGENT-TOOL-CALLING` Ch78 NC**：作者actual Ch78 132–140完整simulatedvsrealexecution/tracecoverage与真实测试独立验收；相关Ch79 197–209的parser/solver模型对应、有限verificationnet/criticaloutcome不可通过删行为自签成功，直接承载“metric→细粒度失败/反例反馈仍只覆盖已运行或已编码空间”。FCL countedfinitetrace是受测反馈配置，不给予这些论点之外的新formal全状态保证；10attempt/iteration预算和未匹配费用保Report。不声称已有FCL实现或全域模型检查。
- **14519 CI-CBM → `MULTIMODAL-REPRESENTATION` Ch23 NC**：actual94–96完整conceptlabel/读出版本、concept准确与完整consumer/介入回归分验，已排“小concept loss即任务保持”；Ch29 984–999无旧图像的teacher/visualprototype参考与syntheticanchor非旧真实分布、consumer漂移/回归又直接承接continualsetting。本文Table5 conceptreg-only不能保旧class、centroid平移pseudo只是局部替代实现；未证明恢复旧分布，不为每个pseudo算法新加段。唯一owner选Ch23的conceptconsumer责任，Ch29只作旧参考/continual交接，不声称已有centroid方法。
- **15037 ProVoice → `MULTIMODAL-REPRESENTATION` Ch23 NC**：actual1387–1410完整memory/trigger/runtime权限、watch-out onset/持续未通知/无关/已通知四人口与interrupt/silence监督、交付历史非模型自称、噪声域silence与recall反侧，已经具体区分“什么时候说”和“说得对不对/有没有真实交付权限”。ProVoice新增合成triggerFPR/Recall+gatedjudgeanswer属于该分责的受限benchmark，thinking反退与人类效用未测保Report；不冒称已有其1182cases或实时权限验证。
- **15184 AAD → `AGENT-PLANNING` Ch79 NC**：actual189–203 schema/constraint/outputartifact、确定性只属于已编码约束、render/参数错误仍交付错plan、修复不替原需求/真实代码验证；Ch78 138–140又承载真实执行trace/placeholder与观测缺口及预算。AAD JSONlink/joint→solver→失败中间render/face-ID把可消费观测外化，但单例demo/无matched因果不能新增长期物理安全或fabrication合同。Newton确定性/六demo与4.14h468calls仅Report，拟唯一ownerCh79已有覆盖，非泛以CAD标签排除或声称已实现该solver。

## R23 四新增必要Source、A28实际POST与A29四NC通过

root actual14332 v1§2–7/Eq1–5/Table1–2必要深入：原冻结2+2+2=6，root消息误写5已当即纠正，不改原分。8.1MUNet/10KMNIST两epoch、spatialaverage D64/128/256train64test；equilibria全用精确linearsolve，无物理Langevin/ADC-DAC/完整生成trajectory/质量实测。Eq5仅λmax/(2J2)不足给一般std比，需cov/方向；1/6复合1/2600不可核，cos.9906不证全UNet分布、固定平衡score不自成time-dependentreverseSDE。kBT×128×400为假设能耗，.008J可比A100step/转换/混合费未测、SPICE与mixing仍未来。中心production-scale/10^7能耗保证争议暂缓，有限rankk coupling/数字bias只Report，重开需reverseprocess对应/误差及全数字-转换-训练-混合成本matched硬件测量。

root actual14302 §3.1–3.4/Eq1–6/4.1–4.6/Table1–2：Wan1.3B videoaxis→viewaxis，replicate避4×temporalcodec合view，PRoPEparalleladapter/稀疏SfMQK InfoNCE/LoRA分责；9222synthetic/8304train477test/33views480²/3seed/8A100，GT是编辑model生成非真几何，virtualcam非实测标定。部分无LoRA/无replication PSNR/SSIM更高、CorrAcc.199非保证，50s/3.1min/35min跨pipeline/resolution不授SLO，完整费用保。cached542783/722045bytes中断但必要主§3–4完整，不将无关后附件缺失当阻塞；5标准可owner。14631 actual§3–5/Table1–5：类别/genre再overview-constraints-examples改写，5variants含/不含原题各5共10solutions；11models/105HE175LCB265CF、narrtemp1/code.2，10输出不等总token/calls同预算，openmodels由Gemini产生叙事非selfsolve，T3过滤有效叙事人口/k8–10非原全人口；部分HE/LCB输、组件混变、算法gold由正确输出回译多数非唯一真，AST仅正确子集。5标准可owner，不强写。

14386 actual§3–4/6–8、B/C受影响深入：hedonic owncoalition/percapita maxcap−αkβ，CoalT五步、6agents/200questions×2/temp0/repeatpref3。中心polyconvergence/consistency概率保证争议：Φ每步增不保证增量≥δ，percapita gap非Φgrid；有限partition仅termination不自动poly。Thm2未列A2却证明用potentialgame，singlemax近似无partition归一化不能给γ≥1−exp(−δ/eps)一般下界；Nash概率等式漏非consistent但stable，p^O√n不等O(1/√n)。5保，局部CoalT73.2/heterowelfare更高而Nash更低仅Report，重开需实际potential增量/复杂度及完整概率条件/证明，不否定全部hedonictheory。

A28 root actual POST读Ch23 590–609/两新段596/598/注2182及Ch24 923–941/两新段929/931/注2842，逐字一致、限制与旧交接保留、限定diffcheck零；两指定lease释放，作者已仅行政同步本人注。累计7实际整合，不新增行政final循环。A29四NC root actual具体局部比较通过：FCL Ch78 128–140+Ch79 197–209；CI-CBM Ch23 94–96+Ch29 984–999；ProVoice当前Ch23 1398–1408；AAD Ch79 schema/solver/render分责。所有NC非声称已有该论文实现，不改准入分。

## A30 ShortestPath / PSIG / modularCL 三最小gap逐字PRE申请

作者actual读Ch8 264–292原子事实/bridge与probe条件；Ch5 277–318证据阶梯/因果patch、337–369replacement/SAE预算与相邻Ch4/6交接；Ch29 980–1004/1031–1062 trainablesubspace/无旧imageanchor/forgetting和Ch28/30交接。以下不同长期责任尚未承载，不自动把reader五提案全改写正文。

**15306 → `WORLDVIEW-LLM-INTELLIGENCE` Ch8**，原atomic/bridge与probe完整两段后、`## 自检问题`前：

> “换一个环境还能答”与“组合长度变长还能答”应作为两条独立的泛化轴。在受控最短路径任务中，可以保留地图拓扑、改变路径长度，或固定长度、改变用于最短路径微调的地图；再只看两个短子路径均已答对的实例，检查模型是否仍能给出对应长路径。这样能把基础局部能力与更长组合的行为失败分开，却不能由失败直接定位某个内部电路。所谓未见地图也必须注明相对哪一阶段未见：随机游走预训练已经接触该地图，不等于微调外地图是模型从未接触的环境。<!-- source-family:SF-2026-ARXIV-2604-15306 -->
>
> [最短路径的受限对照](https://arxiv.org/html/2604.15306v1)中，条件长路径成功率随长度从0.811降至0.589；受测 RL、十候选投票或最短选择没有突破最佳 SFT，并不证明所有奖励学习或测试时计算都无效。加入少量较长训练样例可以改善长度外推，过长样例又会反退；固定样例记录数也没有控制总 token 和 compute。应共同记录预训练接触、微调支持、条件人口与完整训练/搜索预算；长度外推失效时，保留更长监督、外部搜索或可验证图算法，不能把空间迁移分数当作可无限复用的组合程序。

本人注：`- SF-2026-ARXIV-2604-15306 — Daily2026-04-18补Apr17；[ShortestPath exact-v1](https://arxiv.org/html/2604.15306v1) §2–7/T1–2/A/D1–2，3+1+3=7。空间迁移与组合长度双轴/conditionalcomposition；预训已见test地图、MLPprobe非causal、RL/TTC有限预算、长监督反退和record非compute匹配近文。独立reader必要Source/root接纳与date有效，作者actual owner比较，逐字PRE待root；未核代码/复现。`

**14338 → `WORLDVIEW-REPRESENTATION` Ch5**，原DRTC完整段后、`Jacobian-adjusted lens`段前：

> 梯度归因还可以改变基线的人口，而不把噪声更小直接当作更忠实的机制解释。沿同一直线写出 `b(t)=x₀+t(x−x₀)`，若基线位置为随机变量 S，其累积分布为 G，在路径绝对连续、相关梯度可积时，平均路径归因可写为对梯度积分加权 `G(t)`。各维归因之和对应 `F(x)−E[F(b(S))]`，不再是相对一个固定 x₀ 的差；基线分布因而属于解释对象的身份，不能改变它后仍声称回答同一个 completeness 问题。<!-- source-family:SF-2026-ARXIV-2604-14338 -->
>
> [PSIG 的有限理论与 toy 对照](https://arxiv.org/html/2604.14338v1)在均匀基线、零均值白噪声模型下给出方差缩减，但权重也改变信号，不能推出真实模型解释更忠实或普遍更高 SNR。数值积分误差还取决于加权被积函数的光滑性或有界变差，重复完整 IG 的基线平均则支付内层梯度预算。应分别验收归因残差、随机/基线敏感度与原模型上的行为干预；条件、梯度预算或任务解释不匹配时，保留固定基线 IG、其他合适基线与 activation patching，不以较平滑热图取代因果证据。

本人注：`- SF-2026-ARXIV-2604-14338 — Daily2026-04-18补Apr17；[PSIG exact-v1](https://arxiv.org/html/2604.14338v1) §2–3.3/Thm3.2/Prop3.6/Thm3.8、§4/T1，2+1+2=5，理论接口gap必要加深。随机路径baseline/CDF权重与期望baseline残差；白噪声/数值正则条件、信号变化和gradientbudget保留，不授LLM因果faithfulness。独立reader必要Source/root接纳及date有效，作者actual owner比较，逐字PRE待root；未复现。`

**14375 → `TRAIN-SFT` Ch29**，trainablesubspace完整段后、`#### 无旧图像时，保持监督与旧读出须保存不同参考`前：

> 若必须减少已提交模块被后续更新破坏的机会，另一条持续学习分支可以冻结共同 feature extractor，把当前任务的 plastic teacher、蒸馏 student 与识别适用输入的 router 分开训练。当前 session 可用局部 buffer 重复学习；达到规定稳定条件后，再冻结 student 与 router、释放这份临时数据。冻结保护的是这些参数不再被未来梯度改写，不能保证输入被正确路由，也不表示临时数据从未重放、参数不可反演或满足法定删除。<!-- source-family:SF-2026-ARXIV-2604-14375 -->
>
> [模块化持续学习的受限对照](https://arxiv.org/html/2604.14375v1)支持把 expert 保持与混合 stream 的路由准确率分别验收，而非只展示每个冻结 expert 在自己任务上的成绩。已有模块、router 数量与选择成本仍会增长，隔离又可能牺牲跨任务迁移；不同标签空间的 soft mixture 也需另验语义与概率校准。其数字任务和人工高维流形不认证真实 LLM 的开放任务边界。适用性误判、容量或总预算失配时，保留显式任务标签、可信 replay、独立 adapter 或重新适配共同表示，不让冻结状态自签整体无遗忘。

本人注：`- SF-2026-ARXIV-2604-14375 — Daily2026-04-18补Apr17；[modularCL exact-v1](https://arxiv.org/html/2604.14375v1) §4–8/Eq1–8/T1–4，2+1+2=5。teacher/student/router与commitfreeze分责，局部buffer非不重放/DP，expertretain非路由保持，容量增长/forwardtransfer与labelspace混合边界近文。独立reader必要Source/root接纳与date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

## A31 Curvature与Diffusion Crossover两最小gap/PRE申请

**14870 → `WORLDVIEW-WHY-MODELS-LEARN` Ch4**：作者actual Ch4 96–146梯度坐标/连续近似/EdgeofStability与minibatch、Ch5诊断阶梯及Ch3知识树/Ch28训练交接。现有讨论是优化动力学/step稳定，尚无“新增一个样本造成lossfield变化”的测量对象与surrogate分账。拟在`<!-- semantic-body-binding:SF-2026-ARXIV-2606.15551 -->`后、minibatch段前两段＋本人注：

> “局部更平”之外，还可以诊断新增一个样本会让当前解附近的损失函数场改变多少。一个受限方法在给定扰动人口上比较相邻数据规模的经验损失变化，区分直接 Monte Carlo 估计与局部二次代理；梯度、Hessian 和扰动协方差共同决定读数。它测量的是 loss-field 对数据加入的敏感性，不是重新优化后模型参数、测试误差或实际训练过程已经稳定；样本数、中心位置、扰动尺度与协方差必须随诊断一起记录。<!-- source-family:SF-2026-ARXIV-2604-14870 -->
>
> [曲率对齐 probing 的必要边界](https://arxiv.org/html/2604.14870v1)包括局部二次近似及导数、损失的统一有界条件，不能把 Gaussian 扰动直接当作全域保证；优先取最大曲率方向也需要相应变化方向的排序与共同坐标等条件，不是普遍最优子空间。受测小模型在较小扰动下可用，增大扰动会反退。解析代理的末阶段可以极快，却仍须支付梯度、Hessian 子空间和代理构建；约18,000倍只比较该末阶段，不能替代完整诊断总耗时。假设或读数不稳时，回到直接扰动、实际 loss/gradient/step 监测与较小邻域，不由这个 sensor 批准更大学习率或更好泛化。

本人注：`- SF-2026-ARXIV-2604-14870 — Daily2026-04-18补Apr17；[curvature probing exact-v1](https://arxiv.org/html/2604.14870v1) §3–7/Eq5–15/Thm2、A2/Lemma5，2+1+2=5。新增样本lossfield非fittedmodel/generalization，局部quadratic/导数界、topD排序限制与三阶段成本近文；不采全域/普遍最优或18000倍总加速。独立reader必要Source/root接纳与date有效，作者actual owner比较，逐字PRE待root；未复现。`

**14790 → `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24**：作者actual DDPM149–194 sampler的xT/逐步z、203以后conditioncache与Ch23/25交接。已有噪声初态/variance配置，但没有将整份采样随机性作为可重组artifact，故不是普通seed插值同义。拟在DDPM采样配置完整段后、`噪声还可以按空间位置分配`段前两段＋本人注：

> 要重组两条随机采样结果，控制对象还可以从初始 seed 扩展为完整噪声轨迹：保存初始 x_T 以及每个反向步骤新抽取的 z_t，逐步混合两份记录，再交给同一 denoiser 与 schedule 重放。这些 z_t 是采样器注入的独立随机量，不是网络预测的 epsilon。一个可调分支只在前面一段反向步骤插值两份噪声，剩余步骤重新采样，因而把保留父代轨迹与产生新变化的区间分开；保存、传递和重放整份噪声序列也增加状态与计算。<!-- source-family:SF-2026-ARXIV-2604-14790 -->
>
> [Diffusion Crossover 的受限对照](https://arxiv.org/html/2604.14790v1)在单类 MNIST/sofa、无 Attention 的 U-Net 与千步 DDPM 中观察到插值参数和感知相似度的关系，但有不显著的 runs，LPIPS/PCA 不能认证语义属性继承或真实几何。球面插值的方向与范数条件也不能提升为任意输入下保 Gaussian 分布的保证。每十个样本约40–50秒的局部配置不证明低延迟，latent 或 DDIM 加速仍是未验证的扩展。混合后质量、多样性或总预算不满足目标时，保留独立噪声采样、普通初始 latent 插值或更多可验候选，而不让“进化重组”名称替代最终生成质量验收。

本人注：`- SF-2026-ARXIV-2604-14790 — Daily2026-04-18补Apr17；[Diffusion Crossover exact-v1](https://arxiv.org/html/2604.14790v1) §3.1–3.3/Eq4/Alg1–2、4.1–4.6/5.1–5.5/T1–2，2+1+2=5。xT与逐步z重组/区间外resample，非预测epsilon；有限singleclass/LPIPS非语义、部分run不显著、norm条件和完整采样费近文，不倒灌Junev2。独立reader必要Source/root接纳与date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

## R24 A30实际POST、root另五必要Source定案

root actual A30三POST：Ch8 279–298/新287/289+注386；Ch5 300–321/新306/308+注706；Ch29 984–1008/新993/995+注1582。逐字一致、原机制/交接完整、反侧近文、限定diffcheck零，三窄lease释放，作者只行政同步注、不多造final。A31两逐字PRE及指定窄lease通过后，作者保存Ch4 138/140+注454和Ch24 195/197+注2848、actual完整邻接读回/diffcheck零，此刻POST待root，不能预计。

**14646 UEC，5争议**：root actual§4/Eq/Alg1、§5–7/Table1–2、B。初G5无正reward定义hard而非固有difficulty，扩G20/temp1.2仅正adv、5120replay每5步；8A80040G/max8192/b512/单trainingrun、各benchmark所有checkpoint取最高，32AIME采样非32训练seed。MathVision28.82<GRPO29.11/QwenMinerva35.7<base47.3、Geometry55.41对50.75非摘要37.9relative；step.79不含matched总trajectory/同质量时间。Thm4.2正adv样本logprob增不保证entropy降，binaryp .2→.3反例；Thm4.1 naturalgradient一阶非实际clippedGRPO全局稳定证明。Alg1 OH>0对正文≥0、queue仅hard对正文regular+hard不一，不抄recipe。中心entropy/convergence保证暂缓，有限扩采/replay经验Report；重开需概率/协方差充分条件、实际算法定义与受控多run对照。

**14698 MFPO，原6标准必要Source通过**：root actual§4.1–4.4/Eq9–30、5.1–5.2/Table1、8.4Eq51–56、§10/Table2。MeanFlow action＋learnedaveragedivergence(Hutchinson/JVPtarget)供近似likelihood，Gaussian/currentpolicy两SNIS proposal按ESS混合；finiteT非exactODEflow、ADN不自动finite-map exactdensity；finiteSNIS biased/ESS非任意integrand方差、estimated随机mix不继承fixedα独立最优证明，MF目标投影只假设接近KL，不采全局softPI收敛。RTX3090/Xeon8280、5MuJoCo+6DMC/5seed/b256/3×256/UTD1/replay1e6；T2 MFPO2step/10candidate .46ms慢于TD3 .14/SAC .15，FlowRL1step实际2NFE，部分baseline作者JAX改写不等全实现budget相同，ADN约5%training和dualproposal/critic/Qrerank费保。不倒灌v2Humanoid、不授真实robot。

**14655 AgentGA，5标准通过**：root actual§3.1–3.5/Eq1–3、4.1–4.5/Table1、§5。外层任务operator+可读parentarchives选seed/freshworkspace，内ReAct，1:1slot子代对elite非直接codeGA；modifiedHedge rank/clip/probbound不继承regret，Jumpstart本测prob0。KimiK2.5/elite5/30itercap/patience5/每调用5实验；16competition仅10完成，privateLB均值非16总体/与AIDE不同modelcompute，Initial12.2对parent48.7混adaptive时序/父质量非随机inheritance因果。15m10s/1.87Mprompt/34252completion只单例、全部CPU/LLM/archive费保，无零泄漏/未来泛化保证。

**14709 HWE，5标准通过**：root actual v1§3.1–3.3/4.1–4.5/Table2–4。>30KPR→417/sixrepos、baseFAIL/patchPASS+LLMscript/humanreview、去泄漏problem、Docker/EDA/tests；VCS245商业license、Verilator仅172子集。7model各CLI/OpenHands不同/Qwenpilot择强framework，6h/500iter是wholeagent非裸权重；GPT295/41770.7、fileprecision .619不单判正确性，额外artifact可能合法/GTfiles非唯一。PASS非全ISA/物理安全，schema/HJSON/generatedcollateral有限失败诊断非全sample因果，SWE异协议不能matchedhardware横比。API估价非订阅实账/完整EDA+CPUwallclock，未核artifact/复现、不读v2/v3，不新增硬件专章。

**14724 HAMSA，5中心强保证隔离提案**：root actual§2.1–2.2/Eq1–8/Thm1、§3.1–3.6/Table3–7。fixedcomplexkernel FFTmix+input幅度gate/SAGU非inputconditional boundedcausal recurrence，L/网格绑定参数；Eq2实际Tustin非ZOH，fixedN SSMkernel集合不因嵌入C^L而成线性子空间，StoneWeierstrass/complete/separable不保证gradient任意ε收敛。Eq5/6全L×Lgate矩阵不由FFT项O(LlogL)授总复杂度，complexW2/magnitude/realgate接口未统一。224²vision/3run/V100、tokenlabel额外监督/不同params与跨paper对比，S4.2ms28M对§3.6 5.1ms15M、throughput与b1latency非互逆、energy12.5J无measurementwindow；部分baseline更准，不能移除scan唯一因果或统一SLO/energy。作者拟中心收敛/总复杂度/性能暂缓，不以Only埋掉；有限FFT/gate经验仅Report，重开需完整gate定义、函数族/优化条件及全成本matched测量，不授LLM SSM替代。

## A32 两具体NC与Sparsemax SAE最小gap/PRE申请

作者actual Ch5 247–277 steer方向/context/范数与输出KL分责，277–320证据阶梯，343–384 explanationreplacement/完整路径、域内faithfulness/受控patch、SAE重构与稀疏/外部一致性/null；Ch4/6接口按原owner边界。

- **14463 psychological steering → `WORLDVIEW-REPRESENTATION` Ch5 NC提案**：247–265明确方向、层、token/context/强度校准、范数不=输出KL、probe可分不等同方向控制/独立行为评价；277–302又有构念标签和干预混杂。本文centroidunits与sweep/开放SJT相对prompt的有限反转不提供更强校准概率或无损心理控制，现有论证已承载为何probeaccuracy不能决定steer、几何参数和评价人口需joint验。保具体新经验/成功极值选择/同statement classifier及相关非movement于Report，不冒称已有其αsweep算法。
- **14477 Vi-CD → `WORLDVIEW-REPRESENTATION` Ch5 NC提案**：343–360明确explanationreplacement的pruning/reconstruction/未替换路径预算、输出约束门控与corruptpatch另验、有限输入域证书不等唯一mechanism、路径/竞争重算；319局部edge完整路径/retainremove又表明单faithfulness非唯一必要。本文receiveraggregation是搜索图实现，foregroundinpaint/已答对人口条件与更稀疏电路经验不推独立子网或全域causal安全；其有限采用命题已具体承载，Report保bezel/T2反退/费用，不声称图压缩已实现于书。

**14925 Sparsemax SAE → Ch5 gap**：当前343–384讨论replacement预算、外部/内部dictionary正则与null，却未解释**共享concept K/V读出+simplex动态support**作为固定TopK的具体架构替代；Ch14拥有normalizer定义、Ch49拥有kernel，不能在此重复求根/实现。拟在完整“干预目标本身也要保留算子的竞争关系”段后、`重构与稀疏目标合理地要求 dictionary`段前，两段＋本人末注：

> 稀疏 dictionary 也可以改变读出结构，而不只调整固定 Top-k 或稀疏惩罚。一个替代分支把原 activation 当作 query，让同一组 concept vectors 分别经过 key 与 value 投影；query–key 分数经 sparsemax 投到 simplex，再用所得稀疏权重重构 activation。每个样本的非零 support 随分数变化，取代预先指定相同 K，但 concept、投影、尺度与训练预算仍是模型选择。这里得到的是一份受约束的解释用重构，不是测出了真实、唯一的概念数；归一化定义归第14章，执行代价归后续推理章节。<!-- source-family:SF-2026-ARXIV-2604-14925 -->
>
> [动态 sparsemax SAE 的有限对照](https://arxiv.org/html/2604.14925v1)在 CLIP 和 GPT-2 Small 上支持这一重构分支，不能由较低 NMSE、分类或可视化结果认证 monosemantic 因果。不同方法尚未匹配实际 L0、参数量与完整计算预算；按目标数据训练集为各类挑概念，也不是完全无目标信息的 zero-shot 评价。更多概念或把平均 support 作为固定 K 都有反退，CE 指标口径亦不能概括成每项无损。应同时检查重构、稀疏覆盖和原模型行为，计入额外投影、归一化及训练费用；质量或覆盖失配时，保留固定 Top-k、普通 SAE 和独立 null/干预对照，不让动态 support 自签解释真实性或安全控制。

本人注：`- SF-2026-ARXIV-2604-14925 — Daily2026-04-18补Apr17；[Sparsemax SAE exact-v1](https://arxiv.org/html/2604.14925v1) §3–4/Eq3–7/Alg1/T1–4及§6KKT，2+1+2=5。sharedconcept K/V+simplex动态support区别固定TopK，gap必要加深；未matchL0/预算、targetclass选concept、CE口径/更多support反退近文，不授真实concept或causal安全。root必要Source/date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

## R25 A31两实际POST通过与行政同步

root actual Ch4 132–149/新138/140+注454、Ch24 188–204/新195/197+注2848，逐字一致、完整上下旧机制/交接/反侧保留、限定diffcheck零；两指定窄lease释放。累计12实际整合。作者已仅同步A30三本人注及A31两本人注行政身份为实际POST通过/锁释放，随下一次DAY读回，不另造final循环；正文及他人notes不变。A32正文尚未获写，14463心理项ID在正式均正确，早期消息14563为行政手误不形成候选/评分。

## A33 fresh独立reader最后十项必要Source/owner真实交付

`supp_apr18_evidence`按root互斥最后10重读Apr18合同/本SUP后执行，不继承刚工作的Apr21材料；每项精确v1原件在本目录`SUP_CORE_<ID>v1_20261015.raw.html`。15153/15128/15063/14989/15001/14751前六必要层root已actual读回接纳，无第三人重复全文；余四以下按reader真实交付，待root接纳汇总，不预支owner/PRE。未写SUP/报告/Books/index。

- **15153 K-Token，5标准**：actual§3.1–3.3/Eq1–2/Alg1、4.1–4.7/Table1–3/Fig5、§5/限制。固定连续K原embedding均值+nearzero residualMLP成一softembedding，encoder与LoRA reader联合输出loss，generation仍原token不压新输出。Qwen2.5-.5B/LoRAr4α16/三任务；Tree19.6–34.6M辅助curriculum、不同方法预算，三次只best。K4输入−75%而Tree98.38<99.97/Amazon91.05<93.54/codePPL1.391>1.293；自定义P-LF1把未压baseline定义为0不当系统优越。50MBencoder/训练/Kgramcache另费，无完整latency/HBM/throughput/SLO，硬件precision ND，不授大模型/递归。actual Ch22 300–346/1184–1223、Ch75 217–219/295已softobservation与adaptedreader预算，但Ch22 328–332离散码重构解码无固定K连续输入/输出不压责任，建议Ch22最小gap，不自动NC。
- **15128 SCENIC，6标准**：actual§4–7/8.1–8.6/9.1–9.2/Table2/Fig4–11/§10。RoCEQPN/TCPFlowID→FPGA SCUfaststream、mandatoryslowpath与Arm离线控制/聚合snapshot分开，Linuxnetdev/rdma-core、GPUdma-buf和地址翻译；200G MTUpacket167ns非CPU逐包。8ms重配置/预载双CC才藏切换，非全部切换无扰动；100/200G switchedmicrobench、4nodeBCAST/GATHER非大模型训练，gradientcompression future。PCIe20GBps低23–25且READ未解、ASIC部分lat更好、netdev关TSO/GRO、synthetic双列hashpartition有fixedoverhead/大集分batch，4flow公平非任意QoS/tenant无timingchannel。NICACK不等GPUmemorycontroller可见，作者另pollGPUcontents才验吞吐。全FPGA/RTL-HLS/bitstream/TLB/driver/Arm/reconfig费用保，precision/appSLO ND。actual Ch36 208–249 endpoint/collectivecompletion/网络进度有相关论点，但streamfast/slow/Arm及NICACK非GPUvisibility需最小gap，建议MTIA完整段后。
- **15063 VGIA，5受影响深入/中心争议**：actual§3–6/Eq2–14/Prop4.1/Alg1–2、AppA全证明、B1–B3/Alg3、C1–C2/D1/Table1。maliciousserver改全发放参数但架构/activation固定，FCReLU/跨轮同fullbatchFedSGD/featurebounds/线性独立/导数非零强假设；共同active梯度相减/biasratio条件代数不证明singletoncertificate。反例为reviewer推断非论文实验：x1=(1,0),x2=(0,1),w=(1,2),labels0，旧threshold0/3/4、新0/2.5/3；两样本都仅激活threshold0，output=u_t*p，共享positiveabscontinuous lastweights令两β跨轮比恒u_new/u_old，即使输入线性独立/导数levelsetnull，唯一slice新旧共线仍错签singleton，重构(1/3,2/3)非原样本。AppA单β连续不推出共享随机下ratio不等。实验FCN1000/100hidden/ACS2048/3seed/double/1e−9阈值，作者11恢复/12验证对CTP20非所有轮优，CTP前2–8轮更多correct；FedAvg n1024/30round、128/256/512batch实际有803.7correct/182FP。多轮通信/恶意发放/重算线代费、硬件时间ND，DP/secureaggregation/Transformer均future。Ch72 174–191已威胁主体/经验恢复与DP证明分责，无正面Books；重开需联合非退化假设、span充分性/数值误受界与目标defense验证。
- **14989 DrRTL，5标准/NC提案**：actual§3/4.1–4.2/Eq2–5、5.1–5.6/Table2–4/Fig5–6、6.1–6.3。parent/同timingfeedback下候选score组内标准化→patternstrategy/SECpass与相对收益的skill；20原humanRTL/avg812LOC、DC+Nangate45nm/.1ns/JasperSEC、10iter×5=50attempt、4fold15train5unseen并reset。avgWNS21.3/TNS16.9/area−5.8但3/20area升；消融支持有限loop非同token/tool/离线skill费，SEC只ref/编码约束，不能“防全部hallucination”；score更低好/Eq5符号不抄recipe。20design约一周/$50LLM非EDA总费，license/hardware/checkpoint/precisionND，Yosys/DC/postroute不能混保证。actual Ch79 225–239 parentID/feedback/外接受与预算，Ch80 192–214 reflection派生权限，建议Ch79具体NC，不冒称已有47skill/Zscore。
- **15001 COEVO，5标准/gap提案**：actual§3/Eq1–3、4.1–4.3/Eq4–9/Alg1、5.1–5.5/Table1–3/Fig2–3/§6。testfraction c与A/D/P四维Pareto，survivalthreshold .25→1使partialcorrect候选留在sandbox搜索，不等部署准入；generationθ1只当前tests全过，非formal语义证明，Algreturnfront仍另验。156/50tasks、4OpenAI+Qwen7B、N10/offspring10/G10/repair3、10independentsearchruns，Pass@1是完整搜索后最终非一次sample。Yosys/OpenSTA/Nangate45nm，43/49bestproduct含ties/分量反退floatdelay3.47>2.32/asynfifo全败；4DNDS→weighted+binary混变、nofilter≠strict1，增强testbench43vs48显coverage重要，不能宣称strictgate单因果。无总token/EDA/时间硬件precision，trainingfree非searchfree。actual Ch79 225–239旧incumbent合法门未承载隔离population存活门，建议只补searchsurvival≠finalcommit，不推翻旧outercorrectness。
- **14751 FL correlations，5标准/gap提案**：actual§II、III–V必要测量、VI/VII Alg1–2、VIII A–E/TableII/Fig4–8。测reshape结构/时间history/空间client相关，AdaSVDFed每Tu选SVD或residualpredict/PCAFed共享basis；server从当前完整update学basis仅后续轮可用，空间收益也依赖时间稳定，basis/mean/history下行维护另费。LeNetMNIST/ResNet18CIFAR10/linearw8a、20client/τ32/nonIID≤4/10label/10runsstd，不同层reshape无统一最优，多localsteps降时间相关。TII ResNetIID无压87iter38.81B元素、PCA105/34.26B、Ada122/37.27B、SVDFed185/81.42B，压缩可翻倍总通信；元素数非linktime/硬件precision，PCAFedRemarkVII1自认计算不实用。j≤2π/θ不保cos正下界、IV Eq13非PSD小denom不任意保持序，不采强保证。actual Ch36 831–858/1440–1456已有stalesupport/errorbudget/encodecriticalpath，建议basis仅nextiter+下行refresh摊销最小差额，非同压缩即NC。
- **14920 DualAxisRM，5标准/NC提案**：actual§3.1–3.3/Eq1、§4–5/Table1–3/限制、A1/T4/D1–2/T5。正式增量窄纠正：Rθ=(CoTsem,CoTturn,S)是两诊断CoT+单binaryAND总分，两个独立rewardchannels在限制写future；GRPO训练evaluator而非SDMpolicy。Qwen2.5Omni7B两SFT+GRPO(K4/format.5+labelacc.5)，Gemini2.5Pro metadataCoT2670、6361synthetic146h+100HH289HM、ID273/OOD233/RWHH53/RWHM44、FG40；syntheticOOD非现场。HM无realGRPO56.82低SFT72.73、加real77.27，HH83.02<84.91，非RL普遍增泛化；40snippethumanCoT4.125/55%偏好不证faithful。4H20/96GB、GRPOLLM-onlyfreezeencoder，precision/总费/时延ND，teacher/TTS/多阶段训练全费。actual Ch66 99–139 binaryverdict≠taxonomy/EvalSpec/peraxislabel来源，Ch23 1387–1425时间/真实交付交接，建议Ch66具体NC不声称已有双独立reward或runtime。
- **14973 perturbrobustness，5标准/NC提案**：actual§2–3/Eq1–10、§4–6/Fig3–7、AppC证明/Table9。归一embedding扰动集合minimumenclosingball radius，Rcos/Rdist单位球sqrt等价、Rdr五公理是定义性质非真实worstutility。连续域抽5点/仅CLIPJPEG近饱和不证明全continuum；Welzl把d视常数不推高维免费线性。6CLIP/DINOv2/9perturb、ImageNet/Food101/NYU，scale趋势反向不识别视觉架构因果，局部半分回归不授新head/扰动校准。T9 λ0 radius.01但cleanACC.16%，λ1 .06/67.99、λ5 .07/68.31，utilityanchor防collapse；20KImageNet/JPEG50epoch/lr1e−5/全扰动encoder+ballsolver费，硬件precision/CI/总时ND。actual Ch23 87–104跨consumerloss/概念metric/fullconsumer分验、Ch66 99–139/151 proxy另验，建议Ch23具体NC，不加Welzl算法段。
- **15294 viewpoint，5标准/NC提案**：actual§3.1–3.2/4.1–4.2/5.1–5.2/Eq4–6/Fig2–4、§6/T2/限制及D/F/I1–2/J。19,591textonly合成2–5步/直角orientation/100objects+unknown，不证真实3D感知，VLM/LLM训练混变。lastnewlineprobe方向/角度>99不等orientation正确使用；clean/corrupt flip最后direction、滤sameanswer、logitdiff归一/随机head消融只支持局部输出贡献，不定唯一binding电路，分母近0敏感；unknownhead65.78→40.73不证安全对齐成因。32heads另19,641train/1epoch/Adam2e−5/B32/Hh缩grad；7BVRU78.7<full96.3/Spin48.4>47.3/BBH48.4<base49.2，无random32FT对照，2A80080GB/11vs5samplessec与50%GPUh不含完整probe/pathsearch。actual Ch5 38–72/272–303 decodable-vs-used/rule-state及干预连带，建议Ch5具体NC，head命名非真实通用机制。
- **15267 CoopEval，5标准/gap提案**：actual§2–3.2、§4Thm1条件、§5协议、§6/Table2/RQ1–6、§7/Impact及C grimtrigger/finitehistoryLemma。repetition/reputation改变可见history与未来互惠，mediator delegation/contract真实改payoff是环境承诺非口头话术。finitegame/ParetobetterthanNE/足够δ仅cooperativeequilibrium存在，不排坏NE/不保证LLM选择；finitek只NE。6config/4finitegame/temp1/概率外部sample、每组合3repeat/k3δ.8、15round再discount非真实infinite。T2 .072/.587/−.321或+.227/.695/.801是normalizedpayoff非合作成功率；Fitness冻payoff跑1000replicatordynamics非在线LLM训练，uniform与evolutionrank会反转，高阶history更差/小kδ可更好/某contract失败。rationale15类GPT5.2judge不证真实动机，>50Kdecisions非独立部署人口，无matchedcalls/token/费，现实执行/授权/用户福利未验。actual Ch82 389–414 belief≠identity/固定policy与metagame，建议只补观察信息vs实际delegation/payoff规则两种机制执行责任，非所有博弈理论或legalcontract。

## R26 SAE实际POST与最后十Source层接纳、四NC通过

root actual SAE Ch5 353–375完整局部/新362/364及704–716内本人注712，逐字一致，原Softmax竞争与externalconsistency保留、dynamic support不当真concept、完整费用/targetclass反侧近文，限定diffcheck零，窄lease释放，累计13实际POST。作者只同步本人注行政状态，随DAY读回、不额外final循环。

root按reader实际证据/owner局部接纳A33最后十项必要Source，65标准/深入＋FedGUI4最低关闭层已完成，不授Books/DAY。14989→Ch79 parent-ID/外接受；14920→Ch66 binary/多轴diagnosis/EvalSpec；14973→Ch23 metric与真实consumer分验；15294→Ch5 decodable-vs-used/局部干预，四具体NC通过，不第三人重复全文，不声称已有其算法。15063中心certificate暂缓不写正面Books；其他五gap作者actual/PRE另层。旧13 owner另交root互斥实际反向比较，作者不重复这些Source。

## A34 SCENIC与FL basis两最小gap逐字PRE

作者actual Ch36 208–249 SHARP/EdgeINC/MTIA完整两段与networkprogress交接，831–861 optimizer-aware sparse support/下一轮mask/残差和matrixoptimizer前后；读Ch35/37与现Ch23/26内存消费者责任。两项是不同责任，不能以都有网络/压缩判同义。

**15128 SCENIC → `TRAIN-DISTRIBUTED-TRAINING` Ch36**：MTIA完整两段后、`网络还可以参与进度反馈而不执行 reduction`段前，两段＋本人注：

> 可编程卸载也可以放进保留通用网络接口的 NIC，而不要求交换机或 accelerator 接管全部协议。一个分层分支由 FPGA 上的 stream compute unit 处理已映射的快速数据流，未支持的路径仍走通用 slow path；Arm/Linux 负责控制、配置和聚合状态，不承担每个线速 packet 的任意计算。Flow/QP 到处理单元的映射、地址翻译、bitstream 与驱动共同定义卸载接口，算子不支持或配置失配时必须保留原网络路径。这与只把 reduction 移进 fabric 不同，但上层 collective 的 group、operator 和结果依赖仍不能改变。<!-- source-family:SF-2026-ARXIV-2604-15128 -->
>
> [SCENIC 的必要原型证据](https://arxiv.org/html/2604.15128v1)还揭示一条 completion 边界：NIC 确认传输，不表示 GPU memory controller 已让消费者看到结果；其吞吐核验另轮询 GPU 内容，不能把网络 ACK 当 GPU 可读证书。100/200G FPGA microbench 和四节点 collective 不等完整大模型训练，梯度压缩训练仍未测。PCIe READ 瓶颈、部分 ASIC 更低 latency、重配置和小集固定开销均需保留，预装配置藏住一次切换也不证明所有切换无扰动。RTL/HLS、构建与驱动、状态/地址维护及 reconfiguration 都计费；未支持数据类型、GPU 可见性或总收益不可验时，回退通用 NIC/endpoint collective 与显式同步，不从线速 packet 处理批准训练 SLO。

本人注：`- SF-2026-ARXIV-2604-15128 — Daily2026-04-18补Apr17；[SCENIC exact-v1](https://arxiv.org/html/2604.15128v1) §4–9/T2/Fig4–11/§10，2+2+2=6。streamfast/mandatoryslow/Arm控制与NICACK非GPUvisibility；microbench非LLM训练、PCIe/ASIC反侧/重配/构建全费近文。独立reader必要Source/root接纳与date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

**14751 FL correlations → 同一owner Ch36**：SCAPE完整末段后、`### 矩阵耦合 Optimizer 必须把更新本身变成 Distributed Operation`前，两段＋本人注：

> 共享低秩 basis 的梯度压缩还带来另一种延迟：server 必须先收到一批当前 updates，才能从它们估计共同子空间并发给 clients，供后续轮投影。因而“不同 clients 的 updates 在这一轮相关”不够；下一轮仍需足够的时间稳定性，且 reshape、中心、basis revision 与刷新轮次必须一致。完整 update 刷新、basis/均值下行、历史与残差维护都是通信合同的一部分，不能只按每个 client 送出的短系数计算节约。<!-- source-family:SF-2026-ARXIV-2604-14751 -->
>
> [联邦更新相关性的有限对照](https://arxiv.org/html/2604.14751v1)显示，不同层的 reshape 没有统一最优选择，更多 local steps 也会削弱某些模型的时间相关；更短的单轮表示可能因收敛更慢而增加总传输量。LeNet/ResNet 与小线性模型的元素数统计，不是带真实链路、拓扑和端到端训练的速度保证，某些 PCA 构造本身也不实用。应共同结算达到目标质量的轮次、所有上下行、basis 计算与临界路径；子空间漂移、维度或净费用失配时，保留 dense updates、已验证的固定压缩/残差方案或更频繁但明确付费的刷新，不由空间相关自签下一轮无损。

本人注：`- SF-2026-ARXIV-2604-14751 — Daily2026-04-18补Apr17；[FL correlations exact-v1](https://arxiv.org/html/2604.14751v1) §II–VIII/Alg1–2/TII/Fig4–8必要层，2+1+2=5。serverbasis后轮可用/空间亦依赖时间、下行refresh与达到质量总元素另计；不采角累积/非PSD强界，不以元素数授速度或生产codec。独立reader必要Source/root接纳与date有效，作者actual owner比较，逐字PRE待root；未复现。`

## A35 K-Token / COEVO / CoopEval 三逐字最小PRE

作者actual Ch22 300–347 summaryhandoff/私有离散码/NSA及Ch75 217–219/295软输入与adaptedreader，Ch21/23表示交接；Ch79 225–241 parent-ID/fastfail/有界codingagent完整两段及Ch78/80；Ch82 389–420 belief、固定群体/metagame→Message非State及Ch81/83交接。三者都是不同消费/接受权，不从名称另立节点。

**15153 K-Token → `MODEL-LONG-CONTEXT` Ch22**：私有离散码的完整“重构目标还要与自由解码”段后、`固定 mask 与 prompt-conditioned routing`段前，两段＋本人注：

> 历史表示还可以不先编码成新离散词表，而把每个固定 K 原始 token 的 embeddings 聚合成一个连续输入：先求均值，再加上近零初始化的残差 MLP，由适配过的 reader 直接消费。训练同时更新压缩器与 reader 的 adapter，只在未压缩的目标输出上计算语言 loss；回答仍逐个生成原词表 token，不把新输出继续按 K 压缩。这改变输入表示与 reader 接口，不是 tokenizer 的可逆合并，也没有教会压缩器逐字重构原文。K 的分组、encoder、reader 与位置解释需要一起验收。<!-- source-family:SF-2026-ARXIV-2604-15153 -->
>
> [K-Token Merging 的有限对照](https://arxiv.org/html/2604.15153v1)只覆盖0.5B模型与三类任务；K=4 虽使输入位置减为四分之一，树推理、分类和代码 PPL 仍有退步，最佳三次结果也不能代替均值与不确定性。大规模辅助 curriculum、压缩器、适配训练和可选 K-gram cache 都增加费用，自定义压缩—性能综合分不认证普遍优越，更没有实测完整 serving 速度或 HBM 优势。精确引用、未知查询、质量或总成本不合格时，保留原始文本、较小 K、普通 summary 或检索回读，不能从短连续序列推断事实无损、输出也被压缩或任意大模型兼容。

本人注：`- SF-2026-ARXIV-2604-15153 — Daily2026-04-18补Apr17；[K-Token exact-v1](https://arxiv.org/html/2604.15153v1) §3.1–3.3/Eq1–2/Alg1、4.1–4.7/T1–3/Fig5/限制，2+1+2=5。固定K连续输入/输出原token，与私有码重构不同；适配reader/输出loss、辅助curriculum/best3与质量反退、无总SLO近文。独立reader必要Source/root接纳/date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

**15001 COEVO → `AGENT-PLANNING` Ch79**：有界codingagent完整两段后、`从历史解检索出可用操作`段前，两段＋本人注：

> 搜索人口的存活门还可以与已接纳程序的 commit 门分开。若候选始终留在隔离的设计搜索环境，可暂时保留只通过部分当前测试、但在资源或结构上有用的分支，再逐代提高存活阈值；同时以正确性测试比例和面积、延迟、功耗维护多目标候选。它允许探索中间的不完整设计，不允许把它替换已验 incumbent，更不能进入真实执行。任务要求每个中间版本都合法、测试覆盖不足或隔离不可保证时，原来的严格 correctness-first 剪枝仍更合适。<!-- source-family:SF-2026-ARXIV-2604-15001 -->
>
> [COEVO 的有限 RTL 搜索对照](https://arxiv.org/html/2604.15001v1)支持这种分层门的可行性，但逐步抬到所有当前测试通过，仍不是完整功能或安全证明；最终 Pareto front 也须重新接受独立 validator。部分面积—延迟乘积更好时单个分量仍可更差，某些任务始终失败，消融又混合改变排序和测试反馈，不能把全部收益唯一归于放宽早期门。多人口、修复、增强 testbench 与 EDA 测量均付费，完整搜索后的 Pass@1 不是一次模型生成的同预算结果。反馈失真、质量/资源目标冲突或预算耗尽时，保留旧 incumbent、严格门与更强独立测试，不让有限 test fraction 取得语义真值或发布权。

本人注：`- SF-2026-ARXIV-2604-15001 — Daily2026-04-18补Apr17；[COEVO exact-v1](https://arxiv.org/html/2604.15001v1) §3–5/Eq1–9/Alg1/T1–3/§6，2+1+2=5。隔离searchpopulation存活门≠incumbent/finalcommit，testfraction非formal正确；组件混变、PPA分量反退/失败与完整searchbudget近文，不推翻旧合法接受规则。独立reader必要Source/root接纳/date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

**15267 CoopEval → `AGENT-MULTI-AGENT` Ch82**：metagame完整段后、`## Message 不是 State`前，两段＋本人注：

> 合作机制也不只是在相同规则下多给一些历史。重复交互与 reputation 主要改变 Agent 能看见谁的过去行为，以及未来互惠的机会；mediator delegation 与 payoff contract 则还依赖环境真实执行委派或收益转移。提出协议、口头同意或投票，并不等于外部系统已经授权且能够兑现这些操作。应分别记录观察接口、partner identity、可委派动作、收益规则与实际执行者，不让 behavioral belief 静默升级成控制权或可执行承诺。<!-- source-family:SF-2026-ARXIV-2604-15267 -->
>
> [CoopEval 的有限博弈证据](https://arxiv.org/html/2604.15267v1)在指定有限游戏、可见历史和足够重视未来回报等条件下讨论合作均衡存在；这不排除坏均衡，也不保证模型群体会到达它。归一化 payoff、固定收益矩阵上的演化加权与实际合作成功率是不同测量，更多历史或某种 contract 仍可更差；合成 rationale 标签也不读取真实动机。重复模型调用、历史和机制执行都计费，有限轮折扣实验不认证现实用户福利、跨机构授权或持续稳定。执行承诺、人口或成本不可验时，保留明确外部规则、固定小组与实际环境对照，不从一个均衡存在命题批准开放协作。

本人注：`- SF-2026-ARXIV-2604-15267 — Daily2026-04-18补Apr17；[CoopEval exact-v1](https://arxiv.org/html/2604.15267v1) §2–7/Thm1条件/T2及必要AppC，2+1+2=5。history信息与delegation/payoff执行承诺分责，均衡存在非选择/稳定；finite15round、normalizedpayoff/evolutionmetric、负侧与调用费近文，不授现实福利/授权。独立reader必要Source/root接纳/date有效，作者actual owner比较，逐字PRE待root；未核artifact/复现。`

## R27 后续实际POST与旧十三owner收束

root实际读回A34 Ch36新241/243与865/867、完整旧邻接及本人注2242/2244，A35 Ch22新332/334、Ch79新237/239、Ch82新401/403、完整旧邻接及各本人注，逐字PRE一致、限定diffcheck零；五实际POST通过、全部窄lease释放，累计18实际整合。本人注只行政同步，不新增独核循环。

root反向实际owner比较通过八NC：14768→Ch27 query/answer/trace lineage与adaptivelearner/GT非truth/预算；14785→Ch26 frame/anchor与body/观察控制分责；14314→Ch56 futureKV/reserve和budget/stopping/sharedslot/tail及Ch34标签/独立评价；14631→Ch74 query改写arm/语义与原题回退；14550→Ch79 signature/graph到compiler与功能语义分验；14655→Ch79 parent谱系/有界innercoding/outercorrectness及Ch80派生reflection；14709→Ch66 EvalSpec人口/scaffold与Ch78真实trace/测试缺口；14648→Ch24 reference warp、几何consumer、双侧anchor未来条件及segment/选帧边界。均指具体已有责任，不声称已有各论文精确算法。连同此前21NC，共29具体NC。其余五真实gap如下，仅PRE准备，不预计整合。

## A36 最后五实际owner差额与逐字PRE

作者重读当前合同/ROADMAP、Books背景理念写作和目标完整局部：Ch23开放分类/动态负侧完整段至negativeprobe；Ch24 populationOT与persistentpair完整段至forwardbridge、2512-25075完整camera/time段至06667边界；Ch8 ICL完整段/nearERM至Post-training；Ch32 implicitpolicy/density与weightedflow完整段至07331边界。相关相邻章交接未变，复用已读上下文；五Source不重审。

**14762 OmniGCD → `MULTIMODAL-REPRESENTATION` Ch23**：动态负侧完整两段后、正侧probe之外段前：

> 开放集合也可以不为每个新域重新微调 encoder，而把聚类的学习对象改成当前样本集合的几何。一个替代分支冻结各模态自己的 encoder，将本集合的高维特征降到二维，再让只在合成点集上训练的 set decoder 联合识别已知与未知簇。这里共享的是集合划分程序，不是不同模态的共同语义空间；类别与 cluster identity 的对应仍需本集合的已知支持。它依赖整组样本的 transductive 访问，不能作为在线单例开放分类器直接部署。<!-- source-family:SF-2026-ARXIV-2604-14762 -->
>
> [OmniGCD 的有限跨模态对照](https://arxiv.org/html/2604.14762v1)支持冻结表示与集合读出的这种分工，却仍有 old/new 类切片反退，且合成训练、encoder、t-SNE、全组驻留与集合推断都付费；二维邻域不保证保住所有语义结构。受测点数和类别上限、集合组成与已知支持要随读出一起版本化，不能由多数据集均值授权任意规模或未知类别真值。全组访问不允许、几何失真或质量/费用失配时，保留原域内微调、专用聚类/分类头与可信支持，不因免去每域训练就称部署免费。

本人注：`- SF-2026-ARXIV-2604-14762 — Daily2026-04-18补Apr17；[OmniGCD exact-v1](https://arxiv.org/html/2604.14762v1) §3–5.3/T1–4，2+1+2=5。独立encoder→本集合2D→synthetic-trained setdecoder，非共同语义空间/在线单例；transductive人口、old/new负侧与全费用近文。必要Source/root独核及date有效，作者actual owner，逐字PRE待root；未复现。`

**15114 Amortized OT → `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24**：persistentpair完整两段后、forwardbridge前：

> 不愿在每批重复求 OT 时，还可以先为指定训练分布付出离线配对和势函数拟合，再把端点耦合摊销为固定数量 sliced potentials 的线性组合。沿投影方向拟合 Radon/Gram 表示或相应 dual approximation，使后续训练读取已拟合的耦合接口；它与保存有限 data/noise permutation 不同，也不保证近似势已经恢复 population 最优配对。分布、投影基与 Gram 条件改变时，需要重新检查拟合和刷新资格，而非把离线对象当作永久 oracle。<!-- source-family:SF-2026-ARXIV-2604-15114 -->
>
> [摊销 OT 的必要对照](https://arxiv.org/html/2604.15114v1)中，二维三任务的 W2² 均弱于独立配对，尽管 NPE 更好；这些量回答不同问题，不能用路径代理覆盖分布误差。CIFAR10 的离线拟合加训练比 OT-CFM 便宜，却仍慢于独立 CFM，求值次数也不等墙钟。应同时结算离线 OT、Gram/势拟合、刷新、训练与实际 solver 的质量和总预算；分布漂移、数值条件或净收益失配时，保留独立配对、每批 OT 或明确恢复的有限配对，不由摊销名称批准免费最优耦合。

本人注：`- SF-2026-ARXIV-2604-15114 — Daily2026-04-18补Apr17；[Amortized OT exact-v1](https://arxiv.org/html/2604.15114v1) §3.2/Eq16–17/4.4T4/AppC T10，2+1+2=5。offline OT→Gram/Radon拟合→固定slicedpotentials摊销，NPE不替W2、比独立CFM更慢/全离线费近文。必要Source/root独核及date有效，作者actual owner，逐字PRE待root；未复现。`

**14641 ASCII → `WORLDVIEW-LLM-INTELLIGENCE` Ch8**：ICL最后nearERM完整段后、Post-training标题前：

> Context 中显式给出结构，与模型自己构造出同样结构，也必须分开验证。将同一关系图写成文本或正确 ASCII 布局，可以测试外部组织是否帮助读出；要求模型先画再答，则同时加入了结构构造错误和额外输出。训练“从文本构造图”与训练“读取给定图”改变的任务接口也不同，推理时是否真的展示该图须另列，不能把两种训练和两种输入合并成更深推理的单一证据。<!-- source-family:SF-2026-ARXIV-2604-14641 -->
>
> [有限合成关系任务的对照](https://arxiv.org/html/2604.14641v1)中，给定正确 ASCII 的受测得分高于纯文本，而自行先画反而更差；构造训练和阅读训练在外部空间任务上的迁移也不同，部分阅读训练切片仍有收益。因此一致的文字与图形输出可能共同出错，不能由一致性或选出的高分子集认证内部空间表示。图构造、微调、输出 token 与独立回归都付费；布局错误、迁移或预算不合格时，保留原文本、可信外部结构与任务级验收，不把可视化步骤强加给每次推理。

本人注：`- SF-2026-ARXIV-2604-14641 — Daily2026-04-18补Apr17；[Text/ASCII exact-v1](https://arxiv.org/html/2604.14641v1) §3–6/T1–3/限制必要层，2+1+2=5。gold外显结构≠自构、construct/read训练和推理展示分责；83.7/75.0/66.6及迁移负侧、consistency非truth/全费用近文。必要Source/root独核及date有效，作者actual owner，逐字PRE待root；未复现。`

**14302 多视图 → `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24**：2512-25075 camera/time完整段后、06667 start前：

> 若复用视频生成器交付多视图，还要区分原 time axis 与现在的 view axis。原时间压缩 codec 可能把相邻帧合在一个 latent 中；直接将这些位置换成不同相机，就把多视图混进原有时间压缩。一个受限分支先复制每个视图，避免四倍时间压缩合并不同视角，再用 virtual-camera adapter 与稀疏 SfM 特征对应约束调节生成。复制只保护 codec 接口，不增加真实观测；相机条件、领域 LoRA 与特征对应也各有责任，不能一起当作已知真几何。<!-- source-family:SF-2026-ARXIV-2604-14302 -->
>
> [有限合成多视图对照](https://arxiv.org/html/2604.14302v1)的参考目标由编辑模型生成，并非真实渲染几何；某些不加 LoRA 或不复制的配置在 PSNR/SSIM 上还更好，特征匹配指标也不签发全视图一致。Adapter/LoRA 训练、SfM、复制驻留与完整生成均需预算，不同分辨率和 pipeline 的时间不能合成端到端速度保证。相机支持不足、codec 混视图、对应错误或净费用不合格时，保留原视频时轴、独立视图与真实几何验收，不将合成相机轨迹升级成 persistent world state。

本人注：`- SF-2026-ARXIV-2604-14302 — Daily2026-04-18补Apr17；[Multi-view exact-v1](https://arxiv.org/html/2604.14302v1) §3–4.4/Eq1–6/T1–2，2+1+2=5。time→view轴与4×codec的replication接口；virtualcamera/SfM/LoRA非真几何，生成GT/局部反退/完整费用近文。必要Source/root独核及date有效，作者actual owner，逐字PRE待root；未复现。`

**14698 MFPO → `TRAIN-PPO` Ch32**：weightedflow完整两段后、07331 start前：

> 隐式连续 policy 还可以用学习的平均 divergence 近似动作密度，再用两种 proposal 估计由 Q 诱导的 Boltzmann 目标分布下的速度场：一支来自当前策略，另一支来自显式 Gaussian，各自形成 self-normalized importance estimate，再按估计 ESS 提议混合。MeanFlow 的少步动作生成、Hutchinson/JVP divergence 训练与候选 Q 选择需要分别验收；有限步生成映射不自动等于连续 ODE 的精确密度，SNIS 的有限样本归一化也有偏。<!-- source-family:SF-2026-ARXIV-2604-14698 -->
>
> [MFPO 的必要连续控制对照](https://arxiv.org/html/2604.14698v1)支持这条有限近似分支，而非精确无偏或普遍最小方差保证。ESS 主要诊断权重退化，不代表任意被积函数的方差；由同批样本估出的随机混合权，不继承固定权且独立估计器的最优证明。受测两步、十候选仍慢于 Gaussian TD3/SAC，额外 divergence 训练、双 proposal、critic 与 rerank 都计费，步数不是完整速度。密度拟合、proposal 支持或总预算不可靠时，回显式 Gaussian/标准 PPO 与独立结果验收，不从 MeanFlow 投影误差或局部控制分数推出全局 soft policy improvement、LLM 策略或真实机器人安全。

本人注：`- SF-2026-ARXIV-2604-14698 — Daily2026-04-18补Apr17；[MFPO exact-v1](https://arxiv.org/html/2604.14698v1) §4.1–4.4/Eq9–30/5.1–5.2/T1、§8.4/§10T2，2+2+2=6。平均divergence近似density/双SNIS与随机ESS不继承精确/最优证明，finiteT/critic rerank/全费用和Gaussian反侧近文。必要Source/root独核及date有效，作者actual owner，逐字PRE待root；未复现。`

## R28 最后五修订PRE与实际POST通过

root actual A36五逐字PRE，四项直接通过；MFPO原“critic期望支持”不精确，root再核v1§4.3/Eq19–28，改为“用两种proposal估计由Q诱导的Boltzmann目标分布下的速度场”后PRE通过，只改这一受影响命题，不重新研究。作者依唯一窄lease保存五处正文/本人注。

root actual POST实读Ch23 162–174及注2198；Ch24 309–321、1803–1816及注2862/2864；Ch8 107–120及注392；Ch32 219–233及注532，修后逐字一致、完整旧邻接/条件和反侧保持、限定diffcheck零。最后五实际POST通过并全部释放，作者仅行政同步本人注，无额外FINAL循环。现23实际整合＋29具体已有覆盖＋13中心争议终态＋1最低4分关闭＝66。23为具体长期差额必要加深，不称全附件/代码审计；65必要标准/深入与FedGUI最低关闭分别有效。普通Source/Books零，剩正式六节归并与非报告作者DAY/完成态FINAL，当前进行中，不授无遗漏。

## A37 六部分正式归并prepared与作者机械检查

正式README已合六节，原0/小时窗与448字符连续原§4保留，66行唯一身份/评分原数字不变；新66小标题均与候选Title+URL一致。23实际整合深入、29具体NC标准、13中心争议和FedGUI最低关闭分别处理，不将prepared自动计完成。§2十四源/原始停止及五主目录＋MiniMax子入口历史不足；§5具名日期资格、有效同v1复用/Jul17事件恢复和13中心精确重开；§6记录实际角色/AB/core抽检及未抽范围，仍未通过待root真实DAY。

作者实际运行V3通过，66行/66唯一/66标题对应，本地链接0缺；23本人注均实际POST通过/无旧待root字段。限定Books/本日报告cached和unstaged diff-check零，未操作index或他人修改。此为格式与冻结检查，不授语义DAY或无遗漏；root收到正式稿后做完整六部分，准备工作不再扩研究入口。

## R29 root实际完整六部分DAY通过

root（非报告作者）实际顺读完整428行六部分，分段1–112、113–208、207–312、312–428，核全部66证据/精确处置、有限来源停止/日期资格、EX分层、23真实POST链与原候选冻结，DAY通过。23整合/29具体NC/13中心隔离/1最低关闭，普通研究/Books/独核零，不授全Coverage/Evidence或无遗漏。

唯一窄修是在§3最后总账后/§4标题前说明原“公告窗口与旧库存的边界”“Books决定”是授权保留旧报告，不代表补充结果；连续原§4未动。root授权作者据实际DAY同步§1/3/5/6及状态完成，§6单独结论通过。保存后只一次字段/冻结/限定检查读回，不另生成行政FINAL轮。作者已按此保存，不改他人Books/State/index，不扩下一日研究池。

root实际回读保存完成态，六部分内容/原窗/衔接说明/结论通过语义均正确；完成态V3最初因未匹配“终态保留项”词汇失败（此前进行中pass不外推完成态）。按root精确指示仅将§5一行改为“以上为本窗终态保留项，已隔离；不用于正面证据、Books，也不支持无遗漏断言。每项定点重开条件如上。”后，作者实际重跑完成态V3通过；没有改scope、反证、来源或validator。原窗相同、448字符连续原§4、66唯一与23/29/13/1分账、六节及本地链接0缺读回仍成立，限定cached/unstaged检查零；不新造行政FINAL轮。
