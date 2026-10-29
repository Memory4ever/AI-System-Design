# 第十六包：轨迹截断、奖励/模仿共源与双学习者交接

完整PRE/具体NC，未SAVE。适用Books上下文/ROADMAP有效；本轮actual Ch33组条件/allowed-set、EAD完整段/marker、ArenaRL两完整段、长度截断两完整段及DAPO全部四项/解释已读；Ch26完整课程/RE-GoT与OnlineRL前后、SynthDemo/SimpleVLA/预测reward、BC-Q仲裁两完整段及后normalizing-flow完整段已读，Ch25/27、32/34交接有效。必要/key沿R8/R18–19/R43/R54，不第二Methods/代码/复现。三个独立gap，不全章锁。

## 12264 T3 / 2+2+2=6 / TRAIN-GRPO Ch33

消费R18/19 §2/3.1/3.2/3.3.3与C3首次必要。现长度截断两段用已采正确长度选择预算，没有**内部belief-deviation proxy提出截断与terminal信用仍分开**；理论fixed latent/error-growth等假设不授真实停滞已进入吸收域。唯一插位在完整SF2603-17449有限截断对照第二段/inline marker后、完整`长度预算也可先用于构造训练起点...`前。未闭的截断答案/bootstrapping不补recipe。

正文：

