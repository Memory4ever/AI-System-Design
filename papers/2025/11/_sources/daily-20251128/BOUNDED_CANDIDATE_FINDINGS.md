# Nov28 有限题摘、日期隔离与关键反侧

作者Aristotle。本窗与查询见[SOURCE_CHECK](./SOURCE_CHECK.md)。四窄API58返回/55唯一发现，加DC相关五身份和本日DeepSeek真实Research的一身份，合计61发现身份；五标题明确范围关闭，实际读56份完整exact-v1题摘，五份题摘后关闭，51份保留潜力。**51不是确定当窗候选或51份标准/深入审阅完成**；未评分/采用/写Books。完整原题摘与逐项身份见[exact-v1](./exact-v1-abstracts.json)，原日期字段见[dates](./exact-date-fields.json)。只把与本日窄主题相关的发现送入题摘判断，宽DC338未扩为队列。

## 首批八项

[FIRST_CALIBRATION](./FIRST_CALIBRATION.md)保留MLPMoE21089、NonMonotonicViT21635、SDT21408、DOPD20982、TraceGen21690、KRISP20795、StructuredPrompt20836、MultiPrefix20799的原题摘、具体增量与原日期。首批已交root，不自授校准。潜力清楚而非摘要已证实；必要反侧如下修正采用边界，不因有局部负证据关闭。

## 后续潜力：只审决定性必要内容

以下每项已实际读完整精确v1题摘；编号为原arXiv ID，原title不借当前晚版。机制方向为准入潜力而非经证据证实，统一日期外部隔离但逐项原字段可查，不以同标签代替日期恢复。

