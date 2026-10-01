# 04/28 arXiv 贡献准入：第三批中十项

本批是旧 V2.1 `retained` 队列第 71–80 个身份 `2604.23932`～`2604.24013`，逐项重读已有原始身份 receipt 的完整标题与摘要。旧评分、日期、Books 结果不继承；缓存若与官方 exact-v1 不一致，以后者为准。“继续”只表示后续有条件审查的线索，未冻结分母或进入完整论文队列。

| ID | 题摘判断 | 当前理由 / 最小消歧 |
| --- | --- | --- |
| 2604.23932 | 继续核贡献 | Geo-distributed LLM 训练的源/目的 OTN rate-matching + segmented long-haul RDMA 可能改变跨 DC 通信状态边界，但摘要仅两句、最高 20×/buffer −62.7% 无模型、链路、流控和端到端分母。仅在官方 v1 有可实现 rate/credit 协议与相关故障回退时准入；不能凭 RDMA 术语和 headline 留作完整候选。 |
| 2604.23940 | 前分母关闭 | 多 Agent decompilation 的 parse→GCC→LLM-generated test→repair 是特定软件逆向应用的既有分层执行验证；“0% behavioral correctness”以作者生成测试为 oracle，未证明源程序真等价，也未改变本项目 Agent 工具 effect/结果验收的长期合同。 |
| 2604.23941 | 继续核贡献 | 230M GUI grounding 用 encoder–decoder 替代缩小 decoder、并把 10.8M 数据筛到 3.8M，可能对端云 Agent perception responsibility 有具体反例；但摘要主要是小模型架构/数据配方局部收益。需核同预算 backbone 和端云接口是否带来新系统选择，不因手机场景自动准入。 |
| 2604.23950 | 继续核贡献 | 视觉 encoder attention sink 与语言中层 text-to-vision attention 对位置偏差的不同抗性，若有相同预算对照，可修正“attention 分数可直接作视觉 token 重要性”命题；需要定点核各层可见性、双阶段剪枝和 Ch23 已有可见性/保真回退差异，不因另一个 prune module 留候选。 |
| 2604.23987 | 继续 | 连续微调中 conformal coverage 在准确率前坍塌、按任务 held-out buffer 在每次更新后重拟阈值，属于 evaluation acceptance 分母变化；摘要已明确 exchangeability / classification-style 限制，不能外推到开放生成。需核 8 task sequence、泄漏/缓冲预算、与 Ch66 slice/calibration 的实际新差异。 |
| 2604.23990 | 前分母关闭 | 三语运行失败→修复→回归的 workflow 与分语言对照符合已有部署评价原则，27 组 81 样本 pilot、同一 foundation model MA=MB；最高 9 分漂移是局部运行观测，不足以改变跨模型或通用 Agent evaluation contract。若后文提供独立新 owner/witness 再定点重开。 |
| 2604.24003 | 继续核贡献 | 发现 short-context post-training 本身压缩推理且带来训练不稳，再按正确/失败 rollout 的 step confidence 选择归零 advantage，可能改变长度目标与 reward 分配的因果归属；需核 context-only 受控基线、verifier 假阴性以及与 Ch33 现有 step credit/失败组处理的差异。+0.86pp 不单独构成主线。 |
| 2604.24005 | 继续核贡献 | 多轮 on-policy distillation 中学生轨迹跑出 teacher support，KL 上升与成功率下降；按可监督 trajectory depth 从短到长或可改变数据准入 owner。需核是否做相同 token/interaction budget 对照、teacher 在 student 状态上的可用性、科学任务只作 benchmark 非 AIforScience 主线。 |
| 2604.24008 | 继续 | PTQ calibration 的目标从泛代表性转为加权 outlier-channel coverage，有可计算的 weighted set-cover 和有条件的 clipping surrogate 上界，可能改变校准样本选择合同；需核真实 channel coverage→量化损失的相关性、AWQ/GPTQ 共同控制及 Ch49 现有 calibration 机制。不能把 stylized upper bound 当真实模型误差保证。 |
| 2604.24013 | 继续核贡献 | 将 RS/AG collective 拆成 P2P 与分片计算以隐藏通信尾部，可能改变 TP/DP overlap 的完成语义；但摘要声称“exact 消除尾延迟”而缺配置和跨 rank 正确性定义。需核依赖图、buffer/collective 顺序与 Ch36 已有分解 overlap；若只是受限调度实现则报告即可。 |

本批 **2 项继续、6 项继续核贡献、2 项前分母关闭**。开放八项只是有限消歧线索，不是八项冻结候选。
