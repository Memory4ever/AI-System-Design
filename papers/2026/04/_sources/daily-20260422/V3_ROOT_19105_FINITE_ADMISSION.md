# 04/22 19105 有限非作者准入复核

复核者：root；2026-09-28。仅审这一 Source Family 的贡献准入，不代表 04/22 整日来源、日期或 Books Gate 通过。

[EgoMotion exact-v1](https://arxiv.org/html/2604.19105v1) 的 §III 与 §IV-D1 将 PaliGemma-2 对 RVQ-VAE motion tokens 的监督、冻结 VLM hidden states 条件化 latent diffusion 分成两阶段。Joint-Tuning 的生成质量/物理指标弱于分阶段方案，但语义对齐反而最好；这支持**该任务下的质量—成本取舍**，没有直接量测两个 loss 的梯度内积或单独排除训练预算、监督接口等替代解释，不能把作者所称梯度冲突写成已证实因果机制。

[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 已有共享 semantic interface、独立 generation head、分阶段冻结/解冻与 loss ratio 的条件分支。此稿新增的是第一视角人类运动生成的局部实现与评价，未改变该长期选择或提供新的接口责任/评价合同。因此同意作者将 19105 从 04/22 正式候选降为 family-specific 前分母关闭，保留已读证据，不评分、不写 Books。若后续有受控梯度诊断或不同任务下可复现的失效边界，再定点重开。其他候选及负侧抽样仍待独立复核。
