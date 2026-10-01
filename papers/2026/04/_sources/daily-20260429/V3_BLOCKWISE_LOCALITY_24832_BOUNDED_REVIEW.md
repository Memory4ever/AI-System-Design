# 2604.24832v1 Blockwise Locality：生成依赖方向不是固定块定义

本项从[第一批完整题摘逆向准入](./V3_REVERSE_TITLE_ABSTRACT_BATCH1.md)恢复为潜在；本次只读[官方 exact-v1](https://arxiv.org/html/2604.24832v1) §3.1–3.3、§4.1–4.4、Appendix A.1–A.3 的决定性方法/主对照与实际 [Ch24 Block Diffusion 段](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。并非第二个家族，未遍历全部附件或复现实验。

## 原文能支持的增量

Ch24:435–449 目前把标准 block diffusion 解释为「块间因果、块内并行修订」，并在该约束下讨论 block size 与 commit。本文提出**反向分配局部性**的受限分支：Scatter 在各块的相同 offset 同步生成，attention mask 只看更早 offset 与自身；每个 offset 内仍可多步 unmask，并非一次 forward 生成所有块。Jigsaw 先以非破坏性 forward 估计未完成块的平均 token entropy，贪心选一块，再在块内 AR／细粒度 diffusion 生成并固定该块；训练时用 block independence mask，未提交块互不可见。因而两者不等价：Scatter 是跨块同步 offset 顺序，Jigsaw 是按低熵选择并逐块 commit；**不能笼统写成块间任意反复改写已提交块**。这确实改变了「局部依赖必须由块间因果承载」的设计假设，而非仅调大/调小 block size。

受控反证有方向性：ICL 线性回归 20 demonstrations + 20 queries、`d=10/15/20` 中 AR 与 Jigsaw 近零 MSE，Scatter 部分改善、标准 MDM/固定块在 `d=20` 失效；反向依赖的 star-graph 路径则 MDM/Scatter/Block 约全对，Jigsaw/AR 约 `0.2`，Jigsaw 缩到 block=1 才恢复；Sudoku 中 MDM/Jigsaw 近全对、AR 为零、Scatter 约 `85%`，且坐标嵌入是任务拓扑条件。这些共同说明局部左到右归纳偏置可以帮助精确绑定，也可能阻断反向因果链，不能宣布任一范式普遍胜出。

自然语言证据比摘要的三玩具任务多一步，但仍很窄：§4.4/表2 在 LM1B、110M、128 context、bert-base-uncased tokenizer、BD3 原 codebase 匹配超参下，Scatter 对作者重跑 BD3 在 block `L=4/8` 的 PPL 为 `32.10>28.20`、`30.50>29.70`，在 `L=16` 才为 `27.10<32.90`；与 BD3 论文报告最佳 `28.23@L4` 横比也必须标明不同运行。350M Scatter `26.58@L16` 没有 matched 350M BD3。AR baseline 与 masked/bidirectional baseline 虽参数和各任务训练数据/预算相配，但 attention 可见性与目标不同，不能把差值全归单一 mask；Jigsaw 未纳入 LM1B matched codebase 对照。§3.3 的 `O(L)` 是 high-fidelity `T≈L` 假设下 NFE，Jigsaw 另付每块 probe；非 FLOPs、wall-clock 或在线 SLO。

## 作者侧处置与日期

贡献入口是 Ch24 当前固定「块间因果/块内修订」叙述之外的**依赖方向与训练 mask 共同选择**，拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard；因实际 Ch24 缺这一反向分支，Books 若采用需按真实 gap 补足必要深入审阅与非作者 source→owner Gate。拟唯一 owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Ch20 sampling 仅管一般 commit/预算，不重复持有训练 factorization。可在 Ch24:449 后用两段说：标准路径仍适合可流式提交的左到右块；若任务依赖更偏 token-local binding，可将局部 AR 放入块内、跨块用受约束的同步 offset 或低熵选择，连同训练 mask 与 commit 顺序一起版本化；反向路径规划/全局约束又可能需要不同可见性。第二段需保上述任务、LM1B matched 与反退、NFE≠时延、无大模型/长文/生产 SLO 证据，不写「扩散全面优于 AR」。**这只是待独立核与共享锁的正文提案，不是已整合。**

日期分账：官方 exact-v1 页眉 `27 Apr 2026` 是提交版本日期，不能独证公开；本日 arXiv 相邻公告/ID 联合链支持 `2604.24832` 于 04/29 08:00 北京批次公开，落 `[04/28 09,04/29 09)`。作者[代码仓库](https://github.com/stein-wang0226/trainable-masked-diffusion) API `created_at=2026-03-11T18:06:15Z`，03/18 固定[提交 `21053816`](https://github.com/stein-wang0226/trainable-masked-diffusion/tree/21053816a4cbe99b202719c777f957c1fde0d7fc)的 README 已有同家族近似标题、Scatter/Jigsaw 与 ICL/Sudoku 概述，但仓库当时公开可见性未知，且该树无完整论文 PDF/TeX；这证明早期代码 artifact 内容存在，不证明论文正文当时已首发，也不能把 repository created 单字段当作首公开。此处**论文正文**按本日公告待独立日期 Gate；若取得早期公开完整正文，应重新归属/去重。原在 106 篇已读题摘的潜在项中；24801 后续日期反查后最新工作账见 checkpoint 页首 `62 潜在+42 前闭+2 已证早公开隔离`，本篇未改变账目；未签正式候选、Books 或日 Gate。
