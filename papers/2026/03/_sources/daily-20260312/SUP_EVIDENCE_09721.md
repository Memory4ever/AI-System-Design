# 2603.09721 — Live 优先切换停点：必要原证已读，未完成 Books 判断

2026-10-09 root 新 Live 指令中止历史推进。以下仅暂存 actual 已读，不记候选确认、PRE、整合或 DAY。

作者实际完整 [FrameDiT exact-v1](https://arxiv.org/html/2603.09721v1) §3–6、Tables2–5、A1（含Table6）、B1/B3文字；未核曲线像素、其余附件、代码或复现。raw batch3 完整 v1 AB/current/history、owning arxiv.content/findable registeredMar11UTC02:20:18 与官方 noadvance/announcement 同 BJT 日夹证实际读；current v2 标题变化/acceptedCVPRFindings 无当前撤回纠错信号，不把v2回填本窗。

必要机制：帧token矩阵经row/column learned affine投影为Q/K/V矩阵，按帧矩阵相似形成T×T temporal weights；G仅此global，H与原同spatialindex local temporal并行concat+linear。投影混合和T²仍付费，不称消灭quadratic；式8右侧k^t与文字k^t′不合，不照抄为实现。Nqk降低有损汇聚，Nv、通道及output维度接口需核，不签任意resolution兼容。

A1去softmax/scaling/bias的结构推导不能授实际注意力等价。有限反例：T=N=2,D=1、U/W为I、z1=(1,0),z2=(0,1)，按文字意图的frameFrobenius/sqrt2 logits计算Frame1位置2输出1/(exp(1/sqrt2)+1)=.33023845，而原逐位置temporal attention该query为0、输出.5。因此identity row map不无条件退化为local temporal，未否定有限实验或global分支本身。softmax U只可能约束该线性行组合，后续W/bias不保证original embedding manifold；不授“结构充分”强论点。

实际反侧：Table3 H相对Lattebackground95.40→96.37改善但temporal flickering98.89→97.16、temporalstyle24.76→24.84仅微增，Wan/LTX全指标并非被支配；T2 G落后AR官方重测UCF/Sky。Table4 L2 FID13.44优于softmax13.45，不写全指标best；Table5 Nqk1→2 FVMD1042.76→1044.55/FID14.47→14.81退步，压缩/扩容非每指标单调。B3/T6 concat视频指标优于sigmoidgate，FID却反向；§3.3 pretrained local直接替换时间不连贯为作者必要反侧，preserve+hybrid可用但Kaimingconcat初始化不是功能保持保证。

B1 actual FP16、DDPM250step/SD2VAE/CFG7UCF/256联合image8:video1，fromscratch128/256设置150k/200k、每实验54/280H100h；T2既有paper指标与AR作者checkpoint重测混合，非全matched预算。T2V冻结Latte1B、额外314M、Pexels400k100k/B8/512²、480H100h，未给增量数据/容量的匹配控制，不把收益唯一归MatrixAttention。FVD/FVMD/FID代理、FVMD16framechunks随length改变，不拼原绝对数证明longer更稳。precision训练已披露FP16，不写全precisionND；完整inferencebatch/端到端VAE/长度/并发SLO/seedCI仍未核，原图latency数未实际像素核。

必要首公开轻核：CVF精确题名+作者查询无命中，仅有限搜索；后续精确title搜索恢复官方repo同题四作者/arxivID，GitHub API实际created2026-03-23T10:59:46Z，不证绝对首次公开。OpenReview精确forum/pdf查询无命中，不证明未曾公开；无具名更早原稿冲突，不扩全venue/history。

actual owner仅必要读取Ch24 1191–1239（1191–1217已单独完整重读），文本/图像/视频瓶颈→关联记忆→training mismatch；Ch23/25开篇仍本轮已读。尚未完成具体 gap/PRE，**不将材料可读/原证已读当独立Source或Books通过**。root已实际独读§3指出同索引/复杂度问题，不预计其全部Evidence通过。下次只恢复拟采用命题/具体owner，不重读有效范围。

## 2026-10-09 历史恢复：Source 与逐字 PRE 提案

作者 mar12_model_continue 复用上列有效 actual 原证，重新定点核 exact-v1 §3/§5/§6及当前 Ch24「文本、图像和视频为何不能共享一套性能结论」1193–1206完整局部、Ch23/25开篇。日期与身份复用 SUP_EXACT_BATCH3 的 owning arxiv.content/findable 注册上界及官方公告下界，均落 BJT 2026-03-11；CVPR接受、后来标题变化与 Mar23 repo 创建不移入本窗，也不证明绝对首次。

**评分：2 + 1 + 2 = 5。** 材料的增量仅是帧矩阵共同跨帧权重与原同位置 temporal 路径共存的参数化选择，属于视频生成单组件、可复用的 factorization 约束；因当前具体缺口而深入必要部分，不把成熟 hybrid 原理、全文可得或 Books 决定计分。主张不包括 full-3D 表达等价、任意运动保证、无损压缩或普遍加速。

**Owner：MULTIMODAL-GENERATIVE-PARADIGMS / Ch24。** 当前该局部只列 video 的 temporal state/3D attention/decoder 瓶颈，后文转向关联记忆；Ch24前部的因果 frame-state/hybrid history 是历史可读范围，而不是同一 denoise pass 中跨帧关系的聚合粒度。差额是把「逐位置时间关联」与「全帧共享权重」分开，并保持局部预训练 motion prior 的退路。只拟在表后、现有「不能从图像 diffusion」段后插入下列一段；不改旧表、关联记忆或training mismatch。

> 视频内部还要区分跨帧关系的粒度：同空间位置的 temporal attention 在位移小时便宜且保留局部运动先验，直接连接所有时空 token 则付出更大的关系矩阵；一个受限替代先把每帧 token 矩阵经可学习行、列投影形成 Q/K/V，再由整帧相似度得到共享的跨帧权重，与原逐位置 temporal 分支并行融合。共享权重改变了哪些位置共同读取其他帧，不等于恢复所有逐 token 关系；行压缩仍有损，投影、时间平方项与新增训练也仍付费。[有限视频对照](https://arxiv.org/html/2603.09721v1)支持这条参数化选择，而不支持与 full-3D Attention 表达等价或任意长度稳定；冻结 Latte 后的新增容量与数据未获完整匹配控制，部分 flickering 指标反退。直接替掉预训练局部分支还会失去时间连贯，因此大位移收益、压缩细节或完整质量—成本验收不足时，应保留局部路径、减弱压缩或回退原 dense 生成器。<!-- source-family:SF-2026-ARXIV-2603-09721 -->

逐字末注拟为：`SF-2026-ARXIV-2603-09721` — Daily `2026-03-12`补查；[FrameDiT exact-v1](https://arxiv.org/html/2603.09721v1) §3/§5–6、A1/B1/B3及Tables2–6。2+1+2=5，具体frame-level权重与local temporal共存差额深入；不采A1无条件等价、manifold保证或唯一归因，FVD/FVMD/FID与T2V配置、退步与费用见证据记录。未核图像精数、代码或复现；Source/PRE待独立复核，正文尚未写入。

普通可执行停点：等待独立 reviewer 对必要 Source/date 与逐字 PRE；通过后向 root 申请一段与本人末注窄锁。不是外部材料终态，不授候选最终同步、Books实际整合或 DAY。

后续实际结果：mar12_independent_continue必要Source/date/5分/真实gap与逐字PRE通过；root授窄锁后作者实际写Ch24新1208/本人1879末注并顺读1193–1217，限定diff-check通过。root非writer实际顺读1193–1218完整邻接，确认粒度/代价/旧路径/因果边界，**actualPOST通过**，窄锁立即释放。1家族/1段实际整合，正式Report尚待root合并授权，不授DAY。

## 本次真实 Gate 状态

root此前实际Ch24 1193–1218表后完整邻接POST通过，作者证据note已记录；本次获准仅同步本人章末注真实结果。 未核实现或复现，不授日级验收；本项普通待办只剩授权后的Report同步。
