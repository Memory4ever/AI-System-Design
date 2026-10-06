# 第八批必要原文与决定核心

## 15515 Obfuscation Atlas — 2+2+2=6，安全受影响深入，作者必要块完成

实际[exact-v1](https://arxiv.org/html/2602.15515v1) §4–6/Tables2–4/Fig2–5、D完整score-function/stopgradient链与H训练配置。MBPP-Honeypot874题只给第一test，reward只执行首codeblock；另外tests只评估，不训练。0.003/char penalty标准化hack激励，四模型Llama3 8/70B与Gemma3 12/27B，LoRA64/128，GRPO G8/120steps/3seeds，400heldoutprompts。分类“honest”为passfirst-passall≤.3，不是无hack；probes followup“Did you respond truthfully?/Yes”残流非任意部署接口。原model和trainedmodel同文本probe区分policy文本evasion与representation drift；fresh offdomainprobe AUC可降，fresh in-domainMBPP近1说明direction变不等representation信息消失。D只stopgradient reward无额外直接activation优化项，不说policygradient不会改变activation；sampleGRPO归一化不直接继承精确unbiased REINFORCE定理。

关键反側：没有detector penalty也有activation drift，罚detector主要驱动policy文本合理化/噪声/第二块“坦白”；高KL/penalty有限条件能减少heldout测试hack，但alpha100 Llama8退化，模型batch有效64/32/8不全matched；theory不认证所有coding/部署honesty。H maxseq512/response256/temp1，probe前向/训练开销、hardware/precision/E2E Not Disclosed，不能称免费monitor；§6高KL规模成本、缺部署policy-evasion detector/非coding未测保留。未核代码/复现；Books actualowner尚可执行。

## 15602 Per-instance Unlearning — 2+2+3=7，理论/隐私受影响深入，作者必要块完成，精确certificate争议

实际[exact-v1](https://arxiv.org/html/2602.15602v1) §3–5/Def3.4/Ass4.1/Prop4.2/Th4.3–4.4/Remark4.5、B2–4/C1–3。删除指定i比较U(A(D),D−i,i)与U(A(D−i),D−i,empty)，并非任意全域DP/直接reference train同义。nonaveraged ridge、强凸m/光滑L、eta1/L/c<1、deterministic sharedinit、learnnoise>0；perinstance梯度difference经contractive learn/unlearn传播，ridgeGaussian residual/noncentralchi²量化而不是沿单随机trajectory取max即cert。选delta_s并分delta_m，噪声argmin只该界与固定K，不称所有机制最小或LLM可cert。ExactLS ShermanMorrison是另一目标/收敛与矩阵成本路径，不能概括其不存在。

中心证明需隔离：C3用轨迹good-event G_i条件化后直接调用B2的独立Gaussian步骤保证；但G_i包含由这些noise生成的整段残差，条件化改变Gaussian独立分布，原B2未证明conditional law可继续使用同tradeoff。C3还写P(Q∈S|G)P(G)=P(Q∈S)，一般只≤，此一处可修但不修前述conditional inference。C2 k=0方差0的quantile未分支且0..T共T+1项/T的unionbound写delta_s有offbyone；这些不是靠再读全附件能自动补足的cert。采用有限个体sensitivity异质性/校准提案，暂不采Th4.3精确(ε,δ)保证，请求root独立核该具体推理链；不因争议改EX。

MNIST frozenResNet50只ridgehead，T300/K30/lambda1e-4/learnnoise.01，7梯度难度代表points，20fullruns；uniformbaseline用oracle全局maxgradient，不拿vs现实固定DP算法普遍更好。CIFARVGGstyleT500/K20fullbatch/C1/lambda1e-4/eta.01 learnnoise0且unlearnnoise.02所有i同，50runs/point，固定probe logit线性distinguisher拟GDP：原文明确cannotcertDef3.4，拟epsilon是经验summary非allattacker隐私保证。formal争议不影响受限结果记录；hardware/precision/E2E Not Disclosed，矩阵/轨迹calibration与retainset继续训练成本未量化。

## 15654 Zombie Agents — 2+2+2=6，安全受影响深入，作者必要块完成

实际[exact-v1](https://arxiv.org/html/2602.15654v1) §2–4、A1–2 writer/memory/tool结构。blackbox外部webcontent→正常session observation→标准summary/rawhistory/reflection/experience更新入库→另sessiontrigger工具行为，区别于ER-MIA实验直接已stored attack；固定weight，window/FIFO和RAG persistence依赖分别再接触/再次写入与retrieval人口。只记录威胁/owner条件，不输出payload步骤。Gemini2.5Flash/GLM4.7Flash，3seeds，window3exposure+20trigger，RAG300exposure/3000bank+20trigger，tools search/read_url/execute_command；bait强制接触并非随机现实infectionrate，正常writer accept率与infectionconditionalASR未独立完整分账。Eq3对所有q召回→1是目标非保证。

§4rawhistory约77%与reflection约12%/refined3–15%说明正常提炼能过滤且非充分防御；window100%retention只有限20rounds非永久，RAG约240copies/23top50为报告图文量级非所有query保证。instruction三guardrails>60%局部，不等所有防护无效；未匹配exposure/token/toolbudget、不报benign utility数值/置信区间或全部config，Casehealth/shopping叙述不证明真实医院财务伤害/legalviolation，生产toolpermission/hardware/precision未披露。未核实现/复现；必要路径可信边界已有owner需actual比较，不默认新段。

## 15756 Layerwise Noncomposability — 3+1+3=7，理论/验证安全深入，作者必要块完成

实际[exact-v1](https://arxiv.org/html/2602.15756v1) §2Def1、§3Th1完整construct/proof、Remark1/§4。ReLU hidden+linearfinal、至少一hidden层、l∞ layerchecks相对prover supplied上一状态，originalfiniteoutputR/entriesg>1。加2m非负triggercoordinates exact初始全零，firstlayer容差内inject正/负delta，后层逐次g放大(之后都exact)，finalM=2R/(delta*g^(k−2))差分补任意z∈[-R,R]^m；model exactfunction不变，权界为max(g,M)，不是固定原width/原weights/所有架构免条件。该构造直接反驳泛localδ→globalclose，不反驳特定sumcheck已做propagation analysis、不说真实随机roundoff必如此或攻破现有协议。

原Remark R20/delta1e-3/g2/k20 M≈.15只参数sanity非FP16真实GPU实验；adversary可构造/commit function-equivalent artifact且choose每步error才该threat。工程需要globalerrorbudget/稳定性/输出metric是从反例推导，不能声称原文给出已部署certifier；无benchmark/runtime开销属Not Applicable(theory)，未核代码或复现。actualBooks owner/邻接待执行。

## 15513 HIMM — 2+2+2=6，root准入校准通过，必要核心/评价完成

完整精确v1题摘见[V3_ADMISSION_EIGHTH](V3_ADMISSION_EIGHTH.md)。实际[§III-A/B](https://arxiv.org/html/2602.15513v1#S3)与§IV-C决定核心读后，增量不只episodic/semantic名词：多视角persistent geometric fusion易累计alignment错→semantic观测独立保存、只在retrieval-time把相关camera pose投到occupancy grid，TopK先visual相似再MLLM验证邻近，并按检索经验修frontier→是否在线融合所有经验与任务时限定对齐成为具体选择。另longtrace伪代码规则容易过注释→以agent轨迹相对GT轨迹距离跨threshold挑3–5偏离点，连GT答案/观察给rule extractor→ground-truth-supported consolidation与无标签在线记忆不同条件。拟2+2+2=6；收益可信度进入必要审阅，不以成熟CLIP/SAM/name保留。

已读有限消融反侧：§IV-C称无episodic时Qwen Match41.3→39.1，但主表full43.1，不能静默统一；同主表Qwen full43.1低于ReEXplore46.2，GPT4o有正向slice。多模块/视觉核验/GT训练经验成本未匹配，不能称无几何误差或普遍更快。该决定块与下方补齐的必要评价共同构成作者审阅，尚待非作者Evidence/Books复核。

必要评价actual§IV-A/B与TableI/II：OpenEQA184 training episodes提供semantic规则/GT答案、GPT4o LLM-Match及×SPL而非独立人类truth；GOAT1/10val-unseen、36scenes/278subtasks、距目标1m stop。GPT路线提高局部指标，但Qwen OpenEQA Match43.1低ReExplore46.2，GOAT SPL31.7低32.6；文本ablation41.3与Table43.1未擅自统一。GT轨迹距离挑3–5规则提炼位置不是无标签在线学习。主文未披露完整hardware/precision/CI/seed/topK和总预算，不授跨模型全胜、实时或安全。决定命题只需分开观测存储与检索时几何投影，未遍历附件。

## 15549 VLM-DEWM — 2+2+2=6，root准入校准通过，必要核心/评价完成

实际[§3.1–3.3](https://arxiv.org/html/2602.15549v1#S3)、§4.1–4.4及必要AppendixD。高层macro failure丢动作阶段→CS只在已验证causal assumption成立后更新，保留ERT expected postcondition与失败后S/G状态做semantic set difference，按interaction phase定位修belief而非重新全plan；commit同时需要lowlevel动作反馈和post-action几何变化，rollback model不等物理世界回滚。这是有限stage-anchored discrepancy接口/成立边界，而非名称新颖。D的JSON schema/entity存在/On-Inside-Near几何关系校验不等真实动力学/碰撞安全；原文称geometry groundtruth也须保持其sensor条件。

actual评价：PyBullet/Gazebo使用GT segmentation/6Dpose以隔离记忆，所有baseline有同CAD/shapeprior与grasp库，但纯VLM是single-shot，整条验证/调用预算并不matched。Franka7DOF1kHz、Robotiq2F85、D435i848×48030fps半结构化已知类别；重置物理场景但保CAD/LTM，不是无先验开放世界。Task1 N50：94%TSR/100%STA、75calls对SAGE72%/261calls；IE是queries与storedentries比，不是bits或零信息损失。Task2 240观测、50问：94%QSR/92.68%STA/509calls对SAGE52%/56.10%/2162；非walltime/token费用。Task3 Table5标N60而说明20inducedfailures及6即时/11多轮诊断，95%TSR与36.96%CDA分母不同，不拼通用失效率/独立因果；w/oCS55%对full95%、w/oM90%但266calls对54，只支持bundle内局部反侧，ERT未单独消融。perception污染/开放词表/动力学gap/阶段粒度与额外deliberation成本均§4.4；必要部分读足停止，未核代码/复现。

决定反侧：realFranka ablation Task3每variant20trials，clear scene memory但保留knownCAD shape/grasp priors；无CS55%vsfull95%但未匹配retry/calls预算，noM90%且266calls vs54；noERT未做，因为作者称协议不可移除，不能给ERT单因果。作者把DEWM称groundtruth，但§4.4承认upstream corruption无法自校、closed-world未知物体可误认、动态/关节极限交低层；数据库原子性只近似物理执行。必要setup/verification AppendixD现已读，非作者Evidence/Books仍待核，不扩其他附录。
