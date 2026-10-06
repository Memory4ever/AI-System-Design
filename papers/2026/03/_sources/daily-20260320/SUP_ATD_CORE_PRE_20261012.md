# ATD2603.17912：本20最小必要Source与有限PRE准备

准备者resume_review17_18，root唯一指派，仅03-20补03-19自然日，原2+1+2=5/date复用本日独核§35。不是自身Source/PRE PASS/安全终态或DAY，未写Books/Report/LS；交resume_mar17非准备者裁有限分采或具体中心暂缓。

## 1. 精确原证与实际停止

[Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages exact-v1](https://arxiv.org/html/2603.17912v1)。actual当前[abs](https://arxiv.org/abs/2603.17912)L8–27同题四作者/完整AB，单v1无具名修订/withdrawal；Submitted03/18不当firstpublic，既有date夹证不重开。

实际必要HTML读取：完整AB47–51，§2.1 L72–80、§2.5–2.7 L116–154、§3 L155–169直接反侧；Appendix A.1–A.2 L216–242决定性公式、B.1 L261–264/B翻译prompt与B.2 L367–380/B.3 L423–515质量筛选，E.1–E.2 L585–617训练/evaluator/对照条件。源open最初返回语言谱系§2.2–2.4亦有实际读，但不把该领域叙事当项目准入或独立机制证据；未逐个全部语言附表、图像像素、其他模型完整结果、代码/复现/版本diff，不扩query。支持和直接反侧已足止。

## 2. 可分采的共同支集与训练接口

跨语言输出token数量不同，直接比较两张attention矩阵没有统一轴。A.1–A.2以同一English句子的固定source token支集为参考：每层/head的target-query→source-key矩阵，沿生成target token平均，再在source支集归一化；heads平均形成每层分布，在这个共同source位置轴上比较运输代价，最后按句子/层聚合。有限增量是**如何把异长目标序列的路由统计投影到一个共同比较支集**，不是target分词完全不影响attention、语言真距离或所有head功能保持。

训练E是另一协议而不是直接照搬A所印exact1D公式：M2M-1001.2B对同English输入预计算并cache reference-language crossattention，target attention随fine-tuning动态生成，使用GeomLoss debiased Sinkhorn divergence/blur.05作辅助loss，CE翻译目标继续存在；uniform layer weighting，λ按CE与auxloss的目标比例动态缩放。Pashto–Farsi比例10:1，Marathi–Hindi/Icelandic–Norwegian1:1。此处借reference路由形成条件训练目标，reference翻译和attention都不拥有真实词对齐或target答案正确性。

比较支集/归一化/模型checkpoint、reference生成与cache身份和消费者loss要绑定；源token索引只表达给定英文tokenizer的顺序，非语义ground cost。Cached参考不是免去准备工作，reference/population失配会施加不合适的归纳偏置。推理最终仍是翻译生成，不纳为在线路由加速/删除head或自动选reference的已实现工程方案。

## 3. 关键评价、反侧与数学强桥隔离

- A/B测量WMT14 English3003句生成99目标语；M2M按GPT-4o yes/almost/no映射1/.5/0挑每语top2000，平均质量阈值0.2保81语；Llama逐语top500/平均阈值0.6保55语。阈值真实已披露，不说没有筛选协议；共同sentence intersection/同m精确配对仍未明确。判分模型/模板与生成质量影响人口，不能用所得距离独立证明语言家族/预训练不偏；逐语top样本若不同须先对齐同m，不擅补原实现已有guard。
- §2.5明承低资源/文字体系与model training影响异常，树拓扑也可能与raw pairwise距离不同；§2.6 Japanese同/异语序p=.946不显著、SVO两组有条件差，不支持普适语序因果。§3明确非历史/地理因果，仍受模型/语料偏差；项目不用family图/热点推语言能力或训练安全。
- E训练最多50k ps/is、mr27007、test2k，20ksteps/AdamW3e-5/B32/warmup.1，单A10080GB，每1k评、三seed均值/标准差。BLEU/chrF/TER/COMET各权限不同，最终quality仍需独立test。主要收益仅作者文述曲线，未读图像像素或取得完整数字/CI；不授每checkpoint/每语言严格改善。
- E.2 distant es/ar reference也通常改善，reference细差受λ掩盖；不能把全部auxloss收益唯一归因语言亲缘。λ过大可干扰CE，related reference不构成安全保证。Reference翻译/attention extraction/cache、head/layer统计、运输loss、三seed/全部训练和每步evaluation均付费；precision、完整准备/训练墙钟、peak memory及batch/concurrency/SLO Not Disclosed。主文“no additional tuning”不能抹掉每pair不同目标比例/动态λ；三对demo不授普遍迁移或最佳recipe。
- **1D计算强桥：** A.2 L241把W2写为CDF的L2差，而标准1D W2对应quantile函数L2差。自构同支集位置0/1/2、P=δ0,Q=δ2，则Eq6最优运输唯一代价4、W2=2；CDF difference在两个单位interval为1，L2范数√2。因此所印CDF快捷式不等Eq6，不照录精确ATD矩阵计算保证；不能由此断言GeomLoss E训练实际错误。
- **tokenization与identity强桥：** 将target attention rows (1,0),(0,1)平均得到(.5,.5)；同样内容若某目标token被重复split两次且相应rows重复成(1,0),(1,0),(0,1)，source分布变(2/3,1/3)。输出轴消去只保证共同维度，未证明分词/序列重复不变。不同languages/head patterns也可有同均值分布，Eq5即0；距离是这项路由统计的metric/语言映射的pseudometric，不授语言身份可辨或全部attention功能保持。

**一次精确请求：** 若要采用tokenization invariant/exactW2/语言metric或完整可复现测量recipe，需提供与Eq6一致的quantile/OT实现、生成token重分段检验、每语言质量筛选后的共同English句子对齐及零距等价对象；与E实际Sinkhorn训练实现分开核。当前仅拟分采共同source支集上的路由比较与cached reference辅助训练接口，不采用上述数学/语言强桥；原5不降、未由准备者授终态。

## 4. actual唯一owner、差额与逐字PRE

sole `MODEL-SELF-ATTENTION`/[Ch14](../../../../../books/part-02-model/14-self-attention.md)。actual开篇1–50确认Q/K/V读取职责、235–278完整probe/边级因果→训练目标→样本支持→归一化/prior邻接和本人末注已读；Ch13/15开篇定位序列坐标与多head组合，Ch33不另复制该模型路由目标。现训练段253–260承载初始化/gradient blindspot和受限召回样本，但未具体承载**异长跨语言路由归一到共同source轴后，以缓存referenceattention作为CE外辅助目标**差额；不是因为语言距离排行或泛泛OT原则写入。拟原260受限学习边界完整段后/归一化262前两段，不重排别族。

### 正文PRE 1

给Attention增加训练目标时，还要先解决比较对象的支集。跨语言生成的target序列长度不同，可在同一source句子的token轴上，把每层target对source的读取沿target位置平均并归一化，再比较这些共同支集上的分布；另一语言的reference读取可以预计算缓存，当前target读取则随训练更新，用运输型辅助loss与原翻译交叉熵共存。这个接口约束的是给定模型、输入和聚合协议下的路由统计，不是真实词对齐、语言亲缘或答案正确性。消去输出轴不等于消除target分词影响，head平均也不保全部读取功能。<!-- source-family:SF-2026-ARXIV-2603-17912 -->

### 正文PRE 2

[ATD的有限迁移演示](https://arxiv.org/html/2603.17912v1)只覆盖三组低资源翻译及所测reference和loss比例；较远reference也能改善，过强辅助约束又可干扰原任务，不能把收益唯一归因语言距离。训练中的熵正则化运输与离线距离协议须分账，原文CDF快捷式不直接授精确W2计算或分词不变保证。Reference生成、attention抽取/cache、运输loss、训练与多seed评价均付费，应共同绑定句子身份、tokenizer、层/head聚合和cache版本，再验最终翻译质量。参考失配、数据偏差或质量回归时，保留原CE、较窄辅助目标和独立对齐/行为评价，不由路由距离签发模型能力或生产SLO。

### 静态来源注PRE

- [ATD2603.17912 exact-v1](https://arxiv.org/html/2603.17912v1)：必要A.1–A.2/Eq2–6、B.1–B.3质量筛选、§2.5–2.7/§3和E.1–E.2。只采共同source支集路由比较与缓存reference辅助训练分责，保CDF/W2、tokenization/zero-distance强桥隔离、质量筛选/语料偏差、reference/λ混杂及全部费用；不授语言因果、精确recipe或生产SLO。未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2603-17912 -->

## 5. 非准备者裁待执行

请resume_mar17独核上述必要原证/三具体反侧、actual sole owner及两literal/static，可裁有限分采或中心终态；不凭一般OT或语言谱系映射owner通过。未root新锁不写，未一次非writer实际POST不计I，无DAY。

## 6. resume_mar17 非准备者有限Source/owner/PRE

2026-10-12实际必要exact-v1 A.1–A.2 L216–242/Eq2–6、B.1 L261–264/B.2 L367–380/B.3 L423–509、§2.5–2.7及§3有关模型/语言因果边界、E.1–E.2 L585–617独读；不遍语言附表/谱系图像/代码或版本史。独算δ0→δ2唯一transport平方代价4，W2=2而CDF差L2=√2；target rows均值(.5,.5)重复split一行变(2/3,1/3)，同均值的不同routes又可零距，三个强桥均不采。原两literal/static有限Source/PRE PASS，原5不变。

实际Ch14完整235–278训练目标/受限召回→归一化/prior及Ch13/15入口读回，共同source支集的异长target读取比较与cached-reference auxiliary-CE接口是具体差额。E实际GeomLoss Sinkhorn与离线所印CDF不合并；动态λ/三个pair、远reference仍改善和过大λ干扰CE、不同人口质量筛选与全部准备/训练评价费用准确保留。原PRE不依赖tokenization invariant/语言身份metric或正确性保证，可以有限分采；root授窄锁后写，一次非writer actualPOST前不计I/DAY。

## 7. resume_review17_18 root sole授权后的实际writer

2026-10-12 root接纳CC一次POST并澄清跨文件输出误认重复（当前Ch23来源注唯一1804，未删除有效内容）后，授本family sole Ch14两literal/static窄锁。实际写前235–282完整边级诊断→训练支持→归一化/prior和末注已读，在SF2603-15923完整段后仅加入原两literal，实际262/264、静态本人659。写后实际250–282和末8行顺读回对原PRE一致，CDF/W2、分词/零距强桥隔离、reference/λ及全費边界保持，没有改相邻family。限定diffcheck0；当前整章numstat16/0包含既有Phasor等修改，本family仅两段+静态注六新增行，不把总diff当自身独占成果。Writer不是POST，交resume_mar17一次完整250–282及651–659本人/邻注实际POST；未接纳不计I/DAY，不改动态身份收据。

## 8. resume_mar17 一次nonwriter actualPOST

2026-10-12实际Ch14完整250–282/new262264及651–659本人/召回/Phasor邻注顺读，逐字回有效两literal/static与已独核原证。训练支持→共同source读取/cached-reference→归一化交接完整，三个强桥隔离、reference/λ人口与全部费用近文，正文marker及静态注各唯一一份；限定diffcheck0。有限actualPOST PASS，不重核心、不改Books身份注，不授本日DAY。
