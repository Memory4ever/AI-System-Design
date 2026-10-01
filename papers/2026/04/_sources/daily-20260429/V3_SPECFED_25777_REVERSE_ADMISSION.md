# 2604.25777v1 SpecFed：受限机制与印刷保证反证的贡献准入

这是 04/29 作者侧 V3 逆向准入，不是非作者单篇或日级 Gate。[官方 exact-v1 身份/完整题摘](https://arxiv.org/abs/2604.25777v1)以 *SpecFed: Accelerating Federated LLM Inference with Speculative Decoding and Compressed Transmission* 为题；v2 于 07/04 才有，以下只用[官方 exact-v1 HTML](https://arxiv.org/html/2604.25777v1) §II–V 的决定性段落。其 arXiv `submitted=04/28T15:44:50Z` 不当首公开；ID 位于本日已有的官方公告相邻窄链内。由于下述贡献前闭，不为排除再追 ISIT 会议及其它可能更早公开的小时。

§II 的确有具体条件：同词表的两个以上 worker 各出完整概率分布，服务器按权重求和，再按小模型草稿作 rejection/residual sampling；每个草稿位上传整词表会增加低带宽通信。§III 只传各 worker top-K token/probability 后，服务器或对 top-K 重新归一，或把余量均摊给被截掉的 token，再聚合。这个恢复改变了原本的 ensemble target distribution；不是 classical exact speculative sampling 对原 target 的分布无损加速。§IV 对局部 L1 误差及聚合误差给余量界，§IV-C 的正确推导可给单步 acceptance 差异不超过加权遗失概率质量。若将来采用此路径，必须分别记原目标分布、重建目标分布、单步 acceptance、完整生成质量和通信/端到端 wall-clock，而非称 top-K 仍精确。

原文中央印刷表述有一个**可局部隔离**的数学反例：Theorem 3 式 (19) 写 `Δα ≤ Δ ≤ Σ wᵢ εᵢ`，但 Theorem 2 式 (17) 和它自己的证明式 (20) 是 `Δα ≤ ½Δ ≤ Σ wᵢ εᵢ`。取单 worker、词表二元、`p=(0.9,0.1)`、K=1，重归一得到 `p'=(1,0)`，故 `ε=0.1`、L1 `Δ=0.2`，直接违反印刷式 (19) 的中段 `Δ≤ε`；不推翻式 (20) 的较窄 acceptance 界，也不证明实际代码或图表错误。§V-B 还把 K=320、|V|=32,000 同时说成 0.1% 和 1%，实际是 1%；并把 Lemma 1 对两种 reconstruction 的等号/不等号描述倒置。故不能照录所谓「stable decoding efficiency」为端到端保证。

实验证据只在 §V-A 的两 worker LLaMA-7B/13B、服务器 LLaMA-68M、A800 模拟、wmt14_ende_de、权重各半和相同 K；§V-B 计算沿未压缩生成序列所得的 token 分布/单步 acceptance 偏差，没有给完整采样轨迹的任务质量、通信 RTT 下的 wall-clock 或生产吞吐。§IV 脚注明言端到端通信成本、吞吐和最终生成质量分析留待未来。本文有局部方法与可诊断的数学排版错误，但不足以独立建立超出既有合同的跨部署新机制。

真实唯一相关 owner 是 [Ch48 Speculative Decoding](../../../../../books/part-05-inference-system/48-speculative-decoding.md)：约 95–140 行已明确 draft `q`、target `p`、exact acceptance/residual、lossy verification 变更目标分布，以及 acceptance/quality/goodput 不可混用；后文还要求跨网络成本验收。SpecFed 的多 worker 加权 top-K 是这个已有边界的受限实例，中心反例只是其印刷式 (19) 缺失 `½`、并未推翻 Ch48 合同。作者侧对旧 60 的潜在线索作**具名前分母关闭**，不评分、不写 Books；不是因「联邦」「小模型」或负面结果硬拒。若有真实多 worker 网络/请求分母表明聚合重建引出 Ch48 尚未覆盖的可靠选型或 exactness 失败条件，再按独立证据重开。此前题摘潜在线索已计在同一 106 工作集合，这次只作 `潜在 −1 / 前闭 +1`，非正式冻结分母、非日 Gate。
