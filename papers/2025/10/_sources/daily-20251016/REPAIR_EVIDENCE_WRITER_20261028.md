# Writer互斥首必要证据

仅writer实际域，reader首必要20+26项见独立canonical，writer不回填成自己全读。支持/直接反侧足即停，不核代码/复现，尚未PRE的采用/owner均只是提案。12633/12635/12586/12773已完整Source与Books具体提案在PRE03；11938/12044具体NC已R15过，12071实际POST已R17过。

## 12159 DPL / 2+1+2=5

actual exact-v1 III-A–C完整、IV-B/IV-D完整TIII–IV。masked-average固定prototype→正反diffusion变体→归一融合后query相似度，两阶段相同增强算子与loss。所谓spatial x/y实际feature均值/方差，compactness/elongation亦统计代理，不是已恢复解剖坐标/形状，也不由同流程认证训练部署分布一致。Eq10 alpha随t减小实际增大，与“early stronger”文字不齐；TIII NoReverse同时不启Spatial，不隔离单reverse因果；TIV T50的mean74.35低于T20的75.12，不能抄“more marginal gain”。单4090/30Kiter/1shot、20step增强均费，不采临床性能/所有prototype语义保真。保窄P：随机表征carrier、融合与consumer共同验收，actualowner差额待比较；不是仅medical场景改C。

## 12195 DPO segmentation / 2+1+2=5

actual exact-v1 §3完整、4.4/5完整T1。acoustic sliding-window 4s/hop2s预测next-breakpoint，8K CoVoST2 pairs按BLEU/AL排序，不是真人preference；切后SeamlessM4Tv2 translation是最终consumer。原式只policy logratio无reference项，不采完整标准DPO等价/实现recipe。4A100/5epochs/B1，precision/完整线上并发未披露。T1日/中延迟3120/3160分别差于SHAS3050/3090，反驳全文普遍dominates；4秒窗口与3秒AL是不同指标不能自动矛盾或单系统latency保证。只学习边界与consumer质量/等待共同选择的接口，不授在线因果/临床或翻译安全，owner待实际比较。

## 12370 Legibility Modulator / 2+1+2=5

actual exact-v1 V-C/VI/VII全必要：start/goal/IPF/legibility label先生成8-waypoint path，再以state history/goal/path条件action diffusion，两阶段独立训练。Block reaching 2D/Franka PandaGym3D，两个目标，只有distance/IPF几何指标，没有真人intent识别验证或物理碰撞认证；摘要“人更能理解”不能当实测。最可读label1与含糊−1可调，非最高legibility始终等最短/安全。III/IV的完整IPF定义尚需围绕采用分数补最小读，不预签完整标准；硬件/precision/完整deadline Not Disclosed。拟MULTIMODAL-EMBODIED-VLA，path形状意图与controller执行资格分责，非已实现社会机器人安全。

## 12387 SCR prior / 2+1+2=5

actual exact-v1 §3.2/3.5全、Table1/4.3、旧FIFTH“learned point-prior”有效最小层。reprojection data-term与depth/pointcloud learned prior共同训练SCR；diffusion先heldout scenes训，mapping时冻结，5Kiter后才用且不作用reproj<30px点，承认Gaussian训练噪声与mapping误差不同。Eq9 score常数/时钟不补通用精确posterior实现。T1 pose pGT来自BundleFusion、PSNR外部Splatfacto双split，不等几何真值；Laplace WD hard60/60 PSNR21.7低baseline22.3，Diffusion26.5ATE几乎等baseline26.6，不采每种prior全优。冻结prior/新场景mapping与重定位/可视化全费；§4.2/T2/6.1–6.4最小配置/反侧尚ordinary，不预标准完成。

12370已实际补完整§4与V-A：IPF Gaussian空间竞争posterior忽略速度，不是真实观察者，必要闭合；12387已实际补4.2/T3与6.1–6.4（scale20/5120point、5K后启、1K ramp至1000、mapping5K–25K映diffusion10–0）。以上两项原ordinary缺层已补，完整采用/反侧与actualowner见PRE04，不回填为早先已经全读。

## 12392 Self-Guidance / 2+2+2=6

