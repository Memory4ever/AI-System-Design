# Writer必要证据与采用边界

后到R24采用校正（优先于下方初读文字）：22026 LN-Scaling方程Var/t与随文exponential不合，不采用其速率结论；原Pre/Post受限几何解释保留。22042不是已证单层干预，而是每emotion按AUROC选所有合格layers/sublayers、独立module作用于selected layers，仍不授主观体验/全局保义。22210语言服务diagnostics不需编译执行，§8已用Pit/MutPy做有限mutation score；只能说它不证明需求/测试oracle正确，不能说完全没测断言有效性。writer已读R24具体原件位置与论证，采纳这些纠正，不重首必要。

## 后到首必要实读（writer保留组）

### 22332 v1

实读§3/3.1、§4.1–4.2、§5.1–5.2、§6–7：原生FF key激活/value向量加TopK，本来就能作为SAE的同对象特征基线；Gemma2/9B、Llama8B、GPT2/Pythia70M多层与随机初始化对照，主要解释中层。SAE宽度16k/32k和TopK10不是任意容量比较。单人annotation能凭振幅/方差猜组别，TopK处理后优势收窄，不能把可辨认artifact叫解释更真实。Proxy-feature oversplit/不对应原FF不证明SAE无用或已识别完整因果功能。采用“解释器须对原生representation及幅度控制比较”的受限反侧；2+2+2=6，WORLDVIEW-REPRESENTATION。

### 22366 v1

实读§3.1–3.3/3.5–3.6、§4.1及§5：tail-truncated orthogonal noise分两通道，masterkey引出16bit sessionkey再绑定256bitpayload；DDIM10 inversion/emptyCFG1检测。SD2.1、CFG7.5/50steps/512²、RTXA6000/PyTorch2.4.1；500攻击图不足实测认证1e-6 FPR，1000prompts*10质量试验的无显著差异不等分布相等。九类常规失真不覆盖adaptive forgery，作者明确承认proxy-inversion伪造、新sessionkey能量异常与可逆ODE限制。仅采用水印可检测性、样本分布及归属威胁分责，不授版权/账号责任证明；2+2+2=6，安全必要已深入，PLATFORM-SECURITY。

### 22467 v1

实读§3.1/Eqs1–3/Alg1、§3.2Theorem1、§4setup及4.2–4.3。低秩J≈UV'使backward近似，但更新仍使用fullparam residual；Alg1 `r_next=r+(g-gtilde)`而下一步又`gtilde+r`，没有标准error-feedback对已消费residual的扣除/重置，常数近似误差可持续累积偏置；丢弃activation后精确g如何得出亦未说明。只给L-smooth/boundedvariance与误差常数项的凸式结论，不能授一般非凸unbiased/convergence。Qwen1.5MoEA2.7B/Dolly15k单H80080GB，precision/B/L/optimizerstate或offload未清，50%峰值省存不能独立对账。中心精确recipe暂不采用，待reader定点核算法是否另有解释；不是因没复现而H。2+2+2=6不降分，TRAIN-PRETRAINING。

### 22475 v1

实读§3.1–3.2、§4setup、§5.3及§7。同一generatedprefix并行persona/neutral路径，confidence取各分布maxprob，divergence实际是maxprob偏离均值，不是token-distribution agreement；相同confidence仍可押相反token。权重lambda-d可负，logit相加亦改变有效temperature，不叫convex consensus。七个1–8B模型的算术/CSQA，身份扰动未必语义不变；随机persona80.3与82.1、同路径退化等消融支持局部多条件计算，不证互补知识/公平性根因。n+1完整logit/KV前向不是免费协作，未严配所有budget。2+2+2=6，MODEL-SAMPLING；并非独立多agent状态通信。

### 22489 v1

