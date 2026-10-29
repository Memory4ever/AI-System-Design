# Oct13首包三个最低决定原域

root本日SUP_INDEPENDENT_20261014§3已actual全部下述必要节点/完整Tables1–4等读取通过，minimum2P1C与FIRST合5P1C。以下作者提案/待核文字只保当时读域，最低门不再普通；必要费用/消费者/预算反侧保持，不授日门/评分/Books。

作者Kierkegaard；只本日FIRST三N，精确v1原HTML均200/exit0；实际读以下节点，不把已下载全body作全稿或完整Evidence。日期/score/Books未授，root尚未actual这些minimum。已读摘要六份不重复展开。

## ZeroGR10419：N→窄P提案

[v1原件](SUP_CORE_2510.10419_20261014.raw)338752bytes。实际完整§4.1–4.3/公式1–6与§6.3–6.6最低比较说明：docid generator把异质文档映射6–8词短句，query generator以task instruction生成B个queries，逐新corpus训练docid生成器作为index；不是无需新corpus索引训练的全球zero-shot模型。自然docid仍可能冲突，§6.3明确冲突率而非严格唯一保证。

关键新消费者规则不是仅温度术语：§4.3为valid-docid prefix trie约束的无放回生成，生成一个完整leaf后从trie移除；温度g(i)按**第i个docid/排行次序**归一sigmoid升高，token位置j沿该docid使用同t_i，不是每token逐步升温。early precision/later recall是rank消费者选择，不等于全部token/所有排名质量一起提高；短句docid碰撞时leaf与document不是一一绑定，未授任意corpus严格bijection/exact排序。

§6.6原文同top100 docids比较greedy无放回、top-p .9、beam；greedy最好Acc@1但低recall，nucleus相反。该明确early-vs-set retrieval消费者反侧足以保窄P，不单借SOTA或新模型名字。没有读Figure6像素/数值及Alg1完整实现，不采用所有长度/beam预算严格匹配或性能数字；自然docid/task多样性/新corpus训练全费不被“zero-shot”省掉。§6.3正文69tasks/图注60tasks文字差额保持，不修为一口径。未证明trie leaf去重解决docid语义冲突或全一般理论。

## BitMar10560：N→窄P提案

[v1原件](SUP_CORE_2510.10560_20261014.raw)132561bytes。实际完整§3/4/5与Tables1–4。3.2 frozen DiNOv2 768D features是**offline预制**，2×2 pooling＋768→128 MLP压缩；不是在线全vision backbone1.58bit。文本/投影ternary learned scales、activations8bit，softmax/residual/LN/logits FP32分责，不能宣整个pipeline单一bitwidth或已核device native kernel。

3.3标准crossattention textQ/visionKV，3.4 memory M(K512,C128) soft outer-product写入α .2、content-softmax读向量，稳定性penalty和usage forgetting、每层concat或residual注入；这些成熟组件本身不准入。§3.4 controller是alignment EMA跌>.12后随机freeze encoder或upweightcrossmodal，§4.3却说memory freezing，方向不替作者选择；caption768D共享空间与主文128D、max256与sink/window4/1020接口也不代补完整recipe。存储slot激活图不能证认知/长期因果。

窄P来自具体消费者反侧：Table4 memory-on的entity/property与VQA增，EWoK Split1/Winoground各-1.6、DevBench无效；§5.2 finetuned七NLP heads无显著变化，psycholinguistic reading alignment0.44/0.11反而低于memory-off1.11/.66。**固定retrieved向量改变generative/特定readout而非统一所有supervised head提升**，可修正多模态memory资格，不因14M/edge/局部基准关。Table1与Table2 BoolQ有不同评价设置，42.83与66.5不拼接。Table3 memory-on/off 57.3/7.7tok/s、RAM956/1076等只作者局部数；mem-on替代long-rangeattention、precompute/capture/SDoffload/设备工作负载未完整匹配，不采用7.5x/79%energy或全memory省费。S4仅训练A6000，不补生产edge设备/同质量SLO。

## RECON10448：N→具体C提案，测量反侧保留

[v1原件](SUP_CORE_2510.10448_20261014.raw)205314bytes。实际完整§3.1–3.3/4.1–4.2/Limitations、AppC Algo1/PPO及AppE完整Table3。真实流程是MSMARCO query/passages相关分类SFT→discardhead、GPT4omini六aspect summary teacher-forcing→SearchR1每search后摘要插入information、普通PPO/检索tokenlossmask。不是只有名字/缺代码：明确存在multi-turn rollout；但原新增仍成熟摘要/相关性预训/teacher distill接现流程，未呈新的执行/验证规则或受控可迁移条件，故具体贡献C提案，不以Books覆盖、费用、实验少关闭。

保留真实反侧但不把所有baseline confound自动当新设计贡献：3.3相对SearchR1同时documents/turn3→5和maxturn3→5，4.1称fair comparison并不等完整相同信息预算；Table1 PopQA两backbone均退（3B .435→.425、7B .457→.454）与“acrossdatasets consistently”文字不齐。AppE同officialcheckpoint报告context948.3→619.7、wallclock28.8→19.9、turns2.13→1.84，是该系统配置运行口径，不能仅归因summary算子或无额外预算。训练13.9vs14.7小时/4H200/500steps不包含summarizer两stage及468K/1.0M teacher资料的完整制备费。原限domain/teacher错误传递保留；未采用clarity=factuality/faithful保证，未执行代码或复现所有pipeline。

作者minimum提案2P1C；加FIRST原3P，当前首六拟5P1C，**仍待root实际准入/必要门核**，不是formal6或分数。具体相异判定只回原受影响节点，不重三全稿/六题摘。ADMIT必要安全仍普通；其他source/current/日门与有界标题差额继续，不因已抓raw建立全文quota。
