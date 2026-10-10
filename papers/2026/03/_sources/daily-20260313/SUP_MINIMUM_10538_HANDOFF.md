# 10538v1：DSFlash最低增量及具名venue门

仅03-13新增窗Mar12 BJT；有效P准入与DATE4日级arxiv夹证复用本日主独核。CVPR2026 Accepted不是已知dated早稿，不要求全网不存在先公开的证明。

本次必要venue原件：`SUP_HANDOFF_DATE_10538_CVF.raw/txt`（精确CVF标题/六作者/页17388–17398/arxiv链接/bibtex June2026）；作者大学 `SUP_HANDOFF_DATE_10538_OPUS.raw/txt`显示online2026/07/02、release2026/07/06。均GET200见 `SUP_HANDOFF9_DATE_FETCH_RESULT.json`。这两个具体正式/机构记录晚于本窗，未识别具名早公开正文；继续有效Mar12 arxiv日，不把July当首次研究日、不保证全网从未早公开。只精确目标论文，无venue全站扫描。

exact-v1 https://arxiv.org/html/2603.10538v1 GET200/190680bytes，`SUP_HANDOFF_SOURCE_10538.raw/txt` 与 `SUP_HANDOFF9_FETCH_RESULT.json`。实际必要读txt545–1315（§3.1–3.6完整/Eq2–7/§4.1）、1300–1599（主T1–3/§4.2–4.5正反侧/结论）。未遍历supplement或复现代码。

实际新增配置：复用冻结EoMT/DINO backbone同时给seg mask与relation features，取patch排除CLS/register/query；现DSFormer同位置maskoverlap由average pooling替冗余操作；对同subject/object共享x，用g与1−g分向、同MLP出双向predicate，训练swap masks双forward+中间consistency，部署单forward；按maskoverlap=0丢非S/O patches与已知ToMe-SD分层组合。两backbone合一、pooling、gate/双output/swap consistency与mask token pruning是当前模型优化配方，不借已知compute reuse/ToMe或SingleMPO原理抬新分。原标注forward比backward三倍的shortcut反侧只当前PSG人口，不授真实方向对称已保证。

关键反侧：T1 DSFlash-L mR30.90/50ms、DSFlash-S*25.05/18ms，不能合成56FPS同时最佳质量。T2 unified backbone30.7→25.0质量退步；T3 prune 28.80→26.67，H100 19→20ms/3090 29→29ms并不加速batch1，GTX230→205ms有当前改善；Prune+ToMe30%26.51/173ms是不同配置。§4.1 latency仅warmup200后的forward均值、不含preprocess、tail/stream/全部署；训练GT segmentation、部署predicted mask失配及mask遗漏不保证“完整真实graph”。不把GTX训练budget与3090 forward合为同硬件SLO。SingleMPO杜绝重复mask预测是继承既有公平协议，不把无重复当真实relation全召回。

提案 **1+1+2=4**：具体architecture/执行优化配置（1）；影响该PSGG模型/当前硬件人口（1）；可复用工程配置但无新长期通用原理（2）。保持P，拟已关闭/仅报告Books0，非EX/NC，不否定局部实际速度/质量收益。最低审阅够即停，不扩全部图/附录/代码或architecture历史。待非准备者原证与评分独核/root采用；不授DAY。
