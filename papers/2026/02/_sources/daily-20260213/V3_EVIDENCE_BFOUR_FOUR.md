# 本日B必要证据：10584 / 10609 / 10615 / 10623

精确v1，四项准入已独立校准，日期均在已核119包络。当前abs轻量核无withdraw/correction声明；10609/10623有窗外v2，不因版本号展开比较，不采用后版正文。以下方法/关键对照/直接反侧已root独立核；10584/10609/10623仅报告通过，10615已窄写Ch36 1575–1577与末注1773，实际正文/邻接已获root非作者POST通过。不授日级，不称第二人全读所有表格/附件。

## [WW-DP-SGD](https://arxiv.org/html/2602.10584v1)

5（2+1+2），DP安全声明受影响深入。§3.1–3.3：固定层权重矩阵谱tail fit估ζ，EMA后向2–6经验health zone/中心4调log C并sat/clamp，只用已DP迭代而不再读当前raw norm。C与Gaussian std σC联动；K周期probe与SVD不是免费，全层/大模型成本和proxy有效性未证。§4/L299–318为条件post-processing/adaptive composition：要求底层每步实际是compatible Poisson Gaussian mechanism，不能由阈值来自DP输出推出任意实现仍DP。

Alg1/L253–262实际写Poisson后除随机|Lt|，空batch另跳过。没有读取实现/检验该随机归一化是否与accountant同构，不背书完整DP实现，也不在此未经证明宣称算法失效；可采用的仅是“已成立底层DP→输出参数后处理选下一阈值”条件命题。Ch72实际493–503已承载sampling/normalization/empty batch conformance，398/407承载post-processing与独立utility；无需制造安全原则diff。

§5/Table3：MNIST/EMNIST/CIFAR10/100/ImageNet100，CNN/ResNet含可能small替代配置，固定q/T/δ与σ预算扫、5seed mean/std；Table3 WW 95.99±.08/89.96±.18/73.89±.89/45.10±.90/65.50±.60只属于各自视觉protocol，不授LLM。Table5 severe-skew对手参数推荐值 vs默认controller，α=.3 WW57.28< AdaDPIGU57.29，不单调dominance。§6/L492–516明确谱proxy不是raw clipping-bias/gradientnorm/泄漏估计，smallmatrix拟合可能不稳，新增controller tuning与SVD成本，privacy取决于实际采样/噪声。hardware、precision、精确各模型variant与token/SLO不适用或Not Disclosed，utility机制因果不是定理。

拟仅报告：保留具体spectral-controller与有限经验取舍，成熟DP后处理不计新增长期知识；没有普遍spectral-zone成立条件，不改变现有DP runtime合同。原源 V3_BFOUR_CORE_0.txt Source173–298；V3_BFOUR_METHOD_0.txt Source299–318；V3_BFOUR_FINAL_0.txt Source363–387/492–516；V3_BFOUR_LAST_1.txt Source388–430。未运行代码/复现，不以可选artifact缺失叫blocked。

## [KPO](https://arxiv.org/html/2602.10609v1)

5（2+1+2），标准。§3/L123–159：token log-ratio作为latent random walk、Gaussian观测噪声；左到右Kalman predict/update用P/(P+V)，zero prior logratio=0，exp平滑输出代替raw IS，再clip。这里causal是只消费过去token，不是因果归因；Gaussian/randomwalk是滤波假设，不证明真实policy density ratio无偏。Q小可能oversmooth/lag，V大压低变化；未获得新unbiased IS/稳定收敛保证。

Qwen3-4B-Base、DAPO math、rule-based binary GT，Btrain32/eval64/G8/maxresponse4096/LR1e−6；clipped Q=1e−6/unclipped1e−4、V1，clip .0003/.0004；GRPO .2、GMPO .4，与tiny-clipped组不相同，不能将所有提升归因filter而非clipping。eval T1/topP1，avg@16/pass@16是每题16生成非16训练seed；H100型号有而数量/precision/收敛成本/重复runs ND。Table1数学集合中Minerva clipped38.23低于GRPO38.67/GMPO38.48/unclipped39.15，不能称全面改善或固定训练预算无成本。

拟仅报告：具体滤波recipe/超参敏感性与局部数学对照值得保留，但不改变Ch31/33 IS真实性与offpolicy support条件；不把经滤波权重变成严格importance ratio或causal credit。原源 V3_BFOUR_FINAL_3.txt Source123–171；V3_BFOUR_METHOD_1.txt Source172–215；V3_BFOUR_CONTINUE_1.txt Source350–365。不读无关prompts/各case，未复现。

## [Wormhole](https://arxiv.org/html/2602.10615v1)