实读§II-B/Eqs13–21、§III-B/C、TableI及§IV-C。按general/task activation norm差分成exclusive/shared channel，shared混合两套Wanda分数；这是启发式domain重权，不是证明语义子空间可精确拆开。正文首次task-only不等式与shared重叠，但紧随intuitive定义明确task-only应低于-alpha，可按有条件解释，不把一次排印升级整篇H。Loss union直接拆三期望未带质量权重、shared分数“两倍”也非任意数据恒等。Qwen3-32B、50/75/90%及2:4/4:8、128校准样本/alpha搜索，在MedQA等仅作通用task-calibration测试，不开展医疗应用；不报告未测kernel加速。alpha极限解释相反亦只采用局部结果。2+1+2=5，INFER-TENSORRT-LLM量化/剪枝校准选择。

### 22543 v1

实读§3.1/3.2 Eq6–8、§4.1–4.2、4.4及AppendixD。FAPO把final-answer positive再分first-error过程标签，以GenRM给positive额外-lambda，组内优势使早期/后期权重随正负人口变；不是硬删除所有中途错误或已证内部因果faithfulness。Qwen3-32B自动标FAPO-Critic85K→Qwen3-4B GenRM；ProcessBench派生集的judgeprecision/recall及reasoning收益分开，critic真值仍依赖标注。Qwen2.5Math7B/32B、verl/GRPO有既有cliphigher等，异步reward服务并不证明fullyasync训练兼容，作者承认未定；self-correction缩短不等普遍应惩罚可恢复探索。2+2+2=6，TRAIN-GRPO具体reward/样本人口，而非通用PRM新真值。

### 22556 v1

实读§III-A–C/Algs1–2/Eqs9–13、§IV-A/D/E/F。标点分段、近期8token不压，segment调分后globalTopB给每段隐式budget，再从大到小找保留score比例>=tau的块；超额最后块仍token级裁剪。score比例是proxy而非语义保真定理，标点也非真实语义边界。Llama3.1-8B/Mistral7Bv0.3、LongBench16任务与NIAH；资源测单A10080GB/FA2、budget1024、无batch顺序decode，128K的9.5x是TBT，不含prefill后压缩/搜索成本的端到端保证，4A100是总实验环境。固定budget96消融分数分别掉2.22/1.24，取舍可采；32个8K请求与256K单请求不是等价并发证据。2+2+2=6，INFER-KV-CACHE。

### 22594 v1

实读§2.2、§3.3 Claim1、§4Assumptions5–7/Theorem1、§5.1–5.2。latent topic/class生成+fullylearned LM作Bayesian条件模型；特例一层position-only attention、无限文档、blockdiagonalWV，不推出现实Transformer一般机制。理论还需输出margin、KL可区分/目标接近pretrain mixture及有界loglikelihoodratio方差；theta范围含自身时严格负KL需排除真实theta的解释，不能直接照录forall式为可执行保证。GPT2只finetune七任务代理pretraining、concepttoken cosine近似任务相似，不等重训/真实KL验证。可采用context与pretraining可识别性共同限制的条件分析，不授多给例子必消偏；2+1+2=5，WORLDVIEW-LLM-INTELLIGENCE，具体有限理论留报告。

### 22603 v1

实读§3.1–3.3、§4.1–4.2、§5/Table1–2及§6。Llama音视频speech任务中间specialtoken与BOS方向相近、MLP2巨大activation；范数不变的定向旋转有局部去/造sink对照，比相关图更强，但未证任意模型唯一根因。BOS/nonBOS cosine平方loss只加中层、lambda在10/100/10000取最优；LRS2 ASR/AVSR、LRS3VSR、高压缩WER下降，低压缩近baseline，不推出所有sink应删或通用多模态改善。训练配置引用既有code而本研究未跑，不授cost零。2+2+2=6，MULTIMODAL-REPRESENTATION。

### 22626 v1