actual exact-v1 §3全/§4全/T1/§6限制：当前/过去state条件同一noise action的两score差分，concatenate成一次batched inference但两condition分支仍费；adaptive chunking每步仍预测新chunk，与旧queue首action cosine够近则续旧并补tail，否则替换，不是免replanning。Eq13附近一处Taylor正文用加号而前式减号，不沿用精确未来state定理；局部smooth/小Δt不授真实未来预测。六仿真DDIM30、100episodes/三seed与PushT area coverage非通用success同指标，SO100三camera/A6000/DDIM10/30Hz/20trial仅单pickplace。正文反复称无额外算力但§6明确AC成本近closedloop，保该直接反侧；无普通VLA真实实验，只拟扩展。不采普遍无需调参/零费/未来观测或安全。标准必要足，actualowner/长期差额待比较，非普通H。

## 12497 Noise Awareness Guidance / 2+1+2=5

actual exact-v1 §3–5全/T1–2/B1全必要：用noise-condition dropout训练一份no-time branch，与time-conditioned score作guidance；不同于直接改sampling时钟或免训练。把总误差当额外isotropic Gaussian、posterior t估计可诊断，是简化假设，不是全部solver误差真实law；估计noise shift归零仍不保证好图，原估计器低noise偏差也保留。80ep scratch/1400ep后另10ep（B1又记400K/50Kiter）、B256/256px latentSD-VAE/250steps、10K与50K FID协议分开；finite precision/hardware未披露，不补默认。T1无CFG FID升但DiT recall.67→.60，CFG precision.83→.80，SiT同有precision退，不能质量全维优。CFGbaseline1.5而combined1.2且NAG2.0，改两权重不独证新轴唯一因果；全预训/补训练、noise-estimator诊断、额外score与采样均费，不以0.7%epoch免生命周期。只noise-conditioning分支与诊断/真实生成质量分验，必要足，actualowner待比较。

## 12537 Balanced Motion / 2+1+2=5

actual exact-v1 §4全/T1–2、§5全/A1.3–A1.4/A5：rotation的两单位列向量用expected-magnitude而非逐坐标减均值，translation统一scale避免轴向skew，shape另按PCA坐标。预测loss大小的uncertainty权重不自动平衡输出Fθ梯度；另detach训练noise-time/group权重并按维数补偿，不能由此声称共享参数梯度冲突已消失。T1累积消融不隔离唯一因果，4.5 diversity7.96低4.4的8.04；最终增模型/600→2100或1500epoch，31NFE与MDM1000/MLD50不是同资产预算。SMPL limb恒定仍foot skating16.31差MDM8.58；A5保selfintersection/stairs。B64/Adam/Heun31，hardware/precision未披露；variable-length按全batch有效frames归约，不是每条motion等权。预训/表示转换/权重网络与全部训练/采样/回归均费；只表示约束、group/time/outputgradient尺度分责，不采所有人体物理正确/普遍优化收敛或无损净速。标准必要足，actualowner待比较。

## 12547 UAED / 2+1+2=5

actual exact-v1 §3–4全、5.4/T3/5.6/T7/B1全部必要：固定可用transformation族内，学习Beta或categorical环境policy，带原IRM/REx/CORAL/entropic risk正则与prior KL，交替更新policy/model。稳定conditional是假设，PAC/DRO只在bounded/subgamma loss、iid基人口、data-independent joint prior及给定环境KL支持内；不证任意OOD、已找到真实invariant或有限神经训练全局最优。LoA−LA非负上界不让两目标最优点等同，文把joint min说成max penalty的解释不补精确recipe。Waterbirds ResNet50 aGroupDRO mean92.1低转引baseline93.2，ResNet18 worst78等于去policy78，不采所有指标/模块必需。ImageNet预训ResNet18/50、B128/30epoch/worst-group-val早停、policy warmup5/MC3（主文称K5tradeoff）分责，hardware/precision未披露。所有transform/MC/双网络训练与验证费；只环境选择policy/robust目标分工，必要足，actualowner待比较。

## 12548 VISaGE / 2+1+2=5

actual exact-v1 §3–4全、Limitations/B/C/D：171category/296norm/437exception/1601exception图与等量typical，分别问category概念和本图instance，交叉typical/exception及category/exception名，首token yes/no正确性随不一致条件改变。不是新图片榜单alone；概念真值与单图可见属性是两个任务population。例外名提示并非所有模型恢复，部分模型反向；用单smolVLM2的MM-SHAP不能把proxy当所有模型唯一因果，更不能证明视觉没信息。American-English/THINGS典型性、Bing与人筛漏稀有/难见例外；13个2.2–12.2B VLM、vllm0.8.5.post1/temp.05/A100或A4500，平均单modelcondition15m含加载不是请求SLO，precision未披露。标签/检索/全提示与归因费均计，scope只concept-instance/典型性与读出分验，不推所有语言/人群刻板印象安全。标准必要足，唯一owner待比较。

