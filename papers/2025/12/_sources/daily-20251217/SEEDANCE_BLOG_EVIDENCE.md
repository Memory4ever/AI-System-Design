# Seedance 1.5 pro：官网Blog发布事件

固定窗口12/16 09:00至12/17 09:00+08。实际检查2026-10-02。事件身份是[官网Blog](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)，ArticleMeta.ID1817 / ArticleID1765883631909 / ArticleType2 / TitleKey同slug；不是arXiv首公开事件。[日期sidecar](../OFFICIAL_EVENT_DATE_RECOVERY.md)恢复PublishDate1765882058000，官方JS消费时区Asia/Shanghai，声明发布时间12/16 18:47:38+08。UpdateTime1788415475000是较晚更新，不冒称本次取到不可变2025HTML。

贡献先于评分：独立音画流程不能约束联合时间一致性 → Blog实际披露MMDiT联合建模、混合模态训练、coherence数据与联合reward链 → 需要把音画一致性理解为联合条件分布与训练信号，而非仅拼接。主线程首批准入已校准。对此收窄命题评分Design Delta2 + System Reach2 + Durability2 =6，标准审阅；不把10×宣传或通用diffusion知识计分。

实际读Blog从Unified Multimodal Joint Generation Architecture到Summary；另读Blog链接报告[2512.13507v1](https://arxiv.org/pdf/2512.13507v1) p2–8：p2§1模型、数据、后训练和效率轮廓，p3–7§2SeedVideoBench1.5，p8应用例子。精确v1取自原站，不采用当前v3；v1提交12/15 16:36:52UTC并不证明当时公开，故它是被链接报告的版本化技术证据，不授另一个首公开事件。未取得不可变历史Blog正文，结论仅限当前官方对该发布事件的披露与早期v1相容部分。

证据支持MMDiT跨模态联合建模及T2VA/I2VA/T2V/I2V多任务轮廓；数据coherence筛选、curriculum与caption；SFT+audio/video RLHF。没有联合模块的方程/细部、reward独立消融、对照budget或硬件/精度/batch/并发/SLO。`>10× end-to-end`及近3×训练收益不进入可归因性能结论（这些配置Not Disclosed）。SeedVideoBench用expert Likert与GSB分开视频/音频/同步，且稳定性可能靠slow-motion牺牲动态性；单一stability指标不等于完整生成质量。未复现或核验部署。

Books已具体对读 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 的两处实际段落：

- `Any-to-any AR 把 Modality Type 移入同一生成序列` 后的跨模态共享训练段（当前约760–770行）解释分别学会两种条件任务不保证一致重构，成组数据、共享prefix及梯度耦合增加一致性约束，独立条件模型仍可共存。它是AR/Omni123的受限论证，不是Seedance的dual-branch diffusion实现。
- 音画共享运动状态段（当前约1183–1187行）解释相同text不规定运动时序一致；实际机制是共同2D轨迹分别改变视频flow endpoint与音频运动condition，joint在不同指标不全面最好。这是共同条件，不是MMDiT跨模态联合模块。

**差异处置：** Seedance新增的是官方披露的联合双分支生成、mixed-task、coherence数据与audio/video后训练的一条完整模型路线；不能说整项已有覆盖。现有正文已经承载“任务接口统一不保证一致性、须有联合约束、共享训练仍有代价”的一般解释。精确v1仅给该路线轮廓，没有联合模块方程/状态布局或控制架构、数据、reward的消融，完整模型absolute/GSB不能分配这些机制的因果收益。因此作者拟 **仅报告**，理由是当前新增披露不足以写出比现有一般约束更具体的可验证机制解释，而不是发布本身没有设计变化。10×/3×不采用，perf配置缺项Not Disclosed。若原始联合模块或归因对照日后披露，定点重开上述两段之间的生成耦合分支，仍由Ch24唯一owner承载，不另建产品清单。决定待root非作者校准；没有Books写入。
