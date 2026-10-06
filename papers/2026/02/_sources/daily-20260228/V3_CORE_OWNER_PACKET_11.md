# 第十一包：AB7后组六项必要原v1与实际owner

仅处理已独立准入校准的具名潜力；不扩大标题库存，不比较全部revision。作者已读下列核心、对应控制/反侧与实际owner，尚待root必要PRE；未改Books、未计safe。机械位置是本目录V3_BLOCKS_2602.<ID>.md，原版本链接均为https://arxiv.org/html/2602.<ID>v1。实际获取见V3_FETCH_AB7_NECESSARY_B.json，2026-10-05T19:03:56～59Z，abs-v1、HTML-v1及当前官方abs均200。当前comments仅见22724 under review、22727 CVPR accepted、22734 project page、22752 WASSA/EACL accepted，其余无comment；没有将后续会议事件另计本窗，也没有据此声称完整版本史已审。

六个原v1均02/26 UTC、晚于02/25 19:00Z提交。由已核官方公告政策得到公开下界02/27 09:00+08，同ID registered提供身份公开上界（不是技术证据或首公告）；UTC原值依次为02/27 02:53:01、:07、:12、:21、:45、:46，上界各加1秒转换+08，全区间落本窗。原字段见V3_THEME_METADATA.json；Submitted不等于public。

## 22719 Activation Subspace Bottlenecks — 2+1+3=6，拟Ch22局部SSM干预

实际原23–55/57–61/71–101、263–276、300–311；未读全部D3表/证明。implicit-attention token weights经min-max缩放后形成加权hidden vector，熵/敏感性诊断选层和Delta feature，再由消融决定局部增益；这是diagnostic→ablation validated scalar branch，不把未给完整basis的“subspace”写成可直接执行投影。Mamba130M与Pile50K调整population，选择/搜索预算不是零。发现摘要“7 SSMs”与原v1完整摘要“5”不同，只纠正本ID；主文60的模型枚举另有Steered/Stable，故不采用跨稿总数headline。

Table6 selected layer/Delta steering 72.5与baseline72.5相同，random67/high-variance33.5是选择错误反侧，不授所有steering有效。D1去layer20 63.5→77而相邻层坏，D2去Delta组与单feature消融不同，不将其混成同一操作；§83平均23.32与“最大17.5”冲突不采用总体百分比。StableMamba的多timescale/gate/sparse global/rescale是另一bundle；main55“256额外参数/成本可忽略”与E301–304约2.8×per-token、shallower约1.5×净计算及每层约4.95M参数不兼容，隔离该成本保证。311 latency .836 vs1.389与memory1.985 vs2.758缺hardware/dtype/input length/batch/SLO，不认证iso-workload端到端优势。只采用已定位局部branch的诊断/干预条件，效果衰退需关闭branch，保原selective recurrence。

实际MODEL-LONG-CONTEXT Ch22 475–499已有固定/选择性Delta、B、C与scan、forward stability≠学习稳定及增状态代价；没有**局部scalar gain须经消融选择，entropy/rank只作诊断且另一architecture bundle成本不能转借**。拟selective-SSM附近单段，只有这一差额，请求窄lease；不另写Ch5。

## 22724 AgentSentry — 2+2+3=7，拟Ch72同边界反事实诊断

实际原37–59/75–84/88–120/121–149/152–194/215–240/246–262。同post-tool/pre-action边界保存snapshot及cached return，在原goal、masked goal、masked+sanitized、原goal+sanitized四regime dry-run proposal，probe不执行effect、不把其输出放回live。218–220 probe要求summarize与建议next tool，改变intent，不是中性随机baseline。Y读/高影响/off-goal severity与独立Auth违规不是同一个真值；Purify保事实/task relevance、可信goal/先前prefix及defender未被妥协是必要外部假设，不由本方法证明。

中心子命题纠错：106/109/110定义IE=mu_mask−mu_maskSan、DE=mu_origSan−mu_maskSan、ACE=mu_orig−mu_mask。111/252写ACE=DE+IE并不成立：mu_orig=2、mu_mask=2、mu_maskSan=0、mu_origSan=0得到ACE0/DE0/IE2；actual187首例ACE0/DE1/IE1也直接冲突。**隔离additivity/causal certificate，不整项D**：四regime相同工具边界重执行、时间趋势与净化替换仍是独立可描述机制。149检测不以DE残差恒零为前提。261实际K1/B0、w2/3不支持bootstrap显著性普遍保证，正IE/ACE趋势只是所定义诊断。每边界四额外calls、缓存、purifier、snapshot与latency成本未给全配置；不能称免费。

