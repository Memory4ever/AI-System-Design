# 2604.24953v1 ViPO：贡献准入与必要证据有界核（作者侧）

本项属于当前 `106=71 潜在+35 前闭` 的 **71 内一项**，不是新增 raw／候选，也不继承旧 V2.1 的 8 分与 Books 处置。官方身份为 [ViPO: Visual Preference Optimization at Scale](https://arxiv.org/html/2604.24953v1)。本次仅读 exact-v1 §3.2、§4、§5.1–5.4、Appendix F 的决定性机制／实验／限制，并对照现有 [Ch31 偏好数据与目标](../../../../../books/part-04-training-system/31-rlhf.md)和 [Ch24 扩散生成](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)的相关段，不展开引文史或全部附件。日期仅复用本日官方公告原始窄批次链，仍须在正式冻结时排查更早的独立公开版本。

## 具体贡献判断

旧判断不能只看“新 1M/300K 数据集或更高生成分数”。同一视觉偏好训练流程里，若偏好对存在多目标冲突，普通 Diffusion-DPO 的 winner/loser 信号可能与易区分或高质量平衡数据处于不同的更新区间。作者的 Eq. 9–10 将 `−log p` 加 `α(1−p)`，梯度相对标准 DPO 多 `1+αp` 因子；在 Pick-a-Pic V2 的受测偏好冲突上选择正 α，在人为 batch 内乱配 loser 的简单偏好上选择负 α，而 SFT 后 ViPO-Image-1M 的最优 α 接近零。它至少给“何时用复杂 loss、何时回退普通 DPO”一个可核的**数据条件×目标函数**局部反例，不仅是数据量榜单；所以作者侧暂保受限候选，拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`、Standard。

但 `α` 由网格搜索选定，不是原文已交付的在线自适应控制器。Eq. 10 的乘因子随 `p` 增加，不能按“正 α 一概下调高置信样本”复述；完整梯度还乘 `(1−p)`，两者要分账。§5.2 的三种数据状态并非同一真实样本池上只改变噪声的随机干预：Pick-a-Pic、batch-shuffled loser 的合成简单样本与另建 ViPO 集合同时改变生成模型、标注、分辨率、prompt 及训练前 SFT，因此 `α≈0` 是该设置的经验选择，不能反向证明 ViPO 标签已接近人类真值，亦不能把 dataset quality 判为唯一因果变量。§5.2 的冲突率 `20.79%` 是五个 reward model 对 pair 排序同向的比例，不是人工偏好错误率。作者 Appendix F 自承 VLM-only labels、未作大规模人类相关验证、α 搜索开销及构建成本。

§5.3 Table 2 给 SD1.5/Pick-a-Pic V2 相同评价设置下 Poly-DPO vs Diffusion-DPO 的局部优势；表注又说明若干 baseline 是官方已发布 checkpoint，不是所有方法在统一训练预算重训。§5.4 Table 4 的 ViPO 组合同时含 SFT 与 Poly-DPO，不能把最终提升全部归因于 `α` 或单独数据规模；同表 FLUX 的 SFT 计数反退、颜色等子项也非齐升。论文 §4 说 300K video pairs，但首版 Table 1 的 “Ours” video 一行写 30,000 pairs（且 30,000 prompts、60,000 videos）；不能未经确认用此表计算视频数据规模或跨数据集成本比。这是**表内身份/数量矛盾**，隔离受影响的规模保证，不吞掉 §5.2 的 image α 分支证据。

## 实际 owner 与作者侧处置

Ch31 已要求偏好数据质量、reference、目标和独立 held-out 结果分账；Ch24 承载 diffusion 生成及其 reward 更新的概率接口。两章未逐项写 Poly-DPO 这个局部损失配方，但现阶段的受限实验还不能把 α 当可迁移的自动噪声诊断器或新训练平台合同。拟 **Report Only / Books No Change**，而非因已有章节就前闭：可保留“在所测视觉偏好设置，较复杂目标函数的收益依赖 pair 质量，数据改善后标准 DPO 可能仍足够”的窄判断。真正独立复核需检查：(1) α 的符号和梯度解释；(2) §5.2 三组是否足以支撑值得保留的条件反例；(3) Ch31/24 是否已承载此判断；(4) 视频 pair 规模印刷矛盾的隔离边界。非作者未核，不记正式候选、Evidence 或日级 Gate 完成。
