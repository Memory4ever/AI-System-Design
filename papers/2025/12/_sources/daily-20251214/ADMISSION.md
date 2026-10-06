# 12/14 具名贡献筛选

作者Gibbs，2026-10-02实际读取。原77项为作者实际精确v1完整题摘；本次七项重开定点复用Mill已实际取得的同身份exact-v1完整题摘/必要局部，见[INDEPENDENT_REVIEW §3–4](INDEPENDENT_REVIEW.md#4-给gibbsroot的最小普通修正)，不冒称作者重读全文。仅含糊准入与具体拟采用命题补局部方法。不是从月目录批量套判断，不以Submitted授公开，不评分日期未授家族。初批校准请求见[首批记录](ADMISSION_CALIBRATION.md)，查询/范围见[SOURCE_SCREEN](SOURCE_SCREEN.md)。

## 潜在家族：模型、训练、系统

| 精确v1 | 原约束 → 原文具体增量 → 窄设计判断；未授事项 |
| --- | --- |
| [WATOS12279](https://arxiv.org/abs/2512.12279v1) | 固定wafer面积挤占compute/memory/D2D；联合架构模板、TP/PP和recompute/remote checkpoint；不能先固定训练策略再独立选硬件。不授模拟为真实生产收益。 |
| [V-Rex12284](https://arxiv.org/abs/2512.12284v1) | 流式视频增量prefill的KV变化；hash-bit时空cluster与按weighted累积质量选token、DRE early-exit；选择预算应随层/head变化。不授exact Attention或硬件实机FPS。 |
| [MixtureKit12121](https://arxiv.org/abs/2512.12121v1) | checkpoint专家组合/交付不统一；共享/专家namespace与forward patch共用保存路径；兼容HF不等于近期MoE kernel兼容。BTX/BTS本身借自前作，不冒称新增算法。 |
| [ACR12219](https://arxiv.org/abs/2512.12219v1) | 属性混在单visual embedding；patch与attribute两级专家在学习时分离；表示解耦不只靠post-hoc头。不因小型zero-shot分类实验排除，不授通用语义解耦。 |
| [MK-GP12238](https://arxiv.org/abs/2512.12238v1) | 固定semantic distance不适应任务；监督学习Matérn/polynomial组合kernel用于ICL选择；距离定义应与检索目标一起验收，不授任意任务提升。 |
| [SCIR12337](https://arxiv.org/abs/2512.12337v1) | IE结果纠错耗重训；双路径self-correction与GPT4检测器蒸馏；纠错sensor/模型训练可分工，不授摘要成本为匹配预算归因。 |
| [DAPT12384](https://arxiv.org/abs/2512.12384v1) | 领域适应假定越多token越好/担忧遗忘；1B/3B四token预算见收益递减且general loss稳定；窄适应/漂移评价值得核，不外推7B–70B。 |
| [VGPO12387](https://arxiv.org/abs/2512.12387v1) | flow阶段价值不同且group reward枯竭；过程value与absolute anchor改变credit/归一化；不授普遍消除reward hacking。 |
| [HetRL12476](https://arxiv.org/abs/2512.12476v1) | 异构GPU/网络与多模型RL依赖不能分开；多层搜索及successive-halving预算联合调度；不照录最大吞吐为所有集群保证。 |
| [Cleave22142](https://arxiv.org/abs/2512.22142v1) | edge memory/网络/churn限制训练；selective hybrid TP、parameter server与设备成本选择；v1实际Dec13提交，不能由后段ID排除或归日。 |
| [CurvaDion13728](https://arxiv.org/abs/2512.13728v1) | 低秩通信仍每步同步；RMMC以已有momentum检测方向曲率并调cadence；需核proxy假设与收敛，不授99%为wall-clock。 |
| [几何11866](https://arxiv.org/abs/2512.11866v1) | saddle/phase/mode connectivity分散解释；L2探测error landscape及解析条件；小MNIST可有学习理论贡献，不授大模型相变普遍律。 |
| [GER11867](https://arxiv.org/abs/2512.11867v1) | synthetic replay默认维持分布；bias/variance分析和latent alignment退化；模型数据闭环须独立验，不授任意synthetic data均失败。 |
| [Neural Chameleons11949](https://arxiv.org/abs/2512.11949v1) | activation monitor以冻结表示可检测为前提；主实验helpful-only/abliterated organism经触发微调避开未见monitor，ensemble/nonlinear仍非全免疫；安全训练版本为另附录条件，不当成实际部署攻击。 |
| [Context11986](https://arxiv.org/abs/2512.11986v1) | 直接生成难区分含糊风险/良性请求；RL context generator从prompt抽取条件；需同时核harm/refusal，不授“推定intent”为事实。 |
| [Safety12066](https://arxiv.org/abs/2512.12066v1) | 单次拒答代表安全的假设；seed/temperature下拒答翻转及judge agreement；有限模型/876prompt协议不授普遍3次足够。 |
| [Cloak12086](https://arxiv.org/abs/2512.12086v1) | obfuscation效用/隐私须重训下游；contrastive disentanglement引导latent diffusion控制取舍；保留表示/目标分责线索，不授传感器结果为形式隐私。 |
| [BOOST12131](https://arxiv.org/abs/2512.12131v1) | 低秩瓶颈套full-rank TP通信浪费；bottleneck-aware TP、online RMSNorm/grouping/低秩checkpoint；不授不同模型质量完全可比。 |
| [FiCCO10236](https://arxiv.org/abs/2512.10236v1) | shard级overlap受dataflow限制；更细分解及operation inefficiency共同调度，DMA卸通信争用；不授一律细粒度更快。 |
| [RLTune10271](https://arxiv.org/abs/2512.10271v1) | 离线profile限制异构AI job配置；RL priority与MILP placement分工；trace收益需核SLO/公平，非生产已部署。 |
| [ESS10576](https://arxiv.org/abs/2512.10576v1) | MLA latent cache容量限制batch；分层offload保留latency-critical部分GPU；模拟吞吐不能授真实PD尾延迟。 |
| [TritorX10977](https://arxiv.org/abs/2512.10977v1) | kernel生成只看热门算子性能；linter/JIT/OpInfo围绕完整ATen coverage；通过所列tests非任意输入正确性，月收录非首发。 |
| [GPU sched10980](https://arxiv.org/abs/2512.10980v1) | 静态priority有碎片/饥饿；受控AI jobs仿真分别比较hybrid/backfill/batch与fairness；局部透明heuristic也可贡献，不授生产保证。 |
| [Dora10990](https://arxiv.org/abs/2512.10990v1) | throughput-only hybrid parallel忽略QoE；模型partition/争用网络/运行时plan组合；QoE约束与能耗须共同核，不因edge负载关闭。 |
| [GPU编译11200](https://arxiv.org/abs/2512.11200v1) | code迭代CPU/GPU传输；GPU-native传统/神经/hybrid编译界及probabilistic verification；需核理论假设，不采用10–100倍或“保证正确”。 |
| [RollMux11306](https://arxiv.org/abs/2512.11306v1) | on-policy分离集群依赖bubble；co-execution group、host residency与phase复用；SLO100%限所测，模型换入成本不能消失。 |
| [Parallax11532](https://arxiv.org/abs/2512.11532v1) | 不支持算子回CPU造成串行和峰值；branch-aware DAG/arena与memory约束调度；不授任意dynamic模型无改动可加速。 |
| [ECCO11727](https://arxiv.org/abs/2512.11727v1) | 每camera重训重复drift；关联分组共享模型并联合GPU/frame transmission；需核共享负迁移，非所有camera可合并。 |
| [SpGEMM12036](https://arxiv.org/abs/2512.12036v1) | irregular访问限制GPU稀疏乘；hash多阶段和near-HBM indirect access用于GNN训练；GNN是直接模型计算，不按小模型/图场景排除。 |
| [LiveUpdate12295](https://arxiv.org/abs/2512.12295v1) | EMT跨cluster更新staleness；推理node低秩trainer、rank自适应和NUMA/QoS隔离；model更新与inference干扰应实测，不授近零开销。 |
| [DCO07312](https://arxiv.org/abs/2512.07312v1) | SPM管理复杂；LLM accelerator软件dataflow引导shared cache dead-block/bypass/thrashing；模拟/RTL不授芯片生产运行。 |
| [RACAM09304](https://arxiv.org/abs/2512.09304v1) | bit-serial DRAM-PIM缺reuse；locality buffer/broadcast及LLM映射；精度/面积/完整成本待核，不采用巨大倍数。 |
| [ODMA09427](https://arxiv.org/abs/2512.09427v1) | LPDDR随机访存使paging代价高；长度预测+动态bucket+large safeguard；硬件条件改变分配选择，不授无错预测或HBM普适。 |
| [PD-Swap11550](https://arxiv.org/abs/2512.11550v1) | FPGA面积需兼顾prefill/decode；attention分区DPR而weight/TMM静态，重配置藏入compute；阶段切换成本和route约束必要。 |
| [FSL-HDnn11826](https://arxiv.org/abs/2512.11826v1) | few-shot端侧更新成本高；weight-cluster提特征、HDC single-pass及early-exit/branch/batched执行共同设计；40nm实测6mJ/image、28images/s只限10-way5-shot条件，不授一般模型收益。 |
| [DFedReweighting12022](https://arxiv.org/abs/2512.12022v1) | 异构client贡献不能用统一聚合权重表达；辅助目标性能与定制加权，适当组合下线性收敛；公平/Byzantine结论须核各自条件，不授任意攻击稳健。 |
| [SiLU12132](https://arxiv.org/abs/2512.12132v1) | ReLU逼近深度/误差代价；层次平方构造使SiLU网络在给定Sobolev函数类常深度、指数误差条件成立；理论表示能力不授硬件成本、可训练性或通用模型质量。 |
| [CFL-HKD10443](https://arxiv.org/abs/2512.10443v1) | client聚类个性化与全局知识碎片化冲突；双层聚合及多教师蒸馏保持跨cluster迁移；直接训练机制，不只IoT指标，未授形式隐私或消除负迁移。 |
| [Entropy Collapse12381](https://arxiv.org/abs/2512.12381v1) | 自生成数据闭环可能缩减表示多样性；§3假设反馈强化/有限novelty并以分布更新骨架解释，§5最小状态仿真、§6.1投影到自训练；保留有条件理论解释供核，不把领域投影当真实神经网络验证，不采用普遍阈值/不可逆定律。 |

## 潜在家族：多模态、评价与Agent

| 精确v1 | 原约束 → 原文增量 → 窄判断；未授事项 |
| --- | --- |
| [Emergence15776](https://arxiv.org/abs/2512.15776v1) | leader知道目标却不能ground follower；非对称观测下pull clarification对push的局部反证；不授所有失败仅通信或通用安全。 |
| [TS-DP15773](https://arxiv.org/abs/2512.15773v1) | diffusion policy时变任务成本；distilled drafter+RL scheduler调speculation；accept率不自动证明lossless control。 |
| [SMRABooth12193](https://arxiv.org/abs/2512.12193v1) | subject/motion LoRA干扰；object-level两表示及位置/时序稀疏注入；分责机制待对照，不授通用解耦。 |
| [AutoMV12196](https://arxiv.org/abs/2512.12196v1) | 长music video跨段一致性/评价；shared character bank与分工、LMM judge落后expert；不是仅因为multi-agent名准入，不授judge替人。 |
| [Frame segmentation12246](https://arxiv.org/abs/2512.12246v1) | timestamp生成无frame梯度；0/1输出概率上叠segmentation loss；目标/表示替代不只是换视频任务。 |
| [Endless World12430](https://arxiv.org/abs/2512.12430v1) | 长视频3D漂移；conditional AR训练及global3D attention；visual scene一致性非action dynamics或无限物理保证。 |
| [PeRL-VL12487](https://arxiv.org/abs/2512.12487v1) | final-only reward忽略视觉抽取/逻辑错误；description reward与text reasoning SFT分开；judge真值与各阶段收益待核。 |
| [Visual Faithfulness12218](https://arxiv.org/abs/2512.12218v1) | 最终答对掩盖unfaithful perception；step decomposition、human meta-eval与局部regeneration；准确率不授解释忠实。 |
| [Intention-Drive12302](https://arxiv.org/abs/2512.12302v1) | geometric准确未必满足human intent；ISR语义评价显示baseline差距；窄action语义反证非实际道路安全。 |
| [STAGE12372](https://arxiv.org/abs/2512.12372v1) | sparse keyframe跨shot不连续；start-end storyboard、memory pack/dual encoding/transition training；不授memory为真实world state。 |
| [VideoARM12360](https://arxiv.org/abs/2512.12360v1) | 全视频预处理耗token；on-the-fly coarse-to-fine tools与hierarchical memory更新；需核漏看/重复工具成本。 |
| [UniMark12324](https://arxiv.org/abs/2512.12324v1) | generation-time水印需内部logits且不能处理既有内容；post-process adapter同时hidden/visible并接黑盒；是兼容路径，非新增水印算法或法规保证。 |
| [Causal quant13725](https://arxiv.org/abs/2512.13725v1) | overall量化分数掩盖rung差异；CLadder/CRASS敏感度差与GT GraphRAG选择性收益；不把ground-truth graph当现实检索。 |
| [RAN12400](https://arxiv.org/abs/2512.12400v1) | retrieval相似不授compliance；III-B/TableII普通RAG较No-RAG准确下降、Agentic RAG增延迟，仍可能规范引用错；仅4files×3runs，不授autonomous enforcement。 |
| [Metaphor12444](https://arxiv.org/abs/2512.12444v1) | GPT评分相关不等于各刺激可替人；sensorimotor load下相关变弱及不同属性misalignment；只保留judge效度条件，非EEG/心理应用结论。 |
| [Introspection12411](https://arxiv.org/abs/2512.12411v1) | detection自身概念被当普遍自知；prompt变化崩溃却可区分注入强度；能力/强度与来源识别分开，非任意模型自省保证。 |
| [Chain Affect12283](https://arxiv.org/abs/2512.12283v1) | reasoning不变可能掩盖高自由生成/协作漂移；重复负面输入与self-selection反馈、role影响；不将功能情感证据拟人化。 |
| [Cognitive-YOLO12281](https://arxiv.org/abs/2512.12281v1) | NAS loop成本高；dataset meta-features到NADL结构生成/编译并有RAG消融；直接模型架构设计不只是检测应用，不授“first principles”因果宣传。 |
| [Taint slicing12313](https://arxiv.org/abs/2512.12313v1) | token切片破坏代码flow；callback/Promise backtracking保留安全语义；上下文选择与模型检测成本联合核，不授99%体积减少为完备检测。 |
| [Market12264](https://arxiv.org/abs/2512.12264v1) | code跑通掩盖数值错误；multi-round pass与P&L reference分开、完美pass仍误；只采执行/结果评价边界，非金融策略。 |
| [Cultural12488](https://arxiv.org/abs/2512.12488v1) | system文化prompt不必达目标；多模型VSM13条件下中国/日本偏差；窄prompt评价反证，非国别本质或一般文化结论。 |
| [KidsArt12503](https://arxiv.org/abs/2512.12503v1) | 单scalar美感评价混合属性；attribute-specific LoRA+ordinal RAFT、多维expert labels；直接评价模型目标，非仅教育应用，需核rubric间干扰。 |
| [ProImage12220](https://arxiv.org/abs/2512.12220v1) | visually plausible不等于规格准确；细粒binary rubric及failed-check回编辑；评价生成模型而非AI科学发现，LMM judge不能自授物理真值。 |
| [ViInfographic12424](https://arxiv.org/abs/2512.12424v1) | 单图/OCR隐藏跨图证据聚合；human verified multi-image/nonspan错误更强；窄评测盲区，不只靠新语种/数据数量准入。 |
| [3D11574](https://arxiv.org/abs/2512.11574v1) | decoder训练混淆encoder固有3D表示；无finetune跨view probe下DINO/VGGT不同条件；不授所有3D-aware encoder胜出。 |
| [EmbodiedComp11612](https://arxiv.org/abs/2512.11612v1) | 图像codec指标不等于闭环VLA任务；低bitrate条件下简单操作失败；需核阈值/任务，非通用bitrate门槛。 |
| [FactorPortrait11645](https://arxiv.org/abs/2512.11645v1) | identity/pose/expression/view纠缠；expression latent与Plücker/normal controls分离；只生成控制机制，非真实物理模型。 |
| [KineMIC11654](https://arxiv.org/abs/2512.11654v1) | T2M目标与kinematic action分类监督不一致；CLIP语义对应引导motion蒸馏；保留生成目标迁移条件，不只HAR分数。 |
| [EditMGT11715](https://arxiv.org/abs/2512.11715v1) | 全局denoise误改非target；multi-layer定位+region-hold token flipping限制；必须测未改区域/错误定位，不授绝对保护。 |
| [Pose11720](https://arxiv.org/abs/2512.11720v1) | music/pose异步和scale不稳；one-hot image/VAE pose表示、共享time index/reference conditioning；codec/时序机制非仅dance应用。 |
| [SVG11749](https://arxiv.org/abs/2512.11749v1) | VFM理解与生成空间脱节；在VFM feature域扩T2I diffusion；分数不证明表示更充分或免费免VAE。 |
| [Fingerprints11771](https://arxiv.org/abs/2512.11771v1) | clean attribution accuracy被当稳健；white/black removal/forgery出现效用稳健性冲突；威胁模型限所列methods/models，不授无方法可用。 |
| [MatAnyone11782](https://arxiv.org/abs/2512.11782v1) | segmentation监督缺boundary且人工matte规模受限；pixelwise learned quality在线监督/离线选择两用；sensor偏差待核，非真值。 |
| [SAM2VideoX11792](https://arxiv.org/abs/2512.11792v1) | 大数据未修structure motion；recurrent tracker双向fusion与Local Gram Flow蒸馏video；不授物理可行或所有运动改善。 |
| [Particulate11798](https://arxiv.org/abs/2512.11798v1) | per-object optimize难scale；单mesh到parts/joints/constraints原生多joint预测；保留结构表示机制，不授生成mesh的真实dynamics。 |
| [V-RGBX11799](https://arxiv.org/abs/2512.11799v1) | intrinsic理解/编辑/生成接口分离；interleaved intrinsic conditioning传播keyframe编辑；一致图像不授现实物理因果。 |
| [GUI-EDA11611](https://arxiv.org/abs/2512.11611v1) | Word/Excel式GUI评价掩盖专业工具动作/推理缺口；2000例、30模型的CAD环境评价显示domain知识限制；保留GUI Agent评测盲区，不采用科学设计结论或未经预算匹配的PhD比较。 |
| [Eik-QRL12046](https://arxiv.org/abs/2512.12046v1) | trajectory数据限制goal-conditioned value学习；Eikonal PDE无轨迹构造与复杂动力学下层次分解；学习目标替代有潜力，不授任意控制可解或物理安全。 |

## Mill差额定点重开：七项

同一原98项有限集合内部改判，没有新增库存。旧理由及实际新依据保留在后文；下列七项均缺first-public，不评分、不授Evidence或Books。

| 精确v1 | 原约束 → 实际增量 → 窄设计判断；复用位置/未授事项 |
| --- | --- |
| [RAST-MoERL13727](https://arxiv.org/abs/2512.13727v1) | 共享encoder与reward固定比例可能失配 → 实际改encoder、稀有/常见expert masking均退化，pool/稀疏度条件对照 → 表示/学习容量选择应核train/test reward失配；Mill §4.2/§5.3–5.5/Table1，不将城市调度类比GPU、不授普遍消除reward hacking。 |
| [EEG-DLite12210](https://arxiv.org/abs/2512.12210v1) | foundation预训练数据/资源约束 → latent压缩/HBOS/k-center选择及不同蒸馏比例 → 数据选择与预训练质量/预算联合核；Mill Method/Algorithm1/Tables1–2，不采医学诊断或“5%通用充分”。 |
| [MRINE12462](https://arxiv.org/abs/2512.12462v1) | 缺模态zero-imputation/noncausal融合 → modality-specific动态缺失预测后因果融合与missing-rate对照 → 缺样条件/动力学假设和表示分开验；Mill §3.2/§4.3–4.4/§5，time-invariant限制，不采脑科学或全模态保证。 |
| [M4Human12378](https://arxiv.org/abs/2512.12378v1) | HAR-only题名判断掩盖实际HMR/表示信息 → RT与CFAR-RPC取舍、split盲区及BEV-RoI到局部3D成本 → 表示/评价split/计算需绑定；Mill §3.2–3.4/§4.1–4.2/§5.1 Tables2–3，不由数据更大或跨模型比较授机制因果。 |
| [EnviroLLM12004](https://arxiv.org/abs/2512.12004v1) | 本地模型只比单项成本或quality → Tables1–3有限质量/资源测量条件 → measurement校准与模型配置选择联合；Mill Method0.5/Results/Limitations，NVML缺失估算power、同家族1B judge未人评，不授平台因果或可靠性。 |
| [DreamRAM12106](https://arxiv.org/abs/2512.12106v1) | memory容量/带宽/功耗不能单独选择 → MAT DLOMAT/3D-HBM空间与ServerGPU iso条件 → 硬件可行性/预测取舍有潜力；Mill III-B/C/IV/IV-C/Appendix，缺LLM trace不自动排除，预测/RowHammer及cell限制不授实机模型或安全。 |
| [Explanation dependency12500](https://arxiv.org/abs/2512.12500v1) | 可读解释被当独立验证 → 另模型给定含错误的诊断后GPT-4V仅生成解释，Study1错误AI下LLM解释相对Basic的准确率退化更大 → 合理化文字不能替代上游判断验证。复用Mill §7实际官方export exact-v1 PDF pp3–4/8/12–13/16/29/51必要协议和反证；最终第二轮Human-First/AI-First准确率无显著差异，两个群体任务不同，不能授expertise纯因果、所有解释有害或专家免疫。必要原文已校准，仅first-public hold，不授临床采用。 |

现84个潜在家族均是日期未授集合，不是本窗新论文/已审阅分母。明确首公开权限缺失后不采用、不进入Books、不支撑覆盖/性能/安全保证；安全隔离不通过Evidence。必要恢复是每家族精确v1个体官方new公告/RSS/email或可核首次正文区间；不能给月ID或Submitted补默认EST时刻。未变化有效题摘复用不等于取得first-public。

## 贡献前关闭

完整题摘明确关闭：[12224](https://arxiv.org/abs/2512.12224v1)是LLM给软件缺陷analytics anonymization参数、IPR/F1领域指标，未建立模型数据/训练或LLM执行新条件；[12326](https://arxiv.org/abs/2512.12326v1)是pentesting58文献归纳，未新增本项目可检验机制/受控反证；[12356](https://arxiv.org/abs/2512.12356v1)是LLM模拟social word-game预测人际兼容；[12371](https://arxiv.org/abs/2512.12371v1)是humanities研究组织方法；[12447](https://arxiv.org/abs/2512.12447v1)两句语言科学立场，无实际新学习/评价机制；[12225](https://arxiv.org/abs/2512.12225v1)是人类认知几何统一框架/psychological simulations，题摘未连接实际模型形成或执行规则；[12389](https://arxiv.org/abs/2512.12389v1)是凝聚态many-body thesis，范围外；[12299](https://arxiv.org/abs/2512.12299v1)是通用edge/fog/cloud服务资源DRL冲突调解，未建立模型workload/platform执行约束。

含糊准入另实际补局部：[AI Transparency Atlas12443](https://arxiv.org/html/2512.12443v1) V-C、VI是三LLM majority vote判documentation completeness和weighted section schema，947命名/披露缺口是inventory；version-aware分析明确future。未给新受控judge效度/错误反证或实际version治理协议，窄关闭，不以consensus授合规或安全。[SafeGen12501](https://arxiv.org/html/2512.12501v1) §3.1–3.3、4.4/Tables6–7、4.5/5，classifier先filter再Hyper-SD，fairness training未给不同于既有两模块微调的具体约束；以F1/FID/SSIM分别映射伦理pillar，manual cases不证明adversarial/公平成立边界。保留这种证据限制，当前未见新增受控反例，不给安全保证，贡献前关闭；不因已有模块组合本身排除。RAN同类组合已因实际检索反向/规范错引证据保留，避免同理由泛关闭。

标题范围外简记仅余：12201文化遗产平台、12240孕产EMR、12320软actuator，明确领域研究/科学应用。未将月列表普通医学/遥感/电路/实时OS/经典分布式ID题名送入贡献队列。

### 原误判与改判依据（不再作为当前关闭理由）

原12106判“通用DRAM、ML仅背景”，原12004判“成熟runtime/judge包装、题摘无反证”，原RAST13727判“交通MDP领域决策”，现均撤销：Mill实际核心分别给出DLOMAT/3D-HBM iso条件、Tables1–3质量/成本和encoder/masking/pool学习条件，不能因无LLM trace或组合成熟关闭。原12210 EEG、12462脑活动、12378 mmwave HAR题名关闭，现分别依据预训练数据选择、缺模态动态融合与实际HMR表示/split恢复；原12500皮肤科标题关闭遗漏错误AI解释诱发依赖的安全信号，现撤销。原标签保留审计，不用于评分、Coverage或Books。

## 已核未来提交下界

精确v1实际版本表：12536 Dec14T03:47:39Z；12548 04:36:06Z；12544 04:28:39Z；12552 04:51:53Z；12508 01:18:48Z，均不早于本窗右端Dec14T01Z。六段补检另定点核12537/12576/12608/12620/12641/12677/12716/12730/12770/12775/12777/12812/12818/12839/12868均Dec14T04:08以后；12967/12976/13059/13063/13109/13070均Dec15；12597/12634/12652/12686/12692/12706/12806/12856/12847均Dec14T08:31以后；12990/13282 Dec15，14151/14256/14322/14661 Dec16。是个体下界，不由编号推定；不否认更早作者原始发布，不授准确归属日，不要求本窗读全文。12501/12503实际Dec14T00:18/00:24仍在可能窗口，已实际读题摘/必要核心，不误排。

## 尚可执行

末批八项完整v1题摘原已实际读完：七项并入潜在集合；[11691](https://arxiv.org/abs/2512.11691v1)是DBNet+++BART及PyQt图库/live四类识别，TotalText十小时训练94.62指标未新增模型学习、执行边界或受控评价反证，贡献前关闭，不按软件实现本身排除。本次七项重开后，同一98项集合为84个唯一potential、11项完整题摘/必要局部关闭、3项标题范围外。12500必要原文已复用Mill §7–8实际校准，旧正文不可得请求撤销；其v1 Submitted原值`2025-12-14T00:06:06Z`不是公开依据。84项仅first-public继续隔离，不是Evidence/Coverage通过；作者普通修复0，交Mill局部核，不自行授日级完成。
