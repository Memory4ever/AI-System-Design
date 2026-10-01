# 2604.23584v1：视觉证据去身份化的有界准入与保证核查（作者侧）

本页只处理本 family 的贡献歧义与中心安全主张，不改变 04/28 正式分母、评分或 Books 状态。来源为 [官方 exact-v1 HTML](https://arxiv.org/html/2604.23584v1) §3.3–3.4、§4–5、§7.2–7.4、§7.6；MINE 原始方法见 [Belghazi et al., ICML 2018](https://proceedings.mlr.press/v80/belghazi18a/belghazi18a.pdf)。当前 owner 对读为 Ch72《隐私检测是 Policy-bound Sensor》正文，以及 Ch76 对 RAG evidence identity、权限与 reader handoff 的正文；旧 V2.1 的 `No Change` 不作本轮事实结论。

## 准入命题与真实差异

完整题摘提出的有意义系统选择是：检索得到的图像有人脸时，整图删除或模糊会损失 gaze/pose/expression 等任务证据；作者将检索后、reader 前的人脸改写为 identity-code 替换，同时保留 spatial attribute code，并分别测人脸识别可重认率与下游视觉问答。Ch72 现有文本匿名化 policy 已区分 privacy/utility 与 attacker model，Ch76 已有 evidence provenance/授权，但两处没有具体说明**生成式视觉去身份化不能自动继承原图的证据身份和真实性**。因此不因局部视觉任务标签前关；若最终保留，primary 应是 Ch72 的隐私 release gate，Ch76 只交接原图/生成图 provenance 与 reader 重新验证。此处仅是作者侧准入理由，尚无独立 owner 判定或共享正文授权。

## 中心保证不能正面采用

1. §3.3 Eq(2) 称所用 MINE learned critic 给出 `I(z_id;z_attr)` 的 *variational upper bound*。MINE 原始 Donsker–Varadhan 形式给固定 critic 的是互信息下界；将该估计训练得小，不能凭此证明真实互信息小。§7.2 Assumption 1 又直接假设真实 `I(z_id;z_attr)≤ε_dis`，DCI/MIG 诊断不是该上界的证书。此项不否定经验性解耦训练，但不许把 loss/diagnostic 当隐私证明。
2. §3.4 的 proposal 先从 gallery 独立抽样，再按与**原身份**的 cosine 阈值拒绝；§7.4 Theorem 4 的关键一步却把“原始 proposal 独立”换成“接受后的 `z′_id` 独立”，令 `I(z_id;z′_id)=0`。这是不同随机变量。最小反例：原身份均匀取正交单位码 `e1/e2`，gallery 独立均匀取同两码，阈值 `τ=0.3`，拒绝同码、接受异码；接受后的码恒为原码的另一项，故 `I(z_id;z′_id)=1 bit`。属性码恒定，满足 Assumption 1 的 `ε_dis=0`；生成图显示替换身份、语义距离只衡量非身份属性，仍可满足 Assumption 2，却有 `I(z_id;I_safe)=1 bit`。该离散例用于反驳 Theorem 4 所称“拒绝后按构造独立”；Theorem 4 未将 Assumption 3 的连续 gallery 前提列入自身条件，不把它外推成所有实际人脸生成器的攻击成功率。§7.4 Remark 1 自承认拒绝引入 coupling，却只称其可忽略，不能补回 Eq(11) 不含附加项的严格 `≤ε_dis`。依赖该式的 §7.6 Corollary 7 也不能只检查 encoder residual 就声称达到目标隐私。
3. §4–5 的 ArcFace/CosFace/AdaFace、视觉问答和 50-step/4-step 成本是作者受测数据/recognition oracle 下的经验结果。识别器阈值、替换身份 realism、gaze/pose/answer 保真分别是不同验收；它们不证明对未知辅助数据、未测识别器或生成图新事实的普遍不可识别性。4-step LCM 降低推理时延也伴随质量/隐私数字变化，不是免费加速。

作者侧暂拟 `Design Delta 2 / System Reach 2 / Durability 2 = 6`，因中心安全保证受上述构造反例影响，触发**受影响部分深入审阅与争议隔离**。暂不把该稿标成实际 Books Existing/Integrate，也不否定其局部经验。非作者须核：反例对 theorem 的假设适用性、Ch72/76 实际增量是否值得正文、当窗 v1 公告与同族更早全文。若无独立支持，Books 保持暂缓；可用机制与实验在报告中窄记，不采用“信息论零泄漏”。
