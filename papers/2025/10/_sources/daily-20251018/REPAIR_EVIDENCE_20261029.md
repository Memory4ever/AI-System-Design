# 单日证据增量：writer实际阅读

只证明具名采用域，不代表整篇/附件全读或复现。精确原件 `REPAIR_CORE_2510.<ID>v1_20261029.html/.txt`；HTML版头有精确v1标识，作者页上编译日期不是公开日。共同公开日联合界见 discovery JSON；无性能跨配置合并。

## 14826 Tool-Use SSM（拟7分，深入中）

实际连续读§2定义/2.1–2.4、§3至3.2及B.1必要证明开头。有限状态空间S、输出α质量最小support无界增长，CoT或一次工具观察后仍由固定状态输出；Theorem2.1不能外推任何长文本都不能生成。Theorem2.2是存在memory oracle及任务相关轨迹、string-matching学习算法的构造，不是SGD在任意任务必学会；外存初始含输入、指针读写/移动、交互输出允许反复回读改变系统记忆边界。算术exact trajectory/answer，乘数限制1或2位；Hanoi报最好seed且跨seed敏感，不能拿摘要“SSM优于Transformer”当统一质量成本比较。工具存储/调用成本未包含在固定模型状态中。后续只需补B.2与coding/讨论的直接反侧，不重全附录。

## 14751 FSP（6分，标准完成）

实际连续§2.1–2.2/Eq1–13、§4.1–4.3/Table1–3。用prefix backbone预测长未来摘要，非把未来直接给inference；multi-hot+BCE或独立reverseLM隐态+l2，单辅助头不等总训练便宜。3B250B tokens、8B1T tokens；同data但明确非含teacher的iso-compute，不能授免费改进。single-head MTP/DS-MTP是对照限制。8B GSM8K NTP71.6%高于FSP70.5%，3B DS-MTP多数task更高；三seed表中math/code为pass@16，不混pass@1。收益只是未来监督形式的可选分支，不保证长程规划或在线看见未来。硬件与训练详参未用于性能采用，端到端加速不适用。Books实际owner/邻接尚待比较，未终判已有覆盖。

## 14865 Midtraining（6分，标准完成）

实际§2–6及§7必要解释，70–410M Pythia/C4/128B固定总token、cosine/AdamW；五mid mixes，SFT各checkpoint超参搜索后5seeds，C4 loss只是原分布遗忘proxy。specialized-general混合与纯domain比较的starting point不同以避免数据重复，不能把Table3全归因比例；§6早引入也改变specialized曝光token量，timing×weight不是正交因果/无条件plasticity定理。v1只支持code所试范围timing更重要/有交互，不反投current v2“late不可能补偿”的强表述。FLAN等不匹配mix收益小，CKA最后层稳定只是关联。Books待实际owner比较。

## 14961 Recurrent-depth diffusion-forcing sampler（7分，深入完成）

实际连续§3.1–3.5/Alg1/Remarks3.1–2、§4假设/4.2–4.3结论及§5.1–5.2/Table1–2。Huginn0125要求input injection与中间态可解码，cache sharing虽非严格必要却决定r×状态内存；Coconut式不直接支持。wavefront推进新token同时精炼旧latent，prefix连续收敛才freeze；阈值是局部启发式，前位晚变化会级联失稳。收缩映射假设下归纳可收敛到AR固定点，真实模型未证明contractive；不是任意随机sampling的分布精确性证明。理论runtime结论限W≤饱和阈值/共享KV/忽略部分执行开销，不授生产等时严格普效。真实A10040GB/batch1/HF dynamic KV/CUDA events、模型变体及四bench；4–5x相对static ARr32，adaptive/selfspec基线更快，HumanEval22.56→20.12降2.44pp，不照抄“约1%”。precision/输入输出长度和并发SLO若未披露为Not Disclosed，不采用跨配置吞吐保证。Books待owner比较。

## 14826 后续必要反侧（深入完成）

