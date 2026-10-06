# NEXT M6：最后已校准 named-tail 的安全/数据/控制必要证据

作者采用提案，非独立通过，不增加 safe。exact-v1、既有日期/完整题摘校准复用；源坐标 `V3_BLOCKS_2602.<ID>.md` 的 block ID。拟 I2/E4；安全项已加深决定其采用的反侧，不泛审无关附件。

## [21773 Easy to Learn, Yet Hard to Forget: Towards Robust Unlearning Under Bias](https://arxiv.org/html/2602.21773v1) — 2+2+2=6，拟 Existing Ch72

forget-class accuracy 下降常被当作已删 → bias-aligned训练中去掉 shortcut 可以反而提高目标 class 表现 → 删除对象与合法泛化能力不能由整类分数互签。必要12–19/28–58/61–73/81–86。原30说forget loss上升、31又写下降；只采用13/32明确的BC accuracy可增加与linear bias probe减弱，不照录整条曲线方向。作者用一次normalized gradient loss-change的top5%近似“sharp”，Hessian diagonal×θ²再mask50%与gradient projection；这不是因果特征识别，72明确partition不纯，GradCAM非因果证据，故不写sharpness=causal。

ResNet50、99.5:0.5 biased训练/50:50 test，class-forgetting；RTX3090/train10ep/unlearn1ep/B128或64/η.001。Table3 retain99.81→91.32(partition-only)→99.45→99.94，forget34.96→20.38→14.56→6.91；partition-only MIA27.89高于18.44反侧，MIA也不是永久删除。Seeds/CI/完整费用ND，gradient/Hessian与group/probe审计额外付费。采用有限shortcut-erasure反例，不采普遍删除成功或因果分解。

实际 Ch72 2656–2662 已明确移除样本后重训仍可从retain合法泛化、不把答案/accuracy当影响删除；2710–2725已区分prevention/参数影响/行为/probe/relearning并保decomposition有效性与retained utility。2745–2758更已将unique memorization与共享能力分账。因此具名反例放报告，拟 Existing，不为CUPID分解recipe造段。

## [21977 When LoRA Betrays: Backdooring Text-to-Image Models by Masquerading as Benign Adapters](https://arxiv.org/html/2602.21977v1) — 2+2+2=6，拟 Existing Ch72

冻结base或只装小adapter容易被误当安全 → text encoder与U-Net两处LoRA可联合学自然词触发 → admission必须绑定实际可变组件与条件行为，而非base hash。必要20–46/48–63/68–81：30%poison，contrastive embedding alias + poison-only timestep-weighted MSE；不采LoRA必然low-pass或通用机制归因。SD1.5/SDXL、rtext8/rU16、25epochs；PoisonLoRA5.4 vs99.8 ASR同时15M vs28M参数，非matchedcapacity。Gemini2.5Pro judge为所测target代理，训练集规模/evalN/CI/seeds/hardware/precision ND。

Adapter composition有反侧：4个object adapter91.6低于单99.8，style65.5低于81.4；benign CLIP23.4低于30.6，λ>1也让benign car→cat。Semantic probing仅定性提案，无defense FPR/recall有效性。不能由干净base、常规FID/CLIP或少量probe认证无后门；替换/隔离adapter与独立trigger/cleancanary是工程验收推断不是论文验证的防御。

实际 Ch72 1021–1056已有生成链、projector/conditioner可变资产、低秩信号≠最终行为、probe/来源/rollback分责；2368–2382明确参数的分布触发行为与admitted adapter bytes、未认证组件和实际执行绑定；80–82本身也承载有限LoRA权限/未检出不授安全。拟 Existing，保两个组件联合身份与matchedcapacity限制于报告，不写攻击recipe。

## [22014 A Diversity Diet for a Healthier Model: A Case Study of French ModernBERT](https://arxiv.org/html/2602.22014v1) — 2+1+2=5，拟 Integrate Ch27

只用全面fine-tuning成绩验收pretraining数据，会把encoder自身差异和下游适配混合 → commensurate size的lexical-diversity采样收益只在部分frozen-encoder/head-only消费下明显 → data-selector质量必须绑定consumer可更新的参数域。必要29–69/73–85。Entropy normalize URL/数字等，BASE共5%FULL，EXTENSION按lexical entropy选，wordcount相近不等exacttoken；不是新entropy算法或其余diversity受控，85承认形态/句法/语义相关混杂。ModernBERT200M22L，random/diverse均483H100h，较小数据不等更短训练；Topline1775h不作matched效果。

73的下游FP32/Adam/B32/最多32ep、5fine-tuningseeds，与pretrainseed数量分开。75 fullencoder+head六任务无清晰一致优劣；76 head-only仅MEDIA/ATIS显著，150M时51.9→61.5与80.2→84.3，到400M差异基本消失。FullFT补偿是作者解释，不证明纯lexical因果；pretrain loss Diverse较高也不等下游更差。Entropy计算/重采样、pretrain与各消费协议回归均计费，不能授高entropy总更好或tinydata可替代所有encoder。

实际 Ch27 246–256已有quality/diversity proxy与population/预算/失配回退，但未明确用可更新encoder vs frozenreadout对同一selector分别验收会改变可见收益。拟在该段后一个短consumer-contract段+ownnote，绑定数据成员、update mask、目标任务和总训练budget；证据不稳仍保random/coverage与fulladaptation，不把这一个French encoder改作LLM定律。

