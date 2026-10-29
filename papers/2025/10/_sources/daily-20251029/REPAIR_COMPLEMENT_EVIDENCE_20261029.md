# 月表有界补检必要证据

Writer仅首读W11分配16项，reader其余16+四含糊及23142定点；原件均为本日`REPAIR_CORE_2510.<ID>.raw/.txt`精确v1。无实现运行/复现声明。下列为writer实际采用判断，Books仍须实际owner比较，不以本笔记预授整合。

16份currentabs NOTICE的comments/明确撤回信号已实际轻读，无撤回；22037后到ICLR2026、22139NeurIPS2025、22172CCL2026不凭venue授更早first。22115当前注仅技术报告，v1封面Oct24与早权重已另恢复：官方README至Oct29最后Sep22、全仓最后Sep26，树无report/pdf，早README仅权重/FP8介绍，未见本技术报告及异构MTP分区具体正文/链接。封面不是公开日，不借权重首发搬移论文；本窗按Oct28合法arXiv界处理技术报告新差额，有限具体渠道已止。

## 22037 Adaptive Transfer Scaling

实际读§2–6。10M–8B、64K SentencePiece、MADLAD400语料、主要九语/部分50语、750余训练run，loss用vocabulary-insensitive量，N/D/C/mixture分轴heldout。目标unique/repeated exposure、具名transfer语言与other分开拟合，top3按共同采样选择，不只language family。BTS仅80pair实测其余预测，script/family相关非因果，不把完整矩阵当全实测。微调vs从头交点依所选Unimax checkpoint和预算，不含公共基座沉没成本；Figure7和正文常数冲突，不采精确通用采购公式。采用目标/来源曝光与重复饱和分别估计、迁移方向不必互惠；2+2+2=6，长期差额深入，不外推1T/任意语料。

## 22099 Dynamic Mode Steering

实际读§3.2/4全部、5设置/表、6消融与A1。所谓memorization标签由prompt族+50采样edit-distance低/高筛选，A1实际GSM8K vs TruthfulQA来源本身混杂；不是观察训练集逐字身份。跨不同clean/corrupt题的activation patch改变答案，不足隔离单一“记忆/泛化”因果模块；IB分解须Markov条件，也不授当前probe测到互信息。Llama3 8/70B三bench局部收益，强steer反退；probe训练/离线patch并非无训练总预算。“泛化真值sensor/因果唯一开关”不采用，保条件proxy驱动centroid steering与独立下游回归这一局部候选；2+1+2=5，不据争议删除有效局部结果。

## 22102 VPSG

实际读§3全机制、4.1、4.2结果条件、4.3消融。Qwen2.5VL3/7B、ScreenSpotPro1581、greedy，grid选alpha/decay但独立选择隔离ND；多视觉PE shuffle辅助路由取log几何均值作负证据，FSM只调坐标数字位，较高位起强/逐位减并在y重置。shuffle后坐标聚集是局部直接反侧，但不是证明所有高分辨率输入都丢PE、或该reference严格do无位置信号。多路开销/完整latencyND，非digit logits不改也不等归一化概率不变。可采用位置敏感负控制和数字grammar分责，2+1+2=5；不授全视觉任务因果/所有坐标可靠。

## 22115 Ling 2.0

实际读§2.1/2.2及§5.1–5.2全段和5.3相关反侧。非把MoE/MTP/FP8沿用本身当新贡献；具体差额是MTP Transformer与loss拆成独立PP单位、每VPP可不同数量含空stage、只重算MTP Transformer不重算logits。Ling1T baseline modifiedMegatron.11、2016Hopper、TP1/EP8/PP21/VPP2、4K/fullrecompute；局部MTP约1.7x MoE，partition后40%相对端到端提升，单MoE VPP对routing imbalance更敏感而可无净收益。FP8[1,128]激活/梯度、[128,128]weight、FP32scale/accum，900B-token lossdiff≤.25%非全部训练误差保证；on-demand transpose减的是两份FP8权重中的缓存副本，不是全模型内存50%。采用异构调度/重算与数值回归联合合同，2+2+2=6；first具体恢复见本文件首段与本日W15，早权重release不替早全文。

## 22139 NMKE

