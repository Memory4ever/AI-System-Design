# 2026-01-27 必要证据笔记（作者工作稿）

本文件只承载本窗实际已读的必要原源。HTML 抓取不等于全文审阅；下列位置为实际采用范围。API 后来摘要只负责发现，事件证据全部限定 v1。普通未读项目仍是待办，不是外部受阻。作者不宣告日级完成。

## 2601.16979 — Critical Sharpness

精确来源：[v1 HTML](https://arxiv.org/html/2601.16979v1)，本地 `v1-16979.json` 段16–76。定义为沿实际 optimizer update direction 使 loss 首次上升的步长 ηc，λc=2/ηc；局部二次近似下对应方向曲率 ΔθᵀHΔθ/(Δθᵀg)，不是无条件 Hessian 最大特征值。只有更新方向与主特征方向充分对齐等条件下才可接近后者。指数试探再二分（ε=1/16，常见5–6次前向）不是免费诊断或硬件吞吐结果。OLMo2 7B 公共 checkpoint 分析不是重新预训练；DCLM/数学数据混合的临界交点约0.7与1B-token实际微调较佳0.6比较，只支持特定数据混合诊断。更广 Dolmino 比例分析未做完整下游验证；不授最优配比定律、独立因果或大规模重训收益。

## 2601.16971 — ARMD

精确来源：[v1 HTML](https://arxiv.org/html/2601.16971v1)，`v1-16971.json` 段22–98（关键段62–63另读）。masked loss 的查询和 KV 都必须排除当前块，否则单独 strict mask 仍可泄漏标签；共享权重的 causal X/strict G 双流和前半层上下文构造，使全部条件项一次前向并行训练。一次前向不等于相同 FLOPs，双流成本不能漏记。Soft Block Parallelism 在各流内顺序，在流间并行；随后块条件独立是近似，不能宣称精确联合采样。125M/345M、OpenWebText、seq1024/batch512，基线迭代预算与附加 SBP 微调不完全同 FLOPs。Table2 的并行质量下降反侧有意义；未披露生产硬件、端到端 latency/SLO，不将采样步数转吞吐。迁移已有大 LLM 仍是未来工作。

## 2601.16956 — DataStates-LLM

精确来源：[v1 HTML](https://arxiv.org/html/2601.16956v1)，`v1-16956.json` 段39–103。DataStates 既有 lazy immutable capture/coalescing 是前驱，不重复当新增；本稿的 state-provider/composite-provider 将3D分片布局、驻留类型、序列化与 byte chunk 迭代交给状态 owner，I/O engine 不猜模型布局。Fwd/Bwd 参数不变期捕获，optimizer step 必须等 capture 完成；host cache 满则等旧 flush，不能笼统称 checkpoint 异步就无停顿。固定 tensor offset 与动态对象日志/end header 分工；C++/CUDA pinned circular buffer、独立 CUDA streams、liburing O_DIRECT 是作者实现说明，未自行运行。Polaris每节点4×A10040GB、512GBDDR4、2×1.6TBSSD，最多64节点256GPU，Lustre峰值650GB/s；seq2048/microbatch16、TP4、BLOOM/Llama负载。15steps每步 checkpoint 是高频压力，另有7B频率2–10测试。effective throughput 是全局bytes/训练受阻时间，不是持续落盘带宽；不合并正文/摘要不同最大倍率，不宣称故障恢复/耐久性经实验验证。完整恢复与非参数可变buffer一致性尚非本稿已证明事实。

## 2601.16934 — Long-document embedding fairness

精确来源：[v1 HTML](https://arxiv.org/html/2601.16934v1)，`v1-16934.json` 段14–76。六语言Wikipedia、每segment1000–2000tokens、3–6段、最长8192；同一segment-set枚举顺序控制内容混杂，OLS误差按segment-set聚类。mGTE的<s> pooling与jina-v3 mean pooling均出现首段偏置；英/中语言偏好会抵消位置惩罚，因此不能只测 monolingual lost-middle。几何cosine指标不是真实召回/排名公平或语义真值。mGTE按128/512-token basket、特定层<s> query row等总mass校准，保留篮内相对分布；可减位置偏置却使 later English/Chinese 相对更强，不能把统一attention当全面公平修复。standalone embedding不校准对照减轻共同坐标变化解释，但没有下游检索评测，仅两encoder模型，校准主要单模型；不推广decoder/全部pooling。

## 2601.16905 — GRIP

精确来源：[v1 HTML](https://arxiv.org/html/2601.16905v1)，`v1-16905.json` 段22–82。router变化可令忘记损失下降却绕开仍持有知识的expert；固定retain representations上 ΔΘX=0 是充分的score不变条件，不是任意未来输入/所有深层状态的无条件保证。选中专家等式、未选专家selection-margin不等式放宽全局零空间；随机半空间投影近似交集。前层更新导致 X 漂移，旧projector失效；PTC用新旧表示和regularized pseudoinverse做后校正，不将正则least squares写为全部分布精确保留。Qwen3-30B-A3B、WMDP/MUSE，Table1 RS/retain有效反侧；强制forget routing-shift queries走top5非选expert为有限白盒测试。

直接反证：表4 forced FA为baseline .26→.37、GRIP .24→.27，而段65/71/77另称5.3×、61%→3%、指向不存在的§5.5；正文指标/叙述不一致，**不采用这些恢复百分比、必要充分、neutralizes steering或black-box timing attack保证**。几何机制和具体evaluation shortcut可保留；真实知识抹除、安全保证不由该测试推出。A.1配置与attack定义已定点读完（见后续补充）；数字冲突仍隔离，非普通未读。

## 2601.16873 — Provably Learning Attention with Queries

精确来源：[v1 HTML](https://arxiv.org/html/2601.16873v1)，`v1-16873.json` §3–4（段18–65）、§5.2（93–109）、§6 assumptions/error（111–117、143–157）、§7（158–168）。输入可任意选择实向量矩阵 X，输出为**精确 scalar regressor value**，并非文本token API。单头合并参数 W=KᵀQ、v=Vᵀwo；v≠0时长度1查v、长度2反sigmoid构造列线性方程，O(d²)恢复合并参数，不能恢复唯一Q/K/V。v=0不可识别。已知rank≤r的随机rank-one matrix sensing在相应条件下O(rd)。噪声不自动无害：已知范数界W、各|vi|≥μ与可控oracle精度 O(με/(W²d))，clip避开反sigmoid边缘才有界误差。多头相同W、任意分配v权重可同函数，参数识别非唯一，但不是证明所有多头函数不能学习。FFN reduction与完整多层LLM、离散token访问均未采用。不授真实API盗模定理。

## 2601.16853 — Reasoning / Theory of Mind

精确来源：[v1 HTML](https://arxiv.org/html/2601.16853v1)，`v1-16853.json` §3段44–99、§4.1.4段123–126、§4.2–5.2段211–234。自写ToM扰动任务与既有benchmark二手结果必须分开，benchmark未重跑。Claude thinking-on/off是同服务行为开关，不是同base-model/RLVR因果消融；API温度/trace/追问不同，表1模型信息不统一。Table5 transparent-access与relationship-change使所有tested模型继续失败（或部分分），不能用整体平均宣称真实心智。可采用窄反侧：在这些新编prompt扰动中reasoning版本表现更稳，但仍有共同失效；模型规模/训练/服务差异及prompt已知性未排尽。作者§5.2明确未量化RLVR贡献、base不可得、trace不忠实、未与其他test-time scaling公平比较；不授RLVR新能力/稳健性普遍因果结论。仅报告局部行为证据。

## 2601.16823 — Chess prior-density

精确v1 `v1-16823.json` §3–4段19–72（模型/协议51–60另读）。1500位置分三组各500：Lichess Masters出现≥1000为WD proxy；10随机legal moves且不在数据库为ND；每侧随机摆10pieces且legal为OOD proxy。模型训练集未知，database frequency不是真实membership，不证明记忆与“fluid intelligence”被干净分离。Stockfish17.1 depth30评move；illegal统一1000CPL，另有排除illegal再相对randomlegal ACPL控制难度。GPT-3.5/4o/5 API不是同规模/同训练受控，不能授architecture/scaling瓶颈。最小采用：此分层下GPT5增reasoning仍未消除低density退化，且更多tokens的收益/成本与熟悉度相关；不外推数学/代码纯记忆。正文“ACPL reduction >100%”表述不作正常百分比收益，GPT5 moderate与固定temperature声明需API约束，未复现。

## 2601.16781 — P-Tokens

精确v1 `v1-16781.json` §3–5/limitations段12–58。只训练BEGIN/END_EDIT embedding，KL向长IKE demonstrations teacher靠近；paraphrase、邻居保原输出、distractor、无edit四种loss约束，不是对每个事实重新改baseweights。CounterFact800train/200val/1000test、zsRE800train/200val/19086test，zsRE无IKE demonstrations，不能把两dataset都称同teacher比较。GPT-J6B/Qwen2.5 7B14B/Llama3 8B；Table2多edit distractor使邻居NS显著退化而ES/PS高，不能仅看edit success。Table4 Qwen7B batch1、20P-tokens prompt58 vs IKE959、.03s vs.17s，训练15h28min约398k次amortization；硬件未在正文披露，短prompt不等于所有成本下降。不同facts/update/retrieval以及非文本API embeddingaccess边界仍在，仅报告此learnededit提示选择，不授持久truth更新或隐私保证。

## 2601.16725 — LongCat早正文去重

已读v1 §3.2–4段61–107（`v1-16725.json`只保留必要slice）。新的多轮DORA内容不能当旧DORA首次，也不能重复算domain-parallel前驱。更关键：官方 `longcat-history.json` 的PDF路径最后Jan23T13:22:36Z a02fe00，首添加Jan23T09:58:45Z；`longcat-early-pdf.json` 实际读该commit PDF第1、9、10页，标题/abstract及streaming samples、multi-version、controller拆分、PD/CPU KV机制已存在。因此这些采用命题的正文早于本窗，arXiv再收录不改变归属；本窗不列确定candidate，未假称早事件已被他日报处理。历史PDF并非此刻当前main，精确链接保留。无需读旧版完整附件或扩大本窗。

## 2601.16651 — Gradient select vs project

精确v1 `v1-16651.json` §3–6/limitations段17–85（19–50、63–84另读补截断）。终态gradient cosine的retrieval surrogate：988 LIMA fine-tuning样本、GPT4o-mini改写与model生成completion、BM25 top5先限定candidate。组件dot/selfdot可求任意subset cosine，再按retrieval accuracy greedy选；randomprojection目标是保fullgradient几何，这不等于检索解释准确。AMD-OLMo1.2B一模型、113component、静态final checkpoint，不授训练删除因果。component selection在此retrieval更好是实际边界；正文没有清楚held-out selection/testsplit，不把近乎1.0 retrieval写泛化解释保证。H1004h precompute+minutes search vs RP高cost，但RP caching假想无I/O与不同维度总和不能外推统一加速。

## 2601.16649 — LUMINA

精确v1 `v1-16649.json` §3–4/limitations段13–52。ListWorld/TreeWorld/GridWorld deterministic环境可构造optimal-action planning hint、precise state以及在sufficient state存在时才history pruning；因此是6种组合，不是3独立模块任意8组合。Qwen3 4–32B nonthinking+CoT,temp.7，部分YaRN长context；ICL必须匹配干预格式。不同规模/环境为level task success挑不同horizon再比较，不授普遍能力ranking；oracle收益可部分归因information intervention但不能抹除prompt/instruction following混杂。step>task success反侧及state/history收益方向随环境/规模变化，说明不应单凭end success归因planning缺陷。不能无真实stateoracle就部署history清空策略。

## 2601.16621 — Rational memory utilization

精确v1 `v1-16621.json` §2–4/limits段11–84。953human核synthetic atomic cases；Ignore/Support/Dominate与多preference IA/LKO区分，query“true intent”是标注标签不是用户真实心理或memorytruth。Qwen2.5 7B/DeepSeekV3/GPT4.1/GPT5在explicit memory reminder条件Ignore尤其弱，单项与all-correct multi分别记账；GPT4.1 judge与humanQWK.87只是ordinalerror评分一致性，非独立无偏groundtruth。RPReasoner把模拟query likelihood与intentprior排名相加不是精确Bayesian posterior，额外call/成本未在性能宣传分账；不采用258%相对增长或production80%因果收益。选择memory relevance与recall/事实准确正交的具体评价反侧足够；§limits承认subjectivity，不授inverse scaling普遍定律或attention因果。

## 2601.16547 — CORD

精确v1 `v1-16547.json` §3–4段21–62、70–100。同audio学生onpolicy prefix分别audio/text条件reverse KL、top20 highKL×earlyposition权重，sequence judge answer一致性GRPO；不是用teacher不同轨迹直接逐token对齐。NuminaMath80k+Kokoro配audio，Qwen2Audio7B/StepAudio2Mini，max200tokens，AdamW3e-5；温度/rollout数在正文声明不完全一致，hardware/端到端成本Not Disclosed。§4.3 Table3 GRPO500→1000step collapse而联合OPD训练3000稳定是此设置反侧，不能授所有GRPO稳定化；judge内部蒸馏/99%自评未独立验证，textteacher也会错。Table2 speech能力低于base、sound近持平，不写全部音频能力无损。反向KL文本“更重teacher高概率”与公式audio加权不严谨，采用公式不照录解释。只保留onpolicy跨模态不同轨迹的匹配选择与局部权重trade-off。

## 2601.16520 — TangramPuzzle

精确v1 `v1-16520.json` §3.1/3.3/4段19–24、38–55、58–66。668配置两tasks、1336instances，TCE exactalgebraic坐标；constraint库存/syntax、area/perimeter、overlap/connectivity与IoU/Hausdorff分账，不能以图像轮廓相似当rigid合法。Table2 GPT5.2 IoU58.49而VPR0/Success0、ClaudeIoU61.61 VPR.15/Success0是窄blindspot；“0有效”不是所有形状从来不能解。官方API/default参数、RTX2080Ti仅客户端，不授模型硬件或可公平排行。每件面积周长检查不是通用刚体全等证明；不采用完整物理正确性保证。3例ICL增加syntaxerror却提升部分IoU反侧。只2D/7固定pieces，不外推真实3D机器人。

## 2601.16514 — Shallow Transformer NTK

精确v1 `v1-16514.json` §3/4段27–67、symmetric initialization78–85、transport class117–125、Theorem1/Prop1 142–154、AR(L)实验169–177。singlepooled固定query、各head单neuron block-diagonal、boundedinput与bounded twice differentiableactivation、no deepstack；target须supnorm constrained transport/RKHS class，symmetric initialization、projection radius≥targetnorm、η=1/√τ。有限步经验MSE bound三类优化/近似/线性化误差无显式T，不是任意深LLM generalization。AR lag实验n5000、m64/tanh、20seeds，TransformerT=L+1内存O(L) vs IndRNN O(1)，且实验不投影，不能宣称理论覆盖该训练全部行为；only局部支持gradient/quality-memory取舍。不把length-independent bound写成attention compute/memory independent。

## 2601.16486 — Timely Machine

精确v1 `v1-16486.json` §3、4.2–5.3、5.5–limits段25–49、62–97、106–115。时间记账generation+tools，不等于tokens；textgames人设相同deploymentresource，人工插tool latency使Qwen8B/32B胜负改变，0.6–4B能力低不能仅按速度选。Simlatency是可控评估不是生产SLO；正文hardware未披露，任务特定。TimelyRL奖励超时0、及时format rf、correctreward+sin utilization鼓励使用可用时间，不是仅最小latency。合成timer teacher/coldstart与RL混合；Table3 on-time提高不等于所有accuracy提高。推断为budget必须include tool及能力，不授未知工具未来时延保证；多模态/多agent未验证。

## 日期约束

## 2601.16466 — PHISH

精确v1 `v1-16466.json` §2–3、§5.1/5.3–5.5、limitations（段10–68）。攻击者只编辑history/user input、blackbox inference；system persona未改变。STIR是朝目标方向的连续trait displacement，经量表范围与目标traits归一，不是二元jailbreak成功率。八模型、三评估；polarity/framing controlled ablation支持history cue影响，但reasoning提升不显著，多轮累积局部。ICD/CWD/PFD防护只部分抵抗；不采用“不可检测”“80%成功”或真人人格/临床效用保证。有限reasoning tasks损失1–6points不能证明所有utility无损。心理量表测模型输出，不当真实心理状态。

## 2601.16450 — Floating-point expressive power

精确v1 `v1-16450.json` §2.2–4.2（26–103）及§5.1 construction opening（106–115）。IEEE-like有限float、ties-even、correctly rounded exp/ReLU、所有sum固定left-associative，无遮罩/位置编码的文中网络定义；不是每个GPU kernel。非结合sum使一般permutation equivariance失效，但首二位置交换仍equivariant；distinct-input域上构造只支持这一最小对称。Theorem2以α≥3×2^p、β−α≥6×2^p重复段碰撞，推出n≥9×2^p存在不可表达equivariant函数；n≤6×2^p−2又有表示正侧。位置相加float非injective，额外dimension位置则可避免这种碰撞。只采用精确算术结论不能直接移植固定浮点运算这一边界；不授现实低比特LLM能力下降阈值、所有归约次序或训练难度保证。无benchmark/hardware，理论结果不适用性能分账。

## 2601.16444 — Numerical judge bias

精确v1 `v1-16444.json` §3–4/limitations（15–83）。四public base/instruct pairs（Gemma7B、Mistral7Bv0.1、Llama3 8B、Qwen2 7B），WMT2020 MTQE七对、GECQE；max5tokens/temp.7、每样10次，过滤非数字、clipping后平均，score0–9。instruct输出常集中8但base较分散不代表judge更准。Table5/6 calibration kurtosis与human Pearson不单调（Llama GEC .180→.021）；temperature/range也依task/model。校准用1000采样估p、gold拟合Beta q，有额外预算及label信息；不授无需gold无偏修复。没有inhouse alignment受控训练、训练data未知，不能只由pairs断言alignment独立因果；kurtosis低不等可靠。仅采用distribution spread与评价准确分账的局部反侧。

## 2601.16398 — White-box sensitivity audit

精确v1 `v1-16398.json` §3–5/limitations（28–65、68–71、85–124、131–134）。从train提direction、validation择layer/scale，λ[-1,1]步.2并线性fit slope，不等输入真实保护属性因果。Llama3.1 8B/Qwen2.5 7B/Ministral8B及domainmodels；synthetic decisiontemplates，whitebox移除explicit gender/race与blackbox替换词不同干预。强gender-name cues令I/O差异接近whitebox，是具体surface-test blindspot，不授哪个测量是真实bias量。Sobol first-order independence假设与关联变量限制，top变量≤.01变化未保证全部概念隔离。linearconcept/validation scale限制明确，保持alternative perturbations反侧，不能推广现实医疗/信贷合规。

## 2601.16390 — CLAS

精确v1 `v1-16390.json` §2–4.2、4.4、limitations（17–86、96–97、110–113）。100平行XQuAD计算dataset-level activation masks，chosen bridge layers；partial-shared与language-specific rescale+blendα可负号逆转，English不动。两instructionbackbones、XNLI target-logitclassification、XQuADgreedy32、singleA40/seq512/no batch。200/language/task grid调参未明确与fulltest完全隔离，不采用test-generalization guarantee。XQuAD均值正但不显著且Hindi/Turkish退化；cosine离English更远与XNLI gains相关，不是divergence造成gains或functional circuit证明。采用geometry alignment并非downstream quality目标的有限反侧；不授均匀语言改善。

## 新增decider与最终处置

已实际读：16863 §3.2/3.4/4.1–4.3/4.7–5.5，fixedteams而非runtimeknapsack、votes的Sneaking反侧；16661 §3–6 pairedcomments程序成功/失败互换与length/intent混杂；16506 §4–5 gateway/DDGT/SATE及有限安全反侧；16615 §3/4.4/5–7 fusion旁路与36→40ms；16462 §3/5 graph-only信息损失。exact-v1日期已由identity-extra.json恢复，SafeThinker必要配置与GraphAnchor评价正文已补齐，见后文。16596 §2.1–2.2/3.6–3.7决定性内容实际读后，具体组合贡献关闭；未删已读材料。

`identity-*.json` 保留精确v1的submission history和DataCite created原值。标准官方availability对应本批下界2026-01-26T01:00:00Z（BJT09:00），created仅上界；30项界内可以写推定公开区间，不能补造精确时刻。17111与17086上界分别Jan27T03:42:15Z/03:41:42Z，使区间跨截止；**日期未唯一确认**，不是已经证实归属01/28，不作正面本窗证据。恢复需要同事件首次公开的官方公告/作者artifact时间；不扩大窗口、不遍历完整版本史。

## 抓取异常保留

`topic-model.atom` 是API错误；`topic-model-recovered.atom` 是截断响应，两者不支撑列表完成或候选证据。有效分页为model-0/20/40/60/80/100.json；这些103条是主题提交slice发现线索，不是103篇当窗候选或全文队列。

## 后续必要审阅与工作稿状态修正

以下补齐前文普通待办；前文“新增decider停点”是当时状态，不是最终结论。

### [GRIP v1](https://arxiv.org/html/2601.16905v1)

已实际读Appendix A/A.1：作者声明128experts/top8、2×H20080GB与8×L40s40GB节点、FP8 E4M3/TransformerEngine，AdamW3e-5、每GPU batch2、最多10000steps，validation择超参；硬件标注依作者原值，未自行验证。WMDP到25%或无法继续降、MUSE以原dense C1–C3为停止条件，预算/模型不能认作完全匹配。§5.2明确仅routing-shift forget queries强制top5非选expert。表与正文冲突未解决，故仍不采用恢复百分比及安全保证；必要审阅够，未再遍历无关证明。

### [NOIR v1](https://arxiv.org/html/2601.16354v1)

已实际读§4/6/8–9：client首1末4blocks、cloud中层；hidden-vocabulary扰动、固定随机重排tokenindex与splitfinetune。威胁为honest-but-curious且无encoder访问，不授恶意server/多用户联合防护。token-pair邻接、feature预算加总不是所有代码/整段隐私；γ条件恢复优势是假设。本文未消除跨promptclustering与adaptive cloud LoRA，§9明确保留。CodeLlama7B/CodeQwen7B/Llama3 8B，CodeAlpaca18k扩376k，MBPP/HumanEval/BigCodeBench，pass10不是pass1且10次通信计成本。A10080GB client显存49.92→67.7GB反侧，不能称普遍廉价edge。两同区域server32token/s结果非WAN验证。只采用受限split架构与attack/utility权衡，不采用全sequence DP或所有代码安全保证。

### [VisGym v1](https://arxiv.org/html/2601.16973v1)

§3–4实际读段16–47：12VLM/OpenRouter，每task70episodes，easy20/hard30steps。历史约4步后/全历史可退化，方向随task变化；ASCII对照仅4task且encoding改变，不是全部perception与planning干净隔离。textfeedback缺失会降，goalimage亦可能引发提前结束。token/context与API预算不完全匹配，不授通用排行或17task数量贡献，仅保留history/rendering可比性盲区。

### [ReViP v1](https://arxiv.org/html/2601.16667v1)

§3–4实际段17–81：completion d=1而视觉G=0明确失败事件；外部Qwen2.5VL72B读取taskstage，TSFiLM调制π0，8H100/batch32/60k。perturbedLIBERO8task、ROKAE6DoF+JODELL/2RGBD共50realtrials。新增observer也带能力与成本混杂，没有独立latency/错误结束率全分账，因此不把总成功率提升归因纯vision/proprio分离，更不证明物理安全。新执行失败定义及纠偏分支足够，只保留局部。

### [OnlineSI v1](https://arxiv.org/html/2601.16538v1)

§4–5实际段25–67：Fuzzy-F1将严格visibleGT子集用于recall、宽松GT用于precision，解决partialvisibility下“未看见”与“错预测”的可比性变化，非有限buffer成熟配方贡献。ScanNet++/ScanNet，SpatialLM1B+CUT3R+GroundedSAM，8A800，只train末encoder/semantic/LLM；1–32frames/stride30，过滤全部side<15cm物体。visibleface具体阈值正文未完整披露，采用评价条件而非复现实绩保证；有限memory不保证整个online系统总成本不增长。

### [SARE v1](https://arxiv.org/html/2601.16527v1)

§3–4实际段26–89，Appendix A.3定点配置见sare-config.json。负概念CE反向、归一gradient近似TargetedSAM最坏参数扰动；不是精确minmax或真erase证明。mPLUG/LLaVA7B，COCO30ktriplets/1600val/1600test，mappingonly一epoch/A800/Adam1e-5。relearn140captions或local10k LoRA配置不足以授任意再训练robustness；只采用此有限relearn反侧。sentenceonly降低CHAIR而POPE退化，多epochs仍collapse；双梯度有成本，不照录negligible overhead。支持“此优化路径改变局部再学敏感性”，不授稳定遗忘保证。

### [Memory-V2V v1](https://arxiv.org/html/2601.16296v1)

§3–4及D/E实际段21–67、112–144：缓存为过去生成video的VAE状态，不是真世界事实；64800directions FOV检索λ.5，top3采用1×4×4、其余1×8×8、user1×2×2tokenization。frame平均key/maxquery响应代理驱动token合并，不是安全因果importance。中期10/20步相关支持局部选择，不能证明任意采样早晚规律。32A100训练，ReCamMaster/LucyEdit2k/1k，batch32；40novelview/50edit、>200frames/3轮。Table4从980.8到648.5（秒）伴MEt3R轻微退化，测试硬件/steps/batch正文Not Disclosed；基线是均匀historytoken，不能当无history整个baseline成本。DRoPE解决user/target/memory范围身份与训练推理gap，外部缓存/检索增长仍计账，不授constant总成本。

### [Ascend W4A16 v1](https://arxiv.org/html/2601.16536v1)

§2–5实际段7–33：vector解包/反量化写globalworkspace、cube读GEMM、splitbuffers/reducevector/doublebuffer。4×weightstorage不等4×计算，nativecast在此非主瓶颈；跨unit GMroundtrip与K≫N形状促SplitK。1.01–1.74vsdata-parallel、1.48vsFP16都是作者核级局部shape/batchpadding结果，精确910variant/compiler/software/quantcalibration Not Disclosed，未测试GPU或端到端LLM，不外推。

### [SFC GEMM v1](https://arxiv.org/html/2601.16294v1)

§II–III实际段10–59：Hilbert连续blockrange绑定Ctile，K方向C副本最终reduce。communication界要求fastmemory容纳assignedC/panels，复制和reduction有代价。OpenMP+LIBXSMM CPU x86/ARM，EMR64/GNR128/EPYC96/Graviton4 96核，125shape512–8192，BF16/cold10reps择最佳c1/2/4与Kblock1/2/4/8，不是无需调参。BRGEMM roofline依microkernel，ACL超过它不矛盾；cachemiss延迟并不等价，reduction会抵消收益。未采用所有下界证明或GPU/跨机外推，只保留CPU cache ownership/工作划分选择。

### [NSED v1](https://arxiv.org/html/2601.16863v1)

§3.2/3.4/4.1–4.3/4.7–5.5实际：broker的knapsack是设计而实验fixed3team/persona、max20ktokens、presence1.5/ReAct4k，AIME30×4重复；匿名vote/diagonal mask不是策略proof。数学consensus约6轮peak而code波动；DarkBench Sneaking .741劣于expert .136，HarmGen混合亦劣，不能把群体共识当安全/正确性或MedianVoter theorem证实。采用有限协作危险放大反侧，runtime成本套利未验证。

### [Code comments v1](https://arxiv.org/html/2601.16661v1)

§3–6实际：1100AVATAR/CodeNet、5PL/20pairs、5translator×3commenter，locals A100/API hardware ND。编译+tests仅局部语义oracle，同代码有comment成功/失败集合不嵌套，具体invalidvariable导致100×100内存问题，注释并非单调帮助。author19词/generated5词与GPT意图分类混杂，不认作intent解释独立因果；COMMENTRA retry依已有failingoracle，不能自动检测生产所有错译。保留新增paired failure路径，不把全部comment越密越好/坏。

### [AuroraEdge v1](https://arxiv.org/html/2601.16615v1)

§3/4.4/5–7实际段25–53、67–88：SigLIP2max256/pad→MLP64；独立cross-fusion仍读未压缩256visual+text并经decoder融合旁路送Qwen1.5B，因此64LMinput不等整个视觉路径64token。8A40训练、单RTX3090/640×480/describeimage，36mscompression→40mscombined，outputlength/batch/precision/prefilldecode ND。11tasks9较优非全部；不采用3×实时edge/全FLOPs保证。旁路表示与压缩账本是实际增量，仅保留受限设计。

### [SafeThinker v1](https://arxiv.org/html/2601.16506v1)

§4–5实际段28–94及Appendix C：finalhidden frozenprobe训练约11k近balanced，δ=.7高风险固定拒绝、低风险SATE、不确定DDGT；SATE LoRA256有害prefixtriplets+benigndistill，prefix半0其余1–100/α.2。DDGT topkoverlap cosineτ=.2、k5、λ.8，**仅首2steps干预**。temp.9/top-p.6/top-k50/max256、A80080GB。Llama3 8/Qwen2.5 7英文ALERT32/3200、HExPHIprefix10/20/40及EasyJailbreak，DeepSeekjudge不是独立真值。fullrouteprefill ASR3.3/5.5/4.5比SATEonly .6差，说明router的效率/误判tradeoff，不能说minimalrisk。额外expert显存与probe falseconfidence bypass明确局限，multiturn/promptinjection仍未来，非全程安全。

### [GraphAnchor v1](https://arxiv.org/html/2601.16462v1)

实际§3/5图抽取用query+旧graph+新文档/推理，evolvinggraph索引指导retrieval，答案读graph+raw；graphonly约3%下降及答案plateau后graph仍长反侧，entropy/attention图不授因果。§4 MuSiQue/HotpotQA/2WikiMQA/Bamboogle，Qwen2.5 7/14、Qwen3 32、Llama3.1 8，bge-large-en-v1.5每步top5、最多4steps，F1/EM；runtimehardware/totalcalls成本ND。精确v1名为Graph-Anchored Knowledge Indexing/GraphAnchor，不采用v2 KAIR。仅保留压缩索引丢失与raw fallback条件，非immutabletruthgraph。

### [RLHF generalization v1](https://arxiv.org/html/2601.16403v1)

实际§3/5/6（19–50/74–171，125–148后补读）：truegroundreward已知非learnedRM；boundedlinearfeatures与realizableθ*，Boltzmann固定ref。fullcoverage/covariance条件或residualεn≤O(1/n)，actionfeatures独立且|A|≤d，Γ条件数仍可能依n/d。stationary finitepopulationbound与GA η1/L**bestgradient iterate** T^-1/4+n^-1/2、SGA η1/(2L√t) bestfullgradient T^-1/8+n^-1/2；不是最后iterate，SGA择点另付完整gradientcost。支持coverage/conditioning决定bound的理论差额，不授真实LLM/RM/普遍dimensionfree结论。

### [Kimi CLI 0.88](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.88)

实际release published_at=2026-01-26T13:10:05Z，BJT21:10:05；PR681 exactpatch（35fa76b6…/toolset.py）移除非OAuth RemoteMCPServer且headers未设时注入runtime.session.id的9行，保留用户headers与FastMCP client，不等于删除所有session支持。官方[2025-06-18 transport](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)§Session Management允许server初始化可选分配Mcp-Session-Id；若返回client后续必须带，404重新初始化，不能拿应用runtime.id冒充server会话。只授静态兼容边界，未跑e2e/任意server验证。Ch83实际lifecycle/version/sessionhandle与backend身份分离已经承载稳定原则，缺这个release实例不是knowledgegap，拟仅报告实现case。

## 贡献关闭（不是外部受阻）

16596：已读完整题摘及v1§2.1–2.2/3.6–3.7，自然语言all-pairs critics主要为成熟critic/比较recipe，未识别受控的新失效条件/评价机制；不因所有批评组合或指标提高独立准入。16278：已读题摘及v1核心，fewshot/selfrevision/SFT/ICL合成数据比较，sentiment/intent局部human-vs-synthetic规模曲线可由既有difficulty/diversity/prompt原则解释，没有新增独立识别条件，“非单调”本身不够。16280：已读题摘与精确v1 PDF决定性内容，四既有error类别×三invoice工具，不新增runtime评价机制；NOTINIT混合omission/malformed但无schema干预控制新原因，14B/32B局部失败比例不能独立贡献。三者材料保留，日期不影响关闭不再请求外部日期。AgentDrive16964/LogitMatch16946完整题摘此前已校准，具体无新评价盲区/边界而关闭，非benchmark/recipe类别排除。
