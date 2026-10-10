# 2603.10703：同日 handoff 最低审阅提案

状态：准备者实际读必要 v1；等待 root 非准备者独核。只占本来源包，不授权候选、Books 或 DAY。

## 身份 / 日期

- WalkGPT: Grounded Vision-Language Conversation with Depth-Aware Segmentation for Pedestrian Navigation；七位作者见 `SUP_ABS3_10703.txt`。
- 完整题摘及准入、Mar12 arXiv 日级事件的原独核有效复用：`SUP_DATE3_10703.raw`、`SUP_INDEPENDENT_REVIEW_20261009.md` DATE3 节。Accepted CVPR 2026 未指向具名 dated 早稿；不从接受日期倒造全文公开，也不扩 venue 全站。
- 实际官方精确 v1 原件：`SUP_HANDOFF7_SOURCE_10703.raw` / `.txt`；GET/时间原件见 `SUP_HANDOFF7_FETCH_RESULT.json`。没有以最新版本替代本窗 v1。

## 实际必要阅读与新增

实际顺读 txt 350–1940：§3 MSQP / CTP / Region Alignment Loss，§4 训练人口和实现，Tables 1–5、直接失效与结论限制；不称读完全部附件。

原有 SEG→SAM mask 接口上，本稿以冻结 SAM 特征构成原尺度、两种 pooled 尺度和全局均值，再用 learned-query cross attention 形成 MSQP；SEG 状态经 MLP 映射多 token mask prompt（CTP）。额外 InfoNCE 的目标来自同一冻结图像特征上的 top-K attention 伪目标，不是外部独立传感器给出的物理真值。文本回答、mask Dice/CE 与该对齐项联合训练。深度不是另训 dense depth head，而是传感器/mask-derived 深度标签转为离散文本监督、输出 distance token。

这一具体多尺度/projector/伪目标组合可继续作为窄 P，不能仅因 pedestrian 应用而 EX；但它不新增“语言必须回到可验证空间证据”的成熟原则，未给出独立取证保证或新通用 grounding 有效条件。Tables 5 的受控移除支持本配置而非机制原创或所有模块的唯一必要性：去 MSQP/multi-scale/NCE 各有局部下降，移除 distance token 主要影响 Depth Acc。正文 Q=36 padding 与消融 Q=32 口径需区分，不认证唯一可执行 query 配方。

## 关键评价 / 反侧

- PAVE 标称约 41k triplets，但本次实际训练/测试为 85×100 帧 / 6×100 帧，91 sessions；程序过滤保证格式/标签一致性不等同真实路径安全、全部用户操作或逐条独立物理核验。
- 7B→13B Depth Acc 从 41.97 到 48.95，而 AbsRel 从 67.88 到 70.66，不能授全面深度改善。Depth Acc 容差为因子 0.5–2，不等精确距离校准。
- Table 3 mIoU 20.16 低于 SwinUNETR 20.60；Table 2 部分 RES 列并非最优。不能将 caption/grounding 指标转为安全导航 success。
- 实际失败包含单视角模糊/遮挡、类别不平衡和不正确路径建议；结论还保留 dataset artifact 与跨域验证未完成。冻结视觉 encoder/LoRA/单 H100 训练不是无训练或现场机器人控制认证。

## 最低评分 / 处置提案

1（局部配置新增）+1（重要性受当前任务/人口约束）+2（可核的实现与局部消融/反侧）=4。建议已关闭 / 仅报告、Books 新写 0；不是 EX，不是具体 NC，不把新实验称已被 Books 吸收。无需为低分稿扩 owner/PRE、全附录或 physical deployment 审阅。若独核识别出上述配置之外真实新条件，再只定点重开那个命题。
