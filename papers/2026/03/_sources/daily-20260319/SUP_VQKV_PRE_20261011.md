# VQKV 2603.16435：必要原证与 actual owner / PRE

作者 resume_mar18；仅03-19补03-18。2+2+2=6给residual codebook/index KV与分块重建/批量编码接口，已有知识差额作必要深入。[精确v1](https://arxiv.org/html/2603.16435v1)§3.1–3.4/Eq1–13、§4.1–4.4/Tables1–3与§6直接成本实际读；不遍全部图像/附录/code或复现。身份/日级夹证复用本日批次，不将Submitted当公开。

## 必要原证 / 关键反侧

独立冻结backbone，但用约10M collected KV/0.1%OpenWebText训练K/V独立residual SimVQ codebook，lr.001/B65536；training-free仅“不更新LM参数”不等零训练/校准。每KVvector逐stage最近entry、残差继续量化，读取求和重建；codebook projectionW是否吸收在entry、正文index/向量记号混用不作为精确公式实现保证。不要把residual stages说成独立子空间或不损信息。PostRoPEK较难重建，56stageK vs16/10stageV、S1024/512或65536只是两个checkpoint设置，不授所有K/V普遍同配置。

Prefill保留初4/recent1024高精度且原完整KV计算，compressed middle只后续部署；Decode保留localtail，每1024step整段压缩以摊串行residualstage和distance计算，blockwise distance避免峰值；attention融合按需重建当前tile的K/V不整序列materialize。不是LOOKAT先计算query-centroidtable再索引，也不删旧位置；“discard oldest”是退出localwindow转code，不能写删除历史。Codebook、index、pinned高精度区、conversion frontier/temporarytile以及longcontext全部读费必须分账。Eq13仅16bit向量vs理想Nlog2S索引，不包含codebook/W、实际整数packing/metadata、init/local/临时区；82.8%不等整GPU或短序列节省。

评价两模型LLaMA3.1-8B/LLaMA3.2-3B，A800多卡/FP16/OpenCompass/32Ktruncation/LongBench,NIAH,RULER；exact engine/library/driver、GPU数/TP、batch、output/eval decoding配置、concurrency、SLO、seed/repeatCI与trainingsteps=NotDisclosed。Baseline KIVI75%、ASVD/Palu80%、SnapKV保2048middle，NIAH部分取另文不是samehardware重跑，不全部归codebook单因果。Table1 avg33.1<full33.5/3B32.2<32.3，8B多个single/multidoc/summary/codetask反退；Table3 50% ASVD33.6>VQ33.5，不采“所有设置最优”。RULER32K 8B79.71<full90.16、3B67.89<78.25，与98.6%LongBench平均不是同协议；不授近无损所有length或任务。

§4.3作者写singleRTX4090(48GB)/FP16/FlashAttention、65536prompt/190kvs824k生成存储峰，设备名称/容量按原文保留但未有实际修改或详细配置桥，不自行改成标准器件或认证4.3倍context能力。超过32K生成容量未等价验证长程任务质量；无吞吐/端到端latency证据。§6明确VQ额外decode compute仍待优化，与实现了customTriton/FlashAttention并存，不授省HBM必加速。支持有限表示与消费接口，未核codebook实现、packing或kernel。

## actual sole INFER-KV-CACHE

已重载ROADMAP、Books合同/背景/学习理念/写法与LS；actualCh45 680–735与1176–1192完整局部、Ch44/46开篇已读。现Ch45 712–714 LOOKAT说明key centroid-index直接查querytable、V仍FP16；708–710量化后lossless codec与frontier分责；696–706不规则layout/codecfusion。没有同时K/V residualcodebook且消费者分块重建、prefillfull与decode批量tail编码的接口，非单纯新增VQ名称。唯一INFER-KV-CACHE，不复制Ch49 kernel教程。拟LOOKAT反侧段之后/二维mixed sparse之前一段＋静态注，未获PRE独核/锁，未写。

### 一段逐字 PRE

码本也可同时表示 K 与 V，而不只让 query 直接查 key 的内积表。一条[受限残差量化分支](https://arxiv.org/html/2603.16435v1)用多个码本逐次编码向量的剩余误差，历史保存索引，Attention 在当前 tile 内查表求和重建 K/V；初始与近期区域保留高精度，Prefill 仍读原完整 KV，Decode 则让退出近期窗口的一段批量编码，以摊薄最近码点搜索和串行 residual stages。冻结 LM 不等无训练，码本拟合、驻留、索引 packing、高精度 tail 与临时重建都占预算；理想索引位数不代表整 GPU 节省，容量可容纳的生成长度也不认证远程引用质量。它与前述直接 query 查表是不同消费者，K/V 误差和码本版本须连同模型、RoPE、编码 frontier 与真实 kernel 验收；受测长 context 和任务仍有反退，省字节未证明完整 Decode 更快。校准漂移、编码难摊销或质量不通过时，保留较温和量化、原窗口和 FullKV，不把重建保真代理当成无损服务保证。<!-- source-family:SF-2026-ARXIV-2603-16435 -->

### 静态来源注

- `SF-2026-ARXIV-2603-16435` — [VQKV exact-v1](https://arxiv.org/html/2603.16435v1)必要§3/Eq1–13/4/Tables1–3/6；采用K/V residualcodebook索引与tile重建、highprecision窗口/批量tail编码分责，training-free仅LM冻结。理想index比率、设备容量叙述、LongBench/RULER反侧与未给decode延迟保留，不授无损/全context能力或生产加速；未核packing/kernel/代码或复現。

## root actual POST（非写入者）

作者依窄锁写后，root实际顺读Ch45完整700–730局部：Mosaic消费者/layout→lossless codec/frontier→LOOKAT query直接表消费→新716残差K/V tile重建→混合稀疏状态/阶段重压缩；并读末8行与本项静态末注，逐字回对上述PRE和已通过必要Source。没有把残差码本改成独立子空间、删除历史或LOOKAT路径；prefill完整/Decode批量tail、高精度与重建暂存预算准确，容量/质量/latency及校准退路均近文。唯一INFER-KV-CACHE，未复制Ch49教程或改其他family。本人注精确版本/边界一致，限定diff-check通过；**本项actualPOST通过，释放Ch45窄锁**。不授其他候选、全覆盖或整日DAY；不再为同步流程身份改写Books静态注。
