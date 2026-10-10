# 2603.09205 — 必要Source/date/PRE及Ch29 actualPOST通过

[Emotion is Not Just a Label: Latent Emotional Factors in LLM Processing exact-v1](https://arxiv.org/html/2603.09205v1)。root完整AB准入，作者actual完整§3–7/A/D.2/F；不授全部图片像素/其他附录、引用旧研究全文、代码或复现。currentv2 Mar16题摘相同/comment空、无已见撤回/纠错说明；不由version变化触发全修订或用后来数据回填本窗。

日期原batch2 actual：arxiv.content owning/findable registeredMar11UTC02:07:56上界，SubmittedMar10UTC05:23:18配本轮实际官方noadvance/最早Mar11BJT08下界，同一BJT日夹证03-11；不是registration、Updated或提交单独公开。无已见必要先稿冲突。

拟2+1+2=5，具体长期gap必要深入。准入时MODEL-SELF-ATTENTION的观察是题摘入口；实际必要方法不改Attention算子，改变SFT辅助objective，应由TRAIN-SFT唯一owner承载，LoRA仅参数实现。采用“冻结估计子空间的补空间上约束paired context representations”，不授情绪为唯一因果或语义真实解耦。

## 机制、区别与边界

§5 centeredSVD：syntheticparallel neutral→多个emotion rewrite，层/module activation meanpool sentence，stackN×d/全局center，topk orthonormal rightvectors V_l。不是直接训练读出，也没有把每个语义组均值先剔除；内容/主题、长度/风格仍可能占principal directions，syntheticparallel并不证明topk都是纯emotion。其0.8–.9alignment/stress来自所引用旧paper描述，本轮未复读旧paper不采用独立验证结论。

训练QA CE＋lambda pairloss；hidden减mu后(I−VV^T)取补空间，仅在context位置计算相同题两情绪变体的相对L2距离＋1−cosine，两种权重alpha/beta/平均层与pair组合。所谓“保情绪”是选择loss测量方向，不把hidden在实际forward中永久替成投影，也不由contextlossmask隔离所有sharedparameter/后层。basis取法、k/layers、lambda/alpha/beta、不同长度重写的token t对齐、relative L2原式明确有ε但其数值、cosine zero-vector处理、basis刷新/模型更新身份必要原文未闭合，不补成执行recipe；正文已对齐位置是必要条件，不认证原实现已完成token对齐。

若被排除方向也载semantic/task信息，补空间一致性不能控制该信息；即使pairloss0也非全hidden/输出恒等或hard noninterference。若rewrite改变事实/否定/角色，也会强迫不同问题不该相同的表示一致。loss约束上下游分支是soft偏好，不能将训练效果写成无跨层spillover保证。

## 评价、混杂、反侧和费用

§3 5fold stratifiedCV logistic attentionfeatures predictsQA AUC.75±.03，answer-span focus-from单项.74±.01；使用answer-span标签属于特权诊断，不是无答案runtime sensor。情绪分类forest86%/macroF1.75是读出相关，非tone→attention→QA唯一因果，更不证明human情绪状态。AURA14400/每emotion1600只平衡类别，不匹配内容/长度/难度；Table3neutral meanwords176.8 vsHappy77.3/Disgust44.3，且§4cap150有原口径冲突，不能声称除tone外已全control。

§4/A/D.2 emotion weaklabels：classifier323776source samples/八模型级联ensemble，三LLM unanimityfilter、humanagreement只定点1350balanced accepted/rejected。LLM-humanmajority58.1% vshumanunanimous62.6%口径不同，不用两数相近认证proxy准确；unanimousLLM subset65.8%也非全人口无错。Gutenberg人写passage不等QA人写，QA三LLM synth/difficultyfilter。保留题valid87.6%但humanexactmatch42.8vsfilteredout63.4；模型可答/小模型错是困难选择不是质量真值。

§6 LLaMA3.1-8B/Ministral/Olmov2，四trainQA数据，alllayerLoRA，AdamW3e-4/weightdecay1e-2/cosineschedule50warmup，batch每题两emotion随1200tokens动态大小、untilconvergence。模型具体尺寸除Llama/precision/GPU/LoRArank/steps与训练seedCI/总时长NotDisclosed，合成增强/regularized/baseline不同token及untilconvergence不matched全预算。数据拆分尤其passage/book/semanticgroup leakage和rewrite保义必要描述未独证，不补不存在复现。

Table4三arm实际反退：AURAtrain→AURAtest Llama plain49.9/augmentation36.2/reg44.6、Ministral51.7/44.2/43.5、Olmo47.4/39.2/42.6，均低于plain；Ministral NQtest/AURAtrainaugmentation57.3→reg57.0，Olmo NQtrainNQtestplain61.1→reg59.8，FriendsQAtrain/reg62.2同augmentation非严格提升。保留跨域有限收益而不采用§7所有条件一致改善或均无害。AppendixF仅Llama预算所限单pair有dataset-dependent反退/非单调alignment，本轮读文字不授fig11/12精数。attentionfeature相关与regularization收益不能把全部增量唯一归emotionsemantic分离，缺whole-space等容量/同费用替代对照。

emotionclassifier/老师rewrite/LLMfilter与humanvalidation、basis activation/SVD、paired全模型forward和activation、projectedpairloss/LoRA训练、调参及独立heldout均付费。训练projection不增部署模块不代表总费用免费/生产SLO成立；没有实测完整设备速度，不推加速。

## owner实际阅读与逐字PRE

作者actualCh14 234–246 probe可读/必要充分/attention干预，Ch29 86–117完整CE→entropy→crosslanguagecalibration→multilingualextractor辅助表示→mask，以及Ch28/30开篇。Ch29现有multilingual extractor/collinearity不是在固定nuisance补空间逐contextpair位置施一致性；Ch14成熟因果边界已充分，不另堆emotionalmetrics新段。唯一TRAIN-SFT拟Ch29 multilingual auxiliary完整段后/一个lossmask例子前两段。

拟段1：

同义输入的一致性也不一定要施加到整份表示：若某种风格变化应保留，却不应任意改变事实回答，可以先从配对变体的层表示估计并冻结一个候选变化子空间，再把 centered hidden states 投到其正交补空间，只在 context 的已对齐位置比较相对距离与方向。主 QA cross-entropy 仍监督答案，辅助 loss 尝试让不属于这份候选变化的表示更一致；子空间用于训练测量，不等于部署时删除所有风格方向。基座、变体生成器、层/module、basis/center、位置对齐、mask 和辅助权重应共同标识，不能仅凭“配对”或 SVD 宣布已找到了纯 nuisance factor。

拟段2：

补空间相近不证明语义解耦：被排除的方向仍可能含任务信息，改写也可能同时改变事实、长度或难度；context 位置的 loss mask 不隔离共享参数及后层传播。需要保义与独立答案对照、原能力和不同变体人口的回归检查。[必要方法与直接反侧](https://arxiv.org/html/2603.09205v1)只支持有限 QA 训练的辅助目标分支，attention feature 的可读相关不是情绪对准确率的唯一因果，平衡 label 数也不等于匹配全部混杂。部分 in-domain 与 neutral 切片仍退步，不采用普遍无害或完整解耦；basis 提取、合成变体、成对 forward/activation、投影、训练和独立校准均付费。对齐、候选子空间或质量—费用失配时，保留普通 verified CE、可信变体增强与分层 held-out 验收，不将 proxy 一致性当行为真值。<!-- source-family:SF-2026-ARXIV-2603-09205 -->

拟自身末注：2603.09205 exact-v1§3–7/A/D2/F，2+1+2=5具体auxiliaryobjective gap深入；仅采用固定候选补空间paired一致性接口，相关非因果/弱label/长度难度混杂、真实反退、token对齐/配方未闭合与完整费用保留。必要非作者Source/date/PRE/POST未授，不认证图精数、代码/复现或所有风格分离。
