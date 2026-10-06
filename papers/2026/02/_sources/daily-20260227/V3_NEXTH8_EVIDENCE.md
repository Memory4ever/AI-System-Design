# 后续8项必要原证/actual owner（待root）

冻结107论文池内普通项，完整exact-v1题摘已独立准入；只读取拟采用机制及决定反侧，不默认fullproof/附件/修订diff。引用`V3_BLOCKS_2602.ID.md`的blockID，不是文件行。尚待root必要源/owner裁决，未计safe，未核代码/复现。

## 21397 MMLoP — 2+1+2=5，拟Ch30窄差额

[v1](https://arxiv.org/html/2602.21397v1)26/28–54/62/70–72。FrozenCLIP的deep连续prompt分别P_v=U V_v、P_t=U V_t；T=V才可共享U，共享的是**prompt位置/低秩系数结构**，不是声称不同维embedding空间有相同rowspace。与weight-LoRA不同，改的是每层显式inputtokens，不能随意merge成同一个W。Frozenzero-shot图像/60template文本特征作feature/logit参照，textclass残差先减当前class集合mean再重归一，参照及支持集并非真实grounding；sharedU也不保证每次两个模态梯度同时受益。

ActualTable4[71]同递增消融：IVLP HM77.51→lowrank77.06（base/novel均降）→加anchor78.78→meanresidual79.20→sharedU79.70；base84.21→83.79，不能说每个目标均改善，非完整factorial因果。Table5[72]rank1novel75.85>rank2 75.01/rank4 75.20；不是任意rank1更好定律。ViTB/16，3seeds，4A6000，9/3depth依任务、30/50epochs；11.5K是trainable参数不是forward/激活/HBM零成本，额外frozenanchor/类mean/训练均付费。

ActualCh30 35–59权重lowrank∆W；426–442区分weight/input/launchstate适配，但没交代**低秩continuousdeepinput共享token因子和class-conditioned anchor并非免训prompt或权重merge**。拟该分责处单窄段，保低秩alone反退、class支持变化、anchor先验、前向费用，固定prompt/full-rank/原CLIP回退；不为新名造论文小节。

## 21515 Strategic Risk Aversion — 2+2+2=6，拟Ch82窄差额

[v1](https://arxiv.org/html/2602.21515v1)73–92/104–115/121–129/430–438。训练partner-shift稳健性不只增加辩论轮数：为每个学习agent加auxadversarialpartner，其目标恶化该agent收益但KL惩罚偏离**正在演化的正常partnerpolicy**；agent在此受限adversary下做PPO，policysharing/随机adversaryrole降低多人规模成本。KL仅约束训练对手分布，不认证真实partner身份/授权/没有串谋；不采用“所有riskaversion免费提高welfare”的理论泛化，aggregativegame结构不适用Tag时训练性能略低[115]。

GSM8K2agents/3rounds/τ10/entropy0，Qwen.5/3/.6/4模型matchedIPPO方向控制；Table1[126]计两者都正确jointaccuracy，Table2[127]与未调Llama1B只计训练agent正确，两个分母不能合并。D.5[431–435]同初稿能力与debate后结果，SRPO训练最终debate较低，crossplay较好；不能把smallLLM变成独立强reasoner或真值oracle。τ选择/auxpolicy/额外rollout和训练，humanpartner/开放任务迁移均未认证，原固定partner/普通PPO与独立答案验收保留。

ActualCh82 350–357已有behavioralbelief≠authenticatedidentity、固定策略群体welfare/online meta策略。差额是**训练期KL-neighborhood adversarialpartner与部署behavioralbelief/权限分离**，用轻微训练收益代价换partner-shift robustness。拟behavioralbelief处单段，不替runtime权限和jointtruth控制。

## 21531 LiLo-VLA — 2+2+2=6，拟Existing Ch26

[v1](https://arxiv.org/html/2602.21531v1)29–47/66–80/83–94/137/139。Globaltransport由MPLib与objectpose提供，localinteraction用wristviewVLA；trainstartSE3扰动承接approach误差，masking结合trainrandomerase。几何heuristic判断失败：无持物阶段localretry重感知/approach，持物失败保守假定lost并回退最近Pick，不是物理undo或当前state真值。

TableI同poseprivilege消融w/oReaching0/full69、w/oRecovery8/full69；但originalPi0.5 83>full78，方法不是每任务优。恢复增加尝试/pose/planner成本，等episode不等motion/wallclock；模拟GTposes/[139]GTskillchecker，实机human验成功，5trials/config、小量4/8skills不能升自动开放安全。Figure4文字36skills/图caption27身份不一致，隔离精确聚合数，不丢真实recipe与TableI有限控制。ExternalYOLOE/FoundationPose、atomicteleop/100k vs30ktraining/不同OpenVLA与pi0.5基座均计费。

ActualCh26 526–534 adaptive stack绑定parent/observation/completion，controller才pop/backtrack、fresh视图/恢复新动作非undo；controller/safety边界856–876已有verifiedskill+planner回退。有限transport/localpose+retrybranch没有改变现有**verifiedskills/状态前置条件/局部恢复**判断，不为该recipe添段。保细负侧/GT与human协议在报告，具体E。

## 21534 ARLArena/SAMPO — 2+2+2=6，拟Ch33窄差额

[v1](https://arxiv.org/html/2602.21534v1)13/24–31/44–57/61–92。BC/formatpenalty/KL/各PO调参是明确testbed前置，调到末20%successratevariance稳定不等全budgetmatched。多turn trajectory已拆为single-turn更新；Table1[13]mask为M_i=1[A_i≥0 or mean_token log(pi_old/pi_current)≤δ]，所以主采用**负advantage且该turn-sequence平均ratio过低时整条turn输出停止更新**，不是必删整段multi-turn episode或语义失败筛选。动态filter、归一population与importancecontrol应分开；不把token宽容软gate/更大KL/更大batch看成等效控制。

Table4[72]CISPO54.42→SeqMask78.88，但KL38.46/updatebatch1024 21.59；SAPO25.16→76.92，KL48.05/batch64.30不全面坏。Text[71]54.12与table54.42隔离精确headline，保表方向。Fig3/4collapse同时KL/gradnorm/format退步是受控相关诊断，不授所有负样本cause或necessarycondition。Lossaggregation[79]对ALFWorld+16.4%而AIME−44.9%，不同预算/任务不能统一。Filter与format/stepadv interaction只作有限观察，不称过滤全失败零组必有非零outcomeadv。SAMPO联合seqclip+global/localadv+filterEq8/9仍recipe，无普遍必要/充分收敛或小模型超越frontier法则。BC数据/所有tuning/多rollout/KL费用、vanilla/fresh conservative更新回退近文。

ActualCh33 169–187已sign-specificclipping与tokensoftgate、reference/freshness；118–141allzero/filter人口明确。差额是**turn-sequence级负/低ratio剔除能修复宽容token更新但附selectionbias**及更强KL/batch不等该控制，拟此段后一个窄paragraph而非全SAMPO新节。Table1具体mask已实际核，不默认全proof。

## 21545 Muon+ — 2+1+2=5，拟Existing Ch28

[v1](https://arxiv.org/html/2602.21545v1)11–33/35–36/58–69/90–94。Momentum→5iterationpolar→row/column归一（col-row与row-col非交换）；ε数值guard/非matrixAdamW/source√m/n缩放，不授rankcollapse全面消失/精确semiorthogonality或收敛定理。LR与方向均sweep取best，Table5更好不证明免调；GPT124–774M/LLama60–1B/固定FineWeb/DCLMtokens、H100/A100BF16有限pretrain/overtrain。不保存secondmoment的postpolar归一本身已有有效作用：Table15matchedLR.005，NorMuonβ2=.95没有额外收益（GPTSmall28.42vsβ2zero28.29/Muon+27.91），不授所有数据不需variance。

ActualCh28 536–543已区分variance modulation前后、postpolar scalar保持几何/column右乘对角不再原orthgeometry、state统计维/EMA/clamp/decay与训练预算、Muon/AdamW回退。去掉history只保方向归一是该分责中的有限简化，独立机制边界已足，不为Muon+名添optimizer段；保必要消融/搜索费用在报告，具体E。

## 21547 RAC — 2+1+2=5，拟Ch45窄差额

[v1](https://arxiv.org/html/2602.21547v1)32–38/50–83/98–115/118–131/185–195。Cacheentry不变，replacement分两个population：topicprevalence按topic arrival的decay+hit，itemimportancefreq+λ·已观察childrenhitmass，value二者乘积；online依旧仅从resident近期语义相似项选**最多一个parent**，非真实causal dependency图。Routing代表/index与localreusegate分开、evictanchor须refresh，O(1)统计更新不等全routing/scan常数。

统一simulatorsemanticthreshold.85由ChatGPT校准，OASST1十×10ktrace，Synthetic20×设置/不拆不交织sessions/ChatGPTvariant，相同容量与hitsemantics支持有限evictioncompare及TP/TSI消融。超宽/过紧阈值、慢/快decay、过大structuralweight均退步[129–131]；normalizedhit/infinitecache分母非真实taskaccuracy、KV数学prefix等价或productionlatency。Dependency theorem以真实ancestor缺失必额外miss为假设，不将embeddingparent赋此保证；另付encoder/index/边维护/eviction扫描/校准成本，单topic/无可靠dependency或预算不足退回LRU/LFU/exactcache。

ActualCh45 145–147semanticcandidate≠correctreuse、317–329LRUworking-set/transfer与拒写已有；未区分**topic群体复访强度×itemobserveddependent reuse**的replacement价值，拟Eviction处一段，不改变cacheauthority/兼容key或授语义similarity合法复用。

## 21548 DualPath — 2+2+2=6，拟Ch55原窄段纠正/增强

[v1](https://arxiv.org/html/2602.21548v1)50–55/85–96/98–111/115–126/142–156。DE-read并非绕开PE直接开始decode：storage→DE DRAM hitbuffer；每层hitKV仍DE→PE HBM，PE对miss做prefill，missKV回DE合成completeprompt；最后DE H2D再decode。两侧storageNIC可池化，但新增DRAM/PCIe/computeNIC流量、按layer/fullblock不同布局、完整prompt可见性前置不消失。

同pairedCNIC把localH2D/D2H也做localRDMAwrite，经IBVL区分modelcollectivehigh/restorelow（99%reservedhigh/lowanti-starvation），只采用**统一QoS入口**机制，不授全拓扑“virtually unaffected”、唯一可行/已独核deployment。Schedulerstoragequeue与unfinishedtokens/GPU配对、择较短readqueue；split一个request两路径还futurework。Baseline内部Basic控制与3项incrementalFigure12支持有限瓶颈迁移；与SGL(MC)implementation/DPvsTP不同作者明说unfair，禁止泛用2xspeed。8Hopper/八400GcomputeNIC+一storageNIC/3FSnoDRAMcache、2P4D等特定PDratio；online0toolgap/0turninterarrival压小真实working set[156]，不可授所有agentSLO。较低hit/共享拥塞/内存不足保单路及重算回退。

ActualCh55完整438–460具体已有dualpath，但正文当前“storage→Decode…绕开Prefill，并把layerwiseKV读取与Decode消费流水化”与50–54**同源接口真实冲突**，不是无新差额却硬写。拟仅纠正这原一段为DE代读→逐层回PE计算→completeprompt DE decode，并在邻接成本段一窄句加CNIC统一QoS额外流量/特定IB边界；保原两路径controlflow与回退，不另造论文节。

## 21585 Duel-Evolve — 2+2+2=6，拟Existing Ch20

[v1](https://arxiv.org/html/2602.21585v1)42–57/68–82/87–96。只在已生成judgedpool上BayesianBradleyTerry Gaussianprior MAP+diagonalLaplace，Thompsonsampling安排pairs和parents、加recentuncertain、confidencehyperparamprune；LLM由parents均值另造candidate并非全solution空间exactposterior或posterior最优抽样。两次换序只保一致decisivepair、丢tie改变selection人口；samejudgegenerator错误相关，置信区间不是truth/校准证书。

MathBench150four-choice/Gemma4B/每gen12new6parents；LCB99/27B4bit/40new5parents、ASTdedup有半batch丢弃、高T1.2与<500char evolvingmemory。publictests1–4作coarsefeedback/hiddenfullsuite作最终评估，不能继承“完全无task scoring”宣传；GEPA LCB训练与val是testset且125iter截断extrapolate，math/GEPA标签privilege不等量；最大150generations不等modelcalls/tokens/compute。BoN同pairwise机制已有强收益，wallclock并行并不免totalfees。保短generation/固定BoN+独立verifier，不授94%可泛化/无oracle保证。

ActualCh20 351–365comparison graph/state、覆盖低degree/近分refinement、correlatedselfjudge非acceptance、428–433全部generation/judge预算，368–376query-local分布状态已有。有限MAP/Laplace/Thompson的实现不改变**已有候选相对偏好作selection/预算proposal、独立oracle验收**；parents演化也不能创造全域posterior，故E，不挂MultiAgent owner或新名recipe。
