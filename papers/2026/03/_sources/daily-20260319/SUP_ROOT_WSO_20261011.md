# WSO16127：必要证据与具体已有覆盖

root 只准备本19的该家族；补03-18自然日，身份/公告日依据复用本日元数据，不把 Submitted 或 ICLR 标签当公开证明。作者未重复审阅。拟准入命题为预训练 loss 与后续 SFT 目标可能偏好不同的 LR schedule；2+2+3=7，必要深入。名称是 Warmup-Stable-Only，不是 overflow 方案。

[精确 v1](https://arxiv.org/html/2603.16127v1)实际必要读取§2.1/2.4、§3–5/表1–4、§6/Eq6及 Appendix C/D/E、F 的表11–18和H/Eq12/表23；没有遍历无关附录、全部图像或旧版本，未核代码/复现。

## 支持与关键反侧

WSO 在 warmup 后维持 LR，不做预训练 decay。从头训练的1B/8B、固定 SFT 配方下，base指标与SFT任务平均的排序确实反转；这是联合交付目标的受限对照，不是“每任务都更好”。表12的MMLU、表18部分指令/事实指标有反向结果；不能把平均胜出改成所有能力都改善。SFT LR 经 AlpacaEval 选择，又在结果中使用该评价；其 reference 是同架构 WSO 的极小LR SFT模型，judge 为 Llama3-70B-Instruct，不是通用绝对胜率。独立选择集、重复seed/置信区间、GPU/完整训练搜索成本未披露。

§6/H 用 Hutchinson Hessian-trace 估计器，1B轨迹及少量scheduler点的负相关只支持解释性关联，不能断言 sharpness 是唯一因果，或从平均trace推全部方向的适配稳定性。不要与现Ch28的输出KL proxy混为同一个量。Appendix C所列batch×step与名义token预算、D的LR网格与表11最优LR存在待澄清口径；因此不认证可复现精确训练配方/严格等FLOPs或工程加速。BF16及数据/SFT配置是作者披露条件，吞吐、运行硬件、并发/SLO不是本篇证明对象（训练任务不要求服务SLO）。

采用范围：选择用于后训练的base artifact时应同时评价后续任务、更新尺度与评估成本，而非仅批准最低base loss；不普遍取消decay、不默认新架构/目标/预算都获益。局部配方与几何解释的未决问题不妨碍这一窄命题，但不得据此授正面生产保证。

## actual owner：具体 NC，不制造书稿 diff

已按AGENTS加载Books上下文及ROADMAP。实际顺读 Ch28「Learning-rate schedule 为什么决定训练轨迹」完整765–797，并读Ch27/29交接。唯一 `TRAIN-PRETRAINING`：[Ch28](../../../../../books/part-04-training-system/28-pretraining.md)。

现正文786–788已明确：base loss 不能替代后训练验收；base checkpoint × SFT update scale 联合比较任务拟合、参数漂移与held-out retention；额外网格增加费用；相关几何证据不能推出 decay 必然遗忘；收敛优先/后训练不敏感/迁移对照弱时保留 warmup–decay。790–792进一步明确预训练与SFT目标可能偏好不同配置，训练预算和固定SFT配方不能无条件外推。它实际承载本次拟采用的长期命题，不仅是同一主题。

**提议：深入完成 / 已有覆盖。** 新对照留在Report；不将WSO算法名称/表中有限胜出/未解几何因果追加为第二owner或章末论文摘要，不把已有覆盖改成低分。没有新写，不需要伪造POST；当前仍待非准备者核验原证与上述具体NC后计安全处置。
