# Apr16 五项实际 Books 写后复核

复核者：root（非报告作者）；检查日期：2026-09-27。复用 apr01 已实际完成且未变化的五项精确 v1 来源→owner 核验，重新顺读下列真实正文及相邻段落。本次不是源实验复现，也不代替全日来源、日期、候选及排除侧验收。

## 实际正文与边界

- **13645 Sim-and-Real Co-Training**：Ch26 在 fleet 数据回流与 sim-to-real 交接处实际承载“保留动作所需 domain condition，再对齐其余表示”，区别于单纯 schema 对齐与盲目域不变。普通 ADDA/OT 不利结果、有限三任务 balanced 真机范围、标签/校准成本及 real-only/mixture 回退均在正文；没有从 latent 对齐推导物理安全。两段与后续物理 domain gap 相容，通过。
- **13733 VLAJS**：Ch26 Online RL 分支实际区分辅助方向、reward 与执行动作，环境执行 PPO proposal、teacher 仅在训练期稀疏提供方向，近零/gripper 例外与撤掉 teacher 均明确。阈值口径冲突、普通 PPO 反胜、20次真机不证安全及 safety veto 就近保留，与前一 compact RL-token 分支是替代路线，不是后者被淘汰。通过。
- **13788 FIDeL**：Ch26 State ownership 后实际区分名义偏离检测与任务失败语义判定；后级不能继承前级校准保证，也不能拥有 continue/retry 权。示教/校准漂移、两级错误与计算成本、人工/确定性回退明确，与 sensor/estimator/controller/environment 分权相接。通过。
- **14029 POINTS-Seeker**：Ch75 视觉 artifact 后实际写入旧文本 observation 渲染、actions/近期 observation 留文本的表示分支；原摘要不会变成原站事实。consumer 适配、render/编码/恢复成本、all-image 不利 slice、短轨迹文本共存与禁止推导端到端时延均明确，未把该分支混为 active-slot 驱逐策略。通过。
- **13706 Co-FactChecker**：Ch75 scratchpad diagnostic 后实际区分可编辑生成 prefix 与内部因果状态；remove/modify/guide、旧 verdict/end-of-thinking 抑制及继续生成作为派生 control artifact，保留原 trace/来源并要求新输出独立验收。gold/rubric oracle、小真人样本、editor/replay 成本与 append-only 回退明确；没有声称忠实思维或普适严格改进。通过。

五项均有带对应 Source Family 的实际正文，不只存在 Review notes。结论：上述五项 actual write-after 通过，可以从普通 Books 待办转为真实整合；全日是否完成仍由剩余终态、来源与非作者日级复核决定。
