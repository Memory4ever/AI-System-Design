# 01/31 首批准入校准（待 root 独立裁决）
窗口：2026-01-30T09:00:00+08:00 ～ 2026-01-31T09:00:00+08:00。
完整原题摘位置：FIRST_ABSTRACT_CALIBRATION.json 对应 id；pMF 的 exact-v1 abstract 原页：https://arxiv.org/abs/2601.22158v1 （在此页完整三段已读，未读全文）。
日期仍需官方公告/metadata复核；API published 是提交字段，不当作首公开。本批不是冻结候选分母。

| 材料 | 作者准入判断 | 具体理由与 owner |
| --- | --- | --- |
| 2601.22156v1 HALO/HypeNet | 拟准入 | 原有 hybrid 转换需较大蒸馏量且长窗质量落差 → layer optimization、HyPE 与结构调整声称在低预算转换保留长窗 → 需要核验转换/长度外推的实际条件，而非仅报告快；MODEL-LONG-CONTEXT。 |
| 2601.22101v1 ECO | 拟准入 | 低比特训练仍保留高精度 master weights → quantization residual 注入既有 momentum 不另开buffer → 需要重考虑 persistent optimizer state 的内存/收敛边界；TRAIN-PRETRAINING。 |
| 2601.22158v1 pMF | 拟准入 | 单步与pixel-space两约束通常分开处理 → 解耦image prediction output与velocity-space MeanFlow loss → 需要核验latent-free单步生成的条件；MULTIMODAL-GENERATIVE-PARADIGMS。 |
| 2601.22128v1 patient JEPA/SFT world model | 排除（已读完整题摘） | 临床疾病trajectory与EHR linear probe的应用研究；ROADMAP明确暂缓AI for Science，不能借world-model owner重新引入医学应用。 |
| 2601.22124 clinical federated LLM | 范围排除（标题明确） | 多机构医学参数高效adaptation，领域应用；不因出现federated/LoRA开全文或全revision。 |
| 2601.22001v1 heterogeneous inference perspective | 准入含糊：需核心定点判断 | 摘要确有CF capacity wall与OI联合lens，但只提出heterogeneity hypotheses；先核它是否新增可判定capacity边界/实测证据还是复述成熟roofline+KV。未定贡献前不扩全文附件。 |

原始宽查询409个metadata只作线索，首200题目浏览并非200候选/摘要审阅。该查询含泛化agent/inference导致领域条目，后续按模型、system、multimodal主线收窄；不把409变成逐项关闭队列。
