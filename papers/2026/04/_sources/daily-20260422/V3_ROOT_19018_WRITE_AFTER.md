# 2604.19018v1 → Ch31 写后独立复核

复核者 root；作者 apr02。已在采用前定点核对[官方 exact-v1](https://arxiv.org/html/2604.19018v1) §4.1–4.3/Eq19、§7/Tables1–2，并在写后重读 `books/part-04-training-system/31-rlhf.md` 的条件化 activation intervention 前后段、Review notes 及局部 diff。此记录只验收该 Source Family 的正文写后语义，不等于 04/22 日级 Gate。

**PASS（窄采用）**：正文把静态方向/施加量问题自然接到离线按层 Jacobian/Riccati gain 与在线当前 feature error，保持 base weights 不变；明确层深 horizon 不是未来 token 规划，feature/setpoint 不是语义真值，actuator 不取得 safety policy authority。对局部线性化、gain 驻留、逐 token 计算与漂移设成本/失效边界，保留小幅静态 steering 和权重后训练的共存/回退。作者 Gemma 切片 PPL 8.95→12.26 的代价没有被抹掉，也没有把作者 toxicity 改善外推成安全保证。相邻的组合 feature intervention 段仍拥有不同命题，未重复本项。

`git diff --check -- books/part-04-training-system/31-rlhf.md` 通过。未复现实验；04/22 的来源、日期、分母及其它候选独立审计仍须单独完成。
