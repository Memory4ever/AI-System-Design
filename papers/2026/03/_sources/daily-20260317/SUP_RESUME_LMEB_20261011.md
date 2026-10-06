# LMEB12572：必要原证与具体已有覆盖提案

仅本17新增03/16；完整AB准入/日级夹证与定点同稿核有效复用，不新增发现。resume_mar17实际打开[exact-v1](https://arxiv.org/html/2603.12572v1)的§2.3/2.4、§3.2/Tables2–3、§4–5、A.2/LongMemEval必要位置；不是借旧done或作者note。拟2+1+2=5，标准审阅；evaluation边界对照必要深入，不授artifact/复现。

原证：IR query/corpus/qrel及可选每query候选池；显式query-time anchor、turn/session粒度及时间元数据。22英语数据集/193任务，15embedding模型；binary qrels、capped Recall，输入1024或512token，与完整记忆消费不同。两instruction设置存在反向；§5 mixedinstruction选择的跨模型低相关只支持本样本，非能力正交定理。AI/human混源、共享corpus不构成独立真实生命周期证据。hardware/precision/batch/concurrency/SLO Not Disclosed。

判断范围：不由普通passage排名认定memory检索、下游回答或权限/更新正确，不外推版本/均值。成本含表示、候选域、索引和下游评价；MTEB/BEIR在开放文档检索中继续合理。

actual Books：resume_mar17顺读Ch77 328–367，现332–350已明确query-time anchor、粒度、authorized candidate scope/source-supersession→retrieval→Context/outcome，并以LMEB限定反证说明通用passage排名不代表memory；write correctness、authorization、deletion/freshness/answeruse单独验收。Ch76 345–383与Ch78开篇交接已读，检索主干不接管Memory状态。唯一AGENT-MEMORY具体已有覆盖，无新差额须写、无PRE/POST写入，也不凭NC降低评分。

尚待resume_review17_18必要Source/具体NC独核；当前不计安全完成或DAY。准入误判/版本信号才定点重开，不扩全部22原数据附件。
