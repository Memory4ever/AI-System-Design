# BrainMisalign necessary Source / owner修正与PRE

作者supp_mar26_fresh；2603.23091v1，03-25日期与2+1+3=6准入有效，保原分。不由脑数据入口自动Science EX；审阅对象是语言模型表示功能干预，不采用脑机/临床应用。

实际[exact-v1](https://arxiv.org/html/2603.23091v1) §3.1–3.4/§4.1–4.3/F2–6/§5、必要A291–293的probe身份、B390–393/C394–397读完；D398–399/462–481只必要图caption轻核最强BERT/HP控制支持，不声称独审所有D–I participant图或重现。目标brainhead以negative squaredPearson配gradient reversal，LM head仍CE；preserving control只打乱fMRI与stimulus对应，brain-tuned另去GRL且把平方corr换corr，不能把tuned同misaligned当只一项变化。LoRA五epoch/B16/AdamW/ωlm.1/ωba10，BERTbase/GPTsmall/Llama3.2-1B；HP8人1211TR/人、Moth6人4028TR且只reading。最后block的linear ridge读出/4fold+nestedridge/current+previous5TR平均tokenstate，与trained adversarialhead/initialtokenembedding不是同对象。

采用仅是“成对干预+permuted控制+独立读出/任务评价”资格；不采brainalignment全模型普适必要、安全/可信推论或braintrue机制。§3.3.4 134把相似LMperformance写Wilcoxon p<.05，与§4.1 179无significantdifference口径相冲；两者都不是预先定义margin的equivalence检验。四连续sections和overlap5TR还需保存边界状态，selection只纳入满足作者match条件者；作者模型data约束与真实globalfunction分开。§3.4 Holmes是200+分类probe、6seeds只是probeinit/ordering，不是6foundation模型训练replicates/端到端任务或safety测试。GPT2HP p=.055、GPT2Moth不一致；aggregate各语言subfield虽trend正也不显著，tunedvs原pretrain仍有反退。不否定局部干预效应，但co-removal/sharedsemanticgradient/优化预算及选择偏差未完全隔离，不能把adversary损失低等同所有brain-relatedinfo不存在或一种性质是唯一因果根源。硬件/precision/lr/rank、总费/部署concurrency/SLO Not Disclosed；额外fMRI/readout/LoRA/probe及独立任务验收均计费，未核代码/复现。

## actual owner修正提案

初筛暂归MODEL-EMBEDDING Ch12；本次actual完整Ch12 96–149显示其explicit scope仅初始输入表示与训练接口，明确tokenembedding≠hiddenrepresentation。本方法干预LoRA后的整模型contextualstates及外读出，不修改词表lookup；把它硬写Ch12会越owner。拟唯一owner改WORLDVIEW-REPRESENTATION Ch5（分数不变），actual完整14–76的分布式特征→probe可读≠实际使用→rulemixture干预→好表示路径与Ch4/6开篇已读。原controlledrule输入steering不承载“训练时对指定读出能力施加反向压力并配permutedlabel控制、保持LMloss也须另验”等资格差额。需reader独校这一owner修正，不自行新增结构。

拟2602.23164完整规则混合段之后/“什么叫‘好的表示’”标题之前原两PRE，保旧段。尚无锁/未写。

## PRE paragraph 1

当待研究的性质没有清楚的输入反事实时，还可以在训练中对一项指定的读出能力施加反向压力，而不把表示相关性直接当功能必要性。一个受限语言模型实验同时保留语言建模目标、训练辅助预测 head，并将该 head 的梯度反向送入适配参数；配对控制保持流程却打乱辅助信号与文本的对应，再以独立训练的读出和下游 probes 比较。它让“去掉某项可读性质之后还剩什么能力”变成可检查的干预问题，但对有限 head 不可读不等于信息已全部删除，适配引起的共同变化也不自动证明被研究性质是唯一因果来源。<!-- source-family:SF-2026-ARXIV-2603-23091 -->

## PRE paragraph 2

[必要方法与反侧](https://arxiv.org/html/2603.23091v1#S3)采用的语言建模匹配口径尚不闭合：相似性检验的显著性写法与结果的无显著差异不同，二者都不提供预先声明容忍区间的等价保证。局部模型与数据组合存在不一致，分类 probe 的多次初始化也不能当完整模型的独立训练重复或实际任务成功；因此只保干预设计与受限观察，不外推某项外部对齐是普适能力、安全或可信度的必要条件。额外适配、辅助信号、readout拟合、probe与反复匹配均付费；应分别保存干预目标、读出类、控制身份和独立任务结果，匹配或归因不足时保留原模型、常规probe与更窄受控实验，而不凭低辅助可读性签发性质删除证明。

## 自身静态证据注 PRE

SF-2026-ARXIV-2603-23091 — [BrainMisalign exact-v1](https://arxiv.org/html/2603.23091v1)，必要§3–5/F2–6及A的probe/B–C读出/必要D caption；仅采用指定读出能力的反向适配＋permuted控制资格，保LM匹配统计口径、有限head非全信息删除/非唯一因果、模型数据反侧与全费用；不采脑对齐普适必要、安全或临床结论，未核实现/复现。
