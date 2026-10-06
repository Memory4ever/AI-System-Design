# FIRST packet — 2025-10-06

作者Huygens；独立复核待Curie。66份精确v1完整题摘及页上版本史已实际读完；不能将这些视为66份Evidence。四主题38命中去重37家族，65条有界标题浏览仅恢复29条相关材料，不把分类total转为全量队列。

首批潜力（均只有提交时刻，尚无完全落窗first-public依据，不评分、不授正面Evidence）：

| 精确材料 | 具体增量与待核边界 |
| --- | --- |
| [ToolCert](https://arxiv.org/abs/2510.03992v1) | 工具metadata攻击下按采样成功率给分布鲁棒下界；需要核分布/置信度而非通用最坏情形安全 |
| [低精度Flash Attention失稳](https://arxiv.org/abs/2510.04212v1) | 低秩表征与偏置舍入误差耦合导致失稳，修正舍入验证；需核精度与控制变量 |
| [Speculative Actions](https://arxiv.org/abs/2510.04371v1) | 猜测下一动作并行执行，改变Agent串行延迟；必须核环境副作用与lossless成立条件 |
| [PatternKV](https://arxiv.org/abs/2510.05176v1) | 在线代表模式对齐后量化残差，改变KV分布而非仅截离群值；需核校准/状态/额外代价 |
| [Inoculation Prompting](https://arxiv.org/abs/2510.04340v1) | 训练时显式诱发不希望泛化的trait，测试撤去提示以抑制trait；局部防御不等通用对齐保证 |

分层代表排除供校准：04002 AgriGPT-VL为农业任务数据/训练流程，未见超出领域指标的机制；04017 Zephyrus为气象科学Agent，ROADMAP暂缓；04127为早期ANN hashing历史入门综述，题摘没有新增评价盲区或机制；04139为低资源语言微调复制指南，未见足以改变具体系统选择的新证据。以上是题摘判断，安全/纠错信号必要原文另定点处理，不用排除理由绕过安全核验。

当前继续必要安全/反侧与含糊scope原文，未等待FIRST；独立校准未回前不授正面Evidence。原件见本目录abs-ID.raw；请求身份见同名receipt，下载不是已读证明。
