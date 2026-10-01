# 04/20 两项中央保证：有限非作者审阅

复核者：root；日报/必要原文审阅作者：apr20_resume。复核日期：2026-09-28。只复核两个争议命题、支持它们的印刷方法与相邻实验以及实际 Books owner，不代签整日 Gate。

## 2604.15780v1 Pruning Unsafe Tickets

[官方 exact-v1](https://arxiv.org/html/2604.15780v1) §2.1–2.4 先用目标模型的 safe/unsafe response 与外部分类器采样，借 masked Wanda attribution、组件比率和逐步 mask 搜索提案，不证明存在唯一“unsafe subnetwork”。§2.4 的 beam 目标印为 `L = CE_safe − CE_unsafe`，紧接着说保留**最高** `L`；若希望 safe CE 降、unsafe CE 升，应选更低 `L`。例如 `(CE_safe, CE_unsafe)=(1,4)` 给 `−3`，`(2,1)` 给 `1`，打印选择后者正逆转叙述目标。该反例只针对 beam 印刷目标/排序，不能推出实现必同错，也不取消 greedy 结果。

作者 Table 1 的 beam over-refusal 46 对 baseline 22.7，utility 7.13 对 8.07；部署无额外生成 token 不等于 mask 构建无时间/显存成本。对照 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 的变换后 artifact 独立安全验收和训练/运行时责任，论文不提供可安全放行所有模型的通用剪枝合同。认同 `2+2+2=6`、仅 beam 中央方向保证 `Disputed/Books 暂缓`；greedy 和受限实验保留为受限 evidence。重开要求同版目标符号、排序及实际选择代码/说明，不要求重审无关攻击集。

## 2604.16067v1 AEGIS

[官方 exact-v1](https://arxiv.org/html/2604.16067v1) §3–4、Algorithm 1 中先用参考 VQA 样本建立各层 Gaussian activation anchor，再对动作 flow loss 与 Wasserstein anchor loss 分开 backward。若两梯度点积 `d<0`，Eq.12 用 `α=d/(||g_ot||²+ε)`，Eq.13 用 `g_final=g_task−α g_ot`；直接代入得到 `〈g_final,g_ot〉=d ε/(||g_ot||²+ε)<0`，并不等于 Eq.14 的严格零。这个代数反例只隔离精确正交/零破坏保证，不证明代码必有更严重错误，也不否定有限遗忘缓解。

§6.5 的 PaliGemma2-3B-Mix-224、LIBERO 动作训练后 5k OK-VQA 评估为 pretrained 60.15、AEGIS 60.23，微差不能单独证明动作能力与参考语义均无损；§7 披露额外 backward 与约 40% wallclock 成本。对读 [Ch30](../../../../../books/part-04-training-system/30-lora.md) 的适配/遗忘分支与 [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的物理 action/safety 边界，不把 activation anchor 当全面知识或部署安全 owner。认同 `2+1+3=6`、精确正交中央保证 `Disputed/Books 暂缓`；保留有限 VQA/专家误差结果。重开需 ε 及零范数分支的同版修正式、实现与严格几何保证一致说明。

两项均是具名有限独立 PASS；不是来源覆盖、负侧召回或 Books 日级 Gate。
