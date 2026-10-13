# Seedream 4.0: Sep10 necessary evidence

作者 Meitner；精确事件为 [2025-09-09 官方发布 Blog](https://seed.bytedance.com/en/blog/seedream-4-0-officially-released-beyond-drawing-into-imagination)，本日原件 `SUP_SEEDREAM4_BLOG_20261011.raw/request.json`。可见 Date 与官方 type2 ID2094 / ArticleID1764227642774 / PublishDate1757347200000 一致；新补窗为 Sep09 完整 BJT 自然日，不要求时分秒，不回写旧时刻窗相交/保留判断。UpdateTime2026不是重要修订本身，当前原页未见影响采用命题的纠错/撤回说明。

## 实际阅读和采用命题

已实际读全部可见 Blog 正文：八类功能、MagicBench/MagicArena 评价说明、Joint Training、加速分项与结尾。原生成/编辑分开的版本及外接控制 → 当前版本披露统一生成编辑架构，native Canny/depth/mask 控制、多图输入/输出及两任务贯穿 CT/SFT/RLHF → 改变该版本多模态输入和后训练协同接口，准入 P。评分 **2+2+1=5**，标准完成；只计该版本工程披露，不把通用 DiT、蒸馏成熟原则或厂商排行计分。

核心披露包括 fine-tuned SeedVLM 提示扩展；DiT 与高压缩 VAE；视频抽帧/HTML 过滤/MoE 合成编辑对；多方面 reward；learnable discriminator 的对抗分布对齐；4/8bit 离线平滑/逐层搜索；未来概率轨迹与 loss 入 KV cache 的加速描述。这些是作者设计说明，不是实现核验或可比收益因果证明。

**Not Disclosed**：任务混合/训练预算/reward 公式、joint 对 single-task 的完整受控条件；VAE 压缩率及 DiT 布局；teacher/student 访问状态和 discriminator 目标；量化校准样本、精度工作负载、hardware/batch/concurrency/SLO；KV cache loss 公式、接受/校正/回退接口。MagicBench/Elo 缺完整 evaluator/sample/种子/置信区间与预算。故不采用 10x 端到端、10步等50步质量、普遍排名、真实物理/时序推理保证；不能从名为 speculative decoding 继承 AR 精确验证语义。

## 必要官网边界

[同模型官网](https://seed.bytedance.com/en/seedream4_0/) 本日原件 `SUP_SEEDREAM4_HOME_20261011.raw/request.json`，实际读可见介绍、功能、评价与底部说明；没有新增联合训练公式/cache 条件。当前官网 Artificial Analysis 榜标记 as of 2025-09-12，窗后数字不回填。Technical report 按 runtime 字段实际定位为 [2509.20427](https://arxiv.org/abs/2509.20427)，本日 `SUP_SEEDREAM4_REPORT_DATE_20261011.raw/request.json`，实际 current 日期/版本说明：v1 submitted Sep24，当前 v3 说明4.0/4.5。它不是 Sep09 公开证据；只作具名后续恢复线索，不把提交日期当首次公开、不扩读后出的全部实验或4.5，也不将官网挂后出的报告当旧 Blog 失效。

未读边界：图像展示/雷达图像素、后出 technical report 全文、代码/API 实现及复现实验，均未采用其数字或实现权限。官网有限必要入口已核，不留下伪装外部 hold 的普通方法待办。

## Books 判断

**仅报告**，不是已有覆盖。实际 owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 开头问题链、786–806 few-step student 状态/teacher与critic目标分责、1080–1108 typed unified generator 与任务 evaluator/capability interference、1187–1208端到端费用；相邻 `MULTIMODAL-REPRESENTATION` Ch23 1–68 codec/版本身份及379–388 rate/distortion/下游容量/decoder成本。当前本文不披露能修正这些具体长期论点的新 cache 正确性条件、joint recipe 成立边界或受控加速因果；只支持这个版本采用这些设计。未把未披露机制编进书，无确认长期缺口或共享 Books 写入请求。

非作者 Cicero 已实际原核心/日期/owner 位置和评分校准，标准完成/仅报告通过见 [独核 §3](SUP_INDEPENDENT_20261011.md#3-seedream4必要evidencebooks具体差额)。单篇有效层不等待72 arXiv题摘，不授日级 DAY/FINAL。
