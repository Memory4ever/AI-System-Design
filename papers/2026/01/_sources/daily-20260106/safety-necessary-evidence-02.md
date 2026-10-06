# Jan06 安全必要命题停点（二）

本记录只是实际精确v1必要读取，不代替候选冻结、Books或日级Gate。原cache formula projection可能丢小于号；ActErase Eq5已回到原HTML确认，不用投影授保证。

## MalOptBench 2601.00213v1

完整题摘准入对象是合法形式的优化任务与恶意目标相结合的评价盲区；2+1+2=5，安全变化深入必要命题。实际§3/4/5.1前7000字符（truncated=true，未称本节全读）、5.2/5.3/Limitations。四种优化任务/60原prompt与改写，13模型；GPT4o同时参与构建/审查/评价不是独立危害真值。ASR聚合三response任一成功，harm score优先从成功中随机选，不等单次请求风险；ASR/harm相关不是独立验证。没有实际运行算法/目标effect，不能叫真实危害或生产事故率。

所测两plug-and-play防御原请求有效、改写条件弱，并有XSTest误拒，不推所有防御失效。token删除的importance实验不是Attention电路因果，不能据它归因安全token被忽略。硬件、precision、独立重复与线上SLO未采用；主信号是目标语义和合法形式分账，当前Ch72 552–558 dual-use授权、608–612 goal alignment组合授权已定点读，root实际必要source及Ch72 542–615核通过具体已有覆盖，不冒充主题已有。

## ActErase 2601.00267v1

完整题摘与实际§3.1–3.3/4.1–4.2/4.5、A1–3/C必要反证；2+1+2=5，deployment-only concept抑制的安全变化深入。source/target prompt双路径提取FFN激活，mask使用Is≥tau且Is<It，冻结source均值在新去噪路径patch，不是删除base weights或训练数据。多concept mask OR、重叠位置平均，C中10concept组合严重生成退化，不能从单concept强结果授组合完备。

原§4.1称50step，A3与threshold表称30step；精确实验recipe冲突隔离，机制与有界反证不依赖选择某一数字。SD1.5/RTX4090，I2P4703/NudeNet与COCO30000/FID/CLIP是有限sensor；Table3多concept逊于TRCE(T+V)，CLIP并非全优。§4.5明确293秒准备与800秒生成1000图，不是zero-setup/production SLO；precision/seed uncertainty=Not Disclosed。training-free仍有prompt生成、双路径准备、mask/activation与推理注入state。原Ch24 1131–1140已经有trajectory rescale sensor/controller与权重删除分账，缺masked source-activation patch及overlap组合失效对象；root必要原源→owner授权后实际Ch24 1141/1143两段+1487首注写入，root非作者actual POST通过，锁释放。Ch23末/25首与当前局部衔接实际已读，不扩大完整概念删除/安全保证。

## Trajectory Guard 2601.00516v1

完整题摘、实际Methodology/Architecture/HybridLoss/Implementation、Dataset/Synthesis/Splits、Metrics/Error/Latency/Ablation/Limitations。新增对象只MiniLM/MLP+GRU重建与in-batch triplet组合的局部task/trajectory anomaly recipe，1+1+2=4；安全deployment变化已读必要范围，不因评分4跳过。5752正常train、1015validation、GPT5扰动、阈值取validation-F1；5822test中外部RAS3802/WhoWhen184全为anomaly，无normal支持，所以external recall不授FPR/总F1或生产coverage。

T4/Xeon与Phi3mini A100/API judge异构计时，32.48ms不授端到端permission-path SLO；long valid sequences重建误报、11+step F1退化必须保。重建coherence和task alignment不等授权或实际工具effect，异常sensor不能获得commit权。组合模块/所测dual-loss增益为局部实现，未建立替代独立policy gate的条件或新的安全保证；1+1+2=4，仅报告具体recipe；root实际必要结构/metrics/latency/error证据核及评分对象校准通过。未复现。
