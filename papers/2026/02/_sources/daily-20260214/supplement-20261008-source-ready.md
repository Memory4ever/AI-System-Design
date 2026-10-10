# 本日作者必要证据停点与拟采用命题

范围：Daily 2026-02-14，本轮补充北京2026-02-13完整自然日；原30候选/评分/日期/窗口及原§4连续正文冻结。此文件是现有原件的具名审阅笔记和续跑位置，不是另一份完成账本。作者必要读不授独立Source、Books或DAY；下载不计阅读。以下历史提案及复核分层保留；最终57新论文日期隔离、官方Lockdown1确定新增已并入日报六部分，最新层以本文件“本轮当前层补记”为准，不改变旧30项。

## core-0：交独立 reviewer_20260214 的12项

共同原件：[exact-v1正文缓存](./supplement-20261008-core-0.json)，每条以 `url` 唯一定位，再按 `sections[].heading/text` 定位原文；缓存保留全文段，不在这里重抄。日期原件为 [dates-first-two](./supplement-20261008-dates-first-two.json)；root已逐字段交叉核本日下/上界，以下12项没有prior-publication/跨界信号。日期通过不替代Source。11495/11509另已root实际Source与Books POST，不在本批。

### 2602.11534 Krause Synchronization Transformers

拟采用命题：旧全局mixing→RBF distance affinity、预定义spatial/causal局部候选W、候选内top-k后局部归一化，给出可显式限制interaction support的设计分支；不授一般Transformer必然collapse或bounded-confidence严格收敛。建议 **2+1+2=5**，标准机制/评价，受影响复杂度和理论宣传定点深入。作者实际必要读§4（Eq5–12、Algorithm1、4.3）/完整§5/§6。

直接反侧与采用边界：§4.2宣称O(NWd)须真的只构造W候选并执行距离/TopK/归一化；Algorithm1先distance再mask，不能从数学mask自动授稀疏kernel或线性端到端，W也未必常数。§5.1/5.4的LLM保留原全局attention，只增加Krause shortcut，两路径LoRA，50K Flan-v2；Llama3-8B W32/k16，不能把vision替换收益或KARM复杂度迁移成LLM加速。Table6 MNLI Acc提高但Macro-F1 55.29→53.72，MMLU-Pro41.67持平。Tables4/5单H100、MNIST784/W128/k96/50K samples与CIFAR3072/W256/k192/10K samples，KARM更快于full ARM但慢于linear ARM；只绑定该质量/速度取舍。重复/CI、precision/batch、完整kernel建邻成本、LLM latency/SLO Not Disclosed。§4.3“suitable scale/support”与Appendix C条件理论不作为已证实际LLM稳定保证；若要采用定理，需另定点读实际条件，不能以本包授全理论。Books候选owner MODEL-SELF-ATTENTION Ch14（interaction support），需Source后实际比正文，不预授覆盖/写锁。

### 2602.11543 SPES

拟采用命题：旧decoder共享参数/全复制优化状态→客户端保存全weight但只对assigned experts维持optimizer/gradient，其余expert冻结；共享部分与assigned expert的聚合/传输不同，从而须分开训练驻留与发布流量。建议 **2+2+2=6**。作者实际必要读§3 Memory-Efficient Decentralized Pretraining（选择、同步、聚合流程）/完整§4/§5。

直接反侧：full model weights仍复制，不是ZeRO式weight分片，也不消除全model downlink；65% uplink不能写all-network减65%。7B实验4×8 A800、13Gbps，2B16 L40S、17Gbps；RDMA对照3.67k vs3.79k依运行配置，不授等效所有通信栈。部分ARC/PIQA/OBQA质量反侧保留，FedAvg shared/expert union策略不能签任意异质客户一致性。更多并发/precision/batch/SLO/端到端网络成本未披露则Not Disclosed。Books候选owner TRAIN-DISTRIBUTED-TRAINING Ch36（decentralized optimizer/aggregation），不能因为名字含memory便自动授Ch39 ZeRO。

### 2602.11639 PACE

拟采用命题：纯on-policy训练早期缺成功credit→initial-policy rejection sampling先构建最短correct路径（无正确则最短fallback），冻结其prefix，再用当前policy生成suffix的hybrid rollout；prefix512逐步退至0/100steps，difficulty coefficient依据hybrid empirical pass-rate，不是固有难度。group reward以长度代理平衡。采用的是训练context curriculum/可执行采样成本分支，不是新GRPO保证。建议 **2+2+2=6**。必要原文§3 Methodology/§4 Experimental Setup/完整§5/Limitations。

直接反侧：全部错误时“shortest”可仍是错误fallback，不授示范正确性；prefix也有training prefill费。1024prefix结果90.3低于512的93.1，不是越长越好。MATH length1490与Table3 1390互不一致，不合并该长度数字。任务/模型/长度预算依原Table1–3，不以accuracy单数推通用高效。§4明确32 NVIDIA A100、batch64、group8；全链成本、CI/SLO未披露写Not Disclosed，不能把已披露硬件标成缺失。Books候选owner TRAIN-GRPO Ch33/训练数据Ch27须实际比较唯一owner；此包不先定双owner，也不把局部长度配方授长期通则。

### 2602.11683 ThinkRouter

拟采用命题：所有位置固定discrete或soft latent→按temperature-scaled概率的max-probability confidence（在Top-k/Top-p/Min-p过滤与重归一化之前），低置信选discrete/high置信用soft top-j，改变autoregressive内部表示传递与decode预算。建议 **2+2+2=6**。作者实际必要读§3 Preliminary/§4 ThinkRouter（Algorithm1 Temperature Scaling注释明确）/完整§5/§6；独核纠正原作者包的pre-temperature误述。

直接反侧：置信只是模型内代理，错latent可高置信；仍顺序AR，不是并行可能世界或calibrated truth。四模型、H100/SGLang、10条validation随机选择与3seeds只支持该配置；Random coding83.13高于ThinkRouter82.94，gpt-oss AIME24离散93.33高于91.67，不能claim所有task Pareto。latency/length/soft-j结果依Table和validation选择，不授质量等长/免费routing。未披露precision/batch/完整SLO应Not Disclosed。Books候选owner MODEL-SAMPLING Ch20，待实际owner比较而非先称覆盖。

### 2602.11698 Spiral Recursive Architecture

拟采用命题：全部token每轮重复共享core→causal chunk pooling形成多分辨率状态、分辨率预算分配、g−1 shift及overlap，给出recurrence的局部/层级信息交接分支。建议 **2+2+2=6**。作者实际必要读§2 Method、完整§3、与拟采用hierarchical dependency直接相关§4、§5。

直接反侧：Pythia160M–1.4B/Pile250B、ctx4096给的是prefill FLOPs而非wall-clock或端到端token费用；recurrence U仍局部预算。去overlap质量下降，MeSH baselines也获益，不授收益唯一归因hierarchy/所有context稳定。kernel/hw/precision/batch/SLO与显存不齐披露则Not Disclosed。Books候选owner MODEL-TRANSFORMER-LAYER Ch17或MODEL-LONG-CONTEXT Ch22须比较其recurrence/状态交接实际论证后选一，不自动复写全recursion理论。

### 2602.11715 DICE

拟采用命题：完整kernel生成的reward-hacking与credit不稳定→固定kernel suffix/prefix/imports/compile wrapper的infill使执行验收约束显式，再过渡完整生成的TraceRL；训练改进需区分compile/正确执行与fast1。建议 **2+2+2=6**，reward/执行验收受影响定点深入。作者实际必要读§3 CuKe construction/§4 Methodology/完整§5/§7；root此前已实际一次决定核心准入，非Source通过。

直接反侧：baseline L2 execution46→0/L3 44→0，而DICE43→39/34→16，只是减轻而非消除reward hacking；L1 fast1 SFT16、DICE9，correctness≠速度收益。full generation与infill阶段的数据、wrapper和search/training成本不能并成统一产能；CUKE新数据/SOTA不是长期机制全部理由。hw/precision/batch/CI/SLO及执行sandbox范围依原文，未披露不造。Books待Source后实际比較 INFER-REQUEST-LIFECYCLE Ch42执行验收与TRAIN-GRPO Ch33 reward/credit，root明确要求唯一owner不先定Ch42；未得owner/PRE/锁不得写。

### 2602.11737 Salient-VCD

拟采用命题：随机corruption contrastive decoding→基于query-agnostic visual saliency选择corruption，再比较原/扰动logits；有限hallucination指标反侧可改变扰动接口判断。建议 **2+1+2=5**，Eq/prose干预身份争议深入受影响内容。必要原文§3 Method（Eq6/7）/完整§4/§5/Limitations。

直接反侧：Eq6/7 δ=−1按显示公式mask LOW-saliency，而prose说most-salient，实际干预identity中心不一致，不能帮作者静默修成统一机制；任何拟采用必须隔离具体mask方向/重开条件。两7B模型POPE/MME、3seeds只是有限检测，query-agnostic saliency易clutter偏置，扰动非真实counterfactual，不授因果faithfulness或general visual grounding。Books先源争议隔离，其他可用局部观测是否报告保留待独核；不以争议降分/排除潜在贡献。

### 2602.11767 TSR

拟采用命题：仅采完整trajectory→按turn进行tree搜索分支、按proxy/task std筛选局部候选，改变rollout搜索预算与训练样本credit；unchanged objective不代表unchanged采样分布。搜索要求可分叉/可重放的模拟状态是本包系统推断，主文tree抽象没有证明实现snapshot已经核验。建议 **2+2+2=6**。必要原文§2 Background/§3 Optimizing Rollouts with Trajectory Search/§4/完整§5/§6。

直接反侧：0.5B/3B、3tasks、3runs、256prompts；equal final trajectories不等equal search/环境调用预算，不授unbiased on-policy或便宜端到端。WebShop5.8–7.7 turns与声称horizon5不一致，效率解释隔离该身份。可fork仿真environment不证明可rollback现实工具外部副作用。hardware、端到端training/search成本、真实tool恢复/授权范围未披露则Not Disclosed。Books候选owner TRAIN-GRPO Ch33（training rollout credit），外部工具rollback仅交接边界不双写Ch78。

### 2602.11824 Revis

拟采用命题：统一activation steering→先average grounded minus blind representation差分vectors，再对blind hall−unknown方向project/正交化，选择最深正Δ单层及quantile threshold，分开视觉缺失与错误承诺，不把一根truth direction授所有hallucination。建议 **2+2+2=6**。必要原文§3 Preliminary Analysis/§4 Design Details/完整§5/§6/§7；不暗示逐sample project再average。

直接反侧：100样本extract+100calibration不是普遍识别；CHAIRI8.23高于8.13。去threshold Qwen无gain而LLaVA collapse，α1.8损utility，blindness本身不可修。TPT.025没有hw/完整运行条件，不能授免费0.025s统一延迟；extract/calibration/judge/steering成本均计。主要诊断/干预语义不同，不授faithful internal cause；owner候选MULTIMODAL-REPRESENTATION Ch23，先实际比較是否最小差额或仅局部配方。

### 2602.11852 ProtoT

拟采用命题：token-token全历史attention→R32 prototype channel softmax、past-only EMA/mass normalization、固定summary state；prototype的显式读写与time-scale是具体factorization，不因可命名概念即授真实可解释推理。建议 **2+2+2=6**。必要原文§3 Prototype Transformer/§4 Experimental Setup/完整§5/§6/Reproducibility statement。

直接反侧：ctx1024→2048 PPL80.5→81.9，234.9M/L12/h512 PPL29.5差于LLaMA25.8/Mamba26.5；不是全部长上下文/质量胜利。PMR negative clamp有条件，不能签任意positive state/稳定保证；GPT5.1概念命名非因果解释。BF16 ctx256训练25.2<LLaMA55.1it/s，32K单H100/b1 inference crossover不能充当总训练/服务优势。prototype/search/normalization真实成本、CI/SLO缺项保留。Books候选owner MODEL-LONG-CONTEXT Ch22（固定state/sequence factorization），待Source与实际owner论点判断。

### 2602.11863 In-Context Function Learning in Large Language Models

拟采用命题：只靠few-shot aggregate误差推ICL机制→已知GP kernel生成连续函数，以GP/1-NN参考和likelihood检查function prior及variance，post-training改变小函数学习的条件证据。建议 **2+1+2=5**。作者必要读主文§2 Background/§3 Methods/完整§4/§5/§7；**缓存附带Supplementary 1–8不计已读或采用**，不遍历附件。

直接反侧：Qwen3四bit、200GP函数、d1–4、0–49shots；empirical GP与expected1NN是该生成分布参考，不授所有函数global lower/upper bound。SE GP likelihood也可在rough Matérn数据较高，variance inflation与部分correction使likelihood不能自动识别真实先验/LLM就是GP；只收窄为局部prediction/calibration证据。不用小实验/理论名称排除。more general distribution、all-model机制、hw/完整token成本/CI缺项不能外推。Books是否改变WORLDVIEW-LLM-INTELLIGENCE Ch8实际ICL解释需Source后具体比较；不为了写书扩读variance全部推导。

### 2602.11882 Where Bits Matter in World Model Planning

拟采用命题：相同总bitwidth即相同planning质量→DINO-WM encoder/dynamics mixed-bit allocation及paired planner budget揭示precision位置与搜索预算耦合，包含严格复验方向翻转。建议 **2+1+2=5**；量化设计反证深入必要内容。作者实际必要读§3 Setup/完整§4 Main Results/§5 Discussion/§6。

直接反侧：仅DINO-WM/Wall任务/M4/48GB weight-only dequant，30或20 paired goals、4000bootstrap；不是低bit kernel部署或端到端加速。mixed4 CI跨0/p=.109，strict66budget符号翻转，near-size INT6更好；不能授encoder precision稳定最佳或全部world-model通用规律。storage bitbudget≠activations/KV/resident memory；planner-cost与quantizer/dequant/统计人口需分开。Books候选owner INFER-TENSORRT-LLM Ch49（low-bit validation/planning分布），world-model Ch25只交接，不双写；待实际owner反证差额。

## 当前作者停点（2026-10-08，北京15:32；后续只增量恢复未完成层）

恢复补记：core-0另十二项已经 reviewer_20260214/root 实际独核结清：十项窄命题Source通过，11737/11767中心冲突隔离、局部仅报告；temperature/filter顺序、PACE hybrid/hardware、TSR模拟可分叉推断、REVIS先平均后project四处事实修正实际复核通过。连同原11495/11509，十四项必要审阅层有效；仅前两已actual owner/POST，其余不授PRE/POST/DAY，不重复读已有效Source。下列旧作者停点是原读数而非新层权限。

尚未授DAY，日报仍进行中。84完整题摘与九项一次决定核心均经root独立准入校准：65潜在贡献/19具体EX，七prior-ICLR家族加ForeAct共8日期隔离，**57日期支持可继续Source**。FLAC与OpenAI Lockdown另列不并入57。原30及连续§4保留。

作者必要机制/关键评价/直接反侧已读 **34/57**（不等独立Source通过）：

- core-first六项：2602.11305/11541/12036/12151/12222/12275；12222证明定点还见[proof-check](./supplement-20261008-12222-proof-check.json)。三个ICLR11451/11549/12172已读原件保留但不计34/57、不继续本窗SourceBooks。
- core-0十四项：2602.11495/11509/11534/11543/11639/11683/11698/11715/11737/11767/11824/11852/11863/11882；其中11495/11509 root独立Source与Ch72/66 PRE/实际POST均通过、锁释放，其余12交本文件独核。
- core-1六项：2602.11965/12005/12078/12204/12262/12271；12262必要补件见[t3d-ablation](./supplement-20261008-t3d-ablation.json)、[t3d-reference](./supplement-20261008-t3d-reference.json)。11909/12113/12318仅缓存不计34，日期隔离，SourceBooks停。
- once-core五项：2602.11351/11564/11758/12099/12221；12221必要conditioning差额见[unidflow-conditioning](./supplement-20261008-unidflow-conditioning.json)，存在ref条件身份争议，不授same-condition DPO。
- core-2三项：2602.11832 JEPA-VLA、2602.11980 SCoT、2602.12205 DeepGen。前两必要Source包已发送root；DeepGen采用边界见下，未授Source。

普通必要证据待读 **23/57**，不是受阻、不是下载完即读：

- core-2尚余五项：2602.11858 Zooming without Zooming、11934 RobotDIFT、12063 VLAW、12155 FAIL、12160 DreamID；exact-v1主文已缓存，下一步只读必要机制、关键评价和直接反侧。
- Agent十八项：2602.11340 BLPO、11409 TRACER、11513 DELDP、11524 ADMIRE、11596 MAPLE、11619 When Agents Disagree、11636 ScalSelect、11729 Crosscoders、11749 AIR、11750 Ambi、11754 Cooperation delay、11782 FlowMind、11812 entropy pool、11877 Probe/Dirichlet、11908 Selective Abstraction、12134 VAT、12268 CM2、12276 CATTS。首八缓存[agent-core-0](./supplement-20261008-agent-core-0.json)，后十[agent-core-1](./supplement-20261008-agent-core-1.json)下载结果已保存；全部仅下载、没有作者必要正文读。TRACE11528 prior-ICLR停本窗Source，不在十八项。

core-first六、core-1六、once五、JEPA/SCoT的必要原件实际已读且先前消息包已发送root，但除本文件具名十二/DeepGen外，其细化采用命题/评分/反侧尚待同日持久整理；这是普通待整理/待独核层，不能让接手复核者凭缓存标题创造采用命题。root可按现有消息恢复或定点让作者补持久包，不授Source通过。

上述34项中十四项必要Source层已有限结清（含两中心局部Only），core-first/core-1/once/core2余二十已读项仍待持久完整采用包与独核；另二十三未读普通Source。十项已Source准备稿开始实际owner比较，首两Books POST有效；不授日级。作者恢复本日未完成层，不重审有效通过层。每日14来源记录/历史缺段/具体日期请求见日报§2/5；不继承旧Coverage标签。没有剩余Books写锁，没有stage/commit/push，没有修改LS/月索引/他日。

## core-first：12151 OServe 的具名Source-ready

