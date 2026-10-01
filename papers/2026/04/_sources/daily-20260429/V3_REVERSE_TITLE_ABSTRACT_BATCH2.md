# 04/29 V3 旧泛化关闭理由的第二批有界题摘判别

作者只对旧 `pre_denominator_closure` 里题名显示**独立机制、评价反例或设计选择冲突**的十个身份完整读题摘；八项拟恢复者均打开官方 exact-v1 摘要（`25098` 的 abs 直链本轮 cache miss，改读官方 [HTML v1](https://arxiv.org/html/2604.25098v1) 标题和摘要），两项拟维持关闭也核官方 exact-v1。此为贡献准入，不是必要方法/主表审阅、日期单篇证明或独立 Gate。旧 receipt 对 `25098` 的标题已不是首版标题，故不能用后稿文字补首版结论。

| ID | 作者侧处理 | 不采用的外推／下一必要核 |
| --- | --- | --- |
| [2604.24885v1](https://arxiv.org/abs/2604.24885v1) | **恢复潜在**：动态分辨率的 1D visual tokenizer 将图像分辨率与 AR token 长度从固定网格解耦，直接改变 Ch23→24 的表示/生成算量选择。 | 64 tokens/1024²、gFID 与 179G FLOPs 绑定 class-conditioned 模型及作者对照，不等于所有高分辨率生成恒成本或生产质量；需核 tokenizer 信息损失与同模型/预算比较。 |
| [2604.24955v1](https://arxiv.org/abs/2604.24955v1) | **恢复潜在评价纠错**：可执行 Agent benchmark 的任务规范/脚本本身可能把有效解误判失败，作者报告 12 个任务方确认问题及 BIXBench Verified-50 的专家对照；潜在改变 evaluator artifact 的发布验收。 | 科学/生信任务仅作**评价基础设施**反证，不恢复 AI for Science 领域能力研究；模型审计不等于独立 truth，须核确认/漏报分母与 Ch66 现有具体合同。 |
| [2604.24964v1](https://arxiv.org/abs/2604.24964v1) | **恢复潜在评价条件**：单站短任务/二值成功率不足以代表真实多站长程 Web Agent；逐任务 rubric 与 rubric-per-step 提出成功和效率分账。 | 200 个 live-web 任务、44.5% 与 1.15% 均是该测试协议分母；是否超出 Ch66 已有轨迹/effect/成本评价仍要对照，不因新 benchmark 名称直接入 Books。 |
| [2604.25098v1](https://arxiv.org/html/2604.25098v1) | **恢复潜在负证据**：先前「结构性裁层损伤 test-time reasoning」不能推出细粒度稀疏权重裁剪同样损伤，可能改变压缩×推理预算选型。 | 首版正式标题是 *Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling*；旧库存丢了前半句。仅两种 7–8B reasoning LLM/四 benchmark；准确率反例不等于在稀疏硬件上有同等 latency/energy 收益。 |
| [2604.25213v1](https://arxiv.org/abs/2604.25213v1) | **恢复潜在安全评价反证**：同域传统篡改校准仍可被 TruFor/DocTamper 检出，但同域 AI inpainting 使两者 AUC 显著下降；检测器原有的 domain competence 不足以保证生成式微改检测。 | v1 摘要 3066 paired forgeries、365 pair-votes、TruFor 0.962→0.599、DocTamper 0.852→0.585；只支持该 GPT-Image-2/文档协议，不证明一般媒体来源不可验证或所有模型自审失败。 |
| [2604.25419v1](https://arxiv.org/abs/2604.25419v1) | **恢复潜在训练机制**：无标签 RLVR 把 rollout 多数票仅作候选 proposal，Lean proof 才允许奖励；未验证时丢弃 plurality 并用零均值残差信号维持梯度，改变 proxy vote 与 verifier authority 的关系。 | v1 只在数学可形式核域测三 backbone 并报 code/general 迁移；不把 Lean proof 外推为任何开放任务 truth，需核 ResZero 的偏差/方差与 compute 成本。 |
| [2604.25634v1](https://arxiv.org/abs/2604.25634v1) | **恢复潜在但需安全保证纠错**：token rank-frequency 的模型间参数差异可能是低成本黑盒替换监测信号，若足够稳健会改变 Ch66 模型身份核对的证据层级。 | 34/36 Mandelbrot 拟合和 q 参数分离**不是**加密 provenance 或单条响应身份认证；「100,000×」是与 sampling detector 的估算延迟，不是端到端安全效果。须核样本长度、温度/解码、提示分布和显著性后才能称分布 fingerprint。 |
| [2604.25872v1](https://arxiv.org/abs/2604.25872v1) | **恢复潜在理论/评价纠错**：proxy reward 的逐对 ranking 错误并不与 policy-gradient 后真实收益损失一一对应；初始 policy 和学习算子可令部分错误良性乃至有益，可能改 reward model 评价目标。 | 理论应按吸引概率的条件核，摘要承认评估指标与下游性能仍有 gap；不把有益错误解读为无需准确 reward 或任何错误可故意注入。 |
| [2604.25000v1](https://arxiv.org/abs/2604.25000v1) | **维持具名前闭**：intent compilation、closure-gap vector、delegation envelope 是开放机构授权问题的概念分解；题摘仅提出 benchmark metric 议程，尚无非同义的执行/验证条件或受控反证。 | Ch72/84 既有授权、证据和 effect 交接需以真实机制增量才重开；不能把有用概念框架误称无学术价值。 |
| [2604.25895v1](https://arxiv.org/abs/2604.25895v1) | **维持具名前闭**：把标注者视为设计者意见延伸、事实证据或独立授权的三种规范角色，是有价值的 RLHF 治理分解，但题摘是文献论证与建议，尚未给与 Ch31/66/72 现有来源/权限分账不同的可检验设计机制或效果边界。 | 不因伦理话题排除；若全文给出会改变 annotation acquisition/aggregation 的具体失效证据可定点重开。 |

本批 `10` 份完整题摘为 `8 潜在＋2 具名前闭`；和首批及原 64 身份互不重合后，作者侧**已处置的最小集合**为 `86＝61 潜在＋25 具名前闭`，另 2 个机构事件潜在。这不代表批次源全部查完，更不是正式候选分母；八个拟恢复均待必要原文/真实 owner/非作者准入核，不能直接计评分或共享 Books。
