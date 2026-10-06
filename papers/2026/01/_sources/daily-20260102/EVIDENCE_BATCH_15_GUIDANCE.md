# Jan02 有限五项：缓存 / 内部引导 / 图像求解 / EoD调度 / reward方向

最新非作者终态：root实际必要精确原源、具体owner及四写后正文/邻接/末注通过；CorGi Ch24 1078/1080、IG Ch24 1169/1171、Tele Ch38 264、D2Align Ch31 799均整合，DiffThinker Ch24 typed parser/生成预算具体已有覆盖。末注与正式日报同步，不授全篇/实现/复现或日级完成。下文拟/待表达为写前过程提案，由本段终态覆盖。

五完整v1题摘root实际准入校准均2+2+2=6；作者标准必要core、评价和直接反侧已actual读取。独立Evidence/具体Books仍待root，不授全部附件、实现核验或复现。日期字段actual DATACITE_POTENTIAL：24195 created03:06:11Z、24176 03:05:44Z、24165 03:05:28Z、24157 03:05:16Z、24146 03:05:00Z；配共同holiday/noadvanceID，公开下界Jan1T01Z，上界各created+1秒，非registration精确公开。相关v2晚于本窗不作为本窗事件。当前原abs/event未见撤回/勘误信号；不遍历全版历史证明没有说明。

## [CorGi24195 exact-v1](https://arxiv.org/html/2512.24195v1)

Actual §3.1–3.4/Eq2–6、§4.1–4.3/Tables1–3。低贡献按相邻interval锚点的feature CKA估计，不是当前step真正删block的因果收益；每interval全算并refresh，按固定排序逐step增加缓存blocks，warmup=总步数20%仅作者选参。§3.2 L127–128明确整block output重用会抹掉前层当前更新，因此仅复用ATTN/FFN分支输出，residual仍消费当前input。CorGi+在warmup取每block cross-attention，top-c text与k=2 imagecluster形成token集合，只局部refresh ATTN，不是所有FFN都partial更新、不是每步重新推saliency。

必要原式（数学对象，不缓存全篇）：`score_i=1-CKA_i(X_i,Y_i)`；Eq6 `Zattn_i(t)=M_i*Ztilde_i(t)+(1-M_i)*Zhat_i`。原位置L140 interval全算、L148集合取warmup步、L172 ATTN-only。这些实现权限不从attention热图推广成真实语义重要性。

SD3.5Large/FLUX1dev/PixArtSigma，COCO2014验证10k prompts/1024²/guide3.5，H100实测端到端inference；precision、batch、concurrency、SLO未披露。Tables1/2并非全指标优于fullcompute：SD3.5 FID/Pick/IR有反退；FLUX不同CorGi+配置LPIPS/.12与另一.09也非单调。PixArt的+增益有限；增interval/γ/δ可毁对象细节（§4.3），原§4.2 L213“+higher speedup/lowerLPIPS”不能跨所有表照录。CKA/crossattn/kmeans/feature驻留与refresh应计成本，未跑代码。

具体owneractual Ch24 1068–1095已有trajectory误差/运动refresh/learnedcache与fullforward，但没有把“cache模块增量、current residual不缓存成旧整block”及block-specific集合与refresh分账。拟原6分具体gap深入受影响§3.2–3.4，最多一至两段接cache误差首段后；不新增结构，待root必要源/owner授锁。

## [Internal Guidance24176 exact-v1](https://arxiv.org/html/2512.24176v1)

Actual §3.2/Eq3–5、§4.1–4.3/Eq6–7、§5.1–5.2/Tables2–4及AppendixE必要训练设置。中间head与finalhead在同输入noise/t上监督相同clean/velocity对象，以较浅输出作为弱参照外推较深输出；不是任意现成checkpoint无需训练即可用。Eq4 `L=Lfinal+lambda*Linter`；Eq5 `Dw=Di+w*(Df-Di)`；Eq7 finaltarget `x0+omega*sg(Df-Di)`，该可选训练分支用EMA，不与推理IG混成一个结果。

§5.2 Table2越深auxhead/多head未越好，Table4 w/interval亦非单调；toy2D说明一种受限方向解释，不证明真实images的manifold因果或所有guidance不降diversity。LightningDiT改Muon与EMA.9995，不能把其整份跨方法FID差全归IG。ImageNet256/50k样本统一类抽样，SiT/DiT250stepEulerMaruyama、Lightning125stepHeun；AppendixE fp16、gradientclip/FlashAttention、大小模型分别作者写A6000pro96GB/409024GB，硬件名称照原披露不自改型号。加Linearhead/aux训练/准备latent仍有成本，samepass不等完全零费用或productionSLO。

Ch24 guidance当前持有外部condition/uncondition、可变scale和teacherfeature粒度，没有内部受训depth readout的弱参照/同forward共享及其相关误差。拟窄段放Conditional Guidance讨论后、Guidance前移Prior前；只承载受训中间输出作为参照、训练预算/强度失效与原CFG共存，root未授锁。