AgentDojo.1.35的949有限cases、四suites/三attacks、GPT4o/3.5/Qwen3Max作者实验不认证任意attack零ASR；Qwen clean utility83.51低于undefended85.57，保负侧。Table3去sanitization UA58.21/ASR22.5，去temporal UA88.57/ASR1.07支持package条件而非单因素全生产安全。Auth/许可仍独立effect gate，Purify失败则不把干净response当可继续授权。

实际PLATFORM-SECURITY Ch72 652–676已有influence/provenance、authority registry与step guard、净化不授effect权；缺**同cached工具边界四regime复执行，diagnostic dry-run和净化后live continuation分开**。请求其后单段窄lease；不采用错误加性分解、不认证工具事实或所有prompt-injection定位。

## 22727 HulluEdit — 2+1+3=6，拟Ch23几何保留与事实边界

实际原23–80/81–114/172–175/185–190。选visual anchor，滑动text states经视觉补空间构造anti-prior basis；在给定有效hidden-dimension正交bases U/P时，Eq16保h_U、将h_P缩为1/(1+lambda_n+lambda_p)，其余h_R缩为1/(1+lambda_n)，VCR/PCR gate控制是否启用。**几何保留chosen visual projection不是grounding truth**；bases依赖当前h，不把固定投影结论扩成整个生成global Lipschitz。

34/35将n_v×d矩阵的left singular vectors当d×r，38/39文本侧同样shape不符；不擅自修正为right vectors或声明实际code正确。只采用“给定有效hidden bases”的Eq16条件分支，隔离所写SVD接口、需同维构造/实现证据才重开。r8/q5/d4096、U每步weighted PCA，缓存anchor不等无每token分解成本；83忽略n_v/n_t不采严格O(dr)。epsilon主文与附录不一致不补执行配置。

单A100、LLaVA7/13/Qwen7等、POPE greedy64/caption T.05/topP1、三seeds与500COCO作者测量，preprocess排除在throughput之外；精度/batch/SLO Not Disclosed。Table4无orthogonal complement 5.6/15.9 vs4.18/13，无gate7.7/22.9坏于原7.08/20.4；MME count118.33→105是直接负侧，不采所有能力保持，MiniGPT若干质量也非全胜。缩residual可能删有用counting信息，失败回原hidden。必要机制/反侧足即停，未核artifact。

实际MULTIMODAL-REPRESENTATION Ch23 950–969已有readout geometry≠任务、transport/ODCRL投影与target overlap；缺**anti-prior只能在visual补空间构造，再分别收缩以物理保选定projection，但事实与counting须独立验收**。请求ODCRL后单段窄lease，保SVD书写争议，不授算法完整实现。

### 22727 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks0–114、172–175、185–190：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+1+3=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：09528条件分布干预与05464非目标补空间已有，但没有视觉投影保留、anti-prior补空间及两种残余软缩放的具体接口，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。hidden-dimension 基记号冲突隔离，不修造实现；去 gate 的 CHAIR 反退、计数118.33→105、预处理排除 TPS 与未干预回退近文。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 22734 Asymmetric Idiosyncrasies — 2+1+3=6，拟Ch24具体已有覆盖

实际原25–65/68–104，49–65截断已补。固定图片/三detail prompts产生caption，text classifier区分caption源很高，生成图像源分类较弱；**source fingerprint可辨不等特定attribute忠实传递**。90K captions、三模型与追加第四class不混分母：text四class chance25%，image三class chance33.3%，FLUX image49.85不称chance。BERT32三epochs与ResNet300epochs并非capacity/预算匹配，finite classifier较弱不能证明信息不可恢复；CLIP/T5 embedding仍可辨source也不证明encoder完全忠实或已因果免责。84%detail judge等与图像judge是不同proxy，不外推caption越细图像必越差。

