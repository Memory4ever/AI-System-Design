# 11388 必要安全 Source / 具体 owner PRE

作者mar14_supplement；精确v1 `SUP_CORE_11388.raw`实际完整读§3–7、Tables2–5、AppendixA2损失与A3人口（不追攻击战术/所有相关文献）。首包准入/日期独核复用，2+2+2=6标准最低，安全/核心主张反侧与owner差额需要受影响内容深入。

## 必要机制与原证

§4.1从harmful训练样本删除显式harmful intent但保留harmless events/帮助措辞，由GPT4o生成sanitized query，GPT4o能提供affirmative response才通过，失败换seed重抽。这个heuristic不是可靠安全truth。§4.2 rephrase level1保同entities/events/actions，level2/3删除部分语义，不是保义token替换；§4.3从layer15起末token平均cosine、topK5/10/15/20，rejected benign更近，是相关而非唯一causal carrier。T2随着低相似度改写RR降低，但混有semantic任务/实体变化，不能授必要充分。

§5把matched triggers转作benign训练监督，同Eq1/SFT/P-SFT/RLVR与harmful-refusal目标混合。248 matched数据与约22000Alpaca比较，不是总token/steps匹配。§3.2+A2的P-SFT是affirmative prefix接refusal target，RLVR是rule-reward/PPO+KL，未详细给执行hyperparameters；不以泛化所有alignment算法采用。

## 评价反侧与不采用

§3 rule keyword absence计算ASR，keyword presence计算RR，**不测semantic harmfulness/答案质量或真实安全**。T3 Llama3U Alpaca KoalaRR57.22→matched21.11同时SorryBenchASR1.36→7.95；原baselineRR5→21.11，OrBenchH16.83→59.21。Qwen2.5U RR15>base3.33/ASR4.85>Alpaca.45。T4 RLVR matchedRR4.44<base5仅局部，OrBench57.09>16.83，同时ASR25.33>Alpaca8.22。§5正文“RR below baseline”不是表中普遍事实；**不采用belowbaseline/保安全pareto优越**。T5 defaultRR21.11/ASR7.95 vslevel2RR54.56/ASR3.46支持两轴tradeoff非免费解除安全。

Llama2chat7B、Llama3U8B、Qwen2.5U7B有限models；Koala/JBenchB/GSM8K/SQL1K/OrBenchH与SorryBench/JBenchH/HExPHI分开人口。A3说明SorryBench只basequeries，P-SFT另prefill attack口径，不能外推未知攻击。§7外部LLM漏意图/oversanitize、规则detector、未优化数据scale/composition直接限制。Hardware/precision、训练batch/learningrate/epochs/alphafinal/sampling、response长度和repeatsCI均Not Disclosed；在线concurrency/SLO不适用本训练机制。无代码/复现证据。

## 实际 owner 差额

实际Ch29 `TRAIN-SFT` Demonstration→数学CE 37–80及response监督84–113/安全蒸馏838–860、Ch27 341–353instruction-hierarchy生成控制、Ch30入口与Ch31 142–170偏好安全训练读过。Ch72 24–43已有benign标签不能认证update安全；不重复其治理命题。Ch29当前能承载示范重新加权条件行为，但没有从同一harmful示范剥离intent、保留benign discourse来做matched affirmative监督的具体分支。Ch27已有合法同类请求hierarchycontrols不等这种refusal association诊断/监督构造；Ch31奖励目标也未覆盖。唯一owner建议Ch29，在demonstration schema/skew说明之后、长demonstration ChunkFT之前以下两段，不写第二owner。parent先实际必要Source/具体PRE再窄写，我POST。

### 拟正文（尚未写）

拒绝示范还可能同时奖励了与风险无关的措辞：一条请求中的普通活动、求助形式与真正有害意图共同出现时，条件最大似然不会自行标明哪一部分应触发拒绝。泛化良性的 instruction 数据在分布接近时仍是便宜基线；更窄的补充分支则从同一 harmful 示范中剥离显式有害意图、保留无害活动与话语结构，经外部模型和审核产生可回答的配对监督，再与原 refusal targets 混合。它试图把风险意图与邻近良性语境分开，不是移除原安全示范或删除一个已证唯一的内部拒绝方向。末token hidden-state 相似度与改写后的拒绝变化只用于发现这种关联，不能充当因果或安全证书。<!-- source-family:SF-2026-ARXIV-2603-11388 -->

这条分支增加外部生成、意图审核、配比选择与训练/回归成本，过滤器仍可能漏掉隐含风险或过度清洗语境。[有限原证](https://arxiv.org/html/2603.11388v1#S5)中的248条 matched data 与约22000条通用数据并非等训练预算，规则关键词测得的拒绝和攻击成功率也不等语义安全或有用回答：部分 benign 拒绝低于通用数据训练，却仍高于原模型，harmful 成功率同时上升。应分别检验合法请求响应、真实 harmful completion、通用能力及构造/训练总费用，不把平均 trade-off 签发为Pareto改善或发布许可。语境匹配、审核或独立行为回归不可靠时，保留已核验的普通 demonstration、保守数据配比和第72章的独立policy/effect gate，而非让外部模型的肯定回答取代安全判断。