2602.12151 [OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration](https://arxiv.org/html/2602.12151v1)。此前作者实际必要读[core-first](./supplement-20261008-core-first.json)中§2 Background/§3 Workload-aware Scheduling/§4 Workload-adaptive Switching/完整§5 Experimental Evaluation/§6；本轮复用身份/精确版本/采用范围，不重复读全文。日期原件[first-dates](./supplement-20261008-first-dates.json)/[dates-first-two](./supplement-20261008-dates-first-two.json)root已逐字段实核，normal上下界支持Beijing Feb13，无本项prior-publication或跨界信号。

拟采用命题：旧单模型多replica的静态placement/请求派发→按request长度簇、实例并行布局建立离线performance profile，在未来minute workload预测下求放置/派发，并将KV drain、迁移/加载作为改变layout的状态切换成本；同次replicas共享模型参数，不同模型是各次实验，不授multiple-LLM联合部署。**planning proposal与当前可见实例/运行中KV的实际切换是不同身份**，不从未来最优布局直接推当前请求已可无缝执行。建议 **2+2+2=6**；profile→forecast→layout切换跨服务边界缺口需定点深入，未授源/owner通过。

关键原证位置：§3的lower max-flow（preflow-push）与upper heuristic交接、Algorithm/search的20次no-improvement停止、长度k-means及performance profile；§4 workload predictor（50-step history、1-minute LSTM forecast）、migration/load/switch的实现分支与headroom；§5必要对照/模型规模/资源/latency及switch反侧，结论不扩到online global optimum。lower placement固定时的max-flow不是upper布局全局最优证书，upper heuristic的停止也不授最优性；配置search12s vs50s、P99相差<6%只属论文local comparison，不授所有workload规划质量。root实际原§3纠正min-cost flow和多LLM身份后采用本窄修，不重复原Source或附件。

直接边界/反侧：profile与输入长度簇、平台kernel/模型/parallelism版本共同有效，forecast有误差/概念漂移；1min控制时钟不能接管逐request硬deadline。4节点×每节点8 H100、节点内NVLink/节点间IB实验是所测资源，不是任意异质集群。模型reload由>50s降至约10s仍非零，KV drain/migration仍付费；10–20% headroom本身降低名义capacity，不把profile/forecast/search与迁移费用排除后称全服务免费。实验按原workload、P99等指标单独比较，不能由吞吐平均值授任意SLO、无限多模型或无interrupt。未公开对应precision/batch/concurrency/全部input-output分布、故障恢复及生产SLO时写Not Disclosed，不自动补齐。未核artifact/复现；已有原核心够支持上述有限proposal/transition命题，STOP，不追加全部附录/代码。

Source后潜在唯一owner INFER-SCHEDULING Ch56（layout policy及transition），需要实际现profile/runtime feedback/placement论证比较；Ch52只作KV/state执行交接，不因能映射双章就写两遍。本包只请求root该项独立Source，不提前授PRE。

### core-first 其余五项已读采用包（恢复已读，不增全文队列）

以下均为此前作者必要正文实际读、现持久化采用范围，不因缓存存在授独立Source。共同精确原件[core-first](./supplement-20261008-core-first.json)，字段url→sections.heading/text；normal日期各自经root字段交叉核，不把提交时刻当公开日。root可逐项按这里的命题独核，支持/直接反侧足即STOP；以下owner仅提议，未实际PRE不授Books。

**2602.12275 OPCD：2+2+2=6。** 必要位置§3 Method/§4 Experiments/§5 Conclusion。采用窄命题：context-conditioned teacher与不带context student的分布不是同一输入身份，on-policy生成配合reverse-KL distillation可把外部context的任务行为转为参数更新；context抽取/teacher采样与student rollout分责，不能把teacher更知情当student已经学到可迁移知识。旧直接raw-context conditioning与SFT仍合理；这不是新通用RL或模型自行得到真值。关键反侧：所选extracted context 77.4、raw context70.5、base75.1，context质量会让结果低于base，self-teacher存在不稳定；top-k reverse-KL只是近似，额外consolidation数据混杂不授纯机制归因，safety83.1<83.3直接反退，不授任意context/teacher配置普遍增益。抽取、teacher计算、采样及训练成本均需保留，未核artifact/复现，不由输出分数授完整产能；精度、全链运行配置/CI/SLO缺项不补造。root独立必要Source窄通过；TRAIN-DISTILLATION不是ROADMAP StableID，需依现真实训练owner实际比较，不自造节点或按名称定章。

**2602.11305 MisAlign：2+1+2=5。** 必要位置§3 Methodology/完整§4/§5/Limitations。采用窄命题：automated alignment assertions的测量须分开两个条件人口：Coverage是misaligned(y=0)被至少一个assertion标中的比例；§3.2.1 False Failure Rate是aligned(y=1)被assertion误拒的比例，不是false-fact/幻觉发生率。Harmonic AS保留两分母及generator/judge身份，不能给一个综合分授真实价值alignment保证。300条human验证的是Mistral domain classification，不认证StageII全部automated assertions或文化/价值真值；英语/所定domain与taxonomy、generator/classifier/judge相互依赖限定有效域。额外生成、分类、人工校准与多轮评价仍付费，配置/全预算/CI缺项不补造。root实际Source纠正后只采用窄测量原则，传统指标本身不授新长期差额；潜在实际owner PLATFORM-EVALUATION-SYSTEM Ch66需比较是否已有覆盖或仅报告，不按映射写新段。

**2602.11541 INTENT：2+2+2=6。** 必要位置§2 Model/§3 Methodology/完整§4/§6/Impact。采用窄命题：tool plan不只比较单次报价，还可用intent likelihood和retry假设计算期望成本/utility，但计划的期望选择权不能覆盖runtime对实际剩余budget的硬affordability检查。γ与retry分布估计、同intent的候选工具及当前budget身份须一起保存，不能按较好期望让一次不可支付调用执行。受限765条BudgetStable、B=50、synthetic prices与FR100等配置不是生产随机失败/真实定价模型；estimated intent/retry失配会改变排序，单一FR不授无预算越界或任务最终正确。该方法只工具价格预算，oracle/model总费另测；缓存匹配后跳simulation不能绕当前runtime余额/价格/权限检查。估计器、重试、工具与规划自身费用分账；真实外部工具授权与硬停止不由该模型证明。root独立必要Source窄通过；潜在实际工具预算执行owner依ROADMAP与正文比较后只选一，不造未核StableID。

**2602.12036 Composition/SPC：2+2+2=6。** 必要位置§2 Preliminary/§3 Methodology & Meta-Experiments/完整§4/§5/§7。root实际§3/5及§4对照纠正本包：SPC是Sequential Prompt Composition，有向地把q1答案数值绑定q2变量，最终GT仍gt2；无所谓pres>2/prompt-preservation参数。§3.3保持同GRPO objective/advantage/importance，只从compositional prompt dataset采样，不改变group或estimator结构。采用窄命题为solve_all全正确零优势人口→通过答案依赖构造更难且可验证的prompts/curriculum，须分开合成数据有效性与最终答案reward：final-only通过未认证两道子题路径正确。训练199K/评价12K及数据构造费用保留，14B GPQA−0.8、4B IMO−0.1与random/full diversity局部更好，不授任何composition普遍最优。合成、变量匹配/GT验证、长prompt rollout与训练仍付费。先停止旧group/credit命题的owner拟议；新的唯一owner须实际比较TRAIN-DATA Ch27与TRAIN-GRPO Ch33课程已有论证，不自动授Ch33，更不把数据curriculum升级为新目标无偏保证。

**2602.12222 DDT/IDFT：2+2+2=6。** 必要位置主文§2 Distribution Discriminant Theory/§3 Applications/完整§4/§5，以及[必要证明定点](./supplement-20261008-12222-proof-check.json) A.1/A.2/Eq24。采用窄命题：teacher答案的指数权重改变离线微调人口，优质/噪声分布及weight/mask须实际验收；IDFT不是当前policy采样的on-policy RL，更不能代替偏好或真实outcome验收。中心理论的无条件推广隔离：E_q φ=H(p)−H(q)−KL，取负需要KL大于entropy gap，Eq2不是一般条件下成立，A.1省略gap，不能照录为任意distribution discriminant保证。仅采用可观测data weighting与直接反侧，不做全理论修复。Numina333K/3epochs、mask−1损害而−5较优、−10增加noise表明极端权重/阈值并非普遍改善；teacher质量、计算权重/过滤和训练仍付费。潜在owner TRAIN-DATA Ch27/现数据加权节点与训练objective按实际正文比较选一，未核完整实现/复现，不授理论修复完成。

### 12151 OServe actualowner PRE：拟仅报告/既有原则覆盖，不造算法diff

作者实际Ch56连续457–526 Routing/Placement/Autoscaling及954–1009 calibrated configuration search、1253–1282离线templates/并行控制与DP↔TP转换；Ch55/57开篇及末尾实际顺读。现471–475已分慢capacity、现成endpoint routing及排空/可用后切流；490只versioned proposal、runtime plan boundary commit；522–524 profile合同和loading/migration delay；954–982 actual measurement→候选/Pareto→silicon validation及硬件/runtime/shape/workload/SLO校准；1253–1257离线模板与在线allocation，1267–1280 KV/communicator/切换费和完整状态验收。Ch55拥有跨P/D可用KV交接，Ch57平台不取代这些request级执行责任。

OServe拟采用的profile/length population、minute forecast→单checkpoint多replica布局proposal、KV drain/migrate/load/headroom→实际readiness与P99回验，在这些长期原则中已能承载；§3固定placement lower max-flow/preflow-push和upper heuristic的局部优化、20次停止、12s/50s、reload约10s不需要变成另一段通用调度教材。**不声称已有正文承载OServe的具体流算法或其数字；那些只作报告中的条件测量证据。** 所以本项建议报告Only（长期原则已有覆盖，但局部实现/测量不是已覆盖事实），不写Ch56，不为k-means/max-flow名称制造diff。请root实际PRE判是否仍有稳定最小差额；若无，即STOP该Books层，无附件/实现扩读。

## core-0 的实际 owner 比较与PRE拟文

以下为作者实际现正文比较，不是PRE通过；review_20260214实核后由root逐owner授锁。位置是本次读取时行号，写前以锚点重定位，保护既存staged/unstaged与他日正文。Source层复用本文件具名限定，不扩附件。11737 Salient-VCD与11767 TSR中心争议仅报告，不拟中心Books正文。

### 第一小组：11863 / 11852 / 11882

**11863 ICL-GP → WORLDVIEW-LLM-INTELLIGENCE / Ch8：拟仅报告或具体已有覆盖，不造diff。** 实际读Ch8 77–119，ICL87–107连续论证：101明确few-shot得分不能证明内部学习算法，103把context版本/示例/截断作为验收输入；105–107进一步分开可实现comparator、pretraining选到它、任务内样本数与训练任务数以及有限实验预算。Ch7/9开篇和末尾实际顺读，Ch7资源/loss不授能力，Ch9控制闭环不授学习机制。此次拟采用是Qwen3/已知GP kernel/200函数/0–49shots的误差与likelihood探针、variance inflation反侧，不证明真实prior或内部算法；该具体probe结果作为已有ICL验收原则的局部证据，而不是新的通用学习算法。故不重写Ch8抽象算法或GP全理论；如果独核认为“kernel likelihood与prediction/calibration分账”是实际稳定差额，可在101之后只补一句，拟文：`已知函数分布的回归探针可同时比较预测误差与核似然，但两者不能互相代证：方差膨胀会改变似然偏好，受限参考学习器只界定该生成分布，不证明模型识别了真实先验或执行同一内部算法。` 请PRE选择Only/已有覆盖/该一句，不把章节映射自动授已有覆盖。

**11852 ProtoT → MODEL-LONG-CONTEXT / Ch22：拟最小整合两段。** 实际读Ch22 460–487（完整KV→有限充分状态、线性Attention累加S/z、ReHyAt局部softmax+远历史summary）及620–658（扩容/固定Register/稀疏item/观测容量），Ch21/23开篇与末尾实际顺读。现正文有finite-kernel summary与EMA/多时钟整体取舍，但未承载“prototype channel作为写入坐标、各channel过去值的mass-normalized EMA、当前query读prototype”的具体summary factorization；这是有序读写而非任意可命名概念。建议插在Ch22线性累加分母说明之后、`固定状态也可以只接管远历史`之前，保留ReHyAt混合路径。

拟文1：`有限状态也可先定义一组可学习prototype通道，让每个到达token对通道产生归一化写入权重，再由各通道累积过去value及相应mass、用不同衰减尺度维护因果EMA；当前token先读取截至上一位置的通道摘要，再将自身写入供后续读取，而非逐项历史KV。这里prototype提供固定数量的读写坐标，不等于发现了独立人类概念；past-only边界、衰减、mass normalization和reset须作为同一状态接口，不能用未来token更新当前读取。它是重新选择历史factorization的模型分支，不是原softmax的精确缓存压缩。` 

拟文2：`通道数固定可使历史状态不随长度增长，却把细节、写入冲突和长程召回转为容量问题，训练graph与投影/归一化工作也未消失。ProtoT的受限小模型对照中，更长context的perplexity可反退，短context训练吞吐亦低于Transformer；单H100长context推理的局部交叉点不能代替全训练或服务SLO，可命名prototype更不认证内部推理faithfulness。EMA尺度、低mass或任务回归时，完整KV、有限kernel summary与已有SSM/hybrid继续共存，应联验任务质量、真实状态费用和端到端执行，而非因长度复杂度或解释性标签默认替换。` 不采用PMR clamp的普遍稳定保证，不要求为本段追加全理论。

**11882 mixed-bit World Model planning → INFER-TENSORRT-LLM / Ch49：拟现有分模块校准段之后一窄段。** 实际读Ch49 918–973相邻校准链；933/935已有上游LLM量化改变action DiT输入、按module layout/teacher/calibration与实际action结果验收，944/946（ProbeQuant）分开局部信号与同预算分配/物理大小；966/968跨timestep precision/search代理、平均bit不授真实成本。Ch48/50开篇及末尾实际顺读，target law与engine runtime不接管precision分配。已有正文承载局部误差≠下游质量/低bitweight≠真实kernel，加一差额仅是**planner搜索预算可反转同precision layout排序，必须作为验证joint condition**，不复写通用量化原则。建议935之后、`部分上游已经量化时`之前，原VLA实验不被覆盖。

拟文：`量化后的latent dynamics若由planner反复展开，precision layout的排序还要绑定搜索预算；同一组paired起点与目标下，encoder/dynamics的位宽组合应与rollout/优化迭代数共同验收，而不能先按固定总bit选出一个永久最佳layout。DINO-WM/Wall的weight-only小实验中，mixed INT4相对uniform的方向在严格planner预算下翻转，初轮差异的区间亦包含零；这只支持模块精度与planner预算的条件耦合，不认证encoder永远应更高精度。模型权重压缩、实际low-bit kernel与全planning latency是不同证据，额外搜索、dequant与校准仍付费；任务、预算或轨迹分布改变时重新回归，并保留uniform、局部高精度或原浮点模型，不从一个位宽或bootstrap读数授全world-model部署保证。` 主文不搬完整成绩表；具体M4/48GB、样本数与bootstrap边界只保留本日来源/末注，无端到端速度宣称。

### 第二小组：11534 / 11543 / 11639

**11534 Krause → MODEL-SELF-ATTENTION / Ch14：拟一机制段及一边界段。** 实际读81–134 mask/归一化/选择/恢复链及419–435 Projection-free Kernel Attention→signed/resolvent→recursive接口，Ch13/15开篇与末尾实际读。现419–423 Gaussian-kernel分支去掉Q/K projection；81–134可见support与kernel费用已有，但未承载**保留learned Q/K、先预定义spatial/causal W候选再按distance/top-k局部归一化**的不同路由/训练接口，不把它误写成projection-free exact执行。建议423之后、`非负归一化也可以被换成`之前。

拟文1：`距离核也可以保留可学习Q/K，而不移除寻址投影：先声明spatial或causal邻域，再在其中按query–key距离的RBF affinity选top-k，仅在保留支集内归一化后读取Value。Bandwidth、邻域与k分别控制软相似度、允许的边及实际混合人口；它们改变模型的局部交互先验，不是把一个已训练dense softmax无损变快，也不由局部聚类倾向推出所有Transformer必然collapse或多簇收敛。`

拟文2：`这类局部路由只有在真正只构造W个候选、完成选择并由稀疏kernel消费时，才具有所声明的O(NWd)计算路径；先算全pair距离再mask并未取得该执行收益，W与选择开销也不能省略。Krause的LLM对照保留全局attention、另加local shortcut，语言质量有持平及Macro-F1反退，因此图像替换/单H100生成结果不认证LLM加速或全任务稳定性。邻域过窄、选择或增设旁路费用不合算、质量回归时，保留全局Q/K/V、固定窗口或已验selector，不以Attention sink曲线代替任务和端到端执行验收。`

**11543 SPES → TRAIN-DISTRIBUTED-TRAINING / Ch36：拟两窄段。** 实际读425–492连续链：433–445 federated tensor type及三类expert参与集合，465–479跨model参数坐标与去中心canonical optimizer owner；Ch35/37开篇与末尾实际读。现正文有forward/backward/upload参与集合不同和canonical block optimizer，但未承载**所有client保存全部weight、只对assigned专家维护可训练gradient/moments、其余冻结、共同部分与expert union不同聚合**的驻留/训练责任设计；不是新的ZeRO parameter shard。建议既有三集合expert段之后、`训练collective通常围绕`之前。

拟文1：`Expert参与也可以在一轮开始前按client资源静态分配：每个client仍驻留全模型weight，但只为assigned experts维护可训练gradient与optimizer state，其余experts冻结，共同层继续参与训练。Coordinator对shared部分作FedAvg，而assigned expert更新按assignment直接接入并合成expert集合，再发布下一轮可用的全模型revision；两者不是同一FedAvg对象，forward使用某expert也不等于该client拥有其更新权。Assignment、base与round身份需同聚合协议绑定，不能把缺席expert当零更新，也不能用总active参数代替每个client的weight驻留。`

拟文2：`这种SPES分支降低本地训练状态和上传集合，却仍保留全weight副本及全模型下发，所报uplink下降不等全网络bytes同比下降，更不是ZeRO式weight分片。Shared/expert聚合、assignment迁移、非IID漂移与模型发布仍付费；受测A800/L40S及特定链路的吞吐接近RDMA也不授所有通信栈或下游质量等价。资源分配或聚合身份不清、稀有expert训练不足、质量或网络总费用回归时，保留共同expert集合/完整更新，或切回已验中心式与分片训练，不从局部state节省授任意异构集群可行。`

**11639 PACE → TRAIN-GRPO / Ch33：拟现prefix课程后的一个差额段。** 实际读380–421 GroupSize/课程→POPE→PrefixRL→A²D连续论证，Ch32/34开篇与末尾实际读；现403–411已承载冻结off-policy prefix与current suffix/去prefix迁移/全成本，415–419承载success-rate-triggered guided探索与提示移除。又实际读980–1046示范数量退火/外部skills scaffold，已有课程及去示范验收，但不承载此hybrid人口长度credit controller。增量只剩**initial policy shortest-correct prefix、长度逐步退火与以hybrid empirical pass-rate调长度credit的controller**，不复写条件采样所有原则。建议411之后、`人工或外部成功prefix不是唯一`之前一段即可。

拟文：`若prefix由initial policy的rejection sampling产生，可先选择最短已验证正确轨迹（没有正确项时仅有最短fallback），冻结其开头，再让current policy续写；随着训练缩短可见prefix，并按hybrid rollout的经验成功率调节长度偏好。这个成功率属于“给了何种开头”的conditional人口，不是题目的固有难度，prefix来源、长度schedule与difficulty coefficient应一起保存；只训练suffix也不证明原prompt分布纯on-policy或无脚手架迁移。PACE的受限数学对照中更长prefix未必更好，前置rejection、prefix prefill及长度reward仍付费，32 A100/batch64/group8训练并非免费探索。Fallback开头、无prefix质量或成本未验时，保留原prompt/outcome RL、经核正确的固定prefix或明确SFT，不把更短输出当成已经减少完整训练预算。`

### 第三小组：11683 / 11698

**11683 ThinkRouter → MODEL-SAMPLING / Ch20：拟一机制段和一边界段。** 作者实际现294–332连续读；314–319 Multiplex已有K次draw聚合单continuous state、接口/独立轨迹分责，前段request-static steering已有但不承载逐位置temperature-scaled confidence驱动discrete/soft表示切换。Ch19/21相邻开篇及末尾先前实际读。拟在Multiplex后、Parallel Sampling前补以下两段，不重写置信真值理论。

拟文1：`单条autoregressive轨迹还可按位置选择离散token或soft embedding，而不固定每步都作同一种聚合：先对temperature-scaled分布、在Top-k/Top-p/Min-p过滤及重归一化之前计算最大概率，低于阈值时采离散token，高于阈值时把top-j候选组合成soft输入。它调节下一步的表示接口，不同时维护多条可选择历史；temperature、阈值、filter次序、j与EOS交接必须共同版本化，不能把过滤后抬高的概率误作原router条件。`

拟文2：`最大概率仍是模型内confidence代理，错误答案也可能高置信；soft表示的接口、聚合与validation选点均付费，较短输出不自动证明完整服务更快或所有任务Pareto占优。ThinkRouter的受限对照里Random在一个coding设置更高，另一数学设置离散baseline更高，故要联验任务、真实decode成本与质量，而不按confidence授正确性。接口不可见、阈值漂移或质量回归时，保留离散单轨迹、固定soft分支及独立verifier/明确停止预算。`

**11698 Spiral → MODEL-TRANSFORMER-LAYER / Ch17：拟两段。** 作者实际555–635连续邻接，前二维token/latent依赖、565–583双时钟及585后共享block混合频率均承载depth预算，未承载causal sequence chunk pooling的多分辨率信息交接。现635后的历史边界仍保留，不双写Ch22容量论证；Ch16/18开篇/末尾先前实际读。拟在双时间尺度段后、`共享 block 的混合频率与校准身份`前。

拟文1：`层级也可沿序列分辨率组织，而不只让两个module持有快慢时钟：对因果chunk作pooling，让不同分辨率以共享core及各自recurrence预算更新，再交回细粒度位置。粗状态包含哪个chunk必须显式定义；g−1 shift用于避免当前位置读取尚未到达的同chunk信息，overlap另影响覆盖与质量，不把二者合称因果保护，pool/upsample、边界和位置身份须保持同一因果图。它改变多分辨率依赖与局部执行预算，不是对完整token recurrence的精确缓存优化。`

拟文2：`Pooling、交接和overlap仍有算量与细节损失，较少prefill FLOPs不等wall-clock、decode费用或长历史无损。Spiral在Pythia160M–1.4B/Pile250B/context4096的受限对照中，移除overlap会伤质量，而相关baseline也受益，不能把全部收益唯一归因于hierarchy。预算、chunk边界或质量不稳时，保留完整token recurrence、固定层深或显式CoT；需要可寻址历史时仍按第22章独立验收，不靠增加局部loop补回被合并的信息。`

### 第四小组：11715 / 11824

**11715 DICE → TRAIN-GRPO / Ch33：拟两段，不写Ch42。** 作者实际659–695的verifier→DrKernel重复profile/shaping→StitchCUDA局部feedback训练链；现有独立执行、reward hack、compile成本都有，但未承载固定prefix/suffix/import/wrapper的infill支持域→完整generation训练的信用与迁移身份。Ch42实际260–304请求pipeline/run identity负责执行，不拥有该训练分布改变；Ch32/34相邻已实际读。唯一ownerCh33，拟在StitchCUDA段后、Group Size前。

拟文1：`完整kernel生成的自由度也可以先受限，再逐步释放：固定kernel的prefix、suffix、imports与compile wrapper，只让policy填指定空缺，并按执行结果训练；之后再转完整generation。固定外部结构改变可行动作和credit支持域，不等于在完整程序分布上已经学会正确生成，infill与full-generation的数据、约束及reward身份须分别保存。DICE的这一路径用于限制可利用的执行漏洞，而不是把compile通过升级为程序语义真值。`

拟文2：`独立tests、已知hack排除和速度评价仍必须分开；DICE减轻后段execution下降但没有消除，L1的fast1还可弱于SFT，因此正确运行与快于参考kernel不能互相代证。固定wrapper构建、编译、重复profiling、搜索及训练切换均付费，预算或operator/shape/dtype/backend包络改变时重验完整generation。新失败、迁移不足或净成本不合算时，保留已验库kernel、明确受限infill与独立完整tests，不由新数据或reward更高授生产kernel可替换。`

**11824 REVIS → MULTIMODAL-REPRESENTATION / Ch23：拟两段。** 作者实际862–891几何操作定义/PCA层干预→failure链，另1155–1192视觉writer/reader/完整sequence与last-position matched干预、late branch/logit contrastive/静态anchor链：已有相关不等因果、视觉缺失≠语言覆盖、输入操作与层身份，但未承载先average grounded−blind再投影blind hall−unknown的条件方向构造与gate。Ch22/24开篇末尾先前实际读；拟在几何操作段后、Failure modes前，不添加另一个truth direction理论。

拟文1：`视觉steering也可先分离两类对照：把grounded与blind状态差分先平均，再相对blind时hallucination−unknown方向作投影/正交化；在校准对照中选择具有正向平均分离Δ的最深层，并用quantile阈值决定是否注入。平均、投影、层与gate的次序是干预身份，不能改成逐sample投影后平均；这只定义所测人口的一条方向，不证明已找到独立truth cause，输入根本缺证据时也不能凭steering恢复视觉事实。`

拟文2：`REVIS的方向提取与阈值各用100样本，层扫描、校准、judge和部署注入均付费；去gate时模型分支可能没有收益或collapse，较强干预会伤utility，局部CHAIRI也可反退。未披露完整硬件/运行配置的TPT不授统一延迟或免费可靠性。失配、blindness或质量回归时，保留原视觉输入、外部OCR/grounding和Unknown输出，分别验支持域、回答质量及干预成本，不把更少幻觉标签当内部faithfulness。`

### 刚完成的2602.12205 DeepGen作者必要读

原件[core-2](./supplement-20261008-core-2.json)精确URL `https://arxiv.org/html/2602.12205v1`，作者实际完整§2 Model Architecture/§3 Training/§4 Data/§5 Experiments/§6 Conclusion。拟采用窄命题：旧VLM final-layer connector→SCB取六个均匀low/mid/high视觉语言features经channel concat+two-MLP/connector，与128think tokens分开；SFT anchor配合多reward group标准化的训练分支仍须测能力trade-off。建议 **2+2+2=6**，受影响训练目标表述和直接负面反侧深入，不授新GRPO、真实reasoning或consumer-hardware效益。

关键位置：§2 Qwen2.5VL3B+SD3.5Medium2B、SigLIP+6层connector；§3三个stage（200K/400K/1500steps）及Eq3–5；§4 in-house10M生成/1.1M编辑与50K Nanobanana/500K QwenImage、Gemini2.5Pro文本标注，teacher/evaluator和多数据成本；§5 Tables1–7/Fig6直接反侧。stage2称unfreeze entire model但VLMLoRA，不能授全部参数unfreeze；Eq4 velocity squared difference叫KL，未证明实际分布KL（covariance/time factor条件未给）不采用等价；Eq5混合loss与Eq3 maximization sign convention需隔离，若后续采用该objective应只定点读Appendix8/实际优化定义，不遍历整份训练附件。本次采用SCB接口和可观测trade-off，不用该式保证训练正确。

Table6 w/oSCB GenEval.86等于full，w/oThink GenEval.87高于full.86，而WISE.68<.72/RISE11.7<13.3，不能授Think causal faithfulness或所有指标增益。Table2 WISE空间RL.70<SFT.82；Table4 RISE所有四栏下降（13.3→10.8），UniREdit77.5→75.7，SFT anchor没有保证全部能力保留。Table7全部1000steps，main table1500steps，不混合其数；Fig6 w/oSFT约300steps劣化与主文约1000不合成确定阈值。Table5 word-accuracy.7533仍低于GLM.9116/LongCat.8658/Qwen.8288，CLIPScore不是OCR真值。main hardware/precision/batch、重复/CI、SLO/全链成本Not Disclosed；5B compact不证明consumer-grade端到端。潜在owner MULTIMODAL-REPRESENTATION Ch23（SCB表示接口）或TRAIN-GRPO Ch33（credit/objective）待Source后实际比唯一长期差额，未锁不写。

### 2602.11858 Zooming without Zooming：作者必要Source-ready

精确原件[core-2](./supplement-20261008-core-2.json) URL `https://arxiv.org/html/2602.11858v1`，本轮作者实际完整§3（R2I/Alg1/ZoomBench）/§4（设置、Tables2–6、Fig5）/§5（dual-view、Table7/8）/§6（Table9 footnote/limitations）/§7；首次大输出截断的§4已单独完整补读，不把截断算已读。日期沿本日该项normal逐字段独核，不以提交日代公开日。

拟采用窄命题：工具crop只重呈已有原图证据时，可在训练先用micro-region视图生成teacher QA，再以box overlay+spatial约束把QA重新锚定到full image，配合consensus/difficulty filtering及DAPO，把部分test-time回读负担转成训练表示能力；**不是任何zoom都information-neutral**。如果global view在编码前已downsample丢了细节，crop提高有效分辨率就相对实际输入增加信息，训练不能补回部署缺失pixels；§6 Table9 footnote明确该例外。所称single-pass只限定无test-time tool interaction/单global-image路径，不授所有autoregressive CoT一个物理forward或无生成费用。建议 **2+2+2=6**，训练/部署输入身份与工具信息增量边界必要深入。

关键评价/反侧：74K合成、Qwen3-VL4B/8B及Qwen2.5VL7B DAPO无SFT，teacher GLM4.5V/Qwen3VL235B/crop生成和筛选仍付费，不能由无SFT推完整OOD能力保证。Table6同10K中box-in-image总体更高，但Color83.19低于Direct83.45，CountQA 74K32.40低于10K33.97；更多数据/box提示不是每项更好。§4文字把Qwen3VL8B baseline写61.52，Table2对应8B实际62.86（61.52属于4B），采用表值，不照录错归。Table5 DiG8B MMStar72.7高于ZwZ7B63.4，跨规模/数据对照不授所有proxy数据稳定胜出。

ZoomBench845问、六维度、crop证据+human-in-loop检查只是所定人口；regional accuracy是经验参照，不是形式或所有任务upper bound：counting即便crop也未解决，ZwZ仍有15.26 global/regional gap。relative-attention box coverage增加不认证实际必要因果路径/faithfulness或无遗漏grounding。Fig5约10×速度分母是ZoomBench每样本时间倒数、质量为另一组Table4平均，未披露完整硬件/precision/batch/CI/SLO不得搬成生产吞吐或所有任务10×。空间/多对象主文明确未广泛训练/评价，其他tool action/general agent distillability仅讨论，不作为已验证贡献。拟潜在唯一owner MULTIMODAL-REPRESENTATION Ch23（global/crop privilege→实际可见像素边界），Source后实际比较而非按工具名写Ch78；材料够支持该窄接口，STOP不遍历Appendix8–12。此项新增作者必要读，尚待非作者Source。

### 2602.11934 Robot-DIFT：作者必要Source-ready

精确原件[core-2](./supplement-20261008-core-2.json) URL `https://arxiv.org/html/2602.11934v1`，作者本轮实际完整III Method（Eq1–9、III-B/C）/IV Experiments（A–D、TablesI–IV）/V Conclusion。采用 **2+2+2=6**：旧噪声条件diffusion teacher features→clean-latent单次视觉student、全decoder-block training-only投影alignment与部署移除teacher/heads；S2-FPN us3/us6/us8从粗语义逐级融合细几何、CLIP text query→visual K/V cross-attention/2D RoPE、多view max聚合，给出可显式分责的语义/接触几何表示接口。Teacher SD2.1冻结，student weight-copy并更新，τ uniform[0,999]，归一化cosine alignment权重从0.1退至0.001；teacher features是该训练参照，不是物理几何真值。部署确定性只指visual backbone，后接Diffusion Policy并不因此变成整policy无采样/单forward。

评价/直接反侧：RoboCasa 24tasks每题50human demos/200epochs、50rollouts，frozen encoder-swap同Diffusion Policy；IV-A Baselines中的DIFT(SD2.1)对照也经manifold distillation得到deterministic Student，Robot-DIFT新增是DROID robot-adapted训练/所述multiscale接口，不声称所有DIFT对照在线stochastic或clean/noisy distillation首次由本篇提出。DROID额外manifold-distillation与standard pretrained视觉baseline数据不完全同预算。TableI原文DINOv3平均称0.27而表0.33，采用表；OpenDrawer Robot.60<DIFT.70、TurnOnStove.44<.58、CounterToSink.06<.08，不能授所有接触任务胜出。TableIII相同冻结backbone/downstream policy在geometry subset支持multiscale与annealing分支，但不是全部task/模态geometric cause。LIBERO10每task50seeds，16动作预测/执行8，OpenVLA单动作需运行8次对齐horizon，TableII .01s vs UVA.23s只原测单trajectory，main没给完整hw/precision/batch/端到端控制SLO，23×不迁移生产。

真实Franka Panda7DoF、wrist/third-person双ZED，四task每题20trials、31–36demos/10Kpolicy steps/16预测执行8；DINOv2 Sort.55>Robot.50、Open.60>.55，Robot Insert仅.35，不把提高均值授安全控制或可精确稳定执行。训练teacher/noise/projection/全block、FPN/cross-attention与policy head成本都计，部署heads移除不授完整训练廉价。刚体范围、rope/cloth/nonrigid与长horizon明确未核；SD2.1边界不授所有video teacher。拟潜在唯一owner MULTIMODAL-REPRESENTATION Ch23（clean/noisy privilege和多尺度接口）或MODEL-WORLD-MODEL Ch25按实际长期差额比较，不能因为机器人名默认主线或仅低延迟保留。该窄机制及直接反侧足，STOP不扩全Appendix，尚待非作者Source。

### core-1 2602.11965 MaT-LoRA：恢复已读的具名Source-ready

精确原件[core-1](./supplement-20261008-core-1.json) URL `https://arxiv.org/html/2602.11965v1`；此前必要作者读本轮按采用位置恢复，§3/4/5及完整§6/7实际有效。拟采用 **2+2+2=6**：独立per-domain LoRA的因子坐标/支持可能不一致，改用共同B/A与time-dependent小core F(t)，把future-domain更新proposal与时间身份/temporal evolution模型分开；F用matrix exp/RNN/MLP的不同归纳偏置，不把已有时间训练标签视为未来分布真值。采用的是受限shared-support参数化和验收，不授data stream与optimal weights必然diffeomorphic。

核心位置§4.2 Eq4–7共同row/column support→B F A；**rank-r独立adapter的跨时union support一般可超过r**，同rank共同basis表达要满足其support条件，不能由每时rank≤r推任意序列等表达能力或常数rank；§5.1 Eq13只固定basis/core-network参数不随T，不等完整activation/optimizer/history或running memory不增长。§4.1 translation lemma只说明已假定weight manifold的平移，不证明真实LLM参数/data动态存在这种manifold。§5.2 Assumptions1–3及Theorem2只作作者有条件理论背景，不采用其稳定/未来外推保证或完整证明；无需为这个有限BFA接口遍历AppendixA。

必要评价§6 Fig2/Table1–2：Rotating2Moons12domains×200/18°/noise.10，first9训练；linear2D coordinates直接投latent、移除标准token/position embedding，不是natural-language未来reasoning。AIC/NewsCLS/Yelp分类在unseen domains、3runs mean±std仅所定时序；不同core变体/rank/horizon共同验收，优势不认证时间t普适预测器。Table2 AIC MaT-LoRA训练740±18s高于Offline532±153/Inc402±77/Last241±31、test2.99s高于2.11/2.46/2.73，不能照录“仅marginal overhead/同延迟”为全成本证书。实验未给完整hw/precision/batch/SLO时Not Disclosed，不因parameter storage较小授端到端更快。Common support失配/shift突变时原独立adapter、末域/增量微调仍合理；ROADMAP真实LoRA owner为TRAIN-LORA Ch30，需实际正文比较，未授PRE/写锁。

### 11305 MisAlign actualowner PRE：拟Only，不加通用指标段

作者实际Ch66 91–119 EvalSpec明确定义eligible population/failure taxonomy/scorer/aggregation与目标链；220–244 conditional与joint population分账、不从行为classifier取latent alignment真值；575–608分布/scorer假设及有限数据不能修错scorer。Ch65/67开篇/末尾已实际读，集群公平和监控不取代评价构念/人群。MisAlign的Coverage(misaligned命中)与FFR(aligned误拒)、domain分类300human和StageII自动assertion分离在这些长期测量原则中已有承载，不提出新算法或可验证的全alignment保证。该具体taxonomy/分类实验仅报告，不声称现书已包含其具体harmonic AS式/数值；建议Only不造Ch66 diff。请root actual PRE裁决，不从传统precision/recall式映射自动保留新长期内容。

### 12275 OPCD actualowner PRE：拟Only/具体原则已有覆盖

作者实际Ch29 621–653：context distillation保留student state coverage，derived strategy冻结teacher读策略+student prefix/student仅prefix、同prefix on-policy更新，近文consent/用户隔离/精确删除/poisoning/teacher staleness/forgetting边界；686–709普通on-policy KD绑定teacher snapshot/refresh及额外generation/teacher forward，Ribbon局部prefix不授完整state覆盖。ROADMAP真实owner是TRAIN-SFT Ch29，不造TRAIN-DISTILLATION。OPCD的view-asymmetric同student prefix接口已有具体承载；top-k reverseKL近似和local consolidated数据/成绩反侧只报告，不声称现书已包含其实验或全概率目标。建议Only不造diff，请root actual PRE；已有数据/隐私/staleness边界不再换论文名复制正文。Ch28/30相邻开篇/末尾已本次实际定点读，不以PRE建议授写权。

### core-1 2602.12005 LaCy：恢复已读的具名Source-ready

精确原件[core-1](./supplement-20261008-core-1.json) URL `https://arxiv.org/html/2602.12005v1`；已有作者必要读，本轮按拟采用恢复§3/4、完整§5/6，不额外授新读数。拟采用 **2+2+2=6**：普通token NLL不区分不可接受事实续写与可接受同义/格式变化，训练用spaCy fact proxy×current high-loss选择把部分GT target换为<CALL>，其余token在排除CALL重归一化分布上学原GT；部署SLM提议CALL再由较大cascade续填。改变的是训练target与委派表示，不以loss/单token语法标签认证事实，也不把CALL就是少量经典置信cascade的新名称。Acceptability含保留GT意义/格式，不是任意所有真实事实等价。

位置：§3 single batch112文档/约44Ktokens、1.3B训练50B时Gemini2Flash acceptability及spaCy English/custom heuristic只是受限诊断；§4 mask及modified NLL与§5.1 inference共同定义接口。主实验334M GPT2-from-scratch/32K SentencePiece+CALL、dwiki3B、约50B/16epochs、ctx1024/full precision/340–440Ksteps为匹配真正GT-gradient token数，不等匹配全部forward训练费。训练每batch15%target CALL，部署greedy与Llama3.2-1B、running quantile把调用budget设22%，不能把两个预算混合成固定线上调用率；cascade tokenizer不同时一次返回可变成多个SLM tokens（尤其数字），共同prefix/token边界及消费需实际验收。

关键反侧：§5.2 FactScore+6.88%只wiki biography原人口，cascade自己FactScore34.2%说明返回事实也可错；§5.3把CALL logit设−∞下gold containment下降只是fact leakage行为probe，不证明权重完全无事实或已经删除知识。§5.4 Ignorefacts/Ignore以更多steps匹配GT-gradient token，等forwardsteps时提升消失（主文直接报告Fig10），CPU标注Table2 152h/Btokens不是免费预处理；比较LLM judge233h/A100或Rho-1 56h/A100不能把CPU/GPU hours等价。§5.5 NLU平均39.9 vs39.6仍有Hella28.5<28.8，不能授全部能力无损。§5.7不同mask变了评价目标人口，loss不与FactScore单调只该委派设置，不能反推一般pretraining loss无用。论文明确pilot、sometimes漏CALL、如何处理CALL后检索不是此篇完整解决；完整hw/batch/CI/服务SLO未给不补造，label/cascade/model-generation与结果核验成本都保留。拟实际唯一owner TRAIN-PRETRAINING Ch28（GT/CALL target职责）或TRAIN-DATA Ch27（proxy标注）须actual正文比较，未授PRE/写锁，不为调用名写完整Agent执行章节。

### core-1 2602.12078：混合递归算子的具名Source-ready

精确原件[core-1](./supplement-20261008-core-1.json) URL `https://arxiv.org/html/2602.12078v1`，作者已有必要读，本轮完整恢复§3/4/5/7，不增加作者读数。拟采用 **2+2+2=6**：递归状态计算既需要跨位置全局通信，也需要多次更新保持状态数值尺度；保留TRM双状态/递归schedule，把单次更新替换为Mamba2→Mamba2→Attention→MLP，另一分支用跨序列MLP-t替代attention。采用有限grid/puzzle里的混合通信与递归验收，不授纯causal Mamba可直接替换双向网格通信，也不授AR语言模型普遍改善。post-residual RMSNorm是实际数值干预，不由稳定幅度推任意递归收敛/Jacobian保证或所有pre-norm必然NaN。

§3 Hcycles3/Lcycles4–6，zH/zL与Qhalt沿用TRM；§4 attention6.83M与hybrid6.86M、hidden512/Mamba dstate128/headdim64/expand2，其他MLP组合参数不同，不称全对照匹配计算量。Table1 ARC pass@1 40.50<40.75，pass@2 45.88>43.88，K100/1000的候选覆盖增益不是正确候选选择概率。Table2 Sudoku hybrid66.5<attention72.2，hybrid-MLP84.2<MLP87.4；Table3 Maze80.6>60.8但checkpoint在6–85%波动，不能授稳定通用递归收益。ARC原MLP-t29.6 pass@2来自原论文、作者未重现，资源/参数比较不等同受控重复。

§5 ARC400puzzles/419inputs（19题有两输入），dihedral/color增强368150/约880每输入、逆变换+投票；K1000是增强池中的correct-anywhere覆盖，不当1000独立同分布解码。hybrid unique candidates339.5 vs266.6、vote entropy5.39 vs4.56，baseline top1share41.1 vs32.9/margin32.3 vs24，增加多样性可能损坏top1集中。hard/easy阈值15%使用两模型共同correct-vote平均，虽作者称model-agnostic，仍依这两模型结果定义，不授独立固有难度标签；hard246/easy173及hybrid-only31/attention-only23限定原人口。§7 compute-normalized评价尚待，完整硬件/precision/batch/训练CI与服务SLO未给。拟owner MODEL-TRANSFORMER-LAYER Ch17须actual比较递归通信/数值边界，未授PRE或写锁；必要机制及直接反侧足即STOP。

### 11541 INTENT actualowner PRE：Ch78期望计划成本与即时可支付性的小差额

唯一owner ROADMAP `AGENT-TOOL-CALLING` Ch78。作者实际顺读现Ch78 146–166 authorized provider、215–232 utility admission、349–395 retry/inflight与tool-value cache、430–470 monitor→Loop Boundaries、499–530后续intent门；相邻Ch77/79开篇/结尾已定点实际读。现文已覆盖效用/失败/预算比较、运行时硬停止和未知inflight不得猜重发，故不重写这些通则。尚未显式承载的是：按计划各step的intent-satisfaction与固定retry假设计算的期望成本，可以用于proposal排序，却不能当每个真实调用的余额reservation/支付凭证；风险折扣或缓存沿用尤其可能混淆这两层。拟仅在现utility admission末段（以“只读、低延迟且高度可靠的工具...”结束）之后、workflow diagnostic前置条件之前补以下一个连续机制/取舍段，其余正文不动：

> 当一次调用可能为同一目标反复重试，单次报价不足以比较整条计划。若每次尝试费用为c、满足当前意图的概率固定为ρ，并暂不计重试带来的信息与策略变化，几何试次数的期望费用c/ρ可作为计划级预算proposal；它不是最坏费用上界，也不证明工具结果正确。Planner可以据此比较候选路径或反馈高成本瓶颈，但执行器仍须在每次真实调用前核当前报价、剩余可用余额与权限，再扣减或预留本次费用。风险折扣、较好的历史成功率或沿用缓存计划都不能跳过这一步。该分工以额外预测/模拟及校准费用换取较少的意外重试；成功概率漂移、失败并非独立同分布、重试改了参数或先前调用仍在inflight时，停用该估算或重新规划，保留硬预算与原幂等/协调协议。

Source限定：本日root已独核§2/3/完整§4/6，采用条件固定ρ模型，不照录论文“pessimistic upper bound”为任意真实失败保证；γ<1是计划风险偏好、不是budget增加。765 BudgetStable/B50/synthetic价格/FR100仅报告，oracle/model费用不包含在工具价格预算，另测；拟段不声称真实所有工具安全无越界。Source通过不授写权，请root actual PRE与窄锁裁决。

### 12036 SPC actualowner PRE：拟Only/Existing，不重复课程链

唯一owner `TRAIN-DATA` Ch27，作者实际完整505–553 synthetic environment/typed composition/分解课程、622–673 policy-relative Sweet Spot与三轴coverage、1097–1116 online controller；Ch29 707–733明辨全同outcome的reward advantage失活与CE人口，Ch26/28相邻开篇/结尾实际读。SPC有向答案绑定生成的具体数据形态、199K/12K及local反侧保留日报；Ch27已经明确“current-policy rollout→correctness/group variance→revise/retire”、composed prompt与composition recipe/verifier lineage，以及组合器不拥有正确性。最终GT2通过不认证中间路径，可由现row/verifier身份分责承载。不是说现书已包含SPC数值绑定算法，也不把环境typed composition强称与SPC数学文本生成同实现；长期增量所需的生成proposal、课程人口、独立验证与原题回退均已具体承载。建议Only/Existing，不为算法名字造一段、也不把同GRPO objective误写为新estimator；请root actual PRE裁决。

### 12222 IDFT/DDT actualowner PRE：拟Only/Existing，理论强保证隔离

实际唯一owner `TRAIN-SFT` Ch29而非笼统按加权词落Ch27。作者实际完整123–148：reference-token概率门、detach/监督分母/完整可见历史、低概率罕见事实反侧、位置筛选不剪完整forward；253–271 teacher soft target/权重、teacher偏差及回退；707–753能力难度、噪声high-loss与有限budget tail selection。Ch27 109–137加权经验风险及1097–1116 checkpoint-coupled selector边界作邻接，Ch28开篇/末尾与Ch30此前LoRA邻接已实读。本文§3.1实际是reference-token loss乘 `p_t(x_t)^{gamma_t}`，其中 `gamma_t=exp(-phi_t)`，不是给外部teacher的固定样本权重；之前“teacher答案指数权重”只指离线reference人口，现细化此身份，**不采用**作者对参数梯度奇点、stop-gradient实现、γ调制必然防遗忘/OOD真值的强保证。Hinted Decoding另一个生成条件接口本轮不采用，未为之追加证明队列。

现Ch29具体已承载概率/相对gain只是监督proposal、loss位置/输入历史/梯度分母分离、阈值/噪声/长尾与forward费用回退；本文非on-policy RL、负熵差等式条件缺口及mask−1/−5/−10有限反侧留日报即可，不需要复制“更多权重并非更正确”通则或补未成立的理论。建议Only/Existing，不声称已书写其p^γ recipe或实验数值；若后续需要采用精确objective与gamma反向实现，须另一次必要证据而非本次安全命题外推。请root actual PRE。

### core-1 2602.12204 CRAM/SRCD：恢复已读的具名Source-ready

精确原件[core-1](./supplement-20261008-core-1.json) URL `https://arxiv.org/html/2602.12204v1`；作者已有必要读，本轮完整恢复§2/4/6/7/8/9，不增加作者读数。拟采用 **2+2+2=6**：固定attention比例只决定何时检索，不把重复检索结果转成可替代计算；CRAM以有界episodic KV buffer、irregular-gap CT更新、低rank semantic adapter及三路router，把已观测retrieval output用stop-gradient目标蒸馏成局部参数化近似。采用的是“是否调用检索”与“重复模式能否由近似器替代”的两层分责，近似误差必须与task outcome联合验收，不把神经记忆名称或生物类比当新机制。

§4 Eq2–8：CT离散ODE-style更新/time-gap gate，semantic rank=d/16；Lcons来自使用episodic retrieval的token，q=exp(−||fsem−rE||²/σ²)只是同当前retrieval输出的近似质量，不是语义真值。q的定义仍需要rE；主文未说明所有部署路由如何无检索在线取得当前q，故不授无需读取teacher/KV便有免费可靠gate、也不替作者补实现。§2 frozen GPT2 124M/355M线性probe的0.84/0.92可预测度只是该probe/数据/层统计，不能推全部LLM 88%attention因果可删或替代后无损。§5 optimality/necessity强理论不是本轮采用命题，无需全证明附件修复。

关键评价/直接反侧§6/7/8：SRCD N2048、5%queries、70%binding来自固定100patterns、Pareto gaps；1.5%=.05×.30仅所构造需检索人口的理论参照，不是所有序列lower bound。Table1 retrieval100%/attention.016同列Dynamics MSE1.211劣于Transformer.589及w/o consolidation1.198，不能说整个task无损。37.8×为训练过程中attention reduction，非总wallclock；语义adapter/路由/CT计算、consolidation scoring与早期cold-start仍计费。Table2只head重新训练、semantic/router冻结的transfer，不是完全零训练；Activity accuracy.181低于SeqBoat.386（§7.6），同样不能用48–52%attention少量替质量验收。§7.4 γ=.43±.04与人类曲线重叠不认证共同生物因果、内部认知或演化最优。至少50%recurrence/约3Ksteps为作者设置的经验条件，novel模式/长buffer范围/错误pattern改变时保留真实episodic读取、原attention或静态路由；完整硬件/precision/batch/全部算费/SLO未给。拟唯一owner MODEL-SELF-ATTENTION Ch14（检索结果参数化替代）或MODEL-TRANSFORMER-LAYER Ch17须actual比长期差额，未授PRE/写锁，支持/反侧足即STOP。

### 2602.12155 FAIL：刚完成作者必要Source-ready

精确原件[core-2](./supplement-20261008-core-2.json) URL `https://arxiv.org/html/2602.12155v1`，本輪实际完整§2 Methods/Alg1–2、§3全部empirical analysis/Tables1–5、§4/Tables6–8、§6/7。**2+2+2=6**：固定expert图像SFT之外，以当前policy在线图像与expert更新discriminator，再分别选择可微vector-field路径反馈（FAIL-PD）或仅scalar discriminator-feedback的CFM-loss-ratio surrogate（FAIL-PG）。实际增量是相同expert/current-policy分布接口下，feedback的可微性与flow更新路径决定训练费用/长程稳定性，非GAIL/GRPO名字本身，不授新通用RL收敛。

§2 PD不是每步展开全ODE：Eq2用局部线性single-step denoising approximation，故不能照录“exact/unbiased limit DDPG”到实际approx训练；t+Δt接近1的分母及t可用范围主文未给完整recipe，本次不采用全时域有效公式或自行修实现。PG Eq3用exp(CFM_old−CFM_current)近似ratio，Eq4称KL未给完整分布等价条件，不授真实density ratio/exactKL/所有flow无偏；沿用group normalization不是新GRPO。Discriminator自己是learned evaluation signal，去掉explicit preference/reward model不等无reward代理或无另一个model。Hybrid每prompt3policy+1expert、BCcold-start/25stepswarmup使两更新路径之外仍有training support干预，不能全归single组件。

实际设置§3.1：13K过滤后的GeminiPro3 prompt-image expert，每prompt仅一image；FLUX1dev policy/Qwen3VL2B-Instruct discriminator，DINOv3/FLUX对照，batch128/32NVIDIAH20，常规512²/1epoch400iterations/CFGoff。teacher生成、过滤、policyrollout、trainablediscriminator及gradient费用全部计，未给完整precision/全部wallclock/CI/服务SLO。§4同checkpoint启optimalCFG是另一评价配置，不混为§3CFGoff数值。

关键反侧：T1 400step PD UniGen62.17<DPO62.83/DPG84.14<84.25/UR3.3938<3.4183，800step PD才达近PG400，非每等预算胜出；Fig2 PG约450后collapse、PD到2000稳定只是该proxy曲线，不证明所有训练稳定或manifold preservation因果。T3加reward梯度后PD UniGen60.88<62.17，PG+FPO HPS11.75低于FPO12.56，反reward-hackingregularizer不授所有quality维度。T6 PD87.32仍低于Seedream88.27而正文称parity；T7 baseline overall表61.30、文61.61不混，Text52.87<Qwen76.14。T8 PDCharacters11.91>11.70但Arts10.16<10.32/Science9.59<11.24；HPS/UR是代理非直接真实human全偏好。离散Xomni与Wan video另expert/模型的T4/5只局部扩模态，未验证所有continuous/discreteflow。只保留conditional feedback-path与独立质量/费用验收；expert偏差、collapse、局部近似或质量回归时回原SFT/受控reward，支持/反侧够即STOP，不遍历Appendix。实际owner待Source后比真实Ch24生成训练接口与Ch33既有目标，未授PRE/Books。

### 2602.12160 DreamID-Omni：刚完成作者必要Source-ready

精确原件[core-2](./supplement-20261008-core-2.json) URL `https://arxiv.org/html/2602.12160v1`；作者本轮实际完整§3/4/5/Eq1–5/Tables1–6。**2+2+2=6**：单人identity或单全局caption不足以绑定多人视觉identity、voice timbre与谁说哪句；双stream video/audio以reference序列concat、结构条件elementwise加法分开可选输入，同身份视觉/音频reference共享预留RoPE segment、target audio频率按Lv/La缩放，另用具名sub_k anchors贯穿video/audio/jointcaption。采用reference身份与内容/结构条件的明确绑定接口，不把concat/Syn-RoPE名称授数学 disentanglement 或任意跨人串扰为零。

关键方法§3.2：M≫L预留索引条件不能由RoPE periodicity保证互identityattention总是低或正交，训练学到关联也不等identity/语音真实授权。§3.3 10K in-pair loss排reference区→20K跨clip完整loss→20K全task4:3:3训练；mask只是目标loss，不证明输入无法copy/信息独立。参考clip是否同人物/声纹的匹配/数据权利仍依数据管线，不自行补“无标签/无需匹配”。§3.4 text/reference两stageCFG分别对两stream应用，有多个条件forward与采样费用，不授单次forward或identity绝对保持。

评价§4：Ovi初始化/lr1e−5/batch32/M150，IDBench-Omni仅200=100R2AV+50RV2AV+50RA2V；ArcFace/WavLM cosine、ViCLIP/CLAP、Whisperlarge-v3 WER与SyncNet为不同proxy，speaker confusion由Gemini2.5Pro judge，SpkConf.08不是实际所有人真实归属错率。完整硬件/precision/steps耗时/重复CI/SLO未给，teacher caption/data清洗与双stream全训练费不能由unified参数省略。主文Table引用有错位（RV2AV说Table4实为Table3，duallevel文称Table6实为Table5），采用表caption，不合并错表。

直接反侧Table2 R2AV AES.618<Wan2.6.632、PQ6.290<6.391；Table4 RA2V SyncD8.659>Humo8.323，优均值不等全同步更好。Table5 w/oSC SpkConf.26而full.08/w/oSynRoPE.12只是多人原切片控制，不能从score认证内部因果必要/形式身份分离。Table6 OnlyIR IDsim.692/timbre.504高于full.674/.493但ViCLIP差，正文指出copy-paste；OnlyCD CLAP.287高于full.282，阶段也非每指标更好。不同阶段/task支持和可能预算混杂不能由naiveMT一行证明所有弱→强curriculum普遍最优。拟唯一owner真实Ch23多reference表示绑定或Ch24生成conditioning，Source后actual比较；该窄身份/条件接口与直接反侧够，STOP不遍历user-study/所有数据附件，不授人物真实授权/安全生成/实现复现。

### core-1 2602.12262 T3D：恢复已读的具名Source-ready

精确原件[core-1](./supplement-20261008-core-1.json) URL `https://arxiv.org/html/2602.12262v1`，作者已有必要读，本輪完整恢复§2/3/4/5/7及原已取[必要ablation](./supplement-20261008-t3d-ablation.json) AppendixD、[reference schedule](./supplement-20261008-t3d-reference.json) C.2，不增加作者读数。**2+2+2=6**：少步masked-diffusion不仅匹配clean teacher最终文本，而用同一teacher实际decoding order得到中间mask状态和最终answer pair；implicit discriminator以teacher/reference样本条件likelihood比较，另按早decoded token加大path CE权重。采用的是训练状态身份与压缩步数验收，不称所有学生真实on-policy占用分布已覆盖/新GRPO，也不把DDO直接等同实际reverseKL。

§3 Eq5–10 teacher来自同pretrained SDAR，生成数据未用groundtruth答案但teacher错误仍能入训练，prompts来自MATHtrain/PrimeIntellect；SFT是BespokeStratos另人口，不授纯目标same-data因果。§5.1 lowconf remask/BS4 steps4，每步一token，记录最终decoding order再mask恢复中间状态、mix random inputtokens；所有训练full-param/8A10040GB。AppendixC.2 reference每10globalsteps以preceding-round student更新并在round内固定，teacher与reference不混成永远同一frozen模型。D中“random initialization”与主文random inputtokens术语未给权重随机初始化证明，不擅自宣称重新随机初始化整个student。C.2“best-performing”选择criterion未完整给，不给无validationleak证书。

§4.2 shared intermediate marginal是Assumption4.2，student初始化teacher/仅teacher训练不保证更新后 pθ(xt)=pφ(xt)；因此只采用teacher-trajectory conditional训练，不授学生deployment联合KL最优或factorization error单调下降。Eq7 sigmoid外置conditional expectation与普通每sampleDDO有区别，DDO upper-bound/理论分析不是本次保证依据，不能由优化上界推真实reverseKL已最小。早token权重来自解码stepπ而非真实因果credit。

关键评价/直接反侧：T1 1.7B TokPS4平均T3D22.27<dParallel22.60，TokPS2 code部分低于原模型；T2 restore full decoding时1.7B四项56.8/78.01/41.2/57.32均低于原59.4/80.59/45.2/59.76，4B GSM89.31<89.84/MBPP54.2<58.6，不照录“无full diffusion损失”。D Table5 DDO-alone12严重退化，random+path69vsbase68仅该MATH切片；DTable6完整58.6<DDO+path60.6，组件组合非所有compression regime最优，main4Bfull MATH70与此69不当同一次数字。λ.2经验并非通用阈值。

T3 dynamicthreshold.9/temp.1不同staticfull，HumanEval accuracy29.27<original33.54虽latency.26<.73；GSMsteps83.03>71.12虽TPS843>580、长度312.48>249.52，不能由总体叙述授所有更少steps。math latency还混长度721.90→525.50，matchedmodel/hardware/完整precision/batch/CI/SLO未给，不把TokPS当端到端加速倍率；teacher生成、reference更新/采样、likelihood与fullparam训练费用另计。trajectory/order/压缩budget失配或原full-step质量回归时保留完整decoding、clean自蒸馏/可信SFT并独立验收。实际owner候选Ch24生成范式或Ch29蒸馏状态接口须Source后actual选一，支持/反侧足即STOP，不遍历全部证明与数据附件。

### DeepGen/Zoom/Robot-DIFT actualowner PRE：三项拟Only/Existing，保留各自局部差额

作者实际Ch23完整16–57输入/坐标/artifact与下采样边界、98–138局部证据/多层summary→producer×consumer接口、675–735多目标/噪声监督/训练特权轨迹蒸馏，以及284–304参考音色分责；Ch22与Ch24相邻开篇/末尾已按ROADMAP真实路径实际读。以下三个具体比较分别请求root PRE，不以Source通过自动授已有覆盖或写锁。

- **12205 DeepGen，唯一 `MULTIMODAL-REPRESENTATION` Ch23，拟Only。** 实际117–123明确访问哪层与summary/空间token分开、producer层×consumer层/位置及训练驻留成本。SCB六层low/mid/high channel concat→MLP/connector后由SD3.5消费，与分类query融合、语言多层注入是不同局部consumer；现文不含其生成器接线recipe，不能声称该具体实现已在书中。但拟采用长期原则只要求producer层与consumer任务/位置/预算共同身份、末层/多层在任务质量/细节切片和费用下可共存，已具体承载。128think tokens与SCB的二维消融、LoRA/stage/质量退化留日报，不授joint causal faithfulness或新GRPO，故不为换consumer名字复制多层表示通则。
- **11858 Zoom，唯一Ch23，拟Only。** 实际16–53已分别绑定实际输入像素、preprocess/encoder坐标与下采样丢失不可补造，131–133要求同pixels换config/同config换pixels控制；717–723训练特权工具轨迹→部署普通VLM与不能推实际执行/无损蒸馏。Zoom新增microcrop QA→box-overlay full-image reanchor是具体合成数据recipe，可保留日报但不是原文全部已在书中。长期判断是工具是否增加实际可见信息与训练期目标能否在部署输入中成立：global编码前丢pixels时crop可能新增信息；同实际pixels重呈则可尝试蒸馏，但teacher consensus/attention和single-image不能授faithfulness/单物理forward。这些输入/特权/费用分责可由上述具体段联合承载，不强造同义段。
- **11934 Robot-DIFT，唯一Ch23，拟Only。** 实际117–123空间细节与layer/readout、688–714监督接入空间/训练与部署移除head成本、717–723训练特权不授环境事实已具体承载。DROID-adapted diffusion features、S2FPN/coarse-fine及clean/noisy teacher projection仍是特定配方；DIFT对照也deterministic distillation，不能把本篇的命名当首次一般蒸馏。本文未隔离多尺度之外所有DROID/representation因果，所拟长期原则只保留训练teacher/噪声身份与部署policy消费者/空间分辨率联合验收，已经具体承载。0.01s/23×、geometry subset和真机负侧留日报，不声称Ch23已有其所有实现或实验，更不移到Ch25 world-state保証。

三项均有真实局部机制/实验贡献，Only不是贡献前EX；现文本对其长期采用命题已足，建议不追加Books。若root认为其中consumer/输入差额仍需正文，请只对具名未覆盖命题另授窄拟文，不扩大附件。

### Agent 2602.11340 BLPO：刚完成作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL `https://arxiv.org/html/2602.11340v1`；作者本輪完整§3/4/5/Eq1–11/Alg1/Tables1–2、必要AppendixA官方HTML定点实读。**2+2+2=6**：多张错误图像同时进prompt optimizer会受视觉context限制；只换普通caption可能遗漏评价任务细节。BLPO把caption prompt q与judge prompt p分开，innerloop以“该caption导致的p更新，在原图label上减少多少judge loss”给q打分，再用选中q支持outer p更新。**Judge f(x,p)仍读取原图**，text caption是optimizer中间证据，不是把最终judge静默改成caption-only，更不是label/真实安全authority。离散prompt的gradient只是概念近似，实际GPT-o3更新文本、模型weights冻结，不授真实可微bi-level全局最优。

§3 Eq9 score是在sampled minibatch上看更新前后loss差，inner history的候选/得分不能代独立test；优化q的目标是当前p-update utility，不是caption忠实度或原像素完整可逆压缩。§4三judge Qwen2.5VL32B/Llama4Scout17B16E/Maverick17B128E、GPT-o3 optimizer、temp0、最多5outerrounds/max10error例；API版本、重caption+候选judge复评分及搜索费用都计，完整hw/precision/batch/总API费/CI定义未披露不补造。少imagecontext不等低全链cost。

必要AppendixA（官方HTML§AppendixA，已定点实读不遍历B/C全部prompts）：训练/eval与test分别100AGIN、200SeeTRUE、140ImageReward、110UnsafeBench；AGIN按score1–5采样但defaultjudge要求7点，ImageReward A称1–7而main§4.1.1称1–5，保留label/输出schema冲突，不自修为统一量表。该平衡小人口非自然图像先验，test采样细节不授全面leak-free；inner评估与训练池共享不能把所有gain当新泛化保证。T1 Qwen AGIN BLPOAcc.14<TextGrad.22而F1同.17；Scout ImageReward BLPOAcc.36<APO.37，SeeTRUEF1.77与TextGrad相同；Maverick AGINAcc.38与TextGrad同，并非所有基线全指标被支配。T2所有Scout局部优于固定caption/直接judgepromptcaption，支持该中间文本适配，不认证caption因果必要、全规模稳定/安全judge真值。T1ScoutUnsafe .83/.84与T2full .81/.82来自不同表且未同一run说明，不合成单性能点。

Caption漏细节/label或task变化/新judge版本/搜索成本失配时保留直接images、小errorbatch/固定prompt、人类或独立annotation；原图始终是评价证据，captionproposal应保留来源和被选历史。潜在唯一owner实际Ch75PromptEngineering或Ch66evaluation由具体caption→p-update接口比较后确定，不以MLLMJudge名写安全保证。必要机制/小人口/直接反侧足，STOP不遍历所有优化prompt附件；尚待非作者Source。

### Agent 2602.11409 TRACER：刚完成作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL `https://arxiv.org/html/2602.11409v1`；本輪完整III Methodology/IV Results/V、Eq1–24/TablesI–IV。**2+2+2=6**：整条对话平均surprisal会稀释局部loop/工具-用户协作失配；分别保持Agent/User actor身份、content-filtered surprisal、semantic×lexical repetition及action-observation/agent-user距离，再以MAX-composite step score和top-k tail均值+worst-step聚合。采用可观察异常人口与稀疏episode测量，分开token置信/重复/交互两方，不授score即真实failure概率或可替代执行authority。

III-B filter排高概率/stopword/纯数字，空集合记ϵ；其content选择依实际token/概率，作者声称unbiased conditional entropy在此随机筛选下不作为本轮保证，numeric ID/金额等可能关键的遗漏只为工程推断，不称论文已测。III-C semantic×lexical最大近邻window repetition、coherence是embedding距离不是真实task progress/执行可行性，字面重复也可能是必要复述；III-D heterogenous分量的α/β/γ、tail比例k/w及embedding/tokenizer必须绑定，MAX不使跨量纲proxy免校准。Agent/User separate score的subadditive不等因果责任分配或严格风险相加；数值低不能跳外部核验。

III-E公式failure bound明确依risk-dominates-hazard `λ≤min(1,c r)`、tail-sparsity残差η、w<1和长度K；这些是假定真实hazard被score支配，验证ranking不证明这个条件普适，不能给生产概率上界/安全保证。只采用测量结构，不扩AppendixA全部证明。Logprob/embedding提取、缓存/window相似度及tail排序有成本，第三方model/user无logprob时去掉U改变feature合同，需重新校准而不是称相同保证继续成立。

IV实际τ² airline50/retail115/telecom114 task、final-state assertion定义failure，三个API模型gemini2.5pro/flash/gpt4.1mini经LiteLLM/functioncalls/temp0/logprob。TII combined全九格AUROC/AUARC优于所列baseline只该模拟人口；TIII agent-only geminiflashAirline.650<SemEnt.721、proTelecom.647<SAUP.671，user-only proRetail.489<SemEnt.576，不能声称各方单独必有优势或原因被唯一定位。TIV aggregation在held-out validation episodes调参、test评价，支持MAX该人口排序，不自行补split数/全部重复CI（主表无CI）。Early-warning以failed trajectories首越threshold、除最终总长度报告20%内比例；阈值“based on AUROC”具体operating selection未全给，不把retrospective failed-only命中率当在线FPR/真实wallclock或20%时必可恢复。AUARC是按uncertain episode拒绝的离线选择，不证明真实干预后task成功增加/安全救回。完整hw/precision/batch/APItoken或wallcost/线上SLO未披露。模型/任务/用户policy、filter或threshold漂移时保留分量诊断、typed tool/外部outcome gate及原hard停止，未知结果回协调；必要支持/反侧足即STOP。潜在真实唯一ownerCh66测量或Ch80协作需actual比tail measurement与actor接口，未授PRE/Books，尚待非作者Source。

## 本轮当前层补记（覆盖上述历史停点，非完成声明）

作者必要Source **57/57**：本作者55项＋root VLAW12063/CATTS12276两项均实际必要读且具名持久。普通未读 **0/57**，全部已非作者必要复核，非下载或摘要计读。原七项BAO/LUVE/GigaBrain/HAIC/JEPA/SCoT窄命题通过，UniDFlow中心隔离；不重计原已读Source。

非作者必要独核层 **57/57 arXiv＋1/1 Lockdown公告**的研究证据仍有效；首次公开日权限需分开：root DAY发现Submitted/v1 Updated/DOI Created与一般政策组合不授逐ID公开，作者一次CL/CV/AI官方月表定位43/57、day fallback400后STOP。57全部移日报§5日期保留，不计确定本窗新增或本日新整合；原30冻结，§3确定31=原30＋官方Lockdown1。36 actualPOST正文和Source/PRE仍有效、不撤，每个本task ownnote(含root INTENT/VLAW)已只追加事件日未证说明；18篇论文具体Only与11737/11767/UniDFlow三中心争议保留，不降分或把普通未读伪受阻。共同公开日精确请求与57 ID/有限恢复在[本轮日期恢复](./supplement-20261008-public-date-recovery.json)，未来仅定点重开归属；所有正文研究移同日报§5，不建平行账本。普通Source/owner/写回0，root已实际修后六部分DAY通过，原30仅冻结不重认证旧日期推定；完成态V3/冻结/链接及限定diff-check已再次PASS；本日结束，不换日，不stage/commit/push，不改他日/索引/LS。

当次机械复验：运行前dirty完整baseline的30候选表行逐字保留、原§4连续正文与原窗口均true；本日进行中V3 schema/consistency PASS；语义整日与完成态未验，不签DAY。限定diff-check PASS。不从HEAD覆盖baseline、不stage/commit/push。

### 11965 MaT-LoRA actualowner PRE：Ch30共享basis到未观测时间proposal的小差额

唯一owner `TRAIN-LORA` Ch30。作者已实际读183–244共享方向/谱core/参数生成、591–648共享坐标与merge验收、748–790适配支持域；当前再顺读201–224完整共享模块邻接。Ch29现SFT目标/teacher边界与Ch31开篇偏好训练交接不承载时序adapter预测。现Ch30 211–213已有共享左右basis＋module小core、rank/容量/费用与独立adapter回退，239的hypernetwork也已有输入生成adapter proposal；不重复这些通则。尚需区分的是**module/task内插选择**与**把尚未观测的时间当外推输入**：共同basis可节省逐时参数，但预测时间core不等于未来域已受验证。拟在现共享模块两段之后、“共享也可沿被选中的FFN行组织”之前补以下一段；若独核认为具体conditional generator与support验收已足以覆盖，可裁决Only而不强制diff。

> 共享方向还可以跨时间，而不只跨同一checkpoint中的模块：让共同左右basis保持固定，把小core写成时间的函数，再用它提出尚未观测时段的低秩增量。这里时间是预测器的输入，未来域的质量仍是待验收对象；每个时刻的独立更新都低秩，不代表它们联合的行列支持仍落在同一个小basis内。采用这条分支须分别验证共享支持、时间预测horizon与突变切片，不能从已见时间的拟合推出任意未来漂移可外推。Matrix-exponential、RNN或MLP core各自增加模型与历史状态计算，固定basis参数较少也不等于完整训练/运行内存恒定或更快；[受限时序分类对照](https://arxiv.org/html/2602.11965v1)中训练与测试时间仍可高于普通适配。支持失配、突变或外推质量退步时，停止发布预测增量，保留最近已验收adapter、逐域独立LoRA或增量微调。<!-- source-family:SF-2026-ARXIV-2602-11965 -->

不采用diffeomorphism/任意rank-r序列等表达/稳定理论保证；Source已独核，等待actual PRE及root窄锁，无写权。

### 12005 LaCy actualowner PRE：Ch28 GT目标与委派目标分责

唯一owner `TRAIN-PRETRAINING` Ch28。作者实际顺读现30–117目标与完整邻接：NTP局部GT、masked mean/normalization、预测方向和future-token/teacher目标、记忆压力分支；相邻Ch27数据provenance及Ch29目标/mask边界已定点核。当前目标分支未明确承载“high-loss×fact proxy选中位置换CALL、其余位置排除CALL重归一化”这个训练职责变化。数据proxy只作Ch27 handoff，不重复标注章、不因CALL名把本项写成Agent实现。拟在现Next-token目标batch mean与课程权重两段之后、预测方向小节之前补以下一段：

> 普通NTP让每个有效位置都学习原GT，却不区分难拟合的事实续写与可接受的措辞变化。一条受限委派分支以事实标注proxy和当前高loss提出候选位置，把这些位置的训练target改成CALL；其余位置仍学原GT，但在排除CALL后重归一化的分布上计算loss。它改变的是模型学习“自己续写还是请求续填”的目标，不是从高loss直接认证事实错误，也不是证明参数删除了事实知识。训练中的CALL配额与部署时的调用预算是两个验收对象，[pilot对照](https://arxiv.org/html/2602.12005v1)的15%训练target与22%部署budget不能合并为固定线上调用率；cascade返回也可能错误或跨越不同tokenizer的多token边界。Proxy标注、cascade生成、真实结果核验及所有forward都须计费，匹配GT-gradient token数不等于匹配总训练计算；Ignore/Ignorefacts屏蔽目标的对照在匹配forward步数时可失去原训练收益，因此不能把等GT-gradient预算的差额全归因于事实委派。Proxy失配、漏CALL、委派质量或净成本退步时，降低/关闭委派目标，保留普通NTP与独立质量验收，不以局部FactScore或loss代替事实真值。<!-- source-family:SF-2026-ARXIV-2602-12005 -->

Source已独核，待root实际PRE及窄锁，不自写Books；不授权重无知识、免费标注、检索已实现或cascade真值。

### core-1 2602.12271 MonarchRT：恢复已读的具名Source-ready

精确原件[core-1](./supplement-20261008-core-1.json) URL `https://arxiv.org/html/2602.12271v1`；已有作者必要读，本轮完整恢复§2/3/4/5/7，不增加作者读数。拟采用 **2+2+2=6**：视频3D token的周期性dense交互不必是低密度top-k；将稀疏**因子**产生的dense attention近似与直接删attention edges分开，以视频维度完整分配到block轴的布局对齐、tiled小块和受限finetuning调整误差/计算。采用这种近似结构与发布验收接口，不授所有video attention必非稀疏，也不由case分析认证完整attention普遍exact。

方法必要位置：§2 dense softmax→交替优化Monarch因子、无需显式完整A，但新方法沿用既有MonarchAttention，不说本篇首次发明；§3.2–3.3 Eq1为positional可分D+sparse semantic S+noise的**模型假设**，Case1–3未穷尽混合semantic block，global fullrank可与block lowrank共存；§4.1 exact positional分解限S=0且整条f/h/w维度各归一个block轴，flattened-index近邻不等视频邻接。§4.2允许在固定baseblock上细分/parameter tying恢复原族的表示包含关系，不等固定训练/finite refinement下质量必单调；§4.2 tile数正文先c1²c2²后example c1c2记述不一致，不采用字面全kernelrecipe/完整strict theorem proof。§4.3 finetuning减少refinement iteration、custom forward/backward仍需训练；α/c跨query/KV frame在HBM且frame维度二次，query chunk mini-sequence是峰值内存控制，不是取消所有quadratic工作或KV存储。

必要评价§5完整T1–8：Self-Forcing与4-step Wan是**注入DMD训练阶段**，50step Wan另diffusion loss finetune；§5.1标题/Setup称training-free但baseline/mainresult明确trained，不把T1/T2当零训练质量。T2 4step quality.842<dense.846、semantic.788<.800、total.832<.837；50step quality.841<.846/total.835<.839，不能照抄allfidelity无损。T1仅一行没有所称14B独立结果，未采用全14B证书。§5.2 T3/T4是training-free另一人口，Monarch90%与trained95%不混；SVG/Radial的85%为overestimate并保留dense首step/首block，oracle top-k成本也不当可执行free baseline。主§3抽样5heads/layers:firstdenoisestep top-p说明所测密度，不普遍所有videohead。

关键效率与直接反侧：T5 B200480p s.95 Monarch5.97ms慢于FA4.53/VSA4.02，T6 B200480p.95 .95ms慢于FA.79；各密度不授全面最快。Kernel最高11.8×不等E2E；T7 RTX480p81frames Wan7164.56→4866.97ms、T8 SelfForcing8309.06→6094.45ms是指定训练/4step/分辨率/GPU人口，H100收益另列。SelfForcing720p RTX5090因KV OOM未E2E核，不能从720p kernel测量补真实部署；最终16FPS另加torch.compile且仅480p，非任意interactiveSLO/首帧/长会话保证。训练、refinement、布局/tiling、核编译与KV预算均计费，主必要段未给完整trainingdata/hw/batch/CI就不自行补造。拟唯一owner在MODEL-ATTENTION Ch14（dense近似vsedge删减）与视频生成Ch24间须actual比较，以机制owner为先；未授PRE/写锁，完整proof/附件不扩读。

### Agent 2602.11513 DEL：刚完成作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL `https://arxiv.org/html/2602.11513v1`；作者实际读完整§3/4/5/6及Impact，新增必要读一项。拟采用 **2+2+2=6**：在诚实但好奇的cloud split接口下，低维编码后用有界binomial stochastic n-bit表示同时决定上传带宽与扰动，再用server端针对扰动分布训练的soft prompt恢复部分质量。它把发送表示、随机化机制与下游适配分责，不把“latent非明文”当隐私保证，也不由低ASR认证所有泄漏被消除。

必要机制：§3.2 cloud知道机制、不知道实际noise，local tokenembedding/encoder→传输representation→cloud decoder/model；§4.1 Eq7 C4训练encoder/decoder，输入v∈[-c,c]^d，以u=2^n−1、p=(A+v)/(2A)抽K~Binomial(u,p)再映射回[-A,A]，不是已有Gaussian noise之后只确定量化的同名包装。Theorem4.2实际给f-sto与Gaussian tradeoff的±γ界，不能省γ直接当精确μ-GDP；Remark4.3等Gaussian隐私/方差只在指定有界坐标、A/σ和渐近条件，‘免费’不推广任意输入。c=C/√d的逐coordinate条件并不由一般L2≤C自动推出，必须核编码输出边界；本包不认证所有sequence/request-level GDP、连续上传组合accountant或完整理论证明。§4.2只训soft prompt，LLM/encoderdecoder冻结；prompt依对应扰动机制/训练数据，server端训练与公开C4迁移分开，不把noise修复成还原原敏感query真值。

完整评价/直接反侧§5 T1–8：c.05/d=b/32，generation100soft tokens、NLU20；binary search在evaluationdataset校准相同embedding inversion ASR，再比COH/PPL，**同ASR不是同DP guarantee**、更不是普遍攻击界。Input-inference BERT另攻击，main默认embeddinginversion，不能授adaptive/newdecoder攻击覆盖。T1 LlamaWiki ASR.02 DEL.562<InferDPT-localLlama.742；T5 MoE16B .02 .586<InferDPT.664/72B .02 .606<.648。T3 MRPC4bit ASR.02 AUC.590<metricDP.598，2bit .02 Acc.703<.711，低bit更小并非全utility无损。T6 C4迁移严格ASR.02 LlamaWiki DEL.514<InferDPT-localOPT.665，不能照录全跨域优势；T7 μ52prompt迁μ40 PPL35.91差于目标prompt32.09。T8 d32严格μ20优于128，而宽松μ60 d128更好，只给受限压缩/噪声切换。

主表T2标题‘Accuracy’但正文/Table1口径COH混用，数字不当分类accuracy；COH/PPL也不等事实正确/隐私强度。通信按n bits/coordinate×d的payload变化计，不自补network RTT、clientmemory/hw/batch或全生成SLO；编码器/decoder预训练、softprompt+100tokens、随机化与多次query费用另结算。输入边界/公开训练数据/部署noise或适配质量失配时，停用该发布路径，保留更保守扰动、其他安全split部署或经明确同意的本地执行；具体隐私owner须actualROADMAP/正文比较，不自动因privacy名称写通用安全保证。Source/PRE未独授，不扩全proof/附件。

### Agent 2602.11524 ADMIRE：刚完成作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL `https://arxiv.org/html/2602.11524v1`；actual完整§3/4/5/7/Limitations，必要[官方附录](https://arxiv.org/html/2602.11524v1#A1) A.1与B.3/B.4.2/B.5–6（HTML482–499/583–660）已读；新增作者一项。拟采用 **2+2+2=6**：成功轨迹生成并随新成功路径更新里程碑，按终局人口给成功轨迹仅hit奖励、失败轨迹进度底值＋hit，改变step credit而非新GRPO。§3 Eq6–11有序pointer只核当前milestone，SentenceBERT动作描述cosine不是独立GUI-state验证；k/K为trajectory统计不改成已核逐步因果progress。Eq13 group所有steps归一，保留长度人口身份；退火是可选scaffold而非必要保证。

直接反侧T3 7B MobileMiniWob adaptive61.1<static-human63；§5.3不退火62>完整61.1。T4 GRPO ALFLook63.6<66.7process；RLOO WebScore80.7<process80.8，DAPOPick93.8<94.9，不照录allsetting领先。§5.4 crossdomain另训1.5B并非GUI模型zero-shot外推。AuxGPT4o生成/修订与processjudge、8A80080GB/32AVD、20step、mini128明确披露；B.4.2校准500pairs .75匹配81.3%<GPT4o85.39%，70×只该matcher批次。B.5完整epoch187.99s>outcome166.83(+12.7%)、posttraining人评4.42非全部在线milestone真值，B.6末coverage92.7%非覆盖所有任务。没有成功轨迹的启动缺口、proxy误匹配/错误更新与额外调用费保留，失配回终局reward/固定经验证rubric。唯一owner训练reward需实际Ch33比较，不自动写执行GUI章；Source/PRE未独授。

独立Source裁决补充已收到并保留：Algorithm1(HTML394–477)逐步k与正文Eq11 trajectory count身份不同；p=min(p+1,K)未锁已完成末项、重复hit仍可增k；K=0空初始化/除法guard未说明。本包仅保留adaptive milestone＋终局非对称辅助信用，不把algorithm授为完整可执行recipe，不扩代码修复。

### 12271 MonarchRT actualowner PRE：唯一Ch14稀疏因子产生dense近似

ROADMAP真实ID `MODEL-SELF-ATTENTION` Ch14（此前Source包简称MODEL-ATTENTION非StableID已在此纠正）。作者actual完整461–556 Flash exactIO→转换/编译/feature sparse/resolvent分支、相邻Ch13/15开篇，以及Ch24 86–110生成状态/历史/稀疏归属；现文已有edge support＋lowrank补偿，但未说明structured sparse factors产生dense approximation以及视频轴layout对近似条件的作用。唯一机制ownerCh14，不在Ch24复制kernelrecipe/实时宣传。拟在495标题下现介绍段之后、‘替换已训练算子’小节前加一连续段：

> 少算关系还可以不直接删除attention edges，而用稀疏的结构化因子近似一张仍然dense的attention map。视频中若位置交互近似沿时间、宽、高分离，block轴须消费真实视频布局，不能把flattened index邻接当时空邻接；不规则语义交互又可能破坏block低rank，因此可进一步细分block，再以适配训练减少在线因子refinement。这与FlashAttention的exact IO优化、以及直接top-k删边是三种不同选择。[受限视频对照](https://arxiv.org/html/2602.12271v1)只支持相应布局、训练与核配置：可分位置的exact表示不认证混合语义attention等价，表示族扩大也不证明有限训练/迭代下质量单调。训练、refinement、layout转换和跨frame中间量都计费；query分块能控峰值内存，却不会取消KV存储，局部kernel倍数也不是端到端或实时SLO，部分GPU/密度反而慢于dense核。布局/质量/摊销不成立时，保留更多refinement、经验证的其他近似或dense FlashAttention，不因因子稀疏宣称删除了所有关系或无损全局加速。<!-- source-family:SF-2026-ARXIV-2602-12271 -->

Source已独核，拟文待actual PRE/root锁。只采用该长期机制与失败边界，不授完整tilenum/theorem/实现或14B/720pRTX部署证书。

### 11409 TRACER actualowner PRE：唯一Ch66跨actor/跨step测量聚合

唯一`PLATFORM-EVALUATION-SYSTEM` Ch66。作者actual2630–2684完整judge sensitivity/invariance→uncertaintyensemble→StatefulEvaluation连续正文，以及Ch65/67开篇交接；现ensemble只说明多个scorer的代理/校准/abstain，没有多actor分量在step内MAX与跨step tail聚合的具体取舍。不授多Agent协议owner或全新风险概率。拟在现‘多个uncertainty scorer’段后、StatefulEvaluation标题前补一连续段：

> 多轮工具交互还须区分‘谁的哪一步出现异常’与‘整段风险怎样汇总’。可分别记录agent和user的filtered content surprisal、重复及action–observation/user–agent coherence，先在step内用MAX保留最突出的分量，再跨step汇聚高风险tail与最坏step，避免均值把稀疏关键异常稀释。过滤数字/停止词后的surprisal只测被选人口，不是无偏全词entropy；MAX也不能免去不同actor、尺度与模型的校准，score不等真实hazard概率或causal责任归属。[有限工具交互对照](https://arxiv.org/html/2602.11409v1)支持failure ranking，failed-only且按最终轨迹长度回看的提前阈值，不证明在线FPR、固定预警时间或实际挽救。部署须绑定actor/model、token过滤、embedding、聚合参数与held-out slice，并另计logprob/表示/缓存与排序费用；sensor只向abstain或复核提出信号，不能越过权限/预算hard gate。尺度漂移、校准或漏读关键内容时，回独立outcome核验、人工升级或原hard限制，不把低score当安全许可。<!-- source-family:SF-2026-ARXIV-2602-11409 -->

Source已独核，待逐字PRE及root锁。BLPO则据root实际Ch75 568–598/Ch66 2637–2678的contextoptimization/judgeconstruct原则，建议Only而不称其具体bilevel recipe已有；请root确认Only层，不造覆盖新配方的虚假声明。

root已实际确认BLPO11340 Only/Existing通过：保留贡献准入与Source，不宣称已有其具体bilevel recipe，无正文写/假POST。

### Agent 2602.11596 MAPLE：刚完成作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL `https://arxiv.org/html/2602.11596v1`；作者完整§3/4/5/Conclusion/Impact实际读，新增一项。拟采用 **2+2+2=6**：多模态policy训练必须区分任务最小所需信号(RMT)与实际暴露信号；modality-isolated构造/标注后按可用输入集合组织训练、分层评价，并分别记录模态缺失/冗余。采用有条件signal-support×training-cohort接口与验收，不把一般sample-level loss/asymmetricclip/zero-variancefilter换名为新GRPO，也不授最小RMT标签客观真值。

必要机制§3独立音/视频/字幕标注→Gemini2.5Flash对齐→controlledsubset生成，LLM检查/有限人工只验证所定样本；QA47893/546trainvideos与5001/68evalvideos分离，Caption5120无humantrain、eval5348/764videos均衡7tags。§4 RMT或compatibleunion组织mini-batch、输入限对应信号，主MUPO却总给VAS；**input identity和batching同时变**，不能从比较单独归因normalize。§4.1前面GRPO定义prompt内Grollouts归一，后面称MU跨异质reward共同归一身份不充分；§4.1 Var(MA)≤Var(MU)及§4.2‘难题必小advantage/gradient’未采用。Eq2/3又对已归一GRPO loss加1/|BM|，不同tag加权目标不等不偏原population估计；不采完整方差/稳定证明。KL-to-Beta(100,1)history只是任务表现proxy，binaryreward到continuousdensity的实际估计/smoothing主文未充分给出，不自补万能difficulty或zeroKL已解所有任务。

完整评价/直接反侧§5 T1–4：Qwen2.5Omni3B、AdamW2e−6/G8/global256mini32/4×H10080GB nodes按原文身份、mixedprecision+FP32head；ctx10240(8192+2048)vsrolloutcontext8096不能静默合一。T1 fullrecipe58.72<samplelevel58.86/staticcurric59.05，AS56.92<MU58.77/VAS57.71<58.14；earlyfilter58.00<58.58。164.72vs523.28s/step含删除zero-variance和输入减少，不授等有效token/全部epoch费或productionSLO。T2 adaptive QA59.82虽aggregate高，S61.35<MU63.82。T3 Caption完整74.00>MAPO73.88但V66.20<66.78/A81.42<83.46/S84.97<87.50；单项adaptiveweight72.89/static72.07/dynamic71.95均低于73.88，不照录逐样本/全tag dominance。Caption是LLMjudge不是事实真值，pass@1由5samples估计非pass@5。

T4 QA+把所有deficit样本标None，并将25%exact/superset原correct替换None；77%是该合成标签约定，不证明真实开放输入不足可可靠abstain/‘true modality awareness无rewardhack’。§5.4.2 CRW仅Caption:full/deficit response表示分离，18.19→18.46fusion和tSNE不授内部causal grounding，暂不采用其未必要细读的具体AppendixE3 recipe。标注、generator/judge、对齐、模态编码/rollout与过滤历史全计费；RMT错/shortcut、judge漂移或真实缺失分布失配时回完整信号原训练、独立缺失切片与Unknown，不认证productionready。拟owner实际MULTIMODAL-REPRESENTATIONCh23/训练Ch33需择一具体差额，Source未独核，附件仅遇拟采用必要缺口再定点，不全读。

### once 2602.11351 BAO：恢复已读窄机制的必要评价包

精确原件[once-core](./supplement-20261008-once-core.json) URL `https://arxiv.org/html/2602.11351v1`；原一次决定核心§4已root准入，本次实际恢复§3/4、完整§5/6/Impact的必要评价与直接反侧，原作者已读项不额外加数。拟采用 **2+2+2=6**：单纯罚用户调用可过早减少求证，行为SFT后用两类turn级罚项改变“连续提交需用户反馈”和“未成功但提前结束”的信用分配；前者Eq2只判连续Au、后者Eq3按剩余turn比例罚，不能把proxy读成真实information gain/overthinking检测。更多environment turns不等新信息，连续用户回应也可能必要，用户授权/真实硬预算仍独立。

§3 fixedhiddencontext/15turn预算与Au(Answer用户反馈)、Ae(Action/Search环境)身份，UR=E[U/trajectorylength]并非绝对用户工时/满意度；§4 GPT4o生成记忆/假设修订与计划SFT，之后GRPO turn scalar播给turn内tokens，reward-to-go/group总return归一。Eq5a G_t却sum从k记号不一致，不自补精确estimator或授新增GRPO。采用罚项的作用对象与误惩边界，不采“所有未用完turn因为thought过量/连续Au必无gain”的归因。

完整§5 T1/明确负侧：4B FunctionPassU1 .2692<无BR.3333、Score.6923<无BR.7179；TelepathyUR.1870>无BE.1452；TurtleScore.1125<无BE.1146。1.7B FunctionScore.3590<无BR.3974、TurtlePassU1 .0563<无BE.0615/无BR.0594。不能以localPareto图宣布全部任务/指标前沿最优。§5.2同SFT/RL样本/epoch不等等teacher/rollout/token/FLOPs，商业模型只身份特定比较，不授全面胜其能力。Function规则反馈仅该simbenchmark、不等普遍真实gap零；Telepathy训练Qwen3-8B用户/评GPT4o，Turtle训练用户+reward同Qwen→评GPT4o，judge/proxy变更是必要评价身份。§5.5长回答rewardhack缓解仅这两judge切换、RTR及轨迹对照，不认证真实用户感受/攻击免疫；SelfBLEU/NVEmbed低相似是表面多样性非informationgain。Function Fig5三seed±std人口保留。

GT4o teacher/SFT、用户模拟/rewardmodel、policyrollout/迭代/监督记录均须计费，主必要段未给完整hardware/batch/服务SLO不补造；精确费用如欲采用需先定点附录，不为该有限接口扩全附件。语言only与固定c不授multi-modal或意图中途变化；惩罚误伤必要求证/提前合法停止或净成本退步时回原终局reward、调低/关闭行为罚项与独立用户预算。拟唯一TRAIN-GRPOCh33须actualowner差额，不写Agent记忆/计划通则。准入已有root裁决，必要Source待非作者独核。

### 原已读七项的单篇独核最小路由（不凭标题自拟）

root已授权独立reviewer逐项按作者窄命题读，不需等待作者长包齐；这些全部已有作者必要读，以下不新增作者分母、Source/PRE尚未自授。BAO采用命题/作者评分及反侧已在上一节持久。余六拟评分均2+2+2=6，具体实际证据若不支持则窄修/隔离，不为给分扩全部附件。

- **LUVE11564**：[once-core](./supplement-20261008-once-core.json) exact https://arxiv.org/html/2602.11564v1，采用§3.3 latent/pixel/frame目标分工与§3.4频带/算子/噪声阶段；视觉编码后的latent目标并不完整约束像素/时间动态，频带/算子与噪声支集各有职责，不统称通用curriculum或只增加video data。必要Source已独核：只免中间codec往返，最终decode/pixel监督训练仍费；T1 TF/SC及4K<2K avg、T5 upsampler .922s>latent .004s、T6普通LoRA FID47.03>无expert46.48，HPS/UM data混杂/全hwE2E缺项保留，不授frequency因果/视觉真实性。
- **HAIC11758**：[once-core](./supplement-20261008-once-core.json) exact https://arxiv.org/html/2602.11758v1，作者已实际定点复读III-B修正：proprio history＋未来reference motion→对象相对pose/velocity/acceleration估计→predicted R,p变换canonical pointcloud→privilegeadapter→student控制。采用对象状态/动态几何估计与控制输入交接，不是一般动态障碍/规划约束恢复；Eq2仅R,p作用点云，v/a另传不授高阶几何投影或真occupancy。外部PC/Ethernet与后文onboard身份冲突隔离；real skate60%/cart+box40%、Slope/body误差退步及完整试次数/CI缺项保留，不授安全许可。修后待reviewer确认必要Source。
- **GigaBrain12099**：[once-core](./supplement-20261008-once-core.json) exact https://arxiv.org/html/2602.12099v1，必要Source已独核：采用3.2 WM预测z/value的maskedconditioning及更新/部署分支，GT future只是WM监督不是policy输入GT future；Stage2mask z/Stage4mask I+z/deploy I固定1，非真实advantage或成功证书。主文无独立p.2消融与两部署mode配对质量，不签无损绕WM；T1 .25s>.11s valueonly、leaderboard0.1与结论0.5身份冲突、人类纠正数据与完整WM全費保留，不授全humanoid/无标签。
- **UniDFlow12221**：[once-core](./supplement-20261008-once-core.json) exact https://arxiv.org/html/2602.12221v1，非作者必要Source发现中心冲突：Eq7/8写不同x_ref^w/x_ref^l，但§4明确3.5M identicalinputs/reference，Impact写sharedconditioning。撤回“实际不同reference preference”采用，不以变量名授新训练目标；两原位置只Report冲突。局部仅保留step-wise Δθ=αtΔu+(1−αt)Δg router/consumer identity，先actualowner判断Only，不救完整DPO。TSGRMSNorm Eq2重复γ→zeroinit非原norm、bias/逐维scale非方向保持、Eq9edit target记txt及DPG91.19/91.91冲突隔离。已有taskLoRA或路由名称本身不构成新长期gap；独核此有限局部/争议Report有效，非中心通过。
- **JEPA11832**：[core-2](./supplement-20261008-core-2.json) exact https://arxiv.org/html/2602.11832v1，采用§3 frozen video predictive representation→VLA actionconsumer，earlyconcat与gatedcross-attention在robot-pretrained身份下可不同，稀疏层插入/不同LR是适配预算；不授representation已知物理/动作因果、不把Flamingo gate作为首次机制。必要§2/4比较raw/robot-pretrained consumer、直接反侧/总latency，root题摘准入有效，owner需actual比较是否已有。
- **SCoT11980**：[core-2](./supplement-20261008-core-2.json) exact https://arxiv.org/html/2602.11980v1，采用§3 phrase绑定离散box的interleaved text-coordinate接口→独立planner/renderer，不jointpretraining；两阶段grounding/aesthetic训练仍计费。MLLM内部check不是独立constraint verifier，不授空间因果/strict几何可满足/零架构成本。必要§4直接对照/反侧限定，不因SCoT名称或三阶段本身扩写。

### Agent 2602.11619 When Agents Disagree：刚完成作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL https://arxiv.org/html/2602.11619v1；actual完整§3/4/5/6/Impact读完，新增作者一项。拟采用 **2+1+2=5**：Agent一致性必须分别量answer、actionsequence与pathlength；相同任务的重复执行能定位早期query分歧，但低diversity不能作为正确概率。采用局部失败测量/反例，不授novelReAct机制或已实现runtimeearlystop控制。

§3 HotpotQA distractor10paragraphs(2gold8distractors)/100hard questions79bridge21comparison，lexicalSearch/Retrieve/Finish；三模型各10runs/temp.7=3000。模型API具体版本/provider保留，不授一般scale/能力→稳定因果。Correctness是caseinsensitive gold/answer互为substring，不是严格semantic/verifier truth；长混合错误回答也可能满足该proxy。Actionsequence主文示例仅tooltype串，args等价是否归一不明，不自补完整replay identity；各query/runtime环境观测仍需固定。

完整§4 T1–5负側：consistent≤2与inconsistent≥6只是分组相关，3–5中间人口不代表极端split结果；Claude/GPT/Llama两组计79/9、70/10、25/29不授全人口错误概率。Llama69% step2仅59/86**发生divergence任务**，非100任务69%、非所有model因果；step数r−.34可能有taskdifficulty混杂，不授裁掉step必更好。T5 comparison correctness80%高于bridge75.7但answerconsistency62.4%低于76.6，构成稳定≠可靠的直接反侧。§4.5 temp0仅20题，temp.7行77.4/4.2与主100题数字同，matched20题对照未独给，不能把+5.4pp当受控温度因果或prod推荐；temp0仍2.2seq非determinism保证。

§5将多次并行agreement/earlyquery干预作为建议而未实际deployment验证；评测100hard、词法检索与fuzzylabel不外推web/coding/alltools。10runs每题与API/search/retrieve总费、重试/选择费用须计，不由观察路径短推出SLO/单位成本；hardware/batch/线上FPR/heldoutcalibration未核不补。难度/输出等价失配或未裁定事实，回独立outcome证据、Unknown/人工复核与原执行权限，不能用共识发布真值。潜在唯一Ch66 actual评价owner须比较具体已有覆盖，初准入root有效，Source待非作者。

### Agent 2602.11636 ScalSelect：作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL https://arxiv.org/html/2602.11636v1；actual完整§3/4/5/6、Eq1–9/T1–7已读。拟采用 **2+2+2=6**：仅按图像相似度选训练数据忽略同图不同指令；目标VLM第一层user→visual attention决定所取视觉token，再对均值表示作column-center/SVD，按dominant subspace的row leverage确定子集。采用instruction-conditioned选择人口与global variance-support分责，不把attention当grounding真值、spectral energy当下游能力或标注正确性。

§3.1累加全部user指令token对visualtoken的head均值attention，90%mass阈值选视觉集合，再平均第一层hidden；conversation含assistant回答，但评分人口是user tokens。Eq2未写causal mask，本包只采用query→visual权重改变token选择，不认证前置视觉hidden自身已读取后面的指令。§3.2 X列中心化、最小k覆盖90%总σ²能量、π_i=∑U_kij²、deterministic top-score；CUR启发不等已证明该确定性top-row子集有随机CUR全重建保证，低方差稀有能力可能漏掉是系统推断非论文已测。§4 O(Ndk)在fixed d及小k前提成立；k=9仅该表示/数据配置，T7中层59/深层260，不能宣称任意分布固定rank。视觉编码、各样本第一层forward/attention提取、Nx d表示/中心化/SVD、token排序及全局top选择成本仍在；主文未测完整selection walltime/memory/总训练净费，training-free不等免费或全链严格线性。

完整§5：LLaVA-V625K去40K textonly、LRV180K；主100K(16%)，LLaVA-Vicuna7B preinstruction checkpoint及Qwen3VL4/8B，8×H10080GB/1epoch。相同epoch不是相同有效token/总forward预算；Rel是各benchmark按表reference归一后平均，不是97.85%统一准确率。T1 MME-P1400.34<Random1418.85、POPE-A83.96<84.96/POPE-P94.73<Length96.71；MMBench与SQA低于COINCIDE，不采全指标dominance。T2预算50→400K认知314.29→299.29且非单调，400K MME-P1425.41<300K1517.26、OCR19.8<full20.3。T3 Qwen8B POPE-P94.39<full96.39、MMBenchEn82.46<84.30，不能以Rel102.39授全能力保留。T4 LRV MME-P840.59<Random848.76。T6 NoInsCon MMBench61.72/55.44高于fullselector59.19/52.80、SQA无center66.29>65.29；T7深层OCR19.60>第一层19.40，支持有限aggregate而非通用第一层最优/attention因果。

不扩所有阈值/训练超参附录，因为此有限支持与直接反侧已足，不采用未核batch/precision/CI/selection speed或productionSLO。目标checkpoint/模板/causal语义或输入分布变化须重新提表示/谱；信号失配/稀有切片漏选/净成本不合适时，保留随机/分层子集或完整训练、独立label与能力slice验收。唯一TRAIN-DATA Ch27须actual比较具体已有selection原则，Source待非作者，不自授Books。

### 11513 DEL actualowner PRE：Ch72随机低比特latent与server适配

唯一`PLATFORM-SECURITY` Ch72。作者actual140–178 PrivateInference完整前后（hardware attestation→HE/MPC→数据/模型混淆→streaming），432–480 DP unit/accountant/经验攻击与composition；Ch71/73交接只核租户与发布治理。已有协议/混淆分支及DP会计并不具体承载“有界低维latent随机量化，同时用server softprompt适配噪声”的消费路径。拟在PrivateInference HE/MPC联合验收两段后、数据/模型混淆分支前补以下一段，数学会计只handoff现DP段不复写：

> 不依赖HE/MPC的另一受限路径，先在client把输入embedding编码到有界低维latent，再以binomial随机机制联合完成扰动与n-bit量化，server解码并用适配过该噪声的soft prompt调用冻结模型。压缩维度、每坐标bit数与扰动强度因而共同决定传输和效用，不是先加噪再把通信免费删掉。[必要原证](https://arxiv.org/html/2602.11513v1)的Gaussian-DP近似仍依坐标有界、维度与随机机制前提，并保留±γ误差；L2有界也不会自动成立更小的逐坐标界，不能直接外推整条对话或重复query的composition保证。相同embedding-inversion ASR只表示该攻击人口下的经验恢复率相近，不表示同DP或覆盖其他攻击，严格隐私与跨域迁移也可能损害效用。Encoder/decoder训练、随机化、server softprompt及额外token都计费，低bit payload不等低端到端时延。输入边界、会计或噪声适配不成立时，应回目标威胁下已核验的密码协议、可信执行、本地处理或拒绝敏感请求，不把压缩表示当匿名证明。<!-- source-family:SF-2026-ARXIV-2602-11513 -->

必要Source独核通过，等待root逐字PRE/窄锁；不授exact μ-GDP、全部序列会计、全攻击或可执行完整recipe。

### 11524 ADMIRE actualowner PRE：Ch33 proxy milestone与终局人口

唯一`TRAIN-GRPO` Ch33。作者actual765–824完整树信用→phase→harness milestone→segment/counterfactual→state接口；现789 milestone由environment/harness验证、双尺度credit和后文gaming边界有效，本项不能覆盖成语言proxy。新增差额是成功轨迹动态生成/修订proxy和按终局人口给不同辅助信号，不是新GRPO或GUI执行判据。拟在现milestone说明段后、语义segment小节前一段：

> 若environment不能提供可验证milestone，还可以从成功轨迹生成有序动作描述，并用后续成功路径修订它们，以语义相似度只匹配当前pointer所指目标。这比harness milestone更弱：命中描述不证明真实GUI状态、有效subgoal或因果进度。辅助信用可按终局人口分开，成功轨迹只计命中项，失败轨迹另保留已命中比例的进度底值和命中增量，避免把同一种过程代理无差别加到所有路径；终局verifier仍独立。[有限对照](https://arxiv.org/html/2602.11524v1)中动态目标与退火并非每次都优于静态或不退火，动作匹配误差、缺少成功路径的启动困难，以及目标生成/修订、judge和rollout费用都须验收。正文的计数与算法逐步计数、末项重复命中和空目标guard还未形成一致可执行合同，因此这里只采用受限信用分工，不照抄完整算法。Proxy错配、更新漂移或净费用不合适时，保留静态经验证目标、原终局reward或harness分支，不能由更密辅助信号自签更可靠控制。<!-- source-family:SF-2026-ARXIV-2602-11524 -->

必要Source独核通过，等待逐字PRE/窄锁；不改变现harness milestone权威与双尺度credit分支。

### 11596 MAPLE actualowner PRE：Ch23信号支持集与训练人口

唯一`MULTIMODAL-REPRESENTATION` Ch23。作者actual600–660完整observation→task-contribution/reliability→训练prior→伪标签→alignment/caption；现622–650有task contribution与当前可靠性分责及频谱prior权重，但未显式定义任务最小需要信号、实际输入与batch/cohort的三份身份。本项不在Ch33重复GRPO归一通则。拟在task-contribution/reliability两段与示意图之后、频谱训练prior段之前补一段：

> 训练人口还须区分‘任务至少需要哪些信号’、‘本次实际给了哪些输入’与‘哪些样本被放进同一cohort’。可以用独立模态标注提出required-modality集合，再按该支持集或兼容集合组织训练、限制所暴露输入，并分别评价缺失、恰好满足与冗余信号；这改变表示的训练条件，不是在线reliability sensor，也不证明标注得到客观最小充分集。[有限多模态对照](https://arxiv.org/html/2602.11596v1)同时改变input与batch构成，不能把全部差额归给组内归一或宣称普遍降低方差；完整配方及部分单模态切片仍有反退。训练标签规则下把缺失样本标None，也不认证开放输入不足时可靠拒答，表示分离不等内部因果grounding。模态隔离生成、标注/对齐、编码、rollout和过滤历史均计费；支持集误标、shortcut或真实缺失分布失配时，回完整信号训练、静态cohort和独立缺失切片验收，事实与Unknown继续由外部证据承担。<!-- source-family:SF-2026-ARXIV-2602-11596 -->

必要Source独核通过，等待逐字PRE/窄锁；不采用CRW未核完整recipe、方差定理或合成None标签的开放abstain证书。

### 12262 T3D actualowner PRE：Ch24 teacher状态与teacher内容同时有身份

唯一`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。作者actual420–450完整masked-generation→teacherorder goldlabel→PUMA→whereplanner，以及1528–1555概率/credit接口和Ch23/29相邻交接。现2601.07568分支已由teacher order构造可见状态、内容仍gold；不能称首次有teacher顺序。真实小差额是用同一次teacher生成的中间状态和最终内容作为joint标签，并按早揭示位置强调path CE；“训练teacher条件”与“更新student真实访问状态”分开。拟在原teacher-order/gold段后、在线mask-law段前加以下一段：

> 顺序来自teacher、内容仍由gold监督，与把同一次teacher生成的中间mask状态和最终文本一起用作训练标签，是两种不同身份。后一分支保留状态与终点的配对，再以teacher/reference的conditional likelihood提出偏好，并按较早揭示的位置加重path CE；teacher内容可以错误，早揭示权重也不是因果credit。[必要对照](https://arxiv.org/html/2602.12262v1)只支持teacher条件轨迹训练，teacher与更新后的student共享中间marginal仍是假设，不能由初始化相同推出部署占用分布已覆盖或真实joint KL已最优。Teacher生成、reference刷新/采样、likelihood和全参数训练都计费；少步质量、原full-step能力、输出长度及实际step/墙钟须分验，恢复完整decoding仍可能退步。轨迹支持或费用不成立时，保留原gold内容监督、clean蒸馏与完整保守decoding，不因模仿顺序便授予正确提交。<!-- source-family:SF-2026-ARXIV-2602-12262 -->

必要Source独核通过，等待root逐字PRE/窄锁；不改变现teacher-order/gold与PUMA forward-masklaw条件，不采DDO全等价。

### 12155 FAIL actualowner PRE：Ch24反馈可微性决定更新路径

唯一`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24。作者actual1528–1578完整rate-policy→reverseconditional→trajectorycredit→relay→SDE→metricreward，1555长轨迹反传已有成本，但并不承载expert/current-policy在线discriminator两种flow更新接口。后文1578–1634生成内反馈与独立truth已有，不能把推理期诊断消费当训练PG/PD。拟在生成后训练开头说明后、Reward更新policy小节前一段：

> Expert图像监督还可以随当前policy样本更新一个discriminator，而不是固定SFT目标或把其分数当独立真值。若反馈可微，一条受限路径以local-linear single-step denoising近似连接终点评分与vector field；若只消费scalar反馈，则以CFM loss差构造ratio surrogate进行更新。这两种接口决定训练梯度路径与费用，不是同一个flow likelihood，也不把实际近似变成exact或无偏policy gradient。[必要实验](https://arxiv.org/html/2602.12155v1)中scalar路径在较长训练后可collapse，可微路径也并非相同预算下每项更好；expert/current-policy配比、BC启动、CFG评价配置与discriminator版本须分开验收。Expert生成/过滤、在线rollout、discriminator训练和反传均付费，代理reward上涨不认证真实偏好或消除hacking。近似、专家支持或质量/预算不成立时，保留原SFT、固定guidance或受控外部reward，PPO/GRPO更新规则仍交Training owner，不照搬完整flow surrogate等价。<!-- source-family:SF-2026-ARXIV-2602-12155 -->

必要Source独核通过，等待root逐字PRE/窄锁；不为GAIL/GRPO命名另写Ch33，不授全部时域Eq2/真实density ratio/exactKL。

### Ambi / FlowMind逐字PRE与Coop / VAT具体Only提议

必要Source57/57非作者层有效复用，不重新读附件。作者本轮实际Ch66 499–528配对context/目标与非目标属性、658–694均值/原始人口/相关性、874–898逐verifier与聚合、924–966轨迹/终局合同，以及Ch65/67开篇；Ch81 171–210 canonical DAG/template/trace、288–310 search/evaluator、635–657 trial→revision分权、908–930 passing trace归纳与Ch80/82开篇；Ch82 60–88 coordination tax、820–888过程/预算边界、1018–1042双时钟与authoritative world state，Ch81/83交接均actual读。以下仅PRE提议、未写、未授owner锁。

- **11750 AmbiBench，唯一PLATFORM-EVALUATION-SYSTEM Ch66**。874–898已有逐项验证和聚合，但不具体承载同一requirement的缺path/parameter/anchor三种信息操作及“逐项任一时点出现”不等“最终联合状态保持”。拟在逐verifier结果聚合说明两段之后、typed生成条件分权之前一段。

> 同一需求还可以通过有界的信息删减构造不同任务人口：保留意图，分别移除操作路径、参数或参照对象，再把需求效果、参考过程与澄清恢复分开测量。这样才能区分不会执行、缺规划线索与缺用户信息；强制缺失参数取非默认值是一种压力构造，不是自然用户分布。逐项需求在任一历史时点都曾找到满足证据，也不保证最终同一个环境状态同时保留所有要求，撤回和相互覆盖必须另验。[AmbiBench的有限对照](https://arxiv.org/html/2602.11750v1)中礼貌对话与缺项恢复可分离，成功子集上的关交互实验不授普遍因果；截图经语义序列化再判分及小样本人审也不成为真实状态/满意度证书。信息删减、初始化、用户模拟、序列化和多轴judge均计费，原需求、缺项种类、证据时点、参考顺序与simulator版本须保留。构念或代理失配时，回原始截图/工具状态、确定性终态verifier和真实澄清/人工确认，不用聚合TSR替代最终效果验收。<!-- source-family:SF-2026-ARXIV-2602-11750 -->

- **11782 FlowMind，唯一AGENT-WORKFLOW Ch81**。现canonical graph、trace/definition和trial→revision权限具体分开，但未承载业务执行结束后撤去业务工具、摘要阶段只开放构图工具的阶段权限切换。拟在177–194 template/realized graph/trace分权两段后、portable pattern前单段，Ch75摘要只handoff不重复。

> 从实际业务轨迹提炼复用图时，还可以先切换工具可见性：业务执行阶段保留真实工具，摘要阶段撤去业务工具，只允许提交构图操作，把继续执行任务与描述可复用流程分成两种权限。摘要得到的是derived graph proposal，原任务成功、图结构有效与图在新测试中的完成率仍是三份证据，不能从一条passing trace直接发布workflow。[FlowMind的受限对照](https://arxiv.org/html/2602.11782v1)有测试率和联合成功率退步，提示/阶段与工具可见性共同变化也未唯一证明减轻认知负担。轨迹生成/筛选、摘要、构图、黑盒测试及开发调参均付费，部分输出token增加、累加调用时长不是墙钟；业务state、图版本、operator与独立测试身份需冻结。压缩遗漏、图质量或预算回归时，保留原trace、显式code-defined template和独立graph测试，实际effect提交继续由runtime当前权限与状态验收；这份发布纪律是工程边界，不宣称论文已实现全部promotion gate。<!-- source-family:SF-2026-ARXIV-2602-11782 -->

- **11754 Cooperation，拟仅报告＋具体Existing，AGENT-MULTI-AGENT Ch82**。60–88已经承载communication强度不是收益、读出/群体切片与coordination tax；1034–1042已具体区分认知/环境时钟、等待不等环境进展、消息不是authoritative world state以及同步/异步成本。新增固定人格、双边同delay的非单调合作曲线是有限局部反证，不增加新通用控制机制；保留20s恢复仍低于0s、仅最后20s和toy非法概率隔离于报告，不能说书稿已有此配方或任何delay结论。无diff/假POST，待非作者actual Only。

- **12134 VAT，拟仅报告＋具体Existing，PLATFORM-EVALUATION-SYSTEM Ch66**。517已明确目标属性改良须与untargeted attributes/context交叉、整体改善与其他条件退步共存；658–694保存per-example/slices、clustered相关性与探索选择偏差，499–528配对cue/构念边界限定normative解释。因此有限paired ordinal multidim shift与跨sample co-variation作为本地测量留报告，nVAT定义/表数冲突不采用，不从相关性得价值因果/现实伤害；不能说现书含56维VAT或其recipe，不重复写通用tradeoff。无diff/假POST，待非作者actual Only。

### HAIC / GigaBrain / DreamID：actualowner最小逐字PRE组

必要Source复用非作者已核层。作者actualCh26 93–112 privileged3D/运行时schema、346–380三种WAM接口与381–435因果使用/训练辅助，Ch23 276–306 acousticclock/timbre分责及735–747 subject/coordinate，Ch24 1050–1099双条件/生成状态，Ch25/27开篇交接。以下未写拟文，root协调PRE/锁后才实施；现有分支均保留。

- **11758 HAIC，唯一MULTIMODAL-EMBODIED-VLA Ch26**。原privileged teacher只训练表示不留现场3D；本项实际部署预测对象状态并构造控制输入，不是一般障碍恢复。拟93–110已有privileged teacher完整块之后、闭环主干前单段。

> 还可以保留显式几何的输入schema，却用状态估计器替代无法持续获取的对象观测：由proprioceptive历史与未来reference motion预测对象相对pose、velocity和acceleration，再用预测R、p变换canonical点云，经adapter交给student controller；v、a另作条件，不是全部高阶量都直接投影进点云。这里reference motion是任务条件，估计点云是可错的控制输入，不是真实occupancy、障碍许可或物理状态恢复证明。[HAIC的有限对照](https://arxiv.org/html/2602.11758v1)有Slope/body误差退步，实机滑行60%、拉车加箱40%且完整试次数/CI不足，不能从几何接口授精准控制。状态估计、点云变换、adapter与控制训练均付费，外部PC/Ethernet与onboard描述尚未闭合，不能签实时全机SLO。对象、reference或坐标失配时回真实可用传感器/显式估计校验、较短任务与已验低层controller；控制提交仍由独立safety envelope决定。<!-- source-family:SF-2026-ARXIV-2602-11758 -->

- **12099 GigaBrain，唯一MULTIMODAL-EMBODIED-VLA Ch26**。现346–360区分显式future/joint/directlatent，但未明确可选择WM预测latent或只value的缺条件训练支持与deployment positive标签；拟该段三接口说明后、appearance/depth/flow两branch前一段，不在Ch25重复predictive truth通则。

> Policy也可在训练中随机缺省预测条件，分别支持读取world model提出的未来latent与只读取value的部署分支；缺省latent与缺省改进标签是不同训练mask，不能把两者混成同一个“未来可省略”证明。真实future只监督world model，部署policy读取的是预测而非GT；部署把改进条件固定为正，仅指定想要的行为，不等当前advantage已知或成功证书。[GigaBrain的有限方法](https://arxiv.org/html/2602.12099v1)没有配对证明两个部署分支质量无损，latent分支.25秒高于value-only .11秒也只是局部计时，不能宣布免费绕过world model。训练mask/阶段、predictor/value/policy版本与实际可见条件须绑定，人类纠正数据、world model训练/预测及action生成均计费。预测失准、标签漂移或预算/质量退步时，保留经验证的value-only/direct policy或完整预测分支，并以真实闭环结果验收，不由固定正标签授行动权限。<!-- source-family:SF-2026-ARXIV-2602-12099 -->

- **12160 DreamID，唯一MULTIMODAL-REPRESENTATION Ch23**。原276–306音色/时间分权和735–747pose/subject配对不涵盖多个主体的跨voice/visual reference联合消费槽。拟参考音色完整两段与family marker后、语言响应声学表达之前一段，Ch24 sampler不重复。

> 多主体reference还要同时回答“这张脸、这个音色和这句台词属于谁”。一个受限接口让同一主体的视觉/音频reference共享预留位置segment，并在video、audio和joint caption里持续使用具名anchor；reference以concat保留可选来源，结构条件另用加法注入，而不是将所有条件混成一个全局caption。位置分段是匹配proposal，不由RoPE周期性保证正交、零串扰或真实身份授权；loss排除reference区也不证明输入无法copy。[DreamID的有限200例proxy评价](https://arxiv.org/html/2602.12160v1)里reference-only身份相似更高却有copy倾向，完整分支也非所有同步/质量指标更好。配对来源、主体anchor、segment尺度、两stream及CFG版本需共同保存，数据匹配/训练、reference编码与多条件forward均计费。配对不明、主体串扰或质量回归时，保留显式单主体/声纹配对、独立同步与输出核验，而不把一致生成当身份真值。<!-- source-family:SF-2026-ARXIV-2602-12160 -->

### BAO / CM2：actual TRAIN-GRPO 逐字PRE；12078/UniDFlow有限Only提议

必要Source有效复用。作者actualCh33 263–271 turn target-likelihood/shaping与718–817 verifier/noise→phase→milestone→slot/segment完整局部，Ch32/34开篇职责。两新段都由唯一TRAIN-GRPO承载目标/信用语义，不复制Agent控制权；尚未写入或自授PRE。

- **11351 BAO**：现turn likelihood变化/成本惩罚分责不承载连续用户询问与未成功提前结束两种人口代理；拟263–271既有target-likelihood段后、局部分叉探索段之前一段。

> 互动成本还可以用行为形状作辅助罚项，而不直接罚每次向用户求证：连续提交需用户反馈的回合与尚未成功就提前终止，分别触发不同惩罚，后者可按剩余回合预算缩放。这会改变求证、环境探索与停止的训练信用，不是从回合类型检测真实information gain或过度思考；连续求证可能必要，剩余预算也不证明继续一定有用。[有限对照](https://arxiv.org/html/2602.11351v1)中完整组合的部分成功率低于去罚项分支，用户调用占轨迹比例也不等工时或满意度。模拟用户/reward身份、行为SFT、rollout与评价费用须分账，不能以相同epoch授等总成本。罚项误伤必要反馈、合法停止或最终质量时，降低/关闭辅助项，保留原outcome reward、明确用户预算与真实执行门禁，不把代理优化当用户意图已完成。<!-- source-family:SF-2026-ARXIV-2602-11351 -->

- **12268 CM2**：原milestone/数值slot聚合说明局部信号与信用分账，但未明确noisy checklist的criteria粒度可细而assignment反而粗及直接collapse条件。拟ADMIRE proxy milestone段后、语义Segment小节前一段，保留harness和ADMIRE现有权威分支。

> 细评价标准与细时间信用还是两条独立轴。没有可靠执行verifier时，可以从参考轨迹提出带evidence、dependency和strictness的binary checklist，分别尝试将其结果聚合到整条轨迹、回合或step；选用较粗assignment不要求把评价criteria也合成一个模糊分数。Checklist仍是learned judge代理，prefix满足不认证真实工具状态，回填以后满足也不识别唯一critical action。[CM2的有限训练曲线](https://arxiv.org/html/2602.12268v1)里细assignment早期快而后更早collapse，支持联验信号密度、相关噪声和信用频率，不证明所有环境应一律稀疏。实际std denominator设1，不能把结果全归普通方差归一化；重复判定flip与空eligible等guard尚未闭合，不能直接发布完整bounded reward算法。标注、每step judge、工具模拟、rollout和训练都付费，模拟器/judge共享身份及context/turn上限须固定；代理漂移、信用失稳或真实任务退步时，保留trajectory outcome、可信harness milestone和独立工具结果验收，不以binary格式自签正确性。<!-- source-family:SF-2026-ARXIV-2602-12268 -->

- **12078混合递归，拟Only/Existing原则。** 作者actualCh17 75–118 Post/PreNorm明确放置改变尺度与Jacobian/训练动态、不可从单次归一化推收敛；545–647双时钟/二维依赖、固定点和迭代预算/质量边界具体承载recurrence的执行/状态验收。双状态TRM里Mamba2→Mamba2→attention→MLP是本地grid配方，postnorm所有配置共同且无placement消融；本日保留Maze波动/Sudoku负侧、augmentation-vote覆盖与费用人口，不宣称书稿已有该recipe，也不造“归一化会稳定所有递归”新段。唯一MODEL-TRANSFORMER-LAYER待非作者Only PRE。

- **12221 UniDFlow，拟争议中心/局部Only，不写Books。** 作者actualCh23 772–785路由只决定条件计算/不能命名固定模态专家，Ch24 1331–1340 model/codec/mask/condition/sampler/adapter共同identity已具体承载局部step adapter消费分责。中心different-reference preference实际训练身份不通过；局部Δθ时变混合未出现需新长期链的独立验证，不把名称当gap。报告保留router观察及条件冲突双方，不冒称书已有整套DFM/DPO公式。非作者Only PRE待核。

### LUVE / ScalSelect / SCoT：actualowner逐字PRE小组

三项必要Source及反側复用review_20260214有效独核，不重开Source。作者本轮actual读Ch24 933–945跨尺度draft/preview及1157–1178 decoder、Ch23 725–771空间/time/provenance与Ch22/25开篇交接、Ch27 220–275 mixture/quality filtering及856–884 attribution、Ch28开篇。下面为未写拟文，待非作者PRE及root逐owner锁；不以已准备段数算Books。

- **11564 LUVE，唯一MULTIMODAL-GENERATIVE-PARADIGMS Ch24。** 现933–945低分辨率proposal由semantic lock或重新HR采样消费，1157–1178拥有最终decoder/temporal接口；尚未承载LR→HR learned latent映射的latent/pixel/frame三目标与band/operator/noise三职责。拟在跨尺度preview两段后、Draft+exact verification前单段，Ch23只保留codec交接，不重复写三目标。

> 跨尺度状态也可以由受训的latent映射接入高分辨率生成，而不先解码成像素、插值后再编码。此时latent重建、解码后的像素误差与相邻帧差分是三个不同目标：latent接近不保证没有block artifact，逐帧像素好也不保证时间一致。高分辨率refinement还可分别限定低通分支进入attention的高噪声阶段、高通分支进入FFN的低噪声阶段；频带、算子位置与训练噪声支集需一起绑定，不能将它们统称一个通用课程或认证频率因果。[受限对照](https://arxiv.org/html/2602.11564v1)中更高分辨率的平均质量仍退步，普通LoRA也有较差FID；数据筛选/锐化与接口共同变化，不保证所有质量提高。中间codec往返被省去，最终decode、像素监督训练、latent映射及expert计算仍付费，不能用单模块速度授整条4K实时。跨尺度失真、时序回归或总费不合算时，保留RGB级联、普通latent插值与原HR采样，并验最终输出而非只验latent。<!-- source-family:SF-2026-ARXIV-2602-11564 -->

- **11636 ScalSelect，唯一TRAIN-DATA Ch27。** 220–275已有visual-budget lineage/quality多样性joint选择；856–884保存梯度/curvature与代理SVD的是归因坐标，不是以instruction→visual权重形成样本activation、再取全数据谱row leverage的训练成员选择。拟在Quality filtering的retention/distribution段后、目标回答likelihood前一段，保持source/label质量权威不变。

> 同图不同指令还可以产生不同的选样表示：先用当前VLM的user-query到visual-token权重提出所取视觉集合，平均这些位置的hidden，再对整个人口的表示中心化并提取主子空间，用row leverage提出保留成员。Query改变的是支持集合的选择，不意味着前置视觉hidden已经读取未来指令；全局谱支持也不是样本真值、grounding或下游能力证书。[有限对照](https://arxiv.org/html/2602.11636v1)中不加指令条件的分支仍在部分任务更好，扩大子集或使用第一层也不是各slice单调最优。应共同保存checkpoint、模板、token选择、中心化、rank与实际训练成员，特别检查低方差稀有能力；此处漏选尾部是工程风险，不是论文已验证结果。编码/attention提取、全数据表示驻留、SVD与后续训练都付费，固定维度小rank的复杂度不等已测净省时。信号失配、覆盖或总预算回归时，保留随机/分层子集、完整训练与独立质量切片，不用谱能量替能力验收。<!-- source-family:SF-2026-ARXIV-2602-11636 -->

- **11980 SCoT，唯一MULTIMODAL-REPRESENTATION Ch23。** 725–771已承载坐标/provenance、估计地图与确定算术、时间输出接口；未承载生成规划中phrase后即时离散box的interleaved输出以及独立renderer消费，而非长纯文本空间推理。拟在空间地图推理的两段后、位置如何进入attention之前一段；generation/control只交接Ch24，不重复其sampler。

> 空间规划的中间输出还可以把每个对象phrase与紧随其后的离散box交错生成，再交给独立renderer消费，而不是先写一段纯文本推理、最后才汇总布局。这个接口让对象语义与拟定区域保持显式配对；box仍是规划条件，不是观测真值、严格几何可满足证明或对象因果定位。Planner的内部self-check不成为独立verifier，renderer/model/坐标网格和grounding训练目标须分别绑定。[SCoT的受限对照](https://arxiv.org/html/2602.11980v1)里较小planner有质量退步，内部约束比率也不等strict success；两阶段grounding/aesthetic训练、额外规划tokens与render均计费，不因未改架构宣称零成本。配对、坐标或画面质量失配时，保留纯文本计划、显式layout与独立约束检查，必要时重新规划，不让流畅空间叙述替最终图像验收。<!-- source-family:SF-2026-ARXIV-2602-11980 -->

### Agent 2602.12268 CM2：作者必要Source-ready

精确[缓存主文](./supplement-20261008-agent-core-1.json)及[exact-v1](https://arxiv.org/html/2602.12268v1)，actual完整§3–7/Tab1–4，必要Appendix.3官方HTML345–347。**2+2+2=6**：细criteria不要求把credit逐step密集分配；同checklist的trajectory/turn/step三路径中，较细assignment早期快但更早collapse，支持把评价粒度与信用时间粒度分开。Checklist后验从已有trajectory抽取binary evidence/focus/pass/dependency/strictness/weight；judge读取当前prefix，不等真实工具state或权限证明。采用两轴分离及受限负侧，不把新GRPO名/全部模拟环境认证为贡献。

§3 Eq2要求依赖在pre-step已满足才给unsatisfied→satisfied事件信用；Eq3把以后满足回填到依赖已满足的早步，只有step路径用。回填不是唯一因果critical step。Eq4声明每item只flip一次，但prefix judge非单调且未给永久完成latch；反复true→false→true可能超出该解释，Eq10空eligible权重分母也未给guard。隔离完整reward执行recipe/确定bounded保证。Strictness失败就不继续reference下一query，后续turn的人口依policy选择；不能把不足后续samples补为真正同state反事实。Appendix.3实际将std denominator设1、G24/48、最终48/trajectory，不能按普通归一化std噪声增益直接认证本实现已唯一causal解释。

§4 Nemotron310K→rule280K→GPT5筛30K；8KCS、另8K复杂RL/500validation。数据过滤/CoT压缩/训练并变，不能归所有收益于binary criteria。工具先exact name+args replay原response，否则30B-A3B模拟；同30B-A3B也judge，非独立真实执行或事务rollback，0.1USD标注/trajectory不含所有rollout/judge费。主文64GPU/680hours，附录未补GPU型号/precision；完整模拟一致性、totalcost/SLO未披露。

§5 Fig3较细assignment早快后collapse，只作者curves非所有环境规律、未给重复CI/直接noise量化。Table2 CM2普通8BBase27/36.40/16.89 avg26.76低于8BThinking32.00和30BA3B32.03；另5K in-domain从Thinking启动41.39是不同人口/初始化，不合并成原outdomain收益。BFCL MultiTurn36.50略低于Thinking37.00；ToolSandbox Interrupt70.31低于Thinking76.77，非每slice优。τ²四次平均、不代表其余表同样四run。训练10Kcontext/30turn与τ²>30K/200turn错配，平台cap须单独验；§6 ensemble/强judge支持细step只是未来方向未实证。必要支持/反侧足STOP，不扩全部prompts/code；唯一TRAIN-GRPO Ch33 actualowner两粒度论点待比，模拟/tool权限只handoff，不重复Ch78。Source待非作者。

### Agent 2602.12134 VAT：作者必要Source-ready

精确[缓存主文](./supplement-20261008-agent-core-1.json)及[exact-v1](https://arxiv.org/html/2602.12134v1)，actual完整§2–6/8/Limitations/Ethical、必要C robustness与E图注（官方HTML475–490/555）。**2+2+2=6**：只汇报目标价值平均提升会遗漏同一scene-action的其他维度联动；用配对pre/post的ordinal judgment shift同时观察target gain、非target变化与跨sample co-variation。采用配对多维测量的接口与局部反证，不把相关性叫干预因果、协调成本或真实下游伤害，不推断latent人格/普世价值。

§2–3 Likert映射中心化ordinal分数、support/violate标签符号，再56microvalue聚10类；Spearman跨sample shift不是单响应价值因果。GND分母实际|Gain|≠0，小gain敏感；§3 R包含self-correlation的定义下nVAT=||R||F/√|V|应至少1，却T2报告约.09–.15；E图注只说绘图省略diagonal，不明确计算也省略/额外归一。C只补80%scene bootstrap、Spearman/Kendall排序一致与56D/10D一致，没有解决metric identity。隔离exact nVAT/完整recipe与数值跨配置比较，不自行修公式。High-VAT hub按同量选择再报告放大不能成为独立risk验证。

§4 synthetic12国家×11domain×2scene×56×2action=29,568，非29,568独立scene；Introduction又称nine countries，留身份冲突。训练20,566/test9,002，B声称scenario-level split，不以条数独立性授保证。27annotator/54实例只局部人工核；T1 neutrality2.97/cultural3.24，不能认证整个数据文化真值或无害。§5四模型fewshot2/4/8与Qwen六SFT/DPO checkpoint不是等总预算、等KL或等能力对照。T2 GPT Stimulation gain−.11/−.18/−.14，Security等shot趋势亦非单调，不照录每次目标改善；tax非normative harm，SFT/DPO co-variation不同不能推出谁更安全或算法因果。

生成、自动judge、多维pre/post复评、alignment训练与scene bootstrap均计费；完整hardware/precision/batch/各model revision/token/walltime/SLO和重复seed未披露。必要支持/反侧足STOP，不扩全示例/附录图或修完整metric。唯一PLATFORM-EVALUATION-SYSTEM Ch66 actualowner比较待做；可能Only保留本地测量，不把公式争议带入Books。Source待非作者。

### Agent 2602.11908 Selective Abstraction：作者必要Source-ready

精确[缓存主文](./supplement-20261008-agent-core-1.json)及[exact-v1](https://arxiv.org/html/2602.11908v1)，actual完整§3–8/Tab1–3，必要H Alg1/Theorem假设（官方HTML379–422），不采用完整理论风险保证。**2+2+2=6**：只删低confidence atomic claim会突然失去全部信息；另生成较不具体候选，再按confidence选择最具体可过门槛版本，失败仍abstain，评价可靠性与具体性不能只按剩余atom数。采用分级claim输出支持域与信息proxy分账，不把更模糊自动等于更真实或高stakes可安全使用。

§3生成/atomize/生成abstraction+逐项评分/重构均原model多次调用，verbal confidence不是事实truth；“较弱”只prompt要求，未核每级严格logical entailment、原claim间依赖或重构不增加新claim。§4 Wikipedia+gptoss120b factchecker的unsupported含查无证据和refuted，不都真false；102人工样本F1.93只该抽样，非全部真值。信息以Wikidata entitycount稀疏proxy/uniformprior计算，claim去重相加不等真正joint语义信息，emptyset/单实体/全零原信息guard未完整给，不采用exactcoverage全域recipe。

§5同36FactScore/76LongFactobjects、六openmodel；原reasoning模式与多候选计费，不推AIforScience领域结论。§6 T2 LlamaFactScore Inline差−.70是本法负侧，竞争prompt仅单point而非同样全threshold投入。T3每response平均48/59.4atoms且每atom约4.4/4.3候选；abstract、评分、检索、SPARQL、重构/验真全部付费，硬件/完整解码/modelrevision/batch/concurrency/wallclock和SLO未披露，不把AURC改善当免费。§7随机30%prompt calibration/100重复、600mean不代表600独立部署数据；H把同response的相关atoms并pool，exchangeability/无ties假设不自动证明实际满足或conditional风险集中。minimal正确threshold以上仍可能选不同错误候选，主文未给完整候选monotonic correctness/重构保真条件；风险量θtest超过quantile也不自动等于最终多claim输出错误率。因此隔离所有α+ε高概率真实风险保证，只留作者有限代理curve和局部方法，停止理论修复/全附录。

唯一PLATFORM-EVALUATION-SYSTEM Ch66，真实claim支持/输出粒度及coverage构念actualowner待比较，不按abstraction名写sampling。失校准、弱化失真或检索不足时保留低置信删除/显式Unknown、独立依据与原输出核验；新rewrite需重新验支持是工程边界，不称原件有独立authority。Source待非作者。

### Agent 2602.11877 RouterXBench/ProbeDirichlet：作者必要Source-ready

精确[缓存主文](./supplement-20261008-agent-core-1.json)及[exact-v1](https://arxiv.org/html/2602.11877v1)，actual完整§3–7/Limitations，定点A/B1/D2官方HTML389–423/469–473。**2+2+2=6**：全局cost-quality曲线可掩盖不同预算区域排名，小模型失败识别与强模型实际补救又是两对象；区分label判别、部署band条件收益与跨domain迁移，以prefix全层hidden训练probe作具体局部实验。采用评价分账与global Dirichlet训练正则/部署固定权重身份，不授逐query自适应权重、概率校准、privacy或真实安全保证。

§3 AUROC只label排序，B1精确任务xVerify9BC与gold语义judge；开放任务GPT5既强模型又judge，label是small score≥SOTA score而非绝对correctness，所以不能说所有ability完全独立强模型身份。LPM/MPM/HCR按callrate或relativeperformance band积分，callrate不等token/延迟总费；performance未必单调，HCR空set/PerfL≤PerfS及d2≤d1没有完整guard，不采用完整metric recipe。§4 β对所有input共享，训练sample/推理均值，uncertainty≠内部因果；多domain混训与模型/label都须固定后校准。

§5主Llama3.1-8B/GPT5、3域各4K、train/val3.2K/.8K、各表test1K/10K等不同人口，linear4096/50epochs/lr1e−4；A seed42单run。T3 Dirichlet68.70vsMean68.04的额外差额远小于crosslayer vsFinal53.91，不将全收益归sampling。T2 AlpacaLPM76.50低于SelfAsk76.52，HCR13.50低于SemanticEntropy14；T6新增domain后原Alpaca71.85→71.63及BigMath66.49→66.18小退，反驳无interference/全additive宣传。D2双方同错，路由不能救；只建议abstain/扩pool未验实际online安全。prefix各层hidden/teacher标签/训练/校准与若转大模型的重复prefill都有费用，hardware/precision/batch/并发/完整modelrevision/APIfee/SLO未披露，不能直接写边云快/省内存。必要反侧足STOP，不扩实现全部pseudocode或全layers解释。

唯一PLATFORM-EVALUATION-SYSTEM Ch66，router execution只handoff既有owner；实际coverage比较待做。保持双边outcome和真实花费、label共享judge风险分开；信号或domain失配时回固定已验收路由/独立verifier或Unknown，不以AUROC批准effect。Source待非作者。

### Agent 2602.11812 EGTP/PLP长度预测：作者必要Source-ready

精确[缓存主文](./supplement-20261008-agent-core-1.json)及[exact-v1](https://arxiv.org/html/2602.11812v1)，actual完整§3/4/5、必要B.2/D.3/E.3（官方HTML320–338/460–471/505–529）。**2+2+2=6**：同prompt随机rollout长度不同，prompt静态forecast与已生成prefix后的remaining forecast须分开；用token预测entropy加权已有hidden，训练邻近长度bin软标签/期望回归，再有限评价长度误差与SJF效果。采用有hidden访问的open模型下表示/估计对象接口，不授EOF确定、训练出的softbin概率已校准、一般SJF最优或免费预测。

§3 entropy→importance只BERT10k梯度相关r=.451，不证EOS因果或全部LLM权重最优；Eq3正文temperature α未进实际式，不采用完整temperature recipe。§3.3 concat所有generatedhidden却称同head，增长维度/固定head适配未交代，隔离完整PLP执行recipe；Fig3 remaining MAE改善仅作者人口，不推出所有步预算单调。D.3 final层非普遍最佳，12层MAE70.26低于24层73.93。LMSYS GPT4/Claude2声称reuse自身hidden，但必要方法没有给可取得对应hidden的接口/代理身份，不采用closedmodel自身activation正面保证，不扩代码救该缺项。

§4 ForeLen reasoning/longseq与GRPO组4静态采样；声明沿原split仍未完整给policy-refresh/time-heldout身份。主训练1V100/10core/64GB、seed42/batch16/最多10epoch/K20/λ.95；D另局部λ.99不替换主值。T1 Qwen3B/7B reasoning本法139.04/133.57差于TRAIL132.20/124.19，宣传all-best撤回。T2两workload+vLLM/SJF未充分给到达率/完整generation硬件/batch/并发/长度/precision/tailSLO；B throughput是jobs/time而非tokens/s、padding分母actualresource不是allocated。E3单4090只预测module .65–.67ms/5–7MB；不认证含prefill logits/full-vocabentropy/所有generatedhidden留存/online反复预测的全费。有限head较快不是移除训练/校准/访问成本，平均JCT不保证fairness或starvation安全。必要反侧已足STOP，不扩其他数据/所有GRPO曲线。

唯一INFER-SCHEDULING Ch56 actualowner比较forecast提案/online更新及真实ready执行；本篇局部representation/长度测量可Only，不把dim不全或closedmodelclaim写Books。无法访问hidden、长度漂移或净费/公平性不成立时保留prompt/固定预算与透明FIFO/公平调度；Source待非作者。

### Agent 2602.11782 FlowMind：作者必要Source-ready

精确[缓存主文](./supplement-20261008-agent-core-1.json)及[exact-v1](https://arxiv.org/html/2602.11782v1)，actual完整§3/4/5/Limitations，定点E.4/F.1–2（官方HTML741–775、845–895）及相邻E.5/6必要人口。拟采用 **2+2+2=6**：同时执行业务和生成复用图会混合工具权限与目标；执行先产真实轨迹，摘要阶段撤去业务工具、只暴露构图工具，再把业务完成、图valid与实际黑盒测试分账。只采用这种阶段工具可见性/derived graph的成立边界，不从实际跑过一条路径推出图可无审批部署、无损语义或通用跨域正确。

§3摘要可聚多trajectory，但它是压缩后的提案；§4.4失败/缺步会传播，成功trace后的图也不必通过全部测试。主表141cases/694tests，T1 GPT5 ES-ReAct测试28.7低于ReAct30，Qwen32 ES-P&E24.9低于P&E25.1；GPT4.1两成功joint95.04降90.78，不能称所有指标都优。§4.3.1漏图133/200与E.5另57/190失败统计不默认为同一人口。所谓cognitive burden是作者解释，工具可见性/提示/阶段一起变，非心理因果单变量证明。

E.4 Table10 Qwen32 ES-ReAct输出tokens增加22.6%，不能推广所有阶段省tokens。F累加调用时长包括调度重试、非wallclock；主体4×A10080GBPCIe、少量4×H100、vLLM.11/PyTorch2.8，AOAI与另一“官方API”记述不合并，precision/各实验完整解码值/CI和生产SLO未披露，研究调参/开发费用不在reported finalized runs内。E.6额外三rollout/成功轨迹选择，只强Claude可解141子集；不能把聚合试次预算隐去、理论O(T+K)替代完整推理/工具/验证费用。主张受限接口的正反证已足，STOP不扩D全理论/所有prompt；复用图需独立测试、真实state与effect授权是工程推断，不说本篇已实现发布控制。唯一AGENT-WORKFLOW Ch81实际owner待比较，Source待非作者。

### Agent 2602.11754 Cooperation/Communication Delay：作者必要Source-ready

精确原件[agent-core-1](./supplement-20261008-agent-core-1.json) https://arxiv.org/html/2602.11754v1，本轮actual完整§2/3/4/5（Fig3/4和Table1文字）。拟采用 **2+1+2=5**：两agent把server上延迟发布的状态作为对手反馈，迟到报复可被误解释成对手愿意容忍，改变后续策略。只保留固定人格/自利reward的连续囚徒困境中，观测新鲜度同时改变诱因与报复链频率、合作率对delay非单调的局部反证；不能由FLCOA五层分类或一条CoT自述授真实因果意图、一般Agent可自发协作或提高延迟改善系统。

§3 server在D_i后反映该agent action并同时通知对手，两边在每Δt读取服务器currentstate、15s timestamped改变历史及累计reward；prompt明确delay存在、目标仅最大化自身reward。不是单纯包传输等待/模型推理慢与权限effect兼容性测量。§4固定双方A=1/C=−1/N=1、双方同delay，60s trial/Δt1s、rewardT/R/P/S=5/3/1/0，GPT5mini/ClaudeSonnet4/T1、每delay10trials，只最后20s统计；Fig3误差为SD非CI。观察U型合作/invertedU利用，20s恢复仍低于0s，不认证全部人格/异步不等delay/不同payoff。输出“没有报复即耐心”只是示例相关解释，未有配对同trajectory counterfactual归责。

§4.2概率toy以p titfortat+(1−p) αD_i defect解释曲线，500trials只为选p/α的模拟；原文α=.1/.2和D15/20可能使αD>1，未说明完整clipping/合法概率guard，不采用完整simulation recipe、所有delay推导或因果唯一解释。硬件/真实LLM调用耗时/并发/server排队、token/API费、精确modelrevision、初始状态及完整SLO未披露；simulatedseconds不能变成墙钟省时，也没实际测试server relocation/time-slot补偿。只框架倡议不算已实现补偿政策。必要支持/反侧足STOP，不扩代码/所有game附件。

唯一owner AGENT-MULTI-AGENT Ch82须actual比较existing stale-observation/参与方identity及协调协议：局部合作曲线留报告；若长期接口已具体覆盖则Only/Existing，不造五层新收纳。保持timestamp/staleness与真实effects独立确认、过期消息不推对方意图是工程推断，不称原论文已实现安全协议。Source待非作者。

### Agent 2602.11750 AmbiBench：作者必要Source-ready

精确原件[agent-core-1](./supplement-20261008-agent-core-1.json) https://arxiv.org/html/2602.11750v1，本轮actual完整§3/4/5/6。拟采用 **2+2+2=6**：单次指令成功不能区分缺UI路径和缺用户约束；固定atomic intent后分别移除path、parameter、anchor，令执行、规划与澄清面对不同缺项人口，再把需求覆盖、参考过程、对话补参分账。实际新增是controlled information stripping和需求first构造下的评价盲区，不从多agent judge名字授真实满意度、交互必然因果或完整动态用户意图。

§3 Prior意图完整保留，但Posterior功能意图先preset选择转pseudo-prior，posterior价值任务排除；175atomic requirement构成240tasks、25apps/five域，其中108interactive，120/80/40 simple/medium/hard。遗漏参数强制non-default，任务ADB注入/初始化；这造出必须澄清的受限人口，不代表真实用户默认值总错或自然生态比例。四clarity有同一requirement构造关系，但非所有任务四层齐全（无parameter跳Incomplete）。

§4 User simulator持U_gt，仅Incomplete/Ambiguous可补已知参数、未定义NoPreference；Detailed/Standard及trivialUI拒答。GPT5 simulator不是人类，自带幻觉/一致性风险。Raw screenshots/action/H_int经MLLM semantic serializer后才交judge，未把semantic text当独立环境truth。Outcome v_i=存在任意e_t满足r_i，TSR是每项存在证据全满足，不自行改成最终同状态同时保持所有约束；持续效果/撤回需独立验。Process semantic LCS参考顺序不认证唯一正确路径；IGR是已补gap比例而非Shannon信息量，DCR/IGR空turn/空gap guard未充分说明，不采完整计算recipe。Metric的时点/对象不同，SHR/ARR/ETR不能替代最终需求效果或对话体验。

完整§5 240tasks/最多25steps、20Snapdragon865/Android13，开源RTX5090/vLLM与闭源API混用，T=0不等确定性；T2 AutoGLM9B但正文AutoGLM7B身份不一致、UI-TARS开源表又正文列proprietaryAPI不统一修复。完整model revision/精度/全API/token费用/重复CI/SLO未披露。T2 Fairy6 RCR48.7/TSR40.4/SHR56.7、UI-Tars DCR87.2但IGR12，Qwen DCR88.9但IGR2.4说明礼貌合规≠缺项恢复；Fairy更高IGR17.7伴更低DCR73.7，不能合并为全优。非interactive框架preserved vs不同interactive model不是matched same-policy因果；mini-ablation先选Fairy成功Incomplete再关交互100→0、RCR23.8，未给选择人口/随机CI，不能授普遍非确定环境无交互必失败。§5.5三expert doubleblind100trace，κ.91、outcome Jaccard.92/step .84/96%validfill只这个抽样proxy校准，不认证全部visualnuance/真实satisfaction、risk或终态effect。动态网络/UI噪声、fluidclarity、simulator漂移均保留。

该有限评价盲区与必要反侧足，STOP不扩全部prompt/代码；后续唯一Ch66 actualowner比较需求/过程/对话分账具体已有论点或新差额，Source待非作者。执行误判/serializer或用户意图失配时保留raw证据、确定性state verifier及真实澄清/人工确认，不以代理TSR授权effect。

### 11619 When Agents Disagree：actualowner Only提议

本作者实际读Ch66 1232–1246重复可靠性合同与2589–2617低熵/高共识错mode及独立truth证据，邻接分别解释重复执行、temperature非环境确定性和partition循环风险。这两条具体原则承载本篇拟长期命题“answer/action/path稳定性只说明重复行为，不能代替正确性”；100题10runs×3model的三轴测量、step2的59/86人口以及matched20温度对照缺项仍留报告，不声称其局部结果全已写书。建议唯一PLATFORM-EVALUATION-SYSTEM **仅报告＋已有原则覆盖**，无正文diff/假POST，待reviewer实际确认。

### 11729 Crosscoder：actualowner逐字PRE提议

本作者实际Ch66 271–286及1232/2589邻接：277–279已有SAE重建/输出扰动/解释预测与干预分责，却不具体承载shared重建prior→exclusive dictionary梯度分区，以及跨tokenizer对齐后representation差异与concept差异的区分。唯一PLATFORM-EVALUATION-SYSTEM，拟在GemmaScope受限评价段后/EvaluationIdentity标题前仅加以下一段；不重复所有sensor、不授cause/安全发布。

> 跨模型的表示差异还受重建目标偏置影响：共享重建容易优先编码共有方向，可另给两模型各自保留dictionary分区，并停止专属feature对另一模型的重建梯度，以更高recall提出待验证差异。这个结构权限不等于概念只存在于一个模型；不同tokenizer还需按decoded-text窗口对齐、保留匹配失败和只取窗口末状态的损失。[受限对照](https://arxiv.org/html/2602.11729v1)中高recall伴随更多假阳性，真实模型的active/interpretable/steerable筛选又改变评价人口，affine映射失败也可能来自对齐、强度或judge。字典训练、activation采集、stitching、steering及大批API judge均计费，资源范围还不含preliminary/tuning；应先screen，再由独立行为/效果测试验证，不以representation exclusivity认证concept唯一或审计全召回。跨版本失配、发现不稳定或误报成本过高时，保留标准共享crosscoder与直接行为测试，sensor不获得effect或发布authority。<!-- source-family:SF-2026-ARXIV-2602-11729 -->

Source已非作者通过，等待reviewer逐字PRE/root窄锁，不自行写；Algorithm完整guard/精确失败n身份未采用，500,000 Opusqueries与toy假阳性/真实筛选/seed不稳定保报告。

### Agent 2602.11749 AIR：作者必要Source-ready

精确原件[agent-core-1](./supplement-20261008-agent-core-1.json) URL https://arxiv.org/html/2602.11749v1；actual完整§3/4/5/6/Impact，必要[官方B1/B2和C人口](https://arxiv.org/html/2602.11749v1#A2) HTML462–497读完。拟采用 **2+2+2=6**，安全与后执行权威差额加深受影响内容：trigger只决定哪些NL check读取已执行tool的环境状态/观察/context；命中后structured remediate执行恢复并终止原task，再由incident生成未来plan-level guardrail。采用post-effect response与future precheck不同时间/证据权限的接口，不授NL check安全证明、未来计划准确或事后恢复能够撤销已泄漏/删除的效果。

§3 ANTLR4 DSL/两个hook(工具后/step前)主文公开参考OpenAIAgentSDK，不核代码、不外推LangChain已实现；同agent解释check与执行remediation、plan-level意图不等实际toolargs/effect。语义恢复动作需单独权限/可恢复状态/当前真实环境核验是工程约束，不称论文已实现全部guard。生成新规则不能自动获得发布authority；错误过宽/过窄、opaque tool以及递归补救的新副作用仍存在。

完整§4 手写rule按已知riskcategory，RedCode25×30、SafeAgent10×25、browser RiOS7×30；#exe是实际incident发生人口、拒绝或任务失败被排除，不是所有任务成功恢复率。T1bias30exe/22det/17era、defaultcase30/19/25；作者把少det归‘未实际生成risk’却与#exe定义冲突，保留人口口径而不改分母为全检测完美。T2 electrical7/7/6/6、slip19/19/17/17；T3phishweb6/5/5/5、induced12/11/10/10等负侧，不照录all>90。人工GT只对应risk/response判定，不自补一致率/盲审/重复CI或开放世界安全。代码多不可逆、rem为–，future block不等损害已消除。

T4 check6.918/8.598/11.735s、response10.514/22.191/25.943s、eradication49.273/94.031/36.272s；benign总27.442→39.610与64.766→90.602是约44%/40%额外时延，不是全部事故检测低于20%原cost。§5并行小model/短delay为建议未测，不能授检测质量保持或delay安全。规则生成GPT5按3例+risktask，T5code84.560%det、CUA84.615%rem/89.744era，明确有infeasible恢复/抽象rule。Agent基础模型/完整版本、硬件、token/API全fee、线上SLO主必要段未披露。

B1 T6 structured rem在此人口优于self，不能由差额证明同推理budget或全归DSL形式；B2三轮100/100/50随机任务描述未充分给逐轮heldout/repeated同task身份，54→6→0等只所采分布、规则集增长，不授新分布零事故。C50/35safe只0FP，小CUA8pass/27fail，不能授开放FPR0或不损helpfulness；没有code良性完整回归。检测/规则/恢复失配时保留硬permission/effect gate、独立inspection/人工协调与原停止，不允许自动再执行不可逆补救。唯一actualownerCh72incidentresponse或Agentworkflow须按现长论点比较，Source待非作者，有限支持/反侧足STOP不扩A全部示例/代码。

### Agent 2602.11729 Cross-Architecture Model Diffing：作者必要Source-ready

精确原件[agent-core-0](./supplement-20261008-agent-core-0.json) URL https://arxiv.org/html/2602.11729v1；作者actual完整§1/2/3/5/6、Eq1–2/F3–6/T1，以及必要官方A硬件/费用与B1.6 alignment/Algorithm1/失败人口(HTML381–383/526–666)读完。拟采用 **2+2+2=6**：共享重建会偏向共享feature，DFC把dictionary划成两model专属与shared分区，截断专属feature对另一model的重建梯度，换取高recall候选；跨架构差异必须分开representation exclusivity、concept capability和下游behavior验证，不以decoder置零自行认证独有概念/未知风险全召回。

§2 BatchTopK k200、两对model middlelayers/100M alignedpairs FineWeb/LMSYS50:50；共享空间允许不同hidden维，但tokenizer对齐不是免费同token。B1.6逐decoded-text窗口贪心扩展、只取各窗口末tokenactivation、不可调和即返回此前prefix；末token包含整个window语义是希望不是已证充分映射。1000texts的992/991成功只该人口，chat/special字符/非英语失败不能以整体99%保证风险slice已覆盖。保留tokenizer/layer/对齐过滤与失配人口，不认证原算法全部guard/normalize可执行正确，未读/未采用其他附录全recipe。

必要§3.2 toy2048概念/800M pairs/5seeds标准误：高recall伴更多shared误判或无concept假阳性，不能以安全场景必然偏好recall代替实际成本目标。真实模型无GT，先另学linear stitching，用steering后Claude4.1Opus行为相似1–5作6−similarity exclusivity，25人工判定只有限judge核验；affine失败也可能是映射/强度/judge误差，并非另一model不懂概念。每类500feature先active/interpretable/clearsteering过滤，不能把过滤后分布外推全部latent。T1 FVE.817同baseline/detection87.78近87.77只重建与代理，不代表行为能力无损或全安全。

§3.3更弱分区1/3%与不同seed漏granularfeature；American/细粒度特征仅部分run发现，只有 broad特征较稳。selected30prompt/LLMjudge/95%CI支持有限注入方向影响行为，但自然输出中的唯一必要原因、来源(训练或数据)未证明；最大激活feature也可无稳定steering。版权拒绝降低时coherence退并经常hallucinate，不能读成取得准确内容；正向又过度拒绝benign。§5 base-v-finetune mirrorfeatures也可能干扰，不授一般跨任何模型的审计完整性。只保留screen→validate workflow，不把政治/版权标签或作者表述当事实truth。

必要A披露：每pair activation采集3×H10080GB约24h，每crosscoder单H10080GB约24h、final五crosscoders；每experiment约500,000 Opus API queries，资源范围不包括preliminary/tuning。另alignment/cache、100M数据、interpretation/stitching/steering/judge及验证费用都计，不授完整总API费/上线SLO。B1.6失败Table5正文n9与column n8身份冲突保留，不采用精确失败全集。发现不稳定、对齐失配或假阳性费过高时，保留标准crosscoder与behavioral/redteam suite、独立effect核验；词表/架构/版本变化重新校准。reviewer已actual必要Source通过；唯一ownerCh66实际差异探测/解释audit需比较，不自动写安全保障或稳定发现保证。必要支持/反侧足即STOP。
