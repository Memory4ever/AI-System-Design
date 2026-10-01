# `2604.20051v1` 有界非作者 source→Books owner 裁决

范围：只复核 [root 必要证据](./V3_ROOT_20051_FINITE_EVIDENCE.md)所提 `2604.20051v1` 的 5 分准入、长期 Books 增量与关键非证明项；不核 04/23 全日来源/首公开，不改该日正式日报或共享 Books，不复现实验。

## 必要原文与真实 owner

- [官方 exact-v1 §3.1–3.2](https://arxiv.org/html/2604.20051v1)：同一 `π_ref` 从任务相关预训练文档生成题目/参考答、采样多答案、条件化文档/参考答/候选生成 weighted rubric，再自行给各候选 0/1/2 分。正负样本是同题最高/最低分两端；格式不合法、同分、长度差超过 100 words 的 pair 被拒绝，随后用离线 DPO，而不是用在线 GRPO 训练。文档只给模型一个额外条件来源，不能使同源评分自动变成独立事实 oracle。
- [§4–5.5 与 Appendix F/J](https://arxiv.org/html/2604.20051v1)：Qwen-2.5-7B base/instruct、Healthcare QA/Creative Writing/Instruction Following 为受测范围。§5.5 的全排序 Spearman `0.3301→0.3424` 和两端 pair 的较强模型同向率 `82.04%→85.14%` 是两种不同统计对象；较强模型排序仍是 proxy，非人工正确率或任意候选保证。文档条件与 rubric 的消融支持局部配方，不独立识别所有共同生成角色；无人工/强 teacher 生成训练标签不等整条评价链无外部 judge 或真值成本。
- 实际 [Ch31 偏好准入](../../../../../books/part-04-training-system/31-rlhf.md)约 125–131、[Ch34 DPO](../../../../../books/part-04-training-system/34-dpo.md)约 244–272 已要求 pair 来源、score/tie/length/选择 mask、reference、独立 held-out 与 coverage/selection-bias 分账。[Ch33 自博弈与 rubric](../../../../../books/part-04-training-system/33-grpo.md)约 1337–1360、1372–1388 已明确自我确认/role collusion、evidence-derived rubric 的来源/版本、独立校准、judge 无 truth authority；其中 policy 不可见 passage + 冻结 judge 是另一条 GRPO 分支，并非与本篇同一个实现。

## 有界结论

**贡献准入：PASS，`2+1+2=5` 标准审阅。Books Decision：`仅报告`（Ch31 `TRAIN-RLHF`、Ch33 `TRAIN-GRPO` 与 Ch34 `TRAIN-DPO` 的现有责任链足以承载要采用的长期判断；不把 POP 的完整实现误记为已有覆盖，也暂不新增正文）。** 本篇最具体的可迁移提醒是：外部文档条件与只取极端 pair 可能在全排序不可靠时提供受限离线偏好信号，但它们只缓解同源排序错误，不赋予同一个模型合成的参考答/rubric/score 事实权威。这个取舍已经可由现章的 pair admission、rubric provenance/独立校准、自博弈同源风险与 DPO 的固定 pair 分布推得；论文未给一个会改变这些责任或回退规则的独立失效/控制边界。若将来有跨模型、同总生成/评审预算的独立结果证明同源 judge 在特定证据条件下可替代既有外部 Gate，再重开 Books 判断。

保留该 family 在 04/23 Daily 的受限机制/反例，不按名称或局部 benchmark 增益前分母关闭；但也不因缺一个字面算法名就追加书稿。日期仍由 04/23 owner 用公告/邻界而非 HTML 页头 `21 Apr` 单独裁决。本记录只是一项非作者有限采用审查，**不是 Books 写后或 04/23 日级 Gate**。
