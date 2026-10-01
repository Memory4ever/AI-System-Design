# 2604.20329v1 有界非作者准入、日期与 owner 复核

复核者：apr02（非 04/23 日报作者）；2026-09-28。本文件仅审这一 Source Family，不替代 04/23 来源、候选分母、Books 或日级 Gate。

## 身份与日期

- [arXiv exact-v1 正文](https://arxiv.org/html/2604.20329v1)与[版本页](https://arxiv.org/abs/2604.20329v1)的题名均为 *Image Generators are Generalist Vision Learners*；v1 提交为 `2026-04-22T08:23:48Z`，它不是首次公告时间。官方 [cs.CV 2026-04 月页后段](https://arxiv.org/list/cs.CV/2026-04?show=2000&skip=2000)连续列出 `2604.20328`、`2604.20329`、`2604.20336`（该页序号 2146～2148），但月页未给逐日公告 heading。
- [arXiv 公告规则](https://info.arxiv.org/help/availability.html)指出最终 ID 在公告时赋予，常规周三 20:00 美东公告对应北京时间 04/23 08:00。该 ID 的 DataCite DOI 记录 `v1 Updated=2026-04-23T00:37:04Z`、`created=2026-04-23T02:02:56Z` 与此批次相容；两字段本身不能证明首次公开。连续 ID＋公告槽支持 arXiv 路径的 **04/23 08:00～09:00 有界推断**，不是逐篇精确公告日志。
- [Google DeepMind 官方出版页](https://deepmind.google/research/publications/240658/)可见日期仅 `April 22, 2026`，未展示时区/时分。页面 JSON-LD 虽序列化 `datePublished=2026-04-22T00:00:00+00:00`，恰为午夜，缺少独立的真实发布钟证据，不能将其秒级字面值径直当成该页公开时刻。若它确为较早公开，则最早公开可落在 04/22 日窗；仅凭 arXiv 次日批次不能排除。

**日期裁决：Date Hold。** 不能安全将最早公开归于 04/23 `[09:00 前]`，也不能因网页自然日直接迁到 04/22。此家族暂不进入任一日正式冻结候选分母、评分或 Books；只在获得 Google 页面带可信时区的原始发布时间/可信首发归档，或其他能判定最早公开窗口的官方证据后定点重开。不为此扩扫 Google 全站。

## 贡献准入与 Books owner

旧 `screening-ledger-final.tsv` 的“单领域局部模型/benchmark”泛句不能支持前分母关闭。[exact-v1 §2](https://arxiv.org/html/2604.20329v1#S2)将 segmentation、metric depth、surface normal 分别编码为可解析 RGB 输出，再用任务数据与原图像生成数据混合 instruction-tune Nano Banana Pro；输出图像经任务解析器回到 mask/度量值才可与 specialist 同分母评价。这不是单个视觉任务的局部调参，而是“生成输出协议／解析器／感知评价”职责分离的候选机制。**同意恢复为待日期归属的潜在候选，拟 2+2+2=6 仅代表审阅投入，不是正式本窗评分。**

[Ch23 统一 Pixel-space 段](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)已区分 native shared visual state 与理解/生成各自证据标准，但未具体承载现成生成器经指令微调输出带任务类型和解析规则的 RGB artifact，再以解码 mask/几何量独立验收。若日期与后续证据 Gate 通过，Ch23 是唯一 canonical owner；Ch24 只需生成范式交接，不因论文名称另起机制段。当前没有 Books 写入或已通过的 Books Decision。

[exact-v1 §3 表1～4及§4](https://arxiv.org/html/2604.20329v1#S3)只能支持作者在受测 2D/3D 基准和保留生成能力设置下的局部结果：内部原训练混合/2D 标注与合成 3D 数据不可独立复现；SA-Co/Gold 仅抽 500 queries，ReasonSeg 另接 Gemini 2.5 Pro；实例分割相对 DINO-X 有退步，法线某些集亦非全面胜出。RGB 色码与深度变换的可解析性依赖任务专属协议、颜色误差和额外生成/解码成本；§4 明言当前生成器计算开销高于轻量 specialist，尚未证多视角/视频。因此不能采用“生成预训练普遍优于判别式预训练”“RGB 是任意视觉任务通用真值”或服务成本优势；若后续提 Books，需将解析有效性、几何精度、原图像生成回归和成本分别验收。

本次必要原文与现有 Ch23/24 实际命题的有限非作者复核通过；日期与完整单篇 Evidence/Books 仍未通过，绝非 04/23 日级 Gate。
