# Jan06 生成、模型记忆与联邦更新必要证据

本记录为实际精确v1选段。已读完整题摘仍不自动变为证据完成；支持与关键反证足够即停。选段中的truncated=true仍非已读完整，本记录只采用已读位置的命题，必要尾段普通工作继续。根复核/Books锁尚未完成，不自授日级Gate。

## CDGS 2601.00126v1

实际§2/3/3.1/3.2、§4前7000字/原HTML Table1–2、完整§5/8/F3。新增为overlap local-mode composition下population pruning与迭代resampling，不是直接用LLM做机器人应用。2+2+2=6。Bethe/平均conditional marginal approximation不等真实全局joint；有限U不保证任意长依赖，low-level short-linear/local-feasibility假设不可提升完整任务正确性。

原§3.1 Eq5 g越大表示lowlikelihood，但J=product exp(-g)越小；Alg1选minJ/文字说lowquality highJ，与式方向相反。原HTML已重开，需唯一ranking score/排序方向及实际实现或勘误后才采用该pruning有效性，不借实验数字抹掉中心冲突。Table1 baseline借原论文、100trials/5seeds、Scene oracle horizon；Table2 50trials且PDDL/task-plan特权不同，ours仍低于GSC original，不宣称各表普遍更优。长视频只6prompts/CogVideoX2B/350frames，aesthetics退步；F3 L40s的0.5H秒不是任意端到端SLO，precision未披露。中心争议拟暂缓，重开仅score/config与受影响论证。

## NeoVerse 2601.00393v1

实际§3各bidirectional motion/Gaussian/sparsekey/degradation子段、§4 implementation/runtime/ablation、A/B必要实现与E限度。新增为dynamic reconstruction→sparsekey linear interpolation→monocular degradation simulation→frozen video model control branch的训练接口，拟2+2+2=6。并非从生成画面直接认定action-conditioned persistent state。

双向速度仅邻近短间隔近似线性；global max visible velocity分静/动态、动态只近邻aggregation以免drift。训练通过novel-camera visibility culling和平均depth边缘模拟，再render回原view取得paired原video target；synthetic degradation不能认证真实novel-view几何。32A800/150K+50Kiter，WanT2V14B；generation336x560/81frames，precision与seed未披露。A800 Table3 baseline49vs81frames、off-shelfdistillation不同，不把20s当纯bidirectional模块speedup；11keyframes部分quality低于fullframes，Table4ablation只DyCheck。Appendix E 2D cartoon缺3D线索与文字失败保留。Ch25 reconstruction与generative world branch具体差异待核，不为新paper新建owner。

## MBC 2601.00756v1

实际§3.2–3.6/4.2/4.3.1/4.4.1–4.4.4。拟2+1+2=5：文档encoder→VQ index bank+fixed trained codebook→queryaggregation→KVLoRA调制。标题online-reset在原文是TRAINING only，online适配仅forward编码/量化/追加bank，不反向更新码本或模型；不要虚构runtime可无损换codebook。EMA/STE/VQ和LoRA是借用原则，新命题是这个模型绑定存储/消费接口。

四backbone 82M/774M/1.5B/7B，1665test documents再同document QA；T5 encoder+512codebook、50epochs、单A10080GB，Llama2模型/amortizer4bit但其余precision未披露。Memory footprint包括码本/indices但不是完整系统内存、模型/encoder/workspace；CaMeLS7B不可fit不当公平quality胜者。retention相对最早200document基线，Distil绝对分低造成高保留，不是永久知识无损；无KVLoRA/VQ分开fullfactorial未作实测归因保证。Ch22的external residual/model-bound derivedstate与Ch77raw evidence边界需局部判断，不当Agent自然语言memory权限新机制。

## HFedMoE 2601.00583v1

实际III-C/D/E全部必要、IV setup、VA1–4/VC1–3。拟2+2+2=6：batch内backward expert-budget与partialexpert/router aggregation的联合更新语义。Forward保sample-level route，backward选择并mask其他gradient；不能由此证明forward峰值fits。D1 IB代理I与D2实际按s排名不同，不授信息最优。E2 r=|Sc∩union|/|union|只是覆盖比例，不度量成对routing一致；Eq20alpha未sum-normalize、Eq21只是加权sum，不能替原文偷偷写标准平均。

IV模型Switch-base-64与叙述395B、DeepSeekMoE16B/8rankQLoRA；server4090+4Jetson AGXXavier、模拟12–32GB上限、batch8/lr1e-4，precision/seeds未完整披露。主动上传usage>=tau不自动等于实际backward被训练expert，必须显式记录update participation；尚未核artifact，不当生产边缘可行性。Selective aggregation基本道理可成立，但完整performance/IB/normalizedrouter中心说明仍需精确config与weightnormalization/usage-vs-update规则；只取有限partial-update边界或暂缓需root校准。

root非作者已实际复核本文件具名中心决定性原段，受影响保证隔离终态通过；此记录不授全篇无错误/代码复现失败/性能普遍性，也不替代其余家族或日级Gate。

## 最终处置同步（2026-10-02，日级Gate待root）

当前最终处置：CDGS6中心score/sorting争议隔离；MBC5局部codec仅报告；NeoVerse6因具体training-interface缺口深入，Ch24 1169/首注1491 actual POST通过；HFed6因三参与集合接口缺口深入，Ch36 399/首注1745 actual POST通过。两Books锁已释放。HFed原公式/归一与性能未决不作为正面依据，仅工程要求采用。
