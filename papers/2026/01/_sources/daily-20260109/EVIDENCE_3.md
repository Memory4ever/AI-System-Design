# 后续小批必要证据（作者准备，独立准入/证据待root）

## 2601.03444v1 Grading Scale，2+1+2=5拟准入

完整v1题摘已ADMISSION_3送校准，日期原值DATES_3/DATE_BASIS支持条件公开区间落窗。实际必要HTML §3.1–3.2、§4.1–4.3、§5.1–5.4、Limitations；选取原始方法/对照/反侧保NECESSARY_CORE_4_RAW.txt，不把准入/证据独立完成提前授予。

作者标准审阅：absolute ICC对象是single rater或panel mean，human–LLM比较使用两个panel均值；高panel内ICC不自动支持跨panel agreement。人判人口150=六benchmark各25、12研究生6+6gender，每人评每item每scale；模型six families、temperature1/nonthinking，三scale0–5/0–10/0–100均允许fractional，因此不是粗细离散档位实验，所有数值线性归[0,1]再跨scale比较。重复block顺序随机与itemshuffle降低anchoring/fatigue，但同人重复评分不授独立samples；gender小切片不外推总体规律。

反侧Table4显示STS-B的0–100优于0–5、MT-Bench的0–10优于0–5；Table6仅Llama/Gemini四temperature，Gemini某些temperature也是0–10更高。因此采用的是scale/人口/slice作为评价身份与内部reliability≠human alignment，不采标题0–5普遍最优或作者‘nonartifact decoding策略’的广泛归因。150合并ICC和逐任务25例差异不能当task难度因果；normalised MAE与ICC量测不同对象，human consensus只是本研究生panel而非任务gold。硬件/推理并发/latency/SLO Not Disclosed，非本篇采用命题；没有运行代码或复现。

具体Books提案为已有覆盖：actual Ch66:271依prompt/量表/先验冻结、stability不等human alignment、aggregate不保sample；Ch66:4152–4160 Judge Agreement正文明确population+scale+missing/abstain+pooling+metric及slice。这些实际正文承载本次拟采用长期判断，不说现章已有该ICC公式/三scale全部实验。有限scale案例留报告，不需新增同义框架。Stable owner PLATFORM-EVALUATION-SYSTEM，Current/LegacyCh66/62。等待root准入与必要原源/具体owner独立核。
## 2601.03401v1 Disclaimer，2+2+2=6拟准入

实际§3.2/Alg1随机生成/选取disclaimer接到input、监督y不变；§3.3跳过layer的KL输出变化与hybrid layer交换，只支持模型当前输出依赖/局部机制干预，不证明这些层内部知识已不可恢复。§4.1–4.4 LoRA Llama3-8B-Instruct、bf16/2048/3epochs/cosine，四English QA，GPT5.1二值judge加BLEU/ROUGE；exact model变体/训练策略图示未给全部可比setting，保有限观察而不照录model-agnostic。必要原文已CORE_4。

本文把下游性能降低定义为降低learnability，实验可支持这份behavioral degradation；但能力是否实际未学/信息不再存在需要额外恢复测量。一个保持disclaimer语义/约束的paraphrase并非删除trigger/改读取策略后的恢复攻击。作者依赖aligned model，Limitations明确弱/无alignment不必成立。GPT生成池的K/实际长度、全部learningrate/batch/hardware、随机重复与CI未披露，不采用整套robust版权/数据保护保证；也不把这些不足说成所有实验无效。Table与正文几个百分点描述不一致只避免采用数字，不为局部观察展开数学审计。未运行代码。

拟具体已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66:2975–2988（actual读取）：单次正确率/refusal/抑制不授训练影响移除，support需要reference/provenance与恢复/派生能力；没有reference时仍可以发布受限suppression/policy-alignment指标。这能承载本次拟采用的评价权限边界，而不是说书中已有Disclaimer训练算法。原6局部training-input trigger观察留报告，不添重复通用框架。独立准入/必要证据待root。

## 2601.03648v1 ELO，2+2+2=6拟准入

实际§3.1–3.3首尾decoder+原embedding/head构成独立浅模型，只更新选层，用1:9 bilingual CP；原deep模型首尾替换后必须全模型FFT做1GB alignment，再chatvector/31K bilingualSFT。§5 zeroalignment明显更差、若干quantitative性能差于FFT/原Instruct、仅SFT也接近部分CP质量，不能把整个recipe结果归detached层或首尾层“天生知识owner”。§7明确整体训练peakmemory不降低，200GB以内有限验证不是TB以上普适尺度律。

真实AppendixB八H100、PT1epoch/SFT10epoch、seq8192、ELO PTbatch4/alignment1/SFT1、seed42、AdamW_bnb_8bit。Table1比较stage9GB+1GB与full10GB，token counts按模型/语言不同，A2平均tokens/GB估算也与Table1具体总token口径不同，不拿byte作为严格matchedcompute；SFT/chatvector与独立selection/重接诊断成本要同算，不采用6.46倍全pipeline/保持English无损结论。未运行代码或对未读artifact作已复现称谓。

