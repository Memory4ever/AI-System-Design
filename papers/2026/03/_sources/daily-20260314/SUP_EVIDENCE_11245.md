# 11245 用户模拟：必要 Source 与具体已有覆盖提案

mar14_supplement，精确[2603.11245v1](https://arxiv.org/html/2603.11245v1)。原HTML `SUP_NECESSARY_11245.raw`/UTC/status见`SUP_NEXT_SOURCE_MANIFEST_RESULT.json`。完整题摘/十一作者/v1history/可见当前事件说明为`SUP_ABS_11245`，最新v2不存在具体纠错宣告，不由版本号扩比；未识别具名更早正文信号。Mar13官方上下界夹证见`SUP_DATE_SECOND.md`及`SUP_DATE_11245.raw`，v1 Wed19:12:31UTC晚截止；不单用Submitted或Registered当首次公开。

## 实际必要读取与评分

实际精确v1 §3统计定义/完整Table1、§4受控setup、§5–7关键结果/直接边界、A1角色扮演与QC全部必要段/A4操作性全部指标、A5/Fig7和A8/Table3。不是只读包/摘要，也未读所有survey/example interactions/模型列表或代码。

新增命题 **2+1+2=5标准完成**：固定agent/task/reward下让人类替换simulator，发现行为生成的结果人口偏移与反馈判分偏移是不同对象、general capability不等proxy fidelity。2分是该有控制的人类反侧修正评价设计，不是借用Dice/ECE；Reach1限单个evaluation pipeline/user-proxy责任，未给生命周期或任意simulator迁移保证；Durability2为可复用的角色/人口/construct边界。候选准入已由root完整题摘校准，具体owner NC仍待实际独核，不授DAY。

## 支持与关键反侧

451 Prolific参与者在165个τ-bench airline/retail任务上角色扮演，三独立annotator batches=495轨迹，与31user simulator交互同GPT5.2 agent/规则reward。它们不是451真实客户自然日志，也不是population-random deployment。A1接口暴露reasoning/tool traces可能改变体验；GPT5 QC仅51作者标注控制，score80只保pass traces，FP2/FN6以及已被proxy筛选的人口限制保留，不认证人类基线无偏。

D1–4由lexicon/regex代理；Formal用em/en dash，uncertainty/clarification是词面匹配，frontloaded words/ID不等真实信息量。Dice对aggregate mean取min/max（均0给100）非人类不可区分证书。ECE是按task difficulty分bin比较proxy/human**result rate**的绝对gap，不是模型confidence校准概率。USI等权汇总D1–4、1−ECE与1−MAE；无survey时五项人口分母不同。三batch mean±std是human参考变化，不是全部simulator/模型独立重复CI。

同agent对照有多数general proxy的success比human63.6%高、specialized全部更低，故不能声称每种simulator都easy或更强ELO必更真实。§6 GPT5.1对体验偏高、task completion反而保守；“反馈都更positive”须收窄到quality而非所有success标签。binary state reward与用户感知quality不同不证明用户感知替代实际state/policy truth。A5 CramérV=.168不等数学正交/零联系；部分policy-constrained人类标签reward1也需要不同construct分账，不照录“无任何质量信息”。A8换Gemini3.1Pro只有五proxy/一次run，human参照仍GPT5.2 agent，作者承认绝对USI不可直比；相近排序不证明general跨agent外部效度。作者结论保留synthetic benchmark快速可复现用途，无线上SLO/真实生产发生率、完整调用/标注费、precision/长度和重复CI保证，未核artifact/复现。

## 实际 Ch66 具体 NC

ROADMAP owner `PLATFORM-EVALUATION-SYSTEM`。[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际连续读1321–1354完整User Simulator小节与前后：非合作/persona policy绑定、合成分布不代表production、参考人类对话与fixedassistant/taskoutcome/judge身份分离、真实human–proxy结果分布校准、相同task/assistant/tools/turnbudget与监督预算、无真实参照时仅预筛选。此处具体承载本稿两角色与人类参照边界，不是标题相关就NC。

另实际读2668–2692含ranking fidelity与construct fidelity段：满意度、完成叙述与真实environment outcome不同向，human ceiling/close-pair/确定性outcome要分开。不把USI等权新指标名或31proxy新排名追加正文，也不用主观满意替代policy/state。当前新版稿并未提出这些设计的新可靠成立条件；本实证验证与已读负侧可留日报。

拟处置：**标准完成/已有覆盖，Books新写0**。若root实际核原证和上述完整owner后发现独立未承载命题再定点重开，不预授NC，不重读全部A3survey或攻击无关素材。无共享Books写锁。
