# Jun03 具名续跑第二批：训练配置与参数化 / 待独核

作者`supp_jun03_close`，仅Jun02 BJT补窗；本日适用上下文沿本轮完整已读有效层复用。四项完整v1题摘与R26/R28联合日证有效，精确arxiv.content/findable registered：01967 `2026-06-02T04:28:11.000Z`、00271 `03:47:36.000Z`、01412 `04:14:56.000Z`、00428 `03:51:18.000Z`，不改字段为实际公开时刻。当前四官方abs均唯一v1，未见撤回/勘误/删除或具名更早正文信号；00428接受后续workshop不改首发。不扩新日期/机构/NAV。

## 01967 SAPO — 2+1+2=5；Ch29单段提案

[v1](https://arxiv.org/html/2606.01967v1) / [原件](SUP_CLOSE_2606.01967v1_20261025.html)。实际读§3–5/Alg1/T1–3、C1/C4/C5、D/E及F主表反侧。任务前生成20个paraphrase，以**当前checkpoint**在250/1000当前任务带target训练样本上的response CE筛选最低loss的一份，再训整任务；不是逐step持续优化prompt，也不是softprompt参数训练。评价该任务也使用所选prompt，因此in-task差额混有elicitation变化，旧/未来任务仍保各自原prompt。Semantic同义/等长只是生成约束，meta-prompt还允许换length/style，未有全面独立保义证书，不补“严格同语义无混杂”。

Llama2-7/13B、Qwen3-8/14B，q/v LoRA rank8、EWC更大rank40，10epoch/Adam1e-4、batch64、8H20/ZeRO2、maxinput1536/output128；precision未披不补。SuperNI各1000，TRACE各3000，统一ROUGE-L含code/分类后处理不等execution正确。小规模2seed、大规模单seed；三paraphraser局部消融3runs。T1有FWT/BWT反退，F表亦有负项，故“all metrics universally improve”和“lowloss最差安全”不采用；§3.3出现负相关不能变成任何任务普适排序。SAPP highloss对照没有等预算随机paraphrase/固定独立evaluationprompt全因子，不把全部改善唯一归动态选择；前20/后50池nested不是独立重采总体保证。

C5只取上8层初始零B的q/v LoRA B梯度、A梯度为0的四prompt相关，不能证明完整模型优化冲突唯一因果或参数已经形成共享能力。E训练增加约8–12.5%墙钟、理论16.6%算力估算且排paraphrase生成，不称免费；所有候选生成/CE、训练/存储/旧新任务回归付费。任务集“unseen to pretrain”无数据溯源不认证未污染。

actual完整读Ch29 Catastrophic forgetting的压力/回退起始组、早期欠优化/retain、Fine-tuning输出空间与“Forget Budget绑定当前Loss”整组，并读response-only prompt影响与梯度路由组；Ch28/30/31开篇职责已读。现文有步长随loss调、mask不关prompt梯度、adapter/replay，但**没有在同任务内用当前checkpoint的targetloss选训练指令、与旧/未来任务共同验收这一输入表述选择**。不是仅“prompt也是identity”。唯一`TRAIN-SFT`；拟在“缓解方法可能包括混入部分pretraining/domain data…”完整段之后、现“需要纠正一组已知分类失败时…”完整段前插一段：

> 训练指令的表述也是可选择的输入变量，而不只是部署时的prompt工程：在每个新任务开始前，可生成若干经核同义候选，用当前checkpoint在该任务有target的小样本上的response loss选一份，再固定它训练该任务。[受限SAPO对照](https://arxiv.org/html/2606.01967v1#S4)观察到当前任务接近时，旧任务保持与未来任务迁移仍会随表述变化；这不保证最低loss对所有任务最安全，部分BWT/FWT仍反退，局部梯度相关也不证明完整干扰机制。训练和评价若同时换prompt，还须与固定评价表述分账，保义、旧任务与未来任务分别验收；候选生成、筛选前向和全部回归都计费，局部墙钟增量未包含生成费。候选不保义、retain支持不足或净预算不合时，保留原经核指令、replay、较小更新及独立adapter，不让低loss自行批准无遗忘。<!-- source-family:SF-2026-ARXIV-2606-01967 -->

## 00271 HeLoCo — 2+2+2=6；actual同family具体NC提案

[v1](https://arxiv.org/html/2606.00271v1) / [原件](SUP_CLOSE_2606.00271v1_20261025.html)。实际读§3/式1–19、§4/T1、Limitations、A2局部证明/A3算法/A4–5设置。Worker从theta−eta*mu*m的lookahead出发，返回的是相对该出发点的位移；arrival时每parameter tensor与**当前**outermomentum比cos。低norm跳过、充分对齐不改、负向只削掉反momentum分量、弱正向再归一旋向momentum；rho arrivalweight另乘，不能把局部方向校正叫修复目标人口偏差。

A2只证非退化块signedmomentum分量不减、norm不增，不证明F下降/全异步收敛，也不保证历史momentum对新域是正确方向。五worker/15M TinyGPT/GPT2 tokenizer/mC4五语言；§4.1 20inner/100outer、4A100节点，§4.2 80inner/300outer、5H100，pace是受控模拟而非真实WAN。非IID语言与worker速度对应会改支持，DyLU同参与率另改局部训练量。A5 AsyncNesterov LR.07而HeLoCo/MLA.7、sync平均/asyncsqrtK/K权重，不是同所有配置纯校正因果；多seed区间/precision未完整披露。T1 extreme sync固定token仍更好；(1,1,15,15,15) HeLoCo较MLA退约1%，abstract把3.3%称wallclock而正文/T1主同token栏需分开，不采用headline普遍性。A4约15min runtime与T1 4800–19200s pace time口径不同，不能合成实机端到端提速。只采用方向/采样分责与局部几何，不采用真实网络或最优性能保证；全通信、block scan、momentum/worker state及收敛回归计费。

actual完整读Ch36 rescaled-async binding、jointavailability两段、enrollment两阶段段及“Arrival Bias与Stale Direction”**同family两完整段/marker**。它们已明确arrival estimator与outeroptimizer职责、当前momentum纠偏、sourcecheckpoint/localstep/correctionepoch、错reference会压新域、alignment/magnitude/收敛共同测量及sync/丢旧fallback。本文更细per-tensor公式保在报告作为已读实现证据；现有正文未虚称全vector具体recipe，已承担拟保留的长期选择，缺逐分支公式不等缺知识owner，不为同family再造同义两段。拟具体已有覆盖；若后续学习任务需要解释tensor内相互混合的实际差额，可定点精炼原段而非复制。

## 01412 GPTQ-intrinsic LoRA — 2+1+2=5；Ch49单段提案

[v1](https://arxiv.org/html/2606.01412v1) / [原件](SUP_CLOSE_2606.01412v1_20261025.html)。实际读§4.2/Alg3/4.3的主bound与投影证明、§5/Alg4、§6/T1–3与C完整numerics；未读所有信息论lowerbound证明/nearoptimal比较，故不采用标题“nearoptimal”或finitealphabet全域最优。旧初提D3借lowerbound大词，本次实际拟用是联合art构造及有效性条件，按2+1+2=5，不为少读/Books改分。

固定L后把X增为[X,XL]、W增为[W;0]，只量化前N行，保后r行全精度R在同GPTQ sweep吸收误差；L取H主eigenvectors，可不显式存X，但增广H因XL依赖本来奇异，lambda/eigen+QR数值支路要绑定。理想infiniteuniformgrid、L=Vr、fixedcalibration/投影下error上界换成残余谱与lambda项；finiteclipping/低bit不直接继承。Bid-Up保持**同一grid**、顺序逐coordinate精确最小化，固定Q的最优rank补偿与之交替才有同一个layer surrogate不增。重新校准grid会改可行集、不能援引同保证；C实际两步用相同dampedH，因此对应regularized目标，randomized lowrank求解/有限数值/后量化LR不自动获得理想exact guarantee，decrease也不证明全局最优。

Qwen3 .6/1.7B，单A100、Wiki2 128×2048训练序列一次采用于196linear、全testPPL、W3/4channel网格；GPTQ*换稳定factor本身有收益，必须与同factor基线比。C第三block downproj另用lambda.05、其余.01，3bit refinement跳过该层，不称每层统一recipe。DeiT2bit/2048image perlayer、L4/R8后量化局部结果有回退，多轮layer surrogate不等accuracy单调，未披真实吞吐/并发/SLO不补。构造H、eig/QR、LR/全部轮次与双支执行存储都付费，未核代码或复现。

actual完整读Ch49 SVDQuant/Nunchaku及FLRQ联合rank/clipping完整两段、LoRaQ完整段、TwinQuant共同loss/consumer段；前后Ch48/50只核职责。已有交替重校网格/共同loss，但没有**在一次sequential量化中保留全精度吸收坐标、以及固定grid给交替surrogate单调的条件**。唯一`INFER-TENSORRT-LLM`，不搬TRAIN-LORA（此处不是task adaptation）。拟在FLRQ完整第二段（结束“部署前继续验收完整执行计划。”）之后、LoRaQ首段之前补一段：

> 量化后再拟合补偿并非唯一构建顺序：固定输入子空间L后，可把校准特征增为[X,XL]，在同一次GPTQ式顺序舍入中只量化原权重坐标，保留后面的全精度R吸收误差，最终执行Q+LR。[联合构造的受限结果](https://arxiv.org/html/2606.01412v1#S4.SS2)不等先量化再追加同rank修正；增广特征线性相关还会使Hessian奇异，正则与数值分解必须同产物记录。后续若要让交替目标不增，须固定同一量化grid、逐坐标精确更新并与最优低秩子问题共用同一surrogate；重选grid、近似分解、有限精度或再量化factors不自动继承该保证。它只约束校准层重构，infinite-grid谱界也不直接批准低bit、下游质量或全局最优；部分任务仍反退。统计/分解、每轮搜索及两路权重与执行费用都计入，数值、质量或consumer不合时保留独立PTQ后补偿、固定已校产物与较高精度路径。<!-- source-family:SF-2026-ARXIV-2606-01412 -->

## 00428 CP adapters — 2+1+2=5；Ch30单段提案

[v1](https://arxiv.org/html/2606.00428v1) / [原件](SUP_CLOSE_2606.00428v1_20261025.html)。实际读§3–7/式1–7/T1–5与边界。一个2048²投影LoRA rank步储4096；CP把row/col分别32×64，四normalizedfactor+lambda储193（不是intrinsic自由度），c项unfold后matrixrank≤c但每方向是Kronecker-structured，细步来自表达约束而非免费任意rank。48 q/v projections总count/Adamstates可复算，base/activation/总内存/执行另计，不是模型压缩。

OPT1.3B/fp16、SST2/RTE/BoolQ，traincap1000/dev500/eval最多1000（实际872/277/1000），5000step/每1000挑bestdev，LoRA LR1e-4/CP2e-4预定未fullsweep，base3seed、selected cells10seed。CP13个testedc/LoRA6个r，U_A(B)用heldout evaluation上max是描述曲线而非deploymentselection，无等searchbudget优胜证书。SST2低预算plateau最初c2不能由3seed宣布最优、BoolQ仍略逊LoRA、RTE差不因增c消失，只有SST2小tensorization检查，不外推所有形状/任务。GPU/latency/SLO未披不补，所有grid、dev选点、seed确认、重构/反向计费，未核代码/复现。

actual完整读Ch30 BA定义、structuredMPS/CDVFT分支、参数量例子/初始化组、同LR不公平与TeRA完整邻组；Ch29/31职责已核。现文解释trainable vs total与结构性参数化，却没有**rank/grid增量分辨率与结构表达能力分开、预算cap只能在tested feasible grid比较**。不是泛“参数少不等更好”，而是一个预算可选集改变的明确取舍。唯一`TRAIN-LORA`，不搬Ch66重复数学owner。拟在参数量例子末完整“该层trainable…其他参数。”后/现初始化解释前补一段：

> Rank还决定可选择预算的步长，而不只是总容量：一个m×n矩阵的LoRA每增一rank便多存m+n个标量。把更新tensorize后，以多条受限Kronecker方向的CP分量求和，可把每步增量变细；[受限OPT对照](https://arxiv.org/html/2606.00428v1#S4)中2048²投影的一步由4096变为193个存储标量，但细网格来自方向结构受限，不保证同预算表达力或质量更强。应同时看原始质量曲线、相近预算点及声明cap内的tested可行集；更多容量点上的事后最大值不是独立选型证据。局部实验有早饱和、逐步改善和持续弱于LoRA三种情形，adapter optimizer-state少也不等总训练内存或时间少；全部tensor重构、搜索与留出确认都付费。任务、结构或净预算不合时，保留普通LoRA较粗rank网格、更宽方向或full update，不由预算步更细批准替换。<!-- source-family:SF-2026-ARXIV-2606-00428 -->

## 当前交付

四项必要/actual-owner ready；01967/01412/00428只上述具体位置单段提案，00271具体NC。无Books写入或预I/POST/DAY；root独核后再处置。Batch1未变无需第三。原MODEL18本批又4必要后，尚10具名：00722/00724/01026/01024/01774/02544/02241/01839/01065/00866；另02358/00289/02502/02576普通，有限发现收束未归零。
