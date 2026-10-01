# Apr20 TCD / NGD 有限独立采用复核

复核者：apr02（非作者、未写本次 Books）。本次实际读取当前 AGENTS、研究/Report 合同、Daily 来源与 ROADMAP；复用已读必要原文和当前 owner 的未变上下文，未复现实验，不核全日日期/来源 Gate，不遍历附件。作者提案见 [两项 owner 包](./V3_TCD_NGD_OWNER_PROPOSALS.md)。

## 2604.15383v1 — Temporal Contrastive Decoding

必要原文：[官方 HTML v1](https://arxiv.org/html/2604.15383v1)，实际 §3.1–3.4/Eq1–9、§4.5 Tables4–5、AppendixB Table7；对读 Ch23 writer/read-path、shared-prefix late counterfactual branch 至“感知到了，不等于行动会使用该模态”的实际正文及交接。该处已有模态干预原则，但未承载保留粗音频语义的慢时间尺度参考、以及干预能否被 decoder 访问的架构条件。

waveform 平滑后重编码 E(Kx) 与 Eq1 的 latent-state 平滑描述不能冒称严格等价实现；同一文本 prefix 下的原/慢路径、正残差、小候选 union 与音频依赖/熵 gate 是受限机制。Table4 的噪声参考、去 gate 与 signed 对照及 Table5 的分离编码架构退步支持选择条件，不证明声学真值或语言 prior 消除。采用提案对这一边界表述准确。

成本必须区分主实验 4×A100 40GB 与运行时单 A800 80GB、eager attention、3 秒音频/100 token、优化复用原路径 KV 的测试。Table7 prefill 2.04×、decode .99×、memory 1.01× 仅该配置；batch2 decode 隐藏部分增加不是全服务零成本/SLO 保证。两路编码/KV 与平滑损失、架构可见性及 speech/强模型退步已在拟稿就近保留。

裁决：2+1+3=6，具体知识缺口深入；source→owner 窄采用通过。唯一 owner `MULTIMODAL-REPRESENTATION` / Ch23，插入点与相邻 Ch22/24 的责任交接成立。可以写两段受限条件分支，尚未真实写回，不计 Integrate 或日 Gate。

## 2604.15554v1 — Natural gradient descent with momentum

身份纠正：官方 v1 标题为 **Natural gradient descent with momentum**；作者包小标题是解释性转述，正式引用应改用官方标题，ID/机制不因此失效。

必要原文：[官方 HTML v1](https://arxiv.org/html/2604.15554v1)，实际 §4.2.1 Eq24–28、§4.2.2 Eq29–30、§4.2.3 Eq31–33、§5.1–5.3；对读 Ch28“聚合梯度与逐样本残差是不同的更新坐标”至共享 Batch 的 preconditioner 估计语义段及 Ch27/29 交接。现有伪逆残差坐标只定义当前步；历史函数动量跨变化 tangent 的重新表示确有独立缺口，而非将参数动量改名。

旧函数动量用 cross-Gram 向当前 tangent 投影，再用当前 Gram 逆/伪逆求参数坐标，不能称精确 parallel transport。QNHB 直接复用旧参数动量依赖近似恒等映射条件；FD 以两次 forward 的函数差减少旧 Jacobian 状态，不是免费或无误差。Gram regularization/谱截断与有限估计引入稳定性成本。

小型 Mackey–Glass/XOR 对照只支持该受限实现：迭代减少不等同 wall-clock，FD/QNHB 可慢于 exact，Nesterov 近似可能需降低 β，line-search 少迭代却更慢；没有大模型随机 minibatch/HPC 普遍收益证据。不读 PDE 领域附件也不把其应用恢复进当前范围。

裁决：2+1+2=5，具体知识缺口深入；source→owner 窄采用通过。唯一 owner `TRAIN-PRETRAINING` / Ch28，在当前残差坐标之后插入历史坐标变化/代价两段合理，SGD/AdamW 或无动量 NGD 回退与旧方案成立条件均保留。尚未写回，后续必须实际 body+邻接非作者写后复核；本文件不代表 Books 或整日完成。
