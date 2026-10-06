# 2026-04-01：第二有限题摘筛选

检查时间2026-10-13 BJT；作者supp_apr01_20261013。仅从已有四query的相关/含糊题名选36，逐个API指定v1读完整AB；原件[1](./SUP_SECOND_AB_1_20261013.xml)、[2](./SUP_SECOND_AB_2_20261013.xml)、[3](./SUP_SECOND_AB_3_20261013.xml)、[4](./SUP_SECOND_AB_4_20261013.xml)。不把取到原件当审阅完成。没有因为可映owner就准入，Books未比较不作“已有覆盖”初筛理由。

## 拟贡献前关闭（请root分层独核；安全/纠错项全核）

| 身份 | 原文具体事实与关闭理由 |
| --- | --- |
| 27693 LVRPO | AB只将已知GRPO preference reward应用统一理解/生成、不用辅助encoder/loss；未给新增reward、归因、概率接口或成立条件。更好benchmark本身不足长期增量。 |
| 28428 Synergy | session/repo工作区、typed memory/agenda/skill与rewarded经历recall组成persistent agent；没有独立新增执行/委派机制或可核failure条件，社会身份愿景不是系统贡献。 |
| 28489 Video as World survey | 三轴效率taxonomy/paradigms/architecture/inference，不提供新增transition/world-state机制或评价反证；不能把video capacity潜力当已验证worldmodel。 |
| 28376 Marco DeepResearch | QA合成、trajectory与test-time自验证三阶段组合及600tool budget对榜；完整AB未给超出通用verification-at-stages的独立机制或反证，只按步骤名称不可准入。 |
| 28534 MPO PicoGPT | 标准MPO/TT-SVD替换Linear、balanced factor shapes和χ扫TinyShakespeare；只是既有张量分解局部适配/压缩数字，未新增机制、可迁移边界或评价纠错。小模型不是关闭理由。 |
| 28763 PoseDreamer | 人体mesh标注数据生成，controllable diffusion+DPO+hard mining/filter组合；未新增模型训练/表示机制，只人体标签生成与任务改善，不按TRAIN-DATA重引场景应用。 |
| 28010 HeteroHub | 静态metadata/多模态训练集/流数据三类整合与协调demo，无独立状态一致性、控制语义或评价反证；不能把closed-loop等通用词当新增合同。 |

## 需要定点判断，不默认准入或全文

| 身份 | 需要核的决定事实；当前不评分 |
| --- | --- |
| 27982 CDH-Bench | visual evidence vscommonsense成对counterfactual到底只是另一任务集，还是揭示prior normalization的独立评价盲区？核配对及模型条件即止。 |
| 28360 CoE | intra entropy+inter ensemble divergence通常等价mixture entropy；需核定理是否新增可改变coordination的边界而非为成熟恒等式命名。 |
| 28407 MiroEval | task-specific rubrics、active factuality与process三轴已成熟；核“process predicts outcome/看不到的弱点”具体新证据与混杂，而非因3dimensions入选。 |
| 28737 ParaSpeechCLAP | intrinsic/situational分模型与combined在composition上的反向排序可能是表示监督取舍；核是否超出任务集/contrastive成熟方法的组合。 |
| 28551 AgentTrace | 风险理解采访+资源/权限/provenance界面，安全相关需定点核是否有新未撤销sideeffect证据或仅成熟auditability界面。 |
| 27349 structuralVL | scene-graphaugmentation对弱model无/负收益是真实负侧潜力；核是否改变可迁移augmentation选择，不能据新高分/公开repo入选。 |
| 27415 Greedy | 四任务3runs，annealing/parallel/第二model无增益，多数首轮改善；negative local结果不能因小或单场景排除，需核预算可比/合成proxy。 |

## 贡献潜力明确（仍须root校准与日门，不当Evidence完成）

