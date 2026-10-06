# VISOR23495 — Source / 两段PRE

作者supp_mar26_fresh；7分/date25及准入reader已PASS。实际 https://arxiv.org/html/2603.23495v1 §3的attention/CKA仅诊断、§4.1–4.4/Eq1–3、§5.1–5.2/T1、§6/T2–4与timing必要原段已读，不无差别全部附录。

## 原证限定

多数LLM层只更新text；固定少数CA读取同份完整visual tokens而不更新其内容，另可选SA同时更新image/text，使后续CA读取已refined视觉。先max配置预训，离线筛可行SA子集，再每训练step随机配置微调；route token/浅层MLP预测当前问题所需配置，多问时取预测中最高cost。离线pseudo labels要运行各配置并用correctness/response loss，99%criterion不是每题线上正确性guard或无偏label。

信息保留仅『未删除原tokens』，不保证执行图变化保持全部下游信息；CA-only在finegrained任务落后，过激token packing重新出现质量下降。T1 VISOR的MME/MMStar/POPE/InfoVQA低于dense，不是allbench支配；T2高packing继续损hard。本文LLaVAOV/Qwen2-0.5B、SigLIP400M、384patch729visualtokens、部分LLavaOV数据未公开实际较小人口、16MI300X、3epochs/AdamW/global128；precision未披露。Transformer-FLOPs不计visionencoder；作者与非作者定点实际回读§6原243行，计时是能容纳所有方法的最大batch，未明确每法异batch，具体batch/请求负载未披露，不认证任意单请求/servingSLO/全费净加速。CA额外参数<7.5%，筛配置/label搜索/route与训练都付费。T3的独立训练预算、T4共享模型受益不唯一归于routing。

## Actual owner与差额

实际Ch23 Fusion483–574/CrossAttention503–520和Conditionalcompute918–930已有query/externalKV通路、latency/modalitygate与交接，却未在此论证中区分『保存多少visual tokens』与『哪些层读取/改写这些tokens』，也没有跨budget子图训练后perinput route这一具体接口。Ch22历史addressability/容量不接管多模态fusion；Ch24概率生成/commit不接管理解输入的执行图。唯一owner MULTIMODAL-REPRESENTATION Ch23，拟插CrossAttention原机制之后、Sharedselfattention前；保二者成熟合理条件，不新建VISOR收纳节。

## 两段逐字PRE（未写，待非writerSource/PRE与root锁）

Cross-attention 的读取与视觉状态的改写还可以拥有不同计算预算：保留完整视觉 token bank，让大多数层只更新 text，少数 cross-attention 层查询当前视觉表示，再由另一些可选 shared self-attention 层重组 image/text；后续查询消费已更新的视觉 bank。这样减少的是跨模态交互和视觉细化的层次数，不是删除多少输入 tokens；原特征还在，也不意味着改变计算路径后细粒度信息必然被正确使用。<!-- source-family:SF-2026-ARXIV-2603-23495 -->

若不同样本需要不同细化深度，可以先筛出可用子图、混合这些配置训练同一模型，再用浅层 router 选择一次执行图；离线 label 的 correctness/loss 与配置搜索是已付费监督，不是在线证据充分性的真值。[受限LLaVA-OV对照](https://arxiv.org/html/2603.23495v1#S4)中，仅 cross-attention 对细粒度任务不够，过强 token 压缩仍退步，完整 tokens 与稀疏交互也非全部任务无损；省去的 Transformer FLOPs 不包含视觉 encoder，最大可容纳 batch 下的计时未披露具体 batch 与请求负载，不认证任意单请求、serving SLO 或全费净加速。视觉 bank、改写层、子图集合、router 和预算须随接口一起验收；细节、路由或实际费用失配时，保留完整 shared-attention、固定预算和原视觉读取路径，而不以 token 未删批准质量或 serving SLO。

本人静态注拟：`SF-2026-ARXIV-2603-23495 exact-v1 §3–6/Eq1–3/T1–4，采用visual bank读取/改写层分责与多budget子图训练/router；不采tokens不删即信息/质量无损、全任务支配或FLOPs=净SLO，保离线pseudo-label搜索、CA-only/packing反退与参数/训练费用；未核代码/复现。`

纠正最大batch语义后必要Source/actualowner/PRE和本人注已真实独核PASS（reader§9）；精确锚HIVE05359完整原段之后、Shared self-attention标题之前，不移动旧段。待root具体窄锁，Books未写、未授POST/DAY。
