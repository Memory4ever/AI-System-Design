# 11219 Senna-2：必要 Source 与实际 Ch26 两段 PRE

mar14_supplement；精确[2603.11219v1](https://arxiv.org/html/2603.11219v1)本地`SUP_NECESSARY_11219.raw`，UTC/200/bytes见`SUP_NEXT_SOURCE_MANIFEST_RESULT.json`。root完整AB准入已核，十一作者/仅v1/Comments项目page，未识别具名先公开或当前纠错说明；Mar13官方日级夹证`SUP_DATE_SECOND.md`/`SUP_DATE_11219.raw`，v1Wed18:33:49UTC晚于截止，owning/findable同日注册，不单用submitted/registered。只审本精确版本，不遍历旧Senna或项目历年。

## 实际必要 Source / 评分

实际§3全必要Eq1–10、§4.1–4.3/Tables1–5、直接§5 limitation；A1的Stage2/3运行配置和A2 f_K Eq11–18完整。支持与关键反侧已够，不展开NAVSIM每项/全部定性video或代码。**2+2+2=6标准最低**：新增是behavioral categorical consistency的梯度选择与bottom-up pseudo-target接口，不给已有adapter/DiT/LoRA/RLVR数学加分；Reach2实际跨高层VLM语义与低层planner监督；Durability2是受限projection与真值分责。实际owner差额下必要深入所读内容，不自授PRE/Books/DAY。

Qwen2.5VL-3B输出speed/direction meta-actions，MLP将hidden与两个decision embeddings供E2E DiT AdaLN条件化；低层另有multi-view时序/perception条件，不是高层文本唯一actioninput。初训freezeVLM并训adapter/E2E，Stage2仅当C=1[f_K(predtraj)=VLMdecision]为0时使用expert trajectory+expert decision监督；Eq5对一致样本的这项loss为0，**不照录prose自reinforcing等同显式新强化loss**。A1先2步DDIM取预测，VLM LoRA而其它全参更新，不是无训免模型执行。

Stage3在3DGSrollout上由TTC<3s/慢于expert&限速的两个proxy判定，对相邻trajectory point配stopgradient推动纵向收缩/伸长，低层refined轨迹再经f_K作为high-level NLL target；不是完整onpolicy unbiased policygradient或已验证真实道路reward。碰撞后frames删除、每四帧取一，teacher target/population改变需保存。论文叫HRL不让它继承GRPO/真实safety guarantees。

f_K速度用前1.5s/0.1s离散轨迹、w5滤波及加速度阈值，unknown速度忽略；direction在匹配时将turn-left与lane-change-left合并，right同理，yaw/lateral thresholds按speed缩放。这种coarse分类同一不保证细轨迹、lane语义、舒适或环境安全，也不能让两个模块共同犯错被label一致掩盖。

Tables1–5关键反側：Stage1 FDE.567/F1.701/AFCR.144；加Stage2 FDE.575（更差）/F1.764/AFCR.118；加Stage3 FDE.597（再退）/F1.760（较Stage2退）/AFCR.077。因此不是纯提高所有openloop或一致性，安全proxy与拟合精度取舍明确。约10000h真实expert demonstration，但closedloop是1300片段重建3DGS（1044train/256test）、openloop100h slice，未认证真实部署collision率。128 L20的Stage2 batch384/5ksteps、64L20的Stage3 batch128/500steps与重建/online rollout成本保留；wholepipeline实际wallclock/precision/重复seedCI/线上SLO未充分披露，无artifact核验/复现。

§5直接限制VLM在edge达不到10Hz，实际异步memorybank缓存features；模拟loop10Hz不能充高层实时deadline或传感新鲜度认证。来源没有公开完整cache-age/controller安全协议，不替作者补实现。

## 实际 owner 差额

ROADMAP `MULTIMODAL-EMBODIED-VLA`/Ch26。实际连续155–179 VLM-conditioned controller、254–288 action-facing gradient authority、691–703语义保存/表示对齐完整节与前后、1085–1112 Wrong but coherent/failure局部。Ch25环境transition与Ch27训练数据只交接，不转移policy训练owner。已有同observation表示对齐/teacher anchor，但没有**从预测trajectory经粗分类比较高层意图来决定谁接受expert梯度**，以及低层refined trajectory反向形成高层监督target的behavioral分支。Wrongcoherent现已要求环境verifier，故不重复新造泛安全章节；只把该条件放在新训练接口附近。

拟放Ch26“从只学Action到同时保存语义并对齐语言与动作”节，现teacher+代价三段之后、低数据语言steering分支之前，待root实际Source/PRE与窄锁。原teacher与pureBC合理性、runtimecontroller不动；两段如下。

## 逐字两段提案

表示接近不保证低层轨迹兑现了高层意图。一个行为侧分支可以先把预测轨迹投影为有版本的速度、方向类别，再与高层决策比较；不一致时同时用expert轨迹和expert类别纠正两层，一致时跳过这项外部监督。这里的projection只提供训练样本选择，不能因两层一致就授予正确或安全标签，也不能把“跳过loss”称作一次新的强化更新。在受限的驾驶接口中，转弯和变道被合并到同一方向类，未知速度类还会被忽略；保留mapping阈值、预测轨迹、粗细类别和被筛选人口，才能知道一致性改善究竟覆盖了什么。直接BC和连续表示对齐在明确示教与稳定动作schema下仍然更简单。

闭环训练还可反向传递监督：先按环境proxy修正低层轨迹，再把修正后轨迹的类别作为高层目标。这让高层适应低层可产生的行为，却会把proxy、投影和低层错误共同带进新标签，不能替代独立环境verifier或运行时safety controller。[有限的双系统对照](https://arxiv.org/html/2603.11219v1)中，加入后一训练阶段降低了模拟器的at-fault collision，但open-loop位移误差与类别一致性仍有反退；重建环境、配对预测、筛选、两层更新及online rollout均付费。高层在edge未达到10Hz、实际靠异步feature缓存也说明训练对齐不等于实时协同：部署仍须另验feature年龄、controller期限与真实闭环结果。projection、proxy或时序不可核时，保留原示教路径、短动作与独立低层检查，不由内部F1批准物理行动。<!-- source-family:SF-2026-ARXIV-2603-11219 -->

Review note拟：exactv1 §3/Eq1–10、Tables1–5、A1 Stage2/3+A2、直接limitation；root Source/PRE通过后实际窄写、非writer POST待实际。只采behavioral alignment/选择接口，不授GRPO式无偏、实际道路安全、实时SLO、代码核验或复现。
