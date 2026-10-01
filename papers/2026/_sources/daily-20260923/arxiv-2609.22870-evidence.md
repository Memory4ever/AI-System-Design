# arXiv:2609.22870v1：FP8 RL clipping 证据笔记

状态：精确 v1 PDF 定点审阅、候选准入、官方公告批次日期、撤回检查、评分及 Ch33 写后复核均已通过独立检查。本笔记只验收单项，整日报状态以日报为准。

- 身份：[Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870)，作者页给 `[v1] Sat, 19 Sep 2026 08:20:54 UTC` 为提交字段；本次读取[精确版本 PDF](https://arxiv.org/pdf/2609.22870v1) 17 页。09-22 官方 New 公告批次对应 09-23 08:00+08；撤回检查已完成，若取得更早作者公开的可核证据再定点重开。不得以提交日当公开日。
- 问题与旧方案：BF16 训练配 FP8 rollout 可造成行为策略/learner 前向精度不一致；此前 TIS 等方案主要修正这条 rollout–train mismatch。两端都用 FP8 能收窄该 mismatch，但不能据此保证 surrogate objective 的裁剪语义不变。
- 机制：§2–4 的 old/current log-prob 经过 FP8 前向，概率单点误差在重要性比率中复合；对负优势 token，`r_BF16 > 1−ε` 而 `r_FP8 ≤ 1−ε` 时，本应压低坏输出的梯度被 clipping 假性归零。作者以 BF16 shadow forward 对同 batch 求负优势 ratio 的参考 lower-tail clipping 分位数，再用 FP8 经验分位数找 lower bound；upper bound 按正/负有效更新幅度比重新平衡。每 20 step 做两次额外 BF16 forward，平滑更新边界，而不是每 step 全精度运行。
- 因果链证据：§3 在 Qwen3-8B-Base、DeepScaleR、GRPO、16K context 下观察中途熵激增、garbled output、lower-bound over-clipping；放松 lower bound 能消除激增却造成过度惩罚、低 reward 和短回答（Figure 5），支持需要双边校准而非单边放宽。§5 对 Qwen3-8B、Qwen2.5-32B GRPO 和 Qwen3-14B DAPO 比较 BF16、FP8 rollout+BF16 train、不同 FP8 scale grain 及校准；Appendix A.5 检查更新周期/初始化敏感性，A.6–A.8 给 batch、长度、采样和评价配置。
- 证据限制：作者只报告所列模型/数学与代码任务/训练配置，未见多 seed 不确定性或独立复现。论文 Figure 7 的最高 1.5× 仅为离线 TorchAO **training-phase** throughput，明确排除周期性 BF16 shadow passes，不可当成端到端 RL 加速；硬件、系统并发与 SLO 未完整披露。Qwen2.5-32B 的熵激增本来较弱；对 sequence-level clipping/不同 objective 的有效性仍是开放问题。论文目前支持该失效路径与受限修复，不证明 FP8 RL 普遍优于 BF16。
- Books 差异初比：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 已写同权重不等于同 policy、quantization graph/scale/kernel 是 rollout identity 的一部分；本篇进一步指出**即使两端统一 FP8**，ratio 的非线性误差仍可改变 clipping/负梯度人口。若准入与独立复核通过，应在 Ch33 现有量化身份段后接续这一压力及校准分支，而非在章末追加论文摘要。`TRAIN-PPO` Ch32 可保留对 token ratio/clipping 的基础机制，不重复 owner。
