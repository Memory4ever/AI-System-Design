# 2604.25380v1 → Ch66 非作者实际写后复核

复核者：apr02；正文写入者：root；04/29 日报作者：apr20_resume。复核结果由 apr02 于本次执行中回报，此记录只覆盖该 source family 的写后判断，不是 04/29 日级 Gate。

- 对照 [官方 exact-v1](https://arxiv.org/html/2604.25380v1) §3、§4.2–4.4、Tables 4/6 和 [Ch66 实际正文](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)约 833–835 行前后，非作者判定 PASS：动作间瞬态状态、采样策略/时间戳/可重放 witness 与结果分账接入 EvalSpec，并与前后 ClawMark→评价主线衔接。
- 正文没有把完整方案 22.1% 归因于单纯选帧；Table 4 DP-only 17.4 与 full 22.1，Table 6 uniform1 16.8/uniform3 16.4/“Ours DP”22.1 的标签或组件归因含混已保留。`missed-event rate` 是书稿提出的验收要求，非论文已测事实。
- `git diff --check -- books/part-06-ai-infrastructure/66-evaluation-system.md` 由非作者核验通过。日期与整日分母、其他候选及来源覆盖仍需单独 Gate。