实际读§3全机制、4.1、4.3–4.5、C限制。AlphaEdit更新加neuron mask，正attribution频次/最大值两score，entropy调一般/特定比例；ZsRE/CounterFact2000顺序及下游回归有局部支持。Eq3声称loggain但右侧写softmax差、Eq7归一max attribution未保证非负，不能照录完整数学配方/entropy安全。正文第88层与caption第8层冲突，tSNE聚集不认证知识原位保真；“general/specific”只是激活分组，不授真实知识实体唯一定位。稀疏不等长期无干扰，dependency closure仍futurework。采用update support/记忆编辑成功/保留能力分验，2+1+2=5，中心精确recipe不采用，普通Books比较继续。

## 22141 LOC

实际读2D→3D全机制、dynamic/static densification与DCL、实验设置及Table3/4消融。OpenSeg/CLIP、trackingIDs/3D boxes、Poisson+KNN生成密集标签，所谓self-supervised不等无标注权限；sparse KD仍在，DCL对dense voxel与text class做InfoNCE，不是完全取消蒸馏。nuScenes/Occ3D，unknown训练排除且mIoU忽略unknown；AUROC/FPR95与closedclass mIoU不同分母。nearest-neighbor dense feature传播可同质化，替换DCL/CosSim有局部对照；不同语义teacher和监督也变，非所有收益唯一归因contrastive。2+1+2=5，采用几何密化与语义标签权限分责、不授未知物体真值或闭环驾驶安全。

## 22172 M-CIF

实际读§2全部、3.1/3.2、4.1–4.3。char→phone→BPE(subword)三级CIF/CTC及quantity约束、G2P字典额外监督；Paraformer12+12/256、八3090、EN/FR/DE150epoch而ZH50，65.39M vs60.11M基线，非完全等预算。8.86→8.55、21.80→18.75、19.48→15.27是WER百分点差，正文误称relative%不沿用；ZH7.06→7.24反退。PE公式若未限定错误对连正确同音也可计，不能照录新指标为独立oracle。采用多尺度边界监督需按语言/token单位分验，2+1+2=5，不采语言类型决定机制的普遍因果。

## 22207 Error-Bounded Predictive Coding

实际读§3全codec/开销、4.1–4.5与A2 rank-residual。BERT/RoBERTa/DistilRoBERTa、WikiText103/V100/五seed；kept positions、overrideflags、rank及fallback须完整共享model/tokenizer/coder，rank在相同masked context才可解。Appendix rank残差构思可用，但正文fallback二元字母{s,not-s}的s依赖未知原token，未给decoder如何知道字母映射；“optimistic/overestimate”两处也冲突，现码长不能认已闭合可解码bitstream。refinement如重写已纠正位置也不自动保无损，CharFid≈1非事实/逐字全等；重复document摊薄静态模型与真正单份成本不同。2+1+2=5；保“模型预测+显式残差+完整bit/失真合同”的提案，不采52–63%已验可解码压缩优势或error-bound保证。完整可互解bitstream/一致cdf与纠正后不改写需后到方可重开该中心性能采用，非正文普通未读受阻。

## 22255 PACR

实际读§4全部推导、5目标、6设置及7.1–7.3。ground-truth answer在training可得，step前后teacher-forced logprob增量并非免标签或免费reward；oracle条件下KL非负若来自一致joint可成立，但文本不同orderprompt未证同joint，且给了正确答案不保证生成faithful过程，不能倒推高增量=正确推理。Qwen2.5Math1.5/7B、Qwen3-4B禁thinking，MATH/五mathbench、8H10080G、三seed，终答案MathVerify。额外每步评分计算未给端到端等价cost；minmax全相等时分母零未闭，不照录稳健实现。保gold-conditioned dense shaping与独立outcome/process验收，2+2+2=6；不授过程faithfulness/更少wallclock或任意policy-invariance。

## 22256 SteerX

实际读§4全部、5实现与消融/threshold/强度反侧。Contriever仅top2history，leave-one-history-out的token logprob差筛anchor，Qwen2.5-1.5B打分、Qwen3-14B总结，再CoS logits或CAShidden steering。去history干预同时改变内容和用户信息，不等identified真实用户偏好do；rouge/meteor/bleu/bertscore提升不等用户授权/满意度/事实真值。Qwen3 8/14B/A100A800/greedy、review与topicwriting，过强steer/过阈值退；额外检索/summary多模型费用未抵消。2+1+2=5；保derived profile的来源/选择/验证分责，非“免训练所以免费/隐私已保”。

## 22376 Smoothed Gradient Ascent

