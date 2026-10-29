# Oct23同日必要Source：模型/训练第4批

作者oct23_live_arxiv。只处理2026-10-22 BJT窗已核准入的29355/29385/29426/29458/29538/29734/29927/29932；已启动重读AGENTS、当前研究/Report合同、Prompt、来源用法/每日arxiv主题、ROADMAP与本日State停点；不恢复其他日期或重扩发现。全部exact-v1，尤其29385不混已见v2。沿[ARXIV原AB/正式分/逐ID公告关联](./ARXIV.md)及[官方分组原件](./arxiv-official-listing-groups.json)，各自为Oct22 New/Cross而非replacement；不能以Submitted代公开。root唯一Books/Report/State writer。本文只必要Source/actualowner/条件PRE，未独核或未实际保存不预签。

## U1 — 2610.29355 GaP-MoE；2+1+2=5；Ch21有限gap提案

原证：[exact-v1 HTML](https://arxiv.org/html/2610.29355v1)、[必要原件](./source-model4-2610.29355.txt)。实读§3全部机制/受限分析、§4对照/§5限制、Alg1/AppA完整步进、AppB证明与C配置。未核实现/复现/全图，不授其形式化全训练专化保证。

旧约束→增量→选择：router/auxiliaryloss并不隔离co-routed expert的相同更新；source以routing概率逐token采leader，保其taskgradient，follower用leader旧gradienthistory的正交补投影，再只以leader原始梯度更新有界FIFO正交基。改变peer间更新耦合，不换taskloss，也不等不改变实际optimizer方向/优化目标。

必要边界：操作对象是expert-output gradient而非直接全parameter矩阵；threshold比较两expert最近basis，alpha1全投影才正交，主alpha首epoch从.1warmup。每expert同batch leader梯度先均值再GramSchmidt；本step投影用更新前buffer，projected follower不入buffer，K>2各follower同一leader独立投影。空/退化基的数值策略不能由公式补猜。AppB用线性expert/SGD与短期gradient近同方向近似消若干项，并未控制完整cross-term、初态或AdamW与非线性网络全轨迹；部分式子的output/weightgradient记法不一致。只采可执行projection分支和局部实验，不采“必然降低outputinnerproduct/无collapse”。

证据/费用：4experts/Top2、BERTbase12层同预训初始化专家、GLUE5epochs；reducedGPT2为6layer/8head/intermediate2048，只有后2层用GaP，其他standardMoE，3seed、h16/8、seq128、AdamW；scratch按validation1000step/patience3选点，不等各法总训练步完全匹配。RTXA600048G fine-tune/A6000Ada48G scratch，未报端到端wallclock/peakmemory。均值modest改善、Table4有局部任务反退、外部XMoE/SimSMoE是作者统一重实现不冒官方artifact。randomrouter对照支持局部不依赖router训练，不授routingfailure鲁棒保证。GramSchmidt/投影、历史驻留、参数搜索与全部训练评价付费，不额外F/B不等免费；h/layer/threshold未系统搜索、大模型未验。

actualowner：完整读Ch21 SD-MoE common/unique梯度分责及前后shared-first/ExpertWeaver段。已有固定公共谱基的两侧parameter投影，但没有“不另分共享权重，以每token随机leader的近期output-gradient子空间限制peer”的替代。唯一 `MODEL-MOE`，只补此不同耦合条件，不把cosine间隔当语义专化证明。

条件逐字PRE：
> 不新增共享参数时，也可直接改变co-routed experts的更新耦合：每token按routing权重采一个leader，保留其taskgradient，把follower的outputgradient投到leader近期梯度基的补空间；基只累计其作为leader时的原始梯度，投影先于本步历史更新。它保留原taskloss却改变实际更新，不等普通optimizer或专家功能必然分离；有限alpha、陈旧/退化基、非线性与Adam状态都使局部正交不等全训练保证。小模型对照支持有条件的质量取舍，也保任务反退；历史驻留、正交化、投影与质量回归均计费。更新一致性、数值或净质量不合时，保原router/auxloss和普通专家更新，不由更大的output角度宣布真实语义专化。

精确插点：Ch21 SD-MoE完整段/marker后、ExpertWeaver完整段前；未写Books。完整上段：

共享 forward 并不阻止 routed experts 在训练时继续追逐同一更新方向。若公共容量用固定左右谱基的投影 $P_U,P_V$ 表示，可以把一次梯度 $G$ 拆成 common 更新 $P_UG+(I-P_U)GP_V$ 与 unique 更新 $(I-P_U)G(I-P_V)$，分别交给公共权重和双侧互补的 expert 权重；后一项在固定基下避开两侧 common 坐标，前一项却可有两个交叉分量、rank 达到 $2k$，不是天然 rank-$k$ 更新。这是 update authority 的分责，不等于专家语义互斥。[SD-MoE 的受限证据](https://arxiv.org/html/2602.12556v1#S3)每16步刷新 SVD 基，但参数、optimizer 与基更新后是否重新对齐仍需独立检验，不能把固定基投影性质延伸为整个训练持续严格正交；刷新和不同学习率也有成本，所测吞吐约下降5%，且存在任务反退。应同时验收实际参数子空间、质量和训练预算；刷新漂移、尾部任务掉分或成本不合算时，普通共享路径、原 routed MoE 与 dense 仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-12556 -->

完整下段：

已有 dense checkpoint 转成 shared/routed 分工时，也不能只按权重大小拆专家。一个条件初始化分支先在校准样本上统计 SwiGLU gate 的输入激活 profile，以跨样本变动决定各层共享比例，把稳定高激活 neuron 留在共享路径，其余聚类成专家；切片须保持同一 neuron 的 gate、up、down 对应，router 可由 gate 向量初始化。但初始化方便不表示函数保持：剪枝时的无权重求和与继续预训练时的 softmax 加权已是不同计算。[ExpertWeaver 的有限对照](https://arxiv.org/html/2602.15521v1#S3)中，25% active sparsity 仍明显掉分，全部权重仍存，校准及 200B token 继续预训练、SFT 也有成本；固定单 GPU 并发的吞吐收益不能推广成总训练更省或所有负载 SLO 改善。于是共享比例与 expert 切片应绑定校准人口、计算函数和训练 artifact，验收质量、权重驻留及实际 dispatch 成本；分布失配或预算不合算时，原 dense、原生 MoE 和更充分训练仍是共存选择。<!-- source-family:SF-2026-ARXIV-2602-15521 -->


## U2 — 2610.29385 PLRM；2+1+2=5；exact-v1；Ch29有限gap提案

原证：[exact-v1](https://arxiv.org/html/2610.29385v1)、[正文原件](./source-model4-2610.29385.txt)，沿已核[精确v1 AB](./arxiv-ab-29385v1.json)。v2可见但不混本窗v1事件/内容。实读§3.1–3.4、§5设置/主结果/mixture反侧、A.1–A.3实际objective、B.2数据与TV定义。未核代码或复现，不读无关生成例。

旧约束→增量→选择：自回归latent rollout训练逐步串行，单Gaussian prior会把不同trace模式拉平；source让posterior从已见CoT并行产生各步目标Gaussian，prior在posterior样本上teacher-force并行预测下一latent，联合答案/重构/分布对齐；多trace时trajectory级一次采strategy并固定，用strategy-conditioned prior mixture表达异质支路。不是部署latent解码也并行，更不等latent语义唯一。

实际目标/反侧：backbone+feature共用、prior/posterior分head，q的step因子条件独立不取消prior依赖已采z<k；推理只见problem，仍AR采latent再生成answer。VISReg约束posterior means而非噪声样本；实际A.2以首latent KL的EM式responsibility贯穿trajectory、减dispersion、0.8/0.2 stopgrad KLbalance及β/VISRegwarmup，Gaussian项按K平均而categorical一次；实际Eq27不是未改动的纯ELBO。Mixture/factorizedposterior/正则提供局部模型族，不证明latent是可识别真实reasoningstrategy、完整posterior或无collapse。

评价：GPT2/Llama3.2-1B、K6/d768/BF16AdamW，主要singletrace M1，40epoch多数/1BCQA10epoch、batch128/256、PTL按任务变；时延图是iteration随latentsteps而非总训练费或部署SLO，CoLaR因少一次targetforward更快，PLRM不是最快。Jointvsfixedtarget消融CQA43.40vs18.35–19.49支持此recipe不唯一隔离所有regularizer。HiddenBranch由ProofWriter2–5valid hiddenfacts构造，21,466/3,179/6,128 unique train/val/test，不当自然开放推理。TVScore以所有gold均匀分布为目标，惩invalid与coverage不齐；M2 TV .7097高于M1 .6252却hit .9205低于.9370，正文“both best”不能外推为所有M更好。Hardware/重复seed/完整端到端预算Not Disclosed，有限OOD非通用transfer证书。目标CoT制备、posterior/decoder/prior全部训练、mixture/正则、串行部署轨迹与外部答案验证均收费；源码/数据v1为未来公开承诺，不冒已开源。

actualowner：已读Ch8 latent recurrence/proposal/计算使用三个具体分支；它明确不拥有SFT优化，故不把训练objective堆入Ch8。Ch29完整数学/结构化head/EBFT/ConceptTokens/训练code搜索局部已读，缺“从trace并行学连续目标分布、joint prior对齐而部署仍AR”的监督适配分支。唯一owner `TRAIN-SFT`，Ch8保latent真值/使用/答案验证的既有边界。不是因名称JEPA映射即入书。

条件逐字PRE：
> Demonstration中的推理也可监督连续latent分布，而不要求部署逐字复述trace：posterior读取训练CoT并行构造每步目标，problem-conditioned prior在posterior样本上teacher-force预测后续latent，并与答案/重构目标联合训练。多条有效trace可用一次采样且贯穿全轨的strategy mixture分开模式，但这种分量不认证真实语义策略；posterior均值正则、分布对齐与实际梯度平衡须分别记录，不能把改权/修正后的训练统称原ELBO。并行的是有目标的训练，不是部署的自回归latent采样；有限对照中更均匀覆盖有效答案也可能降低单次命中。目标制备、posterior/prior/decoder、全部训练与外部答案核验都计费；模式坍缩、prior失配或净质量不合时，保留显式CoT监督、单一latent路径或原verified SFT，不由紧凑latent和较快iteration批准真实推理或总成本更低。

精确插点：Ch29训练code控制完整段后/CATS数值条件完整段前。上段全文：

条件接口还可以由训练搜索提出，而不由人工给每段标注概念：在固定层为每个token chunk选择一个离散code，将对应向量加到这段hidden；训练期对已知目标采样多条code序列，选conditional likelihood较高者，再联合监督router、codebook与语言模型。[这条受限适配分支](https://arxiv.org/html/2605.14323v1)改变的是内部控制条件与训练环，不是添加可见推理token或MoE expert，也不能继承理想策略搜索的全局最优保证。目标答案可用于训练选code，部署却只有router；主文与附录搜索数不一致、解码和完整费用未闭，不能给出通用运行配方。同数据/步数不等同候选搜索预算，去code后的退步也不证明语义唯一或原能力无损。所有候选前向、路由/先验与联合训练均付费；控制失配、collapse或质量/总费不合算时，保留普通verified SFT与显式条件，不用可命名code代替独立行为验收。<!-- source-family:SF-2026-ARXIV-2605-14323 -->

下段全文：

当 demonstration 还携带可控的数值属性，控制标签存在不等于训练人口提供了足够的变化：从 reference 计算目标 readability 或长度比例，把它作为 response 条件接口，仍需检查每个目标区间的样本支持与 source→reference 的变化。验收分别测 target–output 属性误差、保义/相似度和真实任务质量；较低属性误差不证明人类可读性，不同属性的 raw scale 也不能直接平均成统一控制能力。<!-- source-family:SF-2026-ARXIV-2604-01779 -->


## U3 — 2610.29426 BIRD-RL；2+2+2=6；建议具体No Change

原证：[exact-v1](https://arxiv.org/html/2610.29426v1)、[必要原件](./source-model4-2610.29426.txt)。实读§2–4 trajectory/state机制、§5.1–3协议/IO、§5.6直接reward/课程反侧，B.1完整allocation/reset/release伪码、C.2实现设置及D.2完整IO推导/E限制。未核代码、隔离faultinjection/通用DB安全，不读无关prompt图。

旧约束→增量→选择：container-per-rollout昂贵，但按toolcall复用会丢同trajectory state或漏前trajectory修改；source按worker划不重叠replicapool，用stabletrajectoryID→worker/DB registry保持整轨binding，到submit/timeout才release，dirty标记在下次allocation前lazyreset。实际执行以预建pool代动态创建，减少online materialization；状态是trajectory而非每次API请求的生命周期。

必要纠错/边界：摘要“spatial12.8x”应收窄为Table3/D.2的online lifecycleI/O：2.94TiB→236GiB，不是peakRAM/storage/end-to-end吞吐；明确排除一次69GiB建池，B16/R16、每DB预留BR/2=128replicas，9.25%发生mutatingrollout且reset比fullcopy便宜的局部条件。hotDB分布可耗尽pool，D.2 O(1)lookup不含queuewait/reset；伪码有allocationtimeoutfailure，不足证明asynctimeout后的在途SQL物理静默、完整异常清理/fencing、多租户或跨DB通用transactionisolation。它支持资源选择，不授“safe/contaminationfree”所有故障。资源fail若作为0reward会扭曲group，不能因pool改进就认已消除此途径。

评价/费用：Qwen2.5Coder7B/14B，VERL0.7.0.dev0/vLLM.11、8H10080G；四阶段包含teacherGT可见合成/SFT，再singleturn与multi-turnGRPO，不把最终44.4/48SR归因pool单模块或与API不同配置视同预算。SFT2阶段各3epoch，RLStage3R16/Stage4R4、最多5assistantturn、greedy15000input、5重复trial不冒5independenttraining。纯executionreward更好仅该代理/任务，测试比例也不是完整语义真值或无偏policygradient证书。建池/读写/reset、队列/失败、teacher、全部训练/rollout/执行与独立回归全费。

actualowner：实际顺读Ch84 Workspace整局部：longrun显式持有文件/进程/服务等，toolwrapper各管导致identity/effect分离；run绑定、suspend/recover/release/destroy及orphan/成本回收都已具体。再读Ch33资源执行机会/异常不能默作zero、mask仍改group统计段。本文trajectory-scopedpool是这些已有生命周期/复用接口在SQL训练的局部实例，lazyreset策略/当前容量属于有限实现取舍，不修正现有判断，不需另为DBpool增通用分支。建议 `AGENT-PLATFORM` Ch84已有覆盖，Ch33已有资源失败分责；保6分本窗报告及I/O具体纠偏，不因NC撤贡献。

## U4 — 2610.29458 Harness Scaling；2+2+2=6；Ch84有限gap提案

原证：[exact-v1](https://arxiv.org/html/2610.29458v1)、[原件](./source-model4-2610.29458.txt)。实读§3全部机制、§4.1–3主对照/选择与repeatcontrol、§5分析/反侧、A五组件实际变体、C.1训练/segment与C.2评价。仅必要低阶design，不机械重证明经典orthogonalarray/Rao界；未核实现/复现/全trajectory图。

旧约束→增量→选择：单harness训练易专化；source把system/tool/observation/context/workflow因子化，5×3levels的243配置中取18个strength2训练设计，随机anchor+最近Hamming邻居为同task两次相邻steps分配，原PPO/GRPO目标在各实际harness下计算。区别于任意堆harness数或只版本化单model/harnesspair；低阶平衡不证明覆盖高阶交互或OOD保证。

必要边界/控制：task/env保持是构造约束，不是形式化信息等价；toolalias含distractors、context保近5/3turn并LLM摘要/文件、workflow强制plan/periodiccheck都会改实际可见条件和费用。每taskK2是successiveupdates，不把不同harness拼成同prompt独立rolloutgroup；compactionsegments仍只以原8rollouts reward归一，各segment继承组与advantage，tokenmean不额外按segment计sample。训练18不等测试所有225未见组合，main只18固定heldout，三独立evaluationruns不是三trainingseeds。Full243消融含测试配置，只fixedbudgetstresstest不算heldoutgeneralization。

设置/反侧：ClawGymTask13.5K、Qwen3-4B/30BA3B，veRL/asynvLLM/H20 16/32GPU，300updates，GRPO16tasks×8rollouts/PPO128×1，无KL/entropyreg，4Bprompt8K/resp32K、30B4K/60K，LR1e−6/clip.2/.28。K1、matchedRepeat2、random18/assignment与K4消融支持组织方式而非重复task唯一解释；更多配置或K不单调更好，baseharness59.82→59.63有小退。Blackbox训练OpenClawv2026.4.5/heldoutClaudeCode2.1.205仅这些外部接口；SFT12800traj×3和RL300×128只有exposure近似，不等成本/训练law。Behavioraljudge图只相关/定性机制，非因果组件唯一贡献。生成variant、compaction/extra工具、完整RL与多配置/黑箱独立回归都收费，matchedsteps非matchedwallclock。

actualowner：已实际读Ch84 model/harness共同演进两完整段与下接controller。已有配对artifact/crossproductregression，但没有“固定训练budget下以低阶配置覆盖+同task近邻变化组织policy训练”的生产人口分支。唯一owner `AGENT-PLATFORM`，不在Ch33再讲factorialartifact；原policy概率、groupidentity仍从Ch33消费。

条件逐字PRE：
> 不只共同升级一对model/harness，也可在训练时显式分配harness人口：把prompt、工具接口、observation、context和workflow拆成可版本化因素，选低阶组合平衡的小集合，再让同task在近邻配置下依次获得训练机会。这里的平衡只覆盖选定因素与pair，不认证高阶交互、信息等价或未见外部harness；context压缩和工具变体仍可改变条件与费用，rollout/group身份不能跨配置混作独立同分布样本。有限matched-repeat与同规模随机集合对照支持组织方式的重要性，更多配置也未必更好；variant生成、全部训练、摘要/工具和独立多配置回归均计费。迁移、baseharness质量或净预算不合时，保留固定harness与已验model/harnesspair，不由配置数或平均分批准通用鲁棒性。

精确插点：Ch84 model/harness共同演进完整反侧段及其marker后、Harness Controller标题前。上段全文：

联合演进扩大探索空间，却增加版本组合和 benchmark overfitting。有限实验不证明某种 co-evolution schedule 最优；生产 release 仍需冻结独立 holdout/environment，无法解释回归时回退上一对已验证 artifact。

下段全文（标题后第一段）：

冻结模型并把 context assembly、tool routing、verification 与 reward decomposition 交给外部 controller，可以在不改 weights 的情况下适配领域；这条路径在 domain 相对稳定、控制变量可观察时比反复微调 backbone 更容易回滚。平台应把 controller policy、dataset lineage、model/provider、tool schema、reward/evaluator 与成本预算登记为配对 artifact，并让 policy engine 对每次 proposed action 重新执行授权；执行结果只有携带 effect receipt 才能成为下一轮训练或发布证据。


## U5 — 2610.29538 Stochastic DPO Graph Pruning；2+2+2=6；Ch34有限gap提案

原证：[exact-v1](https://arxiv.org/html/2610.29538v1)、[原件](./source-model4-2610.29538.txt)。实读§3.1–3.5采样/目标/条件无偏、§4设置/归因/Full–Branch/限制，B.4直接证明、D.7匹配profile/训练条件。未遍历无关强凸optimum/全附表证明，不将它们授LLM收敛；未核实现/复现。

旧约束→增量→选择：删监督不等省执行；source在相应操作前分别采position只省outputhead、prefix省suffixexecution、branch省一路backward。Position无偏mean不等非线性DPOloss/gradient无偏；prefix改变早晚token权重；独立正概率branch采样+逆概率只恢复当前已声明position/prefix目标的conditionalgradient。必须先区分sum/logprob与本文lengthnormalized mean；不能都叫“不改原DPO”。

关键机制：两侧policy/reference仍计算当前值以保同一margin；未选侧no_grad，选侧loss乘1/q再反传，q与parameter和两种mask独立。B.4有限两项求和证明可核，不保证finite-step参数、AdamWtrajectory或质量无偏；importance噪声随小q变大，dropout/RNG/数值会破坏完全同value对照。Position uniformsubset在head前选，prefix只在causal/prompt保留条件下与原prefix值等价，range/curvature只是附加理论假设；rho_min.5的full-optimum界作者自己指出vacuous。共享参数不使chosen/rejected每步概率符号单调。

直接归因/代价：Qwen3-4B/8B与Mistral7B，LoRA64/alpha128/dropout.05、FA2/checkpoint/AdamW β1，8×Ascend910B32GiB、global64/perdevice2×accum4。Full-concat较Full快4.9%却多27%memory，两profile不可混。16pairedprofile轮/4warmup/旋转order：head仅投validresponses保全部监督已省8905MB，进一步删40%监督只省642MB，93.3%归因implementation而非监督删除；branchvsFullconcat1.426x，prefix少tokens但时延改善≤2.1%且重复测量差同量级，不能凭省token补造物理因果。跨家族仅branch验证，2Qwenseeds+Mistralseed42同recipe训练省约30%墙钟伴meanaccuracy降.25–.45pp，openendedMistralAH亦降；judge分不证明同质量。Float64两branch枚举与BF16差异/重复noise为有限gradientchecks，D.7澄清check关LoRAdropout、正式训练仍.05。完整两侧forward/reference、选侧backward、额外采样/调参与各任务回归全计费，不能把speedup授任意seq/batch/SLO。

actualowner：Ch34完整SequenceLogProb/sum/responsemask、两侧scoregradient、DPO系统复杂度局部已读。已有signedpairgradient却没有把“省head/suffix/backward”及其不同objective/conditional估计权限分开，唯一owner `TRAIN-DPO`；不在Ch49误写为新attentionkernel。

条件逐字PRE：
> DPO的省算也应按被省掉的图分责：在head前选response位置可省词表投影，在执行前截prefix才省后缀attention/activation；删部分loss不自动省掉它们。均匀位置mean无偏仍会经过非线性pairloss，prefix又偏向早位置，二者一般改变原目标，先冻结sum或length-normalized定义。另一条分支保两侧当前score构成同一margin，只为独立采到的一侧保backwardgraph并以正采样概率的倒数加权；条件于既定mask/prefix时可恢复该目标的期望梯度，不等参数轨迹、质量或Adam更新无偏。少一路反传换更多梯度噪声，head全监督实现也可能已经给出大部分memory收益；两侧forward/reference、采样与质量回归仍付费。RNG/score身份、长回答偏好或净质量不合时，保普通完整pairgraph、全部response监督及已验batch布局，不由监督减少量批准端到端加速或无损。

精确插点：Ch34 DPO移除系统复杂度末完整反侧段后/“DPO保留了什么难题”标题前。上段全文：

但计算通常仍比单条 SFT 更重，因为每个 pair 至少包含 chosen 与 rejected 两条 response，reference logprobs 也要计算或读取。

下接标题是 `## DPO 保留了什么难题`；其第一完整段已实际读：第一，preference data quality。错误、表面化或单一人群偏好会直接进入 objective。


## U6 — 2610.29734 Monitorability Is Trainable；2+2+2=6；Ch72有限gap提案

原证：[official exact-v1 PDF](https://arxiv.org/pdf/2610.29734v1)，[HTML404原件](./source-model4-2610.29734.txt)已由PDF解除，非external。实读p1–10核心/直接实验/结论，p15/21/23–24/33–36必要协议/反侧与toy mechanism；[核心](./source-model4-2610.29734-p1-10.txt)、[必要附录文字](./source-model4-2610.29734-necessary-appendix.txt)。附录原件含p37但本次只读开头，未读完p37，不作全章签字；未核代码、复现、全40页图像。

旧约束→增量→选择：只避免CoT直接奖惩不足以保monitorability；source把已有CoT-output MI surrogate做独立post-training，在同prompt组的CoT×output likelihood矩阵上用lengthnormalized own-vs-mixture logratio，奖励cap在组内α=.75quantile再standardize以偏向低信息轨迹。新增conditionaloutput χ²软约束/νPIcontroller，惩给相同CoT重新编私人output含义，而不只锁marginaloutput；这一权限差异可以同时允许CoT分布和边缘行为改变。

必要限制：MI本身来自Anwar先前方法，不当新发明；有限组/selfterm/lengthnorm/cap/标准化是surrogate而非exactpopulationMI/LCVaR无偏证书。MIgradient只落CoT、divergencegradient只落output，但共享参数不等decoder严格冻结。主要实现clippedtokenlogratio再聚合seqbudget；MBPP是另一完整sequenceratio实现且controller排除invalid/nonfinite，不能混称同一个严格χ²上界。未用task/monitor/行为labels当主要奖励不等所有设置无formatreward：MBPP保format。无monitorfeedback也不能保证non-manipulability，私编码/未知风险、后续evadertraining与强Agent自然失败未证。

证据/分母：GPTOSS120B压缩后GPQA训练/198Diamond+60AIME/OODMMLU评价，每题4CoTs，judge coverage/legibility0–4几何均值；worstcase是4条最差再题均值非全尾保证，2posttrainingruns且fixedreference。压缩回修保部分token节省，放松budget会加长trace；不把judge分作causalfaithfulness。MBPP Qwen2.5-7B从3sourcepolicies中先选高hackcheckpoint，782train/192holdout×4，3000steps/2updates/group8/batch16，MI-only3seeds/full.4五seeds；主表recall/FPR是seed等权与AppB pooledfraction不同，MIonlyFPR20.1%vsfull3.9%。crossedCoT保fixedCoT时base/recoveredcodepolicy47.6/48.2truepass，支持概率转向base已有正确模式（replacement），不是仅让同一坏行为更诚实（revelation）。

更多反侧：fictionaldefects800train/200test×4、107defect，700stepLoRA32；否认率降会改变recall条件分母，Qwen32B/Llama70B未成功复刻其obfuscation构造。安全三bench各自fullparam7B100updates、固定一split，base/post生成各自prefix/continuation，故是matchedquestion的within-policy predictability非同轨trace因果；SORRYunsafe21.9→22.8不改善安全。Consequential指标针对trace自己的最终答案而非正确答案，每8sentenceprefix抽32/50continuations、Beta1,1/100Ksamples，SCRUPLES50step后验选择因继续训练更冗长；tracecoverage增可伴spandensity降、bootstrap区间含零，不写普遍faithfulness。All n²likelihood评分、reference/controller、全部rollout/训练、长CoT、probe/monitor/多continuations评价均计费；Tinker部分硬件/precision/总wallclock Not Disclosed，不凭复用GRPO组称minimal零开销。

actualowner：实际读Ch31 output/CoT reward分工、无需直接CoT奖也退化与rewarddescription修复完整局部；再完整读Ch72原Anwar MI条件信息/decoder可读性及相邻gap段。已有MI不保可读/真值，尚缺“低尾独立修复stage+固定CoT的decoder条件约束，而非marginal行为固定”的具体替代。沿原MI唯一owner `PLATFORM-SECURITY` Ch72，不在Ch31重复定义同一MI方法；controller仅训练proposal不授tool权限。

条件逐字PRE：
> 已退化的CoT还可进入独立的监测性修复阶段，而不把monitor的判决直接当训练奖励：同prompt的多轨迹互相评分，以有限组条件likelihood差提出信息奖励，并截平高分端以偏向较弱轨迹。若只约束marginaloutput，模型仍可给每条CoT换一套私人含义；改为惩罚固定CoT后的output分布漂移，只是软限制decoder重编码，仍允许通过改变CoT人口转向另一行为。两条路须分验：同一坏行为变可见，与更多生成原本已支持的正确行为，不是相同安全结论。有限MI/χ²估计、tokenmask和共享参数不授严格信息/行为保证，较可读或较易预测也非causalfaithfulness；矩阵评分、reference、全部训练、额外trace与独立行为回归均计费。未知风险、私编码、长度或原能力退化时，保原checkpoint、独立outcome与effect gate，不由修复后的monitor分数批准安全或发布。

精确插点：Ch72原MI/Anwar完整段后（SF2602-18297）、receiver/sentinelgap段前。完整上段：

训练时保留 reasoning 与 outcome 的信息联系，也不保证指定 monitor 能读到需要的属性。条件 mutual information 可以约束 outcome 与 CoT 仍有关联，却不独自认证某个风险属性、因果忠实或外部 decoder 的可得性；policy 能读的隐写编码仍可能让另一个 monitor 失效。一条受限训练分支用同 prompt 的多条 rollout 做 conditional-likelihood surrogate，并结合任务或监测 reward；该近似不等 exact MI，训练改善也未消除 reward hacking。[原版本的支持与直接反侧](https://arxiv.org/html/2602.18297v1#S4)要求将信息存在、指定 decoder 可读性、elicitation 和最终 outcome 分别验收。多 rollout、likelihood 比较与 monitor 调用都计费，模型/channel/prompt、length normalization、clipping 与 decoder 身份须可查；改变模型或训练目标后重新校准，信息不足、policy-only 编码或任务能力退化时保留原 checkpoint、独立 outcome 测试和 effect-time gate，不把 MI surrogate 当作 truth 或权限证书。<!-- source-family:SF-2026-ARXIV-2602-18297 -->

完整下段：

信息是否可供某个审计者使用，还可以用两端相对各自baseline的任务收益比较：在相同可安全重放信号上，分别测receiver与trusted sentinel有/无信号的utility gain，再取两增益之差。它改变了监测目标：不是只查编码形式，而是核给定audit objective和decoder能力下的可消费差距。[受限隐写形式化与对照](https://arxiv.org/html/2602.23163v1)中，同一trace对答案与evaluation-awareness任务可有不同gap；零gap也可能包含两端都能消费的敏感标签线索。理论sup仅被有限prompt/采样近似，normalized gap需要正receiver gain，不能把0/0当通用读数。Gap下降须分开报告sentinel得益与receiver损失，paraphraser的soft保持惩罚不保证逐项无损；ROT13部分比较还人为给receiver明文，不能外推同密文自然攻击。标签、replay、双端采样、训练和额外预算均付费，延迟效果或能力elicitation不足会漏检。无法安全重放、无可信任务真值或能力不匹配时，保留原monitor、独立outcome与effect gate，不由低gap认证无隐写或部署安全。<!-- source-family:SF-2026-ARXIV-2602-23163 -->


## U7 — 2610.29927 Benchmark Difficulty Measure；2+1+3=6；Ch66有限gap提案

原证：[exact-v1](https://arxiv.org/html/2610.29927v1)、[原件](./source-model4-2610.29927.txt)。实读§2测量/coverage理论、§3.1估计/诊断、§4.1–3生成机制/对照、A.2限制、B.1 Lipschitzcoupling证明/B.2全部maxgap证明、C.4–5定义/拟合比较开头/C.6后验不确定性、E.1与E.2直接验证。不冒所有表/图/IRT诊断原始响应全核；不核artifact/复现或将测量框架扩为science应用。

旧约束→增量→选择：均分隐含题目difficulty经验measure，既会偏离用途权重，也会完全不观察一个局部难度区间；source区分W1 mismatchedmeasure与最大相邻gap，在声明的难度轴/条件模型中给出分数失真与局部改善不可检测的边界，再以固定原panel能力给新题单独校准、targetmidpoint重写/人审插题。选择从“更多同题重复/更大总体均分”转为“先核目标人口与空缺区域，再决定补题/重复”。

理论范围：Δ(z) L-Lipschitz才有scoregap≤L W1及margin足够大的rank稳定；不是任意真实modelcurves/未知L的保证。Uniform unique maximin只针对指定固定Lebesgue均值、位置完全不知的函数类，不证明所有应用应均匀或难度坐标唯一。B.2固定z与n、相互独立Bernoulli pre/post重复，宽w≤maxgap存在完全同观测分布的局部改善，任何levelα检验最坏power只α；w>gap时用逐item max/Hoeffding+unionbound，k→∞power1，不是有限重复必发现、也不是仅aggregate均分检验。真实估计z/多维能力/依赖错误不自动满足。

测量与成本：25bench/7类作构念示例，不把领域指标当新应用贡献；非agent12models1.7–397B每item最多32rollouts、各推荐temperature/topP，agent依HAL15–66models；Bayesian1PL/MCQ guessing，能力panel/解码配置共同定义难度，不是item固有值。每bench minmax到[0,1]，实现DDM对同大小midpoint empiricaluniform而非连续Uniform，W1理论与实际reference须分清；minmax/endpoints和非线性换坐标可改变gap/均匀含义，跨bench不授绝对同量尺。MCMC/LOO/posteriors只支持当前panel稳定，MaxGap极值比DDM更不确定，2PL部分更好BIC却badchains不等单维真值已证。

BenchFill：最多8round×4parents×4children，原panel/固定ability只校准新b，GPT5.4先validity/至少3人最终审校；相同16T proposalbudget baseline没有nearestmemory/reflist/iterativeupdate，多部件组合不能唯一归因memory。24gap新题均过人审、gap指标下降有限；温和SFT3个AIME局部验证32rollouts/100Kstratifiedpermutation且3/3vs0/3，只小选择人口不授未来trainingprogress必可测。GPU L40S48G/RTXPro6000Blackwell96G，精度与完整生成/评测总wallclockNot Disclosed；原panel全部响应、IRT/MCMC、生成/反复annotation、人审、train/probe与独立评价全费。新题继承样式不认证同construct/无污染，不能用填小gap自签全部任务有效性。

actualowner：实际读Ch66 IRTposterior排序、forced-ceiling题审计、WILD目标预测方差与SkillEval具体邻接，及旧benchmarkcompression区分估计/selection/cache。已有测量模型/拟合和用途目标，但没有“估计difficulty上的空区域使任意同题重复也不能看见特定局部改善”的support边界；不把诊断本身写成普遍效力。唯一 `PLATFORM-EVALUATION-SYSTEM` Ch66，窄gap在IRT审计之后/预算选题之前。

条件逐字PRE：
> 难度测量还应先审题库在这条轴上有没有支持，而不只估计模型能力或多跑同一批题：同样的performancecurve按不同difficultymeasure积分，会改变均分与排序；固定题集中的空区间又可能让只发生在该区间的改善完全不可见，再多独立重复也不能补出未观察位置。这个边界依声明的一维difficulty和条件表现模型，有限IRT估计、minmax坐标与相关回答不能直接继承精确gap定理，uniform也不是所有用途的正确权重。可先冻结用途measure、panel/量尺与不确定性，再对缺口提出新题、校准并独立审其构念/答案，而非只追更难或更均匀。Panel响应、拟合、重写/人审与验证全计费；量尺失配或新题不保原目标时，保留原分项、冻结anchors与独立用途评价，不由小gap或平滑总体曲线认证能力没有进步/退步。

精确插点：Ch66 IRT forcedceiling审题完整段/marker后、WILD完整段前。上段全文：

同一响应矩阵也可以用于审计题目，而不只给模型排名：先用与总体排序一致的 items 校准能力，再固定能力，比较每题在 reference 匹配概率的两种强制 ceiling 假设下的拟合，以差额提出优先回审队列。[受限 IRT 审计](https://arxiv.org/html/2605.30504v1)把难题、异常标签和无唯一答案分开，却不使拟合 ceiling 或模型多数成为真值；tie/all-wrong 等过滤人口仍需另审。弱 reference 来自模型聚合，头部精度不是全题人工 gold，panel 能力跨度及跨 subset 量尺失配也会改变排序。继承标签须追溯源题与构造规则，某模型异常同意疑似错标签只触发训练数据/选择流程检查，不证明污染因果。多模型响应、判分、拟合、人工复核和谱系维护全部计费；证据或量尺不稳时，保留原题、Unknown 与独立专家/可执行核验，不由高异常分自动改标签或否定排行榜。<!-- source-family:SF-2026-ARXIV-2605-30504 -->

下段全文：

增加有区分度的题目还需要回答“对哪个测量目标有信息”。单维 IRT 中最大化 Fisher information 可近似减少能力参数方差；能力变成多维后，信息矩阵的迹较大不保证目标 benchmark 的预测方差更小。一个条件分支先固定已知题目参数和目标任务集合，再选择最能降低这些目标预测方差的题目，每观察一次答案就更新能力后验；若题目成本相差很大，可再按历史输入输出 token 成本折扣信息收益，而不是只压低题目数量。测量目标、选题规则、历史成本和已观察响应需要随同保存。[受限证据：WILD §3、§5–7](https://arxiv.org/html/2604.01418v1#S3)

## U8 — 2610.29932 FrontierCS2；2+1+2=5；建议具体No Change/报告保留

原证：[exact-v1](https://arxiv.org/html/2610.29932v1)、[原件](./source-model4-2610.29932.txt)。实读§3构建/§4judge/§5.1–5.3协议及主结果口径、§6.3直接反例/§7总结、AppB资源说明；未审全部48任务原repo/patch或不相关cryptography/FPGA机制，不将这些case当项目新机制，不复现。

旧约束→增量→选择：从作者workingrepo删contribution却保依赖，比一段problemstatement生成单program更接近集成研发；judge私有reference/evaluator/finalworkloads、Agent只能发允许文件patch，最终一份nomination按everymetric×everyheldoutworkload验收。给出meanfinalscore超过reference而仍因某quality/workloadfail的直接系统case，修正“平均更高等于R&D通过”的解释；不证明Agent创新或通过论文review。

实际协议：48任务/13domain、每12reportedmodel仅一个harness/一次run，5h；沙箱无外网只到driver，modelcall与patch分流，GPUdev与verifier隔离；不等排除预训练memorization/所有channel或相同harness下纯model因果。Score只作dev feedback，final不替Agent选bestdev；无final/2provider拒绝按本benchmarkfail，不能推所有研究耗尽都应记能力零。Reference threshold有些要求更快、有些允许质量band，‘beats’是达各task门而非所有rawmetric严格大于reference；reference恢复代码不是唯一合法方案，也不代表未知真实最优。

直接反例/限制：SVG-EAR任务中候选所有clips更快且平均quality更好，仍2clips质量带失败；平均/合取门确是不同对象，pass也可能不比reference总分高。所有metric过门也不能表示未纳入的成本好，纸中case自身承认size/bytes差异会被pass或score漏掉。FCI是permetric+scoremargin/ranefit、另13thanchor624runs/90%taskbootstrap，非真实能力posterior；一run不刻画seedvariability。Costbudgetcurve把未完成run置零、完成才取最终heldout结果，单调是接口构造，不是真正逐预算重启的anytime性能；DeepSeek费为lowerbound，榜单不当稳定通用采购建议。

AppB明确GPUhours是runbudget非实测成本，GPUtype/CPU/RAM按task异构、A10080G，不合并统一吞吐/速度。repo制备、sandbox/全部patch与dev/finalexecution、独立GPU、modelcall和人工case分析均收费。Network隔离与holdingfinal只支撑当前benchmark口径，不证明生产CS研发安全、任务已无污染或一般科学发现。

actualowner：实际完整读Ch66 Per-verifierOutcome/aggregation数段，明确all-pass/mean/majority可改排序、typedoutcomes/阈值权重须留；Cornetto故障目标/健康约束/全部同时通过段具体覆盖合取验收。再完整读Ch66 HarnessOptimization隐藏test/最终提名，以及workspace冻结evaluator/reference两独立边界。本文workingrepo删除是新的任务人口与有价值局部实例，不补出这些已有接口之外的长期机制；建议 `PLATFORM-EVALUATION-SYSTEM` Ch66已有覆盖，报告保5分/协议与实例，不以NC改判贡献或宣全部case已核。

## 本批停点/精确交接

8/8作者必要Source/actualowner已存并分批交reader，非独核完成/Books已存。U3 BIRD/U8 FrontierCS2建议具体NC；U1 Ch21、U2 Ch29、U4 Ch84、U5 Ch34、U6 Ch72、U7 Ch66为六条单段PRE，各有精确完整上下邻接。均沿原分，不按数量调整。只本note与source-model4必要原件有写入；无Report/Books/State/index/stage/commit/push。

再次定点核官方分组：同一个Oct22页眉 `Showing new listings for Thursday, 22 October 2026` 下，cs.LG New submissions编号29355[74]/29385[77]/29426[83]/29458[86]/29538[97]/29734[116]/29927[121]/29932[122]；29385等另有Cross但无replacement归属。沿已核v1公开边界，未把次日可见v2或Submitted改名为公开。所有必要正文已取得，普通reader/root待办不冒external；更大同日余项沿root分配表扣本8，不越权宣布其他作者完成。
