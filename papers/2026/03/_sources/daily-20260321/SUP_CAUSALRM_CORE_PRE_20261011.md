# CausalRM18736 必要原证 / owner / PRE

准备者root，仅03-21补03-20自然日，独立准入日期夹证复用，不迁旧候选。拟2+2+2=6，反馈观测与标签两个通道的联合校正边界确有知识差额深入，非给成熟IPS/DR本身新分。未写/未独核/DAY未授。

## Necessary exact-v1

[HTML](https://arxiv.org/html/2603.18736v1) §2.2/3.1–3.4/Eqs4–17/Alg1、§4.1–4.7/Tables1–5/Limitations、AppendixA必要Theorems1–3及bias/variance边界、B数据生成/冻结MLP/GRPO配置实际读。不核实现/复现或遍references。

- 目标全prompt-response人口D的真实二元偏好损失，观测子集O中既有o选择又有r标签flip。class-conditional rho01/rho10总和<1，解2×2损失线性系统得noise surrogate；known率时条件期望校正，但anchor估计需weak separability和足够极端样本，拟合extreme不是无条件真实人类偏好。极接近退化时分母变小/负损失放大。任意context/user-dependent noise不在常数rho配方内。
- IPS对O的surrogate按1/p重权，必须有全D的o和充分support，非仅click日志就可知未观察总体。DR补全error model再校正观测残差，所谓double robustness不豁免正确noise ratios、反馈可识别/positivity；小p仍可能巨大权重。AppendixA Theorem2 imputer写准确逐样本noisy loss，并非一般x-only模型自然满足；不授任意MNAR或hidden user confounding。Theorem3需imputer符号/误差条件，不采总是降方差；校正surrogate可为负，原proof positivity不得普遍化。Alg1选anchor用ζ、求ρ行却写θ，与§3.4/B proxy说明不一致，不照可执行recipe。
- 实验不是实际观测用户click：HelpSteer/UltraFeedback/PKU-SafeRLHF标量median二值化作proxy r*，再按r*设p并合成flip，独立原test作oracle。支持该构造中的两通道有限对照，不认证真实用户因果无偏或普遍真实偏好。Table1部分MAE中DR不优于IPS，Table3合成目标拟合不是部署效果。
- 冻结LLM embeddings＋256/64/1 MLP，propensity/proxy/imputer额外训练，32 H800与Xeon披露但precision/任务各GPU分配、全walltime/seedCI/concurrency/SLO未披露。主文与B learning rate下界不同，不照recipe。下游Qwen2.5-7B/Llama2-7B GRPO，batch256、rollout4/T1、KL.001、prompt/response各2048、20steps、DeepSeekV3 safetyjudge；有限安全score不是human truth/benign效用保持或公平全预算。
- 噪声模型、观察支持、极端anchor/权重或独立行为不能验时保留Unknown/受控人工偏好，不能把no feedback当负面、click当true reward，亦不由RM loss下降签安全发布。

## Actual owner delta

`TRAIN-RLHF` Ch31：实际76–125 reward/标签通道、153–185 preference身份/噪声与wildfeedback，Ch30/32入口实际读。已有后续等级反馈、随机标签/隐私通道，没有**观测选择率与标签错误必须分开联合校正**及anchor/positivity/DR不豁免noise条件。只两段置WildReward119后隐私通道121前，不重复安全authority。

## 两段逐字 PRE

把点击、复制或赞踩用作 reward 时，还要拆开两个观测通道：用户是否留下反馈，以及留下的标签是否表达真实偏好。只给有反馈样本重加权，仍可能学到错误标签；只校正标签，仍会把偏向强烈意见的人口当作全部请求。一条有条件的分支先用二元标签噪声矩阵修正每样本损失，再按反馈被观察的 propensity 校正总体贡献；附加误差补全模型的 DR 分支，可以在规定条件下放松 propensity 与补全两者都准确的要求，但不豁免标签噪声率和可识别前提。训练方需要完整观测人口、支持域与可校准噪声，不能仅凭日志里存在一个点击就自动恢复真实偏好。<!-- source-family:SF-2026-ARXIV-2603-18736 -->

这种联合校正增加 propensity、proxy/anchor 与误差模型的训练费用；极小观察率和接近不可逆的噪声矩阵会放大权重或损失，anchor 假设不成立、用户差异无法被观测条件解释时也不能靠“因果”名称消除偏差。[CausalRM 的受限对照](https://arxiv.org/html/2603.18736v1)由已有偏好 proxy 合成选择和翻转噪声，不是实际用户日志的无偏认证；DR 也不在全部误差指标上最好。应分开检验 reward 拟合、下游行为、监督人口和完整构建成本，不由有限安全 judge 分数推出真实安全或 helpfulness 保持。支持、噪声或补全无法验收时，保留 Unknown、受控人工偏好与独立行为评价，而不是把无反馈当负面或用历史参与度批准发布。

## 静态注 PRE

- `SF-2026-ARXIV-2603-18736` — [CausalRM exact-v1](https://arxiv.org/html/2603.18736v1) §2.2–4.7/Eqs4–17/Alg1/Tables1–5与必要A/B；只采用噪声/观察选择两通道校正及条件/费用分责。合成median proxy、anchor/positivity与正确噪声率前提、DR方差符号/误差条件、Alg1 θ/ζ身份差异和独立下游评价保留；不授真实用户因果无偏、总是降方差或普遍安全，未核实现/复现。

## 非准备者必要 Source / actual owner / PRE：正式有限通过

resume_mar18在本21独立恢复合同后，实际exact-v1 §2.2、§3.1–3.4/Eqs4–17/Alg1，§4必要数据构造、Tables1–5及4.3–4.7/Limitations，A Theorems1–3/bias与variance推导、B数据/冻结MLP/GRPO配置；actual Ch31完整76–125与153–185及Ch30/32开篇，逐字核原两PRE和静态注。Source/sole TRAIN-RLHF差额/PRE正式有限PASS；已有WildReward119保留Unknown与标签出处，隐私121有已知扰动通道，却没有反馈选择与标签翻转联合校正/anchor支持域/DR不豁免noise条件，插两段连接顺读成立。2+2+2=6是该联合接口差额，不给成熟IPS/DR本身新分。

实际独核确认Alg1 extrema用ζ但ρ用θ、A Theorem2逐样本surrogate imputer条件与一般x-only模型不等、Theorem3正文不等号和降方差叙述方向相反，proof正性也不能覆盖负surrogate；均不作为可执行配方或普遍保证。以ρ01=.2、ρ10=.1、预测1且观察标签1的MSE为例，surrogate为−.2/.7<0，故不能由非负原始MSE推imputer普遍正。正确noise/支持域和观测条件仍必要，未由因果名称授任意MNAR/hidden-user识别。Table1 DR在多项MAE劣于IPS、synthetic median proxy与独立test oracle并非真实用户logs、主文/B LR下界差及有限judge/20step行为评价，原PRE反侧均保留。

限定采用两观测通道与校准/费用/Unknown回退可独立于这些中心外推，原两段与静态注不需改；待root唯一Ch31窄写后一次非writer actual正文/完整邻接/本人注POST，未计safe/DAY，未核实现/复现或遍无关附件。

## 非 writer actual POST：正式有限通过

resume_mar18实际顺读Ch31完整109–141：强度/有序监督→WildReward→新121/123两段→隐私通道→score例子，以及末九行本人1481静态注/全部邻注，逐字回对两PRE/有效Source，actual POST正式有限PASS；唯一marker/静态注各一处，限定diffcheck空。总体观察与噪声校准条件、proxy合成、DR非所有MAE最佳、费用/Unknown及独立行为评价均近文，未将原公式矛盾写成可执行recipe或真实用户无偏/普遍安全。未改变其他family，不需递归改静态注身份；仅单项I安全，尚非整日DAY。
