# 2604.23581v1 AgentEval：有界 Source→Owner 判断（作者侧）

固定本窗 `[2026-04-27 09:00, 2026-04-28 09:00) BJT`。本页只复核此家族的必要 exact-v1 与现有正文，不把旧收据的 `retained`、v1 `Updated` 或现有 Books 内容当首公开/准入证明；日期与非作者判断仍待 Gate。

官方 [exact-v1](https://arxiv.org/html/2604.23581v1) §3.1–3.4/Algorithm 1 的可复用对象是 typed step、父依赖与该类型的 rubric。逐节点评分时把父节点 context 给同一 judge；若低于类型阈值，再以低分 parent 作 `propagated`/`root` 的贪心标记。该标记是诊断启发式，不是对父节点干预后的因果识别，也不证明 judge 分数是工具效果真值。

§4.2–5.1/Table 3 的同 judge、同 rubric 的 Flat Step 对照，在 **150 个有人类标注的 case / 195 个失败步骤**上，FDRec `.67→.89`、RCA `.38→.72`；450 是三工作流总测试 case，不应换成 Table 3 的人工分母。该对照支持在受测 DAG trace 中加入 dependency context 的局部收益，但正文 §5.5/附录的约 12% 非 DAG trace（54 条）结果更低，retry loop 尤明显。§6/Appendix M 的修复时间将此前 47 incident 的人员回忆与后来的 156 event 系统日志相较，起止定义也不同，不能宣称同协议的因果工时节省。

实际 [Ch69 Trace](../../../../../books/part-06-ai-infrastructure/69-trace.md)「Root-cause graph」已明确 immutable trace → 派生 dependency graph → backward slice → candidate module → reproduce/patch/regression-test/abstain，并指出 graph 是诊断 view、不是 patch authority。实际 [Ch66 Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已分 typed step/tool outcome、judge/rubric 与最终 task effect。此稿把两层已有责任联接成 typed-score + parent-context 的一个受限实现，并给 Flat 同协议对照；它强化了 DAG 诊断的证据，但未改变本书的 graph/score/effect 权限、状态身份或放行条件。**作者建议候选保留，Books 窄判 Existing Coverage（Ch69 主、Ch66 交接），不为贪心最低分 parent 另写通用根因算法。**若非作者确认当前正文实际缺“父依赖必须进入 evaluator context”的长期评价责任，可只重开该窄命题。

日期方面，receipt 的 v1 `Updated=2026-04-28T00:50:01Z` 与当前 OAI 04/28 为公告段旁证；须按正常周一公告槽、连续 ID/邻界及同族更早公开反证有界判断，不能写为逐篇公告秒点。此页非独立审阅、非正式分母或日 Gate。
