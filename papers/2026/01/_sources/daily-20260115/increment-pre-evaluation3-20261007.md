# 三项评价/校准潜力必要证据与owner提案

作者supp_jan15；已由root完整题摘准入校准，本次只v1必要命题。原件为increment-j15eval-core0–2及increment-j15evalrequired3/4/6，直接abs为increment-j15evaldirect5。日期原字段在increment-dates47，正常announcement下界与Jan14正式ID存在上界按已核方法限定本日；Submitted/Updated/注册不单独授first-public。三个abs当前后续版本无撤回/勘误标记，当前链接无更早dated完整稿，轻核到此不遍历未来全文。

## 07984 Cross-Cultural Expert-Level Art Critique Evaluation with Vision-Language Models — 2+1+2=5 标准完成，具体Existing提案

实际§3–6/Limitations、AppB2/B7–14/F：TierI关键词/TFIDF与语言密度仅heuristic，TierII五维rubric，isotonic只校aggregate而非各维。15VLM/294anchors/4406有效评价，450人标298fit/152holdout；288anchors与人标重叠，五折crossfit MAE.441 vs全fit .433仅局部，不据此称leakage贡献<2%（作者把相对error错当calibration gain）。训练47.6% MAE降低不是heldout5.2%，跨RF→RG heldout4.8%/相关.91不保证所有culture；Islamic/Indian校准反退且部分culture n<25。ICC−.50说明本panel量表不一致，不证明所有ensemble无意义；humanκw.39不是校准后的语义共识。B8纯TierII MAE.43/ρ.756优于robust fusion .58/.670，B9权重排名稳定不是对humanρ≥.97；B7 fusion3.73仍高于TierII3.60，不能当保证降低语义虚高。B14六culture各98却称686总数不统一，故不采用其balanced结论证普遍culture差。AppE作者列具体API version字符串有内部时序可疑，仅按作者协议身份保留、不认证真实endpoint版本；hardware/precision/batch/concurrency/SLO/完整调用费未披露。没有复现/运行artifact。

actual PLATFORM-EVALUATION-SYSTEM Ch66:328–347完整邻接已承载逐judge正尺度不等正确率、共偏差不被fit清除、配对/absolute单位分责与人工anchor/区间退路；368–389已承载fixed bias与随机repeat区别、agreement不授下游统计真值。采用此处具体反侧不改这些判断，拟NoChange—Existing；不为cultural task收纳新段、不采单judge一定优或isotonic万能命题。

## 07974 Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis — 2+1+2=5 标准完成，具体Existing提案

实际§3–6/Limitations：7LLMs/6prompts/4英语域，516k配对文本；去模板/非英语/长度筛选后人文50:17:33split，不是自然全流量。XLMRbase/DeBERTaV3small每种168独立detectors，3epochs/lr2e-5/WD.01/batch16/len512，HGX H100约400GPUh，precision/concurrency/SLO/seed Not Disclosed。跨prompt固定模型域；跨model/domain使用0-shot，并非所有因素共同OOD。nearperfect ID仍有跨domain57%与prompt80–89%失败。80feature的AI-human差异shift与accuracy取abs Pearson，失去方向且复用人口；总体crossprompt.109/.116与局部>.7不能合成统一机制。§6.3确实另做Bonferroni/BH及Spearman，不能误写没有多重检验校正；跨dataset严格校正没有feature显著，更不能采passivevoice为唯一根因。作者Limitations明确关联非因果、限英语与encoder，未验证counterfactual intervention或新generator。无更早direct完整稿信号/撤回，未复现。

actual Ch66:551–587完整论点明确部署风险依赖人口/scorer/污染，不由样本量修分布；636–665明确共享prompt/聚类相关、多切片选择、独立holdout和关联≠失败原因。采用本稿拆prompt/model/domain与整体弱关联、严格校正的反侧已有这些实际承载，拟具体Existing。检测分数不用于自动作者身份/安全结论；不归普遍LLM detector无效定理。

## 07965 When Models Know When They Do Not Know: Calibration, Cascading, and Cleaning — 2+1+2=5 标准完成，Ch56具体差额待root

实际§2.1–2.3/§3.1–3.5/AppD/E Alg1/2：以verifier二值或任务score定义confidence，15equal-count bins；vision temperature/language sampled-token平均logit Platt，非sequence jointlikelihood。heldout一半validation校准/一半test，ECE降低非逐request无误。关键路由**不是线上先跑两模型**：validation按小模型confidence分bin预先统计large−small平均calibrated advantage，再选择advantage较小Kbins；线上先生成小模型，只对未选bin调用large。两模型各自marginal校准并不逻辑保证按small-bin后large仍conditional校准，作者这里只有限跨模态/五LM任务/三种ImageNet-C与MMLUAdversarial对照，非全OOD证书。Small-use比例与accuracy curve不等完整latency/FLOP/SLO，升级还支付已生成small的沉没费用，硬件precision/batch/concurrency/fullSLO Not Disclosed。RouteLLM baseline从pretrained/finetune/scratch择最高APGR，随机baseline是理论平均。same-size并非免费调用；classification/MCQ与codepass不是全部开放生成。

Cleaning two专家都不同gold且highconfidence仅提出flag，独立性是假设。ImageNet1000 flagged random人工核不同于全库rate，cleaning models不等evaluation models但共同训练背景未独立；MMLU/ARC/MBPP用GPT4o thinking pseudo-label不是人工真值，不能把两者human validation权限合并。96.266%cleaned accuracy改变label/evaluation对象，不授原库全部饱和。

actual INFER-SCHEDULING Ch56:1035–1048已读per-model/per-band calibration、选样反馈/漂移与admission分责；1057–1075已读反事实route、profiling/在线实际费用及小模型先付prefill/升级重prefill。现有虽承载校准/费用原则，**validation small-confidence分箱排序large的平均增益、线上只small读取bin**未在这些邻接明确；不为成熟Platt/temperature/ensembling itself新增书。拟若该conditional升级规则确长期差额，只在Calibration Routing State邻接一段，保conditional calibration未证明/离线双模型统计与small完整生成费用、保fixed强路径fallback；当前无写锁。若实际更具体已有段能承载同branch则Existing，不据主题相同默认。
