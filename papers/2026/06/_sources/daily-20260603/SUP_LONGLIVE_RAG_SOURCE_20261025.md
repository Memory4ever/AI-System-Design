# 02553 LongLive-RAG：必要证据 / 六分 / Ch25小差额

Jun03仅补Jun02 BJT。AGENTS/当前Research与Report合同、适用Sources/统一入口/ROADMAP与本日停点已按恢复读取；R62完整exact-v1题摘/准入/联合日期有效复用，v1提交Jun01 17:50:49Z、正常最早Jun02 00Z至同日精确DOI登记上界，不把单字段冒实际公开时刻。[当前abs](https://arxiv.org/abs/2606.02553)唯一v1，所见无withdrawn/erratum，不遍历假想渠道。

## 实际必要域和反侧

实读 [exact-v1 HTML](https://arxiv.org/html/2606.02553v1) §3.1–3.4/Alg1/式1–9、§4/T1–3、A限制与E数据/训练/评价设置。未核全部relatedwork/图像像素/案例/代码或复现；T3c检索预算图只读作者正文说明，不冒独立量图。充分支持下述有限接口后停止。

冻结AR视频diffusion backbone，query为上一已完成clean latent的1024维retrieval embedding；一次/block检索，所选历史context复用全部denoise steps。近期状态出local window时，成对写key bank和真正供generator读的context bank，cosine/topK排除最近R条。不是把压缩embedding喂生成器，也不是每去噪步重新检索、真实世界状态或可纠正过去错误的时间回滚。相同WAN VAE坐标下用一个encoder跨三backbone，不授任意codec/family通用。

AE重建不足以令key适合非近邻检索：局部window cosine高于margin才惩罚，长程重现不被一律当negative；二阶embedding平滑抑制候选集无意义抖动，reconstruction仍保内容。三个目标共同塑形检索几何，并非修改base动力学。无可用历史时回原sink+local；生成误差仍会被存回/重新取回，近邻query本身漂移可导致检索失配。

比较固定total attention12、sink1，RAG用retrieved6+local5，其余基线按各自规则填槽，不是靠扩大attention取得全部收益。128 MovieGenBench prompts均经Qwen2.5-7B改写，三backbone/30/60/120s；T2 average rank最好不等每指标最好，30s Self-Forcing dynamic degree52.03高于RAG42.24，120s SF DeepForcing background96.83/motion98.97也高于RAG96.40/98.75。这些是视觉代理，不证身份真值、动作/物理动态或时间无界稳定。

T3 CausalForcing30s：AEonly subject94.82/imaging69.48，AE+delta94.76/69.14反退；完整smooth组合95.43/70.07改善，但不能宣称delta单项支配/各目标独立因果。各方案同槽比较支持受限非局部信息选择，不将全部改善归损失单项。主结果无全run重复不确定性/严格配对seed，不自补显著性。辅助VLM不是新独立world truth，本文不采用其分数。

E：数据由SelfForcing prompt池抽10%、seed0，LongLive自产90-latent轨迹，20k+latents制备6×A6000约7天；其后AE训练<100A6000 GPUh。AE AdamW/LR3e-4/WD1e-4/batch128/400epoch/seq8、1024维、delta窗3/margin.85、smooth系数1、mixed precision enabled但未指统一dtype，10%validation最低total选checkpoint。量化结果另6×A6000约一周，不能拿此计入数据/训练总费；T1额外encoding/search单A6000约4ms/block是120s规模局部，两子项3.96+.08不严格等所列4.08，不自修或宣称恒定总成本。历史key/context驻留仍增长、真实attention读与数据制备/训练/调优/解码评价全付费；原图分辨率、精确软件/重复、服务concurrency/全SLO在采用域Not Disclosed。不运行性能或由topK小就免历史存储。

## 具体owner与两段PRE

正式Design Delta2 + System Reach2 + Durability2 = 6：受限证据改变“重建良好embedding足以作为长视频历史检索key”的选择，区分key几何、真正被读context及本地/非本地共同预算。不是RAG名称、三backbone榜名或一般有memory主题加分。已确认小缺口，深入采用域，不全附件。

唯一 `MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。实际读recent/view/state整组、MemCam完整机制/成本两段、depth residual段、motion-aware tokenizer/QK完整两段，及“从规则检索到学习式Context Query”完整原理/代价/回退组。现文已讲pose/FoV、query关联、几何可靠性、训练自产history与memory内容因果审计，但未具体说明固定backbone下用局部反冗余/二阶smooth来训练独立检索key。不是凭marker无命中硬I；不重复RAG/WorldModel基本机制，不抢Ch24生成范式或Ch76文档RAG owner。

拟位：MemCam后depth-residual完整段之后，`离屏记忆除了需要推进状态`完整段之前。前者要求depth/pose；新分支在没有该先验的开放生成中学content key，下段再说motion-aware读取。原两段待首次非writer核，未授写/保存/POST/I/DAY。

### 原两段PRE

没有可靠相机或深度先验时，也可直接用自产latent的内容找回非近邻历史，但“能重建画面”不等于“适合挑选互补历史”。一个[受限视频检索分支](https://arxiv.org/html/2606.02553v1)固定生成器，为完成的latent另训紧凑key，令局部时间窗中过高的相似度受罚，同时保重建与二阶平滑，避免top-k都落在近期冗余或因key抖动频繁换集；长程重现不被一律推开。上一已完成latent提出query，key只负责选索引，生成器实际读取对应context；固定attention预算内，非局部条目会占掉部分近期槽位，而不是免费增加历史。

这条分支改善的是读取几何，不恢复已丢失的真实状态，也不能保证漂移query取回正确内容。局部反冗余单项仍有画质指标退步，完整组合在受测共享latent坐标的模型上改善，不等跨codec或每指标支配；更多非局部读取还会减少局部连续性支持。自产key/context历史继续增长，离线造数、encoder训练、每块编码/搜索和真实context读取都付费。短序列、检索质量或净预算不合时，原sink/近期窗口、显式关键帧与可信观测刷新仍合理，不能以较低检索毫秒数签发常数总内存、长期无漂移或物理行动安全。<!-- source-family:SF-2026-ARXIV-2606-02553 -->

## 后续已成事实

R157首次必要/正式6/actual Ch25原两段PRE通过后，root按指定完整双锚真实保存原两段及章末单注；R158唯一实际写后复核通过，整合生效。前文提案仅准备历史，无待POST，不预DAY。
