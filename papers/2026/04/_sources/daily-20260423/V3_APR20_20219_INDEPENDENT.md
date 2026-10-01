# 2604.20219v1 有界非作者 Evidence→owner 核

审阅者：apr20_resume；04/23 作者：root。本核只读[root 单篇提案](./V3_ROOT_20219_FINITE_EVIDENCE.md)、[官方 exact-v1](https://arxiv.org/html/2604.20219v1) 摘要、§1.1–1.2、Theorem 2.1、Corollary 2.2–2.3 与紧随的 Remark，并对读实际 [Ch4](../../../../../books/part-01-worldview/04-why-models-learn.md) 表示能力／UAT／Depth Separation 与 [Ch5](../../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 中间表示、readout 与实际使用的相邻论证。未读证明全篇、附件、其他版本；不签首公开日期、04/23 整日 Gate，也不写共享 Books。

**结论：窄 PASS。** 原文给特构、固定宽 `2dN+d+2` 的两 sine 通道＋其余 ReLU 通道网络；每一级 `Φ_l` 是保留先前项的前缀计算加仿射读出头，不是 raw hidden state。Theorem 2.1 的 `L^p` translation-modulus 上界与 Hölder 条件下的几何收敛使“只保证最终输出”的一般近似说法多一个可保留的条件化替代构造，故有超出章节名映射的理论增量。`2+1+2=5` 标准审阅合理：设计差额来自逐层可读出的构造及残差保留，系统关系只到单个网络的表达层，不是训练—推理跨层证据；长期性仅限该条件式表达认识。不能给更高系统 reach，也不因没有 Transformer 实验硬拒理论结果。

**Ch4/5 比较与 Books：**Ch4 现已把函数族存在性、梯度优化、泛化分账，并说明 UAT 不回答参数／数据／实际可达；Depth Separation 只在特定函数族谈深浅表示效率。Ch5 已区分 hidden state 的可读出、模型真实使用及受控行为。两章并未把“每个前缀附读出头都有 `N^{-l}` 尺度上界”写成普通网络属性；本篇的特构结果可以在日报作为这个区别的受限实例，但尚无证据使一般 LLM/Transformer 深度选择、训练策略或发布 Gate 改判。root 的 **仅报告、Books No Change** 有具体 owner 对照，不把整套特构强塞入 Ch4 通用主线，也不误称完整算法 `Existing`。

**保留反证：**§1.2 明说混合激活不继承纯 ReLU MGDL 的实际误差逐级单调保证；定理是存在性上界随级数收紧，不是任意训练轨迹实际 loss 单调。Corollary 2.3 的参数数只计实数仿射系数，Remark 明确未控制权重幅度、两 sine 解码器位精度、数值稳定或训练复杂度。不能从 `Φ_l` 误推 raw hidden state 已有 certified accuracy，也不能推 Transformer、PDE 以外任务或部署 SLO 的有效收益。root 单篇提案已保这些边界，未见需修正的中央事实；此 PASS 只及上述必要原文、5 分准入与实际 Ch4/5 处置。
