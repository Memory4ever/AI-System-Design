# RAMP17891：必要证据与中心处置待独核

root sole准备，仅03-20补03-19；原准入/公开日及2+2+2=6复用，不重新迁日。[精确v1](https://arxiv.org/html/2603.17891v1)与[当前身份页](https://arxiv.org/abs/2603.17891)实际读；单v1/两作者，无当前页影响采用的撤回说明。必要§3.1–3.5/Eq8–21/Alg1、§4.2–4.5/Eq22–23/Alg2/Tables4–5、§5.2–5.7/Tables8–17、§6.1–6.4/Tables18–22已读。未核代码、全部附录/图像或复现，不扩其它量化论文。

## 采用边界

SAC按layer calibration统计、结构特征、前层位宽与运行平均预算提出3/4/5/6位，整轮量化PPL作为terminal reward，经replay更新；这是离线allocation，不是逐token自适应。归一化特征跨模型迁移仍须每模型重新校准。§3.1 Eq8/Alg1预算是layer位宽算术平均，不含各矩阵元素数、group scale、未量化embedding/head及runtime驻留；不能等同实际byte上限。GGUF导出另映射nominal bits到具体format并保存type/scales，执行仍调用backend kernel，“kernel-free”只表示无需新写专用kernel。

## 中心不一致与定点反侧

原文质量优先/严格预算的配方尚不能照录：Eq19对同幅PPL相对变化，改善奖励系数+10、退步惩罚-5；下文却称退步惩罚更重，方向相反。Eq20在4.25处为-0.5，而4.25+epsilon变为-20epsilon²、趋近0，超界略多可反而受更少罚；这不是不可违反的cliff预算约束。此为直接式代入，不否定学习policy原则，也不声称作者代码必然使用这些式。

导出身份亦未闭合：§4.2.3说存W/alpha且dequant自动无损恢复，Alg2却对Q/K/V及gate/up乘channel scale、对应RMSNorm乘逆scale。两种约定可各有配对等价，但不能把文字拼成已经核验的同一执行链；整数quant/dequant自身还非lossless。需要具体scale坐标、norm/权重补偿与实际导出schema才能采用这个精确artifact机制。

评价只限作者Llama/Mistral和WikiText/四commonsense tasks；§5.4 batch1/context2048/FP32/三次mean±std措辞不由表中单点补成已披露CI。Table16迁移差0.01/0.02 PPL不证明唯一architecture因果，仍有target calibration与选择费用。Table5跨平台数值明确来自public llama.cpp benchmarks，不是同RAMP artifact/相同配置的实测复现；不采3.05倍/生产可用/全平台等价SLO。全部calibration、搜索整轮quant/eval、目标重校准、导出/backend和质量回归付费。

## Books判断提案

实际Ch49:1110–1195完整anchor/PTQ/physical-layout/质量验收邻接及2060–2090闭环precision-search已读；已有正文明确nominal bit不等物理预算、proposal不拥有runtime验收。当前候选新主张是可迁移layer policy及其quality-first/ScaleFold导出耦合，但中心奖励和导出身份不齐，不以主题覆盖冒充已证新配方，也不强行加一段相似通用原则。提案保持6分，**争议/暂缓、Books0**；一次材料请求仅指Eq19–20实际奖励/硬预算执行，以及ScaleFold→GGUF的同一坐标与实现/勘误。保留原证与有效离线选择思路，不授正面性能/部署/安全保证；非外部访问失败、非范围排除。

交resume_mar17非准备者有限必要证据/实际owner复核；尚未独核或计安全终态，不授DAY。

## 非准备者有限独核与安全终态

2026-10-12 resume_mar17实际独读exact-v1必要§3.1–3.4/Eq8–20 L362–528、Alg1/Eq21 L535–576、§4.2.1–4.4/Eq22–23/Alg2 L624–705（含public benchmark性质）、§5.2–5.6/T8–16 L748–901；支持及决定性反侧足即止，未冒读全部1202行、所有附录/图像或实现。原root更深实读范围分层复用，不由准备者记录冒作本人全读。

独算PPL相对改善/退步各.1，Eq19为+1与-.5，实际方向与“退步更重”文字相反。Eq20在4.25为-.5，在4.2501约-0.0000002；增一点超界反而少罚，不能从此函数授硬预算cliff。Eq8/Alg1仍是layer算术mean，量大小/scales和映射GGUF真实bpw不相同。Alg2可在配对输入尺度/权重列补偿前提保持量化前映射，但W/alpha导出声称与W乘s/RMSNorm逆s的同一坐标身份、runtime如何读/恢复未闭合；不能把alpha等于s或其倒数自行补造，更不能以量化dequant称lossless。有效离线layer-policy思路不否定，当前不采其quality-first/hardbudget/ScaleFold精确耦合或headline。

实际Ch49完整1110–1195和2060–2094＋48/50入口已顺读；已有具体physical layout/artifact逐格式与完整部署验收不支持把本新配方当已证NC。新policy/导出耦合关键桥仍争议，不为省时新增通用相似原则段。**原6分、中心终态隔离/暂缓Books0有限PASS**，非访问受阻/范围EX/降分/假已有覆盖，不授正面Evidence/Coverage/质量性能或部署保证。一次精确请求保持：Eq19–20实际奖励/硬budget执行或勘误，ScaleFold→GGUF同一尺度坐标/Norm补偿/schema/实际消费；只返回后定点重开这些桥。root接纳后才同步本日安全终态；不授DAY。
