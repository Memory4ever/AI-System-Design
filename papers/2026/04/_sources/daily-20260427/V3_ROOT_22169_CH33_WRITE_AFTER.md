# 04/27 ReCast：Ch33 非作者写后核验

复核者：root；正文作者：apr01。范围仅 `SF-2026-ARXIV-2604-22169` 与 Ch33 实际写入，不替代 04/27 整日报 Gate。

- 官方 [exact-v1](https://arxiv.org/html/2604.22169v1) §3.1–3.4 先区分 task reward 与只用于组内选择的结构分数：全零组才由目标输出派生正 anchor，替换最低结构分项；随后以任务奖励最高正例与结构分数最高的未命中项组成局部更新对。`books/part-04-training-system/33-grpo.md` 中新增两段均保留了这条 producer、筛选与更新链，没有将结构接近写成任务成功。
- 原文 §4 与 §5.5 的 `W_search=G`、`W_update=O(1)` 是 actor-side 支持宽度分离，不是 rollout 生成成本消失。Ch33 明确 old/reference log-prob、actor 反传才按常数对处理，并要求搜索成本与 actor 成本分账。原文 §5.1 给 Qwen3-8B、64 Ascend NPU、`G=32`；Table 4 的 `371.54→77.00s/step` 和 `211.04→12.71s/actor update` 被限定于该离线推荐实验，未外推服务加速。
- 原文 §5.3.4 与 §6.2 明确较强 backbone 时 Repair-only 可转负、实验只覆盖离线单目标 next-item。新增正文保留目标派生 anchor 相对自采样 rollout 的身份差异与 selection/off-policy 风险，也保留普通 GRPO、Dynamic Sampling 或跳过的适用边界。这里的风险是从机制推出的审慎工程推断，并非作者已测出的部署故障。
- 相邻交接：Ch32 保留 on-policy trajectory、ratio 与 critic 责任；Ch33 的新段置于 Dynamic Sampling 与固定 anchors 的不同分支之后、全错组转 SFT 分支之前，阅读链为“丢弃或补采 → 保留但只变统计 → 目标派生修复并缩窄 actor → 任务目标分流”。Ch34 继续离线 preference pair 的另一分支；没有把推荐实验升格为所有 RLHF 的替代。

结论：本 Source Family 的必要证据、实际正文和前后衔接写后 **PASS**；可将本项记为实际 Books Integration。未复现实验，不签 04/27 的 14 来源、候选分母、日期、负面侧或整日报 Gate。
