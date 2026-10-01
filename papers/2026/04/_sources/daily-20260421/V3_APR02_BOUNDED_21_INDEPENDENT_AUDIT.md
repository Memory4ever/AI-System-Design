# Apr21 有限21项非作者必要审阅

审阅者：`/root/apr02`；访问日期：2026-09-27。独立于本日作者 `/root/apr01`。本文件只记录实际完成的必要原文、具体反证与现有 owner 对读；不重扫原始270题摘、不遍历版本史或全部附件、不写作者报告及共享 Books，也不代替本日来源、日期、冻结分母和日级 Gate。日期3项只复核隔离依据，其余18项审阅必要采用范围；没有复现实验。

## 第一批：日期与披露合同

- **2604.16515v1 / 日期隔离**：实际打开官方 abs-v1，并核原始 receipt 的 own-version Updated=July13、OAI 空。Submitted Apr15 不证明首次公开；晚 Updated 也不单独证明真实 July owner。当前窗口依据不足，隔离、不评分的处置通过。
- **2604.16521v1 / CAMP / 6分纠错深入、窄争议**：实际读官方 PDF-v1 III.F、IV.C–G、Table IV。API request logs 是 adversary 可见对象；非 hard-block 类别在阈值前原样外发，后续修改本地历史不能删除已经发送的远程请求日志。因此累计零暴露保证不能由四场景表推得；若只验最后请求须明确更换分母。SSN 等 hard-block 类别从 turn0 有保护，不得否定全部类别/全部经验。对读 Ch72 trajectory ledger 与 Ch84 input/consent，窄裁决通过。
- **2604.16524v1 / Anumati / 6分保护行为深入、仅报告**：实际读 HTML-v1 §3、§4.3、§6.1。callee claim-level skill gate 有实现责任，但 understood/reasoning/fingerprint 仍有 self-attestation；JWS 未实现，微基准不含 wire/TLS。对读 Ch72/84，保留受限协议，不采用法律/实际遵从保证；不是整份方案已完整 Existing。
- **2604.16529v1 / 日期隔离**：实际打开 abs-v1，并核 receipt own-version Updated=Apr22T01:08Z、OAI Apr22。Submitted Apr16 不能把它塞入 Apr21 窗口，晚字段亦不能单独定真实 owner；隔离不评分通过。

## 第二批：选择器与采样律

- **2604.16535v1 / SCATR / 5分标准、仅报告**：实际读 §4、BoN 配置、Table2，并对读 Ch66 model-specific probe 正文。Qwen1.7B HumanEval 59.3 低于 PRM 60.4 的反例保留；0.15–0.20ms 是局部 scorer，不是 N16 总生成时间。模型/领域特定训练与迁移范围成立，Only 通过。
- **2604.16536v1 / 日期隔离**：官方 abs-v1 Submitted Apr16；receipt own-version Updated=July14、OAI 空。仅据这些不能恢复本窗首次公开，也不能单独确定 July owner；隔离通过。
- **2604.16555v1 / LLM as Tool / 5分标准、仅报告**：实际读 §3.3 Eq2/4、AppC.2 Table6，对读 Ch81 typed candidate/evaluator/held-out 主线。操作/node/module 分层决定与残余 LLM 参数职责成立；coarse 随机 35.58 高于 LLM 29.98，不能采用规则挖掘100%正确或更大 LLM 必更差的因果结论。Only 通过。
- **2604.16557v1 / S-GRPO / 6分纠错深入、窄争议**：实际读 §4.2–4.3 Eq7、§5 Table1–2。全失败组固定注入一条 GT 不是旧策略的原始采样律，不能同时写 mixed group 全部来自 π_old 并据此声称纯 on-policy/unbiased。保留 bootstrap 经验、δ=1 的 general 退步、Qwen4B semantic judge 非真值；不否定全部训练效果。窄裁决通过。

## 第三批：测试效应与成本

- **2604.16543v1 / Conjunctive / 6分保护深入、仅报告**：实际读 §3.5、C.2/C11，及 Ch72 fragment recomposition 正文。exact marker 和模拟 privileged effect 不是真实 tool side effect；ρ 的有限模型不能升级全框架权限保证。Only 通过。
- **2604.16565v1 / BMC / 6分标准、仅报告**：实际读 §4.1、Alg1、Eq14、Table3。GT gate、mask/reconstruction、max10 重试均是有限评价合同。**K=16 是每次 reconstruction 的16个去噪步骤，不是16条独立重构样本**；此纠正已发作者，作者确认已落盘。额外去噪、encoder评分与重试成本不能省略，density proxy 不等 truth。Only 通过。
- **2604.16571v1 / EquivFusion / 6分标准、仅报告**：实际读 §3.2、§4.1–4.2、§5及 SoftFloat future，对读 Ch49 typed/numerical correctness 主线。integer miter、静态/有界展开与编码假设是证明范围，未实现浮点通路不外推。Only 通过。
- **2604.16576v1 / Retriever / 5分标准、仅报告**：实际读 §8.1。几何正则改变了表示但双向干预未给一致鲁棒提升；有限白盒/direct-transfer 不等最终 QA 安全。Only 通过，不将干预失败改写为全部几何信号无用。

## 第四批：三个 owner 比较与一个受限 recipe

