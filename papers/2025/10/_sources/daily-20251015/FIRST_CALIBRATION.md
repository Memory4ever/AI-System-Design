# 2025-10-15 首批潜力校准包

作者Euler，待root非作者独立准入校准；不授DAY。窗口BJT [2025-10-14 09:00,2025-10-15 09:00)。独立读取本日原入口与题摘，不继承14候选池。

完整精确v1题摘已实际读六项：下表五项加MeTA-LoRA 11598；FlexPipe仅HTML标称v1摘要恢复，另留内容身份限制。首批以下五项均缺首次公开历史公告/完全落窗bounds，提交字段不作公开时刻，不评分、不授正面Evidence。原件 RAW_FIRST_ABSTRACTS.json、RAW_FIRST_ABSTRACTS_TAIL.json、RAW_FIRST_AND_BOUNDED_TITLES.json。

| 身份 | 原文实际增量与待校准边界 | 日期原值 |
| --- | --- | --- |
| [2510.11683v1 BGPO](https://arxiv.org/abs/2510.11683v1) | MC likelihood近似需保留多sample非线性objective图；构造可按sample累积的线性下界，on-policy值/梯度等价有具体假设，可能改变dLLM RL显存与估计精度取舍。不能由constant memory声称总RL训练显存固定；v2/3不倒灌。 | Submitted Mon,13 Oct2025 17:47:50 UTC；v2 Tue14 09:26:10 UTC仅版本线索，未证明重要修订或首公开。 |
| [2510.11690v1 RAE](https://arxiv.org/abs/2510.11690v1) | 重建VAE潜空间与表示预训练encoder+trained decoder的替代，高维latent下DiT头/动力学适配可能改变生成codec设计；不采用should be default或FID单数字作普遍结论。 | Submitted Mon,13 Oct2025 17:51:39 UTC。 |
| [2510.11602v1 Deconstructing Attention](https://arxiv.org/abs/2510.11602v1) | 拆开token mixing、sequence dependence、softmax/dot-product及QK耦合，统一层和hybrid受控替换；失败孤立模块可与标准attention共存是必要设计反侧，不以负面结果排除。 | Submitted Mon,13 Oct2025 16:42:14 UTC。 |
| [2510.11677v1 Chronologically Consistent Generative AI](https://arxiv.org/abs/2510.11677v1) | 数据和instruction-following模型限定知识截点，潜在修正forecast评价的lookahead泄漏；固定weights只支持复制身份，不自动保证所有数据均无泄漏。latest题名不同，不代v1。 | Submitted Mon,13 Oct2025 17:45:24 UTC。 |
| [2510.12121v1 Targeted Representation Editing](https://arxiv.org/abs/2510.12121v1) | 从方向最大化改为target-reaching，以TD value估计部分生成的最终属性强度并梯度干预hidden，可能改变精确控制取舍；3B/Phi-mini局部实验仍有准入潜力。 | Submitted Tue,14 Oct2025 03:50:22 UTC。 |

代表排除已实际读core：Plex Coffee是既有Notion connector/自定义GPT的领域部署反馈，无模型或检索机制新解释；Argentina是LOI计划，未披露能耗/互联机制；Anthropic economic-policy原core是宏观税制/劳动力情景，不是模型训练或系统设计机制。OpenAI Well-Being council有安全信号，已经实际读How we work/Expanding safety，仅专家治理过程/未来改进未披露新guard机制或评价，不因标题安全就评分。以上日期分别由本日官方RSS/hydration核定落窗，仍不构成候选。

FlexPipe标称v1 HTML出现EUROSYS2026及cluster-trace-v2026，不能据现页默认它就是2025初版可采用内容；原abs v1缓存未恢复，待必要精确身份。Google Coral NPU已读架构/工具链core有具体矩阵优先与C/MLIR lowering潜力，但Oct15日名时区不明，仅相交日期；matrix unit原文明确尚开发，不能写已发布完整矩阵硬件或低功耗保证。以上作为额外限制，不纳本批正面Evidence。
