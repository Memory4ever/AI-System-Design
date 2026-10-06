# 最后五项的一次决定核心与首次公开纠偏

作者已实际读以下exact-v1原源必要核心（curl本轮空正文后官方HTML Web成功，不标外部正文受阻）。只为贡献准入决定，不默认全文队列。完整题摘原文见V3_ADMISSION_FINAL_ABSTRACTS.md；本文是具体判断依据，待root独立校准。

## 12544：有具体target admission差额，首公开信号先核

https://arxiv.org/html/2602.12544v1 §2.2 L108–133：部分CSR改动不仅是一组reward项，还选择首次达到最大CSR的最短prefix；原task下stop仅CSR=1接受，部分成功则删除未满足的task constraints、重写stop reasoning，让target与新task一致。可改变“原失败动作是否可直接蒸馏”的准入判断。此项暂不宣称新发明HER或通用无偏监督。

current官方abs Comments COLM2025。一次具名OpenReview搜索返回同题同作者原稿 https://openreview.net/pdf/94dc5128f5357bccc1a6a42d1c5ce09fc5a0da1f.pdf ，实际页首明确Published as a conference paper at COLM2025。待有限论坛公开日期/原稿身份核；arXiv Feb2026首次登记只证明该artifact，不替论文首公开，不能先纳本窗候选。

## 12714：拟准入前关闭，并保label/trust信号

https://arxiv.org/html/2602.12714v1 §3 L148–150：原标注forced-choice primary，tie全部保primary、任意非primary票保minor、Other丢弃。§4.3 L197–205：gate是组内correct/incorrect evidence-score均值差的软折扣，始终正，不是取得独立事实证据才允许tool reward。tool+GRPO与标签重标尚未建立本项目新增可靠性条件；不凭emotion领域目标定义或gate公式准入。少数primary votes不等co-occurring真值、soft gate不兑现only-when硬准入，信号保留，不说论文无价值。

## 12746：拟有界准入

https://arxiv.org/html/2602.12746v1 §4.5/Table3；本日V3_ADMISSION_12746_FINAL_CORE.txt B98–120。固定总20experts且相同replay/loadbalance，五allocation含2/4/6/8与2/2/8/8；更偏深不必更好。因此它不只是LoRAexpert+replay组合，而提供同容量分配反侧，影响以layer allocation替换统一配置时的选择。2+1+2=5拟标准；CER局部、gradual-depth不是全模型定律，replay去除不是allocation唯一因果。

## 12756：拟范围/贡献关闭，保guarantee信号

https://arxiv.org/html/2602.12756v1 §4.3–5 L139–185。冻结LLM numeric patch forecaster，加历史估计residual observer、两阶段训练与head局部Lipschitz正则。theorem假设真误差、全x contraction与单步误差有界，是普通control条件，未建立基础生成主线的新增机制；局部head约束不认证整个plant，推理estimated observer误差未被该theorem覆盖。关闭理由是当前直接项目增量未建立，不将一般TSF或小理论一律排除，不删其provably stable宣传与证明interface缺口。

## 12876：拟准入前关闭

https://arxiv.org/html/2602.12876v1 §§3–4 L110–138/188–216、§5.3 L264–273。publicly searchable evidence、人工sub-goals、过程成功分数与visual grounding/planning错误分类是成熟评价构件；本次核心未给相对于现有过程评价的具体漏测反证或新成立边界，只增加题库/覆盖与现模型指标。未因评价局部或新benchmark本身排除，而是尚未建立长期判断差额；保原任务结构和独立诊断价值，不授public可访问即稳定可复现。

## 12618：既有发表信号，定点重开日期

current官方abs https://arxiv.org/abs/2602.12618 Comments BigData2025（v1 Submitted2026/02/13 04:49:27Z）。DBLP具名记录同题同作者IEEE BigData2025:4544–4551只作出版身份线索，不作正文证据；待一次publisher公开字段核。贡献准入已过不因访问/费时删除，但最终本窗身份不得借arXiv登记覆盖更早首公开。
