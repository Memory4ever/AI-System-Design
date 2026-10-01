# 04/20 十一项负侧冲突：非作者逆向准入审校

复核者：root；日报作者：apr20_resume。复核日期：2026-09-28。依据当前研究合同 §3，不以章节可映射、小模型、局部场景或已有 Books 主题作自动准入/排除。定点重开各官方 exact-v1 的主张、必要方法与关键反证，并比对实际 owner。这里裁的是贡献分母与处置边界，不代签 109 项全部 Evidence 或整日来源/日期 Gate。

## 七项恢复：有限准入通过

| 家族 | 独立裁决与不能越过的边界 |
| --- | --- |
| [15622 AdaVFM](https://arxiv.org/html/2604.15622v1) | **恢复，2+2+2=6，标准仅报告。**Cloud MM-LLM 低频更新场景/class 与 edge VFM 高频逐帧执行形成两个不同控制时钟；Ch49/54 的模型档位/设备预算没有自动覆盖语义候选陈旧。§3 的 subnet/class 双输出与§6.3 用逐图生成场景注释模拟低频输入的差距必须同时保留；不能把局部图像分类/分割和 FLOPs 推为真实端云尾延迟。 |
| [15794 Self-Distillation Recovery](https://arxiv.org/html/2604.15794v1) | **恢复，2+1+2=5，标准仅报告。**受损 checkpoint 后，静态 teacher bootstrap 与 student 自己 rollout 蒸馏的次序是具体训练选择，超出笼统“蒸馏可恢复”。Table 1 的 science/tooluse 互有取舍，Table 4 的剪枝恢复仍比原 MMLU 低 2.55pp；CKA 接近不是功能因果或原表示流形已恢复，追加训练预算不匹配。Ch29 暂无必须改写的稳定结论。 |
| [15871 UniEditBench](https://arxiv.org/html/2604.15871v1) | **恢复，2+1+2=5，标准仅报告。**633 图+77 视频构造 source/target/instruction 配对，使 reconstruction 与 instruction edit 的比较单位具体化，值得核比较有效性而不是只增加榜单。Ch66 的 EvalSpec 一般合同未因这组图像/视频指标改写；distilled judge、样本分层与 train/test 不明限于受测协议，不能当人类真值或普遍公平性证明。 |
| [15741 Sequential Internal Dispersion](https://arxiv.org/html/2604.15741v1) | **恢复，2+1+2=5，标准仅报告。**跨 token/层的表示 dispersion 改变正确性 sensor 的输入支持范围；作者 OOD 表里单独 Internal Variance AUC 60.56 高于完整组合 58.67，反证“多加内部信号必然更准”。Ch66 已规定 sensor/真值、切片与校准分离，本文是受限选型反例；监督标签、读取成本和跨任务漂移未消失。 |
| [15760 KWBench](https://arxiv.org/html/2604.15760v1) | **恢复，2+2+2=6，标准仅报告。**223 个未经提示的专业问题先要求识别应解决什么，之后才计执行；这把 task-specification 输入本身变成评价对象，不能由“已给定清楚任务”的成功率替代。Ch66 原有成功/能力分账仍成立。单 judge、缺同题显式提示消融及 human baseline，不能把 gated 低分识别为模型推理因果或真实职业失败率；此处并非恢复 AI for Science 的领域任务。 |
| [15521 FreqFlow](https://arxiv.org/html/2604.15521v1) | **恢复，2+1+2=5，标准仅报告。**图像 flow 的低/高频条件分支与空间 velocity 联合训练是具体生成目标分解，Table 6 的单/双分支消融使“只有视频 attention 频谱类比”旧关闭理由不足。Ch24 已有 flow 目标和条件化分支；本论文未控制全部容量/训练算量，也未披露可横推的硬件、NFE、延迟合同，不能把局部 FID 差写成通用生成范式。 |
| [15621 AdaRankLLM](https://arxiv.org/html/2604.15621v1) | **恢复，2+1+2=5，标准仅报告。**有序检索子集（包括 k=0）使弱/强 backbone 的检索深度选择出现条件变化；Table II 的 Qwen3 Thinking Vanilla-10 Overall/EM `34.18/54.85` 高于 AdaRankLLM `32.75/51`（同表对应行），不能宣传任意模型质量收益。Ch76 已有深度/噪声/成本权衡；oracle 每题最佳 k、token/端到端时延不匹配，故只保留有限反例。 |

## 四项维持贡献前关闭

| 家族 | 独立排除理由及保留事实 |
| --- | --- |
| [15657 CovAgent](https://arxiv.org/html/2604.15657v1) | RTL coverage-hole 六类与 19 个设计上的领域化工具/反馈组合可复查，但 Ch66 已要求将不可达/坏 reference/执行失败与能力分母分开；七工具与上下文、预算同变，未隔离可迁移的新选择合同。旧实验不删除，不能把百分比当纯框架因果。 |
| [15802 CHOP](https://arxiv.org/html/2604.15802v1) | 相邻 chunk 的 prefix 索引/重抽是局部 RAG 实现；Ch76 已承担结构边界与 retrieval→reader 分账。Top-1 检索命中提高，但回答 F1 `0.2760 < 0.2763`，无单独 prefix 消融/完整索引成本，不能推答案质量或新长期方案边界。 |
| [15972 WORC](https://arxiv.org/html/2604.15972v1) | 预测低权重角色后重复 quota 属 Ch82 既有弱链路预算问题的 heuristic；未识别真正因果弱点，同讨论次数不等同 token/总成本或独立样本。保局部结果，不形成可复用的资源选择准则。 |
| [15756 TTL](https://arxiv.org/html/2604.15756v1) | 冻结视觉编码器、仅调 OOD text prefix 与伪标签 bank，是具体视觉 OOD 适配组合；Ch23/66 已要求污染反馈、阈值和成本共同验收。论文未给超出这条合同的跨流状态/保护条件；不否定局部 FPR/运行时间实验，也不因视觉领域本身硬排。 |

因此独立准入结果与作者 `7 恢复 + 4 前关闭` 一致，允许工作账 `150=109候选+40前关闭+1日期隔离` 继续；这是有限准入 PASS，不意味着七项新恢复都应写 Books，也不意味着 40 个负侧逐篇全文核过。七项各自标准 Evidence 已在正式 §4，跨本窗 08–09 的 arXiv 公告归属仍需与来源/日期 Gate 一起核。外部来源缺口和剩余具名单篇同行不能由此豁免。