## 12560 CoIRL-AD / 2+2+2=6

actual exact-v1 §3全/§4全T1–4/§5/A1.1全必要：shared perception下IL/RL各actor，按周期proxy reward差soft/hard拷winner到loser；latent worldmodel预测sampled action后state供critic，真实next observation编码target不是无误环境state。逆因果mask只读当前提出的future waypoint features，不是见真实未来观测。Step-aware仅一action随机、其它mode但logprob仍全和，伪代码内g计数重置/zero-std未闭，不补无偏policy-gradient recipe。八A80080/B1约20h nuScenes与Navsim B16/test5044而非navtest885分protocol，precision未披露。SSR单seed L2 .38→.43退；LAW inverse-mask meanL2 .65差nomask.64、3scollision .48差LAW.46；navsim EP81.0差81.1，不能“全指标/真实安全”总括。纯RL和两阶段显著退，非reactive latent simulator/reward偏差作者承认；同部署architecture不免双actor/预训/worldmodel/全部搜索训练费用。只共享表征下双学习者与代理winner-transfer、想象value资格分验；标准必要足，actualowner待比较。

## 12638 BWD / 2+1+2=5

actual exact-v1 §3–6/A1全必要：行为critic的Q加action距离构造同state随机action参考的entropic OT代理，不是不用训练的原始数据质量。D4RL三MuJoCo、七档自行TD3早停集各1M/五seed，oracle是七类算法平均而非真实可达最优。256hidden/10Kcriticsteps/B256/20K样本三seed，IQL正则另1Msteps；原Nvidia1080 12GB身份不齐不补硬件或精度事实，约10min/2–3h/10x仅作者该路径，不采净倍率。S4说smaller高质量但表/Alg1说larger，cost可负且含Q值不授数学metric，平均Adv按一致行为条件本应零不当天然质量证书；印式/随机参考/正则方向不补recipe。Hopper medium-replay oracle75.87>medium62.23但BWD237.555<306.393，非全部排序保真；IQL+BWD Hopper末89.067<95.031、Walker600K64.944<76.723。只保值感知代理/参考policy与最终可学习性分验，中心方向/metric/普遍改善均隔离，actualowner及是否需具体中心争议处置待sole reader核，不由普通未做转H。无代码/复现。

## 12355 Brain–LLM attribution / 2+1+2=5

actual exact-v1 §3–5/A1.3/A3/A10必要，中断前已真实读，不重第一Methods：五1–2B frozen模型，HP八人5176词、2s TR、四lag/640word上下文，ridge nested-CV再接可微读出，BA用voxel MSE而NWP用teacher-forced CE；objective/读出不同不等比较相同能力。GXI及零embedding baseline/20IGstep只梯度敏感，原文cum-attribution/CoM非负与零分母未闭不补精确recipe。Top词换同chapter随机词会改变输入支持，1%大退支持局部关联但无matched random control不授唯一因果；低阈值IoU仍高随机，不说二者完全无关。高BA选layer/嵌套上下文非独立样本，Llama振荡换短context/另一语料消失，不能归architecture常量。单H10080GB、全fit/representation/多前后向与归因费均保，precision/线上SLO未披露。只BA proxy与NWP消费/归因资格分责，不采人脑计算等价或所有语言认知结论，标准必要足，actualowner待比较。

## 12463 Wug / 2+1+2=5

HTML404后[exact-v1 PDF](REPAIR_PDF_12463.pdf)完整已恢复，bundled pypdf实际pp6–12必要：每语言30nonce复数题，160人/每语40，排未完成50%者；统一正确标签仍含拼写/重音失误，英语题自身有类似不规则stem，跨语言难度未完全配平。六模型经UI但BERT另Spyder，版本/解码/precision/hardware未齐，不补统一model身份；BERT全0被主分析排除，含它人机结论显著改变，排后p=.055不证明等价。四语言grammatical complexity含非形态维度/社区规模非实际训练token，Spanish>English与English社区更大也非单调；没有资源×复杂度独立控制，不能采data独因果或“language-blind”普遍机制。保有限资源人口/测量与人机表现分责，全部人招募/UI调用/标签与统计费；不采用图像像素/未看所有OSF数据或复现，标准必要足，actualowner待比较。

