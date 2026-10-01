# Apr22 首批准入独立校准

复核者 apr01，非本日报作者；2026-09-27。已实际重读当前 AGENTS、研究/Report/每日来源合同及 ROADMAP，读取作者 V3_REVIEW_CHECKPOINT 的准入问题，并从 owner-replay20260422 原始库存逐项读完整题名与摘要。范围只下列9项，不是515全题摘/日级验收、证据完成或Books授权；日期/精确版本及必要方法评价由作者继续。

| 家族 | 独立准入裁决与原文依据 |
| --- | --- |
| 2604.18592 | 保留准入。摘要明确句子前缀×层深两个退出维度联合，在语义逐步积累的分类条件下改变‘完整输入后只做层退出’执行分支。3–8B/情感分类不是硬拒；但不能由computational saving推生产latency，且微调削弱收益是关键负边界。 |
| 2604.18616 | 保留准入。摘要的tile标签传播、use-site关系断言、layout algebra/SMT及反例定位形成不同于功能pass/fail的kernel优化反馈；不是因Agent+compiler名词入选。必要原文须核symbolic语义与硬件policy支持范围，99–104%和零runtime overhead不能直接外推。 |
| 2604.18658 | 保留安全评价准入。摘要把generic harm→owner harm与tool-vocabulary迁移分开，并给通用LLM对照与结构goal/action输入条件；这修正防御跨环境可行性判断，不只是新场景数。27任务/posthoc300分母、规则绑定和有限CI后续核，不采用形式框架普遍保证。 |
| 2604.18788 | 保留准入。摘要明确动态expert路由与ANE静态shape冲突，capacity tiers、grouped execution、load-aware graph residency及CPU/GPU回退是具体执行/状态分工；不是端侧产品升级。离线校准漂移、prefill适用边界和能耗测量需必要证据。 |
| 2604.18791 | 保留准入。摘要有context H32、same-budget LoRA与memory-conditioned state verifier的控制比较，可能证明历史长度不能替代执行验证/恢复职责。不能先把三种gap当所有长任务充分原因，rollback是否真实物理回退须核。 |
| 2604.18860 | 保留保护深入准入。摘要明确截图与dispatch之间的focus/notification变化，pre-dispatch的像素/窗口复核与零视觉DOM盲区是可定位新失效路径。180 trials/零FP只此受控样本，不能写普遍拦截或OS原子保证。 |
| 2604.18995 | 保留准入。摘要区分局部confidence/position簇与跨step稳定token，finalize规则加trajectory适配训练改变可编辑/commit边界，而不只是减少步数。必要评价核质量、threshold/训练成本及步骤不等端到端时延。 |
| 2604.18805 | 前分母关闭通过。完整摘要研究八科学领域agent的认识论/科研workflow，当前AI for Science明确暂缓；不能借Evaluation/Agent owner恢复这一领域任务。关闭不是否定其科学意义，不追全部发表史。 |
| 2604.18652 | 最小接口消歧后前分母关闭。实际重开[官方HTML v1](https://arxiv.org/html/2604.18652v1) §4、§5.1–5.4：typed binding/schema、非特权proposal、IDG消费污点传播、sink要求VERIFY清污点、FSM全局policy、预算分层checker。原文没有给概率语义到确定ISA的新保真桥、动态policy的独立保证或受控失效条件；kernel/ISA命名与五类taxonomy不足以新增长期机制。§6数值仅特定host guardrail对照，不使该组合成为新保证。不因‘无新架构’作硬拒，而是已读决定准入的接口实际内容后关闭。若作者在具体实现找到新增可执行失效/保护契约可定点重开，不全附件。 |

七项潜在贡献准入口径通过；一项范围关闭通过；一项接口消歧后关闭。评分仅维持作者最低投入草案，不据本次准入校准预支来源/日期/证据/Books/日级Gate。
