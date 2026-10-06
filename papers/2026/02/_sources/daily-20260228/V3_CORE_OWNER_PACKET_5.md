# 第五包：有限理论/控制/目标边界

全部采用本轮 exact-v1 HTML 的实际必要块；date来自originalabs v1精确Submitted及sameIDregistered上界，结合官方announcement下界，范围全落本窗，不称registered首公开。22445 originalabs v1 Wed25 22:08:44UTC，registered Fri27 02:46:33UTC已恢复；此前缺metadata不再当EX。root已实际核必要原块/owner PRE，以及七处新正文/完整邻接/自身末注POST通过；七ownnotes同步通过并释放Ch36/25/26/66/24/33窄lease。22479只作中心争议终态隔离，无Books写入。以下保留决定依据，不授日级Gate。

## 22445 fault-tolerant reduction，2+1+3=6

原blocks22–49、50–77、84–86/97–99/106–108/112–119/134–139/147–178：fail-stop、网络可靠不丢包/重排/无限延迟、结合且交换的reduce op；先在f+1组内up-correction交换原输入，再进入I(f)树，保证幸存输入完整且不重复、失败输入完整计入或完全缺席。根在reduce中失败可no-op，不保证所有rank正常progress；AllReduce另需至少f+1个预知不会在操作中失败的候选（可预先失败）、一致候选顺序和外部容错broadcast。这不是任意ongoing GPU failure可无条件继续。计数排除failure-monitor通信，未测真实GPU/训练；survivor aggregate不等固定batch原梯度/optimizer commit。

Actual Ch36 975–1006现有全组恢复/SPARe原shard完整计入/R2CCL网络恢复/已提交状态重绑已读，缺**先组内up-correction再容错树的条件性reduce分支**。请求fault章节SPARe附近一段＋自身note，保持failed贡献all-or-none与训练分母不同、不承诺AllReduce任意根失败或故障检测免费、原checkpoint回退。只审该条件，不要求整个broadcast proof。

## 22452 CWM，2+1+2=5

原blocks23–96：Qwen2.5-7B LoRA r8/α16 qkvo，以action loglikelihood InfoNCE τ.6加margin γ2/λm.3/λr.005，16负例分别nothing/rejection/cross-task；同arch/data SFT与16neg BCE对照。ScienceWorld这里是可执行Agent环境不是科学领域应用。最小edit 74例CWM93.24/SFT86.49，rejection切片持平；无真实完整agent部署，预计减少invalid actions30–40%是future不是结果。Type3“cool vs heat”可以都physically valid只是goal错；live GARR是从env ALL valid actions中rank一个expert gold的字符串匹配，不是物理可行性真值，OOD CWM top1低于SFT，rawmargin尺度也不认证ranking或risk。30epochs/earlystop，hardware/precision Not Disclosed。

Actual Ch25 1123–1139已读expert/offexpert action support、integrity/trajectory fidelity、matched budget和独立physical controller，尚未承载**对action loglikelihood做hard-negative对比训练仍把goal correctness混成physical feasibility**这条mechanism/evaluator边界。建议Ch25 integrity gate附近单段：对比分离局部否定/任务错配能减少相近动作混淆，但3种负样本truth分账，gold ranking不代physical gate、safety score未校准及训练/比较费用、原SFT/实环境验证回退。不将本文“world model”名称推广为可预测完整dynamics。

## 22461 EgoAVFlow，2+1+3=6

原blocks22–27/49–118/83–89：human RGBD→HaMeR手腕/gripper-equivalent动作，CoTracker+depth/DROIDSLAM经ChArUco坐标锚；三diffusion模型分别action policy、action-conditioned未来3D flow、camera-view prior。由未来点可见性/LOS/FOV及近末端softpenalty对view采样作reward guidance；预测future不是新真实observation，softdistance不授碰撞shield。T24/H12执行半chunk。same robot policy的human-view模仿控制定位camera guidance差额；表示baseline保持view模块但预处理不同，不授唯一表示因果。4任务各25次，success同时要求任务成功且对象全过程可见，非纯task success。初始点必须可见，不负责搜索未知POI；未来flow/跟踪/遮挡失配、额外预测与guidance/三模型训练和标定代价；camera数/全部实时控制费用未完整披露。

Actual Ch26 64–75坐标/观测接口与viewID→metric waypoint、429–449 trajectory/future state分责已读，缺**动作条件未来3D flow指导主动相机、view prior不只复现人类视角**的控制分支。请求坐标/观测接口相邻一段＋ownnote，human motion伪动作不是低层可执行证明，初始visible与softpenalty、复合success/费用/固定视角与重观测回退同段。不要把相机guided prior写成语言条件通用foundation model。

## 22465 ConstraintBench，2+1+2=5

原blocks12–64/71–99：10领域各20=200直接NL→JSON solutions，6models1200；independent checker重算全部constraints/objective对formal Gurobi opt，parse/APIfail算infeasible全200，joint optimum是可行且0.1%内。模型自己说objective会错，facility85%feasible却0 strict joint opt；within5%只27%左右，阈值不同不能混。Table3“Optimality95.2”是质量score不是0.1%条件精确最优率；joint30.5/feas65算46.9%，不采95.2为严格最优率。formal task oracle不授原NL语义；LLM迭代生成、discard无opt任务、每20例单次/temp0稳定性、tokenbudget无JSON等人口保留。不能从有限生成失败推AR模型不可能优化。

Actual Ch66 1768–1802已读verifier量级/容差、binary verdict≠semantic忠实及solver参数扰动，但缺**直接solution feasibility、相对gap连续score、给定阈值joint/conditional opt rate必须分账**。请求该solver论证附近一段+ownnote，formal reference权限/失败全分母与阈值/质量分数分开，独立重算代价与可执行solver/ref/human回退。具体95.2冲突只隔离子命题，不必整项D。

