# 10524v1：最低必要增量判断（非报告作者准备）

仅03-13增量窗：2026-03-12 BJT自然日。2026-10-10由root将未读停点转交本作者；不写Report/Books/共享ledger。准入独核及DATE4日级夹证直接复用主独核§第四包及DATE4/5原字段复核（10349/10512/10524/10538/10640/10261十项）有效层，不重复以Submitted单独授公开日。精确身份为 **AILS-NTUA at SemEval-2026 Task 8: Evaluating Multi-Turn RAG Conversations**，五位作者与本日 `SUP_ABS4_10524` 相同，Comments无具名先稿/修订线索。

原证：官方 https://arxiv.org/html/2603.10524v1 ，实际GET200，576142bytes，时间及final URL见 `SUP_HANDOFF9_FETCH_RESULT.json`。完整原响应 `SUP_HANDOFF_SOURCE_10524.raw`，文本同名txt；不是latest或代码复现。

实际必要阅读：txt457–719（§3完整：五query、hybrid rerank、nested RRF、span/双candidate/多judge与answerability）；969–1156（§5 TaskA–C全部关键评价/Table4–6/结论）；5034–5108（D.1条件/阈值扫Table38）；5182–5183（Limitations完整）。未读所有34附加tables或prompt附件，无需扩大。

新增命题：对话query五种改写在同一语料对齐ELSER上，两级RRF先压三高variance改写为Weak Consensus，再与稳定两路按corpus权重融合；与异构retriever的局部比较表明更多R@100不必改善R@5/10。三种answerability judge分别消费文档、span和答案，partial与unanswerable不同人口。新颖性是本语料局部配置/诊断，不是RRF、HyDE、多judge或拒答校准的发明。

必要正反侧：Table4 dev .483→.607为逐配置增量，非全检索器普遍支配；异构unique gold平均rank37–54，引入fusion噪声只限当前retriever/rewriting。Table6多judgeANS95.8/UNANS21.8/F1 24.0；加calib ANS92.3/UNANS27.3/F1 23.1，不授calibration在所有指标改善。主文83.9%accuracy和Table6的95.8%ANS recall不是同指标。D.1称阈值.7最大macro-F1，Table38/caption实际列HM最大；保留口径不据此认证唯一最优。开发unanswerable6.5%与test19.1%/领域和turn分布漂移；作者建议test阈值.6未在gold验证，不能据此授部署校准。Answer judge偏semantic plausibility及span不足不是全LLM因果定理；多模块累计消融不能识别每模块独立作用。成本降为uniformGPT4o三分之一只当前路由比较，不是整RAG生产总费用认证。

评分提案 **1+1+2=4**：新本地fusion/threshold/routing配置（1）；影响当前multi-turn RAG语料和selector局部（1）；可复用但非基础算法/跨系统新不变量（2）。不把成熟retrieval-vs-answerability分账原则、SemEval排名、pipeline模块数或未来适配建议计新分。准入P保留；拟 **已关闭／仅报告／Books0**，非EX、非具体已有覆盖新实验。0–4最低投入已够，不强制owner/PRE/POST。独核尚待；root采用后才同步正式。
