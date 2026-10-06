# 第十批有限余项必要 core

只既有 v1 题摘集合。root 实际准入/Source 待核，不授 Books 锁、不计正式候选；其余附件到具体命题即止。

## 00923 CogSym：拟 2+2+2=6

[v1](https://arxiv.org/html/2604.00923v1) Methodology/Results/Limitations：Llama2-7B、Javanese/Sundanese GoogleTranslate Alpaca52K、1epoch/seed42/AdamW8bit/b16/bf16，word translation/COMET/sentiment/primary-school IndoMMLU；front 更新 embedding、rear 更新 LM head，CogSym 两者都更新而 k 不计这些层。前后层任务方向差异是有限层选择资格，不把 sweep 当相同全部 trainable 参数数或脑区因果证明。8/32 outer layers 加两端模块局部近 full FT，position inward 变差，FIM comparable、LoRA r128 同模式；无需再做 FIM 是选择器费用，不是完整 forward/backward 降75%测证。sequential memory50% 为文中估计，rear-first 对生成约退10%，先前 region 保持不保证；中层数学/推理、其它语言/架构尚未验证。拟采用是 adaptation task 方向与 layer/embedding/head 冻结边界，非人类脑类比。

## 00938 WARP：拟 2+2+2=6，正式保证纠错必要深入

[v1](https://arxiv.org/html/2604.00938v1) §3.2–3.5/4.1–4.3、Alg1/B.1–B.3：只分类 head 前 dense，先前 v(x) 固定；GSN 小时 auxiliary-disjoint FT 可改 repair weight/bias 和 head，随后 QP 只改 W。top-r left singular basis更新、最小范数+repair slack、remain linear constraints，并每轮真实 repair margin 检查；GSN/feasibility 与真实验收差额可采用，不把成熟 QP+SVD 本身计新机制。Theorem3.1 是通过停止条件的有限样本保证，3.2/B.2 把 first-order 近似等同 true gap，Remark3.1 承认高阶误差；Table5 SST2 remain margin 798/800、786/800 而非全满足，仅仍正确。证书在修复层 representation v 的 L2 球，不是原文本/token 输入或全网络保证。Eq12把 logit-composition Lipschitz写成 gap bound 未处理 competing-row 差，故不逐字授该 gap 常数；radius 另带2不能仅凭这一处宣判所有 radius 无效。BERT/DistilBERT 两 binary tasks、rank2/3072variables、repair47–108/remain200–800；SST2 general91.4/92.7% <同层LoRA97.5/98.0，RTE83.8/86.2% <原99.2/99.0。多轮SVD/GSN-FT/QP全部费用，不将 polynomial 当高效生产。需要 root 决定有限 repair feasibility/验收命题能否进入正文，不能替作者补全全域定理。

## 01151 multi-agent collusion probe：拟 2+2+2=6，安全反侧深入

[v1](https://arxiv.org/html/2604.01151v1) §3.1–3.3/4/Table1/4.4：Qwen3-32B 4bit/twoA5500，四 agents、两个 secretly instructed colluders；Core50场景/17域，Transfer36对、Stego20对。公共激活26–30层、最后 token；Core平均讨论轮、其它 final-round，不能当相同传感器过程。deception logistic direction+sorted/PCA或max/split/variance/cosine，具体 collective feature 资格是拟差额；AUROC 排名不是校准/阈值安全gate。剔除4未执行 collusion 的训练场景，label 是指令非执行 truth，control可能emergent coordination；缺 privileged observer 控制，知道暗号不等参与。Transfer best .84，cosine .54且多类<.5，方向不可跨场景固定；Stego高分不证明所有隐写/恶意协作可检。39 matched hands单层token分析仍 preliminary、heatmap schematic，不声称真实像素/因果定位。攻击者适应 monitoring 未测，闭源无whitebox权限；可采用群体结构与部署 observer合同，不采 universal collusion detector。

## 01152 Brainstacks：拟贡献前 EX，保留零遗忘负侧供独核

[v1](https://arxiv.org/html/2604.01152v1) §3.2/3.5–3.6/4.1–4.3Tables1/3/4：成熟冻结 additive MoE-LoRA stacks、经验 delta SVD output projection、greedy outcome-labelled sigmoid router 组合。400(另实测200)旧域样本top64(另32)输出方向，仅截断 sampled span；正交新 delta 不授非线性 downstream 输出不变。旧域 stacks 独占激活时原路径可重现，不等混合路由零遗忘。Table3 projection仍 chat.853→1.778、code.493→1.452等 ungated退步，router无 all-input 保证且固定chat floor.20；Gemma3-12B 200题各项 routed HellaSwag.650<.670、MedQA.350<.385、GSM unchanged。TinyLoRA参数50.5/53.6M非完全等，MoE20.2min>9.5min；1200vs400steps堆stack改善不授同budget。实际局部 routing/outcome收集与冻结恢复虽工程合理，未新增 projection条件/遗忘合同/独立因果机制，拟贡献前EX，不按小模型或访问费用关闭。若 root 判断“几何隔离≠mixed-route输出保证”的原反侧足够新学习修正，可仅定点重开这一命题；不自动以 broad zero-forgetting headline取5分。

## 停点

四项必要原证到拟采用/关闭判断即止。最后仅 01161 shift 与 01170 ORCA 两项必要 core；00199 首公开精确日仍孤立，不扩年份或 revision史。