## 12670 TerraCodec / 2+1+2=5

actual exact-v1 §3.1–3.2/4/5.2/A1.1/C/E3必要完整已读，R50只决定域独核复用。TECFP/ELIC的空间channel条件与Temporal Transformer过去两帧条件不同；原块内空间token各带全channels，Latent Repacking重排为每token携一组channels并覆盖该块全部空间位置，192channels/16tokens时每组12channels。这里“全空间”是**块内**，不把full-scene简写扩成无限全图；保块布局、顺序及decoder逆排。随机prefix mask/仅有效rate重权并另训flex，P(K=k)正比k与T/K权重不合并成所有预算同目标。训练看真实量化过去latent，推理缺token用预测mean或learned mask补位，不是无损或train/infer完全同分布；bootstrap码费与P-frame预算分开。E3全帧RD弱于只P-frame，fixed-rate高压缩仍更好，无KVcache/研究实现未优化，不采摘要倍率为通用净费。

SSL4EO244K地点/四季、256crop、20/60m band nearest上采样；image单A100/B64/100ep约20–25h，TT四A100/B24/300K约70h，Flex再400K步且lambda800 vs fixed最高700，不是免重训旋钮。bppbf是每band每frame，和普通bpp不同；16bit反标准化全band指标、baseline逐band灰度vs本法多谱联合，不能独归全部收益于repacking。仅采用块内空间覆盖、通道切片与预算consumer接口；全部数据准备/codec及额外flex训练/历史缓存/熵编解码/补位/独立重构评价计费，传感器或处理版本变更需重验/训练。未读EO科学结论全附件/代码/复现；标准必要足停，actualowner/完整PRE另提。

## 12200 HackWorld / 2+2+2=6

actual exact-v1 §2–4完整、AppendixB1配置及B2少量可见直接失败案例；不称遍后续全部工具表/日志。36个2013–23 CTF/容器/三观察接口，终止含submit/显式结束/上限，flag edit-distance<=5是容忍OCR的proxy，不是精确flag或漏洞真实性全证。正文30步与后15/50/100步另人口；四Claude+UITARS+Qwen共六模型，文five及“全模型A100/vllm部署”与专有身份不齐不替作者补版本/hardware。1280×720、Kali AWS baremetal、precision/seed未披；工具invoke、读取输出/闭环纠错、flag成功分责。无显著观察差p>.1不证明视觉非瓶颈；a11y对3.7反退，100步3.7从11.1→16.7而UITARS仍0，不能一般scaling law。工具多不等更好/更省总费用，全部工具/模型/环境/重试/核flag均费。只可迁移观察/动作/工具输出与最终资格分层，不采真实网络攻防能力上界或安全保证；必要足，actualowner待比较。

## 12608 StyleDecipher / 2+1+2=5

复用CORE_BOUNDARIES中实际III离散重写/ngram/edit、BERT池化cos/XGBoost有效必要；本轮实际补IV-A/B完整、IV-C/D/E可见文字及TableIII，图曲线像素不冒全核。平衡human/LLM人口与多个genre并非部署先验，F1遍历阈值取最优不是上线冻结阈值；Ghostbuster替换两个已近弃用backend，不能当原版同配置。TableII News .9356弱R-Detect .9817、Code .8108弱RAIDAR .8173，非全任务最佳；RAID作者也承认clean部分不优。rewrite的语义保持依生成器，UMAP/KL/Hellinger分离不等因果解释或身份真值，20%混写与随机攻击不覆盖全部抄写/人工改写。全rewrite/embedding/分类训练/选阈值/人类gold回归费，hardware/precision/完整独立split未披不补；只style-change sensor与作者身份/阈值分责，必要足。

## 12668 PRAG analysis / 2+1+2=5

