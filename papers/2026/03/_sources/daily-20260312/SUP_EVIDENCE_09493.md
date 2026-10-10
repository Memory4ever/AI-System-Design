# 2603.09493 — EvoPrompt：历史方向固定与历史作用保留不是同一保证

作者 mar12_model_continue，2026-10-09恢复；只属Daily03-12补窗03-11。冻结完整题摘/准入复用SUP_EXACT_BATCH3及本日独立校准；必要实际读取[exact-v1](https://arxiv.org/html/2603.09493v1) §3–5、Eq5–14、Tables1–4，不核曲线像素/代码/复现。current标题Guided Prompt Evolution与v1 Evolving Prompt Adaptation分清；当前无withdraw/comments安全纠错，不以v2/v3或改标题触发全版本比较。未见具体具名先稿冲突，不扩会议或作者全集。

日期复用原batch3：owning arxiv.content/findable的registered Mar11UTC02:14:55与官方noadvance/公告下界共同夹在BJT2026-03-11；Submitted不单独证明公开，后来current不回填。

**评分：2+1+2=5。** 增量是低秩prompt projector的训练时间参数化：每epoch保留已学方向、重新学习它们的scalar幅度并追加新方向；单适配组件、稳定容量/保留约束。因具体长期gap深入，不把成熟LoRA/Soft-HGR或可映owner直接计分。

## 必要机制、反证与采用边界

§3.2共同E生成visual/text各层prompt，两个modality各有自己的W_shared，而非两个encoder共用同一矩阵；layer adapter AB加在shared projector上，插token，不是直接改冻结CLIP权重。§3.3 Eq8 normalized AB/Frobenius、Eq9累加历史项：历史方向冻结，所有历史α与新方向仍可训练，W_shared固定；rank按epoch经验递减，不证明累计rank或存储恒定。旧α可为0或改变，因此历史作用可消失或混合，固定方向不保预测不变；E等可学接口亦不能由冻结CLIP推出无遗忘。实际只采用该有限参数化分支，不采用论文“forgetting-free”普遍结论。

§3.4 Eq12 tr(C_v C_t)是两个empirical covariance的乘积正则，不直接强制每个modal的offdiagonal为0、更不推出独立。作者侧简单反例：C_v=[[1,1],[1,1]], C_t=[[1,-1],[-1,1]]均PSD，乘积0但各modal维度强相关；只反驳无条件orthogonality/independence保证，不否认有限训练收益。Eq13仍有原frozenCLIP输出的constancy正则，消融不能把保留效果唯一归因历史方向。

§4 ViT-B/16冻结两encoder、单A800、通常16shot/11dataset、E五向量d512、prompt length5、layers6–12、three seeds mean top1；未披露本轮可核precision、完整CI/方差、推理端到端batch之外并发/SLO。Table1平均novel77.76高于CLIP74.22却不等所有切片保留：FGVCAircraft的novel39.14高于CLIP36.29，但DTD64.10低于MMA65.63；OxfordPets base95.30也低于多baseline。T2 targetmean66.82仅高MMA66.61，Aircraft24.20低MMA25.33，OxfordPets90.40低MaPLe90.49。T3 Sketch49.40低PromptSRC49.55。T4去E.T. base77.42更好/novel70.25更差，说明取舍，不是每metric必优。三seed平均未给variance不签显著差异。

Table4c只5epoch trainable0.764M、training4.5ms/image、FPS1282.1/batch100；MMA0.675M/2.2ms更便宜，PromptSRC0.046M更少参数，不能写最少/最快。历史方向存储/累加、投影与双encoder prompt计算、frozenCLIP constancy前向、covariance及超参/多seed训练仍付费；0.764M trainable不是总resident或部署内存。正文说Appendix给schedule/algorithm，但本HTML无附录section；本采用不需要具体rank数值配方，不把普通可选recipe缺失转外部阻塞。

## Owner 与逐字 PRE

actual读取Ch30低秩初始化/scale局部、187–254容量论证以及Ch29/31开篇；Ch23 64–98 projectors/几何局部用于分责。Owner **TRAIN-LORA / Ch30**：现有module-shared basis及未来时间core不拥有每训练epoch固定historical direction、可改historical scalar这条分支；Ch23只拥有prompt表示入口，不重复训练算法。拟在Ch30「共享方向还可以跨时间」前插入一段，保留原跨模块与跨域时间分支。

> 共享方向还可以沿训练阶段累积，而不预设同一组 basis 永久覆盖任务。一个受限的视觉—语言 prompt 适配分支，将各层低秩 projector 增量分成归一化矩阵方向和 scalar 幅度；每个阶段冻结此前方向，只重新学习旧幅度并加入新方向，晚期新项还可使用更低 rank。这固定了旧方向的坐标，却没有固定其作用：旧幅度变小甚至为零仍可改变预测，累计方向存储也不会因晚期 rank 下降自动恒定。[有限 CLIP 对照](https://arxiv.org/html/2603.09493v1)还联合原模型输出正则，部分任务反退，不证明无遗忘或把收益唯一归因这条更新规则。历史保存与累加、prompt 投影、参考前向和调参都付费；旧任务回归、方向失配或累计预算不合算时，应保留普通静态 LoRA、独立 prompt 适配与逐任务保留验收，而不是用冻结基座替代行为检查。<!-- source-family:SF-2026-ARXIV-2603-09493 -->

末注拟为：`SF-2026-ARXIV-2603-09493` — Daily `2026-03-12`补查；[EvoPrompt exact-v1](https://arxiv.org/html/2603.09493v1) §3–5/Eq5–14/Tables1–4。2+1+2=5，历史方向与可学习幅度分责gap深入；不采forgetting-free、covariance去相关/独立保证或最少参数/最快。有限CLIP人口、原输出正则混杂、任务退步与历史/参考费用保留。未核图像点位、实现或复现；Source/PRE待独立复核，正文未写。

当前可执行待办为独立Source/date/逐字PRE及root窄锁/actual POST；不授Books完成或DAY，无必要外部阻塞。

后续实际：独立reviewer Source/date/5分/Ch30真实gap及逐字PRE通过；root授窄锁，作者落新217单段和820本人末注、顺读211–225并限定diffcheck通过，锁立即释放。root非writer实际顺读共享模块→阶段方向/幅度→timecore→安全行完整邻接，actualPOST PASS。1家族/1段实际整合，Report待root合并授权，不授DAY。

## 本次真实 Gate 状态

root此前实际Ch30 211–225共享模块→epoch→跨时间core→安全行POST通过，作者证据note已记录；本次获准仅同步本人章末注真实结果。 未核实现或复现，不授日级验收；本项普通待办只剩授权后的Report同步。