## 22474 UPS，2+1+2=5

原blocks28–47/49–55/59–65/67–100/101/175–181：N80calib(40ambig40straight)、40test，M2/K10动作sample；sequence score κ=1−min各phase minALLcorrect labels p，ceil((N+1)(1−eps))/N quantile形成prediction set。singleton执行，>1clarify，只有NONE teleop再训residual并重校准，empty-set分支未给。eps.15，不是所有控制85%成功物理保证；i.i.d/exchangeability、correct action校准与deployment询问/错误路径同人口需核。§101明确assume未来WorldModel与Gemini narration正确完整，因此只校准VLM-verifier接口，不校准整个物理链。DreamerV3/Gemini3flash narrate/Gemini2flash verifier/baseDiffusion，sim nutpeg与Franka杯bins；1Q&A=1step只是计数不等真实成本，residual训练与改分布必须重新calibrate，不能授无遗忘。

Actual Ch26 1113–1123已读runtime正常/plan/update/recover与critic不确定预算，缺**prediction set大小将意图歧义澄清与低层技能失败/残差训练分开**具体机制。请求该安全提交附近单段+ownnote，仅保条件CP范围，world/narration先验/empty set未证与calibration费用/独立controller回退同段；empty-set拒绝是本章工程推断不归因原文。不授无需全部低层物理验证。

## 22479 TRC2，2+1+2=5，中心争议隔离提案

已读原chunk routing/readout与对照，root已校准潜力。必要新增反侧actual blocks117–120和Appendix285–294 EqA.39–42：C_ctx取同chunk ALL token均值，DWConv PadLeft(k_lat−1)包含current chunk tap，经PWConv后broadcast到该chunk ALL位置并加回Y_chunk。原152–156称next-token teacher-forced evaluation/same pipeline，未提供禁用这条current-summary路径或只投给NEXT chunk的限定。即使router first pooling，仍不消除此路。

一个结构反例已足：C=2，同chunk输出Y1=0、Y2=b，DWConv仅current tap系数1/PW identity，则第1位置加b/2，依赖未来第2 token；“chunk-causal”不证明token-causal。这里是本文公开公式的反例，不称实测训练实现一定如此。只要没有精确配置或接口证明排除该路径，高PPL/continual优势中心采用应安全D/暂缓；保chunk-routing条件结构潜力不说全部论文无价值，不遍历所有artifact。重开需要对应原run禁用/one-chunk-shift配置＋无future dependency检查或正确的AR接口，非更多摘要或大表。

Actual Ch22 304–306已有summary仅所属chunk、边界交接不得偷看后文；497–518固定状态读写/遗忘责任已读，但争议项不写Books、不制造此知识gap。未验证全部可选assoc-memory/训练代码。

## 22486 FM intrinsic manifold，2+1+3=6

原blocks54–77/79–83/87–113：compact boundaryless β≥2-smooth d-manifold正reach，density按d-volume且α-Hölder/下界>0，velocity空间Jacobian≤L*/(1−t)^(1−xi)。分段ReLU classes、exact empirical minimizer、专设时间grid与earlystop，d≥3；W2含support项n^(−β/(2α+d))、density项n^(−(α+1)/(2α+d))和n^(−1/2)日志项，constants依ambientD/geometry。指数用intrinsic d不等实现费用不依D；support项可慢于minimax，density dominant才nearoptimal，不授每个sampler/optimizer。数值MLP固定宽度在spheres/torus d2–5,D2d/3d/4d，5runs；d2例不在d≥3 theorem，RK45/Euler示图不等预算比较，finite NFE/wallclock未证明。必要假设/结果已足，不审全proof。

Actual Ch24 184–199已读CFM density/regularity、平均velocity不是直线及solver分责，缺**低维支持的volume density、统计指数与ambient计算/endpoint/support恢复项分账**。请求FM机制段后一段+ownnote，假设/exact ERM/earlystop/geometry常数和solver/代价同段，不把统计定理授实用训练或加速。

## 22495 RLAD/TRRD，2+1+2=5

原blocks37–68/70–98/105–108：r=(student/old)^α(student/teacher)^(1−α)，α.5；背景KLpiRef保留，只换teacher监督。用这个r进入advantage-signed PPO min/clip，实现teacher-old几何anchor对正负A不同更新压力，nearzero A几乎无teacher项。Eq3 α1=GRPO/α0teacher，而paragraph50说反，采用公式端点，记录文内冲突；anchor无normalization不能称proper mixture policy。surrogate clipping不强制r硬界，Eq49 |logr|≤log(1+eps)即使硬clip也错（lower−log(1−eps)更大），不得授exact global KL/trustregion/DPO或reward−weightedKL等价保证。局部mechanism/author实验仍可独立采用，不因理论宣称冲突删实际新分支。

Qwen3 .6B/1.7B←8B，logic8H200/group8/B256/2K–8K；math64H200/105K，bestcheckpoint以AIME24选择亦用于eval，selection人口需保。Table4time32H200和64training不同；567.4/491.2−1≈15.5%不是about12，KDRL568.1局部近同成本，teacher不部署但outputlength不签identicallatency。部分metrics KDRL更高，teacher/log-ratio clipping额外条件，精度未披露。

Actual Ch33 1015–1030 OPD rollout/teacher-compression/verifier已读，缺**按signed advantage经teacher-old几何ratio改变clip压力**。请求OPD该段后单段+ownnote，仅公式mechanism与局部性能、理论hardbound/端点冲突和费用/原KDRL/GRPO回退，不授本论文未成立数学保证。