实读§3.1–3.2.4、§4、§5–6。typed不可变message+实测runtime/RSS回传、有限输入网格log-log拟合→重规划，可报告资源反馈闭环。静态pruner实际对algorithm字符串regex，非程序复杂度证明；默认只输入n对通用任务不足，timeout/missing值与LLM回退不认证渐近BigO。26任务*3seed=78，表49/29分域不符合16/10各*3，73.08%run success与80.77%task cumulative是不同人口；所有失败全效率与staticprune/编码错误叙述亦不齐。singlepassbaseline和多次尝试预算不等，硬件profile披露不足。采用有限已测资源约束与正确性分责，不采普遍优越/复杂度认证；2+1+2=5，AGENT-REFLECTION，方法组合局部证据留报告。

### 22641 v1

实读§3–5/Alg1、KVcache、§6/6.1及§8。冻结已finetune backbone，浅n层+两FC/LayerNorm imitation预测末四层融合表征，CE+cos+KD训练20epochs；共享前n层KV并由fullmodel逐token greedy校验/首错纠正。低层直接head差不等所有VLM必须此结构；Alg含EOS条件排印/KL下标冲突，采用标准greedy验证概念而不照录无错实现。BLIP2 OPT2.7B/FlanT5xl、LLaVA1.5-7B及caption/dialog/MMVet，1.85x等为平均pertoken延迟，短1–2tokenVQA收益小；无一般sampling无损证据、tailSLO/完整硬件runtime未披露。2+2+2=6，INFER-SPECULATIVE-DECODING。

### 22969 v1（纠正先前误排）

实读intro相对globaldensity工作的新1hopmeanobs条件机制、§V Assumptions/Lemma1/Theorem1及Lemmas2–3/Eqs21–34、§VI-B/ablation/horizon。基于noisepredictor/classifier梯度Lipschitz及邻轨迹有界spread C，把mean-conditioned drift差界转成shared-noise SDE路径KL上界；还需起始分布项与端点可积性，不是单凭有限C普遍收敛。界不随N自动消失，均值隐藏邻居异质相关性；这是条件压缩/通信-误差取舍的新论点，不只wireless数值应用，应准入2+2+2=6。只采用模拟QoS/理想RF与meanfield消融范围，长horizon更差，不映射为LLM serving/SLO证明。MULTIMODAL-GENERATIVE-PARADIGMS条件化采样；不借非LLM理由排除，交reader定点确认后作Books判断。

本轮后到补读：22101 §3.1–3.2、§4.1–4.3已实读，故下方早期“需继续核”已经关闭。OSSCAR剪50%MLP及最后8blocks再SFT→375M；1.7B离线summary用冻结下游yes/no分布KL+长度惩罚，GSPO/w0.4；同一摘要分布再SFT优于只在fulldescription训练。它不保证对新consumer的无损压缩，离线生成/刷新成本不消失，所有联合吞吐仍按原配置限定。

全部ID前缀2510。日门引用DC2原件及INVENTORY合法联合界，非submitted/created独断；精确v1正文为`REPAIR_CORE_<ID>.raw/.txt`，current abs为NOTICE，只检查版本/早稿/撤回信号。未运行代码或复现。以下是writer已实际阅读位置及判断，不以下载计完成；Books决定待具体正文比较。

## 21956 v1

实读§3.1–3.3/Eqs5–23、§4算法-线程/数据复用、§5.1–5.2/必要Table2。采用仅为可分离核`1+qk`的前缀累积、反向后缀重算与IO联动，不等softmax精确替代；Q/K单位化限制核值/梯度。手工backward避免autograd保存每个ND²中间量，仍需ND输入/输出存储。Eqs17–18因果求和上界与Eq21后缀递推有表面索引不一致，不把排印当已验证实现证明。

单层A6000 FP32/B4/H16/D128、100次平均；N范围1k–300k，维度实验N4096。1.4B/Pythia结构、Wiki40B英文、8*A6000、context8192/globalbatch256相同步数，LA迭代收敛慢但wallclock快。作者3.3x/3.6x仅对应GatedLA该配置；不能外推现代bf16/fused kernel、端侧、所有语义能力或线上SLO。当前论文的FLOPs/内存语句有D依赖叙述不一，采用不包含普遍complexity证明。标准证据足，2+2+2=6；长期比较应落MODEL-LONG-CONTEXT，而不把自写CUDA实现当本项目复现。

