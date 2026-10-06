# 2026-02-24：V3 原源必要证据停点

作者：feb24_v3。本文是本日恢复点，不继承旧 V2 收据或 Weekly 判断。`V3_NATIVE_*.txt/json` 保留实际原响应与查询；本记录只写已实际读到的源段，不把下载成功当审阅。尚缺关键对照、日期或 Books 对读的普通待办仍是普通待办；不得据此标完成。所有 arXiv 采用版本为明确的 `v1` HTML，DataCite 当前摘要只作发现。

## 已读 core，仍待 owner 比较及独立证据复核

- **2602.17809 SBA**：§3.2 KFAC tangent Hessian、QR retraction、posterior samples平均；Theorem1仅局部二阶/高度集中的posterior，并非全域Bayes校准保证。§5.1有OrthoLoRA/Laplace/Gauss+Proj、5 seeds、同rank/3epoch；AppendixF显示训练7%与推理5次forward的成本不能混称7%总体开销。Limitations指出MAP外局部近似、70B+与多语言未验证；distilled student不保留完整aleatoric/epistemic分解。拟命题是正交adapter上“不确定性先建模在切空间”这一替代分支，不授理论与所有任务绝对校准。
- **2602.17817 GPUMemNet/GPUUtilNet**：§3.1 FakeTensor无法计allocator reserved/optimizer/buffer，部分CUDA-only与dynamic ops失败；§6 8GB bins换精度但浪费可拼放机会、GPT2新算子OOD、framework优化改标签需重收。SMACT/SMOCC/DRAMA单任务预测不能相加成为共置干扰，Transformer DRAMA仅62%。不是把MLP97%推广为LLM调度保证。
- **2602.17835 IProX**：§4 influence second-moment reweighted SVD，随后low-rank gradient matching+logit KL，不以weight reconstruction等同ranking fidelity。AppendixC Table12换standard SVD且其余不变有2–3分差，§4.2与AppendixB保留过强compression、layer-wise误差积累和stochastic训练限制。尚待核§5主要预算/耗时及公式假设后关闭深入审阅。
- **2602.17837 TFL（安全，强制深入）**：§III white-box gradient+same-machine DRAM威胁，不是remote-only黑箱。§IV新增keyword loss与aux benign utility；ImpactScore、range限制与SKIP继承旧方法，不将借用项算新增。§V TableI基于head-only、两target questions、2A100-80GB搜索、DDR3/DDR4实物；主要baseline FP4/BF16不一致。DeepSeek-R1 reasoning关闭。§VI/§VII head protected仍可body攻击，不能以整体QA/困惑度稳定判排除定向完整性破坏。尚待实物映射与关键utility消融定点核，未声称HBM硬件/所有部署可攻击。
- **2602.17846**：§3按noise level测memorization，不以train-test MSE gap直接替代；§4 Gaussian shell coverage与posterior concentration解释中噪声风险，small-noise empirical optimum与learned denoiser不能混淆。§5只target中间noise段undertrain；理论基于特定几何与Gaussian/circulant idealization，尚待同gap-budget控制与质量成本。
- **2602.17867 ADAPT**：§3.2/3.4独立beam provenance+guaranteed/free slots、adaptive gradient/logit mutations，避免GCG initialization与trajectory local minima；§4.3同initialization多run变异。Gemma2-2B SAE latent testbed，不等于最大激活prompt证明单义feature语义或因果行为；尚待主baseline预算与limitations。
- **2602.17869 CompressV**：§3.2 unconstrained AE compact latent有OOD holes；avg-pool residual+learned丢失信息补偿使latent留在原feature space。§4.3 fixed32frames/64× comparison无constraint有loss spikes、Gaussian约束仅部分缓解、residual更好，预训练尤其shot-change有益。AppendixA.4消融省略stage2，不能把全3-stage SoTA增益都归因AE。本项core确认不是“列两模块”准入。
- **2602.17898 convex readout/PCC**：§2.1固定final embeddings、convex权重与scalar linear readout；Theorem2.2/AppendixD小intrinsic dispersion相对baseline signal ratio<1时给PCC gain bound。不是residual/FFN/整个Transformer或LLM能力上界。§3 dispersion-normalized loss/temperature/residual是条件分支，尚待精确公式与owner是否已有相同边界。
- **2602.17909 Range3C**：§2.2 angular local GP均值深度与variance阈值mask后才geometric condition；§3.2 unchanged GEN3C、VoD同camera path/首RGB、MoGe替radar/LiDAR，稀疏range不等同dense perception。未看到variance单项消融，故sensor总收益不归因confidence mask，不外推完整world transition模型。
- **2602.17913 TierMem**：§2 immutable raw+provenance summary、sufficiency router升级与verified writeback；§5.3 linked/global-BM25对照不仅省成本，还更多token/延迟，不能称指针免费。§5.2 LoCoMo hard recall71.7%，非可靠miss detector保证。§5.4同fixed queries三epoch且回答时tier1 frozen、between-epoch writeback，非真实线上自主持续学习证明。
- **2602.17930/17931 MIRA，单家族**：17931是同作者short文本、同memory graph+advantage shaping，合并而不双计。17930 §2.3 utility来自同on-policy rollout与memory/state-action/goal-phase match；§2.4有随优势比例衰减而非改environment reward。Theorem需boundedness/scale/trust region；不能把PPO clip本身当全局收敛保证。§3小tabular+MiniGrid/BabyAI、same architecture/hyperparameters；AppendixD misaligned LLM priors可导致收益下降，剩余理论和limits待核。
- **2602.17951 ROCKET**：§3/4 shared residual-stream projector替multi-projector gradient interference、nested浅层少参数/深层多参数；AppendixH数学需Jacobian near-isometry/subspace assumptions，不是跨层loss天然同向。尚待Table8 matched预算/稀疏激活control与训练条件。
- **2602.17993 TurboConn**：§3 token t高层→t+1低层避免同token循环，路径depth随序列增长；grouping改变并行训练/路径深度取舍，不能只称不增FLOPs无代价。尚待同finetune/连接密度/延迟对照。
- **2602.18007 heterogeneous training**：§2.1 PP跨vendor-Gloo、TP/DP homogeneous native CCL；§2.2 host control管理MR/connection/event，GPU→chunk D2D→GDR→NIC→peer再D2D，消除host data bounce但不是零拷贝或无CPU参与。Device/Net/CCL adaptors与hierarchical collective。尚待实际硬件与对照。
- **2602.18020 UaOR**：§3 action entropy trigger、next FFN attentive observation blending；§4.3 Table4 random matching injection rate与all-layer对照，direct-add collapse、mean-blending难超强baseline，不能只说加观测就更稳。§4.3Table5 instruction与observation效果不同；主结论需训练/推理环境约束。
- **2602.18022 DCAG**：§4 RoPE后K/V bias+delta独立缩放；固定attention下V线性，K经softmax非线性。只对局部算子成立，整个多层DiT输出不保证线性/两通道统计独立。尚待PIE固定编辑质量与saturation限制。
- **2602.18037 Gradient Regularization**：v1标题Prevents，当前标题Mitigates，不继承当前修订结论。§3连续action+smoothing+Lipschitz true reward连接flat maximum与proxy BT error；LM discrete仅实验外推。§2.3额外finite-difference梯度，§5实际reward hacking控制尚待核；不得称GR保证消除hacking或KL失效普遍。
- **2602.18055 MAGE**：一次core补准入事实：§4.1 Fig3/4同total rank比较input-only2split与input/output4split，input understanding与output generation对应的LoRA独立更新、其他冻结；不是仅general/expert名字组合。§5 SEED-X/Llama2-13B、已见image/text模态，§7新增未见模态未测且专家成本随模态扩张。
- **2602.18071 EgoPush**：v1 TableI teacher99.31/98.34/99.22→student70.70/21.09/0；不能用当前abstract87.3/54.8/0倒填。§4.2只改变teacher perception，RL/architecture/hyperparameters相同；trajectory/time仅successful episodes有选择偏差。§5 reactive current depth+short action history无belief，occlusion中view goal/corridor可deadlock，不授普适VLA边界。
- **2602.18093 PrediT**：§3 linear-multistep AB predictor/AM corrector，高dynamics补真实model evaluation，dynamic horizon；higher order降低局部误差需trajectory smooth，不是任意skip免费。§4 Table2 predictor/corrector/DSM ablation、AppendixH threshold/corrector speed-quality取舍；尚待机器与端到端成本条件。
- **2602.18420 SPQ**：§6.1/6.2 matched weight memory下SVD适attention/prune适MLP、§6.4 ratio/variance阈值约束。Table3 C4/部分reasoning劣化不能叫所有quality保持；§8.3还含200-step LoRA recovery，GPTQ没有等价recovery对照，不能把改进纯归因三组件协同。Table2 one-sided p不能据not significant证明非劣性。保留条件与待核，不机械排除成熟组合。

