# 2603.10990v1：色彩评价目标与 refinement 资格的必要证据

仅03-13日报补充03-12北京时间自然日；准备者 mar13_supplement，非Books writer。本包待非准备者必要Source/评分/具体owner独核，不授formal/DAY。

## 身份、日期及原件

Too Vivid to Be Real? Benchmarking and Calibrating Generative Color Fidelity；Zhengyao Fang、Zexi Jia、Yijia Zhong、Pengcheng Luo、Jinchao Zhang、Guangming Lu、Jun Yu、Wenjie Pei。现有完整题摘/history [SUP_ABS3_10990.raw](./SUP_ABS3_10990.raw)仅v1、Comments accepted CVPR2026；未见轻量当前header中的撤回/纠错说明。准入§19具体目标混杂/色彩定向校准有效复用，不由文章主题或版本号准入。

DATE3原字段registered Mar12T02:14:42、created前一秒/arxiv.content/findable及正常Mar12 BJT公告批次夹证支持此arXiv日级事件；Submitted11T17:18:12与Updated12T01:04:40本身不是公开日期依据。具名CVPR先稿信号只定点恢复[官方单篇原响应](./SUP_VENUE_10990_CVF.raw)：同题八作者、pp37258–37267、明确链接2603.10990，Bib month June2026；不含本篇更早dated original release。后会议接受不推早公开，不声称排除全网未见早稿。请求与原件见[manifest/result](./SUP_CORE_10990_MANIFEST_RESULT.json)：exact-v1 https://arxiv.org/html/2603.10990v1 GET200/238409 bytes/2026-10-10T04:06:24.305872Z；CVF指定单篇GET200/6632 bytes/下一毫秒。没有扫全会议库或读异日候选。

## 实际必要Source与采用边界

实际读取精确v1 §1–7的必要论证、§3数据构造/§4 Eq1–7/§5 Eq8–11、完整主Tables1–5及SupplementA统计/评测人口、C实现说明、D训练条件/Limitations。Figures读相关正文/caption，不签视觉像素或未给出的曲线数值；没有代码复现、全部图库或旧版差分。

原约束是偏好/语义一致不等现实风格色彩目标；增量是对固定真实照片的saturation-scaling定向探针、CFG制造的有序real/synthetic监督及另标humanCFD目标，再用同一metric的语义attention调制采样。若成立，需要把审美偏好和特定色彩目标分账；并将标签制造器、CFG人口、独立人工锚点和优化后judge身份保存，不能只用优化所用metric自签保真。