## [DiffThinker24165 exact-v1](https://arxiv.org/html/2512.24165v1)

Actual §3.1–3.3、§4.1–4.4、AppendixA.1必要设置及B/C直接限制。采用命题仅为视觉solutionimage→parser的受限solver替代，不是新FM损失或已证实内部parallelsearch。公式接口 `xsol=G(x,c); yparsed=Psi(xsol)`（L104–107）；§3.3 L152显式选择high structural parseability。五任务独立fine-tune；DiffThinker++用新版imageedit作主表，其他ablation是原DiffThinker，不能混成同checkpoint因果对照。

Table3 FM/SFT均5epochs但batch8/32、GRPO1epoch/batch128或64/group4，不是matched训练compute。8H200测训练/latency仅VSP特定population；precision与productionbatch/concurrency/SLO未披露。Euler20steps定预算，§4.3 step/data曲线、C Figure18/21/24实际失败说明不能授可靠解或任务难度不影响质量；projection中多线条不证明真实分支search/pruning。视频baselineWan5B与image20B且结构不同，不授图像范式因果优越。N图像+MLLM verifier还有候选及judge成本，非独立世界证据；当前case比较在作者选的DiffThinker成功population，不能推一般失败率。

具体ExistingCoverage提案：Ch24 739–746已有nativeimage provisional→typedparsercommit→taskevaluator与invalid/schema/codec条件；156有steps/NFE/真实cost分账、863有finalmedia gate。它们实际承载本次可保留的生成输出/可解析性/正确性分责，不声称含本篇gridrecipe或内部search论点；该局部solver实测留报告，不追加重复正文。待root必要源及这些具体位置核。

## [TeleChat24157 exact-v1](https://arxiv.org/html/2512.24157v1)

Actual §4.2 L247–254以及原§3.2/模型配置仅为设置身份。准入对象只EoD稀疏attention后的同total-length异document-composition cost：tokens在较长doc后部读取更多可见token，按subsequence长度redistribute microbatch以减少rank等待。不是EoD mask就自动使densebackend少FLOPs，具体执行须真正消费block/sparse可见性；文档长度cost不与PP layerpartition当同一控制量。

必要原位置L252 EoD阻断跨document、L253同packed长度异cost、L254 microbatch redistribute。§4.2无单独量化收益/消融表/特定NPU型号与该项precision或服务SLO，不能把报告整体nearlinear/MFU/10%PP收益归本调度。未跑代码，保留Attentionbackend、packed组成及每rank实际timing验证；重排不得改变全局训练人口、EoD语义或optimizer accumulation提交。

Ch38 244–264 stagebalance已有per-layerprofile/HAPMoE异构计划，189–195 readiness处理jitter，但未承载同shape样本因EoD内部长度分布而异cost、在样本分配而不是layerplacement消除等待。拟一窄段于stagebalance/profile后、HAPMoE前，明确稀疏backend条件、重排及统计开销/fullsemanticbatch不变。若profile无差/重排费用高回固定按token分配。待root必要源/owner锁。

## [D2Align24146 exact-v1](https://arxiv.org/html/2512.24146v1)

Actual §3.2/§4.2/Eq4–10、§4.3、§5/Tables1–2、B.1–B.2、D.1–D.2。Stage1冻结FLUXgenerator，用生成样本优化单directionvector；归一化text±b再以ω外推，用同frozenCLIP型HPS评分器。Stage2冻结b再更新generator；这改变rewardinstrument，不证明已识别唯一人类偏好偏差。

必要原式 `e±=normalize(etext±bv)`；`etilde=e−+omega*(e+−e−)`；`Rguided=cos(eimg,etilde)`；Stage1/2均最大化此reward但参数权限分别b/θ。One-stepknownnoise重建提供训练期reward对象，不等online最终sample精确真值。Table1原始HPS高分可与heldoutquality低分并存，但ours非每metric最好；Table2特定DivGen四人口切片对比不授任意无条件modecoverage或prompt跟随保证。

B.2 stage1 3000steps+stage2 20，baselineDance/Flow300及SRPO20；bf16/720²/AdamW5e-6/batch1/accum2，sampling/inference25/50原字段分开，hardware与productionSLO未披露。不能用20步骤称总训练比300便宜。D.1 100prompts/同seed/20盲评人四维偏好，D.2 80template sets/20人看requesteddiversity；不把该调查当独立代表全人群偏好，未披露不确定性不补造。

Books待定：Ch31 795已承载policy-tilted评价人口、861迭代proxy自强化与independent evaluation；拟采用的非保证边界可具体ExistingCoverage，但不声称已包含方向vector算法。若root判断“固定generator学评分条件、再固定条件学generator”的参数权限需长期承载，则仅窄补该受限分工及额外阶段成本，先核具体gap，不按主题自动关闭或写入。
