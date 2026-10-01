# Apr21 五项有界非作者复核：16918–16940

审阅者 apr02，作者 apr01，实际访问 2026-09-27。沿当前 AGENTS、研究合同与统一入口；仅核本组必要 exact-v1 方法、主要反证、真实 owner 与相邻交接，不核日级来源/日期，不重扫 raw、不通读全部附件、不写作者报告或 Books。

## 有限结论

2 项 6 分缺口深入 source→owner 提案通过（FreshPER/Ch33、D-QReLO/Ch30）；2 项 5 分标准仅报告通过；1 项 5 分纠错深入的中心采用保证暂缓通过。提案仍没有实际 Books 写入，争议不是外部材料不足，整日不据此 Complete。

## 2604.16918v1 FreshPER：6 gap 深入，Ch33 窄提案通过

实际核[官方原文](https://arxiv.org/html/2604.16918v1) §3.1–3.5、§4.3、Appendix F Table5。确有三种不同对象：base-priority 的年龄/重算、非均匀 buffer sampling 的权重、behavior/current action ratio。实际顺读 Ch33 的 objective staleness、阶段化 replay 与“Replay 是成本与分布的共同选择”（1121–1135 附近）；已覆盖年龄/reuse与分布代价，但没有把旧 priority 的寿命及 buffer 分布纠正单独持有的机制讲清。

2+2+2=6 支持在现 replay 段内窄补这一分工，不为年龄增加 truth/admission 权力。原文 §3.5 允许 reward priority 固定、advantage/TD priority 重算，不能写所有 PER 从不重算。ESS 上界与 KL≈steps 只是衰减动机；action ratio 不自动修正 state distribution。Table5 的 Standard PER 有 IS、默认 FreshPER 无 IS，须保留该对照差异，不归因全部收益于 decay。τ 失败、简单任务 transient instability/饱和与缩短 buffer/fresh-only 回退应紧邻正文；不外推同 compute/wall-clock。仅 source→owner PASS。

## 2604.16919v1 N-HMC：5 纠错深入，中心采样保证暂缓通过

实际核[原文](https://arxiv.org/html/2604.16919v1) §2.2、§3.1 Eq7–9/Algorithm1。噪声 latent 经确定性 DDIM 的 likelihood 定义，与实际 transition 是否保有 posterior 稳态是两件事。Algorithm1 在拒绝后缩 δ、重新采 momentum，repeat 到接受才推进外层计数；普通 MH 的 holding 与 adaptation 合法性不能由接受公式直接补齐。

作者三状态控制流反例成立：对 uniform 的对称 K，move 概率 (.2,.5,.5)，去掉 holding 后 jump-chain 稳态为 (1/6,5/12,5/12) 而非 uniform。这只证明一般“直到接受再计步”不自动继承 MH 稳态，**不是**该具体连续 HMC 在所有参数下的数值证伪。2+1+2=5 纠错深入、窄争议/暂缓采用 posterior 保证合理；保留 latent likelihood 与有限重建经验，不声称全部实验无效。恢复需要与实际接受/拒绝/adaptation 一致的 transition/holding 桥，不要求展开全附件或发表史。

## 2604.16923v1 Alignment Imprint：5 标准仅报告通过

实际核[原文](https://arxiv.org/html/2604.16923v1) §3.1–3.3、Table5 与 B.1 必要假设。base/aligned likelihood 差、self-information 加权及条件扰动标准化是受限统计分支；SFT exponential tilt 是建模假设，不是任意训练的精确身份。B.1 用了额外 variance/CLT 条件，不能只列主文 Assumption1–2 就宣传无条件 ROC 支配。

1+2+2=5 标准仅报告准确。Table5 的单项加权并非所有切片都增益；统计模型 pair/source/domain/编辑和长度合同必须保留，检测分数不是作者身份真值。此处分层的理论限制已足够阻止强采用，无须把全部理论改判错误或增加 provenance 保证型 Books 正文。

## 2604.16937v1 No One Fits All：5 标准仅报告通过

实际核[原文](https://arxiv.org/html/2604.16937v1) §3、§5.1–5.3/Table2–3。模型先跑 Native/Translate 两响应，再提 response-level features 并选结果；不是生成前省一次调用的 cheap router。训练标签只保留一方正确的样本，oracle any-correct 也不是部署 selector。

1+2+2=5 标准仅报告通过。局部少量增益和 feature importance 不识别内部文化/translation 因果；双生成/翻译/提特征成本没有完整端到端 SLO 比较。既不升级通用多语控制策略，也不因已有 routing 主题把全部实现称为 Existing；保留 post-response portfolio 这一准确作用域即可。

## 2604.16940v1 D-QReLO：6 gap 深入，Ch30 窄提案通过

实际核[原文](https://arxiv.org/html/2604.16940v1) §3.3 Eq6–16、§4、Table2–3、§5.2。已经完成 full FT 后，1-bit sign×mean-absolute scale 再近似量化残差的 SVD，是 delta artifact 的压缩责任，不退还训练成本。实际顺读 Ch30 Merge/base lineage→量化表示→动态 adapter（380–405 附近），现有分支未明确这一 full-FT 后资产路径及压缩顺序。

2+2+2=6 支持在 Merge 资产段内窄补：先分训练参数化与训练后压缩；再绑定 base、scale、residual factors 和实际部署 layout/行为回归。Table3 支持受测顺序分支，不是所有矩阵的普适优劣。BitDelta 1/16 对比其他 1/8 不 matched；ceil/额外 scale 与 singular values 不是严格 byte cap，rank 增大有退步。不得采用无损、通用胜过 LoRA 或生产 latency 倍数；保留原 adapter/full checkpoint 共存与 Ch49 执行交接。仅 source→owner PASS，尚需锁/实际写后。

## 文件与验收范围

只新增本审计文件，五身份完整；新增文件空白检查无错误。未改作者 README/notes、Books、全局 checkpoint；未 stage、commit、push。未复现实验，未证明日级冻结分母、日期窗口或来源零遗漏。普通两项 Books 待办仍需推进，不冒充外部 Blocked。
