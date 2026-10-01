# 04/24 Ch23 两项非作者写后复核

复核者 root；2026-09-28。仅复核已经实际写入的 `SF-2026-ARXIV-2604-21326` 与 `SF-2026-ARXIV-2604-21079`；不代表 04/24 整日 Gate 通过。

- MiMIC：[精确 v1](https://arxiv.org/html/2604.21326v1) §3–5/A.3 与 Ch23 的 fusion point、后续多模态 ICL / Ch76 handoff 对读。正文 272–274 讲独立编码、decoder 分别跨读、single-modality mix-in 和 caption dropout 的缺模态训练支持；保留纯文本切片退步、ratio 调参成本和受限数据集，未把检索排序当融合的固有保证。原文 Table 4 与 §5.5 支持此窄机制，不支持所有 workload 上的 FiD 普适优越性。身份未混入 `2604.21343`。实际写后 PASS。
- Foveated Reasoning：[精确 v1](https://arxiv.org/html/2604.21079v1) §2–4、Eq.15 与 Ch23 旧静态/active-observation 段及下段 reliability Gate 对读。正文 418–420 把离散观察动作、连续 box、crop 重入轨迹与 correct-only 面积正则接到旧方案边界；明确新 KV、路径依赖、单图与错误区域风险，不把更小 crop 视为证据充分。原文 Eq.15–16 和受测任务支持此机制方向，不证明视频或生产 tail。实际写后 PASS。

两项 Review notes 均在章末，没有机制正文落在 Review notes 之后；`git diff --check -- books/part-03-multimodal-world-models/23-multimodal-representation.md` PASS。尚未复现实验；日报状态须与此独立写后结果同步。