## 明确改判/排除的新增原依据（待独立确认）

- **2602.17881 thesis**：AppendixA明确German说明核心steering prediction已在2505.22637的ICLR2025workshop公开；原abs也含direction/activation difference与steering efficacy预测。不是旧审阅重复声明，而是此次学位稿新增事件未展示独立的新长期机制；仅定点contribution list核增量后可关闭，不遍历89页。
- **2602.18025**：§3.1共用locomotion objective，§3.3继承URMA common morphology policy、joint/foot descriptor attention；具体新贡献是16robot offline-IQL+static morphology conflict grouping。论文引言引用robot foundation不等于实证语言/VLA或一般基础模型设计桥接；该实际scope待parent校准后EX，而非所有跨embodiment研究范围外。

## 第三批已经开始的必要源位置

- **2602.18094 OODBench**：§1承认训练corpus未知，以detector故障+human语义对象定义OOD；§5.3多个detector intersection vs symmetric difference产生hard/soft。这只能证特定common-class困难切片，不证明真正训练分布外。AppendixE threshold越严subset缩小/界限变淡；还需§3 construction与sampling控制。
- **2602.18095 Logitext**：§3.3 outer Z3 Boolean candidates+inner LLM propose/verify/refine NL text constraints；T-round失败会block当前Boolean assignment，不等于semantic UNSAT正确证书。§4.2 clause LLM error、example list误作conjunction，LegalBench任务低于holistic baseline。其长期命题是partial formalization的solver语义边界，非形式求解器让所有自然语言可靠。
- **2602.18116 FOLD**：§2 theory比较有one-rank slack且local parameter-Lipschitz；§3 empirical却match retainedsize/FLOPs、CNN同REPAIR、ViT/LLM no calibration，不能将理论直接换成matched-rank universal保证。§4/AppendixF高lr sharp minima可反转，small60M/130M Llama不是7B质量保证。
- **2602.18131 tPC-RTRL**：§3 Eq12历史influence+immediate梯度、Eq13在converged inferred hidden state评估Jacobian，F=0时exact而实际通常非0；§4 copy/WikiText2/EnFr近BPTT，§5仅single recurrent layer，多层O(L²) influence matrices未解决，不授低成本替代BPTT。
- **2602.18137 adversarial QA**：§3 strong/weak同context，maximize LLM-judge answer disagreement，TextGrad question改写后teacher回答做SFT；expert/judge/guide同strong model，有shared error。§4三CUAD合同491题、synthetic token数不等，没有直接oracle真值/等budget控制；可保留target-conditioned合成的条件，不宣称分歧必为target错误或泛用省70×。
- **2602.18145 frequency-aware attention**：§3是token-position谱，不是wallclock时间频率；高pass L2 feature+linear detector，context与generated attention分开。Toy analysis仅简化latent sources，不能high-frequency即因果hallucination；仍待训练/test分割和主comparison。
- **2602.18152 statistical signature**：§3gzip UTF8 rawbytes无tokenization，用prefix curve测长度积累；§4 Wikipedia/Grok含同topic重写与长prefix混人类段、Reddit/Moltbook有来源混杂。需定点受控Human–AI小prefix与heldout边界，不把整体社会统计采作机制。
- **2602.18176 Info-Gain sampler**：§3 state剩余mask marginal entropy、candidate actions一次batched evaluation后maximize IG-immediatecost；Fig2 caption符号相反但Eq5/argmax清楚，不照抄caption。批forward不是一次标量forward成本，需AppendixF计算与budget。entropy只是模型代理，不是groundtruth information。
- **2602.18181 SeedFlood**：§3同RNG/init，seed-scalar message每client只apply一次，D hops同步flood产生all-gather-like更新；SubCGE shared低rank canonicalbasis聚合O(n+rd)而非O(nd)。§4.5 delayedflood使bounded stale updates，非无时延拓扑保证；通信与网络规模/diameter仍有关，只主要payload不随modeldimension。

## 后续实际 core 与需继续的局部对照

