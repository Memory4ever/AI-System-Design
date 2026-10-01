# 2604.24885v1 VibeToken：输出像素尺度与 AR latent 长度分责

- 官方首版：[VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](https://arxiv.org/html/2604.24885v1)，本日 arXiv 窄公告批次支持 04/29 08:00 北京归属，仍待本日 first-public 例外和独立日级核；首页 `27 Apr` 是 submitted/首版元数据，不单独作为公开时刻。
- 本核仅 §3–5、Table 1/2/4/5、§K 及真实 Ch23/24 命题；不读全附件、后稿或复现实验。

## 机制与必要反证

传统固定 patch/grid 的 2D 离散视觉表示使 AR 序列长度随输出面积增长；固定格 1D tokenizer 虽短，却不能直接处理任意尺寸。本文 §4.1 把输入 patch kernel 从共享最大 kernel 插值、位置 grid 重采样、短 1D latent 数 `L∈[32,256]` 的训练采样，与按目标 `(H,W)` 自适应的 decoder 分开。§4.2 的 class-conditioned AR prior 另接目标分辨率/aspect embedding，使 **AR latent length 可固定而最终像素尺度可变化**；不是说输出像素、不经 decoder 的全链计算或质量也与分辨率无关。固定 2D grid、单分辨率专用 AR 与另接超分模块仍是不同成本/质量分支。

受限支持与代价：Table 1 小模型 VAE 消融显示 dynamic grid+adaptive patch 的 1024² FLOPs 299→90G、rFID 131.20→5.38，但这不是完整大型模型单因素消融；Table 2 的 64–256 token/rFID 曲线与 Table 4 下游 gFID方向不同。Table 4 在 256² GPT-B/100 epoch 下，64-token generalist 的 CFG gFID `9.37` 差于相同 64-token specialist `8.42`，也差于 LlamaGen `7.15`；§5.2 承认 256/512² specialist 可更好，混合分辨率并非免费。训练只用 ImageNet1k 256–512² 混合，重建外推以 FFHQ 1024²/任意长宽比、生成以 class-conditioned 图像为主；§K 明示未验证 text-to-image、开放词汇或视频。

**精确成本纠错：** 摘要/Introduction 称“恒定 179 GFLOPs inference”；§5.2 及脚注实际定义为 `L=64`、**每个 AR forward step、无 KV cache** 的 179G，整个 64-token 生成成本更高且随 `L` 增长。Tokenizer 编解码仍是独立账：§5.1 给最终 LL 在 1024² 最大约 `1.04T` FLOPs，Table K 给单图 tokenizer 及完整生成的测量秒数；不能用单次 179G 替代整图算力、decoder cost 或并发尾延迟。Table K 0.46s 是其单图实验，并非生产 SLO。摘要 `3.94` gFID 与 §5.2 0.46s 对应的 `3.54` 不是可合并的同一印刷数字；本核不依赖此差值作机制判断。

## 唯一 owner 与处置

已核 [Ch23 Representation Artifact](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)约 235–248 的 `position/order/N/K`、native-resolution/aspect policy、compression ratio、decoder capacity 与 matched-generator rate–distortion–generation frontier；[Ch24 生成管线](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)约 670–675 已明确主生成器与 decoder 成本分账。本文以分辨率与 token 长度解耦的具体受限架构说明既有选择合同的一个实现分支，但尚未给可迁移的部署 admission/fallback 或改变 Ch23 的已有 artifact identity。**不是因它是视觉领域/局部模型而拒绝；是其可迁移设计边界已由 Ch23/24 的具体命题承载，当前没有非同义 Books 增量。**

作者拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard、`No Change — Existing Coverage`，报告中可仅保上述真实机制及成本纠错；不采“生产级”“任意分辨率恒定全链成本”或跨模态一般化。若 matched capacity、固定总体图像质量与完整 decoder/AR latency 的同协议实验显示 `L` 与目标尺度解耦引出 Ch23 未覆盖的明确失效/选择反转，可定点重开。原在 106 完整题摘潜在工作池，作者侧不改 `64+41+1`；待单篇非作者及日期/来源/日 Gate。
