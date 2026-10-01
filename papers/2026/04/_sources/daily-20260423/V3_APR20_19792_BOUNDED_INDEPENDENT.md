# 04/23 19792 exact-v1 有限非作者裁决

复核者：apr20_resume；作者：root。仅对本窗 [OpenCLAW-P2P v6.0 exact-v1](https://arxiv.org/html/2604.19792v1) 首页身份与 §12.2 Theorem 12.1 的 attention pruning 中央保证作必要核验，并对照 `V3_EVIDENCE_REVIEW.md` 该项拟处置；不读后发 v7 的数学纠正或全篇生态声称，不签本日来源、其他候选或整日 Gate。

**结论：6 分保护性深入、中央保证窄争议隔离 PASS，不作仅报告支持。** §12.2 打印的 `q·k ≤ ||q|| (||b̄||+r_B)` 在 `r_B` 确实包住该 block keys 时是原始 logit 的 Cauchy–Schwarz 上界；这个有限代数事实仍有效。但原文接着说界低于阈值 `θ` 即可 *safely bypass* 整个 block，未说明相对所有未裁剪 logits 的 softmax 分母、删除概率质量、value 范数或输出误差。取 `q=0`、非空多个 key blocks、正阈值 `θ>0`，所有上界与 logits 均为0而落在阈值以下；原 attention 仍是均匀分布，删全部 block 会使输出未定义。即便实现强制保留一个 block，令两个 block values 分别0与1，原输出为1/2，保留其一会变为0或1。故“raw-logit 上界→安全 normalized-attention/output 裁剪”的无条件推导不成立；不由此断言实际代码一定逐块删光、Lean 证明文件内容为何，或所有稀疏 attention 实现无效。

只隔离这项全输出 safety / complexity guarantee 的推理，不抹去已打印的 raw-logit 界、其他可独立核的存储/引用流程或有限平台观察；它们仍须按各自证据处置。重开该保证只需 v1 同一对象上的阈值/至少一块保留规则、softmax-tail mass 与 value-weighted 输出误差界，或相应可核实现/定理条件；无需全版比较或复现整个平台。v1 首页正式题为 *OpenCLAW-P2P v6.0: Resilient Multi-Layer Persistence, Live Reference Verification, and Production-Scale Evaluation of Decentralized AI Peer Review*，不能以当前 raw 的后发 v7 标题/纠正叙述替代。日期归属与其他贡献仍由日报作者独立收口。
