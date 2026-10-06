# K6：冻结池必要core与actual owner，待root独核

仍57/108安全终态，51普通。本包准备不计完成。精确v1题摘已准入校准；只核采用命题、决定性控制/反侧，不扩证明/附件。原坐标为`V3_BLOCKS_2602.<ID>.md` blockID，非物理行；未运行代码/复现。拟I4/E1/D1，其中21919只保有限经验不采用失效保证，21633中心frame问题交root决定。

## 21628 RuCL — 2+2+2=6，拟Ch33窄增量

[v1](https://arxiv.org/html/2602.21628v1)22–70/77–90/157。Teacher读取GT生成通用rubric，先用初始policy 2000rollouts评每条适用性a和适用条件下成功s：coverage>=.99后保六条，再以条件成功率Σas/Σa分easy/hard。该人口是**初始模型/条件支持集**，不是每题固有难度。Bernoulli reward CV=√(1/p−1)只描述reward，不等policy-gradient可靠性，原43所谓gradient CV不采用；训练51未明示online applicability如何做分母，不补造。

Hard权重起初0；所有easy rubric的batchmean连续w步>=τ才启动linear/sigmoid ramp。这是reward-component课程，不是重排task/data；gate仍同源judge的过程达标代理，非truth或避免lucky guess证书。Table3同backbone/data outcome-only59.14/uniform59.29/linear60.79/sigmoid63.94，但LogicVista uniform50.11>sigmoid49.66，非全指标胜。α.7局部最优、.5/.9退，窗口10不如20，30近似，不授阈值定律。

73–76/124–126：Qwen2.5VL7B/ViRL39K，teacher Gemini3Pro、judge Qwen3VL235B-A22B、H200/verl、batch256/global128/G8/temp1/KL.01；GPU数、precision/完整墙钟未披露。生成20条→2000rollout→六条、每response rubric judge、滑窗及调参全部费用；初始difficulty随policy drift可失效，157承认固定分层限制。

ActualCh33 1625–1661已有版本rubric、共享偏差、token credit、pool admission/retirement；1599–1606是task generator课程，378–380是题目sampling。尚缺**先按适用支持集定义rubric初始达标率，再以持续easy达标门开启hard reward weight**的controller。拟rubric段单段，不采用gradientCV/所有过程都真，保outcome-only/staticweights/随机coverage及gate漂移回退。

## 21633 SC-VLA — 2+2+2=6，拟中心state-guide接口争议，不写Books

[v1](https://arxiv.org/html/2602.21633v1)39–77/84–115/145–162。中间DiT token分预测progress和relative physical state，监督MSE；冻结base action+SAC residual读取(s,p,Δs)，progress大时减弱direction reward。不是无外部监督：StageI示范p/Δ目标，StageII仍r_env+c。动作16queries与worldtoken不是physical consistency证书。

**采用中心接口冲突**：50–52 Eq8平移target Δs_pos=R_tᵀ(P_t′−P_t)明确local frame；68–71 Eq13 Pgoal=Pt+Δshat_pos、Eq14 dot实际(Pt+n−Pt)与该local方向，没有R_t旋回world。非identityR时两向量不在同frame，可产生错误/反向shaping。此处直接决定把预测未来转成环境reward，不能静默补R或只称外围符号。请求同版实现/澄清Δ与P坐标、实际reward与Fig4对应；未取得前不采用“state-guide物理一致”或全文精确配方。

ManiSkill四任务100demos/各50eval，72→SPI82→OAR86；PlaceSphere1无新增。Fig4静态guide晚期失败支持退火有限经验，却未解决frame接口。ARX5真机只SPI（60demos/任务20trials），不能移用OAR真实部署。成功episode长度不是失败-inclusive吞吐。L40/50k/B32/seed42；SAC seed0、500k/600k/3M各任务和warmup预算，表没有含全部启动墙钟。ActualCh26 1094已有learnedprogress correction/校准与无邻域回退，532 stop/progress需fresh视觉验收。记录有限经验，不用Only隐藏中心冲突；不因本frame问题否定所有SPI经验，是否可独立收窄由root裁决。

## 21818 SkyReels-V4 — 2+2+2=6，拟Ch24跨流编辑合同窄增量

[v1](https://arxiv.org/html/2602.21818v1)29–65/97–108/117–142。Video/audio两同宽MMDiT分支，video预训/audio从头，两路共同text条件与额外crossattention；audio先更新再用新audio更新video，共同t训练两flowloss。音频218tokens对应21video frames的RoPE缩放是对齐prior，不是实际同步证书。

Video condition VAE latent+binary preserved/generated mask并入noisyvideo channels；53–55明确**audio全程从scratch生成，即使video某region被保留**。所以视觉编辑mask不能继承为全影音preservation合同。负RoPE conditionoffset不是所有token的真实timeline；低清全部frame+高清keyframe+refiner是额外级联，不是native高分辨率只一次生成。

2000+prompts/50专业评价者Likert五维和GSB偏好，仅有限厂商评价，未披露每模型人数、顺序、CI、matched sampling/version与费用。无architecture ablation，不能把ratings单归crossattention或宣称所有声学同步最好；VSA局部3×attention不等整体质量预算速度。双分支、AV数据训练、low/highkey生成与refiner、VAE/所有采样费。ActualCh24 71局部video mask不保证非mask零变，274–275已有audio history/target噪声支持；未明确**联合生成的各流preserve/regenerate集合必须单独声明，video mask不授权audio原声保真**。拟该接口单段，原独立音/视频编辑与joint-regenerate回退，不采同步/真实编辑保证。

## 21897 Task-aware Heterogeneous APIs — 2+2+2=6，拟Ch36执行完成界面窄增量

[v1](https://arxiv.org/html/2602.21897v1)75–100/104–130。任务wrapper返回不解依赖：每native async library operation注册event/counter，taskfunction已返回仍推迟dependencyrelease，polltask等全部counter0才完成。Blocking API变async+task suspend/resume，不阻塞CPUexecutor；runtime仍拥有buffers、event寿命与异常。Triton AOT cubin/DriverAPI免Triton解释runtime并不免nativecontext/stream兼容，CUDA/SYCL/offload仍分别编译和memory API。

GPT2四粗粒度GPUtasks的forkjoin与task接近；混合custom kernel+cuBLAS优于全手写说明kernel成本也重要，非任务DAG普遍更快。MN5 H10064GB单node/context256/1.5B（其他sizes）与112core CPU/256GB，precision未明确。CPU MKL/libomp+PoCL oversubscription用公共nOSV线程executor缓解；**细粒度GPT2 64–2048tasks的PoCL仍差，即使统一线程池**，launch/taskgranularity是另一瓶颈。HPCCG仅辅助执行边界，不收领域结果。同步/poll/event bookkeeping、nativecalls、executor资源总费用。

ActualCh36 330–343已functional collective异步readiness、buffer lifetime/order，但尚缺**普通task返回与内嵌异步多API计数完毕的分责、共享CPUexecutor只能解oversubscription不能消细launch**。拟此处单段，未宣称interop统一语义；原显式同步/forkjoin/coarsetask与vendor library回退，Ch49只交接kernels执行。

## 21919 NESS — 2+1+2=5，拟具体Existing Ch30，仅有限经验

[v1](https://arxiv.org/html/2602.21919v1)41–96/99–112/138。以输入矩阵的小singular basis U固定，V可训练，ΔW=UV。有限单layer bound假设pastinput完整support与**显式spectralnorm上界**；77–80却称standard weight decay实现该hardbound，L2 penalty并不强制给定norm，故不采“by construction bounded interference/zero forgetting”。Algorithm1采**current D_t**而前文I_t指pastconcat；89 covariance积累没澄清取哪些stage，不能补成完整pastoracle。即使旧层输入扰动小，不直接约束上游层同时变化的全network输出。

五seeds/AlexNet CIFAR10/ResNet18多dataset和MiniImage20，bestLR/SGDm或SAM；task-specific heads/biasBN另预算。SGD BWT近0但ACC72.46<SGP75.99/Mini63.72<DFGP68.64，支持有限保留/适应冲突而非保证。Nearlyfullrank某层不总廉价，covariance+spectralrebuild、previousdata可用性、regweight校准与stage回归费；hardware/precision/walltime未披露。

ActualCh30 781–793已经small-input/probe subspace保护只是proposal、表征漂移、谱分解/训练代价及独立retention gate，不授固定线性子空间完整保护。**拟E有限低干扰support经验**，明确隔离源hardbound保证与past/current输入identity；不因外围theorem错误隔离全部有效实验。若root认为source中心必须D，保原有限经验与中心争议并存而不写Books。

## 22013 RobustVisRAG — 2+2+2=6，拟Ch23单向辅助分支窄增量

[v1](https://arxiv.org/html/2602.22013v1)31–80/表3–4。Encoder增加one degradationtoken，能query全部patch，但patch不能读它；clean/degraded semantics alignment+distortion type triplet+orthogonality，retrieval另contrastive，generationLLM冻结只adaptvision。**辅助支路只train，infer丢弃**，不是在线增加qualitysensor/gate。原SCM S⊥D与cosorthogonal不是可识别统计独立，72/79声称do(D=d0)近似不采用因果证书。

DVisRAG362110train/3607syntest/1891controlled print-photograph realtest，synth12×5随机degrade保QA并不保所有readability，真实test未参与adapt。MiniCPM-V2.0retrieval/V2.6gen，MRR10与generation 5%numeric tolerance分账。Paired删alignment/uni分支有限反侧支持该training组合；两阶段restore真实top1 40.42<原42.99/retrieval53.59<56.47，full55.39；SigLIP适配clean71.52→68.84，非任何encoder都改善。附录hardware/precision/seedCI未在必要正文披露，不授性能普遍性。Extra trainingtoken/Q/data，inferencebranchdrop只是架构不加，不是profile确认零成本。

ActualCh23 575–594分taskcontribution与sample reliability但gate在线；37–51保source/modality身份。尚缺**仅训练的nuisance汇集支路可读semanticpatch、semanticpatch不可反读aux，部署去支路而独立验收保留表示**，不是增模态或因果真值。拟相关representation段窄段，不复述RAG流程；clean/degraded regression、原encoder/restore与重新paired适配回退，额外训练及infer执行校验费用近文。
