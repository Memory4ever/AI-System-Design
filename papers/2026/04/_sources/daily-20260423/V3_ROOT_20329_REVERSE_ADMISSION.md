# 04/23 Google DeepMind / arXiv 2604.20329v1 反向准入

作者：root；2026-09-28。此条只纠正贡献筛选，**不是**确认首次公开落在 04/23 的 09:00 截点内，也不是 Books / 日级 Gate。

## 身份与来源

- [Google DeepMind Publications 原文](https://deepmind.google/research/publications/240658/)将 *Image Generators are Generalist Vision Learners* 列为 2026-04-22，未给时区或时刻。
- [arXiv:2604.20329v1](https://arxiv.org/html/2604.20329v1) 是本次采用的原始正文；[版本页](https://arxiv.org/abs/2604.20329v1)给出 v1 提交为 2026-04-22 08:23:48 UTC，**提交不能充当公告/公开时刻**；后续 v2/v3 不能回填 v1 主张。论文当前官方撤回标记未见，但须在最终候选冻结前复核。
- 旧 `screening-ledger-final.tsv` 把它以前分母的通用“单领域/局部模型/benchmark”理由关闭；这个理由未审查原始摘要中提出的统一输出接口，故该关闭不能原样继承。

## 为什么需要重开准入

原路径为理解任务配置专门 encoder/head/loss，而图像生成器负责视觉样本。v1 §2 把 segmentation、metric depth、normal 的目标编码为**可逆或可解析 RGB 图像**，以相同 image-generation 输出通道承载多种感知任务，再用少量任务数据与原生成数据混合 instruction-tune 既有 Nano Banana Pro。设计问题从“能否生成像图的答案”变成“统一输出协议能否使生成模型同时承担可测感知”。这可能改变 Ch23 的表示/输出 identity 与 Ch24 的生成—理解交接，因此满足项目主线**潜在**增量；仅有 cs.CV 标签、章节映射或厂商名本身都不是准入依据。

证据上限同样明确：§3 的 2D/3D 基准和表 1–3 是作者报告；部分比较使用不同 specialist 与任务协议，SA-Co/Gold 只随机抽 500 queries，ReasonSeg 还接 Gemini 2.5 Pro。§2 使用未公开的原始训练混合、内部 2D annotations 与合成 3D 数据，没有“同样 task data、从零训练或另一生成 backbone”的充分因果对照；故不能把其结果写成“视觉生成预训练普遍优于判别预训练”或“RGB 是任意视觉任务的通用真值接口”。像素色码解析、颜色偏差、生成成本及精度误差需与专用 head 的质量/时延分开验收。作者还承认 instance segmentation 不是对所有 specialist 最优。

**工作裁决：恢复为待日期归属的潜在候选**，暂拟 Design Delta 2、System Reach 2、Durability 2，合计 6/9，仅是审阅投入建议，非正式本窗分数。需要非作者按贡献阈值、Ch23/24 现有具体论点和 exact-v1 的证据上限复核；若仍应关闭，必须用上述机制/对照的具体理由，而非原通用句。若获准入但无法独立核定首次公开窗口，放入日期缺口，不虚列 04/23 正式候选。Books 尚未修改。
