# Apr22 四项 Books 反向建议的有限非作者复核

复核者：apr01，非本日报作者，未写本组 Books。2026-09-28 本轮实际重开四项官方必要方法/关键反证，并顺读 Ch5 绑定、probe 与参数移植正文及 Ch24 训练 support、Few-step target construction 正文。仅核这四项反向建议，不验证日期、全部来源或日级 Gate；未复现实验，不改作者报告或 Books。

## 19052：不能以一般 filler/role 覆盖冒称完整具体 Existing

[官方 v1](https://arxiv.org/html/2604.19052v1)实际 §3.1–3.3，尤其 Eqs1–7、CBR intervention、跨 context 两假说。Ch5 现约171行确实已有内容与角色绑定，约183–219行已有 probe/干预/粒度的证据阶梯；这些承担一般原则，不承担“按 entity 与 relation 双索引定位属性”和“跨 context 同结构仍可能需坐标 translation”的具体受限分支。仅把采用命题缩成“语义相似不能解释关系”会丢掉原准入的机制，不足支持整篇已有覆盖。

建议保6分深入的具体候选，给 Ch5 一小段双索引→受控 patch→跨 context 坐标对齐的条件性命题，再由 root 决定必要正文。不是要求写完整 PLS 算法或唯一原生 circuit。两家族/合成五域与受限 DocRE 不证明开放泛化，拟合坐标和非自然 patch 仍需行为验收；现一般绑定模型继续保留。此处是反向 Existing 未通过，不是原论文普遍机制已证实。

## 19117：受限仅报告可通过；不建议称整个共享 circuit 已有覆盖

[官方 PDF v1](https://arxiv.org/pdf/2604.19117v1)实际 §3.4、§4.1/4.3–4.6、§5 和必要 shared-set 反证。Ch5 现217–219行已明确参数充分性、activation relay、行为恢复与干预粒度分开，并保冗余和输入范围；本次最窄的解释边界已有真实承载。原受测方向/位置差异和 zeroing 迎合增加可留 Daily 的深入仅报告，不需要以每一任务补一段通用 granularity 原则。

保留该来源独立的经验，而非称该 circuit 或所有任务方向已在书中实现；head-set sufficiency 不推 necessity，行为改善不推内部 substrate 消失。自然 checkpoint 对照非唯一因果，有限 DPO/单模板、probe 等效检验和 white-box 成本不升级开放 monitor。6分深入仅报告的具体处置通过，原候选不删除。

## 19009：Only 反向建议遗漏了训练 target 的具体生成/评价接口

[官方 v1](https://arxiv.org/html/2604.19009v1)实际 §3.1–3.3/Eqs1–6、§4 的主要对照。Ch24 现1092–1118行已有 student 访问状态和冻结 teacher 的 midpoint energy selection，却没有在线 fake-score 与固定 real-score 差构造 stop-gradient regression target、对该 target 解码评分并调节正负更新的分支。它不只是再说“target 需要验收”，也不等已有 navigator 选择 teacher 路径；直接将其收窄成 Only 的已有覆盖理由不足。

建议维持6分 gap 深入，最小采用“评价原始 student sample”和“评价拟更新的构造目标”是不同监督对象，target 生成器/reward/学生更新分别绑定；不采用全面 gradient 冲突消除或 reward 真值保证。fake estimator、分组、VAE/reward 增加成本，局部指标退步、未匹配总 compute 与未充分人评均保留。正文可极窄，不能用一般原则代替该机制。

## 19141：一般部署 support 不能替代 maximum-vs-mean 的新条件

[官方 v1](https://arxiv.org/html/2604.19141v1)实际 §3.1–3.3/Eqs3–4、§4.1–4.2/Tables1–2。Ch24 现103–105行与1097–1099行已有自生成/off-trajectory support 责任；它们并未表达异构 patch 时刻中平衡平均噪声仍会留下接近 clean 的最大信息，因而缺少纯噪声起点。原贡献是训练状态联合分布的可检查失配，不只是一般“训练覆盖部署”。

建议维持6分深入，最小条件段可解释先控制允许的最干净 patch，再采各 patch 时刻；difficulty head 和异步采样只是受限后续分支，不必全面写算法。不能把 max 上界称每个有限样本必取等号、uncertainty 当真值或同 NFE 当同 wall-clock。保 REPA FID 反例、额外 head/训练/调度成本及同步 sampler 回退。该 Only 的反向 Existing 理由未通过，并不要求全局扩审。

## 本轮边界

实际4项：1个深入仅报告建议通过，3个反向覆盖理由需修正为真实窄机制比较并交 root；不改变候选数、评分、日期或作者完成状态。不授权写锁、不计实际整合，不签整日报告。未变化的有效证据可复用，后续只核必要 literal/变化正文与邻接。
