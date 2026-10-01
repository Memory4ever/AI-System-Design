# 2604.25491v1 The Forensic Cost of Watermark Removal：有界证据与 Ch72 提案

本项是 04/29 作者侧必要审阅，非独立 Gate 或共享 Books 写入授权。[官方 exact-v1](https://arxiv.org/html/2604.25491v1) 的正式题名只有上述短题；旧 receipt 的后缀不得回填。已读 §1 threat model、§3、§4.1–4.6/Tables 1–5、§5–6 和 [Ch72 生成内容 provenance 正文](../../../../../books/part-06-ai-infrastructure/72-security.md)；不读不相关引用史。它已在[第三批完整题摘反查](./V3_REVERSE_TITLE_ABSTRACT_BATCH3.md)恢复为潜在线索，**不再次改变**当前 106＝69＋37 作者工作账。拟入选日期仍须绑定本日 arXiv 官方公告联合批次与单篇更早公开例外；HTML 首页 “28 Apr 2026” 单独不是北京时间时刻。

## 机制、评价与反证

以往移除评估常看 watermark 原 detector 是否失效与图像失真；作者加入第三个对象：**水印移除后是否仍可被独立的 forensic detector 识别为受攻击图像**。§3 的 ConvNeXtV2-Tiny+MLP 不是验证原图作者或合法编辑链，而是对干净图/带水印图与四类移除输出作二分类；平台场景是缺失原水印后再检移除痕迹，阳性也不能自动归责/处罚。§4 的 COCO 原图 5,000、VideoSeal 与 TrustMark 两种 post-hoc 多 bit 水印、256×256 水印及 224×224 detector，约 80k 派生图按**原图 ID**作 70/10/20 train/validation/test，避免同图跨 split。训练包含 WMForger 与生成式攻击，因此 seen-method 结果不是未知攻击零样本。

Table 2 的移除 ASR、Table 1 的 PSNR/LPIPS/FID 与 Table 3 的 forensic TPR 必须分别读。以 FPR=`10^-3`、由 COCO held-out 校准的阈值，Table 3 的 TrustMark/VideoSeal 两水印下 DiffPure TPR `0.253/0.254`、SANA-VAE `0.403/0.342`、WMForger `0.815/0.801`、CtrlRegen `0.427/0.369`；因此摘要“各攻击都能检测”只能保存在这个受限阈值下的**非零但强弱悬殊**发现，不能说几乎全部移除都可追踪。§4.4/Table 4 留一攻击族训练后，held-out DiffPure AUC `0.7670`、SANA-VAE `0.8682`，作者还报前者 TPR `13.3%`、后者 `36.5%`；跨未见方法衰减不能被训练内 Table 3 掩盖。§4.3 的强噪声可压低 AUC，却带明显画质损失，仍不是所有自适应攻击的下界。§4.5 的 1,000 张 FLUX 图只测所设阈值误报，不证明所有 GenAI 产物不会触发；§5 明说自适应规避、gen-time 水印与更高分辨率未证。

§6 提醒在百万张/日平台即使 `10^-3` FPR 也约千张干净图被标，需 base rate 与人工复核；高风险账号定向监测与全量自动处罚有不同误报成本。因此三轴是不同**证据和决策对象**，不能把 forensic detector 阳性当 cryptographic provenance、创作者身份或恶意意图。Table 5 的“可叠加任意现有水印”是架构上不改 watermarker 的可能性，不是已跨所有方案/分辨率验收。

## 项目准入与唯一 owner

具体贡献是把“移除成功＋感知质量”不足以刻画对抗成本这一缺口，转成**移除痕迹可检测性／检测器误报率**的独立评价轴；若成立，会改变 provenance 事故分流与 red-team 的 acceptance test。拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5/9`、标准审阅；因可能改变 Ch72 的安全评价合同，对该窄命题补足深入 Books 判断，不改分数倒推。实际 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 已要求 metadata＋embedded signal＋public verifier，并明确 watermark negative 不是“非 AI 生成”证明、保留 positive/negative/inconclusive；但其现有段落尚未把 **watermark signal absent 与 removal artifact positive** 分为两个检测器及独立的 FPR/TPR、适用率和处置权限。Ch66 拥有 EvalSpec/scorer 身份，Ch72 是该安全结果如何影响 provenance/风险处置的唯一正文 owner。

最小 source→actual-owner 提案：在 Ch72 layered provenance 的 negative/inconclusive 论点后，补“原 watermark 阴性不直接终止调查；已知移除 threat model 下可另跑 forensic trace sensor，分别报告原水印存活率、图像质量、痕迹 TPR@部署 FPR 及未知攻击/后处理切片。痕迹阳性只提示复核，不证明原作者、水印被移除或恶意行为；高误报量／未知攻击或分辨率变化时回退签名来源、原始记录和人工调查”。不采该论文 detector 为通用实现，不写自动处罚，不用 `10^-3` 当业务许可阈值。请非作者核 §3、Tables 2–4、§5–6 与 Ch72:827–840 的实际差异；核通过并获共享锁后才能写 Books。当前不计 Integrate／日 Gate。
