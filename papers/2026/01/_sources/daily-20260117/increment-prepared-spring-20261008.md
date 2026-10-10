# SPRInG09974 必要原证与窄 owner 差额

当前处置：root必要源/actual owner PRE通过并授Ch77窄锁，正文967/969、自身2137末注实际POST通过，完整951–1008邻接已非writer顺读，锁释放。随机训练对照只匹配30%数据比例，不证明selector/重评分全预算匹配，已修正近正文；本项5分深入整合正式同步，不授DAY。以下提案历史保留，不重新请求已完成PRE。

准入已独立题摘校准，2+1+2=5标准；若采用以下Ch77差额则受影响深入，不扩703行附件。exact-v1 https://arxiv.org/html/2601.09974v1；原件increment-spring-aai-method-20261008.json（§3/4.1）、increment-spring-aai-eval-20261008.json（§4.2–4.3）、increment-aai-current-spring-app-20261008.json（AppA1/A2及所见必要部分）、increment-spring-aai-current-gate-20261008.json（D2及当前abs），find/Limitations原件待保存同目录。实际必要范围§3 Eq1–8/§4 T1–3、A1 Alg1/2、A2 T4、D2 T8、Limitations264–270。

机制采用：旧adapter/base sequence-likelihood差与base-likelihood质量项只对本期新增interactions产生top30%更新proposal，不是真实persistent preference drift detector；仅选中数据fine-tune，旧buffer不是replay训练集。更新后把本期选中与旧buffer并集，用新adapter再评分；未满Nmax全存，否则全局topNmax，形成尚未被新参数充分解释的残差检索bank。第三权限在当前query：BM25 top2超过σ才把history消费进retrieval分支；同一adapter/共享已提交prefix两条件概率以λ混合（Eq8不是raw-logit相加），不是参数/事实truth裁决，λ=.5固定而非逐token学习gate。

边界与反侧：Gemma3-4BIT/两LongLaMP任务，每任务small/large各50用户、5period，90%history/10%test按时间切分；没有独立标注真实drift。Table2相同30%对Random支持局部选择而非只规模，Review ROUGE-L均.125不优；Table3 λ=.1/.5 Review均.142不授通用λ；A2四retention Review都.145，不能独占归因全局最高；α∞与.5/1表同数，非novelty独占证据。D2 Q3 Abstract RL.190<无gate.191，Review RL.142<无gate.143，R1有局部收益；跨users/periods汇总BM25 quartile设阈值，不授纯online无lookahead校准。σ失配/假drift与噪声仍存在；没检到history回纯参数，不意味着参数此时真实。greedy/repPenalty1.2/max600，LoRA Q/V r8 α8两epoch/max768；hardware/precision/concurrency/SLO/重复seed/CI/实测完整费用NotDisclosed。两路径每step两forward、base/adap打分、新adapter重评分、每用户adapter存储与维护都费；30%训练量不证明端到端净省，adaptive早退是futurework。

日期/current：DataCite09974原字段Submitted Jan15T01:32:27Z、Updated-v1 Jan16T01:12:33Z、registered Jan16T02:43:57Z；依已核正常公告/正式ID仅公告赋予规则形成Jan16BJT正式事件上下界，不单用registered证明firstpublic。当前abs v3 Aug30、v2 Aug10，Comments EMNLP26/30页；所见当前页无撤回/纠错/安全说明，v1必要原文未见直接更早全文signal，不宣称全互联网不存在早稿。

actual owner作者实际读Ch77:950–990完整邻接：parametric facts/共享reasoning adapter、micro-LoRA atom、migration与raw退路已有；但不存在**更新选择→更新后仍需保留的残差→当前query允许消费**这三个不同population/权限，不能把一个memory-quality score同时任命三者。提案唯一AGENT-MEMORY：在parammemory/adapter段邻接用1–2短段自然补充：原external history与adapter共存；更新前score仅决定参数更新候选，更新后rescore决定bounded evidence buffer，当前query relevance才决定本次读入；三revision绑定和原始记录保留，score/gate非truth，误筛/旧偏好/新adapter漂移、双条件forward/重评分费用与静态history+固定adapter/关retrieval退路就近。不抄BM25阈值/30%作为通用recipe，不在Ch30或Ch20重复写。尚待root PRE/owner窄锁，本包不自授通过。