- §1/Fig1正文与caption报告在同真实照片上改变饱和度时，若干偏好scorer偏向更vivid图像；只采所测目标错配的定向证据，不核未视觉曲线的精确幅度，更不由此证实生产T2I模型过饱和的唯一训练因果。
- §3：CFD由189490张经CLIP-IQA/Qwen2.5VL72B过滤真实照片、12类别与模型caption构造；六synthetic样本对应CFG7.5/10/15/20/25/30、11种T2I模型，标签预置真实最佳及较大CFG更差。160K train/30K test组不等独立真实色彩ground truth；模型caption也不保证真实照片语义完全保存。主文与补充“over1.1M synthetic”口径不与总图1.12M混合。
- §4 Eq5–7：Qwen2-VL多模态encoder与Reward-head作soft rank拟合有序标签；相同数据/epochs的Table4对照可限定评价soft-rank和text-conditioning。Eq6含j=i自比较0.5偏移与标签口径需精确recipe协调，不能据此否定局部经验或编造实现故障。
- §5/C：normalized text/image feature dot-product经softmax/κ、文本token平均、0–1 normalize/upsample成map，再以 s0[1−λ(1−t/T)a'] 逐位置/时间调CFG。这里map是所学语义agreement，不由命名认证色彩错误定位。正文及C“generated image”究竟哪步图像/何时更新map未精确说明；每步重算noise不等每步重跑CFM或闭环颜色测量。不采用精确可执行pipeline或免费plug-and-play保证，无需为了本次不采用的实现扩读代码。

## 关键评价、直接反侧及费用

- Table1本制造SynPairs/RealSyn正确排序83.6/80.1，HPSv3为57.5/58.3；不是统一所有评价目标的优越性。§6 RealSyn说随机synthetic counterpart而补充A说最低CFG7.5，保留协议差异；两个子集各5000 pairs，SynPairs为相邻CFG，不补作所有配对或独立photometric oracle。
- humanCFD6690图、超过20000ratings、每图三trained annotators，§3.3 mean Spearman>.85为所得inter-rater consistency，不是训练资格阈值；所评包括sharpness/illumination/saturation/overall realism，是该条件的人类目标，不是客观全色彩真值。Table2 Spearman84.9/Pearson85.4/Kendall71.4对HPS74.4/76.0/62.8，仅限定人口目标。
- Table3 SD3.5 full FID13.3→13.1、CLIP28.2不变、Δsat .15→.07、CFM4.9→6.9；PixArt16.5→16.4、27.2→27.5、.09→.02、4.4→6.4；Hunyuan22.1→19.9、27.5不变、.14→.03、.8→2.1。Δsat以真实总体平均.33作参考不是每prompt色彩真值；CFM既用来构造refinement又打分，提升不是独立放行证书。
- Table5 SD3.5 temporal-only FID18.0/CLIP25.9/Δsat.18/CFM−1.3，差于baseline13.3/28.2/.15/4.9；spatial-only13.2/28.2/.12/6.8，full13.0/28.2/.07/6.9。Table3 full13.1与T5 full13.0不合并或补同配置。T4 full vs pairwise/visual-only支持此配方局部收益，不授soft-rank或双模块普遍必要。没有统计CI不因此降分，但不能把.1或.2增量授确定普遍收益。
- H20/one epoch/batch32/lr2e−6/warmup.05/input448/τ.1/κ10为披露条件；生成完整steps、λ调参人口、总CFG扫描/encoder调用、端到端时长、batch/concurrency/SLO为Not Disclosed。训练free只指不改T2I参数，不等metric免训练/调用免费。Limitations明示只靠CFG强度构造失真限制多样性，未涵盖所有color defects。

## 最低评分与实际唯一owner

拟 **2+1+2=5**：Design2为具体定向probe/条件评价人口揭示审美目标与特定色彩目标的错配；Reach1限定生成评价这一组件，不借联想的全训练/平台链抬分；Durability2为可复用的目标/制造标签与人工锚点资格，不因CVPR或成熟CFG/Goodhart原则加分。必要评价反侧/与当前知识判断关系已读到足够，不默认完整AB潜力必须深审全附件。

拟 **具体已有覆盖，Books0**，唯一owner `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际顺读129–143完整局部：131错误proxy目标；133 reference encoder/population/scorer identity；135 MOS几何不是事实概率/跨域真值；137 ProtoBias冻结反向配对制造规则、filter/judge与人工锚、相关性不证全部主标签；139 conditionalmetric对象/归一化/独立人工校准。另585–606区分控制预算/实际成本、有限分布估计；这些具体承载本次要保留的评价资格，不只题名相近。新CFM/CFR recipe及本实验数字**没有被现章吸收**；它们在本日报保留局部结果，本次采用边界不需新增长期接口。Ch24拥有采样CFG效应，不把其未精确公开的map刷新/颜色定位当新已验证执行合同；不另写第二owner或以安全权限概念掩盖recipe缺口。

5分标准必要阅读因具体评价设计反側加深受影响内容完成；等待非准备者独核后才能正式列为深入完成/具体NC。无PRE/POST或Books写请求，不把普通未读外部化。若以后拟采用独立色彩定位或普遍refinement保证，只定点恢复map输入/刷新identity、相应独立label及heldout适配、完整费用和失败人口，不要求本次遍历全部实现证明论文永远正确。