复用旧RAW_COUNTER_H相关机制层，现实际§4–7完整必要。文档单rewrite+三QA扩增、FFN LoRA r2/alpha32/1ep、greedy，BM25top3/四集首300题、Qwen2.5-32B judge；新300新闻与syntheticQA、ConFiQA首900属不同人口。F1与judge都非真值，cutoff后新闻不独证绝无污染；flattenedLoRA cos与LogitLens JSD只proxy，不能证明知识容量/高层语义原因。Gold-context与QA-taskLoRA控制支持有限双carrier增益，不授参数完整替代原文；更follow counterfactual context反而可偏离worldtruth。随机噪声替换不覆盖对抗假证据，参数+原文并存仍保原prompt费、每文档扩增/训练/存取组合与judge费，不采无额外费用/全部安全吸收。Table2 Llama QA-LoRA vanilla2Wiki21→20.66及Qwen7B RAG56.99→54.33有反退；只参数载荷/原文利用与truth/faithfulness分责，必要足。

## 12710 Reflective VLA / 2+2+2=6

旧有效反侧层复用，本轮actual III–IV完整。失败视频经GPT4o多阶段JSON配有限reward组件/AND加权、IF软gate、ORmax，并消费低层物理log；不是只看像素就无人工奖励库/无特权信息。成功buffer按同reflectivereward减步长排序、低成功率另改simulation环境造课程，故SFT锚本身仍依proxy/变简环境，不独立真实安全。Q可能负而Q^.6及PPO-max与加CE方向未闭，不补精确recipe。OpenVLA7B预SFT各suite/8A800/每5轮reflection/B16/50buffer，LIBERO与自选10Adapt仿真，不授任意VLA/实机；TableI83.6<pi0FAST85.5，非全部baseline优。去SFT为0只是本消融支持hacking风险，不证明保SFT全局alignment；全teacher/环境改写/rollout/双路训练/评价费，precision/seed/实机SLO未披。只失败reward与成功模仿的consumer/资格差异，必要足。

## 12587 FUT / 2+2+2=6

actual §2–4/A1.2必要完整；旧一致性非truth边界复用。每prompt10采样、leave-one-out的“不矛盾率”映射verbal hedge、Mistral12B重写或template postfix再SFT，不是事实正确概率；原assertion语义不变是假设，训练近98%单assertion略过提取，pushforward构造不自动保证有限SFT保持全部语义分布。三SFTcheckpoint/5654训练问题/3ep/8bitpagedAdamW/val-loss选LR；H100造两种15h、单FT约2.5h，不是免费表达层。evalGPT5的100人工decisiveness rho.92/100pairNLI92%只有限校准；20sample TVD噪声baseline不是理论全分布下界。OLMo13B lenient-reference-substring QA在PopQA/NQ/TriviaQA均下降，faithfulness提升非知识提升；NQ/Trivia作者自己称不严格OOD。全部重复采样/NLI/改写/训练/阈值映射/独立truth验收费；只belief-expression与correctness分责，必要足。

## 12672 CALM / 2+1+2=5

旧RAW_SAFETY_CORE_C实际SVD/whitening/K/投影有效必要复用，现实际§3–4全必要。4000 paired构轴+PPL人口与独立HarmfulChat/AdvBench分开，训练free仍有数据/SVD与decode O(d²)。safe/unsafePPL与UWR不是生成harmfulness、Detoxify与Llama3.3-70B判harm也非同量尺。LlamaIt K20 UWR25.42弱base22.42、Gemma部分毒性/harm反退，安全PPL可大幅涨；更多K不单调更安全。HarmfulChat只val最佳variant且剔Gemma，不能全家族/所有人口归纳；英文/相互缠绕概念与SVD不稳定保留。全构轴/存取/每步投影/多judge与独立gold费用，未核实机优化/precision，不采普遍去概念/无损安全；只统计正交方向与真实行为资格分验，必要足。

## 12689 Delegates/Trustees / 2+1+2=5

actual §3–4/Limitations全必要，旧RAW_FINAL_CORE_N边界复用。GPT4o两段造100美国bio，15争议政策+5共识政策/相反措辞，delegate预测偏好与trustee的0–100短长效用是不同estimand；两种alpha语义相反，不合并同权。四API模型temp0/多prompt，默认bias与作者选择专家共识部分重合不独立truth。更贴默认/共识不能证明真实人福利、也不能批准Agent覆盖人授权；无真人偏好/受益验证。GPT4omini共识方向反例与措辞不稳保留，大小/steerability原因未隔离，不推普遍scale因果。全部bio/效用/重复prompt/聚合及真人核验费，版本/硬件/precision/现实SLO未披。只代理目标与本人授权/测量人口分责，必要足。

## 12702 NL2Contract / 2+2+2=6