| 身份 | 原约束→实际增量→受影响选择 |
| --- | --- |
| 27914 ITQ3_S | rotation后量化与CUDA逆FWHT融合；声称无额外transform误差/严格优于任意uniform需核，实际weight/activation共同变换及精确实现边界；不能接受zero-error宣传。 |
| 27153 preconditionedattention | attention病态矩阵→每headconditioning矩阵→训练condition/额外算子如何取舍；理论假设与效率需核。 |
| 27707 LoRAforget | sequential encoderforgetting→>95%frozen与classifier/shallowadapter逼近LoRA→低forgetting是否归低rank还是frozenbackbone；controlled5runs/6tasks异质性是新归因反侧。 |
| 27164 daVinci | volume-only预算→domain饱和、processingdepth与adaptivecurriculum200ablation→预训练data工作预算/处理深度选择，不能仅开源标准/声望准入。 |
| 27481 DyMoE | 旧expertfreeze仍forget→旧token被新expert吸引的routingdrift及token-type regularization→冻结weights不足保持behavior；核token分类/shift。 |
| 28114 AFM | crossattn step dynamics→pre-softmax Fourier bands按progress调制→控制位置/频带vsentropy作用；非把entropy当独立axis。 |
| 28386 COvolve | 固定环境→env/policy可执行程序对抗生成及MSNE混合→课程/不遗忘保证资格；未见任何truth/泛化保证。 |
| 28416 evolutionaryRL | rewardsearch→可执行completeupdate rule搜索，禁止actorcritic/TD/bootstrap及post range优化→算法搜索scope与evaluationbudget，核新机制/holdout。 |
| 28444 ECR | relevance不能消歧→atomicclaims EER选择及H终止→区分confidence stopping与事实充分，不把低entropy当true；核估计与oracle。 |
| 28554 Hydra | adapterweights恢复不够→attention-mode/lmhead/KV-aware解码三必要接口→retrieval/generation共享VLM且switch需状态恢复，greedy/stochastic有限输出对照不是全分布同一。 |
| 28622 G-TRAC | riskbounded path→trustfloor剪枝+Dijkstra/anchor同步→path总risk是否等价nodefloor，核组合risk与partitionfailure，不能按trust名称给安全保证。 |
| 27343 WMF-AM | completion同分→累计state-tracking受控3ablation/Kcalibration预测有限agentbattery→评价construct与长度难度选择；不能认作任意Agent通用能力分数。 |
| 27375 KAWHI | outcomeuniform→视觉关键heads/regions与paragraphcreditreweight→attention代理与因果credit分验，核实际归因/奖励实现。 |
| 27240 CARE | 激活safety不透明→causalmediation+benign/malicious generalizedeig subspaceprojection→dualmodalrepaireffect/utility tradeoff，安全关键原证必要。 |
| 27517 OpenClawtax | 190advisory patch差分→三moderate/high组合成跨层RCE、lexical allowlist假设失效→单层补丁不能替统一trust边界；安全必要原证，不输出操作攻击链。 |
| 27522 HiddenAds | 不显式trigger→自然semantic image+recommendation行为触发且task正确→benign效用不授权广告执行；prompt/softprompt/finetune权限分账，安全必要。 |
| 27524 AgentPR | rawoverall agent少breaking→maint/refactoring/chore切片更高、confidence不筛安全→能力结论须tasktype+ASTproxy分验，核commits/selection混杂。 |
| 27439 agingattack | addition功能等价→inputpermutation晶体管stress不等价→数字功能验收与physicalreliability分开；长期4年claim需核simulation边界。 |
| 27449 LOME | perframepose/hand输入video→jointaction/envcontext训练→actionguidance与visualphysicalconsequence是否支持独立transition选择，不从pour视频推出可执行robotmodel。 |
| 27910 GAAMA | graphhubdominance→concept节点/typedPPR+semantic融合→具体检索/语义mix的1pt消融vs成熟pipeline，需核真增量而非4nodes名词。 |
| 27987 DsCo | diffusiondistillationefficiencylimit→NOpt/doping原data混合→小syntheticquota与原例保留边界；theory仅分布/分类设置，不给任意foundation训练lossless。 |
| 27771 EmergentRisks | 单agentguard→resourcecompetition/handoff/aggregation下非rare collectivefailure→安全gate不能只单体；核实际intervention/重复/基线而非社会类比。 |

以上保留初始AB阶段的潜力校准，不是22确定候选或完整Source审阅。当前有效单项及普通下一步以本日[SUP_SCOPE](./SUP_SCOPE_20261013.md)末段/README六部分为准；不沿用此处最初‘仅28718/未写Books’旧运行标签，原20仍冻结，最终新增分母未定。