## 21970 v1

实读§3.3–3.4、§4.1–4.5/Figs2–9、§5.2/5.4。Llama3.2-1B、5k合成训练/100合成测试的JSON exact match不等开放电商能力；T4的44.56→7.92tok/s与VRAM3.27→1.93GB是作者本配置观测。文中明确“suggests/appears”dequant开销，没提供kernel trace，不能写成已验证根因或T4无法低比特。CPU Ryzen5800HS上的GGUF/llama.cpp与FP16路径不是GPU消融，18x不跨设备比较；Q4和Q5质量不一。batch、输入/输出长度、并发、SLO、精确engine/kernel版本、重复运行不确定性Not Disclosed；无生产流量证据。采用“压缩不保证加速，要测格式/引擎/硬件/workload联合路径”的局部反例，不采用现代GPU一定反转/小模型普遍等大模型。2+1+2=5，安全/设计反侧必要已读足；待INFER-TENSORRT-LLM具体覆盖比较。

## 21977 v1

实读§2.1–2.4、§3.1–3.5、§3.8–3.9、Limitations。DSA先用KL拟合option-token分布，再把单一背景变化的quantile shift跨背景共享，stopgradient到样本较多组、更新小组；只调最后transformer/softmax层。五survey corpus、Qwen3-4B/32B，随机2k/4k样本，10 runs；TS直接经验分布是必要对照，JSD/KLD而非one-hot accuracy。

独立背景假设与实际背景相关性冲突已由作者明示，语料抽取有LLM参与；不能把模拟替代真人、所测总体分布当真正未见人口。**中心数学疑点**：Eq中shift `d_k=s_b1^k-s_b2^k`可有负值且不归一，§2.3却直接写KL(d_LLM,d_hat)，原文未披露把有符号shift变概率分布的映射；stopgradient亦不能修复KL定义域。由此不能采用该loss为可执行稳定训练配方，待reader精确核此点；不因未复现造hold。局部TS评价/跨组共享思路可报告，若必要定义无法从原件解决则是具体中心争议而非普通待办。2+1+2=5不因争议降分。

## 21978 v1

实读§4、§5.1/5.3与Limitations，Qwen2.5-VL3B/7B，RLVR-only与hybrid分开；8GPU、4rollouts，7B500steps/batch16。uniform replay、PropMix、coreset、LwF等对照；KL默认关，LwF另设0.01，不将别的reasoning模型对比当等预算消融。可报告“当前任务KL不测任务外遗忘、重放需跨域目标监测”的有效局部反例。

**中心recipe疑点**：定义c=current/previous loss却称c>1为loss下降；sigma求和到t+W且除W-1，而声称在线、均值用截至t的W项；等权baseline在§5.3写lambda=1/K，但§4系数平均应为1，scale关系未解释。主张不直接采用其在线scheduler公式/一般稳定性。变化不是普通未读；reader需核是否排版/代码有当前原文可用解释，若不能须具体隔离中心机制。保留实验观察不将矛盾泛化为replay无效，2+2+2=6。

## 21986 v1

实读§3.3–3.5、§4.1–4.2与§4.4必要消融。前后各2块dense，中间sparse75%，mask回填、channel concat/project与浅层残差融合；2x2组留1token保证局部覆盖，短fulltoken阶段弥合train/infer gap。PDG无条件支路只过浅层，条件支路过中层；不是任意模型直接删CFG一半。

ImageNet1K256²、SiT-B/2/XL/2、SD/Flux VAE不同channel不能混；主要效率为DeepSpeed估算training/inference FLOPs，不把9.8x计算节省写成通用wallclock。相同75%drop结构采样比uniform好，87.5%变差；删任一路与浅层depth消融支持互补，不证明局部/全局唯一因果功能或所有生成域。512²/few-step仅文中局部扩展，不需要无关附件。长期可采分层计算+低成本细节旁路、token拓扑与训练分布交接，2+2+2=6；待MULTIMODAL-GENERATIVE-PARADIGMS具体比较。