- **2602.18182**：§3以2×2PL适宜区间而非能力单调值定义propensity；§4四类约250题/低难度隔离能力，7级normative rubric与同GPT4.1生成/判分存在共偏。尚须主heldout条件，不称模型内在人格或Agent安全证明。
- **2602.18196 RAT+**：§3/Appendix Table7先dense recurrent预训练再active learning/resolution adaptation，非training-free；大D从depth1/2分布起点变化时固定1B dense recurrence仍失败。1.5B/100B与2.6B/200B作者训练规模不授免费递归；性能数字尚需实际配置。
- **2602.18224 SimVLA**：§4.1/§4.5 Table6只在自身recipe单knob控制；98.6对no shuffling9.9/no normalization12.3体现recipe的重要，而head与conditioner只是同recipe内局部对照。外部baseline引用或同input复现未统一全部recipe/compute；realrobot同500h/64H100/150K仍有π0.5 pretrained initialization差异。不以0.5B胜大模型推出架构无效；可保留架构比较须先控制recipe的具体设计反证，深入。
- **2602.18230 scoreable games复现（纠错深入）**：§3.1.5公开parser在malformed response时fallback暴露私有scratchpad，修正版去fallback并将invalid games排除denominator且另报failure；AppendixD低leakage/较少deal partly mechanical。需把invalid率与conditional success分列；原p1阈值+10与last-valid deal接受规则亦已纠正，不据20场/不同量化模型排普遍人格排名。
- **2602.18232 CCD**：§3仅低confidence+reasoning region subtract masked high-confidence历史分布，high-confidence anchor/attention link是启发式一阶近似，不是完整因果证明；尚需branch/KV/端到端成本与threshold对照，不泛化所有生成。
- **2602.18252 robust tokenizer（安全深入）**：§3 APGD攻击量化前continuous feature而非不可导code index，fine-tune encoder接近原输入表示、冻结codebook/downstream；§4.2替换tokenizer后其它模型组件不变。§5即使攻击失败仍125/128indices改变，index稳定非安全必要条件；ε2/255、4/255与clean/robust quality需分列，非所有后端安全。
- **2602.18292 BoK**：§4.3非负token coverage U=sum w[1−(1−q)^K]的diminishing return、KL镜像更新；不是完整正确solution覆盖。§4.4同prompts/scripts/Tmax3072、两个Qwen7B的MATH500/GPQA/HumanEval，尚需K与样本budget/结果；topk50非所有采样器全局最优。
- **2602.18297 CoT monitor（修正假设深入）**：§2/§3 X→Z→O与Y=g(O,X)；MI(O;Z|X)>0是monitor可能所需信息，不授单一attribute一定可测。信息gap与policy/elicitation gap分开；policy作为monitor只在自身建模条件消除信息gap，不产生真值标签。尚需MI surrogate RL control与隐藏channel反证，不称意识/真实因果透明。
- **2602.18301 protoTokens**：§3每example冻结LLM优化e,m至accuracy0.9或maxiter，causal mask内一forward重建省的是后续decode，不抹去per-example优化。§4.5强anchor伤重建，关系matrix蒸馏+batch6改善局部semantic geometry，未实现general semantic预测器；不是通用sequence codec速度保证。
- **2602.18307 VeriSoftBench**：§3依赖closure curated context取groundtruth proof的oracle，未给lemma proof bodies也非实际retrieval算法。fullvsoracle curated是条件对照；Gödel full44/curated496因ctxlimit不同，Aristotle100subset与全部500不同，不直接合成榜单。主Table3/费用尚需绑定protocol，不称自动证明生产可靠。
- **2602.18308 JPmHC**：§2无限宽/各向同性/自由概率解释bistochastic skip方向收缩；正交Cayley局部skip不授整个有限Transformer dynamical isometry。§7.4承认419Kvs349Ksteps、架构pre/post改变，matchedcompute未来；TinyRecursiveModel ARC-AGI1不能归因纯正交优势。
- **2602.18333**：§2 modular arithmetic/S5 formal state tasks与ID测试；N*是预设LR/seed grid最小成功样本量，不是平均seed概率。Transformer vs LSTM/inputdependent denseSSM；§4weightsharing主要结果尚待读，不能外推所有language sample complexity。
- **2602.18374 ZS-IP**：§3.2 PCA/edge pre/post pushlines给VLM grounded contact空间，而非2Dgrid抽象坐标；depth/ArUco几何映射和OMPL/Pilz低层独立。§5grid失败是接触点解释盲区，7DoF/最多5iter；遮挡strawberry只有1次成功、错误stack VLM成功判定仍算failure。尚需Table2sample数，不授通用zero-shot manipulation。
- **2602.18397 VLA-Perf**：§3解析roofline先假定accuracy threshold满足，无quality实测。π0三相机224px/768vision/32language、50actionchunk/10denoise/14DoF；singlecomponent local movement忽略，跨组件network载荷分raw/image/vision/KV/action。§4.9异步提升throughput不减少latency、增staleness控制质量未测；尚需实际validation误差，不把hypotheticalGPU解析结果称部署benchmark。
- **2602.18417**：§3闭子群U(d)上hidden state/矩阵乘积+Exp更新，而非仅operator norm约束；no QKV map/group similarity与input tangent embedding改算子。parameter-matched TinyShakespeare/PTB only O(d)；mixing dimension/seed1与compute未matched；limits还需定点核。
- **2602.18422 GeneratedReality**：§3 hybrid2D skeletonControlNet+3D handtokens，先各自训练后joint减轻从零不稳，不把camera/hand可控性当物理真实。14B condition研究与5B causal/distilled12frame推理不同；Quest3/H100实际11FPS/1.4s，0.002s只condition preprocessing，不是20msVR。11人主观体验/textbaseline motorcondition不同；WiLoR/GLOMAP伪GT误差不能当physics证书。
- **2602.18424 CapNav**：§3 45indoorscenes473basepaths×5agents=2365QA，5075edge annotation，多validpaths非单gold；能力/clearance重新限定可行图。human61%与partial judge表明任务判定不完美。thinking的9matchedpairs平均+6.87pp但约8×time，不能从accuracy单点判部署收益；还需metric/agentbound定点核。
- **2602.18425 RVR**：§3两个retriever：initial query与query+verified covered context查询missing docs；corpus/inbatch negative生成与两个indexes不免费。recallcoverage解决多evidence完整性非只topk重排；尚需verifier错误和matched retrieval budget控制。
- **2602.18428 noiseblind**：§4 codimension>2或discrete near-manifold posterior集中，noise level可以从input辨别是有条件可识别，不是所有域无歧义。§6 sampler仍需time/schedule μ(t),ν(t)，Δv=|ν|estimateerror；增益与denoising误差衰减共同决定实际误差，不称ν有界必要条件。§7 matched实验/质量对照待审，不称schedule-free generation。
- **2602.18432 SARAH**：§3 causalVAE每frames_s μ/σ依precedingframes，mirror decoder/用户位置与双人audio条件；历史latent加噪训练替explicit pastmotion mode collapse。gazeCFG headfacing非真眼神理解；SHOW缺userconditioning不作完全matched反侧。300FPS非headset端到端，hardware/ablation待核。
- **2602.18434 MemStream**：§3固定128frame/64featurepairs ReKV至Qwen2.5VL dynamic resolution时query cosine出现temporal drift/redundancy，是局部诊断非所有cache定律。§4AKS以same-patch时间差异稀疏attention保留全部KEYcache；内部/外部retrieval RRF非trainedMoE。Table4/5成本/质量仍待审，不称完整历史压缩。

## 当前可推进 owner 小组

- **17869**实际Ch23 Rate/distortion段已有consumer分布/2602.12370 motion latent扰动；缺feature-reconstruction AE预训练compactlatent接LLM时residual avgpool锚定分布。拟2+1+2=5，具体缺口深入，不写AVS+AE组合或全SOTA保证。原Eq10/11中X/f写法不一致，采用文字“pooled feature anchor”，不造实现轴。
- **17898**实际Ch14单head凸读取/Value尺度与signed替代已在正文；缺固定final embeddings+同scalarlinearhead的PCC相对mean条件界。Theorem2.2要求||w||>0、Rtilde<sigma0/||w||，gain≤2Rtilde/(sigma0/||w||−Rtilde)；不授整个deepTransformer上限。拟2+1+2=5，具体缺口深入，仅采用此局部理论，不靠UCI收益证明通用Attention。
- **18055**实际Ch30已覆盖expert initialization/static与dynamicgradient grouping，未分input understanding/output generation四update责任。§4.1同totalrank comparison支持分责分支；Eq1四adapter都参与forward，§4.1“frozen remains inactive/no influence”与式相冲，不采用该说法。PEMA Eq4形状/empiricalFisher等同Hessian并未充分定义，非本次采用命题，不把它写成配方。§5.7六任务8H100约一周，§7 onlyseenimage/text/linear expertcost；拟2+1+2=5具体缺口深入，PRE已请求root，未写Books。

17881此前“parts已公开”判断修正为逐贡献匹配：本日实际读2505.22637完整abstract，七prompt types、directionagreement、separability三项逐一覆盖当前§1.8，不以parts一句推出all；该事件无明确新增命题 EX请求root，不展开双版全文。

### 三项 PRE 原拟正文（现已写入，三项实际 POST 通过）

以下是写前拟稿留档，不替代现有 Books。17869 实际正文补精确训练条件为“compressor 先预训练；消融的 MLLM 训练仅 stage1 projector 对齐 + SFT，省略 stage2”；root 重新实际读取修正正文、完整邻接与末注后 POST 通过。17898/18055 的实际正文、完整邻接与末注亦已 root POST 通过。三项锁已释放，日级仍进行中。

