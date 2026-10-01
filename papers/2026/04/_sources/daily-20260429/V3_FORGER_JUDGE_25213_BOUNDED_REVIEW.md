# 2604.25213v1：同域传统篡改校准不能担保生成式局部编辑检测

- 官方首版：[When the Forger Is the Judge: GPT-Image-2 Cannot Recognize Its Own Faked Documents](https://arxiv.org/html/2604.25213v1) §3–6、Appendix A/B/D/E。本文属于本日 arXiv 窄公告批次的身份线索；仍需本日 first-public 例外和独立日级 Gate，不能用 `submitted 28 Apr` 单字段签发。
- 安全用途只记录检测/评价边界，不转载文中的文档伪造生成提示或操作配方。

## 机制、主实验、直接反证

同为收据/表单域，传统 cross-camera splice 与 OCR token splice 的受测检测器 AUC 分别为 TruFor `0.962`、DocTamper `0.852`；换成该研究的 GPT-Image-2 局部生成编辑后是 `0.599`、`0.585`。这说明**同域校准不能替代篡改机制切片**：前者依赖可见 sensor-noise 或 JPEG-history 不连续性，生成式重绘/输出处理可能改变证据通道。§5.2 Table 5 还显示相同 v2 中 TruFor 主要在 WildReceipt 有信号 `0.791`，而 PDF-rasterized XFUND 为 `0.500`；来源载体和攻击方式都要入 EvalSpec。

本文 v2 从 4,062 个继承 specs 形成 3,066 对成功样本，约 24.5% 未进入测试且主要因 provider 接受尺寸限制（§3.3）；人工只在小的收据切片做 120 位非专家/365 次 2AFC pair-votes，不能从 `0.501` 推断所有专业鉴伪者或所有文档均无辨识力。三计算系统对 3,066 forged＋3,066 authentic 作成对评分，但“自身模型”只返回单次二元 yes/no；Appendix D 明示其 `AUC=0.532` 代数上是 **balanced accuracy**，不能与连续分数的 TruFor/DocTamper AUC 直接当同一排序质量指标。其 6.8% ambiguous 输出在 Appendix E 的填补假设下为 `0.500–0.568`，主表过滤 `0.532` 不是缺失无偏估计。五种 prompt 仅 50+50 的小切片且解析率不同，不证明任何 prompt 都无法改善。

§5.4 的两传统校准集是分别为检测器训练机制构造，和 v2 的 inpainting 还同时不同于 splice/compositing/re-encoding；因此结果支持“这两种传统信号在当前 GPT-Image-2 样本上不稳”的受限判断，不能把 `0.27–0.36` AUC 差全部归于单一 generator 因果。§3.3 的 3,062 个旧 v1 同 spec 配对有助控制源图/目标字段，但 Appendix B 说明新旧 mask/prompt/output processing 不完全相同。作者 §3.4 将持续相同的 providerInternalError **推断**为未公开 safety classifier，不能把它写成官方实现事实或政策覆盖保证。

## 真实 owner 与作者侧处置

已对读 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)约 193–200 的 evaluator identity、约 720–744 的 deterministic/judge authority、约 3650–3665 的 detector revision/reference distribution/threshold/FP-FN，以及 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)约 1690–1710 的模型/judge 不获 effect authority。本文提供有价值的“来源载体 × 篡改机制 × detector revision × prompt/parse state”局部反证，但 Ch66 已要求 detector 的 reference distribution、阈值、误报漏报、verifier authority 和原始 outcome 身份；Ch72 已明确自判并非安全证明。没有提出新的检测器或改写这些 owner 的长期 admission/fallback。AIForge-Doc v1 已建立传统→生成式 inpainting 的总体检测落差，v2 对新模型、自审与同域校准作受限增强；不按新模型名自动创 Books 段。

作者拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard、`No Change — Existing Coverage`；日报只保有界评价纠错与分母，不采“生成器必认不出自己”“全部视觉取证已失效”或 provider 内部政策推断。原在 106 完整题摘潜在工作池，不改当前 `64+41+1`，仍待单篇非作者、日期/来源及整日 Gate。