实际B.2指针oracle/有限transition lookup的构造段、§3.3及§4；正定理依任务轨迹覆盖状态-符号转换并以外存承载增长，不是现实SGD的统一sample/computation bound。coding是合成依赖graph传v10变量的bug，不是通用SWE基准；Mamba790M/Pythia1B、8192训练context，transformer各条件择更好RoPE配置，不能推出所有真实repo/所有Transformer优劣。理论与实验足以采用“系统边界改变固定状态瓶颈”，不采用无需外存成本的无限泛化。B.2完整后半概率证明不用于新数学承诺，未全读全proof/全附件。

## 14557 MX+（6分，必要深入完成，原事件去重待核）

实际§4–5/Alg1、7.1/7.2–7.4必要。32元素block的最大幅值BM exponent可改mantissa，但须small-block flush与额外8bit index，平均4.25→4.5bit，非纯4bit/标准MX硬件直接无修改。转换BF16路径在A6000，native-MX软件处理在5090/CUTLASS，额外sparse MMA/寄存器交换有费用；7.3把vLLM执行时间定义为aggregate GEMM，不是完整服务墙钟。Llama2-13B/4请求/1024in64out，prefill1.54x慢、decode6.71%慢，不能用“negligible”抹掉phase代价。RTL28nm/AccelSim硬件结果不是实芯片；精度评估各种OPT/Llama/Mistral/Phi/Qwen与KV/权重/activation全dot cast、BF16norm，同质量与速度不混。另ACM DOI须核更早发布，未判本日新family。

## 14614 FAL（7分，深入完成）

实际§4/Eq2/4.2、§5及§6.1–6.4/T1–2。各层MHA保留residual，MLP改读LN(Xi)+首层attention的LN，局部加和再一次allreduce，不是原网络等价重排。FAL+保原层间依赖另加首层信号，质量分支不继承FAL通信减半。RTX3090PCIe/H200NVLink2–8卡、GPT变体774M–8.3B，单GPU3090/4090/A6000；OpenWebText/Pile/SuperGLUE。774M平均相同却BoolQ/ReCoRD/WiC等反退；FAL+更低PPL不保更高SuperGLUE，MLM/causal称谓混用不补齐。训练from scratch与受限Alpaca不同LR验证，不授任意checkpoint无损替换。未用未核appendix inference数字作采用。Books需具体架构→执行分责，非给Ch37只记一个allreduce消失。

## 14420 Instruction self-supervised RL（6分，标准完成）

实际§3完整/§4.1–4.5及Limitations。GPT4o生成约3k seed的多约束instruction，hard规则/soft binary model；有约束响应作为positive、未给约束响应作为negative只是pseudo-label，不是必然满足/违反。算术均值reward不保全约束同时满足，curriculum变训练人口。Qwen1.5/7B/Llama8B/R1distill，人工各50四/五constraint组校准KT/PC，未认证全分布；WritingBench等退步保留，32B未验。所谓label-free不等无GPT4o/seed/人审，模型分类0.2s不授端到端119x。仅报告当前recipe与局部证据，是否存在长期gap待实际owner比较。

## 14256 Identity-GRPO（6分，标准完成）

实际§3完整/Eq1–10/§4/T1–4。10k auto/5k human pairs，human-teacher筛auto只留48%，混合采样由auto→human；original>generated是构造假设，VLM投票与GME过滤不保identity真值。BTT含tiesθ5，reward Qwen2.5VL3B+vision更新；8A100/VACE&Phantom1.3B/训练25step33帧416×240、评价50step。增组数与异初始noise共同帮助group variance，但参考图/更改prompt/分辨率与样本费用都变，非一般多模态GRPO配方。500human RM benchmark与100生成sample/user vote分账，18.9%是自RM分数相对增益非真实identity保存率。未核像素/运行；现有通用pseudo-label/奖励人口边界可承载，Books待具体比较。

## 14388 Hi-Agent（6分，标准完成）

