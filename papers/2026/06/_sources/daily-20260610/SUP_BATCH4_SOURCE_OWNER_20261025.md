# 第4批已准备单篇必要证据/actual owner

准入与日期见SUP_BATCH4_ADMISSION，reader已准入其中10；09287只经定点准入核后关闭贡献、不评分、不进owner，07665日期未决不列确定候选。以下准备好即交，不等待其余。

## STAR-KV 08382（2+2+2=6）

作者实读exact-v1 §3–5、A.3 Training Settings。按K各head/V各block学spectral threshold α，tanh surrogate+KL与Σexp(-α)促进压缩，离线hardcut；不是严格全局budget或最优rank保证。HD-K/JD-V基于局部重构误差/执行取舍，V可吸收到output而K受RoPE阻挡；latent singular尺度造成outlier，20%高bit/80%低bit各独立Hadamard。Eq12同时写r_out≫r_in与20/80相矛盾，不采用该不等式或推广量化比例为唯一recipe。

A.3是所有model parameters lr2e-5、α1e-2，AdamW，一epoch compression-aware后额外1000steps KD；3000 FineWebEdu，seq8192/4096，保护layers0/1/31、two RTXPro6000、约6GPUhour/epoch，未披露训练batch不借attention计时batch16。故不能说只训练几个threshold或<6小时为全流程唯一成本；产物含改变的model weights而非原checkpoint无损cachecodec。RULER4K LongChat不同seed两run不授普遍稳定；Llama3.1 MK2 86.0低于Palu99.8与full99.8，LongBench明显低full。Table4五task avg与Table1六task不同，不合并。20x是作者名义rank×bit配置，不认证含保护层/scale/metadata的真实resident总字节。

系统：Llama2-7B/RTX4090 batch16 Attention operator；32/64K baseline OOM后的速度是8/16K线性外推，不采用实测baseline或普遍6.9x。Table5 generation按各方案最大可fitbatch（如128vs16），3.1x不是同batch/SLO效果。短context量化反会慢。未核实现/像素/复现，支持与反侧足够，不扩无关附录/全部代码。

actual `INFER-KV-CACHE` Ch45:675–710完整已读，已有按head producer分解/读取时重构/V晚聚合（2604.02570）、多种跨层residual路径；缺按Khead/Vblock学阈值、allweights calibration与hard-materialization身份。建议唯一插在2604.02570完整段后、以“跨层冗余还允许…”起的重建分支前。拟仅以下段+自身trueH2注，待reader一次必要/actualowner/原稿核与root窄授：