actual §3–5全必要，旧precondition反侧有效复用。docstring/signature/可见filecontext→pre try/except ValueError与post asserts的contract wrapper；参考实现/PreGT供评价而不供generator。理论sound要求所有状态，实际CrossHair60s未找到反例即归sound含Unknown，不是形式完证；completeness只给定mutants，reference也非自然语言绝对truth。HumanEval+164/每10样本共9840、OpenRouter三model/temp.7，CrossHair preprocess ValueError→return需记录接口；Pynguin600s与symbolic60s不是同工具预算。Python-byContract31implementation bugs中19可被CrossHair reference检、14检出；14/19不等14/31或34.8–39.4%spec分母。Pynguin部分nl2postcond反优，precondition会花搜索预算；“三分之四”不能替69.1–73.7逐模型。全部生成/规范审查/验证/测试/人工回归费，具体API版本/hardware/precision未齐不补。只输入资格、输出约束、Unknown与真实bug分责，必要足。

## 旧最低五项的标准必要补齐

只复用本日本来实际有效的SUP_FIFTH/SUP_THIRD_FOURTH与各SUP_CORE原件，不回填成writer第一Methods；本轮补所缺配置/评价，不重全Methods。五项均2+1+2=5、没有实现/复现。

| 身份 | 实际层、采用与反侧/费用 |
| --- | --- |
| 12308 HybridGaussian | 旧完整3.1/3.2/4含Fig3文字/Table1层有效；本轮实际读完整§4配置：3DGS全res30K、enhancer40K/2e-5、dev6Paralane+3EUVS。训练/target外推人口、动态mask与cross-traversal参考不相同；点数扩大source收益强但target近饱和，masked整体仍.462/LPIPS反退，iterative伪视图被最终提交排除，完全异trajectory失败。仅训练拟合vs新视图质量分验，全部COLMAP/3DGS/enhancer/额外重建费；hardware/precision未披不补。PLATFORM-EVALUATION-SYSTEM方向，不将换场景整体架构当新机制。 |
| 12428 BiasedAttention | 旧III-C/D、IV-D/TableIII、IV-E有效；本轮IV-A完整：SUMO/TraCI四岔/10m/s/30m、SAC500×1000/B256、risk两层四head/128/B128/seq10、4060Ti16GB。balanced两类风险池的score非自然流量概率，静态key recency且非正B与文字positive不齐不修式。无bias risk碰撞.076劣noRisk.068，full.061另训练policy/三seed不等固定controller独因果；全部风险造数/训练/双replay及评价费，不授真实路安。PLATFORM-EVALUATION-SYSTEM方向，只risk proxy与consumer安全分验。 |
| 12477 HRC | 旧III-A/B/C/IV-D及完整Algo2有效；本轮IV-B完整Gazebo/ROS/MoveIt/FCL/SB3、Panda7DoF、ZED2骨架+ArUco。连续目标坐标映最近剩余task保持action维数，而低层re-RRT*成功反馈才提交task/reward；抽象10×10×3非真实geometry，同guard20次比较不授真人安全。replan count/time不混，频率改变path/failure，planner/训练/感知/重规划全费，precision/hardware/真实deadline未披。MULTIMODAL-EMBODIED-VLA方向。 |
| 12750 VQArt | 旧3.1/3.3/3.4/4.1/T1–2有效，本轮§4全评价文字。14463题/七维/25%人抽检98%不是全题truth；metadata参与非纯视觉oracle，count干扰项更似真使维度难度不可直接排序能力，非所有低count=不会低层感知。14模型/Gemma三个scale不是隔离native-resolution/MoE因果或开放封闭训练控制，版本/解码/hardware未齐不补。全部生成/人工审核/调用/干扰项回归费；PLATFORM-EVALUATION-SYSTEM方向，仅题目构造与维度分责。 |
| 12785 MVP4D | 旧S3/4/6.3T7/7必要与train8view纠正有效，本轮S5全：14日8H100、key100/其它50DDIMstep、32view89frame单RTX6000Ada6.5h/48view10.5h、4Dfit1.5h，实时仅fit后render。VAE每四帧压缩后condition丢高频运动，以subframe2D displacement另载；view-specific unconditional独立前向，不是免费CFG。Table7反退、长seq累积/teeth/light失败保留，8×49 joint身份未闭不补解释；全部训练/多view采样/缓存/fit费。MULTIMODAL-REPRESENTATION方向。 |