实际§4完整/Eq1–5、§5设置及5.2–5.3。hierarchical subgoal→atomic action、交替GRPO；所谓environment reward是与oracle action type/坐标阈值比较，另72B judge估feasibility，不是真实终态成功证明。Gn→nG比较枚举树与单步局部训练，不是所有trajectory GRPO必需指数rollout。Qwen3B×2、4A80080GB/22h、约1200手检轨迹；AitW仅General/WebShopping各96，不能称全AitW。hierarchy-only60到87.9、SFT67.6不能隔离全部监督/预算，AndroidWorld3B26.3与72B+7B56.5不同资源配置。split按template/seed仍非任意任务泛化；Source足以收窄局部信用分配，不授无critic最优/通用SOTA。

## 14657 DBP-MAE（6分，标准必要域已读，评价尾待补）

实际§2/Eq1–5及§3.1、Discussion前段。每层R独立decorrelation更新并最后融合WR，encoder-only/decoder导致不稳；BP与DBP各自调LR、10%ImageNet/ADE、5初始化，wallclock排除validation。37.3%更慢每epoch却21.1%更快到baseline阈值，2H100/2EPYC9334；不能把epoch减半当训练减半或carbon估算变通用能耗。截断的§2.2尾、§3.2–3.3和Discussion局限尾须定点补读后才关标准层，不重整文。

## 14977 Terra（7分，深入完成）

实际§3完整/Eq1–9与§4.1–4.4/T2–3。point position+feature latent、P2G-VAE→固定3D Gaussian，joint position-feature flow；训练LAP最近noise匹配改变transport coupling不是物理groundtruth，condition点在去噪固定/concat，历史区域累加仍增长。ScanNetv2/958train243val，输入RGBD+poses，2.4m方形crop、VAE36k/flow100k+40k，不能与RGB-only reconstruction等信息比较。几何一致来自同一静态场景渲染，不是action-conditioned dynamics/真实物理/无界一致性；图像FID/KID低于Prometheus，position perturbation损reconstruction但助generation。长期空间state与生成器共享场景接口可采用，不能把论文名world model授transition/永久loop closure；未看gallery像素/核实现，硬件precision时延未披不用性能宣称。Books待Ch25具体owner/邻接。

## 14979 NEO（6分，标准完成）

实际§3.1–3.2/Eq1–2/§4.1、4.3必要ablation设置与A3限制。PEL两conv/32patch，新增H/W QK维度与zero-init K使初始保原text通道，T/H/W独立freq/index、image双向/text因果mask；不是免费position重标或从零训练全部语言能力。Qwen3-1.7/8B、prebuffer12/6层、参数约+10%，pretrain冻结LLM只训新增路径，mid/SFT全训；345M+40M+4M与主表390M量级不混。16×8GPU80GB型号/precision未披，smallablation20M+2M与全规模分开，Table3部分ChartQA/InfoVQA反退不宣单调；A3明确只image-text dense，video/embodied/generation是展望。表示/位置隔离与升级artifact可长效，Books待Ch23具体比较，不采用通用native胜modular宣传。

## 14830 RL-100（7分，深入必要域完成）

实际§3.1–3.4/Eq12–22与Alg1前段、§6.1–6.5、§8未来边界。共享environment advantage跨denoising steps、chunk reward/γ^chunk，IQL critic+learned transition的AM-Q门控只代理提升，5%阈值不保证真实monotonic。IL→offline候选→采集→重训/online与consistency student分责；OPE/teacher持续更新、encoder冻结条件与重置成本不能省。v1明确400DDIM/400及CM500/500，非currentAB1000/1000；未用summary凑总trial。zero-shot92.5、few-shot86.7/新增1–3h、physical95各不同人口；单步生成非控制环总时延10x，实际episode1.05–1.16x且模态/策略路径共同改变。futurework明确复杂遮挡/变化布局、autonomous reset仍待，不把100%有限trial或2h运行当家庭/工厂任意安全部署。未读全Appendix/视频/代码，硬件precision/全SLO未用于performance采用。Books需具体比较offlineOPE门/一致性部署权限。

## 14943 LaSeR（6分，必要数学反侧深入完成，受限采用）

