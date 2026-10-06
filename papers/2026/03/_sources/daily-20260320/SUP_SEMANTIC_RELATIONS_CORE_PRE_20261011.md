# SemanticRelations17624：受限probe证据/owner差额与PRE

resume_mar17，2026-10-11，只本20补03/19。2+1+2=5与完整AB/日字段及出版方May2026无窗前字段已非作者独核§12；不复日期。原证 https://arxiv.org/html/2603.17624v1 ，当前轻量说明未见具体重要纠错，复用批4。本packet准备未独核/未写/无POST。

## 必要Source范围与直接边界

实际v1 §3.1–3.4 L108–162/EqLD、FR、DR，§4.1–4.3/T2–6 L165–238，§5/7 L239–253。足以支持所采probe接口与直接反側，停止，不开repo/字典全表/旧版本/全部文献，不以未见图像精确坐标作定量拟合。

- Three dense base decoder models：Pythia70M(6layers)、GPT2 124M(12)、Llama3.1 8B(32)。WordNet3.0每四relation1000pairs+random1000；去重/lemma-disjoint80:20，再3neutraltemplate＝15000instance。不是三架构完全控制的capacity scaling或instruction/MoE/跨语言结论。Groundtruth英语词库偏差保留。
- 对attention/MLP/postresidual meanpool后multinomiallinearprobe，train-onlyzscore、heldouttest，bootstrapwithinclass CI；T2 postresidual总体更可读而MLP非唯一owner，peaklayer广CI/不稳定不是uniquerelationlayer。
- SAE列按probe coefficient magnitude选topk。§3.4说validation选k，§4.3.1又写training90%reference327选，精确selectionrecipe不采用。L210作者声明keep-only/remove-only的绝对logit改变量相同，但这不是一般线性代数结论：w=(1,1)、x=(1,3)、S={1}时原logit4、keep1、remove3，绝对改变量为3与1。该等同声明及所需条件隔离，不据此授model生成等义；原PRE只采probe空间分验。
- LDsem目标probe logit减max非目标semanticlogit、排randomclass；FR也是只semantic类的probe flip，DR是原probe gold→nongold。Injection/ablation只改变probe所消费表示，不到nexttoken或完整decodedoutput；§3.4L162与§7明确限制。大probe shift不是模型因果使用该关系或安全编辑证明。
- T4/5 Llama topk effects较强、同k随机5seed控制较小支持probe feature specificity；Hyper DR .35 vsHypo .41，不能称“零可抑制/全冗余”或证明唯一机制；smallmodel弱/不稳保留。不同容量/SAE/runtime没有完全matching，不授scale因果。
- reversalT3原表Rand Pythia-.03/GPT2-.04；L201正文实际写Δ<0.5，没有百分号，不能改写为<.5%或据此称表值违反该字面界。尺度/方向口径保留，不采精确drop结论。Table1 dog→animal称Hyper、§4.2.2 animal→dog又称Hyper，精确方向命名未闭合，不采用其directional accuracy数字/排序为定律。有限可采关系分开验收，不从symmetriccosine推出有向正确。
- T6新template mean.72→.47，none.55，peak新.92/none.74；作者“promptmostlyinvariant/只是readoutcalibration”解释不是已控制唯一因果。不同population/readout/intervention强弱须绑定，不能把peak保留当上下文稳定保证。
- §7承认probe关联/patch非线性交互夸大、onlybase密集/英语词库。硬件/precision/token长度/完整dictrevision、重复训练seed、全部SAE训练+probe+bootstrap+patch wallclock/token费用 Not Disclosed，不能授practicalediting效率。未核artifact或复现。

## 实际soleowner

实际Ch12 88–130初始/上下文表示与cosine边界、Ch16 240–285完整知识库/关系几何段及Reviewnotes、Ch15/17intro。Ch16 258已有“读出≠因果使用”，264直接editrecall≠多跳。未承载“关系标签readout空间的patch定义、其necessity/sufficiency不能继承nexttoken行为、relation-specific联合验收”的具体差额。仅sole `MODEL-FFN` Ch16 261总结后/现weightedit段前一段，不把postresidual证据称soleMLP或反映embeddinglookup修改；非主题NC。

## 原单段逐字PRE（待独立裁）

语义关系的干预还要注明被改变的是哪一个读出对象。一个稀疏特征子集可以提高线性probe对某关系的margin，移除同一子集也可以使probe改判；这只是在固定probe空间定义的sufficiency/necessity，不等于后续网络会因果使用它、更不认证next-token或完整生成的关系正确。[有限WordNet对照](https://arxiv.org/html/2603.17624v1#S3.SS4)同时比较Attention、MLP和完整post-residual，并显示关系种类、模型及提示改变时的读出与干预效果不同；不能由近邻cosine、某个peaklayer或“高sufficiency”把关系当作单一可编辑槽位。采用时应分别冻结有向关系标签、template、probe/SAE revision与干预位置，另验原模型输出、无关关系和上下文回归；这是工程验收要求，不冒称原论文已验证生成编辑。特征选择、字典训练与重复干预都付费，probe shift不稳、标签方向或selection口径未闭合时，保留原checkpoint与外部关系证据，不从probe成功提交权重变更。<!-- source-family:SF-2026-ARXIV-2603-17624 -->

静态本人注拟文：`SF-2026-ARXIV-2603-17624` — Daily `2026-03-20`；[SemanticRelations exact-v1](https://arxiv.org/html/2603.17624v1) §3.1–3.4/EqLD、FR、DR、§4.1–4.3/T2–6与§5/7。只采probe干预对象及relation/template联合验收边界，不采方向表口径、冗余唯一解释或next-token编辑保证；base dense/WordNet/SAE选择与成本限制保留。未核代码或复现实验。

## 实际窄写/作者读回

reader必要Source/actualowner/原PRE有限PASS已持久独核§15；两notes修正最终定点准确。root授本family Ch16唯一一段+静态注，作者逐字写新263与本人362；完整248–277与354–362本人/STEM邻注顺读，probe对象→生成另验→weight-edit直接/组合回归交接准确，保持其他正文/注，限定diffcheck0。一次nonwriter actualPOST待reader，不计safe或DAY，不在Book复制流程身份。