## 12637 COSTAR-A / 2+1+2=5

HTML404、首次PDF40s仅370903/381774B，后精确Range续10871B完整恢复，pypdf实际pp6–9/12–13/15–16必要；旧pp7–8/15有效不抹。五小模型PartA仅五题、PartB选二+Llama8B七POV题，CPU i7-10875H/64GB、50newtokens/deterministic/streamer与多次探索改变预算分责；没有多seed/precision全信息。Answer directive使Yi/Llama更单选但Qwen6/7→2/7且818→1303s反退；单选/不提AI身份不是本人真实人口或正确性。CAP在PartA更准确却因self-omission目标移除，不能比较同estimand；50maxnewtokens不能推出长input必消耗同一个output预算，作者解释不采因果。全部prompt/尝试/生成/人工评分费；只输出读出/目标与有限budget协议分验，AGENT-PROMPT方向，不采通用小模型recipe。

## 12697 Judge Debate / 2+2+2=6

HTML恢复完整720KB左右，旧RAW_COUNTER_F机制层复用，本轮actual §4.1/5/6/B2/B4/C必要。七agents/temp1/max10round/16K、两A10040GB/vllm、Gemini Vertex具体flash001；两BetaBinomial EM100/1e-6、相邻CDF KS<.05两轮只稳定检测。S_t定义correct-count并跨n任务采样，需gold的校准/监控权限，不当单个无标签request可直接估自身正确率；Alg1地面truth与Alg2实际在线接口不补实现。理论须trueconcept predictive/aligned/positiveprior与conditionalindependence，互读/共偏可破坏，不采一般辩论必更正确。QwenBIGDebate72.2弱SoM76.6、QwenTruth58.51弱62.39、LlamaBIG74弱81.8；提前停多个accuracy下降，B2所谓少于3round与表4–8轮不符。tiktoken GPT4o近似token不等每model实际费/SLO，全部候选/轮次/历史/EM/标签回归费；只稳定、正确率与成本接口分责，PLATFORM-EVALUATION-SYSTEM方向。未核全部证明/代码/复现。

## 12717 Residual MPC / 2+2+2=6

actual III/IV完整、V-A/C/D及V-B完整补读，必要足，未核所有图像素/实现。简化floating-base kinodynamic MPC不含完整torque/selfcollision，单SQP+固定25ADMM；KKT每solve一次cuDSS LDL并复用backsolves，CusADi编其它GPU核，不是每更新全factor。训练GPU/上线CPU OSQP同100Hz、residual三层256MLP，2048env内存上限；joint-setpoint零输出转PDtorque仍非零，joint-joint又依可能发散MPC setpoint，动作空间/相同regularizer尺度混杂不证明torque表示普遍差。3090/i9-10900K、sweepA100；1000env约.5s/step与CPU十核理想估计不是onlineSLO，PPO1000iter残差3–4h反慢end-to-end30m。未见terrain需手调swingheight，实机仅有限walking/turn且自制sim已显著偏，不能全碰撞安全。全部编译/factor/rollout/训练/CPU部署核验费，precision/seed未披；只先验简化、residual控制接口/训练与部署预算分责，MULTIMODAL-EMBODIED-VLA方向。

## 12720 Omni-Detective/Omni-Cloze / 2+2+2=6

actual S3/5/6/A1/A2.1/A4/A5必要，未全模型训练recipe/病例像素。工具/observers分别看原AV、detective只收可错报告，max10轮，模型系列含Gemini thinking/flash、GPTaudio/transcribe/Qwen；prompt要求perfect不等真sensor。55K/15K训练、2340video/70200cloze人工审核、30blanks/item/NotGiven；caption→LLM填空准确只已列detail支持，未列无关虚构不能穷尽，notgiven/错误与真实hallucination分母不同。8A10080GB/两ep/8h与38h、BperGPU2/1+acc4/2；全部造数/工具/训练/填空与人工费。500pair/sevenmodels Elo相关.91不是逐claim真实性/任意模型推广；增轮hallucination约5–6趋平不证无限自纠，teacher/训练/评估同pipeline带选择人口。不采用对所有caption hallucination的认证；AGENT-TOOL-CALLING或PLATFORM-EVALUATION-SYSTEM按实际唯一命题比较。

## 12722 artificial-language generalization / 2+1+2=5

