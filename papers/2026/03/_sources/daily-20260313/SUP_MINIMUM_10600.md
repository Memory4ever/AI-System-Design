# 10600 Trajectory-Informed Memory：最低关闭判断（待非作者）

仅03-13补Mar12 BJT自然日。第三完整题摘和决定core准入有效复用；本次直接重对SUP_ABS3_10600.txt题名/七作者/完整abstract/history/v1，无可见撤回说明。DATE4 submittedMar11T09:54:09Z/registeredMar12T02:05:28Z日级夹证已非作者核通过，公开不由submitted单独认证。SUP_ADMISSION_DECIDER_MANIFEST_RESULT.json官方 https://arxiv.org/html/2603.10600v1 GET200/285051bytes/UTC2026-10-09T12:52:43.673000Z，实际SUP_DECIDE_10600.raw/txt原件留存。

## 新增命题与最低评分

新配方按trajectory逻辑phase切subtask、留原step range/source、抽2–4 strategy/recovery/optimization tips，再泛化/cluster/merge，按task/metadata检索并写进prompt；保留的是该粒度与其源标签、检索消费差额，不是普通summary/RAG或三类别命名。拟Design1+Reach2+Durability1=4：局部segmentation/tip/merge实现1，执行轨迹→memory producer/store→prompt consumer跨边界2；GPT4.1与单AppWorld配置的工程对照1，未另外确立可靠自归因/无oracle写入、通用粒度或新稳定admission条件。不能借已知provenance、独立失败验证、粒度随任务选择成熟约束抬Durability，也不因Books有memory主题或工作量倒定低分。

拟最低4分已关闭、不进一步采用Books0，非准入EX/非已有覆盖本稿实验，未formal。原因是新证据范围仍是当前tip构造/检索组合的局部取舍，不能支持新的通用可信写入或因果机制；如后续实际可靠validation/admission边界成立可重开，当前不为了潜在高分扩附件。

## 实际必要原件

直接读§3.1.1–3.1.4完整extract/attribution/tip/schema/两phase（289–755）、§3.2完整generalize/cluster/merge/storage（755–815）、§3.3检索及prompt（815–980，prompt示例只格式）、§4.1–4.4完整配置/协议/Tables1–12（980–1450）、§6结论/未测scope（1548–1575），并直接相关§5.3/5.4仅核原文自身与成功/失败经验memory的差异声明，不继承被引用前作数字或重开别家族。首次3.2合并段大输出截断后755–815单独恢复；不将未看代码/线上CUGA运行、完整references/图pixels或其他model验证当已核。

有GT outcome报告用报告，**无GT则从agent自己的reflection/self-correction/error-recognition推断成功/失败/恢复**；随后LLM回溯思维作immediate/proximate/root/contributing原因叙述，不包含受控action替换或可识别因果估计。原source ID/step range支持来源回查，不认证描述/label正确。Merge使用tip category/priority/outcome，成功来源优先和恢复tips优先；无GT的自述可能进入这些优先规则并自强化，不因此声称实际全部污染或造假。Subtask generalization删除app/user/task qualifier可复用，也可能删掉适用条件，cosine.85聚类不是equivalence真值或冲突裁决证明。

Runtime cosine threshold/topk与LLM metadata/query/priority选择只是proposal；提示tips在task context后/standard instructions前，不获得本次权限或source truth。§4同GPT4.1 Agent及extractor、simplified ReAct、max30steps，tips来自train/dev，test-normal heldout不与source partition混。TGC全programmatic unit tests，SGC每scenario全部variant，非同一指标/分母；没有test tips入memory的可见声明，不推test泄漏。完整有效task/scenario数量、重复运行seed/CI、embedding实际identity、采样配置/总token、memory生成/merge/LLM-selection全费用和wallclock在这些必要段 Not Disclosed；作者framework实测AppWorld不签CUGA生产效果，多agent/model-family是future work。

Table1/2 subtask+LLM TGC73.2/SGC64.3 vs69.6/50，Table6 subtask+cosine73.8/57.1，Table4 task+cosine72/62.5；同cosine下细粒度TGC高而SGC低，LLM选择加调用且从配置同时改变metadata/priority，不能用aggregate唯一归因phase或“因果诊断”。Table3 task cosine τ.5/top3 TGC66.7/SGC48.2低baseline69.6/50；Table5 medium TGC64.6/SGC43.8低baseline66.7/56.2，反例收紧“all configurations substantial improvement”。原§4.1.4说两strategy都top5，而后cosine最佳/no-topk及top3不同，保持原协议差别不补成统一公平prompt budget。Train easy memory94.4/83.3低base100/100，dev hard两者100并非新提升。不同threshold/chosen tip长度/数和retrievalLLM开销未统一；不授通用τ.6/topk、额外memory恒有益或更省。

## 不进一步采用与唯一owner

ROADMAP `AGENT-MEMORY` Ch77唯一owner，Ch76只检索交接。本次actual完整顺读Ch77 138–153失败reflection pending/环境receipt与模型proposal、185–217检索计划/原始source与预算、280–310派生来源/事实与retrieval-policy、706–738 hierarchical skill的phase粒度/适用条件/source/isolated validation/rollback。已存在这些长期资格，并不等本文新AppWorld实验或具体implementation已被吸收。本文没有在无oracle判断、step因果、cluster等价或按部署目标选粒度上补出新的已验证稳定条件，因此不制作同principle的第二正文段，也不泛称已有覆盖来免必要读。

若有独立验证的tip标签/冲突裁决、same-tip数量与token预算的粒度/检索受控对照、真实no-GT与外部receipt分账及新的可核admission或撤销界，到达仅重开相应命题。当前普通未披露不伪造外部阻塞，不需为了这些未来可能结论读全部代码/复现实验。待非作者最低Source/actual新增评分及关闭理由核；未formal/DAY。
# root非作者实际最低裁定

root直接§3.1 GT/selflabel及回溯、§3.2完整merge责任、§4.2.3–4/Tables6–7原件独核，1+2+1=4、不进一步采用Books0 PASS落主ledger。正式同步第29项，不改EX/不称新实验已有覆盖，不授DAY。

