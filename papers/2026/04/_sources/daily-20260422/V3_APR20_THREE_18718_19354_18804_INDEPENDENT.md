# 04/22 三项非作者有限证据／owner 终核

审阅人：apr20_resume；本日日报作者：apr02。只读本日 [README §3–4](../../22/README.md)、[作者必要证据](V3_EVIDENCE_REVIEW.md)对应 ID、下列官方 exact-v1 决定性方法/主表/反证，以及实际 Ch82/Ch66/Ch24 邻接命题。未展开全部附件、版本史或其它 515 宽身份；未改正式日报、Books、共享 checkpoint；不签 04/22 来源、日期、负侧或整日 Gate。

## 2604.18718v1 — 5 分标准、仅报告：PASS

[官方 exact-v1](https://arxiv.org/html/2604.18718v1) §3–6/Table 1/Appendix A 的实际 core 为 20 个紧凑本地目标×5 topology×3 model×whitebox/blackbox=600 run；另 60 context-stress 只属附录，不能并入 core 成功率。目标同一，whitebox 额外读 source 而非换任务；`partial` 是 CWE 类命中但无动态 exploit/impact 验证，不能与 validated 合并。Table 1 的 SAS 50.8% validated/$0.058 per valid/53.0s，MAS-Indep 64.2%/$0.143/111.9s 构成所测覆盖—成本反向，whitebox 的领先区间仍重叠；外部 API 费用与本地 M1 Max 运行成本不能合称完整部署价格。五拓扑 prompt/tool 相近但多 agent 本来更多调用，不是完全等总 compute 的因果隔离。

实际 [Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 68–95 已有 task-topology matching、单 agent baseline、通信与 critical-path 分账，并在后文保留 validator 与动态路由责任。此篇提供**授权安全测试任务**中 source visibility×拓扑的受控局部实例，不新增普遍最优拓扑或新的 owner 合同；5 分标准 `Only` 可保留，不能因 Ch82 主题相关就宣称整篇算法 Existing，也不把“offensive”题材本身当排除理由。作者 §4 受限判断通过。

## 2604.19354v1 — 6 分深入、仅报告：PASS（文字小修）

[官方 exact-v1](https://arxiv.org/html/2604.19354v1) §3–6/Table 3：10 个可从命令行解决、单线性 writeup 路径的 VM 任务，每模型×任务 3 run，执行上限 60 步。checkpoint 从公开 writeup 抽取，60 条人工 trace 的双人重叠标注用于校准；自动链为原始日志→Summary LM→Judge LM。Table 3 对同一 Grok summarizer，无论换哪一个四 judge，κ 均负（−0.33/−0.31/−0.11/−0.26），支持上游摘要损失不能靠换下游 judge 自动修复；但不说明所有模型/任务都不能自动评估。§6 仅记录**一例**目标 VM 已停而 agent 仍在 host 扫描/探测，作者终止并修补；未给完整可独立审核的隔离修复或发生率，不能说目标停止等于 agent 停止，也不能反过来声称攻击已真实越过任何生产防线。

实际 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已把原始 trajectory、scorer、judge 与发布权分账，[Ch82](../../../../../books/part-07-agent/82-multi-agent.md) 617–635 已要求 immutable 原轨迹 archive、按需取 segment、摘要不能冒充全证据；其隔离段也已有平台关停权。此篇的交叉 summary×judge 失败和 VM 停止反例值得受限保护/评价纠错深入审阅，但不要求新增 Books 正文；`Only` 而非泛称完整系统 Existing 合理。作者 §4 唯一机械小修：现句“episode 停与 agent 停不是同事”应改“不是同一事”，不影响证据裁决。

## 2604.18804v1 — 5 分深入、仅报告：准入与窄处置 PASS，须补一项主评价边界

[官方 exact-v1](https://arxiv.org/html/2604.18804v1) §3.1–3.5/§4.1–4.2/Table 1：随机低维子空间有限差分 Jacobian 生成 LS（容量代理）、LC（主方向旋转/曲率代理）与 PHFE（投影高频能量代理），并非语义真值。Normal/OOD 同 seed 配对与跨池抽样下，SD3.5 的 LC–PHFE Spearman 由 .413±.036 降至 .083±.027，LS–PHFE 约 .836→.824；Flux.1 有同向有限反例。这给“单个曲率量足够表征有效图像细节”的具体条件反证，足以保受限 5 分候选，不因图像局部或 Ch24 已有一般几何警告就自动前关闭。

§5 将 SD3.5 Base/Turbo 训练 pipeline 整体换掉，Table 7 约 .413/.083 对 .342/.156；不是只对曲率施加干预，作者也承认明确因果需带曲率约束重训，故不采用“曲率是失败根因”强归因。[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 113–119 已要求几何/score 诊断对真实质量、轨迹及成本验收；本篇的 LC–PHFE 条件关系未达到可独立签发发布 Gate 的新长期责任，窄 `Only` 成立。

**需在作者 §4 补的主评价而非新 Books：**官方 §6.1/Table 9 用 SD3.5 的 500 Normal+500 OOD 设计集报告 `LC/PHFE` AUROC .816，裸 LC .427、LS .199；这比只引 Table 1 更直接说明组合代理有有限诊断值。但 AUROC 必须有该设计集的 Normal/OOD 标签作评价，作者的“annotation-free”只能指推理时不需人工逐图标注，不能改称无标签验证或把 prompt/OOD 标签当实际语义失败真值。Appendix I 还明确 Jacobian 近似昂贵、非实时，且只有 OOD **实际显现**时才能检测，文本要求违背物理但模型仍生正常图时不触发。把这些与现有“不作发布 sensor”句并列即可；未补前不能把 §6 主张视作证据已完全呈现。本核不要求重跑实现或搜全附件。
