# 2025-10-16 首批非作者准入校准包

作者Euler；交Cicero。BJT[2025-10-15 09:00,2025-10-16 09:00)，正式候选0，尚无正面Evidence/评分/Books提案。这里只请求具体潜力理由及排除边界校准，不请求授日级完成。首公开尚缺官方历史公告或完全落窗bounds；精确v1 Submitted不是first-public，后续版本不倒灌。

实际完整v1题摘/版本史见[首批原响应](RAW_FIRST_V1.json)及[剩余题摘实读](RAW_FIRST_V1_REMAINING.json)。Atom当前题名不可替代v1，例如12586当前改题为There is No VAE，实际v1仍为Advancing End-to-End Pixel Space Generative Modeling via Self-supervised Pre-training。

| 精确材料 | 原有约束 → 原文增量 → 待核设计选择 | 日期/证据边界 |
| --- | --- | --- |
| [Laminar 2510.12633v1](https://arxiv.org/abs/2510.12633v1) | 全局actor/rollout权重同步受长尾轨迹阻塞 → relay参数服务独立拉取权重、动态repack长尾 → 训练/生成异步粒度与staleness/吞吐的取舍 | Submitted 14日15:29:14Z只发现；1024GPU/5.48x为作者摘要，未核成本/对照，不采用 |
| [Memory as Action 2510.12635v1](https://arxiv.org/abs/2510.12635v1) | 外置启发式工作记忆与任务policy分离 → RL统一学习编辑操作，非prefix轨迹按memory action切段并用trajectory优势 → 记忆编辑如何进入可训练action语义 | Submitted 14日15:29:57Z；2026v2/v3不采用。“标准policy gradient不可用”为原文待核前提，不写普遍定理 |
| [3-Model Speculative Decoding 2510.12966v1](https://arxiv.org/abs/2510.12966v1) | draft尺寸/接受率冲突 → 插入qualifier并使用fuzzy接受 → 三阶段资源及可控质量损失取舍 | Submitted 14日20:20:06Z；明确摘要承认target质量取舍，不声称分布严格不变/无损 |
| [BanaServe 2510.13223v1](https://arxiv.org/abs/2510.13223v1) | 静态P/D资源及prefix cache热点耦合 → layer权重/attention KV迁移、global store与重叠传输 → 路由与cache placement脱耦成本 | Submitted 15日07:20:14Z；摘要vLLM/DistServe收益未核workload/SLO，不采用；2026journal字段不定首次公开 |
| [Pixel-space 2510.12586v1](https://arxiv.org/abs/2510.12586v1) | 像素空间训练/效率落后latent空间 → clean语义与确定采样轨迹encoder预训练，再随机decoder联合微调 → 非VAE扩散/consistency训练可行性 | Submitted 14日14:41:16Z；ImageNet局部结果不自动排除，也未证明一般替代VAE |
| [VLA attack/defense 2510.13237v1](https://arxiv.org/abs/2510.13237v1) | VLA物理行动对视觉扰动鲁棒性不足 → 跨模态alignment与clean/adv latent双目标patch、视觉encoder对抗微调 → 可迁移攻击与防御边界 | Submitted 15日07:42:44Z；必要安全core尚待读，LIBERO不写真实机器人安全保证 |

代表性范围排除：[InferA 2510.12920v1](https://arxiv.org/abs/2510.12920v1)完整AB实际读完，监督者/专业Agent检索分析HACC宇宙学ensemble数TB，原文任务与评价属于暂缓科学应用；不以通用Agent节点重引。日期未核首公开，不为不影响处置另追日期。

需要校准边界：[COSTAR-A 2510.12637v1](https://arxiv.org/abs/2510.12637v1)完整AB已读。追加Answer组件对≤8B模型POV输出结构/决断性增益且模型间不同；不能只因局部/小模型排除。原AB未给足能改变设计的具体成立条件，作者将定点核评价/限制后判准入，不擅自写已关闭。

另两个官方core已实读：[Coral](RAW_CORAL_TITLES.json)的MLIR/IREE lowering与scalar/vector/matrix设计有潜力，但matrix仍开发、CHERI仅being designed；Oct15日名未知时区；[PaddleOCR-VL](RAW_TARGET_CORES_B.json)动态分辨率视觉encoder+0.3B语言模型及layout→recognition分工为潜力，Oct16日名同样不足落窗。均暂不评分/正式Evidence，首批校准不等日级DAY。

本日普通source、题摘筛选及必要安全/设计反侧继续；不等待校准而停止无关初筛，不展开未经校准的正面采用。共享Books/月度入口/LEARNING_STATE不写，作者不自审。