实际MULTIMODAL-GENERATIVE-PARADIGMS Ch24 238–240明确seq-attention与pooled modulation职责，pooled-path inactive/semantic-decouple不可由分离指标直接判定，必须分验condition path与image quality；该具体论点已承载本包采用的**源身份/表征可辨≠生成语义忠实**，没有论文名缺口。拟Existing，优先不写；若root认为有限source-fingerprint对照确实需要局部验证，则只该论点一段，不重复Ch66。仅保作者有限classifier/judge结果与分母，生成API/HW/dtype/steps/seeds成本未披露，不认证所有caption细节损失。

## 22751 EGPO — 2+1+3=6，拟Ch33不新增anchor的退化group分支

实际原19–32/33–81/88–110。H为old policy对sampled response的平均negative log likelihood，非完整token分布entropy/calibrated truth。Hbar/(H+epsilon)权重再按正确/错误asymmetric clamp，默认不renormalize；all-correct skip、all-wrong A=-1保bounded weights、mixed沿标准group advantage。Eq4是full-response ratio，不替作者改成token ratio/geometric mean。可选clamp后renormalize会破坏方向界：correct weights2/1与wrong1平均4/3后第二correct为.75，不能同时授原>=1保证；均值权重1也不保证gradient scale/zero-sum。统一负adv不必然有非零expected score gradient，verifier最后答案不标记每个token正确。

1.5/7B QwenMath/R1、Stable10K、五epochs770steps G16/lr1e-6、lambda.8/2、eight eval draws T.6/topP.95/k20，与3072/16K family长度分开，不采正文4096一刀切；eight draws不是八training seeds。Table1 AIME13.33低EDGE16.67，Table2 C5 MATH81.05更高但Minerva35.29低default37.13，保component tradeoff不采全胜。训练HW/dtype/完整sequence预算ND；old logs已经记录时才能复用，不能授普遍zero overhead，不把“NLL代理”改称metacognition真值。

实际TRAIN-GRPO Ch33 510–555、534–548已有DAPO mixed过滤、boundary anchor/target injection、多teacher补all-wrong与consolidation；缺**原self-group内NLL权重和asymmetric/default-no-renorm分支，不添anchor/teacher而有限使用all-wrong**。请求退化group分支附近一段窄lease，保skip/可靠verifier回退和非token causal credit。

## 22752 Constrained Conversational Personalization — 2+1+3=6，拟Ch29已有覆盖

实际原34–75/77–104/123–131。三个8B模型、EN/DE政治X与LB moderated RTL人口、每语言3800/650 user split、up-to30 history/heldout reply，bio由Qwen235B生成且排last reply。one epoch full-input system/user/completion loss，4500sequence/8bit paged AdamW/single L40S48，不冒充response-masked SFT。five generations T.75是sampling次数非training seeds；selected Qwen3 embedding cosine是semantic proxy非human intent/事实真值。未独立读AppendixD的替代embedder结果，不将作者指向当交叉验证已完成。

LB三个model embedding distance .579→.605/.578→.610/.583→.597退步，同时length/lexical格式更近；EN改进、DE mixed，人口与资源不同不能作纯resource causal结论。History .399 vscombined .397不能证明bio普遍无用；one heldout reply不覆盖行为分布。只采用受控负面**SFT更像style/length并不保证语义proxy变好，需要按language/population分账**，不声明所有personalization退步。

实际TRAIN-SFT Ch29 18–62已有SFT改format/role interface不等semantic truth，192–219明确正确性不能用fluency/style/language替代，94–96语言confidence/accuracy单独验收。拟具体Existing，不为本paper名称追加gap。若root认为history/bio相近本身没有可保留新设计差额，作为受限报告事实也可，但不强改书。

## 窄复核请求

请root依拟采用命题核上列原blocks及实际owner：22719/724/727/751拟四个单段I；22734/752拟两个具体Existing。22724只隔离错误加性公式，22727只隔离SVD形状/实现接口，独立可描述经验命题仍在；不请求整篇all-proof、不把安全headline授production、不把待PRE记完成。取得具体lease后才实际写，完整邻接/自身末注另送POST。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22751：原必要blocks33–61/74–81/102–105与actual owner独核；Ch33正文551/完整541–559/own2962 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：22719：2+1+3=6，entropy提假设/消融选择gain，独立bundle及费用；必要原v1/直接反侧与actual owner独核，Ch22正文493/自身1327及完整邻接root非写入者actual POST通过；22724：2+2+3=7，同tool边界四regime dryrun/净化后continuation，非加性或授权；必要原v1/直接反侧与actual owner独核，Ch72正文678/自身4284及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