## 22026 v1

实读§2/2.3、Table2、Theorem3.1/Cor3.2与§4.3/Theorem4.3、§5限制。无FFN、Q/K/V tied或identity的attention-only连续深度系统；把token分解r*theta，链式法则给角速度的1/r投影，norm位置改变token依赖speed regulator，但不是相同轨迹的统一换速。聚类定理限随机初始化和特定矩阵；terminal速率定理更要求极窄cone及Q'K范数约束。Pre/Peri局部多项式与Post指数不等所有模型塌缩结论；线性r增长与随机初始化sqrt(t)不一致作者已明示，未分析实际反传/中段/metastability。采用“径向/角向分开能暴露norm位置影响”的有假设解释，不采Peri普遍最佳或训练优化证明。2+2+3=7，必要数学与直接限制已深入足；owner MODEL-TRANSFORMER-LAYER。

## 22042 v1

实读§3、§4.1–4.2与§6方法/评价、§7限制。mean-pooled激活centered-SVD（synthetic neutral/emotion rewrites）与real dataset线性对齐；ML-AURA one-v-all neuron AP不是感情体验。Llama3.1-8B为主、OLMo/Ministral附局部证；八emotion dataset语言受支持清单选择，有标签ontology/翻译风格混杂不能称跨文化普遍情感结构。

§6 top40 SVD维、所选层单层MLP residual shift，emotion-token CE/margin加hidden-state cosine/L2一致性；deterministic temp0。大多数label控制成功及Hindi/envy/excitement不稳，证明表征/输出可操作，不证明内在感受或语义保真（hidden相似只是代理）。MLP及layer选择的监督不能称完全无监督发现；不必重复无关神经科学附件。2+1+2=5标准完成，owner WORLDVIEW-REPRESENTATION，具体steering数值留报告。

## 22067 v1

实读§3–4、§5.1、§6消融/alpha/efficiency与结论限制。固定query阶段的正attention变化，spaCy信息词与top50%head，50TextVQA校准layer/head；生成时saliency bias且同时按比例增query，避免只放大视觉sink。3模型LLaVA1.5 7/13B及Qwen2-VL7B、CHAIR/POPE/MMHal分别指标；Qwen缺baseline实现不作跨模型baseline排名。alpha>5在MME退化，vague/视觉不相关query会误saliency；不能称attention即因果真值/无条件去幻觉。相对latency1.13仅32输出token的MMHal/LLaVA7B，硬件、batch、并发、SLO等Not Disclosed，不授部署成本保证。2+1+2=5标准完成；待MULTIMODAL-REPRESENTATION具体覆盖。

## 22101 v1

实读§5.1–5.3、§6在线结果及§3/4压缩范围需继续核。600M→375M与摘要context900→220不能把两者共同效果归单因；SGLang0.4.6/CUDA12.6/H100，Poisson request每个10candidate，p95<500ms；prefill-only最后token relevance-logit，不生成chat，330/420/1530 items/sec/GPU为此协议。

Serving新增具体是同forward内prefixKV物化后复用：suffix对sharedprefix和自身causal两次attention、LSE合并，区别先单独prefill再剩余prompt的两pass时序。batch tokenization、去sampling/不必要token-logprob、合并GPU gather/延后CPU copy/gc.freeze只能作为此高RPS scoring路径的作者工程例，不给任意chat服务照搬。在线cache15min与PID depth/traffic shaping联合，不将10x当单一kernel收益；生产效果是作者报告而非本项目部署证明。2+2+2=6，精确owner拟INFER-KV-CACHE（实现时序）/其他已覆盖principles只报告，待完整相关邻接比较。

## 22132 v1

实读§3.1–3.3、§4.1–4.4、Table1与§5。8orthogonal thought vectors，hidden-state attention/gate与3D控制向量→4096D映射；Gemma2-9B加1.06B trainable、layer21、1000steps、GSM8K单数据，不可称8小向量零成本。标准CE加lambda0.1负entropy，非无标注完全self-supervision。