## [22088 Force Policy](https://arxiv.org/html/2602.22088v1) — 2+2+2=6，拟 Integrate Ch26

在固定tool frame纠正视觉动作，对受不同contact regime约束的motion/force会混轴 → local policy按regime提出interaction frame、force/position selection与desiredwrench → frame、mask、目标和低层控制责任必须成组校准，而不只增加force输入。必要26–43/47–73/77–100。Locally conservative/invariant topology排除plastic/fracture，knowngravity/inertia要补偿；结构/耗散不同关系的orthogonalization在48明确ill-posed，Gemini3Pro visualsemanticclassifier参与regime选择，不是force自动恢复geometry的证明。IF原点用EEF不是已估contactpoint；zero/collinear条件没有完整识别证书，不采用普遍力学保证。

Local读motion/wrenchhistory、旧globalvisualcontext且67仍读wristimage，不称force-only；其Σrotation、Sselection、desiredwrench和chunk为proposal，S/hysteresis决定local/global切换，错global/no-contact仍可失败。两路async/50Hz resample/DTW、dropoldprefix与加速度规划不认证worstdeadline，hybridforce-positioncontroller继续physicalcommit。

FlexivRizon4/6DoFsensor/2D415，50demos、PushFlip20trial/其余10trial；partialphase记.5success不可搬成full completion，πA800 vsothers3090不能归因系统速度。TableIV新obj5trial有5/5→2/5；wrench-only50 vsfull90 Scrape否定所有vision无关。45N低于基线是该任务proxy不是物理安全阈；contactpoint/torque future100明确未解。额外sensor标定、regime/modelcaller、同步/DTW/controller费用与free-spacepose/保守低层fallback近新段。

实际 Ch26 776–790已有视觉chunk→快contactfeedback与腕/握持分责，但未承载regime-dependent frame/mask/wrench三件接口绑定，不能仅由固定toolframe/stiffness继承。拟其间单短段+ownnote；不动现有reactiveexpert或重新定义安全权限。

## [22107 Don't stop me now: Rethinking Validation Criteria for Model Parameter Selection](https://arxiv.org/html/2602.22107v1) — 2+1+2=5，拟 Existing Ch28/66

validation loss常被直接当最终任务quality → 同一完整训练trajectory交叉训练objective和validationselector，accuracy选点与loss选点可不同 → objective、selection和独立test验收要分账。必要40–49/57–61/75–89/95–100/105–118。ShallowonehiddenReLU、SGD20Kepochs/B64/lr.01/10fold15%val，train-onlyzscore；同trajectory3trainloss×3valloss/accuracy为核心控制，不是不同run预算比较。89 patience10/50与posthoc选点按实际规则处理，事后max test accuracy是retrospectiveoracle，不能部署或用它调selector证明未知test最佳。

83–85只分别将selector与testoracle比较；Shapiro→onesidedt/Wilcoxon与overlapfold有条件，failuretoreject不是equivalence，更不构成loss-vsaccuracy的直接显著差异。CE/T10 oracle相对gap5.98 vs.43只属该协议，不能授所有lossES坏；plateau/tie解释为假设，不是已识别因果。Fulltrajectory与earlystop计算费用、checkpoint eval与testoracle费用分开；hardware/precision ND。

实际 Ch28 120–126已有mean/分位loss与目标任务关系、proxy不能单签质量；Ch66 78–116的EvalSpec、3270–3287独立目标证书/selection-vscertification明确选择对象和holdout责任；Ch27 166已有不能testbest反选。拟 Existing，报告保同trajectory控制的新有限反证，不为一般earlystopping造Gap。

## [22197 Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes](https://arxiv.org/html/2602.22197v1) — 2+2+2=6，拟 Existing Ch72

Protection评价若只列专用adaptiveattacker会漏普通生成修复能力 → 公开img2img和prompt/strength搜索在多个有限保护协议下可破坏signal → threatmodel必须包含一般变换、utility与完整攻击budget。必要18–31/40–56/74–101/156–167。8prompt pairs选最好不是无需搜索；512输入/部分256upscale和strength改变质量，closedGPT4o/GPTImage1身份不一致不采精确architecturalclaim。

PRC500SDP样本 FPR1e-5:SDXLTPR0、Flux.258，Flux质量较好但不是最低检出；GPTfallback100为选出的Fluxfailed人口，组合.060不升级为独立普遍率。VINE1000WB/FPR.001下Flux.878弱，追加adaptivecrop.7%到.066是另协议，不能同genericdenoise合并。UnGANable17样本原先按counter失败选择，不是总体风险率；SIREN有限0TP不证明所有模型/defender可行性不可能。NoPRCtrainingcode只限制adaptive实验，不阻断上述公开变换经验。跨backbone supervised vsunsupervised强弱也不作scaling因果。

采用一般攻击可用性及分协议预算，完整N、threshold、quality/sourceutility与搜索/生成费要绑定；不授保护全失败/删除水印成功证书/所有归属否认。实际 Ch72 1092–1114已三分provenance、watermark变换/质量/移除痕迹与adaptiveunknown/inconclusive；2710–2717又明确prevention与parameterdeletion分层、shallowprobe/恢复预算。拟 Existing；无通用防御或攻击recipe写入。
