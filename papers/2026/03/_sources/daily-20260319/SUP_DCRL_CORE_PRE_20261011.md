# DCRL16223：必要原证、实际 owner 与受限 PRE

仅本19既有家族；resume_mar17准备，非本日报作者。重载实际AGENTS/研究与Report合同/统一prompt/完整ROADMAP、Sources每日与主题说明、19README/STOP及LS路由。准入2+1+2=5保持；日期复用本日SUP_LATER_METADATA中精确v1与arxiv.content findable夹证，Submitted不作公开时刻，不扩发现或下一日。当前[官方事件页](https://arxiv.org/abs/2603.16223)只有v1/10pages说明，未见影响采用命题的撤回或勘误；不据此证明全站无纠错。

## 必要原证与直接反侧

实际[精确v1 HTML](https://arxiv.org/html/2603.16223v1)§2–3、Eq1–15/Alg1/Tables1–3，A.2–3、C.1–2/Tables5–6及D.2–4。未审完整代码、全图像/曲线拟合或复现实验；已足够判断受限接口，不遍无关附件。

§2.1/Eq4–6每轮复制当前policy，按anchor轨迹token的clipped概率做一次负log(1−p)下降，形成临时explorer；原policy不直接承受此unlearning更新。两者各生成G条同prompt轨迹，按最终答案频率的harmonic分数选伪标签；这是同源参数的受控扰动，不是独立模型或独立真值。有限样本仅一侧出现的答案harmonic为0；双路均缺正确答案时不能凭聚合创造支持。

§2.3/Eq15区分共识提案与梯度准入：低anchor一致率时explorer仍参与伪标签，但其轨迹不参加policy梯度；高时合两集合。这是具体接口增量，但正文用滑窗平均、Alg1 line9用即时rho；T4写更新样本16而Eq15高时可合32。§2 GRPO分母仅写pi_old，未明确explorer轨迹的行为策略/importance ratio桥。因此不签发精确sampling/update recipe或无偏保证；保留当前policy/copy/行为分布与两个集合身份是工程推断。

Eq12对伪标签给1、另一anchor多数给.5；原文说保留奖励避免负advantage不普遍成立：奖励组(1,1,1,.5)均值.875，.5样本优势分子为−.375。该反例只驳非负保证，不否认局部保守奖励实验。

D定理假设正确答案更耐受unlearning，却未证明token抑制会辨识真/假，也未约束所有其他答案。独立归一反例按(sp,true,other)：p0=(.9,.001,.099)，p1=(.000001,.001,.998999)，均和1；sp被强压、true保持，r_true=1≫r_sp≈1.11e−6，但harmonic约(2e−6,.001,.18015)选择第三错误答案。即便sp趋零，也不能从仅true>sp推出true全局argmax。共享偏差、有限G及零交集不授全局纠错/连续自改进定理。

§3在DAPO-Math-14k两epoch、3模型与TTA上评测；Pass@1为每题16次采样平均，不是16个独立训练seed。T1部分任务低于其他label-free baseline，且8B均值50.9未追平gold GRPO53.5；T3去harmonic的GSM8K更高、去保守reward的MMLU更高。T5过大unlearning LR实际失败；T6合池多数投票明显更差，支持“扰动与聚合不可混为多采样”而非普遍提升。TTA是在目标benchmark上适配，不是未见人口独立迁移证书，也不采‘免过拟合’。T4各16意味着提案至少两轮rollout加copy反向更新；同两epoch/超参不等同token、训练或墙钟预算，GPU/数值精度/全費及训练重复不确定性在已读范围Not Disclosed，未核artifact不授生产降本。

## actual owner 与差额

sole `TRAIN-GRPO`，actual Ch33完整715–783：730–739已拥有group相关误差与majority无法消共偏差，741–755有有效gold/噪声结构与可信独立检查，762有TTRL数字parser不认证完整行为，764后独立verifier更新/authority。尚未拥有“临时扰动copy只作伪标签提案，提案集合与真正梯度集合可分离”的具体控制分支。Ch31完整440–463的majority sharpening/mode extinction与历史伪标签不是此同轮copy接口；Ch32开篇行为旧策略ratio、Ch34开篇离线偏好合同已对齐，不新增第二owner。建议在Ch33当前762后/764小标题前单段，保留旧可信verifier与独立采样分支。

## 逐字 PRE（待 root 非准备者核验，未授 Books）

共识奖励还可以先改变提案分布，而不是把更多同源回答当作独立核验。一个[受限双路分支](https://arxiv.org/html/2603.16223v1)每轮复制当前policy，在副本上临时抑制已采轨迹的token概率，再用原policy与扰动副本的答案频率共同提议伪标签；副本没有获得外部真值，其暂时更新也不直接写回原policy。参与共识的轨迹与进入policy梯度的轨迹是两份集合，后者须保留实际行为策略和准入身份，不能把提案认可自动当作可直接训练。双路仍可能共同出错，单侧缺席的有效答案也可能被共识筛掉；伪标签必须接受独立outcome切片检查，而不是由扰动耐受性自证正确。副本构造、额外rollout、临时反向更新、聚合与回归均计费，局部改进不授普遍纠错、无偏更新或更低总成本；扰动损伤能力、准入语义未锁定或质量回退时，保留原checkpoint、可信外部verifier与预算匹配的普通采样。<!-- source-family:SF-2026-ARXIV-2603-16223 -->

静态注：`SF-2026-ARXIV-2603-16223` — [v1](https://arxiv.org/html/2603.16223v1)§2–3/Eq1–15/Alg1/Tables1–3、A.2–3、C.1–2/Tables5–6与D.2–4。仅临时copy的共识提案与梯度准入分离、同源偏差和全费用边界；未采全局true-selection定理、非负advantage或精确更新recipe，未核代码/复现。

## 未采用主张及一次精确重开请求

### root 非准备者 Source / PRE 裁决

其后resume_mar17按原PRE实际写Ch33新766及本人静态3194；root非writer实际回读745–790完整相关噪声→格式准入→新双路提案→Verifier更新段落、末九行EGCA/DyJR/本人注并回对原PRE与必要原证，actualPOST通过。一段一注，不采中心理论/未闭合配方；Ch33窄锁已释放，可计本家族受限整合安全，不授日级DAY。该记录覆盖下方历史“尚待”表述。

root 实际复查 exact-v1 §2/Eq4–15/Alg1，§3.1–3.3/Tables1–3、Limitations，A.2–A.3、C.1–C.2/Tables5–6及D.2–D.4；读足本段采用接口与决定性反侧，不核全图、代码或复现。复算第三答案harmonic约.18015>.001及reward .5低于组均值.875；这些反侧确实限制全局正确性和非负优势，不妨碍采用临时copy的提案/梯度两集合分离。实际Ch33 705–790的相关错误→独立gold→格式门→更新权威路线与本PRE匹配，具体接口不是仅同主题已有覆盖。2+1+2=5及受限逐字PRE通过；作者未采用的理论、16/32配方、行为ratio和全费用保证仍隔离，未通过那些主张。待协调Ch33窄写后，仍须非writer检查实际正文/完整邻接/本注，不授DAY。

局部接口可供独核，但D全局正确性与recipe一致性不因PRE保守表述获得验证。只请求一次：所有候选的harmonic严格排序/有效假设或勘误，体现共享错误与正确答案缺席的有限G受控trace；滑窗/即时rho和16/32实际准入、copy生成策略与likelihood denominator的最小执行说明；同人口/质量/总token与copy更新预算的独立对照及训练重复不确定性。可由具名勘误、最小可检artifact或受限条件证明替代，仅重开上述未采命题；不降分、转EX或将主题覆盖冒NC，不支持正面普遍纠错/性能保证。当前Source/PRE尚待root非准备者，未写未POST，不计安全完成或DAY。
