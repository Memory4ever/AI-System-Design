# 2604.24952v1 Semi-DPO：扩散时间段偏好标签与代理置信度

本篇属旧 60 完整题摘中的潜在线索，不增加 `106＝70 潜在＋36 具名前闭` 工作集合。仅读[官方 exact-v1 HTML](https://arxiv.org/html/2604.24952v1) §3.1–3.3、§4/Tables 1–5、Appendix 6.2/6.4/6.9 与真实 [Ch34 DPO pair-gradient](../../../../../books/part-04-training-system/34-dpo.md)、[Ch31 preference contract](../../../../../books/part-04-training-system/31-rlhf.md)、[Ch24 diffusion](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 相邻命题。尚未查项目页/代码、版本史和早于 arXiv 的独立首发例外；公告窄链只是当窗身份线索，不代替日期 Gate。

## 贡献准入与真实 owner

单一 winner/loser 在多维视觉偏好发生冲突时会把成对标注写成所有去噪时刻的同向监督；原 DPO 可以在清晰偏好、有效 reference 下继续使用，但此处的问题是**时间段与偏好维度的监督职责不一致**。Semi-DPO 的具体受限分支是：五个预训练 proxy reward 对原标注全体一致者留下约 21% clean anchor；其余当 unlabeled，经 clean-only Diffusion-DPO 冷启后，按 diffusion time interval 对 pair 的 DPO margin 符号重标，绝对 margin 过 interval-specific threshold 才进入下一轮 DPO（§3.3 Eq. 8–10）。这不是一套人类多维真值标签，也不是完全不使用 reward model：显式模型仍用于预处理 consensus，只是训练迭代不再另训一个 reward model。

Ch31 已有标注者/目标身份、异质偏好不能压成单标量、admission 与自举伪标签 provenance；Ch34 已分 `beta`、pair-gradient gate 与 preference truth 的责任；Ch24 已有 diffusion time/state。三章**尚无**同义的“随去噪时刻改变 pair 标签符号与接受阈值，clean anchor 持续保留”训练分支。作者侧暂拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5/9` Standard、`Books：Ch34 可能的最窄条件性增量，待非作者 source→actual owner 核`；若同行证明它只是已有数据 admission＋伪标签机制在视觉 diffusion 的局部 recipe、没有可迁移的选择边界，应转 Report Only，不因“DPO”名称或 Ch34 路由硬留 Books。Ch24 只供时刻语义，不重复展开偏好算法；没有共享 Books 写锁，不能计 Integrate。

## 评价与不能偷换的保证

- Appendix 6.2/Eq. 16 的方差下界是在一个特定 dimension `k`、`Δr_k>0/<0` 二分（证明还用 `p_a+p_c=1`，零差 pair 未涵盖）和作者定义的 oracle 方向下，来自全方差分解的**组间项**。它说明定义下两组更新方向的散度，既未单凭该式证明训练实际发散/收敛至次优，也未证明五个 proxy 对每个维度给出人类真实标签。§3.2 的“数学保证 suboptimal convergence”须收窄成机制动机，不能当训练保证。
- Appendix 6.9 Table 7 在作者的 clean test portion `3,992` pairs 上，timestep 50–550 的二元预测准确率约 71–73%，950 降至 59%；作者据此对 >650 的 interval 提高 threshold。`|margin|` 是模型自身 confidence proxy，非天然校准的人类偏好概率；同一 test portion 被用于阈值调整的披露，不能冒称完全独立最终校准集。训练时序、reward proxy identity 和 interval threshold 必须保留。
- §4 Table 2 的 GenEval overall：SD1.5 `42.34`、Diff-DPO `43.00`、Semi-DPO `47.31`；SDXL `55.63`、Diff-DPO `58.02`、Semi-DPO `58.41`。不是各分项全胜：SDXL `Two` 为 Semi-DPO `80.81` 低于 Diff-DPO `82.58`，`Single` 为 `97.50` 低于 `99.38`；Table 3 亦有 SD1.5 Color `0.471` 低于 InPO `0.482`，Non-Spa `0.310` 低于 Diffusion-DPO `0.312`。只保 SD1.5/SDXL、Pick-a-Pic V2 与所测评估器的受限结果，不称多维人类偏好已被恢复。
- §4.3 Table 4 的 Iter0→Iter1 提升明显、Iter1→Iter2 多数有限；Appendix 6.9 的 `132 GPUh` 是 Iter0＋Iter1，`228 GPUh` 才含 Iter2，对照单阶段 Diffusion-DPO `192 GPUh` 时不能拿两轮质量与一轮成本混用。五个预训练 proxy 的先验训练/调用成本及筛掉数据的覆盖损失不在同一 GPUh 总账；部署模型架构不变不等于训练成本零。

非作者下一步限定为：§3.3 的时间段 pseudo-label 是否真是 Ch34/31 未持有的选择条件；Table 7 threshold 是否用同一 clean test portion 调整；App 6.2 的二分条件和“次优收敛”外推是否需更窄；Ch34 相邻段能否承载而不重复 Ch24。日期、最终候选冻结、整体 Source/Evidence/Books/独立日 Gate 另核。
