# Apr20 original eight — 有界非作者准入校准

复核者：apr01；报告作者：apr20_resume。本次实际重读当前 AGENTS、研究/Report 合同、统一入口、每日来源/arXiv 路由与 ROADMAP；读取原始 `20260420/arxiv-owner-receipt.json` 中八项完整题摘，并定点重开下列官方 exact-v1 必要内容。只裁决贡献入口及决定准入的边界，不验收本日日期、全部来源、Evidence 完成、Books 采用或日级 Gate；没有修改 Books 或作者正式报告。旧泛化标签未作为否定依据。

## 15351 — Aletheia

[官方 v1](https://arxiv.org/html/2604.15351v1) §3.1–3.5、§4–6 的已实际必要阅读可复用。准入通过：adapter 不必每层执行，短梯度画像按 layer chunk 选子集，为微调成本与任务相关性提供可检查的局部执行分支。跨模型主对照 rank16，与单模型 asymmetric-rank recipe search 分开；没有同数量随机/深度选择对照，不将收益唯一归因于梯度排序。200-step 与 compute-matched 结果不能混成同预算因果结论。可按作者拟 2+1+2=5 标准审阅；不因“层选择已有主题”关闭，不据初筛核准 Books。

## 15414 — TeLAPA

[官方 v1](https://arxiv.org/html/2604.15414v1) §3–3.1 实际重开。准入通过：保留源任务能力最优单一 policy 不等于保留未来可适应起点；archive 中多种行为邻域经短 adaptation probe 选择，optimizer 重置与 latent embedder 的 anchor/replay/periodic reembedding 构成真实学习状态分支。不是仅把“多模型库存”映射到平台章，也不因 MiniGrid 或无 LLM 硬排。五任务/有限重访不证明通用终身学习、坐标维护或 lineage 的因果充分性；library、probe 与重嵌入成本须随证据保留。拟 5 分标准继续，实际 owner/Only 仍由作者比较。

## 15451 — Weak-to-Strong KD

[官方 v1](https://arxiv.org/html/2604.15451v1) §3 Algorithm1、§4.3 Table3 实际重开。准入通过：弱但适配的 frozen teacher 用于早期优化，学生连续两次超过 teacher validation 后永久撤去 KD；teacher gap × active lifetime 是相较一概强 teacher/全程 KD 的具体选择条件。Table3 太弱或太强可失去收益，不能采用 universal speedup。first@target 的 epochs/steps 不是总 wall-clock，active forward 和上游 teacher 构建不免费，≤15% 是本来源操作带而非普遍定理。5 分标准合理。

## 15614 — E-BoN

[官方 v1](https://arxiv.org/html/2604.15614v1) §2.3–3.1、Algorithms1–2 实际重开，复用已实际 Eq16–19 定点阅读。准入通过：固定 N 候选仍可用 entmax 形状与状态目标缩放改变探索/利用分布，新增的是采样操作条件，不仅又一个 locomotion 应用。它在 off-policy SAC 条件下依赖额外 transition/marginal 模型；all-zero objective 的均值倒数不应默补可行。近似 entmax 不叫精确采样，固定候选数不保证端到端恒定时延，foundation/LLM 只为动机而非已测负载。拟 5 分标准保留受限分支；本次不独立签其形式保证。

## 15623 — Overmind NSA

[官方 v1](https://arxiv.org/html/2604.15623v1) §1–2/Table1 与 §3 入口实际重开。具体前分母关闭通过：真实优化对象是 NVSA/LTN/LNN/NLM 的 symbolic binding、codebook search、fuzzy operators；Padé/dual-window address bypass 对这些模式有硬件价值，但正文没有建立该负载与当前 foundation 表示、训练、Attention/模型状态或大模型执行约束的直接研究桥。抽象的“可优化非线性/内存”类比不足以恢复；不是以没有 LLM、参数小或 accelerator 主题作为硬门槛。无需为该范围关闭追完整发表史或所有硬件附件。

## 15877 — Experience Compression Spectrum

[官方 v1](https://arxiv.org/html/2604.15877v1) §1–2、Figure1/映射与研究议程实际重开。具体前分母关闭通过：trace/memory/skill/rule 的轴与 missing-diagonal 是现有系统的组织及待研究问题，近似压缩比没有共同成本—质量合同；没有实际新跨层选择器、恢复/失效机制或受控综合证据改变成熟设计判断。不因综述体裁自动排除，也不由低 cross-citation 推系统失效、或把“压缩越高越通用”当已证明普律。本项保持未 selected/不评分。

## 16076 — PGCM

[官方 v1](https://arxiv.org/html/2604.16076v1) §3.1–3.4、§4.1–4.2 实际重开。准入通过：part→离散 visual prototype→concept-only task 接口，让概念含义由可显示的原型及表映射承载，具有具体可编辑表示分支，不是仅可解释性指标改善。原型选择受 reconstruction/concept/task 联合训练；hard concepts 不自动证明人类语义或因果忠实。segmenter 先消费完整图像，不能声称区域外像素从未影响表征；编辑成本及 CelebA 等负迁移仍保留。5 分标准可继续，非 LLM 不构成拒绝理由；不在本次签 Books。

## 16090 — AW-PSP

[官方 v1](https://arxiv.org/html/2604.16090v1) §3.1–3.3 Eq1–15、§4 入口及 Table1–4 实际重开。准入通过：参与可用性与本地数据联合相关时，最快/最可用 worker 选择会形成数据支持偏置；availability、recovery 与 co-failure 共同进入 sampling probability，是训练同步与数据支持交界的可迁移条件，不只是 FL 名称映射 Ch36。保留 limited CIFAR/容器 trace 证据、covered-label accuracy 的条件分母；ρ 未限制时 Eq15 合法概率条件不能默补，全类质量/线上规模不由现表证明。5 分标准仅报告是可接受后续判断，不因小 ResNet 或 edge 场景硬关。

## 有界结论

八项：六个具体贡献入口通过，15623/15877 两个具体前分母关闭通过。此结论不把六项自动升级 Deep、Integrate 或最终当窗候选，不代表全部447库存/150题摘独立审阅。作者仍须按本日日期及实际证据、具体 Books 命题完成后续；发现保证矛盾可按受影响命题精确隔离，不删已读有效证据。
