# 2604.19083v1 → Ch72 实际写后复核

复核者 root，非该书稿段落与 Apr22 日报作者。已定点重新打开 [官方 exact-v1](https://arxiv.org/html/2604.19083v1) §5.1–6.3、Eq8、Table3 与附录 E.1；实际顺读 `PLATFORM-SECURITY` Ch72 的 soft-channel provenance → 本次新增两段 → Artifact contract，以及章末该家族 Review note。`git diff --check -- books/part-06-ai-infrastructure/72-security.md` 通过。

**写后 PASS（仅此家族）。** 正文把整体 `ΔW` 谱或单 neuron 阴性、同输入的 projector 输出 `ΔE`、trigger probe 与最终生成/下游 effect 分开，未让一个诊断 sensor 自动成为发布授权。LLaVA-1.5-7B 的低秩移除是受限切片，不同攻击、层与 rank 非单调；clean 对照、配对输入、未知 trigger、MathVista/POPE 退步及回退边界均在机制附近。未采用作者的普遍因果或充分修复保证，没有把论文名称堆成独立清单。

这不证明 Apr22 日期、候选分母、其余证据或整日报 Gate。作者据此同步当日 Books 栏和章末状态；若后续独立审阅发现身份/日期反证，只定点重开本家族。