6（2+2+2），标准，并对可能simulation接口gap定点深入。§3–6：共享switch port将flows连成partition；FCG weighted graph只保留rate/link-overlap，忽略pathlength/position，不是完整packet/CCA状态。memo保存start→end FCG、transmitted-size、convergence-time；weighted isomorphism再复用，这个抽象依赖有限网络/CCA动态，不能由图同构声称任意externalstate等价。steady detection是窗口relative rate fluctuation<θ，估平均rate；θ太低不提速、太高误判，l需覆盖CCA周期但过大增加进入时延。Theorem1–3只记录作者conditional结论，本报告不采用“过去短窗稳定保证无限未来”或无条件rate/FCT bound，未给全证明背书。

§6.2/6.3明确globalclock不能直接跳；每partition只调整本地event timestamps并保留steady port buffer occupancy以维持其他partition可用shared buffer。已知flow-entry/completion/reroute事件截断跳点，实时interrupt需skip-back恢复至输入时刻。与只画fidelity口号不同，这是具体不能抹掉共享state/localtime的模拟执行接口。

§7两Xeon共56core/128GB，ROFT/Fat-tree/Clos、理想DP/PP/EP流（一GPU一host；不模拟TP/SP flows），microbatch1/defaultθ5%/l2000；ns3单核和Unison16核比较。FCT平均error<1%不授尾部/所有packet，第一flow packet RTT NRMSE仅有限sensor。memo比只steady跳过误差更高。真实GPT18B trace TP8-DP16-PP2-VPP2/B512/recompute/硬件扰动，speed97.75x或加Unison133.35x，E2E训练时间估计误差3.02% vs ASTRA+ns3 3.01%；这是模拟器walltime不是训练GPU提速。硬件GPU型号、precision/各trace可复现性、最终modelquality、productionSLO Not Disclosed。

可能Books差额（待root PRE不先写）：Ch36实际1567–1573只有少量realrank+虚拟participant和fidelity校准，没有上述partition-local时间、共享buffer占用与interrupt恢复的skip接口。若该有限工程约束有长期价值，可在其现simulation节最小加1–2段，保存完整packet DES旧路径、FCG非完整state、真实trace误差与拓扑/CCA重验；不采用摘要1000x/“语义等价”或Theorem2–3普遍保证。若仅报告亦须保留上述具体增量而非说graph-name成熟。原源 V3_BFOUR_METHOD_2.txt Source130–200；V3_BFOUR_CONTINUE_2.txt Source207–237；V3_BFOUR_LAST_0.txt Source238–315/326–417；V3_BFOUR_FINAL_1.txt Source334–359。

## [BNRM](https://arxiv.org/html/2602.10623v1)

5（2+1+2），标准。§3/L116–177：nonnegative Gamma latentθ/全局Φ、Weibull amortized posterior，BT utility θ·Φ difference与稀疏ELBO；LLM head输出2K k/scale，η正则。非负不消除factor scaling/permutation，不自动唯一可解释概念或因果credit；posterior variance还无calibration证明。GPT5 top-k case factor语义是辅助描述，原prompt亦承认只看Φ正值不足判断quality。

UF40k/400k、holdout8k，Gemma2/2B LoRA vs Skywork8B协议不混；原文C1称full finetuning但L499明确only value head updated，不将所有权重更新当事实。Table6 LoRA baseline LR1e−5/BNRM5e−5，full baseline2e−6/BNRM2e−5；same epoch/data不等same优化轨迹或独立机制因果。RM maxlen1024/B24或128、PPOlen4096/B16/AdamW/coswarmup，LoRAr32α64 vs policy r8α32、evalT.7；PPO twoLLama3-8B有限一epoch，部分HellaSwag/BBH等回归，不全面dominance。H/W、precision、重复trainingseeds、PPO SLO ND。

BoN“gold”实际Mistral7B-Instruct-UF reward模型，不是真人/独立事实oracle；1k prompts/N1–405，以logN−(N−1)/N作selectionKL估计。25%标签随机noise只受控该label-flip，长度相关性降低不证明所有reward hacking不存在。η过强/弱回归，语义因子case不因果。拟仅报告：稀疏参数化/经验proxy对齐值得保留，尚无新增真实reward/唯一因子/校准适用条件，不改变Ch31 reward与evaluator独立权威的长期约束。原源 V3_BFOUR_CORE_1.txt Source116–177；V3_BFOUR_METHOD_3.txt Source204–246；V3_BFOUR_CONTINUE_3.txt Source533–546；V3_BFOUR_FINAL_2.txt Source403–481；V3_BFOUR_LAST_2.txt Source489–503。未核artifact/复现。
