# Nov07 后续局部独立准入校准

复核者：root，非日报作者。检查时间：2026-10-04T16:08:54+08:00。

本次只处理 [SECOND_CALIBRATION](SECOND_CALIBRATION.md) 中八个需要裁决的方向，不重审首批有效校准，也不授日期、候选分母、完整Evidence、Books或日级完成。实际读取完整题摘及决定准入的原文片段，原件见 [TOPIC_SCREENING](TOPIC_SCREENING.md)、`nov07-admission-ambiguous-core.txt`、`nov07-admission-key-points.txt`、`nov07-ambiguous-decision-evidence.txt`、`nov07-narrow-tail-core.txt`、`nov07-custom-control-core.txt`。

## 裁决

| 材料 | 准入层裁决与边界 |
| --- | --- |
| 2511.02997v1 Control Protocols | 潜在贡献通过。固定攻击下的控制成绩不能代替攻击者知道控制流程后自适应攻击的结果；原文新增的是具体评价信息契约下的反侧，不是泛泛最小权限。未核全部攻击预算或安全率分母，不能采用摘要数字或生产安全保证；必要安全证据按受影响命题核验。 |
| 2511.03675v1 Whisper Leak | 潜在贡献通过。加密内容不自动隐藏流式响应的流量特征，且所测试缓解方法仍有局部泄露，改变平台侧敏感信息边界。完整摘要支持该方向，尚不授权具体检出率、所有模型或任意网络环境保证；后续Blog不得代替v1首次公开。 |
| 2511.03163v1 SRFT-GaLore | 潜在一般优化机制通过，医疗任务结果不采用为一般模型收益。替代SVD的结构化随机梯度投影可独立讨论；原文左侧sketch/QR与后续投影尺寸未充分定义，中心实现正确性及主子空间保证保留争议。Table3的rank128、refresh50、batch4、A6000、32-bit optimizer条件不能外推通用加速。争议不是改判范围外的理由，也不支持Books正面公式。 |
| 2511.02996v1 SCALE-VLP | 潜在一般跨模态损失机制通过，领域知识/医学应用仍不引入。§3.2的关系加权确实改变pairwise objective，足以核验，而非只有换数据。off-diagonal target仍0，增大权重会加强negative BCE惩罚，不直接构成partial positive；batch row-normalization也不授权无collective保证。只保留该损失及关系监督边界，不采用作者更强语义。 |
| 2511.03060v1 Curved Spacetime | 潜在局部表示证据通过。固定step norm随机方向null与with/without/base context edits提供可检验的representation reorientation观测；不把弯曲路径当内禀曲率、相对论证明、attention唯一因果归因或新架构。§4.2～4.3的方法足以决定继续核该受限probe，不需要另造spacetime知识树。 |
| 2511.03051v1 ScalingEval | 贡献关闭。完整摘要及§2.2实际提供模型共识驱动的推荐评价和排行榜；用参与模型投票构造truth再比较agreement，类别分歧没有独立truth anchor，也未形成对共享偏差或真实correctness的受控新反证。缺少独立truth本身是复核者的成熟评价提醒，不是本文已建立的新评价盲区证据。关闭依据是实际增量停留于应用比较/既有聚合，不是因为benchmark、实验规模或审阅成本；保留原记录，不为不影响处置的日期新建请求。 |
| 2511.03276v1 Diffusion Super Data Learners | 不把新arXiv身份当本窗新贡献事件。实际作者仓库写full paper10/03、code/logs10/27，作者Notion写Released Aug09；当前没有识别到本窗实质修订。这些声明不足以证明早期稿与v1逐字相同，也不证明旧月份已审阅或Books吸收。保留有意义的matched-budget方向及事件身份限制，若取得本窗新机制/重要修订原证据再定点恢复；本日不扩扫8/10月。 |
| OpenAI November6 action controls | 潜在具体安全约束变化通过。实际读取Enterprise/Edu release原文L916～920：工作区可控制custom connector的单项action，新action默认禁用、修改action沿用原状态、Refresh需管理员作为用户连接。只采用这些当次披露，不补当前Help后续snapshot语义。日期仅原始日粒度且时区未核，不能授完全落窗或Books采用。 |

这些裁决没有将日期隔离项变为确定候选。有限恢复后确实不能证明落窗的，保留具体潜在机制、采用边界和最小重开材料，不盲目扩读不用于正面采用的全部实验。安全/纠错及中心冲突仍需保留足以阻止错误采用的必要证据。

## 剩余范围

未检查 [CURRENT_STOP](CURRENT_STOP.md) 的其他16项及UserAlign/3TF/Common-O剩余普通裁决、MiMo/MiniMax来源尾项和整日六部分。作者继续这些有限工作；不得把本次八项校准写成全量筛选或日级通过。已有首批必要证据仍有效，不重复无差别阅读。