实际§3.2/Eq6–14、§3.3/Alg1/3.4、§4.1与4.3–5.3，3.3首次截断已单独补完整。末token logit以外部verifier标签作MSE，可在额外一token求值给代理；reference均值校准/unusedtoken选型/正负class reweight与warmup/advantage混合都不是无监督自证。Eq10把zc/zi都赋exp(1/β)与Eq8仅正确label得1冲突；正确Z=1+p_ref(z_correct)(exp(1/β)-1)，小p还须控制指数乘积。该具体反侧由sole reader R11独核成立，不采true reward恒等式或天然Z=1。OT3B/Qwen7B/ORZ7B/DeepMath/五mathbench、T1/topP1/max8192；verification剔除无final答案，不能与全样本accuracy混。generalreasoning用modelverifier仅65–70%F1，advantage混合退步而关闭；零额外token是未来变体且偶发续写不稳。受训proxy可仅报告，中心推导保留争议/更正重开，不用降分抹掉。

## 14635 ATGen（6分，标准完成）

实际§4完整/§5.1及§5.4末用途/5.5直接反侧。IO正确由goldcode执行、attack须正确IO，adversarialcode须过当前test且失败gold suite；所谓自然bug仍来自采样/筛选，不能由无手写mutation授真实生产分布。adaptive只在原bug已能攻破才花采样预算；3000APPS/Codeforces→16822train/911test-pairs，难度按Qwen7B初始攻击率分层，不是独立固有难度。retry10→30 adversarialratio17.1→23.7、attack47.96→49.94同时IOacc74.09→70.69，不能只报更强攻击。generatedtests作为新RLreward是proxy，训练阶段仍依gold tests/solution；未认证无gold任务正确性/所有漏洞覆盖。缺省硬件/precision/端到端费用不采用数字效率，Books待具体数据/评测owner。

## 14620 CodeSeq（6分，标准完成）

实际§3完整/Eq1–2/§4.1–4.2与4.6后段/4.7–4.8。有限数列5–7test及教师对两个example输出的一致性不证明通项唯一/所有n正确；反思合格是可执行测试代理。passrate估solvability依采样模型/N，CSSR=-λlog(sov+eps)+(1-λ)正确自生case比例，只在alltests通过给奖；sov0/自生case数0要实现定义未核不能补。5487SFT/1543RL与Tulu3混入、Llama8B/Qwen7B，200新GTG与三close/三OOD，reported多seed均值但不虚构seed数/算力匹配；反思轮数越多也改变token/难度。保留稀疏难度估计/测试oracle的边界，不将samplepass称数学归纳证明，Books待实际owner。

## 14526 Noise Projection（6分，标准+中心反侧完成）

实际§3.3、§4完整/Eq3–9、5.1–5.5。prompt-conditioned noise projector+VLMtoken RM、VAE KL约束及reward差loss是受训重加权，不是原SD条件分布精确恢复；其将训练noise称sample-specific deterministic/更窄space不能证明高斯独立采样不存在，post-selection的条件子集也不等原训练prior。loss名quasiDPO依RM可微分，不是直接偏好logratio理论。SDXL1024/A100，singleprompt及各五prompt混合，RMseed0–299/训练0–49或99、unseen350–499；unseenseed非unseenprompt。Qwenjudge兼RMteacher/caption、ImageReward另proxy，全图无真实semanticgold；自集合split-FID/IS不认证真实data质量，原文明确diversity降低。保持baseweights不动仍新增训练/RM/前向，不能授权免费/任意prompt泛化或KL防所有rewardhack。Books可仅受限prior-guidance原理，不采用上述强因果。

## 14453 Natural Language Tools（6分，标准完成）

实际§2架构/§3完整协议/§4.1–4.4与§5.8–5.9。YES/NO列举工具+parser，仍是输出格式与parse合同，不是无schema；独立selection与response模型改善任务干扰却增加无tool时第二调用。两个各16合成input/10主模型×5API重复×两prompt变体=6400，非6400独立真实任务；API错误排除重试，不保可靠性SLO。只有single-turn parameterless selection，不支持argument grounding/副作用授权，多工具exactmatch非执行正确。31.4%token降包含input减少/output增，不等latency/费用通用降；GPT5方差反增。心理健康语境只协议压力测试，不采用任何临床/危机响应效力。Books待Ch78真实选择/参数/执行权限具体覆盖。