轨迹预算也可由内部状态变化提出，而不只看已生成长度：在训练中以belief偏离或变化的proxy选择保留前缀/截断位置，尝试减少末段漂移对信用的污染。[受限belief截断分支](https://arxiv.org/html/2510.12264v1#S3)的停止信号不是正确性标签，内部停滞也不自动满足理想latent模型的吸收域条件；不同任务里集合收缩、judge-unknown或oracle向量相似又是不同信息权限。Sensor/参考状态、任务与policy版本、实际保留前缀、terminal verifier、mask和归一化须共同保存；截断后的答案从何取得、如何给终奖或bootstrap未闭时，不据此给出可执行训练配方，更不能让训练oracle变成部署自知。随机截断亦可改善、较强阈值也会退，不能把全部收益唯一归于belief机制。全部原轨迹生成、状态测量/奖励、被丢后缀、选参和独立质量回归均付费；信号、信用或净质量失配时，保完整rollout、明确的长度buffer/原outcome训练，不由短前缀或理论势函数批准必要推理全保、无偏更新和通用token节省。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12264 -->`

本人末注：

- `SF-2025-ARXIV-2510-12264` — Herschel，Daily2025-10-16补Oct15；消费Cicero R18/19 exact-v1 §2/3.1/3.2/3.3.3/C3首必要，2+2+2=6，仅belief proxy截断与terminal信用/信息权限分责差额深入。保fixed latent/error-growth假设、集合/judge/oracle不同角色、k9/随机截断反侧、未闭答案/bootstrapping与全费，不采吸收域识别/部署oracle/精确recipe。未第二Methods/代码/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12710 Reflective VLA / 2+2+2=6 / MULTIMODAL-EMBODIED-VLA Ch26

writer III/IV必要/R54 key已成。现RE-GoT完整段修订奖励图，SynthDemo先给独立成功checker示教，未承担**失败视频构造reward后同reward再筛成功SFT buffer，锚与被锚目标共源**。插在完整RE-GoT段/独立SF2509-16136 marker后、OnlineRL标题前；上方人工阶段奖励完整段/marker与下方OnlineRL核心完整两段已读。

正文：

失败反馈也可同时进入奖励构造与后续模仿人口：先由视频反思在既有primitive和物理log支持内生成结构化reward，再用同一reward及步长proxy选择成功轨迹作SFT，与RL更新交替。[受限反思训练分支](https://arxiv.org/html/2510.12710v1#S3)中的SFT并不是独立真实安全锚，因为它仍继承奖励库、筛选器与课程环境的共同偏差；去SFT失败只支持该消融风险，不证明保留它就全局aligned。视频/特权log、reward程序、环境revision、buffer准入和动作policy须共同绑定，分别验reward有效性、模仿人口和真实任务，不能由高reward轨迹自己签监督真值。负值幂与损失方向未闭不补PPO/CE recipe，较低成功时简化环境也改变训练支持，有限仿真不授实机。全部反思调用、改环境、成功和失败rollout、buffer/SFT/RL与独立闭环回归均付费；奖励、支持或质量失配时，保可信任务reward、真实示教/原policy和独立controller，不由更强自反思批准无hacking、物理安全和免费适配。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12710 -->`

本人末注：

- `SF-2025-ARXIV-2510-12710` — Herschel，Daily2025-10-16补Oct15；旧反侧与本轮exact-v1 III/IV必要、Cicero R54 key，2+2+2=6，仅failure反思reward/同源成功SFT人口的双消费者差额深入。保primitive/physical logs、简化课程、Q^.6及PPO/CE方向未闭、去SFT0非保SFT全alignment、83.6<85.5与全费，不授实机安全。未核实现/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12560 CoIRL-AD / 2+2+2=6 / MULTIMODAL-EMBODIED-VLA Ch26

writer §3/4/5/A1.1必要/R43key有效。当前BC-Q/RL-Q是逐状态value仲裁部署动作，不承担**共享perception下IL/RL双actor周期比较proxy，winner参数soft/hard转给另一方**。唯一插位完整BC-Q仲裁两段/独立SF2605-05172 marker后、完整`当更新目标确实需要action likelihood时...`前；上下完整对照/normalizing-flow段已读。只这份训练交接，不采全step-aware更新式或真实驾驶安全。

正文：

模仿与RL还可在训练期互相提供候选参数，而不只在部署时由gate选动作：共享感知，保留两份actor，按周期比较各自proxy回报，以soft或hard方式把较好者的actor权重传给另一方。[受限协同训练分支](https://arxiv.org/html/2510.12560v1#S3)把学习路径、比较器与权重交接分开；proxy赢家不等真实环境更好，共享表示也让两路错误相关，不能把一次复制称独立纠错或行为无损。两actor/共享encoder、reward、比较人口/时钟和传递系数须共同保存，另验新旧任务；latent world-model提供的未来value仍是预测，读取提出的waypoint也不是看到真实未来。混合采样/完整logprob及计数归一未闭时不补无偏policy-gradient recipe，顺序训练或纯RL反退也不独证某一个交接规则。全部IL/RL预训、world-model/critic、双actorrollout、选择和独立真实回归均付费；proxy、表示或净质量失配时，保独立IL/已验RL、停止传递并回原policy/controller，不由同部署架构或更高模拟均分批准零额外训练和道路安全。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12560 -->`

本人末注：

- `SF-2025-ARXIV-2510-12560` — Herschel，Daily2025-10-16补Oct15；exact-v1 §3/4/5/A1.1必要与Cicero R43 key，2+2+2=6，仅shared perception/IL–RL两actor、proxy winner参数传递/imagined critic分责差额深入。保特权/waypoint非未来观测、stepaware/logprob/计数未闭、SSR/LAW/navsim反退及全费，不采单组件唯一因果/实路安全。未核代码/复现；整体PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## 12211 ReRe / 2+1+2=5 / TRAIN-GRPO Ch33具体NC提案

消费R8 §3.1–3.2/4.1–4.2首次必要，只合法item/重复和invalid负例、beam生成下rank reward与真实consumer分责；保beam非原policy独立无偏rollout、语义/协同reward增而NDCG可退、Qwen0.5B/8H20/2epoch/G16/B512和全费。actual Ch33 allowed-set完整段SF2602-16833共同绑定候选集合/合法性/parser/采样policy，合法样本非原未约束人口；ArenaRL完整两段SF2601-06487把rank差分与真实质量间隔、candidate/judge/ties和完整费用分开；EAD完整段SF2510-05251另要求behavior采样law/target/mask/比率身份，截尾不能授精确消偏。实际已承担本次稀疏失败差分/合法候选与消费者验收，不把Arena tournament说成本文beam算法，不采用其未核精确RL推导；拟NC，不写段/marker/注。

请sole reader整体审三完整原文/独立marker/本人注和一具体NC；尚未SAVE/不预POST或日级，普通工作继续。