| 精确v1身份 | 原约束→实际潜在增量→可能改变的具体选择 |
| --- | --- |
| [G2VLM 2511.21688](https://arxiv.org/abs/2511.21688v1) | 语义VLM缺空间几何监督→统一重建特征/3D属性与交错空间推理→几何表示和推理接口可共同训练的条件，不采所有空间任务领先 |
| [RoParQ 2511.21568](https://arxiv.org/abs/2511.21568v1) | 同义问法答案不稳→judge筛选不一致改写并跨变体SFT→训练/评价需区分准确率与改写方差 |
| [Model merging 2511.21437](https://arxiv.org/abs/2511.21437v1) | 视觉子空间合并收益不能直接迁移→四LLM随机checkpoint组合的反侧→合并前任务几何/参数选择需重新考虑；不是所有LLM只能TaskArithmetic |
| [VLM distractors 2511.21397](https://arxiv.org/abs/2511.21397v1) | 更多推理不保证抗干扰→视觉干扰准确率下降但长度不增的局部对照→评价应分开干扰与长度；不采用强制compute导致下降的因果说法 |
| [R-MUSE 2512.17911](https://arxiv.org/abs/2512.17911v1) | 直接forget可能伤推理→保留reasoning的多模态unlearning目标→考察信息泄露与推理保留两轴。Available Dec，未深审，不授删除/隐私保证 |
| [Masks 2511.21338](https://arxiv.org/abs/2511.21338v1) | 双向masked模型上下文不必稳→附加mask干扰、local positional bias及loss-invariance修正→比较上下文表述/训练不变条件 |
| [Martin's Law 2511.21334](https://arxiv.org/abs/2511.21334v1) | 模型规模/训练不必单调形成词义→Pythia多checkpoint词频/多义关系测量→可审表示形成的局部反证，不把DBSCAN簇数当唯一真值 |
| [CCD 2512.02044](https://arxiv.org/abs/2512.02044v1) | 单步confidence解mask忽视轨迹→历史conditional mutual information自适应选择→并行解码质量/步数取舍；Available Dec |
| [LAPA 2512.07855](https://arxiv.org/abs/2512.07855v1) | 乘法/稀疏预测代价→log-domain leading-one预测与多轮shift稀疏执行→预测成本与实际硬件可行性；Available Dec |
| [Bits to Rounds 2511.21103](https://arxiv.org/abs/2511.21103v1) | 并行解码confidence不直接对应轮数→信息量/轮数理论及探索不确定性→需核假设后选择解码预算，不授无条件最优 |
| [Orthographic 2511.21086](https://arxiv.org/abs/2511.21086v1) | reasoning token多不必提高约束满足→28配置/58字谜中局部预算与分布偏差反侧→保留任务与difficulty评价边界，不归因根本架构 |
| [Audio tokens 2511.20973](https://arxiv.org/abs/2511.20973v1) | 音频长token成本→分段/平均池化与LoRA的质量-token对照→音频压缩预算选择，不直接授3x端到端 |
| [Length-MAX 2511.20849](https://arxiv.org/abs/2511.20849v1) | token数量/bytes归一化不同→graph partition+length greedy的分词与五运行对照→训练预算需同byte/损失协议，不授所有LM token最大化最优 |
| [SAGE 2511.20820](https://arxiv.org/abs/2511.20820v1) | SAE自动解释缺反馈→Agent主动实验和解释修正→feature解释可信度评价可改；原摘要重复句保持raw不修原文 |
| [DSD 2511.21669](https://arxiv.org/abs/2511.21669v1) | 边云speculation网络/长度不稳→AWC自适应窗口→网络预算和draft收益的局部取舍，simulation不授生产 |
| [GPU-Virt 2512.22125](https://arxiv.org/abs/2512.22125v1) | 软件quota不等实际算力隔离→HAMi/BUD控制精度与受限负载反侧→GPU资源合同需核实测权限；synthetic LLM/模拟MIG边界见下 |
| [BRIDGE 2511.21104](https://arxiv.org/abs/2511.21104v1) | 只反馈验证错误不必形成好证明→code/spec/proof结构化中间表示→程序验证的状态/反馈机制潜力，未授所有证明正确 |
| [GPU memory 2512.07853](https://arxiv.org/abs/2512.07853v1) | 多模态训练peak不易估计→layer factorization峰值预测→预准入预算与误差边界，Available Dec |
| [LLaMCAT 2512.00083](https://arxiv.org/abs/2512.00083v1) | 内存访问并发与cache拥塞→MSHR仲裁/负载均衡及thread throttling→LLM推理trace下执行计划取舍，混合cycle simulation非产品性能；Available Dec |
| [Activated LoRA 2512.17910](https://arxiv.org/abs/2512.17910v1) | adapter改动破坏prefix KV共享→base-aligned activation mask/hash→限定兼容前缀跨adapter复用，不外推全部跨模型；Available Dec |
| [ADVLA 2511.21663](https://arxiv.org/abs/2511.21663v1) | 通用patch需要昂贵训练→attention-guided top-patch稀疏梯度→可审特定白盒攻击预算/失败条件，不授物理部署保证 |
| [UPA 2511.21192](https://arxiv.org/abs/2511.21192v1) | 每victim查询昂贵→surrogate feature/InfoNCE与attention universal patch迁移→限定黑盒transfer权限，不把physical-trained数据当机器人实测 |
| [RS Co-training 2511.21272](https://arxiv.org/abs/2511.21272v1) | 高分辨率VLM定位/多任务负载→dynamic-resolution ZoomInChain与共训对照→保留一般表示/分辨率条件潜力，不仅凭remote-sensing应用关闭 |
| [ND tokenizer 2511.21191](https://arxiv.org/abs/2511.21191v1) | 3D点场景token昂贵→multi-scale normal-distribution transform/decoder→3D codec与prompt segmentation粒度取舍 |
| [SocialNav 2511.21135](https://arxiv.org/abs/2511.21135v1) | 社会导航反馈难探索→脑式动作层级/flow policy与GRPO安全探索→模型行动训练机制，不因导航标题泛化关闭 |
| [RadarFM 2511.21105](https://arxiv.org/abs/2511.21105v1) | 雷达scene的continuous坐标/文本不齐→native-coordinate caption/hash-aware contrastive→保留通用模态表示潜力，不仅看领域分数 |
| [ENACT 2511.20937](https://arxiv.org/abs/2511.20937v1) | pixel generation指标不代表行动世界模型→POMDP forward/inverse序列重排对照→环境预测/状态一致评价盲区，8972样本不授普适因果 |
| [Matrix 2511.21686](https://arxiv.org/abs/2511.21686v1) | 中心协调器数据生产瓶颈→peer queues/decentralized taskflow→同hardware吞吐条件可审，不借repo名字造release |
| [BAMAS 2511.21572](https://arxiv.org/abs/2511.21572v1) | 固定Agent拓扑/模型忽略预算→ILP模型选择+RL拓扑→joint allocation与communication-budget条件 |
| [Tool-RoCo 2511.21510](https://arxiv.org/abs/2511.21510v1) | 工具可用不代表协作使用→四自治style/三机器人bench中低协作激活局部反侧→检查protocol/action使用，不归因普遍Agent架构失败 |
| [MADRA 2511.21460](https://arxiv.org/abs/2511.21460v1) | 单judge容易过拒→四维critical evaluator引导debate/consensus→风险识别与safe-task拒绝的取舍；并非无compute成本或实际物理安全证明 |
| [Prune4Web 2511.21398](https://arxiv.org/abs/2511.21398v1) | DOM逐项LLM读取昂贵→语义Python scoring/pruning program→grounding接口与2turn反馈成本条件，不授所有web端到端加速 |
| [OVOD-Agent 2511.21064](https://arxiv.org/abs/2511.21064v1) | 稀有类被动VLM检测少反馈→八状态MDP/bandit主动选择及transition reward→探索/检测反馈机制潜力，不仅领域指标 |
| [SABER 2512.07850](https://arxiv.org/abs/2512.07850v1) | 小mutation可能不可逆→摘要/precondition check/用户确认/历史reflection→可审aux检查与任务标注纠错，Available Dec，不提前采用 |
| [RILKE 2511.20892](https://arxiv.org/abs/2511.20892v1) | 连续edit互扰→局部低维representation edit/改写稳健router与frozen weights→知识控制位置/干扰条件 |
| [EvoMemory 2511.20857](https://arxiv.org/abs/2511.20857v1) | 静态对话不代表test-time学习→streaming experience、ExpRAG/ReMem主动refine→检索与记忆更新的评价条件 |
| [TrackList 2511.21006](https://arxiv.org/abs/2511.21006v1) | 单问法低估head/tail知识→definition/example query linguistic diversity与response-diversity反侧→保留知识评价protocol潜力；医学样本不等于原命题纯医学应用 |
| [Spira 2511.20834](https://arxiv.org/abs/2511.20834v1) | 稀疏卷积坐标map准备开销→packed coordinate一次map/双dataflow并行→3D模型kernel形状/稀疏性条件 |
| [Aragog 2511.20975](https://arxiv.org/abs/2511.20975v1) | 多模型Agent阶段路由昂贵→one-time router跨accuracy configs与stage load scheduling→质量/SLO与路由开销取舍 |
| [HPC 2511.21413](https://arxiv.org/abs/2511.21413v1) | batch Slurm难适应同步服务→job/endpoint注册/health readiness及跨scheduler控制→可审具体状态交接与网关瓶颈，不仅K8s+Slurm组合 |
| [MemFine 2511.21431](https://arxiv.org/abs/2511.21431v1) | MoE训练显存挤压→chunk route/experts/recompute与分析memory预算→细粒度训练调度选择，48/4.42%未正面采用 |
| [Model cards 2511.21661](https://arxiv.org/abs/2511.21661v1) | model-card接口协议不免费→MCP/REST local microbench与session设计→具体stack通信成本反侧，不以benchmark标签关闭 |
| [Math-V2 2511.22570](https://arxiv.org/abs/2511.22570v1) | 最终答案正确不认证推导→准确/忠实verifier奖励、自检自修与增大验证计算→训练/验证gap潜力，未采用竞赛分数 |

## 五份题摘后关闭

- [Time series 2511.21514](https://arxiv.org/abs/2511.21514v1)：完整v1题摘的activation patching/SAE用于一个time-series分类任务，未明确新增通用解释机制或模型形成条件；不是因小模型本身关闭。
- [MortgageLLM 2511.21101](https://arxiv.org/abs/2511.21101v1)：residual instruction/domain experts/task routing组合服务mortgage数据，摘要给领域指标与fewshot用法，未给改变通用优化/路由条件的具体增量；不借DPO/dual-expert成熟名词准入。
- [Burmese ASR 2511.21088](https://arxiv.org/abs/2511.21088v1)：IPA/phonetic alignment seq2seq纠错服务低资源Burmese，未披露新的通用ASR表示/优化条件，领域提升不够准入。
- [AI Urban Scientist 2512.07849](https://arxiv.org/abs/2512.07849v1)：科学研究工作流应用，ROADMAP下一阶段暂缓，不能由Agent节点重引。
- [L4M legal 2511.21033](https://arxiv.org/abs/2511.21033v1)：完整题摘与必要§5原core L1550–1580读后，LLM角色+SMT对法律statute/事实抽取的组合及领域指标没有新增通用证明条件；formalization错误传播、deterministic rule parsing的既有边界明确，不能把SMT对子式soundness升级法律语义保证。此处不以“已有原则/名字有owner”单独排除。

五标题范围关闭仅原发现题名明确：2511.21500 Physiological Signal、2511.21034 Dairy Cow、2511.20956 Breast Ultrasound属于临床/科学应用；2512.07865 Swedish register mobility、2511.21364 Bangla disaster属于领域既有Transformer应用。未读其全摘要/正文、不称全类排除，原题名见四query。无所见题名纠错/撤回标记；没有为“没有标记”遍历全站。

## 必要受影响安全与设计反侧：实际读到哪里

**MultiPrefix 20799** [原core](./core-2511.20799v1.txt) L457–655定义/公式、L1259–1325预算、1470–1490/1748–1870反侧：`P=ceil(eta*|s|)`与prefix distinct embedding阈值是heuristic，不是最优证明。GCG `max(10,2P)` seeds与达到目标停止；1000随机gibberish negatives无命中不是matched natural未见样本保证；GCG+PS会改变mem标签。Aligned/base/chat templates改变可提取性，不等数据抹除；Mistral图7/prose 24.2/22.0有不一致，不选择单数字。900 PileCC分层作者成本平均不外推分布普遍。只保留审计预算/阴性解释潜力。

**ADVLA 21663** [原core](./core-2511.21663v1.txt) 方法projector白盒gradient、L810–895 setup、L1084–1156结果/敏感性：LIBERO四suites每10task×50rollout，四OpenVLA独立suite变体，sim/H100。FR=1-SR，clean23.5与attack100不叫clean0上ASR100；UADA亦100。4/255、6iter、top10%patch；0.06s单迭代与UADA15h训练是不同成本单位，不授端到端优势。“imperceptible”未有人类实验，不当物理机器人安全保证。

**UPA 21192** [原core](./core-2511.21192v1.txt) 方法及§4.1 L3282–3398/Table1：BridgeDataV2 physical训练数据与LIBERO simulation分别训练surrogate；victim OpenVLAoft/oftw/pi0，victim无梯度查询不等无白盒surrogate依赖。每suite十task十trial/预定不遮挡patch位置；作者physical setting是训练分支，当前评价LIBERO，不能认证实机物理攻击。Feature deviation/repulsive InfoNCE、内外优化与attention semantic loss支撑限定transfer机制，不授全任务/家族有效。

**MADRA 21460** [原core](./core-2511.21460v1.txt) §3 L310–502初始化/四维critical评分/多轮debate，§5/6 L1245–1270 dataset/setup及L1880–1898反侧：800 safe/unsafe各400，作者专家重新标注92.3% agreement非独立安全真值。两sim环境/17与8动作API；critical model能力和agent数改变safe over-rejection（某配置可35.8%）与unsafe检测取舍，不能只录90%。不训练≠“no demand for compute”；没有matched全部tokens/API成本，不能授训练免费、普遍physical safety或因果herd消除。

**SABER 2512.07850** [原core](./core-2512.07850v1.txt) §4 L1028–1067、§5 L1128–1200、§6 L1280–1410与限制L1499–1518：aux mutation checks/summary/preconditions/user confirmation及cache embedding history不免费；作者纠正airline70/retail92 caps与31/50、53/115 underspecification，未独立逐任务diff。Qwen main/aux、Claude用户simulator、30turncap不授matched总token成本；SWE仅reflection非mutation gate。回归关系不授因果降低92%风险、28%相对不写28points；Available Dec10，不提前采用更正/安全保证。

**KRISP 20795** [原core](./core-2511.20795v1.txt) §2–6 L95–365：原BASE在OKVQA32.37% raw、ModelA在VQAV2 74.14% relative、ModelB在DAQUAR27.75% relative，数据集/协议不同，不能叫受控复现达到75%或效率更优。DAQUAR text8.88%/relative27.75、频率/过拟合与ConceptNet噪声/反义词，保留局部低资源pitfall方向；不采“fundamental capacity threshold”因果或有限答案域免hallucination。

**GPUVirt 2512.22125** [原core](./core-2512.22125v1.txt) L3772–4010：HAMi/BUD实际软件控制测试，但MIG是ideal100建模/规范模拟，LLM为custom CUDA attention/KV/batching synthetic非完整框架。A100 singleGPU与版本依赖、BUD作者改进非独立评估，不授真实MIG所有数字或资源隔离形式证明。局部quota实际控制精度的反侧可留潜力。

**ModelCards 21661** [原core](./core-2511.21661v1.txt) L378–437：Jetstream2/Hawaii、PythonMCP1.10.1 SSE/Neo4j5.21、1000ops/fewKB及13.63MB pseudo-syntheticWAN；REST7.5ms/nativeMCP26.7ms与wrapper只此stack。Backend相近但Flask/FastMCP/integration不等protocol因果控制；不写所有MCP3.6x代价、session通用保证或因owner无模型卡名称造Books缺口。

**Merging 21437** [原core](./core-2511.21437v1.txt) §5 L2400–2410及Appendix L3606–3675：随机checkpoint且未alignment/clustering；TIES main选10%density，作者明说满density结果回升但接近TA所以未选，负侧受超参选择影响。不能宣称所有LLM方法失效或TaskArithmetic唯一可用，几何解释仍作者推断。

**VLM distractors 21397** [原core](./core-2511.21397v1.txt) setup与L615/826–828、Appendix预算L2133–2155：natural overthinking观察不能推出强制compute降性能；prompt1024/2048/4096未有效控制长度，不是hardcap对照。简单VQA/Waterbirds与属性抽取协议，不授数学/Agent多步普适架构结论。

**HPC 21413** [原core](./core-2511.21413v1.txt) §3.2/3.3 L570–700、§5 L950–990：synchronous job submit避免port竞态、job/endpoint双注册、health ready后才路由，启动超时30min；queue>5s持续30s/15s worker反馈。每request数据库lookup/网关TTFT瓶颈与benchmark网络未分清，作者明说work-in-progress/non-best-practice。保留跨scheduler state交接及局部瓶颈潜力，不授生产ready/全HPC规模best practice。

## 有限日期恢复与停点

MLPMoE gist creation Nov26 05:36:05Z、public false/unlisted及单history不是首次公开正文；TraceGen项目页此次未见dated News；Matrix repo创建Mar28/pushed2026非paper release。StructuredPrompt HELM PR Sep27→Oct4已是旧integration。具名搜索仅第一页，其提交标签/后publication不构成精确首公开。Math-V2官方Nov27未TZ、Submitted Nov27 16:01:22Z、Updated Dec1、release API[]与README native reset/web官方恢复均已实际本日尝试；不能把later metadata当public，也不简单以提交日判窗外。

51潜力必要首公开精度/上下界仍未确定，具体需求只请求一次：原官方公告、作者首次公开事件或完全落窗上下界。到达时仅重开该身份/受影响证据，不重扫整月；不同Available Dec字段原样保留，不强行填本窗或用它认证完整paper首次公开。当前不评分/正面采用/Books，不授全methods/附件。首批/代表性负侧及来源等待root非作者校准，已准备内容无需等所有日期材料到达；共享Books/state/index不写。
