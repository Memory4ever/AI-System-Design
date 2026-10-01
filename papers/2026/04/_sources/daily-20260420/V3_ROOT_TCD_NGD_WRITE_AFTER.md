# Apr20 TCD / NGD 实际写后复核

复核者：root，非报告作者、非两处正文写入者。复用 apr02 已实际读取的必要 exact-v1 source→owner 审阅；本次检查真实正文、前后衔接和证据区，不称重新复现或整日 Gate。

- `2604.15383v1`：实际 Ch23 shared-prefix counterfactual 段之后的两段已经解释慢音频参考→同文本历史双路径→音频依赖/不确定性 gate，并紧接模型可见性、speech 退步、双编码/KV 和 prefill 成本。没有把 waveform/state blur 冒称严格等价，或把 logit 差当真值；接“感知到了，不等于行动会使用该模态”不改变 perception/action owner。source-family 标记在机制正文，Review notes 在后且仅保存证据。写后通过。
- `2604.15554v1`：实际 Ch28 聚合梯度/逐样本残差坐标之后两段解释历史函数动量经 cross-Gram 向当前 tangent 投影，再回参数坐标；未称精确 parallel transport。FD 两次 forward、旧导数状态、近似可慢或发散以及非 LLM 通用加速均就近保留，下一段继续估计偏差的责任，没有把不同 optimizer 分支写成替代史。正式题名已核正。写后通过。

两项可据真实正文登记整合；不覆盖 Apr20 的剩余来源、候选、Books 或日级验收。未经复现实验，作者 benchmark 不升级生产保证。