## 14349 VaCo（6分，标准完成）

实际§3完整/Eq2–3、4设置及4.1/4.2/4.3。MTQ→VAL拟合各frozen VFM、MSE+InfoNCE，TGM屏蔽MTQ组间访问/仍读image；只是信息流隔离不证明task不干扰/teacher真值，causalperception这里指因果mask顺序不是因果识别。PT训projector/MTQ/VAL，SFT再训LLM，部署不调用多VFM但仍新增query与forward；LLaVA Vicuna/Qwen7B、LLAVA558K/Cambrian737K+ASV2、8H2098GB，VGGT对照不隔离全部数据/算力，不授几何是唯一bottleneck。现有多teacher/representation派生监督与权限链可承载，实际Books对比后再终判。

## 14300 AdaMoE（6分，标准完成）

实际§2.2–2.3/Eq3–7、3.1/3.3与3.4。π0 action expert upcycle shared+routed，router topk选择、scaleadapter加上softmax权重；最终可能非凸/负scale，router仍参与weight和taskgradient，不是完全隔离优化或保证避免collapse。LIBERO/RoboTwin19，top1/4expert较好不授普遍最优，λ过大/小反退；ALOHA双Piper450demonstration/四task各50trial，50→71.5是21.5pp，不是21.5%相对改善，训练预算/置信未支持全域。框架是action模块容量分支不等全VLAMoE/实时SLO，Books待Ch21/26owner实际论证。

## 14200 RLSR（6分，标准完成）

实际§2.3–2.4/§3.1、§3.2叙述与§5。embedding cosine作为reference-answer奖，不保证事实/数字/否定一致；MiniLM33M截512与QwenEM8B32k不同信息/成本。前称base、设置又采用instructiontuned variants，不能宣从未对齐base替代SFT。Llama8B/Qwen7/32B、Tulu/Infinity各100k；SFT+RLSR额外训练非iso-FLOPs，18bench有9/18等非全指标提升，Alpaca/Arena judge排名不证明alignment真值。直接RLSR与混合recipe各有适用，不把SFT=仅记忆/RL=泛化当定律。Books待实际owner比较，未采用更大规模扩展。

## 14179 Virtually Being（6分，标准完成）

实际§3/3.1–3.2、4.1与4.5–4.7。4DGS重渲多view/camera及relight给定制数据，ControlNet前40%step/前25%block与subjectfinetune/regularization共存；75/160相机采集、两人各256+128relit/27joint视频是真实制备成本。联合训练与独立subject模型mask-blending分支不同；genericlayout先生成→segment扩满画面→同seed10%layout后每subject单独预测再混，既非权重merge也非任意遮挡/身份精确保证。混合AdaFace .320低于joint .337，18人60prompt偏好不等真实动态/永久identity；估计camera误差不作物理认证。未看gallery/视频或核实现；source足以保training data vs runtimecomposition成本，Books待owner。

## 14095 Recursive Latent Space Reasoning（6分，标准必要完成）

实际§4.1四机制/式2–4、4.2实证文字及§5开头机制分责。inputadaptive recurrence按graphdepth、显式每步算法state监督、四factor argmax后reembed与训练corruption纠错；不是任意LLM无标签latent思考，受控modular arithmetic/两层16head256hidden、N≤32train与best-hyperparam基线。continuous→discrete改善支持锚定分支，但监督/分解接口是任务已知，不能把所测OOD近满分授开放语义/真实推理。机制干预未全读/不采用细电路因果或唯一解释，hardwareprecision/真实latency未披不采免费效率。Books待现有latent/recurrent论证具体覆盖。

## 14657 定点补读闭合

实际补§2.2融合WR完整尾、§3.2–3.3及Discussion完整局限尾。DBP fine-tune validation loss略差(p.069)、mIoU .185→.196是1.1pp/6.11%相对，不能混；decoder不稳与长期固定DBP LR/衰减主LR不匹配导致末期发散，earlystop/同schedule只是建议。结论限小数据ViT-MAE、额外R内存/更新与LR调参，非通用训练优化器。标准层完成；未采工业图像领域效力作本项目机制证据。
