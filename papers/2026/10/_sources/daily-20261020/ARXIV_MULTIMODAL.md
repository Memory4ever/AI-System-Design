# Multimodal slice — Daily 2026-10-20

作者：oct20_author_resume；独立复核：待root。只own本文与mm_assets，不写Books/LS/其他ARXIV分工。窗口为北京时间2026-10-19自然日，公开日依据复用同日本源公告段及root已完成AB校准，v1 submitted日期不改名为公告日。新抓取精确v1 HTML、请求与可读提取见`mm_assets/html_<id>.*`；下载全文不等于全文都审阅。以下仅列实际读段和拟采用边界；作者未复现、未运行artifact、未核图像像素。Score为原文新增命题，不给成熟原则加分。

## 1. 已完成必要核心，待非作者证据/Books复核

### 2610.23854 MFlow

- 身份：[Rethinking the design space of Vanilla Pixel Diffusion Transformers v1](https://arxiv.org/html/2610.23854v1)。根任务校准准入；2+1+2=5，标准所需核心完成并为具体Books差额加读，不能从“已校准”推证据通过。
- 实读：§3.1–3.3/式1–7（本地行153–273）、§4.1–4.2/Table1、§5/Table2–3、MFlow/ConvRefiner ablation与§6（行545–572）、A.8（1583–1612）。
- 原约束→增量→选择：大patch pixel预测的clean/velocity压力不同，硬PCA rank要额外扫参→固定PCA基下每方向`m_i∈[0,1]`学习混合、用`[(1-t)I+tM]^{-1}`恢复velocity并仍在velocity空间训练→预测参数化可从硬子空间改成方向级软分配，而非换掉概率路径。`t=0`noise、`t=1`data；严格可逆仅`t<1`，不能把原文“always exact”推广到`t=1,m_i=0`。
- 核心反侧：Table2无LPIPS MFlow3.74差于JiT3.70/Asym3.59；有LPIPS3.33。H-level Table3 Asym1.79仍优于MFlow1.81；低训练loss未持续改善FID（A.8）。直接在graded target训练造成m向clean的平凡激励（3.66→4.88），所以不是随意选择loss空间。容量/模态的M曲线是有限实证，不是普遍容量定理。
- 第二分支：JiT大patch频谱缺口并非所有pixel/latent模型共有；冻结骨干加4-block ConvRefiner/近clean GAN补高频。Table1 ImageNet256、H/16、FID50k1.81保持，HF deficit−6.63→−1.29dB；额外5%普通训练不能同样修复，refiner无GAN效果较弱，DiP detailer能过冲且FID退步。频谱接近不证明真实纹理/感知更好，A.8要求人审等互补评价。
- 条件/费用：ImageNet256固定backbone重新训练与per-model sampler调参；T2I900M预训练/33.5M SFT为私有数据，不能外推公平普遍排名。PCA、gain训练、调参、LPIPS/GAN、refiner与全部采样付费；未核全部Appendix配置，硬件/精度/完整wall-clock为本次未核，不发布加速百分比。
- 具体Books建议：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24当前约481–485已有image-like输出/velocity loss与AsymFlow硬正交子空间及低噪clamp边界；还没有**软M非projector、方向级gain、moving target/velocity-loss防平凡解**。建议原AsymFlow后窄增一段保硬rank仍合理；ConvRefiner只附频谱/FID分验反侧，不扩独立章节。root审后决定，不先称整合完成。

### 2610.23795 PPMem

- 身份：[Persistent Planar Memory for Video World Models v1](https://arxiv.org/html/2610.23795v1)，2+2+2=6；标准必要范围完成，因具体representation/writer差额补读消融。
- 实读：§3.1–3.3（约125–222），§4.1–4.4/Table2–5（223–458），§5限制。Wan2.2 TI2V5B；25-frame chunks，DL3DV/RE10K80k+clips，主评100+100 scenes，ablation56室内scenes。
- 增量：无显式persistent geometry或逐像素点云增长→7参数plane primitive的变长global pool，每chunk内部预测geometry；multi-camera occlusion删旧、quality去重、基于已提供下一chunk camera pose预删待替换plane；render depth/RGB/mask回馈下一chunk。固定backbone视频pass与LoRA geometry额外pass分离，不是所有denoise都联合优化video/depth。
- 对照/边界：Table3同checkpoint inference替换，无memory/外部MoGe点云/posthoc Plana3R对照，joint plane pool δ1.25 70.3 vs64/55/57，支持本模型里memory/内部预测差额，不独占表征唯一原因。Table4 concat-only δ72.3**高于**DTF70.3，主要收益是depth存在；DTF新增证据是输入scale probe的faithfulness，不是所有指标胜出。Table5删normal导致all-zero深度，说明7参数耦合依赖；有机水/植被、未见极端camera和dynamic plane为限制/未来工作。
- 数字约束：100k primitives/5MB在约400frames场景，不是常量memory；相对210M densePC的3数量级是理论逐像素全累积估计，不能写所有生产点云压缩1000倍。各baseline native resolution/base model不同，Table2全系统排名不纯归因plane。额外geometry pass、render、pool维护、深度伪标及两阶段训练全部付费，未核wall-clock/precision，不报实时。
- Books建议：`MULTIMODAL-WORLD-MODELS` Ch25“Persistent world state”现有点云/TSDF生成几何循环与约611行固定六feature planes的constant-storage/coarsening；缺**变长plane primitives pool与局部删除/质量替换/下一已知pose预删**分支。建议fixed-feature-plane段后加一组对比，强调plane pool不是那种固定张量、static structured scene prior与derived geometry非真实world state。待root独核/实际写后。

### 2610.23542 MIST / M3-Agent

- 身份：[Execution Before Memory: Diagnosing Memory Failures in Video World Models v1](https://arxiv.org/html/2610.23542v1)，3+2+3=8，深入必要证据完成。
- 实读：§3/式1–2、§4/Table2–3、§5/式3、§6–7/Table4–6、§8具体反证与scope（本地190–760）。
- 增量：memory总分低可来自未执行reveal而非遗忘→setup/leak/action/reveal/inside分别判，冻结前两shot只重生末shot；43个paired baseline有41 never-open→持久性尚未被测，不能把总分解释成backbone忘记。三shot Wan TI2V5B与packed15s MiniMaxH3的failure人口不同（后者更多open-wrong），不能混表。
- 干预证据：Table2 one-kept/43非best5，setup0.852→0.851、reveal0.147→0.492、never-open41→20、correct1→13，仍10open-wrong；paired mean提升0.34 CI0.24–0.45。Table3 equal5 tries包含target answer的same-sentence resample，不能称target-free；去target rewrite只0.174且28/43仍closed。
- 关键反证：M3使用**报告同一scorer做oracle keep-best**，不是可部署独立critic；原candidate保留，revision可破坏correct。MBench固定leave-return0.251低于base0.292、keep-best0.446且双指标各pick，oneclip per item0.443；WRBench T0.452→0.570多来自departure/return gates而非画质，不由成分相关推出因果。Heldout8B reader非人审，不替official scorer；无score lastframe reader不胜baseline。§8明确不证明backbone存了target；需target-blind selector、heldout cases和human labels。
- 费用：每组多次视频采样、VLM诊断、prompt重写和scorer均付费；模型/clip length/seeds/预算各protocol分列，未读取所有Appendix预算不能拼全系统成本。未复现、不授生产部署。
- Books建议：`MULTIMODAL-WORLD-MODELS` Ch25“Evaluation：从画面质量到干预结果”/“视觉连贯不证明不可见状态”有一般诊断，但需增**先证执行揭示操作成立、再问persistence；oracle选择/target可见性不可当memory修复**。拟窄增一段，保完整43分母、分层gate与反证；与Ch66交接，不重复ownership。

### 2610.23531 PONDER

- 身份：[PONDER: Learning to Generate in the Right Order v1](https://arxiv.org/html/2610.23531v1)，2+1+2=5；标准核心/必要具体差额完成。
- 实读：§3.1–3.5/式1–7（约100–230）、§4/Table1–4及§5限制（391–395）。
- 增量：冻结masked continuous-token generator，policy读本轮固定backbone features/初始noise按预定K选位置，允许visible patch重新mask，未来轮新context再生成。每轮内部先后决策只通过candidate mask相互影响，不重新计算backbone；R removals需N+R fills、共N+2R位置决策，不能说revision无计算开销。
- 优化/对照：同canvas同generator noise的group只变order，terminal reward作group-relative单次onpolicy更新，无PPO clip/ratio/reference KL。FIDgrad是SPD covariance假设下Gaussian plug-in FID的influence derivative，EMA moments近似，不是单图真实质量oracle。Sudoku冻结generator、同R9 learned removals96.7hard vs random removals62.7，支持where revise局部作用；ImageNet同R32 learned2.70 FID vs random-removal2.76，增量远小于order主效应。额外FDr5不含Inception缓解同reward单指标但不证明无reward hacking。
- 限制：policy每generation iteration额外forward；generator denoise内循环与position外循环不能混NFE。R预定且必须耗尽，没学何时停；延长预算不证明任意prompt持续改善或净延迟下降，reward依赖与RL采样成本保留。
- Books建议：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 Masked已有约798行**冻结predictor、选可见集合、remask、比例schedule**（2610.22099）。单“可撤回顺序”已覆盖；真实差额在**连续image latent、终态FID一阶population reward、固定R动作会计/无自适应stop**。建议补一个短的FIDgrad/revision预算段或仅报告；请root据现有段定窄差额，不重复重写remask原则。

### 2610.23423 Momentum

- 身份：[Momentum: Persistent Dynamics for Video World Models v1](https://arxiv.org/html/2610.23423v1)，2+2+2=6，必要核心完成。实读§3.1–3.4.2（120–169），§4/Table2与Table4（393–470），A.2配置定位与camera/SCS评价定义（770–820）。
- 增量：离屏状态随观察者轨迹停更→global time-indexed8camera rigs为world state；WorldUpdate按rig graph BFS由最近已生成邻居重投影，同深度可并行更新同步reference videos；WorldInteract读时间对齐refvideo生成target trajectory，同world rollout可供多target复用。无实体追踪，固定rig workload不随实体数增长，不等无rig/rollout成本或真实动力学。
- 对照：CARLA六城、seen/unseen各30测试session、300frames10fps；25m外不活跃rig复制末帧且不作reprojection source。Table2 GTreference只隔离interact；Table4 generatedreference才是端到端，unseen SCSdyn .084→.190（相对+126.2%）支持受限动态一致性；seen translation .060→.080反退、rotation .026持平。graph/multirig对照主要定性，不能独占因果或称等完整预算。
- 指标与费用：SCSdyn是SAM3.1车辆/人/自行车/动物类别union的IoU、2fps抽帧、双空剔除，不是instance identity/物理守恒；camera error为DA3估计、32framechunk、translation各maxnorm归一，非绝对metric pose。8H100、704×1280、WorldInteract77frames/H5/35ODEstep/CFG3只约束披露配置。rig视频、geometry/reprojection、graph依赖、target generation与训练全部付费。
- Books建议：Ch25约609已有LiveWorld离屏monitor动态分支；不可重加“离屏持续动态”。实际差额是**多rig同步/图依赖、与target解耦的world rollout多observer复用**，建议紧接LiveWorld加一段并保有限静态camera network/生成world非真值及双阶段完整费用。待root独核。

### 2610.23324 CatchUp

- 身份：[CatchUp v1](https://arxiv.org/html/2610.23324v1)，2+2+2=6，必要核心完成。实读§3.2 oracle诊断（232–290）、§4.1–4.3/式与runtime顺序（291–399）、§5.1配置（400–419）、§5.3–5.4/Table4–6（788–892）。
- 增量：monotonic pruning不能在深层找回早期少算证据，直接重入又携带旧depth状态→2/7/15/23层重新按当前textquery/旧visualkey选同预算集合，保留所有原visual的deferred状态与depth；选定重入后，用持续active anchors在对应旧depth到当前depth的残差，按旧feature cosine与spatial distance加权，修正重入状态。选择发生在修正前，不能称LTC改善同轮selection；无anchor时跳过修正。
- 证据/反侧：LLaVA1.5-7B576tokens、64/128/192预算；fixedroute/budget的dense fulltrajectory **oracle替换仅诊断**RefCOCO18.96→23.18，非部署。Table5 monotonic/stale/LTC Ref15.78/18.96/21.26，但stale POPE74.92低于monotonic75.81；LTC76.62。Table6空间only Ref21.39高于combined21.26，混合策略并非全指标最好。路由与dense overlap/recall仍不完美，不授精确恢复。
- 成本：Table4无LTC2.131TFLOP/1589.28ms/0snapshot，LTC2.194/1611.17ms/22.5MB；+2.96%prefill、+1.38%E2E换Ref+2.3pt。图6 matchedprefill约1%内比较；89%少active visual tokens只约8%E2E收益，不是8倍全链加速。snapshot不同于KV；全部状态、allcandidate评分、snapshot与anchor修正计费。硬件/推理precision/batch/outputlength本次未找到，不授SLO。
- Books建议：Ch23约1148–1166已覆盖“停止更新但仍可读KV”及decode-stage可恢复备用集合；缺**prefill跨depth重入、depth-tagged快照与共同anchor残差转移**，不是泛称recoverable token。建议在freeze/read-path与decode备用集合附近窄补这一分支，明确文本decode重选与层间重入是两种时钟；Ch45只交接存储生命周期。

### 2610.23263 SCALE

- 身份：[SCALE v1](https://arxiv.org/html/2610.23263v1)，2+2+2=6，必要核心完成。实读§4.1–4.4/式7–16/Algo1（约170–329）、§5.1–5.3/Table2–7（329–615）、E配置/额外training成本及I限制（1328–1368、1482–1495）。未逐条验证附录proof。
- 增量：CFG guidance-free training只学条件/无条件差→把真实noisy sample与模型估clean再同level加噪的selfreference差也折入训练目标；α控制SCG、β控制CFG，嵌套两层interpolation训练后一个forward输出，而非推理时另造real reference。PatchMix以λ.2的patch替换使reference靠近real支持；stopgrad α1参照只在**本update**无环，同网络α1切片仍随训练更新，不是冻结teacher。
- 理论/对照：unlimitedcapacity/data且base在real和reference都匹配datascore的idealoptimum才给条件期望SCG，不证明有限模型回真实manifold。Table4 DiT50DPMsolver NFE100→50/FID2.17→1.87；LlamaGen NFE512→256/FID3.07→2.58但IS256→253反退。T5scratch9.04→8.75、T6linear8.67 vsPatch8.60是有限差额；T7λ.5/.2同FID2.58，IS不同，不能称任意更强SCG单调改善。
- 成本/限制：DiTXL2/LlamaGenL ImageNet256、SD1.5 512/LAIONAesthetic5+、finetune<5%pretrainbudget；SD1.5从GFT权重再训LoRA，非原权重无适配。两额外nograd分支仍付费，Table1训练/step相对CFG1.12 vsGFT1.06；NFE一半不等全链wallclock一半。离支持远、低α可失败；更大flow模型、RL兼容/安全用途为未验未来工作，DPO补充实验不是安全保证。
- Books建议：Ch24约2059–2089实际已有内部depth差单forward guidance与condition prior steering，不能用“省CFG双forward”单独加分。实际差额是**real/self-generated支持对比、训练期PatchMix/stopgrad本update参照、双αβ内化guidance**，建议置于singleforward guidance分支后，保原CFG与有限支持假设/训练成本；不独开模型名章节。

### 2610.22975 Sink-Sparse Hybrid Attention

- 身份：[Sink-Sparse Hybrid Attention v1](https://arxiv.org/html/2610.22975v1)，2+1+2=5，标准必要核心完成。实读§3–4/式1–7/Algo1–2（70–276），§5.1–5.5/Table1–4及直接限制（277–560）。
- 增量：训练后DiT可用layer/head稳定高attentionmass少算，但静态稀疏丢弱全局context→4prompts×2seeds离线聚合全denoisesteps、逐row取达到τ质量的最短blockprefix，之后按原tokenorder复用静态mask；另以fullQ读取meanpooledKV，并按两branch logsumexp、poolsize `+log(g)`自适应混合。不是因果LLM开头sink，不改weights/schedule。
- 精确性边界：pooled branch是**全support粗摘要**而非严格不相交的omitted complement，因此有重叠；logsumexp融合与g30校正不使pool后的权重/输出等于dense softmax。mask只在calibration经验mass下选，不保证新prompt所有步骤都保τ。成本仍二次阶，近似系数ρ+1/g；主branch sparsity不含comp成本。
- 对照/反侧：单A800SXM4-80GB，共同FlashAttention/QKnorm/RoPE stack；Wan2.1T2V1.3B832×480/81frames/50steps、τ.85 dense164.80s→106.73s=1.54×，VBench8dim均值.656→.659，但subject/background/aesthetic等仍降；τ.7更快1.74×而均值.647低于dense。ZImageTurbo2048²/8steps23.39→14.88s=1.57×、SoftTIFA GM16.38→15.21反退，不能称无损。计时不含init/outputwrite，推理precision/batch未核。
- 消融/费用：Table4 τ.7 sinkonly87.22s/.581→hybrid94.57s/.647，τ.85收益仅+.006；τ更高不单调。默认离线8条完整dense trajectory约22min为**估算**，扩大4×4约43.9min/.650、8×4约87.9min/.649不单调。模型特定mask、pool/fusion及校准费用全保留；分布漂移/稀有依赖会漏，跨backbone转移未验。
- Books建议：Ch24约1054已有训练内生persistent/local同softmax与coarsepool提名，1361已有block首步探测复用mask；本篇差额是**模型特定跨trajectory离线静态mask＋全局pooledKV双branch归一融合**，不冒充前述训练内生history或exact并集softmax。建议有限加速分支一段，保重叠/近似、校准摊销及质量反退。

### 2610.22957 QART

- 身份：[QART v1](https://arxiv.org/html/2610.22957v1)，2+2+2=6，必要核心完成。实读§3.1–3.4/式1–7（110–164）、§4.1–4.7/Table1–2（165–409）、A.2数据/slot与training/projector（892–1000）、C.4直接限制（1336–1350）。
- 增量：固定queryagnostic encoder/固定token数把“保什么/花多少”混为一事→冻结SigLIP2图文encoder，query预测patch support；2起始slots、shared recurrentTransformer持续汇聚所选patch/text，shareddecoder重构全grid但只在querysupport评coverage，grow<.85每次+6、halt≥.95（δ.30），最多32slots/6rounds。仅slotstates跨轮；growth停止而existing slots仍可refine，非一次prune。
- 关键对照：同checkpoint固定K2 VQAv246.27→50.93（1→3rounds），支持recurrence独立于growth。CORE Table2 querysupport/budget二开92.01%/17.25slots/4.25rounds；仅support开92.08/32/6，support也关79.7/32/6，分离定向表征与预算两职责。VQAv276.37保dense81.4的93.8%，~29tokens/24.8×少tokens，仍低于dense；跨原backbone的pruner不作公平绝对排名。Winoground fixedquery会降，PODS粗query仍有细粒度，均有限任务不是语义充分性证书。
- 成本反侧：§4.6 batch1 **0.87×E2E变慢**，batch4 1.14×/1.84×prefill，batch8 1.53×/2.54×与21→32.2samples/s；20–25×token减少不能替净加速。384²/729patch FP16预缓存训练、BF16B256训练配置不等推理precision；计时GPU/完整cache边界本次未找到，不授SLO或真实在线总价。dense queryregion标注训练、relevance/recurrence/每轮decoder、projector两阶段适配均付费；slotcount离散惩罚不经allocation传梯度，非已学optimalhalt。
- 限制/Books：singleimage、阈值跨任务需调、region监督仍需；新query要重新构造，不能假定原tokens为queryagnostic永久缓存。Ch23约1022–1066已有内容/任务预算、约1110已有query-conditioned fixedbudget选择与局部/global两预算；缺**querysupport重构coverage分别控制grow/halt且可仅refine不grow**。建议唯一owner `MULTIMODAL-REPRESENTATION` Ch23预算段窄补，不把reconstruction通过升级下游理解通过。

### 2610.22499 JAVIS

- 身份：[JAVIS: Joint Audio-Visual Interaction and Streaming for Real-Time Conversational Agents v1](https://arxiv.org/html/2610.22499v1)，2+1+2=5，标准必要核心完成。实读§2.1–2.3/式1（86–214）、§3.1–3.4/Table1–5（215–373）、§4 futurework。
- 增量：speech→face级联等待/丢context→冻结FAC sharedLLM，LoRA JointRefinedHead的同组hidden供speech token与20维FLOATmotion coefficient两个decoder；LLM5Hz展开为25Hz、5frames=.2s，motion读取当前H及下一chunk H、上一motion和portraitstate。无waveformdecode/reencode瓶颈，但**一chunklookahead需等待未来H**，不是零等待或full-duplex。8layer1024motiontransformer、10Eulersteps、frozenCosyVoice3 decoder/vocoder与FLOAT renderer均仍执行。
- 对照：140未见VStyle样本，LSE-C9.59与FACInfiniteTalk持平、LSE-D6.74略优6.86；IQ.744弱于.754，speechWER.44弱于.31/.41，不称全项优。26raters/30queries的表达适配3.76±.16 vs3.44±.14支持局部human偏好，motion3.92±.13未胜4.02±.11。Table5去lookahead LSE-C9.59→8.80，但WER.44→.37/UTMOS4.29→4.31反向更好；未有隔离共享head vs等预算独立head的完备因果对照。
- 成本/速度分母：2×RTX4090、5queries均值，首包定义**音和视频都可用**，1.27s/RTF.541/12.1soutput；约200×只对FACInfiniteTalk252s，不对同样分块FLOAT2.09s/RTF.560/11.8s（仅首包−39%），也不是任意线上200×。940497monologueclips后716565dialogsamples、B8/AdamW1e-4；334.13h JAVIS-Syn为合成、SyncNetlipfilter，数据承诺acceptance后发布不等已开放。合成API/portrait、过滤、两stage、speech/motion/render/传输全付费；未核推理precision/concurrency/p99。
- Books建议：Ch24约1503–1539 typed统一输出已有decoder/类型合同，Ch23约1778–1828已有多时钟/可打断状态原则；差额是**共享speech refined hidden双decoder、motion低维chunk与一chunklookahead等待**。建议Ch24 specialist→typed分支窄补，引用Ch23时间合同不复制。未来full-duplex/listening不能写已支持。

## 2. Xiaomi-Lens-0 定点准入核查

### 2610.23279 Xiaomi-Lens-0

- [exact-v1](https://arxiv.org/html/2610.23279v1)首次timeout，经一次有限重试200恢复；实读§2.2.1–2.4/式2–8（154–194）及§4.4/Table8–9（1268–1350）。不是仅因“mask+latent模块组合”准入：存在明确共享参数监督/消费接口与同Stage2数据、关闭maskloss的对照，建议2+1+2=5，标准必要核心完成，**待root独立确认准入**；不混进根任务原已校准10项。
- 具体接口：pre-mergerpatchgrid生成一次F供多maskqueries复用，LM `<|mask|>`上下文state作动态classifier，maskloss同时回vision与LM两路；jointstage之前先冻结backbone训decoder。新增的groundedCoT只监督文字所提region的范围。**推理mask是输出旁支，后续文字仍只读image与此前tokens，没有crop/regionfeature回灌**；不能从inspectablemask称新增观察、真正用mask进行闭环思考或视觉因果证明。
- 对照范围：bboxonly已带来多数REC/感知收益；Table8同Stage2数据加maskloss只再增REC1.1–2.4点、perception.2–1.4点。Table9 groundedreasoning新数据仅再增REC.1–.6、RES.5–.8，不等单独识别CoTlatent唯一原因或全问题推理变强。此核查不采整套benchmark最好/5.6汇总或部署速度；premerger特征驻留、decoder/多mask、grounding与trace标注、两阶段训练均付费。原文残差/互信息恢复动机不作为严格信息无损结论。
- Books定点建议：Ch23现有约101行densehead读浅/深层以及已存在grounding/主动crop分支，需对照的差额是**同共享premergergrid、masktokenstate双参数路由监督，且输出mask不回馈语言**。建议仅在sharedencoder→denseoutput邻接补这一边界或NC；不因已有Principle删掉来源准入。现阶段无Books写入。

## 3. 独立复核与交接

未由作者自签。原10项必要证据均完成作者阅读，23279有限定点核查后建议5分、待root独立准入；Books建议是具体delta候选而非已实施/已验收。root可按现有条目并行独核，不等其他来源完成；Books实际写入仍由root协调。机器/全文下载不代替语义审阅，作者未运行artifact、复现、验证全部图像/附件或全proof，不授整日通过。

## 4. 当前 Books 实读比较与最小差额交接（未写 Books）

root 调整分工后，`oct20_author_resume` 实际读当前 Ch23/24/25 的下列具体正文与局部邻接；只准备 Books 判断，不重 Source、不写 MM Books。这里的 reader 仍是本文件 Source 作者，不能据此签独立 Source 通过；root 的必要 Source 独核另行完成。节点来自当前 ROADMAP：Ch23=`MULTIMODAL-REPRESENTATION`，Ch24=`MULTIMODAL-GENERATIVE-PARADIGMS`，Ch25=`MULTIMODAL-WORLD-MODELS`。行号是此次实际读取版本，可由段首与 SF marker 稳定定位。

| Family | 实际当前覆盖 | 最小 Books 决定建议及边界 |
|---|---|---|
| 23854 MFlow | Ch24:481/483 已分输出参数化与 velocity-space loss，485 AsymFlow 已有正交低秩 noise/补空间 clean 与 clamp/费用。实读476–492。 | 窄增于485后：硬 projector/rank 与非 projector 的方向级软 gain 是两种选择；后者须在 velocity 空间监督以免 moving target 平凡偏 clean，并保 `t<1` 可逆边界、LPIPS/排名反侧。ConvRefiner 不另开支，仅为频谱/FID/感知不可互代的报告证据。不是重新解释 image-like head。 |
| 23795 PPMem | Ch25:613/615/617 已有固定六 feature planes、bounds warp/coarsening 和 constant storage≠constant resolution；609 为动态 monitor。实读594–634。 | 固定 plane 张量后窄增对比分支：变长 plane primitive pool，以 occlusion/quality/下一已知 pose 删除或替换，render 几何再反馈；保 pool 随场景长、static structured scene prior、geometry pass 与 render 全费。不是“plane memory”同名替换，不采1000倍生产压缩/实时。 |
| 23542 MIST | Ch25:619后区分视觉连贯与不可见状态；991–1010 将预测误差升级为 predicates/admission，但未在这两处拆 reveal 是否真正执行与揭示后 persistence。 | 窄增于评价开头：先固定 setup 并验证 action/reveal gates，未打开者不进入“已测遗忘”解释；target 可见改写、同 scorer oracle keep-best 与更多采样的成本/选择偏差不得冒充 memory 修复。保43完整配对人口、残余 open-wrong 与闭环未证。无需复制 Ch66 一般评价合同。 |
| 23531 PONDER | Ch24:820 已冻结 predictor、policy 选下一轮可见集合并 remask、独立比例控制、固定 horizon 不授提前 commit；816/818 与822/824/826邻接实读。 | 泛化“学习顺序/可撤回”具体 NC，已覆盖；若采用仅补一个训练反馈分支：连续 image 用终态 population-FID 一阶 plug-in/EMA 代理训练位置 policy，固定 R 要付 N+R fills/N+2R decisions、没有学停。不得再写一组 remask 原则，亦不把 FIDgrad 当单图质量真值。 |
| 23423 Momentum | Ch25:609 LiveWorld 已有离屏 monitor 的全局时间补齐、投影和 imagined≠observation；611递归地图另分自身/对象动态。 | 只补在609后：同步多 rig 以图依赖推进 world rollout，再由 time-aligned reference 支持不同 target observer 复用，区别于跟着单个观察轨迹续写。保8-rig支持、远处inactive复制、generated-vs-GT references、非 instance/物理真值及两阶段全费。不重加“离屏动态持续”。 |
| 23324 CatchUp | Ch23:1150/1152 已冻结视觉更新而保读 K/V；1161/1163 是 decode 重选备用集合；1034也已有相同 decode 接口。实读1106–1172。 | 只补 prefill 的层深时钟：保全候选 depth-tagged snapshots，重入集合先按旧状态选，再用共同 active anchors 的跨 depth 残差近似修正；与 decode token-time 回读不同。保无 anchors 不修正、非 oracle exact、状态驻留和1611.17vs1589.28ms反侧，不能按89%少 tokens 报全链倍率。 |
| 23263 SCALE | Ch24:2073/2075 是内部 depth readout 差的 single-forward guidance；2079/2081 是 prior steering，二者均非 real/self-generated 支持对比。实读2055–2093。 | 内部 depth guidance 后、prior 小节前窄补：训练期把真实 noisy 与同噪级 self-reference 差、条件/无条件差共同内化，PatchMix 改 reference 支持，stopgrad 仅当前 update。保理想 optimum/离支持失败、额外 no-grad 与适配费用、NFE非完整墙钟。不能只写“省CFG双forward”。 |
| 22975 SinkSparse | Ch24:1054/1056 是训练内生 persistent/local 同一 masked softmax、coarsepool只提名；1361/1363 是每 block 首步 dense probe 后复用索引。两处完整段已读。 | 原生稀疏之后窄补训练后模型特定跨 trajectory 静态 mask、全支持 mean-pooled KV 双 branch logsumexp 融合；全 support 有重叠，`+log(g)`不授 dense exactness。保校准摊销、近似二次项、分项质量反退与分布漂移回 dense。不是 LLM 开头 sink，也非并集精确 softmax。 |
| 22957 QART | Ch23:1022后已分 relevance/coverage与selector/预算责任；1048有前景/context两预算，1050/1052 image-only可复用压缩，1109/1111是名词引导残差几何覆盖。实读1022–1068/1106–1172。 | 只补 query-support 重构 coverage 控制 recurrent slots 的 grow/halt、可停 growth 而继续 refine。coverage 是 querysupport下的重构代理，不是 downstream理解证书；新 query 须重建，不继承 image-only永久cache。保 region监督/适配、阈值、全 decoder费用，batch1变慢与batch8受限收益。 |
| 22499 JAVIS | Ch24:1503–1539 已分 specialist/typed generator/decoder；Ch23:1778–1829 已分多时钟、arrived prefix与commit/cancel。这些不说明同份 speech refined hidden 如何并供 motion decoder。 | Ch24 specialist→typed 邻接仅一段联合消费者分支：共享 speech hidden 与低维 motion chunk 双 decoder，motion等一chunk未来 hidden，不能称零等待/全双工。保专用 codec/renderer、首包音视频同时可用、2.09→1.27s的正确同类分母与有限偏好/质量反侧；引用 Ch23时间owner、不复制runtime规则。 |
| 23279 Xiaomi-Lens-0 | Ch23:101已有浅视觉层/LM末层图像位置→dense geometry head与先训head再适配主干；1169/1171是另一个真 crop acquisition接口。实读72–128/1161–1172。 | 如root独核准入后，仅在dense head后补共享 pre-merger grid供多mask query、上下文mask state作动态读出及maskloss同时进入vision/LM两路；推理mask输出不回馈后续文字，不能借 inspectable mask 升格主动观察/视觉因果。保同Stage2关maskloss差额有限、bbox贡献/新trace数据混杂和全部费用。不是把“mask+latent”模块名当机制。 |

以上为具体 owner 的窄差额判断，不是全章穷尽搜索或实施验收。可用一个自然段将机制与直接反侧/费用连起来，不按论文名新增小节。PONDER 泛化机制明确 NC，其余也只准上述限定差额；是否写这些窄段由 root 结合独立 Source 结果决定。本支到此保存并停止，未修改 Ch23/24/25、LS 或索引；RO四项另见 RO_REVIEW.md 已真实非 writer POST 的记录，不能借用来给 MM 自签。