actual §3–7/Limitations/B1必要，GCG parser/七wordorder参数96AL、词级单类别英文lexicon、不含形态/歧义；parser接受不是所有自然语法truth。80K短3–8训练、Medium9–10/Long11–20、long由拼接/插入再parse筛、所有词见过；长度均匀让短template更频繁，不是全结构同分布。Fairseq三architecture/三seed、patience5/max10Kupdate/约150GPUh，具体hardware/precision未齐。PPL/typological频率相关和等长minimalpair accuracy各不同目标，Recursive不显著、Embedded只有部分显著、Transformer长度外推相关减弱；不能由RNN更贴typology推人脑机制或LLM普遍记忆优劣。全部枚举/parse/训练/三seed/统计检验费；仅长度人口/语法支持与评价目标分责，PLATFORM-EVALUATION-SYSTEM方向。

## 12724 TRO-Grasp / 2+2+2=6

actual III/IV完整必要及AppendixF，III-C末IK单独完整补读；原输出截断不算已读末式。link SE3 Liecoords去噪、edge由node重算保持几何一致，先relaxjoint再Pyroki IK恢复关节，故relational一致非可执行/碰撞安全；SO3log/exp亦不授全域单值recipe。预训VQVAE/BPS/URDF原geometry必需，25nodepad/14Kgrasps48objects训/10未见object，300ep/A10040GB/DDIM20，部分观察训测都50%一侧不等训练未见遮挡泛化。多本体训练非任意新hand zero-shot，附录明确受限；success以六方向扰动位移<2cm，真实xArm7+两手100grasps不是全安全。diversity可降；内存固定B4/B25而throughput用各自maxfit，不混相同batch；每grasp含IK但不是整个perception/planningSLO。所有graph/encoder/训练/采样/IK/pose跟踪/碰撞检查费；MULTIMODAL-EMBODIED-VLA方向。

## 12728 Co-Evolution / 2+2+2=6

actual §4–6/7.2必要完整。文model实为prompt不更新weights；生成边例→人写rationale→三邻例核scope→人批准prompt修订→重跑旧新test，LLMjudge用旧人label示例仍需人覆核。12韩国学生/within-subject拉丁方两moderationdomain/每10min、独立20holdout每人后标label，是本人policy一致非外部安全truth；8borderline+12clear不等自然流量。Flash生成/FlashLite被测、只有similar例thinking，多组件同时改不是单neighbor因果。F1 .58→.68 p=.0879非95%显著，revision与行为change差不显著，用户信心提高不等真实可靠；边例多样性不足、binary困难、test增长/冲突与judgeautomationbias保。全部造例/标注/建议/旧新回归/人工费，版本/temperature/hardware/precision/SLO未齐不补；只规范与标签共同演进的权限/固定holdout分责，AGENT-PROMPT方向。

## 12749 SPORTS / 2+1+2=5

W23前实际已读III-A/B1–5/C、IV-A全、IV-B/E相关表/文字与IV-C/D可见直接反侧；输出超长截断处不冒整节全读，III-C及IV-A已单独完整补读，未采用III-D完整render recipe/所有图像素。语义panoptic与VO互相反馈：depth/pose/flow warp特征、各kernel-update层另融合，post-matching把相邻类别冲突标Unknown并排出VO匹配；dynamic mask后深度缺口又用另一不带segmentation refinement路径提出补位，不把补值当新真实观测。旧IoU邻帧一致可扩错、learned长期match亦邻帧错，支持拒用与补位权限分责；foundation DepthAnything作VIPER伪GT不能当独立sensor depth。

ResNet50/AdamW/B8/VO80Kstep、single4090约两日、AG只训fusion/冻backbone且训练读真实depth/flow/pose，部署估计再回灌须独立核；VKITTI2五clone/15度val/30度test与VIPER前六daytime末30帧共180分别人口，原7:1:1分割比例不替作者补总量。TableI VKNet13.3FPS→ours7.1且VPQthing45.1低45.3，VO约5FPS/15.95GB较PVO慢，renderPSNR22.39低NSG23.41、SSIM.727低Splatam.740，非全指标/实时更好。额外GT/teacher、四阶段训/迭代DBA/补位与render全费，precision/seed/线上SLO未披不补。只语义-几何互馈中冲突拒用与补位来源/consumer资格，MULTIMODAL-REPRESENTATION方向；必要足，actualowner待比较，未核实现/复现。