**中心可核冲突**：Table1 CoT0.7725 vs随文89.7%，无法同口径；8选择概率的Shannon entropy即使以bit计也≤3，而Table1报告4.228（正文把它描述为同一thought selection entropy，未交代另一变量/单位）。控制平均0.417掩盖Length2.7%，不授长短/复杂度可可靠控制。下游收益未有CE/LoRA/1.06B额外参数及entropy单独预算消融，PCA仅4.4%variance不证明固定语义strategy。拟2+1+2=5，必要中心疑点待reader定点核；不把未复现当争议、不把作者headline进Books。

## 22109 v1

实读§2–4/Table1、§5边界：causal depthwise卷积在每embedding维生成log-spaced SITH滤波槽，再concat近期m=256未压token，只在首block前压缩，loss仅近期token；预处理O(MLd)没消失，不是固定状态/任意horizon恒时。GPT2small124M、A10040GB、WT103/PG19、13种槽数及delta-pulse同长度对照，perword PPL与token PPL分开。L53窗口8192仍有损，近细远粗不能精确恢复任意旧事实；Table1不同架构/参数不等严配预算，PG19无同规模公开对照，不能由PPL优势授通用语言/检索胜。2+1+2=5标准足，拟MODEL-LONG-CONTEXT输入压缩分支。

## 22118 v1

实读§3.1/3.2、§4人审、§5/RQ1–2：2D detector bbox生成定性空间primitive，轻量predicate先筛再realize问题，不依赖单视图3D恢复；因此不能把2D大小/左右当真实3D尺度/距离。人审OpenSpaces50图250问、GRAID317对/4人，原文57.6%是answers incorrect而非摘要的validation rate，不能混；GRAID91.16%是排invalid/confusing的样本率，不是全库误差上界。Llama3.2Vision11B/LoRA200steps、基本六问跨类型及BDD→NuImages支持局部迁移，但data源/detector标签/定性ontology受限，不证明真实spatialworld已恢复。2+1+2=5，采用可审判定primitive降低伪标误差链；拟TRAIN-DATA，具体人审分母留报告。

## 22127 v1

实读§3.1–3.3问题、§4.1–4.3/Eqs6–10、§5setup及A.2。CLIP corruption下embedding variance collapse，按pseudo-label估计class/globalmean并累计梯度，只更新LayerNorm；每batch后重置encoder/optimizer但保留mean/gradient累积，不能只说“reset”就无跨batch状态。小batch某类仅一样本会退化为totalvariance，跨batchmean是具体避免这类proxy错位的设计。CIFAR10C/100C/ImageNetC的ViTB32/B16/L14，severity5，各corruption独立适配，默认B20；不授任意连续domain切换/攻击下伪标签可靠或新类安全保证。文本embedding融合含Kprior10000，历史类计数不确定时原prior要保留。2+1+2=5标准完成，拟MULTIMODAL-REPRESENTATION适配状态/统计边界；不采用普遍理论保证。

## 22171 v1

实读§4.1–4.2/5.1、§5.3与5.3.1：VisualBERT113M scorer把generated-token/prob-bin/hidden projection合并，BCE训练correctness；不是无监督真值/黑箱无取件。精确v1为LLaVA7/13B+InstructBLIP、AOKVQA/VizWiz（PathVQA科学支线不扩）；**当前题摘Qwen-VL/两dataset/5%等后改事实不倒填**。LAVE GPT3.5对众包答案给label是评价器支持，risk/coverage阈值从calibration20%挑，不由AUROC保证任意风险水平；AOKVQA→OKVQA混合越OOD、各法都退化。需要scorer训练、hidden读出和113M执行费；不把排名增强当分布无关校准/安全。2+1+2=5，拟PLATFORM-EVALUATION-SYSTEM的可学习选择/人口合同。

## 22201 v1

