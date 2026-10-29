# LOOM：有限持久配对逐字 PRE（未写入）

作者 resume_mar18；只补 2026-03-17。必要原证复用 root 已实际审阅的 exact-v1 §3.1–3.3、§4.1–4.2/Tables1–3、Appendix B/C/D/G，范围见 SUP_ROOT_LOOM_STOP_20261011.md。拟 2+2+2=6；不采用全局最优/唯一 permutation 收敛、免费总训练预算或条件生成保证。

唯一 owner 为 MULTIMODAL-GENERATIVE-PARADIGMS / Ch24；实际端点配对段（当前259–267附近）已有 population prox 与学习后冻结的 forward bridge，却未承载有限训练集配对跨 minibatch 持久更新的状态。拟插在 population OT/prox 段后、forward bridge 段前；以下两段送 root 与非writer 逐字核，不授写锁或 DAY。

端点配对的另一条分支不每个 minibatch 都重新抽独立噪声，而是为有限训练集保存 data/noise 的对应关系，在当前 batch 内按距离重新匹配，并把更新后的全局 permutation 带到下一批。它将 coupling 从一次性采样规则变成持久训练状态；多个 noise cache 可以缓解固定配对的过拟合，但不等于 population OT oracle。当前 batch 的匹配代价不增，也不能推出全局最优、唯一 permutation 或相同代价下映射最终不变；cache、配对身份、随机种子与更新协议应随恢复状态共同保存。<!-- source-family:SF-2026-ARXIV-2603-15279 -->

这种持久配对以索引、cache 与重复匹配费用换更易学习的有限路径，却可能停在小批次次优匹配或对固定噪声过拟合；条件生成还须另验 label-conditional source marginal，朴素配对会引入偏置。[必要方法与直接反侧](https://arxiv.org/html/2603.15279v1)只支持受测无条件图像、网络与 solver 的质量/NFE 取舍，部分数据和 NFE 下原 OT-CFM 仍更好。种子存储不取消配对计算，同 epoch 的训练墙钟也有额外费用，不能从更少求值推出总预算免费或生产延迟改善。质量、条件分布、状态恢复或净成本失配时，独立端点、每批重新匹配与已有 forward bridge 继续合理，不把持久 permutation 静默提升为普遍最优 coupling。<!-- source-family:SF-2026-ARXIV-2603-15279 -->
