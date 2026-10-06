# WMReward / LAMaS / multilingual metrics — 必要证据待root核

三项normalSubmitted/正常公告条件及registered上界完全落窗，原字段见本目录date JSON。官方exact-v1缓存按ID；未核artifact/复现，不把submitted作公开。

纠偏后终态：root已实际终裁10553中心sign争议6分NoBooks、10580标准5分OnlyReport；必要证据保留。10560仍普通Books/独立终裁，不由下文旧gap提议自动写书。10580不再将recipe未写视作confirmed长期差额。

## 10553 WMReward — 拟2+2+2=6，中心sign争议安全终态NoBooks

实际v1 §2.2–2.4 L122–182：冻结generator，滑窗context-only VJEPA predictor与wholewindow future encoder比较，Eq6写`r=mean(1-cos)`，正文却称closer future得到higher reward；Eq2/9/10又写正exp(lambda*r)、正梯度和argmax。三处中心方向与“减少surprise”相反。有限定点恢复A2 L1398–1414明确Eq12/13是**负**omega_s*gradient(r)，Table8L1333–1398 guidance scale均正，不可把一般tilt/BoN与实际guidance视作同一已核reward方向。未自行修成cos、负r或argmin，不作完整proof/附件恢复。

实际§3.1 L186–188 PhysicsIQ5s/16particles，§3.2 L496–500 VideoPhy344/8particles/VLM per-axis>4并承认semanticadherence下降；Table4 L610–648 vLDM1H200/MAGI24B8H200，base106.77s/265.66s，guidance约5.02×/4.96×和4.27×/2.07×memory，BoN约N时间成本、并发与perGPUbudget不可混成free。A1Table8 DDIM50/rectifiedflow16或32步，FPS/分辨率/trim不同，不造同workloadE2E。B L1419–1422 fiveannotators/随机左右/neutral分母分开，人偏好非physicsgroundtruth；D L1431–1432明确VJEPA surprise混perceptual因素、突然状态变化/复杂mirror/siphon失效。precision/完整servingbudget/seed ND。

中心方向冲突不由局部evaluator收益修复。可保留作者局部physics/semantics/费用事实，不采用统一reward-tilt/BoN/guidance配方或physicaltruth。拟6中心争议NoBooks安全终态，重开需author明确Eq6方向、Eq2/9/10和12/13的同一sign convention、实际selection实现；不改4分/删candidate/外部Blocked，不无限版本diff。当前Ch24 sampling与Ch25 learneddynamics边界不补写作者缺失约定。

## 10560 LAMaS — 拟2+2+2=6，critical-path credit具体gap深入，拟Ch82两段

实际§3.1–3.7 L126–200：MaAS复用operator但把refinement从same-layer输入改为previous-layer，层内才可并行；不是保持完全同语义的调度重排。Latency=sum(layermax)，cost=sum(alloperators)；给每层argmax proxy operator完整latencypenalty，其他operator只task/cost，EMA rewardnormalize。该policy-gradient是局部信用设计，未证明无偏梯度/真实所有bottleneck，也未覆盖tie/共享resource/contention。Topology选择仍proposal，EarlyExit不替真实runtime/toolgate。

实际4.1L201–226/4.2L328–350、Table2L226–258与4.3/Table5L380–406：HumanEval/GSM8K/MATH，GPT4o-mini-0718 API T1，L4/K4/threshold.3/costlambda3，latencylambda.005但除50，toolγ50virtualtokens/s。CP_len用outputtokens+toolseconds*γ层max，不是实测wallclock或SLO；queue/network/rate limits故意排除。Table2HumanEval pass93→92.11有反退，不能“全部无损”。w/o latency同并行结构支持非仅parallel化；w/oCPcredit单HumanEval92.11→91.60/CP1042.7→1197.5局部对照，不证明latencycausal/一般最优。splits沿MaAS未在本篇详细列、seed/重复数/precision/hardware/训练全费/CI ND，APIcost只有测试调用不是lifecycle成本。Lim424–426明确system/runtime因素未纳入。

实际 `AGENT-MULTI-AGENT` Ch82 L177–196承载DAG预算proposal/随机成本/运行时fanout，但不含训练时cost与layermax latency分离后只把latency惩罚给criticaloperator。拟这里在拓扑策略段后两短段：先改真实依赖再学CPcredit，proxy/语义变更/quality成本反侧近正文，realaccounting/固定worker或singleagent退路。需要root原源/owner核及窄锁，非借成熟criticalpath给高分。

## 10580 multilingual intrinsic metrics — 2+1+2=5，标准必要证据完成，拟仅报告

实际§3–5 L142–298：NLL/PPL/BPC/BPEC/IP/MRR的单位与population不同；multi-parallel维持semantic内容不使surface概率同一，固定tokenizer/model只保证同一接口。EN同句与4humanDEreferences比较：全部DE值在EN同一侧才定义sample-rank一致，原splits均值与rowwise按分数sort的splits另列，后者人为极端重组不是自然部署分布/独立新population。Eq7“universal distribution”只是讨论性假设，不采所有语言共享分布/metric无效定理；论文L297称PPL线性变换与Eq3exp不同，不采用这一错误措辞。

实际§6 L298–325/Table2/3、§7/limitsL386–452：originalDE四split平均ranking一致，row-sorted extreme splits不一致，提供**取参考表述能改跨语言难易排序**的局部反侧，不证明任何模型/所有指标必反转。语言form/模型配置混杂不得解释语言本身难度；同test/segmentation model-to-model旧比较仍合理，共享char单位可改善跨tokenizer比较，但不直接跨语言construct。tinyLlama-style143Mmono/279Mmulti，32k/150kvocab，EuroParl21/UNPC6，平行lines而非同token预算；B/Table6 L750–814 BF16/FP32grad/3epoch/AdamW LR3e−4等，H100总mono≈50h/multi12+18h加alignment/tokenizer，seed/CI/end-to-endserving ND。泛语/大model外推未证、generationquality不在本研究。

纠偏后具体准入：原判断“平行语义消除信息量差，跨语intrinsic值可代表语言难易”→实际EN及四DE同义reference中原split均值一致、按metric row-wise极端重组后排序可反转→不能把语言难易排序当reference-independent construct，应绑定单位/population/reference并做敏感性。mono原DE NLL6.43–6.64、EN6.91，sortedDE5.89–7.23；是可核局部反例，非所有模型/自然人口排序必反转。已实际核§3–7单位/分布、Eq7讨论性假设、Table2/3原split与extreme条件及作者允许合法同分布模型比较。

`PLATFORM-EVALUATION-SYSTEM` Ch66翻译semanticcompiler/语言scores不能互换承载上位取舍，但未写本次reference实验不等长期gap；也不冒Existing已承载精确实验。标准证据收窄为已知metric对form/reference敏感的局部反侧，无普遍metric无效或新的可验证semantic measurement机制。拟OnlyReport，保留候选/必要证据而非为减工作量删项；root校准支持此受限终裁，必要范围终裁待确认，不申请Books锁。