实读§IV-A/B、§V-A/C/D与结论限制。构造incoherent副分支：部分action-token selfattention map置identity，使token不交流，再用`(1+lambda)v-lambda*vIC`作flow field；这是候选guidance，不由densityratio文字直接证明实际flow严格采样该目标，更不授物理硬约束。GR00T-N1、RoboCasa24任务/DexMimicGen及SO101两pickplace，3次×24/10trials；现实gripper加rubber改动不隐藏。ATV/Jerk只对approach前64timesteps，人机后半轨迹已分叉；更平滑不等更正确/更安全，ensemble也可更平滑却模糊多模态动作。额外分支/cache和late-layer选择均成本，未披露完整deadline/SLO。2+2+2=6标准足，拟MULTIMODAL-GENERATIVE-PARADIGMS（sampler proposal），controller执行仍Ch26。

## 22210 v1

实读§4.2 providers、§5 keytoken/DEF/REF最小enclosing-symbol及diagnostics迭代、§7.2setup/results与讨论。LSP取件只在workspace；lexicalsemantic tokens+AST挑keytokens，精确symbol边界替相似chunk；generated tests用diagnostics纠错不等完整编译/执行证明，动态Python盲点作者已明示。六项目/三语言、方法>10行、5runs/最多5次repair；baselines受context限，覆盖率不测断言有效/需求正确，不能称所有语言完备最小依赖。仅保符号接口有条件复用与静态诊断-执行分责，全部LSP启动/index/query/repair调用计费。2+2+2=6，拟AGENT-RAG实际依赖取件，执行验收不转给retriever。

## 22272 v1

实读§4.1/4.2、§5.1–5.5、§6.1.4/6.2：相同text-retriever选slide，以text/image分别给Qwen2VL；图像保layout/formula，检索仍可漏视觉-only线索。CPT Llama3.1-8B、33%wiki replay、≤15epochs/domainPPL earlystop，1course调LR后迁所有course；小数据失败不证明一般CPT不如RAG。grader MistralLarge2相关0.84不等逐题truth，部分language/exam反向；domainPPL下降不保考试能力/任务外知识。RAG k4与文本chunk300等调优，3类GPU路径不直接成本合并。2+1+2=5，采用检索表示/consumer模态可不同及LMloss/任务结果独立，拟AGENT-RAG具体覆盖/版本事实仅报告。

## 22276 v1：准入依据实质变化，提请reader定点改判

实读§3过滤、§4标注、§5.1–5.5及§7。当前DataCite所谓native-v-translated matched-filtering/两model-family对照**不在v1**。v1只同SigLIP2、same30ksteps/B8192/8H200比较WAON155M与ReLAION日文subset可下载85M，两者都是native来源，过滤/数据量也不同；不能据其授“native优于translated的主因”。v1剩余为新日文图文资源、单人选图374类benchmark及任务性能，没有初筛拟保留的受控source-origin新证；相同主题不是保留理由。请求reader核v1采用依据失效后排除此新候选（不动旧safeguard，不因Books或工作量删池），保全部已读原件/具体改判，后改native对照仅其真实修订事件线索。

## 22317 v1

实读§2.2/2.3、§3.2–3.5、§6/7。CPU前缀trie按gain-ratio排序4-token context，IB1kNN/TRIBL2/IGTree分别在失配点局部kNN或node分布读出；IGTree majority-agree剪枝有损，数据/model容量耦合不是固定神经参数替代。GPT2/Neo身份与训练数据、CPU/GPU路径不同，>1B训练硬件变且single-run；拟合外推trillion不保证长期scaling或绿色优势。

重要反侧：§6的所谓PPL只平均目标获得非零概率的token，TRIBL2仅41.9%/更大63%人口，不能与GPT全support PPL比或说更会语言；logprob求和和PPL术语也未闭。memory速度可报告，但训练/驻留最多4–8TB CPU节点、查找和语料存储不能省。2+2+2=6标准/反侧足；有效增量是稀疏support/条件评价与存储-查找取舍，具体旧算法或当前scaling数值仅报告，待owner比较。