具体owner差异提案TRAIN-LORA，Ch30:124–141 actual：当前已说冻结不删forward及轮换trainable集合，但没有“摘除执行层成另一个训练函数→装回后全模型compatibility alignment”的替代分支。可在activation-budget段后/轮流更新标题前一窄段：更新集合与执行graph不同，浅CP降低bulkstage但改变上下文函数，必须重接/heldout质量验证；把fullalignment/阶段预算/peakmemory与qualityfallback同账，不授无损/普遍首尾最优。等待root准入/原源/owner及具体写锁，未写共享文件。
## 2601.03666v1 e5-omni，2+2+2=6拟准入

作者实际必要原文§2.2–2.4、§3.1/3.3–3.6及AppendixB；精确片段CORE_4按原页面身份保存。每个input按活跃模态均分w，再对query/target两温度平均作为pair logit温度；负例curriculum按行保留top fraction，DCL对negative aggregate减正项并加数值floor。协方差不是每个模态分别配平：query与positive target合并求同一batch W，再比较两端变换后的Cov。训练logitsharpness、选中negative人口及二阶几何是不同调节对象，不由整体检索分数授每pair相关性真值、false-negative已消除或通用跨模态对齐。

真实Qwen2.5-Omni LoRA/一epoch/512query与target/8H100/batch20×acc2；heldout1K调参。Leave-one-out不是全factorial，whitening/CORAL共同移除不区分独立作用；VOC2007联合PCA+固定32D随机投影的分布重叠不等paired正确性；γ/λ过强反退，QVHighlight/Charades等7B不全优3B。AppendixB仅示训练batch W，没有明确部署W/相似度温度冻结与index兼容协议，因此不采用在线检索收益或完整部署产物结论；不因此冻结所有受限训练观察。无代码复现。

actual owner MULTIMODAL-REPRESENTATION Ch23:459–512当前语义/时空/行动及目标空间、负例梯度分责，未明确混合模态pair温度与query/target二阶几何的分账。拟仅一窄段接contrastive对齐目标或负例讨论：温度、negative selection、Cov是不同训练接口；联合W须共享并绑定batch/产物身份，几何重叠不取代排名，新增校准/训练成本、漂移重核与普通对比/固定温度回退。这是具体gap提案，不把三个成熟组件各算新增/长寿命分数。准入/必要证据/owner独立待root，尚未写共享Books。

## 2601.03525v1 VeRPO，2+2+2=6拟准入

作者实际§4.1–4.3 Eq2–9、§5.1/5.2/Table1/3与AppendixA；核心原式保CORE_4。ρ_j按同prompt当前old-policy组的所有turn统计，各trajectory按长度隐式参与不同权重；w=exp(-αρ)，再除测试难度Gaussian density。不等固定任务难度或因果step贡献。最后按测试权重求各turn partial success，与折扣terminal全通过结果分别居中/归一合并，terminal仍只证明这份有限suite，而不是任意程序功能真值。

直接必要反侧：Eq4/其后σ=std({ρ_j})/2；所有测试具有相同passrate（包括全通过/全失败）时σ=0，Gaussian项为0/0。Eq5 ε仅保护density分母，不能修复Eq4 bandwidth。因此精确density定义/数值实现采用权限待澄清：需原实现的σ floor或明确zero-variance分支与对应结果。不宣称所有表结果无效，也不授作者robustness/unbiased保证；其它正带宽条件下的提出机制和有限观察可保留。Fnorm=1不自动消除组依赖权重的估计偏差。

真实TACO7436 filtered题、Qwen3-8B、veRL/8H800、32prompts×10responses、16384max/训练temperature1、eval.6及8samples/pass@1；single/multiturn训练和eval各人口，partial-only及difficulty-only部分表切片不优outcome基线。0.10秒reward overhead是在已支付unit-test执行的该配置，不授总执行无成本/通用GPU0overhead；density另有测试数平方项。没有运行代码，原页source comingsoon不当访问故障。

actual TRAIN-GRPO Ch33:1383–1408 immediate/outcome归一和population已有，2016–2031 action/token信用已在；当前未承载由同组当前策略的unit-test passrate/density改变测试权重。但中心density定义不明，暂不申请Books；可精确隔离该增量数值链而保旧固定/均匀test权重和outcome verifier。评分不为省审降级，准入及必要证据终态仍待root独立核。

## 最新独立必要裁决与写后同步（jan01_v3，覆盖上述作者准备停点）

原评分不变；下列只为实际必要范围，不称全部附件或复现。Grading/Disclaimer具体Existing通过；VeRPO中心density隔离；ELO/e5 source→owner与实际新段/邻接/源注POST通过。后四Metaphor6Only、MoE7中心hold、SESS5Only、ABC5Only均具名到终态；完整位置/反侧如下：