实际读§4全部、5.2设置/指标与反侧、A2。normaldata可由retain近邻或GPT4omini生成，TOFU1%/Llama2-7B OPT2.7B Phi1.5B；并非真的只forgetdata无其他信息。r可正负，合成“label”可负非概率分布。Eq5展开与Eq6的r项符号不一致，Eq9仅给已假设d(r)最小norm且未加forget有效约束，不证明最优遗忘/全程稳定。作者承认r随训练变而实际固定，优化依基座/数据。KS高p不证明retain-only分布等价/删除，极端r仍collapse。2+1+2=5；采用遗忘方向与safe再学习混合的局部取舍，拒绝精确最优r/可认证删除保证，不把整候选因中心理论过度推断抹去。

## 21954 Model-Aware Tokenizer Transfer

实际读§3.2–3.5、4.1/4.2与C层选择直接反侧线索。共同最小字符串segment对齐两分词，取segment末token query，按segment汇总attention-weighted V匹配；student除新input embedding外冻结，overlap embedding固定、FOCUS初始化。不是只对齐attention概率，也不证明知识只在FFN。Gemma3 12B乌克兰语240M tokens及4B/Qwen3 .6B五语约50M/语；H100单卡局部迁移预算，heuristic预处理语料/训练成本不可忽略。tied input/output有利，untied更弱；多层AIM相对单选层反而退，12B翻译BLEU仍低于原模型。压缩率提高不直接授端到端50%加速，新增vocab扩大LMhead成本。采用跨tokenizer比较须共同segment和后层交互/输出接口分验，2+2+2=6，因可能长期差额深入受影响内容。

## 21961 PUNT

实际读§3全机制及4实验、4.2短答直接反侧、4.3误差定义。按confidence排序，二分anchor/test，增加tentative anchor后KL变化裁冲突，合并同层测试需Independence Stability假设；这不是一般Transformer必然性质，零attention与分布不变的双向等价未被证明为所有网络定理，间接路径/取消效应不能静默排除。递归与迭代KL方向也相反，不照录成唯一精确配方。Dream7B/LLaDA1.5 MTBench/IFEval与数学代码局部比较；log|M|次额外前向/denoise，短答NFE收益不稳，不能以step数代wallclock/SLO。采用“并行选集还需测条件依赖、置信高不授联合独立”的可检验替代接口，非采样分布精确无损保证；2+2+2=6，长期差额触发深入。

## 21983 Persuasion fingerprint

实际读§2/3.1/3.2–3.4/4限制。WizardLM-Uncensored按七框架重写AdvBench520，六开源家族Ollama；同一query多次改写任一成功与原单prompt不等query budget，keyword ASR及info_score均非人类心理/模型独立指纹真值。Table5不同模型排序确不同，但单生成器/单数据且无多seed/跨域复验，不能认稳定人格或独特forensics identity。局部反侧足支持安全回归须分模板/家族/预算与有害判据，不仅普通新攻击率；2+1+2=5。可采用局部异质性，psychological成因及普遍fingerprint不采用。

## 22007 Watermark pseudorandom collision

实际读§3.1完整两级分区、3.3条件、6.1/6.2及8限制。重复context共用PRNG seed，再按observed token分子块；Gumbel统计可在不同token子块独立，inverse-transform不能沿用同一细分权限。跨块独立是哈希/随机key建模假设，不由敏感性单独证明；不采所有密码哈希输出统计独立的无条件断言。OPT1.3B/C4 human2000、生成直至300unique statistics，synthetic含复制注入；raw名义.01约.03而去重复后的局部FPR回到附近，是有效反证。surrogate Δ忽略原prompt，oracle优势不当实际可用。采用有效独立单位不是原始token数、null/population/seed-reuse要入校准；不照录整套最优score/asymptotic theorem。2+2+2=6，FPR设计反证深入。

## 22028 QE length bias

实际读§3.1–3.4、4.1–4.3。WMT24++十语，假设人工post-edit errorfree、同文前五segment逐步拼接，限500token；另Gemini2.5Pro同source五改写取最短/最长且人审，控制source不等完全控制所有语义/风格。MetricX/CometKiwi与两Gemini judge随长增误判，55–64%短偏好是该协议非一般长度定律；部分XX→EN Comet方向异质。训练预测error density再乘长度及有reference只缓解不消除，训练分布因果归因未独立完全控制。采用聚合错误数/密度及同质质量负控制分责；2+2+2=6，具体评价反证深入，不授全域无偏QE或RL收益。