**Ch23，现2602.12370段后：** 重构预训练的压缩表示也要适配实际消费者，而不只让自己的 decoder 复原原特征。直接学习任意 compact latent 能先用视频单独训练，却可能使接入 LLM 的未见视频落入表示空洞；一种受限分支把 pooled 原特征作为锚点，让 compressor 学平均池化丢失的残差，再重构原特征、进行语言对齐。[CompressV 的原版本对照](https://arxiv.org/html/2602.17869v1#S3)中，无约束 latent 的对齐 loss spikes、Gaussian 约束与 residual anchor 的差异支持这一接口选择，而不是证明平均池化无损或所有自编码器都必须残差化。控制实验固定32帧/64×压缩且省略第二训练阶段，不能把完整三阶段榜单收益全归因锚点；预训练、池化与压缩/投影仍计费，shot-change 采样也不证明事件完整性。细节损失、消费分布或对齐回归时，应保留完整特征、平均池化/选择式压缩或重新联合训练，不把重构通过当下游理解通过。

**Ch14，现Laplacian两段后：** 凸读取还可能在一个更窄的读出合同下限制可改变的结果：固定每个样本的 final embeddings，并用同一 scalar linear head 比较 attention pooling 与 mean pooling，若各样本凸包离均值的最大半径之 RMS 为 Rtilde，mean prediction 标准差为 sigma0，且 ||w||>0、Rtilde<sigma0/||w||，则 PCC 的绝对变化不超过 2Rtilde/(sigma0/||w||−Rtilde)。[该局部定理](https://arxiv.org/html/2602.17898v1#S2.SS4)说明高度同质的固定特征未必能只靠换凸权重获得明显相关性增量；接近条件边界时界会变松，并非全 Transformer 或 LLM 的能力上限。改变 encoder、head 或加入非凸残差会改变比较对象，训练与校准也有成本；任务只需稳定聚合或假设不满足时，mean/softmax 仍合理，需要新信息时应先检查表示与非线性组合，不把更尖的权重当成新增证据。

**Ch30，现静态/动态梯度重新耦合段后：** 多模态持续适配还可以按任务的输入与输出责任分组，而不只按任务标签划分 experts：只按 image/text 输入拆两路，可能把“读图后生成文本”和“读文后生成图像”的更新混在一起；一条受限分支分别维护 image/text understanding 与 image/text generation 四类 LoRA，只更新当前输入/输出对应的两路，其余冻结。[同 total rank 的原版本对照](https://arxiv.org/html/2602.18055v1#S4.SS1)支持这种更新 mask 的局部抗遗忘取舍，不证明四路已经具有独立语义或适应未见模态。冻结仅限制训练更新，不表示 adapter 不参与 forward：原求和式仍包含四路，不能据此授推理免费或旧行为精确保留；额外 adapter 状态、任务顺序校准与随模态增长的容量/计算仍须计费。证据限 SEED-X 的已见图像/文本与有限六任务，生成质量或新任务学习仍需单独验收；责任划分无收益、成本过高或新增模态接口未证时，普通 LoRA、独立 adapter/replay 与 full fine-tuning 继续保留。

## 必要对照追加（不再为未采用数字扩审附件）

- **17835** §5.1 top5% Dolly selection/随机5% warmup、同selecteddata FullFT4epochs；1%构造资料再10%probe/90%align。§5.3同GH200，IProX scoring38–44min+construction<10min=43–51min vs full3B90min、offtheshelf1B40min；因此不是比所有小proxy更快，省时对象必须明确。拟不保留普适速度倍数，机制/quality负侧已足，owner待比较。
- **17846** §5 CIFARcar2K三分支同40Kiter/8checkpoints，1024sample FID参照5K训练cars；gap[1,5]胜dummy是作者局部数据。CelebA1024gray同DDPM100Kiter/batch512，9gap不同midrange有质量–memorization Pareto，不证明midnoise固定阈值跨模态安全。与§3denoiserswap共同支持“端点看似不memorize仍可沿trajectory传中段记忆”，机制/关键反证足，owner待比较。
- **17867** §4.1 A40-48GB约80s，但GCG6prompts、ADAPT10/3groups、BEAST128beam、candidate/iteration/backward成本不同，不以宣传百分比证明等预算最优。486features只前1000latents/层的分层采样，rawactivation/MAE作为proxy；human correlation不是语义因果。保留多trajectory/变异诊断与singleGemma2-2B residualSAE条件，标准必要证据足，owner待比较。
- **17951** §5.1 same projector architecture，OpenVLA7B LoRA50K/batch32与fullFT30K/batch64分列；RoboTwin subset100trials/seed0。Table8multi-independent80→shared98.2→nested98.5支持shared分支，但Table7的cost=#model×batch×steps是估算不是wallclock24×。AppendixH的near-isometry+erroralignment条件不保证所有gradientsconstructive；拟不采用硬件速度，必要证据足，owner待比较。
- **17990** §3.1静态workflow4,973gold/44,757variants，nodecount自动验证+manualsubset；merge被定义为granularity损失，未测真实executionimpact。§5missing/compression/paraphrase三者使Graph/lexical/order/Judge各响应不同；semantic/judge也需gold/rubric，不能由metricbundle判实际任务可靠。标准证据足，owner待比较。
- **17993** §4.2同3epochs/batch64但LoRArank120 vs140平衡params；15–45connections，group4/α100。§4.4单A10080GB，loss序列并行后time/step1.36–4.87×，不是零计算增量；α100大group时Parity与GSM8K退步，反馈强度与group共同稳定。仅有限ID reasoning/softtokenλ0.1control，不授推理普遍更便宜；必要证据足，owner待比较。
- **18022** §5.1单QwenImageEdit60layer/24steps/CFG4/1024²/seed42 PIE700；matchedδk对照支持局部fidelity小收益及δv1.2回退/δk1.15有SSIMPSNR反側。虽然列CLIPscore，§6明确完整editingquality tradeoff未来，不能把保留源图当编辑成功或noartifact安全。只采用K nonlinear/V conditionallinear控制接口，非所有图像编辑更好；标准必要证据足，owner待比较。
- **18093** §4.1 FLUX/HunyuanVideo A80080GB、DiTXL2 RTX4090/FlashAttention，共solver/steps/CFG除原方法特别条件；FLUX1024²50step、video17/45frames分列。Table2AB/AM/DSM消融显示更多skip的AB+DSM更快但ImageReward弱，fullABM交换速度质量。Table3HunyuanVideo17framebaseline76.71s→PrediT27.21s只该设置；某Taylor/Profiling45frameOOM不称allmethodsqualitywin。必要证据足，owner待比较。
- **17798** exact-v1§3实际nonnegative squaredprojection affinity+κ expertconcentration，Eq5仍softmax(αfixedlogits)。熵单调公式dH/dα=−αVar同样适用于固定任意logits，因此原文“温度softmax可能非单调”的解释不采用。Theorem2 uniformexpertmixture/targetaffinity≥γ/others≤ργ与κmin>ρκmax，不由几何正则自动授任意真实corpusloadbalance。§6.1仅350M/1.3B OpenWebText/A100/5seeds，routingcostO(Ndkr) vslinearO(Nd)，§Limit7B+未证；v1摘要本身含2.7B，与已披露实验配置范围未充分对应，不能补造后版归因。潜在projection routing保留，原entropy独占/无collapse保证纠正；因设计反证深入，owner待比较。root 已独核该数学反侧与 v1 摘要冲突。

- **17778 AskingForever（安全，深入）**：§3.1完成判定是Qwen2.5-32B LLM judge，不核原问正确性；同一模型模拟Easy/Hard用户，非真人。§3.2训练5000Alpaca澄清对话的last-user-token residual additive vectors，前9turn施加、第10turn禁用以强制回答，不能称自然效用保持。§4/Tab1两组各250题、最多10turn右删失；GSM8K accuracy只valid boxed numeric answers作分母，部分配置下降20.2pp，输入token包含每轮重送history。价格只是input/output假定比，未测wallclock/SLO/实际账单。§5.1 rank1/16 LoRA供应链分支中GSM8K有效回答≤4，准确率省略，不能授能力保持。§5.2/AppendixA.4直接搜索25处FP16权重bit并改写（N64、top10/layer、≤3turn），作者用A40/H100实验；A6000 Rowhammer可行性援引旧研究，不是本篇真实GPU物理Rowhammer验证。§6防御提示仅部分缓解，few-shot有58×benign input overhead，prompt cache未测。§A.1两台各8×A40/H100服务器，Torch2.5.1/CUDA12.4。必要支持与关键反证已足：参数完整性威胁能通过持续澄清消耗trajectory预算，non-harmful/completion与availability不同；不授所有模型、多轮攻击均无效用下降、实体硬件攻击或生产成本保证。date Submitted19Feb19:21:09Z在Thu14EST cutoff之后，Registered23Feb02:23:22Z给已公开上界，采用公告机制的本窗起点至10:23:22+08区间。尚待实际Ch72 owner/相邻比较和root必要证据与PRE。

- **17937 DSPy instruction optimization**：必要§4.2–4.3/§5.1–5.4实际读足；三源100条混合train、只accuracy搜prompt，同model提案/评价，MMSci onlytest/图转text。Qwen32B COPRO调用频率90→93却成功执行42→12，SIMBA/MiPRO降低调用又延长reasoning；不授少调用即正确或跨family统一optimizer。Tab8 Direct gold-support90.2→67.4与refute39→70.6显示label tradeoff，CoT ordinal/数值focus相关不授单因果。50条SciTab手审中smallmodel的CoT-only成功对应ReAct schema/table表示错误，20errorcases多标签/100subset分别保留，不混分母。§Limit说同seed instruction/单SQL，与§5.7提追加初始prompt与多tool ablation有叙述范围不一致；本次不引用那些未读附件，也不外推通用选择器。标准必要证据足，拟2+1+2=5；实际Ch74 Prompt生命周期已要求task/format/toolchoice/cost联合回归与model/schema绑定，constraint-residual段已有scalar改进可能过度/不足调用；Ch78 parse/schema/semanticvalidation执行独立。拟已有覆盖这些实际论点，不用局部优化器优胜为正文堆名；root证据/具体Existing复核待核。

- **17910 APEMO**：§3.2只是固定weights/decoding/topology下的peak/ending inference分配覆盖层，不同modelalignment训练算法；§4 sharedcap但realizedcost不同，Ollama1B/1.5B/2B、T2/T8，Tab1各block n16/18/20/21/30与1–2episodes不合并成统一样本。§4.2run-level bootstrap只固定config/seed/policy/length，不把episode伪重复。§6.5明确无人类subject，reuse/trust/frustration是作者定义代理，不证真实人偏好；monitor/repair端到端latency未测，traprebound model敏感，externalplanexecute不是全工业pipeline对比。拟采用时间分配与topology正交、后验用户评价权重只是假定目标，不授人类信任或跨模型系统收益。方法/关键反侧已足，实际owner差额与root必要证据待核。

## 恢复后日期受影响的有限集合

实际重新读取本日DataCite20个完整原摘：17674/75/76/81/82/84/86/88/91/92/93/94/95/96/98/99、17743/44/53/73。这是已发现日期受影响主线标题的定点恢复，不扩展770个身份为题摘队列。17753仅30agent透明度目录；17699通用riskcertification未建立foundation/system具体桥接；17773物理flow/Navier-Stokes科学应用暂缓：拟具体EX、日期未核后停止。其余17有具体机制/边界潜力，已请求root独立完整原摘校准；潜力尚不授当窗候选。17692须必要core核parameter-memory backflow是否真的有通用机制而非medical应用数字，不能由owner名称准入。

官方advanced search实际表单提示announcement只支持年月精度；day-level请求返回validation表单，不能据此得到首次公开日。02/19 cutoff前Submitted与23日metadataUpdated/Registered仍不足首公开下界。已作两条官方限定websearch，返回empty只是恢复失败而非零事件；正在有限核day-list可否访问及公告历史snapshot，不用论文Submitted倒填公开。

日期有限恢复现停止：`V3_NATIVE_date_recovery2.json`记录官方day-list HTTP400与公告archive-CDX timeout。root已独立读取20完整原摘并通过17潜力+3具体EX校准；17692确有通用参数-memory backflow，medical只局部评测，不因此scope排除。17身份为2602.17674/17675/17676/17681/17682/17684/17686/17688/17691/17692/17693/17694/17695/17696/17698/17743/17744，缺必要first-public下界；原Submitted/Updated/Registered保在DataCite原响应，Submitted早至01/21而月份ID仍02不能被默认为02/23。只将必要日期隔离，未评分、未采用正文或Books，不授positiveGate；重开需当窗dated officialannouncement或可核其历史snapshot，不泛查全月/全版本。轻量当前abs信号检查单独保实际结果。

**17798/17778 Books推进：** root必要原源与actual owner PRE通过；Ch21 g_e说明后单段+note、Ch72 lifecycle WAF句后单段+note已经实际写入并顺读完整邻接，root实际正文/邻接/自身末注非作者POST通过，窄锁释放。三项17869/17898/18055亦POST通过，总计5处整合；日级仍进行中，不由共享写入数定义完成。

**17937/18007 Existing：** root已实际独核17937§4.3/§5.2与Ch74联合回归/constraint-scalar反侧、Ch78validation，2+1+2=5标准已有覆盖通过；不遍历prompt附录。18007§2.1–2.2、§3.1/3.4/4.1–4.2与Ch36 L374–382两正文已独核，2+2+2=6标准已有覆盖通过。2节点H2008/MI325X8、TP1/PP2、homogeneousDP4 vsheteroDP8/unevenpartition、500iterloss近只为有限correctness，不授exactnumerics或资源等价。新本日原源证据和实际owner支持Existing，不沿旧V2末注代验收。

## 新必要审阅停点与 18145 写后位置

- **18145**：exact-v1 §3.2–3.4/Eq2–8 的 context/generated attention 分离按 token-position 变换后 L2 幅值 concatenate、线性 detector，不是时间频率。§4/Table1 有 Mistral QA 的 Lookback AUROC 高于 Fourier，不采用全指标获胜；§5.3 high/low/full-spectrum 控制支持新增位置变化特征。C.3/C.4 冻结模型 teacher-forcing 已有 response，LR maxiter1000、threshold 用 validation 或 train 的10%，不是实证在线免费预警。D.1 QA→D2T/Summ 迁移不对称；cutoff/padding/model access/labels 必须绑定。未采用 Laplacian norm=Dirichlet energy 的等号。actual Ch66 原 L230–236 residual SAE sensor 与解释测量合同均不含位置频率，Ch76 reader 不接管评估 owner；65/67 相邻交接已读。2+1+2=5，真实 gap 深入；root 必要 source/owner PRE 通过并授窄锁，实际 Ch66 L234 单段与 L5544 末注已写，作者完整邻接/末注顺读与限定 diff-check 通过，锁释放，待 root 实际 POST。
- **18152**：§3.3 Human–AI Parallel 固定 prompt/first chunk，human second chunk 对六个 GPT/Llama continuation，可见 matched population 的 prefix 压缩曲线差异；§4 社会来源与 Wikipedia/Grok 混人类长文不能给通用小长度阈值。Histogram GB 的 binary/3class/7class 数字在已读方法/结果中未披露 heldout 切分，不将其作为部署可分性；长 prefix 的 compression/lexical entropy 解耦只是局部生成统计，不推理真实 manifold。尚待最终限定命题与 actual owner/独立处置。
- **17837（安全深入）**：§V-B 实际采用 DeepHammer profiling/page-swap，把 offline TFL 搜出的 weight 目标放到 vulnerable physical DRAM pages、hammer aggressor rows；CPU i7-3770、Hynix DDR3/Samsung DDR4，5,490,033 可翻转 bits 是 profile，不是 GPU HBM。A100 搜索与 CPU DRAM 物理阶段分开，white-box same-machine 条件保留。§IV 的 keyword loss/aux benign utility 是实际新增，ImpactScore/range/SKIP 借用不计增量；Eq5 relative attack improvement−utility drop 与文字 minimize/minimum 方向有冲突，不变成 recipe。TableII–VI utility 的 Qwen4 反侧及两 target questions不授所有扰动保能力。actual Ch72 L903–922 已有 parameter bitflip/EOS availability，L983–995 已有 aggregate quality 稳定不能排定向 backdoor；L189–203 GPU PTE 物理链不是此 CPU weight attack。具体新损失是否改变长期解释、还是现有完整性/定向验证已覆盖，待独立 Books 判断；不制造物理攻击 gap。
- **18252（安全深入）**：§4.1 classification AutoAttack 与 retrieval 100-step APGD/STE 分开；AT radius 增大有 clean/robust tradeoff。§4.2 quantitative VQA 固定 Llama2-7B/downstream 只换 tokenizer，但 caption/image targeted string 示例是 qualitative，不当 harmful success rate。§5 supervised 更新 encoder+codebook+classifier、10-step CE ε4；unsupervised 只 encoder、10-step feature ε8，radius/objective 不同，不能将 transfer 优势全归因 label-free。攻击失败仍125/128indices变化仅说明 index 稳定非安全必要、变化非有害充分条件。未采用 caption ε4/155 的异常数值。待必要 ensemble 设置及 actual Ch23/Ch72 owner 差额，不读无关应用附件。
- **18297（假设修正/安全深入）**：§4.2.1 每 rollout 计算 conditional likelihood 对比 K=16 同 prompt CoT 混合，length norm 与 clipped reward 不授 exact MI。§5.1–5.2 MBPP 两 visible tests/第三 heldout gate、BigMath 正确或任何 negative number 的 hacked verifier；Qwen2.5-7B 有 small hacked SFT examples/math system hints，1500/2000 steps、五 reward 条件三 seeds。monitor reward 随训练被 obfuscate，MI/oracle 改善但未消除 hacking。A.2 Takeaways 明确 MI 本身不 disincentivize steganography：policy 可读的编码不保证另一个 monitor 可读；3B suppression 经常 task collapse、7B prompt 条件显著改变拒绝率，不能称能力/可信透明统一定律。信息是否存在与 attribute/monitor 可得、计算/elicitation gap 不同，§Limits 未涵盖全部实际开销。待 actual owner 比较及 root 必要证据，非普通未读项隔离。

17 个早提交日期隔离项已实际检查当前官方 abs 页面中的 withdrawal/retraction/erratum/corrigendum 字符信号，`V3_NATIVE_early_signal_check.json` 保存17次200与执行时间，定点检索无命中。仅此当前页检查，不授全部版本/历史无标记；日期必要下界仍不可得，按前述终态隔离，不作零事件。

18145 root已实际顺读Ch66 L226–243/body234与ownnote5544，非作者 POST 通过；末注与本日 Report 已同步。总计6处整合/2项已有覆盖，不定义日级最终候选分母，普通其余待办仍执行。

### 四项局部配置关闭与后续 owner 判断

- **18176** F.1/F.2 共享prefix只有一KV但每candidate仍activation增长，beam需要不同prefix caches；K·N forward复杂度被batch隐藏部分不是消失。TraDo8B/512tokens/block16/N8的24%memory与20–40%overhead仅作者条件，Eq26 ε≪(N−1)Tf是硬件执行假定、Eq27近似未闭合完整图；不采用统一1.2–1.5×speedup或近最优熵保证。高confidence bypass省搜索也改变执行人口。方法+直接成本反侧足，不为缺hardware额外扩审未采用数字；拟具体candidate-lookahead entropy代理与cost权衡，owner待比较。
- **18020** §4三simulation模型族/三seed/RTX4090；real四任务各50expert训练/20testrollouts，不称全部training-free。B.2 OpenVLA-OFT用56action hidden positions，而π0/CogACT使用prefix/cognition单token entropy，因为连续action head无离散概率；这些不是相同action uncertainty人口。γ/α逐task heuristic search，阈值非out-of-sample通用calibration；real不同model的GPU/训练steps不同。Table4 matched injectionrate、direct-addcollapse/meanblend强baseline反侧及同model局部控制足；不采“mutual information必单调”或物理安全保证。actualCh26已有uncertainty-conditioned compute/horizon，缺内部FFN observation reinjection的适用接口，owner差额待必要PRE。
- **18037** §5 finite-difference GR仅扰transformer blocks、embedding/head不动并clip，用原policy actions复用两个gradient，不做新policy采样/importance correction，作者仅经验称可行，不授无偏。AlpacaFarm同GPT4.1Nano label/judge+trainingwinrate earlystop，每method gridsearch，1.5B全pipeline三seeds，strongRM下reset略优于GR。GSM8K格式reward下降但accuracy升，MATH按初始category/level分difficulty不是oracle逐题新能力；LLMjudge分数升与ruleaccuracy分离。C.2/C.4 GR与KL/NoReg所用bestLR不同，RLHF/RLVR tokens/batches分别，不授相等训练成本。GH200 rollout7.4s/update60→150ms只是某配置。连续Gaussian/smoothing/Lipschitz理论与discreteLM实验分账，必要机制/对照/直接反侧足；actualCh31已有KL/参考reset/gradientgeometry告警，但尚未写flatness控制替代KL的新接口，PRE待比较。
- **18094** §4选knownclass image实例，以其他存在labels−inf净化softmax后设threshold或误分类；CLIP/BLIP2 intersection为Hard、symmetricdifference为Simple及人工subset，不证明训练corpus真实未覆盖。AppA从~77k下采样大category到≤6000，sourcevalidation、label语义改名/删除ambiguous/background；yes/no keyword parser有格式人口，不把ID90%认证完整parser。BAP logicalaccuracy还需counting同时正确，不能混成单步reasoning。§5.3/Ethreshold敏感已读，普通主源+关键反侧足，不遍历整套开放/闭模型统计附录；拟模型相对failure slice而非确证training-OOD，owner及独立处置待核。

actual owner 已定点比较：Ch79 L155–175 encoded constraints/semantic translation与成本回退支持18095 Existing提案；Ch72 L912–915 bitflipavailability与981–991 targetedartifactquality边界支持17837 Existing提案；Ch27 L325–326 generator/judge共偏与501–520 failurecurriculum支持18137 Existing提案（均等待root必要source与具体Existing，不主题映射代完成）。18152受控compression/词entropy差异拟标准仅报告，不采用通用来源检测器或“社会统计无评价启示”；root必要source与处置待复核。

PRE已向root提交但尚无写锁：18252 Ch23 encoder-only old-feature-anchor鲁棒替换（codebook/downstream冻结、攻击ensemble和cleanloss）；18297 Ch72 conditionalMI不排policy-only编码（训练反馈/decoder可读性）；18428 Ch24 blind-model与scheduledsampler/parameterizationgain误差分账；17846 Ch24 step vstrajectory noise-specific memorization；18093 Ch24 history多步forecast与J=0才测δ/真实刷新，Alg1启动f_previous未说明不采完整recipe；17809 Ch30正交adapter切空间局部posterior。未为准备PRE写入Books，不等待无关材料继续其他本日项。

### 新实际终态与必要局部配置（恢复后续接）

root实际必要原源及actual正文核：17837 Ch72 bitflip/availability与targeted质量边界、18095 Ch79 encodedconstraint/semantic失败、18137 Ch27共偏与failureproposal→oracle均Existing通过；不声称完整新配方已被书覆盖。18152有限压缩统计Only标准5通过，不采未清heldout的部署分类保证。17809 Ch30 body201/ownnote903已实际写入，作者191–219邻接及note顺读、限定diffcheck通过；root实际191–207与note POST通过，锁释放。18252 Ch23 body182/note1271、18297 Ch72 body872/note4212已经PRE后窄写，作者完整邻接/末注已顺读并释放，root实际POST待核；18297移到Argon两段之后保持原“该版本”指代。

- **18182** §4 heldout是另360 TimeQA/MentalQA人口（answerable/unanswerable各180）；18 ADeLe能力+propensity以RF预测，十模型×三incitedlevel、10fold按instances交叉验证，不是leave-model或leave-incitation。Table4局部加propensity反而降低，2×2PL适宜区间量表/规范rubric只测特定行为，不授内在人格或安全。必要机制+评价反侧足，actual owner待比较。
- **18232** §3.2–3.3/Table1–3 Mean@8是八次单trajectory采样均值，不是ensemble输出；AIME25调阈值迁移另三mathbench，部分配置与baseline持平。遮蔽高confidence历史再contrast的额外branch需要forward/cache，实际read setup没有端到端runtime/hardware披露，标Not Disclosed，不采用negligibleoverhead宣传。熵与正确/错误token confidence变化不证因果或通用校准，必要有限证据足，owner待核。
- **18292** §4.4同Qwen7B/Math7B、prompt/script/Tmax3072；Table3 mirror steps5局部时间15.84→16.88、更多steps不单调，hardware Not Disclosed。实际results未披露solution best-of-K样本budget，top-k50不是utility式的K；覆盖效用针对token非完整正确解。Table1 GPQA/HumanEval有退步，不采用“所有setting均胜”文本；必要机制/反侧足，owner待核。
- **18333** §4 κ由每个length与joint的best LR/seed grid最小成功样本量组成，不是expected sample cost；Transformer在CoT有κ<1，recurrent在Outcome/Aligned CoT可高共享但普通CoT约1，format造成recall bottleneck。lengthOOD相关不证状态共享唯一因果或recurrent普遍更省样本。必要有限证据足，owner待核。
- **18374** §4–5/Table1–2八任务各10trials，SR是conclusiveanswer、不单是物理动作成功；oracle是实验后专家标pushlines/keypoints非线上可得。两个in-context图提高复杂任务但改条件/动作路径更长；2Dgrid接触点误解与pushline具体接口可保留，ArUco/几何/OMPL仍必要，遮挡识别与checker失败不授zero-shot通用控制保证。必要证据足，owner待核。
- **18397** §3/Table1解析roofline对旧π0 Triton RTX4090数据，仅emptylanguage/chunk63/10steps验证，1–3cam理论14.7/22.5/30.4ms低于实测20.0/27.3/36.8；表名Real/Roofline但百分比实际为Roofline/Real，不照录方向。后续设计的chunk50/lang32不同；忽略本地搬运/launch/OS，不认证端到端SLO或控制质量。必要验证反侧足，owner待核。
- **18417** §7明确仅字符TinyShakespeare/PTB、single seed、O(d)验证；子群模板不等所有SU(d)/其他group已验证，parameter匹配不等compute匹配。闭群hidden state/Exp接口是替代算子而非普遍Transformer稳定保证，必要源已足，owner待核。
- **18424** §3/4 agentprofile+video或frames+NODES输入，inference不提供GT graph；路径GT仅供annotation/判分，不能混同输入。A100/A40或API混合、各model frames接口不同，主Table2取testedframe setting最好值；4人各20题不是一般能力上界。Explanation judge有fullgroundtruth而非实际physicaltrace，score四权重默认.25、正负预测条件人口分账，不把多项分数当部署可行证书。后续root必要源与actualCh79有限Existing已通过。
- **18425** §6.1–6.6 verifier 100doc goldstring人口选择高recall模型，precision34.06/recall74.05；oracle有真值且turn>2继续改善，LLM plateau显示冗余与错误反馈瓶颈。输出50initial+50nonduplicate second、verifier budgets10/20/50/100、双retriever两indexes训练/检索与验证均计费，少verifierdoc时更差；不称匹配整端费用/全evidence已找齐。必要反侧足，actualRAG owner待核。
- **18432** §4 A100/T400、fps以一次全400frame生成除总time而非causal streamingdeadline；8GPU训练batch16。FGD Avg为batchmean，S/NS为pooldistribution不可加权合并；VAE缺失损分布而foot物理proxy近不变，headfacing CFG强度与FGD有tradeoff，不认证眼神理解/全部physics。必要实现/消融足，owner待核。
- **18434** §5.2/5.4 Qwen2.5VL7B，.5FPS/200–256token frame/17000token window、64framefeatures retrieval；AKS~16×是滑窗attention稀疏率非全部KEYcache压缩。Table4不同压缩率/quality，有CGbench tokenmerge优于AKS；Table5 PECore整体VideoMME退步、onlineRVS-Movie下降2pp，不采allbenchwin。RRF额外encoder/retrieval费用不能由training-free取消；必要对照足，owner待核。

### 2026-10-05T14:18 后实际闭环同步

17846/18093/18428 Ch24三段及末注已root实际POST通过；18428最终采用增益与去噪误差共同决定放大，不授ν有界必要性。17913 Ch77把raw truth纠正为原始记录后root实际POST通过；18425 Ch76最终并入未全verify文档与relevance≠truth界限实际POST通过。五项自身末注及Report已同步；18094仅OOD支持域定义接口、18397仅roofline/surrogate校准与真实SLO边界Existing通过。当前完成22家族（14整合/7已有覆盖/1仅报告），最终候选分母尚未冻结，其余普通待办继续。

新PRE原源/actual owner定点已root通过并授单段+自身末注窄锁：17835 Ch27 weightedSVD的K-FAC/层局部surrogate、probe/damping与Table12标准SVD控制；18176 Ch24 candidate后forward评剩余marginal entropy heuristic与cost（Eq5 IG−cost而Fig2 caption反写，保冲突不授全局最优）；18182 Ch66 demand-window测量、instance-wise而非leave-model crossvalidation与规范/同源/局部退步反侧。写后实际顺读再root POST，不扩理论/附件。

三新实际写后：17835 Ch27 body830/note1520、18182 Ch66 body308/note5548原源/实际正文完整邻接非作者POST通过。18176 Ch24 body362/note2053的root POST发现ImmediateCost误写执行成本；实际源Immediate Cost是所填位置marginal entropy，本处已改“本轮所填token的不确定性代价”，与真实candidate forward/activation费用分开。Eq5最大化IG−cost而Fig2 caption反写的冲突保留在证据/自身末注，不在正文罗列图号；作者精准句/邻接重新实际顺读及diff-check通过，root最终POST待核。

18176纠正Immediate Cost后root实际局部POST通过；18308 source§2/3/7.4与actualCh17 L458–476的局部orthogonal carry与完整网责任边界Existing通过，不采用有限Cayley exactness或混杂预算质量。18182 §4.1 rubric hand-crafted、GPT4.1做demand标注与§4.3 answer extraction，未证生成题目；正文已精准改“GPT-4.1需求标注与答案抽取仍可能共偏”，原‘生成与判分’解释不采用，root局部再核待结论，不扩全部证据。

17835/18176/18182（需求标注角色纠正后）root实际POST均通过且自身notes/Report已同步；18308限定Existing已同步，当前26家族（17整合/8Existing/1Only）。18037 Ch31 body326/note1300与17909 Ch25 body525/note1583必要PRE后窄写、作者完整邻接及自身末注实际顺读并释放，root实际POST通过。18224（准确§4.3/Table6而非早前§4.5定位）、18307、18230的限定Existing已root必要源与actualCh66具体论点复核通过，尚待报告同步。

18020/18374 Ch26两互不重叠PRE窄段已实际写入：18020 body1105/note1912、18374 body73/note1914；作者完整邻接/末注顺读、限定diff-check通过，锁释放。root实际正文/1097–1119与66–81邻接及两自身notes POST通过，报告/末注已同步；不把既有obs重消费当新鲜观测或contact proposal当物理安全。未主动写LS/索引，不自行切他日。

### 2026-10-05T15:00:35+08:00 诊断暂停安全停点

三批实际13+21+34=68 unique DOI，11具体EX为17848/17875/17881/17808/18025/18026/18029/18107/18262/18266/18372；17930/31合一家族，得到56。加17778为57 arXiv、官方SWE/PSM为59冻结唯一家族。原字段在V3_NATIVE_datacite.txt的dates(v1 Submitted/Updated)和registered；Submitted全在Thu14EST之后、Fri14EST之前，结合已核Sun20EST公告给公开下界，registered只给上界，不当首公开。17早提交潜力日期终态隔离在59之外，3早提交具体EX保持，不重开宽池。

59内互斥：36终态=21整合POST+14限定Existing+1Only，23普通待办=21 arXiv+SWE/PSM。最新17817/17867/17871限定Existing已root必要源/实际owner核通过；原方法整体不授已有覆盖。Report36行/小节V3通过，未日级验收。

普通21 arXiv IDs：17910、17930/31单家族、17951、17990、17993、18022、18071、18420、18116、18131、18181、18196、18232、18292、18301、18333、18417、18422、18424、18432、18434。最近四PRE：17993 Ch17内部高→后token低投影旁路gap；17990 Ch81静态graph metric≠execution限定Existing；18071 Ch26短obs/history≠unseenbelief限定Existing；18420 Ch49共同预算/代理quality与kernel费用限定Existing待裁。最小原源：各V3_NATIVE_html_2602.ID.txt经V3_read_html.py，17993 rows41–60/70–96、17990 rows18–34/48–68、18071 rows50–65/93–104、18420 rows96–124。四项均未写Books、未获终态，无主动共享锁。

必要支持+直接反侧已足的项不扩大附件；剩余ordinary多数已core/局部控制但actual owner与非作者处置仍未完成。按用户诊断要求停止扩下一批，不重置已验成果。

### 2026-10-05 诊断恢复后实际处置（覆盖上方36停点）

冻结59未缩池；旧36有效证据/POST复用。新19安全终态使报告55=29实际整合、21限定已有覆盖、3仅报告、2中心争议。报告§4是采用判断入口，下面仅保恢复位置，不另造收据或全附件队列：

- 新整合17993 Ch17、17951 Ch29、18116 Ch49、18131 Ch28、18181 Ch36、18196/18417 Ch22、18292 Ch20均已root必要原源/actualowner PRE与实际正文/完整邻接/ownnote POST通过。分别保grouping只约束downward路径、shared projector与nested容量、clustermean非matchedrank质量保证、PC/BP目标/理想收敛、RNG/去重/可靠送达、全长recurrence与稀疏read、局部tokenhit及群Exp精确闭包/数值条件。计算、训练/恢复预算与小实验直接反侧近正文，不授production保证。
- 新Existing17990 Ch81、18071 Ch26、18420 Ch49、18022 Ch14、18301 Ch12、18333 Ch22、SWE官方Ch66均已root必要原源及actual限定论点核验；不称全配方已有。新Only17910与PSM由未披露controller/解释假说及公开局限支持，不以类比造长期机制。
- 新17930/31归一家族的PPO objectiveclip→hardratio→KL/nondivergence链、18232 C符号/percentilecontroller方向均经root实际公式反侧核验并终态隔离，不支持正面Evidence或Books；精确纠正与执行/证明需求见报告§5。
- 原始HTML经只读helper抽取，不以原CSS行号作证：17993 rows41:96；17951 75:96/118:137/271:305；18116 14:49/61:107；18131 55:66/78:112；18181 40:88/91:126；18196 40:77/118:119；18232 23:129；18292 194:249；18022 23:133；18301 25:52/90:121；18333 23:87；18417 15:118。核心机制、关键评价与直接反侧足即停止，非全文/全附件审阅或实现复现。
- 官方SWE只支持o3难解特选138人口缺陷/有限回忆信号，不支持整个500污染率或SWEPro优越；PSM原发布meta支持本窗，current July8改文不借作完整历史细节，采用核心解释与exhaustiveness/future明确局限。两项原页和actualowner/处置经root独核。
- 最后四项18422/18424/18432/18434必要源/actualowner PRE全部通过。18424 Ch79及18434 Ch45限定Existing已通过；18422 Ch24 body228/224–236+note2069、18432 Ch23 body281/275–287+note1285已窄写并由作者实际顺读/限定diff-check通过，锁释放，root实际POST待核。14B/5B成本与codec/generator两侧前缀分别限定。仍不可用本段自行授日级完成。

55行V3格式/本地链接与限定diff-check已通过；修正Ch14 StableNode/path及MIRA材料单primary-link格式。格式检查不是语义完成。root日级整体复核待最终59同步，未写LS/索引、未stage/commit/push。

最终内容同步：18422 Ch24与18432 Ch23实际body/完整邻接/ownnote已root非作者POST通过，限定Existing18424/18434也通过。Report现59逐项=31实际整合+23具体已有覆盖+3仅报告+2中心争议，普通扫描/候选证据/Books待办0；日级独立整体验收待执行，未由此自行记完成。59行V3格式与本地链接已通过，来源14行、17日期隔离与两中心争议重开条件仍保留。

2026-10-05T18:16:50+08:00 root最终日级非作者语义通过：实际六部分/最终增量证据与31真实POST已核，59=57arxiv+2官方、31/23/3/2互斥、59证据小节及14来源停止/17日期和中心/历史目录隔离一致；复用68题摘/11负侧分批实际核，不把宽库存当全文队列。Report同步Complete/独立结论通过，普通0；隔离项不授positiveGate。完成态V3/本地链接与限定diff-check重跑通过；句末标点/终态保留项显式字段已作格式修正，不改变语义裁决，root随后复验完成态后维护LS/index，不自行增加全局完成数。