- 03388 2+2+2=6：必要exact-v1 §2.1–2.5 L100–121、§3.1–3.5 L123–198及限制203–206由jan01_v3实际独立核。19K metaphor与随机mask只匹配token数，不保语义/位置；continued PT未配非隐喻等compute，SAE是association而非独立介入，100+100 detector不是部署风险校准。Thinking训练关/测开和Qwen同家族judge人口保留，训练硬件/优化总预算Not Disclosed。只报告受限训练特征敏感性反证；Ch72:573–603已有输入支持/安全迁移与sensor权限，不声称精确recipe覆盖或删除隐喻是普遍防线。未读A3全部feature表、未复现。

- 03401 2+2+2=6：必要§3/Alg1及评价/限制，CORE4 local122–204由jan01_v3实际核。监督y未改，skip-KL/hybrid定位当前输出依赖；English LoRA与保持trigger语义的paraphrase不证明信息不能学或不可恢复。Ch66:2963–3003已实际承载suppression、retrain reference、恢复与retain边界，具体Existing通过；不称算法已覆盖、不授版权/删除保证，未复现。

- 03444 2+1+2=5：必要§3–5/限制与CORE4 local1–121由jan01_v3实际核：ICC(A,1)/(A,k)与跨panel两列分别测量，150×12 fractional评分线性归一不等离散档位实验。有限温度/任务反侧不支持0–5普遍最优。Ch66:258–282、4135–4178实际承载稳定≠alignment、scale/pooling/population/metric身份，具体Existing通过，不声称已含本篇ICC公式或普遍量表选择，未复现。

- 03525 2+2+2=6：必要§4/Eq2–12、Table1/成本及AppA（CORE4 local487–575）由jan01_v3实际核。ρ按同组所有turn长度人口，σ=stdρ/2在相同rates为0，Eq4出现0/0；Eq5分母ε不是bandwidth floor，Fnorm=1不授unbiased。精确隔离density采用权限，保positive-bandwidth有限观察、不否所有实测。重开仅zeroσ分支/原实现及对应配置结果；不写Books、不扩附件。

- 03577 2+2+3=7：jan01_v3实际exact-v1 §2–3.2 L84–156、§5.1–6.2 L184–271、AppB437–473、AppF/G589–656；Thm3.3 exact collision entropy依AppB f≈p，而one-shot Top-k完整support保证的证明仅OMP首步并另需uniform weights。独立反例k=2，e1=(1,0,0)、e2=(0,1,0)、e3=(.1,.1,sqrt(.98))，y=100e1+e2；μ=.1<1/3但scores=(100,1,10.1)，选{1,3}残差平方.98989899而{1,2}=0。只隔离exact entropy/coherence恢复及regularizer普遍最优保证，不判有限synthetic曲线无效；受限OLS/KL数学不修复未知router target/softmax系数。重开精确algorithm、系数/归一/噪声假设与修正证明，不进入Books。

- 03648 2+2+2=6：必要§3.1–3.3/§5/7/AppB、CORE4 local205–325与Ch30:108–158由jan01_v3实际source→owner核。浅CP→替换deep首尾→全FFT alignment与chatvector/SFT分阶段付费；zeroalignment退步，9+1GB不是同token/compute，wholepipeline peak不下降。原6因具体gap深入，Ch30:137一段及804注已jan01_v3实际126–149/注POST通过；保LoRA/FFT共存fallback，不采无损或headline。

- 03666 2+2+2=6：必要§2.2–2.4/3.1/3.3–3.6/AppB、CORE4 local327–486与Ch23:449–519由jan01_v3实际核。双方active-modality均温为pair sharpness，row-negative selection/aggregate与joint Q/P同W后Cov分别定义人口和几何；不是各模态白化或pair真值。batchW未示部署冻结/index相容，仅作为工程要求，γλ过强反侧/额外成本保留。原6具体gap深入，Ch23:509及1064注已jan01_v3实际497–517/注POST通过；不授online部署/独立组件因果，未复现。

- 03493 2+1+2=5：jan01_v3实际exact-v1 §3 L64–108、§4–7 L109–142、AppA175–181。非负similarity/λ只授既定F的submodular近似，不授prompt最优；同OPRO100×7、2次mean、8A10080G及有限模型预算。repLarge弱random而AnchorLarge更好；GPQA全部198作pool选择20/40又测198，选择/测试重合不授独立heldout泛化。Ch66 subset-fidelity/heldout与Ch79统计预算已定义稳定责任，新增只局部selector case，不声称exact算法Existing，原5仅报告。

- 03895 2+1+2=5：jan01_v3实际exact-v1 §4.1–4.5/Alg1 L107–256、§5.1–5.2/Table3 L257–305。Eq5/6直接clipped-ratio×sequenceA无PPO min，区间外本梯度0不阻共享参数移动；未解决token credit。Bound需Amax/Gmax，Eq14lower须max(e2,e4)非min；Table2不依sign与Eq5冲突子命题不采，不扩大冻结全部实测。实际四ε=.2未验自适应非对称，AIME/AMC有退步，不授entropy普保。Ch33:120–199已有objective/sign/粗credit合同；本局部loss case仅报告，不称exact覆盖，原5不降。