- **2604.16583v1 / POLAR / 6分真实 Ch56 gap**：实际读 §2、Alg1–2、§3.2、Assumption1–2、§5.1；对读 Ch56 routing/placement 分权及 Calibration feedback 正文。具体新增命题是 resident cache 的冷成本影响探索，而 chosen routing feedback 又决定 slow cache identification；显式 probe 与快路由/慢 residency 的双向可观测性耦合尚未完整承载。窄 source→owner 提案通过，**没有实际写入**。IID/full-rank/hot-margin 与 exact SolveCache 的条件理论不赋给 greedy；校准模拟/合成请求不证明生产 tail SLO。可在原主线插两段，不另写算法摘要。
- **2604.16584v1 / LeetProof / 5分标准、仅报告**：实际读 §4.2、§5.2、§6.2–6.4，对读 Ch66 reference/verifier 主线。PBT 只检测已采样 soundness/uniqueness，不证明完整 NL intent；$5预算只 code/proof，不含 spec 生成；四问题 Lean 胜出边界保留。Only 通过，不称整个实现 Existing。
- **2604.16585v1 / GNWM / 5分标准、仅报告**：实际读 §3.2–3.4、§4.2、§6.2，并对读 Ch25 observed/latent/imagined state authority。grid-snap 防模糊不证明物理 transition 真值；有限数据/任务 recipe 不保证任意维度唯一训练最优、无界 rollout 或普适因果发现。没有以任意子集 p=z 反例否定 full-vector 形式下界。Only 通过。
- **2604.16587v1 / vStream / 6分真实 Ch66 gap**：实际读 §3.3–3.6、Table1、E.2、F.3.1，对读 Ch66 Interpretability Graph Diagnostic Authority 正文。具体新增是昂贵干预标签训练→已完成 span 的廉价线性 region ranking；现正文没有完整承载该 amortized sensor 分支。窄 source→owner 提案通过，**没有实际写入**。Pearson 相对排序不是绝对 effect/完整原决策 faithful；correct-answer 选择、32 mask 的离线 forward、DINO、materialized attention、async 队列成本必须保留；117×非生成 E2E，SDPA/Flash 实际无成本路径未获证实。高风险采用应回退必要原始干预。

## 第五批：归一化保证、优化理论和词表迁移

- **2604.16591v1 / RASLIK / 6分纠错深入、窄争议**：实际读 §3.1 规范化式、Alg1、AppB Step1/6及必要实验设置。k=1，q=(1,0)、g=(1,2)，Rademacher 投影归一化后 h(q)=r1、h(g)=r2，期望内积0而真实 cosine=1/√5，故规范化估计无偏保证不成立；threshold 后的随机集合均值也不自动继承 score 无偏。不采用由该桥推得更新无偏/MSE严格改善，不否定匹配集合经验；Eq1符号只记更新约定待澄清，不单凭符号断言实现反向。窄裁决通过。
- **2604.16607v1 / 文本检测 / 5分标准、仅报告**：实际读 §4.2、§5.1–5.2，对读 Ch66 calibration slice 正文。固定0.5与每域1000样本选 EER 的阈值合同不同；human-only accuracy 是 specificity，非 generated recall，F1 受类别率影响。受限排名不证明检测普遍不可能。Only 通过。
- **2604.16620v1 / PASTA / 5分标准、仅报告**：实际读 Assumption1、Alg1、Theorem3。β=0/S=1/p=1 配随离初始化距离改变的 batch 已是一种条件分支，不能声称所有情况非 anchor 不可；BG-0 oracle计数依 smoothness 等假设，非 Transformer Adam/GPU实测效率。对读 Ch28 实际训练 recipe 主线，Only 通过；未重建全证明。
- **2604.16646v1 / framework比较 / 5分标准、仅报告**：实际读 §3.5、§3.7、关键结果与 Ch81责任主线。同 GPT5.2、双角色、temperature0、timeout500s 不隔离全部内置抽取/context/API 波动；跨可用 benchmarks 的 SEM 使用不同 n，不是复现实验的置信区间。host P40/L4 不是远端 GPT 推理硬件。Only 通过，不采用架构因果排名。
- **2604.16656v1 / FragMend / 6分真实 Ch11 gap**：实际读 §3.1–4、§6.1–6.4、AppA，并对读 Ch11 Vocabulary Adaptation 及 Ch12 输入/输出参数交接。现章已有对齐初始化/联合 checkpoint 迁移；真正窄增量是表示可组合性驱动 item selection×hidden mapping initialization，以及 HF added-item 优先使短项增加实际 token 数的反收益。source→owner 提案通过，**没有实际写入**；可在原迁移段补两段，保留 probe/readout 不证明内部词义、FVT Latin 更好、OOD退步、LAPT与序列成本不等端到端收益。

## Primary identities 与验收边界

上述实际引用均为 `https://arxiv.org/html/2604.<ID>v1`，其中 CAMP16521采用 `https://arxiv.org/pdf/2604.16521v1`；日期三项另实际核 `https://arxiv.org/abs/2604.<ID>v1` 与本日原始 receipt。必要原文 locator 已逐项具名，不把消息收到视为已读。

本文件支持三个日期隔离和十八个有限 source/disposition 判断，包括 POLAR/vStream/FragMend 的三个窄 source→owner gap；不授权共享 Books，不声称独立核完全部270题摘、全站来源、首次公开日志或复现实验。作者必须同步具体纠正、落实真正必要 Books、完成写后与日级独立 Gate 后才能决定本日报状态。
