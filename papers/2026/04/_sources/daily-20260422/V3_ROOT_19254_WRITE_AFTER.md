# 2604.19254v1 → Ch30 写后独立复核

复核者 root，作者 apr02。先前[写前裁决](V3_ROOT_19254_FINITE_OWNER.md)已对读[官方 exact-v1](https://arxiv.org/html/2604.19254v1) §3.1–3.3/Table1 与 Ch30；本次实际重读 Ch30 的 S0 段、紧邻新正文、Merge 段及 Review note，检查本次局部 diff 和 `git diff --check`。首次写后发现注入/更新控制流易读反，作者已定点修正，复核的是修正后的实际文本。本记录只签该家族的写后语义，不代签整日 Gate。

**PASS**：新段明确第 `l` 层先用 `h^(l-1)` 与 `s^(l-1)` 形成差分注入，算出 `h^l` 后才更新 `s^l` 供下一层，符合原文控制流；没有把所有投影/门控权重误作共享。它在固定 `S0` 与 mergeable delta 中间补充 depth-conditioned attached shadow state，资产身份、reset/隔离、额外执行和 detached 非等价有对应 trade-off。旧 LoRA、固定 S0 和可 merge 路径在其原条件下共存；Table1 的强退步未被写成普遍性能外推。Review note 保存 exact-v1、受测限制和未复现边界。04/22 的日期、分母、其它候选与独立日级复核仍另行处理。