> Producer投影的rank也可从固定比例改为校准得到：给K的每个head与V的每个block分别学习spectral threshold，以soft surrogate配合distillation/压缩压力训练，再离线hard截断成确定布局。[STAR-KV的受限分支](https://arxiv.org/html/2606.08382v1#S4)同时更新model weights，并非只调几个无损codec参数；K按head、V联合分解与V晚聚合是特定质量/重构成本取舍，不能由局部谱误差宣称全局最优。不同rank又改变latent outlier与量化布局，应把checkpoint、阈值、保护层、rotation/bit/scale和kernel一起发布。校准与额外恢复、重构/量化和布局均付费，长context检索仍可回退；OOM baseline外推和各自peak-batch吞吐不能签同batch服务加速。人口、质量或净费用失配时，保原固定rank/普通分解、较高精度与FullKV，不把名义rank×bit压缩率当完整resident容量。<!-- source-family:SF-2026-ARXIV-2606-08382 -->

## FuseFSS 09551（2+2+2=6）：拟具体E

作者实读exact-v1 §3–6、§7 Conclusion/Discussion必要开头，不声称读全部附录/AppendixM证明或实现。typed fixedpoint scalar interval/polynomial/predicate spec编译成公开masked wire上的packedcomparison与vectorintervalpayload；postprocessing仍含Beaver/AND/B2A与vector max/sum等，两个backend evaluations不是整个模型两次通信。One-time per-wire masks/keys/triples、mask-independent padding形状与显式shape leakage必要。仅2noncolludingservers、至多1semi-honest腐化、securebackend/triple assumptions的gate-level composition，不授恶意模型。

§6双RTXPro6000Blackwell/双EPYC9654/CUDA13，seq128/batch1主要BERT/GPT、BERT32–512；五run去warmup取余四median，不是独立训练seed。在线/通信/keygen/keys四账，LAN1GB/s .5ms/WAN400MB/s4ms是投影不是实际网络；Sigma sameFSS可比，SHAFT devicemismatch不强合CPUHE其他family比较。未用小模型或非生产条件否定潜贡献，但采用只能支持上述有限范围。

actual Ch72:2458–2504完整已读，2494/2496正文已具体解释scalar spec→两backend接口→secretshared后处理、不能当Softmax全流程两调用、随机材料新鲜与padding/shape、相同semi-honest/非串通边界，故拟E、不追加一般隐私警句或制造diff。reader可一次必要/actualbody核，不依赖任何旧Reviewtrace或他日候选。

## BUDDY 09514（2+2+2=6）：拟具体E

作者读exact-v1 §3–5、§6 limitation/A3.2必要：首尾层必执行，给b转k=round(bL)-2的topk中间层；scorer+离线单种prior、firstlayer KV/value summary和newtoken更新context，optional GRPO predictor提深度，topk STE+LoRA与modeljointSFT。只满足离散层数预算，不是时延/显存硬预算；浮动执行路径会缺历史KV，作者zero-fill表示未执行，没实现cache补全等future方向。

§5 LoRA r8 all-linear、Alpaca SFT batch8/2epochs BF16与相同baseline配置，commonsense八任务与Alpaca/SAMSum 128token计时不能合成普遍无损。Table4 lightpruning decode仅1.01x、SAMSumprefill1.00x，深剪枝质量明显退；固定staticpath decode仍可能更快。A3.2 Llama2-7B/A100 batch5 seq256局部overhead（router4.58ms/gatherscatter2.64ms）不是线上tailSLO；allblocks驻留VRAM不减。K+V反不如单V，高sparsity feature最佳层/Key亦改变，不授firstlayer/V普遍最优。未核代码/复现或无关附录。

actual Ch49:2170–2187完整已读，2178/2180正文已逐项承载首层KV→scorer/prior/topk、另budgetpredictor、路径变化历史KV不自动有效、zero-placeholder/allweights驻留、router/gather/异路batch/静态path与难推理回退边界，具体E，不重复改书；不以已有trace作正文覆盖。

## PRISM 09563（2+2+2=6）：拟instruction-set reporter最小I

作者实读exact-v1 §3–5、Limitations与AppendixG必要；仅final128生成token/layer16的Qwen3.5-9B residual snapshots，不传prompt或prompt-token activations，不传自然语言probe问题。learnedprojection→softprefix，重用frozenbaseweights+LoRA自回归解码bullet list；SFT后judge-GRPO coverage/Hall/两侧长度惩罚，空prediction不凭低Hall成功。不是same-pass廉价scalarprobe，权重共享不免额外prefix/报告generation。

~280K UltraChat/IFconstraints/IFEval，同语料SFT+RL；1000 heldout四设置各250、5–7约束/~1000prompttokens，构造AP/HO避开常规benchmark拒答是selection边界。samebackbone LatentQA/ActivationOracles有重训对照，文本only GPT5.5是不同model/训练条件，不全归activation优势。单validation-selected ckpt不是多独立seed；Table2adversarial-subset .740不同Table1整体.745不合为安全检出率。

reference由同Qwen3.5从prompt提取，50record/180bullet audit176正确/3partial/1错仅该样本；G coverage49reports170bullets与Hall18reports113bullets，人类/LLM反复修rubric/重评共享gold，Hall judgeκ.705不是独立heldout/deploy校准。原Hall rubric准许由prompt/context/response支持的implicit bullet，可能reward plausible rationalization而非recover真正operative instruction；原文Limitations亦承认，不把ISR label当因果active set或groundtruthintent。未核代码/复现，非生产safetyintervention或任意长Agent。

actual `PLATFORM-MONITORING` Ch67:284–337完整已读：AERIC samepass hiddenstate scalar hazard与capture staging/descriptor已有，缺多instruction-language reporter接口/原始生成window身份与set-level coverage/幻增。拟在AERIC完整binding end后、以“高频scrape…”起的费用段前加下段+自身trueH2注，待reader必要/owner/原稿一次核/root窄授：

> 当一个hazard分数不足以说明“读出了哪些约束”时，还可把生成位置的activation window投影成soft prefix，再由共享base weights的LoRA interpreter解码多条instruction报告。[PRISM的受限分支](https://arxiv.org/html/2606.09563v1#S4)不向reporter传原prompt或自然语言probe，但仍要额外前向和自回归生成，并非上面的same-pass scalar监测。报告须分别测reference覆盖、unsupported bullets和安全相关子集，不能用低幻增或总体覆盖替代关键约束找回；prompt/response支持的合理解释也不证明该指令实际因果驱动了动作。其单checkpoint、固定layer/window和oracle/judge标签只支持受控set-retrieval，未验证任意长trajectory或真实intent。Activation capture、projection/adapter训练、报告生成及独立校准均付费；模型/窗口、标签或费用失配时，保原hazard/output sensor与人工调查，reporter只提可复查候选，不能直接触发权限变更。<!-- source-family:SF-2026-ARXIV-2606-09563 -->

## 09061 Chunked Prefill（2+2+2=6）：时间目标之外的活跃人口/有效进展

作者实读exact-v1 §3.1–3.3与§4.1–4.6。Aging只换prefill顺序，LPRS在硬token可行域内用16维状态/MLP作离散chunk搜索，以非对称时间偏差靠近目标；两者都不能单独约束跨轮未完成prefill人口。APC Eq12以sequence slots、decode占用、剩余token/Lmin限制活跃prefill数，Eq13–14再检查有效chunk并在无活跃prefill时warm-start。这是具体人口与进展控制差额，不把成熟aging或latency prediction本身当新增原理。

公式边界不能被prose抹掉：Eq14 warm-start分支在|P|=0且c*<mi时未再检查Ct；h<mi也只给min(h,mi)，所以并非所有路径都严格满足activity cap或Lmin，更不保证105ms或有界等待。Eq12以已提交U计剩余预算，不能把论文的round-local选中集合直接外推为整个runtime的全局resident population。

评价分开：Aging为Sarathi-Serve/Qwen3-8B、单RTX4090、ShareGPT200请求/0.1s、context/gen最多512；1024chunk均值反退，双RTX5090的256chunk/maxseq10与32亦有反退，Ascend/OpenPangu仅portability无matched FCFS表。LPRS/APC为Qwen3-8B、单RTX PRO5000 72GB、TP=PP=1，profile36868样本8:1:1，MLP300epochs、heldout3713；非独立多seed/CI。1000请求/4096长度的0.1s高并发局部改善，但1s regular所有full-request分位LPRS均慢于token budget（P50 138.52>129.29、P99 153.35>148.99ms）。Table9 regular prefill .09ms与105ms目标的口径不据此认证真实TTFT或生产结果，也不在未核代码时断言表错。

APC对照为同LPRS框架下49:1短30–50/长200–220tokens、动态到达；Table10平均scheduled prefill5.32→.46、平均chunk .78→6.29、request E2E143.65→111.68ms，仅此人口、无CI；不是通用22%增益。Feature采集、候选搜索、控制与KV/slot资格均计费，未核实现或复现实验，必要支持与直接反侧已足，不扩完整代码/无关附件。

实际`INFER-SCHEDULING` Ch56:370–431及510–575已读，当前Iteration Scheduling有FCFS/age/fairness、2606.05933两轮预测与anchor保护、后有QBA debt，但没有09061/APC的round-local未完成prefill人口+进展接口。拟放05933两完整段后、QBA前单段，trueH2自身来源注；待reader一次原稿核/root窄授，不先写Books：

> 靠近本轮时间目标，也未必让未完成Prefill有效前进：Decode优先后，过多Prefill可能各得极小chunk，反复支付调度与kernel开销。一条[受限活跃控制分支](https://arxiv.org/html/2606.09061v1#S3.SS3)先按剩余sequence slots、token预算与有效chunk粒度限制本轮活跃Prefill数，再检查单请求进展；没有活跃Prefill时另有warm-start，不能把它等同于继续缩小预测chunk。其warm-start公式并不在所有路径重验人口上限或达到最小粒度，预测时间目标也不是硬SLO。作者单GPU/Qwen3-8B、49:1短长prompt对照支持减少碎片这一局部取舍；一般负载下时间预测调度本身还可能慢于固定token预算，不能推广为普遍增益。状态采集、搜索、控制、KV/slot资格和长请求等待共同验收；人口/进展限制不合负载或预测失准时，保固定chunk、保守admission与独立公平队列，不让局部时间误差替runtime签资源安全或有界等待。<!-- source-family:SF-2026-ARXIV-2606-09061 -->

## 09338 Multi-Hop Knowledge Composition（2+2+2=6）：实体/中间桥人口隔离的单前向负面证据

作者实读exact-v1 §2–5/B1–5/C5，支持与直接反侧已足；不是遍历全部附录/代码。100K biographies六属性加单向friend/enemy，把Pcomp与Pheld严格实体与中间bridge隔离；所有实体都有atomic五改写/属性乱序，只有Pcomp进composition PT，FT又只其75%，新Pcomp与Pheld分开评价。GPT2Small/Medium/Large124/354/774M从头训/RoPE，主实验单seed，512context/49152token batch/800Ksteps/39.3B总tokens；unique tokens随aug变，常用atomic/composition30/70但Exp1为50/50、Exp9为15/15/17.5×4。LoRA Q/V/embedding多rank选best，4H100/约8hPT+2hFT为作者披露，不是本轮复现。

Table2九格式Pheld 2hop/3hop均chance，但其1hop可降到.38/.40，不能通称97%仍全完美；baseline Table3 1hop.97、2hop.01只其人口。Table9在constituent两个1hop都正确条件下，Pheld2hop仍0而Pcomp有非零，故不只是知识未记住。Implicit RDF让未FT的Pcomp2hop .79，explicit-only .08，混合最高.83但unique/corpus不同，非各格式同暴露预算绝对排名。FullFT在Pcomp2hop.99同时Pheld1hop.01已遗忘，不证明原模型缺任何composition信息；Chinchilla倍数不能认证已穷尽优化/容量或strict prerequisite。结论只受测单前向implicit regime，不推广CoT/ICL/检索、全LLM或永不泛化。

C5 logitlens只single-token桥名约66%；explicit强emit但.08、implicitRDF不强emit却.79是读出/行为受限分离，不是原计算因果定位/bridge缺失证明，不借成熟readout警句供本项新增分。可保长期差额是严格cooccur人口/中间实体隔离的验证设计与受测失败，而非‘预训练failure非capacity’中心夸大。

actual`WORLDVIEW-REPRESENTATION` Ch05:93–145与430–480完整已读。已有CtD/归纳器等组合接口、信息存在/可读/被用，以及01430两段positive thinking新知识访问迁移；没有该strict entity/bridge cooccur heldout负对照。拟在01430完整两段后/“解释模型也有自己的Faithfulness Budget”前单段，与已有额外thinking分支并存；自身trueH2注。待reader一次原稿核/root窄授，不先写Books：

> 已学事实能逐条取回，也未必能在一次前向中隐式组合；检验时可将实体及其中间关系桥严格分成人口，给所有实体atomic事实，只让一部分在预训练中出现组合上下文，再把新组合与从未组合暴露的人口分开测。[受限自然语言传记对照](https://arxiv.org/html/2606.09338v1#S3)中，后者即使两个组成的单hop都答对，2hop仍未成功；隐式或混合格式可帮助已暴露人口，但显式桥名可读本身不保证组合；所测增强均未带来该人口间迁移。这是GPT-2规模、单seed与单前向协议下的负面证据，不证明任意架构存在普遍容量上限、信息完全不存在，也不反驳上面的额外thinking访问训练。部分augmentation还损伤单hop，完整微调的组合恢复又伴随留出人口遗忘，故须共同检查事实保留、实体/桥暴露与真实组合行为，不能用总训练token充足或桥名可读自签可迁移算法。数据制备、全部预训/微调与rank选择均计费；目标人口未验证时，保显式分解、检索或独立访问训练并分别验收，不从局部失败推出无限补数据或普遍无解。<!-- source-family:SF-2026-ARXIV-2606-09338 -->

## 09079 FlashMemory-DS-V4（2+2+2=6）：未来读取标签离线化的容量/质量替代分支

作者实读exact-v1 §2–4、Figure1 caption硬件披露；不借后版1M/2.8×throughput/2.7×concurrency。模型仍保全部128:1 HCA、原prompt最后8K和所有decoded local CSA；其余历史CSA留CPU cold pool，预测每64decode step一次未来窗口的粗集合，三层10/12/20 OR阈值≥.5取回GPU后，native indexer在子集内细Topk，故这是近似限制主attention候选，不同于Janus exact selection corrective-read。CPU pool/keys、HCA/localwindow、query projector、搬回/细选全须计费；并不只存13%全部模型状态。

§2.2离线冻结backbone抽future64步各CSA层score，softmax/top-p .6/至少3层vote后union伪标签；不是正确性gold。固定K_IComp与hidden/labels预抽，只训练query投影dualencoder，BCE/focal/负采样3:1；singleH20hour仅optimizerloop，不含10K documents16K–512K的巨大backbone数据制备及500-run/week sweep。§2.4 interval64与threshold.5没系统消融，3layer取舍也无全layer causal归因；r2048是architecture query projection非PEFT LoRA。

§3 Figure1仅8H20/SGLang部署日志KV footprint，模型DSV4Flash；precision/batch/onlineconcurrency/latency/CI未披露，不自行补造。Table1等保HCA/local控制，RULER128/256K为94.3→93.2、90.5→88.2反退，其他平均77.5vs76.9非无损或‘denoiser导致’因果。平均13.5%作者表述是KV footprint聚合，不拿.42/3.90不同聚合比改叫总GPU比例。Table2 no-context125K→500K仍.26→.65GB非O1；MRCR76→48，oracle top50%仍退约2点说明dense-dependent人口须独立验。没有control把失败唯一归因frozenkeys/shallowdot或RoPE，§3.3.3‘exactly2×’仅作者局部诊断/未给曲线统计，不采普遍hard bound或不可逆1M失败。未核代码/复现，中心可保有限机制/反侧而非全部营销因果。

actual`INFER-KV-CACHE` Ch45:394–465与486–512已读：Janus保exact候选的预取、RaBitQ按mass、PrHS跨步复用、prefill聚类短表和latent memory均有，但没有未来多步pseudo-label预抽/固定key的backbone-free query训练及outergate→native innerTopk。拟在RaBitQ完整边界段后、PrHS“反复支付selector…”前单段，属未来horizon预测的替代分支；只本人trueH2注，不改已有各段。待reader必要/actual owner/唯一literal一次核后root窄授：

> 另一条容量分支不只近似当前排序，而是离线把未来若干Decode步骤的历史命中合成伪标签，固定预抽的Key与hidden state，只训练query-side检索器；运行时周期预测要从CPU取回的粗集合，再由原indexer在其中细选。[受限lookahead方案](https://arxiv.org/html/2606.09079v1#S2)仍保全局压缩状态和局部窗口，省去训练loop中的大backbone，不免前期backbone trace、伪标签制备、搜索与搬运费用。外层漏召回会改变可读历史，不能继承exact预取的补漏保证，也不能以减少KV推出更高服务吞吐。作者同模型长context对照存在RULER退步，MRCR更明显反退；无context任务的绝对保留量仍随候选历史增长，pointwise gate并不自带O(1)容量。阈值/周期、密集历史依赖与长度迁移须随质量和完整费用共同校准；未验证人口或索引漂移时，扩大取回集合、恢复完整读取或保守offload，不把局部平均质量接近当无损、安全或固定长度外推保证。<!-- source-family:SF-2026-ARXIV-2606-09079 -->

## 08327 CHIAR-Former（2+1+2=5）：局部bundle报告，中心条件争议H

作者与reader各实际读exact-v1 §3–8全部相关main（不是所有代码/附件）。4层/d256/4heads/T256、17.4M对16.1M、WikiText103118M与WikiText2 2.4M、IMDB/ListOps同GPT2BPE，AdamW10LM/20cls epochs、L4/约4h每run/总120GPUh。v1主表WT103test35.92 vs63.95，但WT2 83.81>75.19、IMDB83.72<84.96、ListOps63.35<98.85；无独立seed/CI，不把IMDB1.24gap<typicalvariance当等价，不能从不同task/人口断言‘token diversity决定’的成立边界。六routing表全attentionGFLOPs .705，非实际gate/真实wallclock证明；total/attention GFLOPs口径不闭，1000steps collapse‘before peak500’文字自冲突。后版反向小corpus/400M/MetaRouter不倒填。

§3 Theorem1中心链有明确反例：单个高频DCTbin能量可H=0，低entropy不保证集中低频；也不推moderate→RBF或high→minimal sufficient fullattention。§4 DCT/iDCT轴是feature d逐token滤波，不是跨token mixing，不可把fixedFourier序列mixer当同一机制。threshold在posttraining按validation33/67percentile的时点与训练gate关系未闭，不能照录可执行一般配置。§7承认formalproof待做，但这不是已经证明理论。Collapse后删RBF在该局部bundle较好，不证明RBF一般冗余或通用collapse发现最小充分operator。

actual作者与reader均读Ch14:487–520、Ch17:1–55/155–215完整。已有projection-free/RBF、Fourier/Haar mixer的独立归纳偏置及contextmixing vs pertoken变换/残差/费用，但并非08327同源覆盖；不能借‘现有一般警句’判E。保准入5，局部四任务bundle及反侧仅报告；核心entropy→operator充分性/data-scale因果边界争议H隔离，Books无新diff。不是因小模型或理论有错删候选，也不为造diff复写成熟‘collapse不必失败’。重开需正确H→error条件、calibration时点与真实gate、matchedcapacity/seed、data量/任务因素对照或具名勘误，只重开中心主张，不扩完整实现。

## 08048 PoE-Bridge（2+2+2=6）：候选到目标的局部桥接，非exact correction

作者实读exact-v1 §3–7及AppendixA必要，未全附件/代码。DLM用同chunk prefix的mean-field边际近似逐token条件Eq5–6；Eq9 sequencePoE不可直接采，Eq10另定义每位置归一的PoE（不是相同sequencegeometricdensity）。先从DLM经accept/residual推向bridge，K个候选再按AR/bridge likelihood重采；w控制接受率/近似质量，V窗口减少多余verification。AR target仍是目标而非最终exact法则，pD概念定义与实际chunk proposal不混。

关键反侧：有限K有bias；§4.3 Eq16明确温度间normalizer不可共同消去但实现为简单省去，不能借K→∞的标准IS定理替这实际mixedtemperature/variable-length stopped候选law签asymptotic保证。Eq14 sequence tempered law与Eq15逐token归一也不能直接等同，本文只采proposal/局部bridge这一经验取舍。Elastic window本身不修复全部近似，更不授output-distribution unchanged总算法保证。

评价Dream7BInstruct→同tokenizer Qwen2.5Math/Coder7B，BF16/A10080GB、batch1、双weights常驻；w=.3/K4/V32，温度.2–.7/target.2。AppendixA三seed均值但无CI，MATH仅首215题；PoE/DLM最多2048新tokens而AR最多16384不同截断，吞吐仅EOS前generatedtokens/decodingwallclock非onlineSLO/同质量对照。Table1 PoE所有四任务仍低AR，HumanEval79.47还低w/oIS80.69，非IS普遍提升；Table2 w=.3比w0质量略低，较大w质量速降。V/K依并行度负载共同折中，未研究multiquery/跨tokenizer。未核实现/复现。

actual`INFER-SPECULATIVE-DECODING` Ch48:964–1046及1080–1124完整已读：已有DLM边际与ARprefix条件差、exact验证路径及SMC粒子重采/有限误差/元数据分责，但缺局部PoE桥先接受再resample及mixedtemperature normalization身份。拟SMC两完整段后/“经典speculative decoding以共享条件…”概括段前一段+trueH2本人注，不改已有SMC/概括；待reader必要/owner/唯一literal一次核/root窄授：

> 若DLM并行候选与AR目标相差过远，另一条近似分支先在每个位置把两者概率几何插值并归一成bridge，以其接受/纠正候选，再对多个候选按AR/bridge权重重采。[受限PoE桥接](https://arxiv.org/html/2606.08048v1#S4)把直接低接受率换成bridge权重、候选数与质量损失的联合选择；它不保持exact target law。混温候选扩大多样性，却需要各proposal自己的归一常数，实际省略这些常数不能由标准IS一致性代证；有限粒子、chunk条件近似与候选停止长度还须共同验。作者单A100/同tokenizer双7B、batch1结果各任务仍低于AR，部分任务加入重采反而较差，生成长度上限也不同，不能把接近accuracy与吞吐拼成同质量保证。两模型驻留、候选生成/评分、纠正与重采全费；只允许近似且匹配质量/真实预算时选择这条分支，需要严格law、结构化输出或质量回归时保经典acceptance/residual与target-only，不由较长接受前缀签无损或并发SLO。<!-- source-family:SF-2026-ARXIV-2606-08048 -->

## 08411 AsyncLane（2+2+2=6）：mutable prefix refinement与frontier advancement的解耦

作者实读exact-v1 §3–5全部相关机制/评价/直接反侧，未核实现或复现。标准blockwise只有一个frontier，AsyncLane在task-specific delimiter（数学period含numeric排除/code newline）加fillratio/minsteps门后把gen拆成refine+newgen，prefix仍可改而continuation立即消费fork时旧状态。两lane独立clock/tree；refine禁止EOS，gen可EOS，validprefix若0则stopspawn；最终DFS先refine后gen，leaf遇mask截断、gen另按EOS截断，是offline output reconstruction不是用户稳定streaming commit证书。Forktime prefix会stale，周期refresh仅meaningful prefix+margin并复用logits，非exact纠正/无误差界。

共享prefix分组batch降低call数而非token计算，lookahead只高置信非EOS填mask、后gen继承；Eq13需同时计fresh/refresh与reuse，不拿总call NFE代整网FLOPs/输出质量。§4 same-pretrained LLaDA/Dream不微调、singleH100/batch1，256/512/1024预算，同block/denoisebudget；precision/重复seed/CI未披露。d3LLM-TF去训练组件只inference-side，非完整d3LLM优越性。所有TPS更高不免多lane/缓存/分组/refresh费用。

直接反侧：Dream GSM8K-CoT、GSM8K等低于vanilla，LLaDA GSM8K各长度也低；不以competitive叫无损。GSM8K-CoT boundary-coupled73.39/TPS144.19→async74.91/166.15为受限同界对照，commit-no-refine68.46，说明不能只早commit。诊断positivelead8%/overlap7.4%支持发生异步但不授所有fork都充分重叠。No-lookahead更短输出/质量67.02 vs74.91，故NFE/token与所有输出token人口要保；delimiter多fork/固定K16均反退，规则边界并非通用语义closure。

actual作者读Ch44 154–238及trace382–386，正文只有AR cadence/结束/状态与泛优化，无本机制；trace“已吸收”不能当正文E。唯一更精确owner按ROADMAP为`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，185–255完整已读：该节明确mutable tokens/cache/streaming commit但缺fork-refine/gen双clock和stale prefix刷新这一具体执行状态分支。拟在“图像和视频往往容忍…”完整段后/“去噪器内部还可…”前一段+本人trueH2注；不改Ch44或跨章复制，不移动旧trace。待reader必要/actualowner/唯一literal核/root窄授：

> 对block-wise masked diffusion，未来区域也不必总等当前块完全填满后才开始；一条[受限异步分支](https://arxiv.org/html/2606.08411v1#S3)在规则delimiter及进度门后分出两条lane：旧prefix继续refine，continuation先用fork时状态向前生成，各有局部clock，最终按树顺序重组。前缀仍可编辑意味着后lane消费的缓存可能stale，须显式记录fork/state身份、refresh与EOS/未解mask的停止传播；这不等用户已经收到稳定prefix，也没有取得原采样law不变的保证。共享prefix分组、lookahead继承和refresh-logit复用可摊call，却不消除token计算、缓存与重建费。单H100/batch1的同backbone对照支持此局部速度—质量取舍，但多个任务质量反退，更多fork也可更差；规则标点不认证语义closure。边界不稳、历史修订或净质量费用不合时，保同步block completion、完整刷新与更保守提交，不由少NFE或早advance签流式一致性和并发SLO。<!-- source-family:SF-2026-ARXIV-2606-08411 -->
